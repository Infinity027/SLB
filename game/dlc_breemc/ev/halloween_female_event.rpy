init python:
    SpecificTalkSubject(**{
    "name": "halloween_invite_female",
    "display_name": "Invite at the party",
    "label": "halloween_invite_female",
    "icon": "button_askhalloween",
    "conditions": [
        IsSeason(2),
        HeroTarget(
            IsGender("female"),
            IsFlag("party_planned"),
            Or(
                IsFlag("halloween_girl", False),
                IsFlag("halloween_girl", None),
            ),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "do_once": False,
    "once_day": True,
    "duration": 0,
    })

    SpecificTalkSubject(**{
    "name": "cancel_halloween_invite_female",
    "display_name": "Cancel invitation",
    "label": "cancel_halloween_invite_female",
    "icon": "button_aborthalloween",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            ),
        ActiveTarget(
            Not(IsActivity("sleep")),
            "active_girl == game.flags.halloween_girl",
            ),
        ],
    "do_once": False,
    "once_day": True,
    "duration": 0,
    })

    Event(**{
    "name": "halloween_intro_female",
    "priority": 1000,
    "label": "halloween_intro_female",
    "conditions": [
        IsNotDone("halloween_intro_female"),
        IsDone("scottie_female_event_01", "jack_female_event_01"),
        IsSeason(2),
        'game.calendar.day_of_season in [20,21,22,23,24,25,26,27,28,29,30]',
        IsHour(20, 23),
        HeroTarget(
            IsGender("female"),
            IsRoom("livingroom"),
            ),
        PersonTarget(mike,
            HasRoomTag("home"),
            ),
        PersonTarget(sasha,
            HasRoomTag("home"),
            ),
        ],
    "once_day": True,
    })

    Event(**{
    "name": "halloween_event_female",
    "priority": 1500,
    "label": "halloween_event_female",
    "conditions": [
        IsDone("halloween_intro_female"),
        IsSpecialDate("halloween"),
        IsHour(20, 23),
        HeroTarget(
            IsGender("female"),
            ),
        PersonTarget(mike,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden())
            ),
        ],
    "clothes": "halloween",
    "disable_clothing_policy": True,
    "once_day": True,
    })


label halloween_invite_female:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_471
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_halloween_invitation_female"):
        call expression f"{active_girl.id}_halloween_invitation_female" from _call_expression_472
    else:
        bree.say "Have you made any plans for Halloween yet?"
        active_girl.say "Yes, I have something planed."
        bree.say "Oh..."
        active_girl.say "Sorry [hero.name], maybe next year?"
        bree.say "Sure..."
    $ renpy.hide(active_girl.id)
    return

label cancel_halloween_invite_female:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_473
    $ renpy.show(active_girl.id)
    bree.say "About the party..."
    bree.say "I'll invite another one..."
    active_girl.say "Okay, don't worry."
    $ game.flags.halloween_girl = None
    $ active_girl.love -= 5
    $ renpy.hide(active_girl.id)
    return


