init 1:
    image bg date_pub = LayeredImageProxy(randchoice(["bg pub", "bg pubexterior", "bg pubplay", "bg pubseat"]))

init python:
    Room(**{
    "name": "date_pub",
    "exits": ["map"],
    "display_name": "Pub",
    "hours": (20, 23),
    "conditions": [
        IsHour(20, 23),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["dateroom"],
    })

    Date(
    "pub",
    display_name = "Pub",
    money_cost=10,
    conditions=[ValidRooms("date_pub")],
    clothes = "casual",
    love_gain = 2,
    )

    Activity(**{
    "name": "date_play_darts",
    "fun": 1,
    "icon": "darts",
    "display_name": "Play darts",
    "rooms": "date_pub",
    "label": "date_play_darts",
    "once_day": True,
    })

    Activity(**{
    "name": "buy_a_round",
    "fun": 1,
    "icon": "round",
    "money_cost": 25,
    "display_name": "Buy a round",
    "rooms": "date_pub",
    "label": "date_buy_a_round",
    "once_day": True,
    })

    Activity(**{
    "name": "date_pub_play_pool",
    "fun": 1,
    "icon": "pool",
    "display_name": "Play pool",
    "rooms": "date_pub",
    "label": "date_pub_play_pool",
    "once_day": True,
    })

    Activity(**{
    "name": "date_eat_a_burger",
    "duration": 0,
    "hunger": 7,
    "money_cost": 20,
    "icon": "burger",
    "once_day": True,
    "rooms": "date_pub",
    "conditions": [
        HeroTarget(MinStat("hunger", 0)),
        ],
    "display_name": "Eat a burger",
    "label": "date_eat_a_burger",
    })

    Event(**{
    "name": "date_pub_random_events",
    "label": "date_pub_random_events",
    "priority": 0,
    "conditions": [
        HeroTarget(OnDate(), IsRoom("date_pub")),
        ],
    "chances": 20,
    "do_once": False,
    "once_day": True,
    })


label date_pub_random_events:
    scene bg pub
    $ renpy.show(date_girl.id)
    $ r = randint(1, 10)
    if r <= 1:
        "After a while, I notice a girl at the next table smiling at me."
        "The fact that I'm clearly on a date doesn't seem to discourage her in the least."
        "[date_girl.name] seems to have noticed her attentions too."
        menu:
            "Blow the other girl off":
                call expression f"date_pub_random_events_dialogues_1_{hero.gender}" from _call_expression_336
            "Flirt back":

                call expression f"date_pub_random_events_dialogues_2_{hero.gender}" from _call_expression_337
                if "submissive" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] blushes at the sight of me paying attention to another girl in front of her."
                    "But she just smiles helplessly and watches all the same."
                elif "yandere" in date_girl.traits:
                    $ game.active_date.score -= 10
                    $ date_girl.yandere += 1
                    "[date_girl.name]'s eyes flare with anger at the mere sight of the other girl as she flirts with me."
                    "But I'm relieved to see that almost all of her ire is directed at the girl, rather than me!"
    elif r <= 2:
        "The table across from us suddenly goes from being empty to filled by a couple and their noisy kids."
        "[date_girl.name] glances over at the ensuing chaos and din, and then back at me."
        menu:
            "Suggest moving":
                call expression f"date_pub_random_events_dialogues_3_{hero.gender}" from _call_expression_338
                if "family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me as though I just said something offensive, and slowly shakes her head."
                elif "not_family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods in agreement, smiling more than a little at my annoyance."
                else:
                    "[date_girl.name] shrugs, as if she's not particularly bothered either way."
            "Fawn over the kids":
                call expression f"date_pub_random_events_dialogues_4_{hero.gender}" from _call_expression_339
                if "family" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] gives the little family an adoring gaze and then another one to me."
                elif "not_family" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] frowns, looking at me like I have smoking turds hanging out of my mouth."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] shakes her head, as if saying she couldn't care less."
    elif r <= 3:
        "Waiting to be served at the bar, a girl jumps ahead of me as soon as the bartender asks who's next."
        "[date_girl.name] stares at the queue-jumper and then looks at me, clearly wondering if I'm going to let it go."
        menu:
            "Protest":
                call expression f"date_pub_random_events_dialogues_5_{hero.gender}" from _call_expression_340
                if "dominant" in date_girl.traits:
                    $ game.active_date.score += 10
                    "The girl looks surprised and apologises, making [date_girl.name] smile and give me a look of approval."
                elif "bitchy" in date_girl.traits:
                    $ game.active_date.score += 10
                    "The girl seems taken aback and lets me go before her, but [date_girl.name] eyes her up and makes a huffy, disapproving sound all the same."
                else:
                    "The girl apologises and steps aside, but [date_girl.name]'s face says that I could have just let the matter drop."
            "Let it go":
                call expression f"date_pub_random_events_dialogues_6_{hero.gender}" from _call_expression_341
                if "dominant" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shakes her head, as if annoyed at my not standing up for myself."
                elif "bitchy" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "The queue-jumper gets her drinks before us, but [date_girl.name] deftly manages to elbow one of them over without being seen."
                    "As we walk away from the bar, I see [date_girl.name] grin at getting her revenge."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] shakes her head."
    elif r <= 4:
        "We're chatting away when the weekly pub quiz begins in the background."
        "[date_girl.name] cocks her head at the first question, as if she's trying to come up with an answer."
        menu:
            "Answer seriously":
                "I know this one, so I just come straight out with the answer."
                if "bookworm" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] looks at me with a smile, genuinely impressed with my show of knowledge."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score += 5
                    "[date_girl.name] looks at me like she's surprised I know the answer."
                else:
                    "[date_girl.name] shrugs, as if she's not really that interested."
            "Answer jokingly":
                "I know this one, but I'd rather joke around, so I make a rude answer up instead."
                if "bookworm" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] tuts and looks away, evidently finding my clowning childish."
                elif "dumb" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] laughs out loud, almost spraying me with a mouthful of her drink."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] gives me a token smile, but doesn't seem all that impressed."
    elif r <= 5:
        "The drinks in front of us are getting dangerously close to being finished."
        "[date_girl.name] drains the last of hers and then looks at the empty glass and back at me."
        menu:
            "Offer to buy the next round":
                "I got the first round of drinks, but what the hell - I feel like treating her."
                call expression f"date_pub_random_events_dialogues_7_{hero.gender}" from _call_expression_342
                if "princess" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] practically beams at me, clearly loving that she's being spoiled."
                elif "rebel" in date_girl.traits or "dominant" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me like I'm patronising her, but doesn't object."
                else:
                    "[date_girl.name] nods casually, pointing to her glass to tell me she wants the same again."
            "Tell her it's her round":
                call expression f"date_pub_random_events_dialogues_8_{hero.gender}" from _call_expression_343
                if "princess" in date_girl.traits or "dominant" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] frowns and shakes her head - clearly she'd been expecting me to pick up her tab all night!"
                elif "rebel" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] scoops up the glasses and heads for the bar without pause or hesitation."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] shrugs and gets up, making her way to the bar."
    elif r <= 6:
        "Don't ask me how it comes up in casual conversation, but somehow I mention that I have a head-banger of a day awaiting me at work tomorrow morning."
        "[date_girl.name] glances down at the line of empty glasses already spread out before me and raises her eyebrows."
        menu:
            "Screw work":
                call expression f"date_pub_random_events_dialogues_9_{hero.gender}" from _call_expression_344
                if "rebel" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] gives me a conspiratorial smile and holds up her drink for an impromptu toast."
                elif "workaholic" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shakes her head, as though she's watching the gradual descent of an alcoholic."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] looks surprised at my comment and shakes her head with a smile."
            "I should be reigning it in":
                call expression f"date_pub_random_events_dialogues_10_{hero.gender}" from _call_expression_345
                if "rebel" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] rolls her eyes, clearly finding my comment utterly lame."
                elif "workaholic" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods in approval, a new-found respect for me clear to see in her eyes."
                else:
                    "[date_girl.name] shrugs and shakes her head, as if to say 'whatever'."
    elif r <= 7:
        "I can smell the food the pub's serving, and it's making me ever more hungry with every passing moment."
        "Tossing [date_girl.name] a menu, I suggest that we order something."
        menu:
            "I want junk food":
                call expression f"date_pub_random_events_dialogues_11_{hero.gender}" from _call_expression_346
                if "trashy" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods and smiles at this, as if I just read her mind."
                elif "gourmand" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me in askance, as if I just suggested that we order road-kill in BBQ sauce."
                else:
                    "[date_girl.name] waves her hand to and fro, as if not convinced she wants exactly the same thing as I do."
            "I hope this is all ethically sourced":
                call expression f"date_pub_random_events_dialogues_12_{hero.gender}" from _call_expression_347
                if "trashy" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks confused, like I've suddenly started speaking a foreign language."
                elif "gourmand" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods approvingly, wrinkling her nose as she sees that my concerns about the menu are legitimate."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] smiles at me, her face saying that she thinks I'm being a little too fussy."
    elif r <= 8:
        "We've already made the mistake of sitting too close to the massive TV mounted on one of the pub's walls."
        "And when it erupts into life [date_girl.name] shoots me a glance as we both realise it's about to show a football game."
        menu:
            "Sweet, I love football":
                call expression f"date_pub_random_events_dialogues_13_{hero.gender}" from _call_expression_348
                if "sporty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] has to practically drag her eyes away from the pre-match hype."
                    "But when she finally does, it's to flash me a look of obvious approval."
                elif "geek" in date_girl.traits or "not_sporty" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] glances around the pub, as if she wants to look at anything other than the TV...and me."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] looks a little put out at the intrusion of the TV, but not like she's about to say so."
            "Why is it always bloody football":
                call expression f"date_pub_random_events_dialogues_14_{hero.gender}" from _call_expression_349
                if "not_geek" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] snorts at this and shakes her head, her look of disbelief questioning my manhood."
                elif "geek" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] throws her hands up in the air and nods emphatically, as if I'm the first person ever to agree with her on this matter."
                else:
                    "[date_girl.name] shrugs, as though she thinks my suggestion would be nice, but also that it's not going to happen any time soon."
    elif r <= 9 and hero.is_male:
        "Checking my wallet before I go to the bar to get the next round in, I notice that I don't have any condoms in there."
        "When I get up and walk in the direction of the bathroom and not the bar [date_girl.name] raises her eyebrows, clearly wondering where I'm going."
        menu:
            "Admit to buying condoms":
                call expression f"date_pub_random_events_dialogues_15_{hero.gender}" from _call_expression_350
                if "slutty" in date_girl.traits:
                    $ game.active_date.score += 10
                    "A filthy smile spreads across [date_girl.name]'s face, as she clearly likes the sound of where this is going."
                elif "innocent" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] looks at me with a shocked expression, as if she's surprised such thing would even be on my mind right now."
                else:
                    "[date_girl.name] gives me a wry sideways glance and shakes her head, amused at my apparent confidence as to just how well the date is going."
            "Claim to need the bathroom":
                call expression f"date_pub_random_events_dialogues_16_{hero.gender}" from _call_expression_351
                if "slutty" in date_girl.traits:
                    "[date_girl.name] waves me off as though she couldn't really care less."
                elif "innocent" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods and smiles sweetly, clearly swallowing the excuse hook, line and sinker."
                else:
                    $ game.active_date.score -= 5
                    "[date_girl.name] frowns and shakes her head, laughing at the fact that I've already given more information than she wanted."
    elif r <= 10:
        "I put the drinks down on the table and then fumble my change back into my wallet, but it's only then that I realise I've been short-changed at the bar."
        "[date_girl.name] sees what I'm doing and the expression on her face tells me that she instantly gets what's happened."
        menu:
            "Blow it off":
                call expression f"date_pub_random_events_dialogues_17_{hero.gender}" from _call_expression_352
                if "poor" in date_girl.traits:
                    $ game.active_date.score -= 10
                    "[date_girl.name] shakes her head, as though she doesn't appreciate me being so casual about money."
                else:
                    "[date_girl.name] shrugs indifferently, at my attitude towards my own money."
                    return
            "Go back and rectify the error":
                call expression f"date_pub_random_events_dialogues_18_{hero.gender}" from _call_expression_353
                if "poor" in date_girl.traits:
                    $ game.active_date.score += 10
                    "[date_girl.name] nods and smiles in agreement, clearly impressed at my frugality when it comes to money."
                else:
                    "[date_girl.name] shrugs and nods, not particularly concerned about my penny-pinching habits."
    $ renpy.hide(date_girl.id)
    return

