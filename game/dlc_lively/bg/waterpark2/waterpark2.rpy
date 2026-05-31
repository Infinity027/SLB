init 5 python:
    class Waterpark2Picker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"Waterpark2Picker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not kylie.flags.gone_forever and kylie.room == "waterpark2":
                    attr.add('kylie')
                if not reona.flags.gone_forever and reona.room == "waterpark2":
                    attr.add('reona')
                if not samantha.flags.gone_forever and samantha.room == "waterpark2":
                    attr.add('samantha')
            
            
            if active_girl.id in ["kylie", "reona", "samantha"]:
                if enable_debug_picker:
                    renpy.log(f"Waterpark2Picker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"Waterpark2Picker result: {attr}")
            return attr

    Room.find("waterpark2").lively_npc = ["kylie", "reona", "samantha"]

init 6:
    layeredimage bg waterpark2:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, Waterpark2Picker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute kylie_clit null
        attribute kylie_tongue null
        attribute reona_clit null
        attribute reona_tongue null
        attribute samantha_clit null
        attribute samantha_ears null
        attribute samantha_lips null
        attribute samantha_tongue null

        always "waterpark2"


        attribute kylie
        attribute kylie_pregnant when kylie
        attribute kylie_collar when kylie
        group multiple auto variant kylie_piercings when kylie
        group kylie_bot auto variant preg when kylie and kylie_pregnant
        group kylie_bot auto variant nopreg when kylie and not kylie_pregnant
        group kylie_top auto variant preg when kylie and kylie_pregnant
        group kylie_top auto variant nopreg when kylie and not kylie_pregnant
        group kylie_hair auto when kylie


        attribute samantha
        attribute samantha_pregnant when samantha
        attribute samantha_collar when samantha
        group multiple auto variant samantha_piercings when samantha
        group samantha_bot auto variant preg when samantha and samantha_pregnant
        group samantha_bot auto variant nopreg when samantha and not samantha_pregnant
        group samantha_top auto variant preg when samantha and samantha_pregnant
        group samantha_top auto variant nopreg when samantha and not samantha_pregnant
        attribute samantha_nohaircut when samantha


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        group reona_hair auto when reona
        group multiple auto variant reona_piercings when reona
        group reona_bot auto when reona
        group reona_top auto when reona


        group multiple auto variant water
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
