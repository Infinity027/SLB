label kat_ice_cream_reaction_male:
    "I thought today was going to be hot, but nothing prepared me for this!"
    "I'm baking in the heat, and one glance at Kat tells me she's feeling the same."
    mike.say "Urgh..."
    mike.say "We need ice-cream, Kat - and quick!"
    "Kat doesn't say a word, just nods in response."
    "And together we hurry over to the ice-cream stand."
    "I order my usual and watch as Kat does the same."
    "But she seems kind of shy and awkward as she's handed her ice-cream."
    "Sure, she starts to lick it, but she's half looking at me the whole time."
    "I try to make it look like I'm not watching her, but that's almost impossible."
    "Slowly I get the feeling Kat's warming to the attention I'm giving her."
    "She's still shy and awkward, but she seems to be blushing a little too."
    "Am I imagining things here..."
    "Or is she starting to make a little show out of this?"
    "Licking sensually and making sure that I see what she's doing?"
    "Whatever she's doing, I'm totally entranced."
    "That is until my own neglected ice-cream starts to melt."
    "The sensation of it dripping onto my hand makes me jump."
    "And just like that I snap back to reality."
    return

label kat_ice_cream_reaction_female:
    "I thought today was going to be hot, but nothing prepared me for this!"
    "I'm baking in the heat, and one glance at Kat tells me she's feeling the same."
    bree.say "Urgh..."
    bree.say "We need ice-cream, Kat - and quick!"
    "Kat doesn't say a word, just nods in response."
    "And together we hurry over to the ice-cream stand."
    "I order my usual and watch as Kat does the same."
    "But she seems kind of shy and awkward as she's handed her ice-cream."
    "Sure, she starts to lick it, but she's half looking at me the whole time."
    "I try to make it look like I'm not watching her, but that's almost impossible."
    "Slowly I get the feeling Kat's warming to the attention I'm giving her."
    "She's still shy and awkward, but she seems to be blushing a little too."
    "Am I imagining things here..."
    "Or is she starting to make a little show out of this?"
    "Licking sensually and making sure that I see what she's doing?"
    "Whatever she's doing, I'm totally entranced."
    "That is until my own neglected ice-cream starts to melt."
    "The sensation of it dripping onto my hand makes me jump."
    "And just like that I snap back to reality."
    return

label kat_ask_phone_male:
    "I make a point of getting out my phone."
    "And I make sure that Kat sees me scrolling through my contacts too."
    mike.say "Huh..."
    mike.say "I was just going to send you that game trailer we talked about the other day."
    mike.say "But I don't think I have your number on here yet!"
    mike.say "You wanna let me have it, Kat?"
    mike.say "Then I can send it to you."
    if hero.charm >= 20 - kat.love:
        show kat shy
        $ hero.smartphone_contacts.append("kat")
        "Kat frowns and shakes her head at this."
        kat.say "I thought I already gave you my number?"
        show kat smile
        kat.say "Well, we can soon sort that out!"
        kat.say "Here it is, [hero.name]."
        kat.say "Now you can get hold of me anytime you like!"
    else:
        $ kat.love -= 1
        $ kat.sub -= 1
        "Kat frowns and shakes her head at this."
        kat.say "If you don't have it, then I didn't give it to you."
        show kat shy
        kat.say "I'm pretty careful about giving out my contact details, [hero.name]."
        kat.say "So I'll let you have my number when you really need it."
        show kat normal
        kat.say "Until then, you have to do it the old-fashioned way."
    return

label kat_ask_phone_female:
    "I make a point of getting out my phone."
    "And I make sure that Kat sees me scrolling through my contacts too."
    bree.say "Huh..."
    bree.say "I was just going to send you that game trailer we talked about the other day."
    bree.say "But I don't think I have your number on here yet!"
    bree.say "You wanna let me have it, Kat?"
    bree.say "Then I can send it to you."
    if hero.charm >= 20 - kat.love:
        show kat shy
        $ hero.smartphone_contacts.append("kat")
        "Kat frowns and shakes her head at this."
        kat.say "I thought I already gave you my number?"
        show kat smile
        kat.say "Well, we can soon sort that out!"
        kat.say "Here it is, [hero.name]."
        kat.say "Now you can get hold of me anytime you like!"
    else:
        $ kat.love -= 1
        $ kat.sub -= 1
        "Kat frowns and shakes her head at this."
        kat.say "If you don't have it, then I didn't give it to you."
        show kat shy
        kat.say "I'm pretty careful about giving out my contact details, [hero.name]."
        kat.say "So I'll let you have my number when you really need it."
        show kat normal
        kat.say "Until then, you have to do it the old-fashioned way."
    return

