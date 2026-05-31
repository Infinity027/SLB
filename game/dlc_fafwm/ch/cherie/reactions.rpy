label cherie_ice_cream_reaction_male:
    "The sun is mercilessly beating down on us today, but I think I've spotted the answer."
    mike.say "It's so hot today, Cherie - I think we need to cool down."
    mike.say "How about an ice-cream?"
    "At the mere mention of grabbing an ice-cream, Cherie's eyes seem to light up."
    if cherie.sub >= 66:
        cherie.say "If that is what you want, [hero.name]."
        cherie.say "Then that is what we will do."
    else:
        cherie.say "What a fantastic idea, [hero.name]..."
        cherie.say "I haven't had one of those in as long as I can remember!"
    "Together we hurry over to the ice-cream stand and choose what we want from the menu."
    "And once we have our orders, we walk off, already licking away at them."
    "But it's hard for me to concentrate on eating my own ice-cream."
    "Because the sight of Cherie licking hers is almost too graphic for a public place!"
    return


label cherie_ask_phone_male:
    "I'm casually scrolling through the numbers on my phone, when I realise something."
    "Cherie and I have known each other for a short while by now."
    "But I don't seem to have her number stored down here on my phone."
    "Which is a situation that I can't let stand."
    "So the best course of action is to just raise the subject with her."
    mike.say "Hey, Cherie..."
    mike.say "I just realised, I don't have your number yet!"
    if hero.charm >= 20 - cherie.love:
        $ hero.smartphone_contacts.append("cherie")
        "Cherie looks up with a surprised expression on her face."
        "And I can see that she's already reaching for her phone."
        if cherie.sub >= 66:
            cherie.say "You do not have it?"
            cherie.say "Oh, I am such a forgetful mess!"
            cherie.say "Of course you shall have my number."
            cherie.say "And you may use it as often as you please."
        else:
            cherie.say "Oh no..."
            cherie.say "No, no, no..."
            cherie.say "That will not do at all!"
            cherie.say "You must be able to reach me whenever you please!"
        "I can't help smiling as Cherie furnishes me with the number."
        "Not to mention making it clear that she expects me to use it too."
        "I hurry to enter it into the directory of my phone."
        "Already thinking up excuses to message or call Cherie at short notice."
    else:
        "Cherie looks up with a knowing expression on her face."
        $ cherie.love -= 1
        $ cherie.sub -= 1
        if cherie.sub >= 66:
            cherie.say "Oh, [hero.name], I would give you literally anything else right now."
            cherie.say "But you must forgive me, for this I cannot do, not yet!"
        else:
            cherie.say "Of course you don't, [hero.name]..."
            cherie.say "Because I haven't given it to you yet!"
        "I find myself nodding dumbly, waiting for Cherie to say more."
        mike.say "So..."
        mike.say "Are you going to?"
        mike.say "Give it to me, that is?"
        if cherie.sub >= 66:
            cherie.say "When the time is right, {i}mon ami{/i}, when the time is right!"
        else:
            cherie.say "Patience, {i}mon ami{/i} - I will give it to you once you have earned it."
        "All I can do is nod and smile as Cherie says all of this."
        "Because I can't exactly demand that she give me her number, now can I?"
    return

