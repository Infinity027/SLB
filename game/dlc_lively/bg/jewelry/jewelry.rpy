init 5 python:
    class JewelryStorePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"JewelryStorePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not alexis.flags.gone_forever and alexis.room == "jewelrystore":
                    attr.add('alexis')
                if not audrey.flags.gone_forever and audrey.room == "jewelrystore":
                    attr.add('audrey')
                if not cherie.flags.gone_forever and cherie.room == "jewelrystore":
                    attr.add('cherie')
                if not lexi.flags.gone_forever and lexi.room == "jewelrystore":
                    attr.add('lexi')
                if not palla.flags.gone_forever and palla.room == "jewelrystore":
                    attr.add('palla')
                if not reona.flags.gone_forever and reona.room == "jewelrystore":
                    attr.add('reona')
            
            
            if active_girl.id in ["alexis", "audrey", "cherie", "lexi", "palla", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"JewelryStorePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"JewelryStorePicker result: {attr}")
            return attr

    Room.find("jewelrystore").lively_npc = ["alexis", "audrey", "cherie", "lexi", "palla", "reona"]

init 6:
    layeredimage bg jewelrystore:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, JewelryStorePicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute alexis_clit null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_navel null
        attribute audrey_nipples null
        attribute audrey_nose null
        attribute audrey_pregnant_navel null
        attribute audrey_tongue null
        attribute cherie_clit null
        attribute cherie_navel null
        attribute cherie_nose null
        attribute cherie_pregnant_navel null
        attribute lexi_clit null
        attribute lexi_navel null
        attribute lexi_pregnant_navel null
        attribute lexi_tongue null
        attribute palla_clit null
        attribute palla_ears null
        attribute palla_glasses null
        attribute palla_navel null
        attribute palla_nose null
        attribute palla_pregnant_navel null
        attribute palla_tongue null
        attribute reona_clit null
        attribute reona_navel null
        attribute reona_pregnant_navel null
        attribute reona_tongue null


        always "jewelrystore"


        attribute reona
        attribute reona_pregnant when reona
        attribute reona_collar when reona
        group multiple auto variant reona_piercings when reona
        group reona_bot auto variant preg when reona and reona_pregnant
        group reona_bot auto variant nopreg when reona and not reona_pregnant
        group reona_top auto when reona
        group reona_top auto variant preg when reona and reona_pregnant
        group reona_top auto variant nopreg when reona and not reona_pregnant
        attribute reona_pureglasses when reona
        group reona_hair auto when reona


        attribute lexi
        attribute lexi_pregnant when lexi
        attribute lexi_collar when lexi
        group multiple auto variant lexi_piercings when lexi
        group lexi_top auto when lexi
        attribute lexi_nohaircut when lexi
        attribute lexi_ears when lexi


        attribute palla
        attribute palla_pregnant when palla
        attribute palla_collar when palla
        group multiple auto variant palla_piercings when palla
        group palla_top auto variant preg when palla and palla_pregnant
        group palla_top auto variant nopreg when palla and not palla_pregnant
        attribute palla_nohaircut when palla


        attribute cherie
        attribute cherie_pregnant when cherie
        attribute cherie_collar when cherie
        group multiple auto variant cherie_piercings when cherie
        group cherie_top auto variant preg when cherie and cherie_pregnant
        group cherie_top auto variant nopreg when cherie and not cherie_pregnant
        group cherie_hair auto when cherie


        attribute alexis
        attribute alexis_pregnant when alexis
        attribute alexis_collar when alexis
        group multiple auto variant alexis_piercings when alexis
        group alexis_bot auto variant preg when alexis and alexis_pregnant
        group alexis_bot auto variant nopreg when alexis and not alexis_pregnant
        group alexis_top auto variant preg when alexis and alexis_pregnant
        group alexis_top auto variant nopreg when alexis and not alexis_pregnant
        attribute alexis_nohaircut when alexis


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        group multiple auto variant audrey_piercings when audrey
        group audrey_bot auto variant preg when audrey and audrey_pregnant
        group audrey_bot auto variant nopreg when audrey and not audrey_pregnant
        group audrey_top auto variant preg when audrey and audrey_pregnant
        group audrey_top auto variant nopreg when audrey and not audrey_pregnant
        attribute audrey_nohaircut when audrey
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
