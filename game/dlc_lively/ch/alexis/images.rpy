init -35 python:
    alexis_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'lips', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'confused', 'cry', 'flirt', 'happy', 'mean', 'mindless', 'sad', 'sadsmile', 'smile', 'stuned', 'surprised', 'talkative', 'upset', 'whining', 'wink'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'collar2', 'blush', 'cum', 'bottomless', 'topless', 'nopatsies'],
}

    def alexis_anim_filter(attrs, anim_dict=alexis_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, PositionPicker], npc=alexis)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'others', 'piercings']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=alexis)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_acc_head = None
        if sgl_attrs['outfits'][0] in ['halloween', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_patsies = None
        if not any(attr in mult_attrs['others'][0] for attr in ('nopatsies', 'topless')) and sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_patsies = "patsies_" + sgl_attrs['outfits'][0]
        
        
        attr_gloves = None
        if sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_gloves = "gloves_" + sgl_attrs['outfits'][0]
        
        
        attr_stockings = None
        if 'bottomless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sexydate', 'sluttydate']:
            attr_stockings = "stockings_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_back = None
        if sgl_attrs['outfits'][0] in ['halloween']:
            attr_acc_back = "acc_back_" + sgl_attrs['outfits'][0]
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc_back, attr_stockings, attr_gloves, attr_patsies, attr_necklace, attr_acc_head)


    def alexis_close_anim_filter(attrs, anim_dict=alexis_attrs):
        return alexis_anim_filter(attrs, anim_dict)

label test_alexis_exps:
    $ pose = 'a'

    $ renpy.show(f"alexis {pose} angry")
    show expression f"alexis {pose} angry" as a2 at left
    "angry"

    $ renpy.show(f"alexis {pose} annoyed")
    show expression f"alexis {pose} annoyed" as a2 at left
    "annoyed"

    $ renpy.show(f"alexis {pose} confused")
    show expression f"alexis {pose} confused" as a2 at left
    "confused"

    $ renpy.show(f"alexis {pose} cry")
    show expression f"alexis {pose} cry" as a2 at left
    "cry"

    $ renpy.show(f"alexis {pose} flirt")
    show expression f"alexis {pose} flirt" as a2 at left
    "flirt"

    $ renpy.show(f"alexis {pose} happy")
    show expression f"alexis {pose} happy" as a2 at left
    "happy"

    $ renpy.show(f"alexis {pose} mean")
    show expression f"alexis {pose} mean" as a2 at left
    "mean"

    $ renpy.show(f"alexis {pose} mindless")
    show expression f"alexis {pose} mindless" as a2 at left
    "mindless"

    $ renpy.show(f"alexis {pose} normal")
    show expression f"alexis {pose} normal" as a2 at left
    "normal"

    $ renpy.show(f"alexis {pose} sad")
    show expression f"alexis {pose} sad" as a2 at left
    "sad"

    $ renpy.show(f"alexis {pose} sadsmile")
    show expression f"alexis {pose} sadsmile" as a2 at left
    "sadsmile"

    $ renpy.show(f"alexis {pose} smile")
    show expression f"alexis {pose} smile" as a2 at left
    "smile"

    $ renpy.show(f"alexis {pose} stuned")
    show expression f"alexis {pose} stuned" as a2 at left
    "stuned"

    $ renpy.show(f"alexis {pose} surprised")
    show expression f"alexis {pose} surprised" as a2 at left
    "surprised"

    $ renpy.show(f"alexis {pose} talkative")
    show expression f"alexis {pose} talkative" as a2 at left
    "talkative"

    $ renpy.show(f"alexis {pose} upset")
    show expression f"alexis {pose} upset" as a2 at left
    "upset"

    $ renpy.show(f"alexis {pose} whining")
    show expression f"alexis {pose} whining" as a2 at left
    "whining"

    $ renpy.show(f"alexis {pose} wink")
    show expression f"alexis {pose} wink" as a2 at left
    "wink"

    return

label test_alexis_outfits:
    $ alexis.flags.sexyswimsuit = False
    $ alexis.flags.sexydate = False
    $ alexis.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"alexis a casual{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b casual{pregnancy}", tag="a2", at_list=[right])
        "casual"

        $ renpy.show(f"alexis a date{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b date{pregnancy}", tag="a2", at_list=[right])
        "date"

        $ renpy.show(f"alexis a halloween{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b halloween{pregnancy}", tag="a2", at_list=[right])
        "halloween"

        $ renpy.show(f"alexis a sexydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b sexydate{pregnancy}", tag="a2", at_list=[right])
        "sexydate"

        $ renpy.show(f"alexis a sexyswimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b sexyswimsuit{pregnancy}", tag="a2", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"alexis a sluttydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b sluttydate{pregnancy}", tag="a2", at_list=[right])
        "sluttydate"

        $ renpy.show(f"alexis a sport{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b sport{pregnancy}", tag="a2", at_list=[right])
        "sport"

        $ renpy.show(f"alexis a swimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b swimsuit{pregnancy}", tag="a2", at_list=[right])
        "swimsuit"

        $ renpy.show(f"alexis a wedding{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"alexis b wedding{pregnancy}", tag="a2", at_list=[right])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
