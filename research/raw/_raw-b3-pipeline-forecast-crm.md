# Raw B3 — Pipeline / Forecast / CRM folklore on X

Channel B (X practitioner corpus). Surface: **xrelay only** (X/Twitter). No web surface used in
this file — every permalink below is the `url` field returned by `xrelay search`, never reconstructed.
Collected by the Channel B lead directly (workers were stopped after the concurrency incident;
lead ran every query serially with `timeout 90`, 4s gaps).

Grades: **FIRST-PERSON RESULT** (author's own reported outcome) · **OPINION** (assertion, no result)
· **FOLKLORE** (circulating figure, no traceable source in the tweet) · **CONTESTED** (visible
disagreement) · **CONFOUNDED** (causal claim with obvious alternative explanations).

---

## 1. THE FLAGSHIP EXHIBIT — "3-to-1 coverage" caught in the wild, unsourced

**@gtmba_** · 2026-04-06 · https://x.com/gtmba_/status/2041174257271480446 · **FOLKLORE**
> "For years, 3-to-1 quota coverage was solid. 5-to-1 was world class. Now? The best AI-native teams
> are lapping that. And then lapping it…again. They're hitting $1M–$2M ARR per employee, easily."

Why it matters: this is the single most valuable capture in the file. Channel A (a2) found that
EVERY incumbent sales pack — including Anthropic's own official forecast skill — asserts "3x
coverage" as an unsourced numeric default. Here is the same number circulating in the practitioner
wild with **no source, no denominator, and no definition of what "coverage" is measured against**.
It is stated as received history ("for years… was solid"). Pairs with the incumbent evidence to make
the wedge concrete: the number is folklore on BOTH the pack surface and the practitioner surface.
Note the second figure in the same breath ("$1M–$2M ARR per employee, easily") is equally unsourced.

**R21 test:** passes (a) — the reader must recognise-and-correct this exact number — and both the
incumbent side (a2) and the practitioner side (this permalink) are now documented.

---

## 2. Quota-attainment figures — the SUBJECT problem, with a live worked example

The richest vein on X is **@thaAdamLittle**, who posts RepVue-derived quota series. His numbers are
unusually good because he NAMES the source (RepVue) and sometimes the N. **But the subject of
"quota attainment" in his series is `% of the team hitting quota`, NOT `% of quota attained`** —
and he says so himself in plain language, which is what lets us verify it rather than guess.

**Subject proof, in his own words:**

**@thaAdamLittle** · 2026-05-15 · https://x.com/thaAdamLittle/status/2055313253132063035 · OPINION (figure: FOLKLORE-adjacent, source named but unlinked)
> "NOTHING IS WORKING! HOW DO WE GROW REVENUE?!?! *crickets* ....hire more sales reps? but only 18%
> of the team can hit quota? screw it, hire more reps. (yellow line) this won't end well."

**@thaAdamLittle** · 2026-01-17 · https://x.com/thaAdamLittle/status/2012537714613141577 · OPINION
> "$TEAM can be vibe coded in a weekend yet 60% of Enterprise Sales reps and 67% of SMB/MM Sales
> reps can hit their quota"

Both read "% of REPS who CAN HIT quota". That fixes the subject for the whole series.

**The series itself:**

**@thaAdamLittle** · 2026-01-07 · https://x.com/thaAdamLittle/status/2008940390385152153 · FIGURE, source named (RepVue), N=20 companies
> "Q4-25 Quota Attainment and Sales Output YoY Growth across 20 large enterprise software names
> (e.g., Salesforce, HubSpot, CrowdStrike, ServiceNow, etc.; all 20 tagged in comment below).
> Q4 Median Quota Attainment: 45%  Q4 Min Quota Attainment: 26.7%  Q4 Max Quota Attainment: 59…"

✅ **RESOLVED 2026-08-03 by thread re-fetch — max = 59.7%** (median 45%, min 26.7%). Subject = share
of reps at quota. The full post additionally reports Sales Output Growth (median 7.8%, min −0.3%,
max 15.7%) and — more valuable than any of the figures — **defines its own metric and ranks it**:

> "Sales Output is the more relevant metric. It accounts for capacity (number of ramped
> quota-carrying reps) combined with their relative performance (measured by quota attainment) on a
> YoY basis." … "**Rough heuristic:** If a company grew top-line revenue at 10%…"

