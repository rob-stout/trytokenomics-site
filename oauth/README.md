# Tokenomics OAuth Workers

Cloudflare Workers that handle OAuth callbacks for Tokenomics.app. The Workers
exchange an authorization code for an access token using a client secret that
lives only on Cloudflare — never in the macOS bundle. The token is then
handed off to the macOS app via the `tokenomics://` URL scheme.

## Currently shipped

- **GitHub Copilot** — `github-worker.js` → `trytokenomics.com/oauth/github`

## One-time setup (per provider)

### 1. Register the OAuth App with the provider

For GitHub:
1. Go to <https://github.com/settings/applications/new>
2. Application name: `Tokenomics`
3. Homepage URL: `https://trytokenomics.com`
4. Authorization callback URL: `https://trytokenomics.com/oauth/github`
5. Save and copy the **Client ID** and **Client Secret**.

### 2. Configure the Worker

```bash
cd oauth
wrangler login                                           # one-time
wrangler secret put GITHUB_OAUTH_CLIENT_SECRET           # paste secret
echo "GITHUB_OAUTH_CLIENT_ID = \"<id>\"" >> wrangler.toml \
  || wrangler secret put GITHUB_OAUTH_CLIENT_ID          # paste id
wrangler deploy github-worker.js \
  --name tokenomics-github-oauth \
  --route 'trytokenomics.com/oauth/github*'
```

### 3. Embed the client_id in the macOS app

Add the GitHub Client ID as a constant in `CopilotConnector.swift` (or read it
from a build setting). The client_id is public; only the secret needs to stay
on the Worker.

## Testing locally

```bash
cd oauth
wrangler dev github-worker.js --port 8787
# Then visit http://localhost:8787/?code=test&state=foo
```

## How the macOS app receives the token

The Worker redirects the browser to `tokenomics://oauth/github?token=...`.
macOS routes that to Tokenomics via the URL scheme registered in
`Tokenomics/Resources/Info.plist`. The app's URL handler stores the token in
Keychain and notifies any in-flight `CopilotConnector`.
