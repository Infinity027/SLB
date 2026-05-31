label angela_ask_birthday_female:
    bree.say "Angela..."
    bree.say "I know this is kind of an awkward question..."
    bree.say "But when is your actual birthday?"
    if hero.charm >= 40 - angela.love:
        show angela happy
        "Angela smiles and shakes her head like it's no big deal."
        angela.say "Oh, didn't I tell you that already, [hero.name]?"
        angela.say "It's Summer 17, just so you know."
        $ angela.flags.birthdayknown = True
    else:
        show angela annoyed
        "Angela frowns, her lips pressed into a hard line."
        angela.say "Hmm..."
        angela.say "If I wanted you to know, I'd have told you already."
        angela.say "You know, [hero.name], there are some things you should never ask a lady!"
        $ angela.sub -= 1
        $ angela.love -= 1
    return

label angela_ice_cream_reaction_female:
    "I order an ice-cream cone with all the trimmings, eyeing it all the time they're putting it together."
    "But I can see that there's something bothering Angela as she watches the toppings pile up."
    bree.say "What's the matter, Angela?"
    bree.say "Don't you like ice-cream?"
    angela.say "Oh no, [hero.name] - I really love it."
    angela.say "I just never let myself eat it in the past."
    angela.say "I always felt like I had to watch my figure, you know?"
    bree.say "Aw, don't worry about that, Angela - have some fun and live a little!"
    bree.say "Hey, ice-cream guys, give me another one of those cones!"
    "Before Angela can object, I grab the first cone and place it in her hand."
    "She gives me a nervous smile and licks at it gingerly."
    "As soon as I have the second cone, I attack it with my tongue."
    "All the time I'm looking Angela in the eye, trying to encourage her."
    "Eventually it works and she begins to lick with more conviction."
    "And soon enough we're both devouring the cones, grinning like kids on a sugar-rush."
    return

label angela_ask_phone_female:
    bree.say "Hey, Angela..."
    bree.say "I wondered if I could get your number?"
    bree.say "I think we're there, aren't we?"
    if hero.charm >= 20 - angela.love:
        show angela happy
        $ hero.smartphone_contacts.append("angela")
        "Angela nods and smiles, already reaching for her phone."
        angela.say "Of course, [hero.name]!"
        angela.say "I was going to ask for your's too."
    else:
        show angela annoyed
        "Angela shakes her head, frowning a little too."
        angela.say "I don't think so, [hero.name]."
        angela.say "No...we're not quite there yet."
        $ angela.love -= 1
        $ angela.sub -= 1
    return

label angela_offer_a_drink_female:
    bree.say "I'm going to grab myself a cold one, Angela."
    bree.say "Can I get something for you too?"
    if (hero.charm >= 60 - angela.love and angela.flags.drinks < 2) or date_girl == angela:
        show angela happy
        "Angela's face brightens at offer of a drink."
        angela.say "Oh, [hero.name]..."
        angela.say "That's so thoughtful of you!"
        angela.say "I'd love a drink, thank you."
        hide angela
        show drink angela
        if angela.love <= 25:
            $ angela.love += 1
        elif date_girl == angela and game.active_date:
            $ game.active_date.score += 5
        call expression angela.get_chat from _call_expression_387
        hide drink angela
        $ angela.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show angela annoyed
        "Angela gives me a polite smile, but she shakes her head at the same time."
        angela.say "Thank you for the offer, [hero.name]."
        angela.say "But I'm fine right now, really I am."
        $ hero.cancel_activity()
        hide angela
    return

label angela_slap_ass_intro_female:
    "I can't take my eyes off Angela's butt!"
    "It's pretty big and really round."
    "But it's SO cute, I just love it!"
    "In fact, I love it so much that I can't help myself."
    "Before I know what's happening, my hand slaps her buttocks!"
    return

label angela_slap_ass_happy_female:
    angela.say "Whoa!"
    angela.say "[hero.name]...well I never!"
    "Angela's cheeks flush red and she looks shocked."
    "But I can see from the look in her eyes that she likes it!"
    return

