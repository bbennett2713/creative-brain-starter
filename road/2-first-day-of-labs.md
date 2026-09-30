# Checkpoint 2: First day of labs

**The idea.** Your brain should learn from the tests you already ran before it makes its own. You give it the same numbers you look at, it tells you the story of your account, and you correct it. It will get things wrong at first. That's the point: every correction you make is written down, and next time it reads the account the way you would.

**Only memories, no file?** Take them. Write each result as they said it, marked `from memory`; never turn "maybe 3x" into a number you use. Set `Founder-checked: yes (from memory)`, and ask for the one screenshot that would settle the biggest claim.

**No ads yet?** Write `No results yet` at the top of `brain/account-story.md`. Still ask questions 5 and 6 below (what convinces someone to buy, what the next ad should be) and write their answers there. Tell them the rest comes back after their first test.

---

## Step 1: Get the numbers they already look at (into `results/`)

- Ask for a Meta Ads Manager export at the **ad level**, last 30 to 90 days, with: Ad name, Starts, Amount spent, Purchases (or their main result), Purchase value or ROAS, Impressions, Link clicks, and 3-second video plays if they run video. Screenshots work too. If they don't know how: Ads Manager, the Ads tab, pick the date range, then Export (the arrow icon), "Export table data", CSV.
- **Ads that send people to Amazon or another marketplace:** Meta can't see those sales. Ask for the Amazon Attribution (or marketplace) export for the same dates; clicks come from Meta, sales from there.
- A second export broken down **by week** helps you see what's fading. Optional.
- They drop it in `results/` or paste it. If they have a thumbnail or screenshot of their top ads, even better: numbers without the ad are half the story.

## Step 2: Check the file before you read it (your job, quietly)

Do this with a short script, then tell them in two lines what you found.

- **The real date range.** Read it from the "Reporting starts/ends" columns, not the file name.
- **One ad, many rows.** The same ad often runs in several ad sets, and duplicates get names like "... - Copy", "... - Copy 2" or a trailing ID. Strip those endings, then add rows with the same name together before judging. Say how many you merged.
- **A minimum before judging.** Count purchases, not dollars. Under about 3 purchases, an ad goes in "not enough spend yet", however good the ROAS looks. From about 3 it's a hint; around 10 it's a real read.
- **Flag what's different:** sale or promo ads, catalog and product-feed ads (not designed creative), and any ad that ran for only part of the period. Every row shows the same Reporting dates, so use the "Starts" column if they added it, or a date in the campaign or ad name, and otherwise ask: "Did any of these launch partway through, or during a launch, sale or email push?"
- **Say what the file can't tell you:** fading without weekly data, new vs returning customers, landing page effects.

## Step 3: The interview (their answer first, then yours)

Ask these one at a time. **Write their answer down before you show yours.** This is how the brain learns how they think.

1. What's winning right now?
2. What's fatiguing (was strong, now slipping)?
3. What's showing promise (good early numbers, small spend)?
4. What didn't get enough spend to judge?
5. What do you think convinces someone to buy? (Then check it against `customer/voice.md` and `brand/product.md`.)
6. What should the next ad be?

## Step 4: Your read, in the same six buckets

Show your read next to theirs. Mark where you agree and where you don't, and why.

**Guardrails (never break):**
- **Spend is the signal, when ads ran side by side.** The ad getting the spend is the one Meta's system proved. If an ad ran alone or was the only one switched on, its spend was the founder's choice, not proof. A small ad with a high return is a candidate, not a winner.
- **Judge each ad by its job.** An attention ad is compared with other attention ads (hook rate, click-through). A closer is compared with other closers (cost per purchase). Never pass or fail an ad on raw ROAS.
- **Never tell them to cut, pause or move money away from the ad carrying the account.** Feed it new versions instead.
- **No budget advice at all.** This folder makes creative. Say what to make next, not where to spend. If they ask "should I kill it?" or "how much should I spend?", say it's their call, then say what the numbers show (which ad is carrying the account) and what a fair read needs (about 10 purchases per version). Never turn that into a dollar figure.
- **One period is a hint.** Write findings as hypotheses with their evidence, never as rules.
- **Look at the ads, not only the numbers.** What does the winning ad actually say and show? Which customer theme, which product benefit, functional or emotional?

## Step 5: Correct it and keep it

- Ask: "What did I get wrong?" Expect them to know things the file doesn't (a promo, a stock-out, a creator who posted).
- Save everything to `brain/account-story.md`: the date range, their six answers, your six answers, what they corrected, and the hypotheses worth testing.
- **Every correction about how to read their account** ("that ad always spikes on payday", "we judge the prospecting campaign on cost per click") goes under "How to read my account" in `brain/house-rules.md`, so they never say it twice.
- If they have their own top ads, note them in `brain/what-worked.md` under "Ads that got the spend", with what they had in common.
- **Hand back:** "Your account in five lines": what's carrying you, what's slipping, what to feed, what needs a fair test, and **the question the next batch should answer**.

**Done when:** `brain/account-story.md` says `Founder-checked: yes` (or `No results yet`).

**Coming back later:** each time they bring a new export, run this again. The interview gets shorter as the brain gets it right. When the brain starts saying things like "you used to read it this way, but the numbers say something else", that's the brain earning its keep. They are still the judge of what's true.