label halloween_intro_female:

    scene bg house with fade
    "I can almost always tell when someone's trying to hide something from me."
    "Like, you get those subtle little hints that they're watching you closely."
    "Or they change the subject when you start to talk about a certain something."
    "But then again, there are times when people make it painfully obvious too."
    "Like the moment I walk into the sitting room and collapse onto one of the sofas."
    scene bg livingroom
    show mike happy at left4
    show sasha happy at right4
    with fade
    "I can clearly see that [mike.name] and Sasha were leaning towards each other."
    show mike surprised
    show sasha surprised
    pause 0.5
    show mike at left
    show sasha at right
    with ease
    "But the second they see me, the pair of them leap apart."
    "And as if they want to be even more suspicious, they end up on opposite ends of the sofa too!"
    bree.say "You know, you guys..."
    bree.say "It's totally cool with me."
    show mike annoyed
    show sasha normal
    "[mike.name] and Sasha were looking guilty before I spoke up."
    show mike surprised
    show sasha surprised
    "But now they kind of look more surprised and confused."
    mike.say "You...you are?"
    show sasha normal
    sasha.say "Shut up, [hero.name]..."
    sasha.say "You don't even know what we were doing just now!"
    show mike normal
    bree.say "Oh, I think I have a pretty good idea."
    bree.say "And sure, it might make things a little awkward at first."
    bree.say "But I'll be able to get used to you two being an item around here."
    show mike surprised
    show sasha surprised
    "[mike.name] and Sasha exchange an even more puzzled glance."
    show mike normal
    "Then they turn back to stare at me, both shaking their heads."
    show sasha joke
    sasha.say "We're not getting together!"
    sasha.say "That's the most ridiculous thing I ever heard!"
    show mike happy
    mike.say "Yeah, totally ridiculous!"
    show mike surprised
    mike.say "Wait...what?"
    show sasha normal
    "If Sasha even hears [mike.name]'s question, she ignores it and presses on regardless."
    sasha.say "We were just talking about something really important."
    sasha.say "Can you guess what it is?"
    show mike normal at left5 with ease
    "Before I can even think of an answer, [mike.name] leaps straight in."
    "It seems like he can't contain his excitement."
    "So he just has to let the cat out of the bag."
    "And he does that by reaching behind the sofa and pulling something out."
    "When he holds it up, I see that it's a pumpkin."
    "One that's been carved into a Jack O Lantern with a huge grin."
    "Almost as big as the one that's currently on [mike.name]'s own face."
    show mike happy at startle
    mike.say "Ta da!"
    mike.say "We're going to have a Halloween party!"
    mike.say "With music and games and it's going to be great!"
    show sasha annoyed
    "Sasha rolls her eyes and lets out a characteristic sigh."
    sasha.say "Way to give it away, [mike.name]!"
    "I shrug and shake my head, not sure what the fuss is about."
    show mike normal
    show sasha normal
    bree.say "Okay, guys..."
    bree.say "But why do you need to talk to me about it?"
    bree.say "It sounds like you already have the whole thing planned."
    show sasha annoyed
    "Sasha shoots [mike.name] a second withering look."
    sasha.say "We do, [hero.name]..."
    sasha.say "But [mike.name]'s getting a little ahead of himself."
    show sasha normal
    sasha.say "We also agreed that we need everyone in the house on board."
    mike.say "So we need you to agree to the party too."
    mike.say "Just say yes, and we can get started already!"
    "I take a moment to think about it, as [mike.name] and Sasha wait for my answer."
    "The thought of a Halloween party isn't that bad."
    "Certainly better than the idea of my housemates becoming a couple."
    "And Halloween is a holiday that I've always loved."
    "Ever since I was a kid going out trick or treating."
    "But do I really want a bunch of strangers in the house?"
    "Running around the place in silly costumes and being a nuisance?"
    menu:
        "Say no to the party":
            bree.say "It was very thoughtful of you both to ask me first."
            bree.say "But I don't want to have strangers wandering around the house."
            bree.say "And if everyone's in costumes, we don't know who they could be."
            bree.say "What if one of them turns out to be a real-life serial killer or something?"
            show mike sad
            "[mike.name]'s face falls the moment he hears me say no to the party."
            "All of the enthusiasm he had before vanishes, replaced with a sulking, sullen silence."
            show sasha annoyed
            "Sasha rolls her eyes and shakes her head at me, showing her disapproval too."
            sasha.say "Way to be a party-pooper, [hero.name]."
            mike.say "Yeah, [hero.name]..."
            mike.say "Some of us actually want to have fun around here!"
            $ game.flags.party_planned = False
        "Jump at the chance of the party":
            bree.say "Didn't I tell you already - Halloween's my favourite holiday!"
            bree.say "Of course we have to have a house Halloween party!"
            bree.say "I'm so glad you told me, because I have lots of great ideas."
            show mike happy
            "[mike.name] can't seem to contain himself once he hears my answer."
            "He actually claps his hands together and bounces up and down on the sofa."
            "Sasha manages to keep herself under control."
            "But I can see in her eyes that she's intrigued by my professed love of the holiday in question."
            "Well, she does like to dress in black most of the time."
            "And a lot of her favourite bands look like they could be in a horror movie too!"
            mike.say "Oh, and it's okay to bring a plus one..."
            mike.say "If you know what I mean?"
            sasha.say "Yeah, if you can think of anyone to bring along!"
            "Oh hell..."
            "Now I feel like they're putting me under some serious pressure."
            "Am I going to get a reputation as the one in the house that's always single?"
            "Urgh..."
            "I just hope I can think of someone to invite to the party in time."
            $ game.flags.party_planned = True
            $ hero.calendar.add(game.calendar.get_future_days_played("halloween"), LabelAppointment(20, ["mike", "sasha"], "Halloween Party", "halloween_event_female", fixed_hour=True))
    if 'halloween_event_female' in DONE:
        $ del DONE["halloween_event_female"]
    return

