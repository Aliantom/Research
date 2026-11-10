<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Reaching no-website, no-email leads without phone calls

> **TL;DR:** Best no-phone route for the 13 phone-only Annapolis leads: a personalized first-class postcard with a per-lead QR link (about $12 for 13) plus a walk-in; no channel has solid response-rate data.
> **Source:** Owner request 2026-11-03 (approved run): how can a solo MD web designer legally reach no-website, no-email local businesses without phone calls  ·  **Project:** site-foundry  ·  **Updated:** 2026-11-03

Date: 2026-11-03. Evidence labels: VERIFIED (read the page this session), REASONED (follows from verified facts), ASSUMED (not checked). Not legal advice; the owner should read the statute pages linked below before the first send.

**Honest summary of the evidence:** the rules (CAN-SPAM, Maryland act, Meta policy, USPS prices) are verifiable from primary pages. Response rates for *personalized-demo mailers to businesses with no website* do not exist in any credible public source I could find. The only numbers are consumer-mail benchmarks, UK data, and a few Reddit anecdotes. Plan on tiny samples (13 leads) and measure your own.

## 1. Bottom line (ranked)

1. **Personalized first-class postcard with a per-lead QR code and short URL, to the 13 phone-only leads.** Cost about $0.91 each through Lob's pay-as-you-go tier (VERIFIED, Lob pricing page, 4x6 first class, $0.905 now, $0.909 from 2026-11-01), so about $12 for 13. Cheaper by hand: print yourself and use a $0.65 postcard stamp (VERIFIED via news summaries of the 2026-07-12 USPS change; confirm on usps.com). Legal exposure is lowest of any channel (REASONED: CAN-SPAM covers email only; see section 3). It is also the only channel that can be automated right up to the owner's "approve and drop in mailbox" step. First step: deploy the demos to Cloudflare Pages (owner approval, still pending) and decide a short demo domain; the QR is only as good as the URL.
2. **Weekend walk-in with the same card, same leads, 2-3 hours.** Costs $0 beyond print. Many practitioners say in-person or local networking is where local clients come from (Reddit thread below, anecdote), but I found no conversion numbers for walk-ins. Treat it as a cheap test, not a proven channel. Do it *after* the postcards land (3-7 days) so the owner can say "I mailed you a card" in person.
3. **Manual Facebook/Instagram message for the social-only leads**, one short message each, sent by the owner by hand. Never automate. A handful of leads, five minutes each.
4. **Email only where the business itself publishes one** (its Facebook About page, a directory listing it controls). Low yield (2 of 15 have one today) and the drafts already exist.

Skip: bulk EDDM, Nextdoor, Yelp, Google Business Profile, form-submit bots (reasons below).

## 2. Candidate channels

