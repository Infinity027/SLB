init python:
    Event(**{
    "name": "common_ending",
    "label": "common_ending",
    "priority": 1000,
    "conditions": [
        IsDayOfWeek("7"),
        IsHour(6, 22),
        "any(Person.get_fiances())"
        ],
    "do_once": False,
    "once_hour": True,
    })

label common_ending:












    python:
        harem_fiances = dict()
        fiances = set(Person.get_fiances())
        available_weddings = list()

        for fiance in fiances:
            ending_label = f"{fiance.id}_{hero.gender}_ending"
            if renpy.has_label(ending_label):
                available_weddings.append((f"{fiance.name}", renpy.Choice(ending_label, displayed_fiances=[fiance.id])))
            else:
                renpy.log(f"WARNING: Missing individual ending label: {ending_label}")
        available_weddings = sorted(available_weddings, key=lambda x: x[0])

        harems_weddings = list()
        available_harems = set([harem for fiance in fiances for harem in fiance.get_harems() ])
        for harem in available_harems:
            fiances_intersection = set(harem.active_members_objects) & fiances
            if len(fiances_intersection) >= 2:
                harem_fiances[harem.id] = sorted(fiances_intersection, key=lambda x: x.id)

        for k,v in harem_fiances.items():
            harems_partial_combinations = list(reversed(list(itertools.chain.from_iterable(itertools.combinations(v, r) for r in range(2, len(v) + 1)))))
            for partial_harem in harems_partial_combinations:
                ending_label = f"{'_'.join([f.id for f in partial_harem])}_{hero.gender}_ending"
                if renpy.has_label(ending_label) and Harem.find_by_name(k).test():
                    harems_weddings.append((f"{k.capitalize()} Harem", renpy.Choice(ending_label, displayed_fiances=[f.id for f in partial_harem])))
                elif not renpy.has_label(ending_label):
                    renpy.log(f"WARNING: Missing harem ending label: {k.capitalize()} {ending_label}")
                else:
                    renpy.log(f"INFO: Failing Harem ending conditions: {k.capitalize()} {ending_label}")

        available_weddings.extend(sorted(harems_weddings, key=lambda x: x[0]))
    if available_weddings:
        $ narrator("Who should I wed?", interact=False)
        $ wedding_choice = renpy.display_menu(available_weddings, screen="orbit_choice", choice_label="Who should I wed?")
        jump expression wedding_choice
    return


