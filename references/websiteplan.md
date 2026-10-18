# Task: Build the Mountain Wave website (GitHub Pages)

This repo (`unity-sites`) hosts the website for **Mountain Wave**, my small indie game
studio. It holds a company landing page plus a page per game, including each game's
privacy policy (required by Google Play and Unity Analytics). The first game is
**Bumper Block**. More games will be added later, so make adding one easy.

Propose a plan and file structure first, then build.

## Structure
- `/` - Company landing page: Mountain Wave logo, a short "about" blurb, an
  "Our Games" section with a card per game (key art thumbnail, name, one-line pitch,
  link to the game page), and a contact email in the footer.
- `/bumperblock/` - Game page: hero key art, short description, a few screenshots
  or art images, a "Coming soon to Android" note (store link placeholder for later),
  and a footer link to the privacy policy.
- `/bumperblock/privacy/` - Privacy policy as its own page with a "Last updated" date.
  This URL goes in the Play Console and in the game's settings, so it must never move.

## Requirements
- Use **Jekyll** (built into GitHub Pages, no build step on my side). Shared layouts
  for company pages, game pages, and policy pages. Drive "Our Games" from a data file
  (e.g. `_data/games.yml`) so a new game = one folder + one data entry.
- All internal links must work both at `https://ventiduke.github.io/unity-sites/`
  and on a future custom domain (use `relative_url` / `baseurl` correctly).
- **Company look:** match the logo: warm cream paper background, black ink, an elegant
  serif. Simple and calm.
- **Game page look:** each game can have its own accent styling. Bumper Block's should
  feel like its pixel-art world (greens, rust, bright vehicle colors) while staying
  readable. Images must render crisp (`image-rendering: pixelated` for pixel art).
- Mobile-friendly, fast, no tracking scripts or cookies on the site itself.
- Make a favicon from the logo (the mountains and wave, without the text).
- Optimize images for the web (resized and compressed copies; keep originals out of
  the published site if large).
- Add a `README.md` explaining how to add a new game and a new policy page.

## Assets I'm providing
- `mountain-wave-logo.png`
- `keyart_stadium.png`, `gameplay_closeup.png`, `arena_overview.png`
- Privacy policy text (below). Format it nicely, don't change its meaning.
- Contact email: [FILL IN]

## Copy
- Draft the company blurb and the Bumper Block description; keep them short, and flag
  them for my review. Game summary: a top-down demolition derby where you drive a
  scrappy kart through an overgrown stadium, ramming cars until clumps of them pop.

## Privacy policy text
[PASTE YOUR POLICY TEXT HERE]

## When done
Tell me exactly how to enable GitHub Pages for this repo (Settings > Pages > branch),
the final URLs for the home page, game page, and privacy page, and anything I need to fill in.
