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
    "I need to get my mind off of the investigation and the fact that I know I've been framed."
    "Since I've been suspended from work, I'm stuck in the house most of the time."
    "And that means I'm just going over the same old stuff in my head, driving myself mad."
    "At first the last thing I wanted to do was actually go out and face the world at large."
    "But I'm starting to feel like I'm losing my mind, and so I force myself out of the door."
    "I have no idea where I'm headed, until I look up and see that I'm outside the Winchester."
    "Looking around, I shrug my shoulders and decide to head in for a drink."
    "I guess drowning my sorrows might be a temporary solution."
    "Inside the pub isn't too crowded, so I don't have to fight my way to the bar."
    "But as I get the barman's attention and order a drink, I also spot a familiar face."
    "Not many of the guys from work drink in here, as it's pretty much in the suburbs."
    "But that's definitely Jeff from accounts over there."
    "And that's the moment the idea pops into my head."
    "I've spoken to Jeff a couple of times while I've held my current position."
    "Not enough to call him a friend, but more than enough to justify saying hello."
    "He's sure to know something about the shit the company's got on me."
    "Maybe I can pump him for some insider info?"
    "I can buy him a drink in the hopes of loosening his tongue too!"
    "Getting Jeff's attention, I wave for him to join me at the bar."
    "He seems happy to see me and eager to lap up the attention I'm giving him."
    "I know it sounds mean to say this, but he's pretty much a stereotypical accountant."
    "Whenever I've seen Jeff and interacted with him, he's been awkward and nervous."
    "So no wonder he's keen to hurry over now, even knowing that I'm on suspension."
    "Anyone else from work would treat me like a pariah right now!"
    mike.say "Hey, Jeff!"
    mike.say "I never thought I'd see you in here!"
    "Jeff" "Ah, yeah, [hero.name]."
    "Jeff" "Well..."
    "Jeff" "I suppose I have hidden depths!"
    "I make a point of laughing at what Jeff just said."
    "Although I admit I have no idea if it was supposed to be a joke or not."
    mike.say "Better hidden than most!"
    "Jeff" "Huh..."
    "Jeff" "What does that mean?"
    mike.say "Nothing, nothing at all..."
    mike.say "Hey, how about I get you another drink?"
    "At the mention of a free drink, Jeff changes his tune."
    "Any hint that he detected my last insult disappears without a trace."
    "Jeff" "Aw, thanks, [hero.name]!"
    "Jeff" "I'll have another one of these."
    "I nod to the barman and pay for Jeff's next drink."
    "The whole time I'm thinking of the best way to bring up the charges against me."
    "I need to mention them casually, to come at it from another angle."
    "But then Jeff just opens his mouth and blurts it out."
    "Jeff" "Sucks that they're doing that to you, [hero.name]."
    "Jeff" "You know...the embezzlement and all that?"
    "I let out a long sigh and shake my head."
    "I'm trying my best to look like I don't really want to talk about it."
    mike.say "Oh yeah, that..."
    mike.say "I guess you'd know all about it, huh?"
    "Jeff nods his head, doing his best to look philosophical."
    "I can tell that he's loving the chance to talk about this."
    "When else does an accountant get to hold court?"
    "Jeff" "Yeah, I'm right in the front lines."
    "Jeff" "Right there whenever this happens!"
    "I blink and then shake my head."
    "Did he just say what I think he did?"
    mike.say "What do you mean by that, Jeff?"
    mike.say "Has this kind of thing happened before?"
    mike.say "Does it happen often?"
    "Suddenly the reality dawns on Jeff that he's said too much."
    "Now he's not acting anymore, and the nerves are showing!"
    "Jeff" "Ah...no...I..."
    "Jeff" "That's all confidential!"
    "Jeff" "I have to get going..."
    "And with that, he necks his drink."
    "Then he turns to leave..."
    menu:
        "Stop Jeff leaving":
            "Before I can stop myself, my hand shoots out."
            "I grab Jeff by the wrist, stopping him from leaving."
            "He looks down at my hand and then up at me."
            "I can see that he's thinking about yelling for help."
            "But a firm squeeze of my fingers is all it takes to stop that."
            mike.say "Where are you going, Jeff?"
            mike.say "We're not finished with our little chat!"
            "I feel like a school bully right now, ashamed of resorting to brute force."
            "But I can see that it's working, cowing Jeff into submission."
            "Jeff" "O...okay...okay..."
            "Jeff" "I'll stay, [hero.name]."
            "Jeff" "Just don't hurt me, yeah?"
            "I let go of Jeff's wrist with a smile."
            "I even smooth down his sleeve for added effect."
            mike.say "So, where were we?"
            mike.say "Oh yeah, I remember!"
            mike.say "You were about to tell me if this kind of thing happens often, right?"
            "Jeff nods, eager to spill his guts now he's been threatened."
            "Jeff" "Yeah, yeah..."
            "Jeff" "Well...nobody says it out loud."
            "Jeff" "But sometimes we get orders from...from high up."
            "Jeff" "And they mean we need to look the other way."
            "I lean in closer, looking Jeff straight in the eye."
            mike.say "I'm hearing a lot of vague shit, Jeff."
            mike.say "You need to be more specific."
            "Jeff" "Alright, [hero.name]..."
            "Jeff" "Sometimes we get told to do things that we know are against the rules."
            "Jeff" "The big bosses tell us to do something illegal, and there's no choice!"
            mike.say "And in my case, Jeff?"
            mike.say "Who's the big boss we're talking about?"
            "Jeff" "I don't know for sure."
            "Jeff" "But when my boss told me we were investigating you..."
            "Jeff" "Well...I might have heard him talking to Dwayne a minute before!"
            "I can't contain my emotions at this revelation."
            "And so I slam my fist down on the bar."
            "Half the people in the pub look in my direction."
            "And Jeff practically soils himself in shock."
            mike.say "Dwayne..."
            mike.say "I should have known it was him!"
            "Jeff" "H...hey..."
            "Jeff" "Wait a minute..."
            "Jeff" "I never said it was him!"
            "At the sound of Jeff's voice, I round on him in surprise."
            mike.say "Huh?!?"
            mike.say "Are you still here?"
            "Jeff" "Not for much longer!"
            "And with that, he scurries away across the pub."
            "I hardly even notice that Jeff's gone."
            "My mind is already racing with the knowledge that Dwayne's involved."
            "Seems he's not above breaking the rules to get what he wants."
            "But all I have right now is the word of one timid accountant."
            "What I need is concrete evidence to back it up."
            "Or at least something I can use to blackmail Dwayne into dropping the investigation!"
            call investigation_points (10) from _call_investigation_points_9
        "Let Jeff go":
            "I think about trying to stop him."
            "But then I drop the idea and just watch him go."
            "I'm in enough trouble already."
            "The last thing I need is an assault charge on top of all that!"
            "But maybe this wasn't a complete loss."
            "Jeff might not have spilled his guts."
            "Yet he did let slip it's not an isolated incident."
            "Which is weird, because I never heard of it happening before."
            "That could be a lead worth following up..."
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
    if r <= 1:
        $ w = 5000 + (randint(1, 5) * 1000)
    elif r <= 25:
        $ w = 2500 + (randint(1, 5) * 500)
    elif r <= 50:
        $ w = 500 + (randint(1, 10) * 200)
    elif r <= 100:
        $ w = 1000 + (randint(1, 5) * 100)
    elif r <= 300:
        $ w = 500 + (randint(1, 5) * 100)
    elif r <= 600:
        $ w = 250 + (randint(1, 5) * 50)
    elif r <= 1200:
        $ w = 50 + (randint(1, 5) * 10)
    elif r <= 2500:
        $ w = 10
    elif r <= 5000:
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
