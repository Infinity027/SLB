init 1:
    layeredimage claire:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=claire)


        attribute idle null


        attribute bottomless null
        attribute topless null
        attribute naked null
        attribute noacc null


        always "claire_ab_body" if_any ["a", "b"]
        always "claire_c_body" if_any ["c"]


        attribute pubes "claire_ab_pubes" if_any ["a", "b"]


        attribute pregnant "claire_ab_pregnant" if_any ["a", "b"]
        attribute pregnant "claire_c_pregnant" if_any ["c"]


        group multiple auto variant piercings_ab when a or b
        group multiple auto variant piercings_c when c


        group body auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "naked"]
        group body auto variant "c" if_any ["c"] if_not ["pregnant", "naked"]
        group body_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["naked"]
        group body_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["naked"]
        group bot auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["bottomless", "naked"]
        group bot_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["bottomless", "naked"]
        group top auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["topless", "naked"]
        group top_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["topless", "naked"]


        attribute blush "claire_ab_blush" if_any ["a", "b"]
        attribute blush "claire_c_blush" if_any ["c"]
        group exp auto variant "ab" if_any ["a", "b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        group poke auto variant "a" if_any ["a", "b"] if_not ["topless", "naked"]

        group poke_piercing auto variant "a" if_all ["nipples"] if_not ["topless", "naked", "c"]


        attribute collar "claire_ab_collar" if_any ["a", "b"]
        attribute collar "claire_c_collar" if_any ["c"]
        group necklace auto variant "ab" if_any ["a", "b"] if_not ["collar"]
        group necklace auto variant "c" if_any ["c"] if_not ["collar"]


        group hands auto if_not ["wedding"]:
            attribute c null
        group hands auto if_all ["wedding"] if_any ["topless", "naked"]:
            attribute c null
        group hands auto variant "wedding" if_any ["wedding"] if_not ["topless", "naked"]:
            attribute c null


        group sleeves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group hands_left auto


        group sleeves_left auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group hair auto variant "ab" if_any ["a", "b"]
        group hair auto variant "c" if_any ["c"]


        group hands_right auto


        group sleeves_right auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group acc_head auto variant "ab" if_any ["a", "b"] if_not ["noacc", "topless", "naked"]
        group acc_head auto variant "c" if_any ["c"] if_not ["noacc", "topless", "naked"]

        group arm auto variant ab when a or b
        group arm auto variant c when c

    layeredimage claire close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=claire)


        attribute idle null


        attribute bottomless null
        attribute topless null
        attribute naked null
        attribute noacc null


        always "claire_close_ab_body" if_any ["a", "b"]
        always "claire_close_c_body" if_any ["c"]


        attribute pubes "claire_close_ab_pubes" if_any ["a", "b"]


        attribute pregnant "claire_close_ab_pregnant" if_any ["a", "b"]
        attribute pregnant "claire_close_c_pregnant" if_any ["c"]


        group multiple auto variant piercings_ab when a or b
        group multiple auto variant piercings_c when c


        group body auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "naked"]
        group body auto variant "c" if_any ["c"] if_not ["pregnant", "naked"]
        group body_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["naked"]
        group body_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["naked"]
        group bot auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["bottomless", "naked"]
        group bot_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["bottomless", "naked"]
        group top auto variant "ab" if_any ["a", "b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top_preg auto variant "ab" if_all ["pregnant"] if_any ["a", "b"] if_not ["topless", "naked"]
        group top_preg auto variant "c" if_all ["pregnant"] if_any ["c"] if_not ["topless", "naked"]


        attribute blush "claire_close_ab_blush" if_any ["a", "b"]
        attribute blush "claire_close_c_blush" if_any ["c"]
        group exp auto variant "ab" if_any ["a", "b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        group poke auto variant "a" if_any ["a", "b"] if_not ["topless", "naked"]

        group poke_piercing auto variant "a" if_all ["nipples"] if_not ["topless", "naked", "c"]


        attribute collar "claire_close_ab_collar" if_any ["a", "b"]
        attribute collar "claire_close_c_collar" if_any ["c"]
        group necklace auto variant "ab" if_any ["a", "b"] if_not ["collar"]
        group necklace auto variant "c" if_any ["c"] if_not ["collar"]


        group hands auto if_not ["wedding"]:
            attribute c null
        group hands auto if_all ["wedding"] if_any ["topless", "naked"]:
            attribute c null
        group hands auto variant "wedding" if_any ["wedding"] if_not ["topless", "naked"]:
            attribute c null


        group sleeves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group hands_left auto


        group sleeves_left auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group hair auto variant "ab" if_any ["a", "b"]
        group hair auto variant "c" if_any ["c"]


        group hands_right auto


        group sleeves_right auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group acc_head auto variant "ab" if_any ["a", "b"] if_not ["noacc", "topless", "naked"]
        group acc_head auto variant "c" if_any ["c"] if_not ["noacc", "topless", "naked"]

        group arm auto variant ab when a or b
        group arm auto variant c when c
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
