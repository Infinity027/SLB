init python:
    
    Event(**{
        "name": "ayesha_female_event_01",
        "label": "ayesha_female_event_01",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                HasRoomTag("gym")
                ),
            PersonTarget(ayesha,
                IsPresent(),
                ),
            ],
        "music": "music/roa_music/2am.ogg",
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_gym_coaching",
        "label": "ayesha_gym_coaching",
        "conditions": [
            IsDone("ayesha_female_event_01"),
            HeroTarget(
                IsGender("female"),
                IsFlag("gymmember"),
                HasRoomTag("gym")
                ),
            PersonTarget(ayesha,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 40),
                ),
            ],
        "music": "music/roa_music/2am.ogg",
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_female_event_02",
        "label": "ayesha_female_event_02",
        "conditions": [
            IsDone("ayesha_gym_coaching"),
            HeroTarget(
                IsGender("female"),
                IsFlag("gymmember"),
                HasRoomTag("gym")
                ),
            PersonTarget(ayesha,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 40),
                ),

            ],
        "music": "music/roa_music/2am.ogg",
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_female_event_04",
        "label": "ayesha_female_event_04",
        "conditions": [
            IsDone("ayesha_female_event_03"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("street")
                ),
            PersonTarget(ayesha,
                Not(IsPresent()),
                Not(IsHidden()),
                MinStat("love", 60),
                ),
            ],
        "music": "music/roa_music/2am.ogg",
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_female_event_05",
        "label": "ayesha_female_event_05",
        "conditions": [
            IsDone("ayesha_female_event_04"),
            IsTimeOfDay("evening"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("street")
                ),
            PersonTarget(ayesha,
                Not(IsPresent()),
                Not(IsHidden()),
                MinStat("love", 80),
                ),
            ],
        "music": "music/roa_music/2am.ogg",
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_kiss_me_female",
        "label": "ayesha_kiss_me_female",
        "max_girls": 1,
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(ayesha,
                IsPresent(),
                Not(IsHidden()),
                MinFlag("kiss", 1),
                MinStat("love", 150),
                ),
            ],
        "music": "music/roa_music/2am.ogg",
        "chances": 20,
        "once_day": True,
        "do_once": False,
        "quit": False,
        })

