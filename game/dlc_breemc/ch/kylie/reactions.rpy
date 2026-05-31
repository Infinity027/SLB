label kylie_ice_cream_reaction_female:
    kylie.say "Urgh..."
    kylie.say "It's so damn hot today, [hero.name]!"
    kylie.say "Maybe coming to the beach wasn't such a good idea?"
    "I can see that Kylie's mood is getting worse by the second."
    "And if it keeps going that way, the whole day is going to be ruined."
    "Glancing around, I quickly settle on something that might save it."
    bree.say "Ice-cream!"
    bree.say "Let's grab an ice-cream, Kylie."
    kylie.say "Oh...okay, [hero.name]."
    "I hurry over to the ice-cream stand with Kylie in tow."
    "And a few seconds later we're ordering ourselves a frozen treat."
    "As soon as I have my ice-cream in my hand, I take a serious lick."
    "Which is also when I notice that Kylie's watching me intently."
    bree.say "What's up, Kylie?"
    bree.say "You eyeing up my choice?"
    kylie.say "Erm...yeah, [hero.name]...something like that!"
    "I laugh and hold it out for her to take a lick too."
    "Kylie hesitates for a moment, but then takes me up on the offer."
    "Then we walk off, chatting as we lick our ice-creams."
    return

label kylie_ask_phone_female:
    bree.say "I was going to call you the other day, Kylie."
    bree.say "But I realised that I don't have your number!"
    bree.say "You want to let me have it now?"
    if hero.charm >= 20 - kylie.love:
        $ hero.smartphone_contacts.append("kylie")
        kylie.say "Of course, [hero.name]."
        kylie.say "I don't want to miss a call from you!"
        kylie.say "Here's my number..."
    else:
        $ kylie.love -= 1
        $ kylie.sub -= 1
        kylie.say "Hmm..."
        kylie.say "I don't give my number out to everyone I meet, [hero.name]."
        kylie.say "I don't want people to know where I am and what I'm doing."
    return

label kylie_ask_birthday_female:
    bree.say "Hey, Kylie..."
    bree.say "When's your birthday?"
    bree.say "I just realised that you never told me."
    if hero.charm >= 40 - kylie.love:
        $ kylie.flags.birthdayknown = True
        kylie.say "I didn't?"
        kylie.say "Hmm...I thought that I already did!"
        kylie.say "Okay, [hero.name], it's Winter 15."
    else:
        kylie.say "Why do you want to know that, [hero.name]?"
        kylie.say "Are you spying on me or something?"
        kylie.say "All the better reason not to give you that info!"
        $ kylie.love -= 1
        $ kylie.sub -= 1
    return

label kylie_offer_a_drink_female:
    bree.say "You want another drink, Kylie?"
    bree.say "I'm ready for another one."
    bree.say "And I can grab you one too, if you like."
    if (hero.charm >= 60 - kylie.love and kylie.flags.drinks < 2) or date_girl == kylie:
        kylie.say "That'd be great, [hero.name]."
        kylie.say "I'll have whatever you're having."
        kylie.say "And I mean EXACTLY what you're having..."
        show drink kylie
        if kylie.love <= 25:
            $ kylie.love += 1
        elif date_girl == kylie and game.active_date:
            $ game.active_date.score += 5
        call expression kylie.get_chat from _call_expression_394
        hide drink kylie
        $ kylie.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        kylie.say "No, [hero.name], I'll pass."
        kylie.say "I like to buy my own drinks, as a rule."
        kylie.say "Believe me, it's pretty easy for someone to spike it while you're not looking."
        kylie.say "I know that from personal experience..."
        $ hero.cancel_activity()
        hide kylie
    return

label kylie_slap_ass_intro_female:
    "You can't deny that Kylie's got some serious curves going on."
    "Whenever she walks past me, I find myself staring at them in awe."
    "In fact, I kind of feel like they're hypnotising me!"
    "Which might explain why I pull back my arm and swing."
    kylie.say "OW!"
    kylie.say "Hey - what the hell?!?"
    "Kylie spins around and looks me straight in the eye."
    kylie.say "[hero.name] - did you just slap me on the ass?!?"
    "All I can do is shrug and smile."
    "That and admit to my guilt."
    bree.say "Erm...yeah, Kylie..."
    bree.say "I guess I did!"
    return

