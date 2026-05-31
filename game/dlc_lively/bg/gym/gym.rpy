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
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, GymPicker], append_npc_from_attributes=True)


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
        attribute hanna_pregnant when hanna
        attribute hanna_collar when hanna
        attribute hanna_nohaircut when hanna
        group multiple auto variant hanna_piercings when hanna
        group hanna_bot auto variant preg when hanna and hanna_pregnant
        group hanna_bot auto variant nopreg when hanna and not hanna_pregnant
        group hanna_top auto variant preg when hanna and hanna_pregnant
        group hanna_top auto variant nopreg when hanna and not hanna_pregnant


        attribute cherie
        attribute cherie_pregnant when cherie
        attribute cherie_collar when cherie
        group cherie_hair auto when cherie
        group multiple auto variant cherie_piercings when cherie
        group cherie_bot auto variant preg when cherie and cherie_pregnant
        group cherie_bot auto variant nopreg when cherie and not cherie_pregnant
        group cherie_top auto variant preg when cherie and cherie_pregnant
        group cherie_top auto variant nopreg when cherie and not cherie_pregnant


        attribute palla
        attribute palla_pregnant when palla
        attribute palla_collar when palla
        attribute palla_nohaircut when palla
        group multiple auto variant palla_piercings when palla
        group palla_bot auto variant preg when palla and palla_pregnant
        group palla_bot auto variant nopreg when palla and not palla_pregnant
        group palla_top auto variant preg when palla and palla_pregnant
        group palla_top auto variant nopreg when palla and not palla_pregnant


        attribute kiara
        attribute kiara_pregnant when kiara
        attribute kiara_collar when kiara
        group kiara_hair auto when kiara
        group multiple auto variant kiara_piercings when kiara
        group kiara_bot auto variant preg when kiara and kiara_pregnant
        group kiara_bot auto variant nopreg when kiara and not kiara_pregnant
        group kiara_top auto variant preg when kiara and kiara_pregnant
        group kiara_top auto variant nopreg when kiara and not kiara_pregnant


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        attribute audrey_nohaircut when audrey
        group multiple auto variant audrey_piercings when audrey
        group audrey_bot auto when audrey
        group audrey_top auto when audrey
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
