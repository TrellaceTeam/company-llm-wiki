# Homes

The home is where the wiki's pages live. Google Drive is the default, and this file has full instructions for it. For any other tool, setup writes the instructions itself and the self-test checks them. Either way the result is `company/home.md`, which every mode reads before it writes a page.

## What a home needs

A tool can hold the wiki when you can do each of these through the person's connected tools:

| Need | Why |
|---|---|
| Create a page inside a folder or under a parent page | Pages sit in the folder plan |
| Keep headings, italics, lists, tables and links on a page | The page format needs them |
| Change a page in place and keep its link | Pages link to each other, and a new link breaks every old one |
| Find a page by its title | Ingest checks for an existing page before it makes one |
| Move a page and keep its link | Tidy reshapes folders as the wiki grows |
| Add a row to a table and read it back | The ledger records each source as it's done |
| See and set who can open a folder | The team reads the wiki, and the system folder stays private |
| Keep each page's past versions | The admin can see and undo any change |

## The self-test

Setup runs it once the home's frame exists: the wiki folder, its index, the system folder, the log and the ledger. Run each check, report one line per check to the person, and save the date and result of each under Self-test in `company/home.md`.

1. **Create.** Make a test page named "Wiki test" in the wiki folder, with a heading, a line in italics, a numbered list, a two-column table and a link to the wiki's index.
2. **Read it back.** Open the page. The heading, italics, list, table and link all came through. Your tools can show text that looks right to you and wrong to a person, such as raw Markdown, so also ask the admin to open the page in their browser and click its link.
3. **Change it in place.** Change one line, then open the page by its old link. The link still works and shows the change.
4. **Find it.** Search for "Wiki test" and find the page. Some tools' search takes a while to pick up a new page. When yours does, note it in `company/home.md`, and find pages through the indexes and folder listings first.
5. **Move it.** Move the page into one of the wiki's folders, and open it by its old link. Then leave a "Wiki test" page in the system folder for the run check below, by moving this one there or creating a new one there.
6. **Ledger.** Add a row to the ledger with "test" as its Source, and read it back.
7. **Sharing.** The wiki folder is open to everyone at the company, and the system folder only to the admin. When your tools can't see or set sharing, give the admin the steps for their tool, one per line, and save "confirmed by {admin} on {date}" as the result.
8. **Comments**, only when people will report corrections by commenting. Add a comment to the test page and read it back.
9. **No clicks.** Note whether any write above stopped for an approval or an Allow click. A scheduled run can't click, so when one did, give the person the setting that lets it run without asking, from [schedules.md](schedules.md#when-a-test-run-fails), and test that write again.

When a check fails, use the fallback the home's section below gives. When there's none, tell the person what failed and the setting or permission that would fix it. Stay on this step until each check passes, has a fallback, or the person confirms the result by hand.

## The run check

The first run after setup, or after a change to the setup, runs this short check, since a scheduled run can have fewer permissions than a chat. Open the "Wiki test" page in the system folder, or create it there when it's gone. Change its last line to the date and time, and open it by its link. Then set the ledger's test row to the same date and time. When any of this stops to ask or fails, log "Couldn't run: {what failed}" and stop.

## Google Drive

### Layout

- **The wiki folder**, named by the person, "Company Wiki" by default. Share it with everyone at the company as Commenter, so people can read and comment but not edit. It holds:
  - **Index**, a Google Doc. The front page: two sentences on how to use the wiki, a line such as "Last updated 16 October 2026. Updates every night.", then one line per folder with its link, what it holds and how many pages.
  - **One folder per fixed folder** in `company/structure.md`, and one per suggested folder below it. Each holds a Google Doc named "{Folder} index", with one line per page: its title as a link, then its question.
  - **Pages**, one Google Doc each, in the folder the placement rules choose.
  - **Corrections**, a Google Doc, when people report corrections there. Share this one Doc with everyone at the company as Editor. Start it with one line: "Found a wrong page? Ask your assistant to report it, or add a line here: the page, what's wrong and how you know."
