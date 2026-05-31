layeredimage bg date_restaurant:
    always:
        "restaurant"

layeredimage bg restaurant:
    always:
        "restaurant"

layeredimage bg publicbathroom:
    always:
        "publicbathroom"

init -2 python:
    Room(
    **{
        "name": "date_restaurant",
        "exits": ["map"],
        "display_name": "Fancy restaurant",
        "hours": (19, 24),
        "music": "music/roa_music/blue.ogg",
        "conditions": [
            IsHour(19, 23),
            Or(InInventory("fancy_clothes"), InInventory("fancy_dress")),
        ],
        "outfit": "date",
        "tags": ["dateroom"],
    }
)

    Date(
    "restaurant",
    display_name="Fancy restaurant",
    money_cost=100,
    conditions=[ValidRooms("date_restaurant")],
    clothes="date",
    love_gain=2,
)

    Activity(
    **{
        "name": "date_hand_on",
        "duration": 0,
        "icon": "touch",
        "rooms": "date_restaurant",
        "display_name": "Touch [date_girl.possessive_adjective] hand",
        "label": "date_hand_on",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_order_for_her",
        "icon": "order",
        "rooms": "date_restaurant",
        "conditions": [
            ActiveTarget(
                IsFlag("eatenrestaurant", False),
                IsFlag("orderedrestaurant", False),
            ),
        ],
        "display_name": "Order for [date_girl.personal_pronoun]",
        "label": "date_order_for_her",
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_eat_restaurant",
        "icon": "eat",
        "display_name": "Eat",
        "label": "date_eat_restaurant",
        "min_girls": 1,
        "hunger": 10,
        "fun": 2,
        "rooms": "date_restaurant",
        "conditions": [
            HeroTarget(
                MinStat("energy", 0),
                MinStat("hunger", 0),
                MinStat("grooming", 0),
                MinStat("fun", 0),
            ),
            ActiveTarget(
                IsFlag("eatenrestaurant", False)
                ),
        ],
        "once_day": True,
    }
)

    Activity(
    **{
        "name": "date_pay_restaurant",
        "duration": 0,
        "icon": "pay",
        "display_name": "Pay for both of you",
        "label": "date_pay_restaurant",
        "min_girls": 1,
        "money_cost": 100,
        "rooms": "date_restaurant",
        "conditions": [
            HeroTarget(
                MinStat("energy", 0),
                MinStat("hunger", 0),
                MinStat("grooming", 0),
                MinStat("fun", 0),
            ),
            ActiveTarget(
                IsFlag("eatenrestaurant")
                ),
        ],
        "once_day": True,
    }
)

    Event(
    **{
        "name": "date_restaurant_random_events",
        "label": "date_restaurant_random_events",
        "priority": 0,
        "conditions": [
            HeroTarget(OnDate(), IsRoom("date_restaurant")),
        ],
        "chances": 20,
        "do_once": False,
        "once_day": True,
    }
)

label date_restaurant:
    $ renpy.show(date_girl.id)
    "We go to a high class restaurant."
    $ renpy.hide(date_girl.id)
    return

label date_pay_restaurant:
    $ renpy.show("restaurant meal pay " + date_girl.id)
    "I pay for both our meals."
    if date_girl.traits & {"submissive", "dominant", "princess", "poor"}:
        $ game.active_date.score += 5
    $ date_girl.sub += 1
    hide restaurant meal
    return

label date_eat_restaurant:
    $ renpy.show("restaurant meal eat " + date_girl.id)
    $ game.active_date.score += 5
    if hero.charm >= date_girl.love:
        $ game.active_date.score += 5
    "I eat with [date_girl.name]."
    call expression date_girl.get_chat from _call_expression_354
    $ date_girl.flags.eatenrestaurant = TemporaryFlag(True, "day")
    $ date_girl.flags.orderedrestaurant = TemporaryFlag(True, "day")
    hide restaurant meal
    return

