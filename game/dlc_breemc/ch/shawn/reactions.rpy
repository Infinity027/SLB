label shawn_ice_cream_reaction_female:
    bree.say "You know what, Shawn..."
    bree.say "I think it's about time for an ice-cream!"
    shawn.say "Erm..."
    shawn.say "Okay, [hero.name] - if that's what you want."
    "I hurry over to the ice-cream stand with Shawn following on behind."
    "And I make a point of ignoring his less than enthusiastic response as I do so."
    "He mutters and mumbles his order at the person working the stand."
    "And when he gets his ice-cream, I see it's a pretty boring one too."
    "But his eyes go wide when he sees me being handed my own choice."
    "Because it's a riot of colour, toppings and sauces!"
    shawn.say "Erm..."
    shawn.say "Wow, [hero.name]..."
    "I stop mid-lick to smile at Shawn."
    bree.say "What's the matter, Shawn?"
    bree.say "See something that you like?"
    "He nods in silence, still staring at my ice-cream."
    bree.say "You want a lick?"
    "Shawn nods again, and I hold out my ice-cream."
    "I watch as he takes a lick and his face lights up."
    shawn.say "That's...really good, [hero.name]!"
    bree.say "Oh, Shawn - you need to relax a little."
    bree.say "You know, have a some fun?"
    return

label shawn_ask_phone_female:
    bree.say "Could I get your number, Shawn?"
    bree.say "I just realised that I don't have it."
    bree.say "And I might, like...well, want to call you or something!"
    if hero.charm >= 20 - shawn.love:
        $ hero.smartphone_contacts.append("shawn")
        shawn.say "Of course you can have it, [hero.name]!"
        shawn.say "Here you go..."
        shawn.say "And don't worry, you can call me anytime you like - day or night!"
    else:
        $ shawn.love -= 1
        $ shawn.sub -= 1
        shawn.say "Nah..."
        shawn.say "I don't think so, [hero.name]."
        shawn.say "I don't just give my number out to people at random."
    return

label shawn_ask_birthday_female:
    bree.say "Shawn..."
    shawn.say "Yeah, [hero.name]?"
    bree.say "When is your birthday?"
    bree.say "I was just wondering about it."
    if hero.charm >= 40 - shawn.love:
        $ shawn.flags.birthdayknown = True
        shawn.say "Oh, right..."
        shawn.say "It's no big secret, [hero.name]."
        shawn.say "It's on Spring 24."
    else:
        shawn.say "Why do you want to know that, [hero.name]?"
        shawn.say "Wait a minute, what's [mike.name] been telling you?"
        shawn.say "I'm keeping my birthday under wraps until I know what's going on here!"
        $ shawn.sub -= 1
        $ shawn.love -= 1
    return

label shawn_offer_a_drink_female:
    bree.say "Looks like you're ready for another pint, Shawn."
    bree.say "Good timing, as I was just going to the bar!"
    bree.say "You want me to grab one for you?"
    if (hero.charm >= 60 - shawn.love and shawn.flags.drinks < 2) or date_girl == shawn:
        shawn.say "You were?"
        shawn.say "Okay, [hero.name], I'll have the same again."
        shawn.say "And thanks for being so thoughtful."
        show drink shawn
        if shawn.love <= 25:
            $ shawn.love += 1
        elif date_girl == shawn and game.active_date:
            $ game.active_date.score += 5
        call expression shawn.get_chat from _call_expression_401
        hide drink shawn
        $ shawn.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        shawn.say "No thanks, [hero.name]."
        shawn.say "I like to pace myself, you know?"
        shawn.say "I'll get one when I'm ready for it."
        $ hero.cancel_activity()
        hide shawn
    return

label shawn_slap_ass_intro_female:
    "As Shawn walks past me, I suddenly have a crazy thought."
    "I wonder if anyone's ever slapped him on the ass?"
    "And if they have, how did he react?"
    "The problem is that I now I can't get the idea out of my head."
    "So much so that when he comes back, I decide to act on impulse."
    return

label shawn_slap_ass_happy_female:
    shawn.say "Ouch!"
    shawn.say "Hey, [hero.name]!"
    shawn.say "Did you just slap me on the arse?!?"
    bree.say "Erm..."
    bree.say "Yeah, Shawn..."
    bree.say "Sorry, but I couldn't resist!"
    shawn.say "Well, okay, [hero.name]..."
    shawn.say "I'm only cool with it because YOU did it."
    shawn.say "But don't make a habit out of it, okay?"
    return