| Channel | Legal / rules | Evidence on response | Cost per contact | Effort (day job) | Automatable to review/send? | Verdict |
|---|---|---|---|---|---|---|
| Addressed first-class postcard + QR (Lob / PostGrid / Click2Mail / DIY) | No federal or Maryland email-style rule applies to postal mail (REASONED; I found no Maryland statute restricting unsolicited commercial postal mail to businesses, but did not search exhaustively). Include sender name and address and an "not interested, tell me and I won't mail again" line as good practice. | No B2B personalized-demo data. Cold direct mail benchmark: 0.9% in the UK JICMAIL 2024 tracker (consumer-heavy, cold) vs 7.9% for warm. Older US DMA figures: 1.28% prospect letter mail (Chief Marketer, old) and 4.9% prospect list in a secondhand 2018 report. All of these are for generic campaigns. Expect 0 or 1 replies from 13 pieces. | Lob Developer $0.905-0.909; PostGrid Starter $0.902 (4x6 first class); DIY about $0.65 postage plus print (print cost ASSUMED $0.10-0.30). | 1 hour to review and mail 13. | Yes: render PDF per lead, owner reviews, then upload to Lob/PostGrid or print. | **Try (rank 1)** |
| EDDM Retail (saturation route mailing) | No permit needed for EDDM Retail, 200-piece minimum per vendor guides; current rate reportedly $0.26 per piece (vendor-cited USPS Notice 123, unverified against usps.com). | n/a | $0.26 postage plus print, but you pay for whole routes, not named businesses. | Medium | Poor fit: no per-lead personalization, which is the whole point. | **Skip** |
| Walk-in drop-off with QR card | Normal courtesy. Respect "no soliciting" signs and any request to leave; trespass law is the real limit (REASONED). | Anecdote only. Reddit commenters (r/ the-thread linked below) report referrals, local networking and face-to-face as their main source; none give walk-in conversion numbers. Warrior Forum anecdote: 1 appointment per 50 cold calls, about half close (cold *calls*, not walk-ins). | $0 plus gas and print. | 2-3 hours on a weekend for roughly 13 stops in downtown Annapolis (ASSUMED route density). | Partly: same card PDF, plus a printed route sheet. | **Try (rank 2)** |
| Facebook Page / Messenger | Meta's Messenger Platform policy (API) allows messages to a person inside a 24-hour window opened by *their* action (VERIFIED, developers.facebook.com policy overview). That governs API/automation; it means automated cold outreach is not allowed. Manual one-off messages from a person are a different case (ASSUMED: Meta's Community Standards spam page, VERIFIED, only restricts "very high frequencies" and repetitive content). | No data. Reddit anecdote: a UK freelancer says cold texting on WhatsApp/Facebook beat cold calling. | $0 | 5 min per lead | **No, manual only.** | **Try, manual, small** |
| Instagram DM | Reported 2023 change: non-followers can receive only one text-only message request until accepted (news coverage 2023, not re-checked against Instagram help pages in 2026). Also recipient spam filters ("Hidden Words"). | None | $0 | 5 min per lead | No | **Watch / manual** |
| Google Business Profile | Google ended Business Profile chat and call history on 2024-07-31 (VERIFIED via Google developer release notes and trade press). There is no GBP messaging left to use. | n/a | n/a | n/a | n/a | **Skip** |
| Nextdoor business | Business Pages let neighbors message the business; I found no way for a business to cold-message another business. A secondhand FAQ says unsolicited repeated promotion of your own business is not allowed; Nextdoor changed its self-promotion policy in 2026 (details not retrieved). | None | n/a | n/a | n/a | **Skip** |
| Yelp | Messaging is for consumers and for business owners replying to reviewers; no sanctioned cold-pitch route, and consumer accounts are "personal, non-commercial" (archived Yelp guideline text via search snippet, unverified at yelp.com). | None | n/a | n/a | n/a | **Skip** |
| Email found from public sources | See section 3. | Reddit anecdote: "1% success rate with cold emailing local businesses" (one commenter). Another thread: 2% reply to generic emails. Both anecdotes. | $0 | Varies | Yes (drafts exist) | **Try only when the business itself published the address** |
| Website contact forms | Not legally different from email, but bot-submission breaks most sites' terms and adds reCAPTCHA friction; the leads have no site anyway. | n/a | n/a | n/a | No | **Skip** |
| Square / Toast / DoorDash / Uber Eats storefronts | No legitimate outreach route found: these pages are for customer ordering, and platforms' terms are about customers, not vendor solicitation (ASSUMED; I did not read their terms). Posting pitches through the order notes field is spam. | n/a | n/a | n/a | No | **Skip** |

## 3. Finding a legitimate email (question 3)

- **CAN-SPAM applies to B2B email.** FTC: "The law makes no exception for business-to-business email." (VERIFIED, FTC compliance guide.) Requirements: accurate header and subject, valid physical postal address, clear opt-out that works at least 30 days, opt-outs honored within 10 business days, penalties up to $53,088 per email.
- **Emailing an address you found publicly is allowed under CAN-SPAM** as long as the message complies; the Act is an opt-out regime, not opt-in (REASONED from the FTC guide, which does not require prior consent). **Harvesting** (scraping addresses in bulk, or dictionary-guessing) is an *aggravated* violation with criminal penalties (VERIFIED from the FTC page; the exact statutory trigger is about sites whose policies bar sharing addresses and about automated generation, ASSUMED from my background knowledge of 15 U.S.C. 7704(b), not read this session). Practical rule: type in addresses the business itself published; never bulk-scrape or guess `info@`.
- **Maryland Commercial Electronic Mail Act, Commercial Law 14-3002 (VERIFIED, mgaleg.maryland.gov):** unlawful to send commercial email to or from Maryland that uses a third party's domain without permission, contains false origin or routing information, or has a false or misleading subject line. It is about deception, not consent. Truthful drafts comply. A private damages remedy ($1,000 per email, from a federal filing seen in search, ASSUMED/unverified) sits in 14-3003; I did not read it, and one court commentary says a subject-line clause was held too vague (unverified). Net: no extra Maryland hurdle for honest emails.
- **Sources:**
  - **Business's own Facebook About / Google Business Profile / chamber directory entry:** fine, the business published it. Best source.
  - **Maryland SDAT business entity search:** gives entity names, resident agent and principal office address, not usually an owner's email (ASSUMED). SDAT's terms reportedly ban automated collection and scraping (search snippet only; read the Website Usage Statement before using anything beyond manual lookup). Useful for the *mailing address and owner/agent name* on a postcard, not for email. Warning: the resident agent is often a law firm or service company (a legal-guide claim, unverified).
  - **State licensing boards:** useful mainly for trades (HVAC, electricians, barbers); the data usually includes a mailing address, rarely a public email (ASSUMED, not checked). I did not verify any board's terms on commercial use.
  - **WHOIS:** these businesses have no domain; skip.
