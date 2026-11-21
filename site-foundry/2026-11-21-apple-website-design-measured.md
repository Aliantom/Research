<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Apple's web design, measured and independently checked

> **TL;DR:** Apple's site is built from a tight type scale, big whitespace, one pill button and video/JS scroll motion that costs 1.7 to 10 MB per page; a local-business site should copy the discipline and the accessibility floor, not the weight, the scrollytelling or the font.
> **Source:** Owner request 2026-11-21: hard research into Apple's website design principles and interactivity, to use as a guideline for local-business sites  ·  **Project:** site-foundry  ·  **Updated:** 2026-11-21

Date: 2026-11-21. Evidence labels: **VERIFIED** (I measured or read it this session), **REASONED** (follows from verified facts), **ASSUMED** (not checked). Web-page text read through a summarizing fetch tool is marked SUMMARY; check wording before quoting it. Not legal advice.

## 1. Bottom line

Apple's design is two separate things. The part worth copying is **discipline**: one message per section, a small set of type sizes, two font weights, neutral colors with one accent, a 44 px pill button, generous whitespace, and motion that is optional. The part to avoid is **weight and spectacle**: the pages measured here shipped 1.7 to 5.4 MB on first load (up to about 10 MB after scrolling), with 0.6 to 1.3 MB of fonts alone, driven by video, 80 to 170 images and 400 to 850 KB of JavaScript. A bakery, barber or auto shop needs a phone call, directions or hours within seconds on a cheap host. The tokens in the companion guideline keep Apple's proportions and replace its font, its weight and its hero-first layout.

Two findings to remember:
1. **Apple's product pages do not put the buy action first.** At 1440x900 the MacBook Air page showed about 650 px of image before the product name, and the price and Buy button sat at the bottom edge of the first screen (VERIFIED from screenshot). A local site must do the reverse: action in the first screen.
2. **Apple's scroll effects are video plus JavaScript, not modern CSS and not canvas.** No canvas elements and no CSS scroll-timeline rules were found on four pages (VERIFIED below); a native-CSS reveal is cheaper than anything Apple ships.

## 2. Apple's own principles (primary sources)

