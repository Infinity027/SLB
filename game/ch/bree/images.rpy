init 1:
    layeredimage bree:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=bree)


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



        group multiple auto variant piercings_a when a and not (navel or pregnant_navel)
        group multiple auto variant piercings_a when a and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_a_rpg when a and rpg
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_evil when a and evil
        group multiple auto variant piercings_a_mouthful when a and mouthful
        group multiple auto variant piercings_a_wink when a and wink
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_dazed when a and dazed
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_flirt when a and flirt
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_lose when a and lose
        group multiple auto variant piercings_a_thumb when a and thumb

        group multiple auto variant piercings_b when b and not (navel or pregnant_navel)
        group multiple auto variant piercings_b when b and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_b_rpg when b and rpg
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_evil when b and evil
        group multiple auto variant piercings_b_mouthful when b and mouthful
        group multiple auto variant piercings_b_wink when b and wink
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_dazed when b and dazed
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_flirt when b and flirt
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_lose when b and lose
        group multiple auto variant piercings_b_thumb when b and thumb

        group multiple auto variant piercings_d when d and not (navel or pregnant_navel)
        group multiple auto variant piercings_d when d and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_d_rpg when d and rpg
        group multiple auto variant piercings_d_sad when d and sad
        group multiple auto variant piercings_d_surprised when d and surprised
        group multiple auto variant piercings_d_evil when d and evil
        group multiple auto variant piercings_d_mouthful when d and mouthful
        group multiple auto variant piercings_d_wink when d and wink
        group multiple auto variant piercings_d_happy when d and happy
        group multiple auto variant piercings_d_angry when d and angry
        group multiple auto variant piercings_d_dazed when d and dazed
        group multiple auto variant piercings_d_annoyed when d and annoyed
        group multiple auto variant piercings_d_flirt when d and flirt
        group multiple auto variant piercings_d_normal when d and normal
        group multiple auto variant piercings_d_cry when d and cry
        group multiple auto variant piercings_d_lose when d and lose
        group multiple auto variant piercings_d_thumb when d and thumb

        group multiple auto variant piercings_z when z and not (navel or pregnant_navel)
        group multiple auto variant piercings_z when z and (navel or pregnant_navel) and not dominatrix
        group multiple auto variant piercings_z_dominatrix when z and dominatrix
        group multiple:
            attribute navel null
            attribute pregnant_navel null
        group multiple auto variant piercings_z_sad when z and sad
        group multiple auto variant piercings_z_surprised when z and surprised
        group multiple auto variant piercings_z_evil when z and evil
        group multiple auto variant piercings_z_mouthful when z and mouthful
        group multiple auto variant piercings_z_wink when z and wink
        group multiple auto variant piercings_z_happy when z and happy
        group multiple auto variant piercings_z_angry when z and angry
        group multiple auto variant piercings_z_dazed when z and dazed
        group multiple auto variant piercings_z_annoyed when z and annoyed
        group multiple auto variant piercings_z_flirt when z and flirt
        group multiple auto variant piercings_z_normal when z and normal
        group multiple auto variant piercings_z_cry when z and cry
        group multiple auto variant piercings_z_lose when z and lose
        group multiple auto variant piercings_z_thumb when z and thumb


        attribute naked null


        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]
        always "bree_haircuts_a_bowsette_haircut" if_all ["bowsette", "a"]
        always "bree_haircuts_b_bowsette_haircut" if_all ["bowsette", "b"]
        always "bree_haircuts_d_bowsette_haircut" if_all ["bowsette", "d"]


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "d" if_any ["d"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "z" if_any ["z"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "d" if_any ["d"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "z" if_any ["z"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["topless", "naked"]


        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]
        group stockings auto variant "z" if_all ["z"] if_not ["pregnant", "bottomless", "naked"]
        group stockings auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        group garterbelt auto variant "z" if_all ["z"] if_not ["pregnant"]
        group garterbelt auto variant "z_pregnant" if_all ["z", "pregnant"]


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
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=bree)


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



        group multiple auto variant piercings_a when a and not (navel or pregnant_navel)
        group multiple auto variant piercings_a when a and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_a_rpg when a and rpg
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_evil when a and evil
        group multiple auto variant piercings_a_mouthful when a and mouthful
        group multiple auto variant piercings_a_wink when a and wink
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_dazed when a and dazed
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_flirt when a and flirt
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_lose when a and lose
        group multiple auto variant piercings_a_thumb when a and thumb

        group multiple auto variant piercings_b when b and not (navel or pregnant_navel)
        group multiple auto variant piercings_b when b and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_b_rpg when b and rpg
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_evil when b and evil
        group multiple auto variant piercings_b_mouthful when b and mouthful
        group multiple auto variant piercings_b_wink when b and wink
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_dazed when b and dazed
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_flirt when b and flirt
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_lose when b and lose
        group multiple auto variant piercings_b_thumb when b and thumb

        group multiple auto variant piercings_d when d and not (navel or pregnant_navel)
        group multiple auto variant piercings_d when d and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_d_rpg when d and rpg
        group multiple auto variant piercings_d_sad when d and sad
        group multiple auto variant piercings_d_surprised when d and surprised
        group multiple auto variant piercings_d_evil when d and evil
        group multiple auto variant piercings_d_mouthful when d and mouthful
        group multiple auto variant piercings_d_wink when d and wink
        group multiple auto variant piercings_d_happy when d and happy
        group multiple auto variant piercings_d_angry when d and angry
        group multiple auto variant piercings_d_dazed when d and dazed
        group multiple auto variant piercings_d_annoyed when d and annoyed
        group multiple auto variant piercings_d_flirt when d and flirt
        group multiple auto variant piercings_d_normal when d and normal
        group multiple auto variant piercings_d_cry when d and cry
        group multiple auto variant piercings_d_lose when d and lose
        group multiple auto variant piercings_d_thumb when d and thumb

        group multiple auto variant piercings_z when z and not (navel or pregnant_navel)
        group multiple auto variant piercings_z when z and (navel or pregnant_navel) and not dominatrix
        group multiple auto variant piercings_z_dominatrix when z and dominatrix
        group multiple:
            attribute navel null
            attribute pregnant_navel null
        group multiple auto variant piercings_z_sad when z and sad
        group multiple auto variant piercings_z_surprised when z and surprised
        group multiple auto variant piercings_z_evil when z and evil
        group multiple auto variant piercings_z_mouthful when z and mouthful
        group multiple auto variant piercings_z_wink when z and wink
        group multiple auto variant piercings_z_happy when z and happy
        group multiple auto variant piercings_z_angry when z and angry
        group multiple auto variant piercings_z_dazed when z and dazed
        group multiple auto variant piercings_z_annoyed when z and annoyed
        group multiple auto variant piercings_z_flirt when z and flirt
        group multiple auto variant piercings_z_normal when z and normal
        group multiple auto variant piercings_z_cry when z and cry
        group multiple auto variant piercings_z_lose when z and lose
        group multiple auto variant piercings_z_thumb when z and thumb


        attribute naked null


        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]
        always "bree_close_haircuts_a_bowsette_haircut" if_all ["bowsette", "a"]
        always "bree_close_haircuts_b_bowsette_haircut" if_all ["bowsette", "b"]
        always "bree_close_haircuts_d_bowsette_haircut" if_all ["bowsette", "d"]


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "d" if_any ["d"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "z" if_any ["z"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "d" if_any ["d"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "z" if_any ["z"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["topless", "naked"]


        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]
        group stockings auto variant "z" if_all ["z"] if_not ["pregnant", "bottomless", "naked"]
        group stockings auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        group garterbelt auto variant "z" if_all ["z"] if_not ["pregnant"]
        group garterbelt auto variant "z_pregnant" if_all ["z", "pregnant"]


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

    layeredimage bree rough oral:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, PubesPicker, OutfitPicker], npcs=[bree], append_npc_from_attributes=True)


        group bg auto:
            attribute pool default


        attribute bree null
        group position auto:
            attribute closed default

        group fg auto


        attribute bree_pregnant


        attribute bree_pubes

        attribute pain


        group multiple auto variant piercings
        group multiple:
            attribute bree_ears null
            attribute bree_lips null
            attribute bree_nose null
            attribute bree_tongue null
            attribute sasha_ears null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_nipples null
            attribute sasha_nose null
            attribute sasha_tongue null


        attribute naked null

        group swimsuit auto variant "bot" if_all ["bree_swimsuit"]
        group swimsuit_pregnant auto variant "bot" if_all ["bree_swimsuit", "bree_pregnant"]
        group swimsuit_sexy auto variant "bot" if_all ["bree_sexyswimsuit"] if_not "bree_pregnant"
        group swimsuit_sexy_pregnant auto variant "bot" if_all ["bree_sexyswimsuit", "bree_pregnant"]

        group top auto


        attribute sasha null
        group sasha auto if_all ["sasha", "open"]:
            attribute normal default
            attribute lick


        attribute sasha_boobjob null
        group sasha_boobjob auto if_all ["sasha", "open", "sasha_boobjob"]


        attribute sasha_haircut null
        group sasha_haircut auto if_all ["sasha", "open", "sasha_haircut"]


        attribute sasha_pregnant null
        group sasha_pregnant auto if_all ["sasha", "open", "sasha_pregnant"]

        attribute fx

        group panel auto

    layeredimage bree switch:
        attribute_function Pickers([PiercingsPicker, OutfitPicker, PregnancyPicker, PubesPicker], npc=bree)


        always "bree_switch_bg"


        attribute pubes


        attribute pregnant


        attribute topless null
        attribute bottomless null

        group outfit_top auto if_not ["topless", "pregnant"]:
            attribute naked null
        group outfit_bot auto if_not ["bottomless", "pregnant"]:
            attribute naked null

        group outfit_top auto variant "pregnant" if_any "pregnant" if_not "topless":
            attribute naked null
        group outfit_bot auto variant "pregnant" if_any "pregnant" if_not "bottomless":
            attribute naked null


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

    layeredimage bree missionary:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, PubesPicker, XrayPicker, MCCGPicker], npc=bree)


        group bg auto:
            attribute bedroom1 default
            attribute bedroom2
            attribute livingroom


        group body auto:
            attribute naked default

        attribute collar


        group expressions auto:
            attribute normal null default
            attribute pleasure null
            attribute ahegao null

        group exp auto variant "bowsette" if_any ["bowsette"]
        group exp auto variant "naked" if_not ["bowsette"]


        always "bree_missionary_legs" if_any ["bowsette"] if_not ["naked"]


        attribute pregnant


        attribute pubes


        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute nose null

        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings_ahegao when ahegao


        attribute bowsette if_not ["naked", "pregnant"]


        attribute arm
        attribute mikemc


        group pussy auto


        group dicks auto:
            attribute outside null default
            attribute vaginal
            attribute anal

        group dicks auto variant "outside" if_any "outside"


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "outside" if_all ["condom", "outside"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie"

        group condomcum auto if_all ["condom"] if_any ["cumshot", "creampie"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute xray null

        group xray_bg auto if_any "xray"


        group xray_creampie auto if_all ["xray", "creampie"] if_not ["condom"]


        group xray_condom auto if_all ["xray", "condom"] if_not ["cum"]


        group xray_condomcum auto variant "xray" if_all ["condom", "xray"] if_any ["cumshot", "creampie"]

    layeredimage bree kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker], npc=bree)


        always:
            "bree_kiss"


        attribute pregnant


        attribute collar


        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
            attribute lips null
        group multiple auto variant piercings


        attribute naked null
        attribute topless null
        group outfit auto when not (pregnant or naked or topless)
        group outfit auto variant pregnant when pregnant and not (naked or topless)


        group outfitmike auto when not naked:
            attribute normal default


        group ears auto when not naked


        group hat auto when not naked


        group acc auto when not naked

    layeredimage bree doggy:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npc=bree)

        attribute noone null

        group bg auto:
            attribute bedroom1 default

        always "bree_doggy_body"

        group mike variant "front" auto if_any "front" if_not ['noone']:
            attribute dickout default
        group mike variant "back" auto if_any "back" if_not ['noone', 'sasha']
        group dick variant "back" auto if_all ["back", "dickout"] if_not ['noone', 'sasha']

        group face auto:
            attribute back default

        attribute collar

        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        attribute pregnant

        attribute pull null
        group pull auto if_any ["pull"]

        attribute condom null
        group condom auto if_any "condom" if_not "noone"
        group condom auto variant "back" if_all ["condom", "back"] if_not ["noone", "cumshot", "vaginal"]
        group condomcum auto if_all ["condom", "cumshot", "back"] if_not "noone"

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        group cumshot auto variant "back" if_all ["cumshot", "back"] if_not ["condom"]

        group multiple auto variant cum

        group eyes auto:
            attribute normal default

        group mouth auto if_any "back":
            attribute normal default

        attribute sasha

        group toy auto
        group toy auto variant "dildo" if_any ["dildoin", "dildoout"]
        group mike variant "back" auto if_all ["back", "beads"] if_not ['noone', 'sasha'] if_any ["cumshot", "cumonass"]
        group dick variant "back" auto if_all ["back", "dickout", "beads"] if_not ['noone', 'sasha']

        group multiple auto variant fx

    layeredimage bree cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, HaircutPicker, MCCGPicker], npc=bree)

        attribute mikemc null
        attribute mc_naked null


        group bg auto:
            attribute bedroom1 default


        group bodies auto:
            attribute naked default

        attribute mc_halloween

        attribute nohaircut null
        attribute haircut


        group acc_stockings auto if_not ["noacc"]


        attribute collar


        attribute blush



        group eyes auto:
            attribute down default

        group mouth auto:
            attribute smile default


        group acc_cap auto if_not ["noacc"]


        group top auto


        attribute pregnant


        attribute pubes


        group bot auto variant "out" if_any "out" if_not ["pregnant", "onass", "onpussy"]
        group bot auto variant "out_pregnant" if_all ["out", "pregnant"] if_not ["onass", "onpussy"]
        group bot auto variant "resting" if_any "resting" if_not ["pregnant", "onass", "onpussy"]
        group bot auto variant "resting_pregnant" if_all ["resting", "pregnant"] if_not ["onass", "onpussy"]


        group dick auto:
            attribute resting null default
            attribute out null
            attribute anal
            attribute vaginal

        group dick auto variant "out" if_any "out"
        group dick auto variant "resting" if_any "resting"


        group bot auto variant "anal" if_any ["anal", "onass"] if_not "pregnant"
        group multiple auto variant bot_anal_pregnant when pregnant and (anal or onass)
        group bot auto variant "vaginal" if_any ["vaginal", "onpussy"] if_not "pregnant"
        group multiple auto variant bot_vaginal_pregnant when pregnant and (vaginal or onpussy)


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute cum null
        group multiple auto variant cum when cum
        group cum auto variant "pregnant" if_all ["cum", "pregnant"]
        group cum auto variant "nopregnant" if_any ["cum"] if_not ["pregnant"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cum", "condomcum"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum", "condomcum"]

        attribute condomcum null
        group condomcum auto if_all ["condom", "condomcum"]


        attribute dickcum null
        group dickcum auto if_any "dickcum"


        attribute cumshot null
        group cumshot auto if_any "cumshot"


        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute lips null
            attribute tongue null

        group fx auto

    layeredimage bree titfuck:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, HaircutPicker], npc=bree)


        group bg auto:
            attribute livingroom default


        group body auto:
            attribute mike default
        group malepubes auto


        group boobs auto:
            attribute down default

        group piercings:
            attribute clit null
            attribute ears null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null


        attribute nipples null
        group nipples auto if_any ["nipples"]


        group dickmike auto variant "up" if_all ["mike", "up"]
        group dickmike auto variant "down" if_all ["mike", "down"]
        group dickdwayne auto if_any ["dwayne"]
        group dickjack auto if_any ["jack"]
        group dickscottie auto if_any ["scottie"]


        group head auto:
            attribute normal default

        attribute nohaircut null
        group haircut auto if_any "haircut"

        attribute collar null
        group collar auto if_any ["collar"]
        group exp auto if_any ["normal"]:
            attribute smile default
        group eyes auto if_any ["normal"]:
            attribute open null default
        group eyes auto variant "facecum" if_all ["normal", "facecum"]
        group eyes auto variant "nofacecum" if_any ["normal"] if_not ["facecum"]


        attribute nose null
        group nose auto if_any ["nose"]


        attribute cum null
        group cum auto if_any ["cum"]
        attribute dickcum if_any ["down"]
        attribute tonguecum null
        group tonguecum auto if_all ["tonguecum", "tongueout", "normal"]
        always "bree_titfuck_tonguecum_lick" if_all ["tonguecum", "lick"]
        attribute facecum


        group hands auto
        group belly auto

    layeredimage bree spoon:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, HaircutPicker, DickPicker], npc=bree)


        group bg auto:
            attribute bedroom1 default


        always "bree_spoon_bodies"
        group body auto
        attribute haircut


        attribute collar


        attribute pubes

        group multiple auto variant piercings_behind


        attribute pregnant


        group multiple auto variant piercings


        attribute speed


        group head auto:
            attribute mike default


        attribute sweat


        attribute bodycum


        group dick auto:
            attribute out default null
        group dick auto variant "out" if_all ["out", "mike"]
        always "bree_spoon_dick_out_small" if_all ["out", "scottie"]


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "out"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]
        group condomcum auto if_all ["condom", "cum", "out"]


        group expeyes auto:
            attribute eyes_closed default
        group expmouth auto:
            attribute mouth_pleasure default
        attribute breath if_not ["mouth_pain"]


        group arm auto variant "mike" if_any ["mike"]:
            attribute pull default
        group arm auto variant "scottie" if_any ["scottie"]:
            attribute pull default
        attribute speedfinger null
        group speedfinger auto if_all ["speedfinger", "finger"]


        attribute squirt

    layeredimage bree showersex:
        attribute_function Pickers([PregnancyPicker, CollarPicker], npc=bree)

        always "bree_showersex_background"

        always "bree_showersex_water"

        always "bree_showersex_body"

        attribute pregnant

        group multiple auto variant piercings

        attribute collar

        group multiple auto variant fx

    layeredimage bree mast:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker], npc=bree)


        always "bree_mast_bg"


        always "bree_mast_body"


        attribute pubes


        attribute pregnant


        group eyes auto:
            attribute cum default
        group mouth auto if_not ["mouth"]


        attribute tongue if_not ["pain"]
        group multiple auto variant piercings


        always "bree_mast_left_arm" if_not ["left"]
        always "bree_mast_left_arm" if_all ["left"] if_any ["mouth", "ass"]


        group what:
            attribute finger null default
            attribute dildo null


        attribute left null
        group where:
            attribute pussy null default
            attribute ass null
            attribute mouth null


        group siz:
            attribute small null default
            attribute medium null
            attribute big null


        group pussy auto if_any ["pussy"] if_not ["left"]
        group pussy_dildo auto if_all ["pussy", "dildo"] if_not ["left", "small"]
        group pussy_left auto if_all ["pussy", "left"]
        group pussy_left_dildo auto if_all ["pussy", "left", "dildo"] if_not ["small"]
        group ass auto if_any ["ass"]
        group ass_dildo auto if_all ["ass", "dildo"] if_not ["small"]
        group fuck_mouth auto if_any ["mouth"]
        group fuck_mouth_dildo auto if_all ["mouth", "dildo"] if_not ["small"]


        group wet auto
        group wet auto variant "left" if_any ["left"]
        group wet auto variant "noleft" if_not ["left"]

    layeredimage bree ending:
        attribute_function Pickers([CollarPicker, EndingKidPicker], npc=bree)

        always:
            "bree_ending_bree"
        attribute collar

        attribute kid

    layeredimage bree pillow attack:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], npc=bree)

        always "bree_pillow_attack_bree"
        attribute pregnant
        group multiple auto variant piercings
        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute sleep default
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]
        attribute collar

    layeredimage bree fuckgames:

        always "bree_fuckgames_bg"
        always "bree_fuckgames_body"

        attribute thrust
        attribute dick
        attribute cum
        attribute fx

        group exp auto:
            attribute normal default

    layeredimage bree maidbj:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=bree)

        always "bree_maidbj_bg"
        always "bree_maidbj_table"
        always "bree_maidbj_body"

        attribute collar

        group exp auto:
            attribute normal default

        attribute nose

        attribute nodick null
        always "bree_maidbj_dick_out" if_any ["normal", "swallow"] if_not ["nodick"]

        attribute cum null
        group cum auto if_any ["cum"]


        attribute phone null
        group phone auto if_any ["phone"]

    layeredimage bree cinema bj:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, DickPicker, HaircutPicker, MCCGPicker])
        attribute breemc null
        attribute mikemc null

        attribute bree null
        attribute mike null

        attribute doctor null


        group bg auto:
            attribute theatre default
            attribute hospital
            attribute bedroom
            attribute livingroom
            attribute office


        always "bree_cinema_bj_body"
        group haircuts auto variant "bree" if_not ["naked", "doctor"] if_any "bree":
            attribute nohaircut null
        group mchaircuts auto variant "breemc" if_not ["naked"] if_any "breemc":
            attribute mc_nohaircut null


        attribute naked null
        group outfits auto variant "mike" if_not ["naked", "doctor"] if_any "mike"
        group mcoutfits auto variant "mikemc" if_not ["naked"] if_any "mikemc"

        always:
            if_any "doctor"
            "bree_cinema_bj_outfits_mike_doctor"


        group piercings auto:
            attribute clit null
            attribute mc_clit null
            attribute ears null
            attribute mc_ears null
            attribute navel null
            attribute mc_navel null
            attribute pregnant_navel null
            attribute mc_pregnant_navel null
            attribute tongue null
            attribute mc_tongue null
            attribute lips null
            attribute mc_lips null
            attribute mc_nipples:
                "bree_cinema_bj_piercings_nipples"
            attribute mc_nose:
                "bree_cinema_bj_piercings_nose"

        group outfits auto variant "bree" if_not ["naked"] if_any "bree"
        group mcoutfits auto variant "breemc" if_not ["naked"] if_any "breemc"


        attribute collar null
        group collar auto if_any ["collar"]

        attribute mc_collar null
        group collar auto if_all ["mc_collar", "breemc"]



        group dick auto:
            attribute mc_big:
                "bree_cinema_bj_dick_big"
            attribute mc_medium:
                "bree_cinema_bj_dick_medium"
            attribute mc_small:
                "bree_cinema_bj_dick_small"


        attribute cum null
        group cum auto if_any ["cum"]


        always:
            if_any "cinema"
            "bree_cinema_bj_dark"


        group light auto

    layeredimage bree bjgames:
        attribute_function Pickers([DayNightPicker, CollarPicker, PiercingsPicker], npc=bree)


        group bg auto


        always "bree_bjgames_body"


        always "bree_bjgames_mike_hand"
        attribute sweat:
            "bree_bjgames_mike_sweat"


        attribute collar


        attribute blush
        group eyes auto:
            attribute up default
        group mouth auto:
            attribute normal default


        attribute nose
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null


        group dick auto:
            attribute small default
            attribute blow null

        attribute serious


        group fx auto


        group multiple auto variant cum


        always "bree_bjgames_shadows" if_any ["night"]

    layeredimage bree dad bj:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=bree)


        always "bree_dad_bj_bg"


        attribute nodad null
        always "bree_dad_bj_body_breedad" if_not ["nodad"]


        attribute aura if_not ["nodad"]:
            "bree_dad_bj_breedad_aura"


        always "bree_dad_bj_body_bree"
        always "bree_dad_bj_body_mike"


        attribute collar


        attribute blush
        group eyes auto:
            attribute up default
        group mouth auto:
            attribute smile default


        attribute nose


        group dick auto:
            attribute small default
            attribute blow null


        group breedad_exp auto if_not ["nodad"]:
            attribute surprised default


        group multiple auto variant bree_fx


        group multiple auto variant cum

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

    layeredimage bree cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, MCGenderPicker])

        attribute bree null
        attribute breemc null
        attribute mikemc null

        attribute shake
        attribute vibrate
        attribute fingerass
        attribute notongue null

        group bg auto:
            attribute bedroom1 default
        always "bree_cunnilingus_body_bree"

        attribute collar

        group bree_fx auto


        group exp auto:
            attribute normal default


        attribute pubes null
        group pubes auto if_any ["pubes"]:
            attribute classic default


        group multiple auto variant piercings_pregnant when pregnant and bree
        attribute pregnant if_any ["bree"]


        attribute lips null
        attribute ears null
        attribute tongue null
        group multiple auto variant piercings when bree
        group multiple auto variant piercings_classic when bree and not pregnant

        always "bree_cunnilingus_finger_left_fingerass" if_all ["dildopussy", "fingerass"] if_any ["mike", "mikemc"]


        group tongue auto variant "mike" if_any ["mikemc", "mike"]
        group tongue auto variant "sasha" if_any ["sasha"]

        group bb auto variant "still" if_all ["sasha"] if_not ["up", "middle", "down", "notongue"]
        group bb auto variant "lick" if_all ["sasha"] if_any ["up", "middle", "down", "notongue"]

        group body auto variant "still" if_not ["up", "middle", "down", "notongue"]
        group body auto variant "lick" if_any ["up", "middle", "down", "notongue"]

        group hairs auto variant "still" if_all ["sasha"] if_not ["up", "middle", "down", "notongue"]
        group hairs auto variant "lick" if_all ["sasha"] if_any ["up", "middle", "down", "notongue"]

        always "bree_cunnilingus_bree_hands" if_any ["up", "middle", "down", "notongue"] if_not ["sasha"]

        always "bree_cunnilingus_finger_fingerass" if_all ["fingerass"] if_any ["mikemc", "mike"] if_not ["dildopussy"]

        group dildo auto variant "mike" if_any ["mikemc", "mike"] if_not "pregnant"
        group dildo auto variant "sasha" if_any ["sasha"] if_not "pregnant"
        group dildo auto variant "mike_pregnant" if_all ["pregnant", "dildopussy"] if_any ["mikemc", "mike"]
        group dildo auto variant "sasha_pregnant" if_all ["pregnant", "dildopussy", "sasha"]

        group multiple auto variant fx when shake
        group multiple auto variant fx when vibrate

    layeredimage bree kitchen bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker], npc=bree)

        always "bree_kitchen_bj_bg"
        always "bree_kitchen_bj_bodies"
        always "bree_kitchen_bj_apron"

        group exp auto:
            attribute normal default

        group multiple auto variant piercings

        attribute collar

        attribute flaccid null
        group dick auto if_not ["flaccid", "rub", "blow"]
        group dick auto variant "flaccid" if_any ["flaccid"] if_not ["rub", "blow"]

        group bree auto

        group multiple auto variant cum

        always "bree_kitchen_bj_fg"

    layeredimage bree rough doggy:
        attribute_function Pickers([DickPicker, CollarPicker, PiercingsPicker, PregnancyPicker, DayNightPicker], npc=bree)

        group bg auto:
            attribute bedroom1 default

        group bg auto variant "day" if_any "day"
        group bg auto variant "night" if_any "night"

        always "bree_rough_doggy_bodies"

        attribute pregnant

        attribute collar

        attribute blush

        group exp auto:
            attribute happy default

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute lips null
            attribute tongue null

        group dicks auto:
            attribute out null default
            attribute vaginal null

        group dick auto variant out when out
        attribute vaginal null
        always "bree_rough_doggy_dick_vaginal" if_any ["vaginal"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["vaginal", "condom"]

        attribute cum null
        group cum_out auto if_any ["cum"] if_not ["vaginal", "condom"]
        always "bree_rough_doggy_cum_vaginal" if_all ["cum", "vaginal"] if_not ["condom"]
        attribute onbody null
        always "bree_rough_doggy_cum_onbody" if_all ["cum", "onbody"] if_not ["condom"]

        attribute condom null
        group condom_out auto if_any ["condom"] if_not ["vaginal", "cumshot"]
        group condom auto if_any ["condom"]
        group condom_cum auto if_all ["condom", "cumshot"]

        attribute boobs

    layeredimage bree scissorhands:
        attribute_function Pickers([PregnancyPicker], npc=bree)

        always "bree_scissorhands_bg"

        always "bree_scissorhands_bodies"

        attribute pregnant

        group bree auto:
            attribute normal default

        group mike auto:
            attribute waiting default

        group haircut auto

    layeredimage bree zbox games:
        attribute_function Pickers([PiercingsPicker, CollarPicker], npc=bree)

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

        group multiple auto variant piercings when not nobree
        group piercings_lips auto if_not ["nobree"]

        always "bree_zbox_games_arms"

        always "bree_zbox_games_arms_mikecasual" if_not ["nakedmike"]

        group cum auto

    layeredimage bree threesome dwaynemike:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=bree)

        group bg auto:
            attribute office default

        always "bree_threesome_dwaynemike_bree"

        attribute pregnant

        group exp_bree auto:
            attribute normal default

        group multiple auto variant piercings

        attribute collar

        attribute pubes

        attribute dwayne

        group dick_dwayne auto if_any ["dwayne"]:
            attribute outside default

        attribute mike null
        group mike_position auto if_any ["mike"]:
            attribute standard default

        group exp_mike auto variant "standard" if_all ["mike"] if_not ["bj"]:
            attribute opened default

        group exp_mike auto variant "bj" if_all ["mike", "bj"]:
            attribute opened default

        group dick_mike auto variant "standard" if_any ["mike"] if_not ["close"]
        group dick_mike auto variant "close" if_all ["mike", "close"] if_not ["suck"]
        attribute suck null
        always "bree_threesome_dwaynemike_dick_mike_suck" if_all ["mike", "close", "suck"]

        attribute condom null
        group condom auto if_all ["dwayne", "condom"]

        attribute cum null
        group condomcum auto if_all ["dwayne", "condom", "cum"]

        attribute creampie null
        group creampie auto if_all ["dwayne", "creampie"] if_any ["anal", "vaginal"] if_not ["condom"]

        attribute cumshot_dwayne null
        group cumshot_dwayne auto if_all ["dwayne", "cumshot_dwayne"]

        group multiple auto variant cum when cum

        attribute cumshot_mike null
        group cumshot_mike auto variant "standard" if_all ["mike", "cumshot_mike"] if_not ["close"]
        group cumshot_mike auto variant "close" if_all ["mike", "cumshot_mike", "close"]

        group fg auto

    layeredimage bree beach bj:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, HaircutPicker, MCCGPicker], npc=bree)


        attribute blush null
        attribute clit null
        attribute collar null
        attribute ears null
        attribute lips null
        attribute navel null
        attribute pregnant_navel null
        attribute tongue null


        always "bree_beach_bj_bg"


        attribute black null
        attribute mikemc null
        always "bree_beach_bj_man_mikemc" when not black
        always "bree_beach_bj_man_black" when black


        always "bree_beach_bj_bree"


        attribute pregnant


        group piercings auto


        group outfit auto:
            attribute naked null


        group head auto:
            attribute handjob default
            attribute blowjob

        group exp auto when blowjob:
            attribute normal default

        attribute tongue when handjob
        attribute cheek_bulge when blowjob


        group collar auto when collar:
            attribute handjob default
            attribute blowjob


        group haircuts auto variant handjob when handjob
        group haircuts auto variant blowjob when blowjob

        group piercings auto variant handjob when handjob
        group piercings auto variant blowjob when blowjob



        group mc_dicks:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        group dick auto variant black when black
        group dick auto variant mc_small when mc_small and not black
        group dick auto variant mc_medium when mc_medium and not black
        group dick auto variant mc_big when mc_big and not black

        group breehand auto
        group breehand auto variant black when black
        group breehand auto variant mc_small when mc_small and not black
        group breehand auto variant mc_medium when mc_medium and not black
        group breehand auto variant mc_big when mc_big and not black

        attribute cumshot null
        group cumshot auto variant black when black and cumshot
        group cumshot auto variant mc_small when mc_small and cumshot and not black
        group cumshot auto variant mc_medium when mc_medium and cumshot and not black
        group cumshot auto variant mc_big when mc_big and cumshot and not black


        attribute cum null
        group cum auto variant handjob when cum and handjob
        group cum auto variant blowjob when cum and blowjob


        always "bree_beach_bj_fg"

    layeredimage bree reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, HaircutPicker, MCCGPicker], npc=bree)

        attribute mikemc null

        group bg auto:
            attribute bedroom1 default

        always "bree_reverse_cowgirl_mike"

        always "bree_reverse_cowgirl_bree"

        attribute collar
        attribute haircut
        attribute pregnant

        attribute pubes null
        group pubes auto if_any "pubes"

        group multiple auto variant piercings

        group fx auto

        group exp auto:
            attribute normal default



        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto if_not "out"

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto if_not "out" if_all "condom"

        attribute hand null
        group hand auto if_any "hand":
            attribute up default

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute cum null
        group condomcum auto if_all ["condom", "cum"]


    layeredimage bree lapdance:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, MCCGPicker], npc=bree)

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

        group multiple auto variant piercings when not nonpc
        group multiple auto variant piercings_ahegao when ahegao and not nonpc
        group multiple auto variant piercings_normal when not (ahegao or nonpc)
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
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, HaircutPicker], npc=bree)

        always "bree_witness_body"

        attribute collar
        attribute nohaircut null
        attribute pregnant

        group multiple auto variant piercings

        group outfit auto if_not ["naked"]
        group pregnant_outfit auto if_any ["pregnant"] if_not ["naked"]

    layeredimage bree spying:
        attribute_function Pickers([HaircutPicker, CollarPicker, PiercingsPicker, OutfitPicker], npc=bree)

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
        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