label date_do_date(date):
    $ date_girl.object = date.participants[0]
    $ game.active_date = date
    $ active_girl.object = date_girl
    $ game.flags.disable_clothing_policy = True
    if game.hour in [14, 20]:
        $ dif = 20
    elif game.hour in [15, 21]:
        $ dif = 30
        $ date_girl.love -= 1
    elif game.hour in [16, 22]:
        $ dif = 40
        $ date_girl.love -= 2
    elif game.hour in [17, 23]:
        $ dif = 50
        $ date_girl.love -= 3
    $ date.abort = False
    $ date.stay = True
    $ date.stay_coffee = True
    $ afternoon = False
    $ evening = False
    $ dinner = False
    $ night = False


    $ renpy.dynamic("valid_events")
    $ valid_events = BeforeDateEvent.valid_events()

    while valid_events:
        $ event = valid_events.pop(0)
        call event_do (event) from _call_event_do_5


    if date.abort:
        $ game.active_date = NoDateEvent()
        $ active_girl.object = None
        $ date_girl.object = None
        $ game.flags.disable_clothing_policy = False
        if game.room.startswith("date_"):
            $ game.room = game.room[5:]
        return

    $ date_girl.flags.dates += 1

    if game.calendar.is_today(*date_girl.birthday) and date_girl.flags.birthdayknown and renpy.has_label(f"{date_girl.id}_birthday_date_{hero.gender}"):

        if game.hour in [14, 15, 16, 17] and date_girl.id in ["audrey", "lavish", "lexi", "reona", "scottie", "morgan"]:
            call expression f"{date_girl.id}_birthday_date_{hero.gender}" from _call_expression_466
            $ date.stay = False
            $ game.pass_time(2)
        elif game.hour in [20, 21, 22, 23] and date_girl.id not in ["audrey", "lavish", "lexi", "reona", "scottie", "morgan"]:
            call expression f"{date_girl.id}_birthday_date_{hero.gender}" from _call_expression_407
            $ game.pass_time(2)
            $ date.stay = False
    while date.stay:
        $ active_girl.object = date_girl
        if game.room not in ["street", "map"]:
            if game.room.startswith("date_"):
                $ game.room = game.room.strip("date_")

            if game.room == "cinemaroom":
                $ game.room = "cinema"
            scene expression f"bg {game.room}"
        else:
            $ game.room = "street"
            scene bg street
        if game.hour in [14, 15, 16, 17] and not afternoon:
            $ renpy.show(f"{date_girl.id} casual")
            $ afternoon = True
            $ dif += 25
            call choose_and_do_date from _date_do_date_afternoon
        elif game.hour == 18 and date.score >= dif and not evening:
            $ evening = True
            $ renpy.show(f"{date_girl.id} casual")
            $ dif += 25
            date_girl.say "I really don't want to end things right now, maybe we can do something else?"
            menu:
                "Yes":
                    call expression f"date_do_date_dialogues_1_{hero.gender}" from _call_expression_408
                    $ game.pass_time(2)
                    call choose_and_do_date from _date_do_date_evening
                "No":
                    call expression f"date_do_date_dialogues_2_{hero.gender}" from _call_expression_409
                    $ date.stay = False
        elif game.hour in [20, 21, 22, 23] and not dinner:
            if game.calendar.is_today(*date_girl.birthday) and date_girl.flags.birthdayknown and renpy.has_label(f"{date_girl.id}_birthday_date_{hero.gender}"):
                call expression f"{date_girl.id}_birthday_date_{hero.gender}" from _call_expression_457
                $ game.pass_time(2)
                $ date.stay = False
            else:
                $ dinner = True
                $ renpy.show(f"{date_girl.id} casual")
                $ dif += 25
                call choose_and_do_date from _date_do_date_dinner
        elif game.hour >= 0 and game.week_day in [6, 7] and game.active_date.score >= dif and not night and (not hasattr(game.active_date, "skip_nightclub") or (hasattr(game.active_date, "skip_nightclub") and not game.active_date.skip_nightclub)):
            $ night = True
            $ renpy.show(date_girl.id)
            if date_girl.flags.nodance:
                date_girl.say "It was really fun."
            else:
                if game.room == "nightclub":
                    date_girl.say "What do you say we stay a little more?"
                else:
                    date_girl.say "What do you say we end this at the club?"
                if "nightclub" in DATES and DATES["nightclub"].test():
                    $ result = renpy.display_menu([("Yes", True), ("No", False)])
                    if result:
                        call expression f"date_do_date_dialogues_3_{hero.gender}" from _call_expression_410
                        call date_do (DATES["nightclub"]) from _date_do_date_night
                    else:
                        call expression f"date_do_date_dialogues_4_{hero.gender}" from _call_expression_411
                else:
                    call expression f"date_do_date_dialogues_5_{hero.gender}" from _call_expression_412
                    $ date.stay = False
        else:

            $ cache_date_girl = date_girl.object
            $ cache_active_girl = active_girl.object
            $ cache_smartphone_girl = smartphone_girl.object

            $ renpy.dynamic("valid_events")
            $ valid_events = AfterDateEvent.valid_events()

            while valid_events:
                $ event = valid_events.pop(0)
                call event_do (event) from _call_event_do_4
                if (date_girl.object and date_girl.object != cache_date_girl) or (active_girl.object and active_girl.object != cache_active_girl) or (smartphone_girl.object and smartphone_girl.object != cache_smartphone_girl) or (event.quit):
                    $ valid_events = []

            if not date_girl:
                $ date_girl.object = cache_date_girl
            if not active_girl:
                $ active_girl.object = cache_active_girl

            if date.stay_coffee:
                $ renpy.show(date_girl.id)
                call expression f"date_stay_coffee_{hero.gender}" from _call_expression_413
            $ date.stay = False
            $ renpy.hide(date_girl.id)



    if not date.abort:
        if date_girl.is_female and date.score >= 90 and date_girl.lesbian > MAX_LES_GUY_KISS and hero.is_male:
            $ date_girl.lesbian -= 1
        elif date_girl.is_female and date.score >= 90 and date_girl.lesbian < MIN_LES_GIRL_KISS and hero.is_female:
            $ date_girl.lesbian += 1
        $ date_girl.love += int((date.score * 0.2) - 10)
    $ game.active_date = NoDateEvent()
    $ active_girl.object = None
    $ date_girl.object = None
    $ game.flags.disable_clothing_policy = False
    if game.room.startswith("date_"):
        $ game.room = game.room[5:]
    return

