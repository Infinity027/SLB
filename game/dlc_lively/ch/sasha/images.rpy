init -35 python:
    sasha_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'boobs': ['noboobjob', 'boobjob'],
    'exps': ['normal', 'angry', 'annoyed', 'cry', 'dazed', 'embarrassed', 'flirt', 'happy', 'joke', 'mindless', 'pain', 'sad', 'sadsmile', 'shocked', 'shout', 'shy', 'stuned', 'surprised', 'talkative', 'upset', 'vangry', 'whining', 'wink', 'wtf'],
    'outfits': ['casual', 'casual2', 'sport', 'date', 'sexydate', 'sluttydate', 'halloween', 'rpg', 'swimsuit', 'sexyswimsuit', 'towel', 'underwear', 'sleep', 'rope', 'strapon', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'leash', 'blush', 'cumface', 'cummouth', 'topless', 'bottomless', 'noacc'],
}

    def sasha_anim_filter(attrs, anim_dict=sasha_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        pickers_attrs = Pickers([PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PiercingsPicker, PositionPicker], npc=sasha)(set(attrs))
        
        if "pregnant_navel" in pickers_attrs:
            pickers_attrs.remove("pregnant_navel")
            pickers_attrs.add("navel")
        attrs.extend(pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'haircuts', 'boobs', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=sasha)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "home"):
            if sasha.flags.topless and not 'topless' in mult_attrs['others'][0]:
                mult_attrs['others'][0].append('topless')
        
        
        if sgl_attrs['outfits'][0] in ['halloween']:
            sgl_attrs['haircuts'][0] = "wig"
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['halloween', 'rpg', 'sexyswimsuit', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_acc_hand = "acc_hand_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_hand = None
        
        
        if sgl_attrs['outfits'][0] in ['rpg']:
            attr_acc_tattoo = "acc_tattoo_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_tattoo = None
        
        
        if sgl_attrs['outfits'][0] in ['rpg']:
            attr_acc_back = "acc_back_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_back = None
        
        
        if 'leash' in mult_attrs['others'][0] and 'collar' not in mult_attrs['others'][0]:
            mult_attrs['others'][0].remove('leash')
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        
        return filtered_attrs(mult_attrs, sgl_attrs, attr_acc_back, attr_acc_tattoo, attr_acc_hand, attr_acc_head)


    def sasha_close_anim_filter(attrs, anim_dict=sasha_attrs):
        return sasha_anim_filter(attrs, anim_dict)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
