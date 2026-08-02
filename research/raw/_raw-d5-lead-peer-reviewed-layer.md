# D-lead slice — the peer-reviewed evidence layer the sales canon never cites

Channel D (evidence vs. folklore), **lead slice** (not a worker file). Scope chosen to fill a gap
none of D1–D4 cover: the **academic literatures that bear directly on core sales practices** —
win/loss learning, discovery questioning, negotiation/anchoring, and what actually predicts
salesperson performance. D1 asks "is the *methodology* evidence-based?" (answer: mostly no).
This file asks the complementary question: **"is there good evidence about the *underlying
activities* — and does it agree with the canon?"** (answer: yes there is, and frequently no it
doesn't).

Method note: the session-wide WebSearch budget was exhausted (200/200) before this slice began.
All retrieval here used WebFetch against DuckDuckGo Lite, the Semantic Scholar Graph API and the
Crossref API via `curl` (with retry loops — S2 429s aggressively), plus `curl` + `pdftotext` for
full texts. Every quote below was read from the actual fetched artifact, not from a search snippet.

Grades: PRIMARY / SECONDARY / VENDOR-SELF-REPORTED / FOLKLORE / CONTESTED.

---

## 1. Win/loss learning: the buyer's stated reason is not the cause

**This is the strongest single citation in my slice, and it is not from the sales literature at all.**

**Nisbett, R. E., & Wilson, T. D. (1977). "Telling More Than We Can Know: Verbal Reports on
Mental Processes." *Psychological Review*, 84(3), 231–259.**
- GRADE: **PRIMARY.** Full text downloaded and read via `curl` + `pdftotext` (2.2MB scan; note
  WebFetch alone could NOT parse this PDF — it returned binary garbage. The curl+pdftotext route
  is what made the verbatim quotes below possible).
- Verified fetchable copy: https://home.csulb.edu/~cwallis/382/readings/482/nisbett%20saying%20more.pdf
- Record: https://psycnet.apa.org/record/1978-00295-001 · Volume/number/date confirmed from the
  article's own masthead in the PDF: "VOLUME 84 NUMBER 3 MAY 1977".
- One of the most-cited papers in the history of psychology.

**Verbatim, from the paper's own abstract (p. 231):**
> "Evidence is reviewed which suggests that there may be little or no direct introspective access
> to higher order cognitive processes. Subjects are sometimes (a) unaware of the existence of a
> stimulus that importantly influenced a response, (b) unaware of the existence of the response,
> and (c) unaware that the stimulus has affected the response. It is proposed that when people
> attempt to report on their cognitive processes, that is, on the processes mediating the effects
> of a stimulus on a response, they do not do so on the basis of any true introspection. Instead,
> their reports are based on a priori, implicit causal theories, or judgments about the extent to
> which a particular stimulus is a plausible cause of a given response."

**Verbatim, conclusion 1 (p. 233):**
> "People often cannot report accurately on the effects of particular stimuli on higher order,
> inference-based responses. Indeed, sometimes they cannot report on the existence of critical
> stimuli, sometimes cannot report on the existence of their responses, and sometimes cannot even
> report that an inferential process of any kind has occurred. The accuracy of subjective reports
> is so poor as to suggest that any introspective access that may exist is not sufficient…"

### Why this lands squarely on win/loss analysis

The paper's own opening examples are **purchase-choice** questions — the authors list prior studies
asking people why they liked particular political candidates or **detergents** (Kornhauser &
Lazarsfeld, 1935), why they chose an occupation, and so on. The framing sentence is literally:
*"'Why do you like him?' 'How did you solve this problem?' 'Why did you take that job?'"*

