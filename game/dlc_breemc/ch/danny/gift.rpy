init python:
    Event(**{
    "name": "danny_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(danny,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "danny",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label danny_give_female:
    if hero.morality <= -25:
        "He hands me a small paper bag."
        bree.say "Thanks."
        "I open it and there is an assortment of colorful pills inside it."
        danny.say "Some fun for my girl!"
        $ hero.gain_item("drugs")
    else:
        "He hands me an envelope."
        bree.say "Thanks."
        "I open it and there is 50{image=gui/icons/icon_money.png} inside it."
        $ hero.money += 50
        danny.say "Go buy whatever you want with it."
    return

label danny_give_birthday_female:
    "I can see that Danny looks edgy today, even for a guy of his particular type."
    "It's almost like he's got something on his mind and it's making him nervous."
    bree.say "Danny..."
    bree.say "Is everything okay?"
    "Danny spins around as soon as I ask the question."
    "And for a moment I think he's going to dash off or something similarly crazy."
    "But then he whips something out from wherever he's been hiding it."
    danny.say "SURPRISE!"
    bree.say "AARGH!"
    danny.say "Happy birthday, [hero.name]!"
    "My heart still pounding in my chest, I force a smile onto my face."
    "And then I accept the gift that Danny's waving around in front of me."
    bree.say "Aww..."
    bree.say "Thank you, Danny."
    bree.say "But maybe next time, don't shout so loud?"
    call danny_give_female from _call_danny_give_female
    return

label danny_give_christmas_female:
    danny.say "Happy Christmas, [hero.name]!"
    "Surprised by the sound of Danny's voice, I spin on my heel."
    "As soon as I do so, I see him standing there behind me."
    "And I can see that he's holding out a gift too."
    bree.say "Thank you, Danny!"
    bree.say "That's so thoughtful of you."
    danny.say "I hope you like it, [hero.name]..."
    danny.say "And it's not stolen, either!"
    call danny_give_female from _call_danny_give_female_1
    return

label danny_give_valentine_female:
    danny.say "Ah..."
    danny.say "You know how it's Valentine's day, [hero.name]?"
    "I turn to see Danny standing in front of me, looking oddly bashful."
    "Which is pretty rare for him, and so makes me all the more intrigued."
    bree.say "Yes, Danny..."
    bree.say "I am aware of that."
    "Danny nods."
    danny.say "Well, I got you a little something - a Valentine's gift."
    "I can't help smiling as I accept the gift from Danny."
    "Fighting to keep from chuckling at his awkward efforts to be romantic."
    bree.say "Thank you, Danny!"
    bree.say "That's so thoughtful of you."
    call danny_give_female from _call_danny_give_female_2
    return



label danny_gift_collar_female:
    if danny.sub >= 90:
        "Danny seems to enjoy the gift."
        $ danny.love += 5
        $ danny.set_sex_slave()
    else:
        "Danny seems to dislike the gift."
        $ danny.love -= 20
        $ danny.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
