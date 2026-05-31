init 1:
    layeredimage bg secondfloor:
        always "secondfloor"
        always "secondfloor_bathroom"
        if hero.is_female or not bree.is_gone_forever:
            "secondfloor_bree"
        if not sasha.is_gone_forever:
            "secondfloor_sasha"

init python:
    Room(**{
    "name": "secondfloor",
    "display_name": "Hallway",
    "exits": ["livingroom", "bedroom5", "bedroom2", "bedroom3", "bedroom4", "bathroom", "housemap"],
    "music": house_music(),
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
    "name": "knock_bathroom_1",
    "duration": 0,
    "rooms": "secondfloor",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        Or(
            PersonTarget(bree,
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            PersonTarget(sasha,
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            PersonTarget(minami,
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            PersonTarget("lexi",
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            PersonTarget("mike",
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            PersonTarget(samantha,
                Not(IsHidden()),
                IsRoom("bathroom"),
                ),
            ),
        ],
    "display_name": "Knock (Bathroom)",
    "icon": "knock_bathroom",
    "label": "knock_bathroom",
    })

    Activity(**{
    "name": "knock_bedroom5",
    "duration": 0,
    "rooms": "secondfloor",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        PersonTarget(minami,
            Not(IsHidden()),
            IsRoom("bedroom5"),
            ),
        ],
    "display_name": "Knock (Minami)",
    "label": ("knock_bedroom", "bedroom5"),
    "icon": "knock_bedroom5",
    })

    Activity(**{
    "name": "knock_bedroom3",
    "duration": 0,
    "rooms": "secondfloor",
    "conditions": [
        HeroTarget(
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            ),
        ],
    "display_name": "Knock (Sasha)",
    "label": ("knock_bedroom", "bedroom3"),
    "icon": "knock_bedroom3",
    })

    Activity(**{
    "name": "knock_bedroom2",
    "duration": 0,
    "rooms": "secondfloor",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(OnDate()),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            ),
        ],
    "display_name": "Knock ([bree.name])",
    "label": ("knock_bedroom", "bedroom2"),
    "icon": "knock_bedroom2",
    })

    Activity(**{
    "name": "clean_the_secondfloor",
    "rooms": "secondfloor",
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
    "label": "clean_the_secondfloor",
    "icon": "vacuum",
    "every_two_days": True,
    })

label clean_the_secondfloor:
    show chibi vacuum
    if (not bree.hidden and bree.activity_name == 'sleep') and (not sasha.hidden and sasha.activity_name == 'sleep') and (not minami.hidden and minami.activity_name == 'sleep'):
        $ wake_up = randint(1, 3)
        if wake_up == 1:
            call expression f"vacuum_bree_sleep_{hero.gender}" from _call_vacuum_bree_sleep
        elif wake_up == 2:
            call expression f"vacuum_sasha_sleep_{hero.gender}" from _call_vacuum_sasha_sleep
        elif wake_up == 3:
            call expression f"vacuum_minami_sleep_{hero.gender}" from _call_vacuum_minami_sleep
    elif (not bree.hidden and bree.activity_name == 'sleep') and (not sasha.hidden and sasha.activity_name == 'sleep'):
        $ wake_up = randint(1, 2)
        if wake_up == 1:
            call expression f"vacuum_bree_sleep_{hero.gender}" from _call_vacuum_bree_sleep_1
        elif wake_up == 2:
            call expression f"vacuum_sasha_sleep_{hero.gender}" from _call_vacuum_sasha_sleep_1
    elif (not bree.hidden and bree.activity_name == 'sleep') and (not minami.hidden and minami.activity_name == 'sleep'):
        $ wake_up = randint(1, 2)
        if wake_up == 1:
            call expression f"vacuum_bree_sleep_{hero.gender}" from _call_vacuum_bree_sleep_2
        elif wake_up == 2:
            call expression f"vacuum_minami_sleep_{hero.gender}" from _call_vacuum_minami_sleep_1
    elif (not sasha.hidden and sasha.activity_name == 'sleep') and (not minami.hidden and minami.activity_name == 'sleep'):
        $ wake_up = randint(1, 2)
        if wake_up == 1:
            call expression f"vacuum_sasha_sleep_{hero.gender}" from _call_vacuum_sasha_sleep_2
        elif wake_up == 2:
            call expression f"vacuum_minami_sleep_{hero.gender}" from _call_vacuum_minami_sleep_2
    elif not bree.hidden and bree.activity_name == 'sleep':
        call expression f"vacuum_bree_sleep_{hero.gender}" from _call_vacuum_bree_sleep_3
    elif not sasha.hidden and sasha.activity_name == 'sleep':
        call expression f"vacuum_sasha_sleep_{hero.gender}" from _call_vacuum_sasha_sleep_3
    elif not minami.hidden and minami.activity_name == 'sleep':
        call expression f"vacuum_minami_sleep_{hero.gender}" from _call_vacuum_minami_sleep_3
    else:
        play sound vacuum
        $ game.set_flag("chores", 25, "week", "+")
        python:
            if game.flags.chores > 100:
                for p in Person.get_housemates():
                    p.love += 1
        "I clean the floor."
    stop sound
    return

label vacuum_bree_sleep_male:
    $ renpy.sound.play("sd/vacuum.ogg", loop=True)
    "I see that my name's down on the rota for vacuuming the house this week."
    "And don't get me wrong, I hate housework as much as the next same human being."
    "But I also want to keep the others sweet and look like I'm doing my bit."
    "So I grab the vacuum-cleaner and begin the arduous task that's been assigned to me."
    "I mean sure, I'm doing it last thing at night before I turn in."
    "But the important thing is that it's getting done at all - right?"
    "Well, apparently someone seems to think differently..."
    scene secondfloor
    show bree sleep annoyed
    bree.say "[hero.name]!"
    bree.say "What are you doing?!?"
    "I feel someone patting me on the back."
    "And so I spin round to see [bree.name] standing in the corridor behind me."
    "She's in her pyjamas, she her hair's a crazy mess too."
    stop sound
    "I turn off the vacuum in order to better hear what she's saying."
    mike.say "Oh...hi, [bree.name]."
    mike.say "Didn't think I'd catch you up at this hour!"
    "[bree.name] rolls her eyes at this."
    "But I can see that she's trying to keep her mood civil all the same."
    show bree angry
    bree.say "You didn't catch me up, [hero.name]."
    bree.say "You woke me up!"
    "I look down at the vacuum-nozzle in my hand."
    "And then I try to hide it behind my back - as if that'll somehow help."
    mike.say "Sorry about that, [bree.name]."
    mike.say "But I'm almost done now."
    mike.say "Shouldn't be more than another half-hour!"
    "I honestly think I can see the veins starting to stand out on [bree.name]'s forehead."
    "That and her eye start to twitch as she tries to hold onto her temper."
    "But it's not a struggle she can keep up for too long."
    bree.say "Ooh, [hero.name]!"
    bree.say "You selfish twerp!"
    bree.say "Couldn't you have done this BEFORE I went to bed?!?"
    menu:
        "Apologise":
            "I play the events of the past few hours back in my head."
            "I'm thinking that I can find proof to throw back at [bree.name]."
            "Something that will show her just why I have to be doing this now."
            "But all I can recall is that I spent hours on the Zbox."
            "Which is obviously my own dumb fault!"
            mike.say "Ah, yeah, [bree.name]."
            mike.say "I should have done that."
            mike.say "But I was on the Zbox instead."
            "I offer her a helpless shrug."
            mike.say "Sorry that I woke you."
            mike.say "And sorry for being an irresponsible jerk too."
            "I see the look on [bree.name]'s face soften at this."
            "She smiles weakly as she rolls her eyes."
            show bree normal
            bree.say "Apology accepted, [hero.name]."
            bree.say "I guess I was playing too."
            bree.say "And I remember asking you to stay when you wanted to quit as well!"
            bree.say "How about you leave the vacuuming until the morning, huh?"
            bree.say "And if Sasha gives you a hard time, I'll tell her I let you off."
            "I nod, returning [bree.name]'s smile."
            mike.say "Thanks, [bree.name]."
            mike.say "See you in the morning."
            "[bree.name] turns on her heel and retreats to her bedroom."
            "Which leaves me alone in the corridor, still clutching the vacuum-nozzle."
            $ bree.love += 1
        "Tell off":
            "Hey, wait a minute - where does [bree.name] get off saying all of that?"
            "She and Sasha are always lecturing me about doing my fair share around here."
            "And here I am, trying to do just that, and getting hassle for it!"
            mike.say "I couldn't have done it earlier, [bree.name]."
            mike.say "It would've cut into my gaming time!"
            "[bree.name]'s eyes go wide at this and her mouth hangs open."
            "Somehow I don't think the explanation is what she wanted to hear."
            show bree lose
            bree.say "That is the single lamest excuse I've ever heard!"
            bree.say "Nobody made you play on the Zbox all night."
            mike.say "Oh no?"
            mike.say "I seem to remember someone asking me to keep playing."
            mike.say "A certain person not a million miles from here too!"
            show bree angry with vpunch
            bree.say "WHAT?"
            bree.say "You mean this is MY fault?!?"
            bree.say "I didn't exactly have to twist your arm!"
            "[bree.name] throws up her arms in utter frustration."
            "And I take a step back in the fear that she's actually going to hit me."
            show bree annoyed
            bree.say "Urgh..."
            bree.say "I can't keep having this conversation."
            bree.say "I need to sleep!"
            bree.say "Just finish it off in the morning, okay?"
            mike.say "Ah, okay, [bree.name]."
            "[bree.name] nods as she turns to walk back to her door."
            bree.say "Oh, and [hero.name]?"
            mike.say "Yeah, [bree.name]?"
            bree.say "If I hear that thing again before then, I'll shove it where the sun doesn't shine!"
            $ bree.love -= 1
            hide bree
            "I watch [bree.name] disappear back into her room, wondering if she really means it!"
    return

label vacuum_sasha_sleep_male:
    $ renpy.sound.play("sd/vacuum.ogg", loop=True)
    "There's nothing that I particularly look forward to getting assigned on the cleaning rota for the house."
    "But when it comes around to being my turn to use the vacuum-cleaner, it's at least a small mercy."
    "With the nozzle in one hand and pulling the rest of the thing behind me, I can hurry here and there."
    "It might be getting late, but if I'm as quick as usual, then I can be in bed in record time!"
    "With that in mind, I power through the rooms and head upstairs to finish off."
    stop sound
    "But I'm no more than halfway down the corridor when the vacuum-cleaner just seems to stop working."
    "Puzzled, I stare down the nozzle, wondering if something got jammed in there."
    "And that's when I hear the sound of someone coughing behind me."
    scene secondfloor
    show sasha sleep annoyed
    sasha.say "Ahem..."
    "I almost jump out of my skin before I realise it's just Sasha."
    "But then I get a better look at the expression on her face."
    "That and the fact she's in her pyjamas."
    "She regards me with an ominous air as she swings the vacuum-cleaner's plug in the air."
    mike.say "Oh...hi, Sasha."
    mike.say "Just getting on with the vacuuming, you know?"
    mike.say "Doing my part to keep the house clean!"
    "Sasha shakes her head like she's being spoken to by a complete moron."
    sasha.say "Yeah, I kind of gathered that, [hero.name]."
    sasha.say "What's bugging me is why you're doing it right now, huh?"
    sasha.say "Why are you doing it while I'm trying to sleep?"
    "I can already feel the guilt beginning to take a hold of me."
    "And it makes me start running off at the mouth a few moments later."
    mike.say "Oh..."
    mike.say "You were asleep?"
    mike.say "Sorry, Sasha - I didn't realise!"
    sasha.say "Oh, don't worry about that, [hero.name]."
    sasha.say "I'm not asleep anymore, thanks to you."
    sasha.say "And you should be a lot more concerned with something else."
    show sasha angry
    sasha.say "Namely where I'm going to stick this plug!"
    menu:
        "Apologise":
            "I'm about to open my mouth and argue the toss with Sasha."
            "But then I notice the tiredness in her eyes."
            "And I remember that I wasted most of the night on the Zbox."
            "She's right, I'm being a pretty selfish ass right now."
            mike.say "I...I'm sorry, Sasha."
            mike.say "You're right, I should have done this hours ago."
            mike.say "I'll finish up in the morning."
            "Sasha blinks, as though she doesn't quite believe what she's hearing."
            "But then I see her mood soften and she shakes her head."
            show sasha normal
            sasha.say "Thanks, [hero.name]."
            sasha.say "And I'm sorry too - for blowing up like that."
            sasha.say "I guess I'm extra tetchy right now!"
            "I nod, appreciating the change in her mood."
            mike.say "No problem, Sasha."
            mike.say "Just let me know if you need anything."
            "Sasha smiles as she passes me the plug to the vacuum-cleaner."
            sasha.say "I just might do that."
            sasha.say "But for now, all I need is some sleep."
            $ sasha.love += 1
            "I stand and wind the cord of the vacuum-cleaner around my arm."
            "Watching Sasha as she walks back to her room and closes the door."
            hide sasha
            "Even after so long living with housemates, I can still screw up."
            "Maybe I should make sure I do this kind of thing before I turn on the Zbox in future..."
        "Argue":
            "Geez, can't a guy catch a break around here?"
            "All I'm doing is making sure that I keep up my end of the cleaning!"
            "I'm pretty sure Sasha would be on my case if I wasn't too."
            "So what if I woke her up by accident?"
            "It's not as if she doesn't like to play heavy metal at maximum volume whenever she pleases!"
            mike.say "Aw, come on, Sasha."
            mike.say "Isn't the important thing that I'm doing it at all?"
            "I see an instant change in Sasha's mood."
            "And I know that I just messed up, big time!"
            "Before she looked pissed at me."
            show sasha vangry
            "But now I can see genuine irritation and annoyance flare in her eyes."
            sasha.say "Oh, so that's how it is, yeah?"
            sasha.say "We girls should be grateful you do your bit?"
            sasha.say "Grateful that the man of the house gets his hands dirty?!?"
            mike.say "No..."
            mike.say "Sasha, that's not what I meant!"
            sasha.say "Well that's what it sounded like from here."
            sasha.say "You know maybe if you spent less time on the Zbox."
            sasha.say "Then you wouldn't have to vacuum in the middle of the night!"
            $ sasha.love -= 1
            "Sasha underlines her point by shoving the plug into my stomach."
            "It's not quite a punch, but the blow's strong enough to make me gasp."
            hide sasha
            "I clutch for the plug as she turns her back on me and stalks away."
            "You know something, maybe she's right."
            "Maybe I should finish off the vacuuming in the morning..."
    return

label vacuum_minami_sleep_male:
    $ renpy.sound.play("sd/vacuum.ogg", loop=True)
    "I hate housework, it's the bane of my existence and something I always try to avoid."
    "But there was no way out of it this time, [bree.name] and Sasha made that abundantly clear."
    "The rota that they seem to have drawn up behind my back says that it's my turn to vacuum."
    "And so here I am, hoovering the carpets when I should be relaxing after a hard day's work."
    "It doesn't help that I put it off until the very last minute either."
    "As it's now getting late, and I'm not even halfway done!"
    "I have my head down, concentrating on some particularly stubborn fluff."
    "Which is why I only notice that I'm not alone anymore when I finally look up."
    "At first I only know that there's a pair of skinny knees in front of me."
    "But as soon as I stand up, I see that they belong to Minami."
    "She's standing there in her pyjamas, arms crossed over her chest."
    "And let's just say that she doesn't look pleased to see me."
    stop sound
    "I hastily turn off the vacuum cleaner so as to better hear what she has to say."
    scene secondfloor
    show minami sleep
    minami.say "Big bro..."
    minami.say "What are you even doing?"
    "I can't help shrugging and holding up the nozzle of the vacuum."
    "Because I would have thought the answer to that was pretty obvious."
    mike.say "Erm..."
    mike.say "I was vacuuming?"
    minami.say "Oh, ha ha, very funny!"
    show minami annoyed
    minami.say "I can see that, you moron."
    mike.say "Then why did you ask..."
    minami.say "Urgh..."
    show minami angry
    minami.say "I meant why are you doing it NOW, big bro."
    minami.say "In the middle of the night and outside my room too!"
    menu:
        "Apologise":
            "Maybe it was a little selfish of me to leave it this late."
            "Minami's got every right to be mad at me for waking her up."
            "I'm her big brother after all."
            "I should be helping her settle in here."
            "And I definitely shouldn't be making things harder for her."
            mike.say "Ah..."
            mike.say "You're right, Minami."
            mike.say "I'm sorry for waking you - it was selfish of me."
            mike.say "Look, I'll pack it in for tonight and finish in the morning."
            show minami normal
            "I see the look on Minami's face soften as I admit that I'm at fault."
            "Nods her head, but doesn't turn to go back into her room."
            minami.say "Thanks, big bro."
            minami.say "But won't you get in trouble with [bree.name] and Sasha?"
            "All I can do is shrug helplessly at this."
            mike.say "I guess so, Minami."
            mike.say "But it's my fault for not doing it sooner."
            mike.say "When you live in a shared house, you have to do your bit."
            "Minami nods and turns to walk away."
            "But then she pauses, looking back over her shoulder."
            minami.say "Ah, big bro..."
            minami.say "Maybe I could help you out in the morning?"
            minami.say "If I get some decent sleep, that is..."
            "I give Minami a smile as she slips into her room and closes the door behind her."
            $ minami.love += 1
        "Tell off":
            "Where in the hell does she get off talking to me like that?"
            "I've never seem Minami pushing the vacuum cleaner around the house."
            "Come to that, I've never seen her cleaning the dishes either."
            "Or on her hands and knees, scrubbing the floors!"
            "And I'd remember if I had seen her doing that last one too..."
            mike.say "You do know that we're not at home anymore - right, Minami?"
            mike.say "We don't have Mom running around after us here."
            mike.say "Everyone does their share of the chores around the house."
            "Minami looks a little surprised by my outburst."
            "But then she seems to recover some of her former composure."
            show minami annoyed
            minami.say "Hey, that's not fair, big bro!"
            minami.say "It's not my fault Mom liked to spoil me."
            minami.say "I...I was mad at you because I needed to sleep, okay?"
            if game.calendar.day_of_week_name not in ['friday', 'saturday']:
                minami.say "I have a class first thing in the morning."
            "I feel my mood soften a little at this."
            "Minami is kind of new to living away from home."
            mike.say "I know it's not great, Minami."
            mike.say "But I got in late from work."
            mike.say "And I need to get this done tonight."
            mike.say "I promise that I'll try to hurry up, okay?"
            show minami angry
            $ minami.love -= 1
            "Minami pouts at this, but she nods all the same."
            hide minami
            "And I wait until she closes her bedroom door to resume cleaning."
            "I don't feel good about it, but she'll just have to cope."
            "Maybe it's time the little princess got used to the real world."
            $ game.set_flag("chores", 25, "week", "+")
    return

label knock_bedroom(bedroom="bedroom2"):
    $ girls = Room.find(bedroom).get_present_girls(valid=True)
    $ upset_girls = Room.find(bedroom).get_upset_girls(girls)
    $ awake_girls = [g for g in girls if g.activity_name != "sleep"]
    if not awake_girls:
        $ renpy.say("", "No answer. " + randchoice(girls).id.capitalize() + " must be sleeping.")
    elif upset_girls:
        $ randchoice(upset_girls).say("Don't come in...")
    else:
        $ randchoice(awake_girls).say("Yes?")
    return

label knock_bathroom:
    $ peeping_girls = [g for g in Room.find("bathroom").get_present_girls(valid=True) if not g.flags.peeped]
    show bg door bathroom with fade
    menu:
        "Take a peek" if peeping_girls:
            if not hero.has_skill("sneaky") and randint(0, 2) == 0 and Harem.find_by_name('home'):
                call caught_peeping (peeping_girls) from _call_caught_peeping
                if _return == "caught":
                    return
            $ girl = randchoice(peeping_girls)
            if all(g in peeping_girls and g.lesbian >= 5 for g in (bree, sasha)):
                show peeping_bath bree sasha
                "I see [bree.name] and Sasha bathing together..."
                "They are so cute!"
                $ bree.flags.peeped = TemporaryFlag(True, "day")
                $ bree.flags.peeped_count += 1
                $ sasha.flags.peeped = TemporaryFlag(True, "day")
                $ sasha.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide peeping_bath
            elif all(g in peeping_girls and g.lesbian >= 5 for g in (bree, minami)):
                show peeping_bath minami bree
                "I see [bree.name] and Minami bathing together..."
                "They are so cute!"
                $ bree.flags.peeped = TemporaryFlag(True, "day")
                $ bree.flags.peeped_count += 1
                $ minami.flags.peeped = TemporaryFlag(True, "day")
                $ minami.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide peeping_bath
            elif Person.is_not_hidden("lexi") and all(g in peeping_girls and g.lesbian >= 5 for g in (lexi, sasha)):
                if game.week_day % 2 == 0:
                    show peeping_bath lexi sasha
                    "I see Lexi and Sasha bathing together..."
                    "They are so cute!"
                    $ lexi.flags.peeped = TemporaryFlag(True, "day")
                    $ lexi.flags.peeped_count += 1
                    $ sasha.flags.peeped = TemporaryFlag(True, "day")
                    $ sasha.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_bath
                else:
                    show peeping_shower lexi sasha
                    "I see Lexi and Sasha showering together..."
                    "They are so cute!"
                    $ lexi.flags.peeped = TemporaryFlag(True, "day")
                    $ lexi.flags.peeped_count += 1
                    $ sasha.flags.peeped = TemporaryFlag(True, "day")
                    $ sasha.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_shower
            elif Person.is_not_hidden("lexi") and all(g in peeping_girls and g.lesbian >= 5 for g in (lexi, minami)):
                if game.week_day % 2 == 0:
                    show peeping_bath lexi minami
                    "I see Lexi and Minami bathing together..."
                    "They are so cute!"
                    $ lexi.flags.peeped = TemporaryFlag(True, "day")
                    $ lexi.flags.peeped_count += 1
                    $ minami.flags.peeped = TemporaryFlag(True, "day")
                    $ minami.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_bath
                else:
                    show peeping_shower lexi minami
                    "I see Lexi and Minami showering together..."
                    "They are so cute!"
                    $ lexi.flags.peeped = TemporaryFlag(True, "day")
                    $ lexi.flags.peeped_count += 1
                    $ minami.flags.peeped = TemporaryFlag(True, "day")
                    $ minami.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_shower
            elif all(g in peeping_girls and g.lesbian >= 5 for g in (samantha, minami)):
                if game.week_day % 2 == 0:
                    show peeping_bath samantha minami
                    "I see Samantha and Minami bathing together..."
                    "They are so cute!"
                    $ samantha.flags.peeped = TemporaryFlag(True, "day")
                    $ samantha.flags.peeped_count += 1
                    $ minami.flags.peeped = TemporaryFlag(True, "day")
                    $ minami.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_bath
                else:
                    show peeping_shower samantha minami
                    "I see Samantha and Minami showering together..."
                    "They are so cute!"
                    $ samantha.flags.peeped = TemporaryFlag(True, "day")
                    $ samantha.flags.peeped_count += 1
                    $ minami.flags.peeped = TemporaryFlag(True, "day")
                    $ minami.flags.peeped_count += 1
                    $ hero.flags.peeped += 1
                    hide peeping_shower
            elif all(g in peeping_girls and g.lesbian >= 5 for g in (samantha, sasha)):

                show peeping_bath samantha sasha
                "I see Samantha and Sasha bathing together..."
                "They are so cute!"
                $ samantha.flags.peeped = TemporaryFlag(True, "day")
                $ samantha.flags.peeped_count += 1
                $ sasha.flags.peeped = TemporaryFlag(True, "day")
                $ sasha.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide peeping_bath











            elif all(g in peeping_girls for g in (mike, sasha)):
                show peeping_bath mike sasha
                "I see [mike.name] and Sasha bathing together..."
                "They are so cute!"
                $ mike.flags.peeped = TemporaryFlag(True, "day")
                $ mike.flags.peeped_count += 1
                $ sasha.flags.peeped = TemporaryFlag(True, "day")
                $ sasha.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide peeping_bath
            elif mike in peeping_girls:
                show peeping_bath mike
                "I see [mike.name] bathing..."
                "He is so cute!"
                $ mike.flags.peeped = TemporaryFlag(True, "day")
                $ mike.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide peeping_bath
            else:
                show expression "peeping " + girl.id
                if renpy.has_label(f"{girl.id}_peeping_scene_{hero.gender}"):
                    call expression f"{girl.id}_peeping_scene_{hero.gender}" from _call_expression_199
                else:
                    "I see [girl.name] showering..."
                    "She is so beautiful."
                $ girl.flags.peeped = TemporaryFlag(True, "day")
                $ girl.flags.peeped_count += 1
                $ hero.flags.peeped += 1
                hide expression "peeping " + girl.id
            call expression f"peeping_result_{hero.gender}" from _call_expression_200
        "Knock":

            $ upset_girls = Room.find("bathroom").get_upset_girls()
            $ renpy.log("upset_girls secondfloor: " + str(upset_girls))
            play sound door_knock
            if upset_girls:
                $ upset_girl = randchoice(upset_girls)
                if upset_girl.activity["clothes"] == "naked":
                    $ renpy.say(upset_girl.id, "Don't come in, it's occupied.")
                elif upset_girl.activity["clothes"] in ["underwear","towel"]:
                    $ renpy.say(upset_girl.id, "Don't come in...")
                else:
                    $ renpy.say(upset_girl.id, "Something is wrong...I can feel it")
            else:
                $ girl = randchoice(Room.find("bathroom").get_present_girls(valid=True))
                $ renpy.say(girl.id, "Yes?")
    return

label peeping_result_male:
    if minami in peeping_girls:
        $ minami.siscon += 1
    if randint(1, 100) > hero.flags.peeped * 10 or hero.has_skill("sneaky"):
        $ hero.fun += 1
    else:
        call expression f"{girl.id}_peeping_reactions_{hero.gender}" from _call_expression_201
    return

label caught_peeping(peeping_girls):
    if Harem.find_by_name("home"):
        $ harem_girls = map(Person.find, Harem.find_by_name("home").active_members)
    else:
        $ harem_girls = [bree, sasha]

    $ roaming_girls = set(harem_girls) - set(peeping_girls)
    $ roaming_girls = [g for g in roaming_girls if Room.has_tag(g.room, "home") and g.activity_name != "sleep" and g.sub < 90]
    if roaming_girls:
        $ caught_girl = randchoice(roaming_girls)
        if renpy.has_label(f"{caught_girl.id}_caught_peeping_{hero.gender}"):
            call expression f"{caught_girl.id}_caught_peeping_{hero.gender}" from _call_expression_202
        else:
            $ renpy.say(caught_girl.id, "HEY!")
            show expression caught_girl.id + " angry"
            $ renpy.say(caught_girl.id, "What are you doing?!?")
            call expression f"caught_peeping_dialogues_1_{hero.gender}" pass (caught_girl=caught_girl.name) from _call_expression_203
            $ caught_girl.love -= 10
            $ caught_girl.sub -= 2

        return 'caught'
    return

label caught_peeping_dialogues_1_male(caught_girl):
    mike.say "Ah..."
    mike.say "H...hey, [caught_girl]!"
    mike.say "I was just..."
    mike.say "Just checking..."
    return

label bree_caught_peeping_male:
    scene bg secondfloor
    "I'm just walking past the bathroom door, minding my own business when I hear it."
    "The sound of running water, like someone's turned on the shower and hopped right in there."
    "Of course, there's nothing at all unusual about that - it's a sound I hear all the time."
    "But the thing is it's only ever that loud when you're on the other side of the door."
    "Or else when the bathroom door's been left open..."
    "I take a quick glace over and see that's exactly what's happened."
    "Whoever's in there has forgotten to close the door behind them."
    scene bg door bathroom with fade
    "I can't help being drawn over to the door."
    "I keep telling myself that all I'm going to do is close it."
    "That I'm not going to take the chance to peek inside."
    "But I'm only human, and so curiosity gets the better of me."
    "I take hold of the handle, and lower my head towards the crack in the door..."
    bree.say "[hero.name]!"
    bree.say "Are you really..."
    bree.say "O...M...G..."
    scene bg secondfloor
    show bree angry
    with hpunch
    "I spin around at the sound of [bree.name]'s voice."
    "A flurry of excuses already leaping around inside of my head as I do so."
    mike.say "No, no, no..."
    mike.say "This isn't what it looks like, [bree.name]!"
    mike.say "I was just going to shut the door, that's all!"
    "[bree.name] shakes her head, dismissing my explanation."
    show bree vangry
    bree.say "Since when does closing a door need you to peak inside, huh?"
    show fx anger
    bree.say "You were going to take a look in there, you pig!"
    show bree angry
    mike.say "No, [bree.name], you've got it all wrong."
    mike.say "I was just checking that there was someone in there."
    mike.say "That nobody left the shower running by mistake - I swear it!"
    show bree vangry
    bree.say "Well, I don't believe you, [hero.name]."
    bree.say "And I'm getting a lock fitted on that bathroom door too!"
    $ bree.love -= 10
    $ bree.sub -= 2
    hide bree with easeoutleft
    "With that, [bree.name] storms off."
    "Leaving me alone and feeling like the pathetic perv she now thinks I am."
    return

label lexi_caught_peeping_male:
    scene bg secondfloor
    "I can't help noticing that the door to the bathroom's been left open as I walk past."
    "And this means that I can also hear the sound of running water coming from inside."
    "I know, I know - I should just shrug it off and keep right on walking."
    "That's what a mature, well-rounded adult would do in this situation."
    "But last time I checked, I wasn't one of those!"
    scene bg door bathroom with fade
    "Which is why I find myself sneaking towards the bathroom door."
    "All I'm going to do is take a quick peek inside."
    "It's not like I'm going to film them on my phone or anything sleazy like that."
    "I mean, there might not even be anybody in there right now."
    "One of the girls could have left the shower running while they went to grab something."
    "I'm turning all of these excuses and justifications over in my mind."
    "Using them to keep my conscience quiet as I lean in to peep through the crack in the door."
    "But if my conscience isn't enough to stop me, the sound I hear next surely is..."
    lexi.say "Well, well, well..."
    lexi.say "What do we have here?"
    scene bg secondfloor
    show lexi smile
    with hpunch
    "I jump up at the sound of Lexi's voice, almost stumbling away from the bathroom door."
    "She's standing no more than a few feet away."
    "And I can see that she has an amused smile on her face too."
    mike.say "Wh...wha..."
    mike.say "What's up, Lexi!"
    mike.say "I...I was just..."
    "Lexi cuts me off before I can cook up an excuse for my actions."
    "She shakes her head, dismissing my attempts to play the innocent."
    show lexi normal
    lexi.say "You were just spying on whoever's in there showering, weren't you?"
    lexi.say "Sneaking around like a disgusting little perv with a stiffy!"
    lexi.say "Is that part of the deal for letting me stay here, [hero.name]?"
    lexi.say "You drooling through a crack in the door whenever I shower?"
    lexi.say "How about when I go for a number one or number two, huh?"
    show fx anger
    lexi.say "Are you gonna watch me do that too?"
    show lexi smile
    mike.say "Aw, come on, Lexi!"
    mike.say "I don't normally do this kind of thing."
    show lexi normal
    lexi.say "So what?"
    lexi.say "You're only a perv on special occasions?"
    lexi.say "Look, [hero.name] - I'll let it slide this one, okay?"
    show lexi angry
    lexi.say "But if I catch you again, I'm telling the other girls."
    lexi.say "And we'll see how they like living with a Peeping Tom!"
    $ lexi.love -= 10
    $ lexi.sub -= 2
    hide lexi with easeoutleft
    "And with that, Lexi strides away."
    return

label minami_caught_peeping_male:
    scene bg secondfloor
    "I can hear the sound of the shower running from all the way down the corridor."
    "Which is a little weird, as you can normally only hear it when you walk by the door."
    "Or else when someone's left the door open..."
    scene bg door bathroom with fade
    "Which I see, as I get closer, is exactly what someone seems to have done."
    "The door is standing open just a little, the crack being no more than an inch."
    "I know that I should just ignore it and keep on walking..."
    "But I'm not made of stone, now am I?"
    "So I hurry over to the bathroom door as quietly as I can manage."
    "I'll just take a quick peep, nothing more than that."
    "And it's more for the sake of satisfying my curiosity than anything else."
    "More that than me perving out at the chance to see one of the girls in the shower."
    "I lean in close, closing one eye as I put the other to the gap..."
    minami.say "BIG BRO!"
    minami.say "What the hell are you doing?!?"
    scene bg secondfloor
    show minami angry
    with hpunch
    "I leap up and back from the door far more quickly than got there in the first place."
    "And then I spin around to see Minami standing behind me."
    "She has her arms crossed over her chest and a look like thunder on her face."
    mike.say "M...Minami..."
    mike.say "I didn't see you there."
    mike.say "You scared the life out of me!"
    "I see Minami's face darken as she hears my tone of voice."
    "She shakes her head and advances on me."
    show minami vangry
    minami.say "Don't give me that, big bro."
    show fx anger
    minami.say "I saw what you were doing."
    minami.say "You were peeping through the bathroom door!"
    show minami angry
    mike.say "No way, Minami!"
    mike.say "I was just..."
    mike.say "Just checking nobody left the shower running, that's all!"
    show minami vangry
    minami.say "No way, big bro."
    minami.say "You're a massive perv!"
    $ minami.love -= 10
    $ minami.sub -= 2
    hide minami with easeoutleft
    "With that, Minami shakes her head and storms off."
    "Which leaves me alone to contemplate what I just did."
    "And I can't help wondering - was there a hint of jealousy at the end there?"
    return

label samantha_caught_peeping_male:
    scene bg secondfloor
    "I just happen to be passing the bathroom door when I hear the sound of running water from inside."
    "Nothing weird about that, apart from the fact the closed door usually keeps the sound from getting out."
    "So the fact that I can hear it out here can only mean one thing - someone left the door open."
    "I know that I shouldn't, that I really ought to just be on my way and forget all about it."
    "But I'm only human - and a quick peek couldn't possibly hurt, now could it?"
    scene bg door bathroom with fade
    "I sneak closer to the bathroom door, keeping as quiet as I can."
    "At the same time I'm leaning forwards, putting my eye to the crack in the door."
    "It's not like I need to watch for any length of time."
    "I can just peek in there long enough to get a good mental image."
    "One that'll come in handy when I'm alone later tonight!"
    "Nobody else needs to know..."
    samantha.say "HEY!"
    samantha.say "What are you doing?!?"
    "At the sound of Sam's voice, I almost jump out of my skin."
    "But I definitely jump away from the bathroom door."
    scene bg secondfloor
    show samantha upset
    with vpunch
    "And when I look up to meet her eye, she doesn't look pleased."
    mike.say "Ah..."
    if samantha.flags.nickname == "cupcake":
        mike.say "H...hey, Cupcake!"
    else:
        mike.say "H...hey, Sam!"
    mike.say "I was just..."
    mike.say "Just checking..."
    mike.say "To...to see if the bathroom was free!"
    "Sam looks at me like I just claimed to have two heads."
    show samantha angry
    samantha.say "Oh yeah?"
    show fx anger
    samantha.say "Then why not knock on the door, huh?"
    show samantha upset
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, that's a great idea, Cupcake!"
    else:
        mike.say "Hey, that's a great idea, Sam!"
    mike.say "I guess I should have thought of that!"
    "Sam lets out a sigh and rolls her eyes."
    show samantha annoyed
    samantha.say "Nice try, [hero.name]."
    samantha.say "But we both know what you were doing just now."
    samantha.say "Geez - did you used to do this when I lived here before?"
    show samantha upset
    "I open my mouth, trying to explain myself."
    "But Sam cuts me off before I can say a word."
    show samantha angry
    samantha.say "Actually, I don't want to know."
    samantha.say "Just promise me that you'll stop it, okay?"
    samantha.say "Maybe that way I can still believe you're not a total sleaze!"
    $ samantha.love -= 10
    $ samantha.sub -= 2
    hide samantha with easeoutleft
    "I nod in silence, and watch as Sam walks away."
    "I don't know what's worse - the guilt at getting caught."
    "Or the knowledge that I've disappointed her."
    return

label sasha_caught_peeping_male:
    scene bg secondfloor
    "I don't make a habit of this kind of thing, but I just couldn't resist the temptation."
    scene bg door bathroom with fade
    "The bathroom door is ajar as I walk past, and I can hear the sound of running water from inside."
    "Sneaking closer, I bend down to take a quick peak, just for a second - I swear it!"
    "And it's at that very moment I hear someone clear their throat behind me."
    "Not the innocent kind of coughing when a person can't help it."
    "But rather then deliberate kind when they're busting your ass!"
    sasha.say "And just what in the hell do you think you're doing?"
    scene bg secondfloor
    show sasha annoyed
    with fade
    "I turn around slowly, already feeling my guts churning."
    "Sasha's standing there, balled fists on her thighs."
    "She looks less than amused right now."
    "In fact, she looks like she's going to kill me!"
    mike.say "Ah..."
    mike.say "Hey, Sasha!"
    show sasha vangry
    sasha.say "Don't act all innocent with me, [hero.name]."
    sasha.say "And remind me - do we have a house policy on peeping?"
    show sasha upset
    "The question's not one that I was expecting."
    "And it leaves me more confused than anything else."
    mike.say "Erm..."
    mike.say "No, Sasha - I don't think we do."
    show sasha vangry
    sasha.say "And do you know WHY that is?"
    show sasha upset
    mike.say "N...no."
    show sasha vangry
    sasha.say "It's because we shouldn't NEED to have one, [hero.name]."
    show fx anger
    sasha.say "Because normal people don't go around perving on their housemates!"
    show sasha upset
    "I can already feel my cheeks burning with shame."
    "And I end up looking down at my feet, afraid to meet Sasha's eye."
    mike.say "Y...yeah, Sasha...that's right."
    mike.say "I don't know what I was thinking."
    show sasha angry
    "Sasha shakes her head and lets out a rueful chuckle."
    show sasha vangry
    sasha.say "Oh, I do, [hero.name]."
    sasha.say "I got a real good idea what was going on inside of your head!"
    sasha.say "And from now on, I'm keeping an eye on you."
    $ sasha.love -= 10
    $ sasha.sub -= 2
    hide sasha with easeoutright
    "With that, Sasha storms off."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
