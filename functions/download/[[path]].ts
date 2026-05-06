// Cloudflare Pages Function: trytokenomics.com/download/*
//
// Routes:
//   /download/dmg                    → latest DMG
//   /download/dmg/latest             → latest DMG
//   /download/dmg/v2.8.7             → specific version DMG
//
// Behavior:
//   1. Resolve target version (cached GitHub API lookup for "latest")
//   2. Insert a row into D1 (timestamp, version, channel, country) — no PII
//   3. 302 redirect to the GitHub release asset
//
// Privacy: stores no IP, no User-Agent string, no cookies. Channel is
// bucketed to "brew" / "web" / "other" by coarse UA sniff. Country is the
// CF-IPCountry header (ISO-2). All other request data is discarded.

interface Env {
  DB: D1Database;
}

const REPO = "rob-stout/Tokenomics";

export const onRequestGet: PagesFunction<Env> = async (context) => {
  const { request, env, params } = context;

  const segments = Array.isArray(params.path)
    ? (params.path as string[])
    : params.path
      ? [params.path as string]
      : [];

  if (segments[0] !== "dmg") {
    return new Response("Not found", { status: 404 });
  }

  const requested = segments[1];
  let version: string | null = null;

  if (!requested || requested === "latest") {
    version = await resolveLatestVersion();
  } else if (/^v?\d+\.\d+(?:\.\d+)?(?:-[A-Za-z0-9.]+)?$/.test(requested)) {
    version = requested.replace(/^v/, "");
  }

  if (!version) {
    return new Response("Version not found", { status: 404 });
  }

  const channel = classifyChannel(request.headers.get("user-agent"));
  const country = request.headers.get("cf-ipcountry") || "XX";
  const ts = new Date().toISOString();

  // Fire-and-forget logging — never block the redirect on D1.
  context.waitUntil(
    env.DB.prepare(
      "INSERT INTO downloads (ts, version, channel, country) VALUES (?, ?, ?, ?)"
    )
      .bind(ts, version, channel, country)
      .run()
      .catch(() => {})
  );

  const target = `https://github.com/${REPO}/releases/download/v${version}/Tokenomics-${version}.dmg`;
  return Response.redirect(target, 302);
};

function classifyChannel(ua: string | null): "brew" | "web" | "other" {
  if (!ua) return "other";
  if (/Homebrew|curl|wget/i.test(ua)) return "brew";
  if (/Mozilla|Safari|Chrome|Firefox|Edge/i.test(ua)) return "web";
  return "other";
}

async function resolveLatestVersion(): Promise<string | null> {
  const apiUrl = `https://api.github.com/repos/${REPO}/releases/latest`;
  const cache = caches.default;
  const cacheKey = new Request(apiUrl, { method: "GET" });

  let response = await cache.match(cacheKey);
  if (!response) {
    response = await fetch(apiUrl, {
      headers: {
        "User-Agent": "tokenomics-download-counter",
        Accept: "application/vnd.github+json",
      },
      cf: { cacheTtl: 3600, cacheEverything: true },
    });
    if (response.ok) {
      const headers = new Headers(response.headers);
      headers.set("Cache-Control", "public, max-age=3600");
      const body = await response.clone().text();
      const cacheable = new Response(body, { status: 200, headers });
      await cache.put(cacheKey, cacheable);
    }
  }

  if (!response.ok) return null;
  const data = (await response.json()) as { tag_name?: string };
  if (!data.tag_name) return null;
  return data.tag_name.replace(/^v/, "");
}
