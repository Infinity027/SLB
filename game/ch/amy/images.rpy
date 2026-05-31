init 1:
    layeredimage amy:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=amy)


        attribute idle null


        group position auto


        attribute pubes null
        group pubes auto when pubes


        attribute pregnant null
        group pregnant auto when pregnant


        attribute blush null
        group blush auto when blush


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default



        group multiple auto variant piercings_a when a
        group piercings auto variant a_normal when a and not work
        group piercings auto variant a_work when a and work and (topless or naked)

        group multiple auto variant piercings_b when b
        group piercings auto variant b_normal when b and not work
        group piercings auto variant b_work when b and work and (topless or naked)


        attribute naked null


        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when (a and pregnant) and not (bottomless or naked)
        group bot auto variant b_pregnant when (b and pregnant) and not (bottomless or naked)


        attribute topless null
        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant a_pregnant when (a and pregnant) and not (topless or naked)
        group top auto variant b_pregnant when (b and pregnant) and not (topless or naked)
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)


        group acc_arm auto variant a when a
        group acc_arm auto variant b when b


        attribute collar null
        group collar auto when collar


        group wig auto variant a when a
        group wig auto variant b when b


        group acc_head auto variant a when a
        group acc_head auto variant b when b

        group acc_tag auto variant a_nipples when a and nipples and not (topless or naked)
        group acc_tag auto variant a_outfit when a and not nipples and not (topless or naked)
        group acc_tag auto variant b_nipples when b and nipples and not (topless or naked)
        group acc_tag auto variant b_outfit when b and not nipples and not (topless or naked)


        group arm auto
        group arm auto variant a when a
        group arm auto variant b when b

    layeredimage amy close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=amy)


        attribute idle null


        group position auto


        attribute pubes null
        group pubes auto when pubes


        attribute pregnant null
        group pregnant auto when pregnant


        attribute blush null
        group blush auto  when blush


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default



        group multiple auto variant piercings_a when a
        group piercings auto variant a_normal when a and not work
        group piercings auto variant a_work when a and work and (topless or naked)

        group multiple auto variant piercings_b when b
        group piercings auto variant b_normal when b and not work
        group piercings auto variant b_work when b and work and (topless or naked)


        attribute naked null


        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when (a and pregnant) and not (bottomless or naked)
        group bot auto variant b_pregnant when (b and pregnant) and not (bottomless or naked)


        attribute topless null
        group top auto variant a when a and not (pregnant or topless or naked)
        group top auto variant b when b and not (pregnant or topless or naked)
        group top auto variant a_pregnant when (a and pregnant) and not (topless or naked)
        group top auto variant b_pregnant when (b and pregnant) and not (topless or naked)
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)


        group acc_arm auto variant a when a
        group acc_arm auto variant b when b


        attribute collar null
        group collar auto when collar


        group wig auto variant a when a
        group wig auto variant b when b


        group acc_head auto variant a when a
        group acc_head auto variant b when b

        group acc_tag auto variant a_nipples when a and nipples and not (topless or naked)
        group acc_tag auto variant a_outfit when a and not nipples and not (topless or naked)
        group acc_tag auto variant b_nipples when b and nipples and not (topless or naked)
        group acc_tag auto variant b_outfit when b and not nipples and not (topless or naked)


        group arm auto
        group arm auto variant a when a
        group arm auto variant b when b

    layeredimage amy kiss teaser:
        always "amy_kiss_teaser"

    layeredimage amy fuck electronic:
        attribute_function Pickers([DickPicker])

        always "amy_fuck_electronic_background"

        always "amy_fuck_electronic_bodies"

        group left_side auto:
            attribute insert
            attribute shawn

        group penetration if_any "insert":
            attribute anal null
            attribute vaginal null

        group fuck_anal auto if_all ["anal", "insert"] if_not "creampie"
        group fuck_vaginal auto if_all ["vaginal", "insert"] if_not "creampie"

        attribute cum null
        group cum_anal auto if_all ["anal", "cum", "insert"] if_not "creampie"
        group cum_vaginal auto if_all ["vaginal", "cum", "insert"] if_not "creampie"

        attribute creampie null
        group creampie auto if_all ["creampie", "insert"]

        always "amy_fuck_electronic_outfits_amy"
        always "amy_fuck_electronic_outfits_mike"
        always if_any "shawn":
            "amy_fuck_electronic_outfits_shawn"

        group amyexpressions auto:
            attribute normal default null

        group shawnexpressions auto if_any "shawn":
            attribute surprised default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
