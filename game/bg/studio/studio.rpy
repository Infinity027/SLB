init python:
    Room(**{
    "name": "studio",
    "hours": (18, 23),
    "conditions": [
        IsDayOfWeek("35"),
        IsHour(18, 23),
        'not Room.find("studio").hidden',
        HeroTarget(
            Not(OnDate()),
            ),
        ],
    "display_name": "Recording Studio",
    "exits": ["map"],
    "music": "music/TeknoAXE/simple_metal.ogg",
    "valid": False,
    "outfit": "casual",
    })

    Activity(**{
    "name": "practice_band",
    "duration": 2,
    "rooms": "studio",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 1),
            MinStat("fun", 0),
            MinFlag("band", 2),
            ),
        PersonTarget("anna",
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget("kleio",
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities(
            "battle_of_the_bands_round_one",
            "battle_of_the_bands_round_two",
            ),
        ],
    "icon": "guitar",
    "fun": 2,
    "display_name": "Practice",
    "label": "practice_band",
    "once_day": True,
    })

    Activity(**{
    "name": "gig",
    "duration": 2,
    "rooms": "studio",
    "conditions": [
        IsDone("battle_of_the_bands_round_two"),
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 1),
            MinStat("fun", 0),
            MinFlag("band", 2),
            IsFlag("bobWon", True),
            MinFlag("bandpractice", 10),
            ),
        PersonTarget("anna",
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget("kleio",
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities(
            "battle_of_the_bands_round_one",
            "battle_of_the_bands_round_two",
            ),
        ],
    "icon": "gig",
    "fun": 2,
    "display_name": "Play a gig",
    "label": "gig",
    "once_week": True,
    })

    Event(**{
    "name": "hide_studio",
    "label": "hide_studio",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            ),
        Or(
            Or(
                PersonTarget(anna,
                    IsGone(),
                    ),
                PersonTarget(kleio,
                    IsGone(),
                    ),
                ),
            And(
                HeroTarget(
                    IsFlag("performance"),
                    ),
                IsDone("kleio_and_anna"),
                ),
            ),
        ],
    "do_once": True,
    })

label hide_studio:
    $ Room.find("studio").hide()
    return

label practice_band:
    $ sasha.flags.schedule = "studio"
    "We practice together."

    if not game.flags.nextgig and "first_gig" not in DONE:
        $ game.flags.nextgig = TemporaryFlag(game.days_played + 41, 41, "gig_ready")


    if game.flags.bandpractice < 100:
        $ game.flags.bandpractice += 10


    if Person.is_not_hidden("kleio") and kleio.lesbian > 11 and hero.charm >= 50:
        $ kleio.lesbian -= 1
    if Person.is_not_hidden("anna") and anna.lesbian > 11 and hero.knowledge >= 50:
        $ anna.lesbian -= 1
    if sasha.lesbian > 11 and hero.fitness >= 50:
        $ sasha.lesbian -= 1
    if Person.is_not_hidden("kleio") and kleio.love < 50 and hero.charm >= 25:
        $ kleio.love += 1
    if Person.is_not_hidden("anna") and anna.love < 50 and hero.knowledge >= 25:
        $ anna.love += 1
    if sasha.love < 50 and hero.fitness >= 25:
        $ sasha.love += 1
    return

label gig_ready:
    $ game.flags.gigready = True
    return

label gig:

    $ band_members = [anna, kleio, sasha]
    if Harem.find_by_name("band"):
        $ band_members = Harem.find_by_name("band").active_members_objects
    $ renpy.random.shuffle(band_members)


    $ gig_outfit = ""
    menu:
        "Play at the pub":
            $ gig_location = "pub"
            $ gig_outfit = " casual"
            $ gig_mult = 1
        "Play at the nightclub" if game.flags.band_reputation >= 50 and game.flags.bandpractice >= 50:
            $ gig_location = "nightclub"
            $ gig_outfit = " date"
            $ gig_mult = 1.25
        "Play at the thunderdome" if game.flags.band_reputation >= 100 and game.flags.bandpractice >= 100:
            $ gig_location = "concert"
            $ gig_outfit = " date"
            $ gig_mult = 1.5


    if Harem.together(anna, kleio, sasha, name="band") and all([g.flags.agree_concert_naked for g in band_members]):
        menu:
            "Play dressed":
                pass
            "Play naked":
                $ gig_outfit = " naked"
                $ gig_mult += 0.25
                $ game.flags.naked_gig = True


    stop music
    scene bg black
    show expression f"bg {gig_location}"
    with fade
    if game.flags.band_reputation < 100:
        $ renpy.say("", f"We decided to play{gig_outfit if gig_outfit == ' naked' else ''} at the {gig_location if not gig_location == 'concert' else 'Thunderdome'} to earn some money and grew up our reputation.")
    else:
        $ renpy.say("", f"We decided to play{gig_outfit if gig_outfit == ' naked' else ''} at the {gig_location if not gig_location == 'concert' else 'Thunderdome'} to earn some money.")
    if "naked" in gig_outfit and renpy.has_label("naked_gig"):
        call naked_gig (gig_location) from _call_naked_gig
    else:
        play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
        show expression f"concert {'stage' if gig_location in ['nightclub', 'concert'] else 'pub'} {' '.join([g.id for g in band_members])}{gig_outfit}"
        with fade
        pause 1
        python:
            for g in band_members+[mike]:
                renpy.scene()
                renpy.show(f"concert solo {'stage' if gig_location in ['nightclub', 'concert'] else 'pub'} {g.id}{gig_outfit}")
                renpy.with_statement(dissolve)
                renpy.pause(1)
    scene bg studio with Fade(0.75, 1, 0.75)


    $ band_love = sum([g.love for g in band_members])
    $ money_produced = int((100 * (game.flags.bandpractice // 10) + band_love) * gig_mult)
    "We earned [money_produced]{image=gui/icons/icon_money.png} with our gig!"
    $ hero_share = int(money_produced * (1 / (len(band_members)+1)))
    $ hero.money += hero_share
    "I take my share, which is about [hero_share]{image=gui/icons/icon_money.png}."


    if game.flags.band_reputation < 100:
        $ reputation_gained = int(max(1, (game.flags.bandpractice * gig_mult // 10) // 1.5))
        $ game.flags.band_reputation = min(game.flags.band_reputation + reputation_gained, 100)
    $ game.flags.bandpractice = 0
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
