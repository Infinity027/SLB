init python:
    Event(**{
    "name": "gaming_harem_event_01",
    "label": "gaming_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_11"),
        IsNotDone("bree_kat_threesome"),
        HeroTarget(IsGender("male")),
        PersonTarget(kat,
            IsActive(),
            MinStat("love", 50),
            MinStat("lesbian", 10),
            ),
        ],
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "gaming_harem_event_02",
    "label": "gaming_harem_event_02",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "conditions": [
        IsDone("gaming_harem_event_01"),
        IsNotDone("bree_kat_threesome"),
        GameTarget(
            Not(IsFlag("gaming_delay")),
            ),
        MinDateScore(90),
        HeroTarget(IsGender("male")),
        PersonTarget(kat,
            InHarem('gaming'),
            MinStat("love", 100),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "gaming_harem_event_04",
    "label": "gaming_harem_event_04",
    "priority": 500,
    "music": "music/roa_music/buddy.ogg",
    "duration": 4,
    "conditions": [
        IsTimeOfDay("evening"),
        IsDone("bree_kat_threesome"),
        GameTarget(
            Not(IsFlag("gaming_delay")),
            ),
        HeroTarget(IsGender("male"),
            HasRoomTag("home"),
            Not(OnDate()),
            ),
        PersonTarget(kat,
            Not(IsHidden()),
            InHarem('gaming'),
            ),
        PersonTarget(bree,
            IsActive(),
            InHarem('gaming'),
            ),
        ],
    "do_once": True,
    })


label gaming_harem_event_01:
    show kat normal
    "Kat fixes me with an intense stare, and she slowly tilts her head to one side as she does so."
    "The effect is pretty distracting, far more so than if she were just studying me casually."
    "So much so that it prompts me to speak up, even if only in the hope of making her stop it."
    mike.say "Kat..."
    mike.say "Is there something bothering you?"
    mike.say "Because you're staring a hole straight through me!"
    "Much to my disappointment, Kat doesn't instantly snap out of it."
    "Instead she keeps right on staring at me as she gives me an answer."
    kat.say "Hmm..."
    kat.say "I was just thinking, [hero.name]..."
    mike.say "And what was it that you were thinking about?"
    mike.say "Would you care to enlighten me?"
    "For a moment I actually think that Kat's going to say no."
    "But then she nods and begins to explain herself at last."
    kat.say "I was just thinking about you and [bree.name]."
    kat.say "You make pretty good partners when it comes to gaming."
    kat.say "So good in fact, that I was wondering if you're dating?"
    menu:
        "Yes, we are dating.":
            "I guess this is the point where we define the parameters of our relationship."
            "Sure, I'm really getting to like hanging out with Kat when I get the chance."
            "But I don't want to be guilty of making her think that we could become more."
            mike.say "Yeah, Kat..."
            mike.say "[bree.name] and I have been an item for a while now."
            mike.say "And I think things are really going well between us too."
            show kat sad
            kat.say "Oh..."
            kat.say "Okay..."
            kat.say "That's...that's great, I guess..."
            $ kat.love -= 2
            "Kat's reaction doesn't seem to match up with her words."
            "And I find myself wondering what I said that could have made it so."
            mike.say "What's up, Kat?"
            mike.say "Did I say something wrong?"
            mike.say "I didn't mean to brag about being in a relationship!"
            "Kat shakes her head, as if she doesn't want to talk about it."
            show kat sadsmile
            kat.say "No..."
            kat.say "It's fine, really..."
            kat.say "I was just curious, that's all."
            "I get the distinct impression that isn't all there is to it."
            "But I don't feel right pressing Kat for more details."
            "So I take the opportunity to change the subject."
            "Hoping that talking about something else will lighten the mood."
        "Nooooo...":
            "Urgh..."
            "Why did she have to ask me that?"
            "I don't want to have to admit that I'm seeing [bree.name]."
            "That would mean that I'd have to back off trying to get anywhere with Kat!"
            "So it looks like the only sensible thing to do is lie like there's no tomorrow."
            mike.say "What?"
            mike.say "[bree.name] and me?!?"
            mike.say "Nah, we're just really good friends, that's all."
            show kat annoyed
            "Kat frowns a little and narrows her eyes."
            "Like she doesn't quite buy it."
            kat.say "Are you sure?"
            kat.say "Because you look like a couple to me."
            show kat angry
            kat.say "She's always hanging off your arm and stuff."
            kat.say "Whispering into your ear and giggling away."
            kat.say "Hell, sometimes she even kisses you!"
            mike.say "I know, I know..."
            mike.say "I really should talk to her about that!"
            mike.say "Because I know how it looks."
            mike.say "But no, we really aren't dating - not at all."
            show kat annoyed
            $ kat.sub -= 2
            "Kat nods, maybe a little more convinced than she was before."
            "But still with a lingering air of scepticism about her."
            kat.say "Okay, [hero.name]..."
            show kat normal
            kat.say "If that's how you say it is, then that's how it is."
        "Yes, but she's not the only one.":
            mike.say "Yeah, Kat..."
            mike.say "[bree.name] and I have been an item for a while now."
            mike.say "And I think things are really going well between us too."
            show kat sad
            kat.say "Oh..."
            kat.say "Okay..."
            kat.say "That's...that's great, I guess..."
            "Kat's reaction doesn't seem to match up with her words."
            "And I quickly realise she was hoping for a very different answer."
            "Which isn't something that discourages me."
            "In fact it does quite the opposite."
            mike.say "But I should tell you, Kat..."
            mike.say "[bree.name] and I have an open relationship."
            show kat shocked
            "Suddenly Kat's interest is piqued."
            show kat at center, zoomAt (1.5, (640, 1040)), vshake
            "And she leans in close, desperate to hear more."
            kat.say "Oh my god..."
            kat.say "Are you serious?"
            kat.say "You see other people too?!?"
            mike.say "Oh yeah..."
            mike.say "We're totally cool with that."
            mike.say "[bree.name] and I believe in sharing the love."
            mike.say "And there's always enough to go round."
            mike.say "Only don't go mentioning to [bree.name] that I told you."
            mike.say "She likes to keep it a secret, okay?"
            show kat shy blush
            "Kat nods, looking more thoughtful than ever."
            kat.say "Wow..."
            $ kat.sub += 2
            $ Harem.join_by_name("gaming", "kat")
            kat.say "That's given me a lot to think about!"
            "I smile as I wait for her to say more."
            "Of course I'm hoping she'll say she wants to share some loving with me!"
            "But I'm frustrated to find that Kat says nothing of the sort."
            "So all I can do is nod and smile, while I will her to ask the question."
            "It doesn't seem to work though, and she soon changes the subject."
            "Which leaves me feeling more than a little frustrated."
            $ game.flags.gaming_delay = TemporaryFlag(True, 1)
    return

