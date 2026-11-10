<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Reaching site-foundry leads with no phone and no email

> **TL;DR:** For leads with no phone or email: walk-ins first, then a manual Facebook/Instagram message, then a hand-mailed postcard with a QR code; skip texts, scraped emails and contact-finder tools.
> **Source:** Owner live chat 2026-10-29: how to reach site-foundry leads that still have no phone or email after Overture (DUS-57)  ·  **Project:** site-foundry  ·  **Updated:** 2026-10-31

Research only. Nothing was contacted, signed up for or submitted. Not legal advice: have a Maryland attorney confirm anything marked REASONED or ASSUMED before volume outreach. Hosting and Overture enrichment are already settled and not covered.

Evidence labels: **VERIFIED** = I opened the source this session. **REASONED** = follows from verified facts. **ASSUMED** = not checked. Many web pages here returned only a summary, not full text; where a primary page would not load I say so.

## 1. Bottom line

1. **Walk-ins with the demo on a phone/tablet, batched by street.** Free, legal, reaches the actual owner, and the strongest channel for a business with no listed phone. Plan: sort leads by street/block (lat/lon is already in the OSM data), visit 6 to 10 per outing in the late morning or mid-afternoon (outside lunch/dinner rush for food places), leave a QR card if the owner is absent. First step: have `foundry` export a route-ordered visit sheet (it fits DUS-53, the shortlist and review sheet).
2. **Manual message from the owner's own account to the business's Facebook Page or Instagram, only for social-only leads.** One personal, specific message per business (the demo link, how the owner found them). Not scripted at volume, not sent from a bot, no follow-up spam. First step: add a `social_url` column from the OSM tags the verify step already reads.
3. **Hand-mailed First-Class postcard with a QR code to the demo**, to the street address, as the fallback for businesses that are closed or hard to catch. About $0.65 postage (VERIFIED, July 12 2026 rate, secondary news source) plus printing. Only for the top-scored leads, in small test batches of 50 to 100 to measure the real response rate.

Do **not** do: texting, auto-dialing, scraping emails, buying contact-finder lists, or bulk-DMing. Reasons in section 4.

## 2. Channels ranked

Rates below are **ASSUMED** unless a source is cited. No credible public benchmark exists for "web design pitch to a no-website local business", so treat every number as a prior to be replaced by the owner's own first 50 contacts. Track outcomes in `leads.json` (contacted, replied, won).

| Rank | Channel | Owner time | Cash cost | Rough expected replies (ASSUMED) | Legal/platform risk |
|---|---|---|---|---|---|
| 1 | Walk-in with demo | ~6 to 10 visits/hour of owner time once batched, plus travel | $0 to $0.10 (a QR card) | Reach a decision-maker on maybe 30 to 50% of visits; a positive conversation on maybe 5 to 15% of those reached. Roughly 1 real conversation per 1 to 2 hours. | Low. See walk-in notes. |
| 2 | Manual FB/IG message to the business's Page | ~3 to 5 min each | $0 | Reply rate for a specific, personal DM to a small business: maybe 10 to 25%, many of them "not interested" | Low if manual, one-to-one, low volume. Gray if repeated or scripted. |
| 3 | Postcard (First-Class, own address list) | ~1 to 2 min per piece once the template is set | ~$0.70 to $1.00 each all-in | Cold mail: sources range 0.9% (UK cold, all sectors) to 2.0 to 4.4% (prospect lists, mixed sectors). Plan on 0.5 to 2% for this offer. 100 cards = ~$70 to $100 for 0.5 to 2 replies. | Very low. |
| 4 | Phone call to businesses where Overture adds a number | ~20 dials/hour, owner time heavy | $0 | Reach a human maybe 20 to 30%; interest in single digits | Moderate, see TCPA/Maryland. Only a manual, voice call by the owner. |
| 5 | Cold email, if an address is found | Minutes per email | $0 | Low and unknowable (ASSUMED 1 to 5% reply on well-targeted small-business email) | CAN-SPAM compliance needed; address sourcing is the problem. |
| 6 | Text message | Low | $0 | Unknown | Highest legal exposure per message. Skip. |