label date_order_for_her:
    $ renpy.show("restaurant meal order " + date_girl.id)
    "I order some food for [date_girl.name]."
    if "submissive" not in date_girl.traits:
        $ renpy.show("restaurant meal bored " + date_girl.id)
        date_girl.say "I can order for myself, thank you very much..."
        $ game.active_date.score -= 10
    else:
        $ renpy.show("restaurant meal blush " + date_girl.id)
        call expression f"date_order_for_her_dialogues_1_{hero.gender}" from _call_expression_355
        $ game.active_date.score += 5
    $ date_girl.sub += 1
    $ date_girl.flags.orderedrestaurant = TemporaryFlag(True, "day")
    hide restaurant meal
    return

label date_hand_on:
    $ renpy.show("restaurant meal hold " + date_girl.id)
    if date_girl.gender == "female":
        "I move my hand on top of hers."
    else:
        "I move my hand on top of his."
    if hero.charm < 100 - date_girl.love:
        $ renpy.show("restaurant meal bored " + date_girl.id)
        date_girl.say "What do you think you are doing?"
        $ game.active_date.score -= 10
    else:
        $ renpy.show("restaurant meal happy hold " + date_girl.id)
        if date_girl.gender == "female":
            "[date_girl.name] interlocks her fingers with mine while smiling."
        else:
            "[date_girl.name] interlocks his fingers with mine while smiling."
        $ game.active_date.score += 5
    hide restaurant meal
    return

label date_restaurant_random_events:
    $ random_event = renpy.random.choice(["gazpachosoup", "flirtywaiter", "noisykids", "lostreservation", "bill", "music", "specialboard", "service", "eatingspeed", "ordering"])
    scene bg restaurant
    $ renpy.show(date_girl.id)
    call expression "date_restaurant_" + random_event from _call_expression_356
    return