label halloween_event_female(appointment=None):
    if game.flags.party_planned:
        if renpy.has_label("halloween_achievement_1"):
            call halloween_achievement_1 from _call_halloween_achievement_1_1
        scene bg bedroom4 with fade
        "We've all been slaving away with the preparations for the party."
        "Determined to ensure the house looks as good as we can possibly make it."
        "And thanks to all of our hard work, it looks like the set of a horror movie."
        "And I mean that in a good way too!"
        "The place is filled with props and decorations that are both scary and fun."
        "But we took so long on it that we're almost too late to actually get ready ourselves."
        "Just before the guests are supposed to start turning up, we scuttle off to our rooms."
        "We've all kept quiet about what we're wearing to make sure it's a surprise."
        show bree halloween happy with dissolve
        "So as soon as I can pull on my own costume, I rush down the stairs to the hallway."
        "And I'm not disappointed with the sight that greets me when I get there."
        scene bg livingroom
        show mike halloween at right5
        show sasha halloween at left5
        with fade
        "[mike.name] and Sasha have really gone to town on this one!"
        show mike perv
        "But [mike.name]'s eyes almost pop out as soon as he sees my costume."
        mike.say "Wow..."
        mike.say "Just...wow!"
        bree.say "I knew you'd get it, [mike.name]."
        bree.say "We must have played that game for days!"
        mike.say "Yeah, [hero.name] - how could I forget Cindy?!?"
        mike.say "And, Sasha..."
        mike.say "You're really rocking the white hair!"
        sasha.say "I always thought I could pull 2B off."
        sasha.say "And the dress is just the icing on the cake!"
        "Sasha and I are still buzzing from [mike.name]'s compliments."
        "But then I see him gazing at us, expectation in his eyes."
        "The I realise he's waiting for us to return the gesture."
        "And we've kind of left him hanging!"
        bree.say "And you're supposed to be..."
        bree.say "Hmm...that guy from Tron?"
        bree.say "The one they had to de-age with CGI?"
        "[mike.name] looks instantly crest-fallen."
        show mike halloween blush
        mike.say "No, [hero.name] - I'm that guy in the original movie."
        "Sasha and I exchange a look of confusion."
        bree.say "There was another Tron movie?!?"
        sasha.say "So why a character from an ancient film?"
        show mike halloween b normal
        "[mike.name] rolls his eyes in frustration."
        mike.say "For your information, Sasha, it's a classic."
        mike.say "And he's a programmer - like me?"
        bree.say "Doesn't he like, get trapped in a game or something?"
        bree.say "That sounds like a nightmare!"
        "That really does sound like a fate worse than death."
        "I can't imagine the horror of having my life controlled by someone else!"
        play sound door_bell
        "But the sound of the doorbell makes me shake it off."
        "Time to focus on the real world and stop thinking about videogames."
        scene bg black with dissolve
        scene bg house
        with wiperight
        "I turn and open the door, only to find a sword sweeping down towards me."
        play sound woosh_punch
        with vpunch
        bree.say "AAARGH!"
        jack.say "Whoa!"
        jack.say "Sorry, [hero.name]!"
        show jack halloween happy
        "I open my eyes to see Jack standing on the doorstep."
        show jack halloween normal
        "The plastic sword is now at his side and he looks a little sheepish."
        scene bg livingroom
        show jack halloween normal
        show mike halloween at right
        show sasha halloween at left
        with fade
        "As I step aside to let him into the house, I see his costume for the first time."
        "He has on a pair of furry shorts and boots, and not much else."
        jack.say "I bring greetings from Cimmeria!"
        show sasha happy
        sasha.say "Hey - by the power of Greyskull!"
        jack.say "Huh?"
        show sasha normal
        sasha.say "You came as He-Man - right?"
        show mike happy
        mike.say "Uh-uh, Sasha - he's Conan!"
        show mike normal
        menu:
            "Agree with [mike.name]":
                "It'd be easy to laugh along with Sasha."
                "But Jack's a sweet guy, so I should defend him."
                bree.say "You're right, [mike.name]."
                $ mike.love += 1
                bree.say "He's Conan for sure."
                bree.say "He-Man has that strappy breastplate thing, and a bob haircut!"
                show jack halloween happy
                "Jack seems to recover himself a little."
                "He nods and cracks a weak smile."
                jack.say "Thanks, [hero.name]."
                show jack halloween normal
                jack.say "I spent ages on this costume!"
                show sasha annoyed
                "Sasha shakes her head at the three of us."
                sasha.say "Geez - lighten up, you guys!"
                sasha.say "This is supposed to be a party."
                show mike happy
                "But at the same time, I see [mike.name] smiling at me."
                if game.flags.halloween_girl == 'jack':
                    "Looks like my standing up for him went a long way."
                else:
                    "Looks like my standing up for Jack won his approval."
            "Agree with Sasha":
                "I can't help laughing at the look on Jack's face."
                "It's pretty obvious he's supposed to be Conan."
                "But He-Man is way funnier!"
                bree.say "Yeah, Jack - Sasha's right."
                show sasha joke
                $ sasha.love += 1
                bree.say "You look just like He-Man!"
                show jack sad
                "Jack looks visibly hurt."
                "His sword almost droops in his hand."
                jack.say "Hey - I spent ages on this costume!"
                show mike angry
                mike.say "Yeah, [hero.name], don't be mean!"
                show sasha happy
                "Sasha and I keep right on laughing."
                "But [mike.name] scowls at me and shakes his head."
                if game.flags.halloween_girl == 'jack':
                    "And Jack just lowers his head as he slinks inside the house."
                    "Which makes me begin to feel more than a little guilty."
                    "Perhaps I should find a way to make it up to him?"
                else:
                    show mike happy
                    "He makes an effort to comfort Jack as best he can."
                    "And I see an almost instant upturn in his mood as a result."
        play sound door_bell
        if game.flags.halloween_girl == 'scottie':
            "The doorbell rings and I hurry into the hallway to see who's turned up."
            "As I'm still the nearest to the door, I open it almost without thinking."
            scene bg black with dissolve
            scene bg house
            with wiperight
            "And instantly find myself staring at three sharp points an inch from my nose."
            with vpunch
            bree.say "Argh!"
            bree.say "What the hell?!?"
        else:
            "There's barely enough time to herd Jack in before the doorbell rings again."
            "As I'm still the nearest to the door, I open it almost without thinking."
            scene bg black with dissolve
            scene bg house
            with wiperight
            "And instantly find myself staring at three sharp points an inch from my nose."
            with vpunch
            "Fuck's sake - this is getting ridiculous!"
        show scottie halloween b
        scottie.say "Cower before by aquatic buffness!"
        "I blink at the sight of Scottie, clutching a rubber trident."
        "He has on an orange top and green leggings, both patterned with scales."
        "But what catches my attention the most is the ginger wig he's wearing."
        bree.say "Come on in, O lord of the deep!"
        scene bg livingroom
        show scottie halloween b
        show sasha halloween at left
        show mike halloween at right
        with fade
        "I have to cover my mouth to keep from laughing."
        show scottie halloween a surprised
        "And I can see a look of confusion on Scottie's face as I do so."
        scottie.say "Uh...what's up, [hero.name]?"
        show scottie halloween a normal
        scottie.say "I'm like Aquaman, yeah?"
        scottie.say "You know - the one the chicks are crazy about?"
        show mike happy
        mike.say "You're definitely Aquaman, Scottie."
        show sasha happy
        sasha.say "Yeah - but not the right Aquaman!"
        menu:
            "Defend Scottie":
                "Poor Scottie - he wanted to be the Jason Momoa version of Aquaman."
                "But someone sold him the classic version instead!"
                "It'd be the easiest thing in the world to laugh at him."
                "But I can see that Sasha's already looking sorry for the guy."
                bree.say "Hey, Scottie - I didn't know you were such a purist!"
                show scottie surprised
                scottie.say "I...I'm a what?!?"
                bree.say "Anyone else would've come as the Aquaman from the movies."
                bree.say "But only someone in the know would have come as classic Aquaman!"
                "It takes a few seconds for Scottie's brain to process this."
                show scottie b happy
                "But then he suddenly nods and smiles."
                scottie.say "Uh...yeah...that's right!"
                scottie.say "What you said, [hero.name]."
                "[mike.name]'s still chuckling to himself."
                show sasha happy
                "But Sasha shoots me a look of thanks."
                if game.flags.halloween_girl == 'scottie':
                    "Which is fine and all."
                    "But I did that for my own benefit, not for her!"
                else:
                    "Which is fine by me, as I did that for her, not Scottie!"
            "Make fun of Scottie":
                if game.flags.halloween_girl == 'scottie':
                    "I know that I should stand up for Scottie."
                    "But he just looks so dumb as he's standing there in that stupid costume."
                else:
                    "Maybe I should stand up for Scottie."
                    "But he just looks so dumb as he's standing there."
                "I can't help but give in."
                bree.say "Wow...that's pretty dumb, Scottie!"
                show scottie surprised
                scottie.say "Wha...what?!?"
                bree.say "You wanted to be the hot Aquaman from the movies."
                bree.say "But someone sold you a costume for the lame one from the comics!"
                "It seems to take a few seconds for Scottie's brain to process this."
                "And then he starts to shake his head and splutter."
                show scottie angry
                scottie.say "Aw, dammit!"
                scottie.say "That was why the guy in the costume shop was laughing!"
                scottie.say "How am I supposed to know all this nerd stuff?!?"
                show sasha angry
                "Sasha shoots me a look that could curdle milk."
                show sasha happy
                "She starts trying to stroke Scottie's bruised ego."
                if game.flags.halloween_girl == 'scottie':
                    "And [mike.name], keeps on sniggering the whole time."
                    "But as I watch Sasha showing Scottie into the house, I realise I might have fucked up."
                    "And I hurry after them, already looking for a chance to get Sasha out of the picture."
                else:
                    "And she makes a point of turning away from me as she does so."
                    "All the time, [mike.name] keeps on sniggering behind his hand."
        "Is that everyone that we invited?"
        hide mike
        hide sasha
        hide scottie
        with fade
        if game.flags.halloween_girl in ["jack", "scottie"]:
            "That's the last of them."
            "Now it's time to get on with hosting the party."
            call nodate_halloween_party_female from _call_nodate_halloween_party_female
            call nodate_halloween_dance_female from _call_nodate_halloween_dance_female
            $ game.hour = 0
            if game.flags.halloween_girl == "scottie" and Person.find(game.flags.halloween_girl).sexperience >= 1:
                call expression game.flags.halloween_girl + "_halloween_sex_female" from _call_expression_530


            scene bg black with dissolve
            call sleep (game.flags.halloween_girl) from _call_sleep_93
        elif game.flags.halloween_girl:
            "Suddenly I realise that my heart is pounding in my chest."
            "I wonder what's the matter with me, and then I remember."
            "The only other guest that we're waiting for is my own date."
            "And so the next person at the door should be my guest!"
            call expression game.flags.halloween_girl + "_halloween_arrival_female" from _call_expression_474
            call expression game.flags.halloween_girl + "_halloween_party_female" from _call_expression_475
            call expression game.flags.halloween_girl + "_halloween_dance_female" from _call_expression_476
            $ game.hour = 0
            if game.flags.halloween_girl in ["mike", "angela", "ayesha", "dwayne", "lexi", "sasha", "shawn", "master"] and Person.find(game.flags.halloween_girl).sexperience >= 1:
                call expression game.flags.halloween_girl + "_halloween_sex_female" from _call_expression_477


            scene bg black with dissolve
            call sleep (game.flags.halloween_girl) from _call_sleep_94
        else:
            "That's the last of them."
            "Now it's time to get on with hosting the party."
            call nodate_halloween_party_female from _call_nodate_halloween_party_female_1
            call nodate_halloween_dance_female from _call_nodate_halloween_dance_female_1
        $ game.flags.party_planned = False
        $ game.flags.halloween_girl = None
        $ hero.energy -= 3
        $ hero.hunger -= 3
        $ hero.grooming -= 3
        $ hero.fun += 6
        $ game.room = "bedroom4"
    $ del DONE["halloween_intro_female"]
    return

