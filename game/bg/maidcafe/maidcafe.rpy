init python:
    Room(**{
    "name": "maidcafe",
    "hours": (9, 19),
    "conditions": [
        IsHour(9, 19),
        Or(
            And(
                HeroTarget(IsGender("male")),
                IsDone("bree_event_07b"),
                PersonTarget(bree,
                    Not(IsHidden()),
                ),
            ),
            HeroTarget(
                IsGender("female"),
                Or(
                    IsFlag("job_day", False),
                    IsFlag("job_day", "maidcafe"),
                ),
            ),
        )
        ],
    "display_name": "Maid Cafe",
    "exits": ["map"],
    "music": "music/roa_music/chillaxing_waves.ogg",
    "outfit": "casual",
    })

    Activity(**{
    "name": "maidcafe_order",
    "money_cost": 25,
    "rooms": "maidcafe",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "display_name": "Order something",
    "icon": "coffee",
    "once_day": True,
    "label": "maidcafe_order",
    })

    Activity(**{
    "name": "maidcafe_welcome_coffee",
    "label": "drink_coffee",
    "duration": 0,
    "energy": 2,
    "money_cost": 25,
    "icon": "coffee",
    "rooms": "maidcafe",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            IsFlag("coffee", False),
            IsGender("male"),
            ),
        PersonTarget(bree,
            Not(IsPresent()),
            ),
        ],
    "display_name": "Order something",
    "once_day": True,
    "say": [
        "Just coffee. Black - like my soul.",
        "Even bad coffee is better than no coffee at all.",
        "Adventure in life is good; consistency in coffee even better.",
        "It doesn't matter where you're from - or how you feel... There's always peace in a strong cup of coffee.",
        "Do you know how helpless you feel if you have a full cup of coffee in your hand and you start to sneeze?",
        ],
    })

    Event(**{
    "name": "maidcafe_welcome",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe")
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "label": "maidcafe_welcome",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "kiara_special_coffee",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe"),
            IsFlag("kiara_bj"),
            Or(
                IsActivity("maidcafe_order"),
                IsActivity("maidcafe_welcome_coffee"),
                ),
            ),
        ],
    "label": "kiara_special_coffee",
    "chances": 20,
    "do_once": False,
    "once_week": True,
    })


label maidcafe_welcome:
    show bree
    bree.say "Welcome, [hero.name]."
    $ bree.flags.greeted = TemporaryFlag(True, 1)
    if bree.sub <= 75:
        $ bree.sub += 1
    return

label maidcafe_order:
    show bree
    bree.say "What can I get you, [hero.name]?"
    menu:
        "Coffee":
            mike.say "I would like some coffee please."
            bree.say "Right away."
            $ hero.energy += 2
        "Cocoa":
            mike.say "I would like some cocoa please."
            bree.say "I'll be back with it in a flash."
            $ hero.fun += 2
        "Moka":
            mike.say "I would like some moka please."
            bree.say "As you wish, [hero.name]."
            $ hero.energy += 1
            $ hero.fun += 1
    scene bg black with dissolve
    pause 0.1
    scene bg maidcafe with dissolve
    if bree.sub <= 50:
        $ bree.sub += 1
    show bree
    if not bree.is_sex_slave:
        bree.say "Here you are, [hero.name]!"
    mike.say "Thank you, [bree.name]."
    hide bree
    return


