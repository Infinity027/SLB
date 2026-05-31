init 1:
    layeredimage natalie:
        attribute_function Pickers([PositionPicker, PregnancyPicker, PubesPicker, PiercingsPicker, CollarPicker, OutfitPicker], npc=natalie)


        attribute naked null
        group position auto


        attribute pubes when a


        attribute pregnant null
        group pregnant auto when pregnant


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute collar null
        group collar auto when collar


        attribute blush null
        group blush auto when blush


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default


        group glasses auto when not scheming
        group glasses auto variant b when b and not scheming:
            attribute up default


        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant a_preg when a and pregnant and not (bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant b_preg when b and pregnant and not (bottomless or naked)


        attribute topless null
        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant a_preg when a and pregnant and not (topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant b_preg when b and pregnant and not (topless or naked)


        group multiple auto variant piercings_a_poke when a and not (topless or naked)
        group multiple auto variant piercings_b_poke when b and not (topless or naked)


        attribute nobraces null
        group braces auto variant a when a and not (pregnant or nobraces or topless or naked)
        group braces auto variant a_preg when a and pregnant and not (nobraces or topless or naked)
        group braces auto variant b when b and not (pregnant or nobraces or topless or naked)
        group braces auto variant b_preg when b and pregnant and not (nobraces or topless or naked)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar


        group acc_head auto variant a when a and not (topless or naked)
        group acc_head auto variant b when b and not (topless or naked)

    layeredimage natalie close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PregnancyPicker, PubesPicker, PiercingsPicker, CollarPicker, OutfitPicker], npc=natalie)


        group position auto


        attribute pubes when a


        attribute pregnant null
        group pregnant auto when pregnant


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute collar null
        group collar auto when collar


        attribute blush null
        group blush auto when blush


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default


        group glasses auto when not scheming
        group glasses auto variant b when b and not scheming:
            attribute up default


        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant a_preg when a and pregnant and not (bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant b_preg when b and pregnant and not (bottomless or naked)


        attribute topless null
        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant a_preg when a and pregnant and not (topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant b_preg when b and pregnant and not (topless or naked)


        group multiple auto variant piercings_a_poke when a and not (topless or naked)
        group multiple auto variant piercings_b_poke when b and not (topless or naked)


        attribute nobraces null
        group braces auto variant a when a and not (pregnant or nobraces or topless or naked)
        group braces auto variant a_preg when a and pregnant and not (nobraces or topless or naked)
        group braces auto variant b when b and not (pregnant or nobraces or topless or naked)
        group braces auto variant b_preg when b and pregnant and not (nobraces or topless or naked)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar


        group acc_head auto variant a when a and not (topless or naked)
        group acc_head auto variant b when b and not (topless or naked)

    layeredimage natalie smartphone:
        always "natalie_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
