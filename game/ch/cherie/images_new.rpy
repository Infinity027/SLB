# =============================================================================
#Cherie — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/cherie/<dress>/<expression>.png
#  The dress is chosen automatically from cherie.get_clothes() (her activity),
#  so every `show cherie <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/cherie/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================
#scene expression make_anim(cherie_hottub, time=0.4, loop=True)
init python:
    register_flat_character("cherie", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ cherie_blowjob01 = [
    "ev2/cherie/blow_03.jpg",
    "ev2/cherie/blow_04.jpg",
    "ev2/cherie/blow_05.jpg"
]

$ cherie_blowjob02 = [
    "ev2/cherie/blow_06.jpg",
    "ev2/cherie/blow_07.jpg"
]

$ cherie_pussy = [
    "ev2/cherie/hottub03.jpg",
    "ev2/cherie/hottub04.jpg"
]

$ cherie_ass01 = [
    "ev2/cherie/hottub09.jpg",
    "ev2/cherie/hottub10.jpg"
]

$ cherie_ass02 = [
    "ev2/cherie/hottub13.jpg",
    "ev2/cherie/hottub14.jpg"
]