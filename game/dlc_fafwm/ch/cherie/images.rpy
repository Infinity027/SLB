init 1:
    layeredimage cherie kiss:
        attribute_function Pickers([CollarPicker, PiercingsPicker, HaircutPicker, OutfitPicker, PregnancyPicker], npc=cherie)


        always "cherie_kiss_arm"


        always "cherie_kiss_mbody"


        always "cherie_kiss_cbody"


        attribute pregnant


        attribute naked null
        attribute topless null
        group outfit auto if_not["naked", "topless"]:
            attribute santa "cherie_kiss_outfit_date"
            attribute rpg "cherie_kiss_outfit_date"
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]:
            attribute santa "cherie_kiss_outfit_pregnant_date"
            attribute rpg "cherie_kiss_outfit_pregnant_date"


        attribute collar


        always "cherie_kiss_armmike" if_not ["halloween"]


        group outfitmike auto if_not ["naked"]:
            attribute work "cherie_kiss_outfitmike_date"
            attribute wedding "cherie_kiss_outfitmike_date"
            attribute sexydate "cherie_kiss_outfitmike_date"
            attribute sluttydate "cherie_kiss_outfitmike_date"


        group multiple:
            attribute clit null
            attribute lips null
            attribute nipples null
            attribute nose null
        group multiple auto variant piercings
        group piercings auto variant casual when casual
        group piercings auto variant date when date
        group piercings auto variant sexydate when sexydate
        group piercings auto variant wedding when wedding

        group necklace auto when not collar


        group haircuts auto:
            attribute haircut if_not[ "wedding", "swimsuit"]
            attribute nohaircut if_not ["wedding", "swimsuit"]


        always "cherie_kiss_hairmike" if_not ["santa"]


        always "cherie_kiss_hand"


        always "cherie_kiss_acc_halloween" if_any["halloween"]


        always "cherie_kiss_handmike"

    layeredimage cherie bj:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        group bodies auto


        attribute pregnant


        always "cherie_bj_haircuts_haircut" if_any "haircut" if_not "swimsuit"
        always "cherie_bj_haircuts_haircut_swimsuit" if_all ["haircut", "swimsuit"]


        group ceyes auto:
            attribute open default


        always "cherie_bj_haircuts_nohaircut_front" if_any "nohaircut"


        attribute naked null
        group outfit auto if_not "naked"
        group outfit auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfit auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not "naked"


        group cmouth auto:
            attribute happy default


        attribute clit null
        attribute lips null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings


        attribute collar null
        group collar auto if_any "collar"


        attribute mc_casual null
        group mikeoutfit auto if_not ["naked"]:
            attribute sexyswimsuit "cherie_bj_mikeoutfit_swimsuit"


        always "cherie_bj_hand_back"


        group dickpos:
            attribute suck null
            attribute outside null default
        group dick auto variant "suck" if_any "suck"
        group dick auto variant "outside" if_any "outside"


        always "cherie_bj_hand_front"


        attribute cum null
        always "cherie_bj_cum_inside" if_all ["suck", "cum"]
        group cum auto variant "outside" if_all ["outside", "cum"]

        attribute bodycum


    layeredimage cherie doggy:
        attribute_function Pickers([HaircutPicker, PiercingsPicker, DickPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        group bodies auto
        always "cherie_doggy_haircut_scalp" if_any "haircut"
        always "cherie_doggy_ear" if_any "haircut"


        group exp auto:
            attribute happy default


        attribute naked null
        group outfit auto if_not "naked"
        group outfit auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfit auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"


        attribute haircut
        always "cherie_doggy_haircut_bun" if_any "haircut"
        always "cherie_doggy_haircut_brand" if_any "haircut"


        attribute clit null
        attribute lips null
        attribute navel null
        attribute nose null
        attribute nipples null
        attribute pregnant_navel null
        group multiple auto variant piercings if_any "haircut"

        always "cherie_doggy_anus" if_any "anal"


        group dickpos:
            attribute anal null
            attribute vaginal null
            attribute outside null default
        group dick auto variant "anal" if_any "anal"
        group dick auto variant "vaginal" if_any "vaginal"
        group dick auto variant "outside" if_any "outside"


        attribute condom null
        group condom auto variant "anal" if_all ["condom", "anal"]
        group condom auto variant "vaginal" if_all ["condom", "vaginal"]
        group condom auto variant "outside" if_all ["condom", "outside"]


        attribute cum null
        always "cherie_doggy_cum_anal" if_all ["anal", "cum"]
        always "cherie_doggy_cum_vaginal" if_all ["vaginal", "cum"]
        group cum auto variant "outside" if_all ["outside", "cum"]


        always "cherie_doggy_mike"

        group multiple auto variant bodycum
        group multiple:
            attribute oncherie
            attribute onmike


    layeredimage cherie cowgirl:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        group bodies auto


        attribute pregnant


        group exp auto:
            attribute happy default


        always "cherie_cowgirl_haircut" if_any "haircut" if_not "swimsuit"
        always "cherie_cowgirl_haircut_swimsuit" if_all ["haircut", "swimsuit"]


        attribute lips null
        attribute ears if_not "nohaircut"
        group multiple auto variant piercings


        attribute naked null
        group outfits auto if_not "naked"
        group outfits auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfits auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"
        group outfits auto variant "pregnant" if_any ["pregnant"] if_not "naked"


        attribute collar


        attribute mc_casual null
        group mikeoutfits auto if_not ["naked"]:
            attribute sexyswimsuit "cherie_cowgirl_mikeoutfits_swimsuit"

        group multiple auto variant mikepiercings

        attribute cum

        attribute bodycum


    layeredimage cherie cunnilingus:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        group bodies auto


        group exp auto:
            attribute happy default


        attribute naked null
        group outfits auto if_not "naked"
        group outfits auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfits auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"


        attribute ears if_not "nohaircut"
        attribute clit null
        attribute lips null
        attribute navel null
        attribute nipples null
        attribute pregnant_navel null
        group multiple auto variant piercings


        attribute collar null
        group collar auto if_any "collar"


        attribute mc_casual null
        group mikeoutfits auto if_not ["naked"]:
            attribute sexyswimsuit "cherie_cunnilingus_mikeoutfits_swimsuit"


    layeredimage cherie standing:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        always "cherie_standing_hand"


        always "cherie_standing_mike"


        group bodies auto


        attribute pregnant


        always "cherie_standing_haircut" if_any "haircut" if_not "swimsuit"
        always "cherie_bj_standing_swimsuit" if_all ["haircut", "swimsuit"]


        group exp auto:
            attribute happy default


        always "cherie_standing_haircuts_nohaircut_front" if_any "nohaircut"


        attribute naked null
        group outfits auto if_not "naked"
        group outfits auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfits auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"
        group outfits auto variant "pregnant" if_any ["pregnant"] if_not "naked"


        attribute clit null
        attribute lips null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings


        attribute collar null
        group collar auto if_any "collar"


        attribute mc_casual null
        group mikeoutfits auto if_not ["naked"]:
            attribute sexyswimsuit "cherie_standing_mikeoutfits_swimsuit"



        group dickpos:
            attribute anal null
            attribute vaginal null
            attribute outside null default
        group dick auto variant "anal" if_any "anal"
        group dick auto variant "vaginal" if_any "vaginal"
        group dick auto variant "outside" if_any "outside"


        attribute condom null
        group condom auto variant "anal" if_all ["condom", "anal"]
        group condom auto variant "vaginal" if_all ["condom", "vaginal"]
        group condom auto variant "outside" if_all ["condom", "outside"]


        attribute cum null
        always "cherie_standing_cum_anal" if_all ["anal", "cum"]
        always "cherie_standing_cum_vaginal" if_all ["vaginal", "cum"]
        group cum auto variant "outside" if_all ["outside", "cum"]

        group bodycum:
            attribute onsex if_all ["bodycum"] if_any ["anal", "vaginal"]
            attribute outside if_all ["outside", "bodycum"]


    layeredimage cherie reverse:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, PubesPicker, DickPicker], npc=cherie)


        group bg auto:
            attribute bedroom default


        always "cherie_reverse_mike_body"


        always "cherie_reverse_bodies_haircut" if_any "haircut"
        always "cherie_reverse_bodies_nohaircut" if_any "nohaircut" if_not "swimsuit"
        always "cherie_reverse_bodies_nohaircut_swimsuit" if_all ["nohaircut", "swimsuit"]


        always "cherie_reverse_novaginal" if_not "vaginal"


        attribute dickbump null
        group dick auto if_any ["dickbump"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute pubes


        always "cherie_reverse_haircut" if_any "haircut" if_not "swimsuit"
        always "cherie_reverse_haircut_swimsuit" if_all ["haircut", "swimsuit"]


        group exp auto:
            attribute happy default


        always "cherie_reverse_nohaircut_brand" if_any "nohaircut"


        attribute ears if_not "nohaircut"
        attribute lips null
        group multiple auto variant piercings


        attribute naked null
        group outfits auto if_not "naked"
        group outfits auto variant "haircut" if_any ["haircut"] if_not "naked"
        group outfits auto variant "nohaircut" if_any ["nohaircut"] if_not "naked"
        group outfits auto variant "pregnant" if_any ["pregnant"] if_not "naked"


        always "cherie_reverse_mike"


        attribute mc_casual null
        group mikeoutfits auto if_not ["naked"]:
            attribute sexyswimsuit "cherie_reverse_mikeoutfits_swimsuit"


        group dickpos:
            attribute anal null
            attribute vaginal null
            attribute outside null default
        group dick auto variant "anal" if_any "anal"
        group dick auto variant "vaginal" if_any "vaginal"
        group dick auto variant "outside" if_any "outside"


        attribute condom null
        group condom auto variant "anal" if_all ["condom", "anal"]
        group condom auto variant "vaginal" if_all ["condom", "vaginal"]
        group condom auto variant "outside" if_all ["condom", "outside"]


        attribute cum null
        always "cherie_reverse_cum_anal" if_all ["anal", "cum"]
        always "cherie_reverse_cum_vaginal" if_all ["vaginal", "cum"]
        group cum auto variant "outside" if_all ["outside", "cum"]

        attribute bodycum


        always "cherie_reverse_hand"


    layeredimage cherie ending:
        attribute_function Pickers([EndingKidPicker], npc=cherie)

        always "cherie_ending_bg"

        always "cherie_ending_cherie"

        always "cherie_ending_desk"

        always "cherie_ending_mike"

        attribute kid

        always "cherie_ending_fg"



init -35 python:
    cherie_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c'],
    'piercings': ['clit', 'ears', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'amused', 'angry', 'annoyed', 'closed', 'cry', 'flirt', 'happy', 'mindless', 'sad', 'sadsmile', 'smile', 'stuned', 'surprised', 'talkative', 'upset', 'whining', 'wink'],
    'outfits': ['casual', 'work', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'funeral', 'wedding', 'underwear', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'chainless', 'noglasses'],
}

    def cherie_anim_filter(attrs, anim_dict=cherie_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, HaircutPicker, PositionPicker], npc=cherie)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        attr_hair = 'hair_appear'
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=cherie)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_acc = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date', 'swimsuit']:
            attr_acc = "acc_" + sgl_attrs['outfits'][0]
        
        
        attr_glasses = None
        if not any(attr in mult_attrs['others'][0] for attr in ('noglasses', 'topless')) and sgl_attrs['outfits'][0] == 'funeral':
            attr_glasses = "glasses_" + sgl_attrs['outfits'][0]
        
        
        attr_hat = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['funeral', 'halloween', 'swimsuit', 'wedding']:
            attr_hat = "hat_" + sgl_attrs['outfits'][0]
            if sgl_attrs['outfits'][0] in ['funeral', 'swimsuit']:
                attr_hair = None
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date', 'sexydate', 'sluttydate', 'wedding']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_chains = None
        if not any(attr in mult_attrs['others'][0] for attr in ('chainless', 'bottomless', 'topless')) and sgl_attrs['outfits'][0] == 'sexyswimsuit':
            attr_chains = "chains_" + sgl_attrs['outfits'][0]
        
        
        attr_gloves = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['funeral', 'wedding']:
            attr_gloves = "gloves_" + sgl_attrs['outfits'][0]
        
        
        poking = None
        if 'nipples' in mult_attrs['piercings'][0] and 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] != 'naked':
            poking = "poking"
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_gloves, attr_chains, attr_necklace, attr_hat, attr_glasses, attr_acc, attr_hair, poking)


    def cherie_close_anim_filter(attrs, anim_dict=cherie_attrs):
        return cherie_anim_filter(attrs, anim_dict)