label ayesha_female_event_01:
    show bg gym
    $ ayesha.flags.notrain = True
    if ayesha.love.max < 40:
        $ ayesha.love.max = 40
    "I step into the gym."
    "It’s as crowded as one could expect, but I’ve never really minded."
    "I can make due with whatever’s open; as long as I’m moving, it’s better than the couch.."
    "Near the back corner of the room is an open section of the floor designated for freeweights and medicine balls and yoga mats."
    "That’s my destination, for now, so that I’m more or less out of everyone’s way as I unlock my phone and start browsing my social media for a spontaneous routine."
    "I'm normally pretty much in a world of my own at the gym."
    "Once I put my ear-buds in and get into my routine, that's it."
    show expression AlphaMask("black", At("ayesha b", center)) as mask with dissolve
    "But today I find myself stopping to stare at another girl in the gym."
    "Which is another thing I don't usually do."
    show ayesha b work with dissolve
    "But then you don't often see a girl like this either."
    "She's so tall and muscular, really put together."
    if hero.morality >= 10:
        "Oh my goodness - look at the size of her arms!"
        "I bet she could pick me up and lift me over her head!"
    elif hero.morality <= -10:
        "Wow...I wonder what those muscles would be like to touch."
        "And what she could do to me if I were to let her!"
    "As I'm standing there checking her out, the girl looks up."
    "She must see me, as she narrows her eyes a little."
    "At first I think that she's going to glare at me."
    show ayesha happy
    "But then her expression changes, and she gives me a smile."
    menu:
        "Smile too":
            "I feel a little bad at having been caught starting."
            "But then I realise that she's only just looked up."
            "So she can't have seen me looking at her all this time."
            "And the smile on her face certainly looks friendly."
            "So I smile back, giving her a little nod too."
            $ ayesha.love += 1
        "Hurry away":
            "Oops!"
            "Looks like the big girl caught me staring at her!"
            "She might be smiling at me, but I still feel embarrassed."
            hide ayesha
            hide expression AlphaMask("black", At("ayesha b", center)) as mask
            with dissolve
            "So I tear my eyes away from her as soon as I can."
            "I just hope that she's not mad enough to come over here."
            "Her arms are bigger than [mike.name]'s legs!"
            $ ayesha.sub -= 1
    show expression AlphaMask("black", At("ayesha b", center)) as mask
    show ayesha happy b work
    with dissolve
    "I risk a look back over my shoulder as I hurry away."
    "And I'm a little alarmed to see the girl still watching me."
    hide ayesha b work with dissolve
    "I can't see her face well enough to read her expression."
    "So I have no idea what her intentions towards me might be."
    hide expression AlphaMask("black", At("ayesha b", center)) as mask with dissolve
    "Hopefully she's here to work out as well."
    "That would stop things from getting too awkward."
    "Maybe even keep her from tracking me down too easily."
    "Pretty soon I'm into my workout."
    "And as I get through it, I find myself forgetting all about the girl."
    ayesha.say "Hey there..."
    "I turn back to the woman behind me."
    show ayesha b work normal at right4 with hpunch
    ayesha.say "How are you doing?"
    if hero.morality >= 10:
        bree.say "Oh..."
        bree.say "I...I'm doing okay..."
        bree.say "I guess!"
    elif hero.morality <= -10:
        bree.say "Oh, hey there!"
        bree.say "I'm doing better for seeing you!"
    "If the girl picked up on my mood, she doesn't show it."
    ayesha.say "You using that?"
    bree.say "Oh."
    "She’s stacked, her muscles toned and prominent even beneath what little clothing she’s chosen to wear, and tall -- an Amazonian in the flesh, towering behind me."
    "I’m almost too awestruck and envious of her body for a moment to reply at all, but I catch myself and shake my head."
    bree.say "Oops, sorry, nope. All yours!"
    "I step aside and allow her access to the mat."
    "She’s not doing yoga, I’m almost sure of that."
    show ayesha joke
    pause 0.2
    show ayesha b work normal at left4 with ease
    "She gives me a cursory, polite smile of appreciation before stepping past me and flipping up its end, allowing it to roll in on herself."
    "Something’s tugging at the back of my mind, though, some memory that leaves my gaze lingering on her as she does."
    show ayesha normal
    "For some reason, she looks so familiar to me."
    "I pop out a hip and plant the hand not holding my phone onto it in thought."
    bree.say "Hey, sorry…"
    show ayesha b work normal at center with ease
    "The woman straightens herself with the mat rolled up onto her shoulder, turning back to me curiously."
    "My thumbnail taps against the locked screen of my phone, and I purse my lips slightly."
    "It’s really driving me crazy that I can't place it at all."
    bree.say "Do I know you from somewhere?"
    "She looks me up and down."
    "She’s pretty, though she’s the kind of ‘built’ that I know a lot of girls are afraid of achieving."
    "I remember learning from a personal trainer a while ago, though, not to mention countless fitness gurus online…"
    "A body like hers never happens on ‘accident.’"
    "She works like a machine to look the way she does, I know, and it makes me feel almost intimidated as I stand there under her scrutiny."
    ayesha.say "Can't say."
    "She seems unbothered by the inquiry anyway, and turns to face me."
    show ayesha joke
    ayesha.say "Name’s Ayesha. Ring a bell?"
    "It doesn't, at first, but then it hits me."
    "The hand at my hip flies up as I snap my fingers victoriously."
    bree.say "You wrestle!"
    show ayesha happy
    "Ayesha gives a low chuckle."
    "Something about the sound tells me there isn't a submissive bone in her body."
    ayesha.say "You got me."
    menu:
        "I’m a huge fan!" if hero.knowledge >= 20 and hero.fitness >= 20:
            $ ayesha.love += 1
            bree.say "I knew I recognized you!"
            "Ayesha set the hand not holding the yoga mat onto her hip."
            show ayesha joke
            ayesha.say "Can't say I get recognized all the time. Especially without the mask. Don't I feel like a regular celebrity."
            bree.say "I mean, around here, you practically are!"
            "I catch myself and try to reign it in a little, before I embarrass myself by gushing too much."
            bree.say "I mean, at the College, anyway. You’re all over the walls!"
            ayesha.say "I earned them a little bit of spotlight and a few awards, yeah."
            "I laughed"
            bree.say "A few. I’ve seen you around on so many placards I’m surprised I didn't realize it right away."
            show ayesha happy at startle
            "She breathed a soft laugh, and a crooked smile crossed her full lips."
            ayesha.say "Hey-- don't make me blush here in public."
        "I think you wrestled at my college.":
            bree.say "I remember now. Your face is all over the walls on your awards."
            "Ayesha shifted her weight, obviously just about ready to get back to her workout."
            ayesha.say "I guess I won them a couple, yeah."
        "Not really my thing…":
            $ ayesha.love -= 1
            "The triumphant smile fades from my face as I shift my weight, all at once a little uncomfortable."
            "Wrestling isn't really my thing, and I can't really comment on her performance or anything."
            "All I know is that I recognized her face from school, those collages on the walls where they display athletes who’ve brought them some kind of prestige."
            "A moment of silence falls between us as I find myself with nothing more to say."
            bree.say "I guess, uh, I’ve never been a huge follower of the sport, or anything."
            show ayesha annoyed
            "She shrugs and shifts her weight, clearly bothered by my pointless interruption to her workout."
            ayesha.say "Isn't gonna be for everyone."
            "I shake my head, spreading my hand in a gesture of ‘go ahead.’"
            bree.say "Hey, I’m sorry for stopping you. It just would have driven me crazy!"
            show ayesha normal
            ayesha.say "No worries."
    show ayesha normal
    "She glances me up and down once more."
    ayesha.say "Are you new here?"
    bree.say "Oh, yeah, sort of. I moved nearby not long ago."
    if hero.morality >= 10:
        bree.say "You mean you were watching my workout?"
        bree.say "Like making sure I was doing it right?"
    elif hero.morality <= -10:
        bree.say "What, like eyeing me up?"
        bree.say "Because you like what you see?"
    show ayesha b joke
    "Ayesha smiles and nods her head."
    "And for the first time I see how pretty she actually is."
    "Sure, she's tall and look as strong as an ox."
    "But there's just something attractive about her too."
    show ayesha b happy
    ayesha.say "Yeah..."
    ayesha.say "Something like that!"
    ayesha.say "I was actually going to say I admire your form."
    ayesha.say "How you manage to be feminine and strong at the same time."
    ayesha.say "It's a lot harder to pull off than people think!"
    show ayesha b joke
    menu:
        "Thank her":
            "I smile and nod at what Ayesha's saying."
            "Even though part of me can't believe what she's saying."
            bree.say "Thank you, Ayesha."
            bree.say "But I'm nothing special."
            bree.say "I just turn up, work-out and then go home!"
            "Ayesha listens to what I have to say."
            "Then she shakes her head."
            ayesha.say "I don't know, [hero.name]..."
            ayesha.say "You seem pretty special to me!"
            "Ayesha looks me straight in the eye as she says this."
            "And for a moment I wonder what's going on."
            "Then it dawns on me."
            "Is she...is she flirting with me?"
            $ ayesha.love += 1
        "I wish I could be more like you":
            "I smile and nod at what Ayesha's saying."
            "But I can't help disagreeing with some of it."
            bree.say "Actually, Ayesha..."
            bree.say "I wish I could be more like you."
            bree.say "You know, strong and powerful."
            bree.say "Everyone seems to expect me to be weak because I'm female!"
            show ayesha annoyed
            "Ayesha's expression looks pained as she listens to me."
            "And she shakes her head."
            "Showing that she disagrees with me in turn."
            ayesha.say "Oh, you wouldn't want to swap places with me, [hero.name]."
            ayesha.say "It's not fun being the tallest girl in the room."
            ayesha.say "Or having guys be intimidated by the size of your biceps!"
            $ ayesha.love -= 1
    show ayesha normal
    ayesha.say "Anyway..."
    ayesha.say "I didn't come over here just to shoot the breeze."
    bree.say "You didn't?"
    show ayesha a
    ayesha.say "Well, I’m actually a personal trainer around here."
    "She gestures vaguely with her head to indicate the location."
    ayesha.say "If you’re ever looking for help, ask for me up front. Be happy to help when I’m not in a workout."
    menu:
        "That’d be great!":
            $ ayesha.love += 1
            bree.say "Wow, thank you! I’ll definitely ask!"
            "Okay, so I can't help it."
            "I’m gushing."
            "Even my old personal trainer at the college used to talk about Ayesha and how much of a strong feminine role model she is."
            "And a girl I used to sit at lunch with in high school went on to cheer in college, including at the wrestling games."
            "Ayesha was sort of a star around there, for her obvious success."
            "I’ve only ever heard good things about her."
            "And of course, with the shows she does now, the fame and glory, the displays of almost artistic physical prowess…"
            "The idea of her training me… sure, I’m embarrassing, but it gives me butterflies."
            show ayesha happy at startle
            "She gives a soft laugh again."
            ayesha.say "Sounds good then. Look forward to it."
        "Oh, thank you.":
            bree.say "Oh, really?"
            "My interest is piqued."
            "Why not?"
            "Maybe I’ll take her up on the offer."
            "God knows the woman knows what she’s doing, with a body and a career like that."
            bree.say "I’m actually in the market for a new trainer, maybe. I’ll definitely keep it in mind!"
            ayesha.say "Sounds good."
        "I’ll probably pass…":
            $ ayesha.love -= 1
            "I feel like I’ve embarrassed myself enough already."
            "It can only get more awkward, honestly."
            "I’m nowhere near at her level, physically."
            "I’m in shape, sure, but not her level of in shape, and I don't want to make myself look stupid in front of someone who I know is a pretty big deal with the people I know at school."
            "Besides, I know she does the wrestling shows, and with that kind of fame and prowess… maybe I’m being a baby, but I’m kind of scared of her."
            bree.say "I, um… I’m not really looking for a trainer right now, honestly."
            show ayesha annoyed
            "She looks me up and down again."
            "This time I can feel that she’s judging me critically as she does."
            "She shrugs one shoulder and turns her attention away, bored with me."
            ayesha.say "Suit yourself."
    bree.say "So, I’ll, um, see you around?"
    show ayesha normal
    "It goes without saying that she’s probably here a lot."
    "I know she’s a sight I’m going to have to get acquainted to, if I’m going to be coming here much."
    "She nods, and I can tell her attention and focus has already shifted back to her workout."
    ayesha.say "Sure thing, uh--"
    bree.say "[hero.name]."
    ayesha.say "See you around, [hero.name]."
    $ ayesha.unhide()
    return