label cherie_ask_birthday_male:
    "I'm thinking about the kind of random things that pass through my head on an average day."
    "But suddenly something occurs to me when I think about the dates that I have to remember."
    "Most of them are birthdays of friends and relatives, but one is missing."
    mike.say "Oh, Cherie..."
    mike.say "I just realised that I don't know the date of your birthday."
    if hero.charm >= 40 - cherie.love:
        $ cherie.flags.birthdayknown = True
        show cherie stuned
        "Cherie looks up with a surprised expression on her face."
        "And I can see that she's already shaking her head"
        if cherie.sub >= 66:
            show cherie surprised
            cherie.say "You do not have it?"
            show cherie happy
            cherie.say "Oh, I am such a forgetful mess!"
            cherie.say "Of course you shall have the date."
            show cherie talkative
            cherie.say "But please do not think that obliges you to mark the occasion in any way."
        else:
            show cherie surprised
            cherie.say "Oh no..."
            cherie.say "No, no, no..."
            cherie.say "That will not do at all!"
            show cherie talkative
            cherie.say "You must know the exact date, {i}mon ami{/i}..."
            show cherie happy
            cherie.say "Otherwise how will we be able to celebrate together?"
        show cherie smile
        "I can't help smiling as Cherie whispers the date to me."
        "I hurry to enter it into the directory of my phone."
        "Already thinking of what the celebrations she mentioned might entail."
    else:
        $ cherie.sub -= 1
        $ cherie.love -= 1
        show cherie stuned
        "Cherie looks up with a scandalised expression on her face."
        "And I can see that she's already shaking her head."
        if cherie.sub >= 66:
            show cherie talkative
            cherie.say "Oh, [hero.name], I would give you literally anything else right now."
            cherie.say "But you must forgive me, for this I cannot do, not yet!"
        else:
            show cherie whining
            cherie.say "Oh, [hero.name]..."
            cherie.say "I thought that you were a gentleman?"
            cherie.say "You should know that you never ask a woman her age!"
        show cherie sad
        mike.say "But, Cherie..."
        mike.say "I wasn't asking that..."
        mike.say "I just wanted to know your..."
        "Cherie raises her hand and waves it in the air in front of me."
        "Which I take to mean that she's shutting down the conversation and that I'm not going to get the answer I wanted."
    return

label cherie_offer_a_drink_male:
    mike.say "Hey, Cherie..."
    mike.say "I'm going to grab another drink."
    mike.say "You want me to get one for you too?"
    if cherie.is_visibly_pregnant:
        $ cherie.love -= 10
        if cherie.sub >= 66:
            "Cherie puts her hands on her belly, looking sad all of a sudden."
            show cherie whining
            cherie.say "I don't want to sound ungrateful, [hero.name]..."
            cherie.say "But aren't you forgetting something?"
            show cherie sadsmile
        else:
            show cherie stuned
            "Cherie looks at me with a scandalised expression."
            "And at the same time she places her hands on her belly in a defensive manner."
            show cherie angry
            cherie.say "[hero.name], you know that I'm pregnant!"
            cherie.say "How could you even suggest such a thing?!?"
            show cherie upset
        mike.say "Oh yeah...my bad!"
        $ hero.cancel_activity()
    else:
        "Cherie holds up her empty glass, shaking it so that the ice inside tinkles around."
        show cherie happy
        if cherie.sub >= 66:
            cherie.say "If you think I could handle another one, [hero.name]?"
            cherie.say "But only if you approve."
        else:
            cherie.say "Oh, how thoughtful of you!"
            cherie.say "I will have the same again, please."
            cherie.say "And don't be too shy with the measures either!"
        show cherie smile
        if cherie.love <= 25:
            $ cherie.love += 1
        elif date_girl == cherie and game.active_date:
            $ game.active_date.score += 5
        call expression cherie.get_chat from _call_expression_224
        $ cherie.set_flag("drinks", 1, "day", mod="+")
    return

label cherie_slap_ass_intro_male:
    "I've never thought of myself as the kind of guy that goes around doing stuff like this."
    "In fact I've always kind of looked down on it as kind of a jerk thing to do."
    "But on the other hand, I'm only human."
    "And Cherie's butt is like nothing I've ever seen before!"
    "So I find my hand sweeping through the air before I even know what's happening."
    play sound spank
    "And when it connects with the divine curve of her buttocks, there's an audible crack."
    "In that moment I feel all of the satisfaction that I was expecting to get from the act."
    "But at the same time the reality of what I just did hits me too."
    "And I can only wait to see what Cherie's reaction will be."
    return

label cherie_slap_ass_happy_male:
    "Cherie looks over her shoulder at me, a genuinely surprised look on her face."
    cherie.say "[hero.name]..."
    cherie.say "Did you..."
    cherie.say "Did you just slap me on the bottom?!?"
    mike.say "Erm..."
    mike.say "Yeah, Cherie - I guess I did."
    "I watch as Cherie's face breaks into a smile."
    if cherie.sub >= 66:
        cherie.say "Oh, that is a relief!"
        cherie.say "I thought for a moment that it might have been someone else."
        cherie.say "And I was worried that you might be jealous!"
    else:
        cherie.say "Oh well, that's alright then."
        cherie.say "It's good to know that my derriere can still catch a man's eye!"
        cherie.say "So, please feel free to give it another slap if you feel inclined."
    return