label gaming_harem_event_02:
    show kat normal
    "Kat and I are hanging out together, doing nothing in particular."
    show kat happy
    "Just kind of enjoying each other's company and talking about whatever comes to mind."
    "You know, the way you do when you're just starting to develop a new friendship?"
    show kat normal
    "In fact I can't really remember exactly what we were talking about when we started."
    "And I certainly have no idea of just where the conversation is supposed to be going."
    show kat smile
    "So I'm not really paying much attention when Kat drops a casual line into the discussion."
    "At least it sounds like a throwaway line to me."
    show kat shy
    kat.say "I really wanted to tell you something, [hero.name]."
    mike.say "Oh yeah?"
    mike.say "What's that?"
    kat.say "Well..."
    kat.say "You might think that I've got a kind of rivalry going with [bree.name]..."
    show kat smile
    kat.say "But the truth is, I really like her!"
    "I kind of combine a nonchalant nod and a casual shrug."
    "Trying not to sound too smug as I respond."
    mike.say "Heh..."
    mike.say "That's not so strange, Kat..."
    mike.say "[bree.name]'s really cool when you get to know her."
    mike.say "I'm not surprised that you like her."
    show kat shy blush at startle
    "Kat kind of coughs a little and shakes her head."
    "And I can see that her cheeks are flushing too."
    "Almost like she's getting flustered about something."
    kat.say "No..."
    kat.say "You don't understand..."
    show kat smile
    kat.say "I mean I REALLY like [bree.name]!"
    "I stare at Kat for a moment."
    "Just long enough for realisation to dawn on me."
    mike.say "You..."
    mike.say "Oh..."
    show kat shy
    mike.say "OH!"
    mike.say "You mean that..."
    show kat angry
    kat.say "If you can't say it, then I will!"
    kat.say "Yes, I have a crush on [bree.name]."
    kat.say "And just to be clear, I mean that I find her sexually attractive."
    kat.say "Not that I want to squash her under a huge rock or something like that!"
    "Now I'm the one stammering and getting flustered."
    "But I do the best I can to get myself back under control again."
    "After all, I'm a thoroughly modern guy."
    "I can handle the fact that a girl likes girls as well as guys."
    mike.say "No worries, Kat..."
    mike.say "I'm like, totally cool with that."
    mike.say "So..."
    mike.say "You're into what, exactly?"
    mike.say "Admiring [bree.name] from afar?"
    show kat shy -blush
    kat.say "Not exactly, [hero.name]..."
    kat.say "Look, I'm not trying to muscle in on your relationship here."
    show kat blush
    kat.say "So I was thinking..."
    kat.say "What would you say to the idea of a threesome?"
    kat.say "Me, you and [bree.name]?"
    menu:
        "Let's do it!":
            "I can't keep myself from grinning."
            "And I nod my head eagerly."
            "Perhaps a little too eagerly, as it turns out."
            show kat defiant
            "Because I see Kat mirroring my smile and nod too."
            "Which means she knows how keen I am on the idea."
            kat.say "Like the sound of that, do you?"
            mike.say "You bet I do!"
            mike.say "I...I mean..."
            mike.say "It could be something I'd be interested in."
            show kat smile -blush
            kat.say "Oh come on, [hero.name]..."
            kat.say "You're practically salivating at the thought of it!"
            "It doesn't seem like Kat's going to fall for my attempt to sound reserved."
            "So I drop all pretence and just decide to be honest."
            mike.say "Of course I want to do it, Kat."
            mike.say "And I'm pretty sure [bree.name] will be into it too."
            mike.say "I just need a chance to talk to her about it."
            show kat happy
            "Kat nods, happy to see her plan coming together."
            kat.say "Okay, [hero.name]..."
            show kat smile
            kat.say "But don't take your sweet time over it, yeah?"
            kat.say "Right now I'm totally up for it, raring to go."
            show kat normal
            kat.say "The longer I have to wait, the greater the chance I might go cold on it."
            mike.say "Sure, sure..."
            mike.say "Look, Kat..."
            mike.say "Here's our address."
            mike.say "Come round any Saturday that suits you."
            mike.say "That's when Sasha will be at band practice."
            mike.say "And I promise that I'll have [bree.name] on board by then."
            show kat smile
            "Kat nods, and we do the best we can to change the subject."
            "But that proves to be easier said than done."
            "As now the genie's well and truly out of the bottle."
            "My head's full of the possibilities of the threesome."
            "And I'm willing to bet Kat's is too."
            $ game.flags.gaming_delay = TemporaryFlag(True, 1)
        "It is appealing, but...":
            "I can't keep myself from frowning."
            "And so I shake my head too."
            "Hoping that it won't look like I'm turned-off by the idea."
            "Because that's not why I'm choosing to say no."
            "The idea of a threesome is very appealing."
            "And with Kat, even more so."
            "But not appealing enough to make me risk what I have with [bree.name]."
            mike.say "I don't think so, Kat."
            show kat surprised -blush
            kat.say "Huh?"
            show kat shocked
            kat.say "You have to be kidding?!?"
            kat.say "I thought every man was dying to have a threesome!"
            kat.say "Especially when it's two girls and one guy!"
            "I hold up a hand to stop Kat."
            show kat normal
            "Before she sells the idea to me so hard that I can't possibly say no."
            "Because it's already pretty hard to do that as things stand!"
            mike.say "Look, Kat..."
            mike.say "I'm flattered, I really am..."
            mike.say "And if I were single, I'd be all over that offer."
            mike.say "But what I have going on with [bree.name]..."
            mike.say "It's really special, you know?"
            mike.say "And the last thing I want is to mess it all up."
            show kat annoyed
            "Kat looks disappointed."
            "But apparently she's willing to have one last try."
            kat.say "You really think she'd freak out at the idea?"
            show kat normal
            kat.say "No chance she's more adventurous than you think?"
            kat.say "That you might be selling her short?"
            mike.say "I don't know, Kat."
            mike.say "But I'm not going to gamble my relationship on that chance."
            $ Harem.leave_by_name("gaming", "kat")
            show kat sad
            "Kat sighs and nods her head."
            kat.say "Aah..."
            show kat sadsmile
            kat.say "I guess I should be complimenting you on your willpower."
            kat.say "I don't think most guys would have needed much persuading..."
            "Both of us are obviously eager to drop the subject."
            "But once it's been mentioned, we can't just pretend it never happened."
            "So the rest of the conversation is pretty awkward."
            "And I think we're both relieved when it's time to part ways."
    return



