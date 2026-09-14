# =============================================================================
#Claire — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/claire/<dress>/<expression>.png
#  The dress is chosen automatically from claire.get_clothes() (her activity),
#  so every `show claire <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/claire/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================
#scene expression make_anim(claire_hottub, time=0.4, loop=True)
init python:
    register_flat_character("claire", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ claire_blowjob01 = [
    claire_blow_03,
    claire_blow_04,
    claire_blow_05
]

$ claire_blowjob02 = [
    claire_blow_06,
    claire_blow_07
]

$ claire_hottub01 = [
    claire_hottub03,
    claire_hottub04
]

$ claire_hottub02 = [
    claire_hottub05,
    claire_hottub06
]

$ claire_hottub03 = [
    claire_hottub10,
    claire_hottub11
]