init 1:
    layeredimage cherie:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=cherie)


        attribute idle null


        group position auto


        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any "pregnant"


        attribute blush null
        group blush auto if_any ["blush"]


        group exp auto:
            attribute normal null default

        group exp auto variant "a" if_any "a"
        group exp auto variant "b" if_any "b"
        group exp auto variant "c" if_any "c"


        group multiple auto variant null_piercings
        group multiple:
            attribute ears null

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c


        attribute naked null


        attribute bottomless null
        group bot auto variant "a" if_all ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_all ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_all ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_all ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_all ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_all ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]

        attribute chainless null
        group chains auto variant "a" if_all ["a"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "b" if_all ["b"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "c" if_all ["c"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]
        group chains auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]
        group chains auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]

        group poke auto variant "ab" if_any ["a", "b"] if_not ["topless", "naked"]
        group poke auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group poke_piercing auto variant "ab" if_all ["nipples"] if_not ["topless", "naked", "c"]
        group poke_piercing auto variant "c" if_all ["nipples"] if_not ["topless", "naked", "a", "b"]

        attribute collar null
        group collar auto if_not "casual" if_any "collar"

        group necklace auto variant "a" if_any ["a"] if_not "collar"
        group necklace auto variant "b" if_any ["b"] if_not "collar"
        group necklace auto variant "c" if_any ["c"] if_not "collar"

        group haircuts auto variant "b" if_any ["b"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "b_wedding" if_all ["wedding", "b"]

        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arms_position auto if_not ["halloween"]
        group arms_position auto variant "haircut" if_all "haircut" if_not ["halloween"]
        group arms_position auto variant "nohaircut" if_all "nohaircut" if_not ["halloween", "wedding", "funeral"]
        group arms_position auto variant "haircut" if_all "nohaircut" if_not ["halloween"] if_any ["wedding", "funeral"]

        group arms_outfit auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group arms_outfit auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group arms_outfit auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]


        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group haircuts auto variant "a" if_any ["a"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "c" if_any ["c"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "a_wedding" if_all ["wedding", "a"]
        group haircuts auto variant "c_wedding" if_all ["wedding", "c"]


        group piercings auto variant "a_date" if_all ["a", "ears", "date"]
        group piercings auto variant "a_sexydate" if_all ["a", "ears", "sexydate"]
        group piercings auto variant "a_wedding" if_all ["a", "ears", "wedding"]

        group piercings auto variant "b_date" if_all ["b", "ears", "date"]
        group piercings auto variant "b_sexydate" if_all ["b", "ears", "sexydate"]
        group piercings auto variant "b_wedding" if_all ["b", "ears", "wedding"]

        group piercings auto variant "c_date" if_all ["c", "ears", "date"]
        group piercings auto variant "c_sexydate" if_all ["c", "ears", "sexydate"]
        group piercings auto variant "c_wedding" if_all ["c", "ears", "wedding"]


        group glasses auto variant "a" if_any ["a"] if_not ["topless", "naked", "noglasses"]
        group glasses auto variant "b" if_any ["b"] if_not ["topless", "naked", "noglasses"]
        group glasses auto variant "c" if_any ["c"] if_not ["topless", "naked", "noglasses"]


        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group hat auto variant "c_nohaircut" if_all ["c", "nohaircut"] if_not ["topless", "naked"]
        group hat auto variant "c_haircut" if_all ["c", "haircut"] if_not ["topless", "naked"]

        group acc auto
        group acc auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group arm auto

    layeredimage cherie close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=cherie)


        attribute idle null


        group position auto


        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any "pregnant"


        attribute blush null
        group blush auto if_any ["blush"]


        group exp auto:
            attribute normal null default

        group exp auto variant "a" if_any "a"
        group exp auto variant "b" if_any "b"
        group exp auto variant "c" if_any "c"


        group multiple auto variant null_piercings
        group multiple:
            attribute ears null

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c


        attribute naked null


        attribute bottomless null
        group bot auto variant "a" if_all ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_all ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_all ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_all ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_all ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_all ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]

        attribute chainless null
        group chains auto variant "a" if_all ["a"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "b" if_all ["b"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "c" if_all ["c"] if_not ["pregnant", "bottomless", "topless", "naked", "chainless"]
        group chains auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]
        group chains auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]
        group chains auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "topless", "naked", "chainless"]

        group poke auto variant "ab" if_any ["a", "b"] if_not ["topless", "naked"]
        group poke auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group poke_piercing auto variant "ab" if_all ["nipples"] if_not ["topless", "naked", "c"]
        group poke_piercing auto variant "c" if_all ["nipples"] if_not ["topless", "naked", "a", "b"]

        attribute collar null
        group collar auto if_not "casual" if_any "collar"

        group necklace auto variant "a" if_any ["a"] if_not "collar"
        group necklace auto variant "b" if_any ["b"] if_not "collar"
        group necklace auto variant "c" if_any ["c"] if_not "collar"

        group haircuts auto variant "b" if_any ["b"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "b_wedding" if_all ["wedding", "b"]

        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arms_position auto if_not ["halloween"]
        group arms_position auto variant "haircut" if_all "haircut" if_not ["halloween"]
        group arms_position auto variant "nohaircut" if_all "nohaircut" if_not ["halloween", "wedding", "funeral"]
        group arms_position auto variant "haircut" if_all "nohaircut" if_not ["halloween"] if_any ["wedding", "funeral"]

        group arms_outfit auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group arms_outfit auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group arms_outfit auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group arms_outfit auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]


        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group haircuts auto variant "a" if_any ["a"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "c" if_any ["c"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "a_wedding" if_all ["wedding", "a"]
        group haircuts auto variant "c_wedding" if_all ["wedding", "c"]


        group piercings auto variant "a_date" if_all ["a", "ears", "date"]
        group piercings auto variant "a_sexydate" if_all ["a", "ears", "sexydate"]
        group piercings auto variant "a_wedding" if_all ["a", "ears", "wedding"]

        group piercings auto variant "b_date" if_all ["b", "ears", "date"]
        group piercings auto variant "b_sexydate" if_all ["b", "ears", "sexydate"]
        group piercings auto variant "b_wedding" if_all ["b", "ears", "wedding"]

        group piercings auto variant "c_date" if_all ["c", "ears", "date"]
        group piercings auto variant "c_sexydate" if_all ["c", "ears", "sexydate"]
        group piercings auto variant "c_wedding" if_all ["c", "ears", "wedding"]


        group glasses auto variant "a" if_any ["a"] if_not ["topless", "naked", "noglasses"]
        group glasses auto variant "b" if_any ["b"] if_not ["topless", "naked", "noglasses"]
        group glasses auto variant "c" if_any ["c"] if_not ["topless", "naked", "noglasses"]


        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group hat auto variant "c_nohaircut" if_all ["c", "nohaircut"] if_not ["topless", "naked"]
        group hat auto variant "c_haircut" if_all ["c", "haircut"] if_not ["topless", "naked"]

        group acc auto
        group acc auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        group arm auto

    layeredimage cherie kiss:

        always:
            "cherie_teaser_kiss_bodies"


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]:
            attribute casual default


        group outfit auto variant "mike" if_not ["naked", "topless"]:
            attribute santa default

    layeredimage cherie smartphone:
        always "cherie_smartphone"

    layeredimage cherie stand:
        attribute_function Pickers([DickPicker])


        always:
            "cherie_stand_bg"


        always:
            "cherie_stand_bodies"


        group outfit auto variant "mike" if_not ["naked"]:
            attribute santa default


        group multiple auto variant cum


        group eyes auto:
            attribute closed default


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        always:
            "cherie_stand_pubes"


        group dick auto variant "out" if_not ["vaginal", "anal", "limp"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal", "limp"]


        group condom auto variant "out" if_any ["condom"] if_not ["cumshot", "vaginal", "anal", "limp"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal", "anal", "limp"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["vaginal", "anal", "limp"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
