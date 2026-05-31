init python:
    Consumable("protein_powder", effects=[("fitness", 5), ("hunger", 1)])

    Event(**{
    "name": "hanna_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "hanna",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label hanna_give_male:
    if "protein_powder" not in hero.inventory:
        $ gift = "protein_powder"
        "She hands me a bottle of protein powder."
        mike.say "Wow!\nThanks!"
        hanna.say "It's nothing..."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label hanna_give_valentine_male:
    "Hanna walks hesitantly towards me."
    call hanna_greet from _call_hanna_greet_7
    show hanna blush
    hanna.say "Happy valentine's day [hero.name]..."
    "Hanna hands me a box of chocolates."
    mike.say "Thank you, Hanna."
    $ hero.gain_item("valentine_chocolates")
    return

label hanna_give_birthday_male:
    "Hanna walks towards me."
    call hanna_greet from _call_hanna_greet_8
    show hanna happy
    hanna.say "Happy birthday [hero.name]!"
    call hanna_give_male from _call_hanna_give_male
    return

label hanna_give_christmas_male:
    "Hanna walks towards me."
    call hanna_greet from _call_hanna_greet_9
    show hanna happy
    hanna.say "Merry Christmas [hero.name]."
    call hanna_give_male from _call_hanna_give_male_1
    return

label hanna_birthday_gift_male:
    show hanna
    if hanna.flags.birthdayknown:
        mike.say "Happy birthday Hanna."
        hanna.say "How sweet, you remembered my birthday!"
    else:
        hanna.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ hanna.flags.birthdayknown = True
    return

label hanna_gift_swimsuit_male:
    show hanna happy
    hanna.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if hanna.sub >= 60:
        show hanna blush
        hanna.say "It's so pretty, thank you [hero.name]."
        $ hanna.flags.sexyswimsuit = True
    else:
        show hanna angry
        $ hanna.love -= 4
        hanna.say "Thanks but no thanks [hero.name]."
        $ hero.cancel_activity()
    return

label hanna_gift_sexy_dress_male:
    show hanna happy
    hanna.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if hanna.sub >= 30:
        show hanna blush
        hanna.say "Thank you [hero.name]."
        $ hanna.flags.sexydate = True
        $ hanna.flags.sluttydate = False
    else:
        show hanna annoyed
        $ hanna.love -= 4
        hanna.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label hanna_gift_slutty_dress_male:
    "I'm always aware of the fact that Hanna's very proud of her figure."
    "And that she likes to show it off every chance that she gets."
    "Which is something that could really rub the average guy the wrong way."
    "But not me."
    "Oh no, I've made a promise to myself that I won't be that kind of a jealous jerk."
    "In fact I've even decided to do something that should show Hanna I'm cool with it."
    "Now all I have to do is choose the right moment to put my plan into action."
    mike.say "Looking good there, Hanna..."
    mike.say "Have you been working out even harder than usual?"
    "To Hanna, compliments on her appearance are like a drug that she's long been addicted to."
    "And so it comes as no surprise that she instantly smiles and begins to unconsciously pose."
    show hanna talkative
    hanna.say "Nope!"
    hanna.say "You're just looking at the long-term benefits of a holistic fitness regimen."
    hanna.say "Believe me, when you run a gym, you have to look this good."
    show hanna normal
    "By now I've managed to fumble the box I've been hiding out from behind my back."
    "And I clumsily hold it out in front of me, like an offering to Hanna."
    mike.say "Speaking of you looking nice..."
    mike.say "I got you a little something."
    mike.say "You know...a little something that should help you...to look nice?"
    "Hanna's trying to look surprised as I place the box in her hands."
    "Like she's totally flattered and wanting to seem like doesn't think she deserves it."
    "But I can read her pretty well by now, and I know that she's desperate to open the thing."
    show hanna surprised
    hanna.say "Oh, [hero.name]…"
    hanna.say "You silly thing!"
    hanna.say "You don't need to go buying me presents like this."
    show hanna normal
    play sound [paper_ripping_1, paper_ripping_2]
    "For all of her performative denial, Hanna's still tearing at the wrapping paper."
    "Stripping it away like a ravenous carnivore trying to get at the meat of its prey."
    "And soon enough the box is open, letting her reach inside and pull out the contents."
    "Which is when I really feel the pressure beginning to mount."
    "As the daring dress that I spent all that time picking out for Hanna is revealed."
    "She holds onto the top, letting it cascade downwards and be revealed in all its glory."
    "And, just like in the store where I bought it, my head is filled with wild visions."
    "Images of the thing stretched tightly over Hanna's glorious curves."
    "The material clinging, so as to leave nothing to the imagination."
    mike.say "Erm..."
    mike.say "So, Hanna..."
    mike.say "What do you think?"
    "Hanna's attention seems to be totally occupied by the dress in her hands."
    "But at the sound of my voice, she looks up and straight into my eyes."
    if hanna.sub >= 70:
        show hanna talkative blush
        hanna.say "[hero.name], I'm amazed..."
        hanna.say "No guy ever bought me a dress like this before!"
        show hanna normal -blush
        mike.say "I...I know it's a bit daring."
        mike.say "But I just thought that..."
        "Hanna's hand shoots out, a finger pressing against my lips."
        show hanna talkative
        hanna.say "Shhh!"
        hanna.say "Don't ruin the moment by apologising."
        show hanna normal
        "I nod eagerly, which seems to be enough to convince Hanna."
        "As she removes her finger from my lips."
        "Then she starts to hold the dress up against herself."
        show hanna flirt
        hanna.say "What I mean by that was no guy's ever had the balls to buy me a dress like this."
        hanna.say "To be able to understand me and get me something that's so...well, so me!"
        hanna.say "They always seem to chicken out and get me something that's totally boring."
        show hanna happy
        mike.say "Oh..."
        mike.say "Well, that's not the kind of guy I am, Hanna."
        mike.say "No, I want to see you show off what you've got!"
        mike.say "I mean...in a positive, empowered and respectful way, of course."
        "Luckily for me, Hanna doesn't seem to really be listening as I begin to babble."
        "Instead she keeps on checking out the dress, happily in a world of her own."
        "Leaving me to hope that I might see her in it sooner, rather than later."
        $ hanna.flags.sluttydate = True
        $ hanna.flags.sexydate = False
    else:
        show hanna angry
        hanna.say "Oh, [hero.name]…"
        hanna.say "When am I going to get the chance to wear something like this?"
        show hanna upset
        mike.say "Erm..."
        mike.say "Well, I was thinking that we could go somewhere together…"
        mike.say "You know, somewhere really nice?"
        "Hanna rolls her eyes and then shoves the dress back into my open hands."
        show hanna angry
        hanna.say "Seriously, [hero.name]…"
        hanna.say "I'm a businesswoman, I run a gym."
        hanna.say "If you want to buy me clothes, then buy me something practical."
        hanna.say "Something that stretches, you know?"
        hanna.say "Something that I can give an aerobics class in?"
        show hanna upset
        "Feeling more than a little crestfallen, I nod my head."
        mike.say "Yes, Hanna..."
        mike.say "Sorry, Hanna..."
        mike.say "I'll be sure to try harder next time."
        $ hanna.love -= 10
        $ hero.cancel_activity()
    return

label hanna_gift_collar_male:
    show hanna
    hanna.say "So, what's up with you?"
    "I'm doing that thing again, where I start looking at Hanna's lean, athletic body beneath her tight, stretchy sportswear."
    "That thing where she notices that I'm looking at her, and smiles in a knowing manner."
    "That thing where I know that she's smiling in that knowing manner, and it makes me want to stare all the more..."
    "No...I need to focus - damn sexy Hanna!"
    mike.say "What's up with me?"
    mike.say "Nothing's up with me...not really..."
    mike.say "I just had something that I wanted to give to you, that's all!"
    "Hanna's smile is still knowing and slightly amused as she nods her head slowly."
    hanna.say "Well, that is kind of having something up with you, you know?"
    "I shake my head gently, both as a gesture of mild disagreement and in the hope of shaking some sense back into my brain."
    "If I don't assert some control over myself and the situation at hand, this is going to get away from me real soon."
    mike.say "What it is, Hanna, is that I feel I've gotten to know you pretty well recently."
    mike.say "At least well enough to know what it is that you really want from our relationship."
    mike.say "Maybe even well enough to know the things you want that you weren't even aware of yourself..."
    "At this, Hanna looks at me sideways, a little puzzled."
    "But I take her not interrupting me as a sign that she wants me to go on."
    "I already have the collar clutched in my hand, worrying it inside of my pocket."
    "And it takes an actual feat of will to force myself to pull it out and let Hanna see it for the first time."
    mike.say "And I think, Hanna, that one of those things is you wanting to grab the attention wherever you go."
    mike.say "You like to have people looking at you, and this will make sure that all eyes are on you - trust me on this..."
    "I hold up the collar so that she can make it out for what it really is, and not mistakenly think it's nothing more than normal jewellery."
    "The leather of the collar is a deep, royal blue with a silver plate attached."
    "On this is inscribed the word 'Juicy'."
    "Hanna's mouth works silently at first, her eyes widening as she realises the implications of what I'm offering to her."
    "She looks at me, and then quickly back at the collar."
    "And then she finally manages to speak."
    if hanna.sub < 90:
        $ hanna.sub -= 10
        $ hanna.love -= 20
        show hanna sad
        hanna.say "Oh, [hero.name]...oh no...no..."
        "Hanna begins to shake her head even as I hold the collar out towards her."
        "She pushes it to one side, not aggressively, but as though she can't stand to see me even holding it."
        mike.say "Hanna...I thought..."
        "No matter how I try to explain myself to her, Hanna refuses to meet my eye."
        "She turns away from me, and then turns her back completely."
        "And before I know it, she's jogging steadily away from me again."
        mike.say "Hanna...wait!"
        "She doesn't turn or say a word, just waves me away as she picks up speed."
        "A moment later, I'm left alone and painfully aware of how badly I just screwed up."
        $ hero.cancel_activity()
    else:
        show hanna blush
        hanna.say "Wh...what is that?"
        hanna.say "It looks like...a dog collar!"
        "I can see from her expression that she's more intrigued than offended."
        "And if she's not rejecting the idea out of hand, then I know that I have sufficient room for manoeuvre."
        mike.say "Sure, it looks like a dog collar, Hanna."
        mike.say "But it's in your size...and I'd like you to wear it."
        "Hanna licks her lips nervously, eyes still fixed on the collar I'm holding."
        hanna.say "You want me to, what - pretend to be your dog?"
        "I make a non-committal sound and tip my head from one side to the other."
        mike.say "It's not so much that I want you to pretend to be a dog, Hanna."
        mike.say "More like I want to show you off to everyone as the prize example of breeding that you are."
        hanna.say "You want to...show me off?"
        mike.say "I want to walk you, like those people walk their expensive dogs."
        mike.say "Loving the fact that people are looking in their direction while they do."
        "Hanna's hands are crossed over her chest now, and she's biting her lip as she ponders my words."
        mike.say "Imagine all of those eyes on you, Hanna, all those people unable to look away until you've passed out of sight..."
        mike.say "You wouldn't need to pretend that you don't want them to look at you anymore."
        mike.say "You could just bask in their attention and leave them wanting more."
        "Slowly, ever so slowly, Hanna reaches out gingerly with one hand to take the collar from me."
        "She turns it over more than once, glancing up at me as she does so."
        "And then finally, she lifts it to her neck and turns around so that I can fasten the strap."
        $ hanna.set_sex_slave()
        hide hanna
        show hanna blush
        "Once the collar is in place, she turns around to face me, her cheeks flushed and red."
        hanna.say "How do I look, [hero.name]?"
        "I shake my head in a small show of disapproval."
        mike.say "You just let me put a collar on you, Hanna."
        mike.say "It's time you got used to calling me 'Master'."
        "Hanna nods eagerly at this."
        hanna.say "Yes...Master!"
        $ hanna.sub += 4
        $ hanna.love += 8
    return

label hanna_gift_butt_plug_male:
    show hanna happy
    hanna.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if hanna.sub <= 50 or not hanna.sexperience:
        show hanna annoyed
        hanna.say "..."
        hanna.say "Keep it... I don't want it so keep it."
        hanna.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show hanna normal blush
        hanna.say "It's perfect!"
        show hanna flirt
        hanna.say "Thanks [hero.name], I'll make a good use of it."
        $ hanna.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
