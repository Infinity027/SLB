init 1:
    layeredimage kat:
        yoffset 15
        attribute_function Pickers([PositionPicker, PubesPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker], npc=kat)


        attribute idle null


        always "kat_body"
        group shoulders auto
        attribute pubes
        attribute pregnant
        attribute collar
        group necklace auto if_not ["collar"]


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings


        attribute blush
        group exp auto:
            attribute normal default


        attribute haircut


        attribute bottomless null
        attribute topless null
        attribute naked null
        group stockings auto when not (bottomless or naked)
        group bot auto if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["bottomless", "naked"]
        group top auto if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["topless", "naked"]
        group poke_piercings auto when nipples and not (topless or naked)


        attribute noacc null
        group acc_body auto if_not ["noacc", "topless", "naked"]
        group acc_head auto if_not ["noacc", "naked"]
        attribute headphones null
        group headphones auto if_any ["headphones"] if_not ["naked", "wedding"]


        group position:
            attribute a default
            attribute b
        group topper auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group topper auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group arm_topper auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc_hand auto variant "a" if_any ["a"] if_not ["noacc"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["noacc"]
        group sleeve auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeve auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group topper auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group topper auto variant "d" if_any ["d"] if_not ["topless", "naked"]
        group position:
            attribute c
            attribute d
        group acc_hand auto variant "c" if_any ["c"] if_not ["noacc"]
        group acc_hand auto variant "d" if_any ["d"] if_not ["noacc"]
        group sleeve auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group sleeve auto variant "d" if_any ["d"] if_not ["topless", "naked"]


        always "kat_lockofhair_haircut" if_all ["haircut", "b"]


        group arm auto

    layeredimage kat close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PubesPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker], npc=kat)


        attribute idle null


        always "kat_close_body"
        group shoulders auto
        attribute pubes
        attribute pregnant
        attribute collar
        group necklace auto if_not ["collar"]


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings


        attribute blush
        group exp auto:
            attribute normal default


        attribute haircut


        attribute bottomless null
        attribute topless null
        attribute naked null
        group stockings auto when not (bottomless or naked)
        group bot auto if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["bottomless", "naked"]
        group top auto if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["topless", "naked"]
        group poke_piercings auto when nipples and not (topless or naked)


        attribute noacc null
        group acc_body auto if_not ["noacc", "topless", "naked"]
        group acc_head auto if_not ["noacc", "naked"]
        attribute headphones null
        group headphones auto if_any ["headphones"] if_not ["naked"]


        group position:
            attribute a default
            attribute b
        group topper auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group topper auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group arm_topper auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group acc_hand auto variant "a" if_any ["a"] if_not ["noacc"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["noacc"]
        group sleeve auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeve auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group topper auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group topper auto variant "d" if_any ["d"] if_not ["topless", "naked"]
        group position:
            attribute c
            attribute d
        group acc_hand auto variant "c" if_any ["c"] if_not ["noacc"]
        group acc_hand auto variant "d" if_any ["d"] if_not ["noacc"]
        group sleeve auto variant "c" if_any ["c"] if_not ["topless", "naked"]
        group sleeve auto variant "d" if_any ["d"] if_not ["topless", "naked"]


        always "kat_close_lockofhair_haircut" if_all ["haircut", "b"]


        group arm auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