label kat_ask_birthday_male:
    mike.say "Did you ever get round to telling me when your birthday is, Kat?"
    mike.say "I think you did, but I went and forgot the date."
    mike.say "You want to remind me?"
    mike.say "Because I'd like to do so something to mark the occasion."
    mike.say "You know, celebrate with you?"
    if hero.charm >= 40 - kat.love:
        show kat surprised
        $ kat.flags.birthdayknown = True
        "Kat's eyes open wide at the question."
        "And she raises her eyebrows too."
        kat.say "You really mean that, [hero.name]?"
        show kat shy
        kat.say "Most people just forget my birthday."
        kat.say "So I don't get to do anything special on the actual day."
        show kat smile
        kat.say "I'll remind you of the date."
        kat.say "But you have to promise me we'll do something special!"
    else:
        show kat shy
        $ kat.sub -= 1
        $ kat.love -= 1
        "Kat's brows furrow at the question."
        "And her lip curls into an odd shape too."
        kat.say "That's very personal information, [hero.name]."
        show kat angry
        kat.say "And if you forgot it, then that's on you!"
        kat.say "I don't go sharing details of my life with just anyone."
        kat.say "You want me to remind you of the date?"
        kat.say "Then you're going to have to prove to me that you can be trusted with the information!"
    return

label kat_ask_birthday_female:
    bree.say "Did you ever get round to telling me when your birthday is, Kat?"
    bree.say "I think you did, but I went and forgot the date."
    bree.say "You want to remind me?"
    bree.say "Because I'd like to do so something to mark the occasion."
    bree.say "You know, celebrate with you?"
    if hero.charm >= 40 - kat.love:
        show kat surprised
        $ kat.flags.birthdayknown = True
        "Kat's eyes open wide at the question."
        "And she raises her eyebrows too."
        kat.say "You really mean that, [hero.name]?"
        show kat shy
        kat.say "Most people just forget my birthday."
        kat.say "So I don't get to do anything special on the actual day."
        show kat smile
        kat.say "I'll remind you of the date."
        kat.say "But you have to promise me we'll do something special!"
    else:
        show kat shy
        $ kat.sub -= 1
        $ kat.love -= 1
        "Kat's brows furrow at the question."
        "And her lip curls into an odd shape too."
        kat.say "That's very personal information, [hero.name]."
        show kat angry
        kat.say "And if you forgot it, then that's on you!"
        kat.say "I don't go sharing details of my life with just anyone."
        kat.say "You want me to remind you of the date?"
        kat.say "Then you're going to have to prove to me that you can be trusted with the information!"
    return

label kat_offer_a_drink_male:
    "I stand up and wave my empty glass in the air."
    "And I make sure that I catch Kat's eye as I do so."
    mike.say "Looks like it's time for another round!"
    mike.say "Can I get you one too, Kat?"
    mike.say "The same again?"
    if kat.is_visibly_pregnant:
        show kat surprised
        $ kat.love -= 10
        "Kat looks at me with genuine surprise."
        "Which puzzles me, until I look down and see her swollen belly."
        kat.say "I don't think that's a good idea, [hero.name]!"
        kat.say "Not in my current condition."
        mike.say "Erm..."
        mike.say "No, Kat..."
        mike.say "You're probably right!"
        $ hero.cancel_activity()
        hide kat
    elif (hero.charm >= 60 - kat.love and kat.flags.drinks < 2) or date_girl == kat:
        "Kat looks at her own glass, which is all but empty too."
        "Then she looks back at me."
        show kat happy
        kat.say "Sure, [hero.name]."
        kat.say "That sounds like a great idea."
        kat.say "So long as you're not trying to get me drunk!"
        hide kat
        show drink kat
        if kat.love <= 25:
            $ kat.love += 1
        elif date_girl == kat and game.active_date:
            $ game.active_date.score += 5
        call expression kat.get_chat from _call_expression_479
        hide drink kat
        $ kat.set_flag("drinks", 1, "day", mod="+")
    else:
        kat.say "Sorry, I don't feel like drinking."
        $ hero.cancel_activity()
    return