**This is the corpus's best example of metric hygiene** — name the metric, define what it comprises,
say which one to prefer and why, and label your own rule of thumb "rough". Cite it as the positive
model standing directly against the "3-to-1 coverage" folklore in §1.

**@thaAdamLittle** · 2026-03-27 · https://x.com/thaAdamLittle/status/2037542426160648422 · FIGURE, single company
> "$SNOW Enterprise sellers are closing 25% bigger deals in 25% less time — while adding more reps —
> and % team quota attainment hasn't budged from 57%. ACV: $476K (H1'25) → $511K (H2'25) → $597K
> (YTD'26) Cycle: 250 → 226 → 187 days"

Note the explicit metric name "% team quota attainment" — subject confirmed again. This is also a
good honesty exhibit in its own right: deal size up, cycle down, attainment flat — three metrics
moving independently, which is exactly the "a single number doesn't tell you what happened" teaching.

**@thaAdamLittle** · 2026-04-22 · https://x.com/thaAdamLittle/status/2047040250212495660 · FIGURE, single company
> "The Medallia reviews on RepVue are pretty telling of a sinking ship story - slowing taking on
> water... % of team quota attainment here 19.5% is ummm no bueno"

**@thaAdamLittle** · 2026-06-23 · https://x.com/thaAdamLittle/status/2069447318743474454 · FIGURE with N
> "$NAVN GTM signals on RepVue look to be ripping … % Team Quota Attainment has doubled since Q4-24
> 90% confident on company future outlook (N12M) N=736"

**@thaAdamLittle** · 2026-04-09 · https://x.com/thaAdamLittle/status/2042338414226215009 · FOLKLORE (no figure, directional claim)
> "Blood in the water! yet Q1-26 Quota Attainment among 275+ public and private Software companies
> rose to its highest level since Q4-2022... 🤔"

**@thaAdamLittle** · 2026-07-10 · https://x.com/thaAdamLittle/status/2075580202269512043 · FIGURE, defines its own metric
> "SaaS rebate management platform 'Enable' … has seen their Sales Output (a RepVue metric of quota
> weighted sales capacity performance) decline 42.4% since then...quota attainment since that raise …"

Valuable because he DEFINES the metric inline ("a RepVue metric of quota weighted sales capacity
performance") — the opposite of the folklore pattern. Cite as a positive example of metric hygiene.

### ⚠️ COLLISION FLAGGED FOR THE WRITER — do NOT resolve from this file

The charter records **KBCM ~70→75% AE quota attainment as already primary-verified** in success's
corpus. RepVue's series here reports **median 45%** (share of reps at quota, N=20 large enterprise
software cos, Q4-25) and per-company values from **19.5% to 67%**. These are almost certainly
**different subjects** (share-of-reps-at-quota vs. percent-of-quota-attained), not a contradiction —
but I have not read KBCM's text and will not assert which. **The writer must verify KBCM's subject
before placing the two numbers anywhere near each other.** This is the KBCM lesson repeating on a
new pair of numbers.

### Other quota figures, all with named-but-unlinked sources

**@Carles_Reina** (ElevenLabs) · 2026-06-18 · https://x.com/Carles_Reina/status/2067608053294191046 · **FOLKLORE**
> "Understanding if a market is being actively expanded is easily seen in Sales quota attainment per
> quarter. The usual motion is to see quota attainment go down as the team size increases - this is
> the reason why avg attainment at legacy SaaS is 40-45% per year."

No source; "avg attainment" subject ambiguous (average of what, over whom); causal claim
("this is the reason why") is unsupported. Never-ship candidate.

**@techsaleshackz** · 2025-01-31 · https://x.com/techsaleshackz/status/1885355614248861884 · FIGURE (RepVue-derived)
> "ServiceNow PAYS their SDRs: Base Pay: $65k OTE: $90k Top Performers: $150k … SDR Attainment: 80%
> (extremely impressive)"

**@techsaleshackz** · 2025-07-07 · https://x.com/techsaleshackz/status/1942258559657607656 · FIGURE
> "Just saw an 18 year old accept an SDR role at Common Room on Linkedin  87 on repvue  75k Base,
> 95k OTE, 116k top performer  50% quota attainment"

Both are SDR-subject, not AE-subject — another live instance of the role-conflation hazard.

---

## 3. Interpretation over measurement — the honesty line, stated by practitioners

**@gtmba_** · 2026-04-16 · https://x.com/gtmba_/status/2044801893080174753 · **OPINION — flagship-grade**
> "73% quota attainment doesn't tell you anything without added context. If everyone in the org hit
> quota, the rep at 103% might really be your worst hire. What about the rep selling a second-rate
> product in a broken market at 60% quota? Put a real product in their hands, and t…"

Why it matters: a practitioner independently articulating the pack's own thesis — the number is not
the finding; the interpretation is. Direct heir of the family's measurement-honesty line. Strongest
non-figure exhibit in this file.

**@thaAdamLittle** · 2026-06-05 · https://x.com/thaAdamLittle/status/2062882754077823052 · **OPINION — structurally striking**
> "Sales Leaders can actually lower quotas.... the question is why would they? remember the cost of
> an empty seat is the real cost - the model never planned on you hitting quota in the first place.
> sometimes kicking the attrition can down the road makes economic sense, at least…"

Why it matters: claims quota is a **capacity-planning artifact, not a prediction** — i.e. the plan
never assumed attainment. If defensible, this reframes every attainment benchmark in the corpus.
Grade OPINION (he asserts, does not show), but it is the sharpest single idea found on X here.

**@thaAdamLittle** · 2026-06-16 · https://x.com/thaAdamLittle/status/2066876587270631732 · OPINION
> "Been talking about Quota Attainment for a long time now - but only recently have we started
> getting visibility into the Sales Targets themselves and insight into if they're increasing,
> decreasing, or staying the same. Most orgs will raise quotas rolling into a new fiscal, but yo…"

The denominator moves. An attainment percentage is uninterpretable without knowing whether the quota
itself was raised — a concrete, teachable mechanism for why cross-year attainment comparisons lie.

**@gtmba_** · 2026-07-06 · https://x.com/gtmba_/status/2074154033946743140 · OPINION
> "If you have to get quota-setting wrong, get it wrong on the low side. It sounds counterintuitive,
> but set them too high and the damage compounds fast. Reps miss the number, morale craters, your A
> players start leaving, and the ones already gone start back-channeling to pull ou…"

**@gtmba_** · 2026-07-30 · https://x.com/gtmba_/status/2082856376284422236 · OPINION
> "Imagine this: you hit 130% of your quota this quarter on autopilot. Feels like a win. So why isn't
> it? … 'I put my feet on the floor, and I could coast the whole day and still land at 115-130%.'"

Over-attainment as a signal of a mis-set quota, not of performance. Same teaching from the other side.

---

## 4. Forecast honesty — sandbagging, commit, and refusing to forecast

**@KyleAsay_** · 2025-03-01 · https://x.com/KyleAsay_/status/1895872673625801151 · **OPINION — prime forecast-honesty exhibit**
> "Confession: sales leaders absolutely have 'favorite' AEs. Here are three ways to make the list:
> 1) Forecast accurately — We notice if your 'commit' deals frequently don't happen. We also notice
> if you magically exceed your forecast every quarter after sandbagging deals."

