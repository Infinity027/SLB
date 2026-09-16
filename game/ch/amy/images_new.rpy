# =============================================================================
#  SASHA — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("amy", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

# $ amy_blowjob01 = [
#     amy_blow_03,
#     amy_blow_04,
#     amy_blow_05
# ]

    amy_blowjob02 = [
        "ev2/amy/blow/06.jpg",
        "ev2/amy/blow/07.jpg"
    ]

    amy_hottub = [
        "ev2/amy/hottub05.jpg",
        "ev2/amy/hottub06.jpg"
    ]