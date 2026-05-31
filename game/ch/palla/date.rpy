label palla_date_intro_valentine_male:
    palla.say "Mirror, mirror, on the wall..."
    palla.say "Who's got the fairest valentine of all?"
    "It takes me a moment to realise that Palla's waiting for an answer."
    mike.say "I...uh..."
    mike.say "I do...I guess?"
    "Palla smiles and nods, evidently pleased with my reply."
    palla.say "That's right, [hero.name], you do!"
    return

label palla_date_intro_halloween_male:
    palla.say "Well, [hero.name], how do I look?"
    "I can't help gasping in admiration as Palla sweeps up to me."
    mike.say "Wow, Palla, you look amazing tonight!"
    mike.say "Are you going the extra mile because it's Halloween?"
    "Palla raises her eyebrows in genuine surprise."
    palla.say "It is?"
    palla.say "Huh, I had no idea!"
    palla.say "No way did I dress like this for Halloween."
    palla.say "I'm dedicated to looking good three hundred and sixty-five days a year!"
    return

label palla_date_intro_christmas_male:
    mike.say "Merry Christmas, Palla!"
    mike.say "Wow...you're looking stylish tonight!"
    "Palla smiles at the compliment, almost purring like a cat."
    palla.say "Thank you, [hero.name]."
    palla.say "I love this time of year."
    palla.say "Because there are so many wonderful winter fashion collections to choose from!"
    return

label palla_date_intro_birthday_male:
    mike.say "Happy birthday, Palla!"
    mike.say "And may I say, you're looking stunning!"
    mike.say "Did you pick that outfit because it's your birthday?"
    palla.say "Thanks for noticing the effort, [hero.name]."
    palla.say "It flies over most people's heads."
    palla.say "But no, I put in the same amount of effort every day of the year."
    return

label palla_date_intro_mc_birthday_male:
    mike.say "Erm...hey, Palla..."
    mike.say "Are you...are you ready for our date?"
    palla.say "Of course I am, [hero.name]."
    palla.say "But what's with you?"
    palla.say "Sounds like you have something on your mind."
    mike.say "Oh yeah...well..."
    mike.say "I was just wondering - did you remember it's my birthday?"
    palla.say "It is?"
    palla.say "Oh dear - I must have forgotten all about it."
    palla.say "After all, I HAVE been so busy picking out my outfit for today!"
    return

label palla_date_eat_a_burger:
    "Palla looks at the burger, then back up at me. She points at the burger."
    palla.say "Doesn't this place have any real food? Something that at least pretends to be a vegetable?"
    mike.say "It's got lettuce and tomato!"
    palla.say "Wilted lettuce and a tomato that's barely even red don't count."
    mike.say "Um. Potatoes are a vegetable, right?"
    "Palla makes a disgusted noise."
    return

label palla_date_buy_drink:
    if palla.is_visibly_pregnant:
        show palla angry
        $ palla.love -= 10
        palla.say "Erm...don't you remember getting me pregnant, [hero.name]?"
        palla.say "Because I certainly do!"
        palla.say "It's basically your fault I can't do anything fun."
        palla.say "At least not while I have your kid inside of me!"
        $ hero.cancel_activity()
        hide palla
    else:
        "As soon as she has a drink in her hand, Palla's mood seems to visibly improve."
        "She becomes more animated and talkative in between sips."
        "Maybe all she needed was something to loosen her tongue?"
    return

label palla_date_play_darts:
    "Palla shrugs and agrees to play a couple of rounds of darts with me."
    "She throws the first dart and it hits and sticks into the wall about 2 feet away from the board. She turns and gives me a flat look."
    palla.say "Oops. I missed."
    "If there were any more sarcasm dripping from that line, it'd make a mess on the floor."
    return

label palla_date_pub_play_pool:
    "Even though I let her break, Palla's just not getting into the game as we begin to play pool."
    "When she lines up a shot, her aim is terribly off. Clearly this isn't her game and it frustrates her. After a few tries, she gives up and puts her stick back on the rack."
    palla.say "I'm surprised, [hero.name], that you want to play a game where I hit your balls with a stick."
    "She turns and walks away from the table, leaving me with no useful response."
    return