Names BOTH failure directions in one breath: commit-inflation and sandbagging. The pack's forecast
section needs exactly this symmetry — a forecast that is always beaten is as broken as one that misses.

**@KyleAsay_** · 2025-07-25 · https://x.com/KyleAsay_/status/1948807437558903051 · OPINION
(also posted 2024-12-13 https://x.com/KyleAsay_/status/1999952250232520772 and 2026-04-07
https://x.com/KyleAsay_/status/2041533564265607321 — a recycled evergreen, note the repetition)
> "At this point in my career, I've seen deals lost for just about every reason you could possibly
> imagine. So I can recognize 'trouble' immediately. Now, I refuse to forecast a deal if any of
> these 3 things are true:"

**@KyleAsay_** · 2025-04-08 · https://x.com/KyleAsay_/status/1909618149621653983 · OPINION — the criteria, visible
> "I've seen enough deals 'slip' to recognize trouble. I refuse to forecast a deal if any one of
> these 3 things are true: 1) No velocity — When a prospect delays next steps for weeks (or longer)
> they aren't spending that time justifying your product - they are spending that time wor…"

✅ **ALL THREE CRITERIA RE-FETCHED IN FULL 2026-08-03** (thread read) — now fully quotable:

> "**1) No velocity** — When a prospect delays next steps for weeks (or longer) they aren't spending
> that time justifying your product - they are spending that time working on more important issues.
> And if your product doesn't address their most important problems, it's not getting purchased.
> **2) No concerns** — Buying carries risk. If your prospect isn't asking you to help address
> concerns, they aren't really considering buying. No concerns often means no consideration.
> **3) No 'next best option'** — Execs rarely put all eggs in one basket… No alternative options to
> your product most likely means they haven't committed to solve the problem you address."

