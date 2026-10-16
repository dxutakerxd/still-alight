# Privacy Policy

Effective date: **16 October 2026**. This page describes Still Alight Android version **1.3.4 (39)** and later production releases. Earlier 1.1.1 builds do not include the advertising SDK.

Still Alight: 3D Candle is published by **Satzquatch**. In this policy, “we” means that publisher. For privacy questions, contact **[tex@discvault.us](mailto:tex@discvault.us)**.

This policy describes the current Android app, our app website, and messages you choose to send for support. They have different data practices, described below.

## The current app

Candle, label, remembrance, saved audio and wallpaper features work without an account or an internet connection. The app shows advertising through Google AdMob (Google Mobile Ads SDK 25.5.0) and offers an optional paid upgrade, **Still Alight Pro**, sold through Google Play with RevenueCat managing the subscription records. Ads and purchases need network access; the built-in sounds and already saved files remain usable offline. We do not operate an app account or cloud-sync service, and the app does not send your candle settings, remembrance names/messages/dates, label content, photos or imported audio to us, to Google's advertising services or to RevenueCat. There are no publisher analytics or remote crash-reporting integrations. Google's and RevenueCat's own data handling is described below.

The app saves information in its private storage so that your choices and creations remain available when you return:

| Information | Why it is used |
| --- | --- |
| An age eligibility decision and, for a user under 13, the date they become eligible | To require a minimum age of 13 before app access and keep the decision when the app reopens |
| A first name or nickname | To personalize Wick’s greetings; editable in Settings → Your name |
| Candle style, shape, orientation, glow, sound, wallpaper and accessibility preferences | To display your chosen candle and remember your settings |
| Timer duration, deadline or paused remaining time, a device-uptime reference and restart count, candle state and audio playback position | To continue or finish the current session correctly, including when the phone's clock is changed |
| Whether wallpaper ads are enabled | To honor the advertising switch in Settings |
| Whether Still Alight Pro is active, its plan, and any 24-hour previews you earned by watching an ad | To unlock Pro features and remember previews already used |
| Names, personal messages and meaningful dates you enter in Remembrance | To create your remembrance candles and run their local schedules |
| Each loved one's chosen sound, an optional private copy of a recording you choose for them with its displayed filename, and whether their sound starts automatically | To play their sound while their candle is lit |
| Which remembrance lighting was last offered on the live wallpaper | So the same lighting is not announced twice |
| Custom-label text, drawings, layers, drafts, saved designs and generated label images | To let you create, edit and display labels on your candles |
| Images you choose to add to a label | To make a private image copy for that design |
| A photo you choose as a wallpaper background, with its crop and positioning settings | To display your chosen background behind the candle |
| Audio you choose to import, its displayed filename and playback position | To play your chosen sound across app screens and, if enabled, in the background |
| Beat-responsive flame choice and temporary low, mid and high audio levels | To make the flame follow the sound played by Still Alight when you enable that option |

Entering remembrance content and importing files are optional. The app does not read your contacts or your device calendar to fill in remembrance profiles or dates. It does not record microphone audio or take camera pictures.

## Files you choose

Android's file picker lets you choose a specific image or audio file. Still Alight reads that selection and makes a private copy; it does not request broad access to your photo library or storage. Images are processed into bounded-size copies for label editing or wallpaper backgrounds. Imported audio, including a recording chosen for a loved one, is copied and checked for supported playback, with a maximum file size of 250 MB.

The original file is not edited or deleted by these import features. A private copy can remain usable after the original is moved or deleted. Image selections may come from a cloud-backed provider shown by Android; that provider handles delivery of the selected file under its own settings and practices. The audio picker requests local files. Selecting a file does not give us access to it.

If you enable **Controls → Sound → Beat-responsive flame**, Still Alight analyzes only its selected sound on your device. For imported audio, a compact set of low, mid and high levels is kept in app-private cache to avoid decoding the file again. Removing the imported audio also removes its cached levels. This feature does not use the microphone, capture audio from other apps or transmit your audio levels.

## App storage, security and device transfers

The app uses Android's app-private files and preferences. Access protection depends on Android and your device's security. This is not a promise of a separate encrypted vault or of protection against someone with access to an unlocked device. Labels and remembrance names or messages can also be visible on your screen or live wallpaper when you choose to display them.

Still Alight disables Android cloud backup and explicitly excludes app preferences, private files, databases, and app-specific external and device-protected storage from Android cloud backup and device-transfer rules. Device manufacturers and independent migration services may behave differently; copies already created by earlier versions or other services are not removed by these rules. Any copies managed by your device or a storage provider are separate from this installed app.

## Optional protected backups

**Settings → Backup & restore** creates an encrypted file containing your remembrance content (including recordings chosen for loved ones), labels, drafts, imported images/audio and candle preferences. You choose its password and destination through Android's file picker. The app does not upload backups automatically or send them to us. If you select a cloud provider, that provider stores the encrypted file under its own practices. Keep the password safe: we cannot recover it or decrypt your backup for you.

