init -35 python:
    aletta_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['chain', 'clit', 'ears', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'dreamy', 'embarrassed', 'flirt', 'happy', 'mindless', 'normal', 'pain', 'pleasure', 'sad', 'sadsmile', 'scared', 'stuned', 'surprised', 'talkative', 'upset', 'whining', 'wink'],
    'outfits': ['casual', 'sport', 'work', 'sexywork', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'suit', 'halloween', 'cosplay', 'wedding', 'underwear', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'leash', 'blush', 'bottomless', 'topless', 'noglasses', 'nopatsies'],
    'accessories': ['glasses', 'helmet', 'remote', 'shake', 'panties'],
}

    def aletta_anim_filter(attrs, anim_dict=aletta_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, PositionPicker], npc=aletta)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'haircuts', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'others', 'piercings', 'accessories']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=aletta)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "work"):
            if aletta.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
            if aletta.flags.bottomless and not 'bottomless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('bottomless')
        
        
        attr_glasses = None
        if 'glasses' in mult_attrs['accessories'][0] and not ('noglasses' in mult_attrs['others'][0] or 'helmet' in mult_attrs['accessories'][0]):
            attr_glasses = "glasses_" + sgl_attrs['positions'][0]
        
        
        attr_helmet = None
        if 'helmet' in mult_attrs['accessories'][0]:
            attr_helmet = "helmet_" + sgl_attrs['positions'][0]
        
        
        attr_hat = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['cosplay', 'sexywork']:
            attr_hat = "hat_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        
        
        
        
        if 'collar' in mult_attrs['others'][0] and sgl_attrs['outfits'][0] == 'sexywork':
            mult_attrs['others'][0].remove('collar')
            mult_attrs['others'][0].append('collar_sexywork')
        
        
        if 'leash' in mult_attrs['others'][0] and 'collar' not in mult_attrs['others'][0]:
            mult_attrs['others'][0].remove('leash')
        
        
        attr_patsies = None
        if not any(attr in mult_attrs['others'][0] for attr in ('nopatsies', 'topless')) and sgl_attrs['outfits'][0] == 'sluttydate':
            attr_patsies = "patsies"
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_patsies, attr_necklace, attr_hat, attr_helmet, attr_glasses)


    def aletta_close_anim_filter(attrs, anim_dict=aletta_attrs):
        return aletta_anim_filter(attrs, anim_dict)

label test_aletta_exps:
    $ pose = 'a'

    $ renpy.show(f"aletta {pose} angry")
    show expression f"aletta {pose} angry" as a2 at left
    "angry"

    $ renpy.show(f"aletta {pose} annoyed")
    show expression f"aletta {pose} annoyed" as a2 at left
    "annoyed"

    $ renpy.show(f"aletta {pose} dreamy")
    show expression f"aletta {pose} dreamy" as a2 at left
    "dreamy"

    $ renpy.show(f"aletta {pose} embarrassed")
    show expression f"aletta {pose} embarrassed" as a2 at left
    "embarrassed"

    $ renpy.show(f"aletta {pose} flirt")
    show expression f"aletta {pose} flirt" as a2 at left
    "flirt"

    $ renpy.show(f"aletta {pose} happy")
    show expression f"aletta {pose} happy" as a2 at left
    "happy"

    $ renpy.show(f"aletta {pose} mindless")
    show expression f"aletta {pose} mindless" as a2 at left
    "mindless"

    $ renpy.show(f"aletta {pose} normal")
    show expression f"aletta {pose} normal" as a2 at left
    "normal"

    $ renpy.show(f"aletta {pose} pain")
    show expression f"aletta {pose} pain" as a2 at left
    "pain"

    $ renpy.show(f"aletta {pose} pleasure")
    show expression f"aletta {pose} pleasure" as a2 at left
    "pleasure"

    $ renpy.show(f"aletta {pose} sad")
    show expression f"aletta {pose} sad" as a2 at left
    "sad"

    $ renpy.show(f"aletta {pose} sadsmile")
    show expression f"aletta {pose} sadsmile" as a2 at left
    "sadsmile"

    $ renpy.show(f"aletta {pose} scared")
    show expression f"aletta {pose} scared" as a2 at left
    "scared"

    $ renpy.show(f"aletta {pose} stuned")
    show expression f"aletta {pose} stuned" as a2 at left
    "stuned"

    $ renpy.show(f"aletta {pose} surprised")
    show expression f"aletta {pose} surprised" as a2 at left
    "surprised"

    $ renpy.show(f"aletta {pose} talkative")
    show expression f"aletta {pose} talkative" as a2 at left
    "talkative"

    $ renpy.show(f"aletta {pose} upset")
    show expression f"aletta {pose} upset" as a2 at left
    "upset"

    $ renpy.show(f"aletta {pose} whining")
    show expression f"aletta {pose} whining" as a2 at left
    "whining"

    $ renpy.show(f"aletta {pose} wink")
    show expression f"aletta {pose} wink" as a2 at left
    "wink"

    return

label test_aletta_outfits:
    $ aletta.flags.sexyswimsuit = False
    $ aletta.flags.sexydate = False
    $ aletta.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"aletta a casual{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b casual{pregnancy}", tag="a2", at_list=[right])
        "casual"

        $ renpy.show(f"aletta a cosplay{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b cosplay{pregnancy}", tag="a2", at_list=[right])
        "cosplay"

        $ renpy.show(f"aletta a date{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b date{pregnancy}", tag="a2", at_list=[right])
        "date"

        $ renpy.show(f"aletta a halloween{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b halloween{pregnancy}", tag="a2", at_list=[right])
        "halloween"

        $ renpy.show(f"aletta a sexydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b sexydate{pregnancy}", tag="a2", at_list=[right])
        "sexydate"

        $ renpy.show(f"aletta a sexyswimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b sexyswimsuit{pregnancy}", tag="a2", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"aletta a sexywork{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b sexywork{pregnancy}", tag="a2", at_list=[right])
        "sexywork"

        $ renpy.show(f"aletta a sluttydate{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b sluttydate{pregnancy}", tag="a2", at_list=[right])
        "sluttydate"

        $ renpy.show(f"aletta a sport{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b sport{pregnancy}", tag="a2", at_list=[right])
        "sport"

        $ renpy.show(f"aletta a suit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b suit{pregnancy}", tag="a2", at_list=[right])
        "suit"

        $ renpy.show(f"aletta a swimsuit{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b swimsuit{pregnancy}", tag="a2", at_list=[right])
        "swimsuit"

        $ renpy.show(f"aletta a underwear{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b underwear{pregnancy}", tag="a2", at_list=[right])
        "underwear"

        $ renpy.show(f"aletta a wedding{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b wedding{pregnancy}", tag="a2", at_list=[right])
        "wedding"

        $ renpy.show(f"aletta a work{pregnancy}", tag="a1", at_list=[left])
        $ renpy.show(f"aletta b work{pregnancy}", tag="a2", at_list=[right])
        "work"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