label kylie_slap_ass_happy_female:
    kylie.say "Oh...well..."
    kylie.say "I guess that's okay then..."
    kylie.say "I should really take it as a compliment!"
    return

label kylie_slap_ass_angry_female:
    kylie.say "How dare you even touch me without permission?"
    kylie.say "Don't you have any respect for personal boundaries?"
    kylie.say "Do that again and you'll regret it!"
    return

label kylie_breakup_female:
    bree.say "Kylie..."
    bree.say "There's no easy way to say this..."
    bree.say "But I don't think I want to be with you anymore."
    "Kylie stares at me as the meaning of my words sinks in."
    "And I watch as her expression goes from disbelief to something else."
    "And that something is cold and more than a little frightening to behold."
    kylie.say "Oh no...tell me I didn't just hear you say that, [hero.name]."
    kylie.say "Tell me that you're not breaking up with me."
    bree.say "I can't, Kylie."
    bree.say "Because that's just how it is."
    bree.say "This thing between us, it's over."
    "Kylie's eye's narrow and become cold."
    "Every ounce of warmth seems to drain out of her face too."
    kylie.say "You're going to regret this, [hero.name]."
    kylie.say "Because you've made a fatal mistake!"
    "Before I can say another word, Kylie turns on her heel."
    "And then she hurries off, leaving me alone and more than a little afraid."
    return

label kylie_go_steady_intro_female:
    bree.say "How many dates have we been on now, Kylie?"
    bree.say "I've kind of lost count!"
    "Kylie frowns, giving away the fact that she's scouring her memory."
    kylie.say "I'm not sure, [hero.name]."
    kylie.say "Normally I'd remember something like that."
    kylie.say "But I think I've been having too much fun to recall!"
    bree.say "And that's a good thing, right?"
    bree.say "Maybe a sign that we should make things official?"
    kylie.say "You mean go steady?"
    bree.say "Yeah, Kylie - that's exactly what I mean."
    return

label kylie_go_steady_yes_female:
    kylie.say "You're right, [hero.name], we should go steady."
    kylie.say "We should totally do that."
    kylie.say "The closer we are together the more perfect things will be."
    return

label kylie_go_steady_no_female:
    kylie.say "I don't think that would be a good idea, [hero.name]."
    kylie.say "I feel like you know more than enough about me already."
    kylie.say "And there are parts of my life that I want to keep private."
    return

label kylie_pet_intro_female:
    "I just feel myself getting overwhelmed with affection for Kylie all of a sudden."
    "Which is why I can't stop myself from reaching out and patting her on top of the head."
    "She reacts instantly, stopping what she's saying and looking surprised."
    "And then she looks me straight in the eye, one hundred percent serious."
    "And, if I'm honest, more than a little scarily too!"
    kylie.say "[hero.name]..."
    kylie.say "Why did you do that?"
    kylie.say "Why did you just pat me on the head?"
    bree.say "I...I don't really know, Kylie."
    bree.say "I just wanted to do something nice, I guess!"
    return

label kylie_pet_happy_female:
    "Kylie's face suddenly breaks into a smile."
    kylie.say "Oh...that's okay then."
    kylie.say "Pat me on the head all you like!"
    return

label kylie_pet_annoyed_female:
    "Kylie frowns and her eyes turn cold."
    kylie.say "Don't ever do that again, [hero.name]."
    kylie.say "I don't like being petted."
    kylie.say "Because I'm not a dog, okay?!?"
    return

label kylie_massage_intro_female:
    kylie.say "Ouch..."
    kylie.say "Damn it!"
    bree.say "Ooh, that looks painful, Kylie!"
    bree.say "Did you pull something?"
    "Kylie nods, making what looks like a stabbing motion to demonstrate."
    kylie.say "Yeah, it hurts whenever I do this."
    kylie.say "No idea why though!"
    bree.say "You want me to take a look at it for you?"
    bree.say "I'm told I give a pretty mean massage!"
    return

label kylie_massage_accept_female:
    kylie.say "Would you, [hero.name]?"
    kylie.say "I really need to be able to move my arm like that again."
    kylie.say "Because...well...because reasons!"
    return

