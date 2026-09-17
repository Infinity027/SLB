init 5 python:
    class GymPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GymPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.flags.gone_forever and audrey.room == "gym":
                    attr.add('audrey')
                if not cherie.flags.gone_forever and cherie.room == "gym":
                    attr.add('cherie')
                if not hanna.flags.gone_forever and hanna.room == "gym":
                    attr.add('hanna')
                if not kiara.flags.gone_forever and kiara.room == "gym":
                    attr.add('kiara')
                if not palla.flags.gone_forever and palla.room == "gym":
                    attr.add('palla')
            
            
            if active_girl.id in ["audrey", "cherie", "hanna", "kiara", "palla"]:
                if enable_debug_picker:
                    renpy.log(f"GymPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GymPicker result: {attr}")
            return attr

    Room.find("gym").lively_npc = ["audrey", "cherie", "hanna", "kiara", "palla"]

init 6:
    layeredimage bg gym:
        attribute_function MultiPickers([ CollarPicker, OutfitPicker, HaircutPicker, GymPicker], append_npc_from_attributes=True)

        attribute empty null            
        attribute force_display null        
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute hanna_armpits null
        attribute hanna_tongue null
        attribute palla_glasses null
        attribute palla_lips null
        attribute palla_tongue null

        always "gym"

        attribute hanna
        attribute hanna_collar when hanna
        attribute hanna_nohaircut when hanna
        group hanna_bot auto variant nopreg when hanna
        group hanna_top auto variant nopreg when hanna

        attribute cherie
        attribute cherie_collar when cherie
        group cherie_hair auto when cherie
        group cherie_bot auto variant nopreg when cherie
        group cherie_top auto variant nopreg when cherie


        attribute palla
        attribute palla_collar when palla
        attribute palla_nohaircut when palla
        group palla_bot auto variant nopreg when palla
        group palla_top auto variant nopreg when palla

        attribute kiara
        attribute kiara_collar when kiara
        group kiara_hair auto when kiara
        group kiara_bot auto variant nopreg when kiara
        group kiara_top auto variant nopreg when kiara

        attribute audrey
        attribute audrey_collar when audrey
        attribute audrey_nohaircut when audrey
        group audrey_bot auto when audrey
        group audrey_top auto when audrey