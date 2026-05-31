init python:
    InteractEvent(**{
    "name": "sasha_threesome_confrontation",
    "priority": 500,
    "label": "sasha_threesome_confrontation",
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("kleio_and_anna"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("sashathreesomedelay", False),
            IsDone("battle_of_the_bands_win"),
            ),
        PersonTarget(sasha,
            IsActive(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        "Person.showdown(sasha, kleio, anna)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kleio_anna_cheating_confrontation",
    "priority": 500,
    "label": "kleio_anna_cheating_confrontation",
    "conditions": [
        IsHour(10, 18),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Or(
                IsRoom("studio", "mall1", "mall2"),
                HasRoomTag("street"),
                HasRoomTag("park"),
                HasRoomTag("pub"),
                ),
            ),
        Or(
            PersonTarget(kleio,
                IsPresent(),
                ),
            PersonTarget(anna,
                IsPresent(),
                ),
            ),
        PersonTarget(kleio,
                Not(IsHidden()),
                InHarem("band"),
                ),
        PersonTarget(anna,
                Not(IsHidden()),
                InHarem("band"),
                ),
        PersonTarget(sasha,
                InHarem("band"),
                HasCheated(),
                ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kleioannafoursome",
    "priority": 500,
    "label": "kleioannafoursome",
    "duration": 1,
    "conditions": [
        IsHour(20, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("livingroom"),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            IsFlag("kleioannafoursome"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kleioannafoursome2",
    "priority": 500,
    "label": "kleioannafoursome2",
    "duration": 2,
    "conditions": [
        IsDone("kleioannafoursome"),
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("studio"),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "anna_kleio_anal",
    "label": "anna_kleio_anal",
    "priority": 500,
    "conditions": [
        'Harem.together("kleio", "anna")',
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        PersonTarget(anna,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            Not(IsHidden()),
            ),
        Or(
            Or(
                PersonTarget(anna,
                    OnDate()
                    ),
                PersonTarget(kleio,
                    OnDate()
                    ),
                ),
            And(
                HeroTarget(Not(OnDate())),
                Or(
                    PersonTarget(anna,
                        IsActive(),
                        ),
                    PersonTarget(kleio,
                        IsActive(),
                        ),
                    ),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "kleio_anna_showdown",
    "priority": 500,
    "label": "kleio_anna_showdown",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            ),
        "Person.showdown(anna, kleio)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "date_set_up",
    "priority": 500,
    "label": "date_set_up",
    "conditions": [
        IsDone("kleio_anna_showdown"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("studio"),
            IsFlag("anna_kleio_date_delay", False),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "anna_concert_naked",
    "label": "anna_concert_naked",
    "display_name": "About our gigs",
    "icon": "gig_talk",
    "duration": 0,
    "conditions": [
        IsDone("gig"),
        HeroTarget(IsGender("male")),
        PersonTarget(anna,
            IsActive(),
            Not(IsFlag("agree_concert_naked")),
            InHarem("band"),
            ),
        PersonTarget(kleio,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("kleio_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget(sasha,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("sasha_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget("amy",
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("amy_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        ],
    "once_week": True,
    })

    SpecificTalkSubject(**{
    "name": "kleio_concert_naked",
    "label": "kleio_concert_naked",
    "display_name": "About our gigs",
    "icon": "gig_talk",
    "duration": 0,
    "conditions": [
        IsDone("gig"),
        HeroTarget(IsGender("male")),
        PersonTarget(kleio,
            IsActive(),
            Not(IsFlag("agree_concert_naked")),
            InHarem("band"),
            ),
        PersonTarget(anna,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("anna_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget(sasha,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("sasha_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget("amy",
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("amy_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        ],
    "once_week": True,
    })

    SpecificTalkSubject(**{
    "name": "sasha_concert_naked",
    "label": "sasha_concert_naked",
    "display_name": "About our gigs",
    "icon": "gig_talk",
    "duration": 0,
    "conditions": [
        IsDone("gig"),
        HeroTarget(IsGender("male")),
        PersonTarget(sasha,
            IsActive(),
            Not(IsFlag("agree_concert_naked")),
            InHarem("band"),
            ),
        PersonTarget(anna,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("anna_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget(kleio,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("kleio_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget("amy",
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("amy_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        ],
    "once_week": True,
    })

label sasha_threesome_confrontation:
    show sasha
    mike.say "I'm not psychic, Sasha, but it feels like something's bugging you."
    show sasha shout
    sasha.say "What - no, I just wanted to talk, that's all."
    show sasha normal
    "My heckles are immediately up at this, but I try to play innocent."
    mike.say "Talk about what, exactly?"
    show sasha shout
    sasha.say "Oh, just stuff in general...I feel like we somehow talk less, even though you're in the band now."
    sasha.say "Weird, yeah?"
    show sasha normal
    "I nod, noticing that she's already the one doing most of the talking."
    show sasha shout
    sasha.say "You guys were on fire tonight, by the way."
    show sasha normal
    mike.say "Thanks, Sasha - you were great too."
    show sasha whining
    sasha.say "Nah, I was a mess."
    show sasha shout
    sasha.say "But you, Anna and Kleio - I don't know, it's kinda like you've just clicked, all three of you all of a sudden."
    show sasha normal
    "I try to look like I'm smiling at the compliment, but I'm already worried Sasha has figured out that Kleio, Anna and I are now a threesome."
    show sasha shout
    sasha.say "Look, we're supposed to be a band, a four-piece, and I think we can be honest with each other - don't you?"
    show sasha normal
    "I nod, preparing myself for the worst."
    show sasha whining
    sasha.say "Just tell me - have the three of you been practising behind my back?"
    sasha.say "Are you gonna kick me out of the band, or just all quit and reform without me?"
    show sasha sad
    "The look of surprise and then relief on my face must be plain to see."
    "Sasha reads instantly that I'm taken aback by the idea."
    show sasha stuned
    "But she's no fool, and soon senses that there's something else behind my reaction."
    show sasha surprised
    sasha.say "Wait a minute...it's not that you want rid of me - but there's something going on here, isn't there?"
    show sasha stuned
    "I start trying to speak, but Sasha cuts me off."
    show sasha whining
    sasha.say "I got suspicious when you all showed up within neat little five minute intervals."
    sasha.say "Normally Kleio's early, Anna's late and we go to the practise room together."
    show sasha annoyed
    "I can almost see the wheels and cogs turning in Sasha's brain as she works it out for herself."
    show sasha whining
    sasha.say "If you're all into something together, something that's making you so in tune with each other, something you're not telling me about..."
    show sasha mindless
    "And there it is, I see the moment her face registers what's going on between Kleio, Anna and myself."
    mike.say "I don't know what to tell you, Sasha."
    mike.say "It just kind of happened - no one's more surprised than me!"
    if sasha.love <= 150 and sasha.lesbian < 9:
        show sasha wtf
        "Sasha wrinkles her features as though she's smelled something nasty."
        sasha.say "Eww...all three of you, together, at once?!?"
        mike.say "It didn't start out that way, honestly!"
        mike.say "I was seeing them separately and they kinda found out about each other."
        sasha.say "And that makes it better how?"
        "I realise how bad that explanation sounds only after I've said it."
        show sasha vangry
        sasha.say "Jesus, why am I exploding all over you when you're all in it together and loving the whole thing?"
        show sasha annoyed
        mike.say "I'm sorry, for what it's worth."
        mike.say "I couldn't help falling for two women that wanted me...I thought you were different enough to be okay with something like that."
        show sasha vangry
        sasha.say "Huh...maybe I'm more traditional than either of us thought."
        $ sasha.set_gone_forever()
    elif sasha.love <= 150 or sasha.lesbian < 9:
        show sasha joke
        "Sasha shakes her head and whistles in what I take to be a show of grudging admiration."
        sasha.say "Well, aren't we the dark horse?"
        show sasha normal
        mike.say "It really didn't happen like that!"
        show sasha shout
        sasha.say "No, I suppose you all just tripped and fell into bed together while you were naked?"
        show sasha normal
        mike.say "More like I was kind of seeing them both and they found out."
        show sasha shout
        sasha.say "You're lucky they wanted to share their toys!"
        show sasha normal
        mike.say "Look, I'm sorry no one told you, Sasha."
        show sasha shout
        sasha.say "Hey, you're telling me now, aren't you?"
        show sasha wink
        "Sasha gives me a knowing wink."
        show sasha shout
        sasha.say "Just don't leave me to jump to the wrong conclusion next time you've got a juicy secret like that!"
    else:
        show sasha embarrassed
        "Sasha looks awkward, blushing and struggling to look me in the eye."
        mike.say "Shit, Sasha...I'm sorry if I've shocked you or pissed you off with all of this."
        show sasha blush
        sasha.say "No...no, it's nothing like that."
        show sasha shy
        "I'm struggling to guess what Sasha means, when she puts her hands on mine atop the table."
        show sasha shout
        sasha.say "This is tough for me to admit, but I've always had kind of a crush on Kleio and Anna..."
        show sasha normal
        mike.say "It's not weird, Sasha - a lot of people think their friends are pretty cute, and we're all really close because of the band."
        show sasha shout
        sasha.say "Okay, I'll spell it out for you - I feel like I'm missing out on something fun, and I want in!"
        show sasha normal
        "My mouth moves, but no words come out."
        show sasha joke
        sasha.say "That's a pretty good impression of a goldfish, but it doesn't give me an answer."
        show sasha normal
        mike.say "Sasha...I'm already reeling from being in a relationship with two women, let alone three!"
        show sasha shout
        sasha.say "Can't be that big of a leap, from a threesome to a foursome, surely?"
        show sasha normal
        mike.say "Well, when you put it like that..."
        show sasha blush
        sasha.say "Look, I'm just asking - maybe put in a good word for me, huh?"
        show sasha shy
        "I nod, trying to keep the thoughts of what possibilities this promises off my mind for the moment."
        $ sasha.flags.kleioannafoursome = True
    show sasha normal
    "We finish our beers and leave in silence."
    "Both of us are too preoccupied with the ramifications of all that's just come out to be able to talk."
    "Whatever happens from here on in, it's sure to change somethings forever."
    return

label kleioannafoursome(appointment=None):
    if appointment:
        scene bg bedroom3 with fade
        "Altogether in Sasha's bedroom, all of us eagerly stripping off our clothes."
    else:
        $ Harem.join_by_name("band", "sasha")
        if renpy.has_label("band_harem_achievement_4") and not game.flags.cheat:
            call band_harem_achievement_4 from _call_band_harem_achievement_4
        scene bg livingroom with fade
        "Anna and Kleio eagerly agreed to come over to my place that evening, no doubt expecting to resume our group activities."
        "I couldn't share their enthusiasm, as I was already feeling my stomach churn at the prospect of telling them about Sasha."
        "Being involved with two girls was dizzying enough, but now I had to ask them to let another one into our already unusual relationship."
        show kleio date zorder 2 at right with moveinright
        "Kleio arrived first, giving me a typically dirty and lingering kiss before throwing herself down on the sofa."
        show anna casual b zorder 1 at right4 with moveinright
        "Anna turned up a few minutes later, hugging me with her usual childish glee and then perching on the edge of the sofa beside Kleio."
        mike.say "Have you eaten, can I get you both a drink?"
        anna.say "Oh, erm...I didn't think you'd ask me that!"
        show kleio seductive
        kleio.say "Maybe later - I'm hungry for something else right now!"
        mike.say "Oh, yeah, of course...me too."
        mike.say "I just thought it might be nice to chat for a bit before we...you know."
        mike.say "It can't all be about the sex, can it?"
        show kleio normal
        kleio.say "I don't see why not!"
        show anna happy
        anna.say "I know - maybe we can talk dirty?"
        "I've begun to fiddle with my collar by now, probably looking like a picture of panic and evasion."
        show kleio annoyed
        kleio.say "Something's up with Loverboy...come on, man - spill your guts."
        "I try not to stammer or trip over my words, aware that Sasha is waiting in her room to hear the outcome of my pitch on her behalf."
        mike.say "Well, the thing is...I was out for a drink with Sasha the other night."
        mike.say "And she, well...she kind of figured out what's going on between us all."
        show anna surprised
        show kleio seductive
        "Anna's expression is one of incomprehension, and then shock."
        "Kleio surprises me by looking amused, rather than annoyed."
        kleio.say "You told her all about it?"
        mike.say "No, I swear - she thought we were spending time together without her because we were planning on kicking her out of the band."
        mike.say "When I told her we weren't, she's smart, so she guessed what it really was."
        show kleio normal
        kleio.say "So what - is she mad, jealous, or a bit of both?"
        show anna annoyed
        anna.say "Ooh, if she is mad, I hope she's not too mad."
        "I try to steel myself as the moment of truth arrives."
        mike.say "She's definitely not mad, but you could say she's jealous."
        mike.say "She asked me to ask you...if she could make what we have into a foursome?"
        show kleio surprised
        kleio.say "Does she now?!?"
        mike.say "Is that a yes, or a no?"
        show kleio seductive
        kleio.say "I'm no prude, so it's a yes - if we can have a threesome, why not a foursome?"
        mike.say "What about you, Anna?"
        show anna blush
        "Anna blushes, clearly intrigued by the idea and yet embarrassed to be put on the spot."
        anna.say "I always had kind of a girl-crush on Sasha, so I say let's do it!"
        "Two votes of yes, and I guess I'd already said the same when I agreed to bring it up with Kleio and Anna, which makes it a clean sweep."
        scene bg secondfloor with fade
        "I nod quickly, letting out a nervous sigh as I get up and start to walk towards the hallway and Sasha's bedroom door, preparing to deliver the news personally."
        play sound door_knock
        "I have no idea why, but I try to make as little sound as possible as I creep towards Sasha's bedroom door and knock quietly."
        show kleio date at right5
        show anna casual at left5
        with dissolve
        "Behind me, Kleio and Anna are making no such effort."
        "Kleio seems to be stalking after me like a cat hunting down a helpless bird with a broken wing."
        "And Anna can't keep from breaking out into what I suspect are nervous bouts of giggles at the prospect of what lies ahead."
        "I turn my head, intending to tell them to shut up, but a voice from the other side of the door stops me before I can speak."
        sasha.say "Who is it?"
        "I realise that she must have been sitting there in silence, just waiting to hear the outcome of my proposal to the other girls."
        mike.say "It's me...can I come in?"
        sasha.say "I guess so."
        scene bg bedroom3
        show sasha sleep
        with fade
        "I make as serious a gesture for Kleio and Anna to keep quiet and wait in the hallway as I can manage, and then open the door to slip into Sasha's bedroom."
        "Sasha has the lights down low, save for a lamp by the bedside, and an open book beside it suggests she's been trying to distract herself without success."
        "But I soon forget those details, as she's sitting up on the bed, wearing only a vest and some shorts, a hopeful look on her face."
        "I should be saying something to her, but all I can do is stare at Sasha and think of what new possibilities she opens up for Kleio, Anna and myself."
        sasha.say "Well...what's the verdict?"
        mike.say "I asked them both, and...and..."
        "Before I can finish the sentence, I feel the door being rudely barged open from behind, pushing me further into the room."
        show kleio date happy at left with moveinleft
        show anna casual happy at right with moveinright
        "Kleio and Anna burst in, both giggling now and looking at Sasha in a manner that suggests they're thinking the exact same thing as me."
        kleio.say "We said YES!"
        "Anna and I both nod, hoping not to be left behind by Kleio's brash entrance."
        kleio.say "If we waited for Loverboy here to tell you, we'd be cleaning cobwebs out of our clits before he got round to it!"
        show anna blush
        anna.say "[hero.name] and I aren't as forward as Kleio, but we're both super excited to be letting you in on this, aren't we?"
        mike.say "Yeah...yeah, it's like being on a roller-coaster...you know, thrilling and a little scary, but in a good way."
        "All three of us have sat down on the bed and around Sasha by this point."
        show sasha happy
        "She smiles and tries to look confident, but she must feel like she's being initiated into some kind of weird, kinky cult right now."
        show sasha joke
        sasha.say "So that's how you guys want it to be, eh?"
        sasha.say "You want to treat me like some kind of fairground ride that's for cheap thrills?"
        show kleio seductive
        kleio.say "Nah, you're the noob - so you get to ride us."
        "Sasha shows a little colour in her cheeks at Kleio's statement, obviously trying to picture what she has in mind."
        "I find that I can tune into what Kleio must be thinking, remembering that she, Anna and I are already used to indulging ourselves as a threesome."
        "If we want to bring Sasha into the fold, then perhaps we should take her by the hand and show her the way."
        show anna casual at center, zoomAt(1.5, (940, 1040))
        "Without asking permission, I reach over and pull Anna's tight t-shirt up and over her head."
        show anna topless
        "Anna makes no effort to stop me, giggling even more as her large breasts are revealed."
        show sasha blush at center, zoomAt(1.5, (740, 1040))
        "Sasha reaches out tentatively with one hand, and Anna gently takes hold of her wrist, guiding her to cup one of her breasts."
        "At the same time, Anna moves closer, beginning to slide alongside Sasha, and slips one hand under her vest and the other into the waistband of her shorts."
        show kleio date at center, zoomAt(1.5, (340, 1040))
        "Kleio chooses that moment to crawl into my lap, unzipping my flies, fingers stroking my dick."
        "She purrs in approval as I return the favour, lifting her skirt with one hand to caress her beneath her knickers as the other pulls off her top and spills her breasts."
        show kleio naked
        show sasha naked
        "We each undress the other as we explore each other's bodies, Kleio and I in one pair and Anna and Sasha the other."
        "Sasha's eyes are as much drawn to watching myself and Kleio as they are to Anna's attentions to her own body."
        "At one point we catch each other's gaze, and wonder if she's as amazed by the situation as I am."
        "Neither of us could have known, when she walked into my house or introduced me to her bandmates for the first time, that we would end up here."
        "It isn't long before everyone is undressed, four naked bodies coming together in the middle of the bed."
        "Sasha tries not to stare at my now very much hard and erect dick, but she can't help herself, and the others are not slow to notice either."
        show kleio normal
        kleio.say "Not a bad specimen, is it?"
        show anna happy
        anna.say "I can personally recommend it, in either hole down there...very nice indeed!"
        "Sasha laughs nervously, not knowing what should happen next."
        show kleio annoyed
        kleio.say "Thing is, it's the only one we got."
        show anna evil
        anna.say "So you have to be fair, you have to agree to share it."
        show kleio seductive
        kleio.say "Yeah, Sasha - no hogging Loverboy's dick!"
        "Sasha looks at me, probably wondering why I'm not a part of the conversation."
        show kleio happy
        kleio.say "But, you do get new-girl's privilege."
        show anna happy
        anna.say "Yeah, you get to ride it as it's your first time!"
        "Part of me is pissed off that Kleio and Anna are talking about me like a piece of meat, despite all the talk of equality in the band."
        "But I have to admit that there's a real thrill to being used in this way, especially when they're debating who should get to have it inside of them."
        "I get no chance to speak before Anna starts pushing me down onto the bed, massaging my dick at the same time."
        "Together, she and Kleio push Sasha backwards, as she gets ever closer to my erection."
    show band foursome with fade
    if renpy.has_label("band_harem_achievement_5") and not game.flags.cheat:
        call band_harem_achievement_5 from _call_band_harem_achievement_5
    "Anna begins to help guide Sasha, who glances over her shoulder as she approaches."
    "It's only at this moment I realise that I'm in total control of just where my dick goes."
    "And in those few seconds, I put my hands on Sasha's hips and make my decision."
    $ who_in = ""
    menu:
        "Fuck Sasha's pussy":
            $ who_in = "sasha_pussy"
            "I figure that, as it's Sasha's first time, I should keep things pretty traditional."
            "I pull her down slowly, so that my dick slides up and between the lips of her pussy."
            show band foursome vaginal sashapleasure
            "Sasha's already quite slick, and so she can offer little resistance as she sits down on me."
            "Gravity makes her take the entire length until there's nothing left that's not inside of her."
            show band foursome kleiopleasure
            "At the same time, Kleio is alternatively kissing one of her exposed nipples while squeezing and pinching the other."
            "Anna busies herself by licking one moment at Sasha's lower lips, and then doing the same to the base of my shaft."
            show band foursome sashanormal
            "Sasha instinctively tries to shift her position, but she is being pleasured from three different angles at once."
            show band foursome sashapleasure
            "Any attempt to move merely serves to intensify the sensations that are clearly coming close to overwhelming her."
        "Fuck Sasha's ass":
            $ who_in = "sasha_ass"
            "I might have been tempted to do Sasha in the traditional manner, but why be conservative in the middle of a foursome?"
            "I angle Sasha forward a little, and push my dick between her buttocks and into her unsuspecting ass."
            show band foursome anal sashapleasure
            "Sasha yelps in surprise as she sinks down on my dick, feeling it probe her ass."
            "But then she moans long and loudly as Anna's tongue begins to explore the folds of her pussy."
            show band foursome kleiopleasure
            "Kleio soon joins in, kissing, nibbling and squeezing Anna's stiffened nipples without pause."
            show band foursome sashanormal
            "I can't honestly think of any more that we could be doing to stimulate Sasha at that moment in time."
            show band foursome sashapleasure
            "And she soon rises towards her climax, body twitching and flinching as the three of us play her like she was one of our instruments."
        "Fuck Anna's mouth":
            $ who_in = "anna_mouth"
            "I don't know what makes me go against the flow, maybe the closeness of Anna's heavy breasts and plump lips."
            "But whatever the reason, I decide to throw a curve-ball at Sasha, and reach around to seize Anna's head."
            show band foursome blowjob
            "At the same time, I push my groin upwards so that my dick slips into her mouth, just as she opens it to ask what I'm doing."
            show band foursome annapleasure
            "Not needing any more explanation, Anna begins to slide her tongue around my shaft, expertly exciting me with each and every movement."
            show band foursome sashapleasure
            "Sasha looks disappointed, but her attention is soon diverted when Kleio begins to kiss and lick at her now stiffening nipples."

            "Soon Sasha seems to have forgotten the fact that I denied her my dick, and is singing more loudly with each moment that passes."
            "As she arches her back and prepares to climax, I realise she's not the only one about to cum."
        "Fuck Anna's pussy":
            $ who_in = "anna_pussy"
            "I'm pretty sure that Anna's gotten up to some crazy stuff in the past."
            "But as this is Sasha's first time, I decide to play it safe even with Anna."
            show band foursome fuckanna annapleasure
            "I take a firm hold of her little round ass, pushing my cock between her legs."
            "Anna's already excited, which means that she's nice and slick down there."
            "And so I can slide straight into her in almost one smooth motion."
            show band foursome kleiopleasure sashapleasure
            "At the same time, Kleio is alternatively kissing one of Sasha's exposed nipples while squeezing and pinching the other."


            "Any attempt to move merely serves to intensify the sensations that are clearly coming close to overwhelming Sasha."
        "Fuck Anna's ass":
            $ who_in = "anna_ass"
            "I know Anna well enough to be sure that she's no amateur when it comes to this kind of thing."
            show band foursome fuckanna annapleasure
            "So when I garb hold of her round little ass, I don't hesitate to spread her buttocks apart."
            "And then I point the head of my cock straight at the target that I'm presented with."
            "Anna yelps in surprise as she sinks down on my dick, feeling it probe her ass."
            "But her yelps soon turn into moans of pleasure as I push my way further into her."
            show band foursome kleiopleasure sashapleasure
            "At the same time, Kleio is alternatively kissing one of Sasha's exposed nipples while squeezing and pinching the other."


            "And she soon rises towards her climax, body twitching and flinching as the three of us play her like she was one of our instruments."
        "Fuck Kleio's pussy":
            $ who_in = "kleio_pussy"
            "I'm pretty sure that Kleio's had times as wild as this before, if not even crazier."
            "But as this is Sasha's first time, I decide to play it safe even with Kleio."
            show band foursome fuckkleio kleiopleasure
            "I take a firm hold of her little pert, proud breasts and pull her backwards onto me."
            "Kleio lets out a yelp of surprise, but then moans with pleasure as she feels my cock between her legs."
            "And I can feel just how wet she is down there, making me want her all the more."
            "I hastily press the head of my cock against Kleio's pussy, feeling her yield to me almost instantly."
            show band foursome annapleasure sashapleasure
            "At the same time, she's alternatively kissing one of Sasha's exposed nipples while squeezing and pinching the other."
            "Anna has her head buried in Sasha's lap, licking away at her pussy all the while."
            "And the harder I thrust my cock into Kleio, the more she kisses Sasha's breasts!"
            "Any attempt to move merely serves to intensify the sensations that are clearly coming close to overwhelming her."
        "Fuck Kleio's ass":
            $ who_in = "kleio_ass"
            "Kleio's a pretty outrageous kind of girl, the type that can take crazy stuff in her stride."
            show band foursome fuckkleio kleiopleasure
            "And it's with this in mind that I take hold of her breasts and pull her backwards onto me."
            "At the same time, I push my cock between her buttocks, aiming for her ass."
            "Kleio gasps in surprise as she feels me push it into her, sinking deeper with every passing second."
            "But her yelps soon turn into moans of pleasure as I push my way further into her."
            show band foursome annapleasure sashapleasure
            "At the same time, she's alternatively kissing one of Sasha's exposed nipples while squeezing and pinching the other."
            "Anna has her head buried in Sasha's lap, licking away at her pussy all the while."
            "And the harder I thrust my cock into Anna, the more she kisses Sasha's breasts!"
            "Any attempt to move merely serves to intensify the sensations that are clearly coming close to overwhelming her."
    "I have perhaps five seconds to decide where exactly I want to be before I lose it."
    menu:
        "Cum in Sasha's pussy" if who_in == "sasha_pussy":
            "Determined to make Sasha the centre of attention during her first time together with us, I push as deep into her as I can."
            show band foursome vaginal creampie sashaahegao with vpunch
            $ sasha.love += 2
            "When I can't hold on any longer, I let go and feel the sensation of my own climax pushing her over the edge."
            "Sasha cries out and stiffens, as while My motions have stopped, Kleio and Anna show no signs of doing the same."
            show band foursome sashapleasure kleionormal annanormal
            "Still riding me and being held up by the other two girls, she remains suspended upright, feeling the full effects without release."
        "Cum in Sasha's ass" if who_in == "sasha_ass":
            "Kleio's playing with her nipples and Anna licking at her pussy seems to be enough to finally bring Sasha to an orgasm."
            show band foursome anal creampie sashaahegao with vpunch
            $ sasha.sub += 2
            "As I feel the sensation rippling through her taut body, she sets me off as well, my dick getting every twinge and tick while up her ass."
            "Adding the sudden pressure of me cumming inside of her makes Sasha arch her back and cry out with unexpected volume."
            "I watch as she takes every single moment of the climax, impaled on my dick and trapped where she sits."
        "Cum in Anna's mouth" if who_in == "anna_mouth":
            "With my dick in Anna's mouth, I can't tell which one of us starts to cum first."
            show band foursome blowjob cumshot annaahegao with vpunch
            $ anna.love += 1
            $ anna.sub += 1
            "But once the ripples of an orgasm start to spread, it pushes us both over the edge."
            "Seconds later I feel the release while my dick is still surrounded by the soft warmth of Anna's mouth."
            show band foursome annapleasure
            "Luckily, she's ready for it, and keeps from choking as she gasps and swallows, which only adds to me own sensations of pleasure."
        "Cum in Anna's pussy" if who_in == "anna_pussy":
            "I'm so deep inside of Anna right now that I can't think of anything else, never mind pulling out!"
            show band foursome creampie cumshot annaahegao with hpunch
            $ anna.sub += 2
            "When I can't hold on any longer, I let go and feel the sensation of my own climax pushing her over the edge."
            "Anna cries out and stiffens, as while my motions have stopped, Kleio and Sasha show no signs of doing the same."
            show band foursome -cumshot cum onannabody annapleasure
            "Still riding my cock, Anna's pinned down and can't hope to escape as I shoot my load into her."
        "Cum in Anna's ass" if who_in == "anna_ass":
            "My cock is as deep inside of Anna's ass as I can get it right now, and the only way is forwards."
            show band foursome creampie cumshot annaahegao with hpunch
            $ anna.love += 2
            "So when I feel myself losing it, she takes everything that I have to give with no hope of escape."
            "Kleio and Sasha must be up to something right now, but all I can think about is letting go."
            show band foursome -cumshot cum onannabody annapleasure
            "And all I can hear is Anna, moaning and whimpering as I fill her with all I have to give."
        "Cum in Kleio's pussy" if who_in == "kleio_pussy":
            "I'm so deep inside of Kleio right now that I can't think of anything else, never mind pulling out!"
            show band foursome cumshot kleioahegao with hpunch
            $ kleio.love += 2
            "When I can't hold on any longer, I let go and feel the sensation of my own climax pushing her over the edge."
            "Kleio cries out and stiffens, as while my motions have stopped, Anna and Sasha show no signs of doing the same."
            show band foursome -cumshot cum onkleiobody kleiopleasure
            "Still riding my cock, Anna's pinned down and can't hope to escape as I shoot my load into her."
        "Cum in Kleio's ass" if who_in == "kleio_ass":
            "My cock is as deep inside of Kleio's ass as I can get it right now, and the only way is forwards."
            show band foursome cumshot kleioahegao with hpunch
            $ kleio.sub += 2
            "So when I feel myself losing it, she takes everything that I have to give with no hope of escape."
            "Anna and Sasha must be up to something right now, but all I can think about is letting go."
            show band foursome -cumshot cum onkleiobody kleiopleasure
            "And all I can hear is Kleio, moaning and whimpering as I fill her with all I have to give."
        "Cum on Anna's face" if who_in == "sasha_pussy" or who_in == "sasha_ass":
            "At the very last moment, I feel myself having a sudden and unexpected change of heart."
            show band foursome -vaginal -anal sashanormal
            "Without warning, I pull my cock out of Sasha in one smooth motion, making her moan in surprise."
            show band foursome cumshot annapleasure with vpunch
            "There's just enough time for me to aim it at Anna's face, before it happens."
            show band foursome -cumshot dickcum
            "I cum without holding back, spattering her features with streamers of sticky, white cum."
            show band foursome cumshot -dickcum blowjob
            $ anna.love += 1
            $ anna.sub += 1
            "Anna gasps and pants as it runs down her cheeks and over her lips."
    if who_in == "anna_ass":
        $ anna.flags.anal += 1
    if who_in == "kleio_ass":
        $ kleio.flags.anal += 1
    if who_in == "sasha_ass":
        $ sasha.flags.anal += 1
    hide band foursome
    show kleio naked seductive zorder 3 at center, zoomAt(1.5, (340, 1040))
    show sasha naked blush zorder 1 at center, zoomAt(1.5, (640, 1040))
    show anna naked wink zorder 2 at center, zoomAt(1.5, (940, 1040))
    with fade
    "Though only Sasha and myself have actually cum, everyone sags onto the bed, like a troupe of puppets who's strings had been suddenly severed."
    "No one speaks, but we can all feel that something pretty amazing and life-changing has just happened to us all."
    "Not only are we all bandmates, we're all lovers now as well."
    if appointment:
        $ game.pass_time(2)
        $ game.room = "bedroom3"
    else:
        call sleep from _call_sleep_48
        $ game.room = "bedroom1"
    return

label kleioannafoursome2(appointment=None):
    if appointment:
        scene bg bedroom1
        "Once again, we're in my bedroom, all four of us eagerly stripping off our clothes."
    else:
        "Maybe it's just me, but since we took the leap of becoming a foursome, the band just seems to gel so much better than before."
        "Even when we're only practising, it's as if we know what each other's going to do before we do it, like we're all of one mind."
        "So much so that after the first practice session following our initial four-way dance, the atmosphere in the small space is crazily charged."
        "While I'm playing like a prodigy, I still can't keep from picturing the girls in various compromising positions."
        "And they must be in a similar state, as glances are shooting between all of us, along with lingering stares when someone thinks on one else is looking."
        "When we finally call it a night, it's fairly obvious that no one really wants to call it a night."
        mike.say "Erm...do any of you guys fancy coming back to my place?"
        mike.say "We can...watch something on Netflix, maybe?"
        show kleio at left
        kleio.say "Why don't you just ask us to come round and look at your damn etchings?!?"
        show sasha shout
        sasha.say "Are you trying to ask us all round for a fuck?"
        show sasha normal
        mike.say "Well...now that you mention it..."
        show anna behind kleio at right
        anna.say "That sounds really good to me - otherwise I'd just end up going home and playing with myself until I fall asleep again!"
        "Well, I guess that decides the matter."
        scene bg bedroom1 with fade
        "Almost before I can get my head in gear, we're back at the house and in my bedroom, all four of us eagerly stripping off our clothes."
    "Kleio seems to be the most tired of all, reclining against the headboard in a languid manner."
    "Sasha drapes herself on the side of the bed, her dark eyes open, yet with a sleepiness that only adds to her appeal."
    "In contrast, Anna is the most eager and alert, almost hopping into the middle of the bed like an excitable puppy."
    show band foursome2 with fade
    "Knowing smiles pass between Sasha, Kleio and myself, each of us turned on and woken-up by Anna's seemingly boundless energy."
    kleio.say "Whoa, down girl!"
    "As if sensing that she's putting us in mind of an eager canine, Anna grins and gets onto all fours."
    show band foursome2 annapleasure kleiopleasure
    "She sticks her tongue out and leans in to lick at Kleio's exposed pussy, earning an aroused chuckle for her efforts."
    show band foursome2 annanormal
    "A second later, she looks over her shoulder at me, wiggling her ass as if she had a tail to show off."
    "When she sees the effect she's having on my dick, she grins, beginning to pant and whine."
    "I'm about to literally pounce on Anna's ass, when Sasha rests an elbow upon it and catches my eye."
    "She smiles slowly, reaching out with one hand to caress the underside of my dick, clearly offering me an another choice altogether."
    menu:
        "Fuck Anna's pussy":
            $ CONDOM = False
            if hero.has_condom():
                menu:
                    "Use protection":
                        $ CONDOM = hero.use_condom()
                    "Don't use protection":
                        pass
            if CONDOM:
                "As good as Sasha's lips look right now, I only have eyes for the ones between Anna's legs."
                show band foursome2 condom
                "I hastily snatch up a condom from the bedside table and put it on, parting Anna's buttock still further with my hands once I'm ready."
                show band foursome2 vaginal annapleasure kleionormal
                "There's no need to play around, as Anna's already more than in the mood, and so I sink into her slowly yet surely."
                "Undeterred by the minor snub, Sasha leans in and begins to use her tongue on Anna's exposed ass, while Anna herself continues to lick at Kleio's pussy."
                "Sasha and I find ourselves gazing at Kleio, as she registers the pleasure from Anna's tongue, as if we're passing it through the petite girl and into her body."
                show band foursome2 kleiopleasure
                "Maybe that's why, as soon as I show signs of peaking and Anna begins to cry out in turn, Kleio begins to clamber up the headboard as her own climax builds as well."
                "I'm all but pounding at Anna's pussy when I finally cum, her buttocks quivering with each thrust."
                "The condom catches everything as it's supposed to, but the force of it tips Anna over the edge as well."
                "She gives up on licking at Kleio's pussy to let out a desperate cry as she succumbs to her orgasm."
            else:
                "What can I say - Anna's pussy is calling to me, and so I answer in kind."
                show band foursome2 vaginal annapleasure kleionormal
                "It only takes a matter of seconds to push into Anna, as she's already slick and welcoming."
                "As I begin to thrust into her, Sasha leans over the other girl's buttocks and starts to lick at her taut ass."
                "Anna herself has not stopped doing the same to Kleio's pussy, and now all four of us are coming together as one mass of heads, limbs and holes that are begging to be filled."
                show band foursome2 kleiopleasure
                "It's Kleio that seems to begin cumming first, throwing her back against the wall and moaning deeply."
                "Then the same reaction almost cascades through us, first with Anna quivering, and then the feeling that I'm about to cum seconds later."
                "Anna fits me like a glove, squeezing me so tightly that I can't imagine there's room inside of her for anything else at all."
                show band foursome2 creampie annaahegao with vpunch
                "But when I finally lose myself and burst in that same exquisite place, the result is explosive."
                $ anna.impregnate()
                "Anna shrieks in helpless arousal as she too now begins to cum, the inside of her pussy squeezing me like a clenching hand."
        "Show Sasha who's the boss" if sasha.sub > 75:
            "I can see both the lips of Anna's pussy and the black-painted lips of Sasha's mouth, both slick, appealing and within reach."
            "It's so hard to choose between them, that I decide I won't."
            show band foursome2 annapleasure anal
            "Firstly I seize Anna's pert buttocks and thrust into her as deeply as I can."
            "She squeals with pleasure, and I watch disappointment cross Sasha's face at being overlooked."
            show band foursome2 annanormal blowjob
            "But after only a handful of thrusts, I pull out without warning and force Sasha's lips around my cock."
            "She chokes in surprise for a moment, but obliges, rather than suffocate, and is soon pleasuring me with some enthusiasm."
            show band foursome2 annapleasure anal
            "Before she can make me cum, I pull away from her and without warning stick my dick back into Anna's ass."
            "Her exhausted panting once again becomes a more intense squeal of pleasure."
            "Sasha watches me from where she's laid, saliva dripping down her chin."
            "I can see confusion on her face, her cheeks flushed red, but her hand already sliding towards her pussy in arousal."
            if game.week_day % 2 == 0:
                "I already know how much Anna loves being taken up the ass, and that turns me on all the more."
                "I can't help but keep on thrusting myself ever harder into Anna's pert little ass, and all too soon I feel myself cumming."
                show band foursome2 annaahegao creampie with vpunch
                "I don't think that I could pull out if I tried, and I listen to her cries of arousal as I release myself into her without pause."
            else:
                "But a second later, I realise that I'm on the brink of cumming too."
                "I decide that Sasha should be rewarded..."
                menu:
                    "Cum in Sasha's mouth":
                        show band foursome2 blowjob cumshot with vpunch
                        "I seize the sides of her head with my hands, pushing her down as my orgasm finally hits."
                        show band foursome2 -blowjob -cumshot cum onsashamouth annanormal
                        "As I hear Sasha gag and splutter with her mouth full of cock and cum alike, I just hope she remembered to breathe through her nose."
                    "Cum on Sasha's face":
                        show band foursome2 -anal
                        "I decide to pull my dick out of Anna's ass."
                        show band foursome2 cumshot with vpunch
                        "Still slick with juices, it nods for a moment before Sasha's face, and then releases itself in a sudden fountain."
                        show band foursome2 -cumshot dickcum cum onsashaface onannabody onkleiobody annanormal
                        "Her mouth open in shock, Sasha is splattered with the sticky, white mass, making me feel a little like an animal marking its territory."
            $ anna.flags.anal += 1
        "Fuck Anna's ass" if sasha.sub <= 75:
            "All I can see is Anna's ass, shaking from side to side, and in that moment I want it more than anything I can imagine."
            show band foursome2 annapleasure anal
            "Taking a buttock in each hand, I mercilessly thrust myself into her anus, pushing until I'm as deep as I can get."
            "Anna's squeal of surprise serves only to turn me on all the more, making me start pumping away in the hope of eliciting more."
            "As I begin to thrust into her, Sasha leans over the other girl's buttocks and starts to lick at her taut ass and my shaft at the same time."
            show band foursome2 kleiopleasure
            "It takes all of Anna's willpower to keep on doing the same to Kleio, as she finds herself being pleasured from two angles at once."
            "As we all begin to build to an inevitable climax, I can't help wondering if we're turned on by Anna's cries just because we're aroused her."
            "Or because she sounds like a wounded, helpless animal and we're all suddenly on the hunt."
            "I already know how much Anna loves being taken up the ass, and that turns me on all the more."
            show band foursome2 annaahegao creampie with vpunch
            "I can't help but keep on thrusting myself ever harder into Anna's pert little ass, and all too soon I feel myself cumming."
            "I don't think that I could pull out if I tried, and I listen to her cries of arousal as I release myself into her without pause."
            $ anna.flags.anal += 1
        "Fuck Sasha's mouth" if sasha.sub <= 75:
            "Anna's lips look appealing, but not as much as Sasha's, black-painted and currently being licked provocatively by her tongue."
            "I turn my dick to face Sasha, suddenly forgetting about Anna's proffered ass."
            show band foursome2 blowjob
            "Sasha looks more than a little triumphant as she begins to kiss and lick the tip of my dick."
            "Before too long she opens her lips wider and slowly slides the head into her mouth, then as much of the shaft as she can take."
            "In that moment, I forget that there are two other girls in the room, being inside Sasha's mouth feels that damn good."
            show band foursome2 annapleasure kleiopleasure
            "Anna and Kleio must have kept on with whatever they were doing, as I can hear moaning that's not me and simply can't be Sasha."
            "But a second later, I realise that I'm on the brink of cumming too."
            menu:
                "Cum in Sasha's mouth":
                    "I don't know if Sasha is planning on releasing me before I cum, but that's not what I want to happen."
                    show band foursome2 cumshot with vpunch
                    "Instead I seize the sides of her head with my hands, holding her down as my orgasm finally hits."
                    show band foursome2 -blowjob -cumshot cum onsashamouth
                    "As I hear Sasha gag and splutter with her mouth full of cock and cum alike, I just hope she remembered to breathe through her nose."
                "Cum on Sasha's face":
                    show band foursome2 -blowjob
                    "Before Sasha can make the decision for me, I pull my dick out of her mouth."
                    show band foursome2 cumshot with vpunch
                    "Still slick with her spit, it nods for a moment before her face, and then releases itself in a sudden fountain."
                    show band foursome2 -cumshot dickcum cum onsashaface onannabody onkleiobody
                    "Her mouth open in shock, Sasha is splattered with the sticky, white mass, making me feel a little like an animal marking its territory."
    hide band with fade
    "It seems as though everyone has used up the very last of the energy they had left over after the practice session, pushing themselves to the point of orgasm."
    "Even Kleio, who was mostly immobile during the four-way love-making session, is all but ready to collapse into unconsciousness."
    "I'm not sure if I should be calling ubers for people or else offering to put them up for the night."
    "But the sound of Anna's loud snoring puts paid to any question of kicking the girls out before morning."
    "I count myself lucky for having bought a bed almost large enough for all four of us to sleep comfortably in."
    "But more lucky to be able to share it with three women the likes of Sasha, Kleio and Anna."
    if appointment:
        $ game.pass_time(2)
    else:
        call sleep from _call_sleep_4
    $ game.room = "bedroom1"
    return

label anna_kleio_propose_male:
    "I'd have been pretty nervous at the prospect of getting down on one knee and asking any one girl to marry me."
    "So you can imagine how scary the idea of doing it with two of them must feel, right?"
    "And as if all of that wasn't enough, this is Anna and Kleio we're talking about too."
    "I mean, neither of them is exactly what you'd call a simple, traditional kind of girl either!"
    "But they are the women that I love, the ones that I want to spend the rest of my life with."
    "So I guess that I'm just going to have to do my best to figure this one out."
    "Since they made polygamy legal so recently, I must be one of the first guys to have done this."
    "Which means there's nothing else to go on other than what feels right."
    "And that's how I come to be going down on one knee in front of Anna and Kleio."
    "I've tried to keep it as traditional as I can, springing it on them out of the blue."
    "And I guess that's why it takes them a little while to actually look around and see me down here."
    show anna at left5
    show kleio at right5
    with dissolve
    anna.say "Ooh, I didn't see you down there!"
    show anna surprised
    anna.say "What's the matter, [hero.name]?"
    kleio.say "Yeah, Loverboy, what's up?"
    show kleio annoyed
    kleio.say "You slip on a turd or something?"
    "As usual, I can read Anna's face like a book, seeing how confused she is by my actions."
    "But I also know the way that Kleio tries to cover up her own emotions pretty well by now too."
    "And so I can tell that underneath her bluster, she's been caught off guard just as much as Anna."
    "Maybe I should offer them some kind of explanation, just for the sake of reassurance."
    "But by now I'm already reaching into my pocket for the matching rings that I bought for the occasion."
    "All of this means that the first words out of my mouth might explain the situation."
    "But they also instantly turn all attention onto Anna and Kleio, literally putting the question to them."
    show anna normal
    show kleio normal
    mike.say "Ah...Anna...Kleio..."
    mike.say "I wanted to ask..."
    mike.say "Will you marry me?"
    mike.say "And each other too, I guess!"
    show anna surprised at left5, vshake
    show kleio surprised at right5, vshake
    "I honestly never thought it possible for Anna's eyes to get any wider, but they do."
    "She shakes her head in silence, and I can only hope it's simply from disbelief."
    "Kleio is silent too, her normally smart mouth hanging open in surprise."
    "So no matter what happens next, I can say one thing for sure."
    "That I finally managed to say something that she didn't have a smart comeback for!"
    "All this time, I'm looking up at them, from Anna to Kleio and back again."
    "It can't have been more than a minute at the most since I asked the question."
    "But it's starting to feel like I've been down here for an age."
    hide anna
    hide kleio
    with moveoutleft
    "Suddenly, Kleio spins Anna around, pulling her into a tight huddle."
    "Their heads are turned away from me as they begin to converse in hushed tones."
    "And no matter how hard I try, there's no way I can hope to hear what they're saying."
    "The only thing I can do is wait, hope stirring in my chest every time one of them looks my way."
    "Each time expecting an answer that, for better or worse, will put me out of my misery."
    show anna at left5
    show kleio at right5
    with moveinleft
    "But when they finally come out of the huddle, it does nothing to lessen the tension that I'm feeling."
    "Because now I'm waiting to hear their answer, for them to decide my fate."
    "And it seems that any ability I might have had to read their expressions has completely deserted me..."
    if anna.love < 195 or kleio.love < 195:
        show anna blush
        anna.say "[hero.name], this is all so sweet of you!"
        show kleio seductive
        kleio.say "Yeah, Loverboy - even I'm touched, you know?"
        "Oh shit - this can't be anything other than bad."
        "They're just flattering me right now, telling me how nice it was of me to propose to them."
        "There's not been a single hint at them saying yes or no."
        "And they wouldn't feel the need to spare my feelings or butter me up if it was a yes."
        "So it can only be a no."
        mike.say "But you don't want to marry me, right?"
        show anna surprised
        "Anna's eyebrows shoot up the moment that I say this, and she looks genuinely shocked."
        anna.say "Wha..."
        anna.say "But how did you know?!?"
        show kleio annoyed
        "Even though Kleio rolls her eyes at Anna's outburst, I can see that there's more in her expression."
        "She understands that they've pretty much showed me their hand, let me know their intentions."
        kleio.say "It doesn't matter how he knows, Anna."
        kleio.say "All that matters is how he takes it."
        show anna annoyed
        "I pause before answering, holding Kleio's eye the whole time."
        "As always, there's an unspoken challenge in them."
        "But I can sense a deeper melancholy in there too, almost a sadness at what's happening here."
        "Almost as if Kleio knows that she's hurting me."
        "And yet still can't say yes just for the sake of my feelings."
        mike.say "I...I understand, Kleio."
        mike.say "It's no big deal..."
        show kleio normal
        kleio.say "It's not you, Loverboy - and I mean that."
        kleio.say "We're just having so much fun right now, you know?"
        kleio.say "We're not ready to put a ring on it and settle down yet."
        show anna normal
        show fx question at left5
        anna.say "We...we don't have to break up now - do we?!?"
        "I shake my head, trying to be grateful for what I have right now."
        "I keep telling myself that things are good and that they don't need to change just yet."
        mike.say "No, Anna - we don't have to break up."
        mike.say "If you two still want me, I know I still want you."
        show anna happy
        anna.say "Yay!"
        anna.say "Let's celebrate with some hot, make-up sex!"
        show kleio seductive
        "Kleio shoots me a look of ironic amusement, and I laugh along with her."
        show kleio normal
        "But I can almost feel the relief coming off of her at the same time..."
        $ anna.love -= 25
        $ anna.sub -= 25
        $ kleio.love -= 25
        $ kleio.sub -= 25
    else:
        "The moment that Anna and Kleio turn around to face me, I lean forward in anticipation."
        "But then Kleio takes me completely by surprise, snatching the rings out of my hand."
        "I watch in stunned silence as she proceeds to jam one onto Anna's finger."
        "And then slides on onto her own as well!"
        kleio.say "You're in luck, Loverboy."
        show kleio happy
        kleio.say "It's a yes!"
        show anna happy
        anna.say "Yeah, [hero.name] - we'd love to marry you."
        anna.say "And each other too!"
        "I begin to get to my feet, trying to find the words to express what I'm feeling right now."
        "But my lips just end up moving with nothing emerging at all, I'm that overwhelmed."
        show kleio normal
        kleio.say "Don't sound too excited, Loverboy."
        kleio.say "Wouldn't want to make a girl feel too special, would we!"
        show anna wink
        anna.say "Oh, don't listen to her, [hero.name]."
        anna.say "She's just teasing."
        anna.say "And she's hiding that she's just as excited as me!"
        mike.say "I...I'm pretty excited too, Anna!"
        kleio.say "And so you should be, Loverboy."
        show kleio seductive
        kleio.say "It's not every day that a loser like you gets a yes from two hot babes!"
        show anna normal
        anna.say "Hey, Kleio - if he's a loser, what does that make you?"
        anna.say "After all, you are marrying him!"
        show kleio blush
        kleio.say "I...well...that's not what I..."
        kleio.say "Ah, shut up, Anna!"
        show anna evil
        "A feline grin spreads across Anna's face."
        "A grin that shows how happy she is to have backed Kleio into a corner for once."
        mike.say "Lay off of her, Anna."
        mike.say "We should be celebrating right now, all three of us."
        show anna happy
        anna.say "Okay, [hero.name], if you say so."
        anna.say "Wait a minute - I got a ring and so did Kleio."
        anna.say "But what about you?"
        anna.say "Should be get you one too?"
        show kleio happy
        "At this I see Kleio begin to smile again, recovering from her previous funk."
        kleio.say "I got a ring you can wear, Loverboy."
        "She presses her hands against her buttocks, squeezing them as she does so."
        kleio.say "It's right down here."
        kleio.say "And I don't want to put it on your finger either..."
        "I hear Anna begin to giggle nervously as I start to sweat."
        "If this is a taste of what married life has in store for me..."
        "Well, here's to it lasting as long as the three of us live!"
        $ anna.set_fiance()
        $ kleio.set_fiance()
    hide kleio
    hide anna
    return

label anna_kleio_male_ending:

    if renpy.has_label("band_harem_achievement_3") and not game.flags.cheat:
        call band_harem_achievement_3 from _call_band_harem_achievement_3
    $ game.hour = 16
    show bg nightclub with fade
    "Like most guys, I never spent too much time wondering what the whole thing would look like when I got married."
    "Hell, I never even spared much of a thought for IF I'd ever actually get married in the first place."
    "And while I know that it's a stereotype that a girl has it all planned out in her head, years in advance."
    "I kind of think that Anna and Kleio probably never saw it turning out like this either!"
    "Never mind that there's three of us tying the knot today, which is cray enough on its own."
    "But then you can throw in on top of that the fact that we chose to do it all in a nightclub too!"
    "I mean, obviously not a random one."
    "This is our favourite spot to spend the night dancing together in the most provocative manner possible."
    "Somewhere that we made some of the best memories that we have as a trio too."
    "When we sat down to thrash out all of the details, it just seemed to make perfect sense."
    "After all, we don't have the most average of relationships, so why have an average wedding?"
    "And then there's all of the little stuff that you don't think of until the time comes."
    "For instance, who stands at the altar and who walks down the aisle?"
    "Does anyone get given away to the other two, or is it the other way around?"
    "In the end, choosing the nightclub solved a good number of those issues all at once."
    "Because there's no altar to stand in front of or aisle to walk down, we just ignored all of that."
    "Instead, we're all standing in front of a crowd of guests that's currently filling the dance-floor."
    "And yeah, the priest was a little stumped by the sight of a DJ box, rather than an altar."
    "But he seemed to get into the spirit of things pretty quickly."
    "If I had to guess, I'd say that the look on his face means he's intrigued to see how this thing goes."
    "And he's certainly not the only person in here that's feeling that way too!"
    "I think the entire guest-list, as well as the three of us are in the same boat."
    show anna wedding b at left5
    show kleio wedding at right5
    with dissolve
    "Well, maybe not so much Anna."
    "She seems to be pretty high on excitement right now, almost bouncing up and down on the spot."
    show anna b happy
    "When I meet her eyes, she smiles so wide that I expect the top of her head to fall off."
    "But as my gaze moves on, I lock eyes with Kleio, who's checking Anna out too."
    "And before she can put on a show of being nonchalant and cocky, I catch the true emotions in them."
    show kleio happy
    "She's every bit as excited as Anna, just that much better at hiding it."
    if anna.is_visibly_pregnant and kleio.is_visibly_pregnant:
        "Plus there's the fact that everyone's staring at Anna and Kleio's swollen bellies!"
        "Their dresses can't hope to hide the fact that they're so close to giving birth."
        "But they can all think what they like, as the three of us can't wait to meet the babies."
    elif anna.is_visibly_pregnant:
        "Plus there's the fact that everyone's staring at Anna's swollen belly!"
        "Her dress can't hope to hide the fact that she's so close to giving birth."
        "But they can all think what they like, as the three of us can't wait to meet the baby."
    elif kleio.is_visibly_pregnant:
        "Plus there's the fact that everyone's staring at Kleio's swollen belly!"
        "Her dress can't hope to hide the fact that she's so close to giving birth."
        "But they can all think what they like, as the three of us can't wait to meet the baby."
    else:
        "But if their moods and demeanour don't match, their dresses certainly do."
        "Despite the differences in their figures, Anna and Kleio chose to wear the exact same dress."
        "I'm not sure if anyone else gets the joke, but it seems to amuse them greatly."
    show kleio normal
    show fx question at right5
    kleio.say "What the hell are you staring at, Loverboy?"
    "Kleio hisses the words at me, but not with any kind of venom or irritation."
    hide fx
    show anna b surprised
    "Anna hears her too, and looks first to Kleio and then to me."
    "And I see confusion growing on her face the whole time."
    mike.say "You want to know what I'm staring at, Kleio?"
    mike.say "I'm staring at the two girls I love."
    mike.say "Because they're fucking hot and I can't wait to be married to them!"
    show anna wedding b blush
    anna.say "Aww!"
    anna.say "[hero.name], that's SO romantic!"
    show kleio seductive
    kleio.say "Touche, Loverboy."
    kleio.say "Nice comeback!"
    show anna b normal
    show kleio normal
    "Priest" "Ahem..."
    "At the sound of the priest clearing his throat with authority, all eyes snap forwards as one."
    "Priest" "Please be seated."
    "That request earns him an entire roomful of people shrugging and shaking their heads."
    "And the priest is soon copying those same gestures himself when he realises there are no chairs to be had."
    "Priest" "Ah...remain standing then."
    "Priest" "Dearly beloved."
    "Priest" "We are gathered here today to witness the joining of these three souls in matrimony."
    "The rest of the ceremony is just the usual stuff that everyone knows off by heart."
    "Sounds weird, I know, but not all that much changes when you add a third person in there!"
    "And before long, we arrive at the exchanging of vows..."
    "Priest" "Do you, Anna, take Kleio and [hero.name] to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    show anna wedding b happy
    anna.say "Ooh, I sure will!"
    "Priest" "Do you, Kleio, take Anna and [hero.name] to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    show kleio wedding annoyed
    kleio.say "Sure, what the hell - in for a penny, in for a pound!"
    with vpunch
    mike.say "KLEIO!"
    show anna surprised b at left5, vshake
    show fx exclamation at left5
    anna.say "KLEIO!"
    show kleio happy
    kleio.say "Okay, okay...I will!"
    show anna b normal
    show kleio normal
    hide fx
    "Priest" "And do you, [hero.name], take Anna and Kleio to be your lawful, wedded partners?"
    "Priest" "Will you honour and obey them, comfort and support them?"
    "Priest" "And, forsaking all others, be faithful to them as long as you all shall live?"
    mike.say "I will."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married in the eyes of the law."
    "Priest" "You may kiss as a symbol of your union."
    show anna b happy
    show kleio happy
    "I can't help beaming like a loon as I look at Anna and Kleio."
    "We did it, we actually did it - I'm married to the two most beautiful girls in the world!"
    "I can sense that we're coming together for a picture-perfect embrace."
    "That and a kiss that'll be a timeless work of art."
    show anna wedding b at center, zoomAt(2, (440, 1380))
    show kleio wedding surprised at center, zoomAt(2, (840, 1380))
    with hpunch
    "But then, in the same moment, Kleio and I let out a yell of surprise."
    "We're dragged together as Anna almost tackles us to the ground in an aggressive hug."
    anna.say "You heard the man - let's press lips!"
    show anna b blush
    show kleio seductive blush
    "And with that, she brings us all together in a three-way embrace."
    "All the time I'm hoping that someone's taking pictures of this."
    "Because it's got to be the hottest thing that's ever happened to me at a wedding!"
    "We haven't even finished as the music we chose begins to play and the ceremony comes to an end."
    "The dance-floor fills around us as the guests start to move, but none of us seems to notice."
    "There'll be plenty of time for us to chat to all of those whom we invited."
    "But right now the only thing that matters is showing Anna and Kleio how much I love them..."
    scene bg park
    show anna at left5
    show kleio at right5
    with fade
    kleio.say "You just leave this to me, Anna."
    kleio.say "These guys want to hear from the one that wears the trousers in this relationship."
    kleio.say "Trust me on that!"
    show anna angry
    anna.say "Hey, Kleio!"
    anna.say "You promised that you'd be nice."
    anna.say "And you're not wearing trousers either - those are hot pants!"
    show kleio annoyed
    kleio.say "Anna, I don't mean..."
    show anna annoyed
    anna.say "You hardly ever wear trousers...or jeans."
    anna.say "[hero.name] wears them all the time, and I have some pairs of my own."
    anna.say "But you..."
    show kleio angry at right5, hshake
    kleio.say "ANNA..."
    show kleio normal
    kleio.say "Anna...will you please stop talking about trousers."
    kleio.say "It was a metaphor, you know - a turn of phrase?"
    show anna normal
    anna.say "Oh, I see!"
    anna.say "Sorry, Kleio - I guess I got a little confused."
    show kleio annoyed
    kleio.say "Urgh..."
    show kleio normal
    kleio.say "Now do you see why I wanted to handle this myself?"
    anna.say "Okay, okay."
    anna.say "If you think that's for the best."
    kleio.say "So, where was I..."
    anna.say "You were talking about trousers, Kleio."
    kleio.say "Thanks, Anna."
    show anna wink
    anna.say "You're welcome."
    kleio.say "Anyway, I know that everyone's been waiting for this to happen."
    kleio.say "To hear all about our relationship from my point of view instead of Loverboy's!"
    show anna normal
    anna.say "And me, Kleio - don't forget about me too!"
    show kleio annoyed
    kleio.say "How could I ever forget about you, Anna?!?"
    show anna happy
    anna.say "Aww, thanks, Kleio - you're unforgettable too!"
    kleio.say "Yeah, that's kind of not what I meant."
    show kleio normal
    kleio.say "But whatever..."
    kleio.say "Can you actually believe that we're both married to Loverboy?"
    kleio.say "Who could have seen that coming!"
    show anna normal
    anna.say "Well, I kind of could."
    show kleio surprised
    kleio.say "What?"
    show kleio annoyed
    kleio.say "Get the hell out of here, you lying little cow!"
    show anna happy
    anna.say "Ha, ha..."
    anna.say "It's true, Kleio, really it is."
    show anna normal
    anna.say "I thought [hero.name] was cute the second he walked into the practice room."
    anna.say "But I knew you thought he was too when you were SO rude to him all the time."
    kleio.say "Hey - I was rude to him because I thought he was a jerk."
    kleio.say "You know, a typical guy?"
    anna.say "Oh no, Kleio - you were being that other kind of rude."
    anna.say "The kind where you really like someone, but can't admit it."
    anna.say "So you're kind of a bitch to them instead."
    kleio.say "We're supposed to be talking about Loverboy here, not me!"
    anna.say "Okay, Kleio."
    anna.say "You tell them all about how you totally didn't fall for him."
    anna.say "Or jump at the chance to have a threesome with me too!"
    show kleio happy
    kleio.say "Yeah, well...that was one of the best things about him walking into our lives."
    kleio.say "Getting to be with a pretty hot guy and one of my best friends at the same time!"
    show anna happy
    anna.say "Aww, you old romantic, you!"
    anna.say "It is neat there being three of us."
    anna.say "As it means you're never lonely, or bored either!"
    if anna.is_visibly_pregnant and kleio.is_visibly_pregnant:
        anna.say "And there'll be five of us soon too!"
        show kleio annoyed
        kleio.say "Urgh...don't remind me."
        kleio.say "I feel like a fucking whale right now!"
        show anna normal
        anna.say "Don't worry, Kleio."
        anna.say "We can put [hero.name] on nappy duty as soon as Tommy and Courtney are born!"
        kleio.say "Hell yeah."
        kleio.say "He was the one that got us both pregnant in the first place!"
    elif anna.is_visibly_pregnant:
        anna.say "And there'll be four of us soon too!"
        kleio.say "Bags not having to be there for nappy changing duty!"
        show anna angry at left5, hshake
        anna.say "KLEIO!"
        kleio.say "Joking, Anna."
        kleio.say "Don't worry - I'll be there to help out with Tommy."
    elif kleio.is_visibly_pregnant:
        kleio.say "And there'll be four of us soon too."
        show anna annoyed
        anna.say "Eww - stinky nappies!"
        show kleio angry at right5, hshake
        kleio.say "ANNA!"
        show anna normal
        anna.say "Sorry, Kleio."
        anna.say "Don't worry - I'll be there to help out with Courtney."
    scene bg black with dissolve
    pause 0.2
    show picnic with timelaps
    kleio.say "It helps to pass the time while we're on the road too."
    kleio.say "Makes all those new towns and cities easier to deal with."
    anna.say "Mmm...yeah - no more roadies and needy fans for this girl, no sir!"
    kleio.say "Anna, you little hussy!"
    anna.say "Aw, cram it, Kleio."
    anna.say "I love [hero.name]'s cock, and so do you!"
    kleio.say "Yeah, I guess you're right."
    kleio.say "Bags getting a hold of it tonight!"
    anna.say "Ooh, Kleio - that's not fair."
    anna.say "You had it last time!"
    kleio.say "You snooze, you lose, Anna!"
    kleio.say "But seriously, Loverboy should be the one begging us."
    kleio.say "He SO lucked out landing two hot bitches the likes of me and you!"
    anna.say "Yeah, I guess we are pretty special!"
    kleio.say "And I'm never gonna let him forget that."
    kleio.say "No way, no how!"
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label anna_sasha_propose_male:
    show anna normal at left5
    show sasha normal at right5
    "There's a few notable things that I never thought I'd actually get to do in my lifetime."
    "One of them was live in a house with two seriously hot girls."
    "Another was to be in a seriously kick-ass band, totally killing it on guitar."
    "But probably the most impossible of all was dating two girls at the same time."
    "And what do you know - I've managed to do all of them."
    "Plus the girls involved in each of them cross over too!"
    "I'm gigging with Anna and dating her."
    "At the same time I'm living with Sasha, gigging with her AND dating her."
    "And it's not like I'm feeling the pressure of it all either."
    "Living, gigging and dating are all going on at the same time."
    "We're having a great time, and things only seems to be getting better."
    "In fact, I kind of feel like I want to be in this thing for the long-term."
    "And that's why I have a pair of rings in my pocket the next time I see the girls."
    "I do my best not to let on that I have something in mind."
    "And it seems to work."
    "Anna and Sasha both look surprised when I get down on one knee in front of them."
    show anna surprised at left5
    show sasha stuned at right5
    anna.say "Ooh..."
    anna.say "What's up, [hero.name]?"
    anna.say "Did you drop something?"
    show sasha surprised
    sasha.say "No way, Anna..."
    sasha.say "Did you never watch a single romantic movie?"
    sasha.say "This is the scene where the guy goes down on one knee and pulls out a ring!"
    show sasha stuned
    anna.say "Oh fuck!"
    anna.say "You...you mean..."
    "I can't help chuckling as I take out the rings."
    "They're such a quirky pair, and that's part of why I love them so much."
    mike.say "Anna..."
    show anna normal
    mike.say "Sasha..."
    show sasha normal
    mike.say "Will you marry me?"
    "I smile up at them, silently willing the two of them to say yes."
    if anna.love >= 195 and sasha.love >= 195:
        "Before I can say another word, Anna and Sasha leap into action."
        show anna b happy at center, zoomAt(2, (440, 1300))
        show sasha happy at center, zoomAt(2, (840, 1300))
        with hpunch
        "They both kind of pounce on me at the same time."
        "And before I know it, they hugging and kissing me like crazy."
        show anna blush
        anna.say "Sure thing, [hero.name]!"
        show sasha flirt
        sasha.say "Yeah, count me in too!"
        show sasha normal
        "I try as best I can to stick the rings on their fingers."
        "But in their excitement, Anna and Sasha get in on the act too."
        "And that means we kind of end up jamming them on together."
        mike.say "Oh wow..."
        mike.say "I was so scared you were going to say no!"
        anna.say "Why would we do that?"
        show anna happy
        anna.say "We've been getting on great!"
        show sasha shout
        sasha.say "Yeah, [hero.name]..."
        sasha.say "we're great as bandmates - even better as partners."
        show sasha happy
        sasha.say "So I think we'd make a great threesome in an official capacity too!"
        show sasha normal
        "I can only nod and smile."
        "Because I'm already imagining what the future holds for us."
        $ anna.set_fiance()
        $ sasha.set_fiance()
    elif anna.love < 195 and sasha.love < 195:
        "Anna and Sasha exchange one of those meaningful looks."
        "You know the kind that I mean."
        "One that any girl can read, but no guy can ever understand."
        "And then they nod, turning to look at me as one."
        anna.say "Aw, [hero.name]..."
        show sasha shout
        sasha.say "We're flattered you'd ask."
        show sasha sadsmile
        anna.say "Sure we are!"
        show sasha whining
        sasha.say "But we can't all get married - even if it is legal now."
        show sasha sadsmile
        "I shake my head, trying to argue against their decision."
        mike.say "But why, guys?"
        mike.say "We all get on great, don't we?"
        show anna annoyed
        show sasha annoyed
        anna.say "Well, yeah..."
        show sasha whining
        sasha.say "But that was when we knew that we could bail out anytime."
        sasha.say "If we're married, then it's not fun anymore, [hero.name]!"
        show sasha sadsmile
        "I put the rings away and slowly get to my feet."
        mike.say "Okay..."
        mike.say "If that's really how you feel..."
        show anna normal
        anna.say "Don't be sad, [hero.name]!"
        show sasha shout
        sasha.say "Yeah, we're not dumping you."
        sasha.say "Just saying we don't want to marry you!"
        show sasha normal
        $ anna.love -= 25
        $ anna.sub -= 25
        $ sasha.love -= 25
        $ sasha.sub -= 25
    elif sasha.love < 195:
        "Anna leaps forwards and throws her arms around me."
        show anna b happy zorder 2 at center, zoomAt(2, (440, 1300)) with hpunch
        anna.say "Of course I will, [hero.name]!"
        anna.say "I'd love to marry you!"
        show sasha sad
        "But I can't help noticing that Sasha's holding back."
        show sasha whining
        sasha.say "Aw, [hero.name]..."
        show sasha shout
        sasha.say "I'm flattered you'd ask."
        show sasha whining
        sasha.say "But we can't all get married - even if it is legal now."
        show sasha sadsmile
        "I shake my head, trying to argue against Sasha's decision."
        mike.say "But why, Sasha?"
        mike.say "We all get on great, don't we?"
        show sasha shout
        sasha.say "Sure we do."
        sasha.say "But that was when we knew that we could bail out anytime."
        sasha.say "If we're married, then it's not fun anymore, [hero.name]!"
        show sasha sadsmile
        show anna normal zorder 2 at center, zoomAt(1.5, (440, 1040))
        anna.say "B...but..."
        show anna annoyed
        anna.say "We can still get married, can't we?"
        mike.say "Of course we can, Anna!"
        show anna happy
        "Almost as soon as I say this, Sasha begins to look thoughtful."
        show sasha shout
        sasha.say "Now if you two got married, and we kept this thing going..."
        show sasha flirt
        sasha.say "That'd be quite kinky."
        sasha.say "Yeah, I think I could work with that..."
        $ sasha.love -= 25
        $ sasha.sub -= 25
        $ anna.set_fiance()
    elif anna.love < 195:
        show sasha happy zorder 2 at center, zoomAt(1.5, (840, 1040))
        "Sasha holds out her hand."
        "And I slip the ring onto her finger."
        show sasha stuned
        "But we're both surprised when Anna takes a step back."
        anna.say "Uh-uh!"
        show anna annoyed
        anna.say "I don't want to get married!"
        "Sasha and I exchange a puzzled look."
        sasha.say "Why the hell not, Anna?"
        show sasha sad
        mike.say "Yeah, Anna, why not?"
        mike.say "I thought things were going really great!"
        "Anna huffs a little and looks down at the ground."
        "I guess it must feel like Sasha and I are ganging up on her right now."
        anna.say "Yeah, I know that!"
        anna.say "But if we get married, then things will change."
        anna.say "You'll say they won't, but they will!"
        show sasha whining
        sasha.say "So..."
        sasha.say "Does that mean you don't want [hero.name] and me to get married?"
        show sasha sadsmile
        "Anna shrugs and keeps on sulking."
        show anna happy
        show sasha normal
        anna.say "No...I guess not."
        show anna normal
        anna.say "But we can all still hang out and fool around, right?"
        $ anna.love -= 25
        $ anna.sub -= 25
        $ sasha.set_fiance()
    return

label kleio_sasha_propose_male:
    show kleio normal at left5
    show sasha normal at right5
    "I've been waiting for the perfect moment to do this, because the time has to be right."
    "And that seems to come at the end of a particularly good practice session for the band."
    "All of us are still buzzing with the energy of playing together so well, it feels great."
    "So as soon as I have Sasha and Kleio together, I decide that this is the moment."
    "I know that it's super cliche and that we're supposed to be ultra modern."
    "But who knows, maybe the girls will think it's ironic?"
    "Hoping for the best, I get down on one knee in front of Sasha and Kleio."
    show sasha surprised
    sasha.say "[hero.name]..."
    sasha.say "What are you..."
    show sasha stuned
    show kleio surprised
    kleio.say "No way!"
    kleio.say "Are you..."
    "I don't offer anything in the way of an answer, save for producing two rings."
    kleio.say "He fucking well is!"
    show sasha surprised
    sasha.say "Whoa..."
    sasha.say "This is unreal!"
    show sasha stuned
    "I've got to admit, that's not the kind of reaction I was expecting."
    "But neither of them has tried to make a run for it yet."
    "So I force myself to smile, ignore my nerves and push on."
    mike.say "Sasha..."
    mike.say "Kleio..."
    mike.say "Will you guys marry me?"
    show kleio happy at left5, vshake
    show sasha happy at right5, vshake
    "As one, Sasha and Kleio burst into laughter."
    "Which is something that doesn't exactly shore up my confidence."
    "As soon as they start laughing, the girls seem to realise their mistake."
    sasha.say "Oh no..."
    show sasha shout
    sasha.say "[hero.name], I'm not laughing at the idea of marrying you!"
    show sasha normal
    show kleio normal
    kleio.say "Me neither, I guess!"
    show sasha shout
    sasha.say "It's just so unexpected, you know?"
    show sasha normal
    kleio.say "Yeah, Loverboy - what she said!"
    mike.say "Erm...okay, I guess..."
    mike.say "I was just trying to be spontaneous, yeah?"
    "An awkward silence falls over the three of us."
    "And I find myself kneeling there, waiting for an answer."
    mike.say "Erm..."
    mike.say "So..."
    mike.say "Am I going to get an answer anytime soon?"
    if kleio.love >= 195 and sasha.love >= 195:
        "All of a sudden, Sasha and Kleio seem to snap out of it."
        "Like the idea of us all getting married is instantly real."
        "They exchange a meaningful look, and then turn their gaze on me."
        "And I can't help feeling like I'm about to be rejected!"
        show sasha shout
        sasha.say "Fucking hell, [hero.name]!"
        show sasha happy
        sasha.say "Why didn't we think of that?"
        show sasha normal
        kleio.say "Yeah, Loverboy."
        show kleio happy
        kleio.say "It's kind of a no-brainer."
        kleio.say "Which is maybe why you were the one that did think of it!"
        "I shake my head as Kleio gives me one of her little insults."
        "But then I remember that I have to accept them as they are."
        "Which means dealing with all those cute little quirks she has!"
        mike.say "So that's your answer?"
        mike.say "Because a simple yes or no is more traditional!"
        show sasha happy
        sasha.say "Yes, [hero.name] - I'll marry you!"
        show sasha normal
        kleio.say "Ditto for me, Loverboy!"
        kleio.say "Let's make this thing legal."
        show sasha normal zorder 2 at center, zoomAt(1.5, (840, 1040))
        show kleio normal zorder 1 at center, zoomAt(1.5, (440, 1040))
        "Together they thrust their hands towards me."
        "And I hurry to shove the rings onto their fingers."
        "Almost as if I'm afraid that they'll change their minds if I don't."
        "Getting back to my feet, I watch them admiring the rings."
        "And something occurs to me in that moment."
        mike.say "Hey..."
        mike.say "Wait a minute!"
        mike.say "Don't I get a ring too?"
        sasha.say "Hmm..."
        show sasha shout
        sasha.say "That's a good question."
        show sasha normal
        kleio.say "Yeah, maybe we could get you something we'd all like."
        show kleio punk
        kleio.say "Like a cock-piercing, yeah?"
        $ kleio.set_fiance()
        $ sasha.set_fiance()
    elif kleio.love < 195 and sasha.love < 195:
        "All of a sudden, Sasha and Kleio seem to snap out of it."
        "Like the idea of us all getting married is instantly real."
        "They exchange a meaningful look, and then turn their gaze on me."
        "And I can't help feeling like I'm about to be judged!"
        show sasha whining
        sasha.say "Seriously, [hero.name]..."
        sasha.say "You can't be serious about wanting us all to get married!"
        sasha.say "Can you?"
        show sasha sadsmile
        mike.say "Well..."
        mike.say "I kind of am!"
        kleio.say "Oh come on, Loverboy!"
        show kleio annoyed
        kleio.say "This thing's working out so well for all three of us."
        kleio.say "Why do you want to go and put a ring on it, huh?"
        kleio.say "Make it official and you make it boring too!"
        show sasha sad
        show kleio sad
        "I start getting back to my feet and putting away the rings."
        "All the time I'm trying to put a brave face on it."
        "But it still hurts to experience this kind of rejection."
        show sasha whining
        sasha.say "[hero.name]..."
        sasha.say "You're okay with that, right?"
        show sasha sadsmile
        kleio.say "Yeah, Loverboy!"
        show kleio normal
        kleio.say "We're not dumping your ass."
        kleio.say "Just that we don't want to be your wives!"
        mike.say "Ah..."
        mike.say "Yeah, I'll be fine."
        mike.say "Just give me a little time, okay?"
        $ kleio.love -= 25
        $ kleio.sub -= 25
        $ sasha.love -= 25
        $ sasha.sub -= 25
    elif sasha.love < 195:
        "All of a sudden, Sasha and Kleio seem to snap out of it."
        "Like the idea of us all getting married is instantly real."
        "They exchange a meaningful look, and then turn their gaze on me."
        "And I can't help feeling like I'm about to be rejected!"
        kleio.say "Fuck yeah, Loverboy."
        show kleio happy
        kleio.say "It's kind of a no-brainer."
        kleio.say "Which is maybe why you were the one that did think of it!"
        show sasha whining
        sasha.say "Seriously, [hero.name]..."
        sasha.say "You can't be serious about wanting us all to get married!"
        sasha.say "Can you?"
        show sasha sadsmile
        "I start getting back to my feet and putting away the rings."
        "All the time I'm trying to put a brave face on it."
        "But it still hurts to experience this kind of rejection."
        show sasha annoyed
        show kleio normal
        "And I can see that Sasha and Kleio are staring at each other too."
        kleio.say "Whoa...wait second, Sasha!"
        show kleio surprised
        kleio.say "You don't like the idea of being married to me?"
        show sasha whining
        sasha.say "That's not what I said, Kleio!"
        sasha.say "I meant that I don't like the idea of marriage in general."
        sasha.say "No matter whether you guys are involved or not."
        show sasha sad
        show kleio normal zorder 2 at center, zoomAt(1.5, (440, 1040))
        "Kleio makes a huffing sound and takes hold of my arm."
        kleio.say "Well maybe I do want that!"
        show kleio happy
        kleio.say "How about it, Loverboy?"
        mike.say "I...I guess so, Kleio."
        "Oh boy!"
        "I never saw things going down like this!"
        $ sasha.love -= 25
        $ sasha.sub -= 25
        $ kleio.set_fiance()
    elif kleio.love < 195:
        "All of a sudden, Sasha and Kleio seem to snap out of it."
        "Like the idea of us all getting married is instantly real."
        "They exchange a meaningful look, and then turn their gaze on me."
        "And I can't help feeling like I'm about to be rejected!"
        show sasha shout
        sasha.say "Fucking hell, [hero.name]!"
        show sasha happy
        sasha.say "Why didn't we think of that?"
        show sasha normal
        show kleio sad
        kleio.say "Oh come on, Loverboy!"
        kleio.say "This thing's working out so well for all three of us."
        show kleio annoyed
        show sasha surprised
        kleio.say "Why do you want to go and put a ring on it, huh?"
        kleio.say "Make it official and you make it boring too!"
        "I start getting back to my feet and putting away the rings."
        "All the time I'm trying to put a brave face on it."
        "But it still hurts to experience this kind of rejection."
        show sasha annoyed
        "And I can see that Sasha and Kleio are staring at each other too."
        show sasha whining
        sasha.say "What do you mean by that, Kleio?"
        sasha.say "You think being married to me would be boring?"
        show sasha annoyed
        kleio.say "I meant being married to ANYONE would be boring, Sasha!"
        show kleio normal
        kleio.say "I wanna live my life and have fun."
        kleio.say "Not settle down and play happy families!"
        show sasha normal zorder 2 at center, zoomAt(1.5, (840, 1040))
        "Sasha makes a huffing sound and takes hold of my arm."
        show sasha shout
        sasha.say "Well maybe I do want that!"
        show sasha happy
        sasha.say "How about it, [hero.name]?"
        show sasha normal
        mike.say "I...I guess so, Sasha."
        "Oh boy!"
        "I never saw things going down like this!"
        $ kleio.love -= 25
        $ kleio.sub -= 25
        $ sasha.set_fiance()
    return

label anna_kleio_sasha_propose_male:
    "I've never been the best at playing it cool when I have something on my mind or keeping my intentions a secret."
    "It tends to mean that the effort required makes me mess up what would otherwise be pretty routine tasks."
    "That and leave people with the distinct impression that my mind is elsewhere and on other things."
    "And so the whole of the band time we've been practising at the rehearsal rooms today, I've been a complete screw-up."
    "Nothing that I try to do comes off, and I can feel the way that it's putting the girls off their game too."
    "But I can't exactly tell them that it's because I have four identical rings stuffed into my pocket, can I?"
    "Nor that they feel like a massive weight that's stopping me from concentrating on anything else."
    "Matters come to a head when I hit a pathetic bum note and explode into a tirade of curses."
    "Even the impotent kick that I aim at my amp in a moment of frustration ends up missing the mark!"
    mike.say "Ah, shit!"
    mike.say "For fuck's sake!"
    show kleio annoyed at right with dissolve
    "Kleio snickers at my outburst, shaking her head as she puts down her guitar."
    kleio.say "Whoa there, Loverboy - you don't suck that bad!"
    kleio.say "I mean sure, you DO suck."
    show kleio happy
    kleio.say "But just at the usual sucky level you always do."
    show anna annoyed at left with dissolve
    "Anna looks at her in as much of a disapproving manner as she can."
    "Which means that she still looks as threatening as a slightly peeved puppy."
    show anna angry
    anna.say "Kleio, you should be helping him out, not putting him down!"
    show anna normal
    anna.say "It's okay, [hero.name] - we all have days when we suck."
    show anna happy
    anna.say "You just need to say fuck it and move on!"
    mike.say "Ah, yeah."
    mike.say "Thanks, Anna...I think..."
    show sasha at center with dissolve
    "Ever the peacekeeper and the level-headed one in the band, Sasha steps in to calm things down."
    show sasha shout
    sasha.say "We have been at it for a while now."
    sasha.say "Maybe we should take a break, before we all start to suck?"
    show sasha normal
    show anna normal
    show kleio normal
    "I'm not sure whether Sasha's suggestion gets me off the hook or throws me under the bus."
    "Yet I'm too grateful to have been provided with a way out to even think of questioning it."
    "Once everyone's put down their instruments and we're just hanging out in the practice room, I feel like it's time."
    "Sure, I'm a bag of fucking nerves and practically ruined the session for everyone else tonight."
    "But the rings in my pocket are the very reason I'm in such a state."
    "And it's only going to get worse if I don't do something about it soon."
    "So, here goes nothing..."
    mike.say "Ah...guys?"
    show fx question as qmark1 at center
    show sasha shout
    sasha.say "Yeah, [hero.name]?"
    show sasha normal
    show fx question as qmark2 at left
    anna.say "Huh, what?"
    show fx question as qmark3 at right
    kleio.say "You got something to say, Loverboy?"
    "They're all looking at me right now, and I have their total, undivided attention."
    "Come on [hero.name] - don't screw this up too!"
    mike.say "The thing is, it's not just one of those days when I can't play for shit."
    show kleio happy
    kleio.say "Which is pretty much every day of the week!"
    mike.say "Ha, ha, Kleio - very funny!"
    mike.say "But no, hear me out, guys, please."
    show kleio normal
    "I take in a deep breath, hold it for a second and then let it out again."
    mike.say "I've never been in a band like this one before, you know?"
    mike.say "Never been so close to a bunch of girls like you, either."
    mike.say "It used to be that when we played together, something just clicked in my head."
    mike.say "It felt right, and in a way that I still can't explain or put into words."
    mike.say "And then, when we became so much more than that..."
    "I have to stop there, holding in my emotions before they get the better of me."
    "And yeah, I know it sounds lame - the wannabe rock-star in a foursome almost crying."
    "But I just can't help the way that I feel right now."
    mike.say "Well, let's just say I've never so happy, so complete in my life."
    mike.say "I love you all more than I can say."
    mike.say "And...and..."
    "I don't even realise it, but I'm sinking down onto one knee as I say all of this."
    mike.say "Will the three of you marry me?"
    mike.say "And...I guess each other too?"
    show anna surprised
    show kleio surprised
    show sasha stuned
    "I fumble for the box that contains the rings, popping it open and offering it to them as I do so."
    "Silence falls over the room as Sasha, Anna and Kleio look at me, the rings and then each other..."
    if anna.love < 195 or kleio.love < 195 or sasha.love < 195:
        "Kleio's the first to react, waving her hands in front of her as shakes her head."
        "She backs away from me until she collides with one of the amps, as if I'm infectious all of a sudden."
        show kleio annoyed at right
        kleio.say "Whoa there, Loverboy!"
        kleio.say "That's a big ask, you know?"
        show anna b surprised zorder 2 at center, zoomAt(1.5, (340, 1040))
        "By way of contrast, Anna moves towards me, her face a picture of worry and incomprehension."
        "Her head is shaking, and her eyes are on the brink of streaming with tears."
        anna.say "Ooh, I'm all confused, [hero.name]!"
        anna.say "Who'd have to move in with who?"
        anna.say "And would I be Kleio and Sasha's wife or husband?!?"
        show sasha normal
        "The only source of relief for me in this moment of complete and utter humiliation is Sasha."
        "She somehow manages to remain pretty stable, nodding her head for me to get up off of my bent knee."
        "But all the same, I can see that the smile on her face is somewhat pained."
        "And I guess that she's torn between her own emotions and sympathy for my own rejection."
        show sasha shout
        sasha.say "Don't let it get to you, [hero.name]."
        sasha.say "I know that you were coming from a good place, we all do."
        sasha.say "But maybe we're just not ready for that kind of commitment yet."
        sasha.say "Maybe in this kind of relationship, that's a decision everyone has to be in on."
        show sasha sadsmile
        "I nod as I hastily stuff the rings back into my pocket, trying to salvage some small measure of dignity."
        mike.say "Yeah, you're probably right, Sasha."
        mike.say "This was a pretty dumb idea on my part!"
        show sasha normal zorder 3 at center, zoomAt(1.5, (640, 1040))
        "Sasha shakes her head as she grabs hold of my hand at this."
        "And though the expression on her face remains the same, I can feel the intensity in her grip."
        show sasha shout
        sasha.say "Don't say that, [hero.name]."
        sasha.say "It's not dumb to do something like that out of love."
        sasha.say "We might not have been ready for it, I know."
        sasha.say "But you just showed the three of us how devoted you are."
        sasha.say "And that's got to count for something, right?"
        show sasha normal
        "I nod, feeling myself able to smile about it for the first time."
        "In fact, I can even start to see the bright side of the situation."
        "I guess that's just something that Sasha has a talent for - finding those elusive silver linings in life."
        $ anna.love -= 25
        $ anna.sub -= 25
        $ kleio.love -= 25
        $ kleio.sub -= 25
        $ sasha.love -= 25
        $ sasha.sub -= 25
    else:
        "Kleio takes everyone by surprise as she elbows Anna and Sasha out of the way."
        "She practically snatches one of the rings out of the box and rams it onto her finger."
        "And then she holds it up like a trophy, waving her hand in the air the whole time."
        show sasha normal
        show kleio a happy zorder 1 at center, zoomAt(1.5, (940, 1040)), hshake
        kleio.say "HAH...YES...YES!"
        kleio.say "Someone DOES want to marry me!"
        kleio.say "In your face Mom...shove it Dad..."
        "She stops dead as she realises all eyes are now on her."
        "Slowly, Kleio lowers her hand."
        "But I note that she still holds the ring against her chest."
        "Almost as if she's afraid someone might take it away from her."
        show kleio a annoyed
        kleio.say "What?!?"
        kleio.say "Can't a girl be happy a guy wants to marry her anymore?!?"
        "Sasha shakes her head and Anna looks simply stunned."
        sasha.say "Okay, Kleio, whatever."
        show sasha happy
        sasha.say "Just don't start calling it your precious, yeah?"
        show sasha normal
        show kleio a normal
        show anna b happy zorder 2 at center, zoomAt(1.5, (340, 1040))
        "In the time that Sasha and Kleio have been conversing, Anna reaches out towards the rings."
        "Anticipating her actions, I pluck one from the box and hold it out to her."
        "She looks up at me with those familiar, innocent eyes."
        "And then her face breaks into the sweetest smile I've ever seen."
        show anna b happy
        anna.say "I'd LOVE to be your wife, [hero.name]."
        show anna b normal
        anna.say "But I don't know if this makes me Kleio and Sasha's wife too!"
        anna.say "Or their husband...or what!"
        "I can't help chuckling as I slide the ring onto Anna's finger."
        "Her innocence and honesty are two of the things I love most about her."
        show sasha shout
        sasha.say "I think we can worry about the details later, Anna."
        show sasha normal
        "I look up to see that, while she's speaking to Anna, Sasha's looking at me."
        mike.say "D...does that mean it's a yes from you too, Sasha?"
        show sasha zorder 3 at center, zoomAt(1.5, (640, 1040))
        "Sasha takes one of the rings for herself."
        "But she holds my hands so that I can help her slip it onto her finger."
        show sasha shout
        sasha.say "Really, [hero.name]?"
        sasha.say "I put up with you as a housemate."
        sasha.say "I let you into the band."
        sasha.say "And I let you into my bed too."
        sasha.say "Haven't you got the hint yet?"
        show sasha happy
        sasha.say "Yeah, I really do want to share my life with you!"
        show sasha normal
        "That only leaves one ring in the box, and so I pick it up myself."
        mike.say "I don't know how these things work, you know?"
        mike.say "But the guy usually has a ring too, and we're all equal partners in this thing."
        mike.say "So I got myself one as well..."
        "Without a single word, Sasha takes the ring from me."
        "And then the three of them put it on my finger as one."
        show kleio happy
        kleio.say "Well, now it's official, you need to get the wedding sorted, Loverboy!"
        show anna b happy
        anna.say "Ooh, yeah - are we going traditional or doing something crazy?!?"
        mike.say "Well, I have got something in mind for that too..."
        $ anna.set_fiance()
        $ kleio.set_fiance()
        $ sasha.set_fiance()
    hide kleio
    hide anna
    hide sasha
    return

label anna_kleio_sasha_male_ending:

    if renpy.has_label("band_harem_achievement_6") and not game.flags.cheat:
        call band_harem_achievement_6 from _call_band_harem_achievement_6
    $ game.hour = 16
    scene empty_stage
    "The gig's been going exceptionally well, with the four of us on fire and the audience lapping up everything we play."
    "I don't know whether we're just on top of our game tonight, or if we're high on what we have planned for the end of the gig."
    "Either way, I know that none of us are ever going to forget this performance, and I hope the crowd won't either!"
    "No one makes mention of what's to come, until we get to the point in the gig where we'd normally do an encore."
    "But instead of that, Kleio grabs the mic and makes a chopping gesture with her hand."
    "The crew have been pre-warned about what's going to happen, and this is their signal to get ready."
    show kleio a date with dissolve
    kleio.say "Okay, you fucking reprobates, listen up!"
    kleio.say "This is the time we'd usually be tickling your pussies with an encore."
    kleio.say "But not tonight, oh no."
    "This meets with the predictable round of boos and pleas for more from the audience."
    "But Kleio stands firm, shaking her head and refusing to be swayed by either."
    show kleio a date annoyed
    kleio.say "Uh-uh, not gonna happen, people."
    kleio.say "And that's because you're gonna get to see something pretty unique happen up here."
    "She turns to wave an arm over the stage, taking in the rest of us as we let her speak for the whole band."
    kleio.say "You know me, Kleio, the voice of the Deathless Harpies."
    show anna date b at left
    show kleio a date normal
    show sasha date at right
    with dissolve
    kleio.say "You know Sasha, on bass and Anna on drums too."
    kleio.say "You may not know [hero.name] on guitar as well."
    kleio.say "But when he joined us, we went from a trio to a four-piece."
    show kleio seductive
    kleio.say "And since then, well...let's just say it's turned into a foursome!"
    "Wolf-whistles sound out from the crowd at this."
    "Along with genuine cries of amazement and support."
    kleio.say "Thanks for being so into our private lives, you perverts!"
    kleio.say "But yeah, [hero.name] popped the question, and we all said yes."
    show kleio date happy
    kleio.say "And because Deathless Harpy fans are like family, you're all invited to the wedding!"
    hide kleio
    hide anna
    hide sasha
    with moveoutright
    "I turn my head away from the cheering audience, nodding to a roadie standing just off-stage."
    "The guy in question, a gaunt, grizzled old veteran called Nick, returns the gesture."
    "He trundles out, not looking at all like a minister of any denomination."
    "But I knew that he had one of those certificates you an apply for online for just that purpose."
    "And so I suggested him as the perfect choice for someone who would be prepared to marry us onstage."
    show victor at center, blacker with moveinright
    "Nick" "Alright, alright - settle down, you slags."
    "Nick" "This is supposed to be a happy occasion, not a fucking riot!"
    "Nick gestures for us all to gather in the middle of the stage, and we hurry to so as we're told."
    show victor at top_mostleft, blacker
    show anna wedding b at left
    show kleio wedding a
    show sasha wedding at right
    with moveinright
    "Nick" "You know, this reminds me of the time I was on tour with Black Sabbath."
    "Nick" "I had to marry one of his wife's dogs to this pot-bellied pig a mate of mine had brought along."
    "Nick" "And unless it went to plan, Ozzy would not go on stage."
    "Nick" "Well, as you can imagine, turned into a proper circus, that did..."
    "I raise my fist to my mouth and make as loud of a coughing sound as I can."
    "As soon as I know that I have his attention, I press Nick to get on with it."
    mike.say "Enough with the war-stories, Nick."
    mike.say "Would you mind getting your skates on, mate?!?"
    "Nick" "Hey, man, cool your jets, yeah?"
    "Nick" "We'll get there, we'll get there!"
    "Nick" "Alright, where was I..."
    "Nick" "Oh yeah, the wedding."
    "Nick" "And faster than usual too, so Mavis here doesn't get his knickers in a twist!"
    "Pointing to each of us in turn, Nick is as good as his word."
    "Now that he's had a verbal kick in the pants, he gets a serious move on."
    "Nick" "So, do you, Sasha, Anna, Kleio and [hero.name]..."
    "Nick" "Take Sasha, Anna, Kleio and [hero.name] to be your lawful, wedded whatever?"
    "Nick" "Forsaking all others, until you get the hump with each other, yeah?"
    show sasha happy
    sasha.say "Count me in."
    show sasha normal
    show anna happy
    anna.say "Yeah, me too!"
    show kleio happy
    kleio.say "What they said."
    mike.say "I do!"
    "Nick smiles broadly at his, clearly amused no end at the complexities of our relationship."
    "He nods before continuing on with the ceremony."
    "Nick" "At this point in the proceedings, it's traditional to ask if anyone's got any objections."
    "Nick" "But under these rather unique circumstances, I think they can go bollocks, yeah?"
    "Nick" "So I have the great pleasure of pronouncing you married."
    "Nick" "All bleedin' four of you!"
    "Nick" "I suppose you can kiss each other, or whatever you do."
    "Nick" "Not that it's any of my business..."
    show anna b blush zorder 2 at center, zoomAt(1.5, (340, 1040))
    show kleio b seductive blush zorder 1 at center, zoomAt(1.5, (640, 1040))
    show sasha b blush zorder 3 at center, zoomAt(1.5, (940, 1040))
    hide victor
    with dissolve
    "Nick's rambling falls away into the background as the four of us come together in a group embrace."
    "I know all of this sounds like a teenage guy's wet dream."
    "But I'm so far beyond any of that stuff right now it's just unreal."
    "The genuine love that I feel, both for and from these guys, is like nothing I could have imagined."
    "I never knew that it could exist between the four of us, that it could be so perfect."
    mike.say "I love you guys."
    show anna happy
    show fx heart zorder 4 at left
    anna.say "Aww, we love you too, [hero.name]!"
    show kleio wedding punk
    kleio.say "Yeah, that and we OWN your ass now, Loverboy!"
    show kleio happy
    show sasha wedding flirt
    show fx exclamation zorder 4 at right
    sasha.say "DEATHLESS HARPIES FOREVER!"
    show sasha happy
    "By now I can hardly hear the sound of the audience in the background."
    "And I have no idea if we're going to do an encore or just walk straight off the stage tonight."
    "All I really care about is this moment in time and being with the women that I love."
    "Because who says we can't be a band as well as being lovers at the same time?"
    "Isn't that they very spirit of Rock n' Roll?"
    scene bg studio
    show anna at left
    show kleio
    show sasha at right
    with fade
    kleio.say "I just wanna say what a fucking rush it is to be getting this award."
    anna.say "Yeah, we didn't even know there was one for the most badass girls in all of metal!"
    kleio.say "But we kind of are, so it makes sense we won!"
    show sasha whining
    sasha.say "Anna, Kleio - what in the hell are you doing?!?"
    sasha.say "Stop screwing around before [hero.name] hears you and freaks out at us!"
    show sasha annoyed
    kleio.say "Ah, he's all talk, Sasha - let us have some fun."
    anna.say "He can be a bit of an old woman, Sasha, you know?"
    show kleio annoyed
    kleio.say "He's always like 'don't go on stage with no panties on, Kleio!'"
    show anna annoyed
    anna.say "Yeah, or 'stop flashing your tits at the fans, Anna!'"
    show sasha shout
    show fx drop at right
    sasha.say "Whatever, you guys."
    sasha.say "We're supposed to be wrapping this whole thing up, you know?"
    sasha.say "Telling how our story ends and how we're all happy now."
    show sasha normal
    show anna normal
    anna.say "Huh...telling who, Sasha?"
    anna.say "There's only the three of us here!"
    show kleio normal
    kleio.say "I dunno about that, Anna."
    kleio.say "Don't you get that weird, creepy feeling that we're always being watched?"
    show anna surprised at left, vshake
    show fx exclamation at left
    anna.say "WHAT?!?"
    anna.say "You mean there was someone watching that time I let [hero.name]..."
    anna.say "Let him put you know what, you know where?!?"
    show sasha annoyed
    sasha.say "Urgh..."
    show sasha whining
    sasha.say "I guess I'm going to have to do this on my own."
    show sasha shout
    sasha.say "But it's not a simple case of us just settling down."
    sasha.say "You know, living happily ever after?"
    scene bg black with timelaps
    scene bus_tour with timelaps
    kleio.say "Fuck no - we're sitting in the back of a tour bus right now."
    anna.say "And we're on a world tour right now too - supporting METALLIKEA!"
    sasha.say "Pardon my bandmates and what passes for their sense of humour."
    sasha.say "But they're not totally full of shit, as we ARE on tour."
    anna.say "We're well into our first headlining tour as a band, playing big cities!"
    kleio.say "Sure, it's small clubs and we're working hard."
    kleio.say "But the graft is starting to pay off."
    sasha.say "And the most important thing is that we're all together on the road."
    sasha.say "We took off pretty much straight after we got married, and we haven't stopped to catch our breath since."
    kleio.say "We're living the rock n' roll lifestyle for real now!"
    sasha.say "Things will have to change once we're back from the tour though."
    if anna.is_visibly_pregnant and kleio.is_visibly_pregnant and sasha.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        kleio.say "Loverboy damn well better be there when we get back from this tour!"
        kleio.say "He's the one that got all of us knocked-up in the first place!"
        anna.say "Yeah - Tommy, Dahlia and Courtney all need their Daddy around!"
        sasha.say "Oh, don't you girls worry about that."
        sasha.say "[hero.name]'s outnumbered now - six-to-one!"
    elif anna.is_visibly_pregnant and sasha.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        kleio.say "Whoa, hold on there, sister!"
        kleio.say "I don't know if I wanna move in with a couple of pregnoids!"
        anna.say "KLEIO!"
        sasha.say "Don't listen to her, Anna, she's just putting it on."
        sasha.say "Dahlia and Tommy love Auntie Kleio, and she loves them too!"
    elif kleio.is_visibly_pregnant and sasha.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        anna.say "Ooh, I want to move in with you guys - and Kleio too!"
        anna.say "Dahlia and Courtney need to have their Auntie Anna on call!"
        kleio.say "Geez..."
        kleio.say "I don't know if I do!"
        sasha.say "Trust me, Kleio - it's easier to just nod and smile..."
    elif anna.is_visibly_pregnant and kleio.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        kleio.say "You damn well better be moving in with us - you and [hero.name]!"
        anna.say "Yeah - Tommy and Courtney are going to need their Daddy around."
        anna.say "And their auntie Sasha too!"
        sasha.say "Geez, don't I even get a say in the matter!"
    elif sasha.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        kleio.say "Bags not having to be there for nappy changing duty!"
        anna.say "Aw, I'll help, Sasha - little Dahlia's SO CUTE!"
    elif anna.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        kleio.say "Bags not having to be there for nappy changing duty!"
        anna.say "KLEIO!"
        sasha.say "Don't listen to her, Anna - I'll be there to help out with Tommy."
    elif kleio.is_visibly_pregnant:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        anna.say "Eww, it's bad enough being on a bus with all those stinky diapers!"
        kleio.say "ANNA - I thought we were supposed to be married!"
        sasha.say "Don't worry, Kleio - I'll be there to help out with Courtney."
    else:
        sasha.say "[hero.name] and I are still technically living with [bree.name]."
        sasha.say "And I don't know if we need to all move in together for this relationship to work."
        anna.say "If [bree.name] moves out, I call first dibs on her room!"
        sasha.say "Anna!"
        anna.say "What?!?"
        anna.say "It's a nice room, I've seen it!"
        kleio.say "And if we live together, we can turn it into a party house too!"
        sasha.say "Oh, grow up, you two!"
    sasha.say "I guess a whole lot depends on whether or not the band takes off."
    sasha.say "That way we could afford to quit our jobs and become full-time musicians."
    kleio.say "That and hire a team of goddamn nannies!"
    anna.say "Ooh, can we get ones that'll breast-feed for us?"
    kleio.say "What...why?"
    anna.say "Well...my nipples are SO sore right now!"
    sasha.say "ANNA!"
    anna.say "But they are!"
    sasha.say "Anyway, where was I..."
    kleio.say "You were saying how great it is being with Loverboy."
    kleio.say "And his manhood!"
    sasha.say "Yeah, there is that too!"
    sasha.say "I guess there's no handbook out there that can tell you how to live with three other people."
    sasha.say "Let alone one that can handle being in a band and setting up home at the same time."
    sasha.say "So we're taking it slowly, one day at a time."
    sasha.say "And we always remember that there's one thing we have above everything else."
    sasha.say "Which is each other..."
    anna.say "Aww, that's so sweet, Sasha - I think I'm gonna cry!"
    kleio.say "Eww..."
    kleio.say "Puke more like - pass the bucket!"
    sasha.say "Hey you two - that was supposed to the last line!"
    sasha.say "You're supposed to say something affirmative like that, then let it fade out."
    sasha.say "It's thoughtful and poignant - and you bitches just ruined it!"
    kleio.say "Dig your panties out of your pussy, Sasha!"
    anna.say "Sorry, Sasha - we love you!"
    sasha.say "Okay, okay..."
    sasha.say "I love you guys too."
    sasha.say "Fuck knows why, but I do..."
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label anna_kleio_anal:
    show bg pub
    "As wrong as it might seem to eavesdrop on a private conversation, sometimes it's a pretty hard thing to avoid."
    "And it's made even worse when you realize in those first few moments of accidentally overhearing that it's a pretty juicy subject."
    "But what if, on top of all that, it then dawns on you that you're actually involved in the subject too?"
    "Surely, under those specific circumstances, even if you're not involved in the conversation, you really should be, right?"
    "Well that's my excuse anyway."
    show kleio annoyed at left5
    show anna at right5
    with dissolve
    kleio.say "Geez, Anna, what is it with you and taking it up the goddamn ass?!?"
    anna.say "Aw, come on, Kleio - you say that like it's weird, or freaky or something!"
    "This is what I hear as I walk back to our table in the local pub, what instantly makes my ears prick up."
    "Can you seriously blame me for hanging back and straining to hear what's being said after that?"
    kleio.say "Well...yeah, Anna."
    kleio.say "I guess I kind of am saying that."
    "I can see from the scowl on Kleio's face that she's not happy at being made to sound more conservative than Anna."
    "She crosses her arms over her chest, clearly uncomfortable with the subject being discussed."
    anna.say "Seriously, Kleio - you have to have done it up the ass before?"
    anna.say "You like guys and girls, right?"
    show anna wink
    anna.say "So you must have done some crazy stuff in bed...or some place else?"
    "The lascivious wink that Anna uses to underline her point is not lost on Kleio."
    show kleio blush
    kleio.say "Sure, I'm not a freakin' nun, Anna!"
    kleio.say "I just..."
    show anna evil
    anna.say "Are you scared it'll hurt, Kleio?"
    anna.say "Well, it kinda does at first."
    anna.say "But you get used to it real quick."
    "At this, she leans in close to Kleio in a conspiratorial manner."
    show anna blush
    anna.say "And, sometimes the pain's the BEST bit too!"
    "Kleio leans back, shaking her head as she casts her gaze around the pub."
    "I realize that she's probably looking for me returning to the table as an excuse to drop the subject."
    "So I make a point of quickly ducking out of sight somewhere I can still easily listen in on the conversation."
    show kleio normal
    kleio.say "I...I don't know, Anna."
    kleio.say "Maybe I could try it - ONCE...and that's all."
    kleio.say "But it'd have to be with someone that I trust."
    show kleio annoyed
    kleio.say "And I still say that I won't like it!"
    show anna happy
    "Anna practically beams at this, seeming to take it as proof positive that Kleio's about to embark on a veritable anal odyssey."
    anna.say "Oh, don't you worry about that."
    anna.say "I know just the guy for the job."
    anna.say "He can break my back doors in any time!"
    show kleio normal
    "It doesn't take me long to figure out that Anna must be talking about me!"
    "I gulp nervously, feeling like the heat in the place has suddenly gone through the roof."
    "It's all that I can do to walk back to the table and pretend like I haven't heard a thing."
    "When all the time my mind is racing at the thought of what Anna's got in mind for Kleio and myself..."
    hide anna
    hide kleio
    return

label kleio_anna_showdown:
    scene expression f"bg {game.room}"
    "I hear footsteps coming towards me..."
    show kleio at left5
    show anna at right5
    "A quick glance over my shoulder reveals Kleio and Anna, both making a beeline for me."
    "Kleio has her usual nonchalant look about her, but by now I can read the sarky look of confidence on her face, and know that she's after something intimate from me."
    "Anna, as usual, is the complete opposite, almost bouncing towards me like an enthusiastic puppy, clearly buzzing and wanting to share that energy with me as soon as possible."
    "I smile at them both, while internally grimacing."
    "This could be awkward, as I'm sure neither knows that I've also been screwing the other at every available opportunity."
    anna.say "Hey, You're great at practice these days."
    show anna wink
    anna.say "Almost like a guitar wizard...you know - the kind that has a magic wand!"
    "She winks in a way that's as close to lascivious as Anna gets, coming off more as cute and needy, making reference to the pillow talk we made during our last sexual encounter."
    show kleio annoyed
    kleio.say "God, Anna - why don't you just paw at his crotch like a Chihuahua in heat!"
    show kleio seductive
    kleio.say "Didn't anyone ever tell you that some guys prefer a feisty alley-cat to a little lap-dog?"
    "She cocks her head and smiles wickedly, knowing that I can't help but know she's referring to the time we fucked in an alleyway after a night out drinking together."
    show anna normal
    anna.say "Huh, well - he didn't mention anything like that when he gave me..."
    mike.say "Whoa, slow down there, Anna!"
    show kleio normal
    kleio.say "He certainly wasn't complaining when I let him..."
    mike.say "Hang on a second, Kleio!"
    "It's a little like watching one of those videos online, where someone's smashed something and then played the footage back in slow motion."
    show kleio surprised
    show anna surprised
    "Confusion spreads across both of the girl's faces, followed soon afterwards by realisation, and then the inevitable horror and outrage."
    show kleio angry
    show anna angry
    "As one, they round on me, arms crossed and faces filled with indignation."
    mike.say "Girls, I can explain..."
    if "kleio_say_preg" in DONE:
        kleio.say "For fuck's sake you even knocked me up!"
        "I can read some kind of distress in Anna's eyes."
    else:
        anna.say "Can you?"
        kleio.say "This should be fucking good!"
    "They look at me expectantly, but I can only shrug and sigh."
    mike.say "No...I guess I can't explain it."
    mike.say "I'm sorry...I guess I just found myself having fun with two mind-blowing girls at once, and I couldn't help myself."
    "Both of the girls still look visibly upset and angry, but my honesty has at least softened them a bit."
    "I go to speak, but Kleio cuts me off."
    kleio.say "You shut the hell up!"
    kleio.say "You said your piece, and this is all down to you thinking with your dick, so thanks for that!"
    kleio.say "As usual, the solution's gonna be down to someone with a vagina."
    "Anna doesn't add to Kleio's verbiage, but she nods in solemn silence to show her agreement."
    "So I keep my peace, waiting for the girls to decide my ultimate fate."
    "Kleio and Anna put their heads together, speaking loud enough for me to hear, but with their backs turned to remind me I'm not the one making the decisions on this matter."
    show kleio normal
    show anna normal
    if (kleio.love < 150 or kleio.lesbian < 9) and not (anna.love < 150 or anna.lesbian < 9):
        kleio.say "You know me, Anna - I'm a pretty open-minded kind of girl."
        kleio.say "But I've been hurt too many times and too hard in the past to let this prick do it to me all over again."
        show anna cry
        anna.say "I'm sorry, Kleio - but I really like him."
        "Snorts and rolls her eyes in frustration at Anna's words."
        anna.say "You know, Kleio, you talk about how sex is just two people coming together."
        anna.say "So how come you crap on me for still wanting [hero.name]?"
        show kleio sad
        kleio.say "Anna, that's not the same thing, I..."
        anna.say "Why is it different when it's me?"
        anna.say "So what if he's had sex with you too?"
        anna.say "We've all had sex with lots of people...and I like doing it with him."
        show anna happy
        kleio.say "Okay, Anna - if that's the way you feel, you can keep him, with my blessing!"
        $ kleio.set_gone_forever()
    elif not (kleio.love < 150 or kleio.lesbian < 9) and (anna.love < 150 or anna.lesbian < 9):
        show anna cry
        anna.say "I can't share a guy with someone else, Kleio."
        anna.say "Maybe if it was a girl, it'd be different...but I haven't been with a guy for so long...and it felt special."
        kleio.say "I hear that, Anna...thing is...I really like this prick...don't ask me why!"
        show anna blush
        "Anna blushes, clearly recalling the time we spent together in bed."
        show anna normal
        anna.say "What's up, Kleio - are you too much of a tough bitch to admit that you like to feel his cock inside of you?"
        "Both Kleio and I are shocked to hear Anna talk like that in public, but I manage to keep quiet...unlike Kleio."
        show kleio annoyed
        kleio.say "Jesus, Anna - you're not taking any prisoners tonight, are you?"
        anna.say "I'm just being honest, Kleio...can't you be honest for once, too?"
        show kleio annoyed blush
        kleio.say "Alright, alright...fuck sake, I admit it - I like this prick...and this prick's prick."
        show anna happy
        "Anna smiles, clearly taking some consolation from having extracted such a confession from Kleio."
        $ anna.set_gone_forever()
    elif (kleio.love < 150 or kleio.lesbian < 9) and (anna.love < 150 or anna.lesbian < 9):
        show kleio sad
        show anna cry
        kleio.say "I had no idea he was fucking you too, Anna."
        anna.say "Same here...sorry."
        kleio.say "Hey, don't beat yourself up - that jerk was the only one of the three of us that knew!"
        kleio.say "I know I get on my high-horse about sex sometimes, but that doesn't feel right when it's a friend like you."
        anna.say "Yeah, I feel pretty much the same...maybe if it was some other girl neither of us knew, it'd be different."
        show anna normal
        show kleio normal
        "Get the distinct feeling that, whatever fun the girls had with me, they're closing ranks as their friendship wins out."
        kleio.say "We're still friends, right?"
        anna.say "Yeah, I guess so...what's a prick between friends?"
        kleio.say "Exactly - fucking nothing!"
        show anna happy
        show kleio happy
        "The girls exchange a pinkie shake and ignore me with deliberate pleasure in doing so."
        $ kleio.set_gone_forever()
        $ anna.set_gone_forever()
    else:
        kleio.say "You know what, Anna - your playing's gotten much better since that prick came along with his prick!"
        anna.say "Speak for yourself, Kleio - your guitar's not the only thing that's been better tuned thanks to [hero.name] as well!"
        "Suddenly they're both looking at me, and I know how a wounded gazelle under the gaze of two lionesses must feel."
        show kleio seductive
        kleio.say "This is the twenty-first century, Anna...and we're pretty good friends, aren't we?"
        show anna blush
        anna.say "Yeah, Kleio, we are...and good friends share things, right?"
        show kleio seductive blush
        kleio.say "Sure they do...things like make-up, clothes, vibrators...and a decent dick, when one finally shows up."
        show anna happy
        anna.say "Oh, believe me...I know how long that takes to happen!"
        "Anna's giggling uncontrollably now, enjoying my discomfort."
        "Kleio looks equally amused, but something in her eyes tells me she's already imagining the possibilities that might lie ahead."
        show kleio happy
        show anna happy
        kleio.say "Like I always say, Anna - sex is just an encounter between two people...or three."
        anna.say "Well, if he's going to screw other girls, then I'd rather it be you...and me!"
        "I can't help gulping in trepidation and more than a little excitement at the prospect."
        "It seems like, without a care for my own feelings, the girls have decided that they're going to keep me!"
        $ Harem.join_by_name("band", "kleio", "anna")
    "No one addresses the metaphorical elephant in the room..."
    "But I can see knowing glances passing between Kleio and Anna, an unspoken code that I'm not to be let in on."
    "For my own part, I can't honestly decide if what's happened is for good or bad."
    "But I'm sure it'll have serious consequences for me before too much time has passed."
    hide kleio
    hide anna
    return

label date_set_up:
    "During our training session, Kleio and Anna come talk to me."
    show kleio at left
    show anna at right
    kleio.say "You're taking us to dinner."
    mike.say "Wow...okay!"
    call select_date_time from _call_select_date_time_6
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call kleio_and_anna from _call_kleio_and_anna
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna"], label="kleio_and_anna", name="Meet Anna and Kleio", fail_label="kleio_and_anna_missed"))
        anna.say "This is gonna be so fun!"
    return

label kleio_and_anna_missed(from_cancel=False):
    if not from_cancel:
        "Shit I missed my date with Kleio and Anna."
        $ kleio.love -= 10
        $ anna.love -= 10
    $ DONE.pop("date_set_up", None)
    return

label kleio_and_anna(appointment=None):
    $ game.flags.sashathreesomedelay = TemporaryFlag(True, 7)
    scene bg street with fade
    $ s = 0
    "A big part of me still can't quite believe where I am right now with Kleio and Anna."
    "After figuring out that I was seeing each one behind the other's back, they've decided that they're going to share me."
    "On the one hand, I'm giddy at the prospect of being involved in what you might call a 'three-way dance'."
    "But I'm also in uncharted territory here, and it's actually quite terrifying."
    "We all decide that we should start slowly, with dinner at a new and pretty hip Chinese restaurant in the centre of town."
    "I find myself waiting on the sidewalk, checking the time while I wait for the girls to arrive."
    anna.say "Hi!"
    kleio.say "Hey, guy!"
    show anna date at right5
    show kleio date at left5
    with moveinright
    "That they've arrived together should make me instantly paranoid, but instead I'm too busy admiring the sight of them both."
    "Anna's wearing a colourful skirt that make her look like an achingly hot little pixie and a top that shows off her impressive chest."
    "Kleio, on the other hand, is wearing a short tartan skirt, fishnets and a cropped top under her leather jacket, and looks like the perfect punk princess."
    mike.say "Hi girls...you look amazing tonight."
    if hero.equipment["clothes"] and hero.equipment["clothes"].name in ["fancy_clothes"]:
        "Anna and Kleio take in that I'm wearing a dress shirt, pants and shoes."
        show kleio annoyed
        kleio.say "Well, aren't we mister fancy pants tonight!"
        show anna happy
        anna.say "Aww, don't be mean, Kleio...[hero.name] went all out for us - it's totally sweet."
        kleio.say "Whatever you say - but if someone thinks you're our pimp, I'm totally playing up to it for the laughs."
        $ kleio.love -= 2
        $ anna.love += 2
    elif hero.equipment["clothes"] and hero.equipment["clothes"].name in ["military_fatigues",]:
        "Anna and Kleio take in that I'm wearing a polo shirt and khaki pants."
        show kleio happy
        kleio.say "Come here straight from the cube farm, did you?"
        show anna annoyed
        anna.say "I forgot what Sasha told me you did in the day time, but I think it involved IT, right?"
        kleio.say "Don't worry - maybe the restaurant will need their Wi-Fi fixed, and you'll be the hero of the day!"
        $ kleio.love += 2
        $ anna.love -= 2
    elif hero.equipment["clothes"] and hero.equipment["clothes"].name in ["leather_jacket"]:
        "Anna and Kleio take in that I'm wearing a leather jacket, band t-shirt and ripped jeans."
        show anna happy
        anna.say "Ooh...I LOVE that band!"
        show kleio happy
        kleio.say "One of us, one of us, one of us!"
        "I can't help grinning, realising that my choice of attire makes us look like a trio set against the rest of the normal, mainstream world."
        $ kleio.love += 5
        $ anna.love += 5
        $ s += 2
    else:
        show kleio annoyed
        kleio.say "Whoa, [hero.name] - way to push the boat out and make a girl feel special!"
        show anna b annoyed
        anna.say "Don't listen to her, [hero.name]...we're already band-mates, friends and...well, a bit more than that too."
        anna.say "It's not like you're making a first impression or anything."
        $ kleio.love -= 5
        $ anna.love -= 5
        $ s -= 1
    scene bg restaurant
    show anna b date at right5
    show kleio date at left5
    with fade
    "We walk inside and the waiter on the door checks our reservation and shows us to our table in a plush booth."
    "The waiter is a young and pretty handsome Asian guy, and I can feel him checking Anna and Kleio out in silence."
    show anna b date at center, zoomAt(1.5, (840, 1140))
    show kleio date at center, zoomAt(1.5, (440, 1140))
    with ease
    "His obvious admiration makes me feel all the more flushed at my sheer luck to be out with both these girls at once."
    "Supplied with menus, the waiter asks me to order drinks for the table."
    menu:
        "Order fruity cocktails":
            mike.say "Three Raspberry Cosmopolitans, please."
            show anna b happy
            anna.say "Ooh, that sounds delicious...and strong."
            show kleio annoyed
            kleio.say "Yeah, but I'm sure they're not the only fruity thing around here!"
            $ anna.love += 5
            $ s += 1
        "Order beers":
            mike.say "Three beers, please."
            show kleio happy
            kleio.say "Hell yeah, and keep 'em coming too!"
            show anna b annoyed
            anna.say "Aww, those cocktails looked all nice and colourful."
            $ kleio.love += 5
            $ s += 1
        "Order spirits":
            mike.say "Three vodkas, with ice."
            show anna b happy
            anna.say "Ooh, I can't remember the last time I had vodka...mainly 'cos of the amount of vodka I had then."
            show kleio happy
            kleio.say "Geez, - you don't mess about...and I like that in a man!"
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Order tap water":
            mike.say "Jug of tap water and three glasses, please."
            show kleio annoyed
            kleio.say "Wow, check out mister big spender here!"
            show anna b annoyed
            anna.say "Well, it's only the start of the night...maybe [hero.name] likes to start off slow and hit his stride later on?"
            $ kleio.love -= 5
            $ anna.love -= 5
            $ s -= 1
    show anna b normal
    show kleio normal
    "The waiter returns with our drinks, and it's time to order the food."
    "The menu's so large and complex that I'm baffled, and so to save face, I suggest that we just order one of the set banquets for three."
    anna.say "Great idea, [hero.name] - that way we can try a little of everything."
    kleio.say "Sounds good to me...too much of one thing's bound to get boring sooner rather than later."
    "The food soon arrives, and I'm surprised by the sheer number of dishes covering the table, unsure of where to start."
    "I can't help but see the parallel between the meal and my new relationship with Anna and Kleio."
    menu:
        "Reach for a knife and fork":
            "I begin to eat with a knife and fork, as I've never gotten the hang of chopsticks."
            kleio.say "Jeez, [hero.name] - when in Rome, and all that crap!"
            show kleio happy
            "Kleio laughs, letting me know that she's fucking with me for the fun of it."
            "Anna coughs nervously and leans in closer before speaking."
            anna.say "Don't feel bad...I could never use them either!"
            $ kleio.love += 2
            $ anna.love -= 2
        "Reach for chopsticks":
            "I snatch up some chopsticks and get stuck into the food."
            kleio.say "Whoa...look at the sophisticated eater we're out with tonight!"
            show kleio happy
            "Kleio's laugh and the twinkle in her eye tells me that she's just fucking with me for fun."
            show anna happy
            anna.say "[hero.name], you're a natural!"
            show anna blush
            anna.say "Can you show me how to do it...or maybe you could feed me a few morsels?"
            $ kleio.love -= 2
            $ anna.love += 2
    show anna normal
    show kleio normal
    "As time goes on, the date seems to be going pretty well."
    "I'm really enjoying the banter between Anna and Kleio as they loosen up and let go a little."
    "If this is what a real threesome is like, then it feels just the same as going out with good friends...only with the prospect of group sex at the end of it all."
    "Suddenly I feel the sensation of something touching my left thigh."
    show anna wink
    "Glancing to my left, I see Anna, flushed from the food and drink, smiling invitingly as she squeezes my left leg with her free hand."
    "A second later, I feel a similar sensation on my right thigh."
    show kleio seductive blush
    "My head spins around to see Kleio, licking her lips suggestively, as she pinches at my right leg, as close to the groin as she can manage."
    menu:
        "Try to calm both girls down":
            "I feel hot and not a little panicked at the prospect of being stroked by both girls in a public place."
            mike.say "Wow...I don't know about you two, but I feel like my pants are fit to burst right off of me!"
            "I overemphasize my words, trying to glance down at my groin to get the true meaning of my words across."
            "Kleio raises a quizzical eyebrow, seeming to catch my meaning."
            show anna annoyed
            "But Anna looks dejected, clearly thinking that she's being rebuffed."
            anna.say "Aww...I was still kinda hungry."
            show kleio normal
            kleio.say "Anna, you ditz - he's saying you can take it home...in a DOGGY BAG!"
            show anna happy
            "Anna takes a moment to understand, and then blushes, laughing a little too loudly in aroused amusement."
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Return Anna's attentions":
            "Maybe it's the alcohol, or the nerves doing the thinking for me...but I suddenly want to see Anna even more aroused and turned on in a public place."
            "I turn to face her, slipping my hand up the inside of her thigh at the same time."
            "The feel of the tights she's wearing and the heat of her thigh is only made all the more amazing by the look on her face as she begins to melt."
            "I reach the top of her thigh, and just stroke the beginnings of her crotch as lightly as I can."
            show anna blush
            "Anna's cheeks are visibly red and she's almost panting now, making me feel she could be made to beg like a dog, right there in the restaurant."
            show kleio annoyed
            "I glance across at Kleio, and see that she's wearing a slight frown at being ignored."
            "But I also notice that her free hand is hovering somewhere around her own groin, suggesting that being neglected is making her long for the balance to be redressed."
            $ kleio.love -= 5
            $ anna.love += 5
        "Return Kleio's attentions":
            "I feel like Kleio's rebellious spirit is infecting me too, making me forget the consequences as I instinctively return her advances."
            "I turn my head to look her in the eye, my right hand roughly grabbing at the hem of her short skirt and climbing upwards like a giant spider."
            "But it's me that gets a surprise, as the tips of my fingers discover that she's already warm and slick to the touch."
            "And that she's not actually wearing any panties tonight."
            show kleio punk
            "I can't keep the shock off of my face, and Kleio's wicked look in return makes me want her more than ever."
            "At last I manage to tear my gaze off of Kleio and look at Anna, more from the need to calm myself down than genuine concern for the other girl present."
            show anna annoyed
            "Anna looks downcast at the attention that I'm giving to Kleio, but somehow the sulkiness in her expression only makes her look all the more desirable."
            $ kleio.love += 5
            $ anna.love -= 5
        "Return both girls' attentions" if hero.charm >= 50:
            "I'm torn as I look from one of the girls to the other, wanting to sample the sweetness of Anna and the tart allure of Kleio all at once."
            "Thinking I must be mad, I put a hand on the closest thigh of each girl, then begin to squeeze and slide my way upwards."
            "The contrast of Anna's pantyhose and Kleio's fishnets feels incredible against the warmth of their thighs."
            show anna blush
            show kleio blush
            "I steal glances at both their faces, seeing that they're gazing at one another, visibly turned on at the feeling of being played with by the same man."
            "A moment later, I have both their skirts hitched up just enough to stroke them between the legs."
            "Anna feels incredible through her tights and panties, but I realise with some genuine shock that Kleio has outdone her by not wearing any at all."
            $ kleio.love += 5
            $ anna.love += 5
            $ s += 2
    "An unsubtle cough breaks the spell, and I look up to see the waiter standing by our table."
    "All three of us snap out of it and try to make it look like we're just more than a little drunk and sleepy, rather than worked into a lather and heading for a threesome later on."
    "I have no idea if the waiter realised what was going on, or how our relationship is supposed to work."
    mike.say "Erm...could we get the cheque, please?"
    menu:
        "Offer to pick up the bill" if hero.money >= 150:
            "When the bill arrives, I decide to make a gesture and pay for the meal."
            mike.say "Don't worry, guys - it's on me."
            show anna happy
            anna.say "Aww, thanks, [hero.name]...what a gentleman."
            show kleio happy
            kleio.say "Whoopie doo...my knight in shining armour!"
            $ kleio.love += 2
            $ anna.love += 2
            $ s += 1
        "Claim to have no money":
            "When the bill arrives, I realise that I've forgotten my wallet."
            mike.say "Ah, shit...I must've left my wallet at home!"
            show anna annoyed
            anna.say "Oh no, [hero.name]...we'll get this one, and you make it up next time."
            show kleio angry
            kleio.say "Fuck me, [hero.name] - you must have a mind like a goddamn Swiss cheese!"
            $ kleio.love -= 2
            $ anna.love -= 2
            $ s -= 1
        "Suggest they split the bill" if hero.money >= 50:
            "When the bill arrives, I remember that we're all supposed to be equals in this relationship, even when it comes to paying for stuff."
            mike.say "Let's go Dutch."
            show anna normal
            anna.say "Sounds fair to me."
            show kleio normal
            kleio.say "Fine...I don't need to be coddled by anyone."
    if s >= 3:
        "With the bill settled, we call a cab and head back to my house, hoping to pick up where we so recently left off."
        call kleio_anna_threesome from _call_kleio_anna_threesome
        $ DONE["kleio_and_anna"] = game.days_played
    else:
        scene bg street with fade
        show anna date at right5
        show kleio date at left5
        "With the bill settled, we're back on the street."
        anna.say "Thanks [hero.name] it was a nice evening."
        kleio.say "Yeah we should do that again soon"
        $ game.flags.anna_kleio_date_delay = TemporaryFlag(True, 2)
        $ DONE.pop("date_set_up", None)
        $ game.pass_time(2)
    return

label kleio_anna_threesome(appointment=None):
    if "kleio_anna_threesome" not in DONE:
        $ game.hour = 23
        $ DONE["kleio_anna_threesome"] = game.days_played
        scene bg house with fade
        "The taxi drops the three of us off outside my house, and I try to look confident as I let the girls inside."
        "But the truth is that I'm already sweating at the realisation that I didn't check beforehand that nobody else would be in tonight."
        scene bg livingroom
        show anna a date zorder 2 at right4
        show kleio date zorder 1 at center
        with fade
        "We enter the living room, Anna and Kleio already giggling and making suggestive comments as they pinch and tickle me in what should be an agreeable manner."
        show anna a date zorder 2 at center
        show kleio date zorder 1 at left4
        with ease
        "I put my finger to my lips, in the vain hope of keeping them quiet for a moment."
        mike.say "Hello...anyone home?"
        $ rooms = ["secondfloor", "kitchen", "pool", "bedroom1", "bedroom2", "bedroom3", "bathroom"]
        if not bree.room in rooms and not sasha.room in rooms:
            "All I get in answer is silence, allowing me to let out a sigh of relief."
            show anna evil
            anna.say "What's up [hero.name], did you think someone was home?"
            show kleio seductive
            kleio.say "Doesn't matter either way - I'm gonna make you guys come so hard they'll hear it all the way down the block!"
        elif not sasha.room in rooms:
            show bree sleep at top_mostright with moveinright
            "Much to my horror, [bree.name]'s head appears around the living room door."
            hide kleio
            hide anna
            bree.say "Hi [hero.name], have you - oh, hello to your friends as well!"
            mike.say "We're...erm...going to my room, just so you know...in case you hear anything weird."
            show bree evil
            "[bree.name] can't help sniggering as she closes the door, knowing full well what's going on between the three of us."
            hide bree with moveoutright
        elif not bree.room in rooms:
            show sasha sleep happy at top_mostright with moveinright
            "I'm left gaping as Sasha opens her bedroom door and smiles at me."
            sasha.say "Oh, hey, [hero.name] - been out at the..."
            show sasha sleep normal
            "She pauses as she sees her band-mates in a state of disheveled amusement behind me."
            sasha.say "Is this a band thing...or a side-project you three are working on behind my back?"
            show kleio happy
            show anna happy
            "Anna and Kleio both burst into filthy laughter, making me think I'm the only one nervous about doing this."
            sasha.say "Don't look so paranoid, [hero.name] - they already warned me about it!"
            hide kleio
            hide anna
            with moveoutleft
            "Before I can protest, Anna and Kleio barge me into my room."
            hide sasha
        else:
            show sasha sleep zorder 2 at top_mostright
            show bree sleep zorder 1 at right
            with moveinright
            "[bree.name]'s head appears around the living room door, and then Sasha's from behind the door to her bedroom."
            "My mouth starts moving, but there's nothing coming out as I realise both my housemates are seeing me come home with two other girls."
            bree.say "Hey, [hero.name] - are we having a party?"
            sasha.say "Or a band practice?"
            show kleio happy
            kleio.say "No and no again...but you might want to put some headphones on pretty soon!"
            hide sasha
            hide bree
            with moveoutright
            "Both [bree.name] and Sasha chuckle knowingly as they disappear back into other rooms."
            "I'm left wondering if I'm the only person in the world that's not so blase about the idea of a threesome."
        hide kleio
        hide anna
        with moveoutleft
        "The girls almost pull me off of my feet as they each take one of my hands and lead me into my bedroom."
        scene bg bedroom1
        show anna a date zorder 2 at center
        show kleio date zorder 1 at left4
        with fade
        "I try to collect myself and say something, but they give me a look that shuts me right up."
        "As Kleio pushes me down onto the bed and Anna starts to unzip my flies, I get the distinct feeling they've planned this beforehand."
        "Anna soon has my pants and underwear down around my ankles, stripping me completely below the waist with characteristic eagerness."
        "Kleio, on the other hand, takes her time removing my top, running her hands over me as she does so and even giving me the occasional kiss as she goes."
        anna.say "Oh wow, Kleio - come look at this!"
        kleio.say "Well hello there, little [hero.name]...I think he likes us, Anna!"
        "Anna's already kneeling on the floor in front of me, and now Kleio slides down to kneel beside her."
        "Both girls are looking up at me now, fingers reaching out to tap my rapidly stiffening cock."
        "Their touches send it wobbling like a fleshy Jack-in-the-Box, much to their amusement."
        kleio.say "Wait a minute, Anna - we're all equals here, so let's get on an even footing."
        anna.say "Huh?"
        show kleio naked
        "Without explaining herself to Anna, Kleio strips off her leather jacket and then pulls her cropped top off over her head."
        "As she unhooks her bra and frees her petite breasts, Anna giggles in realisation and follows her lead."
        show anna naked
        "Moments later, her much larger and heavier breasts are also bared before me, and both girls are naked to the waist."


















        "I was never too big on classical mythology, but I think I know how an ancient Greek guy might have felt when he was presented with the sirens right now."











        "I take a deep breath and reach out for one of the two girls before me."
    else:
        scene bg bedroom1
        show anna a date zorder 2 at right4
        show kleio date zorder 1 at center
        with fade
        "Once in my bedroom, the girls don't waste time on foreplay."
        "They push me on the bed while stripping."
    menu:
        "Fuck Kleio":













            "Good girls may go to heaven, but bad girls win for me every time, and I pull Kleio towards me while I lay on my back."
            "But she comes of her own volition, refusing to be pulled and instead crawling onto me like an alley cat in heat."
            "Kleio looks into my eyes, and her almost mocking come on makes me thrust in her a second later."
            hide kleio
            hide anna
            show band threesome anna suck kleio_pleasure finger vaginal
            with fade
            "Kleio almost purrs with satisfaction as I fill her up and mounts me like she was a bitch, her tightness making me go harder and stronger than I would normally dare."
            anna.say "Hey, guys...don't forget about me!"
            show band threesome blowjob kleio_happy -finger
            "If Kleio's a feral alley cat, then Anna's a mischievous kitty, she takes my cock out of Kleio and into her mouth."
            "Kleio begins to play with her petite breasts, whilst grinning wickedly at making Anna pleasure us both at once."
            "Anna begins to kiss the base of my shaft, gently at first and then with more intensity."
            "As she works her way upwards, she starts to caress and then fully lick at my length with her tongue."
            show band threesome kleio_pleasure vaginal finger
            "After a while she angles my cock toward, then inside Kleio's pussy."
            "Kleio starts to groan and buck from our combined efforts, and her movements mean that I can feel myself about to cum."
            menu:
                "Cum inside Kleio's pussy":
                    "We're sweating so much from the exertion and shared body heat that Kleio almost slips out from my grasp."
                    show band threesome cum kleio_orgasm with vpunch
                    "But I hold her in place, feeling the wave of my orgasm finally take hold."
                    "The sensation inside of Kleio pushes her over the edge too, and she cums a moment later."
                "Cum inside Anna's mouth":
                    "I grip the back of Anna's head with one hand as tremors start to rock through me, and I push deeper; she makes no protest though her eyes tear up a bit."
                    show band threesome kleio_happy deep cum -finger with vpunch
                    "Groaning, I gasp for breath as my cock twitches and throbs, forcing her to swallow quickly as pleasure sends spurts of hot cum straight down her throat."
                    "It takes several moments for my climax to pass, and when it does, I drop back to the bed, panting, trying to catch my breath."
                    "Dimly, I feel Anna licking at my cock lightly before she pulls away."




    hide band
    show anna a naked blush at center, zoomAt(1.5, (840, 1040))
    show kleio a naked happy blush at center, zoomAt(1.5, (440, 1040))
    with fade
    "As the three of us lay there, bathed in sweat and slippery from our collective efforts, I start to feel weirdly proud of what we've just done."
    "Everyone, even Kleio, has a satisfied smile on their face, and seems to be happy enough simply to keep quiet and enjoy the afterglow."
    "Slowly we end up laid together on the bed, curled up almost as close as we were whilst having sex a moment before."
    hide anna
    show anna a naked surprised at center, zoomAt(1.5, (840, 1040)), vshake
    "Suddenly, Anna jumps at the sound of someone snoring loudly."
    anna.say "Ooh - what's that noise!"
    mike.say "I think we tired Kleio out!"
    "Anna and I gaze over at the sight of Kleio, dead to the world and making a sound like a sawmill."
    show anna a happy
    anna.say "Aww, doesn't she look sweet when she's asleep?"
    "I just chuckle quietly, but I can't help admitting that she's right."
    $ kleio.sexperience += 1
    $ anna.sexperience += 1
    scene bg black with dissolve
    if renpy.has_label("band_harem_achievement_2") and not game.flags.cheat:
        call band_harem_achievement_2 from _call_band_harem_achievement_2
    $ game.room = "bedroom1"
    call sleep from _call_sleep_49
    return

label anna_concert_naked:
    show anna at center, zoomAt(1.25, (640, 880)) with fade
    "Keep trying to make sure that I have a neutral expression on my face."
    "All in the hope of not giving anything of my true intentions away."
    "But that's pretty hard when I'm so close to Anna."
    "Because I just can't help checking her out whenever I glance in her direction!"
    show anna surprised
    anna.say "[hero.name]…"
    anna.say "Are you doing what I think you're doing?"
    mike.say "Erm..."
    mike.say "That depends on what you think I'm doing, Anna!"
    show anna evil at startle
    "I hear Anna let out a sweet little giggle."
    show anna b at center, traveling(2.0, 0.3, (640, 1340))
    "And then she pops up, right in front of my eyes."
    anna.say "Well..."
    anna.say "I think you were checking me out!"
    "It'd be far easier to look her in the eye if she were less well-endowed in certain areas."
    "Like, right now her chest is thrust right up against me."
    "And whenever Anna moves, her breasts jiggle like a couple of space-hoppers!"
    mike.say "I..."
    mike.say "I might have been, Anna..."
    show anna happy
    anna.say "Oh, [hero.name]…"
    anna.say "That's totally okay with me!"
    show anna wink
    anna.say "I just wondered if you wanted to get a better view?"
    "Anna underlines her point by thrusting her chest towards me."
    "And I'm not kidding when I say it ends up an inch from my face."
    "I almost forget what I was trying to do in the first place."
    "But when I remember, I take a small step backwards."
    mike.say "Thanks, Anna..."
    mike.say "But maybe later, okay?"
    show anna worried at center, traveling(1.5, 1.0, (640, 1040))
    "Anna looks a little put out by my response."
    "So I decide to get straight to the point."
    "As that might help to distract her and change the subject."
    mike.say "I was just thinking..."
    show anna normal
    mike.say "When we're performing as a band..."
    mike.say "The audience gets to see how talented and artistic we all are."
    mike.say "You know, through hearing our music?"
    show anna annoyed
    "Anna seems more than a little puzzled by the sudden change of subject."
    "But I can see that she's doing all she can not to show her confusion."
    "Instead she tries as best she can to cover it up with interest in what I'm saying."
    show anna normal
    anna.say "Uh..."
    anna.say "Yeah..."
    anna.say "I know what you mean."
    mike.say "Well it's a shame they can't see that side of you too, Anna."
    mike.say "Because your body is just as impressive as your drumming."
    show anna blush
    "Anna's face shifts into an embarrassed smile."
    "Her cheeks flush red too."
    "And she looks around, like she's afraid someone heard me."
    show anna embarrassed
    anna.say "[hero.name], you're so naughty sometimes!"
    anna.say "I couldn't possibly do that - be naked on stage."
    show anna blush
    mike.say "Why not, Anna?"
    mike.say "I've seen lots of artists do it."
    mike.say "And if you're an artist, then it's not lewd or dirty."
    show anna surprised
    "Anna's frowning at me now."
    "Not able to conceal her confusion any longer."
    anna.say "It isn't?"
    mike.say "No, Anna..."
    mike.say "It's art, not filth!"
    mike.say "How do you think they get away with it in paintings and statues?"
    show anna annoyed
    "I can see Anna thinking about what I'm saying."
    "In fact I can almost hear the cogs whirring inside of her head."
    show anna happy
    anna.say "Oh yeah..."
    anna.say "I always wondered about that!"
    show anna normal
    "I let the ideas sink in for a few moments longer."
    "Giving Anna just enough time to get tied up in all those challenging new thoughts and possibilities."
    "Then I pop the question."
    "The one I've been building up to all this time."
    mike.say "So..."
    show anna surprised
    mike.say "Maybe the band should perform naked too?"
    if anna.love >= 200 and anna.sub >= 90:
        show anna blush
        "As soon as she hears the words, Anna starts to nod."
        "And I can see that her eyes are starting to widen at the notion."
        show anna evil
        anna.say "You're right, [hero.name]…"
        show anna happy
        anna.say "People always say the human body is beautiful."
        anna.say "Like it's nothing to be ashamed of, you know?"
        anna.say "So why shouldn't we show ours off?"
        show anna normal
        "I'm already nodding eagerly."
        "Doing all I can to encourage Anna."
        mike.say "Got it in one, Anna."
        mike.say "We should be setting an example."
        mike.say "Getting naked on principle!"
        show anna surprised
        "Anna looks at me in confusion."
        anna.say "Where?"
        anna.say "I thought we were doing it on the stage?"
        mike.say "Figure of speech, Anna..."
        mike.say "You remember that conversation we had on the subject?"
        show anna normal
        "Anna nods and smiles."
        "But I have my doubts that she does."
        show anna evil
        anna.say "Anyway..."
        show anna wink
        anna.say "I'm gonna call the girls up."
        anna.say "And I'm gonna tell them about this great idea of yours!"
        show anna normal
        mike.say "Ah..."
        mike.say "No, Anna..."
        mike.say "Better let me do that - because it's my idea, yeah?"
        "Anna shrugs at this."
        show anna evil
        anna.say "Whatever, [hero.name]…"
        anna.say "But I'm sure they'll all want to do it too."
        show anna wink
        anna.say "Especially when they hear it's all artistic and stuff!"
        $ anna.flags.agree_concert_naked = True
    else:
        show anna annoyed
        "As soon as she hears the words, Anna seems to snap out of it."
        "Before she was wide-eyed and taking in every word I said."
        "But now she's looking at me with a genuine fear in those same eyes."
        show anna worried
        anna.say "Oh no, [hero.name]…"
        anna.say "I couldn't do that!"
        anna.say "That kind of stuff only works for painters and statuers, like you said!"
        mike.say "Sculptors, Anna..."
        mike.say "People that make statues are called sculptors."
        "Anna's too worked-up to take offence at being corrected."
        "Which I guess is a small mercy."
        show anna angry
        anna.say "Whatever they're called, it's different."
        anna.say "I'm just a drummer in a rock band."
        anna.say "I can't go out there naked!"
        $ anna.love -= 5
        show anna unpleased
        "I think about arguing with Anna some more."
        "But I can tell from the look on her face there's no point."
        "She's already on the verge of working herself up into a state."
        "And once she does that, it'll be hours before she calms down again."
        "So I decide to let the matter drop for now."
        "Maybe I can refine my argument and try another time."
        "Anna might have forgotten all about the suggestion by then."
        "So it'll be like wiping the slate clean."
        $ anna.flags.agree_concert_naked = False
    scene bg black with dissolve
    return

label kleio_concert_naked:
    show kleio at center, zoomAt(1.25, (640, 880)) with fade
    "Any of the other girls and I'd have tried to beat about the bush with the idea that I have."
    "Laid out metaphorical breadcrumbs for them to follow before we got to the heart of the matter."
    "But with Kleio, none of that stuff would ever work, and she's sniff me out almost instantly."
    "So with her something different is required, something that on the surface seems far cruder."
    "Yet in reality has it's own levels of complex sophistication that are just below the surface."
    "The time-honoured art of reverse psychology..."
    show kleio at center, traveling(1.5, 1.0, (640, 1040))
    mike.say "Hey, Kleio..."
    mike.say "Did you ever..."
    show kleio seductive
    kleio.say "Did I ever what, Loverboy?"
    "As soon as Kleio responds to me, I pause and then shake my head."
    mike.say "Nah..."
    mike.say "Forget about it, Kleio."
    show kleio surprised
    mike.say "It was nothing."
    hide kleio with dissolve
    "Even before I manage to turn away from Kleio, she's already taken the bait."
    "Because I feel her hand on my shoulder, spinning me around to face her again."
    show kleio angry at center, zoomAt(1.5, (640, 1040)) with hpunch
    kleio.say "Oh no you fucking don't!"
    kleio.say "You know how that pushes my bloody buttons..."
    kleio.say "So tell me what you were going to say, before I shake it out of you!"
    show kleio upset
    "Still doing the best I can to keep up the act, I shrug my shoulders."
    "Then I let out what I hope is a convincing sight of surrender."
    mike.say "Okay, Kleio, okay..."
    mike.say "I just had this crazy idea about something the band could do."
    mike.say "Something that'd be so out there and crazy it'd really challenge our audience."
    mike.say "And I was going to pitch it to you, but then I thought, nah."
    mike.say "I should be telling it to Sasha instead, or maybe even Anna."
    "It's weird, because you shouldn't be able to see the heckles rise on a human being."
    "But I swear that I see Kleio bristle, just like a cat that senses a genuine threat."
    show kleio angry
    kleio.say "And why the fuck would you do that, pray tell?"
    kleio.say "Since when have those two dummies been more edgy than me?"
    kleio.say "They wouldn't know 'out there' if they woke up next to it in bed the morning after a bender!"
    show kleio upset
    "I do the best I can not to smile as Kleio walks right into my trap."
    "By now she's so pissed off at being passed over it's clouding her vision."
    "Which means that she's far less likely to really think about what I have to suggest."
    mike.say "If you say so, Kleio..."
    mike.say "I was just thinking that nudity is like, the final frontier, right?"
    mike.say "I mean, everyone makes a statement with how they dress."
    mike.say "So if The Deathless Harpies wore nothing on stage..."
    mike.say "Wouldn't that make us the most cutting edge band out there?"
    show kleio annoyed
    "Kleio frowns at me as my point finally becomes clear."
    kleio.say "What are you saying, Loverboy?"
    show kleio surprised
    kleio.say "That you want us to do gigs in the buff?!?"
    "I nod eagerly, trying to sound convincing."
    mike.say "Exactly that, Kleio..."
    mike.say "We should all perform in the nude!"
    if kleio.love >= 150 and kleio.sub >= 100:
        show kleio annoyed
        "For a moment I think that Kleio's going to laugh in my face."
        "But then I see that she's actually thinking about it."
        kleio.say "You know what..."
        show kleio normal
        kleio.say "You might have a point!"
        kleio.say "We're always getting labelled and put into little boxes our entire lives."
        kleio.say "Even the clothes we wear are really corporate name tags and billboards."
        show kleio punk
        kleio.say "It's only when we're naked that we're stripped of all that bullshit."
        kleio.say "That we're really showing our true selves!"
        show kleio normal
        "I'm perhaps following less than fifty percent of what Kleio's saying."
        "But I can sense that most of it is positive and getting her fired-up."
        "All of which means Kleio's about to jump onto the bandwagon in a big way."
        mike.say "I knew I should have stuck to my instinct, Kleio..."
        mike.say "I knew that I should have come to you first!"
        mike.say "You're the one that always thinks outside of the box!"
        show kleio seductive
        "Kleio might pretend not to like praise and flattery."
        "But the truth is that she likes it every bit as much as the next girl."
        "Perhaps even more so if it's pitched to flatter her radical self-image."
        show kleio happy
        kleio.say "You got that right, Loverboy!"
        kleio.say "If anyone's got the balls to be naked on stage, it's me."
        show kleio normal
        kleio.say "Now you go ask the others the same question."
        kleio.say "And see if they have the stones for it too!"
        show kleio normal
        "I nod, agreeing to everything Kleio's saying."
        "As well as doing the best I can to pretend this was her idea."
        "Because that's another way to wrap her round your finger."
        "And one more thing that she's unlikely to notice too."
        $ kleio.flags.agree_concert_naked = True
    else:
        show kleio happy at startle
        "Kleio throws back her head and laughs at the suggestion."
        "Then she looks me in the eye and makes a point of laughing in my face too."
        kleio.say "Ha!"
        show kleio talkative
        kleio.say "You're gonna have to do better than that, Loverboy."
        show kleio normal
        "I shake my head, trying to look confused by her answer."
        mike.say "I don't get it, Kleio..."
        mike.say "What are you talking about?"
        show kleio annoyed
        "Kleio rolls her eyes."
        "Apparently seeing through the act."
        show kleio talkative
        kleio.say "You think I haven't been worked on like that before?"
        kleio.say "Tell me the others are more likely to get your pitch..."
        show kleio normal
        kleio.say "Then reel me in when you hurt my pride?"
        kleio.say "And performing in the nude?"
        kleio.say "Really?"
        show kleio punk
        kleio.say "Just how dumb do you think I am?!?"
        show kleio normal
        "I can feel myself starting to get embarrassed and awkward."
        "Pretty soon I'm looking this way and that, trying to avoid her eye."
        mike.say "No, Kleio..."
        mike.say "It's not like that at all."
        show kleio a seductive at center, traveling(2.0, 0.5, (640, 1340))
        "Kleio leans in with a smile on her face."
        "Such a sweet one that it catches me totally off-guard."
        show kleio a upset with vpunch
        "But then I gasp as she grabs hold of my balls and squeezes."
        mike.say "Argh..."
        show kleio a normal
        kleio.say "You just be thankful that you get to see me naked at all, Loverboy..."
        $ kleio.sub -= 5
        show kleio a punk
        kleio.say "Or else I'll chop these things off and wear them on a necklace!"
        $ kleio.flags.agree_concert_naked = False
    scene bg black with dissolve
    return

label sasha_concert_naked:
    show sasha annoyed at center, zoomAt(1.25, (440, 880)) with fade
    "Some girls you need to build up to it with."
    "Other's you need to make them think it was their idea."
    "But when it comes to a girl like Sasha, neither of those works."
    "With her, you know that you're just going to have to come out with it."
    "And whether she says yes or no depends on how you pitch the idea to her."
    "The only problem with all of that is the nature of what I need to ask Sasha."
    "Because as well as the chances of her saying yes or no, she might also get mad."
    "Which means that I'm going to have to be prepared to flee the scene too."
    "As well as looking for the signs that's where things are going."
    show sasha at center, traveling(1.5, 1.0, (540, 1040))
    mike.say "Sasha..."
    mike.say "There's no way to dress this up."
    mike.say "So I'm just going to come out and say it, okay?"
    show sasha normal at center, zoomAt(1.5, (640, 1040)) with ease
    "Sasha turns to face me as I'm saying all of this."
    "And I see that she's raised her eyebrows as well."
    show sasha shout
    sasha.say "Oh..."
    sasha.say "Is that so?"
    show sasha normal
    mike.say "Erm..."
    mike.say "Yeah, it is."
    mike.say "So just hear me out before you judge me..."
    show sasha annoyed
    "Now Sasha looks more intrigued than ever."
    "And I can feel the pressure as her eyes bore into me."
    mike.say "I..."
    mike.say "I was thinking..."
    "Sasha nods."
    show sasha joke
    sasha.say "I thought you did that on occasion."
    mike.say "Ha, ha..."
    mike.say "Anyway..."
    show sasha upset
    mike.say "I was thinking about the band."
    mike.say "Specifically how we could get more eyes on us."
    show sasha normal
    "I see Sasha's expression change as I mention the band."
    "Like she's heard something she takes seriously for the first time."
    show sasha shout
    sasha.say "You have?"
    sasha.say "That's great, [hero.name]!"
    sasha.say "So what are you thinking?"
    sasha.say "I'm always coming up with ideas of my own..."
    sasha.say "But anything you've come up with I want to hear!"
    show sasha normal
    "I take a deep breath, preparing myself to take a leap."
    "Because this is going to be a bit of a gamble."
    mike.say "Okay, Sasha..."
    mike.say "I want you to expand your mind for a moment..."
    mike.say "And imagine the impression we'd make performing naked!"
    show sasha stuned
    "Sasha looks at me blankly for a moment."
    "Then she blinks and shakes her head."
    "Almost like she's not sure she heard me right."
    show sasha surprised
    sasha.say "I'm sorry..."
    sasha.say "Did you just say naked?"
    sasha.say "As in nude?"
    show sasha stuned
    "I nod my head, still trying to look serious."
    "Because I figure I have to in order to sell the idea."
    mike.say "That's exactly what I said, Sasha."
    mike.say "I'm suggesting that The Deathless Harpies perform naked."
    mike.say "I believe it'd make us stand out, make us unique."
    if sasha.love >= 175 and sasha.sub >= 95:
        "I'm expecting Sasha to tell me I'm crazy."
        "And so I have a couple of back-up arguments ready to go."
        show sasha normal
        "But much to my surprise, I see that she's actually nodding!"
        show sasha shout
        sasha.say "You know what..."
        sasha.say "That's something I'd never have thought of myself!"
        sasha.say "It's so crazy and out there, but it might just work."
        show sasha normal
        "Now it's my turn to be the one looking at Sasha like I've misheard."
        "Because I was so ready for her to tell me I was talking shit."
        "The idea she might be agreeing with me just won't take hold."
        mike.say "And that's..."
        mike.say "A good thing?"
        show sasha embarrassed
        "Sasha nods, though I can see she's still thinking."
        "Like the idea is starting to gain a footing in her mind."
        "Changing and mutating as she starts to get to grips with it."
        show sasha shout
        sasha.say "Yeah, [hero.name]..."
        sasha.say "So long as we handle it the right way."
        sasha.say "Like it has to make artistic sense."
        sasha.say "So it's obvious we're making a bold statement."
        show sasha joke
        sasha.say "Not just parading around in the nude like strippers!"
        show sasha normal
        "I'm more than eager to support Sasha in this."
        "To begin the process of this becoming her idea as much as mine."
        mike.say "Sure, Sasha, sure..."
        mike.say "That's kind of your thing, right?"
        mike.say "Bending the idea into a shape that makes sense?"
        show sasha happy
        "Sasha's nodding more than ever."
        "Warming to the idea more with each second that passes."
        show sasha shy
        "And I have to stop myself from smiling too much."
        "Or else I'm afraid that I'll give the game away."
        "But it looks like I managed to pull it off."
        "Sasha's on board, which means I have a serious ally on my side going forwards."
        $ sasha.flags.agree_concert_naked = True
    else:
        show sasha annoyed
        "Sasha doesn't hesitate to shake her head at this."
        show sasha at startle
        "And she adds a chuckle for good measure."
        "Making it clear to me she doesn't agree in the slightest."
        sasha.say "It'd make us look unique alright..."
        show sasha vangry
        sasha.say "Uniquely stupid!"
        show sasha angry
        "I'm already doing the best I can to argue."
        "Shaking my own head in response to her answer."
        mike.say "But don't you see, Sasha?"
        mike.say "It's artistically bold..."
        mike.say "A way to challenge perceptions of..."
        show sasha a upset
        "Sasha holds up a hand to stop me."
        "Cutting me off before I can get into my stride."
        show sasha vangry
        sasha.say "Forget it, [hero.name]."
        sasha.say "People go to a gig to hear music."
        sasha.say "And they go to a strip-club to see naked flesh."
        sasha.say "If you want to see one, you're not interested in the other!"
        show sasha upset
        "I open my mouth to say more."
        "But the way Sasha narrows her eyes silences me."
        show sasha annoyed
        sasha.say "Just forget about the idea, okay?"
        sasha.say "And if this is the kind of thing you dream up for the band..."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        show sasha vangry
        sasha.say "Then you'd be better stopping that too, and leaving it up to me."
        $ sasha.flags.agree_concert_naked = False
    scene bg black with dissolve
    return

label naked_gig(gig_location="pub"):
    $ band_members_id = Harem.find_by_name("band").active_members
    $ renpy.random.shuffle(band_members)
    $ concert_bg = 'stage' if gig_location in ['nightclub', 'concert'] else 'pub'
    "I guess that I shouldn't be the one suffering from nerves right now."
    "Because this was originally my idea, and I talked the girls into it too."
    "But now we're mere seconds away from going onstage to perform."
    "And suddenly the idea of doing so naked sounds a whole lot scarier!"
    if Harem.find("amy", name="band"):
        show amy naked at mostright4
        show sasha naked at mostleft4
        show kleio naked at left4
        show anna naked at right4
        with fade
    else:
        show sasha naked at left
        show kleio naked
        show anna naked at right
        with fade
    "I take a look around, checking out everyone that's standing around me."
    "Which immediately makes me feel at least a little better."
    "As I get a sudden reminder that, as intimidating as this is, at least I won't be doing it alone!"
    "I see Sasha, naked as the day she was born and psyching herself up like she always does."
    "Then there's anna, twirling her drumsticks as though there's nothing weird about her being naked."
    "Kleio, going through her usual vocal exercises, even though I can see how they make her chest jiggle."
    if Harem.find("amy", name="band"):
        "And last of all Amy, freshly reinstated and just as bare-assed as the rest of us."
    show anna talkative
    anna.say "Are yah ready, [hero.name]?"
    show anna happy
    anna.say "Because I sure am!"
    show anna normal
    "At the sound of Anna's voice, I turn to face her."
    "And it takes me a moment to figure out what's going on."
    "She's looking at me with confidence and excitement written all over her face."
    "And I suddenly realise that she must have taken my gazing over the band as me checking their readiness."
    "So now she's doing the best she can to prove that she's ready for the task ahead."
    mike.say "Oh..."
    mike.say "Oh yeah, Anna..."
    mike.say "I'm ready to go out there and knock them dead!"
    "Kleio chooses that exact moment to jump into the conversation."
    "Chuckling to herself and raising an eyebrow as she does so."
    show kleio talkative
    kleio.say "You'd better be, Loverboy..."
    show kleio annoyed
    kleio.say "This was your idea, remember?"
    show kleio normal
    show sasha annoyed
    "Before Kleio can say anything more, Sasha comes to my rescue."
    show sasha shout
    sasha.say "Yeah, and we all agreed to it too."
    show sasha joke
    sasha.say "Do you remember that, Kleio?"
    show sasha normal
    show kleio talkative
    "Kleio's about to say something back to Sasha."
    show kleio normal
    if Harem.find("amy", name="band"):
        "But then Amy cuts her off before she can speak."
        show amy lying
        amy.say "No time for that, guys..."
        show amy happy
        amy.say "That's our cue!"
        show amy normal
    else:
        "But then Anna cuts her off before she can speak"
        show anna talkative
        anna.say "No time for that, guys..."
        anna.say "That's our cue!"
        show anna normal
    "In the moments that follow, instinct seems to take over."
    "Everyone hurries to do all the things they'd do at a normal gig."
    "Habit seeming to make us forget for a moment that we're all naked."
    "And the next thing I know, we're all running out onto the stage."
    show expression f"concert {concert_bg} {' '.join(band_members_id)} naked mc_flaccid" with fade
    "I pick up my guitar and sling it around my neck without thinking."
    "It's only when I look down to check everything out that I remember I'm in the nude!"
    "Looking up, I can see that everyone else seems to be having a similar moment of realisation."
    "But then I hear the sound of the crowd, and I'm amazed to find that they're cheering."
    "And by that I mean they're cheering even more than normal."
    mike.say "Wow..."
    mike.say "I...I think they like it!"
    "Sasha and Kleio join me as I stand staring out into the crowd."
    sasha.say "They're going crazy, and we haven't even played a note!"
    kleio.say "You think that's new?"
    kleio.say "I swear I see naked folks out in the crowd too!"
    "Straining to see where Kleio's pointing, my eyes bulge in their sockets."
    mike.say "Fucking hell..."
    mike.say "You're right, Kleio..."
    mike.say "People are actually taking their clothes off out there!"
    kleio.say "Man..."
    kleio.say "We need to get playing, before this thing turns into a riot!"
    mike.say "Or an orgy!"
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "With that, we launch into our set."
    "And the familiar routine of playing our material soon helps to ground me."
    "Sure, things still feel weird, but I feel like we're quickly getting used to it."
    "The only problem is that another feeling is starting to creep up on me as we play."
    hide concert
    show expression f"concert solo {concert_bg} {band_members_id[0]} naked" with fade
    "Because every time I sneak a look at one of the girls, I start feeling hot under the collar."
    "Yeah, yeah...I know I'm not wearing one - it's a figure of speech!"
    show expression f"concert solo {concert_bg} {band_members_id[1]} naked" with fade
    "I went into this thing just thinking it would be a chance to see them all naked, you know?"
    "A gimmick that might take off, but even if it didn't, a chance for me to get a real eyeful."
    show expression f"concert solo {concert_bg} {band_members_id[2]} naked" with fade
    "But I never banked on the sight of them playing in the nude affecting me so much."
    "It's a challenge for me to keep my mind on the song that I'm playing."
    if Harem.find("amy", name="band"):
        show expression f"concert solo {concert_bg} {band_members_id[3]} naked" with fade
    "Because all it seems to want to do is imagine getting up to fun stuff with the girls."
    hide concert solo
    show expression f"concert {concert_bg} {' '.join(band_members_id)} naked mc_hard" with fade
    "And before too long, let's just say that I'm grateful for the way my guitar covers my groin!"
    "Doing the best I can to clear my mind of sexual thoughts, I try to focus on just playing."
    scene bg black
    show expression f"concert solo {concert_bg} mike naked" at center, zoomAt(1.35, (640, 960))
    with fade
    "But when I walk over to Sasha to do the duelling guitars thing, I get a big surprise."
    "Because she reaches out and tries to put her hand behind my instrument."
    "And...well...on my other instrument!"
    "I manage to dodge out of the way in time, and all she gets is a pinch of one buttock."
    scene bg black
    show expression f"concert {concert_bg} {' '.join(band_members_id)} naked mc_hard"
    with fade
    "But as soon as I'm safely out of reach, I take the time to check out the girls."
    "And I'm amazed to see the tell-tale signs of them all being in a similar state to me."
    "Somehow the experience of playing naked is getting them worked up as well!"
    "That's not all though, there's something else starting to happen."
    "The state we're all getting into is making us screw up the music too."
    "Right now it's subtle, luckily too subtle for the crowd to notice."
    "Though if I don't do something about it soon, then we're going to be in serious trouble."
    "But the question is what am I actually going to do?"
    "What one spontaneous act could release all that sexual tension?"
    "Suddenly it hits me, and I steal a glance down at my still painfully hard cock."
    "I'm going to have to put it to use, to actually do one of the girls right here and right now!"
    "But which one of them is it going to be?"
    menu:
        "Fuck Amy" if Harem.find("amy", name="band"):
            "I look to my left and see Amy, playing away like a demon."
            scene bg black
            show expression f"concert solo {concert_bg} amy naked" with fade
            "And before I know it, I'm walking straight towards her."
            "She turns and sees me as I make it over to her."
            amy.say "[hero.name]..."
            amy.say "Is it just me..."
            amy.say "Or did it get REALLY hot in here?"
            "I'm nodding and doing the best I can to maintain eye contact with Amy."
            "But I keep getting distracted by the sight of her rather magnificent breasts."
            "And the fact that I'm staring at them doesn't seem to be lost on her."
            mike.say "Yeah, Amy..."
            mike.say "So hot..."
            mike.say "So totally and utterly hot!"
            amy.say "You think that's hot?"
            amy.say "Then wait until you get a load of this!"
            "Before I know what's happening, Amy turns her back to me."
            scene bg black
            $ renpy.show (f"amy stand {concert_bg} mike goofy")
            with hpunch
            "And then she literally thrusts her ass up against my groin!"
            "Her butt pushes my guitar out of the way, revealing my painfully hard cock."
            "Which obviously then ends up sliding neatly between Amy's thighs too."
            "Before I can say a word, Amy looks back over her shoulder."
            $ renpy.show (f"amy stand opened")
            amy.say "Don't make me beg, [hero.name]..."
            amy.say "Just give me what I want..."
            amy.say "Please!"
            $ renpy.show (f"amy stand goofy")
            "Forgetting where we are and what's going on around us, I hurry to oblige."
            "My hands seize Amy's waist and I thrust myself forwards."
            "At the same time she bends over, her hands almost touching the stage."
            "This means that she's spread wide, almost letting me straight in."
            "The resistance that I meet only lasts a few short seconds."
            "And then I plunge all the way into Amy, not stopping until I'm filling her."
            "What follows is a desperate coupling, rough and frenetic in nature."
            "Looking over Amy's shoulder means that I'm pretty much staring into the crowd."
            "And it doesn't take long for the fans watching to figure out what we're doing."
            "I start to hear cheers and chants aimed directly at us, urging us on."
            $ renpy.show (f"amy stand opened up", at_list=[stepback(speed=0.05, h=10, v=0)])
            pause 0.2
            $ renpy.show (f"amy stand down")
            "This makes me start to bang Amy harder than ever."
            "Obviously this also means the two of us can't play at the same time."
            $ renpy.show (f"amy stand up", at_list=[stepback(speed=0.05, h=10, v=0)])
            pause 0.2
            $ renpy.show (f"amy stand down")
            "But the other members of the band quickly step in to pick up the slack."
            "The girls improvise, playing impromptu chords inspired by our actions."
            $ renpy.show (f"amy stand up blush breath hair", at_list=[stepback(speed=0.05, h=10, v=0)])
            pause 0.2
            $ renpy.show (f"amy stand down")
            "And Anna hammers out a solo to go along with it too."
            "I feel strangely honoured to have them play as I fuck Amy."
            $ renpy.show (f"amy stand up", at_list=[stepback(speed=0.05, h=10, v=0)])
            pause 0.2
            $ renpy.show (f"amy stand down")
            "But the way that we're going at it means things don't last too long."
            "I can already feel the end coming up on me fast."
            $ renpy.show (f"amy stand ahegao tongue sparkles up", at_list=[stepback(speed=0.05, h=10, v=0)])
            pause 0.2
            $ renpy.show (f"amy stand down insert")
            with hpunch
            pause 0.2
            $ renpy.show (f"amy stand down insert cum")
            with hpunch
            "And when it happens I make one final thrust into Amy."
            with hpunch
            "She takes all that I have to give, and then sinks down onto her knees."
            "Amy slides off my cock and leaves me standing there, exposed and exhausted."
        "Fuck Anna":
            "All it takes is one look over my shoulder and at the drumkit."
            scene bg black
            show expression f"concert solo {concert_bg} anna naked" with fade
            "As soon as I set my eyes on Anna, sitting there behind it, my mind's made up."
            "She's still hammering away with her drumsticks as I hurry over to her."
            "And the force with which she's hitting the drums is making her breasts bounce up and down too!"
            anna.say "Oh..."
            anna.say "Hey, [hero.name]..."
            anna.say "You wanna do a cool solo or something?"
            "I shake my head in response, already taking hold of Anna's waist."
            mike.say "Not exactly, Anna."
            mike.say "I want to do something..."
            mike.say "But it's not a solo."
            "Anna seems to be too confused to resist my efforts to make her stand."
            "And instead she just looks at me with a puzzled expression on her face."
            anna.say "Huh..."
            anna.say "Then what is it?"
            mike.say "Actually, Anna..."
            mike.say "It's you!"
            "Swinging my guitar around my back, I thrust myself forwards."
            "Luckily for me, Anna's drumkit stands on a platform."
            show expression f"anna standing {concert_bg}" with fade
            "And that means her ass is at the perfect height for what I have in mind."
            "The head of my cock pushes right between Anna's buttocks."
            "And she lets out a squeal of surprise as I begin to go deeper still."
            anna.say "Oh wow..."
            anna.say "Are you?"
            show expression f"anna standing {concert_bg} pleasure"
            anna.say "You really are!"
            "I can feel how Anna's already beginning to lean back into me."
            "Which lets me know that she's up for it too, despite her surprise."
            "And it doesn't take long for her body to send me a similar message too."
            show expression f"anna standing {concert_bg} normal"
            "At first the muscles of Anna's ass resist my efforts to get inside."
            "But then I feel them start to relax, and I'm soon inching into her."
            "Looking over Anna's shoulder means that I'm pretty much staring into the crowd."
            show expression f"anna standing {concert_bg} pleasure"
            "And it doesn't take long for the fans watching to figure out what we're doing."
            "I start to hear cheers and chants aimed directly at us, urging us on."
            "This makes me start to bang Anna harder than ever."
            show expression f"anna standing {concert_bg} wiggle"
            "In turn she's forced to brace herself against her drumkit."
            "Obviously this also means the two of us can't play at the same time."
            "But the other members of the band quickly step in to pick up the slack."
            "The girls improvise, playing impromptu chords inspired by our actions."
            show expression f"anna standing {concert_bg} wiggle pull"
            "All of which only serves to encourage me in banging Anna harder still."
            "For her part, Anna's moaning with every thrust."
            "And the way I'm pushing her into the drums makes them thump in time."
            with vpunch
            "Suddenly I feel myself losing it, shooting my load into Anna's ass."
            show expression f"anna standing {concert_bg} ahegao" with vpunch
            "This seems to make her cum too, throwing her hands up as she does so."
            show expression f"anna standing {concert_bg} ahegao -wiggle -pull annahand" with vpunch
            "They hit the cymbals, causing a clattering noise that sums up Anna's orgasm pretty well."
            "Then I gently lower her back down onto her stool."
            "And she slides smoothly off my cock to slump over her drums."
            $ anna.sexperience += 1
            $ anna.love += 4
        "Fuck Kleio":
            "I cast my gaze around the stage, looking at each of the girls in turn."
            scene bg black
            show expression f"concert solo {concert_bg} kleio naked"
            with fade
            "But as soon as my eyes settle on Kleio, I forget all about the others."
            "Without a conscious thought, I start walking the short distance towards her."
            "And I haven't taken more than two steps before her head snaps around."
            "I freeze as Kleio looks straight at me, like she could sense my approach."
            "As soon as she does so, I feel my heart sink a little."
            "Because I can't help thinking that she's about to tell me to back off."
            "So it comes as a real surprise when she turns and starts running towards me!"
            mike.say "Wha..."
            mike.say "What are you..."
            "I don't get the chance to finish what I was going to say."
            "Because the distance between Kleio and me is only a couple of metres at the most."
            "And even before she reaches me, I see her leap backward into the air."
            "Kleio launches herself into the air, reaching out for me."
            "I only just manage to react in time."
            "Slinging my guitar behind me on it's strap, I spread my arms and catch the incoming Kleio!"

            $ renpy.show (f"kleio reverse cowgirl {concert_bg} hard hurt mic")
            with fade
            "Her weight and momentum make me stagger backwards."
            "And I fail to keep my balance and not topple over."
            mike.say "Kleio..."
            mike.say "What's going on?!?"
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} hard pleasure")
            kleio.say "No time for explanations, Loverboy..."
            kleio.say "I need it now, and I need it bad!"
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} hurt")
            "It takes me a second to realise that Kleio's on the exact same wavelength as me."
            "That she wants the same thing as I do right now."
            mike.say "Me too, Kleio..."
            mike.say "Great minds, eh?"
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} pleasure")
            kleio.say "Never mind that..."
            kleio.say "Just hurry up and fuck me already!"
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} hurt")
            "Kleio might have put herself in my arms and be ordering me to satisfy her right now."
            "But that still doesn't mean that she's going to sit back and wait for it to happen."
            "And I know that because I can already feel her reaching down and grabbing hold of my cock!"
            "The next thing I know, Kleio's pushing it hard against the lips of her pussy too."
            "It seems that Kleio's even more ready for it than I thought too."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} vaginal fist ")
            with vpunch
            "Because almost the same moment she pushes down there, I feel myself starting to sink into her."
            "I hear myself gasping almost like it's someone else making the sound."
            "Because almost all of my senses are occupied with the sensation of what's going on down there."
            "And even when I'm inside, Kleio doesn't let up or leave me to take the lead."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} up")
            pause 0.2
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} vaginal down", at_list=[startle(0.05,-10)])
            "Instead she begins to bounce up and down in my arms, riding me for all she's worth!"
            "Looking over Kleio's shoulder means that I'm pretty much staring into the crowd."
            "And it doesn't take long for the fans watching to figure out what we're doing."
            "I start to hear cheers and chants aimed directly at us, urging us on."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} up")
            pause 0.2
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} vaginal down", at_list=[startle(0.05,-10)])
            "This makes Kleio start to ride me harder than ever."
            "Obviously this also means the two of us can't play at the same time."
            "But the other members of the band quickly step in to pick up the slack."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} up")
            pause 0.2
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} down closed", at_list=[startle(0.05,-10)])
            "The girls improvise, playing impromptu chords inspired by our actions."
            "All of which only serves to encourage me to got at Kleio harder still."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} pleasure up")
            pause 0.2
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} down rock punk ahegao", at_list=[startle(0.05,-10)])
            "Pretty soon I feel myself start to reach my limit."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} up")
            pause 0.2
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} down cum")
            with vpunch
            "And within moments I shoot my load into Kleio."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} down squirte back")
            with vpunch
            "She clings on tighter than ever, her own orgasm taking hold."
            $ renpy.show (f"kleio reverse cowgirl {concert_bg} -squirte flacid down -cum aftercum")
            with vpunch
            "Then I collapse onto my back, letting Kleio slide off of me too."
        "Fuck Sasha":
            "All it takes is a quick look around the stage for me to make up my mind."
            scene bg black
            show expression f"concert solo {concert_bg} sasha naked" with fade
            "Guitar in hand, I march over to where Sasha's standing with her own instrument."
            "Then I walk up behind her, pressing myself against her back."
            "I figure that way I can make it look like I'm coming over to play a duet."
            "Maybe even challenge Sasha to a kind of solo-duel with our guitars."
            "But the moment I make it over there, Sasha leans back into me."
            "Or maybe it'd be more honest to say that she rubs her ass against my groin!"
            mike.say "Whoa..."
            mike.say "Settle down, Sasha..."
            mike.say "I can't play with you doing that to me!"
            "When Sasha turns her head to look back at me, I'm surprised by what I see."
            "Because the look on her face and in her eyes is one of totally helpless hunger."
            "And by that I mean hunger of the distinctly sexual kind!"
            sasha.say "It's no use, [hero.name]..."
            sasha.say "I...I'm just so horny right now..."
            sasha.say "I have to do something about it!"
            "I do the best I can to look concerned, rather than turned-on."
            mike.say "Don't worry, Sasha..."
            mike.say "I think I know what might help."
            "Swinging my guitar around on it's strap, I free my cock to pop out in front of me."
            "And the moment she lays eyes on it, Sasha seems to tune into the same wavelength I'm on."
            sasha.say "Oh yeah..."
            sasha.say "I think that'd do it!"
            "Not wasting any time, I reach out and take hold of Sasha's wrists."
            "And as I thrust myself forwards, she pushes her ass backwards."
            show expression f"sasha stand {concert_bg}" with fade
            "Normally there'd be some work to do before the real action happened."
            "But the moment I feel the head of my cock touch the lips of her pussy, they begin to part."
            "So it looks like Sasha wasn't exaggerating when she said that she was desperate."
            show expression f"sasha stand {concert_bg} vaginal insert"
            "This means that I begin to sink into her almost without any effort on my part."
            "And as soon as I'm inside Sasha, I start to pump away in earnest."
            "Looking over Sasha's shoulder means that I'm pretty much staring into the crowd."
            "And it doesn't take long for the fans watching to figure out what we're doing."
            show expression f"sasha stand {concert_bg} vaginal pleasure insert"
            "I start to hear cheers and chants aimed directly at us, urging us on."
            "This makes Sasha start to push herself back and into me harder than ever."
            show expression f"sasha stand {concert_bg} vaginal speed wiggle insert"
            "Obviously this also means the two of us can't play at the same time."
            "But the other members of the band quickly step in to pick up the slack."
            show expression f"sasha stand {concert_bg} vaginal speed wiggle normal insert"
            "The girls improvise, playing impromptu chords inspired by our actions."
            "All of which only serves to encourage me to got at Sasha harder still."
            "Pretty soon I feel myself start to reach my limit."
            show expression f"sasha stand {concert_bg} vaginal speed wiggle creampie insert" with vpunch
            "And within moments I shoot my load into Sasha."
            show expression f"sasha stand {concert_bg} vaginal speed wiggle ahegao" with vpunch
            "She pushes back harder than ever, her own orgasm taking hold."
            show expression f"sasha stand {concert_bg} vaginal wiggle ahegao" with vpunch
            "Then I let go of Sasha's wrists, letting her slide off me."
            "And luckily for me she collapses onto her knees, rather than landing flat on her face."
            $ sasha.sexperience += 1
            $ sasha.love += 4
    scene expression f"bg {gig_location}"
    if Harem.find("amy", name="band"):
        show sasha naked at mostleft4
        show kleio naked at left4
        show anna naked at right4
        show amy naked at mostright4
        with fade
    else:
        show sasha naked at left
        show kleio naked
        show anna naked at right
        with fade
    "After the show, everyone comes off the stage still buzzing with sexual energy."
    "And we make it back to the dressing-room where our clothes are without anyone saying a word."
    "The silence is kept up as we all begin to get dressed, but it's obvious something's different."
    "It feels like we crossed a line tonight, that we did something revolutionary."
    "And while I have no idea where this is ultimately going to go..."
    "I just feel like things are never going to be the same for The Deathless Harpies."
    return

label kleio_anna_cheating_confrontation:


    kleio.say "Hey, asshole, stop right there - I want a word with you!"
    "At the sound of the familiar voice and the irate tone in which it's owner is speaking, I freeze on the spot."
    "Spinning around, I'm treated to the rather intimidating sight of Kleio, hands on hips and with a face like thunder."

    $ renpy.scene()

    $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(1.75, (1040, 1120))])
    show kleio a angry at center, zoomAt(1.75, (440, 1120))
    with hpunch
    mike.say "Erm...hey, Kleio!"
    mike.say "Look, I'd love to stop and chat, really I would."
    mike.say "But I just remembered that I have to be somewhere else right now!"
    "I turn and try to make good my escape at the very moment that Kleio's lips begin to form an objection."
    "My desperate hope is that I can fall back on the lame old excuse of not having heard her before I turned tail and ran away."

    hide kleio
    $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(1.75, (240, 1120))])
    show anna b angry at center, zoomAt(1.75, (840, 1120))
    with hpunch
    "But as soon as my head is facing in the opposite direction, I almost run into Anna, already blocking my route of escape."
    "She's looking almost as serious as Kleio does right now, arms crossed over her chest, squashing her large breasts together."
    "Ah...it's probably not the best time to be thinking like that!"
    "Dammit though, she used her diminutive stature to sneak past me without being seen and cut me off."
    mike.say "Anna...I didn't see you down there!"
    "Oops - pretty much the worst opening line I could have come out with, especially given the circumstances of the meeting."
    "Luckily for me, Anna seems to be too worked up to actually notice what I just said to her anyway."
    anna.say "You're not going anywhere, [hero.name]."
    show anna angry
    anna.say "Not until you explain yourself, you...you...you creep!"
    show anna annoyed
    "In the time that I've been bandying words with Anna, Kleio has caught up with me too."
    $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(2, (140, 1240))])
    show anna a angry at center, zoomAt(2, (840, 1240))
    with vpunch
    pause 0.3
    show anna b
    "She gives me a shove in the small of the back, sending me staggering a couple of steps forward."
    show kleio a angry at center, zoomAt(2, (-280, 1240))
    $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1.75, 1.5, (240, 1120))])
    show kleio a angry at center, traveling(2.5, 1.5, (340, 1500))
    show anna b angry at center, traveling(2.5, 1.5, (940, 1500))
    pause 1.5
    "And then they advance on me as one"
    mike.say "So...I guess that Sasha's already had that little chat with you guys?"
    show kleio angry zorder 2 at traveling(3.5, 1.5, (440, 2040))
    "Kleio leans in and shoves a finger literally within an inch of my eye."
    "And for a moment, I actually think that she might use it to scoop out my eyeball, right there and then."
    kleio.say "Of course she told us, you lousy douchebag!"
    kleio.say "We were all bandmates long before you ever showed up."
    kleio.say "We were like sisters - and sisters look out for each other!"
    show kleio a angry at center, traveling(2.5, 0.5, (340, 1500))
    "I can't help flinching back from Kleio's verbal assault, finding it almost impossible to look her in the eye."
    show anna sad
    "Looking away, I briefly make eye contact with Anna."
    "Though she was as angry as Kleio at first, I can instantly see that she's now wearing a sad, downcast expression."
    "That hurts worse than the way in which Kleio's words are stinging me, knowing that I've hurt a sweet girl like Anna so deeply."
    "Summoning all of my courage, I hold up and hand in front of Kleio's stream of abuse."
    $ renpy.scene()
    $ renpy.show(f"bg {game.room}")
    show kleio a angry at left
    show anna b angry at right
    with fade
    mike.say "Okay, okay, Kleio - that's enough!"
    show kleio surprised
    "She stops in her tracks, probably more from the shock of being told to shut up than any genuine desire to cease her attack on me."
    mike.say "That's enough..."
    "I repeat the words for a second time and in a more calm tone."
    mike.say "So you've heard Sasha's side of things, and now you're pissed - I get that."
    mike.say "But the least you can do is listen to my side of the story as well."
    show kleio annoyed
    "Kleio's lips twist into the beginnings of a cynical sneer."
    show anna talkative
    "But before she can say another word, Anna puts a hand on her friend's arm, forcing her to stop."
    anna.say "He's right, Kleio."
    anna.say "We've only heard this from Sasha, and she was really mad when she told us about it."
    show anna normal
    "Trying not to sound too much like I'm desperately pouncing on the bone that Anna's just tossed me, I nod slowly in agreement."
    mike.say "She makes a good point, Kleio."
    mike.say "And I know you're not the kind of person to judge a guy like that - not without hearing his side."
    mike.say "I mean, that'd be the kind of thing a typical man would do to a woman in the same circumstances, wouldn't it?"
    "Kleio looks annoyed, but as the truth of my words sinks in, she begins to soften a little and then nods sadly."
    show kleio talkative
    kleio.say "Yeah, you got me, you prick..."
    kleio.say "So go on, spill your guts before I lose my patience and do it for you!"
    show kleio normal
    "For all her bravado, I can see just how much Kleio seems to have been genuinely hurt by what she's been told."
    "I don't know if what I have to say for myself will change any of that."
    "But I have to try, for the sake of everyone caught up in this mess that I've made."
    if (anna.flags.cheated) or (kleio.flags.cheated):
        with fade
        mike.say "Okay, you guys - cards on the table."
        mike.say "I don't want there to be any secrets between us, for good or bad."
        "I pause to take a deep breath before going on."
        mike.say "So, yes...I was seeing another girl on the side."
        mike.say "And yes, it was while we were all together..."
        show anna surprised
        "Anna instantly covers her mouth with her hands, her eyes watering with the promise of tears."
        show kleio angry
        "Predictably though, Kleio's sneer returns just as quickly, and she shakes her head, suspicions confirmed."
        mike.say "All I can say is that I was in a pretty strange place when we all hooked up together."
        mike.say "It's not an excuse - it's just what it is."
        mike.say "Maybe I just fell back into old habits with one girl because I wasn't quite ready to be with three all at the same time?"
        "I wait for a moment to see what kind of a reaction my bare confession will elicit."
        show anna sad
        show kleio annoyed
        "But Anna's still staring at me in silence and Kleio looks as though she's mulling over my words inside of her head."
        "Maybe what I need to do is focus on winning one of them over?"
        "And then convince them to help me do the same with the other..."
        menu:
            "I should try to convince Kleio":
                "Being the more rational and intelligent of the pair, surely Kleio's the one I can best reason with?"
                "I lean aside and whisper to her, making sure that Anna can't hear what I'm saying."
                $ renpy.show(f"bg {game.room}", at_list=[center, zoomAt(1.75, (1040, 1120))])
                show kleio at center, zoomAt(1.75, (440, 1120))
                show anna a at center, zoomAt(1.75, (1640, 1120))
                with fade
                mike.say "Hey, Kleio - you understand where I'm coming from, right?"
                mike.say "Yeah, I screwed up, but I'm only human and I'm sorry."
                "Kleio cocks her head on one side, regarding me with a renewed interest."
                show kleio talkative
                kleio.say "And I'd do that how, exactly?"
                show kleio normal
                mike.say "Talk to her - convince her that it's okay to forgive me too."
                "At this, a slow smile creeps across Kleio's face."
                show kleio b talkative
                kleio.say "Okay, [hero.name] - I'll make sure you get just what you deserve..."
                show kleio a angry
                play sound punch_hard
                with vpunch
                "Being up so close, there's no way I could have seen Kleio wind up and drive her knee into my groin."
                show kleio punk d
                pause 0.5
                $ renpy.show(f"bg {game.room}", at_list=[center, traveling(1.75, 0.3, (1040, 820))])
                show kleio at center, traveling(1.75, 0.3, (440, 820))
                show anna at center, traveling(1.75, 0.3, (1640, 820))
                pause 0.3
                play sound body_fall
                with vpunch
                "I make a muffled cry of agony and then collapse onto my knees, still moaning pathetically."
                show kleio at startle(0.05,-10)
                pause 0.1
                hide kleio
                hide anna
                with easeoutleft
                "Even though my eyes are watering from the pain, I can clearly see Kleio walk over to Anna and take her arm."
                "Together, they walk away, laughing at the sight of me doubled over and crying from the blow to the very thing that got me into this mess in the first place."
                $ kleio.love -= 25
                $ anna.love -= 25
            "I should try to convince Anna" if hero.charm >= 60 and anna.love >= 100:
                "I don't think I can appeal to reason, as Kleio looks ready to demand blood."
                "But I know that Anna's pretty much ruled by her heart over her head."
                mike.say "Anna, I know I fucked up, but I'm sorry."
                mike.say "Please, give me another chance?"
                mike.say "Imagine what the world would be like if no one ever did that for someone they loved?"
                show kleio annoyed
                "Kleio rolls her eyes at my words, but I can see that Anna's actually considering them."
                "She's made some pretty dumb mistakes of her own in the past, and I know that she's got a compassionate heart too."
                show anna talkative
                anna.say "Oh, [hero.name]...I DO want to give you another chance!"
                show anna normal
                mike.say "Thank you, Anna - you won't regret it, I promise you that."
                show kleio talkative
                kleio.say "Jesus, Anna - pass the bucket so I can puke!"
                show kleio annoyed
                show anna surprised
                "At first, Anna looks shocked at Kleio's dismissal of what just happened."
                show anna angry
                "But then her expression darkens, and then she's the one poking a finger into the other girl's surprised face."
                show kleio surprised
                show anna talkative
                anna.say "Like you're perfect, Kleio!"
                anna.say "I could tell some pretty juicy stories about you having your fun and thinking fuck the consequences!"
                anna.say "How many times have Sasha and I forgiven you, huh?"
                show anna annoyed
                "At the mention of her own past indiscretions, Kleio's cheeks redden, and she almost tries to cover Anna's mouth with both hands."
                show kleio talkative
                kleio.say "Alright, Anna - maybe you have a point after all!"
                kleio.say "I suppose we can give him another chance - ONE more chance, that is..."
                show kleio normal
                show anna happy
                "Anna nods happily and throws her arms around the both of us."
                "Pulled into an awkward embrace, I can only offer a nervous smile in answer to Kleio's own."
                "Neither of us seeming to know where this is going to go next."
                scene bg black with dissolve
                $ anna.love += 5
                $ kleio.love -= 5
    else:
        mike.say "When Sasha was telling you all about my many and various sins, did she happen to mention that I'd finished seeing the other girl before we all hooked up?"
        show anna surprised
        "Both Anna and Kleio seem to be about to say something as soon as I've finished speaking."
        "But as the message finally starts to sink in, they become confused, looking at each other in puzzlement."
        mike.say "I guess that's a no, then?"
        mike.say "Well, I suppose she was too emotional to remember that part."
        "I try to sound understanding as I say this, not wanting to come over as dismissing Sasha as some hysterical woman that can't control herself."
        "But I can already see that my side of the story had set Kleio to thinking again about what she's heard."
        "Anna, on the other hand, looks to be on the verge of an emotional outburst that I can't quite explain."
        "Surely what I've just told her should be a relief to hear?"
        "After seeing how differently they reacted to the same news, maybe I need to tackle them alone, rather than as a pair?"
        "Perhaps that way I can better convince them of what I'm saying?"
        menu:
            "I should try to talk to Anna":
                "I'm genuinely concerned for Anna after that unexpected reaction, so I try to talk to her first."
                mike.say "Anna, please - tell me what's wrong?"
                "Now she actually is crying, and I see the first of the tears rolling down her cheeks from her simply massive eyes."
                "Shit - she really does look like something out of a cheesy anime about soppy young girls and their first taste of romance!"
                show anna dazed
                anna.say "It's ruined...ruined..."
                anna.say "Why did you have to go and ruin it like that?!?"
                "I shake my head in honest confusion at this, not understanding what she means at all."
                mike.say "Anna, what are you even talking about?"
                mike.say "I just got done telling you that I didn't cheat on you, that the girl Sasha met was ancient history!"
                show anna cry
                "Anna shakes her head and wails in desperation, actually spraying her salty tears around like a lawn-sprinkler."
                show anna dazed
                anna.say "Why did you have to tell me that you'd been with that other girl, [hero.name]?"
                anna.say "Now I can't stop seeing you with her!"
                show anna cry
                "I can only shake my head in bafflement at this."
                mike.say "But, Anna...I've been with lots of other girls before you!"
                show kleio blush
                "At this, she throws her head back and begins to wail even louder than before."
                "I look at Kleio, my face showing that I'm desperate for an answer as to what I've done wrong."
                "But she just rolls her eyes in frustration and puts her arm around Anna's shoulder so that she can lead her sobbing friend away."
                "As I watch them go in a stunned silence, Kleio looks back at me and shrugs."
                "It seems like she's just as confused as to where this leaves us all as I am myself."
                $ anna.love -= 10
                $ kleio.love -= 5
            "I should try to talk to Kleio" if hero.charm >= 40 and kleio.love >= 80:
                "I know that Kleio's the less emotional of the pair, and so most likely to hear me out."
                "So I lean over to her and subtly nod in Anna's direction."
                mike.say "Kleio, you have to help me out here."
                mike.say "I thought you'd both be relieved to know I wasn't seeing that girl behind your backs."
                mike.say "But Anna's reacting like I was sleeping with the entire town!"
                show kleio annoyed
                "Kleio looks at me for a moment, as though she's about to say something about sisterhood and how all men are jerks."
                "But then she shakes her head and rolls her eyes, before turning to face Anna with a no-nonsense look on her face."
                show kleio angry
                show kleio talkative
                kleio.say "For fuck's sake, Anna, what's the matter with you now?"
                kleio.say "[hero.name] just swore to us that he wasn't cheating on us - isn't that what we wanted to hear?"
                show kleio annoyed
                show anna cry
                "Anna looks at her for a moment, her lip wobbling, and then bursts into a fresh flood of tears."
                show anna dazed
                anna.say "I...I...can't stop thinking about him with her!"
                show anna cry
                mike.say "But, Anna...it was ages ago!"
                "I find myself standing there, completely stumped as to what I should say or do next."
                "But luckily for me, it seems that Kleio's not suffering from the same problem."
                show kleio talkative
                kleio.say "Jesus, Anna - that's the most stupid thing you've ever said in front of me."
                kleio.say "And you really have said some stupid shit before now!"
                show kleio annoyed
                show anna surprised
                "The intensity of Kleio's tirade is enough to stop Anna's blubbering completely."
                "She stares at her friend with those massive watery eyes, shocked by the way she's being spoken to."
                show anna sad
                show kleio talkative
                kleio.say "We've all fucked people in our past, and we might end up fucking new people in the future too."
                kleio.say "Stop turning [hero.name] into some kind of fairy tale prince - because he sure as hell isn't one!"
                show kleio normal
                mike.say "Erm, thanks, Kleio...I think..."
                "Kleio wraps an arm around her friend's shoulder and begins to lead her away."
                "As I watch them go, Kleio looks back and gives me a weak smile."
                show kleio talkative
                kleio.say "Don't worry, [hero.name] - I'll take care of her."
                kleio.say "We all need to sit down and have this out between us."
                kleio.say "But I somehow, I think we'll be okay!"
                "I nod and smile, but keep quiet, hoping that Kleio's right."
                $ anna.love -= 5
                $ kleio.love += 5
        show kleio at startle(0.05,-10)
        show anna a at startle(0.05,-10)
        pause 0.1
        hide kleio
        hide anna
        with easeoutleft
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
