init 1:
    layeredimage amy:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=amy)

        attribute idle null

        group position auto

        attribute pubes null
        group pubes auto when pubes

        attribute blush null
        group blush auto when blush

        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default

        attribute naked null

        attribute bottomless null

        attribute topless null

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
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=amy)

        attribute idle null

        group position auto

        attribute pubes null
        group pubes auto when pubes

        attribute blush null
        group blush auto  when blush

        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default

        attribute naked null

        attribute bottomless null

        attribute topless null
 
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