label angela_slap_ass_angry_female:
    angela.say "What the hell!"
    angela.say "Did you...did you actually just slap my ass?!?"
    bree.say "Uh...yeah...I guess..."
    angela.say "Urgh...don't ever do that to me again!"
    return

label angela_breakup_female:
    bree.say "Ah, Angela..."
    angela.say "Oh yes, [hero.name]?"
    bree.say "I kinda have something I need to tell you..."
    angela.say "Oh dear..."
    angela.say "That doesn't sound very good, [hero.name]!"
    bree.say "Yeah...there's no easy way to say this, Angela."
    bree.say "But I don't think this is working out - us, I mean."
    bree.say "In fact, I think we should stop seeing each other."
    "Angela looks genuinely shocked, like she's not prepared to hear me say such a thing."
    "All of which makes me saying those words and sticking to them that much harder."
    angela.say "Oh...okay, [hero.name]."
    angela.say "If that's what you think is for the best?"
    bree.say "I...I do, Angela."
    bree.say "I think we should do it now too, so we can maybe stay friends."
    "Angela nods sadly, as if she knows that nothing of the sort is going to happen."
    return

label angela_go_steady_intro_female:
    bree.say "Angela..."
    bree.say "I have something I wanted to ask you..."
    "Angela turns to look me in the eye."
    "It's like she senses how nervous I am from the tone of my voice."
    angela.say "Go ahead, [hero.name]."
    angela.say "I'm listening."
    bree.say "Well..."
    bree.say "We're getting on pretty well, right?"
    bree.say "So I wondered if you wanted to make it official between us?"
    bree.say "You know, like go steady?"
    return

label angela_go_steady_yes_female:
    "Angela smiles and nods the moment I get the words out."
    angela.say "Of course I would, [hero.name]!"
    angela.say "I kind of assumed we already were."
    angela.say "But I'm happy to make it official too!"
    return

label angela_go_steady_no_female:
    "Angela smiles, but she shakes her head slowly."
    angela.say "Aww..."
    angela.say "That's so sweet of you, [hero.name]!"
    angela.say "But I just don't think we're there yet."
    bree.say "Oh...okay, Angela - if you say so."
    return

label angela_pet_intro_female:
    "Angela's pretty tall for a woman, maybe even a little taller than me."
    "So when I see her sitting down, it feels odd to be towering over her."
    "But she looks so cute down there, I can't help taking advantage."
    "And it's not like I'm doing anything bad - just patting her on the head!"
    return

label angela_pet_happy_female:
    angela.say "Oh..."
    angela.say "Hey, [hero.name]!"
    "Angela smiles up at me, her eyes full of adoration."
    "Obviously she liked what I just did to her."
    return

label angela_pet_annoyed_female:
    angela.say "Hey!"
    angela.say "What do you think you're doing?!?"
    "Angela glares up at me, obviously annoyed at what I just did."
    bree.say "Erm...sorry, Angela."
    bree.say "I promise I won't do that again."
    return

label angela_massage_intro_female:
    bree.say "Angela..."
    bree.say "You seem a little stiff."
    bree.say "Like you're in pain, you know?"
    "Angela nods at this, but then she winces."
    angela.say "Ooo...ouch!"
    angela.say "Yes, [hero.name]..."
    angela.say "I must have pulled something without realising it!"
    bree.say "I could maybe give you a massage, if you like?"
    return

label angela_massage_accept_female:
    angela.say "Would you, [hero.name]?"
    angela.say "Oh, you're an angel!"
    angela.say "How soon can you fit me in?"
    return

label angela_massage_refuse_female:
    angela.say "Thank you for the offer, [hero.name]."
    angela.say "But I really think I need to see a professional!"
    return

label angela_piercing_nipples_reaction_female:
    bree.say "Whoa, Angela!"
    bree.say "I see you went ahead and got those piercings!"
    "Angela blushes at the mere mention of the subject."
    "She looks left and right like it's some kind of secret."
    angela.say "Y..yes, [hero.name] - I did."
    angela.say "But how did you know?"
    bree.say "Erm...that's a pretty tight top, you know?"
    bree.say "It kinda doesn't leave much to the imagination!"
    "Angela's cheeks turn an even deeper shade of red."
    angela.say "But...what do you think, [hero.name]?"
    angela.say "Do you like them?"
    bree.say "Oh yeah, Angela!"
    bree.say "They look great - super sexy!"
    "Angela smiles, pleased to hear that I approve."
    "And the flush on her cheeks changes subtly."
    "Going from embarrassment to arousal."
    return