label date_restaurant_gazpachosoup:
    $ renpy.show("restaurant meal eat " + date_girl.id)
    "I've chosen to order a starter tonight, as the gazpacho soup just sounded too good to miss."
    "[date_girl.name] follows my lead, ordering the soup too."
    "As soon as the waiter delivers it to the table, I pick up my spoon and take a mouthful."
    "But then I wrinkle up my nose, realizing that it's stone cold!"
    menu:
        "Complain that the soup is cold":
            $ renpy.show("restaurant meal -eat bored " + date_girl.id)
            call expression f"date_restaurant_gazpachosoup_dialogues_1_{hero.gender}" from _call_expression_357
            if "bookworm" in date_girl.traits:
                $ renpy.show("restaurant meal eat happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] looks at me in surprise, then covers her mouth to stifle a rush of giggles."
            elif "dumb" in date_girl.traits or "trashy" in date_girl.traits:
                $ renpy.show("restaurant meal eat bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name]'s face curls into an expression of disgust, and she shoves her own bowl aside."
            else:
                "[date_girl.name] shrugs, as if she's not sure what to think."
            "It's only when the waiter comes over and explains that gazpacho soup is served cold that I realize how badly I just screwed up!"
        "Eat the soup without complaint":
            "Of course, gazpacho soup's always served cold, so I just shrug and eat another spoonful."
            if "bookworm" in date_girl.traits:
                $ renpy.show("restaurant meal eat happy " + date_girl.id)
                $ game.active_date.score += 10
                "[date_girl.name] eats her soup without complaint too, smiling the whole time."
            elif "dumb" in date_girl.traits or "trashy" in date_girl.traits:
                $ renpy.show("restaurant meal eat bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] grimaces after her first mouthful, shoving the dish away from her."
                "She looks irate at being served cold soup, and pretty pissed at me for ordering the same!"
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] looks surprised at the soup being cold."
                "But as I don't complain, she keeps her thoughts to herself."
    hide restaurant meal eat
    return

label date_restaurant_flirtywaiter:
    $ renpy.show("restaurant meal waiter " + date_girl.id)
    "Once the waiter's shown us to our table, I notice that he's not really paying me any attention."
    "Instead he's practically gushing over [date_girl.name], laughing at her every word."
    menu:
        "Put up with the waiter":
            "Maybe I should say something to the guy."
            "But what if that makes me look paranoid and jealous?"
            "So I end up just sitting there, smiling weakly."
            if "flirty" in date_girl.traits:
                $ renpy.show("restaurant meal waiter blush " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] practically laps up the attention, totally ignoring me in favor of the waiter."
                "All I can do is keep quiet, feeling like a fool the whole time."
            elif "innocent" in date_girl.traits:
                $ renpy.show("restaurant meal waiter bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] practically squirms with discomfort in her seat the whole time."
                "But what's worse is when she looks at me, almost imploring me to save her from his clutches..."
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] smiles awkwardly at the waiter's attentions, but looks relieved when he finally leaves us alone."
        "Put the waiter in his place":
            "Who in the hell does this guy think he is?!?"
            "Well, he's wrong if he thinks that I'm going to sit back and let him get away with this shit!"
            $ renpy.show("restaurant meal waiter bored " + date_girl.id)
            call expression f"date_restaurant_flirtywaiter_dialogues_1_{hero.gender}" from _call_expression_358
            if "dominant" in date_girl.traits:
                $ renpy.show("restaurant meal waiter happy " + date_girl.id)
                $ game.active_date.score += 10
                "The waiter looks at me in surprise, then apologizes profusely."
                "[date_girl.name] smiles at the invitation, happy to make me the beneficiary of her knowledge on the subject."
            elif "innocent" in date_girl.traits:
                $ renpy.show("restaurant meal waiter bored " + date_girl.id)
                $ game.active_date.score -= 10
                "The waiter looks at me in surprise, then apologizes profusely."
                "[date_girl.name] rewards me with a malevolent glare, as if I were some kind of possessive monster."
            else:
                "[date_girl.name] shrugs and points to a couple of items on the menu, but doesn't really seem that concerned with what I end up ordering."
    hide restaurant meal
    return

label date_restaurant_noisykids:
    $ renpy.show("restaurant meal " + date_girl.id)
    "I didn't notice it when we walked in, but the sound reaches my ears once we sit down at our table."
    "[date_girl.name] hears it too - the unmistakable racket of a whole family out for a meal together."
    $ renpy.show("restaurant meal waiter " + date_girl.id)
    "The waiter shrugs his shoulders, giving us a pained smile that seems to say there's nothing he can do about the matter."
    menu:
        "Complain about the kids":
            $ renpy.show("restaurant meal waiter bored " + date_girl.id)
            call expression f"date_restaurant_noisykids_dialogues_1_{hero.gender}" from _call_expression_359
            if "family" in date_girl.traits or date_girl.is_visibly_pregnant:
                $ renpy.show("restaurant meal waiter bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] looks shocked at my outburst, almost concerned for the poor family I'm ranting about."
            elif "bitchy" in date_girl.traits:
                $ renpy.show("restaurant meal waiter happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] nods approvingly as she shoots venomous glances towards the harassed parents."
            else:
                "[date_girl.name] wears an expression that's sympathetic, but ultimately as helpless as anyone else."
        "Fawn over the kids":
            call expression f"date_restaurant_noisykids_dialogues_2_{hero.gender}" from _call_expression_360
            if "family" in date_girl.traits or date_girl.is_visibly_pregnant:
                $ renpy.show("restaurant meal waiter happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] smiles at me happily, her eyes becoming as wide as saucers, nodding the whole time."
            elif "bitchy" in date_girl.traits:
                $ renpy.show("restaurant meal waiter bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] curls her lip and shakes her head, like I just admitted to being a cannibal or something similarly distasteful."
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] kind of nods her head in an odd fashion, as if to say that I'm entitled to my own opinion on the matter."
    hide restaurant meal
    return

label date_restaurant_lostreservation:
    "As the waiter searches in vain for my name on the list, it becomes obvious that they've lost my reservation."
    "Everyone's apologized, assured me that it's just a hiccup and smiled awkwardly."
    "But we're still no closer to actually getting shown to a table."
    menu:
        "Give the waiter a piece of your mind":
            call expression f"date_restaurant_lostreservation_dialogues_1_{hero.gender}" from _call_expression_361
            if "yandere" in date_girl.traits:
                $ renpy.show(date_girl.id + " happy")
                $ game.active_date.score += 5
                "[date_girl.name] nods approvingly, smiling as she watches the waiter squirm."
            elif "lazy" in date_girl.traits:
                $ renpy.show(date_girl.id + " annoyed")
                $ game.active_date.score -= 5
                "[date_girl.name] rolls her eyes and sighs, as if it's all too much hassle."
            else:
                $ renpy.show(date_girl.id + " annoyed")
                $ game.active_date.score -= 5
                "[date_girl.name] looks irritated and maybe even a little embarrassed."
        "Stand there and wait":
            call expression f"date_restaurant_lostreservation_dialogues_2_{hero.gender}" from _call_expression_362
            if "yandere" in date_girl.traits:
                $ renpy.show(date_girl.id + " angry")
                $ game.active_date.score -= 10
                "[date_girl.name] seethes at the sight of me apologizing, looking like she literally wants to kill someone."
            elif "lazy" in date_girl.traits:
                $ renpy.show(date_girl.id + " annoyed")
                "[date_girl.name] shrugs and snorts derisively, but she nods all the same."
            else:
                $ renpy.show(date_girl.id + " annoyed")
                $ game.active_date.score -= 5
                "[date_girl.name] looks irritated and maybe even a little embarrassed."
    return

label date_restaurant_bill:
    $ renpy.show("restaurant meal askbill " + date_girl.id)
    "The desserts are finally done and all that's left is to have coffee and ask for the bill."
    "But when it arrives, [date_girl.name] looks at me with the obvious question in her eyes."
    "Just how are we going to handle actually paying for the meal?"
    menu:
        "Offer to cover the bill" if hero.money >= 40:
            call expression f"date_restaurant_bill_dialogues_1_{hero.gender}" from _call_expression_363
            if "rebel" in date_girl.traits or "workaholic" in date_girl.traits:
                $ renpy.show("restaurant meal askbill bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] looks at me with her mouth open and shaking her head, clearly offended by the gesture."
            elif "princess" in date_girl.traits or "dominant" in date_girl.traits:
                $ renpy.show("restaurant meal askbill happy " + date_girl.id)
                $ game.active_date.score += 10
                "[date_girl.name] smiles approvingly and nods in agreement."
            else:
                $ game.active_date.score += 5
                "[date_girl.name] shrugs and nods, as if to say that she doesn't expect it, but it's a nice gesture all the same."
            $ hero.money -= 40
        "Suggest they split the bill":
            call expression f"date_restaurant_bill_dialogues_2_{hero.gender}" from _call_expression_364
            if "rebel" in date_girl.traits or "workaholic" in date_girl.traits:
                $ renpy.show("restaurant meal askbill happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] nods in agreement, clearly happy with the idea."
            elif "princess" in date_girl.traits or "dominant" in date_girl.traits:
                $ renpy.show("restaurant meal askbill bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] shakes her head and tuts loudly, apparently unhappy with being asked to contribute."
            else:
                "[date_girl.name] smiles and nods, as if she's fine with the suggestion."
            if hero.money <= 20:
                $ hero.money = 0
            else:
                $ hero.money -= 20
    hide restaurant meal
    return

label date_restaurant_music:
    $ renpy.show("restaurant meal " + date_girl.id)
    "Something's been bugging me the whole time that we've been in the restaurant."
    "And for the longest time I couldn't put my finger on just what it was."
    "Then it hits me - they're playing some godawful background music."
    "But do I mention it and risk spoiling the evening by moaning to [date_girl.name]?"
    menu:
        "Don't mention the music":
            "I figure that [date_girl.name] might not even have noticed how bad it is."
            "So I just smile and do my best to ignore it too."
            if "trashy" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 10
                "I noticed that [date_girl.name] is actually mouthing the lyrics to the awful song."
                "So maybe shitting on it would have been a bad idea after all!"
            elif "music" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] looks like someone's pouring raw sewage into her ears."
                "And from the look on her face, she's clearly surprised that I can even stand to listen to this garbage."
            else:
                "[date_girl.name] seems to be ignoring the music too, and so I go right along with her."
        "Complain about the music":
            $ renpy.show("restaurant meal bored " + date_girl.id)
            call expression f"date_restaurant_music_dialogues_1_{hero.gender}" from _call_expression_365
            if "trashy" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] gasps and shakes her head at my comment."
                "And it's only now that I realize she's been singing along to the tune this whole time."
            elif "music" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] smiles and nods, screwing up her face as if the music is causing her physical pain."
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] shrugs and nods, as though she's not too keen on the music, but doesn't feel as passionate as I do about the subject."
    hide restaurant meal
    return

label date_restaurant_specialboard:
    $ renpy.show("restaurant meal " + date_girl.id)
    "I've eaten here before and I know the menu pretty well."
    "But today the stuff on the specials board just seems to catch my attention."
    "And they sound even better when the waiter's described them to us in minute detail."
    menu:
        "Order something adventurous":
            call expression f"date_restaurant_specialboard_dialogues_1_{hero.gender}" from _call_expression_366
            if "playful" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 10
                "[date_girl.name]'s eyes widen with interest, as if she's eager to see what strange dish I've ordered."
            elif "lazy" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] clucks her tongue and rolls her eyes, as if she's not impressed."
                "She proceeds to order the blandest thing on the menu, like she's underlining the point."
            else:
                $ game.active_date.score += 5
                "[date_girl.name] raises her eyebrows at my choice, while she orders something a little less adventurous."
        "Order something safe":
            call expression f"date_restaurant_specialboard_dialogues_2_{hero.gender}" from _call_expression_367
            if "playful" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] sighs and shakes her head."
                "She then proceeds to order the most intimidating thing on the specials board."
                "And it's as if she's trying to shame me by doing so."
            elif "lazy" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] nods in agreement, and then orders the exact same thing as me."
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] raises her eyebrows at my choice, while she orders something a little more adventurous."
    hide restaurant meal
    return

