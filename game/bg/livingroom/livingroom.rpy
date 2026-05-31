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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
            IsGender("male"),
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
    show couch fun masturbate
    pause 0.2
    show couch fun down
    pause 0.2
    show couch fun up
    pause 0.2
    show couch fun down
    pause 0.2
    show couch fun up
    "I decide to have a little fun by myself."
    show couch fun down
    pause 0.1
    show couch fun up
    pause 0.1
    show couch fun down
    pause 0.1
    show couch fun masturbate cumshot with vpunch
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
    if Person.is_not_hidden("lexi") and lexi.present and lexi.activity_name == 'sleep':
        call play_videogames_lexi_sleep from _call_play_videogames_lexi_sleep
    else:
        "I play some video games."
        $ hero.gain_skill("video_games", 1)
    $ hero.flags.video_games_played += 1
    return

label play_videogames_lexi_sleep:
    "I've been waiting for everyone to turn in for the night, listening out for their doors closing."
    "And as soon as I hear the last click, I'm out of my own door and headed for the living room."
    "It doesn't take me more than a few seconds to switch on the Zbox and grab the joypad."
    "I'll teach [bree.name] to beat my high-score and then spend the rest of the night rubbing my face in it!"
    "It's only when the TV comes to life too that I realise I've forgotten something."
    "When [bree.name] plays on the Zbox, she like to turn the volume up nice and loud!"
    "The noise sounds like an explosion in the otherwise silent house."
    "And it sends me scrambling for the remote to turn in down before I'm discovered."
    "But even as I hit the button, another sound lets me know it's too late!"
    scene bg livingroom
    show lexi underwear annoyed
    lexi.say "Gnurr..."
    lexi.say "Urgh..."
    lexi.say "What the..."
    "My head snaps around, seeking the source of the grunts and groans."
    "And that's when I see Lexi for the first time, still wrapped up in a nest of blankets."
    "Her hair is a crazy mess and she looks like she's been drooling in her sleep too."
    "Of course, how could I have forgotten?"
    "She's still sleeping on the couch after her trailer burnt down!"
    mike.say "Erm..."
    mike.say "Hey, Lex!"
    "Lexi wrinkles up her face as she stares at me with bleary eyes."
    "She rubs them with the back of her hand."
    "And I can tell that she's trying to make sense of what's going on."
    lexi.say "[hero.name]?"
    lexi.say "Did I oversleep?"
    lexi.say "Is it morning already?"
    "Well, this is kind of awkward..."
    mike.say "No, Lexi."
    mike.say "It's still a little earlier than that!"
    "Lexi sits up as her head begins to clear."
    "She glances at the time, and then seems to come fully awake."
    lexi.say "No kidding, [hero.name]!"
    lexi.say "What are you doing in here anyway?"
    lexi.say "I was trying to sleep!"
    "I have the TV on with the Zbox game on the screen."
    "And I'm sitting on the floor with the joypad in my hand."
    "Even if I deny it, Lexi can't help but see the truth!"
    mike.say "I...was trying to beat [bree.name]'s high-score."
    mike.say "And I kind of forgot that you were sleeping in here!"
    show lexi angry
    lexi.say "Wow, [hero.name], just wow."
    lexi.say "Way to make a girl feel wanted around here!"
    menu:
        "Apologize":
            "She's right - what in the hell am I doing here?"
            "After all that Lexi's been through recently too."
            "What kind of a friend am I being to her?"
            mike.say "I'm sorry, Lexi."
            mike.say "I should've remembered you were here."
            mike.say "Geez, I'm a bad friend to you!"
            "Lexi just stares at me for a minute in silence."
            "I can see from her body-language that she was ready for a fight."
            "But not for me to back down and offer her an apology."
            show lexi normal
            "She relaxes, shaking her head a little."
            lexi.say "Ah, forget about it, [hero.name]."
            lexi.say "I just get cranky when someone wakes me up, that's all!"
            lexi.say "And just for the record..."
            lexi.say "You're a real good friend to me."
            lexi.say "One of the best I've ever had!"
            "I see Lexi flush a little as she admits this."
            "And I look away too, touched by her honesty."
            mike.say "This...well, this can wait until tomorrow."
            mike.say "I think it's time we both called it a night, okay?"
            "Lexi nods and begins to settle down on the sofa again."
            "But before I reach the door, she catches my eye."
            show lexi wink
            lexi.say "Oh, and remember, [hero.name]..."
            lexi.say "There are better games to play down here in the middle of the night."
            lexi.say "It just depends who you're playing them with!"
            $ lexi.love += 1
        "Tell off":
            "I know that Lexi's probably woken up irritable."
            "And she can't help the mess that she's in right now."
            "But all the same, I feel my temper getting the better of me."
            "Where does she get off disrupting the my domestic bliss?"
            mike.say "You know you could try to sound a little grateful, Lexi."
            mike.say "I did take you in when you needed somewhere to stay."
            mike.say "So I woke you up - so what?"
            mike.say "Isn't it better than sleeping on the street?!?"
            lexi.say "What would you know about life on the streets, huh?"
            lexi.say "At least there I wouldn't have to deal with your crap!"
            "As if to underline her point, Lexi leaps up off the sofa."
            "She bundles the blankets up and looks this way and that."
            mike.say "Ah...where are you going, Lexi?"
            mike.say "It's not like there's anywhere else to sleep!"
            "At this, Lexi fixes me with a spiteful glare."
            lexi.say "Oh, I don't know, [hero.name]."
            lexi.say "I'm betting there's one bed that's empty right now."
            lexi.say "Seems you want to be here rather than asleep in it!"
            $ lexi.love -= 1
            hide lexi
            "And with that, she storms off, leaving me alone in the living room."
            "All I can do is sigh and shake my head."
            "Looks like I'm stuck sleeping on the sofa tonight."
            "So the least I can do is get on with beating [bree.name]'s high-score first..."
            $ hero.gain_skill("video_games", 1)
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
    if Person.is_not_hidden("lexi") and lexi.present and lexi.activity_name == 'sleep':
        call vacuum_lexi_sleep from _call_vacuum_lexi_sleep
    else:
        play sound vacuum
        $ game.set_flag("chores",25,"week","+")
        python:
            if game.flags.chores > 100:
                for p in Person.get_housemates():
                    p.love += 1
        "I clean the living room."
    stop sound
    return