label kat_offer_a_drink_female:
    "I stand up and wave my empty glass in the air."
    "And I make sure that I catch Kat's eye as I do so."
    bree.say "Looks like it's time for another round!"
    bree.say "Can I get you one too, Kat?"
    bree.say "The same again?"
    if hero.is_visibly_pregnant:
        show kat surprised
        $ kat.love -= 10
        "Kat looks at me with genuine surprise."
        "Which puzzles me, until I look down and see her staring at my swollen belly."
        kat.say "I don't think that's a good idea, [hero.name]!"
        kat.say "Not in your current condition."
        bree.say "Erm..."
        bree.say "No, Kat..."
        bree.say "You're probably right!"
        $ hero.cancel_activity()
        hide kat
    elif (hero.charm >= 60 - kat.love and kat.flags.drinks < 2) or date_girl == kat:
        "Kat looks at her own glass, which is all but empty too."
        "Then she looks back at me."
        show kat happy
        kat.say "Sure, [hero.name]."
        kat.say "That sounds like a great idea."
        kat.say "So long as you're not trying to get me drunk!"
        hide kat
        show drink kat
        if kat.love <= 25:
            $ kat.love += 1
        elif date_girl == kat and game.active_date:
            $ game.active_date.score += 5
        call expression kat.get_chat from _call_expression_480
        hide drink kat
        $ kat.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        kat.say "Sorry, I don't feel like drinking."
    return

label kat_slap_ass_intro_male:
    "Kat's not exactly the most buxom of girls, if you know what I mean?"
    "Sure, she's got everything she needs to be feminine and sexy."
    "But it's all sleek and slender, very petite in size."
    "That doesn't mean her ass is anything less than hypnotic though!"
    "Every time she walks past me, I feel the urge to reach out and touch it."
    "I have to fight it for all I'm worth."
    "But I just know that I won't be able to resist forever!"

    return

label kat_slap_ass_intro_female:
    kat.say "OW!"
    kat.say "What the..."
    kat.say "What just happened?!?"
    "Did I just..."
    "Did I just slap Kat's ass without realising it?"
    mike.say "Erm..."
    mike.say "My bad, Kat..."
    mike.say "I just couldn't help myself!"
    "Kat's not exactly the most buxom of girls, if you know what I mean?"
    "Sure, she's got everything she needs to be feminine and sexy."
    "But it's all sleek and slender, very petite in size."
    "That doesn't mean her ass is anything less than hypnotic though!"
    "Every time she walks past me, I feel the urge to reach out and touch it."
    "I have to fight it for all I'm worth."
    "But I just know that I won't be able to resist forever!"
    kat.say "OW!"
    kat.say "What the..."
    kat.say "What just happened?!?"
    "Did I just..."
    "Did I just slap Kat's ass without realising it?"
    bree.say "Erm..."
    bree.say "My bad, Kat..."
    bree.say "I just couldn't help myself!"
    return

label kat_slap_ass_happy_male:
    kat.say "OW!"
    kat.say "What the..."
    kat.say "What just happened?!?"
    "Did I just..."
    "Did I just slap Kat's ass without realising it?"
    mike.say "Erm..."
    mike.say "My bad, Kat..."
    mike.say "I just couldn't help myself!"
    "Kat's normally demure expression changes in an instant."
    "Where before she was confused and embarrassed, she's now smiling."
    "But at the same time her cheeks are still flushed with colour."
    kat.say "I..."
    kat.say "I guess it's okay, [hero.name]."
    kat.say "But only because it's you!"
    kat.say "Just give me a little notice next time, okay?"
    kat.say "I...I might want you to do it again..."
    kat.say "And maybe a little harder too!"
    return

label kat_slap_ass_happy_female:
    "Kat's normally demure expression changes in an instant."
    "Where before she was confused and embarrassed, she's now smiling."
    "But at the same time her cheeks are still flushed with colour."
    kat.say "I..."
    kat.say "I guess it's okay, [hero.name]."
    kat.say "But only because it's you!"
    kat.say "Just give me a little notice next time, okay?"
    kat.say "I...I might want you to do it again..."
    kat.say "And maybe a little harder too!"
    return

