init 1:
    layeredimage claire kiss:
        attribute_function Pickers([CollarPicker, PiercingsPicker, HaircutPicker, OutfitPicker, PregnancyPicker], npc=claire)


        always "claire_kiss_mbody"


        group outfitmike auto if_not ["naked"]:
            attribute wedding "claire_kiss_outfitmike_date"
            attribute sluttydate "claire_kiss_outfitmike_date"


        always "claire_kiss_cbody"


        attribute pregnant


        attribute collar


        attribute clit null
        attribute lips null
        attribute nipples null
        attribute pregnant_navel null
        group multiple auto variant piercings


        attribute naked null
        attribute topless null
        group outfit auto if_not["naked", "topless"]:
            attribute santa "claire_kiss_outfit_date"
            attribute rpg "claire_kiss_outfit_date"
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]:
            attribute santa "claire_kiss_outfit_pregnant_date"
            attribute rpg "claire_kiss_outfit_pregnant_date"


        group haircuts auto


        group acc auto


        always "claire_kiss_hairmike"


        always "claire_kiss_shadow"


        always "claire_kiss_armmike" if_not ["halloween"]


        group outfitmike_sleeve auto if_not ["naked", "swimsuit", "sexyswimsuit", "sluttyswimsuit"]:
            attribute casual default
            attribute wedding "claire_kiss_outfitmike_sleeve_date"
            attribute sluttydate "claire_kiss_outfitmike_sleeve_date"
            attribute sexydate "claire_kiss_outfitmike_sleeve_date"

    layeredimage claire smartphone:
        always "claire_smartphone"


    layeredimage claire bj:
        attribute_function Pickers([HaircutPicker, PiercingsPicker, CollarPicker, DickPicker], npc=claire)


        group bg auto:
            attribute bedroom default


        always "claire_bj_cbody"


        attribute collar

        always "claire_bj_righthand"


        group eyes auto:
            attribute open default


        group mouth auto:
            attribute happy default

        attribute tongue
        attribute saliva


        attribute naked null
        group outfit auto if_not "naked"


        attribute clit null
        attribute lips null
        attribute navel null
        attribute nipples null
        attribute pregnant_navel null
        group multiple auto variant piercings


        always "claire_bj_hairshadow"
        group haircuts auto:
            attribute nohaircut default


        group mike auto:
            attribute down default


        attribute mc_casual null
        group mikeoutfit auto if_not ["naked"]:
            attribute sexyswimsuit "claire_bj_mikeoutfit_up_swimsuit" if_any "up"
            attribute sexyswimsuit "claire_bj_mikeoutfit_down_swimsuit" if_any "down"
        group mikeoutfit auto variant "up" if_any ["up"] if_not ["naked"]
        group mikeoutfit auto variant "down" if_any ["down"] if_not ["naked"]

        attribute facecum


        group dickpos:
            attribute blowjob null
            attribute out null default
        group dick auto variant "down" if_any "down"
        group dick auto variant "blowjob" if_all ["up", "blowjob"]
        group dick auto variant "up" if_any "up" if_not "blowjob"


        group lefthand auto


        attribute cum null
        always "claire_bj_cum_inside" if_all ["up", "blowjob", "cum"]
        group cum auto variant "out" if_all ["up", "cum"] if_not ["blowjob"]
        group cum auto variant "down" if_all ["down", "cum"]

        attribute bodycum if_not "down"

    layeredimage claire cunnilingus:
        attribute_function Pickers([CollarPicker, PiercingsPicker, HaircutPicker, PubesPicker, OutfitPicker, PregnancyPicker, ButtplugPicker, RoomPicker], npc=claire)

        group bg auto

        always "claire_cunnilingus_bodies"

        attribute pregnant

        attribute pubes

        attribute buttplug

        attribute collar

        group eyes auto:
            attribute wide default
            attribute pleasure
            attribute closed

        group mouth auto:
            attribute happy default

        group pussy auto

        group multiple auto variant piercings
        attribute nose null

        attribute cum null
        group cum auto when cum

        attribute naked null
        group outfits auto when not naked
        attribute casual null

        group haircuts auto

        group arms auto:
            attribute lick default

        attribute tongue

    layeredimage claire doggy:
        attribute_function Pickers([CollarPicker, PiercingsPicker, HaircutPicker, OutfitPicker, ButtplugPicker, RoomPicker, DickPicker], npc=claire)

        group multiple:
            attribute casual null
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null

        group bg auto

        group dicks auto:
            attribute outside null default
            attribute anal null
            attribute vaginal null

        group dicks auto variant inside when anal or vaginal

        attribute condom null
        group condom auto variant vaginal when condom and vaginal

        attribute buttplug when not anal

        always "claire_doggy_creampie" when cum and (anal or vaginal) and not condom

        always "claire_doggy_claire"

        attribute naked null
        group outfits auto when not naked

        group mouth auto:
            attribute happy default
        group eyes auto:
            attribute wide default

        always "claire_doggy_piercings_ears"
        group multiple auto variant piercings

        attribute drool

        attribute cum null
        group cum auto when cum

        group haircuts auto

        group dicks auto variant outside when outside
        group condom auto variant outside when condom and outside

        always "claire_doggy_mike"

        group cumshot auto when cum and outside and not condom

    layeredimage claire sixtynine:
        attribute_function Pickers([HaircutPicker, CollarPicker, PiercingsPicker, OutfitPicker, DickPicker, RoomPicker], npc=claire)


        group bg auto

        always "claire_sixtynine_claire"

        attribute naked null
        group outfits auto when not naked
        attribute casual null

        attribute collar
        attribute nose
        attribute clit null
        attribute navel null
        attribute pregnant_navel null
        attribute nipples null

        group mouth auto:
            attribute happy default

        group eyes auto:
            attribute wide default

        attribute makeup

        group haircuts auto

        group dicks auto:
            attribute out null default
            attribute blowjob null
            attribute lick null

        always "claire_sixtynine_mike_up" when out or blowjob
        always "claire_sixtynine_mike_down" when lick

        group dick auto variant out when out
        group dick auto variant blowjob when blowjob
        group dick auto variant lick when lick

        group tongue auto

        attribute drool

        attribute cumshot null
        group cumshot auto when cumshot

        attribute cum null
        group multiple auto variant cum when cum

    layeredimage claire fullnelson:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PubesPicker, CollarPicker, PiercingsPicker, OutfitPicker, ButtplugPicker, DickPicker, RoomPicker], npc=claire)

        group bg auto

        always "claire_fullnelson_bodies"

        group anus auto when anal

        always "claire_fullnelson_novaginal" when not vaginal

        attribute pregnant
        attribute buttplug

        group eyes auto:
            attribute wide default

        group mouth auto:
            attribute happy default

        group multiple auto variant piercings
        attribute pubes

        attribute naked null
        attribute casual null
        group outfits auto when not naked

        always "claire_fullnelson_arms"

        group haircuts auto

        group dicks auto:
            attribute out null default
            attribute anal null
            attribute vaginal null

        group dick auto variant out when out
        group dick auto variant anal when anal
        group dick auto variant vaginal when vaginal

        attribute condom null
        group condom auto variant out when condom and out
        group condom auto variant vaginal when condom and vaginal


        attribute cum null
        always "claire_fullnelson_cum_anal" if_all ["anal", "cum"]
        always "claire_fullnelson_cum_vaginal" if_all ["vaginal", "cum"]
        group cum auto variant "out" if_all ["out", "cum"]

        group multiple auto variant bodycum

    layeredimage claire missionary:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker, PubesPicker, OutfitPicker], npc=claire)


        group bg auto:
            attribute bedroom default


        always "claire_missionary_claire"


        always "claire_missionary_anus" if_any ["anal", "plug"]


        attribute pubes


        attribute pregnant


        group haircuts auto:
            attribute nohaircut default


        group eyes auto:
            attribute wide default


        group mouth auto:
            attribute happy default


        attribute lips null
        group multiple auto variant piercings


        attribute naked null
        attribute casual null
        group outfit auto if_not "naked"
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not "naked"


        always "claire_missionary_mike"


        always "claire_missionary_mike_eyes"


        attribute collar


        attribute buttplug


        always "claire_missionary_mikeoutfit_underwear" if_any ["underwear"] if_not ["naked"]


        group dickpos:
            attribute anal null
            attribute vaginal null
            attribute out null default
        group dick auto variant "anal" if_any "anal"
        group dick auto variant "vaginal" if_any "vaginal"
        group dick auto variant "out" if_any "out"


        attribute condom null
        group condom auto variant "anal" if_all ["condom", "anal"]
        group condom auto variant "vaginal" if_all ["condom", "vaginal"]
        group condom auto variant "out" if_all ["condom", "out"]


        always "claire_missionary_mikeoutfit_date" if_any ["date", "sexydate", "sluttydate"] if_not ["naked"]



        attribute cum null
        always "claire_missionary_cum_anal" if_all ["anal", "cum"] if_not ["condom"]
        always "claire_missionary_cum_vaginal" if_all ["vaginal", "cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom"]


        group multiple auto variant bodycum if_not ["condom"]

    layeredimage claire ending:

        always:
            "claire_ending_bg"


        attribute mike


        attribute boy


        attribute claire


        attribute girl


        group multiple auto variant food

