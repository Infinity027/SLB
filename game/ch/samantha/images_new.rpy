
# =============================================================================
#  Samnatha — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("samnatha", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ samnatha_blowjob01 = [
    samnatha_blow_03,
    samnatha_blow_04,
    samnatha_blow_05
]

$ samnatha_blowjob02 = [
    samnatha_blow_06,
    samnatha_blow_07
]

$ samnatha_hottub = [
    samnatha_hottub02,
    samnatha_hottub03
]