- **The system folder**, named "{wiki name} system", in the admin's own My Drive and shared with no one. It holds:
  - **Wiki log**, a Google Doc. At the top, the Running line while a run is writing, then a "Held for {admin}" section and a "Setup suggestions" section, then one entry per run, newest first.
  - **Wiki ledger**, a Google Sheet with these columns: Source, File, Link, File ID, Last changed, Read on, Pages, Status, Note. [sources.md](sources.md#the-queue) lists the Status values.
  - **Drafts**, a folder, when every change waits as a draft.
  - **Wiki test**, the page the self-test leaves for the run check.

Keep the system folder out of shared drives, since every member of a shared drive can open every folder in it. Put the wiki folder where everyone can reach it. In a shared drive, each person's access comes from their role in that drive, so people with a Contributor role or higher can edit pages there. To keep pages comment-only, use a folder in the admin's My Drive shared with the whole company as Commenter, or a shared drive where the company has the Commenter role.

In ChatGPT, Google Drive's newer view reached My Drive and files shared directly with you but not shared drives, as of September 2026. When the team uses ChatGPT, run the self-test from ChatGPT, and use a My Drive folder when a shared drive fails.

### Writing a page

- **Create** a page as a Google Doc in its folder, titled with the subject. Make it a Google Doc, never a Word or Markdown file, since every assistant's Drive tool reads Google Docs. When your tools can only upload a file, upload Markdown with conversion to Google Docs turned on.
- **Format** the title as Title or Heading 1, the question in italics, the status line as plain text, sections as Heading 2 and 3, and Sources as a numbered list. Use Docs tables for tables.
- **Change** a page in place, in the same Doc. Never delete a page and create it again, since its link changes and every link to it breaks. When your tools can only replace a Doc's whole text, replace it in the same Doc.
- **Fallback** when no tool changes a Doc in place: create the new version as a new Doc, move the old one to the system folder, then update every link to it, on pages and in indexes, in the same run. Note the fallback in `company/home.md`, since it costs more each run.

### Links

Link to a page with its Doc link, using the page's title as the link text. Link to a source with its Drive file link. A page's link stays the same through edits and moves, so links between pages last.

### Finding pages

Search Drive for the title inside the wiki folder, and read the folder index the placement rules point to. To find every page built from one source, read that source's Pages cell in the ledger, then search the wiki folder for the source's title.

### Moving and merging

- **Move** a page by moving its Doc to the new folder. The link keeps working. Update both folder indexes.
- **Merge** two pages that answer the same question. Carry every unique fact, with its citation and its Sources entry, into the page you keep. Then point every link to the other page at the kept one, replace the other page's text with one line, "Merged into {kept page link} on {date}.", and take it off its folder index. Tidy trashes these one-line pages once no page links to them.

### Log and ledger

Write a log entry for every run, newest first:

```text
16 October 2026, 02:07, run
Checked Meeting notes, Customer calls and #ops.
Read 6 sources. Created Pricing and Kestrel Components. Changed 4 pages: Priya Raman, Sales pipeline, Ashgrove Plastics, Customers index.
Held 1: Jordan Ellis, see Held. Skipped 1: Offer letter draft, shared with 2 people. Failed 0.
Queue: 0 due, 412 backfill.
Review: Fixed Pricing: the pilot price is $10,000, not $12,000.
```

The Checked line names every source whose changes the run queued, so the next run can tell when each one was last checked. Give each file one ledger row, and update it as the file moves through the queue. Last changed is the file's own last-changed time when you queued or read it. A failed row keeps a count in Note, such as "failed 2 times: the file is too long to open", so the next run tries it again.

Setup and status add a "Setup saved" entry each time they save the person's copy, so the next run knows to run the run check.

### Known limits

- Assistants read the text of Docs, Sheets, Slides, PDFs and Office files. Images inside them are skipped.
- Live editing of Docs in Claude was in beta as of October 2026. The self-test shows what works for this account.
- On Team, Business and Enterprise plans, the plan's owner decides whether connector actions such as moving or trashing a file can run without a click. A scheduled run that stops to ask fails. [schedules.md](schedules.md#when-a-test-run-fails) has the fix.

## Anywhere else

For another tool, write `company/home.md` yourself from the template below. Use the Google Drive section as the model. Each part there has a job, so find what does that job in this tool. A folder is whatever groups pages, such as a parent page in Notion, a page tree in Confluence or a folder in a SharePoint library. The ledger is whatever table the tool keeps, such as a Notion database, a Microsoft List or an Excel sheet. The system folder is anything only the admin can open.

Work out each part from the tool's connected actions, the hints here and the tool's own help pages. Then run the self-test. Every check that passes is a line you've proved, and every fallback you write is one the next run can use.

Some connectors only search and read until an admin turns on writing, often with a consent step in the tool's own admin center. When this one can't create or change a page, tell the person straight away. Give them the steps to turn on writing first. When that isn't possible, offer a home whose connector can write and that everyone at the company can already open. Sources can stay where they are.

A few things differ between tools, so check each one:

- **Moves.** In some tools a page moved to another site, library or space gets a new link. Keep the system folder somewhere a move into it is never needed, and when a move does change a link, fix every link to the page in the same run, as the change fallback does.
- **Search.** When the tool's search reaches beyond the wiki and the source folders, such as a whole company's files, filter every result by its folder or path before you open it, and write the filter in `company/home.md`.
- **Roles.** Not every tool has a comment-only role. Give the team read access to the wiki, and point corrections to the corrections doc when people can't comment without edit rights.
- **Limits.** Some connectors cap how many writes a person can make in a while. When a run hits a cap, lower the Run size and note the cap in `company/home.md`.
- **Pages that hold pages.** In some tools, such as Notion, a folder is a page whose body holds its sub-pages. Change those pages line by line, never by replacing their whole text.
- **History.** Some plans keep past versions for a limited time. Note how long in `company/home.md`.

Hints for common tools:

- **Notion.** A top page named after the wiki, in a teamspace everyone can open, as the index. Fixed folders as child pages, and wiki pages as their sub-pages. The system folder as a private page of the admin's, holding the log as a page and the ledger as a database with the ledger's columns. Corrections as a page everyone can edit. Page history is built in, for a time that depends on the plan.
- **SharePoint or OneDrive.** A folder in a site library everyone can open. Pages as Word documents, with subfolders as the folder plan. The system folder in the same library, with access for the admin only, so a move keeps its link. The ledger as an Excel sheet, or a Microsoft List when the connector can write to one. Version history is built in.
- **Confluence.** A space everyone can open, with the page tree as the folder plan. The ledger as a table on one page. Page history is built in.
- **A folder on this computer**, in a coding agent only. Pages as Markdown files, with relative links. Git keeps the history when the person wants it.

## Home template

```markdown
# Home

How to work in this wiki's home, {tool}. Written by setup on {date}. Edit any line, or ask for a change in plain words.

## Layout
- Wiki: {where it is, and how folders and pages nest}
- Index: {where the front page is}
- System: {where the log, the ledger and drafts are}

## Writing a page
- Create: {how}
- Format: {how the title, question, status line, sections and Sources look}
- Change: {how to change a page in place}
- Fallback: {what to do when a change in place fails | none needed}

## Links
- {how to link a page and a source}

## Finding pages
- {how to search by title, and how to find the pages one source built}

## Moving and merging
- {how}

## Log and ledger
- {where each lives and its format}

## Sharing
- Wiki: {who, at what access}
- Corrections: {who, at what access | not used}
- System: {admin only}

## Self-test
- {date}: Create, passed
- {date}: Change in place, {passed | failed, fallback used}

## Known limits
- {such as file types the tool can't read}
```
