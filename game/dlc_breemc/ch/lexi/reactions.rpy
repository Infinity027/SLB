label lexi_ask_birthday_female:
    bree.say "Oh, Lexi..."
    bree.say "I meant to ask - when's your birthday?"
    if hero.charm >= 40 - lexi.love:
        show lexi happy
        $ lexi.flags.birthdayknown = True
        lexi.say "Erm..."
        lexi.say "Let me think about it..."
        lexi.say "It's Summer 5, I think!"
    else:
        show lexi annoyed
        lexi.say "Geez, [hero.name]..."
        lexi.say "What is this, a fucking interrogation?"
        lexi.say "If I wouldn't tell the police, then I'm not telling you!"
        $ lexi.sub -= 1
        $ lexi.love -= 1
    return

label lexi_ice_cream_reaction_female:
    "I hurry over to the ice-cream stand and order my usual cone."
    "And then I stand and watch as it comes together, sprinkles, sauce and all!"
    "I can see Lexi eyeing up the cone just like me, staring with naked admiration."
    lexi.say "Ooh..."
    lexi.say "I need to get me one of those!"
    "I smile and nod, happy to indulge Lexi."
    bree.say "Make that two, okay?"
    "The server nods and starts to work on a second cone."
    "But not before they had me the first one."
    "Hold it up for Lexi to see, brandishing it like a trophy."
    bree.say "Looking good, huh?"
    bree.say "You want a lick?"
    "Lexi nods eagerly."
    lexi.say "Oh yeah!"
    lexi.say "My tongue's already tingling!"
    "Lexi and I take turns at licking the cone until hers is ready."
    "And then we walk away together, tongues working overtime."
    return

label lexi_ask_phone_female:
    bree.say "Can I get your phone number, Lexi?"
    bree.say "I was just looking through my phone."
    bree.say "And I realised that I don't have it!"
    if hero.charm >= 20 - lexi.love:
        show lexi happy
        $ hero.smartphone_contacts.append("lexi")
        lexi.say "You don't?"
        lexi.say "That's weird - I thought I gave it to your already!"
        lexi.say "No worries...here you go..."
    else:
        show lexi annoyed
        lexi.say "Yeah well..."
        lexi.say "If you don't have it, then I don't want you to have it!"
        lexi.say "Sorry, but that's how it is, [hero.name]."
        $ lexi.love -= 1
        $ lexi.sub -= 1
    return

label lexi_offer_a_drink_female:
    bree.say "I'm going to grab a drink, Lexi."
    bree.say "Can I get you one too?"
    bree.say "It's no problem!"
    if (hero.charm >= 60 - lexi.love and lexi.flags.drinks < 2) or date_girl == lexi:
        show lexi happy
        lexi.say "Oh yeah!"
        lexi.say "That'd be great, [hero.name]."
        lexi.say "I'll have the same again."
        hide lexi
        show drink lexi
        if lexi.love <= 25:
            $ lexi.love += 1
        elif date_girl == lexi and game.active_date:
            $ game.active_date.score += 5
        call expression lexi.get_chat from _call_expression_395
        hide drink lexi
        $ lexi.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show lexi annoyed
        lexi.say "What the hell?"
        lexi.say "You think I can't afford my own drinks or something?"
        lexi.say "Geez...that's SO typical!"
        $ hero.cancel_activity()
        hide lexi
    return

label lexi_slap_ass_intro_female:
    "I know that it's kind of wrong, something I really shouldn't do."
    "But the moment Lexi stands up, I can't take my eyes off her ass."
    "It's just so round, perfect and inviting - have to touch it!"
    "That's how I end up swinging my hand towards her butt a moment later."
    "Then I hear the unmistakable sound of it making contact."
    "And Lexi jumps forwards, yelping in surprise!"
    return

label lexi_slap_ass_happy_female:
    lexi.say "Whoa..."
    lexi.say "Did you just..."
    "Lexi regards me with a wry smile on her face."
    lexi.say "Oh, [hero.name]...you'd better know what you're starting here!"
    return

label lexi_slap_ass_angry_female:
    lexi.say "What the hell..."
    lexi.say "[hero.name]...did you just slap my ass?!?"
    "Lexi glares at me, a look of sheer annoyance on her face."
    lexi.say "Do it again and I'll break your wrist!"
    return

