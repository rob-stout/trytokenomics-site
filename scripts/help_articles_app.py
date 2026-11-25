# More Help articles: using the Mac app and the extension day to day, and fixing
# problems. Same fields as help_articles.py; merged into ARTICLES there.

SETUP = "/setup"

APP_ARTICLES = [
    # ── Using Tokenomics ─────────────────────────────────────────────
    {
        "slug": "menu-bar",
        "topic": "using-tokenomics",
        "title": "How do I choose what the menu bar shows?",
        "summary": "By default the menu bar shows whichever tool is closest to its limit. You can pin one tool instead from the popover's Menu Bar Display menu.",
        "keywords": "menu bar menubar icon rings ring smart pin pinned tracker display mode most urgent percentage number inner outer",
        "legacy": [],
        "body": """
<p>The menu bar icon shows one tool at a time, as two rings and a percentage.</p>
<h2>Smart or pinned</h2>
<ul>
<li><strong>Smart (most urgent)</strong> is the default. The menu bar shows whichever tool is closest to its limit, so the most pressing one is always in view.</li>
<li><strong>Pin Tracker</strong> keeps one tool in the menu bar no matter what.</li>
</ul>
<p>To switch, open the popover and click the display button in its footer, then choose <strong>Smart (most urgent)</strong> or a tool under <strong>Pin Tracker</strong>. The button only appears once you have two or more tools connected.</p>
<h2>Reading the rings</h2>
<ul>
<li><strong>Inner ring:</strong> the short window, the limit you're likely to hit first, like Claude's 5-hour window.</li>
<li><strong>Outer ring:</strong> the longer window, like Claude's 7-day window. Tools with only one limit show one ring.</li>
<li><strong>Dots:</strong> the <a href="/help/pace-dot">pace dots</a>, one on each ring.</li>
<li><strong>Percentage:</strong> the inner ring's value.</li>
</ul>
""",
    },
    {
        "slug": "pace-dot",
        "topic": "using-tokenomics",
        "title": "What does the pace dot mean?",
        "summary": "The pace dot shows where your usage would be if you'd used your limit evenly since it last reset. If your fill is past the dot, you're on track to run out early.",
        "keywords": "pace dot dots marker even pace ahead behind burning on track missing hidden why no",
        "legacy": [],
        "body": """
<p>A bar at 60% doesn't tell you much on its own. Whether that's fine depends on how far into the window you are.</p>
<p>The pace dot marks where your usage would sit if you'd spread it evenly since the window opened. Two hours into a five-hour window, the dot sits at 40%.</p>
<ul>
<li><strong>Fill short of the dot:</strong> you're using less than an even pace, so you have room.</li>
<li><strong>Fill past the dot:</strong> you're burning faster than an even pace and will run out before the window resets if you keep going.</li>
</ul>
<h2>Why some bars have no dot</h2>
<p>The dot only appears on limits that reset on a schedule. A balance that doesn't reset on a timetable has no pace to compare against. Runway, ElevenLabs and Cursor also hide the dot when their service doesn't report a billing date, because without that the math would be a guess.</p>
""",
    },
    {
        "slug": "usage-alerts",
        "topic": "using-tokenomics",
        "title": "How do usage alerts work, and how do I change them?",
        "summary": "Tokenomics notifies you when a tool crosses 80% by default, and again if you hit the limit. Change the threshold, the window or turn alerts off in Settings → Notifications.",
        "keywords": "alert alerts notification notifications threshold warn warning 80 percent limit hit ready again reset banner disable turn off mute window short long both",
        "legacy": [],
        "body": """
<p>Each tool alerts you once when its usage crosses a threshold, so you can slow down before you hit a wall.</p>
<ul>
<li><strong>The warning</strong> reads like “Claude 5-Hour Window at 80%”, then “You may hit your limit soon” and when it resets.</li>
<li><strong>If you keep going and reach 100%</strong>, you get one more: “You've hit your usage limit.”</li>
<li><strong>When a limit you hit resets</strong>, Tokenomics tells you it's “ready again”.</li>
</ul>
<p>Click an alert to open that tool's tab.</p>
<h2>Changing them</h2>
<p>Open Settings (the gear in the popover) → <strong>Notifications</strong>:</p>
<ul>
<li><strong>Per tool:</strong> switch alerts on or off, and set the threshold from 50% to 100% in steps of 10. The default is on, at 80%.</li>
<li><strong>Alert Window:</strong> choose whether the <strong>Short</strong> window (like Claude's 5-hour), the <strong>Long</strong> one (like the 7-day), or <strong>Both</strong> can trigger alerts. The default is Short.</li>
</ul>
<p>After an alert, that tool won't alert again until its usage drops 10 points below your threshold, usually when the window resets.</p>
<h2>Not getting any alerts?</h2>
<p>macOS asks for permission the first time an alert is due, not during setup. If you said no, Settings → Notifications shows “Notifications are disabled in System Settings.” with a link to turn them back on.</p>
<p>Alerts come from the Mac app. The browser extension doesn't send notifications.</p>
""",
    },
    {
        "slug": "widgets",
        "topic": "using-tokenomics",
        "title": "How do I add and set up the desktop widgets?",
        "summary": "Right-click your desktop, choose Edit Widgets and search for Tokenomics. Small shows one tool; medium, large and extra large show more.",
        "keywords": "widget widgets desktop notification center add small medium large extra large edit select provider smart overflow in app",
        "legacy": [],
        "body": """
<ol>
<li>Right-click your desktop and choose <strong>Edit Widgets</strong>.</li>
<li>Search for <strong>Tokenomics</strong> and pick the <strong>AI Usage</strong> widget.</li>
<li>Choose a size and drag it where you want it.</li>
</ol>
<h2>The sizes</h2>
<ul>
<li><strong>Small:</strong> one tool as two rings. By default it shows whichever tool is closest to its limit. To pick a specific one, right-click the widget, choose <strong>Edit “AI Usage”</strong>, and set <strong>Provider</strong>.</li>
<li><strong>Medium:</strong> up to 3 tools as bars.</li>
<li><strong>Large:</strong> up to 7.</li>
<li><strong>Extra large</strong> (macOS 27 and later): up to 14.</li>
</ul>
<p>If you have more tools than fit, the widget says “+3 in app” (or however many). Widgets follow the tab order you set in the popover. On the small widget, the inner ring is the short window and the outer ring is the long one, the same as the menu bar.</p>
<p>Widgets show what the Mac app last read. If they look out of date, see <a href="/help/widget-not-updating">why a widget shows old numbers</a>.</p>
""",
    },
    {
        "slug": "add-hide-reorder",
        "topic": "using-tokenomics",
        "title": "How do I add, hide, reorder or remove a tool?",
        "summary": "Add tools from Settings → Setup providers…, hide them with their switch in AI Connections, and reorder tabs by holding ⌘ and dragging.",
        "keywords": "add hide show remove disconnect reorder order drag rearrange tab tabs ai connections setup providers toggle switch found not tracked yet banner",
        "legacy": [],
        "body": """
<h2>Add a tool</h2>
<p>Open Settings (the gear in the popover) → <strong>Setup providers…</strong> to run guided setup for any tool. You can also go to <strong>AI Connections</strong> and click <strong>Connect</strong> next to a tool.</p>
<p>If Tokenomics notices a tool on your Mac that you haven't added, the popover shows a banner like “Found Cursor — not tracked yet.” Click <strong>Add</strong> to set it up.</p>
<h2>Hide a tool</h2>
<p>In <strong>AI Connections</strong>, switch a tool off to hide it from the menu bar, popover and widgets. With the browser extension and Mac app 2.10.5 or later, this also hides it in the extension (<a href="/help/mac-app-and-extension">how they sync</a>).</p>
<h2>Reorder tabs</h2>
<p>Hold <strong>⌘</strong> and drag a tab in the popover. Widgets and the browser extension follow the same order.</p>
<h2>Remove a tool completely</h2>
<ul>
<li><strong>Stability AI and Runway:</strong> switch the tool off in AI Connections, then click <strong>Disconnect</strong> to delete its API key.</li>
<li><strong>Coding tools</strong> (Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor): Tokenomics only reads their sign-in, so there's nothing to disconnect. Switch them off to hide them, or sign out in the tool itself.</li>
<li><strong>Web tools:</strong> switch the site off in the extension's settings.</li>
</ul>
""",
    },
    {
        "slug": "group-by-company",
        "topic": "using-tokenomics",
        "title": "What does Group by Company do?",
        "summary": "It puts each company's products under one tab, like ChatGPT and Codex CLI under OpenAI, with a section for each inside. It's on by default.",
        "keywords": "group by company brand tabs openai google combine separate per provider layout",
        "legacy": [],
        "body": """
<p>Some companies have more than one product with its own limit: OpenAI has ChatGPT and Codex CLI, and Google has the Gemini app and Gemini CLI.</p>
<p>With <strong>Group by Company</strong> on, each company gets one tab in the popover, with a section for each product inside and a plan label on each. Medium and large widgets and the Pin Tracker list group the same way.</p>
<p>Turn it off in Settings → <strong>Group by Company</strong> to give every product its own tab.</p>
<p>Why the products are separate at all: see <a href="/help/two-meters">why ChatGPT and Gemini show two meters</a>.</p>
""",
    },
    {
        "slug": "updates",
        "topic": "using-tokenomics",
        "title": "How do updates work?",
        "summary": "The Mac app checks for updates automatically and tells you when one is ready; you choose when to install it. The extension updates itself through the Chrome Web Store.",
        "keywords": "update updates updating version new sparkle check homebrew brew upgrade latest which version",
        "legacy": [],
        "body": """
<p>The Mac app checks for new versions automatically. When one is ready you get a “Tokenomics Update Available” notification, and Settings shows a blue dot on <strong>Update Available</strong>. Click it to install.</p>
<p>To check yourself, open Settings and click <strong>Check for Updates</strong>. Your current version is shown next to it.</p>
<p>Installed with Homebrew? The app updates itself the same way, so there's no need to run <code>brew upgrade</code>.</p>
<p>The browser extension updates through the Chrome Web Store, usually within a few hours of a release. When an update needs access to a new site, Chrome asks you to approve it first.</p>
<p>What changed in each version is on the <a href="https://github.com/rob-stout/Tokenomics/releases" target="_blank" rel="noopener">changelog</a>.</p>
""",
    },
    {
        "slug": "launch-at-login",
        "topic": "using-tokenomics",
        "title": "Does Tokenomics start when I log in?",
        "summary": "Only if you turn on Launch at Login in Settings. Otherwise it's gone from the menu bar after a restart until you open it again.",
        "keywords": "launch login startup start automatically restart reboot open boot gone disappeared missing menu bar",
        "legacy": [],
        "body": """
<p>Not unless you ask it to. Open Settings (the gear in the popover) and turn on <strong>Launch at Login</strong>.</p>
<p>If it's off, Tokenomics disappears from the menu bar after you restart your Mac. Open it from your Applications folder to bring it back.</p>
<p>Widgets keep showing the last numbers while the app isn't running. Tapping a widget's refresh button opens the app.</p>
""",
    },
    {
        "slug": "shortcuts-and-settings",
        "topic": "using-tokenomics",
        "title": "Keyboard shortcuts, Siri and text size",
        "summary": "⌘R refreshes, ⌘-drag reorders tabs, and Siri and Shortcuts can check or refresh your usage. Text size is in Settings.",
        "keywords": "keyboard shortcut shortcuts hotkey command siri spotlight apple shortcuts app intents text size font bigger smaller compact large refresh quit",
        "legacy": [],
        "body": """
<h2>Keyboard shortcuts in the popover</h2>
<ul>
<li><strong>⌘R</strong> refreshes every tool.</li>
<li><strong>⌘-drag</strong> a tab to reorder it.</li>
<li><strong>⌘Q</strong> quits Tokenomics.</li>
</ul>
<h2>Siri, Spotlight and Shortcuts</h2>
<p>Tokenomics adds three actions you can use in the Shortcuts app, Spotlight or with Siri:</p>
<ul>
<li><strong>Check Usage</strong>, for example “Check Tokenomics usage”.</li>
<li><strong>Refresh Usage</strong>: “Refresh Tokenomics”.</li>
<li><strong>Show Usage</strong>: “Show Tokenomics”.</li>
</ul>
<h2>Text size</h2>
<p>Settings → <strong>Text Size</strong> offers Compact, Medium and Large. The popover resizes to fit.</p>
""",
    },
    {
        "slug": "extra-usage-and-credits",
        "topic": "reading-numbers",
        "title": "What are Extra Usage and Credits Balance?",
        "summary": "Extra Usage shows how much of your monthly extra-usage spending limit you've used on Claude. Credits Balance shows prepaid credits on your OpenAI account.",
        "keywords": "extra usage credits balance spend spending money dollars monthly limit max plan overage paid",
        "legacy": [],
        "body": """
<p><strong>Extra Usage</strong> appears on the Claude tab when your plan has extra usage turned on. It shows how much you've spent of your monthly extra-usage limit, like “$12.40 / $50.00”. Extra usage is what Anthropic bills once you go past your plan's included limits.</p>
<p><strong>Credits Balance</strong> appears on the Codex CLI section when your OpenAI account has prepaid credits, showing the remaining balance.</p>
<p>Both only appear when the service reports them. If you don't see them, your account doesn't have them.</p>
""",
    },
    {
        "slug": "toolbar-icon",
        "topic": "using-tokenomics",
        "title": "What's the number on the extension's toolbar icon?",
        "summary": "It's the short-window usage of whichever site is closest to its limit, or the one you pin. Change it from the popup's Toolbar Display menu.",
        "keywords": "toolbar icon badge number percentage extension chrome pin smart toolbar display",
        "legacy": [],
        "body": """
<p>The extension's toolbar icon shows a percentage: the short-window usage of one site.</p>
<ul>
<li><strong>Smart</strong> (the default) shows whichever site is closest to its limit.</li>
<li><strong>Pin</strong> a site to always show that one.</li>
</ul>
<p>Open the popup and use the <strong>Toolbar Display</strong> menu to switch.</p>
""",
    },
    {
        "slug": "chatgpt-plan",
        "topic": "reading-numbers",
        "title": "ChatGPT shows the wrong plan or limit. Can I fix it?",
        "summary": "Usually Tokenomics reads ChatGPT's real limits. If it can't, it counts your messages against your plan's limits, and you can set the plan yourself in the extension's settings.",
        "keywords": "chatgpt plan wrong limit incorrect free plus pro team override auto detect messages estimate estimated",
        "legacy": [],
        "body": """
<p>Normally the extension reads ChatGPT's own limits, the same numbers ChatGPT uses, so the plan doesn't matter.</p>
<p>When those aren't available, it falls back to counting the messages you send and comparing them with your plan's published limits. That count only includes messages sent from this browser, and the reading is marked as estimated.</p>
<p>If the plan is wrong in that case, open the extension's settings, find <strong>ChatGPT</strong>, and change <strong>Auto-detect</strong> to <strong>Free</strong>, <strong>Plus</strong>, <strong>Pro</strong> or <strong>Team</strong>.</p>
""",
    },
    {
        "slug": "leonardo-setup",
        "topic": "browser-extension",
        "title": "How do I set up Leonardo?",
        "summary": "Visit app.leonardo.ai with the extension installed and it picks up your sign-in, or paste a Leonardo API key in the extension's settings.",
        "keywords": "leonardo api key token setup credits tokens renewal reset",
        "legacy": [],
        "body": """
<p>There are two ways:</p>
<ol>
<li><strong>Open app.leonardo.ai</strong> in your browser while signed in. The extension picks up the access your browser already has and reads your token balance from then on.</li>
<li><strong>Paste a Leonardo API key</strong> in the extension's settings, under Leonardo. You create one at app.leonardo.ai under API Access; Leonardo may require an API plan for that.</li>
</ol>
<p>Leonardo doesn't always report when your tokens renew. See <a href="/help/renewal-dates">why a renewal date might be missing</a>.</p>
""",
    },
    {
        "slug": "renewal-dates",
        "topic": "reading-numbers",
        "title": "Why don't Leonardo or Suno show a renewal date yet?",
        "summary": "Those services report your balance but not when it renews. Tokenomics learns your renewal day the first time it sees your balance refill.",
        "keywords": "renewal renew reset date countdown missing leonardo suno credits refill monthly daily",
        "legacy": [],
        "body": """
<p>Leonardo (on some plans) and Suno tell Tokenomics your balance but not when it renews.</p>
<p>So the extension watches for the refill: when your plan's balance jumps up without you buying more, it notes the day and counts forward from it each month. Until it has seen one refill, there's no countdown.</p>
<p>Suno's free plan renews daily rather than monthly, which this method can't tell apart, so the countdown may be wrong on a free Suno account.</p>
""",
    },

    # ── Fixing problems ──────────────────────────────────────────────
    {
        "slug": "menu-bar-not-updating",
        "topic": "fixing-problems",
        "title": "Why did my menu bar numbers stop updating?",
        "summary": "Tokenomics checks less often when you're not actively coding, and catches up when you open the popover. Older versions could stop checking entirely; update to 2.10.5.",
        "keywords": "stale old not updating stopped frozen menu bar numbers updated ago refresh polling idle every minutes how often",
        "legacy": [],
        "body": """
<p>Tokenomics checks each tool on its own schedule, from every minute (Codex CLI and Gemini CLI, which it reads from files on your Mac) to every 10 minutes (Stability AI). To go easy on each service, it checks less often when you haven't used Claude Code for about 9 minutes, at most every 15 minutes, and speeds back up as soon as you're active again.</p>
<ul>
<li><strong>Opening the popover</strong> refreshes anything older than its usual schedule, so what you see there is current.</li>
<li><strong>The refresh button</strong> (or <strong>⌘R</strong>) checks every tool right away.</li>
<li><strong>The line at the bottom of the popover</strong> says when the numbers were last updated, like “Updated 2m ago”.</li>
</ul>
<p>In versions before 2.10.5, Tokenomics stopped checking altogether after 9 minutes without Claude Code activity, until you clicked refresh. If you're on an older version, <a href="/help/updates">update</a> to fix that.</p>
<p>Still stuck on old numbers? A service may be rate-limiting Tokenomics (<a href="/help/rate-limited">what that looks like</a>), or a sign-in may have expired (<a href="/help/sign-in-expired">how to fix it</a>). Web tools also need your browser open; see <a href="/help/mac-app-and-extension">how the Mac app and extension work together</a>.</p>
""",
    },
    {
        "slug": "gemini-cli-numbers",
        "topic": "reading-numbers",
        "title": "How are Gemini CLI numbers counted, and which plan should I pick?",
        "seo_title": "Gemini CLI Usage Limits: How Requests and Tokens Are Counted",
        "summary": "Google doesn't report Gemini CLI usage, so Tokenomics counts today's requests from Gemini CLI's own files on your Mac, against the daily limits of the plan you choose.",
        "keywords": "gemini cli plan free standard enterprise requests tokens today estimate estimated daily limit midnight pacific reset choose plan google ai",
        "legacy": [],
        "body": """
<p>Google doesn't offer a way to look up Gemini CLI usage. So Tokenomics counts it itself, from the session files Gemini CLI saves on your Mac, and compares that with the daily limits of your plan. That makes it an estimate, and the popover says “Estimated from your local Gemini CLI sessions”.</p>
<p>You'll see two bars: <strong>Requests Today</strong> and <strong>Tokens Today</strong>. Both reset at midnight Pacific time, when Google's daily limits do.</p>
<h2>Choosing your plan</h2>
<p>The plan sets the limits Tokenomics counts against:</p>
<div class="doc-table-wrap">
<table class="doc-table">
<thead><tr><th scope="col">Plan</th><th scope="col">Requests per day</th></tr></thead>
<tbody>
<tr><td>Free</td><td>1,000</td></tr>
<tr><td>Standard</td><td>1,500</td></tr>
<tr><td>Enterprise</td><td>2,000</td></tr>
</tbody>
</table>
</div>
<p>Tokenomics asks the first time you open the Gemini CLI tab (“Choose your Gemini plan”). To change it later, click the plan badge on the tab, or use the plan control on the Gemini CLI row in Settings → AI Connections.</p>
<p>The Gemini app at gemini.google.com is separate; the browser extension reads its own limits. See <a href="/help/two-meters">why Gemini shows two meters</a>.</p>
""",
    },
    {
        "slug": "copilot-meters",
        "topic": "reading-numbers",
        "title": "What do the GitHub Copilot meters show?",
        "seo_title": "GitHub Copilot Premium Requests in Tokenomics, Explained",
        "summary": "Paid Copilot plans show your premium requests used this month. Free plans show your monthly chat and code-completion allowances.",
        "keywords": "copilot github premium requests chat completions free pro business enterprise plan monthly reset unlimited zero 0",
        "legacy": [],
        "body": """
<ul>
<li><strong>Paid plans</strong> (Pro, Pro+, Business, Enterprise): one bar, <strong>Premium Requests</strong>, with how many you've used of your monthly allowance, like “75 / 300 used”, and when it resets. Chat and code completions are unlimited on these plans, so they don't need a meter. If your premium requests are unlimited, the bar says “Unlimited”.</li>
<li><strong>Free plan:</strong> two bars, <strong>Chat</strong> and <strong>Completions</strong>, showing how much of each monthly allowance you've used.</li>
</ul>
<p>Paid plans showed 0% or nothing in versions before 2.10.5. <a href="/help/updates">Update</a> if that's what you see.</p>
<p>Tokenomics reads these through the GitHub CLI's sign-in. If Copilot isn't connected yet, see the <a href="/setup#copilot">setup guide</a>.</p>
""",
    },
    {
        "slug": "rate-limited",
        "topic": "fixing-problems",
        "title": "What does “Couldn't load usage data — check back in a few minutes” mean?",
        "summary": "The service asked Tokenomics to slow down. It keeps showing your last numbers and tries again after a short wait. Here's that and the other error messages.",
        "keywords": "error rate limit limited 429 couldnt load usage data check back server error network connection couldnt read something went wrong message",
        "legacy": [],
        "body": """
<p>That message means the service is rate-limiting Tokenomics: it's been asked to check less often for a while. Tokenomics keeps showing the last numbers it got, waits, and tries again. Each retry waits longer: 5 minutes, then 10, 20, 40, up to an hour, unless the service says exactly when to come back.</p>
<p>You don't need to do anything. Hover over the “Updated…” line at the bottom of the popover to see “Rate limited — showing most recent available data.”</p>
<h2>Other messages</h2>
<ul>
<li><strong>No network connection:</strong> your Mac is offline. It retries when you're back.</li>
<li><strong>Server error (503)</strong> or another number: the service had a problem. It usually clears on its own.</li>
<li><strong>Couldn't read usage data:</strong> the service sent something Tokenomics didn't recognize, often after the service changed. Check for an <a href="/help/updates">update</a>, and <a href="/help/report-a-problem">tell us</a> if it continues.</li>
<li><strong>Not signed in</strong> or <strong>Session expired:</strong> see <a href="/help/sign-in-expired">signing back in</a>.</li>
<li><strong>API key no longer works:</strong> your Stability AI or Runway key was revoked or expired. Click <strong>Update key</strong> and paste a new one.</li>
<li><strong>Keychain access needed:</strong> see <a href="/help/keychain-prompt">the Keychain prompt</a>.</li>
</ul>
""",
    },
    {
        "slug": "keychain-prompt",
        "topic": "fixing-problems",
        "title": "Why does macOS ask for my password to read my Claude Code sign-in?",
        "summary": "Claude Code keeps its sign-in in your Mac's Keychain. Click Allow Access, enter your Mac password, and choose Always Allow so macOS stops asking.",
        "keywords": "keychain password prompt allow access always allow claude code sign-in permission asks twice dialog macos didnt allow",
        "legacy": [],
        "body": """
<p>Claude Code stores its sign-in in your Mac's Keychain. macOS protects it, so Tokenomics has to ask before reading it. The Claude tab says “Tokenomics needs permission to read your Claude Code sign-in.”</p>
<ol>
<li>Click <strong>Allow Access</strong>.</li>
<li>macOS asks for your Mac password. It may ask twice.</li>
<li>Choose <strong>Always Allow</strong> each time, so it doesn't ask again.</li>
</ol>
<p>If you see “macOS didn't allow access. Try again.”, the prompt was cancelled or closed. Click <strong>Allow Access</strong> again.</p>
<p>Tokenomics only reads that sign-in to ask Anthropic for your usage. It never changes it or copies it anywhere.</p>
""",
    },
    {
        "slug": "sign-in-expired",
        "topic": "fixing-problems",
        "title": "It says “authentication expired” or “Session expired”. How do I fix it?",
        "summary": "Your coding tool's sign-in ran out. Sign in to the tool again, or click Reconnect to be walked through it.",
        "keywords": "authentication expired session expired reconnect sign in again login logged out token re-authenticate not signed in",
        "legacy": [],
        "body": """
<p>Tokenomics uses the sign-in your coding tools keep on your Mac. When that sign-in expires, Tokenomics can't read your usage until you sign in again.</p>
<ul>
<li><strong>Easiest:</strong> click <strong>Reconnect</strong> on that tab. Guided setup walks you through signing in, and Tokenomics notices automatically when you're done.</li>
<li><strong>Or do it yourself:</strong> sign in to the tool the usual way (for Claude Code, run <code>claude</code> in Terminal and sign in), then click refresh in the popover.</li>
</ul>
<p>For Stability AI and Runway, the message is “API key no longer works”. Click <strong>Update key</strong> and paste a new key.</p>
<p>For web tools in the browser extension, just sign back in to the site.</p>
""",
    },
    {
        "slug": "setup-errors",
        "topic": "fixing-problems",
        "title": "Guided setup showed an error. What do I do?",
        "summary": "What each guided-setup message means and how to get past it: Terminal permission, Homebrew prompts, sign-in not detected, and more.",
        "keywords": "setup error guided onboarding homebrew cancelled download permission denied terminal automation didnt detect check now couldnt find install failed",
        "legacy": [],
        "body": f"""
<ul>
<li><strong>“Tokenomics needs permission to open Terminal.”</strong> Setup uses Terminal to install tools and sign you in. Click <strong>Open System Settings</strong>, go to Privacy &amp; Security → Automation, and allow Tokenomics to control Terminal. Then click <strong>Try again</strong>.</li>
<li><strong>“Homebrew install was cancelled. You'll need to approve the admin prompt to continue.”</strong> Installing Homebrew needs your Mac password. Run the step again and enter it when Terminal asks.</li>
<li><strong>“Homebrew couldn't download.”</strong> Check your internet connection and try again.</li>
<li><strong>“The install didn't complete.”</strong> Something went wrong inside Homebrew. Run <code>brew doctor</code> in Terminal to see what, then try again.</li>
<li><strong>“We didn't detect a sign-in. If you finished signing in, tap Check now.”</strong> Finish signing in in Terminal or your browser, then click <strong>Check now</strong>.</li>
<li><strong>“Sign-in was cancelled.”</strong> Start the step again when you're ready.</li>
<li><strong>“We couldn't find … after installing it.”</strong> Click to re-run detection. If it still fails, quit and reopen Tokenomics.</li>
<li><strong>“Permission denied writing to …”</strong> Click <strong>Clear cache &amp; retry</strong>.</li>
<li><strong>“That key didn't work. Check it and try again.”</strong> Stability AI or Runway turned down the API key you pasted. Copy the whole key again, or make a new one. If it says it couldn't reach the provider instead, check your connection.</li>
<li><strong>“We couldn't securely store your sign-in.”</strong> macOS blocked the Keychain. Open Keychain Access and check that your login keychain is unlocked.</li>
</ul>
<p>Every install step also has a way to skip it if you already have that tool. The <a href="{SETUP}">setup guide</a> walks through each tool, and <a href="/help/what-setup-installs">what setup installs</a> lists everything it adds.</p>
""",
    },
    {
        "slug": "what-setup-installs",
        "topic": "browser-extension",
        "title": "What does guided setup install on my Mac?",
        "summary": "Only what each coding tool needs: Homebrew, Node.js, the tool itself, and for Claude Code a line that adds it to your PATH. Terminal opens for installs and sign-ins.",
        "keywords": "install installs homebrew node npm terminal password admin zprofile path local bin tokenomics-cli codex gemini claude code gh github cli what does setup change",
        "legacy": [],
        "body": f"""
<p>Guided setup installs a coding tool only if you don't already have it. Each step has a way to skip it.</p>
<ul>
<li><strong>Homebrew</strong>, the standard Mac package manager, if Copilot, Codex CLI or Gemini CLI needs it. This opens Terminal and asks for your Mac password.</li>
<li><strong>Node.js</strong>, through Homebrew, for Codex CLI and Gemini CLI.</li>
<li><strong>Codex CLI and Gemini CLI</strong>, into a folder of their own: <code>~/.tokenomics-cli</code>.</li>
<li><strong>GitHub CLI (<code>gh</code>)</strong>, through Homebrew, for Copilot.</li>
<li><strong>Claude Code</strong>, using Anthropic's own installer, into <code>~/.local/bin</code>. Setup also adds one line to <code>~/.zprofile</code> (or <code>~/.bash_profile</code>) so your Terminal can find it.</li>
</ul>
<p>Signing in to these tools happens in Terminal or your browser, the same as if you set them up yourself. During Claude Code's sign-in, macOS may ask whether it can access folders like Music or Photos. It doesn't need them, so it's safe to say no.</p>
<p>Uninstalling Tokenomics doesn't remove these tools, because you may use them on their own. See <a href="/help/uninstall">how to uninstall</a> if you want them gone too. Step-by-step details for each tool are in the <a href="{SETUP}">setup guide</a>.</p>
""",
    },
    {
        "slug": "safari",
        "topic": "browser-extension",
        "title": "I use Safari. How do I track my web tools?",
        "summary": "Tokenomics for Safari is in App Store review. Until it's out, use the extension in Chrome, Brave, Arc or another Chromium browser alongside Safari.",
        "keywords": "safari apple app store tokenomics for safari default browser web extension mac app store",
        "legacy": [],
        "body": """
<p><strong>Tokenomics for Safari</strong>, a free Mac App Store app with a Safari extension inside, is in App Store review. We'll link it here as soon as it's out.</p>
<p>Until then, the browser extension runs in Chrome and other Chromium browsers (Brave, Arc, Vivaldi, Opera). You don't have to switch browsers for everything: sign in to the AI sites you want tracked in that browser, and the extension reads them there. The Mac app picks up the numbers either way.</p>
<p>Your coding tools (Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor) don't need a browser at all; the Mac app reads them directly.</p>
""",
    },
    {
        "slug": "widget-not-updating",
        "topic": "fixing-problems",
        "title": "Why does my widget show old numbers or “Open Tokenomics to sync”?",
        "summary": "Widgets show what the Mac app last read. If the app isn't running, they can't update. Tap the widget's refresh button to open the app and refresh.",
        "keywords": "widget old stale not updating out of date open tokenomics to sync refresh blank empty",
        "legacy": [],
        "body": """
<p>Widgets don't fetch anything themselves. They show the numbers the Mac app last read.</p>
<ul>
<li><strong>“Open Tokenomics to sync”</strong> means the widget has nothing yet. Open Tokenomics once and it fills in.</li>
<li><strong>Old numbers</strong> usually mean the app isn't running, for example after a restart. Turn on <a href="/help/launch-at-login">Launch at Login</a> so it's always there.</li>
<li><strong>The refresh button</strong> on a widget asks the app to refresh, and opens it in the background if it's quit.</li>
</ul>
<p>Web tools also depend on the browser extension; with your browser closed, they show the last reading, marked with its age. See <a href="/help/mac-app-and-extension">how the Mac app and extension work together</a>.</p>
""",
    },
    {
        "slug": "codex-numbers",
        "topic": "reading-numbers",
        "title": "Why don't my Codex CLI numbers change, or say “No active session”?",
        "seo_title": "Codex CLI Usage Not Updating? Why It Says “No Active Session”",
        "summary": "Codex CLI's numbers come from the logs Codex writes on your Mac, so they only change after you use Codex. ChatGPT in the browser doesn't move them.",
        "keywords": "codex cli no active session not updating zero 0 stale weekly 5 hour openai logs",
        "legacy": [],
        "body": """
<p>Tokenomics reads Codex CLI's usage from the session logs Codex saves on your Mac. Each time you use Codex, it records your current limits there.</p>
<ul>
<li><strong>“No active session”</strong> means there's no recent Codex session to read from. Run Codex once and the numbers appear.</li>
<li><strong>Numbers not moving:</strong> they only change after you use Codex again.</li>
<li><strong>ChatGPT on the web</strong> has its own, separate limits, read by the browser extension. Using ChatGPT doesn't change Codex CLI's numbers. See <a href="/help/two-meters">why there are two meters</a>.</li>
</ul>
""",
    },
    {
        "slug": "report-a-problem",
        "topic": "fixing-problems",
        "title": "How do I report a bug or send feedback?",
        "summary": "Open Settings → Report Bugs / Feedback, or email hello@trytokenomics.com. Include the tool, your plan and your Tokenomics version.",
        "keywords": "bug report feedback issue github email contact support problem feature request",
        "legacy": [],
        "body": """
<p>In the Mac app, open Settings → <strong>Report Bugs / Feedback</strong>. It opens a new issue on GitHub. Or email <a href="mailto:hello@trytokenomics.com">hello@trytokenomics.com</a>.</p>
<p>These help us fix it faster:</p>
<ul>
<li>Which tool it's about, and your plan on it (for example Claude Max or ChatGPT Plus).</li>
<li>Your Tokenomics version, shown next to <strong>Check for Updates</strong> in Settings, and the extension version if it involves the browser.</li>
<li>What you expected to see and what you saw. A screenshot helps.</li>
</ul>
<p>Never include API keys or passwords.</p>
""",
    },
    {
        "slug": "check-claude-usage",
        "topic": "reading-numbers",
        "title": "How do I check my Claude usage?",
        "seo_title": "How to Check Your Claude Usage Limits (3 Ways)",
        "summary": "On claude.ai, open Settings → Usage. In Claude Code, type /usage. Or keep it in your menu bar with Tokenomics, so you see it before you hit the limit.",
        "keywords": "check claude usage limit how much left remaining settings usage page /usage command claude code session weekly reset tracker monitor",
        "legacy": [],
        "body": """
<p>Claude shows your usage in two places, and Tokenomics adds a third that's always visible.</p>
<ul>
<li><strong>On claude.ai or the Claude desktop app:</strong> open Settings → Usage (or go to <code>claude.ai/settings/usage</code>). <strong>Current session</strong> is your 5-hour window; the weekly bar is your 7-day window. Each shows when it resets.</li>
<li><strong>In Claude Code:</strong> type <code>/usage</code> to see the same limits and their reset times without leaving the terminal.</li>
<li><strong>In your menu bar, with Tokenomics:</strong> both windows sit in the menu bar as rings, with a <a href="/help/pace-dot">pace dot</a> that shows whether you're on track to run out early. <a href="/help/usage-alerts">Usage alerts</a> warn you before you hit the limit, so you don't have to remember to check.</li>
</ul>
<p>Chats and Claude Code draw from the same limits, so all three show the same numbers. <a href="/help/claude-usage-limits">How the 5-hour and weekly windows work</a>.</p>
""",
    },
    {
        "slug": "check-copilot-usage",
        "topic": "reading-numbers",
        "title": "How do I check my GitHub Copilot premium requests?",
        "seo_title": "How to Check Your GitHub Copilot Premium Request Usage",
        "summary": "See premium requests in your GitHub Copilot settings, your editor, or your Mac menu bar with Tokenomics. The allowance resets on the 1st of each month (UTC).",
        "keywords": "check github copilot premium requests usage how many left monthly allowance reset settings billing ide tracker",
        "legacy": [],
        "body": """
<ul>
<li><strong>On GitHub:</strong> your Copilot settings page on github.com shows premium requests used this month. The billing pages break it down further.</li>
<li><strong>In your editor:</strong> Copilot's status menu in supported editors shows your usage too.</li>
<li><strong>In your menu bar, with Tokenomics:</strong> paid plans get a <strong>Premium Requests</strong> bar, like “75 / 300 used”, with a <a href="/help/pace-dot">pace dot</a> so you can tell if you'll run out before the month ends. Free plans get Chat and Completions bars instead. <a href="/help/copilot-meters">What the Copilot meters show</a>.</li>
</ul>
<p>Premium request allowances reset on the 1st of each month at midnight UTC.</p>
<p>Tokenomics reads Copilot through the GitHub CLI's sign-in. If it isn't connected yet, see the <a href="/setup#copilot">setup guide</a>.</p>
""",
    },
]