label ayesha_female_event_02:
    ayesha.say "Hey, [hero.name]!"
    "I look up at the sound of a familiar voice."
    show ayesha happy with dissolve
    "And I find myself looking at Ayesha as she towers over me."
    "She looks taller and more buff than the last time I saw her."
    "But she has a huge smile on her face."
    "Like she's really pleased to see me."
    bree.say "Ah..."
    bree.say "Hey, Ayesha."
    bree.say "How are you doing?"
    "Ayesha nods and smiles, eager to speak to me."
    ayesha.say "I'm doing pretty good, [hero.name]."
    ayesha.say "A lot better for bumping into you, actually!"
    "Well now I am intrigued."
    "The beautiful Amazon from the gym is please to see me."
    "I can't help returning Ayesha's smile and wanting to hear more."
    bree.say "Why's that, Ayesha?"
    bree.say "Have I been on your mind all this time?"
    show ayesha surprised at startle
    "I see Ayesha's eyes go wide."
    show ayesha blush
    "And she even seems to blush a little."
    "Am I seeing things, or is the giantess actually bashful?"
    ayesha.say "I..."
    ayesha.say "I don't know about that, [hero.name]!"
    ayesha.say "I was just wondering if you..."
    ayesha.say "Well...if you were into wrestling?"
    "I don't think I've ever been asked that question by a girl before."
    show ayesha normal
    "And it makes me blink in surprise."
    bree.say "What..."
    bree.say "You mean like the stuff at the Olympics?"
    bree.say "Or the stuff on TV with all the crazy costumes?"
    ayesha.say "The last one - I mean professional wrestling."
    ayesha.say "It's just...I have tickets for a show."
    show ayesha blush
    ayesha.say "And I wondered if you wanted to come along too?"
    "I'm still so surprised it takes me a second to say anything."
    bree.say "You're really into that stuff?"
    bree.say "I thought it was mostly for guys?"
    "Ayesha shakes her head at this."
    show ayesha normal
    ayesha.say "Oh no, [hero.name]!"
    ayesha.say "There are lots of female wrestling fans."
    ayesha.say "And female wrestlers too."
    ayesha.say "Like me - I wrestle myself."
    "I've already seen Ayesha working out at the gym while clad in lycra."
    "So it doesn't take much convincing for me to believe her."
    ayesha.say "So what do you say, [hero.name]?"
    ayesha.say "You want to come to the matches with me?"
    menu:
        "Why not":
            bree.say "Okay, Ayesha..."
            bree.say "I've never been to a wrestling show before."
            bree.say "But it's always fun to try something new."
            "Ayesha looks delighted with my answer."
            "But she does the best she can to play it cool."
            "Though I can see she's finding it pretty hard."
            ayesha.say "You'll come?"
            show ayesha happy
            ayesha.say "That's great, [hero.name]!"
            ayesha.say "Well...I mean it's good, you know?"
            ayesha.say "I could probably have found someone else to go with me..."
            show ayesha blush
            ayesha.say "But I wanted to ask you first..."
            "I can see that Ayesha's starting to babble."
            "So I step in to stop her before she embarrasses herself."
            bree.say "Let me know where and when, okay?"
            bree.say "Here...take my mobile number."
            show ayesha happy
            "Ayesha and I swap numbers, then say a brief goodbye."
            $ hero.smartphone_contacts.append("ayesha")
            "Then she walks away, looking pretty pleased with herself."
            $ ayesha.love += 1
            $ hero.calendar.add(game.days_played + 3, LabelAppointment(18, "ayesha", "Wrestling show", "ayesha_female_event_03", "ayesha_female_event_03_missed"))
        "Sorry, not my thing (Never meet Ayesha again)":
            bree.say "Hmm..."
            bree.say "That doesn't sound like my kind of thing."
            bree.say "Sorry, Ayesha - but I think I'm going to have to say no."
            show ayesha annoyed
            "Ayesha looks instantly disappointed."
            "But she does the best she can to hide it."
            "Waving her hand in front of her like it's nothing."
            show ayesha normal
            ayesha.say "No problem, [hero.name]."
            ayesha.say "I kind of knew it was a long-shot."
            ayesha.say "But maybe we can think of something else to do together?"
            "I nod and smile, keen to smooth all of this over."
            bree.say "Of course we can, Ayesha."
            bree.say "Just let me know where and when, okay?"
            "Ayesha nods too."
            "And then she walks away, looking just a little happier."
            $ ayesha.set_gone_forever()
    return

label ayesha_female_event_03_missed:
    "Shit I missed the wrestling show with Ayesha."
    $ ayesha.love -= 5
    $ DONE.pop("ayesha_female_event_02")
    return

