init 1:
    layeredimage emma:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, SeasonPicker, IndoorOutdoorPicker], npc=emma)


        attribute indoor null
        attribute outdoor null
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        attribute pubes

        attribute naked null

        group panties auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group top auto variant "a" if_any ["a"] if_not ["casual", "pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["casual", "pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["casual", "topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["casual", "topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_all ["a", "casual"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_all ["b", "casual"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant", "casual"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant", "casual"] if_not ["topless", "naked"]


        attribute collar if_all ["b"]


        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        attribute blazer null
        group blazer auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked", "halloween"]
        group blazer auto if_any ["blazer"] if_not ["topless", "naked"]


        attribute hat null
        group hat auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked"]
        group hat auto if_any ["hat", "wedding"] if_not ["topless", "naked"]


        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage emma close:
        yalign 0.04
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, SeasonPicker, IndoorOutdoorPicker], npc=emma)


        attribute indoor null
        attribute outdoor null
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        attribute pubes

        attribute naked null

        group panties auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group top auto variant "a" if_any ["a"] if_not ["casual", "pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["casual", "pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["casual", "topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["casual", "topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_all ["a", "casual"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_all ["b", "casual"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant", "casual"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant", "casual"] if_not ["topless", "naked"]


        attribute collar if_all ["b"]


        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        attribute blazer null
        group blazer auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked", "halloween"]
        group blazer auto if_any ["blazer"] if_not ["topless", "naked"]


        attribute hat null
        group hat auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked"]
        group hat auto if_any ["hat", "wedding"] if_not ["topless", "naked"]


        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage emma smartphone:
        always "emma_smartphone"

    layeredimage emma kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker], npc=emma)

        always "emma_kiss"

        attribute collar

        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]

        group hat auto if_not ["naked"]

        group outfitmike auto if_not ["naked"]:
            attribute normal default

    layeredimage emma lick:
        attribute_function Pickers([ CollarPicker], npc=emma)


        always "emma_lick_bg"


        always "emma_lick_emma"


        group exp auto:
            attribute shy default
        attribute collar

    layeredimage emma hj:
        attribute_function Pickers([ CollarPicker, DickPicker], npc=emma)


        group bg auto:
            attribute bedroom default
        always "emma_hj_mikemc"
        always "emma_hj_emma"

        attribute pregnant
        attribute collar

        group exp auto:
            attribute normal default


        group dick auto


        attribute cum null
        group cum auto if_any ["cum"]


        always "emma_hj_emmafrontarm"


        group mikehand auto

    layeredimage emma bj:
        attribute_function Pickers([ CollarPicker], npc=emma)


        always "emma_bj_bg"


        always "emma_bj_bodies"


        attribute blush



        group mouth auto if_not ["blowjob"]:
            attribute scare default

        group eyes auto:
            attribute lookdown default

        attribute cum null
        attribute alot null
        group multiple auto variant cum_alot when alot
        group multiple auto variant cum


        always "emma_bj_handright" if_not ["handjob"]


        group dick auto:
            attribute limp default


        attribute handjob null
        group handjob auto if_any ["handjob"]


        attribute speed null
        group speed auto if_all ["speed", "handjob"]


        attribute creampie null
        group creampie auto if_any ["creampie"]


        attribute cumshot if_any ["chub"]


        attribute dickcum if_any ["hard"]


        always "emma_bj_handleft"

    layeredimage emma doggy:
        attribute_function Pickers([CollarPicker], npc=emma)

        always "emma_doggy_bg_back"

        always "emma_doggy_bodies"

        always "emma_doggy_light"

        always "emma_doggy_bg_front"

        attribute limp

        attribute cum null
        always "emma_doggy_drip_cum" if_any ["cum"]
        always "emma_doggy_drip_squirt" if_all ["squirt", "limp"]


        attribute squirt


        attribute pregnant


        attribute cumshot if_not ["limp"]


        group exp auto:
            attribute smile default


        attribute noacc null
        group acc auto:
            attribute necklace default if_not ["noacc", "collar"]       
            attribute collar

        attribute leash default if_any ["necklace", "collar"] if_not ["noacc"]

        group multiple auto variant fx

        attribute saliva if_any ["ahegao"]

    layeredimage emma missionary:
        attribute_function Pickers([CollarPicker, PubesPicker, DickPicker], npc=emma)

        always "emma_missionary_bg"

        attribute mike

        always "emma_missionary_emma"

        attribute pubes

        attribute collar

        group acc_legs auto

        group outfit auto

        group exp auto:
            attribute normal default

        attribute mikehand if_any ["mike"]

        group fuck auto if_any ["mike"]

        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]

        attribute condom null
        group condom_fuck auto if_all ["condom", "vaginal"]

        group dick auto if_any ["mike"] if_not ["vaginal", "anal"]

        attribute dickcum null
        group dickcum auto if_any ["dickcum"]

        group condom auto if_any ["condom"] if_not ["cumshot", "vaginal", "anal"]

        group condomcum auto if_all ["condom", "cumshot"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom"]

        attribute cumbody

    layeredimage emma ending:
        attribute_function Pickers([EndingKidPicker], npc=emma)

        always "emma_ending_bg"

        always "emma_ending_bodies"

        always "emma_ending_grass_bg"

        attribute kid

        always "emma_ending_grass_fg"

        always "emma_ending_light"