Per dollar, walk-ins and Page DMs win (free). Per owner hour, walk-ins win once batched because travel is shared; DMs win on pure typing time but have a small audience (only social-only leads). Mail is the only channel that scales without owner time, but at 0.5 to 2% and about $0.80 a piece, it costs roughly $40 to $160 per reply (REASONED from the assumed rates), against a site priced $300 to $1,500. It can still pay, but test small.

## 3. Channel details and rules

### Direct mail
- **USPS price (July 12 2026):** domestic postcard stamp $0.65, Forever stamp $0.82, metered letter $0.78. Source is a news summary of the PRC-approved increase; some outlets still described it as pending. REASONED to be current; confirm on usps.com before printing.
- **EDDM Retail:** about $0.260 per piece, no permit, flat size up to 3.3 oz (multiple vendor pages, not usps.com). But EDDM goes to every address on a carrier route, not to a named address. For a short list of specific storefronts it wastes money on residences; it only makes sense for a route that is mostly one shopping strip. REASONED.
- **Print-and-mail APIs (options only; owner sends everything):** Lob lists postcards "starting at" $0.872, $0.612, $0.582 depending on tier (its pricing page, fragmentary). Thanks.io lists 4x6 at $0.54 standard / $0.59 First-Class and 6x9 at $0.61 / $0.66; Stannp 6x9 at $0.56 to $0.61 (vendor pages). PostGrid does not publish prices. At 50 to 100 pieces a month, the volume tiers likely do not apply, so budget about $0.75 to $1.00. Self-printing 4x6 cards and stamping them costs about $0.70 to $0.80 and takes a few hours per 100, which is fine for tests.
- **Rules:** CAN-SPAM covers email only, so no federal marketing-mail statute applies. Including the sender's name, address and "reply to stop" is good practice. Mailing to a public street address from OSM is fine (OSM data is ODbL; ASSUMED OK for mailing, ODbL attribution applies to publishing the database, not to sending a card).
- **Response-rate sources:** ANA/DMA figures are quoted second-hand: average 4.4%, house lists 5 to 9%, prospect lists 2.0 to 4.4%, and a UK cold-mail figure of 0.9%. I could not open the ANA report itself. These blend sectors and mostly describe consumer offers. One source states plainly there is no reliable public benchmark for B2B postcards. Treat as an upper bound.

### Walk-ins
- No source gives a reliable rate; the table values are ASSUMED. The safest design is a pilot: 30 visits, log owner present / conversation / interest / yes.
- **Batching:** cluster by walkable street segment, ordered by closing time (restaurants after lunch before dinner, salons midweek, trades early). Use the 1D lead score to pick the top 6 to 10 per cluster. Bring the demo on a phone, a printed QR card, and a business card.
- **Law:** The "peddler/solicitor license" rules I could find are written for door-to-door selling and I could not open the official Annapolis or Anne Arundel code (an aggregator site says a license is required, ASSUMED and unverified). Walking into an open business during hours to offer a service is generally treated differently from residential door-knocking, but ASSUMED. Check Annapolis City Code and Anne Arundel County Code, or ask the city clerk, before the first outing. Always honor a "no soliciting" sign or a request to leave.

### Social-only businesses (Facebook, Instagram)
- **Meta Messenger Platform policy (opened):** promotional content is allowed within the 24-hour window after the user messages the Page. Outside that window you need approved message tags, and "use of tags outside of approved use cases may result in restrictions". The page does not directly address a person messaging a Page cold. That policy governs *Page-to-user* automated messaging; it is not the rule for a person writing to a business.
- **Facebook Terms (opened):** no automated data collection without permission; do not "use the services to send spam".
- **Instagram:** I could not open the Terms. Secondary summaries say Instagram bans "repeatedly contacting people for commercial purposes without their consent" and unsolicited bulk messaging. ASSUMED accurate; confirm in the live Terms.
- **Practical rule (REASONED):** a Page exists to receive messages from the public. One manual, personal, relevant message from the owner's own account is ordinary use. Anything automated, templated at volume, sent from several accounts, or repeated after silence risks restrictions or a ban, and the owner has said no rule-breaking. Do not use browser automation, Meta API "outreach", or DM tools. The agents can *draft* and the owner pastes and sends.
- Personal profiles: do not message an owner's personal profile; use the business Page.

