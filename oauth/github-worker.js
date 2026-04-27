/**
 * Cloudflare Worker — GitHub OAuth callback for Tokenomics.app.
 *
 * Flow:
 *   1. Tokenomics.app opens https://github.com/login/oauth/authorize?client_id=...
 *      &scope=read:user&state=<random>&redirect_uri=https://trytokenomics.com/oauth/github
 *   2. User approves on GitHub.
 *   3. GitHub redirects back here with ?code=...&state=...
 *   4. This Worker exchanges the code for an access token (using the
 *      GITHUB_OAUTH_CLIENT_SECRET env var that lives only on the Worker —
 *      never in the macOS bundle).
 *   5. Redirects the browser to tokenomics://oauth/github?token=<token>&state=<state>.
 *   6. macOS picks up the URL via the `tokenomics://` scheme registered in
 *      Info.plist; the app's URL handler stores the token in Keychain.
 *
 * Required env vars (set via `wrangler secret put`):
 *   GITHUB_OAUTH_CLIENT_ID      — GitHub OAuth App client ID
 *   GITHUB_OAUTH_CLIENT_SECRET  — GitHub OAuth App client secret
 *
 * Deployment:
 *   $ wrangler deploy oauth/github-worker.js \
 *       --name tokenomics-github-oauth \
 *       --route 'trytokenomics.com/oauth/github*'
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // GitHub redirects here with ?code=...&state=...
    const code = url.searchParams.get('code');
    const state = url.searchParams.get('state') || '';
    const error = url.searchParams.get('error');

    // User denied authorization on GitHub.
    if (error) {
      return redirectToApp({ error, state });
    }

    if (!code) {
      return new Response('Missing authorization code', { status: 400 });
    }

    if (!env.GITHUB_OAUTH_CLIENT_ID || !env.GITHUB_OAUTH_CLIENT_SECRET) {
      return new Response('OAuth not configured on server', { status: 500 });
    }

    // Exchange the code for an access token.
    let tokenResp;
    try {
      tokenResp = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'User-Agent': 'tokenomics-oauth-worker'
        },
        body: JSON.stringify({
          client_id: env.GITHUB_OAUTH_CLIENT_ID,
          client_secret: env.GITHUB_OAUTH_CLIENT_SECRET,
          code
        })
      });
    } catch (err) {
      return redirectToApp({ error: 'token_exchange_failed', state });
    }

    if (!tokenResp.ok) {
      return redirectToApp({ error: `token_exchange_status_${tokenResp.status}`, state });
    }

    const payload = await tokenResp.json();
    const token = payload.access_token;

    if (!token) {
      const ghErr = payload.error || 'no_token_in_response';
      return redirectToApp({ error: ghErr, state });
    }

    // Hand the token off to Tokenomics via its custom URL scheme.
    return redirectToApp({ token, state });
  }
};

/**
 * Render a tiny HTML page that immediately redirects the browser to the
 * tokenomics:// scheme. Falls back to a clickable link if the scheme handler
 * doesn't pick it up automatically.
 */
function redirectToApp({ token, error, state }) {
  const params = new URLSearchParams();
  if (token) params.set('token', token);
  if (error) params.set('error', error);
  if (state) params.set('state', state);
  const appURL = `tokenomics://oauth/github?${params.toString()}`;

  const safeURL = appURL
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;');

  const body = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Returning to Tokenomics…</title>
  <meta http-equiv="refresh" content="0;url=${safeURL}" />
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
           background: #F3EFE5; color: #1C1C1E; text-align: center;
           padding: 80px 24px; }
    a    { color: #007AFF; text-decoration: none; font-weight: 500; }
    @media (prefers-color-scheme: dark) {
      body { background: #0E334D; color: #ECECF1; }
      a    { color: #5AC8FA; }
    }
  </style>
</head>
<body>
  <p>Returning to Tokenomics…</p>
  <p><a href="${safeURL}">Tap here if Tokenomics didn't open automatically.</a></p>
  <script>setTimeout(function () { window.location.href = ${JSON.stringify(appURL)}; }, 50);</script>
</body>
</html>`;

  return new Response(body, {
    status: 200,
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}