label angela_piercing_navel_reaction_female:
    bree.say "Ooh, Angela!"
    bree.say "You got a belly-button piercing!"
    "Angela looks a little embarrassed."
    "She leans in closer so as not to be heard."
    angela.say "What do you think, [hero.name]?"
    angela.say "Does it suit me?"
    angela.say "You don't think I'm too old for a piercing, do you?"
    "I shake my head, dismissing Angela's concerns."
    bree.say "No way, Angela!"
    bree.say "It looks great - super sexy!"
    "Angela smiles, pleased to hear that I approve."
    "And the flush on her cheeks changes subtly."
    "Going from embarrassment to arousal."
    return

label angela_piercing_clit_reaction_female:
    angela.say "Ah, [hero.name]..."
    angela.say "I have something to show you..."
    "I can see that Angela's already starting to blush."
    "So I lean in closer, so that nobody else can overhear us."
    bree.say "What's that, Angela?"
    angela.say "Well...I got a piercing, [hero.name]!"
    angela.say "And it's in a VERY intimate place!"
    bree.say "Oh, Angela!"
    bree.say "Did you get one...down there?!?"
    "Angela nods, giggling and blushing for real now."
    bree.say "I can't wait to see it!"
    return

label angela_piercing_head_reaction_female:
    "Angela looks left and right, making sure nobody else is looking."
    "Then she sticks her tongue out at me."
    "I'm surprised by the gesture, but then I do a double-take."
    bree.say "Angela!"
    bree.say "You got a tongue piercing?!?"
    "Angela pulls her tongue back into her mouth and grins."
    angela.say "Oh yes!"
    angela.say "It feels weird, but I love it."
    angela.say "What do you think?"
    bree.say "I love it too, Angela."
    bree.say "It's SO rebellious!"
    return

label angela_movie_liked_reaction_female:
    bree.say "I really enjoyed that movie, Angela."
    bree.say "What did you think?"
    "Angela nods eagerly."
    angela.say "Me too, [hero.name]."
    angela.say "It's the best movie I've seen in a long time."
    angela.say "Thanks for convincing me to come along."
    return

label angela_movie_indifferent_reaction_female:
    bree.say "I really enjoyed that movie, Angela."
    bree.say "What did you think?"
    "Angela raises her eyebrows and shrugs."
    angela.say "Hmm..."
    angela.say "It was okay, I guess."
    angela.say "But it wasn't anything special."
    return

label angela_movie_disliked_reaction_female:
    bree.say "I really enjoyed that movie, Angela."
    bree.say "What did you think?"
    "Angela shakes her head, wrinkling her nose in disgust."
    angela.say "Oh no, [hero.name]!"
    angela.say "How can you even say that?"
    angela.say "It was terrible, from start to finish!"
    return

