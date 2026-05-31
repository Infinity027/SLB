layeredimage bg date_beach:
    if game.hour >= 20 or game.hour <= 5:
        "beach_night"
    else:
        "beach_day"

init -2 python:
    Room(
    **{
        "name": "date_beach",
        "exits": ["map"],
        "display_name": "Beach",
        "hours": (14, 17),
        "conditions": [
            IsHour(14, 17),
            IsSeason(0, 1),
            InInventory("swimsuit"),
            HasVehicle(motor=True),
        ],
        "music": "music/roa_music/summer_air.ogg",
        "outfit": "swimsuit",
        "tags": ["dateroom"],
    }
)

    Date(
    "beach",
    display_name="Beach",
    conditions=[ValidRooms("date_beach")],
    clothes="swimsuit",
    love_gain=3,
)

    Activity(
    **{
        "name": "date_icecream_beach",
        "money_cost": 10,
        "hunger": 1,
        "icon": "icecream",
        "rooms": ("date_beach", "date_nudistbeach"),
        "display_name": "Have an ice cream",
        "label": "date_icecream_beach",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_suntan",
        "energy": 2,
        "icon": "tan",
        "rooms": ("date_beach", "date_nudistbeach"),
        "conditions": [
            InInventory("lotion"),
        ],
        "display_name": "Apply sunscreen",
        "label": "date_suntan",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_swimmingrace_beach",
        "energy": -2,
        "icon": "swim",
        "rooms": ("date_beach", "date_nudistbeach"),
        "display_name": "Swim together in the sea",
        "label": "date_swimmingrace_beach",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_play_beach",
        "icon": "playinsea",
        "rooms": ("date_beach", "date_nudistbeach"),
        "display_name": "Play in the sea",
        "label": "date_play_beach",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_volley_beach",
        "icon": "beachvolleyball",
        "rooms": ("date_beach", "date_nudistbeach"),
        "conditions": [
            HeroTarget(MinStat("fitness", 50)),
        ],
        "display_name": "Play some beach volley",
        "label": "date_volley_beach",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_castle_beach",
        "icon": "sandcastle",
        "rooms": ("date_beach", "date_nudistbeach"),
        "conditions": [
            HeroTarget(MinStat("charm", 50)),
        ],
        "display_name": "Make a sand castle",
        "label": "date_castle_beach",
        "once_day": True,
    }
)

    Event(
    **{
        "name": "date_beach_random_events",
        "label": "date_beach_random_events",
        "priority": 0,
        "conditions": [
            HeroTarget(OnDate(), IsRoom("date_beach", "date_nudistbeach")),
        ],
        "chances": 20,
        "do_once": False,
        "once_day": True,
    }
)

