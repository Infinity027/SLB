init 1:
    layeredimage lexi:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=lexi)

        attribute idle null

        attribute nophone null
        always "lexi_phone_a" if_any ["a"] if_not ["nophone"]

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute blush null
        group blush auto if_any "blush"

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        attribute tongue null

        attribute naked null

        attribute topless null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless","naked"]

        attribute bottomless null

        always "lexi_phone_b" if_any ["b"] if_not ["nophone"]

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]

        attribute lolly null
        group lolly auto if_any ["lolly"] if_not ["lollipop"]:
            attribute inside default

        attribute collar null
        group collar auto if_any ["collar"]

        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "c" if_any ["c"]

        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "c" if_any ["c"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage lexi close:
        yalign 0.2
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=lexi)

        attribute idle null

        attribute nophone null
        always "lexi_close_phone_a" if_any ["a"] if_not ["nophone"]

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute blush null
        group blush auto if_any "blush"

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        attribute tongue null

        attribute naked null

        attribute topless null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless","naked"]

        attribute bottomless null

        always "lexi_close_phone_b" if_any ["b"] if_not ["nophone"]

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]

        attribute lolly null
        group lolly auto if_any ["lolly"] if_not ["lollipop"]:
            attribute inside default

        attribute collar null
        group collar auto if_any ["collar"]

        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "c" if_any ["c"]

        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "c" if_any ["c"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage lexi smartphone:
        always "lexi_smartphone"

    layeredimage lexi lapdance:
        attribute_function Pickers([OutfitPicker, CollarPicker,  MCCGPicker], npc=lexi)

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
        always "lexi_lapdance_lexi" when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        attribute collar when not nonpc

        attribute lexi_naked null
        group outfits auto when not (nonpc or naked or lexi_naked)

        always "lexi_lapdance_fg"
        always "lexi_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage lexi ending:
        always "lexi_ending_bg"

        group multiple auto variant kids

        always "lexi_ending_fg"

    layeredimage lexi ending2:
        always "lexi_ending2_bg"

        group outfit auto

        always "lexi_ending2_fg"