init -35 python:
    claire_attrs = {
    'motions': ['idle'],
    'positions': ['a', 'b', 'c'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'bored', 'bothered', 'careless', 'conceited', 'cry', 'dazed', 'disappointed', 'eating', 'embarrassed', 'evil', 'furious', 'guilty', 'happy', 'mad', 'mindless', 'pained', 'pissed', 'pleased', 'pout', 'sad', 'sadsmile', 'shy', 'startle', 'stuned', 'surprised', 'talkative', 'upset', 'whining', 'wink'],
    'outfits': ['casual', 'sport', 'date', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'halloween', 'wedding', 'underwear', 'naked'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'noacc'],
}

    def claire_anim_filter(attrs, anim_dict=claire_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PositionPicker], npc=claire)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['positions', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=claire)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_acc_head = None
        if not any(attr in mult_attrs['others'][0] for attr in ('noacc', 'topless')) and sgl_attrs['outfits'][0] in ['halloween', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['casual']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        poking_piercings = None
        if 'topless' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] != 'naked':
            poking_piercings = "poking"
        
        
        acc_remover = []
        if 'topless' in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['sluttydate']:
            acc_remover.append('topless_sluttydate')
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs(mult_attrs, sgl_attrs, attr_necklace, attr_acc_head, poking_piercings, acc_remover)


    def claire_close_anim_filter(attrs, anim_dict=claire_attrs):
        return claire_anim_filter(attrs, anim_dict)

