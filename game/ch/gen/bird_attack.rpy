init 1:
    layeredimage bird attack:
        attribute_function Pickers([MCCGPicker])

        always "bird_attack_bg" if_any ["breemc"]
        attribute breemc

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute mc_collar

        group mc_outfits auto if_any ["breemc"]

        attribute mikemc