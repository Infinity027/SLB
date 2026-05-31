init 1:
    layeredimage bird attack:
        attribute_function Pickers([MCCGPicker])

        always "bird_attack_bg" if_any ["breemc"]
        attribute breemc

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute mc_collar

        group multiple auto variant mc_piercings

        group mc_outfits auto if_any ["breemc"]

        attribute mikemc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
