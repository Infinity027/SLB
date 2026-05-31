init 5 python:
    class MansionPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"MansionPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not cherie.flags.gone_forever and cherie.room == "mansion":
                    attr.add('cherie')
            
            
            if active_girl.id in ["cherie"]:
                if enable_debug_picker:
                    renpy.log(f"MansionPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"MansionPicker result: {attr}")
            return attr

    Room.find("mansion").lively_npc = ["cherie"]

init 6:
    layeredimage bg mansion:
        attribute_function MultiPickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, MansionPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute cherie_clit null
        attribute cherie_ears null


        attribute day "mansion_day"
        attribute night "mansion_night"


        attribute cherie
        attribute cherie_pregnant when cherie
        attribute cherie_collar when cherie
        group multiple auto variant cherie_piercings when cherie
        group cherie_bot auto variant preg when cherie and cherie_pregnant
        group cherie_bot auto variant nopreg when cherie and not cherie_pregnant
        group cherie_top auto variant preg when cherie and cherie_pregnant
        group cherie_top auto variant nopreg when cherie and not cherie_pregnant
        group cherie_hair auto when cherie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
