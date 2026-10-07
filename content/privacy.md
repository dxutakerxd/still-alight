# Privacy Policy

Effective date: **1 October 2026**. This page describes Still Alight Android version **1.2.1 (test-ad development build)**. Earlier 1.1.1 builds do not include the advertising SDK.

Still Alight: 3D Candle is published by **Satzquatch**. In this policy, “we” means that publisher. For privacy questions, contact **[tex@discvault.us](mailto:tex@discvault.us)**.

This policy describes the current Android app, our app website, and messages you choose to send for support. They have different data practices, described below.

## The current app

Candle, label, remembrance, saved audio and wallpaper features work without an account or an internet connection. Version 1.2.1 includes Google Mobile Ads SDK 25.5.0 for development test advertisements. Ads need network access. In this test-ad build, selecting or replacing a custom audio file requires completing a rewarded demo ad; an already saved file and the built-in sounds remain usable offline. We do not operate an app account or cloud-sync service, and the app does not send your candle settings, remembrance names/messages/dates, label content, photos or imported audio to us or include that content in advertising requests. There are no purchases, subscriptions, publisher analytics or remote crash-reporting integrations. Google's advertising SDK has its own data handling, described below.

The app saves information in its private storage so that your choices and creations remain available when you return:

| Information | Why it is used |
| --- | --- |
| Candle style, shape, orientation, glow, sound, wallpaper and accessibility preferences | To display your chosen candle and remember your settings |
| Timer duration, deadline or paused remaining time, candle state and audio playback position | To continue or finish the current session correctly |
| Whether customization test ads are enabled | To honor the advertising switch in Settings |
| Names, personal messages and meaningful dates you enter in Remembrance | To create your remembrance candles and run their local schedules |
| Custom-label text, drawings, layers, drafts, saved designs and generated label images | To let you create, edit and display labels on your candles |
| Images you choose to add to a label | To make a private image copy for that design |
| A photo you choose as a wallpaper background, with its crop and positioning settings | To display your chosen background behind the candle |
| Audio you choose to import, its displayed filename and playback position | To play your chosen sound across app screens and, if enabled, in the background |
| Beat-responsive flame choice and temporary low, mid and high audio levels | To make the flame follow the sound played by Still Alight when you enable that option |

Entering remembrance content and importing files are optional. The app does not read your contacts or your device calendar to fill in remembrance profiles or dates. It does not record microphone audio or take camera pictures.

## Files you choose

Android's file picker lets you choose a specific image or audio file. Still Alight reads that selection and makes a private copy; it does not request broad access to your photo library or storage. Images are processed into bounded-size copies for label editing or wallpaper backgrounds. Imported audio is copied and checked for supported playback, with a maximum file size of 250 MB.

The original file is not edited or deleted by these import features. A private copy can remain usable after the original is moved or deleted. Image selections may come from a cloud-backed provider shown by Android; that provider handles delivery of the selected file under its own settings and practices. The audio picker requests local files. Selecting a file does not give us access to it.

If you enable **Controls → Sound → Beat-responsive flame**, Still Alight analyzes only its selected sound on your device. For imported audio, a compact set of low, mid and high levels is kept in app-private cache to avoid decoding the file again. Removing the imported audio also removes its cached levels. This feature does not use the microphone, capture audio from other apps or transmit your audio levels.

## App storage, security and device transfers

The app uses Android's app-private files and preferences. Access protection depends on Android and your device's security. This is not a promise of a separate encrypted vault or of protection against someone with access to an unlocked device. Labels and remembrance names or messages can also be visible on your screen or live wallpaper when you choose to display them.

Version 1.2.0 disables Android cloud backup and explicitly excludes app preferences, private files, databases, and app-specific external and device-protected storage from Android cloud backup and device-transfer rules. Device manufacturers and independent migration services may behave differently; copies already created by earlier versions or other services are not removed by these rules. Any copies managed by your device or a storage provider are separate from this installed app.

## Optional protected backups

**Settings → Backup & restore** creates an encrypted file containing your remembrance content, labels, drafts, imported images/audio and candle preferences. You choose its password and destination through Android's file picker. The app does not upload backups automatically or send them to us. If you select a cloud provider, that provider stores the encrypted file under its own practices. Keep the password safe: we cannot recover it or decrypt your backup for you.

Restoring replaces current app content after the file is authenticated and validated. Temporary decrypted files are kept in app-private storage during the operation and removed afterward. Restored session timers are stopped and background sound is disabled. Deleting app data does not delete backup files you exported; remove those through the file provider where you saved them.

## Background sound

Optional background playback uses an Android media playback foreground service with system media controls. The app requests only the foreground-service permissions needed for that playback. It does not request microphone access. Network access is used for test advertising, not for transmitting your imported audio or remembrance content. The playback notice shows the sound name and session end time; remembrance names are not included in that notice. Sound follows the displayed candle and stops when that candle becomes unlit, when you stop it from the media controls, or when another player takes permanent audio focus. When remembrance ends and restores an already-lit everyday candle, sound can continue with that candle.

## Keeping and deleting app content

Local content is kept so you can reuse it until you remove it or reset the app. You can delete remembrance profiles and dates, delete saved label designs, discard label drafts, and remove imported audio using the app's controls.

These controls have specific scopes. Restoring an original label does not delete the saved custom design. Deleting a design removes its saved design and rendered revisions. Its imported image copies are removed when no saved design, revision or draft still uses them. Other drafts and shared images remain available. Deleting a remembrance profile removes its profile and dates, but does not remove every custom-label file that may have been created for it. Replacing and applying a different wallpaper photo removes the previous saved photo copy; switching to a bundled background or color keeps that photo available. **My Photos → Remove saved photo** removes the private copy without deleting your original.