label cherie_slap_ass_angry_male:
    "Cherie looks over her shoulder at me, a genuinely surprised look on her face."
    cherie.say "[hero.name]..."
    cherie.say "Did you..."
    cherie.say "Did you just slap me on the bottom?!?"
    mike.say "Erm..."
    mike.say "Yeah, Cherie - I guess I did."
    if cherie.sub >= 66:
        "Cherie lowers her head, as if upset and yet afraid to speak up about it."
        cherie.say "Oh..."
        cherie.say "Oh, I see."
        cherie.say "Then I suppose that is fine..."
    else:
        "I watch as Cherie's face darkens with rage."
        cherie.say "What is wrong with you?"
        cherie.say "Do you have no respect for women whatsoever?"
        cherie.say "You will never do that to me again - do you understand?!?"
    return

label cherie_breakup_male:
    if randint(0, 1) == 0:
        "I've been dreading this moment ever since the need for it became apparent."
        "But there's no way I can get out of it, because things have simply got to change."
        "So taking a deep breath, I just come out with it, consequences be damned."
        mike.say "Cherie, there's no easy way to say this..."
        mike.say "But I think we need to end things between us."
        show cherie stuned
        "Cherie stares at me blankly at first, as if she doesn't understand what I'm saying."
        show cherie sad
        "But then realisation seems to dawn on her, and she begins to shake her head."
        show cherie whining
        cherie.say "No, no, no..."
        cherie.say "I cannot have heard you correctly, {i}mon ami{/i}..."
        cherie.say "You cannot be saying that you want to deposit me?!?"
        show cherie sad
        mike.say "Erm..."
        mike.say "The term is actually to 'dump' you, Cherie..."
        mike.say "And that's exactly what I mean."
        show cherie whining
        cherie.say "But what have I done to deserve this?"
        cherie.say "I thought that we were getting on like a...a house on fire?"
        show cherie sad
        "I shake my head, doing the best I can to explain myself to Cherie."
        mike.say "I'm sorry, Cherie, but this just isn't working out."
        mike.say "And so I want to end it now, before one of us gets hurt."
    else:
        "You know those times when you hate yourself for having to do something?"
        "But at the same time you also know that there's no way you can avoid it?"
        "I suppose that we've all been there at one time or another."
        "And the only thing that you can do is just grit your teeth and get on with it..."
        mike.say "Ah, Cherie..."
        mike.say "There's something I need to tell you..."
        show cherie stuned
        "Cherie turns to face me with a look of surprise on her face."
        show cherie sad
        "But it soon turns to one of worry when she sees my own expression."
        show cherie whining
        cherie.say "Oh dear..."
        cherie.say "I'm not going to like this."
        cherie.say "Am I, [hero.name]?"
        show cherie sad
        "I try to respond to that question with a reassuring smile."
        "But all I can manage is a half-hearted kind of grimace."
        mike.say "No, Cherie, I guess not."
        mike.say "I just don't think we have a future together."
        mike.say "I'm sorry, but I think we should end it."
        show cherie a closed
        "Cherie takes in a deep breath, filling her lungs."
        show cherie a talkative
        "And then she lets it out slowly."
        show cherie a normal
        "I watch as a strange transformation takes place."
        "Right before my eyes, Cherie's whole demeanour changes."
        "Just now she looked like my confession was causing her emotional pain."
        "But she seems to draw herself together and all of that vanishes from her face."
        "And in it's place I can see all of the poise and strength of a mature woman."
        "For all I know this could be just for show."
        "But it's more than enough to affect me."
        "And I feel like Cherie just turned the tables on this whole thing."
        show cherie a talkative
        cherie.say "Well, if that's really the way you feel, [hero.name]."
        cherie.say "Then I can't say I want to keep it going either."
        cherie.say "I don't have time for a man that isn't devoted to me!"
        cherie.say "For a while there I thought you might be that man."
        cherie.say "But you're actually still a little boy!"
        show cherie a normal
        "Cherie tosses her head as she delivers this last insult."
        "And I can feel it hit me like a genuine slap to the face!"
        "I open my mouth to say something in return."
        "But Cherie holds up a hand to silence me."
        show cherie a talkative
        cherie.say "If we're over, then so is this conversation, [hero.name]."
        cherie.say "And I'd really rather not see you again!"
        show cherie a normal
    return

