label sasha_ice_cream_reaction_male:
    mike.say "It's too damn hot today, Sasha - what we need is ice cream!"
    sasha.say "Sounds good to me - let's go hit the ice cream stand!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Sasha chooses the same thing, but with her own combination of flavours."
    mike.say "Wow...looks like you're enjoying that, Sasha!"
    sasha.say "Hell yeah - nothing comes between this girl and ice cream!"
    "Sasha grins as she begins to lick at her cone, pleasure plain to see on her face."
    "Pretty soon I forget all about my ice cream, only remembering it when it begins to melt."
    "All the time my attention is on Sasha, as she licks and laps at her cone."
    "And my mind is dreaming up other things that she could lick with that tongue too!"
    return

label sasha_ask_phone_male:
    mike.say "Sasha, can I get your number?"
    mike.say "I just realised I don't have it!"
    if hero.charm >= 20 - sasha.love:
        show sasha happy
        $ hero.smartphone_contacts.append("sasha")
        sasha.say "Sure thing, [hero.name]."
        sasha.say "But no fucking dick pics!"
    else:
        show sasha annoyed
        $ sasha.love -= 1
        $ sasha.sub -= 1
        sasha.say "You don't need my number, [hero.name]."
        sasha.say "Just leave me a note on the noticeboard in the hallway!"
    return

label sasha_ask_birthday_male:
    mike.say "Sasha..."
    mike.say "Hey, Sasha..."
    mike.say "When's your birthday?"
    if hero.charm >= 40 - sasha.love:
        show sasha happy
        $ sasha.flags.birthdayknown = True
        sasha.say "Spring 21, [hero.name]."
        sasha.say "So put the date in your diary."
        sasha.say "Because we're gonna party when it comes around!"
    else:
        show sasha annoyed
        $ sasha.sub -= 1
        $ sasha.love -= 1
        sasha.say "Hey, this colour isn't out of a bottle!"
        sasha.say "And anyway, you're even older than me, [hero.name]!"
    return

label sasha_offer_a_drink_male:
    mike.say "Sasha!"
    mike.say "I'm going to the bar."
    mike.say "You want another one?"
    "Almost the second the words are out of my mouth, Sasha turns to face me."
    if sasha.is_visibly_pregnant:
        show sasha angry
        $ sasha.love -= 10
        sasha.say "What the..."
        sasha.say "Are you taking the piss or what?"
        sasha.say "Did you forget that I'm bloody pregnant?!?"
        $ hero.cancel_activity()
        hide sasha
    elif (hero.charm >= 60 - sasha.love and sasha.flags.drinks < 2) or date_girl == sasha:
        show sasha happy
        sasha.say "Geez, I thought you'd never ask!"
        sasha.say "Grab me a rum while you're there."
        sasha.say "And make it a double, okay?"
        hide sasha
        show drink sasha
        if sasha.love <= 25:
            $ sasha.love += 1
        elif date_girl == sasha and game.active_date:
            $ game.active_date.score += 5
        call expression sasha.get_chat from _call_expression_267
        hide drink sasha
        $ sasha.set_flag("drinks", 1, "day", mod="+")
    else:
        show sasha annoyed
        sasha.say "Nope, no way, no thank you!"
        sasha.say "I can look after myself, [hero.name]."
        $ hero.cancel_activity()
        hide sasha
    return

label sasha_slap_ass_intro_male:
    "Sasha looks so good as she's walking along beside me."
    "So good I can't keep my eyes off of her ass."
    "And I can't keep my mind on anything else either!"
    "I want to give it a little slap so badly."
    "Surely she can't begrudge me that?"
    return

label sasha_slap_ass_happy_male:
    sasha.say "Huh!"
    sasha.say "What was that?!?"
    sasha.say "Did you just slap my ass, [hero.name]?"
    "I can't try to pin it on somebody else."
    "So I just nod and wait for Sasha's reaction."
    if sasha.flags.boobjob and sasha.flags.haircut:
        "Sasha giggles and beams at me."
        sasha.say "You can do that anytime you want, [hero.name]!"
    else:
        "Sasha looks at me with a sly grin."
        sasha.say "Okay, [hero.name] - you got away with it this once."
        sasha.say "But don't push your luck!"
    return

