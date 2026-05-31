init 1:
    image bg date_park = LayeredImageProxy(randchoice(["bg park", "bg pond"]))

init -2 python:
    Room(
    **{
        "name": "date_park",
        "exits": ["map"],
        "display_name": "Park",
        "hours": (14, 18),
        "conditions": [
            IsHour(14, 18),
        ],
        "music": season_music(),
        "random_music": True,
        "outfit": "casual",
        "tags": ["dateroom"],
    }
)

    Date(
    "park",
    display_name="Park",
    clothes="casual",
    conditions=[ValidRooms("date_park")],
    love_gain=2,
)

    Activity(
    **{
        "name": "date_go_for_a_run",
        "fun": 1,
        "icon": "jog",
        "display_name": "Run together",
        "rooms": "date_park",
        "conditions": [
            HeroTarget(MinStat("fitness", 10)),
        ],
        "label": "date_go_for_a_run",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_hold_hand",
        "fun": 1,
        "icon": "holdhand",
        "display_name": "Hold [date_girl.possessive_adjective] hand",
        "rooms": ("date_park", "date_mall1"),
        "conditions": [
            HeroTarget(MinStat("fitness", 10)),
        ],
        "label": "date_hold_hand",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_read_poetry",
        "fun": 1,
        "icon": "sing",
        "display_name": "Read poetry",
        "label": "date_read_poetry",
        "rooms": "date_park",
        "conditions": [
            HeroTarget(MinStat("knowledge", 10)),
        ],
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_picnic",
        "fun": 1,
        "hunger": 10,
        "icon": "picnic",
        "display_name": "Have a picnic",
        "label": "date_picnic",
        "rooms": "date_park",
        "conditions": [
            IsSeason(0, 1, 2),
        ],
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_cloud_gaze",
        "fun": 1,
        "icon": "clouds",
        "display_name": "Watch the clouds",
        "rooms": "date_park",
        "conditions": [
            HeroTarget(MinStat("charm", 10)),
        ],
        "label": "date_cloud_gaze",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_snow_ball_fight",
        "fun": 1,
        "icon": "snowball",
        "display_name": "Have a snowball fight",
        "rooms": "date_park",
        "conditions": [
            IsSeason(3),
            HeroTarget(MinStat("fitness", 10)),
        ],
        "label": "date_snow_ball_fight",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_ice_skating",
        "fun": 1,
        "icon": "iceskating",
        "display_name": "Ice skate",
        "rooms": "date_park",
        "conditions": [
            IsSeason(3),
            HeroTarget(MinStat("fitness", 25)),
        ],
        "label": "date_ice_skating",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_make_snowman",
        "fun": 1,
        "icon": "snowman",
        "display_name": "Make a snowman",
        "rooms": "date_park",
        "conditions": [
            IsSeason(3),
        ],
        "label": "date_make_snowman",
        "once_day": True,
    }
)

    Event(
    **{
        "name": "date_park_random_events",
        "label": "date_park_random_events",
        "priority": 0,
        "conditions": [
            HeroTarget(OnDate(), IsRoom("date_park")),
        ],
        "chances": 20,
        "do_once": False,
        "once_day": True,
    }
)











