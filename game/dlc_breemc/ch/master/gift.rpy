init python:
    Item("turtle_keychain")

    Event(**{
    "name": "master_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(master,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "master",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label master_give_female:









    if "turtle_keychain" not in hero.inventory and master.love >= 40:
        $ gift = "turtle_keychain"
        "He hands me a cute keychain."
        bree.say "What a cute little turtle!"
        master.say "It sure is my dear."
        bree.say "Thank you Master. I'll always carry it."
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label master_give_birthday_female:
    master.say "Happy birthday, my dear!"
    master.say "And here is a gift for my favourite pupil!"
    bree.say "Oh, thank you, master!"
    bree.say "It's so sweet of you to remember my birthday."
    master.say "Ah, it was nothing, my dear."
    master.say "My mind is as well-trained as my body!"
    call master_give_female from _call_master_give_female
    return

label master_give_christmas_female:
    master.say "Merry Christmas, my dear."
    master.say "Here is your festive gift!"
    bree.say "Really?"
    bree.say "Master, you didn't have to buy me anything!"
    master.say "Nonsense, my dear."
    master.say "You've been a good pupil all year long."
    master.say "And doesn't that mean you get a present from an old man with a long beard?"
    call master_give_female from _call_master_give_female_1
    return

label master_give_valentine_female:
    master.say "Happy valentine's day, my dear!"
    master.say "I wanted to give you this gift."
    master.say "Just my way of saying thank you for being my valentine."
    bree.say "Aw, that's so kind of you, master!"
    bree.say "But now I feel bad."
    bree.say "Because I didn't get you anything!"
    master.say "Nonsense, my dear."
    master.say "Your company is the only gift I require."
    $ hero.gain_item("valentine_chocolates")
    return


label master_gift_collar_female:
    if master.sub >= 90:
        "Master seems to enjoy the gift."
        $ master.love += 5
        $ master.set_sex_slave()
    else:
        "Master seems to dislike the gift."
        $ master.love -= 20
        $ master.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
