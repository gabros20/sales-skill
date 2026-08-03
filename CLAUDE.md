# Claude Code repository guide

This is the released `sales-skill` (runtime skill `sales`, under `skills/sales/`). Read
[AGENTS.md](AGENTS.md) for the ownership boundary and non-negotiable invariants — especially: run
the Existence Gate before building any sales apparatus, never ship a win rate without its
denominator, grade every figure inline, and treat forecast method and forecast accuracy as
different claims — accuracy is published by no one. This skill does not own demand creation or
deliverability doctrine (`marketing`), funnel experiments (`growth`), pricing-tier design or
dunning (`product`), the sales assistant's mechanics and evals (`ai`), or CRM sync/write-path
mechanics (`automation`). The renewal-vs-expansion-close boundary with `success` is contested and
carried forward, never resolved silently.

Run `scripts/check-sync` before any release. Keep `SKILL.md` the router; keep versions out of it.
