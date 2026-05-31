label aletta_ice_cream_reaction_male:
    mike.say "Hey, Aletta - let's get some ice cream!"
    aletta.say "Hmm...that sounds like a good idea."
    aletta.say "I could really do with cooling down!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "But Aletta orders herself a pretty fancy sundae that comes with a long spoon."
    mike.say "Wow, Aletta - that thing looks amazing!"
    aletta.say "Mmm...it tastes pretty amazing too!"
    "I watch, my mouth hanging open as Aletta spoons ice cream into her mouth."
    "And I don't know which makes me feel more hungry."
    "The ice cream itself, or the way Aletta's eating it!"
    return

label aletta_ask_phone_male:
    mike.say "I was just wondering, Aletta..."
    mike.say "Could I maybe get your number?"
    if hero.charm >= 20 - aletta.love:
        show aletta happy
        $ hero.smartphone_contacts.append("aletta")
        aletta.say "Hmm..."
        aletta.say "I think so, [hero.name]."
        aletta.say "We do have a lot to talk about..."
    else:
        show aletta annoyed
        $ aletta.sub -= 1
        $ aletta.love -= 1
        aletta.say "You don't need to ask for it, [hero.name]."
        aletta.say "You can find my office number in the company directory."
    return

label aletta_ask_birthday_male:
    mike.say "Hey, Aletta..."
    mike.say "When is your actual birthday?"
    if hero.charm >= 40 - aletta.love:
        show aletta happy
        $ aletta.flags.birthdayknown = True
        aletta.say "Really, [hero.name]?"
        aletta.say "You could have looked it up in my personnel file."
        aletta.say "Anyway - it's Winter 14."
    else:
        show aletta annoyed
        $ aletta.sub -= 1
        $ aletta.love -= 1
        aletta.say "Really, [hero.name]!"
        aletta.say "If I wanted you to know that, I would have told you!"
        aletta.say "And don't go looking in my personnel file either!"
    return

label aletta_offer_a_drink_male:
    mike.say "Hey, Aletta..."
    mike.say "Let me buy you a drink!"
    "Almost the second the words are out of my mouth, Aletta turns to face me."
    if aletta.is_visibly_pregnant:
        show aletta angry
        $ aletta.love -= 10
        aletta.say "I'm going to pretend you didn't say that, [hero.name]."
        aletta.say "For your sake and the sake of our unborn child."
        aletta.say "But I won't forget a second time!"
        $ hero.cancel_activity()
        hide aletta
    elif (hero.charm >= 60 - aletta.love and aletta.flags.drinks < 2) or date_girl == aletta:
        show aletta happy
        aletta.say "Why thank you, [hero.name]."
        aletta.say "A glass of red wine, please."
        hide aletta
        show drink aletta
        if aletta.love <= 25:
            $ aletta.love += 1
        elif date_girl == aletta and game.active_date:
            $ game.active_date.score += 5
        call expression aletta.get_chat from _call_expression_205
        hide drink aletta
        $ aletta.set_flag("drinks", 1, "day", mod="+")
    else:
        show aletta annoyed
        aletta.say "Hmm..."
        aletta.say "I don't need to be taken by the hand."
        aletta.say "And I can afford to pay for my own drinks as well!"
        $ hero.cancel_activity()
        hide aletta
    return

label aletta_slap_ass_intro_male:
    "I might be playing with fire here."
    "But Aletta's ass is just hypnotic today!"
    "And I can't keep my hands under control."
    "Before I know it, the sound of a slap reaches my ears."
    "But it's closely followed by the sound of Aletta's reaction..."
    return

label aletta_slap_ass_happy_male:
    aletta.say "Oh..."
    aletta.say "Oh my..."
    "Aletta looks at me in utter shock."
    "And I expect her to slap me any second now."
    "But instead, I see her cheeks flush with colour."
    "And she chuckles with embarrassment."
    aletta.say "Oh, [hero.name]!"
    aletta.say "You naughty boy!"
    return

label aletta_slap_ass_angry_male:
    aletta.say "Oh my god..."
    aletta.say "Did you actually just..."
    "Aletta looks at me in utter shock."
    "And I expect her to slap me any second now."
    "But instead, I see her cheeks flush with colour."
    "And her eyes flare with anger."
    aletta.say "I cannot believe you actually just did that!"
    "She shakes her head and walks off in an angry huff."
    return

