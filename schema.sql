-- D1 schema for tokenomics-downloads
-- Apply once with: wrangler d1 execute tokenomics-downloads --file=./schema.sql --remote

CREATE TABLE IF NOT EXISTS downloads (
  id      INTEGER PRIMARY KEY AUTOINCREMENT,
  ts      TEXT    NOT NULL,         -- ISO-8601 UTC
  version TEXT    NOT NULL,         -- e.g. "2.8.7"
  channel TEXT    NOT NULL,         -- "web" | "brew" | "other"
  country TEXT    NOT NULL          -- ISO-2 from CF-IPCountry, "XX" if unknown
);

CREATE INDEX IF NOT EXISTS idx_downloads_ts      ON downloads(ts);
CREATE INDEX IF NOT EXISTS idx_downloads_version ON downloads(version);
CREATE INDEX IF NOT EXISTS idx_downloads_channel ON downloads(channel);