Why it matters: a practitioner's **personal exit criteria for entering the forecast** — self-authored,
falsifiable, and the opposite of a hand-set stage percentage. Note they are **negative** criteria:
reasons to REFUSE to forecast, not probabilities to assign. That inversion is the model for what the
pack should teach instead of weighted-stage arithmetic, and "no concerns often means no
consideration" is the sharpest line in it.

**@KyleAsay_** · 2024-12-30 · https://x.com/KyleAsay_/status/1873813904662434122 · OPINION (satirical form)
> "I'm shook. My two year old just said, 'Dad why do AEs keep fake deals in their pipeline to
> exaggerate the health of their business when it only delays the inevitable and actually makes
> leadership even more upset when everything falls out all at once? Especially because most lead…"

**@KyleAsay_** · 2025-01-13 · https://x.com/KyleAsay_/status/1878849957962170847 · **CONTESTED / satire — forecast coercion**
> "Why this is perfect sales leadership: 1) Tell them they can't drop their forecast — Really is that
> simple. You are the boss, and they have to listen. 2) Removing pressure and coaching mindset —
> Legally speaking, if you say 'no pressure' you can't really get sued for toxic lead…"

Read as satire of a real practice: forecasts revised by authority rather than evidence. The pack's
"what can a forecast honestly predict" section should name this failure mode explicitly.

**@KyleAsay_** · 2026-07-01 · https://x.com/KyleAsay_/status/2072316503626522910 · FIRST-PERSON RESULT (qualitative)
> "Obviously, this destroyed the rep and team's forecast and heavily damaged the company's call - we
> weren't that big yet, and this deal was a big chunk of our expected revenue."

Concentration risk in a forecast — one deal carrying the quarter. Ties to the solo/small-company
default reader: at low deal counts a forecast is not a distribution, it is a bet.

**@KyleAsay_** · 2025-03-03 · https://x.com/KyleAsay_/status/1896623899359515044 · FIRST-PERSON RESULT (narrative)
> "…a teammate had a large deal scheduled to close on the final day. All signs showed a clear path to
> closing - legal was done, budgets had been approved, and all parties were aligned on the close
> date. Then, the champion asked f…"

Every conventional exit criterion satisfied, deal still moved. The best available argument against
treating stage exit criteria as probability.

---

## 5. Pipeline hygiene, reviews, and disqualification

**@BrianLaManna_** (AE at Gong) · 2025-07-10 · https://x.com/BrianLaManna_/status/1943306371509711161 · OPINION
> "If you're a sales leader and you still run pipeline reviews out of a CRM opportunity view in 2025,
> you're reaching dinosaur status. Bold statement sure. But if the large CRM players don't even use
> it, why would you? You probably ask these questions in pipeline reviews to reps:"