label date_stay_coffee_male:
    if renpy.has_label(f"{date_girl.id}_ask_fuck_date_{hero.gender}"):
        call expression f"{date_girl.id}_ask_fuck_date_{hero.gender}" from _call_expression_414
    else:
        call date_ask_fuck_date from _call_date_ask_fuck_date
    if _return:
        $ renpy.hide(date_girl.id)
        call expression f"{date_girl.id}_fuck_date_{hero.gender}" pass (_return) from _call_expression_415
    return

label date_ask_fuck_date:
    if renpy.has_label(f"{date_girl.id}_fuck_date_{hero.gender}") and (
        game.active_date.score >= (100 - date_girl.flags.drinks * 5) and (
        date_girl.love >= 100 or date_girl.flags.drinks >= 3 or (
        date_girl.id == "reona" and date_girl.purity < 50)) and not date_girl.flags.nosex):
        if renpy.has_label(f"{date_girl.id}_ask_hot_coffee_{hero.gender}"):
            call expression f"{date_girl.id}_ask_hot_coffee_{hero.gender}" from _call_expression_531
        else:
            date_girl.say "Maybe I could, you know..."
            date_girl.say "Come for a hot coffee."
        menu:
            "Yes" if hero.stamina and (not date_girl.flags.addressknown or date_girl.id not in ["audrey"]):
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_416
                return "hero"
            "My place" if hero.stamina and date_girl.flags.addressknown and date_girl.id in ["audrey"]:
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_532
                return "hero"
            "Your place" if hero.stamina and date_girl.flags.addressknown and date_girl.id in ["audrey"]:
                call expression f"date_ask_fuck_date_dialogues_1_{hero.gender}" from _call_expression_533
                return date_girl.id
            "No" if hero.stamina:
                call expression f"date_ask_fuck_date_dialogues_2_{hero.gender}" from _call_expression_417
                $ date_girl.love -= 5
                if date_girl.id == "reona" and date_girl.purity < 50:
                    $ reona.sub -= 2
                return False
            "No. I'm exhausted." if not hero.stamina:
                "I had too much 'hot coffee' lately, I should rest."
                call expression f"date_ask_fuck_date_dialogues_3_{hero.gender}" from _call_expression_418
                $ date_girl.love -= 5
                if date_girl.id == "reona" and date_girl.purity < 50:
                    $ reona.sub -= 5
                return False
    else:
        date_girl.say "It was really nice."
    return False

label choose_and_do_date:
    show bg street

    if sum([afternoon, evening, dinner]) == 1:
        if game.calendar.is_today("valentine") and renpy.has_label(f"{date_girl.id}_date_intro_valentine_{hero.gender}"):
            call expression f"{date_girl.id}_date_intro_valentine_{hero.gender}" from _call_expression_419
        elif game.calendar.is_today("halloween") and renpy.has_label(f"{date_girl.id}_date_intro_halloween_{hero.gender}"):
            call expression f"{date_girl.id}_date_intro_halloween_{hero.gender}" from _call_expression_420
        elif game.calendar.is_today("christmas")and renpy.has_label(f"{date_girl.id}_date_intro_christmas_{hero.gender}"):
            call expression f"{date_girl.id}_date_intro_christmas_{hero.gender}" from _call_expression_421
        elif game.calendar.is_today(*date_girl.birthday) and date_girl.flags.birthdayknown and renpy.has_label(f"{date_girl.id}_date_intro_birthday_{hero.gender}"):
            call expression f"{date_girl.id}_date_intro_birthday_{hero.gender}" from _call_expression_422
        elif game.calendar.is_today(*hero.birthday) and renpy.has_label(f"{date_girl.id}_date_intro_mc_birthday_{hero.gender}"):
            call expression f"{date_girl.id}_date_intro_mc_birthday_{hero.gender}" from _call_expression_423

    $ spots = game.get_dates()
    $ spot = "None"
    if spots:
        $ n_spots = [(date_spot.display_name, date_spot) for date_spot in spots]
        call screen select(n_spots, "date spots")
        $ spot = _return
        $ renpy.hide(date_girl.id)
    else:
        "There is no dating place I could or would take her to right now."
    if spot != "None":
        $ day = game.days_played
        $ hour = game.hour
        $ game.active_date.location = spot
        call date_do (spot) from _choose_and_do_date
    elif hero.activity:
        $ hero.cancel_activity()
    return

