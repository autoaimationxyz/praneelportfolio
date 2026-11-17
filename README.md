# Praneel Mohan — Portfolio

Social Media & Performance Marketing · Meta & Google Ads · Client Servicing & Customer Success

Plain static site: HTML, CSS and vanilla JavaScript. No build step, no dependencies.

## Run it locally

```sh
cd praneel-portfolio
python3 -m http.server 8080
```

Open http://127.0.0.1:8080/

## Where the media lives (important)

**No images, videos, logos or the CV are in this GitHub repo.** They are ignored by
`.gitignore` and live only in the local `assets/` folder:

| Folder | What |
|---|---|
| `assets/videos/` | 33 portfolio videos (MP4) |
| `assets/posters/`, `assets/covers/` | Video posters and cover cards |
| `assets/creatives/` | Signature Global / Zeyar creatives |
| `assets/*.webp` | RevCore Autos thumbnails |
| `assets/sector-art/` | Section illustrations |
| `assets/logos/` | Brand logos |
| `assets/Praneel_Mohan_CV.pdf` | CV download (add this file) |

So when you deploy, upload from the **local folder** (which has the media), not from GitHub alone.

## Deploying (pick one)

1. **Netlify Drop (easiest)** — go to https://app.netlify.com/drop and drag the whole
   `praneel-portfolio` folder in. You get a live URL in a minute; add a custom domain
   (e.g. praneelmohan.com) in Site settings.
2. **Cloudflare Pages (direct upload)** — Workers & Pages → Create → Pages → Upload assets →
   drop the folder. Max 25 MB per file (the largest video is ~24 MB, so it fits).
3. **Netlify/Vercel CLI** from this folder: `npx netlify deploy --prod --dir .`

Re-deploy the same way whenever you change something. Code changes also go to GitHub
(`git add -A && git commit -m "..." && git push`), media never does.

## Pages

- `index.html` — hero, results, full experience timeline, case studies, brands, creative work, skills, about
- `performance.html` — 90-day Meta & Google Ads campaign (850 leads), week-by-week and by channel
- `case-studies.html` — 10 project stories
- `work.html`, `sector-*.html` — creative work by sector
- collection pages (`signature-global.html`, `revcore-autos.html`, `kapiva.html`, `zeyar.html`, …)
- `contact.html` — email / phone / WhatsApp / LinkedIn, form opens your email app (nothing is stored)

Built from the unused TLC — The Last Call venture site; the agency-only planner and services
pages are in `_archive-tlc/` (local only).
