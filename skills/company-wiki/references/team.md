# Team

How everyone at the company gets the wiki. Each person gets a small skill, `company-wiki-reader`, that tells their assistant to read the wiki before it answers a question about the company, and to report a wrong page. It can't change the wiki or the setup. The admin keeps the full skill.

## 1. Build the team's skill

Run this with the values from `company/setup.md`:

```text
python <skill>/scripts/wiki.py reader --name "<wiki name>" --company-name "<company name>" --home "<home tool>" --index "<index link>" --report <doc|comment|admin> --corrections "<corrections doc link>" --admin "<admin name>" --out <your outputs folder>/company-wiki-reader.zip
```

Leave out `--corrections` unless reports go to the corrections doc, and `--home` when the wiki is in Google Drive. Name the file `company-wiki-reader.zip` for an owner to upload for the whole company. Name it `company-wiki-reader.skill` when you hand it to one person in Claude, so it shows a Save skill button. Read the script's output, and check it lists the link you gave.

**Done when** the file is built.

## 2. Share the wiki

Check that the wiki folder is open to everyone at the company to read, as Commenter where the tool has that role, and the corrections doc to edit when it's used. When it isn't, give the admin the steps for their tool, one per line. For Google Drive: right-click the folder, Share, then under General access pick the company and the role.

**Done when** everyone at the company can open the wiki's index.

## 3. Roll it out

Give the admin the steps for their app and plan, one per line.

- **Claude, Team or Enterprise plan, as an owner.** Organization settings, then Plugins & skills. On the Policy tab, check that code execution and Skills are on. Then upload the file. It shows for every member under Customize, then Skills, and loads in Claude Code when they sign in with their Claude account. Help page: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
- **ChatGPT, Business or Enterprise plan.** Upload the file under Plugins, then Skills, then Create, then Upload from your computer. Then open the skill's menu, choose Share, and share it with the workspace. An admin may need to allow sharing first, under Permissions & roles. On Enterprise, an admin can install it for everyone so it's used without each person adding it. Help page: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- **No admin plan, or a small team.** Send the file to each person, with the install steps from [company-folder.md](company-folder.md#save-it) and the name `company-wiki-reader` in place of `company-wiki`.
- **Coding agents.** Unzip the file into the person's skills folder: `~/.claude/skills/` for Claude Code, and `~/.agents/skills/` for Codex, Cursor and OpenCode.

Each person also connects Google Drive, or the wiki's home, once in their own app. On a Team, Business or Enterprise plan, an owner may need to turn that connector on for the company first.

The admin gets the team's skill too when it goes to everyone. That's fine: both skills answer the same way, and the reader hands any wiki work to the full skill when it's there.

**Done when** the admin has rolled it out, or has the file and the steps.

## 4. Try it

Ask the admin to start a new chat, or ask a teammate, and ask a question the pilot pages answer, such as "What does a typical contract cost?" A good answer names and links the wiki pages it used. Save "Team rollout: done {date}" in `company/setup.md`.

When the wiki moves or the corrections doc changes, build the team's skill again and roll the new file out the same way.
