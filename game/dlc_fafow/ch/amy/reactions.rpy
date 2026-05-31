label amy_ice_cream_reaction_male:
    "I can see that Amy's not used to spending time at the beach."
    "She's pretty pale, and it looks like the sun is really bothering her too!"
    mike.say "I feel like I'm melting, Amy!"
    mike.say "Maybe we should go grab an ice-cream?"
    "At the mere mention of the word, Amy comes back to life."
    amy.say "Oh yeah!"
    amy.say "That sounds perfect!"
    "Together we hurry over to the ice-cream stand."
    "And I don't hesitate to order my favourite."
    "Amy orders something that looks almost as good."
    "With ice-cream almost as pale as her own skin."
    "And as she begins to lick it, my mind fills with inappropriate thoughts!"
    "Amy seems to notice that something's up with me."
    amy.say "Are you okay, [hero.name]?"
    "She holds out her ice-cream."
    amy.say "Would a lick of mine help?"
    mike.say "Oh yeah, Amy..."
    mike.say "I'd kill for a lick of yours!"
    return

label amy_ask_phone_male:
    "Well, here goes nothing."
    "After all, the worst she can say is no, right?"
    mike.say "Ah, Amy..."
    mike.say "I was just wondering..."
    mike.say "Could I maybe get your phone number?"
    mike.say "I mean...if not it's okay...I just..."
    if hero.charm >= 20 - amy.love:
        if 'fafow' in DLCS:
            $ hero.smartphone_contacts.append("amy")
        show amy happy
        "Amy smiles and shakes her head as I trip over myself."
        amy.say "Of course you can have my number, [hero.name]!"
        amy.say "I've been meaning to give it to you anyway."
        amy.say "It's just that we always end up talking about so much other stuff."
        amy.say "I seem to remember when it's too late!"
    else:
        $ amy.love -= 1
        $ amy.sub -= 1
        show amy sad
        "Amy frowns and shakes her head as I trip over myself."
        amy.say "Nah, I don't think we're there yet, [hero.name]."
        amy.say "If I want you to have it, then I'll give it to you."
        show amy normal
        amy.say "I'm not trying to be a bitch, that's just how it is."
        amy.say "So don't make it awkward by asking again."
    return

label amy_ask_birthday_male:
    mike.say "I know that Shawn mentioned when your birthday was, Amy."
    mike.say "But he's got such a terrible memory!"
    mike.say "Could you tell me the date yourself?"
    "I smile as I ask the question, trying to look casual."
    mike.say "I mean, just so I know for sure?"
    if hero.charm >= 40 - amy.love:
        $ amy.flags.birthdayknown = True
        show amy happy
        "Amy smiles and nods happily."
        amy.say "No problem, [hero.name]."
        amy.say "It's on the [active_girl.birthday[1]] of [active_girl.birthday[0]]."
        show amy normal
        amy.say "And I wouldn't trust what Shawn says either."
        amy.say "He's always fucking up the dates at work!"
    else:
        $ amy.sub -= 1
        $ amy.love -= 1
        show amy sad
        "Amy narrows her eyes and shakes her head."
        amy.say "Erm...no."
        amy.say "I'm pretty careful about sharing my personal details around."
        show amy upset
        amy.say "And what in the hell is Shawn thinking doing it behind my back?"
        show amy normal
        amy.say "I need to have a talk with him about that..."
    return

label amy_offer_a_drink_male:
    mike.say "Huh...looks like I polished that one off!"
    mike.say "You want me to get you one while I'm at the bar, Amy?"
    if amy.is_visibly_pregnant:
        "Amy glances down at her swollen belly and then back up at me."
        amy.say "Erm..."
        $ amy.love -= 10
        amy.say "What do you think?!?"
        "I nod my head, already feeling my cheeks flushing red."
        $ hero.cancel_activity()
        hide amy
    elif (hero.charm >= 60 - amy.love and amy.flags.drinks < 2) or date_girl == amy:
        amy.say "Sure thing!"
        amy.say "I'll have whatever you're having."
        amy.say "And thanks for thinking of me too!"
        hide amy
        show drink amy
        if amy.love <= 25:
            $ amy.love += 1
        elif date_girl == amy and game.active_date:
            $ game.active_date.score += 5
        call expression amy.get_chat from _call_expression_478
        hide drink amy
        $ amy.set_flag("drinks", 1, "day", mod="+")
    else:
        amy.say "Sorry, I don't feel like drinking."
        $ hero.cancel_activity()
    return

