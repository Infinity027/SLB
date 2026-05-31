init python:
    Equip("guardian_of_the_cosmos_t-shirt", gender="female", price=100, effects={"geek": 30, "charm": -10})

    Event(**{
    "name": "jack_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(jack,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "jack",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label jack_give_female:








    if "guardian_of_the_cosmos_t-shirt" not in hero.inventory:
        $ gift = "guardian_of_the_cosmos_t-shirt"
        "He hands me what looks like a T-shirt."
        bree.say "A weird design T-shirt?"
        jack.say "Not any T-shirt [hero.name], it's one a the few that were made for the infamous show Guardian of the Cosmos!"
        bree.say "A rare piece like that must be expensive. Thanks Jack!"
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label jack_give_birthday_female:
    jack.say "Happy birthday, [hero.name]!"
    jack.say "And here's your gift from me."
    bree.say "Thank you, Jack."
    bree.say "That's so thoughtful of you!"
    jack.say "I picked it out myself, [hero.name]."
    jack.say "I've been trying to pick up any hints you might have dropped!"
    bree.say "Thanks, Jack - it's just what I wanted!"
    call jack_give_female from _call_jack_give_female
    return

label jack_give_christmas_female:
    jack.say "Merry Christmas, [hero.name]!"
    jack.say "Here's your gift from me."
    jack.say "Come on, [hero.name] - open it now!"
    bree.say "Right now, Jack?"
    bree.say "Shouldn't we wait until Christmas morning?"
    jack.say "No way, [hero.name] - I want to see the look on your face when you see what I got you!"
    bree.say "Okay, Jack, I'll open it now!"
    call jack_give_female from _call_jack_give_female_1
    return

label jack_give_valentine_female:
    jack.say "Happy valentine's, [hero.name]!"
    jack.say "I got you a little something too..."
    bree.say "Oh, Jack - you didn't have to do that!"
    jack.say "Aw, [hero.name]..."
    jack.say "I'm just so happy to have a valentine this year."
    jack.say "It's the least I could do!"
    bree.say "The best gift of all is having you as my valentine, Jack!"
    $ hero.gain_item("valentine_chocolates")
    return

label jack_birthday_gift_female:
    show jack
    "I take a deep breath and pull out the gift that I've been hiding."
    "And then I hand it over to Jack."
    bree.say "Happy Birthday, Jack!"
    if jack.flags.birthdayknown:
        jack.say "Aw, thanks so much, [hero.name]!"
        jack.say "I wasn't dropping hints when I told you the date!"
        bree.say "No worries, Jack - I'd never have remembered otherwise!"
    else:
        jack.say "Aw, thanks so much, [hero.name]!"
        jack.say "But I never told you when it was - so how did you know?"
        bree.say "I don't know, Jack - would you believe it was a lucky guess?"
        $ jack.flags.birthdayknown = True
    return

label jack_gift_swimsuit_female:
    "I make sure that I have a smile on my face as I pull out the gift I've been hiding."
    "And then I hand it straight over to Jack, watching as his face lights up with surprise."
    jack.say "Whoa..."
    jack.say "What's this, [hero.name]?"
    jack.say "It's not my birthday!"
    bree.say "I know, I know..."
    bree.say "It's just something to wear at the beach, or in the pool!"
    "Jack keeps on smiling until he pulls out what was inside the package."
    "It's a pair of swimming trunks...well, more like briefs."
    jack.say "Wow, [hero.name]..."
    jack.say "These thing are small!"
    bree.say "I think I heard someone call them 'budgie smugglers'!"
    bree.say "Or maybe a 'banana hammock'!"
    if jack.sub >= 60:
        "Jack holds the briefs against himself, stretching them out as he does so."
        "He looks up at me, his eyes wide with amazement."
        jack.say "I...I can't wear these...can I?!?"
        jack.say "I mean...not when I'm such a big guy!"
        "I shake my head and make a tutting sound."
        "Totally dismissing Jack's reservations."
        bree.say "Of course you can, Jack!"
        bree.say "And you've got nothing to be ashamed of either!"
        bree.say "I love your body - it's big and manly!"
        bree.say "Plus they'll show off another part of your manhood too!"
        "Jack begins to nod eagerly as I talk him round."
        "Clearly he's already thinking of the possibilities."
        jack.say "Okay, [hero.name] - so long as you like them."
        jack.say "I'll wear them the next time we're at the beach!"
        bree.say "Or the pool!"
        jack.say "That too!"
        $ jack.flags.sexyswimsuit = True
    else:
        $ jack.love -= 10
        "Jack shakes his head and thrusts them back at me."
        jack.say "I...I'm grateful, [hero.name] - really I am."
        jack.say "But there's no way I can wear something like this!"
        jack.say "I'd get laughed out of the place!"
        "I take the trunks back from Jack, nodding at the same time."
        "I'm already feeling embarrassed to have got it so wrong."
        bree.say "Erm...okay, Jack."
        bree.say "I'll take them back to the store."
        bree.say "Maybe I can exchange them for something more...roomy?"
        jack.say "No, [hero.name], no..."
        jack.say "I think it's best that I buy my own swimwear from now on!"
        $ hero.cancel_activity()
    return

label jack_gift_sexy_dress_female:
    show jack happy
    jack.say "Oh, [hero.name], is it for me?"
    "He unwraps the sexy outfit."
    show jack normal
    jack.say "Thanks but no thanks [hero.name], I'm not ready to wear this..."
    $ hero.cancel_activity()
    return

























































label jack_gift_slutty_dress_female:
    show jack happy
    jack.say "Oh, [hero.name], is it for me?"
    "He unwraps the slutty outfit."
    show jack normal
    jack.say "Thanks but no thanks [hero.name], I'm not ready to wear this..."
    $ hero.cancel_activity()
    return























































label jack_gift_collar_female:
    "I know that I'm taking a risk in giving this gift to Jack."
    "But it's been gnawing away at me ever since I got the idea."
    "And I'm a sure as I can be that he's been sending me the right signals."
    "So the only way I can scratch this itch is to go through with it."
    "I hand it straight over to Jack, watching as his face lights up with surprise."
    jack.say "Whoa..."
    jack.say "What's this, [hero.name]?"
    jack.say "It's not my birthday!"
    bree.say "I know, I know..."
    bree.say "It's just something to wear."
    bree.say "Something I think you're going to like..."
    "Jack keeps on smiling until he pulls out what was inside the package."
    "It's a dog-collar and leash, made of leather and just his size."
    jack.say "Wow, [hero.name]..."
    jack.say "Why didn't you just say you wanted to get a dog?"
    bree.say "No, Jack, no..."
    bree.say "It's for you to wear!"
    bree.say "I've been getting signals from you, yeah?"
    bree.say "Picking up hints that you want me to be the one in charge?"
    "Jack's eyes go wide as he begins to understand just what I mean."
    if jack.sub >= 90:
        $ jack.set_sex_slave()
        jack.say "H...how did you know?"
        jack.say "[hero.name], how did you know?"
        jack.say "I always wanted do get into this sort of stuff!"
        "Jack grips the collar like he's afraid someone will take it off him."
        "And for a moment I think he's going to start growling like a dog!"
        bree.say "I...I guess it was just a hunch!"
        bree.say "You want me to put that thing on you?"
        "Jack nods eagerly and I hurry to oblige."
        hide jack
        show jack
        "And once the collar is around his neck, he looks as proud as can be."
        $ jack.love += 5
        jack.say "This feels great, [hero.name]!"
        jack.say "Like it's just supposed to be there!"
        "I nod as fast as I can, my heart hammering in my chest."
        "Amazed that my guess proved to be one hundred percent correct!"
    else:
        jack.say "Well, yeah, [hero.name]!"
        jack.say "I kinda like it when you take over..."
        $ jack.love -= 20
        $ jack.sub -= 10
        jack.say "But that doesn't mean I want to be your dog!"
        "Jack thrusts the collar and leash back at me."
        "And it looks like he's more than glad to be rid of them."
        bree.say "Oh..."
        bree.say "Oh shit..."
        bree.say "Look, I'm sorry, Jack..."
        bree.say "I totally misread the situation!"
        "Jack holds his hand up and shakes his head."
        jack.say "It's okay, [hero.name]."
        jack.say "Just promise me you won't do this again, okay?"
        "I nod as fast as I can, my heart hammering in my chest."
        "How could I have fucked up so badly?!?"
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