### Google Business Profile
- There is **no legitimate cold-outreach path through GBP** that I found. The only mechanism is the "request ownership" flow, which exists so a person can claim their own listing. Using it as a way to contact someone else's business would misuse the flow (REASONED).
- Google's own guidance warns owners to distrust unsolicited contacts offering profile help, so pitching "we manage your Google listing" to cold leads also hits a scam-adjacent reputation. VERIFIED (support.google.com/business/answer/14509283).
- **Places API data:** Google's policy says you must not pre-fetch, cache or store Places content beyond place IDs (VERIFIED, developers.google.com policies page). The pipeline note 1A-2 already flags this. I could not open the full Maps Platform Terms to check for an explicit bar on lead lists or telemarketing; assume it applies. REASONED: using Places phone numbers to build a stored call list is likely a terms problem. Looking one up by hand while verifying a lead is a different matter, but the exact boundary is UNVERIFIED.

### State business registries (MD SDAT, VA SCC, DC CorpOnline)
- **Virginia SCC CIS:** the public search returns entity name, SCC ID, type, formation date, status, principal office address, and registered agent (secondary summaries). I could not load the SCC page.
- **Maryland SDAT:** the Business Entity search is public. Bulk data is sold through a contractor (SpecPrint), per a Maryland Attorney General Public Information Act opinion (PIACB 19-12, 2019; I saw only its summary). Current price and licence terms not found.
- **DC CorpOnline:** the DLCP page returned 404; nothing verified.
- **What they give you:** registered agent and principal office, which for many small businesses is a lawyer, a registered-agent company, or the owner's home. They rarely give a direct phone or email. Owner names are sometimes shown for sole-proprietor trade names (Maryland trade-name filings).
- **Is outreach with it allowed?** I found no statute or published term that bans commercial use of the *public search results* in these three states. I did **not** open their terms, so UNVERIFIED. Automated scraping of the search sites is a different question and likely breaches site terms or triggers CAPTCHAs; do not scrape. Use is a manual lookup of a few top leads.
- **Gotcha:** mailing a personal home address found this way is legal but feels intrusive, and registered-agent addresses are useless. REASONED recommendation: use a registry only to find the *owner's name* for a card addressed to "Owner, Business Name", and mail to the storefront.

### Cold email (CAN-SPAM)
VERIFIED from the FTC guide (ftc.gov, opened):
- It applies to B2B email; there is no business exemption.
- Required: accurate From/To/Reply-To; subject line that matches content; clear disclosure that it is an ad; a valid postal address; a clear opt-out; honor opt-outs within 10 business days; do not sell or transfer opted-out addresses.
- Penalty up to $53,088 per violating email.
- Harvesting addresses from sites or generating guesses (a dictionary attack) is an aggravated violation; criminal penalties are possible.
- **Consequences for site-foundry:** (1) never guess `info@domain` or generate addresses; (2) use only an address the business itself publishes for contact; (3) the existing drafts already carry name, address and opt-out, but also check each has the "advertisement" disclosure; (4) keep an opt-out suppression list so a `foundry` run never re-drafts to someone who opted out. Because most remaining leads have no email at all, this channel is small.

### Cold calls and texts
**Federal (VERIFIED for the facts cited; sources opened or search-confirmed as noted):**
- **National Do Not Call:** the FTC Q&A (opened) says most calls to a business made to solicit sales from that business are exempt from the DNC rules. The registry covers consumers' personal numbers.
- **Cell phones and sole proprietors (key risk):** many small-business numbers are the owner's personal cell. A secondary source reports a court ruling (Chennette) that treats a mixed-use number listed on the registry as presumptively residential for standing, with the caller bearing the burden of proving it is a business number. An FCC 2023 order (89 Fed. Reg. 5098, Jan 26 2024) extended registry protection to marketing *texts* to wireless numbers. Details on business exemptions in that order were not confirmed. REASONED: a text to a sole proprietor's cell is the single highest-risk contact in this whole plan.
- **Autodialers/texts:** after *Facebook v. Duguid* (2021) the autodialer rule is narrow, so manually typed texts to stored numbers mostly fall outside it. But the DNC and state rules above still apply, prerecorded and artificial-voice calls remain restricted, and a manual-send policy needs real proof (do not use any bulk SMS tool).
- **One-to-one consent rule:** vacated by the Eleventh Circuit in January 2025 (law-firm summaries; I did not open the opinion). It never took effect. The "revoke-all" rule was delayed to January 31, 2027 (summaries). Not relevant to manual one-off contact, but it shows the rules are still moving.
- Call between 8 a.m. and 9 p.m. local time (federal rule; ASSUMED standard).

