init python:
    Room(**{
    "name": "firstfloorbathroom",
    "display_name": "Bathroom",
    "exits": ["livingroom", "housemap"],
    "music": house_music(),
    "outfit": "underwear",
    "tags": ["home"],
    })


    Event(**{
    "name": "bathroom_broken",
    "label": "bathroom_broken",
    "conditions": [
        HeroTarget(
           Not(IsFlag("bathroomrepaired")),
           IsRoom("firstfloorbathroom"),
           ),
        ],
    "do_once": False,
    "once_day": False,
    })

label bathroom_broken:
    "This is the first floor bathroom but it's been broken for ages..."
    "I need 5000{image=gui/icons/icon_money.png} to get it fixed it."
    if hero.money >= 5000:
        menu:
            "Get it fixed":
                $ hero.money -= 5000
                $ game.flags.bathroomrepaired = True
            "Leave it":
                pass
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