label aletta_breakup_male:
    show aletta
    "There's no easy way to say this."
    "But Aletta's a no-nonsense type of girl."
    "So I figure that the best way is to just say it."
    mike.say "Aletta..."
    mike.say "I've been thinking recently."
    "Aletta raises an eyebrow at this and regards me with interest."
    aletta.say "Well, that's an ominous statement if I ever heard one!"
    aletta.say "So tell me, [hero.name] - what have you been thinking about?"
    "I take a deep breath, hold it for a moment and then let it out."
    "Here goes nothing..."
    mike.say "About us, Aletta."
    mike.say "I don't think it's working."
    mike.say "I mean, I don't think we're working."
    "For the first time I can recall, Aletta's lost for words."
    show aletta surprised
    "She just stares at me, a look of utter shock on her face."
    "And I find myself stammering to fill the void as a result."
    mike.say "I mean...we can still be friends."
    mike.say "That is if you want to..."
    mike.say "It might be awkward at work, but..."
    "Aletta holds up a hand to silence me."
    show aletta annoyed
    "She shakes her head as she finally begins to speak again."
    aletta.say "Let me get this straight, [hero.name]."
    aletta.say "YOU are dumping ME?"
    mike.say "Erm..."
    mike.say "Yeah, Aletta - I guess so!"
    show aletta angry
    aletta.say "How could you do this to me, [hero.name]?"
    aletta.say "Oh god - how am I ever going to live this down?!?"
    "All I can do is shrug and offer a weak smile at this."
    "I had thought that Aletta might be upset to lose what we had."
    "But it sounds like she's more worried about losing face at work!"
    mike.say "Like I said, Aletta..."
    mike.say "We can still be friends, right?"
    "Suddenly Aletta shoots a look in my direction."
    "One that hits me like a physical slap to the face."
    aletta.say "I don't need friends, [hero.name]."
    aletta.say "And if you don't need me..."
    aletta.say "Then I certainly don't need you!"
    aletta.say "You just made an enemy at work too - so watch your back!"
    return

label aletta_go_steady_intro_male:
    mike.say "We've been seeing each other for a while now, Aletta."
    mike.say "And I think it's about time that we officially went steady."
    mike.say "What do you think?"
    return

label aletta_go_steady_yes_male:
    aletta.say "Hmm..."
    aletta.say "I like the sound of that, [hero.name]."
    aletta.say "If feels...official!"
    return

label aletta_go_steady_no_male:
    if game.week_day % 2 == 0:
        aletta.say "Hmm..."
        aletta.say "I don't think so, [hero.name]."
        aletta.say "This isn't the time to make things official."
    else:
        mike.say "I would like us to be an official couple, you know 'go steady' as they say."
        if hero.flags.isceo:
            aletta.say "That would not be appropriate. You're my boss!"
        else:
            aletta.say "That would not be appropriate. I'm your boss!"
    return

label aletta_pet_intro_male:
    "I don't even stop to think about what I'm doing."
    "And I certainly don't have a thought for the consequences either!"
    "I just do it - I pat Aletta on the head..."
    return

label aletta_pet_happy_male:
    aletta.say "Oh..."
    aletta.say "I..."
    aletta.say "That's so weird, [hero.name]!"
    aletta.say "But I think I like it..."
    return

label aletta_pet_annoyed_male:
    aletta.say "What on earth do you think you're doing, [hero.name]?!?"
    aletta.say "Don't you EVER do that to me again!"
    aletta.say "And I mean it!"
    return

label aletta_massage_intro_male:
    mike.say "You work too hard Aletta!"
    mike.say "You should really learn to take it easy sometimes."
    mike.say "How about I give you a massage, help you to loosen up?"
    return

label aletta_massage_accept_male:
    aletta.say "Hmm..."
    aletta.say "My muscles are feeling pretty knotted up."
    aletta.say "And that makes it hard to concentrate on my work..."
    aletta.say "Okay, [hero.name], I'll take you up on the offer."
    return

label aletta_massage_refuse_male:
    aletta.say "Urgh..."
    aletta.say "You're making it worse, [hero.name]!"
    aletta.say "I can practically feel my muscles getting tighter with every word you say!"
    aletta.say "Just leave me alone, okay?"
    return

label aletta_piercing_nipples_reaction_male:
    aletta.say "Hmm..."
    aletta.say "You know, I never thought about getting my nipples pierced before."
    aletta.say "But I don't know why I didn't do it sooner."
    aletta.say "It feels really great!"
    return

label aletta_piercing_navel_reaction_male:
    aletta.say "You know what, [hero.name]..."
    aletta.say "I think my belly-button looks really cute pierced."
    aletta.say "Thank you for putting the idea into my head."
    return

