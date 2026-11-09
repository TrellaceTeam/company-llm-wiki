# Company LLM Wiki

A company wiki your AI assistant writes from the files your team already keeps, and that every Claude or ChatGPT on your team reads before it answers. Every claim links to the file it came from. It lives where you work: Google Drive by default, or SharePoint, Notion, Confluence or another tool your assistant can reach.

> [!NOTE]
> This is a beta. The method behind it runs our own firm, and this version, which sets itself up inside Claude or ChatGPT, is new. Please tell us how it went in an [issue](https://github.com/TrellaceTeam/company-llm-wiki/issues), good or bad.

## Install it

Paste this into Claude, ChatGPT or a coding agent such as Claude Code or Codex:

```text
Set up this skill and install it for me: https://github.com/TrellaceTeam/company-llm-wiki
```

Your assistant follows [INSTALL.md](INSTALL.md). It gets the skill, a set of steps your assistant follows, sets it up with you, then installs your own copy with your setup inside, so you install it once.

If you can, connect Google Drive, or wherever your team keeps its files, to your assistant before you paste the line. In Claude, that's Customize, then Connectors. In ChatGPT, it's Plugins. Some apps see a new connection only in a new chat. When yours does, your assistant tells you what to click and gives you a line to paste there, and your setup picks up where it stopped.

We built this method for our own firm. It has compiled more than 1,500 of our meeting notes, calls, decisions and docs into more than 1,000 cited pages, and our agents read it before they answer anything about a client. This repository is a clean port of it, with none of our data.

## Why a wiki

Ask an assistant what to do about a customer, and it suggests the thing you tried last month. The answer is in a call note, a Slack thread or a doc nobody opens.

Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) idea fixes this for one person. An agent reads each source once and writes it into wiki pages that build on each other, so knowledge adds up between questions. Searching your documents for each question, the usual approach, starts from raw chunks every time.

This is the version for a team that lives in shared folders and chat assistants:

- **It reads what you already keep.** You point it at folders, and it never changes a file in them.
- **It reads only what everyone can open.** It checks each folder's sharing, so a page never tells someone what's in a file they can't see.
- **Every claim is cited.** Each page lists its sources, and a teammate checks a claim by opening one link.
- **Contradictions stay visible.** When two sources disagree, the page keeps both under "Open questions", and a person decides.
- **It runs on its own.** After setup it checks your folders on the schedule you pick, and it stays quiet unless something needs you.
- **Your whole team gets it.** Everyone's Claude or ChatGPT reads the wiki first, and anyone can report a wrong page by telling their assistant.

## Setup

Setup takes about 30 to 45 minutes, and your part is a few of them. The assistant does the rest.

1. **It looks around.** It checks what's connected, such as Google Drive, and shows you how to connect anything missing.
2. **It comes back with one plan.** Which folders to learn from, with each one's file count and sharing, and what to skip, such as HR files. Where the wiki lives, by default a new Google Drive folder shared with everyone. The top folders, such as Customers, People and Product, picked from a sample of your files. How changes go live, the schedule, how long your history takes to fill in, and how your team gets it.
3. **You say yes**, or change any line first.
4. **It builds everything.** The wiki's folders, a private log and ledger, and a self-test that makes a test page, edits it, links it, finds it and moves it. For SharePoint, Notion, Confluence or another tool, it works out how the wiki maps onto it and writes its own instructions.
5. **It writes pages from ten recent files.** You check three claims against their sources. Anything you'd change becomes a house rule.
6. **It schedules the runs**, and builds a small skill for everyone else, with your wiki's link inside.
7. **You save your own copy.** In Claude or ChatGPT, it hands you one file to save. Then it starts one scheduled run and reads its log, to check it works with nobody watching, and starts filling in your history.

## Then it runs on its own

- **Each run** fixes reported pages, queues new and changed files from the folders that are due, and reads them one at a time, rereading its own work every ten files. It keeps a log and a ledger in a private folder only you can open, so a run that stops partway loses nothing.
- **Each tidy** reviews the recent changes on the strongest model your app offers, merges duplicate pages, settles contradictions, checks that every citation and link works, and checks that no run was missed.
- **You hear from it** only when you asked to, such as when a change waits for your yes or a folder's sharing got narrower.
- **Your team asks their own assistant**, which answers from the wiki with links to the pages. When someone says a page is wrong, their assistant files a correction, and the next run checks it against the sources.
- **To change anything**, ask in plain words: "Add the Sales folder", "Check Meeting notes every hour", "Show me the held changes".

