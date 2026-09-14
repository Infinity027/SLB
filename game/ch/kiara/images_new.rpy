# =============================================================================
#Kiara — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/kiara/<dress>/<expression>.png
#  The dress is chosen automatically from kiara.get_clothes() (her activity),
#  so every `show kiara <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/kiara/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================
#scene expression make_anim(kiara_hottub, time=0.4, loop=True)
init python:
    register_flat_character("kiara", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ kiara_blowjob01 = [
    kiara_blow_03,
    kiara_blow_04,
    kiara_blow_05
]

$ kiara_blowjob02 = [
    kiara_blow_06,
    kiara_blow_07
]

$ kiara_pussy = [
    kiara_hottub05,
    kiara_hottub06
]

$ kiara_ass= [
    kiara_hottub10,
    kiara_hottub11
]