label kat_slap_ass_angry_male:
    "Kat's normally demure expression changes in an instant."
    "Where before she was confused and embarrassed, she's now purely angry."
    "And she doesn't hesitate to tell me exactly how she feels about it."
    kat.say "Don't smile at me like that, [hero.name]!"
    kat.say "Where do you get off doing something like that?"
    kat.say "You think you can just touch me anytime you like?!?"
    kat.say "Well you can't!"
    kat.say "So just keep your hands to yourself in future."
    return

label kat_slap_ass_angry_female:
    "Kat's normally demure expression changes in an instant."
    "Where before she was confused and embarrassed, she's now purely angry."
    "And she doesn't hesitate to tell me exactly how she feels about it."
    kat.say "Don't smile at me like that, [hero.name]!"
    kat.say "Where do you get off doing something like that?"
    kat.say "You think you can just touch me anytime you like?!?"
    kat.say "Well you can't!"
    kat.say "So just keep your hands to yourself in future."
    return

label kat_breakup_male:
    "I hate doing this kind of thing, it's never easy and it's always painful."
    "But I guess it's like tearing a plaster off a wound - best to do it quickly."
    "So I take a deep breath and look Kat straight in the eye."
    mike.say "Kat..."
    mike.say "I need to talk to you about something."
    "Kat's expression changes as she reads the look on my face and in my eyes."
    "It goes from mere interest to worry and visible anxiety in mere seconds."
    kat.say "[hero.name]..."
    kat.say "I'm not going to like this, am I?"
    mike.say "No, Kat - but I have to say it."
    mike.say "It's us, this relationship..."
    mike.say "I just don't think it's working out."
    mike.say "Not how either of us hoped it would."
    "Something flares in Kat's eyes for a moment, and she opens her mouth."
    "I think she's going to argue against me, to plead for another chance."
    "But then it seems to die down, and she just nods her head."
    kat.say "Oh, [hero.name]..."
    kat.say "I didn't want to admit it - but I've been feeling the same."
    kat.say "Maybe if we admit it now, we can still salvage something?"
    kat.say "Like, we could still be friends?"
    mike.say "We can only try, Kat."
    mike.say "We can only try."
    return

label kat_breakup_female:
    "I hate doing this kind of thing, it's never easy and it's always painful."
    "But I guess it's like tearing a plaster off a wound - best to do it quickly."
    "So I take a deep breath and look Kat straight in the eye."
    bree.say "Kat..."
    bree.say "I need to talk to you about something."
    "Kat's expression changes as she reads the look on my face and in my eyes."
    "It goes from mere interest to worry and visible anxiety in mere seconds."
    kat.say "[hero.name]..."
    kat.say "I'm not going to like this, am I?"
    bree.say "No, Kat - but I have to say it."
    bree.say "It's us, this relationship..."
    bree.say "I just don't think it's working out."
    bree.say "Not how either of us hoped it would."
    "Something flares in Kat's eyes for a moment, and she opens her mouth."
    "I think she's going to argue against me, to plead for another chance."
    "But then it seems to die down, and she just nods her head."
    kat.say "Oh, [hero.name]..."
    kat.say "I didn't want to admit it - but I've been feeling the same."
    kat.say "Maybe if we admit it now, we can still salvage something?"
    kat.say "Like, we could still be friends?"
    bree.say "We can only try, Kat."
    bree.say "We can only try."
    return

label kat_go_steady_intro_male:
    "I'm always nervous when I ask a girl something like this."
    "And in Kat's case, it's no exception to the norm."
    "I'm looking awkward and avoiding her eye."
    "So much so that she's moved to call me out on it."
    kat.say "[hero.name], what's the matter?"
    mike.say "Ah, well..."
    mike.say "I kinda wanted to ask you something, Kat..."
    kat.say "Okay, [hero.name], ask away!"
    mike.say "Erm...I was wondering..."
    mike.say "Would you like to...maybe...go steady?"
    return

