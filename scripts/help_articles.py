# Help center content: one entry per article. Edit here, then run
#   python3 scripts/build_help.py
# to regenerate help/index.html, help/<slug>.html and sitemap.xml.
#
# Fields:
#   slug     URL: /help/<slug>
#   topic    key into TOPICS
#   title    the question (H1 + <title>)
#   summary  one or two sentences: meta description, hub list and search snippet
#   keywords extra words people search with that the answer doesn't use
#   legacy   old /faq#anchors that should land here
#   body     the answer, as HTML

TOPICS = [
    {"id": "browser-extension", "num": 1, "title": "Getting set up",
     "desc": "Installing, which tools and browsers work, what it costs, and how the app and extension fit together."},
    {"id": "using-tokenomics", "num": 2, "title": "Using Tokenomics",
     "desc": "The menu bar, widgets, alerts and settings, day to day."},
    {"id": "reading-numbers", "num": 3, "title": "Your numbers",
     "desc": "Each AI tool counts usage its own way. Here's what each meter means."},
    {"id": "fixing-problems", "num": 4, "title": "Fixing problems",
     "desc": "Error messages, prompts, and what to try when numbers look wrong."},
    {"id": "privacy-permissions", "num": 5, "title": "Privacy & permissions",
     "desc": "What Tokenomics reads, what it stores on your device, and what it never sends."},
]

CHROME_URL = "https://chromewebstore.google.com/detail/tokenomics-ai-usage-limit/nolficmmhjkgmoclepbclpmefilhlejl"

