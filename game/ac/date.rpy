init python:
    InteractActivity(**{
    "name": "ask_date",
    "display_name": "Ask on a date",
    "label": "date_her",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("breakup", False),
            IsFlag("noproposedate", False),
            MinStat("love", 20),
            ),
        Or(
            And(
                HeroTarget(
                    IsGender("male")
                    ),
                ActiveTarget(
                    IsGender("female")
                    )
                ),
            HeroTarget(
                IsGender("female")
                )
        )
        ],
    "icon": "askdate",
    "once_day": "ACTIVE",
    "duration": 0,
    })

    InteractActivity(**{
    "name": "cancel_date",
    "display_name": "Cancel date",
    "label": "cancel_date",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            ),
        ActiveTarget(
            IsDatePlanned(),
            IsFlag("breakup", False),
            ),
        ],
    "duration": 0,
    "icon": "abortdate",
    })

    Activity(**{
    "name": "end_date",
    "label": "end_date",
    "display_name": "Date next step",
    "duration": 0,
    "icon": "date_next_step",
    "order": 1,
    "conditions": [
        HeroTarget(
            OnDate(),
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    })


label end_date:
    $ game.room = "map"
    return

label cancel_date:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_87
    $ renpy.show(active_girl.id)
    call cancel_date_internal from _cancel_date
    $ renpy.hide(active_girl.id)
    return

label cancel_date_internal:
    $ renpy.dynamic("found_dates", "appointment", "day")
    $ found_dates = hero.calendar.find(girl=active_girl.id)
    if len(found_dates) > 1:
        python:
            choices = []
            for (day, appointment) in found_dates:
                choices.append((appointment.name, (day, appointment)))
        $ narrator("Which date should I cancel ?", interact=False)
        $ day, appointment = renpy.display_menu(choices)
        $ hero.calendar.remove(day, appointment, cancelled=True)
    else:
        $ hero.calendar.find_and_remove(girl=active_girl.id, cancelled=True)
    call expression f"cancel_date_internal_dialogues_1_{hero.gender}" from _call_expression_62
    active_girl.say "Okay, don't worry."
    $ active_girl.love -= 5
    return

label date_her:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_29
    $ renpy.show(active_girl.id)
    call date_her_internal (False) from _date_her

    if active_girl:
        $ renpy.hide(active_girl.id)
    return

label date_her_internal(smartphone):
    if renpy.has_label(f"{active_girl.id}_ask_date_{hero.gender}"):
        call expression f"{active_girl.id}_ask_date_{hero.gender}" from _call_expression_50
        if _return is None or _return == False:
            return
        $ date_choice = _return
    else:
        call expression f"date_her_internal_dialogues_1_{hero.gender}" from _call_expression_63
        if active_girl.flags.nodate or (active_girl.love < 50 and active_girl.id != "reona"):
            active_girl.say "I'm sorry [hero.name], I don't see you that way."
            return
        else:
            active_girl.say "Sure, it might be fun, when do you want us to go?"
            $ date_choice = True
    python:
        choices = []
        smartphone = False if smartphone is None else smartphone
        if not smartphone and game.hour in [14, 20] and not active_girl.on_date:
            if date_choice or (isinstance(date_choice, Appointment) and (not date_choice.fixed_hour or (date_choice.fixed_hour and date_choice.hour == game.hour))):
                choices.append(("Now", ("now", 0)))
        if game.hour < 20:
            if not hero.calendar.has_appointment(game.days_played, 14, active_girl.id) and not hero.calendar.has_appointment(game.days_played, 20, active_girl.id):
                choices.append(("Today", (game.days_played, game.week_day)))
        for i in range(1, 7):
            day = game.week_day + i
            if day > 7:
                day -= 7
            if not hero.calendar.has_appointment(game.days_played + i, 14, active_girl.id) and not hero.calendar.has_appointment(game.days_played + i, 20, active_girl.id):
                if i == 1:
                    choices.append(("Tomorrow", (game.days_played + i, day)))
                else:
                    choices.append(("Next " + game.get_day_str(day).capitalize(), (game.days_played + i, day)))
        choices.append(("Cancel", ("cancel", None)))
        day, week_day = renpy.display_menu(choices)
    if day == "cancel":
        $ hero.cancel_activity()
    elif day == "now":

        if date_choice:
            $ hero.calendar.add(game.days_played, DateAppointment(game.hour, active_girl.id))
        elif isinstance(date_choice, Appointment):
            $ date_choice.hour = game.hour
            $ hero.calendar.add(game.days_played, Appointment)
        call go_on_date from _date_her_internal
    else:

        if date_choice and ((isinstance(date_choice, Appointment) and date_choice.fixed_hour and date_choice.hour > 14) or (day == game.days_played and game.hour > 14)):
            $ choices = [("Evening", 20), ("Cancel", "cancel")]
        else:
            $ choices = [("Afternoon", 14), ("Evening", 20), ("Cancel", "cancel")]
        $ hour = renpy.display_menu(choices)

        if hour == "cancel":
            $ hero.cancel_activity()
        else:
            if day == game.days_played and hour == 20:
                $ s = "Let's meet up tonight."
            elif day == game.days_played and hour == 14:
                $ s = "Let's meet up this afternoon."
            elif day == game.days_played + 1 and hour == 20:
                $ s = "Let's meet up tomorrow night."
            elif day == game.days_played + 1 and hour == 14:
                $ s = "Let's meet up tomorrow afternoon."
            elif hour == 20:
                $ s = f"Let's meet up {game.get_day_str(week_day).capitalize()} evening."
            elif hour == 14:
                $ s = f"Let's meet up {game.get_day_str(week_day).capitalize()} afternoon."
            call expression f"say_sentence_{hero.gender}" pass (sentence=s) from _call_expression_66
            python:
                from operator import attrgetter
                if isinstance(date_choice, Appointment):
                    
                    date_choice.hour = hour
                    hero.calendar.add(day, date_choice)
                elif date_choice:
                    did_harem = False 
                    
                    harems = Harem.find(active_girl)
                    if harems:
                        
                        time_of_day = "afternoon" if hour == 14 else "evening"
                        season = game.calendar.get_future_season(day)
                        
                        
                        
                        appts = sorted(
            [
                appt for appt in hero.calendar.get_appointments(day, hour)
                if isinstance(appt, DateAppointment) or
                (isinstance(appt, HaremAppointment) and HAREMS[appt.harem].is_active(active_girl))
            ], key=attrgetter('name'), reverse=True)
                        appts = [("harem" if isinstance(appt, HaremAppointment) else "date", appt) for appt in appts]
                        
                        for (appt_type, appt) in appts:
                            if appt_type == "harem":
                                
                                people = appt.participants + [get_person_id(active_girl)]
                                
                                lbl = get_harem_date_label(season=season, time_of_day=time_of_day, people=people)
                                if lbl:
                                    
                                    hero.calendar.add(day, HaremAppointment(hour, harem, people, lbl))
                                    hero.calendar.remove(day, appt)
                                    did_harem=True
                                    break
                            else:
                                
                                
                                for harem in harems:
                                    if all([harem.is_active(person) for person in appt.participants]):
                                        
                                        people = appt.participants + [get_person_id(active_girl)]
                                        
                                        lbl = get_harem_date_label(season=season, time_of_day=time_of_day, people=people)
                                        if lbl:
                                            
                                            hero.calendar.add(day, HaremAppointment(hour, harem, people, lbl))
                                            hero.calendar.remove(day, appt)
                                            did_harem=True
                                            break
                            
                            if did_harem:
                                break
                    
                    if not did_harem:
                        hero.calendar.add(day, DateAppointment(hour, active_girl.id))
    return

init 10 python:
    def get_harem_date_label(season, time_of_day, people):
        import itertools
        
        
        if not season or not time_of_day or not people:
            raise Exception("Invalid values for Harem date label search")
        
        time_list = [tuple([season, time_of_day]), tuple([time_of_day])]
        
        girl_list = [x for x in itertools.permutations([x for x in people])]
        
        lbl_list = itertools.product(girl_list, time_list)
        
        
        lbls = sorted(
        [(len(x + y), "harem_date_" + ("_".join(x + y))) for (x, y) in lbl_list],
        reverse=True,
    )
        
        for _, lbl in lbls:
            if renpy.has_label(lbl):
                return lbl
        return None
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