label date_eat_a_burger:
    show expression f"date pub burger {active_girl.id}"
    if renpy.has_label(f"{active_girl.id}_date_eat_a_burger"):
        call expression f"{active_girl.id}_date_eat_a_burger" from _call_expression_141
    else:
        "We eat a burger together."
    hide expression f"date pub burger {active_girl.id}"
    if "gourmand" in active_girl.traits:
        $ game.active_date.score += 5
    $ game.active_date.score += 5
    return

label date_buy_a_round:
    if renpy.has_label(f"{active_girl.id}_date_buy_a_round"):
        call expression f"{active_girl.id}_date_buy_a_round" from _call_expression_142
    else:
        if active_girl.is_visibly_pregnant:
            $ renpy.show(f"{active_girl.id} angry")
            $ active_girl.love -= 10
            active_girl.say "Are you serious?!?"
            active_girl.say "You're gonna buy drinks for everyone but I'll be the one not being able to enjoy it?"
            active_girl.say "You must be joking [hero.name]!"
            $ hero.cancel_activity()
        elif (hero.charm >= 60 - active_girl.love and active_girl.flags.drinks < 2):
            $ renpy.show(f"drink {active_girl.id}")
            "I pay a round of beers to the whole pub."
            $ active_girl.set_flag("drinks", 1, "day", mod="+")
            $ game.active_date.score += 5
            if "rebel" in active_girl.traits:
                $ game.active_date.score += 5
            $ renpy.hide("drink")
        else:
            $ renpy.show(f"{active_girl.id}")
            "I want to pay a round of beers to the whole pub."
            "But [active_girl] doesn't seem to want to drink, so I refrain from doing so."
            $ hero.cancel_activity()
    return