label shawn_slap_ass_angry_female:
    shawn.say "Ouch!"
    shawn.say "Hey, [hero.name]!"
    shawn.say "Did you just slap me on the arse?!?"
    bree.say "Erm..."
    bree.say "Yeah, Shawn..."
    bree.say "Sorry, but I couldn't resist!"
    shawn.say "That isn't cool, [hero.name]!"
    shawn.say "This is the twenty-first century, yeah?"
    shawn.say "Just because it's a girl doing it to a guy doesn't make it okay."
    return

label shawn_breakup_female:
    bree.say "Urgh..."
    bree.say "You're going to hate me for this, Shawn..."
    bree.say "But I..."
    "Shawn's face suddenly becomes the definition of panic."
    shawn.say "Oh god, no!"
    shawn.say "You're breaking up with me, aren't you?"
    bree.say "Erm..."
    bree.say "How did you know?"
    shawn.say "Do you know how many times a girl's done this to me, [hero.name]?"
    shawn.say "I've heard them all!"
    shawn.say "We need time apart to grow!"
    shawn.say "It's not you, it's me!"
    shawn.say "Can we still be friends?"
    shawn.say "I've been dumped so many time I can sense it before you can say it!"
    shawn.say "I must have been dumped like a thousand time!"
    bree.say "Oh...well..."
    bree.say "This is a little awkward..."
    bree.say "Because that's exactly what's happening right now!"
    shawn.say "AAARGH!"
    shawn.say "One thousand and one times!"
    return

label shawn_go_steady_intro_female:
    bree.say "I had a lot of fun on our last date, Shawn."
    shawn.say "Me too, [hero.name] - it was a blast!"
    bree.say "Actually, I had a lot of fun on ALL the dates we've had."
    shawn.say "I can't argue with that, [hero.name]."
    shawn.say "I think we're pretty good together!"
    bree.say "Well..."
    bree.say "Maybe we should make it a more permanent arrangement?"
    shawn.say "You mean, like go steady?"
    bree.say "Exactly that, Shawn!"
    return

label shawn_go_steady_yes_female:
    shawn.say "You're right, [hero.name]."
    shawn.say "We should totally go steady."
    shawn.say "Starting right now!"
    return

label shawn_go_steady_no_female:
    shawn.say "Ah..."
    shawn.say "I don't think so, [hero.name]."
    shawn.say "I think we've been having a good time BECAUSE we've kept it casual."
    shawn.say "Going steady would just ruin that."
    return

label shawn_pet_intro_female:
    "I never noticed how short Shawn is before now."
    "I mean, he's not like super small or anything."
    "But I think he's shorter than [mike.name] and the other guys I know."
    "So much so that I can almost touch the top of his head as he walks by."
    "I'm testing out this theory a moment later."
    "But then my hand makes contact with his spiked hair!"
    shawn.say "Hey, [hero.name]!"
    shawn.say "Did you just pat me on the head?!?"
    bree.say "Erm..."
    bree.say "Yeah, Shawn..."
    bree.say "Sorry, but I couldn't resist!"
    return

label shawn_pet_happy_female:
    shawn.say "Well, okay, [hero.name]..."
    shawn.say "I'm only cool with it because YOU did it."
    shawn.say "But don't make a habit out of it, okay?"
    return

label shawn_pet_annoyed_female:
    shawn.say "That isn't cool, [hero.name]!"
    shawn.say "This is the twenty-first century, yeah?"
    shawn.say "It's not okay to make fun of someone's height."
    return

label shawn_massage_intro_female:
    shawn.say "Ooh..."
    shawn.say "Ouch..."
    bree.say "Oh, Shawn..."
    bree.say "That looks really painful!"
    "Shawn nods, but then regrets it as his muscles twinge again."
    shawn.say "Urgh..."
    shawn.say "I pulled a muscle in the stock-room the other day."
    shawn.say "And it's been killing me ever since!"
    bree.say "You want me to look at it?"
    bree.say "Maybe give you a massage?"
    return

