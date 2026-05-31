init 1:
    layeredimage scottie kiss:
        attribute_function Pickers([OutfitPicker, MCPicker, HaircutPicker], npc=scottie)

        always "scottie_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "scottie_kiss_bodies_bowsette"

        attribute naked null
        attribute topless null

        group haircuts auto if_not ["bowsette"]:
            attribute mc_nohaircut null


        group outfits auto if_not ["naked", "topless"]:
            attribute swimsuit null
            attribute underwear null
            attribute casual default
            attribute chinese "scottie_kiss_outfits_casual"
            attribute bowsette "scottie_kiss_outfits_halloween"
            attribute invisible "scottie_kiss_outfits_halloween"


        group multiple auto variant mcpiercings
        group mcoutfits auto if_not ["naked", "topless"]

    layeredimage scottie cowgirl:
        attribute_function Pickers([OutfitPicker, MCPicker], npc=scottie)

        group bg auto:
            attribute bedroom default

        always "scottie_cowgirl_bodies_scottie"

        group dick auto if_not ["outside"]

        always "scottie_cowgirl_scottie_pubes" if_not ["outside"]

        attribute creampie

        group breehips auto:
            attribute up default

        group breepubes auto variant "up" if_any "up"
        group breepubes auto variant "down" if_any "down"

        group dick auto if_any ["outside"]:
            attribute outside default

        attribute condom null
        group condom auto if_any "condom"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "condom"
        group cumshot auto variant "condom" if_all ["cumshot", "condom"]

        group pregnancy auto variant "up" if_any "up"
        group pregnancy auto variant "down" if_any "down"

        always "scottie_cowgirl_bodies_breemc"

        group multiple auto variant piercings

        group fx auto

        attribute mc_collar
        attribute leash

        group exp auto:
            attribute normal default

        group haircuts auto

    layeredimage scottie doggy:
        attribute_function Pickers([PubesPicker, MCCGPicker], npc=scottie)

        attribute nonpc null

        group bg auto:
            attribute bedroom default

        always "scottie_doggy_bodies_breemc"
        attribute mc_pubes

        attribute mc_pregnant

        attribute mc_nohaircut null
        attribute mc_haircut

        group multiple auto variant piercings

        attribute mc_collar

        group multiple auto variant spank

        attribute cum if_any "outside"

        group exp auto:
            attribute normal default

        attribute naked null

        group bot_position:
            attribute up null default
            attribute down null

        group bot auto variant "up" if_any "up" if_not "naked"
        group bot auto variant "down" if_any "down" if_not "naked"

        attribute pubes
        group dick auto if_not ["nonpc"]:
            attribute outside default
        attribute condom null
        group condom auto if_any "condom" if_not ["nonpc"]

        attribute creampie null
        group creampie auto if_any "creampie" if_not "condom"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "condom"
        group cumshot auto variant "condom" if_all ["cumshot", "condom"]

        always "scottie_doggy_bodies_scottie" if_not ["nonpc"]

        group fg auto

    layeredimage scottie missionary:
        attribute_function Pickers([PubesPicker, MCCGPicker], npc=scottie)

        attribute nonpc null

        group bg auto:
            attribute bedroom default


        group scottie_fuck auto if_any ["fuck"] if_not ["nonpc"]:
            attribute pose1 default

        always "scottie_missionary_breemc"

        attribute mc_pubes

        attribute mc_pregnant

        attribute mc_nohaircut null
        attribute mc_haircut

        group multiple auto variant piercings

        attribute mc_collar


        group dick auto variant "pose1" if_all ["fuck", "pose1"] if_not ["nonpc"]:
            attribute outside default
        group dick auto variant "pose2" if_all ["fuck", "pose2"] if_not ["nonpc"]:
            attribute outside default
        group dick auto variant "pose3" if_all ["fuck", "pose3"] if_not ["nonpc"]:
            attribute outside default

        attribute pubes null
        group pubes auto variant "pose1" if_all ["fuck", "pose1", "pubes"] if_not ["nonpc"]:
            attribute outside default
        group pubes auto variant "pose2" if_all ["fuck", "pose2", "pubes"] if_not ["nonpc"]:
            attribute outside default
        group pubes auto variant "pose3" if_all ["fuck", "pose3", "pubes"] if_not ["nonpc"]:
            attribute outside default

        attribute condom null
        group condom auto if_any "condom"
        group condom auto variant "pose1" if_all ["fuck", "pose1", "condom"] if_not ["nonpc"]
        group condom auto variant "pose2" if_all ["fuck", "pose2", "condom"] if_not ["nonpc"]
        group condom auto variant "pose3" if_all ["fuck", "pose3", "condom"] if_not ["nonpc"]

        attribute cumshot null
        group cumshot auto if_all ["fuck", "outside", "cumshot"] if_not ["nonpc", "condom"]
        group condomcum auto if_all ["fuck", "outside", "condom", "cumshot"] if_not ["nonpc"]

        attribute creampie null
        group creampie auto if_any "creampie" if_not "condom"

        group hands auto
        group multiple auto variant piercings_vaginal when vaginal

        group exp auto:
            attribute normal default

        group arms auto:
            attribute up default

        attribute speed

        group scottie auto if_not ["nonpc"]:
            attribute fuck null default

        group cum auto

    layeredimage scottie beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[scottie], append_npc_from_attributes=True)

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


        always "scottie_beats_scottie"
        group outfit auto if_not ["naked"]

        always "scottie_beats_fx"


    layeredimage breemc scottie spoon:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=scottie)


        group bg auto:
            attribute bedroom1 default


        always "breemc_scottie_spoon_bodies"
        group body auto

        attribute mc_haircut:
            "breemc_scottie_spoon_haircut"


        attribute mc_collar:
            "breemc_scottie_spoon_collar"

        attribute mc_pubes:
            "breemc_scottie_spoon_pubes"


        attribute pregnant


        group multiple auto variant piercings


        attribute speed


        group head auto:
            attribute scottie default


        attribute sweat


        attribute bodycum


        group dick auto:
            attribute out default null
        always "breemc_scottie_spoon_dick_out_small" if_all ["out", "scottie"]


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "out"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]
        group condomcum auto if_all ["condom", "cum", "out"]


        group expeyes auto:
            attribute eyes_closed default
        group expmouth auto:
            attribute mouth_pleasure default
        attribute breath if_not ["mouth_pain"]


        group arm auto variant "scottie" if_any ["scottie"]:
            attribute pull default
        group arm auto variant "scottie" if_any ["scottie"]:
            attribute pull default
        attribute speedfinger null
        group speedfinger auto if_all ["speedfinger", "finger"]


        attribute squirt

    layeredimage scottie standing:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=scottie)

        attribute breemc null
        attribute mc_collar null

        group bg auto:
            attribute bedroom default

        group mirror auto if_any "bathroom":
            attribute mc_nohaircut null

        always "scottie_standing_bodies"

        group haircuts auto:
            attribute mc_nohaircut null

        attribute mc_pubes

        group exp auto:
            attribute normal default

        group multiple auto variant piercings:
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_nipples null

        group outfit auto
        group mc_outfit auto

        group dick auto:
            attribute outside default
            attribute anal
            attribute vaginal

        attribute condom null
        group condom auto if_any "condom"

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute cumshot null
        group cumshot auto if_any "cumshot"



        always "scottie_standing_fx"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
