init python:
    InteractActivity(**{
    "name": "test_dna",
    "display_name": "Test his DNA",
    "label": "dna_test",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            IsGender("male")
            ),
        HeroTarget(
            IsGender("female"),
            IsFlag("foundpreg")
            ),
        InInventory("dna_test"),
        ],
    "once_day": "ACTIVE",
    "icon": "dna",
    })

label dna_test:
    "I discreetly test [active_girl.name]'s DNA."
    $ hero.lose_item("dna_test")
    if active_girl.id == hero.flags.pregnancy_father:
        "[active_girl.name] is the father of my child..."
    else:
        "[active_girl.name] is not the father of my child..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
