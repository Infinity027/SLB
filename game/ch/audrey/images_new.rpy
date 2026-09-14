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
    register_flat_character("sasha", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ audrey_blow = [
    audrey_blowjob2_1,
    audrey_blowjob2_2,
    audrey_blowjob2_3
]

$ audrey_miss_pussy01 = [
    audrey_missionary1,
    audrey_missionary2
]

$ audrey_miss_pussy02 = [
    audrey_missionary3,
    audrey_missionary4
]

$ audrey_miss_pussy03 = [
    audrey_missionary5,
    audrey_missionary6
]

$ audrey_hottub = [
    audrey_hottub03,
    audrey_hottub04
]