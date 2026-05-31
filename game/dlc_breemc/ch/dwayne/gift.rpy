init python:
    Event(**{
    "name": "dwayne_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(dwayne,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "dwayne",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label dwayne_give_female:








    if "luxury_bracelet" not in hero.inventory and dwayne.love >= 40:
        $ gift = "luxury_bracelet"
        "He hands me a small well design bag.."
        bree.say "Wow Dwayne!\nYou shouldn't have."
        dwayne.say "Of course I needed to. What will I look like for if you don't wear expensive jewelery?"
        bree.say "Thank you anyway, it's ravishing."
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label dwayne_give_birthday_female:
    dwayne.say "Happy birthday, [hero.name]!"
    dwayne.say "And here's your present too."
    bree.say "Wow, Dwayne..."
    bree.say "This looks expensive!"
    dwayne.say "Oh it is, [hero.name] - you bet it is."
    dwayne.say "Only the best when you're with me, girl!"
    call dwayne_give_female from _call_dwayne_give_female
    return

label dwayne_give_christmas_female:
    dwayne.say "Merry Christmas, [hero.name]!"
    dwayne.say "Unlike Santa, I deliver my gifts in person!"
    bree.say "Dwayne!"
    bree.say "I love the gift."
    bree.say "But I'm worried you're spoiling me!"
    dwayne.say "Nonsense, [hero.name], complete nonsense."
    dwayne.say "If anything, I'm educating you on the finer things in life!"
    call dwayne_give_female from _call_dwayne_give_female_1
    return

label dwayne_give_valentine_female:
    dwayne.say "Hey, there's my sexy little valentine!"
    dwayne.say "And here's a little something to reward her."
    dwayne.say "Because she's so DAMN hot!"
    bree.say "You bought me a valentine's gift?"
    bree.say "Oh, Dwayne - you didn't have to do that!"
    dwayne.say "Ha, ha...isn't that the entire point, [hero.name]?"
    dwayne.say "I don't do things because I HAVE to."
    dwayne.say "I do things because I WANT to!"
    $ hero.gain_item("valentine_chocolates")
    return







































label dwayne_give_a_gift_reaction_positive_female:
    "As soon as Dwayne sees what's inside the box, his smile vanishes."
    show expression f"{active_girl.id} therock"
    "And the look on his face becomes one of dumbstruck amazement."
    "Like he simply can't believe what he's seeing in there."
    show expression f"{active_girl.id} happy"
    dwayne.say "[hero.name]..."
    dwayne.say "What the..."
    dwayne.say "Where did you find this?"
    show expression f"{active_girl.id} smile"
    "I can feel the sense of delight welling up inside of me."
    "Because I can tell that Dwayne's gob-smacked with the gift."
    bree.say "Oh..."
    bree.say "It took quite some searching, you know?"
    bree.say "But I just knew it was the right gift for you."
    "Dwayne nods slowly as he listens to me explain myself."
    show expression f"{active_girl.id} happy"
    "But the whole time he's still staring at the gift in his hand."
    "And I feel even more pride swell up in me as he does so."
    "Because believe me, that is one hard man to impress."
    return

label dwayne_give_a_gift_reaction_neutral_female:
    "As soon as Dwayne sees what's inside, his smile kind of fades."
    show expression f"{active_girl.id} therock"
    "It's not like Dwayne looks pissed at what's in the box."
    "More like he's seriously unimpressed with what he's seeing."
    dwayne.say "Oh..."
    show expression f"{active_girl.id} normal"
    dwayne.say "Okay..."
    "I force a smile onto my face, trying to lighten Dwayne's mood."
    bree.say "Well, Dwayne..."
    bree.say "What do you think of your gift?"
    "Dwayne kind of shrugs and shakes his head a little."
    "Like he can't even summon up the enthusiasm to pretend he likes it."
    show expression f"{active_girl.id} shout"
    dwayne.say "Like I already said, [hero.name]..."
    dwayne.say "It's okay."
    dwayne.say "So stop fishing, yeah?"
    show expression f"{active_girl.id} annoyed"
    "I can almost feel the flush of my cheeks turning red."
    "The embarrassment sweeping over me as Dwayne dismisses the gift and me alike."
    return

label dwayne_give_a_gift_reaction_negative_female:
    "As soon as Dwayne sees what's inside, the smile on his face vanishes."
    show expression f"{active_girl.id} therock"
    "And by the time he looks up at me, there's a serious frown in its place."
    show expression f"{active_girl.id} shout"
    dwayne.say "Is this supposed to be some kind of a joke, [hero.name]?"
    show expression f"{active_girl.id} vangry"
    dwayne.say "Because if it is, I don't think it's very funny!"
    show expression f"{active_girl.id} upset"
    "I find myself shrugging my shoulders and shaking my head."
    "Because I can't wrap my head around Dwayne's reaction to the gift."
    bree.say "But..."
    bree.say "I don't understand..."
    bree.say "I thought you'd love it!"
    show expression f"{active_girl.id} shout"
    dwayne.say "Well here's a reality check, [hero.name]..."
    show expression f"{active_girl.id} vangry"
    dwayne.say "You thought wrong!"
    show expression f"{active_girl.id} upset"
    "With that, Dwayne thrusts the box back into my hands."
    "Which leaves me feeling utterly deflated."
    return


label dwayne_gift_collar_female:
    if dwayne.sub >= 90:
        "Dwayne seems to enjoy the gift."
        $ dwayne.love += 5
        $ dwayne.set_sex_slave()
    else:
        "Dwayne seems to dislike the gift."
        $ dwayne.love -= 20
        $ dwayne.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
