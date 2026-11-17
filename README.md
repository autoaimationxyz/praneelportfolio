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

- `index.html`: hero, What I do (six services), milestones, work experience, work samples, case studies, clients (with Instagram links), skills, about.
- `performance.html`: FB & Google Ad campaign (90 days): weekly bifurcation of leads by channel, estimated vs actual.
- `case-studies.html`: project stories.
- `work.html`, `sector-*.html`: work by sector; collection pages (`revcore-autos.html`, `signature-global.html`, `creator-agencies.html`, `kapiva.html`, …).
- `revcore-autos.html`: 19 YouTube thumbnails with links to the videos.
- `contact.html`: contact details and a message form that opens your email app.

Work data lives in `portfolio.js` (videos), `creatives.js` (designs) and `content.js` (thumbnails). Media files stay in `assets/` and never go to GitHub.
