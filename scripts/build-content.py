#!/usr/bin/env python3
"""Render Still Alight's public Markdown content as standalone static pages.

Run from any directory: python website/scripts/build-content.py
Uses only Python's standard library. The deliberately small renderer supports
the content's headings, paragraphs, quotes, lists, tasks, tables and inline
formatting. Raw source HTML is escaped, and local Markdown links are validated.
"""

from __future__ import annotations

import html
from html.parser import HTMLParser
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit


WEBSITE = Path(__file__).resolve().parents[1]
CONTENT = WEBSITE / "content"
PUBLIC = WEBSITE / "public"
PAGES = {
    "privacy": ("Privacy Policy", "How your information is handled."),
    "terms": ("Terms of Use", "The details of using Still Alight."),
    "support": ("Support", "A little help with your candle."),
    "delete-data": ("Delete your data", "Your content, and how to remove it."),
}
LEGAL_ROUTES = ("privacy", "terms", "support", "delete-data")
LIST_ITEM = re.compile(r"^\s*(?:(\d+)\.|([-+*]))\s+(.+)$")
HEADING = re.compile(r"^(#{1,6})\s+(.+)$")
TABLE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")


def local_link(target: str) -> str:
    """Preserve safe external links; turn source Markdown names into routes."""
    target = html.unescape(target.strip())
    parts = urlsplit(target)
    if parts.scheme:
        if parts.scheme not in ("https", "http", "mailto"):
            raise ValueError(f"Unsupported link scheme: {target}")
        return target
    if target.startswith("#"):
        return target
    if parts.netloc or parts.path.startswith("/"):
        raise ValueError(f"Use a content-relative Markdown link: {target}")
    if Path(parts.path).suffix == ".md":
        slug = Path(parts.path).stem
        if slug not in PAGES or not (CONTENT / f"{slug}.md").is_file():
            raise ValueError(f"Unknown content link: {target}")
        return f"../{slug}/" + (f"#{parts.fragment}" if parts.fragment else "")
    raise ValueError(f"Unsupported relative link: {target}")


def inline(source: str) -> str:
    """Render inline Markdown while keeping literal HTML safely escaped."""
    result = []
    position = 0
    while position < len(source):
        if source[position] == "\\" and position + 1 < len(source):
            result.append(html.escape(source[position + 1]))
            position += 2
            continue
        if source[position] == "`":
            end = source.find("`", position + 1)
            if end != -1:
                result.append(f"<code>{html.escape(source[position + 1:end])}</code>")
                position = end + 1
                continue
        if source.startswith("**", position):
            end = source.find("**", position + 2)
            if end != -1:
                result.append(f"<strong>{inline(source[position + 2:end])}</strong>")
                position = end + 2
                continue
        if source[position] == "*":
            end = source.find("*", position + 1)
            if end != -1:
                result.append(f"<em>{inline(source[position + 1:end])}</em>")
                position = end + 1
                continue
        if source[position] == "[":
            label_end = source.find("](", position + 1)
            if label_end != -1:
                depth = 1
                target_start = label_end + 2
                target_end = target_start
                while target_end < len(source) and depth:
                    if source[target_end] == "(":
                        depth += 1
                    elif source[target_end] == ")":
                        depth -= 1
                    if depth:
                        target_end += 1
                if depth == 0:
                    label = inline(source[position + 1:label_end])
                    target = html.escape(local_link(source[target_start:target_end]), quote=True)
                    result.append(f'<a href="{target}">{label}</a>')
                    position = target_end + 1
                    continue
        result.append(html.escape(source[position]))
        position += 1
    return "".join(result)


def paragraph(lines: list[str]) -> str:
    pieces = []
    for index, line in enumerate(lines):
        pieces.append(inline(line.rstrip()))
        if index < len(lines) - 1:
            pieces.append("<br>\n" if line.endswith("  ") else "\n")
    return f'<p>{"".join(pieces)}</p>'


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def slugify(text: str) -> str:
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "section"


