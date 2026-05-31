init -35 python:
    palla_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'lips', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'blank', 'cry', 'flirt', 'grumpy', 'happy', 'joke', 'mindless', 'sad', 'sadsmile', 'shy', 'stuned', 'submissive', 'surprised', 'talkative', 'vangry', 'vulnerable', 'whining', 'wink'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'naked'],
    'others': ['pregnant', 'collar', 'pubes', 'blush', 'facecum', 'bottomless', 'topless', 'noacc'],
    'accessories': ['gag', 'wallet', 'glasses'],
}

    def palla_anim_filter(attrs, anim_dict=palla_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker], npc=palla)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        pwet_pickers_attrs = Pickers([PositionPicker], npc=palla)(set(attrs))
        attrs.extend(pwet_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'haircuts', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'accessories', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=palla)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_collar = "collar_" + sgl_attrs['positions'][0] if 'collar' in mult_attrs['others'][0] else None
        
        
        attr_pregnancy = "pregnant_" + sgl_attrs['positions'][0] if 'pregnant' in mult_attrs['others'][0] else None
        
        
        if sgl_attrs['outfits'][0] in ['halloween']:
            attr_haircut = "haircut_" + sgl_attrs['positions'][0]
        else:
            attr_haircut = sgl_attrs['haircuts'][0] + "_" + sgl_attrs['positions'][0]
        
        
        if sgl_attrs['outfits'][0] == "naked":
            attr_outfit = sgl_attrs['outfits'][0]
        else:
            attr_outfit = sgl_attrs['outfits'][0] + "_" + sgl_attrs['positions'][0]
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['halloween', 'maid']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        if any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) or sgl_attrs['outfits'][0] == 'naked':
            mult_attrs['accessories'][0] = []
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_collar, attr_pregnancy, attr_haircut, attr_outfit, attr_acc_head)


    def palla_close_anim_filter(attrs, anim_dict=palla_attrs):
        return palla_anim_filter(attrs, anim_dict)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