label vacuum_lexi_sleep:
    $ renpy.sound.play("sd/vacuum.ogg", loop=True)
    "I know that I've left it a little too late to be running the vacuum-cleaner around the house."
    "But there's only the downstairs that needs to be done, and everyone else has already gone to bed."
    "That means I can get on with it and not have to worry about disturbing any of the others."
    "Plus there won't be ant witnesses should I need to cut corners as well!"
    "Everything goes according to plan until I reach the living room."
    "At first I just assume that what's a sofa is a messy pile of blankets."
    "One of the girls must have been using them to make a nest earlier in the day."
    "I just shrug and get on with the vacuuming, as cleaning it up isn't my problem."
    "But I'm not even a quarter of the way done when I hear a shout behind me."
    scene bg livingroom
    show lexi underwear annoyed
    lexi.say "HEY!"
    lexi.say "What the hell are you doing?!?"
    stop sound
    "I kill the power to the vacuum-cleaner and turn around."
    "And there, poking a bleary-eyed head out of the tangle of blankets, is Lexi."
    "Oh shit, now I remember."
    "She's still crashing on the sofa after her trailer burnt to the ground!"
    mike.say "Erm..."
    mike.say "Vacuuming, I guess."
    "Lexi shakes her head, trying to throw off the mugginess of sleep."
    "But I can see that she's less than elated to have been disturbed."
    lexi.say "Is that a thing around here, [hero.name]?"
    lexi.say "You wander into everyone's room with that thing?"
    lexi.say "Or don't I count?"
    mike.say "I...I guess I just forgot you were in here, Lexi."
    show lexi angry
    lexi.say "Urgh..."
    lexi.say "I can't handle this shit right now."
    lexi.say "I need my beauty sleep!"
    "I can't help looking at the dishevelled state of Lexi's hair as she says this."
    "She's also been drooling out of the corner of her mouth while she was sleeping."
    "And the temptation to agree with that last statement is almost too much to resist."
    "But as I really want to keep my balls attached to my body, I keep it to myself."
    menu:
        "Apologise":
            "What on earth am I thinking?"
            "Lexi's been through so much recently."
            "And her life wasn't a bed of roses before that either."
            "Now she's sleeping on my sofa, with only the clothes on her back!"
            "What kind of a friend am I?"
            mike.say "I'm sorry, Lexi."
            mike.say "I just forgot you were in here, that's all."
            mike.say "I'll finish up in the morning."
            show lexi normal
            "By now, Lexi's finally shaken off the drowsiness."
            "And she seems to have been mollified by my apology too."
            lexi.say "Oh...don't beat yourself up, [hero.name]."
            lexi.say "I guess this is pretty weird for the both of us!"
            lexi.say "But I am grateful that you let me stay here."
            mike.say "I know that, Lexi."
            mike.say "But it was the least I could do."
            mike.say "Now, you should get back to sleep."
            "Lexi sighs and lies back down in her nest of blankets."
            lexi.say "I'll try, [hero.name]."
            lexi.say "But this sofa's doesn't make a great bed."
            lexi.say "Who knows - maybe I could get an upgrade?"
            mike.say "I don't know about that, Lexi."
            mike.say "There aren't any spare beds in the house right now."
            "Lexi raises an eyebrow at this, smiling as she does so."
            show lexi flirt
            lexi.say "Oh, I don't mind sharing!"
            lexi.say "Good night, [hero.name]!"
            mike.say "Ah..."
            mike.say "G...good night, Lexi!"
            $ lexi.love += 1
        "Tell off":
            "And anyway, where does Lexi get off lecturing me?"
            "I was the one that took her in when she lost everything!"
            "You'd think that she might be a little grateful."
            mike.say "Well you are getting to stay here rent-free, Lexi."
            mike.say "And we never put a limit on the length of that either.."
            "By now, Lexi's finally shaken off the drowsiness."
            "Her eyes go wide and the corners of her mouth turn down at this."
            lexi.say "Huh, and here I was thinking you were just doing me a good turn!"
            lexi.say "You sound like you have something to say, [hero.name]."
            lexi.say "So why don't you just come out and say it, huh?"
            "Okay, she asked for this."
            "I take a deep breath before I say it."
            mike.say "I'll tell you what I mean, Lexi."
            mike.say "I mean maybe if you helped out around the house for once."
            mike.say "Maybe then those of us that are actually paying the bills wouldn't be doing it so late!"
            "Lexi's up off of the sofa the moment I'm done talking."
            "She still has the blankets wrapped around her."
            "Which makes her look more than a little ridiculous."
            "But that doesn't stop her waving a finger in my face."
            lexi.say "I'm going to pretend you didn't say that, [hero.name]."
            lexi.say "And that's because you're my friend, as well as a good guy."
            lexi.say "I'm going to sleep somewhere else now."
            lexi.say "So you can think about how mean you just were to me."
            mike.say "B...but, Lexi..."
            mike.say "Where else are you going to sleep?"
            "Lexi looks back over her shoulder as she walks out of the living room."
            lexi.say "I'm taking your room, and you can have the sofa."
            lexi.say "Good night - hope you feel better in the morning!"
            hide lexi
            $ lexi.love -= 1
            "Wait a minute..."
            "What just happened?"
            "How did I end up losing my own bed and sleeping on the sofa?!?"
            $ game.set_flag("chores", 25, "week", "+")
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
    "I have that really bad habit of getting home from work in the evening and just collapsing on the sofa with the TV blaring at me."
    "At one point, I might actually have sat down to watch something specific, but these days it's more like sensory white noise."
    "Often I won't even so much as know what I'm watching, unless something truly noteworthy catches my attention or someone walks in and yells at me."
    "Tonight it was a case of the former, rather than the latter."
    "And in some ways I was rather glad that I was the only person in the room when I realised what was being said."
    "As distracted as I am when slumped in front of the TV, there are certain terms and phrases that seem to always break through the haze and register with me."
    "Almost like Pavlov ringing the bell for his trained dogs, I'll immediately sit up and begin to pay attention."
    "In this case, the word just so happens to be 'polygamy'."
    "I look up, instantly intrigued, and see that I'm actually watching the news."
    "Grabbing the remote, I rewind by about thirty seconds to catch the start of the current story."
    "Shady guy" "...saw the second reading of the controversial 'Marriage and Social Institution Reform Bill' before the lower house."
    "Shady guy" "Dubbed the 'Bigamy Bill' by its critics on account of its most far-reaching effects, the bill was expected to finally be thrown out in today's session."
    "Oh yeah - the bill going through parliament that had a clause about polygamy buried in there somewhere."
    "I'd read a little about it online, and it was supposedly all about equalising the rights of marriage and civil partnerships for everyone, no matter their orientation."
    "The bit about polygamy was probably the least important aspect of it all."
    "But the constantly outraged conservative right were too afraid of being labelled anti-LGBTQ+ bigots to go after the main portions of the bill."
    "So they'd seized upon the polygamy part as a kind of backdoor to oppose it, nicknaming it the 'Bigamy Bill' as a result."
    "Shady guy" "But in a shock move, it received the backing of the formerly abstaining members to narrowly pass into law."
    "Shady guy" "Its opponents have cited this move as proof of a wider conspiracy to undermine..."
    "The anchor went on with her dissection of the matter, but I had already stopped listening some time beforehand."
    "It was actually happening, and soon the law would change to allow anyone that wanted to marry more than one person at a time."
    "I guess someone else might have been mulling over the wider social implications of this change in the law."
    "But what instantly sprang into my mind, was the fact that if polygamy was normalised, then relationships between more than two individuals would be as well."
    "It might only be the more open-minded of girls that would begin to come round to the idea at first."
    "But surely it would mean that, were someone to raise the possibility with two or more members of the opposite sex, they wouldn't automatically earn themselves a slap across the face?"
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
    if renpy.has_label("home_harem_achievement_2") and not game.flags.cheat:
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
