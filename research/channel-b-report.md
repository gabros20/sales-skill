# Channel B report — the X/Twitter practitioner corpus

Lead: sales-lead-b · Date: 2026-08-03 · Pack: `sales` (14th and final)
Raw files: `research/raw/_raw-b1-founder-led-sales.md` · `_raw-b2-ai-outbound.md` ·
`_raw-b3-pipeline-forecast-crm.md` · `_raw-b4-methodology-buying-side.md`

**Surface: xrelay (X/Twitter) ONLY for every claim in this channel.** No WebSearch (crew-wide quota
exhausted mid-run), no WebFetch. Every permalink in every raw is a tool-returned `url` field — none
reconstructed. Where this channel reports a NULL, that null is scoped to X and says so.

**Execution note (affects how much weight to give the coverage gaps):** this channel suffered the
xrelay wedge incident. Four sonnet workers were spawned, three fired concurrent searches, X throttled,
and the processes hung and were killed. The controller then stopped all workers and **the lead ran
the entire sweep solo, strictly serialised** (`timeout 90`, `--limit 12–14`, ≥4s gaps, one query in
flight). The corpus below is therefore smaller and more uneven than a four-worker sweep would have
produced — roughly 19 queries rather than the ~120 planned. It is honestly graded and fully
permalinked, but **b2 (AI-outbound) and b4 (methodology) are partial sweeps**, and their gaps are
enumerated rather than papered over.

---

## 1. The headline: three surfaces now agree that forecast accuracy is never measured

This is the most important thing Channel B contributes, and it converges with C and D independently.

- **C (c2/c0):** GitLab's public handbook — forecasting is a documented NULL; the public heuristic
  "33% assumed win rate" is explicitly non-measured; "update the Close Date to ensure you're
  forecasting accurately" is an *instruction to be accurate*, not a measurement.
- **A (a2):** every incumbent pack, including Anthropic's official forecast skill, asserts unsourced
  numeric defaults — "3x coverage", "5-min = 21x".
- **B (this channel, `_raw-b3`):** **zero** practitioners state a stage-weighted probability AND say
  whether it was ever backtested. **Zero** report their own team's measured forecast accuracy. The
  hand-set stage weight is not defended on X, not attacked on X — it is simply never examined.

That triple null is the flagship's evidentiary spine. And Channel B found the incumbent number
circulating in the practitioner wild, which is what makes the wedge concrete rather than a complaint
about other people's packs:

> **"For years, 3-to-1 quota coverage was solid. 5-to-1 was world class."**
> — @gtmba_, 2026-04-06 · https://x.com/gtmba_/status/2041174257271480446 · **FOLKLORE**

Stated as received history, no source, no definition of what coverage is measured against. Pair it
with a2's finding and the pack can say: *this number has no origin on either surface.*

**The constructive half.** b3 shows the defect; b1 supplies the fix, and it is buildable by a solo
reader with no CRM and no statistics:

> **"*Write down* 'If we lose this deal, it will be because of X.' in advance. If you lose the
> deal/account/etc, ask why you lost it. Check against your prediction, and get better at
> predicting."**
> — @patio11, 2021-01-04 · https://x.com/patio11/status/1345906043197427713

A written-prediction-then-scored-outcome loop. It serves win/loss learning *and* forecasting honesty
at once, and it is the only calibration mechanism this channel found anywhere. **Recommended as a
candidate flagship primitive**, credited to patio11.

---

## 2. Strongest first-person exhibits (one line each, all permalinked)

1. **@gtmba_** — "73% quota attainment doesn't tell you anything without added context" · the pack's
   own interpretation thesis, stated independently by a practitioner · https://x.com/gtmba_/status/2044801893080174753
2. **@patio11** — write the predicted loss reason down in advance, then check it · the calibration
   primitive · https://x.com/patio11/status/1345906043197427713
3. **@KyleAsay_** — "We notice if your 'commit' deals frequently don't happen. We also notice if you
   magically exceed your forecast every quarter after sandbagging" · names BOTH forecast failure
   directions · https://x.com/KyleAsay_/status/1895872673625801151