label palla_date_buy_a_round:
    if palla.is_visibly_pregnant:
        show palla angry
        $ palla.love -= 10
        palla.say "Erm...don't you remember getting me pregnant, [hero.name]?"
        palla.say "Because I certainly do!"
        palla.say "It's basically your fault I can't do anything fun."
        palla.say "At least not while I have your kid inside of me!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - palla.love and palla.flags.drinks < 2):
        show drink palla
        if palla.love < 100:
            "Palla just kind of shrugs when I say that the next round is on me."
            "But I can't really figure out if she's not particularly interested in more drink."
            "Or if she just expects me to buy her drinks for the privilege of being seen in her company."
        elif palla.love < 160:
            "I buy a round of beers for the whole pub."
            palla.say "Don't expect buying everyone a drink to impress me, [hero.name]."
            mike.say "I don't expect anything to impress you. I keep hoping for a pleasant surprise."
            palla.say "Keep hoping, sucker."
            mike.say "Hope springs eternal."
            palla.say "So does that hole in your wallet if you keep buying drinks for everyone who isn't {b}me{/b}."
        else:
            "I buy a round of beers for the whole pub."
            palla.say "Oh, big spender. You trying to show off the size of your wallet?"
            mike.say "It's not my big wallet you're interested in."
            "Palla shoots a glance toward my crotch."
            palla.say "It can be both, right? Yes, definitely both."
        $ game.active_date.score += 5
        if "rebel" in palla.traits:
            $ game.active_date.score += 5
        $ palla.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Palla doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label palla_dance_with_replace_male:
    show palla
    $ renpy.dynamic("palla_nick")
    $ palla_nick = "Palla"
    if not palla.flags.nokiss:
        $ palla_nick = randchoice(["Sexy", "Gorgeous", "Bitch", "Beautiful"])
    mike.say "Hey [palla_nick], care to dance?"
    if not "palla_event_04" in DONE:
        palla.say "Yes, but not with you."
        $ hero.cancel_activity()
        return

    if hero.has_skill("dance"):
        palla.say "Fuck yeah!"
        hide palla
        show dance palla
        "As we dance together, it's as though the two of us become one. Mostly I lead, and she anticipates my every move."
        if palla.love > 120:
            "When the right music comes by, she presses her body right up to mine, and we dance dirty. She doesn't hesitate to use everything in the dance."
            "And I mean everything."
            "When we dance, it is erotic, it is exhilarating, and it is exhausting."
    elif hero.flags.teaching_dance == -1:
        palla.say "No way, you can't dance for shit."
        menu:
            "Teach me!":
                mike.say "Teach me to dance!"
                palla.say "Maybe, I'll think about it."
                $ hero.flags.teaching_dance = 1
                $ palla.love += 1
                hide palla
                return
            "Forget it!":
                mike.say "Oh forget it, then."
                $ hero.flags.teaching_dance = -1
                $ palla.love -= 1
                hide palla
                return
    elif not hero.flags.teaching_dance:
        palla.say "Sure, I love to dance!"
        "But I'm a terrible dancer, and Palla quickly gets frustrated."
        palla.say "You really need to learn to dance, asshole."
        menu:
            "Okay, teach me!":
                mike.say "Teach me! You're great at this!"
                palla.say "Hmm. Maybe. I'll think it over."
                $ hero.flags.teaching_dance = 1
                $ palla.love += 1
                hide palla
                return
            "Forget it!":
                mike.say "Oh forget it, then."
                $ hero.flags.teaching_dance = -1
                $ palla.love -= 1
                hide palla
                return
    else:
        palla.say "Ready for a dance lesson?"
        mike.say "Yes!"
        hide palla
        show dance palla
        if hero.flags.teaching_dance == 1:
            "Palla spends the better part of an hour walking me through some of her basic dance moves. That part isn't too hard."
            "The more interesting part is how I need to read her, to anticipate what she's going to do."
            "While at the same time I use subtle cues to communicate to her what I'm going to do. Sometimes it's just the first step."
            "And we both know the routine. But sometimes we get creative."
            "That part I don't do very well at, but I'm definitely learning."
        elif hero.flags.teaching_dance == 2:
            "We build on what I learned last time, introducing a few more dance moves and routines. While at first it's hard, one part of it really motivates me."
            "Whenever I get it really right, she gets this hungry look in her eyes, like she just wants to throw me down and fuck me right there."
            "This dancing thing really turns her on, and the more I get into it, the more I start to see why."
        elif hero.flags.teaching_dance == 3:
            "When we started, Palla didn't really want to teach me to dance, she clearly thought I would be a burden."
            "But as I get better, she's really taken a shine to it. And I am definitely getting better."
            "And to be honest, this is the nicest to me she has ever been."
        else:
            "Palla shows me a few new moves, and I'm able to work out where they go pretty quickly. After an hour or so she gives me a big smile."
            palla.say "I think, [hero.name], that your lessons are done, and while you still have a lot to learn, you can dance well enough that I won't say you suck anymore!"
            $ hero.gain_skill("dance")

        $ hero.flags.teaching_dance += 1

    $ bonus = hero.fitness / 20
    if hero.has_skill("dance"):
        $ bonus += 2
    $ palla.love += bonus
    $ hero.fun += 2
    $ game.pass_time(needs=True)
    hide dance palla
    return

