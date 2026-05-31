init python:
    Room(**{
    "name": "stripclub",
    "hours": (18, 4),
    "conditions": [
        IsHour(18, 4),
        ],
    "display_name": "Strip club",
    "exits": ["map"],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "outfit": "casual",
    "conditioned_bg": {
                        "hero.is_male": "bg stripclub",
                        "hero.is_female": "poledance hanna harmony shiori"
                        }
    })

    Activity(**{
    "name": "get_a_lapdance",
    "fun": 5,
    "rooms": ["stripclub"],
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 0),
            ),
        ],
    "display_name": "Get a lap dance",
    "once_day": True,
    "icon": "lapdance",
    "money_cost": 50,
    "label": "lapdance",
    })

    Activity(**{
    "name": "harmony_poledance",
    "fun": 3,
    "money_cost": 10,
    "rooms": "stripclub",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        IsDone("harmony_event_04_slutty"),
        PersonTarget("harmony",
            Not(IsHidden()),
            IsRoom("stripclub"),
            ),
        ],
    "display_name": "Wait for Harmony's dance",
    "once_day": True,
    "icon": "dancegirl",
    "money_cost": 50,
    "label": "harmony_poledance",
    })

    Activity(**{
    "name": "drink_poledance",
    "label": "drink_poledance",
    "duration": 0,
    "fun": 1,
    "money_cost": 25,
    "rooms": ["stripclub"],
    "duration": 1,
    "conditions": [
        HeroTarget(MinStat("fun", 0)),
        Or(
            PersonTarget("bree",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            PersonTarget("hanna",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            PersonTarget("harmony",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            PersonTarget("lexi",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            PersonTarget("reona",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            PersonTarget("shiori",
                Not(IsHidden()),
                IsRoom("stripclub"),
                ),
            ),
        ],
    "display_name": "Order a drink and watch the show",
    "icon": "beer",
    })

label lapdance:
    $ renpy.dynamic("present_npcs", choices=[], valid_npcs=[], stripclub_room="stripclub")
    if game.room == "date_stripclub":
        $ stripclub_room = "date_stripclub"
    $ present_npcs = Room.find(stripclub_room).get_present_girls()
    python:
        for npc in present_npcs:
            if npc.id == "shiori" and DONE.get("shiori_stripclub_lapdance_1") and npc.love >= 140:
                valid_npcs.append(npc)
            elif npc.love >= 140 and npc.id != "kiara":
                valid_npcs.append(npc)
    if valid_npcs:
        if len(valid_npcs) == 1:
            $ random_npc = valid_npcs[0]
        else:
            python:
                for npc in sorted(valid_npcs, key=lambda x: x.name):
                    choices.append((f"{npc.name}", npc))
            $ narrator("Who should perform the lapdance?", interact=False)
            $ random_npc = Person.find(renpy.display_menu(choices))
        if renpy.has_label(f"get_{random_npc.id}_lapdance"):
            call expression f"get_{random_npc.id}_lapdance" from _call_expression_264
            if hero.sexperience <= 10:
                $ hero.flags.sexperience += 1
            return
        else:
            $ renpy.show(f"{random_npc.id} lapdance")
    else:
        show chibi lap
    if hero.sexperience <= 10:
        $ hero.flags.sexperience += 1
    "I get a lap dance..."
    return

label harmony_poledance:
    "Raucous music plays as Harmony strides out into the middle of the stage."
    "She hold herself like she owns the place, like a queen holding court."
    "Instantly the crowd pick up on something about the way she's smiling."
    "It's like they just know this is going to be something special."
    "And from the moment she starts to move, Harmony doesn't disappoint."
    show harmony poledance sexynun with fade
    "I was amazed at how little she was wearing when we met up earlier in the night."
    "But now somehow she manages to turn taking it all off into an entire act!"
    "Harmony twists and turns her body, inching her dress off of her shoulders."
    "Little by little, more of her naked flesh is exposed to the watching audience."
    "The weird thing is that I'm every bit as entranced as everyone else."
    "I mean, I've seen Harmony naked more than a few times by now."
    "But somehow seeing her on stage like this makes it all seem new."
    "I'm straining to see all that I can, just like everyone else."
    "And the more I see, the more I crave to see the rest of her."
    "I don't know if Harmony practised this routine beforehand."
    "Maybe the whole thing of dragging me in here was a set-up."
    "Then again, it could all be spontaneous, something she has a natural gift for."
    "Either way she's killing it up there, and I'm getting harder by the second."
    "Harmony's down to her bra and panties by now."
    "And she's wrapping herself around the pole on the stage."
    "I can't believe how easily she's teasing the audience in here."
    "They're following her every move, almost begging for more!"
    "When she finally turns her back and unhooks her bra, the place goes wild."
    "Harmony covers her breasts with both hands, then turns back around."
    "For a moment I think she's going to leave it at that."
    show harmony poledance naked with dissolve
    "But then she reaches out for the pole with her hands."
    "This allows her heavy, round breasts to fall free."
    "Harmony starts to move again, making them sway back and forth."
    "The motion is hypnotic, impossible to ignore."
    "I don't know if I'm being reminded of breast-feeding as a child."
    "Or just seduced by the most perfect pair of breasts imaginable!"
    hide harmony poledance with fade
    return


label drink_poledance:
    $ valid_girls = []
    $ hero.flags.watchedpoledance += 1
    $ present_girls = Room.find(game.room).get_present_girls()
    python:
        for npc in present_girls:
            if npc.id != "kiara":
                valid_girls.append(npc)
    $ valid_girls_ids = " ".join([valid.id for valid in valid_girls])

    scene poledance
    $ renpy.show("poledance " + valid_girls_ids)
    "I watch the pole dance show."
    if hero.flags.watchedpoledance > 5:
        scene bg stripclub
        if len(valid_girls) == 1:
            show expression valid_girls[0].id
            $ renpy.say(valid_girls[0].id, "Thank you [hero.name].")
            $ renpy.say(valid_girls[0].id, "For being such a good client.")
            hide expression valid_girls[0].id
            show expression f"{valid_girls[0].id} naked"
            $ renpy.say(valid_girls[0].id, "Here's a small reward.")
        elif len(valid_girls) == 2:
            show expression valid_girls[0].id at left
            show expression valid_girls[1].id at right
            $ renpy.say(valid_girls[0].id, "Thank you [hero.name].")
            $ renpy.say(valid_girls[1].id, "For being such a good client.")
            hide expression valid_girls[0].id
            hide expression valid_girls[1].id
            show expression f"{valid_girls[0].id} naked" at left
            show expression f"{valid_girls[1].id} naked" at right
            $ renpy.say(valid_girls[0].id, "Here's a small reward.")
        elif len(valid_girls) > 2:
            show expression valid_girls[0].id at left
            show expression valid_girls[1].id at right
            show expression valid_girls[2].id
            $ renpy.say(valid_girls[0].id, "Thank you [hero.name].")
            $ renpy.say(valid_girls[1].id, "For being such a good client.")
            hide expression valid_girls[0].id
            hide expression valid_girls[1].id
            hide expression valid_girls[2].id
            show expression f"{valid_girls[0].id} naked" at left
            show expression f"{valid_girls[1].id} naked" at right
            show expression f"{valid_girls[2].id} naked"
            $ renpy.say(valid_girls[2].id, "Here's a small reward.")
        $ renpy.show(f"poledance naked {valid_girls_ids}")
        "I enjoy my special show."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
