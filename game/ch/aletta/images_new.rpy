
# =============================================================================
#  aletta — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/aletta/<dress>/<expression>.png
#  The dress is chosen automatically from aletta.get_clothes() (her activity),
#  so every `show aletta <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/aletta/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================

init python:
    register_flat_character("aletta", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
        "halloween"
    ])

    aletta_ofc_bj = [
    "ev2/aletta/office_bj03.jpg",
    "ev2/aletta/office_bj04.jpg",
    "ev2/aletta/office_bj05.jpg",
    "ev2/aletta/office_bj06.jpg",
    "ev2/aletta/office_bj07.jpg",
    ]

    aletta_ceo_fuck = [
    "ev2/aletta/ceo_fuck4.jpg",
    "ev2/aletta/ceo_fuck5.jpg",
    "ev2/aletta/ceo_fuck6.jpg",
    "ev2/aletta/ceo_fuck5.jpg",
    ]

    aletta_spank = [
    "ev2/aletta/spank8.jpg",
    "ev2/aletta/spank9.jpg",
    "ev2/aletta/spank9.jpg",
    
    ]

    aletta_ofc_titjob = [
    "ev2/aletta/titjob3.jpg",
    "ev2/aletta/titjob4.jpg",
    "ev2/aletta/titjob5.jpg",
    ]

    aletta_cowgirl_pussy = [
    "ev2/aletta/cowgirl03.jpg",
    "ev2/aletta/cowgirl04.jpg",
    "ev2/aletta/cowgirl05.jpg",
    ]

    aletta_cowgirl_pussy = [
    "ev2/aletta/cowgirl03.jpg",
    "ev2/aletta/cowgirl04.jpg",
    "ev2/aletta/cowgirl05.jpg",
    "ev2/aletta/cowgirl04.jpg",
    ]

    aletta_cowgirl_ass = [
    "ev2/aletta/cowgirl13.jpg",
    "ev2/aletta/cowgirl14.jpg",
    "ev2/aletta/cowgirl15.jpg",
    "ev2/aletta/cowgirl16.jpg",
    "ev2/aletta/cowgirl15.jpg",
    "ev2/aletta/cowgirl14.jpg",
    ]

    aletta_titjob = [
    "ev2/aletta/titjob03.jpg",
    "ev2/aletta/titjob04.jpg",
    "ev2/aletta/titjob05.jpg",
    "ev2/aletta/titjob04.jpg",
    ]

    aletta_doggy_ass = [
    "ev2/aletta/doggy11.jpg",
    "ev2/aletta/doggy12.jpg",
    "ev2/aletta/doggy13.jpg",
    "ev2/aletta/doggy12.jpg",
    ]

    aletta_doggy_pussy01 = [
    "ev2/aletta/doggy11.jpg",
    "ev2/aletta/doggy12.jpg",
    "ev2/aletta/doggy13.jpg",
    "ev2/aletta/doggy12.jpg",
    ]

    aletta_doggy_pussy02 = [
    "ev2/aletta/doggy02.jpg",
    "ev2/aletta/doggy03.jpg",
    "ev2/aletta/doggy04.jpg",
    "ev2/aletta/doggy03.jpg",
    ]

    aletta_miss_ass01 = [
    "ev2/aletta/missionary13.jpg",
    "ev2/aletta/missionary14.jpg",
    "ev2/aletta/missionary15.jpg",
    "ev2/aletta/missionary14.jpg",
    ]

    aletta_miss_ass02 = [
    "ev2/aletta/missionary16.jpg",
    "ev2/aletta/missionary17.jpg",
    "ev2/aletta/missionary18.jpg",
    "ev2/aletta/missionary17.jpg",
    ]

    aletta_miss_pussy = [
    "ev2/aletta/missionary03.jpg",
    "ev2/aletta/missionary04.jpg",
    "ev2/aletta/missionary05.jpg",
    "ev2/aletta/missionary04.jpg",
    ]

    aletta_ofc_cowgirl_pussy = [
    "ev2/aletta/ofc_cowgirl13.jpg",
    "ev2/aletta/ofc_cowgirl14.jpg",
    "ev2/aletta/ofc_cowgirl15.jpg",
    "ev2/aletta/ofc_cowgirl14.jpg",
    "ev2/aletta/ofc_cowgirl13.jpg"
    ]

    aletta_ofc_cowgirl_ass = [
    "ev2/aletta/ofc_cowgirl02.jpg",
    "ev2/aletta/ofc_cowgirl03.jpg",
    "ev2/aletta/ofc_cowgirl04.jpg",
    "ev2/aletta/ofc_cowgirl03.jpg",
    "ev2/aletta/ofc_cowgirl02.jpg"
    ]

    aletta_ofc_doggy_ass = [
    "ev2/aletta/ofc_doggy03.jpg",
    "ev2/aletta/ofc_doggy04.jpg",
    "ev2/aletta/ofc_doggy05.jpg",
    "ev2/aletta/ofc_doggy04.jpg",
    "ev2/aletta/ofc_doggy03.jpg"
    ]

    aletta_ofc_doggy_pussy = [
    "ev2/aletta/ofc_doggy12.jpg",
    "ev2/aletta/ofc_doggy13.jpg",
    "ev2/aletta/ofc_doggy12.jpg"
    ]

    aletta_res_bj = [
    "ev2/aletta/res_bj03.jpg",
    "ev2/aletta/res_bj04.jpg",
    "ev2/aletta/res_bj03.jpg"
    ]

    aletta_res_cunn = [
    "ev2/aletta/res_cunnilingus03.jpg",
    "ev2/aletta/res_cunnilingus04.jpg",
    "ev2/aletta/res_cunnilingus05.jpg",
    "ev2/aletta/res_cunnilingus03.jpg",
    ]

    aletta_h_fuck01 = [
    "ev2/aletta/h_fuck04.jpg",
    "ev2/aletta/h_fuck05.jpg",
    "ev2/aletta/h_fuck06.jpg",
    "ev2/aletta/h_fuck05.jpg",
    "ev2/aletta/h_fuck04.jpg",
    ]

    aletta_b_bj = [
    "ev2/aletta/b_fuck03.jpg",
    "ev2/aletta/b_fuck04.jpg",
    "ev2/aletta/b_fuck05.jpg",
    "ev2/aletta/b_fuck04.jpg",
    "ev2/aletta/b_fuck03.jpg",
    ]

    aletta_b_fuck01 = [
    "ev2/aletta/b_fuck10.jpg",
    "ev2/aletta/b_fuck11.jpg",
    "ev2/aletta/b_fuck12.jpg",
    "ev2/aletta/b_fuck11.jpg",
    "ev2/aletta/b_fuck10.jpg",
    ]

    aletta_b_fuck02 = [
    "ev2/aletta/b_fuck13.jpg",
    "ev2/aletta/b_fuck14.jpg",
    "ev2/aletta/b_fuck13.jpg",
    ]