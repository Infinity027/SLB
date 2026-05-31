init 1:
    layeredimage shawn kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, MCCGPicker], npc=shawn)


        attribute breemc null
        always "shawn_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "shawn_kiss_body_shawn"


        attribute collar


        attribute mc_pregnant


        attribute mc_collar


        group multiple auto variant piercings


        attribute mc_naked null
        group mc_outfit auto if_not ["mc_pregnant", "mc_naked"]
        group mc_outfit auto variant "pregnant" if_any ["mc_pregnant"] if_not ["mc_naked"]


        attribute naked null
        group shawn_outfit auto if_not ["naked"] :
            attribute casual default
            attribute chinese "shawn_kiss_shawn_outfit_casual"
            attribute bowsette "shawn_kiss_shawn_outfit_halloween"
            attribute invisible "shawn_kiss_shawn_outfit_halloween"


        attribute mc_haircut if_not ["bowsette"]
        attribute mc_nohaircut null


    layeredimage shawn beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[shawn], append_npc_from_attributes=True)

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


        always "shawn_beats_shawn"
        group outfit auto if_not ["naked"]

        always "shawn_beats_fx"

    layeredimage shawn foreplay:
        attribute_function Pickers([MCCGPicker])


        always "shawn_foreplay_bree"


        attribute mc_haircut


        group piercings auto

    layeredimage shawn reverse cowgirl:
        attribute_function Pickers([MCCGPicker])

        attribute nomc null
        attribute breemc null

        group bg auto:
            attribute bedroom default

        always:
            "shawn_reverse_cowgirl_breemc_legback"

        group hand auto

        always:
            "shawn_reverse_cowgirl_shawn"

        group body_position auto:
            attribute up null default
            attribute down null

        group body auto variant "down" if_any "down"
        group body auto variant "up" if_any "up"

        group pregnancies auto variant "down" if_any "down"
        group pregnancies auto variant "up" if_any "up"

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        group multiple auto variant piercings_down when down
        group multiple auto variant piercings_up when up

        group acc auto variant "down" if_any "down"
        group acc auto variant "up" if_any "up"

        group haircuts auto variant "down" if_any "down"
        group haircuts auto variant "up" if_any "up"

        group eyes_exp auto:
            attribute back null default
            attribute ahegao null
            attribute closed null
            attribute wink null

        group eyes auto variant "down" if_any "down"
        group eyes auto variant "up" if_any "up"

        group mouth_exp auto:
            attribute normal null default
            attribute ahegao null
            attribute pleasure null
            attribute smile null

        group mouth auto variant "down" if_any "down"
        group mouth auto variant "up" if_any "up"

        group dick_positions auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        always:
            "shawn_reverse_cowgirl_shawn_pubes"

        group dick auto variant "down" if_any "down"
        group dick auto variant "up" if_any "up"

        attribute condom null
        group condom_up auto if_any "condom" if_not "down"

        attribute cumshot
        attribute creampie null
        group creampie auto variant "down" if_all ["down", "creampie"]
        group creampie auto variant "up" if_all ["up", "creampie"]

        attribute cum null
        group cum auto variant "down" if_all ["down", "cum"]
        group cum auto variant "up" if_all ["up", "cum"]

        group fx auto variant "down" if_any "down"
        group fx auto variant "up" if_any "up"

        group fg auto

    layeredimage shawn doggy:
        attribute_function Pickers([MCCGPicker])

        attribute nonpc null

        group bg auto:
            attribute bedroom default

        attribute breemc

        attribute mc_pregnant

        attribute buttplug

        attribute floats

        attribute mc_haircut
        attribute mc_nohaircut null

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        attribute mc_pubes

        attribute cum null
        group cum auto if_any "cum"

        group eyes auto:
            attribute back default

        group mouth auto:
            attribute normal default

        group shawn auto if_not "nonpc":
            attribute far default

        attribute hand

        group dick_positions auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out" if_not "nonpc"
        group dick auto variant "vaginal" if_any "vaginal" if_not "nonpc"
        group dick auto variant "anal" if_any "anal" if_not "nonpc"

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto variant "vaginal" if_all ["vaginal", "condom"]

        attribute pubes null default
        group pubes auto variant "out" if_all ["out", "pubes"]
        group pubes auto variant "vaginal" if_all ["vaginal", "pubes"]
        group pubes auto variant "anal" if_all ["anal", "pubes"]

        attribute cumshot

        attribute creampie null
        group creampie auto variant "vaginal" if_all ["vaginal", "creampie"]
        group creampie auto variant "anal" if_all ["anal", "creampie"]

        attribute squirt

        group multiple auto variant fx
        group fg auto


    layeredimage shawn missionary:
        attribute_function Pickers([MCCGPicker])

        attribute breemc null
        attribute mc_pregnant null
        attribute halloween

        group bg auto:
            attribute bedroom default

        always:
            "shawn_missionary_bodies"
        always:
            "shawn_missionary_zombie" if_any "halloween"

        attribute mc_pubes

        attribute mc_halloween

        attribute mc_collar

        attribute mc_haircut

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        group dick auto:
            attribute out default
        group dick auto variant "zombie" if_any "halloween":
            attribute out default

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute condom null
        group condom auto if_any "condom"

        attribute squirt

        group eyes auto:
            attribute normal default

        group mouth auto:
            attribute closed default

        group multiple auto variant fx
        group fg auto

    layeredimage shawn cowgirl:
        attribute_function Pickers([MCCGPicker])

        attribute breemc null
        attribute naked null
        attribute mc_naked null
        attribute dominatrix null

        group bg auto:
            attribute bedroom default

        always:
            "shawn_cowgirl_bodies"

        attribute mc_collar
        attribute mc_pregnant

        group top auto if_not ["mc_naked", "naked"]

        attribute hand

        group haircuts auto

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_nose null
            attribute mc_tongue null

        group piercings auto variant "vaginal" if_any "vaginal"

        attribute mc_pubes

        group stockings auto if_not ["mc_naked", "naked", "mc_pregnant"]
        group stockings auto variant "pregnant" if_any "mc_pregnant" if_not ["mc_naked", "naked"]
        group garterbelt auto if_not ["mc_naked", "naked", "mc_pregnant"]
        group garterbelt auto variant "'pregnant'" if_any "mc_pregnant" if_not ["mc_naked", "naked"]


        group dick auto:
            attribute out default

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute condom null
        group condom auto if_any "condom"

        attribute cum null
        group cum auto if_any "cum"

        attribute cumshot

        group eyes auto:
            attribute normal default

        group mouth auto:
            attribute closed default

        group multiple auto variant fx

    layeredimage shawn standing:
        attribute_function Pickers([MCCGPicker])

        attribute breemc null

        group dry_wet auto:
            attribute dry null default
            attribute wet null

        group bg auto:
            attribute bedroom default

        always:
            "shawn_standing_bodies"

        attribute mc_pregnant
        attribute mc_collar

        group chest auto:
            attribute still default

        group haircuts auto variant "dry" if_any "dry"
        group haircuts auto variant "wet" if_any "wet"

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        group piercings auto variant "still" if_any "still"
        group piercings auto variant "shake" if_any "shake"

        attribute cum null
        group cum auto if_any "cum"

        attribute cumshot

        group eyes auto:
            attribute normal default

        group mouth auto:
            attribute closed default

        group multiple auto variant fx
        group fg auto


    layeredimage shawn ending:
        attribute_function Pickers([MCCGPicker, EndingKidPicker], npc=shawn)

        attribute breemc null
        attribute mc_casual null
        attribute mc_clit null
        attribute mc_ears null
        attribute mc_lips null
        attribute mc_navel null
        attribute mc_nipples null
        attribute mc_nose null
        attribute mc_pubes null
        attribute mc_tongue null


        attribute bg


        attribute bodies
        group haircuts auto if_any "bodies":
            attribute mc_nohaircut null
        always:
            "shawn_ending_shotgun" if_any "bodies"


        attribute fire


        attribute mc_pregnant null
        group baby auto if_all ["bodies", "mc_pregnant"]:
            attribute white default
            attribute afro
            attribute latin

        group baby_white_hair auto if_all ["bodies", "mc_pregnant"] if_not ["afro", "latino"]:
            attribute black
            attribute blond default
            attribute brown
            attribute red


        attribute zombie2
        attribute zombie3
        attribute zombie1
        attribute zombie4
        attribute zombies

    layeredimage insert shawn whip:

        always:
            "insert_shawn_whip_shawn"
        group multiple auto variant slash

    layeredimage palla death:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, MCCGPicker], npcs=[palla])


        always:
            "palla_death_bg"



        attribute nomc null
        always when not nomc:
            "palla_death_breeshadow"
        always when not nomc:
            "palla_death_breemc"
        attribute mc_haircut
        attribute mc_pregnant

        group multiple auto variant mcpiercings when not nomc

        group mcoutfit auto when not nomc
        group mcoutfit auto variant mc_pregnant when mc_pregnant and not nomc



        always:
            "palla_death_pallabody"
        attribute palla_pregnant

        attribute palla_collar

        group multiple auto variant piercings
        group multiple:
            attribute palla_clit null
            attribute palla_ears null
            attribute palla_navel null
            attribute palla_nipples null
            attribute palla_nose null
            attribute palla_pregnant_navel null

        group outfit auto:
            attribute date default
            attribute sexydate null
            attribute sluttydate null
        group outfit auto variant pregnant when pregnant:
            attribute date default
            attribute sexydate null
            attribute sluttydate null


        always:
            "palla_death_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