label date_park_random_events:
    scene bg park
    $ renpy.show(date_girl.id)
    $ r = randint(1, 10)
    if r <= 1 and game.season == 3:
        "It's so bitingly cold today that I'm glad to have wrapped up with more warm layers than I would usually have bothered with."
        "But a casual glance at [date_girl.name] shows me that she's shivering and I can almost hear her teeth chattering."
        menu:
            "Offer her your coat":
                call expression f"date_park_random_events_dialogues_1_{hero.gender}" from _call_expression_315
                if "princess" in date_girl.traits:
                    "[date_girl.name] accepts the offer without hesitation, happy to be on the receiving end of such kindness."
                    $ game.active_date.score += 10
                elif "rebel" in date_girl.traits:
                    "[date_girl.name] shakes her head in disgust at the offer and walks on ahead, rubbing her arms for added warmth."
                    $ game.active_date.score -= 10
                else:
                    "[date_girl.name] refuses for a short while, and then grudgingly accepts the offer."
                    $ game.active_date.score += 5
            "Do not offer her your coat":
                call expression f"date_park_random_events_dialogues_2_{hero.gender}" from _call_expression_316
                if "princess" in date_girl.traits:
                    "[date_girl.name] makes a haughty noise and turns her nose up at me, clearly having been expecting more than a critical comment."
                    $ game.active_date.score -= 10
                if "rebel" in date_girl.traits:
                    "[date_girl.name] frowns as if she doesn't particularly care and just shakes her head, as if not in the least bit bothered about the discomfort."
                    $ game.active_date.score += 5
                else:
                    "[date_girl.name] looks a little hurt at the blunt nature of my comment, rubbing her arms in an attempt to generate more warmth."
                    $ game.active_date.score -= 5
    elif r <= 2 and game.season == 1:
        "The grassy areas of the park are almost all covered with people playing casual games and sports."
        "Eventually the inevitable happens, and a football rolls to a stop, right by my feet."
        "As the people to whom it belongs begin to call for it back, [date_girl.name] looks at me to see what my reaction will be."
        menu:
            "Punt the ball back":
                "I take a couple of steps back and punt the ball as hard as I can in their direction."
                "It's nothing particularly impressive, but it gets the job done all the same."
                if "sporty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] seems impressed with the way I stepped up to even such a minor challenge."
                elif "geek" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks surprised that I'd even know what to do with a football without an explanation."
                else:
                    $ game.active_date.score += 5
                    "[date_girl.name] doesn't seem in the least bit perturbed or impressed by what just happened, and so we just walk on."
            "Ignore the ball and walk on":
                "Afraid that I'll just send the ball flying in the wrong direction, I ignore it and pretend not to have heard the cries of its owners behind me as I walk on."
                if "sporty" in date_girl.traits or "not_geek" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] says nothing, but I can see her shaking her head in disbelief that I'd be so timid."
                elif "geek" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] keeps quiet, but I can see a look of empathy in her eyes, as if she'd have done the same thing for similar reasons."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] doesn't seem in the least bit perturbed or impressed by what just happened, and so we just walk on."
    elif r <= 3:
        "I can vaguely hear the sound of someone calling out in vain for an errant dog to come to heel."
        "[date_girl.name] yelps in surprise and alarm, making me glance round to see a large and very slobbery dog bearing down on us."
        menu:
            "Recoil from the dog":
                "I've never been too keen on big dogs, and this one seems to have appeared out of nowhere."
                "I cry out too and back off from the dog, trying to keep it from getting any closer."
                if "innocent" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] clings to me, looking relieved to see me have the same reaction as she did."
                elif "playful" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks surprised at my reaction, and instantly goes to pet the approaching dog."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] makes no move to approach the dog, but looks a little surprised at my dramatic reaction to it all the same."
            "Pet the dog":
                "I'm fond enough of dogs to know that this one just wants to play, so I hold out my hand and encourage him to come closer for a fuss."
                if "innocent" in date_girl.traits:
                    "[date_girl.name] cries out again, not reassured by my example, and hides behind my back."
                    $ game.active_date.score -= 10
                elif "playful" in date_girl.traits:
                    "[date_girl.name] follows my lead, and soon we're showering the happy dog with praise and attention as his owner approaches."
                    $ game.active_date.score += 10
                else:
                    "[date_girl.name] smiles at my petting the eager dog, but doesn't seem inclined to join me in doing so any time soon."
                    $ game.active_date.score += 5
    elif r <= 4:
        "Walking through a secluded part of the park, it occurs to me that a spot amongst the trees is almost completely hidden from the view of the path we're on."
        "[date_girl.name] notices the attention that I'm giving the little nook and looks at me for an explanation."
        menu:
            "Admit it looks inviting for an amorous liaison":
                call expression f"date_park_random_events_dialogues_3_{hero.gender}" from _call_expression_317
                if "slutty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] grins wickedly, instantly picking up on the possibilities of sex in a public place."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] gives me a puzzled look, as if she thinks I mean to use the spot to piss in or something just as mundane."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] smiles indulgently, but I get the impression she has a more pure and romantic image of the whole thing than I do."
            "Say it could be used for a prank":
                call expression f"date_park_random_events_dialogues_4_{hero.gender}" from _call_expression_318
                if "slutty" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] stares at me, amazed that I'd miss such a blatant opportunity to misbehave in public."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] giggles and snorts at the thought of pulling off just such a prank."
                else:
                    $ game.active_date.score += 5
                    "[date_girl.name] shakes her head, not sure if she should find my childish suggestion pathetic or endearing."
    elif r <= 5:
        "I have to confess to being rather fond of admiring female joggers as they pass me in the park."
        "Unfortunately for me, it's become such a habit, that when a couple sprint past, I totally forget who's company I'm currently in."
        "[date_girl.name] notes my interest in their lycra-clad forms, making me stutter to explain myself."
        menu:
            "Admit that you were looking":
                call expression f"date_park_random_events_dialogues_5_{hero.gender}" from _call_expression_319
                if "flirty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] smiles and squeezes my hand, giving me the distinct impression that she's storing that little admission away for a later date."
                elif "yandere" in date_girl.traits:
                    $ game.active_date.score -= 10
                    $ date_girl.yandere += 1
                    "[date_girl.name] almost ignores what I say, as she shoots evil, almost threatening glances at the joggers as they disappear around a corner up ahead."
                else:
                    "[date_girl.name] shakes her head a little ruefully, but seems to appreciate my honesty all the same."
            "Make an insulting comment":
                call expression f"date_park_random_events_dialogues_6_{hero.gender}" from _call_expression_320
                if "bitchy" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] sneers a little and nods in agreement, clearly amused by my putting the other girls down in front of her."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] gives me a scrutinising look, as if she's not sure she believes I was just looking to pass judgement on the joggers."
    elif r <= 6:
        "As we walk past a stand of trees, the sound of someone playing a guitar and singing can be heard."
        "When the musician comes into view, I see a long-haired, hippy kind of guy being adored by at least half-a-dozen girls."
        "[date_girl.name] smiles sideways at me, clearly looking to discover just what I think of the scene."
        menu:
            "Dismiss the guitarist as a jerk":
                call expression f"date_park_random_events_dialogues_7_{hero.gender}" from _call_expression_321
                if "workaholic" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] raises her eyebrows in approval and snorts derisively at the fawning crowd around the bohemian guitarist."
                elif "music" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shakes her head and snorts at my dismissing the guitarist, clearly thinking that I'm just jealous of the attention that he's attracting."
                else:
                    "[date_girl.name] shrugs, as if she's not convinced that I'm being entirely unbiased in my assessment of the guitarist and might be just a little jealous."
            "Envy the guitarist his popularity":
                call expression f"date_park_random_events_dialogues_8_{hero.gender}" from _call_expression_322
                if "workaholic" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shakes her head in disapproval, clearly not impressed by the bohemian guitarist or my desire to emulate him."
                elif "music" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] smiles in genuine approval, pressing herself a little closer to me now she knows I desire a bohemian lifestyle too."
                else:
                    "[date_girl.name] shrugs, as though she's not particularly interested in the idea of emulating what pretty much amounts to a busker."
    elif r <= 7:
        "The green spaces of the park are almost totally full of happy, laughing families, their picnics spread out on colourful blankets."
        "Parents sit on the ground, while kids toss frisbees and play with bouncy dogs."
        "I see that [date_girl.name] is staring intently at the scene, and she turns her head, catching me staring at her in turn."
        menu:
            "Gush over the happy families":
                call expression f"date_park_random_events_dialogues_9_{hero.gender}" from _call_expression_323
                if "family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] squeezes my hand suddenly and smiles as widely as her mouth can manage."
                    "It seems like I've said something that she very much approves of..."
                elif "not_family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name]'s mouth hangs open as she almost literally shudders at the thought of being in the same position as the parents on their picnic blankets."
                else:
                    "[date_girl.name] gives me an enigmatic grin, but doesn't say as much as a word in way of response."
            "Shudder at the thought of being tied down with a family":
                call expression f"date_park_random_events_dialogues_10_{hero.gender}" from _call_expression_324
                if "family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me with an expression of surprise and not a little sadness on her face."
                elif "not_family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] gives me a slow and very much approving smile, letting me know that she feels the exact same way too."
                else:
                    "[date_girl.name] gives me an enigmatic grin, but doesn't say as much as a word in way of response."
    elif r <= 8 and game.season == 1:
        "We had been planning on going for walk around the park, but the amazingly hot weather sees us finding a suitable spot and just laying down instead."
        "As I settle down to enjoy the sun, I notice that a couple of girls nearby have actually gone topless, right here in the park!"
        "[date_girl.name] follows my gaze and sees the same thing, and then looks at me as if challenging me to explain my interest in the sight."
        menu:
            "Disapprove of the topless sunbathing":
                call expression f"date_park_random_events_dialogues_11_{hero.gender}" from _call_expression_325
                if "trashy" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shrugs and keeps on admiring the sight of the girls, as if she's impressed by their boldness."
                elif "submissive" in date_girl.traits or "princess" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods furiously, as if she's almost too eager to second my disapproval."
                else:
                    "[date_girl.name] shrugs, as if to say that she's not particularly interested in what other people are doing right now."
            "Applaud the topless sunbathers":
                call expression f"date_park_random_events_dialogues_12_{hero.gender}" from _call_expression_326
                if "trashy" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] chuckles and shakes her head, as if taking my admiration for the topless sunbathers as a personal challenge."
                    "One that she will have to rise to at a later date..."
                elif "submissive" in date_girl.traits or "princess" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me as if she's been given an outright order, and begins to unbutton her top..."
                else:
                    "[date_girl.name] shrugs, as if to say that she's not particularly interested in what other people are doing right now."
    elif r <= 9:
        "I spot that a new cafe has opened up in the park, and then remember hearing pretty good things about it too."
        "It's getting close to lunchtime, and I wonder if we should call in and grab a bite to eat."
        "[date_girl.name] notices the cafe too, and then that I'm looking at it with interest."
        menu:
            "Suggest that you grab a bite to eat at the cafe":
                call expression f"date_park_random_events_dialogues_13_{hero.gender}" from _call_expression_327
                if "poor" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] keeps on staring at the fancy decor of the place, and I begin to wonder if I've made a mistake."
                elif "gourmand" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods with enthusiasm, practically pulling me towards the door."
                else:
                    "[date_girl.name] give me a 'what-the-hell' smile, and seems to want to leave the ultimate decision up to me."
            "Suggest that you just eat a hotdog":
                call expression f"date_park_random_events_dialogues_14_{hero.gender}" from _call_expression_328
                if "poor" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods and smiles, looking positively relieved at my suggestion."
                elif "gourmand" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name]'s face falls at my suggestion, and she looks back over her shoulder longingly as we walk away."
                else:
                    "[date_girl.name] shrugs and shakes her head, as if to say that she's fine with whatever."
    elif r <= 10:
        "I hear voices from around the corner, and then see a large group of people come into view as we walk around it."
        "Craning my neck, I can just see that the crowd has gathered to watch what looks like a play being performed in the open air."
        "[date_girl.name] spots the same thing, standing up on her tip-toes to get a better look."
        menu:
            "Suggest that you stay and watch":
                call expression f"date_park_random_events_dialogues_15_{hero.gender}" from _call_expression_329
                if "bookworm" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods with enthusiasm, already looking for a way into the crowd."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] rolls her eyes and sighs dramatically, as though the idea is the most tedious thing ever."
                else:
                    "[date_girl.name] gives a nonchalant shrug, as if she's equally happy to indulge me or simply walk on by."
            "Sneer at the players":
                call expression f"date_park_random_events_dialogues_16_{hero.gender}" from _call_expression_330
                if "bookworm" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] frowns at me and furrows her brows, as if resisting the temptation to call me an uncultured oaf."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] laughs and nods in agreement, shaking her head at the crowd as we walk away."
                else:
                    "[date_girl.name] shakes her head, as if she's not particularly interested in or offended by the presence of the play and its audience."
    $ renpy.hide(date_girl.id)
    return