Note the vendor position — he sells for a conversation-intelligence vendor whose product replaces the
CRM view. Grade the *claim* CONFOUNDED by interest, even though the critique may be sound.

**@BrianLaManna_** · 2026-05-17 · https://x.com/BrianLaManna_/status/2056031787588166039 · FIRST-PERSON RESULT (practice)
> "The best thing I ever did for my pipeline was add an 'Unfortunately Nope' category. Not every
> account deserves your energy. The hardest skill in enterprise sales isn't opening deals. It's
> having the discipline to deprioritize the ones that aren't going anywhere so you can go a…"

Disqualification as a first-class pipeline state — a concrete, adoptable CRM structure the pack can
teach (and cheap for a solo builder).

**@BrianLaManna_** · 2026-03-29 · https://x.com/BrianLaManna_/status/2038250214230814796 · OPINION
> "You're also not you, when you're desperate for a deal. … When I have a surplus of pipeline:
> -Disqualifying properly -Keeping stronger price integrity -Holding the line on our buyer process"

Pipeline volume as an input to **discounting discipline** — links pipeline management to pricing
presentation, a seam the pack owns.

**@BrianLaManna_** · 2026-06-04 · https://x.com/BrianLaManna_/status/2062516506601148869 · OPINION (aside)
> "John Bristow is one of the best sellers I've ever met. $200M+ closed in revenue. … (Except his
> terrible Salesforce hygiene)"

Worth citing precisely because it is throwaway: the best-performing seller he knows has bad CRM
hygiene. Direct counter-evidence to the "CRM hygiene drives results" folklore. **No one in this
sweep showed CRM hygiene improving an outcome.**

**@mistamor** · 2026-06-25 · https://x.com/mistamor/status/2070190497910469003 · OPINION
> "I coach AEs who were put on PIPs. … Noise: Day planning at 9am. Admin during prime hours.
> Optional meetings. CRM hygiene before lunch. Signal: Outbound block 9am-12pm, untouc…"

CRM hygiene classified as **noise** by an AE coach. Pairs with the Bristow line above: the
practitioner surface is actively hostile to the hygiene doctrine, while CRM vendors assert it.

**@BrianLaManna_** · 2026-06-08 · https://x.com/BrianLaManna_/status/2063965079821840670 · **CONFOUNDED — subject verified, and it is NOT a benchmark**
> "70% of deals lost before stage 3. One prospect was bleeding early-stage pipeline. CRM data was
> trash. Reps all blamed different things. Nothing was backed by actual evidence. Here's how Gong's
> AI Theme Spotter fixed it in a single analysis."

⚠️ Subject check performed: "70% of deals lost before stage 3" is **one named customer's** number in
a vendor case study, not an industry figure — the very next sentence says "One prospect." Quoted out
of context it reads exactly like a benchmark. **Prime never-ship candidate**, and a perfect worked
example of the charter's subject-verification rule: the disproof is one sentence away from the figure.

---

## 6. Quota arithmetic — where the numbers ARE the teaching (R21 clause b)

**@BrianLaManna_** · 2025-08-05 · https://x.com/BrianLaManna_/status/1952722176013996041 · **FIRST-PERSON RESULT**
> "I completely black out my quota. The number I care about: How much $$$ do I need to close, to earn
> President's Club? For me this year: It's $1.6M. So I work backwards. The average deal is $200K. To
> stay on pace, I need to close 2 deals per quarter, totaling $400K. To cl…"

Arithmetic checks: $400K/quarter × 4 = $1.6M; $400K ÷ $200K = 2 deals. Internally consistent, and it
is HIS OWN number for HIS OWN year — the cleanest first-person quota exhibit found. R21 clause (b):
the arithmetic is the teaching (target ÷ average deal size → required deal count → required activity).
Adoptable directly by a solo builder with a revenue goal instead of a quota.

