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

    layeredimage danny fight:

        attribute lexi if_any "win":
            "danny_fight_lexi_happy"

        attribute lexi if_any "lose":
            "danny_fight_lexi_sad"

        attribute alone:
            "danny_fight_danny_win"

        attribute win:
            "danny_fight_danny_win"

        attribute win:
            "danny_fight_hero_lose"

        attribute lose:
            "danny_fight_hero_win"

    layeredimage danny fight2:
        group lexi auto
        group die auto

    layeredimage danny corpse:
        group location auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
