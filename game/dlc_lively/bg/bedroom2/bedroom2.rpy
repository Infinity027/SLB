init 5 python:
    class Bedroom2Picker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"Bedroom2Picker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "bedroom2":
                    attr.add('bree')
            
            
            if active_girl.id in ["bree"]:
                if enable_debug_picker:
                    renpy.log(f"Bedroom2Picker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"Bedroom2Picker result: {attr}")
            return attr

    Room.find("bedroom2").lively_npc = ["bree"]

init 6:
    layeredimage bg bedroom2:
        attribute_function Pickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, Bedroom2Picker], npc=bree)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute clit null
        attribute ears null
        attribute lips null
        attribute navel null
        attribute nipples null
        attribute pregnant_navel null
        attribute tongue null


        attribute day "bedroom2_day"
        attribute night "bedroom2_night"


        attribute bree
        attribute pregnant when bree
        attribute collar when bree
        group multiple auto variant piercings when bree
        group bot auto when bree and not (naked or bottomless)
        group top auto when bree and not (naked or topless)
        group top auto variant preg when bree and pregnant and not (naked or topless)
        group top auto variant nopreg when bree and not (pregnant or naked or topless)
        group hair auto when bree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