label nodate_halloween_party_female:
    scene bg black with timelaps
    pause 1
    $ game.pass_time(2)
    scene bg livingroom with timelaps
    "By now the party is well and truly underway."
    "All of the guests we're expecting are here."
    "They're standing around, chatting in little groups."
    "And some are even dancing on the makeshift dancefloor."
    "Even the pretty cheesy Halloween soundtrack we put together is going down well."
    "I can feel all of my worries starting to fade away at last."
    "And now that we're all having fun, time seems to pass more quickly."
    "That is until I hear the sound of people raising their voices."
    "At first I thought it was just the sound of the music playing in the house."
    "But there's nothing mistaking Sasha and [mike.name]'s voices when they're upset about something."
    "Hurrying to follow the sound, I find them by the table in the dining room."
    "That's where we set up the food for tonight, all of it with a Halloween theme."
    "There's a bowl of punch, some candy - that kind of thing."
    "Not a feast that would feed an army or anything crazy like that."
    "Just enough for everyone to have a snack if they get peckish."
    "Now I see Sasha and [mike.name] standing on one side of the food."
    "Both of them glaring in disapproval across the table."
    "Looking to the other side, I see Jack and Scottie."
    "They're staring at their feet, looking decidedly sheepish."
    "And both of them are clutching plates."
    "Plates almost overflowing with food from the table."
    scene bg kitchen
    show mike halloween annoyed at right5
    show sasha halloween annoyed at mostright5
    show scottie halloween at mostleft5
    show jack halloween normal at left5
    with fade
    "As soon as I walk into the room, they all start talking at once."
    show mike angry
    mike.say "Can you believe these guys, [hero.name]?!?"
    mike.say "If they eat all that, there won't be enough to go round!"
    show sasha vangry
    sasha.say "Yeah, [mike.name]'s right - they're a pair of pigs!"
    show mike annoyed
    show sasha annoyed
    "Now that Sasha and [mike.name] have spoken, Jack and Scottie chime up too."
    "The pair of them leaping to their own defence."
    jack.say "Hey, that's a mean thing to say!"
    jack.say "I was just a little hungry, that's all."
    show scottie angry
    scottie.say "Right, man!"
    scottie.say "We didn't know you were so precious about this stuff!"
    "Well, at least they all managed to say their piece."
    "But now they all seem to be staring at me."
    "Ah crap, they must want me to wade in on this one."
    "And I bet they all think I'm going to side with them too!"
    menu:
        "Side with [mike.name] and Sasha":
            "Maybe we should have put up a sign or told people when they arrived."
            "But then Jack and Scottie are both adults."
            "You'd think they had the manners not to hoover it all up!"
            bree.say "I don't remember saying this was an all you can eat buffet!"
            bree.say "If you were that hungry, you should have eaten before you came."
            $ mike.love += 1
            $ sasha.love += 1
            "[mike.name] and Sasha choose now to pile in and vent their frustrations as well."
            show mike angry
            mike.say "Okay, you two can eat what's on your plates."
            mike.say "But then you don't come near this table again all night!"
            show sasha vangry
            sasha.say "And you'd better hope there's still enough to feed the rest of us."
            sasha.say "Because if it does, you're paying for pizza for everyone else!"
            show mike annoyed
            show sasha annoyed
            show jack sad
            jack.say "Aww..."
            jack.say "That's so unfair!"
            show scottie sad
            scottie.say "But...uh..."
            scottie.say "If we do have to get pizza..."
            scottie.say "We can have some too, right?"
            show mike angry
            show sasha vangry
            "[mike.name] and Sasha roll their eyes and groan at this."
            mike.say "How can you STILL be hungry?"
            sasha.say "Have you got a tapeworm or something?!?"
        "Side with Jack and Scottie":
            "I can see why it's so annoying Jack and Scottie went crazy."
            "But then maybe we should have told them or put up a sign."
            "After all, the food is for the guests, which includes them."
            bree.say "Don't be so hard on them, guys."
            bree.say "This is a party, after all."
            $ mike.love -= 1
            $ sasha.love -= 1
            "All this seems to do is make [mike.name] and Sasha more angry."
            "Jack and Scottie, on the other hand, move to back me up."
            show jack halloween happy
            jack.say "You guys did such a good job."
            jack.say "We just couldn't stop ourselves!"
            show scottie halloween happy
            scottie.say "Y...yeah...what he said!"
            scottie.say "Best buffet I've seen in SO long."
            show mike happy
            mike.say "Oh..."
            mike.say "You really think so?"
            mike.say "Thanks, guys!"
            "[mike.name] seems to have been won over by their flattery."
            show mike normal
            show sasha angry
            "But Sasha's made of sterner stuff."
            sasha.say "Well, you'd better hope the food doesn't run out."
            show sasha vangry
            sasha.say "Because if it does, you're paying for pizza for everyone else!"
            show sasha angry
            show jack halloween sad
            jack.say "Aww..."
            jack.say "That's so unfair!"
            show scottie sad
            scottie.say "But...uh..."
            scottie.say "If we do have to get pizza..."
            scottie.say "We can have some too, right?"
            show mike angry
            "[mike.name] and Sasha roll their eyes and groan at this."
            bree.say "How can you STILL be hungry?"
            sasha.say "Have you got a tapeworm or something?!?"
    return