Restoring replaces current app content after the file is authenticated and validated. Temporary decrypted files are kept in app-private storage during the operation and removed afterward. Restored session timers are stopped and background sound is disabled. Deleting app data does not delete backup files you exported; remove those through the file provider where you saved them.

## Background sound

Optional background playback uses an Android media playback foreground service with system media controls. The app requests only the foreground-service permissions needed for that playback. It does not request microphone access. Network access is used for advertising and Pro purchases, not for transmitting your imported audio or remembrance content. The playback notice and lock-screen media controls show the sound and session end time. They name the built-in sounds, but show "Your audio" or "A remembrance recording" instead of an imported filename, and they never include remembrance names. Sound follows the displayed candle. Pausing from the media controls keeps the controls available to resume while that candle stays lit. Sound stops when the candle becomes unlit or when another player takes permanent audio focus. When remembrance ends and restores an already-lit everyday candle, sound can continue with that candle.

## Remembrance sound and notifications

Each loved one can have their own sound: silent (the default for new loved ones), the everyday sound, a built-in sound, or a recording you choose for them. It plays while their candle is lit. Choosing a recording for a loved one never requires an ad.

When a loved one with a sound has a candle that lights on the live wallpaper while Still Alight is closed, the app can start that sound automatically if you turned on **Start the sound when their candle lights on my wallpaper** and Android allows it. Otherwise, it shows a notification such as "Mom's candle is lit" with a **Play their sound** button. The notification is silent, includes the loved one's name, hides that name on a secure lock screen, and offers no Play button during a phone call. It is created on your device; no notification content is sent to us.

On Android 13 and later, the app asks for permission to show notifications only when you give a loved one a sound. You can refuse or change this in Android settings; sound still plays when you open the app. The app does not use notifications for advertising or marketing.

## Keeping and deleting app content

Local content is kept so you can reuse it until you remove it or reset the app. You can delete remembrance profiles and dates, delete saved label designs, discard label drafts, and remove imported audio using the app's controls.

These controls have specific scopes. Restoring an original label does not delete the saved custom design. Deleting a design removes its saved design and rendered revisions. Its imported image copies are removed when no saved design, revision or draft still uses them. Other drafts and shared images remain available. Deleting a remembrance profile removes its profile, dates and any recording chosen for that loved one, but does not remove every custom-label file that may have been created for it. Replacing a loved one's recording, or changing them to a different sound, removes the previous recording copy. Replacing and applying a different wallpaper photo removes the previous saved photo copy; switching to a bundled background or color keeps that photo available. **My Photos → Remove saved photo** removes the private copy without deleting your original.

For a complete reset of this installed copy, use Android's **Clear storage / Clear data** for Still Alight, or uninstall it. This removes the app's local preferences and private files from that installation. It does not delete original files in your gallery or file provider, support emails, or separate copies made by device-transfer or backup services. See [Delete your data](delete-data.md) for instructions. We cannot remotely retrieve or delete the app's private content on your device.

## When you contact support

If you email us, we receive your email address, message and any attachments you choose to include. We use that information to understand and respond to your request. Sending a support message is separate from using the offline app, and your email provider and ours process the message to deliver it.

Please send only what is needed to explain the issue. You can request access to, correction of, or deletion of support correspondence by emailing [tex@discvault.us](mailto:tex@discvault.us). Any rights and lawful exceptions that apply depend on your location and circumstances.

We keep support correspondence for as long as it is needed to handle your request and related support. We delete it on request unless we are legally required to retain it. Email service providers process messages to deliver and store correspondence; their own security, backup and retention practices also apply.

## The website

This website is hosted by GitHub Pages. Visiting it is separate from using the Android app. GitHub processes website requests and logs visitors' IP addresses for security purposes, whether or not they are signed into GitHub. GitHub controls retention of its hosting records under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

The website's own code does not set cookies, use browser storage, run analytics or advertising trackers, or load third-party fonts or embedded media. Its images, models, scripts and sound samples are served with the site. Candle controls run in your browser without sending your selections to us. Audio only plays when you start it. Links to other websites and email services are subject to those services' practices. For privacy requests about GitHub's hosting records, use the contact and rights information in GitHub's Privacy Statement; we cannot delete GitHub's security logs ourselves.

## Advertising

Still Alight shows ads from Google AdMob using the publisher's AdMob account; these ads earn advertising revenue. Ad requests set Google's non-personalized-ad parameter, so ads are not based on your past activity; this does not mean that the SDK processes no data. **Still Alight Pro removes ads.**

A clearly marked native ad with an image or muted video can appear above the wallpaper **Backgrounds** choices. We do not place automatic ads in Home, Remembrance, label editing, full-screen candle/wallpaper previews, timer controls, or backup/restore. Native ad requests and display are suppressed while an everyday candle or an app/wallpaper remembrance candle is lit, while app sound/background playback is active, and during photo importing. An in-flight request may finish after a state change; its result is discarded instead of displayed. Native requests are limited to one per customization visit and at least ten minutes apart within the app process. Ads do not control candle lighting, wax or timers. Offline or failed ad requests do not prevent wallpaper customization.

