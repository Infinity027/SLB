label hanna_ice_cream_reaction_male:
    mike.say "We need to cool down, Hanna - come on, let's go grab an ice cream!"
    hanna.say "Yeah - that sounds good to me!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Hanna chooses the same thing, but with her own combination of flavours."
    hanna.say "I love this stuff...but..."
    hanna.say "Urgh...damn it...come here!"
    "As Hanna tries to lick her cone, one of the scoops slips off."
    "It runs down her arm and she chases it with her tongue, licking desperately."
    "I can't take my eyes off her as she does this, it's just so suggestive."
    "And all I can think of is Hanna using her tongue like that in an intimate situation!"
    return

label hanna_ask_phone_male:
    mike.say "Can I have your number, Hanna?"
    mike.say "All I have for you is the gym number!"
    if hero.charm >= 20 - hanna.love:
        show hanna surprised
        $ hero.smartphone_contacts.append("hanna")
        hanna.say "What?!?"
        hanna.say "You don't have it?"
        show hanna happy
        hanna.say "Well, we can soon fix that!"
    else:
        show hanna annoyed
        $ hanna.love -= 1
        $ hanna.sub -= 1
        hanna.say "The gym number's fine for now, [hero.name]."
        hanna.say "Just ask the person on reception to take a message."
    return

label hanna_ask_birthday_male:
    mike.say "Your birthday, Hanna?"
    mike.say "Remind me when that is?"
    if hero.charm >= 40 - hanna.love:
        show hanna surprised
        $ hanna.flags.birthdayknown = True
        hanna.say "Huh?!?"
        show hanna annoyed
        hanna.say "I can't believe I didn't tell you already!"
        show hanna happy
        hanna.say "It's Fall 30."
    else:
        show hanna annoyed
        $ hanna.sub -= 1
        $ hanna.love -= 1
        hanna.say "Hey!"
        hanna.say "I don't look this good just because I work-out."
        hanna.say "And I'm not lying about my age either!"
    return

label hanna_offer_a_drink_male:
    mike.say "You want a drink, Hanna?"
    mike.say "I'm headed to the bar, so I can grab you one too."
    "Almost the second the words are out of my mouth, Hanna turns to face me."
    if hanna.is_visibly_pregnant:
        show hanna angry
        $ hanna.love -= 10
        hanna.say "Alcohol, [hero.name]?"
        hanna.say "Really?!?"
        hanna.say "Am I the only one looking out for this kid?"
        $ hero.cancel_activity()
        hide hanna
    elif (hero.charm >= 60 - hanna.love and hanna.flags.drinks < 2) or date_girl == hanna:
        show hanna happy
        hanna.say "Sure thing, [hero.name]."
        hanna.say "Mine's a light beer."
        hanna.say "And thanks for thinking of me!"
        hide hanna
        show drink hanna
        if hanna.love <= 25:
            $ hanna.love += 1
        elif date_girl == hanna and game.active_date:
            $ game.active_date.score += 5
        call expression hanna.get_chat from _call_expression_229
        hide drink hanna
        $ hanna.set_flag("drinks", 1, "day", mod="+")
    else:
        show hanna annoyed
        hanna.say "Urgh..."
        hanna.say "No, [hero.name], I do not."
        hanna.say "You know I'm on a health kick this month too!"
        $ hero.cancel_activity()
        hide hanna
    return

label hanna_slap_ass_intro_male:
    "I can't seem to take my eyes off of Hanna's ass today."
    "It's just so perfectly toned and pert as she walks along."
    "Like a living advertisement for the gym where she works."
    "I just can't keep myself from giving it a playful slap!"
    return

label hanna_slap_ass_happy_male:
    hanna.say "Whoa..."
    hanna.say "[hero.name]..."
    hanna.say "Did you just do what I think you did?!?"
    "I can feel myself flushing a little at the question."
    "But I force myself to nod all the same."
    hanna.say "You dog!"
    hanna.say "But all the same..."
    hanna.say "Thanks for the compliment!"
    return

