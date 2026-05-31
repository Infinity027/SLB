init -35 python:
    shiori_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c', 'd', '_a', '_b'],
    'arms_c': ['peace', 'nopeace'],
    'arms_d': ['notpressed', 'pressed'],
    'piercings': ['clit', 'lips', 'navel', 'nipples', 'nose', 'tongue'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'bruised', 'embarrassed', 'flirt', 'happy', 'joke', 'mindless', 'sad', 'sadsmile', 'smile', 'stuned', 'surprised', 'talkative', 'upset', 'whining'],
    'outfits': ['casual', 'sport', 'work', 'sexywork', 'stripper', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'cowkini', 'miko', 'cosplay', 'halloween', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless'],
}

    def shiori_anim_filter(attrs, anim_dict=shiori_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PositionPicker], npc=shiori)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'arms_c', 'arms_d', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=shiori)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "work"):
            if shiori.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
            if shiori.flags.bottomless and not 'bottomless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('bottomless')
        
        
        if sgl_attrs['positions'][0] in ['_a', '_b']:
            sgl_attrs['positions'][0] = sgl_attrs['positions'][0][1:]
        else:
            
            sgl_attrs['positions'][0] = (
            {'a': 'c', 'b': 'd'} if Room.has_tag(shiori.room, "work") and sgl_attrs['outfits'][0] in ('sexywork', 'work')
            else {'c': 'a', 'd': 'b'}
        ).get(sgl_attrs['positions'][0], sgl_attrs['positions'][0])
        
        
        
        
        
        
        
        
        
        
        
        attr_hat = None
        if sgl_attrs['outfits'][0] in ['cosplay', 'cowkini', 'wedding']:
            attr_hat = "hat_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if not any(attr in mult_attrs['others'][0] for attr in ('collar', 'topless')) and sgl_attrs['outfits'][0] in ['date', 'work']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_tail = None
        if sgl_attrs['outfits'][0] == 'cowkini':
            attr_tail = "tail_" + sgl_attrs['outfits'][0]
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_tail, attr_necklace, attr_hat)


    def shiori_close_anim_filter(attrs, anim_dict=shiori_attrs):
        return shiori_anim_filter(attrs, anim_dict)

label test_shiori_exps:
    $ pose = 'a'

    $ renpy.show(f"shiori {pose} angry")
    show expression f"shiori {pose} angry" as s2 at left
    "angry"

    $ renpy.show(f"shiori {pose} annoyed")
    show expression f"shiori {pose} annoyed" as s2 at left
    "annoyed"

    $ renpy.show(f"shiori {pose} bruised")
    show expression f"shiori {pose} bruised" as s2 at left
    "bruised"

    $ renpy.show(f"shiori {pose} embarrassed")
    show expression f"shiori {pose} embarrassed" as s2 at left
    "embarrassed"

    $ renpy.show(f"shiori {pose} flirt")
    show expression f"shiori {pose} flirt" as s2 at left
    "flirt"

    $ renpy.show(f"shiori {pose} happy")
    show expression f"shiori {pose} happy" as s2 at left
    "happy"

    $ renpy.show(f"shiori {pose} joke")
    show expression f"shiori {pose} joke" as s2 at left
    "joke"

    $ renpy.show(f"shiori {pose} mindless")
    show expression f"shiori {pose} mindless" as s2 at left
    "mindless"

    $ renpy.show(f"shiori {pose} normal")
    show expression f"shiori {pose} normal" as s2 at left
    "normal"

    $ renpy.show(f"shiori {pose} sad")
    show expression f"shiori {pose} sad" as s2 at left
    "sad"

    $ renpy.show(f"shiori {pose} sadsmile")
    show expression f"shiori {pose} sadsmile" as s2 at left
    "sadsmile"

    $ renpy.show(f"shiori {pose} smile")
    show expression f"shiori {pose} smile" as s2 at left
    "smile"

    $ renpy.show(f"shiori {pose} stuned")
    show expression f"shiori {pose} stuned" as s2 at left
    "stuned"

    $ renpy.show(f"shiori {pose} surprised")
    show expression f"shiori {pose} surprised" as s2 at left
    "surprised"

    $ renpy.show(f"shiori {pose} talkative")
    show expression f"shiori {pose} talkative" as s2 at left
    "talkative"

    $ renpy.show(f"shiori {pose} upset")
    show expression f"shiori {pose} upset" as s2 at left
    "upset"

    $ renpy.show(f"shiori {pose} whining")
    show expression f"shiori {pose} whining" as s2 at left
    "whining"

    return

label test_shiori_outfits:
    $ shiori.flags.sexywork = False
    $ shiori.flags.sexyswimsuit = False
    $ shiori.flags.sexydate = False
    $ shiori.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"shiori a casual{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b casual{pregnancy}", tag="s2", at_list=[right])
        "casual"

        $ renpy.show(f"shiori a cosplay{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b cosplay{pregnancy}", tag="s2", at_list=[right])
        "cosplay"

        $ renpy.show(f"shiori a cowkini{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b cowkini{pregnancy}", tag="s2", at_list=[right])
        "cowkini"

        $ renpy.show(f"shiori a date{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b date{pregnancy}", tag="s2", at_list=[right])
        "date"

        $ renpy.show(f"shiori a halloween{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b halloween{pregnancy}", tag="s2", at_list=[right])
        "halloween"





        $ renpy.show(f"shiori a sexydate{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b sexydate{pregnancy}", tag="s2", at_list=[right])
        "sexydate"

        $ renpy.show(f"shiori a sexyswimsuit{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b sexyswimsuit{pregnancy}", tag="s2", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"shiori a sexywork{pregnancy}", tag="s1", at_list=[mostleft4])
        $ renpy.show(f"shiori b sexywork{pregnancy}", tag="s2", at_list=[left4])
        $ renpy.show(f"shiori c sexywork{pregnancy}", tag="s3", at_list=[right4])
        $ renpy.show(f"shiori d sexywork{pregnancy}", tag="s4", at_list=[mostright4])
        "sexywork"

        $ renpy.hide("s3")
        $ renpy.hide("s4")

        $ renpy.show(f"shiori a sluttydate{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b sluttydate{pregnancy}", tag="s2", at_list=[right])
        "sluttydate"

        $ renpy.show(f"shiori a sport{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b sport{pregnancy}", tag="s2", at_list=[right])
        "sport"

        $ renpy.show(f"shiori a stripper{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b stripper{pregnancy}", tag="s2", at_list=[right])
        "stripper"

        $ renpy.show(f"shiori a swimsuit{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b swimsuit{pregnancy}", tag="s2", at_list=[right])
        "swimsuit"

        $ renpy.show(f"shiori a wedding{pregnancy}", tag="s1", at_list=[left])
        $ renpy.show(f"shiori b wedding{pregnancy}", tag="s2", at_list=[right])
        "wedding"

        $ renpy.show(f"shiori a work{pregnancy}", tag="s1", at_list=[mostleft4])
        $ renpy.show(f"shiori b work{pregnancy}", tag="s2", at_list=[left4])
        $ renpy.show(f"shiori c work{pregnancy}", tag="s3", at_list=[right4])
        $ renpy.show(f"shiori d work{pregnancy}", tag="s4", at_list=[mostright4])
        "work"

        $ renpy.hide("s3")
        $ renpy.hide("s4")

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
