init 5 python:
    class BookstorePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"BookstorePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not amy.flags.gone_forever and amy.room == "bookstore":
                    attr.add('amy')
                if not bree.flags.gone_forever and bree.room == "bookstore":
                    attr.add('bree')
                if not harmony.flags.gone_forever and harmony.room == "bookstore":
                    attr.add('harmony')
                if not minami.hidden and minami.room == "bookstore":
                    attr.add('minami')
            
            
            if active_girl.id in ["amy", "bree", "harmony", "minami"]:
                if enable_debug_picker:
                    renpy.log(f"BookstorePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"BookstorePicker result: {attr}")
            return attr

    Room.find("bookstore").lively_npc = ["amy", "bree", "harmony", "minami"]

init 6:
    layeredimage bg bookstore:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker, OutfitPicker, BookstorePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_nose null
        attribute bree_tongue null
        attribute harmony_nose null
        attribute harmony_tongue null
        attribute minami_clit null
        attribute minami_ears null
        attribute minami_navel null
        attribute minami_pregnant_navel null


        always "bookstore"


        attribute harmony
        attribute harmony_pregnant when harmony
        attribute harmony_collar when harmony
        group multiple auto variant harmony_piercings when harmony
        attribute harmony_nohaircut when harmony
        group harmony_bot auto variant nopreg when harmony and not harmony_pregnant
        group harmony_bot auto variant preg when harmony and harmony_pregnant
        group harmony_top auto variant nopreg when harmony and not harmony_pregnant
        group harmony_top auto variant preg when harmony and harmony_pregnant


        attribute minami
        attribute minami_pregnant when minami
        attribute minami_collar when minami
        group multiple auto variant minami_piercings when minami
        group minami_hair auto when minami
        group minami_bot auto variant nopreg when minami and not minami_pregnant
        group minami_bot auto variant preg when minami and minami_pregnant
        group minami_top auto variant nopreg when minami and not minami_pregnant
        group minami_top auto variant preg when minami and minami_pregnant


        attribute amy
        attribute amy_pregnant when amy
        attribute amy_collar when amy
        group multiple auto variant amy_piercings when amy
        attribute amy_nohaircut when amy
        group amy_bot auto variant nopreg when amy and not amy_pregnant
        group amy_bot auto variant preg when amy and amy_pregnant
        group amy_top auto variant nopreg when amy and not amy_pregnant
        group amy_top auto variant preg when amy and amy_pregnant


        attribute bree
        attribute bree_pregnant when bree
        attribute bree_collar when bree
        group multiple auto variant bree_piercings when bree
        group bree_bot auto variant nopreg when bree and not bree_pregnant
        group bree_bot auto variant preg when bree and bree_pregnant
        group bree_top auto variant nopreg when bree and not bree_pregnant
        group bree_top auto variant preg when bree and bree_pregnant
        attribute bree_nohaircut when bree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
