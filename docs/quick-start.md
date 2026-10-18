# Start with your AI tool

Use Claude Code or Codex. You do not need both.
The skills ship with this repo. No API key goes in these files.
You still need access to the AI tool you choose.

## Make your own copy

On GitHub, click **Use this template**, then **Create a new repository**.
Clone your new repo to your computer. Open that folder in your AI tool.
A Git clone keeps the hidden `.claude` and `.agents` folders.

## Claude Code

1. Open this repo in Claude Code.
2. Type `/skills`. Check that `ask-matt` is listed as a project skill.
3. Type `/memory`. Check that the project `CLAUDE.md` and its imported
   `AGENTS.md` are listed. Press Escape to leave the menu.
4. Run `/ask-matt` and describe the flow you want to try.

Claude reads the entry files in `.claude/skills/`. Each one points to the
shared skill in `.agents/skills/`. The entries run only when you ask.
If you already have a personal skill with the same name, Claude may use it
first. Check the source in `/skills` before you start.

## Codex

1. Open this repo in Codex.
2. Check that `ask-matt` is in the skill list.
3. Use `$ask-matt` in chat and describe the flow you want to try.

Codex reads `.agents/skills/`. The `agents/openai.yaml` files hold Codex menu
labels and settings. They do not change the shared instructions or require
an OpenAI account when you use Claude Code.

## Do I need Matt's setup skill?

This copy already has its setup files:

- [A place for tasks](agents/issue-tracker.md): local Markdown files.
- [Task labels](agents/triage-labels.md).
- [Shared terms and doc rules](agents/domain.md).

You can start here without running setup again. Run
`setup-matt-pocock-skills` when you need to choose a different tracker or
change those rules. Do not replace an app's current tracker with a second one.

## Use this with an app you have

Ask a developer to follow [the app guide](app-setup.md). Merge the kit into
the app with care. Keep the app's current rules and skills. Check the skill
names for conflicts. Restart the AI session after adding the files.

Then choose the real React parts, add the design rules, and plan 1 flow.
The kit cannot fill those choices in for your team.

## Check the files

Run `python3 scripts/check_workspace.py` from this repo.
Claude entries are already built. You only need to run
`python3 scripts/sync_claude_skills.py --write` after changing shared skill
names or descriptions. It updates entry files inside this repo only.

The paths and invocation settings follow the
[Claude skills guide](https://code.claude.com/docs/en/skills) and
[shared instruction guide](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools).
