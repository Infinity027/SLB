init 1:
    layeredimage alexis:
        attribute_function Pickers([PositionPicker,   CollarPicker, PubesPicker, OutfitPicker], npc=alexis)

        attribute idle null

        group acc_back auto

        group position auto

        attribute pubes

        attribute blush

        group exp auto:
            attribute normal default

        attribute naked null

        attribute bottomless null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute nopatsies null
        group patsies auto variant "a" if_any ["a"] if_not ["nopatsies", "topless", "naked"]
        group patsies auto variant "b" if_any ["b"] if_not ["nopatsies", "topless", "naked"]

        attribute topless null

        group acc_head auto

        attribute collar

        group necklace auto if_not "collar"

        group fx auto

        group arm auto

    layeredimage alexis close:
        yalign 0.05
        attribute_function Pickers([PositionPicker, CollarPicker, PubesPicker, OutfitPicker], npc=alexis)

        attribute idle null

        group acc_back auto

        group position auto

        attribute pubes

        attribute blush

        group exp auto:
            attribute normal default

        attribute naked null

        attribute bottomless null
        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute nopatsies null
        group patsies auto variant "a" if_any ["a"] if_not ["nopatsies", "topless", "naked"]
        group patsies auto variant "b" if_any ["b"] if_not ["nopatsies", "topless", "naked"]

        attribute topless null

        group acc_head auto

        attribute collar

        group necklace auto if_not "collar"

        group fx auto

        group arm auto

    layeredimage alexis smartphone:
        always "alexis_smartphone"

    layeredimage alexis ending:
        always "alexis_ending_bg"
        always "alexis_ending_dog"

        always "alexis_ending_alexis"