class Markdown:
    def __init__(self) -> None:
        self.sections: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.table_count = 0

    def unique_id(self, title: str) -> str:
        base = slugify(title)
        result = base
        count = 2
        while result in self.ids:
            result = f"{base}-{count}"
            count += 1
        self.ids.add(result)
        return result

    def render(self, source: str) -> str:
        lines = source.splitlines()
        output = []
        index = 0
        while index < len(lines):
            line = lines[index]
            if not line.strip():
                index += 1
                continue
            heading = HEADING.match(line)
            if heading:
                level, title = len(heading[1]), heading[2]
                identifier = self.unique_id(title)
                if level == 2:
                    self.sections.append((identifier, title))
                output.append(f'<h{level} id="{identifier}">{inline(title)}</h{level}>')
                index += 1
                continue
            if line.startswith("```"):
                block = []
                index += 1
                while index < len(lines) and not lines[index].startswith("```"):
                    block.append(lines[index])
                    index += 1
                if index == len(lines):
                    raise ValueError("Unclosed fenced code block")
                output.append(f'<pre><code>{html.escape(chr(10).join(block))}</code></pre>')
                index += 1
                continue
            if line.startswith(">"):
                quoted = []
                while index < len(lines) and lines[index].startswith(">"):
                    quoted.append(re.sub(r"^> ?", "", lines[index]))
                    index += 1
                output.append(f'<aside class="editor-note">{paragraph(quoted)}</aside>')
                continue
            if index + 1 < len(lines) and TABLE_SEPARATOR.match(lines[index + 1]):
                headers = cells(line)
                self.table_count += 1
                table_id = f"table-{self.table_count}"
                output.append(
                    f'<div class="table-scroll" tabindex="0" role="region" '
                    f'aria-labelledby="{table_id}"><table>'
                    f'<caption id="{table_id}" class="sr-only">'
                    f'{html.escape(" / ".join(headers))}</caption><thead><tr>'
                    + "".join(f'<th scope="col">{inline(cell)}</th>' for cell in headers)
                    + "</tr></thead><tbody>"
                )
                index += 2
                while index < len(lines) and lines[index].strip().startswith("|"):
                    row = cells(lines[index])
                    if len(row) != len(headers):
                        raise ValueError(f"Table column count mismatch: {lines[index]}")
                    output.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
                    index += 1
                output.append("</tbody></table></div>")
                continue
            item = LIST_ITEM.match(line)
            if item:
                ordered = bool(item[1])
                tag = "ol" if ordered else "ul"
                start = f' start="{item[1]}"' if ordered and item[1] != "1" else ""
                output.append(f"<{tag}{start}>")
                while index < len(lines):
                    item = LIST_ITEM.match(lines[index])
                    if not item or bool(item[1]) != ordered:
                        break
                    item_source = item[3]
                    task = re.match(r"^\[([ xX])\]\s+(.+)$", item_source)
                    if task:
                        done = task[1].lower() == "x"
                        symbol = "✓" if done else "□"
                        status = "Complete" if done else "To do"
                        output.append(
                            f'<li class="task-item"><span class="task-status" aria-hidden="true">{symbol}</span>'
                            f'<span class="sr-only">{status}: </span>{inline(task[2])}</li>'
                        )
                    else:
                        output.append(f"<li>{inline(item_source)}</li>")
                    index += 1
                output.append(f"</{tag}>")
                continue
            body = [line]
            index += 1
            while index < len(lines) and lines[index].strip():
                next_line = lines[index]
                if HEADING.match(next_line) or next_line.startswith((">", "```")) or LIST_ITEM.match(next_line):
                    break
                if index + 1 < len(lines) and TABLE_SEPARATOR.match(lines[index + 1]):
                    break
                body.append(next_line)
                index += 1
            output.append(paragraph(body))
        return "\n".join(output)


