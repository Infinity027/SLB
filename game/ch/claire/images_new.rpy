# =============================================================================
#Claire — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/claire/<dress>/<expression>.png
#  The dress is chosen automatically from claire.get_clothes() (her activity),
#  so every `show claire <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/claire/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================
#scene expression make_anim(claire_hottub, time=0.4, loop=True)
init python:
    register_flat_character("claire", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "date",
        "sexydate",
        "swimsuit",
        "sport",
        "underwear",
        "naked",
    ])

    # claire_blowjob01 = [
    #     "ev2/claire/blow_03.jpg",
    #     "ev2/claire/blow_04.jpg",
    #     "ev2/claire/blow_05.jpg"
    # ]

    # claire_blowjob02 = [
    #     "ev2/claire/blow_06.jpg",
    #     "ev2/claire/blow_07.jpg"
    # ]

    claire_hottub01 = [
        "ev2/claire/hottub03.jpg",
        "ev2/claire/hottub04.jpg"
    ]

    claire_hottub02 = [
        "ev2/claire/hottub05.jpg",
        "ev2/claire/hottub06.jpg"
    ]

    claire_hottub03 = [
        "ev2/claire/hottub10.jpg",
        "ev2/claire/hottub11.jpg"
    ]