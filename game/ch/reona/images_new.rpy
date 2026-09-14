# =============================================================================
# reona — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("reona", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ reona_blowjob01 = [
    reona_blow_03,
    reona_blow_04,
    reona_blow_05
]

$ reona_hottub = [
    reona_hottub05,
    reona_hottub06
]