**The decisive experiment is a consumer-choice study (pp. 243–244), the "position effect" studies.**
Quoted verbatim, with its local context:
> "In both studies, conducted in commercial establishments under the guise of a consumer survey,
> passersby were invited to evaluate articles of clothing—four different nightgowns in one study
> (378 subjects) and **four identical pairs of nylon stockings** in the other (52 subjects).
> Subjects were asked to say which article of clothing was the best quality and, when they
> announced a choice, were asked why they had chosen the article they had. There was a pronounced
> left-to-right position effect, such that the right-most object in the array was heavily
> overchosen. For the stockings, the effect was quite large, with the right-most stockings being
> preferred over the left-most **by a factor of almost four to one**. When asked about the reasons
> for their choices, **no subject ever mentioned spontaneously the position of the article** in the
> array. And, when asked directly about a possible effect of the position of the article,
> **virtually all subjects denied it**…"

SUBJECT CHECK (per the charter's verify-the-subject rule): the 4:1 figure is the **stockings** study
(n=52, four *identical* pairs), not the nightgown study (n=378, four *different* nightgowns). The
items were identical, so every "reason" a subject gave for choosing one was necessarily a
confabulation. Do not merge the two studies or transfer the 4:1 ratio to the nightgowns.

**The sharpest finding for our purposes is the observer-subject result (pp. 1302–1320 of the text
file / discussion section), which is stronger than "buyers are sometimes wrong":**
> "The observer subjects made predictions that in every case were similar to the erroneous reports
> given by the actual subjects."

and, on the authors' word-association study:
> "the judgments of the probability that particular word cues would affect particular target
> responses were positively correlated with the original subjects' 'introspective reports' of the
> effects of the word cues on the target responses. (**Both subject reports and observer
> predictions were slightly negatively correlated with true cuing effects.**)"

That is the load-bearing point. Outside observers who never experienced the situation produced the
*same* answers as the people who did. **A stated reason therefore carries no privileged information
about the actual cause** — it is a plausible theory, and an outsider can generate the same theory.
Applied to sales: when a lost-deal interview yields "we went with X because of price," that answer
is evidence about *what reason sounds plausible to the buyer*, not about what caused the loss.

The authors are careful about the boundary condition, and the pack must carry it honestly —
they explicitly do **not** claim reports are always wrong (abstract, continued):
> "This suggests that though people may not be able to observe directly their cognitive processes,
> they will sometimes be able to report accurately about them. Accurate reports will occur when
> influential stimuli are salient and are plausible causes of the responses they produce, and will
> not occur when stimuli are not salient or are not plausible causes."

So the honest teaching is **not** "win/loss interviews are worthless." It is: *self-reported reasons
are reliable only where the true cause was salient and plausible; they are systematically
unreliable for exactly the subtle, competitive, relational factors win/loss analysis most wants to
learn about* — and there is no way for the interviewer to tell which case they are in from the
answer alone. Combine with a behavioural/outcome signal, never treat the stated reason as the cause.

### Does the win/loss vendor category acknowledge this? (spot check — one page, scoped honestly)

I checked the leading win/loss vendor's own buyer-interview guidance — Clozd, "Win-Loss 101: What to
Ask Buyers in Win-Loss Interviews": https://www.clozd.com/blog/win-loss-101-what-to-ask-buyers-in-win-loss-interviews

**Result: the page contains no acknowledgment of self-report limitations** — no mention of post-hoc
rationalisation, social-desirability bias, or any validity concern about buyer-stated reasons. Its
stated rationale is a *consistency* argument, not a validity one ("you don't have enough consistent
data to identify any meaningful trends"), and it claims interviews "give you data that no other tool
or platform can provide."

GRADE: **VENDOR-SELF-REPORTED**, and deliberately scoped: this is **one page from one vendor**,
checked once. It is evidence that the category's flagship how-to content does not raise the problem;
it is **not** a claim that no win/loss practitioner anywhere addresses it. Do not let the pack
overstate this into "the whole win/loss industry ignores validity" — that assertion would need the
grep-verified uniqueness check the family's rules require, and I did not do it. What it does support
is the narrower, defensible claim that **the standard practitioner guidance treats the buyer's stated
reason as data rather than as testimony to be corroborated.**

**Family line:** this is the sales-side instance of the measurement-honesty through-line
(attribution → feasibility → health-score validity → forecast honesty). It is also structurally the
same discovery the `success` pack made with Ascarza/BTYD — the canon's central inferential move is
unvalidated. Flagged for the controller as a **wedge candidate**, since win/loss learning is in the
charter's Includes list (item 14) and no incumbent pack is likely to cite this literature.

---

## 2. What actually predicts salesperson performance — two real meta-analyses

The canon sells universal systems. The peer-reviewed meta-analytic record says the determinants are
**contingent**, and that one of the canon's favourite virtues only shows up when reps grade their
own homework.

### 2a. Franke & Park (2006) — the self-rating trap

**Franke, G. R., & Park, J.-E. (2006). "Salesperson Adaptive Selling Behavior and Customer
Orientation: A Meta-Analysis." *Journal of Marketing Research*, 43(4), 693–702.
DOI 10.1509/jmkr.43.4.693.** Cited 738× (Semantic Scholar).
- GRADE: **PRIMARY** (peer-reviewed meta-analysis in a top-tier journal). Bibliographic record and
  abstract read directly from the Crossref API: https://api.crossref.org/works/10.1509/jmkr.43.4.693

**Verbatim from the abstract:**
> "The authors combine findings from **155 samples of more than 31,000 salespeople** to test
> alternative models of antecedents and consequences of adaptive selling behavior (ASB) and
> customer orientation (CO). A random-effects meta-analysis yields average values for 28 different
> correlations **ranging from -.16 to .35**, 19 of which are significant. Controlling for
> salesperson gender and selling experience, structural equation modeling indicates that **ASB
> increases self-rated, manager-rated, and objective measures of performance, whereas CO increases
> only self-rated performance.**"

**Two findings the pack should carry:**
1. **The self-rating trap.** *Customer orientation improved only SELF-RATED performance* — it did
   not show up in manager ratings or objective measures. Adaptive selling survived all three.
   This is a measurement-validity result of exactly the family's house type: a widely-praised sales
   virtue looks effective only in the measure most vulnerable to the respondent's self-image.
   Any "our reps are more customer-focused" claim measured by asking the reps is uninformative.
2. **Effect sizes are modest.** Correlations top out at .35 across 28 relationships, with some
   negative. Nothing in the credible sales literature supports transformation-grade claims.

SUBJECT CHECK: the 31,000+ figure is **salespeople pooled across 155 samples in a meta-analysis** —
it is not one study, not one company, and not 31,000 *calls* or *deals*. Do not restate it as a
study of 31,000 salespeople at a firm.

### 2b. Kerr & Marcos-Cuevas (2023) — determinants are contingent, not universal

**Kerr, P. D., & Marcos-Cuevas, J. (2023). "Reclaiming the contingent nature of the determinants of
salesperson performance: an extended meta-analysis." *Journal of Personal Selling & Sales
Management*. DOI 10.1080/08853134.2023.2250561.** Cited 14×.
- GRADE: **PRIMARY.** Record + abstract read from the Semantic Scholar Graph API.
- Open-access copy located (not paywalled): https://dspace.lib.cranfield.ac.uk/handle/1826/20409

**Verbatim from the abstract:**
> "we present a meta-analysis of the determinants of salesperson performance using **150 studies,
> 936 raw effects, and ten moderating variables captured from 2009 to 2020**. Our findings enable us
> to identify **19 key determinants** of performance and to classify these within a sales determinant
> continuum, **ranging from universal, to context-specific to necessary but insufficient predictors
> of performance**. Our results show **the significant influence the operationalization of
> salesperson performance has on the relationship between sales determinants and performance
> outcomes.**"

Two points for the pack. First, a modern, large, peer-reviewed meta-analysis explicitly concludes
that most performance determinants are **context-specific or merely necessary-but-insufficient**,
not universal — which is the academic warrant for the pack refusing to prescribe one methodology.
Second, and again a measurement-honesty finding: **how you operationalise "performance" significantly
changes which determinants appear to matter.** Same trap as 2a, stated at the level of the whole
literature.

---

## 3. Negotiation and pricing presentation: the anchoring doctrine has real boundary conditions

The canon's advice ("always anchor first, anchor high") is drawn from anchoring research, but the
current peer-reviewed record is more interesting than the advice — and in two places contradicts it.

### 3a. A 26-million-observation field study (the largest evidence base found in this channel)

**Schweinsberg, M., Petrowsky, H. M., Funk, B., & Loschelder, D. D. (2023). "Understanding the
first-offer conundrum: How buyer offers impact sale price and impasse risk in 26 million eBay
negotiations." *Proceedings of the National Academy of Sciences (PNAS)*.
DOI 10.1073/pnas.2218582120.** Open access: https://doi.org/10.1073/pnas.2218582120
- GRADE: **PRIMARY** (PNAS, real-world behavioural field data at extreme scale). Abstract read from
  the Semantic Scholar Graph API record.

**Verbatim from the significance statement:**
> "In price negotiations, a vexing question plagues buyers everywhere. How ambitious is the ideal
> first offer? While more ambitious offers lower the price, they also risk nonagreement. The
> literatures in psychology, management, and data science **have yet to offer an empirical answer to
> this first-offer conundrum.** Based on over **26 million eBay negotiations**, we generate an answer
> that integrates a **linear anchoring effect on price and nonlinear effects on impasse risk.** We
> offer applied, machine learning–based recommendations and contribute to the scholarly debate by
> establishing first-offer effects and **nonlinear relationships that are incompatible with current
> theorizing.**"

This is the shape the pack should teach and the canon never does: **the price benefit of a more
aggressive anchor is roughly linear, but the risk of no deal at all is non-linear.** "Anchor high"
is therefore not a monotonic rule — there is a tradeoff frontier, and past a point you buy a small
price gain with a sharply rising chance of no deal. Note also the authors' own admission that the
literature had *not* previously answered this empirically. SUBJECT CHECK: these are **buyer** offers
in an online consumer marketplace (eBay Best Offer), not B2B enterprise negotiations — the shape of
the finding transfers, the specific numbers do not, and the pack must say so.

### 3b. A documented first-mover DISADVANTAGE under information asymmetry

**Maaravi, Y., & Levy, A. (2017). "When your anchor sinks your boat: Information asymmetry in
distributive negotiations and the disadvantage of making the first offer." *Judgment and Decision
Making*. DOI 10.1017/s193029750000646x.** Cited 19×.
- GRADE: **PRIMARY.** Open-access PDF confirmed at Cambridge Core:
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/55F2E0FACFE342C18EEA768A9E4A3B72/S193029750000646Xa.pdf/div-class-title-when-your-anchor-sinks-your-boat-information-asymmetry-in-distributive-negotiations-and-the-disadvantage-of-making-the-first-offer-div.pdf

**Verbatim from the abstract:**
> "The literature on behavioral decision-making and negotiations to date **usually advocates
> first-mover advantage in distributive negotiations**, and bases this preference on the anchoring
> heuristic. In the following paper, we suggest that the preference for moving first vs. moving
> second in negotiations **may not be as clear-cut as presumed**, especially in situations
> characterized by **information asymmetry** between negotiating counterparts. In Study 1, we
> examined people's initiation preferences and found that **unless taught otherwise, people
> intuitively often prefer to move second.** In Studies 2–4, we experimentally tested the suggested
> advantage of moving second, and demonstrated that in information-asymmetry scenarios — **when one
> party has perfect background information and the other has none — it is actually preferable for
> both counterparts not to give the first offer** while negotiating."

Directly relevant to **pricing presentation**, which the charter assigns to sales (product owns
pricing *design*). The common B2B case — seller knows their own cost/discount floor and comparable
deals, buyer does not, or vice versa — is an information-asymmetry case, precisely where the
blanket "always make the first offer" advice is contested by experimental evidence.
GRADE for the doctrine itself: **CONTESTED**, with a permalinked source on each side (the standard
first-mover-advantage literature vs. this paper) — which satisfies the charter's R21 rule (c),
"both sides are permalinked," making this figure/claim worth carrying.

---

## 4. Discovery questioning — a NULL RESULT worth recording

I attempted to locate the peer-reviewed literature on **question-asking in conversation** (the
Huang/Yeomans/Brooks/Minson/Gino line on question-asking and interpersonal liking) as an evidence
base for discovery-call practice, since SPIN's own evidence base collapsed (see D1).

**FIRST PASS = NULL, and it was a TOOLING NULL.** My Semantic Scholar query
`asking+questions+increases+liking+conversation` returned an empty `data` array. I originally
recorded that as a genuine empty result. **It was not.** On re-running the same claim-area against
**OpenAlex** (which, per D3, does not rate-limit, unlike S2 which 429s constantly), both papers
surfaced immediately. This is a live instance of exactly the hazard the controller ruled on — a
degraded search surface producing something that reads as evidence of absence.

**CLOSED — the literature exists, and it is top-tier:**

- **Huang, K., Yeomans, M., Brooks, A. W., Minson, J. A., & Gino, F. (2017). "It doesn't hurt to
  ask: Question-asking increases liking." *Journal of Personality and Social Psychology*.**
  DOI: 10.1037/pspi0000097
- **Yeomans, M., Brooks, A. W., Huang, K., Minson, J. A., & Gino, F. (2019). "It helps to ask: The
  cumulative benefits of asking follow-up questions." *JPSP*.** DOI: 10.1037/pspi0000220
- GRADE: **PRIMARY** for both (peer-reviewed, JPSP). Author lists and venues verified from the
  OpenAlex records, not from memory — note my own earlier guess at the 2017 author list was
  incomplete, which is why it is written out in full here.

**THE CAVEAT IS LOAD-BEARING AND MUST TRAVEL.** These are studies of **question-asking in
conversation and its effect on liking** — speed-dating and get-to-know-you dyads — **not studies of
sales discovery calls.** They establish that asking questions, and especially *follow-up* questions,
increases how much a counterpart likes you. They do **not** establish that any sales questioning
framework improves deal outcomes, and they must never be used to retroactively validate SPIN.

So the honest position for the pack is now sharper than "no evidence exists":
**there is good evidence that question-asking builds rapport, and no published evidence that any
branded sales questioning methodology improves win rates.** Those are different claims, and the
canon routinely conflates them. That gap is itself teachable material.

---

## 5. Gap-fill for D4: California's bot-disclosure law, from the primary statute

D4 (AI-outbound) explicitly declined to report US state-level AI disclosure law because it could
not primary-source it, and correctly refused to guess. I closed that gap, because AI-sales POLICY
is assigned to this pack by the charter (ai owns agent mechanics; sales owns the policy).

**California Business & Professions Code, Division 7, Part 3, Chapter 6 — "Bots" (§§ 17940–17943).
Added by Stats. 2018, Ch. 892, Sec. 1 (SB 1001). Effective January 1, 2019. Operative July 1, 2019
per § 17943.**
- GRADE: **PRIMARY** (the statute's own text, retrieved from the California Legislature's official
  code site and extracted in full via `curl` + HTML strip, not from a summary).
- Permalink: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&title=&part=3.&chapter=6.&article=

**§ 17941(a), verbatim and complete:**
> "It shall be unlawful for any person to use a bot to communicate or interact with another person
> in California online, with the intent to mislead the other person about its artificial identity
> for the purpose of knowingly deceiving the person about the content of the communication **in
> order to incentivize a purchase or sale of goods or services in a commercial transaction** or to
> influence a vote in an election. **A person using a bot shall not be liable under this section if
> the person discloses that it is a bot.**"

**§ 17941(b), verbatim:**
> "The disclosure required by this section shall be clear, conspicuous, and reasonably designed to
> inform persons with whom the bot communicates or interacts that it is a bot."

**§ 17940(a), verbatim:**
> "'Bot' means an automated online account where all or substantially all of the actions or posts
> of that account are not the result of a person."

Two things make this unusually on-point for a sales pack. First, the statute's operative clause is
aimed *specifically at commercial selling* — "in order to incentivize a purchase or sale of goods or
services in a commercial transaction" is the exact conduct an AI SDR performs. Second, it is a
**safe-harbour statute, not a ban**: disclosure cures liability. The pack's AI-sales policy can
therefore be stated as a concrete, sourced rule rather than a vibe — *disclose the bot, clearly and
conspicuously, at the point of interaction.* That aligns with EU AI Act Art. 50(1) (D4, §B5), giving
two independent jurisdictions converging on the same operational requirement.

### CORRECTION — a scope claim that is widely repeated and is WRONG

There is a common secondary claim that California's bot law "only applies to platforms with
10 million or more monthly visitors." **The statute's own structure falsifies this.** The chapter
defines two *different* terms:

> **§ 17940(b)** "'**Online**' means appearing on any public-facing Internet Web site, Web
> application, or digital application, including a social network or publication."  ← no threshold
>
> **§ 17940(c)** "'**Online platform**' means any public-facing Internet Web site, Web application,
> or digital application, including a social network or publication, **that has 10,000,000 or more
> unique monthly United States visitors or users** for a majority of months during the preceding 12
> months."

The prohibition in § 17941(a) is triggered by communicating "**online**" — the § 17940(b) term,
which carries **no visitor threshold**. The threshold-bearing term "online platform" appears in the
operative text of this chapter in exactly one place, and it is not the prohibition:

> **§ 17942(c)** "This chapter does not impose a duty on **service providers of online platforms**,
> including, but not limited to, Web hosting and Internet service providers."

So the 10-million figure defines whose *infrastructure providers* are carved out — it does **not**
limit who the prohibition binds. A solo founder running an AI SDR against California recipients is
within scope on the face of the text.

GRADE: **PRIMARY** for the statutory text and its structure (both definitions and all three
operative sections were read verbatim). I am reporting *what the text says*; I am not offering a
legal opinion on how courts have construed it, and the pack must not either — the honest framing is
"the statute's prohibition is not written with the 10M threshold; do not assume you are exempt."
Flagged for the controller as a **candidate never-ship claim in inverted form**: the never-ship item
is the *exemption* claim ("we're under 10M visitors so it doesn't apply"), which is the version a
reader is most likely to arrive with.

---

## 6. CORRECTION TO D1 — the MEDDPICC ruling, read from the actual federal opinion

D1 reported the MEDDPICC trademark ruling from a **PR Newswire press release issued by MEDDICC
Ltd., the winning party**, and graded the opinion text SECONDARY because it had not read the
opinion. I retrieved the actual court documents. **D1's core finding is confirmed, but two of its
surrounding characterisations are wrong, and one is inverted.** This matters because the charter
treats licensing/IP claims as a hard-verification class.

**Primary documents, downloaded and read in full (`curl` + `pdftotext`):**
- **Opinion, ECF No. 99** (33 pages), filed 04/21/26:
  https://storage.courtlistener.com/recap/gov.uscourts.paed.621688/gov.uscourts.paed.621688.99.0.pdf
- **Order, ECF No. 100** (3 pages), filed 04/21/26:
  https://storage.courtlistener.com/recap/gov.uscourts.paed.621688/gov.uscourts.paed.621688.100.0.pdf
- Docket: *MEDDICC LTD. v. 01 CONSULTING LLC*, No. 2:24-cv-01836 (E.D. Pa.), filed 2024-04-30,
  Chief Judge Wendy Beetlestone, cause 15:1125 Lanham Act —
  https://www.courtlistener.com/docket/68488997/meddicc-ltd-v-01-consulting-llc/
- GRADE: **PRIMARY** (the court's own opinion and order, via CourtListener/RECAP — a neutral
  third-party repository, not a party's press release).

### CONFIRMED — the holding is real, and here is its exact wording and exact scope

> "Accordingly, a jury 'would be compelled to find,' El, 479 F.3d at 238, that **MEDDPICC is a
> generic term for business education services and content.** And on that basis, Plaintiff is
> entitled to summary judgment on all of Lahoutifard's counterclaims and on its claim for a
> declaratory judgment of noninfringement." (Opinion, p. 31)

And from the Order (¶ 2(a)(iii)):
> "IT IS FURTHER ORDERED that the Director of the United States Patent and Trademark Office (PTO)
> is HEREBY ORDERED to **CANCEL the trademark at Registration Number 6,489,058** and MAKE an
> appropriate entry upon the records of the PTO."

**SCOPE PRECISION the pack must preserve:** the holding is that MEDDPICC is generic **"for business
education services and content"** — the registration classes at issue (class 9 e-books/videos and
class 41 online courses). It is *not* an abstract ruling that "MEDDPICC is a generic word." Do not
strip the service-category qualifier when citing this.

### CORRECTION 1 — summary judgment was granted IN PART, and the case is not over

D1 says "Chief Judge Wendy Beetlestone granted summary judgment on April 21, 2026." The Order says:

> "Plaintiff's Motion for Summary Judgment … **The Motion is DENIED in all other respects.**"

Summary judgment was **granted in part and denied in part** (Opinion, p. 2: "Plaintiff's Motion will
be granted in part and denied in part"). Plaintiff's tortious-interference and trade-libel claims
**survive and remain live** — the Order expressly sets a schedule for them (¶ 3), and the opinion's
final paragraph states "Plaintiff has not shown that it is entitled to summary judgment on its
contractual interference claims." The docket's last known filing is **July 16, 2026**, i.e. the
litigation was still active as of ~2.5 weeks before this research. The pack must not describe this
as a concluded case or a clean sweep.

### CORRECTION 2 (INVERTED) — McMahon's testimony was EXCLUDED, not relied upon

D1 wrote that "The court relied in part on expert testimony from **John McMahon** … giving this
ruling unusual evidentiary weight as closer to a primary-source-adjudicated history." **The opposite
happened.** Order ¶ 1:

> "Upon consideration of **Defendants' Motion to Exclude Expert Testimony of John McMahon** … IT IS
> HEREBY ORDERED that the Motion is **GRANTED** as follows. **McMahon shall not be permitted to
> testify at trial** about his understanding that: … e. some terms are categorically prohibited from
> serving as trademarks because they are the generic name for the category…; g. the MEDDPICC
> methodology cannot be considered a trademark; h. Lahoutifard's mark should have never registered…"

Nine enumerated topics (a–i) were excluded — essentially all of McMahon's legal-conclusion opinions.
The genericness holding rests on the court's own analysis of consumer-perception evidence, **not** on
McMahon. D1's inference of "unusual evidentiary weight" from McMahon's involvement should be struck.
Root cause worth recording: this error entered because the source was **the winning party's press
release**, which naturally foregrounded its own expert and omitted that he was partly excluded.

### BONUS — the opinion is now the best available PRIMARY history of MEDDIC, better than the vendor page

D1 flagged the MEDDIC origin date as CONTESTED (vendor page said 1996; press release implied early
1990s). **The court's findings resolve it**, and supersede meddicc.com as a source:

> "**In the early 1990s**, a software startup, Parametric Technology Corporation (PTC), found itself
> in need of a way of identifying sales opportunities compatible with its limited product
> capabilities. Through a process of trial and error, PTC's sales team took their best practices for
> managing business opportunities and distilled them into an acronym: MEDDIC." (Opinion, p. 3)

> "Most importantly, **in 2005, former PTC employees coined MEDDPICC.** MEDDPICC preserved the core
> sales qualification framework embodied in MEDDIC while adding two components: **Paper Process and
> Competition.**" (Opinion, p. 4)

Also court-found, and useful for the pack's lineage map: Lahoutifard "joined the firm in 1992 after
being recruited by John McMahon," "takes no credit for coining MEDDIC," "left PTC in 1995 or 1996,"
launched MEDDIC Academy "in or around 2017," and obtained Reg. No. 6,489,058 in **September 2021**.

### A NEW never-ship figure, and a conflict with D1's

The opinion contains its own PTC revenue claim, and **it does not match the vendor figure D1 flagged**:

> "In the 1990s, PTC trained its sales force to use MEDDIC. **Its revenues shot up from $1 million in
> 1989 to $1.1 billion in 1998.**" (Opinion, p. 3)

D1's never-ship list flagged the vendor version, "PTC grew revenue from $300M to $1B+ in four years."
These are **two different figures for the same underlying story**, and now one of them appears in a
federal opinion — which will make it *more* quotable, not less. Both are uncontrolled
post-hoc attributions of a decade of company growth to a sales acronym; the court was recounting
background, not making a causal finding. **Ship neither as evidence that MEDDIC works.** If the
lineage is discussed at all, the honest form is: a court recorded PTC's growth as background to the
methodology's origin, which is not a claim about the methodology's effectiveness.

---

## Grading summary

| Source | What it establishes | Grade | Bears on |
|---|---|---|---|
| Nisbett & Wilson 1977, *Psych Review* 84(3):231–259 | Stated reasons for choices are post-hoc plausible theories, not introspected causes; observers reproduce the same reports | PRIMARY | **Win/loss learning** (charter item 14) |
| Franke & Park 2006, *JMR* 43(4):693–702 | 155 samples / 31,000+ reps: adaptive selling raises objective performance; customer orientation raises **only self-rated** performance | PRIMARY | Rep behaviour, and measurement validity |
| Kerr & Marcos-Cuevas 2023, *JPSSM* | 150 studies / 936 effects: determinants are universal → context-specific → necessary-but-insufficient; operationalisation of "performance" changes the answer | PRIMARY | Why no single methodology is prescribable |
| Schweinsberg et al. 2023, *PNAS* | 26M eBay negotiations: linear anchor effect on price, **non-linear** effect on impasse risk; "incompatible with current theorizing" | PRIMARY | Negotiation, pricing presentation |
| Maaravi & Levy 2017, *JDM* | Under information asymmetry, moving **second** is preferable for both parties | PRIMARY (contests the doctrine) | Negotiation, pricing presentation |

## Candidate never-ship figures / claims from this slice

- **"Always make the first offer / always anchor high."** Not a never-ship *figure* but a never-ship
  *rule* — CONTESTED with permalinks on both sides (Maaravi & Levy 2017; Schweinsberg et al. 2023's
  non-linear impasse risk). If the pack states it, it must state the boundary conditions.
- **The 4:1 stockings ratio (Nisbett & Wilson).** Safe to ship *only* with its subject attached
  (n=52, four **identical** pairs, right-most over left-most). Never as "consumers prefer
  right-hand options 4:1" — that generalisation is not what the study licenses.
- **"31,000 salespeople" (Franke & Park).** Ship only as "155 samples pooled in a meta-analysis,"
  never as a single study or single firm.
- **"26 million negotiations" (Schweinsberg et al.).** Ship only with "eBay Best Offer, consumer
  marketplace, buyer-side offers" attached. The scale invites decontextualised reuse as though it
  were B2B evidence; it is not.
- **"California's bot-disclosure law only applies to platforms with 10M+ monthly visitors."**
  A never-ship claim in *inverted* form — the danger is a reader using it to conclude they are
  exempt. Falsified directly by the statute's structure (§ 17941(a) is triggered by "online" per
  § 17940(b), which has no threshold; the 10M figure lives in § 17940(c) "online platform," used
  operatively only in the § 17942(c) service-provider carve-out). Worth teaching as a
  recognise-and-correct item under charter R21 clause (a).
- Note on the **–.16 to .35** correlation range: worth shipping *as* the teaching (charter R21
  clause b — its arithmetic is the point), because it calibrates the reader against
  transformation-grade vendor claims.