label date_beach_random_events:
    scene bg beach
    $ renpy.show(date_girl.id)
    $ r = randint(1, 5)
    if r == 1:
        "I try to keep my eyes off of the other girls on the beach today and on [date_girl.name]."
        "But I'm only human, and so I eventually get caught as my eye wanders in their general direction."
        "I shrug, trying to laugh it off as best I can while coming up with a good excuse for my behaviour."
        menu:
            "Deny":
                call expression f"date_beach_random_events_dialogues_1_{hero.gender}" from _call_expression_271
                if "innocent" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] blushes at the mention of the revealing swimsuits and nods in agreement."
                elif "slutty" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] rolls her eyes and shakes her head, clearly annoyed by my prudish comments."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] strains to see the girls I'm talking about, but looks less than convinced of my professed disapproval."
            "Admit":
                call expression f"date_beach_random_events_dialogues_2_{hero.gender}" from _call_expression_272
                if "innocent" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks instantly hurt and like she just can't understand why I'm looking at other girls."
                elif "slutty" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] raises her eyebrows at the admission, as if she's intrigued by my honesty."
                    "But at the same time, I notice how she thrusts her chest out and flaunts herself all the more."
                else:
                    "[date_girl.name] shakes her head in disapproval, but I can see that she's smiling in amusement at my typically male behaviour."
    elif r == 2:
        "As we relax on the sand, I notice a gaggle of kids engaged in the building of sandcastles not too far away."
        "I can't help watching them, and kind of marvelling at the amount of effort they're putting into it."
        "But all too soon the tide starts to come in, washing away all of their work in mere moments."
        menu:
            "Laugh":
                call expression f"date_beach_random_events_dialogues_3_{hero.gender}" from _call_expression_273
                if "bitchy" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] laughs as she watches the kids trying in vain to save their work."
                elif "family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at the kids with sympathy in her eyes, and then back at me in a disapproving manner."
                else:
                    "[date_girl.name] looks over at the kids, but doesn't seem overly concerned about their plight."
            "Sympathise":
                call expression f"date_beach_random_events_dialogues_4_{hero.gender}" from _call_expression_274
                if "bitchy" in date_girl.traits:
                    $ game.active_date.score -= 5
                    "[date_girl.name] tuts and shakes her head, like she's disappointed in my compassion for the kids."
                if "family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods in sympathy, clearly feeling the same compassion for the kids."
                else:
                    "[date_girl.name] looks over at the kids, but doesn't seem overly concerned about their plight."
    elif r == 3 and hero.has_skill("guitar"):
        "I'm feeling pretty chilled and relaxed as we hang out at the beach."
        "And right now seems like it might be the perfect moment to whip out my guitar to serenade [date_girl.name]."
        "She's seen that I have it with me, but I'm still not sure if she'll be into it..."
        menu:
            "Play the guitar":
                call expression f"date_beach_random_events_dialogues_5_{hero.gender}" from _call_expression_275
                "I smile as I begin to strum the instrument and clear my throat."
                if "music" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods and smiles, eagerly leaning forward to hear me play."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score -= 5
                    "[date_girl.name] blows out her cheeks and shakes her head, clearly annoyed at having her sunbathing interrupted."
                else:
                    $ game.active_date.score += 5
                    "[date_girl.name] rolls onto her side to listen, but keeps on sunbathing all the same."
            "Don't play the guitar":
                "I reach for the guitar, but then hesitate and pull my hand away from it again."
                call expression f"date_beach_random_events_dialogues_6_{hero.gender}" from _call_expression_276
                if "music" in date_girl.traits:
                    $ game.active_date.score -= 5
                    "[date_girl.name]'s mouth falls open, as if she's disappointed."
                    "I could offer to play anyway, but I sense that the moment has passed me by..."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] smiles in approval, then closes her eyes and keeps on soaking up the rays."
                else:
                    "[date_girl.name] shrugs and closes her eyes, as if she would have listened, but isn't devastated at not hearing me play."
    elif r in(3, 4):
        "I've spotted a bunch of girls playing beach volleyball not too far from where we're sitting."
        "Okay, okay...I admit it - I've been watching them on the sly since I noticed them!"
        "I see that they're a couple of players short, and so when their ball lands by my foot, they call for us to come join their game."
        menu:
            "Accept":
                call expression f"date_beach_random_events_dialogues_7_{hero.gender}" from _call_expression_277
                "I pull [date_girl.name] to her feet, giving her little choice in the matter."
                if "sporty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] hardly need any motivation, as she leaps to her feet and hurries over to play."
                elif "yandere" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] frowns from the moment we get over to the other girls, looking daggers at them the whole time."
                elif "flirty" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] follows my lead, but makes certain that she's in my line of sight the entire game."
                else:
                    "[date_girl.name] shrugs and allows me to drag her along in my wake."
            "Refuse":
                "I toss the ball back to the girls, but shake my head at their invitation to play."
                call expression f"date_beach_random_events_dialogues_8_{hero.gender}" from _call_expression_278
                if "sporty" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] nods, but looks pouty and somewhat disappointed at the missed chance to compete."
                elif "yandere" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] gives me an approving smile, and eyes the girls as if daring them to come as much as a single step closer."
                elif "flirty" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] looks pleased to have been let off the hook, but eyes the other girls jealously all the same."
                else:
                    "[date_girl.name] nods at my decision, not looking too bothered either way."
    elif r == 5:
        "As I lie on the beach, my eye settles on a girl in a swimsuit that's visibly pregnant."
        "The curve of her belly and the way that she cradles it fascinates me."
        "And I'm still looking at her when [date_girl.name] catches me in the act."
        menu:
            "Play it down":
                call expression f"date_beach_random_events_dialogues_9_{hero.gender}" from _call_expression_279
                if "family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at the pregnant girl, and then down at the ground, as if my words have made her feel sad."
                if "slutty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] smiles at the implications of what I'm saying, probably thinking of sex without the consequences."
                if "rebel" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] looks haughtily at the pregnant girl, as if judging her lifestyle choices."
                else:
                    "[date_girl.name] nods and then shakes her head, leaving me wondering what she really thinks."
            "Own it":
                call expression f"date_beach_random_events_dialogues_10_{hero.gender}" from _call_expression_280
                if "family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] gives me a wide smile and nods with genuine enthusiasm, as if I've said just the right thing."
                elif "slutty" in date_girl.traits:
                    $ game.active_date.score -= 5
                    "[date_girl.name] shakes her head in disbelief, tutting at the sentiment I've just expressed."
                elif "rebel" in date_girl.traits:
                    $ game.active_date.score -= 5
                    "[date_girl.name] looks haughtily at the pregnant girl, as if judging her lifestyle choices."
                else:
                    "[date_girl.name] nods and gives me an enigmatic look, leaving me wondering what she really thinks."
    return

