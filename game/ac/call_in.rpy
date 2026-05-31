init python:
    Activity(**{
    "name": "call_in",
    "display_name": "Call someone in",
    "label": "call_in",
    "duration": 0,
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        Or(
            PersonTarget("aletta",
                Not(IsHidden()),
                Not(IsPresent()),
                HasRoomTag("work"),
                MinStat("sub", 50),
                ),
            PersonTarget("audrey",
                Not(IsHidden()),
                Not(IsPresent()),
                HasRoomTag("work"),
                MinStat("sub", 30),
                ),
            PersonTarget("shiori",
                Not(IsHidden()),
                Not(IsPresent()),
                HasRoomTag("work"),
                MinStat("sub", 40),
                ),
            PersonTarget("lavish",
                Not(IsHidden()),
                Not(IsPresent()),
                HasRoomTag("work"),
                MinStat("sub", 40),
                ),
            ),
        ],
    "icon": "callin",
    })

label call_in:
    menu:
        "Aletta" if Person.is_not_hidden("aletta") and Room.has_tag(aletta.room, "work") and aletta.room != game.room and aletta.sub >= 50 and game.flags.isceo:
            call aletta_call_in from _call_aletta_call_in
            $ aletta.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Audrey" if Person.is_not_hidden("audrey") and Room.has_tag(audrey.room, "work") and audrey.room != game.room and audrey.sub >= 30:
            call audrey_call_in from _call_audrey_call_in
            $ audrey.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Shiori" if Person.is_not_hidden("shiori") and Room.has_tag(shiori.room, "work") and shiori.room != game.room and shiori.sub >= 40:
            call shiori_call_in from _call_shiori_call_in
            $ shiori.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Lavish" if Person.is_not_hidden("lavish") and Room.has_tag(lavish.room, "work") and lavish.room != game.room and lavish.sub >= 40:
            call lavish_call_in from _call_lavish_call_in
            $ lavish.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Nobody":
            pass
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
