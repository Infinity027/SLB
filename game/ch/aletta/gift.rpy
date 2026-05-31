init python:
    Event(**{
    "name": "aletta_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(aletta,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "aletta",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label aletta_give_male:
    "She hands me an envelope."
    mike.say "Thanks."
    "I open it and there is 50{image=gui/icons/icon_money.png} inside it."
    $ hero.money += 50
    aletta.say "Go buy whatever you want with it."
    return

label aletta_give_valentine_male:
    "Aletta walks confidently towards me."
    call aletta_greet from _call_aletta_greet_7
    show aletta blush
    aletta.say "Happy valentine's day [hero.name]..."
    "Aletta hands me a box of chocolates."
    mike.say "Thank you, Aletta."
    $ hero.gain_item("valentine_chocolates")
    hide aletta
    return

label aletta_give_birthday_male:
    "Aletta walks towards me."
    call aletta_greet from _call_aletta_greet_8
    show aletta happy
    aletta.say "Happy birthday [hero.name]!"
    call aletta_give_male from _call_aletta_give_male
    return

label aletta_give_christmas_male:
    "Aletta walks towards me."
    call aletta_greet from _call_aletta_greet_9
    show aletta happy
    aletta.say "Merry Christmas [hero.name]."
    call aletta_give_male from _call_aletta_give_male_1
    return

label aletta_birthday_gift_male:
    show aletta
    if aletta.flags.birthdayknown:
        mike.say "Happy birthday Aletta."
        aletta.say "How sweet, you remembered my birthday!"
    else:
        aletta.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ aletta.flags.birthdayknown = True
    return

label aletta_gift_swimsuit_male:
    show aletta happy
    aletta.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if aletta.sub >= 60:
        show aletta blush
        aletta.say "It's so pretty, thank you [hero.name]."
        $ aletta.flags.sexyswimsuit = True
    else:
        show aletta angry
        aletta.say "Thanks but no thanks [hero.name]."
        aletta.say "You think I would wear that?"
        $ aletta.love -= 4
        $ hero.cancel_activity()
    return

label aletta_gift_sexy_dress_male:
    show aletta happy
    aletta.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if aletta.sub >= 30:
        show aletta blush
        aletta.say "Thank you [hero.name]."
        $ aletta.flags.sexydate = True
        $ aletta.flags.sluttydate = False
    else:
        show aletta annoyed
        $ aletta.love -= 4
        aletta.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label aletta_gift_slutty_dress_male:
    "I remember back when I only worked with Aletta and she could be so totally intimidating."
    "So just imagine for a moment what it's like to actually be dating her for me now."
    "Especially when I feel like I'm going out on a limb with what I'm about to do."
    mike.say "H...hey, Aletta..."
    mike.say "How's it hanging?"
    "The moment the words are out of my mouth, I feel myself wincing."
    "Even more so when Aletta looks up, raising a single eyebrow."
    show aletta talkative
    aletta.say "Hmm..."
    aletta.say "Aren't you supposed to ask that when someone has a thing that hangs?"
    show aletta annoyed
    mike.say "Oh yeah, yeah..."
    mike.say "Totally, Aletta!"
    mike.say "I'm just a little nervous because..."
    mike.say "Because I got you something - so surprise!"
    "Beginning to panic, I'm galloping over everything that I mean to say smoothly."
    "And at the same time I whip the box I've been hiding out from behind my back."
    "Then I all but shove it straight into Aletta's face."
    "She blinks and takes a step backwards."
    "And she takes it from my hands before I can use it to push her over backwards."
    show aletta talkative
    aletta.say "Oh..."
    aletta.say "A gift for me?"
    aletta.say "And given with such enthusiasm too."
    show aletta normal
    "I'm so eager too see Aletta's reaction that I totally miss the sarcasm in her voice."
    mike.say "That's right, Aletta - so hurry up and open it already!"
    "Aletta lets out a weary sigh and begins to do as I ask."
    "While I look on with unconcealed anticipation."
    play sound [paper_ripping_1, paper_ripping_2]
    "Even more so once Aletta's torn away the wrapping paper and revealed what's inside."
    "Which is a dress of a rather daring cut, which I'm eager to see on her."
    if aletta.sub >= 70:
        show aletta stuned
        "The moment that she truly sees the dress, Aletta's whole mood seems to change."
        "Before now she was wearily going through the motions for the sake of appearances."
        "But now her eyes are wide open and she's holding the dress up against her."
        mike.say "So..."
        mike.say "What do you think?"
        mike.say "Pretty nice, huh?"
        "Aletta looks up at me, shaking her head as she does so."
        show aletta surprised
        aletta.say "How did you know?"
        aletta.say "I've always wanted a dress like this."
        aletta.say "But somehow I never got around to buying myself one."
        show aletta happy
        "All I can do is shrug as I begin to blush at Aletta's enthusiasm."
        mike.say "I guess that's what I'm here for, Aletta..."
        mike.say "To know you better than you know yourself!"
        "Aletta's nodding away as I say all of this."
        "But she looks more than a little distracted right now."
        "So I can't be sure if she's actually hearing me or not."
        show aletta talkative
        aletta.say "Yes, yes...of course."
        aletta.say "I have to wear this the first chance I get."
        aletta.say "Even if it's just to reward you for being so insightful, [hero.name]."
        show aletta happy
        "Okay, now my head really is starting to spin a little!"
        mike.say "Sure thing, Aletta - just name the date!"
        $ aletta.flags.sexydate = False
        $ aletta.flags.sluttydate = True
    else:
        show aletta annoyed
        "But much to my disappointment, Aletta doesn't seem all that impressed."
        "In fact she seems to be holding the dress at arm's length."
        "Almost like it's giving off an offensive stench."
        mike.say "So..."
        mike.say "What do you think?"
        mike.say "Pretty nice, huh?"
        "Aletta simply sighs, closing her eyes as though gathering her strength."
        "And then she shoves the dress back into my hands, box and all."
        "In fact she shoves it so hard I can't help taking a step backwards."
        mike.say "Urgh!" with vpunch
        show aletta angry
        aletta.say "No, [hero.name], it is not 'nice'."
        aletta.say "It's cheap and tasteless."
        aletta.say "And I never want to see it again."
        show aletta annoyed
        mike.say "Okay, Aletta - I guess it's a good thing I kept the receipt!"
        $ aletta.love -= 10
        $ hero.cancel_activity()
    return

label aletta_gift_collar_male:
























    mike.say "Okay, okay...Aletta, we've become far more than just a couple of people that happen to work together, haven't we?"
    "She regards me quizzically, but nods in agreement all the same."
    mike.say "In fact, you might say that we've become a couple that works together instead - if you follow?"
    "Aletta rolls her eyes at the cheesiness of the line, and rotates a finger to tell me I need to get to the point more quickly."
    mike.say "I suppose what I'm trying to say is that, when I first met you...I'll be honest - I kinda thought you were a bitch!"
    mike.say "But that changed when I finally got to know the person that you really are."
    mike.say "And then I discovered that, while you weren't really the bitch that you pretended to be, you secretly wanted someone to make you their own bitch for real!"
    "The look on Aletta's face in response to this is hard to read."
    "On the one hand, the colour in her cheeks could be the first signs of anger and outrage."
    "But on the other, it could just as easily be the beginnings of her admitting her true feelings and finally releasing all of those pent up emotions."
    "I've come too far to quit now, so I steel my nerves and press on."
    mike.say "You've been hiding behind the image of a hard-ass that you've created for yourself for too long, Aletta."
    mike.say "I want you to put this on and let people know that you really are a bitch after all."
    mike.say "But I want you to let them know that you're MY, bitch, Aletta!"
    "At this, I pull out a black leather collar from my pocket, with a chain lead attached to it."
    "The collar is unadorned, save for the word 'Bitch', spelt out in golden letters on the front."
    if aletta.sub < 90:
        show aletta angry
        "Aletta's eyes widen in horror at the sight of the collar, and she lets out a fierce shriek that almost pierces my eardrums."
        aletta.say "[hero.name], you asshole!"
        aletta.say "Just what kind of a sick mother-fucker are you?!?"
        "She swings for me, hitting the hand that's holding the collar and lead, sending them spinning away."
        aletta.say "To think that I let you close to me!"
        aletta.say "To think that I trusted you!"
        aletta.say "You don't know the first thing about me."
        aletta.say "Not if you think that what I want is to be treated like an animal!"
        "She begins to stalk away from me, turning her head to hurl yet more abuse my way as she leaves."
        aletta.say "If you want someone to put a collar on and call a bitch, then buy a goddamn dog!"
        $ aletta.love -= 20
        $ aletta.sub -= 20
        $ hero.cancel_activity()
    else:
        "It seems that I was right, as Aletta tentatively accepts the collar from me and begins to fasten it around her own neck."
        "She says nothing the whole time, but keeps on shooting nervous glances in my direction."
        "Her expression makes me think that she's afraid of either doing something wrong, or else going to slowly as she puts it on."
        "So much so that I'm actually surprised to see that her hands aren't shaking."
        "But once the collar is securely fastened around her neck, Aletta looks up at me with expectant eyes, as if she's awaiting my next command."
        $ aletta.set_sex_slave()
        hide aletta
        show aletta
        mike.say "How does that feel, Aletta?"
        "She puts a hand to her neck, feeling the presence of the collar and seeming to understand what it signifies."
        aletta.say "It...it feels...good, it feels good, [hero.name]..."
        "I frown a little and shake my head."
        mike.say "Now, now, Aletta - I don't remember saying that you could call me that!"
        aletta.say "I'm sorry...M...Master?"
        "I smile at the use of the appropriate title, nodding my head in approval."
        "Things changed significantly between Aletta and myself today, to the degree that I'd be confident to say they'll never be the same again."
    return

label aletta_gift_butt_plug_male:
    show aletta happy
    aletta.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if aletta.sub <= 50 or not aletta.sexperience:
        show aletta annoyed
        aletta.say "..."
        aletta.say "Keep it... I don't want it so keep it."
        aletta.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show aletta normal blush
        aletta.say "It's perfect!"
        show aletta flirt
        aletta.say "Thanks [hero.name], I'll make a good use of it."
        $ aletta.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
