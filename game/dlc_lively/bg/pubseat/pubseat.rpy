init 5 python:
    class PubSeatPicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"PubSeatPicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not audrey.flags.gone_forever and audrey.room == "pubseat":
                    attr.add('audrey')
                if not kleio.flags.gone_forever and kleio.room == "pubseat":
                    attr.add('kleio')
                if not lexi.flags.gone_forever and lexi.room == "pubseat":
                    attr.add('lexi')
                if not morgan.flags.gone_forever and morgan.room == "pubseat":
                    attr.add('morgan')
                if not reona.flags.gone_forever and reona.room == "pubseat":
                    attr.add('reona')
            
            
            if active_girl.id in ["audrey", "kleio", "lexi", "morgan", "reona"]:
                if enable_debug_picker:
                    renpy.log(f"PubSeatPicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"PubSeatPicker result: {attr}")
            return attr

    Room.find("pubseat").lively_npc = ["audrey", "kleio", "lexi", "morgan", "reona"]

init 6:
    layeredimage bg pubseat:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker, PubSeatPicker], append_npc_from_attributes=True)


        attribute empty null            
        attribute force_display null        
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_tongue null
        attribute kleio_clit null
        attribute kleio_ears null
        attribute kleio_navel null
        attribute kleio_nipples null
        attribute kleio_nose null
        attribute kleio_pregnant_navel null
        attribute kleio_tongue null
        attribute lexi_clit null
        attribute lexi_navel null
        attribute lexi_nose null
        attribute lexi_pregnant_navel null
        attribute lexi_tongue null
        attribute morgan_clit null
        attribute morgan_navel null
        attribute morgan_nipples null
        attribute morgan_tongue null
        attribute reona_clit null
        attribute reona_tongue null


        always "pubseat"


        attribute morgan
        attribute morgan_pregnant when morgan
        attribute morgan_makeup when morgan
        attribute morgan_collar when morgan
        group morgan_hair auto when morgan
        group multiple auto variant morgan_piercings when morgan
        group morgan_bot auto variant preg when morgan and morgan_pregnant
        group morgan_bot auto variant nopreg when morgan and not morgan_pregnant
        group morgan_top auto variant preg when morgan and morgan_pregnant
        group morgan_top auto variant nopreg when morgan and not morgan_pregnant


        attribute audrey
        attribute audrey_pregnant when audrey
        attribute audrey_collar when audrey
        attribute audrey_nohaircut when audrey
        group multiple auto variant audrey_piercings when audrey
        group audrey_bot auto variant preg when audrey and audrey_pregnant
        group audrey_bot auto variant nopreg when audrey and not audrey_pregnant
        group audrey_top auto variant preg when audrey and audrey_pregnant
        group audrey_top auto variant nopreg when audrey and not audrey_pregnant


        attribute kleio
        attribute kleio_pregnant when kleio
        attribute kleio_collar when kleio
        group kleio_tattoo auto when kleio
        group kleio_bot auto variant preg when kleio and kleio_pregnant
        group kleio_bot auto variant nopreg when kleio and not kleio_pregnant
        group kleio_top auto variant preg when kleio and kleio_pregnant
        group kleio_top auto variant nopreg when kleio and not kleio_pregnant
        group kleio_hair auto when kleio


        attribute lexi
        attribute lexi_collar when lexi
        group multiple auto variant lexi_piercings when lexi
        group lexi_bot auto when lexi
        group lexi_top auto when lexi
        attribute lexi_nohaircut when lexi


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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
