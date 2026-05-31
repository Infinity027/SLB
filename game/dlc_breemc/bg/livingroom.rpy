init python:
    Activity(**{
    "name": "livingroom_masturbate_female",
    "fun": 1,
    "duration": 0,
    "max_girls": 0,
    "label": "livingroom_masturbate_female",
    "icon": "masturbate",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MaxStat("fun", 3),
            MaxStat("morality", -25),
            ),
        ],
    "display_name": "Masturbate",
    "once_day": True,
    })

    Activity(**{
    "name": "play_videogames_with_mike",
    "fun": 3,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("fun", 0)
            ),
        InInventory("zbox_360"),
        PersonTarget(mike,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsActivity("tv"))
            ),
        ],
    "display_name": "Play video games with [mike.name]",
    "label": "play_videogames_with_mike",
    "icon": "videogame",
    })

label livingroom_masturbate_female:
    "I decide to have a little fun by myself."
    "Mmmmmh, that feels good."
    if hero.morality >= -49:
        $ hero.morality -= 1
    return



label play_videogames_with_mike:
    show bree console 3
    "I play some video games with [mike.name]."
    $ hero.gain_skill("video_games", 1)
    $ mike.love += 1
    if hero.has_skill("video_games"):
        show bree console 2
        $ mike.sub += 1
        "And I win!"
    else:
        show bree console 1
        $ mike.sub -= 1
        "And I lose..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