label amy_slap_ass_intro_male:
    "Did I ever mention that Amy's got a really nice ass?"
    "And I'm not just saying that, I really mean it."
    "Her ass is an exceptional work of art in it's own right!"
    "Every time she walks past me, I can feel it working on me."
    "I just want to reach out and touch it!"
    "And I know that sooner or later, I won't be able to resist!"
    "So when it happens, I'm as surprised as anyone..."
    return

label amy_slap_ass_happy_male:
    amy.say "OUCH!"
    amy.say "Hey, who did that?"
    amy.say "Who slapped my ass?!?"
    mike.say "Erm..."
    mike.say "Sorry, Amy..."
    mike.say "It was me!"
    "Somehow, finding out that I was responsible seems to help."
    "Amy's expression softens, and she cracks a smile."
    amy.say "Oh..."
    amy.say "It was you!"
    amy.say "Well...just let me know before you do it next time, okay?"
    "I can see Amy's cheeks flushing as she says all of this."
    "And it's not hard to guess that she kind of liked what I just did."
    "Only she thinks that she needs to make a show of disapproval."
    "Just to keep up appearances."
    return

label amy_slap_ass_angry_male:
    amy.say "OUCH!"
    amy.say "Hey, who did that?"
    amy.say "Who slapped my ass?!?"
    mike.say "Erm..."
    mike.say "Sorry, Amy..."
    mike.say "It was me!"
    "I see anger flare in Amy's eyes as I admit to being guilty."
    "She points a finger in my face and wags it ferociously."
    amy.say "You think that's okay?"
    amy.say "You think that because we're friends you can touch me like that?!?"
    amy.say "You ever do that to me again, and I'll break your damn arm!"
    mike.say "Okay, Amy, okay!"
    mike.say "I promise I won't!"
    return

label amy_breakup_male:
    "Urgh..."
    "There's no easy or pleasant way of doing something like this."
    "So I guess that I just have to go ahead and take the bull by the horns..."
    mike.say "Amy..."
    mike.say "We need to talk..."
    amy.say "That doesn't sound good!"
    amy.say "About what, exactly?"
    mike.say "About us."
    show amy annoyed
    amy.say "Yeah, that definitely not good!"
    "I nod, but then try to get straight down to business."
    mike.say "This thing between us, Amy..."
    mike.say "It started out great."
    mike.say "But I don't think it's going anywhere."
    "I see defiance flare in Amy's eyes for a moment."
    "And I think she's going to argue the opposite."
    "Or at least blame the whole thing on me."
    "But then it vanishes and she seems to sag under the weight of realisation."
    show amy sad
    amy.say "Shit..."
    amy.say "You're right."
    amy.say "I tried to deny it, but you're right."
    show amy normal
    amy.say "We should end this thing while we can still stand the sight of each other!"
    mike.say "I'd like that, Amy..."
    mike.say "I really would!"
    return

label amy_go_steady_intro_male:
    mike.say "Amy..."
    amy.say "Yeah, [hero.name]?"
    mike.say "We get along, right?"
    mike.say "I mean, I like you and you like me?"
    amy.say "That's the way I see it, yeah."
    mike.say "Well..."
    mike.say "I think I like you enough for it to be more than that."
    mike.say "Like...enough for us to make it official, you know?"
    amy.say "You mean...you want to go steady with me?"
    mike.say "Pretty much, yeah!"
    return

label amy_go_steady_yes_male:
    amy.say "Why didn't you just come out and say so?"
    amy.say "Of course I would, [hero.name]!"
    amy.say "I love the time we spend together already."
    amy.say "So that'd just be more of a good thing!"
    mike.say "Wow..."
    mike.say "That's great, Amy!"
    return

