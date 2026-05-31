label danny_abortion_reaction_female:
    danny.say "Hmm..."
    danny.say "Now what do we have here?"
    "I look up to see Danny studying me with apparent interest."
    "He's rubbing his chin and frowning, like he's in deep thought too."
    "Which is pretty unusual for a guy like him."
    "And pretty unnerving for me as the centre of his attention!"
    bree.say "Erm..."
    bree.say "Danny?"
    danny.say "Huh?"
    danny.say "Yeah, [hero.name] - what is it?"
    bree.say "Why are you looking at me like that?"
    "Danny seems to snap out of it then, coming back to reality."
    "And what's even stranger is that he looks a little embarrassed."
    "Something very unusual for him."
    danny.say "I...I just noticed something, [hero.name]."
    danny.say "You don't look pregnant anymore."
    danny.say "Did you get rid of it?"
    bree.say "If by 'it' you mean the foetus, then yeah."
    bree.say "I had a termination."
    if (danny.flags.know_is_father and danny.love >= 150) or danny.love <= 150:
        "As the realisation dawns on Danny, his face darkens."
        "And the change is so dramatic that I can't help taking a step backwards."
        danny.say "WHAT?!?"
        danny.say "You mean after all that crap we went through..."
        danny.say "You just went and got rid of it without telling me?!?"
        "I'm shaking my head, still surprised by Danny's reaction."
        bree.say "I...I thought you'd be pleased, Danny!"
        bree.say "I thought the last thing you'd want was to be a father!"
        "Danny's eyes narrow until they're almost slits in his face."
        "And he points an accusatory finger in mine."
        danny.say "You don't think for me, [hero.name]!"
        danny.say "And this isn't on me either!"
        danny.say "You did all of this on your own."
        "I reach out for Danny in desperation."
        "But he slaps my hand away and turns on his heel."
        "And I daren't follow him for fear of what else he might do."
    else:
        "As the realisation dawns on Danny, he lets out a sigh of relief."
        "Then he shakes his head and whistles ruefully."
        danny.say "Phew..."
        danny.say "I gotta say, [hero.name]..."
        danny.say "That's a whole fucking lot of weight off my mind!"
        "I nod nervously, still worried he might lose his temper."
        "But Danny shows no signs of flipping, as he nods his head."
        danny.say "I mean..."
        danny.say "It sucks you had to do that, [hero.name]..."
        bree.say "Yeah, Danny..."
        bree.say "But I think we both know it was the right thing."
        "Danny nods again, looking unusually sensitive."
        "Is it possible that this thing's really gotten to him?"
        "That he's deeper than he seems?"
        "Maybe, but that's something to think about later."
        "Right now I need to focus on the stuff right under my nose."
    return


label danny_belly_interaction_female:
    $ danny.set_flag("interact", 1, 1, "+")
    show danny at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call danny_belly_kiss_female from _call_danny_belly_kiss_female_1
        "Caress my belly":
            call danny_belly_caress_female from _call_danny_belly_caress_female_1
        "Listen to the baby":
            call danny_belly_listen_female from _call_danny_belly_listen_female_1
        "Never mind":
            pass
    return

label danny_belly_caress_female:
    show danny smile at center, zoomAt(1.5, (640, 1040))
    "I keep feeling really self-conscious when I catch Danny staring at my belly."
    "And what makes it worse is the fact that he's really shameless about it too."
    "Like, most guys will stare when they think that they can get away with it."
    "But when you catch them in the act, they at least have the class to look a little guilty."
    "All that Danny does is look me right in the eye, whilst wearing that pirate's grin of his!"
    "Hell, sometimes he even goes as far as to throw in a lascivious wink too."
    "But this time I feel so self-conscious as he leers in my direction that I can't take it."
    "So I round on Danny, and give him a piece of my mind."
    bree.say "Okay, Danny, cut it out."
    bree.say "I know that I got fat, okay?"
    bree.say "But that's what happens when you're pregnant."
    bree.say "And that's something you had a hand in too, remember?!?"
    "I was expecting Danny to change his tune, but I'm instantly disappointed on that one."
    "Because all that he does in response is throw his head back and bellow with laughter."
    show danny joke at startle
    danny.say "HA!"
    danny.say "You're still as fierce as ever, [hero.name]..."
    danny.say "I love it!"
    danny.say "And I love you too!"
    show danny smile
    "I look at him with a frown on my face, trying to work him out."
    bree.say "So what, Danny?"
    bree.say "You're not pissed that I have a belly?"
    "Danny shakes his head as he reaches out to place a hand on it."
    "And I do the best I can to keep from getting distracted as he starts to stroke it too."
    "Oh my god - this guy's such a charming asshole!"
    show danny joke
    danny.say "Hell no!"
    danny.say "I think it looks really hot on you, [hero.name]."
    danny.say "Plus your boobs got bigger too - so it's a double win!"
    show danny smile
    "I know that I should be mad at Danny for the way he's talking to me."
    "But that's all part of how I got into this situation in the first place."
    "Falling for his bad-boy charms!"
    show danny joke
    danny.say "Ooh.."
    danny.say "I felt the little varmint kick!"
    danny.say "They're gonna be a proper little slugger!"
    show danny smile
    "It must be a total coincidence, but that's what my dad used to call me!"
    "Oh damn it..."
    "Now I really can feel myself melting inside for Danny."
    "I'm even starting to imagine him teaching our kid to play ball!"
    $ danny.love += 2
    return

