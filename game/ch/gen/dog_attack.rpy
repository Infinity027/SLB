init 1:
    layeredimage dog attack:
        attribute_function Pickers([MCCGPicker])

        always "dog_attack_bg" if_any ["breemc"]
        attribute breemc

        attribute mc_nohaircut null
        attribute mc_haircut

        group mc_outfits auto if_any ["breemc"]

        attribute mc_collar

        group multiple auto variant mc_piercings

        attribute mikemc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
