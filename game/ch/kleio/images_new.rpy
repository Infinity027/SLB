
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

$ kleio_blowjob01 = [
    kleio_blow_03,
    kleio_blow_04,
    kleio_blow_05
]

$ kleio_blowjob02 = [
    kleio_blow_06,
    kleio_blow_07
]

$ kleio01_hottub = [
    kleio_hottub02,
    kleio_hottub03,
    kleio_hottub04,
    kleio_hottub03
]

$ kleio02_hottub = [
    kleio_hottub05,
    kleio_hottub06,
    kleio_hottub07,
    kleio_hottub06
]