# Install the company wiki

These steps are for the AI assistant a person asked to "install this for me". A person can follow them by hand too. Installing takes a minute. Setup follows straight after, in the same conversation, and takes about 30 to 45 minutes.

1. **Work out where you're running.** Done when you know which section below is yours.
2. **Install the skill.** Done when the skill's `SKILL.md` is where your app will load it, or you've unzipped it in your working folder to run setup from.
3. **Run setup now.** Done when setup has started, in this conversation.

## 1. Work out where you're running

| You are | Follow |
|---|---|
| A coding agent with a terminal, such as Claude Code, Codex, Cursor or OpenCode | [Coding agents](#coding-agents) |
| Claude, in a chat, the desktop app or Cowork | [Claude](#claude) |
| ChatGPT | [ChatGPT](#chatgpt) |
| Any other assistant | [Anything else](#anything-else) |

## 2. Install the skill

### Coding agents

1. Run `node --version`. With Node.js 22.20 or later, install for every project on this computer:

   ```
   npx skills add https://github.com/TrellaceTeam/company-llm-wiki -g -y
   ```

   When the person gave you a link to a branch or a fork, use their link.
2. Without Node.js 22.20, download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip), unzip it, and copy the `company-wiki` folder into your skills folder: `~/.claude/skills/` for Claude Code, and `~/.agents/skills/` for Codex, Cursor and OpenCode.
3. Find the installed `SKILL.md` and note its folder. That's `<skill>` in the skill's steps.

### Claude

You can't add a skill to the person's account yourself. You can hand them a file to save, and Claude shows a Save skill button on skill files it shares. Run setup first, so that file already holds their setup. We haven't tested this route end to end yet.

1. Code execution must be on. If you can't run code, ask the person to turn on "Code execution and file creation" under Settings, then Capabilities. On a Team or Enterprise plan, an owner may need to allow it and allow skills.
2. Download the skill into your working folder and unzip it:

   ```
   curl -fsSL -o company-wiki.zip https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip
   ```

   When the download is blocked, ask the person to download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip) and drop it into this chat.
3. Run setup from the unzipped `company-wiki` folder. Near the end it packs the skill with the person's setup inside as `company-wiki.skill`, for them to save. Scheduled runs use that saved copy.

### ChatGPT

Skill uploads work on ChatGPT Business, Enterprise, Healthcare and Edu. We haven't tested this route yet.

1. Ask the person whether they see a Skills tab under Plugins. Without it, follow [Anything else](#anything-else).
2. Ask them to download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip) and attach it here. Unzip it in your Python tool.
3. Run setup from the unzipped `company-wiki` folder. Near the end it packs the skill with their setup inside as `company-wiki.zip`, for them to upload under Plugins, then Skills, then Create, then Upload from your computer.

### Anything else

An assistant that can load a skill, reach the company's files and run on a schedule can follow this skill too. We haven't tried any beyond the ones above. Without skills or schedules, the person can still use the wiki once it exists, but someone has to set it up and run it from one of the apps above.

## 3. Run setup now

Read `SKILL.md` in the installed or unzipped folder, then follow its `references/setup.md` in this conversation. Don't wait for a new session. Start with one line, such as "Installed. Setup takes about 30 minutes, one question at a time." Then look around, as setup's step 1 says, and ask the first question.

## Update it later

The person can ask: "Update the company wiki from https://github.com/TrellaceTeam/company-llm-wiki and keep my setup."

- **Coding agents.** Copy the skill's `company/` folder somewhere safe, install again as above, then copy `company/` back into the new skill folder. Check that `company/setup.md` is there.
- **Chat apps.** Copy the installed skill's `company/` folder to your working folder, get and unzip the new zip as above, and run `python company-wiki/scripts/wiki.py pack --company <the copied company folder> --out <your outputs folder>/company-wiki.skill`. Use `company-wiki.zip` as the name outside Claude. Share the file to save in place of the old one, and rebuild the team's skill too, as `references/team.md` says.
