
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

# $ alexis_blowjob01 = [
#     alexis_blow_03,
#     alexis_blow_04,
#     alexis_blow_05
# ]

# $ alexis_blowjob02 = [
#     alexis_blow_06,
#     alexis_blow_07
# ]

    alexis01_hottub = [
        "ev2/alexis/hottub03.jpg",
        "ev2/alexis/hottub04.jpg",
        "ev2/alexis/hottub05.jpg",
        "ev2/alexis/hottub06.jpg",
        "ev2/alexis/hottub05.jpg",
        "ev2/alexis/hottub04.jpg"
    ]

    alexis02_hottub = [
        "ev2/alexis/hottub09.jpg",
        "ev2/alexis/hottub10.jpg",
        "ev2/alexis/hottub11.jpg",
        "ev2/alexis/hottub10.jpg"
    ]