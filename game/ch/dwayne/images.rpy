init 1:
    layeredimage dwayne:
        attribute_function Pickers([OutfitPicker], npc=dwayne)
        attribute naked null
        always:
            if_not ["swimsuit", "casual", "work"]
            "dwayne_body"
        group outfit auto if_not ["naked"]
        group dicks auto


        attribute blush

        group exp auto:
            attribute normal default
        group hat auto
        group arm auto

    layeredimage dwayne close:
        yalign 0.0
        attribute naked null
        always:
            if_not ["swimsuit", "casual", "work"]
            "dwayne_close_body"
        group dicks auto
        group outfit auto if_not ["naked"]:
            attribute casual default
            attribute work


        attribute blush

        group exp auto:
            attribute normal default
        group hat auto
        group arm auto

    layeredimage dwayne smartphone:
        always "dwayne_smartphone"

    layeredimage dwayne fight:
        group pos auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