label cherie_go_steady_intro_male:
    "Cherie and I have been spending so much time together recently it's unreal."
    "Every spare second that I get, I seem to be with her and having a great time."
    "In fact it's becoming so natural for us to be together that I think we're ready."
    "I think that we're ready to admit that we need to take things to the next level."
    "But thinking it's the easy part - now I have to convince Cherie of it too."
    mike.say "Cherie..."
    mike.say "What do you think about going steady?"
    show cherie happy
    cherie.say "What a strange question - I think otherwise we would fall over and get hurt!"
    show cherie normal
    mike.say "Ah, no..."
    mike.say "I mean that I'd like us to start dating more seriously, yeah?"
    return

label cherie_go_steady_yes_male:
    show cherie surprised
    "Cherie gapes in surprise as she realises what I mean."
    show cherie happy
    if cherie.sub >= 66:
        cherie.say "Oh, now I understand!"
        cherie.say "And if that is what you want, [hero.name]..."
        cherie.say "Then that is what shall happen."
    else:
        cherie.say "Oh, I see!"
        cherie.say "That would be a very good idea, I think."
        cherie.say "Something that I very much approve of."
    show cherie smile
    "I'm nodding as Cherie voices her approval of the idea."
    "And why in the hell wouldn't I be?"
    "I got the exact answer that I wanted!"
    return

label cherie_go_steady_no_male:
    show cherie surprised
    "Cherie gapes in surprise as she realises what I mean."
    cherie.say "Oh, I see!"
    show cherie whining
    if cherie.sub >= 66:
        cherie.say "It breaks my heart to say this, but I cannot!"
    else:
        cherie.say "I don't think that would be a very good idea, [hero.name]."
    show cherie sad
    mike.say "But why not, Cherie?"
    mike.say "Don't you want to be with me?"
    show cherie talkative
    cherie.say "Of course I do, {i}mon ami{/i}!"
    if cherie.sub >= 66:
        cherie.say "But I am not ready for such a commitment."
        cherie.say "I fear I am...how do you say - 'damaged goods'?"
    else:
        cherie.say "But I cannot make such a commitment."
        cherie.say "Not so soon after breaking up with Dwayne."
    show cherie sadsmile
    "I want to argue the toss with Cherie, but I don't see how I can."
    "So all I can do is nod and hope that she changes her mind sometime soon."
    return

label cherie_pet_intro_male:
    "I've never thought of myself as the kind of guy that goes around doing stuff like this."
    "In fact I've always kind of looked down on it as kind of a jerk thing to do."
    "But on the other hand, I'm only human."
    "And Cherie's kind of making me think crazy thoughts too."
    "So I find my hand hovering in the air before I even know what's happening."
    "And then I bring it down gently, patting her on the top of the head."
    "In that moment I feel all of the satisfaction that I was expecting to get from the act."
    "But at the same time the reality of what I just did hits me too."
    "And I can only wait to see what Cherie's reaction will be."
    return

label cherie_pet_happy_male:
    show cherie stuned
    "Cherie looks over her shoulder at me, a genuinely surprised look on her face."
    show cherie surprised blush
    cherie.say "[hero.name]..."
    cherie.say "Did you..."
    cherie.say "Did you just pat me on the head?!?"
    show cherie stuned
    mike.say "Erm..."
    mike.say "Yeah, Cherie - I guess I did."
    show cherie smile
    "I watch as Cherie's face breaks into a smile."
    show cherie happy
    if cherie.sub >= 66:
        cherie.say "Oh, that is a relief!"
        cherie.say "I thought for a moment that it might have been someone else."
        cherie.say "And I was worried that you might be jealous!"
    else:
        cherie.say "Oh well, that's alright then."
        cherie.say "So long as it was you doing so, [hero.name]."
        cherie.say "I'm more than happy to let you pet me any time!"
    show cherie normal -blush
    return

