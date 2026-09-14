
# =============================================================================
#  bree — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("bree", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ bree_blowjob01 = [
    bree_blow_03,
    bree_blow_04,
    bree_blow_05
]

$ bree_blowjob02 = [
    bree_blow_06,
    bree_blow_07
]

$ bree_hottub = [
    bree_hottub03,
    bree_hottub04,
    bree_hottub05,
    bree_hottub04
]