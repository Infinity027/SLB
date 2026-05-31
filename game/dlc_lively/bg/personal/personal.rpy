init 5 python:
    class PersonalPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PersonalPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.flags.gone_forever and ("audrey_event_05" not in DONE or "audrey_event_06" in DONE) and audrey.room == "personal":
                    attr.add('audrey')
                if not cassidy.hidden and cassidy.room == "personal":
                    attr.add('cassidy')
                if not lavish.hidden and lavish.room == "personal":
                    attr.add('lavish')
                if not shiori.hidden and shiori.room == "personal":
                    attr.add('shiori')
            
            
            if active_girl.id in ["audrey", "cassidy", "lavish", "shiori"]:
                if enable_debug_picker:
                    renpy.log(f"PersonalPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PersonalPicker result: {attr}")
            return attr

    Room.find("personal").lively_npc = ["audrey", "cassidy", "lavish", "shiori"]

init 6:
    layeredimage bg personal:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, PersonalPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute audrey_naked null
        attribute audrey_topless null
        attribute audrey_bottomless null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute cassidy_naked null
        attribute cassidy_topless null
        attribute cassidy_bottomless null
        attribute cassidy_ears null
        attribute cassidy_lips null
        attribute cassidy_nose null
        attribute cassidy_tongue null
        attribute lavish_naked null
        attribute lavish_topless null
        attribute lavish_bottomless null
        attribute lavish_clit null
        attribute lavish_tongue null
        attribute shiori_naked null
        attribute shiori_topless null
        attribute shiori_bottomless null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_tongue null
        attribute nopeace null
        attribute peace null
        attribute pressed null
        attribute notpressed null


        attribute day "personal_day"
        attribute night "personal_night"


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        group multiple auto variant audrey_piercings when audrey
        group audrey_bot auto variant preg when audrey and audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group audrey_bot auto variant nopreg when audrey and not audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group audrey_top auto variant preg when audrey and audrey_pregnant and not (audrey_topless or audrey_naked)
        group audrey_top auto variant nopreg when audrey and not audrey_pregnant and not (audrey_topless or audrey_naked)
        always "bg_personal_audrey_nohaircut" when audrey


        attribute lavish
        attribute lavish_pregnant when lavish
        attribute lavish_collar when lavish
        always "bg_personal_lavish_nohaircut" when lavish
        group multiple auto variant lavish_piercings when lavish
        group lavish_bot auto variant preg when lavish and lavish_pregnant and not (lavish_bottomless or lavish_naked)
        group lavish_bot auto variant nopreg when lavish and not lavish_pregnant and not (lavish_bottomless or lavish_naked)
        group lavish_top auto variant preg when lavish and lavish_pregnant and not (lavish_topless or lavish_naked)
        group lavish_top auto variant nopreg when lavish and not lavish_pregnant and not (lavish_topless or lavish_naked)


        attribute shiori
        attribute shiori_pregnant when shiori
        attribute shiori_collar when shiori
        always "bg_personal_shiori_nohaircut" when shiori
        group multiple auto variant shiori_piercings when shiori
        group shiori_bot auto variant preg when shiori and shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group shiori_bot auto variant nopreg when shiori and not shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group shiori_top auto variant preg when shiori and shiori_pregnant and not (shiori_topless or shiori_naked)
        group shiori_top auto variant nopreg when shiori and not shiori_pregnant and not (shiori_topless or shiori_naked)


        attribute cassidy
        attribute cassidy_pregnant when cassidy
        attribute cassidy_collar when cassidy
        group multiple auto variant cassidy_piercings when cassidy
        group cassidy_bot auto variant preg when cassidy and cassidy_pregnant and not (cassidy_bottomless or cassidy_naked)
        group cassidy_bot auto variant nopreg when cassidy and not cassidy_pregnant and not (cassidy_bottomless or cassidy_naked)
        group cassidy_top auto variant preg when cassidy and cassidy_pregnant and not (cassidy_topless or cassidy_naked)
        group cassidy_top auto variant nopreg when cassidy and not cassidy_pregnant and not (cassidy_topless or cassidy_naked)
        always "bg_personal_cassidy_nohaircut" when cassidy
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