label palla_train_with_replace_male:
    show palla
    mike.say "Palla, do you want to work out together?"
    if "palla_event_03f" in DONE and palla.love >= 60:
        palla.say "Why not."
        "I work out with Palla."
        $ hero.flags.dirty = TemporaryFlag(True, "day")
        $ hero.fitness += 1
        $ hero.fun += 2
        $ bonus = 1
        if hero.fitness >= 75:
            $ bonus += 1
        $ palla.love += bonus
        if hero.fitness >= palla.sub:
            $ palla.sub += 1
    else:
        palla.say "I don't think so."
        $ hero.cancel_activity()
    hide palla
    return

label palla_date_play_arcade_intro_male:
    palla.say "Urgh..."
    palla.say "I can't believe I let you talk me into this, [hero.name]."
    palla.say "This place is dingy, smelly and full of awful people!"
    "I can't help shaking my head at Palla's opinion of the arcade."
    "I mean sure, it's a little dark and the carpet is kind of sticky."
    "But to me, it's like an Aladdin's Cave of wonder!"
    mike.say "Just give it a chance, Palla."
    mike.say "Then you'll see how much fun this place can be."
    mike.say "I honestly believe that there's a videogame for everyone!"
    "Palla crosses her arms over her chest and rolls her eyes."
    palla.say "Well, I believe that you're delusional!"
    "I try to ignore Palla's negative vibes as best I can."
    "And at the same time I begin scanning the arcade."
    "Then my eyes settle on a particular cabinet."
    mike.say "Let's try this one, Palla."
    mike.say "It's called 'Demon's Lair'."
    mike.say "The idea of the game is to rescue the princess."
    palla.say "Hmm..."
    palla.say "I'd rather play the princess myself."
    palla.say "But whatever - let's get this over with!"
    "I nod eagerly, already feeding coins into the slot."
    return

label palla_date_play_arcade_win_male:
    "One thing I forgot to mention to Palla was the difficulty of this game."
    "It's beyond hard, probably verging on brutal!"
    "Which isn't a problem for me, as I've played the hell out of it."
    "But it begins to punish Palla almost from the start!"
    palla.say "Wha...what just happened?"
    palla.say "Did I...did I just get killed?!?"
    palla.say "That's not fair!"
    mike.say "Yeah, Palla..."
    mike.say "This game's a tough one."
    mike.say "But it's all about the timing, yeah?"
    "I don't think that Palla pays much attention to my advice."
    "Because as we eat through our credits, nothing seems to change."
    "She dies quickly and often, complaining every time."
    "And it doesn't help that I'm doing pretty well either!"
    "Once we're done, I can almost feel Palla's anger."
    "It's like the emotion's seeping out of her pores!"
    palla.say "Well, that was a waste of time and money."
    palla.say "And I never want to play another videogame as long as I live!"
    mike.say "That's probably a good idea, Palla."
    palla.say "Of course it is, [hero.name]!"
    palla.say "But thank you for agreeing with me."
    mike.say "Yeah, you're so bad at it that there's really no point..."
    return

