init 1:
    layeredimage lavish:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=lavish)


        group tail auto if_not ["bottomless", "naked"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_tongue when tongue
        group multiple auto variant piercings_lips when lips


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        group sweater auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group sweater auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group sweater auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group sweater auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]


        group bracelet auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group bracelet auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        attribute collar null
        group collar auto if_any ["collar"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]


        group hat auto if_not ["topless", "naked"]
        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage lavish close:
        yalign 0.1
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=lavish)


        group tail auto if_not ["bottomless", "naked"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_tongue when tongue
        group multiple auto variant piercings_lips when lips


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        group sweater auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group sweater auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group sweater auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group sweater auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]


        group bracelet auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group bracelet auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        attribute collar null
        group collar auto if_any ["collar"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]


        group hat auto if_not ["topless", "naked"]
        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage lavish smartphone:
        always "lavish_smartphone"

    layeredimage lavish cunnilingus:
        attribute_function Pickers([CollarPicker,PregnancyPicker,PubesPicker,PiercingsPicker],npc=lavish)


        always "lavish_cunnilingus_bodies"


        group exp auto:
            attribute normal default
            attribute climax


        group hand auto:
            attribute dildo null
            attribute fing null default


        group fing auto if_any ["fing"]:
            attribute vaginal default
            attribute anal


        group dildo auto if_any ["dildo"]:
            attribute vaginal default
            attribute anal


        group mike_tongue auto:
            attribute up default
            attribute down


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings


        attribute squirt


        attribute pubes


        attribute pregnant


        attribute collar


        group multiple auto variant piercings_preg

    layeredimage lavish kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker], npc=lavish)


        always "lavish_kiss"


        attribute collar if_not ["cosplay"]


        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute nose null
            attribute tongue null
        group multiple auto variant piercings_naked when naked or topless
        group multiple auto variant piercings


        group outfitmike auto if_not ["naked"]:
            attribute normal default


        attribute pregnant


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "naked", "topless"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]

    layeredimage lavish files:
        always "lavish_files"

    layeredimage lavish pool sex:
        always "lavish_pool"

    layeredimage lavish bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker], npc=lavish)


        group bg auto:
            attribute bedroom default


        group mike auto:
            attribute tip default


        group outfit_mike auto variant "tip" if_any ["tip"]
        group outfit_mike auto variant "deep" if_any ["deep"]


        always "lavish_bj_lavish"


        attribute pregnant


        group arm auto variant "tip" if_any ["tip"]:
            attribute back default
        group arm auto variant "deep" if_any ["deep"]:
            attribute back default


        group head auto:
            attribute tip default


        group multiple auto variant piercings_tip when tip
        group multiple auto variant piercings_deep when deep


        group exp auto variant "tip" if_any ["tip"]:
            attribute normal default
        group exp auto variant "deep" if_any ["deep"]:
            attribute normal default


        group dick auto variant "tip" if_any ["tip"]:
            attribute out default
        group dick auto variant "deep" if_any ["deep"]:
            attribute out default


        attribute cum null
        group multiple auto variant cum when cum


        attribute cumshot null
        group cumshot auto if_all ["cumshot","out"]


        group hand auto variant "tip" if_any ["tip"]
        group hand auto variant "deep" if_any ["deep"]


        attribute creampie null
        group creampie auto if_all ["creampie","blow"]


        attribute clit null
        group multiple auto variant piercings_naked when naked
        group multiple auto variant piercings


        attribute topless null
        group outfit auto variant "top" if_not ["topless"]:
            attribute naked null
        attribute bottomless null
        group outfit auto variant "bot" if_not ["bottomless"]:
            attribute naked null


        attribute collar null
        group collar auto if_any ["collar"]

    layeredimage lavish missionary:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker], npc=lavish)

        group bg auto:
            attribute bedroom default
        always "lavish_missionary_body"

        group exp auto:
            attribute normal default

        attribute pregnant

        attribute tongue if_not ["normal"]
        group multiple auto variant piercings

        group dick auto

        attribute condom

        group cum auto

    layeredimage lavish cowgirl:
        attribute_function Pickers([DickPicker, PubesPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=lavish)


        always "lavish_cowgirl_bg"


        always "lavish_cowgirl_bodies"


        attribute collar


        group multiple auto variant piercings_exp


        group exp auto:
            attribute pleasure default


        group multiple auto variant piercings


        group dicks:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto if_not ["out"]


        group condom auto if_any ["condom"] if_not ["out"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["out", "condom"]


        group multiple auto variant piercings_pubes


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings_out


        attribute bodycum


        group dick auto variant "out" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["out", "dickcum"] if_not ["condom"]


        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]


        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]


        group condomcum auto if_all ["out", "condom", "cumshot"]


        always "lavish_cowgirl_light"

    layeredimage lavish doggy:
        attribute_function Pickers([DickPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=lavish)


        always "lavish_doggy_bg"


        always "lavish_doggy_mike_righthand" if_any ["mike"]


        always "lavish_doggy_lavish"


        group pregnant auto if_any ["pregnant"]:
            attribute naked default


        attribute torn null
        group outfit auto if_not ["torn"]
        group outfit auto variant "torn" if_any ["torn"]


        attribute plug null
        group plug auto if_any ["plug"] if_not ["anal"]


        group exp auto:
            attribute happy default


        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_lust when lust
        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings_ahegao when ahegao


        group mike_lefthand auto if_any ["mike"]:
            attribute pregnant if_any ["pregnant"]
            attribute normal default if_not ["pregnant"]


        group dick auto if_any ["mike"]


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group dick_out auto if_any ["mike"] if_not ["vaginal","anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]


        group condom_out auto if_any ["condom"] if_not ["cumshot","vaginal","anal"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]


        attribute mike


        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings_torn when torn
        group multiple auto variant piercings_naked when naked
        group multiple auto variant piercings


        attribute collar

    layeredimage lavish ending:
        attribute_function Pickers([EndingKidPicker], npc=lavish)


        always "lavish_ending_bg"


        always "lavish_ending_bodies"


        attribute kid


        always "lavish_ending_light"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
