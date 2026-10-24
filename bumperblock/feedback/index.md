---
layout: page
game: bumperblock
title: Feedback
description: Tell us what happened in Bumper Block: bugs, ideas, what was fun. The form takes a minute.
lede: You're playing a test build, and what you noticed is the most useful thing we can get.
# This page's URL is in the game (the Send feedback buttons). Do not move or rename it.
permalink: /bumperblock/feedback/
---
{%- assign game = site.data.games | where: "slug", page.game | first %}

## What helps most

- What was fun, and what wasn't.
- Anything that confused you: the repair colour, the pairs rule, a hint that got in the way.
- Where you died or got boxed in, and whether it felt fair.
- Anything that stuttered, and what phone you were on.
- Would you play again tomorrow?

Write as little or as much as you like. Everything on the form is optional.

<div class="feedback-form">
  <iframe src="{{ game.feedback_form }}?embedded=true" title="Bumper Block feedback form" loading="lazy" width="100%" height="1500">Loading the form…</iframe>
  <p class="feedback-form__alt">If the form doesn't show here, <a href="{{ game.feedback_form }}">open it in a new tab</a>.</p>
</div>

## Sending from the game

The Garage and the end-of-race screens have a **Send feedback** button. It posts your note to
this same form and adds, so you don't have to type them, the level you were on, your phone's
model and Android version, the game's version, and a one-line summary of your last run. You can
leave the device details out with the switch on that screen. What we keep and for how long is in
the [privacy policy]({{ '/bumperblock/privacy/' | relative_url }}).
