init 1:
    layeredimage morgan:
        attribute_function Pickers([PositionPicker,  CollarPicker, OutfitPicker, PubesPicker], npc=morgan)

        group outfitbg auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group outfitbg auto variant "b" if_any ["b"] if_not ["topless","naked"]

        group position auto
        attribute pubes null

        group pubes auto if_any "pubes":
            attribute b null

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

        attribute topless null

        attribute collar null
        group collar auto if_any ["collar"]

        attribute necklace null
        group necklace auto if_any ["necklace"] if_not ["collar"]

        group hairs auto

        group top auto variant "a" if_all ["a","halloween"] if_not ["topless","naked"]
        group top auto variant "b" if_all ["b","halloween"] if_not ["topless","naked"]

        attribute makeup null
        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any ["makeup"]:
            attribute normal default

        attribute tongue null
        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage morgan close:
        yalign 0.12
        attribute_function Pickers([PositionPicker,  CollarPicker, OutfitPicker, PubesPicker], npc=morgan)

        group outfitbg auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group outfitbg auto variant "b" if_any ["b"] if_not ["topless","naked"]

        group position auto

        attribute pubes null

        group pubes auto if_any "pubes":
            attribute b null

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
        group bot auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["topless","naked","halloween"]
        group top auto variant "b" if_any ["b"] if_not ["topless","naked","halloween"]

        group acc_top auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_top auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute necklace null
        group necklace auto if_any ["necklace"] if_not ["collar"]

        group hairs auto

        group top auto variant "a" if_all ["a","halloween"] if_not ["topless","naked"]
        group top auto variant "b" if_all ["b","halloween"] if_not ["topless","naked"]

        attribute makeup null
        group exp auto:
            attribute normal default
        group exp auto variant "makeup" if_any ["makeup"]:
            attribute normal default

        attribute tongue null
        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage morgan smartphone:
        always "morgan_smartphone"

    layeredimage morgan mermaidcg:
        attribute_function Pickers([ CollarPicker], npc=morgan)

        always:
            "morgan_mermaidcg_background"

        group hairs auto:
            attribute nohaircut null

        attribute makeup
        attribute collar

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
        attribute_function Pickers([CollarPicker, OutfitPicker,  HaircutPicker], npc=morgan, use_morgan_cg_outfits=True)
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

        attribute naked null

        group outfit auto if_not "naked"

        attribute collar
        attribute necklace

        always:
            if_any ["naked", "redhalf_morgan", "whitetank_morgan"]
            if_all ["pregnant_navel"]
            "morgan_housewife_ending_piercings_pregnant_navel"

    layeredimage morgan househusband ending:
        attribute_function Pickers([CollarPicker, OutfitPicker,  HaircutPicker], npc=morgan, use_morgan_cg_outfits=True)
        always:
            "morgan_househusband_ending_bg"

        always:
            "morgan_househusband_ending_morgan"

        attribute makeup

        attribute haircut

        attribute naked null
        group outfit auto if_not "naked"

        attribute collar
        attribute necklace

        always:
            if_any ["naked", "redhalf_morgan", "whitetank_morgan"]
            if_all ["pregnant_navel"]
            "morgan_househusband_ending_piercings_pregnant_navel"

        always:
            "morgan_househusband_ending_fg"

    layeredimage morgan standing:
        attribute_function Pickers([CollarPicker,  HaircutPicker, PubesPicker, MCCGPicker], npc=morgan, use_morgan_cg_outfits=True)

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
