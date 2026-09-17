init 5 python:
    class CinemaPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"CinemaPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "cinema":
                    attr.add('aletta')
                if not amy.flags.gone_forever and amy.room == "cinema":
                    attr.add('amy')
                if not camila.flags.gone_forever and camila.room == "cinema":
                    attr.add('camila')
                if not claire.flags.gone_forever and claire.room == "cinema":
                    attr.add('claire')
                if not kat.flags.gone_forever and kat.room == "cinema":
                    attr.add('kat')
                if not lavish.flags.gone_forever and lavish.room == "cinema":
                    attr.add('lavish')
                if not minami.hidden and minami.room == "cinema":
                    attr.add('minami')
                if not morgan.flags.gone_forever and morgan.room == "cinema":
                    attr.add('morgan')
                if not reona.flags.gone_forever and reona.room == "cinema":
                    attr.add('reona')
            
            
            if active_girl.id in ["aletta", "amy", "camila", "claire", "kat", "lavish", "minami", "morgan", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"CinemaPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"CinemaPicker result: {attr}")
            return attr

    Room.find("cinema").lively_npc = ["aletta", "amy", "camila", "claire", "kat", "lavish", "minami", "morgan", "reona"]

init 6:
    layeredimage bg cinema:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker,  CollarPicker, OutfitPicker, HaircutPicker, CinemaPicker], append_npc_from_attributes=True)

        attribute empty null            
        attribute force_display null        
        attribute aletta_clit null
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_navel null
        attribute aletta_nipples null
        attribute aletta_nose null
        attribute aletta_tongue null
        attribute amy_nipples null
        attribute camila_ears null
        attribute camila_lips null
        attribute camila_nose null
        attribute camila_tongue null
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nipples null
        attribute claire_nose null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_tongue null
        attribute lavish_clit null
        attribute lavish_nose null
        attribute lavish_tongue null
        attribute minami_clit null
        attribute minami_ears null
        attribute minami_nipples null
        attribute minami_nose null
        attribute morgan_tongue null
        attribute reona_clit null
        attribute reona_navel null
        attribute reona_nose null
        attribute reona_tongue null

        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always "snow"

        attribute morgan
        attribute morgan_collar when morgan
        group morgan_bot auto variant nopreg when morgan
        group morgan_top auto variant nopreg when morgan
        group morgan_hair auto when morgan

        attribute reona
        attribute reona_collar when reona
        group reona_bot auto variant nopreg when reona
        attribute reona_pureglasses when reona
        group reona_hair auto when reona

        attribute minami
        attribute minami_collar when minami
        group minami_bot auto variant nopreg when minami
        group minami_top auto variant nopreg when minami
        group minami_hair auto when minami

        attribute camila
        attribute camila_collar when camila
        group camila_bot auto variant nopreg when camila
        group camila_top auto variant nopreg when camila
        group camila_hair auto when camila


        attribute amy
        attribute amy_collar when amy
        group amy_bot auto variant nopreg when amy
        group amy_top auto variant nopreg when amy
        attribute amy_nohaircut when amy


        attribute kat
        attribute kat_collar when kat
        group kat_bot auto variant nopreg when kat
        group kat_top auto variant nopreg when kat
        attribute kat_nohaircut when kat


        attribute lavish
        attribute lavish_collar when lavish
        group lavish_bot auto variant nopreg when lavish
        group lavish_top auto variant nopreg when lavish
        attribute lavish_nohaircut when lavish


        attribute claire
        attribute claire_collar when claire
        group claire_bot auto variant nopreg when claire
        group claire_top auto variant nopreg when claire
        group claire_hair auto when claire


        attribute aletta
        attribute aletta_collar when aletta
        group aletta_bot auto variant nopreg when aletta
        group aletta_top auto variant nopreg when aletta
        attribute aletta_glasses when aletta
        group aletta_hair auto when aletta
