init -35 python:
    bree_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'd', 'z'],
    'piercings': ['clit', 'navel', 'nipples', 'ears', 'lips', 'nose', 'tongue'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'blank', 'cry', 'dazed', 'evil', 'flirt', 'gloomy', 'happy', 'hesitating', 'lose', 'mindless', 'mouthful', 'sad', 'sadsmile', 'sleepy', 'smile', 'stuned', 'surprised', 'talkative', 'thumb', 'vangry', 'wink'],
    'outfits': ['casual', 'innocentcasual', 'work', 'sport', 'date', 'puredate', 'innocentdate', 'sexydate', 'sluttydate', 'swimsuit', 'innocentswimsuit', 'sexyswimsuit', 'towel', 'underwear', 'daddy', 'rpg', 'bowsette', 'karate', 'halloween', 'invisible', 'chinese', 'dominatrix', 'apron', 'maid', 'pinkmaid', 'sleep', 'wedding', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'leash', 'blush', 'cum_mouthful', 'cum_face', 'bottomless', 'topless'],
}

    def bree_anim_filter(attrs, anim_dict=bree_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, PositionPicker], npc=bree)(set(attrs))
        if "pregnant_navel" in pickers_attrs:
            pickers_attrs.remove("pregnant_navel")
            pickers_attrs.add("navel")
        attrs.extend(pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'haircuts', 'exps', 'outfits']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        if (sgl_attrs['positions'][0] == 'z') != (sgl_attrs['outfits'][0] == 'dominatrix'):
            sgl_attrs['positions'][0] = "a"
            sgl_attrs['outfits'][0] = "casual"
        
        
        exp = sgl_attrs['positions'][0] + '_' + sgl_attrs['exps'][0]
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=bree)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        if not game.flags.disable_clothing_policy and Room.has_tag(game.room, "home"):
            if bree.flags.topless:
                if not 'topless' in mult_attrs['others'][0]:
                    mult_attrs['others'][0].append('topless')
                if sgl_attrs['outfits'][0] == 'sleep':
                    sgl_attrs['outfits'][0] = 'underwear'
        
        
        if sgl_attrs['outfits'][0] in ['rpg']:
            attr_acc_tattoo = "acc_tattoo_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_tattoo = None
        
        
        if sgl_attrs['outfits'][0] in ['halloween', 'maid', 'pinkmaid', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        else:
            attr_acc_head = None
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, exp, attr_acc_head, attr_acc_tattoo)


    def bree_close_anim_filter(attrs, anim_dict=bree_attrs):
        return bree_anim_filter(attrs, anim_dict)

label test_bree_exps:
    $ pose = 'a'

    $ renpy.show(f"bree {pose} angry")
    show expression f"bree {pose} angry" as b2 at left
    "angry"

    $ renpy.show(f"bree {pose} annoyed")
    show expression f"bree {pose} annoyed" as b2 at left
    "annoyed"

    $ renpy.show(f"bree {pose} blank")
    show expression f"bree {pose} blank" as b2 at left
    "blank"

    $ renpy.show(f"bree {pose} cry")
    show expression f"bree {pose} cry" as b2 at left
    "cry"

    $ renpy.show(f"bree {pose} dazed")
    show expression f"bree {pose} dazed" as b2 at left
    "dazed"

    $ renpy.show(f"bree {pose} evil")
    show expression f"bree {pose} evil" as b2 at left
    "evil"

    $ renpy.show(f"bree {pose} flirt")
    show expression f"bree {pose} flirt" as b2 at left
    "flirt"

    $ renpy.show(f"bree {pose} gloomy")
    show expression f"bree {pose} gloomy" as b2 at left
    "gloomy"

    $ renpy.show(f"bree {pose} happy")
    show expression f"bree {pose} happy" as b2 at left
    "happy"

    $ renpy.show(f"bree {pose} hesitating")
    show expression f"bree {pose} hesitating" as b2 at left
    "hesitating"

    $ renpy.show(f"bree {pose} lose")
    show expression f"bree {pose} lose" as b2 at left
    "lose"

    $ renpy.show(f"bree {pose} mindless")
    show expression f"bree {pose} mindless" as b2 at left
    "mindless"

    $ renpy.show(f"bree {pose} mouthful")
    show expression f"bree {pose} mouthful" as b2 at left
    "mouthful"

    $ renpy.show(f"bree {pose} normal")
    show expression f"bree {pose} normal" as b2 at left
    "normal"

    $ renpy.show(f"bree {pose} sad")
    show expression f"bree {pose} sad" as b2 at left
    "sad"

    $ renpy.show(f"bree {pose} sadsmile")
    show expression f"bree {pose} sadsmile" as b2 at left
    "sadsmile"

    $ renpy.show(f"bree {pose} sleepy")
    show expression f"bree {pose} sleepy" as b2 at left
    "sleepy"

    $ renpy.show(f"bree {pose} smile")
    show expression f"bree {pose} smile" as b2 at left
    "smile"

    $ renpy.show(f"bree {pose} stuned")
    show expression f"bree {pose} stuned" as b2 at left
    "stuned"

    $ renpy.show(f"bree {pose} surprised")
    show expression f"bree {pose} surprised" as b2 at left
    "surprised"

    $ renpy.show(f"bree {pose} talkative")
    show expression f"bree {pose} talkative" as b2 at left
    "talkative"

    $ renpy.show(f"bree {pose} thumb")
    show expression f"bree {pose} thumb" as b2 at left
    "thumb"

    $ renpy.show(f"bree {pose} vangry")
    show expression f"bree {pose} vangry" as b2 at left
    "vangry"

    $ renpy.show(f"bree {pose} wink")
    show expression f"bree {pose} wink" as b2 at left
    "wink"

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
