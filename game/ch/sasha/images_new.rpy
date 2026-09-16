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

    #sasha_mast01 = [
    #         sasha_mast_01,
    #         sasha_mast_02,
    #         sasha_mast_03,
    #         sasha_mast_02,
    #     ]

    sasha_mast02 = [
            "ev2/sasha/mast_04.jpg",
            "ev2/sasha/mast_05.jpg",
        ]

    sasha_blow_couch = [
            "ev2/sasha/blow_couch01.jpg",
            "ev2/sasha/blow_couch02.jpg",
        ]

    sasha_blow = [
            "ev2/sasha/blow_03.jpg",
            "ev2/sasha/blow_04.jpg",
        ]

    sasha_rimjob = [
            "ev2/sasha/blow_03.jpg",
            "ev2/sasha/blow_04.jpg",
        ]

    sasha_blow_hand = [
            "ev2/sasha/blow_08.jpg",
            "ev2/sasha/blow_09.jpg",
        ]

    sasha_cowgirl_jump = [
            "ev2/sasha/cowgirl_pussy07.jpg",
            "ev2/sasha/cowgirl_pussy06.jpg",
            "ev2/sasha/cowgirl_pussy05.jpg",
            "ev2/sasha/cowgirl_pussy06.jpg",
        ]

    sasha_cowgirl_speed = [
            "ev2/sasha/cowgirl_pussy08.jpg",
            "ev2/sasha/cowgirl_pussy09.jpg",
        ]

    sasha_cowgirl_rough = [
            "ev2/sasha/cowgirl_pussy02.jpg",
            "ev2/sasha/cowgirl_pussy03.jpg",
        ]

    sasha_beach_cowgirl = [
            "ev2/sasha/cowgirl_beach01.jpg",
            "ev2/sasha/cowgirl_beach02.jpg",
            "ev2/sasha/cowgirl_beach03.jpg",
            "ev2/sasha/cowgirl_beach02.jpg",
        ]

    sasha_beach_cowgirl_rough = [
            "ev2/sasha/cowgirl_beach04.jpg",
            "ev2/sasha/cowgirl_beach05.jpg",
        ]  

    sasha_hottub = [
            "ev2/sasha/hottub03.jpg",
            "ev2/sasha/hottub04.jpg",
        ]  