label ayesha_female_event_03(appointment=None):
    if ayesha.love.max < 60:
        $ ayesha.love.max = 60
    scene bg arena at flip, dark, center, zoomAt (2.5, (-300, 1020)) with fade
    "I have to admit that I'm more than a little nervous about going to a wrestling show."
    "For one thing, I know almost nothing about pro-wrestling, how it works or what's supposed to happen."
    "Sure, I've walked in on [mike.name] watching it a couple of times and I know they make videogames based on it."
    "But aside from that I'm pretty much clueless!"
    show ayesha casual normal at right with easeinright
    "Oh, and then there's the fact that I'm going with Ayesha too."
    "I kind of think this is a date, but I'm not totally sure."
    "Maybe it's more like a try-out date, to see if things work out?"
    "Urgh...I need to clear my head so I don't screw this up!"
    show ayesha casual normal at center with ease
    ayesha.say "These are our seats, [hero.name]..."
    ayesha.say "These two right here."
    show ayesha casual normal at center, zoomAt(1.5, (640, 1040)) with fade
    "I hurry over to the seats that Ayesha's pointing at."
    "But when I look up, I find myself looking straight at what I guess is the wrestling ring."
    bree.say "Is this right, Ayesha?"
    bree.say "We're awfully close to where they're going to be fighting!"
    bree.say "Isn't that dangerous?"
    "Ayesha shakes her head as she sits down next to me."
    ayesha.say "They're wrestlers, [hero.name]."
    show ayesha joke
    ayesha.say "Not man-eating lions!"
    ayesha.say "They don't bite."
    show ayesha annoyed
    ayesha.say "Well...some of us do!"
    show ayesha happy
    "Ayesha smiles, like she's trying to reassure me."
    "But when it doesn't seem to work, she leans in a little closer."
    ayesha.say "Okay, [hero.name]..."
    show ayesha normal
    ayesha.say "I'm going to let you in on a little secret, yeah?"
    ayesha.say "This isn't a fight, like in boxing or MMA."
    ayesha.say "It's more like...an exhibition, you now?"
    bree.say "Huh?"
    bree.say "What do you mean?"
    ayesha.say "Let's just say the ending is worked out before the match."
    "Ayesha nods and adds a wink for good measure."
    menu:
        "It's kind of a performance?":
            "My eyes go wide as I realise the implications of what Ayesha just said."
            bree.say "Oh!"
            bree.say "So it's kind of like a play?"
            bree.say "But with wrestling instead of acting?"
            show ayesha happy
            "Ayesha nods."
            $ ayesha.love += 2
            ayesha.say "It's sort of like that, and sort of not."
            ayesha.say "It really helps if you can suspend your disbelief."
            bree.say "I'm not sure how to do that."
            bree.say "But I promise I'll give it my best shot."
            "This seems to be enough to satisfy Ayesha."
            "She leans back in her seat, relaxing a little."
            ayesha.say "One thing though, [hero.name]..."
            ayesha.say "Don't call it fake, yeah?"
            show ayesha annoyed
            ayesha.say "People really don't like it when you do that!"
            "That seems like a really strange thing to get mad about."
            "But I nod all the same."
            if hero.morality >= 25:
                bree.say "Don't worry, Ayesha, I understand."
                bree.say "I used to do amateur dramatics at school."
            if hero.morality <= -25:
                bree.say "No problem at all, Ayesha."
                bree.say "I'm into roleplay myself - especially the physical kind!"
        "It's all fake?":
            "My eyes go wide as I realise the implications of what Ayesha just said."
            bree.say "Wait..."
            bree.say "You mean it's fake?!?"
            "At the mere mention of the word fake, Ayesha scowls."
            $ ayesha.love -= 2
            "She shakes her head as she leans in closer still."
            show ayesha annoyed
            ayesha.say "Shh!"
            ayesha.say "Don't use that word!"
            "Now I really am puzzled."
            "What Ayesha's saying doesn't seem to make sense."
            bree.say "But you said they're not fighting for real."
            bree.say "How can that be anything but..."
            bree.say "Well...anything but that word you don't seem to like?"
            show ayesha normal
            ayesha.say "It's more like a play, [hero.name]."
            ayesha.say "You have to suspend your disbelief."
            ayesha.say "Look, just try it, okay?"
            ayesha.say "I guarantee you'll have fun."
            "I nod, deciding to let the matter drop."
            "Maybe Ayesha's right and I will like it."
            "But I can't help thinking that it does sound a lot like a kid's pantomime!"
            if hero.morality >= 25:
                bree.say "Don't worry, Ayesha, I understand."
                bree.say "I've done some acting in my spare time."
            if hero.morality <= -25:
                bree.say "No problem at all, Ayesha."
                bree.say "I'm an expert when it comes to faking it!"
    scene bg arena at flip, dark, dark, center, zoomAt (2.5, (-300, 1020))
    show ayesha casual normal at dark, center, zoomAt(1.5, (640, 1040))
    with fade
    "Before I can say another word, the lights go down."
    play music "music/TeknoAXE/simple_metal.ogg" loop fadein .5
    "And then loud rock music starts to play over the PA system."
    show ayesha happy at startle with dissolve
    "The people sitting around us start to go crazy - Ayesha too!"
    show ayesha normal
    "All of this makes me feel like I'm at a rock concert, rather than a sporting event."
    "I watch as a guy in a suit walks down the aisle."
    "He has a microphone, so I assume he's the ring announcer."
    "My suspicions are confirmed when he climbs into the ring and starts the show."
    "MC" "Ladies and gentlemen..."
    "MC" "Welcome to Pro Wrestling BANG!"
    "MC" "Our first contest is scheduled for one fall!"
    "Crowd" "ONE FALL!"
    with vpunch
    "I jump in my seat as the entire crowd shouts the words together."
    show ayesha happy at startle
    "Ayesha notes my surprise and chuckles, clearly amused."
    "MC" "Introducing first, weighing in at one hundred and thirty pounds..."
    show ayesha normal
    "MC" "The Muay Thai Mistress..."
    "MC" "Magrat!"
    "Hardcore music plays as a tough-looking girl walks down the aisle."
    "She's more ripped than most guys I've seen and she's even wearing an eye-patch!"
    "I have no idea if it's real of a part of her costume - and I'd be scared to ask!"
    "She climbs into the ring and I see she's wearing kick-boxing gear."
    "MC" "And her opponent, from Osaka Japan..."
    "MC" "Weighing in at two hundred sixty pounds..."
    "MC" "Edna Hyundai..."
    "The music that plays this time is more like something I'd expect to hear at a spa!"
    "It's all oriental flutes and ethereal strings."
    "But when I see this Edna girl for myself, I can't help gasping in surprise."
    "She's walking down the aisle, throwing what looks like white powder around."
    "And she's huge!"
    "I thought the first girl looked tough - but this one is terrifying!"
    "And from the crazy kimono she's wearing, she must be a sumo wrestler."
    "Unlike the kick-boxer, this girl doesn't climb straight into the ring."
    "Instead she walks around the outside while the crowd jeers at her."
    bree.say "Why is she doing that, Ayesha?"
    bree.say "Everyone seems to hate her!"
    bree.say "Doesn't she get that they don't want to talk to her?"
    ayesha.say "She's the heel, [hero.name], the bad guy."
    ayesha.say "She wants the fans to hate her and get worked up."
    ayesha.say "That's part of her job, to make them get into it by hating on her!"
    show ayesha annoyed
    "As the sumo wrestler gets closer, I notice Ayesha sitting back."
    "In fact, it's almost like she's shrinking down into her chair."
    "The sight is pretty funny, as there's no chance of her hiding herself."
    "Ayesha's way too tall for that to work!"
    bree.say "What's the matter, Ayesha?"
    bree.say "You're not scared of that girl, are you?"
    bree.say "You're way tougher-looking than her!"
    ayesha.say "It's not that, [hero.name]."
    ayesha.say "I've wrestled Edna in the past."
    ayesha.say "And I don't want her to see me!"
    "But as I turn my head to look where Edna is, it's already too late!"
    "Edna" "By my sacred ancestors!"
    "Edna" "If it isn't Ayesha the Amazon!"
    show fx anger
    "Edna" "Skulking in the crowd with all the other scum, I see?"
    "Edna" "And with a scrawny little bitch on your arm too!"
    hide fx
    "Puzzled by this last comment I look around me."
    "That is until Ayesha explains what's going on"
    ayesha.say "She's talking about you, [hero.name]!"
    bree.say "Oh...I see..."
    bree.say "Wait a minute - she's being mean to me!"
    menu:
        "Defend Ayesha and yourself":
            "I can't believe what I'm hearing."
            "Ayesha told me that the wrestlers are kind of pretending."
            "But she never told me that they'd start hurling insults at me!"
            show ayesha surprised at startle
            show fx exclamation
            bree.say "Who are you calling scrawny?!?"
            bree.say "At least I can see my feet!"
            hide fx
            bree.say "You could be wearing carpet slippers for all you can see!"
            "The big girl looks surprised to hear me standing up to her."
            "Maybe she thought that I was going to be an easy target."
            "Or maybe I just found a weak spot."
            "In a way, I'm kind of more surprised when the crowd starts to cheer me."
            "Edna" "You shut your filthy mouth!"
            "Edna" "And anyway...this is glandular - I can't help it!"
            bree.say "Oh, come on - you know as well as I do that's a myth!"
            bree.say "What you need is more exercise and less cake!"
            bree.say "You need to be dragged down to the gym by Ayesha here."
            bree.say "This Amazon's got a workout to shrink your tank-ass!"
            hide ayesha
            show ayesha casual a angry
            with hpunch
            "As if she's feeding off of what I'm saying, Ayesha stands up."
            show ayesha annoyed
            $ ayesha.sub += 2
            show ayesha b
            pause 1
            show ayesha a
            pause 1
            show ayesha b
            "And she flexes her muscles, making her arms ripple."
            show ayesha a
            pause 1
            show ayesha b
            "She's pulling off poses that you see in body-building competitions."
            ayesha.say "Yeah, you bet I'm the Amazon!"
            ayesha.say "And this Amazon's ready to kick your ass!"
            show ayesha angry
            ayesha.say "Nobody insults my girl and gets away with it!"
            "Suddenly the crowd begins to chant as one."
            show ayesha annoyed
            "Crowd" "Ayesha...Ayesha...Ayesha!"
            "Edna literally snarls at this."
            "But she backs off all the same, rolling into the ring."
            show ayesha happy
            "I turn to Ayesha, my eyes wide with admiration and affection."
            "And, if I'm honest, not a small amount of carnal desire too!"
            bree.say "Ayesha...you're my hero!"
            $ ayesha.love += 2
            show ayesha blush
            ayesha.say "What?!?"
            ayesha.say "Aw...stop it, [hero.name]!"
            show ayesha happy
            ayesha.say "Actually, don't stop it - I like being your hero!"
        "Let Ayesha defend you":
            bree.say "Is...is she allowed to do that?!?"
            "Edna" "I don't need your permission to insult you!"
            "Edna" "You dumb little skank!"
            $ ayesha.sub -= 2
            "I look at Edna and then back at Ayesha."
            "I had no idea this kind of thing happened at these shows."
            "I'm a paying member of the audience - a customer!"
            "And I'm not used to this kind of treatment."
            show ayesha angry
            ayesha.say "Hey, butter-ball - eyes on me!"
            "I can't help looking up at Ayesha in awe."
            hide ayesha
            show ayesha casual a angry
            with hpunch
            "She's standing up and looking Edna straight in the eye."
            "And I feel my heart beat faster at what she does next."
            show ayesha b
            pause 1
            show ayesha a
            pause 1
            show ayesha b
            "Ayesha flexes her muscles, making her arms ripple."
            show ayesha a
            pause 1
            show ayesha b
            "She's pulling off poses that you see in body-building competitions."
            show ayesha annoyed
            ayesha.say "Yeah, you bet I'm the Amazon!"
            ayesha.say "And this Amazon's ready to kick your ass!"
            show ayesha angry
            ayesha.say "Nobody insults my girl and gets away with it!"
            "Suddenly the crowd begins to chant as one."
            show ayesha annoyed
            "Crowd" "Ayesha...Ayesha...Ayesha!"
            "Edna literally snarls at this."
            "But she backs off all the same, rolling into the ring."
            show ayesha happy
            "I turn to Ayesha, my eyes wide with admiration and affection."
            "And, if I'm honest, not a small amount of carnal desire too!"
            bree.say "Ayesha...you're my hero!"
            $ ayesha.love += 5
            show ayesha blush
            ayesha.say "What?!?"
            ayesha.say "Aw...stop it, [hero.name]!"
            show ayesha happy
            ayesha.say "Actually, don't stop it - I like being your hero!"
    show ayesha casual happy at dark, center, zoomAt(1.5, (640, 1040)) with fade
    play music "music/roa_music/2am.ogg" loop fadein .5
    "Now that both of the intimidating girls are in the ring, I feel a lot safer."
    "Even more so when Ayesha sits down next to me again."
    "I hear a bell ring, and that seems to mean the fight is starting."
    "Edna and Magrat start grappling, then tossing each other around the ring."
    "And the weirdest thing is that I find myself quite enjoying it."
    "I don't think I'm going to become the biggest fan of wrestling any time soon."
    "But I do think that I'm starting to see what the appeal of this stuff is."
    scene bg street
    show ayesha casual normal
    with fade
    "After the show, Ayesha seems eager to find out what I thought of it."
    ayesha.say "That was a really great show."
    ayesha.say "Tell me you loved it, [hero.name]!"
    show ayesha happy
    ayesha.say "How could you not love it?!?"
    bree.say "I've got to admit, Ayesha..."
    bree.say "It was a lot of fun."
    bree.say "I never knew that watching people pretend to fight could be so entertaining."
    ayesha.say "So..."
    ayesha.say "You know that I'm a wrestler too."
    show ayesha blush
    ayesha.say "What do you think about coming to a show where I've got a match?"
    menu:
        "I'd love that":
            "My eyes go wide at the mere mention of seeing Ayesha in the ring."
            "And I nod my head, desperate to let her know how I feel about the idea."
            if hero.morality >= 25:
                bree.say "Of course I would, Ayesha!"
                bree.say "I thought you were going to kick that mean girl's ass today."
                bree.say "I'd love to see you deal with a bully like that!"
            if hero.morality <= -25:
                bree.say "I was hoping you'd say that, Ayesha!"
                bree.say "Because I really want to see what you can do to a girl."
                bree.say "And maybe you can do something similar to me afterwards?"
            "Ayesha looks delighted with my answer."
            show ayesha happy
            "She nods eagerly."
            ayesha.say "That's great, [hero.name]!"
            ayesha.say "I'll let you know when my next show is happening."
            ayesha.say "It should be easy to get you a ticket."
            "I nod and smile, showing Ayesha that I'm up for it."
            "And we walk off, discussing the finer details of the matches."
            $ ayesha.love += 2
        "I don't want to see you get hurt":
            "My eyes go wide at the mere mention of seeing Ayesha in the ring."
            "And I shake my head, desperate to let her know how I feel about the idea."
            if hero.morality >= 25:
                bree.say "No way, Ayesha!"
                bree.say "I'd be terrified the whole time."
                bree.say "Scared that you were going to get hurt."
            if hero.morality <= -25:
                bree.say "No thanks, Ayesha."
                bree.say "I think I'd rather you got physical with me."
                bree.say "If you know what I mean?"
            show ayesha annoyed
            "Ayesha looks disappointed with my answer."
            "But she nods all the same."
            show ayesha normal
            ayesha.say "Okay, [hero.name], if that's how you feel about it."
            ayesha.say "I know that wrestling's not for everyone."
            ayesha.say "Maybe we can get together and do something else instead?"
            $ ayesha.sub += 1
            "I nod and smile, letting Ayesha know that I'm more keen on this idea."
            "And that seems to cheer her up a little."
    $ DONE["ayesha_female_event_03"] = game.days_played
    return

