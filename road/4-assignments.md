# Checkpoint 4: Assignments

**The idea.** Check-ins that run on their own. A full account read, a mini one, or a quick update: which ads are taking off, new winners emerging, winners fading, what the experts said this week. They do double duty: they keep the founder updated, and every time the founder corrects one, they keep the brain updated too. And they use the plan the founder already pays for, in the hours they aren't working.

**Optional.** "Not now" is a fine answer. Offer it again after their first test has run.

---

## Step 1: Pick the assignment

Offer these, and let them choose one to start (one is plenty):

- **Weekly account check:** new winners, winners fading, ads that need more spend to judge, what to feed next. Needs a fresh export in `results/` each week, or a connected ad account (see below).
- **Weekly outside skim:** checkpoint 3's skim, rerun on new posts.
- **Before-the-next-batch prep:** reread the brain, the last results and the skim, and draft the next plan card for them to react to.

Ask how they want it delivered: a file in `reports/`, a message, an email. Only offer what their setup actually supports.

## Step 2: Set it up (your job)

- **Scheduling:** check what scheduling their Claude setup actually offers (for example scheduled tasks in the Claude desktop app, or a `/schedule` command in Claude Code), and set it up with them if it exists. Don't promise a feature you can't see.
- **Cloud schedulers can't see this folder.** A cloud scheduler (like `/schedule` in Claude Code) runs on a copy of a GitHub repo, and `.gitignore` keeps `results/` out of git on purpose, so it can't see their exports. Don't set one up for an account check. A scheduler that runs on their own computer (for example a scheduled task in the Claude desktop app) can work.
- **If there's no local scheduler,** create a slash command instead (for example `.claude/commands/check-in.md`) so they type `/check-in` on Monday morning and get the same report.
- **Data:** a weekly account check needs fresh numbers. The simplest is a weekly export dropped into `results/`. If they want it automatic, say plainly that it needs an ad-account connection (an MCP connector or an API token for their ad platform). Help them set it up only if they want to, and **read-only**: this folder never changes their ads.
- Write what's scheduled, when, and how it's delivered to `brain/assignments.md`.

## Step 3: Grade the reports

Tell them: "Don't trust these blindly at first. Each report is a chance to check the brain's homework."

Every report ends with three verdict slots for anything it found. The founder picks one per finding, and you write it down:

- **"Yes, that's true."** It becomes a rule in `brain/house-rules.md` (or a line in `brain/account-story.md`).
- **"No, and here's why."** The why becomes a rule so it doesn't make that mistake again.
- **"Interesting, dig deeper."** It becomes an open question for the next check-in.

- **Hand back:** run the assignment once now, so they see the first report and grade it.

**Done when:** `brain/assignments.md` lists one assignment and its first report has been graded, or says `Not now`.
