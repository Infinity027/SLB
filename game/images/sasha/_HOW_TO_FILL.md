# How to fill Sasha's images

Drop one PNG per file below. Naming must match **exactly** (the game calls these names).

## Pattern
```
images/sasha/<dress>/<expression>.png
```

## Dress folders (already created)
`casual` (REQUIRED — the fallback for everything), `date`, `sexydate`, `swimsuit`,
`sexyswimsuit`, `sport`, `underwear`, `towel`, `sleep`, `naked`, `topless`, `bottomless`

## Expression files needed in each dress folder
Start with the **core**: `normal.png`, `talkative.png`, `happy.png`, `smile.png`,
`sad.png`, `angry.png`, `annoyed.png`, `surprised.png`, `blush.png`, `flirt.png`

Then add: `sadsmile, vangry, upset, shy, embarrassed, wink, cry, shout, joke,
whining, confused, evil, bored, stuned, sleep` (all `.png`).

## Minimum to see her in-game
`images/sasha/casual/normal.png` alone will already show up everywhere (it's the
final fallback). Fill `casual/` fully first, then the other dresses.

## Fallback behaviour (so partial art never crashes)
For `show sasha <expr>` the engine tries, in order:
1. `images/sasha/<current_dress>/<expr>.png`
2. `images/sasha/<current_dress>/normal.png`
3. `images/sasha/casual/<expr>.png`
4. `images/sasha/casual/normal.png`
5. blank (no error)

The "current dress" is chosen automatically from her activity via `get_clothes()`.

## Events / CGs
Full scene images go in `game/ev/sasha/` or `game/ev2/sasha/` (not here).

## Sex scenes (later)
Pose art goes in `images/sasha/poses/<pose>/<face>.png` — a separate task.
```
```
