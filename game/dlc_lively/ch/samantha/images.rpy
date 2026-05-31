init -35 python:
    samantha_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'navel', 'nipples', 'ears', 'lips', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'cry', 'flirt', 'gloomy', 'happy', 'mindless', 'sad', 'sadsmile', 'stuned', 'surprised', 'talkative', 'upset', 'wink'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'underwear', 'halloween', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'cum', 'bottomless', 'topless'],
    'accessories': ['ring'],
}

    def samantha_anim_filter(attrs, anim_dict=samantha_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker, PositionPicker], npc=samantha)(set(attrs))
        if "pregnant_navel" in pickers_attrs:
            pickers_attrs.remove("pregnant_navel")
            pickers_attrs.add("navel")
        attrs.extend(pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'accessories', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=samantha)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "home"):
            if samantha.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('topless')) and sgl_attrs['outfits'][0] in ['halloween']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sluttydate', 'wedding']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        else:
            attr_necklace = None
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs('appear', mult_attrs, sgl_attrs, attr_necklace, attr_acc_head)


    def samantha_close_anim_filter(attrs, anim_dict=samantha_attrs):
        return samantha_anim_filter(attrs, anim_dict)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
