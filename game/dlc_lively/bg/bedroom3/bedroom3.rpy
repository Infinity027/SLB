init 5 python:
    class Bedroom3Picker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"Bedroom3Picker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not sasha.hidden and sasha.room == "bedroom3":
                    attr.add('sasha')
            
            
            if active_girl.id in ["sasha"]:
                if enable_debug_picker:
                    renpy.log(f"Bedroom3Picker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"Bedroom3Picker result: {attr}")
            return attr

    Room.find("bedroom3").lively_npc = ["sasha"]

init 6:
    layeredimage bg bedroom3:
        attribute_function Pickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, Bedroom3Picker], npc=sasha)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute clit null
        attribute lips null
        attribute navel null
        attribute noboobjob null
        attribute pregnant_navel null
        attribute tongue null


        attribute day "bedroom3_day"
        attribute night "bedroom3_night"


        attribute sasha
        attribute pregnant when sasha and not boobjob
        attribute pregnant variant boobjob when sasha and boobjob
        attribute boobjob when sasha
        group multiple auto variant piercings when sasha
        group multiple auto variant piercings_bb when sasha and boobjob
        group multiple auto variant piercings_bobb when sasha and not boobjob
        group bot auto when sasha and not (naked or bottomless)
        group top auto variant bb_preg when sasha and boobjob and pregnant and not (naked or bottomless)
        group top auto variant bb_nopreg when sasha and boobjob and not (pregnant or naked or bottomless)
        group top auto variant nobb_preg when sasha and pregnant and not (boobjob or naked or bottomless)
        group top auto variant nobb_nopreg when sasha and not (boobjob or pregnant or naked or bottomless)
        group hair auto when sasha
        attribute collar when sasha
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
