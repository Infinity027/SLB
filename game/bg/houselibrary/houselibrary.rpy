init python:
    Room(**{
    "name": "houselibrary",
    "exits": ["secondfloor", "housemap"],
    "display_name": "Reading room",
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
        "name": "read",
        "label": "readhouselibrary",
        "knowledge": 0.5,
        "rooms": "houselibrary",
        "conditions": [
            HeroTarget(
                MinStat("energy", 5),
                MinStat("hunger", 5),
                MinStat("grooming", 5),
                MinStat("fun", 5),
                MaxStat("knowledge", 25),
                ),
            ],
        "icon": "study",
        "display_name": "Read",
        "once_day": True,
        })

label readhouselibrary:
    show chibi book
    $ renpy.say("", randchoice([
        "I sit down with a good book and start reading.",
        "I learn something new. That was worth it.",
        "It was an interesting read. A nice way to spend time.",
        "Some people collect friends. I collect first editions.",
        "A good book hits harder than leg day.",
        "Ho! That a dystopian novels... This is so 1984.",
        "How some people doesn’t like lord of the ring? There doesn’t know what they're Tolkien about.",
    ]))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