label angela_abortion_reaction_female:
    "When I see Angela, I almost turn and walk the other way."
    "But then I take a deep breath and keep on going."
    "Because I have to face her sooner or later."
    "So now is as good a time as any, I guess..."
    angela.say "[hero.name]?"
    angela.say "I...I see that you went through with it then?"
    angela.say "I mean, you had it done?"
    "All I can do is nod and try to put a smile on my face."
    "Even though that's the last thing I feel like doing right now."
    bree.say "How did you know, Angela?"
    bree.say "I haven't told anyone else about it yet."
    if angela.love >= 150:
        "I see a pained smile spread across Angela's face."
        "Almost the perfect companion to the one on mine."
        angela.say "I guess I just recognised the look in your eyes, [hero.name]."
        angela.say "It's the kind of thing only a woman would notice."
        bree.say "Do you mean..."
        bree.say "Have you..."
        "Angela gives me a look that stops my questions dead."
        "One that lets me know I shouldn't probe any deeper."
        angela.say "Let's just say I've had my own experiences, [hero.name]."
        angela.say "And I know what you're probably feeling right now."
        angela.say "So if you need anything - anything at all..."
        angela.say "Or just to talk, give me a call."
        "I nod and then it seems like the conversation is over."
        "And Angela walks away, leaving me to ponder what she just said."
    else:
        "Angela folds her arms over her chest."
        "And she looks at me with a cold expression on her face."
        angela.say "I could just sense it, [hero.name]."
        angela.say "That warm glow an expecting mother has..."
        angela.say "It's gone from around you."
        "I find myself backing off a little at Angela's words."
        "They're unexpectedly barbed and hurtful."
        bree.say "I..."
        bree.say "I only did what I had to, Angela!"
        bree.say "I thought you'd have understood that?"
        "Angela shakes her head."
        angela.say "No, [hero.name] - not at all!"
        angela.say "No mother could ever do that."
        angela.say "No real woman capable of nurturing a life!"
        "I open my mouth to respond, but then I stop."
        "As it seems like the conversation is over."
        "And Angela walks away, leaving me to ponder what she just said."
    return


label angela_belly_interaction_female:
    $ angela.set_flag("interact", 1, 1, "+")
    show angela at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call angela_belly_kiss_female from _call_angela_belly_kiss_female_1
        "Caress my belly":
            call angela_belly_caress_female from _call_angela_belly_caress_female_1
        "Listen to the baby":
            call angela_belly_listen_female from _call_angela_belly_listen_female_1
        "Never mind":
            pass
    return

label angela_belly_caress_female:
    show angela smile at center, zoomAt(1.5, (640, 1040))
    "I keep spending so much time staring down at my belly that I'm getting a crick in my neck."
    "And every time I look up, I expect to see everyone around me shooting disapproving looks in my direction."
    "So it's a bit of a surprise when I'm greeted by the sight of Angela practically beaming at me."
    bree.say "Erm..."
    bree.say "Are you okay, Angela?"
    bree.say "You look a little blissed out over there!"
    "At first Angela doesn't really seem to hear what I'm saying to her."
    "She just keeps right on staring at me in that same vacant manner."
    "But then she blinks and seems to snap out of it."
    show angela surprised
    angela.say "What?"
    angela.say "Oh...sorry, [hero.name]."
    show angela fragile
    angela.say "It's just been a while since I was around someone that's pregnant."
    scene expression f"bg {game.room}" at blur(10), dark
    show angela_dylan_ending_fx_swirl as swirl at clock(5), center, zoomAt(2.0, (640, 1800)), blur(5)
    show angela mindless at center, zoomAt(1.5, (640, 1040))
    with dissolve
    angela.say "It kind of brought back all of those memories for me."
    "I nod and smile, keen to show Angela that I understand."
    bree.say "I suppose so, Angela."
    bree.say "You already went through all of this, yeah?"
    show angela blush
    "Angela blushes a little as she nods."
    angela.say "It's weird, [hero.name]..."
    angela.say "I used to get so tired of everyone wanting to touch my bump."
    angela.say "And so I've been holding back from asking you to do the same thing."
    angela.say "But I just can't keep my mind off it!"
    "I shrug and gesture to my belly."
    bree.say "It's fine, Angela..."
    bree.say "You can feel it if you like."
    scene expression f"bg {game.room}"
    show angela smile at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "Almost as soon as the words are out of my mouth, Angela's on the move."
    "And a moment later I find her leaning over my belly, gently touching it."
    "I open my mouth to say something, as Angela seems to engrossed to speak."
    "But then I find myself closing it again as I watch her."
    "Angela just seems to delighted to be able to put her hands on me."
    "The joy she's projecting is infecting me too."
    $ angela.love += 2
    return

