init 1:
    layeredimage jack:
        attribute_function Pickers([OutfitPicker], npc=jack)
        attribute naked null
        always "jack_body" if_not "casual"

        always "jack_dick" if_any ["naked"]

        group outfit auto if_not "naked"

        group exp auto:
            attribute normal default null

        attribute nosebleed
        attribute blush

        group acc_head auto if_not "naked"

        group arm auto

    layeredimage jack close:
        attribute_function Pickers([OutfitPicker], npc=jack)
        yalign 0.0
        attribute naked null
        always "jack_close_body" if_not "casual"

        attribute dick if_any ["naked"]

        group outfit auto if_not "naked"

        group exp auto:
            attribute normal default null

        attribute nosebleed
        attribute blush

        group acc_head auto if_not "naked"

        group arm auto

    layeredimage jack smartphone:
        always "jack_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
