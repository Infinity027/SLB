init 1:
    layeredimage anna:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=anna)

        attribute leash if_all ["collar","a"]:
            "anna_leash_a"

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute sticks

        always:
            if_any ["a"]
            "anna_tattoo_a_heart"

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute ears null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute bottomless null

        attribute topless null

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]

        group makeup auto variant "a" if_any ["a"]
        group makeup auto variant "b" if_any ["b"]

        group wig auto variant "a" if_any ["a"]
        group wig auto variant "b" if_any ["b"]

        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]

        group cum auto if_any ["ahegao"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute leash if_all ["collar","b"]:
            "anna_leash_b"

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage anna close:
        yalign 0.08
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=anna)

        attribute leash if_all ["collar","a"]:
            "anna_close_leash_a"

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute sticks
   
        always:
            if_any ["a"]
            "anna_close_tattoo_a_heart"

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute ears null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute bottomless null

        attribute topless null

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]

        group makeup auto variant "a" if_any ["a"]
        group makeup auto variant "b" if_any ["b"]

        group wig auto variant "a" if_any ["a"]
        group wig auto variant "b" if_any ["b"]

        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]

        group cum auto if_any ["ahegao"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute leash if_all ["collar","b"]:
            "anna_close_leash_b"

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage anna smartphone:
        always "anna_smartphone"

    layeredimage anna ending:
        attribute_function Pickers([CollarPicker, EndingKidPicker], npc=anna)


        always "ending_anna_bg"


        always "ending_anna_family"


        attribute kid


        attribute collar

    layeredimage anna standing:
        attribute_function Pickers([CollarPicker], npc=anna)

        group bg auto:
            attribute bedroom default

        always:
            "anna_standing_bodies"

        group mikehand auto:
            attribute back default
            attribute pull null

        attribute collar

        group hair auto

        attribute blush

        attribute annahand

        group eyes auto:
            attribute normal default
        group mouth auto

        group chest auto:
            attribute still default

        group multiple auto variant fx

        group fg auto