label shawn_massage_accept_female:
    shawn.say "Would you do that for me, [hero.name]?"
    shawn.say "I'd be really grateful."
    shawn.say "Anything that'd relieve the pain!"
    return

label shawn_massage_refuse_female:
    shawn.say "That sounds really tempting, [hero.name]."
    shawn.say "But I want to have a professional take a look."
    shawn.say "If I can't lift stuff, then I can't do my job!"
    return

label shawn_piercing_nipples_reaction_female:
    "I notice that Shawn's fidgeting a more than usual today."
    "It's like something's itching and he can't scratch it."
    "So I lean in and try to find out what the problem is."
    bree.say "What's the matter, Shawn?"
    shawn.say "It's..."
    shawn.say "It's my nipples, [hero.name]!"
    bree.say "Your nipples?!?"
    shawn.say "Yes, my nipples - I had them pierced!"
    bree.say "Whoa, Shawn..."
    bree.say "That is SO hot!"
    "Shawn's mood seems to improve as he hears the approval in my voice."
    "She stops fidgeting and smiles, as if it's not bothering him anymore."
    return

label shawn_piercing_navel_reaction_female:
    "I notice that Shawn's fidgeting a more than usual today."
    "It's like something's itching and he can't scratch it."
    "So I lean in and try to find out what the problem is."
    bree.say "What's the matter, Shawn?"
    shawn.say "It's..."
    shawn.say "It's my navel, [hero.name]!"
    bree.say "Your navel?!?"
    shawn.say "Yes, my navel - I had it pierced!"
    bree.say "Whoa, Shawn..."
    bree.say "That is SO hot!"
    "Shawn's mood seems to improve as he hears the approval in my voice."
    "She stops fidgeting and smiles, as if it's not bothering him anymore."
    return

label shawn_piercing_dick_reaction_female:
    "I notice that Shawn's fidgeting a more than usual today."
    "It's like something's itching and he can't scratch it."
    "So I lean in and try to find out what the problem is."
    bree.say "What's the matter, Shawn?"
    shawn.say "It's..."
    shawn.say "It's my dick, [hero.name]!"
    bree.say "Your dick?!?"
    shawn.say "Yes, my dick - I had it pierced!"
    bree.say "Whoa, Shawn..."
    bree.say "That is SO hot!"
    "Shawn's mood seems to improve as he hears the approval in my voice."
    "She stops fidgeting and smiles, as if it's not bothering him anymore."
    return

label shawn_piercing_tongue_reaction_female:
    "I notice that Shawn's fidgeting a more than usual today."
    "It's like something's itching and he can't scratch it."
    "So I lean in and try to find out what the problem is."
    bree.say "What's the matter, Shawn?"
    shawn.say "It's..."
    shawn.say "It's my tongue, [hero.name]!"
    bree.say "Your tongue?!?"
    shawn.say "Yes, my tongue - I had it pierced, look!"
    "Shawn sticks out his tongue to prove he's telling the truth."
    bree.say "Whoa, Shawn..."
    bree.say "That is SO hot!"
    "Shawn's mood seems to improve as he hears the approval in my voice."
    "She stops fidgeting and smiles, as if it's not bothering him anymore."
    return

label shawn_movie_liked_reaction_female:
    bree.say "That was some movie, huh, Shawn?"
    bree.say "I loved every moment of it - start to finish!"
    bree.say "Definitely the best one I've seen this year!"
    "Shawn nods in agreement, beaming at my loving the movie."
    shawn.say "It was amazing, [hero.name] - totally amazing!"
    shawn.say "And I love that you're into it too."
    shawn.say "Most people can't appreciate a film like that."
    return

label shawn_movie_indifferent_reaction_female:
    bree.say "That was some movie, huh, Shawn?"
    bree.say "I loved every moment of it - start to finish!"
    bree.say "Definitely the best one I've seen this year!"
    "Shawn makes a huffing sound and shakes his head."
    shawn.say "Urgh..."
    shawn.say "I guess it was okay, [hero.name]."
    shawn.say "But it was a bit derivative and predictable..."
    return

