# Schedules

How each app runs the wiki on a schedule, and how to set it up. We checked these against each app's help pages in October 2026, and apps change their menus often. When a step here doesn't match what the person sees, follow the app's own help page and update `company/setup.md` with what worked.

## Prompts

Use these word for word, so every run finds the skill and asks nothing. In ChatGPT and Codex, start each one with `$company-wiki `, or pick the skill in the task's settings where the app offers that.

| Task | Prompt |
|---|---|
| Run | Use the company-wiki skill to do a scheduled run of the company wiki. Follow its saved setup, ask no questions, and end with the run's log entry. |
| Tidy | Use the company-wiki skill to do a maintenance run: tidy the company wiki. Follow its saved setup, ask no questions, and end with the tidy's log entry. |
| Backfill | Use the company-wiki skill to do a backfill run of the company wiki. Follow its saved setup, ask no questions, and end with the run's log entry. |

Name the tasks "Company wiki run", "Company wiki tidy" and "Company wiki backfill", and save the names in `company/setup.md`.

## Claude

Scheduled tasks run in Anthropic's cloud on every paid plan, so they keep running when the computer is off. They use the connectors, skills and plugins on the person's account, so the saved copy of this skill must be installed first.

1. Ask Claude in this chat to create the task, with its name, prompt, cadence and model. Claude shows the task, and the person clicks Schedule. You can also type `/schedule` in a Cowork task.
2. Or set it up by hand: Scheduled in the left sidebar, then New task, then Set up manually. Fill in the name, the prompt, the approval mode, the frequency and the model. Pick the approval mode that runs without stopping to ask. Leave the folder empty, since a local folder makes the task run only on that computer.

On a Team plan, cloud runs are on unless an owner turned them off. On an Enterprise plan, an owner has to turn on "Run Cowork in the cloud" in Organization settings, then Cowork, and give the person that capability. Help page: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork

## ChatGPT

Scheduled tasks run from ChatGPT on the web and in the desktop app, and they can use skills and plugins. A task on the web keeps no files between runs, which suits the wiki, since its state lives in the home.

1. Ask ChatGPT in this chat to create a standalone scheduled task, with its name, prompt, cadence and model. A standalone task starts a new chat for each run.
2. Or set it up by hand: Scheduled, then New task. Paste the prompt, which starts with `$company-wiki`, and pick the cadence and the model.

On an Enterprise plan, a Team Task runs on the team's service account and the workspace's connections, so the wiki doesn't depend on one person's account. Set it up from Scheduled, then New task, with the Team switch on, once an admin has allowed Team Tasks and shared a Google Drive connection with the team. Help page: https://learn.chatgpt.com/docs/automations

## Claude Code

- **On this computer.** In the desktop app's Code tab, open Routines, then New routine, and choose Local. It runs while the computer is on.
- **In the cloud.** A cloud routine clones a GitHub repository on every run and loads the skills committed there. It suits a team that keeps the skill, with its `company/` folder, in a private repository. Choose Cloud in the same place, or type `/schedule` in the terminal.

Help page: https://code.claude.com/docs/en/routines

## Codex

In the ChatGPT desktop app, open Scheduled and create a standalone task in the project where the skill is installed, with the prompt starting `$company-wiki`. It runs while the computer is on and the app is open. Pick a sandbox setting that lets the run use the connected tools. Help page: https://learn.chatgpt.com/docs/automations

## Anything else

The computer's own scheduler can start a coding agent in the folder where the skill is installed, such as Task Scheduler on Windows or cron on a Mac or Linux. The command is `claude -p "<the prompt>"` for Claude Code, or `codex exec "<the prompt>"` for Codex. It runs while the computer is on and the person is signed in to the agent. A run with nobody watching can't approve a tool, so first allow the wiki's connector tools in the agent's settings, such as Claude Code's permission rules or Codex's sandbox and approval settings.

## Pause, change or stop a task

Open Scheduled in the app, then the task. Each app lets the person pause, edit, run now or delete it there. After a change to the setup's schedule, change the task to match.

## When a test run fails

A task that finished without an error may still have done nothing, so always read the log entry.

| What the run shows | The fix |
|---|---|
| It stopped to ask before writing or sending a report | In Claude, set the task's approval mode to run without asking, and set the write tools of the wiki's home, such as Google Drive's, to always allow under Customize, then Connectors. On a Team or Enterprise plan, an owner may first need to let members allow actions without asking, in Organization settings, then Connectors. In ChatGPT, allow the plugin's actions in its settings when the app offers that. When an app has no such setting, it can't write unattended yet, so schedule the wiki from another app in this file, or ask for "update the wiki now" in a chat |
| It couldn't find the skill | The saved copy isn't installed on this account, or the prompt doesn't name the skill. Save it as [company-folder.md](company-folder.md#save-it) says, and use the prompt above |
| It couldn't reach Drive or another tool | The connector isn't connected on this account, or scheduled tasks can't use it. Connect it, then run again. For a Team Task, ask the admin to share the connection with the team |
| It ran out of usage or time | Lower the Run size in `company/setup.md`, or run more often with fewer sources each time |
