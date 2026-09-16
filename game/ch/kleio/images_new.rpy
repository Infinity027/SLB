
# =============================================================================
#  kleio — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("kleio", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

    kleio_blowjob01 = [
        "ev2/kleio/blow_03.jpg",
        "ev2/kleio/blow_04.jpg",
        "ev2/kleio/blow_05.jpg"
    ]

    kleio_blowjob02 = [
        "ev2/kleio/blow_06.jpg",
        "ev2/kleio/blow_07.jpg"
    ]

    kleio01_hottub = [
        "ev2/kleio/hottub02.jpg",
        "ev2/kleio/hottub03.jpg",
        "ev2/kleio/hottub04.jpg",
        "ev2/kleio/hottub03.jpg"
    ]

    kleio02_hottub = [
        "ev2/kleio/hottub05.jpg",
        "ev2/kleio/hottub06.jpg",
        "ev2/kleio/hottub07.jpg",
        "ev2/kleio/hottub06.jpg"
    ]