label sasha_slap_ass_angry_male:
    sasha.say "Huh!"
    sasha.say "What was that?!?"
    sasha.say "Did you just slap my ass, [hero.name]?"
    "I can't try to pin it on somebody else."
    "So I just nod and wait for Sasha's reaction."
    if sasha.flags.boobjob and sasha.flags.haircut:
        "Sasha begins to pout a moment later."
        sasha.say "Urgh..."
        sasha.say "That's SO mean, [hero.name]!"
    else:
        "Sasha shakes her head at me."
        sasha.say "This is the twenty-first century, [hero.name]."
        sasha.say "And that is NOT cool."
    return

label sasha_breakup_male:
    show sasha
    "I've been dreading this moment since I came to the conclusion it had to happen."
    "I'm one hundred percent sure that it's the right thing to do."
    "But that doesn't make it any easier to actually do the thing."
    "So in the end, I just have to take a deep breath and get on with it..."
    mike.say "Sasha..."
    mike.say "I really need to talk to you about something!"
    "Sasha turns to look me in the eye."
    show sasha annoyed
    "She frowns a little and wrinkles her nose."
    sasha.say "Urgh..."
    sasha.say "That's never a good thing to hear, [hero.name]."
    sasha.say "I'm not going to like this, am I?"
    mike.say "Ah...no, Sasha, you're not."
    mike.say "I think that we need to talk about us."
    mike.say "I...I just don't think this relationship is going anywhere."
    "Sasha lets out a sigh and shakes her head."
    sasha.say "No, you're right, I don't like it!"
    sasha.say "And I don't like how you're tossing what we have away either!"
    "Now it's my turn to shake my head at what Sasha's suggesting."
    mike.say "Hey, Sasha!"
    mike.say "I'm not tossing anything away here!"
    mike.say "I thought about this long and hard, you know?"
    sasha.say "Yeah, I bet you wrestled with your conscience alright."
    sasha.say "But you never once thought of saying a word to me?"
    sasha.say "Never thought we could work it out?"
    sasha.say "No, the first thing I hear about it is that we're over!"
    mike.say "Sasha, I couldn't..."
    sasha.say "For fuck's sake, [hero.name] - we live under the same roof!"
    sasha.say "We must talk to each other a hundred times a day!"
    sasha.say "Well that's going to change for certain."
    sasha.say "If we're over, then you can leave me the hell alone!"
    show sasha angry
    "I keep trying to say my piece, to get a word in edgeways."
    "But Sasha's well and truly on the warpath by now."
    "And she's not about to let me have my say anytime soon."
    sasha.say "Fuck you, [hero.name]!"
    sasha.say "And fuck whatever feelings I used to have for you too."
    sasha.say "Now you're just some pathetic bastard I have to live with!"
    return

label sasha_go_steady_intro_male:
    mike.say "I've been thinking, Sasha..."
    mike.say "We're really great together, you and me."
    mike.say "We should go steady, don't you think?"
    return

label sasha_go_steady_yes_male:
    sasha.say "Yeah, [hero.name], I think so too."
    sasha.say "So if that's what you want."
    sasha.say "We're officially official, okay?"
    return

label sasha_go_steady_no_male:
    sasha.say "Maybe we're doing great BECAUSE we're not official?"
    sasha.say "Did you ever think about that, [hero.name]?"
    sasha.say "Yeah, I know - mind blown!"
    return

label sasha_pet_intro_male:
    "I pat Sasha on the head before I know what I'm doing."
    "And then I almost freeze in place as I realise."
    "I mean, how's a girl like her going to take that?"
    return

label sasha_pet_happy_male:
    sasha.say "Whoa..."
    sasha.say "That was unexpected and a little weird!"
    sasha.say "But I kinda liked it too..."
    return

label sasha_pet_annoyed_male:
    sasha.say "Ah, [hero.name]..."
    sasha.say "You can have that one for free."
    sasha.say "You do it again, and you'll pay for it!"
    return

label sasha_massage_intro_male:
    mike.say "You look like you're in pain, Sasha."
    mike.say "How about you let me take a look at it?"
    mike.say "I'm told I give a really great massage!"
    return

label sasha_massage_accept_male:
    sasha.say "That's some big talk there, [hero.name]!"
    sasha.say "But you're right - I am in pain here."
    sasha.say "So let's see how good you really are..."
    return

label sasha_massage_refuse_male:
    sasha.say "Ah..."
    sasha.say "Nah, [hero.name], you're fine where you are."
    sasha.say "I don't want you making it worse!"
    return

label sasha_piercing_nipples_reaction_male:
    sasha.say "Huh...getting my nipples pierced seems like a no-brainer now!"
    sasha.say "I mean, why in the hell didn't I get one before?"
    sasha.say "But I guess I have you to thank for that, [hero.name]."
    sasha.say "I wonder what other great ideas you can cook up in that head of yours?"
    return

