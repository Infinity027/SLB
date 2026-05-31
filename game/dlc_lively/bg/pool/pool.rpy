init 5 python:
    class PoolPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PoolPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "pool":
                    attr.add('bree')
                if not sasha.hidden and sasha.room == "pool":
                    attr.add('sasha')
                if not minami.hidden and minami.room == "pool":
                    attr.add('minami')
                if not samantha.hidden and samantha.room == "pool" and Harem.find('samantha', name='home'):
                    attr.add('samantha')
                if not lexi.hidden and lexi.room == "pool" and Harem.find('lexi', name='home'):
                    attr.add('lexi')
            
            
            if active_girl.id in ["bree", "sasha", "minami", "samantha", "lexi"]:
                if enable_debug_picker:
                    renpy.log(f"PoolPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PoolPicker result: {attr}")
            return attr

    Room.find("pool").lively_npc = ["bree", "sasha", "minami", 'samantha', "lexi"]

init 6:
    layeredimage bg pool:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, PoolPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute bree_topless null
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_tongue null
        attribute lexi_clit null
        attribute lexi_ears null
        attribute lexi_navel null
        attribute lexi_nipples null
        attribute lexi_nose null
        attribute lexi_pregnant_navel null
        attribute lexi_tongue null
        attribute minami_topless null
        attribute minami_collar null
        attribute minami_clit null
        attribute minami_ears null
        attribute minami_nose null
        attribute samantha_clit null
        attribute samantha_lips null
        attribute samantha_tongue null
        attribute sasha_topless null
        attribute sasha_pregnant null
        attribute sasha_clit null
        attribute sasha_ears null
        attribute sasha_lips null
        attribute sasha_navel null
        attribute sasha_pregnant_navel null
        attribute sasha_nipples null
        attribute sasha_noboobjob null
        attribute sasha_nose null
        attribute sasha_tongue null


        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"


        attribute sasha
        attribute sasha_boobjob when sasha
        attribute sasha_collar when sasha
        group sasha_bot auto when sasha and not (sasha_naked or sasha_bottomless)
        group sasha_top auto variant bb when sasha and sasha_boobjob and not (sasha_naked or sasha_topless)
        group sasha_top auto variant nobb when sasha and not (sasha_boobjob or sasha_naked or sasha_topless)
        group sasha_hair auto when sasha


        attribute lexi
        attribute lexi_pregnant when lexi
        attribute lexi_collar when lexi
        group lexi_bot auto when lexi and not (lexi_naked or lexi_bottomless)
        group lexi_top auto when lexi and not (lexi_naked or lexi_topless)
        attribute lexi_nohaircut when lexi


        attribute samantha
        attribute samantha_collar when samantha
        attribute samantha_pregnant when samantha
        group multiple auto variant piercings_samantha when samantha
        group samantha_bot auto when samantha and not (samantha_naked or samantha_bottomless)
        group samantha_top auto when samantha and not (samantha_naked or samantha_topless)
        group samantha_top auto variant preg when samantha and samantha_pregnant and not (samantha_naked or samantha_topless)
        group samantha_top auto variant nopreg when samantha and not (samantha_pregnant or samantha_naked or samantha_topless)
        attribute samantha_nohaircut when samantha


        attribute minami
        attribute minami_pregnant when minami
        group minami_hair auto when minami
        group multiple auto variant piercings_minami when minami
        group minami_bot auto when minami and not (minami_naked or minami_bottomless)
        group minami_top auto when minami and not (minami_naked or minami_topless)
        group minami_top auto variant preg when minami and minami_pregnant and not (minami_naked or minami_topless)
        group minami_top auto variant nopreg when minami and not (minami_pregnant or minami_naked or minami_topless)


        attribute bree
        attribute bree_pregnant when bree
        group multiple auto variant piercings_bree when bree
        group bree_hair auto when bree
        attribute bree_collar when bree
        group bree_bot auto when bree and not (bree_naked or bree_bottomless)
        group bree_bot auto variant preg when bree and bree_pregnant and not (bree_naked or bree_bottomless)
        group bree_bot auto variant nopreg when bree and not (bree_pregnant or bree_naked or bree_bottomless)
        group bree_top auto when bree and not (bree_naked or bree_topless)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