For a complete reset of this installed copy, use Android's **Clear storage / Clear data** for Still Alight, or uninstall it. This removes the app's local preferences and private files from that installation. It does not delete original files in your gallery or file provider, support emails, or separate copies made by device-transfer or backup services. See [Delete your data](delete-data.md) for instructions. We cannot remotely retrieve or delete the app's private content on your device.

## When you contact support

If you email us, we receive your email address, message and any attachments you choose to include. We use that information to understand and respond to your request. Sending a support message is separate from using the offline app, and your email provider and ours process the message to deliver it.

Please send only what is needed to explain the issue. You can request access to, correction of, or deletion of support correspondence by emailing [tex@discvault.us](mailto:tex@discvault.us). Any rights and lawful exceptions that apply depend on your location and circumstances.

We keep support correspondence for as long as it is needed to handle your request and related support. We delete it on request unless we are legally required to retain it. Email service providers process messages to deliver and store correspondence; their own security, backup and retention practices also apply.

## The website

This website is hosted by GitHub Pages. Visiting it is separate from using the Android app. GitHub processes website requests and logs visitors' IP addresses for security purposes, whether or not they are signed into GitHub. GitHub controls retention of its hosting records under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

The website's own code does not set cookies, use browser storage, run analytics or advertising trackers, or load third-party fonts or embedded media. Its images, models, scripts and sound samples are served with the site. Candle controls run in your browser without sending your selections to us. Audio only plays when you start it. Links to other websites and email services are subject to those services' practices. For privacy requests about GitHub's hosting records, use the contact and rights information in GitHub's Privacy Statement; we cannot delete GitHub's security logs ourselves.

## Google test advertising

Version 1.2.1 uses Google's publicly provided demo application, native ad unit and rewarded ad unit IDs. These development ads are not connected to the publisher's AdMob account and do not earn advertising revenue. Live ads and personalized advertising are not enabled. Ad requests also set Google's non-personalized-ad parameter; this does not mean that the SDK processes no data.

A clearly marked native ad with an image or muted video can appear above the wallpaper **Backgrounds** choices. We do not place automatic ads in Home, Remembrance, label editing, full-screen candle/wallpaper previews, timer controls, or backup/restore. Native ad requests and display are suppressed while an everyday candle or an app/wallpaper remembrance candle is lit, while app sound/background playback is active, and during photo importing. An in-flight request may finish after a state change; its result is discarded instead of displayed. Native requests are limited to one per customization visit and at least ten minutes apart within the app process. Ads do not control candle lighting, wax or timers. Offline or failed native ad requests do not prevent wallpaper customization.

In **Controls → Sound**, tapping **Watch ad to access custom audio** or **Watch ad to replace audio file** opts into one full-screen rewarded demo ad. Completing the ad opens Android's local audio picker once; skipping, closing before the reward or an unavailable ad does not open it. The ad may contain video, an image or interactive content. Still Alight pauses its own sound while the ad is shown and resumes it afterward if the candle session remains active. Already imported audio can be played or removed without another ad. The rewarded ad is user initiated and is separate from the wallpaper ad switch. Builds with demo ads disabled let users choose a file directly.

The app requests network access and network-state access for advertising. The SDK also declares wake-lock permission for its internal work; advertising does not enable the app's Keep screen awake setting. This build removes the Android advertising-ID and AdServices advertising-ID, attribution and topics permissions. It does not supply names, dates, messages, label text, photos, audio, imported filenames, location coordinates or content-based targeting keywords to the advertising SDK.

Google documents that its Mobile Ads SDK can collect and share IP addresses, advertising interactions, diagnostic/performance information and device or account identifiers for advertising, analytics and fraud prevention. Removing advertising-ID permission does not prevent all other identifiers or network information from being processed. The SDK may keep local state or caches. Test advertisements do not eliminate SDK network traffic or these data considerations. See [Google's Mobile Ads SDK data disclosure](https://developers.google.com/admob/android/privacy/play-data-disclosure) and [Google Privacy Policy](https://policies.google.com/privacy).

You can turn **Settings → Wallpaper demo ads** off. This removes a displayed wallpaper ad and prevents new app-issued wallpaper ad requests. It does not disable the optional rewarded ad requested by tapping the custom-audio button. Turning the switch off does not undo requests already sent, stop every SDK-internal operation, or erase information already held by Google. Clearing app storage removes local app/SDK storage; Google's records are governed by its policy and privacy controls. The local wallpaper-ad switch is not a production advertising-consent form.

## Future live advertising and purchases

Live advertising is unavailable in this development build. Before enabling it, the publisher must configure the real AdMob IDs, Google's User Messaging Platform and any applicable privacy choices, and update this policy and Play disclosures for the final SDK and settings. A paid ad-free option managed through RevenueCat remains a possible future feature; RevenueCat is not integrated and no purchase is currently offered. Future pricing, restore behavior and data handling will be described before that feature is introduced.

## Intended audience

Still Alight is intended for adults aged 18 and older. It does not provide app accounts or collect age information. If you believe a child has sent personal information to our support address, contact us to request its deletion, subject to applicable legal retention requirements.

## Changes and contact

We will update this policy when the app or related services change. The published page will show its effective date, and material changes will be accompanied by any notice or consent required for that change.

Publisher: **Satzquatch**  
App: **Still Alight: 3D Candle**  
Privacy contact: **[tex@discvault.us](mailto:tex@discvault.us)**
