init python:
    Activity(**{
    "name": "go_on_date",
    "label": "go_on_date",
    "display_name": "Go on a date",
    "notification": "You have a date!",
    "icon": "date",
    "duration": 0,
    "conditions": [
        HeroTarget(Not(OnDate())),
        "hero.calendar.has_date()",
        ],
    })

    Activity(**{
    "name": "go_on_appointment",
    "label": "go_on_date",
    "display_name": "Go to the appointment",
    "notification": "You have an appointment.",
    "icon": "appointment",
    "duration": 0,
    "conditions": [
        HeroTarget(Not(OnDate())),
        "hero.calendar.has_appointment()",
        ],
    })

label go_on_date:

    python:
        if globals().get("appointment"):
            del appointment

    $ renpy.dynamic("appointment")
    if game.room == "map":
        $ game.room = "street"
    python:
        appointments = hero.calendar.get_appointments()
        if len(appointments) == 1:
            result = 0
        else:
            i = 0
            choices = []
            for appt in appointments:
                choices.append((appt.name, i))
                i += 1
            result = renpy.call_screen("select", choices, "Choose", cap = False)

    if result != "None":
        $ hero.activity = None
        $ appointment = appointments[result]
        $ hero.calendar.remove(game.days_played, appointment)
        if isinstance(appointment, Appointment) and appointment.do() != None:
            call expression appointment.do() pass (appointment) from _call_expression_84
    else:
        $ hero.cancel_activity()
    $ game.pass_time(0)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
