init python:
    Event(**{
    "name": "harmony_lexi_showdown",
    "priority": 500,
    "label": "harmony_lexi_showdown",
    "conditions": [
        HeroTarget(
            OnDate(),
            IsRoom("date_beach", "date_nudistbeach"),
            ),
        PersonTarget(lexi,
            OnDate(),
            MinStat("love", 125)
            ),
        PersonTarget(harmony,
            Not(IsHidden()),
            MinStat("love", 125),
            IsFlag("blowjob"),
            ),
        "Person.showdown(harmony, lexi)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "goodevil_harem_event_01",
    "label": "goodevil_harem_event_01",
    "duration": 1,
    "priority": 500,
    "conditions": [
        TogetherInHarem('goodevil', 'harmony', 'lexi'),
        GameTarget(IsFlag("goodevil_delay", False),),
        HeroTarget(
            IsActivity("work", "workhard", "work_personal", "workhard_personal")
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            MinStat("love", 135),
            MinStat("lesbian", MIN_LES_GIRL_SEX),
            ),
        PersonTarget(harmony,
            Not(IsHidden()),
            MinStat("love", 135),
            MinStat("lesbian", MIN_LES_GIRL_SEX),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "goodevil_harem_event_02",
    "label": "goodevil_harem_event_02",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("goodevil_harem_event_01"),
        GameTarget(IsFlag("goodevil_delay", False)),
        HeroTarget(
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            MinStat("love", 160),
            MinStat("lesbian", MIN_LES_GIRL_SEX),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(harmony,
            Not(IsHidden()),
            MinStat("love", 160),
            MinStat("lesbian", MIN_LES_GIRL_SEX),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        Or(
            Or(
                PersonTarget(lexi,
                    OnDate()
                    ),
                PersonTarget(harmony,
                    OnDate()
                    ),
                ),
            And(
                HeroTarget(Not(OnDate())),
                Or(
                    PersonTarget(lexi,
                        IsActive(),
                        ),
                    PersonTarget(harmony,
                        IsActive(),
                        ),
                    ),
                ),
            ),
        ],
    "do_once": True,
    })

label harmony_lexi_showdown:
    scene bg beach
    show lexi swimsuit normal zorder 2
    with fade
    "The weather was just so great today that Lexi and I had to come to the beach."
    "With the sun beating down on us like it is right now, we'd be crazy to be anywhere else."
    "In this heat, the only thing to do is strip down to a swimsuit and lie on the sand."
    "Well, in my case it's more like lie on the sand and stare at Lexi the whole time."
    "I mean, there's no way the weather can get hotter than she is!"
    show lexi happy
    "And Lexi seems to appreciate the attention too, loving the fact my eyes are on her."
    "The hips, the belly, the breasts..."
    show lexi wink
    "And not to mention the filthy smile on her beautiful face too."
    "It makes me wish I'd brought a hat to cover up my groin."
    "Because she's making me painfully hard right now!"
    lexi.say "Like what you see, huh?"
    show lexi flirt at center, zoomAt(1.5, (640, 1040))
    lexi.say "You want to see some more?"
    "I'm about to nod, my tongue hanging out like a dog's."
    "But then I see something that draws my eye away from Lexi."
    "Of course it's another girl."
    "But one that's built in a very different way."
    "I see full thighs and buttocks, a curved belly and awesome breasts."
    "And by the time my eyes reach the girl's face, I know exactly who she is."
    show lexi surprised
    mike.say "Harmony!"
    show harmony swimsuit normal zorder 1 at right with easeinright
    harmony.say "Hi, [hero.name]..."
    harmony.say "Fancy bumping into you here at the beach!"
    "Harmony's standing on the sand a few feet away from Lexi and me."
    "Her hands are resting on her generous hips as she looks down at us."
    "And I can see from the look in her eye that she's more a little pleased to see me."
    show lexi annoyed at center, zoomAt(1.25, (420, 920))
    lexi.say "Ahem!"
    show lexi angry
    lexi.say "Who the fuck is this, [hero.name]?"
    lexi.say "Some random slut you know?"
    show lexi annoyed
    show harmony sad
    "My eyes go wide as I turn to glance at Lexi."
    "I know that she's not the most polite or well-mannered girl I ever met."
    "But even so I can't quite believe what just came out of her mouth."
    mike.say "LEXI!"
    mike.say "Don't talk to Harmony like that!"
    "I'm expecting Harmony to be offended by Lexi's rudeness."
    show harmony normal
    "But if she is, then he doesn't seem to show it."
    show harmony at center, zoomAt(1.25, (860, 920))
    "Instead, Harmony sits down on the sand right beside us."
    harmony.say "It's okay, [hero.name]."
    harmony.say "It takes a slut to know a slut."
    show harmony mean
    harmony.say "Right, Lexi?"
    "Lexi makes a huffing sound and narrows her eyes."
    show lexi angry
    lexi.say "I'm not just any slut."
    show lexi wink
    lexi.say "I'm an exceptional slut!"
    show harmony normal
    "Harmony raises her eyebrows at Lexi's outburst."
    "But then something seems to occur to her."
    harmony.say "You really think so, Lexi?"
    harmony.say "Because [hero.name] here would know."
    harmony.say "He's experienced what I can do first-hand."
    show harmony mean
    show lexi normal
    harmony.say "And you look like the kind to have given him everything on the first date!"
    "It doesn't take much for Lexi to rise to the bait."
    "And she sits up to look Harmony straight in the eye."
    lexi.say "You really want to take me on, bitch?"
    show lexi annoyed
    lexi.say "Because I guarantee that you'll lose!"
    "Harmony keeps on smiling as she turns her gaze to me."
    harmony.say "What do you think, [hero.name]?"
    harmony.say "Are you up for it?"
    "Both of them are staring at me now."
    "My instinct is to say no, of course it is."
    "But I'm pretty sure they won't quit if that's my answer."
    mike.say "Urgh..."
    mike.say "Okay, okay..."
    mike.say "But you have to respect my decision, yeah?"
    mike.say "No holding it against me."
    show harmony normal
    harmony.say "Of course."
    show lexi normal
    lexi.say "You got it."
    lexi.say "But what is he going to judge us on?"
    harmony.say "Hmm..."
    harmony.say "How about giving oral?"
    lexi.say "Works for me."
    lexi.say "Okay, [hero.name], who gives the best head?"
    lexi.say "Me or double-butt here?"
    "I look from Lexi to Harmony and back again."
    "Christ...it looks like they're actually going to make me do it!"
    "So I shake my head and begin to recall the last time each of them went down on me."
    "And when I do that, there's only one possible answer..."
    if harmony.love >= 150 and lexi.love >= 150:
        "There's no way I can choose between the two of them."
        "They both give blow-jobs that are out of this world."
        "But there's no way to compare them and decide which one's better."
        "And I can't just choose one of them for the sake of ending the argument either."
        "Because the moment I do, the other one is going to turn on me!"
        "Maybe if I'm honest about all of that, then they'll see reason?"
        mike.say "How can I choose between the two of you girls?"
        mike.say "You both have your own unique ways of giving head."
        mike.say "And on top of that, I can't remember every blow-job you gave me!"
        mike.say "So how am I supposed to compare them?"
        show harmony annoyed
        show lexi annoyed
        "Harmony and Lexi don't look very pleased with my answer."
        "And it looks like my efforts to call it a stalemate aren't going to work either."
        lexi.say "Well you should remember all the times I've blown you!"
        lexi.say "You should be grateful that I've even done it at all!"
        "For a moment Harmony looks like she's going to give me an ear-bashing too."
        "But then I see a thoughtful look spread over her face."
        "And I just know she's had an idea of some kind."
        show harmony normal
        harmony.say "If [hero.name] swears he doesn't remember, we can soon fix that."
        lexi.say "Huh?"
        show lexi normal
        lexi.say "What are you talking about?"
        harmony.say "All we need to do is take him over there..."
        "Harmony jerks her head towards some rocks a little way from where we're sitting."
        harmony.say "Make sure that nobody can see what we're doing..."
        "Suddenly, realisation seems to dawn on Lexi."
        lexi.say "Oh..."
        lexi.say "I get it!"
        show lexi flirt
        lexi.say "We drag him over there and give him oral!"
        "Harmony smiles and gives Lexi a nod."
        harmony.say "Exactly that, Lexi."
        show harmony blush
        harmony.say "I can't think of a fairer way to settle it."
        harmony.say "What do you think, [hero.name]?"
        show harmony normal
        show lexi normal
        "What do I think?!?"
        "Just a few seconds ago I was trapped between two angry girls."
        "But now they're asking me to let them compete to see who gives better head!"
        "Of course I'm going to think that's a great idea!"
        mike.say "Erm..."
        mike.say "Okay, girls."
        mike.say "I guess I can go along with that..."
        "I'm trying hard not to sound too enthusiastic as I agree to the competition."
        "Mainly because I'm worried that they might turn on me again if I look too eager."
        "What I need to do is keep their attention on the rivalry between them."
        "And off of the fact that I've gotten pleasure from them both in the past."
        "The plan seems to be working, as Harmony and Lexi each grab one of my wrists."
        "And together they unceremoniously haul me to my feet."
        "Then they waste no time in dragging me over to the nearby rocks."
        "Once we're behind them, I see that Harmony was right."
        "There's no chance of anyone seeing us back here."
        "We're in the shade, away from the sun and the sea."
        mike.say "Okay..."
        mike.say "How are we going to..."
        "Before I can finish, Harmony and Lexi yank down my trunks."
        "And then they kneel down in front of me, looking like they mean business."
        lexi.say "I think I should get to go first."
        show lexi happy
        lexi.say "Because we were on a date before you even showed up."
        harmony.say "We can't take turns at this!"
        show harmony annoyed
        harmony.say "We can't risk him not being able to go twice without a rest."
        show lexi normal
        lexi.say "So what in the hell are we going to do?"
        show harmony normal
        harmony.say "We have to work on him at the same time."
        "This said, Harmony looks up and into my eyes."
        harmony.say "Then you finish with whoever you think did the best."
        harmony.say "Okay, [hero.name]?"
        "I nod eagerly, keen to agree to anything if it'll get things started."
        mike.say "Sure thing, Harmony."
        mike.say "I'll make my choice before I shoot my load!"
        "Harmony and Lexi both nod at this."
        "Which I guess is as close as they're going to get to a sporting handshake."
        "I'm expecting Harmony to signal that it's time to go for it."
        "Or that they'll both wait for me to tell them to begin."
        "But instead the pair of them just fall on me at the same moment."
        scene goodevil bj with fade
        "What follows is perhaps the strangest blow-job I've ever had."
        "Harmony and Lexi jostle for position, trying to push each other out of the way."
        "But at the same time they're both trying to get at my cock too!"
        "In the end, Harmony's the one that gets to the head first."
        show goodevil bj suck left
        "And she smiles up at me as she takes it into her mouth."
        "Normally she'd have taken her time, but here she just wants to get hold of it."
        "Not to be outdone, Lexi goes lower and starts to suck on my balls."
        "Like I said, there's no slow build-up here, they just go for it."
        "Which means that I'm jolted into the thing along with them."
        "And straight away I'm reminded of just how hard it's going to be to choose a winner."
        "Because Harmony and Lexi are pretty much evenly matched."
        "Lexi's got tons of experience at this kind of thing, making her a real pro."
        "But all those years of repression have turned Harmony into a kind of sexual savant!"
        "And it's a real shame that the two of them feel they have to compete."
        "Because with them working different parts of me, their efforts are complementing each other nicely."
        "As they get into the act, it seems I might be getting even luckier."
        "And that's thanks to Harmony and Lexi seeming to concentrate on pleasing me."
        "You know, rather than pushing each other aside?"
        "While Harmony is swallowing my cock, Lexi is playing with my balls."
        "And more than once I swear that I see them actually swap places."
        show goodevil bj suck right
        "Something they manage to pull of without getting in each other's way."
        show goodevil bj suck left
        "In fact, it's getting hard for me to remember which one of them is where."
        show goodevil bj suck right
        "More than once I close my eyes with my cock in Lexi's mouth."
        show goodevil bj suck left
        "And when I open them again, I see Harmony in her place!"
        "But which one of them is doing better?"
        "I know that I'm going to have to make a decision soon."
        "Because I can't take much more of this!"
        menu:
            "Cum on Harmony":
                "The next time I look down and see my cock in Harmony's mouth, that seals the deal."
                show goodevil bj suck left
                "I can't hold on any longer, and it seems like she's the one that's got me to this point."
                "So I just let myself go and do what come naturally."
                menu:
                    "Cum in her mouth":
                        "I don't even think about pulling my cock out of Harmony's mouth."
                        with vpunch
                        "I just shoot my load straight down her throat instead!"
                        show goodevil bj suck left cum inmouth with vpunch
                        "Harmony's eyes go wide with surprise, but then she realises what's happening."
                        with vpunch
                        "And she swallows every drop without losing a beat."
                    "Cum on her face":
                        "At the very last moment, I pull my cock out of Harmony's mouth."
                        "She gasps as it happens, but then immediately begins to squeal."
                        show goodevil bj facial left cum cumshot with vpunch
                        "And that's because streamers of warm, sticky cum are painting her face."
                        with vpunch
                        "All the same, Harmony kneels there until I'm done."
            "Cum on Lexi":
                "The next time I look down and see my cock in Lexi's mouth, that seals the deal."
                show goodevil bj suck right
                "I can't hold on any longer, and it seems like she's the one that's got me to this point."
                "So I just let myself go and do what come naturally."
                menu:
                    "Cum in her mouth":
                        "I don't even think about pulling my cock out of Lexi's mouth."
                        with vpunch
                        "I just shoot my load straight down her throat instead!"
                        show goodevil bj suck right cum inmouth with vpunch
                        "Lexi's eyes go wide with surprise, but then she realises what's happening."
                        with vpunch
                        "And she swallows every drop without losing a beat."
                    "Cum on her face":
                        "At the very last moment, I pull my cock out of Lexi's mouth."
                        "She gasps as it happens, but then immediately begins to grin."
                        show goodevil bj facial right cum cumshot with vpunch
                        "And that's because streamers of warm, sticky cum are painting her face."
                        with vpunch
                        "All the same, Lexi kneels there until I'm done."
                        with vpunch
                        "And her cheeks are steaked with the stuff."
        "Afterwards, I pull up my shorts, suddenly aware of the fact we're out in public."
        "Harmony and Lexi are still sitting on the ground, panting and eyeing each other."
        "But I think I can see something new in their eyes as they do so."
        "Am I going mad, or is there some kind of weird respect growing between them?"
        $ game.flags.goodevil_delay = TemporaryFlag(True, 2)
        $ Harem.join_by_name("goodevil", "harmony", "lexi")
    elif harmony.love >= lexi.love:
        mike.say "Don't get me wrong, Lexi..."
        mike.say "You're good."
        mike.say "But Harmony's the best I've ever had."
        show harmony happy
        "Harmony's smile is as wide as it can possibly be."
        "But Lexi looks like she literally wants to kill me."
        lexi.say "What the fuck, [hero.name]?"
        show lexi angry
        lexi.say "What the actual fuck?!?"
        "I hold up my hands in an effort to fend Lexi off."
        mike.say "Hey!"
        mike.say "You said you wouldn't hold it against me!"
        "All my pleading earns me is a slap across the face from Lexi."
        "While I'm still reeling from it, she gets up and grabs her stuff."
        lexi.say "Fuck you, [hero.name]."
        hide lexi with easeoutright
        "I watch as Lexi storms off down the beach."
        "But then I feel the sensation of a hand on my groin."
        "And I look round to see Harmony leaning in close to me."
        harmony.say "Forget about that bitch, [hero.name]."
        harmony.say "Because I want to talk to you about your answer."
        show harmony blush
        harmony.say "About how I give the best head you ever had..."
        $ lexi.set_gone_forever()
        $ hero.cancel_event()
        $ game.room = "map"
        $ game.active_date.stay = False
    else:
        mike.say "Don't get mad, Harmony..."
        mike.say "You give great head."
        mike.say "But Lexi's got you beat when it comes to giving head."
        show lexi happy
        "Lexi's smile is as wide as it can possibly be."
        "But Harmony looks pretty fucking annoyed."
        harmony.say "How can you say that, [hero.name]?"
        show harmony angry
        harmony.say "How can you choose this cheap slut over me?!?"
        "I hold up my hands in an effort to fend Harmony off."
        mike.say "Hey!"
        mike.say "This was all your idea, Harmony!"
        "All my pleading earns me is a slap across the face from Harmony."
        "While I'm still reeling from it, she gets up and grabs her stuff."
        harmony.say "Up yours, [hero.name]."
        hide harmony with easeoutright
        "I watch as Harmony storms off down the beach."
        "But then I feel the sensation of a hand on my groin."
        "And I look round to see Lexi leaning in close to me."
        lexi.say "Forget about that fat cow, [hero.name]."
        lexi.say "Because I want to talk to you about your answer."
        show lexi flirt
        lexi.say "About how I give the best head you ever had..."
        $ harmony.set_gone_forever()
        $ game.active_date.score += 20
    return

label missed_goodevil_harem_date(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony and Lexi are going to be mad."
        $ harmony.love -= 10
        $ lexi.love -= 10
    return

label goodevil_harem_event_01(appointment=None):
    $ renpy.dynamic(harmony_score=0, lexi_score=0)
    scene bg street with fade
    "I've been doing the best I can to juggle seeing Harmony and Lexi at the same time."
    "Going out on a date with Harmony on one day and then Lexi the next."
    "Hell, I've even tried taking one of them out in the day and one in the evening."
    "And trying to keep them both happy on the same day almost killed me!"
    "Sure, it helps to have a pair of girlfriends that are cool with sharing me."
    "But at the same time I know that they're also intrigued by what I'm doing when they're not present."
    "Lexi and Harmony are a pretty kinky pair of girls, so I guess that's only natural."
    "So it's not long before we decide that we should all go on a date together."
    "And just what would be a suitable venue for such an occasion?"
    "A church social event?"
    "A barbeque at my parent's place?"
    "Or maybe a trip to the opera?"
    "Of course not!"
    "A night at the strip club is just what the doctor ordered."
    "So I arrange to meet the pair of them outside the place on the night."
    "And I'm also sure to tell them the time we need to be getting there too."
    scene bg alley
    show harmony sexydate normal
    with fade
    "Which is kind of why I'm surprised to see Harmony already here when I arrive."
    mike.say "Oh..."
    mike.say "Hi, Harmony!"
    mike.say "Aren't you a little early?"
    show harmony happy
    "Harmony gives me one of her winning smiles, the kind that so easily get me hard."
    "And she flutters her lashes at me too, which only serves to add to the effect."
    show harmony normal
    harmony.say "Hi there, [hero.name]..."
    harmony.say "I'm not early."
    harmony.say "I'm just super enthusiastic!"
    show harmony happy at startle
    "Harmony giggles, as if to seal the deal."
    "And all I can do is nod and smile back at her."
    mike.say "Well..."
    mike.say "It's about the time we agreed to meet by now."
    mike.say "I wonder where Lexi's gotten to?"
    show harmony annoyed
    "Harmony shrugs, and we both make a point of looking up and down the street."
    "But Lexi's still nowhere to be seen."
    show harmony normal with fade
    "Harmony and I spend some time chatting as the minutes tick by."
    "And it's a good while until I spot Lexi finally turning the corner."
    "She waves to us as she walks up, without a hint of an apology."
    show lexi sexydate happy at left with easeinleft
    lexi.say "Here I am!"
    lexi.say "So what are we waiting for?"
    show harmony annoyed at right with ease
    harmony.say "You, apparently!"
    harmony.say "[hero.name] and I have been standing here for ages!"
    show lexi annoyed
    lexi.say "That sounds more like a 'you problem' than a 'me problem'!"
    lexi.say "You should have just waited for me inside the place."
    show harmony normal
    "At this, Harmony turns to look at me."
    show lexi normal
    "Then Lexi does the same thing."
    "I guess they're expecting me to step in and settle the matter."
    menu:
        "You should have warn us Lexi!":
            mike.say "It's not cool to leave us standing around like that, Lexi."
            mike.say "And we didn't go inside because we're all on this date together."
            mike.say "So we were trying not to leave you out of the fun."
            show lexi angry
            "Lexi opens her mouth to argue the point with me."
            "But then the reality of the situation seems to dawn on her."
            show lexi annoyed
            "And she goes into a little bit of a sulk."
            lexi.say "Okay, okay..."
            lexi.say "Point taken."
            show harmony mean
            "Harmony, on the other hand, looks vindicated."
            "Though I'm glad she keeps her mouth shut this time."
            $ harmony_score += 1
            $ lexi_score -= 1
        "You were not exactly on time either Harmony!":
            mike.say "You weren't here on time either, Harmony."
            mike.say "Sure, you were here early."
            mike.say "But what's up with that?"
            mike.say "Are you trying to make the rest of us feel bad?"
            show harmony upset
            "Harmony opens her mouth to argue the point with me."
            "But then the reality of the situation seems to dawn on her."
            show harmony annoyed
            "And she goes into a little bit of a sulk."
            harmony.say "Alright, [hero.name]..."
            harmony.say "I get your point."
            "Lexi, on the other hand, looks vindicated."
            show lexi yawn
            "Though I'm glad she keeps her mouth shut this time."
            $ harmony_score += 1
            $ lexi_score -= 1
        "Scold them both.":
            mike.say "It's not cool to leave us standing around like that, Lexi."
            mike.say "And we didn't go inside because we're all on this date together."
            mike.say "So we were trying not to leave you out of the fun."
            show lexi angry
            "Lexi opens her mouth to argue the point with me."
            "But then the reality of the situation seems to dawn on her."
            show lexi annoyed
            "And she goes into a little bit of a sulk."
            "Harmony, on the other hand, looks vindicated."
            show harmony mean
            "That is until I turn around and lecture her too."
            mike.say "But you weren't here on time either, Harmony."
            show harmony angry
            mike.say "Sure, you were here early."
            mike.say "But what's up with that?"
            mike.say "Are you trying to make the rest of us feel bad?"
            show harmony annoyed
            harmony.say "Alright, [hero.name]..."
            harmony.say "I get your point."
            lexi.say "Okay, okay..."
            lexi.say "Point taken."
            "I nod, trying to draw a line under the matter."
            "It sucks to argue so early into a date."
            "But sometimes you have to put your foot down."
            $ harmony_score -= 1
            $ lexi_score -= 1
        "Try to ease the tension.":
            "I hold up my hands, appealing for peace."
            mike.say "Okay, okay..."
            mike.say "It doesn't matter who got here when."
            mike.say "All that matters is the fact we're here now."
            mike.say "And we're going to have a great time, right?"
            show lexi angry
            show harmony angry
            "I see both of the girls open their mouths to argue."
            "But then they see each other doing it too."
            show lexi annoyed
            show harmony annoyed
            "And that seems to be enough to stop things from escalating."
            "Okay, maybe it's not an apology from either of them."
            "But it's at least a temporary truce."
            harmony.say "Alright, [hero.name]..."
            show harmony normal
            harmony.say "I get your point."
            lexi.say "Okay, okay..."
            show lexi normal
            lexi.say "Point taken."
            "I nod, trying to draw a line under the matter."
            "It feels good to have avoided an argument to early on."
            "And hope that things can only get better from here."
            $ harmony_score += 1
            $ lexi_score += 1
    hide lexi
    hide harmony
    with easeoutright
    "As we walk into the strip club, I take a moment to look the girls over."
    scene bg stripclub with fade
    show harmony sexydate normal at left
    show lexi sexydate normal
    with easeinleft
    "They're both dressed in what I've come to think of as their signature styles."
    "Neither of them seems to see any point in covering themselves up."
    "But Harmony is definitely into more flashy stuff."
    "Whereas Lexi's still rocking that trailer-park style!"
    "My eyes are drifting from one of them to the other."
    "But it seems like I haven't been able to do so unnoticed."
    lexi.say "I can feel your eyes all over me, [hero.name]!"
    show lexi flirt
    lexi.say "I guess you like what you see?"
    show harmony annoyed
    harmony.say "Excuse me..."
    show harmony blush
    harmony.say "I think you'll find he was checking me out!"
    "Urgh..."
    "We've only been inside the place a couple of minutes."
    "And they're already starting up another argument!"
    menu:
        "You look stunning Harmony!":
            mike.say "Look, Lexi..."
            mike.say "I like what you have on, really I do."
            show harmony normal
            show lexi happy
            mike.say "But Harmony's just made a bit more of an effort."
            show lexi annoyed
            mike.say "Don't you think?"
            show lexi angry
            "I see anger flare in Lexi's eyes as I ask the question."
            show harmony blush
            "At the same time, Harmony almost blushes at the compliment."
            harmony.say "Why, thank you!"
            harmony.say "I do try to make an effort."
            $ harmony_score += 1
            $ lexi_score -= 1
        "That's quite any outfit Lexi!":
            mike.say "Look, Harmony..."
            mike.say "I can see you've made an effort, I really can."
            show lexi normal
            show harmony happy
            mike.say "But it kind of looks like you're trying too hard."
            show harmony annoyed
            mike.say "I prefer casual and effortless - like Lexi here."
            show harmony angry
            "I see anger flare in Harmony's eyes as I share my opinion."
            show lexi happy
            "At the same time, Lexi's basking in the praise I just gave her."
            lexi.say "When you're this good, why try harder?"
            lexi.say "Right, [hero.name]?"
            $ harmony_score -= 1
            $ lexi_score += 1
        "You're both incredible!":
            mike.say "Can't I check you both out?"
            show lexi normal
            show harmony normal
            mike.say "I mean, I am dating the both of you!"
            mike.say "And that's supposed to be part of the fun, right?"
            "Harmony and Lexi exchange a look as I explain myself."
            show lexi surprised
            show harmony surprised
            "And then, much to my relief, the former nods and the latter shrugs."
            show harmony normal
            harmony.say "He's got a point, Lexi."
            harmony.say "We are a lot to take in!"
            show lexi normal
            lexi.say "You got that right, Harmony."
            lexi.say "I'm surprised he can even handle us!"
            $ harmony_score += 1
            $ lexi_score += 1
        "Huh, you said something?":
            mike.say "Erm..."
            mike.say "Girls, we are in a strip club."
            show lexi normal
            show harmony normal
            mike.say "I'm looking at ALL the girls in here."
            mike.say "Not just you two!"
            "Harmony and Lexi exchange a look as I explain myself."
            show lexi surprised
            show harmony surprised
            "And I have to say they look surprised by my what I have to say."
            "And then, much to my relief, the former nods and the latter shrugs."
            show harmony normal
            harmony.say "Well if that's the way things are..."
            harmony.say "Then we'll just have to work harder to get your attention!"
            show lexi normal
            lexi.say "Hell yeah!"
            lexi.say "By the end of the night, you won't want to look at anyone else!"
            $ harmony.sub += 1
            $ lexi.sub += 1
            $ harmony_score += 1
            $ lexi_score += 1
    show lexi normal
    show harmony normal
    "Now that we're inside, I finally have a chance to look around and take in the atmosphere."
    "The club is pretty busy, and the vibe feels good as I spot a place for us to sit."
    show harmony at left5
    show lexi at right5
    with ease
    "Harmony and Lexi are about to sit down in their chosen seats when I hold up a hand."
    mike.say "Whoa!"
    mike.say "We need to get ourselves some drinks."
    harmony.say "Oh yeah!"
    show harmony happy
    harmony.say "Good thinking, [hero.name]."
    lexi.say "And more importantly..."
    show lexi happy
    lexi.say "We need to decide who's gonna go get them!"
    show lexi normal
    show harmony normal
    menu:
        "What if we did it in alphabetical order?":
            "I think about it for a moment, trying to be fair."
            "And then an idea pops right into my head."
            mike.say "Why don't we go on alphabetical order?"
            "Before I can say another word, Lexi leaps in."
            show lexi happy
            lexi.say "That's a great idea!"
            lexi.say "We should definitely do that!"
            mike.say "Okay, so that's two in favour."
            mike.say "What about you, Harmony?"
            if hero.name > harmony.name:
                show harmony annoyed
                "As soon as I turn to face Harmony, I begin to regret my choice."
                "Because from the expression she's wearing, I can tell she's not impressed."
                harmony.say "Of course I'm not for that."
                harmony.say "Harmony comes way before Lexi and [hero.name]!"
                lexi.say "Too bad, Harmony."
                lexi.say "You're out-voted, two to one!"
                hide harmony with easeoutleft
                "I watch as Harmony gets up and heads to the bar."
                "Muttering under her breath the entire way."
                $ harmony_score -= 1
                $ lexi_score += 1
            else:
                show harmony happy
                "As soon as I turn to face Harmony, I can see that she's pleased with the idea."
                harmony.say "That's a really great idea."
                harmony.say "Thank you, [hero.name]."
                "I nod as I get up and begin walking to the bar."
                "Feeling happy to have finally found a way to please them both."
                "Well, at least one that doesn't involve being naked."
                $ harmony_score += 1
                $ lexi_score += 1
        "The eldest pays the first round":
            "I think about it for a moment, trying to be fair."
            "And then an idea pops right into my head."
            mike.say "Why don't we go in order of age?"
            mike.say "Oldest first, yeah?"
            "Before I can say another word, Harmony leaps in."
            show harmony happy
            harmony.say "That's a great idea!"
            harmony.say "We should definitely do that!"
            mike.say "Okay, so that's two in favour."
            mike.say "What about you, Lexi?"
            if tuple(hero.birthday) > tuple(lexi.birthday):
                show lexi annoyed
                "As soon as I turn to face Lexi, I begin to regret my choice."
                "Because from the expression she's wearing, I can tell she's not impressed."
                lexi.say "Of course I'm not for that."
                lexi.say "And thanks for the reminder I'm the oldest!"
                harmony.say "Too bad, Lexi."
                harmony.say "You're out-voted, two to one!"
                hide lexi with easeoutleft
                "I watch as Lexi gets up and heads to the bar."
                "Muttering under her breath the entire way."
                $ harmony_score += 1
                $ lexi_score -= 1
            else:
                show lexi happy
                "As soon as I turn to face Lexi, I can see that she's pleased with the idea."
                lexi.say "That's a really great idea."
                lexi.say "Thank you, [hero.name]."
                "I nod as I get up and begin walking to the bar."
                "Feeling happy to have finally found a way to please them both."
                "Well, at least one that doesn't involve being naked."
                $ harmony_score += 1
                $ lexi_score += 1
        "I'll buy the first round":
            "I was going to suggest one of the girls get the first round."
            "But then I realise that wouldn't be very gentlemanly of me."
            mike.say "You two just sit tight."
            mike.say "I'll go grab the first round of drinks."
            "This seems to go down very well with Harmony and Lexi."
            "But then why wouldn't it?"
            show harmony happy
            harmony.say "Thank you, [hero.name]."
            harmony.say "You're such a charmer!"
            show lexi happy
            lexi.say "Yeah, [hero.name] - you're making me wet already!"
            lexi.say "And by the way, mine's a double."
            "I nod as I get up and begin walking to the bar."
            "Feeling happy to have finally found a way to please them both."
            "Well, at least one that doesn't involve being naked."
            $ harmony_score += 1
            $ lexi_score += 1
        "I'll let this to you two":
            "I was going to suggest that I buy the first round."
            "But then I remember that all of this was my idea."
            "So they should be doing something to thank me."
            mike.say "I'm going to park myself right here."
            mike.say "And you two can go get me a drink."
            mike.say "Okay?"
            "Harmony and Lexi are finally united in something."
            "Even if that is looking daggers at me!"
            harmony.say "Ooh..."
            show harmony annoyed
            harmony.say "You're no gentleman, [hero.name]."
            lexi.say "That's for sure!"
            show lexi annoyed
            lexi.say "Don't be surprised if I spit in your drink."
            hide harmony
            hide lexi
            with easeoutleft
            "I nod and smile as the girls get up and walk to the bar."
            "Sure, they might have sounded pissed at me just now."
            "But I'm sure they were just yanking my chain."
            $ harmony_score -= 1
            $ lexi_score -= 1
    scene bg stripclub
    show harmony sexydate normal at center, zoomAt (1.5, (440, 1140))
    show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
    with fade
    "A couple of drinks seems to be just what the doctor ordered."
    "Because once we've drunk them, everyone seems to be getting on much better."
    show lexi happy
    show harmony happy
    "But we're still waiting for the first act to come on stage."
    "And when they do, I'm surprised to see that they look familiar."
    mike.say "Wait a minute..."
    mike.say "Where have I seen that girl before?"
    lexi.say "Huh!"
    show lexi normal
    lexi.say "Her face is familiar."
    harmony.say "It should be."
    show harmony normal
    harmony.say "She was sitting just over there until a minute ago."
    lexi.say "So what's she doing up there?"
    play sound spank
    with vpunch
    "I slap my forehead as realisation dawns on me."
    mike.say "Of course!"
    mike.say "It's open pole night."
    mike.say "Anyone can get up there and try their hand at dancing."
    "This news seems to send a thrill through Harmony and Lexi."
    "And why not?"
    "They were expecting to see professional dancers."
    "But now they get to see fellow members of the audience dancing instead."
    "The first girl up there is a really voluptuous specimen."
    "Yet she moves with all the grace of a ballet dancer."
    "She's followed by a thinner and more edgy girl."
    "And her raunchy style more than makes up for her slighter figure."
    "After the first couple of dances are over, the girls are really into it."
    "And I can see that they're keen to discuss what they've seen."
    harmony.say "So, [hero.name]..."
    show harmony blush
    harmony.say "Did you like the first girl or the second best?"
    lexi.say "I think I know which one he liked more."
    show lexi flirt
    lexi.say "But I want to see if I guessed right."
    menu:
        "The first one, I think":
            mike.say "Oh, that's easy..."
            mike.say "I liked the first girl the best."
            mike.say "Fuller figure equals better dancer!"
            show harmony happy
            "Harmony smiles as soon as she hears what I have to say."
            "Which I suppose means that she approves of my choice."
            "But Lexi looks more than a little annoyed."
            "So she must have guessed wrong!"
            show lexi annoyed
            lexi.say "Ah..."
            lexi.say "Typical guy - always going for the big-boned girls!"
            harmony.say "Hey!"
            show harmony annoyed
            harmony.say "No fat-shaming!"
            $ harmony_score += 1
            $ lexi_score -= 1
        "The second one was great":
            mike.say "Oh, that's easy..."
            mike.say "I liked the second girl best."
            mike.say "The more sultry the dancer the better!"
            show lexi happy
            "Lexi grins like a delighted alley-cat as soon as she hears this."
            "Which I suppose means she guessed right."
            "But Harmony looks more than a little annoyed."
            "So I'm going to assume she was hoping to hear the opposite."
            show harmony annoyed
            harmony.say "Hrmph..."
            harmony.say "Typical man - always going for the hussy!"
            lexi.say "Hey!"
            show lexi annoyed
            lexi.say "No slut-shaming!"
            $ harmony_score -= 1
            $ lexi_score += 1
        "I'm not sure":
            mike.say "Oh, that's easy..."
            mike.say "I didn't like either of them."
            mike.say "One was too heavy for me."
            mike.say "And the other was too sultry."
            show lexi annoyed
            show harmony annoyed
            "Harmony and Lexi both look annoyed at my answer."
            "Which I suppose means that neither of them expected to hear that."
            harmony.say "Hey!"
            harmony.say "No fat-shaming!"
            lexi.say "No slut-shaming either!"
            lexi.say "Typical guy - no woman can ever please him."
            harmony.say "Yeah, we're always too fat or too thin."
            harmony.say "Too forward or not forward enough!"
            $ harmony_score -= 1
            $ lexi_score -= 1
        "Tough choice":
            mike.say "Wow..."
            mike.say "That's a tough one."
            mike.say "Fuller figure equals better dancer!"
            mike.say "But he more sultry the dancer the better too!"
            mike.say "I guess I liked them both."
            show lexi surprised
            show harmony surprised
            "Harmony and Lexi both look surprised by my answer."
            "Which I suppose means that neither of them expected to hear that."
            show harmony normal
            harmony.say "I suppose it's okay to like both."
            lexi.say "Yeah..."
            show lexi normal
            lexi.say "It's not good to discriminate."
    show lexi normal
    show harmony normal
    "As we sit watching the amateurs shaking their stuff, I can feel something building up between us."
    "It's like the sensation of an unspoken question that's just hanging in the air as we talk about other stuff."
    "And in the end, it's Harmony and Lexi that give voice to it."
    harmony.say "You know..."
    show harmony blush
    harmony.say "It doesn't look too hard."
    lexi.say "What doesn't?"
    lexi.say "Getting up there to dance?"
    harmony.say "Uh-huh."
    "As soon as I hear this, I know what's coming next."
    "And I do the best I can to head it off at the pass."
    mike.say "Wait a minute..."
    mike.say "Are you suggesting one of us gets up there?!?"
    "As one, Harmony and Lexi turn to face me."
    show harmony happy
    harmony.say "That's a great idea, [hero.name]!"
    show lexi happy
    lexi.say "Yeah!"
    lexi.say "You should totally do it!"
    mike.say "That's not what I said!"
    "But my pleas fall on deaf ears."
    "Because Harmony and Lexi are already trying to drag me out of my seat!"
    menu:
        "It shouldn't be harder than a workout session":
            hide lexi
            hide harmony
            with dissolve
            "I'm halfway onto the stage before I can even begin resisting."
            "And by that time, I realise that I'm not getting out of this."
            "So the only choice I have is to try and make the best of it."
            if hero.fitness >= 85:
                "I launch myself into what I hope is a decent improvised dance routine."
                "All the while making sure to regulate my breathing too."
                "And it's not long before I'm glad of all those trips to the gym."
                "Because moving like this is surprisingly tough!"
                "Part of me is worried that I'm paying more attention to breathing than dancing."
                "But that worry begins to fade as I hear the audience start to clap."
                "Hell, it sounds like some of them are even whistling and cheering too!"
                "This makes the act of dancing feel less challenging."
                "And I begin to make some more ambitious moves."
                "Sure, not all of them come off."
                show harmony sexydate normal at center, zoomAt (1.5, (440, 1140))
                show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
                with fade
                "But I leave the stage and return to my seat feeling proud of myself."
                "And it seems like Harmony and Lexi are impressed too."
                show harmony happy
                harmony.say "Five out of ten for technique, [hero.name]."
                harmony.say "But ten out of ten for effort!"
                show lexi happy
                lexi.say "Those were some nice moves."
                lexi.say "And you really made yourself sweat!"
                $ harmony_score += 1
                $ lexi_score += 1
            else:
                "I launch myself into what I hope is a decent improvised dance routine."
                "But it doesn't take me long to begin feeling more than a little out of breath."
                "I'm gulping in lungfuls of breath as I lurch around the stage."
                "And yet it seems to do nothing to help me keep on moving."
                "The inevitable end comes when I feel a sharp pain in my sides."
                "It seems to be a bad case of stitch, bad enough to double me over."
                play sound body_fall
                with vpunch
                "That and leave me helplessly sitting on my ass in the middle of the stage."
                "I can hear the crowd booing as I get onto my hands and knees."
                "And there are even people pelting me with random objects as I crawl back to my seat."
                show harmony sexydate annoyed at center, zoomAt (1.5, (440, 1140))
                show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
                with fade
                harmony.say "Well that wasn't a very impressive performance!"
                show lexi annoyed
                lexi.say "It was kind of embarrassing too."
                mike.say "Urgh..."
                mike.say "Help me..."
                mike.say "I feel like...I'm dying here!"
                $ harmony_score -= 1
                $ lexi_score -= 1
        "It's just dance, should be easy":
            hide lexi
            hide harmony
            with dissolve
            "I'm halfway onto the stage before I can even begin resisting."
            "And by that time, I realise that I'm not getting out of this."
            "So the only choice I have is to try and make the best of it."
            "Which shouldn't be that hard."
            "As I have a lot of experience when it comes to dancing."
            if hero.has_skill("dance"):
                "As I walk out onto the stage, I try to remember some basic steps."
                "And it doesn't take long for me to feel the rhythm inside of me."
                "From that point on, everything just seems to come together."
                "And before I know it, I'm dancing up a storm."
                "I hear the audience start to clap."
                "Hell, it sounds like some of them are even whistling and cheering too!"
                "This makes my confidence grow more by the second."
                "And I begin to make some more ambitious moves."
                "They lap these up too, cheering for more."
                show harmony sexydate normal at center, zoomAt (1.5, (440, 1140))
                show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
                with fade
                "I leave the stage and return to my seat feeling proud of myself."
                "And it seems like Harmony and Lexi are impressed too."
                show harmony happy
                harmony.say "Ten out of ten for technique, [hero.name]!"
                harmony.say "You really got me hot under the collar."
                show lexi happy
                lexi.say "Those were some nice moves."
                lexi.say "You made me sweat too!"
                $ harmony_score += 1
                $ lexi_score += 1
            else:
                "As I walk out onto the stage, I try to remember some basic steps."
                "But there must be something putting me off about the place."
                "Or maybe it's the drinks that I've already sunk tonight."
                "Because all that I can manage is a stumble as I drag my feet."
                "No matter what I try, nothing seems to work."
                "And it's all downhill from there."
                play sound body_fall
                with vpunch
                "The worst comes when I trip over and fall."
                "Which leaves me helplessly sitting on my ass in the middle of the stage."
                "I can hear the crowd booing as I get onto my hands and knees."
                "And there are even people pelting me with random objects as I crawl back to my seat."
                show harmony sexydate annoyed at center, zoomAt (1.5, (440, 1140))
                show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
                with fade
                harmony.say "Well that wasn't a very impressive performance!"
                show lexi annoyed
                lexi.say "It was kind of embarrassing too."
                mike.say "Ouch..."
                mike.say "Give me a break, you guys."
                mike.say "My ass is aching right now!"
                $ harmony_score -= 1
                $ lexi_score -= 1
        "You should both go":
            show harmony at center, zoomAt (1.5, (440, 1040))
            show lexi normal at center, zoomAt (1.5, (840, 1040))
            with ease
            "Harmony and Lexi almost have me halfway to the stage before I know it."
            "But that's when an idea pops into my head."
            mike.say "I'd love to see you two dance..."
            mike.say "The pair of you together!"
            show lexi surprised at startle
            show harmony surprised at startle
            "All of a sudden, the girls stop dead."
            show lexi normal
            show harmony normal
            "And they exchange a meaningful look as the idea sinks in."
            if hero.charm >= 90:
                "I can see that both of them want to impress me."
                "More so that they want my eyes on them badly too."
                "Without a single word, Harmony and Lexi let go of me."
                show harmony at center, traveling (1.0, 1.0, (540, 720))
                show lexi normal at center, traveling (1.0, 1.0, (740, 720))
                "And then they clamber onto the stage, one after the other."
                "What follows is a revelation for me and everyone else in the room."
                scene bg black
                show poledance harmony lexi sexydate with dissolve
                "As seeing one of them on stage alone would have been amazing."
                "But together there's something special about their performance."
                "Harmony and Lexi are dancing together for sure."
                "Yet at the same time they're also competing for my attention."
                "Each trying to outdo the other without letting it show."
                "The result is a truly sensual display of dancing."
                "And the audience seems to be as enthralled as I am."
                "Hell, it sounds like some of them are even whistling and cheering too!"
                "When Harmony and Lexi finally come off the stage, they look flushed and exhausted."
                "And it's hard for me to conceal the fact that I'm totally turned-on too."
                $ harmony_score += 1
                $ lexi_score += 1
            else:
                "First Harmony shakes her head."
                "And then Lexi does the same."
                harmony.say "Nice try, [hero.name]."
                lexi.say "But you're not getting out of it that easily!"
                hide lexi
                hide harmony
                with hpunch
                "With that, they shove me the last few feet onto the stage."
                "I launch myself into what I hope is a decent improvised dance routine."
                "But it doesn't take me long to begin feeling more than a little out of breath."
                "I'm gulping in lungfuls of breath as I lurch around the stage."
                "And yet it seems to do nothing to help me keep on moving."
                "The inevitable end comes when I feel a sharp pain in my sides."
                "It seems to be a bad case of stitch, bad enough to double me over."
                play sound body_fall
                with vpunch
                "That and leave me helplessly sitting on my ass in the middle of the stage."
                "I can hear the crowd booing as I get onto my hands and knees."
                "And there are even people pelting me with random objects as I crawl back to my seat."
                show harmony sexydate annoyed at center, zoomAt (1.5, (440, 1140))
                show lexi sexydate normal at center, zoomAt (1.5, (840, 1140))
                with fade
                harmony.say "Well that wasn't a very impressive performance!"
                show lexi annoyed
                lexi.say "It was kind of embarrassing too."
                mike.say "Urgh..."
                mike.say "Help me..."
                mike.say "I feel like...I'm dying here!"
                $ harmony_score -= 1
                $ lexi_score -= 1
        "I'll pass":
            "Harmony and Lexi almost manage to drag me to the stage before I can resist."
            "But then I put on the breaks and stop them in their tracks."
            "And it doesn't take me long to fight my way back to my seat."
            harmony.say "You're no fun, [hero.name]!"
            lexi.say "And you're a coward too!"
            mike.say "Hey!"
            mike.say "I came here to watch people dancing."
            mike.say "Not to get roped into it myself!"
    with fade
    "By the time most of the dancers have come and gone, we're getting ready to leave."
    scene bg alley with fade
    pause 0.1
    show harmony sexydate at left4
    show lexi sexydate at right4
    with easeinright
    "Everyone's had more than few drinks, and so we're a bit wobbly as we walk outside."
    mike.say "So..."
    mike.say "Are we going to call it a night here?"
    mike.say "Or do you fancy going somewhere else?"
    mike.say "Maybe doing something else too?"
    if harmony_score >= 4 and lexi_score >= 4:
        "As soon as I make the suggestion, Harmony and Lexi start to nod."
        harmony.say "I'm having a great time."
        show harmony happy
        harmony.say "I don't want to go home yet!"
        lexi.say "I'm totally up for doing something else."
        show lexi happy
        lexi.say "Whatever you feel like, [hero.name]."
        mike.say "That's great!"
        mike.say "Come on, guys..."
        mike.say "We can decide what and where as we walk."
        "And with that, the three of us stagger off together into the night."
        call goodevil_threesome from _call_goodevil_threesome
        $ game.flags.goodevil_delay = TemporaryFlag(True, 2)
    elif harmony_score >= 4:
        harmony.say "I'm having a great time."
        show harmony happy
        harmony.say "I don't want to go home yet!"
        lexi.say "Nah..."
        lexi.say "I'm not in the mood."
        "Lexi waves a hand in the air to underline her point."
        hide lexi with dissolve
        "And then she turns her back on me and walks away into the night."
        mike.say "I guess that just leaves you and me, Harmony."
        mike.say "We can decide what and where as we walk."
        "And with that, the two of us stagger off together into the night."
        call harmony_fuck_date_male from _call_harmony_fuck_date_male
    elif lexi_score >= 4:
        lexi.say "I'm totally up for doing something else."
        show lexi happy
        lexi.say "Whatever you feel like, [hero.name]."
        harmony.say "Oh no!"
        harmony.say "I'm way too tired to go anywhere else."
        "Harmony waves a hand in the air to underline her point."
        hide harmony with dissolve
        "And then she turns her back on me and walks away into the night."
        mike.say "I guess that just leaves you and me, Lexi."
        mike.say "We can decide what and where as we walk."
        "And with that, the two of us stagger off together into the night."
        call lexi_fuck_date_male from _call_lexi_fuck_date_male_1
    else:
        "As soon as I make the suggestion, Harmony and Lexi start to shake their heads."
        harmony.say "Oh no!"
        harmony.say "I'm way too tired to go anywhere else."
        lexi.say "Nah..."
        lexi.say "I'm not in the mood."
        "I shrug as the pair of them turn and walk away into the night."
        hide lexi
        hide harmony
        with dissolve
        "Because I suppose all I can do is try harder next time."
        "That and hope there will be a next time!"
        $ game.pass_time(2)
    $ hero.replace_activity()
    if game.active_date:
        $ game.active_date.stay = False
    return


label goodevil_harem_event_02(appointment=None):
    scene bg pub
    show lexi date at right
    show harmony date at left
    "After Harmony and Lexi got introduced to each other, I kind of got to thinking."
    "They're a pair of girls from very different backgrounds, that's for sure."
    "But they actually have a lot in common when it comes to their interests."
    "Well...specifically their interests of a carnal nature, if you know what I mean?"
    "And as a guy that has their best interests at heart, I knew they needed to meet up."
    "Because a girl can always use a friend that shares their interests."
    "So I took it upon myself to selflessly arrange for the three of us to grab a drink."
    "Now we're sitting here in the Winchester, and I can't wait to see where this goes!"
    mike.say "So..."
    mike.say "Here we are, guys."
    mike.say "Just three friends, hanging out together."
    "I'm doing the best I can to play the innocent in all of this."
    "But it's pretty obvious that Harmony and Lexi aren't fooled in the slightest."
    "Without as much as a word exchanged between them, they share a knowing glance."
    "Then they add a roll of the eyes and a nod of the head, just for good measure."
    show lexi annoyed
    lexi.say "Drop the fucking act already!"
    show harmony annoyed
    harmony.say "Yeah, [hero.name]."
    harmony.say "You're so easy to see through!"
    lexi.say "I can sense your dirty thoughts from where I'm sitting!"
    harmony.say "And don't forget the smell of him sweating away over there!"
    "This isn't how things were supposed to go down."
    "I was supposed to be playing it cool and bridging the gap between them."
    "You know, making myself essential in the relationship I want to create here?"
    "Instead it looks like Harmony and Lexi might be about to cut me out!"
    mike.say "Okay, okay..."
    mike.say "I guess we all know why we're here."
    lexi.say "Yeah, we do."
    show lexi wink
    lexi.say "Because you're a perv!"
    show harmony happy
    harmony.say "A proper horny little bastard!"
    mike.say "No, no, no!"
    mike.say "We're all here because we're like-minded individuals."
    mike.say "We're all liberated sexual beings, right?"
    show lexi flirt
    lexi.say "You could call me that."
    lexi.say "And Harmony sure seems to be."
    lexi.say "But I still think you're a perv!"
    "Harmony can't help giggling as Lexi puts me on the spot."
    "And she doesn't seem to pick up on me giving her a pleading look either."
    "But then she gets a thoughtful look on her face."
    "Which gives me a glimmer of hope."
    harmony.say "You know normally I wouldn't just come out and say something like this..."
    harmony.say "But seeing as we're all talking about being liberated and stuff..."
    harmony.say "I know a really crazy place where we could have some fun."
    harmony.say "If you two are brave enough, that is?"
    "I sense the chance to show how bold I am."
    "And so I shoot a quick glance at Lexi."
    mike.say "I know that I'm brave enough, Harmony."
    mike.say "But I can't speak for Lexi here..."
    show lexi annoyed
    lexi.say "HEY!"
    lexi.say "Like I'd need you to speak for me anyway!"
    lexi.say "You can count me in on this one."
    show lexi normal
    lexi.say "Where are you talking about, Harmony?"
    "Harmony doesn't answer the question."
    "Instead she smiles and makes a point of finishing off her drink."
    "Then she stands up and beckons for us to follow."
    harmony.say "Oh no."
    harmony.say "I get to keep it a secret until we're there."
    harmony.say "So if you're really up for it, let's go!"
    "Lexi gives me an intrigued look as she gets up too."
    "But neither of us says a word as we hurry after Harmony."
    "I'm not sure where she's taking us at first."
    "But as we make various turns and take certain streets that changes."
    "And pretty soon I have a good idea of where we're headed."
    "Still, I keep it to myself, keen to see Lexi's reaction."
    harmony.say "Okay..."
    harmony.say "Here we are!"
    scene bg street
    show lexi date surprised at right
    show harmony date at left
    lexi.say "You...you mean the church?"
    lexi.say "You want to get it on in there?"
    "Looks like my guess was right."
    harmony.say "What's the matter, Lexi?"
    harmony.say "Is a little sacrilege too rich for your blood?"
    show lexi annoyed
    lexi.say "What?"
    lexi.say "No...no way!"
    lexi.say "It's just...wouldn't an abandoned church be better?"
    "Harmony giggles again."
    "Obviously amused at being able to make Lexi nervous."
    show harmony happy
    harmony.say "Don't worry, Lexi..."
    harmony.say "There's nobody in there tonight."
    harmony.say "And I still have my keys from before they excommunicated me!"
    "Lexi doesn't look like she's totally convinced."
    "But she nods all the same, trying to win back some measure of respect."
    show lexi normal
    lexi.say "Huh..."
    lexi.say "I guess that's okay then."
    show harmony normal
    harmony.say "Okay, great!"
    harmony.say "So what about you, [hero.name]?"
    menu:
        "No way!":
            "I'm already starting to back off as Harmony asks the question."
            "And I add shaking my head to the mix as all attention turns to me."
            mike.say "Oh no..."
            mike.say "No way!"
            show lexi surprised
            show harmony surprised
            "Harmony and Lexi both look shocked by my refusal."
            harmony.say "You have got to be kidding!"
            lexi.say "Yeah, [hero.name]..."
            lexi.say "This was, like, your idea!"
            mike.say "Erm...no, it wasn't."
            mike.say "My idea was for us all to hook-up together."
            mike.say "I never said anything about fucking in a damn church!"
            show harmony normal
            harmony.say "Well I'm going inside, whatever you say!"
            show lexi normal
            lexi.say "Yeah, me too."
            lexi.say "I didn't come all this way to back down now!"
            hide harmony
            hide lexi with dissolve
            "I shrug as I turn on my heel and start to walk away."
            mike.say "Well, I hope you have fun!"
            "I can hear Harmony and Lexi shouting something at me as I walk away."
            "But I make sure to ignore it as I put some distance between myself and the church."
            "Sure, I may have just lost out on some pretty hot sex."
            "But there are some lines that even I won't cross."
            $ lexi.love -= 4
            $ harmony.love -= 4
            return
        "All right":
            "I don't even have to think about my answer."
            "Not even for a second."
            mike.say "Of course I'm up for it, Harmony!"
            mike.say "Like you even have to ask?"
            "I start to walk towards the doors of the church."
            mike.say "So, Harmony..."
            mike.say "Where do we get into this place?"
            harmony.say "There's a side-door this way."
            harmony.say "Follow me, you guys."
            "Lexi and I follow close on Harmony's heels."
            "And she wastes no time in showing us to the door she mentioned."
            scene bg church
            show lexi date at right
            show harmony date at left
            "Once we're inside, Harmony quickly locks it behind us."
            "It's then that I realise how weird being in an empty church actually is."
            "Every sound we make echoes around the place."
            "And the shadows look strange, like they're moving on their own."
            mike.say "Uh, Harmony..."
            mike.say "You're sure this place is empty?"
            lexi.say "What's the matter?"
            show lexi wink
            lexi.say "You getting cold feet?"
            mike.say "No way!"
            mike.say "I just want to be sure, that's all."
            harmony.say "Stop worrying, [hero.name]."
            harmony.say "And follow me, okay?"
            mike.say "What's wrong with getting it on right here?"
            "Harmony shakes her head at this."
            "And then she walks straight down the aisle of the church."
            harmony.say "Who wants to fuck in the pews?"
            show harmony blush
            harmony.say "When we can do it on the altar!"
            show harmony normal topless
            "Harmony's already stripping off her clothes as she says this."
            show lexi normal topless
            "And then I see Lexi rush past me, beginning to do the same."
            "It's almost like she's eager to keep up with Harmony."
            "Like she feels the other girl is outdoing her right now!"
            "I shake my head and begin to get undressed too."
            show harmony naked
            "Because it really does look like we're doing this thing."
            show lexi naked
            "And by the time I make it to the altar, they're both naked."
            "Harmony and Lexi are smiling at me."
            "What's more, they seem to be waiting for something."
            mike.say "What's the matter with you guys?"
            mike.say "I thought you were both raring to go?"
            show lexi wink
            lexi.say "We're waiting for you to choose, [hero.name]!"
            show harmony blush
            harmony.say "Which one of us gets to be the sacrificial offering?"
            call goodevil_church_threesome from _call_goodevil_church_threesome
            $ DONE["goodevil_church_threesome"] = game.days_played
    $ hero.replace_activity()
    return

label goodevil_church_threesome:
    menu:
        "Fuck Harmony":
            call goodevil_church_threesome_fuck_harmony from _call_goodevil_church_threesome_fuck_harmony
        "Fuck Lexi":
            call goodevil_church_threesome_fuck_lexi from _call_goodevil_church_threesome_fuck_lexi
    return

label goodevil_church_threesome_fuck_harmony:
    "Part of me thinks that it'd be fun to fuck Lexi right now."
    "Especially knowing that the altar's probably going to be used the very next day."
    "But Harmony was the one that really pushed to do this thing."
    "So it only seems fair that she's the one that gets fucked."
    "And I'm starting to think that I should choose her instead."
    "That way I can make sure she's not left on the sidelines."
    "That she's really drawn into the thing."
    "So with that in mind, I walk over to where she's standing."
    harmony.say "Oh yeah..."
    harmony.say "I know what that look is all about!"
    "I can't help smiling as I reach out and grab Harmony."
    "She doesn't resist for a second."
    "Instead she smiles up at me as I lift her off the ground."
    "Planting her ass on the altar, I push her legs apart."
    scene goodevil threesome harmonyfuck
    show goodevil threesome harmonyfuck church
    harmony.say "Oooh!"
    harmony.say "Hello there!"
    harmony.say "I think I know what to do with you..."
    "Harmony reaches down and takes hold of my cock."
    "She gives it a hard squeeze and then giggles."
    "All of which lets me know that she's ready to go."
    menu:
        "Fuck her pussy":
            "Before Harmony even knows what's happening, I stroke my cock along her lips."
            "A move that means she gets to know what my intentions are without me saying a word."
            "Harmony quivers in my hands, but I note that she makes no effort to escape."




































            "I don't hesitate for a second longer."
            "I can already feel how slick and warm Harmony is down there."
            "So I just keep right on pushing, working the head of my cock up and down."
            "Before I know it, I can feel the sensation of her lips beginning to part."
            "And in one smooth motion, I find myself sinking all the way into her."
            show goodevil threesome harmonyfuck vaginal
            "Harmony lets out a deep, helpless moan of pleasure as my cock fills her."
            "At the same time she's clinging onto the edge of the altar."
            "Already standing on tiptoes, she tries to haul herself up higher."
            "All for the sake of being able to let me get deeper into her."
            "But also for the sake of letting me push harder as I begin to move."
            "I don't know if it's Harmony's own efforts that make it happen."
            "Or if my thrusting into her from behind provides the push."
            "But either way, she's soon clambering onto the top of the altar."
            "This makes it much easier for me to use all of my strength as I pound away."
            "But it also means that far more of Harmony is within reach."
            "And Lexi doesn't wait for an invitation to take advantage."
            "Until now, she's just been standing by and watching."
            "But I catch sight of her over Harmony's shoulder."
            "And I feel her fingers as they reach down between the other girl's legs too!"
            "Lexi runs the tips of her fingers around Harmony's exposed pussy."
            "She tickles and teases those folds of sensitive flesh without mercy."
            "And the result is that Harmony finds herself trapped between the two of us."
            "I'm thrusting in and out of her from behind."
            "While Lexi uses her hands to play with the other girl around the front."
            "Harmony is helpless to do anything but succumb to our attentions."
            "She cries out and moans from the sensations overtaking her body."
            "That is until Lexi leans in closer and kisses her."
            "Given another source of relief, Harmony instantly returns the gesture."
            "And I'm treated to the sight of their tongues twisting together."
            "There's not a hint of jealousy or envy inside of me as I watch them."
            "In fact, the sight only serves to make the passion in me stronger."
            "I put all of my remaining strength into fucking Harmony."
            "And their kiss only ends when she can't take any more from me."
            harmony.say "Oh god..."
            harmony.say "I'm going to cum..."
            harmony.say "You're making me..."
            "Harmony's not the only one that's about to cum."
            "I can feel myself losing it too!"
















            call cum_reaction (harmony, 'vaginal') from _call_cum_reaction_259
            if _return == "vaginal_outside":

                if randint(0, 100) <= 25:
                    menu:
                        "Cum on both girls":
                            show goodevil threesome harmonyfuck -vaginal
                            call goodevil_church_threesome_cumshare from _call_goodevil_church_threesome_cumshare
                        "Go on with Harmony":
                            show goodevil threesome harmonyfuck -vaginal
                            "I have just the time to pull out before the inevitable happens."
                            "Harmony lets out a moan as I slide out of her."
                            "Then she literally collapses onto the altar."
                            show goodevil threesome harmonyfuck cumshot with hpunch
                            "Just then I shoot my load over her back and buttocks."
                            "Holding her in place so that she doesn't fall to the floor."
                else:
                    show goodevil threesome harmonyfuck -vaginal
                    "I have just the time to pull out before the inevitable happens."
                    "Harmony lets out a moan as I slide out of her."
                    "Then she literally collapses onto the altar."
                    show goodevil threesome harmonyfuck cumshot with hpunch
                    "Just then I shoot my load over her back and buttocks."
                    "Holding her in place so that she doesn't fall to the floor."
            elif _return == "vaginal_inside_pill":
                harmony.say "Do it..."
                harmony.say "Cum in me!"
                "Luckily for us, Harmony's on the pill."
                "So there's no danger in me granting her request."
                "I can just keep on going until the inevitable happens."
                show goodevil threesome harmonyfuck creampie with hpunch
                "And when it does, Harmony literally collapses onto the altar."
                "I thrust myself into her one last time, just for good measure."
                "Holding her in place so that she doesn't fall to the floor."
            elif _return == "vaginal_inside_pregnant":
                harmony.say "Do it..."
                harmony.say "Cum in me!"
                "Luckily for us, Harmony's already pregnant."
                "So there's no danger in me granting her request."
                "I can just keep on going until the inevitable happens."
                show goodevil threesome harmonyfuck creampie with hpunch
                "And when it does, Harmony literally collapses onto the altar."
                "I thrust myself into her one last time, just for good measure."
                "Holding her in place so that she doesn't fall to the floor."
            else:
                harmony.say "Do it..."
                harmony.say "Cum in me!"
                "Harmony's demand comes as such a surprise that I forget myself."
                show goodevil threesome harmonyfuck creampie with hpunch
                "I cum inside of Harmony, with nothing at all between us."
                "Harmony collapses onto the altar, making sounds of pure delight."
                "But I'm already filled with dread at the thought of what just happened."
        "Fuck her ass":
            "Before Harmony even knows what's happening, I push my cock between her buttocks."
            "A move that means she gets to know what my intentions are without me saying a word."
            "Harmony quivers in my hands, but I note that she makes no effort to escape."
            harmony.say "Ooh..."
            harmony.say "My...my ass!"
            "I don't hesitate for a second longer."
            "I can already feel how warm and welcoming Harmony is down there."
            "So I just keep right on pushing, working the head of my cock up and down."
            "Before I know it, I can feel the sensation of her muscles beginning to part."
            show goodevil threesome harmonyfuck anal
            "And in one smooth motion, I find myself sinking all the way into her."
            "Harmony lets out a deep, helpless moan of pleasure as my cock fills her."
            "At the same time she's clinging onto the edge of the altar."
            "Already standing on tiptoes, she tries to haul herself up higher."
            "All for the sake of being able to let me get deeper into her."
            "But also for the sake of letting me push harder as I begin to move."
            "I don't know if it's Harmony's own efforts that make it happen."
            "Or if my thrusting into her from behind provides the push."
            "But either way, she's soon clambering onto the top of the altar."
            "This makes it much easier for me to use all of my strength as I pound away."
            "But it also means that far more of Harmony is within reach."
            "And Lexi doesn't wait for an invitation to take advantage."
            "Until now, she's just been standing by and watching."
            "But I catch sight of her over Harmony's shoulder."
            "And I feel her fingers as they reach down between the other girl's legs too!"
            "Lexi runs the tips of her fingers around Harmony's exposed pussy."
            "She tickles and teases those folds of sensitive flesh without mercy."
            "And the result is that Harmony finds herself trapped between the two of us."
            "I'm thrusting in and out of her from behind."
            "While Lexi uses her hands to play with the other girl around the front."
            "Harmony is helpless to do anything but succumb to our attentions."
            "She cries out and moans from the sensations overtaking her body."
            "That is until Lexi leans in closer and kisses her."
            "Given another source of relief, Harmony instantly returns the gesture."
            "And I'm treated to the sight of their tongues twisting together."
            "There's not a hint of jealousy or envy inside of me as I watch them."
            "In fact, the sight only serves to make the passion in me stronger."
            "I put all of my remaining strength into fucking Harmony."
            "And their kiss only ends when she can't take any more from me."
            harmony.say "Oh god..."
            harmony.say "I'm going to cum..."
            harmony.say "You're making me..."
            "Harmony's not the only one that's about to cum."
            "I can feel myself losing it too!"
            call cum_reaction (harmony, 'anal') from _call_cum_reaction_260
            if _return == "anal_outside":
                "Luckily for me, I'm still in full control."
                "That means I have the time to pull out before the inevitable happens."
                show goodevil threesome harmonyfuck -anal
                "Harmony lets out a moan as I slide out of her."
                "Then she literally collapses onto the altar."
                show goodevil threesome harmonyfuck cumshot with hpunch
                "Just then I shoot my load over her back and buttocks."
                "Holding her in place so that she doesn't fall to the floor."
            else:
                "But as I'm deep inside Harmony's ass, that's not an issue."
                "I can just keep on going until the inevitable happens."
                show goodevil threesome harmonyfuck creampie with hpunch
                "And when it does, Harmony literally collapses onto the altar."
                "I thrust myself into her one last time, just for good measure."
                "Holding her in place so that she doesn't fall to the floor."
            $ harmony.flags.anal += 1
    $ harmony.sexperience += 1
    $ harmony.love += 2
    return

label goodevil_church_threesome_fuck_lexi:
    "Part of me wants to just make a grab for Harmony."
    "After all, this was all her idea to begin with."
    "But my gaze keeps getting drawn towards Lexi."
    "And I'm starting to think that I should choose her instead."
    "That way I can make sure she's not left on the sidelines."
    "That she's really drawn into the thing."
    "I beckon for Lexi to come towards me, and she seems to obey."
    "Turning to offer Harmony a smile, she starts to climb down from the altar."
    "She does this so that her back is towards me, buttocks swaying."
    "But I make sure that she doesn't have time to get both feet down."
    "And that's because I pounce on her before she's able to."
    "I clasp one hand on each of Lexi's thighs."
    "Then I pull her backwards without warning."
    scene goodevil threesome lexifuck
    show goodevil threesome lexifuck church
    lexi.say "WHOA!"
    lexi.say "What are you..."
    "By way of answer, I push myself hard against Lexi."
    "This means that my cock, by now rock hard, is jammed between her buttocks."
    lexi.say "Now maybe if church was a little more like this..."
    lexi.say "Then I'd have been saved from a life of depravity!"
    "Almost the same moment that Lexi says the words, I jump into action."
    "And that's because I have no intention of letting her take the lead."
    "Instead I push her up against the altar."
    "And then I take aim at my ultimate goal."
    menu:
        "Fuck her pussy":
            "I'm more than ready to get on with it myself."
            "And the more I look down at Lexi's pussy, the more I want it!"
            "I already know that's where I'm going, no doubt in my mind."





































            "Lexi seems to be on the same page as me too."
            "As she shuffles forwards on her ass."
            "And all the time she's still eyeing up my cock."
            lexi.say "So, [hero.name]..."
            lexi.say "What are you waiting for?"
            lexi.say "A sign from the heavens?"
            "I hear Harmony gasp and then snicker."
            "But Lexi's comment elicits a different reaction from me."
            "In one move I lift her up and pull her towards me."
            "While at the same time I aim my cock at it's intended target."
            show goodevil threesome lexifuck vaginal
            lexi.say "Mmm..."
            lexi.say "Aah..."
            lexi.say "Of fuck!"
            "Using gravity and her own weight, I pretty much sit Lexi on me."
            "Sure, her pussy puts up the kind of resistance that I'd expect."
            "But she's already excited, aroused at the idea of what we're doing."
            "So it doesn't take long for her muscles to begin to surrender."
            "As this happens, she inches slowly downwards, a little at a time."
            "And as she does so, my cock sinks ever deeper into her as well."
            "All the time this is happening, I'm holding Lexi in my arms."
            "She's wriggling and writhing like crazy, and it feels so good!"
            "Only when I know that I can't go any deeper do I even think about putting her down."
            "And then I part her legs, putting one of them over my shoulder."
            "Lexi leans back on the altar, watching me with helpless interest."
            "Harmony does what she can to help support the other girl."
            "Bit it soon becomes apparent that her real interests lie elsewhere."
            "And that fact is revealed as soon as her hands start to wander."
            "Harmony begins to stroke and squeeze, to pinch and play."
            "Even though I'm still deep inside Lexi, this distracts her."
            "And it does so just long enough for me to start moving."
            "As my body moves back and forth, she's suddenly reminded of my presence."
            "Lexi gasps and moans, falling even further backwards on the altar."
            "Right now she really does look like a sacrificial offering."
            "Lexi's helpless to resist anything that we're doing to her."
            "Instead she's forced to simply lie back and take it all."
            "I can feel my pace quickening by the second now."
            "And only part of that is on account of the sensation of being inside Lexi."
            "Another element in play here is the fact that I'm watching Harmony too."
            "Left alone and to her own devices, she's taking full advantage of Lexi."
            "No part of the other girl's body is left alone and untouched."
            "I keep catching Harmony glancing at me as she explored Lexi too."
            "And the fact she's enjoying me watching her is plain to see in her eyes."
            "I'd like to be able to say that it's my efforts which win out in the end."
            "That I'm the one who actually makes Lexi start to cum."
            "But the reality is that Harmony probably has a hand in it too."
            lexi.say "Shit..."
            lexi.say "I'm not joking..."
            lexi.say "Here it comes!"
            "Lexi begins to buck and twist, clinging onto me."
            "I can feel the muscles of her pussy clenching my cock."
            "And in no time at all, she's not the only one cuming!"

















            call cum_reaction (lexi, 'vaginal') from _call_cum_reaction_261
            if _return == "vaginal_outside":

                if randint(0, 100) <= 25:
                    menu:
                        "Cum on both girls":
                            show goodevil threesome lexifuck -vaginal
                            call goodevil_church_threesome_cumshare from _call_goodevil_church_threesome_cumshare_1
                        "Go on with Lexi":
                            show goodevil threesome lexifuck -vaginal
                            "I have just the time to pull out before the inevitable happens."
                            "Lexi lets out a moan as I slide out of her."
                            "Then she literally collapses onto the altar."
                            show goodevil threesome lexifuck cum with hpunch
                            "Just then I shoot my load over her back and buttocks."
                            "Holding her in place so that she doesn't fall to the floor."
                else:
                    show goodevil threesome lexifuck -vaginal
                    "I remember to pull out before it's too late."
                    "And I start to shoot my load the second I'm free."
                    show goodevil threesome lexifuck cum with hpunch
                    "My cock bobs up, spraying Lexi's belly with cum."
                    "Then she falls backwards onto the altar."
                    "I stagger backwards, totally exhausted."
                    "And I leave holding her up to Harmony."
            elif _return == "vaginal_inside_pregnant":
                lexi.say "Do it already..."
                lexi.say "It's not like you didn't already knock me up!"
                "I silently thank Lexi for the timely reminder that she's pregnant."
                "And I can just keep right on going until the very end."
                show goodevil threesome lexifuck cum vaginal
                "When I'm done, Lexi falls backwards onto the altar."
                "I let her motion pull me out of her."
                "And I leave holding her up to Harmony."
            elif _return == "vaginal_inside_pill":
                lexi.say "Fucking do it!"
                lexi.say "I'm still on the pill!"
                "I silently thank Lexi for the timely reminder that she's on the pill."
                show goodevil threesome lexifuck cum vaginal
                "And I can just keep right on going until the very end."
                "When I'm done, Lexi falls backwards onto the altar."
                "I let her motion pull me out of her."
                "And I leave holding her up to Harmony."
            else:
                lexi.say "Don't stop..."
                lexi.say "Just keep going!"
                "I'm so wrapped up in the moment that I don't realise what I'm doing."
                show goodevil threesome lexifuck cum vaginal
                "And a moment later I feel myself losing it inside of Lexi."
                "She looks delighted with what just happened, like she couldn't be happier."
                "But I'm already feeling a rising sense of dread about what I just did."
        "Fuck her ass":
            "I'm more than ready to get on with it myself."
            "And the more I look down at Lexi's ass, the more I want it!"
            "I already know that's where I'm going, no doubt in my mind."
            "Lexi seems to be on the same page as me too."
            "As she shuffles forwards on her butt."
            "And all the time she's still eyeing up my cock."
            lexi.say "So, [hero.name]..."
            lexi.say "What are you waiting for?"
            lexi.say "A sign from the heavens?"
            "I hear Harmony gasp and then snicker."
            "But Lexi's comment elicits a different reaction from me."
            "In one move I lift her up and pull her towards me."
            "While at the same time I aim my cock at it's intended target."
            show goodevil threesome lexifuck anal
            lexi.say "W...wait..."
            lexi.say "That's...that's my ass!"
            lexi.say "Mmm..."
            lexi.say "Aah..."
            lexi.say "Of fuck!"
            "Using gravity and her own weight, I pretty much sit Lexi on me."
            "Sure, her ass puts up the kind of resistance that I'd expect."
            "But she's already excited, aroused at the idea of what we're doing."
            "So it doesn't take long for her muscles to begin to surrender."
            "As this happens, she inches slowly downwards, a little at a time."
            "And as she does so, my cock sinks ever deeper into her as well."
            "All the time this is happening, I'm holding Lexi in my arms."
            "She's wriggling and writhing like crazy, and it feels so good!"
            "Only when I know that I can't go any deeper do I even think about putting her down."
            "And then I part her legs, putting one of them over my shoulder."
            "Lexi leans back on the altar, watching me with helpless interest."
            "Harmony does what she can to help support the other girl."
            "Bit it soon becomes apparent that her real interests lie elsewhere."
            "And that fact is revealed as soon as her hands start to wander."
            "Harmony begins to stroke and squeeze, to pinch and play."
            "Even though I'm still deep inside Lexi, this distracts her."
            "And it does so just long enough for me to start moving."
            "As my body moves back and forth, she's suddenly reminded of my presence."
            "Lexi gasps and moans, falling even further backwards on the altar."
            "Right now she really does look like a sacrificial offering."
            "Lexi's helpless to resist anything that we're doing to her."
            "Instead she's forced to simply lie back and take it all."
            "I can feel my pace quickening by the second now."
            "And only part of that is on account of the sensation of being inside Lexi."
            "Another element in play here is the fact that I'm watching Harmony too."
            "Left alone and to her own devices, she's taking full advantage of Lexi."
            "No part of the other girl's body is left alone and untouched."
            "I keep catching Harmony glancing at me as she explored Lexi too."
            "And the fact she's enjoying me watching her is plain to see in her eyes."
            "I'd like to be able to say that it's my efforts which win out in the end."
            "That I'm the one who actually makes Lexi start to cum."
            "But the reality is that Harmony probably has a hand in it too."
            lexi.say "Shit..."
            lexi.say "I'm not joking..."
            lexi.say "Here it comes!"
            "Lexi begins to buck and twist, clinging onto me."
            "I can feel the muscles of her ass clenching my cock."
            "And in no time at all, she's not the only one cuming!"
            call cum_reaction (lexi, 'anal') from _call_cum_reaction_262
            if _return == "anal_outside":
                "Since I chose to have some fun with Lexi's ass, there no danger."
                show goodevil threesome lexifuck cum anal
                "And I can just keep right on going until the very end."
                "When I'm done, Lexi falls backwards onto the altar."
                "I let her motion pull me out of her."
                "And I leave holding her up to Harmony."
            else:
                "I remember to pull out before it's too late."
                show goodevil threesome lexifuck out
                "And I start to shoot my load the second I'm free."
                show goodevil threesome lexifuck cum out with hpunch
                "My cock bobs up, spraying Lexi's belly with cum."
                "Then she falls backwards onto the altar."
                "I stagger backwards, totally exhausted."
                "And I leave holding her up to Harmony."
            $ lexi.flags.anal += 1
    $ lexi.sexperience += 1
    $ lexi.love += 2
    return

label goodevil_church_threesome_cumshare:
    "At the last moment I find the willpower to hold on a little longer."
    "And as soon as my cock is free, I beckon to Harmony and Lexi."
    scene goodevil threesome cumshare
    show goodevil threesome cumshare church
    "Both of them climb onto the altar and kneel in front of me."
    "They look up eagerly as I keep on rubbing my cock."
    "And a moment later I find that I can't hold on any longer."
    "With a shudder that affects my entire body, I finally let go."
    "Moving just a little as it happens, I manage to hit both of them."
    show goodevil threesome cumshare cumshot with vpunch
    "Streams of sticky white cum paint lines across their faces."
    "Harmony and Lexi have it on their noses, cheeks and lips."
    "Strings of the stuff even spread between their cheeks."
    "As it happens, their gasps of shock turn into giggles of amusement."
    "And I watch as they lick their lips, swallowing as much as they can."
    $ harmony.love += 1
    $ lexi.love += 1
    return


label goodevil_threesome:
    if 'lexi_trailer_onfire' not in DONE:
        scene bg trailer with fade
    else:
        scene bg bedroom1 with fade
    show harmony sexydate normal at left4
    show lexi sexydate normal at right4
    with easeinleft
    if 'lexi_trailer_onfire' not in DONE:
        "After a long and rambling discussion, the three of us decide to head to Lexi's trailer."
        "She argues that it's closer and there's fewer people to hear what we get up to than at my place."
        "I'm not sure that I believe her on either count, but I don't see any point in arguing."
        "And Harmony keeps pretty quiet until we actually reach the door of the trailer."
        harmony.say "Oh my..."
        harmony.say "This is...quaint!"
        "Lexi lets out a laugh at this, though I can't tell if she's amused of offended."
        "Either way she throws open the door and strides inside, leaving us to follow her example."
        scene bg trailerinside
        show harmony sexydate normal at left4
        show lexi sexydate happy at right4
        with fade
        lexi.say "Welcome to my little palace on wheels!"
        lexi.say "Come on in, and make yourselves at home."
        "By now I'm more than used to the chaotic state in which Lexi chooses to live."
        "But it's easy to see that Harmony's more than a little amazed at what she's seeing."
        show harmony surprised
        harmony.say "What happened in here, Lexi?"
        harmony.say "Was there an earthquake?"
        show lexi at startle
        "Lexi laughs again and shakes her head."
        lexi.say "Hah!"
        show lexi normal
        lexi.say "The ground does shake in here."
        lexi.say "But not in the way you mean!"
        show harmony blush
        mike.say "Erm..."
        mike.say "Lexi's kind of a free-spirit, Harmony."
        "Lexi nods at this, picking up an open can of something from the counter."
        "She takes a swig of the contents, and her face twists into an expression of disgust."
        "Then she throws the can over her shoulder, without a care for where it lands."
        lexi.say "Urgh..."
        lexi.say "That's right, Harmony..."
        lexi.say "I do what the fuck I like."
        show lexi wink
        lexi.say "And I fuck who I like too!"
        show lexi normal
        "I can't help smiling as I see the change come over Harmony."
        "The realisation dawning on her of the freedom Lexi enjoys here."
        "Before this place must have looked like nothing more than a dumpy trailer."
        "But now she's beginning to see the possibilities."
        harmony.say "You mean you could just..."
        harmony.say "Start to strip off?"
        show harmony topless with dissolve
        "As she says this, Harmony is already peeling off her clothes."
        "And she then proceeds to toss them aside."
    else:
        "After a long and rambling discussion, the three of us decide to head to my place."
        "Harmony is already peeling off her clothes."
    "Lexi nods in approval, watching Harmony with growing interest."
    lexi.say "Oh yeah..."
    show harmony naked with dissolve
    lexi.say "Just like that!"
    "Lexi's taking off her clothes too, even as she's watching Harmony."
    show lexi topless with dissolve
    "I don't know if she's even aware that she's doing so!"
    if 'lexi_trailer_onfire' not in DONE:
        harmony.say "And you could just sweep the counter clear..."
        show lexi naked with dissolve
        harmony.say "Like this?"
        "With one sweep of her arm, Harmony does just that."
        "She swipes all of the stuff on the counter onto the trailer floor."
        "It clatters down all around our feet."
        "But none of is pay it any attention."
        "Instead Lexi and I watch as Harmony, now naked, climbs onto it."
        harmony.say "And you could just do it, right here?"
        harmony.say "Not caring what anyone else thinks?"
        "Lexi answers by leaning in and kissing Harmony, full on the lips."
    else:
        show lexi naked with dissolve
        "Lexi leans in and kisses Harmony, full on the lips."
    "There's no stiffening or surprised in Harmony either."
    "She simply accepts it, returning the kiss with enthusiasm."
    "I keep on watching in silence for a few more moments."
    "But then I realise that I'm still standing there fully clothed."
    "And I begin to tear off my own clothes, afraid of being left out!"
    menu:
        "Fuck Harmony":
            if 'lexi_trailer_onfire' not in DONE:
                call goodevil_threesome_fuck_harmony from _call_goodevil_threesome_fuck_harmony
            else:
                call goodevil_threesome_fuck_harmony ("bedroom") from _call_goodevil_threesome_fuck_harmony_1
        "Fuck Lexi":
            if 'lexi_trailer_onfire' not in DONE:
                call goodevil_threesome_fuck_lexi from _call_goodevil_threesome_fuck_lexi
            else:
                call goodevil_threesome_fuck_lexi ("bedroom") from _call_goodevil_threesome_fuck_lexi_1
    if 'lexi_trailer_onfire' not in DONE:
        scene bg trailerinside
        show lexi sexydate happy nophone at right5
        show harmony sexydate happy at left5
        "Once we're all off the counter and getting dressed, I'm glad of where we are."
        "Sure, Lexi's trailer might be a massive dump on wheels."
        "But there are no housemates to walk in on us."
        "And the other residents of the trailer park seem to keep themselves to themselves."
        "If they heard a sound, then they're certainly not lining up to complain about it."
        harmony.say "I see the benefit of having a place of your own now."
        lexi.say "Be it ever so humble..."
        lexi.say "There's no place like home!"
        show harmony normal
        harmony.say "So..."
        harmony.say "Next time we do it at your place?"
        harmony.say "Right, [hero.name]?"
        show lexi normal
        mike.say "Huh?"
        mike.say "Since when?"
        show lexi happy
        lexi.say "Since we just agreed it."
        lexi.say "Two to one!"
    return


label goodevil_threesome_fuck_harmony(location="trailer"):
    "A little of the spell might have been broken as I hurry over."
    "But it was still the sight of Harmony climbing onto the counter that enchanted me."
    "So I make straight for her as she's reclining atop it."
    "Lexi seems to sense this even before I reach the other girl."
    "And she surprises me by not protesting in the slightest."
    "Instead she climbs up behind Harmony, taking hold of her shoulders."
    harmony.say "Huh?"
    harmony.say "What are you..."
    harmony.say "Oh my goodness!"
    scene bg black
    $ renpy.show(f"goodevil threesome harmonyfuck {location}")
    with fade
    "While Harmony is distracted by Lexi, I make good use of the chance."
    "Parting her legs, I push myself right up between her thighs."
    "And believe me, Harmony has some serious thighs on her!"
    "This means that I'm soon wedged in place, ready for business."
    "Harmony leans back against Lexi as I turn her almost onto her side."
    "I push one of her legs down onto the counter."
    "But the other I lift up and brace against my shoulder."
    "This means that she's laid open to me, with all the options on show."
    "I take a moment to look up, meeting Harmony's eye."
    "She looks flushed, her cheeks red and her eyes wide."
    "But all the same, she nods eagerly."
    "Letting me know that she's ready for whatever I have in mind."
    "Now the only question is where am I going to put it?"
    menu:
        "Fuck pussy":
            "Call me old-fashioned, but I want me a little bit of Harmony's pussy tonight."
            "Well, to be perfectly honest, I want all of it!"
            "And I don't intend to wait for it to come to me either."
            "Wriggling the last bit of the way forwards, I feel it wedge between Harmony's thighs."
            "She does all she can to make it easier for me to get in there."
            "And together we guide my cock home, until it brushes against her pussy."
            "As soon as this happens, Harmony lets out an almost desperate moan."
            harmony.say "[hero.name]..."
            harmony.say "Hurry up and put it in me!"
            harmony.say "I want to feel your cock inside of me!"
            "That's all I need to hear."
            "Now there's no way I need anyone's help to make it happen."
            show goodevil threesome harmonyfuck vaginal
            "Seizing Harmony by her thighs, I make a massive thrust forwards."
            "This isn't enough to see me inside, but it pushes my cock hard against her."
            "I repeat the same movement, again and again."
            "Each time I feel Harmony getting slicker and looser down there."
            "Until finally, one thrust changes everything."
            "All of a sudden, Harmony's body surrenders to me."
            "And I plunge all of the way inside her in one motion."
            "The feeling is almost impossible to describe."
            "It feels like sinking into something soft, warm and welcoming."
            "But more than that, as she's alive and rising to her passion at the same time as me."
            "For a moment I feel like this is going to be all me."
            "That Harmony's just going to lie back and take it."
            "Then I feel the sensation of her pussy clamping down on my cock!"
            mike.say "Wha..."
            mike.say "How are you..."
            "There's no answer from Harmony, just a knowing smile."
            "And then another squeeze of her muscles."
            "Which is more than enough for me to get the message."
            "Harmony wants me to fuck her, and she's not going to wait for it to happen either!"
            with vpunch
            "Spurred into action, I begin to thrust back and forth in earnest."
            "Putting all of my energy into doing what Harmony wants."
            "At first I feel like she's watching me closely."
            "Making sure that I do as I'm told."
            "But soon my efforts seem to be paying off, and she begins too relax."
            "Her eyes glazing over from the pleasure she's feeling, Harmony sags backwards."
            "And she'd likely have collapsed onto her back were it not for Lexi."
            "The other girl supports her diligently, but doesn't remain passive."
            "Instead I watch as Lexi's hands start to explore Harmony's body."
            "Helpless to resist, she can only gasp and moan as she's played with."
            "Lexi pinches her nipples, squeezes her breasts and even traces the outline of her pussy."
            "All the time I'm still pounding away at Harmony as hard as I possibly can."
            with vpunch
            "And while she seems to be melting in our hands, one part of her is coming alive."
            "Where before she was using her muscles to clench on me, they're now going haywire."
            "I take it as a sign that Harmony is on the verge of losing it."
            "And that I need to decide where I'm going to be when I lose it too."
            menu:
                "Cum inside her":
                    "Trusting Lexi to hold onto her, I keep right on going."
                    "I thrust my cock in and out of Harmony until the very end."
                    with vpunch
                    "And when I feel myself about to cum, I push in as deep as I can."
                    with vpunch
                    "This means that Harmony takes all of it, nothing held back."
                    show goodevil threesome harmonyfuck creampie with vpunch
                    "Now she really does seem to collapse into a helpless mess."
                    "Quivering and quaking in the grip of Lexi and myself."
                "Pull out":
                    "Trusting Lexi to hold onto her, I pull my cock out of Harmony."
                    if randint(0, 100) <= 25:
                        menu:
                            "The girls seem to have something in mind":
                                call goodevil_threesome_cumshare (from_girl="harmony", location=location) from _call_goodevil_threesome_cumshare
                            "Cum on Harmony":
                                show goodevil threesome harmonyfuck -vaginal with hpunch
                                "She lets out a long moan as it happens, unable to stop herself."
                                with hpunch
                                "Then I shoot my load over the curves of Harmony's exposed body."
                                show goodevil threesome harmonyfuck cumshot with hpunch
                                "Now she really does seem to collapse into a helpless mess."
                                "Quivering and quaking in the grip of Lexi and myself."
                                "Sweat mixing with everything else running over her body."
                    else:
                        show goodevil threesome harmonyfuck -vaginal with hpunch
                        "She lets out a long moan as it happens, unable to stop herself."
                        with vpunch
                        "Then I shoot my load over the curves of Harmony's exposed body."
                        show goodevil threesome harmonyfuck cumshot with hpunch
                        "Now she really does seem to collapse into a helpless mess."
                        "Quivering and quaking in the grip of Lexi and myself."
                        "Sweat mixing with everything else running over her body."
        "Fuck ass":
            "I decide that I'm going to go for Harmony's ass tonight."
            "In the hope of showing her how crazy things can get in this trailer"
            "And I don't intend to wait for it to come to me either."
            "Wriggling the last bit of the way forwards, I feel it wedge between Harmony's thighs."
            "She does all she can to make it easier for me to get in there."
            "And together we guide my cock home, until it brushes between her buttocks."
            "As soon as this happens, Harmony lets out an almost desperate moan."
            harmony.say "[hero.name]..."
            harmony.say "Hurry up and put it in me!"
            harmony.say "I want to feel your cock inside of me!"
            "That's all I need to hear."
            "Now there's no way I need anyone's help to make it happen."
            "Seizing Harmony by her thighs, I make a massive thrust forwards."
            "This isn't enough to see me inside, but it pushes my cock hard against her."
            "I repeat the same movement, again and again."
            "Each time I myself getting ever deeper down there."
            "Until finally, one thrust changes everything."
            show goodevil threesome harmonyfuck anal
            "All of a sudden, Harmony's body surrenders to me."
            "And I plunge all of the way inside her in one motion."
            "The feeling is almost impossible to describe."
            "It feels like sinking into something soft, warm and welcoming."
            "But more than that, as she's alive and rising to her passion at the same time as me."
            "For a moment I feel like this is going to be all me."
            "That Harmony's just going to lie back and take it."
            "Then I feel the sensation of her ass clamping down on my cock!"
            mike.say "Wha..."
            mike.say "How are you..."
            "There's no answer from Harmony, just a knowing smile."
            "And then another squeeze of her muscles."
            "Which is more than enough for me to get the message."
            "Harmony wants me to fuck her, and she's not going to wait for it to happen either!"
            "Spurred into action, I begin to thrust back and forth in earnest."
            "Putting all of my energy into doing what Harmony wants."
            "At first I feel like she's watching me closely."
            "Making sure that I do as I'm told."
            "But soon my efforts seem to be paying off, and she begins too relax."
            "Her eyes glazing over from the pleasure she's feeling, Harmony sags backwards."
            "And she'd likely have collapsed onto her back were it not for Lexi."
            "The other girl supports her diligently, but doesn't remain passive."
            "Instead I watch as Lexi's hands start to explore Harmony's body."
            "Helpless to resist, she can only gasp and moan as she's played with."
            "Lexi pinches her nipples, squeezes her breasts and even sliding fingers her pussy."
            "All the time I'm still pounding away at Harmony as hard as I possibly can."
            "And while she seems to be melting in our hands, one part of her is coming alive."
            "Where before she was using her muscles to clench on me, they're now going haywire."
            "I take it as a sign that Harmony is on the verge of losing it."
            "And that I need to decide where I'm going to be when I lose it too."
            menu:
                "Cum inside ass":
                    "Trusting Lexi to hold onto her, I keep right on going."
                    with vpunch
                    "I thrust my cock in and out of Harmony until the very end."
                    with vpunch
                    "And when I feel myself about to cum, I push in as deep as I can."
                    show goodevil threesome harmonyfuck creampie
                    "This means that Lexi takes all of it, nothing held back."
                    "Now she really does seem to collapse into a helpless mess."
                    "Quivering and quaking in the grip of Lexi and myself."
                "Pull out of ass":
                    "Trusting Lexi to hold onto her, I pull my cock out of Harmony."
                    if randint(0, 100) <= 25:
                        menu:
                            "The girls seem to have something in mind":
                                call goodevil_threesome_cumshare (from_girl="harmony", location=location) from _call_goodevil_threesome_cumshare_2
                            "Cum on Harmony":
                                show goodevil threesome harmonyfuck out with vpunch
                                "She lets out a long moan as it happens, unable to stop herself."
                                show goodevil threesome harmonyfuck out cumshot with vpunch
                                "Then I shoot my load over the curves of Harmony's exposed body."
                                with vpunch
                                "Now she really does seem to collapse into a helpless mess."
                                "Quivering and quaking in the grip of Lexi and myself."
                                "Sweat mixing with everything else running over her body."
                    else:
                        show goodevil threesome harmonyfuck out with vpunch
                        "She lets out a long moan as it happens, unable to stop herself."
                        show goodevil threesome harmonyfuck out cumshot with vpunch
                        "Then I shoot my load over the curves of Harmony's exposed body."
                        with vpunch
                        "Now she really does seem to collapse into a helpless mess."
                        "Quivering and quaking in the grip of Lexi and myself."
                        "Sweat mixing with everything else running over her body."
            $ harmony.flags.anal += 1
    $ harmony.sexperience += 1
    $ harmony.love += 2
    return

label goodevil_threesome_fuck_lexi(location="trailer"):
    "I can see that Lexi's totally distracted by the kiss she's sharing with Harmony."
    "So I take it as the perfect opportunity to sneak up behind her and get into position."
    "Lexi's actually a little closer to getting onto the table than Harmony when I catch her."
    "She's on her tip-toes, one leg raised and her thighs a good distance apart."
    "This means that when I slap my hands on her waist, she's in a perfect position."
    "Had I been grabbing Harmony, I'd have expected her to let out a squeal at the very least."
    "And the girls might be pretty well matched when it comes to the size of their libidos."
    "But when it comes to experience, Lexi wins, hands down."
    "That means she still has the presence of mind to know just what's happening."
    "Lexi doesn't leap or flinch in my grasp."
    "Instead she simply turns her head to look back over her shoulder."
    scene bg black
    $ renpy.show(f"goodevil threesome lexifuck {location}")
    with fade
    lexi.say "Okay, [hero.name]..."
    lexi.say "So you caught me."
    lexi.say "Now what are you going to do with me, huh?"
    "I'm about to act on my instincts and answer Lexi's question."
    "But before I can make my move, she moans and turns her gaze away from me."
    "And that's because Harmony seems to have taken full advantage of her distraction."
    "Rather than simply kissing the other girl, her hands are now all over Lexi's body."
    "Harmony is exploring every line and curve, right in front of me."
    "The sight is a massive turn-on, and the effects plain to see."
    "I could quite happily stand here and watch this all play out."
    "But there's already almost an ache down there, distracting me the whole time."
    "And what better way to deal with it than to stick the offending organ into Lexi?"
    menu:
        "Fuck her pussy":
            "Lexi's legs are still spread wide enough for me to be able to get easy access."
            "And I can choose whatever hole happens to take my fancy."
            "But as I work my cock between her thighs, I feel it slide against her pussy."
            "Lexi's lips are already warm and more than a little slick."
            "All of which means she's pretty excited and almost ready for me."
            "That realisation makes me forget all about her other holes."
            "And I begin to stroke the head of my cock back and forth against her."
            "Each pass up and down those soft, wet lips seems to affect Lexi a little more."
            "At first she merely shakes a bit, making a whimpering sound."
            "But soon enough she's wriggling and writhing more with each pass."
            "And her whimpers have turned into full-on moans of pleasure."
            lexi.say "Ah..."
            lexi.say "Oh yeah..."
            lexi.say "Stop teasing me..."
            lexi.say "Give it to me already!"
            "It's not like I need the encouragement to get on with the task at hand."
            "Yet I still feel a sudden urge to try harder as Lexi's words ring in my ears."
            "And all it takes is a step up in intensity and speed on my part."
            "That's more than sufficient to make things start happening down there."
            show goodevil threesome lexifuck vaginal
            "After only a couple more thrusts back and forth, I feel something change."
            "Where before they were pressed tight together, now Lexi's lips begin to part."
            "Just a little at first, no more than a fraction of an inch."
            "But that's all I need to be able to begin slipping inside."
            "Each subsequent push sees her open wider and me go deeper."
            "Until, all at once, there's nothing left to stop me."
            "The entire length of my cock sinks straight into Lexi."
            "And I don't stop until I feel her buttocks slap against my groin."
            with vpunch
            "Lexi's climbing upwards now, trying to get onto the counter."
            "But as that would lift her off of me, I can't her succeed."
            "Tightening my grip on her, I pull Lexi down as I push myself upwards."
            "This all but impales her on my cock, leaving her no hope of escape."
            "And it also puts her at the perfect angle for me to take advantage."
            "If I was trying hard before, I put everything I have into it now."
            "Trapped in that spot, all Lexi can do is hold on and take it."
            "My cock thrusting in and out of her alone would have been enough."
            "More than sufficient to get the job done."
            "Yet Lexi also has to contend with what Harmony's doing at the same time."
            "All the while, the other girl's attentions haven't wavered or wandered."
            "If anything, they seem to have become even more intense as Lexi's become more helpless."
            with vpunch
            "And between us, we're working her into a state of total ecstasy."
            "I can tell that from the way Lexi's starting to move."
            "Then way she's wriggling on my cock."
            "And I know it won't be too long before she cums."
            "But from what I'm feeling down there, it won't be long for me either!"
            menu:
                "Cum inside her":
                    "I keep my hold on Lexi and just push on to the end."
                    with hpunch
                    "This means that when I finally lose it, I'm deep inside of her."
                    show goodevil threesome lexifuck cum with hpunch
                    "And she takes all that I have to give, nothing held back."
                    with hpunch
                    "Lexi practically claws at the counter, scrabbling for purchase."
                    "But no matter how she tries, she can't escape my orgasm or her own."
                "Pull out":
                    "I make sure to keep a tight hold on Lexi as I pull out of her."
                    if randint(0, 100) <= 25:
                        menu:
                            "The girls seem to have something in mind":
                                call goodevil_threesome_cumshare (from_girl="lexi", location=location) from _call_goodevil_threesome_cumshare_1
                            "Cum on Lexi":
                                show goodevil threesome lexifuck -vaginal
                                "And as soon as I do so, she moans at the sensation."
                                with hpunch
                                "Collapsing forwards, she practically claws at the counter."
                                with hpunch
                                "Her orgasm rendering her totally helpless as I cum too."
                                show goodevil threesome lexifuck cum with hpunch
                                "Shooting my load over her exposed back and buttocks."
                    else:
                        show goodevil threesome lexifuck -vaginal
                        "And as soon as I do so, she moans at the sensation."
                        with hpunch
                        "Collapsing forwards, she practically claws at the counter."
                        with hpunch
                        "Her orgasm rendering her totally helpless as I cum too."
                        show goodevil threesome lexifuck cum with hpunch
                        "Shooting my load over her exposed back and buttocks."
        "Fuck her ass":
            show goodevil threesome lexifuck
            "Lexi's legs are still spread wide enough for me to be able to get easy access."
            "And I can choose whatever hole happens to take my fancy."
            "But as I work my cock between her thighs, I feel it jam in the cheeks of her ass."
            "Lexi's buttocks are already warm and more than a little slick."
            "All of which means she's pretty excited and almost ready for me."
            "That realisation makes me forget all about her other holes."
            "And I begin to stroke the head of my cock back and forth against her."
            "Each pass up and down those soft, welcoming buttocks seems to affect Lexi a little more."
            "At first she merely shakes a bit, making a whimpering sound."
            "But soon enough she's wriggling and writhing more with each pass."
            "And her whimpers have turned into full-on moans of pleasure."
            lexi.say "Ah..."
            lexi.say "Oh yeah..."
            lexi.say "Stop teasing me..."
            lexi.say "Give it to me already!"
            "It's not like I need the encouragement to get on with the task at hand."
            "Yet I still feel a sudden urge to try harder as Lexi's words ring in my ears."
            "And all it takes is a step up in intensity and speed on my part."
            "That's more than sufficient to make things start happening down there."
            "After only a couple more thrusts back and forth, I feel something change."
            "Where before they were pressed tight together, now Lexi's muscles begin to relax."
            "Just a little at first, no more than a fraction of an inch."
            "But that's all I need to be able to begin slipping inside."
            "Each subsequent push sees her open wider and me go deeper."
            "Until, all at once, there's nothing left to stop me."
            show goodevil threesome lexifuck anal
            "The entire length of my cock sinks straight into Lexi."
            "And I don't stop until I feel her buttocks slap against my groin."
            "Lexi's climbing upwards now, trying to get onto the counter."
            "But as that would lift her off of me, I can't her succeed."
            "Tightening my grip on her, I pull Lexi down as I push myself upwards."
            "This all but impales her on my cock, leaving her no hope of escape."
            "And it also puts her at the perfect angle for me to take advantage."
            "If I was trying hard before, I put everything I have into it now."
            "Trapped in that spot, all Lexi can do is hold on and take it."
            "My cock thrusting in and out of her alone would have been enough."
            "More than sufficient to get the job done."
            "Yet Lexi also has to contend with what Harmony's doing at the same time."
            "All the while, the other girl's attentions haven't wavered or wandered."
            "If anything, they seem to have become even more intense as Lexi's become more helpless."
            "And between us, we're working her into a state of total ecstasy."
            "I can tell that from the way Lexi's starting to move."
            "Then way she's wriggling on my cock."
            "And I know it won't be too long before she cums."
            "But from what I'm feeling down there, it won't be long for me either!"
            menu:
                "Cum in ass":
                    with hpunch
                    "I keep my hold on Lexi and just push on to the end."
                    show goodevil threesome lexifuck cum with hpunch
                    "This means that when I finally lose it, I'm deep inside of her."
                    with hpunch
                    "And she takes all that I have to give, nothing held back."
                    "Lexi practically claws at the counter, scrabbling for purchase."
                    "But no matter how she tries, she can't escape my orgasm or her own."
                "Pull out":
                    show goodevil threesome lexifuck out
                    "I make sure to keep a tight hold on Lexi as I pull out of her."
                    with hpunch
                    "And as soon as I do so, she moans at the sensation."
                    show goodevil threesome lexifuck cum with hpunch
                    "Collapsing forwards, she practically claws at the counter."
                    with hpunch
                    "Her orgasm rendering her totally helpless as I cum too."
                    "Shooting my load over her exposed back and buttocks."
            $ lexi.flags.anal += 1
    $ lexi.sexperience += 1
    $ lexi.love += 2
    return


label goodevil_threesome_cumshare(from_girl="lexi", location="trailer"):
    if from_girl == "lexi":
        "At the very last moment, just before I shoot my load, Harmony grabs hold of it."
    else:
        "At the very last moment, just before I shoot my load, Lexi grabs hold of it."
    "In fact she grabs hold of it so hard and so fast that I'm stopped in my tracks."
    "All thought of shooting my load vanishes as I struggle to see what's going on."
    "Because Lexi and Harmony are already moving here and there, intent on some secret plan."
    mike.say "Huh..."
    mike.say "What are you..."
    "Before I can get the question out, they've taken me by the hand."
    "And together they practically shove me up and onto the counter."
    "There's no time for me to even ask what's happening."
    scene bg black
    $ renpy.show(f"goodevil threesome cumshare {location}")
    "As they both lean in close, putting their heads on level with my waist."
    "And then they start to put their hands on my cock too."
    "Harmony and Lexi work me like a pair of professionals."
    "Like a team that's totally on the same page."
    "They don't seem to even need to talk to each other."
    "Instead they just get down to it and work me into a state of helpless pleasure."
    "Soon enough they lean in closer, bringing lips, tongues and teeth into play."
    "And they're just as good at working together in this way too."
    "It's hard for me to tell which of them is doing what at any one time."
    "Add to this the fact I spend most of the time this lasts with my eyes closed."
    "Simply because I can't bring myself to look down at what they're doing."
    "All for fear that it'll make me lose it."
    "But I needn't have worried, because they have a plan for that too."
    "At the first sign of me approaching my orgasm for a second time, they pull back."
    "Harmony and Lexi kneel in front of me on the counter, patiently waiting."
    show goodevil threesome cumshare cumshot with vpunch
    "Their mouths are open and they're looking up at me intently."
    with vpunch
    "So when I do shoot my load, it falls directly on their faces."
    with vpunch
    "I watch as they giggle with delight, licking up every drop they can."
    $ harmony.love += 1
    $ lexi.love += 1
    return

label goodevil_harem_fuck_date(appointment=None):
    call goodevil_threesome from _call_goodevil_threesome_1
    return

label goodevil_threesome_mikebedroom:
    scene bg house with fade
    "I feel like a fool as I sneak up the path to the porch and then to the front door of the house."
    "Partly because it seems so crazy to be trying not to be spotted going into my own home."
    "And probably a lot more on account of the fact that my companions aren't even trying to help."
    show harmony with easeinleft
    harmony.say "Why are you crouching down like that, [hero.name]?"
    harmony.say "I thought you said your housemates were out tonight?"
    "I know that Harmony's not speaking any louder than normal as she asks her questions."
    "But to me it sounds like she's shouting at the top of her voice."
    mike.say "I know that's what I said, Harmony..."
    mike.say "But there's still a chance one of them could have come home early."
    show harmony at left
    with ease
    show lexi at right
    with easeinright
    lexi.say "Huh..."
    lexi.say "Sounds to me like you embarrassed to be seen with us!"
    "Unlike Harmony, Lexi really is speaking more loudly than she needs to."
    "And I already know that it's deliberate, in response to my trying to sneak around."
    mike.say "Shh!"
    mike.say "Keep it down, Lexi..."
    mike.say "You're going to wake the entire street!"
    show lexi b sad
    "Lexi instantly starts to sulk as I say this."
    "Tutting and shaking her head as she follows on my heels."
    lexi.say "I still say that we should have gone to my place."
    lexi.say "I make all the noise I like there and nobody ever complains."
    "From the way that she's laying into me right now, that doesn't seem hard to believe."
    "But I push those concerns aside as I reach the front door and hastily open it."
    scene bg livingroom with fade
    show lexi at right
    show harmony at left
    with easeinleft
    "Harmony and Lexi slip inside, and then I close and lock it behind us."
    "Then I make straight for another door - specifically the one to my bedroom."
    "Harmony seems eager to get inside, but Lexi lingers in the doorway."
    lexi.say "Hey..."
    lexi.say "Why can't we do it out here?"
    lexi.say "We got the whole place to ourselves."
    scene bg bedroom1 with fade
    show lexi at right
    show harmony at left
    with easeinleft
    "By way on answer, I grab hold of her wrist and pull her into my room."
    lexi.say "Hey!"
    mike.say "Just get in here, Lexi."
    mike.say "I won't feel safe until you're both in here with me."
    show harmony surprised
    harmony.say "Ooh..."
    show harmony happy
    harmony.say "This is nice!"
    hide harmony with dissolve
    play sound "<from 0 to 1.0>sd/SFX/house/bed_jump.ogg" fadeout 0.2
    "Suddenly the sound of mattress springs squeaking and a bedframe straining fills the air."
    scene bg bedroom1 at center, zoomAt(2.5, (1540, 1240))
    show harmony happy at center, zoomAt(1.5, (640, 940))
    with fade
    "As one, Lexi and I turn to see that Harmony is pretty much ignoring our squabbling."
    play sound "<from 0 to 1.0>sd/SFX/house/bed_jump.ogg" fadeout 0.2
    show harmony at startle(0.14,-60)
    pause 0.1
    show harmony at startle(0.10, 20)
    pause 0.2
    show harmony at startle(0.14,-30)
    pause 0.1
    show harmony at startle(0.05, 10)
    "In fact she's already made it to my bed, as we can see from a trail of her discarded clothes."
    play sound "<from 0 to 1.0>sd/SFX/house/bed_jump.ogg" fadeout 0.2
    show harmony at startle(0.14,-60)
    pause 0.1
    show harmony at startle(0.10, 20)
    pause 0.2
    show harmony at startle(0.14,-30)
    pause 0.1
    show harmony at startle(0.05, 10)
    "And now she's testing out the properties of my mattress, which would explain all of the sounds."
    "Believe me, it's quite a sight too."
    play sound "<from 0 to 1.0>sd/SFX/house/bed_jump.ogg" fadeout 0.2
    show harmony at startle(0.14,-60)
    pause 0.1
    show harmony at startle(0.10, 20)
    pause 0.2
    show harmony at startle(0.14,-30)
    pause 0.1
    show harmony at startle(0.05, 10)
    "Lexi and I are held spellbound as we watch Harmony bouncing up and down on my bed."
    "I mean, it's pretty easy to see that there's a lot of her to do the bouncing."
    play sound "<from 0 to 1.0>sd/SFX/house/bed_jump.ogg" fadeout 0.2
    show harmony at startle(0.14,-60)
    pause 0.1
    show harmony at startle(0.10, 20)
    pause 0.2
    show harmony at startle(0.14,-30)
    pause 0.1
    show harmony at startle(0.05, 10)
    "But until you actually see all of it in motion..."
    "Well, it's pretty hard to put into words just how the sight affects a person!"
    mike.say "Yeah, Harmony..."
    mike.say "It looks pretty nice from where I'm standing too!"
    scene bg bedroom1
    show lexi flirt at right
    show harmony happy at left
    with fade
    lexi.say "Fuck me, [hero.name]..."
    lexi.say "What were we arguing about again?"
    mike.say "Beat's me, Lexi..."
    mike.say "But I don't think it matters anymore!"
    show lexi topless at center with ease
    "As one, we dash across the room, already tearing off our own clothes."
    "And we reach the bed at almost the same moment, leaping towards Harmony."
    "At the last moment, she looks up in surprise."
    show harmony surprised
    harmony.say "Oh..."
    harmony.say "Oh my!"
    "Lexi and I land on the bed together."
    "And for a second I hold my breath, thinking that it's going to break under our weight."
    "But when it doesn't, I make my move, pouncing on Harmony."
    "She lets out a cry of delight as Lexi does the same thing."
    "And together, the three of us descend into a tangle of limbs on the bed."
    menu:
        "Fuck Harmony":
            call goodevil_threesome_mikebedroom_fuck_harmony from _call_goodevil_threesome_mikebedroom_fuck_harmony
        "Fuck Lexi":
            call goodevil_threesome_mikebedroom_fuck_lexi from _call_goodevil_threesome_mikebedroom_fuck_lexi
    call goodevil_threesome_mikebedroom_end from _call_goodevil_threesome_mikebedroom_end
    return

label goodevil_threesome_mikebedroom_fuck_harmony:
    "I make a grab for Harmony, meaning to try lining her up for what I have in mind."
    "But in all the confusion that's going on, I have no idea where I am."
    "So it should probably come as no surprise to me that I totally miss my target."
    play sound body_fall
    "Though perhaps falling off the bed altogether is a little more vexing."
    "I hear Lexi laughing at me as I tumble onto the floor."
    "But I pop right back up again, determined to make the best of the situation."
    "As soon as I'm upright once more, I see a chance to make this work for me."
    "Because Harmony is sitting up on the bed right now, facing towards me."
    show goodevil threesome harmonyfuck bedroom
    "Quick as a flash, I grab hold of her thighs and part them."
    "And then I position myself right in the middle, pulling her towards me."
    "I'm at the perfect height to push my cock between her formidable thighs."
    "So within seconds I'm ready to take things to the next stage."
    "For her part, Harmony looks up at me."
    "Her cheeks are flushed red and her eyes wide."
    "And she nods her head, just enough to let me know what she wants it."
    "From that point on, it's a done deal."
    "Harmony's the one that's going to get it."
    "And nothing is going to stop me making that happen."
    menu:
        "Fuck her pussy":
            "The moment I feel the head of my cock against Harmony's pussy, my mind's made up."
            "It's like something clicks inside of my head and makes me want to be inside of her."
            "Pulling her closer, I press it even harder against the folds of her pussy."
            "As I do so, Harmony's torso is jerked backwards, almost flopping onto the bed."
            "But that's when Lexi chooses to step in, catching Harmony and holding her up."
            harmony.say "Oh..."
            harmony.say "Lexi..."
            harmony.say "There you are!"
            "Lexi doesn't respond to a word that the other girl says."
            "Instead she proceeds to take full advantage of her helpless state."
            "In the blink of an eye, Lexi's hands are all over Harmony."
            "She strokes, squeezes and pinches every part of that voluptuous body too."
            "The sight of it and the effect it has on Harmony seriously turning me on."
            harmony.say "Ah..."
            harmony.say "Oh shit..."
            harmony.say "Fuck me, [hero.name]..."
            harmony.say "Please?"
            "Now how can I resist an plea like that?"
            "Thrusting myself forwards, I find that Lexi's lent me a hand too."
            show goodevil threesome harmonyfuck vaginal
            "This time the head of my cock slithers and slides over Harmony's pussy."
            "In fact she's so wet and helpless that it begins to sink in right away."
            "All I have to do is keep on pushing, and I feel myself sinking into her."
            "As this is happening, Harmony's words melt away, losing all meaning."
            "Instead she begins to moan, nodding her head to urge me on."
            "As soon as I can't get any deeper into her, I begin to move back and forth."
            "There's no time for being subtle or taking my time here."
            "I simply start to thrust in and out of Harmony for all I'm worth."
            "This seems to be exactly what she wants too."
            "The sounds of her moaning become louder and even less coherent."
            "And her head bobs back and forth atop her neck the whole time."
            "Lexi isn't idle either, continuing to caress Harmony's helpless form."
            "Together we set about using her to indulge our deepest desires."
            "And in doing so we pleasure Harmony at the same time too."
            "By now her eyes have almost rolled back into her head."
            "All that's keeping her upright is Lexi's support."
            "And the full curves of her body are jiggling like crazy."
            "Part of me wants to keep this going for as long as possible."
            "To see just how far we can push Harmony before everyone is exhausted."
            "But suddenly I begin to feel the sensation of her pussy twitching around my cock."
            "The movement seems to spread out, affecting the rest of her body as well."
            "And it's then that I know Harmony is on the brink of cuming."
            "Though it's not just her that's being getting there."
            "The way she's squeezing means that I'm being taken along for the ride!"
            menu:
                "Cum inside":
                    "Relying on Lexi to hold Harmony in place, I quicken my pace."
                    with hpunch
                    "Using the last of my strength, I redouble my efforts too."
                    show goodevil threesome harmonyfuck creampie with hpunch
                    "This means that Harmony and I cum almost in the same second."
                    with hpunch
                    "Buried as deep in her as possible, I let go with everything I have."
                    "And it seems like her orgasm is that much more intense as a result."
                "Pull out":
                    "Relying on Lexi to hold Harmony up, I drag my cock out of her."
                    "This causes her to let out a deep, sensual moan at the sensation."
                    with hpunch
                    "And it also pushes Harmony over the edge as well."
                    show goodevil threesome out cumshot with hpunch
                    "I gasp as I shoot my load over the curves of her breasts and belly."
                    with hpunch
                    "All the time watching as Harmony quivers and quakes from her own climax."
                "Cum on their faces":
                    call goodevil_threesome_mikebedroom_double_oral_finish from _call_goodevil_threesome_mikebedroom_double_oral_finish
        "Fuck her ass":
            "The moment I feel the head of my cock jam between Harmony's butt cheeks, my mind's made up."
            "It's like something clicks inside of my head and makes me want to be inside of her ass."
            "Pulling her closer, I jam it even deeper between her buttocks."
            "As I do so, Harmony's torse is jerked backwards, almost flopping onto the bed."
            "But that's when Lexi chooses to step in, catching Harmony and holding her up."
            harmony.say "Oh..."
            harmony.say "Lexi..."
            harmony.say "There you are!"
            "Lexi doesn't respond to a word that the other girl says."
            "Instead she proceeds to take full advantage of her helpless state."
            "In the blink of an eye, Lexi's hands are all over Harmony."
            "She strokes, squeezes and pinches every part of that voluptuous body too."
            "The sight of it and the effect it has on Harmony seriously turning me on."
            harmony.say "Ah..."
            harmony.say "Oh shit..."
            harmony.say "Fuck me, [hero.name]..."
            harmony.say "Please?"
            "Now how can I resist an plea like that?"
            "Thrusting myself forwards, I find that Lexi's lent me a hand too."
            show goodevil threesome harmonyfuck anal
            "This time the head of my is right up against the hole of Harmony's ass."
            "In fact she's so wet and helpless that it begins to sink in right away."
            "All I have to do is keep on pushing, and I feel myself sinking into her."
            "As this is happening, Harmony's words melt away, losing all meaning."
            harmony.say "M...my ass..."
            harmony.say "Mmm...my..ass..."
            "Instead she begins to moan, nodding her head to urge me on."
            "As soon as I can't get any deeper into her, I begin to move back and forth."
            "There's no time for being subtle or taking my time here."
            "I simply start to thrust in and out of Harmony for all I'm worth."
            "This seems to be exactly what she wants too."
            "The sounds of her moaning become louder and even less coherent."
            "And her head bobs back and forth atop her neck the whole time."
            "Lexi isn't idle either, continuing to caress Harmony's helpless form."
            "Together we set about using her to indulge our deepest desires."
            "And in doing so we pleasure Harmony at the same time too."
            "By now her eyes have almost rolled back into her head."
            "All that's keeping her upright is Lexi's support."
            "And the full curves of her body are jiggling like crazy."
            "Part of me wants to keep this going for as long as possible."
            "To see just how far we can push Harmony before everyone is exhausted."
            "But suddenly I begin to feel the sensation of her muscles twitching around my cock."
            "The movement seems to spread out, affecting the rest of her body as well."
            "And it's then that I know Harmony is on the brink of cuming."
            "Though it's not just her that's being getting there."
            "The way she's squeezing means that I'm being taken along for the ride!"
            menu:
                "Cum inside":
                    "Relying on Lexi to hold Harmony in place, I quicken my pace."
                    with hpunch
                    "Using the last of my strength, I redouble my efforts too."
                    show goodevil threesome harmonyfuck creampie with hpunch
                    "This means that Harmony and I cum almost in the same second."
                    with hpunch
                    "Buried as deep in her as possible, I let go with everything I have."
                    "And it seems like her orgasm is that much more intense as a result."
                "Pull out":
                    "Relying on Lexi to hold Harmony up, I drag my cock out of her."
                    "This causes her to let out a deep, sensual moan at the sensation."
                    with hpunch
                    "And it also pushes Harmony over the edge as well."
                    show goodevil threesome harmonyfuck out cumshot with hpunch
                    "I gasp as I shoot my load over the curves of her breasts and belly."
                    with hpunch
                    "All the time watching as Harmony quivers and quakes from her own climax."
                "Cum on their faces":
                    call goodevil_threesome_mikebedroom_double_oral_finish from _call_goodevil_threesome_mikebedroom_double_oral_finish_1
    return

label goodevil_threesome_mikebedroom_fuck_lexi:
    "I'm thinking that the obvious thing here would be to make a grab for Harmony."
    "After all, Lexi and I were just hypnotised by the sight of her bouncing on my bed."
    "But I see that Lexi's already doing all she can to get her hands on the other girl."
    "So I decide to take a different approach, sliding off the bed."
    "As Lexi and Harmony meet in the middle, I pop up behind the former."
    "And as they begin to exchange a kiss, I pull her backwards."
    show goodevil threesome lexifuck bedroom
    "This seems to take Lexi by complete surprise, breaking her away from Harmony."
    lexi.say "Huh?"
    lexi.say "What are you..."
    lexi.say "Oh...oh fuck!"
    "For a moment I'm surprised too, not knowing what's happened to Lexi."
    "But then I look down and see a hand between her thighs."
    "The fingers of which are massaging Lexi's exposed pussy!"
    "As soon as I look up, I see Harmony gazing straight at me."
    harmony.say "Mmm..."
    harmony.say "She feels so nice and wet down there, [hero.name]."
    harmony.say "Like she's almost ready for you!"
    "I can't keep a smile from spreading across my face at this."
    "And Harmony smiles too, urging me on to do what comes next."
    "But it's not like I need that much encouragement."
    "My hands are all over Lexi's body the very next instant."
    "I don't hesitate to caress every part of her that I can reach."
    "Though I confess that as soon as I reach her breasts, my hands stay there."
    "As I massage them, working the nipples so they harden, Lexi lets out a helpless moan."
    "At the same time, Harmony keeps me appraised of what's going on down below."
    harmony.say "Ooh..."
    harmony.say "She's getting hotter and softer!"
    harmony.say "Almost like she's melting in the palm of my hand."
    harmony.say "I think you should put it in her soon, [hero.name]!"
    "Lexi's head sways and bobs as Harmony says this."
    "And I realise that she's nodding."
    "Trying to make me act on the other girl's words."
    menu:
        "Fuck her pussy":
            "Knowing that Lexi wants it as badly as me serves the spur me on."
            "And so I don't hesitate to thrust my cock straight between her thighs."
            "As I do so, the head slides over the lips of her pussy."
            "This makes Lexi moan all over again, and it sends a shiver through her entire body."
            "But in the same moment I'm discovering just how right Harmony was."
            "Lexi's pussy is wetter, hotter and softer than I've ever felt it before."
            "In fact it really does feel like she's melting!"
            "Practically all I have to do is line myself up."
            show goodevil threesome lexifuck vaginal
            "Then as soon as I begin to move forwards, her lips part for me."
            "I'm tempted to thrust myself straight into Lexi."
            "To get as deep as I possibly can and begin pounding her."
            "But somehow I manage to hold myself back and take my time."
            "This means that I get to enjoy the sensation of sinking in slowly."
            "Feeling every inch of my cock as it pushes inside."
            "The decision seems to be one that Lexi approves of too."
            "I can feel her trying as best she can to keep still the whole time."
            "It's like she wants to pull me deeper, to throw herself backwards onto me."
            "And yet her nerve holds, just like mine."
            lexi.say "Yeah..."
            lexi.say "M...more..."
            lexi.say "I want...more!"
            "Just as Lexi finishes making her demand, I feel myself come to a halt."
            "There's nowhere else for me to go, and so she's asking at the perfect time."
            "I've satisfied my need to go slowly and indulge my more refined sensibilities."
            "So now I can just give way to the more animalistic urges that have been building up inside of me."
            "And that means that I instantly start to move inside of Lexi."
            "My first thrust almost sends her sprawling onto the bed."
            "It's only Harmony catching Lexi and holding her up that prevents it."
            "But I don't let that stop me for a moment, trusting to the other girl to keep it up."
            "Now there's nothing to make me hold back, and I give Lexi everything that I've got."
            "Where before I was going slowly, now I make an effort to go as fast as I can."
            "Plus I'm sure to be as hard and forceful as I think she can take."
            "I do this because I know Lexi well enough to be sure it's what she wants."
            "And when she wants something, she expects to get it too."
            "Almost from the start I know that I'm right."
            "Because Lexi's body responds in kind almost as soon as I begin."
            "She makes no effort to escape, instead pushing herself back against me."
            "And she soaks up everything that I give her too, then demands more."
            "What was an intense and drawn-out experience for me becomes a blur."
            "Sensation and movement are the only things that seem to exist in the moment."
            "And time becomes a strange concept that has almost no meaning."
            "Only when those sensations begin to change do I become aware of myself again."
            "The subtle changes in Lexi's body that tell me the end is fast approaching."
            "And the echoes that they create in my own as a result."
            "Once that happens, I know that there's not long left."
            "One of us is going to cum any second!"
            menu:
                "Cum inside":
                    "All of this speed and force means that I can't even think of stopping."
                    with hpunch
                    "So I don't, I just keep on going until the moment that I lose it."
                    show goodevil threesome lexifuck cum with hpunch
                    "Then I shoot my load as deep into Lexi as possible."
                    with hpunch
                    "The effect is instant and explosive, making her cum too."
                    "And then the two of us all but collapse atop Harmony."
                "Pull out":
                    show goodevil threesome lexifuck out
                    "I use the last of my strength and control to pull out before the end."
                    "But still I feel like I cum the moment that my cock pops out of her."
                    with hpunch
                    "Lexi collapses atop Harmony, sending them both sprawling onto the bed."
                    show goodevil threesome lexifuck cum with hpunch
                    "And then I shoot my load over her back and buttocks."
                    with hpunch
                    "Striping them with sticky, white lines."
                "Cum on their faces":
                    call goodevil_threesome_mikebedroom_double_oral_finish from _call_goodevil_threesome_mikebedroom_double_oral_finish_2
        "Fuck her ass":
            "Knowing that Lexi wants it as badly as me serves the spur me on."
            "And so I don't hesitate to thrust my cock straight between her butt cheeks."
            "As I do so, the head slides around her hole."
            "This makes Lexi moan all over again, and it sends a shiver through her entire body."
            "Harmony might have been on the money when it comes to Lexi's pussy."
            "But right now all I'm interested in is her ass."
            "It really does feel like she's melting!"
            "Practically all I have to do is line myself up."
            show goodevil threesome lexifuck anal
            "Then as soon as I begin to move forwards, her muscles part for me."
            "I'm tempted to thrust myself straight into Lexi."
            "To get as deep as I possibly can and begin pounding her."
            "But somehow I manage to hold myself back and take my time."
            "This means that I get to enjoy the sensation of sinking in slowly."
            "Feeling every inch of my cock as it pushes inside."
            "The decision seems to be one that Lexi approves of too."
            "I can feel her trying as best she can to keep still the whole time."
            "It's like she wants to pull me deeper, to throw herself backwards onto me."
            "And yet her nerve holds, just like mine."
            lexi.say "Yeah..."
            lexi.say "M...more..."
            lexi.say "I want...more!"
            "Just as Lexi finishes making her demand, I feel myself come to a halt."
            "There's nowhere else for me to go, and so she's asking at the perfect time."
            "I've satisfied my need to go slowly and indulge my more refined sensibilities."
            "So now I can just give way to the more animalistic urges that have been building up inside of me."
            "And that means that I instantly start to move inside of Lexi."
            "My first thrust almost sends her sprawling onto the bed."
            "It's only Harmony catching Lexi and holding her up that prevents it."
            "But I don't let that stop me for a moment, trusting to the other girl to keep it up."
            "Now there's nothing to make me hold back, and I give Lexi everything that I've got."
            "Where before I was going slowly, now I make an effort to go as fast as I can."
            "Plus I'm sure to be as hard and forceful as I think she can take."
            "I do this because I know Lexi well enough to be sure it's what she wants."
            "And when she wants something, she expects to get it too."
            "Almost from the start I know that I'm right."
            "Because Lexi's body responds in kind almost as soon as I begin."
            "She makes no effort to escape, instead pushing herself back against me."
            "And she soaks up everything that I give her too, then demands more."
            "What was an intense and drawn-out experience for me becomes a blur."
            "Sensation and movement are the only things that seem to exist in the moment."
            "And time becomes a strange concept that has almost no meaning."
            "Only when those sensations begin to change do I become aware of myself again."
            "The subtle changes in Lexi's body that tell me the end is fast approaching."
            "And the echoes that they create in my own as a result."
            "Once that happens, I know that there's not long left."
            "One of us is going to cum any second!"
            menu:
                "Cum inside":
                    "All of this speed and force means that I can't even think of stopping."
                    with hpunch
                    "So I don't, I just keep on going until the moment that I lose it."
                    show goodevil threesome lexifuck cum with hpunch
                    "Then I shoot my load as deep into Lexi as possible."
                    with hpunch
                    "The effect is instant and explosive, making her cum too."
                    "And then the two of us all but collapse atop Harmony."
                "Pull out":
                    show goodevil threesome lexifuck out
                    "I use the last of my strength and control to pull out before the end."
                    "But still I feel like I cum the moment that my cock pops out of her."
                    with hpunch
                    "Lexi collapses atop Harmony, sending them both sprawling onto the bed."
                    show goodevil threesome lexifuck cum with hpunch
                    "And then I shoot my load over her back and buttocks."
                    with hpunch
                    "Striping them with sticky, white lines."
                "Cum on their faces":
                    call goodevil_threesome_mikebedroom_double_oral_finish from _call_goodevil_threesome_mikebedroom_double_oral_finish_3
    return

label goodevil_threesome_mikebedroom_double_oral_finish:
    "At the very last moment, just before I shoot my load, Lexi grabs hold of my cock."
    "In fact she grabs hold of it so hard and so fast that I almost shoot my load right there and then."
    "But that thought soon vanishes as I struggle to see what's going on."
    "Lexi and Harmony are already moving around on the bed."
    "As if they're putting into action some secret plan."
    mike.say "Huh..."
    mike.say "What are you..."
    show goodevil threesome cumshare bedroom
    "Before I can get the question out, they've taken me by the hand."
    "And together they practically shove me onto the bed."
    "There's no time for me to even ask what's happening."
    "As they both lean in close, heads on level with my waist."
    "And then they start to put their hands on my cock too."
    "Harmony and Lexi work me like a pair of professionals."
    "Like a team that's totally on the same page."
    "They don't seem to even need to talk to each other."
    "Instead they just get down to it and work me into a state of helpless pleasure."
    "Soon enough they lean in closer, bringing lips, tongues and teeth into play."
    "And they're just as good at working together in this way too."
    "It's hard for me to tell which of them is doing what at any one time."
    "Add to this the fact I spend most of the time this lasts with my eyes closed."
    "Simply because I can't bring myself to look down at what they're doing."
    "All for fear that it'll make me lose it."
    "But I needn't have worried, because they have a plan for that too."
    "At the first sign of me approaching my orgasm for a second time, they pull back."
    "Harmony and Lexi kneel in front of me on the counter, patiently waiting."
    "Their mouths are open and they're looking up at me intently."
    show goodevil threesome cumshare cumshot
    "So when I do shoot my load, it falls directly on their faces."
    "I watch as they giggle with delight, licking up every drop they can."
    return

label goodevil_threesome_mikebedroom_end:
    "Once we're done, all I can do is lie back on my bed."
    "Harmony and Lexi seem to be in the same state too."
    "They lie with their limbs tangled in mine, breathing slowly."
    "Neither of them moves or says a single word the whole time."
    "And I begin to think that I could get used to this."
    "Sharing a bed with the two of them, sleeping curled up together too."
    "The only problem would be the need to keep the pair of them satisfied."
    "I don't know if I could manage that on a nightly basis, or if they be the end of me."
    "But even then - what a way to go!"
    $ harmony.sexperience += 1
    $ harmony.love += 2
    $ lexi.sexperience += 1
    $ lexi.love += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