label gaming_harem_event_04:
    scene bg livingroom
    show bree casual normal
    with fade
    "[bree.name] and I have been running around the house for what feels like ages, trying to get everything sorted."
    "We've been making sure we have an adequate supply of snacks and drinks, enough to last three people all night."
    "Then we've checked and double checked that the Z-Box and all of the peripherals for it are in perfect working order."
    "And, perhaps most importantly of all, we've ushered Sasha out of the door and locked it behind her."
    "But not before extracting assurances from her that she won't be back home until at least after midnight."
    show bree casual normal at center, zoomAt(1.25, (640, 880)) with fade
    "Once all of that is done, [bree.name] and I find ourselves standing, staring at each other in the livingroom."
    mike.say "Well?"
    mike.say "Is that it?"
    mike.say "Did we cover all the bases?"
    show bree hesitating
    "[bree.name] looks stressed and more than a little frazzled right how."
    "And I guess I'd see the same thing on my own face if I looked in the mirror."
    "But she still manages to nod her head in response to the question."
    show bree talkative
    bree.say "I think so..."
    bree.say "At least I can't remember anything else."
    bree.say "But then my brain feels like tofu right now!"
    show bree sadsmile
    "I'm about to say something that I hope will help to soothe [bree.name]'s nerves."
    play sound door_knock
    "But then there's the sound of a knock at the door."
    "As one, we turn to look in the direction of the noise."
    mike.say "That has to be her, right?"
    show bree talkative
    bree.say "Well it can't be Sasha, because she has keys."
    show bree normal
    mike.say "Then it's got to be Kat!"
    "[bree.name] and I hurry over to the door, both trying to open it at once."
    "Which means that the first thing the person on the other side sees is a mess of limbs."
    "Then they're treated to our heads poking around the side, like we're fighting for space."
    scene bg black
    pause 0.1
    scene bg house
    show kat casual annoyed
    with wiperight
    kat.say "Erm..."
    kat.say "Hi, guys..."
    kat.say "Does this mean you're glad to see me?"
    kat.say "Because I'm kinda finding it hard to tell!"
    show kat timid
    "[bree.name] and I get into a little scuffle as she says this."
    "One that results in me taking an elbow to the stomach."
    "I can't tell if it's deliberate or not, but it means that I take a step back."
    scene bg livingroom
    show bree casual normal at center, zoomAt(1.25, (640, 880))
    with fade
    "And [bree.name] uses the chance to open the door fully, letting Kat into the house."
    show bree happy
    bree.say "Hey, Kat..."
    bree.say "Come on in!"
    show bree normal at center, zoomAt(1.25, (440, 880))
    show kat casual shocked at center, zoomAt(1.25, (840, 880))
    with easeinright
    kat.say "Oh..."
    kat.say "Are you okay, [hero.name]?"
    show kat stuned
    "I manage to hold up a hand and wave it at Kat, but I'm still kind of bent over double."
    show kat normal
    mike.say "Fine...I'm fine..."
    mike.say "Just catching my breath..."
    mike.say "That's all!"
    show bree smile at center, zoomAt(1.25, (480, 880)) with ease
    "[bree.name] distracts Kat from my plight by taking her arm."
    "And then she starts to lead the other girl towards the sitting room."
    show bree happy
    bree.say "Never mind him, Kat..."
    bree.say "Let me show you some of the games we've got lined up for tonight."
    show bree normal
    "I follow on their heels as they walk into the sitting room."
    show bree casual normal at center, zoomAt(1.5, (340, 1040))
    show kat casual normal at center, zoomAt(1.5, (940, 1040))
    with fade
    "And I'm pleased to notice Kat still looking back at me."
    "But by the time we're all in there, I've pretty much recovered."
    "So I can stand up and make an effort to get back into the conversation."
    show kat enthusiastic
    kat.say "Wow..."
    kat.say "This all looks so great."
    show kat happy
    kat.say "You guys didn't have to go to this much effort just for me!"
    show kat normal
    mike.say "Don't be silly, Kat..."
    mike.say "We take gaming nights seriously in this house."
    mike.say "So you'd better get used to this."
    show bree talkative
    bree.say "Oh, and we don't hold back just because you're new either."
    bree.say "So I hope you brought your best game along tonight, Kat?"
    show bree normal
    "I think [bree.name] was expecting Kat to be a little surprised by the challenge."
    "Either that or to get her competitive spirit really fired-up."
    show kat smile
    "But instead, I see a knowing smile spread across Kat's face."
    show kat defiant
    kat.say "Oh..."
    kat.say "Is that so?"
    show kat normal
    "Until now I was just watching the interaction between the two of them."
    "Wanting to see where the conversation was going."
    "But now I can detect a counter-challenge in Kat's words."
    "And for some reason it makes me want to back [bree.name] up."
    mike.say "She's telling the truth, Kat..."
    mike.say "We don't take any prisoners here."
    mike.say "And neither of us is gonna go easy on you!"
    show kat busted
    "Kat raises her eyebrows at this."
    show kat defiant
    kat.say "Big talk, [hero.name]."
    kat.say "How about we see if you can back it up?"
    kat.say "How about we make a little wager?"
    show kat normal
    show bree happy
    "[bree.name] and I exchange a glance, a shrug and a nod."
    show bree talkative
    bree.say "Okay, Kat..."
    bree.say "That'd make things more interesting for sure."
    show bree normal
    mike.say "Yeah, Kat..."
    mike.say "What did you have in mind?"
    show kat smile
    "Kat's smile gets wider still, like a Kat creeping up on its prey."
    "And I can't help getting the feeling she has us right where she wants us right now."
    show kat talkative
    kat.say "Just this..."
    kat.say "We keep score tonight, okay?"
    show kat whinge
    kat.say "And whoever comes last has to make whoever comes first...cum."
    kat.say "You know, really put your money where your mouth is!"
    show kat normal
    "I'm about to ask [bree.name] what she thinks of the terms Kat's offering."
    "But even as I turn my head, she's already started speaking."
    show bree talkative
    bree.say "Okay, Kat..."
    bree.say "You're on - but I want to add a stipulation."
    bree.say "We're playing the games with our hands, right?"
    bree.say "But the loser can't use them for the forfeit, okay?"
    show bree normal
    show kat smile
    "My head snaps back to Kat, who nods eagerly."
    show kat talkative
    kat.say "Agreed!"
    kat.say "What about you, [hero.name]?"
    kat.say "I take it you're in?"
    show kat normal
    "It'd have been nice to get a word in somewhere along the line."
    "But really, what have I got to lose in all of this?"
    "Either I win and get one of the girls to pleasure me."
    "Or I lose and I get to explore one of them with my tongue."
    "Hell, even if I come in the middle, I get to watch them go to town on each other!"
    mike.say "Sure thing, Kat..."
    mike.say "I'm totally up for that."
    show bree at startle
    show kat at startle
    "Everyone exchanges nods and handshakes to seal the deal."
    "Then we settle down for a night of hardcore gaming."
    "With a valuable prize at stake and a lot of fun promised to the winner."
    show play console bree with fade
    "What follows is a good few hours of everyone trying to beat everyone else."
    show play console kat with fade
    "At times [bree.name], Kat and myself trade first, second and last place."
    hide play console
    show play console kat breemc nomike
    with fade
    "But once it's all over, there's one clear winner."
    "And one clear loser too."

    $ renpy.dynamic("winner", "winners", "loser", "losers", "max_score", "min_score", "scores")
    $ scores = {"Mike": hero.knowledge, "[bree.name]": bree.sub, "Kat": kat.sub}
    if hero.has_skill("video_games"):
        $ winner = "Mike"
        $ scores.pop("Mike")
        $ min_score = min(scores.values())
        $ losers = [k for k,v in scores.items() if v == min_score]
        $ loser = randchoice(losers)
    else:
        $ max_score = max(scores.values())
        $ min_score = min(scores.values())
        $ winners = [k for k,v in scores.items() if v == max_score]
        $ winner = randchoice(winners)
        $ losers = [k for k,v in scores.items() if v == min_score]
        $ loser = randchoice(losers)
    if winner == "Mike" and loser == "Kat":
        call gaming_harem_kat_blowjob from _call_gaming_harem_kat_blowjob
        $ kat.sub += 1
        $ bree.love += 2
    elif winner == "Mike" and loser == "[bree.name]":
        call gaming_harem_bree_blowjob from _call_gaming_harem_bree_blowjob
        $ bree.sub += 1
        $ kat.love += 2
    elif winner == "[bree.name]" and loser == "Mike":
        call gaming_harem_bree_cunnilingus from _call_gaming_harem_bree_cunnilingus
        $ bree.love += 2
    elif winner == "[bree.name]" and loser == "Kat":
        call gaming_harem_kat_cunnilingus_bree from _call_gaming_harem_kat_cunnilingus_bree
        $ kat.sub += 1
    elif winner == "Kat" and loser == "Mike":
        call gaming_harem_kat_cunnilingus from _call_gaming_harem_kat_cunnilingus
        $ kat.love += 2
    elif winner == "Kat" and loser == "[bree.name]":
        call gaming_harem_bree_cunnilingus_kat from _call_gaming_harem_bree_cunnilingus_kat
        $ bree.sub += 1
    $ hero.replace_activity()
    $ game.room = "livingroom"
    $ game.flags.gaming_delay = TemporaryFlag(True, 1)
    return

