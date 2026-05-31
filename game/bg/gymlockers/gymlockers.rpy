init python:
    Room(**{
    "name": "gymlockers",
    "hours": (6, 22),
    "conditions": [
        IsHour(6, 22),
        InInventory("sport_clothes"),
        ],
    "display_name": "Gym lockers",
    "exits": ["map", "gymreception", "gym", "gymmachine", "mma"],
    "music": "music/roa_music/higher.ogg",
    "outfit": "sport",
    "tags": ["gym"],
    })

    Activity(**{
    "name": "take_a_shower_gym",
    "rooms": "gymlockers",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("grooming")),
            IsFlag("dirty"),
            IsFlag("gymmember")
            ),
        ],
    "grooming": 8,
    "display_name": "Take a shower",
    "label": "take_a_shower_gym",
    "icon": "shower",
    })

label take_a_shower_gym:
    play sound shower
    show chibi shower
    $ hero.flags.dirty = TemporaryFlag(False, "day")
    "I take a shower..."
    stop sound
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
