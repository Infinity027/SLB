init python:
    class LivingroomPicker(object):
        def __call__(self, attr):
            
            if (game.calendar.is_today("fall", 31) and game.hour >= 8 or
            game.calendar.is_today("winter", 1) and game.hour < 6):
                attr.add("halloween_decor")
            elif (game.calendar.is_today("winter", 25) and game.hour >= 8 or
            game.calendar.is_today("winter", 26) and game.hour < 6):
                attr.add("christmas_decor")
            else:
                attr.add(game.calendar.season_name)
            
            if Harem.find('lexi', name='home'):
                attr.add("blanket")
                if lexi.room == "livingroom" and lexi.activity["activity"] == "sleep":
                    attr.add('lexi_sleep')
            
            return attr

init 1:
    layeredimage bg livingroom:
        attribute_function MultiPickers([DayNightPicker, LivingroomPicker], append_npc_from_attributes=True)
        attribute blanket null
        attribute lexi null
        attribute lexi_sleep null
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always "snow"
        group season_fg auto variant "day" if_any "day"
        group season_fg auto variant "night" if_any "night"
        group blanket if_any "blanket":
            attribute day "bg_livingroom_blanket_day"
            attribute night "bg_livingroom_blanket_night"
        group lexi if_any "lexi_sleep":
            attribute day "bg_livingroom_lexi_day"
            attribute night "bg_livingroom_lexi_night"

