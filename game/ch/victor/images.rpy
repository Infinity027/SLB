init 1:
    layeredimage victor:
        attribute_function Pickers([OutfitPicker], npc=victor)
        attribute naked null

        always:
            "victor_body"
        always if_any "naked":
            "victor_dick"

        group outfit auto if_not "naked"

        group exp auto:
            attribute normal null default

        attribute blush

        group hat auto

        group tie auto if_not ["naked", "swimsuit", "sport"]:
            attribute down default

        attribute gun
        attribute wounded

        group arm auto


    layeredimage victor close:
        yalign 0.05
        attribute_function Pickers([OutfitPicker], npc=victor)
        attribute naked null

        always:
            "victor_close_body"
        always if_any "naked":
            "victor_close_dick"

        group outfit auto if_not "naked":
            attribute casual default

        group exp auto:
            attribute normal null default

        attribute blush

        group hat auto

        group tie auto if_not ["naked", "swimsuit"]:
            attribute down default

        attribute gun
        attribute wounded

        group arm auto

    layeredimage victor smartphone:
        always "victor_smartphone"

    layeredimage victor firefight:
        attribute po null
        always:
            "victor_firefight_base"
        attribute fire
        group po auto if_any["po"]:
            attribute base default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
