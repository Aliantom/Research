<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Outreach compliance for site-foundry (DC, Maryland, Virginia)

> **TL;DR:** Manual cold email works with CAN-SPAM fixes and a suppression list; cold calls need DNC scrubbing and Virginia rules; skip cold SMS; Google Places terms bar storing its data. Not legal advice.
> **Source:** Owner request 2026-11-02: rules that apply before any site-foundry cold outreach in DC, Maryland and Virginia  ·  **Project:** site-foundry  ·  **Updated:** 2026-11-03

For owner awareness, not legal advice. Nothing was changed in the repo and nothing was sent. The law here is moving (see texts below), so this reflects what I could read on 2026-11-02.

**Evidence labels.** VERBATIM = I read the primary text directly. SUMMARY = I read the primary page through a summarizing fetch tool, so check the wording before relying on it. SECONDARY = law-firm or other commentary, opinion not read. REASONED = my reading, no court or agency source says it. ASSUMED = from memory, not checked. I read no court opinions in full.

## Bottom line

| Channel | Verdict | Why |
|---|---|---|
| Manual cold email | **Workable after fixes** | B2B gets no CAN-SPAM exemption, but no consent is needed. It needs an ad identifier, opt-out handling and suppression. State laws only add "don't lie", though with $500 per email private suits in MD and DC. |
| Manual cold call | **Workable with process, moderate risk** | Federal DNC rules largely exempt real business lines. Virginia's text has no B2B carve-out and many small-business numbers may be owners' personal cells. Scrub against the registry and follow the strictest rules. |
| Cold SMS | **Don't** | Expressly covered in Virginia, covered by the FCC rule, a live court split, and the worst fit with "personal cell". Text only after the owner of the business asks. |
| Autodialer, prerecorded, AI voice, bulk SMS tool | **Never** | MD, VA and DC each restrict these and the federal penalties are per call. Also barred by repo rules. |
| Google Places data | **Do not store or build demos from it** | Terms bar saving names, addresses and reviews, and bar use with a non-Google map. None is stored today. |
| OSM and Overture data | **Fine, with a credit line** | Licences allow this. Demos currently lack a data credit. Don't share the lead file. Licences do not give permission to contact anyone. |

**Biggest gaps today:** no suppression list in the pipeline, drafts lack a clear "this is a solicitation" line, placeholder sender details don't block a draft, and there is no phone process at all (DNC date, line type, script).

## How the pipeline works now (read from the repo)

- Leads come from OSM via Overpass (`leads.py`), filled in from a local Overture Places parquet (`enrich.py`). `drafts` writes `out/drafts/<slug>.md` with `status: needs-review`. Nothing sends. `out/` and `.env` are gitignored.
- Current `out/leads.json`: 100 leads, 64 with a phone, 42 with an email, 59 with contact data sourced from Overture. **20 of the 42 emails are on gmail, yahoo, hotmail or similar**, which suggests some are personal addresses of owners. Phone line type is not recorded.
- `grep` for suppression, opt-out or contacted fields in `src/` found none, and `out/drafts/` is currently empty.
- **Google:** I found no Places API call, `place_id` or `googleapis` reference in `src/`, `tests/`, `docs/` or `out/`. `docs/open-problems.md` only proposes Places as a future step (1A-2, build step 5). The code's Google references are a blocklisted directory domain, Chrome's path and a plain `google.com/maps/dir` Directions link in demos, which is a link, not stored data. This was a keyword search of known identifiers, so it is strong but not a proof about every value's origin.

## 1. Email

### Federal: CAN-SPAM, applies to B2B

