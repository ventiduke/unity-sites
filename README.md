# unity-sites

The Mountain Wave website: a company landing page plus a page (and privacy policy) for each
game. It's a plain Jekyll site that GitHub Pages builds by itself, with no build step on your side.

Live at **https://ventiduke.github.io/unity-sites/**

| Page | URL |
|---|---|
| Company home | https://ventiduke.github.io/unity-sites/ |
| Bumper Block | https://ventiduke.github.io/unity-sites/bumperblock/ |
| Bumper Block privacy policy | https://ventiduke.github.io/unity-sites/bumperblock/privacy/ |

## Layout of the repo

```
_config.yml              site title, contact email, url/baseurl, what not to publish
_data/games.yml          one entry per game: drives "Our Games" and each game page's header
_layouts/
  base.html              <head>, favicon; applies a game's theme when the page has `game:`
  company.html           company pages (cream paper, ink, serif)
  game.html              game pages: hero art, name, pitch, store link or "Coming soon"
  policy.html            policy pages, with a "Last updated" date
_includes/               game card, footer, responsive <picture> helper
assets/css/site.css      shared styles and the company look
assets/css/games/        one theme file per game (e.g. bumperblock.css)
assets/fonts/            self-hosted fonts (EB Garamond, Jersey 10; SIL OFL licenses alongside)
assets/img/              web-sized images, made by tools/make_images.py
index.html               company landing page
bumperblock/index.md     Bumper Block page
bumperblock/privacy/     Bumper Block privacy policy
favicon.svg, favicon-32.png, favicon.ico, apple-touch-icon.png
references/              original art and notes: kept in the repo, never published
tools/make_images.py     makes the web images from references/
```

The site loads nothing from other servers (fonts are self-hosted) and has no analytics,
tracking scripts or cookies.

## Turn on GitHub Pages (once)

1. On GitHub, open the repo, then **Settings > Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main` and the folder to `/ (root)`, then **Save**.
4. Wait a minute or two. The address appears at the top of that page.

## Add a new game

Say the game is "Sky Hop" with the slug `skyhop` (the slug becomes its URL: `/skyhop/`).

1. **Art.** Put the original key art in `references/` (e.g. `references/skyhop_keyart.jpg`).
   Add a line to `JOBS` in `tools/make_images.py`:
   ```python
   "skyhop/keyart": dict(src="skyhop_keyart.jpg", widths=[640, 1280, 1920]),
   ```
   Then run `python3 tools/make_images.py` (needs `pip install pillow`). It writes
   `assets/img/skyhop/keyart-640.webp`, `-640.jpg` and so on.
2. **Data.** Add an entry to `_data/games.yml` (the file's comments explain each field):
   ```yaml
   - slug: skyhop
     name: Sky Hop
     pitch: One line about the game.
     image: /assets/img/skyhop/keyart
     image_widths: [640, 1280, 1920]
     image_alt: What the key art shows.
     pixel_art: false
     theme: skyhop          # leave out to use the plain company look
     platform: Android
     store_url: ""          # paste the store link once it's live
     privacy: true
   ```
   The game now shows up in "Our Games" on the home page.
3. **Page.** Create `skyhop/index.md`:
   ```markdown
   ---
   layout: game
   game: skyhop
   title: Sky Hop
   description: A sentence for search engines and link previews.
   ---
   A paragraph or two about the game, then any sections you like (## headings, lists...).
   ```
4. **Theme (optional).** Copy `assets/css/games/bumperblock.css` to `assets/css/games/skyhop.css`,
   rename `.theme-bumperblock` to `.theme-skyhop`, and change the colors and fonts.
5. **Privacy policy.** See the next section.

## Add a policy page

Policies use `layout: policy`. For a game's privacy policy, create `<slug>/privacy/index.md`:

```markdown
---
layout: policy
game: skyhop
title: Privacy Policy
description: How Sky Hop handles your data.
last_updated: 2026-10-18
permalink: /skyhop/privacy/
---

## What we collect

...
```

- The page title shows as "Sky Hop Privacy Policy", in the game's theme, with the date.
- Set `privacy: true` on the game in `_data/games.yml` so its footer links to the policy.
- Other policies (terms, a studio-wide policy) work the same way: pick a folder, set
  `permalink`, and leave out `game:` for the company look.
- **Never move or rename a policy that's already in a store listing.** Its URL is in the
  Play Console and in the game. Edit the text in place and update `last_updated`.

## Moving to a custom domain later

In `_config.yml` set `url` to the new domain (e.g. `https://mountainwave.games`) and `baseurl`
to `""`, add the domain under Settings > Pages > Custom domain, and update the privacy URLs in
the Play Console and in each game. All internal links use `relative_url`, so nothing else changes.

## Preview locally (optional)

```sh
gem install jekyll
jekyll serve
```

Then open http://localhost:4000/unity-sites/.
