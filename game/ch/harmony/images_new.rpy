# =============================================================================
# harmony — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("harmony", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

    harmony_blowjob01 = [
        "ev2/harmony/blow_03.jpg",
        "ev2/harmony/blow_04.jpg",
        "ev2/harmony/blow_05.jpg"
    ]

    harmony_hottub = [
        "ev2/harmony/hottub04.jpg",
        "ev2/harmony/hottub05.jpg"
    ]