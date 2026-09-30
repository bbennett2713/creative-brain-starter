# Creative Brain Starter

You don't need more AI ads. You need an AI that knows your brand well enough to plan and make good ones.

This folder, opened in Claude Code, becomes a **creative brain** for your brand: a lab assistant that learns your offer, your customers, your ad account and your taste, then plans your ads as experiments and builds them from your real photos and your customers' real words. You stay the senior scientist. It drafts, you decide, and every correction you make is written down so you never have to make it twice.

- **It learns before it makes.** Your product, your reviews, and the tests you've already run come first.
- **It plans before it builds.** Every batch is an experiment with a hypothesis and a success measure, so win or lose, you learn something.
- **It never fakes anything.** No AI-generated product images. No made-up reviews or claims. Every word traces back to your customers or your brand.
- **It grows.** The folder remembers every correction, every result and every rule.

The ads are the chocolate. The brain is the carrot.

## Quickstart

1. **Get Claude Code.** You need a paid Claude plan. The easiest way is the Claude desktop app (claude.com/download), which has a Code tab. Or install it in the terminal: https://claude.com/claude-code
2. **Get this folder.** Click the green **Code** button above, then **Download ZIP**, and unzip it somewhere you'll find it.
3. **Open the folder in Claude Code and type `start`.**
   - Desktop app: open the Code tab, choose this folder.
   - Terminal: `cd` into the folder, run `claude`, then type `start`.

That's it. Claude does the technical parts (installing the image renderer, reading exports, pulling from your website) and walks you through the rest, one step at a time. You can stop anytime; type `start` again and it picks up where you left off.

## The road

Eight checkpoints, the way you'd train a new lab assistant. Each one hands you something useful right away, and each one ends with a decision only you can make.

| | Checkpoint | You give | You get back |
|---|---|---|---|
| 1 | **Syllabus day** | Your website, brand files, reviews (it can pull most of this itself) | A brand card, a product teardown, your customer's words, and 10 headlines they already wrote |
| 2 | **First day of labs** | The ad results you already look at (skip if you haven't run ads yet) | The story of your account, the six questions answered, and the question your next test should answer |
| 3 | **Outside reading** | The people you trust about ads | A skim of what they're saying, and how they'd read your account |
| 4 | **Assignments** | A yes to a weekly check-in (optional) | Reports that run on their own, which you grade |
| 5 | **Lab project** | Photos, and ads you admire | A small test, graded A to F in rounds, until it makes ads that look like you |
| 6 | **Final project** | Your pick of lane, and your prediction | A creative roadmap and a one-page experiment plan |
| 7 | **Build the experiment** | A yes on the ad list | 4 to 6 ads, square and tall, every word sourced |
| 8 | **Second semester** | Your results, after the test runs | What you learned, and the next experiment planned |

Then 6, 7, 8 again, with a smarter brain each time. You can read any lesson in the `road/` folder.

Handy commands inside Claude Code: `start` (pick up where you left off), `/results` (I have new numbers), `/grade` (correct something it made).

## What's in the folder

- `brain/`: what it knows. Your rules, what's off limits, your account's story, your roadmap, what worked. Edit it anytime.
- `road/`: the eight lessons, in plain English.
- `brand/`, `photos/`, `customer/`, `references/`, `results/`, `reading/`: where your material goes. Drag things in, messy is fine.
- `output/`: your brand card, lab tests and ad batches.
- `templates/`: a branded ad and a native (looks-like-a-post) ad, the patterns every ad follows.
- `scripts/`: the renderer (HTML to PNG) and a check that every quote is word for word.

## Your stuff stays yours

Everything lives in this folder on your computer. Nothing is posted, uploaded or changed in your ad account. If you put your copy on GitHub, keep it private: the `.gitignore` keeps your photos, reviews, results and brand files out, but `brain/` holds what it learned about your business.

## Credits

Built by Ben Bennett at Smart Marketer, for the talk "AI Creative Systems" at Acquire 2026.

## License

MIT. See `LICENSE`.