label test_cherie_exps:
    $ pose = 'a'

    $ renpy.show(f"cherie {pose} amused")
    show expression f"cherie {pose} amused" as c2 at left
    "amused"

    $ renpy.show(f"cherie {pose} angry")
    show expression f"cherie {pose} angry" as c2 at left
    "angry"

    $ renpy.show(f"cherie {pose} annoyed")
    show expression f"cherie {pose} annoyed" as c2 at left
    "annoyed"

    $ renpy.show(f"cherie {pose} closed")
    show expression f"cherie {pose} closed" as c2 at left
    "closed"

    $ renpy.show(f"cherie {pose} cry")
    show expression f"cherie {pose} cry" as c2 at left
    "cry"

    $ renpy.show(f"cherie {pose} flirt")
    show expression f"cherie {pose} flirt" as c2 at left
    "flirt"

    $ renpy.show(f"cherie {pose} happy")
    show expression f"cherie {pose} happy" as c2 at left
    "happy"

    $ renpy.show(f"cherie {pose} mindless")
    show expression f"cherie {pose} mindless" as c2 at left
    "mindless"

    $ renpy.show(f"cherie {pose} normal")
    show expression f"cherie {pose} normal" as c2 at left
    "normal"

    $ renpy.show(f"cherie {pose} sad")
    show expression f"cherie {pose} sad" as c2 at left
    "sad"

    $ renpy.show(f"cherie {pose} sadsmile")
    show expression f"cherie {pose} sadsmile" as c2 at left
    "sadsmile"

    $ renpy.show(f"cherie {pose} smile")
    show expression f"cherie {pose} smile" as c2 at left
    "smile"

    $ renpy.show(f"cherie {pose} stuned")
    show expression f"cherie {pose} stuned" as c2 at left
    "stuned"

    $ renpy.show(f"cherie {pose} surprised")
    show expression f"cherie {pose} surprised" as c2 at left
    "surprised"

    $ renpy.show(f"cherie {pose} talkative")
    show expression f"cherie {pose} talkative" as c2 at left
    "talkative"

    $ renpy.show(f"cherie {pose} upset")
    show expression f"cherie {pose} upset" as c2 at left
    "upset"

    $ renpy.show(f"cherie {pose} whining")
    show expression f"cherie {pose} whining" as c2 at left
    "whining"

    $ renpy.show(f"cherie {pose} wink")
    show expression f"cherie {pose} wink" as c2 at left
    "wink"

    return