def legal_links(current: str) -> str:
    return "\n".join(
        f'<a href="../{slug}/"' + (' aria-current="page"' if current == slug else "")
        + f'>{html.escape(PAGES[slug][0])}</a>'
        for slug in LEGAL_ROUTES
    )


def render_page(slug: str) -> str:
    title, description = PAGES[slug]
    source = (CONTENT / f"{slug}.md").read_text(encoding="utf-8")
    source = re.sub(r"\A# .+\n+", "", source, count=1)
    markdown = Markdown()
    body = markdown.render(source)
    contents = "\n".join(
        f'<a href="#{identifier}">{inline(label)}</a>'
        for identifier, label in markdown.sections
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)} Information for Still Alight: 3D Candle by Satzquatch.">
  <meta name="theme-color" content="#171411">
  <title>{html.escape(title)} · Still Alight</title>
  <link rel="icon" type="image/svg+xml" href="../assets/brand/favicon.svg">
  <link rel="stylesheet" href="../legal.css">
</head>
<body>
  <a class="skip-link" href="#content">Skip to content</a>
  <header class="site-header">
    <a class="wordmark" href="../" aria-label="Still Alight home">
      <img class="brand-mark" src="../assets/brand/quiet-flame-light.svg" alt="" width="36" height="36">
      <span>Still Alight</span>
    </a>
    <a class="back-link" href="../"><span aria-hidden="true">←</span> Back to the candle</a>
  </header>
  <main id="content">
    <div class="page-intro">
      <p class="eyebrow">Here to help</p>
      <h1>{html.escape(title)}</h1>
      <p class="page-description">{html.escape(description)}</p>
    </div>
    <div class="document-layout">
      <aside class="document-nav">
        <nav aria-label="On this page">
          <p class="nav-label">On this page</p>
          {contents}
        </nav>
        <div class="nav-divider"></div>
        <nav class="related-pages" aria-label="Help and legal pages">
          {legal_links(slug)}
        </nav>
      </aside>
      <article class="document" aria-label="{html.escape(title, quote=True)}">
        {body}
        <a class="to-top" href="#content">Back to top <span aria-hidden="true">↑</span></a>
      </article>
    </div>
  </main>
  <footer class="site-footer">
    <div><a class="footer-brand" href="../" aria-label="Still Alight home"><img class="brand-mark" src="../assets/brand/quiet-flame-light.svg" alt="" width="36" height="36"><span>Still Alight</span></a><p>A little light. A little room to breathe.</p></div>
    <nav aria-label="Footer">{legal_links(slug)}<a href="https://satzquatch.com/">More from Satzquatch <span aria-hidden="true">↗</span></a></nav>
    <p class="footer-note">Android version 1.0.0. Published by Satzquatch · <a href="mailto:tex@discvault.us">tex@discvault.us</a></p>
  </footer>
</body>
</html>
'''


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("href"):
            self.links.append(attributes["href"])
        if attributes.get("id"):
            self.ids.append(attributes["id"])


def verify_generated() -> None:
    """Check every generated local href, excluding the separately built home."""
    for slug in PAGES:
        page = PUBLIC / slug / "index.html"
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        if len(parser.ids) != len(set(parser.ids)):
            raise ValueError(f"Duplicate heading IDs: {page}")
        for href in parser.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc:
                continue
            if href == "../":
                continue  # Home is maintained by the main site build.
            target = (page.parent / parts.path).resolve() if parts.path else page
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                raise ValueError(f"Broken link in {page}: {href}")
            if parts.fragment:
                target_parser = parser
                if target != page:
                    target_parser = Links()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                if parts.fragment not in target_parser.ids:
                    raise ValueError(f"Broken fragment in {page}: {href}")


def main() -> None:
    for slug in PAGES:
        destination = PUBLIC / slug / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render_page(slug), encoding="utf-8")
    verify_generated()
    print(f"Built and verified {len(PAGES)} static content pages in {PUBLIC}")


if __name__ == "__main__":
    main()