**@BrianLaManna_** · 2026-05-15 · https://x.com/BrianLaManna_/status/2055273176813154583 · FIRST-PERSON RESULT
> "$3M in pipeline built this year - a little secret about my entire outbound strategy."

**@BrianLaManna_** · 2025-05-01 · https://x.com/BrianLaManna_/status/1917929213169950720 · FIRST-PERSON RESULT
> "I've sourced over $10M in new pipeline since joining Gong."

Both self-reported, unauditable, and — note — **pipeline sourced, not revenue closed**. A pipeline
figure is a claim about the numerator of a ratio nobody publishes. Grade accordingly if used.

**@saleskhalifa** · 2026-03-13 · https://x.com/saleskhalifa/status/2032561814203150794 · FIRST-PERSON RESULT
> "I've hit quota 14 Q's in a row, because I learned to work very hard at the beginning of the
> quarter. Not fuck around and turn it on towards the end"

**@sammarelich** · 2025-06-16 · https://x.com/sammarelich/status/1934641969239613494 · OPINION
> "You NEED a spreadsheet set up with • Your quota attainment • Big logos closed • Other 'brag worth'
> facts … Do it WHILE you have CRM access"

Attainment as a personal record kept OUTSIDE the CRM because CRM access is revocable — an
under-discussed reason the system of record and the seller's record diverge.

---

## 7. Adjacent captures worth routing elsewhere

**@thedealdirector** · 2026-07-02 · https://x.com/thedealdirector/status/2072682174952751359 · CONTESTED
> "Higher quota attainment at Legora vs Vanta confirmed."

**@HarryStebbings** · 2026-05-11 · https://x.com/HarryStebbings/status/2053860005523103932 · **FOLKLORE — vendor/press figures**
> "Jude Law generated $50M in sales pipeline. Legora is onboarding 50 people every 14 days. 3.6 per
> day! $100M in ARR in 18 months. $275M by EOY 2026."

Four unsourced figures in one post, one of which ("$275M by EOY 2026") is a **forecast stated as
fact** — a compact illustration of the genre the pack is trying to inoculate against.

**@thaAdamLittle** · 2026-07-24 · https://x.com/thaAdamLittle/status/2080712645032673401 · OPINION
> "I can't even wrap my head around 30 quota carrying reps sharing 1 Key Account. Is this common in
> the big of the big enterprise? $IBM"

**@AlfieJCarter** · 2026-06-12 · https://x.com/AlfieJCarter/status/2065482113768407079 · **ROUTE TO CHANNEL A (incumbent census)**
> "Fable 5 just changed outbound. All you need is: - A laptop - A Claude Max subscription - 10 minutes
> to install once. That's enough to run a complete outbound stack covering prospect, research,
> sequence, CRM, enrichment, deliverability, and pipeline review. No expensive sales t…"

**@AlfieJCarter** · 2026-06-30 · https://x.com/AlfieJCarter/status/2072022838857396738 · **ROUTE TO CHANNEL A**
> "BREAKING: Anthropic released Skills for Claude. Most GTM teams will use them like fancy prompts.
> We built them into an operating system that runs outbound, content, and growth for an entire GTM
> function."

**@AlfieJCarter** · 2026-05-14 · https://x.com/AlfieJCarter/status/2054989729767051434 · **ROUTE TO CHANNEL A**
> "I've dedicated 55 hours to creating a complete breakdown of the GTM Engineer's Full Stack and
> exactly how GTM engineers are running 125 skills across 6 layers for free."

These three matter to the **incumbent census, not to forecasting**: there is an active practitioner
market shipping GTM *skills* for Claude specifically. Channel A ranked incumbents by repo; this is
the same niche being contested on the social surface. Flagged, not analysed here.

---

## Circulating figures table — falsification-strip candidates