label date_restaurant_service:
    $ renpy.show("restaurant meal " + date_girl.id)
    "I know they always give you a short while between sitting down and coming to take your order."
    "But it's starting to feel like forever, and no one seems to be coming to serve us."
    "Every member of the waiting staff that passes just looks straight through is like we're not even there."
    menu:
        "Make a scene to get the waiter's attention":
            $ renpy.show("restaurant meal order " + date_girl.id)
            call expression f"date_restaurant_service_dialogues_1_{hero.gender}" from _call_expression_368
            "Sure, I feel like a jerk doing it - but within seconds we have a waiter by the table, apologizing and ready to take our orders."
            "I shrug as I look over at my date, seeking her approval for what I've done."
            if "dominant" in date_girl.traits or "bitchy" in date_girl.traits:
                $ renpy.show("restaurant meal order happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] nods at me, an approving smile already spreading across her face."
            elif "innocent" in date_girl.traits:
                $ renpy.show("restaurant meal order bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] looks down at the floor, her cheeks visibly burning with embarrassment."
            else:
                $ game.active_date.score -= 5
                "[date_girl.name] looks glad that I've shut up, and like she just wants to order her food already."
        "Wait patiently for the waiter's attention":
            call expression f"date_restaurant_service_dialogues_2_{hero.gender}" from _call_expression_369
            if "dominant" in date_girl.traits or "bitchy" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] rolls her eyes, evidently frustrated at my lack of urgency."
            elif "innocent" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] nods hastily, offering a supportive smile."
            else:
                "[date_girl.name] shrugs and keeps on looking desperately at every member of the waiting staff that passes by our table."
    hide restaurant meal
    return

