init 5 python:
    class HousePicker(object):
        def __call__(self, attr):
            if not persistent.lively_bg or attr & {"empty"}:
                return attr
            
            if config.developer:
                attr.add('minami')
            
            
            if enable_debug_picker:
                test_result = attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment"))
                renpy.log(f"HousePicker test: {test_result}\n    - 'attr & force_display': {attr & set(['force_display'])}\n    - 'not game.active_date or isinstance(game.active_date, NoDateEvent)': {not game.active_date or isinstance(game.active_date, NoDateEvent)}\n    - 'not IN_EVENT_WITH': {not IN_EVENT_WITH}\n    - 'not globals().get(appointment)': {not globals().get('appointment')}")
            
            
            if attr & {"force_display"} or ((not game.active_date or isinstance(game.active_date, NoDateEvent)) and not IN_EVENT_WITH and not globals().get("appointment")):
                
                
                if not kylie.hidden and kylie.room == "house":
                    attr.add('kylie')
                if not minami.hidden and minami.room == "house":
                    attr.add('minami')
            
            
            if active_girl.id in ["kylie", "minami"]:
                if enable_debug_picker:
                    renpy.log(f"HousePicker remove active/interact girl: {active_girl.id}")
                attr.discard(active_girl.id)
            
            
            if enable_debug_picker:
                renpy.log(f"HousePicker result: {attr}")
            return attr

    Room.find("house").lively_npc = ["kylie", "minami"]

init 6:
    layeredimage bg house:
        attribute_function MultiPickers([DayNightPicker, SeasonPicker, PiercingsPicker, CollarPicker, HaircutPicker, OutfitPicker,VehiclePicker, HousePicker], append_npc_from_attributes=True)


        attribute night null
        attribute day null
        attribute empty null            
        attribute force_display null        
        attribute naked null
        attribute bottomless null
        attribute topless null
        attribute kylie_clit null
        attribute kylie_ears null
        attribute kylie_navel null
        attribute kylie_nipples null
        attribute kylie_nose null
        attribute kylie_pregnant null
        attribute kylie_pregnant_navel null
        attribute kylie_tongue null
        attribute minami_ears null
        attribute minami_nipples null


        attribute sportscar null
        attribute car null
        attribute bike null

        group season auto variant night when night and not (sportscar or car or bike)
        group season auto variant day when day and not (sportscar or car or bike)

        group season auto variant night_sportscar when night and sportscar and not (car or bike)
        group season auto variant day_sportscar when day and sportscar and not (car or bike)

        group season auto variant night_car when night and car and not (sportscar or bike)
        group season auto variant day_car when day and car and not (sportscar or bike)

        group season auto variant night_bike when night and bike and not (car or sportscar)
        group season auto variant day_bike when day and bike and not (car or sportscar)


        attribute kylie
        attribute kylie_casual when kylie
        attribute kylie_nohaircut when kylie


        group season_fg auto variant day when day
        group season_fg auto variant night when night


        attribute minami
        attribute minami_collar when minami
        group multiple auto variant piercings_minami when minami
        group minami_hair auto when minami
        always "bg_house_minami_bot_minami_underwear" when minami and minami_casual and not (minami_naked or minami_bottomless)
        group minami_bot auto when minami and not (minami_naked or minami_bottomless)
        group minami_top auto when minami and not (minami_naked or minami_topless)


        always "bg_house_butterfly" when minami
        always:
            "snow"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
