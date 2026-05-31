label scottie_ask_phone_female:
    if game.week_day % 2 == 0:
        bree.say "Can I get your number, Scottie?"
        bree.say "I just realised I don't have it in my phone!"
    else:
        bree.say "Hey, Scottie..."
        bree.say "Can I get your phone number?"
        bree.say "You know, like so I can call you?"
    if hero.charm >= 20 - scottie.love:
        $ hero.smartphone_contacts.append("scottie")
        if game.week_day % 2 == 0:
            scottie.say "I understand, [hero.name]."
            scottie.say "If I were you, I'd want my number too!"
            scottie.say "Here you go..."
        else:
            scottie.say "Oh yeah!"
            scottie.say "You can totally have my number, [hero.name]!"
            bree.say "Erm...okay, Scottie - you can tell me now."
            scottie.say "Uh...wait a sec...I...I think I lost my phone..."
            scottie.say "Oh no, here it is!"
            scottie.say "Now if I could only remember how this thing works..."
            bree.say "Erm...here, Scottie - let me help you with that."
    else:
        if game.week_day % 2 == 0:
            scottie.say "Oh no, not yet, [hero.name]."
            scottie.say "You only get my number when I say so."
            scottie.say "And right now, I don't say so!"
        else:
            scottie.say "No way, [hero.name]!"
            scottie.say "That's like a really private thing to ask!"
            bree.say "Geez, Scottie!"
            bree.say "I'm only asking for it so I can call you!"
            scottie.say "Ah, you say that now, [hero.name]!"
            scottie.say "But what if you sell it to tele-marketers?"
            scottie.say "Once those guys get their claws into you, they never let go!"
        $ scottie.love -= 1
        $ scottie.sub -= 1
    return

label scottie_ask_birthday_female:
    if game.week_day % 2 == 0:
        bree.say "Scottie..."
        bree.say "I was just wondering..."
        bree.say "When is it your birthday?"
    else:
        bree.say "Hey, Scottie..."
        bree.say "When is your birthday?"
        bree.say "In don't want to miss it!"
    if hero.charm >= 40 - scottie.love:
        $ scottie.flags.birthdayknown = True
        if game.week_day % 2 == 0:
            scottie.say "Same day it's always been, [hero.name]."
            scottie.say "Winter 2."
        else:
            scottie.say "Oh yeah!"
            scottie.say "I should totally tell you that, [hero.name]!"
            bree.say "Erm...okay, Scottie - you can tell me now."
            scottie.say "Uh...wait a sec...I forgot it..."
            scottie.say "Oh, here it is, Winter 2 - I keep it on my phone, yeah?"
            scottie.say "Because I forget it a lot!"
    else:
        show scottie angry
        if game.week_day % 2 == 0:
            scottie.say "Hey, [hero.name]!"
            scottie.say "Are you trying to catch me out?"
            scottie.say "I can almost always remember my birthday!"
        else:
            scottie.say "No way, [hero.name]!"
            scottie.say "That's like sensitive information!"
            bree.say "Geez, Scottie!"
            bree.say "I'm not gonna use it to defraud you!"
            scottie.say "Ah, you say that now, [hero.name]!"
            scottie.say "But a guy can never be too careful."
        $ scottie.sub -= 1
        $ scottie.love -= 1
    return

label scottie_ice_cream_reaction_female:
    scottie.say "Hey, [hero.name]..."
    scottie.say "It's ice-cream time!"
    "I look around as Scottie makes the announcement."
    "It comes out of nowhere and takes me totally by surprise."
    bree.say "Huh?"
    bree.say "Oh...that's a great idea, Scottie!"
    bree.say "Let's go!"
    "Together we hurry over to the ice-cream stand."
    "I order my usual ice-cream while Scottie looks on."
    "Then he shakes his head and scoffs."
    scottie.say "What in the hell is that thing supposed to be?"
    bree.say "Hey, Scottie!"
    bree.say "That's my favourite - I always have it!"
    scottie.say "Sounds lame to me!"
    scottie.say "Wait until you check this out..."
    "Scottie proceeds to order his own ice-cream."
    "And he's really specific with the instructions."
    "In fact he seems to be ordering the poor server around the whole time!"
    "When he finally gets his order, her presents it to me like a winner's trophy."
    scottie.say "There you go, [hero.name]."
    scottie.say "Now THAT'S and ice-cream!"
    bree.say "I gotta admit, Scottie - that does look good."
    "Scottie nods and offers it to me for a lick."
    "I do the same, and he hesitates, but then licks mine in turn."
    bree.say "Mmm...that IS good, Scottie!"
    scottie.say "Ah...your's is pretty good too, [hero.name]."
    scottie.say "Obviously not as good as mine - but pretty good all the same..."
    return

