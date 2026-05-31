label shiori_ice_cream_reaction_male:
    mike.say "I'm feeling all hot and bothered, Shiori - we should grab some ice cream!"
    shiori.say "Oh, I love ice cream - let's go!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Shiori chooses the same thing, but with her own combination of flavours."
    shiori.say "Mmm...this was such a good idea, [hero.name]!"
    shiori.say "Oh...oh, oh, oh...oh my...oh no!"
    "I look down, trying to see what's upsetting Shiori."
    "And it's then that I see the ice cream dripping onto her breasts!"
    shiori.say "Oh, I'm so clumsy - whatever must you think of me?!?"
    "I'm thinking of Shiori right now, but not in the way that she's afraid I am!"
    return

label shiori_call_in:
    if not shiori.flags.comIn and "shiori.show_off_3" in DONE:
        $ shiori.flags.comIn = True
        "Ever since I caught my first glimpse of that butt-plug sticking out of Shiori, I haven't been able to get it out of my mind."
        "Each and every time I see her, all I can do is wonder if it's still up there and how it looks if it is."
        "Before too long, it gets so bad that I can't tear my mind off of it and onto anything else."
        "I just keep looking up at the door to my office, wondering when Shiori's going to appear next."
        "In the end, the whole thing is driving me to distraction, and I just have to do something about it."
        "Without allowing myself to think of the possible consequences, I pick up the phone on my desk."
    else:
        "You know when you get one of those ideas in your head, the kind you just can't ignore?"
        "Sure, you try your best to push it aside and get on with your day like a normal human being."
        "But it's still in there, worming away in the very back of your mind."
        "And it's so much worse when you're sitting in the office and all you can think about is sex."
        "Every time I catch a glimpse of Shiori, it gets that much worse."
        "Where does she get off being so hot and sexy in the workplace?"
        "It's like she's doing it just for the sake of driving me insane!"
        "Eventually I can't take it anymore, and I pick up the phone on my desk."
    if game.days_played % 2 == 0:
        shiori.say "Ah, hello..."
        shiori.say "Shiori here?"
        "Even her voice turns me on."
        "It's so demure and innocent."
        "It just makes me want to do wicked things to her!"
        mike.say "Erm..."
        mike.say "Hey, Shiori..."
        mike.say "Could you step into my office for a moment?"
        "At the sound of my voice, Shiori's tone instantly picks up."
        "It's like she's delighted be handed a chance to please me."
        shiori.say "Of course, [hero.name]."
        shiori.say "I'm on my way!"
        play sound door_knock
        "It takes Shiori less than a minute to knock at my office door."
        "But even so, I still find myself getting impatient as I wait."
        mike.say "Come in, Shiori."
        show shiori
        "Obedient as ever, Shiori opens the door and scuttles inside."
        "She closes it neatly behind her and then hurries over to my desk."
        "I see that she's clutching a notepad and pen, looking eager to help."
        shiori.say "Here I am, [hero.name]."
    else:
        shiori.say "Hello, this is Shiori speaking."
        shiori.say "How may I help you?"
        "Even the sound of her sweet, innocent voice is enough to get me hotter."
        mike.say "Ah, Shiori..."
        shiori.say "Oh, hello, [hero.name]!"
        shiori.say "What can I do for you?"
        "I have to bite my tongue at this, to keep from saying something that I'll instantly regret."
        mike.say "Erm...yeah..."
        mike.say "Could you come in here when you have a minute, Shiori?"
        shiori.say "Sure thing, [hero.name] - I'll be right there!"
        "I put the phone down and shake my head at just how trusting she is."
        if Person.is_not_hidden("lavish") and Person.is_not_hidden("audrey"):
            "Audrey or Lavish would have demanded to know just what I wanted."
        elif Person.is_not_hidden("audrey"):
            "Audrey would have demanded to know just what I wanted."
        elif Person.is_not_hidden("lavish"):
            "Lavish would have demanded to know just what I wanted."
        "But Shiori's happy to simply come running to me, like an eager puppy..."
        "And sure enough, a short while later, I hear a rapping at my office door."
        mike.say "Come in."
        show shiori
        "Shiori bustles into the office, all smiles and even a cute little wave."
        shiori.say "Well, [hero.name] - here I am!"
    return