label kat_go_steady_intro_female:
    "I'm always nervous when I ask a girl something like this."
    "And in Kat's case, it's no exception to the norm."
    "I'm looking awkward and avoiding her eye."
    "So much so that she's moved to call me out on it."
    kat.say "[hero.name], what's the matter?"
    bree.say "Ah, well..."
    bree.say "I kinda wanted to ask you something, Kat..."
    kat.say "Okay, [hero.name], ask away!"
    bree.say "Erm...I was wondering..."
    bree.say "Would you like to...maybe...go steady?"
    return

label kat_go_steady_yes_male:
    "Now it's Kat's turn to look nervous, like she's been put on the spot."
    "She glances this way and that, like she's afraid to look me in the eye too."
    "But then she seems to pluck up the courage to give me an answer."
    kat.say "Oh, [hero.name]..."
    kat.say "I've been hoping you'd ask me that!"
    kat.say "Of course I want to go steady with you!"
    kat.say "I would have asked you myself..."
    kat.say "But I could never find the courage."
    return

label kat_go_steady_yes_female:
    "Now it's Kat's turn to look nervous, like she's been put on the spot."
    "She glances this way and that, like she's afraid to look me in the eye too."
    "But then she seems to pluck up the courage to give me an answer."
    kat.say "Oh, [hero.name]..."
    kat.say "I've been hoping you'd ask me that!"
    kat.say "Of course I want to go steady with you!"
    kat.say "I would have asked you myself..."
    kat.say "But I could never find the courage."
    return

label kat_go_steady_no_male:
    "Now it's Kat's turn to look nervous, like she's been put on the spot."
    "She glances this way and that, like she's afraid to look me in the eye too."
    "But then she lets out a sigh and shakes her head."
    kat.say "Oh, [hero.name]..."
    kat.say "It's sweet of you to ask me like that."
    kat.say "But I don't think we're in that place right now."
    kat.say "So I'm going to have to say no."
    return

label kat_go_steady_no_female:
    "Now it's Kat's turn to look nervous, like she's been put on the spot."
    "She glances this way and that, like she's afraid to look me in the eye too."
    "But then she lets out a sigh and shakes her head."
    kat.say "Oh, [hero.name]..."
    kat.say "It's sweet of you to ask me like that."
    kat.say "But I don't think we're in that place right now."
    kat.say "So I'm going to have to say no."
    return

label kat_pet_intro_male:
    "Kat just seems to get cuter every time I look at her."
    "And I can't stop looking at her, so it's getting out of control!"
    "I feel like I'm losing the ability to think straight around her."
    "Instinct is winning over willpower."
    "And the next time I walk past her..."
    kat.say "HEY!"
    kat.say "What was that?!?"
    "Kat leaps up and confronts me, hands on her hips."
    kat.say "Did you just pat me on the head?"
    kat.say "Why would you do something like that?"
    mike.say "I'm sorry, Kat..."
    mike.say "You're just so cute."
    mike.say "I guess I couldn't resist!"
    return

label kat_pet_intro_female:
    "Kat just seems to get cuter every time I look at her."
    "And I can't stop looking at her, so it's getting out of control!"
    "I feel like I'm losing the ability to think straight around her."
    "Instinct is winning over willpower."
    "And the next time I walk past her..."
    kat.say "HEY!"
    kat.say "What was that?!?"
    "Kat leaps up and confronts me, hands on her hips."
    kat.say "Did you just pat me on the head?"
    kat.say "Why would you do something like that?"
    bree.say "I'm sorry, Kat..."
    bree.say "You're just so cute."
    bree.say "I guess I couldn't resist!"
    return

label kat_pet_happy_male:
    "For a moment I think Kat's going to tear a strip off of me."
    "But then I see her begin to blush, and she looks away."
    kat.say "You..."
    kat.say "You really mean that, [hero.name]?"
    kat.say "That I'm cute, like a pet or something?"
    mike.say "I...I don't know about a pet, Kat..."
    mike.say "But you're definitely cute."
    mike.say "And I really can't resist you!"
    "Kat flutters her eyelids and starts to giggle."
    kat.say "Well..."
    kat.say "Maybe that's something I could get used to!"
    return

