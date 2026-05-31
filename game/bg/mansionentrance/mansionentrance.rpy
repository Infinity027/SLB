init python:
    class MansionEntrancePicker(object):
        def __call__(self, attr):
            
            if (game.calendar.is_today("winter", 25) and game.hour >= 8 or
            game.calendar.is_today("winter", 26) and game.hour < 6):
                attr.add("christmas_decor")
            else:
                attr.add(game.calendar.season_name)
            
            return attr

init 1:
    layeredimage bg mansionentrance:
        attribute_function Pickers([DayNightPicker, MansionEntrancePicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "mansionentrance",
    "exits": ["map", "mansion"],
    "conditions":[
        IsDone("cherie_event_01"),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        Or(
            InInventory("dwayne_corpse"),
            InInventory("aletta_gun"),
            PersonTarget("cherie",
                HasRoomTag("mansion"),
                Not(IsActivity("sleep")),
                )
            ),
        ],
    "display_name": "Entrance",
    "outfit": "casual",
    "tags": ["mansion"],
    })
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
