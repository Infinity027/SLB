init 1:
    layeredimage danny kiss:
        attribute_function Pickers([MCCGPicker, OutfitPicker], npc="danny")
        attribute breemc null
        attribute naked null
        attribute topless null

        attribute mc_pubes null

        always "danny_kiss_bodies"

        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute sport null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute casual default
            attribute chinese "danny_kiss_outfits_casual"
            attribute bowsette "danny_kiss_outfits_date"
            attribute invisible "danny_kiss_outfits_date"

        group mcoutfits auto if_not ["naked", "topless"]

        group mchaircuts auto if_not ["bowsette"]
        always "danny_kiss_haircut_bowsette" if_any "bowsette"

        group mceyes auto:
            attribute closed default

        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null


        group mcacc auto if_not ["naked", "topless"]

    layeredimage danny lapdance:
        attribute_function Pickers([MCPicker], npc="danny")
        always "danny_lapdance_bg"

        attribute nomc null
        always "danny_lapdance_breemc" if_not "nomc"
        attribute mc_haircut if_not "nomc"

        group exp auto if_not "nomc":
            attribute normal default

        group multiple auto variant piercings_breemc when not nomc
        group multiple auto variant piercings_breemc_ahegao when ahegao and not nomc
        group multiple auto variant piercings_breemc_notahegao when not (ahegao or nomc)

        always "danny_lapdance_breemc_sexyoutfit" if_not "nomc"

        group arm auto if_not ["fuck", "nomc"]

        always "danny_lapdance_fg"
        always "danny_lapdance_light"

        attribute fuck

    layeredimage danny blowjob:
        attribute_function Pickers([MCCGPicker], npc="danny")

        attribute breemc null

        group bg auto:
            attribute bedroom default

        always "danny_blowjob_bodies"

        attribute naked null
        always "danny_blowjob_dannycasual" if_not ["naked"]

        attribute mc_collar

        group multiple auto variant piercings

        attribute speed
        attribute mc_naked null
        group outfits auto if_not ["mc_naked"]

        group position auto:
            attribute lick default

        group multiple auto variant null_piercings
        group multiple:
            attribute mc_ears null
        group multiple auto variant piercings_lick when lick
        group multiple auto variant piercings_suck when suck
        group multiple auto variant piercings_deepthroat when deepthroat

        attribute mc_nohaircut null
        group haircuts auto variant "lick" if_any ["lick"]
        group haircuts auto variant "suck" if_any ["suck"]
        group haircuts auto variant "deepthroat" if_any ["deepthroat"]

        group mouth auto variant "lick" if_any ["lick"]:
            attribute normal default
        group eyes auto variant "lick" if_any ["lick"]:
            attribute opened default
        group eyes auto variant "suck" if_any ["suck"]:
            attribute opened default
        group eyes auto variant "deepthroat" if_any ["deepthroat"]:
            attribute opened default

        group dick auto:
            attribute lick null
        group dick_lick auto if_any ["lick"]:
            attribute limp default

        attribute cum null
        group cum auto if_any ["cum"]
        group cum auto variant "lick" if_all ["cum", "lick"]

        attribute facecum if_any ["lick"]
        attribute bodycum if_all ["lick", "hard"]

        group fg auto

    layeredimage danny stand:
        attribute_function Pickers([MCCGPicker], npc="danny")

        attribute mc_casual null


        group bg auto:
            attribute bedroom default
        attribute knock if_any ["bedroom"]


        attribute breemc
        attribute mc_pubes
        group multiple auto variant mc_piercings
        group multiple:
            attribute mc_ears null


        group mc_outfit auto:
            attribute mc_halloween
            attribute mc_naked null default


        attribute analgape
        attribute analdrip if_any ["analgape"]
        attribute vaginaldrip


        group mouth auto:
            attribute mouth_hurt default
        group eyes auto:
            attribute eyes_scared default


        attribute mc_nohaircut
        attribute mc_haircut


        attribute alone null
        group danny auto if_not ["alone"]:
            attribute fuck default


        always "danny_stand_pinkstrand" if_any ["mc_haircut"] if_not ["alone"]


        group dick if_any ["fuck"] if_not ["alone"]:
            attribute vaginal
            attribute anal
        attribute cum null
        group cum if_all ["fuck", "cum"] if_not ["condom", "alone"]:
            attribute vaginal
        group cum if_all ["fuck", "cum"] if_not ["alone"]:
            attribute anal
        attribute condom null
        group condom if_all ["fuck", "condom"] if_not ["alone"]:
            attribute vaginal


        attribute squirt


        group dick if_any ["fuck"] if_not ["alone"]:
            attribute out default
        group cum if_all ["fuck", "cum"] if_not ["condom", "alone"]:
            attribute out default
        group condom if_all ["fuck", "condom"] if_not ["cum", "alone"]:
            attribute out default
        group condomcum if_all ["fuck", "condom", "cum"] if_not ["alone"]:
            attribute out default


    layeredimage danny doggy:
        attribute_function Pickers([MCCGPicker], npc="danny")

        group breemc_head:
            attribute up null default
            attribute down null


        group bg auto:
            attribute bedroom default

        attribute squirt
        attribute creampie


        attribute breemc
        group piercings auto:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_tongue null


        attribute nonpc null
        always if_not ["nonpc"]:
            "danny_doggy_danny"

        always if_not ["nonpc"]:
            "danny_doggy_left_hand"

        group hairs auto if_all ["down", "head"] if_not ["nonpc"]

        group right_hand auto if_not ["nonpc"]:
            attribute ass default
            attribute head if_any "down"

        group dick auto if_not ["nonpc"]:
            attribute out default
            attribute vaginal null
            attribute anal null

        group head auto variant "up" if_any "up"
        group head auto variant "down" if_any "down"


        group mouth_layers:
            attribute hurt default null
            attribute pleasure null
            attribute ahegao null

        group mouth auto variant "up" if_any "up"
        group mouth auto variant "down" if_any "down"

        group eyes_layers:
            attribute normal default null
            attribute closed null
            attribute rolled null

        group eyes auto variant "up" if_any "up"
        group eyes auto variant "down" if_any "down"

        group piercings auto variant "up" if_any "up"
        group piercings auto variant "down" if_any "down"

        attribute breath if_not "up"

        attribute condom if_any "out" if_not ["nonpc"]
        attribute cum if_not ["condom", "nonpc"]
        attribute cumshot if_not ["condom", "nonpc"]

        attribute speed

        group multiple auto variant acc

        group fg auto

    layeredimage danny beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[danny], append_npc_from_attributes=True)

        attribute nomc null
        attribute naked null


        attribute breemc if_not ["nomc"]
        attribute mc_haircut if_not ["nomc"]
        attribute mc_pregnant if_not ["nomc"]
        group multiple auto variant mc_piercings when not nomc
        group mc_outfit auto if_not ["nomc", "naked"]
        group mc_pregnant_outfit auto if_any ["mc_pregnant"] if_not ["nomc", "naked"]
        attribute mc_collar if_not ["nomc"]


        group foe auto
        group foe_naked auto if_any ["naked"]
        group foe_outfit auto if_not ["naked"]


        always "danny_beats_danny"
        group outfit auto if_not ["naked"]


        group foe_head auto
        group foe_acchead auto if_not ["naked"]

    layeredimage danny punched:
        attribute_function Pickers([MCCGPicker])

        attribute mc_casual null
        attribute mc_nohaircut null

        group danny auto:
            attribute missed default

        attribute breemc
        attribute mc_haircut

        group arm auto

        always "danny_punched_mc_casual"
        group arm_outfit auto

        attribute mc_pregnant null
        always "danny_punched_pregnant_mc_casual" if_any "mc_pregnant"

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null
        attribute mc_collar
        group exp auto:
            attribute hit null

        group fx auto

    layeredimage danny faceslap:
        attribute_function Pickers([MCCGPicker])

        attribute breemc null
        group breemc auto:
            attribute missed default

        group haircuts auto variant "hit" if_any "hit":
            attribute mc_nohaircut null
        group haircuts auto variant "missed" if_any "missed":
            attribute mc_nohaircut null

        attribute mc_casual null
        always "danny_faceslap_outfit_hit_mc_casual" if_any "hit"
        always "danny_faceslap_outfit_missed_mc_casual" if_any "missed"

        attribute mc_pregnant null
        always "danny_faceslap_outfit_pregnant_hit_mc_casual" if_all ["hit", "mc_pregnant"]
        always "danny_faceslap_outfit_pregnant_missed_mc_casual" if_all ["missed", "mc_pregnant"]

        group multiple auto variant piercings_hit when hit
        group multiple:
            attribute mc_clit null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null

        group multiple auto variant piercings_missed when missed
        group multiple:
            attribute mc_clit null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null

        group collars auto variant "hit" if_any "hit"
        group collars auto variant "missed" if_any "missed"

        always "danny_faceslap_danny"
        group fx auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
