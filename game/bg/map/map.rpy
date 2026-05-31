init 1:
    layeredimage bg map:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "map",
    "exits": [
        "alley",
        "amusement",
        "audreylivingroom",
        "amyhome",
        "aquarium",
        "beach",
        "cemetery",
        "church",
        "cinema",
        "forest",
        "garage",
        "golf",
        "gymreception",
        "hospital",
        "kart",
        "kathome",
        "housemap",
        "maidcafe",
        "mallmap",
        "mansion",
        "nightclub",
        "office",
        "park",
        "pallalivingroom",
        "photostudio",
        "policestation",
        "pub",
        "restaurant",
        "rooftop",
        "sexshop",
        "shootingrange",
        "street",
        "stripclub",
        "studio",
        "trailer",
        "university",
        "waterpark",
        "zoo",
        "victorsafehouse",
        ],
    "display_name": "City",
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    })

    Event(**{
    "name": "meet",
    "conditions": [
        HeroTarget(IsRoom("map")),
        ],
    "chances": 5,
    "label": "meet",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "assault",
    "conditions": [
        IsHour(0, 4),
        HeroTarget(
            IsGender("male"),
            IsRoom("map"),
            IsFlag("dannydead", False),
            ),
        ],
    "chances": 5,
    "label": "assault",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "found_money",
    "conditions": [
        HeroTarget(IsRoom("map")),
        ],
    "chances": 1,
    "label": "found_money",
    "do_once": False,
    "once_week": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "dog_shit",
    "conditions": [
        HeroTarget(
            IsRoom("map"),
            MinStat("luck"),
            ),
        ],
    "chances": 5,
    "label": "dog_shit",
    "do_once": False,
    "once_week": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "wish_had_sport_clothes",
    "conditions": [
        HeroTarget(IsRoom("map")),
        Not(InInventory("sport_clothes")),
        ],
    "chances": 20,
    "label": "wish_had_sport_clothes",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "wish_had_fancy_clothes",
    "label": "wish_had_fancy_clothes",
    "conditions": [
        HeroTarget(IsRoom("map")),
        Not(InInventory("fancy_clothes")),
        ],
    "chances": 20,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "dog_attack_male",
    "label": "dog_attack_male",
    "conditions": [
        IsHour(6, 20),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("map"),
                HasRoomTag("street"),
            ),
            Or(
                HasSkill("animalhated"),
                MaxStat("energy", 3),
                ),
            ),
        ],
    "chances": 10,
    "once_week": True,
    })

label dog_attack_male:
    if game.room == "map":
        show bg street
    else:
        show expression f"bg {game.room}"
    "I'm just walking down the street, minding my own business when it happens."
    $ renpy.sound.set_pan(-0.75, 0, channel='sound')
    play sound dog_small
    "I hear a sudden barking and the sound of claws skittering behind me."
    "Turning around, I'm just in time to see a burr of scruffy fur heading my way."
    mike.say "Aw...hey there, boy!"
    "I hold out my hand to the fast-approaching dog, but it doesn't seem interested."
    $ renpy.sound.set_pan(-0.5, 0, channel='sound')
    play sound dog_small
    "Instead it bares it's teeth and makes a lunge for my ankle."
    play sound "<from 0 to 0.6>sd/SFX/animals/dog_small.ogg"
    show dog attack with hpunch
    $ persistent.dog_attack = True
    call injured from _call_injured_1
    "Before I know it, the damn mutt is chewing on my leg!"
    mike.say "Aaargh!"
    mike.say "Get off me, you flea-bitten little shit!"
    play sound "<from 0 to 0.6>sd/SFX/animals/dog_small.ogg"
    "Luckily the dog seems to have gotten more of my pants than my actual leg."
    "But it holds on stubbornly as I swing my leg back and forth, trying to dislodge it."
    play sound "<from 0 to 1.0>sd/SFX/objects/cloth_tearing.ogg"
    "After perhaps half-a-dozen good shakes, I hear the sound of my pants tearing."
    $ renpy.sound.set_pan(-0.75, 0, channel='sound')
    play sound dog_crying
    "And the dog goes flying with one more swing, sailing a good few feet away."
    scene bg street
    "I don't waste the chance and start to run as soon as I'm free."
    "And I don't stop to see where the dog landed either."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    "I just keep on running until I'm sure it's not following me anymore."
    $ hero.fun -= 10
    hide dog
    return

