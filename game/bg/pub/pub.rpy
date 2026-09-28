init python:
    Room(**{
    "name": "pub",
    "exits": ["map", "pubexterior", "pubplay", "pubseat"],
    "display_name": "Pub",
    "hours": (19, 3),
    "conditions": [
        IsHour(19, 3),
        ],
    "music": "music/roa_music/can_you_hear_me.ogg",
    "ambience": "sd/SFX/ambiences/pub.ogg",
    "outfit": "casual",
    "tags": ["pub"],
    })

    Activity(**{
    "name": "eat_a_burger",
    "label": "eat_a_burger",
    "duration": 0,
    "hunger": 7,
    "money_cost": 25,
    "once_day": True,
    "conditions": [
        HeroTarget(
            MinStat("hunger", 0),
            HasRoomTag("pub"),
            ),
        ],
    "display_name": "Eat a burger",
    "icon": "burger",
    })

    Activity(**{
    "name": "drink",
    "label": "drink_beer",
    "duration": 0,
    "fun": 1,
    "money_cost": 25,
    "rooms": "pub",
    "conditions": [
        HeroTarget(
            MinStat("fun", 0),
            HasRoomTag("pub"),
            ),
        ],
    "display_name": "Order a drink",
    "icon": "beer",
    })

    Activity(**{
    "name": "buy_lottery_ticket",
    "money_cost": 10,
    "conditions": [
        HeroTarget(
            HasRoomTag("pub"),
            ),
        ],
    "display_name": "Buy a lottery ticket",
    "icon": "lottery",
    "label": "buy_lottery_ticket",
    })

    Event(**{
    "name": "jeff_in_the_pub",
    "label": "jeff_in_the_pub",
    "priority": 500,
    "conditions": [
        IsDone("work_call_the_accountant"),
        IsNotDone("cassidy_investigation_complete"),
        HeroTarget(
            HasRoomTag("pub"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99),
            ),
        ],
    "do_once": True,
    })

label jeff_in_the_pub:
    #attention: jeff pub
    "Suspended from work means I'm stuck at home brooding over the investigation."
    "The walls are closing in, so I force myself out for a drink."
    "I end up outside the Winchester, walk in, and that's when I spot him — Jeff from accounts."
    "He's one of the few people from work who'd acknowledge me right now."
    "Awkward, nervous type, but maybe that works in my favour."
    "I wave him over and buy him a drink, keeping the conversation light at first."
    mike.say "Hey, Jeff. I never thought I'd see you in here."
    "Jeff" "Ah, yeah, [hero.name]. I suppose I have hidden depths!"
    mike.say "Better hidden than most. So, how about another drink?"
    "Jeff jumps at the offer, clearly thrilled to be noticed."
    "I pay for his drink and steer the conversation where I need it."
    mike.say "So, must be rough for you guys in accounting with all this mess."
    "Jeff" "Yeah, it does suck that they're doing that to you. The embezzlement and all that?"
    "I sigh and look away, playing reluctant."
    mike.say "Yeah... I guess you'd know all about it."
    "Jeff" "Yeah, I'm right in the front lines. Right there whenever this happens!"
    "That phrase stops me cold. 'Whenever this happens.'"
    mike.say "What do you mean by that? Has this kind of thing happened before?"
    "Jeff realizes too late what he's said. The nerves come back instantly."
    "Jeff" "Ah, no, I... that's all confidential. I have to get going."
    "He necks his drink and stands to leave."
    menu:
        "Stop Jeff leaving":
            "Without thinking, I grab his wrist."
            "He looks down at my hand, then back up at me, silently asking for help."
            "A firm squeeze is enough to remind him he's not in a position to yell."
            mike.say "We're not finished here, Jeff."
            "He nods quickly, desperate to comply."
            "Jeff" "Okay, okay. I'll stay. Just don't hurt me, yeah?"
            "I let go and smooth down his sleeve, playing calm."
            mike.say "So, this happens often? With the big bosses ordering people to look the other way?"
            "Jeff nods, eager to spill now that he's been threatened."
            "Jeff" "Yeah, sometimes we get orders from high up. Sometimes we're told to do things that are... well, against the rules. Illegal, really."
            mike.say "And in my case? Who's the big boss?"
            "Jeff" "I'm not sure, but when my boss told me we were investigating you... I heard him talking to Dwayne right before."
            "The name hits like ice water. Dwayne. Of course."
            "I slam my fist on the bar without thinking."
            "Half the pub turns to look. Jeff practically jumps out of his skin."
            mike.say "Dwayne. I should have known."
            "Jeff" "Wait, I never actually said it was him!"
            "But I'm already done listening. So is he, apparently."
            "Jeff scurries away across the pub."
            "My mind is racing. Dwayne's behind this. And I have a timid accountant's word as proof."
            "Not concrete, but it's something. Enough to work with."
            call investigation_points (10) from _call_investigation_points_9
        "Let Jeff go":
            "I think about stopping him, then let it go."
            "I'm in enough trouble without an assault charge."
            "But Jeff did let slip something useful — this isn't the first time."
            "He said 'whenever this happens,' which means there's a pattern."
            "That's a lead worth following up on."
    return

label eat_a_burger:
    show chibi burger
    "Crunch, crunch...\nCrunch..."
    return

label drink_beer:
    show chibi beer
    "Glou, Glou...\nGlou..."
    return

label buy_lottery_ticket:
    show chibi lottery
    "I buy some lottery tickets."

    $ r = randint(1, 30000)
    if hero.is_lucky:
        $ r = min([r, randint(1, 30000)])
    elif hero.is_unlucky:
        $ r = max([r, randint(1, 30000)])
    if r <= 10:
        $ w = 5000 + (randint(1, 5) * 1000)
    elif r <= 50:
        $ w = 2500 + (randint(1, 5) * 500)
    elif r <= 150:
        $ w = 500 + (randint(1, 10) * 200)
    elif r <= 500:
        $ w = 1000 + (randint(1, 5) * 100)
    elif r <= 1000:
        $ w = 500 + (randint(1, 5) * 100)
    elif r <= 1500:
        $ w = 250 + (randint(1, 5) * 50)
    elif r <= 3000:
        $ w = 50 + (randint(1, 5) * 10)
    elif r <= 5000:
        $ w = 10
    elif r <= 10000:
        $ w = 5
    else:
        $ w = 0
    $ hero.money += w
    if w:
        "I won [w]{image=gui/icons/icon_money.png}!"
    else:
        "I lost..."
    return
return