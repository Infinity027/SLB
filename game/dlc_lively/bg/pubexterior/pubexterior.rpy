init 5 python:
    class PubExteriorPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PubExteriorPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not anna.flags.gone_forever and anna.room == "pubexterior":
                    attr.add('anna')
                if not emma.flags.gone_forever and emma.room == "pubexterior":
                    attr.add('emma')
                if not kat.flags.gone_forever and kat.room == "pubexterior":
                    attr.add('kat')
                if not kylie.flags.gone_forever and kylie.room == "pubexterior":
                    attr.add('kylie')
            
            
            if active_girl.id in ["anna", "emma", "kat", "kylie"]:
                if enable_debug_picker:
                    renpy.log(f"PubExteriorPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PubExteriorPicker result: {attr}")
            return attr

    Room.find("pubexterior").lively_npc = ["anna", "emma", "kat", "kylie"]

init 6:
    layeredimage bg pubexterior:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, PubExteriorPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_nose null
        attribute anna_tongue null
        attribute emma_clit null
        attribute emma_navel null
        attribute emma_pregnant_navel null
        attribute emma_tongue null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_pregnant_navel null
        attribute kat_tongue null
        attribute kylie_clit null
        attribute kylie_ears null
        attribute kylie_navel null
        attribute kylie_pregnant_navel null
        attribute kylie_tongue null


        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always "snow"


        attribute kylie
        attribute kylie_pregnant when kylie
        attribute kylie_collar when kylie
        always "bg_pubexterior_kylie_hair_kylie_nohaircut" when kylie
        group multiple auto variant kylie_piercings when kylie
        group kylie_bot auto variant preg when kylie and kylie_pregnant
        group kylie_bot auto variant nopreg when kylie and not kylie_pregnant
        group kylie_top auto variant preg when kylie and kylie_pregnant
        group kylie_top auto variant nopreg when kylie and not kylie_pregnant


        attribute kat
        attribute kat_pregnant when kat
        attribute kat_collar when kat
        always "bg_pubexterior_kat_nohaircut" when kat
        group multiple auto variant kat_piercings when kat
        group kat_bot auto variant preg when kat and kat_pregnant
        group kat_bot auto variant nopreg when kat and not kat_pregnant
        group kat_top auto variant preg when kat and kat_pregnant
        group kat_top auto variant nopreg when kat and not kat_pregnant


        attribute anna
        attribute anna_pregnant when anna
        attribute anna_collar when anna
        always "bg_pubexterior_anna_nohaircut" when anna
        group multiple auto variant anna_piercings when anna
        group anna_bot auto variant preg when anna and anna_pregnant
        group anna_bot auto variant nopreg when anna and not anna_pregnant
        group anna_top auto variant preg when anna and anna_pregnant
        group anna_top auto variant nopreg when anna and not anna_pregnant


        attribute emma
        attribute emma_pregnant when emma
        attribute emma_collar when emma
        always "bg_pubexterior_emma_nohaircut" when emma
        group multiple auto variant emma_piercings when emma
        group emma_bot auto variant preg when emma and emma_pregnant
        group emma_bot auto variant nopreg when emma and not emma_pregnant
        group emma_top auto variant preg when emma and emma_pregnant
        group emma_top auto variant nopreg when emma and not emma_pregnant
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
