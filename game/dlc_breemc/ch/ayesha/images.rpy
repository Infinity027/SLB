init 1:
    layeredimage ayesha beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[ayesha], append_npc_from_attributes=True)

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
        group foe_dick auto if_any "naked"
        group foe_outfit auto if_not ["naked"]


        always "ayesha_beats_ayesha"
        group multiple auto variant piercings
        group outfit auto if_not ["naked"]

        always "ayesha_beats_fx_motion"
        attribute blood null
        group fx variant "blood" if_any "blood"

    layeredimage ayesha fingering:
        attribute_function Pickers([MCCGPicker, OutfitPicker, PiercingsPicker], npc=ayesha)

        attribute breemc null
        attribute naked null
        attribute mc_naked null

        always "ayesha_fingering_bg"
        always "ayesha_fingering_bodies"
        group mchaircuts auto:
            attribute mc_nohaircut null

        group exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple auto variant mcpiercings
        attribute mc_ears null

        attribute tattoo null
        always "ayesha_fingering_halloween_tattoo" if_any ["halloween", "tattoo"]

        group outfit auto when not naked
        attribute mc_casual null

        group mcoutfit auto when not (naked or mc_naked)

        attribute squirt

        always "ayesha_fingering_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