label palla_date_play_arcade_lose_male:
    "One thing I forgot to mention to Palla was the difficulty of this game."
    "It's beyond hard, probably verging on brutal!"
    "It's something that kept me from playing the game."
    "But to my surprise, Palla seems not to notice it at all."
    palla.say "Wow..."
    palla.say "The graphics are so amazing!"
    palla.say "They're just like a cartoon."
    mike.say "I...I kind of need to concentrate, Palla!"
    mike.say "Argh!"
    mike.say "I died again!"
    "Palla doesn't seem to hear what I'm saying."
    "Because she keeps on distracting me when I'm playing."
    "And at the same time, she somehow breezes through the game when she's in control."
    "One we've eaten through our credits, I'm frazzled and exhausted."
    "And it doesn't help that Palla's beaten me with ease."
    palla.say "Why didn't you tell me videogames could be like this, [hero.name]?"
    palla.say "It was like being inside of a movie!"
    mike.say "Whatever, Palla..."
    palla.say "Oh, don't sulk, [hero.name]."
    palla.say "You can't help it if you suck!"
    return

label palla_dick_reactions:
    if not palla.flags.seendick:
        $ palla.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions palla smile
            palla.say "Nice to see you have some upsides!"
            mike.say "Hey - nice time to pick to be mean!"
            show dick reactions palla mock
            palla.say "Blah, blah, blah..."
            show dick reactions palla tasty
            palla.say "Just stop talking and do something with it already!"
            $ palla.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions palla mock
            palla.say "Hmm..."
            mike.say "What's the problem, Palla?"
            palla.say "Well, let's just say I'm disappointed."
            show dick reactions palla smile
            palla.say "But I'm not surprised!"
            $ palla.sub -= 10
            $ palla.love -= 10
        hide dick reactions
    return

label palla_halloween_invitation:
    show palla
    "Palla's the only girl that I want to invite to the Halloween party."
    "Were it anyone else, all I'd do is walk up and ask the question."
    "But Palla's a little bit more complicated than that."
    "And that's because she..."
    "Well, let's be honest - Palla can be a bit of a bitch!"
    "And by that I mean she can be a massive bitch!"
    "I need to tread carefully with this one."
    "Pitch it to her in just the right way..."
    mike.say "Hey, Palla..."
    mike.say "You wanna come to a Halloween party at my place?"
    "Arrgh!"
    "What did I just do?!?"
    "The words are out of my mouth before I can even think!"
    "And I can see Palla's instant reaction to them too."
    palla.say "What, [hero.name]?"
    palla.say "Did you really just invite me to a...a Halloween party?"
    palla.say "At that dump you live in too?"
    "Every word feels like a slap in the face."
    "And Palla lands them with expert precision."
    "Already she's got my head spinning!"
    mike.say "Erm...yeah, Palla."
    mike.say "I guess I did!"
    mike.say "You don't have to come if you don't want to."
    mike.say "I mean, I DO want you to come."
    mike.say "Will you come?"
    show palla annoyed
    "Palla rolls her eyes and tuts in disapproval."
    if palla.love >= 100 or palla.sub >= 90:
        palla.say "Just a second..."
        palla.say "Your housemates, they're girls - aren't they?"
        mike.say "They were last time I checked, Palla."
        "Palla goes quiet for a moment."
        "But I can see that she's thinking."
        palla.say "This party..."
        palla.say "Would it happen to be a costume party?"
        mike.say "Oh yeah - yeah, it is!"
        mike.say "I should have said that already!"
        show palla happy
        "A slow smile spreads across Palla's face."
        "Which is something that should reassure me."
        "But instead it kind of makes me nervous."
        palla.say "Fine, [hero.name]."
        $ palla.sub -= 1
        $ palla.love += 1
        palla.say "I'll come to your dumb little party."
        palla.say "And I'll make sure my costume is the best one there."
        show palla normal
        palla.say "An outfit that'll put your housemates to shame!"
        mike.say "Y...yeah, Palla."
        mike.say "That sounds great!"
        $ game.flags.halloween_girl = "palla"
    else:
        palla.say "Eww..."
        $ palla.love -= 1
        palla.say "I'm going to ignore that, [hero.name]!"
        show palla normal
        palla.say "Then we can start the conversation over again."
        "I nod slowly, feeling like I'm being walked over."
        mike.say "Erm..."
        mike.say "Sure thing, Palla."
        mike.say "Ah...thank you...I guess?"
        "Palla makes another tutting sound."
        "She shakes her head in a dismissive manner."
        "Which I realise means that the matter is over."
        palla.say "Try again, [hero.name]."
        show palla blush
        palla.say "And you might want to try harder this time."
        palla.say "Or else you'll be spending Halloween without me."
        show palla normal
        palla.say "And that's worse than spending it alone!"
    return

