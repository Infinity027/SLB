init 1:
    layeredimage jack kiss:
        attribute_function Pickers([OutfitPicker, MCPicker], npc=jack)


        always "jack_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "jack_kiss_bodies_bowsette"

        attribute naked null
        attribute topless null


        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute sport null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute chinese "jack_kiss_outfits_casual"
            attribute bowsette "jack_kiss_outfits_halloween"
            attribute invisible "jack_kiss_outfits_halloween"


        attribute mc_nipples
        group mcoutfits auto if_not ["naked", "topless"]

        group haircuts auto if_not ["bowsette"]
        attribute mc_nose
        attribute mc_collar


        group multiple auto variant acc when not naked

    layeredimage jack beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[jack], append_npc_from_attributes=True)

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
        group foe_outfit auto if_not ["naked"]


        always "jack_beats_jack"
        group outfit auto if_not ["naked"]


        group foe_crouch auto if_not ["naked"]
        group foe_crouch auto variant "naked" if_any ["naked"]

        always "jack_beats_fx"

    layeredimage jack handjob:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, CollarPicker], npcs=[bree])
        always:
            "jack_handjob_bg"

        always:
            "jack_handjob_bodies"

        attribute bree_pregnant

        group multiple auto variant piercings

        attribute naked null
        always:
            if_not "naked"
            "jack_handjob_bree_casual"

        always:
            if_not "naked"
            if_any "bree_pregnant"
            "jack_handjob_bree_pregnant_casual"

        always:
            if_not "naked"
            "jack_handjob_jack_casual"

        attribute cumshot

    layeredimage jack blowjob:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, CollarPicker], npcs=[bree])
        always:
            "jack_blowjob_bg"

        always:
            "jack_blowjob_bodies"

        attribute bree_pregnant

        group multiple auto variant piercings

        attribute naked null
        always:
            if_not "naked"
            "jack_blowjob_bree_casual"

        always:
            if_not "naked"
            if_any "bree_pregnant"
            "jack_blowjob_bree_pregnant_casual"

        always:
            if_not "naked"
            "jack_blowjob_jack_casual"

        group cum auto

        group dick auto

    layeredimage jack cowgirl:
        attribute_function Pickers([MCCGPicker], npc=jack)


        group bg auto:
            attribute bedroom default


        always "jack_cowgirl_breeleg"
        always "jack_cowgirl_mc_outfit_leg_mc_halloween" if_any ["mc_halloween"]


        attribute breemc
        group arm auto variant "back"
        attribute mc_haircut
        attribute mc_nohaircut null
        attribute mc_collar
        attribute mc_pregnant
        always "jack_cowgirl_tits_nomove" if_any ["mc_halloween"]
        group tits auto if_not ["cuddle"]:
            attribute nomove default
            attribute bounce if_not ["mc_halloween"]
            attribute suck if_not ["mc_halloween"]
        attribute mc_ears null
        group multiple auto variant piercings when not cuddle
        group multiple auto variant piercings_nomove when nomove and not cuddle
        group arm auto variant "front"
        group arm auto:
            attribute resting default null

        group mc_outfit_body auto:
            attribute mc_naked null default
            attribute mc_halloween if_any ["mc_halloween"]


        always "jack_cowgirl_pose_straight" if_any ["mc_halloween"]

        group pose auto:
            attribute straight default
            attribute cuddle if_not ["mc_halloween"]

        group mc_outfit_arm_mc_halloween auto if_any ["mc_halloween"]


        group exp auto:
            attribute normal default


        group fg auto


    layeredimage jack missionary:
        attribute_function Pickers([MCCGPicker], npc=jack)
        attribute mcalone null


        group bg auto:
            attribute bedroom default


        attribute breemc
        attribute mc_nohaircut null
        attribute mc_haircut
        attribute mc_pubes

        group jack_position auto if_not "mcalone":
            attribute outside default

        attribute mc_pregnant
        attribute mc_collar
        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null

        group exp auto:
            attribute normal default

        attribute condom null
        group condom auto if_any "condom"

        attribute creampie
        attribute cumshot

        group multiple auto variant fx

        attribute insert null
        group insert_bg auto if_any "insert"
        group insert_condom auto if_all ["insert", "condom"]
        group insert_creampie auto if_all ["insert", "creampie"]

    layeredimage jack reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, MCCGPicker], npc=jack)

        group bg auto:
            attribute bedroom4 default

        always "jack_reverse_cowgirl_bree"

        attribute collar
        attribute haircut
        attribute pregnant

        attribute pubes null
        group pubes auto if_any "pubes"

        group multiple auto variant piercings

        group fx auto

        group exp auto:
            attribute normal default

        always "jack_reverse_cowgirl_jack"

        group dick auto:
            attribute out default

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute condom null
        group condom auto if_all "condom"

        attribute cumshot null
        group cumshot auto if_any "cumshot":
            attribute nocondom default


    layeredimage jack doggy:
        attribute_function Pickers([PiercingsPicker, MCCGPicker], npc=jack)

        attribute mcalone null

        group bg auto:
            attribute bedroom4 default

        attribute breemc

        attribute mc_haircut
        attribute mc_nohaircut null

        group beyes auto:
            attribute back default

        group bmouth auto:
            attribute normal default

        attribute mc_pregnant

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null

        attribute fx

        group jack_position auto if_not "mcalone":
            attribute play default

        group jmouth auto if_any "fuck" if_not ["mcalone"]:
            attribute happy default

        group jackarm auto if_not ["mcalone", "fuck"]:
            attribute fingering default

        attribute dildo
        attribute grasp
        attribute hair
        attribute mc_collar

        always:
            if_not ["mcalone", "fuck", "grasp"]
            if_any ["mc_collar"]
            "jack_doggy_ring"

        always:
            if_not ["mcalone", "fuck"]
            if_all ["grasp", "mc_collar"]
            "jack_doggy_leash"

        group front_hair auto if_not ["mcalone", "fuck"] if_all ["grasp", "hair"]

        group fg auto


    layeredimage jack ending:
        attribute_function Pickers([MCCGPicker, EndingKidPicker], npc=jack)

        always:
            "jack_ending_bg"

        always:
            "jack_ending_jack"


        group girl auto if_any ["mc_pregnant"]:
            attribute white null default
            attribute black
            attribute latin null

        always:
            "jack_ending_shelf"

        attribute breemc
        attribute mc_pregnant null
        group haircuts auto:
            attribute mc_nohaircut null

        group girl auto if_any ["mc_pregnant"]:
            attribute white
            attribute black null
            attribute latin

        group hairs auto if_any ["mc_pregnant"] if_not ["black", "latino"]:
            attribute dark null default
            attribute blond
            attribute brown
            attribute red

        always:
            "jack_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
