init 5 python:
    class BathroomPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"BathroomPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "bathroom":
                    attr.add('bree')
                    if bree.activity_name == "pee":
                        attr.add('bree_pee')
                    elif bree.activity_name == "bath":
                        attr.add('bree_bath')
                    elif bree.activity_name == "brush":
                        attr.add('bree_brush')
                if not sasha.hidden and sasha.room == "bathroom":
                    attr.add('sasha')
                    if sasha.activity_name == "pee":
                        attr.add('sasha_pee')
                    elif sasha.activity_name == "shower":
                        attr.add('sasha_shower')
                    elif sasha.activity_name == "brush":
                        attr.add('sasha_brush')
                if not minami.hidden and minami.room == "bathroom":
                    attr.add('minami')
                    if minami.activity_name == "brush":
                        attr.add('minami_brush')
                    elif minami.activity_name == "shower":
                        attr.add('minami_shower')
                if not samantha.hidden and samantha.room == "bathroom" and Harem.find('samantha', name='home'):
                    attr.add('samantha')
                    if samantha.activity_name == "brush":
                        attr.add('samantha_brush')
                    elif samantha.activity_name == "bath":
                        attr.add('samantha_bath')
                if not lexi.hidden and lexi.room == "bathroom" and Harem.find('lexi', name='home'):
                    attr.add('lexi')
                    if lexi.activity_name == "shower":
                        attr.add('lexi_shower')
                    elif lexi.activity_name == "pee":
                        attr.add('lexi_pee')
            
            
            if active_girl and active_girl.id in ["bree", "sasha", "minami", "samantha", "lexi"]:
                if enable_debug_picker:
                    renpy.log(f"BathroomPicker remove active/interact girl: {active_girl.id}")
                for i in copy.copy(attr):
                    if i == active_girl.id or i.startswith(f"{active_girl.id}_"):
                        attr.discard(i)
            
            
            if enable_debug_picker:
                renpy.log(f"BathroomPicker result: {attr}")
            return attr

    Room.find("bathroom").lively_npc = ["bree", "sasha", "minami", 'samantha', "lexi"]