label gaming_harem_cumpetition_intro(appointment=None):
    scene bg livingroom
    show bree casual normal at center, zoomAt(1.5, (340, 1040))
    show kat casual normal at center, zoomAt(1.5, (940, 1040))
    with fade
    "Once again, the house is set up for another session of game cumpetition."
    "We start by the usual handshakes and cheering small talk."
    show play console bree with fade
    "What follows is a good few hours of everyone trying to beat everyone else."
    show play console kat with fade
    "At times [bree.name], Kat and myself trade first, second and last place."
    hide play console
    show play console kat breemc nomike
    with fade
    "But as hours pass, an odd thought hits me."
    "It seems that we're adapting our playstyle to achieve one specific reward."
    menu:
        "I win, Kat loses":
            call gaming_harem_kat_blowjob from _call_gaming_harem_kat_blowjob_1
        "I win, Bree loses":
            call gaming_harem_bree_blowjob from _call_gaming_harem_bree_blowjob_1
        "Kat win, I lose":
            call gaming_harem_kat_cunnilingus from _call_gaming_harem_kat_cunnilingus_1
        "Bree win, I lose":
            call gaming_harem_bree_cunnilingus from _call_gaming_harem_bree_cunnilingus_1
        "Kat win, Bree loses":
            call gaming_harem_bree_cunnilingus_kat from _call_gaming_harem_bree_cunnilingus_kat_1
        "Bree win, Kat loses":
            call gaming_harem_kat_cunnilingus_bree from _call_gaming_harem_kat_cunnilingus_bree_1
    return

label gaming_harem_kat_blowjob:
    scene bg livingroom
    show play console kat
    with fade
    "Putting my joypad down, I turn to Kat with a smile on my face."
    hide play console
    show kat casual upset at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Looks like I came out on top, Kat..."
    mike.say "And you..."
    "Kat cuts me off before I can actually say the words."
    show kat angry blush
    kat.say "Yeah, yeah..."
    kat.say "I know where I finished."
    kat.say "And I know what it means too!"
    show kat sadsmile
    "Kat's already dropped her own joypad and she's turning towards me."
    "I'm sitting on the sofa, but she's crawling across the floor."
    "And she's looking up at me as she keeps getting closer."
    mike.say "And..."
    mike.say "And you're okay with that?"
    "By now Kat's made it all the way to me."
    "And she's propping herself up on my knees."
    show kat talkative
    kat.say "I was the one that suggested the bet, wasn't I?"
    kat.say "So it'd be pretty shitty of me to welch on it..."
    show kat shy
    "Kat holds my eye as she's saying all of this."
    "But at the same time she's reaching out with her hands."
    "And I can feel her unzipping my flies a moment later."
    scene bg black
    show kat blowjob handjob livingroom
    with fade
    "Then her eyes go down as she finds my cock and pulls it out."
    "It's instantly obvious that I'm already turned-on by Kat's actions."
    "Because my cock's half erect when she starts handling it."
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    pause 0.35
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    "And it only takes a little more stroking to get it the rest of the way."
    show kat blowjob eyes_closed
    "Kat doesn't waste any more time, closing her eyes and leaning over it."
    show kat blowjob mouth_lick
    "But as her lips close around the head, I see [bree.name] watching intently too."
    "That only serves to make the whole situation even more intense."
    "As I can practically feel the sexual tension [bree.name]'s giving out right now."
    show kat blowjob mouth_lick
    pause 0.15
    show kat blowjob tongue2
    pause 0.15
    show kat blowjob tongue3
    pause 0.15
    show kat blowjob tongue1
    "Kat starts out slow, using only her lips and the tip of her tongue."
    "But that doesn't last very long."
    show kat blowjob -handjob
    "As she soon seems to get a taste for what she's doing."
    "Her tongue wraps around the head then licks around the shaft."
    show kat blowjob blow
    "Her lips suck and caress wherever they touch."
    "Kat even brings her teeth into play, making me flinch and twitch."
    "All in all, she handles my cock with expert skill."
    "Far better than she did her joypad earlier in the night."
    show kat blowjob cum with hpunch
    "And when I finally shoot my load into her mouth, Kat gulps down every last drop."
    "Making me wonder if she might have thrown the games she played on purpose."
    return

label gaming_harem_bree_blowjob:
    scene bg livingroom
    show play console bree
    with fade
    "Putting my joypad down, I turn to [bree.name] with a smile on my face."
    hide play console
    show bree casual annoyed at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Looks like I came out on top, [bree.name]..."
    mike.say "And you..."
    show bree sadsmile blush
    "[bree.name] cuts me off before I can actually say the words."
    show bree evil
    bree.say "Yeah, yeah..."
    bree.say "I know where I finished."
    bree.say "And I know what it means too!"
    show bree sadsmile
    "[bree.name]'s already dropped her own joypad and she's turning towards me."
    "I'm sitting on the sofa, but she's crawling across the floor."
    "And she's looking up at me as she keeps getting closer."
    mike.say "And..."
    mike.say "And you're okay with that?"
    "By now [bree.name]'s made it all the way to me."
    "And she's propping herself up on my knees."
    show bree talkative
    bree.say "I agreed to the bet too, didn't I?"
    bree.say "So it'd be pretty shitty of me to welch on it..."
    show bree normal
    "[bree.name] holds my eye as she's saying all of this."
    "But at the same time she's reaching out with her hands."
    "And I can feel her unzipping my flies a moment later."
    scene bg black
    show bree cinema bj bree livingroom
    with fade
    "Then her eyes go down as she finds my cock and pulls it out."
    "It's instantly obvious that I'm already turned-on by [bree.name]'s actions."
    "Because my cock's half erect when she starts handling it."
    "And it only takes a little more stroking to get it the rest of the way."
    "[bree.name] doesn't waste any more time, closing her eyes and leaning over it."
    "But as her lips close around the head, I see Kat watching intently too."
    "That only serves to make the whole situation even more intense."
    "As I can practically feel the sexual tension Kat's giving out right now."
    "[bree.name] starts out slow, using only her lips and the tip of her tongue."
    "But that doesn't last very long."
    "As she soon seems to get a taste for what she's doing."
    "Her tongue wraps around the head then licks around the shaft."
    "Her lips suck and caress wherever they touch."
    "[bree.name] even brings her teeth into play, making me flinch and twitch."
    "All in all, she handles my cock with expert skill."
    "Far better than she did her joypad earlier in the night."
    show bree cinema bj cum with vpunch
    "And when I finally shoot my load into her mouth, [bree.name] gulps down every last drop."
    "Making me wonder if she might have thrown the games she played on purpose."
    return