label shiori_ask_phone_male:
    mike.say "I wanted to get your number, Shiori."
    mike.say "You know - so I can call you some time?"
    if hero.charm >= 20 - shiori.love:
        show shiori happy
        $ hero.smartphone_contacts.append("shiori")
        shiori.say "You do?!?"
        shiori.say "Of course you can have my number, [hero.name]!"
        shiori.say "And you can call me anytime you like too!"
    else:
        show shiori annoyed
        $ shiori.love -= 1
        $ shiori.sub -= 1
        shiori.say "Oh...oh dear..."
        shiori.say "I don't think so, [hero.name]."
        shiori.say "I don't think that would be appropriate!"
    return

label shiori_ask_birthday_male:
    mike.say "Hey, Shiori..."
    mike.say "When is your birthday?"
    if hero.charm >= 40 - shiori.love:
        show shiori happy
        $ shiori.flags.birthdayknown = True
        shiori.say "Oh..."
        shiori.say "It's Spring 23, [hero.name]."
        shiori.say "Thank you for asking!"
    else:
        show shiori annoyed
        $ shiori.sub -= 1
        $ shiori.love -= 1
        shiori.say "But...but..."
        shiori.say "I already told you how old I am!"
        shiori.say "Don't you believe me?!?"
    return

label shiori_offer_a_drink_male:
    mike.say "Would you like a drink, Shiori?"
    mike.say "I'm going to the bar, so it's no trouble to get you one too."
    "Almost the second the words are out of my mouth, Shiori turns to face me."
    if shiori.is_visibly_pregnant:
        show shiori angry
        $ shiori.love -= 10
        shiori.say "Oh...how could you, [hero.name]?"
        shiori.say "You know I can't drink when I'm pregnant!"
        shiori.say "I thought you cared about me and the baby?!?"
        $ hero.cancel_activity()
        hide shiori
    elif (hero.charm >= 60 - shiori.love and shiori.flags.drinks < 2) or date_girl == shiori:
        show shiori happy
        shiori.say "Oh...okay, [hero.name]."
        shiori.say "Maybe I could have a glass of wine?"
        shiori.say "Red or white - whichever you prefer!"
        hide shiori
        show drink shiori
        if shiori.love <= 25:
            $ shiori.love += 1
        elif date_girl == shiori and game.active_date:
            $ game.active_date.score += 5
        call expression shiori.get_chat from _call_expression_270
        hide drink shiori
        $ shiori.set_flag("drinks", 1, "day", mod="+")
    else:
        show shiori annoyed
        shiori.say "No...no, I shouldn't."
        shiori.say "Or else I'll have a terrible headache in the morning."
        $ hero.cancel_activity()
        hide shiori
    return

label shiori_slap_ass_intro_male:
    "Sometimes I just can't believe how curvy Shiori actually is."
    "I mean, it's like some horny dude sat down and thought her up!"
    "She's a work of art when she walks along, a sure turn-on when she runs too!"
    "And that ass..."
    "I just can't keep myself from giving it a little slap!"
    return

label shiori_slap_ass_happy_male:
    "As soon as my hand makes contact with her butt, Shiori jumps."
    "And she lets out the cutest little cry of alarm too!"
    shiori.say "Ooh..."
    shiori.say "What was that?"
    shiori.say "Did...did you just slap my butt?"
    "I nod my head, not seeing why I should hide it."
    "And as soon as I do, I see Shiori's cheeks flush red."
    shiori.say "Well...I..."
    shiori.say "I guess it's okay if YOU do it, [hero.name]!"
    return

label shiori_slap_ass_angry_male:
    "As soon as my hand makes contact with her butt, Shiori jumps."
    "And she lets out the cutest little cry of alarm too!"
    shiori.say "Ooh..."
    shiori.say "What was that?"
    shiori.say "Did...did you just slap my butt?"
    "I nod my head, not seeing why I should hide it."
    "And as soon as I do, I see Shiori's cheeks flush red."
    shiori.say "Oh, I can't believe you'd do that!"
    shiori.say "That is SO mean, [hero.name]!"
    return