- FTC: "The law makes no exception for business-to-business email." Up to $53,088 per violating email on the FTC page, which was last updated January 2024, so the current figure may be higher. (SUMMARY, [FTC guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business))
- No prior consent is required. It is an opt-out regime. (REASONED from the FTC guide's list of requirements.)
- Required in each message, per [15 USC 7704](https://www.law.cornell.edu/uscode/text/15/7704)(a)(5) (VERBATIM): clear and conspicuous identification as an advertisement or solicitation, clear and conspicuous notice of the opportunity to decline, and a valid physical postal address.
- Also required (FTC guide, SUMMARY): accurate headers, non-misleading subject, opt-out that works for 30 days after sending, honored within 10 business days, no fee or extra steps, and opted-out addresses never sold or transferred. A PO box or registered private mailbox satisfies the address rule, so the owner need not publish a home address.
- Address harvesting is an aggravated violation only when automated collection from a site with a no-transfer notice, or dictionary generation, is involved (15 USC 7704(b)(1), SUMMARY). `foundry verify` fetches homepages but does not extract emails. Keep it that way. Any future email scraper raises this risk.
- Only the FTC, states and internet access providers can sue under CAN-SPAM, not ordinary recipients (15 USC 7706, SUMMARY for (g); the rest REASONED). Practical private exposure therefore comes from state law.

### State add-ons

CAN-SPAM preempts state email statutes except where they prohibit "falsity or deception" ([15 USC 7707(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2023-title15/html/USCODE-2023-title15-chap103.htm), SUMMARY). The Fourth Circuit, which covers MD and VA, read that narrowly in *Omega World Travel v. Mummagraphics*, 469 F.3d 348 (2006) (SECONDARY). All three local laws are in fact deception laws. None adds its own opt-out or consent rule that I found.

| | Maryland CEMA | Virginia | DC Spam Deterrence |
|---|---|---|---|
| Cite | [Com. Law 14-3001](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3001) to [3003](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3003) (SUMMARY) | [18.2-152.3:1](https://law.lis.virginia.gov/vacode/title18.2/chapter5/section18.2-152.3:1/), [152.12](https://law.lis.virginia.gov/vacode/title18.2/chapter5/section18.2-152.12/) (SUMMARY) | [28-5001](https://code.dccouncil.gov/us/dc/council/code/sections/28-5001), [5002](https://code.dccouncil.gov/us/dc/council/code/sections/28-5002), [5003](https://code.dccouncil.gov/us/dc/council/code/sections/28-5003) (VERBATIM) |
| Bars | Third-party domain without permission, false origin or path, misleading subject | Falsifying or forging routing information in connection with spam (crime; felony tiers by volume or revenue) | False routing or header info, false or misleading subject, using a third party's identity |
| Reach | From MD computer, or address the sender knows or should know is a MD resident's; knowledge presumed if the domain registrant would say so on request | Spam through or into a provider's network | From a DC computer, or to a DC resident's address, DC-based provider or DC-registered domain |
| Private remedy | Recipient: greater of $500 or actual, plus attorney's fees | Injured person: lesser of $10 per message or $25,000 per day, plus fees, where spam breaches provider policy | Non-provider: actual plus $500 per message or $50,000 per day, whichever is less, plus fees |

- **Maryland's status:** a 2004 circuit court ruling struck CEMA down as applied. A 2006 appellate decision, *MaryCLE v. First Choice*, reversed that case, but I confirmed only that from commentary, not the constitutional reasoning (SECONDARY). Commentators describe CEMA class actions still being filed in 2026. Treat it as live.
- **Consequence for the draft:** the subject line is the state-law pressure point. "A free website preview for {name}" is true of the preview, but the actual offer is paid work. A plaintiff could call that misleading. I rate this low to moderate given the body explains the price model, but it costs nothing to fix. (REASONED)

## 2. Calls and texts

### Federal (TCPA, FCC rules, FTC TSR)

- **Manual call, not prerecorded:** the autodialer rules don't reach it. *Facebook v. Duguid* (2021) limits "autodialer" to random or sequential number generation (SECONDARY). Clicking through a list by hand is the safe pattern. Prerecorded voice rules apply regardless ([47 CFR 64.1200(a)](https://www.law.cornell.edu/cfr/text/47/64.1200), SUMMARY).
- **FTC TSR:** calls "between a telemarketer and any business" are exempt, except for retail sale of nondurable office or cleaning supplies, and the misrepresentation rules still apply ([16 CFR 310.6(b)(7)](https://www.law.cornell.edu/cfr/text/16/310.6), VERBATIM). The FTC says "most" such calls are exempt ([FTC Q&A](https://www.ftc.gov/business-guidance/resources/qa-telemarketers-sellers-about-dnc-provisions-tsr-0), SUMMARY).
- **FCC national DNC:** the rule protects a "residential telephone subscriber" (64.1200(c)(2)). The FCC's 2003 order says DNC rules "will also not prohibit calls to businesses" (¶37) and that it "declined to permit businesses to register their numbers", but "a business could nevertheless request that its number be added to a company's do-not-call list" (final regulatory flexibility analysis). Same order: wireless subscribers may participate (¶36). (VERBATIM, [FCC 03-153](https://docs.fcc.gov/public/attachments/FCC-03-153A1.pdf))
- **So B2B is exempt only if the line is really a business line.** The definition of "telephone solicitation" covers calls "to any person" (f)(15), and the protection turns on the subscriber being residential. A hairdresser whose listed number is her personal cell is the hard case. *Dobronski v. Tony Packo's* (E.D. Mich. Oct. 2, 2026) held that a number used for business when registered was void on the registry, which helps. It is one non-binding district ruling and turned on use at registration (SECONDARY, [Greenspoon Marder](https://www.gmlaw.com/news/eastern-district-of-michigan-dismisses-tcpa-claims-based-on-invalid-do-not-call-registry-registration/)). Mixed-use cell phones are unresolved in what I found.
- **Remedy:** private suit after more than one call in 12 months, up to $500 per violation, with a defense for due-care procedures ([47 USC 227(c)(5)](https://www.law.cornell.edu/uscode/text/47/227), VERBATIM). One call to a registered number is thus less exposed federally, but Virginia has no such threshold (below). (REASONED)
- **Company-specific DNC:** record requests and honor them within 10 business days at most, and give the caller's name, the entity's name and a contact number (64.1200(d)(3), (d)(4), SUMMARY). Quiet hours: 8 a.m. to 9 p.m. local (64.1200(c)(1)).
- **Registry access:** up to five area codes free; $85 per additional area code from October 1, 2026; sole proprietors enter an SSN if no EIN (FTC Q&A, SUMMARY). The DMV has more than five codes (ASSUMED: 202, 771, 301, 240, 227, 410, 443, 667, 703, 571, 540), so start with one region. Annapolis fits in the free tier.

### Texts: unsettled, so plan for the bad outcome

- The FCC's rule applies (c) and (d) to "telephone solicitations or telemarketing calls or text messages to wireless telephone numbers" (64.1200(e), VERBATIM).
- *Steidinger v. Blackstone Medical* (7th Cir. July 14, 2026) held texts aren't "telephone calls" for the private suit in 227(c)(5). *Card v. R.J. Reynolds* (M.D.N.C. Sept. 3, 2026) followed it, reported as the first in the Fourth Circuit. Courts in California, Pennsylvania and Texas went the other way in October 2026. No Fourth Circuit or D.C. Circuit ruling found. *Steidinger* is limited to the private suit and leaves FCC enforcement alone. (SECONDARY: [K&L Gates](https://www.klgates.com/thought-leadership/Litigation-Minute-Seventh-Circuit-Rules-That-Text-Messages-Are-Not-Telephone-Calls-Under-the-TCPAWhat-To-Know-and-What-Comes-Next-8-5-2026), [Duane Morris](https://blogs.duanemorris.com/classactiondefense/2026/09/09/first-district-court-in-the-fourth-circuit-holds-that-the-tcpas-do-not-call-provision-does-not-cover-text-messages/), [Bubeck](https://www.bubecklaw.com/privacyspeak/no-treats-for-tcpa-defendants-three-more-courts-say-texts-are-calls))
- That split gives little comfort here, because Virginia covers texts by statute, and Maryland separately forbids violating the TCPA "as implemented by" the FCC rule (next section). (REASONED)
- A consent note: for a registered number, consent has to be a signed written agreement including the number (64.1200(c)(2)(ii), VERBATIM). An inquiry by the business within three months is a separate route under the established business relationship definition, and that definition is written for residential subscribers (f)(5) (SUMMARY). See *King v. Bon Charge* (D. Del. Apr. 30, 2026) on the difference between these consent types (SECONDARY).

### Virginia: the strictest, and no B2B carve-out in the text

[Virginia Telephone Privacy Protection Act](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-510/), amended by 2025 c. 626, effective January 1, 2026 (date SECONDARY; text VERBATIM):

- **Scope:** "telephone solicitation" includes any call "to any landline or wireless telephone with a Virginia area code" and "any text message sent to any wireless telephone with a Virginia area code", for offering goods or services. I read §§ 59.1-510 to -518 and found no business exemption.
- **DNC:** [§ 59.1-514(B)](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-514/) bars solicitations to a number on the National DNC Registry. The exceptions are a signed written agreement, an established relationship or a personal relationship. Defense: reasonable procedures, including a registry copy no more than 31 days old.
- **Opt-out:** honored for **at least 10 years**. For texts, by replying UNSUBSCRIBE or STOP.
- **Time:** 8 a.m. to 9 p.m. at the contacted person's location ([§ 511](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-511/)).
- **Identification:** first and last name and the seller's name, promptly ([§ 512](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-512/)).
- **Caller ID:** must send a number that takes do-not-call requests during business hours; no blocking ([§ 513](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-513/)). So no `*67`.
- **Remedy:** a "natural person who is aggrieved" gets $500 for a first violation, $1,000 for a second, $5,000 for each after, plus fees, with no two-call threshold, and it can be filed in small claims ([§ 515](https://law.lis.virginia.gov/vacode/title59.1/chapter44/section59.1-515/)). AG and local attorneys can enforce too (§ 517).
- **Reading:** a sole proprietor is a natural person and a business number with a 703 code fits the plain text. An argument remains that a business number can't validly be on the registry, which would defeat (B) but not the opt-out, time or ID rules. I found no Virginia decision on this. Treat every Virginia-code number as covered. (REASONED, **lawyer question**)
- Prerecorded or synthesized devices need consent or a live operator first ([§ 59.1-518.2](https://law.lis.virginia.gov/vacode/title59.1/chapter44.1/section59.1-518.2/), VERBATIM). AI voice is out.

### Maryland

- **[Stop the Spam Calls Act](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-4502), Com. Law 14-4501 to -4503,** effective January 1, 2024 (VERBATIM for 4501 and 4502; SUMMARY for 4503):
  - (a)(3): no automated selection or dialing, and no recorded message, without signed written consent. Written consent covers calls, texts and voicemail.
  - (a)(1)(iii) exempts "a business-to-business sale where the telephone solicitor has been lawfully operating continuously for at least 3 years under the same business name". **A new business doesn't qualify, and it exempts subsection (a) only.**
  - (b): must transmit real caller ID.
  - (c): **no calls between 8 p.m. and 8 a.m.**, no more than three times in 24 hours on the same subject, no voice disguise to defraud. These have no B2B exemption.
  - Remedy: greater of $500 or actual, and up to treble if willful ([14-4503](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-4503)). In-state area codes are presumed to reach someone who lives or **has a business** in Maryland, which suggests businesses are in scope. (REASONED)
- **[14-3201](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3201) and [3202](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-3202)** (VERBATIM): violating the TCPA or TSR is a state violation. An affected individual gets fees and the greater of $500 or actual. This imports the federal rules, including the residential limit and arguably the FCC's text rule, into a state claim. No separate Maryland DNC list found.
- **Telephone Solicitations Act, [14-2201](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-2201)** (SUMMARY) concerns consumer goods and services, primarily personal or household. A business website looks outside it. (REASONED)
- [PUC 8-205](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gpu&section=8-205) supplies the definition: an "organized activity, program, or campaign" to communicate by phone with "residents of Maryland". I read the definition only.

### DC

- **[34-1701](https://code.dccouncil.gov/us/dc/council/code/sections/34-1701)** (SUMMARY): bars prerecorded or synthesized solicitation systems, unless there is a preexisting relationship about prior purchases. Civil penalty up to $1,000, then $5,000.
- **[22-3226.01 and following](https://code.dccouncil.gov/us/dc/council/code/sections/22-3226.01)** (VERBATIM): a "telephone solicitor" must register and post a **$50,000 bond** ([.03](https://code.dccouncil.gov/us/dc/council/code/sections/22-3226.03)); failing to is listed as telephone solicitation fraud ([.06](https://code.dccouncil.gov/us/dc/council/code/sections/22-3226.06)). But the term excludes someone who "does not accept payment for the sale of good or services in that telephone call". "Consumer" means anyone who may have to pay, which isn't limited to individuals. So **never take payment on a call to a DC number**. (REASONED; I don't know how this is enforced. **Lawyer question** before DC calling.)
- **CPPA, 28-3901 and following:** $1,500 per violation or treble damages for consumers ([DC OAG](https://oag.dc.gov/consumer-protection/other-consumer-help-agencies-and-websites/submit-consumer-complaint/district-columbia-consumer-protection-laws), SUMMARY). It is consumer-focused, and I did not confirm whether a small-business buyer qualifies.
- I found no DC-specific DNC list or mini-TCPA for live calls. My search on this was limited, so absence isn't confirmed.

### One rule set for all three

Use the strictest of each. It's simpler than tracking jurisdictions:

- Manual dial only, live human only, no voicemail drops.
- Call 9 a.m. to 7 p.m. local in practice. The legal outer limit is 8 a.m. to 8 p.m. (MD).
- First and last name and business name right away, a contact number if asked, real caller ID.
- Scrub the registry no more than 31 days before each call. Skip registered numbers in all three, as a policy choice.
- Record any "don't call" on the spot, apply it across phone, text and email, and keep it for good (VA's minimum is 10 years).
- Don't take payment on a cold call.
- Never call a number that seems to be a home or personal line, unless it is on a business's own storefront, site or profile, and even then the registry check applies.

## 3. Data terms

### Google Places: not stored today, and the planned use conflicts with the terms

[Maps Platform Terms](https://cloud.google.com/maps-platform/terms), last modified August 26, 2026, section 3.2.3 (VERBATIM):
- (a) No Scraping: Customer will not "pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services" or "copy and save business names, addresses, or user reviews".
- (b) No Caching except as the service terms permit.
- (c) No creating content based on Google Maps Content.
- (e) No Use With Non-Google Maps: will not "display or use Places content on a non-Google Map".

[Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms), last modified October 28, 2026 (VERBATIM): may use Places content without a Google map, not "in conjunction with a non-Google map" (14), may cache latitude and longitude for 30 days (14.3), and may cache `place_id` (A.3). [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies) (SUMMARY): place IDs can be stored indefinitely, and attribution must be visible and unmodified.

**What this means (REASONED):**
- Writing a Places phone, hours, website or address into `leads.json` conflicts with (a) and (b).
- Building a demo from Places facts conflicts with (a) and (c), and the demo's OpenStreetMap iframe adds (e).
- A boolean like "Google lists a website" saved after a live lookup is a greyer derived value. Only `place_id` is clearly safe to store. Using Places for verification needs reading the current terms first, and possibly a lawyer's view if it becomes core.
- `docs/open-problems.md` table 1C says "use phones from OSM or Places". That's the line to change. The note at 1A-2 ("keep only what the terms allow") is right, but in practice that allowance is close to nothing beyond `place_id`.
- A person looking a business up by hand in Google Maps is a different matter, governed by consumer terms that I did not read. Scraping that page is not OK, and the same goes for tools that do it.

### OpenStreetMap: ODbL

- Attribution must be to "OpenStreetMap", linked to openstreetmap.org/copyright where possible, and placed so anyone exposed to the work sees it without having to interact ([OSMF guidelines](https://osmfoundation.org/wiki/Licence/Attribution_Guidelines), SUMMARY).
- A public Produced Work needs a notice that the contents come from the database under the ODbL ([ODbL 4.3](https://opendatacommons.org/licenses/odbl/1-0/), SUMMARY).
- **Gap:** demos embed the OSM map iframe, whose page credits OSM for the map, but the page's own text credits nobody for the facts (`build.py`). Published demos should have a footer credit.
- Share-alike applies once a derivative database goes to anyone "other than You or under Your control" (ODbL). Internal use doesn't trigger it ([OSMF FAQ](https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ), SUMMARY). `leads.json` mixes OSM with Overture and verification results, so **don't hand the lead file to a contractor, list buyer or the public.** Recipients of a Produced Work can also ask for the data behind it.
- The FAQ says nothing on contact or personal data. ODbL is a data licence, not permission to contact.

### Overture Places

- [Overture attribution page](https://docs.overturemaps.org/attribution/) (SUMMARY): no theme-level licence shown for Places. Sources are listed individually: Meta, Microsoft, PinMeTo and others under CDLA Permissive 2.0, Foursquare under Apache 2.0 with a notice, AllThePlaces under CC0. `enrich.py`'s header calls the whole set CDLA-Permissive-2.0, which is a simplification.
- [CDLA Permissive 2.0](https://cdla.dev/permissive-2-0/) (VERBATIM): sharing data requires including the licence text, and there are no restrictions on results. Overture's page suggests the credit "Overture Maps Foundation". The Foursquare notice applies if that data is redistributed.
- Licences say nothing about privacy or accuracy. A gmail address may be an owner's personal one. The current checklist item ("the contact address is the business's own public one") is the right control, but it should be a real check against the business's own materials.

## 4. Concrete changes (proposals, none applied)

### Draft template (`outreach.py`)

Proposed body:

```
**Subject:** Website preview for {name}, from a local web designer

Hi,

I'm {sender}, a local web designer. This is a sales message: I sell websites to local businesses,
and I made a preview for {name} from public listing details so you can see what you'd get:

{demo_url}

The preview costs nothing. If you'd like the real site, with your photos, services, contact form and
own web address, it's ${price} flat, plus optional hosting and updates.

If you'd rather not hear from me, reply "no thanks" or "stop". I won't contact you again and I'll
take the preview down.

{sender}
{business name, if different}
{address}
```

Why each change:
- Says it is a sales message in the body. This is the plainest way to meet 7704(a)(5)(A)(i). The FTC guide allows leeway in how, but the current "one-time offer" footer is weak.
- Subject no longer leads with "free".
- Moves the opt-out to body text, away from an italic footer, for "clear and conspicuous".
- Removes "one-time offer", because any follow-up would make it false. Decide the policy: no follow-up by email is simplest.
- States a real price if one exists. "Flat price" with no number invites a deception claim if the real offer turns out different (REASONED, low risk).
- "The preview will be taken down" must be true. Expiry and same-day takedown (open-problems 2C) aren't built. Build or do by hand before the first send.
- "local web designer" must be true, and `{sender}` must be the real person or registered trade name.

### Pipeline

1. **Suppression list** (highest priority): a file outside `out/`, because `out/` is disposable. Key on normalized email, phone, domain and `osm_id`. `drafts`, `shortlist` and any future call sheet exclude matches. It must survive `leads --refresh` and `merge`. Never share it.
2. **Refuse placeholder drafts:** `drafts` should fail if `FOUNDRY_SENDER_NAME` or `FOUNDRY_SENDER_ADDRESS` is unset. Today they default to `[YOUR NAME]` and `[YOUR MAILING ADDRESS]`.
3. **Contact log:** date, channel, who and outcome per lead. It is needed for opt-out timing, the 3-in-24-hours rule and any due-care defense.
4. **Lead fields:** `jurisdiction` (from address and area code), `email_kind` (business domain or free mail), `line_type` (manual: storefront, personal cell or unknown), `dnc_checked_on`.
5. **Don't add outreach value to personal contacts:** `shortlist.py` gives +40 for any phone and +25 for any email. Consider lower scoring for free-mail emails and for phones not confirmed as business lines. Home-based categories (some hairdressers, beauty) deserve a flag.
6. **Keep Google out of `Lead`:** add a test or `AGENTS.md` line that no Places-sourced value goes in `leads.json` or demos. Update open-problems 1A-2, 1C and build step 5.
7. **Demo footer:** "Business details from OpenStreetMap (link to /copyright) and Overture Maps Foundation. Preview only." In `build.py`, and extend the `shots` banner check to require it.
8. **Publishing:** check for a personal email on a demo before uploading. The demo currently prints whichever `lead.email` it has as a contact card.
9. **Docs:**
   - `AGENTS.md`'s "CAN-SPAM compliant" line should add the ad identifier and suppression.
   - `outreach.py`'s docstring should mention state rules.
   - Open-problems 1C "Manual calls to business lines are fine" should become "manual calls after DNC scrub; Virginia has no B2B carve-out".
   - 1C's "None beyond normal courtesy" for walk-ins is untested. I didn't research local solicitor or peddler licensing or "no soliciting" rules.
10. **No code for phone or SMS sending** stays as is. Add a call sheet with script and quiet hours only if the owner wants to call.

### Pre-send checklist additions

- [ ] Not on the suppression list
- [ ] From address and name are mine, reply inbox is monitored daily
- [ ] Email looks like the business's own, confirmed on its own materials
- [ ] Message says it's a sales message, includes a real postal address, opt-out in the body
- [ ] Call: registry checked in the last 31 days, it's a business line, within hours, script open, no payment taken

### Suggested rollout

Email and walk-ins first in Maryland, under 20 or so hand-reviewed messages. Calls after scrubbing. Virginia-code numbers last. Texts only on request. (Judgment, not law.)

## 5. Questions for a lawyer

A single consult with a Maryland or Virginia telemarketing or advertising attorney should cover these:

1. Does Virginia § 59.1-514(B) reach a business's listed number, or a sole proprietor's cell, on the registry, and does the 10-year opt-out apply to business lines? (Highest value)
2. How should a mixed-use cell be treated under the FCC rule and Maryland 14-3201?
3. Does DC 22-3226 apply to no-payment B2B calls, and what about the bond in practice?
4. Is CEMA fully enforceable, and is the proposed subject and body OK under CEMA and DC?
5. Does building and hosting an unrequested demo under a business's name and details raise trademark, false-endorsement or right-of-publicity issues, even with the banner and noindex? Not researched here.
6. If Places is ever wanted: can a live check that stores only `place_id` plus a boolean satisfy Google's terms?
7. Business set-up: entity, trade name, local licences, and whether a home address can be avoided. Not researched here.

## 6. What I could not confirm

- Opinions in *Steidinger*, *Card*, *Dobronski*, *MaryCLE*, *Omega* and *Duguid* were not read, only commentary. *Duguid* is settled; the rest should be read if relied on.
- SUMMARY-labelled statutes (MD 14-3001 to 3003, 14-4503, VA 18.2-152.x, DC 34-1701) came through a summarizer. Check the wording.
- Any FCC rulemaking in progress on B2B texts: one search found none. FCC revoke-consent timing wasn't confirmed. It isn't needed if every opt-out is honored at once.
- Meta and Facebook messaging terms, local peddler rules, carrier A2P/10DLC rules for SMS and postal rules were not researched.
- The FTC penalty figure may be out of date.

## Related

site-foundry brief, [2026-10-29 Reaching leads without phone or email](2026-10-29-reaching-leads-without-phone-or-email.md)