label kat_pet_happy_female:
    "For a moment I think Kat's going to tear a strip off of me."
    "But then I see her begin to blush, and she looks away."
    kat.say "You..."
    kat.say "You really mean that, [hero.name]?"
    kat.say "That I'm cute, like a pet or something?"
    bree.say "I...I don't know about a pet, Kat..."
    bree.say "But you're definitely cute."
    bree.say "And I really can't resist you!"
    "Kat flutters her eyelids and starts to giggle."
    kat.say "Well..."
    kat.say "Maybe that's something I could get used to!"
    return

label kat_pet_annoyed_male:
    "My explanation doesn't seem to satisfy Kat."
    "And it certainly doesn't do anything to calm her down either!"
    kat.say "So that's all I am to you, huh?"
    kat.say "Something cute that you can pet when the urge takes you?!?"
    "I back off a little, shaking my head."
    mike.say "No, Kat - it's not like that!"
    kat.say "It isn't?"
    kat.say "Well that's not how it looks from where I'm standing!"
    kat.say "Go buy yourself a dog if you want something to pet!"
    return

label kat_pet_annoyed_female:
    "My explanation doesn't seem to satisfy Kat."
    "And it certainly doesn't do anything to calm her down either!"
    kat.say "So that's all I am to you, huh?"
    kat.say "Something cute that you can pet when the urge takes you?!?"
    "I back off a little, shaking my head."
    bree.say "No, Kat - it's not like that!"
    kat.say "It isn't?"
    kat.say "Well that's not how it looks from where I'm standing!"
    kat.say "Go buy yourself a dog if you want something to pet!"
    return

label kat_massage_intro_male:
    kat.say "OW!"
    kat.say "Ow, ow, ow!"
    "I jump back a little as Kat yelps in pain."
    "But I regret it when I see that she's one hundred percent genuine."
    mike.say "What's the matter, Kat?"
    mike.say "That sounded painful!"
    "She nods, seemingly grateful for the sympathy."
    kat.say "Let's just say spending hours hunched over a controller's not good, [hero.name]."
    kat.say "At least not for your muscles!"
    kat.say "I think I pulled something important pretty badly."
    mike.say "You want me to take a look, Kat?"
    mike.say "Maybe give you a massage?"
    mike.say "I'm a gamer too - so I know where it hurts!"
    return

label kat_massage_intro_female:
    kat.say "OW!"
    kat.say "Ow, ow, ow!"
    "I jump back a little as Kat yelps in pain."
    "But I regret it when I see that she's one hundred percent genuine."
    bree.say "What's the matter, Kat?"
    bree.say "That sounded painful!"
    "She nods, seemingly grateful for the sympathy."
    kat.say "Let's just say spending hours hunched over a controller's not good, [hero.name]."
    kat.say "At least not for your muscles!"
    kat.say "I think I pulled something important pretty badly."
    bree.say "You want me to take a look, Kat?"
    bree.say "Maybe give you a massage?"
    bree.say "I'm a gamer too - so I know where it hurts!"
    return

label kat_massage_accept_male:
    "Kat seems to think about it for a moment."
    "And she nods her head, even though it seems to cause her more pain."
    kat.say "I guess I could let you do that, [hero.name]."
    kat.say "I can't wait to see a professional."
    kat.say "And you can hardly make it worse than it already is!"
    "I nod and smile."
    "But I'm secretly hoping she's right about that last point!"
    return

label kat_massage_accept_female:
    "Kat seems to think about it for a moment."
    "And she nods her head, even though it seems to cause her more pain."
    kat.say "I guess I could let you do that, [hero.name]."
    kat.say "I can't wait to see a professional."
    kat.say "And you can hardly make it worse than it already is!"
    "I nod and smile."
    "But I'm secretly hoping she's right about that last point!"
    return

label kat_massage_refuse_male:
    "At the mere mention of my touching her, Kat backs off."
    "And she shakes her head, even though it seems to cause her more pain."
    kat.say "Thanks, but no thanks!"
    kat.say "I appreciate the offer, [hero.name]."
    kat.say "I don't want to make things worse."
    kat.say "What I need is to see a professional."
    return

label kat_massage_refuse_female:
    "At the mere mention of my touching her, Kat backs off."
    "And she shakes her head, even though it seems to cause her more pain."
    kat.say "Thanks, but no thanks!"
    kat.say "I appreciate the offer, [hero.name]."
    kat.say "I don't want to make things worse."
    kat.say "What I need is to see a professional."
    return