label ayesha_female_event_04:
    if ayesha.love.max < 80:
        $ ayesha.love.max = 80
    scene expression f"bg {game.room}"
    "I know that I really shouldn't be walking down the street while staring at my phone."
    "But it's just one of those things that everyone does, right?"
    "You only really think about it when you do it and something goes wrong."
    "Kind of like right now..."
    with hpunch
    bree.say "Wha..."
    show ryan casual angry zorder 2 at flip, blacker, center, zoomAt (1.2, (640, 900))
    "Guy" "Urgh..."
    "I feel myself collide with another person, and I leap back on pure instinct."
    "By some miracle I manage to hold onto my phone as I do so."
    bree.say "Oops..."
    bree.say "Sorry!"
    bree.say "I was totally wrapped up in my phone!"
    "I make a point of smiling and shrugging at the guy who I bumped into."
    "He doesn't look too badly shaken up by the collision."
    "So hopefully he's just going to shrug it off and we can leave it at that."
    "Guy" "No problem, Lady..."
    "Guy" "That's not a problem you're going to have for much longer."
    "I'm a little puzzled by what he just said."
    "So I shake my head and try again."
    bree.say "Erm..."
    bree.say "I don't think I heard you properly."
    bree.say "Look, is there anything I can do to help?"
    "The guy looks me square in the eye."
    "And now he has a distinctly threatening look on his face."
    "Guy" "Yeah, lady..."
    "Guy" "You can hand over your phone!"
    "Guy" "And everything else too!"
    "My eye go wide as I finally realise what's happening here."
    show ryan casual zorder 2 at flip, blacker, center, zoomAt (1.65, (640, 1060))
    "I go to take a step backwards, but the guy lurches forwards."
    "At the same time he's thrusting a hand forwards inside his jacket."
    "I have no idea what he's got in there."
    "But I sure as hell don't want to find out the hard way!"
    menu:
        "Give him everything":
            "Oh my god!"
            "This is actually happening!"
            "Am I going to get stabbed, maybe even killed?!?"
            bree.say "Okay, okay, okay!"
            bree.say "I'm doing it!"
            bree.say "Just don't hurt me, please!"
            "I scramble to do as the mugger asks."
            "But I'm panicking, and that makes me fumble."
            "And I almost end up dropping my things onto the sidewalk."
            "Mugger" "Hurry the fuck up!"
            "Mugger" "I want all of your shit!"
            "Mugger" "Otherwise I'm gonna cut you!"
            "I nod frantically as I try to do what he wants."
        "Scream for help":
            "What does this guy think?"
            "That this is the past?"
            "And that I'm some kind of helpless little woman?"
            bree.say "You really think I'm going to do that?!?"
            bree.say "It's broad daylight, and we're in the middle of the street!"
            bree.say "HEY EVERYONE..."
            bree.say "THIS CLOWN'S TRYING TO MUG ME!"
            "I look around, expecting people to come to my aid."
            "But instead they back off, doing all they can to avoid the situation."
            "Mugger" "What the fuck are you trying to pull?!?"
            "Mugger" "Gimmie your shit NOW!"
            "Mugger" "Or else I'll cut you, bitch!"
            "Ah well, I guess it was worth a try!"
    "I'm too distracted to notice what's going on around me."
    "Which is why I fail to see the shadow looming over the mugger."
    show ryan casual at blacker, hshake, center, zoomAt (1.65, (640, 1060))
    "Mugger" "Wha..."
    show ryan casual at blacker, vshake, center, zoomAt (1.65, (540, 1060))
    "Mugger" "Ah...aargh!"
    "I look up in surprise as the mugger's arm is dragged backwards."
    "This pulls his hand out of his pocket, and I see what he's holding for the first time."
    bree.say "HEY!"
    bree.say "That's not a knife!"
    bree.say "It's your mobile!"
    "All the mugger can manage in response is a strangled groan."
    show ayesha casual angry zorder 1 at center, zoomAt(1.5, (840, 1040)) with dissolve
    "But then I see a familiar face looking at me over his shoulder."
    ayesha.say "Yeah, [hero.name]..."
    ayesha.say "Looks like this asshole's just a chancer!"
    ayesha.say "Still, lucky I spotted you when I did, eh?"
    "I nod and smile as Ayesha manhandles the mugger."
    "In fact I even clap my hands together in glee."
    if hero.morality >= 25:
        bree.say "Oh, Ayesha..."
        bree.say "You're a life-saver!"
    if hero.morality <= -25:
        bree.say "Oh my god, Ayesha..."
        bree.say "You came out of my dreams and to my rescue!"
    ayesha.say "Just a second, [hero.name]."
    show ayesha joke
    ayesha.say "I need to teach this guy a lesson..."
    "Ayesha cranks the mugger's arm again, almost lifting him off his feet."
    show ayesha annoyed
    "He lets out a wail of pain and alarm, dropping his mobile onto the sidewalk."
    menu:
        "Watch Ayesha":
            "Part of me is pretty ashamed that I just stand and watch what happens next."
            "I know that I should step in and stop Ayesha beating the guy up."
            "But another part of me wants to see him get what he deserves."
            "And yet another is fascinated to see Ayesha in action."
            "So I stand back and watch as she goes to work."
            "Needless to say, the mugger doesn't stand a chance."
            show ayesha at startle
            play sound punch_hard
            pause 0.2
            show ryan casual at flip, blacker, hshake, center, zoomAt (1.65, (540, 1060))
            pause 1.0
            show ayesha at startle
            play sound punch_hard
            pause 0.2
            show ryan casual at flip, blacker, hshake, center, zoomAt (1.65, (440, 1060))
            "Ayesha roundly clobbers the guy with her fists."
            "And just like when I was trying to get help, nobody bothers to interfere."
            hide ryan at flip, blacker, center, zoomAt (1.65, (440, 1060)) with moveoutleft
            "In fact, Ayesha gives him such a beating that he runs the moment she lets him go."
            $ hero.morality += 1
        "Help Ayesha":
            "I'm practically cheering Ayesha on as she starts to clobber the mugger."
            show ayesha at startle
            play sound punch_hard
            pause 0.2
            show ryan casual at flip, blacker, hshake, center, zoomAt (1.65, (540, 1060))
            pause 1.0
            show ayesha at startle
            play sound punch_hard
            pause 0.2
            show ryan casual at flip, blacker, hshake, center, zoomAt (1.65, (440, 1060))
            "Her fists fly this way and that, landing blow after blow on the guy."
            "And just like when I was trying to get help, nobody bothers to interfere."
            "I don't once stop to think whether she should be doing this or not."
            "In fact, when the chance presents itself, I wade in too."
            "Swinging my leg back, I let it go and plant my foot right where I want it."


            pause 0.2
            show ryan casual at flip, blacker, vshake, center, zoomAt (1.65, (440, 1060))
            "Which is between the mugger's legs!"
            hide ryan at flip, blacker, center, zoomAt (1.65, (440, 1060)) with moveoutbottom
            "He groans and crumples to his knees, barely able to stay upright."
            "But amazingly, he manages to scuttle away the moment Ayesha lets him go."
            $ hero.morality -= 1
    "Once the mugger is out of sight, I turn to Ayesha."
    show ayesha normal at center, zoomAt(1.5, (640, 1040)) with ease
    "And I can feel myself bursting with relief to see her."
    "But I can feel something else as well."
    "Something that's harder to define."
    if hero.morality >= 25:
        bree.say "Oh, wow..."
        bree.say "I'm so glad to see you, Ayesha!"
        bree.say "You saved my life back there!"
    if hero.morality <= -25:
        bree.say "Ayesha..."
        bree.say "My hero!"
        bree.say "I'll do anything to repay you."
        bree.say "And I do mean anything!"
    show ayesha happy
    "Ayesha smiles broadly as she waves away my thanks."
    ayesha.say "Ah, it was nothing, [hero.name]."
    ayesha.say "I'm just glad I was able to help."
    "I'm about to say more."
    show ayesha surprised at startle
    "But at that moment, Ayesha's phone makes a sound."
    "She pulls it out and shakes her head."
    show ayesha sad
    ayesha.say "Sorry, [hero.name]..."
    show ayesha annoyed
    ayesha.say "I have to go."
    ayesha.say "There's an emergency at the gym!"
    "Before I can even ask what on earth that could be, Ayesha strides off."
    hide ayesha with easeinleft
    "I watch as she disappears down the street, leaving me alone and still a little confused."
    return

