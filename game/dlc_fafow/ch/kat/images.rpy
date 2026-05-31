init 1:
    layeredimage kat smartphone:
        always "kat_smartphone"

    layeredimage kat kiss:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker], npc=kat)


        always "kat_kiss_bodies"


        group mikeoutfit auto if_not ["naked"]:
            attribute normal default


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null


        attribute naked null
        attribute topless null
        group outfit auto when not (naked or topless)


        attribute haircut


        attribute collar

    layeredimage streaming:


        group capture auto



        group body auto if_not ["sex"]:
            attribute stream default
            attribute cam


        group exp auto variant "cam" if_any ["cam"] if_not ["sex"]:
            attribute normal default
        group exp auto variant "stream" if_any ["stream"] if_not ["sex"]:
            attribute normal default


        always "streaming_haircut" if_any ["cam"]


        attribute interface_fg




    layeredimage kat mast:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PubesPicker], npc=kat)

        attribute squirt null


        always "kat_mast_image"
        always "kat_mast_bg"


        attribute haircut


        attribute collar


        group multiple auto variant piercings




        group eyes auto:
            attribute eyes_open default
        group mouths auto:
            attribute mouth_normal default


        group squirt if_any ["squirt"] if_not ["finger", "rub"]:
            attribute vibrator


        attribute vibrator if_not ["finger", "rub"]
        attribute speed if_any ["vibrator"] if_not ["finger", "rub"]


        group hand:
            attribute rest


        attribute pubes


        group hand:
            attribute normal default
            attribute rub
            attribute finger


        group squirt if_any ["squirt"]:
            attribute rub
            attribute finger


        attribute shake

    layeredimage kat missionary:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "kat_missionary_body"


        attribute bodycum


        attribute collar
        attribute pregnant
        group multiple auto variant piercings
        attribute pubes


        attribute vaginaldrip
        attribute analdrip


        attribute speed


        group eyes auto:
            attribute eyes_normal default
        group mouth auto:
            attribute mouth_normal default
        attribute tongueout if_any ["mouth_normal"]


        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group depth:
            attribute tip null default
            attribute full null


        group anal auto if_all ["mike", "anal"]
        group vaginal auto if_all ["mike", "vaginal"]


        attribute condom null
        group condom auto variant "vaginal" if_all ["mike", "vaginal", "condom"]


        attribute cum null
        group cum auto if_all ["mike", "cum", "full"] if_not ["condom"]


        always "kat_missionary_mikehand" if_any ["mike"] if_not ["pinch"]
        attribute pinch


        group out auto if_all ["mike", "out"]


        group condom auto variant "out" if_all ["mike", "out", "condom"] if_not ["cum"]
        group condomcum auto variant "out" if_all ["mike", "out", "condom", "cum"]


        group cum auto variant "out" if_all ["mike", "out", "cum"] if_not ["condom"]


        attribute mike


        group light auto

    layeredimage kat cowgirl:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "kat_cowgirl_base"


        attribute bodycum


        attribute pubes
        attribute pregnant
        attribute collar
        group multiple auto variant piercings


        group kateyes auto:
            attribute eyes_open default


        group katmouth auto:
            attribute mouth_open default
        attribute tongueout if_any ["mouth_open"]


        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group dick auto
        group dick auto variant "out" if_all ["out"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]
        group condom_cum auto variant "out" if_all ["condom", "out", "cum"]


        group dickcum:
            attribute dickcum_ass null
            attribute dickcum_pussy null
        group dickcum_ass auto variant "out" if_all ["out","dickcum_ass"] if_not ["condom"]
        group dickcum_pussy auto variant "out" if_all ["out","dickcum_pussy"] if_not ["condom"]

    layeredimage kat doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker], npc=kat)

        group bg auto:
            attribute bedroom default

        attribute mike
        always "kat_doggy_mike_outfit" if_all ["mike"] if_not ["naked", "halloween"]
        always "kat_doggy_katbody"

        attribute collar

        attribute speed
        attribute cum if_all ["mike"]

        group kat_outfit if_not ["naked"]:
            attribute casual

        attribute pregnant

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute tongue null

        always "kat_doggy_mikehand_left" if_all ["mike"] if_not ["up", "halloween"]
        always "kat_doggy_mikehand_left" if_all ["mike", "halloween", "naked"] if_not ["up"]
        always "kat_doggy_mikehand_right" if_all ["mike"]
        always "kat_doggy_mikehand_left_outfit" if_all ["mike"] if_not ["naked", "halloween"]
        always "kat_doggy_mikehand_right_outfit" if_all ["mike"] if_not ["naked", "halloween"]

        attribute naked null

        group kathand auto if_not ["halloween"]:
            attribute down default
        group kathand auto if_all ["halloween", "naked"]:
            attribute down default
        group kathand_up_outfit auto if_any ["up"] if_not ["naked"]
        group kathand_down_outfit if_any ["down"] if_not ["naked"]:
            attribute casual

        group kat_outfit if_not ["pregnant", "naked"]:
            attribute halloween
        group kat_outfit_pregnant if_any ["pregnant"] if_not ["naked"]:
            attribute halloween

        always "kat_doggy_mikehand_halloween_left" if_all ["mike", "halloween"] if_not ["up", "naked"]

        group kathand_down_outfit if_any ["down"] if_not ["naked"]:
            attribute halloween

        always "kat_doggy_mikehand_up" if_all ["mike", "up"]

        attribute arcade

        group kateyes auto:
            attribute eyes_open default

        group katmouth auto:
            attribute mouth_open default

        attribute tongueout if_any ["mouth_open"]


        attribute haircut



    layeredimage kat blowjob:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, OutfitPicker], npc=kat)

        attribute no_people null


        group bg auto:
            attribute bedroom default


        group dick auto if_not ["no_people"]


        attribute naked null
        always "kat_blowjob_mike" if_not ["no_people"]
        always "kat_blowjob_mikeoutfit" if_not ["naked", "no_people"]


        attribute handjob null
        group handjob auto if_all ["out", "handjob"] if_not ["no_people"]:
            attribute back default
        group sleeves_handjob auto variant "back" if_all ["out", "handjob", "back"] if_not ["topless", "naked", "no_people"]
        group sleeves_handjob auto variant "forth" if_all ["out", "handjob", "forth"] if_not ["topless", "naked", "no_people"]
        group hand auto if_not ["handjob", "no_people"]
        group sleeves auto variant "out" if_any ["out"] if_not ["handjob", "topless", "naked", "no_people"]


        group kat auto if_not ["no_people"]:
            attribute out default


        group multiple auto variant piercings_out when out and not no_people
        group multiple auto variant piercings_blow when blow and not no_people


        attribute collar null
        group collar auto if_any ["collar"] if_not ["no_people"]


        attribute bottomless null
        group bot auto variant "out" if_any ["out"] if_not ["bottomless", "naked", "no_people"]
        group bot auto variant "blow" if_any ["blow"] if_not ["bottomless", "naked", "no_people"]
        attribute topless null
        group top auto variant "out" if_any ["out"] if_not ["topless", "naked", "no_people"]
        group top auto variant "blow" if_any ["blow"] if_not ["topless", "naked", "no_people"]


        group tongues auto if_all ["out", "mouth_lick"] if_not ["no_people"]:
            attribute tongue1 default
        group mouth auto variant "out" if_any ["out"] if_not ["no_people"]:
            attribute mouth_normal null default
        group eyes auto variant "out" if_any ["out"] if_not ["no_people"]:
            attribute eyes_open default
        group eyes auto variant "blow" if_any ["blow"] if_not ["no_people"]:
            attribute eyes_open default


        attribute cum null
        group cum auto if_any ["cum"] if_not ["no_people"]
        group cum auto variant "out" if_all ["out", "cum"] if_not ["no_people"]
        attribute facecum


        attribute breath null
        group breath auto if_any ["breath"] if_not {'no_people'}


        attribute curtain null
        attribute shadows null
        group curtain auto if_any ["curtain"]
        group curtain auto variant "shadows" if_all ["curtain", "shadows"]

    layeredimage kat cunnilingus:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, OutfitPicker, MCCGPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        attribute no_chair null
        group chair auto when not no_chair


        always "kat_cunnilingus_kat"
        attribute pregnant


        attribute collar when date or naked

        group multiple auto variant piercings
        attribute ears null
        attribute tongue null

        attribute pubes


        group eyes auto:
            attribute eyes_open default
        group mouth auto:
            attribute mouth_open default


        attribute naked null
        group outfit auto when not (naked or pregnant)
        group outfit auto variant pregnant when pregnant and not naked
        attribute collar when sexydate


        group leftarm:
            attribute normal default
        group sleeve_leftarm auto variant normal when normal and not naked


        attribute mike null
        group tongue auto when mike:
            attribute tongue1 default
        attribute mikemc when mike
        group mikeoutfit auto when mike and not naked


        group tableleg auto when no_table


        group leftarm when mike:
            attribute hold
        group sleeve_leftarm auto variant hold when hold and mike and not naked


        attribute spoon when restaurant and not no_table
        always "kat_cunnilingus_rightarm"
        group sleeve_rightarm auto variant spoon when spoon and not naked
        group sleeve_rightarm auto variant nospoon when not (spoon or naked)


        attribute vibrator null
        group vibrator auto when vibrator:
            attribute turnoff default


        attribute no_table null
        always "kat_cunnilingus_table" when restaurant and not no_table
        attribute bowl when restaurant and not no_table


        attribute remote when vibrator and not mike

    layeredimage kat mask:
        always "kat_mask_fx"

    layeredimage katjack bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "katjack_bj_kat"


        attribute pregnant


        group head auto:
            attribute normal default


        attribute clit null
        attribute ears null
        attribute navel null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_suckjack when suckjack
        group multiple auto variant piercings_suckmike when suckmike


        attribute collar null
        group collar auto if_any ["collar"]


        attribute haircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_not ["haircut"]


        attribute mouthcum if_any ["normal"]
        attribute facecum if_any ["normal"]
        attribute bodycum


        always "katjack_bj_mikedick"


        attribute suckmike


        attribute mikecum null
        group mikecum auto if_any ["mikecum"]


        group lefthands auto:
            attribute lefthand_back default


        always "katjack_bj_mike"


        always "katjack_bj_jackdick"


        attribute suckjack


        attribute jackcum null
        group jackcum auto if_any ["jackcum"]


        group righthands auto:
            attribute righthand_back default


        always "katjack_bj_jack"

    layeredimage katjack doublepen:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        group backmale auto


        always "katjack_doublepen_top"


        attribute pregnant


        group multiple auto variant piercings_top


        always "katjack_doublepen_bot"


        attribute pubes


        group multiple auto variant piercings_bot


        group head auto:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_orgasm when orgasm


        attribute collar null
        group collar auto if_any ["collar"]


        attribute blush if_any ["normal"]


        group eyes auto if_any ["normal"]:
            attribute open default
        group mouths auto if_any ["normal"]:
            attribute smile default


        attribute haircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_not ["haircut"]


        group frontmale:
            attribute mikefront


        group mikefront_pose:
            attribute mikeout null default
            attribute mikevaginal null
        group mikefront_dick auto if_all ["mikefront"]
        group mikefront_dick_mikeout auto if_all ["mikefront", "mikeout"]


        group jackfront_pose:
            attribute jackout null default
            attribute jackvaginal null
        group jackfront_dick auto if_all ["jackfront"]


        group mikeback_pose:
            attribute mikeout null default
            attribute mikeanal null
        group mikeback_dick auto if_all ["mikeback"]
        group mikeback_dick_mikeout auto if_all ["mikeback", "mikeout"]


        group jackback_pose:
            attribute jackout null default
            attribute jackanal null
        group jackback_dick auto if_all ["jackback"]


        attribute mikecondom null
        group mikefront_condom auto if_all ["mikefront", "mikecondom"]
        group mikefront_condom_mikeout auto if_all ["mikefront", "mikecondom", "mikeout"]
        group mikeback_condom auto if_all ["mikeback", "mikecondom"]
        group mikeback_condom_mikeout auto if_all ["mikeback", "mikecondom", "mikeout"]


        attribute jackcondom null
        group jackfront_condom auto if_all ["jackfront", "jackcondom"]
        group jackback_condom auto if_all ["jackback", "jackcondom"]


        attribute mikecum null
        group mikefront_cum auto if_all ["mikefront", "mikecum"] if_not ["mikecondom"]
        group mikefront_cum_mikeout auto if_all ["mikefront", "mikecum", "mikeout"] if_not ["mikecondom"]
        group mikeback_cum auto if_all ["mikeback", "mikecum"] if_not ["mikecondom"]
        group mikeback_cum_mikeout auto if_all ["mikeback", "mikecum", "mikeout"] if_not ["mikecondom"]


        attribute jackcum null
        group jackfront_cum auto if_all ["jackfront", "jackcum"] if_not ["jackcondom"]
        group jackback_cum auto if_all ["jackback", "jackcum"] if_not ["jackcondom"]


        group frontmale:
            attribute jackfront

    layeredimage katjack foreplay:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "katjack_foreplay_bodies"


        attribute pregnant


        attribute pubes


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute tongue null


        group finger auto:
            attribute down default


        attribute squirt null
        group squirt auto if_any ["squirt"]


        attribute haircut null
        group haircut auto if_any ["haircut"]:
            attribute normal default
        group nohaircut auto if_not ["nohaircut"]:
            attribute normal default


        attribute nose if_any ["normal"]


        attribute collar null
        group collar auto if_any ["collar"]


        group eyes auto:
            attribute closed default
        group mouths auto:
            attribute shy default

    layeredimage katjack jackfuck:
        attribute_function Pickers([PiercingsPicker, DickPicker, PregnancyPicker, PubesPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "katjack_jackfuck_bodies"


        attribute pregnant


        attribute pubes


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute nipples null
            attribute tongue null


        attribute bodycum


        group eyes auto:
            attribute closed default


        always "katjack_jackfuck_nohaircut" if_not ["haircut"]
        attribute haircut


        group mikedick auto:
            attribute mikeoutside null default
        group mikedick auto variant "mikeoutside" if_any ["mikeoutside"]


        attribute mikecondom null
        group mikecondom auto if_any ["mikecondom"]
        group mikecondom auto variant "mikeoutside" if_all ["mikecondom", "mikeoutside"]


        attribute mikecum null
        group mikecum auto if_any ["mikecum"] if_not ["mikecondom"]
        group mikecum auto variant "mikeoutside" if_all ["mikecum", "mikeoutside"] if_not ["mikecondom"]


        attribute mikedickcum null
        group mikedickcum auto if_all ["mikedickcum", "mikeoutside"] if_not ["mikecondom"]


        attribute shake


        attribute jack


        group jackdick auto if_any ["jack"]:
            attribute jackoutside default


        attribute jackcum null
        group jackcum auto if_all ["jack", "jackcum"]


        always "katjack_jackfuck_jackhand" if_any ["jack"]

    layeredimage katjack mikefuck:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, DickPicker, XrayPicker], npc=kat)


        group bg auto:
            attribute bedroom default


        always "katjack_mikefuck_kat"


        attribute collar


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute tongue null


        attribute top_bodycum
        attribute bot_bodycum


        group eyes auto:
            attribute normal default


        always "katjack_mikefuck_nohaircut" if_not ["haircut"]
        attribute haircut


        always "katjack_mikefuck_mouths_open" if_any ["suck"] if_not ["jack"]
        group mouths auto:
            attribute open default
            attribute suck null


        group jackdick auto if_any ["jack"]


        attribute jackcum null
        group jackcum auto if_all ["jack", "jackcum"]


        attribute jack


        attribute mike


        attribute pregnant
        attribute pregnant_navel


        group mikedick:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group mikedick auto variant "out" if_all ["mike", "out"]


        attribute mikecondom null
        group mikecondom auto variant "out" if_all ["mike", "out", "mikecondom"]


        attribute mikecum null
        group mikecum auto variant "out" if_all ["mike", "out", "mikecum"] if_not ["mikecondom"]


        attribute xray if_all ["mike", "vaginal"]
        always "katjack_mikefuck_xray_mikecum" if_all ["mike", "vaginal", "xray", "mikecum"]

    layeredimage kat ending:
        attribute_function Pickers([EndingKidPicker], npc=kat)
        attribute kid null
        always "kat_ending_pregnant" when kid
        always "kat_ending_base" when not kid

    layeredimage katjack ending:
        attribute_function Pickers([EndingKidPicker], npc=kat)
        always "katjack_ending_bg"
        always "katjack_ending_jack"
        always "katjack_ending_mike"
        attribute kid null
        always "katjack_ending_girl" when kid
        always "katjack_ending_boy" when not kid
        attribute kat
        always "katjack_ending_fg"

