# Company LLM Wiki

A company wiki your AI assistant writes from the files your team already keeps, and that every Claude or ChatGPT on your team reads before it answers. Every claim links to the file it came from. It lives where you work: Google Drive by default, or SharePoint, Notion, Confluence or another tool your assistant can reach.

> [!NOTE]
> This is a beta. The method behind it runs our own firm, and this version, which sets itself up inside Claude or ChatGPT, is new. Please tell us how it went in an [issue](https://github.com/TrellaceTeam/company-llm-wiki/issues), good or bad.

## Install it

Paste this into Claude, ChatGPT or a coding agent such as Claude Code or Codex:

```text
Install this for me: https://github.com/TrellaceTeam/company-llm-wiki
```

Your assistant follows [INSTALL.md](INSTALL.md). It installs the skill, a set of steps your assistant follows, then walks you through setup in the same chat.

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

Setup takes about 30 to 45 minutes, and most of it is a pilot on ten of your files. The assistant asks one question at a time.

1. **Your tools.** It checks what's connected, such as Google Drive, and shows you how to connect anything missing.
2. **Your sources.** You name the folders the wiki learns from. It checks each one is shared with the whole company, and asks how often to check it and what to skip, such as HR files.
3. **Your wiki's home.** By default, a new Google Drive folder shared with everyone. For SharePoint, Notion, Confluence or another tool, the assistant works out how the wiki's folders, pages and ledger map onto it, and writes its own instructions. Either way it runs a self-test there: it makes a test page, edits it, links it, finds it, moves it and writes to the ledger.
4. **Your folders.** It proposes a few fixed top folders, such as Customers, People and Product, and you decide how much freedom it has below them.
5. **How changes go live.** Straight in, held for you when they're about people or conflicts, or held as drafts. You pick when it tells you about a run, and how people report a wrong page.
6. **A pilot.** It writes pages from ten recent files and shows you three claims to check. Your feedback becomes house rules. Then you pick how to fill in the rest of your history: a little each run, all at once, or on its own schedule until it's done.
7. **The schedule.** It sets up the scheduled runs in your app.
8. **Your team.** It builds a small skill for everyone else, with your wiki's link inside, and shows you how to give it to the whole company.
9. **Your own copy.** It saves your setup inside your copy of the skill. In Claude or ChatGPT, it hands you one file to save. Then it starts one scheduled run and reads its log, to check it works with nobody watching.

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
| [INSTALL.md](INSTALL.md) | How an assistant, or you, installs it in each app |
| [examples/fennick/](examples/fennick/README.md) | A fictional company's saved setup and two of its pages |

## From Trellace

[Trellace](https://www.trellace.com/?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki) works with B2B founders in the messy middle, after product-market fit and before a repeatable go-to-market team. That's usually $1 million to $10 million in annual revenue. We run our firm on this wiki, then rebuilt it so any team can run it with the tools they already have. We publish the methods we use because GTM needs more open source projects.

- **Founders.** If something here is close to what you're working through, [book a 30-minute GTM Sparring Session](https://www.trellace.com/contact?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki).
- **Investors.** Most of our work starts with an introduction from a fund. If a company you back comes to mind, [make an introduction](https://www.trellace.com/contact?utm_source=github&utm_medium=readme&utm_campaign=company-llm-wiki).
- **More free tools.** See everything we've published at [github.com/TrellaceTeam](https://github.com/TrellaceTeam).

## License

[MIT](LICENSE). Use it, change it and ship it, including for commercial work.