4. **@arvidkahl** — "Founder-led sales is both fun and super scary… I find that very hard to balance!"
   · the solo builder's actual psychological problem · https://x.com/arvidkahl/status/1896219399369249126
5. **@thaAdamLittle** — "$SNOW … closing 25% bigger deals in 25% less time … and % team quota
   attainment hasn't budged from 57%" · three metrics moving independently ·
   https://x.com/thaAdamLittle/status/2037542426160648422
6. **@dvassallo** — "$18,340 of my sales came from turning on PPP pricing on Feb 1. Yes, maybe some
   of…" · a real dated attribution *with the author's own hedge attached* ·
   https://x.com/dvassallo/status/1641958262403899392
7. **@techsaleshackz** — "I threw MEDDIC, BANT, and frameworks out the window" · the methodology
   verdict from someone who improved by discarding them · https://x.com/techsaleshackz/status/2000955127813824846
8. **@salesxsaas** — "I've still yet to see a real world example where an AI SDR agent has booked a
   qualified call" · a falsifiable challenge that went unanswered · https://x.com/salesxsaas/status/2019037210805403922
9. **@BrianLaManna_** — best-and-final asked twice, then a new negotiator at a 9/30 close date · the
   forecast date is the lever used against the seller · https://x.com/BrianLaManna_/status/1972968791828000962
10. **@Shpigford** — "if you still require an enterprise sales call to give pricing, you're going to
    be eaten alive" · the existence gate moving from below · https://x.com/Shpigford/status/2066881769027047658

---

## 3. Two findings that should change what the pack writes

### (a) The subject of "quota attainment" is unstable — and a collision is already live

@thaAdamLittle's RepVue series is the best-sourced quota data on X (source named, sometimes with N).
Its subject is **share of reps hitting quota** — he says so himself: "only 18% of the team can hit
quota", "60% of Enterprise Sales reps … can hit their quota". Median across 20 large enterprise
software companies, Q4-25: **45%**, min 26.7%.

⚠️ **The charter records KBCM ~70→75% AE quota attainment as already primary-verified in success's
corpus.** These are almost certainly *different subjects* (share-of-reps-at-quota vs
percent-of-quota-attained), not a contradiction — but I have not read KBCM's text and will not assert
which. **The writer must verify KBCM's subject before the two numbers go anywhere near each other.**
This is the KBCM lesson recurring on a fresh pair of numbers; details in `_raw-b3` §2.

### (b) The "57% of the buying journey" claim does not circulate on X

Searched and came back null (b4 §5). The claim lives in vendor/analyst material — d1/d2's ground,
plus Channel E's note that webdesign carried a second instance of the genre ("9 in 10 buyers rule out
before contact"). **Implication:** it is a content-marketing artifact, not peer folklore, so the pack
should teach *recognition in published material* rather than framing it as a myth colleagues repeat.
⚠️ Caveat: one phrasing tried, no web cross-check possible during the outage — re-run before the pack
asserts practitioners don't repeat it.

---

## 4. The honesty line has a concrete boundary case

> "Take this cold email copy and create 25 variations. Same meaning, different structure. Vary:
> sentence order, word choice, punctuation, line breaks."
> — @seanlongden, 2026-08-02 · https://x.com/seanlongden/status/2083901909979521259

Explicitly to defeat "copy fingerprinting". Same meaning, 25 shapes — that is **detection evasion,
not personalisation**, and it ships as a ready-made Claude prompt. This is the cleanest available
articulation of where sales's *AI policy* differs from ai's *mechanics*: ai owns how to generate 25
variants; sales owns whether you should. **Recommend the pack cite this permalink as the boundary and
decline to teach the technique.**