init -35 python:
    kat_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c', 'd'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'afraid', 'angry', 'annoyed', 'busted', 'confused', 'crazy', 'defiant', 'enthusiastic', 'happy', 'mindless', 'normal', 'offended', 'sad', 'sadclosed', 'sadsmile', 'shocked', 'shy', 'smile', 'smileclosed', 'stuned', 'surprised', 'talkative', 'timid', 'upset', 'whinge', 'whining', 'yawn'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'noacc', 'headphones'],
}

    def kat_anim_filter(attrs, anim_dict=kat_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PubesPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PositionPicker], npc=kat)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=kat)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_acc_head = None
        if 'noacc' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['halloween', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        
        
        attr_headphones = None
        if 'headphones' in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['casual']:
            attr_headphones = "headphones_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_hand = None
        if 'noacc' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sexydate']:
            attr_acc_hand = "acc_hand_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['wedding']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_body = None
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['date']:
            attr_acc_body = "acc_body_" + sgl_attrs['outfits'][0]
        
        
        attr_stockings = None
        if 'bottomless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_stockings = "stockings_" + sgl_attrs['outfits'][0]
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_stockings, attr_acc_body, attr_necklace, attr_acc_hand, attr_headphones, attr_acc_head)


    def kat_close_anim_filter(attrs, anim_dict=kat_attrs):
        return kat_anim_filter(attrs, anim_dict)

