init 1:
    layeredimage kiara:
        attribute_function Pickers([PositionPicker, CollarPicker,  PubesPicker, HaircutPicker, OutfitPicker], npc=kiara)

        attribute idle null

        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute cap null

        group body_position auto

        attribute collar null
        group collar auto when collar

        attribute pubes null
        group pubes auto when pubes

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
        group acc_arm auto variant c when c and not (topless or naked) and not sluttydate

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

        group arm auto when not c
        group arm auto variant c when c

    layeredimage kiara close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, CollarPicker,  PubesPicker, HaircutPicker, OutfitPicker], npc=kiara)

        attribute idle null

        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute cap null

        group body_position auto

        attribute collar null
        group collar auto when collar

        attribute pubes null
        group pubes auto when pubes

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
        group acc_arm auto variant c when c and not (topless or naked) and sluttydate

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

        group arm auto when not c
        group arm auto variant c when c