label palla_halloween_arrival:
    scene bg house
    "Opening the door, my head is still full of thoughts about the party."
    "I'm worried about a hundred little things that could go wrong."
    show palla halloween
    "But then I stop dead in my tracks, stunned by what I see before me."
    mike.say "I..."
    mike.say "Whoa..."
    mike.say "Is that...are you..."
    palla.say "Well hello to you too, [hero.name]!"
    palla.say "I guess you like what you see, huh?"
    "Palla stands before me, wearing only a seashell bikini top above her waist."
    "Below it, she has on a skirt made out of shimmering green material."
    "It's patterned with scales and has a slip up one side."
    "And to top it all off, she wears a long, red wig."
    mike.say "You're The Little Mermaid?!?"
    show palla happy
    "Palla nods happily, soaking up the attention like a sponge."
    "She sure knows how to show off like a seductive siren!"
    palla.say "The Little Mermaid was always my favourite princess growing up."
    palla.say "So naturally I just had to be her for the party."
    show palla normal
    palla.say "I make a perfect mermaid - don't you think?"
    menu:
        "Agree":
            mike.say "Wow, Palla...just wow!"
            mike.say "Just when I didn't think you could get any hotter!"
            $ palla.love += 1
            "Palla practically purrs and preens as I shower her with praises."
            "But I'm really not pretending to be impressed."
            "She looks incredible, like a real fairy tale princess."
            palla.say "Aww..."
            palla.say "Thank you, [hero.name]."
            palla.say "But you're right, it does look that good on me!"
            mike.say "I...I always had a thing for mermaids, Palla."
            mike.say "So this is pretty much like my dreams have come true!"
            "Palla cocks her head on one side."
            "And then she gives me an indulgent smile."
            palla.say "Of course, this must be like a dream for you."
            palla.say "I mean, did you ever think you'd be dating someone as hot as me?"
            "I nod and smile at this, ushering Palla inside."
            "Though I can't shake the vague feeling that I was just insulted..."
        "Disagree":
            "The words are out of my mouth before I can stop myself."
            "I don't know where they come from."
            "They just pop into my head and I say them out loud."
            mike.say "I don't know, Palla."
            mike.say "I always had you down as more of an Ursula."
            mike.say "Or maybe even a Cruella Deville."
            mike.say "You know - because you're so into fashion and all that?"
            $ palla.sub += 1
            $ palla.love -= 2
            show palla angry
            "I watch as Palla's face darkens more with every word I say."
            "And I'd stop if I could, but they just keep on coming out of me!"
            palla.say "WHAT?!?"
            palla.say "How can you even say that, [hero.name]?"
            palla.say "I'm obviously a princess - not some nasty villain!"
            mike.say "Ah..."
            mike.say "Yeah, Palla, obviously."
            mike.say "I don't know what I was thinking!"
            show palla annoyed
            "Palla makes a huffing sound and pushes past me to get inside."
            "I can see that I have some serious grovelling to do."
            "But at least she stormed into the house, rather than away from it..."
    scene bg black with dissolve
    pause 1
    return