- Net: this channel will convert 2 of 15 leads at best; do not spend engineering time here.

## 4. Practitioner evidence (and how much to trust it)

- Reddit, Feb 2026 (via a third-party mirror, VERIFIED read): a new UK freelancer cold-called and got "two maybes and 50 rejections." Top comments: cold calling yields little; referrals, networking and local communities do better; one says cold texting on WhatsApp/Facebook beat calling; one says "1% success rate with cold emailing local businesses"; another says most small businesses "don't need a website" (Squarespace/Wix are cheap). All anecdotes, UK, mostly subscription pitches.
- A search for first-hand walk-in or postcard conversion numbers (2025-26) returned almost only vendor marketing (lead-finder tools, agencies). Per the standard here I treat those as not evidence. **I found no credible walk-in conversion figure.**
- A Warrior Forum cold-call anecdote: about 2% book an appointment, about half of those close. Old, cold *phone* calls.
- A Reddit view worth noting: businesses with no website often chose that on purpose; businesses with a bad site or 30+ reviews and no site may be better prospects. This supports using site-foundry's lead score (reviews, category) to pick which 13 to mail first.

## 5. Adjacent ideas

- **Tell them what they get, not that you built it:** the card should show the business's own name and a phone screenshot of the demo, a short URL, "free preview, nobody has your site but you", and what you cost. The personalized screenshot is the one thing generic mailers cannot copy. (REASONED; no A/B data.)
- **Track opens per lead:** Cloudflare's free web analytics per demo path tells you if the card or walk-in drove a visit even with no reply.
- **Bad-site expansion (docs/open-problems.md 1B)** multiplies leads that have a reachable email on their existing site; a better pool than no-site leads for email.
- **Local networking:** Annapolis chamber or BNI-type groups are what experienced freelancers in that thread credit; slow, but warm. Not automatable.

## 6. Rejected (so nobody re-researches)

- **EDDM:** pays per route, cannot personalize per business.
- **Google Business Profile chat:** shut down 2024-07-31.
- **Nextdoor / Yelp as outbound channels:** built for consumers and replies, no cold B2B messaging route found, solicitation risks account action.
- **Contact-form bots and automated DMs:** breach platform terms and the owner's own no-bot-forms rule.
- **Buying email lists / scraping directories:** harvesting is an aggravated CAN-SPAM violation; bad quality anyway.
- **Order-platform pages (Square, Toast, DoorDash):** customer-facing; nothing legitimate for vendor pitches.

## 7. What site-foundry code would change (no code touched)

Top channel is the postcard, with walk-in using the same artifact.

1. **`foundry mailers [--slug S ...] [--leads shortlist]`** in a new `src/sitefoundry/mailers.py`, wired in `cli.py` next to `drafts`:
   - Skips leads missing `street`, `city` or `postcode` and any `presence` of `site`; reports why.
   - For each lead writes `out/mailers/<slug>.pdf`: page 1 front (business name, phone screenshot from `out/shots`, short URL, QR, offer line, sender name and address from the existing `FOUNDRY_SENDER_NAME` / `FOUNDRY_SENDER_ADDRESS` env vars), page 2 back (address block in the USPS 4.25x6-inch postcard layout with clear zones, a return address, a "not interested? reply or text and I won't mail again" line).
   - Render with the headless Chrome that `shots.py` already uses (`--print-to-pdf` from an HTML template), so no new heavy dependency.
   - The QR needs one small pure-Python library (`segno` or `qrcode`); add it as an optional extra (`mail`) like `enrich`. `qrcode` is not installed on this box today (VERIFIED, import failed).
   - Also writes `out/mailers/manifest.csv` (slug, name, address, short URL, status `needs-review`) and a combined `print-sheet.pdf` for walk-ins (4 cards per sheet).