label hanna_slap_ass_angry_male:
    hanna.say "Whoa..."
    hanna.say "[hero.name]..."
    hanna.say "Did you just do what I think you did?!?"
    "I can feel myself flushing a little at the question."
    "But I force myself to nod all the same."
    hanna.say "Urgh..."
    hanna.say "I can't believe you'd do that!"
    hanna.say "What are you - some kind of caveman?!?"
    return

label hanna_breakup_male:
    show hanna
    "I have to keep myself from looking at Hanna too much."
    "Because if I do, then I start getting distracted by how good she looks."
    "And that's not helpful when I have to do something as harsh as I have to now."
    "I need to keep focused, keep my eyes on the ultimate goal."
    "And I need to keep my eyes off of Hanna's ass..."
    mike.say "Hanna..."
    mike.say "We need to talk!"
    "Hanna gives me a lop-sided grin."
    "And then she shakes her head."
    hanna.say "Then you need to look at my face, [hero.name], not my ass!"
    hanna.say "What's on your mind?"
    "I let out a painful sigh, dreading what comes next."
    "But I have no choice other than to push on through it."
    mike.say "It's us, Hanna."
    mike.say "I think we need to see other people."
    mike.say "I'm sorry - but we're just now working out!"
    show hanna annoyed
    "Hanna frowns at this, narrowing her eyes."
    hanna.say "Is that supposed to be some kind of a joke?"
    mike.say "What?!?"
    mike.say "Oh...no, no."
    mike.say "I mean our relationship, Hanna."
    mike.say "I think we should end it."
    "Now I see the first signs of understanding appear on Hanna's face."
    "And it's not the most pleasant sight I've ever associated with her."
    show hanna angry
    hanna.say "Really, [hero.name]?"
    hanna.say "You're just gonna drop that one on me, huh?"
    hanna.say "Be all casual, like it's no big deal?!?"
    mike.say "No, Hanna, it's not like that!"
    mike.say "Of course it's a big deal!"
    hanna.say "Is it really?"
    hanna.say "Because from where I'm standing it doesn't feel like it."
    hanna.say "It feels like I've been throw away!"
    hanna.say "Like...like an old, sweaty sports bra!"
    hanna.say "Get the hell away from me, [hero.name]."
    hanna.say "And don't show your face at my gym again!"
    return

label hanna_go_steady_intro_male:
    mike.say "I was thinking, Hanna..."
    mike.say "We're great together, aren't we?"
    mike.say "So we should really go steady."
    return

label hanna_go_steady_yes_male:
    hanna.say "You're right, [hero.name]."
    hanna.say "We're like the power couple at the gym!"
    hanna.say "We should totally go steady!"
    "Hanna kisses me full on the lips."
    "Which I take as a reward for saying the right thing."
    return

label hanna_go_steady_no_male:
    hanna.say "Ah, I don't know, [hero.name]..."
    hanna.say "I'm having a great time with you."
    hanna.say "But I don't think we're there yet."
    return

label hanna_pet_intro_male:
    "I pat Hanna on the head even before I realise I'm doing it."
    "And instantly I know that it probably wasn't the best decision."
    "But all I can do now is hope that she takes it the right way..."
    return

label hanna_pet_happy_male:
    hanna.say "Wha..."
    hanna.say "Did you...did you just..."
    hanna.say "You did, didn't you?"
    hanna.say "And I liked it too - so you can do it again!"
    return

label hanna_pet_annoyed_male:
    hanna.say "Whoa..."
    hanna.say "Hold on a minute there, mister!"
    hanna.say "You won't be doing that to me again."
    return

label hanna_massage_intro_male:
    mike.say "Whoa, Hanna..."
    mike.say "You're knotted up like a rope!"
    mike.say "Let me give you a quick massage."
    mike.say "That'll fix you right up!"
    return