label aletta_piercing_clit_reaction_male:
    aletta.say "Oh...oh my..."
    aletta.say "It feels so...so weird!"
    aletta.say "But I really like it, [hero.name]!"
    return

label aletta_piercing_head_reaction_male:
    aletta.say "Hmm..."
    aletta.say "I still like the fact that I got this piercing, [hero.name]."
    aletta.say "But tell me the truth, okay?"
    aletta.say "You didn't want me to get it in the hope of shutting me up, did you?"
    return

label aletta_piercing_nose_reaction_male:
    aletta.say "How did I ever let you talk me into getting this thing?"
    aletta.say "Oh god, everybody's going to be staring at me in the office!"
    aletta.say "But...I...I do kind of like it!"
    return

label aletta_movie_disliked_reaction_male:
    aletta.say "Urgh...I don't know why I let you convince me to see that film - it was just dreadful!"
    return

label aletta_movie_indifferent_reaction_male:
    aletta.say "Well, that was a painfully average experience!"
    return

label aletta_movie_liked_reaction_male:
    aletta.say "I can't stop thinking about that movie, [hero.name] - I have to see it again!"
    return

label aletta_call_in:
    $ res = randint(0, 2)
    if res == 1:
        scene expression f"bg {game.room}"
        mike.say "Aletta can you come to my office?"
        show aletta
        if not aletta.is_sex_slave:
            aletta.say "Yes [hero.name]?"
        else:
            aletta.say "Yes Master?"
    else:
        scene expression f"bg {game.room}"
        "I feel nervous picking up the phone and making a call like this one."
        "Hell, who am I trying to kid?"
        "I feel nervous calling Aletta for the most innocent of reasons."
        "So how was I going to feel anything but awkward asking her for a favour."
        "Especially that certain kind of favour I want to keep between the two of us!"
        play sound "<from 0 to 2>sd/SFX/phone/phone_calling.ogg"
        "As usual, Aletta picks up the phone in record time."
        aletta.say "Yes..."
        aletta.say "What do you want?"
        mike.say "Ah..."
        mike.say "Hey, Aletta..."
        if aletta.is_sex_slave:
            aletta.say "Oh, it's you, Master."
        else:
            aletta.say "Oh, it's you, [hero.name]."
        aletta.say "What can I do for you?"
        "I think I can detect a slight softening in Aletta's voice as she realises it's me."
        "Not like she changes her attitude completely and becomes all sweetness and light."
        "More as if she remains professional, but doesn't sound quite as angry."
        mike.say "I...I was wondering if you could come over to my office."
        mike.say "There's something that I need to talk over with you."
        mike.say "And it's kind of sensitive - if you know what I mean?"
        aletta.say "Hmm..."
        aletta.say "I suppose I could spare a few minutes."
        if aletta.is_sex_slave:
            aletta.say "Okay, Master - I'll be there ASAP."
        else:
            aletta.say "Okay, [hero.name] - I'll be there ASAP."
    return

label aletta_belly_kiss_male:
    show aletta at center, zoomAt(1.25, (640, 880))
    show aletta at center, traveling(1.75, 1.0, (640, 880))
    "I bend over, pursing my lips as I bring them closer to the curve of Aletta's belly."
    "It just looks so big, round and beautiful that I can't resist the urge to kiss it!"
    show aletta stuned at center, traveling(1.25, 0.2, (640, 880))
    "But just before I can lay a big one on it, my target is pulled backwards and out of reach."
    mike.say "Hey..."
    mike.say "What's going on?"
    "I look up to see that Aletta's looking down at me."
    "And I note that she's also cradling her belly in a protective manner."
    show aletta angry
    aletta.say "I should ask you the same thing!"
    aletta.say "It's bad enough that I have to be swollen up like a balloon."
    aletta.say "But do I also have to cope with my stomach making you behave like a lunatic?"
    show aletta upset
    mike.say "Aw..."
    mike.say "Come on, Aletta!"
    mike.say "All I want to do is kiss it."
    show aletta annoyed
    "Aletta narrows her eyes at this."
    show aletta embarrassed
    aletta.say "You know, there was a time when you'd beg me to kiss my lips."
    aletta.say "Then you went and got me pregnant - and fat!"
    aletta.say "And now you're obsessed with my belly."
    show aletta sadsmile
    "All I can do is shrug."
    mike.say "I still want to kiss you on the lips, Aletta."
    mike.say "And if I'm honest, lot's of other places too..."
    mike.say "So just let me kiss your belly once?"
    mike.say "Please?"
    show aletta normal
    "Aletta lets out a sigh."
    "But then she shakes her head."
    show aletta talkative
    aletta.say "If it'll get you over the obsession..."
    aletta.say "Then one kiss - but just one!"
    show aletta normal at center, traveling(2.0, 0.5, (640, 980))
    "I take the chance to lean in and place a kiss on Aletta's belly."
    "And even though she looks away while I do it, I swear she's actually enjoying it."
    "Because I catch her sneaking a look at what I'm doing."
    show aletta happy
    "And when I do, I can see that she's smiling."
    return