label kylie_massage_refuse_female:
    kylie.say "No, [hero.name]..."
    kylie.say "Thanks for the offer, but I think I'll pass."
    kylie.say "I really need to be able to move my arm like that again."
    kylie.say "Because...well...because reasons!"
    kylie.say "So I need to have a professional take a look."
    return

label kylie_piercing_nipples_reaction_female:
    "I can tell that Kylie's got something that she wants to show me."
    "But from the look on her face, she's going to make me guess what it is."
    bree.say "What is it, Kylie?"
    bree.say "Come on, don't keep me in the dark!"
    "Kylie just smiles and holds her tongue."
    "But she stares downwards, drawing my gaze."
    bree.say "Is that...did you..."
    kylie.say "Yeah, [hero.name] - I had my nipples pierced!"
    bree.say "Oh wow, Kylie!"
    bree.say "I can't wait to see them!"
    return

label kylie_piercing_navel_reaction_female:
    "I can tell that Kylie's got something that she wants to show me."
    "But from the look on her face, she's going to make me guess what it is."
    bree.say "What is it, Kylie?"
    bree.say "Come on, don't keep me in the dark!"
    "Kylie just smiles and holds her tongue."
    "But she stares downwards, drawing my gaze."
    bree.say "Is that...did you..."
    kylie.say "Yeah, [hero.name] - I had my navel pierced!"
    bree.say "Oh wow, Kylie!"
    bree.say "I can't wait to see it!"
    return

label kylie_piercing_clit_reaction_female:
    "I can tell that Kylie's got something that she wants to show me."
    "But from the look on her face, she's going to make me guess what it is."
    bree.say "What is it, Kylie?"
    bree.say "Come on, don't keep me in the dark!"
    "Kylie just smiles and holds her tongue."
    "But she stares downwards, drawing my gaze."
    bree.say "Is that...did you..."
    kylie.say "Yeah, [hero.name] - I had my clit pierced!"
    bree.say "Oh wow, Kylie!"
    bree.say "I can't wait to see it!"
    return

label kylie_piercing_tongue_reaction_female:
    "I can tell that Kylie's got something that she wants to show me."
    "But from the look on her face, she's going to make me guess what it is."
    bree.say "What is it, Kylie?"
    bree.say "Come on, don't keep me in the dark!"
    "Kylie just smiles and holds her tongue."
    "Then she opens her mouth and sticks it out at me!"
    bree.say "Is that...did you..."
    kylie.say "Yeah, [hero.name] - I had my tongue pierced!"
    bree.say "Oh wow, Kylie!"
    bree.say "I can't wait to find out how it feels!"
    return

label kylie_movie_disliked_reaction_female:
    "As soon as we come out of the theatre, I can see Kylie's glancing my way."
    "And that means she's waiting to hear what I thought of the movie."
    "Which also means I won't hear her opinion until I've spilled my guts."
    bree.say "That was amazing, wasn't it, Kylie?"
    bree.say "I was jumping in my seat the whole time!"
    kylie.say "I don't think so, [hero.name]."
    kylie.say "I love a good slasher movie."
    kylie.say "But I hate it when the killer's so boring and two-dimensional."
    kylie.say "And they never sympathise with their point-of-view either!"
    return

label kylie_movie_indifferent_reaction_female:
    "As soon as we come out of the theatre, I can see Kylie's glancing my way."
    "And that means she's waiting to hear what I thought of the movie."
    "Which also means I won't hear her opinion until I've spilled my guts."
    bree.say "That was amazing, wasn't it, Kylie?"
    bree.say "I was jumping in my seat the whole time!"
    kylie.say "I don't think so, [hero.name]."
    kylie.say "I love a good slasher movie."
    kylie.say "But most of that stuff would never work in real life."
    kylie.say "Believe me, I know it!"
    return

label kylie_movie_liked_reaction_female:
    "As soon as we come out of the theatre, I can see Kylie's glancing my way."
    "And that means she's waiting to hear what I thought of the movie."
    "Which also means I won't hear her opinion until I've spilled my guts."
    bree.say "That was amazing, wasn't it, Kylie?"
    bree.say "I was jumping in my seat the whole time!"
    kylie.say "I know, I know..."
    kylie.say "I love a good slasher movie, [hero.name]!"
    kylie.say "So many great ideas too..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
