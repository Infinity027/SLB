init python:
    Event(**{
    "name": "victor_auto_greet",
    "label": "auto_greet",
    "girl": "victor",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(victor,
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
    "name": "victor_give_phone_number",
    "label": "give_phone_number",
    "girl": "victor",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(victor,
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
    "name": "victor_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(victor,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "victor",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "victor_are_you_sick",
    "label": "are_you_sick",
    "girl": "victor",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(victor,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (victor, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "victor_auto_chat",
    "label": "auto_chat",
    "girl": "victor",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(victor,
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
    "name": "victor_ask_out",
    "label": "ask_out",
    "girl": "victor",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(victor,
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
    "name": "victor_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "victor",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(victor,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label victor_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = victor.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = victor.get_activity(bye_hour)
    if not activity == victor.activity:
        if day != game.week_day:
            $ victor.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ victor.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"victor {bye_outfit}")
        if activity["activity"] == "sleep":
            victor.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            victor.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            victor.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            victor.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            victor.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            victor.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            victor.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            victor.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            victor.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            victor.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            victor.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            victor.say "I'll go get dressed."
        hide victor
    return

label victor_cheated(action, cheat_npc=None):
    show victor
    "The kiss feels like heaven, that is until the moment it ends, and I see that Victor's been watching me the whole time!"
    $ victor.love += 1
    hide victor
    return

label victor_beats_ryan_female:
label victor_beats_scottie_female:
label victor_beats_jack_female:
label victor_beats_shawn_female:
label victor_beats_mike_female:
label victor_beats_danny_female:
label victor_beats_dwayne_female:
    if randint(1, 100) <= 70:
        return "abort"
    if active_girl.id == "ryan":
        "I can feel Ryan's lips against mine, his hands all over me."
    elif active_girl.id == "jack":
        "Jack's kissing me with a passion, squeezing me tight."
    elif active_girl.id == "shawn":
        "Shawn has me in his arms, kissing me like crazy."
    elif active_girl.id == "mike":
        "[mike.name] pulls me closer, kissing me more intensely all the time."
    elif active_girl.id == "danny":
        "Danny grabs me and pulls me in for a rough, but passionate kiss."
    elif active_girl.id == "dwayne":
        "Dwayne holds me tight and places a confident kiss on my lips."
    "I know that I should be stopping him, but it's so hard to resist!"
    victor.say "What the hell's going on here?!?"
    victor.say "[hero.name], who is this guy?"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show victor angry at right4
    $ renpy.show(f"{active_girl.id} angry", at_list=[left4])
    if active_girl.id == "ryan":
        "At the sound of Victor's voice, Ryan releases me from his grip."
    elif active_girl.id == "danny":
        "At the sound of Victor's voice, Danny turns around to glare at him."
    elif active_girl.id == "dwayne":
        "At the sound of Victor's voice, Dwayne turns around and raises a single eyebrow."
    else:
        "At the sound of Victor's voice, [active_girl.name] leaps away from me."
    bree.say "Victor, I..."
    bree.say "I can explain..."
    bree.say "This isn't what it looks like!"
    show victor upset fly with dissolve
    "Victor waves a hand in the air, dismissing my words."
    show victor angry at startle(0.1, 5)
    victor.say "No need to explain, [hero.name]..."
    victor.say "I've dealt with this kind of shit before."
    victor.say "This is just between me..."
    if active_girl.id == "ryan":
        victor.say "And this piece of shit!"
    elif active_girl.id == "jack":
        victor.say "And fat boy here!"
    elif active_girl.id == "shawn":
        victor.say "And the fucking clerk!"
    elif active_girl.id == "mike":
        victor.say "And the salary man!"
    elif active_girl.id == "danny":
        victor.say "And this piece of scum!"
    elif active_girl.id == "dwayne":
        victor.say "And chrome-dome over there!"
    "I can't help gasping in surprise at Victor."
    "He looks like some kind of legendary hitman or something!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "Don't I recognise you from somewhere?"
        ryan.say "Didn't you used to be a surfer?"
    elif active_girl.id == "jack":
        jack.say "Whoa...I'm being threatened by a mafioso!"
        jack.say "This is so weird!"
    elif active_girl.id == "shawn":
        shawn.say "Hey, I'm cool with the mob!"
        shawn.say "I pay my protection money!"
    elif active_girl.id == "mike":
        mike.say "Hey, man!"
        mike.say "I don't want to get whacked!"
    elif active_girl.id == "danny":
        danny.say "Whoa...I think I heard of you!"
        danny.say "If I kick your ass, I'll be a made man!"
    elif active_girl.id == "dwayne":
        dwayne.say "Where did you even get that suit?"
        dwayne.say "You look like an extra from a mafia movie!"
    "But it doesn't look like Victor's in the mood to listen."
    $ renpy.hide(f"{active_girl.id}")
    hide victor
    $ renpy.show(f"victor beats {active_girl.id}")
    "Instead he squares up to his opponent, fists raised."
    "And then he lands one...two...no, three punches!"


    pause 0.2
    with vpunch
    with hpunch
    with vpunch
    "That seems to throw his opponent off, enough for Victor to follow up."
    victor.say "HAH!"
    "Victor strikes his opponent's throat with the edge of his hand."
    "And [active_girl.name] collapses to the ground, choking and gagging."
    $ renpy.show(f"bg {game.room}")
    show victor upset at center, zoomAt(1, (640, 720))
    pause 0.3
    show victor upset at center, traveling(1.6, 1, (640, 1020)) with ease
    "Then he steps over his defeated opponent and towards me."
    show victor fly with dissolve
    victor.say "Come on, [hero.name]..."
    victor.say "Let's get the hell out of here."
    return

label victor_greet:
    if renpy.has_label(f"victor_greet_dialogues_{hero.gender}") and not victor.flags.greeted:
        scene expression f"bg {game.room}"
        $ victor.flags.greeted = TemporaryFlag(True, 1)
        show victor
        $ result = randint(1, 3)
        if result == 1:
            victor.say "Hello, [hero.name]."
        elif result == 2:
            victor.say "Hi, [hero.name]."
        elif result == 3:
            victor.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                victor.say "Good morning [hero.name]."
            elif game.hour < 19:
                victor.say "Good afternoon [hero.name]."
            else:
                victor.say "Good evening [hero.name]."
        call expression f"victor_greet_dialogues_{hero.gender}" from _call_expression_464
        hide victor
    return

label victor_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Victor."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Victor."
        elif game.hour < 12:
            bree.say "Good morning Victor."
        elif game.hour < 19:
            bree.say "Good afternoon Victor."
        else:
            bree.say "Good evening Victor."
    return

label victor_kiss_female:
    scene expression f"bg {game.room}"
    if victor.love < 25 and not victor.is_boyfriend and not game.active_date.score >= 75:
        show victor
        "I feel like the time is right for me to make my move."
        "So I lean in and go for it, aiming my lips at Victor's."
        "But I forgot he has those hitman's reflexes and reactions."
        "And he twists away at the last moment, leaving me hanging."
        with hpunch
        bree.say "Huh..."
        bree.say "What the..."
        show victor surprised at startle(0.1, 5)
        victor.say "Ah, sorry..."
        victor.say "I thought you were, like, going for a gun, or something!"
        "He thought I was going for a gun?!?"
        show victor annoyed
        "That has to be, at the same time, the lamest and most outlandish excuse I ever heard!"
        "But of course I have to put a smile on my face and try to hide my embarrassment."
        bree.say "Oh yeah, sure..."
        bree.say "Happens to me all the time!"
        hide victor
        $ victor.love -= 1
    elif not victor.flags.kiss:
        show victor
        "I feel like the time is right for me to make my move."
        "So I lean in and go for it, aiming my lips at Victor's."
        "But I forgot he has those hitman's reflexes and reactions."
        show victor kiss with fade
        "Which means that he's there before me, pressing his lips against mine."
        "And wow, all of that energy he puts into knocking off his targets..."
        "Yeah, I swear I can feel all of it flowing into this damn kiss!"
        "Victor really leans into it too, committing to the act."
        "And by the time it's over, I'm left breathless and gasping."
        "My head spinning and my heart pounding like crazy."
        "Totally blown away by something that I started on a whim."
        hide victor kiss with fade
        $ victor.flags.kiss += 1
        $ victor.love += 5
    else:
        show victor kiss with fade
        "Victor seems to steal kisses in the same way he pulls off hits."
        "Swiftly and in the blink of an eye, swooping in on his target."
        "Then he hits it with expert precision, even before I know it's happening."
        "The whole thing happening so fast that I'm swept along with it."
        "Unable to resist giving into him and in helpless thrall to my own passions."
        hide victor kiss with fade
        $ victor.flags.kiss += 1
        $ victor.love += 5
    return




label victor_ask_date_female:



    call victor_ask_date_alone_female from _call_victor_ask_date_alone_female
    return _return

label victor_ask_date_alone_female:
    if not victor.flags.hadadate:
        bree.say "Victor..."
        show victor joke at startle(0.1, 5)
        victor.say "Hmm...yes, [hero.name]?"
        show victor normal
        bree.say "I know it's complicated and hurtful because of your wife and kitty but..."
        bree.say "We get on pretty well, don't we?"
        bree.say "I mean, we both like each other, right?"
        show victor happy
        victor.say "Oh yes, [hero.name] - you're lots of fun!"
        show victor normal
        bree.say "So what would you say to us spending more time together?"
        bree.say "Like, just the two of us?"
        show victor upset with dissolve
        "Victor ponders this for a moment."
        "And then a light seems to come on behind his eyes."
        show victor surprised at startle(0.1, 5)
        victor.say "Oh..."
        show victor happy
        victor.say "You mean a date?"
        bree.say "Yeah, Victor."
        bree.say "That's exactly what I mean!"
    else:
        bree.say "Let's go on a date!"
    if victor.love < 50 or victor.flags.nodate:
        show victor upset with dissolve
        victor.say "I don't know about that, [hero.name]..."
        victor.say "I'm a pretty dark character, you know?"
        victor.say "I have depths that hide terrible secrets!"
        victor.say "It'd be better to keep a safe distance!"
        $ date_choice = False
    else:
        show victor happy
        victor.say "That sounds like a great idea, [hero.name]!"
        victor.say "I wish I'd thought of it myself."
        victor.say "Going on a date with you would be amazing!"
        $ victor.flags.hadadate = True
        $ date_choice = True
    return date_choice

label victor_pregnancy_congratulations:
    show victor happy
    victor.say "Hey, congratulations, [hero.name]..."
    victor.say "You didn't tell me you were pregnant!"
    "The voice seems to come out of nowhere."
    "And I can't help yelping and jumping in surprise."
    bree.say "Arrgh!"
    bree.say "What the hell?!?"
    show victor upset
    "I see Victor standing there."
    "And his hands are raised like he's about to defend himself."
    bree.say "Victor!"
    bree.say "Don't sneak up on me like that!"
    show victor annoyed with dissolve
    "Victor looks a little sheepish and puts his hands down again."
    show victor joke
    victor.say "Sorry, [hero.name]..."
    victor.say "Moving silently's kind of what I do!"
    victor.say "Erm...you're not going to go into labour, are you?"
    show victor normal
    bree.say "No, Victor..."
    bree.say "I don't think so!"
    $ victor.love += 1
    return

label victor_propose_female:
    show victor
    "I can already feel my nerves threatening to get the better of me."
    "And it's all I can do to keep focussed on the task that I've set for myself."
    "Part of me wants to just forget the whole idea and pretend it never even occurred to me."
    "But another knows that I'll hate myself if I don't buckle down and just do it."
    "So as soon as I spot my chance, I reach into my pocket and pull out the ring."
    if hero.morality >= 25:
        bree.say "V...Victor..."
        bree.say "Will you...will you marry me?"
    if hero.morality <= 25:
        bree.say "Victor, I'm SO into you!"
        bree.say "Will you marry me?"
    else:
        bree.say "Victor, I have to ask you this..."
        bree.say "Will you...marry me?"
    "I'm so used to being the one that's surprised around Victor."
    "So much so that it takes me a moment to figure out the look on his face."
    "And when I do, it becomes clear that he's totally amazed by what I just said."
    "Victor blinks and shakes his head, as if trying to clear it and think straight."
    "And all the while I'm left waiting for his answer."
    "Every second this drags on feels like an eternity."
    "Making me long for him to speak up and put me out of my misery."
    "Even if I don't get the answer I want, at least it'd be a release!"
    if victor.love < 195:

        show victor surprised at hshake
        "Suddenly Victor seems to jerk back into the moment."
        "It's like his brain catches up and kicks him up the ass."
        show victor upset with dissolve
        "His eyes become more focussed and he finally seems to see the ring in my hand."
        "But even so, I'm still almost holding my breath as I wait to hear his answer."
        "Balancing on a fine line and ready to fall one way or the other."
        show victor joke at startle(0.1, 5)
        victor.say "Ah..."
        victor.say "Isn't it supposed to be the guy giving the girl a ring?"
        victor.say "That's the way I remember doing it the last time I got married!"
        show victor normal
        "Ouch...I can feel that double blow land like a punch to the gut!"
        "Not only is he throwing the gesture back in my face."
        "He's also invoking the spectre of his dead wife too."
        "The woman that's been rendered into an untouchable saint thanks to her untimely death."
        bree.say "Well, there's nothing traditional about dating a hitman either, Victor!"
        bree.say "That's why I figured that I'd go ahead and shake things up a little."
        bree.say "So..."
        bree.say "That was kind of more an inquiry than an answer, wasn't it?"
        bree.say "And I'm kinda being left hanging here!"
        show victor upset with dissolve
        "Victor gets that super serious look on his face."
        "The one that furrows his brows and tells me he's about to lay down the law."
        show victor joke
        victor.say "You're dead on the money when you say I'm a hitman, [hero.name]."
        victor.say "And that means I don't get to lead a normal life."
        victor.say "I tried all of that once before, and it ended in tragedy."
        victor.say "I love you too much to let the same thing happen to you."
        show victor normal
        "I wait in vain for him to come back with another line."
        "One that turns all of that on it's head and gives me the answer I want to hear."
        "But when it doesn't appear, I stuff the ring back into my pocket."
        "At the same time trying to hide the fact that my heart is kind of breaking."
        "Instead of arguing, I just nod my head and let the matter drop."
        "Because the pain I'm feeling is already too much."
        "And I can't bear the thought of making it worse."
        $ victor.love -= 25
    else:

        show victor surprised at hshake
        "Suddenly Victor seems to jerk back into the moment."
        "It's like his brain catches up and kicks him up the ass."
        show victor upset with dissolve
        "His eyes become more focussed and he finally seems to see the ring in my hand."
        "But even so, I'm still almost holding my breath as I wait to hear his answer."
        "Balancing on a fine line and ready to fall one way or the other."
        show victor joke at startle(0.1, 5)
        victor.say "Ah..."
        victor.say "Y...yeah, [hero.name]..."
        show victor happy
        victor.say "I do...I mean...I will!"
        victor.say "That is, I'll marry you, yeah?"
        show victor normal
        "Now I feel like time has finally returned to normal."
        "And the world seems to rush in on me as I realise what he just said."
        bree.say "You..."
        bree.say "You really mean that?"
        bree.say "I thought that with the shooting and the killing people..."
        bree.say "You know, that it might not be your kind of thing?"
        "Victor seems to be more than a little overwhelmed by the whole thing."
        "He rubs the back of his head and kind of shrugs his shoulders."
        show victor shout
        victor.say "Well, in my line of work, you kind of realise how short life is, [hero.name]."
        victor.say "Guys tend to either have no emotional ties whatsoever."
        show victor upset
        victor.say "Or else they just decide to live life to the max."
        show victor angry at startle(0.1, 5)
        victor.say "Grab the chances they get and think: Fuck it!"
        bree.say "And just to be clear..."
        bree.say "You're the second one, right?"
        show victor happy with dissolve
        "Victor nods and smiles as he holds out his hand."
        "For a moment I don't know what he wants me to do."
        "But then I remember the ring, and hurry to slide it onto his finger."
        "I think traditionally the guy's supposed to give the girl the ring."
        "But then what's traditional about asking a hitman to marry you?"
        $ victor.set_fiance()
        $ victor.love += 10
    hide victor
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