label test_cherie_outfits:
    $ cherie.flags.sexyswimsuit = False
    $ cherie.flags.sexydate = False
    $ cherie.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"cherie a naked{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b naked{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c naked{pregnancy}", tag="c3", at_list=[right])
        "naked"

        $ renpy.show(f"cherie a casual{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b casual{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c casual{pregnancy}", tag="c3", at_list=[right])
        "casual"

        $ renpy.show(f"cherie a date{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b date{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c date{pregnancy}", tag="c3", at_list=[right])
        "date"

        $ renpy.show(f"cherie a funeral{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b funeral{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c funeral{pregnancy}", tag="c3", at_list=[right])
        "funeral"

        $ renpy.show(f"cherie a halloween{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b halloween{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c halloween{pregnancy}", tag="c3", at_list=[right])
        "halloween"

        $ renpy.show(f"cherie a sexydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b sexydate{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c sexydate{pregnancy}", tag="c3", at_list=[right])
        "sexydate"

        $ renpy.show(f"cherie a sexyswimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b sexyswimsuit{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c sexyswimsuit{pregnancy}", tag="c3", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"cherie a sluttydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b sluttydate{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c sluttydate{pregnancy}", tag="c3", at_list=[right])
        "sluttydate"

        $ renpy.show(f"cherie a sport{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b sport{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c sport{pregnancy}", tag="c3", at_list=[right])
        "sport"

        $ renpy.show(f"cherie a swimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b swimsuit{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c swimsuit{pregnancy}", tag="c3", at_list=[right])
        "swimsuit"

        $ renpy.show(f"cherie a underwear{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b underwear{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c underwear{pregnancy}", tag="c3", at_list=[right])
        "underwear"

        $ renpy.show(f"cherie a wedding{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b wedding{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c wedding{pregnancy}", tag="c3", at_list=[right])
        "wedding"

        $ renpy.show(f"cherie a work{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"cherie b work{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"cherie c work{pregnancy}", tag="c3", at_list=[right])
        "work"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
