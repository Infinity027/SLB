init 5 python:
    class FlowerShopPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"FlowerShopPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not claire.flags.gone_forever and claire.room == "flowershop":
                    attr.add('claire')
                if not reona.flags.gone_forever and reona.room == "flowershop":
                    attr.add('reona')
            
            
            if active_girl.id in ["claire", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"FlowerShopPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"FlowerShopPicker result: {attr}")
            return attr

    Room.find("flowershop").lively_npc = ["claire", "reona"]

init 6:
    layeredimage bg flowershop:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, FlowerShopPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute claire_navel null
        attribute reona_nose null
        attribute reona_tongue null


        always "flowershop"


        attribute claire
        attribute claire_pregnant when claire
        attribute claire_collar when claire
        group multiple auto variant claire_piercings when claire
        group claire_bot auto variant preg when claire and claire_pregnant
        group claire_bot auto variant nopreg when claire and not claire_pregnant
        group claire_top auto variant preg when claire and claire_pregnant
        group claire_top auto variant nopreg when claire and not claire_pregnant
        group claire_hair auto when claire


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        group multiple auto variant reona_piercings when reona
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant
        attribute reona_pureglasses when reona
        group reona_hair auto when reona
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
