# Design AI workspace

Build more of each screen in code. Keep Figma for ideas and sketches.

This kit helps a team use AI with its own React code. The designer guides the
work. AI helps build it. The team checks the result.

## How it works

1. Sketch an idea in Figma.
2. Pick the React parts your app already has.
3. Ask Claude or Codex to build with those parts.
4. Open the screen and try it.
5. Have a designer check the look and a developer check the code.

Keep the same parts and styles across screens. Test what the app does. Check
how it looks on a phone. Try it with a keyboard, too.

## Start here

Ask a developer to help with the first setup:

- [Set up your app](docs/app-setup.md). Use the app you have.
- [List its UI parts](design-system/components.md). These are React components.
- [Add your design rules](design-system/rules.md).
- [Plan 1 small test](briefs/pilot.md).

Then [follow the steps](docs/workflow.md). Build 1 flow: the steps a person
takes to finish a task. Check that flow before you add more.

## Pick a skill

Skills are guides that tell AI how to help. You choose when to use each one.

- `grill-with-docs`: work through the plan, 1 question at a time.
- `implement`: build 1 small change from start to end.
- `tdd`: write a test, then make it pass.
- `code-review`: check the code against the plan and the team's rules.

For a big plan, use `to-spec` and `to-tickets` to split the work.
Use `improve-codebase-architecture` when old code is hard to change.
It is an extra tool. You do not need it for each task.

[See all 16 skills](docs/skills.md).

## What you get

- [Shared terms](CONTEXT.md) and [rules for AI](AGENTS.md).
- A [plan for 1 flow](briefs/pilot.md).
- A [review sheet](templates/review.md) to record checks and sign-off.

This is a starter kit, not a ready app. No app or Figma file is linked yet.
No team trial has run. Start small and record what works.

## Where it came from

[Read about the work behind this kit](docs/experience.md). Jerami uses Codex
with React and Tailwind in his own Next.js site. He guides changes and checks
the result.

The skills come from local copies of [Matt Pocock's skills](https://github.com/mattpocock/skills).
See the [license notes](THIRD_PARTY_NOTICES.md) and [saved file hashes](skills-manifest.json).

## Check the kit

With Python 3 installed, run:

```sh
python3 scripts/check_workspace.py
```

This checks the kit's files and links. It does not test your app.