ARTICLES = [
    # ── Getting set up ───────────────────────────────────────────────
    {
        "slug": "supported-tools",
        "topic": "browser-extension",
        "title": "Which AI tools does Tokenomics work with?",
        "seo_title": "AI Tools Tokenomics Tracks: Claude, ChatGPT, Copilot & More",
        "summary": "From Claude Code and Cursor to ChatGPT, Midjourney and Suno. Here's the full list, what each meter tracks, and how each one connects.",
        "keywords": "supported compatible list providers websites sites tools claude chatgpt gemini midjourney elevenlabs grok perplexity leonardo suno udio claude code codex cli github copilot cursor stability runway",
        "legacy": ["ext-sites"],
        "common": "Coding tools, chat apps and creative tools, from Claude Code to Suno. The web ones connect through the browser extension.",
        "body": """
<p>Coding tools connect through the Mac app, which reads the sign-in they already keep on your Mac. Web tools connect through the <a href="/#extension">browser extension</a>, which reads the sites you're signed in to. A few take an API key you paste once.</p>
<div class="doc-table-wrap doc-table-wrap--wide">
<table class="doc-table">
<thead><tr><th scope="col">Tool</th><th scope="col">What it tracks</th><th scope="col">Connects through</th></tr></thead>
<tbody>
<tr><td>Claude</td><td>5-hour and 7-day limits, shared by chats and Claude Code</td><td>Mac app (through Claude Code) or extension</td></tr>
<tr><td>ChatGPT</td><td>Chats on chatgpt.com</td><td>Extension</td></tr>
<tr><td>Codex CLI</td><td>OpenAI's coding agent, in Terminal: 5-hour and weekly limits</td><td>Mac app</td></tr>
<tr><td>Gemini</td><td>Chats on gemini.google.com</td><td>Extension</td></tr>
<tr><td>Gemini CLI</td><td>Google's coding agent, in Terminal: <a href="/help/gemini-cli-numbers">requests and tokens today</a>, estimated</td><td>Mac app</td></tr>
<tr><td>GitHub Copilot</td><td><a href="/help/copilot-meters">Premium requests</a> (paid plans), or chat and completions (free)</td><td>Mac app</td></tr>
<tr><td>Cursor</td><td>Premium requests</td><td>Mac app</td></tr>
<tr><td>Stability AI</td><td>Image and video generation credits</td><td>Mac app, with an API key</td></tr>
<tr><td>Runway</td><td>Video generation credits</td><td>Mac app, with an API key</td></tr>
<tr><td>ElevenLabs</td><td>Voice generation credits</td><td>Extension</td></tr>
<tr><td>Midjourney</td><td><a href="/help/midjourney-fast-hours">Fast Hours</a></td><td>Extension</td></tr>
<tr><td>Leonardo</td><td>Image generation credits</td><td>Extension</td></tr>
<tr><td>Grok</td><td>Chats on grok.com</td><td>Extension</td></tr>
<tr><td>Perplexity</td><td>Pro searches and research</td><td>Extension</td></tr>
<tr><td>Suno</td><td>Music generation credits</td><td>Extension</td></tr>
<tr><td>Udio</td><td>Music generation credits</td><td>Extension</td></tr>
</tbody>
</table>
</div>
<p>If you have both the Mac app and the extension, the web tools the extension reads also show in your menu bar and widgets (<a href="/help/mac-app-and-extension">how they work together</a>). Suno and Udio reach the Mac app in its next update; the extension shows them today.</p>
<p>Setting up a coding tool? The <a href="/setup">setup guide</a> walks through each one.</p>
""",
    },
    {
        "slug": "browsers",
        "topic": "browser-extension",
        "title": "Which browsers does the extension work in?",
        "summary": "Google Chrome, plus Brave, Arc, Vivaldi and Opera from the Chrome Web Store. Versions for Microsoft Edge and Safari are on the way.",
        "keywords": "browser browsers chrome edge chromium brave arc opera vivaldi safari firefox beta canary store install supported add-ons",
        "legacy": ["browsers"],
        "body": f"""
<p>Google Chrome. Install it from the <a href="{CHROME_URL}" target="_blank" rel="noopener">Chrome Web Store</a>.</p>
<p>It's a standard Chromium extension, so other Chromium browsers like Brave, Arc, Vivaldi and Opera can install it from the Chrome Web Store too.</p>
<p>Versions for Microsoft Edge (on Edge Add-ons) and Safari (Tokenomics for Safari, a free app on the Mac App Store) are in review. We'll link them here as soon as they're live. Firefox isn't supported.</p>
<p>Use Safari day to day? You can still track your web tools now; see <a href="/help/safari">tracking web tools if you use Safari</a>.</p>
<p>If you also run the Mac app, it links up with Chrome (including Beta and Canary), Edge, Brave, Vivaldi, Opera and Arc, so your readings reach the menu bar and widgets from any of them.</p>
""",
    },
    {
        "slug": "extension-without-mac-app",
        "topic": "browser-extension",
        "title": "Does the extension work without the Mac app?",
        "seo_title": "AI Usage Tracker for Chrome, No Mac App Needed | Tokenomics",
        "summary": "Yes. It works on its own in your browser. The Mac app adds menu bar rings, widgets and coding tools, and the two stay in sync.",
        "keywords": "without alone standalone only need required require both sync together connect menubar widgets",
        "legacy": ["ext-standalone"],
        "common": "Yes, on its own in your browser. The Mac app adds menu bar rings, widgets and coding tools, and the two stay in sync.",
        "body": """
<p>Yes. The extension works on its own in your browser: click its toolbar icon to see a meter for each site you're signed in to.</p>
<p>The Mac app adds three things:</p>
<ul>
<li><strong>Menu bar rings</strong>, so you see your closest limit without opening anything.</li>
<li><strong>Desktop widgets</strong> in small, medium and large, plus extra large on macOS 27. See <a href="/help/widgets">setting up widgets</a>.</li>
<li><strong>Coding tools</strong> the browser can't see: Claude Code, Codex CLI, Gemini CLI, GitHub Copilot and Cursor.</li>
</ul>
<p>If you have both, they sync: the extension's readings show in the menu bar and widgets, and the order you set for your tabs carries across. See <a href="/help/mac-app-and-extension">how the two work together</a>.</p>
""",
    },
    {
        "slug": "mac-app-and-extension",
        "topic": "browser-extension",
        "title": "How do the Mac app and the browser extension work together?",
        "summary": "The Mac app reads your coding tools, the extension reads your web tools, and they share usage numbers on your computer so each shows the full picture.",
        "keywords": "sync syncing synced together both link linked connect connection bridge share mac app extension primary source which wins conflict order visibility settings refresh helper native messaging",
        "legacy": [],
        "body": """
<p>Each one reads the tools it can reach. Then they share what they read, so both show the full picture.</p>
<h2>Who reads what</h2>
<div class="doc-table-wrap doc-table-wrap--wide">
<table class="doc-table">
<thead><tr><th scope="col">Read by</th><th scope="col">Tools</th></tr></thead>
<tbody>
<tr><td>Mac app</td><td>Claude (through Claude Code's sign-in), Codex CLI, Gemini CLI, GitHub Copilot, Cursor, and Stability AI and Runway with an API key</td></tr>
<tr><td>Browser extension</td><td>ChatGPT, Gemini, Midjourney, Leonardo, Grok, Perplexity, Suno and Udio, plus Claude and ElevenLabs from their websites</td></tr>
</tbody>
</table>
</div>
<h2>What the Mac app gets from the extension</h2>
<p>Everything the extension reads from a web-only tool shows in your menu bar, popover, widgets and notifications, usually within a second or two of the extension reading it.</p>
<p>When your browser is closed, the Mac app keeps showing the last reading, marked “Last read 2h ago”, for up to two days or until that limit resets. Usage can't go down until a reset, so the last number is still a safe guide.</p>
<p>Two tools can come from either side, and the Mac app picks one:</p>
<ul>
<li><strong>Claude:</strong> the Mac app always uses Claude Code's sign-in. Chats and Claude Code share the same limits, so the website reading would show the same numbers. If you only use claude.ai and don't have Claude Code, Claude shows in the extension but not in the Mac app.</li>
<li><strong>ElevenLabs:</strong> the Mac app uses the extension's reading. If you added an ElevenLabs API key in an earlier version of the Mac app, it keeps using that key instead.</li>
</ul>
<h2>What the extension gets from the Mac app</h2>
<p>The extension's popup also shows Codex CLI, Gemini CLI, GitHub Copilot and Cursor from the Mac app, so you can check them from your browser. For Claude, the popup shows whichever reading is newer. ChatGPT and Codex CLI always appear as separate tabs, since they have separate limits (extension 1.1.2 and later).</p>
<h2>Settings that sync</h2>
<ul>
<li><strong>Tab order</strong> syncs both ways. Rearrange tabs in either one and the other follows; the most recent change wins.</li>
<li><strong>Turning a tool on or off</strong> syncs both ways: switch it off in the Mac app's settings or the extension's, and it's hidden in both. The most recent change wins. (Needs Mac app 2.10.5 or later.)</li>
<li><strong>Refresh</strong> works across both: refreshing in the Mac app asks the extension to re-read its sites within a minute, and refreshing in the extension makes the Mac app re-check its tools.</li>
</ul>
<h2>What never crosses over</h2>
<p>Only usage numbers and these few settings. Your sign-ins, cookies and API keys stay where they are: a key you paste into the extension never reaches the Mac app, and the other way round.</p>
<p>The link is entirely on your computer. When the extension has new numbers, your browser hands them to a small helper inside Tokenomics.app, which saves them to a file the Mac app reads. Nothing goes over the internet. This is the “communicate with cooperating native applications” permission Chrome mentions; see <a href="/help/extension-permissions">what the extension can access</a>.</p>
<h2>Setting up the link</h2>
<ol>
<li>Install the Mac app and the browser extension.</li>
<li>Open the Mac app at least once after installing the extension. That's when it sets up the link, for Chrome (including Beta and Canary), Edge, Brave, Vivaldi, Opera and Arc.</li>
<li>Open the extension's popup. Your web tools appear in the Mac app shortly after.</li>
</ol>
<p>Not seeing readings in the Mac app? Try the steps in <a href="/help/troubleshooting">Something's not working</a>.</p>
""",
    },
    {
        "slug": "windows-and-linux",
        "topic": "browser-extension",
        "title": "Does Tokenomics work on Windows or Linux?",
        "seo_title": "Track AI Usage Limits on Windows and Linux | Tokenomics",
        "summary": "The browser extension does, in Chrome. The menu bar app, widgets and coding-tool tracking need a Mac for now.",
        "keywords": "windows linux pc chromebook requirements requirement macos version sonoma supported platform",
        "legacy": [],
        "body": f"""
<p>The browser extension does. It runs anywhere Chrome does, including Windows and Linux. Install it from the <a href="{CHROME_URL}" target="_blank" rel="noopener">Chrome Web Store</a> and it shows your usage for the AI sites you're signed in to.</p>
<p>The menu bar app is Mac only for now. It needs macOS 14 Sonoma or later, and it's what tracks coding tools (Claude Code, Codex CLI, Gemini CLI, GitHub Copilot and Cursor) and draws the menu bar rings and widgets. A Windows and Linux version of the app is on the roadmap.</p>
""",
    },
    {
        "slug": "is-it-free",
        "topic": "browser-extension",
        "title": "Is Tokenomics free?",
        "seo_title": "Is Tokenomics Free? Yes: No Subscription, No Paid Tier",
        "summary": "Yes. The Mac app and the browser extension are free, with no subscription, no ads and no account to make.",
        "keywords": "price pricing cost costs pay paid money subscription buy charge ads account sponsor license licence opensource open source github code",
        "legacy": ["free"],
        "body": """
<p>Yes. The Mac app, the browser extension and Tokenomics for Safari are all free. There's no subscription, no ads and no account to make.</p>
<p>The code is source-available on <a href="https://github.com/rob-stout/Tokenomics" target="_blank" rel="noopener">GitHub</a>, so you can read every line, and the <a href="/license">license</a> makes it free for personal use. It isn't MIT-licensed: commercial rights are reserved, so there's room for paid capabilities later, like a version for teams. If those ever ship, the current app stays free for everyone who already has it.</p>
<p>If you'd like to chip in, there's a <a href="https://buymeacoffee.com/robstout" target="_blank" rel="noopener">Buy me a coffee</a> page.</p>
""",
    },
    {
        "slug": "extension-consent",
        "topic": "browser-extension",
        "title": "Does the extension start reading as soon as I install it?",
        "summary": "No. It shows a short consent screen first, and nothing is read until you click Agree and turn on.",
        "keywords": "consent agree enable disable turn off stop pause delete data start blank empty install",
        "legacy": ["ext-consent"],
        "body": """
<p>No. On install it shows a short consent screen that explains what it reads and stores. Nothing is read until you click <strong>Agree and turn on</strong>.</p>
<p>To turn it off later, open the extension's settings and click <strong>Stop reading and delete my data</strong>. That deletes everything it saved, and it stays off until you agree again.</p>
<p>You can also switch individual sites off in the extension's settings, which hides them from the popup.</p>
""",
    },
    {
        "slug": "signing-in",
        "topic": "browser-extension",
        "title": "How does signing in work?",
        "summary": "There's nothing to sign in to. The Mac app reads the sign-in your coding tools already keep, the extension uses the sites you're signed in to, and Stability AI and Runway take an API key.",
        "keywords": "signin login password credentials keychain token api key cli auth account authenticate paste",
        "legacy": ["sign-in"],
        "body": """
<p>Tokenomics has no account of its own, and you never give it a password. It uses the sign-ins you already have:</p>
<ul>
<li><strong>Coding tools</strong> (Claude Code, Codex CLI, Gemini CLI, GitHub Copilot, Cursor): the Mac app reads the sign-in those tools already saved on your Mac. There's nothing to paste.</li>
<li><strong>Web tools</strong> (ChatGPT, Gemini, Midjourney and the rest): the browser extension uses the sites you're signed in to, the same way the site's own pages do.</li>
<li><strong>Stability AI and Runway</strong>: paste an API key once during setup. The Mac app keeps it in the macOS Keychain.</li>
</ul>
<p>If a coding tool isn't installed or signed in yet, guided setup does it for you, in Terminal or your browser (<a href="/help/what-setup-installs">what setup installs</a>). For Claude Code, macOS asks once before Tokenomics can read its sign-in; see <a href="/help/keychain-prompt">the Keychain prompt</a>.</p>
<p>Tokenomics never copies your sign-in anywhere else. The specifics are itemized on the <a href="/privacy">Privacy page</a>.</p>
""",
    },
    {
        "slug": "elevenlabs-setup",
        "topic": "browser-extension",
        "title": "How do I set up ElevenLabs?",
        "summary": "Visit elevenlabs.io with the extension installed, or paste an ElevenLabs API key into the extension. The Mac app shows whatever the extension reads.",
        "keywords": "elevenlabs eleven labs api key keys setup permission user access characters credits",
        "legacy": ["ext-elevenlabs"],
        "body": """
<p>ElevenLabs connects through the browser extension, in one of two ways:</p>
<ol>
<li><strong>Open elevenlabs.io</strong> in your browser while signed in. The extension picks up the access your browser already has and reads your usage from then on.</li>
<li><strong>Paste an API key into the extension</strong> (open the extension's settings and find ElevenLabs). It then reads your usage directly, without you visiting the site. While a key is set, the extension stops using your site sign-in. Remove the key to go back.</li>
</ol>
<p>The Mac app shows the extension's reading in your menu bar and widgets. It updates every few minutes while your browser is open; with the browser closed, the Mac app keeps the last reading. If you added an ElevenLabs key in an earlier version of the Mac app, it keeps using that key instead.</p>
<h2>Making a key</h2>
<p>In ElevenLabs, open <a href="https://elevenlabs.io/app/settings/api-keys" target="_blank" rel="noopener">API Keys</a> and create a key. Set “User” to “Access” and leave everything else on “No Access”. That's all Tokenomics needs, and a key like that can't generate audio or change your account. If the key is missing that permission, Tokenomics won't save it and tells you why.</p>
<h2>Things you might notice</h2>
<ul>
<li><strong>Reset dates on Free accounts.</strong> ElevenLabs sometimes keeps reporting the first month's reset date long after it passed. Characters still refresh monthly on that day, so Tokenomics counts forward to the next one.</li>
<li><strong>The extension saves keys on your device</strong>, in your browser's extension storage, unencrypted. Use a key with only the “User” permission so it's harmless if it ever leaked.</li>
</ul>
""",
    },
    {
        "slug": "uninstall",
        "topic": "using-tokenomics",
        "title": "How do I uninstall Tokenomics?",
        "seo_title": "How to Uninstall Tokenomics on Mac (and Remove Everything)",
        "summary": "Use Settings → Uninstall Tokenomics… to remove the app and everything it set up. To remove the extension, right-click its toolbar icon and choose Remove.",
        "keywords": "uninstall remove delete trash removal clean leftover preferences extension get rid brew zap homebrew keychain",
        "legacy": ["uninstall"],
        "body": """
<h2>The Mac app</h2>
<p>Open Settings (the gear in the popover) and choose <strong>Uninstall Tokenomics…</strong>. It removes Tokenomics and everything it set up, then moves the app to the Trash:</p>
<ul>
<li>its settings, saved usage numbers and caches;</li>
<li>Launch at Login;</li>
<li>the link files it adds to your browsers for the extension;</li>
<li>API keys you gave it, from your Keychain.</li>
</ul>
<p>It leaves your AI tools alone. Your Claude Code sign-in stays, so you won't be signed out.</p>
<p>Installed with Homebrew? Run <code>brew uninstall --zap tokenomics</code> instead, which does the same cleanup.</p>
<p>If you just drag the app to the Trash, those extras stay behind. They're harmless, but the in-app option is cleaner.</p>
<h2>Tools setup installed for you</h2>
<p>Uninstalling Tokenomics doesn't remove coding tools that guided setup installed, since you may use them on their own (<a href="/help/what-setup-installs">what setup installs</a>). To remove them too:</p>
<ul>
<li><strong>Codex CLI and Gemini CLI:</strong> delete the <code>~/.tokenomics-cli</code> folder.</li>
<li><strong>Claude Code:</strong> follow Anthropic's uninstall instructions, and remove the line setup added to <code>~/.zprofile</code>.</li>
<li><strong>Homebrew, Node.js and the GitHub CLI:</strong> remove them with Homebrew if you don't use them elsewhere.</li>
</ul>
<h2>The browser extension</h2>
<p>Right-click its toolbar icon and choose <strong>Remove</strong>. That deletes everything it saved.</p>
""",
    },
    {
        "slug": "troubleshooting",
        "topic": "fixing-problems",
        "title": "Something's not working. What can I try?",
        "summary": "Most problems clear up by checking you're signed in, clicking refresh, or reopening your browser. Here's the full checklist.",
        "keywords": "broken troubleshoot troubleshooting fix help error problem issue stuck blank empty nothing missing zero refresh reload restart update updated sync not working",
        "legacy": ["not-working"],
        "body": """
<p>Most problems clear up with one of these:</p>
<ul>
<li><strong>Check you're signed in</strong> to that site in the same browser. Gemini, Suno, Leonardo and ElevenLabs need you to open the site in a tab at least once, because the extension reads them from the page.</li>
<li><strong>Click refresh</strong> in the extension's popup.</li>
<li><strong>Check the site is switched on</strong> in the extension's settings.</li>
<li><strong>If the popup shows nothing at all,</strong> make sure you clicked <strong>Agree and turn on</strong> on the <a href="/help/extension-consent">consent screen</a>.</li>
<li><strong>If the Mac app isn't getting readings,</strong> check that it's running and that you've opened it at least once since installing the extension. That's when it sets up the link. Then reopen the popup.</li>
<li><strong>Just updated the extension?</strong> Quit and reopen your browser.</li>
</ul>
<p>More specific fixes:</p>
<ul>
<li><a href="/help/menu-bar-not-updating">The menu bar stopped updating</a></li>
<li><a href="/help/rate-limited">“Couldn't load usage data” and other messages</a></li>
<li><a href="/help/keychain-prompt">macOS keeps asking for my password</a></li>
<li><a href="/help/sign-in-expired">“Authentication expired”</a></li>
<li><a href="/help/setup-errors">Guided setup showed an error</a></li>
<li><a href="/help/widget-not-updating">A widget shows old numbers</a></li>
</ul>
<p>Problem with a coding tool, like Claude Code or Copilot? The <a href="/setup">setup guide</a> covers each one.</p>
""",
    },

    # ── Reading your numbers ─────────────────────────────────────────
    {
        "slug": "claude-usage-limits",
        "topic": "reading-numbers",
        "title": "How do Claude's 5-hour and 7-day limits work?",
        "seo_title": "Claude Usage Limits Explained: 5-Hour and Weekly Windows",
        "summary": "The 5-hour window is the rolling cap most people hit first; the 7-day window is the weekly ceiling. Chats and Claude Code share both.",
        "keywords": "anthropic limit quota rate reset weekly week rolling pro max 5 hour 7 day window single one desktop claude code",
        "legacy": ["claude-windows", "anthropic-one-window"],
        "body": """
<p>These are Anthropic's own limits, not something Tokenomics invented.</p>
<h2>The 5-hour window</h2>
<p>The rolling cap most people hit first. It resets about five hours after your first message in the current block. If Tokenomics shows 80% with two hours left, you're close to a rate limit, so pace your prompts or switch tasks.</p>
<h2>The 7-day window</h2>
<p>The longer ceiling, resetting weekly from your first message of the cycle.</p>
<p>If your plan has extra usage turned on, the Claude tab also shows how much of your monthly extra-usage limit you've spent. See <a href="/help/extra-usage-and-credits">Extra Usage</a>.</p>
<h2>Why Claude has one set of limits</h2>
<p>Claude on the web, the Claude desktop app and Claude Code all draw down the <strong>same 5-hour and 7-day windows</strong> on your subscription. One set of limits covers every surface, so Claude gets one meter with two bars. OpenAI and Google do it the other way, with a separate meter per product. See <a href="/help/two-meters">why ChatGPT and Gemini show two meters</a>.</p>
""",
    },
    {
        "slug": "two-meters",
        "topic": "reading-numbers",
        "title": "Why do ChatGPT and Gemini show two meters?",
        "seo_title": "ChatGPT and Gemini Usage Limits: Why There Are Two Meters",
        "summary": "ChatGPT and Codex CLI share an OpenAI login but have separate limits, and so do the Gemini app and Gemini CLI. Tokenomics shows each limit on its own.",
        "keywords": "openai codex gemini meters separate gpt two bars twice double duplicate widget small medium large rows chatgpt cli google",
        "legacy": ["chatgpt-two-bars", "widget-openai-twice"],
        "body": """
<p>ChatGPT and Codex CLI are two different products that share one OpenAI login but count against <strong>separate limits</strong>. ChatGPT has its own chat limits; Codex CLI has its own weekly quota tied to your plan. Same account, different meters, and OpenAI doesn't give a combined number, so Tokenomics shows both and you can see which one you're closer to.</p>
<p>The same is true for <strong>Gemini</strong>: the Gemini app at <code>gemini.google.com</code> and the Gemini CLI share a Google account but track usage separately.</p>
<p>Claude is the exception: chats and Claude Code share one set of limits. See <a href="/help/claude-usage-limits">how Claude's limits work</a>.</p>
<h2>In widgets</h2>
<p>Widgets show each limit as its own row, because there's no room to nest them. If you've connected both ChatGPT and Codex CLI, you'll see two OpenAI rows. On the <strong>small widget</strong> you pick exactly one: open the widget's edit panel and choose <strong>ChatGPT</strong> or <strong>Codex CLI</strong>.</p>
<div class="doc-callout">
<p><strong>Upgrading from an earlier version?</strong> If your small widget was set to “OpenAI” or “Google AI,” it now shows <strong>Codex CLI</strong> or <strong>Gemini CLI</strong>, because that's what those entries were already tracking. To show the chat limit instead, pick it in the edit panel.</p>
</div>
""",
    },
    {
        "slug": "are-numbers-exact",
        "topic": "reading-numbers",
        "title": "Are the numbers exact?",
        "summary": "Almost always. Tokenomics shows the limits each tool reports. The few readings it has to work out itself are marked as estimates.",
        "keywords": "accurate accuracy estimate estimated wrong correct precise numbers chatgpt gemini cli label off",
        "legacy": ["ext-exact"],
        "body": """
<p>Almost always. For nearly every tool, Tokenomics shows the same limits and reset times the tool itself uses.</p>
<p>A few readings have to be worked out:</p>
<ul>
<li><strong>ChatGPT</strong>: the extension normally reads ChatGPT's real limits. If it can't, it falls back to counting the messages you send from that browser (the time and model only, never what you wrote) against your plan's limits. See <a href="/help/chatgpt-plan">fixing the ChatGPT plan</a>.</li>
<li><strong>Gemini CLI</strong>: Google doesn't report it, so Tokenomics counts your requests from the session files Gemini CLI keeps on your Mac, against the daily limits of the plan you choose. See <a href="/help/gemini-cli-numbers">how Gemini CLI is counted</a>.</li>
</ul>
<p>Estimated readings are labelled: the extension shows an <strong>estimated</strong> tag, and the Mac app's popover says “Estimated from…” under the numbers.</p>
<p>If a number looks wrong, click refresh first. If it's still off, <a href="/help/report-a-problem">tell us</a> which tool and plan you're on.</p>
""",
    },
    {
        "slug": "midjourney-fast-hours",
        "topic": "reading-numbers",
        "title": "What are Midjourney's Fast Hours?",
        "seo_title": "Midjourney Fast Hours Explained: How to Track What’s Left",
        "summary": "Fast Hours are the GPU time Midjourney gives your plan each month for Fast mode. Tokenomics shows how many you've used. Relax mode doesn't count.",
        "keywords": "midjourney fast hour hours relax mode turbo gpu credits plan monthly basic standard pro mega",
        "legacy": ["midjourney-fast-hours"],
        "body": """
<p>Midjourney measures paid usage in Fast Hours: GPU time spent generating in Fast mode. Each plan comes with a set number every month.</p>
<p>The extension shows how many Fast Hours you've used of your plan's monthly total, refreshed from your Midjourney account. Relax mode doesn't use Fast Hours, so Relax jobs don't move the meter.</p>
<p>If it shows no plan, your Midjourney account doesn't have an active subscription.</p>
""",
    },

    # ── Privacy & permissions ────────────────────────────────────────
    {
        "slug": "privacy",
        "topic": "privacy-permissions",
        "title": "Is my data sent anywhere? Does Tokenomics see my chats?",
        "seo_title": "Does Tokenomics Read Your Chats? Privacy, Answered",
        "summary": "No. Nothing goes to any server the author controls: no analytics, telemetry or tracking. The extension reads usage numbers, never your chats or prompts.",
        "keywords": "privacy private tracking telemetry analytics safe secure security collect server data chat prompt conversation message history read sent send",
        "legacy": ["data", "ext-data", "ext-chats"],
        "common": "No. There's no analytics, telemetry or tracking, and nothing is sent to any server the author controls.",
        "body": """
<p>No. Tokenomics talks only to the AI services you use, to fetch your own usage, plus the Mac app on your own computer if you have it. Nothing goes to any server the author controls. There's no analytics, telemetry or tracking code in the app or the extension.</p>
<h2>What it keeps</h2>
<p>The Mac app saves only the usage numbers its widgets need, on your Mac. The extension saves your settings and latest numbers in your browser's extension storage, on your device.</p>
<h2>Your chats and prompts</h2>
<p>The extension reads usage numbers, not conversations, and it doesn't store your prompts or chats. On ChatGPT it notes the time and model of each message you send, to <a href="/help/are-numbers-exact">estimate usage</a> when exact numbers aren't available. It never keeps what you wrote.</p>
<p>The full, itemized breakdown of what each part reads and connects to is on the <a href="/privacy">Privacy page</a>.</p>
""",
    },
    {
        "slug": "extension-permissions",
        "topic": "privacy-permissions",
        "title": "What can the browser extension access, and why?",
        "summary": "Only the AI sites it works with, to read your own usage numbers. It doesn't ask for access to all websites. Here's what each permission is for.",
        "keywords": "permission permissions host storage store token see websites reason native application messaging warning bridge cooperating communicate access",
        "legacy": ["ext-access", "ext-why-sites", "ext-native"],
        "body": """
<h2>Which sites</h2>
<p>Only the AI sites it works with: Claude, ChatGPT, Gemini, Midjourney, ElevenLabs, Grok, Perplexity, Leonardo, Suno and Udio. It doesn't ask for access to all websites, and it doesn't touch any others.</p>
<h2>Why it needs them</h2>
<p>Each site shows your usage in its own account pages, with no shared way to get it. To show it in the popup, the extension asks that site for your numbers, the same way the site's own pages do, using the sign-in you already have. That's the only reason it has access. Numbers refresh every few minutes.</p>
<h2>What it stores</h2>
<p>Your settings and latest numbers, in your browser's extension storage on your device. For ElevenLabs and Leonardo it also saves the access token the site gives your browser, or an API key you paste in its settings.</p>
<h2>“Communicate with cooperating native applications”</h2>
<p>Chrome shows this for the permission the extension uses to hand your usage numbers to the Tokenomics Mac app, if you have it installed. It stays on your computer, and your sign-in tokens are never sent over it. Without the Mac app, nothing happens.</p>
""",
    },
    {
        "slug": "affiliation",
        "topic": "privacy-permissions",
        "title": "Is Tokenomics affiliated with these AI services?",
        "summary": "No. Tokenomics is independent and unofficial. It reads your own usage with your own sign-in.",
        "keywords": "affiliated official unofficial endorsed partner terms allowed ban banned legal trademark",
        "legacy": ["ext-allowed"],
        "body": """
<p>No. Tokenomics is independent and unofficial. It uses your own signed-in session to read your own usage, the same numbers the services show you on their own account pages.</p>
<p>Each service has its own terms; please read them. Claude, ChatGPT, Gemini, Midjourney, ElevenLabs, Grok, Perplexity, Leonardo, Suno, Udio and related names are the property of their owners and are used here only to say which services Tokenomics works with.</p>
""",
    },
]

