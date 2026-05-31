label kiara_ice_cream_reaction_male:
    mike.say "It's so hot today, Kiara!"
    mike.say "I think we should grab an ice-cream and try to cool down."
    "Kiara nods as she wipes her forehead."
    kiara.say "That is a very good idea, [hero.name] - lead the way."
    "Together we hurry over to the ice-cream stand and place our order."
    "And within a couple of minutes, we have our ice-creams."
    "Kiara starts to lick away at hers, and that's when I realise there's a problem."
    "The idea was to cool down, but the sight of Kiara's tongue wrapping around that ice-cream..."
    "Well, let's just say it's making me hot in a whole different way!"
    return

label kiara_ask_phone_male:
    mike.say "Oh, Kiara, I meant to ask..."
    mike.say "I didn't get your telephone number."
    mike.say "You think I could have it?"
    show kiara annoyed
    "Kiara raises an eyebrow as I ask the question."
    "Looking at me as if she's weighing up her options."
    if hero.charm >= 20 - kiara.love:
        if 'fafwm' in DLCS:
            $ hero.smartphone_contacts.append("kiara")
        show kiara smile
        show kiara talkative
        kiara.say "Of course you may have it, [hero.name]."
        kiara.say "I am surprised that I did not give it to you already."
        show kiara smile
        "Kiara pulls out her phone and fiddles with it until she finds what she wants."
        "Then she holds it up for me to copy her number into my contacts."
        mike.say "Thanks, Kiara - I promise not to send you too many messages!"
    else:
        show kiara sad
        kiara.say "Hmm..."
        show kiara talkative
        kiara.say "If you do not have it, that can only mean one thing."
        kiara.say "And that is that I did not want you to have it yet."
        kiara.say "Ask me again in a little while, and maybe that will have changed."
        show kiara sad
        $ kiara.love -= 1
        $ kiara.sub -= 1
    show kiara normal
    return

label kiara_ask_birthday_male:
    mike.say "I was going to ask, Kiara..."
    mike.say "What's the date of your birthday?"
    show kiara normal
    "Kiara gives me a thoughtful look as I ask the question."
    "Which is kind of annoying, as I was hoping for a straight answer."
    show kiara talkative
    kiara.say "The date of my birthday, you say?"
    if hero.charm >= 40 - kiara.love:
        show kiara smile
        $ kiara.flags.birthdayknown = True
        show kiara talkative
        kiara.say "I suppose that there is no harm in telling you."
        kiara.say "My birthday is on the [active_girl.birthday[1]] of [active_girl.birthday[0]]."
        kiara.say "But I will not tell you the year I was born."
        kiara.say "Because a woman has to retain some of her secrets."
        show kiara smile
        mike.say "Oh yeah, of course you do."
    else:
        show kiara annoyed
        pause 1
        show kiara guilty
        kiara.say "I do not think the time is right to tell you that."
        kiara.say "A woman must retain some of her secrets."
        kiara.say "And this is one that I choose to keep, for now."
        $ kiara.sub -= 1
        $ kiara.love -= 1
        show kiara annoyed
        "I can tell from the look on Kiara's face that she's not going to budge."
        "So all I can do is nod and let the matter drop."
        hide kiara
    return

label kiara_offer_a_drink_male:
    "As I drain the last few dregs of my drink, I'm already standing up and turning towards the bar."
    mike.say "Looks like it's time for another round."
    mike.say "How about you, Kiara?"
    mike.say "You want a pint of something?"
    if kiara.is_visibly_pregnant:
        show kiara disappointed
        "Kiara's eyes go wide with surprise as I ask the question."
        "And at the same time her hands move to her belly, as if to shield it from harm."
        show kiara angry
        kiara.say "[hero.name], did you forget about something?!?"
        $ kiara.love -= 10
        show kiara irritated
        "Suddenly reminded of the fact she's pregnant, I shake my head."
        mike.say "Oh yeah, sorry!"
        mike.say "Maybe a soft drink or a fruit-juice instead?"
        $ hero.cancel_activity()
        hide kiara
    elif (hero.charm >= 60 - kiara.love and kiara.flags.drinks < 2) or date_girl == kiara:
        show kiara smile
        "Kiara picks up her glass and swills around the remaining liquid inside."
        kiara.say "I think that you are trying to get me drunk!"
        kiara.say "But then so what if you are?"
        kiara.say "I will have another one of these."
        hide kiara
        show drink kiara
        if kiara.love <= 25:
            $ kiara.love += 1
        elif date_girl == kiara and game.active_date:
            $ game.active_date.score += 5
        call expression kiara.get_chat from _call_expression_541
        hide drink kiara
        $ kiara.set_flag("drinks", 1, "day", mod="+")
    else:
        show kiara annoyed
        kiara.say "Sorry, I don't feel like drinking."
        $ hero.cancel_activity()
        hide kiara
    return

