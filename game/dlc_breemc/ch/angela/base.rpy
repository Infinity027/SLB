init python:
    Event(**{
    "name": "angela_auto_greet",
    "label": "auto_greet",
    "girl": "angela",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("None"),
            ),
        PersonTarget(angela,
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
    "name": "angela_give_phone_number",
    "label": "give_phone_number",
    "girl": "angela",
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(angela,
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
    "name": "angela_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(11, 12),
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(angela,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "angela",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "angela_are_you_sick",
    "label": "are_you_sick",
    "girl": "angela",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(angela,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (angela, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "angela_auto_chat",
    "label": "auto_chat",
    "girl": "angela",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(angela,
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
    "name": "angela_ask_out",
    "label": "ask_out",
    "girl": "angela",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(IsActivity("ask_date")),
            ),
        PersonTarget(angela,
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
    "name": "angela_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "angela",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(angela,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label angela_bye(bye_outfit=None):
    call npc_bye_outfit (npc=angela, bye_outfit=bye_outfit) from _call_npc_bye_outfit_24
    $ (day, h, activity, bye_outfit) = _return
    if not activity == angela.activity:
        if day != game.week_day:
            $ angela.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ angela.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"angela {bye_outfit}")
        if activity["activity"] == "sleep":
            angela.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            angela.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            angela.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            angela.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            angela.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            angela.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            angela.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            angela.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            angela.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            angela.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            angela.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            angela.say "I'll go get dressed."
        hide angela
    return

































label angela_cheated(action, cheat_npc=None):
    show angela disgusted
    if action == "kissing":
        "The kiss feels SO good, so right - until I look up and see Angela staring at me, horror in her eyes!"
    else:
        "This feels SO good, so right - until I look up and see Angela staring at me, horror in her eyes!"
    $ loss = 5
    if angela.flags.girlfriend or angela.flags.fiance:
        $ loss += 5
    $ angela.love -= loss
    return

label angela_kiss_female:
    scene expression f"bg {game.room}"
    if angela.love < 25 and not angela.is_girlfriend and not game.active_date.score >= 75:
        show angela
        "This feels to weird to me, so strange that I don't know what to do."
        "So I just go with my instinct, leaning in ever closer to Angela."
        "She doesn't seem to notice what I'm doing until the very last moment."
        "And then her eyes go wide with surprise, her breath catching in her throat."
        "For a moment I hold my breath, waiting to see if she leans into me."
        "To see if she takes the invitation to kiss me..."
        show angela disgusted
        "But then Angela pulls back and turns her head away from me."
        "In that moment I feel a sudden, dull pain in my chest."
        "Perhaps it's not my heart breaking, not quite."
        "But it's wounded nonetheless, and this is going to leave a scar for sure."
        if angela.love < 40:
            $ angela.sub += 1
        else:
            if randint(1, 2) == 1:
                $ angela.love -= 1
        hide angela
    elif not angela.flags.kiss:
        hide angela
        show angela kiss
        "This feels to weird to me, so strange that I don't know what to do."
        "So I just go with my instinct, leaning in ever closer to Angela."
        "She doesn't seem to notice what I'm doing until the very last moment."
        "And then her eyes go wide with surprise, her breath catching in her throat."
        "For a moment I hold my breath, waiting to see if she leans into me."
        "To see if she takes the invitation to kiss me..."
        "And she does just that, she does exactly what I hope she would!"
        "But all the same, it still takes me completely by surprise."
        "I wanted this like crazy, and yet when it happens, I'm stunned!"
        "Every second that Angela kisses me, my heart is pounding in my chest."
        "And I know that I don't want this thing to end!"
        hide angela kiss
        $ angela.flags.kiss += 1
        $ angela.love += 5
        call angela_kiss_reaction_female from _call_angela_kiss_reaction_female
    else:
        hide angela
        show angela kiss
        "Angela seems to know the signals that I'm giving out."
        "And she doesn't hesitate to give me what I want either."
        "Her kisses are either short and intense, leaving me wanting more."
        "Or else they're long and lingering, leaving me feeling exhausted."
        "But the thing is that I never know which kind she's in the mood to give me."
        "And so until the moment that our lips touch, it's a mystery."
        "The only way that I can ever find out is as the kiss is shared between us."
        hide angela kiss
        $ angela.flags.kiss += 1
        $ angela.love += 5
        call angela_kiss_reaction_female from _call_angela_kiss_reaction_female_1
    return

label angela_propose_female:









    "All the time that Angela and I were going through the affair with her husband, everything was so intense."
    "There was weird and crazy stuff happening on an almost daily basis, things getting stranger all the time."
    "In the middle of it all, I couldn't hope to see what life would be like once all of it was finally over."
    "So now that it is, everything seems weird all over again, because it's so different in comparison."
    "Every day that passes when there's not a new revelation to shake me up feels odd."
    "And not having to think up plots to win Angela's freedom means that I'm often lost for something to do!"
    "But I think that initial stage of strangeness is finally starting to come to an end now."
    "I find that I'm not looking over my shoulder the whole time."
    "That and I can actually enjoy my time with Angela when we're together."
    "I mean look at us right now - we're just hanging out at the beach."
    "You could easily mistake us for nothing more than an ordinary couple!"
    angela.say "Penny for your thoughts, [hero.name]?"
    "The sound of Angela's voice shakes me out of my wandering thoughts."
    "And I turn to glance at her, lying beside me on the sand."
    show angela swimsuit normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Huh?"
    bree.say "What's that, Angela?"
    bree.say "I was miles away!"
    "Angela chuckles and shakes her head."
    show angela happy
    angela.say "I can see that!"
    angela.say "I was just wondering what had you so wrapped up in your own head."
    show angela normal
    bree.say "Oh, you know..."
    bree.say "I was just thinking about how ordinary we must look."
    show angela annoyed
    "Angela's face turns into an expression of mock offence at this."
    "And she gives me a gentle shove on the arm."
    show angela happy
    angela.say "Speak for yourself, [hero.name]..."
    angela.say "I didn't come this far in life to be called ordinary!"
    show angela normal
    bree.say "No, no..."
    bree.say "That's not what I meant."
    bree.say "It's just that we've been through so much stuff recently."
    bree.say "And now that it's all over, you'd never know it to look at us."
    show angela normal
    "Angela leans back on her elbow and looks out to sea."
    "I can see that she's contemplating my words as she does so."
    "And I give her the space to think up a considered answer."
    show angela flirt
    angela.say "You know what, [hero.name]..."
    show angela happy
    angela.say "That's kind of a relief for me."
    angela.say "I feel like I want to pass for normal for a while."
    show angela worried
    angela.say "I really used to hate it when people recognised me from the posters."
    angela.say "And now the last thing I want is to be remembered as Dylan Devant's assistant."
    show angela fragile
    "I nod in agreement."
    bree.say "You're far more than that, Angela."
    bree.say "You're [mike.name] and Minami's mom, for one thing."
    bree.say "And..."
    "I reach out, putting my hand atop Angela's."
    bree.say "You're pretty important to me too!"
    show angela surprised
    "Angela looks up in surprise."
    show angela normal
    "But then her face breaks into a genuine smile."
    show angela happy
    angela.say "Thank you, [hero.name]."
    angela.say "I feel the same way about you too."
    angela.say "I just sometimes have those moments of realisation, you know?"
    angela.say "It hits me that I'm starting a new chapter of my life."
    angela.say "That I have someone new to share it with as well."
    show angela normal
    "I'm nodding all the time that Angela's saying this."
    "Because I feel the exact same way."
    bree.say "Me too, Angela, me too!"
    bree.say "I've wanted to talk to you about the future for a while now."
    bree.say "But I was never sure if you were ready to think about that kind of stuff."
    bree.say "You know, after everything that's happened?"
    "Angela holds up a hand to stop me."
    "And for a moment I think that she's going to ask me to change the subject."
    "So what she actually says next comes as a rather big surprise."
    show angela shy
    angela.say "I know how you feel, [hero.name]."
    angela.say "So maybe I should have said this earlier..."
    show angela blush
    angela.say "But what the hell, I'm saying it now - I love you!"
    bree.say "Angela..."
    bree.say "I..."
    bree.say "I love you too!"
    "Neither of us has to even think about what happens next."
    hide angela
    show angela kiss swimsuit
    with fade
    $ angela.flags.kiss += 1
    "We both lean in close and share a long, lingering kiss."
    "And in doing so, I feel like we express everything that's gone unsaid."
    "All of those little niggling questions seem to disappear in mere seconds."
    "And once it's over, I feel more confident and whole than I have in a long time."
    show angela shy swimsuit at center, zoomAt(1.5, (640, 1040)) with fade
    bree.say "So..."
    bree.say "I guess you see this thing going the distance, right?"
    bree.say "You and me being together for the long-term?"
    show angela happy
    angela.say "Oh yeah, [hero.name]!"
    angela.say "And I don't see it staying as 'this thing' either."
    angela.say "If that's what you want too?"
    show angela normal
    bree.say "You mean you want to make it formal?"
    bree.say "I was worried you might have been put off being married for life!"
    show angela happy
    angela.say "Maybe to hypnotists!"
    angela.say "But certainly not to the right person."
    show angela normal
    bree.say "Then let's do it..."
    bree.say "Let's make it official!"
    "I get down on one knee, because I'm a sucker for romantic traditions."
    "And I ask the question..."
    bree.say "Angela..."
    bree.say "Will you make me the happiest girl in the world?"
    bree.say "Will you marry me?"
    show angela surprised
    "Angela gasps in surprise and sheer amazement."
    "In fact, she's so shocked that she leaves me down on one knee for quite a while!"
    "And I'm beginning to ache by the time she actually give me her answer."
    if angela.love < 195:
        show angela annoyed
        angela.say "[hero.name]..."
        angela.say "I...I don't know what to say!"
        bree.say "Well...yes or no is kind of traditional right about now!"
        show angela blush
        "Angela's cheeks flush a bright shade of red and she looks this way and that."
        "It's almost like she can't bring herself to look me straight in the eye."
        "I get slowly to my feet, a sense of dread beginning to settle over me."
        bree.say "Angela..."
        bree.say "Are you okay?"
        bree.say "I know this is a bit out of the blue..."
        "Angela waves away my concerns, a tight smile on her face."
        "But I can see that the smile is just for show."
        show angela happy
        angela.say "Oh, [hero.name]..."
        angela.say "Why did you have to go and ask me that?"
        angela.say "Things were going so well."
        angela.say "We were having so much fun!"
        show angela fragile
        "I shake my head, baffled by what she's saying."
        bree.say "I...I don't understand?"
        bree.say "If things are so great, why not make it official?"
        show angela worried
        angela.say "Because I'm still trying to deal with how my last marriage ended, that's why!"
        angela.say "I still don't know how much of that was me and how much was stuff planted in my head!"
        show angela fragile
        bree.say "Oh...I see..."
        bree.say "I'm sorry, Angela..."
        show angela worried
        angela.say "Look, [hero.name]..."
        angela.say "Let's just forget about it, okay?"
        show angela fragile
        "I nod silently, feeling stupid for not seeing the obvious issues of Angela's past."
        "But I'm also more than a little afraid of what they could mean for our future too."
        $ angela.love -= 25
        $ angela.sub -= 25
    else:
        angela.say "[hero.name]..."
        angela.say "I...I don't know what to say!"
        bree.say "Well...yes or no is kind of traditional right about now!"
        angela.say "Oh god..."
        show angela happy blush
        angela.say "Yes...yes of course I will!"
        show angela normal
        "I almost forget to get back to my feet as Angela says those words."
        "I mean, this is exactly what I wanted to hear her say."
        "But now that it's actually happening, it's kind of surreal!"
        bree.say "You really mean that?!?"
        show angela happy
        angela.say "Of course I do, [hero.name]!"
        angela.say "I really want to marry you!"
        show angela normal
        bree.say "I was afraid with what happened to you..."
        bree.say "You know, before all of this?"
        "Angela shakes her head, dismissing my concerns."
        show angela happy
        angela.say "Don't you see, [hero.name]?"
        angela.say "That's why I want to do this with you."
        angela.say "I don't know how much of my last marriage was really me."
        angela.say "Or how much was stuff that somebody else put inside of my head."
        angela.say "But with you, I know that everything I feel is one hundred percent real!"
        show angela normal
        "I never thought of it like that before."
        "But what Angela's saying makes perfect sense."
        "And maybe later I'll be able to really appreciate what it means too."
        "But right now I'm too tied up with the moment to be able to think of anything else."
        $ angela.set_fiance()
    hide angela
    return

label angela_kiss_reaction_female:
    if angela.lesbian < MIN_LES_GIRL_SEX:
        $ angela.lesbian += 1
    return

label angela_ask_date_female:



    call angela_ask_date_alone_female from _call_angela_ask_date_alone_female
    return _return

label angela_ask_date_alone_female:
    bree.say "Erm...Angela?"
    bree.say "I've really enjoyed spending some time with you."
    bree.say "And I wondered...would you like to do it again?"
    bree.say "Like maybe go on an actual date with me?"
    if angela.love < 50 or angela.flags.nodate:
        "Angela smiles, but I can see that she's trying to be kind."
        "And when she shakes her head a little, I know what her answer is going to be."
        angela.say "That's sweet of you, [hero.name]."
        angela.say "And I'm flattered, really I am."
        angela.say "But I don't think we have that kind of a relationship - at least not yet."
        $ date_choice = False
    else:
        "Angela's face lights up at the mere mention of a date."
        "She nods eagerly, like she's been waiting for me to ask."
        angela.say "That's a great idea, [hero.name]!"
        angela.say "I'd love to go on a date with you!"
        $ date_choice = True
    return date_choice

label angela_greet:
    if renpy.has_label(f"angela_greet_dialogues_{hero.gender}") and not angela.flags.greeted:
        scene expression f"bg {game.room}"
        $ angela.flags.greeted = TemporaryFlag(True, 1)
        show angela
        $ result = randint(1, 3)
        if result == 1:
            angela.say "Hello, [hero.name]."
        elif result == 2:
            angela.say "Hi, [hero.name]."
        elif result == 3:
            angela.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                angela.say "Good morning [hero.name]."
            elif game.hour < 19:
                angela.say "Good afternoon [hero.name]."
            else:
                angela.say "Good evening [hero.name]."
        call expression f"angela_greet_dialogues_{hero.gender}" from _call_expression_386
        hide angela
    return

label angela_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Angela."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Angela."
        elif game.hour < 12:
            bree.say "Good morning Angela."
        elif game.hour < 19:
            bree.say "Good afternoon Angela."
        else:
            bree.say "Good evening Angela."
    return


label angela_pregnancy_congratulations:
    show angela happy
    "Angela gives me a knowing smile and nods."
    "And it's only then that I see her staring at my belly."
    "Instinctively my hand goes to shield it, a gesture I can't help."
    "And that's enough to confirm Angela's obvious suspicions."
    angela.say "Looks like congratulations are in order, [hero.name]!"
    angela.say "Somebody's going to be a mommy!"
    "Now it's my turn to smile and nod."
    "Angela's found me out, so there's no point denying it."
    bree.say "You got me, Angela!"
    bree.say "I guess you've already been through all of this, yeah?"
    bree.say "When you had [mike.name]?"
    show angela normal
    "Angela shakes her head at this."
    "And for a moment she looks a little sad."
    "But then she seems to shake off the feeling."
    "And she smiles again."
    angela.say "Of course I do, [hero.name]!"
    show angela happy
    angela.say "Of course I do..."
    $ angela.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
