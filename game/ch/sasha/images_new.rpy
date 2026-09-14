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
        "towel",         # after a shower
        "sleep",         # sleepwear
        "naked",
    ])


$ sasha_mast01 = [
        sasha_mast_01,
        sasha_mast_02,
        sasha_mast_03,
        sasha_mast_02,
    ]

$ sasha_mast02 = [
        sasha_mast_04,
        sasha_mast_05,
    ]

$ sasha_blow_couch = [
        sasha_blow_couch01,
        sasha_blow_couch02,
    ]

$ sasha_blow = [
        sasha_blow_03,
        sasha_blow_04,
    ]

$ sasha_rimjob = [
        sasha_blow_03,
        sasha_blow_04,
    ]

$ sasha_blow_hand = [
        sasha_blow_08,
        sasha_blow_09,
    ]

$ sasha_cowgirl_jump = [
        sasha_cowgirl_pussy07,
        sasha_cowgirl_pussy06,
        sasha_cowgirl_pussy05,
        sasha_cowgirl_pussy06
    ]

$ sasha_cowgirl_speed = [
        sasha_cowgirl_pussy08,
        sasha_cowgirl_pussy09
    ]

$ sasha_cowgirl_rough = [
        sasha_cowgirl_pussy02,
        sasha_cowgirl_pussy03
    ]

$ sasha_beach_cowgirl = [
        sasha_cowgirl_beach01,
        sasha_cowgirl_beach02,
        sasha_cowgirl_beach03,
        sasha_cowgirl_beach02,
    ]

$ sasha_beach_cowgirl_rough = [
        sasha_cowgirl_beach04,
        sasha_cowgirl_beach05
    ]  

$ sasha_hottub = [
        sasha_hottub03,
        sasha_hottub04
    ]  