label date_castle_beach:
    if game.room == 'date_nudistbeach':
        show expression "beach sandcastle " + date_girl.id + " naked mc_naked"
    else:
        show expression "beach sandcastle " + date_girl.id
    "I make a sand castle with [date_girl.name]."
    call expression date_girl.get_chat from _call_expression_64
    if "playful" in date_girl.traits:
        $ game.active_date.score += 5
    if "not_playful" in date_girl.traits:
        $ game.active_date.score -= 5
    hide expression "beach sandcastle " + date_girl.id
    return

label date_volley_beach:
    if game.room == 'date_nudistbeach':
        show expression "beach volleyball " + date_girl.id + " naked"
    else:
        show expression "beach volleyball " + date_girl.id
    "I play some beach volley with [date_girl.name]."
    $ game.active_date.score += 5
    call expression date_girl.get_chat from _call_expression_65
    if "playful" in date_girl.traits or "sporty" in date_girl.traits:
        $ game.active_date.score += 5
    if "not_playful" in date_girl.traits or "not_sporty" in date_girl.traits:
        $ game.active_date.score -= 5
    if hero.fitness >= date_girl.sub:
        $ date_girl.sub += 2
        "I won!"
    else:
        $ date_girl.sub -= 2
        "I lose."
    hide expression "beach volleyball " + date_girl.id
    return

label date_play_beach:
    if game.room == 'date_nudistbeach':
        show expression "playing water " + date_girl.id + " naked mc_naked"
    else:
        show expression "playing water " + date_girl.id
    "I play with [date_girl.name] in the sea."
    $ game.active_date.score += 5
    call expression date_girl.get_chat from _call_expression_90
    if "playful" in date_girl.traits or "sporty" in date_girl.traits:
        $ game.active_date.score += 5
    if "not_playful" in date_girl.traits or "not_sporty" in date_girl.traits:
        $ game.active_date.score -= 5
    hide expression "playing water " + date_girl.id
    return

label date_swimmingrace_beach:
    if game.room == 'date_nudistbeach':
        show expression "swimmingrace " + date_girl.id + " naked"
    else:
        show expression "swimmingrace " + date_girl.id
    "I swim with [date_girl.name] in the sea."
    $ game.active_date.score += 5
    call expression date_girl.get_chat from _call_expression_92
    if "sporty" in date_girl.traits:
        $ game.active_date.score += 5
    if hero.fitness >= date_girl.sub:
        $ date_girl.sub += 2
        "I won!"
    else:
        $ date_girl.sub -= 2
        "I lose."
    hide expression "swimmingrace " + date_girl.id
    return

label date_suntan:
    if game.room == 'date_nudistbeach':
        show expression "beach cream " + date_girl.id + " naked"
    else:
        show expression "beach cream " + date_girl.id
    "I put sunscreen lotion on [date_girl.name]."
    $ game.active_date.score += 5
    call expression date_girl.get_chat from _call_expression_132
    if "princess" in date_girl.traits:
        $ game.active_date.score += 5
    hide expression "beach cream " + date_girl.id
    return

label date_icecream_beach:
    if game.room == 'date_nudistbeach':
        show expression "beach icecream " + date_girl.id + " naked mc_naked"
    else:
        show expression "beach icecream " + date_girl.id
    if renpy.has_label(f"{active_girl.id}_ice_cream_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_ice_cream_reaction_{hero.gender}" from _call_expression_281
    else:
        "We eat an ice cream together."
    call expression date_girl.get_chat from _call_expression_282
    if "gourmand" in date_girl.traits:
        $ game.active_date.score += 5
    hide expression "beach icecream " + date_girl.id
    return

label date_beach:
    if game.room == 'date_nudistbeach':
        $ renpy.show(date_girl.id + " naked")
    else:
        $ renpy.show(date_girl.id)
    "We go to the beach."
    if "sports_car" in hero.inventory:
        $ game.active_date.score += 5
    $ renpy.hide(date_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
