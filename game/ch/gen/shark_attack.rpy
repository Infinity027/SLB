init 1:
    layeredimage shark attack:
        attribute_function Pickers([MCCGPicker])

        always "shark_attack_bg"
        always "shark_attack_shark"
        always "shark_attack_water"

        attribute mikemc

        attribute breemc
        attribute mc_nohaircut null if_any "breemc"
        attribute mc_haircut if_any "breemc"

        group outfits auto if_any "breemc"
        group multiple auto variant piercings when breemc

        always "shark_attack_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