label amy_go_steady_no_male:
    amy.say "Don't take this the wrong way, [hero.name]..."
    amy.say "I like you, but not in that kind of way!"
    mike.say "Oh..."
    mike.say "Oh, I see..."
    amy.say "But we can still be friends, yeah?"
    amy.say "Nothing has to change between us!"
    mike.say "I don't know about that, Amy..."
    return

label amy_pet_intro_male:
    "I can't help thinking about how cute Amy is."
    "And the fact that she's shorter than me only makes it worse."
    "I could just reach out and pat her on top of the head."
    "The first thing she'd know about it was the sensation of it happening."
    "Just reach out and..."
    amy.say "Huh..."
    amy.say "What the..."
    amy.say "Hey!"
    amy.say "Did you just pat me on the head?!?"
    mike.say "Erm..."
    mike.say "Yeah, Amy..."
    mike.say "I guess I did!"
    return

label amy_pet_happy_male:
    "For a moment, I think Amy's going to chew me out."
    "But then her expression softens and she shakes her head."
    amy.say "Good job it was you and not somebody else!"
    amy.say "Because I only let people I like do that to me."
    amy.say "Sometimes I let them do other things to me as well..."
    mike.say "R...really?"
    mike.say "How do I get to find out what those things are?"
    return

label amy_pet_annoyed_male:
    "Amy balls her fists and plants them on her thighs."
    "And the look she gives me is enough to make me regret my actions!"
    amy.say "You look here, mister..."
    amy.say "If you want to pat someone on the head..."
    amy.say "Then you go buy yourself a damn dog!"
    mike.say "Okay, Amy, okay!"
    mike.say "I won't do it again."
    mike.say "I swear!"
    return

label amy_massage_intro_male:
    amy.say "Oooh!"
    amy.say "Ouch, ouch, ouch!"
    mike.say "Whoa..."
    mike.say "That looks painful, Amy!"
    amy.say "Yeah, I know!"
    amy.say "Shawn had me stacking shelves and carrying boxes all day yesterday."
    amy.say "I must have pulled something in my back while I was doing it."
    mike.say "You want me to take a look?"
    mike.say "I'm told I give a pretty good massage."
    mike.say "I've even been called 'magic hands'!"
    return

label amy_massage_accept_male:
    "Amy shrugs, but then winces in pain from the movement."
    amy.say "Ah!"
    amy.say "Why the hell not?"
    amy.say "It's not getting any better on its own."
    amy.say "And it's not like you can make it any worse!"
    "Amy laughs, like she's waiting for me to confirm that fact."
    "But as I can't, I choose to change the subject instead."
    mike.say "Just show me where it hurts, Amy."
    mike.say "I think I know a place where you can lie down..."
    return

label amy_massage_refuse_male:
    "Amy shakes her head and instinctively starts to back away."
    amy.say "No!"
    amy.say "I mean...no thanks, [hero.name]."
    amy.say "I appreciate the offer."
    amy.say "But the last time I let a friend do that..."
    amy.say "Well...let's just say I ended up looking like a hunch-back!"
    mike.say "Oh..."
    mike.say "Okay, Amy..."
    mike.say "I suppose that makes sense."
    return

label amy_piercing_nipples_reaction_male:
    amy.say "Hey, [hero.name]..."
    amy.say "Notice anything different?"
    "As she says this, Amy thrusts her chest out towards me."
    "And I can't help noticing that there is something different."
    mike.say "Whoa..."
    mike.say "Amy, you got your..."
    amy.say "Nipples pierced!"
    amy.say "Doesn't it look good?"
    mike.say "It sure does!"
    return

label amy_piercing_navel_reaction_male:
    amy.say "Hey, [hero.name]..."
    amy.say "Notice anything different?"
    "As she says this, Amy thrusts her belly out towards me."
    "At the same time she lifts up her top."
    "And I can't help noticing that there is something different."
    mike.say "Whoa..."
    mike.say "Amy, you got your..."
    amy.say "Navel pierced!"
    amy.say "Doesn't it look good?"
    mike.say "It sure does!"
    return