label date_do(date):
    $ game.active_date.location = date
    if date_girl.flags.last_date_location == date.name:
        $ game.active_date.score -= 10
    $ date_girl.flags.last_date_location = date.name
    $ date_girl.flags.last_date_day = game.days_played
    if date.name in date_girl.desire_factors:
        $ game.active_date.score += 25
    elif f"not_{date.name}" in date_girl.desire_factors:
        $ game.active_date.score -= 25
    if date.money_cost:
        $ hero.money -= date.money_cost
    $ starting_time = game.hour
    $ starting_day = game.day
    $ date_girl.set_room(f"date_{date.name}")
    $ game.room = f"date_{date.name}"
    if date.clothes:
        $ date_do_old_girl_clothes = game.girl_clothes
        $ game.girl_clothes = date.clothes

    scene expression f"bg date_{date.name}"
    if hasattr(date, "bypass_greetings") and date.bypass_greetings:
        pass
    else:
        call expression f"{date_girl.id}_greet" from _date_do_greet
    if renpy.has_label(f"{date_girl.id}_date_{date.name}_{hero.gender}"):
        call expression f"{date_girl.id}_date_{date.name}_{hero.gender}" from _date_do_girl_date
    else:
        call expression f"date_{date.name}" from _date_do_date

    $ max_time = (24 - game.hour) % 6

    if game.active_date.stay == False:
        return
    call enter_room (back=date.name, room_present_girls=[date_girl.id], max_time=max_time) from _call_enter_room_2

    python:
        if date_girl:
            for n in date.needs.keys():
                hero[n] += date.needs[n]
            for s in date.attributes.keys():
                hero[s] += date.attributes[s]
            love_gain = date.love_gain
            for g in date_girl.desire_factors:
                if g == date.name:
                    love_gain = love_gain * 1.5
                elif g == f"not_{date.name}":
                    love_gain = love_gain / 2
            date_girl.love += love_gain
        if starting_day == game.day and game.hour < starting_time + max_time and game.hour != 0 and game.active_date.stay:
            game.pass_time(starting_time + max_time - game.hour, True)
        if date.clothes:
            game.girl_clothes = date_do_old_girl_clothes
        room_present_girls = None
    return


label time_for_our_date:
    $ renpy.dynamic("appointments", "appointment")
    $ renpy.show(active_girl.id)
    $ appointments = hero.calendar.get_appointments(girl=active_girl.id)
    if len(appointments) == 0:
        return
    $ appointment = appointments[0]
    active_girl.say "Let's go on our date [hero.name]."
    menu:
        "Yes":
            call expression f"time_for_our_date_dialogues_1_{hero.gender}" from _call_expression_424
            $ hero.calendar.remove(game.days_played, appointment)
            if isinstance(appointment, Appointment) and appointment.do() != None:
                call expression appointment.do() pass (appointment) from _call_expression_138
        "No":
            call expression f"time_for_our_date_dialogues_2_{hero.gender}" from _call_expression_425
    if active_girl:
        $ renpy.hide(active_girl.id)
    return

