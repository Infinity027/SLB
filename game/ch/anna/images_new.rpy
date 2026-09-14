# =============================================================================
# Anna — flat image system  (replaces the old split layeredimage)
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

init python:
    register_flat_character("anna", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ anna_blowjob01 = [
    anna_blow_03,
    anna_blow_04,
    cassidy_blow_05
]

$ cassidy_blowjob02 = [
    cassidy_blow_06,
    cassidy_blow_07
]

$ anna_hottub = [
    anna_hottub03,
    anna_hottub04
]