label test_claire_exps:
    $ pose = 'a'

    $ renpy.show(f"claire {pose} angry")
    show expression f"claire {pose} angry" as c2 at left
    "angry"

    $ renpy.show(f"claire {pose} annoyed")
    show expression f"claire {pose} annoyed" as c2 at left
    "annoyed"

    $ renpy.show(f"claire {pose} bored")
    show expression f"claire {pose} bored" as c2 at left
    "bored"

    $ renpy.show(f"claire {pose} bothered")
    show expression f"claire {pose} bothered" as c2 at left
    "bothered"

    $ renpy.show(f"claire {pose} careless")
    show expression f"claire {pose} careless" as c2 at left
    "careless"

    $ renpy.show(f"claire {pose} conceited")
    show expression f"claire {pose} conceited" as c2 at left
    "conceited"

    $ renpy.show(f"claire {pose} cry")
    show expression f"claire {pose} cry" as c2 at left
    "cry"

    $ renpy.show(f"claire {pose} dazed")
    show expression f"claire {pose} dazed" as c2 at left
    "dazed"

    $ renpy.show(f"claire {pose} disappointed")
    show expression f"claire {pose} disappointed" as c2 at left
    "disappointed"

    $ renpy.show(f"claire {pose} eating")
    show expression f"claire {pose} eating" as c2 at left
    "eating"

    $ renpy.show(f"claire {pose} embarrassed")
    show expression f"claire {pose} embarrassed" as c2 at left
    "embarrassed"

    $ renpy.show(f"claire {pose} evil")
    show expression f"claire {pose} evil" as c2 at left
    "evil"

    $ renpy.show(f"claire {pose} furious")
    show expression f"claire {pose} furious" as c2 at left
    "furious"

    $ renpy.show(f"claire {pose} guilty")
    show expression f"claire {pose} guilty" as c2 at left
    "guilty"

    $ renpy.show(f"claire {pose} happy")
    show expression f"claire {pose} happy" as c2 at left
    "happy"

    $ renpy.show(f"claire {pose} mad")
    show expression f"claire {pose} mad" as c2 at left
    "mad"

    $ renpy.show(f"claire {pose} mindless")
    show expression f"claire {pose} mindless" as c2 at left
    "mindless"

    $ renpy.show(f"claire {pose} normal")
    show expression f"claire {pose} normal" as c2 at left
    "normal"

    $ renpy.show(f"claire {pose} pained")
    show expression f"claire {pose} pained" as c2 at left
    "pained"

    $ renpy.show(f"claire {pose} pissed")
    show expression f"claire {pose} pissed" as c2 at left
    "pissed"

    $ renpy.show(f"claire {pose} pleased")
    show expression f"claire {pose} pleased" as c2 at left
    "pleased"

    $ renpy.show(f"claire {pose} pout")
    show expression f"claire {pose} pout" as c2 at left
    "pout"

    $ renpy.show(f"claire {pose} sad")
    show expression f"claire {pose} sad" as c2 at left
    "sad"

    $ renpy.show(f"claire {pose} sadsmile")
    show expression f"claire {pose} sadsmile" as c2 at left
    "sadsmile"

    $ renpy.show(f"claire {pose} shy")
    show expression f"claire {pose} shy" as c2 at left
    "shy"

    $ renpy.show(f"claire {pose} startle")
    show expression f"claire {pose} startle" as c2 at left
    "startle"

    $ renpy.show(f"claire {pose} stuned")
    show expression f"claire {pose} stuned" as c2 at left
    "stuned"

    $ renpy.show(f"claire {pose} surprised")
    show expression f"claire {pose} surprised" as c2 at left
    "surprised"

    $ renpy.show(f"claire {pose} talkative")
    show expression f"claire {pose} talkative" as c2 at left
    "talkative"

    $ renpy.show(f"claire {pose} upset")
    show expression f"claire {pose} upset" as c2 at left
    "upset"

    $ renpy.show(f"claire {pose} whining")
    show expression f"claire {pose} whining" as c2 at left
    "whining"

    $ renpy.show(f"claire {pose} wink")
    show expression f"claire {pose} wink" as c2 at left
    "wink"

    return