label danny_belly_kiss_female:
    show danny joke at center, zoomAt(1.5, (640, 1040))
    danny.say "Mmm..."
    danny.say "Come here, baby..."
    danny.say "Let me lay some smack on that thing!"
    show danny normal
    "I feel the sensation of hands taking hold of my belly."
    "But there's nobody around to be seen."
    "That is until I look down."
    show danny at center, zoomAt(1.5, (640, 1240)) with ease
    "Then I see Danny, kneeling on the ground in front of me."
    show danny at center, traveling(2.5, 0.3, (640, 1940))
    "And he's already leaning forwards, puckering his lips!"
    bree.say "Danny..."
    bree.say "What are you doing down there?"
    bree.say "What are you..."
    bree.say "Oh..."
    bree.say "Oh my goodness!"
    show danny smile
    "I can feel my reaction to Danny's attentions changing with each passing moment."
    "At first I feel surprised, almost shocked at what he's doing."
    "But it's not like I can summon up an iota of will to resist either."
    "And the more he kisses my belly, the more I feel the urge to resist melting away."
    "This means that I'm soon helpless to resist, just standing there as he has his way."
    "And this isn't some reserved friend just planting a peck on my belly for good luck."
    "Danny's kissing it with a passion, like he means every one of them."
    "But somehow, the fact that he's the one doing it means that I'm not creeped out."
    "In fact, I'm not put off in the slightest."
    "Instead I find myself leaning into the experience."
    "Putting my hands on Danny's shoulders in an effort to keep him down there."
    "And all the time hoping that he's not going to get tired of what he's doing any time soon."
    "I just hope that there's nobody watching us as all of this is happening."
    "Because I feel like there's a distinct possibility Danny won't stop at just kissing."
    "I mean, he seems to be getting all worked-up, so he might go lower and do more..."
    "Oh man, now I am starting to blush and feel self-conscious."
    "Where did all of that even come from?"
    "For a moment there I was actually thinking of pushing Danny's head lower!"
    "And now I feel like I need to go take a long, cold shower."
    $ danny.love += 3
    return

label danny_belly_listen_female:
    show danny joke at center, zoomAt(1.5, (640, 1040))
    danny.say "Ooh..."
    danny.say "The kid's lively today, huh?"
    show danny smile
    "I can't help twitching and looking up as Danny says this."
    "Because the baby really is moving inside of me right now."
    "But the odd thing is that they were pretty still before Danny showed up."
    "It's about then that an idea occurs to me."
    bree.say "Danny..."
    bree.say "Would you come over here and talk to my bump?"
    show danny normal
    "Danny looks at me sideways."
    "Like he suspects that it might be some kind of trick."
    show danny scared
    danny.say "Huh?"
    danny.say "Are you sure about that?"
    show danny normal
    "I nod and pat my belly."
    bree.say "Of course I am, Danny."
    bree.say "And you can trust me."
    bree.say "I'm not the cops, am I?"
    show danny smile
    "This seems to be enough to convince Danny."
    "Because a moment later he makes it over to me."
    show danny at center, traveling(2.5, 0.3, (640, 1940))
    "Then he gets down on one knee and puts his ear to my belly."
    show danny joke
    danny.say "Erm..."
    danny.say "Wadda ya want me to say?"
    show danny smile
    "The question throws me a little."
    "Because I hadn't thought of that."
    bree.say "I don't really know, Danny..."
    bree.say "But I'm sure whatever you can think of will be fine."
    bree.say "I think the baby just likes the sound of your voice."
    "Danny's eyebrows shoot up at this."
    "And for the first time he looks like he's taking it seriously."
    show danny joke
    danny.say "Oh, sure thing, [hero.name]..."
    danny.say "I'll just start talking about something that gets me going, yeah?"
    danny.say "Like motorbikes...that's a thing I can talk about all day long!"
    danny.say "Oh yeah, I swear that I remember the first one I ever saw..."
    show danny smile
    "Soon enough, Danny's prattling on about motorbikes and all that stuff."
    "But the truth of the matter is that I'm totally not listening to him."
    "Instead all of my attention is focussed on my bump."
    "I'm feeling every little twitch and turn the baby makes."
    "And I was right, they are responding to Danny's voice!"
    "Which I guess means that there must be something about him."
    "Some redeeming quality that's buried so deep it's hard to see."
    "But something that a true innocent can easily sense and be drawn too."
    $ danny.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