label ask_out:
    if renpy.has_label(f"{active_girl.id}_ask_out"):
        call expression f"{active_girl.id}_ask_out" from _call_expression
    else:
        call expression f"{active_girl.id}_greet" from _call_expression_1
        $ renpy.show(active_girl.id)
        python:
            choices = []
            if game.hour < 20:
                if not hero.calendar.has_appointment(game.days_played, 14, active_girl.id) and not hero.calendar.has_appointment(game.days_played, 20, active_girl.id) and not game.active_date:
                    choices.append(("this", game.days_played))

            for i in range(1, 7):
                day = game.week_day + i
                if day > 7:
                    day -= 7
                if not hero.calendar.has_appointment(game.days_played + i, 14, active_girl.id) and not hero.calendar.has_appointment(game.days_played + i, 20, active_girl.id):
                    if i == 1:
                        choices.append(("tomorrow", game.days_played + i))
                    else:
                        choices.append((f"next {game.get_day_str(day)}", game.days_played + i))

            str_day, day = randchoice(choices)
            if game.hour < 14 :
                choices = [("afternoon", 14), ("evening", 20)]
                str_hour, hour = randchoice(choices)
            else:
                str_hour, hour = ("evening", 20)
        active_girl.say "Would you like to go somewhere with me [str_day] [str_hour]?"
        $ choices = [("Yes", 1), ("No", 2)]
        if renpy.display_menu(choices) == 1:
            call expression f"ask_out_dialogues_1_{hero.gender}" from _call_expression_426
            $ hero.calendar.add(day, DateAppointment(hour, active_girl.id))
            $ active_girl.love += 1
        else:
            call expression f"ask_out_dialogues_2_{hero.gender}" from _call_expression_427
            $ active_girl.love -= 1
        $ renpy.hide(active_girl.id)
    return

label are_you_sick:
    call expression f"{active_girl.id}_greet" from _call_expression_8
    $ renpy.show(active_girl.id)
    active_girl.say "You don't look so well..."
    active_girl.say "You should rest."
    $ active_girl.love += 1
    $ renpy.hide(active_girl.id)
    return

label auto_chat:
    if renpy.has_label(f"{active_girl.id}_auto_chat"):
        call expression f"{active_girl.id}_auto_chat" from _call_expression_9
    else:
        call expression f"{active_girl.id}_greet" from _call_expression_10
        $ renpy.scene()
        $ renpy.show(f"bg {game.room}")
        $ renpy.show(active_girl.id)
        active_girl.say "Do you have some time to talk?"
        $ choices = [("No, sorry.", 1), ("Yeah, sure.", 2)]
        $ result = renpy.display_menu(choices)
        if result == 1:
            $ active_girl.love -= 1
        else:
            $ active_girl.set_flag("daily_interact", 1, 1, "+")
            $ chat = active_girl.get_chat
            if game.room in ["livingroom", "pub", "pubplay", "pubseat", "park", "coffeeshop"]:
                $ renpy.show(f"chatting {active_girl.id} {game.room}")
            else:
                $ renpy.show(active_girl.id)
            call expression chat from _call_expression_11
            $ renpy.hide("chatting")
        $ renpy.hide(active_girl.id)
    return

label auto_greet:
    $ renpy.show(active_girl.id)
    call expression f"{active_girl.id}_greet" from _call_expression_13
    $ renpy.hide(active_girl.id)
    return

label send_text:
    $ nvl_mode = "phone"
    nvl clear
    play sound cell_vibrate
    pause 1.0
    "It's a text from [active_girl.name]."

    if date_girl:
        $ result = renpy.display_menu([("Ignore it", 1), ("Read it", 2)])
        if result == 1:
            $ active_girl.love += 1
            $ renpy.return_statement()
    $ result = randint(0, active_girl.love())
    if result >= 150 and active_girl.sexperience >= 1:
        if renpy.has_label(f"{active_girl.id}_dirty_texts") and randint(0, 2) >= 1:
            call expression f"{active_girl.id}_dirty_texts" from _call_expression_428
        else:
            $ t = randchoice(girl_dirty_texts)
            while t:
                $ line = t.pop(0)
                if line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=line[1]) from _call_expression_429
                else:
                    call expression f"text_sentence_{active_girl.id}" pass (sentence=line[1]) from _call_expression_506
        $ active_girl.love += 2
    elif result >= 75 and active_girl.flags.kiss >= 1:
        if renpy.has_label(f"{active_girl.id}_flirty_texts") and randint(0, 2) >= 1:
            call expression f"{active_girl.id}_flirty_texts" from _call_expression_430
        else:
            $ t = randchoice(npc_flirty_texts)
            while t:
                $ line = t.pop(0)
                if line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=line[1]) from _call_expression_431
                else:
                    call expression f"text_sentence_{active_girl.id}" pass (sentence=line[1]) from _call_expression_507
        $ active_girl.love += 1
    else:
        if renpy.has_label(f"{active_girl.id}_friendly_texts") and randint(0, 2) >= 1:
            call expression f"{active_girl.id}_friendly_texts" from _call_expression_432
        else:
            $ t = randchoice(npc_friendly_texts)
            while t:
                $ line = t.pop(0)
                if line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=line[1]) from _call_expression_433
                else:
                    call expression f"text_sentence_{active_girl.id}" pass (sentence=line[1]) from _call_expression_508
        $ active_girl.love += 1
    return