label shiori_breakup_male:
    show shiori
    "I've tried to come at this from every conceivable angle that I can imagine."
    "But there's just no other way that I can come out of this one."
    "No matter what I do, I'm going to end up as the villain of the piece."
    "So in the end, all I can do is grit my teeth and get on with it..."
    mike.say "Shiori..."
    mike.say "I have something that I really need to tell you."
    mike.say "Something really important..."
    "Shiori turns to face me, looking up from below."
    "Oh god - she looks so innocent and helpless."
    "Trusting too, like she's put herself totally into my hands!"
    shiori.say "Oh..."
    shiori.say "What is it, [hero.name]?"
    shiori.say "I'm listening."
    mike.say "It's about us, Shiori - you and me."
    shiori.say "Y...yes?"
    mike.say "I think...that we should stop seeing each other."
    show shiori annoyed
    "Shiori stares at me in silence for a moment."
    "It's like she literally can't process what I just said to her."
    "Then she looks down at her feet, shaking her head."
    show shiori sad
    shiori.say "Y...you're just the same."
    shiori.say "I thought you were different."
    shiori.say "But you're just the same as all men!"
    "The slap comes out of nowhere, taking me by complete surprise."
    "In the aftermath, as I hold my cheek, I don't know who's more shocked."
    "I'm stunned that Shiori even had it in her to slap me."
    "But she's staring at her hand like it's something she's never seen before."
    mike.say "Shiori, I..."
    "I'm too late to offer any words of comfort or explanation."
    "Instead I can only watch as Shiori bursts into tears and hurries away."
    "I have no idea what happens between us now, none at all."
    "But the fact we work in the same office is going to make things awkward..."
    return

label shiori_go_steady_intro_male:
    mike.say "I've really been enjoying our time together, Shiori."
    mike.say "Which is why I wanted to ask..."
    mike.say "Would you like to go steady with me?"
    return

label shiori_go_steady_yes_male:
    shiori.say "Y...you really mean it, [hero.name]?!?"
    shiori.say "I'd love to - of course I would!"
    hide shiori
    show shiori kiss
    $ shiori.flags.kiss += 1
    "Shiori almost leaps into my arms, wrapping herself around me."
    "Our lips meet, and she kisses me like her life depends on it."
    return

label shiori_go_steady_no_male:
    shiori.say "Oh...oh I don't know, [hero.name]..."
    shiori.say "I like you a lot, you have to know that's the truth."
    shiori.say "But I don't think I'm, ready for that yet!"
    return

label shiori_pet_intro_male:
    "Without a second thought, I pat Shiori on the head."
    "Her shortness makes it easy, almost too easy to do."
    "But the moment I'm finished, I wonder if I did the right thing."
    return

label shiori_pet_happy_male:
    shiori.say "Ooh...oh my..."
    shiori.say "Th...thank you, [hero.name]."
    shiori.say "You made me feel really special!"
    return

label shiori_pet_annoyed_male:
    shiori.say "Oh dear...oh dear..."
    shiori.say "You really shouldn't do that, [hero.name]."
    shiori.say "You know that you shouldn't!"
    return

label shiori_massage_intro_male:
    mike.say "Ooh...that looks like it hurts, Shiori!"
    mike.say "Why don't you come over here and let me take a look?"
    mike.say "I'm told I give a great massage."
    return

label shiori_massage_accept_male:
    shiori.say "Oh, yes, [hero.name]."
    shiori.say "That would be perfect."
    shiori.say "I bet you have magical, healing hands!"
    return

label shiori_massage_refuse_male:
    shiori.say "Oh, no, [hero.name]!"
    shiori.say "My doctor told that it's pretty bad."
    shiori.say "And that I should only let a professional handle it!"
    return

label shiori_piercing_nipples_reaction_male:
    shiori.say "I...I wasn't too sure about getting my nipples pierced, [hero.name]."
    shiori.say "But now that I know you like it..."
    shiori.say "Well, I'm starting to like it too!"
    return

label shiori_piercing_navel_reaction_male:
    shiori.say "D...does it look nice, [hero.name]?"
    shiori.say "I can't see it for my chest!"
    shiori.say "But so long as you like it, then I do too!"
    return

label shiori_piercing_clit_reaction_male:
    shiori.say "Ooh...it feels so strange down there!"
    shiori.say "But...you like it?"
    shiori.say "Right, [hero.name]?"
    shiori.say "Because if you like it, then I like it too!"
    return

label shiori_piercing_head_reaction_male:
    shiori.say "Oh...I hope this doesn't make my voice sound all funny..."
    shiori.say "And you'll still let me kiss you?"
    shiori.say "Won't you, [hero.name]?"
    shiori.say "Because that'll make it all worthwhile!"
    return

label shiori_piercing_nose_reaction_male:
    shiori.say "Does...does it look okay, [hero.name]?"
    shiori.say "Because I like it if you do."
    shiori.say "And you do like it, don't you?"
    return

label shiori_movie_disliked_reaction_male:
    shiori.say "Oh dear...I...I don't think I liked that movie at all!"
    return

label shiori_movie_indifferent_reaction_male:
    shiori.say "D...did you like the movie?"
    shiori.say "Because I just couldn't follow it!"
    return

label shiori_movie_liked_reaction_male:
    shiori.say "Oh, that was fantastic - thank you SO much for taking me to see it!"
    return

