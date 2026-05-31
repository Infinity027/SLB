init 1:
    layeredimage ryan:
        attribute_function Pickers([OutfitPicker], npc=ryan)

        attribute naked null

        always "ryan_body" if_not ["tux", "casual"]


        attribute blush


        group exp auto:
            attribute normal default

        group outfit auto if_not ["naked"]

        group arm auto

    layeredimage ryan close:
        yalign 0.0
        attribute_function Pickers([OutfitPicker], npc=ryan)

        attribute naked null

        always "ryan_close_body" if_not ["tux", "casual"]


        attribute blush

        group outfit auto if_not ["naked"]

        group arm auto

    layeredimage ryan fight:
        group punch auto:
            attribute punchryan default

    layeredimage ryan bus:
        always "ryan_bus_bg"
        always "ryan_bus_nohit" if_not ["hit"]
        attribute bodies
        attribute hit

    layeredimage ryan smartphone:
        always "ryan_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