label shawn_movie_disliked_reaction_female:
    bree.say "That was some movie, huh, Shawn?"
    bree.say "I loved every moment of it - start to finish!"
    bree.say "Definitely the best one I've seen this year!"
    "Shawn looks at me in utter horror, shaking his head."
    shawn.say "What are you talking about, [hero.name]?"
    shawn.say "That was the worst piece of garbage I ever saw!"
    shawn.say "I mean, were we even watching the same film?!?"
    return


label shawn_belly_interaction_female:
    $ shawn.set_flag("interact", 1, 1, "+")
    show shawn at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call shawn_belly_kiss_female from _call_shawn_belly_kiss_female_1
        "Caress my belly":
            call shawn_belly_caress_female from _call_shawn_belly_caress_female_1
        "Listen to the baby":
            call shawn_belly_listen_female from _call_shawn_belly_listen_female_1
        "Never mind":
            pass
    return

label shawn_belly_caress_female:
    show shawn normal at center, zoomAt(1.5, (640, 1040))
    "I can see the way that Shawn's looking at me right now."
    "And it's a look that I've gotten very used to as a pregnant woman."
    "It's the age old 'I want to touch your bump, but I don't want to seem like a weirdo' look."
    "I guess I should have known that Shawn would be that kind of guy."
    "The kind that would be awkward about that type of thing."
    "He's doing that thing where they stare at you really hard as soon as they think you're not looking."
    "Then the moment that you actually turn in their direction, their head snaps away like they're neck's going to snap!"
    "So I've found that the best thing in those situations is just to call their bluff."
    bree.say "Shawn..."
    bree.say "You keep looking at my belly."
    show shawn surprised at center, zoomAt(1.5, (640, 1040))
    shawn.say "What was that, [hero.name]?"
    shawn.say "Me, looking at your belly?"
    shawn.say "No way!"
    show shawn stuned
    "I can't help chuckling and shaking my head at Shawn's denial."
    "Because it's probably the least convincing thing I've ever heard."
    bree.say "It's totally okay, you know?"
    bree.say "Almost everyone's had a feel of it by now."
    bree.say "And I'd hate for you to get left out."
    show shawn normal
    "Shawn can't help looking down at my belly as I tell him all of this."
    "And more than once he looks like he's actually beginning to reach out for it."
    "But every time he stops himself before he does so, almost flinching backwards."
    show shawn talkative at center, zoomAt(1.5, (640, 1040))
    shawn.say "I..."
    shawn.say "Ooh..."
    shawn.say "I don't know..."
    show shawn normal
    "I know Shawn pretty well by now."
    "And in a situation like this, he could be days making up his mind."
    "So it looks like I'm going to have to step in again to get things moving."
    "Which in this case involves lifting up my top and waiting for the right moment."
    "And when it comes, I take a step forwards, which places my belly against Shawn's hands."
    show shawn embarrassed at center, zoomAt(1.5, (640, 1040))
    shawn.say "Oh..."
    shawn.say "[hero.name]..."
    shawn.say "I'm sorry...I didn't mean to..."
    show shawn surprised at center, zoomAt(1.5, (640, 1040))
    shawn.say "Oh wow...that is quite nice!"
    show shawn smile
    "I watch with relief as Shawn's embarrassment turns into fascination."
    "And after that it doesn't take him long to forget all about his worries."
    "From that point on he only seems to be interested in caressing my belly."
    "Which is something I'm more than happy to sit back and allow him to do."
    $ shawn.love += 2
    return

