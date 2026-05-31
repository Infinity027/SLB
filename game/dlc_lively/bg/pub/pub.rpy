init 5 python:
    class PubPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PubPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not alexis.flags.gone_forever and alexis.room == "pub":
                    attr.add('alexis')
                if not amy.flags.gone_forever and amy.room == "pub":
                    attr.add('amy')
                if not samantha.flags.gone_forever and samantha.room == "pub":
                    attr.add('samantha')
                if not sasha.hidden and sasha.room == "pub":
                    attr.add('sasha')
            
            
            if active_girl.id in ["alexis", "amy", "samantha", "sasha"]:
                if enable_debug_picker:
                    renpy.log(f"PubPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PubPicker result: {attr}")
            return attr

    Room.find("pub").lively_npc = ["alexis", "amy", "samantha", "sasha"]

init 6:
    layeredimage bg pub:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, PubPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute alexis_navel null
        attribute amy_clit null
        attribute samantha_clit null
        attribute samantha_lips null
        attribute samantha_navel null
        attribute samantha_nose null
        attribute samantha_pregnant_navel null
        attribute samantha_tongue null
        attribute sasha_clit null
        attribute sasha_lips null
        attribute sasha_noboobjob null
        attribute sasha_nose null
        attribute sasha_tongue null


        always "pub"


        attribute sasha
        attribute sasha_boobjob when sasha
        attribute sasha_pregnant variant bb when sasha and sasha_boobjob
        attribute sasha_pregnant variant nobb when sasha and not sasha_boobjob
        attribute sasha_collar when sasha
        group multiple auto variant sasha_piercings_back when sasha
        group multiple auto variant sasha_piercings_back_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_back_nobb when sasha and not sasha_boobjob
        group sasha_bot auto variant preg when sasha and sasha_pregnant
        group sasha_bot auto variant nopreg when sasha and not sasha_pregnant
        group sasha_top auto variant preg_bb when sasha and sasha_pregnant and sasha_boobjob
        group sasha_top auto variant preg_nobb when sasha and sasha_pregnant and not sasha_boobjob
        group sasha_top auto variant nopreg_bb when sasha and not sasha_pregnant and sasha_boobjob
        group sasha_top auto variant nopreg_nobb when sasha and not sasha_pregnant and not sasha_boobjob
        group sasha_hair auto when sasha
        group multiple auto variant sasha_piercings_front when sasha


        attribute amy
        attribute amy_pregnant when amy
        attribute amy_collar when amy
        group multiple auto variant amy_piercings when amy
        group amy_bot auto variant preg when amy and amy_pregnant
        group amy_bot auto variant nopreg when amy and not amy_pregnant
        group amy_top auto variant preg when amy and amy_pregnant
        group amy_top auto variant nopreg when amy and not amy_pregnant
        attribute amy_nohaircut when amy


        attribute alexis
        attribute alexis_pregnant when alexis
        attribute alexis_collar when alexis
        group multiple auto variant alexis_piercings when alexis
        group alexis_bot auto variant preg when alexis and alexis_pregnant
        group alexis_bot auto variant nopreg when alexis and not alexis_pregnant
        group alexis_top auto variant preg when alexis and alexis_pregnant
        group alexis_top auto variant nopreg when alexis and not alexis_pregnant
        attribute alexis_nohaircut when alexis


        attribute samantha
        attribute samantha_pregnant when samantha
        attribute samantha_collar when samantha
        group multiple auto variant samantha_piercings when samantha
        group samantha_bot auto variant preg when samantha and samantha_pregnant
        group samantha_bot auto variant nopreg when samantha and not samantha_pregnant
        group samantha_top auto variant preg when samantha and samantha_pregnant
        group samantha_top auto variant nopreg when samantha and not samantha_pregnant
        attribute samantha_nohaircut when samantha
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
