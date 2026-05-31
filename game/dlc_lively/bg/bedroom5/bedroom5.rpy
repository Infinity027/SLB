init 5 python:
    class Bedroom5Picker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"Bedroom5Picker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not minami.hidden and minami.room == "bedroom5":
                    attr.add('minami')
            
            
            if active_girl.id in ["minami"]:
                if enable_debug_picker:
                    renpy.log(f"Bedroom5Picker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"Bedroom5Picker result: {attr}")
            return attr

    Room.find("bedroom5").lively_npc = ["minami"]

init 6:
    layeredimage bg bedroom5:
        attribute_function Pickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, Bedroom5Picker], npc=minami)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute clit null
        attribute ears null
        attribute navel null
        attribute nipples null
        attribute nose null
        attribute pregnant_navel null


        attribute day "bedroom5_day"
        attribute night "bedroom5_night"


        attribute minami
        attribute pregnant when minami
        attribute collar when minami
        group hair auto when minami
        group stockings auto when minami and not (naked or bottomless)
        group bot auto variant preg when minami and pregnant and not (naked or bottomless)
        group bot auto variant nopreg when minami and not (pregnant or naked or bottomless)
        group top auto when minami and not (naked or topless)
        group top auto variant preg when minami and pregnant and not (naked or topless)
        group top auto variant nopreg when minami and not (pregnant or naked or topless)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