Adjacent, and worth keeping consistent: @arvidkahl on whether a one-person company may present as
having "sales reps" (https://x.com/arvidkahl/status/1897011837893550461), and the positive pattern of
AI that "marks where it's unsure, for review" (https://x.com/arvidkahl/status/2082583176040374609).

---

## 5. Candidate never-ship figures (channel-wide)

| Figure | Where it came from | Subject as ACTUALLY stated | Permalink | Grade |
|---|---|---|---|---|
| **3-to-1 / 5-to-1 pipeline coverage** | b3 | quota coverage; base undefined, no source | https://x.com/gtmba_/status/2041174257271480446 | **FOLKLORE — primary target** |
| **70% of deals lost before stage 3** | b3 | **ONE named customer** in a vendor case study — the disproof is the next sentence | https://x.com/BrianLaManna_/status/2063965079821840670 | **CONFOUNDED — reads as a benchmark** |
| **1 closed deal per 20k–30k leads** | b2 | his own chained rates imply **15k–30k**; the low bound is wrong | https://x.com/levikmunneke/status/2083588733228745109 | **ARITHMETIC FAILS — use as teaching, never as benchmark** |
| **avg attainment at legacy SaaS is 40–45%/yr** | b3 | "avg attainment" undefined, no source, causal claim attached | https://x.com/Carles_Reina/status/2067608053294191046 | **FOLKLORE** |
| **AI-SDR market $5.8B, >20%/yr** | b2 | market size, no source, category undefined | https://x.com/salesxsaas/status/2080037249631076775 | **FOLKLORE** |
| **"The science says" $9.99 > $10** | b1 | no study named, magnitude undefined | https://x.com/dvassallo/status/1531338262333165569 | **FOLKLORE** |
| **$1M–$2M ARR per employee "easily"** | b3 | AI-native teams, no N, no source | https://x.com/gtmba_/status/2041174257271480446 | **FOLKLORE** |
| **"Most people book 2 calls/week, I book 10–15"** | b2 | unsourced baseline vs own claim, by the method's seller | https://x.com/DurgaprasadDP/status/2083252877146079604 | **CONFOUNDED** |
| **Legora $50M pipeline / $100M ARR / $275M by EOY-2026** | b3 | press/vendor; **$275M is a FORECAST stated as fact** | https://x.com/HarryStebbings/status/2053860005523103932 | **FOLKLORE** |
| **7yrs / 2x President's Club / $19m ARR sold** | b4 | offered as a methodology's evidence base; awards are not a test | https://x.com/FidelCacheFlow/status/2067366055102615697 | **FOLKLORE — genesis pattern** |
| **"59…" max quota attainment** | b3 | **truncated by projection — DO NOT QUOTE** | https://x.com/thaAdamLittle/status/2008940390385152153 | **UNVERIFIED** |

**Usable-with-subject (not never-ship):** the RepVue series (45% median / 26.7% min / 57% $SNOW /
19.5% Medallia / 18% / 60%–67% by segment) — all `share of reps at quota`, source named. And
@BrianLaManna_'s personal quota arithmetic ($1.6M ÷ $200K avg deal → 2 deals/quarter,
https://x.com/BrianLaManna_/status/1952722176013996041), where the arithmetic checks and IS the
teaching (R21 clause b).

---

## 6. Surprises worth flagging to the controller

1. **X is hostile to CRM-hygiene doctrine.** The only hygiene→outcome links found run *backwards*:
   the best seller a top AE knows has "terrible Salesforce hygiene"
   (https://x.com/BrianLaManna_/status/2062516506601148869), and an AE coach classifies "CRM hygiene
   before lunch" as PIP-level *noise* (https://x.com/mistamor/status/2070190497910469003). Nobody
   showed hygiene improving anything.
2. **The deliverability-collapse thesis is asserted but unevidenced on X.** This was the brief's
   top-priority capture and it did not materialise: no first-person domain burn, no before/after
   reply rate, no dates. Only assertion ("email as a channel is done",
   https://x.com/jeffreyhuber/status/2033577620793925656). The pack should temper any claim that the
   collapse has been *demonstrated*.
3. **Nobody on X is debating AI-disclosure in sales.** Zero results argued for or against telling a
   prospect an AI wrote the message. The pack would be staking genuinely open ground — which
   strengthens the wedge but means there is no practitioner consensus to cite.
4. **There is an active market shipping GTM *skills for Claude* specifically** — @AlfieJCarter's
   "125 skills across 6 layers" (https://x.com/AlfieJCarter/status/2054989729767051434), a
   "Claude for RevOps playbook" (https://x.com/AlfieJCarter/status/2052454306998039013), and a claim
   that a Claude subscription replaces the outbound stack
   (https://x.com/AlfieJCarter/status/2065482113768407079). **Routed to Channel A** — this is the
   same niche being contested on the social surface, and A ranked incumbents by repo only.
5. **No settled solo-founder CRM exists.** @arvidkahl asking in public "what is the current sales CRM
   that indie SaaS founders use?" (https://x.com/arvidkahl/status/1922424549120811049) plus C's
   finding that only Odoo models stage exit criteria (and ships it empty) — the pack's CRM-structure
   section has real room.
6. **@robwalling surfaced two founder-sales authorities we never swept:** @jjen_abel (Jen Abel) and
   @Kazanjy (Pete Kazanjy — d4 already established *Founding Sales* is all-rights-reserved).

---

## 7. COVERAGE STATEMENT — what was NOT searched

**Search surface backing every claim area in this channel: xrelay (X/Twitter).** No claim here is
backed by a web surface. The WebSearch quota died crew-wide mid-run; per the controller's ruling, no
null in this channel was produced via WebSearch, so none needs the WebFetch re-run — but equally,
**nothing here has been cross-checked against a second surface.**

**Queries actually run (19 total).** Open (`--product Top`): `weighted pipeline`, `pipeline coverage`,
`forecast accuracy`, `sales forecast`, `pipeline review`, `quota attainment`, `sales sandbagging`,
`pipeline coverage ratio`, `CRM hygiene`, `sales win rate`, `forecast category commit`, `AI SDR`
(since 2024-01-01), `cold email deliverability` (since 2024-01-01), `MEDDIC`, `discovery call sales`,
`buying journey before contacting`. Author-targeted (typed `--from`, single term):
`thaAdamLittle`+quota, `KyleAsay_`+forecast, `gtmba_`+quota, `BrianLaManna_`+pipeline,
`patio11`+sales, `arvidkahl`+sales, `robwalling`+sales, `tylertringas`+pricing, `dvassallo`+pricing.

**Authors NOT searched:** `levelsio`, `jasonlk` (Jason Lemkin — the largest single omission on the
founder-led axis; d4 covers his doctrine from the web, so the gap is X-side corroboration only),
`jjen_abel`, `Kazanjy`, `Steli`, `techsaleshackz`, `TechSalesGuy`, `Carles_Reina`, `sammarelich`,
`saleskhalifa`, `mistamor`, `thedealdirector`, `randomrecruiter`, `BowTiedSalesGuy`, `axtalks`,
`levikmunneke`, `AlfieJCarter`. **No handle was vetted with `xrelay user`** — no author in this
corpus should be treated as authoritative on reputation alone.

**Terms NOT searched:** `MEDDPICC`, `Challenger`, `SPIN selling`, `BANT`, `Sandler`, `Gap Selling`,
`SPICED`, `sales methodology`, `buying committee`, `champion`, `procurement`, `security review`,
`objection handling`, `no decision`, `compelling event`, `mutual action plan`, `happy ears`,
`deal slipped`, `close date`, `deal desk`, `exit criteria`, `stage weighted`, `3x pipeline`,
`pipeline is a lie`, `commit`, `best case`, `Clari`, `forecast call`, `RevOps`, `11x`, `Artisan`,
`Instantly`, `Apollo`, `Clay`, `AI BDR`, `email warmup`, `domain burned`, `spam folder`,
`personalization at scale`, `sequences`, `outbound is dead`, `reply rate`, `meetings booked`,
`SDR replaced`.

**Methods NOT used:** **zero `xrelay thread` calls** — no thread was read, so every quote is bounded
by the 400-char projection. **Any quote ending in "…" must be re-fetched before it ships**; this
affects the dvassallo PPP hedge, KyleAsay_'s three no-forecast criteria (only the first is visible),
and the thaAdamLittle Q4-25 max value (marked UNVERIFIED). No `--product Latest` pass anywhere — the
whole corpus is `Top`-ranked, biasing toward high-engagement and older posts, which is a real
weakness for the AI-outbound axis. Bookmarks and `my-posts` local caches were never consulted.

**Highest-value top-up if the controller wants one** (in priority order): (1) `domain burned`,
`email warmup`, `reply rate` — the likeliest home of the missing first-person deliverability
evidence; (2) `--from jasonlk` for X-side founder-led corroboration; (3) thread-reads on the four
truncated quotes above; (4) the untouched methodology terms for b4.

---
---

# ADDENDUM — 2026-08-03, commissioned top-up (12 queries of an ~18 cap)

Run by the lead, serialized, `timeout 90`, ≥4s gaps. Surface: xrelay only.
**Two of this channel's own NULLS were FALSIFIED by this pass. Both corrections are below, and both
raws have been amended in place so nobody reads a stale null.** Verdicts elsewhere unchanged.

## A. CORRECTION 1 — the deliverability null was WRONG (b2 NULL #1)

b2 reported "no first-person deliverability war story with numbers." **False.** Found on the first
top-up query:

**@harsh_biz** · 2026-07-09 · https://x.com/harsh_biz/status/2075218419927122424 · **FIRST-PERSON RESULT**
> "We went from 0.1% to 1% reply rate in 3 days. **(No auto-replies counted)** No new copy. No new
> offer. We randomly fell to 0.1% one day, and here's how we fixed it to hit 1%+."

This is the exhibit b2 said did not exist, and it is better than expected: a **10× reply-rate swing
with copy and offer explicitly held constant** — isolating deliverability as the cause — and it
carries its own denominator caveat ("no auto-replies counted"), which is precisely the discipline the
pack wants to model. **Reply rates are a deliverability artifact before they are a copy artifact.**

## B. CORRECTION 2 — "no practitioner defends a named methodology" was WRONG (b4 NULL #1)

b4 reported that no author argued *for* any named framework, with a caveat against over-reading it.
The caveat was right and the null is now falsified twice over:

**@Chris_Orlob** · 2026-05-14 · https://x.com/Chris_Orlob/status/2054924787202314444 · **OPINION — a real defence**
> "I read The Challenger Sale seven times in my early 20s. The insight that stuck: your job isn't to
> understand the buyer's existing frame for their problem. It's to teach them to think about it in a
> way they couldn't before you showed up."

**@BowTiedSalesGuy** · 2021-11-12 · https://x.com/BowTiedSalesGuy/status/1459230799283339272 · **CONTESTED — with himself**
> "I agree with many sensible sales methodologies: 1) Sandler 2) GAP selling 3) SPIN selling. But
> that's missing the big picture. Sales isn't just consultative… Sales is also pitching. Creating
> Wanting. Combine both = Chad Salesman"

Note this is the **same author** who in 2022 posted "BANT MAN FAB MEDDIC / NGMI"
(https://x.com/BowTiedSalesGuy/status/1542578172188819456). One practitioner, opposite positions,
14 months apart. The honest finding is therefore **not** "practitioners reject the frameworks" but
**"practitioner opinion is genuinely split, and individuals move within it."** The pack must not
claim a practitioner consensus in either direction.

## C. NEW — a taxonomy correction the pack should carry

**@Chris_Orlob** · 2025-09-28 · https://x.com/Chris_Orlob/status/1972230446781227215 · **OPINION — category correction**
> "PSA for Sales Leaders: MEDDPICC is not a sales methodology. MEDDPICC is a deal qualification and
> deal health framework. If you tell your reps 'follow the steps in MEDDPICC' without giving them the
> skills to do it? You're destined for some disappointing pipeline reviews."

Load-bearing because the whole corpus — including d1 — files these artifacts under "methodologies".
If a qualification *checklist* is mistaken for a selling *method*, the pack inherits a category error
and will teach the wrong thing. Recommend the pack distinguish **qualification/deal-health frameworks**
(MEDDIC/MEDDPICC/BANT) from **selling methods** (SPIN/Challenger/Sandler) and say why it matters.

Vendor counter-position, for contrast — **@meddpicc** · https://x.com/meddpicc/status/1965397852869275721 · **CONFOUNDED**
> "You can't forecast when you're not aligned. Partner-sourced pipeline without MEDDPICC can be
> unpredictable. ❌ No Champion = no internal voice… ❌ No process = no predictability"

A framework vendor asserting a **forecast-accuracy benefit with zero evidence** — the flagship's
target genre, now with a permalink.

## D. The honesty line is a PATTERN, not one case — three evasion exhibits

b2 offered one detection-evasion exhibit. There are now **three, independent, from different actors**:

1. **Copy-spinning** — @seanlongden · https://x.com/seanlongden/status/2083901909979521259 — "25
   variations. Same meaning" explicitly to defeat copy fingerprinting.
2. **Simulated human engagement** — @NickAbraham12 · https://x.com/NickAbraham12/status/1416026033422315523
   > "What email warmup SaaS can - scroll on your emails to mimic human behavior - star your emails -
   > click the links in your email to mark them as safe. Perfect email deliverability ✅"
3. **Account farming with proxies** — @webjuice_ie · https://x.com/webjuice_ie/status/1801280371771715820
   > "I just installed G Accounts Email Warmup tool and connected my 30 G Accounts… it can farm each G
   > account and use proxies so it keeps real. Sticky reviews and manipulation are coming soon"

All three manufacture false signals of human behaviour to defeat a receiving system's filters. And it
is a funded industry: a warmup tool "generates 1.2 million a year"
(https://x.com/staticmaker1/status/2046044489593348568). **Upgrade the recommendation:** the pack
should draw its line against the *category* — manufacturing false engagement signals to defeat
filtering — not against one prompt. That is a rule a reader can apply to tools that don't exist yet.

## E. "Email is cooked" is now CONTESTED, not settled

b2 recorded the collapse thesis as asserted-but-unevidenced. Two practitioners now attribute failure
to **configuration and offer**, not channel death:

**@NickAbraham12** · https://x.com/NickAbraham12/status/2083915025115201597 · OPINION
> "'All of my cold emails are going to spam' — My brother in Christ, your inboxes have been
> disconnected and warmups have been disabled for two weeks. How can you possibly complain?"

**@seanlongden** · https://x.com/seanlongden/status/2083627610546864595 · OPINION
> "Prospects: 'We tried cold email before, it didn't work' Me: 'What was your offer?' … 'Cold traffic
> will not get on calls for cost or time saving offers, that's why'"

Against @jeffreyhuber's "email as a channel is done"
(https://x.com/jeffreyhuber/status/2033577620793925656). Both poles permalinked → **grade the
collapse thesis CONTESTED**, and note that the sceptics offer a *diagnosis* while the collapse side
offers an assertion.

## F. All four truncated quotes re-fetched — every one materially better

1. **thaAdamLittle Q4-25 — UNVERIFIED value now VERIFIED.** Max = **59.7%** (median 45%, min 26.7%).
   Bonus: the full post also gives Sales Output Growth (median 7.8%, min −0.3%, max 15.7%) and — more
   valuable — **defines its own metric and says which one to prefer**: Sales Output "accounts for
   capacity (number of ramped quota-carrying reps) combined with their relative performance (measured
   by quota attainment) on a YoY basis," and he labels his own rule of thumb "Rough heuristic."
   **This is the corpus's best example of metric hygiene** — name it, define it, rank it, flag the
   heuristic as rough. Cite it as the positive model against the "3x coverage" folklore.
2. **dvassallo PPP — the full hedge, and a bonus arithmetic lesson.** Complete: "Yes, maybe some of
   these sales would have happened anyway at full price, but I'm sure this helped increase revenue."
   Every bucket carries its own counterfactual. Full breakdown of ~$100K: PPP $18,340 · PayPal
   $18,850 · affiliates $5,370 · Discover $999 · Google $14,727 · existing Gumroad accounts $71,889
   (71%+). ⚠️ **These sum to $130,175 — 30% MORE than the $100K total — because the categories
   overlap (channel vs payment method vs account status).** That is a teaching exhibit in itself:
   attribution buckets that cannot be summed, from an author who never claims they can.
3. **KyleAsay_ — all three criteria now visible** (b3 had only the first):
   > "1) **No velocity** … 2) **No concerns** — Buying carries risk. If your prospect isn't asking you
   > to help address concerns, they aren't really considering buying. No concerns often means no
   > consideration. 3) **No 'next best option'** — Execs rarely put all eggs in one basket… No
   > alternative options to your product most likely means they haven't committed to solve the
   > problem you address."
   Now fully quotable. These are **negative** exit criteria — reasons to *refuse* the forecast — which
   is exactly the inversion the flagship needs against hand-set stage probabilities.
4. **arvidkahl — the existence-gate argument has a falsifiable boundary condition.** Full text adds:
   > "The relationship-building of sales, the custom solution work required to land and retain a
   > larger business: all of that is much less tech than it depends on interpersonal dynamics. **And
   > as long as humans make tech choices instead of AI systems**, these companies will possess a moat
   > that prevents them from being cloned by a well-written prompt."
   The conditional is the valuable part: it states what would have to change for the argument to
   fail. Much stronger than the truncated version.

## G. Figures added to the never-ship list

| Figure | As stated | Subject as actually stated | Permalink | Grade |
|---|---|---|---|---|
| "70% of salespeople struggle to meet quotas" | rhetorical opener | **third distinct subject** for a "70%" quota figure in this corpus; no source | https://x.com/iuditg/status/1691365238598492161 | **FOLKLORE** |
| "proven to increase conversion by 48…" | Solution Selling claim | "proven" with no study; value truncated in source | https://x.com/iuditg/status/1691365238598492161 | **FOLKLORE** |
| "benchmarked against data from 244,000+ outbound campaigns" | promotional prompt pack | no method, no access, selling the artifact | https://x.com/jack_9947/status/2062217948853416237 | **CONFOUNDED** |
| "$6M ARR" agency | own agency milestone | self-reported, unauditable | https://x.com/NickAbraham12/status/2069119532308775087 | FIRST-PERSON (unverifiable) |
| "email warmup cost $90/month PER inbox" 10 yrs ago | historical price claim | secondhand, retold about a third party | https://x.com/NickAbraham12/status/2042351983252640025 | FOLKLORE |
| **59.7%** | Q4-25 max quota attainment | share of reps at quota, 20 large enterprise SW cos, RepVue | https://x.com/thaAdamLittle/status/2008940390385152153 | **NOW VERIFIED — usable with subject** |

⚠️ **"70%" now has THREE different subjects in this corpus** — deals lost before stage 3 (one
vendor's customer), salespeople struggling to meet quota (folklore), and dvassallo's 71% of sales
from existing accounts. Any bare "70%" in a sales context should be treated as unidentified until its
subject is read.

## H. Also routed to Channel A (incumbent census)

Two more Claude-sales-prompt products: a "244-Prompt B2B Sales Library"
(https://x.com/AlfieJCarter/status/2062218335417192777, https://x.com/jack_9947/status/2062217948853416237)
and a "375 Prompt Book for Fundraising" (https://x.com/rdominguezibar/status/2083606674162561055).
Consistent with A's fragmentation finding — the niche is being contested with prompt packs that cite
nothing.

## I. Addendum coverage

**Queries run (12):** `domain burned cold email` · `email warmup` · `cold email reply rate` ·
`spam rate cold email` · `MEDDPICC` · `Challenger Sale` · `SPIN selling` · `Sandler sales` (all
`--product Top`), plus **4 `xrelay thread` root re-fetches** (ids 2008940390385152153,
1641958262403899392, 1909618149621653983, 1933686087462830355). Six queries of the ~18 cap unused.

**Still NOT searched:** `--from jasonlk` (skipped per controller), BANT (skipped — D confirmed no
primary exists), `Gap Selling`, `SPICED`, `buying committee`, `champion`, `procurement`,
`mutual action plan`, `no decision`, `11x`, `Artisan`, `Instantly`, `Clay`. **`SPIN selling` and
`Sandler sales` both returned near-total noise** (finance/gaming/Piper Sandler collisions) — their
thin coverage here reflects a term-collision problem on X, not an absence of discourse. No
`--product Latest` pass anywhere in this channel, still.

**Net effect on the channel's verdicts:** the flagship convergence, the patio11 primitive, and the
"3-to-1 coverage" folklore finding are all UNCHANGED and now better supported. Two nulls corrected,
one thesis downgraded from unevidenced to CONTESTED, one taxonomy error caught, four exhibits
upgraded to fully-quotable.