label shawn_belly_kiss_female:
    show shawn normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Shawn..."
    bree.say "Would you do something for me?"
    "As soon as he hears the question, Shawn is right there in front of me."
    "He looks so attentive it's almost funny, like he's totally eager to please."
    show shawn happy
    shawn.say "Yeah, [hero.name]..."
    shawn.say "Whatever you need!"
    shawn.say "You just say it, and I'll do the best I can to make it happen."
    show shawn smile
    "I nod and smile, getting ready to make my pitch."
    bree.say "Okay, Shawn..."
    bree.say "The thing is that everyone's been wanting to touch my bump."
    bree.say "You know, to feel the baby move and all that?"
    "Shawn nods."
    show shawn complain
    shawn.say "I bet that's a pain, [hero.name]!"
    shawn.say "You must be crazy tired of it by now."
    show shawn sadsmile
    "I'm still smiling as I answer Shawn."
    "But I'm shaking my head, rather than nodding."
    bree.say "Oh no, I don't mind it at all."
    bree.say "In fact, I was hoping that someone might go a little further?"
    "I watch as Shawn swallows nervously."
    "He's obviously waiting to hear just what I have in mind."
    bree.say "What I really wanted was for someone to kiss it."
    show shawn surprised
    shawn.say "To...to kiss it?"
    show shawn stuned
    bree.say "Yeah, Shawn - that's what I said."
    bree.say "So what do you think?"
    bree.say "Are you up for it?"
    show shawn surprised
    "Suddenly Shawn looks shocked, like he wasn't expecting me to ask it of him."
    "But then I see a change come over him, almost like he's mentally stepping up to the challenge."
    show shawn happy
    shawn.say "Of course I will, [hero.name]..."
    shawn.say "You just bring it on!"
    show shawn normal
    "I find myself chuckling at Shawn's sudden surge of bravado."
    "But luckily he doesn't seem to notice as he's already kneeling down."
    show shawn at center, traveling(2.5, 0.3, (640, 1940))
    "And as soon as I have my top lifted up, he leans forwards."
    "Then he places his lips against my stomach, and there's no looking back."
    "Where before he was all nerves, now Shawn's firmly in the driving seat."
    "I don't think there's a single spot of skin on my whole belly that he misses."
    "And once he's done I can feel a warm glow settling over me."
    "One that I think is going to last for a good long time to come."
    $ shawn.love += 3
    return

label shawn_belly_listen_female:
    show shawn normal at center, zoomAt(1.25, (640, 880))
    bree.say "Shawn..."
    bree.say "Would you come over here and do me a favour?"
    show shawn normal at center, traveling(1.5, 0.3, (640, 1040))
    "Shawn nods as he hurries over towards me, eager to help out."
    show shawn talkative
    shawn.say "Of course, [hero.name]..."
    shawn.say "I'd do anything for you!"
    show shawn normal
    "I can't help smiling as I feel a little safer just for hearing that."
    bree.say "It's no big deal, Shawn..."
    bree.say "I just wondered if you'd mind listening to the baby?"
    "Shawn frowns and shakes his head."
    show shawn happy
    shawn.say "Wouldn't we need an ultrasound scanner for that, [hero.name]?"
    shawn.say "You know, the thing they have at the hospital?"
    show shawn normal
    bree.say "I'm not worried about the baby, Shawn."
    bree.say "I just want to see what you can hear."
    bree.say "I'm curious, that's all."
    "Shawn shrugs at this."
    show shawn talkative
    shawn.say "Huh..."
    shawn.say "Well, I guess it couldn't hurt."
    shawn.say "Okay, I'll give it a try."
    show shawn normal
    "I nod happily as Shawn agrees to do as I ask."
    "And then I pull up the hem of my top, revealing the curve of my belly."
    show shawn at center, traveling(2.5, 0.3, (640, 1940))
    "Shawn nods as he gets down on one knee, already turning his head to the side."
    "I can see that he's trying to be as gentle as he can the whole time."
    "And not for the first time I feel a sense of reassurance on account of this."
    show shawn talkative
    shawn.say "Erm..."
    shawn.say "Okay, [hero.name]..."
    shawn.say "Here goes nothing!"
    show shawn normal
    "I nod and watch with genuine interest as Shawn moves here and there."
    "At the same time I can vaguely feel the sensation of the baby moving inside of me."
    "And pretty soon their movements seems to become closer in alignment."
    bree.say "So..."
    bree.say "Can you hear anything down there?"
    bree.say "Anything at all?"
    "Shawn waves his arm in the air."
    "And I guess that means he wants me to keep the noise down."
    "But all the same I still can't help asking more questions."
    bree.say "Is that a yes?"
    show shawn talkative
    shawn.say "It's a maybe!"
    shawn.say "I mean, I can hear something in there."
    shawn.say "And I guess that's got to be the baby, right?"
    shawn.say "Like, there shouldn't be anything else that big in there!"
    show shawn normal
    "I'm nodding eagerly as Shawn keeps telling me what he thinks he can hear."
    "All the time he's moving here and there, following the baby as it moves."
    "And I don't exactly know what we're achieving with all of this."
    "But it definitely feels like we're bonding on a meaningful level right now."
    $ shawn.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
