init 1:
    layeredimage master kiss:
        attribute_function Pickers([OutfitPicker, MCPicker], npc=master)

        attribute breemc null

        attribute naked null
        attribute topless null


        always "master_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "master_kiss_bodies_bowsette"

        attribute mc_nose

        attribute mc_nohaircut null
        attribute mc_haircut if_not ["bowsette"]


        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute sport null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute casual default
            attribute chinese "master_kiss_outfits_casual"
            attribute bowsette "master_kiss_outfits_date"
            attribute invisible "master_kiss_outfits_date"


        group mcoutfits auto if_not ["naked", "topless"]

    layeredimage master bj:
        attribute_function Pickers([MCCGPicker], npc=master)
        always:
            "master_bj_bg"

        attribute breemc

        attribute mc_pubes
        group bot auto if_not "naked"
        attribute mc_pregnant

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null

        group hand auto if_not "handjob":
            attribute back default

        attribute naked null
        group top auto if_not "naked":
            attribute mc_karate default

        group top auto variant "pregnant" if_any "mc_pregnant" if_not "naked"

        attribute mc_haircut
        attribute mc_nohaircut null

        group eyes auto:
            attribute opened default

        group mouth auto if_not "suck":
            attribute normal default

        group sex_action:
            attribute still null default
            attribute suck null
            attribute lick null

        group dick auto variant "far" if_all ["far"]
        group dick auto variant "close" if_all ["close"]

        group hand_position auto:
            attribute down null default
            attribute up null
        group hand auto variant "down" if_all ["handjob", "down"]
        group hand auto variant "up" if_all ["handjob", "up"]

        group sleeve auto variant handjob when handjob and mc_karate and not naked

        group body auto

        group pubes auto

        attribute aura if_all ["still", "close"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        attribute cum null
        group cum auto if_any "cum"
        group insert auto


    layeredimage master sixtynine:
        attribute_function Pickers([MCCGPicker], npc=master)

        group bg auto:
            attribute beach default

        always:
            "master_sixtynine_bodies_master"

        attribute breemc

        attribute naked null
        group outfits auto if_not "naked":
            attribute mc_karate default

        always:
            "master_sixtynine_masterhands_tight"

        group haircuts auto

        group mouth auto if_not "blow":
            attribute normal default

        group multiple auto variant piercings

        group eyes auto:
            attribute open default

        group dicks_master auto:
            attribute out default

        group breehands auto:
            attribute still default

        attribute cumshot null
        group cumshot_master auto if_any "cumshot" if_not "blow"
        attribute cum null
        group cum auto if_any "cum"

        group fx auto
        group fg auto


    layeredimage master beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[master], append_npc_from_attributes=True)

        attribute nomc null
        attribute naked null


        attribute breemc if_not ["nomc"]
        attribute mc_haircut if_not ["nomc"]
        attribute mc_pregnant if_not ["nomc"]
        group multiple auto variant mc_piercings when not nomc
        group mc_outfit auto if_not ["nomc", "naked"]
        group mc_pregnant_outfit auto if_any ["mc_pregnant"] if_not ["nomc", "naked"]
        attribute mc_collar if_not ["nomc"]
        always "master_beats_fx_kiball" if_not ["nomc"]


        always "master_beats_master"
        group outfit auto if_not ["naked"]
        always "master_beats_kiball"


        group foe auto
        group foe_naked auto if_any ["naked"]
        group foe_outfit auto if_not ["naked"]

    layeredimage watermelon:

        always "master_watermelon"

    layeredimage master cowgirl:
        attribute_function Pickers([MCCGPicker, OutfitPicker], npc=master)
        attribute breemc null
        attribute mc_nohaircut null
        attribute mc_casual
        attribute casual

        always:
            "master_cowgirl_bg"

        always:
            "master_cowgirl_window"

        always:
            "master_cowgirl_bodies"

        always:
            "master_cowgirl_master_eyes"

        always:
            "master_cowgirl_mc_eyes"

        attribute mc_haircut

        attribute mc_pregnant

        attribute naked null
        group outfit auto
        group mc_outfit auto
        always:
            "master_cowgirl_mc_outfit_mc_halloween_normal" if_any "mc_halloween"
        always:
            "master_cowgirl_mc_outfit_mc_halloween_pregnant" if_all ["mc_halloween", "mc_pregnant"]

        group multiple auto variant piercings

        group fx auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
