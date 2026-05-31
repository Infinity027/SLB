init 1:
    layeredimage shawn:
        attribute_function Pickers([OutfitPicker, CollarPicker], npc=shawn)

        zoom 1.05


        attribute naked null
        always "shawn_naked" if_not "halloween"
        group outfit auto


        group exp auto:
            attribute normal default if_not "halloween"


        group dick auto variant "medium":
            attribute floppy default if_any ["naked"]


        attribute blush


        attribute sick


        attribute glasses
        attribute noglasses null
        always "shawn_glasses" if_any ["date"] if_not "noglasses"


        attribute collar


        group arm auto


        attribute hat

    layeredimage shawn smartphone:
        always "shawn_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
