# SSP Card Cash website

Static website for SSP Card Cash, Lucknow. No build step is needed: Vercel serves the `site/` folder (see `vercel.json`).

## Deploy on Vercel
1. Import this repository in Vercel (Framework preset: **Other**).
2. Leave Build Command and Install Command empty. Output directory is set to `site` in `vercel.json`.
3. Add your domain in Vercel → Project → Settings → Domains.

## Edit content
Edit `generator/services.py`, `generator/locations.py`, `generator/pages.py`; settings (domain, phones, hours, map) are at the top of `generator/build.py`. Then rebuild:

```
cd generator
python3 pages.py ../site prod
```
Commit and push; Vercel redeploys automatically.

## Replace images
- Hero: `site/assets/img/hero-placeholder.svg` (and `generator/built_img/`)
- Locations: `generator/built_img/locations/<slug>.webp` (800×450), then rebuild.

## Contact form
Submissions are emailed to sspcardcash@gmail.com via FormSubmit. The first submission sends an activation email to that inbox; click **Activate** once.
