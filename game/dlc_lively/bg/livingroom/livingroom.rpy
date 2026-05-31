init 5 python:
    class LivingroomPicker(object):
        def __call__(self, attr):
            
            
            if (game.calendar.is_today("fall", 31) and game.hour >= 8 or
            game.calendar.is_today("winter", 1) and game.hour < 6):
                attr.add("halloween_decor")
            elif (game.calendar.is_today("winter", 25) and game.hour >= 8 or
            game.calendar.is_today("winter", 26) and game.hour < 6):
                attr.add("christmas_decor")
            else:
                attr.add(game.calendar.season_name)
            
            if not persistent.lively_bg or attr & {"empty"}:
                if Harem.find('lexi', name='home'):
                    attr.add("blanket")
                    if lexi.room == "livingroom" and lexi.activity["activity"] == "sleep":
                        attr.add('lexi_sleep')
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"LivingroomPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not lexi.hidden and Harem.find('lexi', name='home'):
                    attr.add("blanket")
                    if lexi.room == "livingroom":
                        if lexi.activity["activity"] == "sleep":
                            attr.add('lexi_sleep')
                        else:
                            attr.add('lexi')
                
                
                if "lexi_sleep" not in attr:
                    if not samantha.hidden and samantha.room == "livingroom" and Harem.find('samantha', name='home'):
                        attr.add('samantha')
                    if not minami.hidden and minami.room == "livingroom":
                        attr.add('minami')
                    if not sasha.hidden and sasha.room == "livingroom":
                        attr.add('sasha')
                
                
                if not bree.hidden and bree.room == "livingroom":
                    attr.add('bree')
            
            
            if active_girl.id in ["bree", "lexi", "minami", "samantha", "sasha"]:
                if enable_debug_picker:
                    renpy.log(f"LivingroomPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"LivingroomPicker result: {attr}")
            return attr

    Room.find("livingroom").lively_npc = ["bree", "sasha", "minami", 'samantha', "lexi"]

init 6:
    layeredimage bg livingroom:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, LivingroomPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute blanket null
        attribute lexi null
        attribute lexi_sleep null

        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always "snow"
        group season_fg auto variant "day" if_any "day"
        group season_fg auto variant "night" if_any "night"

        group blanket if_any "blanket":
            attribute day "bg_livingroom_blanket_day"
            attribute night "bg_livingroom_blanket_night"

        group lexi if_any "lexi_sleep":
            attribute day "bg_livingroom_lexi_day"
            attribute night "bg_livingroom_lexi_night"

        group npc auto

        group pregnancy auto

        attribute sasha_boobjob
        attribute sasha_noboobjob null

        group collars auto

        group multiple auto variant piercings
        group multiple:
            attribute bree_clit null
            attribute bree_pregnant_navel null
            attribute bree_navel null
            attribute bree_tongue null
            attribute lexi_tongue null
            attribute minami_clit null
            attribute minami_ears null
            attribute minami_pregnant_navel null
            attribute minami_navel null
            attribute minami_nipples null
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_pregnant_navel null
            attribute samantha_navel null
            attribute samantha_tongue null
            attribute sasha_lips null
            attribute sasha_nose null
            attribute sasha_tongue null

        group outfit auto variant "bree" if_not "bree_pregnant"
        group outfit auto variant "lexi" if_not "lexi_pregnant"
        group outfit auto variant "minami" if_not "minami_pregnant"
        group outfit auto variant "sam" if_not "samantha_pregnant"
        group outfit auto variant "bb" if_any "sasha_boobjob" if_not "sasha_pregnant"
        group outfit auto variant "nobb" if_not ["sasha_boobjob", "sasha_pregnant"]
        group outfit auto variant "breepreg" if_any "bree_pregnant"
        group outfit auto variant "lexipreg" if_any "lexi_pregnant"
        group outfit auto variant "minamipreg" if_any "minami_pregnant"
        group outfit auto variant "sampreg" if_any "samantha_pregnant"
        group outfit auto variant "sashapreg_nobb" if_any "sasha_pregnant" if_not "sasha_boobjob"
        group outfit auto variant "sashapreg_bb" if_all ["sasha_pregnant", "sasha_boobjob"]

        group haircuts auto:
            attribute lexi_nohaircut null
            attribute samantha_nohaircut null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
