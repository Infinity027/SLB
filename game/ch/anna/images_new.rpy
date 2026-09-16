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

    # anna_blowjob01 = [
    #     "ev2/anna/blow/03",
    #     "ev2/anna/blow/04",
    #     "ev2/anna/blow/05"
    # ]

    # anna_blowjob02 = [
    #     "ev2/anna/blow/06",
    #     "ev2/anna/blow/07"
    # ]

    anna_hottub = [
        "ev2/anna/hottub03.jpg",
        "ev2/anna/hottub04.jpg"
    ]