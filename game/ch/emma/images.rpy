init 1:
    layeredimage emma:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, SeasonPicker, IndoorOutdoorPicker], npc=emma)


        attribute indoor null
        attribute outdoor null
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        group position auto

        group exp auto:
            attribute normal default


        attribute pubes

        attribute naked null

        group panties auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group top auto variant "a" if_any ["a"] if_not ["casual",  "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["casual", "topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not [ "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not [ "bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_all ["a", "casual"] if_not [ "topless", "naked"]
        group top auto variant "b" if_all ["b", "casual"] if_not [ "topless", "naked"]

        attribute collar if_all ["b"]


        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        attribute blazer null
        group blazer auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked", "halloween"]
        group blazer auto if_any ["blazer"] if_not ["topless", "naked"]


        attribute hat null
        group hat auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked"]
        group hat auto if_any ["hat", "wedding"] if_not ["topless", "naked"]


        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage emma close:
        yalign 0.04
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, SeasonPicker, IndoorOutdoorPicker], npc=emma)


        attribute indoor null
        attribute outdoor null
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null


        group position auto

        group exp auto:
            attribute normal default


        attribute pubes

        attribute naked null

        group panties auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]

        group top auto variant "a" if_any ["a"] if_not ["casual",  "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["casual",  "topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not [ "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not [ "bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_all ["a", "casual"] if_not [ "topless", "naked"]
        group top auto variant "b" if_all ["b", "casual"] if_not [ "topless", "naked"]

        attribute collar if_all ["b"]


        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        attribute blazer null
        group blazer auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked", "halloween"]
        group blazer auto if_any ["blazer"] if_not ["topless", "naked"]


        attribute hat null
        group hat auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["topless", "naked"]
        group hat auto if_any ["hat", "wedding"] if_not ["topless", "naked"]


        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage emma smartphone:
        always "emma_smartphone"

    layeredimage emma kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker], npc=emma)

        always "emma_kiss"

        attribute collar

        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]

        group hat auto if_not ["naked"]

        group outfitmike auto if_not ["naked"]:
            attribute normal default

    layeredimage emma ending:
        attribute_function Pickers([EndingKidPicker], npc=emma)

        always "emma_ending_bg"

        always "emma_ending_bodies"

        always "emma_ending_grass_bg"

        attribute kid

        always "emma_ending_grass_fg"

        always "emma_ending_light"
