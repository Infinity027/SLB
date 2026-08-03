init python:
    Room(**{
    "name": "mansion",
    "exits": ["map", "mansionentrance"],
    "conditions":[
        IsDone("cherie_event_01"),
        HeroTarget(
            Not(OnDate()),
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
    "display_name": "Mansion",
    "outfit": "casual",
    "tags": ["mansion"],
    })