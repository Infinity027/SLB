init -35 python:
    kylie_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'y'],
    'piercings': ['clit', 'ears', 'lips', 'navel', 'nipples', 'nose', 'tongue'],
    'exps': ['normal', 'angry', 'annoyed', 'blush', 'crazyhappy', 'crazysad', 'happy', 'impressed', 'mindless', 'sad', 'sadhappy', 'shy', 'shout', 'smile', 'stuned', 'surprised', 'talkative', 'vangry', 'whining', 'yandere'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'christmas', 'jail', 'wedding', 'sleep', 'underwear', 'naked'],
    'hoods': ['hooddown', 'hoodup'],
    'others': ['pregnant', 'pubes', 'collar', 'bloodyface', 'bottomless', 'topless'],
    'accessories': ['knife', 'bloodyknife', 'handcuffs', 'hoodie'],
}

    def kylie_anim_filter(attrs, anim_dict=kylie_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, PositionPicker], npc=kylie)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'hoods']},
        {k: [[], anim_dict[k]] for k in ['motions', 'others', 'piercings', 'accessories']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=kylie)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_acc = None
        if sgl_attrs['outfits'][0] in ['casual', 'christmas', 'halloween', 'wedding']:
            attr_acc = "acc_" + sgl_attrs['outfits'][0]
        
        
        if 'hoodie' in mult_attrs['accessories'][0]:
            if 'topless' in mult_attrs['others'][0] or sgl_attrs['outfits'][0] == 'naked':
                mult_attrs['accessories'][0].remove('hoodie')
        else:
            sgl_attrs['hoods'][0] = None
        
        
        attr_hair = 'hair_hoodup' if sgl_attrs['hoods'][0] == 'hoodup' else None
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc, attr_hair)


    def kylie_close_anim_filter(attrs, anim_dict=kylie_attrs):
        return kylie_anim_filter(attrs, anim_dict)

label test_kylie_exps:
    $ pose = 'a'

    $ renpy.show(f"kylie {pose} angry")
    show expression f"kylie {pose} angry" as k2 at left
    "angry"

    $ renpy.show(f"kylie {pose} annoyed")
    show expression f"kylie {pose} annoyed" as k2 at left
    "annoyed"

    $ renpy.show(f"kylie {pose} blush")
    show expression f"kylie {pose} blush" as k2 at left
    "blush"

    $ renpy.show(f"kylie {pose} crazyhappy")
    show expression f"kylie {pose} crazyhappy" as k2 at left
    "crazyhappy"

    $ renpy.show(f"kylie {pose} crazysad")
    show expression f"kylie {pose} crazysad" as k2 at left
    "crazysad"

    $ renpy.show(f"kylie {pose} happy")
    show expression f"kylie {pose} happy" as k2 at left
    "happy"

    $ renpy.show(f"kylie {pose} impressed")
    show expression f"kylie {pose} impressed" as k2 at left
    "impressed"

    $ renpy.show(f"kylie {pose} mindless")
    show expression f"kylie {pose} mindless" as k2 at left
    "mindless"

    $ renpy.show(f"kylie {pose} normal")
    show expression f"kylie {pose} normal" as k2 at left
    "normal"

    $ renpy.show(f"kylie {pose} sad")
    show expression f"kylie {pose} sad" as k2 at left
    "sad"

    $ renpy.show(f"kylie {pose} sadhappy")
    show expression f"kylie {pose} sadhappy" as k2 at left
    "sadhappy"

    $ renpy.show(f"kylie {pose} shout")
    show expression f"kylie {pose} shout" as k2 at left
    "shout"

    $ renpy.show(f"kylie {pose} shy")
    show expression f"kylie {pose} shy" as k2 at left
    "shy"

    $ renpy.show(f"kylie {pose} smile")
    show expression f"kylie {pose} smile" as k2 at left
    "smile"

    $ renpy.show(f"kylie {pose} stuned")
    show expression f"kylie {pose} stuned" as k2 at left
    "stuned"

    $ renpy.show(f"kylie {pose} surprised")
    show expression f"kylie {pose} surprised" as k2 at left
    "surprised"

    $ renpy.show(f"kylie {pose} talkative")
    show expression f"kylie {pose} talkative" as k2 at left
    "talkative"

    $ renpy.show(f"kylie {pose} vangry")
    show expression f"kylie {pose} vangry" as k2 at left
    "vangry"

    $ renpy.show(f"kylie {pose} whining")
    show expression f"kylie {pose} whining" as k2 at left
    "whining"

    $ renpy.show(f"kylie {pose} yandere")
    show expression f"kylie {pose} yandere" as k2 at left
    "yandere"

    return

label test_kylie_outfits:
    $ kylie.flags.sexyswimsuit = False
    $ kylie.flags.sexydate = False
    $ kylie.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"kylie a naked{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b naked{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y naked{pregnancy}", tag="k3", at_list=[right])
        "naked"

        $ renpy.show(f"kylie a casual{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b casual{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y casual{pregnancy}", tag="k3", at_list=[right])
        "casual"

        $ renpy.show(f"kylie a christmas{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b christmas{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y christmas{pregnancy}", tag="k3", at_list=[right])
        "christmas"

        $ renpy.show(f"kylie a date{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b date{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y date{pregnancy}", tag="k3", at_list=[right])
        "date"

        $ renpy.show(f"kylie a halloween{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b halloween{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y halloween{pregnancy}", tag="k3", at_list=[right])
        "halloween"

        $ renpy.show(f"kylie a jail{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b jail{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y jail{pregnancy}", tag="k3", at_list=[right])
        "jail"

        $ renpy.show(f"kylie a sexydate{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b sexydate{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y sexydate{pregnancy}", tag="k3", at_list=[right])
        "sexydate"

        $ renpy.show(f"kylie a sexyswimsuit{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b sexyswimsuit{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y sexyswimsuit{pregnancy}", tag="k3", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"kylie a sleep{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b sleep{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y sleep{pregnancy}", tag="k3", at_list=[right])
        "sleep"

        $ renpy.show(f"kylie a sluttydate{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b sluttydate{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y sluttydate{pregnancy}", tag="k3", at_list=[right])
        "sluttydate"

        $ renpy.show(f"kylie a sport{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b sport{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y sport{pregnancy}", tag="k3", at_list=[right])
        "sport"

        $ renpy.show(f"kylie a swimsuit{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b swimsuit{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y swimsuit{pregnancy}", tag="k3", at_list=[right])
        "swimsuit"

        $ renpy.show(f"kylie a underwear{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b underwear{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y underwear{pregnancy}", tag="k3", at_list=[right])
        "underwear"

        $ renpy.show(f"kylie a wedding{pregnancy}", tag="k1", at_list=[left])
        $ renpy.show(f"kylie b wedding{pregnancy}", tag="k2", at_list=[center])
        $ renpy.show(f"kylie y wedding{pregnancy}", tag="k3", at_list=[right])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
