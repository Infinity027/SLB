init 5 python:
    class DrugstorePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"DrugstorePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not anna.flags.gone_forever and anna.room == "drugstore":
                    attr.add('anna')
                if not shiori.flags.gone_forever and shiori.room == "drugstore":
                    attr.add('shiori')
                if not kat.flags.gone_forever and kat.room == "drugstore":
                    attr.add('kat')
                if not reona.flags.gone_forever and reona.room == "drugstore":
                    attr.add('reona')
            
            
            if active_girl.id in ["anna", "shiori", "kat", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"DrugstorePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"DrugstorePicker result: {attr}")
            return attr

    Room.find("drugstore").lively_npc = ["anna", "shiori", "kat", "reona"]

init 6:
    layeredimage bg drugstore:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, DrugstorePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute anna_ears null
        attribute anna_nose null
        attribute anna_tongue null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_nose null
        attribute kat_tongue null
        attribute peace null
        attribute nopeace null
        attribute pressed null
        attribute notpressed null
        attribute reona_clit null
        attribute reona_innersexy null
        attribute reona_navel null
        attribute reona_pregnant_navel null
        attribute reona_nose null
        attribute reona_tongue null
        attribute shiori_clit null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_tongue null


        always "drugstore"


        attribute anna
        attribute anna_collar when anna
        attribute anna_nohaircut when anna
        attribute anna_pregnant when anna
        group multiple auto variant anna_piercings
        group anna_bot auto variant nopreg when anna and not anna_pregnant
        group anna_bot auto variant preg when anna and anna_pregnant
        group anna_top auto variant nopreg when anna and not anna_pregnant
        group anna_top auto variant preg when anna and anna_pregnant


        attribute shiori
        attribute shiori_pregnant when shiori
        group multiple auto variant shiori_piercings
        group shiori_top auto variant nopreg when shiori and not shiori_pregnant
        group shiori_top auto variant preg when shiori and shiori_pregnant
        attribute shiori_collar when shiori
        attribute shiori_nohaircut when shiori


        attribute kat
        attribute kat_pregnant when kat
        group multiple auto variant kat_piercings
        group kat_bot auto variant nopreg when kat and not kat_pregnant
        group kat_bot auto variant preg when kat and kat_pregnant
        group kat_top auto variant nopreg when kat and not kat_pregnant
        group kat_top auto variant preg when kat and kat_pregnant
        attribute kat_collar when kat
        attribute kat_nohaircut when kat


        attribute reona
        attribute reona_pregnant when reona
        group multiple auto variant reona_piercings
        attribute reona_collar when reona
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_hair auto when reona
        attribute reona_pureglasses when reona
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
