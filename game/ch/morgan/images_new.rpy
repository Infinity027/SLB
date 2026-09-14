
# =============================================================================
#  morgan — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/sasha/<dress>/<expression>.png
#  The dress is chosen automatically from sasha.get_clothes() (her activity),
#  so every `show sasha <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/sasha/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================

init python:
    register_flat_character("morgan", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ morgan_blowjob01 = [
    morgan_blow_03,
    morgan_blow_04,
    morgan_blow_05
]

$ morgan_blowjob02 = [
    morgan_blow_06,
    morgan_blow_07
]

$ morgan_hottub = [
    morgan_hottub03,
    morgan_hottub04,
    morgan_hottub05,
    morgan_hottub04
]