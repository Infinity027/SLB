init 5 python:
    class KitchenPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"KitchenPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "kitchen":
                    attr.add('bree')
                if not sasha.hidden and sasha.room == "kitchen":
                    attr.add('sasha')
                if not minami.hidden and minami.room == "kitchen":
                    attr.add('minami')
                if not samantha.hidden and samantha.room == "kitchen" and Harem.find('samantha', name='home'):
                    attr.add('samantha')
                if not lexi.hidden and lexi.room == "kitchen" and Harem.find('lexi', name='home'):
                    attr.add('lexi')
            
            
            if active_girl.id in ["bree", "sasha", "minami", "samantha", "lexi"]:
                if enable_debug_picker:
                    renpy.log(f"KitchenPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"KitchenPicker result: {attr}")
            return attr

    Room.find("kitchen").lively_npc = ["bree", "sasha", "minami", 'samantha', "lexi"]

init 6:
    layeredimage bg kitchen:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, KitchenPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute topless null
        attribute bottomless null
        attribute naked null
        attribute bree_clit null
        attribute bree_collar null
        attribute bree_ears null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_nipples null
        attribute bree_nose null
        attribute bree_pregnant null
        attribute bree_pregnant_navel null
        attribute bree_tongue null
        attribute minami_clit null
        attribute minami_ears null
        attribute minami_navel null
        attribute minami_nipples null
        attribute minami_nose null
        attribute minami_pregnant null
        attribute minami_pregnant_navel null
        attribute lexi_tongue null
        attribute samantha_clit null
        attribute samantha_ears null
        attribute samantha_lips null
        attribute samantha_navel null
        attribute samantha_pregnant null
        attribute samantha_pregnant_navel null
        attribute samantha_tongue null
        attribute sasha_clit null
        attribute sasha_lips null
        attribute sasha_navel null
        attribute sasha_tongue null

        attribute bree_topless null
        attribute lexi_topless null
        attribute minami_topless null
        attribute samantha_topless null
        attribute sasha_topless null

        attribute day "kitchen_day"
        attribute night "kitchen_night"


        attribute bree
        attribute bree_pregnant when bree
        group bree_bot auto when bree and not (bottomless or naked)
        group bree_top auto when bree and not bree_pregnant and not (bree_topless or bree_naked)
        group bree_top auto variant pregnant when bree and bree_pregnant and not (bree_topless or bree_naked)
        group bree_hair auto when bree


        attribute samantha
        group multiple auto variant samantha_piercings when samantha
        attribute samantha_collar when samantha
        group samantha_bot auto when samantha and not (samantha_bottomless or samantha_naked)
        group samantha_top auto when samantha and not (samantha_topless or samantha_naked)
        attribute samantha_nohaircut when samantha


        attribute sasha null
        group sasha_body auto when sasha
        group sasha_preg auto variant bb when sasha and sasha_boobjob
        group sasha_preg auto variant nobb when sasha and sasha_noboobjob
        group multiple auto variant sasha_piercings_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_nobb when sasha and sasha_noboobjob
        group sasha_bot auto when sasha and not (sasha_bottomless or sasha_naked)
        group sasha_top_bb auto when sasha and not sasha_pregnant and sasha_boobjob and not (sasha_topless or sasha_naked)
        group sasha_top_nobb auto when sasha and not sasha_pregnant and sasha_noboobjob and not (sasha_topless or sasha_naked)
        group sasha_top_pregnant_bb auto when sasha and sasha_pregnant and sasha_boobjob and not (sasha_topless or sasha_naked)
        group sasha_top_pregnant_nobb auto when sasha and sasha_pregnant and sasha_noboobjob and not (sasha_topless or sasha_naked)
        group sasha_hair auto when sasha
        attribute sasha_collar when sasha
        group multiple auto variant sasha_piercings when sasha


        attribute lexi
        group multiple auto variant lexi_piercings when lexi
        attribute lexi_collar when lexi
        group lexi_bot auto when lexi and not lexi_pregnant and not (lexi_bottomless or lexi_naked)
        group lexi_bot auto variant pregnant when lexi and lexi_pregnant and not (lexi_bottomless or lexi_naked)
        attribute lexi_pregnant when lexi
        group lexi_top auto when lexi and not lexi_pregnant and not (lexi_topless or lexi_naked)
        attribute lexi_nohaircut when lexi
        group multiple auto variant lexi_piercings_front when lexi


        attribute minami
        attribute minami_collar when minami
        attribute minami_pregnant when minami
        group minami_bot auto when minami and not minami_pregnant and not (minami_bottomless or minami_naked)
        group minami_bot auto variant pregnant when minami and minami_pregnant and not (minami_bottomless or minami_naked)
        group minami_top auto when minami and not minami_pregnant and not (minami_topless or minami_naked)
        group minami_top auto variant pregnant when minami and minami_pregnant and not (minami_topless or minami_naked)
        group minami_hair auto when minami
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