label gaming_harem_bree_cunnilingus:
    scene bg livingroom
    show play console bree
    with fade
    "I put down my joypad and turn to face [bree.name], who's already got a smile on her face."
    hide play console
    show bree casual smile at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Erm..."
    mike.say "I gotta say..."
    mike.say "That did not turn out how I'd hoped!"
    show bree talkative
    bree.say "A bet's a bet, [hero.name]..."
    bree.say "You're not going to try to get out of it, are you?"
    show bree normal
    "I shake my head and let out a chuckle at this."
    mike.say "Oh no, [bree.name]..."
    mike.say "No way!"
    show bree smile
    "[bree.name] nods, her smile growing wider still."
    "I watch as she beckons me over to her with one finger."
    "And at the same time, she slides her thighs apart too."
    "Like I already said, I don't see this as any kind of punishment."
    "More like an enjoyable forfeit, if anything."
    "So I make a point of not getting up as I move towards [bree.name]."
    "Instead I choose to crawl on all fours, acknowledging her victory over me."
    "Only when I make it to where she's sitting do I raise myself up."
    scene bg black
    show bree cunnilingus bree livingroom
    with fade
    "And even then only enough to put my head between her thighs."
    kat.say "Make sure you do a good job, [hero.name]!"
    "The sound of Kat's voice makes me glance up for a moment."
    "And I see that she's come over to watch as well."
    "Now that I have an audience, I can feel the pressure to perform."
    "But rather than putting me off, it makes me all the more determined."
    "Lowering my head, I close my eyes and push out my tongue."
    show bree cunnilingus down
    pause 0.25
    show bree cunnilingus middle
    pause 0.25
    show bree cunnilingus up
    "And it doesn't take me long to find what I'm looking for."
    "The bittersweet tang of [bree.name]'s pussy hits the tip a moment later."
    "And the taste of it spurs me on to do what I need to do."
    show bree cunnilingus down
    pause 0.25
    show bree cunnilingus middle
    pause 0.25
    show bree cunnilingus up
    "Turning my head a little, I push my tongue into the folds of [bree.name]'s pussy."
    show bree cunnilingus down pleasure
    pause 0.25
    show bree cunnilingus middle
    pause 0.25
    show bree cunnilingus up
    "Exploring them I slowly begin to work my way inwards, towards her actual lips."
    "I'm not interested in taking my time here, just in pleasuring her."
    "And the effects are instant, as I feel [bree.name] start to twitch in her seat."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up
    "These motions only serve to push me to go further and faster."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up
    "And soon enough I'm pushing the tip of my tongue as deep as it can go."
    show bree cunnilingus down shake
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "[bree.name]'s really quaking and quivering by now, her thighs squeezing my head."
    show bree cunnilingus middle pleasure
    pause 0.15
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "But I don't let that stop me, and I push on further still."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "In fact I don't stop until I can hear her moaning like crazy."
    show bree cunnilingus livingroom ahegao with vpunch
    "And even then it's Kat who pulls me out of there."
    "My breath coming in gasps as [bree.name] curls into a helpless ball"
    return

label gaming_harem_kat_cunnilingus_bree:
    scene bg livingroom
    show play console kat breemc nomike
    with fade
    "I put down my joypad with a growing sense of excitement."
    hide play console
    show kat casual shy at center, zoomAt(1.5, (440, 1040))
    with fade
    "Then I look over to where Kat's sitting, noting how she's staring at the ground."
    show bree casual smile at center, zoomAt(1.5, (840, 1040)) with easeinright
    "Next I turn my gaze to [bree.name], who's beginning to smile like the cat that got the cream."
    mike.say "So..."
    mike.say "I make that as me finishing second."
    mike.say "[bree.name] coming first..."
    mike.say "And Kat coming in last!"
    show kat sadsmile
    "Kat nods her head, as I say all of this."
    show kat talkative blush
    kat.say "Okay, okay..."
    kat.say "I know where I finished."
    kat.say "And I know what it means too!"
    show kat shy
    mike.say "And..."
    mike.say "And you're okay with that?"
    hide kat with easeoutbottom
    "As if to answer my question, Kat slides out of her seat and onto the ground."
    "And I watch as she crawls on all fours over to where [bree.name]'s sitting."
    show bree surprised blush
    bree.say "Oh wow..."
    show bree happy
    bree.say "Looks like I won big time tonight!"
    show bree smile
    "[bree.name] spreads her thighs apart as Kat lifts herself up."
    scene bg black
    show kat cunnilingus bree livingroom
    with fade
    "And as her head goes down between [bree.name]'s thighs, I lose sight of it."
    "That alone is enough to see me leap up and hurry over there."
    "And I strain to get the best view possible as Kat closes in on [bree.name]'s pussy."
    "I can't see as much as I'd like to, but I can still see a lot of glistening pink."
    show kat cunnilingus bree tongue blush
    "It's only when I see Kat's tongue moving that I can tell what's what."
    "From then on I can enjoy the chance to watch the whole thing play out."
    "That and hear the effects that Kat's efforts are having on [bree.name]."
    show kat cunnilingus bree pleasure
    "Kat's tongue seems to move ever faster and dip ever deeper."
    "And all the time that she's at it, [bree.name]'s moans become louder still."
    "I risk a glance upwards, seeing [bree.name]'s head tossing and turning."
    "And I note that her hands are almost tearing at the sofa too!"
    "The whole thing is making me feel hot under the collar as well."
    show kat cunnilingus bree orgasm squirt fx with vpunch
    "My heart beating faster as [bree.name]'s worked towards her climax."
    with vpunch
    "And when it finally does come, [bree.name] wails with sheer pleasure."
    return

