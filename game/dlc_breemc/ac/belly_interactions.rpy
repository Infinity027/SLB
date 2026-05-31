init python:

    InteractActivity(**{
    "name": "belly_interactions_female",
    "display_name": "About my belly",
    "label": "ACTIVE_GIRL_belly_interaction_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinCounter("pregnant", 60),  
            HasStamina(),
            ),
        ActiveTarget(
            IsActive(),
            IsPresent(),
            MinStat("love", 120),
            Not(IsActivity("sleep")),
            ),
        ],
    "icon": "belly",
    "priority": 600,
    "do_once": False,
    "once_day": True,
    "duration": 0,
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