label shiori_belly_kiss_male:
    show shiori sad at center, zoomAt(1.25, (640, 880))
    shiori.say "Uf…"
    shiori.say "Oh..."
    shiori.say "Oh bother!"
    show shiori at center, traveling(1.5, 1.0, (640, 1040))
    "I look around to see Shiori walking towards me."
    "Or to be more precise, waddling in my general direction."
    "She's clutching her belly like it ways a literal ton."
    "And she looks totally beat too, utterly exhausted."
    "I hurry over to help, taking her hand in mine."
    "The other arm I use to support the small of her back."
    mike.say "Shiori..."
    mike.say "Are you okay?"
    show shiori stuned
    "But to my surprise, Shiori tries to pull away from me."
    show shiori annoyed
    "She even turns her head so I can't make eye-contact."
    show shiori whining
    shiori.say "Don't look at me, [hero.name]!"
    shiori.say "I'm so embarrassed to be seen..."
    shiori.say "I look like a big, fat cow!"
    show shiori annoyed
    "I refuse to be put off by Shiori's self-deprecating comments."
    show shiori surprised at center, traveling(2.0, 1.0, (640, 980))
    "And I pull her closer to me, going down on one knee at the same time."
    mike.say "Shiori..."
    mike.say "You're the most beautiful girl in the world."
    mike.say "And all I want to do is kiss this belly of yours."
    "Shiori makes a token attempt to resist as I pull up her top."
    "But when I start to gently kiss her belly, I feel her begin to relax."
    show shiori happy
    "And before too long she's clinging onto me, cooing and sighing."
    return

label shiori_belly_caress_male:
    show shiori whining at center, zoomAt(1.25, (640, 880))
    shiori.say "Oh, [hero.name]…"
    shiori.say "My belly getting so big."
    shiori.say "I'm going to be nothing but stretch-marks when this baby's born!"
    show shiori sad at center, traveling(1.5, 1.0, (640, 1040))
    "I can't help chuckling as I pull Shiori closer to me."
    "And without a conscious thought, my hand goes straight to her belly."
    mike.say "I'm sure it won't be as bad as all that, Shiori."
    mike.say "You already gave birth once."
    mike.say "And after that you still had a dynamite body!"
    show shiori sadsmile
    "Shiori leans her head on my shoulder as I fondly stroke her belly."
    "I can see that she's soothed by my words, but still nervous."
    mike.say "Let's worry about the future when it happens, yeah?"
    mike.say "After all, we're going to have our hands full with this little one!"
    "As if hearing us mention them, the baby chooses that moment to kick."
    show shiori happy
    "Shiori lets out a laugh, despite her former mood."
    "And I feel it lift my heart, on account of the delight I hear in it."
    show shiori talkative
    shiori.say "Did you see that, [hero.name]?"
    shiori.say "I think the baby recognises your voice!"
    shiori.say "Keep talking to them!"
    shiori.say "And keep your hand on my belly, please?"
    show shiori happy
    "Eager to raise Shiori's spirits, I do as she says."
    "Enjoying the chance to see her smiling and truly happy."
    return

label shiori_belly_listen_male:
    show shiori surprised at center, zoomAt(1.25, (640, 880))
    shiori.say "Ooh..."
    shiori.say "I think..."
    shiori.say "Oh yeah, the baby's moving!"
    show shiori normal at center, traveling(1.5, 0.3, (640, 1040))
    "I hurry to Shiori, already reaching out my hand to touch her belly."
    show shiori surprised at center, traveling(2.0, 1.0, (640, 980))
    "But then a thought occurs to me, and I kneel down in front of her again."
    show shiori normal
    shiori.say "What are you doing?"
    shiori.say "Why are you getting down on one knee?"
    mike.say "Relax, Shiori..."
    mike.say "I'm not going to propose!"
    mike.say "I just want to try something a little different, that's all."
    "Lifting the hem of Shiori's top, I turn my head to the side."
    "And then I place my ear against the curve of her belly."
    "Of course Shiori's not an idiot."
    "So she instantly knows what I'm doing."
    show shiori surprised
    shiori.say "Can you hear anything?"
    shiori.say "Well, can you?"
    "I wave my hand gently, gesturing for quiet."
    "Once Shiori obliges me, I begin to adjust."
    "And then I can hear it, the weird sounds of something moving in liquid."
    mike.say "Wow..."
    mike.say "It's like the ultrasound, Shiori..."
    mike.say "Like the baby's swimming around inside you!"
    show shiori happy
    shiori.say "Oh..."
    shiori.say "I wish we could record it."
    shiori.say "That way I could listen too!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
