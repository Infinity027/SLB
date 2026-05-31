init 5 python:
    class ElectronicPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"ElectronicPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not amy.flags.gone_forever and amy.room == "electronic":
                    attr.add('amy')
                if not kat.flags.gone_forever and kat.room == "electronic":
                    attr.add('kat')
                if not morgan.flags.gone_forever and morgan.room == "electronic":
                    attr.add('morgan')
            
            
            if active_girl.id in ["amy", "kat", "morgan"]:
                if enable_debug_picker:
                    renpy.log(f"ElectronicPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"ElectronicPicker result: {attr}")
            return attr

    Room.find("electronic").lively_npc = ["amy", "kat", "morgan"]

init 6:
    layeredimage bg electronic:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, ElectronicPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_nose null
        attribute kat_tongue null
        attribute morgan_clit null
        attribute morgan_tongue null


        always "electronic"


        attribute morgan
        attribute morgan_pregnant when morgan
        attribute morgan_collar when morgan
        group multiple auto variant morgan_piercings when morgan
        always "bg_electronic_morgan_face" when morgan and not morgan_makeup
        attribute morgan_makeup when morgan
        group morgan_hair auto when morgan
        group morgan_bot auto variant nopreg when morgan and not morgan_pregnant
        group morgan_bot auto variant preg when morgan and morgan_pregnant
        group morgan_top auto variant nopreg when morgan and not morgan_pregnant
        group morgan_top auto variant preg when morgan and morgan_pregnant


        attribute amy
        attribute amy_pregnant when amy
        attribute amy_collar when amy
        attribute amy_nohaircut when amy
        always "bg_electronic_amy_earphones" when amy
        group multiple auto variant amy_piercings when amy
        group amy_bot auto variant nopreg when amy and not amy_pregnant
        group amy_bot auto variant preg when amy and amy_pregnant
        group amy_top auto variant nopreg when amy and not amy_pregnant
        group amy_top auto variant preg when amy and amy_pregnant


        attribute kat
        attribute kat_pregnant when kat
        attribute kat_collar when kat
        attribute kat_nohaircut when kat
        group multiple auto variant kat_piercings when kat
        group kat_bot auto when kat
        group kat_top auto variant nopreg when kat and not kat_pregnant
        group kat_top auto variant preg when kat and kat_pregnant
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
