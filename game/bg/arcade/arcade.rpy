init python:

    Gift("cute_plushie", price=100, tags=["plushie"], love_bonus=1, bonus_traits=["artsy", "innocent", "playful"])

    Room(**{
    "name": "arcade",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "display_name": "Arcade",
    "exits": ["mall1", "bakery", "bookstore", "clothesshop", "tattooshop", "mallmap"],
    "music": "music/roa_music/pixel_story.ogg",
    "outfit": "casual",
    "tags": ["mall_southside"],
    })

    Activity(**{
    "name": "play_a_videogame",
    "label": "play_a_videogame",
    "rooms": "arcade",
    "conditions": [
        HeroTarget(
            MinStat("energy", 1),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 0),
            ),
        ],
    "icon": "playarcade",
    "fun": 3,
    "money_cost": 1,
    "display_name": "Play a game",
    })

    Event(**{
    "name": "arcade_competition",
    "label": "arcade_competition",
    "conditions": [
        IsDayOfWeek(1, 3, 5),
        HeroTarget(IsRoom("arcade")),
        ],
    "chances": 50,
    "do_once": False,
    "once_week": True,
    })

    Event(**{
    "name": "play_with_bree",
    "label": "play_with_bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("arcade")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("playarcade"),
            MinStat("love", 10),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label play_a_videogame:
    if randint(1, 2) == 1:
        show chibi arcade
        $ renpy.say("", randchoice([
                "I play a few games of Street Racer.",
                "I play Fatal Kombat for a while.",
                "Meat Fighter 2 is such a great game, the boob physics are awesome...",
                ]))
    else:
        show chibi clawmachine
        "I decide to play the claw machine."
        if randint(1, 2) == 1 or hero.is_lucky:
            "I won a cute plushie!"
            $ hero.gain_item("cute_plushie")
        else:
            "I lost..."
    $ hero.flags.video_games_played += 1
    return

label play_with_bree:
    call expression "bree_greet" from _call_expression_16
    show bree
    "[bree.name] looks at me with a defiant look."
    bree.say "Wanna play me?"
    menu:
        "Accept":
            $ bree.love += 1
            mike.say "Sure."
            if hero.has_skill("video_games"):
                $ bonus = 10
            else:
                $ bonus = 0
            if hero.knowledge + bonus >= 25:
                if hero.knowledge + bonus >= bree.love:
                    $ bree.love += 1
                "I beat her quite easily."
                mike.say "That was fun."
                bree.say "Yeah, we definitely gotta come again some time!"
            else:
                mike.say "I was defeated."
                bree.say "Don't worry, you'll get me next time!"
        "Refuse":
            show bree cry
            mike.say "No, sorry."
            bree.say "Another time then."
    hide bree
    return

label arcade_competition:
    "There is a video game competition going on."
    "The participation fee is 25{image=gui/icons/icon_money.png}."
    if hero.money >= 25:
        $ result = renpy.display_menu([("Participate",1), ("Don't participate",2)])
        if result == 1:
            show chibi arcade
            $ hero.money -= 25
            if hero.has_skill("video_games"):
                $ bonus = 3
            else:
                $ bonus = 0
            $ bonus += hero.knowledge // 20 + randint(-5, 5)
            if bonus > 0:
                $ money = bonus*15
                "I won! The prize was [money]{image=gui/icons/icon_money.png}."
                $ hero.money += money
            else:
                "I lost."
            $ game.pass_time(1, needs=True)
        else:
            "I don't feel like participating."
    else:
        "I don't have money to participate."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