label kiara_slap_ass_intro_male:
    "Kiara's ass is like a work of art, something that should be framed and hung in a gallery."
    "So is it any wonder that I can't resist drawing back my hand and swinging it on an intercept course?"
    "It describes a low arc through the air, connecting with one of those shapely buttocks."
    "The sound is extremely satisfying to my ear, adding to the overall delight of Kiara's ass."
    "But of course it also means that the game is up, as she springs forwards and lets out a yelp of surprise."
    kiara.say "Ouch!"
    kiara.say "Did you..."
    kiara.say "Did you just slap my bottom?!?"
    mike.say "Ah..."
    mike.say "Yeah, I guess I did do that."
    mike.say "It just looked so good that I couldn't resist it."
    return

label kiara_slap_ass_happy_male:
    "Kiara's lips curl into an ironic smile, and she wags a finger in my face."
    kiara.say "It's lucky that you were the one to do it, [hero.name]."
    kiara.say "Anyone else and I would have been quite irate."
    "I nod eagerly, thankful to have been let off the hook."
    "But I'm left wondering if Kiara's reaction means I can do it again or not."
    return

label kiara_slap_ass_angry_male:
    "Kiara's brows crease into an angry frown, and she plants her balled fists on her hips."
    kiara.say "You're lucky that I like you, [hero.name]."
    kiara.say "Because if it were anyone else..."
    kiara.say "Well, let us just say that they would have regretted it!"
    "I nod nervously, thankful to have been let off so lightly."
    "And I make a mental note not to do it again."
    return

label kiara_breakup_male:
    mike.say "There's no easy way to say this, Kiara..."
    mike.say "So I'm just going to come out with it."
    mike.say "I think that we should end things, that we should break up."
    "Kiara looks at me, shaking her head in disbelief."
    show kiara talkative
    kiara.say "You cannot be serious, [hero.name]!"
    kiara.say "I thought that things were going well between us?"
    show kiara annoyed
    "The look on Kiara's face is almost enough to break me."
    "Almost enough to make me change my mind on the spot."
    "But somehow I shake it off and stiffen my resolve."
    mike.say "I've been trying my best to make it work, I really have."
    mike.say "But I just don't feel that spark anymore."
    mike.say "And I want to end it while we can maybe still be friends."
    mike.say "Or at least while we can still stand the sight of each other."
    show kiara irritated
    "Kiara looks like she wants to keep on arguing with me."
    "But I think she can see from the look in my eyes that I'm serious."
    "And I watch as all of the fight seems to drain out of her."
    show kiara talkative
    kiara.say "Ah...this is so hard!"
    kiara.say "But if it is what you want, then so be it."
    kiara.say "I would not want to hold you against your will."
    show kiara sadsmile
    "I can only manage to nod gratefully in response to Kiara's words."
    "That and then turn away, beginning to walk off alone."
    "Because what I need right now is solitude and time."
    hide kiara
    return

label kiara_go_steady_intro_male:
    mike.say "Kiara..."
    mike.say "We've been hanging-out together a lot recently, haven't we?"
    "Kiara shakes her head at me and lets out a chuckle."
    show kiara talkative
    kiara.say "Hanging-out!"
    kiara.say "You make us sound like silly little teenagers."
    kiara.say "But yes, we have been spending a great deal of time together."
    show kiara normal
    "I nod, eager to go further down that same line of discussion."
    mike.say "Yeah, and it got me thinking - maybe it's time we went steady?"
    "Kiara frowns and wrinkles her brow."
    show kiara talkative
    kiara.say "You want us to walk more slowly, more carefully?"
    show kiara evil
    mike.say "No, no, no - it means to officially start dating someone."
    mike.say "I'm asking if you want to be my girlfriend!"
    return

label kiara_go_steady_yes_male:
    "Kiara chuckles again, but much to my relief, she does so while smiling."
    show kiara talkative
    kiara.say "Of course I would, [hero.name]."
    kiara.say "The way you ask me these things..."
    kiara.say "It makes me feel like I am a teenager again myself!"
    show kiara smile
    "I'm nodding and laughing as she says this too."
    "But mainly because I'm too delighted to do anything more."
    return

