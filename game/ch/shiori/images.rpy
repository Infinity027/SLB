init 1:
    layeredimage shiori:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=shiori)


        attribute idle null


        group tail auto


        group position auto:
            attribute _a "shiori_position_a"
            attribute _b "shiori_position_b"


        group hair auto variant a when a or _a
        group hair auto variant b when b or _b
        group hair auto variant c when c


        attribute pubes when not (a or _a)
        attribute pubes variant c when c
        attribute pubes variant d when d


        attribute pregnant null
        group pregnant auto when pregnant


        always "shiori_boobs_d" when d and not pressed


        attribute ears null
        group multiple auto variant piercings_a when a or _a
        group multiple auto variant piercings_b when b or _b
        group multiple auto variant piercings_c when c
        group multiple auto variant piercings_d when d


        attribute naked null

        group stockings auto variant a when (a or _a) and not (bottomless or naked)
        group stockings auto variant b when (b or _b) and not (bottomless or naked)
        group stockings auto variant c when c and not (bottomless or naked)
        group stockings auto variant d when d and not (bottomless or naked)

        attribute bottomless null
        group bot auto variant a when (a or _a) and not (pregnant or bottomless or naked)
        group bot auto variant b when (b or _b) and not (pregnant or bottomless or naked)
        group bot auto variant c when c and not (pregnant or bottomless or naked)
        group bot auto variant d when d and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when ((a or _a) and pregnant) and not (bottomless or naked)
        group bot auto variant b_pregnant when ((b or _b) and pregnant) and not (bottomless or naked)
        group bot auto variant c_pregnant when (c and pregnant) and not (bottomless or naked)
        group bot auto variant d_pregnant when (d and pregnant) and not (bottomless or naked)

        group necklace auto variant c when c and not (collar or naked or topless)
        group necklace auto variant d when d and not (collar or naked or topless)

        attribute topless null
        group top auto variant a when (a or _a) and not (pregnant or topless or naked)
        group top auto variant b when (b or _b) and not (pregnant or topless or naked)
        group top auto variant c when c and not (pregnant or topless or naked)
        group top auto variant d when d and not (pregnant or topless or naked)
        group top auto variant a_pregnant when ((a or _a) and pregnant) and not (topless or naked)
        group top auto variant b_pregnant when ((b or _b) and pregnant) and not (topless or naked)
        group top auto variant c_pregnant when (c and pregnant) and not (topless or naked)
        group top auto variant d_pregnant when (d and pregnant) and not (topless or naked)

        group harness auto variant a when (a or _a) and not (pregnant or topless or naked)
        group harness auto variant b when (b or _b) and not (pregnant or topless or naked)
        group harness auto variant a_pregnant when ((a or _a) and pregnant) and not (topless or naked)
        group harness auto variant b_pregnant when ((b or _b) and pregnant) and not (topless or naked)


        group lefthand auto
        group sleeves_left auto variant c when c and not (naked or topless)
        group righthand auto variant c when c
        group sleeves_right auto variant nopeace when nopeace and c and not (naked or topless)
        group sleeves_right auto variant peace when peace and c and not (naked or topless)

        group hand auto variant d when d
        group sleeves_d auto variant notpressed when d and notpressed and not (naked or topless)
        group sleeves_d auto variant pressed when d and pressed and not (pregnant or naked or topless)
        group sleeves_d auto variant pressed_pregnant when d and pressed and pregnant and not (naked or topless)


        attribute collar variant d when d


        always "shiori_head_d" when d


        attribute blush when a or _a or b or _b


        group exp auto when a or _a or b or _b:
            attribute normal default
        group exp auto variant c when c:
            attribute normal default
        group exp auto variant d when d:
            attribute normal default


        group piercings variant d when d:
            attribute nose


        group hair auto variant d when d


        attribute lips null
        attribute tongue null
        group piercings_lips auto when lips and not d
        group piercings_tongue auto when tongue and not d
        group piercings_lips_d auto when lips and d
        group piercings_tongue_d auto when tongue and d


        attribute collar when a or _a or b or _b
        attribute collar variant c when c


        group necklace auto when not (collar or naked or topless or c or d)


        group multiple auto variant fx


        group hat auto when a or _a or b or _b


        group arm auto
        group arm auto variant a when a or _a
        group arm auto variant b when b or _b

    layeredimage shiori close:
        yalign 0.15
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=shiori)


        attribute idle null


        group tail auto


        group position auto:
            attribute _a "shiori_close_position_a"
            attribute _b "shiori_close_position_b"


        group hair auto variant a when a or _a
        group hair auto variant b when b or _b
        group hair auto variant c when c


        attribute pubes when not (a or _a)
        attribute pubes variant c when c
        attribute pubes variant d when d


        attribute pregnant null
        group pregnant auto when pregnant


        always "shiori_close_boobs_d" when d and not pressed


        attribute ears null
        group multiple auto variant piercings_a when a or _a
        group multiple auto variant piercings_b when b or _b
        group multiple auto variant piercings_c when c
        group multiple auto variant piercings_d when d


        attribute naked null

        group stockings auto variant a when (a or _a) and not (bottomless or naked)
        group stockings auto variant b when (b or _b) and not (bottomless or naked)
        group stockings auto variant c when c and not (bottomless or naked)
        group stockings auto variant d when d and not (bottomless or naked)

        attribute bottomless null
        group bot auto variant a when (a or _a) and not (pregnant or bottomless or naked)
        group bot auto variant b when (b or _b) and not (pregnant or bottomless or naked)
        group bot auto variant c when c and not (pregnant or bottomless or naked)
        group bot auto variant d when d and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when ((a or _a) and pregnant) and not (bottomless or naked)
        group bot auto variant b_pregnant when ((b or _b) and pregnant) and not (bottomless or naked)
        group bot auto variant c_pregnant when (c and pregnant) and not (bottomless or naked)
        group bot auto variant d_pregnant when (d and pregnant) and not (bottomless or naked)

        group necklace auto variant c when c and not (collar or naked or topless)
        group necklace auto variant d when d and not (collar or naked or topless)

        attribute topless null
        group top auto variant a when (a or _a) and not (pregnant or topless or naked)
        group top auto variant b when (b or _b) and not (pregnant or topless or naked)
        group top auto variant c when c and not (pregnant or topless or naked)
        group top auto variant d when d and not (pregnant or topless or naked)
        group top auto variant a_pregnant when ((a or _a) and pregnant) and not (topless or naked)
        group top auto variant b_pregnant when ((b or _b) and pregnant) and not (topless or naked)
        group top auto variant c_pregnant when (c and pregnant) and not (topless or naked)
        group top auto variant d_pregnant when (d and pregnant) and not (topless or naked)

        group harness auto variant a when (a or _a) and not (pregnant or topless or naked)
        group harness auto variant b when (b or _b) and not (pregnant or topless or naked)
        group harness auto variant a_pregnant when ((a or _a) and pregnant) and not (topless or naked)
        group harness auto variant b_pregnant when ((b or _b) and pregnant) and not (topless or naked)


        group lefthand auto
        group sleeves_left auto variant c when c and not (naked or topless)
        group righthand auto variant c when c
        group sleeves_right auto variant nopeace when nopeace and c and not (naked or topless)
        group sleeves_right auto variant peace when peace and c and not (naked or topless)

        group hand auto variant d when d
        group sleeves_d auto variant notpressed when d and notpressed and not (naked or topless)
        group sleeves_d auto variant pressed when d and pressed and not (pregnant or naked or topless)
        group sleeves_d auto variant pressed_pregnant when d and pressed and pregnant and not (naked or topless)


        attribute collar variant d when d


        always "shiori_close_head_d" when d


        attribute blush when a or _a or b or _b


        group exp auto when a or _a or b or _b:
            attribute normal default
        group exp auto variant c when c:
            attribute normal default
        group exp auto variant d when d:
            attribute normal default


        group piercings variant d when d:
            attribute nose


        group hair auto variant d when d


        attribute lips null
        attribute tongue null
        group piercings_lips auto when lips and not d
        group piercings_tongue auto when tongue and not d
        group piercings_lips_d auto when lips and d
        group piercings_tongue_d auto when tongue and d


        attribute collar when a or _a or b or _b
        attribute collar variant c when c


        group necklace auto when not (collar or naked or topless or c or d)


        group multiple auto variant fx


        group hat auto when a or _a or b or _b


        group arm auto
        group arm auto variant a when a or _a
        group arm auto variant b when b or _b

    layeredimage shiori smartphone:
        always "shiori_smartphone"

    layeredimage shiori kiss:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, CollarPicker], npc=shiori)

        group multiple:
            attribute nopeace null
            attribute peace null
            attribute notpressed null
            attribute pressed null


        always:
            "shiori_kiss"


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]


        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        group multiple auto variant piercings_naked when naked or topless
        group multiple auto variant piercings


        group outfitmike auto if_not ["naked"]:
            attribute normal default
            attribute mwedding


        attribute collar

        group necklace auto if_not ["collar"]

    layeredimage shiori spanking:
        always "shiori_spanking_bg"
        always "shiori_spanking_body"

        group exp auto:
            attribute normal default

        attribute blush "shiori_spanking_blush"

        group top auto:
            attribute top default

        group outfit auto:
            attribute bot default

        group red auto
        group fx auto
        group slap auto

        attribute leak "shiori_spanking_leak"

        attribute man:
            "shiori_spanking_man"
        attribute man:
            "shiori_spanking_man_eyes"

        attribute foot "shiori_spanking_foot"

    layeredimage shiori bj:
        group bg auto:
            attribute bedroom default

        group body auto:
            attribute base default

        attribute outfit
        group outfit auto if_any "outfit"

        group face auto if_not "suck"

        group exp auto variant "boobs" if_any "boobs"

        group exp auto variant "base" if_not "boobs":
            attribute smile default

        group multiple auto variant cum_mouth
        group multiple:
            if_not ["suck"]

        group dick auto:
            if_not ["suck","boobs"]
            attribute high default

        group multiple auto variant cum_base
        group multiple:
            if_not ["boobs", "suck"]
        group multiple auto variant cum_boobs
        group multiple:
            if_not ["suck"]
            if_any "boobs"

        always:
            if_any ["boobs"]
            if_not ["suck"]
            "shiori_bj_dick_boobs"

        always:
            if_all ["boobs", 'tits']
            if_not ["suck"]
            "shiori_bj_cum_boobs_tits_tip"

        always:
            if_not ["suck","boobs"]
            "shiori_bj_hand"

        always:
            if_all ["outfit"]
            if_not ["boobs"]
            "shiori_bj_outfit_hand"

        attribute cumshot:
            if_not "suck"

        group cumshot_suck auto:
            if_all ["cumshot", 'suck']

        attribute facial null
        group facial auto:
            if_any "facial"
            if_not "suck"

        always "shiori_bj_leg"
        always:
            if_any ["office"]
            "shiori_bj_office_fg"

        attribute speed:
            if_not "boobs"

    layeredimage shiori milk:
        attribute_function Pickers([PiercingsPicker, OutfitPicker], npc=shiori)


        always:
            "shiori_milk_bg"


        group shiori auto


        group multiple auto variant piercings


        always:
            "shiori_milk_desk"


        always:
            "shiori_milk_milk"


        always:
            "shiori_milk_light"

    layeredimage shiori sleep office:
        attribute_function Pickers([OutfitPicker, PiercingsPicker], npc=shiori)

        always "shiori_sleep_office_bg"

        group outfit auto:
            attribute work default

        group multiple auto variant piercings when (topless or naked)

    layeredimage shiori reverse:
        attribute_function Pickers([PiercingsPicker, XrayPicker, PregnancyPicker], npc=shiori)


        group bg auto:
            attribute bedroom default

        always "shiori_reverse_body"

        attribute pregnant

        group exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute lips null
            attribute tongue null

        group dick auto:
            attribute out default
            attribute nodick null

        attribute condom

        attribute wet

        attribute xray null
        group xray auto if_any "xray" if_not "cum"
        group xray_cum auto if_all ["xray", "cum"]

        group cum auto

        attribute milk

        attribute squirt

    layeredimage shiori doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker, ButtplugPicker], npc=shiori)
        group bg auto:
            attribute bedroom default

        always "shiori_doggy_body"

        group skin auto

        attribute nomike null
        always:
            if_not "nomike"
            "shiori_doggy_mike"

        group exp auto:
            attribute normal default

        attribute buttplug if_not ["anal", "gape"]

        attribute naked null
        group outfits auto if_not "naked"

        attribute gape

        group sexyswimsuit auto if_any "sexyswimsuit" if_not "naked":
            attribute nofuck default

        group fuck auto:
            if_not "nomike"
            attribute done default

        attribute condom null
        group condom auto if_any "condom" if_not ["nomike", "cumshot"]

        group condomcum auto if_all ["condom","cumshot"] if_not ["nomike"]

        attribute cumshot null
        group cumshot auto:
            if_any "cumshot"
            if_not ["nomike","condom", "gape"]

        always:
            if_all ["gape", "cumshot"]
            if_not ["condom"]
            "shiori_doggy_gape_cumshot"

        group multiple auto variant fx

        group fg auto

    layeredimage shiori lapdance:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, CollarPicker, MCCGPicker], npc=shiori)

        group bg auto:
            attribute stripclub default

        attribute mikemc null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mcoutfit auto:
            attribute mc_casual default

        attribute nonpc null
        always "shiori_lapdance_shiori" when not nonpc
        always "shiori_lapdance_outfits_stripper" when stripper and not (nonpc or naked or shiori_naked)

        group exp auto when not nonpc:
            attribute normal default

        group multiple auto variant piercings when not nonpc
        group multiple auto variant piercings_ahegao when ahegao and not nonpc
        group multiple auto variant piercings_normal when not (ahegao or nonpc)

        attribute shiori_naked null
        group outfits auto when not (nonpc or naked or shiori_naked or stripper)

        attribute collar when not nonpc

        group light auto

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage shiori fall:
        attribute_function Pickers([PubesPicker, OutfitPicker], npc=shiori)
        group bg auto:
            attribute office default

        group props auto

        always:
            "shiori_fall_body"

        group exp auto:
            attribute open default

        attribute plug

        attribute pubes

        attribute naked null
        attribute nopanties null
        group panties auto if_not ["nopanties", "naked"]

        group outfit auto if_not ["naked"]

        group fg auto

    layeredimage shiori stretch:
        attribute bg default
        attribute shiori default

        group exp auto:
            attribute yawn default

    layeredimage shiori missionary:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, XrayPicker], npc=shiori)
        attribute condom null

        always:
            "shiori_missionary_bg"

        group bgfx auto

        always:
            "shiori_missionary_body"

        always:
            if_any ["pregnant"]
            "shiori_missionary_pregnant"

        group exp auto:
            attribute normal default

        group multiple auto variant piercings

        always:
            if_any "collar"
            "shiori_missionary_collar"

        always:
            if_all ["xray", "vaginal"]
            "shiori_missionary_xray_vaginal"
        group multiple auto variant xray_condom when xray and condom
        group multiple auto variant xray_raw when xray and not condom

        group fx auto

    layeredimage shiori missionary2:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker, PubesPicker, OutfitPicker], npc=shiori)

        attribute notpressed null
        attribute peace null


        group bg auto:
            attribute office default


        always:
            "shiori_missionary2_shiori"


        attribute pubes


        attribute naked null
        group outfit_top auto if_not ["naked"]


        attribute pregnant


        group outfit_pregnant auto if_any ["pregnant"] if_not ["naked"]


        group boobs auto:
            attribute still default


        group multiple auto variant piercings_still when still
        group multiple auto variant piercings_bounce when bounce


        group outfit_bra_pregnant auto variant "still" if_all ["pregnant","still"] if_not ["nobra","naked"]


        attribute nobra null
        group outfit_bra auto variant "still" if_any "still" if_not ["nobra","naked"]
        group outfit_bra auto variant "bounce" if_any "bounce" if_not ["nobra","naked"]


        group outfit_bot auto if_not ["pregnant","naked"]
        group outfit_bot auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]


        attribute collar


        attribute blush


        group exp auto:
            attribute normal default


        attribute ears null
        attribute tongue null
        attribute lips null
        group multiple auto variant piercings


        group dick auto if_not "dwayne":
            attribute outside default


        group dwayne_dick auto if_not "mike":
            attribute outside default


        attribute condom null
        group condom auto if_any "condom" if_not ["anal","dwayne"]
        group dwayne_condom auto if_any "condom" if_not ["anal","mike"]


        attribute creampie null
        group creampie auto if_any "creampie" if_not ["condom","dwayne"]
        group dwayne_creampie auto if_any "creampie" if_not ["condom","mike"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["condom","dwayne"]
        group dwayne_cumshot auto if_any "cumshot" if_not ["condom","mike"]


        if hero.has_condom():
            "shiori_missionary2_condoms"


        group body auto:
            attribute mike default


        group outfit_mike auto if_not "dwayne"


        group outfit_dwayne auto if_not "mike"



        group multiple auto variant fx

    layeredimage shiori piledriver:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=shiori)


        always "shiori_piledriver_bg"


        attribute slap


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        always "shiori_piledriver_clit" if_all ["clit", "outside"] if_not ["dildo"]
        always "shiori_piledriver_clit" if_all ["clit", "inside"] if_not ["dildo", "vaginal"]



        attribute torn null
        group outfit auto if_not ["torn"]:
            attribute naked default null
        group outfit auto variant "torn" if_any ["torn"]

        attribute pregnant null
        group pregnant auto if_any ["pregnant"]
        attribute rope


        attribute plug null
        group plug auto if_any ["plug"]:
            attribute out default


        attribute squirt


        attribute blush
        group acc auto variant "head"
        group exp auto:
            attribute normal default


        attribute collar


        attribute bodycum null
        group bodycum auto if_any ["bodycum"]


        attribute dildo
        attribute dildovibes


        attribute big default null
        group inorout:
            attribute outside default null
            attribute inside null
        group outside auto variant "small" if_all ["outside", "small"] if_not ["nomike"]
        group outside auto variant "medium" if_all ["outside", "medium"] if_not ["nomike"]
        group outside auto variant "big" if_all ["outside", "big"] if_not ["nomike"]
        group inside auto if_any ["inside"] if_not ["nomike", "dildo"]
        group inside auto variant "dildo" if_all ["inside", "dildo"] if_not ["nomike"]


        attribute nomike null
        group mike auto if_not ["nomike"]:
            attribute vaginal default


        attribute cumshot null
        group cumshot auto variant "outside_small" if_all ["cumshot", "outside", "small"] if_not ["nomike"]
        group cumshot auto variant "outside_medium" if_all ["cumshot", "outside", "medium"] if_not ["nomike"]
        group cumshot auto variant "outside_big" if_all ["cumshot", "outside", "big"] if_not ["nomike", "condom"]
        group cumshot auto variant "inside" if_all ["cumshot", "inside"] if_not ["nomike"]


        attribute condom null
        group condom auto variant "outside_big" if_all ["condom", "outside", "big"] if_not ["nomike", "cumshot"]
        group condom auto variant "inside" if_all ["condom", "inside"] if_not ["nomike"]
        group condomcum auto variant "outside_big" if_all ["condom", "cumshot", "outside", "big"] if_not ["nomike"]


        always "shiori_piledriver_clit_usedvagina" if_all ["clit", "inside", "vaginal"]
        always "shiori_piledriver_clit_usedvagina" if_all ["clit", "dildo"]

    layeredimage shiori ending:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker, PregnancyPicker, EndingKidPicker], npc=shiori)
        attribute pregnant null

        always:
            "shiori_ending_bg"

        always:
            "shiori_ending_shiori"

        always:
            "shiori_ending_kanta"

        attribute kid null
        always "shiori_ending_tetsuo" when kid
        always "shiori_ending_mike" when not kid

        group multiple auto variant piercings
        group outfit auto

        always:
            if_any "collar"
            "shiori_ending_collar"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
