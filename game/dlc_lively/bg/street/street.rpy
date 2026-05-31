init 5 python:
    class StreetPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"StreetPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not anna.flags.gone_forever and anna.room == "street":
                    attr.add('anna')
                if not camila.flags.gone_forever and camila.room == "street":
                    attr.add('camila')
                if not claire.flags.gone_forever and claire.room == "street":
                    attr.add('claire')
                if not harmony.flags.gone_forever and harmony.room == "street":
                    attr.add('harmony')
                if not kat.flags.gone_forever and kat.room == "street":
                    attr.add('kat')
            
            
            if active_girl.id in ["anna", "camila", "harmony", "kat"]:
                if enable_debug_picker:
                    renpy.log(f"StreetPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"StreetPicker result: {attr}")
            return attr

    Room.find("street").lively_npc = ["anna", "camila", "claire", "harmony", "kat"]

init 6:
    layeredimage bg street:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, StreetPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute anna_ears null
        attribute anna_nose null
        attribute anna_tongue null
        attribute camila_clit null
        attribute camila_lips null
        attribute camila_nose null
        attribute camila_tongue null
        attribute claire_clit null
        attribute harmony_clit null
        attribute harmony_navel null
        attribute harmony_nipples null
        attribute harmony_nose null
        attribute harmony_pregnant_navel null
        attribute harmony_tongue null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_nose null
        attribute kat_tongue null


        attribute day null
        attribute night null
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group claire_hair auto when claire
        group multiple auto variant claire_piercings when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant


        attribute harmony
        attribute harmony_pregnant when harmony
        attribute harmony_collar when harmony
        group multiple auto variant harmony_piercings_back when harmony
        group harmony_bot auto variant preg when harmony and harmony_pregnant
        group harmony_bot auto variant nopreg when harmony and not harmony_pregnant
        group harmony_top auto variant preg when harmony and harmony_pregnant
        group harmony_top auto variant nopreg when harmony and not harmony_pregnant
        always "bg_street_harmony_nohaircut" when harmony
        group multiple auto variant harmony_piercings_front when harmony


        attribute camila
        attribute camila_pregnant when camila
        attribute camila_collar when camila
        group multiple auto variant camila_piercings_back when camila
        group camila_bot auto variant preg when camila and camila_pregnant
        group camila_bot auto variant nopreg when camila and not camila_pregnant
        group camila_top auto variant preg when camila and camila_pregnant
        group camila_top auto variant nopreg when camila and not camila_pregnant
        group camila_hair auto when camila
        group multiple auto variant camila_piercings_front when camila


        attribute anna
        attribute anna_pregnant when anna
        group multiple auto variant anna_piercings when anna
        group anna_bot auto variant preg when anna and anna_pregnant
        group anna_bot auto variant nopreg when anna and not anna_pregnant
        group anna_top auto variant preg when anna and anna_pregnant
        group anna_top auto variant nopreg when anna and not anna_pregnant
        attribute anna_nohaircut when anna


        attribute kat
        attribute kat_pregnant when kat
        attribute kat_collar when kat
        group multiple auto variant kat_piercings when kat
        group kat_bot auto variant preg when kat and kat_pregnant
        group kat_bot auto variant nopreg when kat and not kat_pregnant
        group kat_top auto variant preg when kat and kat_pregnant
        group kat_top auto variant nopreg when kat and not kat_pregnant
        attribute kat_nohaircut when kat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
