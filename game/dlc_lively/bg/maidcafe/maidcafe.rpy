init 5 python:
    class MaidCafePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"MaidCafePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "maidcafe":
                    attr.add('bree')
                if not kiara.flags.gone_forever and kiara.room == "maidcafe":
                    attr.add('kiara')
            
            
            if active_girl.id in ["bree", "kiara"]:
                if enable_debug_picker:
                    renpy.log(f"MaidCafePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"MaidCafePicker result: {attr}")
            return attr

    Room.find("maidcafe").lively_npc = ["bree", "kiara"]

init 6:
    layeredimage bg maidcafe:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, MaidCafePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_tongue null
        attribute kiara_clit null


        always "maidcafe"


        attribute kiara
        attribute kiara_pregnant when kiara
        attribute kiara_collar when kiara
        group multiple auto variant kiara_piercings when kiara
        group kiara_bot auto variant preg when kiara and kiara_pregnant
        group kiara_bot auto variant nopreg when kiara and not kiara_pregnant
        group kiara_top auto variant preg when kiara and kiara_pregnant
        group kiara_top auto variant nopreg when kiara and not kiara_pregnant
        group kiara_hair auto when kiara


        attribute bree
        attribute bree_pregnant when bree
        attribute bree_collar when bree
        attribute bree_nohaircut when bree
        group multiple auto variant bree_piercings when bree
        group bree_bot auto when bree
        group bree_top auto when bree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
