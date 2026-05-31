init python:
    Equip("dolca_gabbane_purse", type="accessory", price=400, effects={"charm": 10})

    Event(**{
    "name": "mike_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(mike,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "mike",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label mike_give_female:
    if "dolca_gabbane_purse" not in hero.inventory and mike.love >= 60:
        $ gift = "dolca_gabbane_purse"
        "He hands me a small well design bag."
        bree.say "No way!\nIs it for real?!"
        mike.say "Sure it is!"
        bree.say "Thank you! Thank you sooo much!"
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label mike_give_birthday_female:
    "[mike.name] walks towards me."
    call mike_greet from _call_mike_greet_1
    show mike happy
    mike.say "Happy birthday [hero.name]!"
    call mike_give_female from _call_mike_give_female
    return

label mike_give_christmas_female:
    "[mike.name] walks towards me."
    call mike_greet from _call_mike_greet_2
    show mike happy
    mike.say "Merry Christmas [hero.name]."
    call mike_give_female from _call_mike_give_female_1
    return

label mike_give_valentine_female:
    "[mike.name] walks hesitantly towards me."
    call mike_greet from _call_mike_greet_3
    show mike blush
    mike.say "Happy valentine's day [hero.name]..."
    "[mike.name] hands me a box of chocolates."
    bree.say "Thank you, [mike.name]."
    $ hero.gain_item("valentine_chocolates")
    return

label mike_birthday_gift_female:
    show mike
    if mike.flags.birthdayknown:
        bree.say "Happy birthday [mike.name]."
        mike.say "How sweet, you remembered my birthday!"
    else:
        mike.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ mike.flags.birthdayknown = True
    return

label mike_bigger_staff_pill_gift_female:
    show mike
    if not 'mike_bigger_staff_pill_gift_female' in DONE:
        "I've been trying to tell myself that it's not a big deal."
        "That I can cope with [mike.name] just the way he is."
        "But who am I kidding - it's a big deal in every sense of the word!"
        "I'm a woman with needs, and he's just not satisfying them."
        bree.say "Hey, [mike.name]..."
        mike.say "Hey, [hero.name]..."
        show fx question
        mike.say "Is something wrong?"
        "I could be subtle and circumspect about all of this."
        "But there's just no way I can keep holding it all in."
        "So I decide that the best thing is to be brutally honest."
        hide fx
        bree.say "You know there is, [mike.name]."
        bree.say "It's your damn manhood."
        bree.say "It's just too small for me!"
        show mike surprised
        "[mike.name]'s eyes go wide as I hurl the accusation at him."
        "And his hands instinctively move to cover his groin."
        show mike blush
        mike.say "B...but, [hero.name]..."
        mike.say "It's not the size that counts, right?"
        show mike happy
        mike.say "It's what you do with it that makes a difference!"
        "I shake my head, dashing [mike.name]'s hope of explaining himself."
        bree.say "Yeah, the thing is..."
        $ mike.love -= 1
        bree.say "That's what girls say to guys who aren't huge down there."
        show mike sad
        bree.say "But they still have enough to make it count if they try really hard."
        mike.say "What are you saying, [hero.name]?"
        show mike normal
        mike.say "That I need to try harder?"
        "I shake my head, beginning to get a little frustrated."
        bree.say "No, [mike.name]."
        bree.say "You could try as hard as you like, but it wouldn't make a difference."
        bree.say "You're feeding a pea to a whale."
        bree.say "You're tossing a hotdog into a hallway."
        show mike down
        mike.say "You...you mean..."
        "I feel my temper finally fray and then snap."
        "And I can't help giving [mike.name] both barrels."
        show mike surprised
        $ mike.love -= 2
        bree.say "I'm saying you have a tiny cock, [mike.name]!"
        $ mike.love -= 2
        bree.say "You possess a micro-penis!"
        $ mike.love -= 5
        bree.say "Your undersized manhood doesn't even touch the sides!"
        show mike sad
        "By now, [mike.name]'s staring down at his feet, unable to look me in the eye."
        mike.say "I..."
        mike.say "I'm sorry, [hero.name]..."
        mike.say "But I don't see what I can do about that!"
        "This seems like the perfect moment to introduce my solution."
        "And so I whip it out, waving it under [mike.name]'s nose."
        "Now he finally looks up, surprised by what he's seeing."
        show mike normal
        show fx question
        mike.say "Huh?"
        mike.say "What's that, [hero.name]?"
        bree.say "It's a pill to cure your ills, [mike.name]!"
        hide fx
        bree.say "Just swallow this down and watch it grow."
        "I hold out the pill, waiting for [mike.name] to take it from me."
        show mike down
        "But he hesitates for a moment, as if unsure."
        bree.say "Come on, [mike.name]!"
        bree.say "What are you waiting for?!?"
        if mike.love >= 150 or mike.sub >= 80:
            "[mike.name] finally seems to shake off his reluctance."
            "He reaches out and takes the pill from my hand."
            "Then he lifts it to his lips as I nod eagerly."
            "But then, at the last minute, he pauses."
            mike.say "[hero.name]..."
            mike.say "This thing is safe, right?"
            bree.say "What are you talking about?"
            bree.say "Of course it's safe!"
            show mike normal
            mike.say "So you read the instructions that came with it?"
            mike.say "There are no side effects, yeah?"
            mike.say "I can take this if I'm on other medication?"
            "All of his questions serve to throw me a little."
            "Because the truth is that I have no idea."
            "I don't know if the pill came with any instructions."
            "And even if it did, I certainly didn't bother to read them."
            "So it looks like lying is the only logical solution."
            bree.say "Of course it's safe."
            bree.say "Totally safe and one hundred percent legit too."
            show mike annoyed
            mike.say "Are you sure, [hero.name]?"
            mike.say "You kind of hesitated a little there."
            mike.say "Almost like you were making something up."
            bree.say "What?"
            bree.say "Me?"
            bree.say "Now way!"
            show mike down
            "Oddly, this seems to be enough to convince [mike.name]."
            "And he shrugs before popping the pill into his mouth."
            show mike normal
            mike.say "Okay, [hero.name] - I trust you."
            "I watch with a growing sense of anticipation as he swallows it."
            show mike down
            "And with any luck, something else will soon be growing too."
            "But then I notice that [mike.name]'s staring at his groin."
            "Almost like he's expecting something to happen straight away."
            bree.say "It's not Viagra, [mike.name]!"
            bree.say "It'll probably take a while to work."
            show mike normal
            show fx exclamation
            mike.say "Oh..."
            mike.say "Okay, [hero.name]..."
            hide fx
            mike.say "I'll find a tape-measure."
            mike.say "And I'll let you know when I see any change down there."
            $ mike.flags.dicksize = "hung"
        else:
            "I'm fully expecting [mike.name] to reach out and take the pill."
            show mike upset
            "But instead the expression on his face changes."
            "It goes from helpless shame to firm resolve."
            "And the change in him is almost a little scary."
            show mike angry
            mike.say "No way, [hero.name]..."
            mike.say "I'm not taking that damn thing!"
            bree.say "Oh yes you are."
            bree.say "I've had just about enough of you and your tiny cock, mister!"
            bree.say "Now take the pill and have your manhood man-up!"
            "I fix [mike.name] with my most serious stare."
            "But it's not enough to change his mind."
            mike.say "I will not!"
            show mike upset
            mike.say "Fuck sake, [hero.name]..."
            mike.say "Imagine how you'd react if I said your breasts were too small."
            mike.say "And then I told you that I wanted you to have them pumped up like balloons!"
            "I can't help thrusting my chest towards [mike.name] as I shake my head."
            bree.say "I'm not the one with the problem here, pal!"
            bree.say "My breasts aren't up for scrutiny!"
            "[mike.name] starts to back away."
            "And he holds up a hand to keep me from following."
            mike.say "Where did you even get it from, huh?"
            mike.say "God knows what could be in that thing, [hero.name]."
            mike.say "I could end up with all sorts of crazy side-effects."
            show mike angry
            mike.say "And all because you're obsessed with cock!"
            bree.say "How dare you?!?"
            bree.say "I am not obsessed."
            bree.say "I just want my pussy filled for a change!"
            bree.say "Is that really too much to ask?!?"
            mike.say "Then go buy a king-sized dildo, and leave me out of it!"
            $ mike.love -= 10
            $ mike.sub -= 10
            $ hero.cancel_activity()
        $ DONE['mike_bigger_staff_pill_gift_female'] = game.days_played
    else:
        bree.say "Will you do me a favor and take that pill again?"
        if mike.flags.dicksize == "hung":
            mike.say "Sorry [hero.name]..."
            mike.say "For you I'll do anything, but I really think walking on three legs will be harder than on two..."
            $ hero.cancel_activity()
        elif mike.love >= 150 or mike.sub >= 80:
            mike.say "If it makes you happier then yes, I'll take it."
            if mike.flags.dicksize == "smalldick":
                $ mike.flags.dicksize = "medium"
            else:
                $ mike.flags.dicksize = "hung"
        else:
            show mike angry
            $ mike.love -= 5
            mike.say "No."
            bree.say "What do you mean \"No\"?"
            mike.say "No, I won't take that pill for you!"
            $ hero.cancel_activity()
    return

label mike_smaller_staff_pill_gift_female:
    show mike
    if not 'mike_smaller_staff_pill_gift_female' in DONE:
        "I've been trying to tell myself that it's just a little thing."
        "That I can cope with [mike.name] just the way he is."
        "But who am I kidding - it's a big thing in every sense of the word!"
        "I'm a woman with needs, but even I can't take much more of it."
        bree.say "Hey, [mike.name]..."
        mike.say "Hey, [hero.name]..."
        show fx question
        mike.say "Is something wrong?"
        "I could be subtle and circumspect about all of this."
        "But there's just no way I can keep holding it all in."
        "So I decide that the best thing is to be brutally honest."
        hide fx
        bree.say "You know there is, [mike.name]."
        bree.say "It's your damn manhood."
        bree.say "It's just too big for me!"
        show mike surprised
        "[mike.name]'s eyes go wide as I hurl the accusation at him."
        "And his hands instinctively move to cover his groin."
        show mike blush
        mike.say "B...but, [hero.name]..."
        mike.say "I thought girls liked big ones, right?"
        show mike happy
        mike.say "Like, the bigger the better?"
        "I shake my head, dashing [mike.name]'s hope of explaining himself."
        bree.say "Yeah, the thing is..."
        bree.say "That's what girls say to guys who aren't huge down there."
        show mike sad
        $ mike.love -= 1
        bree.say "But what you have is some kind of crazy trouser snake, [mike.name]."
        bree.say "Actually, it's more like a monster anaconda!"
        show mike normal
        mike.say "What are you saying, [hero.name]?"
        mike.say "That I need to be more gentle in future?"
        "I shake my head, beginning to get a little frustrated."
        bree.say "No, [mike.name]."
        bree.say "You could try to be as gentle as you like, but it wouldn't make a difference."
        bree.say "You're beating me to death with your meat."
        bree.say "You're pecking me to death with your pecker."
        show mike down
        mike.say "You...you mean..."
        "I feel my temper finally fray and then snap."
        "And I can't help giving [mike.name] both barrels."
        show mike surprised
        $ mike.love -= 2
        bree.say "I'm saying your cock is too big, [mike.name]!"
        $ mike.love -= 2
        bree.say "You possess an over-sized manhood!"
        $ mike.love -= 5
        bree.say "You're starting to make my pussy have an echo!"
        show mike sad
        "By now, [mike.name]'s staring down at his feet, unable to look me in the eye."
        mike.say "I..."
        mike.say "I'm sorry, [hero.name]..."
        mike.say "But I don't see what I can do about that!"
        "This seems like the perfect moment to introduce my solution."
        "And so I whip it out, waving it under [mike.name]'s nose."
        "Now he finally looks up, surprised by what he's seeing."
        show mike normal
        show fx question
        mike.say "Huh?"
        mike.say "What's that, [hero.name]?"
        bree.say "It's a pill to cure your ills, [mike.name]!"
        hide fx
        bree.say "Just swallow this down and watch it shrink."
        "I hold out the pill, waiting for [mike.name] to take it from me."
        show mike down
        "But he hesitates for a moment, as if unsure."
        bree.say "Come on, [mike.name]!"
        bree.say "What are you waiting for?!?"
        if mike.love >= 150 or mike.sub >= 80:
            "[mike.name] finally seems to shake off his reluctance."
            "He reaches out and takes the pill from my hand."
            "Then he lifts it to his lips as I nod eagerly."
            "But then, at the last minute, he pauses."
            mike.say "[hero.name]..."
            mike.say "This thing is safe, right?"
            bree.say "What are you talking about?"
            bree.say "Of course it's safe!"
            show mike normal
            mike.say "So you read the instructions that came with it?"
            mike.say "There are no side effects, yeah?"
            mike.say "I can take this if I'm on other medication?"
            "All of his questions serve to throw me a little."
            "Because the truth is that I have no idea."
            "I don't know if the pill came with any instructions."
            "And even if it did, I certainly didn't bother to read them."
            "So it looks like lying is the only logical solution."
            bree.say "Of course it's safe."
            bree.say "Totally safe and one hundred percent legit too."
            show mike annoyed
            mike.say "Are you sure, [hero.name]?"
            mike.say "You kind of hesitated a little there."
            mike.say "Almost like you were making something up."
            bree.say "What?"
            bree.say "Me?"
            bree.say "Now way!"
            show mike down
            "Oddly, this seems to be enough to convince [mike.name]."
            "And he shrugs before popping the pill into his mouth."
            show mike normal
            mike.say "Okay, [hero.name] - I trust you."
            "I watch with a growing sense of anticipation as he swallows it."
            show mike down
            "But with any luck, something else will soon be shrinking."
            "But then I notice that [mike.name]'s staring at his groin."
            "Almost like he's expecting something to happen straight away."
            bree.say "It's not supposed to work straight away, [mike.name]!"
            bree.say "It'll probably take a while to work."
            show mike normal
            show fx exclamation
            mike.say "Oh..."
            mike.say "Okay, [hero.name]..."
            hide fx
            mike.say "I'll go find a tape-measure."
            mike.say "And I'll let you know when I see any change down there."
            $ mike.flags.dicksize = "smalldick"
        else:
            "I'm fully expecting [mike.name] to reach out and take the pill."
            show mike upset
            "But instead the expression on his face changes."
            "It goes from helpless shame to firm resolve."
            "And the change in him is almost a little scary."
            show mike angry
            mike.say "No way, [hero.name]..."
            mike.say "I'm not taking that damn thing!"
            bree.say "Oh yes you are."
            bree.say "I've had just about enough of you and your huge cock, mister!"
            bree.say "Now take the pill and down-size your manhood!"
            "I fix [mike.name] with my most serious stare."
            "But it's not enough to change his mind."
            mike.say "I will not!"
            show mike upset
            mike.say "Fuck sake, [hero.name]..."
            mike.say "Imagine how you'd react if I said your breasts were too big."
            mike.say "And then I told you that I wanted you to have them reduced!"
            "I can't help thrusting my chest towards [mike.name] as I shake my head."
            bree.say "I'm not the one with the problem here, pal!"
            bree.say "My breasts aren't up for scrutiny!"
            "[mike.name] starts to back away."
            "And he holds up a hand to keep me from following."
            mike.say "Where did you even get it from, huh?"
            mike.say "God knows what could be in that thing, [hero.name]."
            mike.say "I could end up with all sorts of crazy side-effects."
            show mike angry
            mike.say "And all because you're obsessed with cock!"
            bree.say "How dare you?!?"
            bree.say "I am not obsessed."
            bree.say "I just want my pussy to not get stretched like an elastic band for a change!"
            bree.say "Is that really too much to ask?!?"
            mike.say "Then go buy a tiny dildo, and leave me out of it!"
            $ mike.love -= 10
            $ mike.sub -= 10
            $ hero.cancel_activity()
        $ DONE['mike_smaller_staff_pill_gift_female'] = game.days_played
    else:
        bree.say "Will you do me a favor and take that pill again?"
        if mike.flags.dicksize == "smalldick":
            mike.say "Sorry [hero.name]..."
            mike.say "For you I'll do anything, but I still want to be able to see it without a magnifying glass..."
            $ hero.cancel_activity()
        elif mike.love >= 150 or mike.sub >= 80:
            mike.say "If it makes you happier then yes, I'll take it."
            if mike.flags.dicksize == "hung":
                $ mike.flags.dicksize = "medium"
            else:
                $ mike.flags.dicksize = "smalldick"
        else:
            show mike angry
            $ mike.love -= 5
            mike.say "No."
            bree.say "What do you mean \"No\"?"
            mike.say "No, I won't take that pill for you!"
            $ hero.cancel_activity()
    return


label mike_gift_collar_female:
    if mike.sub >= 90:
        "[mike.name] seems to enjoy the gift."
        $ mike.love += 5
        $ mike.set_sex_slave()
    else:
        "[mike.name] seems to dislike the gift."
        $ mike.love -= 20
        $ mike.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
