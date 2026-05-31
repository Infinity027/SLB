init 5 python:
    class BreakroomPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"BreakroomPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "breakroom":
                    attr.add('aletta')
                if not audrey.flags.gone_forever and ("audrey_event_05" not in DONE or "audrey_event_06" in DONE) and audrey.room == "breakroom":
                    attr.add('audrey')
                if not cassidy.hidden and cassidy.room == "breakroom":
                    attr.add('cassidy')
                if not lavish.hidden and lavish.room == "breakroom":
                    attr.add('lavish')
                if not shiori.hidden and shiori.room == "breakroom":
                    attr.add('shiori')
            
            
            if active_girl.id in ["aletta", "audrey", "cassidy", "lavish", "shiori"]:
                if enable_debug_picker:
                    renpy.log(f"BreakroomPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"BreakroomPicker result: {attr}")
            return attr

    Room.find("breakroom").lively_npc = ["aletta", "audrey", "cassidy", "lavish", "shiori"]

init 6:
    layeredimage bg breakroom:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, BreakroomPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute aletta_naked null
        attribute aletta_topless null
        attribute aletta_bottomless null
        attribute aletta_clit null
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_nose null
        attribute aletta_tongue null
        attribute audrey_naked null
        attribute audrey_topless null
        attribute audrey_bottomless null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_navel null
        attribute audrey_nipples null
        attribute audrey_nose null
        attribute audrey_pregnant_navel null
        attribute audrey_tongue null
        attribute cassidy_naked null
        attribute cassidy_topless null
        attribute cassidy_bottomless null
        attribute cassidy_clit null
        attribute cassidy_ears null
        attribute cassidy_navel null
        attribute cassidy_nose null
        attribute cassidy_pregnant_navel null
        attribute cassidy_tongue null
        attribute lavish_naked null
        attribute lavish_topless null
        attribute lavish_bottomless null
        attribute lavish_clit null
        attribute lavish_navel null
        attribute lavish_pregnant_navel null
        attribute lavish_tongue null
        attribute shiori_naked null
        attribute shiori_topless null
        attribute shiori_bottomless null
        attribute shiori_clit null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_navel null
        attribute shiori_nipples null
        attribute shiori_nose null
        attribute shiori_pregnant_navel null
        attribute shiori_tongue null
        attribute peace null
        attribute nopeace null
        attribute notpressed null
        attribute pressed null


        attribute day "breakroom_day"
        attribute night "breakroom_night"


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        group bot_audrey auto variant nopreg when audrey and not (audrey_pregnant or audrey_bottomless or audrey_naked)
        group bot_audrey auto variant preg when audrey and audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group top_audrey auto variant nopreg when audrey and not (audrey_pregnant or audrey_topless or audrey_naked)
        group top_audrey auto variant preg when audrey and audrey_pregnant and not (audrey_topless or audrey_naked)
        always "bg_breakroom_audrey_hair" when audrey


        attribute cassidy
        attribute cassidy_collar when cassidy
        group multiple auto variant piercings_cassidy when cassidy
        group bot_cassidy auto when cassidy and not (cassidy_bottomless or cassidy_naked)
        group top_cassidy auto when cassidy and not (cassidy_topless or cassidy_naked)
        always "bg_breakroom_cassidy_hair" when cassidy


        attribute shiori
        attribute shiori_pregnant when shiori
        attribute shiori_collar when shiori
        group multiple auto variant piercings_shiori when shiori
        group bot_shiori auto variant nopreg when shiori and not (shiori_pregnant or shiori_bottomless or shiori_naked)
        group bot_shiori auto variant preg when shiori and shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group top_shiori auto variant nopreg when shiori and not (shiori_pregnant or shiori_topless or shiori_naked)
        group top_shiori auto variant preg when shiori and shiori_pregnant and not (shiori_topless or shiori_naked)
        always "bg_breakroom_shiori_hair" when shiori


        attribute lavish
        attribute lavish_pregnant when lavish
        attribute lavish_collar when lavish
        group multiple auto variant piercings_lavish when lavish
        group bot_lavish auto variant nopreg when lavish and not (lavish_pregnant or lavish_bottomless or lavish_naked)
        group bot_lavish auto variant preg when lavish and lavish_pregnant and not (lavish_bottomless or lavish_naked)
        group top_lavish auto variant nopreg when lavish and not (lavish_pregnant or lavish_topless or lavish_naked)
        group top_lavish auto variant preg when lavish and lavish_pregnant and not (lavish_topless or lavish_naked)
        always "bg_breakroom_lavish_hair" when lavish


        attribute aletta
        attribute aletta_pregnant when aletta
        attribute aletta_collar when aletta
        group multiple auto variant piercings_aletta when aletta
        group bot_aletta auto variant nopreg when aletta and not (aletta_pregnant or aletta_bottomless or aletta_naked)
        group bot_aletta auto variant preg when aletta and aletta_pregnant and not (aletta_bottomless or aletta_naked)
        group top_aletta auto variant nopreg when aletta and not (aletta_pregnant or aletta_topless or aletta_naked)
        group top_aletta auto variant preg when aletta and aletta_pregnant and not (aletta_topless or aletta_naked)
        attribute aletta_glasses when aletta
        group aletta_hair auto when aletta
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
