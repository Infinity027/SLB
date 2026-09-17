init 5 python:
    class ParkPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"ParkPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.hidden and audrey.room == "park":
                    attr.add('audrey')
                if not emma.hidden and emma.room == "park":
                    attr.add('emma')
                if not harmony.hidden and harmony.room == "park":
                    attr.add('harmony')
                if not kat.hidden and kat.room == "park":
                    attr.add('kat')
                if not lavish.hidden and lavish.room == "park":
                    attr.add('lavish')
                if not palla.hidden and palla.room == "park":
                    attr.add('palla')
                if not shiori.hidden and shiori.room == "park":
                    attr.add('shiori')
            
            
            if active_girl.id in ["audrey", "emma", "harmony", "kat", "lavish", "palla", "shiori"]:
                if enable_debug_picker:
                    renpy.log(f"ParkPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"ParkPicker result: {attr}")
            return attr

    Room.find("park").lively_npc = ["audrey", "emma", "harmony", "kat", "lavish", "palla", "shiori"]

init 6:
    layeredimage bg park:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker,  CollarPicker, OutfitPicker, ParkPicker], append_npc_from_attributes=True)

        attribute empty null            
        attribute force_display null        
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute emma_lips null
        attribute emma_tongue null
        attribute harmony_clit null
        attribute harmony_navel null
        attribute harmony_tongue null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_nose null
        attribute kat_tongue null
        attribute lavish_tongue null
        attribute palla_ears null
        attribute palla_glasses null
        attribute palla_lips null
        attribute palla_tongue null
        attribute shiori_clit null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_navel null
        attribute shiori_tongue null
        attribute peace null
        attribute nopeace null
        attribute pressed null
        attribute notpressed null

        attribute day null
        attribute night null
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

        attribute shiori
       
        attribute shiori_collar when shiori
        group shiori_bot auto variant nopreg when shiori
        group shiori_top auto variant nopreg when shiori
        always "bg_park_shiori_nohaircut" when shiori


        attribute lavish
        attribute lavish_collar when lavish
        group lavish_bot auto variant nopreg when lavish
        group lavish_top auto variant nopreg when lavish
        always "bg_park_lavish_nohaircut" when lavish


        attribute emma
        attribute emma_collar when emma
        group emma_bot auto variant nopreg when emma
        group emma_top auto variant nopreg when emma
        always "bg_park_emma_nohaircut" when emma


        attribute harmony
       
        attribute harmony_collar when harmony
        group harmony_bot auto variant nopreg when harmony
        group harmony_top auto variant nopreg when harmony
        always "bg_park_harmony_nohaircut" when harmony

        attribute kat
       
        attribute kat_collar when kat
        group kat_bot auto variant nopreg when kat
        group kat_top auto variant nopreg when kat
        always "bg_park_kat_nohaircut" when kat

        attribute palla
       
        attribute palla_collar when palla
        group palla_bot auto variant nopreg when palla
        group palla_top auto variant nopreg when palla
        always "bg_park_palla_nohaircut" when palla

        attribute audrey
        attribute audrey_collar when audrey
        group audrey_bot auto variant nopreg when audrey
        group audrey_top auto variant nopreg when audrey
        always "bg_park_audrey_nohaircut" when audrey