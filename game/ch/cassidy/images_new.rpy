# =============================================================================
# Cassidy — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/cassidy/<dress>/<expression>.png
#  The dress is chosen automatically from cassidy.get_clothes() (her activity),
#  so every `show cassidy <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/cassidy/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================
#scene expression make_anim(cassidy_hottub, time=0.4, loop=True)
init python:
    register_flat_character("cassidy", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ cassidy_blowjob01 = [
    cassidy_blow_03,
    cassidy_blow_04,
    cassidy_blow_05
]

$ cassidy_blowjob02 = [
    cassidy_blow_06,
    cassidy_blow_07
]

$ cassidy_hottub = [
    cassidy_hottub03,
    cassidy_hottub04
]