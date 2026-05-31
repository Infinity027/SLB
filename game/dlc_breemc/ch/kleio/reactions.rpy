label kleio_ask_birthday_female:
    bree.say "Hmm..."
    bree.say "When's your birthday, Kleio?"
    bree.say "I just realised I have no idea of the date!"
    if hero.charm >= 40 - kleio.love:
        show kleio happy
        $ kleio.flags.birthdayknown = True
        kleio.say "No big deal, [hero.name]."
        kleio.say "It's on the [active_girl.birthday[1]] of [active_girl.birthday[0]]."
        kleio.say "So now you know."
    else:
        show kleio annoyed
        kleio.say "Yeah well..."
        kleio.say "If you don't know, that means I didn't tell you."
        kleio.say "And if I didn't tell you, that means I don't want you to know!"
        $ kleio.sub -= 1
        $ kleio.love -= 1
    return

label kleio_ice_cream_reaction_female:
    bree.say "Hey, Kleio..."
    bree.say "Let's get ice-cream!"
    kleio.say "Huh?"
    kleio.say "Oh yeah, [hero.name] - great idea."
    "Together we hurry over to the ice-cream booth and both order what we want."
    "I can't help overhearing what Kleio's ordering, as it sounds pretty weird."
    "And as they put her order together, it starts to look pretty wild too!"
    "When my own ice-cream is done, I have to snap out of it and tear my eyes away."
    "I watch as Kleio takes her order and shoots me a knowing smile."
    kleio.say "Looks good, huh?"
    kleio.say "You want a lick?"
    bree.say "Oh yeah, Kleio!"
    bree.say "You bet I do!"
    "Kleio offers me her ice-cream and I eagerly take a lick."
    "It tastes just as good as it looks, which shows on my face."
    "It's unique, quirky and yet very good - just like Kleio!"
    "I return the favour, offering my cone to Kleio in turn."
    "Then we walk off together, enjoying our ice-creams together."
    return

label kleio_ask_phone_female:
    bree.say "Hey, Kleio..."
    bree.say "Can I get your phone number?"
    bree.say "I thought I already had it, but it looks like I don't!"
    if hero.charm >= 20 - kleio.love:
        show kleio happy
        $ hero.smartphone_contacts.append("kleio")
        kleio.say "You don't?"
        kleio.say "Huh...I thought I gave it to you too."
        kleio.say "Here it is..."
    else:
        show kleio annoyed
        kleio.say "Well, if you don't have it I didn't give it to you."
        kleio.say "And I'm pretty careful about who I do give it to, [hero.name]."
        kleio.say "So if you don't have it, I probably didn't want you to have it."
        $ kleio.love -= 1
        $ kleio.sub -= 1
    return

label kleio_offer_a_drink_female:
    bree.say "I'm going to get another from the bar."
    bree.say "You want one too, Kleio?"
    bree.say "That one's almost finished."
    if (hero.charm >= 60 - kleio.love and kleio.flags.drinks < 2) or date_girl == kleio:
        show kleio happy
        kleio.say "Huh?"
        kleio.say "Oh, sure, [hero.name]!"
        kleio.say "And thanks - I'll get you one back next time."
        hide kleio
        show drink kleio
        if kleio.love <= 25:
            $ kleio.love += 1
        elif date_girl == kleio and game.active_date:
            $ game.active_date.score += 5
        call expression kleio.get_chat from _call_expression_393
        hide drink kleio
        $ kleio.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show kleio annoyed
        kleio.say "Geez, [hero.name]!"
        kleio.say "I can get my own damn drinks."
        kleio.say "I'm not some helpless little girl!"
        $ hero.cancel_activity()
        hide kleio
    return

label kleio_slap_ass_intro_female:
    "I can't take my eyes off of Kleio's ass, no matter how hard I try."
    "It's just so pretty, pert and perfect, it's like it's calling to me!"
    "I honestly don't know why I get the urge to do it, or where it comes from."
    "I just swing my arm without thinking, and my hand connects with her ass."
    "Kleio lets out a yelp of alarm and leaps forwards."
    "Then she turns around, eyes wide with shock and disbelief."
    kleio.say "Did...did you..."
    kleio.say "Am I going crazy here..."
    kleio.say "Did you actually just slap my ass?!?"
    bree.say "Ah...yeah..."
    bree.say "I guess so, Kleio!"
    return

label kleio_slap_ass_happy_female:
    "Kleio crosses her arms over her chest and regards me with a wry smile."
    kleio.say "Wow..."
    kleio.say "You've got some serious balls on you, girl!"
    kleio.say "But do that again and you'll regret it!"
    return

