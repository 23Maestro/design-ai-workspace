---
name: research
description: "Investigate a question against high-trust primary sources in the current session and capture the findings as Markdown. Use only when the user explicitly names this skill."
---

## Invocation contract

Use this skill only when the user explicitly names it. Keep all analysis and execution in the current session. Recommend related skills or a separate task when useful, and leave every launch to the user. Leave agent hooks and model settings unchanged. Stage, commit, push, branch, and worktree actions require a separate explicit request from the user.

Do the research in the current session. If the work should move elsewhere, prepare a handoff and let the user launch the separate task.
Its job:

1. Investigate the question against **primary sources** — official docs, source code, specs, first-party APIs — not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.
