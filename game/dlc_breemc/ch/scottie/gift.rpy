init python:
    Event(**{
    "name": "scottie_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(scottie,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "scottie",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label scottie_give_female:









    if "sexy_swimsuit_equip" not in hero.inventory and scottie.love >= 40:
        $ gift = "sexy_swimsuit_equip"
        "He hands me what looks like a bunch of strings."
        bree.say "Wow!\nIs that really to wear in public?"
        scottie.say "Sure, it'll look great on you!"
        bree.say "Well thank you, I'll try it someday."
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label scottie_give_birthday_female:
    scottie.say "Happy birthday, [hero.name]!"
    scottie.say "I got you a present too."
    bree.say "Oh, thank you, Scottie!"
    bree.say "But how did you remember the date?"
    bree.say "I'm just worried because you remember the last time I helped you learn something?"
    bree.say "And it made you forget how to drive?"
    scottie.say "Hey, that is not what happened!"
    scottie.say "I was just drunk!"
    call scottie_give_female from _call_scottie_give_female
    return

label scottie_give_christmas_female:
    scottie.say "Merry Christmas, [hero.name]!"
    scottie.say "Here's your present."
    bree.say "Can I open this now, Scottie?"
    scottie.say "Oh no, [hero.name] - no way!"
    scottie.say "You have to wait until Christmas morning."
    scottie.say "Otherwise Santa will be pissed with you!"
    bree.say "Well, he would be, Scottie - if he was real!"
    scottie.say "Wait...what?!?"

    $ hero.gain_item("pastry")
    return

label scottie_give_valentine_female:
    scottie.say "Happy valentine's day, [hero.name]!"
    scottie.say "I got you a present too."
    scottie.say "For being the best valentine in the whole world!"
    bree.say "Aw, thanks, Scottie!"
    bree.say "I'm really impressed."
    scottie.say "Impressed that I got you a gift?"
    bree.say "No, impressed that you know about valentine's day."
    bree.say "I didn't even think you could spell 'valentine's!"
    scottie.say "HEY!"
    $ hero.gain_item("valentine_chocolates")
    return

label scottie_birthday_gift_female:
    show scottie
    if scottie.flags.birthdayknown:
        bree.say "Happy birthday Scottie."
        scottie.say "How sweet, you remembered my birthday!"
    else:
        scottie.say "How do you know my birthday?"
        bree.say "I didn't, it's just pure luck."
        $ scottie.flags.birthdayknown = True
    return


label scottie_gift_collar_female:
    if scottie.sub >= 90:
        "Scottie seems to enjoy the gift."
        $ scottie.love += 5
        $ scottie.set_sex_slave()
    else:
        "Scottie seems to dislike the gift."
        $ scottie.love -= 20
        $ scottie.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
