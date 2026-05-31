init 5 python:
    class OfficePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"OfficePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.flags.gone_forever and ("audrey_event_05" not in DONE or "audrey_event_06" in DONE) and audrey.room == "office":
                    attr.add('audrey')
                if not lavish.hidden and lavish.room == "office":
                    attr.add('lavish')
                if not shiori.hidden and shiori.room == "office":
                    attr.add('shiori')
            
            
            if active_girl.id in ["audrey", "lavish", "shiori"]:
                if enable_debug_picker:
                    renpy.log(f"OfficePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"OfficePicker result: {attr}")
            return attr

    Room.find("office").lively_npc = ["audrey", "lavish", "shiori"]

init 6:
    layeredimage bg office:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, OfficePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute audrey_bottomless null
        attribute lavish_bottomless null
        attribute shiori_bottomless null
        attribute audrey_topless null
        attribute lavish_topless null
        attribute shiori_topless null
        attribute audrey_naked null
        attribute lavish_naked null
        attribute shiori_naked null
        attribute peace null
        attribute nopeace null
        attribute pressed null
        attribute notpressed null
        attribute audrey_collar null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_navel null
        attribute audrey_nipples null
        attribute audrey_nose null
        attribute audrey_pregnant_navel null
        attribute audrey_tongue null
        attribute lavish_clit null
        attribute lavish_ears null
        attribute lavish_lips null
        attribute lavish_navel null
        attribute lavish_nipples null
        attribute lavish_nohaircut null
        attribute lavish_nose null
        attribute lavish_pregnant null
        attribute lavish_pregnant_navel null
        attribute lavish_tongue null
        attribute shiori_clit null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_navel null
        attribute shiori_nose null
        attribute shiori_pregnant_navel null
        attribute shiori_tongue null

        attribute day "office_day"
        attribute night "office_night"


        attribute lavish
        attribute lavish_collar when lavish
        group bot_lavish auto when lavish and not (lavish_bottomless or lavish_naked)
        group top_lavish auto when lavish and not (lavish_topless or lavish_naked)


        attribute audrey
        attribute audrey_pregnant when audrey
        group bot_audrey auto variant nopreg when audrey and not (audrey_pregnant or audrey_bottomless or audrey_naked)
        group bot_audrey auto variant preg when audrey and audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group top_audrey auto variant nopreg when audrey and not (audrey_pregnant or audrey_topless or audrey_naked)
        group top_audrey auto variant preg when audrey and audrey_pregnant and not (audrey_topless or audrey_naked)
        attribute audrey_nohaircut when audrey


        attribute shiori
        attribute shiori_pregnant when shiori
        group multiple auto variant shiori_piercings when shiori
        group bot_shiori auto variant nopreg when shiori and not (shiori_pregnant or shiori_bottomless or shiori_naked)
        group bot_shiori auto variant preg when shiori and shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group top_shiori auto variant nopreg when shiori and not (shiori_pregnant or shiori_topless or shiori_naked)
        group top_shiori auto variant preg when shiori and shiori_pregnant and not (shiori_topless or shiori_naked)
        attribute shiori_collar when shiori
        attribute shiori_nohaircut when shiori
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