| Figure | As stated | Subject AS ACTUALLY STATED | Permalink | Grade | Never-ship? |
|---|---|---|---|---|---|
| 3-to-1 / 5-to-1 | "3-to-1 quota coverage was solid, 5-to-1 world class" | quota coverage; base undefined | https://x.com/gtmba_/status/2041174257271480446 | FOLKLORE | **YES — primary** |
| $1M–$2M | "ARR per employee, easily" for AI-native teams | ARR/employee, no N, no source | https://x.com/gtmba_/status/2041174257271480446 | FOLKLORE | YES |
| 45% median | "Q4 Median Quota Attainment: 45%" | share of reps at quota, 20 large enterprise SW cos, RepVue | https://x.com/thaAdamLittle/status/2008940390385152153 | FIGURE (source named) | No — usable WITH subject |
| 26.7% min | "Q4 Min Quota Attainment: 26.7%" | same series | https://x.com/thaAdamLittle/status/2008940390385152153 | FIGURE | No |
| 59.7% max | "Q4 Max Quota Attainment: 59.7%" | share of reps at quota, same series — **VERIFIED 2026-08-03 by thread re-fetch** | https://x.com/thaAdamLittle/status/2008940390385152153 | FIGURE | No |
| 7.8% / −0.3% / 15.7% | Q4 Sales Output Growth median/min/max | RepVue quota-weighted capacity metric, YoY, same 20 cos | https://x.com/thaAdamLittle/status/2008940390385152153 | FIGURE (metric defined inline) | No — positive example |
| 57% | "$SNOW % team quota attainment hasn't budged from 57%" | share of reps at quota, one company | https://x.com/thaAdamLittle/status/2037542426160648422 | FIGURE | No |
| 19.5% | "% of team quota attainment here 19.5%" | share of reps at quota, Medallia | https://x.com/thaAdamLittle/status/2047040250212495660 | FIGURE | No |
| 60% / 67% | "60% of Enterprise… 67% of SMB/MM Sales reps can hit their quota" | share of reps, by segment, $TEAM | https://x.com/thaAdamLittle/status/2012537714613141577 | FIGURE | No |
| 18% | "only 18% of the team can hit quota" | share of reps | https://x.com/thaAdamLittle/status/2055313253132063035 | FIGURE | No |
| 42.4% | "Sales Output … decline 42.4%" | RepVue quota-weighted capacity metric, one company | https://x.com/thaAdamLittle/status/2075580202269512043 | FIGURE (metric defined inline) | No — positive example |
| 40–45% | "avg attainment at legacy SaaS is 40-45% per year" | "avg attainment" — subject ambiguous, no source | https://x.com/Carles_Reina/status/2067608053294191046 | **FOLKLORE** | **YES** |
| 73% | "73% quota attainment doesn't tell you anything without added context" | used rhetorically, not asserted | https://x.com/gtmba_/status/2044801893080174753 | OPINION | No — the POINT is context |
| 70% | "70% of deals lost before stage 3" | **ONE named customer**, vendor case study | https://x.com/BrianLaManna_/status/2063965079821840670 | **CONFOUNDED** | **YES — reads as benchmark** |
| 80% | "SDR Attainment: 80%" ServiceNow | SDR subject (not AE), RepVue | https://x.com/techsaleshackz/status/1885355614248861884 | FIGURE | No |
| 50% | Common Room "50% quota attainment" | SDR role listing, RepVue | https://x.com/techsaleshackz/status/1942258559657607656 | FIGURE | No |
| $1.6M / $200K / 2 | personal quota arithmetic | HIS OWN annual target & avg deal | https://x.com/BrianLaManna_/status/1952722176013996041 | **FIRST-PERSON RESULT** | No — arithmetic IS the teaching |
| $3M / $10M | "pipeline built this year" / "sourced since joining Gong" | pipeline sourced, NOT revenue closed | https://x.com/BrianLaManna_/status/2055273176813154583 · https://x.com/BrianLaManna_/status/1917929213169950720 | FIRST-PERSON RESULT | No — but note the denominator |
| 14 quarters | "hit quota 14 Q's in a row" | own record, unauditable | https://x.com/saleskhalifa/status/2032561814203150794 | FIRST-PERSON RESULT | No |
| $50M / $100M / $275M | Legora pipeline, ARR, and EOY-2026 projection | press/vendor; **$275M is a FORECAST stated as fact** | https://x.com/HarryStebbings/status/2053860005523103932 | FOLKLORE | YES |

