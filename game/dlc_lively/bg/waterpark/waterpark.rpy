init 5 python:
    class WaterparkPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"WaterparkPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.flags.gone_forever and audrey.room == "waterpark":
                    attr.add('audrey')
                if not claire.flags.gone_forever and claire.room == "waterpark":
                    attr.add('claire')
                if not palla.flags.gone_forever and palla.room == "waterpark":
                    attr.add('palla')
                if not sasha.hidden and sasha.room == "waterpark":
                    attr.add('sasha')
            
            
            if active_girl.id in ["audrey", "palla", "sasha"]:
                if enable_debug_picker:
                    renpy.log(f"WaterparkPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"WaterparkPicker result: {attr}")
            return attr

    Room.find("waterpark").lively_npc = ["audrey", "claire", "palla", "sasha"]

init 6:
    layeredimage bg waterpark:
        attribute_function MultiPickers([ CollarPicker, HaircutPicker, OutfitPicker, WaterparkPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute claire_clit null
        attribute palla_clit null
        attribute palla_glasses null
        attribute palla_navel null
        attribute palla_tongue null
        attribute sasha_clit null
        attribute sasha_lips null
        attribute sasha_navel null
        attribute sasha_tongue null
        attribute sasha_noboobjob null

        always "waterpark"

        attribute claire
        
        attribute claire_collar when claire
        group claire_hair auto when claire
        group claire_bot auto variant nopreg when claire
        group claire_top auto variant nopreg when claire

        attribute sasha
        
        attribute sasha_boobjob when sasha
        attribute sasha_collar when sasha
        group sasha_bot auto when sasha
        group sasha_top auto variant bb when sasha and sasha_boobjob
        group sasha_top auto variant nobb when sasha and not sasha_boobjob
        group sasha_hair auto when sasha

        attribute audrey
        
        attribute audrey_collar when audrey
        attribute audrey_nohaircut when audrey
        group audrey_bot auto variant nopreg when audrey
        group audrey_top auto variant nopreg when audrey

        attribute palla
        attribute palla_collar when palla
        attribute palla_nohaircut when palla
        group palla_bot auto variant nopreg when palla
        group palla_top auto variant nopreg when palla

        group multiple auto variant water