label date_pub_play_pool:
    show expression f"pool {active_girl.id}"
    if renpy.has_label(f"{active_girl.id}_date_pub_play_pool"):
        call expression f"{active_girl.id}_date_pub_play_pool" from _call_expression_143
    else:
        "We play a few games."
    $ bonus = 5
    if "playful" in active_girl.traits:
        $ bonus += 5
    if "not_playful" in active_girl.traits:
        $ bonus += 5
    $ game.active_date.score += bonus
    if hero.charm >= date_girl.sub:
        $ date_girl.sub += 2
    else:
        $ date_girl.sub -= 2
    hide expression f"pool {active_girl.id}"
    return

label date_play_darts:
    show expression f"date pub dart {active_girl.id}"
    if renpy.has_label(f"{active_girl.id}_date_play_darts"):
        call expression f"{active_girl.id}_date_play_darts" from _call_expression_144
    else:
        "We play a few games."
    if hero.fitness >= date_girl.sub:
        $ date_girl.sub += 2
    else:
        $ date_girl.sub -= 2
    $ bonus = 5
    if "playful" in active_girl.traits:
        $ bonus += 5
    if "playful" in active_girl.traits:
        $ bonus += 5
    $ game.active_date.score += bonus
    hide expression f"date pub dart {active_girl.id}"
    return

label date_pub:
    $ renpy.show(active_girl.id)
    "We go to the pub."
    $ renpy.hide(active_girl.id)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
