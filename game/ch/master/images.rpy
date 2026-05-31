init 1:
    layeredimage master:
        attribute_function Pickers([OutfitPicker], npc=master)
        attribute naked null

        always "master_body"

        always:
            if_any "naked"
            "master_dick"

        group outfit auto if_not ["naked"]

        attribute topless null
        attribute bottomless null
        group top auto when not (topless or naked)
        group bot auto when not (bottomless or naked)

        group exp auto:
            attribute normal null default


        attribute blush


        attribute glasses
        attribute noglasses null
        always:
            if_not "noglasses"
            "master_glasses"

        group arm auto

    layeredimage master close:
        yalign 0.2
        attribute naked null

        always "master_close_body"

        always:
            if_any "naked"
            "master_close_dick"

        group outfit auto if_not ["naked"]

        group exp auto:
            attribute normal null default



        attribute blush

        attribute noglasses null
        always:
            if_not "noglasses"
            "master_close_glasses"

        group arm auto

    layeredimage master smartphone:
        always "master_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