Rewarded ads are only shown when you choose them. In **Controls → Sound**, **Watch ad to access custom audio** or **Watch ad to replace audio file** opts into one full-screen rewarded ad; completing it opens Android's local audio picker once. A locked Pro colour, scene or the beat-responsive flame can also be tried once for 24 hours by choosing to watch a rewarded ad. Skipping, closing before the reward or an unavailable ad grants nothing. Still Alight pauses its own sound while an ad is shown and resumes it afterward if the candle session remains active. While a remembrance candle is lit, choosing custom audio opens the picker directly without an ad, and Pro imports audio without one. Already imported audio can be played or removed without another ad.

The app requests network access and network-state access for advertising. The SDK also declares wake-lock permission for its internal work; advertising does not enable the app's Keep screen awake setting. The app removes the Android advertising-ID and AdServices advertising-ID, attribution and topics permissions. It does not supply names, dates, messages, label text, photos, audio, imported filenames, location coordinates or content-based targeting keywords to the advertising SDK.

Before any ad is requested, the app uses Google's User Messaging Platform to check whether a consent choice is needed for your region (for example, the EEA, UK or Switzerland), and shows Google's consent form when it is. No ad is requested until Google's platform reports that ads can be requested. Where your region requires it, **Settings → Ad privacy choices** lets you review or change that choice. Google's consent platform processes information as described in Google's policies.

Google documents that its Mobile Ads SDK can collect and share IP addresses, advertising interactions, diagnostic/performance information and device or account identifiers for advertising, analytics and fraud prevention. Removing advertising-ID permission does not prevent all other identifiers or network information from being processed. The SDK may keep local state or caches. See [Google's Mobile Ads SDK data disclosure](https://developers.google.com/admob/android/privacy/play-data-disclosure) and [Google Privacy Policy](https://policies.google.com/privacy).

You can turn **Settings → Wallpaper ads** off. This removes a displayed wallpaper ad and prevents new app-issued wallpaper ad requests. It does not disable rewarded ads you choose to watch. Turning the switch off does not undo requests already sent, stop every SDK-internal operation, or erase information already held by Google. Clearing app storage removes local app/SDK storage; Google's records are governed by its policy and privacy controls. The wallpaper-ad switch is a separate local preference and does not replace the consent choice above.

## Still Alight Pro purchases

Still Alight Pro is an optional upgrade, offered as a monthly or yearly subscription or a one-time lifetime purchase. Prices are shown in the app and by Google Play before you buy. Google Play processes the payment under your Google account; we never receive your payment card or billing address. Subscriptions renew automatically until you cancel them in Google Play; **Manage subscription** in the app opens that page, and uninstalling the app does not cancel a subscription. **Restore** checks your Google Play purchases again, for example on a new phone.

RevenueCat, Inc. manages the Pro records for us. When you open the Pro screen, buy, restore or the app checks your Pro status, the app sends RevenueCat an anonymous app-specific identifier that it creates, the purchase token and order details Google Play provides (product, price, currency, purchase and renewal dates, and status), and basic technical information such as the app and Android versions, store country and language. RevenueCat also processes the network information, such as the IP address, that any internet request involves. The app turns off RevenueCat's automatic collection of device advertising identifiers and sends no names, remembrance content, labels, photos or audio. We use this information to provide Pro, restore purchases and keep purchase records. See the [RevenueCat Privacy Policy](https://www.revenuecat.com/privacy/) and the [Google Privacy Policy](https://policies.google.com/privacy).

If you want RevenueCat's records about your anonymous purchase identifier deleted, contact us at [tex@discvault.us](mailto:tex@discvault.us); Google Play keeps its own order records under your Google account.

## Intended audience

Still Alight requires users to be at least 13 years old. Before the candle guide or app features are available, the app asks for a birthday and checks it on the device. Users whose entered birthday indicates they are under 13 cannot proceed to name collection or use the app. This is a self-declared age check, not identity verification.

For eligible users, the app retains the eligibility decision rather than the entered birthday. For a rejected user, it retains the decision and the date they will turn 13 so the restriction persists when the app reopens and can end at that age. These records and your greeting name stay in this installation’s private storage and are excluded from the app’s optional exported backups. They are not sent to us or supplied to advertising requests. App-issued ad consent, ad requests and Pro purchase checks wait until age and name setup is complete. Clearing app storage or uninstalling removes this local state.

If you believe a child has sent personal information to our support address, contact us to request its deletion, subject to applicable legal retention requirements.

## Changes and contact

We will update this policy when the app or related services change. The published page will show its effective date, and material changes will be accompanied by any notice or consent required for that change.

Publisher: **Satzquatch**  
App: **Still Alight: 3D Candle**  
Privacy contact: **[tex@discvault.us](mailto:tex@discvault.us)**
