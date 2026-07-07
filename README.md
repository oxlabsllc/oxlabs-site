# OX Labs — Marketing Site

Single-page static marketing site for OX Labs. Plain HTML, CSS, and vanilla JavaScript — no frameworks, no build step. Made for GitHub Pages.

```
/
├── index.html        # the whole site (single page)
├── css/style.css     # all styles
├── js/main.js        # nav, scroll navigation
├── assets/           # favicon and any future images
└── README.md
```

## 1. Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `oxlabs-site`) and push this folder to it:

   ```bash
   git init
   git add .
   git commit -m "OX Labs marketing site"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/oxlabs-site.git
   git push -u origin main
   ```

2. In the repo on GitHub, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to "Deploy from a branch", pick the `main` branch and the `/ (root)` folder, then save.
4. After a minute or two the site is live at `https://YOUR_USERNAME.github.io/oxlabs-site/`.

Any push to `main` redeploys automatically.

## 2. Add a custom domain later

1. Buy a domain (e.g. `oxlabs.com`) from any registrar.
2. Create a file named `CNAME` (no extension) in the repo root containing just the domain:

   ```
   oxlabs.com
   ```

3. At your registrar, add DNS records:
   - **Apex domain** (`oxlabs.com`): four `A` records pointing to GitHub Pages' IPs — `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - **www subdomain**: a `CNAME` record pointing to `YOUR_USERNAME.github.io`
4. In the repo's **Settings → Pages**, enter the domain under **Custom domain** and check **Enforce HTTPS** once the certificate is issued (can take up to an hour).

## Notes

- No cookies, no analytics, no tracking — by design.
- The only external request is Google Fonts (EB Garamond).
- Contact is by email only (`oxlabsllc@gmail.com`).