label test_claire_outfits:
    $ claire.flags.sexyswimsuit = False
    $ claire.flags.sexydate = False
    $ claire.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"claire a casual{pregnancy} haircut", tag="c1", at_list=[left])
        $ renpy.show(f"claire b casual{pregnancy} haircut", tag="c2", at_list=[center])
        $ renpy.show(f"claire c casual{pregnancy} haircut", tag="c3", at_list=[right])
        "casual"

        $ renpy.show(f"claire a date{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b date{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c date{pregnancy}", tag="c3", at_list=[right])
        "date"

        $ renpy.show(f"claire a halloween{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b halloween{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c halloween{pregnancy}", tag="c3", at_list=[right])
        "halloween"

        $ renpy.show(f"claire a sexydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b sexydate{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c sexydate{pregnancy}", tag="c3", at_list=[right])
        "sexydate"

        $ renpy.show(f"claire a sexyswimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b sexyswimsuit{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c sexyswimsuit{pregnancy}", tag="c3", at_list=[right])
        "sexyswimsuit"

        $ renpy.show(f"claire a sluttydate{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b sluttydate{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c sluttydate{pregnancy}", tag="c3", at_list=[right])
        "sluttydate"

        $ renpy.show(f"claire a sport{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b sport{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c sport{pregnancy}", tag="c3", at_list=[right])
        "sport"

        $ renpy.show(f"claire a swimsuit{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b swimsuit{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c swimsuit{pregnancy}", tag="c3", at_list=[right])
        "swimsuit"

        $ renpy.show(f"claire a underwear{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b underwear{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c underwear{pregnancy}", tag="c3", at_list=[right])
        "underwear"

        $ renpy.show(f"claire a wedding{pregnancy}", tag="c1", at_list=[left])
        $ renpy.show(f"claire b wedding{pregnancy}", tag="c2", at_list=[center])
        $ renpy.show(f"claire c wedding{pregnancy}", tag="c3", at_list=[right])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