label hanna_massage_accept_male:
    hanna.say "Ah..."
    hanna.say "You're right, [hero.name]!"
    hanna.say "I think I need your hands on me."
    hanna.say "And quickly too!"
    return

label hanna_massage_refuse_male:
    hanna.say "Ah..."
    hanna.say "No thanks, [hero.name]."
    hanna.say "It feels like it might be serious."
    hanna.say "So I owe it to myself to have someone check it out at the gym."
    hanna.say "You know, someone that's qualified?"
    return

label hanna_piercing_nipples_reaction_male:
    hanna.say "I used to think just working out was enough to make me look good."
    hanna.say "But now that I see myself with these things in my nipples..."
    hanna.say "Well, they just make me look that much better!"
    return

label hanna_piercing_navel_reaction_male:
    hanna.say "Wow...I used to think my abs couldn't get any better."
    hanna.say "But this piercing really puts them over the top!"
    hanna.say "This was a great idea, [hero.name]!"
    return

label hanna_piercing_clit_reaction_male:
    hanna.say "I was worried that I wouldn't be able to show this thing off."
    hanna.say "But I can feel it with every step that In take!"
    hanna.say "I can't wait to see how it feels when I'm working out!"
    return

label hanna_piercing_head_reaction_male:
    hanna.say "Weird, I worked on almost every part of my body before now."
    hanna.say "But it never occurred to me to do anything to my tongue!"
    hanna.say "I guess I have you to thank for that, [hero.name]."
    return

label hanna_piercing_nose_reaction_male:
    hanna.say "I like the feel of this thing, [hero.name], and the look too."
    hanna.say "It was a great idea of yours for me to get pierced there."
    hanna.say "And it's already turning heads in my direction too!"
    return

label hanna_movie_disliked_reaction_male:
    hanna.say "Well, that movie stank worse than last week's workout gear!"
    return

label hanna_movie_indifferent_reaction_male:
    hanna.say "Huh...I was SO bored I stopped paying attention in there!"
    return

label hanna_movie_liked_reaction_male:
    hanna.say "Wow...I loved that movie - it really got my heart pumping!"
    return

label hanna_belly_kiss_male:
    show hanna whining at center, zoomAt(1.25, (640, 880))
    hanna.say "It's not fair..."
    hanna.say "I used to be fit..."
    show hanna angry
    hanna.say "Damn it, I used to be smoking hot!"
    show hanna upset at center, traveling(1.5, 0.3, (640, 1040))
    "At the sound of Hanna's voice, I rush over to her."
    "It seems that she's wailing in distress right now."
    "So I obviously want to know what the problem is."
    mike.say "Are you okay, Hanna?"
    mike.say "Is the baby okay?"
    show hanna sad
    "At the mere mention of the word 'baby', Hanna bursts into tears."
    "It's so loud and so sudden that I can't help taking a step backwards."
    show hanna whining
    hanna.say "Waah..."
    hanna.say "The baby..."
    hanna.say "That's all anyone cares about!"
    hanna.say "Nobody gives a shit about me anymore..."
    hanna.say "I'm just turning into a big, fat heifer!"
    show hanna sad
    "On the surface of things, what Hanna's saying sounds pretty stupid."
    "I've only grown to love her all the more since she's been pregnant."
    "And in terms of her looks, she's practically glowing right now."
    "Her body's trim and healthy, responding to motherhood perfectly."
    "Sure, she's gained weight, but it suits her, making her look weirdly hot."
    "But of course all of this means nothing in terms of what's going on inside of her head."
    show hanna at center, traveling(2.0, 0.5, (640, 980))
    "So I take a gamble, getting down on my knees."
    "And I start to plant kisses on her belly."
    show hanna surprised
    hanna.say "Wha..."
    hanna.say "What are you doing?"
    mike.say "What does it look like, Hanna?"
    mike.say "I'm getting down on my knees..."
    mike.say "And I'm worshipping you - because you're a total goddess!"
    show hanna confused
    hanna.say "You can't..."
    hanna.say "Well, I guess you could..."
    show hanna normal
    hanna.say "If you really wanted to..."
    hanna.say "Okay, okay...so long as you see me as the goddess of beauty."
    hanna.say "Not like, some weird cow-goddess or something!"
    return

