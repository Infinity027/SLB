init python:
    InteractActivity(**{
    "name": "talk",
    "display_name": "Talk",
    "icon": "talk",
    "conditions": [
        ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "label": "talk",
    "duration": 0,
    "once_hour": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "politics_talk",
    "display_name": "Talk about politics",
    "label": "_talk_politics_",
    "duration": 0,
    "icon": "politics_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "food_talk",
    "display_name": "Talk about food",
    "label": "_talk_food_",
    "duration": 0,
    "icon": "food_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "travels_talk",
    "display_name": "Talk about travels",
    "label": "_talk_travels_",
    "duration": 0,
    "icon": "travels_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "tv_talk",
    "display_name": "Talk about tv",
    "label": "_talk_tv_",
    "duration": 0,
    "icon": "tv_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "sports_talk",
    "display_name": "Talk about sports",
    "label": "_talk_sports_",
    "duration": 0,
    "icon": "sports_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "fashion_talk",
    "display_name": "Talk about fashion",
    "label": "_talk_fashion_",
    "duration": 0,
    "icon": "fashion_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "books_talk",
    "display_name": "Talk about books",
    "label": "_talk_books_",
    "duration": 0,
    "icon": "books_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "people_talk",
    "display_name": "Talk about people",
    "label": "_talk_people_",
    "duration": 0,
    "icon": "people_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "computers_talk",
    "display_name": "Talk about computers",
    "label": "_talk_computers_",
    "duration": 0,
    "icon": "computers_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "music_talk",
    "display_name": "Talk about music",
    "label": "_talk_music_",
    "duration": 0,
    "icon": "music_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "love_talk",
    "display_name": "Talk about love",
    "label": "_talk_love_",
    "duration": 0,
    "icon": "love_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    GenericTalkSubject(**{
    "name": "sex_talk",
    "display_name": "Talk about sex",
    "label": "_talk_sex_",
    "duration": 0,
    "icon": "sex_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep"))
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    })

    SpecificTalkSubject(**{
    "name": "birthday_talk",
    "display_name": "Talk about birthday",
    "label": "_talk_birthday_",
    "duration": 0,
    "icon": "birthday_talk",
    "conditions": [
       ActiveTarget(
            Not(IsActivity("sleep")),
            IsBirthday()
            ),
        ],
    "known": True,
    "do_once": False,
    "once_day": "ACTIVE",
    })

label talk:
    call expression f"{active_girl.id}_greet" from _call_expression_25
    $ daily = active_girl.flags.daily_interact
    if (hero.charm + (active_girl.love // 2)) // 2 >= daily * 10 or date_girl == active_girl:
        $ subjects = active_girl.get_talk_subjects()
        if subjects:
            $ renpy.show(active_girl.id)
            $ chosen_subject = renpy.call_screen("choose_talk", subjects)
            $ renpy.hide(active_girl.id)
            if chosen_subject.id != "cancel":
                $ active_girl.set_flag("daily_interact", 1, 1, "+")
                $ renpy.show(active_girl.id)
                if renpy.has_label(chosen_subject.label):
                    call expression chosen_subject.label from _call_expression_185
                    $ chosen_subject.apply_changes()
                elif renpy.has_label(f"{active_girl.id}{chosen_subject.label}{hero.gender}"):
                    call expression f"{active_girl.id}{chosen_subject.label}{hero.gender}" from _call_expression_186
                    $ chosen_subject.apply_changes()
                else:
                    $ renpy.log(f"Unable to find label: {active_girl.id}{chosen_subject.label}{hero.gender}")
                $ renpy.hide(active_girl.id)
            else:
                $ hero.cancel_activity()
        else:
            "We have nothing to talk about."
            $ hero.cancel_activity()
    else:
        $ renpy.show(active_girl.id)
        $ active_girl.say("Sorry, I don't have time right now.")
        $ hero.cancel_activity()
        $ renpy.hide(active_girl.id)
    $ active_girl.set_flag("interact", 1, 1, "+")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