label cherie_pet_annoyed_male:
    show cherie stuned
    "Cherie looks over her shoulder at me, a genuinely surprised look on her face."
    show cherie surprised
    cherie.say "[hero.name]..."
    cherie.say "Did you..."
    cherie.say "Did you just pat me on the head?!?"
    show cherie stuned
    mike.say "Erm..."
    mike.say "Yeah, Cherie - I guess I did."
    if cherie.sub >= 66:
        show cherie annoyed
        "Cherie lowers her head, as if upset and yet afraid to speak up about it."
        show cherie talkative
        cherie.say "Oh..."
        cherie.say "Oh, I see."
        cherie.say "Then I suppose that is fine..."
    else:
        show cherie upset
        "I watch as Cherie's face darkens with rage."
        show cherie angry
        cherie.say "What is wrong with you?"
        cherie.say "I am not your pet to pat and paw at as you choose!"
        cherie.say "You will never do that to me again - do you understand?!?"
    show cherie annoyed
    return

label cherie_massage_intro_male:
    show cherie closed
    "I can see Cherie wincing and holding her back, like he muscles are causing her pain."
    "And a moment later she speaks up, confirming my suspicions."
    show cherie whining
    cherie.say "Ooh..."
    cherie.say "I think I have pulled a muscle!"
    show cherie sadsmile
    mike.say "You want me to take a look at that, Cherie?"
    mike.say "Maybe give you a quick massage?"
    mike.say "I've been told that I have magic hands!"
    "I make a point of flexing my fingers as I say all of this."
    "Smiling to make sure that Cherie gets my meaning too."
    return

label cherie_massage_accept_male:
    show cherie normal
    "Cherie seems to instantly tune into what I'm suggesting."
    show cherie smile
    "She nods and does the best that she can to put on a smile too."
    show cherie happy
    cherie.say "Oh, [hero.name]..."
    if cherie.sub >= 66:
        cherie.say "You would do that for me?!?"
        cherie.say "How could I ever refuse such an offer?"
    else:
        cherie.say "That is so kind of you!"
        cherie.say "Here, let me show you just where it hurts..."
    show cherie normal
    "Cherie takes hold of my hands and gently guides me to the spot."
    "And I note that as she does so, she's sure to press them home."
    "Letting me know that she really wants me to work hard on the muscles in question."
    return

label cherie_massage_refuse_male:
    show cherie sad
    "Cherie shakes her head, still wincing from the pain she's experiencing."
    "Hell, she even takes a couple of steps backwards while waving me away with one hand."
    show cherie talkative
    cherie.say "Thank you for the offer, [hero.name]..."
    if cherie.sub >= 66:
        cherie.say "But you are not a medical professional."
        cherie.say "And if something were to go wrong, I would never forgive myself."
    else:
        cherie.say "But I have been under a very expensive doctor for the complaint."
        cherie.say "And I worry that you could undo his good work if I let you massage me there."
    show cherie sadsmile
    "I can't help feeling disappointed at Cherie turning me down like that."
    "But it's not like she hasn't got a pretty good excuse there."
    "And I'm not about to try and force her to change her mind either."
    return

label cherie_piercing_nipples_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie lift her top."
    "Which reveals her breasts, and their newly-pierced nipples."
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you like them."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_piercing_navel_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie lift her top."
    "Which reveals her belly, and its newly-pierced navel."
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you it them."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_piercing_clit_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie pulls down her waistband."
    "Which reveals the contents of her panties, including her newly-pierced clit!"
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you like it."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_piercing_head_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie opening her mouth."
    "Which reveals her newly-pierced tongue."
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you like it."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_piercing_ears_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie lift her head."
    "Which reveals her newly-pierced ears."
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you like it."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_piercing_nose_reaction_male:
    cherie.say "[hero.name], look at this..."
    "I turn just in time to see Cherie lift her head."
    "Which reveals her newly-pierced nose."
    cherie.say "What do you think?"
    mike.say "Oh man!"
    mike.say "That's amazing!"
    cherie.say "I am so glad you like it."
    if cherie.sub >= 66:
        cherie.say "That makes it all worthwhile."
    else:
        cherie.say "This feels like something I should have done years ago."
    return

label cherie_movie_disliked_reaction_male:
    cherie.say "I really didn't care for that movie, not my kind of thing at all."
    return

label cherie_movie_indifferent_reaction_male:
    cherie.say "It was okay, I suppose...I really wasn't paying attention in there."
    return

label cherie_movie_liked_reaction_male:
    cherie.say "Oh my goodness...that was SO moving, I felt like I was living the movie with the characters!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
