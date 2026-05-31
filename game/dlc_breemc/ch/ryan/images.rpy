init 1:
    layeredimage ryan kiss:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=ryan)

        attribute breemc null


        always "ryan_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "ryan_kiss_bodies_bowsette"

        attribute naked null
        attribute topless null


        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute chinese "ryan_kiss_outfits_casual"
            attribute bowsette "ryan_kiss_outfits_halloween"
            attribute invisible "ryan_kiss_outfits_halloween"


        group mcoutfits auto if_not ["naked", "topless"]

        group haircuts auto if_not ["bowsette"]:
            attribute mc_nohaircut null

        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_nose null
            attribute mc_tongue null

    layeredimage ryan cowgirl:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=ryan)



        attribute bedroom3 null

        group bg auto:
            attribute mcbedroom default


        always:
            "ryan_cowgirl_bodies"


        attribute cumshot null
        attribute bodycum null


        group exp auto:
            attribute normal default


        attribute mc_collar


        attribute haircut


        attribute mc_pregnant


        attribute pubes


        group multiple auto variant mcoutfits:
            attribute bottom
            attribute pregnant_bottom
            attribute bra
            attribute hat
            attribute top


        group multiple auto variant piercings


        attribute nakedryan null
        always:
            if_not "nakedryan"
            "ryan_cowgirl_ryanoutfit_halloween"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