label aletta_belly_caress_male:
    show aletta at center, zoomAt(1.25, (640, 880))
    "I have to admit that I'm more than a little nervous about Aletta's big, pregnant belly."
    "The truth is that I find it fascinating for reasons that I just can't begin to explain."
    "And I also feel guilty to admit this..."
    "But it does kind of make Aletta look even hotter than normal too!"
    "I'm just worried that she won't want me to draw attention to it."
    "You know, as she's so serious and focussed on the important things in life?"
    show aletta talkative
    aletta.say "[hero.name]…"
    aletta.say "Are you staring at my stomach right now?"
    aletta.say "Looking at it like you want to touch it?"
    show aletta sadsmile
    "Oh no, busted!"
    "Aletta must have caught me in the act."
    "Well, there's no point in denying it now."
    mike.say "Ah, yeah..."
    mike.say "I kind was..."
    mike.say "And I kind of do!"
    show aletta annoyed
    "For a moment I think that Aletta's going to tell me off."
    "But then I see her look around, like she's checking we're alone."
    show aletta happy
    aletta.say "Alright, fine..."
    aletta.say "You can touch it now."
    show aletta normal
    "Just in case I mistook what she just said, Aletta makes her intentions clear."
    show aletta at center, traveling(1.75, 1.0, (640, 880))
    "And she does so by thrusting her belly in my direction."
    "Which means that it's almost forced into my hands!"
    "I'm still looking at her in shock when I suddenly feel something move."
    "And as soon as that happens, nothing else seems to matter in the entire world."
    "I look down at the signs of life in there, and then back up at Aletta."
    "And I don't know if it's the look on my face or the moment we just shared..."
    show aletta happy
    "But Aletta's features melt into a helpless smile of total happiness."
    "There's no need for either of us to speak, no need for words."
    "Right now we're communicating on what feels like a higher level."
    return

label aletta_belly_listen_male:
    show aletta talkative at center, zoomAt(1.25, (640, 880))
    aletta.say "[hero.name]..."
    aletta.say "I want you to do something for me."
    show aletta normal
    "The question comes out of nowhere, taking me by surprise."
    "And when turn to look at Aletta, I can see that it must be important."
    "Because she has a serious look on her face."
    "The kind of look that you don't mess with."
    mike.say "Sure, Aletta..."
    mike.say "What do you need me to do?"
    "Aletta holds my eye, but then she begins to look down."
    "Compelled to follow, I do so until her gaze comes to rest on her belly."
    show aletta talkative
    aletta.say "I can feel the baby when it moves, obviously."
    aletta.say "But the thing is that I can't hear it."
    show aletta embarrassed
    aletta.say "So I was wondering if..."
    show aletta sadsmile
    mike.say "You want me to listen to your belly?"
    show aletta embarrassed
    aletta.say "Would you?"
    aletta.say "Just for a few moments?"
    show aletta sadsmile
    "By now Aletta's starting to look a little embarrassed."
    "But I know how hard she can find things like this."
    "So I want to do all I can to alleviate that awkwardness."
    mike.say "Of course, Aletta..."
    mike.say "I'd love to!"
    show aletta normal at center, traveling(2.0, 0.5, (640, 980))
    "Before Aletta can even make a move, I'm down on my knees."
    "And then I'm pressing my ear against the curve of her belly."
    "I only have to wait a few moments before the baby moves."
    "And when it does, I feel the sensation against the side of my head."
    "But I definitely hear something too."
    mike.say "Whoa!"
    show aletta surprised
    aletta.say "What is it?"
    aletta.say "What did you hear?"
    show aletta stuned
    mike.say "A deep sound..."
    mike.say "Like someone moving underwater!"
    show aletta happy
    "I look up to see Aletta nodding happily."
    "Which I guess means that was what she wanted to hear."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
