init 5 python:
    class CEOPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"CEOPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not aletta.flags.gone_forever and not game.flags.JudiciaryDelay and aletta.room == "ceo":
                    attr.add('aletta')
                if not audrey.flags.gone_forever and ("audrey_event_05" not in DONE or "audrey_event_06" in DONE) and audrey.room == "ceo":
                    attr.add('audrey')
                if not cassidy.hidden and cassidy.room == "ceo":
                    attr.add('cassidy')
                if not cherie.hidden and cherie.room == "ceo":
                    attr.add('cherie')
                    if cherie.flags.isceo:
                        attr.add('desk')
                    else:
                        attr.add('couch')
                if not lavish.hidden and lavish.room == "ceo":
                    attr.add('lavish')
                if not shiori.hidden and shiori.room == "ceo":
                    attr.add('shiori')
            
            
            if active_girl.id in ["aletta", "audrey", "cassidy", "cherie", "lavish", "shiori"]:
                if enable_debug_picker:
                    renpy.log(f"CEOPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"CEOPicker result: {attr}")
            return attr

    Room.find("ceo").lively_npc = ["aletta", "audrey", "cassidy", "cherie", "lavish", "shiori"]

init 6:
    layeredimage bg ceo:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, CEOPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute couch null
        attribute desk null
        attribute aletta_naked null
        attribute aletta_topless null
        attribute aletta_bottomless null
        attribute aletta_clit null
        attribute aletta_ears null
        attribute aletta_lips null
        attribute aletta_navel null
        attribute aletta_tongue null
        attribute audrey_naked null
        attribute audrey_topless null
        attribute audrey_bottomless null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute cassidy_naked null
        attribute cassidy_topless null
        attribute cassidy_bottomless null
        attribute cassidy_clit null
        attribute cassidy_ears null
        attribute cassidy_eyebrow null
        attribute cassidy_lips null
        attribute cassidy_navel null
        attribute cassidy_nipples null
        attribute cassidy_nose null
        attribute cassidy_pregnant_navel null
        attribute cassidy_tongue null
        attribute cherie null
        attribute cherie_naked null
        attribute cherie_topless null
        attribute cherie_bottomless null
        attribute cherie_clit null
        attribute cherie_ears null
        attribute lavish_naked null
        attribute lavish_topless null
        attribute lavish_bottomless null
        attribute lavish_clit null
        attribute lavish_tongue null
        attribute shiori_naked null
        attribute shiori_topless null
        attribute shiori_bottomless null
        attribute shiori_ears null
        attribute shiori_lips null
        attribute shiori_navel null
        attribute shiori_nohaircut null
        attribute shiori_tongue null
        attribute nopeace null
        attribute peace null
        attribute pressed null
        attribute notpressed null


        always "ceo"


        attribute shiori
        attribute shiori_pregnant when shiori
        always "bg_ceo_shiori_nohaircut" when shiori
        group multiple auto variant shiori_piercings when shiori
        group shiori_bot auto variant preg when shiori and shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group shiori_bot auto variant nopreg when shiori and not shiori_pregnant and not (shiori_bottomless or shiori_naked)
        group shiori_top auto variant preg when shiori and shiori_pregnant and not (shiori_topless or shiori_naked)
        group shiori_top auto variant nopreg when shiori and not shiori_pregnant and not (shiori_topless or shiori_naked)
        attribute shiori_collar when shiori


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        group multiple auto variant audrey_piercings when audrey
        group audrey_bot auto variant preg when audrey and audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group audrey_bot auto variant nopreg when audrey and not audrey_pregnant and not (audrey_bottomless or audrey_naked)
        group audrey_top auto variant preg when audrey and audrey_pregnant and not (audrey_topless or audrey_naked)
        group audrey_top auto variant nopreg when audrey and not audrey_pregnant and not (audrey_topless or audrey_naked)
        attribute audrey_nohaircut when audrey


        attribute aletta
        attribute aletta_pregnant when aletta
        attribute aletta_collar when aletta
        attribute aletta_glasses when aletta
        group multiple auto variant aletta_piercings when aletta
        group aletta_bot auto variant preg when aletta and aletta_pregnant and not (aletta_bottomless or aletta_naked)
        group aletta_bot auto variant nopreg when aletta and not aletta_pregnant and not (aletta_bottomless or aletta_naked)
        group aletta_top auto variant preg when aletta and aletta_pregnant and not (aletta_topless or aletta_naked)
        group aletta_top auto variant nopreg when aletta and not aletta_pregnant and not (aletta_topless or aletta_naked)
        group aletta_hair auto when aletta


        group cherie auto when cherie

        attribute cherie_pregnant variant desk when cherie and desk
        attribute cherie_collar variant desk when cherie and desk
        group multiple auto variant cherie_piercings_desk when cherie and desk
        group cherie_top_preg auto variant desk when cherie and desk and cherie_pregnant and not (cherie_topless or cherie_naked)
        group cherie_top_nopreg auto variant desk when cherie and desk and not cherie_pregnant and not (cherie_topless or cherie_naked)
        group cherie_hair auto variant desk when cherie and desk

        attribute cherie_collar variant couch when cherie and couch
        group multiple auto variant cherie_piercings_couch when cherie and couch
        group cherie_top auto variant couch when cherie and couch and not (cherie_topless or cherie_naked)
        group cherie_hair auto variant couch when cherie and couch


        attribute lavish
        attribute lavish_pregnant when lavish
        attribute lavish_collar when lavish
        attribute lavish_nohaircut when lavish
        group multiple auto variant lavish_piercings when lavish
        group lavish_bot auto variant preg when lavish and lavish_pregnant and not (lavish_bottomless or lavish_naked)
        group lavish_bot auto variant nopreg when lavish and not lavish_pregnant and not (lavish_bottomless or lavish_naked)
        group lavish_top auto variant preg when lavish and lavish_pregnant and not (lavish_topless or lavish_naked)
        group lavish_top auto variant nopreg when lavish and not lavish_pregnant and not (lavish_topless or lavish_naked)


        attribute cassidy
        attribute cassidy_pregnant when cassidy
        attribute cassidy_collar when cassidy
        group cassidy_bot auto variant preg when cassidy and cassidy_pregnant and not (cassidy_bottomless or cassidy_naked)
        group cassidy_bot auto variant nopreg when cassidy and not cassidy_pregnant and not (cassidy_bottomless or cassidy_naked)
        group cassidy_top auto variant preg when cassidy and cassidy_pregnant and not (cassidy_topless or cassidy_naked)
        group cassidy_top auto variant nopreg when cassidy and not cassidy_pregnant and not (cassidy_topless or cassidy_naked)
        attribute cassidy_nohaircut when cassidy
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