| Source (date) | What it says | Use for a small site |
|---|---|---|
| HIG Layout (fetched 2026-11-21 from Apple's documentation JSON) | "Order content by relative importance"; "Align elements to make them easier to scan"; "Group related items" with negative space; "Use progressive disclosure" (VERIFIED) | One message per section, most important item first and top-left |
| HIG Typography | iOS/iPadOS default text size 17 pt, minimum 11 pt (table) (VERIFIED) | Body 17 px or larger |
| HIG Accessibility | Contrast: 4.5:1 up to 17 pt, 3:1 at 18 pt or bold; default control 44x44 pt, minimum 28x28; about 12 pt padding around bezeled controls; support text enlargement to 200 percent; Reduce Motion should reduce zooming, scaling and peripheral motion; do not autoplay video without controls (VERIFIED) | Contrast, tap-target and motion rules |
| HIG Motion | "Add motion purposefully"; "Make motion optional"; "Aim for brevity and precision in feedback animations"; "Let people cancel motion" (VERIFIED) | Short, optional motion |
| HIG Writing | "Be clear"; "Be action oriented": label buttons and links with a verb (VERIFIED) | "Call", "Get directions", "Order pickup" |
| HIG Materials | Liquid Glass is a controls/navigation layer, "Don't use Liquid Glass in the content layer"; "use ... sparingly" (VERIFIED) | Translucent header is optional polish, never a content style |
| WWDC25 session 356, "Get to know the new design system" (June 2025; SUMMARY) | Stated ideas: harmony, hierarchy through layout and grouping "instead of relying on decoration", content-first UI, consistency of labels and symbols, concentric corner radii | Hierarchy from spacing and size, not borders and shadows |

The older HIG trio "clarity, deference, depth" was not found in the current pages fetched; the current language is hierarchy, harmony, consistency (REASONED from the WWDC25 session and the pages above).

## 3. apple.com as built (measured 2026-11-21)

Method: Chrome 157 driven from Playwright (Python), no throttling, empty cache, deviceScaleFactor 1, viewports 1440x900 and 390x844 (iPhone user agent), pages: home, /iphone/, /macbook-air/, /privacy/ (a "why Apple" style editorial page; /why-apple/ returned 404). One load per viewport plus one reduced-motion reload each, then a gentle scroll to trigger lazy loading. LCP/CLS came from PerformanceObserver, not Lighthouse: no Lighthouse or Playwright browser folder existed on this machine, so Lighthouse was **not run on apple.com** (the site-foundry Lighthouse figures in section 5 are from reports the repo already contained). These are single lab runs on one network; treat times as indicative.

**Type (VERIFIED, computed styles).** Body 17 px / 25 px line-height (1.47), color #1d1d1f on white. Desktop sizes in use: 12, 14, 17, 21, 24, 28, 32, 40, 48, 56, 64, 72, 80 px. Mobile sizes: 12, 14, 17, 19, 21, 24, 28, 32, 40, 48. Only two weights carry nearly everything: 400 and 600 (a few 700/800). Heading line-heights are tight: 80/84, 56/60, 40/44, 28/32 (about 1.05 to 1.14). Letter-spacing is size-dependent and set by the font: -0.374 px at 17 px, -0.224 px at 14 px, +0.196 px at 28 px, -0.28 px at 56 px, -1.2 px at 80 px. Font family: "SF Pro Text" for 17 px and smaller, "SF Pro Display" above, Helvetica Neue/Arial fallback. Heading sizes step down on phone (for example 56 to 32 px).

**Widths and spacing (VERIFIED).** Content columns: 980 px (nav and most copy), 1024 px, `min(1260px, 87.5%)` for galleries, up to `min(1680px, 87.5%)`; copy columns of 410, 584 and 680 px. Section vertical padding on desktop: 110 to 180 px (typically 144 to 170). On a 390 px phone it stays large: 72 to 112 px. Alternating surfaces: white, #f5f5f7 and black.

**Color and contrast (VERIFIED, ratios computed by me).** Primary button #0071e3 with white text: 4.70:1. Link #0066cc on white: 5.57:1. Body #1d1d1f on white: 16.83:1. Secondary text rgba(0,0,0,.56): 4.94:1; #6e6e73: 5.07:1. **#86868b on white: 3.62:1, which fails 4.5:1 for small text, and it appears 59 times on the MacBook Air page.** Dark-mode link #2997ff on black: 6.96:1.

**Buttons (VERIFIED).** Primary "Learn more"/"Buy": background #0071e3, white text, radius 980 px (pill), padding 11 px 21 px, 17 px/400, height 44 px; small variant padding 8 px 15 px, 14 px, height 36 px. Round 56 px glass play/pause buttons on dark pages.

**Navigation (VERIFIED).** Global nav 44 px high on desktop, 48 px on phone, background rgba(245,245,247,.8) with `backdrop-filter: saturate(1.8) blur(20px)`; fixed on the home page, absolute on product pages. Product ("local") nav on MacBook Air and Privacy pages: `position: sticky; top: 0`, 52 px desktop, 48 px phone. 50 to 69 `backdrop-filter` rules per page. On the phone the global nav collapses to icon buttons.

**Media (VERIFIED).** Every image is a `<picture>` with several `<source>` variants (home: 48 pictures, 64 sources; MacBook Air: 105 pictures, 369 sources) and size-named files such as `..._small.jpg` on phone and `..._largetall.jpg` on desktop. Native `loading="lazy"` appeared on only 1 of 48 images on the home page and none elsewhere, so lazy loading is done by script. Videos: `preload="none"` or `metadata`, muted, `playsinline`, no `autoplay` attribute set at load, an HLS player script (hls.js) on the MacBook Air page; the MacBook Air phone LCP element was a video (small.webm).

**Motion (VERIFIED).** Transition/animation durations in the CSS: 0.24 s, 0.3 s, 0.32 s, 0.4 s, 0.5 s most common, 1 s for large hero animations. Easings: `cubic-bezier(0.4, 0, 0.6, 1)` (most used), `cubic-bezier(0.42, 0, 0.58, 1)`, `cubic-bezier(0.25, 0.1, 0.3, 1)`, plus plain `ease`. Scroll effects: 0 canvas elements on all four pages; 0 `ScrollTimeline` and 0 CSS scroll/view-timeline rules (the "animation-timeline" matches were `auto` resets only); 1 to 12 IntersectionObserver instances; 79 to 85 `requestAnimationFrame` uses in the page scripts; sticky elements (13 on /iphone/). So the "scrollytelling" is video and script-driven, not canvas image sequences. **Reduced motion:** 4 to 61 `prefers-reduced-motion` blocks per page; with reduced motion emulated, 0 videos were playing on every page, and the Privacy page gates its gallery animation behind `no-preference`.

**Weight and speed (VERIFIED, unthrottled, empty cache).**

| Page (viewport) | First load | After scroll | Requests after scroll | Fonts | JS | LCP |
|---|---|---|---|---|---|---|
| Home (desktop) | 1.65 MB | 3.38 MB | 89 | 829 KB | 418 KB | 0.64 s |
| Home (phone) | 1.70 MB | 2.38 MB | 89 | 931 KB | 418 KB | 0.38 s |
| iPhone (desktop) | 2.01 MB | 2.57 MB | 74 | 790 KB | 606 KB | 3.13 s |
| iPhone (phone) | 1.88 MB | 2.08 MB | 75 | 790 KB | 606 KB | 1.73 s |
| MacBook Air (desktop) | 5.37 MB | 10.07 MB | 174 | 1.31 MB | 828 KB | 0.50 s |
| MacBook Air (phone) | 3.86 MB | 5.40 MB | 178 | 1.31 MB | 828 KB | 1.41 s (a video) |
| Privacy (desktop) | 1.91 MB | 2.23 MB | 95 | 588 KB | 850 KB | 1.47 s |

CLS was at or near 0 everywhere except the MacBook Air page on phone after scrolling (0.042, still under 0.1). SF Pro files served per weight: 117 KB to 235 KB each (10 files on the MacBook Air page). Page height: the MacBook Air page is about 35,000 px on a phone (roughly 41 screens). The iPhone page on desktop had an LCP of 3.13 s in this run, above the 2.5 s "good" line, which shows that even Apple's own pages rely on fast connections; one run only.

## 4. Independent analysis

| Source (date) | Finding | Evidence |
|---|---|---|
| NN/g, "Scrolljacking 101" (Aug 6, 2023; SUMMARY) | Study of sites using scrolljacking: most participants were at least mildly disoriented; worst when scroll rate or direction changes and text must be read; problems amplified on mobile; "more user pain than benefits"; use only to progressively disclose valuable information, below the fold, not on mobile. Participant count not stated | usability study, secondary summary |
| NN/g, "Parallax Scrolling" (Jan 20, 2019; SUMMARY) | Observed Apple's site: some users scrolled past blank screens before effects animated; most users indifferent to effects; use parallax for background imagery only, leave elements in final position, add in-page navigation | qualitative testing |
| NN/g, "Hamburger Menus and Hidden Navigation Hurt UX" (Jun 26, 2016; SUMMARY) | 179 participants, 6 sites: hidden navigation used 27 percent on desktop vs 48 percent visible; on mobile 57 percent vs 86 percent for combo navigation; discoverability down over 20 percent; acceptable on mobile when more than 4 top-level links | quantitative study |
| NN/g, "Photos as Web Content" (2010, reviewed 2026; SUMMARY) | Eye tracking: users ignore generic stock photos of people, study real staff photos closely; the key point is that "these are real people who actually work at the company" | eye-tracking, old but stable |
| web.dev, Core Web Vitals (updated Oct 31, 2024; SUMMARY) | Good thresholds at the 75th percentile: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less | Google documentation |
| web.dev, Optimize LCP (updated Mar 31, 2025; SUMMARY) | Make the LCP image discoverable in HTML; `fetchpriority="high"` on one or two images at most; "Never lazy-load your LCP image"; ideal split TTFB 40 percent, load delay under 10, load duration 40, render delay under 10 | Google documentation |
| web.dev, Scroll-driven animations (May 5, 2023; SUMMARY) | CSS `animation-timeline: scroll()/view()` can run off the main thread; support listed for Chrome/Edge 115, Safari 26 and Firefox 159 (support claims for the last two not independently checked; Chrome 157 here returned true for `CSS.supports('animation-timeline','scroll()')`, VERIFIED). The page does not discuss reduced motion | Google documentation |
| web.dev, prefers-reduced-motion (undated; SUMMARY) | Parallax and zoom can trigger vestibular symptoms; default to removing non-essential movement under `reduce`; treat decorative motion as optional | Google documentation |
| HTTP Archive Web Almanac 2025, Page weight (SUMMARY) | Median home page 2.86 MB desktop, 2.56 MB mobile; median JS 697 KB desktop, 632 KB mobile; 75 to 80 requests | large crawl dataset |
| W3C WCAG 2.2, SC 2.5.8 Target Size (Minimum) (SUMMARY) | Level AA: pointer targets at least 24x24 CSS px, with spacing and inline exceptions | standard |
| Google / Ipsos, "The Role of Click to Call" (Sep 2013; VERIFIED, PDF read) | 3,000 US smartphone users surveyed July 2013: 70 percent of mobile searchers have used click to call; 47 percent say that if a business has no phone number in its results they will be more likely to explore other brands | survey, 13 years old, shows direction only |

**Where Apple's approach hurts (REASONED from the above):**
- Cost: Apple's median first load (about 1.9 MB) is below the web median (2.56 MB mobile) only because Apple's CDN is fast; for a visitor on a weak phone connection the 0.6 to 1.3 MB of fonts alone is larger than a whole local-business page should be.
- Usability: NN/g found scroll-linked effects disorient, lose task-focused users and fail on mobile; Apple's pages are built for leisure browsing and a product the visitor already wants.
- Hero-first layout hides the action (section 1).
- Apple's own small gray (#86868b, 3.62:1) fails its own HIG guidance of 4.5:1; do not copy that color.
- Local conversion needs a phone number and hours, which a product-launch layout never needs to show.

**Where the evidence is thin:** no controlled study isolates the effect of a sticky call bar on local-service sites. The only searchable numbers were vendor claims and case studies (not opened). Treat a sticky Call/Directions bar as a cheap test, not a proven lift (ASSUMED benefit; check with call tracking on the live demos).

## 5. Fit for a small local site (summary; the full token set is in the companion guideline)

| Apple technique | Verdict | Why |
|---|---|---|
| One headline + one visual + one action per section | **ADOPT** | Costs nothing; matches HIG layout and NN/g content-first |
| Tight type scale, two weights, tight heading line-height | **ADOPT** | Costs nothing; font swapped to a licensed face |
| Large section whitespace | **ADAPT** | Keep rhythm, shrink (64 to 128 px) so key info appears in the first screens |
| Pill primary button, verb labels | **ADAPT** | Height 48 to 56 px on phone; label with the action |
| Sticky local nav | **ADAPT** | On a one-page site use a bottom Call/Directions bar and a few anchor links |
| Translucent blurred header | **ADAPT (optional)** | One property; needs solid fallback; HIG says controls layer only |
| Reveal on scroll | **ADAPT** | CSS `view()` timeline inside `@supports`, transform only, off under reduced motion |
| Scrollytelling, pinned sections, video heroes, frame sequences | **AVOID** | 1.7 to 10 MB; NN/g problems; no value for a call |
| Hero image first, CTA later | **AVOID** | Opposite of the local job |
| SF Pro, Apple logos, Apple product photos, "Apple-like" claims | **AVOID** | License and trademark (below) |
| Low-contrast gray text | **AVOID** | Fails WCAG AA |

**Fonts and legal (VERIFIED from Apple's pages, SUMMARY; not legal advice).** Apple's San Francisco license (dated 2016-02-24) permits use "solely for creating mock-ups of user interfaces to be used in software products running on Apple's iOS, OS X or tvOS", forbids embedding the font, and bars using it to "create, develop, display or otherwise distribute any ... website content". Apple's third-party guidelines say not to use the Apple logo or graphic symbols "on or in connection with web sites", allow Apple names only referentially, and prohibit implying affiliation or endorsement. Apple serves SF Pro to its own visitors as web fonts, but that does not extend to anyone else. Licensed options: Inter (SIL Open Font License 1.1, a free and open source family, variable font available, optical sizes from text to display); the system font stack (`system-ui`, `-apple-system`), which renders the visitor's own device font and ships zero bytes. WebKit documents `-apple-system` as the way to use the system font, San Francisco, on iOS and macOS (July 2015). Whether referencing the user's installed system font is acceptable under Apple's license is REASONED yes (the site does not embed or distribute the file) and has no explicit Apple statement; confirm if it matters.

**Existing site-foundry baseline (VERIFIED, repo Lighthouse reports dated 2026-11-21, mobile).** The three hand-built flagships weigh 135 to 201 KiB in total, LCP 1.3 to 1.6 s, CLS 0, Lighthouse performance 100, accessibility 95 to 100 (the 95 was a pre-fix run), SEO 63 (a known gap), with a bottom Call/Directions bar, a view-timeline reveal under `no-preference`, and self-hosted woff2 fonts of 26 to 37 KB. The generator is therefore already far lighter than Apple; what the research adds is standardized tokens and automated budget checks.

## 6. Rejected or not used

- **Canvas image sequences** (the classic AirPods Pro style): none found on Apple's current pages and far too heavy for a small site.
- **JavaScript scroll libraries (GSAP, Lottie, ScrollMagic):** not used by Apple's pages in my scan (no gsap or Lottie strings in the first 30 scripts) and not needed.
- **Copying SF's letter-spacing numbers onto another font:** SF's tracking is part of the font's optical-size system (HIG Typography: the system font adjusts tracking at every point size); with Inter use small negative tracking on large headings only (REASONED).
- **Third-party "Apple design teardown" blogs:** not used as evidence.

## 7. Sources (all opened this session, 2026-11-21 unless noted)

- Apple HIG JSON pages: layout, typography, color, motion, accessibility, materials, writing, images, `https://developer.apple.com/design/human-interface-guidelines/` (content fetched from developer.apple.com documentation data; current as fetched)
- WWDC25 session 356: https://developer.apple.com/videos/play/wwdc2025/356/ (June 2025)
- Apple fonts license page: https://developer.apple.com/fonts/
- Apple trademark guidelines: https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html
- apple.com pages measured: https://www.apple.com/ , /iphone/ , /macbook-air/ , /privacy/ (2026-11-21)
- WebKit, "Using the System Font in Web Content": https://webkit.org/blog/3709/using-the-system-font-in-web-content/ (2015-07-27)
- Inter: https://rsms.me/inter/
- NN/g scrolljacking: https://www.nngroup.com/articles/scrolljacking-101/ (2023-08-06)
- NN/g parallax: https://www.nngroup.com/articles/parallax-usability/ (2019-01-20)
- NN/g hidden navigation: https://www.nngroup.com/articles/hamburger-menus/ (2016-06-26)
- NN/g photos: https://www.nngroup.com/articles/photos-as-web-content/ (2010, reviewed 2026)
- web.dev Core Web Vitals: https://web.dev/articles/vitals (2024-10-31)
- web.dev Optimize LCP: https://web.dev/articles/optimize-lcp (2025-03-31)
- web.dev scroll-driven animations: https://developer.chrome.com/docs/css-ui/scroll-driven-animations (2023-05-05)
- web.dev prefers-reduced-motion: https://web.dev/articles/prefers-reduced-motion
- HTTP Archive Web Almanac 2025 page weight: https://almanac.httparchive.org/en/2025/page-weight
- W3C WCAG 2.2 Target Size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Google/Ipsos click to call, Sept 2013: https://www.thinkwithgoogle.com/_qs/documents/1454/click-to-call_research-studies_hz2ytgv.pdf
