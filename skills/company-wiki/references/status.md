# Status

For the admin, in a chat: how the wiki is doing, what's waiting for them, and changes to the setup.

## 1. Show how it's doing

Read the log and the ledger, then reply with:

- **Health.** The last run, when it ran and its result, and the next one. Any missed runs, tools that stopped working, or sources that failed three times. When no scheduled run has happened since the last "Setup saved" entry, say so, and offer to start one now as setup's step 10 does.
- **Since you last asked**, or the last seven days the first time. Sources read, pages created and changed, and up to five changed pages as links.
- **Backfill.** Done, or how many files are left and about how many runs that takes at the current pace.
- **Waiting for you.** How many held changes, drafts and setup suggestions there are.

**Done when** the admin has the summary.

## 2. Held changes and drafts

Show each held change: the page, the change, its source and why it was held. For a draft, show what it changes on the page in a few lines. Ask: "Apply these {n} changes?" Options: "Apply all", "Go through them one by one", "Not now".

Apply each yes by the page rules. Copy a draft's text into its page, or move a new page into place, then remove the draft. Mark each entry in the log "Applied {date}" or "Declined {date}". A declined change stays out, so add its reason under Notes in `company/setup.md` when the admin gives one that should hold.

**Done when** every held change and draft has a yes, a no or a "not now".

## 3. Setup suggestions

Show each suggestion with the file and the line it would add or change. Ask: "Add these to your setup?" Options: "Add all", "Go through them one by one", "Not now". Save each yes in `company/` as [company-folder.md](company-folder.md#save-it) says, and in a chat app share the packed file to save. After the save, add a "Setup saved" entry to the log. Mark each entry in the log "Added {date}" or "Declined {date}".

**Done when** every suggestion has a yes, a no or a "not now".

## 4. Changes to the setup

For a change such as "add the Sales folder", "check Meeting notes every hour" or "pause the backfill", redo only the step of [setup.md](setup.md) it belongs to, then save. When the change touches a schedule, change the scheduled task too, as [schedules.md](schedules.md) says. In a chat app, the next run sees the change once the person saves the new copy.