label lexi_breakup_female:
    show lexi
    "I take a deep breath and steel myself for what I'm about to say."
    "Nobody wants to hear it, and I really don't want to say it."
    "But I can't just keep on bottling it up inside either."
    bree.say "Lexi..."
    bree.say "We need to talk..."
    lexi.say "Sure thing, [hero.name]!"
    lexi.say "What do you want to talk about?"
    bree.say "No, Lexi..."
    bree.say "I mean we need to talk about US!"
    "A look of recognition spreads over Lexi's face."
    show lexi sad
    lexi.say "Oh..."
    lexi.say "Okay..."
    bree.say "I think we need to call it a day, Lexi."
    return

label lexi_go_steady_intro_female:
    "I take a deep breath and steel myself for what I'm about to say."
    "I'm feeling pretty scared at going out on a limb like this."
    "But I just know that I'll regret it if I don't step up and speak up."
    bree.say "Lexi..."
    lexi.say "Yeah, [hero.name]..."
    bree.say "We're getting on great, aren't we?"
    lexi.say "Erm...yeah, [hero.name]..."
    lexi.say "I think we're pretty good together!"
    bree.say "So..."
    bree.say "What would you say to us making it official?"
    bree.say "You know, like going steady?"
    return

label lexi_go_steady_yes_female:
    lexi.say "Oh yeah, [hero.name]..."
    lexi.say "Why didn't I think of that already!"
    lexi.say "I think that's a great idea!"
    return

label lexi_go_steady_no_female:
    lexi.say "Urgh..."
    lexi.say "We were getting on, [hero.name] - until you went and ruined it!"
    lexi.say "Guys are right, why do girls always want to complicate things?"
    return

label lexi_pet_intro_female:
    "I don't know where the urge comes from, it just kind of pops into my head."
    "I take one look at Lexi, and I can't help it, she's just so cute and sexy!"
    "Before I can stop myself, I reach up and pat her on the head like she's a dog!"
    "Lexi's eyes pop open in surprise, and she looks at me like she's lost for words."
    "All I can so is shrug and smile, already starting to sweat under her gaze."
    return

label lexi_pet_happy_female:
    lexi.say "What are you patting me on the head for, [hero.name]?"
    lexi.say "There's a whole bunch of places that's be more fun."
    lexi.say "Try patting me there instead, okay?"
    return

label lexi_pet_annoyed_female:
    lexi.say "What the hell are you doing, [hero.name]?"
    lexi.say "I'm not your damn pet!"
    lexi.say "So don't treat me like I am, okay?!?"
    return

label lexi_massage_intro_female:
    bree.say "Ooh...ouch!"
    bree.say "That looks pretty painful, Lexi."
    lexi.say "Yeah, yeah..."
    lexi.say "I pulled it a while back and it never really got better."
    bree.say "You want me to give you a massage?"
    bree.say "I've been told I have magic hands!"
    return

label lexi_massage_accept_female:
    lexi.say "That sounds good, [hero.name]."
    lexi.say "I could use some help with it."
    lexi.say "When can you fit me in?"
    return

label lexi_massage_refuse_female:
    lexi.say "Oh no...no way!"
    lexi.say "I don't need anyone making it worse."
    lexi.say "I need to get my ass to a professional."
    return

label lexi_piercing_nipples_reaction_female:
    "I spot them almost as soon as I lay eyes on Lexi."
    "I mean, it's no wonder, as she hardly covers herself up!"
    "In fact I can see every detail of them through her skimpy top."
    lexi.say "You spotted them, right?"
    lexi.say "I finally went and got it done."
    bree.say "Piercings?"
    lexi.say "You bet, [hero.name]!"
    lexi.say "Both nipples!"
    "I nod slowly, unable to tear my eyes away from them."
    "I'm already wondering what those things must feel like."
    "And what they'd feel like if I could get my hands on them."
    bree.say "Looks great, Lexi!"
    bree.say "You need help trying them out?"
    "Lexi lets out a peal of filthy laughter."
    "And then she shoots me a wink."
    lexi.say "I thought you'd never ask!"
    return

label lexi_piercing_navel_reaction_female:
    "I spot it almost as soon as I lay eyes on Lexi."
    "I mean, it's no wonder, as she hardly covers herself up!"
    "In fact I can see it perfectly as her belly is bare."
    lexi.say "You spotted it, right?"
    lexi.say "I finally went and got it done."
    bree.say "A piercing?"
    lexi.say "You bet, [hero.name]!"
    lexi.say "Check out my belly button!"
    "I nod slowly, unable to tear my eyes away from it."
    "I'm already wondering what it must feel like."
    "And what it'd feel like if I could get my hands on it."
    bree.say "Looks great, Lexi!"
    bree.say "You need help trying it out?"
    "Lexi lets out a peal of filthy laughter."
    "And then she shoots me a wink."
    lexi.say "I thought you'd never ask!"
    return

