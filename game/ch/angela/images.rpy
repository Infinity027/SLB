init 1:
    layeredimage angela:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=angela)

        group position auto

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute collar

        attribute pubes

        always:
            "angela_ring"

        attribute lips null

        group acc_underwear auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group acc_boobs auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_boobs auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute naked null

        attribute bottomless null

        attribute topless null

        group hand auto variant "a" if_any ["a"]:
            attribute dropped default

        group handoutfit auto variant "a_dropped" if_all ["a", "dropped"] if_not ["topless", "naked"]
        group handoutfit auto variant "a_raised" if_all ["a", "raised"] if_not ["topless", "naked"]
        group handoutfit auto variant "a_pinch" if_all ["a", "pinch"] if_not ["topless", "naked"]

        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc_hand auto variant "a_dropped" if_all ["a", "dropped"] if_not ["topless", "naked"]
        group acc_handoutfit auto variant "a_pinch" if_all ["a", "pinch"] if_not ["topless", "naked"]

        group acc_neck auto variant "a" if_any ["a"]
        group acc_neck auto variant "b" if_any ["b"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]

        group glasses auto variant "a" if_any ["a"]
        group glasses auto variant "b" if_any ["b"]

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage angela close:
        yalign 0.03
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=angela)

        group position auto

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute collar

        attribute pubes

        always:
            "angela_close_ring"

        attribute lips null 

        group acc_underwear auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group acc_underwear auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group acc_boobs auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_boobs auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute naked null

        attribute bottomless null

        attribute topless null

        group hand auto variant "a" if_any ["a"]:
            attribute dropped default

        group handoutfit auto variant "a_dropped" if_all ["a", "dropped"] if_not ["topless", "naked"]
        group handoutfit auto variant "a_raised" if_all ["a", "raised"] if_not ["topless", "naked"]
        group handoutfit auto variant "a_pinch" if_all ["a", "pinch"] if_not ["topless", "naked"]

        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc_hand auto variant "a_dropped" if_all ["a", "dropped"] if_not ["topless", "naked"]
        group acc_handoutfit auto variant "a_pinch" if_all ["a", "pinch"] if_not ["topless", "naked"]

        group acc_neck auto variant "a" if_any ["a"]
        group acc_neck auto variant "b" if_any ["b"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]

        group glasses auto variant "a" if_any ["a"]
        group glasses auto variant "b" if_any ["b"]

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage angela smartphone:
        always "angela_smartphone"