label palla_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show palla halloween at left
    show bree halloween angry at right
    with dissolve
    palla.say "Urgh..."
    palla.say "Looks like someone shopped at goodwill for their costume!"
    "I'm getting used to the way that Palla often insults people at random."
    "And normally she at least has the manners to do it quietly and out of earshot."
    "But tonight she has to contend with the loud music to make herself heard."
    "Which means that the object of her withering insults can hear her too!"
    bree.say "HEY!"
    bree.say "Are you talking about me?!?"
    "I turn around just in time to see [bree.name] bristling with anger."
    "But Palla doesn't seem at all concerned to have been caught out."
    palla.say "Trash attracts trash, I guess!"
    bree.say "Well what about you, huh?"
    show palla angry
    bree.say "Dressed as a mermaid because you stink of rotten fish?!?"
    "Looks like I need to step in before this gets out of hand!"
    menu:
        "Defend Palla":
            mike.say "Hey, [bree.name]!"
            mike.say "Palla's our guest."
            mike.say "And she's my date too!"
            $ bree.love -= 2
            $ palla.sub -= 1
            show palla normal
            "Both of the girls round on me at the same time."
            "I see a look of calm amusement on Palla's face."
            "But [bree.name] doesn't seem happy with me at all."
            bree.say "Oh, is this YOUR date, [hero.name]?"
            bree.say "Then you can put up with her bad manners by yourself!"
            hide bree
            show palla at center
            "With that, [bree.name] walks away."
            "Which leaves me to deal with the fallout from Palla."
            palla.say "How do you live with someone like that, [hero.name]?"
            palla.say "So thin-skinned and with no sense of style!"
            mike.say "Ah, [bree.name]'s not so bad."
            mike.say "She's just a little sensitive, that's all!"
        "Defend [bree.name]":
            mike.say "Hey, Palla!"
            mike.say "Quit it with the hostility, okay?"
            $ palla.love -= 2
            $ palla.sub += 1
            show palla blush
            "Both of the girls round on me at the same time."
            "I see a look of relief on [bree.name]'s face."
            "But Palla doesn't seem happy with me at all."
            bree.say "Oh, is this YOUR date, [hero.name]?"
            bree.say "Ouch..."
            bree.say "She's pretty sharp - be sure you don't cut yourself!"
            hide bree
            show palla at center
            "With that, [bree.name] walks away."
            "Which leaves me to deal with the fallout from Palla."
            palla.say "I am supposed to be your date, [hero.name]."
            palla.say "You could have stood up for me just now!"
            mike.say "Ah, yeah, Palla."
            mike.say "But I don't have to live under the same roof as you!"
            show palla annoyed
            palla.say "Hmm..."
            palla.say "That's something we can both be glad of!"
    scene bg black with dissolve
    pause 1
    return

label palla_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show palla halloween
    with dissolve
    mike.say "Hey, Palla..."
    mike.say "I love this song!"
    mike.say "Come on - let's dance!"
    hide palla
    "I make for the dance-floor a moment later."
    "And then I turn around, looking for Palla."
    "But she's nowhere to be seen."
    "Glancing around in confusion, I scan the room."
    show palla halloween angry
    "And then I see her, hobbling in my direction."
    "The tight skirt that comprises most of her costume is the problem."
    "It's making her move with painful slowness."
    "And from the look on Palla's face, she's not amused!"
    menu:
        "Compensate":
            "As soon as Palla minces up to me, I step forwards to meet her."
            hide palla
            show dance palla halloween
            "Putting one hand on the small of her back, I take one of hers in the other."
            "And then I do the best I can to walk her through an impromptu slow-dance."
            "It doesn't take long for Palla to figure out what I'm trying to do."
            "My guess is that she's seen enough movies where the princess dances at the ball."
            "And while I may not be her idea of a prince, she seems to get the idea."
            $ palla.love += 4
            hide dance
            show palla halloween happy
            "By the time the song comes to an end, she's actually smiling."
            palla.say "That was...nice."
            palla.say "Thank you, [hero.name]."
            "And coming from Palla, that's high praise indeed!"
        "Carry on regardless":
            "I can't help laughing as Palla minces up to me."
            hide palla
            show dance palla halloween
            "And the situation only gets worse for her as we start dancing."
            "I move around without a problem, keeping in time with the music."
            "But Palla can hardly manage to turn on the spot."
            "Even doing that means she keeps on tottering dangerously."
            "And before the end of the song, disaster strikes."
            palla.say "Whoa..."
            palla.say "Help me..."
            palla.say "I'm going to fall!"
            hide dance with vpunch
            "Palla topples over and goes down like a felled tree."
            "There's nothing she can grab hold of and nobody catches her."
            "She lands flat on her face, and I scramble to her aid."
            $ palla.love -= 4
            show palla halloween angry
            "As I lead Palla gingerly away, she's muttering under her breath."
            "And I'm kind of glad I can't make out what she's saying."
    scene bg black with dissolve
    pause 1
    return