label amy_piercing_clit_reaction_male:
    amy.say "Hey, [hero.name]..."
    amy.say "Notice anything different?"
    "As she says this, Amy thrusts her groin out towards me."
    "I can't see what she's talking about."
    "But I can make a pretty good guess."
    mike.say "Whoa..."
    mike.say "Amy, you got your..."
    amy.say "Clit pierced!"
    amy.say "And it feels REALLY good!"
    mike.say "I bet it does!"
    return

label amy_piercing_head_reaction_male:
    amy.say "Hey, [hero.name]..."
    amy.say "Notice anything different?"
    "As she says this, Amy sticks her tongue out at me."
    "And I can't help noticing that there is something different."
    mike.say "Whoa..."
    mike.say "Amy, you got your..."
    amy.say "Tongue pierced!"
    amy.say "Doesn't it look good?"
    mike.say "It sure does!"
    return

label amy_piercing_nose_reaction_male:
    amy.say "Hey, [hero.name]..."
    amy.say "Notice anything different?"
    "As she says this, Amy thrusts her nose towards me."
    "And I can't help noticing that there is something different."
    mike.say "Whoa..."
    mike.say "Amy, you got your..."
    amy.say "Nose pierced!"
    amy.say "Doesn't it look good?"
    mike.say "It sure does!"
    return

label amy_belly_kiss_male:
    show amy normal at center, zoomAt(1.25, (640, 880))
    mike.say "Amy..."
    mike.say "Would you come over here?"
    show amy puzzled
    "Amy looks up from what she's doing."
    "And I see she interest written all over her face."
    show amy happy
    amy.say "Oh..."
    amy.say "Okay, [hero.name]..."
    amy.say "But what do you want?"
    show amy normal at center, traveling(1.5, 0.3, (640, 1040))
    "As Amy hurries over, I can't help beginning to smile."
    "She just looks so beautiful and full of life."
    "Even more so now that she's pregnant and showing the fact."
    mike.say "Oh..."
    mike.say "I just have the overwhelming urge to kiss you, that's all!"
    show amy happy
    "I can see the delight on Amy's face as she hears this."
    "And by the time she reaches me, she's almost running."
    amy.say "Here I am, [hero.name]..."
    amy.say "Always ready for a kiss from you!"
    show amy normal
    "I nod, making a show of puckering my lips in front of Amy."
    show amy at center, traveling(1.5, 0.3, (640, 940))
    "But then I begin to kneel down before her."
    show amy stuned
    "And this seems to cause her instant confusion."
    show amy surprised
    amy.say "[hero.name]..."
    amy.say "What are you doing?"
    amy.say "My lips are up here!"
    show amy stuned
    mike.say "It's not your lips I want to kiss!"
    show amy at center, traveling(2.0, 1.0, (640, 980))
    "To illustrate my point, I place my lips on the curve of Amy's belly."
    "And then I proceed to lay gentle kisses on the whole thing."
    "I don't stop until I've kissed as much of it as I can reach."
    show amy happy
    "All the time listening to Amy sighing and giggling as I do so."
    show amy normal at center, traveling(1.5, 0.3, (640, 1040))
    "And when I stand up, I can see that she's amused by my antics."
    show amy happy
    amy.say "Oh, [hero.name]..."
    amy.say "You're such a lame ass!"
    amy.say "But I guess that's one of the reasons I love you..."
    hide amy
    show amy kiss
    with fade
    "Amy underlines this by leaning in and planting her lips on mine."
    "And the kiss that follows lets me know just how serious she is."
    return