init 6:
    layeredimage bg bathroom:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, BathroomPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute topless null
        attribute bottomless null
        attribute naked null
        attribute bree_naked null
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_pregnant_navel null
        attribute bree_tongue null
        attribute lexi_naked null
        attribute lexi_clit null
        attribute lexi_navel null
        attribute lexi_nohaircut null
        attribute lexi_nose null
        attribute lexi_pregnant_navel null
        attribute lexi_tongue null
        attribute minami_naked null
        attribute minami_ears null
        attribute samantha_naked null
        attribute samantha_clit null
        attribute samantha_lips null
        attribute samantha_navel null
        attribute samantha_nohaircut null
        attribute samantha_pregnant_navel null
        attribute samantha_tongue null
        attribute sasha_naked null
        attribute sasha_lips null
        attribute sasha_tongue null

        attribute bree_topless null
        attribute lexi_topless null
        attribute minami_topless null
        attribute samantha_topless null
        attribute sasha_topless null

        attribute day "bathroom_day"
        attribute night "bathroom_night"


        attribute lexi null
        group lexi auto

        attribute lexi_collar variant lexi_pee when lexi and lexi_pee
        attribute lexi_collar variant lexi_shower when lexi and lexi_shower

        attribute lexi_pregnant variant lexi_shower when lexi and lexi_shower

        always "bg_bathroom_lexi_pee_lexi_hair" when lexi and lexi_pee
        always "bg_bathroom_lexi_shower_lexi_hair" when lexi and lexi_shower

        group multiple auto variant lexi_piercings_lexi_pee when lexi and lexi_pee
        group multiple auto variant lexi_piercings_lexi_shower when lexi and lexi_shower

        group lexi_top auto variant lexi_pee when lexi and lexi_pee and not (lexi_topless or lexi_naked)
        group lexi_bot auto variant lexi_pee when lexi and lexi_pee and not (lexi_bottomless or lexi_naked)


        attribute samantha null
        group samantha auto

        attribute samantha_pregnant variant samantha_bath when samantha and samantha_bath
        attribute samantha_pregnant variant samantha_brush when samantha and samantha_brush

        attribute samantha_collar variant samantha_bath when samantha and samantha_bath
        attribute samantha_collar variant samantha_brush when samantha and samantha_brush

        group multiple auto variant samantha_piercings_samantha_bath when samantha and samantha_bath
        group multiple auto variant samantha_piercings_samantha_brush when samantha and samantha_brush

        group samantha_top auto variant samantha_brush when samantha and samantha_brush and not (samantha_topless or samantha_naked)
        group samantha_bot auto variant samantha_brush when samantha and samantha_brush and not (samantha_bottomless or samantha_naked)

        always "bg_bathroom_samantha_bath_samantha_hair" when samantha and samantha_bath
        always "bg_bathroom_samantha_brush_samantha_hair" when samantha and samantha_brush

        group samantha_water auto variant nopreg when samantha and not samantha_pregnant
        group samantha_water auto variant preg when samantha and samantha_pregnant


        attribute bree null
        group bree auto

        attribute bree_pregnant variant bree_bath when bree and bree_bath
        attribute bree_pregnant variant bree_pee when bree and bree_pee
        attribute bree_pregnant variant bree_brush when bree and bree_brush

        attribute bree_collar variant bree_bath when bree and bree_bath
        attribute bree_collar variant bree_pee when bree and bree_pee
        attribute bree_collar variant bree_brush when bree and bree_brush

        group multiple auto variant bree_piercings_bree_bath when bree and bree_bath
        group multiple auto variant bree_piercings_bree_pee when bree and bree_pee
        group multiple auto variant bree_piercings_bree_brush when bree and bree_brush

        group bree_top auto variant bree_pee when bree and bree_pee and not (bree_topless or bree_naked)
        group bree_bot auto variant bree_pee when bree and bree_pee and not (bree_bottomless or bree_naked)
        group bree_top auto variant nopreg_bree_brush when bree and bree_brush and not (bree_pregnant or bree_topless or bree_naked)
        group bree_top auto variant preg_bree_brush when bree and bree_brush and bree_pregnant and not (bree_topless or bree_naked)

        attribute bree_nohaircut variant bree_bath when bree and bree_bath
        attribute bree_nohaircut variant bree_pee when bree and bree_pee
        attribute bree_nohaircut variant bree_brush when bree and bree_brush
        attribute bree_haircut variant bree_bath when bree and bree_bath
        attribute bree_haircut variant bree_pee when bree and bree_pee
        attribute bree_haircut variant bree_brush when bree and bree_brush

        group bree_water auto variant nopreg when bree and not bree_pregnant
        group bree_water auto variant preg when bree and bree_pregnant


        attribute minami null
        group minami auto

        attribute minami_pregnant variant minami_shower when minami and minami_shower
        attribute minami_pregnant variant minami_brush when minami and minami_brush

        attribute minami_collar variant minami_shower when minami and minami_shower
        attribute minami_collar variant minami_brush when minami and minami_brush

        group multiple auto variant minami_piercings_minami_shower when minami and minami_shower
        group multiple auto variant minami_piercings_minami_brush when minami and minami_brush

        group minami_top auto variant minami_brush when minami and minami_brush and not (minami_topless or minami_naked)
        group minami_top auto variant minami_brush when minami and minami_brush and not (minami_bottomless or minami_naked)

        attribute minami_nohaircut variant minami_shower when minami and minami_shower
        attribute minami_nohaircut variant minami_brush when minami and minami_brush
        attribute minami_haircut variant minami_shower when minami and minami_shower
        attribute minami_haircut variant minami_brush when minami and minami_brush


        attribute sasha null
        group sasha auto

        attribute sasha_pregnant variant sasha_shower when sasha and sasha_shower
        attribute sasha_pregnant variant sasha_pee when sasha and sasha_pee
        attribute sasha_pregnant variant sasha_brush when sasha and sasha_brush

        attribute sasha_collar variant sasha_shower when sasha and sasha_shower
        attribute sasha_collar variant sasha_pee when sasha and sasha_pee
        attribute sasha_collar variant sasha_brush when sasha and sasha_brush

        attribute sasha_boobjob variant sasha_pee when sasha and sasha_pee
        attribute sasha_boobjob variant sasha_brush when sasha and sasha_brush
        attribute sasha_noboobjob variant sasha_brush when sasha and sasha_brush

        attribute sasha_nohaircut variant sasha_shower when sasha and sasha_shower
        attribute sasha_haircut variant sasha_shower when sasha and sasha_shower

        attribute sasha_boobjob variant sasha_shower when sasha and sasha_shower

        group multiple auto variant sasha_piercings_sasha_shower when sasha and sasha_shower
        group multiple auto variant sasha_piercings_sasha_brush when sasha and sasha_brush
        group multiple auto variant sasha_piercings_nobb_sasha_shower when sasha and sasha_shower and sasha_noboobjob
        group multiple auto variant sasha_piercings_nobb_sasha_pee when sasha and sash_pee and sasha_noboobjob
        group multiple auto variant sasha_piercings_nobb_sasha_brush when sasha and sasha_brush and sasha_noboobjob
        group multiple auto variant sasha_piercings_bb_sasha_shower when sasha and sasha_shower and sasha_boobjob
        group multiple auto variant sasha_piercings_bb_sasha_pee when sasha and sasha_pee and sasha_boobjob
        group multiple auto variant sasha_piercings_bb_sasha_brush when sasha and sasha_brush and sasha_boobjob

        group sasha_top auto variant bb_sasha_pee when sasha and sasha_pee and sasha_boobjob and not (sasha_topless or sasha_naked)
        group sasha_top auto variant nobb_sasha_pee when sasha and sasha_pee and sasha_noboobjob and not (sasha_topless or sasha_naked)
        group sasha_bot auto variant sasha_pee when sasha and sasha_pee and not (sasha_bottomless or sasha_naked)
        group sasha_top auto variant nopreg_sasha_brush when sasha and sasha_brush and not (sasha_pregnant or sasha_topless or sasha_naked)
        group sasha_top auto variant preg_sasha_brush when sasha and sasha_brush and sasha_pregnant and not (sasha_topless or sasha_naked)
        group sasha_top auto variant nobb_nopreg_sasha_brush when sasha and sasha_brush and sasha_noboobjob and not (sasha_pregnant or sasha_topless or sasha_naked)
        group sasha_top auto variant nobb_preg_sasha_brush when sasha and sasha_brush and sasha_noboobjob and sasha_pregnant and not (sasha_topless or sasha_naked)
        group sasha_top auto variant bb_nopreg_sasha_brush when sasha and sasha_brush and sasha_boobjob and not (sasha_pregnant or sasha_topless or sasha_naked)
        group sasha_top auto variant bb_preg_sasha_brush when sasha and sasha_brush and sasha_boobjob and sasha_pregnant and not (sasha_topless or sasha_naked)

        attribute sasha_nohaircut variant sasha_pee when sasha and sasha_pee
        attribute sasha_nohaircut variant sasha_brush when sasha and sasha_brush
        attribute sasha_haircut variant sasha_pee when sasha and sasha_pee
        attribute sasha_haircut variant sasha_brush when sasha and sasha_brush

        group multiple auto variant sasha_piercings_ontop_sasha_pee when sasha and sasha_pee
        group multiple auto variant sasha_piercings_ontop_sasha_brush when sasha and sasha_brush
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