label scottie_offer_a_drink_female:
    bree.say "You wanna drink, Scottie?"
    bree.say "I'm running dry here."
    bree.say "So I can grab you one while I get myself another."
    if (hero.charm >= 60 - scottie.love and scottie.flags.drinks < 2) or date_girl == scottie:
        show scottie

        scottie.say "Oh...yeah, [hero.name]!"
        scottie.say "I didn't realise I was done with this one!"
        scottie.say "Can you grab me another of these bad boys?"
        hide scottie
        show drink scottie
        if scottie.love <= 25:
            $ scottie.love += 1
        elif date_girl == scottie and game.active_date:
            $ game.active_date.score += 5
        call expression scottie.get_chat from _call_expression_400
        hide drink scottie
        $ scottie.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show scottie angry
        scottie.say "Oh no, [hero.name]!"
        scottie.say "I don't want someone spiking my drinks!"
        scottie.say "I'll buy my own, thank you very much."
        $ hero.cancel_activity()
        hide scottie
    return

label scottie_slap_ass_intro_female:
    "I think of Scottie as a pretty rough-and-tumble kind of guy."
    "The kind of guy that's not afraid of acting in an old-fashioned, macho kind of way."
    "So I feel pretty safe as I draw back my arm and swing a hand at his ass."
    "It connects with a satisfyingly solid sound."
    "And I have to admit that the feeling is pretty nice too!"
    return

label scottie_slap_ass_happy_female:
    "Scottie turns around, surprise written all over his face."
    scottie.say "Hey!"
    scottie.say "Who did that?!?"
    scottie.say "Was it you, [hero.name]?"
    bree.say "Yeah, Scottie - it was me!"
    "Scottie smirks at me and shakes his head."
    scottie.say "I never thought you had it in you, [hero.name]!"
    scottie.say "I'm gonna have to keep a closer eye on you!"
    "I smile at his reaction, trying not to blush at the same time."
    "Why does the big goof have that kind of effect on me?"
    return

label scottie_slap_ass_angry_female:
    "Scottie turns around, surprise written all over his face."
    scottie.say "Hey!"
    scottie.say "Who did that?!?"
    scottie.say "Was it you, [hero.name]?"
    bree.say "Yeah, Scottie - it was me!"
    "Scottie scowls at me, shaking his head."
    scottie.say "You can't just do stuff like that, [hero.name]!"
    scottie.say "If it's not cool for a guy to do it to you..."
    scottie.say "Then it's not cool for you to do it to a guy either!"
    bree.say "Sorry, Scottie..."
    bree.say "I won't do it again, I promise!"
    return

label scottie_breakup_female:
    bree.say "Ah..."
    bree.say "There's no easy way to say this, Scottie..."
    scottie.say "Huh?"
    scottie.say "Why's that, [hero.name]?"
    scottie.say "Is it in some weird foreign language?"
    "I resist the urge to bury my head in my hands."
    "Instead I force a grim smile onto my face and press on."
    bree.say "No, Scottie..."
    bree.say "I mean I have something heavy to lay on you."
    bree.say "And it's that I think we should stop seeing each other."
    "I pause for a moment, then something occurs to me and I go further."
    bree.say "And by that I mean we should break up, Scottie."
    bree.say "End our relationship, yeah?"
    scottie.say "Sure I known what you mean, [hero.name]."
    scottie.say "What do you think I am, a frickin moron?"
    "I have to bite my tongue to keep from giving the obvious answer."
    bree.say "Stick to the matter at hand, Scottie."
    bree.say "I want to break up with you, okay?"
    scottie.say "I mean, sure, [hero.name] - if that's what you want."
    scottie.say "It's...sniff...nothing to me...snuffle..."
    bree.say "Oh god, Scottie..."
    bree.say "Are you...are you actually crying?"
    scottie.say "Of course not...sniffle..."
    scottie.say "I just have something in my eye!"
    return

