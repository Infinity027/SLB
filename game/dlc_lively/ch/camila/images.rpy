init -35 python:
    camila_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'navel', 'nipples', 'nose', 'date_ears', 'sexydate_ears'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed','blush', 'bored', 'flirt', 'happy', 'mindless', 'sad', 'sadsmile', 'stuned', 'surprised', 'talkative', 'upset', 'weird', 'whining', 'wink'],
    'outfits': ['casual', 'work', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'bottomless', 'topless', 'nojacket'],
    'accessories': ['bullet', 'card', 'handcuff', 'mug', 'donut', 'wine', 'smoke'],
}

    def camila_anim_filter(attrs, anim_dict=camila_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PositionPicker], npc=camila)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others', 'accessories']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=camila)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        if sgl_attrs['outfits'][0] in ['halloween']:
            sgl_attrs['haircuts'][0] = None
        
        
        attr_smoke = None
        if 'smoke' in mult_attrs['accessories'][0]:
            attr_smoke = "smoke_" + sgl_attrs['positions'][0]
        
        
        attr_acc_head = None
        if sgl_attrs['outfits'][0] == 'sluttydate':
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        
        
        if 'ears' in mult_attrs['piercings'][0]:
            if sgl_attrs['outfits'][0] == 'halloween':
                mult_attrs['piercings'][0].remove('ears')
            elif sgl_attrs['outfits'][0] == 'date':
                mult_attrs['piercings'][0].remove('ears')
                mult_attrs['piercings'][0].append('date_ears')
            elif sgl_attrs['outfits'][0] == 'sexydate':
                mult_attrs['piercings'][0].remove('ears')
                mult_attrs['piercings'][0].append('sexydate_ears')
        if 'date_ears' in mult_attrs['piercings'][0] and sgl_attrs['outfits'][0] != 'date':
            mult_attrs['piercings'][0].remove('date_ears')
        if 'sexydate_ears' in mult_attrs['piercings'][0] and sgl_attrs['outfits'][0] != 'sexydate':
            mult_attrs['piercings'][0].remove('sexydate_ears')
        
        
        attr_necklace = None
        if not 'collar' in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['casual', 'date', 'work']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_arm = None
        if sgl_attrs['outfits'][0] in ['date', 'sexydate']:
            attr_acc_arm = "acc_arm_" + sgl_attrs['outfits'][0]
        
        
        attr_jacket = None
        if not any(attr in mult_attrs['others'][0] for attr in ('nojacket', 'topless')) and sgl_attrs['outfits'][0] == 'casual':
            attr_jacket = "jacket_" + sgl_attrs['outfits'][0]
        
        
        attr_eyes = None
        if sgl_attrs['outfits'][0] != 'halloween':
            attr_eyes = "eyes_" + sgl_attrs['exps'][0]
        elif sgl_attrs['exps'][0] == 'angry':
            attr_eyes = "eyes_" + sgl_attrs['exps'][0] + "_halloween"
        attr_mouth = "mouth_" + sgl_attrs['exps'][0]
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_mouth, attr_eyes, attr_jacket, attr_necklace, attr_acc_head, attr_smoke)


    def camila_close_anim_filter(attrs, anim_dict=camila_attrs):
        return camila_anim_filter(attrs, anim_dict)

label test_camila_exps:
    $ pose = 'a'

    $ renpy.show(f"camila {pose} angry")
    show expression f"camila {pose} angry" as c2 at left
    "angry"

    $ renpy.show(f"camila {pose} blush")
    show expression f"camila {pose} blush" as c2 at left
    "blush"

    $ renpy.show(f"camila {pose} bored")
    show expression f"camila {pose} bored" as c2 at left
    "bored"

    $ renpy.show(f"camila {pose} flirt")
    show expression f"camila {pose} flirt" as c2 at left
    "flirt"

    $ renpy.show(f"camila {pose} happy")
    show expression f"camila {pose} happy" as c2 at left
    "happy"

    $ renpy.show(f"camila {pose} mindless")
    show expression f"camila {pose} mindless" as c2 at left
    "mindless"

    $ renpy.show(f"camila {pose} normal")
    show expression f"camila {pose} normal" as c2 at left
    "normal"

    $ renpy.show(f"camila {pose} sad")
    show expression f"camila {pose} sad" as c2 at left
    "sad"

    $ renpy.show(f"camila {pose} sadsmile")
    show expression f"camila {pose} sadsmile" as c2 at left
    "sadsmile"

    $ renpy.show(f"camila {pose} surprised")
    show expression f"camila {pose} surprised" as c2 at left
    "surprised"

    $ renpy.show(f"camila {pose} talkative")
    show expression f"camila {pose} talkative" as c2 at left
    "talkative"

    $ renpy.show(f"camila {pose} upset")
    show expression f"camila {pose} upset" as c2 at left
    "upset"

    $ renpy.show(f"camila {pose} weird")
    show expression f"camila {pose} weird" as c2 at left
    "weird"

    $ renpy.show(f"camila {pose} whining")
    show expression f"camila {pose} whining" as c2 at left
    "whining"

    $ renpy.show(f"camila {pose} wink")
    show expression f"camila {pose} wink" as c2 at left
    "wink"

    return

label test_camila_outfits:
    $ camila.flags.sexyswimsuit = False
    $ camila.flags.sexydate = False
    $ camila.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"camila a casual{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b casual{pregnancy}", tag="c2", at_list=[right])
        "casual"

        $ renpy.show(f"camila a date{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b date{pregnancy}", tag="c2", at_list=[right])
        "date"

        $ renpy.show(f"camila a halloween{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b halloween{pregnancy}", tag="c2", at_list=[right])
        "halloween"

        $ renpy.show(f"camila a sexydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b sexydate{pregnancy}", tag="c2", at_list=[right])
        "sexydate"

        $ renpy.show(f"camila a sexyswimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b sexyswimsuit{pregnancy}", tag="c2", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"camila a sluttydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b sluttydate{pregnancy}", tag="c2", at_list=[right])
        "sluttydate"

        $ renpy.show(f"camila a sport{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b sport{pregnancy}", tag="c2", at_list=[right])
        "sport"

        $ renpy.show(f"camila a swimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b swimsuit{pregnancy}", tag="c2", at_list=[right])
        "swimsuit"

        $ renpy.show(f"camila a wedding{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b wedding{pregnancy}", tag="c2", at_list=[right])
        "wedding"

        $ renpy.show(f"camila a work{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"camila b work{pregnancy}", tag="c2", at_list=[right])
        "work"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
