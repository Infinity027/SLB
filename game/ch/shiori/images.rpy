init 1:
    layeredimage shiori:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=shiori)

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

        always "shiori_boobs_d" when d and not pressed

        attribute ears null
        attribute naked null

        group stockings auto variant a when (a or _a) and not (bottomless or naked)
        group stockings auto variant b when (b or _b) and not (bottomless or naked)
        group stockings auto variant c when c and not (bottomless or naked)
        group stockings auto variant d when d and not (bottomless or naked)

        attribute bottomless null

        group necklace auto variant c when c and not (collar or naked or topless)
        group necklace auto variant d when d and not (collar or naked or topless)

        attribute topless null

        group lefthand auto
        group sleeves_left auto variant c when c and not (naked or topless)
        group righthand auto variant c when c
        group sleeves_right auto variant nopeace when nopeace and c and not (naked or topless)
        group sleeves_right auto variant peace when peace and c and not (naked or topless)

        group hand auto variant d when d
        group sleeves_d auto variant notpressed when d and notpressed and not (naked or topless)
        group sleeves_d auto variant pressed when d and pressed and not (naked or topless)

        attribute collar variant d when d

        always "shiori_head_d" when d

        attribute blush when a or _a or b or _b

        group exp auto when a or _a or b or _b:
            attribute normal default
        group exp auto variant c when c:
            attribute normal default
        group exp auto variant d when d:
            attribute normal default

        group hair auto variant d when d

        attribute lips null
        attribute tongue null

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
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=shiori)

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

        always "shiori_close_boobs_d" when d and not pressed

        attribute ears null

        attribute naked null

        group stockings auto variant a when (a or _a) and not (bottomless or naked)
        group stockings auto variant b when (b or _b) and not (bottomless or naked)
        group stockings auto variant c when c and not (bottomless or naked)
        group stockings auto variant d when d and not (bottomless or naked)

        attribute bottomless null

        group necklace auto variant c when c and not (collar or naked or topless)
        group necklace auto variant d when d and not (collar or naked or topless)

        attribute topless null

        group lefthand auto
        group sleeves_left auto variant c when c and not (naked or topless)
        group righthand auto variant c when c
        group sleeves_right auto variant nopeace when nopeace and c and not (naked or topless)
        group sleeves_right auto variant peace when peace and c and not (naked or topless)

        group hand auto variant d when d
        group sleeves_d auto variant notpressed when d and notpressed and not (naked or topless)
        group sleeves_d auto variant pressed when d and pressed and not (naked or topless)

        attribute collar variant d when d

        always "shiori_close_head_d" when d

        attribute blush when a or _a or b or _b

        group exp auto when a or _a or b or _b:
            attribute normal default
        group exp auto variant c when c:
            attribute normal default
        group exp auto variant d when d:
            attribute normal default

        group hair auto variant d when d

        attribute lips null
        attribute tongue null

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

    layeredimage shiori milk:
        attribute_function Pickers([ OutfitPicker], npc=shiori)

        always:
            "shiori_milk_bg"

        group shiori auto

        always:
            "shiori_milk_desk"

        always:
            "shiori_milk_milk"

        always:
            "shiori_milk_light"

    layeredimage shiori sleep office:
        attribute_function Pickers([OutfitPicker], npc=shiori)

        always "shiori_sleep_office_bg"

        group outfit auto:
            attribute work default

    layeredimage shiori lapdance:
        attribute_function Pickers([OutfitPicker,  CollarPicker, MCCGPicker], npc=shiori)

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

    layeredimage shiori ending:
        attribute_function Pickers([ CollarPicker, OutfitPicker, EndingKidPicker], npc=shiori)
        always:
            "shiori_ending_bg"

        always:
            "shiori_ending_shiori"

        always:
            "shiori_ending_kanta"

        attribute kid null
        always "shiori_ending_tetsuo" when kid
        always "shiori_ending_mike" when not kid

        group outfit auto

        always:
            if_any "collar"
            "shiori_ending_collar"