label palla_halloween_sex:
    scene bg livingroom
    show palla halloween
    with fade
    "I've been trying to keep a lid on it all night, distracting myself whenever the chance arose."
    "But by the time it's getting late, I just can't hold it in any longer, no matter how I try."
    "I've been following Palla around all evening, watching her ass through that tight mermaid tail."
    "Not to mention the seashell bra that she was on too and all the flesh that's on show!"
    "I think that Palla knows the effect she's having on me too."
    "Because she makes sure I get a view of her whenever she bend over or stretches for any reason."
    "Then, just when I think that I'm going to explode from the tension in my body, she pounces!"
    "Without warning, Palla opens the door to the bedroom."
    "And then she pushes me inside without a word of warning."
    scene bg bedroom1
    show palla halloween
    with fade
    mike.say "Whoa..."
    mike.say "What's going on!"
    "A moment later, Palla all but throws herself into my arms."
    "She wraps her arms around my neck and pulls me close to her."
    hide palla
    show palla kiss halloween
    with fade
    $ palla.flags.kiss += 1
    "I feel her lips press against mine and her tongue slip into my mouth."
    "It doesn't take long for me to shake off the surprise."
    "And I do all that I can to return Palla's passionate attentions."
    "As she writhes and wriggles in my arms, it begins to feel like she's a real mermaid."
    "The tightness of her costume means I can imagine her squirming after being caught in a net."
    hide palla
    show palla halloween blush
    with fade
    "All of a sudden, Palla breaks away from the kiss."
    "She pants heavily, trying to catch her breath."
    "And then she fixes me with the seductive gaze of a siren."
    palla.say "They never show this bit in the movies."
    palla.say "The part where the mermaid princess gets fucked by her prince."
    "I nod eagerly, already imagining what comes next."
    palla.say "And the story always says the mermaid wanted legs."
    palla.say "But I think what she really wanted was a pussy!"
    "I nod again, because I don't think I can manage to actually speak."
    "Every word that comes out of Palla's mouth makes me harder than ever!"
    palla.say "Do you want it, [hero.name]?"
    palla.say "Do you want to be the first to fuck my pussy?"
    palla.say "It's so wet and slippery..."
    show palla stand bedroom wet pleasure with fade
    "As if she needed to make it more clear, Palla turns her back to me."
    "And then she pulls aside her tight skirt, revealing her pert ass."
    "But she also reveals the fact that she's not wearing panties either."
    "She's been walking around all night with noting under her costume!"
    "I don't even realise that I'm moving."
    "The first thing I know is that I have Palla up against the wall."
    "She's pressed against the glass of the mirror."
    "And she looks back over her shoulder at me, eyes wide with anticipation."
    "Palla doesn't say a word, but she nods her head."
    "Which is all the permission that I need."
    "I have my clothes off in a matter of seconds."
    "And then my hands are all over Palla once more."
    "One tugs down her bra, spilling her breasts."
    show palla stand dick
    "The other guides my cock between her thighs."
    "She wasn't kidding when she said she was wet either."
    "All it takes is for my cock to press against the lips of her pussy."
    show palla stand -dick ahegao
    "And then I hear her gasp as I slip smoothly inside of her."
    "I don't stop moving until I'm as deep into Palla as I can go."
    "And once there, I keep on pushing forwards."
    "This pushes Palla into the mirror, her breath fogging the glass."
    "But before she can collect herself, I start to move inside her."
    "I don't bother to start slow and build up speed."
    "Instead my thrusts are as fast and powerful as I can make them."
    "Palla's already teased me into a state of almost desperate arousal."
    "And so all that I want to do is take her as quickly as I can."
    "My groin slaps noisily against her exposed buttocks."
    "Her breasts are squashed against the wall, over and over again."
    show palla stand normal
    "Palla looks back over her shoulders at me as I pound her without mercy."
    "She's gasping the whole time, almost squealing with each thrust."
    "Palla might have claimed she wanted to be a mermaid princess."
    "But she's throwing herself into the role of being a wanton siren right now!"
    palla.say "Fuck me..."
    palla.say "Fuck me harder..."
    palla.say "Make the mermaid cum!"
    "That's more than I can take, the limit of my resistance."
    show palla stand ahegao cum with hpunch
    "I lose it all at once, shooting my load into Palla."
    with hpunch
    "She lets out a scream of pure release, her muscles turning to water."
    with hpunch
    "Palla leans against the tiled wall and slides slowly downwards."
    "She slips off of my cock and collapses onto the bedroom floor."
    "All I can do is stand there, panting and leaning against the wall."
    "I know that I should help her up, at least check she's okay."
    "But I'm afraid that I'd just end up collapsing beside her."
    $ palla.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
