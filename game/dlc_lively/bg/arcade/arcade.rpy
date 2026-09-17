init 5 python:
    class ArcadePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"ArcadePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "arcade":
                    attr.add('bree')
                if not kat.flags.gone_forever and kat.room == "arcade":
                    attr.add('kat')
            
            
            if active_girl.id in ["bree", "kat"]:
                if enable_debug_picker:
                    renpy.log(f"ArcadePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"ArcadePicker result: {attr}")
            return attr

    Room.find("arcade").lively_npc = ["bree", "kat"]

init 6:
    layeredimage bg arcade:
        attribute_function MultiPickers([CollarPicker, OutfitPicker, ArcadePicker], append_npc_from_attributes=True)

        attribute empty null            
        attribute force_display null        

        always "arcade"

        attribute bree
        attribute bree_collar when bree
        always "bg_arcade_bree_nohaircut" when bree


        attribute kat
        attribute kat_collar when kat
        always "bg_arcade_kat_nohaircut" when kat
