init python:
    Item("puppy_plushy")

    Event(**{
    "name": "victor_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(victor,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "victor",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label victor_give_female:








    if "puppy_plushy" not in hero.inventory and victor.love >= 60:
        $ gift = "puppy_plushy"
        "He hands me cute little plushy."
        bree.say "What a cute little puppy plush!"
        victor.say "Take good care of her."
        bree.say "Sure Victor. Thank you!"
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label victor_gift_birthday_female:
    "I hand the package over to Victor, making sure to smile widely as I do so."
    bree.say "There you go, Victor!"
    if victor.sub >= 50:
        victor.say "Oh wow, [hero.name] - thank you so much!"
    elif victor.sub <= -50:
        victor.say "Oh, thank you, [hero.name]."
    else:
        victor.say "Wow, [hero.name] - thank you!"
    victor.say "You remembered my birthday?"
    if victor.flags.birthdayknown:
        if hero.morality >= 25:
            bree.say "Of course I did, Victor - you told me ages ago, remember?"
        else:
            bree.say "I always try to remember important dates, Victor!"
        if hero.morality <= -25:
            bree.say "Oh yeah - and I've got a special surprise for you later too!"
    else:
        "Oops - I totally forgot that was today!"
        "But that doesn't mean I have admit as much."
        if hero.morality >= 25:
            bree.say "Erm...of course I did, Victor!"
        else:
            bree.say "How could I ever forget?"
        if hero.morality <= -25:
            bree.say "Yeah, it's not like my brain's just full of dirty stuff, you know?"
    return

label victor_gift_swimsuit_female:
    bree.say "Erm, Victor..."
    bree.say "You remember we talked about maybe going to the waterpark?"
    bree.say "Or even to the beach?"
    "I see Victor's eyebrows rise as he's reminded of the conversation."
    victor.say "Ah, yeah, [hero.name]."
    bree.say "And you remember how you said you didn't have any swimming trunks?"
    victor.say "I do, [hero.name]."
    "I nod and smile as I produce the box that I've been hiding behind my back."
    if hero.morality >= 25:
        bree.say "Well here you go - I hope I got your size right!"
    else:
        bree.say "Well I got you some as a surprise - hope you like them!"
    if hero.morality <= -25:
        bree.say "Well now you do - and I bet you'll look super sexy in them!"
    "Victor still seems stunned and he takes the box from me and opens it."
    "And he doesn't look any less confused when he pulls out the trunks and holds them up."
    "Because he's probably looking at the smallest pair of budgie-smugglers he's ever seen!"
    if victor.sub >= 60:
        show victor happy
        "Which is why I'm quite surprised when he starts holding them up against himself."
        "As if trying to picture how they'll look when he's wearing them and nothing else."
        if victor.sub >= 50:
            victor.say "They're perfect, [hero.name] - thank you so much!"
        elif victor.sub <= -50:
            victor.say "They don't leave anything to the imagination - but I can make that work."
        else:
            victor.say "They're pretty small, [hero.name] - but I think I can pull them off."
        "I'm nodding all the time that Victor's saying this, trying to urge him on."
        "Because I can already imagine the sight of him in them."
        "And it's making me feel all funny inside!"
        $ victor.flags.sexyswimsuit = True
    else:
        show victor annoyed
        "I'm hoping that Victor might do something like hold them up to himself."
        "But instead he thrusts out his hand, offering them straight back to me."
        if victor.sub >= 50:
            victor.say "I...I can't wear these, [hero.name] - other women would be looking at me!"
        elif victor.sub <= -50:
            victor.say "I am not wearing those, [hero.name] - my privates are not for public display!"
        else:
            victor.say "These are way too small for me, [hero.name] - they'd cut off the circulation to my privates!"
        "I want to argue with Victor, to tell him that they're not really that small."
        "But I can tell from the look on his face that it's pointless."
        "So I just take the trunks back and let the matter drop."
        $ victor.love -= 4
    return

label victor_gift_collar_female:
    "I can feel the sensation of my heart pounding in my chest as I take out the box."
    "And the sense of trepidation only gets worse as I offer it to Victor."
    if hero.morality >= 25:
        bree.say "I...I got you something, Victor."
    if hero.morality <= -25:
        bree.say "Hey, big boy, I have something for you."
    else:
        bree.say "Hey, Victor, I got you a gift."
    bree.say "I think you're really going to like it."
    "I can see the surprise and interest on Victor's face as he takes the box from me."
    "And as he opens it up, I feel the tension rising inside of me all over again."
    "Even more so as he pulls out the length of fancy leather from inside."
    "Because now, as Victor holds it up, it's obvious that the thing is a collar."
    "One made along the same lines as a dog collar, but unmistakably sized for a human neck."
    bree.say "Erm..."
    bree.say "So..."
    bree.say "What do you think?"
    if victor.sub >= 90:
        show victor happy
        "I feel a flood of genuine relief as Victor begins to nod his head."
        "And another as he actually puts the collar around his neck too!"
        if victor.sub >= 50:
            victor.say "It's perfect, [hero.name] - I love it!"
        elif victor.sub <= -50:
            victor.say "Spot on, [hero.name] - I should have asked you for one of these myself!"
        else:
            victor.say "This is amazing, [hero.name] - how did you know?"
        victor.say "Now would you mind helping me put it on?"
        "I nod eagerly as I rush to help Victor putting on the collar."
        "Relieved and excited in equal measures that he's so into it."
        $ victor.set_sex_slave()
    else:
        show victor annoyed
        $ victor.love -= 10
        "I can almost feel my anxiety getting the better of me as Victor returns my gaze."
        "Because the look of bemusement in his eyes is plain to see."
        if victor.sub >= 50:
            victor.say "[hero.name], is that really how you see me?"
        elif victor.sub <= -50:
            victor.say "What in the hell is this supposed to be?"
        else:
            victor.say "You really want me to wear this?"
        victor.say "You think I'm, like, your dog?!?"
        "Victor tosses the collar back to me and then turns on his heel."
        "Walking away and leaving me to muse on just how badly I've screwed up."
    return

label victor_gift_slutty_pants_female:
    "I've been waiting for the right moment to give Victor the gift I got for him."
    "And when I sense the time is right, I whip out the box that it's wrapped up in."
    if hero.morality >= 25:
        bree.say "I...I got you something, Victor."
    if hero.morality <= -25:
        bree.say "Hey, big boy, I have something for you."
    else:
        bree.say "Hey, Victor, I got you a gift."
    bree.say "I think you're really going to like it."
    "I can see the surprise and interest on Victor's face as he takes the box from me."
    "And as he opens it up, I feel the tension rising inside of me all over again."
    "Which gets even worse as he unfolds the pants that I bought for him."
    "Or to be more precise, the very tight, very revealing pants I bought him!"
    "Victor seems to pick up on the cut of them straight away."
    "Looking up at me with a genuine surprise and amazement in his eyes."
    bree.say "Erm..."
    bree.say "So..."
    bree.say "What do you think?"
    if victor.love >= 75:
        "Much to my relief, Victor begins holding the pants against his legs."
        "Which is a sure sign that he's already picturing himself in them."
        if victor.sub >= 50:
            victor.say "I think it's great someone bought me new pants!"
        elif victor.sub <= -50:
            victor.say "I think this is a challenge, [hero.name] - to be confident enough to wear these pants!"
        else:
            victor.say "I think they're great, [hero.name] - I'd never have had the guts to buy them for myself!"
        "I'm nodding all the time that Victor's saying this, trying to urge him on."
        "Because I can already imagine the sight of him in them."
        "And it's making me feel all funny inside!"
    else:
        "Much to my dismay, Victor shakes his head."
        "And he makes a point of tossing the pants back to me."
        if victor.sub >= 50:
            victor.say "[hero.name], I can't wear this - everyone would stare at me!"
        elif victor.sub <= -50:
            victor.say "Nice try, [hero.name] - but I'm a hitman, not a male stripper!"
        else:
            victor.say "Sorry, [hero.name] - these are way too revealing for my line of work!"
        "I want to argue with Victor, to tell him that they're not really that revealing."
        "But I can tell from the look on his face that it's pointless."
        "So I just take the trunks back and let the matter drop."
    return

label victor_gift_sexy_pants_female:
    "I've been waiting for the right moment to give Victor the gift I got for him."
    "And when I sense the time is right, I whip out the box that it's wrapped up in."
    if hero.morality >= 25:
        bree.say "I...I got you something, Victor."
    if hero.morality <= -25:
        bree.say "Hey, big boy, I have something for you."
    else:
        bree.say "Hey, Victor, I got you a gift."
    bree.say "I think you're really going to like it."
    "I can see the surprise and interest on Victor's face as he takes the box from me."
    "And as he opens it up, I feel the tension rising inside of me all over again."
    "Which gets even worse as he unfolds the pants that I bought for him."
    "Or to be more precise, the very flattering pants in his precise size."
    "Victor seems to pick up on the cut of them straight away."
    "Looking up at me with a genuine surprise and amazement in his eyes."
    bree.say "Erm..."
    bree.say "So..."
    bree.say "What do you think?"
    if victor.love >= 50:
        "Much to my relief, Victor begins holding the pants against his legs."
        "Which is a sure sign that he's already picturing himself in them."
        if victor.sub >= 50:
            victor.say "I think it's great someone bought me such nice pants!"
        elif victor.sub <= -50:
            victor.say "I think this is a challenge, [hero.name] - to be secure in my manliness enough to wear these pants!"
        else:
            victor.say "I think they're great, [hero.name] - they really show off my legs!"
        "I'm nodding all the time that Victor's saying this, trying to urge him on."
        "Because I can already imagine the sight of him in them."
        "And it's making me feel all funny inside!"
    else:
        "Much to my dismay, Victor shakes his head."
        "And he makes a point of tossing the pants back to me."
        if victor.sub >= 50:
            victor.say "[hero.name], I can't wear this - everyone would be able to see my butt!"
        elif victor.sub <= -50:
            victor.say "Nice try, [hero.name] - but I'm a hitman, not a male model!"
        else:
            victor.say "Sorry, [hero.name] - I'd tear the ass out of these at work!"
        "I want to argue with Victor, to tell him that they're not really that tight."
        "But I can tell from the look on his face that it's pointless."
        "So I just take the trunks back and let the matter drop."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
