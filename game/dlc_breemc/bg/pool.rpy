init python:
    Activity(**{
    "name": "play_in_the_pool_with_everyone_female",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with everyone",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("female"),
            Not(OnDate()),
            ),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget("mike",
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        ],
    "once_day": True,
    "label": "play_in_the_pool_with_everyone_female",
    })

label play_in_the_pool_with_everyone_female:
    show sasha at left
    show mike at right
    "I play in the pool with Sasha and [mike.name]."
    $ mike.love += 1
    $ mike.flags.greeted = TemporaryFlag(True, 1)
    $ sasha.love += 1
    $ sasha.flags.greeted = TemporaryFlag(True, 1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
