init python:
    Activity(**{
    "name": "call_in_home",
    "display_name": "Call someone in",
    "label": "call_in_home",
    "duration": 0,
    "conditions": [
        HeroTarget(
            HasRoomTag("home"),
            Not(OnDate()),
            ),
        Or(
            PersonTarget("bree",
                Not(IsPresent()),
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                MinStat("sub", 50),
                ),
            PersonTarget("sasha",
                Not(IsPresent()),
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                MinStat("sub", 50),
                ),
            PersonTarget("minami",
                Not(IsPresent()),
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                MinStat("sub", 50),
                ),
            PersonTarget("samantha",
                Not(IsPresent()),
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                MinStat("sub", 50),
                ),
            PersonTarget("lexi",
                Not(IsPresent()),
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                MinStat("sub", 50),
                ),
            ),
        ],
    "icon": "callin",
    })

label call_in_home:
    menu:
        "Sasha" if Person.is_not_hidden("sasha") and Room.has_tag(sasha.room, "home") and sasha.room != game.room and sasha.sub >= 50 and sasha.activity_name != "sleep":
            mike.say "Sasha can you come here?"
            show sasha talk
            sasha.say "Yes [hero.name]?"
            $ sasha.flags.forceLocation = (game.days_played, game.hour, game.room)
        "[bree.name]" if Person.is_not_hidden("bree") and Room.has_tag(bree.room, "home") and bree.room != game.room and bree.sub >= 50 and bree.activity_name != "sleep":
            mike.say "[bree.name] can you come here?"
            show bree talk
            bree.say "Yes [hero.name]?"
            $ bree.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Minami" if Person.is_not_hidden("minami") and Room.has_tag(minami.room, "home") and minami.room != game.room and minami.sub >= 50 and minami.activity_name != "sleep":
            mike.say "Minami can you come here?"
            show minami talk
            minami.say "Yes big bro?"
            $ minami.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Samantha" if Person.is_not_hidden("samantha") and Room.has_tag(samantha.room, "home") and samantha.room != game.room and samantha.sub >= 50 and samantha.activity_name != "sleep":
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake can you come here?"
            else:
                mike.say "Samantha can you come here?"
            show samantha talk
            samantha.say "Yes [hero.name]?"
            $ samantha.flags.forceLocation = (game.days_played, game.hour, game.room)
        "Nobody":
            pass
    return
return