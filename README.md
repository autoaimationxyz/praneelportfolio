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

- `index.html`: the whole story on one page: hero with a reel player, results, what I do, case studies, a work strip, experience, toolkit, about and contact.
- `work.html`: every piece of work (videos, designs, thumbnails) with category filters and a viewer.
- `case-850-leads.html`, `case-uth-times.html`, `case-take1.html`, `case-revcore-autos.html`: case studies.
- `_redirects`: sends old page addresses from version 1 to the new pages (Netlify reads this automatically).

## Adding new work

Every piece lives in `js/data.js`. Add one entry per piece with `id`, `type` (`video`, `design` or `thumb`), `cat`
(`ads`, `realestate`, `automotive`, `thumbnails`, `brands`, `creators`, `stories`, `jewellery`), `title`, `role`,
`src`, `poster`, `w` and `h`. Put the media file in `assets/` (it stays off GitHub).
