init 1:

    layeredimage kiara smartphone:
        always "kiara_smartphone"

    layeredimage kiara ending:
        attribute_function Pickers([EndingKidPicker], npc=kiara)


        always "kiara_ending_bg"
        always "kiara_ending_limo"


        always "kiara_ending_couple"


        always "kiara_ending_eyes_nokid"
        attribute kid "kiara_ending_eyes_kid"


        always "kiara_ending_arm_nokid" when not kid
        attribute kid "kiara_ending_arm_kid"


        attribute kid


        always "kiara_ending_bodyguard1"
        always "kiara_ending_bodyguard2"

init -35 python:
    kiara_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c', 'd'],
    'piercings': ['clit', 'ears', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'blank', 'bothered', 'childish', 'confident', 'cringe', 'delicious', 'disappointed', 'disgusted', 'dreaming', 'evil', 'fantasize', 'flirt', 'guilty', 'hurt', 'irritated', 'mindless', 'mischievous', 'pleading', 'pout', 'preying', 'remorse', 'sad', 'sadsmile', 'scream', 'serious', 'shock', 'shout', 'smile', 'stare', 'stuned', 'surprised', 'talkative', 'tantrum', 'tasty', 'unhappy', 'uninterested', 'upset', 'warning', 'whining'],
    'outfits': ['casual', 'work', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'naked'],
    'others': ['pubes', 'collar', 'bottomless', 'topless'],
    'accessories': ['cap'],
}

    def kiara_anim_filter(attrs, anim_dict=kiara_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        add_pickers_attrs = Pickers([CollarPicker,  PubesPicker, HaircutPicker, PositionPicker], npc=kiara)(set(attrs))
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others', 'accessories']},
        prv_def_vals=['outfits']
    )
        
        
        if sgl_attrs['positions'][0] == 'd':
            sgl_attrs['exps'][0] = 'smoking'
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=kiara)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        if 'cap' in mult_attrs['accessories'][0]:
            if ('topless' in mult_attrs['others'][0] or sgl_attrs['outfits'][0] == 'naked'):
                mult_attrs['accessories'][0].remove('cap')
            else:
                sgl_attrs['haircuts'][0] = None
        
        
        attr_hat = None
        if 'cap' not in mult_attrs['accessories'][0] and 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] == 'halloween':
            attr_hat = "hat_" + sgl_attrs['outfits'][0]
        
        
        attr_glasses = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_glasses = "glasses_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_arm = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date', 'halloween', 'sluttydate', 'wedding', 'work']:
            attr_acc_arm = "acc_arm_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date', 'sexydate', 'wedding', 'work']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        poking = None
        if 'nipples' in mult_attrs['piercings'][0] and 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] != 'naked':
            poking = "poking"
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_necklace, attr_acc_arm, attr_glasses, attr_hat, poking)


    def kiara_close_anim_filter(attrs, anim_dict=kiara_attrs):
        return kiara_anim_filter(attrs, anim_dict)