label kat_piercing_nipples_reaction_male:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    mike.say "Whoa..."
    mike.say "You had your..."
    kat.say "My nipples pierced, yeah!"
    kat.say "You like it?"
    mike.say "You bet I do, Kat!"
    mike.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_nipples_reaction_female:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    bree.say "Whoa..."
    bree.say "You had your..."
    kat.say "My nipples pierced, yeah!"
    kat.say "You like it?"
    bree.say "You bet I do, Kat!"
    bree.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_navel_reaction_male:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    mike.say "Whoa..."
    mike.say "You had your..."
    kat.say "My navel pierced, yeah!"
    kat.say "You like it?"
    mike.say "You bet I do, Kat!"
    mike.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_navel_reaction_female:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    bree.say "Whoa..."
    bree.say "You had your..."
    kat.say "My navel pierced, yeah!"
    kat.say "You like it?"
    bree.say "You bet I do, Kat!"
    bree.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_clit_reaction_male:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    mike.say "Whoa..."
    mike.say "You had your..."
    kat.say "My clit pierced, yeah!"
    kat.say "You like it?"
    mike.say "You bet I do, Kat!"
    mike.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_clit_reaction_female:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    bree.say "Whoa..."
    bree.say "You had your..."
    kat.say "My clit pierced, yeah!"
    kat.say "You like it?"
    bree.say "You bet I do, Kat!"
    bree.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_head_reaction_male:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    mike.say "Whoa..."
    mike.say "You had your..."
    kat.say "My tongue pierced, yeah!"
    kat.say "You like it?"
    mike.say "You bet I do, Kat!"
    mike.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_head_reaction_female:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    bree.say "Whoa..."
    bree.say "You had your..."
    kat.say "My tongue pierced, yeah!"
    kat.say "You like it?"
    bree.say "You bet I do, Kat!"
    bree.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_nose_reaction_male:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    mike.say "Whoa..."
    kat.say "You like it?"
    mike.say "You bet I do, Kat!"
    mike.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_piercing_nose_reaction_female:
    kat.say "[hero.name]..."
    kat.say "Come over here..."
    kat.say "I have something to show you!"
    "I do as Kat says, eager to see what it could be."
    "And once I'm up close, it's pretty hard to miss!"
    bree.say "Whoa..."
    kat.say "You like it?"
    bree.say "You bet I do, Kat!"
    bree.say "That is SO hot!"
    "Kat grins, clearly delighted with my response."
    return

label kat_belly_kiss_male:
    show kat normal at center, zoomAt(1.25, (640, 880))
    "Most of Kat's wardrobe seems to be stuff that doesn't quite cover her up."
    "T-shirts, tops, skirts, all of which are designed to show off her slight figure."
    "But now that she's sporting an impressive baby-bump, things are a little different."
    "Now her belly juts out from under those cropped tops like it's trying to escape!"
    "And she always seems to be trying to pull something up or down to cover herself."
    "I know that I should be sympathetic and help out all I can."
    "But the problem is that it's kinda cute, and I like watching her doing it."
    show kat annoyed
    kat.say "Damn it!"
    kat.say "How did I..."
    kat.say "How did I get so fat!"
    show kat upset
    mike.say "Erm..."
    mike.say "I thought you might remember that, Kat..."
    mike.say "I was there at the time, and it's kind of etched into my mind!"
    "Kat looks up from her belly, and instinctively tries to cover it."
    "She has her hands wrapped around it, making it look like she's clutching a basket ball."
    "And the expression on her face tells me that she's not at all amused."
    show kat angry
    kat.say "Oh yeah, I remember now..."
    kat.say "This is at least fifty percent your fault!"
    show kat upset
    mike.say "I admit it, Kat..."
    mike.say "You got me bang to rights, guilty as charged."
    show kat at center, traveling(1.5, 0.3, (640, 940))
    "I'm in the process of kneeling down as I'm saying all of this."
    mike.say "And given the chance, I'd do it all over again!"
    "I close my eyes as I finish speaking."
    show kat at center, traveling(2.0, 1.0, (640, 980))
    "And then I lean in close enough to plant a kiss on Kat's belly."
    "Then another, and another, travelling all over the curve of it."
    "My guess is that this won't take long to mollify her."
    "And I'm proven right as I feel her relaxing, little by little."
    show kat surprised
    "But it's when she lets out a genuine sigh of relief that I know I've pulled it off."
    "Which means that I can go right on planting kisses on her belly without any concern."
    show kat happy
    "Secure in the knowledge that every successive one is helping to lighten her mood."
    "And I have to say that it's having a similar effect on me too."
    return

