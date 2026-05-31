init 5 python:
    class GymLockersPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"GymLockersPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not alexis.flags.gone_forever and alexis.room == "gymlockers":
                    attr.add('alexis')
                if not emma.flags.gone_forever and emma.room == "gymlockers":
                    attr.add('emma')
                if not lavish.flags.gone_forever and lavish.room == "gymlockers":
                    attr.add('lavish')
                if not reona.flags.gone_forever and reona.room == "gymlockers":
                    attr.add('reona')
            
            
            if active_girl.id in ["alexis", "emma", "lavish", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"GymLockersPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"GymLockersPicker result: {attr}")
            return attr

    Room.find("gymlockers").lively_npc = ["alexis", "emma", "lavish", "reona"]

init 6:
    layeredimage bg gymlockers:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, GymLockersPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute alexis_clit null
        attribute alexis_nose null
        attribute emma_collar null
        attribute emma_tongue null
        attribute lavish_clit null
        attribute lavish_navel null
        attribute lavish_tongue null
        attribute reona_clit null
        attribute reona_ears null
        attribute reona_navel null
        attribute reona_nipples null
        attribute reona_nose null
        attribute reona_tongue null


        always "gymlockers"


        attribute lavish
        attribute lavish_collar when lavish
        group multiple auto variant lavish_piercings when lavish:
            attribute lavish_nipples when not lavish_sport
        group lavish_bot auto when lavish
        group lavish_top auto when lavish
        attribute lavish_nohaircut when lavish


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant
        group reona_hair auto when reona


        attribute alexis
        attribute alexis_pregnant when alexis
        attribute alexis_collar when alexis
        group multiple auto variant alexis_piercings when alexis
        group alexis_bot auto variant preg when alexis and alexis_pregnant
        group alexis_bot auto variant nopreg when alexis and not alexis_pregnant
        group alexis_top auto variant preg when alexis and alexis_pregnant
        group alexis_top auto variant nopreg when alexis and not alexis_pregnant
        attribute alexis_nohaircut when alexis


        attribute emma
        attribute emma_pregnant when emma
        group multiple auto variant emma_piercings when emma
        group emma_bot auto variant preg when emma and emma_pregnant
        group emma_bot auto variant nopreg when emma and not emma_pregnant
        group emma_top auto variant preg when emma and emma_pregnant
        group emma_top auto variant nopreg when emma and not emma_pregnant
        attribute emma_nohaircut when emma
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
