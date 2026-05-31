init 1:
    layeredimage kiara:
        attribute_function Pickers([PositionPicker, CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, HaircutPicker, OutfitPicker], npc=kiara)


        attribute idle null


        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute cap null


        group body_position auto


        attribute collar null
        group collar auto when collar


        group multiple auto variant piercings_a_hidden when a
        group multiple auto variant piercings_b_hidden when b
        group multiple auto variant piercings_c_hidden when c
        group multiple auto variant piercings_d_hidden when d


        attribute pubes null
        group pubes auto when pubes


        attribute pregnant null
        group pregnant auto when pregnant


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c
        group multiple auto variant piercings_d when d


        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when a and pregnant and not (bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant b_pregnant when b and pregnant and not (bottomless or naked)
        group bot auto variant c when c and not (pregnant or bottomless or naked)
        group bot auto variant c_pregnant when c and pregnant and not (bottomless or naked)
        group bot auto variant d when d and not (pregnant or bottomless or naked)
        group bot auto variant d_pregnant when d and pregnant and not (bottomless or naked)

        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant a_pregnant when a and pregnant and not (topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant b_pregnant when b and pregnant and not (topless or naked)
        group top auto variant c when c and not (pregnant or topless or naked)
        group top auto variant c_pregnant when c and pregnant and not (topless or naked)
        group top auto variant d when d and not (pregnant or topless or naked)
        group top auto variant d_pregnant when d and pregnant and not (topless or naked)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar
        group necklace auto variant c when c and not collar
        group necklace auto variant d when d and not collar


        group arms auto variant low
        group arms auto:
            attribute d null


        group acc_arm auto variant low_d when d and not (topless or naked)
        group acc_arm auto variant a when a and not (topless or naked)
        group acc_arm auto variant b when b and not (topless or naked)
        group acc_arm auto variant c when c and not (topless or naked) and not (pregnant and sluttydate)
        group acc_arm auto variant c_pregnant when c and pregnant and sluttydate and not (topless or naked)


        group acc_up auto variant a when a and not (topless or naked)
        group acc_up auto variant b when b and not (topless or naked)
        group acc_up auto variant c when c and not (topless or naked)
        group acc_up auto variant d when d and not (topless or naked)

        group head auto


        attribute blush
        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b
        group exp auto variant c when c

        group eyes auto  when d:
            attribute eyes_normal default
        always "kiara_mouth_smoking" when d
        attribute tears

        group poke auto variant a when a and not (topless or naked)
        group poke auto variant b when b and not (topless or naked)
        group poke auto variant c when c and not (topless or naked)
        group poke auto variant d when d and not (topless or naked)

        group poke_piercing auto variant a when a and nipples and not (topless or naked)
        group poke_piercing auto variant b when b and nipples and not (topless or naked)
        group poke_piercing auto variant c when c and nipples and not (topless or naked)
        group poke_piercing auto variant d when d and nipples and not (topless or naked)


        group haircuts auto variant a when a and (not cap or (topless or naked))
        group haircuts auto variant b when b and (not cap or (topless or naked))
        group haircuts auto variant c when c and (not cap or (topless or naked))
        group haircuts auto variant d when d and (not cap or (topless or naked))


        group hat auto variant a when a and not (cap or topless or naked)
        group hat auto variant b when b and not (cap or topless or naked)
        group hat auto variant c when c and not (cap or topless or naked)
        group hat auto variant d when d and not (cap or topless or naked)


        group cap auto when cap and not (topless or naked)


        group glasses auto variant a when a and not (topless or naked)
        group glasses auto variant b when b and not (topless or naked)
        group glasses auto variant c when c and not (topless or naked)
        group glasses auto variant d when d and not (topless or naked)


        group arms auto variant up


        group acc_arm auto variant up_d when d and not (topless or naked)


        group multiple auto variant piercings_a_front when a
        group multiple auto variant piercings_b_front when b
        group multiple auto variant piercings_c_front when c
        group multiple auto variant piercings_d_front when d


        group arm auto when not c
        group arm auto variant c when c

    layeredimage kiara close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, HaircutPicker, OutfitPicker], npc=kiara)


        attribute idle null


        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute cap null


        group body_position auto


        attribute collar null
        group collar auto when collar


        group multiple auto variant piercings_a_hidden when a
        group multiple auto variant piercings_b_hidden when b
        group multiple auto variant piercings_c_hidden when c
        group multiple auto variant piercings_d_hidden when d


        attribute pubes null
        group pubes auto when pubes


        attribute pregnant null
        group pregnant auto when pregnant


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c
        group multiple auto variant piercings_d when d


        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when a and pregnant and not (bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant b_pregnant when b and pregnant and not (bottomless or naked)
        group bot auto variant c when c and not (pregnant or bottomless or naked)
        group bot auto variant c_pregnant when c and pregnant and not (bottomless or naked)
        group bot auto variant d when d and not (pregnant or bottomless or naked)
        group bot auto variant d_pregnant when d and pregnant and not (bottomless or naked)

        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant a_pregnant when a and pregnant and not (topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant b_pregnant when b and pregnant and not (topless or naked)
        group top auto variant c when c and not (pregnant or topless or naked)
        group top auto variant c_pregnant when c and pregnant and not (topless or naked)
        group top auto variant d when d and not (pregnant or topless or naked)
        group top auto variant d_pregnant when d and pregnant and not (topless or naked)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar
        group necklace auto variant c when c and not collar
        group necklace auto variant d when d and not collar


        group arms auto variant low
        group arms auto:
            attribute d null


        group acc_arm auto variant low_d when d and not (topless or naked)
        group acc_arm auto variant a when a and not (topless or naked)
        group acc_arm auto variant b when b and not (topless or naked)
        group acc_arm auto variant c when c and not (topless or naked) and not (pregnant and sluttydate)
        group acc_arm auto variant c_pregnant when c and pregnant and sluttydate and not (topless or naked)


        group acc_up auto variant a when a and not (topless or naked)
        group acc_up auto variant b when b and not (topless or naked)
        group acc_up auto variant c when c and not (topless or naked)
        group acc_up auto variant d when d and not (topless or naked)

        group head auto


        attribute blush
        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b
        group exp auto variant c when c

        group eyes auto  when d:
            attribute eyes_normal default
        always "kiara_close_mouth_smoking" when d
        attribute tears

        group poke auto variant a when a and not (topless or naked)
        group poke auto variant b when b and not (topless or naked)
        group poke auto variant c when c and not (topless or naked)
        group poke auto variant d when d and not (topless or naked)

        group poke_piercing auto variant a when a and nipples and not (topless or naked)
        group poke_piercing auto variant b when b and nipples and not (topless or naked)
        group poke_piercing auto variant c when c and nipples and not (topless or naked)
        group poke_piercing auto variant d when d and nipples and not (topless or naked)


        group haircuts auto variant a when a and (not cap or (topless or naked))
        group haircuts auto variant b when b and (not cap or (topless or naked))
        group haircuts auto variant c when c and (not cap or (topless or naked))
        group haircuts auto variant d when d and (not cap or (topless or naked))


        group hat auto variant a when a and not (cap or topless or naked)
        group hat auto variant b when b and not (cap or topless or naked)
        group hat auto variant c when c and not (cap or topless or naked)
        group hat auto variant d when d and not (cap or topless or naked)


        group cap auto when cap and not (topless or naked)


        group glasses auto variant a when a and not (topless or naked)
        group glasses auto variant b when b and not (topless or naked)
        group glasses auto variant c when c and not (topless or naked)
        group glasses auto variant d when d and not (topless or naked)


        group arms auto variant up


        group acc_arm auto variant up_d when d and not (topless or naked)


        group multiple auto variant piercings_a_front when a
        group multiple auto variant piercings_b_front when b
        group multiple auto variant piercings_c_front when c
        group multiple auto variant piercings_d_front when d


        group arm auto when not c
        group arm auto variant c when c

    layeredimage kiara maidcafe blowjob:
        attribute squirt
        always:
            "kiara_maidcafe_blowjob_bg"

        always:
            "kiara_maidcafe_blowjob_kiara"

        always:
            "kiara_maidcafe_blowjob_mike"

        always:
            if_any "squirt"
            "kiara_maidcafe_blowjob_squirt"

        group eyes auto:
            attribute down default

        group mouth auto:
            attribute smile default

        group hand auto:
            attribute mast default

        group dick auto:
            attribute medium default
            attribute blow null

        group multiple auto variant cum
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