label kiara_go_steady_no_male:
    "Kiara chuckles again, but this time i not that she's also shaking her head."
    show kiara guilty
    kiara.say "I am flattered, but I must say no."
    show kiara talkative
    kiara.say "I do not think that our relationship has matured to that degree."
    kiara.say "So let us wait until that time comes."
    show kiara annoyed
    "Obviously that's not the answer that I was looking for."
    "But all I can do is nod in agreement and let the matter drop for now."
    return

label kiara_pet_intro_male:
    "Sometimes I just feel an overwhelming sense of affection for Kiara."
    "So much so that I want to do something about it, something to show her how I feel."
    "But there doesn't seem to be any conscious thought involved as I reach out to do so."
    "And patting her on the head - well that's not something I could have planned in advance."
    "Yet that's exactly what my hand does, the palm coming down gently on top of Kiara's head."
    show kiara angry
    kiara.say "What..."
    kiara.say "What was that?"
    kiara.say "Did you pat me on the head?!?"
    show kiara irritated
    mike.say "Ah..."
    mike.say "Yeah, I guess I did do that."
    mike.say "I just felt the urge and couldn't resist!"
    return

label kiara_pet_happy_male:
    "Kiara shrugs and smiles, shaking her head."
    show kiara talkative
    kiara.say "Well maybe give me some warning next time?"
    show kiara cringe
    kiara.say "That way I won't be so surprised when it happens."
    show kiara smile
    "I nod my head, making a mental note of Kiara's request."
    "But also feeling thankful that she was okay with it in the end."
    return

label kiara_pet_annoyed_male:
    "Kiara frowns and shakes her head."
    show kiara angry
    kiara.say "Well I would remind you that I am a woman, and not a dog!"
    kiara.say "If you want to do that to someone, go buy a canine companion."
    kiara.say "Because you certainly will not be doing that to me again!"
    show kiara
    "I nod nervously, thankful to have been let off so lightly."
    "And I make a mental note not to do it again."
    return

label kiara_massage_intro_male:
    show kiara whining
    kiara.say "Argh..."
    kiara.say "My back - I am in so much pain!"
    kiara.say "I must have pulled a muscle when I was moving things in the cafe."
    show kiara sad
    "I can't help wincing in sympathy as Kiara arches her back."
    "Because the severity of her pain is plain to see."
    mike.say "Ooh, that does look painful!"
    mike.say "Is there anything that I can do to help?"
    mike.say "I've been told I give a pretty mean massage."
    return

label kiara_massage_accept_male:
    show kiara talkative
    kiara.say "Well, that does sound appealing."
    kiara.say "And if there's any chance that it could help..."
    kiara.say "Very well, [hero.name], I accept your offer."
    show kiara smile
    "It's almost impossible for me to hide my excitement as Kiara says yes."
    mike.say "That's great, Kiara - now let's go somewhere more private and get started!"
    return

label kiara_massage_refuse_male:
    show kiara talkative
    kiara.say "That is a kind offer, [hero.name]..."
    kiara.say "But I am afraid that I cannot accept."
    kiara.say "Were something to go wrong, I would not be able to work at the cafe."
    kiara.say "So I will arrange to see a professional as soon as I am able."
    show kiara annoyed
    "I nod at this, disappointed to be denied the chance to give Kiara a massage."
    "But I guess that she does make a good point, so at least that counts for something."
    return

label kiara_piercing_nipples_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had them pierced!"
    "Kiara pulls down her top, letting me see a glimpse of pierced nipple!"
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return

label kiara_piercing_navel_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had it pierced!"
    "Kiara pulls up her top, letting me see a glimpse of pierced navel!"
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return

label kiara_piercing_clit_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had it pierced!"
    "Kiara pulls down her panties, letting me see a glimpse of pierced clit!"
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return

label kiara_piercing_ears_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had them pierced!"
    "Kiara turns her head, letting me see her new earrings."
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return

label kiara_piercing_head_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had it pierced!"
    "Kiara sticks out her tongue, letting me see a glimpse of the piercing!"
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return

label kiara_piercing_nose_reaction_male:
    kiara.say "I have finally done it, [hero.name]..."
    kiara.say "I have had it pierced!"
    "Kiara leans in close, letting me see the piercing in her nose!"
    mike.say "WHOA!"
    mike.say "That's amazing - and totally hot too!"
    kiara.say "I am glad to hear that you approve."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
