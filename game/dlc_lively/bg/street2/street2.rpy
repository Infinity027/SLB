init 5 python:
    class Street2Picker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"Street2Picker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "street2":
                    attr.add('aletta')
                if not ayesha.flags.gone_forever and ayesha.room == "street2":
                    attr.add('ayesha')
                if not cherie.flags.gone_forever and cherie.room == "street2":
                    attr.add('cherie')
                if not kiara.flags.gone_forever and kiara.room == "street2":
                    attr.add('kiara')
                if not kleio.flags.gone_forever and kleio.room == "street2":
                    attr.add('kleio')
                if not reona.flags.gone_forever and reona.room == "street2":
                    attr.add('reona')
            
            
            if active_girl.id in ["aletta", "ayesha", "cherie", "kleio", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"Street2Picker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"Street2Picker result: {attr}")
            return attr

    Room.find("street2").lively_npc = ["aletta", "ayesha", "cherie", "kiara", "kleio", "reona"]

init 6:
    layeredimage bg street2:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, Street2Picker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_nose null
        attribute aletta_tongue null
        attribute ayesha_tongue null
        attribute kiara_clit null
        attribute kleio_clit null
        attribute kleio_nose null
        attribute kleio_tongue null
        attribute reona_tongue null


        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"


        attribute kiara
        attribute kiara_pregnant when kiara
        attribute kiara_collar when kiara
        group kiara_hair auto when kiara
        group multiple auto variant kiara_piercings when kiara
        group kiara_bot auto variant preg when kiara and kiara_pregnant
        group kiara_bot auto variant nopreg when kiara and not kiara_pregnant
        group kiara_top auto variant preg when kiara and kiara_pregnant
        group kiara_top auto variant nopreg when kiara and not kiara_pregnant


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        attribute reona_pureglasses when reona
        group reona_hair auto when reona
        group multiple auto variant reona_piercings when reona
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant


        attribute cherie
        attribute cherie_pregnant when cherie
        attribute cherie_collar when cherie
        group multiple auto variant cherie_piercings when cherie
        group cherie_bot auto variant preg when cherie and cherie_pregnant
        group cherie_bot auto variant nopreg when cherie and not cherie_pregnant
        group cherie_top auto variant preg when cherie and cherie_pregnant
        group cherie_top auto variant nopreg when cherie and not cherie_pregnant
        group cherie_hair auto when cherie


        attribute aletta
        attribute aletta_pregnant when aletta
        attribute aletta_collar when aletta
        group aletta_hair auto when aletta
        attribute aletta_glasses when aletta
        group multiple auto variant aletta_piercings when aletta
        group aletta_bot auto variant preg when aletta and aletta_pregnant
        group aletta_bot auto variant nopreg when aletta and not aletta_pregnant
        group aletta_top auto variant preg when aletta and aletta_pregnant
        group aletta_top auto variant nopreg when aletta and not aletta_pregnant


        attribute kleio
        attribute kleio_pregnant when kleio
        attribute kleio_collar when kleio
        group kleio_hair auto when kleio
        group multiple auto variant kleio_piercings when kleio
        group kleio_bot auto variant preg when kleio and kleio_pregnant
        group kleio_bot auto variant nopreg when kleio and not kleio_pregnant
        group kleio_top auto variant preg when kleio and kleio_pregnant
        group kleio_top auto variant nopreg when kleio and not kleio_pregnant


        attribute ayesha
        attribute ayesha_pregnant when ayesha
        attribute ayesha_collar when ayesha
        group multiple auto variant ayesha_piercings when ayesha
        group ayesha_bot auto variant preg when ayesha and ayesha_pregnant
        group ayesha_bot auto variant nopreg when ayesha and not ayesha_pregnant
        group ayesha_top auto variant preg when ayesha and ayesha_pregnant
        group ayesha_top auto variant nopreg when ayesha and not ayesha_pregnant
        attribute ayesha_nohaircut when ayesha
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
