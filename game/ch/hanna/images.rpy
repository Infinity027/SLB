init 1:
    layeredimage hanna:
        attribute_function Pickers([PositionPicker,  CollarPicker, OutfitPicker, ArmpitsPicker, PubesPicker], npc=hanna)

        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute blush

        group exp auto:
            attribute normal default

        attribute armpits null
        group armpits auto if_any "armpits"

        attribute naked null

        attribute bottomless null

        attribute topless null

        attribute sweat null
        group sweat auto if_any ["sweat"]

        attribute collar

        group multiple auto variant acc
        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b

        group arm auto

        group hat auto

    layeredimage hanna close:
        yalign 0.05
        attribute_function Pickers([PositionPicker,  CollarPicker, OutfitPicker, ArmpitsPicker, PubesPicker], npc=hanna)

        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute blush

        group exp auto:
            attribute normal default

        attribute armpits null
        group armpits auto if_any "armpits"

        attribute naked null

        attribute bottomless null

        attribute topless null

        attribute sweat null
        group sweat auto if_any ["sweat"]

        attribute collar

        group multiple auto variant acc
        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b

        group arm auto

        group hat auto

    layeredimage hanna smartphone:
        always "hanna_smartphone"

    layeredimage hanna stand:
        attribute_function Pickers([ CollarPicker], npc=hanna)

        group bg auto:
            attribute house default

        always "hanna_stand_bodies"

        attribute collar

        attribute naked null
        always "hanna_stand_outfit_mike" if_not ["naked"]
        always "hanna_stand_outfit_hanna" if_not ["naked"]

        group fg auto

    layeredimage hanna lapdance:
        attribute_function Pickers([OutfitPicker, PubesPicker, CollarPicker,  MCCGPicker], npc=hanna)

        group bg auto:
            attribute stripclub default

        attribute mikemc null
        attribute naked null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mcoutfit auto when not naked:
            attribute mc_casual default

        attribute nonpc null
        always "hanna_lapdance_hanna" when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        group multiple:
            attribute nose null
            attribute tongue null

        attribute pubes when not nonpc
        attribute armpits when not nonpc

        attribute hanna_naked null
        group outfits auto when not (nonpc or naked or hanna_naked)

        attribute collar when not nonpc

        always "hanna_lapdance_fg"
        always "hanna_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage hanna gym ending:
        attribute_function Pickers([ CollarPicker, EndingKidPicker], npc=hanna)
        always:
            "hanna_gym_ending_bg"

        always:
            "hanna_gym_ending_mike"

        attribute kid

        always:
            "hanna_gym_ending_hanna"

        attribute collar

        always:
            "hanna_gym_ending_sexywork"

        always:
            "hanna_gym_ending_fg"

    layeredimage hanna house ending:
        attribute_function Pickers([ CollarPicker, EndingKidPicker], npc=hanna)
        always:
            "hanna_house_ending_bg"

        always:
            "hanna_house_ending_mike"

        always:
            "hanna_house_ending_hanna"

        attribute kid
        always:
            if_any "kid"
            "hanna_house_ending_casual"

        always:
            "hanna_house_ending_apron"

        attribute collar

        always:
            "hanna_house_ending_fg"
