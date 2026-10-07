# Crowd Cannon: Lanes

A lane-based spin on [Crowd Cannon](https://github.com/pippopoppi/crowd-cannon). Same drag-to-aim cannon, tiny blue soldiers, red bases and champions, but the lower battlefield is split into five lanes with different jobs.

**Play it:** https://pippopoppi.github.io/crowd-cannon-lanes/

No install, no build step, no dependencies. One HTML page plus one JavaScript file on an HTML5 canvas.

## How it works

- **Fight lane (middle).** Enemies always funnel into it and march toward your sandbag line. Your soldiers only fight there.
- **Card lanes.** Cards drift toward you like soldiers. The first soldier to touch one applies it to your whole army: ×2, ×3, ×5, +N are good, −N and ÷2 are bad. Cards that reach your line do nothing.
- **Prize lane.** A crate with a hit counter drifts down. Every soldier that hits it knocks one off. Reach zero and you get a reward: a new weapon (Spread, Volley), a new soldier type (Runner, Shield, Archer), or a bonus (rapid fire, army ×2, line repair, coins).
- **Open field.** Above the lanes you get the original gates, walls, moving gates and speed boosts, then the red bases. Destroy them all to win.

Weapons and soldier types are unlocked only through crates. Coins still buy upgrades in the shop. Progress is saved in the browser.

## Controls

Drag (or arrow keys) to move the cannon. Keys `1` and `2` or the on-screen buttons deploy the Knight and the Bomber.

## Running locally

```
python3 -m http.server 8000
```

then open http://localhost:8000/.

## Regenerating the share image

```
python3 tools/make_og.py
```

needs Pillow and writes `og.png` and `icon-180.png`.

## Licence

MIT