label lexi_piercing_clit_reaction_female:
    "There's something odd about the way Lexi's walking."
    "Like something's different below her waist."
    lexi.say "You spotted it, right?"
    lexi.say "I finally went and got it done."
    bree.say "A piercing?"
    lexi.say "You bet, [hero.name]!"
    lexi.say "Wait until you see my pussy!"
    "I nod slowly, unable to tear my eyes away from Lexi's groin."
    "I'm already wondering what it must feel like."
    "And what it'd feel like if I could get my hands on it."
    bree.say "Sounds great, Lexi!"
    bree.say "You need help trying it out?"
    "Lexi lets out a peal of filthy laughter."
    "And then she shoots me a wink."
    lexi.say "I thought you'd never ask!"
    return

label lexi_piercing_head_reaction_female:
    "Lexi sticks her tongue out the moment that she sees me."
    "And I see that there's something new in the middle of it."
    "I can't be sure from this angle, but it looks like a piercing."
    lexi.say "You spotted it, right?"
    lexi.say "I finally went and got it done."
    bree.say "A piercing?"
    lexi.say "You bet, [hero.name]!"
    lexi.say "Check out my tongue!"
    "I nod slowly, unable to tear my eyes away from it."
    "I'm already wondering what it must feel like."
    "And what it'd feel like if I could wrap my own tongue around it."
    bree.say "Looks great, Lexi!"
    bree.say "You need help trying it out?"
    "Lexi lets out a peal of filthy laughter."
    "And then she shoots me a wink."
    lexi.say "I thought you'd never ask!"
    return

label lexi_movie_liked_reaction_female:
    bree.say "Wow..."
    bree.say "That was SUCH a great movie!"
    bree.say "Don't you think, Lexi?"
    lexi.say "You bet, [hero.name]!"
    lexi.say "I was jumping out of my seat the whole time!"
    lexi.say "We gotta go see it again!"
    return

label lexi_movie_indifferent_reaction_female:
    bree.say "Wow..."
    bree.say "That was SUCH a great movie!"
    bree.say "Don't you think, Lexi?"
    lexi.say "Aah..."
    lexi.say "I dunno, [hero.name]..."
    lexi.say "It was kind of average, you know?"
    return

label lexi_movie_disliked_reaction_female:
    bree.say "Wow..."
    bree.say "That was SUCH a great movie!"
    bree.say "Don't you think, Lexi?"
    lexi.say "Urgh..."
    lexi.say "You have NO taste, [hero.name]!"
    lexi.say "That film was such a pile of garbage!"
    return

label lexi_abortion_reaction_female:
    lexi.say "Hey, [hero.name]..."
    lexi.say "Wait up!"
    "I turn to see Lexi hurrying towards me."
    "And my immediate instinct is to do the exact opposite."
    "I'm just not in the kind of mood where I can be chatty."
    "But it looks like I'm not going to get a choice."
    "So I do the best I can to force a smile onto my face."
    bree.say "Oh..."
    bree.say "Hey, Lexi!"
    "Even as she catches up to me, I can see where this is going."
    "From the way Lexi's studying me with interest, I just know it."
    lexi.say "Wait a minute, [hero.name]..."
    lexi.say "Something's different about you..."
    lexi.say "You...you're not pregnant anymore!"
    "I let out a weary sigh and nod."
    "I don't want to have this conversation right now."
    "But there's no way of getting around it that I can see."
    bree.say "No, Lexi..."
    bree.say "I decided that I couldn't do it."
    bree.say "So I...I had a termination."
    if lexi.love >= 150:
        "Lexi surprises me by nodding and looking sympathetic."
        "I'd been expecting her to lecture me about it."
        "Maybe even harangue me about the sanctity of human life."
        lexi.say "That must have been hard, [hero.name]."
        lexi.say "I know more than a few girls from my time on the streets..."
        lexi.say "They wound up in the same mess as you did."
        lexi.say "And they did the same thing too."
        lexi.say "Wasn't easy for a single one of them."
        "I nod, genuinely grateful for Lexi's kind words."
        bree.say "Thanks, Lexi."
        bree.say "Most people don't see it that way."
        bree.say "They seem to think I'm some kind of monster!"
        "Lexi shakes her head at this."
        lexi.say "Nah, [hero.name]..."
        lexi.say "You're just someone that had to make a hard decision."
        lexi.say "That's all."
    else:
        "Lexi frowns and shakes her head at me."
        "And I can feel the lecture coming even before it starts."
        lexi.say "You did, huh?"
        lexi.say "Well I know more than a few girls from my time on the streets..."
        lexi.say "They wound up in the same mess as you did."
        lexi.say "Difference is they toughed it out."
        lexi.say "I guess they were just made of harder stuff than you!"
        "Now it's my turn to frown."
        bree.say "I don't need to be lectured by you, Lexi!"
        bree.say "This was my decision to make."
        bree.say "And it was only going to affect my life!"
        lexi.say "Sure, [hero.name], sure."
        lexi.say "The kid's life doesn't count - does it?"
        "I roll my eyes and turn my back on Lexi."
        "I don't need this right now."
        "But my walking away doesn't shut her up."
        lexi.say "What's the matter, [hero.name]?"
        lexi.say "Can't talk your way out of that one?"
    return


