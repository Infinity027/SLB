init 1:
    layeredimage amy smartphone:
        always "amy_smartphone"

    layeredimage amy kiss:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker], npc=amy)


        always "amy_kiss_bodies"


        group mikeoutfit auto if_not ["naked"]:
            attribute normal default


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null


        attribute naked null
        attribute topless null
        group outfit auto when not (naked or topless)


        attribute collar

    layeredimage amy cunnilingus:
        attribute_function Pickers([PiercingsPicker, OutfitPicker, PubesPicker, CollarPicker], npc=amy)

        attribute naked null
        group mike:
            attribute mikesit null
            attribute mikelick null


        group bg auto:
            attribute bedroom default


        always "amy_cunnilingus_upperbody"


        group multiple auto variant piercings


        attribute topless null
        group top auto if_not ["topless", "naked"]


        group basearms if_not ["holding"]:
            attribute open
        group basearms if_not ["mikesit", "mikelick"]:
            attribute footjob
        group basesleeves auto variant "open" if_any ["open"] if_not ["holding", "topless", "naked"]
        group basesleeves auto variant "footjob" if_any ["footjob"] if_not ["mikesit", "mikelick", "topless", "naked"]


        group arms if_any ["bedroom"]:
            attribute holding
        group sleeves auto variant "holding" if_all ["holding", "bedroom"] if_not ["topless", "naked"]


        attribute mikesit if_any ["cinema"]


        group legs:
            attribute open
            attribute closed default
        group legs if_not ["mikesit", "mikelick"]:
            attribute footjob


        attribute speed if_any ["footjob"] if_not ["mikesit", "mikelick"]


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute openass if_any ["open"]
        attribute openpussy if_any ["open"]


        group multiple auto variant piercings_open when open


        attribute vibrator if_any ["open"]
        attribute buttplug if_any ["open"]


        group stockings auto variant "open" if_any ["open"] if_not ["bottomless", "naked"]
        group stockings auto variant "closed" if_any ["closed"] if_not ["bottomless", "naked"]


        attribute vibrator_remote if_any ["open"]


        attribute bottomless null
        group bot auto variant "open" if_any ["open"] if_not ["bottomless", "naked"]
        group bot auto variant "closed" if_any ["closed"] if_not ["bottomless", "naked"]


        attribute mikelick if_any ["open"]
        always "amy_cunnilingus_mikelick_outfit" if_all ["mikelick", "open"] if_not ["naked"]
        attribute mikehand if_all ["mikelick", "open"]


        attribute popcorn if_any ["closed"]


        group basearms:
            attribute closed
        group basesleeves auto variant "closed" if_any ["closed"] if_not ["topless", "naked"]


        group arms if_any ["open"] if_not ["mikelick"]:
            attribute masturbating
        group sleeves auto variant "masturbating" if_all ["masturbating", "open"] if_not ["mikelick", "topless", "naked"]


        group head auto:
            attribute down default


        attribute collar null
        group collar auto if_any ["collar"]


        group exp auto variant "down" if_any ["down"]:
            attribute normal default


        group multiple auto variant piercings_down when down
        group multiple auto variant piercings_up when up


        attribute cumshot if_any ["footjob"] if_not ["mikesit", "mikelick"]


        attribute finger null
        group finger auto if_any ["finger"] if_not ["mikesit", "mikelick"]:
            attribute fingerout default


        attribute closeup if_all ["mikelick", "open"]
        attribute notongue null
        group closeup auto variant "tongue" if_all ["mikelick", "open", "closeup"] if_not ["notongue"]:
            attribute tonguedown default

    layeredimage amy bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker, DickPicker], npc=amy)


        group bg auto:
            attribute bedroom default


        always "amy_bj_mike"
        always "amy_bj_mikeoutfit" if_not ["naked"]


        attribute naked null
        always "amy_bj_amy"
        attribute collar
        attribute nipples if_any ["naked"]
        group outfit auto if_not ["naked"]


        attribute handjob null

        always "amy_bj_rightarm" if_not ["handjob"]
        always "amy_bj_rightarm_handjob" if_any ["handjob"]
        group sleeve auto variant "right" if_not ["naked", "handjob"]
        group sleeve auto variant "right_handjob" if_any ["handjob"] if_not ["naked"]

        attribute noleftarm null
        always "amy_bj_leftarm" if_not ["handjob"]
        always "amy_bj_leftarm" if_all ["handjob", "noleftarm"]
        always "amy_bj_leftarm_handjob" if_any ["handjob"] if_not ["noleftarm"]
        group sleeve auto variant "left" if_not ["naked", "handjob"]
        group sleeve auto variant "left" if_all ["handjob", "noleftarm"] if_not ["naked"]
        group sleeve auto variant "left_handjob" if_any ["handjob"] if_not ["naked", "noleftarm"]


        group head auto:
            attribute up default
        group nose auto


        group mouth auto variant "up" if_any ["up"]:
            attribute mouthlust default
        group mouth auto variant "down" if_any ["down"] if_not ["blow"]:
            attribute mouthlust default
        attribute mouthcum null
        group mouthcum auto variant "up" if_all ["mouthcum", "up"]
        group mouthcum auto variant "down" if_all ["mouthcum", "down"] if_not ["blow"]


        group eyes auto variant "up" if_any ["up"]:
            attribute eyeslust default
        group eyes auto variant "down" if_any ["down"]:
            attribute eyeslust default


        group acc_head auto variant "up" if_any ["up"] if_not ["naked"]
        group acc_head auto variant "down" if_any ["down"] if_not ["naked"]
        attribute facecum null
        group facecum auto if_any ["facecum"]


        group dick auto if_not ["handjob"]
        group dick auto variant "handjob" if_any ["handjob"]


        attribute blow null
        group blow auto if_all ["blow", "down"] if_not ["handjob"]:
            attribute gentle default


        attribute cum null
        group cum auto if_any ["cum"] if_not ["handjob", "blow"]
        group cum auto variant "handjob" if_all ["cum", "handjob"] if_not ["noleftarm"]
        group cum auto variant "handjob_noleftarm" if_all ["cum", "handjob", "noleftarm"]
        always "amy_bj_cum_blow_hard" if_all ["cum", "blow", "hard", "down"] if_not ["handjob"]


        group outfit auto variant "detail" if_not ["naked", "handjob"]
        always "amy_bj_leftarm_fingers" if_any ["handjob"] if_not ["noleftarm"]



    layeredimage amy missionary:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=amy)


        group bg auto:
            attribute bedroom default


        always "amy_missionary_amy"


        attribute collar


        group multiple auto variant piercings


        group exp auto:
            attribute normal default


        group fg auto


        group leg auto:
            attribute spread default


        attribute pubes null
        group pubes auto if_any ["pubes"]


        group multiple auto variant piercings_spread when spread
        group multiple auto variant piercings_lock when lock


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute buttplug null
        group buttplug auto if_any ["buttplug"] if_not ["anal"]


        group hole:
            attribute mike null
            attribute finger null
            attribute openpussy null
        group finger auto if_all ["finger", "lock"] if_not ["mike"]:
            attribute finger1 default
        attribute openpussy if_any ["lock"] if_not ["mike"]


        always "amy_missionary_dripcum" if_all ["openpussy", "cum", "vaginal"] if_not ["mike"]
        attribute bodycum if_any ["spread"]


        group dick:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group out auto variant "spread" if_all ["mike", "out", "spread"]
        group vaginal auto if_all ["mike", "vaginal"]
        group anal auto if_all ["mike", "anal"]


        attribute condom null
        group condom_out auto variant "spread" if_all ["mike", "condom", "out", "spread"] if_not ["cum"]
        group condom auto variant "spread" if_all ["mike", "condom", "spread"] if_not ["cum"]
        group condom auto variant "lock" if_all ["mike", "condom", "lock"] if_not ["cum"]
        group condom_cum auto variant "spread" if_all ["mike", "condom", "cum", "out", "spread"]


        attribute cum null
        group cum_out auto variant "spread" if_all ["mike", "cum", "out", "spread"] if_not ["condom"]
        group cum auto variant "spread" if_all ["mike", "cum", "spread"] if_not ["condom"]
        group cum auto variant "lock" if_all ["mike", "cum", "lock"] if_not ["condom"]


        group mike auto if_any ["mike"]


        group light auto

    layeredimage amy doggy:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker, CollarPicker, PubesPicker], npc=amy)


        group bg auto:
            attribute bedroom default


        attribute nomc null
        always "amy_doggy_mikehead" if_not ["nomc", "finger"]


        always "amy_doggy_amy"
        attribute pubes
        always "amy_doggy_mikehand" if_not ["finger", "grab", "nomc"]
        attribute pregnant


        group puss auto:
            attribute closedpussy null default


        group head auto:
            attribute lookdown default
        group exp auto variant "lookdown" if_any ["lookdown"]:
            attribute normal default
        group exp auto variant "lookup" if_any ["lookup"]:
            attribute normal default


        attribute collar null
        group collar auto if_any ["collar"]


        group multiple auto variant piercings_lookdown when lookdown
        group multiple auto variant piercings_lookup when lookup
        group multiple auto variant piercings


        always "amy_doggy_asshole" if_any ["buttplug", "assgap"] if_not ["anal"]
        attribute assgap null
        attribute buttplug null
        group buttplug auto if_any ["buttplug"]:
            attribute plugin default


        attribute beads null
        group beads auto if_any ["beads"] if_not ["vaginal"]:
            attribute beads1 default


        group dick:
            attribute finger null
            attribute out null default
            attribute vaginal null
            attribute anal null
        group finger auto if_any ["finger"] if_not ["nomc"]:
            attribute fingerdown default
        group mike auto if_any ["out", "vaginal", "anal"] if_not ["nomc"]:
            attribute ease default
        group out auto if_any ["out"] if_not ["trust", "nomc"]
        group vaginal auto if_any ["vaginal"] if_not ["nomc"]
        group anal auto if_any ["anal"] if_not ["nomc"]


        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cum", "nomc"]
        group condom auto variant "vaginal" if_all ["vaginal", "condom"] if_not ["nomc"]
        group condom_cum auto if_all ["out", "condom", "cum"] if_not ["nomc"]


        attribute cum null
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom", "nomc"]
        group cum auto variant "vaginal" if_all ["vaginal", "cum"] if_not ["condom", "nomc"]
        group cum auto variant "anal" if_all ["anal", "cum"] if_not ["nomc"]
        attribute squirt null
        group squirt auto if_any ["squirt"]


        group boobs auto:
            attribute down default
        group multiple auto variant piercings_nipples when nipples


        attribute speed if_any ["vaginal", "anal"]
        attribute screencum


        always "amy_doggy_light" if_not ["cemetery"]

    layeredimage amy cowgirl:
        zoom 1.07 xoffset 40 yoffset 27
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker], npc=amy)


        group bg auto:
            attribute bedroom default


        always "amy_cowgirl_mike"


        group lower auto
        group pregnant auto if_any ["pregnant"]
        group upper auto
        group head auto:
            attribute up default


        group exp auto variant "up" if_any ["up"]:
            attribute normal default
        group exp auto variant "down" if_any ["down"]:
            attribute normal default


        attribute halloween null
        group wig_halloween auto if_any ["halloween"]


        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_down when down


        attribute speed null
        group speed auto if_any ["speed"]


        attribute mikehand


        attribute bodycum


        group dick:
            attribute out null default
            attribute anal null
            attribute vaginal null
        group out auto if_any ["out"]
        group anal auto if_any ["anal"]
        group vaginal auto if_any ["vaginal"]


        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cum"]
        group condom_cum auto variant "out" if_all ["out", "condom", "cum"]


        attribute cum null
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom"]
        group cum auto variant "up" if_all ["up", "cum"] if_not ["condom"]
        group cum auto variant "down" if_all ["down", "cum"] if_not ["condom"]

    layeredimage amy ending:
        attribute_function Pickers([EndingKidPicker], npc=amy)


        always "amy_ending_bg"
        always "amy_ending_mike"


        attribute kid null
        always "amy_ending_daughter" when kid
        always "amy_ending_amyhand" when not kid


        always "amy_ending_amy"


        always "amy_ending_head2" when kid
        always "amy_ending_head1" when not kid

    layeredimage amy kneeling:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker], npc=amy)

        attribute naked null


        always "amy_kneeling_bg"
        always "amy_kneeling_mike"


        always "amy_kneeling_short"
        always "amy_kneeling_amy"
        attribute pregnant


        always "amy_kneeling_hand" if_not ["leash"]
        always "amy_kneeling_hand_leash" if_any ["leash"]


        attribute clit null
        attribute navel null
        group multiple auto variant piercings
        group multiple auto variant piercings_naked when naked


        always "amy_kneeling_outfit" if_not ["naked"]


        always "amy_kneeling_arm_normal" if_not ["pat"]
        always "amy_kneeling_tshirt" if_not ["naked"]
        attribute pat
        always "amy_kneeling_tshirt_shoulder" if_not ["naked"]
        attribute leash

    layeredimage amy stand:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker], npc=amy)

        attribute insert null
        attribute mike null


        group main_bg auto:
            attribute bedroom1 default


        always:
            if_all "insert"
            "amy_stand_insert_bg"

        always:
            if_all "insert"
            "amy_stand_insert_dick"

        group insert auto:
            attribute condom
            attribute cum


        always "amy_stand_main_mikemc" if_any ["mike"]


        always "amy_stand_main_amy"
        attribute pregnant null
        always "amy_stand_main_pregnant" when pregnant


        group main_mhands auto if_any ["mike"]:
            attribute butt default



        group main_boobs auto:
            attribute up
            attribute down default


        attribute collar null
        always "amy_stand_main_collar" when collar


        attribute blush null
        always "amy_stand_main_blush" if_any ["blush"]

        group main_aeyes auto:
            attribute pleasure default

        group main_amouth auto:
            attribute opened default


        attribute clit null
        attribute nose null
        attribute nipples null
        group main_piercings auto variant "nipples"


        always "amy_stand_main_ponytails" if_not ["hair"]


        group multiple auto variant main_fx


        always "amy_stand_main_fg_lights" if_any ["stage"]


    layeredimage fg:
        zoom 0.667

        attribute dreamy

init -35 python:
    amy_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'embarrassed', 'flirt', 'grumpy', 'guilty', 'happy', 'lying', 'mad', 'mindless', 'pain', 'pout', 'puzzled', 'sad', 'sadsmile', 'shy', 'stuned', 'surprised', 'upset', 'whining', 'worried'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'work', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'noacc'],
}

    def amy_anim_filter(attrs, anim_dict=amy_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker], npc=amy)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        pwet_pickers_attrs = Pickers([PositionPicker], npc=amy)(set(attrs))
        attrs.extend(pwet_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=amy)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['maid', 'sluttydate', 'sport', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['work']:
            attr_acc_body = "acc_body_" + ("pierced_" if 'nipples' in mult_attrs['piercings'][0] else "") + sgl_attrs['outfits'][0]
        else:
            attr_acc_body = None
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc_body, attr_acc_head)


    def amy_close_anim_filter(attrs, anim_dict=amy_attrs):
        return amy_anim_filter(attrs, anim_dict)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
