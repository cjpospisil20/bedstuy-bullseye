# Pointing bedstuybullseye.io at this site

The domain was unregistered as of 2026-09-18 (RDAP returned 404). Two steps:
you buy it, then we point it here.

## 1. Buy the domain

Any registrar works. `.io` runs roughly **$35–70/year** — it is one of the
pricier TLDs, and renewal is usually higher than the first year, so check the
renewal price not just the intro price.

- **Cloudflare Registrar** — sells at wholesale cost, no markup, and its DNS is
  free and fast. Best value if you do not mind using Cloudflare for DNS.
- **Porkbun** — cheap, clean interface, free WHOIS privacy.
- **Namecheap** — fine, slightly pricier on `.io`.

Turn on **WHOIS privacy** (free at all three). Without it your name, address,
phone and email go into the public WHOIS record.

## 2. DNS records to create

At the registrar's DNS panel, add these **five** records:

| Type | Name / Host | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `cjpospisil20.github.io.` |

Those four A records are GitHub Pages' apex servers. All four — GitHub uses them
for redundancy.

## 3. Tell GitHub

Repo → **Settings → Pages → Custom domain** → enter `bedstuybullseye.io` → Save.
Then wait for the DNS check to pass and tick **Enforce HTTPS**.

Equivalent from the terminal:

```bash
gh api -X PUT repos/cjpospisil20/bedstuy-bullseye/pages \
  -f cname=bedstuybullseye.io -F https_enforced=true
```

## 4. Timing

DNS usually propagates in 10–30 minutes, occasionally up to 24 hours. The HTTPS
certificate is issued automatically by GitHub once the DNS check passes — that
can take another hour. **Do not enable "Enforce HTTPS" until the certificate has
been issued**, or the site will show a security warning in the meantime.

## Check it worked

```bash
dig +short bedstuybullseye.io          # should list the four 185.199.x.x addresses
curl -sI https://bedstuybullseye.io    # should return HTTP/2 200
```

## One caution

Adding the custom domain writes a `CNAME` file to the repo root. From that point
the `github.io` URL **redirects** to the custom domain — so if the domain ever
lapses or DNS breaks, the site becomes unreachable at both addresses until it is
fixed. Keep the renewal on auto-pay.