label gaming_harem_kat_cunnilingus:
    scene bg livingroom
    show play console kat
    with fade
    "I put down my joypad and turn to face Kat, who's already got a smile on her face."
    hide play console
    show kat casual upset at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Erm..."
    mike.say "I gotta say..."
    mike.say "That did not turn out how I'd hoped!"
    show kat talkative blush
    kat.say "A bet's a bet, [hero.name]..."
    kat.say "You're not going to try to get out of it, are you?"
    show kat shy
    "I shake my head and let out a chuckle at this."
    mike.say "Oh no, Kat..."
    mike.say "No way!"
    show kat smile
    "Kat nods, her smile growing wider still."
    "I watch as she beckons me over to her with one finger."
    "And at the same time, she slides her thighs apart too."
    "Like I already said, I don't see this as any kind of punishment."
    "More like an enjoyable forfeit, if anything."
    "So I make a point of not getting up as I move towards Kat."
    "Instead I choose to crawl on all fours, acknowledging her victory over me."
    "Only when I make it to where she's sitting do I raise myself up."
    scene bg black
    show kat cunnilingus livingroom mike
    with fade
    "And even then only enough to put my head between her thighs."
    bree.say "Make sure you do a good job, [hero.name]!"
    "The sound of [bree.name]'s voice makes me glance up for a moment."
    "And I see that she's come over to watch as well."
    "Now that I have an audience, I can feel the pressure to perform."
    "But rather than putting me off, it makes me all the more determined."
    "Lowering my head, I close my eyes and push out my tongue."
    "And it doesn't take me long to find what I'm looking for."
    "The bittersweet tang of Kat's pussy hits the tip a moment later."
    "And the taste of it spurs me on to do what I need to do."
    show kat cunnilingus eyes_close
    "Turning my head a little, I push my tongue into the folds of Kat's pussy."
    "Exploring them I slowly begin to work my way inwards, towards her actual lips."
    "I'm not interested in taking my time here, just in pleasuring her."
    "And the effects are instant, as I feel Kat start to twitch in her seat."
    show kat cunnilingus mouth_close
    "These motions only serve to push me to go further and faster."
    "And soon enough I'm pushing the tip of my tongue as deep as it can go."
    show kat cunnilingus eyes_open mouth_hurt
    "Kat's really quaking and quivering by now, her thighs squeezing my head."
    "But I don't let that stop me, and I push on further still."
    "In fact I don't stop until I can hear her moaning like crazy."
    show kat cunnilingus eyes_up mouth_open with vpunch
    "And even then it's [bree.name] who pulls me out of there."
    "My breath coming in gasps as Kat curls into a helpless ball"
    return

label gaming_harem_bree_cunnilingus_kat:
    scene bg livingroom
    show play console kat breemc nomike
    with fade
    "I put down my joypad with a growing sense of excitement."
    hide play console
    show bree casual smile at center, zoomAt(1.5, (440, 1040))
    with fade
    "Then I look over to where [bree.name]'s sitting, noting how she's staring at the ground."
    show kat casual smile at center, zoomAt(1.5, (840, 1040)) with easeinright
    "Next I turn my gaze to Kat, who's beginning to smile like the cat that got the cream."
    mike.say "So..."
    mike.say "I make that as me finishing second."
    mike.say "Kat coming first..."
    mike.say "And [bree.name] coming in last!"
    show bree sadsmile blush
    "[bree.name] nods her head, as I say all of this."
    show bree talkative
    bree.say "Okay, okay..."
    bree.say "I know where I finished."
    bree.say "And I know what it means too!"
    show bree normal
    mike.say "And..."
    mike.say "And you're okay with that?"
    hide bree with easeoutbottom
    "As if to answer my question, [bree.name] slides out of her seat and onto the ground."
    "And I watch as she crawls on all fours over to where [bree.name]'s sitting."
    show kat surprised blush
    kat.say "Oh wow..."
    show kat whinge
    kat.say "Looks like I won big time tonight!"
    "[bree.name] spreads her thighs apart as [bree.name] lifts herself up."
    scene bg black
    show bree cunnilingus kat livingroom lookback
    with fade
    "And as her head goes down between Kat's thighs, I lose sight of it."
    "That alone is enough to see me leap up and hurry over there."
    "And I strain to get the best view possible as [bree.name] closes in on Kat's pussy."
    show bree cunnilingus kat closeup
    "I can't see as much as I'd like to, but I can still see a lot of glistening pink."
    "It's only when I see [bree.name]'s tongue moving that I can tell what's what."
    "From then on I can enjoy the chance to watch the whole thing play out."
    "That and hear the effects that [bree.name]'s efforts are having on Kat."
    "[bree.name]'s tongue seems to move ever faster and dip ever deeper."
    show bree cunnilingus kat pleasure lookfront breath
    "And all the time that she's at it, Kat's moans become louder still."
    show bree cunnilingus kat -closeup
    "I risk a glance upwards, seeing Kat's head tossing and turning."
    "And I note that her hands are almost tearing at the sofa too!"
    "The whole thing is making me feel hot under the collar as well."
    show bree cunnilingus kat ahegao squirt with hpunch
    "My heart beating faster as [bree.name]'s worked towards her climax."
    with hpunch
    "And when it finally does come, Kat wails with sheer pleasure."
    return

