init -35 python:
    minami_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'constipated', 'cry', 'flirt', 'happy', 'hunt', 'mindless', 'sad', 'sadsmile', 'scared', 'stuned', 'surprised', 'talkative', 'tehe', 'vangry', 'whining'],
    'outfits': ['casual', 'sport', 'sleep', 'underwear', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'bikini', 'halloween', 'rpg', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'norobe'],
}

    def minami_anim_filter(attrs, anim_dict=minami_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PiercingsPicker, PositionPicker], npc=minami)(set(attrs))
        if "pregnant_navel" in pickers_attrs:
            pickers_attrs.remove("pregnant_navel")
            pickers_attrs.add("navel")
        attrs.extend(pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'haircuts', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=minami)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "home"):
            if minami.flags.naked and not 'naked' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('naked')
            elif minami.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
        
        
        attr_acc_back = None
        if not any(attr in mult_attrs['others'][0] for attr in ('topless', 'naked')) and sgl_attrs['outfits'][0] == 'rpg':
            attr_acc_back = "acc_back_rpg_" + sgl_attrs['haircuts'][0]
        
        
        attr_acc_head = None
        if not any(attr in mult_attrs['others'][0] for attr in ('topless', 'naked')):
            if sgl_attrs['outfits'][0] in ['date', 'wedding']:
                attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
            elif sgl_attrs['outfits'][0] == 'rpg':
                attr_acc_head = "acc_head_rpg_" + sgl_attrs['haircuts'][0]
        
        
        attr_kimono = None
        if 'norobe' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] == 'underwear':
            attr_kimono = "kimono"
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc_back, attr_acc_head, attr_kimono)


    def minami_close_anim_filter(attrs, anim_dict=minami_attrs):
        return minami_anim_filter(attrs, anim_dict)

label test_minami_exps:
    $ pose = 'a'

    $ renpy.show(f"minami {pose} angry")
    show expression f"minami {pose} angry" as m2 at left
    "angry"

    $ renpy.show(f"minami {pose} annoyed")
    show expression f"minami {pose} annoyed" as m2 at left
    "annoyed"

    $ renpy.show(f"minami {pose} constipated")
    show expression f"minami {pose} constipated" as m2 at left
    "constipated"

    $ renpy.show(f"minami {pose} cry")
    show expression f"minami {pose} cry" as m2 at left
    "cry"

    $ renpy.show(f"minami {pose} flirt")
    show expression f"minami {pose} flirt" as m2 at left
    "flirt"

    $ renpy.show(f"minami {pose} happy")
    show expression f"minami {pose} happy" as m2 at left
    "happy"

    $ renpy.show(f"minami {pose} hunt")
    show expression f"minami {pose} hunt" as m2 at left
    "hunt"

    $ renpy.show(f"minami {pose} mindless")
    show expression f"minami {pose} mindless" as m2 at left
    "mindless"

    $ renpy.show(f"minami {pose} normal")
    show expression f"minami {pose} normal" as m2 at left
    "normal"

    $ renpy.show(f"minami {pose} sad")
    show expression f"minami {pose} sad" as m2 at left
    "sad"

    $ renpy.show(f"minami {pose} sadsmile")
    show expression f"minami {pose} sadsmile" as m2 at left
    "sadsmile"

    $ renpy.show(f"minami {pose} scared")
    show expression f"minami {pose} scared" as m2 at left
    "scared"

    $ renpy.show(f"minami {pose} stuned")
    show expression f"minami {pose} stuned" as m2 at left
    "stuned"

    $ renpy.show(f"minami {pose} surprised")
    show expression f"minami {pose} surprised" as m2 at left
    "surprised"

    $ renpy.show(f"minami {pose} talkative")
    show expression f"minami {pose} talkative" as m2 at left
    "talkative"

    $ renpy.show(f"minami {pose} tehe")
    show expression f"minami {pose} tehe" as m2 at left
    "tehe"

    $ renpy.show(f"minami {pose} vangry")
    show expression f"minami {pose} vangry" as m2 at left
    "vangry"

    $ renpy.show(f"minami {pose} whining")
    show expression f"minami {pose} whining" as m2 at left
    "whining"

    return

label test_minami_outfits:
    $ minami.flags.sexyswimsuit = False
    $ minami.flags.sexydate = False
    $ minami.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"minami a bikini{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b bikini{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c bikini{pregnancy}", tag="m3", at_list=[right])
        "bikini"

        $ renpy.show(f"minami a casual{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b casual{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c casual{pregnancy}", tag="m3", at_list=[right])
        "casual"

        $ renpy.show(f"minami a date{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b date{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c date{pregnancy}", tag="m3", at_list=[right])
        "date"

        $ renpy.show(f"minami a halloween{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b halloween{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c halloween{pregnancy}", tag="m3", at_list=[right])
        "halloween"

        $ renpy.show(f"minami a rpg{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b rpg{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c rpg{pregnancy}", tag="m3", at_list=[right])
        "rpg"

        $ renpy.show(f"minami a sexydate{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b sexydate{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c sexydate{pregnancy}", tag="m3", at_list=[right])
        "sexydate"

        $ renpy.show(f"minami a sexyswimsuit{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b sexyswimsuit{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c sexyswimsuit{pregnancy}", tag="m3", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"minami a sleep{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b sleep{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c sleep{pregnancy}", tag="m3", at_list=[right])
        "sleep"

        $ renpy.show(f"minami a sluttydate{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b sluttydate{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c sluttydate{pregnancy}", tag="m3", at_list=[right])
        "sluttydate"

        $ renpy.show(f"minami a sport{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b sport{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c sport{pregnancy}", tag="m3", at_list=[right])
        "sport"

        $ renpy.show(f"minami a swimsuit{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b swimsuit{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c swimsuit{pregnancy}", tag="m3", at_list=[right])
        "swimsuit"

        $ renpy.show(f"minami a underwear{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b underwear{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c underwear{pregnancy}", tag="m3", at_list=[right])
        "underwear"

        $ renpy.show(f"minami a wedding{pregnancy}", tag="m1", at_list=[left])
        $ renpy.show(f"minami b wedding{pregnancy}", tag="m2", at_list=[center])
        $ renpy.show(f"minami c wedding{pregnancy}", tag="m3", at_list=[right])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
