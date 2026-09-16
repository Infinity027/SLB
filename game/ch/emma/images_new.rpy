# =============================================================================
#  SASHA — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/emma/<dress>/<expression>.png
#  The dress is chosen automatically from emma.get_clothes() (her activity),
#  so every `show emma <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/emma/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================

init python:
    register_flat_character("emma", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

    emma_hottub = [
        "ev2/emma/hottub03.jpg",
        "ev2/emma/hottub04.jpg"
    ]