label kiara_special_coffee:
    scene bg maidcafe with fade
    "Here I am, lost in my thoughts, wondering what I'm going to order today."
    show kiara talkative at center, zoomAt(1.25, (940, 880)) with easeinright
    kiara.say "Ah, [hero.name]."
    kiara.say "It's such a pleasure to see you again."
    show kiara smile
    "I smile at Kiara, trying as best I can not to give off the wrong signals."
    "Which is hard, because almost everything about her seems to have a definite sexual undertone."
    show kiara normal
    mike.say "Y...yeah..."
    mike.say "It's a pleasure to see me - I mean you..."
    mike.say "I mean, hi!"
    show kiara tantrum at startle
    "Kiara tosses her head back and lets out a deep, genuine laugh at my tongue-tied answer."
    show kiara talkative at center, zoomAt(1.25, (640, 880)) with ease
    kiara.say "Have you already ordered?"
    show kiara normal
    mike.say "Not yet. I like everything here."
    mike.say "To choose is to renounce, as it's said."
    show kiara stare
    "A glimmer lights up in Kiara's eyes."
    show kiara talkative at center, traveling(1.0, 0.3, (940, 720))
    kiara.say "I know exactly what you need. Follow me in the back-room."
    show kiara normal
    menu:
        "A coffee it is":
            mike.say "Thanks but I think I'll go for a good old black coffee."
            show kiara sad
            "I can see a look of disappointment in Kiara's eyes."
            show kiara whining
            kiara.say "Too bad. Enjoy your coffee then."
            show kiara talkative
            kiara.say "Maybe I'll see you around some time."
            hide kiara with easeoutright
            "And then she's gone."
            "I order my coffee, and I'm gone too."
            $ hero.energy += 2
            $ hero.replace_activity()
            $ game.room = "street"
            return
        "I'm in":
            mike.say "Let's say I'm more than intrigued. Let's go."
    scene bg maidcafe at dark, blur(5)
    show kiara delicious at center, zoomAt(1.5, (640, 1040))
    with fade
    pause 0.3
    show kiara at center, zoomAt(1.5, (640, 1280)) with ease
    "The door is barely closed, Kiara already kneeling down in front of me reaching for my flies."
    kiara.say "Mmm..."
    show kiara talkative
    kiara.say "These pants are SO tight."
    kiara.say "I can see every little detail, [hero.name]."
    kiara.say "It's like you've been teasing me the whole time you've been here!"
    show kiara normal
    play sound pants_unzip
    "She has my flies open by now."
    "And her fingers are reaching inside..."
    show kiara talkative
    kiara.say "But I knew I wanted some of this the moment that I saw it."
    kiara.say "Getting it between my lips - that's all I've been able to think about!"
    scene kiara maidcafe blowjob with fade
    "And then she does just that."
    "I'd be lying if I said I wasn't already hard."
    "She's a stunning woman, with a body to die for."
    "And what she's doing, in such a place? What if someone open the door."
    "The element of danger's more than enough to make my cock as stiff as a board."
    show kiara maidcafe blowjob lick up big
    "Kiara starts by kissing the head of my dick."
    "She goes slowly, looking up at me the whole time."
    play sexsfx1 bj_sucking loop
    show kiara maidcafe blowjob blow down handjob -medium
    "And then she begins to take it into her mouth an inch at a time."
    "She's good, but the fear of being discovered makes it so much more intense."
    show kiara maidcafe blowjob up
    "Every moment that she has my cock in her mouth, I want to gasp and cry out."
    "But I have to bite down on the urge for fear of giving the game away."
    show kiara maidcafe blowjob down
    "By the time Kiara has the length of my cock inside of her mouth, I'm almost holding my breath."
    "More than once I hear voices getting closer of the door."
    "But it always fades out."
    show kiara maidcafe blowjob inmouth surprise squirt with hpunch
    play sexsfx1 cum_inside
    with hpunch
    "Maybe it's the sense of relief that makes me cum a second later."
    with hpunch
    "Whatever the reason, Kiara takes it in her stride."
    with hpunch
    "She hardly flinches as I shoot my load into her mouth."
    "I watch as she stands up casually, stuffing my cock back into my pants."
    stop sexsfx1
    scene bg maidcafe
    show kiara talkative at center, zoomAt(1.25, (640, 880))
    with fade
    kiara.say "I hope you enjoyed this special treat."
    show kiara smile
    "And so I hurry out of the cafe, already trying to get my head into a better order."
    scene bg black with dissolve
    $ game.room = "street"
    $ game.pass_time(1)
    $ hero.replace_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
