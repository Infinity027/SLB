init python:
    Event(**{
    "name": "cassidy_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "cassidy",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label cassidy_give_male:
    "She hands me a box, obviously from a pastry shop."
    mike.say "Thanks."
    $ hero.gain_item("cake")
    return

label cassidy_give_valentine_male:
    "Cassidy walks hesitantly towards me."
    call cassidy_greet from _call_cassidy_greet_7
    show cassidy blush
    cassidy.say "Happy valentine's day [hero.name]..."
    "Cassidy hands me a box of chocolates."
    mike.say "Thank you, Cassidy."
    $ hero.gain_item("valentine_chocolates")
    return

label cassidy_give_birthday_male:
    "Cassidy walks towards me."
    call cassidy_greet from _call_cassidy_greet_8
    show cassidy happy
    cassidy.say "Happy birthday [hero.name]!"
    call cassidy_give_male from _call_cassidy_give_male
    return

label cassidy_give_christmas_male:
    "Cassidy walks towards me."
    call cassidy_greet from _call_cassidy_greet_9
    show cassidy happy
    cassidy.say "Merry Christmas [hero.name]."
    call cassidy_give_male from _call_cassidy_give_male_1
    return

label cassidy_birthday_gift_male:
    show cassidy
    if cassidy.flags.birthdayknown:
        mike.say "Happy birthday, Cassidy!"
        cassidy.say "How sweet, you remembered my birthday!"
    else:
        cassidy.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ cassidy.flags.birthdayknown = True
    return

label cassidy_gift_swimsuit_male:
    show cassidy happy
    cassidy.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if cassidy.sub >= 60 or cassidy.status == 'pet':
        show cassidy blush
        cassidy.say "Thank you [hero.name], but you really want me to wear that?"
        mike.say "Yes!"
        cassidy.say "That seems really...overly sexy, don't you think?"
        mike.say "That's the point. You deserve to show off your beauty."
        $ cassidy.flags.sexyswimsuit = True
    else:
        show cassidy angry
        cassidy.say "No thanks."
        $ cassidy.love -= 5
        $ cassidy.sub -= 5
        $ hero.cancel_activity()
    hide cassidy
    return

label cassidy_gift_sexy_dress_male:
    show cassidy happy
    cassidy.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if cassidy.sub >= 30 or cassidy.status == 'pet':
        show cassidy blush
        cassidy.say "Thank you [hero.name]."
        $ cassidy.flags.sexydate = True
        $ cassidy.flags.sluttydate = False
    else:
        show cassidy angry
        $ cassidy.love -= 4
        cassidy.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label cassidy_gift_slutty_dress_male:
    "I've been doing the best I can to keep the surprise present hidden from Cassidy."
    "But the moment she lays eyes on me, it's like she's got some kind of sixth sense."
    "Well, at least when it comes to presents being brought into her immediate vicinity."
    "And she's on me like a bloodhound with a scent to follow!"
    show cassidy talkative
    cassidy.say "Hey, [hero.name]..."
    cassidy.say "What's that you got there?"
    show cassidy normal
    "All the time Cassidy's asking me this, she's trying to duck around behind me."
    "Stretching and straining to see what I have held back there and out of view."
    "Hell, she even tries the old cross, you know?"
    "Ducking first one way and then the other in the hope I won't react in time."
    mike.say "Wha..."
    mike.say "What the..."
    mike.say "Cassidy..."
    mike.say "Will you stop it?!?"
    show cassidy talkative
    cassidy.say "Hard to say, under the circumstances."
    cassidy.say "I don't normally quit until I get what I want."
    cassidy.say "So that means there's always the option to just give it to me!"
    show cassidy normal
    "Sensing that the fun isn't going to last too much longer, I decide to fold."
    "Which means pulling out the package and handing it over to Cassidy."
    mike.say "Okay, Cassidy..."
    mike.say "You win."
    show cassidy happy
    "Cassidy claps her hands together with glees."
    "And then she plucks the package out of my hands."
    cassidy.say "I always do!"
    cassidy.say "Now let's see what you got me..."
    play sound [paper_ripping_2, paper_ripping_1]
    "It doesn't take long for Cassidy to tear off the wrapping paper."
    "And the she pulls the dress I bought for her out of the box."
    show cassidy normal
    "Letting it unfold and hang from her hands, she looks it up and down."
    "Something that shows off just how skimpy and revealing the cut of the thing really is."
    mike.say "So, Cassidy..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    if cassidy.sub >= 70:
        "Cassidy starts nodding her head almost the moment I'm done asking the question."
        "And the next thing I know, she's holding the dress up against herself."
        "Smoothing the slinky fabric over the equally slinky curves of her body."
        "And watching her doing that is certainly making the purchase feel worthwhile."
        show cassidy talkative
        cassidy.say "Oh, [hero.name]..."
        cassidy.say "I must have, like, a million dresses in my wardrobe."
        cassidy.say "But I never had one as daring as this before."
        show cassidy wink
        "I'm nodding eagerly by now, doing all I can to encourage Cassidy."
        mike.say "Well, I'm happy to give you your million and first dress."
        mike.say "As well as to help you along the road to being a bad girl!"
        "Cassidy giggles with mischief."
        show cassidy happy
        cassidy.say "You'd just better hope daddy doesn't catch me in this!"
        "Normally a girl's father would be the farthest thing from my mind."
        "But the I remember that the dad in question here just so happens to be Dwayne."
        "My super-rich, super-alpha boss - a guy who could make my life hell on the merest whim."
        mike.say "Erm..."
        mike.say "Yeah, Cassidy..."
        mike.say "Maybe we should keep this one for private occasions?"
        "I'm not quite sure if Cassidy actually hears what I'm saying to her."
        "But even if she doesn't, I'm still going to be as careful as I possibly can."
        "Because even a dress like that isn't worth suffering Dwayne's wrath for."
        $ cassidy.flags.sexydate = False
        $ cassidy.flags.sluttydate = True
    else:
        "Cassidy starts shaking her head almost the moment I'm done asking the question."
        "And the next thing I know, she's roughly shoving it back into my hands."
        show cassidy angry
        cassidy.say "Nice?!?"
        cassidy.say "Are you kidding me?"
        cassidy.say "Do you know what Daddy would do to me if her caught me in that thing?"
        show cassidy upset
        "Normally I'd be quick to dismiss the very notion of what a girl's dad might happen to think."
        "But the I remember that the dad in question here just so happens to be Dwayne."
        "My super-rich, super-alpha boss - a guy who could make my life hell on the merest whim."
        "So maybe I should have thought this one out a little more carefully?"
        mike.say "Ah..."
        mike.say "Now that you mention it, Cassidy..."
        mike.say "You might well have a point there!"
        show cassidy angry
        cassidy.say "Well of course I do!"
        cassidy.say "So you'd better hurry up and make that thing disappear, okay?"
        cassidy.say "And super fast too!"
        show cassidy annoyed
        $ cassidy.love -= 10
        $ hero.cancel_activity()
    return

label cassidy_gift_collar_male:
    show cassidy happy
    mike.say "I have something for you."
    cassidy.say "Oh really? I hope it's not some cheap crap."
    mike.say "No, this is...well, maybe not expensive by your standards, but it wasn't cheap."
    "I hand the box to Cassidy, and she opens it, slowly. There is no small amount of avarice in her eyes until she sees the collar in the box."
    show cassidy normal
    "She pulls it out and holds it up, looking at it from every angle, clearly showing off the word 'Princess' etched into it."
    cassidy.say "You expect me to wear this?"
    if cassidy.status == 'mistress':
        cassidy.say "No, this must be for you to wear, and the present is that I get to tug you around on a leash!"
        mike.say "No, that's not what I."
        cassidy.say "Put it on for me, [hero.name]!"
        "Oh, fuck. I clearly did not think this through, did I?"
        cassidy.say "Put this on right now, or we're going to march down to the piercing shop. We'll pierce your head and get the word [hero.name] tattooed right there above your public hair. Your choice."
        "I take the collar from her outstretched hands and look at it. This is humiliating."
        cassidy.say "Come on, I want to see you in it."
        "I'm about to say \"fuck this\", but then I remember she'll probably get me fired. So, I grit my teeth and put the collar on."
        cassidy.say "Oh. Yes, [hero.name], you certainly are a pretty, pretty Princess, aren't you?"
        "I look down at the floor, feeling the anger and humiliation burning at my cheeks."
        "Cassidy laughs at my discomfort."
        $ cassidy.sub -= 10
        cassidy.say "Okay, fine, you can take it off. But from now on, I'm going to call you Princess."
        mike.say "Oh God no."
        cassidy.say "Oh, it's the least I can do."
        "I take the collar off and put it back in the box."
        $ cassidy.flags.mikeNickname = "Bitch"
        cassidy.say "I'm going to save this, though. It might come in handy for some of our play, later on, [hero.name]."
    elif cassidy.status == 'pet':
        mike.say "Yes, of course. You're my pet. I want everyone to know it."
        show cassidy sad
        cassidy.say "It's humiliating!"
        mike.say "Nonsense, it's beautiful. You {b}are{/b} a bit of a spoiled Princess, and this just advertises that fact a little bit."
        if cassidy.love < 160 or cassidy.sub < 90:
            cassidy.say "Please don't make me wear this."
            mike.say "This one is non negotiable. It doesn't hurt, and frankly you look beautiful in it."
            "She looks at me for a moment, then looks back at the collar in her hands. After a moment--reluctantly--she places it around her neck. The clasp clicks together with a loud, satisfying {b}snap{/b}."
            $ cassidy.collared = True
            mike.say "The only thing more beautiful than you in that collar will be you in that collar, on your knees."
            show cassidy blush
            cassidy.say "Yes, Master. As you wish."
            $ cassidy.flags.mikeNickname = "Master"
            $ cassidy.sub += 10
            $ cassidy.love -= 6
        else:
            show cassidy happy
            cassidy.say "It's beautiful, Master. Thank you for this amazing gift."
            "She looks at me for a moment, then looks back at the collar in her hands. After a moment, she places it around her neck. The clasp clicks together with a loud, satisfying {b}snap{/b}."
            $ cassidy.collared = True
            mike.say "The only thing more beautiful than you in that collar will be you in that collar, on your knees."
            show cassidy blush
            cassidy.say "And I look forward to serving you that way, Master."
            mike.say "I'm a lucky, lucky man to get such a beautiful, talented sex slave like yourself. I guess what you put me through to get here was actually worth it."
            cassidy.say "It'll be worth it when your cock is in my mouth, Master, for sure."
            "She gives me a little wink."
            $ cassidy.love += 10
    else:
        show cassidy angry
        cassidy.say "You cannot possibly be serious. Why the fuck would I wear such a thing?"
        "Cassidy throws the collar at me. It hits me right in the forehead, bouncing off and clattering to the floor."
        cassidy.say "Fuck you, [hero.name]."
        $ cassidy.love -= 20
        $ hero.cancel_activity()
    hide cassidy
    return

label cassidy_gift_butt_plug_male:
    show cassidy happy
    cassidy.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if cassidy.sub <= 50 or not cassidy.sexperience:
        show cassidy annoyed
        cassidy.say "..."
        cassidy.say "Keep it... I don't want it so keep it."
        cassidy.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show cassidy normal blush
        cassidy.say "It's perfect!"
        cassidy.say "Thanks [hero.name], I'll make a good use of it."
        $ cassidy.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
