// Cloudflare Pages middleware: keeps every page's version label current.
//
// Pages carry a hard-coded label like "v2.10.4 · macOS 14+" (class js-version).
// As an HTML page is served, this swaps in the latest GitHub release, so search
// engines, link previews and visitors without JavaScript all see the right
// version, and no scheduled job has to commit version bumps.
//
// public/_routes.json limits this to HTML pages; images, scripts and fonts never
// run it. Cloudflare asks GitHub at most about once an hour (the same cached call
// /api/latest-version makes). Nothing about the visitor is stored or forwarded.
// If GitHub can't be reached, the page is served unchanged.

const RELEASE_URL = "https://api.github.com/repos/rob-stout/Tokenomics/releases/latest";

async function latestVersion(): Promise<string | null> {
  try {
    const res = await fetch(RELEASE_URL, {
      headers: { Accept: "application/vnd.github+json", "User-Agent": "trytokenomics-site" },
      cf: { cacheTtl: 3600, cacheEverything: true },
    });
    if (!res.ok) return null;
    const data = (await res.json()) as { tag_name?: string };
    const m = data.tag_name?.match(/^v?(\d+\.\d+\.\d+)$/);
    return m ? m[1] : null;
  } catch {
    return null;
  }
}

export const onRequest: PagesFunction = async (context) => {
  const response = await context.next();
  const isHtml = (response.headers.get("content-type") || "").includes("text/html");
  if (context.request.method !== "GET" || !isHtml) return response;

  const version = await latestVersion();
  if (!version) return response;

  return new HTMLRewriter()
    .on(".js-version", {
      element(el) {
        el.setInnerContent(`v${version} · macOS 14+`);
      },
    })
    .transform(response);
};
