init python:
    Consumable("make-up_for_dummies", price=100, effects=[("charm", 2), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])

    Event(**{
    "name": "angela_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(angela,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "angela",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label angela_give_female:






    if "make-up_for_dummies" not in hero.inventory:
        $ gift = "make-up_for_dummies"
        "She hands me a pretty large book."
        bree.say "What is this Angela?"
        angela.say "Something to help you glow up, you need it."
        bree.say "Thanks I guess."
    else:
        $ gift = "flowers"
        "She hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label angela_give_birthday_female:
    angela.say "Happy birthday, [hero.name]!"
    angela.say "And here's a gift to celebrate too."
    bree.say "Thank you, Angela."
    bree.say "That's so thoughtful of you!"
    call angela_give_female from _call_angela_give_female
    return

label angela_give_christmas_female:
    angela.say "Merry Christmas, [hero.name]!"
    angela.say "And don't open this until Christmas Morning, okay?"
    bree.say "A gift for me?"
    bree.say "Angela, that's so kind!"
    call angela_give_female from _call_angela_give_female_1
    return

label angela_give_valentine_female:
    angela.say "Thanks for being my valentine, [hero.name]."
    angela.say "And here's a little token of my appreciation too!"
    bree.say "A valentine's gift?"
    bree.say "Oh, Angela - that's so romantic!"
    $ hero.gain_item("valentine_chocolates")
    return


label angela_gift_collar_female:
    if angela.sub >= 90:
        "Angela seems to enjoy the gift."
        $ angela.love += 5
        $ angela.set_sex_slave()
    else:
        "Angela seems to dislike the gift."
        $ angela.love -= 20
        $ angela.sub -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
