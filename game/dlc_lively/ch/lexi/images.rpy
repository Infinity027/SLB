init -35 python:
    lexi_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c'],
    'piercings': ['clit', 'ears', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'beat', 'blank', 'bored', 'bubblegum', 'flirt', 'happy', 'lollipop', 'mindless', 'sad', 'sadsmile', 'smile', 'surprised', 'wink', 'wow', 'yawn'],
    'outfits': ['casual', 'underwear', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'jail', 'halloween', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'cum', 'topless', 'bottomless'],
    'accessories': ['nophone', 'bandaid', 'lolly'],
    'lolly': ['inside', 'outside'],
}

    def lexi_anim_filter(attrs, anim_dict=lexi_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker, PositionPicker], npc=lexi)(set(attrs))
        if "pregnant_navel" in pickers_attrs:
            pickers_attrs.remove("pregnant_navel")
            pickers_attrs.add("navel")
        attrs.extend(pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'lolly']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others', 'accessories']},
        prv_def_vals=['outfits']
    )
        
        
        exp = sgl_attrs['positions'][0] + "_" + sgl_attrs['exps'][0]
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=lexi)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "home"):
            if lexi.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
        
        
        attr_phone = 'phone' if 'nophone' not in mult_attrs['accessories'][0] else None
        
        
        if 'lolly' not in mult_attrs['accessories'][0] or sgl_attrs['exps'][0] == 'lollipop':
            sgl_attrs['lolly'][0] = None
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, exp, attr_phone)


    def lexi_close_anim_filter(attrs, anim_dict=lexi_attrs):
        return lexi_anim_filter(attrs, anim_dict)

label test_lexi_exps:
    $ pose = 'a'

    $ renpy.show(f"lexi {pose} angry")
    show expression f"lexi {pose} angry" as l2 at left
    "angry"

    $ renpy.show(f"lexi {pose} annoyed")
    show expression f"lexi {pose} annoyed" as l2 at left
    "annoyed"

    $ renpy.show(f"lexi {pose} beat")
    show expression f"lexi {pose} beat" as l2 at left
    "beat"

    $ renpy.show(f"lexi {pose} blank")
    show expression f"lexi {pose} blank" as l2 at left
    "blank"

    $ renpy.show(f"lexi {pose} bored")
    show expression f"lexi {pose} bored" as l2 at left
    "bored"

    $ renpy.show(f"lexi {pose} bubblegum")
    show expression f"lexi {pose} bubblegum" as l2 at left
    "bubblegum"

    $ renpy.show(f"lexi {pose} flirt")
    show expression f"lexi {pose} flirt" as l2 at left
    "flirt"

    $ renpy.show(f"lexi {pose} happy")
    show expression f"lexi {pose} happy" as l2 at left
    "happy"

    $ renpy.show(f"lexi {pose} lollipop")
    show expression f"lexi {pose} lollipop" as l2 at left
    "lollipop"

    $ renpy.show(f"lexi {pose} mindless")
    show expression f"lexi {pose} mindless" as l2 at left
    "mindless"

    $ renpy.show(f"lexi {pose} normal")
    show expression f"lexi {pose} normal" as l2 at left
    "normal"

    $ renpy.show(f"lexi {pose} sad")
    show expression f"lexi {pose} sad" as l2 at left
    "sad"

    $ renpy.show(f"lexi {pose} sadsmile")
    show expression f"lexi {pose} sadsmile" as l2 at left
    "sadsmile"

    $ renpy.show(f"lexi {pose} surprised")
    show expression f"lexi {pose} surprised" as l2 at left
    "surprised"

    $ renpy.show(f"lexi {pose} wink")
    show expression f"lexi {pose} wink" as l2 at left
    "wink"

    $ renpy.show(f"lexi {pose} wow")
    show expression f"lexi {pose} wow" as l2 at left
    "wow"

    $ renpy.show(f"lexi {pose} yawn")
    show expression f"lexi {pose} yawn" as l2 at left
    "yawn"

    return

label test_lexi_outfits:
    $ lexi.flags.sexyswimsuit = False
    $ lexi.flags.sexydate = False
    $ lexi.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"lexi a casual{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b casual{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c casual{pregnancy}", tag="l3", at_list=[right])
        "casual"

        $ renpy.show(f"lexi a date{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b date{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c date{pregnancy}", tag="l3", at_list=[right])
        "date"

        $ renpy.show(f"lexi a halloween{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b halloween{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c halloween{pregnancy}", tag="l3", at_list=[right])
        "halloween"

        $ renpy.show(f"lexi a jail{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b jail{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c jail{pregnancy}", tag="l3", at_list=[right])
        "jail"

        $ renpy.show(f"lexi a sexydate{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b sexydate{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c sexydate{pregnancy}", tag="l3", at_list=[right])
        "sexydate"

        $ renpy.show(f"lexi a sexyswimsuit{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b sexyswimsuit{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c sexyswimsuit{pregnancy}", tag="l3", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"lexi a sluttydate{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b sluttydate{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c sluttydate{pregnancy}", tag="l3", at_list=[right])
        "sluttydate"

        $ renpy.show(f"lexi a sport{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b sport{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c sport{pregnancy}", tag="l3", at_list=[right])
        "sport"

        $ renpy.show(f"lexi a swimsuit{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b swimsuit{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c swimsuit{pregnancy}", tag="l3", at_list=[right])
        "swimsuit"

        $ renpy.show(f"lexi a underwear{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b underwear{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c underwear{pregnancy}", tag="l3", at_list=[right])
        "underwear"

        $ renpy.show(f"lexi a wedding{pregnancy}", tag="l1", at_list=[left])
        $ renpy.show(f"lexi b wedding{pregnancy}", tag="l2", at_list=[center])
        $ renpy.show(f"lexi c wedding{pregnancy}", tag="l3", at_list=[right])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