label test_kiara_exps:
    $ pose = 'work a'

    $ renpy.show(f"kiara {pose} angry")
    show expression f"kiara {pose} angry" as k2 at left
    "angry"

    $ renpy.show(f"kiara {pose} annoyed")
    show expression f"kiara {pose} annoyed" as k2 at left
    "annoyed"

    $ renpy.show(f"kiara {pose} blank")
    show expression f"kiara {pose} blank" as k2 at left
    "blank"

    $ renpy.show(f"kiara {pose} bothered")
    show expression f"kiara {pose} bothered" as k2 at left
    "bothered"

    $ renpy.show(f"kiara {pose} childish")
    show expression f"kiara {pose} childish" as k2 at left
    "childish"

    $ renpy.show(f"kiara {pose} confident")
    show expression f"kiara {pose} confident" as k2 at left
    "confident"

    $ renpy.show(f"kiara {pose} cringe")
    show expression f"kiara {pose} cringe" as k2 at left
    "cringe"

    $ renpy.show(f"kiara {pose} delicious")
    show expression f"kiara {pose} delicious" as k2 at left
    "delicious"

    $ renpy.show(f"kiara {pose} disappointed")
    show expression f"kiara {pose} disappointed" as k2 at left
    "disappointed"

    $ renpy.show(f"kiara {pose} disgusted")
    show expression f"kiara {pose} disgusted" as k2 at left
    "disgusted"

    $ renpy.show(f"kiara {pose} dreaming")
    show expression f"kiara {pose} dreaming" as k2 at left
    "dreaming"

    $ renpy.show(f"kiara {pose} evil")
    show expression f"kiara {pose} evil" as k2 at left
    "evil"

    $ renpy.show(f"kiara {pose} fantasize")
    show expression f"kiara {pose} fantasize" as k2 at left
    "fantasize"

    $ renpy.show(f"kiara {pose} flirt")
    show expression f"kiara {pose} flirt" as k2 at left
    "flirt"

    $ renpy.show(f"kiara {pose} guilty")
    show expression f"kiara {pose} guilty" as k2 at left
    "guilty"

    $ renpy.show(f"kiara {pose} hurt")
    show expression f"kiara {pose} hurt" as k2 at left
    "hurt"

    $ renpy.show(f"kiara {pose} irritated")
    show expression f"kiara {pose} irritated" as k2 at left
    "irritated"

    $ renpy.show(f"kiara {pose} mindless")
    show expression f"kiara {pose} mindless" as k2 at left
    "mindless"

    $ renpy.show(f"kiara {pose} mischievous")
    show expression f"kiara {pose} mischievous" as k2 at left
    "mischievous"

    $ renpy.show(f"kiara {pose} normal")
    show expression f"kiara {pose} normal" as k2 at left
    "normal"

    $ renpy.show(f"kiara {pose} pleading")
    show expression f"kiara {pose} pleading" as k2 at left
    "pleading"

    $ renpy.show(f"kiara {pose} pout")
    show expression f"kiara {pose} pout" as k2 at left
    "pout"

    $ renpy.show(f"kiara {pose} preying")
    show expression f"kiara {pose} preying" as k2 at left
    "preying"

    $ renpy.show(f"kiara {pose} remorse")
    show expression f"kiara {pose} remorse" as k2 at left
    "remorse"

    $ renpy.show(f"kiara {pose} sad")
    show expression f"kiara {pose} sad" as k2 at left
    "sad"

    $ renpy.show(f"kiara {pose} sadsmile")
    show expression f"kiara {pose} sadsmile" as k2 at left
    "sadsmile"

    $ renpy.show(f"kiara {pose} scream")
    show expression f"kiara {pose} scream" as k2 at left
    "scream"

    $ renpy.show(f"kiara {pose} serious")
    show expression f"kiara {pose} serious" as k2 at left
    "serious"

    $ renpy.show(f"kiara {pose} shock")
    show expression f"kiara {pose} shock" as k2 at left
    "shock"

    $ renpy.show(f"kiara {pose} shout")
    show expression f"kiara {pose} shout" as k2 at left
    "shout"

    $ renpy.show(f"kiara {pose} smile")
    show expression f"kiara {pose} smile" as k2 at left
    "smile"

    $ renpy.show(f"kiara {pose} stare")
    show expression f"kiara {pose} stare" as k2 at left
    "stare"

    $ renpy.show(f"kiara {pose} stuned")
    show expression f"kiara {pose} stuned" as k2 at left
    "stuned"

    $ renpy.show(f"kiara {pose} surprised")
    show expression f"kiara {pose} surprised" as k2 at left
    "surprised"

    $ renpy.show(f"kiara {pose} talkative")
    show expression f"kiara {pose} talkative" as k2 at left
    "talkative"

    $ renpy.show(f"kiara {pose} tantrum")
    show expression f"kiara {pose} tantrum" as k2 at left
    "tantrum"

    $ renpy.show(f"kiara {pose} tasty")
    show expression f"kiara {pose} tasty" as k2 at left
    "tasty"

    $ renpy.show(f"kiara {pose} unhappy")
    show expression f"kiara {pose} unhappy" as k2 at left
    "unhappy"

    $ renpy.show(f"kiara {pose} uninterested")
    show expression f"kiara {pose} uninterested" as k2 at left
    "uninterested"

    $ renpy.show(f"kiara {pose} upset")
    show expression f"kiara {pose} upset" as k2 at left
    "upset"

    $ renpy.show(f"kiara {pose} warning")
    show expression f"kiara {pose} warning" as k2 at left
    "warning"

    $ renpy.show(f"kiara {pose} whining")
    show expression f"kiara {pose} whining" as k2 at left
    "whining"

    return

label test_kiara_outfits:
    $ kiara.flags.sexyswimsuit = False
    $ kiara.flags.sexydate = False
    $ kiara.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"kiara a casual{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b casual{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c casual{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d casual{pregnancy}", tag="k4", at_list=[mostright4])
        "casual"

        $ renpy.show(f"kiara a date{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b date{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c date{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d date{pregnancy}", tag="k4", at_list=[mostright4])
        "date"

        $ renpy.show(f"kiara a halloween{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b halloween{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c halloween{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d halloween{pregnancy}", tag="k4", at_list=[mostright4])
        "halloween"

        $ renpy.show(f"kiara a sexydate{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b sexydate{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c sexydate{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d sexydate{pregnancy}", tag="k4", at_list=[mostright4])
        "sexydate"

        $ renpy.show(f"kiara a sexyswimsuit{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b sexyswimsuit{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c sexyswimsuit{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d sexyswimsuit{pregnancy}", tag="k4", at_list=[mostright4])
        "sexyswimsuit"

        $ renpy.show(f"kiara a sluttydate{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b sluttydate{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c sluttydate{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d sluttydate{pregnancy}", tag="k4", at_list=[mostright4])
        "sluttydate"

        $ renpy.show(f"kiara a sport{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b sport{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c sport{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d sport{pregnancy}", tag="k4", at_list=[mostright4])
        "sport"

        $ renpy.show(f"kiara a swimsuit{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b swimsuit{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c swimsuit{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d swimsuit{pregnancy}", tag="k4", at_list=[mostright4])
        "swimsuit"

        $ renpy.show(f"kiara a underwear{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b underwear{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c underwear{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d underwear{pregnancy}", tag="k4", at_list=[mostright4])
        "underwear"

        $ renpy.show(f"kiara a wedding{pregnancy}", tag="k1", at_list=[mostleft4])
        $ renpy.show(f"kiara b wedding{pregnancy}", tag="k2", at_list=[left4])
        $ renpy.show(f"kiara c wedding{pregnancy}", tag="k3", at_list=[right4])
        $ renpy.show(f"kiara d wedding{pregnancy}", tag="k4", at_list=[mostright4])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
