init 5 python:
    class GaragePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GaragePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not kleio.flags.gone_forever and kleio.room == "garage":
                    attr.add('kleio')
            
            
            if active_girl.id in ["kleio"]:
                if enable_debug_picker:
                    renpy.log(f"GaragePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GaragePicker result: {attr}")
            return attr

    Room.find("garage").lively_npc = ["kleio"]

init 6:
    layeredimage bg garage:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, GaragePicker], npc=kleio)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute nose null
        attribute tongue null


        always "garage" when not kleio
        always "bg_garage_bg" when kleio


        attribute kleio
        attribute pregnant when kleio
        attribute collar when kleio
        group multiple auto variant piercings when kleio
        group bot auto variant nopreg when kleio and not (pregnant or naked)
        group bot auto variant preg when kleio and pregnant and not naked
        group top auto variant nopreg when kleio and not (pregnant or naked)
        group top auto variant preg when kleio and pregnant and not naked
        group hair auto when kleio
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
