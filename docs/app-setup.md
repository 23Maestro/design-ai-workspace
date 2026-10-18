# Connect an app

This template has no app runtime. Complete this page in the target app repo
before implementation. An engineer owns the first setup.

## Copy with care

Read the target repo's agent rules first. Compare `.agents/skills/` names before
copying. Merge approved rules into the existing agent guide. Do not overwrite
an existing `AGENTS.md`, `CONTEXT.md`, component library, or skill folder.
Copy the design-system pages and brief only after choosing their target paths.
Keep a single task tracker and update links to match the chosen paths.

## Record the app

- App repo and exact reviewed revision: pending.
- Designer and engineer reviewers: pending.
- Framework and package manager: pending; use the app's current choices.
- Install command: pending.
- Run command: pending.
- Typecheck and lint commands: pending.
- Behavior and accessibility check commands: pending.
- Build command: pending.
- Approved hosted preview path: pending.
- Existing Figma library and protected workflow: pending.
- Tracker and pilot issue: pending.
- Review base ref: pending; it must resolve before the `code-review` skill runs.

Connect the real component exports in [the map](../design-system/components.md).
Record source tokens in [the rules](../design-system/rules.md). Test commands
are required for the pilot only where they check the agreed behavior. Mark
missing checks as gaps. Never invent a passing result.

## Give the agent a bounded request

Use the pilot brief's scope. Name the existing components, protected values,
and required states. Ask for 1 complete slice. Inspect the result before
expanding. Use the existing app framework; this harness does not require
Next.js, Vercel, Figma Make, or Paper.