label scottie_go_steady_intro_female:
    bree.say "How many dates have we been on now, Scottie?"
    bree.say "Is it four or five - or could it even be half-a-dozen?"
    scottie.say "No way, [hero.name]!"
    scottie.say "We've never been on seven dates!"
    bree.say "Whatever the number, it's a lot - right?"
    "Scottie frowns and nods."
    scottie.say "Yeah, I guess so, [hero.name]!"
    bree.say "Well that's why I was thinking..."
    bree.say "Maybe we should make things a little more...official?"
    "Scottie's face becomes a picture of alarm at this."
    scottie.say "What, like get married or something?"
    bree.say "No, Scottie!"
    bree.say "I meant we could agree to go steady!"
    return

label scottie_go_steady_yes_female:
    "Scottie looks instantly relieved."
    scottie.say "Oh, thank god!"
    scottie.say "Yeah, [hero.name], that sounds good."
    scottie.say "I think I can handle that."
    return

label scottie_go_steady_no_female:
    "My explanation doesn't seem to help calm Scottie down one bit."
    scottie.say "Oh no, [hero.name], no way!"
    scottie.say "Sure, it'll start out as going steady."
    scottie.say "But next thing you'll be trying to pin me down with more and more commitment!"
    bree.say "Erm...okay, Scottie."
    bree.say "Maybe we're just not there yet..."
    return

label scottie_pet_intro_female:
    "Scottie's so dumb and adorable, always full or energy."
    "So much so that I can't help being reminded of a dog."
    "In fact, I just can't help myself from acting on that feeling."
    "And before I know what I'm doing, I pat him on top of the head."
    bree.say "Aww..."
    bree.say "Aren't you a good boy?"
    "Scottie stops what he's doing and stares straight at me."
    scottie.say "Huh?"
    scottie.say "Did you just pat me on the head?"
    scottie.say "And call me a good boy?"
    bree.say "Erm...yeah, Scottie."
    bree.say "I guess I did!"
    return

label scottie_pet_happy_female:
    scottie.say "Oh...that's okay then!"
    "Scottie smiles so broadly that I expect his tongue to hang out of his mouth."
    "Then he scratches himself behind the ear without realising that he's doing it."
    "Part of me wants to throw a stick, just to see what his reaction would be."
    "But in the end, I decide not to push my luck..."
    return

label scottie_pet_annoyed_female:
    scottie.say "Hey!"
    scottie.say "I'm not a dog, you know?"
    bree.say "I know, I know...I'm really sorry, Scottie..."
    "Before I can finish, Scottie's attention is dragged away by something."
    scottie.say "Is...is that a squirrel?!?"
    scottie.say "Watch this, [hero.name]!"
    scottie.say "I bet I can catch it!"
    return

label scottie_massage_intro_female:
    scottie.say "Ah, fuck..."
    scottie.say "Dammit..."
    bree.say "That sounds painful, Scottie!"
    bree.say "You pulled a muscle?"
    scottie.say "Yeah, it's sport-related."
    bree.say "You got it from playing sports?"
    scottie.say "No, I got it from WATCHING sports."
    scottie.say "My team scored and I jumped up to celebrate."
    scottie.say "Next thing I know, something went snap!"
    bree.say "You want me to take a look at it?"
    bree.say "I'm told I give a pretty mean massage!"
    return

label scottie_massage_accept_female:
    scottie.say "Would you, [hero.name]?"
    scottie.say "I'll try anything to get rid of the pain!"
    scottie.say "Just let me take my shirt off..."
    return

