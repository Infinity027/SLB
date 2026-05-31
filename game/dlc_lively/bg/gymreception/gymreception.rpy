init 5 python:
    class GymReceptionPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GymReceptionPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "gymreception":
                    attr.add('bree')
                if not cassidy.flags.gone_forever and cassidy.room == "gymreception":
                    attr.add('cassidy')
                if not claire.flags.gone_forever and claire.room == "gymreception":
                    attr.add('claire')
                if not samantha.flags.gone_forever and samantha.room == "gymreception":
                    attr.add('samantha')
            
            
            if active_girl.id in ["bree", "cassidy", "claire", "samantha"]:
                if enable_debug_picker:
                    renpy.log(f"GymReceptionPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GymReceptionPicker result: {attr}")
            return attr

    Room.find("gymreception").lively_npc = ["bree", "cassidy", "claire", "samantha"]

init 6:
    layeredimage bg gymreception:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, GymReceptionPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_tongue null
        attribute cassidy_ears null
        attribute cassidy_nose null
        attribute cassidy_tongue null
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_pregnant_navel null
        attribute samantha_clit null
        attribute samantha_lips null
        attribute samantha_navel null
        attribute samantha_pregnant_navel null
        attribute samantha_tongue null


        always "gymreception"


        attribute bree
        attribute bree_pregnant when bree
        attribute bree_collar when bree
        group multiple auto variant bree_piercings when bree
        group bree_bot auto variant preg when bree and bree_pregnant
        group bree_bot auto variant nopreg when bree and not bree_pregnant
        group bree_top auto variant preg when bree and bree_pregnant
        group bree_top auto variant nopreg when bree and not bree_pregnant
        attribute bree_nohaircut when bree


        attribute cassidy
        attribute cassidy_pregnant when cassidy
        attribute cassidy_collar when cassidy
        attribute cassidy_nohaircut when cassidy
        group multiple auto variant cassidy_piercings when cassidy
        group cassidy_bot auto variant preg when cassidy and cassidy_pregnant
        group cassidy_bot auto variant nopreg when cassidy and not cassidy_pregnant
        group cassidy_top auto variant preg when cassidy and cassidy_pregnant
        group cassidy_top auto variant nopreg when cassidy and not cassidy_pregnant


        attribute samantha
        attribute samantha_pregnant when samantha
        attribute samantha_collar when samantha
        group multiple auto variant samantha_piercings when samantha
        group samantha_bot auto variant preg when samantha and samantha_pregnant
        group samantha_bot auto variant nopreg when samantha and not samantha_pregnant
        group samantha_top auto variant preg when samantha and samantha_pregnant
        group samantha_top auto variant nopreg when samantha and not samantha_pregnant
        attribute samantha_nohaircut when samantha


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group multiple auto variant claire_piercings when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant
        group claire_hair auto when claire
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
