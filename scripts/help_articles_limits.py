"""Help articles: how each AI tool's usage limits work.

Written from research on 2026-11-25 against each provider's own help center,
pricing page and docs. Providers change these often: when a fact changes, edit
it here and rebuild (scripts/build_help.py). Numbers appear only where the
provider publishes them.
"""

CHECKED = "Checked against each provider's own pages in November 2026. Providers change limits often, so their usage page is the final word."


def _foot():
    return f'<p class="help-note">{CHECKED}</p>'


LIMIT_ARTICLES = [
    # ── Claude ────────────────────────────────────────────────────────
    {
        "slug": "claude-usage-limits",
        "topic": "limits",
        "title": "How do Claude's usage limits work?",
        "seo_title": "Claude Usage Limits Explained: 5-Hour, Weekly and Fable",
        "summary": "Claude has a 5-hour session limit and a weekly limit, shared across chats, Claude Code and the desktop app. Max and Ultra also have a separate weekly Fable limit.",
        "keywords": "claude usage limits 5-hour 5 hour session weekly 7-day limit reset fable opus pro max ultra max 20x max 5x usage credits extra usage claude code shared how long",
        "legacy": ["claude-limits"],
        "common": "A 5-hour session limit and a weekly limit, shared by chats and Claude Code.",
        "body": """
<h2>The limits</h2>
<ul>
<li><strong>5-hour session.</strong> Starts with your first message and resets in full five hours later.</li>
<li><strong>Weekly limit, all models.</strong> Resets at a fixed day and time assigned to your account. It doesn't depend on when you started chatting or when you subscribed.</li>
<li><strong>Weekly Fable limit</strong> (Max and Ultra). Fable uses your limits faster than other models, and has its own weekly cap of up to half your weekly limit. On Pro, Fable runs on usage credits.</li>
</ul>
<p>Anthropic doesn't publish message counts. How far a limit goes depends on the model, how long the conversation is, the features you use and the effort level.</p>

<h2>By plan</h2>
<ul>
<li><strong>Free:</strong> limited usage every 5 hours and every week. No Claude Code.</li>
<li><strong>Pro ($20/month):</strong> more than Free. Includes Claude Code.</li>
<li><strong>Max ($100/month):</strong> 5× Pro, every 5 hours and every week.</li>
<li><strong>Ultra ($200/month):</strong> 10× Pro every week, and <strong>no 5-hour limit</strong> once your account is verified (it happens automatically). If Settings → Usage shows no “Current session” bar, you're verified.</li>
</ul>
<p>Plan names changed in late 2026: the old <strong>Max 20x</strong> is now <strong>Ultra</strong>, and <strong>Max 5x</strong> is now just <strong>Max</strong>.</p>

<h2>What shares a limit</h2>
<p>Chats on claude.ai, the desktop app, Claude Code and Claude Code in your editor all draw from the same limits. A long coding session can leave less room for chat, and the other way round.</p>

<h2>When you hit a limit</h2>
<ul>
<li>Wait for the reset, or upgrade (new limits apply right away).</li>
<li>Turn on <strong>usage credits</strong> (formerly “extra usage”) in Settings → Usage, and your work continues at API rates instead of stopping. You can set a monthly spending cap. <a href="/help/extra-usage-and-credits">More on usage credits</a>.</li>
<li>Claude Code gets a small wrap-up allowance so it can finish what it's doing.</li>
</ul>
<p>The monthly API credits included with Max and Ultra can't be used in the Claude apps or Claude Code.</p>

<h2>Where to check</h2>
<p>Settings → Usage on claude.ai, or <code>/usage</code> in Claude Code. <a href="/help/check-claude-usage">How to check your Claude usage</a>.</p>

<h2>In Tokenomics</h2>
<p>The 5-hour window is the inner ring and the weekly window the outer ring, each with a <a href="/help/pace-dot">pace dot</a>. On Ultra, you'll see only the weekly window, because there's no 5-hour limit to show. From the browser extension's next update (1.1.3), it also shows your separate Fable weekly limit, your plan (Pro, Max or Ultra), and your usage credits when they're on.</p>
""" + _foot(),
    },
    # ── ChatGPT ───────────────────────────────────────────────────────
    {
        "slug": "chatgpt-limits",
        "topic": "limits",
        "title": "How do ChatGPT's usage limits work?",
        "seo_title": "ChatGPT Usage Limits Explained: Plans, Thinking and Codex",
        "summary": "Everyday chat is unlimited on most plans, but Thinking, Pro models and tools like images and voice have their own limits. From December, Plus, Pro and Business share one allowance across ChatGPT and Codex.",
        "keywords": "chatgpt usage limits message cap limit reached thinking gpt pro weekly free go plus pro business team images voice deep research codex shared allowance december how many messages",
        "legacy": [],
        "common": "Chat is mostly unlimited; Thinking, Pro models and tools have their own limits.",
        "body": """
<h2>The limits</h2>
<ul>
<li><strong>Everyday chat:</strong> unlimited on Free and Go, subject to abuse safeguards.</li>
<li><strong>Tools:</strong> file uploads, image generation, voice and data analysis have separate limits, even on plans with unlimited chat.</li>
<li><strong>Thinking and Pro models:</strong> have their own caps. On Pro, the top model has a weekly limit. OpenAI no longer publishes message counts for these.</li>
</ul>
<p>When you reach a Thinking or Pro-model limit, ChatGPT often switches you to another model instead of stopping, so it's easy to miss.</p>

<h2>By plan</h2>
<ul>
<li><strong>Free and Go ($8/month):</strong> unlimited everyday chat; tools are limited. Go may include ads.</li>
<li><strong>Plus ($20/month):</strong> may have message caps, especially when demand is high.</li>
<li><strong>Pro ($100, $200 or $500/month):</strong> three tiers. “Unlimited” access is subject to abuse guardrails, and the top models have weekly limits.</li>
<li><strong>Business:</strong> seats use their included limits first, then the workspace's credit pool.</li>
</ul>

<h2>ChatGPT and Codex: one allowance from December</h2>
<p>Today, Codex has its own allowance, separate from chat. It's already shared with ChatGPT Work, ChatGPT for Excel and Workspace Agents. <strong>Starting in December 2026, Plus, Pro and Business plans share one allowance across ChatGPT and Codex</strong>, measured in tokens. Quick “Instant” chat replies don't count against it. Some people may see the change early. <a href="/help/codex-limits">How Codex limits work</a>.</p>

<h2>When you hit a limit</h2>
<p>Wait for the reset, switch models, upgrade, or (for the shared allowance) buy credits.</p>

<h2>Where to check</h2>
<p>Settings → Usage in ChatGPT shows remaining usage and reset times where OpenAI provides them.</p>

<h2>In Tokenomics</h2>
<p>ChatGPT doesn't report chat limits anywhere Tokenomics can read them. What chatgpt.com does report is your plan's <strong>Codex allowance</strong>, so from the browser extension's next update (1.1.3) that's what the ChatGPT meters show, labelled “Codex allowance”, with windows named by their real length. From December, that's the same allowance your ChatGPT use draws from on Plus, Pro and Business. If your plan looks wrong, see <a href="/help/chatgpt-plan">fixing the ChatGPT plan</a>.</p>
""" + _foot(),
    },
    # ── Codex ─────────────────────────────────────────────────────────
    {
        "slug": "codex-limits",
        "topic": "limits",
        "title": "How do Codex usage limits work?",
        "seo_title": "Codex Usage Limits Explained: 5-Hour and Weekly Windows",
        "summary": "Codex in a ChatGPT plan has its own allowance: 5-hour and weekly on Plus, weekly only on Pro, monthly on Go. Local tasks, cloud tasks and image generation all draw from it.",
        "keywords": "codex usage limits codex cli 5-hour weekly limit plus pro go business cloud tasks local messages image generation credits reset shared chatgpt status usage",
        "legacy": [],
        "common": "Its own allowance: 5-hour and weekly on Plus, weekly only on Pro.",
        "body": """
<h2>Windows by plan</h2>
<ul>
<li><strong>Plus and Business (Standard seats):</strong> a 5-hour allowance and a weekly allowance. The same usage counts against both, but they can reset at different times, so you can hit the 5-hour limit with plenty of the week left.</li>
<li><strong>Pro ($100, $200 or $500):</strong> weekly only. Pro has no 5-hour limit.</li>
<li><strong>Go:</strong> a monthly allowance.</li>
<li><strong>Free and Go</strong> can use Codex in the desktop app; Codex cloud needs Plus or higher.</li>
</ul>

<h2>What counts</h2>
<ul>
<li>Local messages (CLI, editor, desktop app) and cloud tasks share the allowance. Cloud tasks tend to use more.</li>
<li>Image generation counts too, at about 3–5× the rate.</li>
<li>Code reviews run from GitHub (tagging <code>@Codex</code>) are counted separately.</li>
<li>Sessions using an API key are billed at API rates, not from your plan.</li>
</ul>
<p>OpenAI publishes rough ranges, not fixed limits: on Plus, a 5-hour window ranges from a handful of messages on the largest models to a few thousand on the smallest.</p>

<h2>Codex and ChatGPT</h2>
<p>Codex already shares its allowance with ChatGPT Work, ChatGPT for Excel and Workspace Agents. From December 2026, Plus, Pro and Business plans share one allowance across ChatGPT chat and Codex too. <a href="/help/chatgpt-limits">How ChatGPT limits work</a>.</p>

<h2>When you hit a limit</h2>
<p>The current turn can usually finish. Then wait for the reset, switch to a smaller model, use a banked reset, buy credits (Plus and Pro), upgrade, or switch to an API key.</p>

<h2>Where to check</h2>
<p>Type <code>/status</code> in a Codex CLI session, or open chatgpt.com/codex/settings/usage.</p>

<h2>In Tokenomics</h2>
<p>The Mac app reads the limits Codex CLI writes to your Mac after each run, so the numbers update when you use Codex locally. Cloud tasks show up after your next local run. From the next update (2.10.5), windows are named by their real length, so Pro plans show a single Weekly window. <a href="/help/codex-numbers">Why Codex numbers sometimes don't change</a>.</p>
""" + _foot(),
    },
    # ── Gemini app ────────────────────────────────────────────────────
    {
        "slug": "gemini-limits",
        "topic": "limits",
        "title": "How do the Gemini app's usage limits work?",
        "seo_title": "Gemini Usage Limits Explained: 5-Hour Refresh and Weekly Cap",
        "summary": "The Gemini app's limit refreshes every 5 hours until you reach a weekly cap. It's based on compute, so images, video, Deep Research and the Pro model use it faster.",
        "keywords": "gemini usage limits gemini app 5 hour refresh weekly limit compute ai plus ai pro ai ultra free video image deep research deep think flash lite ai credits",
        "legacy": [],
        "common": "A 5-hour refresh up to a weekly cap, based on compute.",
        "body": """
<h2>How it works</h2>
<p>Since May 2026, the Gemini app measures compute rather than counting prompts. Your limit <strong>refreshes every 5 hours until you reach your weekly limit</strong>. Google doesn't publish the numbers for either.</p>
<p>What a request costs depends on how complex it is, the features it uses and how long the chat has run. Image, video and music generation, Deep Research, the Pro model, extended thinking and Deep Think use it faster; video costs the most. A single complex prompt can take a noticeable bite out of a 5-hour block.</p>

<h2>By plan</h2>
<ul>
<li><strong>Free:</strong> the standard limit. Uses Auto model routing by default.</li>
<li><strong>Google AI Plus:</strong> 2× standard.</li>
<li><strong>Google AI Pro:</strong> 4× standard.</li>
<li><strong>Google AI Ultra:</strong> 5× or 20× the <em>AI Pro</em> limit, depending on the subscription.</li>
</ul>

<h2>When you hit the limit</h2>
<p>Keep chatting with the lighter Flash-Lite model, wait for the refresh, upgrade, or (AI Pro and Ultra) buy AI credits at API prices.</p>

<h2>What's separate</h2>
<p>The Gemini API and AI Studio have their own per-minute and per-day limits, per project. Work and school accounts follow their own rules. <a href="/help/gemini-cli-numbers">Gemini CLI</a> is separate again.</p>

<h2>Where to check</h2>
<p>In gemini.google.com, open Settings → Usage Limits.</p>

<h2>In Tokenomics</h2>
<p>The browser extension reads Google's own usage numbers and shows the 5-hour window and the weekly window, each with its real reset time. Google doesn't report your plan, so you pick it once. <a href="/help/two-meters">Why there are two meters</a>.</p>
""" + _foot(),
    },
    # ── Copilot ───────────────────────────────────────────────────────
    {
        "slug": "copilot-limits",
        "topic": "limits",
        "title": "How do GitHub Copilot's usage limits work?",
        "seo_title": "GitHub Copilot Limits Explained: AI Credits vs Premium Requests",
        "summary": "Since June 2026, monthly Copilot plans use AI credits (1 credit = $0.01): Pro gets 1,500 a month, Pro+ 7,000, Max 20,000. Annual Pro and Pro+ plans still use premium requests. Everything resets on the 1st.",
        "keywords": "github copilot limits ai credits premium requests monthly allowance pro pro+ max business enterprise free completions multiplier reset 1st utc budget overage",
        "legacy": [],
        "common": "AI credits since June 2026; annual plans still use premium requests.",
        "body": """
<h2>AI credits (most plans, since June 2026)</h2>
<p>Copilot now charges by tokens at each model's published rate, in <strong>AI credits</strong> (1 credit = $0.01). Each month includes:</p>
<ul>
<li><strong>Pro ($10):</strong> 1,500 credits (1,000 base + 500 flex)</li>
<li><strong>Pro+ ($39):</strong> 7,000 (3,900 + 3,100)</li>
<li><strong>Max ($100):</strong> 20,000 (10,000 + 10,000)</li>
<li><strong>Business ($19/seat):</strong> 1,900 per user, pooled across the organization</li>
<li><strong>Enterprise ($39/seat):</strong> 3,900 per user, pooled</li>
<li><strong>Free:</strong> 2,000 code completions a month, plus limited chat and agent use</li>
</ul>
<p>Base credits are used first, then flex credits (which GitHub may adjust over time). Chat, the CLI, the cloud agent and third-party agents use credits. <strong>Code completions don't</strong> on paid plans. Using auto model selection is 10% cheaper.</p>

<h2>Premium requests (annual Pro and Pro+ only)</h2>
<p>If you pay yearly for Pro or Pro+, you keep the older model until your plan ends: 300 premium requests a month on Pro, 1,500 on Pro+. Each model costs a multiple of a request (a small model can be a fraction, a big one many requests).</p>

<h2>What shares the allowance</h2>
<p>One allowance covers Copilot in your editor, on github.com and in the CLI. On Business and Enterprise, it's pooled across everyone.</p>

<h2>Reset</h2>
<p>Midnight UTC on the 1st of each month, whatever day you subscribed. Nothing rolls over.</p>

<h2>When you run out</h2>
<p>Individuals can upgrade or set a budget for extra usage; the old fallback to a cheaper model is gone. On Business and Enterprise, extra usage is on by default unless an admin turns it off.</p>

<h2>Where to check</h2>
<p>github.com/settings/billing → AI usage, or your Copilot settings → Usage. In VS Code, click the Copilot icon in the status bar. <a href="/help/check-copilot-usage">More ways to check</a>.</p>

<h2>In Tokenomics</h2>
<p>Tokenomics reads Copilot through the GitHub CLI's sign-in. Free plans show Chat and Completions bars. From the next update (2.10.5), paid plans show an <strong>AI Credits</strong> bar with how much of your monthly allowance you've used; seats without a set allowance (common on Business and Enterprise) show credits used; annual plans keep Premium Requests. <a href="/help/copilot-meters">What the Copilot meters show</a>.</p>
""" + _foot(),
    },
    # ── Cursor ────────────────────────────────────────────────────────
    {
        "slug": "cursor-limits",
        "topic": "limits",
        "title": "How do Cursor's usage limits work?",
        "seo_title": "Cursor Usage Limits Explained: X Subscription and Legacy Plans",
        "summary": "New Cursor customers are on The X Subscription: one weekly pool shared with Grok, covering Cursor's own models. Older plans (Pro, Pro+, Ultra) keep two monthly pools.",
        "keywords": "cursor usage limits x subscription plus premium super ultra pro pro+ legacy weekly pool monthly cursor models other models grok composer third-party claude gpt on-demand usage",
        "legacy": [],
        "common": "A weekly pool shared with Grok on new plans; monthly pools on older ones.",
        "body": """
<h2>The X Subscription (new customers)</h2>
<p>Cursor is now sold as part of <strong>The X Subscription</strong>, together with Grok and X:</p>
<ul>
<li><strong>Free</strong> (limited), <strong>Plus</strong> ($8), <strong>Premium</strong> ($30, 4× Plus), <strong>Super</strong> ($100, 15× Plus), <strong>Ultra</strong> ($200, 50× Plus). No absolute amounts are published.</li>
<li>One <strong>weekly</strong> pool covers Cursor's own models (Composer and Grok) across the editor, CLI, Cloud Agents and the Grok apps. Using Grok elsewhere draws from the same pool.</li>
<li>Third-party models such as Claude and GPT aren't included: on Premium and up they're paid from prepaid credit at API prices.</li>
</ul>
<p>At the limit, keep going on prepaid credit, wait for the weekly reset, or upgrade. Requests aren't downgraded in quality or speed. Check usage at grok.com/dashboard.</p>

<h2>Older plans (Hobby, Pro, Pro+, Ultra, Teams)</h2>
<p>These continue unless you switch. They have two <strong>monthly</strong> pools that reset with your billing date: “Cursor Models” and “Other Models” (third-party models at API price). Pro and up include unlimited Tab completions. On-demand usage past the pools is off by default for individuals and on by default for Teams. Check usage at cursor.com/dashboard.</p>

<h2>In Tokenomics</h2>
<p>The Mac app reads Cursor's local sign-in. Older plans show your usage for the billing cycle. From the next update (2.10.5), The X Subscription shows one <strong>Weekly Usage</strong> bar with its reset time.</p>
""" + _foot(),
    },
    # ── Grok ──────────────────────────────────────────────────────────
    {
        "slug": "grok-limits",
        "topic": "limits",
        "title": "How do Grok's usage limits work?",
        "seo_title": "Grok Usage Limits Explained: Weekly Pool and Free Allowance",
        "summary": "Paid Grok plans share one weekly usage pool across chat, voice, images, video and Cursor. The free tier has its own allowance on a separate schedule.",
        "keywords": "grok usage limits weekly pool supergrok x premium x subscription plus premium super ultra free daily extra usage credits reset grok tab on x cursor",
        "legacy": [],
        "common": "One weekly pool on paid plans; a separate allowance on Free.",
        "body": """
<h2>How it works</h2>
<p>Since June 2026, paid Grok plans have <strong>one shared weekly usage pool</strong> instead of separate limits for each feature. Chat, voice, image and video generation all draw from it, at different rates depending on the compute they need. It's shared across the Grok apps, the Grok tab on X and Cursor.</p>
<p>The pool resets every week on a schedule shown in Settings → Usage.</p>
<p>Guides that quote “N queries every 2 hours” or separate Think and DeepSearch caps describe the old system.</p>

<h2>Plans</h2>
<p>New customers get The X Subscription (since October 2026): <strong>Plus</strong> ($8), <strong>Premium</strong> ($30, 4× Plus), <strong>Super</strong> ($100, 15× Plus), <strong>Ultra</strong> ($200, 50× Plus). Older SuperGrok and X Premium plans continue unless you switch. xAI publishes only multiples, not actual amounts.</p>
<p>The <strong>free tier</strong> isn't part of the weekly pool. Free chat and voice have their own allowance that resets on its own schedule.</p>

<h2>When you hit the limit</h2>
<p>Paid features pause until the weekly reset, but you can buy Extra Usage Credits (web only, from $5, priced higher per action than included usage, expire after a year), turn on Auto Top Up, or upgrade. Free chat and voice keep working on their own allowance.</p>

<h2>Where to check</h2>
<p>Settings → Usage on grok.com or in the app. It shows the percentage used by product and when it resets.</p>

<h2>In Tokenomics</h2>
<p>On the free tier, the browser extension shows grok.com's query allowance. From the extension's next update (1.1.3), paid plans show the <strong>weekly pool</strong> percentage and when it resets, the same number as Settings → Usage.</p>
""" + _foot(),
    },
    # ── Perplexity ────────────────────────────────────────────────────
    {
        "slug": "perplexity-limits",
        "topic": "limits",
        "title": "How do Perplexity's usage limits work?",
        "seo_title": "Perplexity Limits Explained: Pro Searches, Research and Credits",
        "summary": "Pro Searches have a weekly limit on Pro and Max (3 a day on Free). Deep Research and file and app creation have separate monthly limits. Credits are only for Computer.",
        "keywords": "perplexity limits pro searches weekly deep research monthly labs file app creation credits computer free pro max reset best mode model choice",
        "legacy": [],
        "common": "Weekly Pro Searches, monthly Deep Research, and credits for Computer.",
        "body": """
<h2>The limits</h2>
<ul>
<li><strong>Pro Searches:</strong> 3 a day on Free; a weekly limit on Pro and Max (“average use” and “advanced use”). At the limit you still get basic searches.</li>
<li><strong>Deep Research:</strong> its own monthly limit, higher on Max. It recovers gradually over time rather than on your billing date, and hitting it doesn't stop other searches. Free gets 1 a month.</li>
<li><strong>File and app creation</strong> (formerly Labs): its own monthly limit on Pro and Max.</li>
<li><strong>Choosing a specific model</strong> counts against limits; “Best” mode has no quota.</li>
</ul>
<p>Perplexity doesn't publish the Pro or Max numbers. (Enterprise Pro gets 400 Pro Searches a week, for comparison.)</p>

<h2>Credits are separate</h2>
<p>Credits (100 = $1) pay for <strong>Computer</strong> tasks, not searches. Max includes 10,000 a month; Pro includes a weekly Computer allowance that resets 7 days after your first task. Monthly credits don't roll over.</p>

<h2>Where to check</h2>
<p>perplexity.ai/account/usage shows credits and Pro's weekly Computer meter.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows Pro Searches and Deep Research remaining. On Free, Pro Searches reset daily and Tokenomics counts down to it. Perplexity doesn't report reset times for Pro and Max, so from the extension's next update (1.1.3) those show what's left with no countdown, rather than a guess.</p>
""" + _foot(),
    },
    # ── Midjourney ────────────────────────────────────────────────────
    {
        "slug": "midjourney-fast-hours",
        "topic": "limits",
        "title": "How do Midjourney's Fast Hours work?",
        "seo_title": "Midjourney Fast Hours Explained: How to Track What’s Left",
        "summary": "Midjourney limits Fast GPU time, not images. Each plan gets Fast hours every month (3.3 on Basic up to 60 on Mega); Relax mode is unlimited on Standard and up and doesn't use them.",
        "keywords": "midjourney fast hours gpu time relax mode turbo basic standard pro mega how many images video extra gpu time reset rollover /info",
        "legacy": ["mj-fast-hours"],
        "common": "Fast GPU time each month; Relax mode doesn't use it.",
        "body": """
<h2>What's limited</h2>
<p>Midjourney counts <strong>GPU time</strong> while it's generating, not clock time or images. Roughly: an image prompt takes about a minute of Fast time, an upscale about 2 minutes, and a batch of four videos 8 minutes or more. Higher quality settings use 2× or 4×.</p>

<h2>Fast hours by plan (per month)</h2>
<ul>
<li><strong>Basic ($10):</strong> 3.3 hours (200 minutes). No Relax mode.</li>
<li><strong>Standard ($30):</strong> 15 hours, plus unlimited Relax for images.</li>
<li><strong>Pro ($60):</strong> 30 hours, plus unlimited Relax for images and SD video. Stealth mode.</li>
<li><strong>Mega ($120):</strong> 60 hours, same extras as Pro.</li>
</ul>

<h2>The three speeds</h2>
<ul>
<li><strong>Fast:</strong> uses your Fast hours.</li>
<li><strong>Relax:</strong> unlimited and free of Fast time, but queued (up to about 30 minutes, longer if you use it a lot). Not available on Basic.</li>
<li><strong>Turbo:</strong> up to 4× faster, at 2× the Fast time.</li>
</ul>

<h2>Reset and extra time</h2>
<p>Fast time resets when your subscription renews. Unused time doesn't carry over, on monthly and yearly plans alike. Extra Fast time is $4 an hour and expires after 60 days; free time earned by rating images expires after 30.</p>

<h2>Where to check</h2>
<p>Manage Subscription → Usage Details, or <code>/info</code> in Discord.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows the Fast hours you've used this period against your plan's allowance.</p>
""" + _foot(),
    },
    # ── Leonardo ──────────────────────────────────────────────────────
    {
        "slug": "leonardo-limits",
        "topic": "limits",
        "title": "How do Leonardo's tokens work?",
        "seo_title": "Leonardo.ai Tokens Explained: Plans, Rollover and Daily Reset",
        "summary": "Free gets 150 tokens a day. Paid plans get a monthly allowance (8,500 to 60,000) with a rollover bank of up to three months, and unlimited relaxed generation on Premium and up once tokens run out.",
        "keywords": "leonardo ai tokens fast tokens daily 150 essential premium ultimate rollover bank top-up relaxed unlimited reset monthly api credit",
        "legacy": [],
        "common": "150 a day on Free; a monthly allowance with rollover on paid plans.",
        "body": """
<h2>By plan</h2>
<ul>
<li><strong>Free:</strong> 150 tokens a day. Resets every 24 hours; unused tokens expire.</li>
<li><strong>Essential ($12/month):</strong> 8,500 a month.</li>
<li><strong>Premium ($30):</strong> 25,000 a month, plus unlimited relaxed image generation on selected models.</li>
<li><strong>Ultimate ($60):</strong> 60,000 a month, plus unlimited relaxed video on selected models.</li>
</ul>
<p>What a generation costs depends on the model, feature, size and number of images; Leonardo doesn't publish a fixed price per image.</p>

<h2>Reset, rollover and top-ups</h2>
<ul>
<li>Paid plans reset monthly on your subscription start date (upgrading doesn't move it).</li>
<li>Unused tokens go into a <strong>rollover bank</strong> of up to three months' worth, used only after this month's tokens. Cancelling clears it.</li>
<li>Top-up tokens never expire, but need an active subscription.</li>
<li>“Unlimited” relaxed generation starts only after your tokens run out, and it's slower.</li>
</ul>

<h2>Where to check</h2>
<p>The token counter in Leonardo. Hover it to see fast tokens, the rollover bank and top-ups.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows tokens left against your plan's allowance. With an API key it shows the balance only. <a href="/help/leonardo-setup">Setting up Leonardo</a>.</p>
""" + _foot(),
    },
    # ── Stability ─────────────────────────────────────────────────────
    {
        "slug": "stability-limits",
        "topic": "limits",
        "title": "How do Stability AI credits work?",
        "seo_title": "Stability AI API Credits Explained: Costs per Image and Balance",
        "summary": "The Stability AI API runs on prepaid credits (1 credit = $0.01) with no monthly reset. An image costs about 2–8 credits depending on the model; upscales cost more.",
        "keywords": "stability ai credits api balance prepaid cost per image stable image ultra sd 3.5 core upscale dreamstudio stable assistant comfy",
        "legacy": [],
        "common": "Prepaid API credits with no monthly reset.",
        "body": """
<h2>How it works</h2>
<p>The Stability AI platform API uses <strong>prepaid credits</strong>: 1 credit = $0.01, and new accounts get 25 free. There's no monthly allowance or reset; you top up when you need more.</p>

<h2>What things cost</h2>
<ul>
<li>Images: Stable Image Ultra 8 credits, SD 3.5 Large 6.5, Core 3, Flash 2.5.</li>
<li>Upscales: Fast 2, Conservative 40, Creative 60.</li>
<li>Most edits and controls: 4–8. Stable Audio: 8. 3D: 4–10.</li>
</ul>

<h2>What's separate</h2>
<p>API credits can't be used in DreamStudio or Stable Assistant, which have their own plans and credits.</p>

<h2>Where to check</h2>
<p>Your account page on the Stability AI platform, under Billing.</p>

<h2>A change to watch</h2>
<p>Stability's image and 3D APIs are moving to Comfy, with Comfy accounts and billing. If you use the API, watch for Stability's notice about the switch.</p>

<h2>In Tokenomics</h2>
<p>Add your API key once in Settings → AI Connections. Tokenomics shows your balance, how much you've used since your last top-up, and an estimate of when you'll run out at your current pace.</p>
""" + _foot(),
    },
    # ── Runway ────────────────────────────────────────────────────────
    {
        "slug": "runway-limits",
        "topic": "limits",
        "title": "How do Runway credits work?",
        "seo_title": "Runway Credits Explained: Plans, Per-Second Costs and Rollover",
        "summary": "Runway charges credits per second of video (Gen-4.5 is 12 a second). Plans include 625 to 9,500 credits a month. Unlimited plans move to Max on November 30, 2026, and API credits are separate.",
        "keywords": "runway credits per second gen-4.5 standard pro max team unlimited explore mode ending rollover purchased credits api credits separate",
        "legacy": [],
        "common": "Credits per second of video; app and API credits are separate.",
        "body": """
<h2>By plan (credits per month)</h2>
<ul>
<li><strong>Free:</strong> 125 credits, once, never expire.</li>
<li><strong>Standard ($15):</strong> 625 (about 52 seconds of Gen-4.5).</li>
<li><strong>Pro ($35):</strong> 2,250 (about 3 minutes).</li>
<li><strong>Max ($95):</strong> 9,500 (about 13 minutes).</li>
<li><strong>Team:</strong> 6,900 per seat, pooled.</li>
</ul>
<p>Video is charged <strong>per second</strong>: Gen-4.5 costs 12 credits a second, so a 5-second clip is 60 credits.</p>

<h2>Reset, rollover and purchases</h2>
<ul>
<li>Plan credits refresh on your billing date.</li>
<li>Standard and Pro: unused credits expire. Max and Team: up to a month rolls over.</li>
<li>Bought credits never expire, and are used after plan and rollover credits.</li>
</ul>

<h2>Unlimited and Explore Mode are ending</h2>
<p>Unlimited closed to new sign-ups in June 2026. Existing Unlimited plans move to Max on <strong>November 30, 2026</strong>, and Max has no Explore Mode.</p>

<h2>App credits vs API credits</h2>
<p>Credits in the Runway app and credits for Runway's developer API are completely separate. API credits are bought per project, cost $0.01 each, and don't reset monthly.</p>

<h2>Where to check</h2>
<p>Plans &amp; Billing in Runway.</p>

<h2>In Tokenomics</h2>
<p>Tokenomics connects to Runway with an API key, so it sees API credits, not the credits in your Runway app plan. From the next update (2.10.5), it reads your balance from Runway's current API and shows how much you've used since your last top-up, with an estimate of when you'll run out.</p>
""" + _foot(),
    },
    # ── ElevenLabs ────────────────────────────────────────────────────
    {
        "slug": "elevenlabs-limits",
        "topic": "limits",
        "title": "How do ElevenLabs credits work?",
        "seo_title": "ElevenLabs Credits Explained: Characters, Rollover and Plans",
        "summary": "ElevenLabs credits (formerly characters) reset monthly. On the website, every model costs 1 credit per character. Paid plans roll unused credits over, up to twice the monthly quota.",
        "keywords": "elevenlabs credits characters monthly free starter creator pro scale business rollover pay as you go turbo flash cost per character reset",
        "legacy": [],
        "common": "Monthly credits (formerly characters), with rollover on paid plans.",
        "body": """
<h2>What's counted</h2>
<p>ElevenLabs renamed “characters” to <strong>credits</strong>; the value didn't change. On the website, every voice model costs 1 credit per character. Through the API, some faster models cost 0.5.</p>

<h2>By plan (credits per month)</h2>
<ul>
<li><strong>Free:</strong> 10,000 (about 10 minutes of speech)</li>
<li><strong>Starter:</strong> 30,000 · <strong>Creator:</strong> 121,000 · <strong>Pro:</strong> 600,000</li>
<li><strong>Scale:</strong> 1.8 million · <strong>Business:</strong> 6 million</li>
</ul>

<h2>Reset and rollover</h2>
<ul>
<li>Credits reset monthly on your billing date, on annual plans too.</li>
<li>Paid plans roll unused credits over, up to 2× your monthly quota, so your balance can reach 3×. Free plans don't roll over.</li>
<li>Downgrading or cancelling loses unused credits at the end of the cycle.</li>
<li>Pay-as-you-go credits are separate and expire 12 months after purchase.</li>
</ul>

<h2>Where to check</h2>
<p>Your profile → Subscription on elevenlabs.io.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows credits used this cycle against your plan, with the reset date ElevenLabs reports. (Versions before 1.1.3 label them “Characters”.) <a href="/help/elevenlabs-setup">Setting up ElevenLabs</a>.</p>
""" + _foot(),
    },
    # ── Suno ──────────────────────────────────────────────────────────
    {
        "slug": "suno-limits",
        "topic": "limits",
        "title": "How do Suno credits work?",
        "seo_title": "Suno Credits Explained: Daily Free Credits and Monthly Plans",
        "summary": "Free gets 50 credits a day. Pro and Premier get a monthly allowance (2,500 or 10,000) that resets on your subscription date, with no carryover. Paid users who run out get 50 a day until renewal.",
        "keywords": "suno credits daily 50 free pro premier platinum monthly 2500 10000 reset carryover top-up credits per song downloads",
        "legacy": [],
        "common": "50 a day on Free; a monthly allowance on paid plans.",
        "body": """
<h2>By plan</h2>
<ul>
<li><strong>Free:</strong> 50 credits a day, resetting daily (UTC).</li>
<li><strong>Pro ($10/month):</strong> 2,500 credits a month, 20 downloads.</li>
<li><strong>Premier ($30/month):</strong> 10,000 credits, 60 downloads.</li>
<li><strong>Platinum ($120/month):</strong> 15,000 song credits plus separate visual credits, 120 downloads.</li>
</ul>

<h2>Reset and top-ups</h2>
<ul>
<li>Paid credits reset monthly on the day and time you subscribed, on yearly plans too. Unused credits don't carry over.</li>
<li>If a paid plan runs out early, you get 50 free credits a day until renewal.</li>
<li>Bought top-up credits never expire, but need an active subscription.</li>
</ul>

<h2>Where to check</h2>
<p>suno.com/account.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows credits left against your monthly allowance. Suno doesn't report a renewal date, so Tokenomics learns it the first time your credits refill. <a href="/help/renewal-dates">More on renewal dates</a>.</p>
""" + _foot(),
    },
    # ── Udio ──────────────────────────────────────────────────────────
    {
        "slug": "udio-limits",
        "topic": "limits",
        "title": "How do Udio credits work?",
        "seo_title": "Udio Credits Explained: Daily and Monthly Limits",
        "summary": "One Udio credit is about 30 seconds of music, and each generation makes two tracks. Free has both a daily and a monthly limit; Standard and Pro have a monthly allowance with no daily cap.",
        "keywords": "udio credits daily monthly free standard pro 2400 6000 per track 30 seconds top-up reset",
        "legacy": [],
        "common": "Daily and monthly on Free; monthly on paid plans.",
        "body": """
<h2>What a credit buys</h2>
<p>One credit is roughly one 30-second track. Each generation makes two tracks, so it costs 2 credits; longer models cost more.</p>

<h2>By plan</h2>
<ul>
<li><strong>Free:</strong> 10 credits a day and a monthly limit. You use the daily credits first. Daily credits refresh 24 hours after your first song that day.</li>
<li><strong>Standard ($10/month):</strong> 2,400 credits a month, no daily limit.</li>
<li><strong>Pro ($30/month):</strong> 6,000 a month, no daily limit.</li>
</ul>

<h2>Reset and top-ups</h2>
<p>Monthly credits refresh one month after your plan (or your free cycle) starts, and don't roll over. Bought credits never expire. When you run out, you can't generate until they refresh or you buy more.</p>

<h2>Where to check</h2>
<p>Your Udio account page.</p>

<h2>In Tokenomics</h2>
<p>The browser extension shows the monthly limit as the main meter and the daily limit as a second meter, with the real reset times Udio reports.</p>
""" + _foot(),
    },
]
