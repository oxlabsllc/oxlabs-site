# OX Labs — Marketing Site

Single-page static marketing site for OX Labs. Plain HTML, CSS, and vanilla JavaScript — no frameworks, no build step. Made for GitHub Pages.

```
/
├── index.html        # the whole site (single page)
├── css/style.css     # all styles
├── js/main.js        # nav, scroll reveals, contact form
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

## 2. Wire up the contact form (Formspree)

The form currently points at a placeholder endpoint and **will not deliver messages** until you swap in a real form ID.

1. Sign up at [formspree.io](https://formspree.io) (free tier is fine to start).
2. Create a new form — Formspree gives you an endpoint like `https://formspree.io/f/abcdwxyz`.
3. In `index.html`, find the form tag and replace `YOUR_FORM_ID`:

   ```html
   <form class="contact-form" id="contact-form" action="https://formspree.io/f/abcdwxyz" method="POST" ...>
   ```

4. Push the change. Submit the form once from the live site — Formspree asks you to confirm your email the first time, and after that submissions arrive in your inbox.

The form includes a hidden `_gotcha` honeypot field for spam; leave it in place.

**Also update the placeholder contact info** (it appears in the contact section, footer, and the error message in `js/main.js`):

- Email: `al@oxlabs.com`
- Phone: `(713) 555-0134` — this is a fictional placeholder number; replace it or delete the phone links entirely.

## 3. Add a custom domain later

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
- The only external requests are Google Fonts (IBM Plex Sans/Mono) and Formspree on submit.
- The dashboard card in the hero is an illustrative mock — well names, operators, and amounts are fictional.