label kleio_slap_ass_angry_female:
    "Kleio crosses her arms over her chest and regards me with a frown."
    kleio.say "You'd better quit that kind of shit right now."
    kleio.say "Or else you're going to regret it, okay?"
    bree.say "Y...yeah, Kleio..."
    bree.say "I get the picture."
    return

label kleio_breakup_female:
    show kleio
    bree.say "Kleio..."
    bree.say "There's something I need to tell you..."
    "Kleio looks up at this, her face already showing a grim expression."
    kleio.say "Oh god..."
    kleio.say "I don't want to hear this, do I?"
    kleio.say "Because it's always bad when someone says that!"
    show kleio annoyed
    "All I can do is shrug helplessly."
    "I've broached the subject now."
    "So it's too late to turn back."
    bree.say "It's us, Kleio..."
    bree.say "I don't think it's going to work out."
    kleio.say "Yeah, yeah..."
    kleio.say "I hear what you're saying, [hero.name]."
    kleio.say "Well...if that's how you feel..."
    bree.say "It is, Kleio, it is."
    bree.say "But maybe we can still be friends?"
    show kleio sad
    "Kleio snorts and shakes her head."
    kleio.say "Let's just concentrate on the break-up, yeah?"
    kleio.say "We can worry about all that shit later."
    return

label kleio_go_steady_intro_female:
    bree.say "Erm..."
    bree.say "Kleio..."
    kleio.say "Yeah, [hero.name]?"
    kleio.say "What's up?"
    "I grin at Kleio, trying and failing to look nonchalant."
    "The truth is that I've been waiting for the right moment to say this."
    "And now that I'm actually doing it, I'm not sure it's so right after all!"
    bree.say "We've been getting on pretty well, haven't we?"
    bree.say "I mean you and me, like as a thing, yeah?"
    "Kleio cocks her head on one side as she listens to me babble."
    "And I can tell that she's struggling to decipher my meaning."
    kleio.say "Yeah, [hero.name]..."
    kleio.say "I've been having some serious fucking fun with you."
    bree.say "So..."
    bree.say "What would you say if I said that we should make it official?"
    bree.say "Like start dating and be a proper couple?"
    return

label kleio_go_steady_yes_female:
    kleio.say "Fuck sake, [hero.name]!"
    kleio.say "You could have just come out and asked me."
    kleio.say "But yeah, I think that's a great idea."
    kleio.say "We should definitely make it official."
    return

label kleio_go_steady_no_female:
    kleio.say "Fuck sake, [hero.name]!"
    kleio.say "All that just to ask if we can make it official?"
    kleio.say "And for the record, no - I don't think we should."
    kleio.say "Making it official would ruin the fun we're having."
    return

label kleio_pet_intro_female:
    "Kleio's making me laugh so hard that I feel like I'm going to puke!"
    "I never knew that she could be so funny, it's almost too much."
    "I feel the need to show her how much she means to me."
    "And I guess that my brain's pretty screwed up in the moment."
    "Because I end up reaching out and patting her on the head."
    "Kleio looks at me in amazement, totally caught off-guard."
    kleio.say "Did...did you..."
    kleio.say "Am I going crazy here..."
    kleio.say "Did you actually just pat me on the head?!?"
    bree.say "Ah...yeah..."
    bree.say "I guess so, Kleio!"
    return

label kleio_pet_happy_female:
    "Kleio crosses her arms over her chest and regards me with a wry smile."
    kleio.say "Wow..."
    kleio.say "That's pretty weird of you, [hero.name]!"
    kleio.say "But don't make a habit of it, okay?"
    kleio.say "I'm not a dog, yeah?"
    return

label kleio_pet_annoyed_female:
    "Kleio crosses her arms over her chest and regards me with a frown."
    kleio.say "You'd better quit that kind of shit right now."
    kleio.say "Or else you're going to regret it, okay?"
    kleio.say "I'm not your fucking dog!"
    bree.say "Y...yeah, Kleio..."
    bree.say "I get the picture."
    return

label kleio_massage_intro_female:
    bree.say "You seem pretty tense today, Kleio."
    bree.say "Like you're carrying a load of stress in your shoulders."
    kleio.say "Yeah, yeah..."
    kleio.say "I think I put something out working in the garage."
    kleio.say "I just have to work it out, you know?"
    bree.say "Well...I could give you a massage, if you like?"
    return

