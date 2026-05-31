init python:
    Room(**{
    "name": "bathroom",
    "exits": ["secondfloor", "housemap"],
    "music": house_music(),
    "outfit": "underwear",
    "tags": ["home"],
    })

    Activity(**{
    "name": "take_a_shower",
    "grooming": 8,
    "rooms": ["firstfloorbathroom","bathroom"],
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("grooming")),
            Not(OnDate()),
            Or(
                IsFlag("bathroomrepaired"),
                IsRoom("bathroom")
                ),
            ),
        ],
    "display_name": "Take a shower",
    "label": "take_a_shower",
    "icon": "shower",
    })

    Activity(**{
    "name": "take_a_bath",
    "grooming": 8,
    "fun": 4,
    "duration": 2,
    "rooms": ["firstfloorbathroom", "bathroom"],
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("grooming")),
            Or(
                IsFlag("bathroomrepaired"),
                IsRoom("bathroom")
                ),
            Not(OnDate()),
            ),
        ],
    "display_name": "Take a bath",
    "label": "take_a_bath",
    "icon": "bath",
    })

    Activity(**{
    "name": "practicespeech",
    "label": "practicespeech",
    "charm": 0.5,
    "icon": "mirror",
    "rooms": ["firstfloorbathroom","bathroom"],
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            MaxStat("charm", 25),
            Or(
                IsFlag("bathroomrepaired"),
                IsRoom("bathroom")
                ),
            Not(OnDate()),
            ),
        ],
    "display_name": "Practice speech",
    "once_day": True,
    })

    Activity(**{
    "name": "clean_the_bathroom",
    "rooms": ["firstfloorbathroom","bathroom"],
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Or(
                IsFlag("bathroomrepaired"),
                IsRoom("bathroom")
                ),
            Not(OnDate()),
            ),
        ],
    "icon": "vacuum",
    "display_name": "Clean",
    "label": "clean_the_bathroom",
    "every_two_days": True,
    })

    Event(**{
    "name": "generic_get_out",
    "label": "generic_get_out",
    "priority": 1000,
    "conditions": [
        HeroTarget(IsRoom("bathroom", "bedroom1", "bedroom2", "bedroom3", "bedroom4", "bedroom5", "bedroom6")),
        ],
    "do_once": False,
    "once_hour": False,
    "quit": False,
    })


label generic_get_out:
    $ upset_npcs = Room.find(game.room).get_upset_npcs()
    $ present_npcs = Room.find(game.room).get_present_npcs()

    if upset_npcs:
        $ game.flags.EventQuit = True
        if game.from_room != "bathroom":

            $ upset_naked_npc = [p for p in upset_npcs if p.activity['clothes'] == 'naked']
            $ upset_clothed_npc = [p for p in upset_npcs if p.activity['clothes'] != 'naked']
            $ naked_npc = [p for p in present_npcs if p.activity['clothes'] == 'naked' and p not in upset_naked_npc]
            $ clothed_npc = [p for p in present_npcs if p.activity['clothes'] != 'naked' and p not in upset_clothed_npc]
            $ npc_to_show = min(len(present_npcs), 3)

            if len(upset_naked_npc + upset_clothed_npc) == npc_to_show:
                $ shown_people = show123people(upset_naked_npc, extra=upset_clothed_npc, expression="angry")
            else:
                if upset_naked_npc:
                    $ shown_people = show123people(upset_naked_npc + upset_clothed_npc, extra=naked_npc + clothed_npc, expression="angry", extra_expression="")
                else:
                    $ shown_people = show123people(upset_clothed_npc, extra=naked_npc + clothed_npc, expression="angry", extra_expression="")

            $ get_out_say = ""
            if any(upset_naked_npc):

                if len(shown_people) > 1 and all([i for i in shown_people if i in upset_naked_npc or i in naked_npc]):
                    $ get_out_say = "We are naked."
                else:
                    $ get_out_say = "I am naked."
                $ npc = randchoice([p for p in shown_people if p in upset_naked_npc])
            elif any(upset_clothed_npc):
                $ npc = randchoice([p for p in shown_people if p in upset_clothed_npc])
            else:
                $ npc = randchoice(shown_people)

            if len(shown_people) == 1 and renpy.has_label(f"{npc.id}_get_out_{hero.gender}"):

                python:
                    for p in shown_people:
                        renpy.hide(p.id)
                call expression f"{npc.id}_get_out_{hero.gender}" from _call_expression_33
            else:
                $ renpy.say(npc.id, "[get_out_say] Please can you step out?")

            python:
                for p in shown_people:
                    renpy.hide(p.id)
                for p in present_npcs:
                    p.flags.greeted = TemporaryFlag(True, 'day')
                    p.set_flag("peeping_tom", 1, "day", mod ="+")
                    if p in upset_npcs:
                        p.love -= p.flags.peeping_tom
        else:
            "I hear a voice through the door."
            if hero.has_skill("hung"):
                python:
                    for p in present_npcs:
                        p.love += 1

            $ npc = randchoice(upset_npcs)
            if renpy.has_label(f"{npc.id}_get_out_{hero.gender}"):
                call expression f"{npc.id}_get_out_{hero.gender}" from _call_expression_449
            else:
                $ renpy.say(npc.id, "[hero.name] I need the bathroom, can you step out?")
                call expression f"generic_get_out_dialogues_1_{hero.gender}" from _call_expression_195

        $ game.room = "secondfloor"
    else:
        if not all(((p.flags.not_get_out and p.activity['clothes'] != 'naked') or (p.flags.not_get_out_naked and p.activity['clothes'] == 'naked')) for p in present_npcs):
            $ naked_npc = [p for p in present_npcs if p.activity['clothes'] == 'naked']
            $ clothed_npc = [p for p in present_npcs if p.activity['clothes'] != 'naked']
            $ shown_people = show123people(naked_npc, extra=clothed_npc)

            if len(shown_people) == 1:
                $ npc = shown_people[0]
                $ name = npc.name
                $ verb = f"{name} is"
                $ first_person = "I"
                $ towel = "a towel"
                if npc.is_male:
                    $ third_person = "his"
                else:
                    $ third_person = "her"
            else:
                $ npc = None
                $ name = "everyone"
                $ verb = "My roommates are"
                $ first_person = "we"
                $ towel = "towels"
                $ third_person = "their"
            if npc and renpy.has_label(f"{npc.id}_not_get_out_{hero.gender}"):

                python:
                    for p in shown_people:
                        renpy.hide(p.id)
                call expression f"{npc.id}_not_get_out_{hero.gender}" from _call_expression_450
            else:

                if all(p.activity['clothes'] == 'naked' for p in shown_people):
                    "[verb] naked..."
                elif all(p.activity['clothes'] == 'underwear' for p in shown_people):
                    "[verb] in [third_person] undies..."
                elif all(p.activity['clothes'] == 'towel' for p in shown_people):
                    "[verb] only wearing [towel]..."
                elif len(shown_people) > 1:
                    "[verb] in various states of undress..."
                else:
                    return

                call expression f"generic_get_out_dialogues_2_{hero.gender}" from _call_expression_196

                $ npc = randchoice(shown_people)
                if all(p.activity['clothes'] == 'naked' for p in shown_people):
                    $ renpy.say(npc.id, "You know... [first_person] don't mind if you come in...")
                else:
                    $ renpy.say(npc.id, "Stop it, we know each other well enough not to be bothered by that...")
            python:
                for p in present_npcs:
                    if p.activity['clothes'] == 'naked':
                        p.flags.not_get_out_naked = True
                    else:
                        p.flags.not_get_out = True
                    p.flags.greeted = TemporaryFlag(True, 'day')
                for p in shown_people:
                    renpy.hide(p.id)
    return