label scottie_massage_refuse_female:
    scottie.say "Oh no, [hero.name]!"
    scottie.say "I'm not letting an amateur get their hands on me!"
    scottie.say "You'll only end up making it worse."
    return

label scottie_piercing_nipples_reaction_female:
    bree.say "Whoa, Scottie - that shirt is REALLY tight!"
    scottie.say "Sure it is, [hero.name]."
    scottie.say "But look a little closer!"
    bree.say "Oh my..."
    bree.say "You got them done?"
    scottie.say "Yeah, [hero.name], I got both nipples pierced!"
    scottie.say "You like?"
    "I nod slowly, still staring at Scottie's nipples."
    bree.say "Oh yeah, Scottie..."
    bree.say "I like, I like!"
    scottie.say "Don't worry, [hero.name]..."
    scottie.say "You can get a closer look soon enough!"
    return

label scottie_piercing_navel_reaction_female:
    bree.say "Whoa, Scottie - that shirt is REALLY tight!"
    scottie.say "Sure it is, [hero.name]."
    scottie.say "But look a little closer!"
    bree.say "Oh my..."
    bree.say "You got it done?"
    scottie.say "Yeah, [hero.name], I got my belly button pierced!"
    scottie.say "You like?"
    "I nod slowly, still staring at Scottie's navel."
    bree.say "Oh yeah, Scottie..."
    bree.say "I like, I like!"
    scottie.say "Don't worry, [hero.name]..."
    scottie.say "You can get a closer look soon enough!"
    return

label scottie_piercing_clit_reaction_female:
    bree.say "Whoa, Scottie - those pants are REALLY tight!"
    scottie.say "Sure they are, [hero.name]."
    scottie.say "But look a little closer!"
    bree.say "Oh my..."
    bree.say "You got it done?"
    scottie.say "Yeah, [hero.name], I got my dick pierced!"
    scottie.say "You like?"
    "I nod slowly, still staring at Scottie's crotch."
    bree.say "Oh yeah, Scottie..."
    bree.say "I like, I like!"
    scottie.say "Don't worry, [hero.name]..."
    scottie.say "You can get a closer look soon enough!"
    return

label scottie_piercing_head_reaction_female:
    "Scottie walks up to me with a smile on his face."
    "Then he opens his mouth and sticks out his tongue."
    bree.say "Oh my..."
    bree.say "You got it done?"
    scottie.say "Yeah, [hero.name], I got my tongue pierced!"
    scottie.say "You like?"
    "I nod slowly, still staring at Scottie's tongue."
    bree.say "Oh yeah, Scottie..."
    bree.say "I like, I like!"
    scottie.say "Don't worry, [hero.name]..."
    scottie.say "You can get a closer look soon enough!"
    "Scottie underlines his point by waggling his tongue at me again."
    return

label scottie_movie_liked_reaction_female:
    bree.say "That move was like the BEST...THING...EVER!"
    bree.say "I want to see it again, stream it as soon as I can and own it on DVD!"
    bree.say "I'm right, aren't I, Scottie?"
    scottie.say "Yeah, [hero.name]!"
    scottie.say "I didn't understand some of the words and most of the plot."
    scottie.say "But the explosions and special effects made up for it!"
    return

label scottie_movie_indifferent_reaction_female:
    bree.say "That move was like the BEST...THING...EVER!"
    bree.say "I want to see it again, stream it as soon as I can and own it on DVD!"
    bree.say "I'm right, aren't I, Scottie?"
    scottie.say "I dunno, [hero.name]..."
    scottie.say "I didn't understand some of the words and most of the plot."
    scottie.say "And there weren't enough explosions and special effects to make up for it either!"
    return

label scottie_movie_disliked_reaction_female:
    bree.say "That move was like the BEST...THING...EVER!"
    bree.say "I want to see it again, stream it as soon as I can and own it on DVD!"
    bree.say "I'm right, aren't I, Scottie?"
    scottie.say "No, [hero.name] - it sucked ass!"
    scottie.say "I didn't understand some of the words and most of the plot."
    scottie.say "And where in the hell were all the explosions and special effects?!?"
    return


