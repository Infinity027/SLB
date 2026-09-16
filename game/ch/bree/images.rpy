init 1:
    layeredimage bree:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=bree)

        attribute idle null

        attribute nohaircut null
        group arms:
            attribute arms01 null
            attribute arms02 null default

        group position auto if_not ["bowsette"]
        always "bree_position_a_bowsette" if_all ["bowsette", "a"]
        always "bree_position_b_bowsette" if_all ["bowsette", "b"]
        always "bree_position_d_bowsette" if_all ["bowsette", "d"]

        group arms auto variant "d" if_any "d" if_not "bowsette"
        group arms auto variant "d_bowsette" if_all ["bowsette", "d"]

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute pregnant null
        group pregnant auto if_any ["pregnant"]

        attribute blush

        attribute collar null
        group collar auto if_all ["collar", "d"]

        group null_exp auto:
            attribute normal null default

        group exp auto variant "a" if_any ["a"]
        group exp auto variant "b" if_any ["b"]
        group exp auto variant "d" if_any ["d"]
        group exp auto variant "z" if_any ["z"]

        attribute naked null

        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]
        always "bree_haircuts_a_bowsette_haircut" if_all ["bowsette", "a"]
        always "bree_haircuts_b_bowsette_haircut" if_all ["bowsette", "b"]
        always "bree_haircuts_d_bowsette_haircut" if_all ["bowsette", "d"]

        attribute bottomless null

        attribute topless null

        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]

        group arms_outfits auto variant "d_arms01" if_all ["arms01", "d"] if_not ["arms02", "dominatrix"]
        group arms_outfits auto variant "d_arms02" if_all ["arms02", "d"] if_not ["arms01", "dominatrix"]

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]
        group acc_arm auto variant "d" if_any ["d"]
        group acc_arm auto variant "z" if_any ["z"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]
        group necklace auto variant "d" if_any ["d"] if_not ["collar"]

        group collar auto if_all ["collar"] if_any ["a", "b"]

        attribute leash null
        group leash auto if_any ["leash"]

        group acc_ears auto variant "a" if_any ["a"]
        group acc_ears auto variant "b" if_any ["b"]
        group acc_ears auto variant "d" if_any ["d"]

        group tattoo auto variant "a" if_any ["a"]
        group tattoo auto variant "b" if_any ["b"]
        group tattoo auto variant "d" if_any ["d"]

        group acc_head auto
        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "d" if_any ["d"]

        group acc_waist auto variant "z" if_any ["z"] if_not ["bottomless", "naked"]

        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "d" if_any ["d"]
        group fx auto variant "z" if_any ["z"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "d" if_any ["d"]

    layeredimage bree close:
        yalign 0.12
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=bree)

        attribute idle null

        attribute nohaircut null
        group arms:
            attribute arms01 null
            attribute arms02 null default

        group position auto if_not ["bowsette"]
        always "bree_close_position_a_bowsette" if_all ["bowsette", "a"]
        always "bree_close_position_b_bowsette" if_all ["bowsette", "b"]
        always "bree_close_position_d_bowsette" if_all ["bowsette", "d"]

        group arms auto variant "d" if_any "d" if_not "bowsette"
        group arms auto variant "d_bowsette" if_all ["bowsette", "d"]

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute blush

        attribute collar null
        group collar auto if_all ["collar", "d"]

        group null_exp auto:
            attribute normal null default

        group exp auto variant "a" if_any ["a"]
        group exp auto variant "b" if_any ["b"]
        group exp auto variant "d" if_any ["d"]
        group exp auto variant "z" if_any ["z"]

        attribute naked null

        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]
        always "bree_close_haircuts_a_bowsette_haircut" if_all ["bowsette", "a"]
        always "bree_close_haircuts_b_bowsette_haircut" if_all ["bowsette", "b"]
        always "bree_close_haircuts_d_bowsette_haircut" if_all ["bowsette", "d"]

        attribute bottomless null

        attribute topless null
        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]
    
        group arms_outfits auto variant "d_arms01" if_all ["arms01", "d"] if_not ["arms02", "dominatrix"]
        group arms_outfits auto variant "d_arms02" if_all ["arms02", "d"] if_not ["arms01", "dominatrix"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]
        group acc_arm auto variant "d" if_any ["d"]
        group acc_arm auto variant "z" if_any ["z"]

        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]
        group necklace auto variant "d" if_any ["d"] if_not ["collar"]

        group collar auto if_all ["collar"] if_any ["a", "b"]

        attribute leash null
        group leash auto if_any ["leash"]

        group acc_ears auto variant "a" if_any ["a"]
        group acc_ears auto variant "b" if_any ["b"]
        group acc_ears auto variant "d" if_any ["d"]

        group tattoo auto variant "a" if_any ["a"]
        group tattoo auto variant "b" if_any ["b"]
        group tattoo auto variant "d" if_any ["d"]

        group acc_head auto
        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "d" if_any ["d"]

        group acc_waist auto variant "z" if_any ["z"] if_not ["bottomless", "naked"]

        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "d" if_any ["d"]
        group fx auto variant "z" if_any ["z"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "d" if_any ["d"]

    layeredimage bree smartphone:
        always "bree_smartphone"

    layeredimage bree switch:
        attribute_function Pickers([ OutfitPicker, PubesPicker], npc=bree)

        always "bree_switch_bg"

        attribute pubes
   
        attribute topless null
        attribute bottomless null

        group exp_mike auto:
            attribute mikewin default

        group exp_bree auto:
            attribute breewin default

        always "bree_switch_light"

    layeredimage bree kat coffee talk:

        always "bree_kat_coffee_talk_bg"

        always "bree_kat_coffee_talk_table"

        always "bree_kat_coffee_talk_kat"

        always "bree_kat_coffee_talk_mike"

        always "bree_kat_coffee_talk_bree"

        always "bree_kat_coffee_talk_tabletop"

        group head auto:
            attribute talkkat default

        group exp_bree auto:
            attribute bnormal default

        group exp_kat auto:
            attribute knormal default

        group exp_mike auto variant "talkbree" if_any ["talkbree"]:
            attribute mnormal default
        group exp_mike auto variant "talkkat" if_any ["talkkat"]:
            attribute mnormal default

    layeredimage bree ending:
        attribute_function Pickers([CollarPicker, EndingKidPicker], npc=bree)

        always:
            "bree_ending_bree"
        attribute collar

        attribute kid

    layeredimage bree pillow attack:
        attribute_function Pickers([CollarPicker,  OutfitPicker], npc=bree)

        always "bree_pillow_attack_bree"
        attribute pregnant
        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute sleep default
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]
        attribute collar

    image breedad fx exclamation:
        contains:
            "ch/bree/ev2/dad_bj/bree_dad_bj_breedad_fx_exclamation.webp"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.1
            zoom 0.9
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
            parallel:
                linear 0.05 zoom 1.0
                linear 0.05 zoom 0.9
                repeat

    image breedad fx surprise:
        contains:
            "ch/bree/ev2/dad_bj/bree_dad_bj_breedad_fx_surprise.webp"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.1
            zoom 0.9
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
            parallel:
                linear 0.05 zoom 1.0
                linear 0.05 zoom 0.9
                repeat

    image breedad fx aura:
        contains:
            "ch/bree/ev2/dad_bj/bree_dad_bj_breedad_fx_aura.webp"
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
                repeat

    layeredimage bree scissorhands:
        always "bree_scissorhands_bg"

        always "bree_scissorhands_bodies"

        attribute pregnant

        group bree auto:
            attribute normal default

        group mike auto:
            attribute waiting default

        group haircut auto

    layeredimage bree zbox games:
        attribute_function Pickers([ CollarPicker], npc=bree)

        always "bree_zbox_games_bg"

        always "bree_zbox_games_mike"

        attribute nakedmike null
        always "bree_zbox_games_mikecasual" if_not ["nakedmike"]

        attribute nobree null
        always "bree_zbox_games_bree" if_not ["nobree"]

        group exp auto if_not ["nobree"]:
            attribute normal null default

        attribute nakedbree null
        always "bree_zbox_games_casual" if_not ["nakedbree", "nobree"]

        attribute collar if_not ["nobree"]

        always "bree_zbox_games_arms"

        always "bree_zbox_games_arms_mikecasual" if_not ["nakedmike"]

        group cum auto

    layeredimage bree lapdance:
        attribute_function Pickers([OutfitPicker,  MCCGPicker], npc=bree)

        group bg auto:
            attribute stripclub default

        attribute mikemc null
        attribute naked null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mcoutfit auto when not naked:
            attribute mc_casual default

        attribute nonpc null
        always "bree_lapdance_bree" when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        group multiple:
            attribute ears null
            attribute tongue null

        attribute bree_naked null
        group outfits auto when not (nonpc or naked or bree_naked)

        group arm auto when not (nonpc or fuck)

        always "bree_lapdance_fg"
        always "bree_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage bruce:

        always "bruce_body"

        group exp auto:
            attribute normal default

    layeredimage bree witness:
        attribute_function Pickers([ CollarPicker, OutfitPicker, HaircutPicker], npc=bree)

        always "bree_witness_body"

        attribute collar
        attribute nohaircut null
        attribute pregnant

        group outfit auto if_not ["naked"]
        group pregnant_outfit auto if_any ["pregnant"] if_not ["naked"]

    layeredimage bree spying:
        attribute_function Pickers([HaircutPicker, CollarPicker,  OutfitPicker], npc=bree)

        attribute down null
        attribute topless null
        attribute bottomless null

        always "bree_spying_body"
        attribute nohaircut null
        attribute haircut
        attribute pubes
        always "bree_spying_upperarms"
        group exp auto:
            attribute surprised default
        group bot auto if_not ["down", "bottomless"]
        group bot auto variant "down" if_any ["down"] if_not ["bottomless"]
        group top auto if_not ["topless"]
        group rightarm auto:
            attribute normal default
        group rightarm auto variant "outfit" if_any ["casual"] if_not ["topless"]:
            attribute normal default
        always "bree_spying_leftarm"
        always "bree_spying_leftarm_outfit_casual" if_any ["casual"] if_not ["topless"]
        attribute collar

# image bree_pool_play = "ch/bree/images/home/pool_play.webp"
# image bree_casual_talk = "ch/bree/images/casual/talk.webp"
# image bree_casual_annoyed = "ch/bree/images/casual/annoyed.webp"
# image bree_casual_kiss = "ch/bree/images/casual/kiss.webp"
# image bree_casual_blush = "ch/bree/images/casual/blush.webp"
