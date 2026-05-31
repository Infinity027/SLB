init python:
    Event(**{
    "name": "shawn_auto_greet",
    "label": "auto_greet",
    "girl": "shawn",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(shawn,
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
    "name": "shawn_give_phone_number",
    "label": "give_phone_number",
    "girl": "shawn",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(shawn,
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
    "name": "shawn_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(shawn,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "shawn",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shawn_are_you_sick",
    "label": "are_you_sick",
    "girl": "shawn",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(shawn,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (shawn, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shawn_auto_chat",
    "label": "auto_chat",
    "girl": "shawn",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(shawn,
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
    "name": "shawn_ask_out",
    "label": "ask_out",
    "girl": "shawn",
    "priority": 100,
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(shawn,
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
    "name": "shawn_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "shawn",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(shawn,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label shawn_bye(bye_outfit=None):
    python:
        if not bye_outfit:
            bye_outfit = shawn.get_clothes()
        day = game.week_day
        bye_hour = game.hour + duration
        if bye_hour > 23:
            bye_hour = 0
            day = day + 1
            if day > 7:
                day = 1
        h, activity = shawn.get_activity(bye_hour)
    if not activity == shawn.activity:
        if day != game.week_day:
            $ shawn.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ shawn.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"shawn {bye_outfit}")
        if activity["activity"] == "sleep":
            shawn.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            shawn.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            shawn.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            shawn.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            shawn.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            shawn.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            shawn.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            shawn.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            shawn.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            shawn.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            shawn.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            shawn.say "I'll go get dressed."
        hide shawn
    return

label shawn_cheated(action, cheat_npc=None):
    show shawn
    if not shawn.sub >= 75:
        show shawn angry
        show fx anger
        $ loss = 5
        if shawn.flags.boyfriend or shawn.flags.fiance:
            $ loss += 5
        $ shawn.love -= loss
        "I see Shawn looking at me [action] someone else with a painful hurting face..."
    else:
        show fx heart
        $ shawn.sub += 1
        "I see Shawn looking at me [action] someone else with envy and lust in his eyes."
    hide shawn
    return

label shawn_beats_ryan_female:
label shawn_beats_scottie_female:
label shawn_beats_jack_female:
    if randint(1, 100) <= 20:
        return "abort"
    if active_girl.id == "ryan":
        "I can feel Ryan's lips against mine, his hands all over me."
    elif active_girl.id == "jack":
        "Jack's kissing me with a passion, squeezing me tight."
    "I know that I should be stopping him, but it's so hard to resist!"
    shawn.say "Oi!"
    shawn.say "Get your filthy hands off her!"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show shawn angry at right5
    $ renpy.show(f"{active_girl.id} angry", at_list=[left5])
    if active_girl.id == "ryan":
        "At the sound of Shawn's voice, Ryan releases me from his grip."
    elif active_girl.id == "jack":
        "At the sound of Shawn's voice, Jack leaps away from me."
    "I gasp and look around to see him standing there, visibly seething."
    bree.say "Shawn, I..."
    bree.say "I can explain..."
    "Shawn holds up a hand, cutting me off."
    shawn.say "No need to explain, [hero.name]."
    if active_girl.id == "ryan":
        shawn.say "This is between me and Mister Slimy!"
    elif active_girl.id == "jack":
        shawn.say "This is between me and fatty!"
    "I can't help gasping in surprise at Shawn."
    "He looks steely, determined and downright manly right now!"
    "Call me shallow, but he's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "Wait a minute..."
        ryan.say "Aren't you the little prick from the electronics store?!?"
    elif active_girl.id == "jack":
        jack.say "Hey, that's not nice!"
        jack.say "I've been working out - so if I put on weight, it's muscle-mass!"
    "Before another word can be spoken, Shawn barrels into him."
    "And with that, the fight is on!"
    "Well, I say fight..."
    "Neither of them seems to be particularly good at it."
    "There's a lot of flailing and what looks like slapping."
    "Not many punches or kicks though."
    "But the decisive moment comes when Shawn sees an opening."
    $ renpy.hide(f"{active_girl.id}")
    hide shawn
    $ renpy.show(f"shawn beats {active_girl.id}")
    with hpunch
    shawn.say "Stitch this, arsehole!"
    "[active_girl.name] cries out in pain as Shawn gouges his eyes."
    "That really shouldn't be the end of it."
    "But the eye-poking really seems to have taken the fight out of [active_girl.name]."
    "He stumbles away, half-blinded as Shawn misses him with another kick."
    shawn.say "Ah, running away!"
    shawn.say "Tired of me kicking your arse?!?"
    return


label shawn_greet:
    if renpy.has_label(f"shawn_greet_dialogues_{hero.gender}") and not shawn.flags.greeted:
        scene expression f"bg {game.room}"
        $ shawn.flags.greeted = TemporaryFlag(True, 1)
        show shawn
        $ result = randint(1, 3)
        if result == 1:
            shawn.say "Hello, [hero.name]."
        elif result == 2:
            shawn.say "Hi, [hero.name]."
        elif result == 3:
            shawn.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                shawn.say "Good morning [hero.name]."
            elif game.hour < 19:
                shawn.say "Good afternoon [hero.name]."
            else:
                shawn.say "Good evening [hero.name]."
        call expression f"shawn_greet_dialogues_{hero.gender}" from _call_expression_463
        hide shawn
    return


label shawn_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Shawn."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Shawn."
        elif game.hour < 12:
            bree.say "Good morning Shawn."
        elif game.hour < 19:
            bree.say "Good afternoon Shawn."
        else:
            bree.say "Good evening Shawn."
    return

label shawn_kiss_female:
    scene expression f"bg {game.room}"
    if shawn.love < 25 and not shawn.is_boyfriend and not game.active_date.score >= 75:
        show shawn
        "I really want to plant a kiss on Shawn's lips."
        "I feel like I've been waiting forever to do it."
        "Like the right moment is never going to come!"
        "So I decide that I have to take the bull by the horns."
        "I just throw caution to the wind and lean in towards Shawn."
        "Closing my eyes, I purse my lips and hope he gets the message..."
        "And then I almost tumble forwards, my eyes popping open again!"
        "The first thing I see when I regain my balance is Shawn backing off."
        "And he looks less than impressed at my efforts to kiss him."
        "All I can do is put on a weak grin and try to play it off as nothing."
        "But the whole time I can feel my guts churning with embarrassment."
        "And I have no idea how I'm going to explain myself to him either."
        hide shawn
        $ shawn.love -= 1
    elif not shawn.flags.kiss:
        show shawn
        "I kinda want to plant a kiss on Shawn's lips."
        "Actually, I want to kiss the guy pretty badly!"
        "But I know how nerdy guys like him can be."
        "I don't want to make a move and end up scaring him off."
        "But when the perfect chance seems to present itself, I have to make a choice."
        "And I decide that it's better to take a leap into the unknown and consequences be damned!"
        show shawn kiss with fade
        "I lean in and plant my lips firmly on his, closing my eyes at the same time and hoping."
        "At first I feel Shawn stiffen with surprise, and I think he's going to pull away."
        "But then Shawn seems to realise what's happening, and he relaxes all at once."
        "And within mere seconds he's leaning into the kiss, returning it with enthusiasm."
        "I can feel my heart begin to race ever faster as the kiss goes on."
        "Like I'm communicating with Shawn on whole different level."
        "And now that it's started, neither of us seems to want it to end!"
        hide shawn kiss with fade
        $ shawn.flags.kiss += 1
        $ shawn.love += 5
    else:
        show shawn kiss with fade
        "I'd like to say that things get more relaxed between Shawn and myself now that we've shared a kiss."
        "But the truth is that it's still a little awkward, and we're both still a little shy."
        "We keep on taking the chance to steal a kiss here and there, whenever we can."
        "And things are getting more intimate and natural, a little at a time."
        "Don't get me wrong - the kisses are amazing, well worth the effort!"
        "But I guess I just have to accept that Shawn's not exactly flaming with passion!"
        "I'm not worried though, not in the slightest."
        "Because I'm sure that I can stoke the fire inside of him."
        "And once I get that fire roaring, there's going to be no holding us back!"
        hide shawn kiss with fade
        $ shawn.flags.kiss += 1
        $ shawn.love += 5
    return





label shawn_ask_date_female:



    call shawn_ask_date_alone_female from _call_shawn_ask_date_alone_female
    return _return

label shawn_ask_date_alone_female:
    if not shawn.flags.hadadate:
        bree.say "I really like hanging out with you, Shawn."
        shawn.say "Me too, [hero.name] - you're a lot of fun."
        bree.say "But...and I hate to say this..."
        bree.say "I kinda feel like [mike.name]'s cramping our style, you know?"
        bree.say "Like he's a third wheel, yeah?"
        shawn.say "You do?"
        bree.say "Yeah, Shawn."
        bree.say "So I was thinking..."
        bree.say "How about we meet up, just the two of us?"
        shawn.say "[hero.name], are you asking me out?"
        shawn.say "Like on a date?!?"
        bree.say "Erm...yeah, Shawn, that's about the size of it!"
    else:
        bree.say "You want to hang out?"
    if shawn.love < 50 or shawn.flags.nodate:
        shawn.say "It's a tempting offer, [hero.name]."
        if not shawn.flags.hadadate:
            shawn.say "But I'd kind of feel like I was going behind [mike.name]'s back."
            shawn.say "So I'm going to have to pass."
        else:
            shawn.say "But no, thanks."
        $ date_choice = False
    else:
        shawn.say "You bet I do, [hero.name]!"
        shawn.say "When can we do it?"
        shawn.say "I'm free like...well, whenever!"
        $ shawn.flags.hadadate = True
        $ date_choice = True
    return date_choice

label shawn_pregnancy_congratulations:
    if game.week_day % 2 == 0:
        show shawn surprised
        "I see Shawn coming towards me at speed."
        "Well, he's rushing over if I'm going to be honest."
        "And he looks like he's got a look of concern on his face."
        shawn.say "[hero.name]!"
        shawn.say "What happened to you?"
        "I look down at my swollen belly."
        "And then back up at Shawn."
        bree.say "Erm..."
        bree.say "What does it look like, Shawn?"
        bree.say "I'm pregnant!"
        show shawn annoyed
        "Shawn looks exasperated and shakes his head."
        show shawn sad
        shawn.say "I know that, [hero.name]!"
        shawn.say "But how did it happen?!?"
        bree.say "Well Shawn, when a man and a woman love each other very much..."
        show shawn blush
        "Shawn's cheeks turn a shade of red."
        show shawn -sad
        "And he seems to finally realise he's making a mistake."
        shawn.say "Okay, [hero.name], okay..."
        show shawn happy
        shawn.say "What I mean to say was - congratulations!"
        shawn.say "You're pregnant, and that's great news!"
    else:
        show shawn annoyed
        "Shawn's doing that thing where he tries to look at me while not looking like he's looking at me."
        show shawn embarrassed
        "Which is the one sure-fire way to make it totally obvious that you're trying to look at someone."
        show shawn annoyed
        "And knowing Shawn as well as I do, it's clear that I'm going to have to call him on it."
        show shawn embarrassed
        "Because there's no way he'll be the one to pluck up the courage to mention the elephant in the room."
        show shawn annoyed
        "Or in this case, the baby in the womb."
        bree.say "Yeah, Shawn..."
        bree.say "I am."
        show shawn surprised
        "Shawn's eyes almost pop out of his head as he takes this in."
        shawn.say "You are?!?"
        shawn.say "I...I mean..."
        show shawn embarrassed
        shawn.say "You are what, [hero.name]?"
        shawn.say "I have no idea what you mean by that!"
        "I smile and pretend to play along."
        bree.say "Just that I'm pregnant, Shawn."
        show shawn happy
        shawn.say "Oh, I see now!"
        shawn.say "Well that's great news."
        shawn.say "Congratulations, [hero.name]!"
    $ shawn.love += 1
    return

label shawn_propose_female:
    show shawn
    "I've been racking my brain for what feels like forever."
    "Trying to figure out the best way to propose to Shawn."
    "But every idea that I come up with seems great at first."
    "Then as soon as I give it a second thought, I find myself cringing inside."
    "It's just so hard to come up with a winning idea for someone that's so..."
    "Well, so sarcastic and more than a little weird!"
    "Seriously, Shawn reminds me of those typically British guys you see in comedy shows."
    "He's totally nerdy and hopeless in social situations for sure."
    "But he's also got that dry wit that guys from the UK seem to have too."
    "So once you've tuned into him, he's always making you laugh."
    "And I guess that's the reason why I'm wanting to propose to him."
    "I met him through [mike.name], when we all hung out together in a group."
    "But one by one, everyone else started dropping away."
    "Until eventually it was just Shawn and myself."
    "Even [mike.name] seemed to read where things were going and backed off."
    "Though I still had to be the one to suggest to Shawn that we start dating!"
    "I'd like to say that it's been plain sailing since then."
    "That it's been all wine and roses."
    "But the truth is that Shawn's too quirky for that to be the case."
    "Though it's the quirks that really make him special."
    "So I guess that I have to accept those."
    "Especially if I want things to work out for us."
    "In the end, the only solution I can think of is the most simple of all."
    show shawn at center, zoomAt(1.5, (640, 1040))
    "I just choose what feels like the right moment, and then I ask the question."
    bree.say "Shawn..."
    bree.say "There's something I wanted to ask you..."
    show shawn surprised
    shawn.say "Oh..."
    show shawn nice
    shawn.say "Okay, [hero.name]..."
    shawn.say "Go ahead, I'm all ears!"
    show shawn normal
    "I nod, trying as best I can to keep calm."
    "But I can already feel the anxiety building up inside of me."
    bree.say "It's something pretty serious, okay?"
    bree.say "So whatever you do, don't panic!"
    show shawn embarrassed
    "Shawn responds to this in typical fashion by pulling a funny face."
    "One that looks like a comical grimace of fear."
    shawn.say "Oooh!"
    show shawn smug
    shawn.say "That sounds ominous, [hero.name]..."
    shawn.say "You're scaring me already!"
    show shawn normal
    "I do the best I can to ignore Shawn's efforts to turn everything into a joke."
    "Another one of those little quirks that make him seem so British."
    "And instead of rising to the bait, I push ahead."
    bree.say "Shawn..."
    bree.say "Ever since we started dating, I feel like we've gotten closer and closer."
    bree.say "And now I think it's time for us to take things to the next level."
    bree.say "So I'm asking you..."
    bree.say "I'm asking you - will you marry me?"
    if sasha.love < 195:

        show shawn surprised
        "As soon as he hears and understands what I just said, Shawn's entire demeanour changes."
        "Where before he was listening with interest, now he looks positively alarmed!"
        show shawn smug
        shawn.say "You're joking, right?"
        shawn.say "You're pulling my leg, yeah?"
        "Shawn has a panicked smile on his face as she says all of this."
        "And he's nodding like crazy, hoping for the answer he wants to hear."
        "But if he's wanting me to just laugh it all off, then he's disappointed."
        "Because the look on my own face is one of surprise and annoyance."
        bree.say "You think I'm joking?"
        bree.say "That I'd say something like that just for a laugh?!?"
        hide shawn
        show shawn sad
        "Shawn instinctively shrinks away from me."
        "The effect his words have had becoming apparent to him."
        "I can almost see the beads of sweat starting to stand out on his forehead."
        shawn.say "[hero.name], I..."
        shawn.say "I didn't mean it!"
        shawn.say "Well no...I did mean that I didn't want to get married."
        shawn.say "But I didn't mean to make a joke of it!"
        shawn.say "Even if I did ask if you were joking..."
        "Shawn's really starting to sweat now."
        "Tripping over his words and grovelling for forgiveness."
        "But I'm not in the mood to give him any such thing."
        hide shawn with fade
        "And so I turn on my heel before storming away."
        "I don't even pause to look over my shoulder either."
        "Because the last thing I want to see right now is Shawn's face."
        $ shawn.love -= 25
    else:

        show shawn happy
        "As soon as he hears and understands what I just said, Shawn's entire demeanour changes."
        "Where before he was listening with interest, now he looks positively elated!"
        show shawn nice
        shawn.say "You're not joking, right?"
        shawn.say "Tell me you're not pulling my leg, yeah?"
        show shawn happy
        "I shake my head, trying to tell Shawn what I think he wants to hear."
        "Because it sounds like he's totally on the same page as me."
        bree.say "Of course I'm not joking, Shawn!"
        bree.say "I'd never joke about something like that."
        show shawn nice
        show fx heart
        shawn.say "Then of course I will!"
        shawn.say "Of course I'll marry you, [hero.name]!"
        show shawn happy
        "For a moment I don't know how to react."
        "I just stand there, staring at Shawn in stunned silence."
        "But then the floodgates just seem to burst open."
        show shawn blush at center, zoomAt(1.75, (640, 1190)) with vpunch
        "And I thrown myself at Shawn, my arms spread wide apart."
        "He looks startled by my sudden movements, not at all prepared."
        "Shawn only just manages to catch me, staggering backwards a way."
        "But he manages to recover, hugging me back with all his strength."
        bree.say "Oh my god..."
        bree.say "We're getting married!"
        show shawn nice
        shawn.say "I know, I know..."
        shawn.say "And I'm bloody terrified!"
        shawn.say "But good terrified, you know?"
        $ shawn.set_fiance()
    hide shawn
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