label sasha_piercing_navel_reaction_male:
    sasha.say "I love it, [hero.name]!"
    sasha.say "This was a great idea."
    sasha.say "And it's going to look SO hot with all of my off-cut t-shirts!"
    return

label sasha_piercing_clit_reaction_male:
    sasha.say "I feel like I just got the ultimate heavy metal upgrade, [hero.name]!"
    sasha.say "Nothing says rock and roll louder than having my pussy pierced!"
    sasha.say "But I don't think I'd have found the courage to do it on my own."
    sasha.say "So thanks for that."
    return

label sasha_piercing_head_reaction_male:
    sasha.say "Whoa...my backing vocals are going to sound weird for a while!"
    sasha.say "But it's worth it, because this thing looks so cool!"
    sasha.say "Thanks for talking me into getting it."
    return

label sasha_piercing_nose_reaction_male:
    sasha.say "Now this is what I'm talking about!"
    sasha.say "I love this shit, [hero.name]!"
    sasha.say "So, when are you getting one too?!?"
    return

label sasha_movie_disliked_reaction_male:
    sasha.say "Urgh...that was a massive disappointment - total waste of time!"
    return

label sasha_movie_indifferent_reaction_male:
    sasha.say "BORING...BORING...BORING...put me to sleep!"
    return

label sasha_movie_liked_reaction_male:
    sasha.say "I loved that movie - everything was perfect from start to finish!"
    return

label sasha_belly_kiss_male:
    show sasha normal at center, zoomAt(1.25, (640, 880))
    "I can't help but keep looking at Sasha's belly, poking our from under her shirt."
    "It's just so fascinating to me, for reasons that I really can't begin to explain."
    "Any moment I expect the buttons to just pop right off her shirt."
    "Or for it to start moving, kinda like something out of a horror movie."
    "But most of all, I have the irresistible urge to kiss it."
    "I don't know why, I just want to!"
    "Luckily for me, I don't think Sasha's caught onto my latest obsession yet."
    show sasha shout
    sasha.say "[hero.name]..."
    sasha.say "Is there any particular reason you keep staring at my bump?"
    sasha.say "I mean, it's not getting bigger by the second, is it?"
    show sasha normal
    "I look up, doing the best I can to feign innocence and incredulity."
    mike.say "Was I, Sasha?"
    mike.say "It must have been unconscious, yeah?"
    mike.say "Like, based on how much I love you and the baby."
    show sasha embarrassed
    "Sasha shakes her head at this."
    show sasha shout
    sasha.say "Oh come on, [hero.name]..."
    sasha.say "Is that the best you can do?"
    sasha.say "This is just like before I was pregnant."
    sasha.say "When I'd catch you ogling my chest..."
    sasha.say "And you'd claim it was just for the aesthetic value!"
    show sasha normal
    "I hold up my hands, showing that I surrender."
    mike.say "Okay, Sasha, okay..."
    mike.say "I...I just kinda want to kiss it, that's all."
    mike.say "I know it's weird and I known that you're gonna say no..."
    show sasha shout
    sasha.say "Okay."
    show sasha normal
    "I stop dead, not really believing what I'm hearing."
    mike.say "Sorry..."
    mike.say "Did you just say yes?"
    "Sasha nods as she pulls up her shirt even further."
    show sasha shout
    sasha.say "Yeah, I did."
    sasha.say "Knock yourself out."
    show sasha normal at center, traveling(1.5, 0.3, (640, 880))
    "Keen to take her up on the offer, I kneel down on the floor."
    show sasha at center, traveling(2.0, 5.0, (640, 980))
    "And then I lean in slowly, still afraid this might be a trick."
    "Like Sasha could pull it away any moment, or else barge her belly into my face."
    "But she stays true to her word, remaining still as I pucker my lips."
    "And the next thing I know, I really am kissing her belly."
    "It's warm, smooth and it feels pretty amazing."
    show sasha happy
    "Even more so when I hear Sasha sighing happily above me too."
    return

