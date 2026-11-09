# Install the company wiki

These steps are for the AI assistant a person asked to set up and install this skill, or only to install it. Most people who paste the link aren't technical. They copied one line from the README and expect you to do the rest. A person can follow these steps by hand too.

Setup comes before the install. You look at what's connected, propose the whole setup as one plan, and build it after one yes. The copy the person installs then already holds their setup, so they install it once. Setup takes about 30 to 45 minutes, and most of that is you writing the first pages.

1. **Work out where you're running.** Done when you know which section below is yours.
2. **Get the skill.** Done when you can read its `SKILL.md`. In a coding agent, that's the installed copy.
3. **Set it up.** Done when setup is finished, or the person has a line to paste in a new chat.
4. **Install their copy.** Done when the copy with their setup is where their app loads it. Setup's step 7 does this.

Whenever the person has to open a new chat, such as after connecting Google Drive, give them the line to paste there, as [setup.md](skills/company-wiki/references/setup.md#moving-to-a-new-chat) says. Then stop. The new chat goes on from that line.

## 1. Work out where you're running

| You are | Follow |
|---|---|
| A coding agent with a terminal, such as Claude Code, Codex, Cursor or OpenCode | [Coding agents](#coding-agents) |
| Claude, in a chat, the desktop app or Cowork | [Claude](#claude) |
| ChatGPT | [ChatGPT](#chatgpt) |
| Any other assistant | [Anything else](#anything-else) |

## 2. Get the skill

When the company-wiki skill is already installed here with a finished setup, use that copy, skip to the mode the person asked for in its `SKILL.md`, and leave the rest of this file.

### Coding agents

1. Run `node --version`. With Node.js 22.20 or later, install for every project on this computer:

   ```
   npx skills add https://github.com/TrellaceTeam/company-llm-wiki -g -y
   ```

   When the person gave you a link to a branch or a fork, use their link.
2. Without Node.js 22.20, download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip), unzip it, and copy the `company-wiki` folder into your skills folder: `~/.claude/skills/` for Claude Code, and `~/.agents/skills/` for Codex, Cursor and OpenCode.
3. Find the installed `SKILL.md` and note its folder. That's `<skill>` in the skill's steps.

Setup saves into this installed copy, so step 4 has nothing left to do.

### Claude

You can't add a skill to the person's account yourself. Claude shows a Save skill button on skill files it shares, so you set up a copy here and hand it over at the end, with the setup inside. We haven't tested this route end to end yet.

1. **Check that you can run code.** When you can't, ask the person to turn on "Code execution and file creation" under Settings, then Capabilities. On a Team or Enterprise plan, an owner may need to allow it and allow skills. When Google Drive, or wherever the team keeps its files, isn't connected yet, ask them to connect it too, under Customize, then Connectors. Then try again here. When this chat still can't run code, move to a new chat, as [setup.md](skills/company-wiki/references/setup.md#moving-to-a-new-chat) says. When code has to stay off, follow [Anything else](#anything-else).
2. **Download the skill** into your working folder and unzip it:

   ```
   curl -fsSL -o company-wiki.zip https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip
   ```

   When the download is blocked, ask the person to download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip) and drop it into this chat.

### ChatGPT

Skill uploads work on ChatGPT Business, Enterprise, Healthcare and Edu. We haven't tested this route yet.

1. Ask the person whether they see Plugins in the sidebar, with a Skills tab. Without it, follow [Anything else](#anything-else).
2. When no file tool such as Google Drive shows in this chat, have them connect it first, as setup's step 1 says, so they attach the zip only once.
3. Ask them to download [company-wiki.zip](https://github.com/TrellaceTeam/company-llm-wiki/releases/latest/download/company-wiki.zip) and attach it here. Unzip it in your Python tool.

### Anything else

An assistant that can load a skill, reach the company's files and run on a schedule can follow this skill too. We haven't tried any beyond the ones above. Without skills or schedules, the person can still use the wiki once it exists, but someone has to set it up and run it from one of the apps above.

## 3. Set it up

Skip this step and step 4 when you followed Anything else and can't load the skill.

Read `SKILL.md` in the installed or unzipped folder, then follow its `references/setup.md` now, in this conversation. Start with one line, such as "Got it. I'll look at what's connected and come back with a plan." Then look around, as setup's step 1 says. When the person's message links a "Setup in progress" doc, start with "Picking up your setup at step {n}." and carry on from there.

## 4. Install their copy

Setup's step 7 saves the company folder the way [company-folder.md](skills/company-wiki/references/company-folder.md#save-it) says for this app.

- **Coding agents.** It saves into the installed copy.
- **Chat apps.** It packs the skill with the person's setup inside, hands them the file with the steps to install it, and waits for them to say it's saved, since scheduled runs use that copy.

When the person wants to stop before setup ends, give them a line to paste when they come back, as [setup.md](skills/company-wiki/references/setup.md#moving-to-a-new-chat) says. They install once, when setup is done.

## Update it later

The person can ask: "Update the company wiki from https://github.com/TrellaceTeam/company-llm-wiki and keep my setup."

- **Coding agents.** Copy the skill's `company/` folder somewhere safe, install again as above, then copy `company/` back into the new skill folder. Check that `company/setup.md` is there.
- **Chat apps.** Copy the installed skill's `company/` folder to your working folder, get and unzip the new zip as above, and run `python company-wiki/scripts/wiki.py pack --company <the copied company folder> --out <your outputs folder>/company-wiki.skill`. Use `company-wiki.zip` as the name outside Claude. Share the file to save in place of the old one, and rebuild the team's skill too, as `references/team.md` says.