label scottie_belly_interaction_female:
    $ scottie.set_flag("interact", 1, 1, "+")
    show scottie at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call scottie_belly_kiss_female from _call_scottie_belly_kiss_female_1
        "Caress my belly":
            call scottie_belly_caress_female from _call_scottie_belly_caress_female_1
        "Listen to the baby":
            call scottie_belly_listen_female from _call_scottie_belly_listen_female_1
        "Never mind":
            pass
    return

label scottie_belly_caress_female:
    show scottie happy at center, zoomAt(1.25, (640, 880))
    scottie.say "Hey, [hero.name]..."
    scottie.say "Guess who's here!"
    show scottie normal
    "The moment that I hear Scottie approaching, I start trying to cover myself up."
    "Normally I'm not that conscious of my appearance, and I really wouldn't care."
    "But today I feel like the hormones have totally taken over."
    "And I can't stand the sight of him seeing me when I'm such a mess."
    bree.say "Oh, Scottie..."
    bree.say "Don't look at me!"
    show scottie stuned
    "Scottie, confused by the request, obviously does the exact opposite."
    show scottie at center, traveling(1.5, 0.3, (640, 1040))
    "Walking straight up to me with a look of genuine concern on his face."
    show scottie surprised
    scottie.say "Huh?"
    show scottie shocked
    scottie.say "What's up, [hero.name]?"
    scottie.say "Are you, like, feeling okay?"
    show scottie stuned
    "Okay, so now I have an awkward situation on my hands."
    "I have to somehow explain the fact that hormones are making me crazy."
    "And what's worse is that I have to explain it to Scottie."
    "Who, with the best will in the world, is a bit of an idiot."
    bree.say "It's...it's just the baby, Scottie..."
    bree.say "Like, my body is going crazy right now."
    bree.say "So it means I'm a mess, inside and out!"
    "Scottie frowns, like he really doesn't understand what I mean."
    "Which is pretty much how I expected this to go for me."
    "So I prepare myself for a frustrating and ultimately fruitless discussion with him."
    show scottie talkative
    scottie.say "Whoa..."
    scottie.say "That's pretty heavy, [hero.name]!"
    show scottie normal
    "But it's what Scottie does next that really throws me."
    "Because he put his hand on my belly, totally without asking it."
    "And he proceeds to kind of stroke it as gently as possible."
    show scottie talkative
    scottie.say "Are you listening in there, little guy or gal?"
    scottie.say "Because you've gotta be nicer to your poor mama!"
    scottie.say "After all, she's letting you live inside of her, yeah?"
    scottie.say "And I think that's pretty cool of her."
    show scottie normal
    "Scottie sounds so serious as he says all of this."
    "But at the same time he also sounds so dumb!"
    "It's probably one of the cutest things I've heard in my entire life."
    "He hasn't mentioned how I look once, not to agree or disagree."
    "Instead he's actually trying to talk the baby into being nicer to me!"
    $ scottie.love += 2
    return