label lexi_belly_interaction_female:
    $ lexi.set_flag("interact", 1, 1, "+")
    show lexi at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call lexi_belly_kiss_female from _call_lexi_belly_kiss_female_1
        "Caress my belly":
            call lexi_belly_caress_female from _call_lexi_belly_caress_female_1
        "Listen to the baby":
            call lexi_belly_listen_female from _call_lexi_belly_listen_female_1
        "Never mind":
            pass
    return

label lexi_belly_caress_female:
    show lexi normal nophone at center, zoomAt(1.5, (640, 1040))
    lexi.say "Ooh..."
    lexi.say "Pregnant bellies are SO hot!"
    lexi.say "Lemmie get my hands on that thing!"
    show lexi smile
    "I look up to be greeted with the sight of hands reaching out towards me."
    "Finger and thumbs flexing as they try to grab hold of me."
    "And all of the zombie films that I ever watched suddenly come back to haunt me."
    with vpunch
    bree.say "Aargh..."
    bree.say "Get away from me!"
    show lexi surprised
    "I've thrown up my own arms and backed off a good couple of metres before I snap out of it."
    "Before I realise that this is Lexi being way too forward, rather than zombies out to get me."
    show lexi angry
    lexi.say "Geez, [hero.name]..."
    lexi.say "I only wanted to touch your bump!"
    show lexi sad
    bree.say "Oh yeah..."
    bree.say "Sorry, Lexi..."
    bree.say "You kind of took me by surprise there."
    show lexi smile
    "Lexi waits for a moment, looking at me like she's waiting for something."
    "And then I realise what it is."
    bree.say "Oh..."
    bree.say "Okay, Lexi..."
    bree.say "I guess it's okay for you to touch it."
    "I put a smile on my face as I pull up my top."
    "But my eyes soon go wide as Lexi practically pounces on my belly."
    "Seriously, most people put a hand on the curve."
    "At the most they kind of stroke it gently."
    "Lexi just pounces on it, grabbing my belly with both hands."
    "And then she's all over it, rubbing and stroking it all over."
    "Then she starts making noises too."
    lexi.say "Mmm..."
    show lexi normal
    lexi.say "Oh yeah..."
    lexi.say "Aah..."
    show lexi happy
    lexi.say "Now that's what I'm talking about!"
    show lexi smile
    "I can't help looking around as Lexi continues to caress my belly."
    "Feeling my cheeks flush with colour at the thought of anyone else seeing her."
    "I mean, I'm not being a prude here, am I?"
    "She is kind of touching my belly like it's..."
    "Well, like it's something that she's finding kind of kinky?"
    bree.say "Erm..."
    bree.say "Lexi..."
    bree.say "Are you almost done down there?"
    bree.say "Because my belly's getting kind of cold."
    "I know that's a really lame excuse, but it's the best I can come up with."
    "And luckily for me, it seems to do the trick."
    show lexi flirt
    "Because Lexi pops back up a moment later, a huge smile on her face."
    "The only problem is that I think it's the kind of smile she has when she's horny!"
    "But there's no way I can think of an excuse to make her take a cold shower."
    $ lexi.love += 2
    return

