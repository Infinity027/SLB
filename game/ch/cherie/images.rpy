init 1:
    layeredimage cherie:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=cherie)

        attribute idle null

        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto:
            attribute normal null default

        group exp auto variant "a" if_any "a"
        group exp auto variant "b" if_any "b"
        group exp auto variant "c" if_any "c"

        group multiple:
            attribute ears null

        attribute naked null

        attribute bottomless null

        attribute topless null

        attribute chainless null
        group poke auto variant "ab" if_any ["a", "b"] if_not ["topless", "naked"]
        group poke auto variant "c" if_any ["c"] if_not ["topless", "naked"]

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

        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group haircuts auto variant "a" if_any ["a"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "c" if_any ["c"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "a_wedding" if_all ["wedding", "a"]
        group haircuts auto variant "c_wedding" if_all ["wedding", "c"]

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
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=cherie)

        attribute idle null

        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto:
            attribute normal null default

        group exp auto variant "a" if_any "a"
        group exp auto variant "b" if_any "b"
        group exp auto variant "c" if_any "c"

        attribute naked null

        attribute bottomless null

        attribute topless null
 
        attribute chainless null

        group poke auto variant "ab" if_any ["a", "b"] if_not ["topless", "naked"]
        group poke auto variant "c" if_any ["c"] if_not ["topless", "naked"]

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

        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group haircuts auto variant "a" if_any ["a"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "c" if_any ["c"] if_not ["wedding", "funeral", "swimsuit"]
        group haircuts auto variant "a_wedding" if_all ["wedding", "a"]
        group haircuts auto variant "c_wedding" if_all ["wedding", "c"]

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
