
# =============================================================================
#  minami — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("minami", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ minami_blowjob01 = [
    minami_blow_03,
    minami_blow_04,
    minami_blow_05
]

$ minami_blowjob02 = [
    minami_blow_06,
    minami_blow_07
]

$ minami_hottub = [
    minami_hottub03,
    minami_hottub04,
    minami_hottub05,
    minami_hottub04
]