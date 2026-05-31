init python:
    Event(**{
    "name": "palla_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "palla",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label palla_birthday_gift_male:
    show palla
    if palla.flags.birthdayknown:
        mike.say "Happy birthday Palla."
        palla.say "How sweet, you remembered my birthday!"
    else:
        palla.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ palla.flags.birthdayknown = True
    return

label palla_gift_swimsuit_male:
    show palla happy
    palla.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if palla.sub >= 60:
        show palla blush
        palla.say "Wow. Wait, you bought this? When did you get good taste in clothes?"
        mike.say "Maybe you rubbed off on me."
        $ palla.flags.sexyswimsuit = True
    else:
        show palla angry
        palla.say "Uh. Yeah. Wow. You haven't earned this yet. Seriously, what makes you think I'd accept shit like this from you?"
        $ hero.cancel_activity()
    return

label palla_gift_sexy_dress_male:
    show palla happy
    palla.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if palla.sub >= 30:
        show palla blush
        palla.say "Thank you [hero.name]."
        $ palla.flags.sexydate = True
        $ palla.flags.sluttydate = False
    else:
        show palla annoyed
        $ palla.love -= 4
        palla.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label palla_gift_slutty_dress_male:
    "I'd be nervous buying clothes for almost any girl that I was seeing or trying to charm."
    "But when you add into the equation the fact that the girl in question is literally a fashion model..."
    "Well, you can imagine that makes the stakes even higher than usual."
    "And on top of that, I also had to choose to buy something that's more than a little controversial too."
    "So by the time I get to see Palla, I'm already anxious and beginning to sweat."
    "All of which she spots almost the second that she sets eyes on me."
    show palla talkative
    palla.say "Hello..."
    palla.say "Somebody's looking extra shifty today!"
    palla.say "What are you up to, [hero.name]?"
    show palla normal
    "I do the best I can to look like I have no earthly idea what Palla's talking about."
    "Shaking my head and trying harder to hide the box that I have held behind my back."
    mike.say "Huh?"
    mike.say "What are you talking about, Palla?"
    mike.say "I'm just standing here, minding my own business while I wait for you."
    show palla joke
    palla.say "Is that so?"
    palla.say "Then you won't mind if I..."
    show palla normal
    "Palla makes a gesture to her right, and my eyes instinctively follow it."
    "Which allows her to neatly slip to the left and get behind me."
    "And before I know it, she's snatches the box out of my hands."
    mike.say "Wha…"
    mike.say "What are you..."
    show palla joke
    palla.say "Well, well, well..."
    palla.say "What do we have here?"
    show palla normal
    "Palla easily evades my clumsy attempts to take the box back."
    play sound [paper_ripping_1, paper_ripping_2]
    "Tearing at the wrapping-paper as she dodges out of my way."
    "And before I can do anything about it, she pulls out what's inside."
    "The dress that I picked out for her unfolds in the blink of an eye."
    "Flapping and swaying as the both of us stop and stare at it."
    "And I can tell you that Palla really is staring at it too."
    "Because of all the things I've seen her in, none of them have been as daring as this dress."
    mike.say "Erm..."
    mike.say "Surprise, Palla!"
    mike.say "I hope you like what I got you?"
    if palla.sub >= 70:
        "Palla's still looking the dress up and down as I finish asking the question."
        "And it takes her a few seconds more to realise that I was actually speaking."
        "But when she finally looks up and meets my eye, I can see that she's genuinely amazed."
        show palla happy
        palla.say "[hero.name]…"
        palla.say "This is..."
        palla.say "This is amazing!"
        show palla normal
        "I feel myself sag in the middle as I let out genuine sigh of relief."
        "A massive weight seeming to suddenly lift off of my shoulders."
        mike.say "You mean that you like it?"
        mike.say "I was worried that..."
        mike.say "Well, what with you being so into fashion and all that..."
        show palla joke
        palla.say "I know, I know..."
        palla.say "But sometimes you need a new eye to change things up."
        palla.say "A hail Mary from someone who knows absolutely nothing about fashion."
        palla.say "You know - someone completely clueless?"
        show palla flirt
        mike.say "And that's me!"
        mike.say "Hey...wait a minute!"
        $ palla.flags.sluttydate = True
        $ palla.flags.sexydate = False
    else:
        "Palla's still looking the dress up and down as I finish asking the question."
        "And it takes her a few seconds more to realise that I was actually speaking."
        "But when she finally looks up and meets my eye, I can see that she's genuinely amazed."
        show palla vangry
        palla.say "[hero.name]…"
        palla.say "This is..."
        palla.say "This is fucking awful!"
        show palla angry
        "Palla's words make me feel like I've been punched in the gut."
        "And the weight of her disapproval almost bends me over too."
        mike.say "You mean that you don't like it?"
        show palla vangry
        palla.say "Don't like it?"
        palla.say "[hero.name], I fucking loathe it!"
        palla.say "This is the single vilest piece of clothing I've ever been presented with."
        palla.say "Normally I'd say take it back and get a refund."
        palla.say "But in this case, I think you should burn it!"
        show palla angry
        mike.say "Oh..."
        mike.say "Okay, Palla."
        $ palla.love -= 10
        $ hero.cancel_activity()
    return

label palla_gift_flowers_male:
    $ palla.flags.gaveflowers = True
    show palla
    if palla.love < 40:
        "Palla looks at the flowers like I just handed her a can of worms."
        palla.say "Do you really think you're going to get on my good side with these?"
        "Then she rolls her eyes and looks away. When she thinks I'm not looking, she smells the flowers and smiles."
    elif palla.love < 80:
        "Palla looks at the flowers and cracks a very slight smile."
        palla.say "I hope you don't think you're going to get into my pants with just these?"
        mike.say "Oh no, you're much too bitchy for that."
        "Palla snorts, but doesn't look offended."
    elif palla.love < 120:
        "Palla looks at the flowers, then at me, then back at the flowers and smiles."
        palla.say "Good try, [hero.name] but it's going to take more than these to get...this."
        mike.say "See, I get a pretty smile and then you gotta be a bitch about it."
        palla.say "Yep, that's what you get with me."
    else:
        "Palla smiles brightly at the flowers."
        palla.say "Why [hero.name], does this mean you like LIKE me?"
        mike.say "Sure, when you're not being a bitch."
        "Palla laughs and flips me off."
    return

label palla_gift_sweets_male:
    $ palla.flags.gavesweets = True
    show palla
    if palla.love < 40:
        "Palla looks at the sweets I just gave her and rolls her eyes."
        palla.say "If I eat this I'm going to have to work out an extra 30 minutes. Is that really what you're after?"
        mike.say "Sure, I like the thought of you all sweaty."
        "Her eyes widen for a moment. Then she catches herself and turns it into an exaggerated eye roll."
        palla.say "What a creep."
    elif palla.love < 80:
        "Palla looks at the sweets. First she smiles, then sighs."
        palla.say "Seriously, now I'm going to need an extra half hour in the gym. You're not worth that."
        mike.say "I think you meant to say \"Thank you.\""
        palla.say "No, I meant to say \"Fuck you.\""
        mike.say "Yup, that's what I get for giving nice things to a world class bitch!"
        "Palla snorts, but doesn't disagree."
    elif palla.love < 120:
        "Palla looks at the sweets and cracks a smile, though she's clearly trying not to."
        palla.say "Oh fuck I know I said I like the romance and candy and flowers and crap but at the time I wasn't thinking about the extra half hour in the gym these things cost me."
        mike.say "Tell you what, I'll go to the gym and spot and count for you."
        palla.say "I bet you're the kind of asshole that will count 1, 2, 3, 4, 3, 3, 3, 4. No thanks."
        mike.say "Oh fuck yeah. I definitely like the idea of making you pump extra hard."
        show palla blush
        palla.say "Ok, that's enough of that, you creep!"
    else:
        "Palla smiles brightly at the sweets."
        palla.say "You better help me work off these extra calories later!"
        mike.say "On the dance floor or just on the floor?"
        show palla blush
        palla.say "On the dance floor. Yes. That's what I meant."
    return

label palla_gift_collar_male:
    show palla happy
    mike.say "I have something for you."
    "I take the box with the collar I got for her and hold it out for her."
    "Naturally, Palla looks suspicious. No matter how close our relationship gets, I'm not sure she'll ever fully trust me--or anyone, really."
    "She carefully opens the box and examines the contents, narrowing her eyes at it without touching what's inside."
    if palla.sub >= 90 and palla.flags.slavepath and "palla_event_13" in DONE:
        "She stares at it for several moments, and I cannot, for the life of me, tell what she's thinking."
        mike.say "Well? Do you like it?"
        palla.say "I'm thinking."
        mike.say "What about?"
        "She looks at me, locking her gaze onto my own."
        palla.say "You know I like...a little rough stuff. This, though. This seems like a lot. Like, something permanent."
        mike.say "It is. It is permanent."
        palla.say "So. So you think I'm your bitch?"
        mike.say "Yes. I feel like I've earned it."
        "She swallows, but she hasn't flown into fury yet, so far."
        palla.say "If...if I wear this, then...I need to know that you...you'll always take care of me. That you love me, and that you need me. And that you'll never hurt me."
        "I don't have to hesitate."
        $ palla.set_sex_slave()
        hide palla
        show palla happy
        mike.say "Palla, I love you. I need you, I will always take care of you, and I will never hurt you. Well, maybe a little, because you like it rough. But only that."
        "She bites her lip, then nods. She holds the box toward me."
        palla.say "W-would you?"
        "She closes her eyes as I slip the collar around her neck. As my fingers brush across her skin, it is tight with goosebumps. She is shaking with fear, anticipation, and a large amount of pure arousal."
        "As it snaps shut, I speak."
        mike.say "You are mine, Palla. My bitch. Mine to command. You will call me master, and you will...serve me."
        "She opens her eyes and looks at me."
        palla.say "Yes, Master. I will give you anything you desire, my love."
        $ palla.love += 5
        $ palla.sub += 5
    elif palla.flags.slavepath:
        "She stares at it for several moments, and I cannot, for the life of me, tell what she's thinking."
        mike.say "Well? Do you like it?"
        palla.say "I'm thinking."
        mike.say "What about?"
        palla.say "I'm thinking whether or not you've earned this, yet."
        mike.say "Have I?"
        "She thinks about it for another half a minute or so, then shakes her head."
        "She offers the box to me."
        palla.say "Not yet. I'm not ready."
        mike.say "Well, that's disappointing. At least you're not mad."
        "Palla smiles."
        palla.say "No, not mad. Just not ready for this."
        $ hero.cancel_activity()
    else:
        palla.say "You have got to be fucking kidding me."
        "Uh oh."
        palla.say "Why the fuck would I wear something this...crass! Ugh. You're a real piece of shit, [hero.name]."
        if palla.love > 120:
            palla.say "I thought we might've had something, but I guess you're just fucking with me, aren't you?"
        else:
            palla.say "I can't imagine why you might've thought this was a good idea."
        palla.say "Go fuck yourself."
        "She dumps the box in a trash can on the way out."
        $ palla.love -= 40
        $ palla.sub -= 40
        $ hero.cancel_activity()
    return

label palla_give_male:
    if "cologne" not in hero.inventory:
        $ gift = "cologne"
        "She hands me a bottle of expensive cologne."
        mike.say "Wow, what's this for?"
        if palla.love < 80:
            palla.say "So I don't have to smell you when you talk to me."
        elif palla.love < 120 or palla.sexperience < 3:
            palla.say "It's a scent I like a lot."
        else:
            palla.say "So the next time I'm fucking you I smell this. I can't wait!"
        mike.say "Wow! Thanks!"
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label palla_give_valentine_male:
    "Palla walks hesitantly towards me."
    call palla_greet from _call_palla_greet_7
    show palla blush
    palla.say "Happy valentine's day [hero.name]..."
    "Palla hands me a box of chocolates."
    mike.say "Thank you, Palla."
    $ hero.gain_item("valentine_chocolates")
    return

label palla_give_birthday_male:
    "Palla walks towards me."
    call palla_greet from _call_palla_greet_8
    show palla happy
    palla.say "Happy birthday [hero.name]!"
    call palla_give_male from _call_palla_give_male
    return

label palla_give_christmas_male:
    "Palla walks towards me."
    call palla_greet from _call_palla_greet_9
    show palla happy
    palla.say "Merry Christmas [hero.name]."
    call palla_give_male from _call_palla_give_male_1
    return

label palla_gift_butt_plug_male:
    show palla happy
    palla.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if palla.sub <= 50 or not palla.sexperience:
        show palla annoyed
        palla.say "..."
        palla.say "Keep it... I don't want it so keep it."
        palla.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show palla normal blush
        palla.say "It's perfect!"
        show palla flirt
        palla.say "Thanks [hero.name], I'll make a good use of it."
        $ palla.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
