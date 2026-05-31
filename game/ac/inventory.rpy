init python:
    Activity(**{
    "name": "inventory",
    "duration": 0,
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        "hero.has_items",
        ],
    "icon": "inventory",
    "display_name": "Open inventory",
    "label": "inventory",
    "order": 1,
    })

label inventory:
    while True:
        $ result = renpy.call_screen("inventory")
        if result == "exit":
            return
        if isinstance(result, Equip):
            $ result.equip()
        elif isinstance(result, Consumable):
            $ result.use()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
