init 5 python:
    class GymMachinePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GymMachinePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "gymmachine":
                    attr.add('aletta')
                if not ayesha.flags.gone_forever and ayesha.room == "gymmachine":
                    attr.add('ayesha')
                if not camila.flags.gone_forever and camila.room == "gymmachine":
                    attr.add('camila')
                if not kylie.flags.gone_forever and kylie.room == "gymmachine":
                    attr.add('kylie')
            
            
            if active_girl.id in ["aletta", "ayesha", "camila", "kylie"]:
                if enable_debug_picker:
                    renpy.log(f"GymMachinePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GymMachinePicker result: {attr}")
            return attr

    Room.find("gymmachine").lively_npc = ["aletta", "ayesha", "camila", "kylie"]

init 6:
    layeredimage bg gymmachine:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, GymMachinePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute aletta_clit null
        attribute aletta_glasses null
        attribute aletta_lips null
        attribute aletta_nose null
        attribute aletta_tongue null
        attribute ayesha_nose null
        attribute ayesha_tongue null
        attribute camila_clit null
        attribute camila_lips null
        attribute camila_nose null
        attribute camila_tongue null
        attribute kylie_clit null
        attribute kylie_ears null
        attribute kylie_nose null
        attribute kylie_tongue null


        always "gymmachine"


        attribute camila
        attribute camila_pregnant when camila
        attribute camila_collar when camila
        group multiple auto variant camila_piercings_back when camila
        group camila_bot auto variant nopreg when camila and not camila_pregnant
        group camila_bot auto variant preg when camila and camila_pregnant
        group camila_top auto variant nopreg when camila and not camila_pregnant
        group camila_top auto variant preg when camila and camila_pregnant
        group camila_hair auto when camila
        group multiple auto variant camila_piercings_front when camila


        attribute ayesha
        attribute ayesha_pregnant when ayesha
        attribute ayesha_collar when ayesha
        attribute ayesha_nohaircut when ayesha
        group multiple auto variant ayesha_piercings when ayesha
        group ayesha_bot auto variant nopreg when ayesha and not ayesha_pregnant
        group ayesha_bot auto variant preg when ayesha and ayesha_pregnant
        group ayesha_top auto variant nopreg when ayesha and not ayesha_pregnant
        group ayesha_top auto variant preg when ayesha and ayesha_pregnant


        attribute aletta
        attribute aletta_pregnant when aletta
        attribute aletta_collar when aletta
        group multiple auto variant aletta_piercings when aletta
        group aletta_bot auto variant nopreg when aletta and not aletta_pregnant
        group aletta_bot auto variant preg when aletta and aletta_pregnant
        group aletta_top auto variant nopreg when aletta and not aletta_pregnant
        group aletta_top auto variant preg when aletta and aletta_pregnant
        group aletta_hair auto when aletta


        attribute kylie
        attribute kylie_pregnant when kylie
        attribute kylie_collar when kylie
        group multiple auto variant kylie_piercings when kylie
        group kylie_bot auto variant nopreg when kylie and not kylie_pregnant
        group kylie_bot auto variant preg when kylie and kylie_pregnant
        group kylie_top auto variant nopreg when kylie and not kylie_pregnant
        group kylie_top auto variant preg when kylie and kylie_pregnant
        attribute kylie_nohaircut when kylie
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
