init python:
    Activity(**{
    "name": "ceo_command",
    "display_name": "Manage Office",
    "label": "manage_office",
    "duration": 0,
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice"),
            ),
        Or(
            And(
                PersonTarget("aletta",
                    Not(IsHidden()),
                    MinStat("sub", 50),
                    ),
                HeroTarget(
                    IsFlag("isceo")
                    ),
                ),
            And(
                PersonTarget("audrey",
                    Not(IsHidden()),
                    MinStat("sub", 50),
                    ),
                HeroTarget(
                    IsFlag("isceo")
                    ),
                ),
            And(
                PersonTarget("cassidy",
                    Not(IsHidden()),
                    IsFlag("status", ("pet", "sex slave")),
                    ),
                ),
            And(
                PersonTarget("lavish",
                    Not(IsHidden()),
                    MinStat("sub", 50),
                    ),
                HeroTarget(
                    IsFlag("isceo")
                    ),
                ),
            And(
                PersonTarget("shiori",
                    Not(IsHidden()),
                    MinStat("sub", 50),
                    ),
                HeroTarget(
                    IsFlag("isceo")
                    ),
                ),
            )
        ],
    "icon": "command",
    })

label manage_office:
    $ shuffle_choices = False
    menu:
        "Aletta" if Person.is_not_hidden("aletta") and game.flags.isceo and aletta.sub >= 50:
            menu:
                "Aletta should wear her sexy uniform" if aletta.sub >= 50 and aletta.flags.sexywork == False and aletta.flags.naked == False:
                    $ aletta.flags.sexywork = True
                "Aletta should not wear her sexy uniform anymore" if aletta.flags.sexywork == True and aletta.flags.naked == False:
                    $ aletta.flags.sexywork = False
                "Aletta should remove her top at work" if not aletta.flags.topless and aletta.sub >= 80:
                    $ aletta.flags.naked = False
                    $ aletta.flags.bottomless = False
                    $ aletta.flags.topless = True
                "Aletta should put her top back" if aletta.flags.topless:
                    $ aletta.flags.topless = False
                "Aletta should remove her bottoms at work" if not aletta.flags.bottomless and aletta.sub >= 85:
                    $ aletta.flags.naked = False
                    $ aletta.flags.bottomless = True
                    $ aletta.flags.topless = False
                "Aletta should put her bottom back on" if aletta.flags.bottomless:
                    $ aletta.flags.bottomless = False
                "Aletta should remove her uniform at work" if not aletta.flags.naked and aletta.sub >= 90:
                    $ aletta.flags.naked = True
                    $ aletta.flags.bottomless = False
                    $ aletta.flags.topless = False
                "Aletta should put her uniform back" if aletta.flags.naked:
                    $ aletta.flags.naked = False
                "Back":
                    jump manage_office
        "Audrey" if Person.is_not_hidden("audrey") and game.flags.isceo and audrey.sub >= 50:
            menu:
                "Audrey should wear her sexy uniform" if audrey.sub >= 50 and audrey.flags.sexywork == False and audrey.flags.naked == False:
                    $ audrey.flags.sexywork = True
                "Audrey should not wear her sexy uniform anymore" if audrey.flags.sexywork == True and audrey.flags.naked == False:
                    $ audrey.flags.sexywork = False
                "Audrey should remove her top at work" if not audrey.flags.topless and audrey.sub >= 80:
                    $ audrey.flags.naked = False
                    $ audrey.flags.bottomless = False
                    $ audrey.flags.topless = True
                "Audrey should put her top back" if audrey.flags.topless:
                    $ audrey.flags.topless = False
                "Audrey should remove her bottoms at work" if not audrey.flags.bottomless and audrey.sub >= 85:
                    $ audrey.flags.naked = False
                    $ audrey.flags.bottomless = True
                    $ audrey.flags.topless = False
                "Audrey should put her bottom back on" if audrey.flags.bottomless:
                    $ audrey.flags.bottomless = False
                "Audrey should remove her uniform at work" if not audrey.flags.naked and audrey.sub >= 90:
                    $ audrey.flags.naked = True
                    $ audrey.flags.bottomless = False
                    $ audrey.flags.topless = False
                "Audrey should put her uniform back" if audrey.flags.naked:
                    $ audrey.flags.naked = False
                "Back":
                    jump manage_office
        "Cassidy" if Person.is_not_hidden("cassidy") and (cassidy.status in ["pet", "sex slave"] or (cassidy.status == "girlfriend" and cassidy.sub >= 80)):
            menu:
                "Cassidy should remove her top" if not cassidy.flags.topless and (cassidy.status in ["pet", "sex slave"] or (cassidy.status == "girlfriend" and cassidy.sub >= 80)):
                    $ cassidy.flags.naked = False
                    $ cassidy.flags.bottomless = False
                    $ cassidy.flags.topless = True
                "Cassidy should put her top back" if cassidy.flags.topless:
                    $ cassidy.flags.topless = False
                "Cassidy should remove her bottoms" if not cassidy.flags.bottomless and (cassidy.status in ["pet", "sex slave"] or (cassidy.status == "girlfriend" and cassidy.sub >= 85)):
                    $ cassidy.flags.naked = False
                    $ cassidy.flags.bottomless = True
                    $ cassidy.flags.topless = False
                "Cassidy should put her bottom back on" if cassidy.flags.bottomless:
                    $ cassidy.flags.bottomless = False
                "Cassidy should remove her outfit" if not cassidy.flags.naked and (cassidy.status in ["pet", "sex slave"] or (cassidy.status == "girlfriend" and cassidy.sub >= 90)):
                    $ cassidy.flags.naked = True
                    $ cassidy.flags.bottomless = False
                    $ cassidy.flags.topless = False
                "Cassidy should put her outfit back" if cassidy.flags.naked:
                    $ cassidy.flags.naked = False
                "Back":
                    jump manage_office
        "Lavish" if Person.is_not_hidden("lavish") and game.flags.isceo and lavish.sub >= 50:
            menu:
                "Lavish should wear her sexy uniform" if lavish.sub >= 50 and lavish.flags.sexywork == False and lavish.flags.naked == False:
                    $ lavish.flags.sexywork = True
                "Lavish should not wear her sexy uniform anymore" if lavish.flags.sexywork == True and lavish.flags.naked == False:
                    $ lavish.flags.sexywork = False
                "Lavish should remove her top at work" if not lavish.flags.topless and lavish.sub >= 80:
                    $ lavish.flags.naked = False
                    $ lavish.flags.bottomless = False
                    $ lavish.flags.topless = True
                "Lavish should put her top back" if lavish.flags.topless:
                    $ lavish.flags.topless = False
                "Lavish should remove her bottoms at work" if not lavish.flags.bottomless and lavish.sub >= 85:
                    $ lavish.flags.naked = False
                    $ lavish.flags.bottomless = True
                    $ lavish.flags.topless = False
                "Lavish should put her bottom back on" if lavish.flags.bottomless:
                    $ lavish.flags.bottomless = False
                "Lavish should remove her uniform at work" if not lavish.flags.naked and lavish.sub >= 90:
                    $ lavish.flags.naked = True
                    $ lavish.flags.bottomless = False
                    $ lavish.flags.topless = False
                "Lavish should put her uniform back" if lavish.flags.naked:
                    $ lavish.flags.naked = False
                "Back":
                    jump manage_office
        "Shiori" if Person.is_not_hidden("shiori") and game.flags.isceo and shiori.sub >= 50:
            menu:
                "Shiori should wear her sexy uniform" if shiori.sub >= 50 and shiori.flags.sexywork == False and shiori.flags.naked == False:
                    $ shiori.flags.sexywork = True
                "Shiori should not wear her sexy uniform anymore" if shiori.flags.sexywork == True and shiori.flags.naked == False:
                    $ shiori.flags.sexywork = False
                "Shiori should remove her top at work" if not shiori.flags.topless and shiori.sub >= 80:
                    $ shiori.flags.naked = False
                    $ shiori.flags.bottomless = False
                    $ shiori.flags.topless = True
                "Shiori should put her top back" if shiori.flags.topless:
                    $ shiori.flags.topless = False
                "Shiori should remove her bottoms at work" if not shiori.flags.bottomless and shiori.sub >= 85:
                    $ shiori.flags.naked = False
                    $ shiori.flags.bottomless = True
                    $ shiori.flags.topless = False
                "Shiori should put her bottom back on" if shiori.flags.bottomless:
                    $ shiori.flags.bottomless = False
                "Shiori should remove her uniform at work" if not shiori.flags.naked and shiori.sub >= 90:
                    $ shiori.flags.naked = True
                    $ shiori.flags.bottomless = False
                    $ shiori.flags.topless = False
                "Shiori should put her uniform back" if shiori.flags.naked:
                    $ shiori.flags.naked = False
                "Back":
                    jump manage_office
        "Cancel":
            $ hero.cancel_activity()
    $ shuffle_choices = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