label hanna_belly_caress_male:
    show hanna angry at center, zoomAt(1.25, (640, 880))
    "Hanna's had to seriously cut down on the time she's spending at the gym now she's pregnant."
    "I mean, she's started teaching classes specifically for women in her position."
    "But there's no way she can afford to be the totally unstoppable gym-bunny she usually is."
    "This means that she's put on a tiny bit of lumber recently, thanks to being less active."
    "Though at the same time, she's still wearing mainly tight, stretchy clothes."
    "Stuff that leaves nothing to the imagination, and her belly sticking out in front of her too!"
    "All of which means I can't help wanting to put my hands on her at every available opportunity."
    mike.say "Ooh..."
    mike.say "Hanna..."
    mike.say "Just let me..."
    show hanna annoyed at center, traveling(1.5, 0.5, (640, 1040))
    "Before I can finish what I was going to say, Hanna cuts me off."
    "And at the same time she barges her huge belly into me too!"
    show hanna angry
    hanna.say "Don't waste your breath asking, [hero.name]."
    hanna.say "I know what you're going to say."
    hanna.say "The same thing everyone says to me these days."
    show hanna whining
    hanna.say "'Oooh, can I touch your bump?'"
    show hanna upset
    "As my hands are already on Hanna's belly, I take that as permission."
    "And I happily begin to caress it, even while listening to he bemoan being pregnant."
    show hanna whining
    hanna.say "They used to want to get their hands on my flat-as-a-board abs."
    hanna.say "Or to feel how firm my biceps were."
    hanna.say "Hell, right now I'd even tolerate them wanting to pinch my ass!"
    hanna.say "But all they're interested in is this massive belly."
    show hanna sad
    "I'm doing the best I can to nod as Hanna goes on about it all."
    "But I'm not really paying attention to what she's saying."
    "Instead I smile as I feel the weight of her belly."
    "Already daydreaming about being a daddy."
    return

label hanna_belly_listen_male:
    show hanna talkative at center, zoomAt(1.25, (640, 880))
    pause 0.2
    show hanna at center, traveling(2.0, 1.0, (640, 980))
    hanna.say "Well..."
    hanna.say "Can you hear anything?"
    show hanna confused
    "With my ear pressed to Hanna's belly, I wave a hand in the air."
    mike.say "Not with you asking me questions I can't!"
    mike.say "Just be quiet for a minute, okay?"
    show hanna annoyed
    "I hear Hanna muttering under her breath as I say this."
    "But at least it means she's not speaking out loud."
    "And the lack of volume means I can actually hear something for the first time."
    show hanna normal
    "I do the best I can to make sure it's not Hanna's own heartbeat I'm hearing."
    "And then I'm sure it's a sound coming from the baby."
    mike.say "There it is..."
    mike.say "I can hear it..."
    mike.say "I can hear the baby moving!"
    show hanna surprised
    hanna.say "You can?"
    hanna.say "Oh, I'm so jealous!"
    hanna.say "If only there was a way I could listen too."
    show hanna normal
    hanna.say "Like, maybe we could record it or something?"
    "I nod absently, again not really hearing what Hanna's saying."
    "Because I can hear the sound of my unborn child moving around in there."
    "I've seen the scans and heard the sounds on the instruments at the hospital."
    "Burt somehow hearing it with my own ear makes the whole thing seem more real."
    "And it's in that moment the reality finally hits me."
    "Oh shit - I really am going to be a dad!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