label bree_kat_propose_male:
    show kat normal at center, zoomAt(1.25, (440, 880))
    show bree normal at center, zoomAt(1.25, (840, 880))
    with fade
    "I've been waiting for the chance to get [bree.name] and Kat together in the same place."
    "And not just because I want to spend as much time with them as I possibly can."
    "But rather on account of the fact that I've got an ulterior motive today."
    "That and two very small items in my pocket that feel like each weighs a ton!"
    mike.say "So..."
    mike.say "I'm really glad that we could all get together today."
    mike.say "Because I kind of have something that I wanted to ask you both."
    show bree smile
    show kat smile
    "As soon as the words are out of my mouth, I see a change in [bree.name] and Kat."
    "Their expressions become knowing, even amused at what I'm saying."
    show bree evil
    show kat shy
    "And they exchange a look that seems to mean they're both thinking the same thing."
    "But I have no hope of telling what that is myself."
    show bree talkative
    bree.say "Oh really?"
    bree.say "Something you wanted to ask us?"
    show bree normal
    show kat talkative
    kat.say "The both of us?"
    kat.say "Hmm..."
    kat.say "I wonder what that could be?"
    show kat normal
    show bree talkative
    bree.say "I couldn't even begin to guess!"
    show kat happy
    show bree happy
    "[bree.name] and Kat are giggling away by now, even nudging me with their elbows."
    "At first I'm totally baffled as to what they're trying to do."
    "But then it hits me like a slap in the face."
    mike.say "Wait a minute..."
    mike.say "You think that..."
    mike.say "That I'm going to ask you to do something kinky?!?"
    show bree stuned
    show kat stuned
    "Now it's [bree.name] and Kat's turn to look confused."
    show bree surprised
    bree.say "Wait..."
    bree.say "You mean you're not?"
    show bree stuned
    show kat surprised
    kat.say "Really, [hero.name]?"
    show kat shocked
    kat.say "Because I was totally getting into the idea!"
    show kat stuned
    "For a moment I have no idea how to respond."
    "But then it hits me that this might be the perfect opportunity for what I have in mind."
    "So I stop arguing, and instead I drop down onto one knee in front of [bree.name]and Kat."
    show bree surprised
    bree.say "What are you..."
    show bree stuned
    show kat shocked
    kat.say "Huh..."
    kat.say "Is he..."
    show kat stuned
    show bree surprised
    bree.say "Oh my god!"
    show bree stuned
    "They're saying all of this as I reach into my pocket and pull out the boxes."
    "But they soon realise what's happening when I pop them open."
    mike.say "[bree.name]..."
    mike.say "Kat..."
    mike.say "Will you marry me?"
    "I'm smiling up at the pair of them as I say this."
    "Waiting to hear what their answers will be."
    if bree.love >= 195 and kat.love >= 195:

        show bree happy
        "[bree.name] instantly starts flapping her hands in the air."
        "Obviously delighted at the offer I'm making."
        bree.say "Of course I will, [hero.name]…"
        bree.say "I'd love to marry you!"
        show bree normal
        "Kat takes a few seconds longer to realise what's happening."
        "But when she does, she seems to be just as elated as [bree.name]."
        show kat surprised
        kat.say "Oh shit..."
        kat.say "You're serious?!?"
        show kat happy
        kat.say "Yes, I'll marry you!"
        show kat smile
        "I shrug as I stand up and put a ring on each of their fingers."
        mike.say "Well..."
        mike.say "Technically you're marrying each other too!"
        mike.say "You do realise that, right?"
        show bree stuned
        show kat stuned
        "[bree.name] and Kat exchange a look of genuine surprise."
        show bree happy at startle
        show kat happy at startle
        "But then they both nod and laugh."
        show bree smile
        bree.say "I guess we are!"
        show kat smile
        kat.say "And that makes the whole thing even better!"
        $ kat.set_fiance()
        $ bree.set_fiance()
    elif bree.love >= 195:

        show bree happy
        "[bree.name] instantly starts flapping her hands in the air."
        "Obviously delighted at the offer I'm making."
        bree.say "Of course I will, [hero.name]…"
        bree.say "I'd love to marry you!"
        show bree normal
        "Kat takes a few seconds longer to realise what's happening."
        "But when she does, she seems to have the opposite reaction to [bree.name]."
        show kat surprised
        kat.say "Oh shit..."
        kat.say "You're serious?!?"
        show kat whining
        kat.say "No way, [hero.name], I don't want to get married!"
        show kat sad
        "I was expecting [bree.name] and Kat to say either yes or no."
        "But I never actually thought of what would happen if they disagreed!"
        "So all I can think to do is get to my feet."
        "And then to put a ring on [bree.name]'s finger."
        show bree talkative
        bree.say "Wait a second, Kat..."
        bree.say "Why wouldn't you want to marry us?"
        bree.say "Are you saying we're not good enough for you or something?!?"
        show bree annoyed
        show kat surprised
        kat.say "What?"
        show kat whining
        kat.say "No, of course not!"
        kat.say "I just don't want to get married, not to either of you or anyone else."
        show kat sad
        "I can't help scratching my head as Kat struggles to explain herself to [bree.name]."
        "Because I have no idea where this leaves us or where we go from here either."
        $ bree.set_fiance()
        $ kat.love -= 25
        $ kat.sub -= 25
    elif kat.love >= 195:

        show bree annoyed
        "[bree.name] instantly starts shaking her head."
        show bree at center, traveling(1.0, 0.3, (840, 720))
        "And she even backs off a few steps too."
        show bree sad
        bree.say "No..."
        bree.say "There's no way I want to get married."
        bree.say "I'm just not ready for the commitment!"
        show bree gloomy
        "Kat takes a few seconds longer to realise what's happening."
        "But when she does, she seems to have the opposite reaction to [bree.name]."
        show kat surprised
        kat.say "Oh shit..."
        kat.say "You're serious?!?"
        show kat happy
        kat.say "Yes, I'll marry you!"
        show kat smile
        "I was expecting [bree.name] and Kat to say either yes or no."
        "But I never actually thought of what would happen if they disagreed!"
        "So all I can think to do is get to my feet."
        "And then to put a ring on Kat's finger."
        show kat surprised
        kat.say "Wait a second, [bree.name]..."
        kat.say "Why wouldn't you want to marry us?"
        kat.say "Are you saying we're not good enough for you or something?!?"
        show kat normal
        show bree surprised
        bree.say "What?"
        show bree talkative
        bree.say "No, of course not!"
        bree.say "I just don't want to get married, not to either of you or anyone else."
        show bree gloomy
        "I can't help scratching my head as [bree.name] struggles to explain herself to Kat."
        "Because I have no idea where this leaves us or where we go from here either."
        $ kat.set_fiance()
        $ bree.love -= 25
        $ bree.sub -= 25
    else:

        show bree annoyed
        "[bree.name] instantly starts shaking her head."
        show bree at center, traveling(1.0, 0.3, (840, 720))
        "And she even backs off a few steps too."
        show bree sad
        bree.say "No..."
        bree.say "There's no way I want to get married."
        bree.say "I'm just not ready for the commitment!"
        show bree gloomy
        "Kat takes a few seconds longer to realise what's happening."
        "But when she does, she seems to be just as reluctant as [bree.name]."
        show kat surprised
        kat.say "Oh shit..."
        kat.say "You're serious?!?"
        show kat annoyed
        kat.say "No way, [hero.name], I don't want to get married either!"
        show kat annoyed
        "I feel kind of stupid, still kneeling on the ground."
        "So I slowly get back to my feet, already putting the rings away."
        mike.say "Well now I feel totally dumb!"
        mike.say "I was all ready to make honest women out of you."
        "[bree.name] and Kat at least have the grace to look a little embarrassed."
        "They both refuse to meet my eye, looking down at their feet instead."
        show bree sad
        bree.say "I'm sorry, [hero.name]…"
        bree.say "But I have to be honest."
        show bree gloomy
        show kat whining
        kat.say "Me too..."
        kat.say "This isn't the kind of thing you can lie about."
        show kat sad
        "I nod, doing the best I can to take solace from their explanations."
        mike.say "Yeah, yeah..."
        mike.say "Maybe I can get my money back on those damn rings."
    $ game.flags.gaming_delay = TemporaryFlag(True, 1)
    return

