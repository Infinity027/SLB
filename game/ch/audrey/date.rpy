init python:
    Event(**{
    "name": "audrey_date_watch_the_movie",
    "label": "audrey_date_watch_the_movie",
    "priority": 500,
    "conditions": [
        IsDone("audrey_sub_event_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinemaroom"),
            IsActivity("date_watch_the_movie")
            ),
        PersonTarget(audrey,
            OnDate(),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": False,
    "once_week": True,
    "chances": 20,
    })

label audrey_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Audrey."
    mike.say "You look great, and I'm so happy you're my valentine!"
    "Audrey snorts at this and shakes her head."
    audrey.say "Yeah, well..."
    audrey.say "You were the best I could get at such short notice!"
    audrey.say "Come on, let's go have some fun before I change my mind..."
    return

label audrey_date_intro_halloween_male:
    audrey.say "Oh, I'm sorry, [hero.name]..."
    audrey.say "Were we supposed to be dressing up as scary monsters for Halloween?"
    "Audrey's question throws me, and I end up looking myself up and down."
    mike.say "What...what are you talking about, Audrey?"
    mike.say "I don't remember anyone mentioning..."
    mike.say "Hey, wait a minute!"
    "Audrey sniggers as reality dawns on me."
    audrey.say "Had you going for a second there!"
    audrey.say "And you do look kinda scary, [hero.name]."
    mike.say "Ha ha, Audrey, very funny!"
    return

label audrey_date_intro_christmas_male:
    mike.say "Merry Christmas, Audrey!"
    mike.say "I hope you're full of festive cheer?"
    "Audrey gives me a crooked grin and shakes her head."
    audrey.say "You were always the first up on Xmas morning, weren't you?"
    mike.say "Huh...how did you know that?"
    audrey.say "Ah, just call it a hunch!"
    return

label audrey_date_intro_birthday_male:
    mike.say "Happy birthday, Audrey!"
    mike.say "I hope you have a good time on our date tonight."
    mike.say "I planned everything out to make it extra special!"
    audrey.say "Yeah, yeah, yeah..."
    audrey.say "I'll be the judge of that, [hero.name]!"
    audrey.say "You just worry about keeping the birthday girl happy..."
    return

label audrey_date_intro_mc_birthday_male:
    mike.say "You ready for our date, Audrey?"
    audrey.say "Hmm..."
    audrey.say "I guess so, [hero.name]."
    mike.say "There's something special about today as well."
    mike.say "You know what it is, Audrey?"
    audrey.say "Nah - I have no idea."
    mike.say "Oh...okay..."
    audrey.say "Ha, ha, ha...oh, [hero.name]!"
    audrey.say "The look on your face!"
    audrey.say "Yeah, yeah...I know it's your birthday."
    return

label audrey_date_eat_a_burger:
    "Audrey doesn't sniff or complain as she picks up her burger and begins to eat."
    "But then she doesn't make any positive sounds as she does so either."
    "I'm not sure if the thing is so-so, or she's just being tactful."
    return

label audrey_date_buy_drink:
    if audrey.is_visibly_pregnant:
        show audrey angry
        $ audrey.love -= 10
        audrey.say "Wow, [hero.name], just wow."
        audrey.say "Way to win Father of the Year!"
        audrey.say "This kid's screwed before it's even been born!"
        $ hero.cancel_activity()
        hide audrey
    else:
        "Audrey seems pleased to have a drink in her hand."
        "And she savours the first sip that she makes as well."
        "She looks like she really enjoyed that."
    return

label audrey_date_play_darts:
    "While she agrees to play a game and does all that's required of her."
    "I get the impression that Audrey couldn't care less about playing darts."
    "But at least she doesn't make it too awkward by complaining the whole time."
    return

label audrey_date_pub_play_pool:
    "Audrey indulges me in a game of pool or two."
    "Though she's not visibly enthused by the act of playing."
    "If anything, I think she gets more out of posing around the table with the cue in her hand."
    return

label audrey_date_buy_a_round:
    if audrey.is_visibly_pregnant:
        show audrey angry
        $ audrey.love -= 10
        audrey.say "Wow, [hero.name], just wow."
        audrey.say "Way to win Father of the Year!"
        audrey.say "This kid's screwed before it's even been born!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - audrey.love and audrey.flags.drinks < 2):
        show drink audrey
        "When I offer to buy the next round, Audrey nods with genuine enthusiasm."
        "I have no idea if she'll return the favour for the next one."
        "But it still feels good to know that there's at least one way I can win her over."
        $ game.active_date.score += 5
        if "rebel" in audrey.traits:
            $ game.active_date.score += 5
        $ audrey.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Audrey doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label audrey_dance_with:
    "There's a look in Audrey's eye as we begin to dance, almost like a challenge of some kind."
    "She's not reluctant to be there or be seen with me, but she's defiant all the same."
    "Audrey holds my eye, as if she's judging the whole time whether or not I live up to her standards."
    return

label audrey_date_play_arcade_intro_male:
    audrey.say "So this is what you do when you're not at work, [hero.name]?"
    audrey.say "Wow...I had no idea you were that much of a nerd!"
    "I turn around just in time to catch the amused sneer on Audrey's face."
    "And not for the first time, I wonder if I made the right decision."
    "I had figured that everyone likes videogames, right?"
    "And so asking Audrey to come along to the arcade with me was a great idea."
    if audrey.flags.nickname == "toy":
        mike.say "What's wrong, Toy?"
    else:
        mike.say "What's wrong, Audrey?"
    mike.say "Don't you like videogames?"
    audrey.say "Oh, you finally piked up on that, did you?"
    mike.say "Well...you never said anything to that effect."
    audrey.say "Yeah, well you never asked!"
    "I can sense that this outing's in danger of going south."
    "And so I make an effort to save it in the only way I can."
    if audrey.flags.nickname == "toy":
        mike.say "Yeah, but you don't have to actually like videogames, Toy."
    else:
        mike.say "Yeah, but you don't have to actually like videogames, Audrey."
    mike.say "You can just like the IDEA of them."
    mike.say "You know, like the fact that they're retro and kind of ironic?"
    "Audrey looks at me sideways, narrowing her eyes."
    audrey.say "Nice try, [hero.name], nice try."
    audrey.say "All that effort earns you one chance to impress me."
    audrey.say "So what are we going to play?"
    mike.say "Erm..."
    mike.say "How about 'Monkey Kong'?"
    mike.say "That's a classic!"
    "I hurry over to the arcade cabinet and start pumping in the coins."
    "And Audrey follows, realising that it's now too late to back out."
    return

label audrey_date_play_arcade_win_male:
    mike.say "You know how to play, right?"
    mike.say "Jump over the barrels and rescue the girl."
    mike.say "That's all there is to it!"
    audrey.say "Okay, [hero.name], whatever!"
    audrey.say "I think I can handle a dumb videogame!"
    "Despite her bold claims, Audrey doesn't do well."
    "She dies quickly and often, cursing every time."
    "And so it's not long before she's out of the game."
    "Then it's my turn!"
    audrey.say "Hey, [hero.name]!"
    audrey.say "How are you doing that?"
    audrey.say "Are...are you cheating?!?"
    if audrey.flags.nickname == "toy":
        mike.say "No way, Toy!"
    else:
        mike.say "No way, Audrey!"
    mike.say "I just had a lot of practice, that's all."
    "Once the game is over, there's a clear winner."
    "My score's way higher than Audrey's."
    "And she's already sulking over it."
    audrey.say "Now what was the point of that?"
    audrey.say "I didn't have fun, and I lost too!"
    if audrey.flags.nickname == "toy":
        mike.say "That's too bad, Toy."
    else:
        mike.say "That's too bad, Audrey."
    mike.say "Because I had a great time!"
    return

label audrey_date_play_arcade_lose_male:
    mike.say "You know how to play, right?"
    audrey.say "Yeah, yeah - how hard can it be?"
    "Without waiting for permission, Audrey elbows me aside."
    "She takes hold of the joystick and begins to play."
    mike.say "You...you have to jump over the barrels!"
    mike.say "And save the..."
    audrey.say "Save the girl, I get it!"
    audrey.say "Urgh...what a sexist concept!"
    "I watch in growing amazement as Audrey plays the game."
    "Somehow she it just seems to click and she does well."
    "Which makes it that much worse for me when my turn comes around."
    "Because this has never been a game I spent too much time playing!"
    audrey.say "Ouch!"
    audrey.say "You really should have jumped over that, [hero.name]!"
    audrey.say "That one too!"
    audrey.say "Wow...you really suck at this game!"
    "Once the game is over, there's a clear winner."
    "Audrey's score is way higher than mine."
    "And she's already gloating over the fact."
    audrey.say "Now what was the point of that?"
    audrey.say "You challenged me to a game and you lost!"
    if audrey.flags.nickname == "toy":
        mike.say "Ah...don't rub it in, Toy!"
    else:
        mike.say "Ah...don't rub it in, Audrey!"
    mike.say "We'll go somewhere you choose next time."
    return

label audrey_dick_reactions:
    if not audrey.flags.seendick:
        $ audrey.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions audrey tasty
            audrey.say "Yeah - that's what I like!"
            audrey.say "Bring that thing over here!"
            if audrey.flags.nickname == "toy":
                mike.say "Ah...don't rub it in, Toy!"
            else:
                mike.say "Sure thing, Audrey!"
            audrey.say "I'm gonna enjoy this!"
            $ audrey.sub += 10
            $ audrey.love += 10
        elif hero.has_skill("smalldick"):
            show dick reactions audrey disgusted
            audrey.say "Hah!"
            audrey.say "Is that IT?!?"
            mike.say "H...hey..."
            mike.say "That's kind of mean, don't you think?"
            show dick reactions audrey mock
            audrey.say "Well, that's kinda small - don't YOU think?"
            $ audrey.sub -= 10
            $ audrey.love -= 10
        hide dick reactions
    return

label audrey_halloween_invitation:
    show audrey
    "The only girl that I want to invite to the Halloween party is Audrey."
    "But how do I even know if she's into something like a party at my place?"
    "I mean, she's not the most simple or straight-up kind of girls."
    "But then maybe that means that she'll jump at the chance to surprise me?"
    "I guess the only answer is to take the bull by the horns and just ask her..."
    if audrey.flags.nickname == "toy":
        mike.say "Little Toy..."
    else:
        mike.say "Audrey..."
    mike.say "Did you have any plans for Halloween?"
    show audrey frown
    "Audrey turns her head to look at me."
    "And I see that there's an incredulous smirk on her face."
    audrey.say "I'm sorry, [hero.name]."
    audrey.say "But did you just say Halloween?"
    if audrey.flags.nickname == "toy":
        mike.say "Uh...yeah. Toy."
    else:
        mike.say "Uh...yeah. Audrey."
    mike.say "That's exactly what I said."
    show audrey happy
    "At this, Audrey bursts out laughing."
    "She shakes her head as she sniggers at me."
    audrey.say "What are you, [hero.name] - five years old?"
    audrey.say "You think I might already be trick or treating with my girlfriends?!?"
    "I try as best I can to ignore her."
    "I know that she wants me to bite."
    "And so the best thing I can do is ignore her."
    "Ignore her and push stubbornly on."
    if audrey.flags.nickname == "toy":
        mike.say "Ha, ha, Toy - very funny."
    else:
        mike.say "Ha, ha, Audrey - very funny."
    mike.say "But you didn't answer my question."
    mike.say "I'm having a party at my place."
    mike.say "And I was wondering if you wanted to come?"
    show audrey annoyed
    "Audrey finally finishes laughing at me."
    "And I see her face become thoughtful as she ponders the invitation."
    if audrey.love >= 100:
        show audrey normal
        audrey.say "You know what, [hero.name] - I might come along after all."
        if audrey.flags.nickname == "toy":
            mike.say "Aw, come on, Toy!"
        else:
            mike.say "Aw, come on, Audrey!"
        mike.say "We're gonna have punch and party-games."
        mike.say "And it'll be a costume party too."
        mike.say "Don't you want to dress up in a scary costume?"
        show audrey flirt
        audrey.say "Ah, [hero.name], I already said yes!"
        "Oops...she did already say yes."
        "I guess I just assumed she'd say the opposite!"
        if audrey.flags.nickname == "toy":
            mike.say "Sure, little Toy - of course you did!"
        else:
            mike.say "Sure, Audrey - of course you did!"
        mike.say "I'm just a bit distracted right now."
        mike.say "You know, what with organising the party and all that?"
        "Audrey rolls her eyes at me and lets out a sigh."
        show audrey annoyed
        audrey.say "Whatever, [hero.name]."
        audrey.say "So long as you're back on form the night of the party."
        show audrey flirt
        audrey.say "Because I can't wait to meet those room-mates of yours!"
        "For a moment I think that I can detect an undertone to Audrey's words."
        "Like she's not just wanting to meet them out of innocent curiosity."
        "But I'm relieved that she said yes to my invitation."
        "And so I push it out of my mind."
        "I'm sure she'll behave herself at the party."
        "Rather than act how she does at work."
        $ game.flags.halloween_girl = "audrey"
    else:
        show audrey frown
        audrey.say "You know what, [hero.name] - I'm going to take a rain-check."
        audrey.say "There's some paint that I've been meaning to watch dry for ages now."
        audrey.say "And I think Halloween is the perfect night to finally do it!"
        "I roll my eyes at Audrey in open frustration."
        "Couldn't she have been nice to me this one time?"
        if audrey.flags.nickname == "toy":
            mike.say "Aw, come on, Toy!"
        else:
            mike.say "Aw, come on, Audrey!"
        mike.say "We're gonna have punch and party-games."
        mike.say "And it'll be a costume party too."
        mike.say "Don't you want to dress up in a scary costume?"
        show audrey surprised
        audrey.say "Wow, [hero.name]!"
        audrey.say "Are you hiring a clown too?"
        show audrey happy
        audrey.say "How about a bouncy-castle?"
        "I hold up my hands, finally admitting defeat."
        if audrey.flags.nickname == "toy":
            mike.say "Okay, little Toy, okay."
        else:
            mike.say "Okay, Audrey, okay."
        mike.say "You don't want to come to the party."
        mike.say "I get it!"
        show audrey normal
        audrey.say "Sure took you long enough!"
        "I let a grunt of frustration and let it drop."
        "With an attitude like that, maybe the party's better off without her!"
    return

label audrey_halloween_arrival:
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But I get caught out again, finding something sharp an inch from my eye."
    "It's a dagger - I'm staring down the blade of a damn dagger!"
    mike.say "Aargh!"
    "I stumble backwards, tripping over the doorstep."
    "And then I fall, landing painfully on my ass."
    show audrey halloween surprised
    audrey.say "Geez, [hero.name]."
    show audrey normal
    audrey.say "I didn't think my costume was THAT scary!"
    "I look up to see Audrey standing over me."
    "She has an identical dagger in each hand."
    "And now I see that they're actually Japanese Sai."
    "That and the fact she's wearing a tight outfit all in red."
    mike.say "Ah..."
    if audrey.flags.nickname == "toy":
        mike.say "Nice Alektra costume, little Toy."
    else:
        mike.say "Nice Alektra costume, Audrey."
    "She smiles broadly as I haul myself up and onto my feet."
    audrey.say "That's right, [hero.name]."
    audrey.say "You like it?"
    menu:
        "Compliment" if hero.charm >= 25:
            "I'm still rubbing my sore ass when she asks me this."
            "And if it were anyone else, I'd be mad as hell right now."
            "But Audrey just looks so good in that costume."
            "Any thought of telling her off just fades away."
            if audrey.flags.nickname == "toy":
                mike.say "Yeah, Toy - you bet I do!"
            else:
                mike.say "Yeah, Audrey - you bet I do!"
            mike.say "You look fantastic!"
            show audrey happy
            $ audrey.love += 1
            "Audrey grins like a Cheshire Cat at this."
            "Clearly she's getting the kind of reaction she wanted."
            "She does a quick turn on the spot to show off."
            "Which only serves to make my eyes almost pop out of my head."
            audrey.say "I went to a lot of effort with all this."
            audrey.say "But it was worth it to get a reaction like that!"
            show audrey flirt
            audrey.say "So are you going to let me in or what?"
            audrey.say "I turned down lots of other offers to come to this crummy party!"
            "A small part of my brain registers the insult in what Audrey just said."
            "But it gets roundly ignored as the largest part is still drooling over her."
            if audrey.flags.nickname == "toy":
                mike.say "Oh yeah...of course, little Toy!"
            else:
                mike.say "Oh yeah...of course, Audrey!"
            mike.say "And maybe we leave the daggers with the coats?"
            mike.say "You think that would be okay?"
        "Criticize":
            "I'm still rubbing my sore ass when she asks me this."
            "And so I'm not in the mood to be positive."
            if audrey.flags.nickname == "toy":
                mike.say "The costume's fine, Toy."
            else:
                mike.say "The costume's fine, Audrey."
            mike.say "It's the accessories I'm not so keen on!"
            show audrey frown
            $ audrey.love -= 4
            if hero.charm >= audrey.sub and hero.fitness >= audrey.sub:
                $ audrey.sub += 5
            "Audrey scowls at this, crossing her arms over her chest."
            "Jesus wept - she's not even come into the house yet."
            "And she's already getting into a pout!"
            audrey.say "Well that's not a very nice thing to say."
            audrey.say "Especially after all the effort I went to."
            show audrey annoyed
            audrey.say "I didn't have to come to your crummy party, you know."
            audrey.say "I turned down other offer to be here!"
            if audrey.flags.nickname == "toy":
                mike.say "Okay, little Toy, okay."
            else:
                mike.say "Okay, Audrey, okay."
            mike.say "I'm sorry I told you off."
            mike.say "Can we just forget about it and have a nice time?"
            "Audrey makes a harumphing noise, like she's still not happy."
            "But she steps into the hallway all the same."
            mike.say "And maybe we leave the daggers with the coats?"
            mike.say "You think that would be okay?"
    scene bg black with dissolve
    pause 1
    return

label audrey_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show audrey halloween
    with dissolve
    audrey.say "Wow, [hero.name]."
    audrey.say "You must have blown some serious small-change at the dollar store!"
    "I look around to see Audrey fingering the decorations."
    "She has an ironic smile on her face as she does so."
    mike.say "Huh..."
    if audrey.flags.nickname == "toy":
        mike.say "Okay, little Toy, okay."
    else:
        mike.say "What was that, Audrey?"
    audrey.say "I said this is some cheap-ass decor."
    show audrey flirt
    audrey.say "Every expense spared, yeah?"
    "Audrey chuckles as she says this."
    "As if she feels the need to underline the insult."
    show audrey at left
    show sasha halloween angry at right
    sasha.say "Hey!"
    sasha.say "We worked hard on this shit!"
    show audrey normal
    audrey.say "Yeah - shit's the very word I was thinking of!"
    menu:
        "Defend Audrey":
            mike.say "Ah, lighten up, Sasha."
            mike.say "It's a Halloween party - it's supposed to be goofy."
            mike.say "Don't get on Audrey's case because she's not buying into it!"
            "Audrey crosses her arms over her chest, a smug grin on her face."
            show sasha vangry
            $ sasha.love -= 2
            "But Sasha frowns at me and shakes her head."
            sasha.say "Way to throw us under the bus, [hero.name]."
            sasha.say "And all to save face in front of your date!"
            mike.say "Come on, Sasha."
            mike.say "Don't be like that!"
            show sasha angry
            "Sasha doesn't dignify that with a response."
            hide sasha
            hide audrey
            show audrey halloween normal
            "She just turns her back on me and storms away."
            audrey.say "Let her go, [hero.name]."
            show audrey flirt
            audrey.say "She's just butt-hurt because you told it how it is!"
        "Defend Sasha":
            mike.say "That's not cool, Audrey."
            mike.say "Sasha's right - we all worked hard on this."
            mike.say "Me too!"
            show sasha normal
            show audrey frown
            "Sasha crosses her arms over her chest, a smug grin on her face."
            $ audrey.love -= 2
            "But Audrey looks at me in what I can only describe as disgust."
            audrey.say "Ah..."
            audrey.say "Excuse me, [hero.name] - but I'm your date!"
            audrey.say "Aren't you supposed to defend me?!?"
            show sasha annoyed
            sasha.say "Not when you're being a cow he's not!"
            hide sasha
            hide audrey
            show audrey halloween annoyed
            "Sasha turns her back on us and storms away."
            "And I can practically feel Audrey seething beside me."
            "Which is going to make things awkward..."
    scene bg black with dissolve
    pause 1
    return

label audrey_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show audrey halloween annoyed
    with dissolve
    audrey.say "Hey, [hero.name], what are we waiting for?"
    show audrey normal
    audrey.say "Let's get out there and dance already!"
    if audrey.flags.nickname == "toy":
        mike.say "Ah...sure, Toy."
    else:
        mike.say "Ah...sure, Audrey."
    mike.say "Let's go..."
    "Before I can say anymore, Audrey has hold of my hand."
    hide audrey
    "She practically drags me onto the makeshift dance-floor."
    "And once we're there, she doesn't waste any time."
    show dance audrey halloween
    "Grinding and writhing against me, she moves to the beat of the music."
    "Something which I'm more than happy to endure."
    hide dance
    show audrey grind
    "That is until she begins doing the same thing to Scottie too!"
    scottie.say "Whoa..."
    scottie.say "Hello there!"
    "Audrey makes sure that she catches my eye as she does this."
    "And I can see that she's smiling the whole time too."
    menu:
        "Protest":
            "I know Audrey pretty well."
            "Well enough that I know when she's trying to provoke me."
            "And I think about turning my back and just walking away."
            "But then it occurs to me - why not fight fire with fire?"
            "So instead of backing down, I step it up."
            "As Audrey dances closer to Scottie, so do I."
            "Pretty soon it's hard to tell who's grinding against who."
            audrey.say "Ah..."
            audrey.say "Wh...what are you doing?!?"
            if audrey.flags.nickname == "toy":
                mike.say "I'm dancing with Scottie, Toy."
            else:
                mike.say "I'm dancing with Scottie, Audrey."
            mike.say "Is there something wrong with that?"
            mike.say "Because I'm cool with you doing it."
            "For a moment Scottie just stares at the two of us."
            "And I'm waiting for him to freak out at me."
            "But then his face cracks into a smile."
            scottie.say "Wow, [hero.name] - you're wild!"
            scottie.say "It's like anything goes round here!"
            "Now that I've called Audrey's bluff, she's trapped."
            "All she can do is force a smile onto her own face."
            $ audrey.sub += 2
            "That and keep right on dancing with Scottie and Me."
        "Accept":
            "I know that Audrey's trying to provoke me."
            "But how can I just sit back and let her do this to me?"
            "She's humiliating me in my own home, in front of my friends too!"
            "I think about pulling her off of the dance-floor."
            "Just like she pulled me onto it beforehand."
            "But that would mean using force to do so."
            "And I'm not that kind of guy."
            hide audrey
            "So in the end, I just turn my back on her and walk away."
            $ audrey.sub -= 2
            "I hear Audrey laughing as I go."
            "But I just ignore the sound and keep on going."
            "I can make my feelings plain to her later."
    scene bg black with dissolve
    pause 1
    return

label audrey_halloween_sex:
    scene bg livingroom with dissolve
    "It's getting late by now and the party seems to be winding down too."
    "Everyone's feeling the effects of the booze and the dancing."
    "And all that I can hear is gentle music and subdued conversation."
    "So I flop down onto the sofa, allowing myself to relax."
    "Which is why I let Audrey lead me to my bedroom."
    scene bg bedroom1
    show audrey close halloween
    "As soon as we're inside, Audrey pushes me onto the bed."
    "While this takes me by surprise, it's not as if I don't like it."
    if audrey.flags.nickname == "toy":
        mike.say "Hey, little Toy."
    else:
        mike.say "Hey, Audrey."
    mike.say "Are you feeling cold?"
    mike.say "Or did you just want a cuddle?"
    "Audrey laughs at this."
    "And she presses herself closer against me."
    audrey.say "Hmm..."
    show audrey flirt
    audrey.say "Why not both?"
    audrey.say "And a little something more too..."
    show audrey kiss halloween with fade
    $ audrey.flags.kiss += 1
    "With that, Audrey leans in and kisses me full on the lips."
    "It's slow, sensual and everything that you could want."
    "And return the gesture without even thinking."
    "But then I feel her hand reaching into my pants."
    hide audrey
    show audrey halloween with fade
    "This makes me pull my lips away from hers and smile."
    "It's all I can do to keep my voice to a low hiss."
    if audrey.flags.nickname == "toy":
        mike.say "Toy!"
    else:
        mike.say "Audrey!"
    "Audrey grins at this, but she doesn't stop for a moment."
    "She just shakes her head at me, clearly enjoying my reaction."
    audrey.say "What does it feel like, [hero.name]?"
    show audrey flirt
    audrey.say "I'm going to ride your cock."
    audrey.say "Right here and right now."
    menu:
        "Accept" if hero.sexperience >= 10:
            mike.say "Fine by me!"
            $ audrey.sub += 1
        "Protest":
            mike.say "But...but..."
            mike.say "What if someone walks in on us?!?"
            audrey.say "Well, the way I see it, you have two choices."
            show audrey normal
            audrey.say "You can shove me off."
            audrey.say "That way you cause a scene with your cock out."
            show audrey flirt
            audrey.say "Or else you can sit still and let me have my way."
            audrey.say "And hope that nobody hears us before I'm done."
            show audrey spoon halloween with fade
            "As if to underline her point, Audrey rubs my cock between her thighs."
            $ audrey.sub -= 5
    "I can instantly tell that she's not wearing any panties under her costume."
    "That and the fact she's already as slick as a seal down there."
    show audrey spoon hard with fade
    "I don't say a word, but Audrey can still tell that I'm turned on."
    "I know it from the look in her eye as she sits down on my cock."
    show audrey spoon vaginal pleasure
    audrey.say "That's right, [hero.name]."
    audrey.say "Just give me what I want."
    audrey.say "Mmm..."
    "Audrey moans softly as I push into her."
    "And I can already feel my desire for her taking over."
    "It's pushing the fear of being discovered to the back of my mind."
    "Soon all I can think of is Audrey, as she pulls me down and onto her."
    "She keeps her moaning and panting low."
    "And I do the best I can to keep myself quiet too."
    "But all the same, that doesn't stop her indulging herself."
    show audrey spoon squeeze
    "Audrey soon takes a hold of my hands and guides them to her breasts."
    "Her costume is light and strappy, meaning that they're easily freed."
    "That done, I don't hesitate to squeeze and pinch at them."
    "And pressing her nipples between my fingers spurs her on even more."
    "Pretty soon I can hear Audrey begin to whimper."
    "The sound that she's making starts out quiet at first."
    "But it soon gets ever louder, making me break out in a nervous sweat."
    "If she keeps this up, forget about anyone walking in on us."
    "Everyone in the house, maybe even the neighbours, will hear her!"
    "I push harder, thrusting into her with all my might."
    show audrey spoon choke
    "And at the same time I clamp a hand over her mouth too."
    "Audrey struggles, wriggling to break free."
    "All of which means she's riding me harder than ever."
    show audrey spoon creampie ahegao
    "She actually bites down on my fingers as I cum."
    "And I can smell the coppery scent of blood as I shoot my load into her."
    "Soon Audrey's cries fade into exhausted panting."
    show audrey spoon squeeze pleasure
    "And only then do I take my hand off of her mouth."
    "Now she really does seem to want to just cuddle."
    "Pressing her head into my chest as her own orgasm takes her."
    $ audrey.sexperience += 1
    $ game.pass_time(1)
    return

label audrey_date_try_the_waterslide:
    show audrey waterslide
    audrey.say "Why not..."
    $ game.active_date.score += 5
    hide audrey waterslide
    return

label audrey_date_watch_the_movie:
    $ renpy.dynamic("sequel")
    init python:
        from roman import roman
        sequel = roman(audrey.flags.goblins + 2)
    scene bg cinemaroom
    if audrey.flags.goblins < 2:
        "I've been itching to see the film Audrey and I are sitting down to watch for ages now."
    "Goblins was one of those cult classics from way back in the eighties that just gets cooler with time."
    if not audrey.flags.goblins:
        "They made a great sequel some time ago."
        "So it's kind of important that I devote myself to the experience, you know?"
        "Here I am, thrilled to see what the writers did with this sequel, Goblins [sequel]."
    elif audrey.flags.goblins <= 3:
        "They started a franchise with some great films."
        "Here I am, waiting to see what the writers did with this sequel, Goblins [sequel]."
    else:
        "The producers found a golden egg and are milking the franchise as much as they can."
        "Here I am, without a great expectation about Goblins [sequel], but sequels can be better, remember Storminator 2."
    if audrey.flags.goblins <= 3:
        "The only problem is that I had to drag Audrey along to see it with me."
        show audrey annoyed casual
        "Even as the trailers are ending and the film is starting, she's still complaining!"
    else:
        "Audrey agreed to come along to see it with me."
        show audrey annoyed casual
        "But I'm pretty sure she has another agenda in mind"
    show audrey angry
    audrey.say "I can't believe I let you take me into this!"
    audrey.say "Dates are supposed to be fun for both of us, you know?"
    mike.say "Keep your voice down, Audrey!"
    mike.say "Some of us are trying to watch the film here!"
    show audrey annoyed
    audrey.say "Urgh..."
    audrey.say "Fine, [hero.name], have it your way!"
    show audrey mock
    audrey.say "I'll just have to find a way to make my own fun..."
    "That sounds pretty ominous, and normally I'd call Audrey out on it."
    show audrey annoyed
    "But she hisses those words at me just as the film finally begins."
    "And that means that my attention is instantly drawn away."
    show audrey cinema bj popcorn with fade
    "Soon enough I find myself forgetting all about her vague promises."
    "Because I'm sinking into a warm, comforting bed of nostalgic goodness!"
    "The film's great, far better than I'd expected it to be."
    "In my head I'm already preparing to discuss it at length with Jack."
    "And to be honest, I'd kind of forgotten that Audrey was even there!"
    show audrey cinema bj mikepleasure with vpunch
    "That's why I can't help jumping in my seat when I feel someone touching me."
    "I throw most of my popcorn in the air and let out a yelp of surprise."
    "But luckily for me it happens almost exactly as a jump-scare on the screen."
    "Which means that everyone else in the place is doing the same thing."
    "I look down and see a hand on my groin, opening my flies."
    show audrey cinema bj audreyhappy mikesurprised
    "And a quick glance to my side shows me that it belongs to Audrey!"
    "It's kind of a relief to find that it's my date that's feeling me up."
    "But that doesn't solve the actual problem of what she's doing."
    mike.say "Audrey!"
    mike.say "Stop it!"
    "Audrey smiles and shakes her head."
    "She's starting to sink down in her seat too."
    "It looks like she means business!"
    "I know better than to argue with Audrey when she in this kind of mood."
    "At least if she's occupied, then I know Audrey's kind of contained too."
    "The I can hopefully watch the movie without further interruption."
    "And who knows, I might even enjoy what she's going to do to me as well!"
    "So all I do is hold my hands up in a gesture of surrender."
    "She nods happily at this, then gets straight back to it."
    show audrey cinema bj blowjob with dissolve
    play sound audrey_moans_blowjob_low loop
    "Within mere moments, Audrey has my cock out of my pants."
    "She leans in close and starts to stroke it to life."
    "Even though I'm concentrating on the film, this doesn't take long."
    "It's like I'm leaving my body in her hands while my mind is on higher things."
    "And Audrey seems perfectly happy with that arrangement."
    "I can feel her licking and kissing around the base of the shaft."
    "This means that I'm soon hard and standing to attention."
    show audrey cinema bj mikepleasure
    "Now her attentions become even more intense."
    "Audrey squeezes my balls as she licks her way higher."
    "By the time she reaches the tip, I'm biting my lip."
    "And when she takes it into her mouth, I feel my heart begin to pound in my chest."
    "But then Audrey chooses to work it slowly and with infinite care."
    "Her head moves up and down gracefully."
    "And she uses her lips, tongue, even her teeth like an expert."
    "I'm still watching the film, taking in everything on the screen."
    "Yet I can feel everything that she's doing to me at the same time."
    "I know the hairs on the back of my neck are standing up."
    "And I can feel my hands digging into the padded arms of my seat."
    "I must be twitching and writhing more than I realise."
    "Because I begin to feel Audrey using her weight to pin me down."
    show audrey cinema bj mikesurprised watching -popcorn with dissolve
    "Suddenly I notice that she's not got my cock in her mouth anymore."
    "The suspicion is confirmed a moment later when I hear her chuckling."
    show audrey cinema bj mikehappy
    "And then, before I can object, she's crawling up and over me."
    "Audrey's sure to stay as low as she can, making sure she's not seen."
    "But that doesn't stop her from getting into the exact position she wants."
    show audrey reverse cowgirl cinema with fade
    "Before I know what she's trying to do, Audrey's straddling me in my seat."
    "She reaches back wit one hand, grabbing my cock as she directs traffic down there."
    show audrey reverse cowgirl vaginal mikepleasure audreyahegao
    play sound audrey_moans_discreet_low loop
    "Then she pushes it hard against her groin, and I discover she's ditched her panties!"
    "How she managed to pull off something like that is beyond me."
    "But it's also that last thing on my mind as I feel how slick she is right now!"
    show audrey reverse cowgirl mikenormal audreypleasure
    "It only takes a few seconds for me to begin pushing inside of her."
    "Audrey speeds this up even more by pushing down with all her weight."
    "Her head is resting on my shoulder now."
    "And so I hear her gasping and panting as I fill her up."
    "Then she starts to grind, almost desperately, against me."
    "My hands reach out and take hold of her haunches."
    "My eyes are still fixed on the screen, but I can't help myself."
    show audrey reverse cowgirl audreyahegao
    play sound audrey_moans_discreet_medium loop
    "I squeeze Audrey tight and push her downwards as I thrust up from below."
    "This makes her squeal into my ear, almost too loud for comfort!"
    "Realising this, she buries her head against my neck."
    show audrey reverse cowgirl audreypleasure
    play sound audrey_moans_discreet_high loop
    "Then Audrey uses her lips to kiss my neck, nibbling and licking too."
    "This isn't romantic sex where we're both expressing ourselves in a beautiful manner."
    "It's quick, dirty fucking in a public place, made hotter by the danger of getting caught!"
    "I keep on thrusting roughly into Audrey, desperate to have her despite everything."
    "And she clings to me like a needy animal in heat, squealing as I pound her."
    "Thankfully it can't go on like this for too long."
    $ audrey.love += 5
    show audrey reverse cowgirl mikepleasure audreyahegao creampie with vpunch
    play sound audrey_moans_discreet_orgasm_1
    "Soon enough I make one last push, then shoot my load into Audrey."
    with vpunch
    pause 0.15
    with vpunch
    "She stiffens, curling into a ball as she cums too."
    show audrey reverse cowgirl exhausted vaginaldrip -creampie mikenormal
    $ game.active_date.score += 40
    audrey.say "Mmm..."
    audrey.say "I...I...I..."
    audrey.say "Whoo..."
    "Then she slides off me, flopping into her own seat."
    show audrey cinema bj popcorn with fade
    "Audrey continues to babble quietly to herself for the rest of the film."
    "But at least now she's satisfied and happy to leave me in peace."
    "And now I know what I have to do to get her to shut the hell up in future."
    "Just fuck her in public, and everything will be fine!"
    $ audrey.sexperience += 1
    $ audrey.flags.goblins += 1
    $ hero.replace_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
