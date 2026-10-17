# Sources

A source is a file the company already keeps, such as meeting notes, a call transcript, a decision, a plan or a spec. The wiki reads sources and never changes them.

## What a source tool needs

Any tool counts when you can do these four things through the person's connected tools:

1. **List** the files in a folder, with each file's ID, title and the time it last changed.
2. **Read** a file's text.
3. **Link** to a file, so a page's Sources list can open it.
4. **See sharing**, when the tool shows it. Without it, the admin confirms each folder is open to everyone at the company. The safest setup then connects the tool through an account that sees only what everyone at the company sees.

## The queue

The ledger is the queue. A row's Status says where each file stands:

| Status | Means |
|---|---|
| due | Changed since it was last read, waiting for a run |
| backfill | Part of the history, waiting for the backfill |
| read | Read at the Last changed time on its row |
| skipped | Left out, with the rule or reason in Note |
| failed | Couldn't be finished, with a count in Note |
| deleted | Gone from the source folders, and its claims removed |

A run first queues what changed, then works through the queue: every due row, oldest change first, then backfill rows when the pace says so. Rows it doesn't reach stay in the queue for the next run, so nothing is lost when a run stops at its size limit.

## Queueing what changed

A source is due when its "Check" setting says so: every run, once a week, or only when asked. Its last check is the newest log entry whose Checked line names it. A source with no check yet counts from the day setup ran, since older files belong to the backfill. For each due source:

1. **List what changed.** List the files changed since the source's last check, minus one day, so a file saved during the last run isn't missed. Include files in its subfolders unless its skip rules leave them out.
2. **Drop what's done.** Drop each file whose ledger row is read, with the same Last changed time.
3. **Apply the skip rules.** Mark files the source's rules or the "Skip everywhere" rules leave out as skipped, with the rule in Note.
4. **Check sharing.** When you can see a file's sharing and it's narrower than its folder's, mark it skipped and log it.
5. **Queue the rest.** Add a due row for each new file, or set an existing row to due with the new Last changed time.

Once every changed file of a source is queued, name the source on the run's Checked line, even if the run reads none of them.

A file moved into a source folder keeps its old Last changed time, so step 1 misses it. Tidy catches these, as [tidy.md](tidy.md) says.

## Reading each kind of file

- **Documents, notes and plans.** Read all of it, comments too when the tool shows them, since a comment often holds the latest decision.
- **Transcripts.** They mishear names and mix up speakers. [ingest.md](ingest.md#2-triage) says how to handle them. An AI summary beside a transcript is a lead, and the transcript wins where they differ.
- **Sheets.** Read the tabs that hold facts a teammate would look up, such as a price list or a hiring plan. A sheet of raw data, such as an export of every support ticket, earns a summary only when the person asks for one.
- **Slides.** Read the slide text and speaker notes. Images are skipped.
- **PDFs and Office files.** Read the text. A scan with no text can't be read, so log it as skipped.
- **Images, audio and video.** Skip them, and log them as skipped. A recording counts through its transcript.
- **Anything your tools can't open.** Try one file of each kind at setup's step 2, such as a OneNote notebook, which some connectors can't read. When a kind won't open, tell the person and offer to skip it, or to have someone export those files to Word or PDF, so they don't fail on every run.

## Notes for common tools

- **Google Drive.** Folders and shared drives. Meet transcripts and Gemini meeting notes are Docs, often in a "Meet Recordings" folder in the organizer's Drive. The organizer may need to move or share them into a source folder.
- **Notion.** A source is a page or a database, with everything under it. Sharing comes from the teamspace, but a page inside it can be locked to fewer people, and Notion's tools don't show sharing, so the admin confirms each source. List what changed by querying a database for rows edited since the last check. Notion AI meeting notes keep the transcript in a block below the summary, which some tools leave out unless asked, so check that a fetched note includes it.
- **SharePoint and OneDrive.** A source is a site library or a folder. Word, PowerPoint, Excel and PDF files read as text. A connector's search may cover every site the person can open, so filter results to the source folders.
- **Confluence.** A source is a space or a page tree.
- **Dropbox and Box.** A source is a folder.
- **Slack or Microsoft Teams.** A source is a channel everyone can join, read one day at a time. Each day with real content is one source, titled "#{channel}, {date}", with a link to the day's first message. In the ledger, its File is that title, its File ID is "{channel}:{date}" and its Last changed is the time of the day's last message. Skip private channels and direct messages.
- **Meeting recorders**, such as Fireflies, Fathom or Gong. Each meeting is one source. Read only meetings shared with the whole company, since a recorder holds every call its users record.
- **A coding agent's own tools.** With no connector, a tool's MCP server or its API works the same way. The person saves any key in a file such as `.env`. Never ask for a key in chat.