label kleio_massage_accept_female:
    kleio.say "You know what, [hero.name]..."
    kleio.say "That sounds really good."
    kleio.say "When can you do me?"
    bree.say "I could start right now!"
    return

label kleio_massage_refuse_female:
    kleio.say "Oh no, no way!"
    kleio.say "I just need to tough it out, that's all."
    kleio.say "I've done it before and I can do it again."
    bree.say "Okay, Kleio, if that's what you want..."
    return

label kleio_piercing_nipples_reaction_female:
    "I can already hear Kleio chuckling as she watches my eyes move downwards."
    "But I just can't help it, I'm already obsessed with her breasts, and she knows that."
    "Now there's something new to see in that region as well, something pretty amazing."
    bree.say "Wow, Kleio..."
    bree.say "You really did it?"
    bree.say "You got them pierced?"
    kleio.say "I sure did, [hero.name]!"
    kleio.say "And they feel super sexy!"
    "I'm nodding my head up and down like crazy."
    "And I can feel myself getting hot just looking at them."
    bree.say "They sure look sexy, Kleio!"
    kleio.say "Oh yeah?"
    kleio.say "Just wait until you see them up close!"
    return

label kleio_piercing_navel_reaction_female:
    "I can already hear Kleio chuckling as she watches my eyes move downwards."
    "But I just can't help it, I'm already obsessed with her flat stomach, and she knows that."
    "Now there's something new to see in that region as well, something pretty amazing."
    bree.say "Wow, Kleio..."
    bree.say "You really did it?"
    bree.say "You got it pierced?"
    kleio.say "I sure did, [hero.name]!"
    kleio.say "And it feels super sexy!"
    "I'm nodding my head up and down like crazy."
    "And I can feel myself getting hot just looking at it."
    bree.say "It sure looks sexy, Kleio!"
    kleio.say "Oh yeah?"
    kleio.say "Just wait until you see it up close!"
    return

label kleio_piercing_clit_reaction_female:
    "I can already hear Kleio chuckling as she watches my eyes move downwards."
    "And that's because she's rubbing her hands on her flies, trying to draw my gaze."
    "Which means there's something new to see in that region as well, something pretty amazing."
    bree.say "Wow, Kleio..."
    bree.say "You really did it?"
    bree.say "You got it pierced?"
    kleio.say "I sure did, [hero.name]!"
    kleio.say "And it feels super sexy!"
    "I'm nodding my head up and down like crazy."
    "And I can feel myself getting hot just thinking at it."
    bree.say "It sure sounds sexy, Kleio!"
    kleio.say "Oh yeah?"
    kleio.say "Just wait until you see it up close!"
    return

label kleio_piercing_head_reaction_female:
    "Kleio strides straight up to me and sticks her tongue out."
    "That's a bratty move, even for someone as bratty as her."
    "But then I see the glint of metal in the middle of her tongue."
    bree.say "Wow, Kleio..."
    bree.say "You really did it?"
    bree.say "You got it pierced?"
    kleio.say "I sure did, [hero.name]!"
    kleio.say "And it feels super sexy!"
    "I'm nodding my head up and down like crazy."
    "And I can feel myself getting hot just looking at it."
    bree.say "It sure looks sexy, Kleio!"
    kleio.say "Oh yeah?"
    kleio.say "Just wait until you feel it up close!"
    return

label kleio_movie_liked_reaction_female:
    bree.say "I'm so glad we decided to see that movie, Kleio."
    bree.say "It's got to be one of the best I've seen in ages!"
    bree.say "You think so too, right?"
    kleio.say "You bet, [hero.name]..."
    kleio.say "That film had everything!"
    kleio.say "Really made me forget the real world for an hour or so!"
    return

label kleio_movie_indifferent_reaction_female:
    bree.say "I'm so glad we decided to see that movie, Kleio."
    bree.say "It's got to be one of the best I've seen in ages!"
    bree.say "You think so too, right?"
    kleio.say "Whoa, settle down, [hero.name]!"
    kleio.say "Obviously you liked it a hell of a lot."
    kleio.say "Left me feeling a little flat though."
    return

label kleio_movie_disliked_reaction_female:
    bree.say "I'm so glad we decided to see that movie, Kleio."
    bree.say "It's got to be one of the best I've seen in ages!"
    bree.say "You think so too, right?"
    kleio.say "You're kidding, you have to be, kidding!"
    kleio.say "That film was absolute fucking bollocks, [hero.name]!"
    kleio.say "You really do have shit taste!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
