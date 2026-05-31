init -35 python:
    audrey_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'awkward', 'cry', 'embarrassed', 'flirt', 'frown', 'gloomy', 'happy', 'joke', 'lying', 'mindless', 'mock', 'sad', 'sadsmile', 'scared', 'stuned', 'surprised', 'talkative', 'upset', 'whining', 'yawn'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'work', 'sexywork', 'strapon', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'facecum', 'bottomless', 'topless', 'noacc'],
}

    def audrey_anim_filter(attrs, anim_dict=audrey_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker], npc=audrey)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        pwet_pickers_attrs = Pickers([PositionPicker], npc=audrey)(set(attrs))
        attrs.extend(pwet_pickers_attrs)
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=audrey)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "work"):
            if audrey.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
            if audrey.flags.bottomless and not 'bottomless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('bottomless')
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('collar', 'topless')) and sgl_attrs['outfits'][0] in ['date', 'wedding', 'work']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        else:
            attr_necklace = None
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('topless')) and sgl_attrs['outfits'][0] in ['swimsuit', 'sexyswimsuit']:
            mult_attrs['others'][0].append('sunglasses')
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_necklace, attr_acc_head)


    def audrey_close_anim_filter(attrs, anim_dict=audrey_attrs):
        return audrey_anim_filter(attrs, anim_dict)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