from help_articles_app import APP_ARTICLES  # noqa: E402
ARTICLES += APP_ARTICLES

# Common-question cards on the hub, in order.
COMMON = ["supported-tools", "privacy", "extension-without-mac-app"]

# Answers elsewhere on the site, so hub searches don't dead-end.
ELSEWHERE = [
    {"title": "How do I install Tokenomics?", "href": "/#install", "where": "On the home page", "w": 1,
     "text": "Download the Mac app from this site, or install it with Homebrew. The browser extension installs from the Chrome Web Store.",
     "kw": "install installing download homebrew brew dmg get"},
    {"title": "Connecting your AI tools to the Mac app", "href": "/setup", "where": "On the setup page",
     "text": "Step-by-step setup for Claude Code, GitHub Copilot, Cursor, Codex CLI, Gemini CLI and API-key providers, with fixes for common problems.",
     "kw": "setup install installing connect connecting troubleshoot troubleshooting fix broken steps guide"},
    {"title": "Privacy policy", "href": "/privacy", "where": "On the privacy page",
     "text": "Exactly what the Mac app, the browser extension and Tokenomics for Safari read, store and connect to.",
     "kw": "privacy policy gdpr legal data stored storage"},
    {"title": "Contact and support", "href": "#contact", "where": "",
     "text": "Email hello@trytokenomics.com or open an issue on GitHub.",
     "kw": "contact email support help bug report issue feedback question human"},
]