label angela_belly_kiss_female:
    show angela happy at center, zoomAt(1.5, (640, 1040))
    angela.say "[hero.name]..."
    angela.say "I kind of wanted to ask you something."
    show angela shy
    angela.say "But I'm worried that it might freak you out."
    show angela normal
    "I look up and see that Angela's standing in front of me."
    "And that she has a rather worried look on her face."
    bree.say "Erm..."
    bree.say "There's only one way to find out, isn't there?"
    bree.say "You either have to ask me, or live in a state of eternal doubt!"
    "I smile and give Angela a wink, trying to make a joke out of it."
    "But she still looks more than a little worried."
    show angela happy
    angela.say "Well..."
    angela.say "I've always had this thing about kissing things."
    angela.say "Kind of when I want to make sure that they're going to be okay."
    show angela normal
    "Angela's already starting to shake her head and wave her hand."
    "Like she's convinced I already think she's insane."
    show angela talkative
    angela.say "It's just a silly little thing..."
    angela.say "For good luck..."
    angela.say "I don't know why I even mentioned it!"
    show angela normal
    bree.say "You want to kiss my bump?"
    bree.say "Of course you can!"
    show angela smile
    "Angela stops dead in her tracks as I say all of this."
    "And she looks on in amazement as I pull up my top."
    "Of course this releases the full curve of my belly."
    "And believe me, it's getting pretty large by now!"
    show angela fragile
    angela.say "Are..."
    angela.say "Are you sure, [hero.name]?"
    show angela smile
    "I nod and Angela doesn't need any more encouragement."
    show angela at center, zoomAt(1.5, (640, 1240)) with ease
    "She gets down on her knees."
    show angela at center, traveling(2.5, 0.3, (640, 1940))
    "And then she leans forward and gives my belly a soft, lingering kiss."
    "I can feel the warmth of her lips through my skin."
    bree.say "Angela..."
    bree.say "That was beautiful."
    bree.say "I can already feel the baby responding to it."
    show angela surprised
    angela.say "Really?"
    show angela normal
    "I take Angela's hand and place it on my belly."
    "Just as I feel a little kick from inside."
    show angela surprised
    angela.say "Oh!"
    show angela happy
    angela.say "I felt that!"
    show angela smile
    "Angela looks up at me with tears in her eyes."
    show angela happy
    angela.say "Thank you for letting me do that, [hero.name]."
    show angela normal
    "The moment is so tender and beautiful."
    "I find myself getting a little emotional too."
    $ angela.love += 3
    return

label angela_belly_listen_female:
    show angela normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Erm..."
    bree.say "Angela..."
    bree.say "Would you mind doing me a little favour?"
    show angela smile
    "Angela turns towards me as soon as I ask the question."
    "And from the look on her face she seems keen to help out."
    show angela happy
    angela.say "Of course, [hero.name]..."
    show angela talkative
    angela.say "What do you need?"
    show angela normal
    "I already have my hands on my belly."
    "So I look down to draw Angela's eye to it."
    "Then I point to the curve, just to make my intentions clear."
    bree.say "Would you mind listening to it?"
    bree.say "Just to check that the baby's okay, you know?"
    show angela smile
    "Angela doesn't waste any time - she's already moving closer."
    show angela at center, zoomAt(1.5, (640, 1240)) with ease
    "And she's already getting down on her knees."
    show angela happy
    angela.say "Of course!"
    angela.say "I'll listen for as long as you like!"
    show angela smile at center, traveling(2.5, 0.3, (640, 1940))
    "Angela places her ear against my belly."
    show angela pleased
    "Then she closes her eyes and stays perfectly still."
    "I can see the look of concentration on her face."
    "Like she's listening to a beautiful piece of music."
    show angela smile
    "And after a few moments, she looks up at me with a smile."
    show angela happy
    angela.say "I can hear it, [hero.name]!"
    angela.say "I can hear the heartbeat!"
    angela.say "It's strong and steady..."
    angela.say "Your baby sounds perfectly healthy to me."
    show angela smile
    "I let out a sigh of relief at Angela's words."
    bree.say "Thanks, Angela."
    bree.say "That's exactly what I needed to hear."
    "Angela keeps her ear pressed against my belly for a few more moments."
    "Almost like she doesn't want this special moment to end."
    show angela happy
    angela.say "It's been so long since I heard that sound."
    angela.say "It brings back so many memories."
    show angela smile
    bree.say "Good memories, I hope?"
    "Angela nods and smiles."
    show angela happy
    angela.say "The very best, [hero.name]."
    angela.say "The very best."
    $ angela.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
