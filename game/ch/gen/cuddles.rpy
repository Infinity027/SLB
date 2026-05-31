init 1:
    layeredimage cuddle:
        attribute_function MultiPickers([RoomPicker, SeasonPicker, HaircutPicker, CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker, MCCGPicker], append_npc_from_attributes=True, add_simple_pregnant_attribute=True)

        attribute mikemc null
        attribute breemc null

        group mc_dick:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        attribute mc_pregnant null

        attribute mc_haircut null
        attribute mc_nohaircut null

        attribute mc_pubes null

        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_nipples null
            attribute mc_nose null
            attribute mc_tongue null

        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        group bg auto:
            attribute bedroom1 default

        group mikemc_below auto when mikemc
        group breemc_below auto when breemc

        group mchaircuts_below auto variant haircut when breemc and mc_haircut
        group mchaircuts_below auto variant nohaircut when breemc and mc_nohaircut

        group dicks_below auto variant small when mc_small
        group dicks_below auto variant medium when mc_medium
        group dicks_below auto variant big when mc_big

        group mcpregnant_below auto when breemc and mc_pregnant

        group npc auto variant mikemc when mikemc
        group npc auto variant breemc when breemc

        group npc_dicks auto

        group breemc auto when breemc
        group mcpregnant auto when breemc and mc_pregnant
        group mchaircuts auto variant haircut when breemc and mc_haircut
        group mchaircuts auto variant nohaircut when breemc and mc_nohaircut

        group dicks auto variant small when mc_small
        group dicks auto variant medium when mc_medium
        group dicks auto variant big when mc_big

        attribute sasha_noboobjob null
        attribute sasha_boobjob

        group pregnancies auto

        group haircuts auto

        group makeup auto if_any ["makeup"]

        group multiple auto variant piercings
        group piercings auto variant boobjob when sasha_boobjob
        group piercings auto variant noboobjob when sasha_noboobjob

        group collars auto

        attribute dressed null

        group outfits auto when (dressed or not summer) and not pregnant
        group pregnant_outfits auto when (dressed or not summer) and pregnant

        group mikemc_above auto when mikemc
        group breemc_above auto when breemc

        group mcpregnant_above auto when breemc and mc_pregnant

        group mchaircuts_above auto variant haircut when breemc and mc_haircut
        group mchaircuts_above auto variant nohaircut when breemc and mc_nohaircut

        group mcpiercings auto variant mc_clit when breemc and mc_clit
        group mcpiercings auto variant mc_ears when breemc and mc_ears
        group mcpiercings auto variant mc_navel when breemc and mc_navel
        group mcpiercings auto variant mc_pregnant_navel when breemc and mc_pregnant_navel
        group mcpiercings auto variant mc_nipples when breemc and mc_nipples
        group mcpiercings auto variant mc_nose when breemc and mc_nose
        group mcpiercings auto variant mc_tongue when breemc and mc_tongue

        attribute mc_collar null
        group mccollar auto when breemc and mc_collar

        group mikemc_hands auto when mikemc
        group breemc_hands auto when breemc

        group blanket auto variant mikemc when mikemc and (fall or winter or morgan)
        group blanket auto variant breemc when breemc and (fall or winter)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
