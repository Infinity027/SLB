init 1:
    layeredimage morgan:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, PubesPicker], npc=morgan)


        group outfitbg auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group outfitbg auto variant "b" if_any ["b"] if_not ["topless","naked"]


        group position auto
        attribute pubes null

        group pubes auto if_any "pubes":
            attribute b null


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null


        group outfit:
            attribute casual null
            attribute sport null
            attribute date null
            attribute swimsuit null
            attribute naked null
            attribute sexyswimsuit null
            attribute tape null
            attribute wedding null


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked","halloween"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked","halloween"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked","halloween"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked","halloween"]


        group acc_top auto variant "a" if_any ["a"] if_not ["topless", "naked", "pregnant"]
        group acc_top auto variant "b" if_any ["b"] if_not ["topless", "naked", "pregnant"]
        group acc_top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group acc_top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute necklace null
        group necklace auto if_any ["necklace"] if_not ["collar"]


        group hairs auto


        group top auto variant "a" if_all ["a","halloween"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_all ["b","halloween"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant","halloween"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant","halloween"] if_not ["topless","naked"]


        attribute makeup null
        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any ["makeup"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings
        if morgan.male >= 60:
            if_any ["ears"]
            "morgan_piercings_ears2"


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage morgan close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, PubesPicker], npc=morgan)


        group outfitbg auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group outfitbg auto variant "b" if_any ["b"] if_not ["topless","naked"]


        group position auto

        attribute pubes null

        group pubes auto if_any "pubes":
            attribute b null



        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null


        group outfit:
            attribute casual null
            attribute sport null
            attribute date null
            attribute swimsuit null
            attribute naked null
            attribute sexyswimsuit null
            attribute tape null
            attribute wedding null


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked","halloween"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked","halloween"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked","halloween"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked","halloween"]


        group acc_top auto variant "a" if_any ["a"] if_not ["topless", "naked", "pregnant"]
        group acc_top auto variant "b" if_any ["b"] if_not ["topless", "naked", "pregnant"]
        group acc_top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group acc_top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute necklace null
        group necklace auto if_any ["necklace"] if_not ["collar"]


        group hairs auto


        group top auto variant "a" if_all ["a","halloween"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_all ["b","halloween"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant","halloween"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant","halloween"] if_not ["topless","naked"]


        attribute makeup null
        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any ["makeup"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings
        if morgan.male >= 60:
            if_any ["ears"]
            "morgan_close_piercings_ears2"


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage morgan smartphone:
        always "morgan_smartphone"

    layeredimage morgan kiss:
        attribute_function Pickers([PregnancyPicker, CollarPicker, OutfitPicker], npc=morgan)

        attribute sport null
        attribute sexyswimsuit null
        attribute swimsuit null


        always:
            "morgan_kiss_bodies"

        attribute pregnant null


        always:
            if_not ["naked", "blueblackswimsuit", "redbluebikinitop", "bluebikinitop", "tuxtop", "bluejacket", "blacktube", "dotdress", "halloween", "sexydate", "sluttydate", "weddingdress"]
            "morgan_kiss_mike_normal"
        always:
            if_any ["tuxtop", "bluejacket", "blacktube", "dotdress", "sexydate", "sluttydate", "weddingdress"]
            "morgan_kiss_mike_date"
        always:
            if_any ["halloween"]
            "morgan_kiss_mike_halloween"


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]:
            attribute camopants null
            attribute blackpants null
            attribute blackskirt null
            attribute blueskirt null
            attribute blackshorts null
            attribute blackmini null
            attribute nopants null
            attribute sweatpants null
            attribute blacktights null
            attribute redbluebikinibottom null
            attribute bluebikinibottom null
            attribute tuxbottom null


        attribute collar
        attribute necklace null


        group face auto:
            attribute natural default


        group hair auto if_not ["halloween"]
        always:
            if_any ["halloween"]
            "morgan_kiss_hair_nohaircut"


        group hat auto if_not ["naked"]

    layeredimage morgan cunnilingus:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker, HaircutPicker, OutfitPicker], npc=morgan)

        attribute makeup null


        group bodies auto:
            attribute bedroom default


        attribute naked null
        always:
            if_not ["naked"]
            "morgan_cunnilingus_mike_outfit_normal"


        group multiple auto variant fx


        group eyes auto:
            attribute opened default


        group mouth auto:
            attribute smile default


        group multiple auto variant piercings_no_top


        attribute topless null
        group outfit variant "top" if_not ["naked", "topless"]:
            attribute whitetank


        attribute pregnant


        group multiple auto variant piercings_no_big_top


        group outfit variant "top" if_not ["naked", "topless"]:
            attribute blackjacket
            attribute bluesweater
            attribute redhalf


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings


        attribute bottomless null
        group outfit auto variant "bot" if_not ["naked", "bottomless"]


        attribute squirt


        attribute collar


        attribute haircut
        attribute nohaircut


        group tongue auto:
            attribute mikedown default

    layeredimage morgan bj:
        attribute_function Pickers([HaircutPicker], npc=morgan)


        always:
            "morgan_bj_bg"


        always:
            "morgan_bj_bodies"


        group eyes auto:
            attribute opened default


        attribute haircut
        attribute nohaircut


        group mouth auto:
            attribute normal default


        group dick auto:
            attribute hard default


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute creampie null
        group creampie auto if_any ["creampie"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute hand if_not ["limp"]

    layeredimage morgan missionary:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, XrayPicker], npc=morgan)
        attribute tongue null
        attribute cum null

        group bg auto:
            attribute bedroom default

        always:
            "morgan_missionary_body"

        group hairs auto

        attribute pregnant:
            "morgan_missionary_pregnant"

        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any ["makeup"]:
            attribute normal default

        group multiple auto variant piercings

        group man auto:
            attribute out default

        group xray auto:
            if_any "xray"
            if_not "condom"
            attribute none null default

        attribute condom:
            if_any "vaginal"
            "morgan_missionary_condom"

        group cum auto:
            if_any "cum"
            if_not "condom"

        group xraycum auto:
            if_all ["xray", "cum", "vaginal"]
            if_not "condom"

        attribute shake:
            "morgan_missionary_fx_shake"

    layeredimage morgan reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, DickPicker, MCCGPicker], npc=morgan)

        always:
            "morgan_reverse_cowgirl_bg"
        always:
            "morgan_reverse_cowgirl_bodies"

        attribute pubes

        attribute pregnant

        attribute makeup null
        group exp auto if_not "makeup":
            attribute normal default
        group exp auto variant "makeup" if_any "makeup":
            attribute normal default

        attribute collar

        group multiple auto variant piercings


        always:
            "morgan_reverse_cowgirl_balls"
        attribute vaginal null
        attribute anal null
        group dick_outside auto if_not ["vaginal", "anal"]
        group dick_vaginal auto if_any "vaginal"
        group dick_anal auto if_any "anal"


        always:
            if_all ["vaginal", "big"]
            "morgan_reverse_cowgirl_bellytap"


        attribute condom null
        group condom_outside auto if_any "condom" if_not ["vaginal", "anal"]
        group condom_vaginal auto if_all ["vaginal", "condom"]


        attribute cum null
        group cum auto:
            attribute onbody null
        group cum_outside auto if_any ["cum"] if_not ["vaginal", "anal"]
        group cum_vaginal auto if_all ["vaginal", "cum"]
        group cum_anal auto if_all ["anal", "cum"]

    layeredimage morgan doggy:
        attribute_function Pickers([CollarPicker, PubesPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=morgan)


        always:
            "morgan_doggy_bg"


        always:
            "morgan_doggy_bodies"


        attribute collar


        attribute makeup


        attribute tongueout


        group mikemouth auto:
            attribute smile default


        group hairs auto


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute clit null
        group multiple auto variant piercings


        group outfit auto


        group acc_head auto


        attribute pregnant null
        group pregnant auto if_any "pregnant":
            attribute naked default


        group multiple auto variant piercings_preg when preg


        attribute xray null
        group xray auto if_any "xray"


        attribute creampie null
        group xray_creampie auto if_all ["xray","creampie"] if_not "condom"


        attribute condom null
        group xray_condom auto if_all ["xray","condom"] if_not "creampie"


        group xray_condomcum auto if_all ["xray","condom","creampie"]


        group dick_in auto


        group condom auto if_all ["condom","vaginal"]


        attribute cum null
        group multiple auto variant cum when not halloween
        group multiple auto variant cum_halloween when halloween


        group dick_out auto if_not ["vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not ["condom","vaginal","anal"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["condom","vaginal","anal"]


        group condom_out auto if_any "condom" if_not ["cumshot","vaginal","anal"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]

    layeredimage morgan mermaidcg:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=morgan)

        always:
            "morgan_mermaidcg_background"

        group hairs auto:
            attribute nohaircut null

        attribute pregnant
        attribute makeup
        attribute collar

        group multiple auto variant piercings

        always:
            "morgan_mermaidcg_glass"

        always:
            "morgan_mermaidcg_mike"

    layeredimage morgan ending:
        attribute_function Pickers([CollarPicker, HaircutPicker, EndingKidPicker], npc=morgan)

        always:
            "morgan_ending_bg"

        always:
            "morgan_ending_bodies"

        attribute collar
        group haircut auto

        attribute kid

    layeredimage morgan housewife ending:
        attribute_function Pickers([CollarPicker, OutfitPicker, PregnancyPicker, PiercingsPicker, HaircutPicker], npc=morgan, use_morgan_cg_outfits=True)
        always:
            "morgan_housewife_ending_bg"

        always:
            "morgan_housewife_ending_mike"

        always:
            "morgan_housewife_ending_morgan"

        always:
            "morgan_housewife_ending_socks"

        attribute makeup

        attribute haircut

        group multiple auto variant piercings

        attribute naked null
        attribute pregnant
        group outfit auto if_not "naked"

        group outfit_pregnant auto if_any "pregnant" if_not "naked"

        attribute collar
        attribute necklace

        always:
            if_any ["naked", "redhalf_morgan", "whitetank_morgan"]
            if_all ["pregnant_navel"]
            "morgan_housewife_ending_piercings_pregnant_navel"

    layeredimage morgan househusband ending:
        attribute_function Pickers([CollarPicker, OutfitPicker, PregnancyPicker, PiercingsPicker, HaircutPicker], npc=morgan, use_morgan_cg_outfits=True)
        always:
            "morgan_househusband_ending_bg"

        always:
            "morgan_househusband_ending_morgan"

        attribute makeup

        attribute haircut

        group multiple auto variant piercings

        attribute naked null
        attribute pregnant
        group outfit auto if_not "naked"

        group outfit_pregnant auto if_any "pregnant" if_not "naked"

        attribute collar
        attribute necklace

        always:
            if_any ["naked", "redhalf_morgan", "whitetank_morgan"]
            if_all ["pregnant_navel"]
            "morgan_househusband_ending_piercings_pregnant_navel"

        always:
            "morgan_househusband_ending_fg"

    layeredimage morgan standing:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, PubesPicker, MCCGPicker], npc=morgan, use_morgan_cg_outfits=True)

        attribute nomc null


        group bg auto:
            attribute bedroom default


        group head auto:
            attribute up default


        group eyes auto:
            attribute wide default


        group lips auto if_not "down":
            attribute pinch default


        attribute makeup null
        group makeup auto if_any "makeup"
        group makeup_eyes auto if_all ["up", "makeup"]
        group makeup_lips auto if_all ["up", "makeup"]


        attribute fingering null
        group multiple auto variant fingering when not nomc



        attribute mikemc if_not ["nomc", "pullout"]

        always:
            "morgan_standing_morgan"
        attribute pregnant


        attribute haircut null
        group haircut auto if_any "haircut"


        attribute nipples
        attribute nose if_any "up"


        group dick_out auto if_not ["nomc", "anal", "vaginal", "pullout"]
        group dick auto if_not "nomc"
        always:
            if_not ["nomc", "pullout"]
            "morgan_standing_mc_pubes"


        attribute cum null
        group cum auto if_any "cum" if_not "nomc"
        attribute cumshot null
        group cumshot auto if_all ["cumshot"] if_not ["nomc", "anal", "vaginal", "condom", "pullout"]
        group creampie auto if_all ["cumshot"] if_any ["anal", "vaginal"] if_not ["nomc", "condom"]


        attribute condom null
        group condom_out auto if_all ["condom"] if_not ["nomc", "anal", "vaginal", "pullout"]
        group condom auto if_all ["condom"] if_not "nomc"


        attribute mark
        attribute spank if_not "pullout"


    layeredimage morgan clawmachine:
        attribute_function Pickers([HaircutPicker, OutfitPicker], npc=morgan)

        attribute date null
        attribute sexydate null
        attribute halloween null
        attribute sport null
        attribute sexyswimsuit null
        attribute swimsuit null
        attribute necklace null

        always:
            "morgan_clawmachine_bg"


        always:
            "morgan_clawmachine_mikemc"

        always:
            "morgan_clawmachine_body"


        group outfit auto:
            attribute camopants null
            attribute blackpants null
            attribute blackskirt null
            attribute blueskirt null
            attribute blackshorts null
            attribute blackmini null
            attribute nopants null
            attribute sweatpants null
            attribute blacktights null
            attribute redbluebikinibottom null
            attribute bluebikinibottom null
            attribute tuxbottom null


        group face auto:
            attribute natural default


        group hair auto:
            attribute nohaircut default


        always:
            "morgan_clawmachine_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
