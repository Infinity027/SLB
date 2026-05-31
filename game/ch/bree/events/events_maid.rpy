init python:
    Event(**{
    "name": "bree_event_04",
    "label": "bree_event_04",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_03"),
        IsNotDone("bree_event_05"),
        IsDayOfWeek("12345"),
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(bree,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 80),
            MinStat("sub", 25),
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "bree_event_05b_notify",
    "label": "bree_event_05b_notify",
    "priority": 500,
    "do_once": False,
    "quit": False,
    "conditions": [
        IsDone("bree_event_04"),
        IsNotDone("bree_event_05b"),
        IsHour(9, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "kitchen", "bathroom", "bedroom1")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            MinStat("love", 100),
            ),
        ],
    })

    Event(**{
    "name": "bree_event_05b",
    "label": "bree_event_05b",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_04"),
        IsHour(9, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("secondfloor", "bedroom2")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            MinStat("love", 100),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_event_06b",
    "label": "bree_event_06b",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_05b"),
        IsHour(18, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom", "kitchen")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            MinStat("love", 110),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    Event(**{
    "name": "bree_event_07b",
    "label": "bree_event_07b",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_06b"),
        IsDayOfWeek("12345"),
        IsHour(12, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("map")),
        PersonTarget(bree,
            Not(IsHidden()),
            MinStat("love", 120)
            ),
        ],
    "priority": 500,
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "bree_event_08b",
    "label": "bree_maidcafe_bj",
    "conditions": [
        IsDone("bree_event_07b"),
        IsHour(18, 20),
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 130),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_09b",
    "label": "bree_event_09b",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("bree_event_08b"),
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_09c",
    "label": "bree_event_09c",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("bree_event_08b"),
        IsHour(18, 20),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("kitchen"),
            MinStat("sub", 50),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_10b",
    "label": "bree_event_10b",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_09b"),
        IsHour(18, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_11b",
    "label": "bree_event_11b",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_10b"),
        IsHour(18, 22),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_11c",
    "label": "bree_event_11c",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("bree_event_10b", "bree_event_09c"),
        IsHour(18, 23),
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv_with_bree"),
            IsRoom("livingroom"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 75),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_12b",
    "label": "bree_event_12b",
    "priority": 500,
    "conditions": [
        IsDone("bree_event_11b"),
        IsHour(18, 20),
        HeroTarget(
            IsGender("male"),
            IsRoom("maidcafe")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 170),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_13b",
    "label": "bree_event_13b",
    "conditions": [
        IsDone("bree_event_12b"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("breedelay", False),
            MinStat("love", 180),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_14b",
    "label": "bree_event_14b",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_13b"),
        HeroTarget(IsGender("male")),
        IsDayOfWeek("67"),
        IsHour(8, 18),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 190),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_14c",
    "label": "bree_event_14c",
    "priority": 500,
    "conditions": [
        IsDone("bree_event_13b", "bree_event_11c"),
        Not(IsDone("bree_event_14c_alternate")),
        IsSeason(1),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach", "date_nudistbeach")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 100),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_14c_alternate",
    "label": "bree_event_14c_alternate",
    "priority": 500,
    "conditions": [
        IsDone("bree_event_13b", "bree_event_11c"),
        Not(IsDone("bree_event_14c")),
        IsSeason(3),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 100),
            ),
        ],
    "do_once": True,
    "quit": False,
})

label bree_event_14c_alternate:
    "It's getting dangerously close to the holiday season, and so that can mean only one thing."
    "It's time to get started shopping for gifts before time runs out and the big day arrives."
    "So there's nothing for it, [bree.name] and I are going to have to head to the mall and brave the crowds."
    "And so here we are, just an average couple, strolling along and pausing to gaze through store windows."
    if bree.is_collared:
        show bree blush leash at center, zoomAt(1.25, (640, 880))
        "Or at least we would be, if [bree.name] weren't wearing a collar and leash!"
        "A leash that I hold tightly in one hand, keeping her by my side."
        "Sure, we live in a pretty liberal, progressive kind of town."
        "But people still aren't used to seeing a collared girl out in public."
        "And I can feel their eyes on us the whole time we're window-shopping."
        "I know that it's giving me a thrill, imagining what they must be thinking."
        "So I can't begin to guess how much it must be affecting [bree.name] right now!"
        "She keeps from letting it show as I issue her commands and tug her leash."
        "But she must be crawling around inside of her own skin."
        "Everyone's looking at us."
        "And yet none of them are saying a thing."
        "It's perfect!"
    show bree blush at center, zoomAt(1.25, (640, 880))
    "I pause for a moment, stepping back from the window we're looking into."
    "A thought just occurred to me, and I feel the need to ask [bree.name] a question."
    mike.say "[bree.name]?"
    "[bree.name] seems to note the change in my tone of voice almost instantly."
    show bree stuned
    "She turns her head to regard me, a look of sudden concern on her face."
    show bree talkative
    if bree.flags.mikeNickname in nickname_master:
        bree.say "Yes, Master."
    elif bree.flags.mikeNickname in nickname_daddy:
        bree.say "Yes, Daddy."
    else:
        bree.say "Yes, [hero.name]."
    bree.say "Yes, [hero.name]."
    show bree normal
    "I can't help smiling at how she uses the special term to address me."
    "It comforts me and goes a little way to answering my question before it's asked."
    "But I still need to hear the answer from her own two lips."
    mike.say "I just wanted to ask, [bree.name]..."
    mike.say "Are you happy right now?"
    show bree stuned
    "[bree.name]'s eyes go wide at the question, and she shakes her head."
    "She seems to think that it's a trick, some kind of test."
    show bree smile
    if bree.flags.mikeNickname in nickname_daddy:
        bree.say "Yes, Daddy."
    elif bree.flags.mikeNickname in nickname_master:
        bree.say "Yes, Master."
    else:
        bree.say "Yes, [hero.name]."
    bree.say "Yes, [hero.name]."
    show bree happy
    if bree.is_collared:
        bree.say "I...I'm SO happy!"
        bree.say "In fact, I don't think I've ever been so happy!"
        show bree normal
        "I can't help smiling at the way [bree.name] tries to sound as upbeat as possible."
        "It's like she's turning into my perfect pet a little more each day."
        "Emphasizing the aspects of her character that I like and pushing aside those that I don't."
        "And it's made all the more gratifying by the fact she seems to be loving it too!"
        mike.say "You must mean that, [bree.name]."
        mike.say "You have to remember that your happiness makes me happy too."
        mike.say "I can't be happy unless my pet is happy to be my pet!"
        "I see [bree.name]'s hand stray unconsciously to the collar around her neck."
        "She nods eagerly, keen to assure me that that all is well."
    else:
        bree.say "Oh, I AM happy!"
        bree.say "I've never been happier since..."
        show bree smile
        bree.say "Well, since we started to...you know..."
        show bree flirt
        "I nod, sensing that [bree.name]'s struggling to find the words."
    show bree normal
    "Then she glances at the contents of the window, as if having a revelation."
    show bree talkative
    bree.say "I...I wanted to give you a gift."
    bree.say "A special gift this festive season."
    bree.say "Something that'll show you how happy I am!"
    show bree normal
    mike.say "That's sweet, [bree.name]."
    mike.say "But I don't need you to buy me something to show you're happy!"
    show bree gloomy
    "Suddenly [bree.name] shakes her head and her expression becomes pained."
    "I can see that she thinks I'm not following her, not grasping her meaning."
    show bree sad
    bree.say "No, no, no..."
    bree.say "I meant that I want to make a promise to you!"
    show bree talkative
    bree.say "A pledge that I intend to keep."
    show bree normal
    "Now this does peak my interest."
    show bree at center, traveling(1.5, 0.3, (640, 1040))
    "I lean in closer, eager to hear what [bree.name] has to say."
    if bree.is_collared:
        "[bree.name] already let me put a collar around her neck."
        "What else could she possibly do to show her submission to me?"
    show bree flirt blush
    if bree.flags.mikeNickname in nickname_daddy:
        bree.say "I...I really want to be your slave, Daddy."
        bree.say "I want to be your slave - mind, body and soul!"
        bree.say "That's how much I love you, Daddy."
    elif bree.flags.mikeNickname in nickname_master:
        bree.say "I...I really want to be your slave, Master."
        bree.say "I want to be your slave - mind, body and soul!"
        bree.say "That's how much I love you, Master."
    else:
        bree.say "I want to be owned by you, possessed by you, [hero.name]!"
        bree.say "I want to dedicate my life to pleasing you!"
        bree.say "That is...if you'll let me?"
    "And here I was thinking that [bree.name] couldn't say anything to surprise me!"
    "Of course, I want to say yes almost as soon as I hear her say the words."
    "But that's where our relationship is different, the reason why it works."
    "I know that [bree.name]'s being honest when she says that she loves me."
    "And I feel the same way about her in return."
    "She might be submissive to me, but our relationship is based on love."
    "I'd never do anything to [bree.name] that would hurt her, anything she didn't want."
    "I'd never exploit the love that she has for me in that way."
    "And that's the very same reason why I know that I can agree to what she wants."
    "I know that it's something she desires deeply, something that will make her happy."
    mike.say "Of course I will, [bree.name]."
    mike.say "If you're sure that's what you want?"
    bree.say "It is...oh, but it is!"
    mike.say "Okay, [bree.name], okay."
    mike.say "You'll be my willing slave."
    mike.say "And I'll be your loving master."
    show bree happy -blush
    "[bree.name] can't conceal the delight that she's feeling right now."
    "Her face beams with happiness, and she makes to throw her arms around me."
    show bree evil
    "But then she stops and looks at the ground."
    "It's almost like she's suddenly ashamed of something."
    "At first I think it's the glances of the passing shoppers."
    "But then I realise that they never bothered [bree.name] before."
    "So that means it must be something else."
    mike.say "What's the matter, [bree.name]?"
    show bree smile
    if bree.flags.mikeNickname in nickname_daddy:
        bree.say "Daddy, I..."
    elif bree.flags.mikeNickname in nickname_master:
        bree.say "Master, I..."
    else:
        bree.say "[hero.name], I..."
    bree.say "Your slave would really like permission to hug you right now!"
    show bree normal
    "I almost laugh out loud at the realisation that she's waiting for permission."
    "But that would hurt [bree.name]'s feelings, so I push the urge down and nod."
    mike.say "Of course you can, [bree.name]!"
    mike.say "You have my permission to hug away!"
    show bree flirt
    "The moment I speak the words, [bree.name] almost lunges at me."
    "A couple of gawking shoppers are forced to leap out of her way."
    hide bree
    show bree kiss
    with fade
    $ bree.flags.kiss += 1
    "And then she wraps her arms around me with an alarming show of strength!"
    "Then she kisses me, full on the lips and with incredible passion too."
    "I can feel [bree.name]'s body pressed against my own."
    "And it doesn't take long for my cock to stiffen in response."
    "I don't know if it's just the sensation of her embracing me."
    "Or if the knowledge that [bree.name] wants me that badly is turning me on."
    "Either way I couldn't care less about the people watching us kiss."
    "They wish they had a relationship as strong and honest as ours!"
    "[bree.name] just gave me the best Xmas present I could have asked for."
    return

label bree_event_04:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "[bree.name]")
    if not result:
        $ hero.cancel_event()
        $ bree.love -= 5
        return
    if bree.love.max < 100:
        $ bree.love.max = 100
    mike.say "Hey [bree.name]."
    bree.say "Hey, [hero.name]."
    bree.say "Could you meet me at the coffee shop in the mall?"
    mike.say "Why?"
    bree.say "Come on! I have something to discuss with you."
    menu:
        "Sure":
            pass
    bree.say "Great! I'll meet you there in an hour."
    scene bg mall1 with timelaps
    $ game.pass_time()
    "So, I wasted time for an hour or so, before heading to the coffee place, setting off a little early to make sure I wasn't late."
    scene bg coffeeshop with fade
    "Predictably, as a result I got there early instead. It wasn't particularly difficult to find so I wasn't wandering for long and [bree.name]'s directions got me to the general area."
    "Looking around, the place seems mostly empty, including free of any specific blonde roommate of mine."
    "A quick check of my phone tells me I am still early, so not a big deal."
    "Grabbing a quick drink I take a seat facing the door, and patiently wait for [bree.name] to arrive."
    "Unfortunately for me, while I was early, [bree.name] is definitely not."
    show bree blush casual with moveinright
    "Around twenty minutes after she arranged to meet me, I see her burst through the door at mach 10 speed, quickly searching the room with wide, almost desperate eyes, before finding me."
    "As our eyes meet, she seems to relax somewhat, although still rushes over to my booth needlessly quickly."
    show bree sad at center, zoomAt(1.5, (640, 1140)), vshake
    bree.say "I'm so sorry I'm late, [hero.name]!"
    show bree gloomy
    menu:
        "Don't worry about it.":
            show bree talkative
            bree.say "Really? I didn't keep you waiting long, did I?"
            show bree sadsmile
            "By now I'd been here for half an hour at least, but it is clear [bree.name] has gotten here as soon as she could."
            "While she is still... Presentable, I can make out a thin layer of sweat covering her face, and her hair's on the messy side."
            "It look like she's been running for a while, if I listen carefully I can even tell she's breathing not only heavily, but slightly raspy too."
            mike.say "No, I just got here myself. It's fine, really."
            show bree happy
            bree.say "Oh, good! I was running late so got really worried!"
            show bree normal
            "She seems to have bought it at least, either that or she knows I'm lying but is relieved I don't care."
            "Either way, she seems to have calmed down a little."
            $ bree.love += 1
        "You kept me waiting.":
            show bree sad
            bree.say "I know! I'm really sorry [hero.name]!"
            show bree gloomy
            mike.say "I even came early so I wouldn't keep you waiting."
            "I've been here long enough to start getting annoyed. It's one thing for her to be late, but it's been quite a while now, and she was the one who set the time to begin with."
            show bree talkative
            bree.say "I won't be late next time, promise!"
            show bree sadsmile
            mike.say "Just make sure that you aren't."
            $ bree.sub += 1
    show bree normal -blush
    mike.say "So, are you getting a drink?"
    "My own coffee hadn't lasted me too long, and even if I'd saved it until now, it wouldn't be hot anymore."
    "Besides, can you ever really have enough coffee?"
    show bree talkative
    bree.say "I like, wasn't going to get one, but you can go get another before I tell you the thing!"
    show bree normal
    mike.say "You sure? I'd feel bad getting myself one when you've not got anything."
    show bree smile
    bree.say "Yep! Go ahead!"
    show bree normal
    menu:
        "Get yourself a drink.":
            "If [bree.name] isn't going to pay for her own drink, I am not going to get one for her."
            "Fortunately for the both of us, there was no line at the moment, so grabbing another coffee only took a few moments."
            "I take a seat again opposite [bree.name], who seems to have relaxed a little more by now, and begin sipping at my drink."
            $ bree.sub += 1
            $ DRINK = False
        "Get yourself and [bree.name] a drink.":
            mike.say "I'm not going to get anything if you aren't. Come on, it's on me."
            show bree talkative
            bree.say "Are you sure? I'll pay you back, promise!"
            show bree sadsmile
            mike.say "Don't worry about that. What do you want?"
            show bree smile
            bree.say "Uh, just a latte please!"
            show bree happy
            bree.say "Thanks [hero.name]!"
            show bree normal
            mike.say "Don't mention it."
            "Fortunately for the both of us, there is nobody else waiting for their drinks, so I head straight to the barista and before long I am returning to our booth."
            "[bree.name] quickly thanks me again as I hand her her drink, which she quickly sips at, immediately pulling a face that suggests it's a little hotter than she expected."
            "After that, she's a little less eager to drink it."
            $ bree.love += 1
            $ DRINK = True
    mike.say "So, what did you want to talk about?"
    show bree smile
    bree.say "Oh yeah! Right, so like, we're friends now, right?"
    show bree normal
    "My curiosity had already been piqued by what was supposedly an 'important' topic, but the question makes me lean forward in my seat, as if searching for more information."
    mike.say "Of course, why?"
    show bree sad
    bree.say "Well, like, I think I'm not gonna make rent this week."
    bree.say "I'm almost there! Just a little short!"
    show bree gloomy
    menu:
        "Don't worry, I'll cover the difference." if hero.money >= 50:
            $ bree.flags.debt = True
            show bree surprised
            bree.say "Really?"
            show bree stuned
            "[bree.name] seems shocked I'd even suggest such a thing, but it isn't a big deal."
            mike.say "Yeah, of course. Like you said, we're friends."
            "It's not like this is a regular thing after all, I've never had troubles with getting rent out of [bree.name] before."
            show bree happy
            bree.say "Wow, thanks [hero.name]! And to think I was nervous to tell you!"
            show bree normal
            mike.say "Yeah well, everyone has off weeks."
            mike.say "You'll have it next week though, right? I can't cover for you forever."
            $ bree.love += 1
        "I'll sort something out.":
            show bree surprised
            bree.say "Really?"
            show bree stuned
            mike.say "Sure. I'll talk to the landlord and Sasha, one week a little short is no big deal."
            show bree smile
            bree.say "Wow, thanks [hero.name]!"
            show bree normal
            mike.say "Don't mention it, it's really not a big deal."
            show bree smile
            bree.say "Hehe, now I feel silly for getting worried about it!"
            show bree normal
            mike.say "You will have it next week though, right? I can't cover for you forever."
            "Part of the reason it's no big deal is that [bree.name]'s been reliable in paying her rent up until now, if that changed the landlord might not be too happy."
        "You better have it.":
            show bree talkative
            bree.say "I'll do my best! Promise!"
            show bree sadsmile
            mike.say "Good, the landlord won't be happy if we don't give them the full amount."
            show bree talkative
            bree.say "It was only like, a warning just in case! I should have it!"
            show bree sadsmile
            mike.say "If you really can't, you might get away with it once, but if you don't have the full hundred by next week there'll be trouble."
            mike.say "You will have it next week, right?"
            $ bree.sub += 1
    show bree talkative
    bree.say "Of course!"
    show bree normal
    mike.say "That's a relief."
    "There's a short lull in conversation as I sip at my drink."
    if DRINK:
        "[bree.name] sips at hers too, but seems to be still cautious not to let it burn her again."
    "Now seems like as good a time as any to pry for more information about [bree.name]."
    "Call me nosey or invasive if you want, but I'm curious and she isn't offering much information about herself without me asking."
    mike.say "You mind if I ask you something?"
    show bree smile
    bree.say "Ask me anything!"
    show bree happy
    bree.say "Hehe, as long as I can ask something in return~!"
    mike.say "It's a deal."
    show bree normal
    mike.say "I was just wondering, I know you're a student, but do you have a job?"
    "For a split second, I worry if I've asked too much, the usual cheerful demeanor slipping for just a moment into something that doesn't last long enough to place, before returning slightly weakened."
    "[bree.name]'s already told me she was unemployed back at the arcade, but I'm digging for more information than that."
    "Besides I kinda forgot she said so when I asked the question, only realising so after the words had escaped my mouth."
    show bree annoyed
    bree.say "Well, actually it's like, a little embarrassing."
    show bree talkative
    bree.say "I used to work in one of those chain fast food places, but I quit when I started school again."
    bree.say "I've just been using my savings as rent!"
    bree.say "That's actually why I wanted to meet here today! I was at a job interview nearby, there's a cafe opening and they need more waitresses!"
    show bree normal
    "So her savings have run out? Better hope she gets the job then, and that she can start soon."
    "By now, she's returned to her full cheerful self once more, any signs of my question being awkward to ask vanished."
    mike.say "Did it go well?"
    show bree talkative
    bree.say "Well, I think so? I mean like, it was hard to tell."
    bree.say "They asked a lot of hard questions, but I did some research beforehand so I think I got them right!"
    bree.say "It was more like a quiz than an interview actually."
    show bree smile
    bree.say "Oh! But the owner seemed happy when I gave her my measurements!"
    show bree normal
    "Wait what?"
    mike.say "Wait what?"
    show bree smile
    bree.say "Hehe, I mean like, she has a uniform that already fits me!"
    bree.say "It wasn't like, a pervert thing!"
    show bree normal
    mike.say "Good, you had me worried there for a minute."
    show bree smile
    bree.say "Hehe, I could tell! You pulled a funny face~!"
    bree.say "Glad to know someone's looking out for me though!"
    show bree normal
    mike.say "It's the least I can do."
    "I leave out the part where I've grown a little protective of [bree.name] because her childish nature and seeming naivety of the world means she's got a target painted on her back."
    "There are hundreds of creeps in this town who'd take advantage of someone like her."
    "I'm trying to be nice after all, I don't want to insult her."
    mike.say "So, this fast food job, was that back home in the country?"
    show bree talkative
    bree.say "Nope! It was here in town, probably a ten minute walk from here!"
    show bree normal
    "That's odd. [bree.name] had made it sound like she'd only just moved here when we visited the arcade together."
    "She talked as though she didn't have any friends, but if she'd been here for a while that didn't make sense to me, especially if she'd been going to both school and her job."
    "Surely one coworker or classmate would get along with her."
    "I think I have been pushy for now though, and I don't want to come across as rude or as doubting her."
    show bree happy
    bree.say "So! My turn to ask a question!"
    show bree normal
    mike.say "Yeah, that was the deal, ask away."
    show bree talkative
    bree.say "Do you like your job?"
    show bree normal
    "That wasn't exactly what I was expecting."
    mike.say "Uh, not really. Actually, it kinda sucks."
    show bree sad
    bree.say "Aww, that's no good."
    show bree talkative
    bree.say "How do you get out of the bed in the morning?"
    bree.say "I mean like, if you hate it, it's gotta suck getting up every day for it."
    show bree sadsmile
    mike.say "Well, yeah, but you gotta do it."
    mike.say "Part of being an adult, I guess."
    show bree annoyed
    bree.say "Being an adult sucks."
    show bree normal
    "I smirk. Not because what she said was wrong, or because I agree with her, but rather that it's the exact sort of thing I'd expect coming from someone like [bree.name]."
    if DRINK:
        mike.say "I could drink to that."
        show bree happy
        bree.say "Then let's!"
        show bree normal
        "[bree.name] gleefully extended her latte into the air, having drank most of it by now, but with enough left to toast."
        "Although I snicker at the thought of toasting with coffee, and snicker again at the irony of phrasing it like that in my mind, I hold mine up too."
        show bree smile
        bree.say "To never growing up!"
        show bree normal
        mike.say "To never growing up."
        "We clink our mugs together, and each take a sip of our drinks, neither disillusioning ourselves about quite how silly that was, but neither of us cared."
    else:
        mike.say "Agreed. Wish I could stayed a kid forever."
        show bree happy
        bree.say "Hehe, me too! That would have been the best~!"
    show bree smile
    "We each share a wide grin."
    "If nothing else, at this point I'm just glad that [bree.name] seems to have relaxed properly again."
    "Nothing stays serious for long with her around after all."
    show bree normal
    mike.say "So, if you're getting a job I guess that means there'll be less time for us to play together."
    show bree smile
    bree.say "Yep, but it also means I'll have money to go to the arcade again~!"
    show bree normal
    mike.say "Heh, good point."
    mike.say "I don't know though, I think I ended up enjoying playing at home a little more."
    show bree smile
    bree.say "Really?"
    show bree normal
    mike.say "Yeah, it's the same game after all."
    mike.say "Something kind of nostalgic about going to the arcade, but sometimes it's just nice to be home."
    mike.say "I think nostalgia is overrated."
    show bree smile
    bree.say "Really? I like nostalgia, it's like, bittersweet, you know?"
    show bree normal
    mike.say "Yeah, it's both the best and worst feeling in the world."
    show bree smile
    bree.say "Yep! That's exactly it."
    show bree normal
    mike.say "Guess the worst part is a little higher for me."
    show bree happy
    bree.say "Well, I'm OK with playing at home! I can save up my money and buy some new games too!"
    show bree smile
    bree.say "Oh! And there's this book that's just come out that looks really good!"
    show bree normal
    mike.say "Well, fingers crossed you get the job then."
    mike.say "You know if you've got a second one lined up yet?"
    show bree talkative
    bree.say "Actually, yep! They asked me to come back next week!"
    bree.say "I'm actually like, really nervous."
    show bree normal
    mike.say "That's normal. Anything I can do to help?"
    show bree talkative
    bree.say "Hmm... Oh, yeah! They like, said the waitresses would be doing both serving and cooking!"
    bree.say "Can you like, do some taste testing and stuff? I wanna practice before I go back, just to make sure I get it!"
    show bree normal
    mike.say "Well, can't say no to that."
    show bree smile
    bree.say "Yay! Thanks [hero.name]! It's nothing fancy, but I've never really cooked before, so I wanna make sure I get it right!"
    show bree normal
    mike.say "If nothing else, I can give you a few pointers."
    mike.say "I'm not a master chef, but if it's just simple stuff I should be able to manage."
    show bree happy
    bree.say "That'd be great! Thank you so much!"
    show bree normal
    mike.say "Don't mention it. I'll be expecting you to make me a few meals sometime in return."
    show bree smile
    bree.say "Deal! If it's alright, can you like, pretend to be a customer and stuff so I can practice serving too?"
    show bree normal
    mike.say "Whatever makes you feel more confident."
    show bree smile
    bree.say "Wow, thanks [hero.name], you're the best!"
    show bree normal
    mike.say "Whatever you say, [bree.name]."
    "We shared another chuckle, before deciding to call it a day."
    "I brought the leftover mugs to the barista, thanking them for the drinks, before heading out of the door with [bree.name]."
    "I had some plans for the evening already, so we agreed to practice as soon as possible."
    "[bree.name] just seemed happy to take a break for the rest of the day, I couldn't help but feel like she must have had a stressful time with the job interview and worrying about rent."
    "Besides, I needed to give her a chance to find some recipes at least."
    hide bree
    $ game.room = "street"
    return

label bree_event_05b_notify:
    "I should check on [bree.name] and see if she needs help with her interview."
    return

label bree_event_05b:
    if bree.love.max < 110:
        $ bree.love.max = 110
    scene bg secondfloor








    show bree talkative
    with fade
    bree.say "Yeah?"
    show bree normal
    "The door is cracked open just enough for her head to poke out, greeting me with that signature grin."
    mike.say "Hey, I was just wondering if you could cook for me."
    show bree surprised
    bree.say "Cook for you?"
    show bree stuned
    "She seems a little confused by the statement, as though she has no idea what I mean, but it clicks soon enough it seems."
    show bree smile
    bree.say "Oh! Uh, sure? Why?"
    show bree sadsmile
    mike.say "Well I mean, thought I could taste test for you."
    "[bree.name] seems conflicted for some reason, and although she eventually nods, shrugs and grins, I get the impression she doesn't really want to make anything."
    "Why is another question altogether, but I just chalk it up to laziness or her preferring the game she's playing."
    "This is important though, so I don't feel guilty for dragging her out of her hole."
    mike.say "So do you want to practice the maid persona while I'm here?"
    "It's only half a joke. If she said yes my day would get better."
    show bree smile
    bree.say "Nope! Thanks though, but I think I'm like, alright with that part."
    show bree normal
    "Damn."
    scene bg kitchen
    show bree
    with fade
    "I shrug and lead her to the kitchen, intending to overlook the process, but when we get there neither of us makes a move."
    mike.say "So?"
    show bree talkative
    bree.say "I'm just like, thinking where to start."
    bree.say "Should I try the soup again?"
    show bree sadsmile
    "It didn't matter much to me either way, I wasn't hungry, just trying to help. So, I shrugged."
    "It was probably better for her to just make whatever she felt most comfortable with, if she wanted to make soup, she could make soup."
    show bree talkative
    bree.say "Alright! I'll give it uh- I'll give it a shot."
    show bree sadsmile
    "She hardly seems confident, in fact she seemed reluctant to come cook in the first place."
    "I begin wondering if something's wrong, but decide it best to just leave her to it. If she needs help, I'm right here."
    mike.say "Sounds good to me. I'm right here if you need some help."
    show bree talkative
    bree.say "Thanks! But uh, would you not prefer like, going and sitting down somewhere?"
    show bree sadsmile
    mike.say "Nah, it's alright. I can watch over you this way."
    show bree talkative
    bree.say "Well OK then! I'll just get started then!"
    show bree sadsmile
    "I smile and nod. It feels like she's maybe putting off actually cooking for as long as possible for some reason."
    show bree b annoyed at left5 with ease
    "I consider asking why, but since [bree.name] begins, reluctantly, collecting her ingredients anyway, I settle on just leaving her to it."
    "It does quickly become apparent however, that my suspicions were right, and something is wrong."
    show bree b dazed at right4 with dissolve
    "As I watch over her, [bree.name] keeps hesitating, reaching for one ingredient and stopping and getting something else entirely, or starting to heat a pot of water before stopping inexplicably."
    show bree a lose at center, vshake
    "At one point, she even starts cutting up a leek before seemingly changing her mind and throwing the entire thing away."
    "More than once I think to intervene, she looks like she has no idea what she's doing, but I refrain out of a sort of morbid curiosity."
    show bree b annoyed at right with dissolve
    "Besides, she isn't going to learn from her mistakes if I'm coddling her constantly."
    show bree a happy at left with dissolve
    "Her attitude and innocence is very childlike, but it'd be condescending for me to look down on her as a result."
    "It does seem like [bree.name] herself is starting to get frustrated though, she's making progress but it's slow and she's started to mutter the recipe aloud to herself."
    show bree b evil at right5 with dissolve
    "I'm not sure how someone can be quite so bad at cooking, but I don't want to be insulting so I don't say anything."
    show bree b surprised at center, hshake
    "I realise that was a mistake however, when as she's cutting carrots, [bree.name] suddenly yelps and drops her knife."
































    mike.say "Are you alright?"
    "I'm worried about [bree.name], more than I usually am, and not just because of the cut."
    show bree cry
    bree.say "Uh, yeah! I'll be fine."
    bree.say "It hurts but it isn't that deep."
    show bree sadsmile
    mike.say "Oh good, that's a relief."
    show bree normal
    "I flash her a half hearted smile, she gives me her usual grin in return, but it does little to put me at ease."
    mike.say "What happened?"
    show bree talkative
    bree.say "What do you mean? I just like, lost focus for a second and my hand slipped."
    show bree sadsmile
    "I was asking more about the cooking as a whole. I'd stayed out of it but it was a mess, and I don't believe her cutting herself was just because of a lack of focus."
    menu:
        "Be mean":
            $ bree.sub += 5
            $ bree.love -= 5
            mike.say "I mean your cooking was atrocious."
            show bree stuned
            "I'm well aware I'm being mean, but I'm also being honest and right now, with the threat of eviction on the horizon if she doesn't get a job, that's what [bree.name] means."
            mike.say "Really bad. I thought you'd practiced."
            show bree gloomy
            "I didn't need to wait for [bree.name]'s answer, the look on her face told me everything I needed to know."
            show bree cry
            bree.say "Well I um didn't practice."
            show bree gloomy
            "She looks upset. In fact, very upset, almost on the brink of tears in fact. I've never seen [bree.name] like this before, it's such a stark contrast to her usual cheerful self I feel my heart sink, even if I think I'm doing the right thing."
        "Be nice":
            $ bree.love += 5
            mike.say "You didn't really practice, did you?"
            "It didn't exactly take a genius to figure that out, if she'd even so much as tried to practice then she'd know the recipe at least."
            show bree cry
            bree.say "...No."
            show bree gloomy
            "She looks upset, very upset actually. Her eyes are almost watering, and are an uncomfortable shade of red."
            "I've never seen [bree.name] like this before. Usually, she's so happy and upbeat, whenever I've seen her upset for whatever reason in the past she's bounced back in seconds but this is something else."




    show bree cry
    bree.say "I should have practised and then I didn't and then I hurt myself and I embarrassed myself in front of you."
    show bree gloomy
    mike.say "That's really why you're upset?"
    show bree sadsmile
    "It seems a little silly to me, to be so worried about what I think, but [bree.name] nods in response and forces a smile."
    "At the very least it seems like she's calming down now."
    mike.say "You don't have to worry what I think of you, I guarantee anything you can do I've done stupider."
    mike.say "One time I was skimming stones and eating, and I took a bite out of a stone and threw my sandwich into a lake."
    "That wasn't true, I actually read that online a while back, but [bree.name] doesn't need to know that."
    show bree happy at startle
    "I get the laugh I wanted, her face finally lighting up once more."
    "That's the thing about people like [bree.name]. They're always so happy that the second you see them upset it hits much harder."
    show bree smile
    bree.say "Thanks. You're pretty good at cheering me up!"
    show bree a normal
    mike.say "Guess so. At least I'm good at something."
    show bree smile
    bree.say "You're great at lots of things! Like Alley Fighter!"
    show bree a normal
    "There's the [bree.name] I know."
    mike.say "You're better and we both know it."
    show bree a smile
    bree.say "I've been playing longer than you though! Like, in time, you'll be better than me!"
    show bree a normal
    mike.say "Well, I will have a head-start practising as you work on cooking some more."
    "[bree.name]'s grin wavers for just a second, but any doubts I had are quickly put to rest as she gives me a determined nod and a thumbs up."
    show bree a smile
    bree.say "I'll be the best cook ever!"
    show bree a normal
    mike.say "Heh, glad to hear it. You should take a break for now though, and be more careful when you're cutting carrots next time."
    show bree a smile
    bree.say "I will! I don't want you to worry!"
    show bree a normal
    mike.say "Heh, alright. You should also bandage that finger properly because I have no idea what I'm doing."
    show bree a smile
    bree.say "Got it! It should heal pretty quick, it wasn't as bad as it looked!"
    show bree a normal
    if hero.has_skill("cooking"):
        mike.say "Sounds good. Let me know when you're practising next, I'll show you a few tricks to keep yourself safe."
        "Well, technically I already have, but I get the impression that [bree.name]'s forgotten them already."
        show bree happy
        bree.say "Oh wow, thanks [hero.name]!"
    else:
        $ bree.love -= 5
        mike.say "That's a relief, I was worried I was going to have to rush you to the hospital."
        show bree happy
        bree.say "Hehe, nothing that serious!"
    bree.say "So yeah! I'll definitely practice and I'm going to nail that interview!"
    bree.say "Then I'll impress you with a good meal and take you to the arcade to celebrate as thanks for your help!"
    show bree normal
    mike.say "Sounds like a good time to me."
    "Also sounds like a date, but I'm positive that she didn't intend it like that."
    show bree smile
    bree.say "Really though, you're being so nice to me! I do appreciate it."
    bree.say "Everyone in this town is nice!"
    show bree normal
    mike.say "Good to see you back to normal, [bree.name]."
    show bree b wink
    "I smile at her, and get a wink and another thumbs up in response."
    show bree a normal
    "We make some small talk while [bree.name] finishes up with her finger, she eagerly tells me more details about a couple of upcoming games."
    hide bree with easeoutleft
    "Then she makes her excuses and vanishes back into her room. Soon after I hear the telltale signs of video games again leaking into the hallway."
    "I sincerely hope that she does practice this time, she'll be in a tricky situation if she doesn't get the job after all."
    "I also think it'd be good for her, not just getting out of the house more, but having something to do aside from playing video games."
    "Well, I should go do things I guess, I'm sure [bree.name]'ll be fine."
    "As much as she reminds me of one sometimes, she isn't a child. It is condescending for me to treat her like one."
    "The best thing I can probably do for her now is remain optimistic."
    return

label bree_event_06b:
    if bree.love.max < 120:
        $ bree.love.max = 120
    scene bg livingroom
    bree.say "Hey, roomie!"
    "I hear [bree.name] calling me from the next room, summoning me, and seemingly not to just play video games for once."
    "I briefly consider that might have been her intention, a quick few rounds of Alley Fighter, but her voice came from the living room."
    "Also, it's a little early, in fact I've not long woken up myself and [bree.name] seems the type to enjoy sleeping in as much as she can get away with."
    "Curious, I poke my head around the corner to see what she wanted."
    scene bg kitchen
    show bree normal at center, zoomAt(1.25, (640, 880))
    with fade
    "I'm surprised to find her stood by the table, which has been set with a clean white tablecloth and fancy cutlery which I can't remember ever owning."
    "And of course, food. Quite a bit of it actually."
    "Closer inspection reveals it's all simple dishes, like the soup she'd been trying to make for the past week now, but they look actually edible if nothing else."
    "The most complicated dish there looked like some kind of home-made burger, and not coincidentally it looked like the least professional dish too."
    show bree happy
    bree.say "So I've been practising and I wanted some opinions before tomorrow!"
    bree.say "Because, like, I'm kinda nervous and stuff!"
    show bree at startle
    "She laughs, and I laugh, but I can tell she's serious, and she's right to be."
    show bree normal
    mike.say "Yeah, of course. You didn't have to make so much though."
    show bree talkative
    bree.say "Well I didn't know like, what they were gonna be serving there?"
    bree.say "I wanted to have my bases covered! Plus it got boring making the same thing over and over and over and over."
    show bree normal
    mike.say "Guess it is good to have a wider spread."
    mike.say "But where'd you find the time to learn so many in just a couple of days?"
    show bree happy at startle
    "[bree.name] laughs again, but breaks eye contact and scratches at the back of her head."
    show bree annoyed
    bree.say "Wellllll~."
    show bree hesitating
    bree.say "I waited until like, you and Sasha had gone to bed then did it in the night!"
    bree.say "You know, if there was gonna be a big mess or something I didn't want to get in the way during the day."
    show bree normal
    "Kind of weak reasoning in my eyes, but [bree.name]'s weird."
    "There is one larger problem with her story though, which makes me roll my eyes and groan."
    mike.say "Thanks I guess, but what about actually sleeping?"
    mike.say "That's important too."
    show bree smile
    bree.say "Well duh! But like, I'm alright! See!"
    show bree b wink
    "She gives me a thumbs up and winks."
    bree.say "Not even tired!"
    show bree normal
    "Every time I start to think that treating her, or even thinking of her, like she's a child is cruel or condescending she does something like this."
    mike.say "Well, as long as you sleep tonight."
    mike.say "This whole thing would have been a waste of time if you fall asleep while you're there."
    show bree a happy
    bree.say "Hehe! I'll stay awake, promise!"
    show bree talkative
    bree.say "Oh! But that does remind me. Would you mind coming with me?"
    bree.say "I mean like, you've been a great help so far, and I totally get it if you're busy!"
    bree.say "But I'd appreciate the like, moral support?"
    show bree normal
    mike.say "I get it. Of course I'll come."
    "I'm in too deep to say no now. Besides, it gives me an excuse not to go to my day job, and I'll take any of those."
    show bree hesitating
    bree.say "Really?"
    show bree happy
    bree.say "Yay! Thanks [hero.name]! You're the best!"
    show bree casual happy at center, zoomAt(1.85, (640, 1240)) with hpunch
    "She practically flings herself at me, almost knocking me off my feet."
    "It takes a second for me to get my breath back and return her embrace, although her face in my chest is making it hard to breathe."
    mike.say "Not sure about the best, but don't worry about it."
    "I enjoy the hug for a few moments, but then try to separate myself when it becomes abundantly clear that [bree.name] isn't going to stop otherwise."
    mike.say "Food's getting cold."
    show bree talkative
    bree.say "Oh! Yeah! Quick, you should eat up!"
    show bree normal at center, traveling(1.25, 0.3, (640, 880))
    "Fortunately that's enough for her to release her death grip, she even pulls out the chair for me."
    mike.say "What a gentleman."
    show bree smile
    bree.say "Hehe! The like, whole thing at a maid cafe is service, right?"
    bree.say "I figured I'd try and get more used to that too!"
    show bree normal
    mike.say "So you'll be putting on the persona? Calling me master and all that?"
    show bree smile
    bree.say "Yep!"
    show bree normal
    "Nice."
    mike.say "Well let's get started then."
    show bree smile
    if bree.flags.mikeNickname:
        bree.say "Of course, [hero.name]!"
    show bree normal
    "I watch her take a moment to straighten her back and clasp her hands behind her back, a posture which naturally juts her chest outwards."
    "Probably by design really, but I'm not going to complain."
    "In fact, the posture and the fact that she adds 'master' to the end of every sentence is pretty much the only change."
    "[bree.name] curtsies towards me, bowing her head as I grab the burger, eager to get it out of the way first."
    show bree smile
    if bree.flags.mikeNickname:
        bree.say "I hope you enjoy, [hero.name]!"
    bree.say "That burger is my own special recipe~!"
    show bree normal
    "That worries me more than its appearance - the fact that she's tried creating something from scratch when just days ago she could barely make a sandwich."
    "But, I try not to let on to my worry, and take a bite."
    "The taste is overwhelming. It feels like a burger, it looks (barely) like a burger, but it tastes just like incredibly strong hot sauce."
    "The spice hits me instantly and it takes all of my willpower not to instantly spit everything out."
    "I barely manage to swallow, then have to practically down the nearby glass of water."
    "My exaggerated reaction clearly caught [bree.name]'s attention, the next time I look at her she's no longer curtsying and has a concerned expression."
    show bree talkative
    if bree.flags.mikeNickname:
        bree.say "Is something wrong, [hero.name]?"
    show bree normal
    menu:
        "Was this a joke?":
            $ bree.sub += 2
            "I react without thinking, the burning sensation in my throat being my main focus and heightening my annoyance."
            "Convinced it's a practical joke, I glare at [bree.name] for a moment, before realising it was, in fact, a genuine attempt."
            "Guilt twinges at me as I force myself to calm down, quickly trying to give an explanation."
            mike.say "I mean, it's really spicy!"
            mike.say "Did you make it out of crystallised hot sauce?"
        "That's really spicy!":
            mike.say "I mean, INCREDIBLY spicy, I couldn't taste anything aside from how hot it is."
    show bree cry
    if bree.flags.mikeNickname:
        bree.say "Oh! Um, I did put a bit of hot sauce in it, [hero.name], I must have used too much."
    bree.say "Accept my deepest apologies for the mistake!"
    show bree gloomy
    "She bows so quickly that for a second I'm scared she's going to slam her head straight through the table."
    "Fortunately, she manages to dodge the stationary object, but she doesn't seem like she's about to go back to normal until I say something."
    mike.say "It's fine, it just caught me by surprise."
    mike.say "Maybe next time make it without the sauce. Get used to making a burger before you try to spruce it up."
    show bree talkative
    if bree.flags.mikeNickname:
        bree.say "Of course, [hero.name]! Once again, I'm truly sorry for serving you something subpar!"
    show bree normal
    "Even if I was furious, the look that [bree.name] gives me as she says that gives my stomach butterflies and causes me to choke on nothing at all."
    "She's really mastered the puppy dog eyes, I'm not sure if that came with practice or it's natural but it makes me feel guilty for her bad cooking."
    mike.say "It's fine, really. Let's just call that one a loss and try the others, alright?"
    if bree.flags.mikeNickname:
        show bree smile
        bree.say "Of course! Thank you, [hero.name]! You're truly kind!"
        show bree normal
    "I really hope she gets this job. Not just because we've worked towards it but because she'd make such a good maid."
    "Also I'd get to see her in the outfit."
    "It doesn't take long for me to try a few more things, there's no point in me finishing anything after all."
    "Just making sure it's not offensively bad."
    "Luckily, [bree.name] staying up all night seems to have paid off."
    "Everything aside from the burger is not only edible, but occasionally genuinely tasty. One or two things I'd actually pay for at a cafe."
    "She's still got a ways to go, but it's a significant improvement."
    "I let her know what I think of each meal after I try it, and if there was any leftover disappointment that her experiment had turned out poorly it quickly dissipated."
    "In fact, her spirits raise more and more after every bite, by the time I've finished she's practically shaking with joy."
    if hero.has_skill("cooking"):
        "I make sure to give proper constructive feedback, letting her know what needs to be changed or congratulating her specifically on what she's done well."
    else:
        "I try to give constructive feedback but I've never had much of a pallet beyond food being good or bad, she seems to appreciate it nevertheless though."
    mike.say "So yeah, not a great start but you've really come a long way."
    mike.say "I'm genuinely impressed. Well done."
    show bree happy blush
    "I'm thankful I'm sitting down, because I can tell from the way [bree.name]'s practically jumping with glee by now that she'd tackle me again otherwise."
    show bree smile
    bree.say "Yay~! I knew I could do it!"
    bree.say "Hehe! And it's all thanks to you!"
    show bree normal
    mike.say "Nah, you're the one who practised. This is your win."
    show bree smile
    bree.say "Hehe~! I'm feeling really good about my chances now, I think I might actually get the job!"
    if bree.flags.mikeNickname:
        bree.say "Like, I'm pretty sure I can act the part, right? You kept blushing when I called you [hero.name] at least!"
    show bree normal
    "Wait I did?"
    show bree smile
    bree.say "And if I can like, cook, that's already half the job locked down!"
    show bree normal
    mike.say "Glad to hear it, confidence is key. If you go in confident in your skills then you'll probably do better."
    show bree smile
    bree.say "Hehe! I'm almost excited now!"
    show bree normal
    mike.say "You need help clearing this all away?"
    show bree smile
    bree.say "Nope! What kind of maid would let her Goshujin-sama do all the work?"
    show bree normal
    "God-damn it. Now that she's mentioned it I can feel my cheeks flush, I must have been doing it this whole time."
    "Now I'm the embarrassed one, which doesn't help the blush fade."
    mike.say "Alright, if you insist."
    "I get up, brushing myself down of any crumbs or the like that clung to my shirt, when I'm caught off guard."
    show bree casual happy at center, zoomAt(1.85, (640, 1240)) with hpunch
    "Now that I was finally standing again, [bree.name] had once again tackled me and once again knocked the wind out of me."
    "I should have known this'd happen."
    mike.say "Oof! You caught me off guard then."
    show bree smile
    bree.say "Hehe! I know!"
    bree.say "Really though, thanks for all the help!"
    show bree normal
    mike.say "It's nothing, I mean it."
    "I pat her back, and try to ignore the two orbs on her chest that are pressed against me."
    show bree flirt at center, traveling(1.25, 0.3, (640, 880))
    "Slowly, I manage to pry myself away again, much to [bree.name]'s dismay."
    mike.say "Ugh, I have to go to work."
    show bree talkative
    bree.say "Oops! Sorry for keeping you so long!"
    show bree normal
    mike.say "It's fine, I just gotta dart."
    show bree smile
    bree.say "Hehe, bye [hero.name]!"
    show bree normal
    "I give her a quick wave, before slipping outside, muttering a few curses to myself for letting myself be so sidetracked."
    scene bg livingroom with dissolve
    "It isn't [bree.name]'s fault, she asked for the help of course but I could have said no or just hurried up, instead I dragged it out and gave it my all."
    "She's good company, if a little weird and invasive at times."
    "It's like she radiates an aura of joy, just being near her sometimes can make a dull day brighter."
    "In fact, because of that, I'm almost excited to take her to the interview tomorrow."
    "I just hope she doesn't mess it up."
    return

label bree_event_07b:
    if bree.love.max < 130:
        $ bree.love.max = 130
    scene bg street
    "The day has finally come, [bree.name]'s fated interview with the maid cafe."
    "A maid cafe being in my town is still a weird thought for sure, but I've long since stopped questioning it and started to appreciate my luck."
    "Maybe it's a super power or something, lately things have really been looking up for a few reasons."
    "Being around [bree.name] regularly is a definite big one."
    "Even now, as we stroll through the streets towards the cafe, instead of seeming anxious and nervous, clamming up and avoiding eye contact."
    "Anything that I would do in her situation really."
    "Instead of all that, she's literally skipping along, eagerly chit-chatting with me about, what else, but video games."
    show bree casual with dissolve
    "I feel like keeping her mind on the task at hand would be a better decision, but for all I know the task at hand is the reason she's talking so much about really anything else."
    "I don't want to start quizzing her or berating her for taking it too casually when it might just be her way of avoiding unnecessary stress. Besides, as I have to keep reminding myself."
    "She isn't a child."
    "I think that her outbursts when cooking or awkwardness when she first told me that she was going to struggle with rent were because of something other than weird circumstance."
    "She never really shows anything other than pure, unadulterated joy, so the instances where she's anything but are just that facade dropping for a moment."
    "After all, nobody can be that happy that often, she's just good at hiding when she isn't."
    "So if something makes her lose that mask it hurts to see that much more."
    "At least, that's my theory. I could be entirely wrong, I'm not a mind reader or anything, but that's all I can think of to explain her weird mood swings."
    "Well, that or she has some genuine mental illness, but for both of our sakes I hope that isn't true."
    show bree happy
    bree.say "So anyway, the news is that the next one's gonna be great!"
    show bree normal
    mike.say "Yeah, it sounds promising."
    "I base my response mostly off her tone of voice."
    "She isn't boring or anything like that, I just have this nasty habit of thinking too much sometimes."
    bree.say "Totally! Like, I wish I had an early copy or something!"
    show bree normal
    bree.say "Oh! We're here!"
    show bree normal
    "I look up from the floor where I was walking, but not quickly enough apparently, since before I know it [bree.name]'s hand has grasped my wrist and she's dragging me into a nearby building."
    scene bg maidcafe with fade
    pause 0.25
    show bree casual normal at left with easeinleft
    "I vocalise my objections but [bree.name] ignores me, and I find myself stood inside what I can only assume must be the maid cafe."
    "It's closed today, so no cute women walking around calling me master. Yet."
    show bree at center with ease
    "I get enough of that at home these days though."
    mike.say "I have to admit, some part of me still doubted that this place was real."
    show bree smile
    bree.say "Hehe! Of course it's real!"
    show bree at right4 with ease
    bree.say "You stay here, OK? I'm going to go talk to the owner!"
    show bree normal at right with ease
    "I give her a nod, then take a seat in a nearby empty chair."
    hide bree with easeoutright
    "Wait hold on a second."
    "HOW much for a coffee?"
    "In fact, looking closer, I see that pretty much everything on the menu is grossly overpriced, often going above double what I'd usually pay anywhere else."
    "I know the food at these places isn't exactly the main attraction but who in their right mind would pay this much?"
    "I'd assumed the place was closed thanks to the lack of people around, but now I'm not sure."
    "It could just be open and this is how busy it usually is thanks to this ridiculous pricing scheme."
    "Well, as long as they pay [bree.name] properly it shouldn't be an issue, until they close down that is."
    "But still, there go my plans of being a regular here. I doubt any amount of hot women in maid outfits could convince me to fork over 10{image=gui/icons/icon_money.png} for a coffee."
    "Actually they probably could, but that's why I need to stay far, far away."
    "Either way, the long, boring wait was luckily not used to anyone's advantage and I was not coerced out of a large amount of cash."
    "Instead I spent most of it on my phone, only really looking up when I heard two approaching pairs of footsteps from the area [bree.name] had entered."
    "I stood up and listened to the conversation, eager to find out how the whole thing went."
    "Manager" "I'm impressed, [bree.name]."
    "Manager" "VERY impressed!"
    bree.say "Thanks!"
    "Manager" "So - we open on Friday."
    "Manager" "Which means I'll need you here Friday at eight, sharp!"
    bree.say "Yeah! Totally! Thank you so much!"
    "This sounds promising."
    show bree casual happy zorder 1 at center, zoomAt(1.0, (740, 720))
    show kiara zorder 2 at center, zoomAt(1.0, (940, 720))
    with easeinright
    "The two round the corner and I see [bree.name], whose smile is pretty much her only facial feature."
    show bree normal at center, zoomAt(1.0, (340, 720)) with ease
    "Much like she had when I'd praised her cooking, she practically shakes with joy."
    "The woman next to her is, in contrast, a picture of calm confidence."
    "Though she's visibly mature in comparison to [bree.name], she all but exudes sexuality as she strides into the room."
    show kiara talkative
    "Manager" "Oh, well hello there."
    "Manager" "Now how on earth did you manage to sneak in here?"
    "Manager" "We're not even open yet!"
    show kiara smile
    "Is she...is she flirting with me?!?"
    show bree normal at center, traveling(1.85, 0.3, (440, 1240))
    "But before I can say a single word, [bree.name] rushes over to me and performs what is quickly becoming her signature half-tackle-half-hug."
    show kiara normal
    with hpunch
    "It catches me by surprise even though it's becoming routine."
    show bree smile
    bree.say "This is [hero.name]! He's my friend, he came for moral support!"
    show bree normal
    "As I wince from the impact, I give the striking older woman all of the greeting I can manage."
    mike.say "Hey."
    show kiara talkative
    "Manager" "A pleasure to meet you, young man."
    "Manager" "You know, you two make quite the cute little pair..."
    "Manager" "We are on the lookout for male staff - butlers, to be specific."
    "Manager" "The hours are good and the pay is pretty high for the industry."
    "Manager" "And the perks are VERY generous, if you impress the management..."
    show kiara normal
    show bree happy blush at center, zoomAt(1.5, (440, 1740)), vshake
    "[bree.name] gasps, breaking her hold on me prematurely."
    show bree smile
    bree.say "Woah! We could work together!"
    show bree normal
    mike.say "Uh, thanks but I've already got a job. I don't think I'd make a good butler either."
    show bree annoyed -blush
    "I'm not the type that thinks calling strangers 'Master' or 'Mistress' all day would be fun."
    "Well, maybe the latter, but in a different context."
    "Also I'm still not convinced this place will be here in a month, so quitting my job for a lower paid position here just feels like a terrible decision."
    show kiara whining
    "Manager" "Well I'm sorry to hear that, Sir, really I am."
    show kiara talkative
    "Manager" "If you have any friends as cute as you, then please, you send them my way!"
    "Manager" "We're counting on having the calibre of staff to wow anyone that walks in through the door - man or woman."
    show bree normal
    "Manager" "Hence my interest in making sure that [bree.name] here is front and centre."
    show kiara normal
    "The woman's got one of those voices, able to make just about anything sound suggestive, yet remain bafflingly respectable at the same time."
    show bree casual at center, traveling(1.25, 0.3, (440, 1210))
    "[bree.name] either doesn't notice or is ignoring it in the hope of making a good impression."
    show bree smile
    bree.say "Hehe! Thanks madame manager! I'm glad like, all of my hard work paid off!"
    show bree normal
    show kiara talkative at center, traveling(1.25, 0.3, (940, 880))
    "Manager" "That it did, [bree.name]."
    show kiara normal
    "The woman literally pets [bree.name] like she's some kind of cat, which makes me feel funny inside, but [bree.name] doesn't question it. Then, she turns to me again."
    show kiara talkative
    "Manager" "As I was saying to your friend, we do most of our training in house, but their dedication is stunning."
    show kiara normal
    "I don't bring up the fact that she left all of her practice until the last minute, or that she stayed up all night to do so."
    show bree smile
    bree.say "Hard work really does pay off!"
    show bree normal
    mike.say "Uh, guess so."
    mike.say "So, should we get going, [bree.name]?"
    "The two make a weird pair, but the woman seems nice enough and although I'm getting some major flirting from her, she doesn't seem malicious."
    "It doesn't make me overly eager to stick around though."
    show bree happy
    bree.say "Yeah! Totally! Thanks again madame manager!"
    show bree normal
    show kiara talkative
    "Manager" "Not a problem, [bree.name]. Farewell to both of you."
    show kiara smile
    show bree at center, zoomAt(1.25, (340, 1210)) with ease
    "The woman bows as we leave, and I realise what she was doing."
    scene bg street
    show bree casual at center, zoomAt(1.25, (640, 880))
    with fade
    mike.say "So uh, did she do the entire interview in character?"
    show bree talkative
    bree.say "Hmm? Oh, madame manager? Yep!"
    show bree smile
    bree.say "She was like that when we talked on the phone too! Cool, isn't it?"
    show bree normal
    mike.say "I'm not sure 'cool' is the right word for it, but sure."
    show bree smile
    bree.say "She's like, really dedicated!"
    show bree normal
    mike.say "Guess so. I can't imagine working with someone like that though, it'd get pretty tiring pretty quick."
    show bree smile
    bree.say "Maybe! But at least I'll have the chance to find out~!"
    show bree b normal at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound spank
    "She beams up at me, and raises a hand. It takes me a few moments to realise what she wants, and I give her a high five."
    show bree happy
    bree.say "We did it, [hero.name]!"
    show bree normal
    mike.say "No, you did it [bree.name]."
    mike.say "This is your win."
    show bree smile
    bree.say "Hehe! But I wouldn't have done it without your help!"
    bree.say "Come on, let's go celebrate!"
    show bree normal with vpunch
    "I feel her hand once again grasp my wrist as she begins dragging me down the street."
    mike.say "Woah! Where are we going?"
    show bree smile
    bree.say "To celebrate!"
    bree.say "There's a really good pizza place down here and it's got some arcade machines!"
    show bree normal
    "Sounds like [bree.name]'s kind of place. In fact, it sounds like mine too, so I'm in no place to judge her."
    mike.say "Fine, but why are you dragging me?"
    "[bree.name]'s surprisingly fast, and we're practically sprinting, it's a genuine effort to keep up with her, and pulling me isn't helping with my balance either."
    "It feels like I'm perpetually about to fall over."
    show bree smile blush
    bree.say "Because I'm excited~!"
    show bree normal
    "If anything, my complaints make her speed up much to my dismay. It's a miracle I'm not met with a face full of the floor before we arrive."
    show bree happy
    bree.say "Tada~!"
    show bree normal
    "Finally, she releases me, just to gesture up towards the building we're stood outside of."
    show bree normal -blush
    "It's a pizza place alright, it doesn't look that impressive either."
    "Maybe it's just because I'm fresh from the Victorian cafe, but it's definitely not something worth the fanfare that [bree.name]'s giving it."
    "I also might just be a little grumpy because I've been left winded by the run here, in fact I might have to start bringing an oxygen canister when I hang out with [bree.name]."
    "It seems like I'm always out of breath for one reason or another when I'm with her."
    mike.say "Great, looks good?"
    "I can tell from the deep breaths [bree.name]'s taking that she's also out of breath, she's just hiding it well."
    show bree smile
    bree.say "Come on! Let's go sit down!"
    scene bg restaurant with fade
    pause 0.25
    show bree casual at center, zoomAt(1.5, (640, 1040)) with easeinright
    "That doesn't stop her from trying to grab me again, but this time I deftly avoid her grasp and head in on my own volition."
    show bree at center, zoomAt(1.5, (640, 1140)) with ease
    "The two of us take a seat and order our food, plain cheese for me and one of everything for [bree.name]."
    mike.say "So, the interview?"
    "I'm eager to find out whether anything we'd practised had actually come up, or if the entire charade had only served to boost her confidence."
    "Either way, it worked."
    show bree smile
    bree.say "Yeah! So most of it was like, her asking me questions about like, maids!"
    bree.say "She seemed to really care about it being authentic or something?"
    bree.say "Either way she seemed really impressed by my act!"
    show bree normal
    mike.say "Well yeah, it's great."
    mike.say "You really hit the nail on the head with it."
    show bree happy
    bree.say "Hehe! Thanks!"
    show bree smile
    bree.say "She even said that she already has a uniform in my size in storage!"
    bree.say "Something about it being custom made for someone else because of their bust then them quitting and it going unused."
    show bree normal
    "That can't have hurt her chances, but I don't want to insinuate she got the job because of her looks, so I just nod along."
    show bree smile
    bree.say "Oh! And she said most of what people order is just coffee, and I make plenty of that myself, so I'm like, all set!"
    show bree normal
    mike.say "Sounds like a pretty easy job then if the whole maid thing comes naturally."
    show bree happy
    bree.say "Hehe! I hope so!"
    show bree smile
    bree.say "I mean I don't wanna complain or anything, but it doesn't pay enough to be like, really taxing and difficult."
    bree.say "Enough for rent though! She even like, gave me an advance so I'm all set!"
    if bree.flags.debt:
        bree.say "Oh! Speaking of which!"
        show bree normal
        "[bree.name] pulls a bill out of her pocket and pushes it towards me."
        show bree smile
        bree.say "Here's your money back!"
        show bree normal
        mike.say "What money?"
        show bree smile
        bree.say "You like, gave me rent money a while back, remember?"
        bree.say "I'm paying you back!"
        show bree normal
        menu:
            "Take the money":
                $ hero.money += 50
                mike.say "Oh yeah, thanks."
                "I take the cash and pocket it, now just a little richer."
                show bree smile
                bree.say "No problem! Thank YOU for letting me borrow it!"
                show bree normal
            "Don't":
                $ bree.love += 2
                "I shake my head, and push the money away, much to [bree.name]'s confusion."
                mike.say "It was a gift, you don't need to give it back."
                show bree smile
                bree.say "Really? Are you sure? I can afford it now!"
                show bree normal
                mike.say "Yeah, I'm sure."
                show bree happy
                bree.say "Alright! You're the best [hero.name]!"
                show bree normal
    mike.say "I'm just glad you're financially stable now."
    "I'm cut off by the pizza arriving, and after quickly thanking the waiter, I realise that this is my chance."
    "I'd been curious about a few things, mostly about her education."
    "I remember her telling me that she quit her last job for school, but she seems entirely disinterested in studying."
    "I hadn't wanted to be nosy, but it was as good a topic as conversation in my eyes."
    mike.say "So, how's university going?"
    show bree surprised
    bree.say "Huh?"
    show bree stuned
    "The question seemed to take her off guard, and I have to repeat it once before I get an answer."
    show bree smile
    bree.say "Oh! It's like, good! I told you I was like, gonna be a doctor, right?"
    show bree normal
    mike.say "Yeah, I think so, but you never really talk about it."
    show bree happy
    bree.say "Hehe! That's because it's boring~. At least it is compared to video games!"
    show bree normal
    mike.say "Yeah, I never liked school either."
    mike.say "It's important though, you just have to power through."
    show bree annoyed
    bree.say "Yep, I guess."
    "Oh boy, I think I said something wrong."
    "[bree.name]'s expression dropped for a moment as she stared down intensely, coincidentally at her pizza which made it seem a touch humorous but I try my best to take her seriously anyway."
    show bree sadsmile
    bree.say "I mean, yep! Totally!"
    show bree normal
    "That was perhaps the least I'd ever believed anything [bree.name]'s ever said."
    mike.say "If you disagree you can just say so, you know?"
    show bree talkative
    bree.say "No! I mean, it's not that I disagree! You're right!"
    show bree sadsmile
    mike.say "Then?"
    "[bree.name] visibly hesitates, they seem torn for some reason. I do what I usually do, stay quiet, I don't push her and leave her to decide between whatever she's deciding between herself."
    show bree hesitating
    bree.say "Alright. So like, I guess you've noticed I don't go to class a lot?"
    show bree normal
    mike.say "Yeah?"
    "It was one of the first things I'd noticed that was off about her actually, but I don't tell her that."
    show bree annoyed
    bree.say "Well like, I actually really, really don't want to be a doctor."
    bree.say "I think what they do is great and all, but I'm just really squeamish!"
    show bree sad
    bree.say "I uh, only realised that too late though and I'd already like, paid my tuition."
    show bree sadsmile
    "That sounded quite short sighted, but not all that out of character for her."
    "I could believe she'd do something like that, but something about her explanation still sounded fishy, I just couldn't quite figure out what."
    "Maybe I should just drop it, [bree.name] is my friend after all, it's weird for me to keep interrogating her like this. I just want to know more about her and she isn't offering much."
    "I'm tired of speculating and guessing, it still feels like we're strangers at times."
    mike.say "Well, you had good intentions at least. That's just a lot of money to waste."
    mike.say "Why don't you see if you can talk to the university? You might be able to sort something out, swap to a different course or just get at least some of your money back."
    show bree smile
    bree.say "Well like, it isn't that simple? It's really hard to explain, but I would if I could!"
    show bree normal
    mike.say "If you don't want to tell me, that's fine."
    mike.say "I can't make you and it'd be rude if I insisted anyway."
    show bree smile
    bree.say "Really? Thanks [hero.name]!"
    bree.say "I really don't like, mean any ill will by it, it's just a complicated situation and like, I don't want to bring down the mood!"
    bree.say "We're like, celebrating! Shouldn't we keep things light?"
    show bree normal
    mike.say "You're right, sorry for asking."
    show bree smile
    bree.say "It's fine! So~."
    bree.say "What do you think of the manager?"
    show bree normal
    "I'm convinced she only asked as a desperate way to change topics. Whatever it is keeping her from talking about university is something I'm not about to discover today."
    "At least I learnt a little about why she doesn't want to go to class, if she's avoiding it then getting a full time job isn't that unusual, and neither is spending all day in bed."
    "Well no, that last part is still weird, but understandable."
    mike.say "The manager? She seems alright. Does she have a name though?"
    show bree talkative
    bree.say "I don't know! She just introduced herself as the manager!"
    show bree normal
    mike.say "Weird."
    show bree talkative
    bree.say "Very! But like, what did you REALLY think of her?"
    show bree normal
    mike.say "Really think of her?"
    show bree hesitating blush
    bree.say "Yeah! She's gorgeous, right?"
    show bree normal
    "I have no idea what [bree.name] is talking about now, and I'm almost afraid to humour her."
    mike.say "I don't know, sure I guess? What about it?"
    show bree smile
    bree.say "Hehe! She was totally hitting on you!"
    show bree normal
    "What?"
    mike.say "What? Wait, really?"
    show bree smile
    bree.say "Yeah! I wouldn't joke about something like that!"
    bree.say "Like, did you not notice?"
    show bree normal
    mike.say "No I didn't notice! Is that why she offered me a job?"
    "That explains all the weird vibes I was getting from her, I just thought it was because of the persona she was putting on."
    show bree smile
    bree.say "Duh! I was gonna give her your number!"
    show bree normal
    mike.say "Woah woah woah, I don't see why you need to do that."
    show bree happy
    bree.say "Hehe! Wow, you're pretty oblivious aren't you?"
    show bree normal
    mike.say "Well I didn't THINK I was."
    show bree smile
    bree.say "Oblivious even to your own obliviousness!"
    show bree normal
    mike.say "How was I supposed to know she was flirting? She's way older than us."
    show bree flirt
    bree.say "Well yeah! Obviously! But like, I think that even if it was someone our age you wouldn't have realised~!"
    show bree normal
    mike.say "What's THAT supposed to mean?"
    "Was [bree.name] flirting with me now? Or was she just messing with me?"
    "Her laughter was clearly at least somewhat at my expense, even if I laughed along."
    "She couldn't be flirting with me, she must just be trying to twist and confuse me now."
    mike.say "I'd definitely have picked up on it if it was a younger girl, trust me."
    show bree talkative
    bree.say "Are you sure~?"
    show bree normal
    "Am I sure? Gah, she really is twisting me around her finger."
    mike.say "I'm sure."
    show bree smile
    bree.say "Hehe! Then I'll take your word for it~!"
    show bree normal
    mike.say "You should, I'm very trustworthy."
    show bree smile
    bree.say "Of course! You've never lied to me at least!"
    bree.say "It's one of your best qualities!"
    show bree normal
    mike.say "Not my natural charisma or athletic prowess? Or what about my amazing wit?"
    show bree smile
    bree.say "Well duh! Of course all of those!"
    show bree normal
    "I laugh again, and take a bite of my meal. I can't tell if she really thinks that highly of me or if she's just joking and being nice, but either way it's nice to hear."
    "Don't get me wrong, I don't swoon to just every girl who compliments me, honest."
    "But whenever [bree.name] says something like that it makes my heart leap in my chest, she's just so consistently adorable and genuine that it means more coming from her."
    mike.say "I'm glad you recognise how amazing I am then."
    show bree smile
    bree.say "Of course! It's hard to miss~!"
    show bree normal
    "Wait is [bree.name] really flirting with me? I'm going to be hung up on this all day."
    "Do I flirt back or is she just being nice again? If I flirt back and she's just being nice she might get the wrong impression and get upset."
    "Or worse, she'll have endless ammunition to tease me. She wouldn't do that of course, but the option would always be there, looming over me."
    "But if I don't flirt I might just miss my chance."
    "Or am I imagining things entirely because she's convinced me that I missed it earlier?"
    "And how did she get into my head so easily to begin with anyway?"
    mike.say "I'm glad I make such a strong impression then."
    show bree smile
    bree.say "Yep! You do that if nothing else!"
    bree.say "I'm all finished with my pizza, I wanna go try some of the games! They got in a couple new machines!"
    show bree normal
    mike.say "You don't have to wait for me, go ahead. I'm taking my time."
    show bree happy
    bree.say "Hehe, thanks [hero.name]! Come join me quick, alright?"
    show bree casual at center, zoomAt(1.5, (640, 1040)) with ease
    pause 0.25
    hide bree with easeoutright
    "Before I can answer, she scrambles out of the booth and practically sprints over to the arcade cabinets sat over in the corner."
    "I'd practically left my pizza alone, to be entirely honest I wasn't all that hungry, it's why I chose something simple, but it still felt like a waste to just leave it to get cold."
    scene bg restaurant at dark, blur(5)
    show bree b casual evil
    with fade
    "I watched [bree.name] as I ate, as she very eagerly mashed buttons."
    "I once again got to see the way she gets oddly focused when playing, even if she was taking it more lightly than usual."
    "Predictably, my mind began to wander once again, that overactive imagination of mine acting up."
    "What if [bree.name] really had been flirting with me? She isn't the kind of person to do that casually. If she flirted with me, she probably genuinely likes me."
    "She does shower me with an awful lot of compliments, and she makes a lot of physical contact too, but as far as I know she's just like that."
    "I could ruin our friendship if I did something and was mistaken, so I can't make that risk."
    "That's assuming that I even wanted a relationship with her."
    "Am I ready for something as serious as being [bree.name]'s boyfriend would be? She's fun of course but it wouldn't be just a little fling."
    show bree happy
    bree.say "Hey, [hero.name]! Come look at this!"
    bree.say "They've got this racing game where you can play as a bunch of Nimtembo characters!"
    show bree normal
    "My train of thought is broken by me being summoned by [bree.name] herself, but that's for the best."
    "Whatever comes, worrying about it isn't going to do any good. In fact, I should follow her lead."
    "Focus on video games and just take things in their stride."
    "More people could do to be a little like [bree.name] in that way."
    mike.say "Sounds good, dibs on Muria!"
    "We spend a shameful amount of time playing video games until the restaurant closes and we're kicked out."
    scene bg street with fade
    "I walk [bree.name] home, I tell her to get a few early nights so she's fresh for training day, she all but tells me she won't, then we part ways."
    "I'm left alone to wonder exactly what the future holds for the two of us."
    $ bree.flags.schedule = "working"
    $ Room.find("maidcafe").unhide()
    return

label bree_maidcafe_bj:
    if bree.love.max < 140:
        $ bree.love.max = 140
    scene bg street
    "It's been a while since [bree.name] started working at the maid cafe, and for the most part I've avoided bringing the subject up."
    "The most I've seen of what she does there is catching a glimpse of her uniform when it's been hung on the back of her bedroom door."
    "I think she knows that I'm more than a little intrigued, and she seems to enjoy dropping it into conversations at random."
    "And as much as I try to look uninterested, I'm sure [bree.name] can sense that she's setting my imagination racing each and every time."
    show screen expression "smartphone_calling" pass ("Bree")
    show mikemc p speak casual smile at center, zoomAt (2.0, (840, 1360))
    with fade
    "So when she casually suggests that I meet her towards the end of her shift, I can hardly conceal my enthusiasm."
    bree.say "Hey, [hero.name]."
    bree.say "I can't talk for long, as I'm on my break."
    bree.say "But you wanna come down and pick me up when I get off?"
    show mikemc happy
    mike.say "Ah, yeah, [bree.name] - sure thing!"
    show mikemc smile
    "[bree.name] laughs at the eagerness in my voice."
    "And I can't help blushing as I make myself so damn obvious."
    bree.say "Okay, [hero.name] - see you then!"
    hide screen smartphone_calling
    hide mikemc
    with fade
    "As soon as the call is over, I glance at the time."
    "It's not too long before [bree.name]'s supposed to be coming off work."
    "But there's nothing to stop me hurrying down there right now."
    "That way I can spend a little more time hanging around the place."
    scene bg maidcafe with fade
    "And so that's how I come to be walking into the maid cafe just as the last customers of the day are leaving."
    "I remember the place from the time I came down to support [bree.name] at her interview for the job."
    "But I still can't help feeling a little nervous as I walk in through the door, looking around for a sight of [bree.name]."
    show bree b evil at right with dissolve
    "It's then that I see her, bending over one of the tables as she collects the soiled cups and plates on a tray."
    "I'm looking at her from behind, and she doesn't seem to notice me as she shuffles around the table."
    "Huh - what else is there to say?"
    "It's just plain old [bree.name] that I see every day in a maid's uniform, right?"
    "Ah, who am I trying to kid?!?"
    "Of course, she looks absolutely and utterly amazing!"
    "[bree.name] has on exactly what springs to mind when most people think of a maid's outfit."
    "A white head-dress and a matching apron over the top of a dangerously short black dress."
    "It's a perfect fit, showing off every curve and line of her body."
    "And I can honestly feel myself starting to get hot under the collar just looking at her in it."
    "But then I realise that I've been standing here, just staring at her in silence like a massive pervert."
    "It's all I can do to make a strangled coughing sound in order to get her attention."
    mike.say "Ahem..."
    show bree talkative
    bree.say "I'm sorry, sir - but we're just about to close for the evening."
    show bree normal
    "For a moment, I almost can't believe that I just heard [bree.name] speaking to me."
    "The tone of her voice and how she shapes the words, they sound so deferential and demure."
    "[bree.name]'s normally so brash and brazen that it comes as quite a surprise to hear."
    mike.say "B...[bree.name]?"
    show bree normal
    mike.say "It's me...[hero.name]."
    "At this she turns her head to gaze in my direction, still filling up her tray as she does so."
    show bree smile
    "[bree.name]'s eyes are full of amusement and her smile almost reaches up to her ears."
    show bree happy
    bree.say "Don't be silly, [hero.name]!"
    show bree smile
    bree.say "I know it's you - I saw your reflection in the window."
    bree.say "I just wanted to give you the full benefit of seeing me in character!"
    show bree normal
    "Only now does she stand up and turn to face me, balancing the tray deftly in one hand."
    show bree flirt at center with ease
    "Then she proceeds to do a little twirl, allowing me to see her from all sides."
    show bree smile blush
    bree.say "Well - what do you think?"
    show bree flirt -blush
    "I open my mouth to say something that I hope will be diplomatic, rather than dirty."
    "But the sight is so impressive that nothing comes out."
    "Instead my mouth just opens and closes in silence."
    show bree happy at startle
    "[bree.name]'s smile becomes wider still, and she giggles in plain delight."
    show bree smile blush
    bree.say "Oh, [hero.name] - you're actually lost for words!"
    bree.say "That's so cute!"
    bree.say "Why don't you have a seat while I finish closing up?"
    show bree flirt -blush
    "She breezes by me on her way towards the counter as she says this."
    show bree wink
    "But she pauses just long enough to look down at my crotch and give me a little wink."
    bree.say "If what you have going on down there will let you, that is..."
    show bree flirt
    "I try to keep from blushing as I sit down, fumbling with my stiff cock the whole time."
    show bree at left4 with ease
    "And while I admit I have no idea how long it should take, I swear [bree.name] takes her sweet time closing up."
    show bree at right4 with ease
    "I watch her all the while, and she seems to be making as much of a show of it as she can."
    "Every time she bends over or stretches just a little, everything moves in just such a way."
    show bree at left5 with ease
    "And every time she walks by where I'm sat, she moves with a rolling gait that makes my eyes bulge."
    show bree at left with ease
    "As she works away, [bree.name] keeps up a casual conversation with me."
    show bree talkative
    bree.say "I didn't know if I'd really like working here when I started."
    show bree smile
    bree.say "But the place has just grown on me so much since then."
    show bree normal
    mike.say "Uh...really?"
    show bree smile at top_mostleft with ease
    bree.say "Oh yeah - I think I have a natural talent for being a maid."
    bree.say "For waiting on someone's every need..."
    show bree flirt
    "She raises her eyebrows as she says this, underlining the point."
    show bree talkative blush
    bree.say "Have you ever wondered what it'd be like to have a maid of your own, [hero.name]?"
    show bree flirt -blush
    "I hear the sound of the lock turning on the door as [bree.name] says this."
    "And I turn around just in time to see her push the key between her breasts."
    mike.say "Ah, yeah...I guess so."
    show bree hesitating blush at left with ease
    bree.say "Well, how about we do a little roleplay, just you and me?"
    show bree normal
    mike.say "Y...yeah, [bree.name] - that sounds great!"
    show bree smile
    "[bree.name] smiles again, but this time she lowers her gaze just a little, not meeting my eye."
    bree.say "Very good, sir."
    show bree normal
    mike.say "Huh...what do you mean..."
    mike.say "Oh...OH...I see!"
    show bree evil at center with ease
    "Still refusing to look up at me, [bree.name] points at my groin."
    "The bulge down there is now quite visible and getting bigger by the moment."
    show bree evil at center, zoomAt (1.0, (640, 720))
    bree.say "I don't mean to presume, sir."
    show bree smile
    bree.say "But would you like me to help you with that?"
    show bree flirt -blush
    "I swallow hard at this, almost biting my tongue as I try to get my words out."
    mike.say "Y...yeah..."
    mike.say "I mean yes...yes I would."
    mike.say "Get over here right away."
    "I hesitate, as I know that the next line I have in mind might be a gamble."
    mike.say "Get over here and...put that mouth to better use!"
    show bree at center, traveling(1.5, 0.3, (640, 1040))
    "[bree.name] nods obediently and starts to walk over to where I'm sitting."
    "But all the same, I'm sure I can see her trying to suppress a giggle."
    show bree happy
    bree.say "Yes, sir."
    bree.say "Right away, sir."
    hide bree
    show bree maidbj nodick
    with fade
    "When she reaches me, [bree.name] kneels in front of me under the table."
    "The place is deserted and the blinds are all closed."
    "Nevertheless, I can't help feeling nervous and keep glancing around, as if we'll be busted any second."
    "But the same paranoia doesn't seem to be affecting [bree.name] in the slightest."
    bree.say "Your cock, sir."
    bree.say "Would you like me to suck it for you?"
    mike.say "That...that sounds g...good to me."
    "[bree.name] doesn't need to hear another word after that."
    "She immediately starts to undo my flies and then reaches inside of my pants."
    show bree maidbj -nodick
    "The very moment that she has my cock out, she leans forward to kiss the tip."
    "And then she begins to lick gently at the head, taking a little into her mouth at a time."
    "All the while she sighs pleasantly, making sounds that show how much she's enjoying herself."
    "It takes me a good while to realise that she's all I can actually hear, and that I've been holding my own breath."
    "But even when I begin to breathe again, I find that I keep missing a breath."
    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
    "As great as [bree.name]'s lips and tongue feel as they wrap around my cock, the sight of her is what really gets me."
    show bree maidbj suck
    "She looks like the perfect fantasy of a beautiful, desirable maid."
    "That and the exquisite manners she demonstrated just now are such a turn on."
    "And they make knowing that I have my cock in that same mouth thrilling as hell."
    "Then, as if to top it all off, [bree.name] looks up at me and meets my eyes for the first time."
    "They're just so big and wide, full of feigned innocence and purity."
    "All I can think is how much she's spoiling me with what I've had her do to me..."
    "It's enough to make me cum, and I make to pull out before I do so."
    "But [bree.name] takes a firm hold of me then, shaking her head in disapproval."
    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
    show bree maidbj suck cum
    with vpunch
    "I cum almost as she does this, making her cough and gag more than a little."
    pause 0.25
    with vpunch
    pause 0.25
    with vpunch
    show bree maidbj swallow cum
    "Though [bree.name] is quick to recover from this, and makes a point of swallowing down all that I have to give."
    "Afterwards, she delicately dabs at her lips and bows her head to me."
    hide sexinserts
    show bree maidbj nuzzle -cum
    bree.say "Thank you for that, sir."
    bree.say "It was so generous of you to give me so much!"
    bree.say "I look forward to the next time you want me to swallow you like that!"
    "I can't do anything, save for sitting there and panting away like an overheated dog."
    "But I do wonder if I should ask about retaining the services of this particular maid..."
    hide bree
    $ hero.fun += 2
    return

label bree_event_09b:
    if bree.love.max < 150:
        $ bree.love.max = 150
    scene bg maidcafe
    "Seems like [bree.name]'s taking to the job at the maid cafe pretty well."
    "I mean, I haven't seen her much since she started working there."
    "But when I have, she's constantly singing it's praises."
    "Look, I'll just come out and admit it - I thought the place would be crawling with creeps and perverts."
    "Girls dressed up as maids and all that, you know?"
    "But whenever I mention that side of things, [bree.name] just laughs and waves away my concerns."
    "Seems like the novelty of the place is enough to make it practically sleaze-free."
    "Well...that and the crazily high prices!"
    "I suppose that's one of the things that makes it feel legit, rather than cheap and tacky."
    "Which leads me to another confession - the prices are mainly what's keeping me away."
    "I'm not stingy, okay?"
    "I just don't like the idea of being convinced to part with my cash by girls in maid costume."
    "That just feels...wrong somehow..."
    "But I've decided that I'm going to put aside my reservations and visit the place."
    "Not because I want to be waited on by maids, you understand?"
    "I just want to show [bree.name] some solidarity, that's all."
    "She'll have to stay in character, of course."
    "Maybe even call me 'Master' while she's in that maid's get-up..."
    "Ah, what am I thinking?"
    "[bree.name]'s a popular, outgoing kind of girl - she's probably the first choice of each and every customer."
    "She already told me most regulars ask for their favourite maid by name."
    "Perhaps I'll have to settle for one of her equally charming colleagues instead?"
    "I guess I could just grin and bear it..."
    "Finding the cafe on my own isn't a problem."
    "I remember escorting [bree.name] there for her interview."
    "The place is just how I recall it, only now it's filled with customers and staff."
    "Now the decor, English Victorian by way of Japanese manga, makes a lot more sense."
    "Several maids bustle here and there, serving guys that fill the tables."
    "It's busy, but not chaotic."
    "And the atmosphere is more laid back and pleasant than I expected too."
    "For one thing, there's not the sexual tension that I'd thought would go along with this kind of thing."
    "At least there isn't until I see a familiar figure approaching me..."
    show kiara talkative with easeinright
    kiara.say "Ah, [hero.name]."
    kiara.say "It's such a pleasure to see you again."
    show kiara smile
    "I smile at the manager of the cafe, trying as best I can not to give off the wrong signals."
    "Which is hard, because almost everything about her seems to have a definite sexual undertone."
    "I remember [bree.name]'s warning about Kiara, about how predatory she can be!"
    mike.say "Y...yeah..."
    mike.say "It's a pleasure to see me - I mean you..."
    mike.say "I mean, hi!"
    show kiara tantrum at startle
    "Kiara tosses her head back and lets out a deep, genuine laugh at my tongue-tied answer."
    show kiara smile
    "The gesture is entirely casual."
    "Yet it's still infused with the sensuality that seems to run through her entire being."
    show kiara talkative
    kiara.say "Tell me, [hero.name] - are you here for business or pleasure?"
    show kiara smile
    "How does she do that?"
    "How does she make everything sound like a filthy innuendo?"
    mike.say "I...I came to see [bree.name]?"
    "To my intense relief, Kiara nods at this."
    show kiara talkative
    kiara.say "Of course, my dear, of course."
    kiara.say "I'll send her right on over to service you."
    show kiara smile
    mike.say "S...service me?!?"
    show kiara talkative
    kiara.say "As a customer, my dear."
    kiara.say "[bree.name] must behave in a professional manner while she's at work."
    show kiara smile
    "I nod hastily, understanding the implications of all Kiara just said."
    hide kiara with easeoutright
    "And it's all I can do to keep my cheeks from flushing at the mere thought of it..."
    "Kiara sweeps away across the cafe, and I hurry to an empty table."
    "Try as I might, I can't help feeling awkward and out of place."
    "As I wait for [bree.name] to appear, the fanciness and affected decor begins to get to me."
    "It's at once too sophisticated for me and yet obviously fake too."
    "I just don't understand how it's supposed to work or make me feel."
    show bree zorder 2 at right with easeinright
    "It comes as a massive relief when I finally see [bree.name] emerge from the back of the cafe."
    show bree at right5 with ease
    "I'll confess that I was expecting her to look like something out of a teenage fantasy."
    "And, of course, she does!"
    show bree at right4 with ease
    "The skirt is so short it's almost obscene."
    "And the rest of the outfit shows off everything that [bree.name] has to offer too!"
    show bree at center with ease
    "It's all that I can do to keep my jaw from dropping open..."
    show bree smile
    bree.say "Hey, [hero.name]!"
    show bree normal
    "It takes me a second to shake off my confusion and realise she's standing right in front of me."
    "I'd been so entranced as I watched her approach that it took me out of the moment."
    show bree talkative blush
    bree.say "[hero.name]..."
    bree.say "What's wrong?"
    show bree flirt -blush
    mike.say "N...nothing, [bree.name]..."
    mike.say "Nothing at all!"
    "A coy smile appears on [bree.name]'s face."
    show bree evil blush
    bree.say "You were taking in the view, weren't you?"
    bree.say "Do you like me in this kind of thing, huh?"
    show bree normal
    "As if she needs to underline the point, [bree.name] gives me a twirl on the spot."
    if not bree.is_sex_slave:
        mike.say "It..."
        mike.say "It really suits you, [bree.name]!"
        show bree happy
        bree.say "Aww, thanks, [hero.name]!"
        show bree smile
        bree.say "I wanted to bring it home to show you."
        bree.say "But Kiara wouldn't let me!"
        show bree normal
        "Well, there's a pretty good reason to be mad at her manager!"
        mike.say "Well, I've seen it now."
        mike.say "And it looks really great on you!"
        show bree smile
        bree.say "Thank you again, [hero.name]."
        bree.say "It means a lot, knowing you approve!"
        bree.say "Anyway - can I get you a drink, or what?"
        show bree normal
        mike.say "Oh, sure..."
        mike.say "Can I get one of those..."
        show kiara zorder 1 at right with moveinright
        kiara.say "Ahem..."
        kiara.say "[bree.name], a word, please."
        "[bree.name] jumps a little as her manager appears out of nowhere and taps her on the shoulder."
        show bree at right5 with ease
        "They walk a few steps off and I see [bree.name]'s demeanour change as she listens to the older woman."
        hide kiara with moveoutright
        "When she comes back over, she offers me a little bow."
        show bree talkative blush at center with ease
        bree.say "So sorry."
        show bree smile
        bree.say "How may I serve you, Master?"
        show bree flirt -blush
        "For a moment I don't know what's going on."
        "But then I recall the fact that [bree.name]'s supposed to be playing the part of an actual maid."
        "She'd all but dropped that with me out of familiarity just now."
    else:
        "I raise my eyebrows at [bree.name], looking surprised to hear her speak in that particular tone."
        show bree dazed
        "She seems puzzled for a moment, but then realisation dawns upon her."
        "Here at work, she's supposed to be playing the part of a prim and proper maid."
        "Asking me a question like that is way too familiar and out of character."
        "[bree.name] offers me a little bow by way of apology."
        if bree.flags.mikeNickname:
            show bree talkative
            bree.say "Please forgive me, [hero.name]."
            show bree normal
            "[bree.name] stands a little taller and stiffer, hands clasped behind her back."
            show bree hesitating
            bree.say "Do you approve of my dress, [hero.name]?"
            show bree normal
            mike.say "I do, [bree.name] - it looks very good on you."
            show bree happy
            show fx exclamation
            bree.say "Oh, thank you, [hero.name]!"
        show bree smile
        bree.say "And how may I serve you today?"
        show bree normal
    mike.say "A coffee, please - filter will be fine."
    if bree.flags.mikeNickname:
        show bree smile
        bree.say "One moment, [hero.name]."
    hide bree with easeoutright
    "And with that, [bree.name] drops a little curtsy and hurries off towards the kitchen."
    "Which leaves me to realise that my heart is pounding in my chest."
    "I'm grateful for being sat down, as my legs feel like jelly too!"
    "A quick check assures me that I haven't got a nosebleed - which is a bonus!"
    "But what's wrong with me?"
    "All I was supposed to be doing is coming down here to treat myself to a look at the maids."
    "And I haven't spared a second glance for any of them apart from [bree.name] the whole time!"
    "Seeing her in that maid's uniform, it makes me feel..."
    "Well, it makes me feel like I did that last time we had pizza together."
    "It makes me feel as though I really like [bree.name], as WAY more than just a friend."
    "We have been getting a lot closer since I started helping her out recently."
    "And I feel like she's been more inclined to seek me out as a result of that."
    "Yet I have no idea if she's starting to feel the same way about me too."
    "Geez, this is awkward!"
    "I don't want to misread [bree.name], or make her think I've only been helping her to get into her pants!"
    "But on the other hand, I'm worried about second-guessing the whole thing."
    "I'd hate to lose the chance of having something with [bree.name] because I was a massive coward..."
    show bree talkative at center, zoomAt(1.0, (640, 720)) with dissolve
    show fx question
    if bree.flags.mikeNickname:
        bree.say "[hero.name]?"
    bree.say "Is the coffee to your liking?"
    show bree normal
    "Surprised by [bree.name]'s return, I glance up at her and then down at the coffee."
    "It looks fine, just like a regular cup of joe."
    "But right now I'd take a cup of boiling acid if she offered me one."
    mike.say "Oh..."
    mike.say "Oh yeah, it looks great."
    mike.say "Thank you..."
    show bree smile
    "[bree.name] offers me a little smile."
    if bree.flags.mikeNickname:
        bree.say "I'm glad, [hero.name]."
    bree.say "You looked a little bit distracted just now!"
    show bree normal
    "Shit - am I really that easy to read?"
    mike.say "It's nothing really."
    mike.say "I guess I just have something on my mind, that's all."
    show bree happy
    "[bree.name]'s smile becomes that little bit wider."
    show bree at center, traveling(1.5, 0.3, (640, 1040))
    "And she leans in that little bit closer."
    if bree.flags.mikeNickname:
        show bree smile
        bree.say "Anything I can help you with, [hero.name]?"
        show bree normal
    "It's like she has this effect on me, that makes me just blurt it out."
    mike.say "It's a girl."
    mike.say "A girl that I like."
    mike.say "And I don't know if she likes me too..."
    mike.say "I...I want to be sure before I make a move."
    "I have no idea what I was expecting [bree.name] to say to that."
    "And I can't tell if she realises I was talking about her either."
    show bree stuned blush
    "[bree.name] seems to freeze up on the spot, eyes wide and cheeks turning red as I watch her."
    show bree surprised
    bree.say "I...I..."
    show bree at center, zoomAt(1.5, (840, 1040))
    show fx exclamation at right
    bree.say "I can't help with that kind of thing!"
    bree.say "Got to...got to go...NOW!"
    hide bree with easeoutright
    "And with that, she's gone, hurrying away across the cafe."
    "All I can do is watch her go, a stunned look on my face."
    "Shaking my head, I take a sip of my coffee."
    "Which, for the record, is very good after all."
    show kiara with dissolve
    kiara.say "Ahem."
    show kiara annoyed
    "I look up to see [bree.name]'s manager standing before me."
    show kiara talkative
    kiara.say "Whatever goes on between [bree.name] and yourself elsewhere is, of course, none of my business."
    kiara.say "But while she is here and working for me, she is very much my concern."
    kiara.say "So would you mind telling me what happened just now?"
    show kiara blank
    "For all that she flirts and flaunts herself, Kiara's tone is totally sincere."
    mike.say "I'm sorry..."
    mike.say "We were just discussing a girl that I like."
    mike.say "And I wanted [bree.name]'s advice on things..."
    show kiara blank
    "Kiara nods, as though I don't really need to say anything more than I already have."
    show kiara talkative
    kiara.say "And did you get [bree.name]'s advice, [hero.name]?"
    show kiara normal
    mike.say "Ah, no..."
    mike.say "She said she couldn't help me."
    show kiara talkative
    kiara.say "Well, here's my advice in place of hers."
    kiara.say "Be direct and be honest, [hero.name]."
    kiara.say "At least, that's what I'd do..."
    show kiara normal
    "I nod, realising that her advice is probably right on the mark."
    "Trying to prod [bree.name] into confessing her feelings for me was never going to work."
    "And also, maybe I was too quick to judge Kiara herself."
    "For all of the flirting and coming onto me, she does seem to care about her staff."
    mike.say "Thanks for the advice, Kiara."
    mike.say "You've given me a lot to think about."
    show kiara smile
    "She smiles in a way that I'm sure has undone many men in the past."
    show kiara talkative
    kiara.say "All part of the service."
    hide kiara with fade
    "I nod as I drain my coffee and stand up to leave."
    "[bree.name] hasn't reappeared, and part of me feels bad about walking out before she does."
    "But I wasn't lying when I said that I had a lot to think about."
    "And so I hurry out of the cafe, already trying to get my head into a better order."
    "Hopefully I can manage it before I have another chance to send [bree.name] fleeing for cover!"
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    $ hero.replace_activity()
    return

label bree_event_09c:
    if bree.sub.max < 75:
        $ bree.sub.max = 75
    scene bg livingroom
    bree.say "Hello?"
    bree.say "Who's there?"
    if bree.flags.mikeNickname:
        bree.say "Is that you, [hero.name]?"
    "At her use of honorifics, and the sound of her voice, I realise that I really do have something well worth looking forward to."
    "How could I be so dumb as to forget that [bree.name]'s here and waiting for me to come home every evening?!?"
    "I toss aside my coat and bag, heading for the kitchen with all haste."
    mike.say "It's me, [bree.name]!"
    mike.say "I'm home."
    if bree.flags.mikeNickname:
        bree.say "Welcome home, [hero.name]."
    bree.say "Oops..."
    bree.say "May I have permission to speak?"
    mike.say "Sure thing, [bree.name]."
    mike.say "But you need to be careful calling me that out loud."
    mike.say "What if Sasha heard y..."
    scene bg kitchen
    show bree apron
    with dissolve
    "As I enter the kitchen, I stop dead in my tracks and in what I was about to say."
    "[bree.name] has her back to me right now, standing in front of the work surfaces."
    "The amazing smell is coming from all the stuff she has bubbling away."
    "And she's wearing a cute little apron that completes the image of domesticity."
    "But none of that's what stops me."
    "What does that is the fact that she's literally wearing nothing else!"
    mike.say "B...b...b..."
    show bree happy
    if bree.flags.mikeNickname:
        bree.say "Don't worry about Sasha, [hero.name]."
    bree.say "She's out for the evening and won't be back until later."
    show bree smile
    bree.say "So I thought I'd take the opportunity to cook for you!"
    show bree normal
    "That said, [bree.name] turns to face me, smiling happily."
    "I thought losing sight of her back would be a disappointment."
    "But the view from the front is more than enough to compensate for its loss!"
    show bree smile blush
    bree.say "Do you like my apron?"
    show bree flirt -blush
    "All I can do is nod desperately, still unable to speak."
    show bree smile blush
    if bree.flags.mikeNickname:
        bree.say "Aww, I'm so glad, [hero.name]."
    bree.say "Everything is supposed to be a treat for you tonight."
    bree.say "The food is a treat for your tastebuds."
    bree.say "And my outfit's a treat for your eyes!"
    show bree normal
    "I'm so flabbergasted by the sight of her that I can only smile at first."
    "My brain's so scrambled that I almost say something about the whole thing being unhygienic!"
    mike.say "It...it sure is that, [bree.name]!"
    "[bree.name] clasps her hands together and does a bashful little bow."
    show bree smile
    show fx heart
    if bree.flags.mikeNickname:
        bree.say "I'm happy to have pleased you, [hero.name]."
    bree.say "Would you like to be seated?"
    show bree normal
    "And with that, I let her usher me to a place at the table."
    "[bree.name] sees me sat down and pours me a glass of wine."
    show bree evil at right with ease
    "That done, she returns to her cooking."
    "But she keeps on looking back over her shoulder, making sure I'm watching her."
    "Believe me, I'm not putting it on when I tell you I don't know what to say."
    "There's subdued lighting, candles and wine too."
    "The whole nine yards in terms of romantic cliches for an intimate meal!"
    "I honestly feel like one of those husbands from an old TV show."
    "You know, the ones where the guy works at the office all day."
    "And then he comes home every night to a meal cooked by his impossibly glamorous, sexy wife!"
    "In fact, I feel like a king!"
    show bree normal at center with ease
    "And when [bree.name] places the plate in front of me, she keeps up the act."
    show bree smile
    if bree.flags.mikeNickname:
        bree.say "There you are, [hero.name]."
    bree.say "I hope the steak is to your liking."
    show bree normal
    "I look at the contents of the plate and then back to [bree.name]."
    "She smiles hopefully as I cut a piece and place it into my mouth."
    "And to be honest, I have no idea what it tastes like."
    "I'm too busy staring at [bree.name] to notice!"
    mike.say "It's amazing, [bree.name]."
    mike.say "Best steak I ever tasted!"
    show bree happy
    "Like I'm going to say anything else!"
    "What kind of a moron would I have to be to ruin all of this by complaining about the food?!?"
    show bree smile
    if bree.flags.mikeNickname:
        bree.say "Oh, thank you, [hero.name]."
    bree.say "Hearing that from you makes it all worthwhile!"
    show bree flirt
    "I take another bite, still looking at [bree.name] as she watches on."
    "This morsel is a lot slower on its journey to my mouth."
    "Not least because her scrutiny is making me a little nervous."
    "I begin to chew the piece of steak, but talk around it this time."
    mike.say "Ah, [bree.name]..."
    mike.say "Are you gonna watch me eat every single mouthful?"
    show bree stuned blush at vshake
    "At this, [bree.name] almost jumps on the spot."
    "Her eyes go wide and she becomes instantly apologetic."
    show bree surprised
    if bree.flags.mikeNickname:
        bree.say "Oh, I am sorry, [hero.name]!"
    bree.say "Of course not - I was just so happy to see you enjoying my cooking."
    show bree smile
    bree.say "But thank you for reminding me to see to your other needs..."
    show bree flirt -blush
    "I raise my eyebrows at this, intrigued by just what those could be."
    "After all, she is standing there in nothing but an apron..."
    "I watch, still chewing the steak, as [bree.name] gets down on her hands and knees."
    "She gives me one last smile, and then crawls under the table."
    "I might have guessed what she was going to do down there."
    "But still, I can't help feeling a rush of excitement as I feel her unzipping my flies."
    scene bree kitchen bj
    show bree kitchen bj flaccid
    with fade
    "[bree.name] remains silent as she gently pulls my cock out of my pants."
    "And then I feel her begin to stroke and lick at it, bringing it to life."
    show bree kitchen bj rub
    "I keep right on eating the steak and drinking the wine the whole time."
    "After all, [bree.name] seems to have planned this whole thing out."
    "So it feels like the right thing to do to get the complete experience!"
    "While I start out chewing the steak with some gusto, I can't keep it up."
    "Pretty soon I'm feeling the warm, welcome sensation of [bree.name]'s mouth."
    "And she's so gentle that I find myself slowing down almost in sympathy."
    "She's already got her lips wrapped around the head."
    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
    show bree kitchen bj blow
    "And when she starts to swallow it deeper, I can't help moaning a little."
    "This only seems to encourage [bree.name], and she does more of the same."
    "Her speed increases too."
    "And I can picture her head, bobbing up and down under there!"
    "I can't keep from moaning some more, as though the food's just that good."
    show bree kitchen bj cumblow
    "Anyone walking in on me right now would probably assume this is the best steak ever cooked."
    "By now, [bree.name]'s arms are wrapped around my waist and she's all but deep-throating me."
    "I hadn't noticed, but I've almost made it the whole way through the steak too."
    "I'm sliding the last morsel through the sauce and pop it into my mouth."
    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
    with vpunch
    "And almost in the same moment, I feel myself explode inside of [bree.name]'s own mouth!"
    with vpunch
    pause 0.25
    with vpunch
    pause 0.25
    show bree kitchen bj open -blow -cumblow cummouth rub cumrub
    "She coughs a little in surprise, but soon regains her composure."
    "Then I feel her dutifully swallow as much as she's able."
    "She licks me clean afterwards, before putting my cock away inside of my pants."
    "I'm wiping my mouth on a napkin when she emerges from under the table."
    hide sexinserts
    scene bg kitchen
    show bree apron happy
    with fade
    "And she's mirroring me again by wiping her lips on the back of her hand."
    "[bree.name] smiles at me, eager to hear how I liked her efforts."
    mike.say "My compliments to the chef!"
    show bree apron flirt blush
    "[bree.name]'s cheeks flush with genuine pleasure at the praise."
    if bree.flags.mikeNickname:
        bree.say "Oh, thank you, [hero.name]."
    bree.say "And thank you for my supper too."
    bree.say "It was most delicious and satisfying!"
    "I smile and nod, still feeling like one of those old-fashioned guys."
    "Like the king of my very own castle."
    "But with a willing slave in place of a queen!"
    hide bree
    $ bree.sub += 2
    $ hero.fun += 2
    return

label bree_event_10b:
    if bree.love.max < 160:
        $ bree.love.max = 160
    scene bg livingroom
    "I haven't seen much of [bree.name] since the incident at the maid cafe."
    "You know, the one where I told her that I was into someone, but not that it was her?"
    "I still have no idea why she reacted in the way that she did."
    "Was it because she feels the same way about me?"
    "Was it because she just sees me as a friend?"
    "Or does she think I was talking about someone else and she's jealous?"
    "I don't have a clue whether it's one of those reasons or something I missed completely."
    "The only solution that I can think of is to take the bull by the horns."
    "So I've made plans to just come right out and tell [bree.name] how I feel about her."
    "If she feels the same way, then that's great."
    "If not, I might be humiliated - but at least it'll clear the air and let us start anew."
    "I'm going to do it tonight, after she gets back from her shift at the cafe."
    "Sasha's out until the early hours of the morning, so we'll have the house to ourselves."
    "Even so, I've cleaned the place up and invested in some candles and rose petals."
    "Hey, it's not like I want to encourage her to say no, is it?"
    "I'm ready long before [bree.name]'s due back."
    "And I feel a little odd sitting alone on the couch amongst the scattered rose petals."
    "But I tell myself this is the perfect chance to get my head in order, to figure out what I'll say to her."
    "Opening the bottle of wine I bought for the occasion and pouring a glass for myself just seems logical too."
    "After all, it's better for me to be relaxed, right?"
    "The only problem is that one glass turns into another."
    "And before I know it I'm dropping off on the couch."
    "I awaken some time later, stirred by the sound of the front door opening."
    show bree maid at top_mostright with moveinright
    "Before I can shake off the sleep and the effects of the wine, she's standing in the doorway."
    "I can't begin to guess what [bree.name]'s thinking right now."
    show bree at right with ease
    "She's just walked in on me, slumped on the sofa - which is nothing new."
    "But the sitting room is scattered with rose petals and illuminated with candle-light."
    "As I struggle to my feet, I begin to mutter, my words slurred and incomprehensible."
    "It's like I'm trying to apologise and tell her how I feel all at once."
    "Everything gets muddled together as it leaves my mouth."
    "And it all peters away into silence as I find myself staring at [bree.name]."
    "She's saying something, but I don't hear it."
    "All I can think is how beautiful she looks."
    "Yeah, she's tired and confused right now."
    "But I don't think I've ever seen a more desirable woman in my entire life!"
    show bree maid at center, zoomAt(1.5, (640, 1040))
    "Close the distance between us, wanting nothing more than to be closer to her."
    "As I do so, I can finally hear what [bree.name]'s actually saying."
    show bree talkative
    show fx question
    bree.say "...[hero.name]?"
    show fx question
    bree.say "Are you even listening to me?"
    show bree normal
    "God, I want her so much right now!"
    "I want to drink the finest wines with her."
    "I want to protect her from the rest of the world!"
    mike.say "[bree.name]..."
    mike.say "I want to give you wine and some protection!"
    show bree surprised
    show fx question
    bree.say "Huh?"
    bree.say "What are you even talking about?"
    show bree stuned
    "In my own mind, what I'm about to do makes perfect sense."
    "Words have failed me, but actions speak so much louder..."
    hide bree
    show bree kiss maid
    with fade
    $ bree.flags.kiss += 1
    "I wrap my arms around [bree.name]'s waist and plant my lips on her mouth."
    "She makes a yelping sound."
    "Which I hope is from surprise, rather than disgust."
    "All the same, I'm already bracing myself for a shove and a slap..."
    "But instead I hear [bree.name]'s yelp turn into a sigh, almost one of relief!"
    "At the same time, I feel her melt into my embrace."
    "[bree.name] drops her bag on the floor and wraps her arms around me."
    "By now she's kissing me with as much hunger as I am her."
    "All of the weariness seems to drain out of [bree.name] as we kiss."
    "And I can almost feel her come alive in my arms."
    "Suddenly there's no need for all of the clumsy, awkward words between us."
    "Our bodies are explaining themselves to each other with such natural ease."
    "I break the kiss a moment later, hearing [bree.name] panting as my lips leave her own."
    "My hands almost tear at the buttons of her coat, and I yank it off of her shoulders."
    "This exposes the maid's uniform that she still has on underneath."
    "I toss the coat aside, staring at the wide-eyed gaze [bree.name]'s giving me."
    "I want her, more than anything else that I can imagine right now."
    "But that doesn't mean that I'll take it without permission."
    "[bree.name]'s eyes betray the fact that she knows how desperately I desire her."
    "There's trepidation and maybe even a little fear in them."
    "Yet I sense that it's fear of the unknown, of giving into her urges."
    "And not fear of being hurt in a physical sense."
    "She nods, a tiny movement of the head."
    "But it's all the permission that I need."
    "I almost grab a hold of [bree.name] then, bundling her backwards and onto the couch."
    "We tumble over together, and she lands on her hands and knees."
    "There's only a split second before I'm on top of her, hands playing over her body."
    "[bree.name] moans and pouts at every touch and every squeeze, urging me onwards."
    "But what urging do I really need?"
    "The girl that I've been secretly longing for all this time is on all fours in front of me."
    "And what's more, she's dressed in a crazily hot maid's outfit too!"
    "My hands are already under [bree.name]'s short skirt, tracing the shape of her buttocks."
    "My fingers twine themselves in the elastic of her panties."
    "In one motion, I yank them down as far as her knees."
    "It only takes me a couple more seconds to unzip my fly and pull [bree.name] backwards."
    "Needless to say, I'm hard as a rock right now."
    "A fact that [bree.name] discovers as the head of my cock presses against her pussy."
    "It feels incredible, even from the outside."
    "Already getting nice and slick, I swear I can feel heat from it too!"
    "I pause for a moment, until [bree.name] looks back over her shoulder at me."
    "She's biting her tongue in anticipation, nodding too."
    "She wants this!"
    "She wants this as much as I do!"
    bree.say "Do it..."
    bree.say "Please, [hero.name] - what are you waiting for?"
    bree.say "Fuck me already!"
    "That's all the encouragement I need."
    show bree missionary vaginal arm with fade
    "And a moment later, I plunge my cock into [bree.name] without holding anything back."
    "The groan that she lets out as I do so is more animal than human."
    "It sounds like all of the built-up frustration and desire inside of her is being let out."
    "Is that how it is?"
    "Has she been this tied-up in knots over me?!?"
    "Whatever the truth might be, I know that's how it is from my side of things."
    "I can't keep from thrusting into [bree.name] like my life depends on it."
    "My thighs are slapping into hers so hard that it's like a round of applause."
    show bree missionary vaginal arm pleasure
    "She's shaking from that and the sensation of me being buried so deep inside of her too."
    "I'm not thinking about how hard I'm fucking [bree.name], just enjoying the moment."
    "And she's taking all that I have to give without the slightest hint of a complaint either."
    "Breasts, belly and thighs, I can feel each and every curve of her body as it moves."
    "As much as I wish this would never end, we can't go on like this forever."
    show bree missionary vaginal arm ahegao creampie with hpunch
    "I cum first, pushing myself as deep into [bree.name] as possible at that moment."
    with hpunch
    "She wails as I fill her, quivering around me as it begins to seep out of her and down her thighs."
    with hpunch
    "[bree.name] cums perhaps a couple of seconds later, the walls of her pussy clasping my cock tightly."
    "And then her legs buckle beneath her, sending [bree.name] sliding off me and onto the sofa below."
    "I follow her down, panting and sweating like crazy."
    mike.say "B...[bree.name]..."
    mike.say "It's you..."
    mike.say "The girl I like...it's you..."
    show bree maid topless flirt blush -cum zorder 1 at center
    bree.say "Y...yeah...yeah..."
    bree.say "I kinda guessed..."
    "[bree.name]'s cheeks are flushed red and she's a mess of crazy hair and dishevelled clothes."
    "But her eyes are alive with an affection that can't be mistaken for anything else."
    show fx heart zorder 2 at center
    bree.say "I kinda like you too!"
    "We just lie there for a while, cuddling and enjoying the moment."
    "The sitting room looks like an explosion in a florist's shop."
    "The couch must stink of sex and sweat right now."
    "And I'm pretty sure that I tore [bree.name]'s uniform too."
    "But none of that's important, and all of it can wait."
    "[bree.name]'s all I can think about."
    "All that I want to think about."
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    call sleep ("bree") from _call_sleep_46
    $ game.room = "bedroom1"
    return

label bree_event_11b:
    if bree.love.max < 170:
        $ bree.love.max = 170
    scene bg livingroom
    "I thought that I'd gotten away with it, the way that I practically jumped on [bree.name] the other night."
    "After all, it wasn't like she didn't throw herself into it and have a good time too."
    "Sure, it wasn't supposed to go that way, but I was convinced that it turned out for the best."
    "That was until the very next morning, when [bree.name] was conspicuous by her absence."
    "She'd either left early or else slept in while I was getting up and leaving for work."
    "I didn't see her the next evening either, and normally I'd have passed it off as a coincidence."
    "But the way we left things, I can't help thinking that she's deliberately avoiding me."
    "And that's why I end up sitting up late on the sofa, just waiting for the sound of her coming home."
    "It's only as I hear the sound of the front door opening that I realise the mistake that I've made here."
    "Glancing around, I see that, save for the rose petals and candles, this is a rerun of the other night!"
    show bree casual at right with easeinright
    "Before I can do anything about it, there she is, standing in the doorway once again."
    "I'm up and on my feet the very next second, waving my hands in the air."
    mike.say "[bree.name], I..."
    mike.say "This isn't what it looks like!"
    show bree surprised
    show fx question at right
    bree.say "Huh?!?"
    bree.say "What are you..."
    show bree stuned
    mike.say "I mean I'm not going to pounce on you again!"
    "I see [bree.name]'s eyes go wide for a moment."
    "And I'm all but convinced that I've made a massive mistake."
    "What if she's been avoiding me because she's changed her mind about the other night?"
    "What if she's thought it through and come to the conclusion that I took advantage of her?!?"
    show bree flirt
    "But then she smiles and looks away, her cheeks reddening just a little."
    show bree evil blush
    show fx question at right
    bree.say "Aw, really?"
    bree.say "How'd you know that I wasn't up for it?"
    bree.say "How'd you know I wasn't hoping you might?"
    show bree flirt
    "It takes a few seconds for what [bree.name]'s saying to actually sink in and make sense."
    "I'd been so sure I needed to expect the absolute worst, anything else doesn't quite click."
    mike.say "Y...you mean..."
    mike.say "You want me to do it again?!?"
    mike.say "Because I can..."
    "I make to close the distance between us."
    show bree normal blush casual at center, zoomAt(1.5, (640, 1040)) with hpunch
    "But my movements are clumsy and awkward this time."
    "[bree.name] holds up a hand, shaking her head gently."
    "The whole time her smile is warm and understanding."
    show bree smile
    bree.say "It's okay, [hero.name]."
    bree.say "You don't have to do it on command, like a performing seal or something!"
    bree.say "And it's not the same when I know it's forced, yeah?"
    show bree normal
    "I nod, still desperate to know that I'm doing the right thing."
    mike.say "But...you're cool with what happened, right?"
    "[bree.name] takes hold of my hands in her own, looking up at me intently."
    show bree smile
    bree.say "Yeah, [hero.name]."
    bree.say "It was a little scary at first."
    show bree evil
    bree.say "But really exciting!"
    show bree normal
    mike.say "I was just trying to tell you how I felt about you, [bree.name]."
    mike.say "Everything was bottled up inside of me."
    mike.say "I guess I just got carried away..."
    show bree smile
    bree.say "You sure did."
    bree.say "It felt like a champagne bottle going off inside of me!"
    show bree normal
    mike.say "Yeah..."
    mike.say "Sorry about that!"
    show bree flirt
    "[bree.name] shakes her head, dismissing my apology."
    show bree smile
    bree.say "Don't be, [hero.name]."
    bree.say "In a way, I think you did us both a favour."
    bree.say "This way neither of us had to say how we felt and risk screwing it up!"
    bree.say "Lucky for us it just felt so right."
    show bree normal
    mike.say "So...do you want to do it?"
    mike.say "Not just the sex, I mean."
    mike.say "Us, you know - you and me?"
    show bree smile blush
    bree.say "So long as you promise to fuck me like that again!"
    show bree normal
    "I can't help staring at [bree.name] with my mouth open in surprise."
    show bree flirt
    "She flushes a deeper shade of red under my gaze, but she doesn't look away this time."
    "I swallow deeply as it dawns on me just what that condition means!"
    mike.say "Sure, [bree.name]."
    mike.say "If that's what you want?"
    show bree smile
    bree.say "You bet it is!"
    show bree flirt
    "[bree.name]'s eyes are full of desire as she says this."
    show bree smile
    bree.say "I can even wear the maid uniform, if you'd like?"
    show bree flirt
    "I nod, the memory of her in it and the promise of seeing it again filling my mind."
    "It makes me hard almost instantly, my heart pounding in my chest."
    show bree talkative -blush
    bree.say "Oh, but speaking of maids..."
    bree.say "I need you to do me a favour."
    show bree normal
    mike.say "Anything, [bree.name] - just name it!"
    show bree smile
    show fx exclamation at center
    bree.say "Aw, thanks, [hero.name] - you're the best!"
    bree.say "You see, I've been distracted since we fooled around the other day."
    bree.say "So much so that I was a complete disaster at work today."
    bree.say "And I told Kiara that I'd make it up to her somehow..."
    show bree normal
    "I'm not sure I like where this is going."
    "But it's too late to back out now."
    "I already promised [bree.name] that I'd help."
    "Plus there's the prospect of more maid sex on the cards!"
    show bree smile blush
    bree.say "But if you came along to help out on my next shift, you'd save my life."
    bree.say "Kiara seems to like you, so I'm sure she'd love it."
    show bree normal
    "Yeah, I bet she would!"
    "Most predators actually have to hunt down their prey."
    "They don't have it served up on a platter for their delectation!"
    mike.say "S...sure, [bree.name]."
    mike.say "I'd be happy to help!"
    show bree happy
    "[bree.name] nods and smiles, clearly over the moon with my answer."
    "But what do I really have to worry about?"
    "Most likely all they'll want me to do is help out in the kitchen or empty the bins."
    "Something like that, right?"
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    return

label bree_event_11c:
    if bree.sub.max < 100:
        $ bree.sub.max = 100
    scene tv
    show tv bree
    with fade
    "I used to get worried when I could tell that a girl like [bree.name] had something that she wanted to ask me."
    "You know how it is, when they just won't come out and say it?"
    "It's like they're bottling up something so important that it needs to come out at the exact right moment?"
    "Well, you might have thought that the kind of changes in the relationship I have with [bree.name] makes that a thing of the past."
    "But no, we still have that same situation arise now and then."
    "The only difference is that I have the pleasure of knowing that it's nothing I need to be worried about."
    "Instead I know that [bree.name]'s trying to summon up the courage to ask me for something."
    "And that it's probably going to be something that's enough to make her blush at the mere thought of it!"
    "Take tonight for example, we're just sitting on the sofa, watching some random crap on TV."
    "No one's saying a word, but all the same, I can feel the atmosphere in the room."
    "I keep catching [bree.name] looking at me sideways, like she's trying to catch my eye."
    "Maybe she thinks that I might see this and ask her what's up."
    "That way she can broach what's on her mind that much more easily."
    "But the truth is that I'm enjoying the chance to watch her squirm just a little."
    "This goes on for a while, until [bree.name] seems to reach breaking point."
    scene bg livingroom
    show bree dazed at center, zoomAt(1.5, (640, 1040))
    with fade
    bree.say "Erm..."
    bree.say "Ah..."
    show bree talkative
    bree.say "...[hero.name]?"
    show fx question
    bree.say "Hey [hero.name]...have you got a moment?"
    show bree blank
    "I make a point of turning down the sound on the TV as she says this."
    "And then I turn my head to regard her, making sure she knows that she's the centre of my attention."
    "Of course, all of this only serves to make her all the more nervous."
    mike.say "Yes, [bree.name]."
    mike.say "What's up."
    show bree normal
    "[bree.name] smiles and nods, thanking me for my indulgence."
    show bree flirt
    "But her cheeks are already flushing with colour."
    "And she struggles to say what's been eating away at her this whole time."
    show bree hesitating blush
    bree.say "Well..."
    bree.say "I was wondering if..."
    bree.say "If you were feeling...energetic tonight?"
    show bree flirt -blush
    "[bree.name]'s tone is so meek and polite."
    "And her choice of words is so careful, yet at the same time so awkward."
    "It's all that I can do to keep my face straight as I look into her eyes."
    mike.say "Hmm..."
    mike.say "I usually feel pretty tired on a weeknight, [bree.name]."
    mike.say "But I got more sleep than usual last night."
    mike.say "So yeah, I guess I am feeling a little more energetic than normal."
    mike.say "Thanks for asking."
    "I know full well that I was supposed to pick up on the less than subtle hint in what she said."
    "And in truth I'm more than up for some fun of a physical nature with [bree.name] tonight."
    "But it's just too good of a chance to tease her to the point of bursting."
    "So I go to turn back to the TV, pretending that the conversation is over."
    show bree hesitating blush
    bree.say "...[hero.name]?"
    bree.say "I meant to ask if you had enough energy for something else!"
    bree.say "If you might want to burn it off?"
    bree.say "Burn it off in an agreeable way?"
    show bree flirt -blush
    "My head's not even turned back the whole way."
    "But I already know what I'm going to say next."
    mike.say "Huh, you think I should, [bree.name]?"
    mike.say "I'm not really in the mood for a jog around the park."
    mike.say "Maybe we could break out the paddles and play table tennis?"
    "The smile is practically plastered on [bree.name]'s face by now."
    "And I can see the effort it's taking her to stay under control."
    show bree talkative blush
    bree.say "No, [hero.name] - that's not exactly what I meant!"
    show bree sadsmile
    mike.say "Well I'm sorry, [bree.name]."
    mike.say "But maybe you should just come out and say what you mean."
    show bree hesitating
    bree.say "I...I..."
    show bree talkative
    bree.say "I want you to fuck me!"
    show bree flirt -blush
    mike.say "What was that, [bree.name]?"
    mike.say "I think my ears might be too sensitive for that kind of language!"
    show bree talkative blush
    bree.say "I'm sorry, [hero.name]..."
    bree.say "I want you to make love to me...please?"
    show bree flirt -blush
    mike.say "Ah, I heard that alright, [bree.name]."
    mike.say "But I think you're going to have to convince me."
    mike.say "How about you show me just how much you want me to do that?"
    "[bree.name] nods in a demure fashion, already lowering her head a little."
    show bree talkative blush
    bree.say "Please, [hero.name]."
    bree.say "I would be most grateful if you'd make love to me."
    show bree flirt -blush
    "I raise my eyebrows, as if to suggest that she's on the right track."
    "But I hold back from giving into her just yet, sensing she might go further still."
    "And she does, clambering off of the sofa and onto her knees before me."
    "[bree.name] clasps her hands together, looking up at me with a pleading expression."
    show bree talkative blush
    bree.say "Oh, [hero.name], please!"
    bree.say "Please make love to me!"
    bree.say "I want you to touch me so much."
    bree.say "I want to feel you inside of me so badly..."
    show bree sadsmile
    "When she puts it like that, how can I even think of saying no?"
    mike.say "That's more like it, [bree.name]."
    mike.say "Good girls that ask nicely deserve to get what they want."
    mike.say "Now you take off your clothes and get down on all fours."
    "[bree.name] nods at this, eagerly hurrying to do as she's told."
    show bree normal naked at hshake with dissolve
    "I watch as she strips off every item of clothing that she has on."
    "And then lowers herself onto her hands and knees, waiting silently for me to join her."
    "I deliberately take my time taking off my own clothes."
    "This means that I can watch [bree.name]'s progress at my own leisure."
    "But it also serves to reinforce the point that I'm the one in charge."
    "And there's never any harm in letting the anticipation grow inside of her either."
    scene bree rough doggy
    show bree rough doggy livingroom
    with fade
    "So by the time I kneel down behind her, [bree.name]'s almost quivering with anticipation."
    "She glances back over her shoulder as I put my hands on her haunches."
    "And then she cries out in surprise as I pull her back and onto me."
    "As demure as [bree.name] might have been in asking for this, I won't be the same in giving it."
    "My cock is already as hard as can be, pushing against the lips of her pussy."
    show bree rough doggy vaginal -big -small -medium
    "It needs no help to find the sweet spot a moment later and begin to push its way inside."
    bree.say "Ooh..."
    bree.say "[hero.name]..."
    bree.say "Will you be gentle?"
    "She says this almost the same moment that the folds of her pussy part for me."
    "And the words become a moan of helpless surrender as I sink further into her."
    "But it's as if that last question were some kind of provocation in my mind."
    "Almost instantly, I begin to thrust in and out of [bree.name], setting a frantic pace."
    show bree rough doggy boobs
    "Before too much time has past, I'm literally pounding her for all I'm worth."
    "[bree.name]'s yelping now, crying out from the sensation of me inside her."
    show bree rough doggy pleasure
    "And almost as loud is the sound of my groin slapping into her buttocks."
    "To think that less than five minutes ago I was totally engrossed in watching TV."
    "And now all that's on my mind is making [bree.name] squeal as loud as I possibly can!"
    "Without thinking too much about it, I reach out with one hand."
    "She gasps as I grab a handful of hair and pull back on it."
    "The only chance that [bree.name] has to lessen the pain she's feeling is to go with it."
    "And so she begins to rise up on her haunches as I tug backwards."
    "Pretty soon she's almost in an upright position, riding my cock for all she's worth."
    "[bree.name]'s breasts bounce and swing as she takes everything that I have to give."
    "Her eyes look frantically backwards, wide and almost desperate."
    "But I can't tell if she's begging for mercy or urging me on all the more!"
    "And for all that [bree.name] seems to be on the brink of losing control, I know my own limits too."
    "I can't keep going like this forever, and the pressure's already building up inside of me."
    with hpunch
    "As I finally cum, I pull back on [bree.name]'s hair one last time."
    show bree rough doggy cum ahegao with hpunch
    "This means that I'm as deep in her as I can possibly be when I shoot my load."
    with hpunch
    "All of [bree.name]'s weight is on me too, so she takes all that I have to give."
    with hpunch
    "She cries out loud, and then subsides into almost a whimper as we come to an end."
    "And as soon as I let go of her hair, she collapses back onto all fours."
    show bree rough doggy -vaginal cum
    "[bree.name] slides off of my cock in one smooth motion, and it bobs up when freed from her body."
    "I kneel over her, looking down on her as she pants and sighs from the aftershocks."
    "And I have to admit that she was right."
    "This was a great way to burn off some energy."
    $ hero.cancel_activity()
    $ game.pass_time(2)
    return

label bree_event_12b:
    if bree.love.max < 180:
        $ bree.love.max = 180
    scene bg maidcafe at dark, blur(5)
    show bree maid smile at center, zoomAt(1.25, (940, 880))
    with fade
    bree.say "See, [hero.name] - I told you it'd fit, and it does."
    show bree happy
    bree.say "You look SO cute in it too!"
    show bree normal
    "We're in the back-room of the maid cafe where [bree.name]'s been working for the past few weeks."
    "I'm looking at my reflection in the mirror as she gazes over my shoulder, a smile on her face."
    "And all I can see is myself fidgeting with the uncomfortable butler's outfit she's forced me into."
    "I can feel my cheeks flushing red as [bree.name] coos over me."
    "And the sensation makes the collar around my neck feel that much tighter."
    mike.say "[bree.name]..."
    mike.say "Are you sure I need to wear this thing?"
    mike.say "I mean, I want to help out with your shift."
    mike.say "But this is..."
    show kiara talkative zorder 2 at center, zoomAt(1.25, (340, 880)) with easeinleft
    kiara.say "Just darling, darling."
    kiara.say "I knew you were perfect for that uniform!"
    show kiara smile
    "In my flustered state, I hadn't noticed [bree.name]'s boss sweep into the room."
    show kiara talkative at center, traveling(1.5, 0.3, (340, 1040))
    "But she wastes no time in leaning over my other shoulder."
    "She seems to want to get as close to me as she can."
    "The scent of her perfume and the cigarette she's smoking is all I can smell."
    show kiara talkative
    kiara.say "It's so kind of you to help out poor little [bree.name] here."
    kiara.say "And it'll be so nice to have a man around the place for a change too."
    show kiara normal
    "I have [bree.name] looking over one shoulder and Kiara over the other."
    "So the best I can manage in way of a response is a dumb grin and a shrug."
    show bree smile
    bree.say "Yeah, [hero.name] - you're a saviour for doing this."
    show bree flirt
    show kiara talkative
    kiara.say "We'll have to think of how we can repay your kindness..."
    show kiara normal
    "Right then my eyes go wide and I almost let out a yelp of surprise."
    "Someone just pinched my ass!"
    "One of them reached out and had a good squeeze!"
    "Sure, these pants are super-tight."
    "And they show off all the hard work I've been putting in down the gym recently."
    "But still, what do they think I am - a piece of meat?!?"
    show kiara talkative
    kiara.say "Okay, you two."
    kiara.say "Time to open up!"
    kiara.say "[bree.name], be sure to show [hero.name] the ropes."
    show kiara normal
    show bree smile
    bree.say "Sure thing, boss!"
    hide kiara with easeoutleft
    bree.say "Come on, [hero.name] - you heard what Kiara said."
    bree.say "This is going to be so much fun!"
    show bree normal
    mike.say "Ah, yeah, [bree.name]..."
    mike.say "I'm having a great time already..."
    scene bg maidcafe
    show bree maid at left
    with fade
    "[bree.name] leads me out into the cafe itself and busies herself opening up."
    show bree maid at center with ease
    "She walks me through everything that I need to know before opening the doors."
    show bree smile
    bree.say "Okay, [hero.name], here goes."
    bree.say "And don't worry - I just know you're gonna be fantastic!"
    show bree normal
    mike.say "If you say so, [bree.name]..."
    hide bree with dissolve
    "And you know what?"
    "She's right!"
    "I find it a little hard-going at first, but there's really not that much to it."
    "Well, apart from the uncomfortable uniform and trying to remember how to work the register."
    "Most of the customers are there for the novelty of it being a maid cafe."
    "And there's far less of the leering and ogling than I'd expected."
    "I mean, what was I thinking - that this place would be like a strip-joint or something?"
    "Sure, [bree.name] looks achingly cute in her uniform, but it's far from being hardcore!"
    "In fact, I soon get used to the smiles and giggles of the female customers."
    "And I even start to feel like I could enjoy the shy kind of attention my own uniform is attracting."
    show kiara at center, zoomAt(1.0, (940, 720)) with dissolve
    "But the attention that Kiara's giving me is another thing entirely..."
    "I keep noticing her out of the corner of my eye, watching me as I work."
    "At first I try to convince myself that she's just wanting to make sure I do a good job."
    "But when I have to bend over to reach something, my already tight pants become tighter still."
    "Kiara has a perfect view of my ass."
    "And I hear her make what can only be described as an appreciative sound!"
    "I try my best to keep out of her way for the rest of the shift."
    "But when [bree.name]'s tied up waiting tables and I'm behind the counter, she makes her move."
    show kiara talkative at center, traveling(1.25, 0.5, (640, 880))
    show fx question
    kiara.say "[hero.name]?"
    show kiara normal
    mike.say "Um...yeah, Kiara..."
    mike.say "I mean, yes, boss?"
    show kiara smile
    "Kiara smiles at my faltering words, shaking her head a little."
    show kiara talkative
    kiara.say "I was just thinking about what I said earlier."
    kiara.say "About how I could repay you for helping us out."
    show kiara normal at center, traveling(1.5, 0.5, (640, 1040))
    "Well, this is awkward!"
    "I'm just about to mumble something about cash in hand being fine."
    show kiara normal at center, traveling(1.5, 0.3, (640, 1280))
    "But then I see Kiara kneeling down behind the counter - right in front of me!"
    show kiara talkative
    kiara.say "I think you deserve the manager's special!"
    show kiara delicious
    "And with that, she reaches for my flies..."
    menu:
        "I can't accept":
            "What in the hell does she think she's doing?!?"
            "There are customers just a couple of feet away."
            "And there's [bree.name], scurrying between the tables with their orders too!"
            mike.say "What are you doing?"
            "I try to keep my voice down."
            "Which means my words come out as a desperate hiss."
            show kiara stuned
            "Kiara looks up at me, a puzzled expression on her face."
            show fx question
            show kiara tantrum
            kiara.say "What does it look like, darling?"
            kiara.say "I'm going to suck your cock!"
            show kiara normal
            "She says it in such a matter-of-fact way."
            "So much so that I almost forget I have a say in the matter."
            mike.say "Well...well you can't!"
            mike.say "Not here - what if someone sees you?!?"
            show kiara uninterested at center, traveling(1.5, 0.5, (640, 1040))
            "Kiara lets out a derisive snort and rolls her eyes."
            "But she gets to her feet all the same."
            show kiara angry
            kiara.say "Okay, [hero.name], whatever you say."
            show fx anger
            kiara.say "You sure know how to kill the mood!"
            show kiara upset at center, traveling(1.25, 0.5, (940, 880))
            "She walks away, arms crossed and shaking her head."
        "Special you say?":
            $ game.flags.kiara_bj = True
            "I know that I should tell her to stop, that this is probably a bad idea."
            "But there are customers just a couple of feet away."
            "And there's [bree.name], scurrying between the tables with their orders too!"
            "If I make a fuss, they're bound to hear it and see what's going on."
            "So I just take a deep breath and let her keep doing what she's doing."
            show kiara delicious
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
            "And what she's doing, in such a public place?"
            "The element of danger's more than enough to make my cock as stiff as a board."
            show kiara maidcafe blowjob lick big
            "Kiara starts by kissing the head of my dick."
            "She goes slowly, looking up at me the whole time."
            play sexsfx1 bj_sucking loop
            show kiara maidcafe blowjob blow up handjob -medium
            "And then she begins to take it into her mouth an inch at a time."
            "She's good, but the fear of being discovered makes it so much more intense."
            show kiara maidcafe blowjob up
            "Every moment that she has my cock in her mouth, I want to gasp and cry out."
            "But I have to bite down on the urge for fear of giving the game away."
            show kiara maidcafe blowjob down
            "By the time Kiara has the length of my cock inside of her mouth, I'm almost holding my breath."
            "More than once I think a customer is going to come to the counter."
            "And when it looks like [bree.name]'s going to ask me something, I'm sure the game is up."
            "But she breezes past with nothing more than a wave and a happy smile."
            show kiara maidcafe blowjob inmouth surprise squirt with hpunch
            play sexsfx1 cum_inside
            with hpunch
            "Maybe it's the sense of relief that makes me cum a second later."
            with hpunch
            "Whatever the reason, Kiara takes it in her stride."
            with hpunch
            "She hardly flinches as I shoot my load into her mouth."
            "I watch as she stands up casually, stuffing my cock back into my pants."
            if renpy.has_label("kiara_achievement_0") and not game.flags.cheat:
                call kiara_achievement_0 from _call_kiara_achievement_0
            scene bg maidcafe
            stop sexsfx1
            show kiara blush at right
            show bree maid at left with easeinleft
            show fx question at left
            bree.say "Hey, boss - what's that you're eating there?"
            "Kiara looks [bree.name] straight in the eye as she asks the question."
            "She swallows my cum without a hint of guilt or concern."
            show kiara talkative
            kiara.say "Oh, sorry, [bree.name]."
            kiara.say "I was just stealing one of your treats!"
            show kiara normal
            "[bree.name] waves away her concern as if it's nothing."
            show bree happy at left
            bree.say "Don't worry about it."
            bree.say "If you mean the candy bar that was in my bag, it's okay."
            bree.say "I could do with cutting down anyway!"
            hide bree
    hide kiara
    with fade
    "Luckily for me, the rest of the shift passes without incident."
    "Kiara disappears into the back of the cafe and I don't see her again."
    show bree maid with fade
    "I help [bree.name] to close the place up, trying to keep my mind off her boss's antics."
    show bree smile
    bree.say "Thanks again for helping me out, [hero.name]."
    bree.say "You really made my shift so much easier."
    show bree normal
    mike.say "Ah...yeah, [bree.name]."
    mike.say "It was no problem, really!"
    show bree smile
    bree.say "Kiara was saying how much she liked having you too."
    show bree normal
    mike.say "She said WHAT?!?"
    show bree smile
    bree.say "That she thought you did well learning the ropes."
    show bree evil
    "[bree.name] leans in and whispers to me in a conspiratorial manner."
    bree.say "Between you and me, I think she'd like to have you here permanently."
    bree.say "She's got SUCH a crush on you, [hero.name]!"
    show bree normal
    mike.say "Really?!?"
    "[bree.name] nods, totally missing just how much she's making me sweat."
    "I try to change the subject as we lock the cafe up for the night."
    "All the time hoping that she doesn't guess just how right she really is!"
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    $ game.pass_time(4)
    $ game.room = "street"
    hide bree
    return

label bree_event_13b:
    if bree.love.max < 190:
        $ bree.love.max = 190
    scene bg livingroom
    show bree
    "Things have been going pretty well between [bree.name] and myself since we managed to actually talk about our feelings for each other."
    "Just getting it all out into the open and realising that we both fell the same way seems to have lifted a weight off of my mind."
    "And with that gone, there's really nothing to stop us from just having fun and enjoying the chance to be together."
    "It all seems to be going that way too, no problems on the horizon to ruin things either."
    "That is until [bree.name] sits me down and tells me that she wants to talk."
    "I know, I know - it's one of the oldest cliches in the book."
    "The girl tells the guy that she wants to talk, that's all - just to talk."
    "Then the guy goes away and builds it up into something that it's not."
    "And before too long, he's convinced himself that she's going to dump him."
    "But don't just accuse me of being that guy."
    "Because the opposite can as easily be the truth."
    "The guy can convince himself that nothing's wrong in the slightest, and then get a nasty surprise."
    "I guess it's lucky for me that I don't get that chance to think about it."
    "And that's because [bree.name] insists that we sit down and talk straight away."
    "Well, I say that we'll talk."
    "I think we all know this is mainly going to be her talking and me listening!"
    show bree smile
    bree.say "[hero.name], I think it's important that we be honest with each other."
    show bree evil
    bree.say "Especially as our relationship has some...unusual qualities to it!"
    show bree flirt
    if bree.is_collared:
        "I notice that [bree.name] can't help fingering the collar around her neck as she says this."
    "She smiles, flushing a little at the reality of it all."
    "I nod, trying to show her that I understand her concerns."
    "After all, not everyone appreciates the more subtle qualities of what we have going on between us."
    mike.say "Okay, [bree.name]."
    mike.say "I get what you're saying."
    show bree smile
    bree.say "Good...good..."
    bree.say "That's good."
    bree.say "That's good because..."
    show bree normal
    "Here it comes."
    "Here comes the part where she plunges her hand into my chest and pulls out my still beating heart!"
    show bree smile
    bree.say "Because my Dad's coming to visit in a couple of days time."
    show bree normal
    "I'm so surprised to hear that, so relieved, that I can't help gasping in relief."
    "Unfortunately, [bree.name] seems to misinterpret this as a groan of annoyance on my part."
    show bree talkative
    bree.say "Yeah, I know it's a pain in the ass."
    bree.say "But at least you're getting it out of the way early, right?"
    bree.say "No need to worry about what he thinks of you if you meet him sooner, rather than later."
    show bree normal
    "I force a smile onto my face."
    "Realising I was worrying about the wrong thing entirely puts me on the backfoot."
    "But dealing with [bree.name]'s dad seems preferable to being told she regrets getting involved with me."
    "Don't get me wrong - it still sucks, just slightly less."
    mike.say "Yeah, I guess you're right, [bree.name]."
    mike.say "I have to meet him sooner or later."
    mike.say "Who knows, he might take an instant liking to me!"
    mike.say "Maybe he'll even see me as potential son-in-law material!"
    show bree dazed
    "[bree.name] tries as best she can to keep her reaction to this off of her face."
    "But her eyes still go wide at what I thought was just an off-hand remark."
    show bree surprised
    show fx drop
    bree.say "Ah, maybe you should just keep off that whole topic?"
    bree.say "Just to be safe, yeah?"
    show bree sadsmile
    "I raise a quizzical eyebrow at this."
    mike.say "Erm, [bree.name]..."
    mike.say "Is there something I should know about your dad?"
    mike.say "Because it sure sounds like there is!"
    show bree blank
    "[bree.name] looks me in the eye for a moment, and I honestly think she's going to deny it."
    "But then she blinks a couple of times and shakes her head in defeat."
    show bree smile
    bree.say "Okay, okay..."
    bree.say "My Dad's not a psycho or anything, right?"
    show bree normal
    "Of course not, because that's the first thing you bring up when someone's perfectly sane!"
    mike.say "Okay...but?"
    show bree talkative
    bree.say "He's a bit old-fashioned, yeah?"
    bree.say "He still likes to think of me as his little girl."
    show bree normal
    "Ah, he's one of THOSE guys!"
    "I can picture him already - all protruding veins and suppressed resentment..."
    if bree.is_collared:
        show bree talkative
        bree.say "And it'll be hard enough to sell this to him..."
        show bree normal
        "I see [bree.name] fingering the collar again."
        "And I can't say I don't get where she's coming from."
    mike.say "Sure thing, [bree.name]."
    mike.say "I understand."
    show bree smile
    "[bree.name] smiles, trying to look reassured by my agreement."
    if bree.is_collared:
        bree.say "It's not just the collar though, or anything to do with you specifically."
    bree.say "My Dad's always been critical of my choice in boyfriends."
    show bree normal
    mike.say "That's how dads are supposed to be, [bree.name]."
    mike.say "I'm sure he was just looking out for you, that's all."
    show bree blank
    "[bree.name] fixes me with an unexpectedly serious glare."
    show bree talkative
    show fx question
    bree.say "Oh, you think so, do you?"
    bree.say "Is that what you think?"
    show fx drop
    bree.say "[hero.name], this is the guy who once CHOSE a boyfriend for me to date!"
    show bree blank
    "Now it's my turn to look at [bree.name] with wide eyes."
    mike.say "No..."
    mike.say "You're bullshitting me!"
    show bree talkative
    bree.say "Nope - he and my Mom vetted the candidates and fixed me up with the winning guy."
    bree.say "I was over the moon at the time."
    show bree vangry
    show fx anger
    bree.say "But now just thinking about it makes me feel like a prize hog put up for auction!"
    show bree angry
    "[bree.name]'s tone is getting ever more angry as she recounts the memory."
    "It's hard to believe that she was the one being so calm and reasonable a moment ago!"
    mike.say "But he was a nice guy, right?"
    mike.say "I mean, your folks wouldn't hook you up with a loser, would they?"
    show bree talkative
    bree.say "Let's just say that my Dad's idea of a loser isn't the same as mine."
    bree.say "And let's just say the whole experience left it's mark on me..."
    show bree sadsmile
    "[bree.name] leaves it at that, not saying what kind of mark she means."
    "And the fact that she doesn't makes me think I shouldn't ask either."
    mike.say "Don't worry about it, [bree.name]."
    mike.say "That's all in the past now."
    "[bree.name] seems to snap out of it then."
    "She shakes her head and makes an effort to smile."
    show bree smile
    bree.say "You're right, [hero.name]."
    bree.say "This is a chance to show my Dad that I'm all grown up now."
    bree.say "I can finally let him know that he doesn't need to look after me anymore."
    show bree normal
    "I nod, trying as best I can to offer all the support that [bree.name] needs."
    "But inside, I'm already beginning to imagine the potential disaster that lies ahead of us..."
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    return

label bree_event_14b:
    if bree.love.max < 200:
        $ bree.love.max = 200
    scene bg livingroom
    show bree casual
    "It's the day of the visit from [bree.name]'s dad, and I'm a mess of mixed emotions."
    "And after what she already told me about the guy, I'm curious to see if she was exaggerating or not."
    "I'm nervous, not least because of the usual pressure of meeting a girlfriend's dad."
    "You always assume they're going to be suspicious of you."
    "But the intense picture that [bree.name] painted of the guy is all I have to go on."
    "Even more so, it's practically the only information I have on her life before we became housemates."
    "Whereas I feel like I'm always telling her and Sasha stories about my life back home."
    "And I'm feeling a weird kind of excitement to finally be getting an insight into [bree.name]'s past."
    show bree talkative
    bree.say "Okay, [hero.name] - here he comes."
    bree.say "Do I have your permission to talk to him?"
    show bree normal
    mike.say "Yes, [bree.name]."
    mike.say "You have permission, to speak freely."
    mike.say "But just so long as he's here."
    show bree talkative
    bree.say "Yes, [hero.name]."
    bree.say "Please remember all that I told you about him too."
    scene bg house
    show bree casual
    "I'm still wondering if he can be all that bad in reality."
    "But I see the need to reassure [bree.name], and so I smile and nod."
    "[bree.name] returns both the smile and the nod, then takes a deep breath as she opens the door."
    show breedad at left
    "We're presented with a stocky-looking guy that's well into his middle years."
    "His face is lined with creases and his head is shaved bald."
    "But his expression is surly and his eyes are intense too."
    "He strikes me instantly as a no-nonsense kind of guy."
    "You know the kind - beer and football, the younger generation are all pussies, and so on..."
    "I can't see anything of him in [bree.name], no matter how hard I try."
    "Which I guess means that her mom must have been quite something in her youth!"
    show bree happy
    show fx exclamation
    bree.say "Daddy!"
    bree.say "You made it!"
    show bree normal
    "[bree.name]'s greeting is warm and sweet as can be, but it does nothing to change his expression."
    if bree.is_collared:
        "He makes a grunting noise, his eyes fixing on the collar that [bree.name] wears around her neck."
    else:
        "He makes a grunting noise."
    "And from there, he looks up, glaring at me!"
    breesdad "Yeah, yeah, yeah..."
    show fx anger at left
    breesdad "You're actually living in this dump?"
    breesdad "I always said renting's for chumps."
    show fx anger at left
    breesdad "It's like throwing money down the drain!"
    "[bree.name] laughs at what her dad just said, trying to make a joke out of it all."
    "But I can already feel the tension in her voice as she does so."
    show bree smile
    bree.say "Oh, Daddy - you and your funny old sayings!"
    show bree normal
    breesdad "Yeah, I'm a regular barrel of laughs."
    show fx anger at left
    breesdad "Maybe that's why you hooked up with a joker like this guy!"
    "He nods his head at me as he says this, as if the point needed to be underlined."
    show bree smile
    bree.say "Oh, sure, Daddy."
    bree.say "[hero.name] here is the best!"
    show bree normal
    breesdad "Is he now..."
    if bree.is_collared:
        show fx question at left
        breesdad "That why he needs to put a collar on you?"
        breesdad "He's trying to keep you from running off with someone better?"
        show bree smile
        bree.say "[hero.name]'s not like that, Daddy!"
        bree.say "We just have a very unique kind of relationship, that's all."
        bree.say "I love him so much that I want to show it."
        bree.say "And so I wear this collar to do just that."
        show bree normal
        show fx question at left
        breesdad "Is that what it does?"
    "He rolls his eyes as he almost barges past her towards the open door."
    "I don't know what to do, other than hold out my hand to him."
    "But all he does is look at it like it was a pile of steaming turds."
    "And then he literally shoulders me out of the way and walks straight into the house."
    "I look at [bree.name] with wide eyes, the annoyance I'm feeling plain to see."
    "But she just looks at me with a painful smile and a helpless look in her eyes."
    "What comes next is an awkward tour of the house."
    "In every room [bree.name] makes an effort and her dad pisses on it."
    scene bg livingroom
    show bree casual at right
    show breedad at left
    "When it's finally over, we end up in the living room for a coffee."
    show fx question at right
    bree.say "Well, Daddy - what do you think?"
    breesdad "What do I think?!?"
    show fx anger at left
    breesdad "I think this set up's worse than when I was stuck in that tower with those damn terrorists that Christmas!"
    breesdad "You should have stuck with that guy I found for you!"
    show fx anger at left
    breesdad "Sure, he knocked you about a bit."
    if not bree.is_visibly_pregnant:
        breesdad "But he'd have knocked you up by now too!"
    "I can see the impact of the comment on [bree.name]."
    "It hits her almost like a physical blow, as if her dad had slapped her across the face."
    show bree cry at right
    "She looks down at her lap, and I already know tears are forming in the corner of her eyes."
    mike.say "[bree.name], would you come over here?"
    "My tone is authoritative, letting her know that I expect obedience."
    show bree gloomy at right
    "But it's still warm enough to be a stark contrast to the one her dad just used."
    "Still sniffling a little, [bree.name] stands up and hurries to obey."
    show bree sad
    bree.say "Y...yes, [hero.name]."
    bree.say "Right away, [hero.name]!"
    show bree sadsmile
    "[bree.name]'s dad narrows his eyes at me, shaking his head."
    show fx anger at left
    if bree.is_sex_slave or bree.flags.mikeNickname in nickname_daddy:
        breesdad "You call him that all the time?"
        breesdad "Jesus Christ - what kind of a sick fuck is this guy?!?"
        "I ignore him totally, instead focussing on [bree.name] alone."
    mike.say "[bree.name], I need to talk to your father, man-to-man."
    mike.say "We're going to be talking about you, but not to you."
    mike.say "So I want you to take my cock out of my pants and suck it while we do."
    show bree surprised at right
    "[bree.name]'s eyes go wide at this."
    "And for a moment I actually think she's going to refuse."
    "Her dad almost chokes on his coffee."
    show fx anger at left with vpunch
    breesdad "WHAT THE HELL?!?"
    show fx anger at left
    breesdad "You'll do no such thing!"
    "But [bree.name]'s already down on her knees in front of me, opening my flies."
    scene bree dad bj with fade
    "I hold her dad's eye as she pulls out my cock, not looking away for an instant."
    "Look, I know that he could snap at any moment."
    "I know he could probably kill me with his bare hands."
    "But I'm guessing this guy is basically a bully."
    "And the best way I know to deal with bullies is to call their bluff."
    show breedad fx surprise
    breesdad "[bree.name], stop that - right now!!!"
    "I shake my head at him as I feel [bree.name] handling my cock."
    show bree dad bj medium lick
    "It's getting harder by the second."
    "But I don't know if it's more from the thrill or the fear of the situation!"
    show bree dad bj blow
    "I open my own mouth at the same moment [bree.name] puts my cock in her own."
    mike.say "I'm guessing that normally works with most people?"
    mike.say "You know, the routine where you shout and bawl?"
    show breedad fx exclamation
    breesdad "It's not any kind of routine, asshole!"
    breesdad "I was a cop for twenty years."
    breesdad "And I know a bullshit punk when I see one too!"
    "I doubt he'd lie about something like that."
    "Shit - I wonder if he still carries a gun?!?"
    "But I'm committed now, and I can't back down."
    "I stroke [bree.name]'s hair as her head starts to bob up and down in my lap."
    show bree dad bj closed
    mike.say "I get that, really I do."
    mike.say "But you have to understand that the power I have over [bree.name] here is entirely different."
    mike.say "You see she used to obey you because she was afraid of you."
    mike.say "Whereas with me, she does as I say because she loves me."
    show breedad fx surprise
    breesdad "Oh yeah?"
    breesdad "Looks more like she's your bitch to me!"
    mike.say "If that's a word you're more comfortable with, then sure."
    mike.say "But those are your words, not mine."
    "Am I imagining it - or is [bree.name] getting more into it as I'm speaking?"
    show bree dad bj saliva
    "Because with every word that I say about my feelings for her, she seems to redouble her efforts!"
    mike.say "You see, I don't feel the need to put [bree.name] down like you do."
    mike.say "I respect her as much as I love her, and she knows that."
    if bree.is_collared:
        mike.say "All of which means she can wear that collar without fear."
    "[bree.name]'s giving it everything she's got right now, working me like a machine."
    "For all of my big talking, I'm still worried that this is going to blow up in my face."
    "I feel like I'm walking a tight-rope, like I could fall to my death at any moment."
    "Fuck - what am I going to do when I actually cum?!?"
    show bree dad bj angry
    show breedad fx aura behind angry
    breesdad "I know what this is, buddy boy."
    breesdad "You've got her brainwashed!"
    show breedad fx exclamation
    breesdad "She's still my little girl, dammit!"
    mike.say "Doesn't look that way to me."
    mike.say "After all, I'm the one getting my cock sucked right now!"
    "That seems to be the final straw, and he shoots up out of his seat."
    "His coffee flies across the room and I honestly think he's about to attack me."
    "But then he storms straight out of the room without looking back once."
    show bree dad bj nodad up
    "I hear the front door slam, and only then do I finally let go."
    mike.say "Yippie Ki Yay, [bree.name]'s Motherfucker!"
    show bree dad bj inmouth blush with hpunch
    "And with that, I shoot my load down [bree.name]'s throat."
    with hpunch
    "She gags a little, but recovers like a pro."
    with hpunch
    "Then she gulps down, as if she's loath to waste even a single drop."
    show bree dad bj smile big ondick -inmouth
    bree.say "Oh, [hero.name]..."
    "I hold up a hand to silence [bree.name]."
    scene bg livingroom
    show bree casual
    "And she stops in the middle of wiping the cum off of her lips."
    mike.say "Your permission to speak expired when that prick left the house."
    mike.say "But you're probably too mixed-up to have remembered that."
    "[bree.name] nods eagerly, keen to make up for her error."
    mike.say "You can speak."
    show bree happy
    bree.say "Thank you, [hero.name]."
    show bree smile
    bree.say "Thank you for standing up for me."
    bree.say "But I'm worried about what he might do..."
    show bree normal
    mike.say "Don't worry, [bree.name]."
    mike.say "He wouldn't stop you sucking my cock right in front of him."
    mike.say "You really think he's going to go and tell his cop buddies all about that?"
    show bree talkative
    show fx drop
    bree.say "I...I suppose not, [hero.name]."
    show bree normal
    "I nod just to underline the point."
    "And then I nod at my semi-erect cock."
    mike.say "Now how about you clean me up?"
    "[bree.name] nods, beginning to smile as she gets on with licking me clean."
    "Best to keep her occupied, rather than letting her dwell on the matter..."
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    return

label bree_event_14c:
    scene bg beach
    "What could be more normal and everyday than a guy and his girlfriend heading out to the beach?"
    "And that's exactly what [bree.name] and I are doing right now."
    "We're just an average couple, strolling along the sand and looking for a spot to sit down."
    show bree
    if bree.is_collared:
        show bree leash
        "Well, apart from the fact that [bree.name] has her collar and leash on as we do so!"
        "Look, I'd be lying if I said that I didn't expect to be getting as much attention as we are right now."
        "It doesn't matter how modern and enlightened people in this city are supposed to be."
        "A sight like that is still going to get heads turning and people talking!"
        "But it's not like either of us actually cares about it."
        "I'm enjoying the feeling of the eyes upon us, and I can see that [bree.name] is too."
        "She's really started to get into the swing of this thing recently."
        "And I also know that the situation's probably getting her more than a little hot under the collar as well!"
        "Both of us are more than able to play it cool as we spread our towels on the sand and settle down."
        "After all, making the whole thing look casual and easy is another part of the thrill."
        "If I weren't holding onto [bree.name]'s leash and commanding her to sit, then we'd look like anyone else here today."
        "But even with that being said, I still want to be sure [bree.name]'s okay."
        "So as we settle down and she presses herself against me, I make a point of asking her as much."
    mike.say "How are you doing, [bree.name]?"
    mike.say "Are you feeling okay today?"
    "[bree.name] looks at me with a slightly puzzled expression on her face."
    "She almost seems to think that what I just said is some kind of test."
    show bree happy
    bree.say "Yes, [hero.name]."
    show bree smile
    bree.say "Of course I am."
    bree.say "I couldn't be happier than I am to be with you right now!"
    show bree normal
    "I nod, satisfied with the sincerity of her answer."
    mike.say "It's very good that you're so obedient and attentive, [bree.name]."
    mike.say "But you have to remember that my happiness depends on yours too."
    mike.say "I can only enjoy your being my pet if you're enjoying it too, you know?"
    show bree blank
    "[bree.name]'s expression becomes suddenly serious, almost a caricature of itself."
    "I can't help smiling at the weight that she attaches to my words."
    show bree talkative
    bree.say "Yes, [hero.name]."
    bree.say "I understand."
    bree.say "But..."
    show bree blank
    "[bree.name] hesitates, the words dying in her throat."
    "I can sense that she desperately wants to say something to me."
    "And so I nod again, letting her know that it's okay for her to speak."
    mike.say "Go on, [bree.name]."
    mike.say "Say what you want to say."
    show bree hesitating
    bree.say "I..."
    bree.say "I just wanted to say that I've been so happy recently, so fulfilled."
    bree.say "Ever since we started to..."
    show bree normal
    if bree.is_collared:
        "I see her hand stray unconsciously to the collar around her neck."
    "And I know that she's talking about the submissive role she's taken on in our relationship."
    mike.say "Me too, [bree.name]."
    mike.say "I feel it's made us closer than ever."
    mike.say "That it's bonded us even."
    "[bree.name] nods at this, almost frantically."
    "It's as if she wants to agree, yet feels the need to go further still."
    show bree smile
    bree.say "That's why I wanted to make a promise to you, Master."
    bree.say "A kind of pledge, you know?"
    show bree flirt
    "I raise my eyebrows at this, intrigued by what she could mean by that."
    if bree.is_collared:
        "[bree.name]'s already let me put a collar on her and lead her around, submitting to my will."
    "What more could she possibly have to offer me after that?"
    show bree talkative blush
    if bree.flags.mikeNickname:
        bree.say "I...I want to be your slave, [hero.name]."
        bree.say "I want to be your slave - mind, body and soul!"
        bree.say "I love you, [hero.name]."
    show bree smile
    bree.say "And so I want to let you have me without reservation!"
    bree.say "From now on, I'm yours to do with as you will."
    bree.say "If you'll have me..."
    show bree normal
    "There are more than a few guys that would have jumped on that opportunity, right there and then."
    "The kind that would just take what [bree.name]'s offering me as a chance to control and exploit her."
    "But even when it turned down this path, our relationship was never about me taking advantage of [bree.name]."
    "It was all about a kink that we'd discovered together and which brought us together as a couple."
    "As much as I enjoy her being submissive to me, I genuinely love [bree.name] and only want what's best for her."
    "Of course I want what she's offering, but I can only think of accepting it because I know her so well."
    "And that means that I know she wouldn't be doing this if it weren't what she wanted too."
    mike.say "Of course I will, [bree.name]."
    mike.say "If that's what you want, then that's what'll happen."
    mike.say "You'll be my willing slave, and I'll be your master."
    show bree happy -blush
    "[bree.name]'s face becomes a picture of happiness and gratitude."
    "She practically beams at me, and I expect her to throw her arms around me at any moment."
    "But when she doesn't, it takes me a couple of seconds to realise why."
    mike.say "You can show your affection, [bree.name]."
    mike.say "In whatever form you feel appropriate."
    "At this, [bree.name] wraps her arms around my neck and presses herself against me."
    show bree kiss with fade
    $ bree.flags.kiss += 1
    "She kisses me, deeply and with a passion that takes me quite by surprise."
    "I can feel my cock stiffening more with each moment that it all lasts."
    "But I don't know if it's from the embrace of such a hot, passionate girl."
    "Or else I'm getting hard from the knowledge that she's just pledged herself to me alone."
    "All that warmth, affection and love - all of it just for me."
    "It's no wonder that I can already feel my head starting to spin at the mere thought of it!"
    hide bree
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
