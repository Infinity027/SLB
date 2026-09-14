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
    cherie_blow_03,
    cherie_blow_04,
    cherie_blow_05
]

$ cherie_blowjob02 = [
    cherie_blow_06,
    cherie_blow_07
]

$ cherie_pussy = [
    cherie_hottub03,
    cherie_hottub04
]

$ cherie_ass01 = [
    cherie_hottub09,
    cherie_hottub10
]

$ cherie_ass02 = [
    cherie_hottub13,
    cherie_hottub14
]