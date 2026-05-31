init python:
    Room(**{
    "name": "alettaoffice",
    "display_name": "Aletta's Office",
    "exits": ["map", "office", "personal","ceo", "breakroom"],
    "hours": (8, 20),
    "conditions": [
        IsDone("aletta_event_01"),
        IsDayOfWeek("123456"),
        IsHour(8, 20),
        HeroTarget(
            IsGender("male"),
            ),
        ],
    "music": "music/roa_music/fly_high.ogg",
    "outfit": "work",
    "tags": ["work"],
    "valid": False,  
    })

    Activity(**{
    "name": "hack_computer",
    "duration": 0,  
    "display_name": "Hack Aletta's computer",
    "rooms": "alettaoffice",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99),
            ),
        PersonTarget("aletta",
            Not(IsPresent())
            ),
        ],
    "label": "hack_computer",
    "icon": "hack",
    "once_day": True,
    })

label hack_computer:
    show chibi computer
    $ cassidy.set_flag("hackattempts", 1, mod="+")
    call investigation_points (max(hero.knowledge // 7, 5)) from _call_investigation_points_1

    $ game.pass_time(1)
    if game.flags.workinvestigation >= 100:
        "I put everything I've already learned together, and go through the accounting details three times, just to verify."
        "Once I eliminate the false trails, there is no doubt. The false transactions were created by Dwayne himself."
        "The CEO of this company is embezzling money, and I'm the fall guy."
        "And now I have proof."
        return

    if cassidy.flags.hackattempts == 1:
        "I sit down at Aletta's computer and log in. I honestly don't know what to look for at first, so I start digging through all the folders regarding accounting."
        "I spend about an hour looking through the accounts, but there's so much there that I don't think I really found anything useful."
        "I'll have to try again tomorrow."
    elif cassidy.flags.hackattempts == 2:
        "I pick up where I left off and look more deeply into the system, going over my own expense accounts for the last several years."
        "It's been awhile, and I should remember all these numbers, but I don't. I flag a few transactions and take some notes on which ones to check tomorrow."
    elif cassidy.flags.hackattempts == 3:
        "I spend an hour looking through the transactions I had flagged. While I'm sure I didn't make them, I still can't tell where they came from. I'll check again tomorrow."
    elif cassidy.flags.hackattempts == 4:
        "After spending another hour checking the transactions, the trail leads to a set of external accounts from a corporate subsidiary. I'll need to research that tomorrow."
    elif cassidy.flags.hackattempts == 5:
        "It turns out the company I found out about last time was set up out of Dwayne's office, but the records are purposefully vague about this. Could Dwayne be the real thief? Alas, I have no proof of this."
    elif cassidy.flags.hackattempts == 6:
        "I dig more into the corporate subsidiary, but I keep hitting dead-ends on what look like false trails of offshore accounts and companies with no employees."
    else:
        "Just when I think I'm getting somewhere, I end up out of clues. It sure looks like these transactions were inserted into my books by someone."
        "But I can't tell who, and the only proof of this is my recollection of them. Nobody's going to buy that."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