label date_restaurant_eatingspeed:
    $ renpy.show("restaurant meal eat" + date_girl.id)
    "I dig into my food as soon as it arrives, as I haven't eaten for hours and I'm seriously hungry."
    "But it doesn't take me long to notice that [date_girl.name] is watching me closely."
    "I guess she's studying the way that I'm eating, and I shouldn't stop for fear of her realizing I know it..."
    menu:
        "Eat quickly":
            "My hunger means that I pretty much demolish my food in record time."
            "Wiping my mouth with my napkin, I shrug and try to laugh it off."
            call expression f"date_restaurant_eatingspeed_dialogues_1_{hero.gender}" from _call_expression_370
            if "workaholic" in date_girl.traits:
                $ renpy.show("restaurant meal eat happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] sighs and nods her head in approval, showing that she feels the same way."
            elif "lazy" in date_girl.traits:
                $ renpy.show("restaurant meal eat bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] snorts in derision, not understanding my need to rush."
            else:
                "[date_girl.name] shrugs and smiles, as if say that it's a matter of each to their own."
        "Savor your food":
            "I slow down pretty quickly, enjoying the chance to actually taste the food that I'm eating for the first time."
            "This means that I finish my meal after [date_girl.name], who has to wait for me to catch up."
            call expression f"date_restaurant_eatingspeed_dialogues_2_{hero.gender}" from _call_expression_371
            if "workaholic" in date_girl.traits:
                $ renpy.show("restaurant meal eat bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] frowns and sighs, as if she can't understand my need to waste precious time."
            elif "lazy" in date_girl.traits:
                $ renpy.show("restaurant meal eat happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] smiles and nods, looking like she's still enjoying the aftertaste of her own meal."
            else:
                "[date_girl.name] shrugs and smiles, as if say that it's a matter of each to their own."
    hide restaurant meal
    return

label date_restaurant_ordering:
    $ renpy.show("restaurant meal " + date_girl.id)
    "Soon after we're seated at our table, the waiter brings over the menus."
    "I take a quick glance at the dishes on offer and then at [date_girl.name]."
    "But she doesn't look up, as [date_girl.possessive_adjective] attention seems to be focused completely on the menu in [date_girl.possessive_adjective] hand."
    menu:
        "Suggest a choice of dish":
            "I guess [date_girl.subject_pronoun]'s having trouble deciding just what [date_girl.subject_pronoun] wants."
            "So maybe I should step in and offer [date_girl.personal_pronoun] a helping hand?"
            call expression f"date_restaurant_ordering_dialogues_1_{hero.gender}" from _call_expression_372
            if "dominant" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 5
                "[date_girl.name] raises a questioning eyebrow and harrumphs, clearly not impressed at my telling [date_girl.personal_pronoun] what to do."
            elif "submissive" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 10
                "[date_girl.name] nods eagerly, looking relieved to have had me step in and help."
            else:
                $ game.active_date.score += 5
                "[date_girl.name] nods, as though [date_girl.subject_pronoun]'s grateful for the advice, but doesn't leap to order what I suggested all the same."
        "Ask [date_girl.personal_pronoun] to suggest a dish":
            "I guess [date_girl.personal_pronoun] interest in the menu must mean that [date_girl.subject_pronoun] knows what [date_girl.subject_pronoun] wants and is hunting it out."
            "And if that's so, then I should probably be asking [date_girl.personal_pronoun] to advise me too!"
            call expression f"date_restaurant_ordering_dialogues_2_{hero.gender}" from _call_expression_373
            if "dominant" in date_girl.traits:
                $ renpy.show("restaurant meal happy " + date_girl.id)
                $ game.active_date.score += 5
                "[date_girl.name] smiles at the invitation, happy to make me the beneficiary of [date_girl.possessive_adjective] knowledge on the subject."
            elif "submissive" in date_girl.traits:
                $ renpy.show("restaurant meal bored " + date_girl.id)
                $ game.active_date.score -= 10
                "[date_girl.name] almost turns pale at the suggestion, shaking [date_girl.possessive_adjective] head and hiding behind [date_girl.possessive_adjective] menu."
            else:
                "[date_girl.name] shrugs and points to a couple of items on the menu, but doesn't really seem that concerned with what I end up ordering."
    hide restaurant meal
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
