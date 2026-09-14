
# =============================================================================
#  lexi — flat image system  (replaces the old split layeredimage)
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
    register_flat_character("lexi", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

$ lexi_blowjob01 = [
    lexi_blow_03,
    lexi_blow_04,
    lexi_blow_05
]

$ lexi_blowjob02 = [
    lexi_blow_06,
    lexi_blow_07
]

$ lexi01_hottub = [
    lexi_hottub03,
    lexi_hottub04,
    lexi_hottub05.
    lexi_hottub04
]

$ lexi02_hottub = [
    lexi_hottub08,
    lexi_hottub09,
    lexi_hottub10,
    lexi_hottub11,
    lexi_hottub10,
    lexi_hottub09
]
