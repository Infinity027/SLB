init -35 python:
    ayesha_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b'],
    'piercings': ['clit', 'ears', 'lips', 'navel', 'nipples', 'nose'],
    'exps': ['normal', 'angry', 'annoyed', 'blush', 'curious', 'flirt', 'happy', 'joke', 'mindless', 'sad', 'sadsmile', 'stuned', 'surprised', 'talkative', 'upset', 'whining'],
    'outfits': ['casual', 'sport', 'work', 'sexywork', 'fight', 'halloween', 'wedding', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'naked'],
    'others': ['pubes', 'collar', 'bottomless', 'topless'],
}
    def ayesha_anim_filter(attrs, anim_dict=ayesha_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        add_pickers_attrs = Pickers([ PubesPicker, CollarPicker, PositionPicker], npc=ayesha)(set(attrs))
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
