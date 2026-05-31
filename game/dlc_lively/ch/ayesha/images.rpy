init -35 python:
    ayesha_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'lips', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'blush', 'curious', 'flirt', 'happy', 'joke', 'mindless', 'sad', 'sadsmile', 'stuned', 'surprised', 'talkative', 'upset', 'whining'],
    'outfits': ['casual', 'sport', 'work', 'sexywork', 'fight', 'halloween', 'wedding', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'bottomless', 'topless'],
}

    def ayesha_anim_filter(attrs, anim_dict=ayesha_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, PositionPicker], npc=ayesha)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=ayesha)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_hat = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['fight']:
            attr_hat = "hat_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_neck = None
        if 'topless' not in mult_attrs['others'][0] and (sgl_attrs['outfits'][0] == 'work' and sgl_attrs['positions'][0] != 'b'):
            attr_acc_neck = "acc_neck_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_arm = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['fight', 'wedding']:
            attr_acc_arm = "acc_arm_" + sgl_attrs['outfits'][0]
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc_arm, attr_acc_neck, attr_hat)


    def ayesha_close_anim_filter(attrs, anim_dict=ayesha_attrs):
        return ayesha_anim_filter(attrs, anim_dict)


label test_ayesha_exps:
    $ pose = 'a'

    $ renpy.show(f"ayesha {pose} angry")
    show expression f"ayesha {pose} angry" as a2 at left
    "angry"

    $ renpy.show(f"ayesha {pose} annoyed")
    show expression f"ayesha {pose} annoyed" as a2 at left
    "annoyed"

    $ renpy.show(f"ayesha {pose} blush")
    show expression f"ayesha {pose} blush" as a2 at left
    "blush"

    $ renpy.show(f"ayesha {pose} curious")
    show expression f"ayesha {pose} curious" as a2 at left
    "curious"

    $ renpy.show(f"ayesha {pose} flirt")
    show expression f"ayesha {pose} flirt" as a2 at left
    "flirt"

    $ renpy.show(f"ayesha {pose} happy")
    show expression f"ayesha {pose} happy" as a2 at left
    "happy"

    $ renpy.show(f"ayesha {pose} joke")
    show expression f"ayesha {pose} joke" as a2 at left
    "joke"

    $ renpy.show(f"ayesha {pose} mindless")
    show expression f"ayesha {pose} mindless" as a2 at left
    "mindless"

    $ renpy.show(f"ayesha {pose} normal")
    show expression f"ayesha {pose} normal" as a2 at left
    "normal"

    $ renpy.show(f"ayesha {pose} sad")
    show expression f"ayesha {pose} sad" as a2 at left
    "sad"

    $ renpy.show(f"ayesha {pose} sadsmile")
    show expression f"ayesha {pose} sadsmile" as a2 at left
    "sadsmile"

    $ renpy.show(f"ayesha {pose} stuned")
    show expression f"ayesha {pose} stuned" as a2 at left
    "stuned"

    $ renpy.show(f"ayesha {pose} surprised")
    show expression f"ayesha {pose} surprised" as a2 at left
    "surprised"

    $ renpy.show(f"ayesha {pose} talkative")
    show expression f"ayesha {pose} talkative" as a2 at left
    "talkative"

    $ renpy.show(f"ayesha {pose} upset")
    show expression f"ayesha {pose} upset" as a2 at left
    "upset"

    $ renpy.show(f"ayesha {pose} whining")
    show expression f"ayesha {pose} whining" as a2 at left
    "whining"

    return

label test_ayesha_outfits:
    $ ayesha.flags.sexyswimsuit = False
    $ ayesha.flags.sexydate = False
    $ ayesha.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"ayesha a casual{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b casual{pregnancy}", tag="a2", at_list=[right])
        "casual"

        $ renpy.show(f"ayesha a date{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b date{pregnancy}", tag="a2", at_list=[right])
        "date"

        $ renpy.show(f"ayesha a fight{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b fight{pregnancy}", tag="a2", at_list=[right])
        "fight"

        $ renpy.show(f"ayesha a halloween{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b halloween{pregnancy}", tag="a2", at_list=[right])
        "halloween"

        $ renpy.show(f"ayesha a sexydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b sexydate{pregnancy}", tag="a2", at_list=[right])
        "sexydate"

        $ renpy.show(f"ayesha a sexyswimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b sexyswimsuit{pregnancy}", tag="a2", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"ayesha a sexywork{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b sexywork{pregnancy}", tag="a2", at_list=[right])
        "sexywork"

        $ renpy.show(f"ayesha a sluttydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b sluttydate{pregnancy}", tag="a2", at_list=[right])
        "sluttydate"

        $ renpy.show(f"ayesha a sport{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b sport{pregnancy}", tag="a2", at_list=[right])
        "sport"

        $ renpy.show(f"ayesha a swimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b swimsuit{pregnancy}", tag="a2", at_list=[right])
        "swimsuit"

        $ renpy.show(f"ayesha a wedding{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b wedding{pregnancy}", tag="a2", at_list=[right])
        "wedding"

        $ renpy.show(f"ayesha a work{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"ayesha b work{pregnancy}", tag="a2", at_list=[right])
        "work"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
