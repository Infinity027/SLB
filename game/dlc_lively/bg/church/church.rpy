init 5 python:
    class ChurchPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"ChurchPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not claire.flags.gone_forever and claire.room == "church":
                    attr.add('claire')
                if not harmony.flags.gone_forever and harmony.room == "church":
                    attr.add('harmony')
            
            
            if active_girl.id in ["claire", "harmony"]:
                if enable_debug_picker:
                    renpy.log(f"ChurchPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"ChurchPicker result: {attr}")
            return attr

    Room.find("church").lively_npc = ["claire", "harmony"]

init 6:
    layeredimage bg church:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, ChurchPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nipples null
        attribute claire_nose null
        attribute claire_pregnant_navel null
        attribute harmony_clit null
        attribute harmony_navel null
        attribute harmony_nipples null
        attribute harmony_nose null
        attribute harmony_pregnant_navel null
        attribute harmony_tongue null


        always "church"


        attribute harmony
        attribute harmony_collar when harmony
        group multiple auto variant harmony_piercings when harmony
        group harmony_bot auto when harmony
        group harmony_top auto when harmony
        group harmony_hair auto when harmony and not harmony_nun


        attribute claire
        attribute claire_collar when claire
        group multiple auto variant claire_piercings when claire
        group claire_bot auto when claire
        group claire_top auto when claire
        group claire_hair auto when claire
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
