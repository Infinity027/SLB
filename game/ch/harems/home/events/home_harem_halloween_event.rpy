init python:
    SpecificTalkSubject(**{
    "name": "halloween_invite",
    "display_name": "Invite at the party",
    "label": "halloween_invite",
    "icon": "button_askhalloween",
    "conditions": [
        IsSeason(2),
        HeroTarget(
            IsGender("male"),
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
            IsGender("female"),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "do_once": False,
    "once_day": "ACTIVE",
    "duration": 0,
    })

    SpecificTalkSubject(**{
    "name": "cancel_halloween_invite",
    "display_name": "Cancel invitation",
    "label": "cancel_halloween_invite",
    "icon": "button_aborthalloween",
    "conditions": [
        HeroTarget(
            IsGender("male"),
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
    "once_day": "ACTIVE",
    "duration": 0,
    })

    Event(**{
    "name": "halloween_intro",
    "priority": 1000,
    "label": "halloween_intro",
    "conditions": [
        IsNotDone("halloween_intro"),
        IsDone("scottie_appears", "jack_event_01"),
        IsSeason(2),
        'game.calendar.day_of_season in [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]',
        IsHour(20, 23),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            IsActivity("None"),
            ),
        PersonTarget(bree,
            HasRoomTag("home"),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            HasRoomTag("home"),
            Not(IsHidden())
            ),
        ],
    "once_day": True,
    })
























    Event(**{
    "name": "halloween_party_cancelled",
    "label": "halloween_party_cancelled",
    "priority": 1000,
    "conditions": [
        IsSeason(2),
        IsDone("halloween_intro"),
        HeroTarget(
            IsGender("male"),
            IsFlag("party_planned"),
            ),
        Or(
            PersonTarget(bree,
                Or(
                    IsHidden(),
                    IsGone(),
                    ),
                ),
            PersonTarget(sasha,
                Or(
                    IsHidden(),
                    IsGone(),
                    ),
                ),
            )
        ],
    })

label halloween_invite:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_231
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_halloween_invitation"):
        call expression f"{active_girl.id}_halloween_invitation" from _call_expression_232
    else:
        mike.say "Have you made any plans for Halloween yet?"
        active_girl.say "Yes, I have something planed."
        mike.say "Oh..."
        active_girl.say "Sorry [hero.name], maybe next year?"
        mike.say "Sure..."
    $ renpy.hide(active_girl.id)
    return

label cancel_halloween_invite:
    $ active_girl.set_flag("interact", 1, 1, "+")
    call expression f"{active_girl.id}_greet" from _call_expression_233
    $ renpy.show(active_girl.id)
    mike.say "About the party..."
    mike.say "I'll invite another one..."
    active_girl.say "Okay, don't worry."
    $ game.flags.halloween_girl = None
    $ active_girl.love -= 5
    $ renpy.hide(active_girl.id)
    return

label halloween_intro:
    scene bg house with fade
    "Did you ever have one of those times when you walked into a room and you were greeted with what you could only describe as a pregnant silence?"
    "You know what I mean - when you walk in on somebody else having a conversation and the moment that they see it's you, everything goes instantly silent?"
    scene bg livingroom
    show bree happy at left4
    show sasha happy at right4
    with fade
    "Well that's what happens as soon as I open the door to the living room to see [bree.name] and Sasha deep into discussing something."
    show bree surprised
    show sasha surprised
    pause 0.5
    show bree evil at left
    show sasha normal at right
    with move
    "They were leaning in close no more than a split second ago, and now they're both sitting bolt upright and trying to look like there's nothing going on."
    "Genuinely more interested in flopping down on one of the sofas and watching something mindless to relax at the end of the day, I decide to play along."
    "And so making no effort to ask what's so scandalous that they need to shut up at the mere sight of me, I find a free spot and begin to search for the remote."
    show bree normal
    "I can feel their eyes on me even as I do so, and I actually quite enjoy torturing them by not asking the question that they're both begging for me to ask."
    "Finding something that I can stick on the TV as visual chewing gum, I steal an innocent look in their direction."
    show bree blush blush
    show sasha annoyed
    "Sasha looks suitably irritated at my ignoring them, and [bree.name] seems almost ready to explode with suppressed excitement."
    "So that requires just a little bit more torture before I give in and indulge them."
    mike.say "Hey, you guys..."
    "I'm sure to make my voice sound curious and yet drag out every word in order to prolong their agony."
    hide bree
    show bree normal at left
    pause 0.1
    show bree normal at left5
    show sasha normal at right5
    with move
    "I see both of the girls suddenly sitting up and paying attention, like Pavlov's dogs at the sound of the bell."
    mike.say "What...kind of a day did you both have at work?"
    "They hang on my every word until the moment that I swerve them by asking a completely unrelated question."
    show bree annoyed
    show sasha angry
    "Sasha's eyes go wide and I could swear that I see Hellfire blossom inside of her pupils."
    "[bree.name], on the other hand, simply lets out a high-pitched yelp that serves both to show her displeasure and let me know that I've reached the end of my allotted rope."
    mike.say "Okay, okay...I'm sorry really I am!"
    mike.say "What were you talking about when I walked in just now?"
    show sasha joke
    show bree normal
    "Sasha fixes me with a sardonic look on her face, crossing her arms over her chest as though she intends to make me work for the information."
    "But then her efforts are completely ruined, as [bree.name] reaches behind the sofa and pulls out a rather large Jack-O-Lantern."
    show sasha normal
    show bree happy at startle
    "She holds it up next to her face, and I'm hard-pressed to tell which one of the two has the wider smile."
    bree.say "We're planning a Halloween party - and it's gonna be totally awesome!"
    sasha.say "Yeah, what she said!"
    "Well, that's not the most sinister of things that they could have been discussing behind my back."
    mike.say "Oh, I see...but why all the secrecy?"
    show bree normal
    mike.say "Why not just come straight out and tell me when I came in?"
    sasha.say "Well, we figured that we needed to have you on board before we could start to make any actual plans."
    bree.say "Yeah, as we're kind of a democracy, we wanted to get your vote, [hero.name]."
    "I don't know about this place being a democracy."
    "Most of the time it feels more like pure anarchy, at least to me."
    "But I guess that I should be grateful that they felt the need to actually ask me, rather than just going ahead and doing it regardless of my feelings."
    menu:
        "Turn down the party":
            mike.say "Thanks for the head's up, guys - that's really thoughtful of you."
            mike.say "But Halloween's never really been my thing, you know?"
            mike.say "What can I say - I guess I'm more Brady Bunch than Addams Family!"
            show bree sad
            show sasha annoyed
            "[bree.name] looks instantly crestfallen, all of the energy that she's put into the announcement turning into disappointment."
            "Sasha makes a dejected grunt that I interpret as meaning that I'm both a party-pooper and a square."
            "I can only shrug and smile helplessly, not happy to have let them down and yet trying to cling to the reassurance that I've at the very least been honest."
            $ game.flags.party_planned = False
        "Jump at the chance of the party":
            mike.say "How could you guys not know that Halloween's my absolute favourite holiday?!?"
            mike.say "Of course I want us to have a Halloween party!"
            mike.say "Not just that - I want it to be the best Halloween party that we can possibly make it!"
            show bree happy
            "[bree.name] lets out a cry of sheer delight and claps her hands together at my enthusiasm."
            "Sasha, as usual, is somewhat more reserved - but I can see in her eyes that she's at least intrigued by my professed love of the holiday in question."
            "After all, what other time of year would her favoured choice of dress be considered practically normal?"
            $ game.flags.party_planned = True
            $ renpy.dynamic("party_participants")
            if Harem.find_by_name("home"):
                $ party_participants = list({"bree", "sasha"} | set(Harem.find_by_name("home").active_members))
            else:
                $ party_participants = ["bree", "sasha"]
            $ hero.calendar.add(game.calendar.get_future_days_played("halloween"), LabelAppointment((20, 22), party_participants, "Halloween Party", "halloween_event", "halloween_party_missed"))
    if 'halloween_event' in DONE:
        $ del DONE["halloween_event"]
    return

label halloween_party_missed:
    "Shit, I missed the Halloween party. The girls are going to be mad."
    $ bree.love -= 4
    $ sasha.love -= 4
    $ del DONE["halloween_intro"]
    return

label halloween_party_cancelled:
    if bree.hidden and sasha.hidden:
        "[bree.name] and Sasha are not available for Halloween."
    if bree.hidden:
        "[bree.name] is not available for Halloween."
    if sasha.hidden:
        "Sasha is not available for Halloween."
    "I have to cancel the party."
    $ hero.calendar.find_and_remove(label="halloween_event")
    $ del DONE["halloween_intro"]
    return

label halloween_event(appointment=None):
    if game.flags.party_planned:
        $ game.flags.disable_clothing_policy = True
        if renpy.has_label("halloween_achievement_1") and not game.flags.cheat:
            call halloween_achievement_1 from _call_halloween_achievement_1
        scene bg bedroom1 with fade
        "Everyone's been working hard to get things ready for the party on time."
        "And thanks to our efforts, the house looks like the set of a horror movie."
        "Don't get me wrong - I mean that in a good way!"
        "It's strewn with decorations and props that give it a spooky, but fun vibe."
        "In fact, we've worked so hard that there's barely enough time to get ourselves ready."
        "At the last moment, just before the guests are supposed to arrive, we all hurry off to our rooms."
        "Nobody's told anyone else what we're coming to the party as, so this should be a surprise."
        "After clambering into my costume, I hurry out and into the hallway."
        scene bg livingroom
        show bree halloween at right
        show sasha halloween at left
        with fade
        "And the sight I'm presented with is pretty impressive, I have to admit!"
        "Honestly - I wish I had enough eyes to stare at all of them at once!"
        mike.say "Wow..."
        mike.say "Just...wow!"
        show bree wink
        bree.say "I knew you'd get it, [hero.name]."
        bree.say "We must have played that game for days!"
        show bree normal
        mike.say "Yeah, [bree.name] - how could I forget Sindee?!?"
        mike.say "And, Sasha..."
        mike.say "You're really rocking the white hair!"
        sasha.say "I always thought I could pull B2 off."
        sasha.say "And the dress is just the icing on the cake!"
        if Person.is_not_hidden("lexi") and Harem.together(bree, sasha, lexi, minami, samantha, name='home'):
            lexi.say "Hey, you guys aren't the only ones that know videogames!"
            show lexi halloween wink with dissolve
            lexi.say "Check me out - I make a pretty good Julie, huh?"
            mike.say "No kidding, Lexi."
            mike.say "Is that a real chainsaw too?!?"
            minami.say "Hey!"
            hide bree
            show minami halloween tehe at right
            with fade
            minami.say "What about me, big bro?!?"
            mike.say "Whoa, Minami..."
            mike.say "You never wore anything like that when we were at school!"
            samantha.say "I hope you like my costume, [hero.name]."
            hide sasha
            show samantha halloween at left
            with fade
            samantha.say "I didn't count on it being this tight!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh no, Cupcake - you look amazing."
            else:
                mike.say "Oh no, Sam - you look amazing."
            mike.say "Spider Cutey never looked better!"
            hide lexi
            hide minami
            hide samantha
            show bree halloween at right
            show sasha halloween at left
            with fade
        elif Person.is_not_hidden("lexi") and Harem.together(bree, sasha, lexi, minami, name='home'):
            lexi.say "Hey, you guys aren't the only ones that know videogames!"
            show lexi halloween wink with dissolve
            lexi.say "Check me out - I make a pretty good Julie, huh?"
            mike.say "No kidding, Lexi."
            mike.say "Is that a real chainsaw too?!?"
            minami.say "Hey!"
            hide lexi
            show minami halloween tehe
            with fade
            minami.say "What about me, big bro?!?"
            mike.say "Whoa, Minami..."
            mike.say "You never wore anything like that when we were at school!"
            hide minami
        elif Person.is_not_hidden("lexi") and Harem.together(bree, sasha, lexi, samantha, name='home'):
            lexi.say "Hey, you guys aren't the only ones that know videogames!"
            show lexi halloween wink with dissolve
            lexi.say "Check me out - I make a pretty good Julie, huh?"
            mike.say "No kidding, Lexi."
            mike.say "Is that a real chainsaw too?!?"
            samantha.say "I hope you like my costume, [hero.name]."
            hide lexi
            show samantha halloween
            with fade
            samantha.say "I didn't count on it being this tight!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh no, Cupcake - you look amazing."
            else:
                mike.say "Oh no, Sam - you look amazing."
            mike.say "Spider Cutey never looked better!"
            hide samantha
        elif Harem.together(bree, sasha, minami, samantha, name='home'):
            minami.say "Hey!"
            show minami halloween tehe with dissolve
            minami.say "What about me, big bro?!?"
            mike.say "Whoa, Minami..."
            mike.say "You never wore anything like that when we were at school!"
            samantha.say "I hope you like my costume, [hero.name]."
            hide minami
            show samantha halloween
            with fade
            samantha.say "I didn't count on it being this tight!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh no, Cupcake - you look amazing."
            else:
                mike.say "Oh no, Sam - you look amazing."
            mike.say "Spider Cutey never looked better!"
            hide samantha
        elif Person.is_not_hidden("lexi") and Harem.together(bree, sasha, lexi, name='home'):
            lexi.say "Hey, you guys aren't the only ones that know videogames!"
            show lexi halloween wink with dissolve
            lexi.say "Check me out - I make a pretty good Julie, huh?"
            mike.say "No kidding, Lexi."
            mike.say "Is that a real chainsaw too?!?"
            hide lexi
        elif Harem.together(bree, sasha, minami, name='home'):
            minami.say "Hey!"
            show minami halloween tehe with dissolve
            minami.say "What about me, big bro?!?"
            mike.say "Whoa, Minami..."
            mike.say "You never wore anything like that when we were at school!"
            hide minami
        elif Harem.together(bree, sasha, samantha, name='home'):
            samantha.say "I hope you like my costume, [hero.name]."
            show samantha halloween
            samantha.say "I didn't count on it being this tight!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh no, Cupcake - you look amazing."
            else:
                mike.say "Oh no, Sam - you look amazing."
            mike.say "Spider Cutey never looked better!"
            hide samantha
        show mike halloween
        with fade
        bree.say "And you're supposed to be..."
        bree.say "Hmm...that guy from Tron?"
        bree.say "The one they had to de-age with CGI?"
        show mike halloween blush
        mike.say "No, [bree.name] - I'm that guy in the original movie."
        bree.say "There was another Tron movie?!?"
        sasha.say "So why a character from an ancient film?"
        show mike halloween b normal
        "I roll my eyes in frustration."
        mike.say "For your information, Sasha, it's a classic."
        mike.say "And he's a programmer - like me?"
        bree.say "Doesn't he like, get trapped in a game or something?"
        bree.say "That sounds like a nightmare!"
        show mike halloween a
        "I nod, instantly shuddering at the mere thought of such a fate."
        show mike halloween down
        "I can't imagine the horror of having my life controlled by someone else!"
        show mike halloween normal
        play sound door_bell
        "But the sound of the doorbell makes me shake it off."
        "Time to focus on the real world and stop thinking about videogames."
        scene bg black with dissolve
        pause 0.1
        scene bg house
        with wiperight
        "I turn and open the door, only to find a sword sweeping down towards me."
        play sound woosh_punch
        with vpunch
        mike.say "AAARGH!"
        jack.say "Whoa!"
        jack.say "Sorry, man!"
        show jack halloween happy
        "I open my eyes to see Jack standing on the doorstep."
        show jack halloween normal
        "The plastic sword is now at his side and he looks a little sheepish."
        scene bg livingroom
        show jack halloween normal
        show bree halloween at right
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
        show bree happy
        bree.say "Uh-uh, Sasha - he's Conan!"
        show bree normal
        menu:
            "Agree with [bree.name]":
                "It'd be easy to laugh along with Sasha."
                "But Jack's my friend, so I should defend him."
                mike.say "You're right, [bree.name]."
                $ bree.love += 1
                mike.say "He's Conan for sure."
                mike.say "He-Man has that breastplate, and a bob haircut!"
                show jack halloween happy
                "Jack seems to recover himself a little."
                "He nods and cracks a weak smile."
                jack.say "Thanks, man."
                show jack halloween normal
                jack.say "I spent ages on this costume!"
                show sasha annoyed
                "Sasha shakes her head at the three of us."
                sasha.say "Geez - lighten up, you guys!"
                sasha.say "This is supposed to be a party."
                show bree happy
                "But at the same time, I see [bree.name] smiling at me."
                "Looks like my standing up for Jack won her approval."
            "Agree with Sasha":
                "I can't help laughing at the look on Jack's face."
                "It's pretty obvious he's supposed to be Conan."
                "But He-Man is way funnier!"
                mike.say "Yeah, Jack - Sasha's right."
                show sasha joke
                $ sasha.love += 1
                mike.say "You look just like He-Man!"
                show jack sad
                "Jack looks visibly hurt."
                "His sword almost droops in his hand."
                jack.say "Hey - I spent ages on this costume!"
                show bree angry
                bree.say "Yeah, [hero.name], don't be mean!"
                show sasha happy
                "Sasha and I keep right on laughing."
                "But [bree.name] scowls at me and shakes her head."
                show bree happy
                "She makes an effort to comfort Jack as best she can."
                "And I see an almost instant upturn in his mood as a result."
        play sound door_bell
        "There's barely enough time to herd Jack in before the doorbell rings again."
        "As I'm still the nearest to the door, I open it almost without thinking."
        scene bg black with dissolve
        pause 0.1
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
        mike.say "Come on in, O lord of the deep!"
        scene bg livingroom
        show scottie halloween b
        show sasha halloween at left
        show bree halloween at right
        with fade
        "I have to cover my mouth to keep from laughing."
        show scottie halloween a sad
        "And I can see a look of confusion on Scottie's face as I do so."
        show scottie halloween a -sad
        scottie.say "Uh...what's up, dude?"
        scottie.say "I'm like Aquaman, yeah?"
        scottie.say "You know - the one the chicks are crazy about?"
        sasha.say "You're definitely Aquaman, Scottie."
        show bree happy
        bree.say "Oh dear - but not the right Aquaman!"
        menu:
            "Agree with Sasha":
                "Poor Scottie - he wanted to be the Jason Momoa version of Aquaman."
                "But someone sold him the classic version instead!"
                "It'd be the easiest thing in the world to laugh at him."
                show sasha sad
                "But I can see that Sasha's already looking sorry for the guy."
                mike.say "Hey, Scottie - I didn't know you were such a purist!"
                scottie.say "I...I'm a what?!?"
                mike.say "Anyone else would've come as the Aquaman from the movies."
                mike.say "But only someone in the know would have come as classic Aquaman!"
                "It takes a few seconds for Scottie's brain to process this."
                show scottie halloween b blush
                "But then he suddenly nods and smiles."
                scottie.say "Uh...yeah...that's right!"
                scottie.say "What you said, dude."
                "[bree.name]'s still chuckling to herself."
                show sasha happy
                "But Sasha shoots me a look of thanks."
                $ sasha.love += 1
                "Which is fine by me, as I did that for her, not Scottie!"
            "Agree with [bree.name]":
                "Maybe I should stand up for Scottie."
                "But he just looks so dumb as he's standing there."
                "I can't help but give in."
                mike.say "Wow...that's pretty dumb, Scottie!"
                show scottie halloween a angry
                scottie.say "Wha...what?!?"
                mike.say "You wanted to be the hot Aquaman from the movies."
                mike.say "But someone sold you a costume for the lame one from the comics!"
                "It seems to take a few seconds for Scottie's brain to process this."
                "And then he starts to shake his head and splutter."
                scottie.say "Aw, dammit!"
                scottie.say "That was why the guy in the costume shop was laughing!"
                scottie.say "How am I supposed to know all this nerd stuff?!?"
                show sasha angry
                "Sasha shoots me a look that could curdle milk."
                "She starts trying to stroke Scottie's bruised ego."
                "And she makes a point of turning away from me as she does so."
                $ bree.love += 1
                "All the time, [bree.name] keeps on sniggering behind her hand."
        hide bree
        hide sasha
        hide scottie
        with dissolve
        if game.flags.halloween_girl:
            "Suddenly I realise that my heart is pounding in my chest."
            "I wonder what's the matter with me, and then I remember."
            "The only other guest that we're waiting for is my own date."
            "And so the next person at the door should be her!"
            call expression game.flags.halloween_girl + "_halloween_arrival" from _call_expression_234
            call expression game.flags.halloween_girl + "_halloween_party" from _call_expression_235
            call expression game.flags.halloween_girl + "_halloween_dance" from _call_expression_236
            $ game.hour = 0
            if game.flags.halloween_girl != "nodate" and Person.find(game.flags.halloween_girl).sexperience >= 1:
                call expression game.flags.halloween_girl + "_halloween_sex" from _call_expression_237
                scene bg black with dissolve
                call sleep (game.flags.halloween_girl) from _halloween_event_girl
            else:
                scene bg black with dissolve
                call sleep from _call_sleep_123
        else:
            "That's the last of them."
            "Now it's time to get on with hosting the party."
            call nodate_halloween_party from _call_nodate_halloween_party
            call nodate_halloween_dance from _call_nodate_halloween_dance
        $ game.flags.party_planned = False
        $ game.flags.halloween_girl = None
        $ hero.energy -= 3
        $ hero.hunger -= 3
        $ hero.grooming -= 3
        $ hero.fun += 6
        $ game.room = "bedroom1"
        $ game.flags.disable_clothing_policy = False
    $ del DONE["halloween_intro"]
    return

label nodate_halloween_party:
    scene bg black with dissolve
    pause 1
    $ game.pass_time(2)
    scene bg livingroom with dissolve
    "The party seems to be getting off to a good start."
    "Everyone is either chatting away happily."
    "Or else they're dancing on the makeshift dance-floor."
    "And the Halloween playlist we put together is the perfect soundtrack."
    "I feel myself getting into the spirit of the thing as well."
    "Time seems to just fly by as we're all having fun."
    "It's only when I hear the sound of raised voices that I snap out of it."
    "At first I think it's just somebody shouting to be heard over the music."
    "But then I recognise the sound of [bree.name] and Sasha in a distinctly bad mood."
    "I follow their voices and find them standing by the table in the dining room."
    "We set this up with a Halloween-themed array of food and drink beforehand."
    "There's a punch, bowls of candy and other things to eat."
    "It's not an epic feats by any means."
    "But we thought people might want a snack during the party."
    scene bg kitchen
    show bree halloween annoyed at right5
    show sasha halloween annoyed at mostright5
    show scottie halloween at mostleft5
    show jack halloween normal at left5
    with fade
    "When I get to the source of the noise, I see [bree.name] and Sasha standing on one side of it."
    "Their faces are stern and disapproving as they stare across the table."
    "Jack and Scottie stand on the other side, looking distinctly sheepish."
    "And I notice that both of them are clutching plates."
    "Plates that are piled dangerously high with food from the table."
    "At the sight of me, everyone seems to come alive."
    show bree angry
    bree.say "Can you believe these guys, [hero.name]?!?"
    show sasha vangry
    sasha.say "Yeah, [bree.name]'s right - they're a pair of pigs!"
    show bree annoyed
    show sasha annoyed
    "Before I can say a word, Jack and Scottie begin talking."
    "Both of them leaping to their own defence."
    jack.say "Hey, that's not fair!"
    jack.say "We were just hungry, that's all!"
    show scottie angry
    scottie.say "Right, man!"
    scottie.say "We didn't know this stuff was being rationed!"
    "It looks like everyone's said their piece."
    "And now they're all staring at me."
    "They obviously expect me to settle the matter."
    "But I get the feeling they all think I'm going to side with them too!"
    menu:
        "Side with [bree.name] and Sasha":
            "I get that nobody told Jack and Scottie to go easy on the food."
            "But the pair of them are supposed to be adults."
            "And they should have the basic manners not to eat everything!"
            mike.say "I don't remember saying we were putting on a feast!"
            mike.say "You guys really should have eaten something before you got here."
            $ bree.love += 1
            $ sasha.love += 1
            "Jumping at the support I'm giving them, [bree.name] and Sasha pile on too."
            show bree angry
            bree.say "You two can eat what's on your plates."
            bree.say "But I don't want to see you near this table again!"
            show sasha vangry
            sasha.say "And you'd better hope the food doesn't run out."
            sasha.say "Because if it does, you're ordering pizza for everyone else!"
            show bree annoyed
            show sasha annoyed
            jack.say "Aww..."
            jack.say "That's so unfair!"
            show scottie sad
            scottie.say "But...uh..."
            scottie.say "If we do have to get pizza..."
            scottie.say "We can have some too, right?"
            show sasha vangry
            "[bree.name] and Sasha roll their eyes and groan at this."
            bree.say "How can you STILL be hungry?"
            sasha.say "Have you got a tapeworm or something?!?"
        "Side with Jack and Scottie":
            "I get that [bree.name] and Sasha are pissed the guys went crazy."
            "But they're right that we didn't tell them to go easy."
            "And the food was supposed to be for the guests too."
            mike.say "Ah, come on - this is supposed to be a party."
            mike.say "Who wants to spend all night arguing?"
            $ bree.love -= 1
            $ sasha.love -= 1
            "[bree.name] and Sasha bristle at my dismissing their concerns."
            "But Jack and Scottie are quick to back me up."
            show jack halloween happy
            jack.say "It just looked so good, you guys."
            jack.say "We couldn't help ourselves!"
            scottie.say "Yeah, that's right."
            scottie.say "Best I've had in ages!"
            show bree normal
            bree.say "Oh..."
            bree.say "You really think so?"
            "[bree.name] might have been swayed by their sudden flattery."
            "But Sasha's made of sterner stuff."
            sasha.say "Well, you'd better hope the food doesn't run out."
            show sasha vangry
            sasha.say "Because if it does, you're ordering pizza for everyone else!"
            show sasha angry
            show jack halloween normal
            jack.say "Aww..."
            jack.say "That's so unfair!"
            show scottie sad
            scottie.say "But...uh..."
            scottie.say "If we do have to get pizza..."
            scottie.say "We can have some too, right?"
            show bree angry
            "[bree.name] and Sasha roll their eyes and groan at this."
            bree.say "How can you STILL be hungry?"
            show sasha vangry
            sasha.say "Have you got a tapeworm or something?!?"
    scene bg black with dissolve
    pause 1
    return

label nodate_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom with fade
    "When I next get a chance to stop and take a breath, I realise something instantly."
    "It's been a couple of hours since the party got started."
    "And I haven't even had the chance to hit the dance-floor yet!"
    "Looking around the room, I search for someone to be my partner."
    "But which lucky lady should I ask to dance?"
    menu:
        "Dance with [bree.name]":
            show bree halloween with dissolve
            mike.say "Hey, [bree.name]..."
            mike.say "You want to dance with me?"
            show bree surprised blush
            "[bree.name] looks a little surprised at the question."
            "But not surprised in a bad way, you know?"
            "More like it's unexpected, but not unwelcome."
            $ bree.love += 2
            show bree happy -blush
            "Sure, [hero.name]."
            bree.say "That sounds like fun!"
            "[bree.name] giggles with delight as I lead her onto the dance-floor."
            hide bree
            show dance bree halloween
            with fade
            "And as soon as we start dancing, the music doesn't seem to matter."
            "All that does is the fact we're together and having a good time."
            "I'm cool with keeping things light and fun."
            "But I soon get the impression [bree.name] has other things in mind."
            "She dances as close to me as she can."
            "And she seems to be pressed close against me the whole time."
            "I'm not complaining about this, not at all."
            "In fact, I can already feel myself stiffening in a certain area!"
            "[bree.name] seems to notice this too."
            "She giggles again as she rubs my crotch with her hand."
            bree.say "Hey, [hero.name]!"
            bree.say "I'm the one that's supposed to be a mechanic."
            bree.say "So how come you're the one with the massive tool?"
            "Let out a nervous laugh, unable to do anything else."
            "And for the rest of the dance I can feel my cock getting ever harder!"
            "I had no idea [bree.name] could be this flirty!"
        "Dance with Sasha":
            show sasha annoyed halloween with dissolve
            mike.say "Hey, Sasha..."
            mike.say "How's it going?"
            show sasha sad
            "Sasha looks at me with a pained smile."
            "And then she shakes her head."
            show sasha annoyed
            sasha.say "Scottie's been hitting on me most of the night."
            sasha.say "And I'm SO not in the mood for his bullshit right now."
            "She glances over to where Scottie's standing."
            show sasha sad at center, zoomAt(1.5, (640, 1040))
            "And then takes me by surprise by scooting closer to me."
            "Sasha leans in, almost pressing herself against my side."
            sasha.say "Sorry about this, [hero.name]."
            sasha.say "I just needed him to see us up close like that."
            show sasha normal
            sasha.say "He's got the message!"
            "I nod, trying to look nonchalant and like I understand."
            "But it's pretty nice to have Sasha this close to me."
            "Maybe there's a way I can prolong the experience?"
            mike.say "No worries, Sasha."
            mike.say "Anything to help out a friend."
            mike.say "How about you pay me back with a dance?"
            show sasha happy
            "Sasha gives me a smile and a nod."
            hide sasha
            show dance sasha halloween
            with fade
            "And as soon as a song she likes comes on, we hit the dance-floor."
            "Sasha shows none of the reluctance to me that she had for Scottie."
            "The action is pretty much hot and heavy right from the start!"
            "She moves in time to the music, never more than an inch from me."
            "And I move in time with Sasha, all of my attention focused on her."
        "Dance with Minami" if Harem.together(bree, sasha, minami, name='home'):
            show minami halloween with dissolve
            mike.say "Ah..."
            mike.say "Hey, Minami - you want to dance?"
            show minami happy
            "Minami's face lights up the moment I ask."
            minami.say "Sure thing, big bro."
            minami.say "Let's hit the dance-floor!"
            hide minami
            show dance minami halloween
            with fade
            "I allow myself to be pulled along by Minami."
            "At first she bounces around like a Jack-in-the-Box."
            "But then she wraps her arms around me and clings on."
            "And all of that energy goes into holding onto me."
            "It's not like one of those slow dances in the movies."
            "In fact, she reminds me a little of an excitable puppy."
            "But all of that intensity is directed at dancing with me."
            "And when I put my hands on her ass, Minami smiles up at me."
            minami.say "See, big bro?"
            minami.say "I told you it'd be fun!"
            "Minami puts her arms around my neck."
            "And then she pulls me down, close enough to kiss me."
            "For a moment, it almost feels like she does just that."
            "But in truth she's just staring up at me."
            "I can almost feel her infectious energy passing into me."
            "The song must have ended some time ago, fading into the next."
            "But I don't even notice the change."
            "Minami's the only thing on my mind the whole time."
        "Dance with Samantha" if Harem.together(bree, sasha, samantha, name='home'):
            show samantha halloween with dissolve
            if samantha.flags.nickname == "cupcake":
                mike.say "Ah, Cupcake..."
            else:
                mike.say "Ah, Sam..."
            mike.say "Would you like to dance?"
            show samantha surprised
            samantha.say "What...oh..."
            show samantha normal
            samantha.say "Sorry, [hero.name]."
            samantha.say "I was miles away."
            show samantha sad
            samantha.say "Just remembering when I lived here with Ryan."
            "Almost as soon as she mentions Ryan's name, Sam shudders."
            "It's like she's trying to shake off the memories of her past."
            show samantha normal
            samantha.say "But screw that guy, right?"
            show samantha happy
            samantha.say "You're right - we should go dance!"
            hide samantha
            show dance samantha halloween
            with fade
            "Sam lets me lead her onto the dance-floor."
            "The song that starts playing is a slow one."
            "And so we end up dancing equally slowly."
            "Slowly and very close together."
            "Neither of us speaks the whole time."
            "Which is a relief to me."
            "As it means I can just enjoy being close to Sam."
            "She looks amazing in her costume, more beautiful than ever."
            "I can't understand how Ryan let her slip away from him."
            "And I promise myself in that moment I won't ever make a mistake like that."
            "Whatever happens between Sam and I, she'll always be a part of my life."
        "Dance with Lexi" if Person.is_not_hidden("lexi") and Harem.together(bree, sasha, lexi, name='home'):
            show lexi halloween with dissolve
            mike.say "Lexi..."
            mike.say "You want to dance with me?"
            show lexi happy
            "Lexi's face lights up at the question."
            lexi.say "Yeah, I sure do!"
            lexi.say "I thought you were never going to ask!"
            "But she doesn't have time to reply."
            "I open my mouth to reply."
            "But my words become a yelp as Lexi grabs my wrist."
            hide lexi
            show dance lexi halloween
            with fade
            "And without hesitation, she pulls me onto the dance-floor."
            lexi.say "Oh yeah."
            lexi.say "Now that's what I'm talking about!"
            "Of course, this isn't going to be a slow-dance."
            "And Lexi makes that apparent right from the start."
            "I don't think there's even a moment she's not rubbing against me!"
            "Lexi gyrates and grinds the whole time, never letting up."
            "It's all that I can do to keep from blushing."
            "But that doesn't mean I want her to stop."
            "I can almost feel the eyes of the other guests on us."
            "As Lexi dances like a stripper in a gentleman's club."
            "By the time the song ends, I'm panting and exhausted."
            "My cock as hard as a rock in my pants."
            "Lexi's going to be all I can dream about tonight!"
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