label ayesha_female_event_05:
    if ayesha.love.max < 100:
        $ ayesha.love.max = 100
    scene bg black
    show bg arena at center, dark, blur, zoomAt (1.75, (500, 1250))
    play sfx1 crowd_big_concert volume 0.8
    with fade

    show hanna sport at blacker, flip, center, zoomAt (1, (320, 720))
    play sound slam
    with hpunch
    pause 0.5
    show ayesha fight at blacker, center, zoomAt (1, (960, 720))
    play sound slam
    with hpunch
    pause 0.5
    play sfx2 crowd_cheer
    show ayesha normal at center, zoomAt (1, (960, 720)) with dissolve
    pause 1

    show hanna at blacker, flip, center, traveling (1, 0.3, (700, 720))
    pause 0.2

    play sound "<from 0.8>sd/SFX/weapons/sword_woosh.ogg"
    show ayesha fight at center, traveling (1, 0.1, (1100, 720))
    play sfx3 crowd_yeah
    pause 0.3
    show ayesha fight at center, traveling (1, 0.1, (1000, 720))
    pause 0.1
    show hanna at blacker, flip, center, traveling (1, 0.2, (420, 720))
    pause 0.5

    show ayesha fight upset at center, traveling (1, 0.1, (750, 720))
    pause 0.1
    play sound punch_hard
    show hanna at blacker, center, zoomAt (1, (400, 720)), hshake
    pause 0.2
    show hanna at blacker, flip, center, traveling (1, 0.5, (250, 720))
    pause 0.5

    show ayesha b with dissolve
    pause 0.5
    show ayesha at center, traveling (1, 0.3, (800, 720))
    pause 0.3
    show ayesha b upset at center, traveling (1, 0.8, (840, 750))
    pause 0.8

    show ayesha a fight angry at center, traveling (1, 0.07, (450, 750))
    pause 0.07
    play sound punch_hard
    play sfx2 crowd_applause
    show hanna at blacker, flip, center, zoomAt(1, (250, 720)), hshake
    show ayesha a fight upset at center, traveling (1, 0.2, (840, 720))
    if hero.morality >= 25:
        bree.say "Oh..."
        bree.say "Oh my god..."
        bree.say "I hope she's okay!"
    elif hero.morality <= -25:
        bree.say "Fuck me..."
        bree.say "How did she bend that girl in half?!?"
        bree.say "And can she do the same to me?"
    else:
        bree.say "WHOA..."
        bree.say "How did she do that?!?"
        bree.say "She's like...like a superhero!"
    "I think I'm shouting at the top of my voice right now, maybe even bellowing."
    "But there's no way even the people sitting to either side of me can hear a word."
    "That's because everyone in the place is up and on their feet, shouting too."

    show hanna at blacker, flip, center, traveling (1, 0.3, (640, 720))
    pause 0.3
    play sound "<from 0.8>sd/SFX/weapons/sword_woosh.ogg"
    show ayesha b upset at center, traveling (1, 0.1, (1000, 720))
    play sfx3 crowd_yeah
    pause 0.1
    show hanna at blacker, flip, center, traveling (1, 0.5, (440, 720))
    pause 0.3
    show ayesha b happy with dissolve
    pause 1
    show ayesha a at startle(0.05,-10)
    pause 0.2
    show ayesha at startle(0.05,-10)
    pause 0.2
    show ayesha at startle(0.05,-10)
    pause 0.2
    show ayesha at hshake
    "My hands are gripping the barricade in front of me as I stare up at the ring."
    "Well, if I'm more honest, I'm actually staring up at Ayesha, who's inside of it."
    show ayesha a at startle(0.05,-10)
    pause 0.2
    show hanna at blacker, flip, center, traveling (1, 1.2, (120, 720))
    show ayesha at startle(0.05,-10)
    pause 1
    show ayesha fight at center, traveling (1, 1, (1100, 770))
    pause 1
    stop sfx1 fadeout 1.5

    show hanna at blacker, flip, center, traveling (1, 0.2, (440, 720))
    pause 0.1
    show ayesha fight angry at center, traveling (1, 0.05, (640, 770))
    pause 0.05
    play sound punch_hard
    show ayesha at hshake
    with hpunch
    pause 0.1

    show hanna at blacker, flip, center, traveling (1, 0.3, (440, 1770))
    pause 0.3
    play sound slam
    with vpunch
    pause 0.5
    show ayesha fight upset at center, traveling (1, 0.3, (640, 770))
    pause 0.5
    play sound boxing_bell volume 0.5
    play sfx1 crowd_big_concert
    play sfx2 crowd_cheer
    play sfx3 crowd_applause
    pause 0.3
    show ayesha fight at center, traveling (1, 0.7, (640, 720))
    pause 0.7
    show ayesha normal with dissolve
    "She just got done pounding her latest opponent into the canvas."
    play sfx2 crowd_encore
    hide hanna at blacker with dissolve

    show ayesha b fight happy at center, traveling(1.2, 1, (320, 820))
    pause 1
    show ayesha a fight happy at center, startle(0.3, 5), zoomAt(1.2, (320, 820))
    pause 1
    show ayesha b fight happy at flip, center, traveling(1.2, 1, (960, 820))
    pause 1
    show ayesha a fight happy at center, startle(0.3, 5), zoomAt(1.2, (960, 820))
    pause 1
    show ayesha b fight happy at center, traveling(1.6, 0.5, (640, 1020))
    pause 0.5
    show ayesha a fight happy at center, startle(0.5, 10), zoomAt(1.6, (640, 1020))
    pause 0.5
    show ayesha b fight happy at center, traveling(1, 0.5, (640, 720))
    "And now she's pulling off some pretty sweet poses as she celebrates for her fans."
    "You know, I never thought that professional wrestling was my kind of thing."
    "But since Ayesha asked me to start coming to her matches, that's really changed."
    "I've found myself getting into them, being swept along with all of the emotion."
    "Though maybe that has more to do with the amazon that's in them than the sport itself?"
    bree.say "AYESHA!"
    bree.say "Ayesha, over here!"
    "Even as I'm shouting Ayesha's name and waving at her, I'm wondering why I'm bothering."
    "There's a couple of hundred other fans in here doing the same thing right now."
    show bg arena at blur, party, zoomAt (1.75, (500, 1250))
    "Plus the lights are flashing and they're playing Ayesha's music too."
    "So I doubt that she can see anything outside of the ring."
    show ayesha fight talkative with dissolve
    pause 0.3
    show ayesha fight talkative at stepback(0.2, 5, 0)
    ayesha.say "[hero.name]!"
    ayesha.say "Hey, [hero.name]!"
    show ayesha fight happy
    "I blink and shake my head, thinking that I must be hearing things."
    "I thought I heard Ayesha calling my name in return."
    "But that must have just been wishful thinking on my part, right?"
    show ayesha fight talkative at startle(0.05,-10)
    ayesha.say "[hero.name], can you hear me?"
    show ayesha fight normal at vshake with dissolve
    "I watch in amazement as Ayesha slides between the ropes and onto the floor."
    show ayesha fight happy at center, traveling (1.2, 1, (640, 820))
    "Then she hurries straight over to where I'm pressed against the barricade."
    show ayesha fight happy at center, traveling (1.4, 1, (640, 920))
    "She makes to throw her arms around me."
    "But the crowd misinterprets this as a chance to swarm her."
    show ayesha fight sad at center, traveling (1, 1.5, (640, 720))
    "I feel a pang of disappointment as she backs off."
    "But then I see Ayesha make a gesture, pointing over her shoulder."
    show ayesha talkative with dissolve
    "Looking me straight in the eye, she mouths the word 'backstage'."
    show ayesha normal
    with dissolve
    "I nod eagerly, already beginning to fight my way out of the crowd."
    "Hurrying to the backstage entrance, the member of staff on the door waves me through."
    "For a moment I wonder just what Ayesha said to them so they'd recognise me as her guest."
    "But the thought is soon pushed aside my excitement as I make it to her changing-room."
    "Well, maybe excitement mixed with a little bit of trepidation would be more honest."
    "Because I'm still not one hundred percent sure of my feelings for Ayesha."
    "And it's not like I have much chance to think about them either."
    stop sfx1 fadeout 3
    stop sfx2 fadeout 3
    stop sfx3 fadeout 3
    scene bg black
    show bg gym at center, blur, blur, zoomAt (1.5, (640, 720))
    with fade
    play sound door_open
    pause 0.5
    play sound door_close
    show ayesha fight happy at center, zoomAt(1.1, (640, 750)) with easeinright
    pause 0.5
    ayesha.say "There you are..."
    ayesha.say "There's my good-luck charm!"
    ayesha.say "I'm so glad you came!"
    show bg gym at center, blur, blur, traveling(1.6, 2, (640, 770))
    show ayesha fight normal at center, traveling(1.4, 2, (640, 920))
    "Ayesha kind of looms in front of me as I walk into the changing-room."
    "She's still in her wrestling gear, which is made of spandex and leaves nothing to the imagination."
    "Plus she's clearly still buzzing from the match, her exposed flesh slick with a sheen of sweat."
    show bg gym at center, blur, blur, traveling(1.7, 0.2, (640, 820))
    show ayesha fight normal at center, traveling(2, 0.2, (640, 1270))
    with hpunch
    "Before I can say a word, Ayesha throws her arms wide and closes the distance between us."
    "I thought that I was a good few feet away from her."
    "But then she has got a far longer stride than me."
    "Which is why I find myself wrapped in her arms a moment later."
    "Well, I guess that I now know what it feels like to be Ayesha's opponent in the ring!"
    "I can feel just how slippery and sweaty she is right now."
    "Though I have to admit that it's not all bad."
    "There's a musky, almost seductive scent about her."
    "And the embrace, while firm, is almost protective in nature."
    bree.say "Ayesha..."
    bree.say "What are you..."
    show ayesha kiss at center, zoomAt(1, (640, 720))
    $ ayesha.flags.kiss += 1
    "The words die on my lips, or rather they're smothered there by Ayesha's own."
    "Is she..."
    "She is!"
    "Ayesha's kissing me right now - full on the lips!"
    menu:
        "Return the kiss":
            "I guess this is one of those times when the heart is more sure than the head."
            "Because I don't resist for a moment, returning the kiss a second after Ayesha initiates it."
            "There's no question in my mind and no resistance in my body, as it just feels so right."
            "As soon as I feel myself wrapped in Ayesha's strong arms, I totally surrender to her."
            "I lean into the kiss as best I can, though I feel like a ragdoll in Ayesha's embrace."
            "And in the end, she's the one that brings it to a close."
            "Ayesha looks oddly bashful as she released me."
            show ayesha fight flirt at center, zoomAt(2, (640, 1270)) with fade
            ayesha.say "Ah, [hero.name]..."
            ayesha.say "I can't help it when you're around me."
            ayesha.say "I just want to hug you and never let go again!"
            ayesha.say "Do you..."
            ayesha.say "Do you feel the same way about me?"
            show ayesha fight normal
            "Man, this is so damn weird!"
            "Here's this literal giantess of a girl, who I just saw smash her opponent in the ring."
            "And she's looking at me like the most bashful, delicate little thing right now."
            bree.say "I gotta admit, Ayesha..."
            bree.say "You caught me off-guard just now."
            bree.say "But yeah, I feel the same."
            bree.say "I want to be your tag-team partner!"
            show ayesha fight surprised with vpunch
            "Ayesha shakes her head, as if she doesn't believe what she's hearing."
            show ayesha fight talkative
            ayesha.say "Wow, [hero.name]..."
            ayesha.say "That was a pretty cheesy way of putting it!"
            ayesha.say "But I'm not complaining - so here goes nothing..."
            ayesha.say "I guess you just pinned the champ!"
            show ayesha fight happy
            pause 0.5
            $ ayesha.love += 6
        "Pull away and tease Ayesha":
            "The kiss doesn't last long, in fact it ends only a few seconds after it starts."
            show ayesha fight normal at center, zoomAt(1.4, (640, 920)) with fade
            "Mainly because I wriggle and squirm until I manage to work my way out of Ayesha's arms."
            "And I can only do that because of how sweaty she is after her match!"
            if hero.morality >= 25:
                bree.say "Eww!"
                bree.say "You're so sweaty, Ayesha..."
                bree.say "Stay away from me until you've taken a shower!"
            elif hero.morality <= -25:
                bree.say "Wow, Ayesha, you're really dripping with sweat."
                bree.say "At this rate you'll have me dripping in a different way!"
            else:
                bree.say "Ayesha, you're totally dripping with sweat!"
                bree.say "Do you knock your opponents out with the smell?!?"
            "Ayesha looks oddly bashful as I pull away from her."
            show ayesha fight talkative
            ayesha.say "Ah, [hero.name]..."
            ayesha.say "I can't help it when you're around me."
            ayesha.say "I just want to hug you and never let go again!"
            ayesha.say "Do you..."
            ayesha.say "Do you feel the same way about me?"
            show ayesha fight sadsmile
            "Man, this is so damn weird!"
            "Here's this literal giantess of a girl, who I just saw smash her opponent in the ring."
            "And she's looking at me like the most bashful, delicate little thing right now."
            bree.say "I..."
            bree.say "I'm not sure, Ayesha."
            show ayesha fight sad with dissolve
            bree.say "But I think that I'd like to find out if I do."
            show ayesha fight normal
            "I see hope flare in Ayesha's eyes at my words."
            show ayesha fight normal at center, traveling(1.4, 0.7, (640, 920))
            "And before I can say a thing, she's reaching out for me again."
            "Her arm wraps around my neck, pulling me into a gentle headlock."
            show ayesha fight talkative
            ayesha.say "That's good enough for me!"
            ayesha.say "Keep this up, and you'll be pinning the champ in no time!"
            $ ayesha.love += 2
            show ayesha fight happy
        "Pull away and back off from Ayesha":
            show ayesha fight normal at center, zoomAt(1.4, (640, 920)) with fade
            "The kiss doesn't last long, in fact it ends only a few seconds after it starts."
            "Mainly because I do all that I can to pull away from Ayesha while she's kissing me."
            "And luckily for me, she seems to get the message almost as soon as I begin to struggle."
            "Ayesha makes a point of stepping backwards once she's released me, holding up her hands."
            show ayesha fight whining
            ayesha.say "Ah..."
            ayesha.say "Sorry, [hero.name]..."
            ayesha.say "I guess the excitement got the better of me."
            show ayesha fight normal
            "I nod slowly, not taking my eyes off of Ayesha for a moment."
            if hero.morality >= 25:
                bree.say "Y...yeah, Ayesha..."
                bree.say "I get it - but that's not cool!"
                bree.say "You can't just go doing things like that to me."
            elif hero.morality <= -25:
                bree.say "Geez, Ayesha..."
                bree.say "I like it as much as the next girl."
                bree.say "But even I'm not that easy!"
            else:
                bree.say "I get it, Ayesha..."
                bree.say "But maybe wait until you've cooled down next time?"
                bree.say "That way you can be sure you're in control."
            "Ayesha looks at the ground as she starts to get changed."
            "And I can tell that she's doing all she can to change the subject too."
            show ayesha fight talkative
            ayesha.say "Yeah, [hero.name]..."
            ayesha.say "You're totally right!"
            ayesha.say "But I'm totally serious too, you know?"
            ayesha.say "Won't you at least give me a chance?"
            show ayesha fight sad
            "Part of me wants to keep on telling Ayesha off for what she did."
            "But I can see that it's already starting to eat her up inside."
            "So I give her a quick nod, and then look away again."
            "Hoping the whole time that I'm doing the right thing."
            $ ayesha.love -= 2
    $ ayesha.set_girlfriend()
    scene bg black
    with fade
    return


