# Design It Twice

When the user wants to explore alternative interfaces for a chosen deepening candidate, use separate design passes in the current session. Based on "Design It Twice" (Ousterhout) — your first idea is unlikely to be the best.

Uses the vocabulary in [SKILL.md](SKILL.md) — **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Before drafting alternatives, write a user-facing explanation of the problem space for the chosen candidate:

- The constraints any new interface would need to satisfy
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch to ground the constraints — not a proposal, just a way to make the constraints concrete

Show this to the user, then wait for confirmation before Step 2.

### 2. Draft separate alternatives

Draft at least three **radically different** interfaces in separate passes. Complete one pass before beginning the next so each constraint remains distinct.

Use the same technical brief for each pass: file paths, coupling details, dependency category from [DEEPENING.md](DEEPENING.md), and what sits behind the seam. Give each pass a different design constraint:

- Pass 1: "Minimize the interface — aim for 1–3 entry points max. Maximise leverage per entry point."
- Pass 2: "Maximise flexibility — support many use cases and extension."
- Pass 3: "Optimise for the most common caller — make the default case trivial."
- Pass 4 (if applicable): "Design around ports & adapters for cross-seam dependencies."

Use both [SKILL.md](SKILL.md) vocabulary and CONTEXT.md vocabulary so each pass names things consistently with the architecture language and the project's domain language.

Each pass outputs:

1. Interface (types, methods, params — plus invariants, ordering, error modes)
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs — where leverage is high, where it's thin

### 3. Present and compare

Present designs sequentially so the user can absorb each one, then compare them in prose. Contrast by **depth** (leverage at the interface), **locality** (where change concentrates), and **seam placement**.

After comparing, give your own recommendation: which design you think is strongest and why. If elements from different designs would combine well, propose a hybrid. Be opinionated — the user wants a strong read, not a menu.
