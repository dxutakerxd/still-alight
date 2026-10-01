# Still Alight

The official startup website for **Still Alight: 3D Candle**, an Android app by **Satzquatch**. The app is being prepared for Google Play.

[Visit Still Alight](https://dxutakerxd.satzquatch.com/still-alight/) · [Privacy Policy](https://dxutakerxd.satzquatch.com/still-alight/privacy/) · [Support](https://dxutakerxd.satzquatch.com/still-alight/support/)

## Website

A warm, candlelit product page with an interactive 3D candle, real Android app screenshots, original rain and fireside audio samples, and accessible Privacy, Terms, Support and data-removal pages.

The candle preview reuses the app's model, wooden lid, coaster and stock label artwork. It supports horizontal rotation, Vanilla/Lavender/Cabin looks, lighting/extinguishing, and reduced motion. Rendering and glass are adapted for the web using Three.js. Sound samples do not autoplay.

## Local development

Requires Node.js 22.12+ and Python 3. No API keys or backend are needed.

```sh
npm ci
npm run dev
```

## Build and deploy

```sh
npm run build
npm run preview
```

The build renders `content/*.md` into standalone HTML pages and writes the complete static site to `dist/`. Legal pages work without JavaScript. Relative asset links allow deployment under a repository path.

The included GitHub Actions workflow builds and deploys pushes to `main` through GitHub Pages. In repository Settings → Pages, the publishing source is GitHub Actions. Each repository builds independently, but a project site inherits any custom domain configured on the account's user Pages site. That domain must have working DNS; the default `github.io` project address redirects to it. See [GitHub's custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages).

## Content updates

- Landing page: `index.html`
- Design: `src/style.css`
- Candle interactions and motion/audio behavior: `src/main.js`
- Public information: `content/privacy.md`, `terms.md`, `support.md`, `delete-data.md`
- Static page generator: `scripts/build-content.py`
- Production assets: `public/assets/`

The information pages describe Android **1.2.0**, the Google demo-ad development build, and distinguish earlier 1.1.1 builds without the SDK. RevenueCat and live ads are not enabled. Before enabling production ads or purchase services, configure applicable consent controls and update the policy, terms and Play disclosures for the final integration. No public Play listing, price or release date is asserted by this site.

Publisher: **Satzquatch**. Support/privacy contact: **tex@discvault.us**.

## Assets and licensing

The approved main identity is Quiet Flame. Reusable SVG symbols, horizontal logos, the preserved SA secondary monogram, and approved imagegen concepts are documented in the [brand kit](brand/README.md).

The background was created with imagegen from the approved Quiet Room concept. The 3D objects, label art, product render and screenshots come from Still Alight. Screenshots include a custom-label example; they are not invented app screens. The sound samples are the app's original synthesized, 24-second, mono PCM loops packaged as WAV files without changing their samples. Delivery images are WebP encodings.

Three.js licensing is included in `public/third-party-notices.txt`. Public source availability does not grant an additional license to the Still Alight artwork or app assets.

The website code does not add analytics, advertising, external embeds, cookies or browser storage. GitHub Pages has its own hosting/security logging, described in the Privacy Policy.