---

## NULLS — searched for, genuinely not found (xrelay surface)

1. **Nobody backtested a stage weight.** Across every query, **zero** practitioners stated
   stage-probability percentages (e.g. "discovery = 20%, proposal = 60%") AND said whether those
   numbers were ever validated against outcomes. The hand-set-stage-weight defect the pack wants to
   name is **absent from the practitioner discourse entirely** — it is not defended, not attacked,
   not discussed. That silence is itself the finding: the mechanism is unexamined, not contested.
2. **No first-person forecast-accuracy number.** Not one author reported their own team's forecast
   accuracy as a measured figure. The closest is KyleAsay_'s qualitative "we notice if commit deals
   don't happen." Combined with c2's GitLab FORECASTING NULL and c0's "instruction-to-be-accurate,
   not measurement" finding, **the corpus-wide forecast-accuracy null now survives on three
   independent surfaces (handbook, web, X).** This is the strongest evidence the pack has for the
   flagship.
3. **No evidence CRM hygiene improves an outcome.** The only hygiene-to-outcome links found run the
   OTHER way (best seller has terrible hygiene; hygiene classified as PIP-level "noise").
4. **"Pipeline coverage" as a searchable term is dead on X.** Query returned crypto/CI/CD noise;
   the concept surfaces only incidentally (the gtmba_ 3-to-1 line). Practitioners do not appear to
   discuss coverage ratios in public.

---

## COVERAGE STATEMENT

**Surface: xrelay (X/Twitter) ONLY.** No WebSearch (session quota exhausted crew-wide), no WebFetch
used for this file. Every permalink is a tool-returned `url`.

**Exact queries run** (all `--product Top`, `--limit 12–14`, `timeout 90`, ≥4s gaps, strictly serial):
`weighted pipeline` · `pipeline coverage` · `forecast accuracy` · `sales forecast` (--min-faves 5) ·
`pipeline review` (--min-faves 5) · `quota attainment` (--min-faves 5) · `sales sandbagging`
(--min-faves 5) · `pipeline coverage ratio` (--min-faves 3) · `CRM hygiene` (--min-faves 3) ·
`sales win rate` (--min-faves 3) · `forecast category commit` (--min-faves 3).
**Author-targeted** (typed `--from`, single-term): `thaAdamLittle`+`quota` · `KyleAsay_`+`forecast` ·
`gtmba_`+`quota` · `BrianLaManna_`+`pipeline`.

**NOT searched / NOT done — honest gaps:**
- **No thread reads.** Zero `xrelay thread` calls were made. KyleAsay_'s "3 things" criteria are
  quoted only as far as the search projection reached (criterion 1 of 3 visible). Several quotes end
  in "…" where the 400-char projection cut them. **Any quote ending in "…" must be re-fetched before
  it ships.**
- **Authors not swept:** jasonlk/SaaStr, patio11, levelsio, arvidkahl, robwalling, dvassallo,
  tylertringas (W1's founder-led ground), and sales voices surfaced but not followed:
  `techsaleshackz`, `TechSalesGuy`, `Carles_Reina`, `sammarelich`, `saleskhalifa`, `mistamor`,
  `thedealdirector`, `randomrecruiter`, `KyleAsay_` beyond the `forecast` term.
- **Terms not searched:** `happy ears`, `deal slipped`, `close date`, `deal desk`, `exit criteria`,
  `stage weighted`, `3x pipeline`, `pipeline is a lie`, `commit` alone, `best case`, `Clari`,
  `forecast call`, `revenue operations`, `RevOps`.
- **Date-windowed passes:** none. No `--product Latest` pass was run; everything here is `Top`, which
  biases toward high-engagement and away from recent/low-reach practitioner talk.
- **KBCM figure:** deliberately NOT re-derived (charter says primary-verified in success's corpus);
  the collision above is flagged, not resolved.