label test_kat_exps:
    $ pose = 'a'

    $ renpy.show(f"kat {pose} afraid")
    show expression f"kat {pose} afraid" as k2 at left
    "afraid"

    $ renpy.show(f"kat {pose} angry")
    show expression f"kat {pose} angry" as k2 at left
    "angry"

    $ renpy.show(f"kat {pose} annoyed")
    show expression f"kat {pose} annoyed" as k2 at left
    "annoyed"

    $ renpy.show(f"kat {pose} busted")
    show expression f"kat {pose} busted" as k2 at left
    "busted"

    $ renpy.show(f"kat {pose} confused")
    show expression f"kat {pose} confused" as k2 at left
    "confused"

    $ renpy.show(f"kat {pose} crazy")
    show expression f"kat {pose} crazy" as k2 at left
    "crazy"

    $ renpy.show(f"kat {pose} defiant")
    show expression f"kat {pose} defiant" as k2 at left
    "defiant"

    $ renpy.show(f"kat {pose} enthusiastic")
    show expression f"kat {pose} enthusiastic" as k2 at left
    "enthusiastic"

    $ renpy.show(f"kat {pose} happy")
    show expression f"kat {pose} happy" as k2 at left
    "happy"

    $ renpy.show(f"kat {pose} mindless")
    show expression f"kat {pose} mindless" as k2 at left
    "mindless"

    $ renpy.show(f"kat {pose} normal")
    show expression f"kat {pose} normal" as k2 at left
    "normal"

    $ renpy.show(f"kat {pose} offended")
    show expression f"kat {pose} offended" as k2 at left
    "offended"

    $ renpy.show(f"kat {pose} sad")
    show expression f"kat {pose} sad" as k2 at left
    "sad"

    $ renpy.show(f"kat {pose} sadclosed")
    show expression f"kat {pose} sadclosed" as k2 at left
    "sadclosed"

    $ renpy.show(f"kat {pose} sadsmile")
    show expression f"kat {pose} sadsmile" as k2 at left
    "sadsmile"

    $ renpy.show(f"kat {pose} shocked")
    show expression f"kat {pose} shocked" as k2 at left
    "shocked"

    $ renpy.show(f"kat {pose} shy")
    show expression f"kat {pose} shy" as k2 at left
    "shy"

    $ renpy.show(f"kat {pose} smile")
    show expression f"kat {pose} smile" as k2 at left
    "smile"

    $ renpy.show(f"kat {pose} smileclosed")
    show expression f"kat {pose} smileclosed" as k2 at left
    "smileclosed"

    $ renpy.show(f"kat {pose} stuned")
    show expression f"kat {pose} stuned" as k2 at left
    "stuned"

    $ renpy.show(f"kat {pose} surprised")
    show expression f"kat {pose} surprised" as k2 at left
    "surprised"

    $ renpy.show(f"kat {pose} talkative")
    show expression f"kat {pose} talkative" as k2 at left
    "talkative"

    $ renpy.show(f"kat {pose} timid")
    show expression f"kat {pose} timid" as k2 at left
    "timid"

    $ renpy.show(f"kat {pose} upset")
    show expression f"kat {pose} upset" as k2 at left
    "upset"

    $ renpy.show(f"kat {pose} whinge")
    show expression f"kat {pose} whinge" as k2 at left
    "whinge"

    $ renpy.show(f"kat {pose} whining")
    show expression f"kat {pose} whining" as k2 at left
    "whining"

    $ renpy.show(f"kat {pose} yawn")
    show expression f"kat {pose} yawn" as k2 at left
    "yawn"

    return