label give_phone_number:
    call expression f"{active_girl.id}_greet" from _call_expression_15
    $ renpy.show(active_girl.id)
    active_girl.say "We should exchange our phone numbers."
    call expression f"give_phone_number_dialogues_1_{hero.gender}" from _call_expression_434
    $ hero.smartphone_contacts.append(active_girl.id)
    $ renpy.hide(active_girl.id)
    return

label check_condom_usage(f_npc, love=160, drinks=1, sub=None):
    $ CONDOM = False
    if not (f_npc.flags.pregnant or f_npc.flags.pill or f_npc.flags.pregrequest):
        menu:
            "Use protection" if hero.has_condom():
                $ CONDOM = hero.use_condom()
                if renpy.has_label(f"{f_npc.id}_use_condom"):
                    call expression f"{f_npc.id}_use_condom" from _call_expression_435
                    if _return in ["leave_without_gain", "leave_with_gain"]:
                        return False
                    elif _return == False:
                        $ CONDOM = False
                else:
                    "I grab a condom from the bedside table before going any further."
            "Don't use protection":
                if renpy.has_label(f"{f_npc.id}_intro_condom"):
                    call expression f"{f_npc.id}_intro_condom" from _call_expression_436
                if f_npc.force_condom_use(love=love, drinks=drinks, sub=sub):
                    if sub and renpy.has_label(f"{f_npc.id}_sub_warn_condom"):
                        call expression f"{f_npc.id}_warn_condom" from _call_expression_437
                    elif renpy.has_label(f"{f_npc.id}_warn_condom"):
                        call expression f"{f_npc.id}_warn_condom" from _call_expression_438
                    else:
                        $ renpy.say(f_npc.id, "Aren't you forgetting a little something?")
                    if sub and f_npc.sub < sub:
                        if renpy.has_label(f"{f_npc.id}_sub_condom_menu"):
                            call expression f"{f_npc.id}_sub_condom_menu" from _call_expression_439
                            return _return
                        else:
                            mike.say "You're going to take my cock raw and you're going to like it!"
                    elif f_npc.love >= love - int(love * .15):

                        if renpy.has_label(f"{f_npc.id}_force_condom"):
                            call expression f"{f_npc.id}_force_condom" from _call_expression_440
                            if _return == False:
                                $ f_npc.love -= 10
                                return False
                            $ CONDOM = True
                        else:
                            "I grab a condom."
                            $ CONDOM = hero.use_condom()
                    else:
                        scene expression f"bg {game.room}"
                        $ renpy.show(f"{f_npc.id} angry naked")
                        show fx anger
                        if renpy.has_label(f"{f_npc.id}_mad_condom"):
                            call expression f"{f_npc.id}_mad_condom" from _call_expression_441
                        else:
                            $ renpy.say(f_npc.id, "No condom, no sex.")
                        $ f_npc.love -= 10
                        return False
                else:
                    if f_npc.pregnant and renpy.has_label(f"{f_npc.id}_pregnant_condom"):
                        call expression f"{f_npc.id}_pregnant_condom" from _call_expression_442
                    elif f_npc.flags.pill and renpy.has_label(f"{f_npc.id}_pill_condom"):
                        call expression f"{f_npc.id}_pill_condom" from _call_expression_443
                    elif f_npc.flags.drugs and renpy.has_label(f"{f_npc.id}_drugs_condom"):
                        call expression f"{f_npc.id}_drugs_condom" from _call_expression_444
                    elif renpy.has_label(f"{f_npc.id}_no_condom"):
                        call expression f"{f_npc.id}_no_condom" from _call_expression_445
    return True

