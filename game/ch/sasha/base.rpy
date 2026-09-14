init python:
    Activity(**{
    "name": "watch_tv_with_sasha",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with Sasha",
    "max_girls": 1,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(MinStat("fun", 0)),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        InvalidActivities(
            "watch_tv_with_everyone_male",
            "watch_tv_with_everyone_female",
            ),
        ],
    "label": "sasha_tv",
    })

    Activity(**{
    "name": "play_in_the_pool_with_sasha",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with Sasha",
    "rooms": "pool",
    "conditions": [
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 10),
            ),
        PersonTarget(bree,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    "label": "sasha_play_pool",
    })

    Event(**{
    "name": "sasha_give_phone_number",
    "label": "give_phone_number",
    "girl": "sasha",
    "conditions": [
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(18, 19),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(sasha,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "sasha",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_auto_greet",
    "label": "auto_greet",
    "priority": 100,
    "conditions": [
        HeroTarget(IsActivity("None")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "girl": "sasha",
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_auto_chat",
    "label": "auto_chat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "girl": "sasha",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_are_you_sick",
    "label": "are_you_sick",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            ),
        ],
    "chances": (sasha, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_ask_out",
    "label": "ask_out",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            Not(HasCheated()),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            Not(HasCheated()),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_masturbation",
    "priority": 500,
    "label": "sasha_masturbation",
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsActivity("knock_bedroom3")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_day": True,
    })

label sasha_masturbation:
    $ hero.cancel_activity()
    "I'm not normally the kind of guy to be caught sneaking around for the sake of looking through a keyhole in the hope of being able to see something."
    "But I'm also only human, and living with a couple of female housemates as cute as [bree.name] and Sasha means that there are times when I just can't help myself and the normal rules go straight out the window."
    "It's just that halfway across the upstairs corridor; I hear a sound coming from behind the door to Sasha's bedroom."
    "I can hear deep, breathy series of sighs and moans that just keeps on getting louder and louder by the second."
    "Thinking that I'll just listen for a moment or two, long enough to confirm my suspicions as to what's going on in there, I walk as quietly as I can over to Sasha's door."
    "Before I can put my ear to the door, I see a chink of light emerging from the keyhole."
    "But almost as soon as my eye adjusts to the light coming from the keyhole, any thought of the morality of what I'm doing is utterly forgotten."
    "Instead I find myself rooted to the spot, straining to get a better view of what I can see inside."
    scene sasha_mast_01
    "Upon the bed, laid on her stomach."
    "Utterly naked, her normally pale skin is flushed with a rosy shade of pink and positively glistening with perspiration."
    "As if I needed any further explanation of just what she's in the middle of doing to herself."
    "Even if I could get my head straight and think about how much of an intimate moment I'm peeping in on here, I don't think that I could tear myself away from the keyhole."
    scene expression make_anim(sasha_mast01, time=0.4, loop=True)
    "She's stroking herself towards cumming with such obvious and audible passion?"
    "I watch with rapt attention as Sasha's fingers perform a dexterous dance over the lips and folds of her pussy."
    "Each touch seems to send shivers of pleasure shooting through her already aroused body, as if she were electrifying every inch of her skin."
    scene sasha_mast_04
    "Part of me is watching simply for the voyeuristic pleasure of seeing Sasha pleasure herself without fear of being disturbed."
    scene expression make_anim(sasha_mast02, time=0.4, loop=True)
    "I watch as Sasha sinks two of her fingers slowly into her pussy, working them in and out, the speed increasing as she goes."
    "At the same time her thumb begins to press down on her clit, massaging the sensitive spot without mercy."
    "My own cock has been hard almost since the moment that I started watching through the keyhole."
    "But now I can't keep from rubbing at it through my pants as I watch Sasha begin to cum at her own hand."
    "To see her features almost rendered insensible by the pleasure that she's experiencing is something I don't think I'll ever forget."
    "It's all that I can do to keep my hand from creeping into my own pants and following her example."
    "And that's something which almost becomes a battle as Sasha tosses her head back and starts to yelp at the arrival of her climax."
    play voice "vo/sasha/moan.ogg"
    scene sasha_mast_climax with hpunch
    "She cums more like an animal in heat than a girl bringing herself off."
    "Finally, her legs begin to wobble from exhaustion, and she literally collapses onto the bedclothes, adding to the dark patches that she's already dropped beforehand."
    "Not wanting to be caught out either way, I clamber to my feet and continue on my way back to my room, trying to hide my painful erection as I go."
    scene bg secondfloor
    return

label sasha_propose_male:
    show sasha
    "I really want to keep as far away from the traditional trappings of a proposal as I can for this, as I'm not exactly asking a traditional girl to marry me."
    "But despite the effort that I've gone to in order to avoid all of the cliches, it's more than worth it for the sake of making the proposal unique."
    "This means that I don't plan a huge gesture or go down on one knee in public with all eyes upon me."
    "Instead, I pick a quiet, intimate moment and pull out the ring without a great deal of ceremony."
    mike.say "Sasha, I have something I've been meaning to ask you..."
    if sasha.love < 195:
        show sasha sad
        "Much to my distress, the look of surprise in Sasha's eyes soon turns to agonised discomfort."
        sasha.say "Oh, [hero.name] - why'd you have to go and do a silly thing like that?"
        sasha.say "I was happy with things just the way they were."
        sasha.say "But this pretty much tells me you're not..."
        "I honestly don't know what to say."
        "How could I have misjudged the situation so badly?"
        $ sasha.love -= 25
        $ sasha.sub -= 25
    else:
        show sasha happy
        "At the sight of the ring, Sasha's eyes light up with what looks like genuine happiness."
        sasha.say "Oh, [hero.name] - are you asking me to marry you?!?"
        mike.say "Y...yes...yes I am, Sasha."
        mike.say "And...is that a yes?"
        sasha.say "Yes, of course it is!"
        sasha.say "I always dreamed of marrying my best friend - and now that dream's coming true!"
        $ sasha.set_fiance()
    hide sasha
    return

label sasha_cheated(action, cheat_npc=None):
    show sasha
    if sasha.is_sex_slave:
        $ sasha.sub += 1
    elif cheat_npc and Harem.together(sasha, cheat_npc):
        sasha.say "Give me back my toy!"
        show sasha kiss
        $ sasha.flags.kiss += 1
        "And without warning Sasha kisses me."
        $ sasha.love += 1
        hide sasha kiss
    else:
        show sasha angry
        if cheat_npc:
            $ sasha.flags.cheatedby = cheat_npc.id
        $ loss = 5
        if sasha.flags.girlfriend or sasha.flags.fiance:
            $ loss += 5
        $ sasha.love -= loss
        sasha.say "What the fuck do you think you are doing you moronic ape?"
    hide sasha
    return

label sasha_play_pool:
    "I splash some water towards Sasha."
    sasha.say "Dimwit! You'll regret that!"
    scene sasha pool
    "After that she retaliates and we play in the water for a while..."
    sasha.say "That was fun!"
    mike.say "It sure was."
    $ sasha.love += 1
    $ sasha.flags.greeted = TemporaryFlag(True, 1)
    scene bg pool
    return

label sasha_tv:
    call sasha_greet from _call_sasha_greet
    if hero.charm >= 40 - sasha.love or sasha.activity_name == "tv":
        call watch_tv_with (sasha) from _call_watch_tv_with_5
    else:
        show sasha talk
        sasha.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide sasha
    return

label sasha_tv_reaction:
    sasha.say "Ok."
    return

label sasha_tv_bj:
    scene expression make_anim(sasha_blow_couch, time=0.5, loop=True)
    "Sasha wraps her fingers around my shaft and rolls her tongue out, licking up along my length."
    mike.say "O... oh wow..."
    mike.say "It feels so good."
    sasha.say "I kind of knew this would please you..."
    if sasha.flags.mikeNickname:
        sasha.say "...[hero.name]."
    "Again, she licks up my shaft, up over the glans and over the tip."
    "What did I do to deserve the greatest roommate in the world?"
    "I wonder this as the excitement of her actions tingles up through my body."
    show sasha_blow_cum with hpunch
    "I can't hold back and, with a groan, I release, shooting up onto her."
    "Cum sprays up onto her face, getting her nice and covered by my jizz."
    show sasha_blow_facial
    "Sasha smiles up at me, batting her half-lidded eyes up in my direction."
    sasha.say "Enjoy this view, [hero.name]."
    "Sasha takes a finger and slips a drop of my cum off of her face."
    "She then wraps her lips around my cock, moaning in delight at the taste."
    $ sasha.flags.couchbj = True
    scene bg livingroom
    return

label sasha_zombietalk:
    mike.say "Okay, in no way is this movie based on a true story."
    sasha.say "It's a future true story."
    sasha.say "A zombie apocalypse is going to happen."
    sasha.say "I mean, studies show only one of us would survive."
    sasha.say "The question is, which one? Depends on survival strategy, you know?"
    sasha.say "Are we talking strength to fight them or ability to blend in and live amongst them?"
    sasha.say "All right, if we're gonna do ability to blend in, l say you."
    sasha.say "You are basically a zombie."
    sasha.say "Wake up at 7:00, shower, eat."
    sasha.say "Eh And, like a zombie, you don't really have any hopes or dreams."
    mike.say "I have dreams."
    sasha.say "Really?"
    $ result = renpy.display_menu([("Finding love", 1), ("Becoming rich", 2), ("Banging a lot of women", 3)])
    if result == 1:
        mike.say "Look, l'm looking for the love of my life."
        $ sasha.love -= 1
    elif result ==2:
        mike.say "Look, l'm going to be filthy rich."
        $ sasha.love += 1
    else:
        mike.say "Look, I'll fuck every woman I can."
    sasha.say "Oh, yeah, you seem to be doing just fine."
    mike.say "I can tell you who would die first in a zombie attack."
    mike.say "I mean, it's obviously you."
    mike.say "You are out of shape, have no marketable talents, and no survival skills."
    sasha.say "There are things in this world that you love."
    sasha.say "That slows people down."
    sasha.say "My cold, black heart and living without attachments to anyone or anything, that's my greatest asset right there."
    $ sasha.flags.zombietalk = True
    return

label sasha_bye(bye_outfit=None):
    call npc_bye_outfit (npc=sasha, bye_outfit=bye_outfit) from _call_npc_bye_outfit_19
    $ (day, h, activity, bye_outfit) = _return
    if not activity == sasha.activity:
        if day != game.week_day:
            $ sasha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ sasha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"sasha {bye_outfit}")
        if activity["activity"] == "sleep":
            sasha.say "I am smashed, I should go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            sasha.say "I'll go clean myself up now, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            sasha.say "I've got to run or I'll be late for work, bye."
        elif activity["activity"] in ["meal"]:
            sasha.say "I am starving, I'll go grab a bite!"
        elif activity["activity"] in ["tv"]:
            sasha.say "I am bored, I'll watch some tv I think."
        elif activity["activity"] in ["drink"]:
            sasha.say "I'll go to the pub and have a drink, see you around."
        elif activity["activity"] in ["sunbath"]:
            sasha.say "It's sunny today, I think I'll go laze around near the pool."
        elif activity["activity"] in ["shop"]:
            sasha.say "I feel like going shopping."
        elif activity["activity"] in ["dress"]:
            play voice "vo/sasha/bye.ogg"
            sasha.say "I'll go get dressed up."
        hide sasha
    return

label sasha_greet:
    $ renpy.log(f"sasha_greet ")
    if renpy.has_label(f"sasha_greet_dialogues_male") and not sasha.flags.greeted:
        scene expression f"bg {game.room}"
        show sasha talk
        $ sasha.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            play voice "vo/sasha/hello.ogg"
            sasha.say "Hello."
        elif result == 2:
            play voice "vo/sasha/hi.ogg"
            sasha.say "Hi, [hero.name]."
        else:
            if game.hour < 6:
                play voice "vo/sasha/hello.ogg"
                sasha.say "Hello [hero.name]."
            elif game.hour < 12:
                play voice "vo/sasha/good_morning.ogg"
                sasha.say "Good morning [hero.name]."
            elif game.hour < 19:
                play voice "vo/sasha/good_afternoon.ogg"
                sasha.say "Good afternoon [hero.name]."
            else:
                sasha.say "Good evening [hero.name]."
        call expression f"sasha_greet_dialogues_male" from _call_expression_263
        if sasha.flags.submissive_interact:
            sasha.say "I like my music, [hero.name] - but nothing rocks me like your cock!"
        hide sasha
    return

label sasha_greet_dialogues_male:
    if sasha.flags.mikeNickname:
        if game.hour < 6:
            mike.say "Hello my slave."
        elif game.hour < 12:
            mike.say "Good morning my slave."
        elif game.hour < 19:
            mike.say "Good afternoon my slave."
        else:
            mike.say "Good evening my slave."
    else:
        $ result = randint(1, 3)
        if result == 1:
            mike.say "Hello, Sasha."
        elif result == 2:
            mike.say "Hi."
        else:
            if game.hour < 6:
                mike.say "Hello."
            elif game.hour < 12:
                mike.say "Good morning Sasha."
            elif game.hour < 19:
                mike.say "Good afternoon Sasha."
            else:
                mike.say "Good evening Sasha."
    return

label sasha_kiss_male:
    scene expression f"bg {game.room}"
    if sasha.love < 25 and not sasha.is_girlfriend and not game.active_date.score >= 75:
        show sasha
        "It can be hard to read Sasha from one moment to the next."
        "Sometimes she's upbeat and fun, other times she can be pretty dark and even angry."
        sasha.say "Try that again and I'll cut your balls off."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        hide sasha
    elif not sasha.flags.kiss:
        hide sasha
        $ sasha.love += 5
        show sasha kiss
        "Sasha seems, for the most part, to work more on instinct than conscious thought."
        "And being around her, it kind of starts to rub off on you too."
        "That's why I hardly give it a second thought when I make to kiss her."
        "I guess I'm lucky that she's taken by surprise in a pleasant way, and lets me do so without objection."
        hide sasha kiss
        $ sasha.flags.kiss += 1
    else:
        hide sasha
        $ sasha.love += 2
        show sasha kiss
        "Sasha's quick to steal a kiss where and whenever the mood takes her."
        "But once she's sneaked what was supposed to be a small show of affection, it never seems to be enough."
        "And yes, her kisses are good enough to need me to get all poetic about them."
        hide sasha kiss
        $ sasha.flags.kiss += 1
    return

label sasha_ask_date_male:
    if Harem.find_by_name("band") and Harem.find_by_name("band").is_active(sasha):
        menu:
            "Ask Sasha on a date":
                call sasha_ask_date_alone_male from _call_sasha_ask_date_alone_male
            "Meet Kleio, Anna and Sasha for a 'hot coffee'" if Harem.together(anna, kleio, sasha, name="band"):
                mike.say "Do you want to get together with Anna and Sasha and have some fun?"
                sasha.say "I'd love to."
                call select_date_time from _call_select_date_time_11
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                menu:
                    "See you in your room":
                        if day == "now":
                            call kleioannafoursome from _call_kleioannafoursome_2
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome"))
                    "Let's meet in my room" if "kleioannafoursome2" in DONE:
                        if day == "now":
                            call kleioannafoursome2 from _call_kleioannafoursome2_3
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome2"))
                return
    else:
        call sasha_ask_date_alone_male from _call_sasha_ask_date_alone_male_1
    return _return

label sasha_ask_date_alone_male:
    mike.say "Sasha, would you like to go on a date with me?"
    if sasha.love < 50 or sasha.flags.nodate:
        sasha.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        sasha.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice

label sasha_walk_outside:
    scene bg livingroom
    mike.say "Okay, let's get you a little fresh air."
    "Sasha look at me in confusion as I stand up."
    "But a gentle yet firm tug on her lead convinces her to follow suit."
    show sasha naked leash
    "I walk her to the front door and open it wide, then gesture for her to step outside."
    menu:
        "Pet play at livingroom":
            call sasha_walk_livingroom from _call_sasha_walk_livingroom
        # "Take her to the park.":
        #     call sasha_walk_outside_park from _call_sasha_walk_outside_park
    $ game.pass_time(1)
    return

label sasha_walk_livingroom:
    scene bg livingroom
    show sasha naked
    show hand sasha
    mike.say "There you go - what are you waiting for?"
    "Sasha raises a tentative hand."
    mike.say "Speak."
    sasha.say "Please, [hero.name]...I don't understand..."
    scene sasha leash
    mike.say "What's not to understand?"
    mike.say "You're my bitch, you're wearing collar, and you're my pet."
    "I see recognition appear in Sasha's eyes."
    scene sasha leash02
    "Without needing to be told, she drops onto all fours and pulls eagerly on her leash."
    scene sasha leash03
    "..."
    scene bg livingroom
    return

label sasha_walk_outside_park:
    scene bg house
    show sasha naked leash
    "She eagerly walks out onto the sidewalk on all fours, and I almost forget to scan the street for signs of anyone watching."
    scene bg street
    show sasha naked leash
    "So hypnotic is the sight of her naked backside in motion and the occasional hint of breasts, swaying from side to side."
    hide sasha
    scene petplay
    show petplay walk sasha leash
    "Several times before we reach the gates of the park, I'm almost half sure that I can see hints of light as people jerk curtains."
    "It's the way I can't be sure if we're being watched or not that makes the thought so thrilling for me."
    "But if anyone is peeping through their drapes at me walking my most unusual pet tonight, they're not making a point of coming out to confront me about it."
    "It's too late for mundane dog-walkers as we finally walk off of the street and into the park."
    "Though I can hear the occasional noise that I'm sure can't be an animal every now and then."
    "There are no street lights in the park, and we seem to be insulated in our own little world of darkness as we find our way to a stand of trees."
    "Just then I hear the unmistakable sound of footsteps approaching quickly."
    "I glance over my shoulder in time to see a jogger pounding her way up the path towards where I'm standing."
    "I step neatly out of the way as she passes, giving her a polite smile."
    "But all the time I'm silently panicking, trying to resist the urge to glance over at Sasha for fear of drawing the eye of the jogger as well."
    "She gives me a brief glance and a smile, before she passes me and jogs off until she's out of sight."
    "Finally I can breathe out and look over towards where I last saw my bitch."
    "Shaken by the experience, but not wanting to show it to Sasha, I walk into the stand of trees and call for her to come to me."
    "She obey eagerly, making me think that either she missed the passing of the jogger entirely, or else did not and enjoyed the thrill of coming so close to being seen."
    show petplay stand sasha
    "It's then that I look up to see that she has a hand raised, asking permission to speak."
    mike.say "Alright, Sasha - what do you have to say?"
    sasha.say "Now that we've had our exercise and fun..."
    sasha.say "Would [hero.name] allow me to do something nice and fun for him?"
    "I look at Sasha's smile and her wide, innocent-seeming eyes."
    "Why shouldn't I indulge her?"
    "We've only seen one other person the entire time we've been out here, and now we're well and truly standing in amongst the trees."
    "Also, my nerves are getting pretty frayed around the edges."
    "I could do with something enjoyable to calm me down before we head back home."
    "I smile indulgently at Sasha and nod my assent."
    "In response, she claps her hands together and happily shuffles forwards until she's kneeling before me."
    show petplay stand sasha sashabj
    "Sasha sets about unzipping my flies and pulling out my cock, making small, excited noise as she does so."
    "It's cold in the spot where we're standing, and that sashaze returns now with a vengeance."
    show petplay stand sasha sashabj inside hold -sashatongueout
    "But as if she can sense the way in which the cold is making me a little uncomfortable, Sasha wastes no time in wrapping her lips around my dick."
    "I'm not yet fully aroused, but the wet, warm sensation of her tongue soon fixes that problem."
    "Watching Sasha's face as she literally coaxes my cock to being fully erect is an experience in and of itself."
    show petplay sashacloseeyes
    "As it grows, she's forced to maneuver around it and struggle to keep the entire thing inside of her mouth as much as possible."
    "Her almost stubborn determination to keep it from escaping her is almost as arousing as the feeling of the blowjob she's giving me at the same time."
    "Indeed, Sasha whines and pines whenever it looks like my dick is going to slip from between her lips."
    show petplay cumshot
    "I lose myself in Sasha's mouth, a trickle of my cum begins to seep from the corner of her mouth."
    show petplay stand sasha -sashabj sashaopeneyes sashaopeneyes sashatongueout nohold outside
    "I stand still and allow Sasha to push my cock back into my pants."
    show petplay walk sashahappy -cum
    "With her lead firmly back in my hand, I give her a firm but gentle tug, making her trot along almost perfectly at heel."
    "It doesn't take us long to walk the short distance back home, and there are even fewer signs of life along the way than there were earlier in the evening."
    return
return