init python:
    Room(**{
    "name": "livingroom",
    "display_name": "Living Room",
    "exits": ["firstfloorbathroom", "secondfloor", "house","kitchen","pool", "bedroom1", "bedroom6", "housemap"],
    "music": house_music(),
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
    "name": "watch_tv",
    "label": "watch_tv",
    "fun": 1.5,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        InvalidActivities(
            "watch_tv_with_everyone_male",
            "watch_tv_with_everyone_female",
            "watch_tv_with_mike",
            "watch_tv_with_sasha",
            "watch_tv_with_bree",
            "watch_tv_with_minami",
            ),
        ],
    "display_name": "Watch TV",
    "icon": "tv",
    })

    Activity(**{
    "name": "play_videogames",
    "fun": 3,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        InInventory("zbox_360"),
        PersonTarget(bree,
            Or(
                Not(IsActivity("tv")),
                IsHidden(),
                IsGone(),
                ),
            ),
        PersonTarget(sasha,
            Or(
                Not(IsActivity("tv")),
                IsHidden(),
                IsGone(),
                ),
            ),
        InvalidActivities("play_videogames_with_bree"),
        ],
    "display_name": "Play video games",
    "label": "play_videogames",
    "icon": "videogame",
    })

    Activity(**{
    "name": "play_videogames_with_bree",
    "fun": 3,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        InInventory("zbox_360"),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Or(
                Not(IsActivity("tv")),
                IsHidden(),
                IsGone(),
                ),
            ),
        Or(
            PersonTarget("lexi",
                IsPresent(),
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                ),
            PersonTarget("lexi",
                Not(IsRoom("livingroom")),
                )
            ),
        ],
    "display_name": "Play video games with [bree.name]",
    "label": "play_videogames_with_bree",
    "icon": "videogame",
    })

    Activity(**{
    "name": "watch_tv_with_everyone_male",
    "fun": 3,
    "duration": 2,
    "icon": "tv",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        ],
    "min_girls": 2,
    "display_name": "Watch TV with everyone",
    "label": "watch_tv_with_everyone_male",
    })

    Activity(**{
    "name": "clean_the_livingroom",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "display_name": "Vacuum",
    "icon": "vacuum",
    "label": "clean_the_livingroom",
    "every_two_days": True,
    })

    Event(**{
    "name": "sasha_livingroom_bree",
    "fun": 3,
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsRoom("livingroom"),
            Not(OnDate()),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "chances": 5,
    "label": "sasha_livingroom_bree",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "wish_had_console",
    "label": "wish_had_console",
    "conditions": [
        HeroTarget(IsRoom("livingroom")),
        Not(InInventory("zbox_360")),
        ],
    "chances": 20,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "polygamy_news_1",
    "label": "polygamy_news",
    "conditions": [
        IsActiveHarem('band'),
        IsHour(20, 21),
        HeroTarget(
            IsActivity("watch_tv"),
            IsRoom("livingroom"),
            IsFlag("polygamy", False),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "polygamy_news_2",
    "label": "polygamy_news",
    "conditions": [
        IsActiveHarem('home'),
        IsHour(20, 21),
        HeroTarget(
            IsActivity("watch_tv"),
            IsRoom("livingroom"),
            IsFlag("polygamy", False),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Activity(**{
    "name": "masturbate_male",
    "fun": 1,
    "duration": 0,
    "max_girls": 0,
    "label": "livingroom_masturbate_male",
    "icon": "masturbate",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            MaxStat("fun", 3),
            Not(OnDate()),
            ),
        ],
    "display_name": "Masturbate",
    "once_day": True,
    })

label watch_tv:
    show chibi tv
    $ narrator(randchoice([
            "I watch a very strange show... An old man was traveling through time in a phone booth.",
            "I hate reality show, they show you how dumb people can be and they don't shoot them at the end.",
            "Again... A superhero movie, I don't know what's so good about men in tights.",
            "News are so depressing... Let's watch Planet Express, I love that show.",
            ]))
    return

label livingroom_masturbate_male:
    scene mc_must1
    "I decide to have a little fun by myself."
    scene expression make_anim(mc_must, 0.15, loop=True)
    scene mc_must2 with vpunch
    "Mmmmmh, that feels good."
    return

label wish_had_console:
    "I should buy myself a gaming system, watching TV is boring."
    show screen message(title="Buy a console!",what="You need a {b}Zbox 360{/b} to be able to play video games at home.")
    pause
    hide screen message
    return

label play_videogames:
    show chibi console
    "I play some video games."
    $ hero.gain_skill("video_games", 1)
    $ hero.flags.video_games_played += 1
    return

label play_videogames_with_bree:
    show bree console 3
    "I play some video games with [bree.name]."
    $ hero.gain_skill("video_games", 1)
    $ bree.love += 1
    if hero.has_skill("video_games"):
        show bree console 1
        $ bree.sub += 1
        $ bree.flags.lost_video_games += 1
        "And I win!"
        if bree.flags.lost_video_games >= 5 and bree.love >= 160 and bree.sub >= 25 and bree.sexperience >= 3:
            call bree_zbox_penalty from _call_bree_zbox_penalty
    else:
        show bree console 2
        $ bree.sub -= 1
        "And I lose..."
    $ hero.flags.video_games_played += 1
    return

label clean_the_livingroom:
    show chibi vacuum
    play sound vacuum
    $ game.set_flag("chores",25,"week","+")
    python:
        if game.flags.chores > 100:
            for p in Person.get_housemates():
                p.love += 1
    "I clean the living room."
    stop sound
    return

label sasha_livingroom_bree:
    $ result = randint(1, 2)
    if result == 1:
        show sasha angry at left
        show bree angry at right
        "Sasha and [bree.name] are arguing about something."
        $ response = renpy.display_menu([("Take [bree.name]'s side", 1), ("Take Sasha's side", 2), ("Stay neutral", 3)])
        if response == 1:
            show bree happy
            $ bree.love += 2
            $ sasha.love -= 1
        elif response == 2:
            show sasha happy
            $ sasha.love += 2
            $ bree.love -= 1
        elif response == 3:
            show bree normal
            show sasha normal
            $ bree.love += 1
            $ sasha.love += 1
        "After my intervention they stop arguing."
    elif result == 2:
        show sasha at left
        show bree at right
        "Sasha and [bree.name] are chatting on the couch."
        "I join them for a while."
        $ bree.love += 1
        $ sasha.love += 1
    return

label polygamy_news:
    $ game.flags.polygamy = True
    "My evening routine is embarrassingly simple: get home, collapse on the sofa, let the TV wash over me."
    "Most nights I couldn't tell you what I'm watching. It's just noise."
    "But certain words have a way of cutting right through — and tonight, one of them does."
    "The word is 'polygamy'."
    "I sit up and grab the remote, rewinding just enough to catch the start of the story."
    "Shady guy" "...saw the second reading of the controversial 'Marriage and Social Institution Reform Bill' before the lower house."
    "Shady guy" "Dubbed the 'Bigamy Bill' by its critics, the bill was widely expected to be thrown out in today's session."
    "Right — I'd read a bit about this online. It was largely about equalising marriage and civil partnership rights regardless of orientation."
    "The polygamy clause was minor, almost buried. But the conservative right had latched onto it as their way in, nicknaming the whole thing the 'Bigamy Bill' to avoid looking anti-LGBTQ+."
    "Shady guy" "But in a shock move, it received the backing of formerly abstaining members and narrowly passed into law."
    "Shady guy" "Its opponents have cited this as proof of a wider conspiracy to undermine..."
    "The anchor kept talking, but I'd already stopped listening."
    "It had actually passed. Polygamy — legal."
    "I suppose most people would be thinking about the broader social implications right now."
    "But my mind went somewhere far more personal: if multi-person relationships were normalised, raising the idea with more than one person at once might no longer earn you an instant slap."
    return

label watch_tv_with_everyone_male:
    $ renpy.dynamic("people")
    $ people = []
    python:
        for g in Room.find(game.room).get_present_girls():
            people.append(g)
    call watch_tv_with (*people) from _call_watch_tv_with
    return

label bj3_porn:
    if renpy.has_label("home_harem_achievement_2"):
        call home_harem_achievement_2 from _call_home_harem_achievement_2
    $ game.flags.threebj = True
    "We watch porn..."
    "The excitation could be felt by anyone..."
    bree_sasha "Hey, [hero.name]."
    sasha.say "It's boring to just watch."
    bree.say "Soooo true."
    mike.say "And?"
    "I think about it a moment."
    sasha.say "Let's have some fun..."
    "Sasha's fingers hook over the straps of her bra then she slides the straps over her shoulders."
    bree.say "Relax, but not too much!"
    "[bree.name] says while shimmying out of her panties."
    "She playfully tosses them off with her foot."
    scene bg livingroom
    show bree naked at left
    show sasha naked at right
    "When I glance at them again, [bree.name] and Sasha stand on either side of the couch."
    "Both of my roommates have removed their clothes and are smiling down at me with their lust and intent."
    sasha.say "Hope you enjoy the view."
    bree.say "Now then!"
    bree.say "Let's get down to business shall we?"
    "The two nod at each other."
    "The two of them lean in over the couch, each of them giving me their fluttering bedroom eyes."
    "As they climb up onto the couch, Sasha on my left and [bree.name] on my right, the soft words whisper gently to my ears."
    "Soon, the two lay their warm bodies up against my own, pressed against my spread legs."
    "I reach up and hold onto both of them, sliding my own fingers over their smooth skin."
    hide bree
    hide sasha
    show couch fun bree sasha
    "Together, they wrap their fingers around my shaft, and roll their tongues out, licking up along my length."
    mike.say "O... oh wow..."
    "Again, they lick up my shaft, up over the glans and over the tip."
    "Their tongues touch, and they both stare up at me, a chuckle shared between the two of them before they wrap their lips around the head."
    "The two best roommates in the world make out with my cock in the middle of it all, their tongues dancing over my skin as their hands move in sync to jerk me off."
    "What did I do to deserve the greatest roommates in the world?"
    "I wonder this as the excitement of their actions tingles up through my body."
    show couch fun bree sasha cumshot
    "I can't hold back and, with a groan, I release, shooting up onto them."
    "Cum sprays up onto their faces, getting them nice and covered by my jizz."
    hide couch
    show couch fun bree sasha facial
    "The girls smile up at me, batting their half-lidded eyes up in my direction."
    sasha.say "Enjoy this view..."
    "Sasha takes a finger and slips a drop of my cum off of her face."
    "She hands it to [bree.name], who wraps her lips around my cock, moaning in delight at the taste."
    hide couch
    return

init python:

    Activity(**{
    "name": "watch_tv_with_everyone_female",
    "fun": 3,
    "duration": 2,
    "icon": "tv",
    "min_girls": 2,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 0),
            ),
        PersonTarget("mike",
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    "display_name": "Watch TV with everyone",
    "label": "watch_tv_with_everyone_female",
    })

    Activity(**{
    "name": "watch_tv_with_mike",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with [mike.name]",
    "max_girls": 1,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("fun", 0)),
        PersonTarget("mike",
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities(
            "watch_tv_with_everyone_female"),
        ],
    "label": "mike_tv",
    })

label watch_tv_with_everyone_female:
    call watch_tv_with (mike, sasha) from _call_watch_tv_with_1
    return


label mike_tv:
    call mike_greet from _call_mike_greet
    if hero.charm >= 40 - mike.love or mike.activity_name == "tv":
        call watch_tv_with (mike) from _call_watch_tv_with_6
    else:
        show mike
        mike.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide mike
    return
return