label scottie_belly_kiss_female:
    show scottie happy at center, zoomAt(1.5, (640, 1040))
    scottie.say "Hey, [hero.name]..."
    scottie.say "How's being pregnant?"
    scottie.say "You look pretty blown!"
    show scottie normal
    "I can't help feeling a little irritated by Scottie's upbeat tone."
    "And the fact that he's still using it when he can see that I'm in a total state."
    bree.say "Thanks for reminding me of how bad I look and feel, Scottie!"
    bree.say "Is there anything else you want to say to depress me?"
    "If I was expecting Scottie to change his tune, then I'm soon disappointed."
    show scottie happy
    "Because he just looks at me with a big, dumb smile on his face."
    scottie.say "Ah, come on, [hero.name]..."
    scottie.say "It can't be all that bad."
    scottie.say "Not when you've got me here to help out."
    scottie.say "And I think I know just the thing..."
    show scottie normal
    "Before I can say a word in response, Scottie leaps into action."
    show scottie at center, traveling(2.5, 0.3, (640, 1940))
    "He kneels down in front of me, and takes hold of my top."
    "Then he pulls it up to reveal the curve of my belly."
    bree.say "Scottie..."
    bree.say "What are you..."
    bree.say "What are you doing?"
    show scottie happy
    scottie.say "Don't worry, [hero.name]..."
    scottie.say "I know what I'm doing."
    show scottie normal
    bree.say "Really?"
    bree.say "Because I wish I did!"
    "I have no idea if Scottie even hears those last few words."
    "Because he leans forwards as I'm saying them."
    "And then he places his lips against the curve of my belly."
    "Then he's away and kissing it before I can say anything else."
    "I have my lips parted and my tongue all lined up for a lashing."
    "But instead of telling Scottie off, I find myself watching in amazement."
    "Because it doesn't take long for me to feel my mood beginning to change."
    "Somehow the sensation of him planting kisses on my belly seems to help."
    "It actually seems to be improving my mood."
    "Which obviously means that I just stand there and leave him to it."
    "Because I'm not about to so anything to add to my stress levels, am I?"
    "Scottie never even seems to notice what's going on around him."
    "He just keeps right on going, oblivious to his surroundings."
    "Like he's totally convinced that he's doing the right thing."
    "And in this case at least, I guess that he really is."
    $ scottie.love += 3
    return

label scottie_belly_listen_female:
    show scottie talkative at center, zoomAt(1.5, (640, 1040))
    scottie.say "[hero.name], [hero.name]..."
    scottie.say "I have a favour to ask!"
    scottie.say "But you have to promise me you'll say yes, okay?"
    show scottie normal
    "I lift my head as soon as I hear Scottie asking me a question."
    "But then I can't keep my face from twisting into an expression of confusion."
    "Because Scottie just seems to come out with stuff like that."
    "Stuff that makes your head spin as you try to make sense of it."
    bree.say "Whoa, whoa, whoa..."
    bree.say "Back up a little, Scottie."
    bree.say "I'm not agreeing to anything before I know what it is!"
    "Scottie looks at me like he's going to argue."
    "But then he frowns and seems to give up on it just as quickly."
    show scottie happy
    scottie.say "Damn it, [hero.name]..."
    scottie.say "You're always one step ahead!"
    scottie.say "Okay, here it is..."
    scottie.say "I want to listen to the baby!"
    show scottie normal
    "I find myself nodding almost as soon as Scottie asks the question."
    bree.say "That's okay, Scottie..."
    bree.say "You can listen to my belly if you like."
    "Unable to resist the temptation, I put on a sly expression."
    bree.say "But if they say anything to you..."
    bree.say "You have to repeat it back to me, okay?"
    show scottie stuned
    "Scottie stares at me in sheer amazement."
    show scottie surprised
    scottie.say "Do..."
    scottie.say "Do you think they might do that?!?"
    show scottie stuned
    "Oh my god, this guy is too dumb to live!"
    "All I do is shrug as I push my belly towards Scottie."
    "And I have no idea if he really means it or not."
    show scottie at center, traveling(2.5, 0.3, (640, 1940))
    "As he hurries to put his ear to the curve a moment later."
    "I watch with a mounting sense of amusement as Scottie listens for the baby."
    "And sure enough, as soon as he gets the first hint of movement, he's away."
    "I mean, he tries to whisper, but I can still hear him down there."
    show scottie talkative
    scottie.say "Ah..."
    scottie.say "Hey there...hey there, little guy or girl."
    scottie.say "Are you hearing me right how?"
    scottie.say "Like, can you say something to me?"
    show scottie whining
    scottie.say "Fuck, [hero.name]...I don't think they can hear me!"
    show scottie stuned
    "Scottie looks up at me in horror, slapping a hand over his mouth."
    show scottie shocked
    scottie.say "Oh no, I dropped the F-word in front of the baby!"
    scottie.say "If they come out saying that, then it's my fault!"
    show scottie stuned
    "Scottie can't help looking puzzled when I burst out laughing."
    "But I don't know if I have the heart to tell him the truth!"
    $ scottie.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