label nodate_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom with fade
    "I feel like I haven't stopped running around since the party started"
    "And looking at the time, I realise that it's been a good few hours since then."
    "What's worse, I haven't even had the chance to hit the dancefloor yet!"
    "I mean, I know that I don't have a date tonight, but that's no reason to lose out."
    "But who should I ask to dance with me?"
    menu:
        "[mike.name]":











































            show mike halloween with dissolve
            "A quick glance around the room and I spot [mike.name] standing on his own."
            "He looks about as tired and harassed as I feel myself."
            "So maybe he'd appreciate the chance to have some fun?"
            bree.say "Hey, [mike.name]..."
            bree.say "You want to dance with me?"
            show mike surprised
            "[mike.name] looks a little surprised at the question."
            "But not surprised in a bad way, you know?"
            "More like it's unexpected, but not unwelcome."
            show mike happy
            $ mike.love += 2
            mike.say "Sure, [hero.name]..."
            mike.say "That sounds like fun!"
            mike.say "If you're sure you want to dance with me?"
            "By way of an answer, I take hold of [mike.name]'s hand."
            "And then I lead him out, onto the dance-floor."
            hide mike
            show dance mike halloween
            with fade
            "And as soon as we start dancing, the music doesn't seem to matter."
            "All that does is the fact we're together and having a good time."
            "I'm cool with keeping things light and fun."
            "But I soon get the impression [mike.name] has other things in mind."
            "He dances as close to me as he can."
            "And he seems to be pressed close against me the whole time."
            "I'm not complaining about this, not at all."
            "In fact, I can already feel him stiffening in a certain area!"
            "[mike.name] seems to notice this too."
            "He's blushing, trying to pull away from me as he realises."
            mike.say "Oh..."
            mike.say "Oh shit..."
            mike.say "Sorry, [hero.name]!"
            "I shake my head, dismissing his concerns."
            bree.say "It's okay, [mike.name]..."
            bree.say "You're a guy."
            bree.say "And these things happen to guys."
            "We keep on dancing for a while longer, and I keep quiet the whole time."
            "But all the while my mind is racing."
            "Because I never knew I had that effect on [mike.name]."




































































    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
