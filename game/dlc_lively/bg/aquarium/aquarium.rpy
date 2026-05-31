init 5 python:
    class AquariumPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"AquariumPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not claire.flags.gone_forever and claire.room == "aquarium":
                    attr.add('claire')
                if not morgan.flags.gone_forever and morgan.room == "aquarium":
                    attr.add('morgan')
                    if morgan.activity_name == "work":
                        attr.add('tank')
                    else:
                        attr.add('normal')
            
            
            if active_girl.id in ["claire", "morgan"]:
                if enable_debug_picker:
                    renpy.log(f"AquariumPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"AquariumPicker result: {attr}")
            return attr

    Room.find("aquarium").lively_npc = ["claire", "morgan"]

init 6:
    layeredimage bg aquarium:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, AquariumPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nipples null
        attribute claire_nose null
        attribute claire_pregnant_navel null
        attribute morgan null
        attribute morgan_tongue null


        always "aquarium"


        group morgan when morgan:
            attribute normal
        attribute morgan_pregnant variant normal when morgan and normal
        attribute morgan_collar variant normal when morgan and normal
        group multiple auto variant morgan_piercings_normal when morgan and normal
        group morgan_bot auto variant preg when morgan and normal and morgan_pregnant
        group morgan_bot auto variant nopreg when morgan and normal and not morgan_pregnant
        group morgan_top auto variant preg when morgan and normal and morgan_pregnant
        group morgan_top auto variant nopreg when morgan and normal and not morgan_pregnant
        group morgan_hair auto variant normal when morgan and normal


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant
        group claire_hair auto when claire


        group morgan when morgan:
            attribute tank
        attribute morgan_pregnant variant tank when morgan and tank
        attribute morgan_collar variant tank when morgan and tank
        group multiple auto variant morgan_piercings_tank when morgan and tank
        always "bg_aquarium_tank_morgan_top" when morgan and tank
        group morgan_hair auto variant tank when morgan and tank
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
