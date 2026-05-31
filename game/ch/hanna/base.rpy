init python:
    Event(**{
    "name": "hanna_give_phone_number",
    "label": "give_phone_number",
    "girl": "hanna",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(hanna,
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
    "name": "hanna_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(14, 15),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(hanna,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "hanna",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "hanna_auto_greet",
    "label": "auto_greet",
    "girl": "hanna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(hanna,
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
    "name": "hanna_auto_chat",
    "label": "auto_chat",
    "girl": "hanna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(hanna,
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
    "name": "hanna_are_you_sick",
    "label": "are_you_sick",
    "girl": "hanna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (hanna, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "hanna_ask_out",
    "label": "ask_out",
    "girl": "hanna",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(hanna,
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
    "name": "hanna_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "hanna",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(hanna,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label hanna_bye(bye_outfit=None):
    call npc_bye_outfit (npc=hanna, bye_outfit=bye_outfit) from _call_npc_bye_outfit_9
    $ (day, h, activity, bye_outfit) = _return
    if not activity == hanna.activity:
        if day != game.week_day:
            $ hanna.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ hanna.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"hanna {bye_outfit}")
        if activity["activity"] == "sleep":
            hanna.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            hanna.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            hanna.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            hanna.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            hanna.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            hanna.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            hanna.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            hanna.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            hanna.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            hanna.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            hanna.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            hanna.say "I'll go get dressed."
        hide hanna
    return

label hanna_cheated(action, cheat_npc=None):
    show hanna
    if cheat_npc and Harem.together(cheat_npc, hanna):
        show hanna flirt
        hanna.say "Aren't you forgetting something?"
        show hanna
        "And without warning Hanna kisses me."
        $ hanna.love += 1
        $ hanna.flags.kiss += 1
    elif hanna.sub >= 75:
        show hanna flirt
        show fx heart
        $ hanna.sub += 1
        "I see Hanna looking at me [action] someone else with envy and lust in her eyes."
    else:
        show hanna sad
        $ loss = 5
        if hanna.flags.girlfriend or hanna.flags.fiance:
            $ loss += 5
        $ hanna.love -= loss
        "I see Hanna looking at me [action] someone else with a painful hurting face..."
    hide hanna
    return

label hanna_greet:
    if renpy.has_label(f"hanna_greet_dialogues_{hero.gender}") and not hanna.flags.greeted:
        scene expression f"bg {game.room}"
        $ hanna.flags.greeted = TemporaryFlag(True, 1)
        show hanna
        $ result = randint(1, 4)
        if result == 1:
            hanna.say "Hello, [hero.name]."
        elif result == 2:
            hanna.say "Hi, [hero.name]."
        elif result == 3:
            hanna.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                hanna.say "Good morning [hero.name]."
            elif game.hour < 19:
                hanna.say "Good afternoon [hero.name]."
            else:
                hanna.say "Good evening [hero.name]."
        call expression f"hanna_greet_dialogues_{hero.gender}" from _call_expression_228
        if hanna.flags.submissive_interact:
            if randint(0, 1) == 0:
                hanna.say "Walk me down the street like a dog, [hero.name] - show me off like the bitch I am!"
            else:
                hanna.say "Seeing you makes me, kind of hot, I guess."
                hanna.say "I really want to show you more, right here.."
        hide hanna
    return

label hanna_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Hanna."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Hanna."
        elif game.hour < 12:
            mike.say "Good morning Hanna."
        elif game.hour < 19:
            mike.say "Good afternoon Hanna."
        else:
            mike.say "Good evening Hanna."
    return

label hanna_kiss:
    scene expression f"bg {game.room}"
    if hanna.love + hero.charm < 80 and not hanna.is_girlfriend and not game.active_date.score >= 75:
        show hanna
        "I've spent so much time looking longingly at Hanna, devouring the curves and lines of her astonishing body."
        "I've also been aware for a good amount of that time just how much she enjoys having my eyes upon her."
        "So it comes as some surprise, how she reacts when I see a chance to kiss her and try to take it."
        "When she recoils, pulling herself away and out of reach, I can't help but be confused."
        "What was she hoping to achieve by flaunting herself in front of me like that?"
        "But whatever it was, I seem to have made a real error of judgement in taking it as an invitation to kiss her!"
        $ hanna.love -= 1
        hide hanna
    elif not hanna.flags.kiss:
        $ hanna.flags.kiss += 1
        if hanna.lesbian > MAX_LES_GUY_SEX:
            $ hanna.lesbian -= 1
        "I've been imagining this moment for almost the whole time that I've spent looking longingly at Hanna."
        "She knows full well that I've been watching her, and I know that she likes that fact too."
        "We've been playing a kind of game with each other for so long now, I feel I have to see if it can go further."
        hide hanna
        show hanna kiss
        $ hanna.love += 5
        "And luckily for me, the gamble pays off, as Hanna doesn't resist me leaning in to kiss her on the lips."
        "My mind's already filled with desire for her body, and all of that makes kissing her crazily intense."
        "It's as if all of the thrill tied up in her stunning form is instantly summed up in that one gesture."
        "In short - it's one hell of a kiss!"
        hide hanna kiss
    else:
        $ hanna.flags.kiss += 1
        hide hanna
        if hanna.lesbian > MAX_LES_GUY_SEX:
            $ hanna.lesbian -= 1
        show hanna kiss
        "Before I'd only get a knowing sideways look and a cheeky smile from Hanna when she knew I was watching her."
        "But now she greets my admiring glances with an expression that affects me almost as much as her beautiful body too."
        "And it's almost as if every kiss that she grants me afterwards is a reward for giving her all of my attention."
        "It doesn't take me long to become pretty much addicted to these all too fleeting shows of affection."
        "And at times I feel almost like a dog, begging for her attention and rushing when called."
        "Not that I could stop, even if I wanted to!"
        hide hanna kiss
        hide hanna
        $ hanna.love += 2
    return

label hanna_kiss_me:
    "I'm so used to watching Hanna as she makes an obvious show of herself for my attention, that I don't even sense what she's about to do."
    "My eyes are too busy following the curves of her hypnotic body to see that she's coming closer with each second that passes."
    "Soon she's close enough to reach out and touch me, which she doesn't hesitate to do."
    "The body that I've spent ages worshipping in my mind pulls me close to it, embracing me."
    "And she's kissing me before I realise just what's happening."
    "And as for the kiss - that's so good it does nothing to bring me back to my senses."
    "If it's a dream, then I'm not even going to try to wake up."
    return

label hanna_walk_outside:
    scene bg livingroom
    hanna.say "Hey, [hero.name]..."
    hanna.say "It's that time of day again!"
    "At the sound of Hanna's voice, I look up from what I'm doing quite casually."
    "But the moment that I lay eyes on her, I leap up, almost standing to attention."
    "And that's because she's completely naked!"
    show hanna naked
    "Well, save for the collar around her neck of course..."
    "Hanna has the leash that matches the collar in her hand, swinging it casually."
    hanna.say "What are you waiting for?"
    hanna.say "You've got to take me to the park for some exercise!"
    "That said, Hanna tosses me the lead and I catch it clumsily."
    "She giggles at my fumbling around, then gets down on all fours."
    mike.say "S...sure thing, Hanna..."
    mike.say "Just let me get you on the leash..."
    "I hurry over, still fumbling with the leash."
    "And it's harder than I expect to bend down and clip it to her collar."
    "I mean, you try doing it with an erection the size of the one she's giving me right now!"
    "Hanna makes matters worse by waggling her ass and sticking her tongue out too."
    "I know that she's doing the best she can to get into the spirit of this thing."
    "But all it makes me want to do is drop my pants and fuck her - right here and now!"
    mike.say "Ah...ahem..."
    mike.say "There we go...good girl."
    hanna.say "Mmm..."
    hanna.say "I like it when you call me that!"
    hanna.say "It makes me want to be the best girl ever!"
    if "cassidy_sub_01" in DONE and "cassidy_sub_02b" not in DONE and not cassidy.flags.agree_walk_outside and not cassidy.hidden:
        call cassidy_sub_02b from _call_cassidy_sub_02b
        return
    "I hurry to open the front door, giving the leash a gentle tug as I do so."
    scene petplay
    show petplay walk hanna leash
    "Hanna obediently trots out after me, walking on all fours the whole time."
    "Luckily for me, it's late enough for everyone else to be tucked up in bed."
    "And if they're not, my neighbourhood is pretty quiet at this time too."
    "Nobody's likely to be peeking around the curtains while we do this thing."
    "Even if they are, I've already planned out a safe route to the park."
    "One that takes us away from the street lights and major roads."
    "With any luck, I'll just look like someone walking a dog anyway."
    mike.say "Come on, girl."
    mike.say "We're not going to get to the park hanging around here!"
    "Hanna nods happily at this, already beginning to walk down the street."
    "I'm not ready for this, and so she jerks me forwards after her."
    "It takes me jogging a few steps to catch up."
    "And even then I'm still walking at a pretty quick pace."
    "I'm amazed at how strong Hanna actually is."
    "That and how fast she can move on all fours!"
    "I know that she practically lives in the gym."
    "But this is crazy!"
    "At the pace Hanna's setting, we make it to the park in record time."
    "And when we do, I'm thinking that we'll take a leisurely walk around the place."
    "But suddenly I feel Hanna pulling me towards the closest expanse of grass."
    hanna.say "Come...on...[hero.name]..."
    show petplay walk hanna leash hannahappy

    if randint(0, 1) == 0:
        hanna.say "I wanna...go play...fetch!"
        "I don't know if all of this is just Hanna putting on an act for my benefit."
        "Or else she's totally getting into the idea of me treating her like a dog."
        "Either way, she's going to yank my arm out of its socket at this rate!"
        "That is unless I make a decision right now..."
        menu:
            "Play fetch with Hanna":
                "Hanna's enthusiasm is infectious, and I just can't resist her."
                show petplay stand hanna
                "So I give in and let her pull me onto the grass."
                "She seems to sense that she's getting her own way."
                "And I have to pick up the pace just to keep from getting tripped up!"
                mike.say "Hey..."
                mike.say "Wait up..."
                "At the sound of my voice, Hanna stops pulling on the leash."
                "She looks back over her shoulder at me, a surprised look on her face."
                hanna.say "Wha...what?"
                hanna.say "Did I do something bad?"
                "I give her what I hope is a reassuring smile as I shake my head."
                mike.say "No, Hanna..."
                mike.say "Well, maybe a little mischievous!"
                mike.say "Now, where did I put that ball..."
                "I let Hanna off the lead before I search for it."
                "And then I pull the tennis ball I brought with me out of my pocket."
                "At the mere sight of it, Hanna seems to go crazy."
                "She's nodding as she scuttles back and forth in front of me."
                "And she even has her tongue hanging out of her mouth too!"
                hanna.say "Oh yeah!"
                hanna.say "Oh yeah, yeah, yeah!"
                mike.say "Here you go, girl!"
                mike.say "Go fetch!"
                "I throw the ball as far and as fast as I can."
                show petplay stand -hanna -leash
                "And I swear that Hanna's off before it even leaves my hand!"
                "My eyes are wide as I marvel at the sight of her running on all fours."
                "Somehow she manages to get up to an amazing speed as she chases the ball."
                "Sure, she's not fast enough to catch it on the first bounce."
                "But she manages it on the second, clamping her teeth around the ball."
                "As soon as she has a firm hold on it, Hanna comes hurtling back towards me."
                "She only just manages to stop herself before she collides with my legs."
                "Then she drops the ball at my feet, pushing it forwards with the tip of her nose."
                show petplay stand hanna
                "I almost forget to pick the ball up and throw it for a second time."
                "But can you blame me when Hanna's got her ass in the air like that?"
                "If she had a tail, it's be wagging like crazy right now!"
                hanna.say "Hmm..."
                hanna.say "Come on!"
                hanna.say "Throw the ball already!"
                "Oh shit..."
                "Now she's whining and looking at me with those big, sad eyes!"
                "I don't think I've ever wanted to fuck this girl so badly!"
                "Somehow I force myself to throw the ball again."
                "And Hanna tears off after it a second time."
                "After that the whole thing becomes a little easier each time."
                "I still feel massively turned-on, but I can keep a lid on it."
                show petplay walk hanna leash
                "When Hanna finally looks like she's getting tired, I put her back on the lead."
            "Make Hanna walk to heel":
                "I think it's about time that I started putting as much into this as Hanna."
                "And the best way I can think of doing that is to treat her like a dog."
                "Or to be more specific, the exact kind of dog that she's pretending to be."
                "So I take a firmer hold of the leash."
                "Not enough to choke Hanna or hurt her."
                "Just enough to stop her from pulling me closer to the grass."
                mike.say "No, Hanna..."
                mike.say "Bad girl!"
                "At the sound of my voice, Hanna stops pulling on the leash."
                "She looks back over her shoulder at me, a surprised look on her face."
                show petplay stand hanna
                hanna.say "Wha...what?"
                hanna.say "Did I do something bad?"
                "I give her what I hope is a reassuring smile as I shake my head."
                mike.say "No, Hanna, just naughty."
                mike.say "Now if you want to be a good girl, then walk to heel, okay?"
                "Hanna's eyes light up at the chance to redeem herself."
                "And she waits obediently for me to give her my next instruction."
                mike.say "Walk on, Hanna."
                mike.say "There's a good girl!"
                show petplay walk hanna leash
                "Before I know it, we're doing just that."
                "Hanna keeps pace at my heel as we stroll around the park."
                "Whenever I look down at her, she beams back up at me too."
                "And I don't miss the chance to appreciate her being on show either."
                "Hanna's body moves like poetry in motion, even though she's on all fours."
                "Her pert buttocks practically bounce and her breasts sway in a delightful way."
                "In fact, I'm so busy watching her that I forget I'm supposed to be taking the lead."
                "This means that I almost walk straight into a tree."
                "But at the last moment, Hanna pulls on her leash."
                "I regain my senses, thinking that she's misbehaving again."
                "And then I see the tree trunk a few inches from my face."
                mike.say "Whoa..."
                mike.say "Thanks, Hanna!"
                show petplay stand hanna leash
                hanna.say "No worries, [hero.name]."
                hanna.say "Just being the best dog I can be!"
    else:
        hanna.say "Won't you let me play with your stick?"
        show petplay stand hannatongueout
        "As if she needs to underline the point, Hanna begins to paw at my zipper..."
        menu:
            "Stop her":
                "I glance around nervously, scanning the surrounding area for any signs of life."
                "There's nothing immediately obvious, but I feel like I'm tempting fate if I say yes."
                mike.say "No, bad dog!"
                show petplay stand hannatongueout hannacloseeyes
                mike.say "Now you do as you're told."
                mike.say "Or else I'll make you sleep out in the back yard tonight!"
                "Hanna whines some more, but then lowers her head and nods meekly."
                "I give a tug on the leash, and she obediently walks to heel once more."
                show petplay walk leash
                "We make it back to my place quicker than we did to the park."
                "And as soon as the door is closed behind us, I can breathe a sigh of relief."
                $ hanna.sub += 1
            "Let her continue":
                "I glance around nervously, scanning the surrounding area for any signs of life."
                "There's nothing immediately obvious, and so I think to hell with it."
                "Unzipping my flies, I give Hanna permission to do her worst."
                mike.say "Okay, there you go."
                mike.say "You've been a good dog tonight."
                mike.say "So you deserve a reward!"
                show petplay stand hannabj outside hold
                "Hanna claps her hands together in glee at this, practically bouncing up and down on the spot."
                "And then she reaches into my open flies with one hand, gently pulling out my cock."
                "It's never been less than halfway stiff the whole time that we've been on this strange, late night walk."
                "So it only takes a little bit of her handling it to go the whole way and get really hard."
                "Perhaps sensing this, or maybe that we're out in a public place, Hanna doesn't take her time."
                show petplay stand hannabj inside hold
                "Instead she takes my cock straight into her mouth, dispensing with the foreplay and getting down to business."
                "This means that the job she does is rough and without her usual flair."
                "But under the rather unique circumstances, it works out just fine."
                "Hanna swallows me as far as she can, sloppily working it in and out as she does so."
                "The sound is something quite atrocious, but the sensation is out of this world."
                show petplay stand hannacloseeyes
                "Pretty soon her head is bobbing back and forth at quite some speed."
                "And I can already feel the urge to cum building up inside of me."
                "All the time I keep on looking this way and that, searching the darkness around us."
                "Suddenly I hear something that I'm certain must be another human being approaching."
                "Which is all I need to lose myself inside of Hanna's mouth!"
                show petplay stand hannabj inside cumshot hannaopeneyes
                "Unprepared for the premature ejaculation, she coughs and gags at it hits the back of her throat."
                "Whereas I'm too preoccupied with pulling my cock out of her mouth and stuffing it back into my pants to help her."
                show petplay stand hannabj outside hannaswallow
                "But almost as soon as the panic begins it's over again."
                "And I realise that what I heard must have been an animal or merely the wind in trees above."
                "As soon as she's done choking, Hanna looks up at me and lets out a questioning whine."
                "I smile and give her a pat on the head, which seems to do the trick, as she smiles happily."
    mike.say "I think we've both had enough exercise for the night, Hanna."
    mike.say "Time we were heading home, okay?"
    show petplay walk hanna leash hannahappy
    "Hanna nods eagerly, coming instantly to heel."
    "I pat her on the head without thinking."
    "But she seems to actually enjoy me doing so."
    "I make a mental note of that as we walk towards the entrance to the park."
    "And I also commit as much of the sight of her on the leash as I can to memory."
    "That way I can recall it later when I'm on my own and have some time on my hands."
    $ hanna.love += 2
    $ hanna.sub += 1
    return

label hanna_propose_male:
    show hanna
    "I've never done anything like this before, so I feel like I'm a bag of nerves."
    "But I just keep on telling myself that I have to go through with this thing."
    "Because I've never felt what I feel for Hanna with any other girl in my life!"
    "I just can't get enough of her, even now that we've been dating for a while."
    "Whenever I get the chance, I'm always hitting the gym just to see her."
    "Which means that my obsession is also making me fitter than ever!"
    "I know that I have to do something to take our relationship to the next level."
    "I have no idea if Hanna's thinking along the same lines as me."
    "But I do know that I'll go mad if I don't do something about it."
    "So I've armed myself with a ring, and I'm just waiting for my chance."
    "Hanna doesn't seem to notice anything's up."
    "She's just chatting away as normal."
    "Talking about everything and nothing all at once."
    "Which means that I can pretty much choose my moment."
    "So when she finally pauses for breath, I make my move."
    "I get down on one knee, pulling out the box that contains the ring."
    hanna.say "So I was like..."
    show hanna annoyed
    hanna.say "Erm, [hero.name]..."
    hanna.say "What are you doing down there?"
    "I pop the box open, making sure that Hanna sees the ring."
    "And the moment she does, her eyes go wide."
    mike.say "Hanna..."
    mike.say "I have something to ask..."
    mike.say "Will you marry me?"
    "Hanna has one hand over her mouth, so I can't read her lips."
    show hanna normal
    "She also seems to be nodding one moment, then shaking her head the next!"
    "I have a smile on my face."
    "But as the seconds turn into minutes, it begins to feel a little forced."
    mike.say "Ah, Hanna..."
    mike.say "I'm kind of waiting for an answer here!"
    "Hanna glances around, seeing that people are starting to stare at us."
    "She's usually eager to be the centre of attention wherever we go."
    "But it looks like we finally found a scenario in which she doesn't."
    "I guess this is the wrong kind of attention."
    "And I can see people starting to get their phones out to film us."
    "Hanna better come up with an answer soon."
    "Or else we're going to be trending online."
    "And it'll be one of those cringe-inducing videos that always go viral too!"
    hanna.say "I...I..."
    if hanna.love < 195:
        hanna.say "I'm sorry, [hero.name]..."
        show hanna sad
        hanna.say "But I just can't marry you."
        hanna.say "Not right now, anyway!"
        "I can't quite believe what I'm hearing."
        "Which is why I put the ring away and get to my feet slowly."
        "My movements are stiff and awkward, like I'm shell-shocked."
        mike.say "I..."
        mike.say "I don't understand, Hanna."
        mike.say "Are you saying you don't want to be with me?"
        mike.say "I thought things were going great with us."
        "Hanna shakes her head hastily."
        "She steps forwards as she does so."
        "And she grabs my hands, squeezing them tightly."
        hanna.say "No, no, no!"
        hanna.say "That's not what I mean at all!"
        hanna.say "I don't want to break up with you."
        hanna.say "I just...don't want to get married right now!"
        "I nod slowly, finally starting to get Hanna's true meaning."
        "It's not what I wanted to hear, not by a long way."
        "But I think that it's one I can wrap my head around."
        mike.say "So what, Hanna?"
        mike.say "You don't think it's the right time?"
        hanna.say "That's about the size of it."
        show hanna normal
        hanna.say "I'm taking on more responsibility at the gym."
        hanna.say "And I have to balance that with time for us."
        hanna.say "Plus I still need time for myself too!"
        "I have to nod in agreement, even as I let out a sigh."
        "And then I make the symbolic gesture of snapping the box shut."
        mike.say "Okay, Hanna."
        mike.say "I think I understand where you're coming from."
        mike.say "Just promise me it's something you'll consider down the line, yeah?"
        "Hanna nods, then leans in to kiss me on the cheek."
        "I can't help smiling and feeling mollified by this."
        "Things didn't exactly turn out how I'd hoped."
        "But at least I still have hope for the future, right?"
        $ hanna.love -= 25
        $ hanna.sub -= 25
    else:
        hanna.say "YES!"
        show hanna happy
        hanna.say "Oh god, yes!"
        hanna.say "Yes I will!"
        "Hanna thrusts out her hand, almost hitting me in the face as she does so."
        "But I don't think I'd have cared if she had slapped me by accident."
        "I'm too busy fumbling the ring onto her finger to be interested in anything else!"
        mike.say "Wow, Hanna..."
        mike.say "You sure know how to keep a guy hanging on!"
        mike.say "I was terrified that you were going to say no just now."
        "I say this as I'm getting to my feet."
        "At the same time Hanna is busy admiring how the ring looks on her finger."
        "But when my words finally sink in, she looks pretty horrified."
        hanna.say "No way, [hero.name]!"
        hanna.say "How could you even think that?!?"
        "I shrug my shoulders, starting to feel a little embarrassed."
        "Now that I hear it coming from Hanna's lips, it does sound a little crazy."
        "But nevertheless, I still feel the need to justify myself to her."
        mike.say "I don't know, Hanna."
        mike.say "I just see how busy you are at the gym."
        mike.say "How dedicated you are and how much of your time it takes up."
        mike.say "I guess I just got paranoid you might not have enough for me!"
        "As she listens to me explain myself, Hanna's expression changes."
        "She begins to look genuinely concerned as she hears my reasoning."
        show hanna annoyed
        hanna.say "Don't be silly, [hero.name]!"
        hanna.say "You come first, okay?"
        hanna.say "Before work and anything else in my life!"
        mike.say "You really mean that?"
        mike.say "Because I know how much that place means to you."
        mike.say "I know how hard you work!"
        hanna.say "Oh shut up and let me bask in the glory of being engaged!"
        show hanna happy
        hanna.say "We're going to have enough hard work organising the wedding!"
        "I nod, realising that she's right."
        "I never even thought of that!"
        "Now we have to actually start planning the wedding!"
        $ hanna.set_fiance()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
