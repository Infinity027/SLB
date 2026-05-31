init python:
    Event(**{
    "name": "kylie_give_phone_number",
    "label": "give_phone_number",
    "girl": "kylie",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(kylie,
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

label kylie_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Kylie."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Kylie."
        elif game.hour < 12:
            bree.say "Good morning Kylie."
        elif game.hour < 19:
            bree.say "Good afternoon Kylie."
        else:
            bree.say "Good evening Kylie."
    return



label kylie_ask_date_female:



    call kylie_ask_date_alone_female from _call_kylie_ask_date_alone_female
    return _return

label kylie_ask_date_alone_female:
    if not kylie.flags.hadadate:
        bree.say "We've been having such a good time together, Kylie."
        bree.say "I was wondering if you wanted to do something with me."
        bree.say "You know...just the two of us?"
        bree.say "We could see a movie or get a bite to eat maybe?"
        kylie.say "That sounds kind of like a date, [hero.name]!"
        "I shrug and offer Kylie what I hope is a nonchalant smile."
        bree.say "Well...it was kind of supposed to, Kylie!"
        bree.say "So what do you say?"
        "Kylie returns the smile."
    else:
        bree.say "Let's go on a date, Kylie!"
    if kylie.love < 50 or kylie.flags.nodate:
        if not kylie.flags.hadadate:
            kylie.say "I think we need to keep things as they are, [hero.name]."
            kylie.say "I like you a lot, but you know I only love [mike.name], right?"
        else:
            kylie.say "Nope..."
        $ date_choice = False
    else:
        kylie.say "I think that sounds great, [hero.name]."
        kylie.say "Let's do it as soon as we can, okay?"
        $ kylie.flags.hadadate = True
        $ date_choice = True
    return date_choice

label kylie_kiss_female:
    scene expression f"bg {game.room}"
    if kylie.love + hero.charm < 80 and not kylie.is_girlfriend and not game.active_date.score >= 75:
        show kylie
        "I feel like there's something in the air whenever Kylie's around."
        "It reminds me of a static charge, like a tingle of electricity."
        "I'm sure she feels it too, as I can see the way she looks at me."
        "Before too long I know that I have to act on this, before it's too late."
        "So when Kylie and I are next alone, I decide to make my move."
        show kylie at center, zoomAt(1.5, (640, 1040))
        "I lean in and try to place my lips against Kylie's."
        show kylie surprised
        "But almost the same moment I do, she jerks her head away."
        "And I find myself staring at her in the most awkward manner possible."
        "Kylie's eyes are wide as she stares back at me too."
        "She looks like what I just did took her by complete surprise."
        "And all I can do is smile, then shake my head."
        show kylie sadhappy
        "Maybe I can convince her it was all just a misunderstanding?"
        "Though that won't do anything to cure the churning sensation in my stomach right now..."
        $ kylie.love -= 1
        hide kylie
    elif not kylie.flags.kiss:
        show kylie
        "There's just something in the air whenever Kylie's around me."
        "I can feel it, like a tingle of electricity between us."
        "And I'm sure that she can feel it too from the way she looks at me."
        "It just keeps on happening, getting more intense each time."
        "Until I can't stand it anymore, and I know that I have to act."
        "As soon as Kylie and I are alone, I make the first move."
        show kylie at center, zoomAt(1.5, (640, 1040))
        "I lean in, holding her eye the whole time."
        "There's an intense interest in Kylie's gaze."
        "And I can imagine that mine betray my thoughts too."
        "They must be full of fear and desire in equal measures!"
        hide kylie
        show kylie kiss
        with fade
        "But Kylie doesn't pull away, even as our lips meet for the first time."
        "And when they do, everything seems to fall into place."
        "All of my doubts disappear, and I feel a sense of release."
        "Kylie returns the kiss with an equal amount of passion too."
        "Letting me know that this is not merely something I'm feeling alone."
        hide kylie kiss with fade
        $ kylie.flags.kiss += 1
        $ kylie.love += 5
        call kylie_kiss_reaction_female from _call_kylie_kiss_reaction_female
    else:
        hide kylie
        show kylie kiss
        with fade
        "Now that we've started, it's like there's no way for us to stop!"
        "Kylie and I are stealing kisses from each other whenever we can."
        "And no matter how many times we do it, it's never enough!"
        "Soon it becomes like a game, between the two of us."
        "How often can we do it and who can start it off first."
        "As well as where and in front of who can we do it too!"
        "I can't believe that I was puzzling over what that feeling was."
        "Now that Kylie and I have made that connection, it just seems so obvious."
        "And as the connection between us grows, it feels all the more natural."
        "The spark's still there, believe me."
        "But now I'm starting to feel it somewhere else as well."
        "Somewhere a lot more intimate and special than my lips too..."
        hide kylie kiss with fade
        $ kylie.flags.kiss += 1
        $ kylie.love += 5
        call kylie_kiss_reaction_female from _call_kylie_kiss_reaction_female_1
    return

label kylie_kiss_reaction_female:
    if kylie.lesbian < MIN_LES_GIRL_SEX:
        $ kylie.lesbian += 1
    return

label kylie_propose_female:
    show kylie
    "I've never been too good at this kind of thing, no matter how hard I've tried."
    "Somehow, when it comes to relationships, I always seem to go to one extreme or the other."
    "One time I fall one a person and they're all I want, so I come over too needy and intense."
    "The next I do all that I can to make sure I'm all casual, and so they think I'm not serious!"
    "Urgh...I guess what I'm trying to say is that I don't know which is the better choice."
    "But I do pride myself on knowing that there are just some times in life when you have to try."
    "Those occasions on which you can't let fear of the consequences rob you of the chance to be happy."
    "And that's why I'm talking myself up as I wait for Kylie to arrive on the scene."
    "Since we met and started to hang-out, things seem to have been on the up for me."
    "We got on so well that soon enough, when we were hanging-out, it was just the two of us."
    "And when we began to admit our feelings for each other and to date, things got better still."
    "Sure, I know that Kylie can be a little intense at times."
    "And then there's all the emotional baggage that she has with [mike.name]..."
    "But I feel like we're working our way through all of that pretty well."
    "Because none of the stuff that I've discovered about her past has changed how I feel about Kylie."
    "In fact, I feel like I want to take things to the next level with her, to really make a commitment."
    hide kylie with fade
    "Which is why I'm waiting to be able to ask her that most fateful of questions."
    "I'm waiting to ask Kylie if she'll marry me!"
    kylie.say "Hey, [hero.name]!"
    with vpunch
    bree.say "Wha..."
    bree.say "Whoa!"
    show kylie a at center, zoomAt(1.5, (640, 1040)) with hpunch
    "Hearing the sound of Kylie's voice behind me, I leap around."
    bree.say "Kylie..."
    bree.say "What are you doing there?"
    bree.say "I thought you'd be coming from the other direction!"
    show kylie annoyed a
    kylie.say "Is that a problem?"
    show kylie sadhappy a
    kylie.say "You know I like to mix it up a little, [hero.name]."
    show kylie happy a
    kylie.say "When they don't know which way you're coming from, it keeps people on their toes!"
    bree.say "You're not kidding..."
    show kylie normal a
    kylie.say "Anyway, wasn't there something you wanted to ask me?"
    "I nod my head, doing the best I can to clear it at the same time."
    "The truth is that Kylie's managed to rattle me more than I expected."
    "And I need to get my brain back in gear if I want to pull this off."
    bree.say "Okay, Kylie..."
    bree.say "Here's the thing..."
    bree.say "I think we're good together - no, actually we're great together."
    bree.say "And so I want to take things to the next level."
    show kylie surprised a
    "Kylie's eyes go wide as she hears what I have to say."
    "And then she gasps as realisation sets in."
    kylie.say "[hero.name]..."
    kylie.say "You mean..."
    bree.say "Yeah, Kylie - I want us to get married!"
    if kylie.love < 195:

        "Kylie doesn't hesitate for a moment."
        show kylie sad a
        "She gives me her answer with a curt shake of the head."
        kylie.say "No way, [hero.name]..."
        kylie.say "There's no way that I could ever get married!"
        "I find myself staring at Kylie in sheer amazement."
        "My mouth hanging open from the surprise of hearing her answer."
        bree.say "What do you mean, Kylie?"
        bree.say "I thought that we were growing together as a couple?"
        show kylie sadhappy a
        "Kylie surprises me again by nodding at this."
        kylie.say "That's right, [hero.name]."
        kylie.say "We've never been closer than we are right now."
        bree.say "Then I don't understand your answer."
        bree.say "Why wouldn't you want to marry me?"
        show kylie annoyed a
        "For a moment, Kylie looks conflicted."
        "Like she wants to be totally honest with me."
        "But she's worried about the fallout from doing so."
        show kylie sad a
        kylie.say "Let's just say you don't know everything about me, [hero.name]."
        kylie.say "There was a time when I had...problems."
        kylie.say "When I used to live in a fantasy world."
        kylie.say "I imagined who I'd be, where I'd live and who I'd marry..."
        kylie.say "And I had a hard time leaving it behind to live in reality."
        "All I can do is nod as Kylie tries to explain herself."
        "But to me it sounds complicated."
        "Maybe a little scary too."
        "And I can't help thinking we have a long way to go before we deal with it."
        "Before we really get to know each other."
        $ kylie.love -= 25
    else:

        "Kylie doesn't hesitate for a moment."
        show kylie smile a
        "She gives me her answer with an enthusiastic nod."
        show kylie happy a
        kylie.say "That's a great idea, [hero.name]..."
        kylie.say "I wish I'd thought of it myself!"
        show kylie smile
        "All of a sudden, Kylie and I are grinning like a pair of fools."
        "I grab hold of her hands and she squeezes mine in return."
        "And it's all that we can do to keep from dancing around in a circle."
        bree.say "Oh god..."
        bree.say "I was so worried you were going to say no!"
        "Kylie shakes her head at this."
        show kylie happy
        kylie.say "I had no idea you were going to propose."
        kylie.say "But I feel like I was always going to say yes."
        show kylie normal a
        kylie.say "There was a time when I had...problems."
        kylie.say "When I used to live in a fantasy world."
        kylie.say "I imagined who I'd be, where I'd live and who I'd marry..."
        kylie.say "And I had a hard time leaving it behind to live in reality."
        show kylie happy
        show fx heart
        kylie.say "But you helped me to get over all that, [hero.name]."
        kylie.say "You taught me how to embrace the here and now!"
        show kylie smile
        "Now I'm the one nodding eagerly as Kylie explains herself to me."
        "There's going to be so much to do, so many things to arrange."
        "But for the moment, all I have to do is be here with Kylie."
        "And hopefully I'll be with her for a long time to come too!"
        $ kylie.set_fiance()
    hide kylie
    return

label kylie_pregnancy_congratulations:
    show kylie surprised
    "The moment Kylie sees me, I can just sense that she knows I'm pregnant."
    "It's like she can read it in my aura or smell it on me somehow."
    "And she seems to be regarding me with a mixture of jealousy and admiration."
    show kylie happy
    kylie.say "You're pregnant, aren't you?"
    kylie.say "Tell me I'm right, [hero.name]!"
    "I find myself blinking in surprise at Kylie's choice of words."
    "Because most people don't simply walk up and demand to know that you're pregnant!"
    "But then Kylie always did seem just a little weird."
    "So I do my best to nod and smile in response."
    bree.say "Got it in one, Kylie!"
    bree.say "I'm going to have a baby!"
    show kylie angry
    "Kylie nods, though her demeanour doesn't become any more friendly."
    kylie.say "So..."
    kylie.say "Is [mike.name] the father?"
    "The question is so bare-faced and bold that I'm taken aback."
    show kylie normal
    "And I have to collect myself before I can answer it."
    if hero.flags.pregnancy_father == "mike":
        bree.say "Erm..."
        bree.say "I'm not sure what it has to do with you, Kylie..."
        bree.say "But yes, [mike.name] does happen to be the father of my child."
        "Kylie's eyes narrow as she looks me up and down."
        "And the experience is more than a little off-putting."
        show kylie angry
        kylie.say "Oh, I see."
        kylie.say "So that's the way it has to be, is it?"
        bree.say "Kylie..."
        bree.say "What does that mean exactly?"
        kylie.say "You won this round, [hero.name]."
        kylie.say "But don't think it's over!"
        hide kylie with easeoutright
        "With that, Kylie turns on her heel and walks away."
        "Leaving me feeling confused and worried in the extreme."
        $ kylie.love -= 5
        $ kylie.yandere += 10
    else:
        bree.say "Erm...no, Kylie..."
        bree.say "[mike.name]'s not the father."
        show kylie happy
        "All of a sudden Kylie's mood changes."
        "Just like that she becomes all sweetness and light."
        kylie.say "Congratulations, [hero.name]..."
        kylie.say "I just know you're going to be a fantastic mommy!"
        "I nod and smile, just waiting for the conversation to be over."
        "Though part of me can't help wondering..."
        "What would she have said if the answer had been yes?"
        $ kylie.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