label date_hold_hand:
    $ renpy.show(active_girl.id)
    "I hold [active_girl.name]'s hand."
    $ gain = 5
    if "innocent" in active_girl.traits:
        "She's blushing quite cutely!"
        $ gain += 5
    if "romantic" in active_girl.traits:
        $ gain += 5
    $ game.active_date.score += gain
    $ renpy.hide(active_girl.id)
    return

label date_picnic:
    $ renpy.show(active_girl.id)
    call expression f"date_picnic_dialogues_1_{hero.gender}" from _call_expression_331
    if "gourmand" in active_girl.traits:
        active_girl.say "Great idea!"
        $ game.active_date.score += 10
    else:
        active_girl.say "I'd love to."
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_make_snowman:
    $ renpy.show(active_girl.id)
    call expression f"date_make_snowman_dialogues_1_{hero.gender}" from _call_expression_332
    if "not_artsy" in active_girl.traits or "not_playful" in active_girl.traits:
        active_girl.say "I don't feel like it."
        $ game.active_date.score -= 20
        $ hero.cancel_activity()
    if "artsy" not in active_girl.traits and "playful" not in active_girl.traits:
        active_girl.say "I don't feel like it."
        $ game.active_date.score -= 10
        $ hero.cancel_activity()
    else:
        active_girl.say "I'd love to."
        "We make a snowman together."
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_snow_ball_fight:
    $ renpy.show(active_girl.id)
    "I throw a snowball at [active_girl.name]."
    if "playful" not in active_girl.traits:
        active_girl.say "Stop it, that's not funny."
        $ game.active_date.score -= 10
        $ hero.cancel_activity()
    else:
        active_girl.say "Hey, You'll pay for that!"
        "We have fun having a snowball fight."
        $ game.active_date.score += 5
        if hero.fitness >= date_girl.sub:
            $ date_girl.sub += 2
            "I won!"
        else:
            $ date_girl.sub -= 2
            "I lose."
    $ renpy.hide(active_girl.id)
    return

