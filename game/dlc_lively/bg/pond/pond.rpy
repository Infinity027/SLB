init 5 python:
    class PondPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PondPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not anna.flags.gone_forever and anna.room == "pond":
                    attr.add('anna')
                if not ayesha.flags.gone_forever and ayesha.room == "pond":
                    attr.add('ayesha')
                if not hanna.flags.gone_forever and hanna.room == "pond":
                    attr.add('hanna')
                if not kylie.flags.gone_forever and kylie.room == "pond":
                    attr.add('kylie')
                if not morgan.flags.gone_forever and morgan.room == "pond":
                    attr.add('morgan')
                if not reona.flags.gone_forever and reona.room == "pond":
                    attr.add('reona')
                if not samantha.flags.gone_forever and samantha.room == "pond":
                    attr.add('samantha')
            
            
            if active_girl.id in ["anna", "ayesha", "hanna", "kylie", "morgan", "reona", "samantha"]:
                if enable_debug_picker:
                    renpy.log(f"PondPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PondPicker result: {attr}")
            return attr

    Room.find("pond").lively_npc = ["anna", "ayesha", "hanna", "kylie", "morgan", "reona", "samantha"]

init 6:
    layeredimage bg pond:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, PondPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_nose null
        attribute anna_tongue null
        attribute ayesha_casual null
        attribute ayesha_clit null
        attribute ayesha_nose null
        attribute ayesha_tongue null
        attribute hanna_armpits null
        attribute hanna_nose null
        attribute hanna_tongue null
        attribute kylie_casual null
        attribute kylie_ears null
        attribute kylie_nose null
        attribute kylie_tongue null
        attribute morgan_clit null
        attribute morgan_tongue null
        attribute reona_ears null
        attribute reona_nose null
        attribute reona_tongue null
        attribute samantha_clit null
        attribute samantha_ears null
        attribute samantha_lips null
        attribute samantha_navel null
        attribute samantha_nipples null
        attribute samantha_nose null
        attribute samantha_pregnant_navel null
        attribute samantha_tongue null


        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"


        attribute reona
        attribute reona_collar when reona
        attribute reona_pregnant when reona
        group multiple auto variant reona_piercings when reona
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_hair auto when reona


        attribute morgan
        attribute morgan_pregnant when morgan
        attribute morgan_makeup when morgan
        attribute morgan_collar when morgan
        group multiple auto variant morgan_piercings when morgan
        group morgan_bot auto variant nopreg when morgan and not morgan_pregnant
        group morgan_bot auto variant preg when morgan and morgan_pregnant
        group morgan_top auto variant nopreg when morgan and not morgan_pregnant
        group morgan_top auto variant preg when morgan and morgan_pregnant
        group morgan_hair auto when morgan


        attribute kylie
        attribute kylie_collar when kylie
        attribute kylie_pregnant when kylie
        group multiple auto variant kylie_piercings when kylie
        group kylie_bot auto variant nopreg when kylie and not kylie_pregnant
        group kylie_bot auto variant preg when kylie and kylie_pregnant
        group kylie_top auto variant nopreg when kylie and not kylie_pregnant
        group kylie_top auto variant preg when kylie and kylie_pregnant
        attribute kylie_nohaircut when kylie


        attribute anna
        attribute anna_collar when anna
        attribute anna_pregnant when anna
        group multiple auto variant anna_piercings when anna
        group anna_bot auto variant nopreg when anna and not anna_pregnant
        group anna_bot auto variant preg when anna and anna_pregnant
        group anna_top auto variant nopreg when anna and not anna_pregnant
        group anna_top auto variant preg when anna and anna_pregnant
        attribute anna_nohaircut when anna


        attribute ayesha
        attribute ayesha_pregnant when ayesha
        group multiple auto variant ayesha_piercings when ayesha
        group ayesha_bot auto variant nopreg when ayesha and not ayesha_pregnant
        group ayesha_bot auto variant preg when ayesha and ayesha_pregnant
        group ayesha_top auto variant nopreg when ayesha and not ayesha_pregnant
        group ayesha_top auto variant preg when ayesha and ayesha_pregnant
        attribute ayesha_collar when ayesha
        attribute ayesha_nohaircut when ayesha


        attribute hanna
        attribute hanna_collar when hanna
        attribute hanna_pregnant when hanna
        group multiple auto variant hanna_piercings when hanna
        group hanna_bot auto variant nopreg when hanna and not hanna_pregnant
        group hanna_bot auto variant preg when hanna and hanna_pregnant
        group hanna_top auto variant nopreg when hanna and not hanna_pregnant
        group hanna_top auto variant preg when hanna and hanna_pregnant
        attribute hanna_nohaircut when hanna


        attribute samantha
        attribute samantha_pregnant when samantha
        attribute samantha_collar when samantha
        group samantha_bot auto variant nopreg when samantha and not samantha_pregnant
        group samantha_bot auto variant preg when samantha and samantha_pregnant
        group samantha_top auto variant nopreg when samantha and not samantha_pregnant
        group samantha_top auto variant preg when samantha and samantha_pregnant
        attribute samantha_nohaircut when samantha
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