label bree_kat_male_ending:
    $ game.hour = 16
    $ game.room = "church"
    $ game.season = 1
    scene bg church wedding with fade
    "Sometimes it feels like only a few seconds ago that I got down on one knee in front of [bree.name] and Kat."
    "Like they both just said that they'd marry me, and all I've done is close my eyes for the briefest second."
    "And now that I've opened them, I'm standing at the altar in a fully decked-out chapel, waiting for them."
    "Of course the truth is that it's been far longer than that, and a hell of a lot has happened in-between."
    "But there's been so much planning, hard work and so many emotional moments since then that it's flown by."
    "Now that the actual day of the wedding is here and it's about to happen, everything feels kind of unreal."
    "I keep looking around at the pews that are filled with guests chosen by [bree.name], Kat and myself."
    "The priest gives me a reassuring smile whenever I he catches my eye."
    "Hell, I can even fell the ways my suit is pinching and making me feel itchy."
    "But it's only when the music actually starts to play that reality finally takes hold."
    "I turn my head to look down the aisle behind me, and that's when the doors burst open."
    show bree wedding at center, zoomAt(1.0, (840, 720))
    show kat wedding smile at center, zoomAt(1.0, (440, 720))
    with dissolve
    "A moment later I see [bree.name] and Kat come walking through them and down the aisle."
    show bree wedding at center, traveling(1.5, 5.0, (940, 1040))
    show kat wedding at center, traveling(1.5, 5.0, (340, 1040))
    "They're walking together, arm in arm as they come closer."
    "And I don't think I've ever seen a more beautiful thing in my life!"
    "[bree.name] looks stunning, her blonde hair streaming out behind her as she comes."
    if bree.is_visibly_pregnant:
        "And her dress has been cut to flatter the curve of her pregnant belly too."
        "So that it adds to the look, rather than sticking out like a sore thumb."
    else:
        "I can't remember ever seeing her dressed up in something so fancy before."
        "And I know it sounds corny, but she really does look like a princess!"
        "Kat's purple hair attracts the eye just as much as [bree.name]'s blonde though."
        "And there's no way that I could ever choose one of them over the other."
    if kat.is_visibly_pregnant:
        "Even with her dress cut to by sympathetic to her pregnancy, it's clear to see."
        "Kat's slight frame stands in stark contrast to her already huge belly."
        "Not that any of us are ashamed of the fact that she's carrying a baby right now."
    else:
        "Like bree, it's so strange to see Kat wearing something so formal."
        "Almost like she's cosplaying as a character from some Japanese roleplaying game!"
        "I don't get to watch [bree.name] and Kat for too long, as they're soon at the altar."
        "And as soon as they reach me, they get into their allotted positions."
        "Which leaves me mere seconds to get into mine before the priest gets the show on the road."
    "Priest" "Ahem..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join together these three people..."
    "Priest" "In the everlasting bonds of holy matrimony."
    "You know how the rest of the ceremony goes, right?"
    "The priest goes on and on about how marriage is sacred and all of that stuff."
    "But it only really gets interesting once you reach the part with the actual vows."
    "So let's skip ahead to that part."
    "Priest" "Do you, [bree.name]..."
    "Priest" "Take Kat and [hero.name]…"
    "Priest" "To be your lawful, wedded partners?"
    show bree happy blush at startle
    bree.say "I do."
    show bree smile
    "Priest" "Do you, Kat..."
    "Priest" "Take [bree.name] and [hero.name]…"
    "Priest" "To be your lawful, wedded partners?"
    show kat happy blush at startle
    kat.say "I do."
    show kat smile
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take [bree.name] and Kat..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "You bet I do!"
    "The priest nods."
    "Priest" "Very good..."
    "Next he turns to address the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these three people may not be joined in marriage..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause that's punctuated by awkward laughter."
    "But luckily for us, nobody speaks up to answer the priest's challenge."
    "Priest" "Then I have great pleasure in pronouncing you married."
    "Priest" "You may celebrate in a manner you find fitting."
    show bree wedding happy blush b at center, traveling(2.0, 0.3, (840, 1340))
    show kat wedding happy blush b at center, traveling(2.0, 0.3, (440, 1340))
    "[bree.name] and Kat throw their arms around me, pulling us into a three-way hug."
    "And I return the gesture with the same amount of enthusiasm myself."
    hide kat
    hide bree
    show bree kiss wedding
    with fade
    $ bree.flags.kiss += 1
    "I'm not sure who's kissing who at any particular moment."
    hide bree
    show kat kiss wedding
    with fade
    $ kat.flags.kiss += 1
    "But it's not like any of us is keeping track."
    hide bree
    hide kat
    show bree wedding smile blush b zorder 1 at center, zoomAt(2.0, (840, 1340))
    show kat wedding smile blush b zorder 2 at center, zoomAt(2.0, (440, 1340))
    with fade
    "The only thing on our minds right now is the crazy fact that we did it."
    "We actually went and got married!"
    "And I don't know where we're going to end up going next."
    "But wherever it is, we'll be going there together."
    scene bg black
    show kat bree ending
    with fade
    bree.say "So this is where we get to tell our side of the story?"
    bree.say "To spill all of [hero.name]'s dirty little secrets?"
    kat.say "I don't think it's quite like that, [bree.name]..."
    kat.say "You're making it sound like he's been arrested and charged with something."
    kat.say "Plus you were one of his 'dirty little secrets' for a while!"
    bree.say "HEY!"
    bree.say "What are you trying to say, Kat?"
    bree.say "It was never anything like that!"
    bree.say "[hero.name] and I were always legit..."
    bree.say "Even before you came along."
    kat.say "Anyway..."
    kat.say "I think they want us to tell the story from our point of view."
    bree.say "Well, I guess it is pretty interesting."
    bree.say "Like, you actually hated [hero.name] and me when we first met - remember?"
    kat.say "Of course I do."
    kat.say "But in my defence, we were mortal enemies at the time!"
    bree.say "Mortal enemies?!?"
    bree.say "Kat, we were competing in a videogames tournament."
    kat.say "Yeah, and I took my career as a competitive gamer very seriously too!"
    kat.say "All I wanted back then was to crush you two and move on to the next challenge."
    bree.say "But that's not what happened, was it?"
    bree.say "Remind me, Kat..."
    bree.say "How did that one end up going?"
    kat.say "Urgh..."
    kat.say "Really, [bree.name]?"
    kat.say "Okay, okay..."
    kat.say "It was you and [hero.name] that crushed me and my partner."
    kat.say "But after that I got to thinking that I wanted to know why."
    kat.say "I wanted to know what it was that gave you two the edge."
    bree.say "And you found out that the magical ingredient was love!"
    kat.say "How do you do that, [bree.name]?"
    kat.say "How do you make everything sound like a cheesy kid's cartoon?"
    kat.say "I'd say I found out it was the genuine connection that you had."
    bree.say "And you wanted in on it too."
    kat.say "Okay, yeah - I did."
    kat.say "The next thing I knew, I was getting all of that and more!"
    bree.say "And we've never looked back."
    bree.say "We're all pretty great as individuals."
    kat.say "But we're so much more when we're all working together."
    bree.say "That's right - we're a family!"
    if bree.is_visibly_pregnant and kat.is_visibly_pregnant:
        kat.say "You can say that again!"
        bree.say "With my little man Mario!"
        kat.say "And don't forget his brother..."
        kat.say "Sweet little Luigi!"
        bree.say "Aww..."
        bree.say "I love watching those two run their daddy around until he's exhausted!"
    elif bree.is_visibly_pregnant:
        kat.say "You can say that again!"
        bree.say "With my little man Mario!"
        kat.say "Aww..."
        kat.say "I love watching him run his daddy around until he's exhausted!"
    elif kat.is_visibly_pregnant:
        kat.say "You can say that again!"
        kat.say "With my sweet little Luigi!"
        bree.say "Aww..."
        bree.say "I love watching him run his daddy around until he's exhausted!"
    else:
        kat.say "Or at least we will be once we have kids."
        bree.say "Ooh..."
        bree.say "I feel broody whenever you mention them!"
        kat.say "My biological clock's ticking too!"
        kat.say "We need to get [hero.name] on the job, and soon!"
    bree.say "Sure, when we're not all slaving away at the studio!"
    bree.say "It's our hard work that's made it a success - not just [hero.name]'s."
    kat.say "I guess it was kind of a no-brainer, us going into business making games."
    kat.say "All three of us have forgotten more about them than most people will ever know."
    bree.say "Yeah, but that's not what makes our games special, Kat."
    bree.say "Our games are special because we put love into each and every one."
    bree.say "The same love that we have for each other."
    kat.say "I hate to say it, [bree.name]..."
    kat.say "But you're right!"
    kat.say "If we do something with love, it always seems to work out for us."
    bree.say "That's the spirit, Kat..."
    bree.say "You, me and [hero.name]..."
    bree.say "Together we can take on the world!"
    kat.say "And we can win too!"
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