**Maryland (VERIFIED: I read the enrolled text of SB 90, Chapter 413, 2023, effective Jan 1 2024):**
- It adds Commercial Law Title 14, Subtitle 45. Consent: calls using an automated dialing system or recorded message need prior express written consent.
- Any telephone solicitation (the Act's text says "including" autodialed or recorded) may not be made between 8 p.m. and 8 a.m., or more than 3 times in 24 hours on the same subject. Caller ID must not be blocked or spoofed.
- A violation is an unfair or deceptive trade practice under Title 13, so the Attorney General can enforce and (per Kelley Drye) individuals can sue. Kelley Drye also reports penalties up to $10,000 per violation ($25,000 repeat).
- **Important correction to the usual summary:** secondary summaries say "business-to-business sales are exempt". The statute text I read says the B2B exemption applies *where the telephone solicitor has been lawfully operating continuously for at least 3 years under the same business name*. The owner's business is new, so the exemption **very likely does not protect the owner**. REASONED from the text. The chapter PDF I extracted has struck-through language flattened out, so the section numbering (14-4502 vs 14-4503) looked duplicated; confirm against the codified statute at mgaleg.maryland.gov before relying on it.
- The statute I read has no private right of action for texts with a 15-day cure. A law-firm summary mentions one; I could not verify it in the chapter text. Treat as UNCONFIRMED.
- The statute defines "telephone solicitation" by reference to Public Utilities §8-205: "an organized activity, program, or campaign to communicate by telephone with residents of Maryland". Plus a rebuttable presumption that a call to any Maryland area code is to a Maryland resident or business. A handful of one-to-one calls to storefronts is arguably not an "organized campaign", but a repeatable lead pipeline calling many businesses looks like one. REASONED.

**Virginia:** the Telephone Privacy Protection Act, amended by SB 1339 (Chapter 626), took effect Jan 1, 2026 per law-firm summaries and the Virginia DLS: texts are treated as solicitation calls, and a "STOP" reply must end messaging for 10 years. I did not open the statute. **DC:** nothing researched. Treat DC texting as unresearched.

**Practical rule (REASONED):** if the owner calls, call as a person, by hand, no autodialer, no recorded message, daytime hours, real caller ID, keep a do-not-call list, never call twice after a "no", and give the business name in the first sentence. Do not text any number unless the person has asked you to (for example, "text me the link" in a call). That one reply makes later texts consensual in practice, and the owner should save the record.

### Contact-finding services
- **Hunter.io terms (opened):** require compliance with applicable law and data-protection rules, forbid copying their website material; they do not address cold outreach explicitly. It finds work emails by domain, so mostly useless for no-website businesses.
- **Apollo terms (opened):** you may not use their contact data in ways that violate CAN-SPAM, CASL or the TCPA; you are "solely responsible" for lawfulness; no resale; no use to train ML models (relevant to evolve-lab). Mostly B2B corporate contacts; very thin coverage of storefronts.
- **Verdict:** the terms do not bar the owner's use, but the data is poor for this niche and the legal burden stays with the owner. Not worth a subscription yet. Not tested: ZoomInfo, Lusha, RocketReach and similar (not opened).
- **Do not** use anything that scrapes Google Maps, Facebook or Instagram for emails or phones (violates platform terms, Facebook Terms section on automated collection verified above), and avoid sellers of "leads with phone numbers", whose consent provenance is unknowable.

## 4. What would break rules (the owner bans rule-breaking)
- Automated or bulk DMs, or bots sending Page messages, on Facebook/Instagram (spam policy; account loss).
- Scraping Google Maps/Places, Facebook or Instagram for contacts, or storing Places data beyond IDs.
- Guessing or harvesting email addresses (CAN-SPAM aggravated violation).
- Texting sole-proprietor cell phones (DNC, Maryland, Virginia exposure).
- Prerecorded or AI-voice calls (federal and Maryland consent requirements). An AI voice agent calling leads would be exactly this. Do not build it.
- Assuming Maryland's B2B exemption covers a business under 3 years old.
- Ignoring "no soliciting" signs; leaving the demo online after a business objects (already in open-problems 2C).

## 5. Rejected, so nobody re-researches
- **Texting leads at scale:** DNC text extension, mixed-use cell numbers, Maryland and Virginia rules, class-action exposure. Not worth it.
- **AI cold-calling / robodialing:** consent rules, plus the owner's reputation. No.
- **GBP ownership-request flow as outreach:** misuse of the flow.
- **Scraping state registries:** automation against site terms; manual lookups are enough.
- **Hunter/Apollo as a primary channel:** low coverage of no-website storefronts.
- **EDDM for named targets:** reaches residences on the route; wasteful for a short storefront list.

## 6. Unknowns to close next (cheap)
1. Anne Arundel County and Annapolis solicitor-licensing code (official text), and whether it applies to entering an open business.
2. Codified Maryland Commercial Law 14-4501 to 14-4504 text and any 2024 to 2026 amendments or cases.
3. The owner's own pilot data: 30 walk-ins, 50 postcards, 10 social DMs, then replace every ASSUMED rate above.
4. Register the business name early; the Maryland B2B exemption needs 3 years of operation under the same name, so this only helps later.
5. Meta's current Instagram Terms (could not open) and the Google Maps Platform Terms (could not open the restriction section).

## 7. Sources (opened this session unless marked secondary)
- FTC CAN-SPAM Compliance Guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business (opened; current penalty $53,088 per email)
- FTC DNC Q&A for telemarketers: https://www.ftc.gov/business-guidance/resources/qa-telemarketers-sellers-about-dnc-provisions-tsr (opened; B2B exemption)
- Maryland SB 90 Chapter 413 (2023), enrolled text: https://mgaleg.maryland.gov/2023RS/Chapters_noln/CH_413_sb0090e.pdf (opened, text extracted; approved May 3 2023, effective Jan 1 2024)
- Kelley Drye on Maryland's law (secondary, omits the 3-year condition): https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/marylands-new-telemarketing-law-now-in-effect
- Meta Messenger Platform policy: https://developers.facebook.com/docs/messenger-platform/policy/policy-overview (opened)
- Meta Spam policy: https://transparency.meta.com/policies/community-standards/spam/ (opened; no mention of DMs)
- Facebook Terms: https://www.facebook.com/terms (opened)
- Instagram terms page: https://help.instagram.com/581066165581870/ (would not load; Instagram claims secondary)
- Google Business Profile security guidance: https://support.google.com/business/answer/14509283 (opened)
- Google Places policies: https://developers.google.com/maps/documentation/places/web-service/policies (opened)
- Hunter terms: https://hunter.io/terms-of-service ; Apollo terms: https://www.apollo.io/terms (both opened)
- FCC one-to-one rule status, revoke-all delay to Jan 31 2027 (secondary search summaries: Steptoe, Varnum, ActiveProspect). FCC 23-107 text-DNC, 89 Fed. Reg. 5098 (Jan 26 2024) (search summary; GAO/govinfo links not opened).
- Facebook v. Duguid (2021), Chennette (mixed-use number presumption): secondary summaries (Bloomberg, Skadden, Faruqi, Orrick) not opened.
- Virginia SB 1339 / Chapter 626, effective Jan 1 2026: secondary (Tenaco, Privacy World blog, Virginia DLS) not opened.
- USPS July 12 2026 prices: news summaries (WDBJ and others) and 3plcenter.com; EDDM $0.260: 4over4 and similar vendor pages. None opened from usps.com (the USPS newsroom URL returned 404).
- Print-and-mail vendor pricing: lob.com/pricing, Thanks.io, Stannp (search summaries only).
- Direct mail response-rate summaries: 4over4.com, directmail.io, focus-digital.co (vendor/secondary; ANA/DMA original not opened).
- Maryland AG PIACB 19-12 on SDAT bulk data: https://www.marylandattorneygeneral.gov/Opinions PIACB Documents/2019/PIACB19_12.pdf (search summary only).

## Follow-ups closed (2026-10-29, Haiku)

Research only. Nothing contacted, submitted or signed up for. Each item lists the answer, the source, and what is still open. Labels as above: VERIFIED = source opened this session.

### 1. Annapolis and Anne Arundel solicitor / peddler rules: PARTLY CLOSED, primary code NOT reached
- **Annapolis (City Code):** Chapter 7.44 "Solicitors" as quoted by a third-party site: a person may not "solicit or canvass on any public way" without registering in the Office of Law and getting the Mayor's written approval (§ 7.44.010). The same site says it also covers soliciting donations on public ways or calling at homes, with a $50 fee and a dated certificate (§§ 7.44.020 and 7.44.030 cited, not quoted). Chapter 7.40 covers peddlers and hawkers. Sources: https://cityrulelookup.com/soliciting/solicitor-permits/annapolis-md (secondary, says rechecked 2026-09-07); Municode ch. 7.40 listing via search: https://library.municode.com/md/annapolis/codes/code_of_ordinances?nodeId=TIT7BULITARE_CH7.40PEHAITME_7.40.086RERE
- **Anne Arundel County:** the county's own page defines a huckster as "one who moves about the county, or goes door to door offering various products for sale or trade," and sends questions to the License Division, (410) 222-7788. It cites no code section and says nothing about exemptions, hours, or businesses pitching businesses. VERIFIED: https://www.aacounty.org/inspections-and-permits/licenses/non-trade-licenses/huckster-license
- **The "Article 7-8" citation** in the aggregator (cityrulelookup) is unverified.
- **Not reached:** Municode (library.municode.com) and the county's amlegal library (codelibrary.amlegal.com) both return HTTP 403 to both the fetch tool and plain curl. ecode360 had no Annapolis or Anne Arundel hit.
- **Answer (REASONED):** Nothing I read clearly requires a licence for a walk-in pitch to an open storefront, but nothing confirms it either. The City text targets soliciting on public ways and calling at homes; the county text targets door-to-door selling of products. Whether a service pitch to an open business falls under either is UNVERIFIED. Ask the Annapolis Office of Law or the county License Division before the first outing. Do not rely on this list.

### 2. USPS First-Class postcard rate: CLOSED (domestic postcard $0.65)
- **Answer:** Domestic postcard single piece is $0.65, retail and commercial. Source is the USPS Notice 123 Price List as served from pe.usps.com: https://pe.usps.com/text/dmm300/Notice123.htm (VERIFIED this session). The page header reads "Notice 123 • Effective October 04, 2026." It does not name the price change it belongs to.
- **Corroboration:** a Nevada state notice of the July 12 2026 increase (https://www.admin.nv.gov/siteassets/content/documents/pd-2026/2026-07-u.s.-postal-service-postage-increase-notice.pdf, secondary-ish, a state agency document); UML notice on PRC approval May 27 2026 (https://www.uml.edu/myuml/submissions/2026/2026-05-29-15-11-43-usps-july-2026-rate-increases.aspx, secondary).
- **Still open:** no Federal Register notice or usps.com price-table page was opened (the USPS pages I tried returned 403). Check usps.com before printing. The commercial presort postcard rates on the same page (about $0.45 to $0.50) apply only to bulk mail, not the owner's small batches.
- **Note correction:** the July 12 2026 date stands, but the Notice 123 header shows October 04 2026, so the rate is current either way.

### 3. State registry terms of use: PARTLY CLOSED
- **Maryland SDAT:** the terms I could open are on dat.maryland.gov, not the Business Express entity search itself. They say: "You may not use data mining, robots, screen scraping, or similar data gathering and extraction tools on this site" and "Anyone using data mining software will have their access blocked." They also say public records are provided "with some limited exceptions" and "used for a wide variety of government and commercial purposes." No rule against using results for marketing. VERIFIED: https://dat.maryland.gov/about/Pages/Website-Usage-Statements.aspx
  - The Business Express entity search (egov.maryland.gov/BusinessExpress/EntitySearch) showed no terms, only Privacy and Accessibility links (VERIFIED). The terms for businessexpress.maryland.gov itself were not found.
  - **Answer:** a manual lookup of a few records is allowed by everything I read. Scraping is banned. No marketing restriction found. UNVERIFIED: whether Business Express terms say more.
- **Virginia SCC:** the SCC accessibility page says: "Information on the SCC website is public and should not be used for commercial purposes beyond its intended public availability," and "Permission is granted to make fair use of the contents of the SCC website." Questions go to sccinfo@scc.virginia.gov (VERIFIED): https://www.scc.virginia.gov/accessibility-and-web-policy/
  - The Clerk's Information System (cis.scc.virginia.gov) showed only a cookie notice, no terms (VERIFIED: https://cis.scc.virginia.gov/). The accessibility page does not name the CIS.
  - **Answer:** a manual lookup is fine. The sentence above is a real caution against commercial use of SCC content, and it may cover CIS records. UNVERIFIED for CIS. Ask SCC before any marketing use. Do not email them without the owner's OK.
- **DC:** CorpOnline is now BOSS (boss.dc.gov), launched August 10 2026, per the DLCP BOSS FAQ (VERIFIED: https://dlcp.dc.gov/sites/default/files/public/BOSS%20Frequently%20Asked%20Questions%20-%20August%202026.pdf). The FAQ says access is through an Access DC login, and it does not say whether the entity search needs one. The old dlcp.dc.gov/corponline URLs redirect to boss.dc.gov. The boss.dc.gov page did not finish loading, so I found no terms. **UNVERIFIED.** Do not assume DC terms match Maryland's.
- **Answer for all three:** manual look-ups of a few top leads look allowed. Do not scrape, bulk-export or automate. The use restriction in the SCC text is the one to take seriously before any marketing.

### 4. Maryland SB 90 codified text (Md. Code, Com. Law § 14-4501 et seq.): CLOSED, with a correction
- **The 3-year condition is in the codified statute.** § 14-4502(a)(1)(iii): "A business–to–business sale where the telephone solicitor has been lawfully operating continuously for at least 3 years under the same business name." VERIFIED: https://mgaleg.maryland.gov/2026RS/Statute_Web/gcl/14-4502.pdf. The codified text carries no strike-through, so the struck-through flattening in the enrolled bill does not apply to this wording.
- **Correction to the note's reading:** the exemption list in (a)(1) opens "This subsection does not apply to:" and so exempts only subsection (a). Subsection (a)(3) is the prior-express-written-consent rule for automated-dialer and recorded calls. The B2B exemption therefore removes the consent requirement for automated or recorded calls only. It does **not** touch § 14-4502(b) (caller ID) or (c) (8 p.m. to 8 a.m. limit, more than 3 calls to the same party in 24 hours on the same subject, and voice disguise). Those apply to every telephone solicitation, B2B or not, and they apply to a human-dialed call too. Read as written. Confirm with counsel. Source for the scope: same PDF.
- **Definitions:** § 14-4501(f) says "Telephone solicitation" has the meaning in Public Utilities § 8-205. VERIFIED: https://mgaleg.maryland.gov/2026RS/Statute_Web/gcl/14-4501.pdf
- **Unverified:** the § 14-4503 and 14-4504 numbering (not opened), and any 2024 to 2026 amendments beyond the 2026 codification I read. Text came from the codified PDF, not the bill.

### Net effect on the plan
- A 3-year-old business name is needed for the B2B carve-out from the consent rule, so the owner cannot use it yet. That only matters for automated or recorded calls, which the plan already rules out.
- Manual calls still face the 8 a.m. to 8 p.m. window and the 3-calls-per-24-hours cap in § 14-4502(c). Keep both in any call routine.
- Use the state registries only for manual look-ups. Treat the SCC "should not be used for commercial purposes" sentence as a reason to ask before any marketing use of Virginia records.
