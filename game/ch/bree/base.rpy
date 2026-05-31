init python:
    Activity(**{
    "name": "watch_tv_with_bree",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with [bree.name]",
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("fun", 0)),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities("watch_tv_with_everyone_male"),
        ],
    "max_girls": 1,
    "label": "bree_tv",
    })

    Activity(**{
    "name": "play_in_the_pool_with_bree",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with [bree.name]",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("male")),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        PersonTarget(sasha,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    "label": "bree_play_pool",
    })

    Event(**{
    "name": "bree_give_phone_number",
    "label": "give_phone_number",
    "girl": "bree",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(bree,
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
    "name": "bree_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(bree,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "bree",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_auto_greet",
    "label": "auto_greet",
    "girl": "bree",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_auto_chat",
    "label": "auto_chat",
    "girl": "bree",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "bree_are_you_sick",
    "label": "are_you_sick",
    "girl": "bree",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (bree, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_ask_out",
    "label": "ask_out",
    "girl": "bree",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "bree_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "bree_masturbation",
    "priority": 500,
    "label": "bree_masturbation",
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsGender("male"),
            IsActivity("knock_bedroom2")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_day": True,
    })

label bree_masturbation:
    $ hero.cancel_activity()
    "I'm only on my hands and knees because I dropped my phone, and I only dropped my phone because I tripped over my own feet."
    "And it's not my fault that I just happened to do all of this in the corridor outside of [bree.name]'s bedroom door either."
    "My honest intention is to do nothing more than scoop it up and get back to my feet."
    "But then I hear a sound coming from the other side of the door and realise how close I am to the keyhole."
    "I guess curiosity just gets the better of me, and before I know it, I'm kneeling in from of the door."
    "Putting my eye to the keyhole, I get a pretty good view of [bree.name]'s bedroom."
    "Although I quickly forget about everything else as soon as I see what's happening on the bed."
    "It's no great surprise to find out that the person laid upon the bed is [bree.name] herself."
    "But the fact that she's currently naked and in the middle of doing something rather intimate is enough to instantly root me to the spot."
    "[bree.name]'s reclining on her side, her legs pulled up so as to better spread her thighs and expose what lies between them."
    "It would be pretty obvious what she's up to, even if I couldn't see what's going on between her legs right now."
    "The flushed colour of her face and the intense sounds she's making would be more than enough to give it away."
    "I'd guess that I've stumbled upon [bree.name] just as she's building towards the climax of a pretty intense session of pleasing herself."
    show bree mast finger
    if bree.sub <= 25:
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        "I can't see any trace of toys or other means of getting herself off lying around within easy reach on the bed."
        "So it seems most likely that [bree.name]'s managed to get this far with only her own fingers and the power of her imagination."
        "I have to admit that, while I'm pretty into the idea of toys in the bedroom, it's quite a turn on to think she can get this worked up with no help whatsoever."
        "While one of her hand is playing with her pussy, the other busies itself by squeezing at the closest breast."
        "For a moment, I find my attention dragged away from the more obvious draw of the first hand, watching the movements of the second."
        "[bree.name] massages her breast as if hoping to somehow release the tension evident in her quivering body."
        "But at the same time, [bree.name]'s fingertips twist and pinch at her nipple."
        "And this seems to have the opposite effect, only making her moan with ever more intensity than before."
    elif bree.sub <= 50:
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        hide bree mast
        show bree mast dildo
        "A slippery, slithering sound alerts me to just what [bree.name]'s free hand is doing, as she produces a lubed-up dildo from somewhere amongst the sheets."
        "The folds of her pussy are already slick, and the dildo begins to sink between the lips almost the moment she begins to push it inside of her."
        "I'm almost as amazed at the sound that it makes as the sight of it, squeaking and squelching like rubber against rubber."
        "And accompanied by the moans that [bree.name] starts to make as she works the dildo in and out of herself, it's something I can't help but watch in fascination."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that [bree.name]'s stirring inside of herself is being expressed by what she's doing with the dildo."
        "I wish so much that it was my own cock inside of her right now that it almost hurts to keep on watching."
        "But there's no way that I'm going to miss out on seeing more because I'm jealous of a sex-toy!"
    elif bree.flags.anal:
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        "A slippery, slithering sound alerts me to just what [bree.name]'s free hand is doing, as she produces a lubed-up dildo from somewhere amongst the sheets."
        "For a moment, I fully expect her to use the hand already working her pussy to part them, so that she can push the dildo inside."
        hide bree mast
        show bree mast dildo ass
        "But then she surprises me by reaching around and actually beginning to shove the entire thing between her buttocks."
        "Though the angle from which I'm watching means I can't see the dildo go on, I can certainly hear the sucking, squelching sound as it does so."
        "And every inch of its progress is written on [bree.name]'s face, as she grimaces and moans at the sensation of it parting the muscles of her backside."
        "The deeper the toy goes, the more intensely she grimaces in delightful pain and rubs yet harder at her already tingling pussy."
        "By the time [bree.name]'s managed to work it in so deep that her fingers are touching her buttocks, there are actual tears welling in the corner of her eyes."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that [bree.name]'s stirring inside of herself is being expressed by what she's doing with the dildo."
    else:
        "As her fingers move quickly, stroking the visibly wet lips of her pussy, I can already hear her panting getting heavier by the second."
        "Compelled to stay right where I am and watch, I can't help wishing that I'd arrived sooner and seen more of what she did to get herself here."
        hide bree mast
        show bree mast dildo mouth
        "With her free hand, [bree.name] holds a sizable dildo up to her lips, licking and caressing the tip with her tongue."
        "Every twitch and twinge that her playing with herself creates, the further into her mouth she seems compelled to push the toy."
        "I never thought that I'd envy a plastic cock so much, but the sight of what she's doing to that thing is making me pine for the same treatment."
        "All of the passion and pleasure that [bree.name]'s stirring inside of herself is being expressed by what she's doing with the dildo."
        "By now she's taking more than half of it into her mouth with each thrust, moaning as she pushes her fingers into herself at the same time."
        "The fact that the sounds she's making are muffled by the dildo in her mouth only seems to make them that much more compelling too."
        "Still rubbing the lips of her pussy, her thumb almost grinding into her clit, [bree.name] almost pushes the dildo so far in that she's deep-throating it."
        "Part of me's worried that she's going to choke, but another is willing her on to see just how much she can swallow."
    hide bree mast
    show bree mast finger
    "I watch as [bree.name] bites her lip so hard that I expect to see her teeth draw blood."
    "And then she begins to roll her head, the locks of her long, blonde hair already becoming heavy ringlets thanks to the sweat upon her skin."
    "While I know that she's simply reacting to the pleasure overtaking her body, this motion of the head still makes [bree.name] appear to be almost delirious."
    "Once her head has been cast back, she seems to recline yet further, giving me a better view of her below the neck."
    "Now that I have almost the whole length of [bree.name]'s form spread out before me, it's hard to stifle the urge begin panting in sympathy."
    "Thinking that she's alone and unseen, she holds nothing back and does whatever it takes to reach her climax."
    "A part of me has to fight the urge to slip a hand into my own pants and copy her example, the sight of her is getting me that hot."
    "But when she finally cums, I can only watch as [bree.name] collapses onto her back."
    "She draws her legs up and curls into a foetal position on the bed, one hand still buried between her thighs."
    "As she falls silent, wrapped in her soaked sheets, I slowly become aware of my own heavy breathing as the only thing that I can still hear around me."
    "Even though she seems to be dead to the world, I'm nevertheless terrified of [bree.name]'s hearing me."
    "And so I hurry back to my room, still hunched over from the effects that my peeping on her has had on my body."
    return

label bree_propose_male:
    show bree
    "When the time finally comes to pop the question to [bree.name], I find myself pretty conflicted as to how I should go about it."
    "I wanted to avoid all the cliches and yet somehow still manage to include all of the really romantic stuff."
    "But in the end, I was in such a state of indecision, that I just decided today was the day, and stuffed the ring into my pocket."
    "I get [bree.name]'s attention, but I can't think of anything clever or original to say."
    "So I simply take her hand and get down on one knee, right then and there."
    mike.say "[bree.name]...will...will you marry me?"
    if bree.love < 195:
        show bree cry
        "[bree.name]'s eyes dart this way and that, noting that people are already starting to look in our direction."
        bree.say "What...are you actually serious?"
        mike.say "Erm...well...yeah, pretty much."
        mike.say "I mean...I have a ring and everything!"
        bree.say "Aw, that's so sweet, [hero.name]!"
        bree.say "But I can't marry YOU!"
        bree.say "Now get up - you're embarrassing me!"
        "Well, that could have gone better..."
        $ bree.love -= 25
        $ bree.sub -= 25
    else:
        show bree happy
        "[bree.name]'s face looks stunned at first, but soon breaks into a beaming expression of pure happiness."
        bree.say "Yes...yes, of course I will!"
        bree.say "Oh, [hero.name] - I thought you'd never ask!"
        "Well, that was easier than I expected it to be!"
        $ bree.set_fiance()
    hide bree
    return

label bree_cheated(action, cheat_npc=None):
    show bree
    if cheat_npc and Harem.together(cheat_npc, bree):
        show bree flirt
        bree.say "Can I get one too?"
        show bree kiss
        $ bree.flags.kiss += 1
        "And without warning [bree.name] kisses me."
        $ bree.love += 1
        hide bree kiss
    elif bree.sub >= 75:
        show bree flirt
        show fx heart
        $ bree.sub += 1
        "I see [bree.name] looking at me [action] someone else with envy and lust in her eyes."
    else:
        show bree sad
        show fx anger
        if cheat_npc:
            $ bree.flags.cheatedby = cheat_npc.id
        $ loss = 5
        if bree.flags.girlfriend or bree.flags.fiance:
            $ loss += 5
        $ bree.love -= loss
        "I see [bree.name] looking at me [action] someone else with tears in her eyes..."
    hide bree
    return

label bree_bye(bye_outfit=None):
    call npc_bye_outfit (npc=bree, bye_outfit=bye_outfit) from _call_npc_bye_outfit_5
    $ (day, h, activity, bye_outfit) = _return
    if not activity == bree.activity:
        if day != game.week_day:
            $ bree.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ bree.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"bree {bye_outfit}")
        if activity["activity"] == "sleep":
            bree.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            bree.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            bree.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            bree.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            bree.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            bree.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            bree.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            bree.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            bree.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            bree.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            bree.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            bree.say "I'll go get dressed."
        hide bree
    return

label bree_play_pool:
    show playing water pool bree
    "I recoil as a wave of water makes contact with my unsuspecting face."
    "[bree.name]'s laugh leaves no question as to what the cause was, so I return in kind, sending a large splash back to her."
    "The back and forth continues for a short while before we decide on a truce."
    "We spend the rest of our time in the pool peacefully."
    bree.say "Hehe, that was really fun!"
    bree.say "We should do it again sometime!"
    mike.say "Sure, no objections here."
    $ bree.love += 1
    $ bree.flags.greeted = TemporaryFlag(True, 1)
    return

label bree_tv:
    call bree_greet from _call_bree_greet
    if hero.charm >= 40 - bree.love or bree.activity_name == "tv":
        call watch_tv_with (bree) from _call_watch_tv_with_2
    else:
        show bree
        bree.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide bree
    return

label bree_tv_reaction:
    bree.say "Why not."
    return

label bree_porn_bad_reaction:
    bree.say "Sorry, I don't want to watch this sort of thing."
    return

label bree_tv_bj:
    show couch fun bree
    "[bree.name] wraps her fingers around my shaft and rolls her tongue out, licking up along my length."
    mike.say "O... oh wow..."
    mike.say "It feels so good."
    bree.say "I kind of knew this would please you."
    "Again, she licks up my shaft, up over the glans and over the tip."
    "What did I do to deserve the greatest roommate in the world?"
    "I wonder this as the excitement of her actions tingles up through my body."
    show couch fun bree cumshot
    "I can't hold back and, with a groan, I release, shooting up onto her."
    "Cum sprays up onto her face, getting her nice and covered by my jizz."
    hide couch
    show couch fun bree facial
    "[bree.name] smiles up at me, batting her half-lidded eyes up in my direction."
    bree.say "Enjoy this view, [hero.name]."
    "[bree.name] takes a finger and slips a drop of my cum off of her face."
    "She then wraps her lips around my cock, moaning in delight at the taste."
    hide couch
    $ bree.flags.couchbj = True
    $ bree.flags.bj += 1
    return

label bree_greet:
    if renpy.has_label(f"bree_greet_dialogues_{hero.gender}") and not bree.flags.greeted:
        scene expression f"bg {game.room}"
        show bree
        $ bree.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            bree.say "Hello, [hero.name]."
        elif result ==2:
            bree.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                bree.say "Good morning [hero.name]."
            elif game.hour < 19:
                bree.say "Good afternoon [hero.name]."
            else:
                bree.say "Good evening [hero.name]."
        call expression f"bree_greet_dialogues_{hero.gender}" from _call_expression_524
        if bree.flags.submissive_interact:
            if randint(0, 1) == 0:
                bree.say "Hey, [hero.name] - can I play with YOUR joystick today?"
            else:
                bree.say "Will you let me play with it [hero.name]..."
                bree.say "Will you let me play with your joystick?"
        hide bree
    return

label bree_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, [bree.name]."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello [bree.name]."
        elif game.hour < 12:
            mike.say "Good morning [bree.name]."
        elif game.hour < 19:
            mike.say "Good afternoon [bree.name]."
        else:
            mike.say "Good evening [bree.name]."
    return

label bree_kiss:
    scene expression f"bg {game.room}"
    if bree.love + hero.charm < 80 and not bree.is_girlfriend and not game.active_date.score >= 75:
        show bree
        "[bree.name] quickly takes a step back, and turns away."
        if bree.love < 40:
            bree.say "Sorry but... I don't really feel comfortable with that."
            $ bree.sub += 1
        else:
            $ result = randint(1, 2)
            if result == 1:
                bree.say "Sorry, but let's just not."
                $ bree.love -= 1
            else:
                bree.say "I'm sorry, but I have to go..."
            "Before I can react, [bree.name] turns and rushes away."
        hide bree
    elif bree.love + hero.charm < 60 or game.active_date.score >= 75:
        hide bree
        if bree.lesbian > MAX_LES_GUY_SEX:
            $ bree.lesbian -= 1
        show bree kiss
        if not bree.flags.kiss:
            $ bree.love += 5
            "I watch [bree.name]'s eyes open wide in surprise, and for a moment I think she might back away, or even run, but slowly her eyelids close as she cautiously returns the affection."
            "Her lips are remarkably soft, I can even taste a hint of strawberry as we meet."
            "My own eyes drift shut, and we only hold together for a brief moment, but there's no denying its simply wonderful."
            "No matter what comes next, something tells me that I will never forget this moment."
            hide bree kiss
            if bree.love >= 60:
                show bree
                bree.say "Um, I think we should talk about this later, alright?"
            else:
                show bree
                bree.say "Oh uh... I've got to go..."
                "Before I can object, [bree.name] begins in the opposite direction."
                "She seemed a little uncomfortable, did I do something wrong?"
        else:
            $ bree.love += 2
            "I take a step closer to [bree.name], and rest my hands lightly on her shoulder."
            "For a brief moment she looks curious, but I catch sight of a moment of recognition in her eyes before my own drift shut."
            "I stop just short of meeting her lips, letting her lean forwards to meet mine, and letting her soft lips dance across mine at her pace."
            "Once again I taste strawberries, before she eventually pulls back, and I move my arms away."
            "I catch a glimpse of a small smile playing on her lips before she tries to hide it, a blush covering her complexion."
            hide bree kiss
        $ bree.flags.kiss += 1
    else:
        hide bree
        show bree kiss
        if not bree.flags.kiss:
            $ bree.love += 5
            "I feel my lips passing over [bree.name]'s as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
            "As is, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling [bree.name] with my tongue."
            "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
            "I let myself inside her, exploring every crevice of her mouth in earnest even if she herself seems hesitant to return the treatment."
            "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
            "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            hide bree kiss
            if bree.love >= 60:
                show bree flirt blush
                bree.say "Wow... Um, that was... Different."
                "I catch a small smile dancing upon her face through the thick blush that adorns her cheeks, letting me know without a shadow of a doubt that it was the good kind of different."
            else:
                show bree flirt blush
                bree.say "Um... I should go..."
                "Before I can object, [bree.name] turns and quickly flees the scene, leaving me wondering what I did wrong."
        else:
            $ bree.love += 2
            if randint(1, 2) == 2:
                "Yet again I feel my lips passing over [bree.name]'s as we embrace, my hands resting comfortably on her hips while her own had ventured to my shoulders, looping around my neck."
                "Today however, I feel particularly adventurous, and not only do I push into her embrace more than I have in the past, but also begin lightly tickling [bree.name] with my tongue."
                "For a moment, I'm not sure if she'll reciprocate, but I feel her lips parting and allowing me access."
                "I let myself inside her, my organ exploring every crevice of her mouth in earnest even if she herself seemed hesitant to return the treatment."
                "I let my eyes open to gauge her reaction, and although she seems rather tense, my ears pick up on a soft whimper of pleasure that tells me she's at least enjoying the treatment."
                "My eyes drift closed once more, and before long we part, although I can still taste her on my tongue."
            else:
                "Once again I step in closer to [bree.name], close enough that our bodies are very nearly touching."
                "I bring one hand to [bree.name]'s chin, tilting her up to face me as I lean down to let our lips meet, the familiar taste of strawberry yet again facing me."
                "My tongue yet again pushes through the barrier that her lips form to begin exploring [bree.name]'s mouth, while she cautiously met me, letting me lead the dance our tongues engaged in."
                "Before long, we pulled away from one another, breathless."
            hide bree kiss
            if hero.charm >= 160 - bree.love and bree.love < 50:
                show bree flirt blush
                bree.say "Stop doing that."
            else:
                show bree flirt blush
                bree.say "Thank you [hero.name]."
        $ bree.flags.kiss += 1
        hide bree
    return

label bree_gift_signed_fantasy_book_male:
    call bree_greet from _call_bree_greet_2
    show bree
    bree.say "Is that what I think?"
    show bree happy
    bree.say "Wow, and it's signed!"
    bree.say "That's the best gift ever!!!"
    $ bree.love += 5
    "She jumps in my arms."
    bree.say "Thank you so much [hero.name]!"
    hide bree
    return

label bree_walk_outside:
    scene bg livingroom
    mike.say "Okay, let's get you a little fresh air."
    "[bree.name] look at me in confusion as I stand up."
    "But a gentle yet firm tug on her lead convinces her to follow suit."
    show bree naked leash
    "I walk her to the front door and open it wide, then gesture for her to step outside."
    menu:
        "Take her out in the garden.":
            call bree_walk_outside_garden from _call_bree_walk_outside_garden
        "Take her to the park.":
            call bree_walk_outside_park from _call_bree_walk_outside_park
    $ game.pass_time(1)
    return

label bree_walk_outside_garden:
    scene bg livingroom
    show bree naked
    show hand bree
    mike.say "There you go - what are you waiting for?"
    "[bree.name] raises a tentative hand."
    mike.say "Speak."
    bree.say "Please, [hero.name]...I don't understand..."
    mike.say "What's not to understand?"
    mike.say "You're my bitch, you're wearing collar, and you need the bathroom."
    "I see recognition appear in [bree.name]'s eyes."
    "Without needing to be told, she drops onto all fours and pulls eagerly on her leash, whining to be allowed outside."
    hide bree
    hide hand
    scene petplay
    show petplay walk bree leash
    "Not willing to be outdone by her, I walk the [bree.name] out of the front door into the garden."
    "Luckily for us, there aren't many lights on the neighborhood windows."
    "That means that only I get to see the spectacle of [bree.name] hunting on her hands and knees for an agreeable spot amongst the flowerbeds."
    "[bree.name] quickly relieve herself too."
    show petplay stand breepee breecloseeyes bree
    mike.say "Finished?"
    show petplay stand -breepee breeopeneyes bree
    "[bree.name] nod happily, not fazed in the least by the experience."
    "Shaking my head, and more than a little turned-on, I lead her back along the street to the house, usher her inside and lock the door."
    return

label bree_walk_outside_park:
    scene bg house
    show bree naked leash
    "She eagerly walks out onto the sidewalk on all fours, and I almost forget to scan the street for signs of anyone watching."
    scene bg street
    show bree naked leash
    "So hypnotic is the sight of her naked backside in motion and the occasional hint of breasts, swaying from side to side."
    hide bree
    scene petplay
    show petplay walk bree leash
    "Several times before we reach the gates of the park, I'm almost half sure that I can see hints of light as people jerk curtains."
    "It's the way I can't be sure if we're being watched or not that makes the thought so thrilling for me."
    "But if anyone is peeping through their drapes at me walking my most unusual pet tonight, they're not making a point of coming out to confront me about it."
    "It's too late for mundane dog-walkers as we finally walk off of the street and into the park."
    "Though I can hear the occasional noise that I'm sure can't be an animal every now and then."
    "There are no street lights in the park, and we seem to be insulated in our own little world of darkness as we find our way to a stand of trees."
    "Just then I hear the unmistakable sound of footsteps approaching quickly."
    "I glance over my shoulder in time to see a jogger pounding her way up the path towards where I'm standing."
    "I step neatly out of the way as she passes, giving her a polite smile."
    "But all the time I'm silently panicking, trying to resist the urge to glance over at [bree.name] for fear of drawing the eye of the jogger as well."
    "She gives me a brief glance and a smile, before she passes me and jogs off until she's out of sight."
    "Finally I can breathe out and look over towards where I last saw my bitch."
    "Shaken by the experience, but not wanting to show it to [bree.name], I walk into the stand of trees and call for her to come to me."
    "She obey eagerly, making me think that either she missed the passing of the jogger entirely, or else did not and enjoyed the thrill of coming so close to being seen."
    show petplay stand bree
    "It's then that I look up to see that she has a hand raised, asking permission to speak."
    mike.say "Alright, [bree.name] - what do you have to say?"
    bree.say "Now that we've had our exercise and fun..."
    bree.say "Would [hero.name] allow me to do something nice and fun for him?"
    "I look at [bree.name]'s smile and her wide, innocent-seeming eyes."
    "Why shouldn't I indulge her?"
    "We've only seen one other person the entire time we've been out here, and now we're well and truly standing in amongst the trees."
    "Also, my nerves are getting pretty frayed around the edges."
    "I could do with something enjoyable to calm me down before we head back home."
    "I smile indulgently at [bree.name] and nod my assent."
    "In response, she claps her hands together and happily shuffles forwards until she's kneeling before me."
    show petplay stand bree breebj
    "[bree.name] sets about unzipping my flies and pulling out my cock, making small, excited noise as she does so."
    "It's cold in the spot where we're standing, and that breeze returns now with a vengeance."
    show petplay stand bree breebj inside hold -breetongueout
    "But as if she can sense the way in which the cold is making me a little uncomfortable, [bree.name] wastes no time in wrapping her lips around my dick."
    "I'm not yet fully aroused, but the wet, warm sensation of her tongue soon fixes that problem."
    "Watching [bree.name]'s face as she literally coaxes my cock to being fully erect is an experience in and of itself."
    show petplay breecloseeyes
    "As it grows, she's forced to maneuver around it and struggle to keep the entire thing inside of her mouth as much as possible."
    "Her almost stubborn determination to keep it from escaping her is almost as arousing as the feeling of the blowjob she's giving me at the same time."
    "Indeed, [bree.name] whines and pines whenever it looks like my dick is going to slip from between her lips."
    show petplay cumshot
    "I lose myself in [bree.name]'s mouth, a trickle of my cum begins to seep from the corner of her mouth."

    show petplay stand bree -breebj breeopeneyes breetongueout nohold outside
    "I stand still and allow [bree.name] to push my cock back into my pants."
    show petplay walk breehappy -cum
    "With her lead firmly back in my hand, I give her a firm but gentle tug, making her trot along almost perfectly at heel."
    "It doesn't take us long to walk the short distance back home, and there are even fewer signs of life along the way than there were earlier in the evening."
    return

label bree_ask_date_male:
    if Harem.find(bree):
        menu:
            "Ask [bree.name] on a date":
                call bree_ask_date_alone_male from _call_bree_ask_date_alone_male
            "Meet [bree.name] and Kat" if Harem.find_by_name("gaming") and Harem.together(bree, kat, name="gaming"):
                call bree_ask_date_kat from _call_bree_ask_date_kat
    else:
        call bree_ask_date_alone_male from _call_bree_ask_date_alone_male_1
    return _return

label bree_ask_date_alone_male:
    mike.say "[bree.name], would you like to go on a date with me?"
    if bree.flags.nodate:
        bree.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        bree.say "Sure, it might be fun, when do you want us to go?"
        return True

label bree_ask_date_kat:
    $ renpy.dynamic("date_choice")
    mike.say "Do you want to get together with Kat and have some fun?"
    bree.say "I'd love to."
    if "gaming_harem_event_04" in DONE:
        bree.say "Do you want to do something special?"
        menu:
            "Gaming cumpetition":
                $ date_choice = "gaming_harem_cumpetition_intro"
            "Simple fooling around":
                $ date_choice = "gaming_harem_threesome_intro"
    else:
        $ date_choice = "gaming_harem_threesome_intro"
    call select_date_time from _call_select_date_time_29
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call expression date_choice from _call_expression_517
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "gaming", ["bree", "kat"], date_choice))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
