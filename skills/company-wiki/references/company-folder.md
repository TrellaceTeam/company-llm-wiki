# Company folder

What setup saves, where it lives and how to save it in each app. The company folder makes this the company's own copy of the skill, so every run starts with no questions.

## What it holds

The folder is `company/`, inside this skill's folder, beside `SKILL.md`. It holds five files:

- `company/setup.md`. The app, the sources and how often to check each one, the wiki's home and its links, how changes go live, reports, corrections, the schedules, the backfill, the team rollout, setup progress and standing notes.
- `company/home.md`. How to work in the wiki's home, with the date and result of each self-test check. [homes.md](homes.md) says how to write it.
- `company/structure.md`. The folder plan: fixed folders, suggested folders and how much freedom you have below them.
- `company/style.md`. House rules from the pilot and later feedback, such as how much detail a page holds and what to leave out.
- `company/glossary.md`. Names that notes and transcripts get wrong, and the right spelling.

The company folder never holds source text, page text, passwords or keys. It holds links to folders and documents, and the names of the people who run the wiki, so share a copy only with people who should see those.

## Where to look for it

1. `company/setup.md` in this skill's folder.
2. `company/setup.md` in your working folder, in a chat where setup ran and the person hasn't installed the new copy yet.
3. `company-wiki-setup/setup.md` in the project folder, where setup saves when the skill's folder is read-only.
4. Files the person attached or added to the project.

## Save it

| Where the skill runs | How to save |
|---|---|
| A coding agent on the person's computer, such as Claude Code, Codex, Cursor or OpenCode | Write the files into `company/` in this skill's folder, and read one back to check that it saved. When the folder is read-only, write them to `company-wiki-setup/` in the project folder, and tell the person where they are. When the folder sits inside a git repository, run `git status --short --untracked-files=all`. When a `company/` file shows, ask whether to add `**/skills/company-wiki/company/` to `.gitignore`, so the setup isn't committed. Leave it committed when a cloud routine runs the wiki from a private repository, since the routine loads the skill from there |
| Claude, in a chat, the desktop app or Cowork | The skill's folder here is a copy that's gone when the chat ends. Write the changed files to a `company` folder in your working folder, then run `python <skill>/scripts/wiki.py pack --company <that folder> --out <your outputs folder>/company-wiki.skill` and share the file. `pack` keeps the company files already in the skill and lays yours over them |
| ChatGPT or another chat app that runs Python | Run the same `pack` command with `--out <your outputs folder>/company-wiki.zip` and share the file |
| An app that can't run code | Give the files as text, and ask the person to add them to a project. Scheduled runs need a saved copy, so suggest Claude, ChatGPT or a coding agent for those |

When you share a packed file, tell the person how to install it, one step per line:

- **Claude.** "Click Save skill on this file. It installs the company wiki as your own copy, with your setup inside. Then open Customize, then Skills, and if two company-wiki skills show, delete the older one." When no Save skill button shows: "Rename the file to company-wiki.zip. Open Customize, then Skills. If an older company-wiki skill is there, delete it first. Click +, then Create skill, then Upload a skill, and pick this file."
- **ChatGPT.** "Open Plugins, then the Skills tab. If an older company-wiki skill is there, delete it first. Choose Create, then Upload from your computer, and pick this file."

A scheduled task uses the copy saved on the person's account, so a run sees a change only once the new copy is saved. Have them replace the old copy, so there's only one.

`pack` names every entry `company-wiki/...`, the shape these apps accept. Only the skill's own files and the company's `.md` files go in, so an export or a key file beside the skill never ships. It lists what it left out.

## Keeping it current