label sasha_belly_caress_male:
    show sasha annoyed at center, zoomAt(1.25, (640, 880))
    "I watch as Sasha sits down, heaving her belly as she does so."
    "All in all, it looks like the whole thing takes a lot of effort."
    show sasha angry
    sasha.say "Urgh..."
    show sasha vangry
    sasha.say "I feel like a fucking whale!"
    sasha.say "And I guess I look like one too?"
    show sasha upset
    "I'm shaking my head even before Sasha casts a glance in my direction."
    "On the one hand because I might see myself as a modern, honest guy."
    "I'm still not dumb enough to agree with any woman calling herself fat!"
    "And on the other because I genuinely don't agree with what Sasha's saying."
    "To me she looks amazing, like she's glowing from the pregnancy."
    "But again, I know that she's probably not just fishing for compliments right now."
    mike.say "If a whale looked as cute as you do, Sasha..."
    mike.say "Well..."
    mike.say "Let's just say it'd be the hottest whale in the world!"
    show sasha happy
    sasha.say "Hah!"
    show sasha joke
    sasha.say "You're really scraping the bottom of the barrel, huh?"
    sasha.say "But don't worry, I appreciate the effort!"
    show sasha normal
    "Sasha kind of pushes her belly out towards me as she says this."
    "A gesture that I choose to take as an invitation on her part."
    show sasha at center, traveling(1.5, 0.3, (640, 1040))
    "So I reach out and place a hand on the curve of her belly."
    "As usual, it feels soft, warm and very inviting."
    "And as I run my hand gently over it, the sensation seems to calm Sasha."
    show sasha happy
    "She leans back in her chair, closing her eyes and letting out a long sigh."
    sasha.say "Ahh..."
    sasha.say "Sometimes I don't want anyone touching me at all."
    sasha.say "But the moment you put your hand on that thing..."
    sasha.say "I dunno, it's almost like my body knows it's you."
    sasha.say "And the baby too - they both just chill the fuck out!"
    mike.say "So you're saying that I'm good for your health?"
    mike.say "Is that it?"
    show sasha normal
    "Sasha's eyes pop open at this, and she fixes me with an ironic stare."
    show sasha shout
    sasha.say "I wouldn't go reading too much into that, [hero.name]."
    sasha.say "My brain's soaked in pregnancy hormones right now."
    sasha.say "So for all I know, I could just be babbling and making no sense!"
    return

label sasha_belly_listen_male:
    show sasha happy at center, zoomAt(1.25, (640, 880))
    pause 0.1
    show sasha at center, traveling(1.5, 0.3, (640, 1040))
    "I reach out my hands and place them on Sasha's belly, enjoying the sensation of how it feels."
    "And Sasha seems to be liking the fact that I'm touching it too, as she has a huge smile on her face."
    "But there's something that's bugging me right now, something that her belly really reminds me of."
    "The it hits me, and I smile as I begin to gently pat my hands on the curve of Sasha's belly."
    show sasha annoyed
    "She frowns as she strains to see what I'm doing."
    show sasha shout
    sasha.say "Hey!"
    sasha.say "What's the big idea?"
    sasha.say "You be careful with that thing!"
    show sasha normal
    mike.say "You know that I always am, Sasha!"
    mike.say "But I just can't resist it."
    mike.say "Your belly reminds me of a big, round drum."
    mike.say "So I want to see if I can get a tune out of you!"
    show sasha stuned
    "Sasha's eyes go wide and her eyebrows shoot up."
    show sasha surprised
    sasha.say "I can't believe you'd say that about me, [hero.name]..."
    sasha.say "I'm a musician, I play a musical instrument."
    sasha.say "I don't want to be used as one myself!"
    show sasha sad
    "I'm about to say something in return."
    "Probably an attempt to mollify Sasha and reassure her I'm joking."
    "But then I feel the sensation of something moving inside of her."
    mike.say "Whoa..."
    mike.say "Sasha, did you eat something spicy for lunch?"
    show sasha whining
    sasha.say "No, I didn't!"
    show sasha sad
    mike.say "Then that has to be the baby moving in there..."
    mike.say "Like...like they're responding to my drumming!"
    show sasha surprised at center, traveling(2.0, 1.0, (640, 980))
    "I take away my hands and lean in closer, putting an ear to the side of Sasha's belly."
    "Again she's straining to see what I'm doing, hampered by her own body."
    sasha.say "You're no drummer, [hero.name]..."
    sasha.say "You can barely play the damn guitar!"
    sasha.say "Anyway, can a baby really respond to something like that?"
    mike.say "I have no idea, Sasha..."
    mike.say "But if there's even a chance of it, then I want to see!"
    mike.say "Well...I mean...I want to hear..."
    "I shut my mouth then and just listen, waiting as patiently as I can manage."
    "And soon enough I'm rewarded with the sound of something moving in there."
    mike.say "There you go, Sasha..."
    mike.say "They moved, and I think it's because they liked my drumming too."
    show sasha normal
    sasha.say "Yeah, well I think at least one of us is going crazy!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
