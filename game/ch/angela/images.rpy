init 1:
    layeredimage angela:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=angela)


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


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute lips null
        group multiple auto variant piercings

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_a_usual when a and not (date or sexydate or wedding)
        group multiple auto variant piercings_a_date when a and date
        group multiple auto variant piercings_a_sexydate when a and sexydate
        group multiple auto variant piercings_a_wedding when a and wedding

        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_b_usual when b and not (date or wedding)
        group multiple auto variant piercings_b_date when b and date
        group multiple auto variant piercings_b_sexydate when b and sexydate
        group multiple auto variant piercings_b_wedding when b and wedding


        group acc_underwear auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group acc_underwear auto variant "b" if_any ["b"] if_not ["bottomless", "naked", "pregnant"]
        group acc_underwear auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group acc_boobs auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_boobs auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group underdress auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "bottomless", "naked"]
        group underdress auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "bottomless", "naked"]
        group underdress auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "bottomless", "naked"]
        group underdress auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "bottomless", "naked"]


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]


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
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=angela)


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


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute lips null
        group multiple auto variant piercings

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_a_usual when a and not (date or sexydate or wedding)
        group multiple auto variant piercings_a_date when a and date
        group multiple auto variant piercings_a_sexydate when a and sexydate
        group multiple auto variant piercings_a_wedding when a and wedding

        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_b_usual when b and not (date or wedding)
        group multiple auto variant piercings_b_date when b and date
        group multiple auto variant piercings_b_sexydate when b and sexydate
        group multiple auto variant piercings_b_wedding when b and wedding


        group acc_underwear auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group acc_underwear auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group acc_boobs auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_boobs auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group underdress auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "bottomless", "naked"]
        group underdress auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "bottomless", "naked"]
        group underdress auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "bottomless", "naked"]
        group underdress auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "bottomless", "naked"]


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]


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

    layeredimage angela breedad bj:
        attribute_function MultiPickers([HaircutPicker, OutfitPicker], append_npc_from_attributes=True)


        always:
            "angela_breedad_bj_bg"


        attribute mike

        group mc_dicks:
            attribute mike_small null
            attribute mike_medium null
            attribute mike_big null


        attribute bree

        attribute bree_nohaircut null


        group bree_outfit auto if_any ["bree"]


        attribute minami


        group minami_outfit auto if_any ["minami"]


        group hair auto if_any ["minami"]


        always:
            "angela_breedad_bj_bree_dad"


        always:
            "angela_breedad_bj_angela"


        attribute tongueout if_any ["out"]


        group eyes auto:
            attribute closed
            attribute opened default


        attribute cum null
        group cum auto if_any ["cum"]       


        group dick auto:
            attribute out default
            attribute blowjob


        attribute dickcum if_any ["out"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