## What a page looks like

Here's part of [the pricing page](examples/fennick/pages/pricing.md) from the example, a fictional company called Fennick Software:

```text
Pricing

How is Fennick priced, and what does a typical contract cost?

Updated 8 October 2026 from 10 sources.

Fennick is priced per plant and billed annually. New customers who sign from
1 September 2026 pay $40,000 a year for the first plant and $20,000 a year for
each additional plant. Until then the prices were $36,000 and $18,000 [1].

Sources
1. Decision: new list prices from 1 September 2026, 18 August 2026, Priya Raman
```

[The example](examples/fennick/README.md) also has the setup the skill saved for Fennick.

## Where it runs

| App | Scheduled runs | Giving it to the team |
|---|---|---|
| Claude, on the web, desktop or Cowork | Scheduled tasks, in Anthropic's cloud, on any paid plan | An owner adds the team's skill for everyone on a Team or Enterprise plan |
| ChatGPT | Scheduled tasks, or Team Tasks on a shared account on Enterprise | Share the team's skill with the workspace on Business or Enterprise |
| Claude Code or Codex | Scheduled tasks on your computer, or your computer's scheduler | Each person adds the team's skill to their skills folder |

Scheduled runs use your plan's usage. In our own runs a file took one to two minutes, plus a review every ten files.

## What it touches

- **Your sources, read-only.** It lists and reads files in the folders you named. It never edits, moves, shares or deletes them.
- **The wiki folder.** It creates and edits pages there. Your team can read and comment.
- **A private system folder.** The log and the ledger, shared only with you.
- **Your setup.** Your copy of the skill holds a `company` folder with your folder links, choices and house rules. It holds no file contents and no keys.
- **Private things stay out.** It skips what you tell it to, and keeps email addresses, phone numbers, pay, health and personal matters off every page.
- **Keys.** It never asks for a password or key in chat.

## Limits

- **It's a beta.** The method is the one we run, and this version is new. The routes for Claude, ChatGPT and coding agents come from each app's own documentation, checked in October 2026, and apps change their menus often.
- **Models make mistakes.** The review every ten files catches many, and a person still opens a citation before relying on a claim.
- **Apps can block silent runs.** Some plans make a scheduled run stop and ask before it writes. Setup's test run finds this, and [schedules.md](skills/company-wiki/references/schedules.md#when-a-test-run-fails) has the fix for each app.
- **Homes beyond Google Drive are untried.** The method stays the same everywhere, and the self-test proves each step in your tool. When a tool can't do a step, such as a connector that only reads, setup tells you and suggests another home.
- **ChatGPT and shared drives.** As of September 2026, ChatGPT's newer Google Drive view didn't reach shared drives. Setup's self-test checks, and it can use a folder in your own Drive shared with everyone instead.
- **It knows only what's in your folders.** A number from your CRM is as current as the last doc that mentions it.
- **Everything it reads goes to your AI provider**, under your plan's terms.

## What's in this repository

| Path | What it's for |
|---|---|
| [skills/company-wiki/](skills/company-wiki/SKILL.md) | The skill: its modes, setup, the page rules, notes for Google Drive and other tools, schedules, the team's skill and the `wiki.py` script |
| [INSTALL.md](INSTALL.md) | How an assistant, or you, sets it up and installs it in each app |
| [examples/fennick/](examples/fennick/README.md) | A fictional company's saved setup and two of its pages |

## From Trellace

[Trellace](https://www.trellace.com/?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki) works with B2B startups to support their growth. We run our firm on this wiki, then rebuilt it so any team can run it with the tools they already have. We publish the methods we use because GTM needs more open source projects.

- **Founders.** If something here is close to what you're working through, [book a 30-minute GTM Sparring Session](https://www.trellace.com/contact?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki).
- **Investors.** Most of our work starts with an introduction from a fund. If a company you back comes to mind, [make an introduction](https://www.trellace.com/contact?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki).
- **Newsletter.** Last Week in GTM is our weekly newsletter for B2B founders and their investors, out every Tuesday. [Sign up or read past issues](https://www.trellace.com/insights?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki).
- **More free tools.** See everything we've published at [github.com/TrellaceTeam](https://github.com/TrellaceTeam).

## License

[MIT](LICENSE). Use it, change it and ship it, including for commercial work.