- Change `company/` during setup, during [status](status.md), and at the end of a run in a coding agent. Never change it halfway through writing a page.
- Write standing rules, such as "check Meeting notes every night", never one run's dates.
- Add a note only when the person says it should hold, or when review reports the same pattern twice.
- In a chat app, pack after every change and offer the file in one line: "Save this file to keep the change."
- After every save of the person's copy, add a "Setup saved" entry to the log, so the next run runs its check.
- In a scheduled run in a chat app, you can't save. Add the lesson under "Setup suggestions" in the log, with the file and the line you'd change.

## Setup template

```markdown
# Company wiki setup

Saved by the company-wiki skill on {date}. Edit any line, or ask for a change in plain words.

## Setup progress
- Tools: {done {date} | not yet}
- Sources: {done {date} | not yet}
- Home and self-test: {done {date} | not yet}
- Folder plan: {done {date} | not yet}
- Changes, reports and corrections: {done {date} | not yet}
- Pilot and pace: {done {date} | not yet}
- Schedules: {done {date} | not yet}
- Team rollout: {done {date} | waiting, by choice | not yet}
- Saved copy: {done {date} | not yet}

## Tools
- Company: {name}. Admin: {name}, {an owner or admin of the plan | not an owner or admin}
- App: {Claude | ChatGPT | Claude Code | Codex | other}, plan {Team | Business | Pro | not known}
- Connectors: {Google Drive, Slack, Gmail}
- Helpers: {subagents | none}
- Schedules: {how this app runs scheduled tasks, from schedules.md}

## Sources
- {name}: {link}, through {connector}. List changes by: {how, such as files changed since a time | database rows edited since a time}. Check: {every run | once a week | only when asked}. Skip: {subfolders, kinds of file, words in titles | nothing}. Shared with {everyone at the company}, checked {date}
- Skip everywhere: {such as HR, payroll, legal and anything marked confidential}

## Home
- Home: {Google Drive | Notion | other}, see home.md
- Wiki folder: {link}, shared with {everyone at the company} as {Commenter | Viewer | read only}
- Index: {link}
- System folder: {link}, in {the admin's My Drive | where home.md says}, shared with no one
- Log: {link}
- Ledger: {link}
- Corrections: {link | none}

## Changes
- Approval: {live | hold some: {people pages, merges and deletions, conflicts} | draft first}
- Reports: {only when something needs the admin | after every run | never}, by {the app's run results | email to {address} | Slack to {channel}}
- Corrections: {the corrections doc | comments on the page | tell the admin}
- Admin: {name}

## Runs
- Run: {cadence, time and time zone}, model {name | the app's default}, task "{task name}"
- Tidy: {cadence, time and time zone | only when asked}, model {the strongest available}, task "{task name}"
- Backfill: {a little each run, {n} files | all at once | its own schedule, {cadence, time and time zone}, task "{task name}" | not wanted}
- Run size: up to {25} sources a run
- Review: after every {10} sources

## Backfill
- Pilot: {n} sources on {date}. Feedback is in style.md
- Scope: {every source folder | the folders named}, files last changed before {date}
- Status: {in progress, see the ledger | done {date}}

## Team
- Reader: company-wiki-reader, built {date}, rolled out by {an organization skill | a workspace share | a file sent to each person}

## Notes
- {date}: {a standing rule the person gave, in their words}
```

## Structure template

```markdown
# Structure

How the wiki is organized. The admin owns this file. The agent reads it before it places a page.

## Fixed
- {Customers}: {one page or folder per customer, prospect or lost deal, with its people, deals and history}

## Suggested
- {Customers/Ashgrove Plastics}: {the largest open deal, with many sources}

## Flexibility
- Below the fixed folders: {use your judgment | only the folders listed | ask first}
```

## Style and glossary templates

```markdown
# Style

House rules for this wiki, from the pilot and later feedback. They add to the page rules in SKILL.md.

- {date}: {the rule, in the person's words where you can}
```

```markdown
# Glossary

Names that notes and transcripts get wrong. Write the right name on every page.

| Heard or written as | The right name | Who or what it is |
|---|---|---|
| {Fenwick} | {Fennick} | {the company} |
```
