init 1:
    layeredimage kylie:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=kylie)


        attribute idle null


        group position auto if_not ["hoodup"]
        group position auto variant "hoodup" if_any ["hoodup"]


        attribute pubes if_any ["naked","bottomless","sexyswimsuit","sexydate"]
        attribute pubes if_all ["topless"] if_any ["date","wedding"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_y when y
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_blush when blush
        group multiple auto variant piercings_sad when sad
        group multiple auto variant piercings_angry when angry
        group multiple auto variant piercings_yandere when yandere
        group multiple auto variant piercings_annoyed when annoyed


        group multiple auto variant piercings_a_topless when a and (naked or topless)
        group multiple auto variant piercings_b_topless when b and (naked or topless)
        group multiple auto variant piercings_y_topless when y and (naked or topless)
        group multiple auto variant piercings_a_sexy when a and (sexyswimsuit or sexydate) and not (naked or topless)
        group multiple auto variant piercings_b_sexy when b and (sexyswimsuit or sexydate) and not (naked or topless)
        group multiple auto variant piercings_y_sexy when y and (sexyswimsuit or sexydate) and not (naked or topless)


        attribute collar null
        group collar auto if_all ["collar"] if_any ["casual", "jail"]


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "y" if_any ["y"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "y_pregnant" if_all ["y", "pregnant"] if_not ["naked","bottomless"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked","hoodie"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked","hoodie"]
        group top auto variant "y" if_any ["y"] if_not ["pregnant","topless","naked","hoodie"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","topless","hoodie"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","topless","hoodie"]
        group top auto variant "y_pregnant" if_all ["y", "pregnant"] if_not ["naked","topless","hoodie"]


        group arms auto


        group top auto variant "arms_y" if_any ["y"] if_not ["topless","naked","hoodie"]


        attribute noacc null
        group acc auto variant "a" if_any ["a"] if_not ["noacc", "naked"]
        group acc auto variant "b" if_any ["b"] if_not ["noacc", "naked"]
        group acc auto variant "y" if_any ["y"] if_not ["noacc", "naked"]
        group acc auto if_not ["noacc", "naked"]


        group collar auto if_all ["collar"] if_not ["casual", "jail"]


        attribute hoodie null
        group hoodie auto if_any ["hoodie"] if_not ["pregnant", "topless", "naked"]
        group hoodie auto variant "pregnant" if_all ["hoodie", "pregnant"] if_not ["topless", "naked"]
        group hood auto variant "a" if_all ["hoodie", "a"] if_not ["topless", "naked"]:
            attribute hooddown default
        group hood auto variant "b" if_all ["hoodie", "b"] if_not ["topless", "naked"]:
            attribute hooddown default
        group hood auto variant "y" if_all ["hoodie", "y"] if_not ["topless", "naked"]:
            attribute hooddown default


        attribute knife if_any ["a"]
        attribute bloodyknife if_any ["knife"]


        attribute handcuffs null
        group handcuffs auto if_any ["handcuffs"]


        attribute bloodyface


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "y" if_any ["y"]

    layeredimage kylie close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=kylie)


        attribute idle null


        group position auto


        attribute pubes if_any ["naked","bottomless","sexyswimsuit","sexydate"]
        attribute pubes if_all ["topless"] if_any ["date","wedding"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_y when y
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_blush when blush
        group multiple auto variant piercings_sad when sad
        group multiple auto variant piercings_angry when angry
        group multiple auto variant piercings_yandere when yandere
        group multiple auto variant piercings_annoyed when annoyed


        group multiple auto variant piercings_a_topless when a and (naked or topless)
        group multiple auto variant piercings_b_topless when b and (naked or topless)
        group multiple auto variant piercings_y_topless when y and (naked or topless)
        group multiple auto variant piercings_a_sexy when a and (sexyswimsuit or sexydate) and not (naked or topless)
        group multiple auto variant piercings_b_sexy when b and (sexyswimsuit or sexydate) and not (naked or topless)
        group multiple auto variant piercings_y_sexy when y and (sexyswimsuit or sexydate) and not (naked or topless)


        attribute collar null
        group collar auto if_all ["collar"] if_any ["casual", "jail"]


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "y" if_any ["y"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "y_pregnant" if_all ["y", "pregnant"] if_not ["naked","bottomless"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "y" if_any ["y"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","topless"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","topless"]
        group top auto variant "y_pregnant" if_all ["y", "pregnant"] if_not ["naked","topless"]


        group arms auto


        group top auto variant "arms_y" if_any ["y"] if_not ["topless","naked"]


        attribute noacc null
        group acc auto variant "a" if_any ["a"] if_not ["noacc", "naked"]
        group acc auto variant "b" if_any ["b"] if_not ["noacc", "naked"]
        group acc auto variant "y" if_any ["y"] if_not ["noacc", "naked"]
        group acc auto if_not ["noacc", "naked"]


        group collar auto if_all ["collar"] if_not ["casual", "jail"]


        attribute knife if_any ["a"]
        attribute bloodyknife if_any ["knife"]


        attribute handcuffs null
        group handcuffs auto if_any ["handcuffs"]


        attribute bloodyface


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "y" if_any ["y"]

    layeredimage kylie smartphone:
        always "kylie_smartphone"

    layeredimage kylie memory:
        always "kylie_peeping"

    layeredimage kylie taser:
        always "kylie_taser"
        always "kylie_taser_mike"
        group multiple auto variant fx

    layeredimage kylie missionary:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker, PubesPicker], npc=kylie)


        group bg auto:
            attribute bedroom1 default
            attribute bedroom4


        attribute mike null
        always "kylie_missionary_mike" if_any "mike"


        always "kylie_missionary_kylie"


        attribute pregnant null


        group exp auto:
            attribute normal default


        attribute xray null
        group xray_dick_vaginal auto if_all ["mike", "xray", "vaginal"]
        group xray_dick_anal auto if_all ["mike", "xray", "anal"]
        group xray_condom_vaginal auto if_all ["mike", "xray", "vaginal", "condom"]
        group xray_cum_vaginal auto if_all ["mike", "xray", "vaginal", "cum"]
        group xray_cum_anal auto if_all ["mike", "xray", "anal", "cum"]


        attribute cum null
        attribute vaginal null
        attribute anal null
        attribute condom null

        group dick_vaginal auto if_any "vaginal"
        group dick_anal auto if_any "anal"

        group condom_vaginal auto if_all ["mike", "vaginal", "condom"]

        group cum_vaginal auto if_all ["vaginal", "cum"] if_not ["xray"]
        group cum_anal auto if_all ["anal", "cum"] if_not ["xray"]


        group multiple auto variant piercings:
            attribute navel if_not "xray"


        group dick_out auto if_any "mike" if_not ["vaginal", "anal"]
        group condom_out auto if_all ["mike", "condom"] if_not ["vaginal", "anal"]
        group cum_out auto if_all ["mike", "cum"] if_not ["vaginal", "anal", "xray"]


        attribute collar

        attribute bellycum


        attribute blood


        attribute pubes


    layeredimage kylie cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, DickPicker], npc=kylie)


        always "kylie_cunnilingus_bg"


        always "kylie_cunnilingus_bodies"


        attribute pregnant


        group miketongue auto:
            attribute down default
            attribute middle
            attribute up


        attribute pubes


        attribute squirt


        group exp auto:
            attribute normal default
            attribute pleasure
            attribute ahegao


        group dick auto


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]


        group hand auto:
            attribute endjob default
            attribute handjob


        attribute speed if_any ["handjob"]


        attribute clit null
        attribute navel null
        attribute pregnant_navel null
        attribute tongue null
        group multiple auto variant piercings


        group handuse auto:
            attribute finger null default
            attribute dildo null
            attribute beads null


        group finger auto if_any ["finger"]:
            attribute vaginal default
            attribute anal


        group dildo auto if_any ["dildo"]:
            attribute vaginal default
            attribute anal


        group beads auto if_any ["beads"]:
            attribute vaginal null
            attribute anal


        attribute cum null
        group multiple auto variant cum when cum      

    layeredimage kylie bj:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker], npc=kylie)


        group bg auto:
            attribute bedroom default
            attribute classroom
            attribute jail


        always "kylie_bj_arm"


        always "kylie_bj_mike"


        group dick auto:
            attribute out default
            attribute blow



        attribute mikepants null
        group mikepants auto if_any ["mikepants"]

        attribute mikeshirt


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute tongue if_any ["out"]


        always "kylie_bj_kylie"


        attribute pregnant


        attribute cum null
        group multiple auto variant cum when cum     


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]


        attribute collar


        group multiple auto variant piercings


        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute casual
            attribute jail


        group exp auto:
            attribute normal default
            attribute pleasure
            attribute surprised


        always "kylie_bj_bars" if_any ["jail"]

    layeredimage kylie cowgirl:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, PubesPicker, CollarPicker], npc=kylie)


        group bg auto:
            attribute bedroom1 default
            attribute bedroom4


        always "kylie_cowgirl_bodies"


        attribute collar


        group exp auto:
            attribute normal default


        attribute pubes


        group multiple auto variant piercings_body



        attribute topless null
        group outfit_top auto if_not ["topless"]

        attribute bottomless null
        group outfit_bot auto if_not ["bottomless"]

        attribute maskless null
        group mask auto if_any ["halloween"] if_not ["maskless"]:
            attribute onside default
        attribute emotionless null
        group mask_onface_exp auto if_all ["halloween", "onface"] if_not ["maskless", "emotionless"]:
            attribute normal default
        group mask_onface_fx auto if_all ["halloween", "onface"] if_not ["maskless"]



        group dick auto if_any ["vaginal"]

        attribute condom null
        group condom auto if_all ["condom", "vaginal"]

        attribute creampie null
        group creampie auto if_all ["creampie", "vaginal"] if_not ["hard"]


        group arm auto
        group arm_halloween auto if_any ["halloween"] if_not ["bottomless"]


        group drip auto if_any ["openpussy"]


        group multiple auto variant piercings_arm when (openpussy or closepussy)


        attribute pregnant
        group outfit_pregnant auto if_any ["pregnant"]



        group dick auto if_not ["vaginal"]:
            attribute hard default

        group creampie auto if_any ["creampie"] if_not ["vaginal", "hard"]

        group condom auto if_any ["condom"] if_not ["vaginal", "condomcum"]

        attribute condomcum null
        group condomcum auto if_any ["condomcum"] if_not ["vaginal", "condom", "anal"]

        attribute dickcum null
        group dickcum auto if_any ["dickcum"]

        attribute cumshot if_any ["hard"]


        attribute ears null
        group multiple auto variant piercings
        group multiple auto variant piercings_notarm when not (openpussy or closepussy)
        group multiple auto variant piercings_notnormal when not normal
        group multiple auto variant piercings_normal when normal


        attribute cumbody


        attribute bloodbath

    layeredimage kylie doggy:
        attribute_function Pickers([DickPicker, PiercingsPicker, OutfitPicker], npc=kylie)


        group bg auto:
            attribute bedroom default
            attribute jail


        always "kylie_doggy_kylie"


        attribute cum null
        group multiple auto variant cum when cum     


        group exp auto:
            attribute normal default
            attribute surprised
            attribute crazy
            attribute ahegao


        group multiple auto variant piercings
        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_crazy when crazy
        group multiple auto variant piercings_ahegao when ahegao


        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute jail


        attribute mike


        group dick auto if_any ["mike"]:
            attribute vaginal
            attribute anal


        attribute condom null
        group condom auto if_all ["mike", "condom"]


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["condom"]


        attribute vaginaldrip
        attribute analdrip


        group dick_out auto if_any ["mike"] if_not ["vaginal", "anal"]


        attribute dickcum null
        group dickcum auto if_all ["mike", "dickcum"] if_not ["condom", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "cumshot"] if_not ["condom", "vaginal", "anal"]


        group condom_out auto if_all ["mike", "condom"] if_not ["cumshot", "vaginal", "anal"]


        group condomcum auto if_all ["mike", "condom", "cumshot"] if_not ["vaginal", "anal"]

    layeredimage kylie spoon:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker, MCCGPicker], npc=kylie)


        attribute a null
        attribute b null
        attribute casual null
        attribute collar null
        attribute d null
        attribute mc_casual null
        attribute mikemc null
        attribute nose null
        attribute p null
        attribute tongue null


        group bg auto:
            attribute bedroom1 default


        always "kylie_spoon_bodies"
        attribute pregnant
        always "kylie_spoon_balls"
        attribute pubes


        group eyes auto:
            attribute closed default


        group dick auto


        group multiple auto variant piercings


        always "kylie_spoon_hair"


        attribute naked null
        group outfits auto if_not ["naked"]


        attribute collar


        attribute condom null
        attribute cumshot null
        group dickout auto if_not ["vaginal", "anal"]
        group dickout auto variant "condom" if_any["condom"] if_not ["vaginal", "anal"]
        group dickout auto variant "cumshot" if_any["cumshot"] if_not ["vaginal", "anal", "condom"]


        always "kylie_spoon_condom_vaginal" if_all ["condom", "vaginal"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group multiple auto variant fx


        always "kylie_spoon_fg_shadow" if_any ["beach"]
        always "kylie_spoon_sand" if_any ["beach"]

    layeredimage kylie kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker, MCCGPicker], npc=kylie)

        group multiple:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null


        group base auto if_not ["bowsette"]
        attribute bowsette "kylie_kiss_base_breemc_bowsette"


        group mcoutfits auto variant "mikemc" if_any "mikemc" if_not ["naked"]
        group mcoutfits auto variant "breemc" if_any "breemc" if_not ["naked"]


        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        group multiple auto variant piercings_mikemc when mikemc
        group multiple auto variant piercings_mikemc_naked when mikemc and (naked or topless)
        group multiple auto variant piercings_breemc when breemc
        group multiple auto variant piercings_breemc_naked when breemc and (naked or topless)


        attribute pregnant null
        attribute naked null
        attribute topless null
        group outfits auto variant "mikemc" if_any "mikemc" if_not ["naked", "topless"]
        group outfits auto variant "breemc" if_any "breemc" if_not ["naked", "topless"]:
            attribute chinese "kylie_kiss_outfits_breemc_casual"
            attribute bowsette "kylie_kiss_outfits_breemc_halloween"
            attribute invisible "kylie_kiss_outfits_breemc_halloween"


        group collars auto variant "mikemc" if_any "mikemc"
        group collars auto variant "breemc" if_any "breemc"


        group acc auto variant "mikemc" if_any "mikemc" if_not ["naked"]
        group acc auto variant "breemc" if_any "breemc" if_not ["naked"]


        group haircuts auto variant "breemc" if_any "breemc" if_not ["bowsette"]
        attribute bowsette "kylie_kiss_breemc_haircut_bowsette"

    layeredimage kylie gift:

        always "kylie_gift"

        group inside auto:
            attribute closed default

        always "kylie_gift_blood" if_not ["sweater", "closed"]

        group exp auto:
            attribute normal default

    layeredimage kylie murder:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker], append_npc_from_attributes=True)

        always "kylie_murder"

        group girl auto

        attribute sasha_collar if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]
        attribute sasha_boobjob if_any ["sasha"]
        attribute sasha_pregnant if_any ["sasha"]

        attribute bree_collar if_any ["bree"]
        attribute bree_pregnant if_any ["bree"]

        always "kylie_murder_blood_throat" if_any ["bree", "sasha"]
        always "kylie_murder_blood_slash" if_any ["bree", "sasha"]
        always "kylie_murder_blood_splash" if_any ["bree", "sasha"]

    layeredimage kylie trial witness:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker], npc=kylie)


        always "kylie_trial_witness_bg"


        attribute pregnant


        group exp auto:
            attribute happy default


        group multiple auto variant piercings


        attribute collar

    layeredimage kylie trial execution:
        attribute_function Pickers([PiercingsPicker, CollarPicker], npc=kylie)


        always "kylie_trial_execution_bg"


        attribute scaredmike


        group head auto:
            attribute sad default


        attribute helmet null
        group helmet auto if_any ["helmet"]


        attribute collar


        group multiple auto variant piercings
        group multiple auto variant piercings_crazy when crazy
        group multiple auto variant piercings_dying when dying
        group multiple auto variant piercings_pain when pain
        group multiple auto variant piercings_sad when sad
        group multiple auto variant piercings_crazypain when (crazy or pain)
        group multiple auto variant piercings_dyingsad when (dying or sad)


        always "kylie_trial_execution_chair"


        attribute fx

    layeredimage kylie ending:
        attribute_function Pickers([EndingKidPicker], npc=kylie)


        always "kylie_ending_bg"


        always "kylie_ending_bodies"


        attribute kid null
        always "kylie_ending_daughter" when kid
        always "kylie_ending_paperbag" when not kid

    layeredimage kylie bad ending:


        always "kylie_bad_ending_bg"


        attribute mike


        attribute kylie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