label lexi_belly_kiss_female:
    show lexi happy nophone at center, zoomAt(1.25, (640, 880))
    lexi.say "Hey, [hero.name]..."
    lexi.say "You mind if I give you a little kiss?"
    show lexi smile
    "I look around to see that Lexi's giving me a naughty smile."
    show lexi wink
    "And when she adds a wink into the mix..."
    "Well, I can hardly say no after that!"
    show lexi smile
    bree.say "Of course you can, Lexi..."
    bree.say "That sounds really nice!"
    "Lexi gives me a nod."
    show lexi at center, traveling(1.5, 0.3, (640, 1040))
    "And then she starts walking over to where I'm standing."
    scene expression f"bg {game.room}" at blur(16), dark, dark with wipedown
    "So I close my eyes and pucker up my lips."
    "Just waiting for the sensation of hers pressing against them."
    "But then I find myself waiting just a little too long for it to happen."
    "And I can feel someone fiddling with my top too."
    scene expression f"bg {game.room}" with wipeup
    "So I open one eye and try to look around, to see what's happening."
    "Though it's not until I look down that I see what's actually going on."
    show lexi happy at center, zoomAt(1.5, (640, 1240)) with dissolve
    "Lexi's kneeling in front of me, and she's pulling up my top too!"
    "With both eyes now open, I try to find out what she's up to."
    bree.say "Lexi..."
    bree.say "What are you..."
    bree.say "Oh...oh my!"
    show lexi at center, traveling(2.5, 0.3, (640, 1940))
    "Before I can finish what I was going to say, Lexi starts kissing my belly."
    "And she's not being gentle about it either, not holding back at all."
    "Instead I feel the sensation of her lips travelling all over my bump."
    "And I can see Lexi really laying in the smooches too!"
    "Just now I was all ready to tell Lexi that I wanted her stop."
    "That she was being weird and I was getting freaked out."
    "Buy the more she kisses me down there, the more I find myself liking it."
    "So in the end, I just decide that the best thing is to leave her to it."
    "Relaxing and letting the experience wash over me, I do just that."
    "And luckily for me, Lexi doesn't seem to be in any danger of getting bored."
    "Once she's done a complete tour of my belly, she just starts over again."
    "And the second time around is easily better than the first."
    "All of which makes me want her to keep right on going."
    "As well as wondering if I can convince her to do it again in the future."
    $ lexi.love += 3
    return

label lexi_belly_listen_female:
    show lexi smile nophone at center, zoomAt(1.25, (640, 880))
    bree.say "Ooh..."
    bree.say "Someone's lively today!"
    bree.say "They're full of life and energy."
    show lexi happy at startle
    "Lexi let's out a chuckle and nods her head at this."
    show lexi normal
    lexi.say "HA!"
    lexi.say "Oh yeah, [hero.name]..."
    lexi.say "I'm totally on fire today."
    lexi.say "I feel like I could climb a mountain!"
    show lexi smile
    "I give Lexi a puzzled frown as I point down to my belly."
    bree.say "Erm..."
    bree.say "I was talking about the baby, Lexi."
    bree.say "They're really moving around in there today."
    "I'm expecting Lexi to be a little embarrassed at the misunderstanding."
    "Or maybe get a little sulky, which would probably be more in character for her."
    show lexi at center, traveling(2.5, 0.3, (640, 1940))
    "But instead she surprises me by instantly bending over and leaning towards my bump."
    "And before I know what's happening, Lexi has her ear pressed to it!"
    show lexi happy
    lexi.say "Oh wow..."
    lexi.say "I see what you mean, [hero.name]..."
    lexi.say "There's some serious action going down in there."
    show lexi smile
    "I nod and smile as I watch Lexi following the baby's movements."
    "And all the time she's doing it, I'm waiting for her to say something."
    "Like, she's taken the massive liberty of putting her ear to my belly."
    "And she hasn't asked my permission even once."
    "So at the very least she could clue me in on what she's hearing."
    bree.say "Erm..."
    bree.say "Lexi..."
    bree.say "Can you actually hear anything down there?"
    bree.say "Or are you just using me to warm your ear up?"
    "Lexi waves a hand in the air, as if she wants me to be quiet."
    show lexi bored
    lexi.say "Shhh..."
    show lexi sadsmile
    lexi.say "I can't hear a thing with you talking so loud!"
    show lexi smile
    "I'm about to say something in response to that."
    "Something about being offended by Lexi's attitude."
    "But then she starts talking again."
    show lexi normal
    lexi.say "Oh yeah, I can hear something now!"
    lexi.say "They're really going for it, [hero.name]..."
    lexi.say "Kicking and turning around like crazy in there."
    lexi.say "I don't know how you can stand it..."
    show lexi happy
    lexi.say "You must feel like a bouncy castle or something!"
    $ lexi.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