label test_kat_outfits:
    $ kat.flags.sexyswimsuit = False
    $ kat.flags.sexydate = False
    $ kat.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"kat a casual{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b casual{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c casual{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d casual{pregnancy}", tag="k4", at_list=[mostright4])
        "casual"

        $ renpy.show(f"kat a date{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b date{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c date{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d date{pregnancy}", tag="k4", at_list=[mostright4])
        "date"

        $ renpy.show(f"kat a halloween{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b halloween{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c halloween{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d halloween{pregnancy}", tag="k4", at_list=[mostright4])
        "halloween"

        $ renpy.show(f"kat a sexydate{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b sexydate{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c sexydate{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d sexydate{pregnancy}", tag="k4", at_list=[mostright4])
        "sexydate"

        $ renpy.show(f"kat a sexyswimsuit{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b sexyswimsuit{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c sexyswimsuit{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d sexyswimsuit{pregnancy}", tag="k4", at_list=[mostright4])
        "sexyswimsuit"

        $ renpy.show(f"kat a sluttydate{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b sluttydate{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c sluttydate{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d sluttydate{pregnancy}", tag="k4", at_list=[mostright4])
        "sluttydate"

        $ renpy.show(f"kat a sport{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b sport{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c sport{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d sport{pregnancy}", tag="k4", at_list=[mostright4])
        "sport"

        $ renpy.show(f"kat a swimsuit{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b swimsuit{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c swimsuit{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d swimsuit{pregnancy}", tag="k4", at_list=[mostright4])
        "swimsuit"

        $ renpy.show(f"kat a underwear{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b underwear{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c underwear{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d underwear{pregnancy}", tag="k4", at_list=[mostright4])
        "underwear"

        $ renpy.show(f"kat a wedding{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kat b wedding{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kat c wedding{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kat d wedding{pregnancy}", tag="k4", at_list=[mostright4])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