2. **Short URL:** `bundle.py` already creates `out/public/<slug>/`; add a `base_url` setting (env var `FOUNDRY_DEMO_BASE`) and a length check so the printed path stays typeable (about 25 characters or less). Needs the Cloudflare Pages deploy and brand domain first (owner decision).
3. **Contact log:** add `out/contact_log.csv` (slug, channel, date, outcome, notes) and a `foundry log` subcommand to record mailed, walked-in, messaged, replied, won. This is the data the lead scorer in open-problems 1D needs, and the only way to get a real response rate.
4. **Draft template (`outreach.py`):** add a `channel` field so the social-message and email drafts differ; postcards skip CAN-SPAM text but keep sender identity.
5. **Never in code:** no Lob/PostGrid API call that sends without the owner pressing a final confirm. If the Lob API is used, default to its test mode and require an explicit `--live`. (Hard line: nothing leaves the machine without the owner's OK.)

## 8. Ranked recommendation

1. Postcards to the 13 phone-only Annapolis leads: about $12 via Lob or about $9-12 DIY. Build `foundry mailers`.
2. Walk-in on the Saturday after delivery with the same card: $0.
3. Manual FB/IG message for social-only leads.
4. Email only where the business published its own address.
Expected result, said plainly: 0-2 replies from 13 mailed leads; judge the channel on 50+ pieces, not 13.

## Sources (all opened this session unless marked)

- FTC CAN-SPAM compliance guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business (fetched 2026-11-03; page edited Jan 2024 per page)
- Maryland Commercial Law 14-3002 (text via mgaleg.maryland.gov): https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3002&enactments=false (fetched 2026-11-03; Justia mirror returned 403)
- Meta Messenger Platform policy overview: https://developers.facebook.com/docs/messenger-platform/policy/policy-overview (no date on page; fetched 2026-11-03)
- Meta Community Standards, Spam: https://transparency.meta.com/policies/community-standards/spam/ (fetched 2026-11-03)
- Lob pricing details: https://help.lob.com/print-and-mail/ready-to-get-started/pricing-details (rates effective 2026-07-12 and 2026-11-01)
- PostGrid print and mail pricing: https://www.postgrid.com/pricing-print-mail/ (fetched 2026-11-03; page shows two unexplained rate tables)
- Google Business Messages shutdown: https://9to5google.com/2024/05/28/google-business-messages-shutting-down/ and https://developers.google.com/business-communications/business-messages/resources/release-notes/update-on-gbm (search results only, snippets read, not opened; 2024)
- USPS July 2026 postcard rate (61 to 65 cents): https://www.uml.edu/myuml/submissions/2026/2026-05-29-15-11-43-usps-july-2026-rate-increases.aspx and https://www.azfamily.com/2026/07/07/price-stamps-could-be-increasing-again-soon-sunday-heres-what-you-need-know/ (search results only; confirm on usps.com)
- EDDM price (about $0.26, vendor-cited): https://www.postgrid.com/every-door-direct-mail/ (search result only)
- JICMAIL 2024 cold vs warm mail: https://printweek.com/content/news/jicmail-data-reveals-growth-in-customer-acquisition-through-mail-campaigns (search result only, UK)
- DMA/ANA response rates: https://www.chiefmarketer.com/direct-mail-gets-most-response-but-email-has-highest-roi-dma/ (search result only; old; consumer-heavy)
- Click2Mail pricing (third-party, likely stale, the $0.55 postcard is below current postage): https://blog.click2mail.com/2025/08/04/bulk-mail-postcard-rates-guide/ (search result only)
- Instagram DM request limits (2023): https://www.engadget.com/instagram-fights-dm-spam-with-limits-on-text-and-photos-165013992.html (search result only)
- Reddit thread via mirror, Feb 2026: https://reddit.sentinel-team.org/posts/1r86ggu/snapshots/2026-02-19T21%3A40%3A20.164555Z (fetched 2026-11-03)
- Warrior Forum cold-call anecdote: https://www.warriorforum.com/offline-marketing/736539-web-design-conversion-rate.html (search result only, old)
- Nextdoor self-promotion policy change: https://blog.nextdoor.com/self-promotion-update (search result only; details not read)
- SDAT terms (snippet only): https://sdat.dat.maryland.gov/RealProperty (not opened in full)
- Site context: ~/code/site-foundry/docs/open-problems.md; site-foundry brief
