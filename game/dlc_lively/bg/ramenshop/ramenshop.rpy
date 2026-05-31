init 5 python:
    class RamenShopPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"RamenShopPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not claire.flags.gone_forever and claire.room == "ramenshop":
                    attr.add('claire')
            
            
            if active_girl.id in ["claire"]:
                if enable_debug_picker:
                    renpy.log(f"RamenShopPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"RamenShopPicker result: {attr}")
            return attr

    Room.find("ramenshop").lively_npc = ["claire"]

init 6:
    layeredimage bg ramenshop:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, RamenShopPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute claire_clit null


        always "ramenshop"


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group multiple auto variant claire_piercings when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant
        group claire_hair auto when claire


        group multiple auto variant ramen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
