init python:
    Activity(**{
    "name": "sleep",
    "duration": 0,
    "label": "sleep",
    "rooms": ("bedroom1", "bedroom4"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 1),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("energy")),
            ),
        ],
    "icon": "sleep",
    "display_name": "Sleep",
    "force_new_context": True,
    })

    Activity(**{
    "name": "set_alarm",
    "duration": 0,
    "rooms": ("bedroom1", "bedroom4"),
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    "icon": "alarm",
    "label": "set_alarm",
    "display_name": "Set Alarm",
    })

    Event(**{
    "name": "sleep_nightmare",
    "label": "sleep_nightmare",
    "conditions": [
        HeroTarget(
            IsActivity("sleep"),
            MaxStat("fun", 2),
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sleep_dream",
    "label": "sleep_dream",
    "conditions": [
        HeroTarget(
            IsActivity("sleep"),
            MinStat("fun", 8),
            ),
        ],
    "chances": 20,
    "do_once": False,
    "once_day": True,
    })

label sleep_dream:
    scene expression f"bg {game.room}" at blur(16), dark with dissolve
    "I had a nice dream."
    $ hero.fun += 1
    return

label sleep_nightmare:
    scene expression f"bg {game.room}" at blur(16), dark with dissolve
    $ game.pass_time(randint(1, 3), True)
    $ hero.cancel_activity()
    call expression f"sleep_nightmare_dialogues_1_{hero.gender}" from _call_expression_137
    "What a horrible nightmare..."
    return

label set_alarm:
    python:
        result = renpy.display_menu([("Early Morning / Night", 1), ("Morning", 2), ("Afternoon", 3), ("Evening", 4), ("No alarm", 5)])
        if result in range(1, 5):
            if result == 1:
                result = renpy.display_menu([("00:00", 0), ("01:00", 1), ("02:00", 2), ("03:00", 3), ("04:00", 4), ("05:00", 5), ("06:00", 6), ("Cancel", "cancel")])
            elif result == 2:
                result = renpy.display_menu([("07:00", 7), ("08:00", 8), ("09:00", 9), ("10:00", 10), ("11:00", 11), ("Cancel", "cancel")])
            elif result == 3:
                result = renpy.display_menu([("12:00", 12), ("13:00", 13), ("14:00", 14), ("15:00", 15), ("16:00", 16), ("17:00", 17), ("Cancel", "cancel")])
            elif result == 4:
                result = renpy.display_menu([("18:00", 18), ("19:00", 19), ("20:00", 20), ("21:00", 21), ("22:00", 22), ("23:00", 23), ("Cancel", "cancel")])
            
            if result != "cancel":
                game.flags.alarm_time = result
                game.flags.alarm_clock = True
        else:
            game.flags.alarm_clock = False
    return

label sleep(sleep_girl=None, sleep_room=hero.bedroom):
    $ game.room = sleep_room
    python:

        duration = 8
        energy_recovery = 1.0
        if hero.has_skill("no_sleep"):
            duration -= 2
            energy_recovery += 0.25
        if "luxury_bed" in hero.inventory:
            energy_recovery += 0.25


        wake_up_event = None
        alarm_triggered = False
        is_hungry = False
        fully_rested = False

        energy_gained = 0.0
        hunger_decay = 0.0
        grooming_decay = 0.0

        for slept_hours in range(1, duration + 1):
            
            game.pass_time()
            energy_gained += energy_recovery
            hunger_decay += 0.4 if hero.has_skill("iron_stomach") else 0.5
            grooming_decay += 0.3
            
            if sleep_room == hero.bedroom:
                
                for event in WakeUpEvent.valid_events():
                    wake_up_event = event
                    break 
                if wake_up_event is not None:
                    break 
                
                if game.flags.alarm_clock and game.flags.alarm_time == game.hour:
                    alarm_triggered = True
                    break
            
            if hero.hunger <= hunger_decay:
                is_hungry = True
                break


        if slept_hours == duration or fully_rested:
            energy_gained += 1.0
            hero.fun += 1
        hero.energy += energy_gained
        hero.hunger -= hunger_decay
        hero.grooming -= grooming_decay


        if slept_hours >= 4 and sleep_room == hero.bedroom:
            if "fitness_machine" in hero.inventory:
                if randint(1, 3) == 3:
                    hero.fitness += 1
            if "knowledge_machine" in hero.inventory:
                if randint(1, 3) == 3:
                    hero.knowledge += 1
            if "charm_machine" in hero.inventory:
                if randint(1, 3) == 3:
                    hero.charm += 1

    scene expression f"bg {game.room}" at blur(16), dark with dissolve
    if not sleep_girl:
        show chibi sleep with dissolve
    else:
        if isinstance(sleep_girl, list):
            $ hero.flags.slept_with = TemporaryFlag(sleep_girl, "day")
            show expression "multisleep homeharem {}".format(" ".join(sleep_girl))
        else:
            $ hero.flags.slept_with = TemporaryFlag([sleep_girl], "day")
            show expression "cuddle {}".format(sleep_girl)

    "Zzz...{w=1}{nw}"

    if wake_up_event is not None:
        call event_do (wake_up_event) from _call_wake_up_event
    else:
        scene expression "bg {}".format(game.room)
        with dissolve
        if alarm_triggered:
            if not persistent.mute_alarm_clock:
                play sound alarm_clock
            "The alarm clock rings"
        elif fully_rested:
            "I'm feeling fully rested."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
