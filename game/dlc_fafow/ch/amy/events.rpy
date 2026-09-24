init python:
    Event(**{
    "name": "amy_start",
    "label": "amy_start",
    "priority": 1000,
    "conditions": [
        
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_kissable",
    "label": "amy_kissable",
    "priority": 1500,
    "conditions": [
        IsDone("amy_teaser_kiss"),
        PersonTarget(amy,
            IsFlag("nokiss"),
            ),
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_dateable",
    "label": "amy_dateable",
    "priority": 1500,
    "conditions": [
        IsDone("amy_teaser_sex"),
        PersonTarget(amy,
            IsFlag("nodate"),
            ),
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_fuckable",
    "label": "amy_fuckable",
    "priority": 1500,
    "conditions": [
        IsDone("amy_teaser_sex"),
        PersonTarget(amy,
            IsFlag("nosex"),
            ),
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_event_01",
    "label": "amy_event_01",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_teaser"),
        PersonTarget("amy",
                    MinStat("love", 20),
                    IsRoom("electronic"),
                    IsFlag("amydelay", False)),
        HeroTarget(
            
            Not(OnDate()),
            IsRoom("electronic")),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "amy_event_03",
    "label": "amy_event_03",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_teaser_kiss"),
        PersonTarget("amy",
                    MinStat("love", 60),
                    IsRoom("electronic"),
                    IsFlag("amydelay", False)),
        HeroTarget(
            
            Not(OnDate()),
            IsRoom("electronic")),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "amy_event_04",
    "label": "amy_event_04",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_event_03"),
        Or(And(IsDayOfWeek("6"), IsHour(9, 13)),
        And(IsDayOfWeek("7"), IsHour(16, 17))),
        PersonTarget("amy",
                    MinStat("love", 80),
                    IsFlag("amydelay", False)),
        HeroTarget(
            
            Not(OnDate()),
            IsRoom("beach")),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "amy_event_06",
    "label": "amy_event_06",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_teaser_sex"),
        PersonTarget("amy",
                     MinStat("love", 120),
                     OnDate()),
        HeroTarget(
            
            OnDate(),
            IsRoom("date_cinema")),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "amy_event_07",
    "label": "amy_event_07",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(15, 23),
        IsDone("amy_event_06"),
        PersonTarget("amy",
                    MinStat("love", 140),
                    Not(IsPresent()),
                    IsFlag("amydelay", False),
                    ),
        HeroTarget(
            
            Not(OnDate()),
            ),
        ],
    "do_once": True,
    "once_day": True,
    })

    Event(**{
    "name": "amy_event_08",
    "label": "amy_event_08",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(8, 15),
        IsDone("amy_event_07"),
        PersonTarget("amy",
                    MinStat("love", 160),
                    Not(IsPresent()),
                    IsFlag("amydelay", False),
                    ),
        HeroTarget(Not(OnDate())),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_event_09",
    "label": "amy_event_09",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(8, 23),
        IsDone("amy_event_08"),
        PersonTarget("amy",
                    IsHidden(),
                    IsFlag("amydelay", False),
                    ),
        HeroTarget(Not(OnDate())),
        ],
    "do_once": True,
    "once_day": True,
    })

    Event(**{
    "name": "amy_event_10",
    "label": "amy_event_10",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(20, 2),
        IsDone("amy_event_09"),
        PersonTarget("amy",
                    MinStat("love", 180),
                    Not(IsHidden()),
                    Not(IsPresent()),
                    IsFlag("amydelay", False),
                    ),
        HeroTarget(Not(OnDate())),
        ],
    "do_once": True,
    "once_day": True,
    })

    Event(**{
    "name": "amy_kink_01",
    "label": "amy_kink_01",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_teaser_sex"),
        PersonTarget("amy",
                     MinStat("sub", 10),
                     OnDate(),
                     ),
        HeroTarget(
            
            IsRoom("date_restaurant"),
            OnDate(),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_kink_02",
    "label": "amy_kink_02",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_kink_01"),
        PersonTarget("amy",
                     Not(IsDatePlanned()),
                     IsActive(),
                     MinStat("sub", 20),
                     MinStat("love", 100),
                     IsFlag("amydelay", False),
                     ),
        HeroTarget(
            
            IsActivity("ask_date"),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "amy_kink_03",
    "label": "amy_kink_03",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_kink_02_date"),
        PersonTarget("amy",
                     IsActive(),
                     MinStat("sub", 40),
                     MinStat("love", 120),
                     IsFlag("amydelay", False),
                     ),
        HeroTarget(
            
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_kink_03_police",
    "label": "amy_kink_03_police",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_kink_03"),
        PersonTarget("amy",
                     IsFlag("police_ticket", True),
                     ),
        HeroTarget(
            
            IsRoom("policestation"),
            ),
        ],
    "do_once": True,
    })

    BeforeDateEvent(**{
    "name": "amy_kink_04",
    "label": "amy_kink_04",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_kink_03_police"),
        PersonTarget("amy",
                     MinStat("sub", 60),
                     MinStat("love", 130),
                     IsFlag("amydelay", False),
                     OnDate(),
                     ),
        HeroTarget(
            
            OnDate(),
            Not(HasRoomTag("home")),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    InteractEvent(**{
    "name": "amy_kink_05",
    "label": "amy_kink_05",
    "priority": 400,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_kink_04"),
        PersonTarget("amy",
                    IsActive(),
                    MinStat("sub", 80),
                    MinStat("love", 150),
                    ),
        HeroTarget(
            
            ),
        ],
    "do_once": True,
    })


label amy_start:
    $ amy.unhide()
    return

label amy_kissable:
    $ amy.flags.nokiss = False
    return

label amy_dateable:
    $ amy.flags.nodate = False
    return

label amy_fuckable:
    $ amy.flags.nosex = False
    return

label amy_event_01:
    if 'amy_teaser_kiss' in DONE and amy.love.max < 60:
        $ amy.love.max = 60
    elif amy.love.max < 40:
        $ amy.love.max = 40
    scene bg electronic
    "I find myself wandering down to the electronics store where Shawn works."
    "That's nothing out of the ordinary, as I often pop in to chat to him."
    "Or else just to browse the aisles and look at all the shit I can't afford."
    "Of course it has nothing to do with the chance that Amy might be working today."
    "I mean, if she happens to be there I'll probably chat to her for a while."
    "But that's not why I'm here."
    "Definitely not!"
    "I'm thinking that as I walk into the store, but then I get distracted."
    "What I thought was the music playing on the PA suddenly makes my ears prick up."
    "It's actually someone playing an electric guitar in the store."
    "And what's more, it sounds amazing!"
    "Hurrying inside, I head for the aisle where the instruments are kept."
    "And that's when I see her."
    scene bg electronic at center, zoomAt(2.5, (640, 1340)), dark, blur(2)
    show amy shy at center, zoomAt(2.5, (440, 1600))
    show concert_solo_instrument_mike at center, zoomAt(2.5, (550, 3000)), rotation(5.5)
    with dissolve
    "Amy's standing there, a guitar in her hands, fingers moving over the strings."
    "It's her, she's the one playing it!"
    "Or to be more accurate, she's the one standing there like a guitar-playing goddess!"
    "I hardly notice the customers standing beside Amy as she plays."
    "Because she's all I can see right now."
    "Amy doesn't seem to notice me either, totally lost in the music."
    "She only comes back to reality once she's done playing."
    "And when it's over, I feel like I've been woken abruptly from a dream."
    show amy happy
    "Amy acknowledges me with a smile as she puts the guitar back on it's stand."
    scene bg electronic
    show amy
    with fade
    "But of course she's sure to finish dealing with her customers before coming over."
    show amy happy
    amy.say "There you go."
    amy.say "I hope that was useful?"
    amy.say "If you need any more help, you know where to find me, okay?"
    show amy at center, zoomAt(1.5, (640, 1040))
    "As soon as the customers have wandered off, Amy hurries over to me."
    show amy normal
    amy.say "Sorry about that, [hero.name]."
    amy.say "I was just showing that guitar off to a customer."
    menu:
        "Tell her you play guitar too":
            mike.say "You weren't just showing it off, Amy."
            mike.say "You were totally killing it!"
            show amy surprised
            "Amy looks surprised at the way I'm gushing over her playing."
            show amy blush
            "And she even seems to be blushing a little."
            "Well, it would be a little if she wasn't a goth!"
            mike.say "And I should know..."
            mike.say "Because I play guitar too!"
            show amy surprised -blush
            "Amy's mouth literally drops open as I tell her this."
            "And she shakes her head in amazement."
            amy.say "Really?!?"
            show amy happy at startle
            $ amy.love += 2
            amy.say "That is SO cool!"
            amy.say "I love finding out I have stuff in common with cool people!"
            "Whoa...wait...what?!?"
            "Did Amy just call me a cool person?"
            "Suddenly I'm the one that's blushing!"
            mike.say "Seriously though, Amy..."
            mike.say "That was majorly impressive!"
            mike.say "With skills like that, you must be in a band, right?"
            show amy shy
            "As soon as I bring the matter up, Amy's expression changes."
            "She seems to almost wince, like it's a painful subject."
            show amy annoyed
            amy.say "Urgh..."
            amy.say "I almost was!"
            mike.say "Oh..."
            mike.say "What happened, Amy?"
            mike.say "I mean...you don't have to say if it's a touchy subject."
            show amy sad
            "Amy shakes her head."
            show amy normal
            "But I note that her smile begins to return too."
            amy.say "Nah, it's not that big of a thing, [hero.name]."
            amy.say "I tried out for them and they wanted me to join."
            amy.say "But there were two of them that I just didn't gel with."
            show amy shy
            amy.say "And I don't need that kind of drama in my life!"
            menu:
                "Tell her you're in a band":
                    "For a moment I think about letting the matter drop."
                    "But then I change my mind and decide to tell Amy about my being in a band."
                    "After all, she seems pretty cool about her own bad experience."
                    "So it really shouldn't be a taboo subject."
                    mike.say "Ah, that really sucks, Amy!"
                    mike.say "I mean, I'm in a band right now."
                    mike.say "And it can get pretty heated at times."
                    mike.say "Because you know how creative types are!"
                    mike.say "But there's no drama on that level."
                    show amy normal
                    "Amy's interest seems to kick up a whole couple of levels as she hears this."
                    "And I can see that she's really interested in hearing more."
                    amy.say "I know I already said you playing guitar too was cool."
                    show amy happy
                    $ amy.love += 2
                    amy.say "But that's super cool as well!"
                    amy.say "You have to tell me when you're playing a gig."
                    amy.say "Because I'd love to come and see you!"
                    "It's all that I can do to keep from beaming with delight at this."
                    "But I try pretty hard to sound nonchalant about it."
                    mike.say "Sure thing, Amy."
                    mike.say "I'll find out when our next date is."
                    mike.say "And then I can put you on the guest-list."
                    show amy normal with fade
                    "We keep on chatting about guitars and music in general."
                    "At least we do until Amy gets called away again."
                    "And that leaves me feeling like we've really connected."
                    "Like we're bonding on a whole new level."
                    "And I can't wait to talk to her again."
                "Keep the fact that your in a band for yourself":
                    "Thank god Amy told me all that when she did."
                    "I was just about to tell her all about being in one myself!"
                    show amy normal with fade
                    "We keep on chatting about guitars and music in general."
                    "At least we do until Amy gets called away again."
                    "And that leaves me feeling like we've really connected."
                    "Like we're bonding on a whole new level."
            $ amy.flags.told_about_band = True
        "Tell her she's an awesome guitar player":
            mike.say "You weren't just showing it off, Amy."
            mike.say "You were totally killing it!"
            show amy surprised blush at startle
            $ amy.love += 1
            "Amy looks surprised at the way I'm gushing over her playing."
            "And she even seems to be blushing a little."
            "Well, it would be a little if she wasn't a goth!"
            show amy normal -blush with fade
            "We keep on chatting about guitars and music in general."
            "At least we do until Amy gets called away again."
            "And that leaves me feeling like we've really connected."
            "Like we're bonding on a whole new level."
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return

label amy_event_03:
    if amy.love.max < 80:
        $ amy.love.max = 80
    scene bg electronic
    "My mind's not totally focused on what's in front of me as I stroll into the electrical store."
    "I'm so used to coming in here that I could probably walk around with my eyes closed and not collide with anything."
    "And the simple fact is that my thoughts are almost totally devoted to Amy right now."
    "Or to be more specific, what we did the last time I was in the store with her!"
    "That's why I'm here, on the flimsiest excuse to be in the store, all for the hope of seeing her."
    "But it doesn't take long for my belief I can wander around with my head in the clouds to be proven wrong."
    "Because a moment later I walk straight into something."
    "Admittedly it's not something solid, and it moves backwards with an all too human grunt."
    show shawn angry at center, zoomAt (1.5, (640, 1040)), dark, dark with hpunch
    shawn.say "Urgh!"
    mike.say "What the..."
    hide shawn
    show shawn angry at center, zoomAt (1.25, (640, 840)), dark
    "I take a step backwards too, trying to regain my senses."
    hide shawn
    show shawn annoyed
    "Then I see what, or to be more specific, who I just collided with."
    mike.say "Oh..."
    mike.say "Hey, Shawn..."
    mike.say "I didn't see you there!"
    "I'm saying all of this in a friendly, easy-going manner."
    "The way that I'd normally greet any of my friends."
    "But all this gets me from Shawn is a frown."
    "And then he crosses his arms over his chest."
    "As if he really needs to make it obvious that he's not happy."
    show shawn angry
    shawn.say "Yeah, I doubt it was me you were looking for, [hero.name]."
    shawn.say "And I bet you weren't looking for something to buy either!"
    show shawn annoyed
    "Now I'm frowning too."
    "Shawn seems to be massively pissed at me for some unknown reason."
    "And he's never been annoyed at me just coming in here to hang-out before now."
    mike.say "What's the matter, Shawn?"
    mike.say "What's with the attitude?"
    show shawn angry
    shawn.say "Ha!"
    shawn.say "Like you don't know what you did!"
    show shawn annoyed
    mike.say "Erm..."
    mike.say "I don't, Shawn."
    mike.say "I really don't!"
    "Shawn points towards the ceiling."
    show shawn angry
    shawn.say "We do have CCTV in here, [hero.name]."
    shawn.say "And it records everything that happens in the store!"
    show shawn annoyed
    "Okay..."
    "Now I get what he means."
    "Shawn must have seen what Amy and I got up to the last time I was here!"
    mike.say "Okay, Shawn..."
    mike.say "Just calm down, yeah?"
    show shawn angry
    shawn.say "Don't tell me to calm down!"
    shawn.say "I'm the big dog in this electronics store."
    shawn.say "And you're barred until further notice!"
    show shawn annoyed
    "It takes a few seconds for what Shawn just said to jump in."
    "And then I realise that he sounds totally serious!"
    show amy at mostright5 with moveinright
    "What's more, the sound of our voices must be carrying."
    "Because I can see Amy looking in our direction too!"
    menu:
        "Confront Shawn":
            "I could walk away, try to make myself look like the bigger man here."
            "But it's really pissing me off that Shawn's being such an ass."
            "I mean, is he really that jealous and petty because Amy likes me and not him?"
            mike.say "Come on, Shawn..."
            mike.say "We both know that this isn't about what Amy and I did."
            mike.say "It's about you being a bitter little bitch!"
            "Shawn's eyes go wide at the insult."
            "And he starts to puff and blow."
            "Like he's going to explode any second."
            "But luckily for me, that's exactly when Amy chooses to wade in."
            show amy angry at right
            show shawn at left5
            with ease
            amy.say "Shawn!"
            amy.say "What are you talking to [hero.name] about?"
            shawn.say "There's no need for you to get involved, Amy."
            shawn.say "This is between me and him."
            amy.say "Bollocks it is, Shawn!"
            show amy at center
            show shawn at left
            with hpunch
            "Amy pushes past Shawn to come stand by me."
            show amy sad
            amy.say "Hey, [hero.name]..."
            amy.say "What's going on here?"
            mike.say "Hey, Amy..."
            mike.say "Apparently I'm barred from the store!"
            show amy surprised
            "As soon as Amy hears this she goes ballistic, turning on Shawn."
            show amy angry at left4, hshake
            amy.say "You mean you actually did it?!?"
            show amy upset
            "Shawn can't help jumping back and flinching as Amy lays into him."
            show shawn angry at left, startle
            shawn.say "Argh!"
            show shawn angry
            shawn.say "Y...yeah, I did it..."
            shawn.say "Didn't I say I was going to ban him from the store?!?"
            show shawn annoyed
            show amy angry
            amy.say "Sure you did."
            amy.say "But I never thought you'd do it!"
            amy.say "I didn't think even you were that big of a prick!"
            menu:
                "Join the fight":
                    show amy upset
                    "Amy looks like she's got Shawn on the run already."
                    "But I want her to know that I've got her back too."
                    mike.say "She's right, Shawn."
                    mike.say "You're being a massive arse!"
                    show shawn angry
                    shawn.say "Hey!"
                    shawn.say "You can't talk to me like that!"
                    shawn.say "I'm the manager of this store!"
                    show shawn annoyed
                    show amy angry
                    amy.say "So what, Shawn?"
                    amy.say "That doesn't make you the king of the world!"
                    amy.say "You can't just ban him because I like him more than you!"
                    show amy upset
                    mike.say "It's kind of like he's abusing his power, isn't it?"
                    "Shawn splutters and shakes his head."
                    show shawn angry
                    shawn.say "That's not..."
                    shawn.say "I didn't ban him because of that!"
                    shawn.say "I banned him because of what you two did in the store!"
                    show shawn annoyed
                    mike.say "So you admit that you spy on employees?"
                    mike.say "That you watch them on the CCTV?"
                    show amy flirt
                    amy.say "Oh, he's not the only one that watches it."
                    "Amy raises an eyebrow as she says this."
                    "And at the same time, Shawn's eyes go wide."
                    show shawn sad
                    shawn.say "Wh...what do you mean?"
                    show amy normal
                    amy.say "Oh, just that I reviewed the footage myself."
                    amy.say "Specifically of you interacting with female customers!"
                    amy.say "And I took a copy too - which I'm going to email to head office!"
                    mike.say "Whoops!"
                    mike.say "Have you been acting in an inappropriate manner, Shawn?"
                    mike.say "One likely to bring the store into disrepute?"
                    shawn.say "There's no need for that!"
                    "Amy doesn't respond straight away."
                    "Instead she nods her head in my direction."
                    shawn.say "You...you want me to un-ban him?"
                    "Amy nods."
                    shawn.say "Okay, he's unbanned."
                    shawn.say "And we're cool now, yeah?"
                    "Amy shakes her head."
                    shawn.say "What more do you want from me?!?"
                    "Amy looks thoughtful."
                    "Then she takes hold of my hand."
                    "And she leans her head on my shoulder."
                    show shawn angry
                    shawn.say "Okay, okay..."
                    shawn.say "I'll back off, leave you two alone from now on!"
                    show amy happy
                    "Amy smiles and makes a shooing motion towards Shawn."
                    hide shawn with moveoutleft
                    "He nods and does as he's told, scuttling away to the back of the store."
                    mike.say "That was some pretty sweet teamwork on our part, Amy!"
                    show amy at center with ease
                    amy.say "Yeah..."
                    show amy flirt
                    amy.say "Maybe he'll keep his nose out of our business from now on."
                    $ amy.love += 4
                    $ amy.sub += 4
                "Let Amy berate Shawn":
                    "I could jump in here and back Amy up."
                    "But honestly she doesn't seem to need it."
                    "So I just stand back and watch the fun."
                    show shawn angry
                    shawn.say "Hey!"
                    shawn.say "You can't talk to me like that!"
                    shawn.say "I'm the manager of this store!"
                    show shawn annoyed
                    amy.say "So what, Shawn?"
                    amy.say "That doesn't make you the king of the world!"
                    amy.say "You can't just ban a guy because I like him more than you!"
                    "Shawn splutters and shakes his head."
                    show shawn angry
                    shawn.say "That's not..."
                    shawn.say "I didn't ban him because of that!"
                    show shawn annoyed
                    amy.say "Of course you did, Shawn."
                    show amy flirt
                    amy.say "But you're not the only one that watches the CCTV around here."
                    "Amy raises an eyebrow as she says this."
                    "And at the same time, Shawn's eyes go wide."
                    show shawn sad
                    shawn.say "Wh...what do you mean?"
                    show amy normal
                    amy.say "Oh, just that I reviewed the footage myself."
                    amy.say "Specifically of you interacting with female customers!"
                    amy.say "And I took a copy too - which I'm going to email to head office!"
                    show shawn normal
                    shawn.say "Come on now, Amy..."
                    shawn.say "There's no need for that!"
                    "Amy doesn't respond straight away."
                    "Instead she nods her head in my direction."
                    shawn.say "You...you want me to un-ban him?"
                    "Amy nods."
                    show shawn sad
                    shawn.say "Okay, he's unbanned."
                    shawn.say "And we're cool now, yeah?"
                    "Amy shakes her head."
                    shawn.say "What more do you want from me?!?"
                    "Amy looks thoughtful."
                    "Then she takes hold of my hand."
                    "And she leans her head on my shoulder."
                    show shawn angry
                    shawn.say "Okay, okay..."
                    shawn.say "I'll back off, leave you two alone from now on!"
                    show shawn annoyed
                    "Amy smiles and makes a shooing motion towards Shawn."
                    hide shawn with moveoutleft
                    "He nods and does as he's told, scuttling away to the back of the store."
                    mike.say "Wow, Amy..."
                    mike.say "That was amazing!"
                    show amy at center with ease
                    amy.say "Well...he's had it coming for a while."
                    show amy flirt
                    amy.say "Maybe now he'll keep his nose out of our business."
                    $ amy.love += 4
                    $ amy.sub -= 4
        "Fuck all of this":
            "Part of me wants to stay right where I am and challenge Shawn."
            "That way I could at least get to say a few words to Amy."
            "Maybe even make myself look like I won't take any crap."
            "But then it occurs to me that discretion might be the better choice here."
            "Shawn's the one that's making a scene and being a petty asshole."
            "So maybe walking away will make me look like the better man here?"
            mike.say "Okay, Shawn..."
            mike.say "If that's what you want, I'll leave."
            show shawn angry
            shawn.say "Yeah you better leave!"
            shawn.say "In fact you're ban from here now! That'll teach you!"
            mike.say "Sure, whatever man."
            mike.say "Call me when you calm down a little, yeah?"
            "I'm sure to make eye-contact with Amy as I turn to walk away."
            scene bg mall1 with fade
            "And I'm almost out of ear-shot when she reaches Shawn."
            "But I get the pleasure of hearing her start to tear into him before I turn the corner."
            $ game.room = "mall1"
            $ Room.find("electronic").hide()
            $ hero.flags.electronic_ban = TemporaryFlag(True, 15, hook=Room.find("electronic").unhide)
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return

label failed_amy_event_04:
    $ DONE.pop("amy_event_04", None)
    return

label amy_event_04:
    scene bg beach
    "It's a great day to be at the beach without a care in the world."
    "The sun is high in the clear, blue sky and the place is buzzing."
    "Which also means that it's full of girls in their bathing suits too!"
    "And I have nothing better to do than stroll along and admire them."
    "Before you say it, that doesn't make me a perv."
    "The appropriate term would be a connoisseur of the female form!"
    "And one specimen in particular is catching my eye right now."
    "I can only see the girl in question from behind."
    "But she's still blowing me away all the same."
    "Well...mainly because of her butt!"
    "She's got an amazingly full and beautiful figure."
    "Maybe she's a little paler than average."
    "Yet that goes really well with her black swimsuit and equally dark hair."
    "And as she moves, I notice there are blue streaks in there as well."
    "Wait a minute...that sounds kind of familiar!"
    "A moment later, the girl in question turns around."
    "And I recognise her as soon as she does."
    show amy swimsuit shy at flip, left with dissolve
    "That's Amy, the goth girl who works at the electronics store with Shawn!"
    "She doesn't seem to see me."
    "Which means that I can keep on watching her without being discovered."
    "But on the other hand, she's only a little way off from where I'm standing."
    "I could easily walk over there and say hi."
    menu:
        "Go see her":
            if 'amy_teaser_sex' in DONE and amy.love.max < 120:
                $ amy.love.max = 120
            if amy.love.max < 100:
                $ amy.love.max = 100
            "And that's just what I do."
            "Because I'm not a peeping Tom!"
            mike.say "Hey there, Amy!"
            hide amy
            show amy swimsuit surprised at center, zoomAt(1.5, (640, 1040))
            with fade
            "At the sound of me calling her name, Amy looks in my direction."
            show amy happy
            "And when she sees that it's me, her face lights up."
            "Which is almost as much of a thrill as seeing her in a swimsuit for the first time."
            "Almost, but not quite!"
            amy.say "[hero.name]!"
            show amy normal
            show fx question
            amy.say "What are you doing here?!?"
            "As soon as she asks the question."
            "Amy chuckles and shakes her head."
            hide fx
            amy.say "Sorry, dumb question..."
            show amy happy
            amy.say "Why wouldn't you be at the beach on a day like this!"
            "I wave away her apology with a smile of my own."
            mike.say "I was about to ask you the same thing, Amy!"
            "I wasn't, but it doesn't hurt to empathise with her."
            mike.say "Did Shawn finally let you escape the store?"
            mike.say "Because I hear he can be a real slave-driver!"
            show amy normal
            amy.say "It's my day off."
            show amy flirt
            amy.say "So no manacles and whips for me today!"
            "I do the best I can to ignore the image that springs into my mind."
            "The combination of Amy, being tied up and physical punishment..."
            "Well, it almost makes me physically shudder with excitement!"
            mike.say "So..."
            mike.say "Are you here with anyone?"
            show amy normal
            "Amy shakes her head."
            amy.say "No, I'm not."
            amy.say "I came here on my own."
            amy.say "Pretty sad, huh?"
            "I shrug as I try to ask my next question in a nonchalant manner."
            "When in reality I'm hoping like crazy that I'll get the answer I want."
            mike.say "What a coincidence, Amy!"
            mike.say "I'm here on my own too."
            mike.say "I don't suppose you want to...maybe...hang-out together?"
            show amy happy
            amy.say "Oh yeah!"
            show amy shy blush
            amy.say "I...I mean...sure, [hero.name]."
            amy.say "Because, it makes sense, right?"
            "I don't know which thrills me more in that moment."
            "The simple fact that Amy said yes without hesitation."
            "Or that she was so enthusiastic she felt the need to try and hide it!"
            show amy normal -blush
            "Amy and I stand on the sand for a while after that."
            "Just chatting and talking about whatever comes to mind."
            "But eventually we start to walk down the beach together."
            "And as we do so, my eye is naturally drawn towards the sights on show."
            show amy flirt
            amy.say "You really have an eye for the ladies..."
            amy.say "Don't you, [hero.name]?"
            "My head spins around to look at Amy."
            "Because I had no idea I was being so obvious!"
            menu:
                "Admit you laid your eyes on some ladies":
                    "I've been caught in the act."
                    "So I guess all I can do is apologise."
                    mike.say "I'm sorry, Amy..."
                    mike.say "I know that I shouldn't be looking at other women."
                    mike.say "But I guess I'm just a typical guy!"
                    "Amy surprises me by laughing and shaking her head."
                    show amy happy
                    amy.say "Don't worry about it, [hero.name]."
                    amy.say "I wasn't trying to make you feel bad!"
                    mike.say "Y...you weren't?"
                    amy.say "No, dumbass!"
                    show amy flirt
                    amy.say "Not when I was looking at them too!"
                    "I stare at Amy for a moment, not sure what she means."
                    "But then it hits me, and I can't believe I took so long to get it."
                    mike.say "Oh..."
                    mike.say "You mean that..."
                    show amy normal
                    amy.say "Yeah - I like guys AND girls!"
                    "Suddenly Amy begins to look worried."
                    show amy worried
                    amy.say "That's not a problem for you - is it?"
                    menu:
                        "It is not a problem":
                            mike.say "Of course not, Amy."
                            mike.say "In fact..."
                            mike.say "I think it's kind of hot!"
                            $ amy.love += 4
                            show amy normal
                            "Amy looks delighted with my answer."
                            "And she leans in closer, like she doesn't want anyone else to hear."
                            show amy flirt at center, zoomAt(2.0, (640, 1340))
                            amy.say "Can I..."
                            amy.say "Can I guess which girls you think are hot?"
                            amy.say "Just to see if I get it right?"
                            "I nod in agreement."
                            "And Amy claps her hands together with glee."
                            show amy normal at center, zoomAt(1.5, (640, 1040))
                            amy.say "Okay, okay, okay..."
                            show amy shy
                            amy.say "Now let me see..."
                            amy.say "What about her?"
                            "Amy points to a petite Asian girl with a black bob."
                            amy.say "You like her, right?"
                            mike.say "I sure do, Amy."
                            mike.say "In my experience, good things come in small packages!"
                            show amy happy
                            "Amy nods, clearly happy to have gotten off to a good start."
                            amy.say "Ooh..."
                            show amy shy
                            amy.say "But then look at her!"
                            "I follow Amy's gaze to see a girl with ebony skin and dyed hair."
                            mike.say "Elegant yet with a hint of quirk..."
                            mike.say "I bet she's hiding some fun ideas in that pretty head!"
                            show amy happy
                            amy.say "And wouldn't I love to find out what they are!"
                            amy.say "Okay..."
                            amy.say "Let's make it best of three!"
                            show amy shy
                            "She pauses as her eyes scan the beach."
                            "And then she settles on her final choice."
                            amy.say "How about her?"
                            "At first I'm a little thrown by Amy's choice."
                            "This time the girl is a tall, very traditional-looking blonde."
                            "I'm sure that Amy's trying to throw me off with this one."
                            "But then I take a closer look, and I see something that changes my mind."
                            show amy surprised
                            mike.say "You think I don't see those tattoos she has, Amy?"
                            mike.say "And the piercings too?"
                            mike.say "Sorry, but I don't judge a book by it's cover."
                            mike.say "I like to look a little deeper!"
                            amy.say "Wow..."
                            show amy normal
                            amy.say "Me too!"
                            amy.say "Looks like we have a lot in common, [hero.name]!"
                            "I can't help nodding and smiling at this."
                            "Because Amy's right, we really do!"
                            "We spend the rest of our time on the beach chatting about this and that."
                            "But when it's time to leave, I find myself a little gloomy at the thought of us parting."
                            "I guess that really does mean that we're starting to become friends."
                        "This is private stuff":
                            mike.say "It's not a problem for me, Amy."
                            mike.say "But maybe I don't need to know if you like a girl or not."
                            $ amy.love -= 2
                            "Amy nods at this."
                            "But I can tell it's not the answer she wanted."
                            amy.say "I guess I can understand that, [hero.name]."
                            amy.say "Kinda like it not being cool for me to go on about other guys, right?"
                            mike.say "I think so, Amy..."
                            "Now there's no hiding the fact that things are getting awkward."
                            "But all I can do is play along as I cringe inside."
                            show amy normal
                            "Luckily for me, Amy soon changes the subject."
                            "And we spend the rest of our time chatting about nothing in particular."
                            "So that by the time I say goodbye and make for home, it's almost forgotten."
                "Tell that you do not {b}see{/b} what she's talking about":
                    "Suddenly embarrassed, I begin to deny it."
                    mike.say "No, Amy..."
                    mike.say "I was just..."
                    mike.say "Erm...looking at the landscape, you know?"
                    $ amy.love += 2
                    show amy normal
                    "Amy chuckles and shakes her head."
                    "I honestly don't think that she believes me."
                    "But I'm grateful that she doesn't challenge me on it."
                    amy.say "Yeah, [hero.name]..."
                    amy.say "The landscape is very beautiful around here."
                    show amy flirt
                    amy.say "Very curvy and buxom."
                    amy.say "Almost feminine - don't you think?"
                    "Now there's no hiding the fact that Amy's teasing me."
                    "But all I can do is play along as I cringe inside."
                    show amy normal
                    "Luckily for me, Amy soon changes the subject."
                    "And we spend the rest of our time chatting about nothing in particular."
                    "So that by the time I say goodbye and make for home, it's almost forgotten."
            $ amy.flags.amydelay = TemporaryFlag(True, 1)
        "No need to go see her":
            "This is the first time that I've ever been able to see Amy in a swimsuit."
            "Whenever I've met her before now, she's always been fully clothed."
            "So this would be a golden opportunity to feast my eyes on the sight."
            "I keep telling myself that I'll go over and say hi if Amy sees me."
            "That I'm not just standing here perving on her."
            "But the more I watch her, the more I can feel my pulse begin to race."
            "And that's because I never realised how desirable her body was before now."
            "Sure, Amy's cute and she has a great personality."
            "All things that attracted me to her when we first met."
            "But the sight of her in a swimsuit seems to bring it all together."
            "And it's not long before I feel a straining at the waistband of my shorts!"
            "Suddenly I'm all to aware of the effect Amy's having on me."
            hide amy with dissolve
            "It's all I can do to tear my eyes away from her and look in another direction."
            "As soon as I can walk in a straight line again, I make my escape."
            "But the image of Amy in her swimsuit is still burned into my memory."
            "And I don't think anything's going to erase it either!"
            $ amy.flags.amydelay = TemporaryFlag(True, 1, hook="failed_amy_event_04")
    return

label amy_event_06:
    if amy.love.max < 140:
        $ amy.love.max = 140
    scene bg cinema
    show amy b at center, zoomAt(1.25, (640, 900))
    with fade
    "The lobby of the cinema is pretty busy as Amy and I try to make our way across it."
    "Looks like we chose the busiest time possible to try and catch a film."
    "But that doesn't mean we're going to just give up and miss out on some cinematic entertainment."
    scene bg cinema at center, zoomAt(1.75, (640, 720)), dark
    show amy b zorder 2 at center, zoomAt(1.5, (640, 1040))
    show samantha b as josie zorder 1 at center, zoomAt(1.5, (940, 1040)), blacker
    show dwayne as tyreese zorder 3 at center, zoomAt(1.5, (300, 1040)), blacker
    with fade
    "I'm trying to make some headway with Amy coming along just behind me."
    show amy annoyed b
    "And she's doing her part to widen the path I make with the liberal use of her elbows."
    "Normally this might have earned us some harsh stares or snarky comments."
    "But right now everyone in the place seems to be doing pretty much the same thing."
    mike.say "Amy..."
    mike.say "What was the screen number again?"
    show amy b at startle
    amy.say "Urgh..."
    amy.say "Number seven...I think!"
    mike.say "You think?"
    mike.say "Like, you're not sure?"
    show amy shy b
    amy.say "The tickets are in my pocket..."
    show amy worried b
    amy.say "I'm scared that if I reach for them..."
    amy.say "I might get trampled to death!"
    hide dwayne as tyreese at center, zoomAt(1.5, (300, 1040)), blacker with easeoutleft
    "Worried for her safety, I turn around to help Amy."
    show amy surprised b at center, zoomAt(1.5, (440, 1040))
    show samantha b as josie at startle, center, zoomAt(1.5, (840, 1040)), blacker
    with vpunch
    "And in doing so we both kind of half-collide with someone going the other way."
    show samantha a as josie at startle, center, zoomAt(1.5, (940, 1040)), blacker
    "Josie" "HEY!"
    "Josie" "Watch where you're going, you fucking oaf!"
    mike.say "Wha..."
    mike.say "What did I do?"
    show samantha b as josie at startle, center, zoomAt(1.5, (940, 1040)), blacker
    "Josie" "Don't give me that!"
    "Josie" "You almost knocked me down, you clumsy bastard!"
    show amy angry at startle
    amy.say "Don't talk to him like that!"
    amy.say "It was an accident you..."
    show amy surprised at startle
    amy.say "Josie?!?"
    show samantha a as josie at startle, center, zoomAt(1.5, (940, 1040)), blacker
    "Josie" "Amy?!?"
    mike.say "Huh?!?"
    "I see the girl we accidentally jostled staring at Amy."
    show amy annoyed
    "And I also see Amy returning the stare with equal intensity."
    amy.say "This is Josie..."
    amy.say "She and I used to date."
    "Josie" "A long time ago!"
    "Josie" "Before she started dating the lesser gender!"
    show amy angry at startle
    amy.say "HEY!"
    "I look at Amy in bafflement."
    "Not really understanding why she seems offended."
    amy.say "She's insulting you, [hero.name]!"
    mike.say "Why?"
    mike.say "What for?"
    show amy annoyed
    "Josie" "Wow, Amy..."
    "Josie" "You bagged yourself a smart one there!"
    "Josie" "At least I don't have to talk to any of my dildos when I'm done using them!"
    menu:
        "Reply":
            "I'm pretty mad that this girl is insulting Amy and me."
            "But I'm actually madder that I had to have it pointed out to me!"
            mike.say "Hey!"
            mike.say "What in the hell did I do to deserve that?!?"
            mike.say "I like never even met you before!"
            "The girl snorts and shakes her head."
            "Josie" "And here's to hoping you never will again!"
            "I'm about to say something in return."
            show amy angry
            "But then I feel Amy take hold of my arm."
            amy.say "Come on, [hero.name]..."
            show amy annoyed
            amy.say "She's not worth it!"
            $ amy.sub -= 2
            "With that, Amy pulls me away through the crowd."
        "Do nothing":
            show amy angry
            amy.say "How dare you?!?"
            amy.say "You never even met him before now!"
            show amy annoyed
            "The girl snorts and shakes her head."
            "Josie" "And here's to hoping I never will again!"
            show amy angry
            "Amy's about to say something in return."
            "But I make a point of taking her by the arm."
            mike.say "Come on, Amy..."
            mike.say "I may not know her."
            mike.say "But I know she's not worth it!"
            show amy annoyed
            $ amy.sub += 2
            "With that, I guide Amy away through the crowd."
    scene bg cinema at center, zoomAt(1.75, (640, 720)), dark
    show amy a sad at center, zoomAt(1.5, (640, 1040))
    with fade
    "As soon as we're far enough away, I stop moving so fast."
    "And I shake my head in sheer amazement."
    mike.say "Wow..."
    mike.say "You actually dated her?"
    mike.say "I'm sorry, but I don't see the appeal!"
    show amy shy
    amy.say "I know how it looks, [hero.name]."
    amy.say "But she wasn't always like that."
    show amy annoyed
    amy.say "Josie just has some beliefs that rub me up the wrong way, you know?"
    show amy upset
    "I can see that Amy's upset by the encounter."
    "But she's not just mad like me."
    "There's something bubbling under her anger."
    "Something that's really bugging her."
    menu:
        "Ask if she wants to talk about it":
            "The film's supposed to be starting soon."
            "But I can see that Amy's needing to talk."
            "So seeing a movie can wait."
            mike.say "Amy..."
            mike.say "You can talk to me about it, you know?"
            mike.say "About the way that girl was with you back there?"
            show amy shy
            "Amy nods."
            "But for a moment I think she's going to turn down the chance to talk."
            "Then she shakes her head."
            show amy worried
            amy.say "You know what, [hero.name]..."
            amy.say "I just don't get it!"
            amy.say "Like, it's sometimes hard to be a girl that likes girls."
            amy.say "Even nowadays there are some people that have a problem with you."
            mike.say "I know, Amy..."
            mike.say "And for what it's worth, I think those people suck."
            amy.say "Yeah they do."
            amy.say "But some girls that like girls can be like them."
            amy.say "They can be mean to girls that like girls AND guys!"
            amy.say "I mean, how crazy is that?"
            "I nod, trying to show that I get what she's saying."
            mike.say "I don't get it either."
            mike.say "It's like they're doing the same thing as the people that hate them!"
            show amy normal at center, zoomAt(2.0, (640, 1340))
            "Amy wraps herself around my arm and leans in close."
            $ amy.love += 2
            $ game.active_date.score += 80
            amy.say "Thanks, [hero.name]..."
            amy.say "I knew you'd understand."
            amy.say "Now let's forget about Josie."
            amy.say "And go see this film!"
            scene bg cinemaroom with fade
            "With that, we fight our way into the theatre."
            "And we're in our seats to catch the end of the opening credits."
        "Tell her to forget about it":
            "Maybe it'd be a more caring thing to ask Amy if she wants to talk."
            "But the film's supposed to be starting soon and I don't want to miss it."
            "Plus the best thing for her right now could be a distraction."
            "And we can always talk after the film anyway."
            mike.say "Ah, let's forget about her, Amy."
            mike.say "The film's starting anyway."
            mike.say "So we need to get in there!"
            show amy shy
            "Amy looks hesitant for a moment."
            "Like she's thinking about saying something more."
            "But then she seems to shake it off."
            "And she nods in agreement."
            show amy normal
            amy.say "Okay, [hero.name]."
            amy.say "You're right - we shouldn't let her ruin our date."
            scene bg cinemaroom with fade
            "Amy takes my hand and we make our way into the theatre."
            "And I remind myself to talk to her about all of this later."
            "I'm sure that I won't forget."
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return

label amy_event_07:
    play sound cell_vibrate
    if "amy" in hero.smartphone_contacts:
        $ result = renpy.call_screen("smartphone_choice", "Amy")
        if not result:
            $ hero.cancel_event()
            $ amy.love -= 5
            return
        mike.say "Hi Amy!"
        amy.say "Hey [hero.name]."
    else:
        $ result = renpy.call_screen("smartphone_choice")
        if not result:
            $ hero.cancel_event()
            return
        mike.say "Hello?"
        amy.say "Hi [hero.name]! It's Amy."
        if 'fafow' in DLCS:
            $ hero.smartphone_contacts.append("amy")
    amy.say "I just wanted to hear your voice."
    amy.say "I feel like we're getting really close, [hero.name]."
    mike.say "I feel the same way, Amy."
    amy.say "..."
    amy.say "Anyway, I've got to run. Talk soon, okay?"
    "She hangs up, and I'm left smiling at my phone like an idiot."
    # === CEMETERY EVENT REMOVED (bridge) ===================================
    #  The old amy_event_07 invited Mike to a "Date at the cemetery"
    #  (amy_event_07_date). That optional cemetery scene has been removed.
    #  To keep Amy's MAIN story chain intact, the love.max bump the cemetery
    #  date used to grant is applied here, so amy_event_08 unlocks exactly as
    #  before (event_07 done + love reaching 160). It also no longer adds Amy
    #  to the optional "goth" harem (that join lived inside the cemetery scene).
    if amy.love.max < 160:
        $ amy.love.max = 160
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return


label missed_amy_event_07_date(from_cancel=False):
    # === CEMETERY EVENT REMOVED ===  no cemetery date is ever scheduled now.
    #  Harmless stub so any pending appointment in an OLD save just returns.
    return


label amy_event_07_date(appointment=None):
    # === CEMETERY EVENT REMOVED ===  the cemetery date scene is deleted.
    #  Harmless stub for OLD saves with a pending appointment; keeps the
    #  love.max 160 gate satisfied and returns.
    if amy.love.max < 160:
        $ amy.love.max = 160
    return


label amy_event_08:
    play sound cell_vibrate
    "I feel the sensation of my phone vibrating in my pocket."
    "Pulling it out, I take a moment to check who's calling."
    $ result = renpy.call_screen("smartphone_choice", "Amy", "(URGENT)")
    if not result:
        $ hero.cancel_event()
        $ amy.set_gone_forever()
        return
    scene expression f"bg {game.room}" at dark with dissolve
    mike.say "Hey, Amy..."
    mike.say "How's it hanging?"
    mike.say "You know I was just thinking about you!"
    amy.say "Hey, [hero.name]..."
    amy.say "I was just calling to say..."
    amy.say "To say that..."
    amy.say "That I'm dumping you..."
    amy.say "Dumping you and leaving town!"
    "For a moment, my brain doesn't seem to be able to process what Amy just said."
    "I don't know if it's because of the way she just galloped through all of it."
    "Or else my brain just doesn't want to have to deal with the implications of it."
    "Either way I end up blinking for a few seconds before I can even respond."
    mike.say "Sorry, Amy..."
    mike.say "I must have had a brain fart back there."
    mike.say "For a moment I thought you said you were dumping me and leaving town!"
    amy.say "That's because I did!"
    amy.say "And there's nothing you can say to change my mind!"
    "All of a sudden the reality of the situation hits me like a slap in the face."
    "And I feel like the ground beneath my feet just gave way."
    mike.say "Amy..."
    mike.say "You can't be serious..."
    mike.say "I mean...why are you dumping me?"
    mike.say "And leaving town too?!?"
    mike.say "This all sounds so crazy!"
    amy.say "Don't ask me to explain it, because I can't."
    amy.say "I just know that it's got to be this way!"
    amy.say "So this is goodbye..."
    mike.say "Amy, wait..."
    mike.say "We can talk about this..."
    mike.say "We can..."
    "Despite all of my efforts to get through to Amy, nothing seems to work."
    scene expression f"bg {game.room}" with dissolve
    "As she ends the call before I can say anything more."
    "Which leaves me staring in silence at the phone in my hand."
    menu:
        "That can't be the end... THAT WON'T BE THE END!":
            "For a moment I think that it's all over, that Amy's just walked out of my life."
            "But then I shake it off and wonder what in the hell I'm even thinking."
            "This is totally crazy, like something that happens in a dumb romance novel or romcom!"
            "And we're not living in one of those - this is the real world."
            "And if Amy thinks that she's going to dump me like that, then she's wrong."
            "At the very least she owes me a damn good explanation!"
            "With that in mind, I hurry over to her place as fast as I possibly can."
            scene bg amyhome with fade
            pause 0.2
            play sound door_banging
            "Walking straight up to the front door, I hammer on it with a clenched fist."
            mike.say "AMY!"
            mike.say "Amy, are you in there?"
            mike.say "You have to open the door so we can talk about this!"
            "Almost as soon as I'm finished saying this, a door opens."
            "But unfortunately it's the one that belongs to Amy's neighbour."
            "I turn in that direction to see a little old woman with a cat in her arms."
            "And another half-dozen or so felines wrapping themselves around her ankles too!"
            "She's looking straight at me, and I'm already preparing myself for a telling-off."
            "So it comes as quite a surprise when that's not what happens."
            "Neighbour" "I'm sorry, young man..."
            "Neighbour" "But the young lady who lives there isn't in."
            mike.say "Oh...erm..."
            mike.say "Thank you...I think..."
            mike.say "You wouldn't happen to know where she went, would you?"
            "The old lady looks at me sadly as she shakes her head."
            "Neighbour" "I'm afraid that I don't."
            "Neighbour" "All I know is that she had some luggage with her."
            "Neighbour" "Looked like she was going on trip to somewhere."
            "My mind races as I try to figure out where Amy could have been headed."
            "The idea of her taking a flight somewhere just doesn't feel right."
            "But the train station seems a far more likely destination."
            mike.say "Thank you..."
            mike.say "But I have to go!"
            "I don't even look at the old woman as I say all of this."
            "Because I'm already turning to run down the stairs and out of there."
            scene bg street with fade
            "As soon as I'm back on street level, I hail a taxi."
            play sound car_door
            "Jumping inside, I pretty much bellow at the driver."
            mike.say "To the station..."
            mike.say "And step on it!"
            "I don't think the driver really takes my demands for speed that seriously."
            "As he's probably more interested in keeping his licence than doing as I asked."
            "Even so, he still manages to get me to the station pretty quickly."
            "I shove the money for the fare into his hand and leap out of the taxi."
            "Because I've already caught sight of Amy in front of the station."
            scene bg taxi car open with hpunch
            "As soon as I'm out of the cab, I rush straight towards her."
            "And in my hurry to reach her, I don't pay any attention to the traffic between us."
            mike.say "AMY!"
            mike.say "AMY...WAIT!"
            "I don't know if it's my shouting that gets Amy's attention."
            "Or whether it's the sound of car horns blaring as I dodge between moving vehicles."
            "But either way she stops in her tracks, allowing me to catch up to her."
            show amy pain casual with dissolve
            mike.say "Amy..."
            mike.say "Don't go!"
            "As soon as she hears my voice, Amy bursts into a flood of tears."
            "She drops the luggage that she's carrying and wrings her hands together too."
            show amy whining
            amy.say "No, no, no!"
            amy.say "You can't be here, [hero.name]..."
            amy.say "You were supposed to let me leave!"
            show amy sad
            mike.say "How can I do that, Amy?"
            mike.say "I have genuine feelings for you."
            mike.say "And I don't even know why you want to leave me!"
            "All this does is send Amy into another burst of crying and wailing."
            show amy whining
            amy.say "But you have to let me go."
            amy.say "You have to because I'm falling in love with you!"
            amy.say "And when that happens, I always screw it up."
            amy.say "So I need to leave before that can happen, don't you see?"
            show amy sad
            "I shake my head, trying to make sure I heard that right."
            mike.say "You're serious?"
            mike.say "You're falling in love with me?"
            show amy whining
            amy.say "Yeah, but weren't you listening?"
            amy.say "I'm sure to make a massive mess of it!"
            show amy sad
            mike.say "I love you too, Amy..."
            mike.say "And I'd rather take my chances that you screw it up."
            mike.say "Much more than I would never knowing if it'd have worked or not."
            show amy lying
            amy.say "You..."
            amy.say "You really mean that?"
            show amy pain
            mike.say "Of course I do, Amy!"
            show amy lying
            amy.say "Well...maybe we could give it a little try, see what happens?"
            show amy at center, zoomAt(1.5, (640, 1040)) with fade
            "I nod eagerly, throwing my arms around Amy."
            hide amy
            show amy kiss casual
            with fade
            $ amy.flags.kiss += 1
            "She returns the gesture, and then it evolves into a kiss."
            "I feel a flood of genuine relief flowing through me the whole time."
            "And sure, we still have to work through whatever issues Amy has."
            "But for now, I'm just grateful that she's decided to stay."
            $ amy.hide()
            $ amy.flags.amydelay = TemporaryFlag(True, 2)
            $ amy.flags.addressknown = True
        "So this is how it ends?":
            "For a moment I'm ready to rush out of the door and straight over to Amy's place."
            "But then it occurs to me that I'm probably already too late to catch her."
            "Amy's not the kind of girl to do something like this as a cry for help."
            "And my guess is that she'll already have been on her way when she made that call."
            "So it seems like there's nothing I can do, save for accepting she's gone and I've lost her."
            "I can already feel the sense of loss and frustration welling up inside of me."
            "Getting worse with every second that passes, making it feel ever more real."
            "Maybe it'll get better in time."
            "Maybe one day I'll be able to forget all about Amy."
            "But until that day comes, I'll always be wondering why she left."
            "And why she felt like she couldn't tell me the reason as well."
            $ amy.set_gone_forever()
    return

label amy_event_09:
    "After the whole incident where she tried to dump me and leave town, I figured Amy would need some time."
    "So I've deliberately left it to her to be the one that contacts me, though it's been a hard thing to do."
    "One thing all of this has made me realise is that my feelings for her are very real and very intense."
    "Which means that I'm constantly fighting the urge to pick up the phone and call her whenever she comes to mind."
    "But somehow I manage to find the willpower to stick to it."
    play sound cell_vibrate
    "And when Amy does choose to call me, I'm crazily relieved to hear from her."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Amy")
    if not result:
        $ hero.cancel_event()
        $ amy.love -= 10
        return
    if amy.love.max < 180:
        $ amy.love.max = 180
    $ amy.unhide()
    scene expression f"bg {game.room}" at dark with dissolve
    mike.say "Hey, Amy..."
    mike.say "It's great to hear your voice!"
    "There's a slight pause on the other end of the line before Amy replies."
    "And when she finally does, her voice sounds more than a little nervous."
    amy.say "H...hi, [hero.name]..."
    amy.say "I was wondering..."
    amy.say "Could we maybe meet up?"
    amy.say "Because I think we have a lot to talk about!"
    mike.say "Of course, Amy..."
    mike.say "Just tell me where and when, okay?"
    scene expression f"bg {game.room}" with dissolve
    "As soon as we've agreed on a time and place, we wrap up the call."
    "And then I hurry to get over there in time to meet Amy."
    scene bg park
    show amy puzzled casual
    with fade
    "When I arrive, she's already there and waiting for me."
    "Which instantly tells me that this is going to be serious."
    "Because Amy almost never gets somewhere before me."
    "And when she does get there, she's usually late too."
    "I try to put all of that out of my mind as I walk over to Amy."
    show amy shy
    "Because I can already see she's standing there wringing her hands."
    "And she's finding it hard to look me in the eyes too."
    mike.say "Hey, Amy..."
    mike.say "I came as fast as I could."
    show amy puzzled
    amy.say "Hey, [hero.name]..."
    amy.say "I wasn't sure you'd want to come at all."
    show amy pain
    amy.say "Not after what I did the other day!"
    amy.say "I'm so sorry about that - can you forgive me?"
    show amy annoyed
    "I manage to put on a weak smile as I wave away Amy's apology."
    mike.say "Of course I can, Amy."
    mike.say "Actually, I'm more worried about you than anything else."
    mike.say "Were you actually going to leave town for real?"
    show amy blush
    "Amy's cheek begin to flush red."
    "And it takes a moment before she can bring herself to nod."
    show amy shy
    amy.say "I...I probably would have gone through with it."
    amy.say "If you hadn't come to stop me, that is."
    amy.say "I've done it before - more than once!"
    "I shake my head, trying to understand what could have made Amy do such a thing."
    "It all just seems too extreme and dramatic to me, I find it hard to explain."
    mike.say "But why, Amy?"
    mike.say "I thought everything was going so well between us?"
    mike.say "We seemed to be getting along great, having so much fun."
    show amy sadsmile
    amy.say "We were, [hero.name]!"
    amy.say "And that's where it always starts with me."
    show amy shy
    amy.say "I meet someone, we hit it off and we start dating."
    amy.say "And just when everything's going great, that's when it happens."
    mike.say "When what happens, Amy?"
    show amy pain
    amy.say "When I start to get paranoid that it won't last."
    show amy annoyed
    amy.say "That it's all going to go wrong and I'm gonna get hurt!"
    amy.say "I get so scared of that happening..."
    show amy worried
    amy.say "I end up dumping them before it can happen for real!"
    show amy annoyed
    "I shake my head, still trying to comprehend what Amy's saying."
    mike.say "But, Amy..."
    mike.say "That sounds like it'd hurt much worse than an actual break-up."
    mike.say "And at least if you did break-up with someone for real..."
    mike.say "Well, you'd still have your memories of all the good times to look back on."
    show amy worried -blush
    "Amy nods at this, looking me straight in the eyes for the first time."
    show amy pain
    amy.say "I know all of that, [hero.name]..."
    amy.say "But this is one of those things that only makes sense in my own head."
    amy.say "When someone else tells me it sounds crazy, I know they're right."
    amy.say "Then when they're gone and I'm alone with the voices in my brain..."
    show amy worried
    amy.say "You know how it is, right?"
    "I don't know if I really do understand what Amy's trying to tell me."
    "But I nod all the same, even if it's just for the sake of moving things on."
    "And it's then that a thought occurs to me."
    mike.say "But this is different, right?"
    mike.say "Something different happened this time round?"
    show amy puzzled
    "Amy looks at me like she's interested in what I'm suggesting."
    "But it seems that I'm going to have to explain myself a little better."
    mike.say "What I mean is, you're still here, Amy."
    mike.say "You wanted to run away like you did before."
    mike.say "But something kept you from doing it."
    mike.say "You're here talking to me about being afraid and running away."
    mike.say "And that makes me think you want to beat your fears, yeah?"
    show amy normal
    "Now Amy's starting to nod."
    "And it seems like my words are getting through to her."
    amy.say "Yeah..."
    amy.say "That makes sense."
    amy.say "I never spoke about it with anyone before, I just ran away."
    show amy sadsmile
    amy.say "That means I can beat this thing...you think?"
    mike.say "I don't think you can beat it, Amy..."
    mike.say "I know you can beat it."
    mike.say "And I'll be there with you every step of the way."
    mike.say "We can beat this thing together."
    show amy kiss casual with fade
    $ amy.flags.kiss += 1
    $ amy.love += 2
    "Amy throws her arms around me without saying another word."
    "And I return the embrace, simply glad to have convinced her to stay."
    "Anything that we have to face in the future can wait."
    "At least until we stop hugging and squeezing the life out of each other."
    return

label amy_event_10:
    "Amy and I have been in kind of a strange place recently."
    "Ever since the whole trying to dump me and run away incident."
    "It's kind of like we're always watching each other."
    "Waiting for someone to mention it or apologise all over again."
    "So when I get a message from Amy, asking me to come over to her place, it makes me a little nervous."
    menu:
        "Go see her":
            pass
        "Maybe another time":
            $ hero.cancel_event()
            $ amy.love -= 5
            return
    if amy.love.max < 200:
        $ amy.love.max = 200
    scene bg street with fade
    "I still say yes, letting her know that I'm on my way over there."
    "But I'm pretty worried about what kind of state Amy might be in when I get there."
    scene bg door black secure at center, zoomAt(1.0, (640, 720)) with fade
    "So much so that I almost hesitate when it's time to knock on the door."
    "But then I shake my head, trying to tell myself that I'm being stupid."
    "Amy and I have already started making progress, so what is there to be scared of?"
    show bg door black secure at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "Before I can change my mind, I reach out my hand and knock."
    mike.say "Hey, Amy..."
    mike.say "I'm here!"
    mike.say "Are you going to let me in or what?"
    amy.say "The door's open, [hero.name]..."
    amy.say "So you can let yourself in."
    scene bg black with dissolve
    pause 0.5
    scene bg amyhome
    with wiperight
    "I push the front door open and step into the hallway."
    "And for at least a few moments, my former misgivings are replaced by new ones."
    "Because I'm already thinking of giving Amy a lecture about the need to keep her door locked."
    "But when I walk into the sitting room, all thought of doing so vanishes."
    amy.say "Hey, [hero.name]..."
    amy.say "Thanks for coming over at such short notice."
    scene bg amyhome at center, zoomAt(1.5, (320, 1000))
    show amy casual puzzled blush at center, zoomAt(2.5, (440, 1600))
    show concert_solo_instrument_mike at center, zoomAt(2.5, (550, 3000)), rotation(5.5)
    with dissolve
    "Amy's sitting on a stool, a guitar balanced in her lap."
    "That's not at all unexpected, as I've known for a long while that she plays."
    "But I definitely wasn't expecting that to figure into my visit here today."
    mike.say "What's with the guitar, Amy?"
    mike.say "Have you been practising?"
    show amy shy
    "Amy glances down at the guitar and then back up at me."
    show amy normal
    amy.say "Yeah..."
    amy.say "Kinda, I guess..."
    "It's one of those weird, non-committal answers."
    "The kind that leave you more puzzled than before you asked the question."
    mike.say "Erm..."
    mike.say "I'd offer to jam with you or something..."
    mike.say "But I left my guitar at home!"
    "Amy shakes her head at this."
    show amy sadsmile -blush
    amy.say "Oh no..."
    amy.say "I should have told you..."
    amy.say "I have something that I want to play for you."
    "Now Amy really has got my full attention."
    "She told me that she used to be in a band."
    "But I never knew if she was the one that actually wrote their songs."
    mike.say "Okay, Amy..."
    mike.say "I suppose you've been working on some new goth stuff?"
    mike.say "Songs about creepy European castles and ancient vampires?"
    show amy shy blush
    "Amy blushes a little at this, and she shakes her head."
    amy.say "Not this time, [hero.name]..."
    show amy puzzled
    amy.say "This time I decided to try and channel my emotions into the lyrics."
    amy.say "I thought that I could use music to express just how I feel about you!"
    "Now it's my turn to be the one blushing."
    "Because Amy just caught me totally off-guard."
    mike.say "A love song?"
    mike.say "About you and me?"
    mike.say "Wow..."
    mike.say "I never thought someone would write something like that!"
    show amy shy
    amy.say "Well..."
    show amy normal
    amy.say "Would you like me to play it for you?"
    "The truth is that I'm kind of scared to hear what Amy's written."
    "It might be the best thing I've ever heard and move me to tears."
    "But what if it's bloody awful and I can't stand to hear it all the way through?"
    "I guess the only choice that I have is to listen and see how it is."
    "So I nod, letting Amy know that she can start playing her song."
    "To be honest, she looks as nervous as I feel."
    show amy upset -blush
    "But I see her steel herself and begin to play."
    "What follows is one of the strangest experiences in my life so far."
    "I listen to Amy play her guitar and sing her song."
    "And it doesn't take me long to realise there's more happening here."
    "Amy's not just playing, she's actually opening herself up to me."
    "The weaving together of music and lyrics lets me see right into her heart."
    "Maybe into her soul as well!"
    "In reality, the song can't have lasted for more than a minute or two."
    "But to me it feels like a lifetime spend inside of Amy's emotions."
    show amy normal
    "And when it's done, I find myself staring at her in a stunned silence."
    "Which is pretty awkward, as I can see that she's waiting for me to say something."
    "To tell her what I think of the song."
    show amy surprised
    amy.say "Ah, [hero.name]..."
    amy.say "Are you feeling okay?"
    amy.say "I finished my song already!"
    "Suddenly I feel myself catapulted back to reality."
    mike.say "WOW!"
    mike.say "That was totally amazing!"
    mike.say "The best love song that I ever heard!"
    show amy blush
    "Amy blinks in surprise, not expecting me to be so crazily positive."
    "And now she really is blushing, her cheeks almost glowing red."
    show amy puzzled
    amy.say "Oh..."
    amy.say "I...I don't know about that!"
    show amy normal
    amy.say "But I am glad that you like it."
    mike.say "Have you thought about recording it?"
    show amy shy
    amy.say "I don't know about that..."
    mike.say "Seriously, Amy - the world needs to hear this song!"
    show amy normal -blush
    amy.say "Really, [hero.name] - I'd like to keep it between us."
    amy.say "You know, between the two of us?"
    "I shrug, realising that I probably should let Amy have her way on this one."
    "And instead I focus my attention on pouring praise on her efforts."
    "Because her expressing her emotions like that can only be a good thing."
    "Amy's facing her feelings and coming to terms with them."
    "Rather than trying to literally run away!"
    return

label amy_kink_01:
    scene bg door restaurant
    amy.say "Whoa..."
    amy.say "[hero.name]..."
    amy.say "Are you kidding me?"
    show amy date surprised blush with dissolve
    "I frown as I turn to look at Amy."
    mike.say "Huh?"
    mike.say "What do you mean?"
    show amy puzzled
    "Amy shrugs, starting to look a little embarrassed."
    amy.say "I mean...is this really where we're going for our date?"
    amy.say "It's pretty fancy, not the kind of place I'm used to!"
    mike.say "Erm..."
    mike.say "Is that a problem, Amy?"
    show amy surprised
    amy.say "Oh no...no way!"
    if amy.sub.max < 20:
        $ amy.sub.max = 20
    show amy normal
    amy.say "I just wanted to say it's pretty impressive, that's all."
    "I nod and decide to leave it at that."
    "It sounds like Amy's giving me a compliment."
    "So I choose to take it as that and not probe any further."
    return

label amy_kink_02:
    show amy
    mike.say "Hey Amy, how about we go at the movie theater tomorrow?"
    mike.say "We could go there and watch a nice movie together?"
    show amy happy
    amy.say "Sure, [hero.name]...why not!"
    show amy normal
    amy.say "Do you already know what you want to watch?"
    mike.say "Yeah, there's Feeblejuice at 17:00."
    amy.say "Alright! Tomorrow, 17:00. Noted!"
    hide amy
    $ hero.cancel_activity()
    $ hero.calendar.add(game.days_played + 1, DateAppointment((17, 17), "amy", "Date at the cinema (Amy)", "amy_kink_02_date", "missed_amy_kink_02_date"))
    $ amy.flags.amydelay = TemporaryFlag(True, 2)
    return

label missed_amy_kink_02_date(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Amy is going to be mad."
        $ amy.love -= 10
    $ DONE.pop("amy_kink_02", None)
    $ storytracker.refresh()
    return

label amy_kink_02_date(appointment=None):
    $ game.room = "street"
    scene bg cinema
    with fade
    "..."
    "....."
    ".........."
    scene bg black with timelaps
    pause 0.2
    $ game.pass_time(1)
    scene bg cinema with timelaps
    "I pull out my phone and check the time."
    "Just like I already did a dozen times before."
    "But on this occasion it's different."
    "Because this time I don't get to see what my phone says."
    amy.say "[hero.name]!"
    amy.say "Hey!"
    amy.say "You are not going to believe what happened to me..."
    show amy b casual pain with easeinright
    "I look up to see Amy hurrying towards me."
    "She's evidently been running to get here."
    "And she seems more than a little agitated too."
    "On the one hand I'm pissed that she's showed up so late."
    "But on the other I am kind of relieved she got here in the end."
    menu:
        "My heart is filled with joy as I see you finally arrive!":
            "I shake my head and offer Amy what I hope is a reassuring smile."
            mike.say "That's okay, Amy..."
            mike.say "You're here now, and that's what matters."
            mike.say "Sure, we're running a little late."
            mike.say "But we can still catch the film if we hurry."
            show amy normal
            $ amy.love += 2
            "Amy cracks a smile of her own as she realises I'm not mad at her."
            "Then she nods as we head inside the theatre."
            show amy happy
            amy.say "Okay, [hero.name]..."
            amy.say "I'll make it up to you, I promise!"
        "You better have a good excuse for being late!":
            "I cross my arms over my chest and give Amy a hard stare."
            show amy surprised
            mike.say "You'd better be about to tell me your phone's screwed, Amy."
            mike.say "Because how else could you be late and not call to let me know?"
            "Amy stops in her tracks as I fire the question at her."
            show amy sad
            $ amy.love -= 2
            $ amy.sub += 2
            "And she looks more than a little mollified by it too."
            amy.say "Oh..."
            amy.say "I...I'm sorry..."
            amy.say "I guess I was just too tied up to think of that."
            "I roll my eyes and shake my head."
            "Which only seems to make Amy look even more guilty."
            mike.say "Look, just forget about it, okay?"
            mike.say "We're already late."
            mike.say "But we can still catch the film if we hurry."
            show amy worried
            amy.say "Okay, [hero.name]..."
            amy.say "I'll make it up to you, I promise!"
            $ DONE.pop("amy_kink_02", None)
            $ hero.cancel_event()
            scene bg black with dissolve
            pause 1
            $ game.pass_time(1)
            return
    scene bg black with timelaps
    pause 1
    $ game.pass_time(1)
    scene bg street
    show amy casual shy
    with timelaps
    "I can see that Amy's got something on her mind."
    "But it doesn't look like she can summon up the courage to say it."
    "Another time I might have been okay to let it go."
    "Or else wait for her to be able to put it into words."
    "But right now I'm intrigued enough to just come out and ask her."
    mike.say "Amy..."
    mike.say "What's up?"
    show amy surprised
    amy.say "Huh?"
    mike.say "I mean..."
    mike.say "You look like there's something bugging you."
    show amy blush
    "The moment I say this, I can see Amy starting to blush."
    "But all the same, she begins to explain herself."
    show amy shy
    amy.say "Well, it was about earlier..."
    amy.say "When I showed up late for the movie."
    "I shake my head and wave my hand in the air."
    "All to show Amy that it doesn't matter."
    mike.say "Nah, it's cool."
    mike.say "I'd almost forgotten it happened!"
    show amy worried -blush
    amy.say "No..."
    amy.say "I meant when I said that I'd make it up to you."
    show amy shy blush
    amy.say "And I was thinking..."
    amy.say "It was kind of naughty of me not to call you or anything."
    show amy puzzled
    amy.say "So maybe you should...punish me a little?"
    "As if to make her point, Amy turns her back to me."
    "And then she sticks her ass out, wiggling it a little too!"
    amy.say "You could like...spank me, maybe?"
    menu:
        "Smack that! All on the floor! Smack that!":
            "I can't keep my face from lighting up at the offer."
            "And my head starts bobbing up and down before I can even say a word."
            mike.say "Y...you're serious?"
            mike.say "You want me to spank you?!?"
            show amy normal
            "The fact that I can't hide my enthusiasm is obvious."
            "And it seems to be filling Amy with confidence too."
            "Because she's looking less embarrassed and more aroused by the second."
            amy.say "Oh yeah, [hero.name]."
            show amy flirt
            amy.say "I want you to spank me nice and hard!"








            amy.say "I've been a very naughty girl, remember?"
            amy.say "So don't feel like you have to go easy on me!"
            hide amy
            show slap amy amy_casual happy waiting
            "Even though Amy's looking the other way, I still nod eagerly."
            "Then I put one hand on her shoulder while raising the other into the air."
            "Both of us seem to be holding out breath as we wait for it to happen."
            "And it's weird, but I almost feel like I have no control over it myself!"
            "So when my hand swings down for the first time, it jolts me back to reality."
            play sound spank
            show slap amy slapping
            $ amy.flags.slapassmod = 5
            if amy.sub.max < 40:
                $ amy.sub.max = 40
            $ amy.sub += 1
            "There's the sound of a sudden cracking, and Amy lets out a yelp."
            "And that's all it takes for me to be into it and away."
            show slap waiting
            pause 0.7
            play sound spank
            show slap slapping
            $ amy.sub += 1
            "Blow after blow makes contact with Amy's pale cheeks."

            show slap waiting
            pause 0.7
            play sound spank
            show slap slapping
            $ amy.sub += 1
            "The feeling is amazing, somehow solid and soft at the same time."


            "My cock's hard almost from the start, my heart pounding in my chest."
            show slap waiting
            pause 0.4
            play sound spank
            show slap slapping
            $ amy.sub += 1
            pause 0.3
            show slap waiting
            pause 0.4
            play sound spank
            show slap slapping
            $ amy.sub += 1
            "I must have been picking up speed and force too."
            "Because pretty soon my hand feels numb and I can't feel a thing."
            "Fearing that I might be doing permanent damage to Amy and myself, I begin to slow down again."
            "And as I do so, her yelps start to subside too."
        "Hitting a woman? Nope, I pass.":


            "I wrinkle my face up at the idea."
            "It's an intriguing offer, for sure."
            "But somehow I just don't feel like it."
            mike.say "Thanks for the offer, Amy."
            mike.say "But could we maybe do something else instead?"
            show amy surprised
            "Amy looks a little surprised at my turning her down."
            "And her embarrassment level rises as a result too."
            "But she does the best she can to recover and move on."
            show amy shy
            amy.say "Oh..."
            amy.say "Okay, [hero.name]..."
            amy.say "We don't have to if you don't want to."
    return

label amy_kink_03:
    show amy annoyed
    "It doesn't take a genius to see that Amy's less than happy when we meet up."
    "Amy might be a goth, but she's not the kind that's always mooching around and miserable."
    "So I guess the right thing to do is ask her and find out what the problem could be."
    mike.say "Amy..."
    mike.say "Is something wrong?"
    mike.say "Did Shawn stop you playing Cure tracks at work again?"
    show amy mad
    "Amy looks at me with a frown on her face."
    amy.say "No he did not, [hero.name]."
    show amy angry
    amy.say "And for your information it's 'THE CURE'!"
    "I hold up my hands and take a step backwards."
    mike.say "Whoa..."
    mike.say "Sorry, Amy."
    mike.say "I was just trying to lighten the mood, that's all."
    mike.say "I guess whatever's bothering you is serious, huh?"
    show amy annoyed
    "My backing off seems to have done the trick."
    show amy sad
    "As Amy's expression softens considerably."
    "But I note that she also sags a little."
    "Which all but confirms my suspicions that it's something serious."
    amy.say "No, [hero.name]..."
    show amy pain
    amy.say "I'm sorry - sorry for snapping at you like that."
    amy.say "But yeah, it's kind of serious."
    amy.say "And I was hoping you could help me out with it too."
    mike.say "Well I won't know that unless you tell me what's up."
    show amy normal
    "Amy nods and lets out a sigh."
    "Then she begins to explain."
    amy.say "Okay..."
    amy.say "So I got a ticket off a cop the other day."
    mike.say "A ticket?"
    mike.say "I didn't know you even had a car."
    show amy upset
    amy.say "I don't!"
    amy.say "The ticket was for anti-social behaviour, if you can believe that!"
    mike.say "Wouldn't that be a citation, rather than a ticket?"
    show amy annoyed
    amy.say "Does that really matter, [hero.name]?"
    show amy mad
    amy.say "Look, I was being hassled by some guy."
    amy.say "Middle of the day, right there in the street."
    "This is starting to sound pretty serious."
    "So I nod, making it clear that I'm listening."
    show amy upset
    amy.say "I tell him to fuck off, but he's not taking the hint."
    amy.say "So then I knee him in the balls and start shouting for help."
    show amy annoyed
    amy.say "Next thing I know, this cop turns up."
    amy.say "And I think that means I'm safe, right?"
    mike.say "Of course, Amy..."
    mike.say "That should have been enough for them to bust that creep!"
    show amy mad
    amy.say "But that's the thing, you see..."
    amy.say "I explain it all to the cop."
    show amy upset
    amy.say "Then when I look round, the guy's gone!"
    amy.say "And the cop, she starts lecturing me about breaching the damn peace."
    amy.say "Next thing I know, the bitch is writing me up!"
    "I can't help grimacing as Amy finishes her story."
    "Because it sounds like she really got screwed-over."
    "But then I remember something else that Amy said."
    mike.say "Erm..."
    mike.say "How exactly do I fit into this, Amy?"
    mike.say "I'm not sure what I can do to help out."
    show amy shy
    amy.say "Thing is, [hero.name]..."
    amy.say "I can't afford to have something like this on my record."
    amy.say "But I don't have a clue about this kind of thing."
    amy.say "And you look a lot more serious than I do."
    show amy worried blush
    amy.say "Would you go down to the station and talk to the cop about this?"
    amy.say "You'd be doing me a massive favour, and I'd be crazily in your debt..."
    menu:
        "I'll talk to that cop":
            "At first I'm not too sure what good me going down there would do."
            "But the idea of coming to Amy's rescue is too appealing to ignore."
            "And then I start to think about just how unfair the whole thing is."
            "The way it went down is a genuine miscarriage of justice!"
            "Well, maybe a small one - but a miscarriage of justice all the same."
            mike.say "Hmm..."
            mike.say "It does sound like that cop was being unfair to you."
            mike.say "And you were only shouting for help, which isn't a crime."
            show amy happy -blush
            amy.say "Exactly!"
            amy.say "So you'll do it?"
            show amy normal blush
            amy.say "You'll go down to the station for me?"
            "I was almost ready to say yes before Amy asked me a second time."
            "But seeing her looking up at me right now, with those big eyes of hers..."
            "I doubt that I could have said no to anything she asked of me."
            mike.say "Of course I will, Amy."
            mike.say "You just leave it to me."
            show amy happy -blush
            $ amy.love += 2
            amy.say "Aww!"
            amy.say "Thanks, [hero.name] - you're the best!"
            $ amy.flags.police_ticket = True
        "I don't really want to be involved":
            "The moment Amy asks me to speak to the cops, I feel my guts churn."
            "There's no way I'm going to be able to get her off just by talking to them!"
            mike.say "No way, Amy!"
            mike.say "I'm not a lawyer."
            mike.say "I can't talk to the cops for you!"
            show amy sad -blush
            "Amy looks disappointed."
            "But she's not about to just let it drop."
            show amy normal
            amy.say "Oh, come on..."
            amy.say "You're super smart, [hero.name]."
            amy.say "I'm sure they'd listen to you."
            "For a moment I'm kind of thrown by Amy's compliment."
            "But then I realise what she's trying to do."
            mike.say "Nice try, Amy..."
            mike.say "But flattery's not going to change my mind."
            mike.say "Anyway, I could end up making things worse."
            "Amy looks like she's going to keep on arguing with me."
            show amy sad
            $ amy.love -= 2
            "But then she stops and clamps her lips together with visible effort."
            "And she nods before opening her mouth again."
            amy.say "I guess you're right."
            amy.say "I'm just going to have to go down there myself."
            amy.say "Maybe I can talk myself out of it..."
            $ amy.flags.police_ticket = False
    $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return

label amy_kink_03_police:
    scene bg street
    "I find myself standing outside the doors to the police station."
    "And just for a moment I have to stop and remind myself of how I got here."
    "That and the reason that I've chosen to walk through those doors too."
    "I'm actually about to try to talk them into letting someone else off."
    "Well, at least it's not me that's on the hook for anything this time."
    "And I guess that the worst thing that can happen is them just saying no."
    "So I take a deep breath, then I open the door and step inside."
    scene bg policestation with fade
    "I don't waste any time in walking up to the desk where a bored-looking cop is sitting."
    mike.say "Erm..."
    mike.say "Excuse me, Officer..."
    show jack date as policeman at center, zoomAt(1.25, (300, 1000)), blacker with dissolve
    "Policeman" "Yeah, yeah..."
    "Policeman" "What can I do you for?"
    mike.say "A friend of mine was served a citation the other day."
    mike.say "She told me it was for breach of the peace?"
    "The cop stares at me blankly for a few seconds."
    "But I'm so nervous I just stare right back."
    "It's only when I see their eyes rolling that I realise they were waiting for me to say more."
    show jack date as policeman at center, zoomAt(1.0, (300, 1000)), blacker, startle
    "Policeman" "And that brings you here why, exactly?"
    "Policeman" "I mean, on a charge like that, we won't have them in the cells or nothing!"
    mike.say "Oh no..."
    mike.say "I wanted to talk to the officer that issued the citation."
    mike.say "To tell them that there must have been a mistake."
    "As soon as the word 'mistake' leaves my mouth, I know that I've made one myself."
    show jack date as policeman at center, zoomAt(1.0, (300, 1000)), blacker, startle
    "The cop looks at me like I just insulted the entire police force."
    "Policeman" "Oh you do, do you?"
    "Policeman" "Come to think of it, I heard about that incident."
    if camila.is_gone_forever or camila.flags.schedule == "hospital":
        "Policeman" "..."
        "Policeman" "You know, that's very kind of you to show up here and try to make things right for your friend."
        "Policeman" "And I am in a good mood today, so let's just forget about this ticket, alright?"
        mike.say "R-Really?!"
        "Policeman" "Of course!"
        "Policeman" "Now get out of here I have work to do."
        mike.say "Thank you officer!"
        if hero.money >= 200:
            "Policeman" "Hey wait just a minute friend!"
            "Policeman" "I expected some kind of appreciation for what I did for your friend."
            "Policeman" "Something more than just {i}\"Thank you officer!\"{/i}"
            mike.say "That's what I thought..."
            $ hero.money -= 200
        if amy.sub.max < 60:
            $ amy.sub.max = 60
        $ game.room = "map"
        return
    "Policeman" "And I know just who the officer in question was."
    "Policeman" "Just you wait right there while I call her up..."
    "I nod and try to smile as the cop picks up the phone."
    "Then I get a nod in return."
    "Policeman" "She'll be right down."
    "Policeman" "And good luck."
    hide jack as policeman with dissolve
    "I turn around and take a few steps away from the reception desk."
    "But not before I hear the cop behind it mutter quietly."
    "Policeman" "Because you're gonna fucking need it!"
    "There's no time for me to say or do anything however."
    "As a door swings open a moment later."
    "And I hear someone calling out from that direction."
    camila.say "Alright..."
    camila.say "Where's the limp-dick wise-guy?"
    camila.say "The one that wants to question my work?!?"
    if "kylie_investigation_2" in DONE:
        "I really should have known that the cop in question would be Camila."
        "And now I have to explain myself to her in the most painful way possible."
        mike.say "Erm..."
        mike.say "Hey, Camila!"
        show camila work surprised with fade
        "As soon as she sees me, Camila's whole demeanour changes."
        "And by that I don't mean that she becomes totally friendly either."
        show camila flirt
        "More like she looks amused at the idea I'm here to challenge her."
        camila.say "Hey, [hero.name]."
        camila.say "Nobody told me the wise-guy was you!"
        show camila bored
        camila.say "So...what's this all about?"
        "I take another deep breath."
        "And then all I can do is just go for it."
        mike.say "Yeah..."
        mike.say "Thing is, you booked a friend of mine the other day."
        show camila surprised
        camila.say "The goth chick?"
        camila.say "Yeah, I remember her."
        mike.say "Her name's Amy..."
        show camila normal
        camila.say "Whatever..."
        camila.say "She was screaming her head off in the middle of the street!"
        mike.say "But the thing was, before you got there..."
        mike.say "She was being harassed...well, assaulted really!"
        "Camila rolls her eyes and chuckles to herself."
        show camila bored
        camila.say "Whatever, [hero.name]."
        camila.say "She gave me that line of BS too."
        camila.say "But there was no sign of any guy when I got there."
        if hero.knowledge >= 70 - camila.love * .35:
            "I pause to think about what the Camila's saying for a moment."
            "And I have to admit that she's right, nobody but Amy actually saw the guy."
            "But then I remember that's not really true."
            "Because in the middle of the city, there's always someone watching."
            show camila annoyed
            mike.say "You know that for sure, Camila?"
            mike.say "I'm sure you checked the CCTV footage around where it happened, right?"
            mike.say "Because that'd be the best way to know for sure."
            "I make sure to keep my tone respectful."
            "That and the expression on my face neutral too."
            "Because the last thing I want is for the Camila to think I'm trying to insult her."
            show camila normal
            camila.say "Ah, shit!"
            camila.say "I hate it when this happens."
            mike.say "You mean..."
            show camila bored
            camila.say "Okay, okay...I admit it."
            camila.say "I forgot to check the CCTV."
            camila.say "Wait here while I go pull it up."
            hide camila with fade
            "I wait patiently as the Camila hurries off."
            "And when she comes back, I do the best I can not to seem smug."
            show camila work weird with fade
            camila.say "Urgh..."
            camila.say "I hate being wrong, [hero.name]."
            camila.say "But it looks like I'm gonna have to tear up that citation."
            show camila normal
            camila.say "Tell your friend she's off the hook."
            show camila at right with ease
            "Camila shrugs and then nods back over her shoulder."
            camila.say "Look, I gotta get back to work."
            show camila wink
            $ camila.love += 2
            camila.say "But did your friend a real solid today, [hero.name]."
            camila.say "And standing up to me took some serious balls."
            hide camila with easeoutright
            "With that, she turns and walks away."
            "Leaving me pleased that I was able to help Amy."
            if amy.sub.max < 60:
                $ amy.sub.max = 60
        else:
            "It sounds like this is a case of one person's word against that of another."
            "But surely Camila should be listening to what a member of the public is claiming?"
            show camila annoyed
            mike.say "Don't you guys have a duty to protect and serve?"
            mike.say "You can't just ignore what Amy says happened!"
            mike.say "Can you?"
            show camila flirt at startle
            "The Camila snorts with laughter at this."
            camila.say "Look, [hero.name]..."
            camila.say "I know that you're a stand-up kind of guy."
            camila.say "And it takes balls to come down here and stand up for your friend."
            camila.say "But unless you can pull some new evidence out of your ass..."
            show camila at right with ease
            "Camila shrugs and then nods back over her shoulder."
            show camila normal
            camila.say "Look, I gotta get back to work."
            camila.say "If you do find anything else out..."
            if "camila" in hero.smartphone_contacts:
                camila.say "Call me, yeah?"
                camila.say "Or just come down here and ask for me."
            else:
                camila.say "Come down here and ask for me."
            hide camila with easeoutright
            "With that, she turns and walks away."
            "Leaving me frustrated that I couldn't do anything to help Amy."
    else:
        "I turn to see who just stormed out of the door."
        show camila work annoyed with fade
        "And when I do, I don't know whether to be scared or turned on."
        "Because the cop that's standing in front of me is pretty hot!"
        "I put a hand in the air and force a nervous smile onto my face."
        mike.say "I..."
        mike.say "I guess that would be me."
        show camila at center, zoomAt(1.5, (640, 1040)), vshake
        "The cop strides towards me the moment I speak up."
        "She comes to a halt right in front of me."
        "Her hands planted on her hips and her jaw jutting out defiantly."
        show camila angry
        camila.say "Okay, asshole..."
        camila.say "You wanna say your piece?"
        camila.say "But make it quick, yeah?"
        camila.say "So I can get on with kicking your butt out of here!"
        mike.say "Yeah..."
        mike.say "Thing is, you booked a friend of mine the other day."
        show camila annoyed
        camila.say "The goth chick?"
        camila.say "Yeah, I remember her."
        camila.say "Screaming her head off in the middle of the street!"
        mike.say "But the thing was, before you got there..."
        mike.say "She was being harassed...well, assaulted really!"
        "The cop rolls her eyes and chuckles to herself."
        show camila bored
        camila.say "Whatever, buddy."
        camila.say "She gave me that line of BS too."
        camila.say "But there was no sign of any guy when I got there."
        if hero.knowledge >= 70:
            "I pause to think about what the cop's saying for a moment."
            "And I have to admit that she's right, nobody but Amy actually saw the guy."
            "But then I remember that's not really true."
            "Because in the middle of the city, there's always someone watching."
            show camila annoyed
            mike.say "You know that for sure, officer?"
            mike.say "I'm sure you checked the CCTV footage around where it happened, right?"
            mike.say "Because that'd be the best way to know for sure."
            "I make sure to keep my tone respectful."
            "That and the expression on my face neutral too."
            "Because the last thing I want is for the cop to think I'm trying to insult her."
            show camila normal
            camila.say "Ah, shit!"
            camila.say "I hate it when this happens."
            mike.say "You mean..."
            show camila bored
            camila.say "Okay, okay...I admit it."
            camila.say "I forgot to check the CCTV."
            camila.say "Wait here while I go pull it up."
            hide camila
            "I wait patiently as the cop hurries off."
            "And when she comes back, I do the best I can not to seem smug."
            show camila work weird
            camila.say "Urgh..."
            camila.say "I hate being wrong, buddy."
            camila.say "But it looks like I'm gonna have to tear up that citation."
            show camila normal
            camila.say "Tell your friend she's off the hook."
            "Before she walks away, the cop reaches into her jacket."
            "I can't help flinching, thinking that she might be going for her gun."
            show camila flirt at center, zoomAt(1.5, (640, 1040)), startle
            "But she laughs as she hands me a business card."
            camila.say "You did your friend a real solid today, buddy."
            camila.say "And standing up to me took some serious balls."




            hide camila with easeoutright
            "With that, she turns and walks away."
            "Leaving me pleased that I was able to help Amy."
            "But also fascinated by the way she kinda scares me and turns me on at the same time."
            if amy.sub.max < 60:
                $ amy.sub.max = 60
        else:
            "It sounds like this is a case of one person's word against that of another."
            "But surely the cop should be listening to what a member of the public is claiming?"
            show camila annoyed
            mike.say "Don't you guys have a duty to protect and serve?"
            mike.say "You can't just ignore what Amy says happened!"
            mike.say "Can you?"
            show camila flirt at center, zoomAt(1.5, (640, 1040)), startle
            "The cop snorts with laughter at this."
            camila.say "Look, buddy..."
            camila.say "You seem like a decent guy."
            camila.say "And it takes balls to come down here and stand up for your friend."
            camila.say "But unless you can pull some new evidence out of your ass..."
            hide camila
            show camila work
            "She underlines her point by shrugging and taking a step backwards."
            "But before she walks away, the cop reaches into her jacket."
            "I can't help flinching, thinking that she might be going for her gun."
            show camila normal







            hide camila with easeoutright
            "With that, she turns and walks away."
            "Leaving me frustrated that I couldn't do anything to help Amy."
            "But also fascinated by the way she kinda scares me and turns me on at the same time."
    $ game.pass_time(1)
    $ game.room = "map"
    return

label amy_kink_04:
    scene expression f"bg {game.room}"
    "I've been looking forward to meeting up with Amy all day."
    "In fact you could probably say it's what's been keeping me going."
    "It's been one of those tough ones, the kind you want to forget."
    "And the promise of spending time on a date with her is just what I need."
    play sound cell_vibrate loop
    "So when my phone rings and I see the call is from Amy, I pick up straight away."
    $ result = renpy.call_screen("smartphone_choice", "Amy")
    if not result:
        stop sound
        $ hero.cancel_event()
        $ hero.cancel_activity()
        $ game.active_date.abort = True
        "Or not. I remember that I have something more important to do right now."
        "Amy will understand if I don't come to our date after all."
        $ amy.love -= 5
        return
    stop sound
    scene expression f"bg {game.room}" at dark with dissolve
    mike.say "Hey, Amy!"
    mike.say "I'm just about ready, okay?"
    mike.say "I should be over in about..."
    amy.say "Urgh..."
    amy.say "Argh..."
    amy.say "ACHOO!" with vpunch
    "The sounds coming from the other end of the phone are unexpected in the extreme."
    "So much so that I have to hold it away from my ear until they finally subside."
    "Once they do, I gingerly put the phone back to where I can hear the call again."
    mike.say "Erm..."
    mike.say "Amy?"
    mike.say "Are you okay?"
    "There's a sound like a blocked sink sucking down air."
    "And then I hear something that could pass for actual words."
    amy.say "Urgh..."
    amy.say "No, [hero.name]..."
    amy.say "I'm...pretty far...from okay!"
    "I don't need to be told twice that Amy's not well."
    "And I don't think she could fake she sounds she's making either."
    mike.say "Ah..."
    mike.say "That really suck, Amy."
    mike.say "I guess we're going to have to take a rain check on our date?"
    "Amy makes a rather unpleasant slurping noise."
    "Then she manages to answer me."
    amy.say "Arrgh..."
    amy.say "I'm sorry..."
    amy.say "I must've caught a bug at work, or something."
    mike.say "Don't worry, Amy."
    mike.say "We can make plans once you're better."
    amy.say "Sure we will..."
    amy.say "Thanks for understanding, [hero.name]."
    menu:
        "Give me a few minutes, I'll come by your place":
            "I'm all ready to wrap the call up and say goodbye to Amy."
            "But then the image of her sitting there all alone pops into my head."
            "And I remember that, as we'd set time aside for the date, I'm not doing anything right now."
            mike.say "Wait a minute, Amy..."
            mike.say "How about I come over there and help you out?"
            amy.say "Oh..."
            amy.say "You don't have to do that, [hero.name]!"
            amy.say "I can take care of myself."
            mike.say "It's no problem, really."
            mike.say "I can be over there in the blink of an eye."
            "Amy goes quiet on the other end of the line."
            "And for a moment I think that she's going to turn me down."
            amy.say "Well...if you really want to..."
            amy.say "I guess it'd be nice to have some company."
            mike.say "Okay, that's settled then."
            mike.say "I'll be there as soon as I can."
            scene expression f"bg {game.room}" with dissolve
            "I end the call and head straight home."
            scene bg house with fade
            pause 0.5
            scene bg livingroom with fade
            "Then I rush to the kitchen."
            scene bg kitchen with fade
            "I grab what I think I'll need from the cupboards."
            "And I hurry straight out of the door."
            scene bg street with fade
            "Once I get to Amy's apartment I think about knocking quietly, as she's ill."
            "But then I realise that's about as much use as a chocolate kettle."
            "So I rap on the door loudly enough to ensure that I'm heard."
            "Then I wait patiently until Amy manages to make it to the door."
            scene bg amyhome
            show amy casual sad blush
            with fade
            "As it swings open and I see her standing there, it's clear she wasn't putting it on."
            "Amy looks pale, even for a goth."
            "And her eyes are rimmed with red that can't be dramatic make-up."
            "The rest of her is hidden under a duvet that's wrapped around her body."
            amy.say "Hey, [hero.name]..."
            amy.say "Thanks again for..."
            show amy surprised at center, vshake
            amy.say "ACHOO!"
            show amy sad
            amy.say "For coming over!"
            "I just about manage to jump out of the way of Amy's sneeze."
            "And then I step inside, making sure to stay out of range of any more."
            mike.say "No worries, Amy."
            mike.say "I brought you some soup and other stuff."
            mike.say "Go make yourself comfortable and I'll warm it up."
            hide amy
            "Amy nods and then staggers off in the general direction of the sitting room."
            "While I head to the kitchen and get to work on the soup."
            "As soon as it's warm, I search out a bowl and pour the soup into it."
            scene bg amyhome at center, zoomAt (2.5, (840, 1320))
            show amy casual sad blush at center, zoomAt (1.5, (640, 1100))
            with fade
            "Then I carry it through to where Amy's huddled on the sofa."
            "Sitting down by her side, I hand over the soup."
            "She takes it eagerly, drinking it straight from the bowl."
            show amy at center, zoomAt (1.65, (640, 1140))
            "And without asking, she leans herself against me too."
            show amy pain
            amy.say "Mmm..."
            amy.say "Thanks, [hero.name]."
            amy.say "I'm feeling too rotten to even be able to make soup for myself!"
            show amy sad
            amy.say "Urgh..."
            if game.hour >= 20:
                amy.say "And to think, we were supposed to be on a date tonight!"
            else:
                amy.say "And to think, we were supposed to be on a date today!"
            mike.say "It's okay, Amy..."
            mike.say "We can make up for it as soon as you're well."
            "Amy lets out a tired sigh as she finishes her soup."
            show amy at center, zoomAt (1.75, (640, 1180))
            "And as she hands me back the bowl, she snuggles herself even closer."
            show amy sadsmile
            amy.say "Hey, [hero.name]..."
            amy.say "Did anyone ever tell you that you're the best?"
            mike.say "No, Amy..."
            mike.say "Not that I recall."
            amy.say "Well they should..."
            $ amy.love += 2
            amy.say "Because that's exactly what you are!"
            "I feel a surge of happiness as Amy says this to me."
            scene bg amyhome with fade
            "More affection and warmth towards her than I was ready for."
            "And I wait eagerly to hear what she's going to say next."
            "But instead I only hear the gentle sound of her snoring on my shoulder."
            "With all the gentleness and care that I'm capable of, I scoop Amy up in my arms."
            "And then I carry her through to the bedroom, placing her on the mattress."
            "I make sure to put the covers over her and tuck her in."
            "Then I let myself out of the apartment and make my way back home."
            scene bg street at blur(16), dark with dissolve
            if game.hour > 18:
                "Sure, I missed out on a date tonight."
            else:
                "Sure, I missed out on a date today."
            "But I feel like I managed to do a good deed instead."
            "And that's got to count for something, right?"
            $ game.room = "street"
            if amy.sub.max < 80:
                $ amy.sub.max = 80
            $ amy.flags.amydelay = TemporaryFlag(True, 2)
        "You better take care of yourself":
            mike.say "No worries, Amy."
            mike.say "You look after yourself, okay?"
            amy.say "I will!"
            amy.say "Talk to you later."
            scene expression f"bg {game.room}" with dissolve
            "As Amy ends the call, it occurs to me that I could have offered to go over there."
            "But then I remind myself that she's a pretty independent kind of girl."
            "Plus going over to her apartment would be a sure way of catching whatever she has too."
            "And I can't afford to be spending time off work recovering from a bug."
            "So I probably made the right decision there."
            $ amy.flags.amydelay = TemporaryFlag(True, 3)
    $ hero.cancel_activity()
    $ game.active_date.abort = True
    scene bg black with dissolve
    return

label amy_kink_05:
    show amy shy blush
    "Amy gives me one of those odd, sideways looks."
    "You know the kind I'm talking about, right?"
    "The ones that let you know a girl has something on her mind."
    "So I decide that the best thing is to call her bluff."
    mike.say "Okay, Amy..."
    mike.say "What is it?"
    mike.say "What's on your mind?"
    show amy surprised
    amy.say "Huh?"
    amy.say "What are you talking about?"
    mike.say "Come on, Amy..."
    mike.say "I can tell from the way you keep looking at me."
    mike.say "You've got something to say."
    mike.say "You're just waiting for the right moment to say it."
    show amy upset
    "Amy opens her mouth to speak."
    "And for a moment it looks like she's going to keep on denying it."
    show amy shy at startle
    "But then she lets out a sigh and shakes her head."
    amy.say "Okay, [hero.name], you got me."
    amy.say "But hear me out on this one, okay?"
    "I nod, prompting Amy to go ahead and say her piece."
    show amy normal -blush
    amy.say "I know that modern guys are supposed to be all sensitive and understanding."
    amy.say "But I really like it when you assert yourself and take control, you know?"
    show amy flirt
    amy.say "I mean...it kinda gives me a thrill."
    amy.say "And it makes me want to fall in line too!"
    "I blink in surprise and amazement at what Amy saying."
    "What she's confessing, actually."
    "And here I was, afraid of doing anything of the kind."
    "Because I thought she'd cut me off at the kneecaps for it!"
    mike.say "You're serious, Amy?"
    mike.say "You really like that kind of thing?"
    show amy shy blush
    "I can see that Amy's cheeks are flushing with colour."
    "And she's finding it hard to look me in the eye right now."
    amy.say "I...I mean a little..."
    amy.say "Like, I don't want you to treat me that way in public."
    amy.say "Or make me act like a slave or anything!"
    show amy puzzled
    amy.say "But...maybe we could do it in private?"
    amy.say "You be a bit more assertive and me be a bit more submissive?"
    menu:
        "I'll be the iron fist and you the velvet glove!":
            "I almost have to pinch myself as I listen to Amy's request."
            "Because I honestly can't believe what I'm hearing."
            "Is she actually asking me for permission to become a sub?"
            "To become MY sub?!?"
            mike.say "Of course we can, Amy!"
            mike.say "I've always wanted to try that kind of thing."
            mike.say "And I think you'd be perfect in that position."
            show amy happy
            if amy.sub.max < 100:
                $ amy.sub.max = 100
            $ amy.sub += 5
            "Amy's face lights up as she hears my answer."
            "I can practically see the delight sparkling in her eyes."
            amy.say "You do?"
            amy.say "That's great!"
            amy.say "We should start as soon as we can."
            show amy flirt
            amy.say "The very next time we're alone together, yeah?"
            mike.say "Sure thing, Amy."
            mike.say "We'll take it slow at first."
            mike.say "But I'm sure it'll work out well."
            show amy happy at center, zoomAt(1.5, (640, 1040)) with hpunch
            "Amy grabs hold of my arm and presses herself against me."
            amy.say "Ooh!"
            amy.say "This is going to be so much fun!"
        "No... I just can't":
            "I don't have to think long about my answer."
            "Because I know the way I feel about this in my gut."
            mike.say "No, Amy..."
            mike.say "I don't think I'd be very comfortable with that idea."
            show amy surprised -blush
            amy.say "What?"
            amy.say "Are you sure about that?"
            show amy worried
            amy.say "We...we could start out really slowly..."
            amy.say "Just kinda feel it out, yeah?"
            "I shake my head at this."
            "Trying as best I can to show Amy that I'm serious."
            mike.say "I mean it, Amy."
            mike.say "If I was being assertive in the past..."
            mike.say "Well...that was because I thought the situation called for it."
            mike.say "Not because I was trying to dominate you for a thrill."
            show amy sad
            $ amy.sub -= 10
            "Amy looks down at her feet."
            "And I can see that her mouth is set in a hard line."
            amy.say "You're sure about that?"
            amy.say "Really sure?"
            mike.say "Yeah, Amy, I am."
            mike.say "It's not something that I'm into."
            mike.say "And I don't like the idea of doing it to you just for a turn-on."
            show amy pain
            "Amy nods, but she doesn't say anything more."
            "Which I guess means that she wants to let the matter drop."
            "Sure, it's more than a little awkward."
            "But I really think it's for the best."
            "I just have to hope that she'll be able to get over it in time."
    return

label amy_male_ending:

    if renpy.has_label("amy_achievement_3") and not game.flags.cheat:
        call amy_achievement_3 from _call_amy_achievement_3
    $ game.hour = 16
    $ game.room = "church"

    if "amy_kink_05" in DONE and amy.sub >= 100:
        scene bg church wedding with fade
        "I know that it's kind of a cliché for girls to spend a lot of time imagining their wedding day."
        "But I'm not sure that Amy ever imagined that it would be happening like this when she did so."
        "For the most part, the chapel looks pretty much how you'd expect it to for any wedding."
        "The place is done up nicely, and the pews on either side of the aisle are filled with guests."
        "One side boasts all of my friends and family, looking happy and dressed up for the occasion."
        "The other is, of course, populated by all of the important people in Amy's life."
        "And yeah, a lot of them are goths, resplendent in their black finery and heavy makeup."
        "But aside from that, this looks like any normal wedding that you might have walked into."
        "Though all of that changes when the music begins to play, filling the chapel with sound."
        "There's a murmur of interest from the guests, and all heads turn to look backwards."
        "From where I'm standing at the altar, I have a better view than almost anyone."
        "Which means that I'm the first to see the doors open and Amy step into the chapel."
        "We made a point of warning the guests that this wasn't going to be a totally ordinary affair."
        show amy b wedding blush at center, zoomAt (1.0, (640, 720)) with dissolve
        "But even so, when people begin to see what Amy has on, there are still gasps of surprise."
        "And that's because my bride sweeps into the chapel and down the aisle totally in black."
        "But unlike most of the other goths in attendance, she's wearing black leather and rubber!"
        "Plus none of the others are wearing anything quite so revealing as Amy's wedding dress."
        "Of course I've seen the dress before, which is my right as her master and husband to be."
        "Yet the sight of it on her and in motion is still enough to take my breath away for a moment too."
        "The dress manages to make Amy look beautiful and elegant in the extreme."
        "And somehow also shows off every inch of her body in the most sexual manner possible."
        "Which is only appropriate, as she's giving herself to me as a more than willing thrall."
        "A slave, if you want to use such a crude term to describe her relationship to me."
        "Though she's putting herself in that position totally on account of her own free will."
        "As ironic as that might sound to someone on the outside and looking in!"
        "I have to suppress a smile as Amy gets closer to the altar."
        show amy b wedding at center, traveling (1.5, 5.0, (640, 1040))
        "Because even before she's halfway there I can hear the sound her dress is making."
        "The thing is so tight that the rubber is already squeaking as she walks!"
        "But none of that really matters."
        "Just as the stares and gasps from the guests don't matter either."
        "When Amy finally makes it to my side at the altar, she's the centre of my attention."
        "I don't even say a word, just stand there staring at her, trying to take it all in."
        "And I can see from the look on her face that she appreciates my attention and admiration."
        "Priest" "Ahem..."
        show wedding amy priest with fade
        "The sound of the priest coughing snaps us both back to reality."
        "And for all of my apparent defiance, I make a real effort to show that I'm on the same page."
        "Because I know full-well that we're pushing the limits of what we can get away with here today."
        "And the guy's being more than accommodating when it comes to the eccentricities of our ceremony."
        "I see that Amy's doing the same thing, making sure to appease the priest."
        "But then that might just be her following my lead."
        "As she's totally devoted to her role as my willing slave these days."
        "Priest" "Now that I have your undivided attention..."
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To bind this woman to this man..."
        "Priest" "As his willing and eager sexual slave."
        "Of course that gets a genuine ripple of surprise and amazement from the guests."
        "But then we were expecting that it would, as we wanted to be totally upfront about all of this."
        "Amy and I just take it in our stride, letting the sounds of surprise wash over us."
        "Yet for all of that, the actual ceremony is pretty familiar."
        "The priest goes through the motions, talking about all the usual stuff."
        "Things only get a little more spicy when we get to the actual vows."
        "Priest" "Do you, Amy..."
        "Priest" "Vow to give yourself wholly to [hero.name], body, mind and soul?"
        "Priest" "To be his slave and obey his will in all things?"
        "Amy totally ignores the gasps from the guests as the priest says all of this."
        "And she nods eagerly in response too."
        amy.say "I do."
        "Priest" "Very good..."
        "Priest" "And do you, [hero.name]…"
        "Priest" "Take Amy to be your obedient and eternal slave?"
        "Priest" "Will you lead, dominate and protect her?"
        mike.say "I will."
        "The priest nods."
        "Priest" "At this point it would be customary to ask for any objections to the union."
        "Priest" "But on this occasion I am asked to solicit any challenges from those here present?"
        "Priest" "So does anyone want to challenge for ownership of Amy?"
        "Where there would normally have been laughter, there's only a stunned silence."
        "Which the priest seems more than happy to take as there being no challenges."
        "Priest" "What a relief!"
        "Priest" "I have to confess that I'm not sure how I would have handled that one!"
        "This at least does get a ripple of nervous laughter."
        "As everyone seems to share the priest's sense of awkwardness."
        "Priest" "Moving swiftly on..."
        "Priest" "It is therefore my pleasure to pronounce you..."
        "Priest" "Erm..."
        "Priest" "Master and slave..."
        "Priest" "I suppose you may do with her as you wish!"
        show wedding amy -priest with dissolve
        "I can hardly hear what the priest is saying as I stare at Amy."
        "We finally did it, we got married on our own terms!"
        "She's now officially mine, and I can do with her as I like."
        "And hopefully as she likes too."
        "I wrap my arms around Amy and pull her close to me."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show amy kiss wedding
        with fade
        $ amy.flags.kiss += 1
        "The sound of her dress creaking and squeaking fills my ears."
        "But I'm too busy planting a huge kiss on her lips to even notice."
        "I want to start our married life in the way we mean to go on."
        "Bold, unafraid and making a show of our love in whatever way we see fit."

        scene bg black
        show amy kneeling
        with fade
        amy.say "Okay, okay...just give me a minute to get myself ready, okay?"
        amy.say "I've totally devoted myself to living my life as [hero.name]'s slave, remember?"
        amy.say "So I'm not used to being asked to speak for myself anymore."
        amy.say "And I'm kind of out of practice!"
        amy.say "Right, here goes..."
        amy.say "It's getting harder to remember what life was like before [hero.name] came along."
        amy.say "That might sound like the kind of thing all the girls say, but for me it's true."
        amy.say "And that's because I never really felt like I knew who I was before we got together."
        amy.say "Sure, I was always totally dedicated to the goth lifestyle and all the trappings."
        amy.say "But it always felt like there was something missing in my life, you know?"
        amy.say "I was constantly trying to find stuff to fill that gap too."
        amy.say "I tried music, books, movies and even thought about taking up acting."
        amy.say "And the flip-side of that was me always ending up in dead-end jobs that I hated."
        amy.say "Yeah, yeah...that's exactly how I landed the job at the electronics store."
        amy.say "I saw the ad online and I fired off my resume without even thinking about it."
        amy.say "I was so used to either hearing nothing back or landing a job I knew I'd hate."
        amy.say "So when the offer of an interview came back, I just strolled on down there as usual."
        amy.say "It was only when I saw Shawn waiting to meet me that I knew something was up."
        amy.say "Trust me, I know that look when a guy gives me it."
        amy.say "I just knew that he'd seen the picture attached to my resume and liked it."
        amy.say "The trouble was that I couldn't say the same thing about him."
        amy.say "Sure, Shawn could be a nice guy, and he tried hard to be nice to me."
        amy.say "Well, at least he did to begin with!"
        amy.say "But I was just taking the job for the sake of the money, and I couldn't hide that."
        amy.say "The only thing in the shop that really interested me was the electric guitars we sold."
        amy.say "And it didn't take long for Shawn to realise I liked the instruments more than him."
        amy.say "I've got to give him credit though, he did his best to turn on the charm."
        amy.say "The only problem was that I'd already decided it wasn't going to work on me."
        amy.say "So his efforts only grated on my nerves, making the whole situation worse."
        amy.say "I honestly thought that I was going to have to quit before too long."
        amy.say "And I was all ready to tell Shawn to shove the job up his ass."
        amy.say "But that was around the time that [hero.name] walked into the store."
        amy.say "Look, even though I'm now officially his slave, I'm not going to sugar-coat it."
        amy.say "My first impression was that a cute guy had walked into the store."
        amy.say "And then I saw that he was one of Shawn's friends."
        amy.say "So I was all set to find out he was just as big of a jerk."
        amy.say "But that didn't happen, and instead I found that he was pretty funny."
        amy.say "Plus we seemed to have a lot in common, hitting it off right from the start."
        amy.say "Shawn screwed up too, when he made it obvious he was totally jealous of [hero.name] too."
        amy.say "Because that only made me all the more interested in this guy."
        amy.say "He's cute, he seems to get me, and us even talking pushed my boss' buttons!"
        amy.say "To be honest, I'd have dated [hero.name] just to spite Shawn."
        amy.say "But luckily for us both, there was more to it than that."
        amy.say "Pretty soon we found that we were getting closer every time we were together."
        amy.say "Hanging out turned into going for drinks, and that became dates."
        amy.say "[hero.name] started to make me feel so comfortable that I dropped my guard with him."
        amy.say "And then I started to realise that I was being myself around him more than anyone else."
        amy.say "So much so that some people might not have recognised the real me that he brought out!"
        amy.say "Oh, and then there was the sex..."
        amy.say "Let's just say that it was the same thing there, only turned up to eleven!"
        amy.say "[hero.name] made me feel so good in that department that I was desperate for more."
        amy.say "And that's where the realisation started to dawn on me about what I really wanted."
        amy.say "I was having so much fun with him in the bedroom that I needed to know it would last."
        amy.say "This wasn't just about wanting [hero.name] to commit to our relationship."
        amy.say "It was a deep and very real need to know that he would keep it up between the sheets."
        amy.say "I'd never realised that I had this need growing inside of me before."
        amy.say "But now I wanted nothing more than the security of knowing that I'd get more."
        amy.say "So that's why I had to reveal my inner desires to him."
        amy.say "I needed to see if he would fulfil my needs in the way I wanted."
        amy.say "If he would allow me to give myself to him so totally as to make it a certain thing."
        amy.say "I don't know if anyone waiting to propose marriage ever felt that nervous."
        amy.say "But I found the courage and I went through with it."
        amy.say "I'm just thankful that he said yes, that he agreed to accept me as his slave."
        amy.say "That was the point in my life when everything seemed to start falling into place."
        amy.say "The thing that made me sure I was finally discovering the person I was always supposed to be."
        amy.say "And since then, we've never looked back."
        amy.say "[hero.name]'s career really took off once he had me to come home to every night."
        amy.say "I took it as my solemn duty to see that he was refreshed by the next morning."
        amy.say "So I would, and still do, make every effort to meet his manly needs."
        amy.say "And you know what, I found a purpose in that like never before."
        amy.say "It was like I finally knew who I was and what I wanted to do with my life."
        amy.say "And since then we've never looked back."
        amy.say "[hero.name] goes out every morning, and comes back every evening."
        amy.say "It's my job to be ready for him when he walks in through that door."
        amy.say "I do whatever he asks of me, without question."
        amy.say "And I do it well."
        amy.say "But my ultimate goal is to anticipate his needs before he tells them to me."
        amy.say "Even before he knows what they are himself."
        amy.say "And when I can do that without pause or hesitation, then I'll know I've achieved perfection."
        amy.say "Because my entire being will have become devoted to servicing him and making him happy."
        amy.say "Which will, in turn, make me happy too."
        amy.say "So wish me luck in my quest."
        amy.say "Because I won't give up until I make it a reality."
        scene bg black with dissolve
        pause 0.5
    else:
        scene bg church wedding with fade
        "I keep fidgeting and playing around with the collar of my suit, yanking at my tie."
        "Which is crazy, because I was fitted out for the damn thing when I hired it."
        "But deep down, I know it's the nerves that are really what's getting to me."
        "No matter how hard I try, there's no way I can calm myself down or chill out."
        "I give in to temptation and take another glance back over my shoulder."
        "And when I do, I see what I've seen all the times I already did so."
        "I see a chapel decorated for a wedding and pews full of guests waiting quietly."
        "Of course I recognise more faces on my side of the chapel than I do on Amy's."
        "But what I'm trying to see is where Shawn ended up choosing to sit."
        "While we were planning the wedding, Amy and I had a little disagreement."
        "And that lead to a bet between the two of us."
        "She was certain that, as my friend, Shawn would sit on my side of the chapel."
        "But I wasn't so sure, knowing how he was always falling for the girls in his life."
        "And how he also kind of had a thing for Amy before we got together."
        "So I bet her that Shawn would sit on her side of the chapel instead."
        "I'm still trying to spot him amongst the other guests when the sound of music fills the air."
        "As one, the guests all rise and turn to look towards the doors at the back of the chapel."
        "I do the same, hardly noticing that I've actually been holding my breath."
        show amy b wedding blush at center, zoomAt (1.0, (640, 720)) with dissolve
        "But when the doors open and Amy walks in, I let it out in a sudden gasp of pure amazement."
        "I'd begged her to let me see what the dress looked like before the wedding."
        "And every time I did, Amy told me to get lost, that I'd have to wait like everyone else."
        "But now that I'm seeing her in it for the first time, I'm glad that she did."
        "Because it was one hundred percent worth the wait!"
        show amy b wedding at center, traveling (1.5, 5.0, (640, 1040))
        "Amy sweeps into the chapel and down the aisle, looking like I've never seen her before."
        "Somehow she's managed to find a wedding dress that makes her look like an angel."
        "Yet it also manages to stay faithful to the goth image that's so much a part of her."
        "And as Amy gets closer to the altar, she only seems to look better."
        "I can't seem to take my eyes off her the whole time."
        "And I must have a huge smile plastered on my face too."
        "Because I swear I can feel my jaw starting to ache."
        "Amy comes to a halt by my side at the altar."
        "And we spend the next few moments grinning at each other like total fools."
        show amy b flirt
        amy.say "Well..."
        amy.say "What do you think?"
        show amy b happy -blush
        amy.say "Aren't you going to say something?"
        show amy normal
        mike.say "Oh..."
        mike.say "Oh yeah..."
        show wedding amy with fade
        mike.say "You look great, Amy - totally amazing!"
        "Priest" "Ahem..."
        show wedding amy priest with dissolve
        "As one, Amy and I snap to attention at the sound of the priest's voice."
        "Priest" "Shall we begin?"
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To join these two people in the bonds of matrimony..."
        "You know how the rest of it goes."
        "The priest runs through the usual lines and questions."
        "And all of it seems to run together in a blur for me."
        "I only seem to come back to reality when I feel Amy elbow me in the ribs."
        "Priest" "Do you, Amy..."
        "Priest" "Take this man to be your lawful, wedded husband?"
        amy.say "I do!"
        "Priest" "And do you, [hero.name]..."
        "Priest" "Take this woman to be your lawful, wedded wife?"
        mike.say "You bet I do!"
        "The priest raises an eyebrow at my enthusiastic response."
        "But he presses on with the ceremony all the same."
        "Priest" "It now falls upon me to call on all those here present..."
        "Priest" "If you know of any reason these two may not be joined together..."
        "Priest" "Speak now, or forever hold your peace!"
        "There's the almost traditional pause and ripple of laughter amongst the guests."
        "But all the time I'm just hoping that Shawn doesn't take this chance to be a dick."
        "I'm sure that he wouldn't really mean it, but he does have a weird sense of humour."
        "Would he stand up and say something as a joke?"
        "Priest" "Very well..."
        "I realise that I've been holding my breath the whole time."
        "And now I let it out as a deep sigh of relief."
        "Priest" "I therefore declare you to be husband and wife."
        "Priest" "You may kiss the bride - if you'd like?"
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show amy kiss wedding
        with fade
        "Amy and I don't need to be given an invitation to do that."
        "We're already throwing our arms around each other as the priest says all of this."
        "And the kiss we exchange is probably a little longer and more intense than it should be."
        "But that's because it's one of relief and genuine love."
        "Amy and I travelled down a pretty twisting road to get here."
        "And now we're at the end of the journey, we're going to celebrate."
        scene amy ending with fade
        amy.say "So this is the bit where I'm supposed to tell my side of the story, right?"
        amy.say "[hero.name] get's to talk about all the fun, juicy bits along the way."
        amy.say "Then I come in at the end and say how great it was being along for the ride?"
        amy.say "Nah...it's okay, it's okay."
        amy.say "I'm just messing with you."
        amy.say "You want me to tell them all about what it's like being with [hero.name]..."
        amy.say "Then I will gladly do so!"
        amy.say "So...you might remember that I had a habit of dumping people and then running away."
        amy.say "And what do you know, that's how I ended up living here."
        amy.say "I stepped off a train with only what I could carry, intending to start over again."
        amy.say "And I took the first job that I could in order to pay the bills."
        amy.say "But they fired me."
        amy.say "So I took a second job."
        amy.say "And the business closed down."
        amy.say "Then I took a third job."
        amy.say "And they fired on the same day the business closed down."
        amy.say "But the fourth job, that was the one in the electronics store."
        amy.say "And I managed to keep that one."
        amy.say "Sure, Shawn was a prick almost from the word go."
        amy.say "It was pretty clear that he was into me too."
        amy.say "But I get the feeling he was into any woman that would come within ten feet of him."
        amy.say "I was seriously thinking of telling him to shove it after only a couple of days."
        amy.say "Like kicking him in the balls before he got round to firing my ass."
        amy.say "But then one day I see this guy strolling into the store."
        amy.say "And he's pretty hot, you know?"
        amy.say "Then I see him talking to Shawn, and I figure they're friends."
        amy.say "Which means that he's probably as big of a jerk as Shawn himself, right?"
        amy.say "But I decide to give him a chance, and it turns out I was wrong."
        amy.say "[hero.name]'s not like Shawn at all."
        amy.say "In fact he's pretty cool, and we have a lot in common too."
        amy.say "So far so good - we start to hang out, then it turns into a couple of dates."
        amy.say "We do the horizontal tango too, and it's getting even better!"
        amy.say "But then, true to form, I start to get that nagging sense of doubt."
        amy.say "Things are going too well, and that just can't last."
        amy.say "Sooner or later I'm going to end up falling for him."
        amy.say "And then I'm going to get hurt!"
        amy.say "So I did what I always used to do."
        amy.say "I called him up and told him it was over, that I was leaving."
        amy.say "And what did he do?"
        amy.say "He rushed over to the station and begged me not to go."
        amy.say "Now that I look back on it, I guess part of me wanted that."
        amy.say "I mean, I could have sent him a message once I was gone."
        amy.say "But I gave him the time to come find me before it was too late."
        amy.say "I think that was about the time I realised that he was different."
        amy.say "I never did that before, I always just left."
        amy.say "And as time passed, I got proven right."
        amy.say "Because together we talked it through and put it behind us."
        amy.say "So when he proposed, I jumped on the chance to make it official."
        amy.say "And I've never looked back since then."
        amy.say "[hero.name]'s flying high in his career."
        amy.say "Though I'm still not sure what he actually does for a living!"
        amy.say "But we're talking about the future and what we want out of life."
        amy.say "And the more we do, the more we both keep mentioning starting a family."
        amy.say "So I don't think it'll be long until we hear the pattering of little feet around here."
        amy.say "And as for me, well..."
        amy.say "It turns out that I'm a hell of a lot better at running an electronics store than I thought."
        amy.say "A little time after [hero.name] and I got married, Shawn ended up in big trouble at work."
        amy.say "He was accused of harassing more than one female customer on the premises."
        amy.say "Head office ended up getting involved, and they launched an investigation."
        amy.say "And they found a witness willing to give them all the dirt on Shawn they needed."
        amy.say "I have no idea who that could have been..."
        amy.say "But it lead to Shawn getting demoted to junior assistant shelf-stacker."
        amy.say "And as I was the next most experienced member of staff, I got a promotion."
        amy.say "So now I'm the boss at the electronics store."
        amy.say "And when I say jump, Shawn asks me how high!"
        amy.say "So yeah..."
        amy.say "Life's turned out pretty good for me so far."
        amy.say "And I'm looking forward to seeing what the future brings."
        amy.say "Who knows, I might even get the urge to reunite with the girls in the band..."
        amy.say "But my first loyalty is always going to be to [hero.name]."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not amy.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_21
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_21
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label amy_birthday_date_male:
    $ DONE["amy_birthday_date_male"] = game.days_played
    # === CEMETERY EVENT REMOVED ============================================
    #  The original birthday date took Amy to the CEMETERY and led into the
    #  cemetery grave-sex scene (amy_birthday_sex_male). Both are removed.
    #  This is a short, generic NON-cemetery birthday date, kept because the
    #  date system calls <char>_birthday_date_male dynamically (the label must
    #  exist or Amy's birthday date crashes). It still marks DONE so the
    #  "birthday_date" quest step and gallery flag complete as before.
    $ game.active_date.clothes = "casual"
    scene bg mall1 with fade
    show amy happy with dissolve
    "Amy's already waiting for me when I arrive, and her whole face lights up the moment she sees me."
    amy.say "[hero.name]! You actually remembered!"
    mike.say "Of course I did, Amy. Happy birthday!"
    "She loops her arm through mine and we spend the evening just wandering and talking."
    "No graveyards, no weirdness - just the two of us, enjoying her birthday together."
    $ amy.love += 3
    $ game.active_date.score += 60
    show amy normal
    amy.say "Thanks for tonight, [hero.name]. Honestly? It was perfect."
    mike.say "Anything for the birthday girl."
    "Eventually it gets late, and I walk her most of the way home before we say goodnight."
    hide amy
    return


label amy_birthday_sex_male:
    # === CEMETERY EVENT REMOVED ===  the cemetery grave-sex scene is deleted.
    #  Harmless stub kept so any stray reference still resolves.
    return