label amy_belly_caress_male:
    show amy angry at center, zoomAt(1.25, (640, 880))
    amy.say "Urgh..."
    amy.say "I should have thought of this before I let you get me in this state!"
    show amy upset
    "I turn around to see Amy standing there, both hands on her swelling belly."
    "And for a moment I think that she's regretting the decision to start a family."
    mike.say "Hey..."
    mike.say "Don't say that, Amy!"
    mike.say "I still think you look beautiful, you know?"
    mike.say "Like totally hot!"
    show amy stuned
    "Amy looks at me with confusion and even a little annoyance on her face."
    "And she shakes her head, letting me know that I've gone and missed the point."
    show amy annoyed
    amy.say "What are you talking about, [hero.name]?"
    amy.say "I'm not saying that I don't want to be pregnant."
    amy.say "And I'm not even moaning about it turning me into a two-legged whale!"
    show amy sad
    "Amy makes a gesture to the clothes that she's wearing."
    "And suddenly I can see exactly what's bugging her."
    "The short skirts and cropped tops she wears don't exactly fit well for a pregnant woman."
    "Her belly is literally sticking out in front of her, like it's burst her shirt."
    "And I can almost feel how much her swollen breasts are ready to burst out of the top too!"
    mike.say "Oh yeah..."
    mike.say "I see what you mean!"
    show amy whining
    amy.say "I feel like I'm gonna have to buy a whole new wardrobe."
    amy.say "Otherwise I'll just end up popping out of everything I own!"
    show amy sad
    mike.say "Wow..."
    mike.say "Now that is a hot image!"
    show amy annoyed
    "Amy frowns at this and shakes her head."
    show amy whining
    amy.say "You really think that's helping matters?"
    show amy sad
    mike.say "Erm..."
    mike.say "No, Amy..."
    mike.say "Of course not!"
    show amy normal at center, traveling(1.5, 0.3, (640, 1040))
    "Desperately trying to think of something I can do, I reach out and touch Amy's belly."
    "Putting both hands on it, I manage to cover a surprisingly large portion of the curve."
    "I'm kind of expecting her to shoot me another withering glance."
    "But to my surprise, Amy's mood seems to soften, and she smiles happily."
    show amy happy
    amy.say "Mmm..."
    amy.say "That feels pretty good."
    amy.say "I like it when you touch my belly, [hero.name]..."
    amy.say "It makes me feel safe."
    show amy normal
    mike.say "I can't keep it there forever, Amy."
    mike.say "But maybe it can stay until you update your wardrobe?"
    return

label amy_belly_listen_male:
    show amy normal at center, zoomAt(1.25, (640, 880))
    mike.say "Huh..."
    mike.say "What was that?"
    show amy stuned
    "Amy looks up at the sound of my voice."
    "And I can see she has a puzzled expression on her face."
    show amy happy
    amy.say "I didn't hear anything, [hero.name]..."
    amy.say "Maybe it's just your imagination?"
    show amy normal
    "I think about it for a second, then shake my head."
    mike.say "No..."
    mike.say "I definitely heard something..."
    mike.say "And it was coming from right here!"
    show amy stuned
    "Amy looks down in amazement as I point at the curve of her belly."
    show amy at center, traveling(2.0, 1.0, (640, 980))
    "But I'm already leaning in closer, putting my ear to her navel."
    show amy surprised
    amy.say "What are you doing?"
    amy.say "There's no way you can hear anything in there!"
    show amy stuned
    mike.say "That's crazy, Amy!"
    mike.say "You know that the scan they gave you at the hospital is ultrasound, yeah?"
    mike.say "That's basically a fancy, scientific name for noise."
    mike.say "And if that works, then this should too."
    show amy annoyed
    amy.say "Yeah..."
    amy.say "I don't think that's how it works."
    show amy puzzled
    "I wave a hand for Amy to be quiet."
    "Because I want all my attention focussed on her belly."
    "Or to be more specific, what's inside of it."
    "And pretty soon I can hear something moving in there."
    "It's not clear or easy to make sense of, but it's definitely there."
    mike.say "I can hear them, Amy..."
    mike.say "I can hear the baby inside of you!"
    show amy normal
    amy.say "That's great news, [hero.name]..."
    amy.say "Why don't you try tapping on my stomach?"
    amy.say "Maybe the baby understands morse code and will tap back?"
    "My head pops up, a look of amazement on my face."
    mike.say "That's a great idea, Amy!"
    mike.say "Do you really thing that could work?"
    mike.say "And what kind of message should I send?"
    mike.say "Something really simple to start with, right?"
    show amy stuned at center, traveling(2.0, 1.0, (640, 1290))
    "It's about then that I get a good look at Amy's expression."
    "It's one of disbelief, fast turning to genuine amusement."
    show amy happy
    amy.say "Oh, [hero.name]..."
    amy.say "Most of the time you're pretty sharp."
    amy.say "But there are moments when you're the biggest dumbass I know!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