label kat_belly_caress_male:
    show kat annoyed at center, zoomAt(1.25, (640, 880))
    kat.say "Ah..."
    kat.say "Uh..."
    kat.say "Urgh!"
    show kat sad
    "I look up to see Kat grimacing as she shifts the weight of her not inconsiderable belly."
    "And it's still a pretty strange thing to see on a girl usually as skinny as she is."
    "But I almost burst out laughing as I see Kat trying to balance a joypad on top of it."
    "Because I realise that most of her frustration is from how it's getting in the way of her gaming."
    mike.say "Are you okay, Kat?"
    mike.say "Because you look kind of stressed out."
    show kat upset
    "Kat's head snaps round, and there's s pretty pissed expression on her face."
    "But then she seems to remember who she's talking too."
    "That and she probably reads from my face that I'm trying to offer her sympathy."
    show kat angry
    kat.say "Oh, you know what the problem is, [hero.name]…"
    kat.say "I just can't get used to this damn bump!"
    kat.say "No matter what I do, it's always in the way."
    show kat upset
    "I shrug and shake my head as I move closer to Kat."
    show kat normal at center, traveling(1.5, 0.3, (640, 1040))
    "At the same time I'm reaching out to put a hand on her belly."
    mike.say "At least it's only temporary, Kat."
    mike.say "In a couple of months, you'll be back to your normal size."
    mike.say "And until then, you can just ask me to hold it for you."
    "I make a point of putting my hand underneath Kat's stomach as I say this."
    "Pretending to support it's weight as I caress her soft, warm skin."
    "And it doesn't seem to take long for this to have an effect on her mood."
    show kat happy
    "Kat sighs, and then stretches out, like a cat relaxing before sleep."
    kat.say "Mmm..."
    kat.say "That does make it feel a little better."
    kat.say "You think you can keep that up for a while longer?"
    mike.say "I'll do my best, okay?"
    return

label kat_belly_listen_male:
    show kat normal at center, zoomAt(1.25, (640, 880))
    pause 0.1
    show kat at center, traveling(2.0, 1.0, (640, 980))
    "I already have my ear to Kat's belly before she realises what's going on."
    "And I'm struggling to hear all that I can as she starts to ask the inevitable questions."
    show kat surprised
    kat.say "Erm..."
    kat.say "What are you doing down there?"
    kat.say "I'd kinda like to know as that's part of my anatomy!"
    "I wave a hand, trying to get Kat to quiet down."
    mike.say "Shh!"
    mike.say "I'm trying to listen to the thing inside there."
    mike.say "The thing I have a fifty percent stake in, remember?"
    "Almost as soon as she hears this, Kat's mood changes."
    "Now it seems like she's extremely interested in what I'm doing."
    "To the point of wanting in on it."
    show kat happy
    kat.say "Oh..."
    kat.say "Well why didn't you just say that?"
    kat.say "So what can you hear?"
    kat.say "Whatever it is, I want to know!"
    "I nod my head, ready to report my findings back to Kat."
    "But at the moment I don't seem to be able to make much out."
    show kat normal
    "So I redouble my efforts, trying to block out everything else."
    "And only then do I begin to be able to hear something from inside."
    "It's weird and hard to pin down what I'm actually listening to."
    "But I figure that it can only be the sound of the kid moving around in there."
    "It's definitely something moving in liquid, swirling and shifting restlessly."
    "So I start to relate what I can hear to Kat."
    "Trying to phrase it in a way that at least kind of makes sense."
    "I don't know if I manage to pull if off or not."
    show kat surprised
    "But she seems to be very interested in what I have to say all the same."
    "So I guess genuine interest in the baby is what makes her pay such close attention."
    show kat happy
    "All of which is fine with me, as I feel that we're bonding every moment this is going on."
    "And that can only be a good thing, a positive for the future."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
