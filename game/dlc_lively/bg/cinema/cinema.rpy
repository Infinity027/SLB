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
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, CinemaPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute aletta_clit null
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_navel null
        attribute aletta_nipples null
        attribute aletta_nose null
        attribute aletta_pregnant_navel null
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
        attribute claire_pregnant_navel null
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
        attribute reona_pregnant_navel null
        attribute reona_tongue null


        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always "snow"


        attribute morgan
        attribute morgan_pregnant when morgan
        attribute morgan_collar when morgan
        group multiple auto variant morgan_piercings when morgan
        group morgan_bot auto variant preg when morgan and morgan_pregnant
        group morgan_bot auto variant nopreg when morgan and not morgan_pregnant
        group morgan_top auto variant preg when morgan and morgan_pregnant
        group morgan_top auto variant nopreg when morgan and not morgan_pregnant
        group morgan_hair auto when morgan


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        group multiple auto variant reona_piercings when reona
        group reona_top variant preg when reona and reona_pregnant:
            attribute reona_casual
        group reona_top variant nopreg when reona and not reona_pregnant:
            attribute reona_casual
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_top variant preg when reona and reona_pregnant:
            attribute reona_purecasual
        group reona_top variant nopreg when reona and not reona_pregnant:
            attribute reona_purecasual
        attribute reona_pureglasses when reona
        group reona_hair auto when reona


        attribute minami
        attribute minami_pregnant when minami
        attribute minami_collar when minami
        group multiple auto variant minami_piercings when minami
        group minami_bot auto variant preg when minami and minami_pregnant
        group minami_bot auto variant nopreg when minami and not minami_pregnant
        group minami_top auto variant preg when minami and minami_pregnant
        group minami_top auto variant nopreg when minami and not minami_pregnant
        group minami_hair auto when minami


        attribute camila
        attribute camila_pregnant when camila
        attribute camila_collar when camila
        group multiple auto variant camila_piercings when camila
        group camila_bot auto variant preg when camila and camila_pregnant
        group camila_bot auto variant nopreg when camila and not camila_pregnant
        group camila_top auto variant preg when camila and camila_pregnant
        group camila_top auto variant nopreg when camila and not camila_pregnant
        group camila_hair auto when camila


        attribute amy
        attribute amy_pregnant when amy
        attribute amy_collar when amy
        group multiple auto variant amy_piercings when amy
        group amy_bot auto variant preg when amy and amy_pregnant
        group amy_bot auto variant nopreg when amy and not amy_pregnant
        group amy_top auto variant preg when amy and amy_pregnant
        group amy_top auto variant nopreg when amy and not amy_pregnant
        attribute amy_nohaircut when amy


        attribute kat
        attribute kat_pregnant when kat
        attribute kat_collar when kat
        group multiple auto variant kat_piercings when kat
        group kat_bot auto variant preg when kat and kat_pregnant
        group kat_bot auto variant nopreg when kat and not kat_pregnant
        group kat_top auto variant preg when kat and kat_pregnant
        group kat_top auto variant nopreg when kat and not kat_pregnant
        attribute kat_nohaircut when kat


        attribute lavish
        attribute lavish_pregnant when lavish
        attribute lavish_collar when lavish
        group multiple auto variant lavish_piercings when lavish
        group lavish_bot auto variant preg when lavish and lavish_pregnant
        group lavish_bot auto variant nopreg when lavish and not lavish_pregnant
        group lavish_top auto variant preg when lavish and lavish_pregnant
        group lavish_top auto variant nopreg when lavish and not lavish_pregnant
        attribute lavish_nohaircut when lavish


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant
        group claire_hair auto when claire


        attribute aletta
        attribute aletta_pregnant when aletta
        attribute aletta_collar when aletta
        group aletta_bot auto variant preg when aletta and aletta_pregnant
        group aletta_bot auto variant nopreg when aletta and not aletta_pregnant
        group aletta_top auto variant preg when aletta and aletta_pregnant
        group aletta_top auto variant nopreg when aletta and not aletta_pregnant
        attribute aletta_glasses when aletta
        group aletta_hair auto when aletta
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
