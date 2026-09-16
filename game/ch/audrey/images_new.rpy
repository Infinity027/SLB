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
    "ev2/audrey/blowjob2_1",
    "ev2/audrey/blowjob2_2",
    "ev2/audrey/blowjob2_3"
]

$ audrey_miss_pussy01 = [
    "ev2/audrey/missionary1",
    "ev2/audrey/missionary2"
]

$ audrey_miss_pussy02 = [
    "ev2/audrey/missionary3",
    "ev2/audrey/missionary4"
]

$ audrey_miss_pussy03 = [
    "ev2/audrey/missionary5",
    "ev2/audrey/missionary6"
]

$ audrey_hottub = [
    "ev2/audrey/hottub03",
    "ev2/audrey/hottub04"
]