init 5 python:
    class AlettaOfficePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"AlettaOfficePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "alettaoffice":
                    attr.add('aletta')
            
            
            if active_girl.id in ["aletta"]:
                if enable_debug_picker:
                    renpy.log(f"AlettaOfficePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"AlettaOfficePicker result: {attr}")
            return attr

    Room.find("alettaoffice").lively_npc = ["aletta"]

init 6:
    layeredimage bg alettaoffice:
        attribute_function Pickers([DayNightPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, AlettaOfficePicker], npc=aletta)


        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute topless null
        attribute bottomless null
        attribute clit null
        attribute lips null
        attribute navel null
        attribute tongue null


        attribute day "alettaoffice_day"
        attribute night "alettaoffice_night"


        attribute aletta
        attribute pregnant when aletta
        attribute collar when aletta
        group multiple auto variant piercings when aletta
        attribute glasses when aletta
        group outfit auto variant nopreg when aletta and not (pregnant or naked or topless)
        group outfit auto variant preg when aletta and pregnant and not (naked or topless)
        group hair auto when aletta
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
