init 5 python:
    class PubPlayPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PubPlayPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not bree.hidden and bree.room == "pubplay":
                    attr.add('bree')
                if not lavish.flags.gone_forever and lavish.room == "pubplay":
                    attr.add('lavish')
                if not palla.flags.gone_forever and palla.room == "pubplay":
                    attr.add('palla')
                if not minami.hidden and minami.room == "pubplay":
                    attr.add('minami')
            
            
            if active_girl.id in ["bree", "lavish", "minami", "palla"]:
                if enable_debug_picker:
                    renpy.log(f"PubPlayPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PubPlayPicker result: {attr}")
            return attr

    Room.find("pubplay").lively_npc = ["bree", "lavish", "minami", "palla"]

init 6:
    layeredimage bg pubplay:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, PubPlayPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_pregnant_navel null
        attribute bree_tongue null
        attribute lavish_clit null
        attribute lavish_tongue null
        attribute minami_clit null
        attribute minami_ears null
        attribute minami_navel null
        attribute minami_nipples null
        attribute minami_nose null
        attribute minami_pregnant_navel null
        attribute palla_clit null
        attribute palla_glasses null
        attribute palla_navel null
        attribute palla_pregnant_navel null
        attribute palla_tongue null


        always "pubplay"


        attribute bree
        attribute bree_pregnant when bree
        attribute bree_collar when bree
        group multiple auto variant bree_piercings when bree
        group bree_bot auto variant nopreg when bree and not bree_pregnant
        group bree_bot auto variant preg when bree and bree_pregnant
        group bree_top auto variant nopreg when bree and not bree_pregnant
        group bree_top auto variant preg when bree and bree_pregnant
        attribute bree_nohaircut when bree


        attribute palla
        attribute palla_pregnant when palla
        attribute palla_collar when palla
        group multiple auto variant palla_piercings_back when palla
        group palla_bot auto variant nopreg when palla and not palla_pregnant
        group palla_bot auto variant preg when palla and palla_pregnant
        group palla_top auto variant nopreg when palla and not palla_pregnant
        group palla_top auto variant preg when palla and palla_pregnant
        group multiple auto variant palla_piercings_front when palla
        attribute palla_nohaircut when palla


        attribute minami
        attribute minami_pregnant when minami
        attribute minami_collar when minami
        group minami_bot auto variant nopreg when minami and not minami_pregnant
        group minami_bot auto variant preg when minami and minami_pregnant
        group minami_top auto variant nopreg when minami and not minami_pregnant
        group minami_top auto variant preg when minami and minami_pregnant
        group minami_hair auto when minami


        attribute lavish
        attribute lavish_pregnant when lavish
        attribute lavish_collar when lavish
        group multiple auto variant lavish_piercings_back when lavish
        group lavish_bot auto variant nopreg when lavish and not lavish_pregnant
        group lavish_bot auto variant preg when lavish and lavish_pregnant
        group lavish_top auto variant nopreg when lavish and not lavish_pregnant
        group lavish_top auto variant preg when lavish and lavish_pregnant
        group multiple auto variant lavish_piercings_front when lavish
        attribute lavish_nohaircut when lavish
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
