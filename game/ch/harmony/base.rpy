init python:
    Event(**{
    "name": "harmony_give_phone_number",
    "label": "give_phone_number",
    "girl": "harmony",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(harmony,
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
    "name": "harmony_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(15, 16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(harmony,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "harmony",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_auto_greet",
    "label": "auto_greet",
    "girl": "harmony",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(harmony,
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
    "name": "harmony_auto_chat",
    "label": "auto_chat",
    "girl": "harmony",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(harmony,
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
    "name": "harmony_are_you_sick",
    "label": "are_you_sick",
    "girl": "harmony",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (harmony, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_ask_out",
    "label": "ask_out",
    "girl": "harmony",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(harmony,
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
    "name": "harmony_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "harmony",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label harmony_bye(bye_outfit=None):
    call npc_bye_outfit (npc=harmony, bye_outfit=bye_outfit) from _call_npc_bye_outfit_10
    $ (day, h, activity, bye_outfit) = _return
    if not activity == harmony.activity:
        if day != game.week_day:
            $ harmony.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ harmony.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"harmony {bye_outfit}")
        if activity["activity"] == "sleep":
            harmony.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            harmony.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            harmony.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            harmony.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            harmony.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            harmony.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            harmony.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            harmony.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            harmony.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            harmony.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            harmony.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            harmony.say "I'll go get dressed."
        hide harmony
    return

label harmony_cheated(action, cheat_npc=None):
    show harmony
    if cheat_npc and Harem.together(cheat_npc, harmony):
        show harmony blush
        harmony.say "Aren't you forgetting something?"
        show harmony
        "And without warning Harmony kisses me."
        $ harmony.love += 1
        $ harmony.flags.kiss += 1
    elif harmony.sub >= 75:
        show harmony blush
        show fx heart
        $ harmony.sub += 1
        "I see Harmony looking at me [action] someone else with envy and lust in her eyes."
    else:
        show harmony angry
        show fx anger
        $ loss = 10
        if harmony.flags.girlfriend or harmony.flags.fiance:
            $ loss += 5
        $ harmony.love -= loss
        "I see Harmony looking at me [action] someone else with a disgusted look on her face..."
    hide harmony
    return

label harmony_greet:
    if renpy.has_label(f"harmony_greet_dialogues_{hero.gender}") and not harmony.flags.greeted:
        scene expression f"bg {game.room}"
        $ harmony.flags.greeted = TemporaryFlag(True, 1)
        show harmony
        $ result = randint(1, 3)
        if result == 1:
            harmony.say "Hello, [hero.name]."
        elif result == 2:
            harmony.say "Hi, [hero.name]."
        elif result == 3:
            harmony.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                harmony.say "Good morning [hero.name]."
            elif game.hour < 19:
                harmony.say "Good afternoon [hero.name]."
            else:
                harmony.say "Good evening [hero.name]."
        call expression f"harmony_greet_dialogues_{hero.gender}" from _call_expression_239
        if harmony.flags.submissive_interact:
            if randint(0, 1) == 0:
                harmony.say "Mmm...I wanna get down on my knees and worship your cock!"
            else:
                harmony.say "I think I should start a cult [hero.name]."
                harmony.say "Whose only purpose is to worship your mighty cock."
        hide harmony
    return

label harmony_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Harmony."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Harmony."
        elif game.hour < 12:
            mike.say "Good morning Harmony."
        elif game.hour < 19:
            mike.say "Good afternoon Harmony."
        else:
            mike.say "Good evening Harmony."
    return

label harmony_kiss:
    scene expression f"bg {game.room}"
    if harmony.love < 25 and not harmony.is_girlfriend and not game.active_date.score >= 75:
        show harmony
        "I know that Harmony's not your average girl, that she's one hell of a lot more innocent and maybe even naive than average."
        "That's why I've waited so long and looked so hard for the right moment to do something like this."
        "I've wanted to kiss her forever, and who wouldn't?"
        "I mean, just look at her!"
        "But I must have been reading the signals wrong, or else just swept up in my own feelings for her."
        "As the very moment that I lean in to steal even the most brief and chaste of kisses, Harmony pulls quickly away from me."
        "She does me the favour of not saying anything to add to the awkwardness of the moment."
        "And I end up feeling like a complete clod, trampling all over her delicate feelings."
        $ harmony.love -= 5
        $ harmony.sub -= 5
        hide harmony
    elif not harmony.flags.kiss:
        hide harmony
        $ harmony.love += 5
        if harmony.lesbian > MAX_LES_GUY_SEX:
            $ harmony.lesbian -= 1
        show harmony kiss
        "I've been holding on for so long by now that it's almost starting to become a physical pain."
        "And I decide in that moment that I just can't wait any more, so to hell with the consequences."
        "I lean in and place my lips upon Harmony's, wondering what her reaction to such a bold move on my part will be."
        "She stiffens for a moment, something that I was fully expecting."
        "But then the same resistance seems to just melt away, and I feel her return the kiss."
        "It's gentle at first, and then steadily builds into a more passionate affair."
        "I have no illusions that a girl as shy and pure as Harmony is about to thrust her tongue down my throat."
        "And so knowing that of her, I can appreciate just how much a show of emotion this is for her."
        hide harmony kiss
        $ harmony.flags.kiss += 1
    else:
        hide harmony
        $ harmony.love += 2
        show harmony kiss
        "You could have been forgiven for thinking that Harmony's shyness and purity means she was no fun at all."
        "But her need for privacy means that, once she's alone with me, her passions are free to express themselves."
        "Her kisses are not wild and wicked, but rather long, lingering and likely to leave her quivering with emotion."
        "Each and every time that I steal the chance to kiss her, Harmony's breath comes heavier and with more intensity."
        "And I can feel the way that her heart begins to beat that much faster as she's held in my embrace."
        "It's weird, how you always start out thinking that it's the girls that are really forward that'll get you hot."
        "But the mere sound of Harmony's almost panting breath as she kisses me is something else."
        "I guess it's thinking of what she might do next that makes it so..."
        hide harmony kiss
        $ cheated_girls = game.get_cheated_girls(harmony)
        if cheated_girls:
            call expression randchoice(cheated_girls).id + "_cheated" pass ("kissing") from _call_expression_119
        $ harmony.flags.kiss += 1
    return

label harmony_propose_male:
    show harmony
    if "religious" in harmony.traits:
        "This shouldn't be something that has the power to reduce me to a quivering pile of nerves."
        "Harmony and I have been dating for a good long while by now, and we're getting on really well."
        "At least I think we're getting on well - and so taking things to the next level is logical, right?"
        show harmony happy
        "I mean, she's been sending out what I think are the right signals."
        "We've talked about the future, what each of us really wants out of life."
        "And to me that's enough of a hint that Harmony wants me to make a statement."
        show harmony normal
        "Which is why I have a tiny box in my pocket that feels like it weighs a ton!"
        "All I have to do now is hold myself together and wait for the right moment..."
        show harmony happy
        harmony.say "...and so I told her that she was wrong."
        harmony.say "There's no way that bible verse can be taken to mean anything like that!"
        show harmony normal
        harmony.say "Don't you think that's right, [hero.name]?"
        show fx question
        harmony.say "[hero.name]...what are you doing?!?"
        "I would have thought that was pretty obvious."
        hide fx
        "I'm kneeling down in front of Harmony."
        "And I'm doing it with a ring held between finger and thumb."
        "But I guess she's pretty confused right now, so she deserves to be indulged."
        mike.say "Harmony..."
        mike.say "You know how much I love you."
        mike.say "And that's why I want you to marry me."
        mike.say "Say you will, Harmony - say you'll be my wife?"
        show fx exclamation
        show harmony sad
        "I don't think I've ever seen a look like that on Harmony's face before."
        "Normally she's a picture of confidence, sure in her faith and convictions."
        hide fx
        "But right now she looks like she's been shaken to the core."
        "Harmony blinks and her lips move, but no sound comes out at first."
        "I stay right where I am, patiently awaiting her answer."
        show harmony normal
        "Finally Harmony's head starts to move."
        "And I wait with baited breath to see which way this will go..."
        if harmony.love < 195:
            "But when I see that Harmony is shaking her head, my guts turn to water."
            "There should be some kind of comfort in the fact that she's smiling too."
            "And in the way she grabs my hands and pulls me back to my feet."
            "But instead I just feel humiliated, like she's condescending in all she does."
            harmony.say "Oh, [hero.name]..."
            harmony.say "Whatever's gotten into you!"
            mike.say "Wh...what do you mean, harmony?"
            mike.say "I love you so much!"
            mike.say "And I want to marry you!"
            mike.say "Don't you feel that way too?"
            show harmony happy
            "Harmony rolls her eyes and tuts at this."
            "It sounds to me like she's talking to a dull child."
            harmony.say "Of course I love you, you silly thing!"
            harmony.say "And marriage is the proper way to celebrate that in the eyes of god."
            show harmony normal
            harmony.say "But we're not ready to make that kind of commitment yet, [hero.name]."
            "I shake my head, still confused by what Harmony is telling me."
            mike.say "We...we're not?"
            mike.say "I thought we were pretty holy, Harmony!"
            show harmony happy
            "Harmony smiles again, like she's indulging my stupidity."
            harmony.say "Well, I think I'm about there."
            harmony.say "But you need to be a little bit more holy, [hero.name]."
            harmony.say "Just a smidgeon more pure and uncorrupted!"
            "Harmony holds up her hand, finger and thumb a little way apart."
            "Showing me how close she thinks I am to divine perfection."
            "All I can do is nod and put the ring away."
            "But I can't help feeling humiliated."
            "Like I'm just not good enough for Harmony, no matter how hard I try."
            show harmony normal
            harmony.say "Don't worry, [hero.name]..."
            harmony.say "As soon as you're holy enough, I'll let you know!"
            $ harmony.love -= 25
            $ harmony.sub -= 25
        else:
            "But when I see that Harmony is nodding her head, relief floods over me."
            "And all of the previous doubts that I had seem to vanish into thin air."
            "I leap to my feet and hastily take hold of her hand."
            "And then I push the ring onto her finger as quickly as I can."
            "It's almost as if I'm afraid she's going to change her mind any moment."
            "As if getting the actual ring on her hand somehow seals the deal."
            mike.say "Oh goodness, Harmony..."
            mike.say "I was scared stiff you were going to say no!"
            "Harmony looks up from admiring the ring on her finger."
            "And I realise that she has tears welling in her eyes."
            harmony.say "Oh, [hero.name]..."
            harmony.say "How could you think such a thing?"
            harmony.say "I've been waiting for this moment, aching for it!"
            "Harmony breathes in a pretty impressive lungful of air."
            "She holds it for a moment, her considerable bosom swelling."
            "And then she lets it out in a long sigh of pure satisfaction and happiness."
            harmony.say "I dared to dream that this would happen."
            harmony.say "I even prayed that it might."
            harmony.say "I prayed even though I knew it was selfish of me to do so!"
            harmony.say "But god was listening, and he chose to bless me!"
            "I'm not too sure what I think of god being given all the credit."
            "I mean, I was the one that forked out for the ring."
            "And I didn't feel like I was getting much divine help when I popped the question just now!"
            "But I'm too wrapped up in the fact that Harmony said yes to care too much anyway."
            mike.say "Oh, Harmony..."
            mike.say "We're going to get married!"
            mike.say "I can't wait to spend the rest of my life with you!"
            show harmony happy
            "Harmony smiles and nods happily."
            harmony.say "And when we are, just you wait, [hero.name]."
            show harmony blush
            harmony.say "Because married couples can have so much more fun."
            harmony.say "And what's even better is that god approves of it all!"
            $ harmony.set_fiance()
    elif "slutty" in harmony.traits:
        "Before we get into this, let me just state something for the record."
        "I'm fine with Harmony just the way she is, and I don't want her to change."
        show harmony happy
        "But I'm finding it hard to keep up with the demands that she's making of me."
        "And I figure that this might be something that helps me out and calms her down."
        "That's why I raid my savings and go out to buy a ring for Harmony."
        show harmony normal
        "I want to ask her to marry me, show her that I'm not going anywhere soon."
        "That way maybe she'll realise that she doesn't have to try so hard!"
        "Once I have the ring in my pocket, all I have to do is pick the right moment..."
        show harmony happy
        harmony.say "...so apparently that's a pretty big one!"
        harmony.say "I mean, I was pretty surprised by that."
        harmony.say "Because I'd have wanted a much bigger one..."
        show harmony normal
        show fx question
        harmony.say "[hero.name], are you actually listening to me?"
        "Harmony glances around, realising I'm no longer where she thought I was."
        hide fx
        "Then she looks down to see me kneeling in front of her."
        harmony.say "[hero.name], what are you doing down there?!?"
        "Is she really asking me that question?"
        "I'd have thought the ring in my hand was a pretty good clue!"
        harmony.say "Ooh..."
        show harmony blush
        harmony.say "Is that a cock-ring?"
        harmony.say "Or a new piercing for my pussy?"
        "I blink at this, amazed at Harmony's questions."
        mike.say "Erm, no, Harmony..."
        mike.say "I'm trying to propose to you!"
        mike.say "I love you more than anything in the world..."
        mike.say "Will you marry me?"
        show harmony normal
        "For the first time that I can recall, Harmony seems lost for words."
        "She shakes her head, her mouth moving without words coming out."
        "Part of me is worried that she's actually going to lose it."
        "That Harmony's going to pass out from the surprise and land on top of me!"
        "I make preparations to catch her, which is more of a challenge than you might think."
        "Because Harmony's never been the lightest of girls, and her curves are a real handful!"
        if harmony.love < 195:
            show harmony sad
            "But then I see a change in Harmony's expression."
            "She smiles down at me, but shakes her head at the same time."
            harmony.say "Oh no, [hero.name]..."
            harmony.say "I couldn't do that!"
            "I almost leap to my feet, amazed at her answer."
            "I'm shaking my head as my mind's racing."
            "I just can't understand why Harmony would turn me down!"
            mike.say "Wha...what's the matter, Harmony?"
            mike.say "Why won't you marry me?"
            mike.say "Is it because I'm not exciting enough?"
            mike.say "Well...I can fix that, you'll see!"
            mike.say "I'll do anything you want, Harmony."
            mike.say "Anywhere, anytime, any position!"
            mike.say "Just please say that you'll marry me?"
            show harmony happy
            "Harmony bursts out laughing at this."
            harmony.say "Oh, [hero.name], you're so funny!"
            show harmony normal
            harmony.say "I do want to marry you eventually - just not right now."
            harmony.say "We can get married when the time's right."
            harmony.say "But before that I have a whole list of things that I want to do!"
            show harmony blush
            harmony.say "And I don't think some of them are actually legal for a married couple!"
            "I nod, trying as best I can to come to terms with what Harmony just said."
            "Sure, it stings to be turned down after I went to all that trouble."
            "But I guess that she does kind of have a point."
            "All the same, Harmony can see that I'm hurt."
            show harmony normal
            "She sighs as she tries to explain herself."
            harmony.say "You remember how I used to be when we first met?"
            harmony.say "I was so obsessed with religion it ruled my life."
            harmony.say "But you changed that, taught me there was more to it than that."
            mike.say "What do you mean, Harmony?"
            mike.say "You don't want to get married because it's religious?"
            mike.say "We could have a civil ceremony instead?"
            show harmony sad
            harmony.say "No, [hero.name]..."
            harmony.say "That's not it."
            harmony.say "Things are good right now, so why change them?"
            "I ponder what Harmony's saying, realising that it sounds familiar."
            "And that's because it's pretty much the stock guy response to commitment."
            "If things are good now, then why change them?"
            mike.say "That makes sense, Harmony!"
            mike.say "We can always tie the knot later."
            mike.say "And we can have some fun along the way too!"
            show harmony normal
            "Harmony leans in to kiss me on the cheek."
            "I can't help smiling at this."
            "Sure, it's not the answer that I wanted."
            "But it's left me feeling happier than before."
            "That and like I understand Harmony a lot better too!"
            "I can only nod and smile, already wondering what I've let myself in for..."
            $ harmony.love -= 25
            $ harmony.sub -= 25
        else:
            show harmony
            "But then I see a change in Harmony's expression."
            "She smiles down at me, and she starts giggling too."
            harmony.say "That's even better than a cock-ring!"
            harmony.say "Of course I will, [hero.name]!"
            "She thrusts her hand out towards me."
            show harmony normal
            harmony.say "What are you waiting for?"
            "Not wanting to waste another second, I do as I'm told."
            "I push the ring onto Harmony's finger and then stand up."
            "She's already holding it out at arm's length, admiring how it looks."
            show harmony happy
            harmony.say "I...I can't actually believe this is happening!"
            harmony.say "It's like a dream come true!"
            "Then I shake my head as my thoughts begin to clear."
            mike.say "You mean it, Harmony?"
            mike.say "You really want to marry me?!?"
            show harmony normal
            "Harmony looks up from admiring the ring on her finger."
            "And she seems more than a little confused by the question."
            harmony.say "Erm...yeah, [hero.name]!"
            harmony.say "Why else would I have said yes?"
            mike.say "Well...because I...because you..."
            mike.say "Oh hell, Harmony - I don't know why!"
            mike.say "I was just scared you'd say no, that's all!"
            show harmony happy
            "Harmony laughs at me and shakes her head."
            harmony.say "It's a real no-brainer, [hero.name]!"
            show harmony normal
            harmony.say "I mean...you remember how I used to be, right?"
            harmony.say "I was obsessed with religion, it was my life!"
            harmony.say "And I always thought it would be - until you came along!"
            show harmony blush
            harmony.say "You showed me that I was missing out on life...and all that cock!"
            "Harmony lets out a particularly filthy laugh to underline her point."
            "But she also wraps her arms around my waist as she does so."
            "And she pulls me into a warm embrace, she curves pressing against me."
            "That gesture reminds me that Harmony's not all about the sex."
            "Underneath all that there's a genuine love for me too."
            mike.say "Well, once we're married we can take things at our own pace, yeah?"
            mike.say "It's like we won't have anything to prove to anyone after that."
            mike.say "Because I kind of feel like we've been a little crazy, you know?"
            show harmony happy
            "Harmony lets out the filthiest snort of laughter I've ever heard."
            "And she shakes her head as she leans it on my shoulder."
            harmony.say "Ha!"
            harmony.say "That's a good one, [hero.name]!"
            show harmony blush
            harmony.say "I have a whole list of crazy shit I want to do!"
            harmony.say "And I don't think some of them are actually legal for unmarried couples!"
            harmony.say "Us tying the knot means they're all on the menu from now on!"
            $ harmony.set_fiance()
    else:
        "I've been getting a strange feeling when I'm around Harmony for a while now."
        "At first it was hard to put a finger on just what it actually was."
        "On the surface, we were both happy and having a good time together."
        "But I always thought that there was something I should have remembered."
        "Something important that was just out of mental reach when I thought about it."
        "And then it hit me - I was feeling like we needed to go to the next level!"
        show harmony happy
        "Yeah, I know, I know..."
        "Guys aren't supposed to be the ones that think about getting more serious."
        "We're supposed to cringe at the very mention of long-term commitment."
        "But I can't explain it, that's just the way I was feeling."
        show harmony normal
        "And I knew that I needed to do something to express those feelings too."
        "So what else is a guy in that position going to do?"
        "I raided my savings, went to a local jeweller, and I bought a ring."
        "And now here I am, waiting for the right moment to pop the question..."
        show harmony happy
        harmony.say "...can't believe I was ever that brain-washed!"
        harmony.say "I've actually been reading up on a lot of other religions recently."
        harmony.say "And I just can't believe how interesting they are, you know?"
        show harmony normal
        show fx question
        harmony.say "[hero.name], are you even listening to me right now?"
        harmony.say "W...wait...what are you doing?!?"
        "Harmony's face is a picture as she stares down at me."
        hide fx
        "Well, she has to, because I'm kneeling in front of her."
        "Before she can come to her senses, I pull out the ring."
        mike.say "Harmony..."
        mike.say "I love you more than anything and anyone..."
        mike.say "Will you marry me?"
        show fx exclamation
        "Suddenly Harmony seems to lose the power of speech."
        "She covers her cheeks with her hands, already blushing."
        "And she blinks too, as if she can't believe her eyes."
        hide fx
        harmony.say "I...I..."
        harmony.say "W...wh...wha..."
        harmony.say "Oh...oh....oh..."
        "I stay exactly where I am, still looking up at Harmony."
        "My expression is patient and hopeful."
        "I'm just waiting for her to give me an answer..."
        if harmony.love < 195:
            show harmony sad
            "Suddenly Harmony seems to snap out of it."
            "She shakes her head and reaches out to grab my hands."
            "For a moment I think she's going to accept the ring."
            "But then she just pulls me to my feet."
            harmony.say "Put that thing away, [hero.name]!"
            harmony.say "It's sweet of you, really it is."
            harmony.say "But we're not there yet."
            "I do as I'm told, more out of confusion than anything else."
            "Then I shake my head as my thoughts begin to clear."
            mike.say "What do you mean, Harmony?"
            mike.say "I thought we'd been getting on great recently?"
            mike.say "So why not make things official?"
            show harmony normal
            "Harmony gives me a smile and shakes her own head too."
            harmony.say "I agree with all of that, [hero.name]."
            harmony.say "Right up to the point where you tried to put a ring on it!"
            "Harmony sighs as she tries to explain herself."
            harmony.say "You remember how I used to be when we first met?"
            harmony.say "I was so obsessed with religion it ruled my life."
            harmony.say "But you changed that, taught me there was more to it than that."
            mike.say "What do you mean, Harmony?"
            mike.say "You don't want to get married because it's religious?"
            mike.say "We could have a civil ceremony instead?"
            show harmony sad
            harmony.say "No, [hero.name]..."
            harmony.say "That's not it."
            harmony.say "It's more that I don't want to rush into such a massive commitment."
            show harmony normal
            harmony.say "I agree that things are good right now, so why change them?"
            "I ponder what Harmony's saying, realising that it sounds familiar."
            "And that's because it's pretty much the stock guy response to commitment."
            "If things are good now, then why change them?"
            mike.say "That makes sense, Harmony!"
            mike.say "I kind of proposed because I felt like I was supposed to."
            mike.say "Like you'd think I wasn't committed if I didn't!"
            "Harmony leans in to kiss me on the cheek."
            show harmony happy
            harmony.say "Give me a break, [hero.name]!"
            harmony.say "I'm pretty new to this non-religious and non-crazy stuff!"
            "I can't help smiling at this."
            "Sure, it's not the answer that I wanted."
            "But it's left me feeling happier than before."
            "That and like I understand Harmony a lot better too!"
            $ harmony.love -= 25
            $ harmony.sub -= 25
        else:
            "Suddenly Harmony seems to snap out of it."
            "She nods her head and reaches out to grab my hands."
            "For a moment I'm worried she's not going to accept the ring."
            "But then she just pulls me to my feet."
            show harmony happy
            harmony.say "Of course I will, [hero.name]!"
            harmony.say "Stick that thing on me!"
            "I do as I'm told, more out of confusion than anything else."
            "Then I shake my head as my thoughts begin to clear."
            mike.say "You mean it, Harmony?"
            mike.say "You really want to marry me?!?"
            show harmony normal
            "Harmony looks up from admiring the ring on her finger."
            "And she seems more than a little confused by the question."
            harmony.say "Erm...yeah, [hero.name]!"
            harmony.say "Why else would I have said yes?"
            mike.say "Well...because I...because you..."
            mike.say "Oh hell, Harmony - I don't know why!"
            mike.say "I was just scared you'd say no, that's all!"
            show harmony happy
            "Harmony laughs at me and shakes her head."
            harmony.say "I've got to admit it came out of the blue."
            show harmony normal
            harmony.say "But it just felt right the moment you said it."
            harmony.say "I don't think I could explain it either!"
            "Harmony blushes a little before she goes on."
            harmony.say "I mean...you remember how I used to be, right?"
            harmony.say "I was obsessed with religion, it was my life!"
            harmony.say "And I always thought it would be - until you came along!"
            show harmony happy
            harmony.say "You showed me that I was missing out on life...and love!"
            harmony.say "So far going along with your crazy ideas has worked out pretty well for me."
            "Harmony leans in to kiss me on the cheek."
            "I can't help smiling at this."
            "Her explanation is quirky and maybe even a little crazy."
            "But it's also one hundred percent Harmony too!"
            "And I just know that this is going to be one hell of an adventure!"
            $ harmony.set_fiance()
    return

label harmony_date_male:
    if Harem.find_by_name("goodevil") and Harem.find_by_name("goodevil").is_active(harmony):
        menu:
            "Ask Harmony on a date":
                call harmony_ask_date_alone_male from _call_harmony_ask_date_alone_male
            "Set up a date with Harmony and Lexi" if Harem.find_by_name("goodevil") and "goodevil_harem_event_01" not in DONE and not hero.calendar.find(label="goodevil_harem_event_01"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_16
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "goodevil", ["harmony", "lexi"], "goodevil_harem_event_01", "Date (Harmony & Lexi)", "missed_goodevil_harem_date"))
                else:
                    call goodevil_harem_event_01 from _call_goodevil_harem_event_01
                    $ DONE["goodevil_harem_event_01"] = game.days_played
                    call sleep from _call_sleep_83
                    $ game.pass_time(2)
                return
            "Set up a date with Harmony and Lexi" if Harem.find_by_name("goodevil") and "goodevil_harem_event_01" in DONE and not hero.calendar.find(label="goodevil_harem_fuck_date"):
                call select_date_time (fixed_hour=20) from _call_select_date_time_17
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                if day != "now":
                    $ hero.calendar.add(day, HaremAppointment(hour, "goodevil", ["harmony", "lexi"], "goodevil_harem_fuck_date", "Date (Harmony & Lexi)", "missed_goodevil_harem_date"))
                else:
                    call goodevil_threesome_mikebedroom from _call_goodevil_threesome_mikebedroom
                    call sleep from _call_sleep_84
                    $ game.pass_time(2)
                return
    else:
        call harmony_ask_date_alone_male from _call_harmony_ask_date_alone_male_1
    return _return

label harmony_ask_date_alone_male:
    mike.say "Harmony, would you like to go on a date with me?"
    if harmony.love < 50 or harmony.flags.nodate:
        harmony.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        harmony.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