label generic_get_out_dialogues_1_male:
    mike.say "Sure."
    return

label generic_get_out_dialogues_2_male:
    mike.say "Sorry [name], I didn't know you would be in here."
    return

label take_a_shower:
    play sound shower
    show chibi shower
    python:
        for girl in Room.find(game.room).get_present_girls():
            if hero.fitness * 2 > girl.love:
                girl.love += 1
            if hero.has_skill("hung"):
                girl.sub += 1
            elif hero.has_skill("smalldick"):
                girl.sub -= 1
    $ game.flags.showered = True
    $ renpy.say("", randchoice([
        "...",
        "...I'm picky 'cause I'm all alone\nMaybe I'm alone 'cause I'm a picky one\nI got a lotta girls waiting for me not to call...",
        "...Je ne fais pourtant de tort à personne,\nEn n'écoutant pas le clairon qui sonne...",
        "...Till the sandman comes\nSleep with one eye open\nGripping your pillow tight...",
        "...Cause' I'm a picker\nI'm a grinner\nI'm a lover And I'm a sinner..."
        ]))
    stop sound
    return

label take_a_bath:
    $ present_girls = Room.find(game.room).get_present_girls()
    $ present_girls = [girl for girl in present_girls if girl.id in ["bree", "lexi", "minami", "samantha", "sasha", "mike"]]
    play sound bath
    if present_girls:
        $ choose_girl = [(f"Take a bath with {p_girl.name}", p_girl.id) for p_girl in present_girls if p_girl.love >= 140 and not p_girl.flags.cheated and ((p_girl.id == "minami" and p_girl.siscon >= 70) or p_girl.id != "minami")]
        $ choose_girl.append(("Bath alone", 'alone'))
        $ girl_id = menu(choose_girl)
        if girl_id != 'alone':
            show expression f"peeping_bath {hero.gender} {girl_id}"
            $ Person.find(girl_id).love += 4
            "We spend a relaxing time in the bath."
            $ game.flags.showered = True
            return
    show chibi bath
    python:
        for girl in present_girls:
            if hero.fitness * 2 > girl.love:
                girl.love += 1
            if hero.has_skill("hung"):
                girl.sub += 1
            elif hero.has_skill("smalldick"):
                girl.sub -= 1
    $ renpy.say("", randchoice([
        "...",
        "...I'm picky 'cause I'm all alone\nMaybe I'm alone 'cause I'm a picky one\nI got a lotta girls waiting for me not to call...",
        "...Je ne fais pourtant de tort à personne,\nEn n'écoutant pas le clairon qui sonne...",
        "...Till the sandman comes\nSleep with one eye open\nGripping your pillow tight...",
        "...Cause' I'm a picker\nI'm a grinner\nI'm a lover And I'm a sinner..."
        ]))
    hide chibi
    $ game.flags.showered = True
    return

label clean_the_bathroom:
    play sound vacuum
    show chibi vacuum
    $ game.set_flag("chores", 25, "week", "+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    stop sound
    return

label practicespeech:
    show chibi traintalk
    $ renpy.say("", randchoice([
        "Hey babe, how ya doin'?",
        "Looking sexy!",
        "Wow, I am hot indeed...",
        "You know you want me.",
        "Wanna try the backdoor?"
        ]))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
