# =============================================================================
#  danny — flat image system  (replaces the old split layeredimage)
#
#  Talking sprites resolve to:   game/images/danny/<dress>/<expression>.png
#  The dress is chosen automatically from danny.get_clothes() (her activity),
#  so every `show danny <expression>` line keeps working unchanged.
#
#  Engine + expression list live in  game/flat_sprites.rpy
#  Drop your PNGs into the folders under game/images/danny/ (see _HOW_TO_FILL.md).
#
#  To revert to the old layered art, restore this file from git.
# =============================================================================

init python:
    register_flat_character("danny", [
        "casual",        # default outfit (REQUIRED — fallback for every other dress)
        "halloween",
    ])

init 1:
    layeredimage danny:
        attribute_function Pickers([OutfitPicker], npc=danny)
        attribute naked null
        always:
            if_not ["fist", "casual", "halloween"]
            "danny_body"
        always:
            if_any "naked"
            "danny_dick"
        attribute fist
        group outfit auto if_not ["fist", "naked"]
        group exp auto:
            attribute normal default null
        group acc auto variant "halloween" if_any "halloween"
        group acc auto
        group arm auto

    layeredimage danny close:
        attribute_function Pickers([OutfitPicker], npc=danny)
        yalign 0.0
        attribute naked null
        always:
            if_not ["fist", "casual", "halloween"]
            "danny_close_body"
        always:
            if_any "naked"
            "danny_close_dick"
        attribute fist
        group outfit auto if_not ["fist", "naked"]
        group exp auto:
            attribute normal default null
        group acc auto variant "halloween" if_any "halloween"
        group acc auto
        group arm auto

    layeredimage danny smartphone:
        always "danny_smartphone"

    layeredimage danny fight2:
        group lexi auto
        group die auto

    layeredimage danny corpse:
        group location auto