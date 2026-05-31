init 5 python:
    class GolfPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"} or "fafwm" not in DLCS:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GolfPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not cherie.flags.gone_forever and cherie.room == "golf":
                    attr.add('cherie')
            
            
            if active_girl.id in ["cherie"]:
                if enable_debug_picker:
                    renpy.log(f"GolfPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GolfPicker result: {attr}")
            return attr

    if Room.find("golf"):
        Room.find("golf").lively_npc = ["cherie"]

init 6:
    layeredimage bg golf:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, GolfPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute cherie_clit null
        attribute cherie_ears null


        always "golf"


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