label date_ice_skating:
    $ renpy.show(active_girl.id)
    "We go to the frozen lake to have fun."
    if "playful" in active_girl.traits:
        $ game.active_date.score += 5
    if "not_playful" in active_girl.traits:
        $ game.active_date.score -= 5
    if "innocent" in active_girl.traits:
        $ game.active_date.score += 5
    if "sporty" in active_girl.traits:
        $ game.active_date.score += 5
    $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_cloud_gaze:
    $ renpy.show(active_girl.id)
    call expression f"date_cloud_gaze_dialogues_1_{hero.gender}" from _call_expression_333
    if "dreamer" not in active_girl.traits:
        active_girl.say "No, thank you."
        $ game.active_date.score -= 10
        $ hero.cancel_activity()
    else:
        active_girl.say "Yes, sure."
        "We sit on a bench and watch at funny clouds."
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_read_poetry:
    $ renpy.show(active_girl.id)
    call expression f"date_read_poetry_dialogues_1_{hero.gender}" from _call_expression_334
    if "not_bookworm" in active_girl.traits or "not_artsy" in active_girl.traits or "not_dreamer" in active_girl.traits:
        active_girl.say "No, thank you."
        $ game.active_date.score -= 20
        $ hero.cancel_activity()
    if "bookworm" not in active_girl.traits and "artsy" not in active_girl.traits and "dreamer" not in active_girl.traits:
        active_girl.say "No, thank you."
        $ game.active_date.score -= 10
        $ hero.cancel_activity()
    else:
        active_girl.say "Yes, sure."
        "We sit under a tree and I start reading her some poetry."
        $ game.active_date.score += 5
    $ renpy.hide(active_girl.id)
    return

label date_go_for_a_run:
    $ renpy.show(active_girl.id)
    call expression f"date_go_for_a_run_dialogues_1_{hero.gender}" from _call_expression_335
    if "sporty" not in active_girl.traits:
        active_girl.say "No, thank you."
        $ game.active_date.score -= 10
        $ hero.cancel_activity()
    else:
        "[active_girl.name] quickly change into her sports clothes."
        $ renpy.show(f"{active_girl.id} sport")
        active_girl.say "Ready whenever you are."
        "We have a good race."
        $ game.active_date.score += 5
        if hero.fitness >= date_girl.sub:
            $ date_girl.sub += 2
            "I won!"
        else:
            $ date_girl.sub -= 2
            "I lose."
        $ renpy.show(f"{active_girl.id} casual")
    $ renpy.hide(active_girl.id)
    return

label date_park:
    $ renpy.show(active_girl.id)
    "We go to the park."
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
