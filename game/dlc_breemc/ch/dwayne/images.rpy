init 1:
    layeredimage dwayne kiss:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=dwayne)

        attribute breemc null
        attribute mc_collar null
        attribute mc_pregnant null

        attribute naked null
        attribute topless null

        always "dwayne_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "dwayne_kiss_bodies_bowsette"

        attribute mc_haircut if_not ["bowsette"]
        attribute mc_nohaircut null


        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null
            attribute mc_clit null
            attribute mc_lips null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null
        group mcoutfits auto if_not ["naked", "topless"]


        group outfits auto if_not ["naked", "topless"]:
            attribute swimsuit null
            attribute underwear null
            attribute casual default
            attribute chinese "dwayne_kiss_outfits_casual"
            attribute bowsette null
            attribute invisible null

    layeredimage dwayne forced kiss:
        attribute_function Pickers([MCCGPicker], npc=dwayne)
        attribute breemc null
        always:
            "dwayne_forced_kiss_bodies"
        attribute mc_haircut
        attribute mc_nohaircut null

        attribute mc_pregnant null
        attribute mc_pubes null

        group mc_outfits:
            attribute mc_casual null

        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null
            attribute mc_clit null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

    layeredimage dwayne grab cheeks:
        attribute_function Pickers([MCCGPicker], npc=dwayne)

        attribute breemc null
        always:
            "dwayne_grab_cheeks_bodies"
        attribute mc_haircut
        attribute mc_nohaircut null

        attribute mc_naked null
        attribute mc_topless null

        attribute mc_pregnant null
        attribute mc_pubes null


        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null
            attribute mc_clit null
            attribute mc_navel null
            attribute mc_pregnant_navel null

        group mcoutfits auto if_not ["mc_naked", "mc_topless"]

    layeredimage dwayne missionary:
        attribute_function Pickers([MCCGPicker], npc=dwayne)

        attribute nonpc null

        group outfits:
            attribute mc_casual null

        group bg auto:
            attribute bedroom default

        always:
            if_not "nonpc"
            "dwayne_missionary_dwayne_legs"

        group dwayne_body auto if_not "nonpc":
            attribute far default

        attribute breemc

        attribute mc_nohaircut null
        attribute mc_haircut
        attribute mc_pubes

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_tongue null

        attribute mc_pregnant

        group dick auto if_not "nonpc":
            attribute out default

        attribute condom null

        group condoms auto if_any "condom" if_not "nonpc"

        attribute cum null

        group cum auto if_any "cum" if_not "nonpc"

        always:
            if_not "nonpc"
            "dwayne_missionary_dwayne_pubes"

        attribute blush

        group eyes auto:
            attribute down default

        group mouth auto:
            attribute smile default

        group nipples auto:
            attribute nofx default
        group piercings auto variant "normal" if_not ["pinch", "speed"]
        group piercings auto variant "pinch" if_any "pinch"
        group piercings auto variant "speed" if_any "speed"

        group dwayne_arms auto:
            attribute waist null default
            attribute pinch null
            attribute choke null

        group dwayne_arms_far auto variant "nopregnant" if_any "far" if_not ["nonpc", "mc_pregnant"]

        group dwayne_arms_far auto variant "pregnant" if_all ["far", "mc_pregnant"] if_not ["nonpc"]

        group dwayne_arms_near auto if_any "near" if_not "nonpc"

        group multiple auto variant fx

        always:
            "dwayne_missionary_fg"


    layeredimage dwayne stand:
        attribute_function Pickers([MCCGPicker], npc=dwayne)

        attribute breemc null
        attribute mc_pubes null

        group mc_outfits:
            attribute mc_casual null

        group bg auto:
            attribute bedroom default

        group bodies auto:
            attribute up default

        attribute mc_pregnant null
        group mc_pregnant auto if_any ["mc_pregnant"]

        group mouths auto variant "up" if_any ["up"]:
            attribute mouth_normal default
        group mouths auto variant "down" if_any ["down"]:
            attribute mouth_normal default

        attribute blush null
        group blush auto if_any ["blush"]
        attribute fear null
        group fear auto if_any ["fear"]

        group eyes auto variant "up" if_any ["up"]:
            attribute eyes_open default
        group eyes auto variant "down" if_any ["down"]:
            attribute eyes_open default

        attribute mc_nohaircut null
        attribute mc_haircut null
        group mc_haircut auto if_any ["mc_haircut"]

        group piercings multiple:
            attribute mc_ears null
        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_down when down

        group arms auto

        group dick auto variant "up" if_any ["up"]
        group dick auto variant "down" if_any ["down"]

        attribute condom null
        group condom auto variant "up" if_all ["up", "condom"]
        group condom auto variant "down" if_all ["down", "condom"]

        attribute cum null
        group cum auto variant "up" if_all ["up", "cum"] if_not ["condom"]
        group cum auto variant "down" if_all ["down", "cum"] if_not ["condom"]

        attribute openpussy null
        group openpussy auto if_all ["openpussy"]

        attribute vaginaldrip null
        group vaginaldrip auto if_all ["vaginaldrip", "openpussy"]

        group hands auto variant "openpussy" if_any ["openpussy"]
        group hands auto variant "default" if_not ["openpussy"]

        group dick:
            attribute out default
            attribute vaginal null
            attribute anal null
        attribute twitch if_any ["out"]
        group condom auto if_any ["condom"] if_not ["cum"]
        group condomcum auto if_all ["condom", "cum"]
        group cum auto if_any ["cum"] if_not ["condom"]

    layeredimage dwayne blowjob:
        attribute_function Pickers([OutfitPicker, PubesPicker, MCCGPicker], npc=dwayne)

        attribute naked null


        group bg auto:
            attribute bedroom default


        always "dwayne_blowjob_dwayne"
        group bot auto if_not ["naked"]


        always "dwayne_blowjob_bree"
        group multiple auto variant piercings
        group mc_outfits auto if_not ["naked"]


        always "dwayne_blowjob_dwayneballs"


        group position auto:
            attribute up default


        attribute mc_nose null
        group mc_nose auto if_any ["mc_nose"]


        attribute mc_haircut null
        group mc_haircut auto if_any ["mc_haircut"]


        attribute onface null
        group onface auto if_all ["onface", "out", "hard"]


        group eyes auto variant "up" if_any ["up"] if_not ["onface"]:
            attribute opened default
        group eyes auto variant "up" if_all ["up", "onface"] if_not ["hard"]:
            attribute opened default
        group eyes auto variant "up" if_all ["up", "onface"] if_not ["out"]:
            attribute opened default
        group eyes auto variant "mid" if_any ["mid"] if_not ["onface"]:
            attribute opened default
        group eyes auto variant "mid" if_all ["mid", "onface"] if_not ["hard"]:
            attribute opened default
        group eyes auto variant "mid" if_all ["mid", "onface"] if_not ["out"]:
            attribute opened default
        group eyes auto variant "down" if_any ["down"] if_not ["onface"]:
            attribute opened default
        group eyes auto variant "down" if_all ["down", "onface"] if_not ["hard"]:
            attribute opened default
        group eyes auto variant "down" if_all ["down", "onface"] if_not ["out"]:
            attribute opened default


        group mouth auto variant "up" if_all ["up", "out"] if_not ["onface"]:
            attribute normal default
        group mouth auto variant "up" if_all ["up", "out", "onface"] if_not ["hard"]:
            attribute normal default
        group mouth auto variant "mid" if_all ["mid", "out"] if_not ["onface"]:
            attribute normal default
        group mouth auto variant "mid" if_all ["mid", "out", "onface"] if_not ["hard"]:
            attribute normal default
        group mouth auto variant "down" if_all ["down", "out"] if_not ["onface"]:
            attribute normal default
        group mouth auto variant "down" if_all ["down", "out", "onface"] if_not ["hard"]:
            attribute normal default


        attribute mouthcum null
        group mouthcum auto if_all ["mouthcum", "tongueout", "out"] if_not ["onface"]


        attribute dwaynehand null
        group dwaynehand auto if_any ["dwaynehand"]
        group sleeves auto variant "up" if_all ["up", "dwaynehand"] if_not ["naked"]
        group sleeves auto variant "mid" if_all ["mid", "dwaynehand"] if_not ["naked"]
        group sleeves auto variant "down" if_all ["down", "dwaynehand"] if_not ["naked"]


        group lockofhair auto if_all ["mc_haircut", "dwaynehand"]


        group dicks:
            attribute out null default
            attribute suck null
        group dick_out auto if_any ["out"]:
            attribute hard default
        group dick_suck auto if_any ["suck"]


        attribute cum null
        group cum_out auto if_all ["cum", "out"]
        group cum_suck auto if_all ["cum", "suck"]


        attribute pubes

    layeredimage dwayne carwindow:


        always "dwayne_carwindow_bg"


        attribute casual
        attribute date null


        group window:
            attribute down null default
            attribute middle
            attribute up

    layeredimage dwayne limo:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, PubesPicker, MCPicker], npc=dwayne)






        always "dwayne_limo_sit"


        attribute dwayne
        always:
            if_any "dwayne"
            "dwayne_limo_dexp"

        attribute blush


        always:

            "dwayne_limo_pubes"



        attribute dnaked null
        group dwayne_outfits auto if_not ["dnaked"]:
            attribute dcasual default


        group dick auto:
            attribute dnaked default
        group dick auto variant "casual" if_any ["dcasual"] if_not ["dnaked", "ddate"]:
            attribute right default
        group dick auto variant "date" if_any ["ddate"] if_not ["dnaked", "dcasual"]:
            attribute right default



        attribute bree
        always:
            if_any "bree"
            "dwayne_limo_bexp"

        group multiple auto variant piercings

        attribute bree_haircut


        attribute bnaked null
        group bree_outfits auto if_any ["bree"] if_not ["bnaked"]:
            attribute casual default

    layeredimage dwayne beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[dwayne], append_npc_from_attributes=True)

        attribute nomc null
        attribute naked null


        attribute breemc if_not ["nomc"]
        attribute mc_haircut if_not ["nomc"]
        attribute mc_pregnant if_not ["nomc"]
        group multiple auto variant mc_piercings when not nomc
        group mc_outfit auto if_not ["nomc", "naked"]
        group mc_pregnant_outfit auto if_any ["mc_pregnant"] if_not ["nomc", "naked"]
        attribute mc_collar if_not ["nomc"]


        always "dwayne_beats_dwayne"
        group naked auto if_any ["naked"]
        group outfit auto if_not ["naked"]


        group foe auto
        group foe_outfit auto if_not ["naked"]
        group dwaynehand auto

        always "dwayne_beats_fx"


    layeredimage dwayne office blowjob female:
        attribute_function MultiPickers([MCCGPicker, PiercingsPicker, HaircutPicker], npcs=[dwayne, aletta])

        attribute nomc null
        attribute nonpc null

        attribute aletta null
        attribute breemc null
        attribute dwayne null

        always "dwayne_office_blowjob_female_bg_ceo"



        always:
            if_not ["nonpc"]
            if_any ["nomc"]
            "dwayne_office_blowjob_female_aletta_back"

        always:
            if_not ["nomc"]
            if_any ["nonpc"]
            "dwayne_office_blowjob_female_mc_back"

        always:
            "dwayne_office_blowjob_female_dwayne"

        always:
            if_not ["nomc", "nonpc"]
            "dwayne_office_blowjob_female_bodies_aletta_breemc"

        always:
            if_not ["nonpc"]
            if_any ["nomc"]
            "dwayne_office_blowjob_female_aletta_body"

        always:
            if_not ["nomc"]
            if_any ["nonpc"]
            "dwayne_office_blowjob_female_mc_body"

        group multiple auto variant piercings_nonpc when nonpc and not nomc
        group multiple auto variant piercings_nomc when nomc and not nonpc
        group multiple auto variant piercings_both when not (nomc or nonpc)


        group mchead auto if_not "nomc":
            attribute mcup default

        group mc_haircuts:
            attribute mc_haircut null
            attribute mc_nohaircut null
        group mcnohaircuts auto if_any "mc_nohaircut" if_not "nomc"
        group mchaircuts auto if_any "mc_haircut" if_not "nomc"



        group aletta_haircuts:
            attribute aletta_haircut null
            attribute aletta_nohaircut null

        group alettanohaircuts auto if_any "aletta_nohaircut" if_not "nonpc"

        group alettahead auto if_not "nonpc":
            attribute alettaup default

        attribute alettatongue if_not "alettablow"

        group alettaeyes auto if_any "alettablow" if_not "nonpc":
            attribute opened default

        group alettahaircuts auto if_any "aletta_haircut" if_not "nonpc"

        group dick_positions:
            attribute noblow null default
            attribute alettablow null
            attribute mcblow null

        group dick auto variant "nonpc" if_any "nonpc" if_not "nomc"
        group dick auto variant "nomc" if_any "nomc" if_not "nonpc"
        group dick auto variant "both" if_not ["nomc", "nonpc"]

        group multiple auto variant cum

        attribute cumshot
        attribute dickcum
        attribute speed
        always:
            "dwayne_office_blowjob_female_dwayne_hands"

    layeredimage dwayne foreplay finger:

        attribute_function Pickers([MCCGPicker])


        group bg auto:
            attribute bedroom default


        always "dwayne_foreplay_finger_bodies"
        attribute mc_pregnant


        attribute mc_collar
        group multiple auto variant piercings


        group haircut auto


        always "dwayne_foreplay_finger_dwayne_eyes"
        group eyes auto:
            attribute closed default

        attribute fingering
        attribute blush
        attribute sweaty
        attribute wet
        attribute squirt

    layeredimage dwayne cowgirl:
        attribute_function Pickers([MCCGPicker, OutfitPicker], npc=dwayne)

        attribute naked null
        attribute mc_naked null

        always "dwayne_cowgirl_bg"
        always "dwayne_cowgirl_bodies"

        group mchaircuts auto:
            attribute mc_nohaircut null

        attribute mc_pubes
        attribute bulge

        attribute mc_collar

        group exp auto:
            attribute normal default

        attribute mc_pregnant

        group multiple auto variant mcpiercings

        group top auto when not mc_pregnant and not mc_naked
        group top auto variant pregnant when mc_pregnant and not mc_naked
        group bot auto when not mc_naked
        group hat auto when not mc_naked

        group outfit auto when not naked
        group belt auto when not naked

        attribute creampie

        attribute squirt

        attribute speed

        always "dwayne_cowgirl_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