label wish_had_sport_clothes:
    "I've heard of a good gym around here, but I'll need sport clothes to be admitted."
    show screen message(title="Buy sport clothes!",what="You need {b}sport clothes{/b} to be able to go to the gym.")
    pause
    hide screen message
    return

label wish_had_fancy_clothes:
    "I've heard of a nightclub around here, but I'll need nicer clothes to be admitted."
    show screen message(title="Buy fancy clothes!",what="You need {b}fancy clothes{/b} to be able to go to the nightclub.")
    pause
    hide screen message
    return

label dog_shit:
    "I step in dog shit..."
    $ hero.grooming -= 2
    return

label found_money:
    scene bg street
    $ amount = randint(5, 50)
    if hero.is_lucky:
        $ amount *= 2
    "I found [amount]{image=gui/icons/icon_money.png} on the sidewalk!"
    if renpy.has_label(f"found_money_{hero.gender}"):
        call expression f"found_money_{hero.gender}" from _call_expression_198
    return

label found_money_male:
    menu:
        "Take it":
            $ hero.money += amount
        "Leave it":
            pass
    return

label assault:
    python:
        choices = []
        for g in Person.all_people():
            if g.room in Room.find("map").exits and g.id != "lexi":
                choices.append(g)
        if choices:
            active_girl.object = randchoice(choices)
            active_girl.set_room("street")
            renpy.show("bg street")
            renpy.say("","The city at night can be scary...")
            active_girl.say("Heeeeelp!")
            renpy.say("", "I hear [active_girl.name] screaming.")
            ch = renpy.display_menu([("Help her",1), ("Don't help her",2)])
            if ch == 1:
                renpy.say("","I rush toward the dark alley the screams are coming from.")
                renpy.show("bg alley")
                renpy.show("danny fist")
                renpy.say(thug_say, "Show me what you're hiding under those clothes, bitch.")
                renpy.hide("danny")
                renpy.show(active_girl.id)
                active_girl.say("Leave me alone...")
                renpy.hide(active_girl.id)
                renpy.show("danny fist")
                mike.say("You should leave her alone, or else...")
                result = game.flags.thugfight
                if result == 0:
                    renpy.say(thug_say,"Else what, sucker.")
                    renpy.say(thug_say,"Okay, if you give me your money, I'll leave her be.")
                    fight = False
                    choices = [("Give it to him",1), ("Refuse",2)]
                    result = renpy.display_menu([("Give it to him",1), ("Refuse",2)])
                    if result == 1 and hero.money >= 100:
                        renpy.say("","I give the thug my money.")
                        renpy.say(thug_say,"Good boy.")
                        hero.money.val = 0
                    elif result == 1:
                        renpy.say("","I give the thug my money.")
                        renpy.say(thug_say,"That's all you got?!")
                        renpy.say(thug_say,"I'm gonna end you!!")
                        hero.money.val = 0
                        result = 2
                    else:
                        mike.say("No way, go fuck yourself.")
                        renpy.say(thug_say,"You'll regret this, faggot.")
                    if result == 1:
                        renpy.hide("danny")
                        renpy.show(active_girl.id)
                        hero.fun -= 5
                        active_girl.love += 2
                        active_girl.say("Thanks for the help.")
                        mike.say("It was nothing.")
                        renpy.hide(active_girl.id)
                        love_gain = 0
                        if "pacifist" in active_girl.traits:
                            love_gain += 2
                        if "not_pacifist" in active_girl.traits:
                            love_gain -= 2
                        if "princess" in active_girl.traits:
                            love_gain += 2
                        active_girl.love += love_gain
                    elif result == 2:
                        result = renpy.display_menu([("Attack him",1), ("Intimidate him",2)])
                        if result == 1:
                            fight = True
                        else:
                            mike.say("You should leave, I have a black belt in origami.")
                            if hero.charm >= 20:
                                renpy.show("danny scared")
                                renpy.say(thug_say,"Is that an ancient japanese ninja martial art?")
                                renpy.say(thug_say,"I won't fight a fucking ninja...")
                                renpy.say("","He turns and runs as if the devil was on his tail.")
                                renpy.hide("danny")
                                renpy.show(active_girl.id)
                                active_girl.say("Thanks for the help.")
                                mike.say("It was nothing.")
                                love_gain = 2
                                if "pacifist" in active_girl.traits:
                                    love_gain += 2
                                if "not_pacifist" in active_girl.traits:
                                    love_gain -= 2
                                if "playful" in active_girl.traits:
                                    love_gain += 2
                                if "not_playful" in active_girl.traits:
                                    love_gain -= 2
                                active_girl.love += love_gain
                                renpy.hide(active_girl.id)
                            else:
                                renpy.say(thug_say,"We'll see about that.")
                                fight = True
                    if fight:
                        d = 25
                        if not hero.has_skill("martial_arts"):
                            d += 25
                        if hero.fitness >= d:
                            renpy.show("danny fight lose")
                            renpy.say("","I kick his ass, badly.")
                            renpy.say(thug_say,"I'll have my revenge!")
                            renpy.say("","He turns and runs as if the devil was on his tail.")
                            game.flags.thugfight = 1
                            renpy.hide("danny fight lose")
                            renpy.show(active_girl.id)
                            mike.say("Are you okay, [active_girl.name]?")
                            active_girl.say("I'm fine [hero.name], thanks for the help.")
                            love_gain = 2
                            if "submissive" in active_girl.traits:
                                love_gain += 2
                            if "princess" in active_girl.traits:
                                love_gain += 2
                            if "pacifist" in active_girl.traits:
                                love_gain -= 2
                            if "not_pacifist" in active_girl.traits:
                                love_gain += 2
                            active_girl.love += love_gain
                            renpy.hide(active_girl.id)
                        else:
                            renpy.show("danny fight win")
                            renpy.say("","The thug kicks my ass, takes my money and leaves me lying on the ground.")
                            renpy.say(thug_say,"Next time, hand it over nicely.")
                            renpy.hide("danny fight win")
                            renpy.show(active_girl.id)
                            if hero.money > 500:
                                hero.money -= 500
                            else:
                                hero.money.val = 0
                            hero.grooming -= 5
                            hero.energy -= 5
                            hero.fun -= 5
                            renpy.show(active_girl.id)
                            active_girl.say("Are you okay, [hero.name]?!")
                            mike.say("I'm fine, at least he left.")
                            active_girl.say("Thanks for the help.")
                            mike.say("It was nothing.")
                            love_gain = 0
                            if "family" in active_girl.traits:
                                love_gain += 2
                            if "princess" in active_girl.traits:
                                love_gain += 2
                            if "dominant" in active_girl.traits:
                                love_gain += 2
                            if "pacifist" in active_girl.traits:
                                love_gain -= 2
                            if "not_pacifist" in active_girl.traits:
                                love_gain += 2
                            renpy.hide(active_girl.id)
                        renpy.call("injured")
                else:
                    renpy.show("danny scared")
                    renpy.say(thug_say,"Oh, it's you...")
                    renpy.say(thug_say,"Sorry sir, I didn't recognize you.")
                    mike.say("Are you okay, [active_girl.name]?")
                    renpy.hide("danny")
                    renpy.show(active_girl.id)
                    active_girl.say("I'm fine [hero.name], thanks for the help.")
                    active_girl.love += 1
                    love_gain = 2
                    if "submissive" in active_girl.traits:
                        love_gain += 2
                    if "princess" in active_girl.traits:
                        love_gain += 2
                    if "pacifist" in active_girl.traits:
                        love_gain += 2
                    if "not_pacifist" in active_girl.traits:
                        love_gain -= 2
                    if "rebel" in active_girl.traits:
                        love_gain += 2
                    if "not_rebel" in active_girl.traits:
                        love_gain -= 2
                    active_girl.love += love_gain
                    renpy.hide(active_girl.id)
                renpy.hide(active_girl.id)
            else:
                renpy.say("","I leave the area discretely.")
                active_girl.love -= 1
    $ active_girl.object = None
    return

label meet:
    python:
        choices = []
        for g in Person.all_people():
            if g.room in Room.find("map").exits:
                choices.append(g)
    if choices:
        $ interact_girl.object = randchoice(choices)
        $ game.room = "street"
        scene bg street
    else:
        return
    $ meet_change_outfit = False
    if interact_girl.get_clothes() not in ["date", "work", "casual"]:
        $ meet_change_outfit = True
        $ meet_old_girl_clothes = game.girl_clothes
        $ game.girl_clothes = "casual"
    "I meet [interact_girl.name] walking in the street."
    $ renpy.show(interact_girl.id)
    call expression interact_girl.id + "_greet" from _call_expression_27
    $ renpy.show(interact_girl.id)
    call expression interact_girl.get_chat from _call_expression_96
    interact_girl.say "See you later, [hero.name]."
    $ renpy.hide(interact_girl.id)
    if meet_change_outfit:
        $ game.girl_clothes = meet_old_girl_clothes
    $ game.room = "map"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
