init 5 python:
    class BeachPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"BeachPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "beach":
                    attr.add('aletta')
                if not alexis.flags.gone_forever and alexis.room == "beach":
                    attr.add('alexis')
                if not cassidy.flags.gone_forever and cassidy.room == "beach":
                    attr.add('cassidy')
                if not lavish.flags.gone_forever and lavish.room == "beach":
                    attr.add('lavish')
                if not reona.flags.gone_forever and reona.room == "beach":
                    attr.add('reona')
            
            
            if active_girl.id in ["aletta", "alexis", "cassidy", "lavish", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"BeachPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"BeachPicker result: {attr}")
            return attr

    Room.find("beach").lively_npc = ["aletta", "alexis", "cassidy", "lavish", "reona"]

init 6:
    layeredimage bg beach:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, BeachPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute aletta_clit null
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_naked null
        attribute aletta_nose null
        attribute aletta_tongue null
        attribute alexis_naked null
        attribute alexis_nipples null
        attribute cassidy_ears null
        attribute cassidy_naked null
        attribute cassidy_nose null
        attribute cassidy_tongue null
        attribute lavish_ears null
        attribute lavish_naked null
        attribute lavish_tongue null
        attribute reona_innersexy null
        attribute reona_naked null
        attribute reona_tongue null


        attribute day "beach_day"
        attribute night "beach_night"


        attribute reona
        attribute reona_pregnant when reona
        group multiple auto variant reona_piercings when reona
        group reona_hair auto when reona
        attribute reona_pureglasses when reona
        group reona_bot auto variant nopreg when reona and not reona_pregnant and not reona_naked
        group reona_bot auto variant preg when reona and reona_pregnant and not reona_naked
        group reona_top auto when reona and not reona_naked
        attribute reona_collar when reona


        attribute lavish
        attribute lavish_nohaircut when lavish
        attribute lavish_pregnant when lavish
        group multiple auto variant lavish_piercings when lavish
        group lavish_top auto variant nopreg when lavish and not lavish_pregnant and not lavish_naked
        group lavish_top auto variant preg when lavish and lavish_pregnant and not lavish_naked
        attribute lavish_collar when lavish


        attribute aletta
        attribute aletta_collar when aletta
        attribute aletta_pregnant when aletta
        group multiple auto variant aletta_piercings when aletta
        group aletta_bot auto variant nopreg when aletta and not aletta_pregnant and not aletta_naked
        group aletta_bot auto variant preg when aletta and aletta_pregnant and not aletta_naked
        group aletta_top auto variant nopreg when aletta and not aletta_pregnant and not aletta_naked
        group aletta_top auto variant preg when aletta and aletta_pregnant and not aletta_naked
        group aletta_hair auto when aletta
        attribute aletta_glasses when aletta


        attribute alexis
        attribute alexis_pregnant when alexis
        attribute alexis_nohaircut when alexis
        group multiple auto variant alexis_piercings when alexis
        group alexis_bot auto variant nopreg when alexis and not alexis_pregnant and not alexis_naked
        group alexis_bot auto variant preg when alexis and alexis_pregnant and not alexis_naked
        group alexis_top auto when alexis and not alexis_naked
        group alexis_top auto variant nopreg when alexis and not alexis_pregnant and not alexis_naked
        group alexis_top auto variant preg when alexis and alexis_pregnant and not alexis_naked
        attribute alexis_collar when alexis


        attribute cassidy
        attribute cassidy_collar when cassidy
        attribute cassidy_nohaircut when cassidy
        attribute cassidy_pregnant when cassidy
        group multiple auto variant cassidy_piercings when cassidy
        group cassidy_bot auto variant nopreg when cassidy and not cassidy_pregnant and not cassidy_gold and not cassidy_naked
        group cassidy_bot auto variant preg when cassidy and cassidy_pregnant and not cassidy_gold and not cassidy_naked
        group cassidy_bot auto variant nopreg_gold when cassidy and not cassidy_pregnant and cassidy_gold and not cassidy_naked
        group cassidy_bot auto variant preg_gold when cassidy and cassidy_pregnant and cassidy_gold and not cassidy_naked
        group cassidy_top auto variant nopreg when cassidy and not cassidy_pregnant and not cassidy_gold and not cassidy_naked
        group cassidy_top auto variant preg when cassidy and cassidy_pregnant and not cassidy_gold and not cassidy_naked
        group cassidy_top auto variant nopreg_gold when cassidy and not cassidy_pregnant and cassidy_gold and not cassidy_naked
        group cassidy_top auto variant preg_gold when cassidy and cassidy_pregnant and cassidy_gold and not cassidy_naked
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
