---
layout: game
game: bumperblock
title: Bumper Block
description: Bumper Block is a top-down demolition derby. Drive a scrappy kart through an overgrown stadium and ram cars until clumps of them pop. Coming soon to Android.
---
<!-- DRAFT COPY: for review -->

Grab the wheel of a scrappy kart and tear around a stadium the jungle took back. Your kart
never stops: you steer, brake and boost. Shove same-colored cars together, and when three
of a color touch while you're in the pile, **they pop**.

Every level hands you an order to fill before your kart falls apart. Meanwhile the arena
keeps filling with traffic, wrecks rust into junk, the police give chase, and the weather
turns.

## How it plays

- **Ram and match.** Push three cars of the same color together to pop the whole clump.
- **Chain it.** Pop clumps back to back for combos and bigger scores.
- **Keep moving.** Dodge the cops, shove through rain, snow and fog, and don't get boxed in.
- **Upgrade.** Spend scrap between runs in the Garage to build up your kart.

## Pick your driver

<ul class="drivers">
  {%- assign drivers = "Rabbit,Raccoon,Cat,Dog" | split: "," -%}
  {%- assign driver_widths = "360" | split: "," -%}
  {%- for d in drivers %}
  {%- assign file = d | downcase | prepend: "/assets/img/bumperblock/driver-" %}
  <li>
    {% include picture.html src=file widths=driver_widths alt=d sizes="(min-width: 760px) 200px, 45vw" class="pixel" %}
    <span>{{ d }}</span>
  </li>
  {%- endfor %}
</ul>
