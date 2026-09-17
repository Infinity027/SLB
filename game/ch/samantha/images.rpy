init 1:
    layeredimage samantha:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=samantha)

        attribute idle null

        always:
            if_not ["halloween"]
            "samantha_backhair"
        always:
            if_any ["halloween"]
            "samantha_backhair_halloween"

        group acc_back auto if_not ["topless", "naked"]

        always:
            "samantha_body"

        attribute pubes

        attribute naked null

        attribute bottomless null
        group stockings auto when not (naked or bottomless)

        attribute topless null

        group necklace auto if_not ["collar"]

        attribute collar

        always:
            "samantha_head"

        attribute blush

        group exp auto:
            attribute normal default

        attribute tongue null
        attribute lips null
        always:
            "samantha_fronthair"

        group acc_head auto if_not ["topless", "naked"]

        group arm auto

        group handpos auto

        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute ring null
        group ring auto if_any ["ring"]

        group fx auto

    layeredimage samantha close:
        yalign 0.14
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=samantha)

        attribute idle null

        always:
            if_not ["halloween"]
            "samantha_close_backhair"
        always:
            if_any ["halloween"]
            "samantha_close_backhair_halloween"

        group acc_back auto if_not ["topless", "naked"]

        always:
            "samantha_close_body"

        attribute pubes

        attribute naked null

        attribute bottomless null
        group stockings auto when not (naked or bottomless)

        attribute topless null

        group necklace auto if_not ["collar"]

        attribute collar

        always:
            "samantha_close_head"

        attribute blush

        group exp auto:
            attribute normal default

        attribute tongue null
        attribute lips null

        always:
            "samantha_close_fronthair"

        group acc_head auto if_not ["topless", "naked"]

        group arm auto

        group handpos auto

        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute ring null
        group ring auto if_any ["ring"]

        group fx auto

    layeredimage samantha smartphone:
        always "samantha_smartphone"

    layeredimage samantha ending:
        attribute_function Pickers([OutfitPicker, EndingKidPicker], npc=samantha)

        attribute kid

        always:
            if_not "pregnant"
            "samantha_ending_bg"

        always:
            if_not "pregnant"
            "samantha_ending_bodies"

        attribute naked null

        group mike auto if_not ["pregnant"]:
            attribute swimsuit if_any ["swimsuit", "sexyswimsuit"]

        always:
            if_not "pregnant"
            "samantha_ending_fg"

    layeredimage samantha selfie:
        attribute_function Pickers([CollarPicker], npc=samantha)

        always "samantha_selfie_bg"
        always "samantha_selfie_base"

        group multiple:
            attribute clit null
            attribute tongue null
            attribute ears null
            attribute navel null

        attribute collar
        attribute cum
