
# =============================================================================
#  alexis — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("alexis", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ alexis_blowjob01 = [
    alexis_blow_03,
    alexis_blow_04,
    alexis_blow_05
]

$ alexis_blowjob02 = [
    alexis_blow_06,
    alexis_blow_07
]

$ alexis01_hottub = [
    alexis_hottub03,
    alexis_hottub04,
    alexis_hottub05,
    alexis_hottub06,
    alexis_hottub05,
    alexis_hottub04
]

$ alexis02_hottub = [
    alexis_hottub09,
    alexis_hottub10,
    alexis_hottub11,
    alexis_hottub10
]