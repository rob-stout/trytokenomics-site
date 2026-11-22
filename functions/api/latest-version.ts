// Cloudflare Pages Function: trytokenomics.com/api/latest-version
//
// Returns { "tag": "v2.10.3" } for the latest GitHub release, so the site's
// version pills can update without the visitor's browser contacting GitHub
// (which would show GitHub the visitor's IP address). Cloudflare asks GitHub
// at most about once an hour; nothing about the visitor is stored or forwarded.

const RELEASE_URL = "https://api.github.com/repos/rob-stout/Tokenomics/releases/latest";

export const onRequestGet: PagesFunction = async () => {
  let tag: string | null = null;
  try {
    const res = await fetch(RELEASE_URL, {
      headers: { Accept: "application/vnd.github+json", "User-Agent": "trytokenomics-site" },
      cf: { cacheTtl: 3600, cacheEverything: true },
    });
    if (res.ok) {
      const data = (await res.json()) as { tag_name?: string };
      if (data.tag_name) tag = data.tag_name.replace(/^v?/, "v");
    }
  } catch {
    // Fall through: the page keeps its hard-coded version.
  }
  return new Response(JSON.stringify({ tag }), {
    status: tag ? 200 : 502,
    headers: { "Content-Type": "application/json", "Cache-Control": "public, max-age=3600" },
  });
};
