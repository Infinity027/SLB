init python:
    Event(**{
    "name": "lavish_start",
    "label": "lavish_start",
    "conditions": [
        IsDone("office_party"),
        HeroTarget(IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(aletta,
            HasRoomTag("work"),
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lavish_event_02",
    "label": "lavish_event_02",
    "conditions": [
        IsDone("lavish_start"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 2),
            ),
        ],
    "music": "music/johny_grimes/nostalgia.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lavish_event_03",
    "label": "lavish_event_03",
    "conditions": [
        IsDone("lavish_event_02"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 4),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_04",
    "label": "lavish_event_04",
    "conditions": [
        IsDone("lavish_event_03"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 7),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_05",
    "label": "lavish_event_05",
    "conditions": [
        IsDone("lavish_event_04"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            IsFlag("projectDelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_06",
    "label": "lavish_event_06",
    "conditions": [
        IsDone("lavish_event_05"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 14),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_07",
    "label": "lavish_event_07",
    "conditions": [
        IsDone("lavish_event_06"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            IsFlag("projectDelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    InteractEvent(**{
    "name": "lavish_event_08",
    "label": "lavish_event_08",
    "conditions": [
        IsDone("lavish_event_07"),
        HeroTarget(HasRoomTag("pub"),),
        PersonTarget(lavish,
            IsActive(),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_09",
    "label": "lavish_event_09",
    "conditions": [
        IsDone("lavish_event_08"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 21),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_10",
    "label": "lavish_event_10",
    "conditions": [
        IsDone("lavish_event_09"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 28),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_11",
    "label": "lavish_event_11",
    "conditions": [
        IsDone("lavish_event_10"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            IsRoom("office"),
            MinCounter("daysemployed", 30),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_12",
    "label": "lavish_event_12",
    "conditions": [
        IsDone("lavish_event_11"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            MinCounter("daysemployed", 35)
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            IsRoom("alettaoffice")
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    InteractEvent(**{
    "name": "lavish_event_13",
    "label": "lavish_event_13",
    "conditions": [
        IsDone("lavish_event_12"),
        PersonTarget(lavish,
            IsActive(),
            MinFlag("promoted", 1),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_14",
    "label": "lavish_event_14",
    "conditions": [
        IsDone("lavish_event_13"),
        HeroTarget(IsActivity("work_personal", "workhard_personal")),
        PersonTarget(lavish,
            HasRoomTag("work"),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_15",
    "label": "lavish_event_15",
    "conditions": [
        IsDone("lavish_event_14"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(lavish,
            OnDate(),
            MinStat("love", 150),
            ),
        ],
    "priority": 1000,
    "music": "music/johny_grimes/nostalgia.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lavish_event_16",
    "label": "lavish_event_16",
    "duration": 1,
    "conditions": [
        IsDone("lavish_event_15"),
        HeroTarget(IsRoom("alettaoffice")),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            HasRoomTag("work"),
            MinStat("love", 160),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_17",
    "label": "lavish_event_17",
    "conditions": [
        IsDone("lavish_event_16"),
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            HasRoomTag("work"),
            IsFlag("lavfleemeetingdelay", False),
            ),
        ],
    "do_once": True,
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_event_18",
    "label": "lavish_event_18",
    "conditions": [
        IsDone("lavish_event_17"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 180),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "do_once":True,
    })

    Event(**{
    "name": "lavish_investigation_callback",
    "label": "lavish_investigation_callback",
    "conditions": [
        IsNotDone("cassidy_investigation_complete"),
        IsHour(15, 21),
        PersonTarget(lavish,
            Not(IsPresent()),
            MinCounter("investigationcallback", 2),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lavish_kiss_me",
    "label": "lavish_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(lavish,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/johny_grimes/nostalgia.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "lavish_preg_talk",
    "label": "lavish_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(lavish,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/johny_grimes/nostalgia.ogg",
    })

    Event(**{
    "name": "lavish_office_bj",
    "label": "lavish_office_bj",
    "priority": 200,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice")),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 100),
            MinStat("sub", 50),
            ),
        "not Room.find(game.room).get_present_girls()",
        ],
    "music": "music/johny_grimes/nostalgia.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "lavish_spanking_alternate_start",
    "label": "lavish_spanking_alternate_start",
    "priority": 200,
    "conditions": [
        IsDone("shiori_scold_5", "audrey_spanking_start"),
        IsNotDone("lavish_spanking_start"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(lavish,
            HasRoomTag("work"),
            MinStat("love", 100),
            MinStat("sub", 40),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lavish_spanking_1",
    "label": "lavish_spanking_1",
    "priority": 200,
    "conditions": [
        IsDone("lavish_spanking_start"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(lavish,
            HasRoomTag("work"),
            IsFlag("spankingdelay", False),
            MinStat("love", 110),
            MinStat("sub", 60),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lavish_spanking_2",
    "label": "lavish_spanking_2",
    "priority": 200,
    "conditions": [
        Or(
            IsDone("lavish_spanking_1"),
            IsDone("lavish_spanking_alternate_start"),
            ),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(lavish,
            HasRoomTag("work"),
            IsFlag("spankingdelay", False),
            IsFlag("start_spanking", True),
            MinFlag("spank_counter", 3),
            MinStat("love", 130),
            MinStat("sub", 70),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "lavish_sub_03",
    "label": "lavish_sub_03",
    "conditions": [
        TogetherInHarem('office', 'audrey', 'lavish', 'shiori'),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(lavish,
            HasRoomTag("work"),
            IsFlag("sexywork"),
            MinFlag("spank_counter", 3),
            MinStat("love", 160),
            MinStat("sub", 80),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })


label lavish_kiss_me:
    call lavish_greet from _call_lavish_greet
    show lavish
    "She can be so quiet and shy, that sometimes I forget Lavish is even there by my side."
    "I wonder if that's one of the reasons that she so often leans in to steal a long, tender kiss from me?"
    "It's like a gentle and totally welcome reminder, not only of her existence, but also of how much I love to feel her close at hand."
    "So much of her is like a whisper, something that's easy to miss when you're not aware of it..."
    "But impossible to forget the very moment that you realise it exists."
    hide lavish
    show lavish kiss
    $ lavish.flags.kiss += 1
    "Her kiss is equally slow and deliberate, making me savour every single moment."
    "The only thing more delicate are the sighs that she lets out at the same time."
    hide lavish kiss
    return

label lavish_start:
    $ lavish.flags.mikeNickname = "hero.family_name"
    $ lavish.unhide()
    $ lavish.set_counter("daysemployed")
    play sound door_knock
    show aletta work
    "There's a knock that breaks me from my concentration, and I'm happy to tear my eyes off my blinding white computer screen for a moment to glance over to Aletta behind me."
    aletta.say "Hey."
    "I roll myself back in my seat a bit, stretching my arms and arching my back as I turn my chair away from my desk to face her."
    mike.say "What's up?"
    aletta.say "I wanted to introduce you to the new intern."
    "I stifle a sigh, forcing a thin smile instead."
    "Great. Another intern around the office to be bombarding me and everyone in earshot with stupid questions, and mucking things up that, eventually, will get back around to me to fix."
    "The last kid that interned here, I was about ready to push out the window by the time he was heading back to classes and leaving us for good."
    "But, I mean, I should have known better, at this point."
    show aletta work at right with move
    show lavish work at left with moveinleft
    "Of course the face that stares back at me when Aletta steps aside is a stunning, doe-eyed young woman that immediately makes my heart skip a beat."
    aletta.say "This is Lavish, you already met her at the party. She's going to be around the office for now, and I told her she could come to you if she needed help."
    "Lavish gives me a soft, demure smile that's sophisticated and classic in its beauty."
    lavish.say "It's nice to meet you."
    aletta.say "Lavish, this is your manager."
    "I get out of my seat quickly, eager to step forward and extend my hand to her."
    "Her fingers are baby soft, warm, and delicate when she extends her hand to shake mine. I find myself wishing I didn't have to let go, savoring the feeling of it there, small, in my palm."
    "Something about the soft, pretty curve to her face makes me want to spin her around by that hand, pull her in, and dance with her."
    "A whiff of something drifts to me -- some kind of deep, spicy perfume that almost entices me in closer to her. Almost."
    "My boss is watching, after all."
    "Maybe some other time."
    show aletta annoyed
    "Aletta folds her arms across her chest, and I realize that maybe I have been shaking the intern's hand for a moment too long, quickly letting it go and stepping back."
    "Lavish doesn't seem to mind. She's got her gaze fixed on me, the smile curling at her lips remaining."
    "In those deep, dark eyes, I could almost swear I see stars."
    "Why's she looking at me like that?"
    show aletta normal
    aletta.say "I trust you're going to take care of her."
    show aletta at right4 with move
    "Aletta says strictly, stepping forward and ushering Lavish a step backwards with a gentle, maternal hand on the arm. She shoots me a sharp glance from behind her glasses."
    aletta.say "No distractions."
    "I flash a grin."
    mike.say "What, me?"
    aletta.say "Hmm."
    show aletta at center
    show lavish at top_mostleft
    with move
    "The two of them turn from me and head back into the heart of the office, though I could swear Lavish lingers just a split second longer than she needed to, glancing once more back over her shoulder at me."
    hide aletta
    hide lavish
    with moveoutleft
    "I almost expect her to tip me a seductive wink when she does. But she turns back around, collected, and follows Aletta away, the two of them speaking something to each other that I can no longer hear."
    "Nice."
    "Can't complain at all about seeing a goddess like that around the office."
    "There's a stupid smile on my face when I turn back to my computer, breathing an airy sigh and flopping myself back into my seat."
    "No distractions, Aletta said. But how am I supposed to focus on work, now?"
    return

label lavish_event_02:
    "I roll myself back from my computer desk, leaning back into my seat and pinching the bridge of my nose."
    "I need to find a file for the project I'm working on, but it's not scanned. Of course it's not."
    "The office is so behind on that, even though they were supposed to hire temp workers to get it done months ago."
    "A brilliant idea strikes me, and my eyes light back up as I lean myself forward, snatching my phone from its cradle."
    "Who needs temp workers when you've got that new, sexy intern, anyway?"
    play sound phone_calling
    "I punch in the extension to her desk, and to my disappointment it rings... and rings... and goes to her voicemail."
    stop sound
    "As soothing and sensual as her voice is on the prerecorded message, it's not what I wanted to hear."
    "I frown as I set my phone back down and push myself to my feet."
    "Fine. Do some legwork myself."
    "The file room isn't far from my desk, anyway, and I turn the corner and push open the heavy door, slipping inside and letting it click closed behind me."
    show bg office with fade
    show lavish files at bottom_to_top
    "I realize right away that I'm not in here alone. I can hear shuffling and the rattling metal sound of drawers being pulled open that probably drowned out the sound of my arrival."
    "Just to make sure I don't give some middle-aged lady a heart attack, I make my way over to the rows of cabinets that the sounds came from, raising a fist to knock on one and announce my presence."
    "But I freeze."
    "Lavish didn't answer my call because she's already here."
    "A pair of long, silky-smooth legs greets my vision, rubbing together with an innocent sensuality as she shifts her weight, focused on digging through the folders."
    "Her ass is plump and rounded beautifully by the heels she's got on today, and though she's a few feet down the aisle it's so prominently in my face it feels like I could take a bite from where I stand."
    "Her stockings cling desperately to the meat of her thighs, pinching the flesh in at the elastics with an alluring sheen under the fluorescent lights."
    "I can see a set of puffy lips between her thighs, clearly visible from beneath her skirt, the panties she's wearing so thin they're nearly sheer, and I just about lose it."
    "Ideas of making my way over to her and taking her, right there in that position, flood my mind so suddenly I feel like I could drown in them."
    "I quickly adjust myself through my pocket and clear my throat to dismiss the thoughts before this gets out of hand."
    hide lavish files
    show lavish surprised
    "Lavish jumps a little bit at the sound, straightening herself quickly and looking back at me."
    lavish.say "Oh."
    show lavish normal
    "She sighs the word, as if in relief."
    lavish.say "It's only you."
    mike.say "'Only' me?"
    show lavish blush
    "I'm teasing her, but a faint blush scatters attractively across her cheeks anyway."
    lavish.say "Did you need something?"
    mike.say "Actually, yeah. I came here to look for the Reynholm files."
    lavish.say "Oh. I could have grabbed those for you."
    mike.say "I called your desk, actually, but I must've just missed you."
    lavish.say "My apologies."
    "I don't know if I'm imagining it, but her voice seems to have softened and deepened a bit, like the voice a woman uses in the bedroom."
    "I can almost feel my heartbeat quicken in response, trained like Pavlov's dogs."
    show lavish wink
    lavish.say "Let me get that for you now."
    show lavish files at bottom_to_top
    "If she was bent over that way out of innocence the first time, I'm hard-pressed to believe she is now."
    "Clutching the files she's already holding to her breasts, she bends over again, slow, and reaches down to the very bottom drawer, pulling it out and flicking her fingertips along the papers inside."
    "I'm not interested in the drawer at all. My gaze stays fixed on the show she's obviously putting on for me."
    "This time when she shifts her weight, making the muscles in her ass and thighs flex and her thighs glide together in her stockings, it's a much more exaggerated motion, and I pulse appreciatively in response, keeping one hand tactfully in my pocket."
    "But this is work, and I can't make assumptions. Maybe she's just one of those office teases. I have to get to know her, first."
    "If she wants it, she can absolutely get it."
    lavish.say "Got it."
    hide lavish files
    show lavish normal
    "She straightens herself again, and just like that, the show's over."
    "Holding the file I was looking for in her free hand, she makes her way over to me, setting it down gently into mine."
    mike.say "Thanks."
    "I clear my throat again, to make sure I don't sound as breathless as the throbbing tension in this isolated room is making me feel."
    mike.say "I appreciate the help."
    show lavish happy
    lavish.say "My pleasure."
    "I'm sure I'm not imagining it now that she practically purrs the words."
    show lavish normal blush
    lavish.say "Please don't hesitate to give me a call if you ever need anything at all."
    menu:
        "Say nothing":
            $ lavish.love += 1
            pass
        "Oh, I'll call!":
            mike.say "Oh, you can bet I'll call! I'm sure I've got lots of things...you can do to me. I mean for me."
            $ lavish.sub += 1
            $ lavish.flags.sleaze += 1
    show lavish at left4 with move
    "She slips past me, and I catch a whiff of that perfume again."
    show lavish at left with move
    "I know I'm never going to be able to smell it in any mall or on any stranger ever again without remembering this moment."
    hide lavish with moveoutleft
    "I hear the door click shut behind me and exhale a whooshing sigh, waiting for the tension in me to go down, too, before I go back to my desk."
    "Back to work."
    return

label lavish_event_03:
    "Most of my job is about servicing and maintaining clients. Fixing stuff when it breaks, creating new ways to do things they need, and making sure the rest of the company can do their jobs."
    "But ever since I got promoted to management, some of my job is about managing my employees. It's weird, in that I don't really think of myself as a boss."
    "But here I am."
    "And today, I need to have our first one on one with Lavish and find out how her first few days are going."
    "Plus, this gives me an opportunity to see if she was flirting with me or not."
    show lavish
    lavish.say "Hello, [hero.name]."
    menu:
        "Call me [heroname]":
            mike.say "Oh, please, we don't need to be so formal. Call me [heroname]!"
            $ lavish.flags.mikeNickname = "heroname"
            $ lavish.love += 2
            lavish.say "Sure thing, [hero.name]!"
        "Let her stay formal":
            $ lavish.sub += 2
            pass
    mike.say "Thanks for coming. So we're supposed to meet regularly to talk about how things are going for you, if there's anything you need from me, and if I can help make sure you can get your job done."
    lavish.say "Well, most of my job has just been busywork, so far."
    "She sounds kind of disappointed about that."
    mike.say "Ah yeah. Interns do get to start at the bottom."
    menu:
        "Throw in an innuendo":
            mike.say "I mean, some girls like to be on the bottom, right?"
            $ lavish.sub += 1
            $ lavish.flags.sleaze += 1
            show lavish blush
            lavish.say "I've always aimed to be on top, [hero.name]."
            mike.say "Well, the bottom is where you start."
            show lavish normal
        "Keep it clean":
            $ lavish.love += 1
    lavish.say "I understand, but I am working on an advanced degree. If this job is going to get me real experience, I should be doing real work."
    mike.say "All in good time, Lavish. I'll tell you what, though. I'll look through my projects and see if there's anything I can give to you."
    $ lavish.career += 5
    show lavish happy
    lavish.say "Thank you, [hero.name]!"
    hide lavish with moveoutleft
    "Well, that was disappointing. I'm supposed to trust an intern with important work, and I didn't get any sense of if she's flirting or not."
    return

label lavish_event_04:
    $ lavish.flags.projectDelay = TemporaryFlag(True, 2)
    "Sometimes, no matter how hard I work, it seems like the stack of things to do just gets higher and higher."
    "And the deadlines get shorter and shorter. And once you start missing deadlines, there's blowback."
    "Today is one of those days. There's so much to do, and I just don't have enough time to do it all."
    "As I look through the pile, I start to wonder if I can pass some of this off to the new intern. She did ask for more real work after all."
    "But she's new, and young, and I don't know how capable she'll be. I really hate to find out on something important."
    "On the other hand, I {b}will{/b} miss deadlines if I don't. So I look through my pile of work, and decide that there are two projects I could give her."
    "The Van Buren project is easier, it's some straight forward report building. It's tedious and will take a lot of time, but doesn't require a lot of skill. But it's important."
    "That client is unhappy, and if this is messed up it could cost the company a lot of money."
    "The Whitehall project is a lot harder. It requires more skill and knowledge and some actual design work. But there will be fewer issues if she messes it up."
    menu:
        "Give her the easier but more important project":
            $ lavish.flags.currentproject = "Van Buren"
        "Give her the harder but less important project":
            $ lavish.flags.currentproject = "Whitehall"
        "Don't give her a project":
            "I decide I can do the work on my own. I'll get it done, though I might wish I would die."
            return
    if lavish.love.max < 30:
        $ lavish.love.max = 30
    $ lavish.love += 1
    show lavish at left with easeinleft
    lavish.say "You wanted to see me, [hero.name]?"
    mike.say "Yes I did. Remember how you were saying you would like something more interesting to work on? Well, I have a project for you!"
    show lavish at center with ease
    "I hand her the stack of folders."
    mike.say "I'll need this stuff done by the day after tomorrow. I won't be able to give you much guidance, as unfortunately I also have a huge pile of work to do."
    show lavish happy
    lavish.say "I won't let you down, [hero.name]!"
    mike.say "I hope not, Lavish! This could be very important to your future here!"
    lavish.say "Thank you! I'll get to work on this right away!"
    hide lavish with easeoutleft
    "Getting to watch her walk out is a nice distraction from the work ahead of me. But alas, now I need to get back to it."
    return

label lavish_event_05:
    show lavish
    if lavish.flags.currentproject == 'Van Buren':
        lavish.say "Hi, [hero.name]! I've completed the Van Buren project, like you asked."
        mike.say "How did it go?"
        lavish.say "It was a lot of the same thing over and over, and making sure all the numbers were right."
        "I take a look through her work. It's very good, actually, but I did expect it to be easy."
        $ lavish.career += 5
        menu:
            "Compliment her":
                mike.say "Great job on this, Lavish! Much better than I expected from a very new intern."
                $ lavish.love += 3
                lavish.say "Thank you, [hero.name]!"
            "Play it cool":
                mike.say "Thanks for taking care of this."
                lavish.say "Any time, [hero.name]!"
            "Make an innuendo out of it":
                mike.say "This work looks even better than you do!"
                $ lavish.sub += 3
                $ lavish.flags.sleaze += 1
                show lavish embarrassed blush
                "Lavish stammers a reply, not able to make coherent words. I'd better cover myself."
                mike.say "Sorry, I mean this is a fantastic job."
                show lavish normal
                lavish.say "Thanks, I guess?"
        mike.say "This kind of work isn't glamorous or exciting, but it can pay well, I guess."
    elif lavish.flags.currentproject == 'Whitehall':
        lavish.say "Hi, [hero.name]! I've completed the Whitehall project, like you asked."
        mike.say "How did it go?"
        lavish.say "It was...really hard. I stayed up all night, though, and did a bunch of extra work. I ran into some problems that took a long time to fix, but I solved them. I hope it's okay?"
        "I take a look through her work. It's very good. She got a few things wrong that I'll have to correct before I send this on, but overall she just saved me a solid day's worth of work."
        $ lavish.career += 10
        menu:
            "I'm impressed!":
                mike.say "Great job on this, Lavish! This is absolutely fantastic, Whitehall will be very pleased."
                $ lavish.love += 5
                lavish.say "Thank you, [hero.name]!"
            "Play it cool":
                mike.say "Thanks for taking care of this."
                lavish.say "Any time, [hero.name]!"
            "Make an innuendo out of it":
                mike.say "For work this good, I think I owe you a drink!"
                $ lavish.sub += 3
                $ lavish.flags.sleaze += 1
                show lavish embarrassed blush
                lavish.say "A drink? Like at a bar? Would that be...appropriate?"
                mike.say "I don't know if it's appropriate, but you deserve a reward. You saved me a bunch of work."
                show lavish normal
                lavish.say "Oh, uh. Okay, sure!"
        mike.say "I'm sorry you stayed up all night on this, though. You don't need to work quite so hard."
    else:
        lavish.say "Hi, [hero.name]. Got a sec?"
        mike.say "Sure, what can I do for you?"
        lavish.say "So, you know how you said you'd find some actual, real work for me to do? Have you found anything yet?"
        "Oh shit. I didn't give her any of those projects. Maybe I should have. It's too late now, I guess."
        mike.say "I'm sorry, I haven't really had a chance. I've been very busy."
        lavish.say "So I've seen."
        "She takes a step toward me, and I swear her next words are purred like a kitten."
        lavish.say "I'd be very...very grateful if you did."
        mike.say "How..."
        "Wow, that word came out a little more high pitched than I meant."
        mike.say "I mean. How grateful?"
        show lavish wink
        lavish.say "Well. I'd certainly owe you a really, really big favor."
        "She's got to be flirting with me, right?"
        $ lavish.flags.promisedFavor = True
        menu:
            "Like a kiss?":
                "No guts, no glory, right?"
                mike.say "Like a kiss?"
                show lavish embarrassed blush
                $ lavish.flags.sleaze += 1
                $ lavish.sub += 3
                lavish.say "Oh, um. I, um. That's not...I mean, is that...what you want?"
                mike.say "Oh, no, I was just trying to figure out what it is you were actually trying to say."
            "I'll keep that in mind!":
                "Better safe than sorry when it comes to getting hit with a sexual harassment lawsuit."
                mike.say "I'll keep that in mind, Lavish. I promise I'll find you something appropriate."
                $ lavish.love += 3
        show lavish normal
        lavish.say "I'm sorry if it seems like I'm badgering you, [hero.name], I just want to get the most out of my experience here."
        mike.say "You do seem extremely ambitious. This isn't exactly glamorous work!"
    hide lavish
    show lavish normal
    lavish.say "It's what I've always wanted to do."
    mike.say "Huh. I'm not sure I've ever heard anyone say that before."
    "Lavish smiles."
    lavish.say "Ambition runs in my family, I guess."
    mike.say "Oh?"
    lavish.say "Yeah, my father used to be the mayor."
    mike.say "You mean the guy they used to call Iron Bill? That's your father?"
    show lavish annoyed
    "Lavish grimaces a little."
    lavish.say "Yeah. That's him."
    mike.say "Wow, he was mayor for twelve years or something, wasn't he?"
    show lavish normal
    lavish.say "Until he couldn't run again because of term limits."
    mike.say "What's he doing now?"
    show lavish angry
    lavish.say "Trying to position himself to run for Governor or something. Look, can we talk about something else? He's not why I'm here."
    mike.say "Oh. Sorry. Is it a sore spot?"
    show lavish normal
    lavish.say "Not exactly, it's just...look, I'd really prefer not to talk about it, okay?"
    mike.say "Okay."
    lavish.say "Do you have another project for me?"
    mike.say "Not at the moment, but I'll look and see, okay?"
    lavish.say "Thanks, [hero.name]!"
    hide lavish with easeoutleft
    "Lavish hurries toward the door, obviously a bit worked up over that conversation. I had no idea her family was so important, and that's definitely something to keep in mind for the future."
    if lavish.love.max < 40:
        $ lavish.love.max = 40
    hide lavish
    return

label lavish_event_06:
    if lavish.love.max < 60:
        $ lavish.love.max = 60
    if lavish.flags.promisedFavor:
        "I've been thinking about how Lavish promised me a big favor if I could give mer something interesting to work on."
        "And I think I've found just the thing."
    else:
        "I've been thinking about the surprisingly good job Lavish did the last time I gave her a project."
        "And I think I've found the next thing for her."
    show lavish
    mike.say "Hi, Lavish. I think I've found something to work on. It won't be fun, but I think it's the kind of experience you're looking for."
    $ lavish.love += 1
    lavish.say "[hero.name], that's great! What do you have for me?"
    "I spend the next few minutes explaining the project to her. It's complicated, and...I don't want to underestimate her, but I'm not sure she'll be up to the task. I guess we'll see, right?"
    "For her part, she asks the right questions and seems to pick up what I'm telling her quickly. That's a good sign."
    show lavish close
    "At the end, and very much to my surprise, she throws her arms around me and gives me a great big hug!"
    "I can feel her breasts squeezing against me, and the smell of her perfume. Maybe she means it or maybe she doesn't, but this is a hell of a turn-on."
    menu:
        "Hug her back":
            "Not knowing quite what to do, I go ahead and return the hug, carefully."
            $ lavish.love += 5
            hide lavish
            show lavish normal blush
            "After a moment she lets go, and the moment is gone."
        "Grab her ass":
            "I can't help myself. It seems like she's been flirting with me non-stop. So whatever, right?"
            "I reach down and put my hand on her ass. I don't squeeze or anything, I just want to see what she'll do."
            "Her reaction is to stiffen. She takes a deep breath and holds it. But that's it. No other reaction."
            hide lavish
            show lavish normal blush
            $ lavish.sub += 2
            $ lavish.flags.sleaze += 1
    show lavish at left4 with ease
    "When it's all over, she heads for the door."
    show lavish at left with ease
    lavish.say "I'll get to work on this right away, [hero.name]! I'll let you know my progress."
    $ lavish.flags.projectDelay = TemporaryFlag(True, 7)
    hide lavish with easeoutleft
    return

label lavish_event_07:
    if lavish.love.max < 80:
        $ lavish.love.max = 80
    show lavish at left with easeinleft
    lavish.say "Hi, [hero.name]! I finished that project you gave me! I hope I did okay. You were right, some of it was really hard."
    mike.say "Oh! Give me a few minutes to look it over."
    show lavish at center with ease
    "When I read through the results of her work, it's clear to me that she's a novice. But a talented novice. It's going to require some touch ups but that's to be expected."
    menu:
        "Great work!":
            mike.say "This is really great work, Lavish! I'm completely impressed!"
            $ lavish.love += 2
            $ lavish.career += 10
            lavish.say "Thanks, [hero.name]! Anything I can do to help!"
        "Not bad":
            mike.say "This is not bad, Lavish. It needs some clean up, though."
            lavish.say "Oh, I'm sorry. I'll do better next time!"
            mike.say "Well, this is how you learn, right?"
            $ lavish.sub += 2
            $ lavish.career += 10
        "You deserve a naughty reward":
            mike.say "Stellar work, Lavish. I could kiss you for such good work."
            show lavish blush
            mike.say "Oh! I mean, not like that."
            lavish.say "Oh, um, it's okay."
            $ lavish.flags.sleaze += 1
            $ lavish.career += 5
            menu:
                "Let it go":
                    pass
                "Unless you want me to":
                    mike.say "Unless you want me to mean it that way!"
                    $ lavish.flags.sleaze += 2
                    show lavish embarrassed
                    "Lavish stammers as she blushes furiously."
                    lavish.say "I, no, I mean um. I mean. [hero.name]!"
                    "She looks away from me, and I laugh to ease the tension."
                    mike.say "Relax, Lavish. I'm just teasing. This is really great work!"
                    lavish.say "Thanks!"
                    show lavish normal
    mike.say "I'll have something else for you in a few days, okay?"
    lavish.say "Oh sure. So...busy work until then?"
    mike.say "I'm afraid so. It's part of the job."
    if lavish.flags.sleaze > 3:
        show lavish at left with ease
        "As she walks out, I swear she emphasizes the swaying of her butt just a little more than usual."
    else:
        show lavish at left with ease
        "I admire Lavish's fine butt as she exits and closes the door behind her."
    hide lavish with easeoutleft
    return

label lavish_event_08:
    if lavish.love.max < 100:
        $ lavish.love.max = 100
    show lavish
    lavish.say "Fancy meeting you here, [hero.name]!"
    $ lavish.flags.informalheroname = hero.name
    if lavish.flags.mikeNickname == "hero.family_name":
        menu:
            "I like it when you call me that outside work":
                mike.say "I like the way it sounds when you call me that outside work, Lavish!"
                show lavish blush
                $ lavish.flags.sleaze += 1
                $ lavish.sub += 2
                $ lavish.flags.informalheroname = lavish.heroname
                lavish.say "Well it is what I'm supposed to call you!"
            "Call me [hero.name]":
                mike.say "No need to be so formal, Lavish. You can call me [hero.name]."
                lavish.say "Oh, okay. In general or just outside of work?"
                menu:
                    "In general":
                        mike.say "In general. I think we're friends, right?"
                        $ lavish.flags.mikeNickname = "heroname"
                        $ lavish.flags.informalheroname = heroname
                        $ lavish.love += 2
                        lavish.say "That's sweet of you to say!"
                    "Outside of work":
                        mike.say "I guess you should still be formal in the office. For appearance's sake."
                        $ lavish.sub += 2
                        $ lavish.flags.informalheroname = heroname
                        lavish.say "Of course!"
            "Just say hi":
                mike.say "Hi Lavish! Nice to see you!"
                $ lavish.flags.informalheroname = lavish.heroname
    menu:
        "Compliment her looks":
            mike.say "It's refreshing to see you outside of office attire. You look stunning, by the way!"
            show lavish blush
            lavish.say "Oh, you flatter me, [lavish.flags.informalheroname]!"
            $ lavish.love += 1
            $ lavish.flags.sleaze += 1
        "Compliment her work":
            mike.say "I don't know if I've said this enough, but you've been doing great work at the office."
            lavish.say "Oh, you flatter me, [lavish.flags.informalheroname]!"
            $ lavish.love += 1
    lavish.say "Say, [lavish.flags.informalheroname], would you like to have a drink?"
    mike.say "Sure! It'd be great to get to know you a bit."
    show date pub burger lavish
    lavish.say "I just want to thank you for the opportunity at work, [lavish.flags.informalheroname]! It really means a lot to me."
    mike.say "Hey, I'm glad to help. My job is to make sure you can succeed at your job, right?"
    lavish.say "Well, you're doing a very good job at your job, I must say."
    if lavish.flags.sleaze >= 5:
        "She leans toward me, just a little bit, and I swear she's being suggestive. It's all I can do not to ask her if she wants to go home with me right now."
    else:
        "Lavish offers me a sweet smile, and in that moment, she seems so innocent and naive."
    mike.say "I don't mean to pry, but you do seem unusually driven, and it sounded like there was something with your family?"
    lavish.say "Oh, yeah. My dad...has high expectations. I haven't met, basically any of them."
    mike.say "What? You've got a great internship and good career ahead of you. You're clearly going to climb the ladder, if not here, wherever you go next. How could you possibly not be meeting his expectations?"
    lavish.say "Well, the family business is politics. And I just don't want to do that."
    mike.say "Oh."
    lavish.say "My job is to be the good little daughter, and give smiles to the cameras, and occasionally say something witty when a reporter is nearby, but mostly to stay quiet."
    lavish.say "And if I work really, really hard at that, maybe in ten or twenty years, I can run for office too."
    lavish.say "And...I don't know. Maybe in twenty years I'll want that. But right now, I just want to be my own person."
    mike.say "Oh, yeah, I get it."
    "It's a bit hard for me to sympathize. Her family can get her anything she wants. I really could've used that, once upon a time."
    lavish.say "Does that sound...shallow?"
    mike.say "Oh! Oh no, not at all. It's just...my family was nobody special, so it's hard for me to relate, you know?"
    lavish.say "I guess? I'm sorry, it's hard for me to imagine other families. I know, that makes me a terrible person."
    "I see I should change the subject."
    mike.say "Hey, don't be hard on yourself. You are your own person, and you're a gorgeous, sexy, capable person at that."
    "She offers me an enigmatic smile."
    lavish.say "And I'll do anything I have to, to get what I want!"
    if lavish.flags.sleaze >= 5:
        "Then she looks right at my crotch and then back up at my eyes."
        lavish.say "If you know what I mean. And it gets me what I want."
        "Oh. Holy shit!"
        mike.say "I do know what you mean!"
    lavish.say "But that's for another time! Thanks for the drink, [lavish.flags.informalheroname]!"
    return

label lavish_event_09:
    $ renpy.dynamic("asksex")
    if lavish.love.max < 120:
        $ lavish.love.max = 120
    play sound door_knock
    "There's a knock on my door. After I shout to come in, Lavish opens the door just a little and looks in."
    show lavish at top_mostleft with easeinleft
    lavish.say "Hi, [hero.name], got a sec?"
    menu:
        "Of course":
            mike.say "Of course."
            show lavish at center with ease
            "Lavish steps all the way into the office and closes the door behind her."
        "Anything for you, Sweetheart":
            $ lavish.love += 2 if lavish.love > 70 else -2
            $ lavish.sub += 1
            $ lavish.flags.sleaze += 1
            pause 1
            show lavish at center with ease
            "Lavish hesitates for a moment, then steps all the way into the office and closes the door behind her."
    lavish.say "Can I ask you a serious question?"
    "At that, I realize that she needs my full attention. So I close my laptop to make sure I'm not distracted."
    mike.say "Sure thing, Lavish. What can I do for you?"
    lavish.say "Do you think I'm qualified for this work?"
    "Oh wow. Putting me on the spot."
    menu:
        "Absolutely" if lavish.career >= 20:
            mike.say "There's no question. You've already proven yourself capable."
            $ lavish.love += 5
        "You could be" if lavish.career >= 10:
            mike.say "I think if you work at it, you could be qualified. You're still pretty new, but I think you can grow into it."
            $ lavish.sub += 2
        "I don't know" if lavish.career >= 5:
            mike.say "I honestly don't know, Lavish. You haven't been here long enough for me to figure that out."
            $ lavish.love -= 5
        "No":
            mike.say "No, you're not. You should be in some other line of work."
            $ lavish.love -= 10
    mike.say "Why do you ask?"
    lavish.say "Well, I saw a job posting in this office for a position. I thought I might apply for it, if you think I can do it."
    mike.say "Oh. Wow, that's awfully soon, isn't it? You've only been here a short time."
    lavish.say "You don't get what you don't reach for, my dad always said."
    mike.say "True that."
    lavish.say "Will you help me get the job?"
    mike.say "What's the job?"
    "Lavish hands me a sheet of paper with the job posting on it. It's...my old job before the promotion."
    "That feels weird. Should I tell her to apply?"
    menu:
        "Yes":
            mike.say "Sure, you can apply. I can't make any promises."
            lavish.say "But you'll put in a good word for me?"
            mike.say "Yeah, I can do that."
            $ lavish.love += 2
        "No":
            mike.say "I don't think that's a good idea."
            lavish.say "Oh. I took this internship because I saw it as a good way to advance my career. I guess that was a mistake."
            mike.say "What are you saying?"
            lavish.say "If this job doesn't get me what I want, I'll go somewhere else."
            mike.say "And you want a promotion, already?"
            if lavish.career > 20:
                lavish.say "I've already earned it with the projects I've done for you, I think."
            else:
                lavish.say "I'm the hardest worker you have."
            mike.say "That's just a reason why I wouldn't want to lose you."
    if lavish.flags.sleaze >= 10:
        lavish.say "I'll...make it worth your while."
        mike.say "What do you mean?"
        show lavish wink
        lavish.say "I've seen the way you watch me walk. I know what you want."
        mike.say "Oh really?"
        show lavish normal blush close
        "She walks up to me and puts her hands on the desk, leaning forward and giving me a fabulous view down her shirt."
        lavish.say "Get me this job, and I'll give you whatever you want."
        $ asksex = False
    else:
        lavish.say "I need this. I need you to make this happen. I'll do whatever you want."
        $ asksex = True
    menu:
        "I will help":
            mike.say "Okay, Lavish. I get you. I'll do what I can, okay?"
            show lavish happy
            "Lavish offers me a big, beautiful smile."
            lavish.say "Thank you so much, [hero.name]!"
        "I will not help":
            mike.say "No, I can't do that. I'm sorry."
            lavish.say "Fine. I quit. I'll find some place who appreciates me."
            $ lavish.set_gone_forever()
        "Whatever I want? Like...sex?" if asksex:
            $ lavish.flags.sleaze = max(lavish.flags.sleaze + 2, 20)
            mike.say "So wait, are you offering to have sex with me if I get you this job?"
            show lavish embarrassed
            lavish.say "I...I mean, I'm not a whore, [hero.name]."
            mike.say "I wouldn't use that word."
            show lavish flirt
            lavish.say "But if that's...that's what you want, I will."
            mike.say "I'll see what I can do."
            $ lavish.flags.owessex = True
        "I'll help but you'd better pay up" if not asksex:
            $ lavish.flags.sleaze += 10
            mike.say "You're right, I'd love to have sex with you. I'll do everything I can to get you this job."
            lavish.say "I'd better get the job, or you get nothing. Okay?"
            mike.say "How can I refuse?"
            show lavish wink
            lavish.say "Good man."
    hide lavish with moveoutleft
    return

label lavish_event_10:
    show lavish with easeinleft
    lavish.say "Hi, [hero.name], I need your help."
    mike.say "Is that so?"
    lavish.say "I've applied for that job, and I've got to do a screening. It has a lot of technical questions. I found an online service that helps with some sample tests and...I'm not quite passing. I think I'm close. I need you to help me make sure I pass."
    mike.say "Right now? It's the middle of the day. I'm working."
    show lavish annoyed
    lavish.say "My screening is tomorrow!"
    mike.say "I thought you were the one who was sure she was qualified?"
    show lavish normal
    if lavish.flags.owessex:
        lavish.say "And you're the one who's going to get a very nice reward."
        lavish.say "If you want that reward, you'd better help!"
    else:
        lavish.say "I am! I just need a little guidance!"

    menu:
        "I'll help":
            mike.say "Okay, I will help you."
            "I spend the next couple of hours going over some of the sample quizzes with her, and pointing out the tricks in the questions. Almost everything she has wrong is simply due to a lack of experience."
            $ lavish.career += 15
            $ lavish.love += 5
            $ hero.cancel_activity()
            $ game.pass_time(4)
        "I can't":
            mike.say "I'm sorry, I really have to get this work done. I can't help you."
            show lavish angry
            lavish.say "Well, thanks for nothing then, {b}[hero.name]{/b}!"
            $ lavish.love -= 10
            $ lavish.flags.didnothelp = True
        "I'll help...for a kiss" if lavish.flags.owessex:
            "Lavish purses her lips, but then she smiles."
            lavish.say "Of course, I think a little...down payment on our arrangement makes sense."
            show lavish kiss work
            $ lavish.flags.kiss += 1
            "Lavish approaches and wraps her arms around me, pressing her entire body up against mine."
            "I would have thought she wouldn't be into it, given the reason we're kissing, but she absolutely is."
            "I can feel her nipples hard against my chest, even as her tongue darts in and out of my mouth, pressing against my own."
            "And all too soon, it's over."
            show lavish flirt
            lavish.say "There, that ought to be enough to...motivate you, right?"
            mike.say "Ah, uh, um. Yes, yes it will."
            show lavish wink
            lavish.say "And don't think this means you get any elsewhere."
            show lavish normal
            "I spend the next couple of hours going over some of the sample quizzes with her, and pointing out the tricks in the questions. Almost everything she has wrong is simply due to a lack of experience."
            $ lavish.career += 10
            $ hero.cancel_activity()
            $ lavish.sub += 2
            $ lavish.flags.sleaze += 5
            $ lavish.flags.kissed = True
            $ game.pass_time(4)
    hide lavish
    return

label lavish_event_11:
    show lavish happy with easeinleft
    "Lavish bursts into my office without even knocking. Good thing I was alone...you never know what I could've been up to in here."
    lavish.say "I passed their screening! They scheduled an interview!"
    mike.say "That's great, Lavish!"
    if lavish.flags.didnothelp:
        show lavish angry
        lavish.say "And no thanks to you!"
        mike.say "I knew you had it in you."
    show lavish normal
    lavish.say "So, do you know anything about how the interview will work?"
    mike.say "Well, I guess you'll talk to Aletta, for sure. Normally me too, but there's not much point in that since you already work for me. They'll ask me what I think."
    mike.say "There's probably a couple other people around the office you'll talk to. I guess some people in other groups, to try and get a less biased opinion of you."
    lavish.say "Help me pass the interview!"
    mike.say "I'm not sure how to do that. I've already talked you through the quizzes."
    lavish.say "I'm sure you can think of something."
    mike.say "All right, I guess I can give you a mock interview, and give you pointers in how to answer? I don't know if it will help, but it might."
    lavish.say "That sounds great. Please?"
    mike.say "Right now?"
    lavish.say "No time like the present, or so they say."
    menu:
        "Fine":
            "I spend the next several hours running through different interview scenarios, thinking about every way I can ask her questions and trip her up."
            "She does pretty well."
            $ lavish.career += 15
            $ hero.cancel_activity()
            $ lavish.love += 5
        "I can't":
            mike.say "I'm sorry, Lavish. I can't now."
            show lavish angry
            play sound door_slam
            "Lavish storms out, slamming the door behind her."
            $ lavish.love -= 10
        "For another kiss" if lavish.flags.kissed:
            mike.say "For another kiss, sure!"
            show lavish kiss work
            $ lavish.flags.kiss += 1
            "Lavish doesn't hesitate, stepping up and embracing me. This time it's longer, and more sensuous."
            "Her lips press against mine, and she squeezes my neck so hard it almost starts to hurt. But it's worth it, so very worth it."
            show lavish
            "And then it's over, and I have to concentrate on giving her a mock interview. It takes some effort to clear my head, but for Lavish it seems like she switched on a dime."
            "I spend the next several hours running through different interview scenarios, thinking about every way I can ask her questions and trip her up."
            "She does pretty well."
            $ lavish.career += 10
            $ hero.cancel_activity()
            $ lavish.sub += 2
            $ lavish.flags.sleaze += 5
        "For a kiss..." if not lavish.flags.kissed:
            "Lavish purses her lips, but then she smiles."
            lavish.say "Of course, I think a little...down payment on our arrangement makes sense."
            show lavish kiss work
            $ lavish.flags.kiss += 1
            "Lavish approaches and wraps her arms around me, pressing her entire body up against mine."
            "I would have thought she wouldn't be into it, given the reason we're kissing, but she absolutely is."
            "I can feel her nipples hard against my chest, even as her tongue darts in and out of my mouth, pressing against my own."
            "And all too soon, it's over."
            show lavish flirt
            lavish.say "There, that ought to be enough to...motivate you, right?"
            mike.say "Ah, uh, um. Yes, yes it will."
            show lavish wink
            lavish.say "And don't think this means you get any elsewhere."
            show lavish normal
            "And then I have to concentrate on giving her a mock interview. It takes some effort to clear my head, but for Lavish it seems like she switched on a dime."
            "I spend the next several hours running through different interview scenarios, thinking about every way I can ask her questions and trip her up."
            "She does pretty well."
            $ lavish.career += 10
            $ hero.cancel_activity()
            $ lavish.sub += 2
            $ lavish.flags.kissed = True
    hide lavish
    return

label lavish_event_12:
    $ renpy.dynamic("convinced")
    $ convinced = 0
    show aletta with easeinleft
    aletta.say "Hi, [hero.name]! I suppose you know already about Lavish's application for your old job?"
    mike.say "I do, indeed."
    aletta.say "Well, she's finished with all her interviews, and I wanted to talk to you about her. How's she done?"
    menu:
        "Fantastic" if lavish.career >= 50 or lavish.flags.sleaze > 20:
            mike.say "She's amazing, Aletta! She's the best intern I've ever had."
            if lavish.career < 50:
                aletta.say "Really? She did pretty well, but best you've ever had? Interesting."
            else:
                aletta.say "That matches what the other interviewers said, too."
            $ convinced += 10
        "She's okay, I guess":
            if Person.is_not_hidden("shiori"):
                mike.say "Well, she's sharper than Shiori, I guess, but that's not saying much."
            else:
                mike.say "Well, she's really sharp."
            $ convinced += 2
        "I wouldn't hire her":
            mike.say "I think maybe someday she'll do well, but she's still too new. She's not ready."
            if lavish.career >= 40:
                aletta.say "Are you just saying that because you want to keep her as your employee?"
                menu:
                    "No!":
                        mike.say "No! It's not that at all, I just don't think she's ready. She's moving very aggressively."
                    "Yes":
                        if lavish.flags.sleaze > 20:
                            mike.say "Well. Okay yes, I guess I do want to keep her...under me."
                            $ convinced += 10
                        else:
                            mike.say "Well. Okay yes, I guess I do want to keep her around."
            else:
                aletta.say "I see."

    if lavish.career + convinced >= 50:
        aletta.say "Okay. You should know I've decided to hire her. But there's a catch."
        mike.say "I don't like the sound of that."
        aletta.say "I'm shifting the position to report to you, not me. I don't really want another report. I promoted you to handle people like her so I don't have to."
        mike.say "Oh. So I guess nothing changes?"
        aletta.say "Sure it changes. You have to give her the same kind of work you used to have. Don't give her softballs. Push her, make sure she can handle it."
        mike.say "And if she can't?"
        aletta.say "Then we replace her. That's how it works."
        mike.say "Okay, then."
        $ lavish.flags.promoted = 1
    else:
        aletta.say "[hero.name], I don't think she's qualified right now. Maybe she can try again in a few months, I don't know. But I'm not giving her the job."
        mike.say "So things stay as they are?"
        aletta.say "Yes, and you have to keep doing that work until we can hire your replacement."
        mike.say "Oh. That sucks."
        aletta.say "Welcome to management."
    hide aletta with easeoutleft
    return

label lavish_event_13:
    show lavish happy with easeinleft
    lavish.say "[hero.name]! [hero.name]! I got the job!"
    mike.say "I know! Aletta told me already."
    show lavish close
    "Lavish runs up to me and wraps her arms around me. I admit, the reward of having such an excited, beautiful woman in my arms, right then, is almost worth everything that we went through to get to this point."
    if lavish.flags.promisedFavor or lavish.love >= 80:
        show lavish kiss work
        $ lavish.flags.kiss += 1
        "And without even expecting it, she turns the hug into one sensational, delicious kiss. As her lips press into mine, I can't help feeling that I've really gained something today. After all, she works for me!"
        hide lavish kiss
        if lavish.flags.promisedFavor:
            lavish.say "That's just a down payment on what I owe you..."
        else:
            lavish.say "That's for being such an amazing man and helping me get this. I owe you so much!"
    $ lavish.flags.nokiss = False
    $ lavish.flags.nodate = False
    if lavish.love.max < 140:
        $ lavish.love.max = 140
    show lavish normal blush -close
    lavish.say "But now...now I have to work!"
    hide lavish with easeoutleft
    return

label lavish_event_14:
    if lavish.love.max < 150:
        $ lavish.love.max = 150
    "I let out a weary sigh as I force myself to buckle down and get on with the work in front of me."
    "It's way after office hours, and I've been talked into working late to get caught up."
    "But all I can think about is the plans that I had to cancel in order to be stuck here tonight."
    "Well, okay...my plans were basically to slob around the house playing on the Zbox."
    "But they were still my plans, dammit!"
    show lavish normal work at top_mostleft with easeinleft
    lavish.say "Hey, [hero.name]."
    lavish.say "How's it looking?"
    "The sound of Lavish's voice snaps me out of the funk that I'm in."
    "My eyes shoot up to see her standing in the doorway, holding two cups of steaming hot coffee."
    "Of course, that was the whole reason I let her talk me into doing this in the first place."
    show lavish at left with ease
    "It was a chance to spend some alone time with the most beautiful girl in the office!"
    mike.say "Oh...ah..."
    mike.say "It's looking real good, Lavish."
    mike.say "I'm tearing into it, yeah?"
    show lavish happy at center with ease
    "Lavish smiles at my positive words, her face lighting up as she does so."
    "And it was worth telling a little white lie just to see that happen."
    "She deposits one of the cups in front of me and sits down on the other side of the desk."
    "I'd rather Lavish was sitting closer to me, obviously."
    "But at least this way she can't actually see the screen of my laptop."
    "Which means she's none the wiser as to the amount of work I've got done!"
    show lavish normal
    lavish.say "I meant to say thanks, [hero.name]."
    lavish.say "It really means a lot to me, you doing this."
    "I wave away Lavish's thanks."
    "Inside I'm basking in every word she says."
    "But I want to look like slick, serious professional."
    mike.say "No worries, Lavish."
    mike.say "Sometimes hard work is it's own reward."
    "Lavish nods at this, but she chuckles too."
    "And I'm sure I see her shake her head a little."
    mike.say "Ah...what's up, Lavish?"
    mike.say "Did I say something funny?"
    show lavish annoyed
    "This time Lavish shakes her head more openly."
    lavish.say "No, [hero.name], not really."
    lavish.say "It's just that..."
    show lavish normal
    lavish.say "Well, I never thought you were so...disciplined."
    lavish.say "You kind of struck me as a bit of a slacker!"
    "My eyes go wide at this, as I think Lavish is seeing straight through me."
    "But she seems to take it as my being offended at what she just said."
    show lavish annoyed blush
    lavish.say "It was just a first impression, you know?"
    lavish.say "You're proving how wrong I was right now!"
    "I nod and make a point of burying myself in my work for a while."
    show lavish normal -blush
    "Lavish takes this as me wanting to get my head down and does likewise."
    "But the reality is that I'm brooding on what she just said about me!"
    "We keep on working alone and in silence for a while."
    "And then I stumble across something that I can't wrap my head around."
    "After staring helplessly at my screen for minutes on end, I give up."
    "Maybe what I need is a fresh pair of eyes to see what I'm missing."
    mike.say "Lavish?"
    show fx question
    lavish.say "Mmm?"
    mike.say "Would you come take a look at this for me?"
    "Lavish nods happily and gets up from her seat."
    hide lavish
    show lavish normal close
    "She walks over and leans in close to see my screen."
    "There can't be more than an inch between us right now."
    "The scent of her body and perfume is all I can smell."
    "And her breath is warm as she looks over my shoulder."
    "She's making it harder to concentrate than before!"
    lavish.say "So, what's the problem?"
    mike.say "Erm..."
    mike.say "I...I just can't get this to make sense."
    mike.say "It's like my head's somewhere else!"
    lavish.say "No problem, [hero.name]."
    lavish.say "I can see what's got you confused..."
    "Without thinking, Lavish reaches out for my mouse."
    "Her fingers brush over mine as my hand is still atop it."
    "Without thinking, I intertwine my fingers with hers."
    "Lavish turns to look me in the eye."
    "But I note that she doesn't pull her hand away."
    "I guess that means the ball is in my court..."
    menu:
        "Remain professional":
            "It'd be the easiest thing in the world to lean in a little closer."
            "I could probably plant a kiss on Lavish's lips before she knew what I was doing."
            "But then I think of what she just said about me."
            "I've only just made her change her mind about be being a slacker."
            "So is goofing off work to make out with her really a good idea?"
            "It's tough, because any chance to kiss Lavish is normally worth taking."
            "But I take a firm hold of myself and release her hand."
            "Lavish keeps looking me in the eye for a moment."
            show lavish embarrassed blush
            "And then she looks away, blushing and chuckling."
            show lavish flirt
            lavish.say "Wow - look at me!"
            lavish.say "I call you a slacker and then I do something like that!"
            lavish.say "How are you supposed to concentrate on your work when I..."
            "Lavish stops, realising that she's beginning to babble."
            show lavish normal -blush
            lavish.say "Anyway..."
            lavish.say "This should fix it!"
            show lavish -close
            "The job done, Lavish hurries back to her side of the desk."
            "She all but hides behind the screen of her own laptop."
            "But after a couple of awkward minutes pass, she looks up again."
            show lavish annoyed
            lavish.say "Ah, [hero.name]..."
            mike.say "Yeah, Lavish?"
            show lavish annoyed blush
            lavish.say "I...I do like it when you hold my hand, you know?"
            show lavish embarrassed blush
            lavish.say "I don't want you to think that I don't!"
            mike.say "It's okay, Lavish - I understand."
            mike.say "There's just a difference between being public and professional."
            mike.say "And sometimes we can forget that difference, right?"
            show lavish normal -blush
            "Lavish nods and smiles, the flush fading from her cheeks."
            "It seems to really mean something to her that I understand."
            "And maybe she's got it right on this subject."
            "Waiting to be intimate in a setting that's more comfortable for her."
            "That really isn't as big of a deal as it might sound."
            "We exchange another round of bashful smiles."
            "And then we get back to work again."
            $ lavish.love += 2
        "Get amorous":
            "Without giving myself time to think of the consequences, I act."
            "Lavish's lips are practically brushing mine already."
            "And so it doesn't take much to plant a kiss on them."
            hide lavish
            show lavish kiss work
            $ lavish.flags.kiss += 1
            "I feel Lavish jump a little in surprise."
            "But she doesn't make any effort to leap away."
            "That said, she does break off the kiss a few seconds later."
            hide lavish
            show lavish embarrassed close work
            "Lavish stands up straight, arms crossed over her chest."
            show lavish normal blush
            "She raises one eyebrow as she regards me."
            lavish.say "Were you struggling with this at all, [hero.name]?"
            show lavish flirt
            lavish.say "Or was that a ploy to get your hands on me?"
            "I shrug my shoulders and look a little sheepish."
            "It's probably best to let her think I was faking it."
            "Better than admitting I'm stumped, anyway."
            mike.say "You got me, Lavish."
            mike.say "I just thought we could take a break, yeah?"
            mike.say "After all, we're on our own - so who'd know?"
            show lavish normal
            lavish.say "Well, I'd know, [hero.name]!"
            lavish.say "Hmm..."
            show lavish annoyed
            lavish.say "Maybe you are a slacker after all!"
            show lavish normal -close
            "With that, Lavish walks back to her own side of the desk and resumes her work."
            "I'm pretty sure that she's not seriously mad at me."
            "But I may have just confirmed her suspicions as to my lack of professionalism!"
            $ lavish.sub += 2
    hide lavish
    return

label lavish_event_15:
    if lavish.love.max < 160:
        $ lavish.love.max = 160
    show lavish normal date
    "Everything seems to be going fine to begin with, and it looks like we're in for a great date night."
    "Lavish looks simply stunning, making me feel pretty lucky to be seen out in public with her."
    "And she's been nothing but smiles since she found out where we're going to be eating tonight too."
    "So when we're shown to our table and handed the menu, I'm feeling confident this is going to go well."
    "Waiter" "Do you see anything that you like?"
    "I look up at the waiter in surprise."
    "We've literally just glanced at the menus."
    "Usually the waiter leaves you alone while you make up your mind."
    "So why is this guy hassling us the moment we've scanned the menu?"
    mike.say "Ah, no..."
    mike.say "Not yet at least!"
    show lavish bored
    lavish.say "Can you give us a few minutes, please?"
    "The waiter looks a little sniffy at this."
    "But then his professionalism seems to take over."
    "Waiter" "I'm sorry for the rush."
    "Waiter" "It's just that we're a little busy tonight."
    show lavish normal
    "Lavish greets the explanation with a tight smile."
    "And then she offers a curt response."
    lavish.say "That's all very well."
    show lavish bored
    lavish.say "But it's not actually our problem, is it?"
    "The waiter stares at Lavish in silence for a moment."
    "But his professional demeanour seems to hold."
    "Waiter" "Of course not, madam."
    "Waiter" "As I already said, I'm sorry."
    "He turns and walks away, leaving us alone."
    show lavish annoyed
    "Lavish shakes her head in askance."
    mike.say "Ah, Lavish..."
    mike.say "Don't you think you were a bit hard on the guy?"
    lavish.say "Oh, [hero.name], don't try to defend him."
    lavish.say "That's how people get to thinking it's okay to behave like that."
    lavish.say "We're paying customers, after all."
    show lavish normal
    lavish.say "We deserve to be treated with respect."
    mike.say "If you say so Lavish..."
    "The waiter reappears a short while later, hovering just within our peripheral vision."
    "If I'm honest, I could have done with another couple of minutes to make up my mind."
    "But I decide to just choose something to speed up the whole process."
    "Waiter" "Sir...Madam..."
    "Waiter" "Are you ready to order now?"
    mike.say "I think I am."
    mike.say "How about you, Lavish?"
    "Lavish makes a non-committal sniffing sound."
    "And she doesn't look up from her menu either."
    lavish.say "I don't know..."
    show lavish bored
    lavish.say "Nothing seems to be jumping out at me..."
    "I can see the strain on the waiter's face as he tries to remain professional."
    "But I have to pinch myself when I hear what he says next."
    "The waiter keeps his lips straight, but hisses between his teeth."
    "Waiter" "Maybe I could see if the chef has anything else to Madam's taste?"
    "Waiter" "Perhaps some watermelon or a bucket of fried chicken?"
    show lavish surprised
    "Lavish looks at the waiter, her mouth hanging open in shock."
    "And then she turns her head to towards me, eyes wide."
    show lavish annoyed
    lavish.say "Did he..."
    lavish.say "Tell me he didn't..."
    show lavish bored
    "But I already know that he did."
    "The question is how am I going to handle it..."
    menu:
        "Play it down":
            "I don't think anyone else heard what the waiter said."
            "And I don't want to cause a scene either."
            "Maybe I can talk my way out of this one?"
            mike.say "Huh?"
            mike.say "What was that, Lavish?"
            mike.say "I didn't hear what the waiter said!"
            "Lavish looks at me in sheer disbelief."
            "And at the same time a smug smile appears on the waiter's face."
            show lavish angry
            lavish.say "You've got to be kidding me, [hero.name]!"
            lavish.say "This guy just racially abused me!"
            "I can feel myself beginning to sweat under the pressure."
            "Lavish isn't even trying to keep her voice down now."
            "And heads are starting to turn in our direction too."
            mike.say "Are you sure, Lavish?"
            mike.say "It's pretty loud in here."
            mike.say "You could have misheard..."
            hide lavish with easeoutright
            "Without bothering to reply, Lavish is up and out of her seat."
            "She doesn't explain herself, just turns and starts to make for the door."
            "I watch her go for a moment, and then realise that I should be going after her."
            "But even as I'm hurrying after her, I'm already dreading what she'll say to me..."
            $ lavish.love -= 2
            $ lavish.sub -= 2
            $ hero.cancel_activity()
        "Call for the manager":
            "Without missing a beat, I stand up and confront the waiter."
            mike.say "Fetch me the manager."
            "The waiter looks genuinely surprised at the demand."
            "I guess he was expecting me to punch his lights out when I got up."
            "Waiter" "Wha..."
            "Waiter" "Why would I do that?"
            "Waiter" "I didn't say anything!"
            "I keep my voice even, not rising to the bait."
            mike.say "I heard exactly what you said."
            mike.say "But that's not what I said."
            mike.say "Now, are you going to fetch the manger or not?"
            "It's at that point I hear a polite yet insistent cough behind me."
            "I turn to see a nervous-looking older woman standing there."
            "Manager" "Ahem..."
            "Manager" "I'm the manager, sir."
            "Manager" "What appears to be the problem?"
            "The waiter makes to open his mouth before I can speak."
            "But I shoot him a glance that almost makes him flinch."
            mike.say "This man used a term of racial abuse in regard to my companion."
            mike.say "And I find it bizarre that I'm having to have this conversation with you."
            mike.say "This is the twenty-first century, for god's sake."
            mike.say "That kind of behaviour is simply not acceptable."
            "Suddenly the manager's entire demeanour changes."
            "Where before she was anxious and uncertain, she becomes firm and focused."
            "And that's because I've handed her the perfect target in the shape of the waiter."
            "Now she can unload on him and distance the establishment from one bad apple!"
            "Manager" "Of course, sir, of course."
            "Manager" "You're one hundred percent correct."
            "Manager" "Be assured he will be dealt with straight away."
            "Manager" "I can offer you your meals for free - as an apology..."
            "I hold up my hand at this, cutting her off mid-flow."
            "And then I shake my head firmly."
            mike.say "No thank you."
            mike.say "My companion has already been insulted on these premises."
            mike.say "And I won't have her stay here a moment longer."
            show lavish normal
            "I look around to Lavish, but she's already on her feet."
            "She almost flies to my side, wrapping her arm in mine."
            "I keep my mouth shut until we leave."
            "And only then to do speak."
            scene bg street
            show lavish angry date
            mike.say "Are you okay, Lavish?"
            mike.say "Sorry if I didn't let you get a word in back there."
            mike.say "I was so angry that I just went off at them!"
            "Lavish shakes her head, smiling as she leans against me."
            show lavish happy
            lavish.say "Oh no, [hero.name]."
            lavish.say "You handled it perfectly."
            show lavish normal
            "Suddenly I feel a flush of pride surge through me."
            "But it's followed a moment later by a growl from my stomach."
            mike.say "Ah..."
            mike.say "Maybe we should find somewhere else to eat?"
            show lavish happy
            lavish.say "That sounds good."
            show lavish normal blush
            lavish.say "So long as you're with me!"
            $ lavish.love += 2
            $ game.active_date.score = 85
            $ game.room = "map"
        "Beat the waiter":
            "I hold up one hand to Lavish as I push my chair back and stand up."
            "The other I've already balled into a fist getting ready for what comes next."
            "The waiter doesn't even see the punch coming."
            play sound punch_hard
            pause 0.2
            with hpunch
            "It smashes into his nose, and I hear something snap."
            "All at once his legs buckle and he falls onto his ass."
            "Blood is already streaming out of his nostrils."
            "And yet he still doesn't seem to know what just happened."
            show lavish angry at hshake
            lavish.say "WHAT ARE YOU DOING?!?"
            lavish.say "[hero.name]..."
            lavish.say "Stop it!"
            "I was all ready to drag the waiter to his feet and give him some more."
            "But the sound of Lavish's cries stops me in my tracks."
            "And as soon as I pause, reality rushes back into my face."
            "Everyone in the restaurant is staring at me."
            "The waiter is cowering on the floor."
            "And my knuckles are covered in his blood!"
            "I shake my head, trying to recover my senses."
            mike.say "I..."
            mike.say "I heard what he said, Lavish."
            mike.say "You expect me to let him talk to you like that?"
            "Lavish is up and out of her seat in a heartbeat."
            "She shakes her head as she starts to back towards the door."
            show lavish angry at hshake
            lavish.say "No, [hero.name] - but he said it to ME!"
            lavish.say "I don't need you to fight my battles for me."
            lavish.say "Or to tell me how I should fight them either!"
            hide lavish with easeoutright
            "I watch her go for a moment, and then realise that I should be going after her."
            "But even as I'm hurrying after her, I'm already dreading what she'll say to me..."
            $ lavish.love -= 2
            $ lavish.sub -= 2
            $ hero.cancel_activity()
    return

label lavish_event_16:
    scene bg alettaoffice
    "Normally I like to zone out a little in the middle of a long and tedious meeting."
    "It's a fine art, keeping just enough of your brain in the room to pick up the gist of things."
    "But also letting your imagination be somewhere else entirely, anywhere more interesting."
    "Not that I can do that right now."
    show lavish work with dissolve
    "Not when Lavish is the one giving the presentation!"
    "She's kind of a hard-ass when it comes to this kind of thing."
    "It's always a subject that she's passionate about."
    "And you're going to be passionate about it too - damn it!"
    "I'll admit I'm paying more attention than I might otherwise have."
    "But seeing as Lavish and I are getting quite serious, it seems like the wise thing to do."
    "The last thing I want is to piss her off in a professional capacity."
    "Because I know that I'll end up paying for it in a personal one!"
    lavish.say "If you'll all take a look at slide number thirty three."
    lavish.say "Then you can see that, if anything, the trend is worse than expected!"
    "I rest my chin on the palms of my hands, leaning forward to see."
    "I have absolutely no idea what Lavish is talking about."
    "And to be honest, the graphs and charts only make it worse."
    "But I keep on nodding whenever it seems appropriate."
    "Which earns me the occasional sideways glance from her."
    "And when those come with a discreet little smile, I know I'm doing well!"
    lavish.say "So..."
    lavish.say "That pretty much wraps it up for this presentation."
    "At the mere mention of the end being in sight, nobody can contain themselves."
    "I hear sighs of relief and exclamations of delight from around the room."
    show audrey work at left with dissolve
    audrey.say "Urgh...thank god!"
    show shiori work at right with dissolve
    shiori.say "Oh, where am I...did I fall asleep?"
    show aletta work at mostleft4
    show audrey work at left4
    show shiori work at mostright4
    show lavish work at right4
    with dissolve
    aletta.say "Ah, yes..."
    aletta.say "Well done, Lavish..."
    "I look around at the others sitting in on the presentation."
    "Sure, the presentation was a little dry."
    "But am I the only one that's got the manners to keep from saying so?"
    lavish.say "I'll be sending the slides and my notes round via email."
    lavish.say "So...are there any questions?"
    "I see a look of panic on the faces of the others."
    "Audrey and Shiori begin to shake their heads."
    "And Aletta opens her mouth to stop Lavish in her tracks."
    aletta.say "I don't think so..."
    mike.say "Actually, Lavish - I had a question?"
    show aletta annoyed
    show audrey annoyed
    show lavish happy
    "I can almost feel the points of the daggers as the others glare at me."
    "But all I'm interested in is the glowing smile on Lavish's face."
    lavish.say "Yes, [hero.name]."
    lavish.say "What did you want to ask?"
    mike.say "I was just wondering..."
    mike.say "What was the source for the data you used?"
    mike.say "The one that was shown in that last graph?"
    show lavish normal
    "Lavish nods, preparing to impart the desired information."
    "The truth is that I have no real interest in it whatsoever."
    "I'm just bugged at the others for being so unkind to her."
    lavish.say "That's a very good question, [hero.name]."
    lavish.say "I love you..."
    show aletta surprised
    show shiori surprised
    show audrey surprised
    show lavish surprised blush
    "It takes me a moment to realise what Lavish just said."
    "To me it sounded like 'Thank you very much'."
    "But one quick glance around the room tells me that's not it at all."
    audrey.say "Whoa, Lavish!"
    audrey.say "Did you just say what I heard you say?!?"
    shiori.say "Oh my!"
    shiori.say "Are you in love with Mister [hero.family_name]?!?"
    show aletta normal
    aletta.say "Hmm, that's very interesting."
    aletta.say "I wonder if that's what they call a Freudian Slip?"
    "Lavish doesn't say a thing in response to any of this."
    "Instead she just stands there, shaking her head."
    "The whole time her eyes are getting ever wider."
    "But as soon as I make a move to get up from my seat, she snaps out of it."
    mike.say "Lavish..."
    mike.say "Are you okay?"
    lavish.say "I...I..."
    lavish.say "Oh god!"
    lavish.say "Oh god no!"
    hide lavish with moveoutright
    "And with that, she turns on her heel and hurries out of the meeting room."
    "My instinct is to go straight after her, to see if there's anything I can do."
    "But then I become aware that the others are now staring at me, rather than Lavish."
    mike.say "I..."
    mike.say "I should probably go after her."
    mike.say "You know - see if she's okay?"
    show shiori normal
    show audrey normal
    "All three of them nod slowly."
    "But their eyebrows are raised and they're watching me like hawks."
    "There's probably no point in trying to play this whole thing down."
    "And so I just make my excuses and follow in Lavish's wake."
    $ game.flags.lavfleemeetingdelay = TemporaryFlag(True, 3)
    $ lavish.hide()
    return

label lavish_event_17:
    "Things have been pretty awkward at work since Lavish's Freudian Slip."
    "She's avoiding me like the plague, which is bad enough on its own."
    "But the fact that she blurted out that she loved me in the middle of a meeting..."
    "Well, that means that we're now the prime subject of gossip in the office."
    "Everyone seems to be looking sideways at me and talking in hushed tones."
    "It's gotten so bad that I seriously thought about working from home for a while!"
    "But then a thought occurs to me - what if it's not the gossip that's the problem?"
    "I mean, it's not like Lavish having feelings for me is that crazy of a revelation."
    "We've been seeing each other for a while now."
    "And things have been going great between us all that time."
    "Maybe what's really bothering me is that Lavish ran off after making her confession."
    "That she ran off before I could really make sense of it all."
    "Suddenly I feel the urgent need to confront Lavish."
    "I need to tell her that what she said wasn't something to be embarrassed about."
    "And I need to tell her that I feel the same way about her too!"
    "It takes me a while to hunt her down."
    show lavish work
    "But eventually I manage to corner Lavish."
    mike.say "Ah..."
    mike.say "Hey, Lavish..."
    show lavish surprised at vshake
    "Lavish almost jumps out of her skin at the sound of my voice."
    show lavish annoyed
    "And I can see that she's looking from me to the nearest doorway."
    "Obviously, she's weighing up her chances of making a run for it!"
    mike.say "Please, Lavish..."
    mike.say "We...we really need to talk."
    mike.say "This is getting in the way of our work!"
    show lavish bored
    "At the mention of the professional side of things, I see Lavish stiffen."
    "I know that she's a stickler for coming off as a model employee."
    "So she can't ignore the issue when it's pitched from that angle."
    show lavish sad
    "Lavish sighs heavily."
    "And then nods her head in surrender."
    lavish.say "Okay, [hero.name], okay."
    lavish.say "I've been avoiding you, I admit it."
    lavish.say "I'm sorry."
    lavish.say "I should never have said that in front of everyone!"
    "I find myself nodding too."
    "But then I shake my head, remembering what I have to say to her."
    mike.say "Yeah, I know that, Lavish."
    mike.say "But that's not it."
    mike.say "I mean, that's part of it."
    mike.say "But it's not all of it."
    lavish.say "Erm..."
    lavish.say "I'm not sure I follow!"
    mike.say "I'm not angry with you, Lavish."
    mike.say "Not for saying what you said or avoiding me either."
    mike.say "I tracked you down because I wanted to tell you something."
    mike.say "I...I love you too, Lavish!"
    show lavish surprised blush
    "Lavish doesn't say anything in response."
    "She just stares at me silently."
    mike.say "Ah..."
    mike.say "Maybe I should have waited until after work..."
    show lavish normal
    "I don't get to finish speaking before Lavish stops me."
    "Without warning, she wraps her arms around my neck."
    hide lavish
    show lavish kiss work
    $ lavish.flags.kiss += 1
    "And then she's kissing me with a passion that almost bowls me over!"
    "I try to return the gesture."
    "But the best I can do is just hold on and enjoy the ride."
    show lavish work normal blush
    "When Lavish finally releases me, I can see that she's blushing."
    lavish.say "I...I'm sorry, [hero.name]."
    lavish.say "That was very unprofessional of me!"
    "I can't help laughing."
    mike.say "I kind of like you when you're unprofessional, Lavish!"
    "Lavish looks away bashfully at this."
    "But she laughs too."
    lavish.say "Well..."
    lavish.say "Maybe I could be a little more unprofessional from now on?"
    show lavish flirt
    lavish.say "You know, in a specific place and for an agreed period of time?"
    "I raise an eyebrow at this last comment."
    "How am I supposed to know if Lavish is being serious or not?"
    show lavish happy blush
    "It's only when Lavish bursts into laughter that I have my answer."
    "All I can do is shake my head and laugh along with her."
    hide lavish
    $ lavish.unhide()
    if lavish.love.max < 180:
        $ lavish.love.max = 180
    $ lavish.love += 2
    return

label lavish_event_18:
    "I hate getting summoned to someone's office for a meeting."
    "Especially when that someone just so happens to be Aletta."
    scene bg alettaoffice
    show aletta at right4
    show lavish sad at left4
    with fade
    "But when I walk in and see Lavish is already there, I feel myself begin to sweat."
    "What's she doing here?"
    "There's no work-related reason for it, is there?"
    "I want to ask what's going on, but this is Aletta's show."
    "So I just nod a hello to her and then one to Lavish as I sit down."
    show aletta happy at right
    show lavish sad at left
    with ease
    aletta.say "So glad you could join me, [hero.name]."
    show aletta normal
    aletta.say "You seem surprised to find Lavish here though!"
    "I shrug at this, not wanting to let Aletta know that I'm rattled."
    mike.say "Not surprised, Aletta."
    mike.say "Maybe a little confused."
    "I see a smile spread across Aletta's face."
    "And it's then that I know she's lured me into a trap!"
    aletta.say "Oh, really?"
    aletta.say "So you don't recall Lavish making an open declaration of love for you?"
    aletta.say "And doing so in the middle of a business meeting, of all places!"
    "Now I get it - now I see what all of this is about."
    "Lavish did say that she loved me in a meeting the other day."
    mike.say "So what, Aletta?"
    mike.say "You can't police our private lives."
    mike.say "Lavish can say she loves me as often as she wants!"
    show lavish blush
    lavish.say "That's not what this is about, [hero.name]!"
    lavish.say "They're worried that I could claim..."
    lavish.say "Well...that I could claim sexual harassment!"
    mike.say "WHAT?!?"
    mike.say "But that's crazy!"
    "Aletta still has that smile on her face as she raises her eyebrows."
    "The one that makes her look like a big cat about to pounce on its prey."
    aletta.say "Oh, is that so?"
    aletta.say "So you're saying that you deny using the influence of your authority?"
    aletta.say "You are above Lavish in the company hierarchy."
    aletta.say "And we have had problems with this kind of thing in the past..."
    "Suddenly, Aletta turns her gaze upon Lavish."
    aletta.say "What do you have to say about all of this?"
    aletta.say "How would you characterise his behaviour?"
    if lavish.flags.sleaze >= 20:
        show lavish annoyed
        "I see Lavish look away for a moment, squirming in her seat."
        lavish.say "I...I have to say that [hero.name]'s a bit of a ladies' man!"
        $ lavish.love -= 25
        $ aletta.love -= 25
        show aletta annoyed
        "Aletta leaps upon Lavish's words, like they're an admission of guilt."
        aletta.say "Ah, I see!"
        aletta.say "So there was an oppressive sexual atmosphere under him?"
        show lavish surprised
        "Lavish looks shocked at the question, and shakes her head."
        lavish.say "NO!"
        lavish.say "That's not what I mean at all!"
        show lavish embarrassed
        lavish.say "He just likes to admire members of the opposite sex, that's all!"
        show aletta angry
        aletta.say "You mean he's predatory?!?"
        $ lavish.sub += 10
        show lavish surprised
        lavish.say "NO...well, maybe just a little bit!"
        show lavish embarrassed
        lavish.say "But not in a bad way!"
        "Oh great - way to go Lavish!"
        "At this rate she'll hand Aletta all the ammunition she needs!"
        show lavish sad
    else:
        "Lavish doesn't hesitate to answer, looking Aletta straight in the eye."
        lavish.say "He's the perfect gentleman, very professional."
        show aletta angry
        "Aletta looks visibly unhappy with the answer."
        aletta.say "Hah!"
        aletta.say "I find that very hard to believe!"
        "I see anger flair in Lavish's eyes."
        "She obviously doesn't appreciate Aletta's tone."
        show lavish angry
        lavish.say "Then get the other girls in the office in here too."
        if Person.is_not_hidden("shiori") and Person.is_not_hidden("audrey"):
            lavish.say "Ask Audrey and Shiori how he behaves around them."
        show aletta normal
        "Aletta seems to back off at this, seeing that she's beaten."
        aletta.say "I'd prefer to keep this to the parties involved."
        aletta.say "The fewer people that know the better!"
        "Lavish looks vindicated, narrowing her eyes at Aletta."
        aletta.say "Okay, so he's not a sleaze-bag."
        aletta.say "But fraternisation in the workplace is still inappropriate!"
    "It sounds like Aletta's already made up her mind that I'm guilty!"
    "I thought that she was supposed to be neutral in things like this?"
    "Isn't she here to represent the company?"
    "She sounds more like a crusading lawyer out to nail a corporate creep!"
    "It's only now I remember the stuff I've heard about her and Dwayne."
    "And some of this starts to make sense to me at last."
    "Aletta was the victim of sexual harassment herself."
    "So maybe that's why she's going after me so hard?"
    if Harem.together(audrey, lavish, name='office') or Harem.together(shiori, lavish, name='office'):
        aletta.say "Off the record, [hero.name]..."
        aletta.say "I know all about what's been going on with the girls under you!"
        "I can already feel myself starting to sweat."
        mike.say "Hey!"
        mike.say "Nobody's done anything they didn't want to do!"
        mike.say "Everything that happened was one hundred percent consensual!"
        "I look to Lavish and then back to Aletta."
        mike.say "Look, the two of you are intelligent, sophisticated modern women."
        mike.say "It'd be an insult to suggest I could make you do something you didn't want to!"
        "Aletta shrugs and lets out a slow sigh."
        if Harem.together(audrey, shiori, lavish, name='office'):
            aletta.say "That goes for Lavish and myself, sure."
            aletta.say "But Audrey and Shiori?"
            aletta.say "One's an infantile attention-seeker."
            aletta.say "And the other one's submissive - practically a doormat!"
        elif Harem.together(shiori, lavish, name='office'):
            aletta.say "That goes for Lavish and myself, sure."
            aletta.say "But Shiori?"
            aletta.say "She's SO submissive - practically a doormat!"
        elif Harem.together(audrey, lavish, name='office'):
            aletta.say "That goes for Lavish and myself, sure."
            aletta.say "But Audrey?"
            aletta.say "She's an infantile attention-seeker."
    elif aletta.sexperience:
        "Of course there's also the fact that Aletta and I slept together in the past."
        "But there wasn't any harassment involved there - we were both up for it!"
        "Oh shit...she was MY manager at the time!"
        "Is she feeling the pressure because she fucked me while I was under her?"
    else:
        "I might not know what Aletta's ultimate aim is here."
        "But I'm not about to let her bully me into submission!"
    "Aletta sits back in her chair, arms crossed over her chest."
    show aletta happy
    "She looks amused and self-satisfied, very pleased with herself."
    aletta.say "So, [hero.name]..."
    aletta.say "What have you got to say for yourself?"
    $ INNOCENCE = False
    menu:
        "Deny everything":
            mike.say "It's...it's all lies!"
            mike.say "I haven't done a thing wrong here!"
            mike.say "And it's not like there's even stuff going on between us!"
            show aletta annoyed
            "Aletta rolls her eyes and shakes her head at my desperate denials."
            show lavish bored
            "And Lavish looks more than a little disappointed."
            "But why wouldn't she - I'm not exactly standing up for her!"
        "Admit guilt":
            mike.say "Whether or not I had relations with my other co-workers isn't the point."
            mike.say "This is about Lavish and myself, right?"
            mike.say "And if that's the case, then I don't have anything to hide."
            hide aletta
            hide lavish
            show lavish close blush
            "I turn to face Lavish."
            mike.say "Lavish, I love you!"
            mike.say "There, now I'm guilty of the same thing as her!"
            mike.say "Whatever way you want to twist it, you're not coming between us!"
            hide lavish
            show aletta at left
            show lavish at right
            show aletta annoyed
            "Aletta rolls her eyes and shakes her head."
            show lavish blush
            "But I can see a fire in Lavish's eyes."
            "And her smile tells me that I said the right thing in her mind."
        "Advocate innocence" if hero.knowledge >= 75 and hero.charm >= 75:
            mike.say "I won't deny the fact that I had relationships with my co-workers, Aletta."
            mike.say "Neither will I deny that those relationships were also sexual in nature."
            "I see a gleam in Aletta's eyes at this."
            "She seems to think I'm handing her all the evidence she needs."
            mike.say "But you can ask anyone that was involved."
            mike.say "And they'll tell you there was always a boundary between work and our private lives."
            show aletta surprised
            "Aletta pauses with her mouth open as my words sink in."
            mike.say "Furthermore, many sociological studies have looked at this area."
            mike.say "And they've established the office as a prime place for relationships to begin."
            mike.say "So you can hardly call healthy relationships between consenting adults deviant behaviour, can you?"
            mike.say "In fact, they're normal, widely-accepted social custom!"
            "Aletta's mouth hangs open, her lips flapping like those of a fish."
            show lavish happy
            "And out of the corner of my eye, I catch a glimpse of Lavish's triumphant smile."
            show lavish normal
            show aletta annoyed
            "Did I...did I just dazzle her with my performance?"
            $ INNOCENCE = True
    "I keep my eyes on Lavish for a moment, trying to see what she's thinking."
    "She's been pretty quiet so far, while Aletta's been attacking me."
    "At first she seemed to be mortified by all of this."
    "But now I can see a change slowly coming over her."
    show lavish angry
    lavish.say "Okay, Aletta, I think that's quite enough."
    lavish.say "You've had your fun, so let's get to the point."
    "At the sound of Lavish's voice, Aletta's head spins around."
    "And the tone of it accounts for the puzzled look on her face too."
    show aletta surprised
    aletta.say "I'm sorry..."
    aletta.say "What did you just say to me?!?"
    lavish.say "You know what I said, Aletta."
    lavish.say "This has gone far enough, and you know it!"
    show aletta angry
    "Aletta now turns her attention onto Lavish alone."
    "I can see that she's using all of her powers to intimidate the other woman."
    "But for some reason it doesn't seem to work at all."
    show lavish normal
    "Lavish just smiles straight back at her."
    aletta.say "What?!?"
    aletta.say "You should be taking this seriously, Lavish!"
    aletta.say "Sexual exploitation in the workplace is a real issue!"
    lavish.say "Oh it is, Aletta."
    lavish.say "And I do take it seriously - when it actually takes place!"
    show aletta annoyed
    aletta.say "But..."
    aletta.say "He...you..."
    "Where Aletta's becoming ever more flustered, Lavish remains cool and calm."
    show lavish bored
    "She tuts and shakes her head, as if Aletta just doesn't seem to understand."
    lavish.say "What are you suggesting, Aletta?"
    lavish.say "That I'm some dim-witted bimbo that can't think for herself?"
    lavish.say "Trust me, I have connections of my own."
    lavish.say "And I could have used them to crush [hero.name]."
    lavish.say "But I didn't, because everything that's happened between us was consensual."
    lavish.say "Hell, maybe my connections mean that I was the one manipulating him!"
    lavish.say "Did you ever think of that, Aletta?"
    "Now it's not just Aletta looking at Lavish in stunned silence."
    "My mouth is hanging open too as her words start to sink in."
    "Is she telling the truth - was she the one manipulating me all along?"
    "But now's not the time to be thinking about stuff like that."
    "I can question Lavish's motivations later, once we're out of this mess."
    "And it looks like the battle's not over yet."
    "Because Aletta's making a valiant effort to fight back!"
    show aletta normal
    aletta.say "Whatever, Lavish, whatever..."
    aletta.say "Save me the feminist speeches, okay?"
    aletta.say "None of that changes the fact you've both put the company at risk."
    aletta.say "That's why I'm going to have to insist that you sign this..."
    "Lavish and I stare at the hefty pile of paper Aletta thumps down in front of us."
    "And then we look back up at her as one."
    aletta.say "This is Corporate Relationship Agreement."
    aletta.say "It was drafted by the legal department - at great expense too!"
    aletta.say "By signing it you'll be declaring your status as a couple."
    aletta.say "It also specifies that the company bears no responsibility for your relationship."
    aletta.say "That and the inevitably messy way it's bound to end!"
    show lavish angry
    lavish.say "Hey!"
    mike.say "Yeah, watch it, Aletta!"
    show lavish bored
    "Aletta waves her hand in the air, dismissing our protests."
    aletta.say "Frankly I don't care about your feelings, either of you!"
    aletta.say "I just want you to sign the document - NOW!"
    "As if to emphasize her point, Aletta shoves the document towards us."
    "Lavish looks me in the eye, waiting to see what I do next."
    menu:
        "Refuse to sign" if not INNOCENCE:
            "I've just about had it with this BS!"
            "Aletta doesn't really care about protecting the company."
            "She's just doing this for the sake of the power trip!"
            "I shake my head and shove the document back towards her."
            mike.say "No way, Aletta."
            mike.say "You can't make me sign this thing."
            "I'm expecting Lavish to leap to my defence any moment."
            "But to my surprise, she looks disappointed with me."
            "And it's only now that I see she already had a pen in her hand."
            mike.say "Y...you were going to sign?!?"
            $ lavish.love -= 50
            show lavish sad
            lavish.say "Of course I was!"
            lavish.say "I don't want to, obviously."
            lavish.say "But it's the only way we can keep seeing each other!"
            "The sound of Aletta chuckling to herself distracts me from Lavish."
            "I look around to see her pretty much gloating."
            aletta.say "Oh dear, is there trouble in paradise?"
            aletta.say "Maybe your sordid little union isn't as strong as you thought?"
            "I can't think of an answer to that."
            "And I don't know what to say to Lavish either."
            "So I leap up from my chair and storm out of the room."
            "Maybe a little fresh air will help to clear my head."
        "Sign the document":
            "Without a moment's hesitation I grab a pen and reach for the document."
            "But then I hear a gasp from Lavish, which makes me pause and look in her direction."
            mike.say "What's wrong, Lavish?"
            mike.say "Don't you want me to sign this thing?"
            show lavish blush
            lavish.say "I...I do want you to sign it."
            lavish.say "But I thought that you'd refuse!"
            lavish.say "I thought I'd have to convince you to do it."
            show lavish happy
            mike.say "If it's the only way to solve this, of course I'll sign it."
            mike.say "It's just a piece of paper, Lavish."
            mike.say "I won't let it come between us!"
            "Instantly I can see that I've said the right thing."
            show lavish normal
            "Lavish nods, her eyes wide and bright with adoration."
            "Aletta lets out a snort of derision at this."
            "But I guess she can't let herself appear too disappointed."
            "After all, she is getting what she wants."
            "And she has to make it look like this is just an impartial action she has to carry out."
            "Lavish signs the document after me, and the she shoves the document back at Aletta."
            aletta.say "There we go!"
            aletta.say "That wasn't too hard, now was it?"
            mike.say "Can we go now, Aletta?"
            mike.say "You've got what you wanted."
            lavish.say "We can go, [hero.name]."
            lavish.say "She can't keep us here any longer."
            lavish.say "If she does, then she's going to be the one facing disciplinary action!"
            "Aletta motions towards the door, a smug grin on her face."
            "But I feel reassured as Lavish takes a tight hold of my hand."
            "And I don't look back as she leads me out of the room."
            $ lavish.flags.signed_document = True
        "Refuse to sign" if INNOCENCE:
            "I can feel the laughter bubbling up inside of me."
            "And there's nothing I can do to keep it from coming out."
            "Aletta seems taken aback when she hears it."
            "But her expression turns to rage a moment later."
            "Because I shove the document back towards her and shake my head."
            show aletta angry
            aletta.say "What the..."
            aletta.say "How dare you?!?"
            mike.say "Ah, shut up, Aletta!"
            mike.say "Where do you get off peddling this garbage, huh?"
            mike.say "Any two-bit lawyer would tear it apart in seconds!"
            aletta.say "I think you'll find that out from the legal department..."
            mike.say "And drop the legalese too!"
            mike.say "This isn't about any of that."
            mike.say "This is about a cowardly company trying to cover it's own ass!"
            mike.say "Trying to protect itself and not the people who work here."
            show aletta annoyed
            "Aletta looks genuinely flustered at my attack."
            "She glances this way and that, like she doesn't know what to do."
            "Hell, she even picks up the receiver of the phone on her desk."
            "And for a moment I think she's going to call security!"
            show aletta angry
            aletta.say "You...you can't say that!"
            aletta.say "You can't say that to me!"
            mike.say "This is a free country, Aletta."
            mike.say "I can damn well say what I want!"
            mike.say "You can't litigate love - it deserves better than this!"
            mike.say "Lavish deserves better than this!"
            "I stand up and thrust out a hand towards Lavish."
            mike.say "Come on, Lavish, we're leaving."
            "I can see that I've said the right thing, hit a chord with Lavish."
            show lavish normal blush
            "She nods, her eyes wide and bright with adoration."
            "And she leaps up, grabbing my hand tightly."
            "Aletta lets out a snort of derision at this."
            aletta.say "You haven't heard the last of this - either of you!"
            aletta.say "I hope you have a decent lawyer!"
            aletta.say "Because you're going to need one!"
            "But neither of us looks back as we walk out of the room."
            "And the feeling of Lavish's hand in mine makes me feel invincible."
    if lavish.love.max < 200:
        $ lavish.love.max = 200
    return

label lavish_preg_talk:
    $ lavish.flags.toldpreg = True
    show lavish
    "I guess I should have noticed that there was something a little off with Lavish today."
    "But then I'm usually distracted by her presence anyway, you know?"
    "Having such a beautiful girl around and knowing that we're an item."
    "I mean, can you blame me for being wrapped up in that thought when she's around?"
    "So when she comes out and confronts me with it, I'm taken by surprise."
    lavish.say "[hero.name]..."
    lavish.say "There's something that I need to tell you."
    lavish.say "Something that's really important."
    "Well, that's more than enough to snap me out of it and get my attention."
    "What guy doesn't dread his significant other having something to tell him?"
    "Especially when it sounds as ominous as that!"
    mike.say "Ah, okay, Lavish."
    mike.say "I'm listening."
    mike.say "What is it?"
    show lavish bored
    "Lavish takes a deep breath, collecting herself before she speaks."
    "And I can see the effort that it's taking written all over her face."
    lavish.say "This isn't an easy thing to admit, [hero.name]."
    lavish.say "But here goes..."
    show lavish normal blush
    lavish.say "I just found out that I'm pregnant!"
    "Wow...just wow."
    "I was honestly expecting Lavish to say she was dumping me or something."
    "But I wasn't prepared for a bombshell like that!"
    mike.say "Y...you're sure, Lavish?"
    mike.say "You took a test and everything?"
    show lavish bored -blush
    "Lavish nods, looking a little irritated at the questions."
    lavish.say "Of course I did, [hero.name]."
    lavish.say "This is serious, so I needed to be sure."
    mike.say "And I'm the father?"
    show lavish angry
    lavish.say "[hero.name]!"
    lavish.say "I haven't been playing around behind your back."
    lavish.say "That means you have to be the father."
    "I nod hastily, sensing that I'm in danger of seriously pissing Lavish off."
    "Of course she's going to be sure of stuff like that."
    "Lavish is nothing if not organised and professional."
    "Even in terms of her private life!"
    mike.say "Have you decided what you want to do?"
    mike.say "You know - about the baby?"
    show lavish annoyed
    "Lavish lets out a sigh, her mood softening as she does so."
    "And I see her hands unconsciously cradling her belly."
    lavish.say "I...I don't want you to think I'm cold, [hero.name]."
    lavish.say "But my first instinct is to have a termination."
    lavish.say "We never planned for this, either of us."
    lavish.say "And going through with it would ruin my career."
    "I nod, keen to show Lavish that I do understand her dilemma."
    "She's worked her ass off to get where she is at work."
    "Everyone would pay lip-service to her taking maternity leave."
    "But they'd snap up her spot as soon as she was out of the office too!"
    show lavish normal
    lavish.say "Well..."
    lavish.say "What do you want to do, [hero.name]?"
    lavish.say "You should have some say in this too!"
    menu:
        "We should keep it":
            "I'm grateful that Lavish wants to get my input on this."
            "Some girls I've known wouldn't have been so eager to hear it!"
            "She's pretty modern and cool like that."
            "And that's when it strikes me with the force of a slap."
            "Why are we thinking like we're living in the last century?"
            mike.say "Why does it have to be your career that takes the hit, Lavish?"
            "Lavish looks at me sideways, clearly not getting my point."
            lavish.say "Erm, because I'm the one that's pregnant, [hero.name]!"
            mike.say "Sure, Lavish, sure."
            mike.say "But after that, what if I was the one to stay home?"
            show lavish bored
            "Lavish stares at me blankly for a moment."
            "Then she blinks and shakes her head, as if finally understanding."
            show lavish normal
            lavish.say "You'd do that?"
            lavish.say "For me?"
            lavish.say "You'd actually quit work and raise the baby?"
            mike.say "Yeah, Lavish, I would."
            mike.say "This is the twenty-first century, and I'm a modern guy."
            mike.say "I'm not afraid of changing nappies!"
            "I can see that Lavish is already turning the idea over in her head."
            "This would mean that she could have the best of both worlds."
            "She gets to keep her career and her baby."
            "Unlike most women, she could really have it all."
            "And I think she wasn't expecting me to even suggest it either."
            "Because she's looking at me with a new shine in her eyes the whole time!"
            show lavish kiss
            $ lavish.flags.kiss += 1
            "Lavish surprises me then by kissing me full on the lips."
            show lavish blush
            "When she breaks it off, I'm the one feeling flustered."
            mike.say "I...I take it you like the idea?"
            "Lavish nods."
            mike.say "But what was the kiss for?"
            lavish.say "Oh you know..."
            lavish.say "Just keeping the little man at home sweet!"
            $ lavish.love += 10
        "You should have a termination":
            "The idea of having a kid with Lavish has instant appeal."
            "I love spending time with her, and I can see a future for us together."
            "But that's what it is right now - a vision of a future."
            "We're both focused on our careers, not ready to start a family."
            mike.say "I understand, Lavish."
            mike.say "And for the record, I don't think you're cold."
            mike.say "In fact, you're really thinking of the child here."
            "Lavish nods, clearly wanting to be reassured by my words."
            "But she's too smart and self-aware to let herself be convinced so easily."
            show lavish bored
            lavish.say "H...how's that, [hero.name]?"
            lavish.say "What do you mean?"
            mike.say "We're not ready for kids, Lavish."
            mike.say "We both know that."
            mike.say "If one or both of us gave up our careers..."
            mike.say "Well, no one would say it out loud."
            mike.say "But we'd end up resenting the kid, and each other too!"
            show lavish normal
            lavish.say "I guess you're right."
            mike.say "You'll be a great mom, Lavish - I know that as well."
            mike.say "But that'll happen when the time's right."
            "Lavish nods, forcing a smile onto her face."
            "Though I can see tears welling in her eyes."
            "I reach out and pull her into an embrace."
            "Neither of us needs to speak right now."
            "Just to know that we're there for each other."
            $ lavish.unpreg()
    return

label lavish_male_ending:
    $ game.hour = 16




    if renpy.has_label("lavish_achievement_3") and not game.flags.cheat:
        call lavish_achievement_3 from _call_lavish_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "This is one of those days that I could never have imagined back when Lavish and I first met."
    "And that's not me being down on myself either - not me saying that I thought she was too good for me."
    "Lavish is just one of those girls that walks into a room and makes you hold your breath."
    "Then you almost pass out because you're staring at her, rather than actually breathing!"
    "At first it was a big thing for me to even see her every day at work, she was just so hot."
    "So I was pretty amazed when she also turned out to be such a great person too."
    "You know how it is - sometimes hot girls are such awful, entitled bitches."
    "But not Lavish, oh no!"
    "We became friends, then we got even closer than that."
    "And now here we are, about to actually tie the knot!"
    "Part of me still can't believe that I'm standing at the altar."
    "I keep glancing back over my shoulder, hoping to catch a glimpse of her."
    "Every time I do so, I can see the assembled guests filling the chapel."
    "But as soon as I hear the swell of music, I forget all about them."
    "That's because, the moment she appears, I only have eyes for Lavish."
    show lavish wedding at center, zoomAt(1.0, (640, 730))
    "She appears at the other end of the chapel, walking down the aisle."
    "And now I know why she insisted on me not seeing the dress before the big day."
    "It's perfect, making her look like a fairy tale bride."
    if lavish.is_visibly_pregnant:
        "Rather than trying to hide the shape of her swelling belly, the dress allows for it."
        "And in doing so it makes her look that much more beautiful too."
        "I know all about the negative connotations of a pregnant bride."
        "But all of that seems so silly and old-fashioned right now."
    else:
        "Somehow it manages to make Lavish look pure and almost innocent."
        "Yet at the same time it doesn't even try to hide her incredible figure either."
        "I don't know what kind of sorcery this is."
        "But I do know that I approve!"
    show lavish at center, traveling(1.5, 3.0, (640, 1040))
    "I guess that my amazement must be written all over my face."
    "Because Lavish is grinning at me by the time she reaches the altar."
    "Of course this only serves to make her look even more beautiful."
    show lavish flirt
    lavish.say "I take it that you approve, [hero.name]?"
    lavish.say "You like what you see?"
    mike.say "Y...yeah, Lavish!"
    mike.say "You look incredible!"
    show lavish happy
    show wedding lavish with fade
    "The helpless nature of my reaction only makes Lavish's smile broader still."
    "And she looks like she's about to say more."
    "But then we're both reminded of where we are and what we're doing right now."
    "Priest" "Ahem..."
    "Priest" "If the two of you are ready?"
    show wedding lavish priest with dissolve
    "Lavish and I suddenly snap to attention."
    "We look at each other and then back at the priest."
    "Our heads are nodding like crazy to show that we're ready to begin."
    "Priest" "Very good..."
    "Priest" "Ladies and gentlemen..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people together in the bonds of holy matrimony..."
    "The rest of the ceremony goes how you'd expect it to."
    "So I'll skip to the important parts, okay?"
    "Priest" "Do you, [hero.name], take Lavish to be your lawful, wedded wife?"
    mike.say "I do!"
    "Priest" "Very good."
    "Priest" "And do you, Lavish, take [hero.name] to be your lawful, wedded husband?"
    lavish.say "I do."
    "Priest" "Then I call upon all those present..."
    "Priest" "That if anyone knows of a reason these two may not be married..."
    "Priest" "Speak now, or forever hold your piece!"
    "There's the customary pause as the priest looks around the chapel."
    "And it's followed by the usual ripple of laughter from the guests."
    "Lavish and I share a nervous exchange of glances, smiling at each other."
    "There's nothing I can imagine that would come between us now."
    "But all the same, I hold my breath until the priest nods his head."
    "Priest" "Very well..."
    "Priest" "It gives me great pleasure to declare you husband and wife."
    "Priest" "You may kiss the bride!"
    show wedding lavish priest with dissolve
    "Like I need anyone to tell me to do that!"
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show lavish kiss wedding
    with fade
    $ lavish.flags.kiss += 1
    "I wrap my arms around Lavish and lean in to kiss her."
    "And she doesn't need to be encouraged either, almost hopping into my embrace."
    "I think that I can hear the sound of people cheering around us."
    "There might be music too, for all I can tell."
    "But the only thing I care about is holding Lavish as close to me as possible."
    "I still can't believe it - she's actually my wife!"
    "I'd pinch myself."
    "But if this is a dream, then I don't want to wake up!"
    scene lavish ending
    with fade
    lavish.say "Well, I suppose the first thing to say is that I never for a moment saw myself ending up here."
    lavish.say "Don't take that as a slight on [hero.name] - or that I'm not happy with how things turned out."
    lavish.say "What I mean is that I'd always had a vision of where I was going, a plan for my life."
    lavish.say "But I guess that's what they mean when they say life is what happens while you're making plans!"
    lavish.say "I was always so focused on my career, on climbing the ladder and making it to the top."
    lavish.say "I never spared a thought about there being room for more in my life."
    lavish.say "Because of that, [hero.name] kind of took me by surprise."
    lavish.say "Before I knew what was happening, we were dating."
    lavish.say "And the next surprise was just how much I was loving it!"
    lavish.say "Look, I know he's a bit geeky and he can be really goofy at times."
    lavish.say "But he's also sweet, romantic and a stand-up guy too."
    lavish.say "At first I thought he was going to be just another typical male colleague."
    lavish.say "You know the kind of man that I mean."
    lavish.say "Macho, arrogant and convinced that a woman's place isn't in the office."
    lavish.say "And one hundred percent convinced that her place is below him too."
    lavish.say "And...I'll admit it - I was too quick to judge him."
    lavish.say "[hero.name] just isn't like that at all."
    lavish.say "Obviously he's not - or else I wouldn't be sitting here telling you all of this!"
    lavish.say "If he were, then I'd never have gotten into a relationship with him."
    lavish.say "And I certainly wouldn't have married him either!"
    lavish.say "But I did, and things seem to have just got better from there."
    lavish.say "After the wedding, we went to Paris for our honeymoon."
    lavish.say "Paris - part of me still can't believe we went somewhere so magical!"
    lavish.say "We stayed there for two entire weeks, and every moment was heaven."
    lavish.say "[hero.name] might have struggled with the language."
    lavish.say "And he was always complaining that the locals were so rude."
    lavish.say "But I was happy every second that we were there."
    lavish.say "In fact, I even suggested that we should live there forever."
    lavish.say "[hero.name] said that he'd think about it."
    lavish.say "As far as I know he's still thinking about it..."
    lavish.say "But anyway..."
    lavish.say "Once we got back home, [hero.name] proved his quality."
    lavish.say "He never once stopped me from getting ahead in the office."
    lavish.say "And he didn't try to open doors for me either."
    lavish.say "Instead he let me achieve everything with my own efforts."
    lavish.say "But that doesn't mean he left me all alone either."
    lavish.say "He was there every step of the way, supporting me the whole time."
    lavish.say "There were even moments when he put my career before his own."
    if lavish.flags.mikeBabies >= 1 or lavish.is_visibly_pregnant:
        lavish.say "And that made me start thinking about what he wanted too."
        lavish.say "[hero.name] was making a sacrifice for me."
        lavish.say "But that just didn't feel right somehow."
        lavish.say "For the first time, work was beginning to feel hollow and unfulfilling."
        lavish.say "It was when I found out that I was pregnant with Mathieu that things changed."
        lavish.say "[hero.name] was ecstatic at the news, and that made me happy too."
        lavish.say "It made me realise that there was more to life than work."
        lavish.say "And that my family made me happier than my career ever could."
    else:
        lavish.say "And that's made me start thinking about what he wants too."
        lavish.say "[hero.name]'s made so many sacrifices for me in the time we've been together."
        lavish.say "It just doesn't feel right somehow."
        lavish.say "It's even starting to make work feel somehow hollow and unfulfilling."
        lavish.say "I don't really know what the answer is."
        lavish.say "But maybe it's time I started to put him before my career too?"
    lavish.say "I suppose that's what [hero.name]'s brought to my life."
    lavish.say "He's taught me that sometimes it's okay not to have a plan."
    lavish.say "That sometimes you can just sit back and see where life takes you."
    lavish.say "But that doesn't mean you can't have a plan ready for when you get there!"
    lavish.say "You just need to keep it under wraps until the time comes when you need it."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not lavish.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_13
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_13
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label lavish_office_bj(called_from_office=False):
    if lavish.sub.max < 60:
        $ lavish.sub.max = 60
    if not called_from_office:
        "I know that I really should be more professional at work, keep my mind on the job."
        "But every time I catch even the briefest glimpse of Lavish, it's just hopeless."
        "She doesn't even have to look in my direction or notice that I'm there at all."
        "I just can't keep my eyes off of her and my thoughts on anything else!"
        "So in the end, I retreat into my office and pick up the phone."
        "Efficient as ever, it doesn't take Lavish more than a second to pick up."
        lavish.say "Good morning, [hero.name]."
        lavish.say "How can I help you today?"
        "God she's good - so on the ball and professional."
        "Yet at the same time she has that undertone of sex-appeal going on too!"
        lavish.say "Erm...hello?"
        "I shake myself back to reality, realising that I forgot to answer."
        "I was too busy mooning over Lavish's sexy voice to notice!"
        mike.say "Ah..."
        mike.say "Hey, Lavish..."
        mike.say "I was wondering...could you step into my office?"
        "Lavish again shows her professionalism by totally ignoring my own blunder."
        "When she responds, her own tone betrays not even the smallest hint of annoyance."
        lavish.say "Of course, [hero.name]."
        lavish.say "I'll be right there."
        lavish.say "Were you wanting to dictate something?"
        mike.say "Yes, Lavish - that's right."
        mike.say "I want you to come in here for some DICK-tation!"
        lavish.say "I'm sorry...what was that?!?"
        mike.say "Nothing, Lavish, nothing..."
        mike.say "Just a little light dictation, like you said."
        "I do the best I can to keep myself under control as I wait for Lavish to arrive."
        "But I can already feel my anticipation rising at the mere thought of being alone with her."
        show lavish at left with easeinleft
        "And the moment she walks through the door, my heart starts pounding inside of my chest."
        lavish.say "Here I am, [hero.name]."
        lavish.say "Where would you like me?"
        "Why do hot girls always do that to me?"
        "Ask an innocent question that I have to take in a filthy way?"
        mike.say "Over here, Lavish, please!"
        mike.say "I'd like to have you over the desk..."
        mike.say "By the desk...I mean by the desk!"
        "Lavish nods, seeming to ignore my stammering and fumbling."
        show lavish at center with ease
        "She sits in the chair on the other side of the desk."
        "And then she takes up her pad and pen, ready for me to begin."
        mike.say "Okay, Lavish, here's the thing..."
        mike.say "I do need your help with something."
        mike.say "But it doesn't involve dictation."
        show fx question
        "Lavish cocks her head on one side, a curious expression on her face."
        "She puts down her pad and paper, regarding me with genuine interest."
        lavish.say "Oh, I see."
        lavish.say "And what would that be?"
        mike.say "I...I was thinking..."
        mike.say "Maybe you could give me some...executive relief?"
        mike.say "Specifically some relief down there?"
    "I push my chair back from the desk."
    "And then I point down between my legs."
    "That's all it takes for Lavish to catch my meaning."
    "And I see her eyes go wide, her mouth forming an 'O'."
    show lavish surprised blush
    lavish.say "That's not exactly part of my job description you know!"
    if not called_from_office:
        lavish.say "In fact, it could be grounds to report you to the HR department!"
        "For a moment I feel like things are about to go south for me."
        "But then I realise something, and I narrow my eyes."
        mike.say "What do you mean by that, Lavish?"
        mike.say "What do you mean it 'could be'?"
        show lavish annoyed
        "Lavish looks more than a little flustered as I say this."
        "She glances this way and that, as if looking for a way out."
        mike.say "Are you...are you trying to negotiate with me?!?"
        mike.say "Like there's something you want in return for blowing me?"
        lavish.say "No...I..."
        show lavish normal
        lavish.say "Well...maybe...I guess!"
        "I can feel a smile spreading across my face right now."
        "And at the same time Lavish's cheeks are flushing red."
        "She is - she's willing to trade favour for favour!"
        mike.say "Okay, Lavish, how about this?"
        mike.say "You give me a blowjob, and I'll make sure you're rewarded."
        mike.say "I'll put you up for the next choice assignment that lands on my desk."
        mike.say "Do we have a deal?"
        show lavish -blush
        "Lavish looks away for a moment, biting her lip."
        "But then I see her ambition win out over her pride."
        "And she nods, already getting up out of her seat."
        lavish.say "Oh god...I'm going to regret this, I just know it!"
        lavish.say "So you'd better make good on your promises, [hero.name]!"
        lavish.say "Because I can cope with regretting something I did."
        lavish.say "But not with regretting something YOU didn't do!"
    "I nod eagerly as I push my chair further back from the desk."
    hide lavish
    show lavish bj office
    with fade
    "And Lavish wastes no time in kneeling down in front of me."
    "She keeps her eyes down as she unzips my pants."
    "Then I feel her reach inside and take hold of my cock."
    lavish.say "Oh..."
    lavish.say "You...you're already hard!"
    lavish.say "I thought I'd have to..."
    lavish.say "I mean the last time that I..."
    "Lavish shakes her head and turns her attention back to the task at hand."
    if not called_from_office:
        "And it's then that I realise what's gotten her so confused."
        "She must have done this before and had to put some work in to get the guy hard."
    "I guess she had no idea how much the thought of her was turning me on!"
    "And I think I can see this reflected in Lavish as she begins her task."
    "I had been expecting that she might carry it out in a mechanical fashion."
    "Just putting in the minimum of effort in order to get it over with."
    show lavish bj blow
    "But instead, she takes her time, kissing the base of my cock gently."
    "Then she licks around my balls with the tip of her tongue."
    "And the subtle way she does it actually makes me gasp in surprise."
    "Lavish seems to take this as my seal of approval."
    show lavish bj hold
    "And she begins to work her way upwards in the same manner."
    "She travels to the very top of the shaft in this way."
    "Kissing, licking and caressing as she goes."
    "By the time she reaches the head, I'm panting at her efforts."
    if not called_from_office:
        "My hands are gripping the arms of my chair."
        "Fingers digging into the soft material."
    "My entire body tenses in anticipation of what comes next."
    "And Lavish certainly doesn't disappoint me either."
    show lavish bj deep pleasure
    "As opens her mouth just wide enough to swallow the tip."
    "Then she ever so slowly eases it inside."
    "But every agonising inch is filled with the sensation of her tongue."
    "Lavish uses that extraordinary part of her body with astounding expertise."
    "More than once I'm sure she wraps it all the way around my cock."
    "Wrapping it up like her tongue's a living ribbon of some kind."
    "Part of me wants to keep quiet while she's at it."
    "Keep a straight face so that I don't let on how good this feels."
    if not called_from_office:
        "That way I can keep a stronger hand when I come to reward Lavish afterwards."
    "But that soon goes out the window, as I just can't keep quiet!"
    mike.say "Oh god..."
    mike.say "Lavish, you're the best!"
    mike.say "You're like the best at everything!"
    show lavish bj tip normal
    "My words seem to have an instant effect on Lavish too."
    "I know that she craves approval in her work."
    "That she always strives to be the best at what she does."
    "And it seems like that extends to giving head too!"
    show lavish bj deep pleasure
    show sexinserts head lavish zorder 1 at center, zoomAt(1, (720, 760))
    "Lavish's head begins to bob up and down like crazy."
    "She's working me with such intensity it feels incredible."
    "There's no way I can hold on much longer."
    "Lavish is going to make me cum!"
    menu:
        "Cum on her face":
            "I make a sudden effort to pull backwards before I lose it."
            show lavish bj tip out normal back
            hide sexinserts
            "And this pulls my cock right out of Lavish's mouth in one movement."
            "She's left with her lips parted and a look of surprise on her face."
            show lavish bj cumshot pleasure
            "A look which hardly changes as I shoot my load onto it."
            "Lavish yelps and tries to cover her face with her hands."
            show lavish bj cum onface -cumshot
            "But she's too late, and most of the semen spatters her nose and cheeks."
            "It runs down her face, dripping off her chin and the end of her nose."
        "Cum in her mouth":
            "I make a sudden effort to push forwards before I lose it."
            show lavish bj creampie pain back
            show sexinserts head lavish zorder 1 at center, zoomAt(1, (720, 760))
            with hpunch
            "And this pushes my cock right down Lavish's throat as I cum."
            with hpunch
            "Her eyes go wide and she makes a gagging noise."
            with hpunch
            "But somehow she manages to swallow everything that I have to give."
            show lavish bj pleasure tip hold
            hide sexinserts
            "Afterwards, Lavish licks her lips and wipes them with the back of her hand."
            "But semen still pools in the corner of her mouth."
            "It runs down her face, dripping off her chin as well."
    show lavish bj normal
    "True to form, Lavish recovers first."
    "She cleans herself up while I sit helplessly in my chair."
    "Hell, she even does me a favour and stuffs my cock back into my pants!"
    "And then she collects her things, nodding at me in a professional manner."
    hide lavish bj
    show lavish
    with fade
    lavish.say "Will that be all, [hero.name]?"
    mike.say "Ah...I...."
    mike.say "Yes, Lavish...that'll be all."
    mike.say "And thank you too!"
    show lavish at top_mostleft with ease
    "Lavish raises an eyebrow as she reaches to open the door."
    if not called_from_office:
        show lavish flirt
        lavish.say "Oh, don't worry, [hero.name]."
        lavish.say "You can thank me by keeping your promises!"
    hide lavish with easeoutleft
    "And with that, she's gone."
    "Which leaves me to stare longingly after her."
    $ lavish.love += 2
    return

label lavish_spanking_start:
    "I can't help smiling at the question."
    "And I guess the expression must look more than a little wolfish and hungry."
    "As Shiori takes an unconscious step backwards as she gazes at me from across the room."
    "All the same I keep on smiling as I push my chair back from the desk."
    mike.say "I'm feeling a little lack of focus this morning, Shiori."
    mike.say "So what I'd like you to do is come over here."
    mike.say "Come over here and lay across my lap."
    mike.say "Then I want you to let me spank your big, round ass - okay?"
    show shiori surprised
    "Shiori's hand shoots up to cover her mouth."
    "And her eyes go wide with shock."
    shiori.say "Y...you want to...spank me?!?"
    show shiori blush
    shiori.say "Right here and now - at work?!?"
    mike.say "That's right, Shiori."
    mike.say "And it's not a request either."
    mike.say "I'm telling you to do as I say - right now!"
    show shiori normal
    "Shiori nods her head as she scuttles around the side of my desk."
    shiori.say "Y...yes, [hero.name]!"
    shiori.say "Of course...I'll be right there!"
    "I watch with satisfaction as Shiori hikes up her skirt."
    "And then she hastily throws herself over thighs."
    hide shiori
    show spank shiori
    with fade
    "The feeling of her weight landing in my lap is amazing."
    "That and the way she has to squirm around to get into place."
    "It's so good that I can already feel my cock getting hard."
    shiori.say "Oh..."
    shiori.say "I've been such a bad girl!"
    shiori.say "You'd better spank me good and hard!"
    "I can't help smiling as I give Shiori's ample butt a good slap."
    show spank shiori spank surprised
    play sound spank
    with hpunch
    "She squeals in alarm, but nods all the same, asking for more."
    "I can already feel my mind beginning to clear."
    "Spanking Shiori is finally getting Lavish off my mind."
    show spank shiori up
    pause 0.3
    show spank shiori spank
    play sound spank
    with hpunch
    "And it's not like I'm cheating on her - not really."
    "I mean, Shiori's not sucking my cock or letting me fuck her over my desk."
    "This is no worse than her getting me a cup of coffee or giving me a massage, right?"
    show spank shiori up
    pause 0.3
    show spank shiori spank
    play sound spank
    with hpunch
    "And spanking her ass feels so good that I don't see how it could be wrong."
    show spank shiori up
    mike.say "We should make a habit of this, Shiori."
    show spank shiori spank pleasure
    play sound spank
    with hpunch
    shiori.say "Y...yes?"
    mike.say "Put aside half an hour a day for spanking!"
    show spank shiori up
    shiori.say "If...if you like!"
    show spank shiori spank marks
    play sound spank
    with hpunch
    mike.say "You bet I like it, Shiori!"
    lavish.say "Oh...my...god!"
    hide spank
    show lavish surprised at top_mostleft
    with vpunch
    "My hand comes to a halt perhaps an inch from Shiori's buttocks."
    "And the pair of us look up, surprise on our faces."
    "Standing there in the open doorway is Lavish."
    "She has a similar look on her face too."
    mike.say "Lavish, wait..."
    mike.say "I can explain..."
    hide lavish with moveoutleft
    "Before I speak another word, Lavish turns and flees the scene."
    "I can't exactly leap up and run after her."
    show spank shiori marks ready
    "I'm pinned under Shiori right now."
    "And it'd hardly be fair to dump her onto the floor."
    play sound door_slam
    "But at least I have the small comfort of the door slamming closed in Lavish's wake."
    shiori.say "Erm..."
    shiori.say "[hero.name]..."
    shiori.say "Do I still have to let you spank me?"
    mike.say "Ah...no, Shiori."
    mike.say "I think we can leave it there, okay?"
    hide spank
    show shiori embarrassed blush
    with fade
    "Shiori gets up from my lap and begins to make herself look presentable."
    "But I hardly notice what she's doing, my mind already awash with new worries."
    hide shiori with easeoutleft
    "How am I going to explain myself to Lavish?"
    "And is she even going to want to hear me out?"
    $ DONE["lavish_spanking_start"] = game.days_played
    $ hero.replace_activity()
    $ lavish.flags.spankingdelay = TemporaryFlag(True, 2)
    $ shiori.sub += 1
    return

label lavish_spanking_alternate_start:
    "You know that feeling that you get when you think you're being watched, a weird sensation of someone's eyes being on you without your knowledge?"
    "You'll just be sitting there, like I happen to be at my desk, when the hairs on the back of your neck stand up and you can't shake it off, no matter how hard you try."
    "In the end, you have no choice but to see if your hunch is correct, and so eventually I have to stop what I'm doing and look up before I go crazy."
    "I'm glad that I manage to keep myself from jumping out of my seat when I see that my suspicions were correct after all."
    show lavish at top_mostleft with dissolve
    "Because there's Lavish, standing in the doorway to my office, looking as shy and innocent as she always does."
    "I swallow in order to clear my throat before I ask her what's up."
    mike.say "Yes, Lavish - was there something that you wanted me for?"
    show lavish blush
    "At this, she seems to flush with colour just a little, which is odd."
    "But I just decide to write it off as being on account of her shyness."
    "And when she opens her mouth to speak, I simply assume she needs a moment to collect her thoughts."
    "Wanting to give her all the space she needs, I glance down at what I was working on before she turned up and wait for her to explain herself."
    show lavish -blush
    "But after almost an entire minute has passed with not even a single word emerging from Lavish's mouth, I look up again."
    mike.say "Were you actually going to say something, Lavish?"
    mike.say "Because if you're just planning on standing there and saying nothing, would you mind doing it elsewhere?"
    show lavish surprised at hshake
    "At this, Lavish yelps and shakes her head whilst waving her hands."
    lavish.say "No...no...I want to ask you something."
    show lavish embarrassed
    lavish.say "But, I'm not sure how..."
    menu:
        "Wave her out":
            mike.say "I'm pretty busy right now."
            show lavish surprised
            mike.say "So come back when you know how or what to ask!"
            $ lavish.love -= 3
            $ lavish.sub += 1
            $ hero.cancel_event()
            return
        "Take a deep breath and listen to her":
            "I offer her what I hope is my best approachable boss smile, trying to remember all of the courses that I've been forced to attend for just such a moment as this."
            "Hopefully I can look and sound sincere, and not make it obvious that I thought they were all just so much touchy-feely bullshit."
            mike.say "That's okay, Lavish - you should know that you can come to me with any problems that you have."
            mike.say "My office door is always open, even if you just want someone to talk to."
            mike.say "You know that, right?"
            show lavish normal at left with ease
    "Lavish offers me a weak smile, clearly trying to show her appreciation for my words."
    "But she's still not opening up about whatever it is that's bugging her."
    mike.say "Lavish, is this work-related, or something to do with your private life?"
    mike.say "We can talk about it either way, but it'd help me to know if you want to speak to me as your boss or a friend."
    "That was one of those questions they teach you to ask, the kind that are supposed to make things more simple."
    "But all it seems to do here is make Lavish look all the more confused."
    show lavish embarrassed
    lavish.say "Oh, [hero.name] ... I don't think I know which one it is!"
    "I'm steadily running out of ideas here, and the last thing that I want is to end up getting frustrated with a colleague that genuinely needs my help."
    "That kind of thing would look really bad on my next quarterly review!"
    mike.say "Well, I think what we need to do here, Lavish, is to figure out just which of those it actually is, okay?"
    show lavish normal at left4 with ease
    "She nods meekly, beginning to look more hopeful as I take charge of the conversation."
    mike.say "I think that you should just go ahead and tell me what's on your mind."
    mike.say "And then we can decide what we should do about it."
    show lavish flirt at center with ease
    "At this, Lavish bites her lip, but seems to find her courage as she opens her mouth to speak."
    lavish.say "It's...it's to do with Audrey...and Shiori too."
    "Ah, now we're getting somewhere - maybe she's just jealous of the perks the other girls in the office are enjoying?"
    "Or maybe they're just being complete bitches to her behind my back?"
    "And there I was thinking that this was going to be a complicated pain in the arse to deal with!"
    mike.say "What's the problem, Lavish?"
    mike.say "I promise that whatever you have to tell me, it won't go beyond these four walls."
    show lavish embarrassed
    "She looks at me for a moment, and then almost tears her eyes away again, as though she simply can't hold my eye for more than a second."
    "My previous belief that I was getting a handle on this and a simple solution was within reach is now rapidly slipping away."
    "I stand up and reach over my desk to take Lavish's hand."
    mike.say "Please, you can tell me - whatever it is."
    lavish.say "I...I know all about what you've been doing with Audrey and Shiori, right here in this office."
    show lavish normal
    lavish.say "They keep on telling me that they're taking down letters for you and all that kind of stuff."
    lavish.say "But I peeked through the blinds the other day..."
    show lavish blush
    lavish.say "I know, [hero.name] ...I know that you're spanking them both!"
    "Oh shit, oh shit, oh shit!"
    "And did I just mention - oh shit!"
    "I'm already preparing every ridiculous excuse that I can cook up and wondering what price she's going to demand for her silence."
    "But when she doesn't come straight out and say it, I begin to wonder if she's leaving me to stew in an attempt to gain more leverage than she already has."
    mike.say "Okay, Lavish...now that I know that you know - what exactly is it that you want from me?"
    "Here it comes, the moment of truth!"
    show lavish embarrassed
    lavish.say "I...I want...to be treated the same as the other girls in the office."
    mike.say "You what?!?"
    show lavish normal
    lavish.say "I want you to spank me too!"
    "Of all the possible things that I could have imagined her saying, suffice to say that was not at the top of the list..."
    menu:
        "Don't spank her":
            "Is this actually happening to me?"
            "Has a stunningly beautiful girl the likes of Lavish actually just walked in here and genuinely asked me to spank her on a regular basis?"
            "I can almost feel my reason deserting me as I contemplate the idea, and find that it's obviously appealing, to say the least!"
            "But then I remember just how Lavish came to be here, and I begin to wonder if I might not be getting too hasty."
            "After all, spanking one girl at work is risky, and two is getting to be a handful."
            "Adding a third would be like spinning plates..."
            mike.say "Ah...I don't think that would be such a good idea, Lavish."
            "Instantly she looks crushed, seeing that the effort to which she's gone to come so far wasted in just a few short words."
            show lavish annoyed
            lavish.say "But...why?"
            if audrey.flags.nickname == "toy":
                mike.say "Well, Lavish...you have to understand that what's going on between myself and my Toy..."
            else:
                mike.say "Well, Lavish...you have to understand that what's going on between myself and Audrey..."
            lavish.say "And Shiori."
            mike.say "Yes, thank you...and Shiori...is, well...it's pretty unique."
            "Lavish cocks her head on one side at this, as if she doesn't quite understand my explanation."
            mike.say "You see, it's not like I just wander around the office, spanking people at random, you know?"
            mike.say "I mean, imagine if that were the case!"
            show lavish bored
            "Lavish says nothing, simply staring at me with that same innocent, uncomprehending expression on her face."
            "I realise that I'm beginning to babble, and that I need to put this matter to bed as soon as possible, before I say something that we'll both regret."
            mike.say "So, now that we've cleared that one up - was there anything else that you needed me for, Lavish?"
            "Still looking more than a little confused, Lavish nevertheless shakes her head and turns to go."
            "I have to admit to being more than a little confused myself."
            "And to not knowing if I handled that situation well, or handled it at all..."
        "Spank her":
            "Is this actually happening to me?"
            "Has a stunningly beautiful girl the likes of Lavish actually just walked in here and genuinely asked me to spank her on a regular basis?"
            "I can almost feel my reason deserting me as I contemplate the idea, and find that it's obviously appealing, to say the least!"
            mike.say "Hmm...I don't know, Lavish."
            "It's all that I can do to keep from sounding elated as I say this."
            if audrey.flags.nickname == "toy":
                mike.say "You have to understand that what I have going on with my Toy and Shiori is a very rare and unusual form of office discipline."
            else:
                mike.say "You have to understand that what I have going on with Audrey and Shiori is a very rare and unusual form of office discipline."
            mike.say "Apart from the three of us, you're the only other person that even knows about it."
            mike.say "And if you speak as much as a word about it to anyone else, we'll all flat out deny it too."
            "Lavish nods, looking very much in earnest and hanging on my every word."
            mike.say "So if I were to let you in on this, then you'd have to swear to keep it a secret as well."
            "Part of me can't actually believe what I'm asking of her right now."
            "I'm promising to let her in on the spanking action happening in my office, but solely on the understanding that she keeps her mouth shut as a condition!"
            "Any moment I expect her to call my bluff and tell me where I can shove it."
            show lavish happy
            "But much to my amazement, she responds by nodding eagerly as her face breaks into a broad and genuine smile."
            lavish.say "Oh, thank you, [hero.name], thank you so much!"
            show lavish wink
            lavish.say "And don't you worry - I'll be sure to keep this all a secret."
            lavish.say "You just see if I don't!"
            hide lavish with easeoutleft
            "And with that, she turns her back and hurries out of my office, leaving me alone once more."
            "I shake my head as I get back to what I was doing before Lavish turned up, scarcely able to believe my luck."
            "I'm working with not one, or two, but three stunning girls every day of the working week."
            "And every one of them is reporting to my office for spanking on a regular basis!"
            "What did I do in a former life in order to deserve this?"
            $ lavish.flags.start_spanking = True
            if lavish.sub.max < 70:
                $ lavish.sub.max = 70
            $ lavish.flags.spankingdelay = TemporaryFlag(True, 3)
    $ hero.replace_activity()
    return

label lavish_spanking_1:
    "I've been dreading the task of speaking to Lavish ever since she walked in on Shiori and me."
    "I mean, how do you go about explaining to the girl that you're dating what she just saw?"
    "Not only was I literally spanking another girl, it was one of her colleagues too!"
    "I'm honestly expecting her to refuse to talk to me the next time I see her."
    "That or coldly inform me that she's referred the matter to the HR department."
    "But when I finally get her alone, Lavish surprises me..."
    show lavish bored
    mike.say "Ah..."
    mike.say "Hey, Lavish..."
    mike.say "I guess I'm not your favourite person right about now, huh?"
    "Lavish crosses her arms and cocks her head on one side at this."
    "She regards me with a look of curious interest on her face."
    "Kind of like the way she might study a fascinating bug under a magnifying glass."
    lavish.say "Hmm..."
    lavish.say "Let's just say that I'm surprised, [hero.name]."
    lavish.say "That wasn't the kind of thing I'm used to seeing in the workplace!"
    mike.say "Look, Lavish..."
    mike.say "If you're mad, I understand."
    mike.say "You have every right to be angry with me."
    "Lavish lets out a snort of frustration at this."
    "She shakes her head, still amazing me by not getting angry."
    lavish.say "I was at the time...angry, that is."
    show lavish annoyed
    lavish.say "And I seriously thought about dumping your ass!"
    lavish.say "That and letting human resources know what you're getting up to on company time."
    "Lavish pauses and I see her expression change."
    "For the first time her irritation seems to pass."
    "And she looks genuinely interested in asking me something."
    show lavish normal
    lavish.say "But then I remembered that you're a guy."
    lavish.say "And guys are pretty weak-willed around that kind of thing."
    lavish.say "Also you're smart, for a guy at least."
    lavish.say "So you're not stupid enough just to be indulging yourself like that."
    show fx question
    lavish.say "There must be something more to it, right?"
    "My heart leaps as Lavish asks the question."
    "I can already sense that she's offering me a way out of this mess!"
    "But before I take it, I pause to consider what she's actually asking me."
    "Sure, I was getting off on spanking Shiori - who wouldn't?"
    "But I also wasn't getting anything done before we got into it."
    "Maybe that's the real reason I was so into it?"
    "Or at least a better explanation than me being a pervert!"
    mike.say "Sure, it's fun, Lavish."
    mike.say "But you know how Shiori can be."
    mike.say "She's always overthinking things, never focused on the job."
    mike.say "Believe it or not, what we were doing helps to keep our heads in the game."
    mike.say "Look, I know it's a little kinky."
    mike.say "But try to think about it in a mature way."
    mike.say "It's really more about thinking outside the box than anything else."
    show lavish annoyed
    "Lavish frowns a little."
    "But I can see that she's thinking it over."
    lavish.say "I had noticed Shiori coming and going from your office."
    lavish.say "And she was always behaving like her ass was tender afterwards."
    lavish.say "I kept watching her because I was keen to see what the problem was."
    lavish.say "But her performance did pick up once she'd been in to see you..."
    "I nod eagerly, keen too confirm Lavish's suspicions."
    mike.say "If it were another girl, I'd never think of spanking her."
    mike.say "But Shiori just doesn't respond well to anything else."
    mike.say "Give her a pep-talk and it just goes in one ear and out the other!"
    "Lavish nods too, as if she's come to a decision."
    show lavish normal
    lavish.say "You're right, [hero.name]."
    lavish.say "I need to expand my horizons, accept new ways of thinking."
    show lavish embarrassed
    lavish.say "And that's why I'd like you to start spanking me too."
    lavish.say "Are you willing to do that?"
    "I can't help blinking and shaking my head."
    mike.say "Y...you want me to..."
    mike.say "To spank you in my office too?!?"
    lavish.say "That's what I said, isn't it?"
    mike.say "Yeah, Lavish - I just needed to hear you say so again."
    mike.say "Sure thing...I can start spanking at your convenience!"
    show lavish flirt
    lavish.say "That's great, [hero.name]."
    lavish.say "I'll let you know when I need it done!"
    "Did that conversation actually just happen?"
    "Did Lavish actually ask me to start spanking her?"
    "Wow...I hope I don't wake up and find this was all some crazy dream!"
    if lavish.sub.max < 70:
        $ lavish.sub.max = 70
    $ lavish.flags.spankingdelay = TemporaryFlag(True, 3)
    $ lavish.flags.start_spanking = True
    return

label lavish_spanking_2:
    "It's been a while since Lavish asked me to start spanking her at work like I was already doing with Shiori."
    "And I was pretty sure that she was enjoying our little sessions snatched at various times during the day too."
    "That's why it catches me off-guard when she brings the subject up out of the blue..."
    show lavish annoyed
    lavish.say "Erm..."
    lavish.say "[hero.name]..."
    mike.say "Yeah, Lavish?"
    mike.say "Did you want to ask me something?"
    mike.say "Are you aching to go over my knee again already?"
    "At the mere mention of spanking, I see Lavish's cheeks flush red."
    show lavish embarrassed
    "And I can't help thinking that I've said the wrong thing."
    lavish.say "Well..."
    lavish.say "It's about that, actually..."
    lavish.say "About the spanking..."
    "I feel my mood change at the way Lavish says those words."
    "Surely the tone of her voice can only mean bad things are about to be said!"
    mike.say "What about the spanking, Lavish?"
    mike.say "I thought you were getting a lot out of it?"
    mike.say "I mean, you've been on target like a laser-beam recently!"
    mike.say "But if you've changed your mind...I understand."
    show lavish embarrassed blush
    "Lavish shakes her head at this."
    "And she looks more embarrassed than ever."
    lavish.say "Oh dear..."
    lavish.say "It's not that at all!"
    show lavish flirt -blush
    lavish.say "I love the spanking, [hero.name]."
    lavish.say "And it's been keeping me focused on my work like never before!"
    mike.say "Then I don't understand, Lavish."
    mike.say "What are you trying to tell me?"
    mike.say "That you need me to spank your more?"
    mike.say "To spank you even harder?"
    "At this, Lavish makes the strangest sound."
    show lavish annoyed
    "It's like a squeak of something being desperately suppressed."
    lavish.say "Oh no..."
    lavish.say "Please don't talk like that!"
    lavish.say "Just the idea of it...it's almost too much!"
    mike.say "Y...you mean?"
    lavish.say "Yes, [hero.name]..."
    show lavish flirt
    lavish.say "I...I think I'm addicted to being spanked!"
    lavish.say "I want it more with every day that passes."
    lavish.say "And I don't care whether it's at work or if it helps me focus at all!"
    lavish.say "I just want to be spanked for the sake of being spanked!"
    "Lavish holds her hands up to her mouth."
    "As if she's shocked by her own admission."
    lavish.say "Oh, I'm sorry, [hero.name]!"
    show lavish normal
    lavish.say "I thought I could handle it - really I did."
    lavish.say "But I think I'm turning into some kind of wanton whore!"
    lavish.say "Sometimes, all I can think about is you spanking my buttocks!"
    show lavish flirt
    lavish.say "My firm, round buttocks..."
    mike.say "OKAY..."
    mike.say "Okay, Lavish..."
    mike.say "I get the picture!"
    "I take a deep breath and try to choose my next words with care."
    "Of course I'm more than pleased to hear Lavish's confession."
    "But I can't let her think that I'm unsympathetic or taking advantage."
    mike.say "Don't worry, Lavish."
    mike.say "I'll do all that I can to help."
    mike.say "Admitting you have a problem is the first step on the road to recovery."
    mike.say "I'll make sure that you get your spanking, at work or anywhere else."
    "Lavish throws her arms around me, nestling her head into my shoulder."
    "I put my arms around her too, pulling her into a tight hug."
    show lavish happy
    lavish.say "Oh, thank you!"
    lavish.say "You're such a great guy, [hero.name]!"
    lavish.say "But do you think you can still love me?"
    lavish.say "Now that you know I'm a wanton slut?"
    mike.say "I don't know, Lavish."
    mike.say "But I'm going to try with all my heart!"
    $ lavish.love += 2
    if lavish.sub.max < 100:
        $ lavish.sub.max = 100
    return

label lavish_sub_03:
    scene expression f"bg {game.room}"
    "It's just another one of those days and another one of those meetings."
    "You know the kind that I mean, right?"
    "The ones that afterwards you won't be able to remember what was said."
    "The ones that just merge together with all the other boring work meetings you've sat through."
    show lavish zorder 3 at center, zoomAt(1.20, (340, 800))
    show audrey annoyed zorder 1 at center, zoomAt(1.1, (860, 950))
    show shiori annoyed zorder 2 at center, zoomAt(1.15, (1100, 950))
    with fade
    "Thankfully this one just involves Lavish, Audrey, Shiori and myself."
    "But it's still a tedious affair, dragging on longer than it need to."
    "Lavish is doing most of the talking."
    show lavish at center, zoomAt(1.20, (320, 800)) with ease
    "But her words are beginning to lose all meaning for me."
    "Instead I'm becoming ever more focused on the movement of her lips."
    show lavish at center, zoomAt(1.20, (360, 800)) with ease
    "Occasionally I catch a glimpse of her tongue between them too."
    "And it's making me think of things far more fun than work..."
    show lavish annoyed at center, zoomAt(1.20, (340, 800)) with ease
    lavish.say "Are you even listening to me right now, [hero.name]?"
    mike.say "Huh..."
    mike.say "What was that, Lavish?"
    show lavish b angry
    "Lavish crosses her arms and shakes her head at me."
    "And I can see the look of disapproval in her eyes."
    lavish.say "I knew it!"
    lavish.say "I just knew you weren't paying attention to me!"
    show shiori embarrassed at startle
    shiori.say "Oh dear..."
    shiori.say "You do go on a little, Lavish."
    shiori.say "And I don't think you should be talking to [hero.name] like that either!"
    show audrey normal
    audrey.say "Shiori's got a point, Lavish."
    audrey.say "For all I care, you can talk to [hero.name] however you like."
    audrey.say "But you're gonna put us all to sleep if you go on much longer!"
    "Lavish doesn't hesitate to turn her attention to her colleagues."
    "Evidently she was expecting more support from them than she's getting!"
    show lavish angry
    lavish.say "Whatever happened to solidarity in the workplace?"
    lavish.say "You guys should be on my side, not his!"
    "I can see that the meeting's in danger of descending into chaos."
    "That is unless I step up and assert my authority over the situation."
    "But how should I go about doing it?"
    "A moment later I remember how Lavish has been responding to me asserting myself in other ways."
    "And I wonder if the same kind of treatment would work in this situation too."
    "I know that Shiori's too submissive to speak out about what I have in mind."
    "On the other hand, Audrey's the kind of girl that would actually love it."
    "So what the hell - here goes nothing..."
    mike.say "Okay, Lavish..."
    mike.say "I'm going to have to pull rank on you right there."
    show lavish surprised at startle
    lavish.say "What the..."
    mike.say "Ah...no, Lavish, I mean it!"
    mike.say "I think this meeting is in need of a new direction."
    mike.say "That's why I'm suggesting that we drop the current topic."
    mike.say "And that you suck my cock instead, okay?"
    "At this, the room falls completely silent."
    "You could hear a pin drop or a mouse fart."
    "Lavish stands as still as stone, still staring at me."
    show audrey surprised at startle
    show shiori surprised at startle
    "At the same time, Shiori and Audrey exchange astonished glances."
    show lavish annoyed
    lavish.say "Y...you're not serious!"
    lavish.say "[hero.name]...you have to be joking!"
    "I shake my head slowly."
    mike.say "No, Lavish."
    mike.say "I'm one hundred percent serious."
    mike.say "I want you to be a good girl and obey me."
    mike.say "Just like you do when I bend you over my knee and spank you."
    mike.say "You're going to suck my cock, right here and now, in front of Audrey and Shiori."
    "Lavish blinks repeatedly, looking at the door and then back to me."
    "I can sense the battle that must be raging inside her head right now."
    "On the one hand she wants to assert herself and defy me."
    "But on the other she's already accepted me as a figure of authority."
    "And that means that she sees pleasing me as a means of advancement."
    "I don't say a word, just push my chair back from the table."
    "Which seems to be the thing that makes something inside of Lavish snap."
    show lavish flirt
    "Without warning, she drops all pretence of defying me."
    show lavish zorder 3 at center, zoomAt(1.65, (640, 1150)) with vpunch
    "Lavish literally rushes over to where I'm sitting."
    show lavish at center, zoomAt(1.65, (640, 1350)) with move
    "One there, she falls onto her knees and fumbles with my flies."
    "Audrey and Shiori look on in stunned amazement as she pulls my cock out."
    scene lavish bj
    show lavish bj office
    with fade
    mike.say "That's right, Lavish."
    mike.say "There's a good girl!"
    "Lavish doesn't say anything in response."
    "Instead she nods, making a desperate whimpering sound."
    "And then she parts her lips, beginning to lick at the base of the shaft."
    show lavish bj hold
    "While she's eager, Lavish isn't in the least bit sloppy."
    "She approaches a blowjob in the same way she does any task."
    "In that I mean she's meticulous and gives it all she has."
    "Lavish works my cock from the base upwards."
    show lavish bj pleasure
    "She makes every inch of progress feel better than the last."
    "I couldn't get harder, even with her tongue and lips caressing me."
    "In fact, she's so good at it that I don't look up until she reaches the top."
    "It's then that I'm suddenly reminded we're not alone."
    show lavish bj tip blow
    "As Lavish swallows the head of my cock, I find myself looking at Audrey and Shiori."
    "I can see them over the top of Lavish's bobbing head."
    "Both of them are watching the show in silent fascination."
    "Shiori looks like she's the most shocked of the pair."
    show lavish bj deep pleasure
    show sexinserts head lavish zorder 1 at center, zoomAt(1, (720, 760))
    "But I can see the hints of arousal in her eyes all the same."
    "And I know that she's imagining herself in Lavish's position."
    "Audrey, on the other hand, is openly smiling and nodding at what she sees."
    "I can guess that she thinks Lavish looks down on the other girls in the office."
    show lavish bj tip
    "And so seeing lavish on her knees and with a cock in her mouth must be a source of delight."
    "For my part, having them as an audience makes the sensation that much sweeter."
    "It feels good to be the one in control of the situation."
    show lavish bj deep
    "And I can sense a growing buzz of power and authority inside of me."
    "Because if I can pull off something like this without them protesting - what else can I do?"
    "My thoughts are curtailed a moment later as I feel myself starting to cum."
    show lavish bj tip
    "Quickly I make a decision and then act upon it."
    menu:
        "Cum in her mouth":
            "I feel the need to draw a line under what I've made Lavish do so far."
            show lavish bj normal
            "And having her swallow seems to be the perfect way to end it."
            show lavish bj tip
            "So I take hold of her head, making sure that she can't escape."
            show lavish bj creampie pain
            show sexinserts head lavish cum zorder 1 at center, zoomAt(1, (720, 760))
            with hpunch
            "Lavish's eyes almost pop out of her head as I shoot my load."
            show lavish bj cumshot pain with hpunch
            "She coughs and almost gags, but then manages to recover."
            show lavish bj cumshot pain with hpunch
            "All she can do is swallow down everything I shoot into her mouth."
            hide sexinserts
            show lavish bj pleasure
            "And when I finally pull my cock out again, she gasps for breath."
            show lavish bj normal
            "Strings of cum dripping off of her chin the whole time."
        "Cum on her face":
            "I feel the need to draw a line under what I've made Lavish do so far."
            "And painting her face seems to be the perfect way to end it."
            show lavish bj tip out normal
            hide sexinserts
            "I pull my cock out of Lavish's mouth just before I cum."
            "But not soon enough for her to be able to know what's going on."
            "She stares up at me, wide-eyed and with an open mouth."
            show lavish bj cumshot pain with hpunch
            "And a second later I shoot my load straight into her unsuspecting face."
            with hpunch
            "Stripes of sticky, white cum paint lines across her cheeks and nose."
            show lavish bj cum onface -cumshot with hpunch
            "Some even lands in her mouth, and she can't help but swallow it down."
    show lavish bj normal
    "I leave Lavish on her knees, cleaning herself up while I make myself decent."
    scene expression f"bg {game.room}"
    show audrey flirt blush at right5
    show shiori embarrassed blush at mostright5
    with fade
    "Standing up, I treat Audrey and Shiori to a knowing smile."
    mike.say "I think that just about wraps things up for now."
    mike.say "Let me know if anything else comes up, okay?"
    shiori.say "Oh..."
    show shiori normal
    shiori.say "Of course, [hero.name]!"
    show audrey normal
    audrey.say "Sure thing, [hero.name]."
    audrey.say "You got it!"
    "I allow myself one last smirk as I walk out of the room."
    scene bg breakroom with fade
    "And part of me wishes that I could hear the conversation that follows."
    "But I'm still gloating at how things turned out in there."
    "Which is more than enough for me."
    $ game.room = "breakroom"
    $ lavish.sub += 3
    $ audrey.sub += 1
    $ shiori.sub += 1
    return

label lavish_birthday_date_male:
    $ DONE["lavish_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg street
    "I pull up outside of Lavish's place at the appointed time and sound the horn."
    "And I only have to wait a minute or so before she comes hurrying out to meet me."
    "I can see that she has a smile on her face, like she's eager to be off."
    "But when I look at what she's wearing, that's a little less reassuring."
    "I convinced Lavish to come along with me on a camping trip to the woods."
    "And more importantly, all for the sake of celebrating her birthday."
    show lavish casual with dissolve
    "But she looks more like she's going for a stroll in the park!"
    show lavish happy
    lavish.say "Hey, [hero.name]..."
    show lavish normal
    lavish.say "I got all the stuff you told me I'd need."
    lavish.say "Right here in this bag..."
    show lavish bored
    show fx question
    lavish.say "Erm...why are you looking at me like that?"
    lavish.say "Did I do something wrong?"
    hide fx
    menu:
        "It's okay Lavish, don't worry about it":
            "To me it looks like Lavish didn't take my advice."
            "I told her to go to the army surplus store for her gear."
            "But I'm going to bet she went straight to the mall instead."
            "Straight to a designer store where they sold her expensive crap!"
            "But I obviously can't tell her that."
            "Because I want this trip to come off."
            mike.say "No, Lavish..."
            mike.say "It looks like you got most of it."
            mike.say "But there's a few things missing."
            mike.say "I guess I forgot to mention those."
            show lavish normal
            $ game.active_date.score += 15
            "I can see that my word have had the desired effect."
            "Lavish looks relieved and nods her head."
            "Evidently accepting that the mistake is probably mine."
            show lavish annoyed
            lavish.say "But what about the things I don't have?"
            show lavish sad
            lavish.say "Are we going to have to call the trip off?"
            mike.say "No, Lavish."
            mike.say "You can just share my gear."
            mike.say "I'm sure we can manage for one night."
            show lavish normal
            $ lavish.love += 2
            "Thankfully, that seems to settle the matter."
        "You are not prepared at all...":
            show lavish surprised
            mike.say "Where did you go to get all of that stuff, Lavish?"
            mike.say "It doesn't look like it came from the army surplus store."
            mike.say "Which I think is where I told you to go, right?"
            show lavish sad
            "Lavish looks more than a little embarrassed."
            "She stares down at her feet, like a kid being told off by an adult."
            lavish.say "Well..."
            lavish.say "I thought the stuff at the army surplus store looked..."
            lavish.say "Kind of cheap and nasty, yeah?"
            show lavish sadsmile
            lavish.say "So I went to one of the designer stores at the mall instead."
            lavish.say "The sales assistant told me this was the best I could get."
            lavish.say "And that's why it was so expensive."
            "Lavish looks up at me with a helpless smile."
            "And I can't help feeling sorry for her."
            mike.say "Ah...actually it's the other way round, Lavish."
            mike.say "The designer stuff wears out real quick."
            mike.say "And the army surplus stuff lasts for a lifetime."
            show lavish sad
            $ game.active_date.score -= 10
            lavish.say "Oh dear..."
            lavish.say "This is my first time camping."
            lavish.say "And I've already messed up!"
            mike.say "No, Lavish!"
            mike.say "Don't worry about it."
            mike.say "I'll make sure you get the hang of it."
    scene black
    play sound car_door
    pause 0.4
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "Lavish opens the passenger door and hops in beside me."
    scene bg map with fade
    "And in a few short minutes we're on the road and heading out of the city."
    "I know these roads pretty well myself, from camping trips with my folks."
    "But I know that Lavish is pretty much new to the idea of doing things in the outdoors."
    "It may not be the wilderness, granted."
    "But I keep on trying to remind myself how scary the woods can be to someone unused to them."
    "On the drive I keep pointing out the best views to Lavish."
    "Though I get the impression it's all just one mass of green to her eyes."
    "Soon enough we pull up in the carpark at the trailhead."
    scene bg forest with fade
    mike.say "Here we are, Lavish..."
    mike.say "This is where our adventure begins!"
    lavish.say "If you say so, [hero.name]."
    lavish.say "But I'm still not sure this is better than a night in a four star hotel!"
    mike.say "Trust me, Lavish."
    mike.say "You'll see a lot more than four stars when sun goes down and the moon comes out!"
    "Lavish still doesn't look convinced."
    play sound car_door
    pause 0.4
    show lavish casual with easeinleft
    "But she gamely gets out of the car and shoulders her backpack."
    lavish.say "Okay..."
    show lavish normal
    lavish.say "So what do we do now?"
    lavish.say "Program our destination into your satnav?"
    "I can't help laughing at the suggestion."
    mike.say "No need for that."
    mike.say "I know this trail like the back of my hand."
    "I hold up my hand to make the point."
    "But then I stare at it in surprise."
    mike.say "Will you look at that?"
    mike.say "I never knew that mole was there before!"
    show lavish surprised
    "I see panic in Lavish's eyes."
    "So I shake my head as quickly as I can."
    mike.say "Kidding!"
    mike.say "I was only kidding!"
    mike.say "I really do know the way."
    mike.say "But we do have a choice to make."
    show lavish normal
    mike.say "There's two places we can camp on the trail."
    mike.say "One's a long hike away, but the views are amazing."
    mike.say "The other's a lot closer, but the scenery is more kinda...meh!"
    lavish.say "But if we choose the closer one, then we have more time once we get there."
    lavish.say "Then we can settle in and really get comfortable, yeah?"
    menu:
        "Still, let's camp far":
            "I shake my head, dismissing Lavish's concerns."
            mike.say "Well, I say that it's longer..."
            mike.say "But it's not really that long at all."
            mike.say "Come on, Lavish..."
            mike.say "The sooner we get going, the sooner we get there."
            show lavish annoyed
            "I set off walking before Lavish has the chance to object."
            "So the only choice that she really has is to follow me."
            "And I'm sure to set a vigorous pace too."
            "Because I want to make good on my claim that it's not too far."
            scene bg forest
            show lavish casual yawn
            with fade
            "Along the way I even make a sure to point out all of the best views."
            "But by the time we actually get to the camping site, Lavish is exhausted."
            "She all but collapses as soon as I declare that we've arrived."
            show lavish upset
            $ game.active_date.score -= 10
            "And I can feel her shooting me an annoyed glance."
            "Which I have no choice but to ignore as best I can."
        "You're right, let's camp close":
            "I think about it for a moment."
            "And then I shrug my shoulders."
            mike.say "I guess we could take the easier route."
            mike.say "Don't want to put too much pressure on the newbie!"
            mike.say "Are you ready?"
            show lavish happy
            $ lavish.love += 2
            "Lavish nods eagerly."
            "And I can see the look of relief on her face."
            "We set off walking down the trail."
            "And we take the easier branch as soon as it appears."
            scene bg forest
            show lavish casual yawn
            with fade
            "Sure, the walk is shorter and the views not as impressive."
            "But we make it to the campsite in record time."
            show lavish normal
            $ game.active_date.score += 15
            "And neither of us is exhausted when we do."
            "So I'm going to count that as a win."
    scene bg forest with fade
    "The first job is to pitch the tent, which I do as Lavish watches me."
    scene bg forest at dark with dissolve
    "And then I start to arrange rocks in a circle to accommodate the fire."
    show lavish normal at center, zoomAt(1.25, (640, 940)) with dissolve
    "This seems to interest Lavish more, and she comes closer as I work."
    "Then it strikes me that this would be a good chance to get her involved."
    "A chance to teach her some real outdoor skills."
    menu:
        "Show Lavish how to make a fire":
            show lavish surprised
            mike.say "Hey, Lavish..."
            mike.say "You might want to watch this."
            mike.say "You know, pick up some tips on starting a fire?"
            show lavish normal at center, zoomAt(1.5, (640, 1040))
            "Lavish nods and leans in closer."
            "And from that point on she watches me closely."
            "From time to time I stop to explain something to her."
            "And more than once she interrupts to ask me a question."
            "Soon I have the fire built and ready to be lit."
            "That makes me feel like I've accomplished something."
            $ game.active_date.score += 10
            "As does the knowledge I've passed on to Lavish too."
        "Ask help from Lavish to light the fire":
            show lavish surprised
            mike.say "Hey, Lavish..."
            mike.say "Come help me build the fire."
            show lavish sad
            "Lavish shakes her head at this."
            lavish.say "Oh no..."
            lavish.say "I wouldn't know where to start!"
            mike.say "Not unless someone shows you!"
            show lavish bored
            "At first I don't think Lavish is going to relent."
            "But then she nods and hurries over to my side."
            "I go slowly, explaining each step to her in detail."
            show lavish normal
            "And together we collect the firewood."
            "Then we stack it in the middle of the stone circle."
            "Finally I let Lavish light the fire."
            show lavish happy
            $ game.active_date.score += 25
            "And as it sparks into life, it illuminates her face."
            "Showing me the glow of genuine achievement in her features."
    scene bg forest at center, zoomAt(1.5, (940, 940)), dark
    show lavish normal at center, zoomAt(1.5, (640, 1140))
    with fade
    "With the fire lit, we can sit back and relax for a moment."
    show lavish surprised
    "But once we do, it doesn't take long for my stomach to growl."
    "In fact it's so loud that Lavish hears it too!"
    lavish.say "Oh my!"
    show lavish normal
    lavish.say "And I thought I was getting hungry."
    mike.say "Yeah..."
    mike.say "Sorry about that!"
    mike.say "I guess it's time I busted out some food."
    "I reach into my backpack to get some of the supplies I brought."
    "And once glance at the fire tells me exactly how we should cook it too."
    mike.say "Time for an essential part of the camping experience, Lavish!"
    mike.say "Wieners and marshmallows!"
    mike.say "Great roasted over an open fire."
    lavish.say "Ooh!"
    lavish.say "Which are we having first?"
    menu:
        "Wieners first!":
            mike.say "Wieners, Lavish..."
            mike.say "It's always got to be wieners first!"
            "I start skewering the sausages on sticks."
            "And then I hand one to Lavish."
            show lavish flirt
            "But as I do so, I can clearly see that she's smirking."
            "She takes the stick with a nod and a smile."
            lavish.say "I thought so, [hero.name]."
            lavish.say "You always struck me as a wiener guy!"
            lavish.say "Like you couldn't wait to get your hands on one!"
            "I frown as I start to hold my own stick over the fire."
            mike.say "Okay, Lavish, very funny."
            mike.say "You made the cheapest joke possible."
            mike.say "Now can we at least try to behave like adults?"
            show lavish happy
            $ game.active_date.score += 10
            "Lavish nods as she begins to roast her wiener too."
            "But I can still hear her sniggering under her breath the whole time."
        "Marshmallows first!":
            mike.say "Marshmallows, Lavish..."
            mike.say "It's always marshmallows first!"
            "I start skewering the marshmallows on sticks."
            "And then I hand one to Lavish."
            "She stares at it with genuine interest."
            show lavish happy
            "Then she looks up at me and smiles."
            lavish.say "I never toasted a marshmallow before."
            lavish.say "I've seen people do it in movies and on TV."
            lavish.say "Like, I must have seen it a million times."
            lavish.say "But I never knew what it actually tasted like."
            mike.say "No time like the present to find out."
            show lavish normal
            "Lavish nods and watches as I start to toast my marshmallow."
            "Then she begins to copy me too."
            "As soon as mine's done, I blow on it and then take a bite."
            "I look up as I do so to see Lavish copying my every move."
            "At least she does until the actually tastes the marshmallow."
            show lavish happy
            $ lavish.love += 2
            $ game.active_date.score += 20
            "And then her eyes widen with sheer delight."
            lavish.say "Mmm!"
            lavish.say "This is so good!"
            mike.say "What did I tell you, Lavish?"
            mike.say "Camping definitely has it's perks!"
    show lavish normal
    lavish.say "So is this camping trip my birthday present?"
    lavish.say "Or are you about to surprise me with something else?"
    lavish.say "Because it's okay if the trip is the gift, obviously!"
    if not hero.has_gifts:
        "I could almost slap myself the moment Lavish says those words."
        "Because I was supposed to buy her something before we came out here."
        "But what with all the work that went into preparing, I must have forgotten!"
        "Luckily for me, she gave me an out in what she just said."
        "I feel bad taking it, but what other choice do I have?"
        mike.say "Oh yeah, Lavish..."
        mike.say "The trip is the present!"
        show lavish sadsmile
        $ game.active_date.score -= 20
        lavish.say "Oh..."
        lavish.say "I see..."
        $ lavish.love -= 10
        lavish.say "That's okay then."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_12
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "Oh yeah..."
                mike.say "Thanks for reminding me, Lavish."
                mike.say "What with planning the trip out here..."
                mike.say "I almost forgot!"
                "I say all of this while rummaging around in my backpack."
                "Then I find the gift and offer it to Lavish."
                show lavish happy
                pause 0.5
                play sound [paper_ripping_2, paper_ripping_1]
                "She smiles and takes it from me, carefully removing the wrapping paper."
                if _return:
                    show lavish surprised
                    "But when she sees what's inside, Lavish looks amazed."
                    lavish.say "Oh..."
                    show lavish blush
                    lavish.say "Oh my goodness!"
                    mike.say "What's the matter, Lavish?"
                    mike.say "Is something wrong?"
                    show lavish normal -blush
                    lavish.say "Oh..."
                    lavish.say "Oh no..."
                    show lavish happy
                    $ game.active_date.score += 20
                    lavish.say "It's perfect, just perfect!"
                    "I feel a sense of pride at Lavish's reaction."
                    "Reassured that I know her better than I thought."
                else:
                    show lavish sadsmile
                    "But when she sees what's inside, Lavish looks disappointed."
                    mike.say "What's the matter, Lavish?"
                    mike.say "Is something wrong?"
                    $ game.active_date.score -= 10
                    lavish.say "Oh..."
                    lavish.say "Oh no..."
                    lavish.say "It's very nice."
                    "Lavish does the best she can to hide it."
                    "But I can still tell the gift isn't what she wanted."
            else:
                "I could almost slap myself the moment Lavish says those words."
                "Because I was supposed to buy her something before we came out here."
                "But what with all the work that went into preparing, I must have forgotten!"
                "Luckily for me, she gave me an out in what she just said."
                "I feel bad taking it, but what other choice do I have?"
                mike.say "Oh yeah, Lavish..."
                mike.say "The trip is the present!"
                show lavish sadsmile
                $ game.active_date.score -= 20
                lavish.say "Oh..."
                lavish.say "I see..."
                $ lavish.love -= 10
                lavish.say "That's okay then."
    scene bg forest at dark with fade
    "By now the sun is starting to fall towards the horizon."
    "Night isn't far away, and the temperature is dropping fast."
    scene bg forest night with dissolve
    "Soon even the fire isn't going to be enough to keep us warm."
    scene bg forest night at center, zoomAt(1.5, (940, 940))
    show lavish normal at center, zoomAt(1.5, (640, 1140))
    with fade
    mike.say "Time to head inside the tent, Lavish."
    mike.say "We'll be warmer once we're inside of our sleeping bags."
    "Lavish nods and we begin to get ready to settle down for the night."
    "But it's not like we're going to fall asleep as soon as we're inside of them."
    "There's still time to squeeze a little something in before that happens."
    if hero.has_skill("guitar"):
        mike.say "How about we sing a campfire song, Lavish?"
        mike.say "That's another camping tradition we should tick off the list."
        show lavish casual surprised with dissolve
        lavish.say "Just the two of us singing together?"
        mike.say "Not quite..."
        mike.say "Because I remembered to bring this!"
        "I whip out my guitar and pluck the strings."
        "Then I get ready to sing the first song that comes to mind."
        play music "music/roa_music/healing.ogg" loop
        show lavish normal
        "At first I'm a little rusty."
        "But it doesn't take me long to get the hang of it."
        "And pretty soon I'm belting out every song that I can remember."
        show lavish yawn
        "Lavish listens intently, now joining in."
        "And for the longest time I think she's not going to."
        "But finally she does, and I'm struck by the sound of her voice."
        "Once I've run out of material, I have to comment on it."
        show lavish normal
        mike.say "Lavish..."
        mike.say "I never heard you sing before."
        mike.say "But your voice...it's beautiful!"
        show lavish surprised blush
        "Lavish instantly blushes and waves away my compliment."
        "But I can see that she's touched by it too."
        show lavish embarrassed
        $ lavish.love += 2
        lavish.say "Oh, it's nothing special."
        lavish.say "But if you really do like it..."
        show lavish happy
        $ game.active_date.score += 20
        lavish.say "Then maybe I could sing for you more often."
    elif randint(0, 1) == 0:
        "Now that it's getting late, the exertions of the day are starting to tell on me."
        "The last thing that I want is to fall asleep early and miss out on more time with Lavish."
        "But keeping my eyes open is going to be a tough thing to do."
        "Unless I can find some hidden reserve of energy deep down inside of me."
        if hero.energy >= 4:
            mike.say "Lavish?"
            mike.say "Are you still awake?"
            lavish.say "Huh..."
            show lavish casual yawn with dissolve
            lavish.say "What?"
            "I can't help chuckling as Lavish sits up."
            mike.say "I think you almost fell asleep there."
            show lavish annoyed
            lavish.say "No...I wasn't asleep."
            lavish.say "I was wide awake!"
            mike.say "So you snore when you're awake now?"
            show lavish embarrassed
            "Lavish looks embarrassed for a moment."
            show lavish happy
            $ game.active_date.score += 10
            "But then she laughs it off."
            "And we sit up for a little longer."
            show lavish normal
            "Just talking about this and that."
            "Until we naturally fall asleep."
        else:
            show lavish normal with dissolve
            lavish.say "[hero.name]?"
            lavish.say "Are you still awake?"
            mike.say "Huh..."
            mike.say "Wha..."
            mike.say "I'm awake, Mom!"
            show lavish happy
            "I hear Lavish giggling from the other side of the tent."
            mike.say "Hey..."
            mike.say "I'm awake!"
            mike.say "I wasn't asleep just now."
            show lavish flirt
            lavish.say "So you snore when you're awake?"
            lavish.say "Don't worry about it."
            show lavish normal
            lavish.say "If you're tired, you should sleep."
            $ game.active_date.score -= 10
            lavish.say "I'll be okay..."
            show lavish bored
            show fx question
            lavish.say "[hero.name], did you hear me?"
            mike.say "Zzzz..."
            hide fx
    else:
        "I must have dropped off for a moment."
        "As I come round to see that Lavish isn't in her sleeping bag."
        show lavish casual with dissolve
        "Instead I find her sitting at the entrance to the tent."
        "It's unzipped and she seems to be staring up at the sky."
        "So I crawl over and join her, watching the embers from the fire spiral upwards."
        show lavish surprised
        lavish.say "Oh..."
        show lavish normal
        lavish.say "Hey, [hero.name]."
        lavish.say "I was just checking out the stars."
        lavish.say "I've never seen them so clearly."
        lavish.say "And there are so many of them too."
        if hero.knowledge >= 85:
            mike.say "It's the light pollution from the city, Lavish."
            mike.say "Out here there's less of it, so there's more sky!"
            mike.say "This is how the sky looked thousands of years ago."
            $ lavish.love += 2
            "Lavish nods eagerly, hanging on every word I say."
            "And she scoots over to where I'm sitting too."
            "Leaning against me in a very pleasant way."
            lavish.say "You know so much about all this, [hero.name]."
            lavish.say "Do you know the names of the stars too?"
            mike.say "I know most of the constellations."
            mike.say "Like that there, for example..."
            mike.say "That's Orion's Belt."
            mike.say "And The Plough is just over there."
            show lavish pleased
            $ game.active_date.score += 20
            "Lavish leans in even closer, looking back to see where I'm pointing."
            "And it's hard to keep my mind on the task at hand."
            "What with the sensation of her body, warm against mine."
        else:
            "I get the feeling that Lavish is waiting for me to do something."
            "Like say something profound and name all of the stars out tonight."
            "But the moment I look up there, it's like my brain just nopes out on me."
            "And I find myself babbling in order to fill up the empty space."
            mike.say "Erm..."
            mike.say "Yeah..."
            mike.say "I dunno, Lavish."
            mike.say "Maybe we're closer to the sky out here or something?"
            show lavish bored
            "Lavish looks at me sideways."
            "Kind of like I have steaming turds hanging out of my mouth."
            "And she shakes her head."
            lavish.say "Yeah well..."
            show lavish sadsmile
            $ game.active_date.score -= 10
            lavish.say "Maybe it's time I got some sleep."
            "With that, she crawls back into the tent."
            "Leaving me alone to curse my big, dumb mouth."
    scene bg forest night at center, zoomAt(1.5, (940, 940)), blur(16) with dissolve
    "At some point the both of us must have fallen asleep."
    "Because I come round to the coolness of the morning."
    scene bg forest with dissolve
    "And the first light of dawn peeking through the opening of the tent."
    "As soon as Lavish opens her eyes, I speak up."
    mike.say "Good morning, Lavish..."
    mike.say "Did you sleep well?"
    show lavish yawn sport with dissolve
    lavish.say "Ooh..."
    lavish.say "I think so."
    mike.say "Well..."
    mike.say "Are you ready to head home?"
    mike.say "Or do you want to hang around a little?"
    if game.active_date.score >= 80 and lavish.sexperience >= 1:
        show lavish normal
        lavish.say "You know what..."
        lavish.say "I think I'm actually starting to like it here."
        lavish.say "You mind if we take it slowly?"
        mike.say "Of course not, Lavish."
        mike.say "We can take as long as you like."
        mike.say "What do you want to do while we're still here?"
        "Rather than answering with words."
        "Lavish unzips her sleeping bag."
        "Then she flips it open, revealing the shape of her body."
        show lavish flirt
        lavish.say "Oh..."
        lavish.say "I'm sure we can think of something!"
        call lavish_birthday_sex_male from _call_lavish_birthday_sex_male
    else:
        show lavish sadsmile
        lavish.say "Actually, I'm a little stiff and cold."
        lavish.say "You mind if we head home?"
        mike.say "Of course not, Lavish."
        show lavish normal
        "We get up and start to take down the tent."
        "Then we pack everything away and prepare to leave."
        "Sure, I would have liked to take things more slowly."
        "Maybe even hang around a little longer."
        "But Lavish kept her part of the bargain."
        "So now I have to keep mine too."
        "The hike back to the car seems quicker than it did on the way out."
        "And before I know it, I'm dropping Lavish off and waving goodbye."
    return

label lavish_birthday_sex_male:
    "Lavish doesn't say a word, but then she doesn't need to."
    "All she has to do is beckon me over with a single finger."
    "That's all it takes for me to unzip my own sleeping bag."
    "And as soon as that's done, I throw myself across the tent."
    show lavish surprised at center, zoomAt(2.0, (640, 1340)) with vpunch
    "Lavish let's out a yelp of surprise as I land beside her."
    "But that's not to say that she's discouraged in the slightest."
    "Because as soon as I reach out for her, she nestles herself into my arms."
    show lavish flirt
    lavish.say "Mmm..."
    lavish.say "I don't think I'm actually awake yet."
    lavish.say "I might need something to get me going this morning."
    lavish.say "You think you can help me with that?"
    "Lavish underlines her point by pushing herself back into me."
    "Pressing her ass hard against my groin as she does so."
    "I want to come out with a smart-ass line in response."
    "Something that'll make her laugh and me sound cocky."
    "But my senses are just too full of her to be able to do it."
    "All I can smell is the scent of Lavish's body."
    "All I can feel is the sensation of it pressed against mine."
    "I want her too badly to think of anything else."
    "My hands are already sliding over her."
    "And they find their way over her belly."
    show lavish yawn blush
    "Then they move downwards, slipping into her panties."
    "Lavish lets out a moan of pleasure as I stroke her down there."
    "Her hair is soft and warm, but I can already feel her getting wet."
    show lavish flirt
    "Suddenly she surprises me by making a grab for her panties."
    "And for a moment I think that she's going to pull my hand away."
    "But much to my relief, her own hand only pushes mine down further."
    "While the other begins to tug down her underwear."
    "At the same time I try to take mine off too."
    show lavish yawn naked with dissolve
    "What follows is an almost desperate struggle."
    "A mess of hands and fingers, all trying to achieve the same thing."
    "When it's perhaps only halfway done, we're already trying to go further."
    "I'm fumbling to push myself forward and Lavish to wriggle backwards."
    show lavish surprised
    "And that's how we first touch, my cock against her pussy."
    "Another time this might have made us stop and get things in order."
    "It might have cleared our minds and caused everything to run smoothly."
    show lavish flirt
    "Instead it just makes the whole thing that much more intense and chaotic."
    "Lavish makes a grab for my manhood, almost like a woman possessed."
    "She pushes it hard against her pussy, like she's desperate."
    "I do the best I can to help, pushing from my side too."
    "We fumble and flail, missing more than once."
    "And then, almost my accident, it happens."
    scene bg black
    show lavish missionary forest
    with fade
    "Lavish parts, opening up to me."
    "And I feel myself sliding into her."
    show lavish missionary vaginal orgasm
    "Instantly I redouble my efforts, going as deep as possible."
    "She freezes as this happens, like she's been turned to stone."
    "And she stays that way until I can't get any deeper."
    "Somehow this seems to be enough to satisfy us both."
    "At least enough to allow our bodies to relax again."
    show lavish missionary normal
    "Now we lie back, folded together and the pace changes dramatically."
    "The feeling of being inside Lavish is enough to calm me down completely."
    "It's incredible, sublime, maybe even divine."
    "I want to savour it for as long as humanly possible."
    show lavish missionary orgasm
    "That's why I begin to move slowly and smoothly."
    "And she seems to appreciate the change too."
    "Before there was a crazy desire in Lavish, almost a desperation."
    "But now she's moving as purposefully as I am."
    "It's like I can feel Lavish melting in my arms."
    "Like I can feel her entire body surrendering to the moment."
    "My hands move over her body as we make love."
    "Not in a desperate or grasping manner."
    "But instead in a gentle and yet deep exploration."
    "They hold and caress, feeling every inch of her on the outside."
    "The same way that I feel like I'm caressing her on the inside too."
    "This allows us to build, slowly and surely."
    "Coming together as our passions mount."
    "And when the moment of release is finally upon us, we go together."
    "I wrap my arms around Lavish, holding her closer than ever."
    show lavish missionary ahegao creampie with hpunch
    $ lavish.love += 4
    "She takes all that I have to give in the core of her being."
    with hpunch
    "And I feel her climax spread through her body like a dawning sun."
    show lavish missionary orgasm with hpunch
    "Afterwards, we lie together, feeling the freshness of the morning breeze."
    "Neither of us feeling the urge to move."
    "Instead happy to remain in the moment for as long as it might last."
    $ lavish.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
