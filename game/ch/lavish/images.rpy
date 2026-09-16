init 1:
    layeredimage lavish:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=lavish)

        group tail auto if_not ["bottomless", "naked"]

        group position auto

        attribute pubes

        attribute blush

        group exp auto:
            attribute normal default

        attribute lips null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        attribute bottomless null

        attribute topless null

        group bracelet auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group bracelet auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        attribute collar null
        group collar auto if_any ["collar"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]

        group hat auto if_not ["topless", "naked"]
        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage lavish close:
        yalign 0.1
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=lavish)

        group tail auto if_not ["bottomless", "naked"]

        group position auto

        attribute pubes

        attribute blush

        group exp auto:
            attribute normal default

        attribute lips null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        attribute bottomless null

        attribute topless null

        group bracelet auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group bracelet auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute collar null
        group collar auto if_any ["collar"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]

        group hat auto if_not ["topless", "naked"]
        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage lavish smartphone:
        always "lavish_smartphone"

    layeredimage lavish files:
        always "lavish_files"

    layeredimage lavish ending:
        attribute_function Pickers([EndingKidPicker], npc=lavish)

        always "lavish_ending_bg"

        always "lavish_ending_bodies"

        attribute kid

        always "lavish_ending_light"