label cum_reaction(fuck_npc, fuck_location, sexperience_min=0, love_min=180, check_sub=False, sub_min=75):
    if hero.is_male:
        if fuck_location == "anal":
            menu:
                "Cum inside":
                    return "anal_inside"
                "Pull out" if hero.sexperience >= sexperience_min + 10:
                    return "anal_outside"
        elif fuck_location == "vaginal":
            menu:
                "Cum inside" if CONDOM:
                    return "vaginal_condom"
                "Pull out" if hero.sexperience >= sexperience_min + 5:
                    return "vaginal_outside"

                "Cum inside" if not CONDOM and fuck_npc.is_visibly_pregnant:
                    return "vaginal_inside_pregnant"

                "Cum inside" if not CONDOM and not fuck_npc.is_visibly_pregnant and fuck_npc.flags.pill:
                    return "vaginal_inside_pill"

                "Cum inside" if not CONDOM and not fuck_npc.is_visibly_pregnant and not fuck_npc.flags.pill and fuck_npc.love < love_min and check_sub and fuck_npc.sub >= sub_min and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_sub"

                "Cum inside" if not CONDOM and not fuck_npc.is_visibly_pregnant and not fuck_npc.flags.pill and fuck_npc.love < love_min and check_sub and fuck_npc.sub < sub_min and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_mad"

                "Cum inside" if not CONDOM and not fuck_npc.is_visibly_pregnant and not fuck_npc.flags.pill and fuck_npc.love < love_min and not check_sub and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_mad"

                "Cum inside" if not CONDOM and not fuck_npc.is_visibly_pregnant and not fuck_npc.flags.pill and (fuck_npc.love >= love_min or fuck_npc.flags.pregrequest or fuck_npc.is_sex_slave or fuck_npc.flags.drugs):
                    return "vaginal_inside_happy"
    else:
        if fuck_location == "anal":
            menu:
                "Let him cum inside":
                    return "anal_inside"
                "Pull him out" if hero.sexperience >= sexperience_min + 10:
                    return "anal_outside"
        elif fuck_location == "vaginal":
            menu:
                "Let him cum inside" if CONDOM:
                    return "vaginal_condom"
                "Pull him out" if hero.sexperience >= sexperience_min + 5:
                    return "vaginal_outside"

                "Let him cum inside" if not CONDOM and hero.is_visibly_pregnant:
                    return "vaginal_inside_pregnant"

                "Let him cum inside" if not CONDOM and not hero.is_visibly_pregnant and hero.flags.pill:
                    return "vaginal_inside_pill"

                "Let him cum inside" if not CONDOM and not hero.is_visibly_pregnant and not hero.flags.pill and fuck_npc.love < love_min and check_sub and fuck_npc.sub >= sub_min and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_sub"

                "Let him cum inside" if not CONDOM and not hero.is_visibly_pregnant and not hero.flags.pill and fuck_npc.love < love_min and check_sub and fuck_npc.sub < sub_min and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_mad"

                "Let him cum inside" if not CONDOM and not hero.is_visibly_pregnant and not hero.flags.pill and fuck_npc.love < love_min and not check_sub and not fuck_npc.flags.pregrequest and not fuck_npc.is_sex_slave and not fuck_npc.flags.drugs:
                    return "vaginal_inside_mad"

                "Let him cum inside" if not CONDOM and not hero.is_visibly_pregnant and not hero.flags.pill and (fuck_npc.love >= love_min or fuck_npc.flags.pregrequest or fuck_npc.is_sex_slave or fuck_npc.flags.drugs):
                    return "vaginal_inside_happy"

label handle_npc_leaving(npc, return_status=None, from_foreplay=False):

    if from_foreplay and return_status not in ["leave_without_gain", "leave_with_gain"]:
        return False

    if return_status == "leave_without_gain":
        return True


    if npc.id == "harmony":
        $ harmony.purity -= 5

    $ npc.sexperience += 1
    if npc.lesbian > MIN_LES_GIRL_SEX:
        $ npc.lesbian -= 1
    if return_status == "leave_with_gain":
        return True
    return False
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
