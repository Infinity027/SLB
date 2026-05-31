init python:
    class poolPicker(object):
        def __call__(self, attr):
            if game.hour >= 20 or game.hour <= 5:
                attr.add("night")
            else:
                attr.add("day")
            if game.calendar.is_today("fall", 31) and game.hour >= 8:
                attr.add("halloween")
            elif game.calendar.is_today("winter", 1) and game.hour < 6:
                attr.add("halloween")
            else:
                attr.add(game.calendar.season_name)
            return attr

init 1:
    layeredimage bg pool:
        attribute_function poolPicker()
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"

init python:
    Room(**{
    "name": "pool",
    "exits": ["livingroom","housemap"],
    "music": house_music(),
    "outfit": "swimsuit",
    "tags": ["home"],
    })

    Activity(**{
    "name": "swim_pool_home",
    "fun": 1,
    "fitness": 1,
    "rooms": "pool",
    "conditions": [
        IsSeason(0, 1),
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 0),
            MinStat("fun", 3),
            Not(OnDate()),
            ),
        InInventory("swimsuit"),
        ],
    "display_name": "Swim",
    "icon": "swim",
    "label": "swim",
    "once_day": True,
    })

    Activity(**{
    "name": "clean_the_pool",
    "rooms": "pool",
    "conditions": [
        IsSeason(0, 1),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "display_name": "Clean the pool",
    "label": "clean_the_pool",
    "icon": "cleanpool",
    "every_two_days": True,
    })

    Activity(**{
    "name": "pool_tan",
    "label": "pool_tan",
    "charm": 1,
    "fun": 1,
    "energy": 1,
    "rooms": "pool",
    "conditions": [
        IsSeason(0, 1),
        IsHour(9, 19),
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        InInventory("swimsuit"),
        ],
    "icon": "tan",
    "display_name": "Sunbath",
    "once_day": True,
    })

    InteractActivity(**{
    "name": "pool_suntan",
    "energy": 2,
    "icon": "tan",
    "conditions": [
        IsSeason(0, 1),
        IsHour(9, 19),
        HeroTarget(
            IsRoom("pool"),
            Not(OnDate()),
            ),
        InInventory("lotion"),
        ],
    "display_name": "Apply sunscreen",
    "label": "apply_sunscreen",
    "once_day": "ACTIVE",
    })

    Activity(**{
    "name": "hot_tub_alone",
    "charm": 1,
    "fun": 1,
    "energy": 1,
    "grooming": 1,
    "rooms": "pool",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 5),
            MinStat("fun", 0),
            IsFlag("hottubrepaired"),
            Not(OnDate()),
            ),
        InInventory("swimsuit"),
        "not Room.find('pool').get_present_girls()",
        ],
    "icon": "hottub",
    "display_name": "Dip in the hot tub alone",
    "once_day": True,
    "label": "hot_tub_alone",
    })

    Activity(**{
    "name": "hot_tub",
    "charm": 1,
    "fun": 1,
    "energy": 1,
    "grooming": 1,
    "rooms": "pool",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 5),
            MinStat("fun", 0),
            IsFlag("hottubrepaired"),
            Not(OnDate()),
            ),
        InInventory("swimsuit"),
        "any(Room.find('pool').get_present_girls())",
        ],
    "icon": "hottub",
    "display_name": "Dip in the hot tub",
    "once_day": True,
    "label": "hot_tub",
    })

    Activity(**{
    "name": "repair_hot_tub",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsFlag("hottubrepaired", False)),
        ],
    "icon": "hottub",
    "display_name": "Look at the hot tub",
    "duration": 0,
    "label": "repair_hot_tub",
    })

    Activity(**{
    "name": "play_in_the_pool_with_everyone",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with the girls",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("male"),
            Not(OnDate()),
            ),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        ],
    "once_day": True,
    "label": "play_in_the_pool_with_everyone",
    })

    Event(**{
    "name": "wish_had_swimsuit",
    "label": "wish_had_swimsuit",
    "conditions": [
        HeroTarget(IsRoom("pool")),
        Not(InInventory("swimsuit")),
        ],
    "chances": 20,
    "do_once": True,
    "quit": False,
    })

label pool_tan:
    show chibi tan
    "I take a nap in the sun."
    return

label apply_sunscreen:
    show expression f"beach cream {active_girl.id}"
    "I put sunscreen lotion on [active_girl.name]."
    call expression Person.find(active_girl.id).get_chat from _call_expression_52
    hide expression f"beach cream {active_girl.id}"
    $ active_girl.love += 2
    return

label repair_hot_tub:
    "The hottub is broken, I need 5000{image=gui/icons/icon_money.png} to get it fixed it."
    menu:
        "Get it fixed" if hero.money >= 5000:
            $ hero.money -= 5000
            $ game.flags.hottubrepaired = True
        "Leave it":
            pass
    return

label hot_tub_alone:
    show chibi hottub
    "I take a dip in the hot tub."
    hide chibi
    return

label hot_tub:
    $ present_girls = Room.find("pool").get_present_girls()
    if len(present_girls) == 1:
        $ girl_id = present_girls[0].id
    else:
        python:
            choose_girl = [(p_girl.id.capitalize(), p_girl.id) for p_girl in present_girls]
            choose_girl.append(("Cancel", 'pass'))
            girl_id = menu(choose_girl)
        if girl_id == 'pass':
            $ hero.cancel_activity()
            return
    if Person.find(girl_id).sub >= 25 and Person.find(girl_id).sexperience >= 1:
        $ renpy.show("hottub " + girl_id + " naked")
    else:
        $ renpy.show("hottub " + girl_id)
    if renpy.has_label(girl_id + "_hottub"):
        call expression girl_id + "_hottub" from _call_expression_116
    else:
        "We spend a relaxing time in the hot tub."
    hide hottub
    return

label play_in_the_pool_with_everyone:
    show sasha at left
    show bree at right
    "I play in the pool with the girls."
    $ bree.love += 1
    $ bree.flags.greeted = TemporaryFlag(True, 1)
    $ sasha.love += 1
    $ sasha.flags.greeted = TemporaryFlag(True, 1)
    return

label wish_had_swimsuit:
    "If only I had a swimsuit, I could take a dive..."
    if game.flags.hottubrepaired:
        show screen message(title="Buy a swimsuit!",what="You need a {b}swimsuit{/b} to be able to swim in the pool and the sea, use the hottub and go to the water-park.")
    else:
        show screen message(title="Buy a swimsuit!",what="You need a {b}swimsuit{/b} to be able to swim in the pool and the sea, use the hottub once repaired and go to the water-park.")
    pause
    hide screen message
    return

label clean_the_pool:
    show chibi cleanpool
    $ game.set_flag("chores", 25, "week", "+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I clean the pool."
    return

label swim:
    show chibi swim
    python:
        swim_say = [
    "I go for a swim."
    ]
        successes = []
        for girl in Room.find(game.room).get_present_girls():
            if hero.fitness * 2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes:
        if len(successes) == 1:
            hide chibi swim
            $ renpy.show(f"{successes[0].id}")
            if isinstance(successes[0], Guy):
                "[successes[0].name] can't take his eyes off me while I swim."
            else:
                "[successes[0].name] can't take her eyes off me while I swim."
            $ renpy.hide(f"{successes[0].id}")
        else:
            if all([isinstance(i, Girl) for i in successes]):
                "The girls can't take their eyes off me while I swim."
            else:
                "They can't take their eyes off me while I swim."
    else:
        $ renpy.say("", randchoice(swim_say))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
