init 1:
    layeredimage mike:
        attribute_function Pickers([PositionPicker, OutfitPicker, PubesPicker, PiercingsPicker, DickPicker, CollarPicker], npc=mike)

        attribute naked null

        group phone:
            attribute dial null default
            attribute speak null


        always "mike_body"

        group position auto:
            attribute a null default
            attribute b null
            attribute p null


        group multiple auto variant piercings

        attribute pubes

        group dick_position auto:
            attribute limp null default
            attribute hard null

        group dicks auto variant "limp" if_all ["limp", "naked"]
        group dicks auto variant "hard" if_all ["hard", "naked"]

        attribute condom null
        group condom auto if_all ["condom", "hard"]

        group boobs auto


        group bot auto if_not "naked"

        group top auto if_not "naked"

        attribute collar

        group handpos auto if_any ["casual", "sport", "swimsuit", "underwear", "towel", "crossdress", "naked"]
        group handpos auto variant "p" if_all "p" if_any ["casual", "sport","swimsuit", "underwear", "towel", "crossdress", "naked"]


        group fx auto


        group exp auto:
            attribute normal default

        group hairs auto:
            attribute nohaircut default

        group beard auto if_not "naked"

        attribute makeup null
        group makeup auto if_any "makeup"

        group hat auto if_not "naked"

        group arms_outfits auto variant "a" if_all ["a"] if_not "naked"
        group arms_outfits auto variant "b" if_all ["b"] if_not "naked"
        group arms_outfits auto variant "p_speak" if_all ["p", "speak"] if_not "naked"
        group arms_outfits auto variant "p_dial" if_all ["p", "dial"] if_not "naked"

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "p" if_any ["p"]

    layeredimage mike close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, OutfitPicker, PubesPicker, PiercingsPicker, DickPicker, CollarPicker], npc=mike)

        attribute naked null

        group phone:
            attribute dial null default
            attribute speak null


        always "mike_close_body"

        group position auto:
            attribute a null default
            attribute b null
            attribute p null


        group multiple auto variant piercings

        attribute pubes

        group dick_position auto:
            attribute limp null default
            attribute hard null

        group dicks auto variant "limp" if_all ["limp", "naked"]
        group dicks auto variant "hard" if_all ["hard", "naked"]

        attribute condom null
        group condom auto if_all ["condom", "hard"]

        group boobs auto


        group bot auto if_not "naked"

        group top auto if_not "naked"

        attribute collar

        group handpos auto if_any ["casual", "sport", "swimsuit", "underwear", "towel", "crossdress", "naked"]
        group handpos auto variant "p" if_all "p" if_any ["casual", "sport","swimsuit", "underwear", "towel", "crossdress", "naked"]


        group fx auto


        group exp auto:
            attribute normal default

        group hairs auto:
            attribute nohaircut default

        group beard auto if_not "naked"

        attribute makeup null
        group makeup auto if_any "makeup"

        group hat auto if_not "naked"

        group arms_outfits auto variant "a" if_all ["a"] if_not "naked"
        group arms_outfits auto variant "b" if_all ["b"] if_not "naked"
        group arms_outfits auto variant "p_speak" if_all ["p", "speak"] if_not "naked"
        group arms_outfits auto variant "p_dial" if_all ["p", "dial"] if_not "naked"

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "p" if_any ["p"]

    layeredimage mike smartphone:
        always "mike_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