label ayesha_kiss_me_female:
    call ayesha_greet from _call_ayesha_greet
    show ayesha
    "I'm not ready for it when it actually happens."
    "One moment I'm smiling at Ayesha, totally at ease."
    hide ayesha
    show ayesha kiss
    with dissolve
    $ ayesha.flags.kiss += 1
    "And the next she's leaning in and planting her lips against mine!"
    "I stiffen for a second, more surprised than scared."
    "But then I can feel my entire body begin to relax."
    "And before I know it, I'm kissing Ayesha back with real passion."
    "I don't question it for a moment, instead giving in totally."
    "Everything about it just feels so right."
    hide ayesha kiss with dissolve
    return


label ayesha_gym_coaching:
    scene bg gym
    "I can't keep doing the same routine again and again if I want to do real fitness."
    "I want to exercise all my muscles."
    "And to do so, I decided to try a new gym machine today."
    "But I soon understand there is something I am doing wrong!"
    "Because I have quite the impression to ride a torture easel."
    "Luckily, someone is coming to rescue me."
    show ayesha work with dissolve
    ayesha.say "Hello [hero.name]."
    ayesha.say "I came over here to ask if you wanted my help, [hero.name]."
    ayesha.say "You remember that I give private classes here at the gym, right?"
    bree.say "Of course, Ayesha."
    bree.say "I just thought I was smarter than this dumb piece of metal and rope."
    ayesha.say "[hero.name], I am here if you want to exercise properly."
    ayesha.say "And I think you'd be the perfect fit."
    ayesha.say "Who knows, maybe you could teach me a few things too?"
    menu:
        "Accept the offer":
            $ ayesha.flags.notrain = False
            $ ayesha.love += 2
            "I start nodding my head almost before Ayesha's done talking."
            "I'm pretty sure there's more to the offer than she's letting on."
            "But I'm intrigued by her, and I want to get to know her better."
            if hero.morality >= 25:
                bree.say "That sounds great, Ayesha."
                bree.say "So long as you promise to be gentle with me?"
                bree.say "Let me take it slowly?"
            elif hero.morality <= -30:
                bree.say "I like the sound of that!"
                bree.say "And I presume these classes would be VERY intimate?"
                bree.say "Totally private and confidential too?"
            show ayesha joke
            "Ayesha laughs and nods."
            show ayesha b
            ayesha.say "Don't worry, [hero.name]..."
            ayesha.say "You'll be in good hands!"
            ayesha.say "I personally guarantee it."
        "Decline the offer":
            $ ayesha.love -= 2
            "I start shaking my head almost before Ayesha's done talking."
            "And I'm already backing away from her too."
            if hero.morality >= 25:
                bree.say "Oh no..."
                bree.say "I think you have me all wrong, Ayesha!"
                bree.say "I'm not that kind of girl at all."
            elif hero.morality <= -25:
                bree.say "I know what you're really after, Ayesha."
                bree.say "And I'm flattered, I really am."
                bree.say "But you're just not my type."
            show ayesha b sad
            "Ayesha looks disappointed with my answer."
            "But she nods her head all the same."
            ayesha.say "Sorry to hear that, [hero.name]."
            ayesha.say "But if you change your mind, you know where to find me."
            ayesha.say "I'll be right here at the gym."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
