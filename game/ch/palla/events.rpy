init python:
    Consumable("cologne", effects=[("charm", 5), ("fun", 1)])

    Event(**{
    "name": "palla_start",
    "label": "palla_start",
    "conditions": [
        IsDone("palla_event_02"),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_event_02",
    "label": "palla_event_02",
    "duration": 1,
    "conditions": [
        IsDone("palla_event_01"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("clothesshop"),
            MinStat("charm", 50),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03",
    "label": "palla_event_03",
    "duration": 1,
    "conditions": [
        IsDone("palla_event_02"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("coffeeshop"),
            ),
        PersonTarget(palla,
            Not(IsPresent()),  
            IsFlag("palladelay", False),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })



    Event(**{
    "name": "palla_event_03a",
    "label": "palla_event_03a",
    "conditions": [
        IsDone("palla_event_03"),
        IsNotDone("palla_event_04"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("coffeeshop"),
            MinStat("money", 20),
            ),
        PersonTarget(palla,
            Not(IsPresent()),  
            IsFlag("palladelay", False),
            MinStat("love", 10),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03b",
    "label": "palla_event_03b",
    "conditions": [
        IsDone("palla_event_03a"),
        IsNotDone("palla_event_04"),
        HeroTarget(IsRoom("clothesshop")),
        PersonTarget(palla,
            Not(IsPresent()),  
            IsFlag("palladelay", False),
            MinStat("love", 20),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_03c",
    "label": "palla_event_03c",
    "conditions": [
        IsDone("palla_event_03b"),
        IsNotDone("palla_event_04"),
        HeroTarget(IsRoom("nightclub", "nightclubbar")),
        PersonTarget(palla,
            IsActive(),
            IsFlag("palladelay", False),
            MinStat("love", 30),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03d",
    "label": "palla_event_03d",
    "conditions": [
        IsDone("palla_event_03c"),
        IsNotDone("palla_event_04"),
        HeroTarget(
            IsActivity("offer_a_drink"),
            HasRoomTag("pub"),
            ),
        PersonTarget(palla,
            IsActive(),
            IsFlag("palladelay", False),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03e",
    "label": "palla_event_03e",
    "conditions": [
        IsDone("palla_event_03d"),
        IsNotDone("palla_event_04"),
        HeroTarget(
            IsActivity("offer_a_drink"),
            HasRoomTag("pub"),
            ),
        PersonTarget(palla,
            IsActive(),
            IsFlag("palladelay", False),
            MinStat("love", 50),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03f",
    "label": "palla_event_03f",
    "conditions": [
        IsDone("palla_event_03e"),
        IsNotDone("palla_event_04"),
        HeroTarget(
            IsActivity("train_with"),
            IsRoom("gym", "gymmachine"),
            MinStat("fitness", 40),
            ),
        PersonTarget(palla,
            IsActive(),
            IsFlag("palladelay", False),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_03g",
    "label": "palla_event_03g",
    "conditions": [
        IsDone("palla_event_03f"),
        IsNotDone("palla_event_04"),
        HeroTarget(
            IsActivity("None"),
            Not(OnDate()),
            IsRoom("coffeeshop"),
            MinStat("money", 10),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("palladelay", False),
            MinStat("love", 70),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_04",
    "label": "palla_event_04",
    "conditions": [
        IsDone("palla_event_03"),
        IsHour(0, 1),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            ContactKnown(),
            IsFlag("palladelay", False),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_04b",
    "label": "palla_event_04b",
    "conditions": [
        IsDone("palla_event_04"),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsActive(),
            IsFlag("nokiss"),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_05",
    "label": "palla_event_05",
    "conditions": [
        IsDone("palla_event_04"),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("nokiss", False),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_06",
    "label": "palla_event_06",
    "conditions": [
        IsDone("palla_event_05"),
        IsHour(23, 0),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            IsFlag("nodate"),
            IsFlag("gaveflowers"),
            IsFlag("gavesweets"),
            IsFlag("event6done", False),
            MaxFlag("datetries", 3),
            MinStat("love", 120),
            ),
        ],
    "gallery": {"conditions": [IsDone("palla_event_06")], 'character':'palla', 'label':'palla_event_06', 'id':'Restaurant BJ', 'icon': 'palla restaurantbj', 'scene': 'livingroom'},
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": False,
    })

    Event(**{
    "name": "palla_event_07",
    "label": "palla_event_07",
    "conditions": [
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("talksex"),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_07b",
    "label": "palla_event_07b",
    "conditions": [
        IsDone("palla_event_07"),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("relationshiptalkdelay", False),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_08",
    "label": "palla_event_08",
    "conditions": [
        IsDone("palla_event_07b"),
        IsHour(0, 1),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            MinStat("love", 120),
            MinStat("sub", 70),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_09",
    "label": "palla_event_09",
    "conditions": [
        IsDone("palla_event_07b"),
        IsDayOfWeek("1245"),
        IsHour(0, 4),
        HeroTarget(
            Not(OnDate()),
            IsRoom("nightclub", "nightclubbar"),
            ),
        PersonTarget(palla,
            Not(IsPresent())
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_10",
    "label": "palla_event_10",
    "conditions": [
        IsDone("palla_event_09"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("electronic"),
            ),
        PersonTarget(palla,
            Not(IsPresent())
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_11",
    "label": "palla_event_11",
    "conditions": [
        IsDone("palla_event_10"),
        IsHour(20, 0),
        HeroTarget(
            Not(OnDate()),
            IsRoom("map"),
            ),
        PersonTarget(palla,
            Not(IsPresent()),
            MinCounter("shawnencounter", 2),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_12",
    "label": "palla_event_12",
    "conditions": [
        IsDone("palla_event_11"),
        IsHour(20, 0),
        HeroTarget(
            Not(OnDate()),
            IsRoom("livingroom"),
            ),
        PersonTarget(palla,
            Not(IsPresent()),
            MinCounter("pallavisit12", 7),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_13",
    "label": "palla_event_13",
    "conditions": [
        IsDone("palla_event_12"),
        HeroTarget(
            Not(OnDate()),
            IsRoom("mall1"),
            ),
        PersonTarget(palla,
            HasRoomTag("mall_southside"),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_event_14",
    "label": "palla_event_14",
    "conditions": [
        IsDone("palla_event_13"),
        IsTimeOfDay("morning", "afternoon", "evening"),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            IsFlag("pallav14delay", False),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_baby_ok",
    "label": "palla_event_baby_ok",
    "conditions": [
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsActive(),
            IsFlag("pillchat"),
            MinStat("career", 75),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_preg_talk",
    "label": "palla_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    })

    Event(**{
    "name": "palla_mall_date_fuck",
    "label": "palla_mall_date_fuck",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsActivity("date_go_shopping"),
            IsRoom("date_mall1"),
            HasStamina(),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sexperience", 2),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_mall_date_fuck_02",
    "label": "palla_mall_date_fuck_02",
    "priority": 500,
    "conditions": [
        IsDone("palla_mall_date_fuck"),
        HeroTarget(
            IsActivity("date_go_shopping"),
            IsRoom("date_mall1"),
            HasStamina(),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sexperience", 2),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": False,
    })

    InteractEvent(**{
    "name": "palla_give_address",
    "label": "palla_give_address",
    "priority": 1000,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("love", 110),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "chances": 25,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_apartment_first_visit",
    "label": "palla_apartment_first_visit",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("pallalivingroom"),
            MinStat("charm", 30),
            ),
        PersonTarget(palla,
            Not(IsActivity("sleep")),
            HasRoomTag("pallahome"),
            IsFlag("addressknown", True),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "palla_repeat_naked_dogeza",
    "label": "palla_repeat_naked_dogeza",
    "conditions": [
        IsDone("palla_apartment_first_visit"),
        HeroTarget(
            IsGender("male"),
            IsRoom("pallalivingroom"),
            ),
        PersonTarget(palla,
            Not(IsActivity("sleep")),
            HasRoomTag("pallahome"),
            IsFlag("status", "sex slave"),
            IsFlag("palladelay", False),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

label palla_start:
    $ palla.unhide()
    return

label palla_event_02:
    "While I do my shopping, I hear a somewhat familiar voice."
    "Girl" "Hey, [hero.name], if you're here, you must have some taste, after all."
    show palla with dissolve
    "I can't quite place it, so I turn around, and Palla is standing there, looking over a few outfits."
    palla.say "Think you could do me a favor? This dress would work perfectly with the shoes I just got."
    palla.say "Since you and Audrey work together, I know you have the money to help a girl out."
    mike.say "Wait, are you, asking me to pay for your clothes for you?"
    show palla joke
    palla.say "What? Are you not a gentleman? I guess I could just tell Audrey what an ass you are, for not helping out a girl in need."
    show palla normal
    menu:
        "Pay" if hero.money >= 100:
            "Looking at the price, it's not that bad. And besides, getting on Palla's good side might actually be a bonus."
            mike.say "Who says I'm not a generous gentleman? Sure, I'll pay for you. Anything for a friend."
            palla.say "Oh, are we friends, now? I think I'll go change into this and see how it goes."
            palla.say "Just go over there and pay for it, but don't you dare go sneaking into the dressing room."
            palla.say "This place has terrible security, you know. No one would ever know."
            hide palla with moveoutright
            "She walks off towards the back and to the dressing rooms."
            "It's a quick transaction as I tell the cashier what I want."
            "She looks totally bored out of her mind and has her face buried in her phone."
            "Wow, Palla was right."
            "Security here is really lax, and even though I was so nice to her, she was still being a bitch."
            $ hero.money -= 100
            $ palla.flags.storepaid = True
            $ pay = True
        "Don't Pay":
            mike.say "What the hell? You want me to pay for your clothes?"
            palla.say "Of course, you are a gentleman, aren't you?"
            mike.say "That doesn't mean I'm going to give you free clothes, you cheapskate!"
            "Palla sighs and turns away from me, only to give me a glance over her shoulder for a narrow, smouldering eyes."
            palla.say "Well, I'm just going to the dressing room now, and take a look at myself in this dress."
            palla.say "You'd better not take advantage of the store's terrible security and follow me in there, you creep!"
            hide palla with moveoutright
            "With that, she storms off, leaving me dumbfounded for a moment. Did she... did she actually want me to go in?"
            $ pay = False
            $ palla.flags.storepaid = False
    menu:
        "Leave":
            "What the hell is that woman's deal?"
            "She's totally ruined my mood with her bitchiness."
            "Might as well head home."
            "There's no way I can think straight while she's around here..."
        "Go in":
            if pay:
                "Well, I've paid for the dress, right? I suppose its only fair I get to see her in it."
                "I slip casually away from the cashier and make my way to the dressing rooms, grabbing a random pair of pants along the way to avoid suspicion."
            else:
                "That uptight fashionista thinks she can get away with bossing me around, does she?"
                "Well, I've gone too high up the corporate ladder to be someone's lackey. Seems I need to teach her a lesson."
                "I storm off towards the dressing room, yanking off a random pair of pants, though my annoyance is probably clear to anyone who might be watching."
                "Here's hoping security is as bad as Palla claimed it was..."
            "Once inside, I can clearly see that there is only one unit occupied."
            "That's my target."
            show bg clothesshop at center, dark
            show palla underwear topless surprised at center, zoomAt (1.2, (640, 860))
            with fade
            "The door pushes open with no lock, and on the other side is Palla, staring wide-eyed at me, still wearing her glasses, but otherwise stripped down to stylish underwear."
            "She holds the dress up against her, as if trying to hide from me, yet drops it immediately."
            palla.say "W... what are you doing? You can't be in here!"
            mike.say "Are you complaining?"
            show palla angry
            palla.say "Of course I am, you ass!"
            mike.say "Then, go on, raise your voice if you don't want me in here."
            show palla annoyed blush
            "She stares at me a moment, her eyes catching onto my own. For a brief moment, she even bites her lip."
            palla.say "Don't you dare force me against the wall and fuck my ass, you sicko!"
            mike.say "Oh, alright, I guess I'll just leave, then."
            show palla surprised
            "Her eyes widen at that, her jaw dropping."
            palla.say "Hey, what are you-?"
            "I need to get rid of this frustration, and it seems she really wants me frustrated, so I grab her head and push her up against the mirror, her glasses sliding awkwardly off her face and her cheek squished against the glass."
            mike.say "Last chance to back out, if you don't really want this."
            show palla angry
            palla.say "Fuck you, asshole. Don't you dare do it!"
            show palla stand with fade
            "I unzip my pants with my free hand, and she stares at my reflection as I hold her down."
            "Obviously, she could push against me, fight back, and call for help."
            "I do everything I can to make sure I'm not really harming her."
            "She's a bitch, but I'm not a monster."
            "I could just as easily get my rocks off at home as with her."
            "No, I have to make sure she wants it."
            "It'll make it all the sweeter."
            "I let go of her head, and she holds onto the wall, not pushing away."
            "Her ass sticks out for me, and I take my now free hands and run them down along her sides, hooking my thumbs in the hem of her underwear, and I pull them down."
            "Already, there's a bit of sticky wetness on them."
            mike.say "And you're the one who called me an asshole."
            mike.say "You know, I'd love to fuck you right now, but you'd want that, wouldn't you?"
            mike.say "No, I think I'll take what you said you don't want."
            "She remains against the mirror as I grip her cheeks, pulling them apart, and giving myself a great view of her asshole."
            palla.say "Whatever you do... please, please, don't fuck my ass."
            "I then slide my cock over her, the head pressing against her tight hole."
            "Her eyes roll back, certainly not the signs of a woman who really didn't want this to happen, but I wasn't going to get rid of her illusion."
            "That only adds to the excitement as I spread her apart with my dick, thrusting into her and grunting with each little bit I go deeper into her."
            palla.say "Y-you call this assault? You're-You're not very good at this, are you!?"
            show palla stand wet
            "Her pussy drips with desire as my cock disappears into her ass with each thrust forward."
            "She stares, transfixed at the situation before her, and bites her lip as she watches, a deep blush going over her face."
            "She grunts with each thrust, her fingers curling against the mirror, nails scratching at the surface."
            palla.say "C... Come on... you you! Can! Do! More! Than! That!"
            "I pick up the pace as she taunts me, closing my eyes shut and gritting my teeth as I bury my face against her back."
            "I plow into her, and she smashes against the mirror again, our fucking thumping against the mirror, making the flimsy walls of the dressing room quake underneath of our rough ride."
            show palla stand wet ahegao with hpunch
            "She bites her lip as she holds back her groan of pleasure, and I feel the spasms around me as she reaches her climax."
            with hpunch
            "I too unleash into her, filling her with my cum."
            with hpunch
            "I pull out, and she dribbles down onto the floor, falling against the mirror and gasping for breath."
            show palla stand wet pleasure
            palla.say "F... fuck... [hero.name], you're an animal. But you'd better get out of here."
            "She pulls her pants up."
            palla.say "If they discover what we did, we won't be allowed back in the store...!"
            $ palla.flags.storeanal = True
            $ palla.flags.anal += 1
            $ palla.sub += 2
            $ palla.sexperience += 1
            call check_cheated ("groping", "palla") from _call_check_cheated_1
    $ palla.unhide()
    return

label palla_event_03:
    if palla.love.max < 10:
        $ palla.love.max = 10
    show palla normal casual glasses
    "When I walk in, I see Palla just stepping away from the counter, fresh coffee in hand. She looks at me and narrows her eyes."
    if palla.flags.storeanal:
        show palla angry
        palla.say "Hey asshole, we need to talk."
        "She looks angry, but there is also something else."
        mike.say "Fine."
        show palla b casual glasses annoyed at center, zoomAt(1.5, (640, 1140)) with fade
        "We walk over to a table and she sits across from me. I feign ignorance and put on my best poker face."
        mike.say "What do you want to talk about?"
        show palla a casual angry -glasses with dissolve
        palla.say "Don't give me that, asshole. You know what I want to talk about."
        if palla.flags.storepaid:
            mike.say "Um, you want to thank me for buying that dress?"
            show palla annoyed
            "Palla shifts a bit and actually looks a little flustered, but recovers herself."
            palla.say "No, I think you already got thanked for that. Asshole."
            "I think she smiled just a little as she said \"Asshole\"."
        mike.say "Ah, you want to talk about your asshole?"
        show palla blush
        palla.say "No! I mean, actually, kind of. What you did to it!"
        "I smile a little and lean forward."
        mike.say "Oh, you mean when I made you scream for more?"
        "I didn't think she could blush more, but she does. I actually think she's turned on just talking about it."
        palla.say "No! I mean, ugh, you're such a dick. You should apologize."
        menu:
            "Apologize":
                mike.say "You want me to apologize for giving you exactly what you asked for?"
                show palla angry
                palla.say "I didn't ask for it, and yes."
                "I sigh."
                mike.say "Fine. I'm sorry I fucked you in the ass. I promise I won't do it again. Unless you ask for it."
                show palla happy
                palla.say "See, that wasn't so bad!"
                "Is she serious? That was the weakest sarcastic apology I could think of."
                show palla wink at center, zoomAt(1.4, (640, 1000)) with move
                show palla normal at center, traveling (1.2, 0.5, (640, 840))
                "She blows me a kiss and leaves the table."
                hide palla with moveoutright
                $ palla.love += 3
            "Not a chance":
                mike.say "Not a chance, bitch! You had every opportunity. I made sure you wanted it, and trust me, you wanted it. I have nothing to apologize for. You're the one who should be apologizing to me!"
                show palla angry
                palla.say "Me, apologize to you? What the hell for?"
                mike.say "For not just asking for what you so obviously wanted!"
                "She leans over the table and points a finger at me, practically stabbing me in the nose with it."
                palla.say "If you ever do anything like that again, I'll, I'll..."
                mike.say "Again? Oh that sounds kind of fun."
                show palla blush
                "She is now completely speechless and blushing furiously."
                mike.say "Sorry I interrupted you. If I do this again, you'll do what now? Get on your knees and scream for more again?"
                show palla at center, zoomAt(1.4, (640, 1000)) with move
                show palla at center, traveling (1.2, 0.5, (640, 840))
                "Clearly at a loss for words, she gets up from the table and storms off, leaving her coffee behind."
                hide palla with moveoutright
                $ palla.sub += 3
    elif palla.flags.storepaid:
        palla.say "Hey [hero.name], let me pay you back for that dress."
        mike.say "Oh great, thanks! It was a hundred bucks."
        show palla blush
        palla.say "Oh that's not what I meant."
        mike.say "What did you mean, then?"
        show palla normal casual
        "Palla hesitates and then mumbles."
        show palla annoyed
        palla.say "Um, something else."
        "That was weird. And I guess she did kind of suggest she wanted me to follow her in, in a kind of \"Don't throw me in that briar patch\" kind of way. I decided to press and see."
        mike.say "What, like a blow job or something?"
        show palla blush
        "She sounds angry, but she doesn't {b}look{/b} angry. In fact she looks kind of turned on."
        palla.say "No! Eww no, gross! Nothing like that! I was thinking I'd let you buy me coffee."
        mike.say "I don't see how that's paying me back."
        show palla normal casual
        palla.say "Well, I'm a famous model, and you could be seen. With me."
        "She waves a hand at the substantial crowd."
        palla.say "They'd all think you're important."
        menu:
            "I'd rather get the BJ.":
                mike.say "Yeah no, pass. I'd rather have the BJ."
                show palla surprised
                if hero.grooming < 4:
                    palla.say "Ugh no! Gross! You smell like you haven't showered in a week!"
                    mike.say "Oh, is that all? What if I went and took a shower, right now?"
                    show palla annoyed
                    "She hesitates, just for a second."
                    palla.say "Uh, still no."
                    "She's really not convincing."
                else:
                    palla.say "Gross! No, I'm not a fucking whore!"
                    mike.say "Oh yeah? Is that why you practically begged me to follow you into the dressing room?"
                    show palla angry
                    palla.say "I told you {b}not{/b} to do that!"
                    mike.say "Yeah, and why would you tell me not to do that? It's not something you'd normally expect a random guy to do."
                    "Palla stammers."
                    mike.say "I bet if I'd followed you in I would have gotten a lot more than a blow job!"
                    show palla annoyed
                    palla.say "Ugh!"
                menu:
                    "What if I said please?":
                        mike.say "What if I said please?"
                        show palla annoyed
                        palla.say "Still no! Asshole!"
                        mike.say "Pretty please? With sugar on top?"
                        "She rolls her eyes."
                        palla.say "Oh fuck off already."
                        show palla at right with move
                        "And with that she heads to the exit, but strangely she doesn't really seem angry. She gives me a look over her shoulder as she walks out, and I swear she gave me a wink just as she turned away."
                        hide palla with moveoutright
                        $ palla.love += 3
                        $ palla.sub += 1
                    "Get on your knees, bitch!":
                        mike.say "Get down on your knees, bitch!"
                        show palla angry
                        palla.say "What?! Here, in public? Christ, you're a fucking asshole."
                        show palla at top_mostright with move
                        "She gets up and storms off, leaving her coffee. But just as she's at the doorway, she looks back over her shoulder and I swear she looked at me with a mix of hunger and hate in her eyes. Then she's gone."
                        mike.say "Serves that bitch right!"
                        hide palla with moveoutright
                        $ palla.love -= 1
                        $ palla.sub += 5
                    "Drop it":
                        mike.say "Fine, never mind. Are we done here?"
                        show palla sad
                        "She actually looks a mixture of embarrassed and disappointed. She mumbles something that sounds like half apology and half a curse, then gets up and leaves."
                        hide palla with moveoutright
                        $ palla.love += 1
                        $ palla.sub -= 5
                $ palla.flags.owesbj = True
            "I'd rather see more of the famous model.":
                mike.say "I'd rather see more of the famous model."
                palla.say "What do you mean?"
                mike.say "Ever done any nude modeling?"
                show palla angry
                palla.say "No! I do high fashion, catalog stuff, not pornography!"
                mike.say "Ahh, too bad. You're kind of hot, and that would totally make up for the dress."
                "She looks at me, a strange mix of intrigue and repulsion on her face."
                palla.say "So what you're saying is if I give you some nude pics, we're even?"
                mike.say "Sure!"
                show palla annoyed
                "Palla shifts around uncomfortably."
                palla.say "I don't know. Are you sure you wouldn't rather have the coffee with me?"
                menu:
                    "Nope!":
                        mike.say "Nah, the pics sound a whole lot better."
                        palla.say "Uh no, no I don't think so."
                        show palla at top_mostright with move
                        "Palla turns to leave. As she reaches the doorway she turns and looks back at me over her shoulder. When she sees me watching her, she turns away again, embarrassed. Then she's gone."
                        hide palla with moveoutright
                        $ palla.love += 2
                    "You could model in person instead, if you like":
                        mike.say "You could model in person instead, if you like!"
                        show palla angry
                        palla.say "Oh sure, first pictures, then you want me to model for you personally. Let me guess, at your place? And then what, you're going to ask to tie me up and fuck me in the ass?"
                        "Wow, where did THAT come from! She looks angry but that one came out of nowhere. Still, it sounds intriguing so I figure I ought to follow it up."
                        mike.say "Wow, that sounds hot! You'd do that? For a dress?"
                        show palla blush
                        palla.say "What? No I wasn't sugg...I mean I wasn't off...oh fuck."
                        "And then she turns and practically runs out of the store."
                        hide palla with moveoutright
                        $ palla.sub += 5
                $ palla.flags.owesnudie = True
            "Forget it":
                mike.say "Forget it, it's not necessary. And I'm not interested."
                show palla sad
                "Palla looks disappointed."
                palla.say "Fine."
                "And she leaves."
                hide palla with moveoutright
                $ palla.love -= 3
    else:
        palla.say "Hey [hero.name], sorry about the thing with the dress. Can I make it up to you?"
        mike.say "That depends, did you actually tell Audrey I'm an ass?"
        "She smiles a little bit, and I can't help but wonder what she's got up her sleeve."
        palla.say "Not yet, but the day isn't over."
        mike.say "Oh, so you're going to make it up to me by threatening me again? Or are you just going to call me a creep and maybe hope I follow you somewhere private and...I don't know what you expected."
        show palla surprised blush
        "Her eyes widen a little and she starts stammering."
        palla.say "No no no that's not what I--"
        "I can't help myself, but she just got so flustered I had to take a little pity on her. Just a little."
        mike.say "Relax, Palla. What did you have in mind, then?"
        show palla casual normal -blush
        "She takes a deep breath."
        palla.say "Well, I guess I thought I'd buy you a coffee and, um, you know, apologize."
        "I swear, it seems like she's two different people right now."
        "On one hand, she clearly has a high opinion of herself and a low opinion of nearly everyone around her. On the other hand, she's actually decided she wants to apologize to me over something I've frankly almost forgotten."
        mike.say "Apologize for which part? Threatening me or assuming I was going to follow you into the dressing room and try to get a look at you changing into that dress?"
        show palla angry
        palla.say "Hey! Don't be an ass!"
        mike.say "Or now you could be apologizing for calling me an ass?"
        "I honestly can't tell if she's angry or aroused right now, or maybe both."
        palla.say "Oh fuck, why am I bothering with the likes of you anyway?"
        "Damn but she knows how to get under my skin. Still, I try to project the calmest demeanor I can."
        mike.say "I don't know, Palla, why are you bothering with \"the likes of me\"?"
        show palla casual normal
        "She suddenly starts talking about a mile a minute, not even taking a breath between sentences."
        palla.say "I guess because Audrey won't stop going on and on about how awesome you are and I thought I'd see what it was all about and I thought I should see what she's going on about and I don't have many friends except Audrey--"
        palla.say "--and she's always talking about you and I hate it and oh you don't care about any of this and I'm really sorry I'm bothering you oh god damn it!"
        show palla at right4 with move
        "She turns to race off, but hesitates, just a second, leaving an opening."
        menu:
            "Grab her wrist and stop her":
                show palla angry at center, zoomAt(1.5, (640, 1040)) with hpunch
                "As she turns I grab her wrist, preventing her from easily taking more than a step. She turns and looks at me, anger in her eyes, but something else."
                "She tries to pull her wrist away, but I maintain a grip that isn't tight enough to hurt her, but will require her to pull pretty hard to get away."
                "She tugs a second time, but interestingly not actually all that hard. It has the effect of forcing her to step toward me, and suddenly she is very nearly pressed up against me. She's almost as tall as I am, and I end up looking directly into her angry green eyes."
                show palla angry
                palla.say "Let go of me, asshole!"
                show palla annoyed blush
                "She doesn't actually pull away again, instead just letting me hold her wrist, her nose a mere couple of inches away from mine. I lower my voice; we are in public, after all, and I don't want this to be a shouting match."
                mike.say "Now, hang on a second, lady. First you threaten me, call me a creep, then say you want to get to know me, and now I'm an asshole? Which is it?"
                "She lowers her voice too, and practically whispers."
                show palla normal
                palla.say "I...I...I just want you to let go of me."
                "I loosen my grip and let my fingers go slack, but don't actually remove them from her wrist, and then I wait to see what she does."
                show palla flirt
                palla.say "And don't you dare try anything. If you try to kiss me, I'll scream."
                "I look down at her lips. They're trembling. She moves her wrist and it's obvious she knows she can pull away at any time, but hasn't yet."
                "That was a dare. I want to, because this girl is hot and this whole angry act is getting me going. I'm not sure if I dare, though. We're in public. What if she really does scream?"
                menu:
                    "Kiss her":
                        hide palla
                        show palla kiss
                        with fade
                        $ palla.flags.kiss += 1
                        "I lean in--it's not too far, she's already right in my face--and touch my lips to hers. My whole body follows, and when her chest presses up against mine, her heart is beating so hard and so fast I can feel it up against me."
                        "Her only immediate response is for her eyes to first widen, then close. The rest of her body stiffens. I wrap my free hand around her waist and pull her fully against me."
                        "After a few more seconds, her lips part and our tongues meet. I tighten my grip on her wrist again and she makes a noise in the back of her throat."
                        "In just a few seconds, this whole thing has me so turned on that my dick starts to harden as our bodies press against each other."
                        hide palla
                        show palla angry at center, zoomAt(1.2, (640, 840))
                        with vpunch
                        "Then, suddenly, she pushes away. I wasn't holding very tightly, so she is easily able to escape my embrace."
                        palla.say "Don't ever do that again, you fucking asshole."
                        show palla at center, zoomAt(1.2, (940, 840)) with move
                        "She turns and heads toward the exit. As she passes through it, she throws me a look over her shoulder, her eyes smoldering. With rage? With desire? Some of both? It's hard to tell."
                        hide palla with moveoutright
                        "And with that, she's gone. I think maybe she wants me to follow her, but I don't think I want to play that game right here."
                        $ palla.love += 5
                        $ palla.sub += 5
                    "Don't kiss her":
                        mike.say "You keep telling me not to do things that I think you want me to do."
                        show palla blush
                        mike.say "But I don't think so, not here, not now anyway. Maybe another time, somewhere else."
                        show palla at center, zoomAt(1.2, (640, 840))
                        "Palla stammers and her wrist pulls easily out out of my loose grip."
                        palla.say "How dare...you fu...you creep! Asshole!"
                        mike.say "Don't forget dick, you haven't called me a dick yet. Or a bastard."
                        show palla angry
                        "For a minute, I actually think she's going to slap me, right there in front of the crowd. But she doesn't, she just scowls at me and, apparently having run out of nasty words for me, turns on her heel and leaves. She looks frustrated. Frankly, so am I."
                        hide palla with moveoutright
                        $ palla.sub += 2
                        $ palla.love += 2
            "Let her go":
                show palla at top_mostright with move
                "I just watch her leave, without saying anything. When she looks back I actually think she might have been crying a little, but it was just a quick glance. Maybe I was imagining it, but it makes me wonder if I did the right thing."
                hide palla with moveoutright
                $ palla.love -= 10

    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03a:
    if palla.love.max < 20:
        $ palla.love.max = 20
    show palla glasses blank
    "When I arrive, I see Palla standing in front of the coffee counter, giving the menu a disdainful look."
    show palla annoyed
    "Then she sees me and her disdainful look transfers from the menu to me. She gives me an absolutely withering glare."
    show palla normal
    "...and then she walks over to me."
    $ renpy.dynamic("name_mike")
    if hero.name.lower() not in ['mike', 'myke', 'michael', 'mychal']:
        $ name_mike = True
        palla.say "Hey there, Mike!"
        mike.say "Err. You talking to me?"
        palla.say "Yeah, am I looking at another Mike?"
        mike.say "But my name is [hero.name]!"
        palla.say "Sure, whatever, Mike. If you say so."
    else:
        $ name_mike = False
        palla.say "Hey there, Jeff!"
        mike.say "Err. You talking to me?"
        palla.say "Yeah, am I looking at another Jeff?"
        mike.say "But my name is [hero.name]!"
        palla.say "Sure, whatever, Jeff. If you say so."
    palla.say "Anyway, buy me a coffee, bitch!"
    menu:
        "Sure":
            mike.say "Sure, why not!"
            "I tell the server I'm getting her drink."
            show palla happy
            "And she buys the most expensive thing on the menu. Then she gives me her beautiful, model-hot smoldering smile."
            $ hero.money -= 10
            $ palla.flags.boughtcoffee = True
            if name_mike:
                palla.say "Thanks, Mike!"
            else:
                palla.say "Thanks, Jeff!"
            $ palla.love -= 10
            $ palla.sub -= 10
            "Then she takes her drink and wanders off."
            hide palla with moveoutright
        "Fuck off":
            mike.say "Fuck off! Why would I buy you a coffee with that attitude?"
            show palla joke
            palla.say "Because I'm a sexy, glamorous super model and you want to be on my good side."
            mike.say "Do you have a good side?"
            show palla b
            "She thrusts her chest out at me and points directly at her breasts."
            palla.say "Honey, every side of me is a good side, or at least that's what my photographer always says."
            palla.say "So anyway, you going to buy me a drink or what?"
            menu:
                "Fine":
                    "I tell the server I'm getting her drink."
                    show palla happy
                    "And she buys the most expensive thing on the menu. Then she gives me her beautiful, model-hot smoldering smile."
                    $ hero.money -= 10
                    $ palla.flags.boughtcoffee = True
                    palla.say "See? It's great to have a sexy model who likes you."
                    if name_mike:
                        palla.say "Thanks, Mike!"
                    else:
                        palla.say "Thanks, Jeff!"
                    $ palla.love -= 10
                    $ palla.sub -= 10
                    "Then she takes her drink and wanders off."
                    hide palla with moveoutright
                "No, fuck off":
                    mike.say "No, seriously, fuck off."
                    $ palla.sub += 2
                    show palla annoyed
                    palla.say "Well what fucking good are you, then?"
                    mike.say "Lots of good, but not with that attitude."
                    palla.say "Harrumph."
                    hide palla with moveoutright
                    "And then she leaves, without ever getting a drink."
        "Did you just call me bitch?":
            mike.say "Did you just call me {i}bitch{/i}?!"
            palla.say "Well, you made such a big deal about me calling you by your name."
            mike.say "My name is [hero.name]."
            palla.say "So?"
            mike.say "So if you want a coffee, you'll say my name and you'll ask nicely."
            show palla annoyed
            palla.say "Ugh, why are you such a tool?"
            mike.say "Do you want the coffee or not?"
            show palla angry
            palla.say "Fine. Buy me a coffee."
            mike.say "Yeah, not if you keep fucking with me like that."
            "Her lips purse and she gives me a pretty serious death glare. The words she utters are not spoken in any fashion you'd consider pleasant."
            palla.say "Will you buy me a coffee, [hero.name]?"
            mike.say "Oh so you do know my name. But I think it's missing one important thing."
            palla.say "What?"
            mike.say "Really? Are you five years old?"
            show palla joke
            palla.say "Not with these tits."
            mike.say "Palla...I'm waiting."
            show palla annoyed
            palla.say "Please. Fine. Please?"
            mike.say "Say it again!"
            show palla angry
            palla.say "Don't push your luck. That's all you get."
            "I ponder for a moment, trying to decide if that's enough."
            menu:
                "Yes, that was worth it":
                    mike.say "Very well."
                    "I tell the server I'm getting her drink."
                    show palla happy
                    "And she buys the most expensive thing on the menu. Then she gives me her beautiful, model-hot smoldering smile."
                    $ hero.money -= 10
                    $ palla.flags.boughtcoffee = True
                    palla.say "Thanks, [hero.name]!"
                    $ palla.love += 5
                    $ palla.sub += 5
                    hide palla with moveoutright
                    "Then she takes her drink and wanders off. I honestly don't know what to make of that."
                "No, not playing that game":
                    mike.say "No, that was much too forced. If you can't be nice I don't see why you deserve nice things from me."
                    show palla angry
                    if name_mike:
                        palla.say "Fuck you, Mike!"
                    else:
                        palla.say "Fuck you, Jeff!"
                    $ palla.love -= 10
                    $ palla.sub += 5
                    "Then she storms off."
                    hide palla with moveoutright
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03b:
    if palla.love.max < 30:
        $ palla.love.max = 30
    show palla glasses at left with dissolve
    "I see Palla rifling through racks of clothing, clearly not finding what she's looking for and getting frustrated."
    "When one particular piece appears to not be what she wants, she throws it across the store and then shouts."
    palla.say "Excuse me, miss!"
    show sasha at right with moveinright
    sasha.say "Yes, can I help you?"
    palla.say "Where are your Boréale Du Monde pieces?"
    sasha.say "Oh, I'm sorry ma'am, the Du Monde line isn't out yet."
    show palla annoyed
    palla.say "Not out? Ridiculous, it was supposed to be out this month."
    sasha.say "I don't know about that, but it wasn't in our catalog as of yesterday."
    palla.say "Ugh. Fine. When will it be out then?"
    sasha.say "I'm afraid I don't know."
    palla.say "Well, be useful dear, and go and fucking look!"
    show sasha angry
    sasha.say "Excuse me? What did you say?!"
    show palla angry
    palla.say "I said to do your job and go look up what your paying customer wants!"
    sasha.say "Oh like you pay for anything."
    "Either Palla didn't hear that, or she pretends not to; instead she turns back to the clothing rack and makes a dismissive gesture toward Sasha, who rolls her eyes and heads to the register."
    hide sasha
    show palla at center
    with moveoutright
    palla.say "I swear, the useless bitches they hire here. What fucking good is she anyway if she can't answer the simplest question?"
    "She continues muttering to herself under her breath, which I can't quite hear."
    show palla at left
    show sasha normal at right
    with moveinright
    sasha.say "I'm sorry, ma'am, but the computer doesn't have a date for that line."
    show palla annoyed
    palla.say "Oh for fuck's sake. I asked for something simple and that's all you got?"
    "I can see Sasha trying to hold her tongue and not rip this woman to shreds for disrespecting her."
    sasha.say "Would you like to look at the computer?"
    palla.say "No, I just want to know when I can get my fucking Boréale!"
    show sasha annoyed
    sasha.say "Look, I've tried to be polite, but if you're going to continue using that language here, I'm going to have to ask you to leave."
    palla.say "Me? You're going to kick {b}me{/b} out of the fucking store?"
    sasha.say "This is a family establishment!"
    "Somehow, they both see me at the same time."
    palla.say "[hero.name], will you please tell this bitch who I am?"
    sasha.say "[hero.name], would you do me a favor and escort this...woman...to the exit?"
    palla.say "Wait, you know him?!"
    sasha.say "Wait, you know him?!"
    menu:
        "Try to defuse the situation":
            mike.say "Ladies! Ladies, this is a public place. It's not a good place to fight."
            sasha.say "Yeah. If you take her outside I can kick her ass where I'm not at work!"
            palla.say "Oh like a twig like her has a chance!"
            show sasha angry
            sasha.say "Fuck off, whore!"
            show palla angry
            palla.say "{b}What{/b} did you call me?!"
            sasha.say "A whore. Which is what you are. You come in here, you never buy anything, but you act like you're our biggest customer!"
            palla.say "Well I fu--[hero.name], help a gal out here?"
            mike.say "How about this. Palla, how about I take you over to the coffee shop and buy you a drink. And we can let Sasha here get back to work?"
            palla.say "Oh fuck that, you can't buy me with a cup of fucking coffee!"
            $ palla.love -= 10
            $ palla.sub -= 5
            "And she spins around and marches right out."
            hide palla with moveoutleft
            show sasha at center with move
            mike.say "Well, that could've gone better."
            show sasha vangry
            sasha.say "Yeah, if you'd had any balls and just escorted her out like I asked we wouldn't still be standing here."
            $ sasha.love -= 4
            "And then she storms back over to the register."
            hide sasha with moveoutright
            "I should've just stayed out of it."
        "Escort Palla out":
            show palla angry
            mike.say "Palla, you're being a bitch. Let's go outside and get you cooled off."
            palla.say "What did you call me?"
            mike.say "A bitch, which you called Sasha like 3 times. She's been professional and nice and you just shit all over her."
            $ sasha.love += 5
            mike.say "Now come with me!"
            palla.say "Well I never! How dare you say that to me!"
            mike.say "Whatever. Let's go."
            "I step toward Palla and put one hand on her upper arm to escort her to the exit. For a moment it looks like she's going to slap me."
            show palla annoyed
            "But then she looks down at the floor and lets me walk her out."
            "When we get to the exit she yanks her arm out of my hand."
            palla.say "I'll remember this, [hero.name]!"
            mike.say "Oh yeah? Will it help you to be nicer to people?"
            show palla angry
            palla.say "Fuck off!"
            "And then she storms away."
            hide palla with moveoutleft
            $ palla.sub += 2
            $ palla.love += 2
        "Stay clear of this one":
            mike.say "Yeah, uh. You two leave me out of this!"
            show palla angry
            palla.say "You spineless piece of shit!"
            show sasha angry
            sasha.say "You worthless ape!"
            "And suddenly all of the anger they were directing at each other spewed forth at me."
            "They both hurled insults at me so fast and at the same time, I couldn't understand any of it."
            "And then after a few moments, as if in unison, they stormed off in different directions; Palla toward the exit, Sasha toward the register."
            hide palla with moveoutleft
            hide sasha with moveoutright
            $ palla.love -= 10
            $ palla.sub -= 10
            $ sasha.love -= 5
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03c:
    if palla.love.max < 40:
        $ palla.love.max = 40
    show palla annoyed
    "When I approach Palla, she's standing near the bar, giving the cute bartender her patented death glare. She holds a hand up to me, suggesting I should wait until she's done with the bartender."
    palla.say "What the fuck is this?"
    "Bartender" "Excuse me?"
    "Palla points at the bright blue drink on the bar in front of her."
    palla.say "Did I stutter? What. The. Fuck. Is. This?"
    "The cute bartender -- a petite blonde with a pixie cut -- looks pointedly at the drink, then back up at Palla. She speaks with a bit of a Southern drawl."
    "Bartender" "It's a Blue Hawaiian, like you ordered."
    palla.say "Yes, I ordered a Blue Hawaiian, but that's not what this is."
    "Bartender" "Maybe I made a mistake while mixing it. Would you like me to do it again?"
    show palla angry
    palla.say "Yes, I'd fucking like you to fucking make it again!"
    "The bartender sighs and makes a face that suggests she doesn't think she gets paid enough to deal with people like Palla. But she takes the drink back and starts mixing another one."
    "She grabs a couple of bottles and expertly mixes alcohol and juice together. Part way through, though, Palla interrupts her."
    palla.say "Wait, what the fuck is that?"
    "Bartender" "Uh, this? This is creme de coconut."
    palla.say "There's no creme de coconut in a Blue Hawaiian!"
    "Bartender" "Sure there is!"
    show palla annoyed
    palla.say "Honey, I've had Blue Hawaiians in Hawaii while watching buff guys swallow torches. There's no coconut in a Blue Hawaiian!"
    "Bartender" "Oh! You mean a Blue Hawaii."
    show palla angry
    palla.say "Yeah, that's what I said!"
    "Bartender" "No you--never mind."
    show palla normal
    "She sighs and turns to me, still standing next to Palla. She offers a tired smile."
    "Bartender" "Free drink? I think you'll need this if you're with her tonight."
    show palla angry
    "Palla turns her death glare on me."
    palla.say "Don't you dare take that disgusting drink."
    menu:
        "Free booze is free booze!":
            mike.say "Sure, hard to turn down a free drink! Thanks!"
            "As she pushes the drink toward me on the bar, she leans a bit -- not at all out of Palla's earshot -- and mock whispers."
            "Bartender" "Let me know if there's anything...else I can get you."
            "The bartender gives me a lewd wink."
            palla.say "Just shut up and make my damned drink right!"
            "I take the free drink and make a big show of enjoying it while Palla glares."
            $ palla.love += 2
            $ palla.sub += 1
            show palla annoyed
            palla.say "You are such a dick."
        "No thanks":
            mike.say "Ah, no thanks, blue drinks aren't my thing."
            $ palla.love -= 5
            $ palla.sub -= 5
            "The bartender shrugs, gives Palla a dark look, and then drinks half of it herself."
            palla.say "Are you going to drink all night or get me my damn drink?"
            "Bartender" "Hold your horses there, cowgirl. I'm on it."
    "After the bartender makes the replacement drink, she doesn't even wait for Palla to pick it up before disappearing. I don't blame her, really."
    show palla normal
    palla.say "I guess this will do. It's not the worst drink I've had, but it's not very good either."
    mike.say "Why do you have to be such a bitch to people over little stuff like that?"
    palla.say "Because if you give anyone an inch, they take a mile. If you let little things go, pretty soon they fuck up the big stuff."
    mike.say "That's a pretty dark outlook."
    show palla blank
    palla.say "I didn't ask you."
    mike.say "Fair enough."
    show palla wink
    palla.say "So you should buy me the next drink."
    mike.say "And why should I do that?"
    show palla joke
    "She holds up one finger and begins counting on them."
    palla.say "One, because I'm cute."
    palla.say "Two, because you like me."
    palla.say "Three, because you're a decent guy."
    show palla happy
    palla.say "Four, because I'm cute."
    menu:
        "You said cute twice":
            $ turnedon = False
            show palla blank
            mike.say "You said that one twice and yeah you're cute but you're not double cute."
            $ palla.love -= 2
            $ palla.sub -= 1
        "You're not as cute as the bartender":
            $ turnedon = True
            mike.say "You're not half as cute as that bartender was."
            $ palla.sub += 2
            show palla angry
            palla.say "Hey! You take that back!"
            mike.say "Now her, I'd buy her a drink if she asked."
            $ palla.love += 2
            show palla blank
            "Palla pouts a bit. She looks like she might actually be hurt."
            show palla normal
    mike.say "Also are you sure about two?"
    palla.say "Well, you're here talking to me, aren't you?"
    mike.say "For now."
    "She narrows her eyes."
    palla.say "Fine. Buy me a drink and I'll dance with you. Once! Just once."
    menu:
        "For a dance? Sure":
            mike.say "Okay, sure. For a dance, I'll buy you a drink."
            $ hero.money -= 10
            $ palla.flags.boughtdrink = True
            "I tell the bartender to put her next drink on my tab, and then Palla leads me to the dance floor."
            $ palla.flags.danced = True
            hide palla
            show dance palla
            with dissolve
            if turnedon:
                "And a bit to my surprise, she's a bit of an animal on the dance floor. I mean, I knew she had some moves, but I didn't realize how much."
                "She's really good -- fluid and precise, and her attention is 100%% focused on me -- it's an incredibly erotic experience!"
                if not hero.has_skill("dance"):
                    $ palla.love += 2
                    "Regrettably, my dance skills are nowhere near hers. When the song ends, her disappointment isn't subtle."
                else:
                    "When we're done, Palla is all smiles, and slightly out of breath. In fact, the look in her eye resembles that happy post-coital expression one gets after a really good shag."
                    $ palla.love += 5
                    $ palla.sub += 4
            else:
                "We go to dance, but Palla doesn't seem to be into it at all. She barely pays attention to me, instead focusing on the music and the other dancers."
                $ palla.love -= 2
            hide dance palla
            show palla
            with dissolve
        "You'll have to do more than that":
            mike.say "I think you'll have to do more than just dance with me."
            palla.say "Oh yeah? You want to go to the bathroom and get a blowjob? For a drink?"
            menu:
                "Yeah":
                    mike.say "Sure, why not? You've got a hell of a mouth on you, might as well put it to good use."
                    show palla happy at startle
                    "When you say something like that, you expect a girl to get mad. But instead she laughs."
                    palla.say "In your dreams."
                    $ palla.love += 5
                    if turnedon:
                        $ palla.sub += 4
                "No":
                    mike.say "Well, when you put it like that, no."
                    show palla annoyed
                    "Palla rolls her eyes."
                    palla.say "On second thought, I don't think I want a drink from you."
                    show palla normal
                    $ palla.love -= 5
                    $ palla.sub -= 10
        "I don't think so":
            mike.say "Yeah, I don't think I'm going to be buying you a drink."
            show palla sad
            "Palla pouts at me."
            palla.say "Why not?"
            menu:
                "Because you're being a bitch tonight":
                    mike.say "Because you're being a bitch tonight, and I'm not going to reward that behavior."
                    show palla blank
                    palla.say "What if I said please?"
                    mike.say "I don't think please is going to do it."
                    show palla joke
                    palla.say "What if I said pretty please, and promised not to be a bitch for the rest of the night?"
                    mike.say "Are you even capable of that?"
                    palla.say "I can be a good actress, when I want."
                    menu:
                        "Oh I've got to see this":
                            mike.say "Oh, I've got to see this. Can Palla manage to go all evening without being a bitch?"
                            show palla happy
                            palla.say "You'll see."
                            "Palla tries to call the bartender over, but the cute blonde completely ignores her until I put my hand up. And then she comes immediately."
                            "Bartender" "What can I get for you, darlin'?"
                            menu:
                                "Get her a Blue Hawaiian":
                                    mike.say "Get Palla here a Blue Hawaiian. On me."
                                    "Bartender" "But that's--"
                                    mike.say "I know."
                                    show palla angry
                                    "Palla shoots me a dark look."
                                    palla.say "Hey, th--"
                                    mike.say "You promised!"
                                    show palla blank
                                    palla.say "Fine."
                                    "She doesn't sound fine. The bartender, on the other hand, looks happier than I've seen her all night."
                                    "Bartender" "Coming right up, sweetheart!"
                                    mike.say "Now, when it gets here, I want you to drink the whole thing."
                                    show palla annoyed
                                    palla.say "But, ew, coconut!"
                                    mike.say "Or you'll just prove that you can't go even ten minutes without being a bitch."
                                    palla.say "You're such a fu--"
                                    "Then she catches herself. She pauses and forces a smile onto her face."
                                    show palla happy
                                    palla.say "Fucking generous dude, [hero.name]. That's what you are."
                                    "Watching her squirm for the next few minutes while she finishes the drink is totally worth it."
                                    "And because I'm not a total dick, I also get her the drink she actually wanted."
                                    $ palla.sub += 10
                                    $ palla.love += 10
                                    $ hero.money -= 20
                                    $ palla.flags.boughtdrink = True
                                    $ palla.flags.notabitch = True
                                "Get her a Blue Hawaii":
                                    mike.say "Get Palla here a Blue Hawaii. On me."
                                    show palla happy
                                    "Bartender" "Coming right up, sweetheart!"
                                    palla.say "Thanks for the drink!"
                                    $ palla.love += 2
                        "Still no":
                            mike.say "Still no."
                            palla.say "Well. What fun are you?"
                            if turnedon:
                                $ palla.love -= 10
                                $ palla.sub -= 5
                "Just don't feel like it":
                    mike.say "Honestly? I just don't feel like it."
                    palla.say "Ugh. Men."
                    $ palla.love -= 10
                    $ palla.sub -= 15
    hide palla
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03d:
    if palla.love.max < 50:
        $ palla.love.max = 50
    show palla glasses
    mike.say "Palla, can I buy you a drink?"
    if not palla.flags.boughtdrink and not palla.flags.boughtcoffee:
        palla.say "Oh sure, now you'll buy me a drink. Did I ask you?"
        mike.say "What, do you only want free drinks when you ask? How weird is that!"
        show palla blank
        "Palla furrows her brow, tilts her head and gives me a strange look."
        palla.say "Basically, yes. I only want things from you when I ask."
        mike.say "Fine, then I won't buy you a drink."
        show palla annoyed
        palla.say "Oh no, you don't get off that easy, pal. Buy me a drink."
        mike.say "You didn't ask."
        show palla wink
        palla.say "Good. I like a man who does what he's told."
        "I roll my eyes at her."
        mike.say "You know what, Palla, I think I'm tired of you being a bitch."
        show palla normal
        palla.say "Then why did you offer to buy me a drink, and then renege?"
        mike.say "For about fifteen seconds I forgot what a bitch you are."
        show palla annoyed
        palla.say "Huh. Fine."
        show palla normal
        palla.say "Would you please buy me that drink you so kindly offered?"
        mike.say "Well, since I did offer..."
    else:
        show palla joke
        palla.say "I like a man who knows to buy his favorite redhead a drink."
        mike.say "Who says you're my favorite redhead?"
        show palla wink
        palla.say "You didn't have to say it. I know I am."
        mike.say "You're pretty full of yourself."
        "Palla blows me a kiss. For a fleeting moment, I can't help but imagine those lips making that gesture on my cock."
    mike.say "So, Blue Hawaiian, then?"
    show palla angry
    palla.say "Now why do you have to fuck up something nice?"
    mike.say "Because I love the look on your face when you get that taste on your tongue. It makes me imagine you sucking my cock."
    show palla annoyed blush
    $ palla.sub += 1
    palla.say "Fuck off, [hero.name]. Maybe I don't want that drink after all."
    mike.say "Oh, relax! Get whatever you want!"
    show palla angry -blush
    palla.say "Not until you apologize."
    menu:
        "Apologize":
            show palla normal
            mike.say "I'm sorry, Palla. I was just teasing, I didn't mean anything by it."
            $ palla.love -= 10
            $ palla.sub -= 10
            palla.say "Well as apologies go I give it a 3 out of 10. You need to really learn to stick the landing."
        "I'll apologize when you stop being a bitch":
            mike.say "I'll tell you what. I'll apologize when you stop being a bitch."
            show palla normal
            if palla.flags.notabitch:
                palla.say "Oh, I see, we're going to play this game again."
            else:
                palla.say "I guess we're at an impasse then, because we both know that's not happening."
            mike.say "So do you want your free drink or do you just want to be a bitch?"
            "Palla seems to think about that for a moment."
            palla.say "Fine, free drinks are better than no drinks."
    hide palla
    show date pub burger palla
    with fade
    "Palla orders a Long Island Iced Tea. When it arrives, she watches me rather intently as she sips it."
    $ hero.money -= 10
    mike.say "What? Why are you looking at me like that?"
    palla.say "Like what?"
    mike.say "I don't know, was kind of thinking like a black widow spider about to eat something."
    if hero.fitness > 50:
        palla.say "Huh. Well, you do have a lot of muscle on you. You'd make good eating."
    else:
        palla.say "No way, you're way too scrawny."
    mike.say "I can't believe we're having this conversation."
    palla.say "What conversation should we be having?"
    mike.say "Can we have a normal conversation?"
    palla.say "Normal is boring. Most guys are boring. Don't be most guys."
    mike.say "What do you want, exactly?"
    palla.say "What do you mean?"
    mike.say "What do you want from me -- or I guess any guy, really -- exactly?"
    "Palla looks up at the ceiling and shrugs."
    palla.say "Someone more interesting than wallpaper paste, for a start. Which this line of questioning is starting to resemble."
    mike.say "That's it?"
    palla.say "Someone charming and handsome to buy me drinks?"
    mike.say "So I'm charming and handsome, is it?"
    palla.say "No, I was explaining what I {b}want{/b}. If you asked me what I think of you, you'd just call me a bitch again."
    mike.say "I just don't understand you. You're abusive to basically everyone for no good reason."
    palla.say "I think I have very good reasons."
    mike.say "And they are?"
    palla.say "Look, everyone sucks. Everyone is out to get whatever they can out of life. They'll use you if they can. They'll take every last thing they can get out of you and crush you if you don't like it."
    mike.say "Surely you don't mean everyone?"
    palla.say "Absolutely."
    mike.say "Even you?"
    palla.say "{b}Especially{/b} me, [hero.name]."
    mike.say "So there's no good in the world?"
    palla.say "What is good, exactly?"
    mike.say "People who do kind things because they like the feeling of kindness?"
    palla.say "That's just selfish people who've figured out they can get their own natural high by doing things. Those people suck the most."
    mike.say "Why, exactly, does anyone put up with you?"
    palla.say "You tell me, [hero.name]. Why do {b}you{/b} put up with me? Why exactly did you buy me this drink?"
    menu:
        "Maybe I just want to fuck your ass again" if palla.flags.storeanal:
            mike.say "Well. I did fuck you in the ass before, I want to know how many drinks it'll take to do that again."
            hide date pub burger
            show palla glasses blush
            with fade
            $ palla.sub += 2
            palla.say "There isn't enough alcohol in this place to get that to happen, dickface."
            show palla normal
        "Watching you be a bitch is better than TV":
            mike.say "The fireworks display whenever you're a bitch to people is more interesting than whatever trash is passing for TV these days."
            palla.say "I always wanted to be on TV."
            mike.say "Well, you've got an audience of one."
            $ palla.love += 3
            palla.say "I wonder if that'd sell. I should pitch it to my agent."
        "I kind of like you":
            mike.say "I don't know, I kind of like you. Not sure why. And it's what guys do when they like a girl?"
            $ palla.love -= 10
            $ palla.sub -= 10
            palla.say "Ugh. Don't be normal. Don't be boring. I don't have time for boring."
        "I was bored":
            mike.say "I was bored."
            palla.say "So you thought I'd liven up your evening?"
            mike.say "Basically, yeah."
            palla.say "Did it work?"
            mike.say "Jury's still out on that one."
            "Palla looks at the half-finished drink in her hand, and one corner of her lip slowly curls up."
            "Without further warning, she tosses the contents of her glass right at my face. I'm awash with the smell of liquor and the chill of half-melted ice cubes."
            hide date pub burger
            show palla glasses happy
            mike.say "What the fuck was that for?"
            palla.say "How about now? Did I liven up your evening?"
            mike.say "Oh fuck {b}off!{/b}"
            "Palla laughs merrily."
            palla.say "Well. Sure livened up mine!"
            $ palla.love += 5
            $ palla.sub -= 2
    $ hero.replace_activity()
    hide date pub burger palla
    hide palla
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03e:
    if palla.love.max < 60:
        $ palla.love.max = 60
    show palla glasses
    mike.say "Palla, can I buy you another drink?"
    show palla annoyed
    palla.say "Will you get all pissy again if I say no?"
    mike.say "Fine, your loss."
    show palla normal
    palla.say "Hey! I didn't say no. It was just a hypothetical."
    mike.say "Yeah, you're a real student of philosophy. Do you want the drink or not?"
    if palla.sub >= 50:
        palla.say "Sure."
    else:
        show palla joke
        palla.say "You need to kiss my ass more."
        menu:
            "Stop being a bitch":
                mike.say "You're the one getting the free drink. You need to kiss {b}my{/b} ass. Now stop being a bitch and take the damn drink."
                $ palla.sub += 3
                palla.say "Yeah, like I thought, pissy if I say no. Dick."
                mike.say "Why do I put up with you again?"
                $ palla.love += 1
            "Please take the drink":
                mike.say "Just please take the drink."
                $ palla.sub -= 10
                $ palla.love -= 10
                palla.say "Sure. Whatever. It's a free drink I guess."
    hide palla
    show date pub burger palla
    with fade
    "While we enjoy our drink, Palla seems uncharacteristically moody. It's not that being moody is unusual for her, but she's usually not quiet."
    mike.say "Something wrong, Palla?"
    palla.say "Oh. Just, I've been thinking about something. About you."
    mike.say "You? You think about me? Should I be flattered or preparing my will?"
    palla.say "Both."
    mike.say "So you going to spill or just leave that so I wonder what the fuck you're on about for the rest of the night?"

    $ girlfriends = hero.get_girlfriends()
    if len(girlfriends) == 0:
        $ girlfriends = hero.get_partners()

    if len(girlfriends) == 0:
        palla.say "[hero.name], why don't you have a girlfriend?"
        if hero.fitness > 60 and hero.knowledge > 60:
            palla.say "Aside from being an utter asshole, you're charming, smart, and handsome."
        elif hero.fitness > 60:
            palla.say "Aside from being an utter asshole, you're charming and handsome."
        elif hero.knowledge > 60:
            palla.say "Aside from being an utter asshole, you're smart and charming."
        else:
            palla.say "You're charming, even when you're being an asshole."
        menu:
            "I'm holding out for you":
                mike.say "I'm holding out for you, Palla."
                $ palla.love -= 10
                $ palla.sub -= 5
                "Palla spits her drink all over the counter, incidentally getting some of it on me."
                palla.say "You've got to be fucking kidding me. Are you really hung up on me? I'm sure there's a dozen girls who'd fuck you at the drop of a hat."
                if palla.flags.storeanal:
                    mike.say "And you were one of them."
                    palla.say "Not like that! Creep!"
                    palla.say "And I promise you you're not getting between my legs again any time soon."
                else:
                    palla.say "And I promise you you're not getting between my legs any time soon."
                mike.say "Oh yeah? What would it take?"
                palla.say "I tell you what, [hero.name]. You, bound with your hands behind you, on your knees, blindfolded. Maybe I'd let you lick me out."
                menu:
                    "Sounds fun":
                        mike.say "Sounds like fun. I bet you taste like honey."
                        $ palla.love -= 10
                        $ palla.sub -= 20
                        palla.say "I taste like vinegar with a side of piss. You'll love it."
                    "Other way around":
                        mike.say "That's the right idea, but reverse the positions. You on your knees. Bound. But no blindfold, I want to look in your eyes while you choke on my cock."
                        $ palla.love += 10
                        $ palla.sub += 10
                        palla.say "In your dreams, dickwad."
                        mike.say "My dreams? I'm pretty sure you're going to be dreaming about that tonight. I hope the orgasm you get is good."
                        "Her cheeks turn bright pink and she looks down at the bar."
                        palla.say "I don't think this abuse was worth a free drink."
                        mike.say "Totally worth it for me."
                        palla.say "Yeah, fuck off."
                        "Then she gets up and leaves the remains of her drink behind."
            "The right girl hasn't come along yet":
                mike.say "The right girl hasn't come along yet. So I'm just waiting."
                palla.say "Oh yeah? What's the right girl like?"
                menu:
                    "Describe Palla":
                        mike.say "She has to be beautiful, of course, and know how to use it. She'd be strong-willed, speak her mind when it suits her. I prefer my women with a bit of an edge. And a challenge."
                        "Palla looks more and more uncomfortable as I describe her traits."
                        $ palla.love += 4
                        $ palla.sub -= 10
                        palla.say "So what you're saying is you're a useless tool and you're never going to get anyone because a girl like that wouldn't put up with you being such a boring dickface."
                        mike.say "Could be. I might be destined to die, alone and unloved. Forgotten by society. Just like you!"
                        palla.say "Oh honey, I'm a star. I'll be remembered forever. And I'll piss on your grave."
                    "Describe opposite of Palla":
                        mike.say "I like petite women with dark hair and dark skin. I like a girl who knows her place, is kind and generous with a lot of empathy. Someone sweet who will make a good mother."
                        $ palla.love -= 4
                        $ palla.sub += 5
                        palla.say "That doesn't exist. I guess you're just shit out of luck. Do you have a backup plan?"
                        if palla.flags.storeanal:
                            mike.say "Just fucking random bitches in the changing room."
                            palla.say "Well you're certainly pretty good at that, I guess."
                        else:
                            mike.say "I guess I'll see what happens."
                        "Palla gets up and steps away from the bar."
                        palla.say "Well, let me know what you find. I can't wait to see who you end up with."
    else:

        if "bree_event_07b" in DONE:
            $ girlfriends = girlfriends.intersection({"sasha", "bree", "hanna", "audrey"})
        else:
            $ girlfriends = girlfriends.intersection({"sasha", "hanna", "audrey"})
        if len(girlfriends) == 0:
            palla.say "So what's up with you and, um, what's her name?"
            mike.say "Pardon?"
            palla.say "You know, that girl you're banging. I don't know her name. She's cute, at least. So good for you."
            mike.say "Ah, uh. I don't think that's your business."
            palla.say "No? And here you are, buying a sexy model drinks in a cheap pub. Are you cheating on her?"
            mike.say "We're just having a drink!"
            if palla.flags.storeanal:
                palla.say "Were you cheating on her when you fucked my ass in the mall?"
                mike.say "Holy shit, Palla, we're in public, you want to talk about that here?"
                palla.say "Cat's out of the bag now, I guess. Can't unscrew a bitch like me."
                mike.say "No, it wasn't cheating."
                palla.say "No? Because that really seems like cheating to me."
                mike.say "You wouldn't understand."
            palla.say "Would you let me watch you fuck her?"
            mike.say "No! Why would you even ask such a thing."
            palla.say "She's cute! I think the two of you would make good porn."
            mike.say "I, uh. No, no, that's not okay."
            palla.say "If you let me watch I might, maybe. Well, I'd let you watch her eat me out. What do you say?"
            mike.say "You're fucked up, Palla."
            palla.say "There was never any question about that."
            palla.say "So, can I watch?"
            menu:
                "No":
                    mike.say "No. And don't ask anymore."
                    $ palla.love += 4
                    $ palla.sub += 2
                    palla.say "Shame! You're suck a boring jerk."
                "Yes":
                    mike.say "Oh fine. She'd think it's hot anyway. So when do you want to do it?"
                    $ palla.love -= 10
                    $ palla.sub -= 10
                    palla.say "Awesome! I'll see when I can squeeze you in. To my calendar, I mean."
                    mike.say "Uh huh. How about tonight?"
                    palla.say "Have to work."
                    mike.say "At night?"
                    palla.say "Modelling isn't a nine to five job, [hero.name]."
                    mike.say "Sure. Tomorrow then?"
                    palla.say "I'll check my calendar and get back to you."
                    mike.say "Uh huh."
                    palla.say "Anyway..."
        else:
            $ renpy.dynamic("gf")
            $ gf = randchoice(list(girlfriends))
            if gf == 'sasha':
                palla.say "So what's up with you and the clothing store girl, anyway?"
                mike.say "Who?"
                if sasha.flags.haircut:
                    palla.say "I don't know her name. Skinny blonde, bad attempt at being goth? Acts like the bad girl but isn't?"
                else:
                    palla.say "I don't know her name. Skinny brunette, bad attempt at being goth? Acts like the bad girl but isn't?"
                mike.say "Do you mean Sasha?"
                palla.say "Is that her name? I only know her as \"Hey you!\""
                mike.say "Well that's not very nice."
                palla.say "Who cares? She's just there to ring up my orders. She doesn't know shit about the clothes. No one there does."
                mike.say "I see."
                palla.say "Anyway, you're banging her, right?"
                mike.say "Why do you care?"
                palla.say "Because you can do better than that stupid waif."
                mike.say "Waif?! Who says that?"
                if not sasha.flags.boobjob:
                    palla.say "Well, what else do you call a skinny, chestless bitch like that?"
                else:
                    palla.say "Well, what else do you call a skinny, fake chest bitch like that?"
                mike.say "I think she's cute."
                palla.say "You'd better, I'd hate to think you were fucking someone you thought was gross. You're better than that."
                mike.say "I feel like you just insulted me and complimented me at the same time. My head's spinning."
                palla.say "So what do you see in her?"
                mike.say "She's got good style!"
                palla.say "That fake goth punk shit she wears? That's not style, that's hand-me-down fashion from the 1970's. They want it back."
                mike.say "She makes good music!"
                palla.say "Music? You give a crap about that?"
                mike.say "What do you want to hear, Palla?"
                palla.say "Tell me you're in love with her."
                mike.say "Why?"
                palla.say "Because if you're not in love with her, you're with the wrong girl."
                menu:
                    "I'm in love with her":
                        mike.say "I love her, Palla. Is that what you want?"
                        $ palla.love -= 10
                        $ palla.sub += 5
                        palla.say "I guess. She's going to hurt you. You know that, right?"
                        mike.say "Why do you say that?"
                        palla.say "That's her type. You think she's sweet and one day she'll snap and tear your balls off."
                        mike.say "Are we talking about you or her?"
                        palla.say "Her!"
                        mike.say "Between the two of you, snapping and ripping off a man's testicles seems more your thing, Palla."
                        palla.say "Hmm. You may be right. Still. She's wrong for you."
                    "I don't love her":
                        mike.say "No, I'm not in love with her."
                        palla.say "You should let her go. You're just going to hurt her."
                        mike.say "That's not your concern."
                        palla.say "So you're just leading her on? Letting her think you're the one, and going to dump her when you get a girl with bigger tits?"
                        mike.say "Hey! I didn't say that!"
                        palla.say "You didn't have to. All men are like that."
                        mike.say "I have no problem with her chest size."
                        if not sasha.flags.boobjob:
                            palla.say "Really? You actually like those tiny boobs? Ugh, I thought you had taste."
                        else:
                            palla.say "Really? You actually like those fake boobs? Ugh, I thought you had taste."
                        mike.say "Obviously I have no taste, I'm sitting here having a drink with {b}you{/b}!"
                palla.say "I bet the sex is good, though. Does she let you tie her up?"
                if sasha.is_sex_slave:
                    mike.say "What if she does?"
                else:
                    mike.say "Why would I tell you that?!"
                palla.say "Oh, I bet she does! I can picture it now, her up against the wall, your cock in her ass. A big ol' ball gag in her mouth! Okay that's hot."
                mike.say "And you call {b}me{/b} a creep."
                palla.say "I'd let her lick my cunt like that."
                mike.say "With a ballgag? How would that work?"
                palla.say "Well you'd take it out of her mouth, of course. Duh. And here I thought you were smart."
                "Palla offers a wink as she gets up."
            elif gf == 'bree':
                palla.say "So what's with you and the blonde bimbo?"
                mike.say "Who?"
                palla.say "You know, long curly hair, big boobs that are probably fake. Acts all sweet and innocent."
                palla.say "Works at that sexy cafe in the city! She calls me Mistress when I get a coffee."
                palla.say "I was wondering how far that act goes. Could I get her to go down on me?"
                palla.say "Ohh, does she go down on you there?"
                if "bree_event_08b" in DONE:
                    mike.say "I'm not saying!"
                else:
                    mike.say "No!"
                palla.say "I hope so! The best use for a bitch like that is to get down on her knees and take it all over her face."
                mike.say "Palla!"
                palla.say "Is this turning you on as much as it is me?"
                mike.say "No!"
                palla.say "Let's go! I'll let you fuck me, right there, if she licks the cum out afterward."
                mike.say "Holy shit, Palla, you're nuts!"
                palla.say "No? You don't think that's hot?"
                mike.say "It doesn't matter, they're closed."
                palla.say "Fine, when do they open? I'll meet you there."
                "There's no way she's serious. She's just fucking with me. She has to be."
                menu:
                    "They open at 9":
                        mike.say "They open at 9, but [bree.name] works lunch and after school. Meet you there at noon?"
                        $ palla.love -= 5
                        $ palla.sub -= 5
                        "Palla laughs merrily."
                        palla.say "Nice try, but I'm not as easy as your blonde bimbo."
                        mike.say "Seriously, fuck you, Palla."
                        "Palla offers a wink as she gets up."
                    "Okay you've had your fun":
                        mike.say "Okay, you've had your fun. But if we ever did something like that, you'd be the one on your knees."
                        mike.say "Licking my cum out of her cunt. Like I'd let you do that to her!"
                        $ palla.love += 5
                        $ palla.sub += 5
                        palla.say "Hot, but I'm not getting on my knees for anyone. Not you and definitely not a bimbo like that."
                        "She makes a disgusted noise and pushes away from the bar."
            elif gf == 'hanna':
                palla.say "Hey, so you and the gym girl, eh?"
                mike.say "What do you mean?"
                palla.say "Hanna, is that her name? Well built. Her boobs probably aren't real but her muscles are!"
                palla.say "How is she in bed?"
                mike.say "What the fuck, Palla? Do you always just ask about shit like that? It's personal!"
                palla.say "Oh. I was thinking of hitting on her. I haven't had a girlfriend in awhile, and I think she'd be fun."
                palla.say "Is she fun?"
                mike.say "None of your business!"
                palla.say "I guess I'll just have to find out for myself."
                mike.say "Oh no you won't!"
                palla.say "No? Maybe you could let me borrow her."
                if hanna.is_sex_slave:
                    mike.say "No, you can't borrow her."
                    palla.say "Oh, so you {b}do{/b} have that kind of relationship! Do you do it in the gym showers?"
                else:
                    mike.say "That's not my call, and ew!"
                    palla.say "Do you do it in the gym showers?"
                mike.say "We might, but that's none of your business!"


                $ palla.flags.hannapeek = True
                palla.say "Well, sport, I have a new hobby now!"
                mike.say "You're sick, Palla."
                palla.say "The word you're looking for is hot. Don't deny it, I know every guy has the two girl fantasy."
                palla.say "And I think I'm going to go and imagine that for a bit."
            else:
                palla.say "I'm glad you're with Audrey."
                mike.say "Oh, uh. I didn't realize you--"
                palla.say "Oh yeah, she told me all about you. Well, almost. Do you choke her when you fuck her?"
                menu:
                    "Yeah, she likes it":
                        $ palla.love += 2
                        $ palla.sub += 2
                        mike.say "I guess since she already told you--yeah, she really gets off on it."
                        palla.say "I know! She's the kinkiest bitch I've ever met. Sometimes I wish I could be her, but I'd probably just end up getting myself killed by some asshole."
                        mike.say "Nah, she's not that bad."
                        palla.say "You don't know the half of it."
                        mike.say "Do tell!"
                        palla.say "Ah, no, that's her business. I shouldn't have mentioned it. Anyway, I'm glad she's got a guy who won't kill her."
                        mike.say "Uh, yeah, okay."
                        palla.say "And absolutely, positively, don't think about me the next time you fuck her."
                    "Not your business":
                        mike.say "That's really none of your business, Palla. If she didn't tell you, I'm not going to!"
                        $ palla.love -= 2
                        $ palla.sub -= 2
                        "Palla pouts."
                        palla.say "You're no fun. I was totally going to go home and masturbate, thinking about you and her."
                        mike.say "You do you. So to speak."
                        palla.say "Yeah. I will. Nobody does me as well as me."
                    "Palla stands up and gives me a wink as she steps away from the bar."
    hide date pub burger palla
    show palla glasses
    with fade
    palla.say "Thanks for the drink!"
    hide palla
    $ hero.replace_activity()
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03f:
    if palla.love.max < 70:
        $ palla.love.max = 70
    show palla
    mike.say "Hey Palla, want to train together?"
    show palla annoyed
    palla.say "Whyever would I want to train with you?"
    mike.say "Because it's more fun than working out by yourself."
    palla.say "That's debatable. I can barely stand to smell you on a good day. And all sweaty in a gym like this?"
    mike.say "What do you mean? I don't smell!"
    show palla joke
    "Palla makes a big show of inhaling through her nose."
    if hero.grooming < 8:
        show palla annoyed
        palla.say "You smell like you just spent three days in the woods and then bathed in a backed up sewer."
        mike.say "You're full of shit."
        palla.say "You {b}smell{/b} like you're full of shit."
        "I sigh."
        mike.say "Would it help if I showered?"
        palla.say "Probably."
        mike.say "Fine, I'll go shower."
        palla.say "No guarantees I'll still be here."
        "I roll my eyes."
        $ hero.cancel_activity()
        $ hero.cancel_event()
        return
    palla.say "You smell like a rabbit cage that hasn't been cleaned in a month."
    mike.say "How do you even know what that smells like? I know you don't have any pets, they'd kill themselves just to get away from you."
    show palla joke
    palla.say "Oh, hey, nice one."
    show palla normal
    palla.say "Fine. But you'll do what I say."
    menu:
        "What do you have in mind?":
            mike.say "Sure, what do you have in mind?"
            $ palla.love -= 6
            $ palla.sub -= 4
            palla.say "I do mostly cardio. So the elliptical, then the treadmill, then a nice run on the rowing machine."
            mike.say "Not much point in doing that together."
            palla.say "I did warn you."
            mike.say "Fine."
            "When we step over to the machines, Palla gets on a machine directly behind me."
            hide palla
            "Which means while I run on the machine, I don't even get to look at her."
            palla.say "Yeah, that's it. You'd better run."
            "Then she's quiet and we do the rest of our workout more or less in silence."
        "Not a chance":
            mike.say "Not a chance, bitch. Today we're doing an upper body set."
            palla.say "Well, someone's a demanding shithead today."
            $ palla.love += 2
            $ palla.sub += 2
            mike.say "You're demanding every day."
            "Palla rolls her eyes, but doesn't argue. We set up for some basic machine presses, Palla first."
            "She lays down on the machine and puts her hands on the press bars, ready to push them up."
            mike.say "How much weight do you usually do on this thing?"
            menu:
                "Set the weight where she says":
                    "I set the weight where she asks, and I count out three sets of ten for her."
                "Set the weight really high":
                    "I add twenty pounds to the weight she says. When she tries to do her set, she can only do three before she's straining, and after five she can't do any more."
                    $ palla.love -= 10
                    $ palla.sub -= 2
                    show palla angry
                    palla.say "Fuck, [hero.name], are you deaf or are you trying to kill me?"
                    mike.say "Oh, my mistake!"
                    show palla normal
                "Set the weight a little high":
                    "I add ten pounds to the weight she says. I count out three sets of ten, and by the time she's done she's huffing, puffing and seriously red."
                    palla.say "Damn, those aren't usually that hard."
                    $ palla.sub += 1
            palla.say "Now, your turn!"
            "We switch positions, and Palla sets the weight without even asking. When I look over, it's set a little high for me."
            "I get started on my set without saying anything, and Palla counts."
            palla.say "1... 2... 3..."
            show palla at zoomAt(1.5, (640, 1140)) with vpunch
            "After the third one, she sits right on my crotch. With the extra weight already on, I have to buck my hips up a little with each lift."
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            palla.say "4... 5... 6..."
            if palla.flags.storeanal:
                "With her pressing down against me, my mind drifts off to our encounter in the changing room."
            "The feel of her ass up against me gives me a bit of a boner."
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            palla.say "6... 7... 8..."
            mike.say "Hey, you did six twice."
            palla.say "I always do six twice! Besides, I thought you liked a lot of six? 9 and 10!"
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            show palla at zoomAt(1.5, (640, 1040)) with vpunch
            show palla at zoomAt(1.5, (640, 1140)) with move
            "When I finish the eleventh press, Palla just sits there looking down at me."
            mike.say "What?"
            palla.say "Oh, just noticing you seem to be enjoying yourself more than usual."
            mike.say "Gee, I wonder why."
            "She wiggles her butt for emphasis."
            palla.say "Next set!"
            "I start my lifts again and she starts counting. About halfway through, where it starts getting really rough with the extra weight both on my arms and on my lap, she leans down a bit."
            if "hanna" in hero.get_partners():
                palla.say "Do you think Hanna is watching us? Do you think she'll be jealous?"
                mike.say "Hey! Fuck off!"
                palla.say "After this I hope you go fuck her in the shower and think about me!"
            else:
                palla.say "I hope you're enjoying this, because this is all of my booty you're ever going to get!"
                mike.say "Like I want your booty."
                palla.say "Oh. I'm hurt. Really. Deeply."
                "Then she shifts and slides her ass across my stiff cock, rather hard. I'm caught by surprise and the press bar slips out of my hands. The machine's weights slam back together."
            hide palla
            show palla happy
            "Palla giggles when she stands up."
            palla.say "You were right, this was fun. We should do this again sometime."
            palla.say "Thanks for the workout!"

    $ bonus = 1
    $ hero.fitness += 1
    $ hero.fun += 2
    if hero.fitness >= 75:
        $ bonus += 1
    $ palla.love += bonus

    hide palla
    $ hero.replace_activity()
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_03g:
    if palla.love.max < 80:
        $ palla.love.max = 80
    show palla annoyed
    "When I approach Palla, she's sitting at one of the small tables, speaking angrily into her phone. And she doesn't sound happy."
    palla.say "...and fuck your mother too!"
    "Palla throws her phone down onto the table. Somehow, she doesn't shatter the glass. Then she looks up at me."
    show palla angry
    palla.say "What the fuck do you want?"
    mike.say "Is this a bad time?"
    palla.say "What does it look like, genius? Yes it's a bad fucking time!"
    mike.say "Need someone to talk to?"
    palla.say "No, I don't! Or if I did, it wouldn't be your smelly ass. Christ, [hero.name], who do you think you are?"
    menu:
        "Have it your way":
            mike.say "Have it your way."
            "I turn to walk away, and after only a few seconds she calls over to me."
            palla.say "Fine, fine, you can sit. Happy?"
            mike.say "No, no, please, don't let me put you out."
            palla.say "Just fucking sit already. You got me to change my mind, take the win before I throw up on you."
            $ palla.love -= 2
            "I sit down at her table."
        "Sit down anyway":
            "I think about it for a moment, and I sit down anyway."
            palla.say "I said I didn't want to talk."
            mike.say "Fine, don't talk. Or do. Or leave, the door's over there. But I'm going to sit here and have a coffee."
            palla.say "What the fuck? This is my table. Get your own."
            "I shrug and make a show of pulling out my phone."
            mike.say "I'm here if you want to talk, but otherwise feel free to ignore me."
            $ palla.love += 2
            $ palla.sub += 2
    "Palla picks up her phone and stares at it blankly for a few minutes. She doesn't actually interact with it, and after a moment, the fire in her eyes dies down to something like normal."
    show palla annoyed
    palla.say "Oh fuck, [hero.name]. I know I'm going to regret this, but can I ask your advice?"
    mike.say "Of course."
    show palla normal
    "Palla takes a deep breath."
    palla.say "My agent, he uh. Ugh. Sorry, it makes me sick to think about it. But there's this gig he wants me to take."
    palla.say "Really, demanded I take, and well, you know I don't really like that."
    mike.say "So don't take it."
    palla.say "He says if I don't...well, he thinks if I don't take the gig it'll make it harder for me to get other gigs."
    mike.say "Ahh. So take it."
    palla.say "The thing is, I have to take my top off for it."
    mike.say "So?"
    palla.say "So I don't do that! It's in my contract. I do high fashion, crap like that. I'm not a nude model."
    mike.say "What's wrong with nude modelling?"
    palla.say "Nothing! It's just that once you do that, you always do that."
    mike.say "Ahh."
    show palla sad
    palla.say "So I don't know what to do."
    menu:
        "Take the job":
            mike.say "You should take the job."
            palla.say "Why?"
            mike.say "Because you don't want to make it harder to get jobs, right?"
            mike.say "Besides, it'd be hot."
            show palla angry
            if palla.flags.owesnudie:
                palla.say "Oh, I see. You just think I should take it because you asked for nude pictures once and you're still on that aren't you?"
            else:
                palla.say "Oh, I see. You just think I should take it because you're hoping to see the pictures."
            palla.say "In your {b}dreams{/b} pal. You're not getting these."
            palla.say "And I'm {b}not{/b} taking the gig."
            "She gets up from the table, knocking over her chair in the process. Then she walks to the other side of the room."
            mike.say "Why did you even ask me then?"
            "But she makes a show of ignoring me. Instead, she pulls out her phone and calls someone. Sigh. She can be such a bitch sometimes."
            $ palla.love -= 10
            $ palla.sub += 1
        "Stick to your principles":
            mike.say "Stick to your principles, then. Don't take the gig. You're the famous model, right? Plenty of jobs will come along."
            show palla normal
            palla.say "Yeah."
            "Palla leans back in her chair, watching me."
            show palla happy
            palla.say "You're right. Thanks. I feel better about it. I'll call him right now."
            $ palla.love += 4
    hide palla
    "Palla pulls her phone out and calls someone, presumably her agent. Everyone in the shop can hear the colorful words she uses as she tells him exactly where he can stick that gig."
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_event_04:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    "My phone goes off, very much to my surprise. I look at the caller ID, and it's Palla. What could she want at this time of night? I'm not sure if it's a good idea or not, but I decide to answer it."
    mike.say "Hey, Palla. What's up?"
    palla.say "Hey [hero.name], I want to go to the club and dance with someone. Take me."
    "Wow, she's got some nerve, bossing me around like that! And in the middle of the night!"
    "I let my voice drip with mocking sarcasm."
    mike.say "Oh hey [hero.name], sorry to call so late. How you doing? I'm kind of lonely, can we go out?"
    palla.say "Yeah, fuck you too. Are you going to take me or not?"
    mike.say "I don't think I'm in the mood to take shit from you tonight, Palla."
    palla.say "[hero.name], Hi. I'm a hot, horny, lonely redhead, and I want to fucking dance. With you. If you ever want to kiss me, or do anything else to me, ever, you'll get your sexy ass over to the club and fucking dance with me."
    "Then her voice softens and turns super sexy."
    palla.say "...And I'll make it worth your while."
    "Well, damn. Is she really offering some sexy time? With that bitch, who knows."
    menu:
        "Pass":
            palla.say "Fine, your loss."
            "There is an audible click as she disconnects the call."
            $ palla.love -= 40
            $ palla.sub.val = 0
            return
        "Fine, I'll meet you there":
            "I agree to meet her, though I don't know if it'll be worth it. On the way over, I realize that she sounded a little drunk."
    $ game.room = "nightclub"
    scene bg nightclub
    show palla date happy
    with fade
    "When I get to the club, Palla is out on the dance floor. I have to admit, the girl has some moves! She is completely lost in the beat, moving and shifting in rhythm."
    "I'm almost entranced. I've never actually seen her like this. The more I watch, the more I realize that she could be a professional dancer."
    show palla normal
    "When the song ends, she slides gracefully off the dance floor and comes up to me. Damn, but she is hot in that dress!"
    show palla at zoomAt(1.5, (640, 1040))
    "To my surprise, she wraps her arms around me in a tight, slightly sweaty hug. The wallet in her hand presses into the small of my back."
    if hero.grooming < 4:
        show palla blank date
        palla.say "Damn, [hero.name], when was the last time you showered? Gross!"
        $ palla.love -= 1
        $ palla.sub -= 3
        show palla annoyed
        palla.say "Seriously if you expect to kiss me, take a shower first next time!"
    hide palla
    show palla date
    "After just a second, she steps back and grabs a passing server."
    palla.say "I want a Long Island Iced Tea, and whatever he's having. Oh, he's buying."
    "I mumble an order at the server, who quickly disappears. Before he is even gone, she drags me out to the dance floor."
    with hpunch
    palla.say "[hero.name], now is the time for dancing!"
    hide palla
    show dance palla
    with dissolve
    if hero.has_skill("dance"):
        "It's easy to get lost in the dance. She is smooth, moving sinuously and sexily against me and away from me as the music demands."
        $ palla.love += 2
        if not palla.flags.danced:
            palla.say "I had no idea you could dance, [hero.name]! You're pretty good at this!"
        else:
            palla.say "Yeah, there's the dancer I remember! You and me, baby, we got moves!"
        mike.say "Yeah, and you're fucking amazing at this!"
        $ hero.fun += 2
        $ hero.energy -= 2
    else:
        "Palla is a far, far better dancer than I am, and I get lost in her twists and turns. I try to keep up, but she seems to lose patience quickly."
        palla.say "[hero.name], if you want to kiss me, you'd better learn how to dance like a fucking man."
        mike.say "I guess you'll just have to teach me!"
        palla.say "Maybe. I'm not sure you're worth it yet."
        mike.say "Oh yeah? And what makes you think you're worth it to me?"
        "Palla thrusts out her sweaty chest and motions to her presented breasts with both hands. In that dress, she may be right; those tits just might be worth it."
        $ hero.energy -= 1
        $ palla.sub += 1
    hide dance palla
    show palla date
    with dissolve
    "After an hour or two of moving and swaying, we both come off the floor again, exhausted and out of breath. Our forgotten drinks are sitting on the little table where the server left them, the ice already melted."
    $ game.pass_time(2)
    palla.say "Well, fuck, now I need a fresh drink. Hey waiter!"
    "She flags down the server and gets a replacement, while I just watch her heaving breasts, glistening where the dress reveals the skin. She notices me watching."
    show palla normal date
    palla.say "Don't get any ideas, creep."
    mike.say "Ideas? You're the one who planted the idea in my head when you called me. At midnight, remember?"
    show palla annoyed
    "She just shrugs. Damn one minute she's sexy as hell, and the next she's an incredible bitch. It really makes me want to put her in her place."
    mike.say "In fact, you promised me a kiss."
    palla.say "I did no such thing."
    mike.say "Yeah you did. Your exact words were that you'd make it worth my while."
    show palla normal
    palla.say "I did! This dress, that dancing? You can't tell me that wasn't worth your while!"
    if hero.has_skill("dance"):
        palla.say "Seriously, that was some of the most fun I've had in months."
    else:
        palla.say "Even if you can't dance for shit, it was still awesome."
    mike.say "That was fun for {b}you{/b}, you said you'd make it worth {b}my{/b} while."
    "Palla shrugs and looks at me over the rim of her glass as she drains her Long Island Iced Tea."
    palla.say "Well, that's what you get. Sorry."
    mike.say "Wow, yeah, totally worth it."
    palla.say "Yes, yes it was. Thanks for admitting it. And fuck, I have to go the bathroom. Don't you dare follow me, creep."
    if palla.flags.storeanal:
        "There she goes again, daring me to follow her. Of course, last time I got some nice booty. Maybe that's what this is all about? Does she just want to feel...used?"
    else:
        "There she goes again, daring me to follow her. What the fuck is up with that?"
    menu:
        "Follow her":
            scene bg restroom with dissolve
            "I wait a couple of minutes, and then follow Palla into the bathroom, hoping she's the only one in there."
            "When I get there, she's looking into the mirror, adjusting her makeup. I see her eyes catch my reflection in the mirror, but she pretends not to see me."
            "Fine, if this is what she wants. I walk up behind her and grab her ponytail with one hand. The other I put on her shoulder and turn her."
            show palla date blush
            "This causes her neck to be wrenched when she spins around, and she gives a little shriek -- of delight!"
            "Encouraged by this, I slip my arm completely around her and pull her into an embrace, still pulling on her hair, though not hard enough to hurt. Much."
            show palla kiss with fade
            $ palla.flags.kiss += 1
            "I press my lips to hers, which pushes her ass back into the sink. She makes a muffled noise into me as I kiss her, hungrily."
            "Still holding her hair, and with my lips still hungrily taking hers, I bring my arm around front and pull her dress aside to fondle those beautiful tits."
            "Her nipple is as hard as a diamond when my palm comes across it, and she makes a muffled moan. Her arms wrap around my shoulders and grip me tight."
            "I am just about to pull her dress up and really go for it when I hear the door slam. I hear a woman practically shout."
            "Girl" "Oh go make out somewhere else, you perverts!"
            hide palla kiss
            show palla date
            with fade
            "I take a step back from Palla, and she looks thoroughly embarrassed. She grabs her purse and runs out through the door."
            hide palla with moveoutright
            "I don't know what to say to the stranger so I shrug kind of awkwardly."
            "Girl" "Just get the fuck out of here so I can pee!"
            "Right, then. I head out the door looking to follow Palla, but when I get out, she's nowhere to be seen."
            "And when I get back to the table, the bill she stuck me with turns out to be 200 bucks!"
            $ palla.flags.nokiss = False
            if palla.love.max < 120:
                $ palla.love.max = 120
            $ game.pass_time(1)
            $ hero.energy -= 1
            $ hero.fun += 1
        "Enough of her crap, I'm going home":
            "I wait for a moment, but she doesn't immediately come back. When the waiter brings the bill, my eyes almost bug out. 200 bucks!"
            $ palla.love -= 20

    if hero.money > 200:
        "I have it though, so I pay the bill anyway, and then I head home."
        $ hero.money -= 200
    else:
        "I don't have that kind of money right now, so I wait until the waiter isn't looking and sneak out."
    $ game.room = "livingroom"
    return

label palla_event_04b:
    show palla annoyed
    palla.say "Oh, it's you. What do you want?"
    mike.say "Just saying hi, I guess."
    palla.say "Oh, sure, now he'll deign to talk to me."
    mike.say "Palla, what did I do?"
    show palla angry
    palla.say "For fuck's sake, [hero.name], you're such a loser."
    mike.say "Yes, and that answers my question, how?"
    palla.say "If you had half a brain you wouldn't have to fucking ask!"
    mike.say "Okay pretend I don't have half a brain and fill me in, because reading your mind is like trying to watch Game of Thrones for the first time starting around season 6. I don't have a fucking clue what's going on in there."
    show palla annoyed
    "Palla rolls her eyes and turns away from me."
    mike.say "Hey! I'm talking to you, bitch!"
    show palla angry
    palla.say "Oh, right, yes and I'm supposed to hang on your every word, right? I'm not your good little bitch, [hero.name], and I'm not going to put up with your bullshit."
    mike.say "Put up with {b}my{/b} bullshit? Seriously?"
    "I didn't realize how much my voice was rising, but I notice other people in the mall starting to take notice of our conversation."
    palla.say "You should run along, now."
    "Is she worth this? I should just walk away, but. Despite it all I kind of like her. Am I stupid? Or just insane?"
    menu:
        "The smart move is to walk away":
            mike.say "Ugh, fine. You're not worth the effort."
            palla.say "And neither are you."
            "With that, she walks away for good."
            $ palla.set_gone_forever()
        "One more try":
            mike.say "Oh aren't you one high and mighty princess. What, I didn't come running like a dog when you snapped your fingers, so now I'm fucking useless?"
            palla.say "Oh, so you {b}do{/b} know why I'm mad! So you're not stupid, you're a liar!"
            mike.say "Oh give it the fuck up, Palla. What do you want from me?"
            palla.say "What do I want from you? Nothing. Nothing at all."
            mike.say "Then why are you still here, talking to me?"
            show palla normal
            "Palla purses her lips and looks down at the ground, then back at me. For a moment I think she's going to just turn and leave, but she doesn't."
            palla.say "Do you have any idea how much Audrey goes on about what a strong, sweet guy with a big dick you are? It's non-fucking-stop. That girl has it so bad for you."
            palla.say "Well, the only part she's right about is the big dick, and I'm not talking about your penis."
            mike.say "So wait, you're trying to steal a guy from your best friend?"
            show palla annoyed
            palla.say "No! It's not like that. Besides you're not really...I mean she's not really. I mean. Fuck. No! That's not what I mean at all."
            "She sighs."
            show palla normal
            palla.say "Look, here's the deal. I opened up to you, and you turned me away. Why should I ever trust you again?"
            mike.say "Trusted me? You called me up in the middle of the night and demanded I go out on your whim. How is that even the same thing?"
            if palla.love.max == 40:
                palla.say "I needed someone, right then. I got nothing. I had to dance with this greasy hard college kid with a fake ID. It was humiliating."
                mike.say "Dear God, Palla, did you let him fuck you?"
                "Palla bites her lip."
                palla.say "No but I let him feel my tits. And I had to shower three times. It wasn't worth it."
            else:
                palla.say "I waited in the bathroom for like half an hour for you!"
                mike.say "How the fuck was I supposed to know that's what you wanted?"
                palla.say "You sure knew in the store!"
                mike.say "What's with you and having guys creep on you, anyway? Don't you think that's just a little bit weird?"
                palla.say "Oh please, you're a bigger perv than I'll ever {b}hope{/b} to be. Yeah so what if that gets me going?"
            mike.say "Jesus, Palla, you're fucked up."
            palla.say "Stones and glass houses."
            mike.say "So fine, now what?"
            palla.say "Yeah, maybe we're not cut out for each other."
            mike.say "Oh no, I didn't just stand here and put up with your abuse for that."
            palla.say "Look, whatever you think you want, I'm a free spirit. I get in moods. If you can't indulge my moods, you're not going to work for me. If you don't want to deal with me asking for midnight dancing, that's your choice, but it's part of the package."
            mike.say "Package, huh. So that makes us a thing?"
            palla.say "Fuck no."
            mike.say "Then what?"
            palla.say "It means I might still be willing to talk to you."
            mike.say "Oh, gee. I feel special."
            show palla annoyed
            "Palla shrugs."
            palla.say "Look, if I hurt your dainty feelings, you know where to fuck off to."
            mike.say "So, do you want to go dancing?"
            show palla normal
            palla.say "Seriously, now? Don't be such a douche. You're still in timeout."
            mike.say "Do I get to come out of timeout?"
            palla.say "I don't know. Do you deserve me?"
            mike.say "Palla, nobody deserves you."
            show palla angry
            "Palla scowls at me."
            mike.say "What? It's true. You can take it the good way or the bad way. They're both true."
            palla.say "There's a good way to take it?"
            mike.say "You don't get to play dumb with me."
            show palla normal
            palla.say "Why do I put up with you again?"
            mike.say "Get back to me when you know the answer to that question."
            palla.say "Okay, I will. See you later."
            mike.say "Will I?"
            palla.say "Probably."
            $ palla.flags.ev4b = True
            $ palla.flags.ev4bDelay = TemporaryFlag(True, 3, "palla_event_04b_finish")
            $ palla.hide()
    hide palla
    return

label palla_event_04b_finish:
    if palla.love.max < 120:
        $ palla.love.max = 120
    if palla.sub.max < 60:
        $ palla.sub.max = 60
    $ palla.flags.nokiss = False
    $ palla.unhide()
    return

label palla_event_05:
    show palla
    palla.say "Hey, [hero.name]. You got a second to chat?"
    "Uh oh, how much abuse am I going to get now?"
    mike.say "Um sure, I got a sec. I guess."
    show palla blank
    palla.say "You don't sound enthusiastic."
    mike.say "Well, you do tell me I'm an asshole and a creep a lot, I'm not sure I'm ready for that just now."
    show palla joke
    palla.say "Okay, fair, I do. But I didn't call you asshole."
    mike.say "Yet."
    if not palla.flags.ev4b:
        show palla normal
        palla.say "Anyway, I wanted to talk about the club."
        mike.say "The dancing or the part where you ran off and disappeared just as it was getting good."
        show palla happy
        palla.say "Oh, so it was getting good?"
        mike.say "Are you trying to get me to say you're a good kisser?"
        palla.say "I already know I'm a good kisser, I don't need you to tell me that."
        mike.say "Uh huh."
        show palla normal
        palla.say "So yeah, I'm sorry, I ran off. And I wanted to thank you for coming and seeing me. I really needed someone, and you were there for me."
        mike.say "You made it pretty clear we'd be done if I didn't go."
        "Her expression changes, and I can't quite read it; it's like her lips are smiling and her eyes are sad. It doesn't make any sense to me."
        palla.say "But you did, and you were there for me. So, I just want..."
    else:
        show palla normal
        palla.say "Anyway, I've been thinking about our last conversation."
        mike.say "Oh? Anything you want to share?"
        palla.say "You're right. Nobody deserves me."
        mike.say "Well, maybe I was a little harsh."
        show palla annoyed
        palla.say "No, I get it. I'm a mean, demanding bitch. And I spent days thinking about what I'm going to do about that."
        mike.say "Oh yeah? And what are you going to do?"
        show palla normal
        palla.say "Absolutely fucking nothing, that's what. I'm comfortable with who I am."
        palla.say "So here's the deal, sport. I'm a mean, demanding, sexy as fuck bitch. Can you deal with that?"
        "Oh man, I really have to think about that. Can I deal with that?"
        mike.say "Sure, I guess."
        palla.say "Nope, nothing less than a full-throated yes will do."
        mike.say "Damn, demanding, aren't we?"
        palla.say "We already established that."
        mike.say "Fine, yes, but you get a caveat."
        palla.say "No caveats."
        mike.say "Fuck that. I'm not your bitch. Got it? I can deal with you being demanding, but you don't get to order me around. You can demand anything you want in the middle of the night."
        mike.say "But I'm not going to just come running. Maybe I will, maybe I won't. But if you treat me like a lapdog, I'm gone. Fair?"
    show palla at zoomAt(1.5, (640, 1040))
    "Without warning, she steps up to me and wraps her arms around my waist, pressing the length of her body up against mine. When she speaks the air from her words blows gently across my nose."
    if not palla.flags.ev4b:
        "I can smell slightly minty, fresh scent. Did she take a breath mint when she saw me?"
        palla.say "...to thank you."
    else:
        palla.say "Fair."
    "Her eyes are locked to mine. I thought for a minute she was going to kiss me, but she doesn't. But she also doesn't look away."
    hide palla
    show palla kiss
    with fade
    $ palla.flags.kiss += 1
    "Screw it, she keeps acting like I should take what I want, so I put my arms around her shoulders and pull her close, pressing my lips against hers."
    "Not a hint of resistance! She practically melts in my arms, and it's a real, genuine kiss. Her lips part and she offers her tongue, following my lead."
    "After a moment she tries to pull away."
    menu:
        "Let her":
            show palla happy
            with fade
            "I let her leave my embrace. She takes a step back and this may be the first time I've ever seen her genuinely smile."
            palla.say "Huh, that wasn't as bad as I thought. Maybe I'll let you do that again."
            $ palla.love += 10
        "Don't let her":
            "No, she's made it clear she wants me to be firm with her, whenever we're together. So when she tries to pull back, I don't let her."
            "I figure if she really tries, I'll let her go, but certainly not the first time."
            "And indeed, as our lips are locked together, she tries to pull away a second time, but this time clearly not actually putting anything into it."
            "So I reach up with my left hand and grab her pony tail. I yank just a little, which pulls her lips away from mine."
            show palla blush at zoomAt(1.5, (640, 1040))
            with fade
            mike.say "This kiss is over when I say it's over."
            "Palla squeaks, but doesn't say anything. So I let go of her hair and put my hand on her neck, pressing her face back into mine."
            hide palla
            show palla kiss
            with fade
            $ palla.flags.kiss += 1
            "This time, the kiss is full of fire and passion. If we weren't in a public place, I swear we we'd do the nasty right there."
            "But these things can't last forever, and after another moment I relax my arms."
            "She doesn't pull away immediately, either."
            show palla normal at zoomAt(1.5, (640, 1040))
            with fade
            "When she does pull away, her eyes are a bit glazed over, like she's high."
            palla.say "Oh, fuck, [hero.name]."
            "I guess she doesn't have any other words for that. And frankly neither do I."
            $ palla.sub += 10
            $ palla.love += 3
    show palla happy
    "When it's all done, Palla smiles brightly."
    mike.say "So, you want to go out sometime?"
    show palla joke
    palla.say "Nope!"
    "Well that takes me by surprise. What the fuck? After that?"
    show palla happy at startle
    "Seeing my distress, Palla laughs."
    palla.say "But! But but but! Keep that up and I'll let you earn it. I just...I just need to know something first."
    mike.say "What's that?"
    show palla joke
    palla.say "That's a secret. Don't worry, I won't keep you hanging for too long."
    mike.say "You better not!"
    palla.say "Unless you're an asshole. Which you are always an asshole so maybe I will."
    mike.say "Okay you can stop playing bitch now."
    hide palla
    show palla wink
    "Palla laughs and walks away. As she turns she makes a show of her ass and gives me the full sexy model walk."
    "Yeah. Her ass really is all that, too. There's a reason she gets paid for this."
    return

label palla_event_06:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    "When my phone vibrates, the caller ID shows another late night call from Palla. The last time she did this, it ended up mostly fun. Maybe she's done keeping me hanging?"
    mike.say "Hey, Palla!"
    palla.say "Hey, Handsome. You free?"
    menu:
        "Sorry, no":
            mike.say "Damn, and you called me handsome too. But I can't right now. Try me again later?"
            $ palla.flags.datetries += 1
            if palla.flags.datetries == 1:
                palla.say "Okay, next time. But you'd better be available then, this is a limited time offer!"
            elif palla.flags.datetries == 2:
                palla.say "You put me off last time, you'd better not put me off again. I'm not kidding!"
            else:
                palla.say "That's it, you lost your chance with me."
                "She hangs up. I try to call her back, but my number is blocked. Well, I guess that's over with."
                $ palla.set_gone_forever()
            return
        "Yes!":
            mike.say "Only if you promise not to call me an asshole."
            palla.say "Oooh, that's asking a lot."
            mike.say "Promise me!"
            palla.say "But what if you act like an asshole?"
            mike.say "I know it'd be a new experience for you, but just this once, try biting your tongue."
            palla.say "Maybe I'll bite something else instead. Anyway, I'll meet you at the restaurant. Oh and [hero.name] don't embarrass me. Dress nice. And shower first! I don't want you to be gross."
    if hero.grooming < 6:
        menu:
            "Take a shower":
                "After she hangs up, I smell my pits. She's right, I do need a shower, so I take one."
                $ hero.grooming += 8
            "I don't smell THAT bad":
                "I'm getting a little tired of that bitch telling me what to do, so fuck the shower."
    else:
        "After she hangs up, I decide that since I already showered today, I don't feel like I need another one."

    if palla.love.max < 160:
        $ palla.love.max = 160
    $ palla.flags.event6done = True
    "I take my time getting to the restaurant. It's not that I'm not looking forward to this; she's dropped enough hints that I think this really is the night."
    "But she's so damn bossy that I really feel like she needs to be kept waiting."
    scene bg door restaurant with fade
    "Of course, that runs the risk of her being angry when I get there, but I have a plan for that. I hope it works."
    "When I get there, she's already at a table, and I take my time walking up to it."
    scene bg restaurant
    show palla date angry
    with fade
    palla.say "Fuck, [hero.name], did you walk here by way of Cuba?"
    mike.say "No, I just walked slowly to let you think about me for awhile."
    palla.say "What, the fuck, a--"
    mike.say "Hey! You promised!"
    show palla annoyed
    "Palla purses her lips, but the word doesn't actually leave her mouth."
    mike.say "Okay, you want the real answer?"
    show palla angry
    palla.say "It better be good, or I swear I'll nail your cock to the table."
    "The answer I had prepared almost disappears from my head at that image. Ow. But after a second I recover."
    mike.say "Palla, you're fucking hot when you're angry, and I wanted to start the night out with a hot, sexy bitch on my arm."
    show palla date normal
    palla.say "Yeah, you have to work on that one, [hero.name]."
    "Damn. Well, at least she doesn't look angry any more."
    "Palla sighs."
    palla.say "If you know what's good for you, *[hero.name]*, you'll knock that shit off right now. Or you won't get what I brought for you."
    "I admit, that gets me curious. She doesn't have room to hide much of anything in that dress, and that wallet couldn't hold much more than a card or two."
    mike.say "Okay, you got me. What did you bring me?"
    palla.say "First, did you shower?"
    if hero.grooming < 6:
        mike.say "Nope, you can take me as I am."
        "Palla sighs, and seriously looks disappointed. I mean, maybe I should've given her that one, but she has to stop bossing me around."
        palla.say "I sure hope. Ugh. Gross dude, just gross."
        $ palla.love -= 5
    else:
        mike.say "Can't you tell, my hair's still wet."
        palla.say "Hmm, and I can't smell you from here."
        $ palla.love += 5
    show palla at zoomAt(1.5, (640, 1040))
    "Palla takes a deep breath, and then turns on her modelling charm. She looks at me and suddenly I'm the camera. And she knows how to work the camera."
    palla.say "Say something nice about me."
    menu:
        "Humor her":
            mike.say "You, uh, you've got a devastating smile?"
            show palla date blank
            palla.say "Seriously, is that all you got?"
            mike.say "No, it's just I'm stunned by your sudden model pose and all the words have been chased from my head by your beautiousness."
            "It wasn't too far from the truth, though really it's stunned by her rapid changes from bitchy to delicious and back again."
            show palla joke
            palla.say "On a scale of 1 to 10 I'm going to give that one a 3, but at least, and work with me here..."
            palla.say "You're not being an asshole."
            show palla flirt
            "Palla leans across the table, giving me a nice view down her dress."
            palla.say "Now, tell me I'm beautiful again."
            mike.say "Okay, Palla, you're beautiful."
            palla.say "Keep going."
            mike.say "Well for one, your body is amazing. Your breasts make me want to grab them and hold them all night."
            show palla date happy
            "I figure if she's not offended by that, I'd go ahead and pursue it."
            mike.say "Your legs, well, when you do that catwalk turn, they make me want to just push you onto a bed, spread them out and dive right in."
            mike.say "And your lips. You really do have the most amazing smile. But I most want to see those lips, wrapped around my cock, sliding back and forth while you finger yourself."
            "I stop and wait for Palla's reaction, which I hope isn't a giant slap in the face."
            $ palla.love += 5
        "Fuck that noise":
            mike.say "Palla, you're gorgeous, but you're being a bossy bitch tonight, and I've just about had enough."
            show palla sad date
            palla.say "Damn it, [hero.name], I'm trying to be good. I really am. Look, I like you, okay? I want you, and I'm trying to give you a chance to earn the right."
            mike.say "The right to what, exactly?"
            palla.say "Jesus, [hero.name], do I have to spell it out? Are you the densest motherfucker in this town, or are we doing this dance because you want to fuck with me?"
            "I sigh, softly, and take a second to compose my words."
            mike.say "Palla, I don't know how to deal with you. One minute you're sweet, one minute you're the world's biggest bitch, and I really don't know how to cope with any of that."
            if hero.grooming < 6:
                show palla sad date
                palla.say "Okay, fine, you win. I thought you would be the one, even as much of an asshole as you are, but you're just not, and you're not going to be. I get it. I'm sorry."
                palla.say "This whole thing was a bad idea. Never mind. I'll leave you alone now."
                "Palla pushes away from the table and gets up. As she turns and storms away, I can see tears streaming down her face."
                "I really wish I understood her, but I don't. Maybe if I'd given in a little more to her whims something could've happened?"
                "But maybe I'm better off not having to deal with that crap."
                $ palla.set_gone_forever()
                return
            else:
                show palla sad date
                palla.say "Okay, at least you showered for me. That's something. Maybe this won't be so bad."
                mike.say "Maybe WHAT won't be so bad?"
                palla.say "You really don't know why you're here?"
                mike.say "I'm here because a crazy but hot woman calls me up in the middle of the night when she's lonely. She teases me but won't ever admit what she actually wants."
                mike.say "I'm here because apparently I'm a masochist who puts up with this crap in the hopes that if I can get past your bitchiness, the sweet, sexy woman will come out."
                show palla normal date
                mike.say "I'm here maybe because I'm stupid or maybe because I'm hopeful. Very possibly it's both."
                mike.say "And mostly I'm here because I'm curious, curious enough to weather your scorn to see what comes out the other side."
                palla.say "Okay. Okay. Okay, maybe I can do this, then."
    hide palla at zoomAt(1.5, (640, 1040)) with moveoutbottom
    "Palla slides forward and disappears under the table."
    "I feel her hands on my knees, which she pushes apart, not entirely gently. Her entire body pushes forward and then I see her red hair peeking out from under the table, in my lap."
    mike.say "Wait, what are you doing?"
    palla.say "When the waiter shows up, tell him I went to powder my nose and order a salad for me."
    show palla restaurantbj with fade
    "Palla unzips my pants and sure enough as soon as her fingers brush against my cock, it responds and springs to attention in her fingers."
    "She brushes her tongue against the very tip."
    if hero.grooming < 6:
        $ palla.love -= 10
        palla.say "I really, really wish you'd showered, this would be a lot less stinky down here."
        mike.say "Um, uh, yeah, next time I guess."
    palla.say "Pretend like nothing's going on. Get your phone out and stare at it. If you say anything or give me up I swear I'll bite."
    "That threat should bother me, but it just turns me on even more."
    show palla restaurantbj suckdick
    "Her lips slide around my penis, taking just the tip of my head into her mouth. She uses her tongue the way only someone who's got some experience at this can do."
    "I pull out my phone, like she said, and pretend to look at it. It turns out to be really, really hard not to make a sound, because she's {b}good{/b} at this."
    "After a few strokes, she starts taking me deeper, bit by bit, until I can start to feel the tip of my cock bumping against the back of her throat."
    "I slip one hand under the table, putting it on the back of her neck. She resists my attempts to speed her up."
    "That's probably just as well, there's no way no one would notice that."
    menu:
        "Make her deep throat":
            "But she's down there, and she's liked it every time I've taken charge. So instead of trying to speed her up, I slow her down."
            "When she tries to pull back, I hold her head right where it is, with my cock just touching her tonsils."
            "And carefully I push her down further, until she's all the way down to the base, and hold her there."
            "I can hear her making a gagging noise, but it doesn't seem too serious, and she isn't fighting me at all."
            with hpunch
            "So I let her go back up to just the head, and then down a few more times, each time holding myself all the way in."
            show palla restaurantbj suckdick dick with hpunch
            "It doesn't take long before I cum all down her throat, and this one feels like it goes on forever."
            with hpunch
            "But just because I've cummed, that doesn't mean she can be done."
            "I keep holding her down there until I'm fully limp, which takes another five or six minutes. She makes a little play at trying to get up, but doesn't try too hard."
            show palla restaurantbj kissdick face
            "Once I'm done, I release my grip on her neck."
            show palla restaurantbj kissfeet
            "She kisses all the way down my thighs, past my knees, and down to my feet."
            "I've never had a girl kiss my feet after a blow job before, and I think I kind of like it!"
            $ palla.sub += 10
        "Let her control the pace":
            "I leave my hand slack on her neck, letting her control the pace."
            show sexinserts head palla zorder 1 at center, zoomAt(1, (-140, 970))
            "It doesn't take her too long, either; like I said, she's good at this. Not a hint of teeth and expert use of her tongue."
            show sexinserts head palla cum zorder 1 at center, zoomAt(1, (-140, 970))
            show palla restaurantbj suckdick dick
            with hpunch
            "I fill her mouth up with my cum, which goes on a lot longer than I would have expected."
            show sexinserts head palla -cum zorder 1 at center, zoomAt(1, (-140, 970))
            show palla restaurantbj kissdick face
            with hpunch
            "I hear her swallow, and then she gives me little kisses all along my belt line and around the insides of my thighs, before backing out from between my legs."
            $ palla.love += 5
    hide sexinserts
    show palla date normal at zoomAt(1.5, (640, 2040))
    show palla at zoomAt(1.5, (640, 1140)) with move
    "Palla slips back up out from under the table, and the conversation at the table next to us suddenly goes stone quiet. I guess someone noticed her."
    show palla date happy
    "But she doesn't seem to mind. She flashes me a bright smile, with just a little bit of my cum dripping from one corner of her mouth."
    palla.say "Oh look, you came before the food did."
    mike.say "Well, damn, I guess I did."
    show palla date normal
    "And then Palla continues the date, pretending that didn't happen."
    "When the waiter brings our meal, she goes on with her normal erratic behavior, alternately telling me I'm handsome and finding something I did, or said or just smelled to be annoyed about."
    "Somehow after that orgasm, it's all a little easier to take, though."
    hide palla
    show palla date normal
    "When the meal is over, and we're on the way out of the restaurant, I invite her back to the house."
    palla.say "Nope, you still haven't earned that one. Yet. But I'll think about it next time, okay?"
    mike.say "Next time?"
    palla.say "There better be a next time."
    mike.say "You know, that's historically been more up to you than me."
    palla.say "Well, ask me again tomorrow and I guess you'll just have to roll the dice."
    "And before I can answer, she gives me a deep, long kiss. Then she strides away, giving me that model hip sway. I do like that model hip sway."
    $ palla.flags.nodate = False
    $ game.pass_time(4)
    $ hero.fun += 3
    $ hero.energy -= 4
    $ game.room = "livingroom"
    return

label palla_event_07:
    $ palla.flags.talksex = False
    $ palla.flags.relationshiptalkdelay = TemporaryFlag(True, 3)
    "I see Palla and she immediately walks up to me."
    show palla normal
    "After our last date, I honestly have no idea what she's going to say or do. On one hand, she clearly enjoyed it."
    "On the other hand, she's always berating me for something."
    "And maybe for her this was a one night stand, but I've always felt like she was looking for something more, even if she never says it."
    show palla angry
    palla.say "[hero.name], we have to talk."
    "Ah, it's going to be like that, is it."
    mike.say "Sure, Palla. What's up?"
    palla.say "I...ugh, I don't really know how to start. I just. Are you going to dump me now?"
    "Okay, so even not knowing what to expect, I didn't expect that."
    mike.say "Dump you? I don't...it's not like we had any kind of agreements."
    show palla annoyed
    palla.say "It's not that, [hero.name], it's just that...ugh, MEN."
    mike.say "Palla, you're not making any sense."
    show palla angry
    palla.say "Just give me the speech. Tell me it was fun and you're done with me."
    menu:
        "I'm done with you":
            mike.say "Fine, if that's what you want to hear. We had our fun, and now we're done."
            show palla sad
            "Palla looks at me, tears welling up in her eyes."
            palla.say "Okay. Thanks for at least being a man."
            show palla cry
            "As she turns, I can hear a sob. It makes me briefly wonder if I've done the right thing."
            $ palla.set_gone_forever()
            hide palla with dissolve
            return
        "It was fun, I'm not done":
            if palla.love.max < 200:
                $ palla.love.max = 200
            $ palla.flags.nodate = False
            $ palla.love += 5
            mike.say "I don't know where this is coming from, Palla. It was fun, it was a LOT of fun."
            mike.say "And I'm not done with you, not yet."
            show palla surprised
            show fx question
            palla.say "Okay, th--wait, really?"
            mike.say "I get the feeling this is not normal for you?"
            hide fx
            show palla blank
            palla.say "Men only ever want one thing, and then they're gone. But, look. I'm not looking for a boyfriend."
            mike.say "So now you're the one who's one and done?"
            show palla joke
            palla.say "No, no. I'll go out with you. Maybe go home with you again."
            if palla.flags.anal:
                show palla annoyed
                palla.say "But no more anal! Ugh!"
            show palla blank
            palla.say "But I don't want to be your girlfriend, and I don't need you to be my boyfriend."
            mike.say "Huh, so friends with benefits?"
            show palla normal
            palla.say "Yeah, a bitch and an asshole who can do the horizontal dance."
            menu:
                "I'm down with that":
                    show palla happy
                    mike.say "Cool, I'm down with that."
                    palla.say "Yeah, I ho--well, yeah."
                    show palla normal
                    "Palla approaches me and gives me a hug and a quick kiss."
                    palla.say "And thanks for not being a typical guy."
                    "And then she walks off, leaving me wondering where this is going to go."
                    $ palla.set_room(None)
                    hide palla
                    return
                "What if I want more?":
                    mike.say "But what if I want a girlfriend, Palla? What if I want more than a fuck friend?"
                    show palla happy
                    $ palla.love += 5
                    palla.say "Should I care what you want?"
                    mike.say "That's...ugh, that's you telling me why I shouldn't want you as a girlfriend."
                    palla.say "You're catching on."
                    mike.say "Fine, but. Will you at least think about it?"
                    show palla normal
                    palla.say "Sure, I'll think about it."
                    "..."
                    palla.say "And I've thought about it, and no. But you get to have these on the regular, right?"
                    "She cups her hands under her breasts and displays them. They're easy to admire."
                    mike.say "Yeah, but..."
                    palla.say "And I don't have to care who you fuck or when you fuck, as long as you throw me a bone now and then. So to speak."
                    mike.say "Okay, fine."
                    palla.say "You don't sound convinced. Fine. Prove it to me, for real, and I'll think about it. For real."
                    mike.say "Prove what?"
                    palla.say "That you're man enough for me. I need...a lot of man. Well, a lot of men, usually. But if you can keep up with me, maybe."
                    mike.say "Okay, it's a deal. I'll prove it."
                    "She gives me a wink and walks away."
                "I want you to be mine and mine alone":
                    mike.say "No, Palla. I want you to be mine. Mine alone."
                    call palla_mine_alone from _call_palla_mine_alone
    hide palla
    return

label palla_mine_alone:
    $ palla.flags.minealone = True
    show palla blush
    if palla.sub.max < 70:
        $ palla.sub.max = 70
    if palla.sub > 50:
        "She goes quiet for just a second, taken by surprise. But also delighted, though she quickly tries to hide it."
        show palla surprised blush
        palla.say "I, uh. No, no. No. I mean I mi--no. Just no."
        mike.say "Mine. My bitch."
        show palla angry
        palla.say "Don't call me that."
        mike.say "My bitch!"
        palla.say "I'm not your bitch. You haven't earned that yet."
        mike.say "Yet."
        show palla happy
        "She smiles."
        palla.say "Yet."
        mike.say "I will."
        show palla normal
        palla.say "Promise?"
        mike.say "Cross my heart."
        show palla happy
        "She smiles and walks away, looking almost dazed."
    elif palla.sub > 25:
        show palla normal
        palla.say "Oh please, [hero.name], don't make me laugh. I'm way too much woman for you."
        mike.say "Way too much bitch for me, anyway."
        palla.say "And you have no idea how to handle a bitch like me."
        mike.say "With a firm hand and a strong word."
        show palla annoyed
        palla.say "Don't make me laugh, [hero.name], your hand just isn't that firm."
        "Oh, she is so full of herself. It makes me want to put her into her place. I just need to find the right time, and right place."
        show palla normal
        palla.say "I gotta run, [hero.name]. If you want me, you know where to find me."
    else:
        show palla angry
        palla.say "Fuck you, [hero.name], you aren't man enough for me. Three of you wouldn't be man enough for me."
        palla.say "And if that's your attitude, maybe we don't get to be fuck friends."
        mike.say "Whoa, wait a minute there, don't have a breakdown."
        show palla annoyed
        palla.say "You can't handle me. I dare you to try."
        mike.say "I'll take that as a challenge."
        show palla normal
        palla.say "You better get creative, then. See you later!"
    $ palla.sub += 5
    return

label palla_event_07b:
    show palla
    palla.say "So, [hero.name], I've been trying to figure out exactly what we are."
    mike.say "Um. People? Human beings? Boys and girls?"
    show palla annoyed
    palla.say "Ha. Ha. Fuck you."
    "I shrug."
    show palla angry
    palla.say "I'm trying to be serious here."
    mike.say "What do you mean, then?"
    show palla normal
    palla.say "How would you define our relationship?"
    "This could be my chance to set the tone of our relationship."
    "What do I want? What do I think she'll put up with? She told me she doesn't want to be anybody's girlfriend."
    "And do I even want that? She has a tendency to flounce, so if I push too hard here this could suck."
    "But it might be worth it."

label palla_event_07b_loop(matter=False):
    menu:
        "Friends" if not palla.flags.minealone:
            mike.say "I'd say we're really good friends, Palla."
            show palla normal
            palla.say "That's it? Just friends?"
            mike.say "How many friends do you have?"
            palla.say "Um. Two?"
            mike.say "Including me?"
            palla.say "Uh, yeah. Including you."
            mike.say "Then I don't think \"just\" friends applies here, Palla."
            palla.say "Yeah, but, you know, we fuck."
            if palla.sexperience > 5:
                palla.say "Kind of a lot."
            mike.say "Um, that's what friends are for?"
            show palla blank
            "Palla shoots me a dark look."
            mike.say "Good friend? Close friend?"
            palla.say "Fuck friend?"
            mike.say "Girlfriend?"
            show palla angry
            palla.say "Don't you dare use that word."
            "I frown."
            mike.say "You say you don't want that, but here we are having this conversation. Which makes it sound like you do want that. Are you being honest with me?"
            show palla annoyed
            palla.say "I don't lie to you."
            mike.say "Are you being honest with yourself?"
            "Palla pauses, and has to think about that."
            show palla normal
            palla.say "Probably. Look, I guess I'm okay being close friends. Who fuck sometimes."
            mike.say "That sounds fun. You wanna?"
            palla.say "Not now. I have a headache."
            show palla happy at startle
            "We both laugh, even though it's stupid."
        "Boyfriend/girlfriend":

            "Screw it, I know what I want even if she doesn't want it."
            mike.say "I think we're boyfriend and girlfriend, Palla."
            show palla angry
            palla.say "Ugh, I don't want to be anybody's fucking girlfriend. Don't feed me that shit sandwich."
            mike.say "What? Why did you ask, then? What are the possible answers? We're friends or you're my girlfriend. What else am I going to say?"
            show palla annoyed
            palla.say "Um, well. I thought maybe, um..."
            "Palla grows frustrated as her words fail."
            palla.say "Fuck, why should I be stuck with an asshole like you?"
            mike.say "Palla..."
            show palla angry
            palla.say "What??"
            mike.say "You're getting angry, but not at me."
            palla.say "Don't tell me who I'm angry at."
            "It's tempting to tell her off, but after all this time I know her well enough to know that I'd be poking a bear. Being patient is hard, but it's the only way forward here."
            mike.say "You had to know what the answer would be when you asked. Would you rather I don't answer these questions?"
            palla.say "Yes! No! I'd rather you weren't an asshole!"
            mike.say "Why don't you want a boyfriend?"
            palla.say "I want a boyfriend, I don't want to be a girlfriend."
            mike.say "What?"
            palla.say "Do I need to use smaller words?"
            mike.say "No, I get the words, I just don't understand them."
            show palla annoyed
            palla.say "Ugh, men."
            "I take a deep breath. Getting angry won't help here."
            "Getting angry really won't help here."
            "But it's so very hard."
            mike.say "So, let me get this right. You want a boyfriend, but your problem is with...being a girlfriend. So you want somebody who's there for you, but you don't want to be there for me?"
            palla.say "Yes! I mean no! That's not quite right."
            show palla normal
            palla.say "I want...look, you understand that all men suck, right?"
            mike.say "I'm pretty sure if I say \"Not all men\", you'll actually slap me, so let's, for the sake of argument, just say yes."
            palla.say "So that's it. I don't want...I don't need, I mean...men fuck over bitches like me."
            mike.say "So wait a minute? Do you not trust me?"
            show palla angry
            palla.say "No!"
            show palla annoyed
            palla.say "I mean, no it's not that I don't trust you."
            mike.say "Then what?"
            show palla normal
            palla.say "It's that I don't trust men."
            mike.say "And I'm a man."
            show palla annoyed
            palla.say "Yes, you are SUCH a man."
            mike.say "Fine. So what you wanted to hear is that I'm your boyfriend, and you're...free to pursue whatever you want."
            show palla normal
            palla.say "Well, I guess when you put it like that..."
            mike.say "It sounds kind of shitty."
            palla.say "I'm sorry. It does. I'm sorry I'm being a bitch."
            mike.say "It's okay."
            show palla annoyed
            palla.say "Fine, Jesus Christ I can't believe I'm saying this to an asshole like you."
            "There's an odd pause, like she was going to say something, and then chose not to. I finally have to ask."
            mike.say "Say what?"
            show palla normal blush
            palla.say "I'll be your fucking girlfriend, okay? Just. Ugh. Don't make me say it again? I feel gross."
            mike.say "Are you kidding? I'm going to make you say it every chance I get."
            palla.say "Do that and you'll wake up without balls one morning. Don't push me. And don't think just because I let you use that word, we're exclusive!"
            mike.say "Feisty. That's what I love about you."
            palla.say "Don't take this the wrong way, but I need to go now or I'm going to throw up."
            mike.say "See you later, girlfriend!"
            "She flips me off as she walks away."
            $ palla.set_girlfriend()
            if palla.sub.max < 70:
                $ palla.sub.max = 70

        "You're mine" if not palla.flags.minealone and palla.sub >= 50:
            $ palla.flags.minealone = True
            mike.say "That's simple, Palla. You're mine. You're mine alone."
            palla.say "Oh you shut that shit up right the fuck now. Don't think I won't shove one of my spiked heels into your ear."
            mike.say "I'm serious. You're a crazy bitch, but...that's what I want. Maybe it's stupid or maybe I'm a masochist."
            mike.say "But I want you, and I want you to be mine."
            call palla_mine_alone from _call_palla_mine_alone_2
            $ palla.set_girlfriend()

        "Does it matter?" if not matter:
            "There seems to be no scenario I can think of where this ends well for me, so I decide to go the middle route."
            mike.say "Does it matter what we are, Palla? It seems like we've got something good here. Let's not throw labels on it."
            palla.say "If you had any less balls you'd be a woman, [hero.name]."
            "Well, that's not the answer I was expecting. I guess I should have known better."
            mike.say "Sadly, Palla, I'll never have a fantastic rack like you do."
            palla.say "Flattery isn't going to get you out of this."
            "Her slight smile reveals the lie in her words."
            mike.say "Seriously, those tits motivate me in so many ways. Can you imagine those tits on me? Wait, I can imagine those tits on me, with my face smashed between them..."
            palla.say "Fine, I get it, you like tits. You and every other dude on the planet."
            mike.say "Yeah but I mean {b}your{/b} tits. They're a cut above."
            palla.say "You're stalling, [hero.name]. Give me a real answer."
            call palla_event_07b_loop (matter=True) from _call_palla_event_07b_loop

        "I already told you" if palla.flags.minealone:
            mike.say "Palla, we've had this conversation before. I want you to be mine."
            palla.say "You told me, yes, but I didn't agree to it."
            mike.say "Well, then I'm going to say it again, and you're going to do whatever you're going to do again."

            if palla.sub >= 60:
                palla.say "I just...want to hear the words."
                mike.say "You're mine."
                palla.say "Your what?"
                mike.say "My girlfriend."
                "Palla closes her eyes. It actually looks like she's having a sexual moment."
                palla.say "[hero.name], I hate that word."
                mike.say "Too bad. You're my girlfriend."
                "Palla squeaks, then nods."
            else:
                palla.say "I just don't know if I can do that, [hero.name]. Not for you, not for anyone."
                mike.say "Well. I can be patient, for now."
                palla.say "So you're not going to let that go?"
                mike.say "I was letting it go, Palla. You're the one who asked."
                "She nods."
                palla.say "You're right."
                palla.say "So, so you want...So you want me to be your...your..."
                mike.say "Girlfriend?"
                show palla annoyed blush
                palla.say "Ugh. Yeah. That."
                mike.say "Yes."
                palla.say "No. I...wait."
                "Palla takes a deep breath. She's shaking."
                show palla normal
                palla.say "Fine, but...we're not exclusive. And never actually...say it."
                mike.say "Say what? Girlfriend?"
                palla.say "Gross! Don't say it."
                mike.say "But...you'll be it?"
                show palla annoyed
                "Palla looks exasperated."
                palla.say "Yes, but only if you promise never to say it again."
                mike.say "I don't think it really works like that."
                palla.say "It does today."
            "When Palla turns to leave, I can see her shoulders trembling. That conversation was hard on her, but I think it will be worth it."
            $ palla.set_girlfriend()
            if palla.sub.max < 70:
                $ palla.sub.max = 70
    return

label palla_event_08:
    play sound cell_vibrate loop
    "I guess by now I should be used to Palla ringing me up late at night. I guess I don't mind, we've always had fun."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    mike.say "Hey sexy bitch. What's up?"
    palla.say "Hey, [hero.name]. I was having trouble settling down, and...I have a weird question for you."
    mike.say "Hit me."
    if palla.flags.minealone:
        palla.say "You told me once that you want me to be yours and yours alone."
        mike.say "I did."
        palla.say "Is that still true? Do you care who else I date?"
    else:
        palla.say "Are you still okay with me dating other people?"
        mike.say "That's kind of an odd question, coming from you."
        palla.say "I know, it's just...just answer the fucking question, okay?"
    menu:
        "I want you all to myself":
            $ palla.flags.slavepath = True
            if palla.sub.max < 100:
                $ palla.sub.max = 100
            mike.say "Yeah, I guess I'm kind of possessive. And I like you."
            mike.say "I think I've earned it."
            palla.say "I don't know..."
            mike.say "Then why the fuck did you ask?"
            palla.say "I was just...having a bad night, I guess, and I wanted..."
            mike.say "Palla, shut up and repeat after me."
            "To my surprise, she actually shuts up."
            mike.say "\"[hero.name], I am yours and yours alone. No one but you can have me.\""
            "There is silence from the other end of the line."
            mike.say "Palla?"
            palla.say "I don't think I can--"
            mike.say "Say it! You asked, you want this. Now say it."
            "There is silence for another few seconds, but then she speaks, and I can hear her trembling."
            palla.say "Wait, [hero.name], wait. I'm not...I'm not saying I won't, but can I have some time?"
            mike.say "Some time? For what?"
            palla.say "To see what it's like. Only dating one guy. I haven't done that since high school, and it was bad."
            "I have to think about that, for a minute. I know she wants a firm hand, but I also know if I go too far, she'll resent it."
            mike.say "Okay, Palla. So you're going to stop dating anyone else?"
            palla.say "Y-yes."
            mike.say "And you'll say it?"
            palla.say "Maybe? I just need...I just need to know it will feel right this time."
            mike.say "Okay. Okay, Palla. We'll give it some time. But you are mine, now."
            palla.say "I...y-yes. I should go, [hero.name]."
            if palla.love >= 160:
                palla.say "I love you!"
            "And before I can respond, the call is disconnected."
        "I don't care who else you see":
            mike.say "It's okay, Palla. I don't care who you see. I know you need space."
            "There is a pause before she answers, and she actually sounds disappointed."
            palla.say "[hero.name], I don't think anyone has ever loved me before. Before you. Do you love me?"
            mike.say "Yes, Palla. I do love you."
            palla.say "Okay, [hero.name]. I think that's what I needed to hear. And...I love you too!"
            "And before I can respond, the call is disconnected."
    return

label palla_event_09:
    "When I arrive in the nightclub, I see Palla in the back. I don't have a chance to see or greet her, though, as she and a blond guy in a black trenchcoat disappear through a door in the back."
    if palla.flags.slavepath:
        "That's weird. She promised herself to me, and that looked like it might be some kind of a date."
    else:
        "I wonder if that's one of the other guys she's seeing."
    menu:
        "Follow her":
            "I decide I should go check that out. But as I approach the door she went through, two rather large men--I think you might call them beefy--step in my way."
            "Bouncer" "The VIP Lounge is private, kid."
            mike.say "Oh, sorry. I was just going in to meet a friend."
            "Bouncer" "Do you have an invitation? I don't see any punks on this list."
            "The bouncer flexes his fist menacingly."
            mike.say "I, ah, no, no."
            "Bouncer" "Beat it, kid."
            "As I walk away, I can't help but wonder who that guy with her was."
        "Leave her alone":
            "Palla's business is her own business, and I should leave her alone."
    return

label palla_event_10:
    "While browsing around the electronics shop, I can't help but think the cashier looks familiar. Maybe it's because I've been here so much I recognize the employees, but I think it's something else."
    show shawn
    "And then it hits me. If he wore a trench coat, he'd could be the guy I saw with Palla the other night. Maybe I can casually figure out what was going on there without being a jerk to anyone."
    mike.say "Hey, man. Didn't I see you in the VIP Lounge the other night?"
    shawn.say "Who, me?"
    "His nametag says \"Shawn\""
    mike.say "Yeah! Shawn, right? I swear it was you, hanging out with a gorgeous redhead, right?"
    shawn.say "Oh right, yeah! I was there with Palla a few nights ago."
    "I choose my words carefully so it doesn't look like I'm prying.."
    mike.say "Good job, man, she's hot! I hope you had a good date!"
    shawn.say "Oh heck yeah, man, she's the sexiest girl I've ever met. Way out of my league, am lucky to have any kind of shot at all with her."
    mike.say "Well hey if I see you there again, I'll be sure to say hi!"
    "Shawn looks around furtively, as though to see if anyone else is watching."
    shawn.say "And if you want to, you know, buy anything...you know, to make the club more fun or something, just hit me up."
    "Buy something? Like what? Drugs?"
    mike.say "Uh, sure. I'll keep that in mind."
    "Now that I think about it, he does smell a bit like stale smoke. Huh."
    mike.say "See you around."
    return

label palla_event_11:
    $ palla.set_counter("shawnencounter", None)
    $ palla.set_counter("pallavisit12")
    show shawn date
    shawn.say "Hey! Hey you, [hero.name]!"
    "Shawn practically runs up to me and gets right up into my face. His tone is angry, and there's an undercurrent of potential violence."
    shawn.say "What the fuck did you say to Palla, huh?"
    mike.say "All I did was ask her about you."
    shawn.say "Bullshit! She was devastated, man! I've never seen her like that. What the fuck did you do to her?"
    "Shawn raises his right hand, ball curled into a fist."
    menu:
        "Hit him first":
            "The dude looks like he's ready to try to take me down, so I don't wait. I step right up and launch my best punch right into his jaw."
            play sound punch_hard
            pause 0.2
            show shawn at center, hshake
            pause 0.2
            hide shawn with moveoutbottom
            with hpunch
            "And he goes right down to the ground."
            shawn.say "You hit me! Why the fuck did you hit me?"
            mike.say "You were about to take a punch at me."
            shawn.say "I wasn't...No, I'm not that kind of guy."
            "Shawn puts one hand on his face where I decked him; it's already starting to turn a bright shade of purple."
            "Ow, man, that fucking hurt."
            mike.say "Well, don't raise your fist at a guy while yelling. I honestly thought you were coming after me."
            show shawn date with moveinbottom
            "Shawn picks himself up off the pavement."
            shawn.say "I'm not going to hit you, but I want to know what you did to Palla!"
        "No need for violence!":
            "I put both hands in the air and take a step backward."
            mike.say "Hey, no need for violence."
            "Shawn looks confused for a moment, then looks at his fist as though it was someone else's. Suddenly realization strikes him and he puts his hand down."
            shawn.say "Oh, sorry man. I'm not violent by nature."
            shawn.say "But fuck man, what did you do to her?"

    mike.say "I didn't do anything, man. Seriously, I asked her about you and she turned into a stone cold bitch and stormed off."
    shawn.say "For serious? That's it?"
    mike.say "I'd say that's weird, but Palla's got some issues."
    shawn.say "You're not wrong."
    shawn.say "Look, are you her boyfriend or something?"
    mike.say "We...have an arrangement, yes."
    shawn.say "Damn, you're lucky, then."
    mike.say "I'm not so sure about that, right now."
    shawn.say "Well, you need to apologize for whatever it is you said."
    mike.say "All I did was ask about you. So are you her other boyfriend?"
    shawn.say "I wish! No."
    mike.say "I thought you said you went on a date with her to the VIP Lounge."
    shawn.say "Oh, that. It was...well it was a date to me, not so much to her."
    mike.say "What was it to her, then?"
    shawn.say "She was just getting me into the VIP Lounge. See, she's still got some contacts so she can get into places like that, but I can't."
    mike.say "You don't really look like the VIP Lounge type, I have to admit. Why would you want to get in there?"
    shawn.say "Oh, my side business."
    mike.say "What's that?"
    shawn.say "Weed. Want to buy some?"
    mike.say "Not right now."
    shawn.say "Pity, I really need the money. We're not going to make rent this month."
    mike.say "We?"
    shawn.say "Yeah, me and Palla."
    mike.say "You live with Palla?"
    shawn.say "Oh. Oh fuck. She's going to murder me if she finds out I told you. I mean, seriously. Please don't tell her!"
    mike.say "{b}You live with Palla?{/b}"
    shawn.say "Yeah man, I needed a roomie to help pay the rent, and she needed a new place. Worked out for a while but I keep having to float her the cash for her half and this month I don't have it."
    mike.say "I didn't know any of this."
    shawn.say "Some boyfriend you are."
    mike.say "How much does she owe you?"
    shawn.say "For this month, 250{image=gui/icons/icon_money.png}."
    mike.say "Total?"
    shawn.say "Um, I don't know. I think it's like five grand by now."
    mike.say "Holy shit."
    shawn.say "Look, I don't care about that. But dude, don't make her cry."
    "I can only laugh."
    mike.say "Look, there's a few things I can make Palla do or not do, but that's not on the list."
    shawn.say "Yeah man, I guess. But. If you hurt her, I'll make sure the zombies get you first."
    mike.say "The zombies?"
    shawn.say "Yeah, when the zombies come."
    mike.say "Uh okay, whatever."
    menu:
        "Offer to cover her rent" if hero.money > 250:
            mike.say "Look, I'll cover her rent this month."
            shawn.say "Oh, no, I can't do that."
            mike.say "Fine, I'll buy 250{image=gui/icons/icon_money.png} of your weed."
            shawn.say "Deal!"
            $ palla.flags.rentpaid = True
            $ hero.money -= 250
            $ hero.gain_item("weed", 2)
            shawn.say "If you ever need more, you know where to find me."
        "Say goodbye to this weirdo":
            mike.say "Goodbye now."
            shawn.say "Zombie food, man."
            mike.say "Ooooooooookay."
    hide shawn
    return

label palla_event_12:
    $ palla.set_counter("pallavisit12", None)
    play sound door_bell
    "The doorbell rings."
    scene bg house
    show palla cry
    with wiperight
    "When I open the door, Palla is standing there. Her eyes are rimmed with red; she's been crying, though despite that her makeup is still perfect."
    palla.say "Hi, [hero.name]."
    mike.say "Palla, I was starting to think I wasn't ever going to see you again."
    "Palla raises a hand like she's going to say or express something with it, but then puts it down and looks away."
    mike.say "Do you want to come in?"
    palla.say "No."
    mike.say "Oh. What do you want, then?"
    show palla cry
    "Palla bursts into tears, as though I'd said something hurtful."
    mike.say "Palla?"
    "She starts to turn away. I know, I can tell, if I let her leave now, I'll never see her again."
    show palla sad at zoomAt(1.5, (640, 1040)) with hpunch
    "So I step forward and put my arms around her. She tries to push away, but I don't let her. I keep a firm hold around her shoulders as I pull her to me."
    "After a few seconds of token struggle, she relaxes and puts her head on my shoulders."
    mike.say "It's okay, Palla."
    show palla cry
    palla.say "No it's not!"
    mike.say "Fine, have it your way. Why isn't it okay?"
    palla.say "You're going to hate me."
    mike.say "I already hate you."
    with vpunch
    "Palla hits me gently in the arm, without actually letting go of me."
    show palla sad
    palla.say "Not funny."
    mike.say "Well, it doesn't hold a candle to holding the woman I love who's crying in the rain. But I liked it anyway."
    "Palla doesn't say anything."
    mike.say "I've missed you."
    palla.say "You have?"
    mike.say "Yeah. You're the only one who calls me an asshole and means \"I love you.\""
    show palla at zoomAt(1.65, (640, 1140))
    "Palla squeezes me a little more tightly."
    mike.say "Now, why again am I going to hate you?"
    palla.say "Because I'm not who you think I am."
    mike.say "You mean a beautiful, willful, amazing bitch that also happens to be mine?"
    palla.say "Okay maybe I'm those things, but..."
    "I sigh. I'm getting pretty tired of her beating around the bush here, but...I'm not lying. I did miss her, and I love having her in my arms right now."
    mike.say "You're not the incredibly successful, rich model you might have been telling everyone you are."
    "She makes a squeaky noise and presses her face into my shoulder."
    mike.say "Why do you think that's going to make me hate you?"
    "She doesn't answer again, but instead just sobs into my shoulder."
    mike.say "I don't hate you. I'm a little disappointed in you for lying to me, and a lot disappointed in you for not dealing with this like an adult. But I don't hate you."
    mike.say "And I'm not going to dump you, either. I still love you."
    "She pulls her face away from my shoulder, finally, and looks up at me. Rimmed with red and exhausted, she looks incredibly vulnerable like that."
    if palla.love >= 160:
        palla.say "I love you, too."
    mike.say "If you need help with--"
    palla.say "Don't say it."
    "I sigh and give her a little squeeze."
    mike.say "Fine, I won't say it, but it's still true."
    show palla normal
    palla.say "Thank you."
    "It clearly did not feel good for her to say that, but now that it's been said, we're past it."
    palla.say "I have to go. I'm sorry to have dumped this on you."
    mike.say "But Palla! I haven't seen you in like a week, and now you're leaving already?"
    palla.say "I have to take care of something. But I won't disappear again, I promise."
    mike.say "You'd better not."
    show palla blush
    "She puts one hand on my chest."
    palla.say "I love you, [hero.name]. I'm so, so lucky to have you. I'm sorry I'm such a dumb bitch."
    mike.say "You're not dumb! Don't ever say that about yourself."
    show palla happy
    palla.say "Fine. I'm sorry I'm such a bitch."
    mike.say "I doubt that you're remotely sorry about that, but I'll take it anyway. See you soon?"
    palla.say "Yes! See you soon."
    $ palla.unhide()
    hide palla
    return

label palla_event_13:
    show palla
    palla.say "Hey, [hero.name], we probably should talk. Can we go grab a coffee?"
    mike.say "Sure."
    $ game.room = "coffeeshop"
    scene bg coffeeshop
    show palla at center, zoomAt(1.5, (640, 1100))
    with dissolve
    "After we've ordered and we sit, Palla wraps her hands around her coffee cup, as though trying to warm them even though it's not cold in here."
    "She looks at me, but doesn't speak. I'm trying to be patient, but the suspense is killing me."
    mike.say "Okay, so what is it? Are we still not back in a good place?"
    palla.say "Oh, you and I are, absolutely. At least, I think we are. We are, aren't we?"
    mike.say "You tell me. You're the one who's been irrational."
    show palla annoyed
    "She bites her lip."
    palla.say "Damn it, I hate when you're right. Yes, yes you and I are in a good place. This isn't about us. This is about me."
    mike.say "What do you mean?"
    show palla normal
    palla.say "Okay, look. This...is harder for me to say than even makes sense. So I just...I guess I just need to rip the bandage off."
    palla.say "I haven't had a modelling job in something like two years."
    mike.say "I don't see what's so hard about that?"
    palla.say "I guess I shouldn't expect you to understand. You've got everything you've ever wanted. Me...the only thing I've ever wanted is this. Modelling is my dream. It's my life. And I thought it was working for awhile."
    show palla sad
    palla.say "And then it wasn't."
    mike.say "So you had to lie about it?"
    palla.say "I don't feel like I lied, really. I didn't tell you I was working at any given time, or how much money I made. Everything I told you about my career was true. Once. I just didn't...mention that I haven't been able to book new gigs."
    mike.say "Okay. I can see this really upsets you. I'm very sorry. Can you do--"
    "Palla holds her hand up and cuts me off."
    show palla normal
    palla.say "Oh no, don't play that white knight bullshit with me, [hero.name]. I'm not telling you this for you to fix it."
    mike.say "Okay, then what?"
    if palla.status == "girlfriend":
        palla.say "If we're going to be...you know, together, you're right, I have to tell you about these things. No matter how much it hurts."
    else:
        palla.say "Because we're close, [hero.name], and I have to be honest about these things. No matter how much it hurts."
    mike.say "I still don't understand, Palla. Why does it hurt so much?"
    show palla angry
    palla.say "Because I'm a failure, [hero.name]! I fuck up everything I ever do in life. My dad thinks I'm a useless cunt, and I guess he's right. I fucked up my career, and I'm trying so hard not to fuck up with you, okay?"
    palla.say "Every time I ever thought about telling you about this, I only ever had one reaction. How could anyone possibly want to be with a giant fucking failure like me?"
    show palla cry
    palla.say "So I didn't want you to know just how big of a failure I am."
    "When she stops talking, she's looking at me with a combination of fire and tears starting to form at the corners of her eyes, it seems really important that I say something smart. Something reassuring. Something charming, maybe."
    mike.say "Ah."
    "Yeah. Brilliant, inspiring, charismatic me, eh?"
    show palla annoyed
    palla.say "That's it? I'm baring my soul to you and that's all you have to say?"
    mike.say "No, it's not. I'm just...I'm taking it in. Look."
    "Quick! Brain! Give me good words here!"
    mike.say "First, you're not a failure."
    show palla angry
    palla.say "Oh fuck you, [hero.name], don't give me platitudes. I blew the one thing I ever really wanted. I have {b}nothing{/b}!"
    mike.say "You have me, right?"
    palla.say "This isn't about you, dipshit. Why do guys always make it about them?"
    "I sigh. Time for a different tactic."
    mike.say "Okay, fine, let's dig into your failure. Why exactly haven't you gotten a job in two years? You told me you're good at it."
    show palla normal
    palla.say "I am good at it."
    mike.say "But?"
    show palla blank
    palla.say "But...nobody will hire me."
    "I don't think I have to ask this, but I'm going to anyway."
    mike.say "Why?"
    palla.say "Let's see, the last one cited...what were the words he used? Personality conflict."
    mike.say "Or to put it bluntly, you're a fucking bitch."
    show palla annoyed
    palla.say "I'm not--Okay, fine. I'm a fucking bitch. Anyone who has a problem with that can fuck off."
    mike.say "It sounds like that's exactly what happened, Palla. They had a problem with it. They fucked off."
    show palla sad
    palla.say "I already tried being nicer."
    mike.say "How long did you manage it?"
    palla.say "Uh, an hour?"
    mike.say "Well, there you go."
    palla.say "Yeah."
    mike.say "So now what?"
    palla.say "I don't know. I can't pay the rent anymore. My credit is maxed out. I don't have anyone to borrow from. I already owe Shawn so much. I probably owe him at least a gratitude fuck. Or ten. Ugh."
    if palla.flags.minealone:
        mike.say "Oh no fucking way are you doing that."
    else:
        mike.say "He'd probably accept it."
    palla.say "So I don't know what to do now, [hero.name]. I really don't."
    mike.say "I could lend you--"
    show palla angry
    palla.say "Don't fucking even."
    mike.say "Damn, Palla. Will you swallow your fucking pride for a minute?"
    show palla normal
    palla.say "It's not pride. Lending me the money isn't a long term solution. Maybe I need to move to another city, one where I haven't burned all the bridges."
    mike.say "Okay, I know you said you don't want me to fix it, but please? There has to be a way I can help."
    palla.say "Can you hire me? Get me a job?"
    mike.say "Well, I might have some contacts. What if...well, I can make some phone calls and see. I can be your agent. I can float your rent until you get back on your feet, and then you can pay me back."
    show palla blank
    "Palla doesn't look convinced."
    palla.say "My agent, huh? How would that work? I don't want to be your charity case, [hero.name]."
    mike.say "Well, you pay agents, right?"
    palla.say "I can't pay you."
    mike.say "I'd say you're paying me already."
    show palla annoyed
    palla.say "I'm not a prostitute, [hero.name]."
    mike.say "Fine. Don't agents take a cut after you get paid? So no work, the agent gets nothing, right? But I get you work, and I get paid too. Plus I get to keep you around as a nice bonus."
    "Palla looks down at the coffee she hasn't taken so much as a sip of, which is now cold."
    show palla normal
    palla.say "Okay. I...I'll think about it."
    mike.say "Okay. But don't think about it so long that you get kicked out and end up homeless."
    palla.say "I guess. I can always give Shawn what he wants. That'll work for awhile."
    mike.say "First, you already said you're not a prostitute, and second, Shawn is having money troubles too."
    show palla sad
    "Palla looks guilty."
    palla.say "Well. Fuck."
    mike.say "So?"
    show palla normal
    palla.say "Give me a day or two to think about it. I'll call you."
    $ palla.flags.pallav14delay = TemporaryFlag(True, 2)
    mike.say "Okay, you do that."
    hide palla
    show palla
    "Palla stands up and pushes aside the coffee."
    palla.say "I love you, [hero.name]. Thanks for...well. This."
    return

label palla_event_14:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    "When I answer my phone, it's Palla."
    palla.say "Hey, [hero.name]. I've given some thought to what you said about being my agent. Are you still willing to do that?"
    menu:
        "Let's do it!":
            mike.say "Yeah! Together we can turn your life around, I think."
        "I've changed my mind":
            mike.say "I've changed my mind. I don't think I'd do a good job."
            palla.say "Oh. My only other option is to move to another city and start over, I think. Are you sure? I don't really want this to be it, but..."
            menu:
                "Okay, I'll do it":
                    mike.say "Okay, I don't want to lose you. I'll do it, and we'll hope for the best."
                "I guess this is goodbye":
                    mike.say "Wow. I can't believe you're just going to leave."
                    palla.say "My career is the only thing that matters to me."
                    mike.say "More than me?"
                    palla.say "[hero.name], I love you. I love you so much. But my career is more important than love. Flat out. I'm sorry it has to be this way."
                    mike.say "Yeah, me too."
                    palla.say "I have to do this quickly, so I don't cry. I'll miss you. I'm sorry."
                    "And then she hangs up."
                    $ palla.set_gone_forever()
                    return
    palla.say "Okay. You're my agent now. You work for me! Go get me a job!"
    mike.say "You're so demanding!"
    "I can manage Palla's career in the smartphone now."
    $ palla.flags.career = True
    $ palla.flags.managecareer = True
    $ palla.flags.jobexpenses = 125
    $ palla.flags.jobloan = 5000
    $ palla.flags.jobloanmax = 125
    return

label palla_event_baby_ok:
    show palla
    palla.say "Hey, [hero.name]...do you still want me to...um. It's hard to say. Do you want me to have...your, um. Baby?"
    menu:
        "Of course!":
            mike.say "Yes, I want you to have my baby!"
        "I'm content":
            mike.say "I'm content with just having you."

    palla.say "Well, I just. Look if you ask me to go off the pill again, I might...answer differently. I might. No promises. Okay?"
    $ palla.flags.babyok = True
    hide palla
    return

label palla_preg_talk:
    show palla
    palla.say "Hey, [hero.name]!"
    "Palla's expression is a weird mix of a smile and trepidation."
    mike.say "Hi, Palla. How're you doing today?"
    palla.say "Well, you know how I agreed to go off the pill? And we, ah. You know."
    mike.say "Sure. I. Oh! You mean? It happened?"
    show palla happy
    palla.say "It happened."
    mike.say "And you're sure you're okay with it?"
    palla.say "Well. I...I'm not sure. But."
    show palla normal
    "She puts her hands on my chest and looks me directly in the eyes."
    palla.say "I love you."
    if palla.love >= 160 or palla.sub >= 80:
        palla.say "I love you so much, I'll do anything for you. Even this."
    palla.say "So. So [hero.name], do you still want me to do this? It's...going to be a big change. A child. My child. You have to help me not fuck it up. right?"
    palla.say "You have to promise, {b}promise{/b} me that you'll make sure we're better parents than mine. Okay?"
    menu:
        "We'll be great parents":
            mike.say "Yes, my love. You'll be a great mother, and I'll be with you the whole way. This will be our child."
            show palla blush at zoomAt(1.5, (640, 1040))
            "Palla throws her arms around me and buries her head into my shoulder."
            show palla happy
            palla.say "I love you so much!"
            $ palla.flags.toldpreg = True
        "This is too much for you, let it go":
            mike.say "I understand. I've pushed you into something you don't {b}really{/b} want, haven't I? Am I being selfish?"
            show palla sad
            palla.say "No, [hero.name], you're not being selfish. I'm the one being selfish. I'm sorry. I want...you to be happy."
            mike.say "And I want you to be happy. Will you be truly happy with this?"
            "Palla looks at me and there are tears in her eyes."
            show palla cry
            palla.say "I'll be happy if it makes you happy."
            mike.say "That's not good enough. I want you to be happy too. That's what matters the most. Look, maybe we can talk about this again another time. Maybe you'll be ready later."
            palla.say "And if I'm not? If it's something I'll do for you, but not for me, will that be enough for you?"
            mike.say "It will have to be enough for me."
            "Palla sniffles, and starts to cry."
            palla.say "Okay, then. I'll...take care of this."
            $ palla.unpreg()
    hide palla
    return

label palla_birthday_date_male:
    $ DONE["palla_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg mall1
    show palla casual
    with fade
    "The mall's not usually the kind of place that I take a girl on a date."
    "Firstly because, to me at least, it's not really a romantic spot."
    "And secondly because it's one of those places that drains your wallet pretty quickly."
    "But then you could say the latter about Palla too."
    "So maybe that explains why I actually chose to bring her here."
    "And so far, it seems to be working out pretty well."
    "Palla's flitting from one store window to another."
    "And she seems to be in her element, which is great."
    show palla happy
    palla.say "This was such a great idea, [hero.name]."
    palla.say "Instead of just going to a restaurant or seeing a film."
    palla.say "We're doing something really exciting instead."
    show palla normal
    palla.say "Don't you think?"
    menu:
        "Be falsely enthusiastic":
            "This was my idea after all."
            "And I know that it was all to please Palla."
            "But I should probably try to sound happy about it too."
            mike.say "Yeah, Palla..."
            mike.say "There's so much choice and variety here at the mall."
            mike.say "You can just go crazy and let your creativity take over."
            show palla happy
            "Palla seems delighted with my answer."
            "Because she nods and pulls me towards the next store window."
            $ game.active_date.score += 10
            palla.say "That's right, [hero.name]!"
            palla.say "I knew that you'd understand."
            palla.say "And I know this is going to be a great birthday too!"
        "Be honest with her":
            "This was my idea, sure."
            "But the whole point was to please Palla."
            "And I'm cool with doing something out of my comfort zone."
            "As long as it makes her happy."
            mike.say "It's not really my kid of thing, Palla."
            mike.say "But I wanted to make you happy on your birthday."
            mike.say "So as long as you're having a good time."
            mike.say "That's what makes me happy."
            "Palla nods at this."
            "But I can tell that she's not totally happy with my answer."
            palla.say "Oh..."
            palla.say "Okay then."
            palla.say "I guess that makes sense."
    show palla normal
    "The conversation soon seems to be forgotten however."
    "As the contents of the next window attract Palla's attention."
    show palla surprised at startle
    palla.say "Oh wow!"
    palla.say "I heard all about the new collection they have here."
    palla.say "It's supposed to be perfect for this season."
    show palla normal at right4 with ease
    palla.say "Come on - we need to look inside!"
    hide palla with easeoutright
    "Before I can say a word in response, Palla darts inside."
    "Which leaves me without any choice but to follow."
    scene bg clothesshop
    show palla normal at left
    with fade
    "As soon as she's in the store, Palla starts to browse."
    "She's studying the clothes on the rails in minute detail."
    "Holding them up against herself to see how they look."
    palla.say "Hmm..."
    palla.say "I really like this one, [hero.name]."
    palla.say "But I wonder if this one is a better match for my eyes..."
    palla.say "What do you think?"
    menu:
        "Choose the first one":
            "I have no idea which of the two is a better match."
            "So I just choose the first and hope for the best."
            mike.say "The first one, Palla."
            mike.say "I think that matches your eyes best."
            show palla surprised
            "Palla looks at me in surprise."
            "And then she shakes her head."
            $ game.active_date.score -= 10
            show palla annoyed
            palla.say "Urgh..."
            palla.say "I should have known better than to ask you!"
            palla.say "Now I can't decide myself."
            palla.say "So I'll just have to get both!"
        "Choose the second one":
            "I have no idea which of the two is a better match."
            "So I just choose the first and hope for the best."
            mike.say "The second one, Palla."
            mike.say "I think that matches your eyes best."
            show palla surprised
            "Palla looks at me in surprise."
            "And then she shakes her head."
            $ game.active_date.score -= 10
            show palla annoyed
            palla.say "Urgh..."
            palla.say "I should have known better than to ask you!"
            palla.say "Now I can't decide myself."
            palla.say "So I'll just have to get both!"
        "It's too hard to choose one or another":
            "I have no idea which of the two is a better match."
            "So I decide that honesty is the best policy."
            mike.say "You know what, Palla..."
            mike.say "They both look great on you."
            mike.say "So I couldn't possibly choose one over the other."
            show palla surprised
            "Palla looks at me with surprise."
            "But there's approval in there as well."
            show palla normal
            $ game.active_date.score += 15
            "She nods and smiles."
            palla.say "You're right, [hero.name]!"
            palla.say "They do both suit me."
            show palla happy
            palla.say "So the logical solution is to get them both!"
            show palla normal
            palla.say "Maybe your fashion sense is improving."
    show palla normal
    "With her intended purchases over her arm, Palla heads for the checkout."
    "And there she hands them over to the girl working behind the till."
    "I watch as the prices pop up on the screen, amazed they can cost so much."
    "But then I suppose that Palla's got an image to maintain."
    "And she can't do that by buying stuff at bargain basement prices."
    "Sales assistant" "That's going to be two hundred and fifty dollars."
    "Sales assistant" "Will that be cash, or card?"
    "Palla chuckles and nods in my direction."
    show palla wink
    palla.say "Do you accept boyfriends?"
    show palla flirt
    "The girl laughs, and now she's looking at me."
    "Wait a minute..."
    show palla normal
    "Palla's expecting me to pick up the bill for her?!?"
    menu:
        "Be nice, take the bill" if hero.money >= 250:
            "I feel like Palla's being pretty entitled to expect me to pay."
            "But perhaps some of this is on me too."
            "I mean, maybe I should have laid down some ground-rules beforehand?"
            "That way we could have avoided an awkward situation like this one."
            mike.say "Okay, Palla..."
            show palla happy
            mike.say "Let me get that for you..."
            "I pay the bill, feeling an almost physical pain as I do so."
            "And all the time I try to keep a smile on my face."
            "My reward for all of this is Palla smiling as we walk out of the place."
            scene bg mall1
            show palla happy casual
            with fade
            $ game.active_date.score += 15
            palla.say "Thank you, [hero.name]."
            palla.say "It's so nice to be with a guy that's generous."
            palla.say "It makes liking you so much easier!"
            "I nod and smile, trying to tell myself that's a good thing."
            "And not that it makes me sound like a complete patsy."
            $ hero.money -= 250
        "No way girl, I'm not paying":
            "I don't even have to think about my answer for a second."
            "Just how entitled is Palla to assume I'd pay for her shopping?"
            "There's no way I'm going to do that!"
            mike.say "Don't look at me, Palla!"
            show palla surprised at startle
            mike.say "If you want them, you buy them yourself."
            scene bg mall1 with fade
            "I make a point of walking out of the store as soon as I'm done."
            "More for the sake of avoiding an argument than anything else."
            show palla annoyed casual at center with moveinright
            "And when Palla joins be a few minutes later, she doesn't look pleased."
            show palla angry casual at startle
            palla.say "[hero.name]!"
            palla.say "How could you embarrass me like that?"
            mike.say "No way, Palla!"
            mike.say "You did that to yourself."
            mike.say "You can't just assume I'm going to buy you random shit!"
            $ game.active_date.score -= 10
            show fx anger
            palla.say "It's my birthday, [hero.name]!"
            palla.say "I thought you were supposed to be making it special?"
            hide fx
            "We walk off deeper into the mall."
            "But Palla's still sulking as we do so."
    show palla normal
    "I take a quick glance at the time, and then I nod."
    "It's just about time for the surprise I have for Palla."
    "Luckily for me, my plan's working out perfectly."
    "Because we're pretty much right outside the unit where we need to be."
    mike.say "Surprise, Palla!"
    mike.say "I hope you're ready to pose like a pro?"
    show palla surprised blush
    "Palla looks confused at this."
    show fx question
    palla.say "What are you talking about?"
    palla.say "Can you try to make sense for a change?"
    "I point towards the door of the unit we're standing in front of."
    mike.say "I booked you a surprise photo-shoot here, Palla!"
    mike.say "So you can have some nice shots to add to your portfolio."
    mike.say "Great idea, huh?"
    show palla mindless
    "Palla nods slowly, looking more than a little stunned."
    "I guess she's not used to me encouraging her like this."
    scene bg photostudio
    show palla normal
    with fade
    "Inside the studio, the photographer fusses over Palla."
    "And she seems to appreciate the treatment too."
    "It's not long before she's getting ready for the shoot."
    hide palla
    $ randevent = randint(1, 3)
    if randevent == 1:
        "It seems like the photographer's ready to go."
        show palla sad casual
        "But Palla comes hurrying over to me."
        "She's looking oddly self-conscious right now."
        show palla sad close
        "And she leans in close to whisper to me."
        palla.say "I..."
        show palla annoyed blush
        palla.say "I don't think I can do this!"
        palla.say "Normally I have more time to prepare."
        "At first I don't know what to say."
        "I'm just not used to Palla showing a lack of confidence."
        "But then I realise that she needs me to be strong."
        "And so I do the best I can to reassure her."
        if hero.charm >= 50:
            mike.say "You don't need time to prepare, Palla."
            mike.say "You're a natural!"
            mike.say "I mean, look at how eager the photographer is to get going."
            show palla surprised
            "Palla blinks in surprise and follows my own gaze."
            palla.say "Oh..."
            palla.say "You really think so?"
            mike.say "Of course I do, Palla!"
            mike.say "This guy must be sick of shooting awful families and their snotty kids."
            mike.say "With you, he's getting to shoot a genuine model!"
            $ game.active_date.score += 15
            show palla normal
            "Palla nods, seeming to gain confidence with every second that passes."
            show palla -close
            "She strides over to where the photographer is waiting."
            with screenshot
            play sound cameraclick
            pause 0.2
            with screenshot
            play sound cameraclick
            "And soon the place is filled with the flash and click of the camera."
        else:
            mike.say "What's the big deal, Palla?"
            mike.say "Just fake it, yeah?"
            mike.say "I mean sure, you've looked better."
            mike.say "But what have you got to lose?"
            show palla sad
            "Palla listens to what I have to say."
            $ game.active_date.score -= 10
            "But her face seems to fall with every word."
            show palla -close
            "And by the time I'm done, she's in an even worse state than before."
            hide palla with moveoutright
            "Without another word, she gathers up her things and heads out the door."
            "And I follow her, shrugging an apology to the photographer as I go."
    elif randevent == 2:
        "I'm starting to feel a little hot in the studio."
        "So I decide to strip down to my T-shirt as I wait for Palla."
        "I notice that the photographer's looking my way as I do so."
        "And the fact that he's kind of staring makes it a little awkward."
        if hero.fitness >= 50:
            "Peeling off my T-shirt, I feel my muscles are a little cramped."
            "So I quickly run through some of the exercises I was taught at the gym."
            "This seems to do the trick, and my body relaxes nicely."
            show palla normal casual
            "It's just then that I see Palla's looking at me too."
            "She and the photographer seem to be discussing something."
            show palla happy
            "Then she hurries over and gives me a knowing smile."
            palla.say "[hero.name]..."
            palla.say "How would you like to be in the shoot with me?"
            mike.say "Be in the shoot?"
            mike.say "With you?"
            palla.say "That's what I said!"
            show palla normal
            palla.say "The photographer thinks we'd look great together!"
            mike.say "Erm..."
            $ game.active_date.score += 15
            mike.say "Okay, Palla - if that's what you want."
            show palla happy close
            "Palla takes me by the wrist and leads me over to the set."
            palla.say "Just follow my lead, okay?"
            "She strides over to where the photographer is waiting."
            "I follow, vowing silently to do the best I can."
            with screenshot
            play sound cameraclick
            pause 0.2
            with screenshot
            play sound cameraclick
            "And soon the place is filled with the flash and click of the camera."
        else:
            "I groan as I heave off what I have on over my T-shirt."
            "And then I let out a sigh of relief as I finally get it over my head."
            "Sitting down on a bench, I feel everything relax and begin to sag."
            "But I still can't help letting out a rasping cough as my body settles."
            "Urgh..."
            "I really need to spend more time down at the gym!"
            "I'm starting to ache just from standing up and walking around."
            "But one thing that I do notice is that the photographer's stopped staring at me."
            "In fact, he seems to be making a conscious effort to look the other way."
            show palla angry casual
            palla.say "[hero.name]!"
            palla.say "Sit up straight, why don't you?"
            show palla annoyed
            palla.say "And for god's sake, suck your gut in!"
            $ game.active_date.score -= 10
            palla.say "You're bringing down the tone of the place!"
            "I do the best I can to satisfy Palla."
            "And she nods, seemingly placated by my efforts."
            "She strides over to where the photographer is waiting."
            with screenshot
            play sound cameraclick
            pause 0.2
            with screenshot
            play sound cameraclick
            "And soon the place is filled with the flash and click of the camera."
    else:
        "I find myself looking around the place as Palla gets ready."
        "And I notice that the studio is pretty much private."
        "There's no way anyone could see in from outside in the mall."
        "Next I take a closer look at the shots on the walls."
        "Most of them are typical shots of families and girls posing."
        "But then I see some a little out of the way that are different."
        "And I mean different in that there's a lot more flesh on show!"
        "Don't get me wrong, they're not pornographic in nature."
        "More what you'd describe as tasteful shots of girls posing in swimsuits and underwear."
        show palla close casual
        palla.say "What are you staring at, huh?"
        "I jump a little as Palla sneaks up on me."
        "But I try my best to look innocent."
        "Because it's pretty obvious what I'm looking at right now."
        mike.say "Oh, nothing..."
        mike.say "Just this guy's more adventurous stuff, you know?"
        if hero.is_lucky:
            show palla angry
            "Palla shoots me a knowing glance."
            show palla normal
            "And she smiles slowly."
            palla.say "You know what, [hero.name]..."
            palla.say "You were the one behind all of this."
            palla.say "So maybe you deserve a little something in return..."
            show palla -close
            "With that, Palla strides off towards the set."
            "I watch her go with interest."
            "And I see her chatting to the photographer."
            "He nods, and then to my amazement, I see Palla getting undressed!"
            show palla underwear with dissolve
            pause 0.2
            with screenshot
            play sound cameraclick
            pause 0.2
            with screenshot
            play sound cameraclick
            "She strips down to her underwear, and then the shoot gets underway."
            with screenshot
            play sound cameraclick
            "I stare and gape the whole time, watching Palla preen and pose."
            "And when it's all over, I still can't believe what just happened."
            show palla close casual with dissolve
            "Dressed again, Palla walks back to me, still smiling."
            palla.say "Don't worry, [hero.name]..."
            $ game.active_date.score += 15
            show palla happy
            palla.say "I'll make sure you get a copy of the shots!"
        else:
            show palla angry
            "Palla shoots me a knowing glance."
            "And she shakes her head."
            show palla annoyed
            palla.say "Well enjoy looking, [hero.name]."
            show palla angry
            palla.say "Because my shoot's not going to be one of those!"
            "I open my mouth, thinking that I might change Palla's mind."
            "But then I see the look in her eyes."
            "And I know that the subject's not open to debate."
            mike.say "Okay, Palla..."
            mike.say "Enjoy yourself and have fun."
            mike.say "Break a leg, or whatever!"
            show palla normal
            "Palla nods, and I take that as notice the conversation is over."
            show palla -close
            "She strides over to where the photographer is waiting."
            with screenshot
            play sound cameraclick
            pause 0.2
            with screenshot
            play sound cameraclick
            "And soon the place is filled with the flash and click of the camera."
    scene bg black with timelaps
    scene bg mall1
    show palla normal casual
    with timelaps
    "With the photoshoot over, I feel the need to ground myself in reality."
    "And there's nothing more ground than a good cup of coffee!"
    "Apologies for the pun..."
    scene bg coffeeshop
    show palla normal casual at center, zoomAt(1.5, (640, 1140))
    with fade
    "But anyway, I order an Americano."
    "And Palla chooses something that I can't even begin to describe."
    palla.say "A double-thin, half-fat, super-slim mecha-mocha..."
    palla.say "With soy milk and a swirl of Guatemalan cinnamon, please!"
    "When Palla's drink turns up, I can't tell how she's supposed to drink it."
    "But that doesn't seem to be her primary concern."
    "As she instantly takes out her phone and starts to photograph it!"
    menu:
        "Take your phone out and do the same":
            "I guess Palla's one of those people that posts her entire life online."
            "And that's kind of the point of ordering a ridiculously over the top coffee."
            "Taking a glance at my own rather plain drink, an idea occurs to me."
            "I pull out my own phone and snap a few pictures too."
            show palla happy
            "This catches Palla's attention, and she seems amused."
            $ game.active_date.score += 15
            show palla joke
            palla.say "Oh, [hero.name], you silly thing!"
            palla.say "At least sprinkle some cinnamon on the top."
            show palla normal
            palla.say "And remember to use a filter too!"
            mike.say "Really, Palla?"
            mike.say "You think that would work?"
            show palla joke
            "Palla looks thoughtful for a moment."
            "Then she gives me a slight nod."
            show palla normal
            palla.say "Well..."
            palla.say "You might get some points for the Spartan aesthetic."
            palla.say "But I wouldn't hold my breath!"
        "Ask her if she's gonna drink it at some point":
            "I guess Palla's one of those people that posts her entire life online."
            "And that's kind of the point of ordering a ridiculously over the top coffee."
            "This really is a new high in terms of pretentiousness, even for her!"
            mike.say "Are you actually going to drink that, Palla?"
            mike.say "Or just take pictures of it until it goes cold?"
            show palla annoyed
            "Palla rolls her eyes and shakes her head."
            palla.say "Of course I'm not going to drink it, [hero.name]!"
            palla.say "These things taste utterly vile."
            show palla normal
            palla.say "But they're on trend at the moment."
            palla.say "So I need to be seen to be ordering them."
            mike.say "That's the most stupid thing I ever heard, Palla!"
            mike.say "What a waste of money, and good coffee too!"
            show palla blank
            $ game.active_date.score -= 10
            "Palla snorts and looks down at me with disdain."
            palla.say "Well, I wouldn't expect you to understand."
            palla.say "Not when you drink Americanos, like a caveman!"
    show palla normal
    "Palla finally puts away her phone and drums her fingers on the table."
    "This causes me to do the same, sensing that it would be wise to do so."
    palla.say "So..."
    palla.say "Today IS my birthday..."
    mike.say "That's right, Palla."
    palla.say "And that would mean you have something for me, right?"
    if not hero.has_gifts:
        "It's pretty forward of Palla to do that."
        "To just come right out and ask for her birthday present!"
        "The only problem is that I didn't get her one."
        "But maybe I can talk my way out of this..."
        mike.say "You mean a present, Palla?"
        mike.say "But all of this is your present!"
        mike.say "All of the stuff we've been doing today."
        "I smile, making it plain that I'm not joking."
        "And it seems to be enough to mollify Palla."
        show palla sad
        $ game.active_date.score -= 20
        $ palla.love -= 10
        palla.say "Oh..."
        palla.say "I see..."
        palla.say "I suppose you're right."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_15
        if _return != "done":
            if _return not in ["None", "exit"]:
                "It's pretty forward of Palla to do that."
                "To just come right out and ask for her birthday present!"
                "But it does provide the perfect opportunity to hand it over."
                mike.say "Of course I do, Palla."
                mike.say "Here you go!"
                "Palla's face lights up as I hand over the gift."
                play sound [paper_ripping_2, paper_ripping_1]
                "And she doesn't hesitate to tear of the paper."
                "Within moments, she's pulling it out of the box."
                if _return:
                    show palla surprised blush
                    "The moment she sets eyes on it, Palla seems amazed."
                    palla.say "Oh, [hero.name]..."
                    $ game.active_date.score += 15
                    show palla happy
                    palla.say "It's perfect!"
                    palla.say "How did you know?"
                    mike.say "Oh, I just kept my ears open for hints."
                    mike.say "And it looks like all the effort paid off!"
                    show palla normal
                    "Palla nods, and then plants a kiss on my lips."
                else:
                    show palla blank
                    "The moment she sets eyes on it, Palla looks disappointed."
                    "Another girl might have tried harder to hide the fact."
                    "But not Palla - she just stuffs it back into the box."
                    mike.say "Erm..."
                    mike.say "Is there a problem, Palla?"
                    $ game.active_date.score -= 10
                    show palla annoyed
                    palla.say "It's not really what I wanted."
                    palla.say "But I suppose you tried your best..."
            else:
                "It's pretty forward of Palla to do that."
                "To just come right out and ask for her birthday present!"
                "The only problem is that I didn't get her one."
                "But maybe I can talk my way out of this..."
                mike.say "You mean a present, Palla?"
                mike.say "But all of this is your present!"
                mike.say "All of the stuff we've been doing today."
                "I smile, making it plain that I'm not joking."
                "And it seems to be enough to mollify Palla."
                show palla sad
                $ game.active_date.score -= 20
                $ palla.love -= 10
                palla.say "Oh..."
                palla.say "I see..."
                palla.say "I suppose you're right."
    hide palla
    show palla normal casual
    "Soon enough I've finished off my coffee and Palla's has gone cold."
    "So it looks like the time has come to call an end to our date."
    "I push back my chair and begin to stand up."
    show palla at center, zoomAt(1.4, (640, 1000)) with move
    show palla at center, traveling (1.2, 0.5, (640, 840))
    "Palla does the same, but doesn't seem to be about to ask a question."
    "You know - the obvious question?"
    "So I guess I'll have to do it myself."
    mike.say "So..."
    mike.say "You ready to call it a day, Palla?"
    if game.active_date.score >= 80 and palla.sexperience >= 1:
        "Palla shakes her head."
        "And the gesture fills me with hope."
        show palla flirt blush
        palla.say "I was going to suggest we do something else, [hero.name]."
        palla.say "Maybe go somewhere there's less people?"
        palla.say "I've had such a good time today."
        show palla wink
        palla.say "It'd be a shame to end it now."
        show palla normal
        "I nod eagerly, trying to hide my enthusiasm just a little."
        mike.say "Me too, Palla!"
        mike.say "Let's go see where we end up, okay?"
        "With that, I pay the bill and we leave together."
        call palla_birthday_sex from _call_palla_birthday_sex
    else:
        "Palla nods and then adds a yawn for good measure."
        palla.say "Yeah..."
        show palla blank
        palla.say "I'm feeling pretty tired."
        palla.say "And I have an early start in the morning."
        "I nod, trying not to let my disappointment show."
        mike.say "Ah..."
        mike.say "Okay, Palla."
        mike.say "Should I call you?"
        show palla normal
        palla.say "Oh no, [hero.name]."
        palla.say "I'll call you."
        "I nod again and add a smile."
        "Hoping to get that call sooner, rather than later."
    return

label palla_birthday_sex:
    scene bg mall1
    show palla normal casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "As we leave the coffee-shop, I'm already thinking about how to get back to my place."
    "Palla's made it pretty clear that she's not ready for our date to come to an end just yet."
    "And from the way she's hanging off my arm, I know exactly what she has in mind too!"
    "I'm wondering if she can hang on in there until we're safely in my bedroom."
    "But that's when she throws me a curve-ball!"
    scene bg publicbathroom
    show palla normal casual at center, zoomAt(1.5, (640, 1040))
    with hpunch
    "As we pass the bathrooms on the way out of the mall, Palla pulls me inside the ladies!"
    "This takes me completely by surprise, as I didn't think she was that kind of girl."
    "And my state of shock means that I'm bundled into one of the cubicles before I know it!"
    scene bg publicbathroom at center, dark
    play sound door_slam
    show palla flirt blush at center, zoomAt(1.75, (640, 1180))
    with hpunch
    "Palla shoves me down onto the toilet as she slams the door closed behind us."
    mike.say "Whoa..."
    mike.say "Palla, I..."
    "Palla shakes her head and puts finger to her lips."
    "Which I assume means that she wants me to shut the hell up."
    "So I close my mouth and nod, letting her know that we're on the same page."
    "I lean back as Palla leans forwards and over me."
    "She doesn't stop to ask permission even for a moment."
    "Instead she quickly unzips my flies and slides her hand inside."
    "I gasp as she grabs hold of my cock and begins to pull it out."
    "At the same time her other hand is reaching to pull down her own panties."
    "Needless to say, what Palla's doing is enough to make me start to get hard."
    "And she adds to this by squeezing and stroking too."
    "It doesn't look like she's planning on stopping to ask me what I want out of this."
    "But from how it's started out, I'm pretty sure that I'll like where it's going."
    "So I'm happy to lie back and let Palla have her way with me."
    hide palla
    show palla stand cabin pleasure dick
    with fade
    "Slowly, she starts to lower herself onto my lap."
    "Her free hand is braced against one wall of the cubicle."
    "And the other makes sure my cock is positioned just so."
    "The first time her pussy touches the tip of my cock, I shudder with anticipation."
    "Palla seems to interpret this as fear, and she looks back over her shoulder at me."
    "The expression on her face is a mixture of sympathy and amusement."
    "But that doesn't stop her from doing it again, enjoying the chance to torture me."
    "Palla does it perhaps half-a-dozen times more, longer and slower each time."
    "And then I feel like I can't take anymore."
    "Either I need it to stop, or I need even more than she's giving me."
    "That's why my hands shoot up a moment later, taking hold of Palla around the waist."
    show palla stand normal
    "She lets out a yelp of alarm, wriggling in my grasp."
    "But that's all she gets the chance to do."
    "As the very next second, I pull her firmly downwards."
    "There's nothing Palla can do to resist me."
    show palla stand wet
    "And on top of that, she's been getting off on her antics too."
    "That means her pussy is warm and slick, anticipating what comes next."
    "And it doesn't put up much resistance as gravity comes into play either."
    show palla stand nodick ahegao
    "Palla moans as she starts to sink down onto my cock."
    "But there's nothing she can do that wouldn't make too much noise."
    "And the last thing she wants is to be caught fucking in the bathroom by mall security."
    "So she has no choice but to surrender herself to me."
    show palla stand normal
    "All the time I'm pulling her down too, filling ever more of her with my cock."
    "I feel empowered by the sensation of holding Palla in my hands."
    "And it makes all of the expense of her birthday seem worth it."
    "In fact, I'm starting to feel like this is the pay-off."
    "Like I'm recouping every penny as I start to fuck her."
    "Back in the mall, I was following Palla around from store to store."
    "Almost scuttling after her like a well-behaved little lap-dog."
    "But now the roles are well and truly reversed."
    show palla stand ahegao
    "And she's bouncing up and down on my cock like an obedient little bitch!"
    "Palla really does seem to be helpless in my hands too."
    "I make a point of sliding them all over her body."
    "Caressing and squeezing wherever and whatever I please."
    "And the only result is that she moans louder, nodding her head to beg for more!"
    "It's only when Palla collapses back against me that I realise she's speaking."
    "With her head resting on my shoulder, I can hear the sound of her whispering."
    "It's faint, but unmistakable."
    "So I strain to hear what she's actually saying."
    palla.say "Oh..."
    palla.say "Oh fuck..."
    show palla stand pleasure
    palla.say "Harder, please..."
    palla.say "Fuck me harder..."
    "Well now I can't do anything other than that, can I?"
    "What the lady wants, the lady gets!"
    "Making sure I have a firm hold on Palla, I get ready to give her what she's asking for."
    show palla stand ahegao
    "And then I start to thrust upwards and into her from below."
    "Using every last ounce of my strength, I'm pounding her without mercy."
    "I try to get as deep as physically possible each time too."
    "And I'm only satisfied when my cock can't go any further."
    "Palla's response to this is pretty dramatic."
    "She wriggles and writhes on my lap, squirming the whole time."
    "At first I think she's trying to break free of my grasp."
    "But then I realise that the opposite is true."
    "She's actually trying to push herself down as hard as she can!"
    "Unable to do anything else, Palla soon begins to grab at her own body."
    "At first she rubs the edges of her pussy with both hands."
    "But this doesn't seem to do enough, and she gasps in frustration."
    "Then her hands settle upon her chest, one on each breast."
    "And here she seems to find a more effective form of release."
    "Palla massages her own breasts, putting on quite a show for me."
    "The tips of her fingers begin to pinch and squeeze at the nipples."
    "And I watch as they stiffen visibly from the attention."
    "But she's not being gentle on herself by any means."
    "Palla's fingers leave red imprints on the skin of her breasts."
    "And her nails scratch at them too, threatening to raise actual blood!"
    "All of this is rapidly becoming too much for me to handle."
    "So when I hear Palla whispering for a second time, I can guess what's on her mind."
    palla.say "H...hold onto me..."
    palla.say "I'm...going to..."
    "Palla doesn't get to finish, because it happens a second later."
    "Only I'm not sure which one of us actually cums first!"
    show palla stand cum with hpunch
    $ palla.sexperience += 1
    "I can feel myself losing it at the same time as Palla's pussy squeezing me."
    with hpunch
    "This means that I shoot my load and she squirm from her orgasm at together."
    with hpunch
    "And I really do have to cling onto her to keep us both from falling off the seat!"
    "I'd like to lie there a lot longer, but the reality of our situation soon sets in."
    scene bg publicbathroom
    show palla casual
    with fade
    "As soon as we're able, Palla and I make ourselves decent."
    scene bg street
    show palla casual
    with fade
    "Then we slip out of the bathroom and leave the mall."
    "The whole time still buzzing from the excitement of what we just did together."
    scene bg black with dissolve
    call sleep from _call_sleep_68
    $ game.room = "bedroom1"
    return

label palla_mall_date_fuck:
    $ hero.replace_activity()
    scene bg clothesshop
    show palla
    "I don't know why I thought taking Palla on a shopping spree would be a good idea. I hate shopping and the mall at the best of times, but with Palla, it's a whole new kind of annoying."
    "Normally Palla doesn't have any patience, but when it comes to clothes, she seems to want to prove it by visiting every single high-end clothes store in the mall."
    "And if I think my patience is tested by her, her treatment of the employees is condescending at best and more like outright disdain."
    "Palla makes a point of being as awkward and demanding as she can without overstepping the mark and being openly rude and abusive."
    hide palla with moveoutright
    "After what seems like hours, I find myself standing outside one of the curtained-off changing rooms in a store the name of which I can't hope to recall."
    "Palla's been inside for three seconds shy of forever, apparently trying to piss off the entire staff of the place by sending them off for endless changes in size and color of the clothes she's only thinking about being interested in buying...maybe."
    "After a while it begins to become apparent that she's succeeded, as none of the girls that she's dispatched to the shop floor seem to be returning."
    palla.say "[hero.name], where the hell are those useless little cows?"
    palla.say "The store's not that big, and the morons work here, how can they get lost?!?"
    mike.say "I don't know...maybe you finally managed to work them to death."
    mike.say "Or maybe they got buried under an avalanche of this season's most trending clothes?"
    palla.say "Ha, ha, very funny."
    palla.say "If there's one thing I hate, it's shitty customer service!"
    "She mutters and complains to herself for a few more moments, and then seems to come to a conclusion of some kind."
    palla.say "Well, if they're not coming back, you'll just have to make yourself useful and go fetch me what I need."
    "Before I can even begin to protest, she thrusts a handful of clothes around the side of the curtain."
    palla.say "I want these in a size larger, the first in fuchsia, the second in puce and the third in azure blue, NOT ultramarine blue."
    palla.say "You got all of that, huh?"
    mike.say "Yes, I got it."
    "I snatch the proffered items and take the chance to walk away for a couple of minutes."
    "What the fuck is fuchsia or puce? And how is azure blue different from...whatever the fuck she said?"
    "Out on the shop floor, I wander around pretending to look for what Palla wants, getting progressively more annoyed that this is what our date has turned into."
    "I try to recall how I dealt with it the last time -- and then it comes back to me suddenly, and I know what I'm going to do about it now too."
    "Hastily shoving the clothes rejected by Palla onto the nearest rack, I grab three more items at random, just to keep up the ruse that I'm doing as I'm asked."
    scene bg clothesshop at center, dark
    show palla underwear
    with fade
    "When I get back to the cubicle, I pull the curtain aside and slip in before Palla realizes it's me."
    palla.say "Oh, [hero.name], there you are...finally!"
    "She's looking over her shoulder at me, expecting me to hand her the new clothes and then leave promptly, like a good boy."
    "I don't answer straight away, as she's standing there in nothing more than her panties."
    "Stood before the mirror as she is, I have an almost perfect view of Palla's nearly naked body, reflected upon its surface."
    "It comes home to me, in that moment, that in spite of the bitching, she's simply stunning to look at."
    palla.say "Don't hang around on my account!"
    palla.say "You can just hand them to me round the curtain next time."
    palla.say "[hero.name], hello...you just run along now, okay?"
    "What I was intending to do comes flooding back to me, and I tear my eyes away from the sight of Palla's hypnotic reflection."
    "Without saying a word, I make like I'm turning to leave."
    "The moment Palla turns her back on me and begins to inspect the clothes I brought at her behest, I stop and turn back around."
    show palla annoyed
    palla.say "Hey, wait a minute, these aren't what I asked--"
    hide palla
    show palla stand
    with fade
    "Palla yelps as I step forward and press her against the cold surface of the mirror."
    "Memories of the first time we did this come flooding back to me. She told me -- with a smile -- that I was an animal. She really wanted it then. Does she want it as much now?"
    "I wrap my right hand around hers, pinning it flat against the silvered glass above her head."
    "With the left, I slide two fingers into the crotch of her panties and lightly stroke the lips of her pussy."
    "Despite her apparent surprise and the shock in her eyes, Palla's already soaking the gusset of her underwear."
    "I guess she does want it as much as the first time!"
    "I keep Palla pinned with one arm while I hastily and rather clumsily strip off my own clothes as well."
    "Her breathing comes fast and in gasps, and I can almost feel her heart beating through her back."
    "She keeps trying to look back at me, but she's too closely pressed against the mirror."
    "All she manages to do is get one cheek squashed into it, making her expression look somewhat comical, despite the situation."
    show palla stand ahegao
    "Now that I'm undressed, I can see that I'm not going to need anything in the way of foreplay."
    "Palla too seems physically ready for me, despite her probably feigned reluctance."
    "I could swear that she even spreads her feet a little wider apart as she feels the brush of my cock on her buttocks."
    show palla stand wet
    "She yelps again as I push into her as far as I can go and remain there for a moment."
    "I can see her cheeks reddening in the mirror, and she closes her eyes now, fully engaged in what's happening."
    "I begin to thrust into Palla, every movement pushing the frustration of the day into the rearview mirror."
    "Fucking her as hard as possible seems to be the best form of therapy for her particular brand of annoyance."
    "The sense of danger, the thought that, at any moment, we might get caught -- it's turning us both on."
    "All it takes is the constant view of Palla's haughty face in such an undignified position, her breasts squashed almost flat against the mirror, the feeling of pounding her deep. God she's hot, especially like this."
    "I know that I can't keep from cumming too much longer."
    "So I need to make a decision as to where she's going to have to take it."
    menu:
        "Pull out":
            "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
            "I adjust my angle so that I can slide out of her pussy in one smooth motion."
            show palla stand dick wet
            "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
            "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
            "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
            "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
            "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
            "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
            show palla stand cum pleasure with hpunch
            "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
            show palla stand cumscreen with hpunch
        "Cum inside":
            "I'm having such a good time of using Palla's own pussy to purge me of the stress she causes me that I'm staying right where I am until I cum."
            "Since there's no chance of dragging this thing out and we might be rumbled at any moment, I step up my efforts."
            "Now I'm literally thrusting into Palla with as much force as I can muster without making enough noise to attract unwanted attention."
            "She too seems to be on the same wavelength, doing nothing to keep me from fucking her ever harder and everything to keep herself quiet as the same time."
            "Palla's pressed right up against the glass now, her breath steaming it up and the sweat from her body making it slick to the touch."
            "Her breasts are making a squeaking sound in time with my thrusts, like someone dragging a fingertip down a windowpane."
            "I can see her biting her lip in an effort to suppress a cry as she begins to cum."
            show palla stand cum pleasure with hpunch
            "That pushes me over the edge, and I lose myself inside of her a second later."
            with hpunch
            "I remain where I am, keeping Palla pinned to the mirror, even after I'm finished cumming."
            "And she's forced to ride out her own orgasm in that same position, fighting to remain silent."
            "All she manages to do is make a small mewling sound, as she twitches and writhes against me, her back slick with sweat."
    "It takes us a good few minutes to get our breath back, dress and compose ourselves, before we can walk out of the place."
    "The best part is...now we can get on with our date!"
    $ palla.sexperience += 1
    $ palla.sub += 2
    $ palla.love += 2
    $ game.active_date.score += 50
    if sasha.room == "clothesshop" and not sasha.is_sex_slave:
        $ sasha.love -= 20
    return

label palla_mall_date_fuck_02:
    "I take Palla on a shopping spree."
    $ renpy.dynamic("value")
    menu:
        "Spend 50{image=gui/icons/icon_money.png}":
            $ value = 1
        "Spend 100{image=gui/icons/icon_money.png}" if hero.money >= 100:
            $ value = 2
        "Spend 200{image=gui/icons/icon_money.png}" if hero.money >= 200:
            $ value = 3
        "Spend 400{image=gui/icons/icon_money.png}" if hero.money >= 400:
            $ value = 4
        "Spend 800{image=gui/icons/icon_money.png}" if hero.money >= 800:
            $ value = 5
        "Spend 1600{image=gui/icons/icon_money.png}" if hero.money >= 1600:
            $ value = 6

    $ hero.replace_activity()
    scene bg clothesshop
    show palla
    palla.say "Wait just a minute, [hero.name]. I appreciate the gesture, I do, but don't think I'm going to put out for you in the changing room again."
    if value < 4:
        mike.say "Should I just wait for you to be done, then?"
        palla.say "No, [hero.name], I want you to watch me try these things on and tell me which one makes me look the hottest. You're buying, and you want me to look good for you, right?"
        mike.say "Just tell me you're not going to try on {b}every{/b} piece of clothing in the store?"
        palla.say "Oh nonsense, most of this stuff doesn't fit me anyway."
        mike.say "That does not make me feel better."
        show palla joke
        palla.say "No but watching these tits go in and out of sexy dresses will."
        mike.say "Does that mean I get to watch you from inside the changing room?"
        palla.say "No."
        mike.say "Then I don't see how that follows."
        show palla normal
        palla.say "Oh, {b}fine{/b}, then. You want a show, fine. Have a show."
        show palla underwear with dissolve
        "I spend the next I don't know how many hours watching an endless parade of garments. In Palla's defense, yes, they're sexy, and yes, she's good at modelling them, and yes, it was entertaining, but...it's really hard to keep focus."
        $ game.pass_time(value)
    else:
        mike.say "For that much, I expect a nice thank you."
        show palla annoyed
        palla.say "What do you think, I'm a whore?"
        mike.say "Well..."
        show palla angry
        "Palla's face turns bright crimson."
        palla.say "How {b}dare{/b} you!"
        "Am I a bad person? Because somehow when Palla is this angry, she's just that much hotter than I normally think she is. And, after all Palla and I have been through, I know getting angry turns her on too. I just have to direct her carefully."
        mike.say "Fine, no, I don't think you're a whore. I do think you're a serious fashionista and that your needs run into the expensive."
        palla.say "And you're a horny asshole who thinks he can buy favors from me?"
        mike.say "Can I?"
        palla.say "Fuck, [hero.name], do you have a romantic bone in your body?"
        mike.say "The question is, do I have a romantic bone in {b}your{/b} body."
        show palla normal
        "Palla stares at me. Yes, the joke was terrible, but all the anger melted from her face. Though not so much a grin."
        palla.say "Fine. Fine fine fine. But let me shop first, because I really need something pretty to make me stop thinking about how fucking smug you look right now."
        mike.say "You have an hour."
        show palla sad
        palla.say "An hour! I'll never find something nice in an hour! And you want me in some nice lingerie, right?"
        "I cock my head to the side, pretending to think it over. I already know this is where I have to give her some rope. She has to think she's won something I wasn't prepared to give."
        mike.say "Fine, an hour and a half."
        show palla annoyed
        palla.say "No way! I need two, no three--wait, you want me to hit Victoria's Secret, so four!"
        mike.say "Four? I'll be asleep, have woke up, shot myself in the head, and then gone back to sleep in four hours. You get two, and if you say another word my credit card is going back into my wallet."
        "Palla frowns."
        show palla normal
        palla.say "Fine. Two hours. But you're helping me try things on."
        "This is the hard part. Can I really sit through two hours of watching her try on clothing? Maybe if she really does stick to the lingerie, and puts on a show."
        mike.say "You'd better give me a show."
        palla.say "Deal."
        $ game.play_music("music/roa_music/city_nights.ogg")
        "We're just about an hour in, when I notice that Palla's actually getting turned on by my boredom. Oh don't get me wrong, I like watching her in these outfits. Some of them are {b}very{/b} sexy and she's a hell of a woman, but I can't tell the difference between half the things."
        "But the more bored I get, the sexier her voice gets, and the more I can see hard nipples through whatever extremely thin piece of fabric she's thrown over them this time."
        "I think that means the time is about right. I make sure none of the staff is looking, and while she's changing for the (approximately) hundred thousandth time, I slip into her changing room."
        "She's facing the mirror, having just removed the latest garment and is in the process of tossing it into the pile."
        "I step right up to her and press her against the mirror."
        show palla stand with fade
        palla.say "Hey! It's only been an hour!"
        "I decide to go rough. I can already tell she's ready."
        mike.say "Shut up, bitch. You can finish when I finish."
        palla.say "But--"
        mike.say "If you say another word I'm going to shove your panties in your mouth to shut you up."
        "Her mouth snaps shut at that. There we go, that's what I want."
        "I use the moment of silence to strip out of my own clothes."
        show palla stand wet
        menu:
            "Fuck her ass":
                if palla.flags.anal < 3:
                    "I press the tip of my head into he waiting anus. It's so tight, though, that it won't go in."
                else:
                    "I press the tip of my head into he waiting anus. It enters freely for the first couple of inches before the tightness stops me. Palla's face contorts, and I pull back out."
                "Luckily, her pussy is flowing with lubricant. I slip myself deep into her cunt, getting myself good and wet, and then I go back to her asshole."
                "I have to work my way in over several tries, but with the fresh, natural lubricant on my cock, each gentle thrust gets me just a little bit further in, until I'm in far enough to truly feel good."
                "While I thrust into and out of her ass, her face thumps into the mirror at the end of every one. After a few moments of this, she starts to make muffled \"ow\" noises, so I slow down a bit and try not to thump her so hard."
                "Look, she likes it when I dominate her like this. It gets her off; but I don't want to hurt her!"
                "It only takes a few more thrusts and I'm ready to blow. And nothing short of gagging her would stop the screech she makes when she orgasms. At least she bites it short."
                $ palla.flags.anal += 1
            "Fuck her pussy":
                "I slip my hard cock into her pussy; she's wet, swollen and totally ready. It goes in easily and I push it in deep."
                "She tries not to make a sound, but a muffled mmf escapes her."
                mike.say "Shut up, bitch!"
                show palla stand ahegao
                "While I thrust into and out of her cunt, her face thumps into the mirror at the end of every one. After a few moments of this, she starts to make muffled \"ow\" noises, so I slow down a bit and try not to thump her so hard."
                "Look, she likes it when I dominate her like this. It gets her off; but I don't want to hurt her!"
                "It only takes a few more thrusts and I'm ready to blow. And nothing short of gagging her would stop the screech she makes when she orgasms. At least she bites it short."
        "I know that I can't keep from cumming too much longer."
        "So I need to make a decision as to where she's going to have to take it."
        menu:
            "Pull out":
                "I've become so fixated on the mirror and Palla's reflection in it, that I simply have to involve it somehow."
                "I adjust my angle so that I can slide out of her pussy in one smooth motion."
                show palla stand dick wet
                "That done, I make good use of the lubricant she's thoughtfully provided, and the sweat forming between her thighs to push my cock into the tight gap."
                "Despite her curvaceous thighs and their generous circumference, the head easily emerges from between them."
                "I can feel the cold touch of the mirror and the warm embrace of Palla's thighs all at once."
                "It's an incredible sensation, and I begin to move back and forth again, enjoying this almost as much as being inside of her."
                "Palla too seems to be getting off on it, as the shaft of my cock rubs against the splayed folds of her pussy."
                "She starts to twitch and moan, letting me know that she's close to cumming herself, and that finishes me too."
                show palla stand cum pleasure with hpunch
                "I cum whilst the head of my cock is poking out from between her thighs, splattering the mirror as well as Palla's thighs and belly."
                show palla stand cumscreen with hpunch
            "Cum inside":
                "I'm having such a good time of using Palla's own pussy to purge me of the stress she causes me that I'm staying right where I am until I cum."
                "Since there's no chance of dragging this thing out and we might be rumbled at any moment, I step up my efforts."
                "Now I'm literally thrusting into Palla with as much force as I can muster without making enough noise to attract unwanted attention."
                "She too seems to be on the same wavelength, doing nothing to keep me from fucking her ever harder and everything to keep herself quiet as the same time."
                "Palla's pressed right up against the glass now, her breath steaming it up and the sweat from her body making it slick to the touch."
                "Her breasts are making a squeaking sound in time with my thrusts, like someone dragging a fingertip down a windowpane."
                with hpunch
                "I can see her biting her lip in an effort to suppress a cry as she begins to cum."
                show palla stand cum pleasure with hpunch
                "That pushes me over the edge, and I lose myself inside of her a second later."
                with hpunch
                "I remain where I am, keeping Palla pinned to the mirror, even after I'm finished cumming."
                "And she's forced to ride out her own orgasm in that same position, fighting to remain silent."
                "All she manages to do is make a small mewling sound, as she twitches and writhes against me, her back slick with sweat."
        "It takes us a good few minutes to get our breath back, dress and compose ourselves, before we can walk out of the place."
        "I have to commend Palla for the act she puts on in handing back the unworn clothes to one of the catty sales assistants striding back into the mall."
        "None of them dare to say anything, but I think I can infer from their evil grins and the comments exchanged behind raised hands as we leave, that they at least suspect the truth of the matter."
        "Not that it really concerns me, as the whole thing has left me feeling an almost zen-like state of calm, purged of the annoyance Palla provoked in me."
        "I'd like to think that the experience might have humbled Palla a little too."
        $ palla.sexperience += 1
        $ palla.sub += 2
        $ palla.love += 2
        if (sasha.room == "clothesshop" or randint(1, 3) == 1) and not sasha.is_sex_slave:
            $ sasha.love -= 20
    $ game.active_date.score += 10
    $ hero.money -= 50 * 2 ** (value - 1)
    return

label palla_male_ending:









    if renpy.has_label("palla_achievement_3") and not game.flags.cheat:
        call palla_achievement_3 from _call_palla_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I don't know about you, but as a pretty typical kind of guy, I never imagined what my wedding would look like."
    "I know that girls are supposed to have it all planned out, but it's just not the kind of thing I'd ever considered."
    "Now Palla, on the other hand, I don't think there's a single thing she hadn't thought out ahead of time."
    "This was kind of a double-edged sword for me, you know?"
    "On the one hand it meant that I didn't have to spend a single moment planning our wedding."
    "But on the other it also meant that I was kind of swept along with all of her meticulous plans."
    "Everything had to be perfect, and by that I mean every single thing!"
    "But now that I'm standing here at the altar, waiting for her, I have to admit it..."
    "Palla planned this thing like a military operation, and it really paid off!"
    "The chapel looks amazing and even the guests look like they've been styled by a fashion genius."
    "It looks like the kind of wedding you see in glossy magazines!"
    "I almost have to pinch myself to remember that this is actually something that involves me."
    "But the sound of the music Palla chose to walk down the aisle to serves the same purpose a moment later."
    "I feel myself snapping to attention, standing straighter and even sucking in my gut!"
    "Every fibre of my being wants to look the best I can for her."
    show palla wedding at center, zoomAt (1.0, (640, 740)) with dissolve
    "And I know why the second that Palla comes into view."
    "Sure, she's obsessed with fashion and looking her best."
    "Yeah, it's kind of the thing that she does and it defines her."
    "But that doesn't mean she's not the most beautiful girl in the world!"
    "I'm not exaggerating when I say that the sight of Palla takes my breath away."
    "I find myself holding it in as I gape at how good she looks in her stylish wedding dress."
    "In fact, I've never seen her looking as lovely as she does right now!"
    "And graceful as well, don't forget graceful!"
    if palla.is_visibly_pregnant:
        "I have to look twice in order to see Palla's round belly."
        "Whoever made her dress must be some kind of fashion wizard!"
        "If I hadn't been the one that got her pregnant, I wouldn't believe she actually was!"
    else:
        "Whoever made Palla's dress must be some kind of fashion genius."
        "But then what else would you expect?"
        "It's just one hundred percent Palla!"
    show palla at center, traveling (1.75, 5.0, (640, 1200))
    "Palla sweeps down the aisle towards me with a fluid motion."
    "I guess this is what she was practicing for whenever she walked down a catwalk!"
    "By the time she reaches my side, I must be staring open-mouthed."
    "Palla smiles and flutters her eyelids at me - which doesn't help snap me out of it at all!"
    show palla happy
    palla.say "You can pick your jaw up off the floor now, [hero.name]!"
    palla.say "And you look pretty good too, just for the record..."
    show wedding palla with fade
    "I move my lips and my jaw, trying to form understandable sounds."
    "But it's no good, Palla's literally left me speechless!"
    "Priest" "Ahem..."
    "Priest" "If you two are ready..."
    show palla joke
    palla.say "Of course we're ready!"
    show palla normal
    palla.say "How about you?"
    show wedding palla priest with dissolve
    "The priest looks more than a little surprised at Palla taking control."
    "But he does an admirable job of shaking it off and getting things underway."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To witness the union of these two souls in holy matrimony..."
    "What follows is a perfect interpretation of Palla's vision."
    "Every word and gesture proceeds as she imagined it and according to plan."
    "And it's a good thing that it does too."
    "Because I'd hate to see what terrible fate awaited anyone dumb enough to ruin Palla's big day!"
    "Soon enough we get to the important part of the ceremony."
    "The one where we actually get to exchange our vows."
    "Priest" "Do you, Palla, take [hero.name] to be your lawful, wedded husband?"
    palla.say "Yes, I do."
    "Priest" "And do you, [hero.name], take Palla to be your lawful, wedded wife?"
    mike.say "I...I do!"
    "Priest" "I call on all those here present..."
    "Priest" "That if they know of any lawful reason these two may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause and ripple of laughter from the guests."
    "But at the same time, I feel a little know of tension in my gut."
    "Because I know Palla will literally kill anybody that ruins this moment for her!"
    "Priest" "Very good."
    "Priest" "It is therefore my great pleasure to pronounce you husband and wife."
    "Priest" "You may kiss the bride!"
    show wedding palla -priest with dissolve
    "I just have time to let out a sigh of relief."
    "But that's all I manage to do before Palla and I kiss."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show palla kiss wedding
    with fade
    $ palla.flags.kiss += 1
    "It's one of those dramatic, sweeping kisses that will look great on the wedding video."
    "And it's a move that Palla made me practice over and over again until I had it down."
    "But don't think for a moment that it's lacking in genuine passion."
    "Palla clings to me like her life depends on it, like she's terrified to let go."
    "But there's no reason for her to be worried."
    "It's not like I'm ever going to let her go again!"
    "Not now that I've married the most beautiful girl in the world."
    if palla.flags.pornfuck:
        scene bg street
        show palla annoyed
        with fade
        palla.say "Frankly, I don't see why I need to be the one that explains all of this!"
        palla.say "[hero.name] usually handles that side of things for me, you know?"
        palla.say "I'm more of an artist, a...performer - I speak through the medium of my body!"
        show palla normal
        palla.say "But if you insist, I suppose that I could prostitute myself just this once..."
        palla.say "I suppose you could say that meeting [hero.name] was a life-changing experience for me."
        palla.say "Not that it seemed that way to begin with."
        palla.say "Back then I was kind of obsessed with high fashion and all that stuff."
        palla.say "I thought that looking good and following the latest trends was the key to happiness."
        palla.say "But [hero.name] sort of started to chip away at that when we started dating."
        show palla blank
        palla.say "At first I thought he was just didn't get it, that he was being an ass."
        palla.say "I used to get so mad at him back then!"
        show palla joke
        palla.say "But slowly I started to realise that I was the one that had it wrong."
        palla.say "I thought that I was into fashion because it was like an art."
        palla.say "Sure, I wanted to be noticed and to have people admire me."
        palla.say "But I was sure that it was all about keeping my clothes on the whole time."
        palla.say "I was using my body like a mannequin in the window of a department store."
        show palla normal
        palla.say "And I needed [hero.name] to show me the error of my ways."
        palla.say "Soon I started to realise that the clothes were just getting in the way."
        palla.say "They were like a fancy layer of wrapping paper on a gift."
        show palla blush
        palla.say "It looks nice and shows off the shape of what's inside."
        palla.say "But sooner or later you have to tear it off to get at the stuff underneath!"
        palla.say "And yes, that was why he suggested that I try getting into more risque stuff."
        palla.say "It was scary at first, because you kind of grow up being told that porn is bad."
        palla.say "Everybody uses it in one way or another, but they try and hide that they do."
        palla.say "Which when you think about it is really dumb."
        palla.say "Everyone's okay with pictures of a model in a bikini being plastered everywhere."
        palla.say "But if the same model takes off those few scraps of cloth it becomes unacceptable!"
        palla.say "I challenge you to explain the logic of the one to me!"
        palla.say "In a way, I suppose you could say that [hero.name] liberated me."
        palla.say "He certainly helped me to find my true calling in life."
        palla.say "Since I got started in porn, I've never looked back."
        palla.say "And it's not me being exploited either - it's actually empowering!"
        palla.say "All I have to do is handle the physical side of things."
        palla.say "[hero.name] handles the business side of it for me."
        show palla happy
        palla.say "He's so creative too, always dreaming up new ideas!"
        palla.say "I think we make a pretty good team."
        if palla.flags.mikeBabies >= 1 or palla.is_visibly_pregnant:
            palla.say "He's such a great father too, so devoted to Mary."
            palla.say "I feel guilty having to jet off to shoots all over the world."
            palla.say "But I know they'll always be there to greet me at the airport when I get back!"
        else:
            palla.say "I think he'd make a pretty good father too."
            palla.say "Which is a thought that kind of took me by surprise."
            palla.say "Because I always assumed that I didn't want to start a family."
            palla.say "But now I'm not so sure..."
        scene palla pornstar ending with fade
        palla.say "My career's still pretty demanding though."
        palla.say "I don't think people realise just how hard a porn-star has to work."
        palla.say "Or how much of the world it's let me see!"
        palla.say "I can't believe that I once wanted to spend my life modelling."
        palla.say "And I don't think I'd have been able to achieve anything like this if I had."
        palla.say "[hero.name] opened my mind to a whole new world."
        palla.say "And together, I think that we can do anything!"
    else:
        scene bg park
        show palla normal
        with fade
        palla.say "I'm amazed it's taken this long for me to be able to actually speak for myself!"
        show palla annoyed
        palla.say "God knows that it must have been like hearing my story from [hero.name]'s point of view."
        show palla normal
        palla.say "I mean, bless him, he means well - but he's not the sharpest tool in the box."
        palla.say "And yes, let's address the elephant in the room before we go any further."
        palla.say "How in the hell did a girl like me end up with a guy like [hero.name]?"
        show palla wink
        palla.say "Honestly, I don't know!"
        show palla blank
        palla.say "When I imagined my future husband, he's not what I had in mind."
        palla.say "I was always picturing a male model or an actor, you know?"
        show palla joke
        palla.say "Maybe not a Hollywood A-Lister, but at least a cute TV star."
        palla.say "Hell, I'd even have settled for a rich guy that worked behind the scenes."
        palla.say "The kind of person that could pull strings and make me famous."
        show palla blank
        palla.say "But here I am with a guy that works in an office."
        palla.say "And one that plays videogames in his spare time too!"
        palla.say "And you know what the strangest thing is?"
        show palla normal
        palla.say "I have to admit that he's actually turned out great!"
        palla.say "The guy makes me happy - and I don't even know why!"
        palla.say "Of course he's crazily in love with me."
        palla.say "Come on - what guy wouldn't be?!?"
        palla.say "But I suppose he kind of grounds me too, you know?"
        palla.say "He reminds me that there's other stuff to life beyond fashion."
        palla.say "There you go - that's it, right there!"
        palla.say "[hero.name]'s changed me, made me able to say stuff like that."
        palla.say "Before I'd have thought that was a crazy statement to make!"
        palla.say "Sure, fashion's still my passion, a massive part of who I am."
        palla.say "But sometimes I can forget all about it and think about him instead."
        show palla annoyed
        palla.say "Wait a minute, I have to stop talking about him like that."
        palla.say "Like he's some kind of guru that's turned my life around!"
        palla.say "It's not like I'm the one that was a hopeless mess when we started dating!"
        show palla normal
        palla.say "I like to think that I was the one that straightened him out, you know?"
        palla.say "Turned him onto taking a pride in his appearance and dressing well."
        palla.say "I mean, he was teetering on the brink of being a slob back then."
        palla.say "If I hadn't taken him in hand, who knows where he'd be now?"
        palla.say "Probably wearing nothing but baggy jeans and band T-shirts!"
        palla.say "And okay, I'll say it..."
        scene palla model ending
        if palla.flags.pornnudes:
            show palla model ending naked
        with fade
        palla.say "I don't know if I'd have made it as a model without him."
        palla.say "High fashion and high stress kind of go hand in hand."
        palla.say "You can't have the former without the latter."
        palla.say "And that's where [hero.name] being a normal guy comes in handy."
        palla.say "I spend so much time around designers and artists."
        palla.say "They're always highly-strung and hyper-sensitive."
        palla.say "The demands they make of a model can be ridiculous."
        palla.say "So it's great to be able to come home to a guy like [hero.name]."
        palla.say "Someone that's not interested in seeing me parade around in their latest creations."
        palla.say "Well, that doesn't mean that [hero.name] isn't interested in seeing me parade around!"
        palla.say "And we sometimes have little fashion shows all of our own, if you know what I mean..."
        if palla.flags.mikeBabies >= 1 or palla.is_visibly_pregnant:
            palla.say "He's such a great father too, so devoted to Mary."
            palla.say "I feel guilty having to jet off to shoots all over the world."
            palla.say "But I know they'll always be there to greet me at the airport when I get back!"
        else:
            palla.say "I think he'd make a pretty good father too."
            palla.say "Which is a thought that kind of took me by surprise."
            palla.say "Because I always assumed that I didn't want to start a family."
            palla.say "But now I'm not so sure..."
        palla.say "So that's the long and short of it - [hero.name] and me."
        palla.say "We seem to be working out pretty well, and marriage agrees with us."
        palla.say "I don't know what the future holds."
        palla.say "But I'm looking forward to finding out with him at my side."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not palla.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_17
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_17
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label palla_give_address:
    show palla
    "I'm just about to say something to Palla when it vanishes right out of my head."
    "You know those moments when that happens, right?"
    "You're all ready to ask a question or point out something that seems important."
    "Then the least little distraction, and it's gone!"
    mike.say "Erm..."
    mike.say "Palla, I..."
    "Palla seems to notice me stumbling over my words."
    "But for some reason she doesn't wait for me to recover the thought."
    "Instead she seems to take it as a chance to change the subject entirely."

    if palla.sub >= 80:
        show palla submissive
        palla.say "I..."
        palla.say "I hope I'm not interrupting you, [hero.name]?"
        palla.say "But I wanted to give you this."
        show palla normal
    else:

        show palla talkative
        palla.say "What are you babbling about now, [hero.name]?"
        palla.say "Well never mind that..."
        palla.say "Because I have something for you."
        show palla normal
    "Surprised by Palla's words, I reach out and take what she's offering without a question."
    mike.say "Oh..."
    mike.say "What is it?"

    if palla.sub >= 80:
        show palla submissive
        palla.say "Ah..."
        palla.say "It's my address."
        palla.say "I...I thought you might like to have it?"
        show palla normal
    else:

        show palla happy at startle(0.05,-10)
        palla.say "It's my address, you silly boy!"
        show palla talkative
        palla.say "Since we're dating now, you should really have it written down."
        show palla normal
    "I can't help smiling as I fold it up and slip the address into my pocket."
    mike.say "Thanks, Palla..."
    mike.say "That's really thoughtful of you."
    mike.say "Kind of makes the whole thing feel more official!"
    $ palla.flags.addressknown = True
    return

label palla_apartment_first_visit:
    scene bg door palla with fade
    pause 0.2
    play sound door_knock
    "I have to admit that I'm feeling more than a little nervous as I knock on Palla's front-door."
    "On the one hand that's because she's one of the most demanding girls I've ever met."
    "On the other, this is also Shawn's front-door too."
    "And I'm hoping that he's not going to be the one that answers it!"
    play sound door_lock
    pause 1.5
    play sound door_open
    "So I can't help holding my breath as soon as I hear the sound of the door being unlocked."

    scene bg black with dissolve
    pause 0.5
    if palla.sub > 100 or palla.is_sex_slave:
        show bg pallalivingroom at center, zoomAt(1.5, (640, 780)) with wiperight
        "The door swings open, but to my surprise, there's nobody standing behind it."
        "I glance into the empty hallway for a few seconds, totally thrown."
        show bg pallalivingroom at center, traveling(1.5, 0.5, (640, 720))
        "But then my eyes travel downwards, and what I see surprises me all over again."
        scene bg black
        show palla dogeza folded at center with vpunch
        mike.say "WHA..."
        mike.say "What the..."
        "Palla's right there in front of me, kneeling on the floor."
        "In fact she's pretty much prostrating herself right now."
        "Her head is actually on the mat behind the front door."
        "But that's not even the craziest thing about what I can see."
        "Because in addition to all that, she's stark naked!"
        show palla dogeza at startle(0.1, 5)
        mike.say "Palla..."
        mike.say "You're..."
        palla.say "I'm greeting my master, like a good slave should."
        palla.say "And I'm making it plain that I'm ready to be used too!"
        "I glance left and right, hoping that nobody's seen what Palla's doing."
        play sound door_close
        "And then I step hastily into the hallway, closing the door behind me."
        "All the time trying my best not to step on Palla in the process."
        $ palla.sub += 2
        $ palla.love += 1

    elif palla.sub <= 40:
        show bg pallalivingroom at center
        show palla flirt
        with wiperight
        "The door opens, to my great relief, to reveal Palla standing in the hallway."
        "She regards me with her usual haughty demeanour, almost looking me up and down."
        show palla joke at startle(0.1, 5)
        palla.say "There you are, [hero.name]…"
        palla.say "You certainly took your time getting here!"
        show palla annoyed
        "The comment comes as kind of a slap in the face, making me pause."
        "And I can't help pulling out my phone to take a quick look at the time."
        show palla angry
        mike.say "Huh?"
        mike.say "I thought I got here right when you told me to?"
        show palla joke
        palla.say "Never mind that - get inside already!"
        show palla normal
        play sound door_close
    else:

        show bg pallalivingroom
        show palla flirt
        with wiperight
        "The door opens, to my great relief, to reveal Palla standing in the hallway."
        "She has her head bowed slightly, looking up at me as she does so."
        "Almost as if she's reluctant to actually look me in the eye."
        show palla submissive at startle(0.1, 5)
        palla.say "Thank you for coming, [hero.name]…"
        palla.say "Would you like to come inside?"
        show palla sadsmile
        "I'm a little taken aback by how demure Palla's being right now."
        "But at the same time I can't say that it's not a pleasant surprise."
        mike.say "Of course I would!"
        show palla happy at startle(0.1, 5)
        "Palla nods and gives me a little smile."
        "Then she steps neatly to the side and gestures for me to enter."
        play sound door_close
    scene bg black with fade
    $ palla.flags.palladelay = TemporaryFlag(True, 1)
    return

label palla_repeat_naked_dogeza:
    scene bg door palla with fade
    pause 0.2
    play sound door_knock
    "As soon as I make it to the door of Palla's apartment, I rap my knuckles on it."
    "Trying to ensure that the sound is loud enough to be heard anywhere inside the place."
    "And yet at the same time also trying to keep from making it sound too loud and aggressive."
    mike.say "Hey, Palla..."
    mike.say "It's me - hurry up and open the door already!"

    if "palla_repeat_naked_dogeza" in DONE:
        play sound door_lock
        pause 1.5
        play sound door_open
        show palla dogeza folded at center
        "When the door swings open and there's nobody there, I'm not surprised in the slightest."
        "Because my eyes travel instantly downwards and I see a familiar sight on the doormat."
        "There's Palla, totally naked and prostrating herself in front of me in the doorway."
        palla.say "Greetings, Master..."
        palla.say "Does the sight of me please you this day?"
        "The first time that she pulled this off in front of me, I'll admit that I was totally thrown."
        "In fact I was more worried about someone spotting her than actually checking out what was on show."
        "But now that I'm over the initial shock, I'm beginning to see the advantages of the whole concept."
        show palla dogeza at startle(0.1, 5)
        mike.say "Indeed it does, Palla."
        mike.say "But are you going to leave me standing out here all day?"
        "Of course this question is greeted by Palla instantly shaking her head."
        "And then she hurries to crawl backwards into the hallway behind her."
        "This means that I can step neatly through the doorway and close it behind me."
        play sound door_close
        "Already thinking of the possibilities now that we're safely inside and in private."
        $ palla.sub += 1
    else:

        "It doesn't take long for me to hear the sound of someone moving around inside."
        play sound door_lock
        pause 1.5
        play sound door_open
        show bg pallalivingroom at center, zoomAt(1.5, (640, 780)) with fade
        "Which is soon followed by the familiar noises of a door being unlocked too."
        "I take a half-step backwards, not wanting to look too eager to get inside."
        "But at the same time I'm already getting excited at the prospect of seeing Palla again."
        show bg pallalivingroom at startle(0.1, 5)
        mike.say "Hi, Palla..."
        mike.say "I..."
        mike.say "Huh?"
        "Fully expecting to see Palla standing in the doorway, I find myself totally stumped."
        "Because as far as I can see, there's nobody there at all!"
        "I'm about to gaze into the hallway beyond, wondering if Palla's already retreated further inside."
        "But then I realise that there actually is someone in the doorway."
        show bg pallalivingroom at center, traveling(1.5, 0.5, (640, 720))
        "Because that's when I almost trip over something soft and pink just inside of it."
        scene bg black
        show palla dogeza folded with vpunch
        mike.say "WHAT THE..."
        mike.say "Palla..."
        mike.say "What are you doing down there?!?"
        "The pink thing that I saw isn't an obstacle keeping me from getting to Palla."
        show palla dogeza at center, zoomAt(1, (640, 720))
        "It actually is, Palla - naked and crouched down on the doormat!"
        palla.say "I'm just greeting you in a respectful manner, [hero.name]."
        palla.say "Letting your see that I know my place."
        "Palla's literally got her forehead on the floor right now."
        "And I can see the whole of her back, as well as the top of her butt!"
        "Her clothes are neatly folded in a pile just to one side of her too."
        "As surprised as I am by this strange, naked stunt, it does seem familiar."
        "And I feel like I've heard of this before."
        show palla dogeza at startle(0.1, 5)
        mike.say "Dogeza!"
        mike.say "Is that what this is?"
        "Palla's head raises and then lowers again."
        "Which I take as a nod of affirmation."
        palla.say "That's right, [hero.name]!"
        palla.say "I'm showing you respect in a traditional, Japanese manner."
        palla.say "I hope that you approve?"
        show palla dogeza at startle(0.1, 5)
        mike.say "Erm..."
        mike.say "If I say yes, can I come inside and close the door?"
        "Palla nods for a second time."
        show palla dogeza at startle(0.1, 5)
        mike.say "Then yeah, this is totally amazing, Palla!"
        "Suitably satisfied with my answer, Palla inches herself backwards and away from the door."
        "Which allows me to hurry inside the apartment and close the door behind me."
        play sound door_close
        "All the time hoping that nobody saw what just went down on the doorstep between us."
        $ palla.sub += 1
        $ palla.love += 1
    return

label palla_apartment_sex:
    if not "palla_apartment_sex" in DONE:
        $ DONE["palla_apartment_sex"] = game.days_played
    scene bg black
    show bg pallalivingroom at zoomAt(1, (640, 720))
    show palla normal at center, zoomAt(1, (640, 720))
    with fade
    "You know those times when you have something on your mind that you daren't say out loud?"
    "So you have to pretend like you're being all thoughtful and distant from the person you're with."
    "All in the hope that they'll tune into it and ask you what's the matter, right?"
    "And then you have the excuse to bring it up with them."
    show palla b angry
    "But because they made you spill the beans, it's not like you're asking them straight up."
    "Yeah, well...let's just say it doesn't always work out as planned with a girl the likes of Palla."
    show palla angry at center, traveling(2.2, 0.2, (640, 1320))
    pause 0.2
    show palla annoyed at center, traveling(1, 0.5, (640, 720))
    show bg pallalivingroom at hshake
    mike.say "OUCH!"
    mike.say "Hey, Palla..."
    mike.say "What was that for?"
    mike.say "Why'd you jab me in the ribs like that?!?"
    $ renpy.dynamic(event_room="pallabedroom")

    if palla.sub <= 80:
        "Palla looks at me as if I'm the one that's doing weird shit by asking the question."
        show palla joke at startle(0.1, 5)
        palla.say "Because you were ignoring me, of course!"
        palla.say "And the only time that's acceptable is when you're not in my presence."
        show palla angry
        "Still rubbing the sore spot where Palla just jabbed me, I shuffle a couple of inches away from her."
        "And I make a mental note not to let my guard down around her like that again too."
        mike.say "I..."
        mike.say "I was just thinking that you have a nice place here, you know?"
        show palla stuned
        "Palla raises her eyebrows, adopting a quizzical expression."
        show palla vangry at startle(0.1, 5)
        palla.say "Ah, yeah, [hero.name]..."
        palla.say "And you're actually going somewhere with that?"
        palla.say "Or are you just stating the obvious?"
        show palla annoyed
        show palla at startle(0.1, 5)
        show bg pallalivingroom at startle(0.1, 5)
        "I nod eagerly, doing the best I can to get round to my point."
        mike.say "What I mean, Palla..."
        mike.say "Is that a place this nice..."
        mike.say "Well, it puts me in a certain kind of mood, you know?"
        "Palla listens to me patiently, waiting until I've said my piece."
        show palla stuned
        "And then I see one of her eyebrows rise higher still."
        show palla talkative at startle(0.1, 5)
        palla.say "Oh, I think I know what you mean!"
        palla.say "And you are such a lucky boy, [hero.name]."
        palla.say "Because right now, I'm in the exact same kind of mood!"
        show palla flirt at traveling(1.4, 0.7, (640, 920))
        "As she's saying all of this, Palla is closing the distance between us."
        "All the time looking like she's getting ready to pounce on me!"
        scene bg black
        show bg pallalivingroom at center
        show palla flirt at center, zoomAt(1.4, (640, 920))
        "Palla stands up and extends her hand towards me."
        show palla talkative at startle(0.1, 5)
        palla.say "Come on, [hero.name]…"
        palla.say "We're already somewhere private."
        palla.say "So let's go somewhere a little more comfortable."
        show palla flirt
        "It's not like Palla has to haul me to my feet to get me to follow her."
        "In fact I almost leap up the moment that she gives my arm the slightest tug."
        "And I hurry after her as she leads me into the hallway of her apartment."
        show palla talkative at startle(0.1, 5)
        palla.say "Okay, here's a fun idea..."
        palla.say "Either we can play it safe and use my room."
        palla.say "Or we can play with nerdy fire, and do it in Shawn's room instead!"
        show palla joke
        menu:
            "Choose to fuck in Palla's room":
                $ event_room = "pallabedroom"
                "Oh man, why did she have to go and mention Shawn?"
                "It's bad enough doing it under the roof where my buddy lives."
                "But actually doing it in his bedroom?"
                "And presumably on his bed too?!?"
                "Nope, that's just too much for me to handle."
                show palla normal
                mike.say "No, no, Palla..."
                mike.say "Your room sounds totally fine to me."
                show palla sad
                "Palla narrows her eyes as I turn down the chance to use Shawn's room."
                "Like she's a tad disappointed that I'd not be up for doing something so risky."
                show palla at stepback(0.1, 5,0)
                pause 0.1
                show palla at stepback(0.1,-5,0)
                pause 0.1
                "But then she shrugs her shoulders and shakes her head."
                show palla talkative
                palla.say "Whatever, [hero.name]…"
                palla.say "My room it is then."
                play sound door_open
                show bg pallabedroom with fade
                $ game.room = "pallabedroom"
                "With that, she pushes open the door to her bedroom."
                "And then she ushers me inside, closing the door behind me."
                "I do the best I can to play it off and act natural."
                "But the truth is that I'm more than a little relieved to be in her room with the door firmly closed."
                "I'm in the act of taking in the stylish décor that fits in so well with Palla's overall image."
                "But then I see that she's already turned her back to me and started to strip off her clothes."
                show palla a underwear flirt at traveling(1.4, 0.5, (640, 920)) with dissolve
                "One by one she removes the expensive underwear she has on."
                show palla topless with dissolve
                "And she drops them onto the floor while walking towards the bed."
                show palla naked with dissolve
                "This means that, as I follow on her heels, she leaves a trail for me to follow."
                "Or at least I could follow it, if I were able to take my eyes of her for as much as a single second."
                "As if hypnotised by the sight, I stumble after Palla, pulling off my own clothes at the same time."
                "She turns as she reaches the bed, lowering herself down onto it and then crawling backwards."
                "And she doesn't stop until her head is resting on the pillow, with the rest of her on show."
                "By now I'm pretty much naked too, clambering to get onto the bed and then onto Palla in turn."
                "As I do so, she doesn't say a word to encourage me, or to dampen my ardor for her either."
                "She just watches my progress, waiting for me to get into a position where I can act on it."
                "And when I'm finally there, Palla lets out a sigh."
                show palla talkative at startle(0.1, 5)
                palla.say "Mmm..."
                palla.say "Well here we are, [hero.name]."
                palla.say "You've got me at your mercy."
                palla.say "So what are you going to do to me, huh?"
                show palla flirt
                menu:
                    "Start with a blowjob":
                        "I have to admit that I'm a little flustered at how eager Palla seems to be."
                        "Because I was expecting to have to put in a lot more effort than that."
                        show palla at startle(0.1, 5)
                        show bg pallabedroom at startle(0.1, 5)
                        mike.say "Well, Palla..."
                        mike.say "I was wondering if we could start things off slowly, you know?"
                        mike.say "Like, maybe help relieve some of the pressure I'm feeling - DOWN THERE?"
                        "I make a point of nodding towards my crotch as I emphasize those last two words."
                        show palla annoyed
                        "Palla looks at me like I just said something really fucking dumb."
                        show palla vangry at startle(0.1, 5)
                        palla.say "Geez, [hero.name]..."
                        palla.say "I can take a subtle hint that you want me to suck your dick!"
                        palla.say "There's no need to spell it out for me."
                        show palla angry
                        "I was awkward before because I was nervous."
                        "But now I'm fidgeting and twitching because I'm getting seriously horny."
                        "The mere thought of Palla going down on me is enough to get me hard."
                        "And so the knowledge it's actually going to happen affects me that much more."
                        mike.say "Oh yeah..."
                        mike.say "I mean, of course I'd like you to do that for me."
                        mike.say "It sounds like a great idea."
                        show palla underwear flirt at center, traveling(1.3, 0.5, (640, 880)) with dissolve
                        "Palla gives me a knowing look as she slides onto the floor in front of me."
                        show palla flirt at traveling(1.4, 1.5, (640, 1400))
                        "But then she turns her attention to the task at hand, if you'll pardon the pun."
                        "I watch in silence as deftly unzips my flies, then slides her fingers inside."
                        "And I can't keep from gasping from the sensation as those digits fins my manhood a moment later."
                        "Palla handles me with a firmness that makes the whole thing that much more exhilarating."
                        "But she never seems to go too far, or treat my cock roughly just for the sake of it."
                        "Like I said, the mere thought of this happening was already making me hard."
                        "So Palla has the extra challenge of getting it out in that same state."
                        "She moves it this way and that, making me gasp at the feeling as she does so."
                        "And then, all of a sudden, it pops out, almost quivering as it stands upright."
                        show palla joke at startle(0.1, 5)
                        palla.say "Mmm..."
                        palla.say "There we are!"
                        "This time when I nod, my head is bobbing up and down like crazy."
                        "And I can't even manage to get my words out in a coherent manner."
                        mike.say "Y...yeh..."
                        mike.say "P...please!"
                        "Palla gives me a nod in return, pretending to be all business."
                        "But I can see the sheer pleasure on her face as she does so."
                        "Letting me know how much she loves being in such a position of power."
                        show palla blowjob pallabedroom at center, zoomAt(1.1, (640, 720))
                        show palla blowjob lick underwear
                        "Though the moment that Palla opens her mouth and actually touches it with the tip of her tongue..."
                        "Oh man, that's when things really start to get wild for me!"
                        "Because Palla gives head in the same way that she performs for all of her photo-shoots."
                        "She devotes herself to the task one hundred percent, ignoring everything else."
                        show palla blowjob at center, startle(0.1, 5)
                        "Little by little, my cock begins to disappear into her mouth."
                        "And as it does so, I find hands gripping onto whatever's close enough."
                        play sexsfx1 bj_sucking
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Like I feel the need to hold onto something, anything, for dear life!"
                        "I can't begin to imagine what's actually going on inside of Palla's mouth right now."
                        "And I don't know what's causing the sensations that I'm feeling either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Lips, tongue and teeth must all be involved in some kind of way."
                        "But I'm damned if I can tell what each of them is doing to me."
                        "Palla has her eyes closed as her head bobs up and down too."
                        "As if she's determined to keep silent and for it to remain a secret."
                        "And believe me when I say that Palla's not skimping on things either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Because I can already feel my cock beginning to go ever deeper down her throat."
                        "Soon enough she's got the entire length of it in there."
                        "And part of me is worried how much further she's going to go!"
                        "But it turns out that I needn't have worried about such things."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "As the sheer sensation of her throat squeezing me is just too much."
                        "And I can already feel myself starting to lose it."
                        stop sexsfx1
                        menu:
                            "Swallow":
                                "Luckily for me, Palla seems to sense it too."
                                "And when I make no move to change things, she acts accordingly."
                                "Keeping up the same pace as before, she gets herself ready."
                                play sound cum_inside
                                show palla blowjob hurt with vpunch
                                "And when I lose it, she simply swallows all that I have to give."
                                with vpunch
                                "Without missing a beat, Palla gulps down every last drop."
                                "Not stopping or gagging once throughout the entire act."
                            "Facial":
                                "Before it actually happens, I make an effort to pull back."
                                "Wanting to extricate myself from Palla's mouth, I try to rise up too."
                                "Luckily for me, she seems to sense what's happening."
                                play sound cum_inside
                                show palla blowjob cum hurt with vpunch
                                "And a moment later I feel my manhood being released."
                                with vpunch
                                "Palla doesn't move away after it's done either."
                                "Instead she sits perfectly still, waiting for the inevitable to happen."
                                "And when it does, she doesn't blink once as her face is spattered."
                                "I shoot my load straight into it, painting her features with thick, white stripes."
                                "Which soon being to run down her cheeks, and then drip off her chin."
                    "Just fuck her":
                        pass
                menu:
                    "Fuck her pussy":
                        "I know that Palla's asking me the question in order to tease me."
                        "That she wants to stoke the desires that I'm feeling for her as much as possible."
                        "But the question still resonates in my mind, and I have an almost instant answer."
                        mike.say "Oh, that's an easy one, Palla..."
                        mike.say "I'm going to stuff your pussy!"
                        show palla stuned
                        "It's obvious that Palla wasn't expecting an answer."
                        "But her eyes go wide and I can see the smile spreading across her face already."
                        show palla happy at startle(0.1, 5)
                        palla.say "Ha!"
                        palla.say "Okay, [hero.name]..."
                        palla.say "It's good to be with a man that knows his own mind!"
                        show palla flirt
                        "I nod, taking Palla's words as permission to have my wicked way with her."
                        "And in exactly that manner of my choosing too."
                        scene bg black
                        show palla missionary pallabedroom
                        with fade
                        call check_condom_usage (palla) from _call_check_condom_usage_154
                        if _return == False:
                            return "leave_without_gain"
                        "Eager to make the most of the time that I have with Palla, I begin to get myself into position."
                        "She lies still beneath me, not moving an inch, but also not doing a thing to impede my efforts either."
                        "So it's simplicity itself to line myself up, pointing my manhood straight between Palla's thighs."
                        "And then I keep right on lowering myself down even further, waiting for that first moment of contact."
                        "When it comes, I feel like a sudden surge of electricity is passing through my body."
                        "The slightest touch of the very tip against Palla's lips is enough to make me stiffen from head to toe."
                        "But rather than making me stop in my tracks, this causes me to flex, head and feet going backwards."
                        "And at the same time it pushes my groin forwards in the middle, pressing it hard against Palla's pussy."
                        palla.say "Ah..."
                        palla.say "Oh..."
                        palla.say "Oh fuck..."
                        "In that moment I feel like I'm almost paralysed, unable to move a muscles."
                        "But the same isn't true of Palla, as she wriggles and writhes beneath me."
                        "I feel her hands reaching out and grabbing hold of my butt, one cheek in each hand."
                        "And then I feel her pull me forwards as she thrusts herself hard against me at the same time."
                        palla.say "[hero.name]..."
                        palla.say "I want it..."
                        palla.say "Give it to me!"
                        "Palla's not asking me to fulfil her wishes when she says that."
                        "Neither is she pleading with me to do what she wants."
                        "Oh no, I can tell that she's simply making a demand."
                        "She's plainly stating what she wants, and I know she's going to get it!"
                        "Even before I can get myself moving and oblige her, she's already taken matters into her own hands."
                        if CONDOM:
                            show palla missionary condom
                        show palla missionary pleasure with dissolve
                        play sexsfx1 slide_in
                        "Desperately rubbing her pussy against the head of my cock, I can feel myself beginning to sink into her."
                        "And one thing that you should know about Palla is that she almost always ends up getting what she wants."
                        "In this case it even seems that her own body is in total lock-step with her mind too."
                        show palla missionary normal with dissolve
                        "Because within moments I can feel the muscles of her pussy start to relax."
                        "At first they feel softer, like they're just relaxing like any other body part would."
                        "But soon enough that changes, and it seems to me that they're actually melting."
                        show palla missionary vaginal with dissolve
                        "Like warming butter or ice-cream, Palla opens to me and my cock slides right in there."
                        "Before now I've almost felt like I was the one being taken by the hand."
                        show palla missionary pleasure with dissolve
                        "Like Palla was firmly in the driving seat and I was just along for the ride."
                        "And yet as soon as I'm all the way inside of her, all of that seems to change."
                        "It's like the sensation is just too much for her, like it's overwhelming her senses."
                        "At the same time I feel like a switch has been flicked on inside of my head."
                        show palla missionary normal with dissolve
                        "In that moment I come alive again, suddenly aware of every inch of my body."
                        "And in particular the inches that are currently lodged deep in Palla."
                        show palla missionary at hshake
                        play sexsfx1 fuck_calm
                        "Even as she leans back, surrendering to the sensations, I'm starting to move in earnest."
                        "I'm not talking about a gentle swinging into motion here either."
                        show palla missionary at hshake
                        "Already I'm picking up speed as I move back and forth, thrusting in and out."
                        "With every repetition of the motion, Palla becomes more helpless still."
                        "Lying back on the bed, she doesn't even try to hold onto me as I pound away at her."
                        "Instead she remains spread out beneath me, like she's almost helpless."
                        "There's no space inside of my head for observing anything more than that."
                        "Because by now I'm totally engrossed in the act, unable to think of anything else."
                        "Luckily for me, in doing so I seem to be totally overwhelming Palla too."
                        "Honestly, this is the most quiet and passive I've ever seen her!"
                        "Normally she'd be assailing me with a list of demands and requirements."
                        "But right now the only sound she's capable of making is a low moaning."
                        show palla missionary at hshake
                        "Palla's thighs move in time with my own, her breasts swaying from my motion."
                        "And though helpless and immobile, she still looks like a work of art."
                        "So much so that I feel myself beginning to lose control."
                        "I know that any moment I'm going to lose it."
                        "And so I have to decide how this thing is going to end."
                        "Because heaven knows Palla's in no fit state to have an opinion on the matter."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                if CONDOM:
                                    "Luckily for me we decided to use protection, which makes things a whole lot simpler."
                                    "Because it means that all I have to do is keep on doing what I'm doing right now."
                                    "Pushing myself as deeply into Palla as humanly possible until the final moment."
                                    "And when that final moment comes, I just let it happen and let myself go."
                                    show palla missionary ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "Which means that everything I have to give explodes inside of Palla."
                                    "The sensation seems to be too much for her, pushing her over the edge."
                                    "And she cums even as I'm still reeling from the effects of my own orgasm."
                                else:

                                    "There's really only one thing that I can do, which is to keep on doing what I'm doing right now."
                                    "Pushing myself as deeply into Palla as humanly possible until the final moment."
                                    "And when that final moment comes, I just let it happen and let myself go."
                                    show palla missionary cumshot ahegao at hshake
                                    play sexsfx1 final_thrust
                                    $ palla.impregnate()
                                    "Which means that everything I have to give explodes inside of Palla."
                                    "The sensation seems to be too much for her, pushing her over the edge."
                                    "And she cums even as I'm still reeling from the effects of my own orgasm."
                            "Pull out":
                                "Using the last of my strength, I make an effort to free myself from Palla's pussy."
                                "It takes everything that I have left, and for a moment I think that I'm not going to make it."
                                "But at the very last moment I manage to pull my cock out of Palla."
                                "The sensation seems to be too much for her, pushing her over the edge."
                                show palla missionary cumshot out ahegao at hshake
                                "And she cums even as I'm still reeling from the effects of it hitting me too."
                                show palla missionary -cumshot cum onbody
                                "Shooting my load over her exposed belly and painting it with sticky, white stripes."
                                $ hero.energy -= 2
                    "Fuck her ass":
                        "I know that Palla's asking me the question in order to tease me."
                        "That she wants to stoke the desires that I'm feeling for her as much as possible."
                        "But the question still resonates in my mind, and I have an almost instant answer."
                        mike.say "Oh, that's an easy one, Palla..."
                        mike.say "I'm going to stuff your ass!"
                        "It's obvious that Palla wasn't expecting an answer."
                        "But her eyes go wide and I can see the smile spreading across her face already."
                        palla.say "Ha!"
                        palla.say "Okay, [hero.name]..."
                        palla.say "It's good to be with a man that knows his own mind!"
                        "I nod, taking Palla's words as permission to have my wicked way with her."
                        "And in exactly that manner of my choosing too."
                        scene bg black
                        show palla missionary out
                        with fade
                        "Eager to make the most of the time that I have with Palla, I begin to get myself into position."
                        "She lies still beneath me, not moving an inch, but also not doing a thing to impede my efforts either."
                        "So it's simplicity itself to line myself up, pointing my manhood straight between Palla's buttocks."
                        "And then I keep right on lowering myself down even further, waiting for that first moment of contact."
                        "When it comes, I feel like a sudden surge of electricity is passing through my body."
                        "The slightest touch of the very tip against Palla's hole is enough to make me stiffen from head to toe."
                        "But rather than making me stop in my tracks, this causes me to flex, head and feet going backwards."
                        "And at the same time it pushes my groin forwards in the middle, pressing it hard against Palla's hole."
                        palla.say "Ah..."
                        palla.say "Oh..."
                        palla.say "Oh fuck..."
                        "In that moment I feel like I'm almost paralysed, unable to move a muscles."
                        "But the same isn't true of Palla, as she wriggles and writhes beneath me."
                        "I feel her hands reaching out and grabbing hold of my butt, one cheek in each hand."
                        "And then I feel her pull me forwards as she thrusts herself hard against me at the same time."
                        palla.say "[hero.name]..."
                        palla.say "I want it..."
                        palla.say "Give it to me!"
                        "Palla's not asking me to fulfil her wishes when she says that."
                        "Neither is she pleading with me to do what she wants."
                        "Oh no, I can tell that she's simply making a demand."
                        "She's plainly stating what she wants, and I know she's going to get it!"
                        "Even before I can get myself moving and oblige her, she's already taken matters into her own hands."
                        show palla missionary -out pleasure with dissolve
                        play sexsfx1 slide_in
                        "Desperately rubbing her hole against the head of my cock, I can feel myself beginning to sink into her."
                        "And one thing that you should know about Palla is that she almost always ends up getting what she wants."
                        "In this case it even seems that her own body is in total lock-step with her mind too."
                        "Because within moments I can feel the muscles of her ass start to relax."
                        "At first they feel softer, like they're just relaxing like any other body part would."
                        "But soon enough that changes, and it seems to me that they're actually melting."
                        show palla missionary anal with dissolve
                        "Like warming butter or ice-cream, Palla opens to me and my cock slides right in there."
                        "Before now I've almost felt like I was the one being taken by the hand."
                        show palla missionary with dissolve
                        "Like Palla was firmly in the driving seat and I was just along for the ride."
                        "And yet as soon as I'm all the way inside of her, all of that seems to change."
                        "It's like the sensation is just too much for her, like it's overwhelming her senses."
                        "At the same time I feel like a switch has been flicked on inside of my head."
                        "In that moment I come alive again, suddenly aware of every inch of my body."
                        "And in particular the inches that are currently lodged deep in Palla."
                        show palla missionary at hshake
                        play sexsfx1 fuck_moderate loop
                        "Even as she leans back, surrendering to the sensations, I'm starting to move in earnest."
                        "I'm not talking about a gentle swinging into motion here either."
                        show palla missionary at hshake
                        "Already I'm picking up speed as I move back and forth, thrusting in and out."
                        "With every repetition of the motion, Palla becomes more helpless still."
                        "Lying back on the bed, she doesn't even try to hold onto me as I pound away at her."
                        "Instead she remains spread out beneath me, like she's almost helpless."
                        "There's no space inside of my head for observing anything more than that."
                        "Because by now I'm totally engrossed in the act, unable to think of anything else."
                        "Luckily for me, in doing so I seem to be totally overwhelming Palla too."
                        "Honestly, this is the most quiet and passive I've ever seen her!"
                        "Normally she'd be assailing me with a list of demands and requirements."
                        "But right now the only sound she's capable of making is a low moaning."
                        show palla missionary at hshake
                        "Palla's thighs move in time with my own, her breasts swaying from my motion."
                        "And though helpless and immobile, she still looks like a work of art."
                        "So much so that I feel myself beginning to lose control."
                        "I know that any moment I'm going to lose it."
                        "And so I have to decide how this thing is going to end."
                        "Because heaven knows Palla's in no fit state to have an opinion on the matter."
                        menu:
                            "Cum inside":
                                "There's really only one thing that I can do, which is to keep on doing what I'm doing right now."
                                "Pushing myself as deeply into Palla's ass as humanly possible until the final moment."
                                "And when that final moment comes, I just let it happen and let myself go."
                                "Which means that everything I have to give explodes inside of Palla."
                                show palla missionary cumshot ahegao at hshake
                                play sexsfx1 final_thrust
                                "The sensation seems to be too much for her, pushing her over the edge."
                                "And she cums even as I'm still reeling from the effects of my own orgasm."
                                $ hero.energy -= 2
                                $ palla.sub += 1
                            "Pull out":
                                "Using the last of my strength, I make an effort to free myself from Palla's ass."
                                "It takes everything that I have left, and for a moment I think that I'm not going to make it."
                                "But at the very last moment I manage to pull my cock out of Palla's ass."
                                show palla missionary cumshot out ahegao at hshake
                                play sexsfx1 pull_out
                                "The sensation seems to be too much for her, pushing her over the edge."
                                "And she cums even as I'm still reeling from the effects of it hitting me too."
                                show palla missionary -cumshot cum onbody at hshake
                                "Shooting my load over her exposed belly and painting it with sticky, white stripes."
                                $ hero.energy -= 2
                                $ palla.sub += 1
                        stop sexsfx1
            "Choose to fuck in Shawn's room":
                $ event_room = "shawnbedroom"
                "The moment that Palla mentions Shawn's room, my interest is piqued."
                "I've always felt a frisson of danger knowing this is his place too."
                "But the opportunity to actually get up to something in his bedroom - and on his bed too!"
                "Well, that's just too good of a chance to pass up."
                show palla surprised at startle(0.1, 5)
                mike.say "SHAWN'S ROOM!"
                mike.say "We have to fuck in Shawn's room!"
                "Palla looks more than a little surprised by how quickly I respond."
                show palla normal
                "Like she was sure that I'd need a little while to warm to the idea."
                "But she recovers her composure with admirable speed."
                show palla joke at startle(0.1, 5)
                palla.say "Okay, okay..."
                palla.say "So you want to live dangerously, yeah?"
                palla.say "Shawn's room it is!"
                show palla happy
                play sound door_open
                show bg shawnbedroom with fade
                $ game.room == "shawnbedroom"
                "Palla opens the door to Shawn's bedroom and ushers me inside."
                "As she closes it behind me, I take a look around."
                "I mean I know what the place looks like, as I've been in here before."
                "Only that was with Shawn when he wanted to show me something in his collection."
                "Or else he had to tell me something that he didn't want Palla overhearing."
                "But now I'm in here without him for the first time, about to use the facilities behind his back."
                "Though I do notice he seems to have acquired some new additions to his collection since I was last here."
                "And I can't help beginning to get drawn into the act of examining them more closely."
                "That is until Palla steps in front of me, already starting to strip off her clothes."
                show palla a underwear flirt at traveling(1.4, 0.5, (640, 920)) with dissolve

                "One by one she removes the expensive underwear she has on."
                show palla topless with dissolve
                "And she drops them onto the floor while walking towards the bed."
                show palla naked with dissolve
                "This means that, as I follow on her heels, she leaves a trail for me to follow."
                "Or at least I could follow it, if I were able to take my eyes of her for as much as a single second."
                "As if hypnotised by the sight, I stumble after Palla, pulling off my own clothes at the same time."
                "She turns as she reaches the bed, lowering herself down onto it and then crawling backwards."
                "And she doesn't stop until her head is resting on the pillow, with the rest of her on show."
                "By now I'm pretty much naked too, clambering to get onto the bed and then onto Palla in turn."
                "As I do so, she doesn't say a word to encourage me, or to dampen my ardor for her either."
                "She just watches my progress, waiting for me to get into a position where I can act on it."
                "And when I'm finally there, Palla lets out a sigh."
                show palla talkative at startle(0.1, 5)
                palla.say "Mmm..."
                palla.say "Well here we are, [hero.name]."
                palla.say "You've got me at your mercy."
                palla.say "So what are you going to do to me, huh?"
                show palla flirt
                menu:
                    "Start with a blowjob":
                        "I have to admit that I'm a little flustered at how eager Palla seems to be."
                        "Because I was expecting to have to put in a lot more effort than that."
                        show palla at startle(0.1, 5)
                        show bg shawnbedroom at startle(0.1, 5)
                        mike.say "Well, Palla..."
                        mike.say "I was wondering if we could start things off slowly, you know?"
                        mike.say "Like, maybe help relieve some of the pressure I'm feeling - DOWN THERE?"
                        "I make a point of nodding towards my crotch as I emphasize those last two words."
                        show palla annoyed
                        "Palla looks at me like I just said something really fucking dumb."
                        show palla vangry at startle(0.1, 5)
                        palla.say "Geez, [hero.name]..."
                        palla.say "I can take a subtle hint that you want me to suck your dick!"
                        palla.say "There's no need to spell it out for me."
                        show palla angry
                        "I was awkward before because I was nervous."
                        "But now I'm fidgeting and twitching because I'm getting seriously horny."
                        "The mere thought of Palla going down on me is enough to get me hard."
                        "And so the knowledge it's actually going to happen affects me that much more."
                        mike.say "Oh yeah..."
                        mike.say "I mean, of course I'd like you to do that for me."
                        mike.say "It sounds like a great idea."
                        show palla underwear flirt at center, traveling(1.3, 0.5, (640, 880)) with dissolve
                        "Palla gives me a knowing look as she slides onto the floor in front of me."
                        show palla flirt at traveling(1.4, 1.5, (640, 1400))
                        "But then she turns her attention to the task at hand, if you'll pardon the pun."
                        "I watch in silence as deftly unzips my flies, then slides her fingers inside."
                        "And I can't keep from gasping from the sensation as those digits fins my manhood a moment later."
                        "Palla handles me with a firmness that makes the whole thing that much more exhilarating."
                        "But she never seems to go too far, or treat my cock roughly just for the sake of it."
                        "Like I said, the mere thought of this happening was already making me hard."
                        "So Palla has the extra challenge of getting it out in that same state."
                        "She moves it this way and that, making me gasp at the feeling as she does so."
                        "And then, all of a sudden, it pops out, almost quivering as it stands upright."
                        show palla joke at startle(0.1, 5)
                        palla.say "Mmm..."
                        palla.say "There we are!"
                        "This time when I nod, my head is bobbing up and down like crazy."
                        "And I can't even manage to get my words out in a coherent manner."
                        mike.say "Y...yeh..."
                        mike.say "P...please!"
                        "Palla gives me a nod in return, pretending to be all business."
                        "But I can see the sheer pleasure on her face as she does so."
                        "Letting me know how much she loves being in such a position of power."
                        show palla blowjob shawnbedroom at center, zoomAt(1.1, (640, 720))
                        show palla blowjob lick underwear
                        "Though the moment that Palla opens her mouth and actually touches it with the tip of her tongue..."
                        "Oh man, that's when things really start to get wild for me!"
                        "Because Palla gives head in the same way that she performs for all of her photo-shoots."
                        "She devotes herself to the task one hundred percent, ignoring everything else."
                        show palla blowjob at center, startle(0.1, 5)
                        "Little by little, my cock begins to disappear into her mouth."
                        "And as it does so, I find hands gripping onto whatever's close enough."
                        play sexsfx1 bj_sucking loop
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Like I feel the need to hold onto something, anything, for dear life!"
                        "I can't begin to imagine what's actually going on inside of Palla's mouth right now."
                        "And I don't know what's causing the sensations that I'm feeling either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Lips, tongue and teeth must all be involved in some kind of way."
                        "But I'm damned if I can tell what each of them is doing to me."
                        "Palla has her eyes closed as her head bobs up and down too."
                        "As if she's determined to keep silent and for it to remain a secret."
                        "And believe me when I say that Palla's not skimping on things either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Because I can already feel my cock beginning to go ever deeper down her throat."
                        "Soon enough she's got the entire length of it in there."
                        "And part of me is worried how much further she's going to go!"
                        "But it turns out that I needn't have worried about such things."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "As the sheer sensation of her throat squeezing me is just too much."
                        "And I can already feel myself starting to lose it."
                        stop sexsfx1
                        menu:
                            "Swallow":
                                "Luckily for me, Palla seems to sense it too."
                                "And when I make no move to change things, she acts accordingly."
                                "Keeping up the same pace as before, she gets herself ready."
                                play sound cum_inside
                                show palla blowjob hurt with vpunch
                                "And when I lose it, she simply swallows all that I have to give."
                                with vpunch
                                "Without missing a beat, Palla gulps down every last drop."
                                "Not stopping or gagging once throughout the entire act."
                            "Facial":
                                "Before it actually happens, I make an effort to pull back."
                                "Wanting to extricate myself from Palla's mouth, I try to rise up too."
                                "Luckily for me, she seems to sense what's happening."
                                play sound cum_inside
                                show palla blowjob cum hurt with vpunch
                                "And a moment later I feel my manhood being released."
                                with vpunch
                                "Palla doesn't move away after it's done either."
                                "Instead she sits perfectly still, waiting for the inevitable to happen."
                                "And when it does, she doesn't blink once as her face is spattered."
                                "I shoot my load straight into it, painting her features with thick, white stripes."
                                "Which soon being to run down her cheeks, and then drip off her chin."
                    "Just fuck her":
                        pass
                menu:
                    "Fuck her pussy":
                        "I know that Palla's asking me the question in order to tease me."
                        "That she wants to stoke the desires that I'm feeling for her as much as possible."
                        "But the question still resonates in my mind, and I have an almost instant answer."
                        mike.say "Oh, that's an easy one, Palla..."
                        mike.say "I'm going to stuff your pussy!"
                        show palla stuned
                        "It's obvious that Palla wasn't expecting an answer."
                        "But her eyes go wide and I can see the smile spreading across her face already."
                        show palla happy at startle(0.1, 5)
                        palla.say "Ha!"
                        palla.say "Okay, [hero.name]..."
                        palla.say "It's good to be with a man that knows his own mind!"
                        show palla flirt
                        "I nod, taking Palla's words as permission to have my wicked way with her."
                        "And in exactly that manner of my choosing too."
                        scene bg black
                        show palla missionary shawnbedroom
                        with fade
                        call check_condom_usage (palla) from _call_check_condom_usage_157
                        if _return == False:
                            return "leave_without_gain"
                        "Eager to make the most of the time that I have with Palla, I begin to get myself into position."
                        "She lies still beneath me, not moving an inch, but also not doing a thing to impede my efforts either."
                        "So it's simplicity itself to line myself up, pointing my manhood straight between Palla's thighs."
                        "And then I keep right on lowering myself down even further, waiting for that first moment of contact."
                        "When it comes, I feel like a sudden surge of electricity is passing through my body."
                        "The slightest touch of the very tip against Palla's lips is enough to make me stiffen from head to toe."
                        "But rather than making me stop in my tracks, this causes me to flex, head and feet going backwards."
                        "And at the same time it pushes my groin forwards in the middle, pressing it hard against Palla's pussy."
                        palla.say "Ah..."
                        palla.say "Oh..."
                        palla.say "Oh fuck..."
                        "In that moment I feel like I'm almost paralysed, unable to move a muscles."
                        "But the same isn't true of Palla, as she wriggles and writhes beneath me."
                        "I feel her hands reaching out and grabbing hold of my butt, one cheek in each hand."
                        "And then I feel her pull me forwards as she thrusts herself hard against me at the same time."
                        palla.say "[hero.name]..."
                        palla.say "I want it..."
                        palla.say "Give it to me!"
                        "Palla's not asking me to fulfil her wishes when she says that."
                        "Neither is she pleading with me to do what she wants."
                        "Oh no, I can tell that she's simply making a demand."
                        "She's plainly stating what she wants, and I know she's going to get it!"
                        "Even before I can get myself moving and oblige her, she's already taken matters into her own hands."
                        if CONDOM:
                            show palla missionary condom
                        show palla missionary pleasure with dissolve
                        play sexsfx1 slide_in
                        "Desperately rubbing her pussy against the head of my cock, I can feel myself beginning to sink into her."
                        "And one thing that you should know about Palla is that she almost always ends up getting what she wants."
                        "In this case it even seems that her own body is in total lock-step with her mind too."
                        "Because within moments I can feel the muscles of her pussy start to relax."
                        "At first they feel softer, like they're just relaxing like any other body part would."
                        "But soon enough that changes, and it seems to me that they're actually melting."
                        show palla missionary vaginal with dissolve
                        "Like warming butter or ice-cream, Palla opens to me and my cock slides right in there."
                        "Before now I've almost felt like I was the one being taken by the hand."
                        show palla missionary pleasure with dissolve
                        "Like Palla was firmly in the driving seat and I was just along for the ride."
                        "And yet as soon as I'm all the way inside of her, all of that seems to change."
                        "It's like the sensation is just too much for her, like it's overwhelming her senses."
                        "At the same time I feel like a switch has been flicked on inside of my head."
                        "In that moment I come alive again, suddenly aware of every inch of my body."
                        "And in particular the inches that are currently lodged deep in Palla."
                        show palla missionary normal at hshake
                        play sexsfx1 fuck_calm
                        "Even as she leans back, surrendering to the sensations, I'm starting to move in earnest."
                        "I'm not talking about a gentle swinging into motion here either."
                        show palla missionary pleasure at hshake
                        "Already I'm picking up speed as I move back and forth, thrusting in and out."
                        "With every repetition of the motion, Palla becomes more helpless still."
                        "Lying back on the bed, she doesn't even try to hold onto me as I pound away at her."
                        "Instead she remains spread out beneath me, like she's almost helpless."
                        "There's no space inside of my head for observing anything more than that."
                        "Because by now I'm totally engrossed in the act, unable to think of anything else."
                        "Luckily for me, in doing so I seem to be totally overwhelming Palla too."
                        "Honestly, this is the most quiet and passive I've ever seen her!"
                        "Normally she'd be assailing me with a list of demands and requirements."
                        "But right now the only sound she's capable of making is a low moaning."
                        show palla missionary normal at hshake
                        "Palla's thighs move in time with my own, her breasts swaying from my motion."
                        "And though helpless and immobile, she still looks like a work of art."
                        "So much so that I feel myself beginning to lose control."
                        "I know that any moment I'm going to lose it."
                        "And so I have to decide how this thing is going to end."
                        "Because heaven knows Palla's in no fit state to have an opinion on the matter."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                if CONDOM:
                                    "Luckily for me we decided to use protection, which makes things a whole lot simpler."
                                    "Because it means that all I have to do is keep on doing what I'm doing right now."
                                    "Pushing myself as deeply into Palla as humanly possible until the final moment."
                                    "And when that final moment comes, I just let it happen and let myself go."
                                    show palla missionary ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "Which means that everything I have to give explodes inside of Palla."
                                    "The sensation seems to be too much for her, pushing her over the edge."
                                    "And she cums even as I'm still reeling from the effects of my own orgasm."
                                else:

                                    "There's really only one thing that I can do, which is to keep on doing what I'm doing right now."
                                    "Pushing myself as deeply into Palla as humanly possible until the final moment."
                                    "And when that final moment comes, I just let it happen and let myself go."
                                    show palla missionary cumshot ahegao at hshake
                                    play sexsfx1 final_thrust
                                    $ palla.impregnate()
                                    "Which means that everything I have to give explodes inside of Palla."
                                    "The sensation seems to be too much for her, pushing her over the edge."
                                    "And she cums even as I'm still reeling from the effects of my own orgasm."
                            "Pull out":
                                "Using the last of my strength, I make an effort to free myself from Palla's pussy."
                                "It takes everything that I have left, and for a moment I think that I'm not going to make it."
                                "But at the very last moment I manage to pull my cock out of Palla."
                                "The sensation seems to be too much for her, pushing her over the edge."
                                show palla missionary cumshot out ahegao at hshake
                                "And she cums even as I'm still reeling from the effects of it hitting me too."
                                show palla missionary -cumshot out ahegao cum onbody at hshake
                                "Shooting my load over her exposed belly and painting it with sticky, white stripes."
                                $ hero.energy -= 2
                    "Fuck her ass":
                        "I know that Palla's asking me the question in order to tease me."
                        "That she wants to stoke the desires that I'm feeling for her as much as possible."
                        "But the question still resonates in my mind, and I have an almost instant answer."
                        mike.say "Oh, that's an easy one, Palla..."
                        mike.say "I'm going to stuff your ass!"
                        "It's obvious that Palla wasn't expecting an answer."
                        "But her eyes go wide and I can see the smile spreading across her face already."
                        palla.say "Ha!"
                        palla.say "Okay, [hero.name]..."
                        palla.say "It's good to be with a man that knows his own mind!"
                        "I nod, taking Palla's words as permission to have my wicked way with her."
                        "And in exactly that manner of my choosing too."
                        scene bg black
                        show palla missionary out
                        with fade
                        "Eager to make the most of the time that I have with Palla, I begin to get myself into position."
                        "She lies still beneath me, not moving an inch, but also not doing a thing to impede my efforts either."
                        "So it's simplicity itself to line myself up, pointing my manhood straight between Palla's buttocks."
                        "And then I keep right on lowering myself down even further, waiting for that first moment of contact."
                        "When it comes, I feel like a sudden surge of electricity is passing through my body."
                        "The slightest touch of the very tip against Palla's hole is enough to make me stiffen from head to toe."
                        "But rather than making me stop in my tracks, this causes me to flex, head and feet going backwards."
                        "And at the same time it pushes my groin forwards in the middle, pressing it hard against Palla's hole."
                        palla.say "Ah..."
                        palla.say "Oh..."
                        palla.say "Oh fuck..."
                        "In that moment I feel like I'm almost paralysed, unable to move a muscles."
                        "But the same isn't true of Palla, as she wriggles and writhes beneath me."
                        "I feel her hands reaching out and grabbing hold of my butt, one cheek in each hand."
                        "And then I feel her pull me forwards as she thrusts herself hard against me at the same time."
                        palla.say "[hero.name]..."
                        palla.say "I want it..."
                        palla.say "Give it to me!"
                        "Palla's not asking me to fulfil her wishes when she says that."
                        "Neither is she pleading with me to do what she wants."
                        "Oh no, I can tell that she's simply making a demand."
                        "She's plainly stating what she wants, and I know she's going to get it!"
                        "Even before I can get myself moving and oblige her, she's already taken matters into her own hands."
                        show palla missionary anal with dissolve
                        play sexsfx1 slide_in
                        "Desperately rubbing her hole against the head of my cock, I can feel myself beginning to sink into her."
                        "And one thing that you should know about Palla is that she almost always ends up getting what she wants."
                        "In this case it even seems that her own body is in total lock-step with her mind too."
                        "Because within moments I can feel the muscles of her ass start to relax."
                        "At first they feel softer, like they're just relaxing like any other body part would."
                        "But soon enough that changes, and it seems to me that they're actually melting."
                        show palla missionary pleasure with dissolve
                        "Like warming butter or ice-cream, Palla opens to me and my cock slides right in there."
                        "Before now I've almost felt like I was the one being taken by the hand."
                        show palla missionary normal with dissolve
                        "Like Palla was firmly in the driving seat and I was just along for the ride."
                        "And yet as soon as I'm all the way inside of her, all of that seems to change."
                        "It's like the sensation is just too much for her, like it's overwhelming her senses."
                        "At the same time I feel like a switch has been flicked on inside of my head."
                        "In that moment I come alive again, suddenly aware of every inch of my body."
                        "And in particular the inches that are currently lodged deep in Palla."
                        show palla missionary pleasure at hshake
                        play sexsfx1 fuck_calm
                        "Even as she leans back, surrendering to the sensations, I'm starting to move in earnest."
                        "I'm not talking about a gentle swinging into motion here either."
                        show palla missionary normal at hshake
                        "Already I'm picking up speed as I move back and forth, thrusting in and out."
                        "With every repetition of the motion, Palla becomes more helpless still."
                        "Lying back on the bed, she doesn't even try to hold onto me as I pound away at her."
                        "Instead she remains spread out beneath me, like she's almost helpless."
                        "There's no space inside of my head for observing anything more than that."
                        "Because by now I'm totally engrossed in the act, unable to think of anything else."
                        "Luckily for me, in doing so I seem to be totally overwhelming Palla too."
                        "Honestly, this is the most quiet and passive I've ever seen her!"
                        "Normally she'd be assailing me with a list of demands and requirements."
                        "But right now the only sound she's capable of making is a low moaning."
                        show palla missionary pleasure at hshake
                        "Palla's thighs move in time with my own, her breasts swaying from my motion."
                        "And though helpless and immobile, she still looks like a work of art."
                        "So much so that I feel myself beginning to lose control."
                        "I know that any moment I'm going to lose it."
                        "And so I have to decide how this thing is going to end."
                        show palla missionary normal at hshake
                        "Because heaven knows Palla's in no fit state to have an opinion on the matter."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                "There's really only one thing that I can do, which is to keep on doing what I'm doing right now."
                                "Pushing myself as deeply into Palla's ass as humanly possible until the final moment."
                                "And when that final moment comes, I just let it happen and let myself go."
                                "Which means that everything I have to give explodes inside of Palla."
                                show palla missionary cumshot ahegao at hshake
                                play sexsfx1 final_thrust
                                "The sensation seems to be too much for her, pushing her over the edge."
                                "And she cums even as I'm still reeling from the effects of my own orgasm."
                                $ hero.energy -= 2
                                $ palla.sub += 1
                            "Pull out":
                                "Using the last of my strength, I make an effort to free myself from Palla's ass."
                                "It takes everything that I have left, and for a moment I think that I'm not going to make it."
                                "But at the very last moment I manage to pull my cock out of Palla's ass."
                                show palla missionary cumshot out ahegao at hshake
                                play sexsfx1 pop_out
                                "The sensation seems to be too much for her, pushing her over the edge."
                                "And she cums even as I'm still reeling from the effects of it hitting me too."
                                show palla missionary -cumshot cum onbody at hshake
                                "Shooting my load over her exposed belly and painting it with sticky, white stripes."
                                $ hero.energy -= 2
                                $ palla.sub += 1
    else:

        "Palla instantly looks guilty, wincing and looking away as I demand an answer."
        show palla submissive at startle(0.1, 5)
        palla.say "Oh..."
        palla.say "I'm sorry, [hero.name]..."
        palla.say "I was just trying to give you a gentle poke, to get your attention."
        show palla sadsmile
        "Still rubbing the sore spot where Palla just jabbed me, I shuffle a couple of inches away from her."
        "And I make a mental note not to let my guard down around her like that again too."
        mike.say "I..."
        mike.say "I was just thinking that you have a nice place here, you know?"
        show palla stuned
        "Palla raises her eyebrows, adopting a quizzical expression."
        show palla happy at startle(0.1, 5)
        palla.say "Oh yeah, totally!"
        palla.say "It's pretty amazing for the price of the rent."
        palla.say "But then I usually let Shawn take care of that!"
        show palla normal
        show palla at startle(0.1, 5)
        show bg pallalivingroom at startle(0.1, 5)
        "I nod eagerly, doing the best I can to get round to my point."
        mike.say "What I mean, Palla..."
        mike.say "Is that a place this nice..."
        mike.say "Well, it puts me in a certain kind of mood, you know?"
        "Palla listens to me patiently, waiting until I've said my piece."
        show palla stuned
        "And then I see one of her eyebrows rise higher still."
        show palla talkative at startle(0.1, 5)
        palla.say "You are?!?"
        show palla talkative
        palla.say "In that case, you only have to ask, [hero.name]."
        palla.say "I'm always happy to oblige!"
        show palla flirt at center, traveling(1.4, 0.7, (640, 920))
        "As she says all of this, Palla is slowly inching towards me."
        "Making it totally clear that she's up for anything I might happen to have in mind."
        scene bg black
        show bg pallalivingroom at center
        show palla flirt at center, zoomAt(1.4, (640, 920))
        "Palla stands up and extends her hand towards me."
        show palla b submissive at startle(0.1, 5)
        palla.say "[hero.name]…"
        palla.say "Would you like to go somewhere a little more private?"
        palla.say "Somewhere we won't be disturbed?"
        show palla flirt
        "I leap to my feet almost the same moment Palla takes my hands in her own."
        "Already more than eager to take her up on the offer that she's making."
        "Of course this seems to please Palla immensely."
        "And she wastes no time in leading me into the hallway."
        show palla talkative at startle(0.1, 5)
        palla.say "The safest place for us to go would probably be my bedroom."
        palla.say "Or, if you're feeling a bit adventurous..."
        palla.say "We could always go out on the balcony?"
        show palla b flirt
        menu:
            "Choose to fuck in Shawn's room":

























                $ event_room = "shawnbedroom"
                "The moment that Palla mentions Shawn's room, my interest is piqued."
                "I've always felt a frisson of danger knowing this is his place too."
                "But the opportunity to actually get up to something in his bedroom - and on his bed too!"
                "Well, that's just too good of a chance to pass up."
                show palla surprised at startle(0.1, 5)
                mike.say "SHAWN'S ROOM!"
                mike.say "We have to fuck in Shawn's room!"
                "Palla looks more than a little surprised by how quickly I respond."
                show palla normal
                "Like she was sure that I'd need a little while to warm to the idea."
                "But she recovers her composure with admirable speed."
                show palla joke at startle(0.1, 5)
                palla.say "Okay, okay..."
                palla.say "So you want to live dangerously, yeah?"
                palla.say "Shawn's room it is!"
                show palla happy
                play sound door_open
                show bg shawnbedroom with fade
                $ game.room == "shawnbedroom"
                "Palla opens the door to Shawn's bedroom and ushers me inside."
                "As she closes it behind me, I take a look around."
                "I mean I know what the place looks like, as I've been in here before."
                "Only that was with Shawn when he wanted to show me something in his collection."
                "Or else he had to tell me something that he didn't want Palla overhearing."
                "But now I'm in here without him for the first time, about to use the facilities behind his back."
                "Though I do notice he seems to have acquired some new additions to his collection since I was last here."
                "And I can't help beginning to get drawn into the act of examining them more closely."
                "That is until Palla steps in front of me, already starting to strip off her clothes."
                "And when I don't come out with anything in the next couple of seconds, she coughs gently."
                show palla b submissive at startle(0.1, 5)
                palla.say "Ahem..."
                palla.say "Would you like me to take my clothes off now?"
                show palla flirt
                "Look, I know full well that I'm supposed to be the one taking Palla in hand here."
                "But there's still no way to prepare yourself for a question the likes of that one."
                "Especially when it's coming from a woman as outstandingly beautiful as Palla."
                "So it takes me a moment to be able to shake off the sheer amazement at being asked the question."
                "And even when I do so, I still feel like I'm stumbling over my words the whole time."
                mike.say "Ah..."
                mike.say "Y...yeah, Palla..."
                mike.say "I'd like that - I'd like it a lot!"
                show palla a happy at startle(0.1, 5)
                "Palla greets my answer with a nod and a smile, adding a little curtsey for good measure."
                "And then she starts to do as she's told, slowly stripping off one item of clothing after another."
                "Believe me, it's the kind of show that's impossible to ignore too."
                "Because Palla uses all of her skill as a model, posing and pouting as she does so."
                show palla a underwear happy with dissolve
                "It's all that I can do to clumsily start taking off my own clothes at the same time."
                show palla a topless normal with dissolve
                "And I even manage to almost fall over myself as I do that, I'm so enthralled by the show she's putting on."
                show palla b naked flirt with dissolve
                "Finally, when she's taken off the last shred of clothing, Palla turns her back to me."
                "Then she bends over, bracing her hands on something I can't see because I'm too busy staring at her ass."
                show palla a submissive at startle(0.1, 5)
                palla.say "Do you like what you see, master?"
                palla.say "Does what I have to offer meet with your approval?"
                palla.say "Because it's yours to do with as you wish - whatever you desire!"
                show palla flirt
                menu:
                    "Start with a blowjob":
                        "I have to admit that I'm a little flustered at how eager Palla seems to be."
                        "Because I was expecting to have to put in a lot more effort than that."
                        show palla at startle(0.1, 5)
                        show bg shawnbedroom at startle(0.1, 5)
                        mike.say "Well, Palla..."
                        mike.say "I was wondering if we could start things off slowly, you know?"
                        mike.say "Like, maybe help relieve some of the pressure I'm feeling - DOWN THERE?"
                        "I make a point of nodding towards my crotch as I emphasize those last two words."
                        show palla flirt at startle(0.2, 5)
                        "Palla's eyes go wide, and she nods her head eagerly."
                        show palla submissive at startle(0.1, 5)
                        palla.say "You mean you want me to go down on you, right?"
                        palla.say "Because if you do, then I'll get right on it."
                        palla.say "I just want to be sure that's what you're asking for, [hero.name]?"
                        show palla flirt
                        "I was awkward before because I was nervous."
                        "But now I'm fidgeting and twitching because I'm getting seriously horny."
                        "The mere thought of Palla going down on me is enough to get me hard."
                        "And so the knowledge it's actually going to happen affects me that much more."
                        mike.say "Oh yeah..."
                        mike.say "I mean, of course I'd like you to do that for me."
                        mike.say "It sounds like a great idea."
                        show palla underwear flirt at center, traveling(1.3, 0.5, (640, 880)) with dissolve
                        "Palla gives me a knowing look as she slides onto the floor in front of me."
                        show palla flirt at traveling(1.4, 1.5, (640, 1400))
                        "But then she turns her attention to the task at hand, if you'll pardon the pun."
                        "I watch in silence as deftly unzips my flies, then slides her fingers inside."
                        "And I can't keep from gasping from the sensation as those digits fins my manhood a moment later."
                        "Palla handles me with a firmness that makes the whole thing that much more exhilarating."
                        "But she never seems to go too far, or treat my cock roughly just for the sake of it."
                        "Like I said, the mere thought of this happening was already making me hard."
                        "So Palla has the extra challenge of getting it out in that same state."
                        "She moves it this way and that, making me gasp at the feeling as she does so."
                        "And then, all of a sudden, it pops out, almost quivering as it stands upright."
                        show palla submissive at startle(0.1, 5)
                        palla.say "Ooh..."
                        palla.say "May I proceed, master?"
                        "This time when I nod, my head is bobbing up and down like crazy."
                        "And I can't even manage to get my words out in a coherent manner."
                        mike.say "Y...yeh..."
                        mike.say "P...please!"
                        "Palla gives me a nod in return, pretending to be all business."
                        "But I can see the sheer pleasure on her face as she does so."
                        "Letting me know how much she loves being able to please me with her actions."
                        show palla blowjob shawnbedroom at center, zoomAt(1.1, (640, 720))
                        show palla blowjob lick underwear
                        "Though the moment that Palla opens her mouth and actually touches it with the tip of her tongue..."
                        "Oh man, that's when things really start to get wild for me!"
                        "Because Palla gives head in the same way that she performs for all of her photo-shoots."
                        "She devotes herself to the task one hundred percent, ignoring everything else."
                        show palla blowjob at center, startle(0.1, 5)
                        "Little by little, my cock begins to disappear into her mouth."
                        "And as it does so, I find hands gripping onto whatever's close enough."
                        play sexsfx1 bj_sucking loop
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Like I feel the need to hold onto something, anything, for dear life!"
                        "I can't begin to imagine what's actually going on inside of Palla's mouth right now."
                        "And I don't know what's causing the sensations that I'm feeling either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Lips, tongue and teeth must all be involved in some kind of way."
                        "But I'm damned if I can tell what each of them is doing to me."
                        "Palla has her eyes closed as her head bobs up and down too."
                        "As if she's determined to keep silent and for it to remain a secret."
                        "And believe me when I say that Palla's not skimping on things either."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "Because I can already feel my cock beginning to go ever deeper down her throat."
                        "Soon enough she's got the entire length of it in there."
                        "And part of me is worried how much further she's going to go!"
                        "But it turns out that I needn't have worried about such things."
                        show palla blowjob at startle(0.1,-10)
                        pause 0.2
                        show palla blowjob at startle(0.1,-10)
                        "As the sheer sensation of her throat squeezing me is just too much."
                        "And I can already feel myself starting to lose it."
                        stop sexsfx1
                        menu:
                            "Swallow":
                                "Luckily for me, Palla seems to sense it too."
                                "And when I make no move to change things, she acts accordingly."
                                "Keeping up the same pace as before, she gets herself ready."
                                play sound cum_inside
                                show palla blowjob hurt with vpunch
                                "And when I lose it, she simply swallows all that I have to give."
                                with vpunch
                                "Without missing a beat, Palla gulps down every last drop."
                                "Not stopping or gagging once throughout the entire act."
                            "Facial":
                                "Before it actually happens, I make an effort to pull back."
                                "Wanting to extricate myself from Palla's mouth, I try to rise up too."
                                "Luckily for me, she seems to sense what's happening."
                                play sound cum_inside
                                show palla blowjob cum hurt with vpunch
                                "And a moment later I feel my manhood being released."
                                with vpunch
                                "Palla doesn't move away after it's done either."
                                "Instead she sits perfectly still, waiting for the inevitable to happen."
                                "And when it does, she doesn't blink once as her face is spattered."
                                "I shoot my load straight into it, painting her features with thick, white stripes."
                                "Which soon being to run down her cheeks, and then drip off her chin."
                    "Just fuck her":
                        pass
                menu:
                    "Fuck her pussy":
                        "Yanking off the mast of my own clothes, I make straight for Palla."
                        "Part of me still can't believe that she's offering herself up to me like this."
                        "But a more primal part of me isn't even thinking about anything of the sort."
                        "Because it's one hundred percent focussed on the chance to get hold of Palla."
                        "Zeroing in on the exquisite prize that I can seer peeking out from between her buttocks."
                        scene bg black
                        show palla doggy shawnbedroom with fade
                        call check_condom_usage (palla) from _call_check_condom_usage_155
                        if _return == False:
                            return "leave_without_gain"
                        "Like I already said, there's only one thing of Palla's that I want right now."
                        "And every fleeting glimpse of it that I get as she moves her legs makes me all the more sure."
                        "I want that neat little pussy, and I want it as soon as I can get a hold of it!"
                        "For her part, Palla seems to be more than happy to put herself totally in my hands."
                        "She's bent over, pushing her ass out behind her and parting her thighs for me."
                        "Literally laying herself open and making no effort to keep me from touching her anywhere the whim takes me."
                        mike.say "Okay, Palla..."
                        mike.say "Here goes nothing!"
                        palla.say "I'm ready, [hero.name]..."
                        palla.say "Ready for whatever's coming next!"
                        show palla doggy with fade
                        "More than willing to trust Palla's reassurances, I clap my hands onto her haunches."
                        "And then I grip her firmly around the waist, pulling her backwards as I thrust forwards."
                        "The instant effect is that my cock pushes straight between her thighs."
                        "Needless to say I'm more than ready for her by now, hard as a rock."
                        "And so it squeezes through the gap without any problems, making Palla gasp."
                        "But the sound soon turns into a deep and helpless moan as the head touches her lips."
                        "I feel a shudder pass through Palla's entire body, and I see her nodding her head."
                        "She doesn't say a single word, or even look back over her shoulder at me."
                        "Yet I know instantly that what I'm seeing is a gesture of complete surrender."
                        show palla doggy at hshake
                        "And it spurs me on the repeat the same motion, rubbing myself against her."
                        "At the same time Palla tries to lower herself down, to make my task easier."
                        "I can already feel that she's seriously aroused, slippery and wet down there."
                        "But I'm definitely not ready for just how relaxed things are getting."
                        "Because the third pass sees things escalate quickly, and become much more intense."
                        "As I make my move, Palla seems to be in the perfect position."
                        "And without hesitation, she opens to the slightest application of pressure."
                        show palla doggy orgasm at hshake
                        play sexsfx1 slide_in
                        "All at once, her lips part and the head of my cock disappears inside her."
                        "But the force that I put into the movement isn't used up as it happens."
                        "Instead I keep right on going, pushing into Palla until I can go no deeper."
                        "She lowers her head, unable to do anything but surrender to what she's feeling."
                        "And at the same time I'm being overwhelmed by similar sensations."
                        "But where they seem to have cowed Palla, they're bringing me to life."
                        show palla doggy normal at hshake
                        play sexsfx1 fuck_moderate loop
                        "Without hesitation, I begin to move faster and with more determination than ever."
                        show palla doggy orgasm at hshake
                        "My third thrust follows close on the heels of the third."
                        show palla doggy normal at hshake
                        "And by the time of the fifth, I'm in a state of constant motion."
                        "All I can think about is thrusting into Palla, as hard and fast as I'm able."
                        "My hands are gripping her more tightly than ever, determined to keep her upright."
                        "And her entire body is shaking from the motion of my pounding away at her."
                        show palla doggy orgasm at hshake
                        "There's no chance in hell of me stopping or even slowing down to check on Palla now."
                        "Which means I'm more thankful than ever for her basically putting herself in my hands."
                        "So I just devote myself to the task at hand, fucking her brains out with all my might."
                        "And not stopping until one or both of us collapses into a heap of helpless, quivering flesh."
                        "I seem to lose all sense of time as I focus solely on hammering away at Palla."
                        "My eyes are staring at her breasts as they sway wildly beneath her."
                        show palla doggy normal at hshake
                        "And my ears are filled with the sound of my thighs slapping against hers."
                        "So when I feel something change inside of me, it comes as a genuine surprise."
                        "Making slow down as I realise that I'm on the verge of cuming."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                if CONDOM:
                                    "Remembering that we chose to use a condom, I give a silent thanks to the gods of contraception."
                                    show palla doggy ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla."
                                    "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                    "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                    $ palla.love += 2
                                else:

                                    "There's nothing that I can do to hold on, not even for a second longer."
                                    show palla doggy ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla."
                                    "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                    "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                    $ palla.impregnate()
                                    $ palla.love += 5
                            "Pull out":
                                "Using the last of my energy, I pull backwards and out of Palla before it happens."
                                show palla doggy at hshake
                                play sexsfx1 slide_out
                                "A moment later I lose it completely, shooting my load over her buttocks and the small of her back."
                                show palla doggy orgasm at hshake
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                show palla doggy ahegao at hshake
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.sub += 3
                    "Fuck her ass":
                        "Yanking off the mast of my own clothes, I make straight for Palla."
                        "Part of me still can't believe that she's offering herself up to me like this."
                        "But a more primal part of me isn't even thinking about anything of the sort."
                        "Because it's one hundred percent focussed on the chance to get hold of Palla."
                        "Zeroing in on the exquisite prize that I can seer peeking out from between her buttocks."
                        scene bg black
                        show palla doggy shawnbedroom with fade
                        "Like I already said, there's only one thing of Palla's that I want right now."
                        "And every fleeting glimpse of it that I get as she moves her legs makes me all the more sure."
                        "I want that neat little butt-hole, and I want it as soon as I can get a hold of it!"
                        "For her part, Palla seems to be more than happy to put herself totally in my hands."
                        "She's bent over, pushing her ass out behind her and parting her thighs for me."
                        "Literally laying herself open and making no effort to keep me from touching her anywhere the whim takes me."
                        mike.say "Okay, Palla..."
                        mike.say "Here goes nothing!"
                        palla.say "I'm ready, [hero.name]..."
                        palla.say "Ready for whatever's coming next!"
                        show palla doggy orgasm with fade
                        "More than willing to trust Palla's reassurances, I clap my hands onto her haunches."
                        "And then I grip her firmly around the waist, pulling her backwards as I thrust forwards."
                        "The instant effect is that my cock pushes straight between her thighs."
                        "Needless to say I'm more than ready for her by now, hard as a rock."
                        "And so it squeezes inbetween her buttocks without any problems, making Palla gasp."
                        "But the sound soon turns into a deep and helpless moan as the head touches her hole."
                        "I feel a shudder pass through Palla's entire body, and I see her nodding her head."
                        "She doesn't say a single word, or even look back over her shoulder at me."
                        "Yet I know instantly that what I'm seeing is a gesture of complete surrender."
                        show palla doggy normal at hshake
                        "And it spurs me on the repeat the same motion, rubbing myself against her."
                        "At the same time Palla tries to lower herself down, to make my task easier."
                        "I can already feel that she's seriously aroused, soft and relaxed she is down there."
                        "But I'm definitely not ready for just how relaxed things are getting."
                        "Because the third pass sees things escalate quickly, and become much more intense."
                        "As I make my move, Palla seems to be in the perfect position."
                        "And without hesitation, she opens to the slightest application of pressure."
                        show palla doggy orgasm at hshake
                        play sexsfx1 slide_in
                        "All at once, her muscles relax even further and the head of my cock disappears inside her."
                        "But the force that I put into the movement isn't used up as it happens."
                        "Instead I keep right on going, pushing into Palla until I can go no deeper."
                        "She lowers her head, unable to do anything but surrender to what she's feeling."
                        "And at the same time I'm being overwhelmed by similar sensations."
                        "But where they seem to have cowed Palla, they're bringing me to life."
                        show palla doggy normal at hshake
                        play sexsfx1 fuck_moderate loop
                        "Without hesitation, I begin to move faster and with more determination than ever."
                        show palla doggy orgasm at hshake
                        "My third thrust follows close on the heels of the third."
                        show palla doggy normal at hshake
                        "And by the time of the fifth, I'm in a state of constant motion."
                        "All I can think about is thrusting into Palla, as hard and fast as I'm able."
                        "My hands are gripping her more tightly than ever, determined to keep her upright."
                        "And her entire body is shaking from the motion of my pounding away at her."
                        show palla doggy orgasm at hshake
                        "There's no chance in hell of me stopping or even slowing down to check on Palla now."
                        "Which means I'm more thankful than ever for her basically putting herself in my hands."
                        "So I just devote myself to the task at hand, fucking her brains out with all my might."
                        "And not stopping until one or both of us collapses into a heap of helpless, quivering flesh."
                        "I seem to lose all sense of time as I focus solely on hammering away at Palla."
                        "My eyes are staring at her breasts as they sway wildly beneath her."
                        show palla doggy normal at hshake
                        "And my ears are filled with the sound of my thighs slapping against hers."
                        "So when I feel something change inside of me, it comes as a genuine surprise."
                        "Making slow down as I realise that I'm on the verge of cuming."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                "There's nothing that I can do to hold on, not even for a second longer."
                                "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla's ass."
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                show palla doggy ahegao at hshake
                                play sexsfx1 final_thrust
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.love += 3
                            "Pull out":
                                "Using the last of my energy, I pull backwards and out of Palla's ass before it happens."
                                show palla doggy at hshake
                                play sexsfx1 slide_out
                                "A moment later I lose it completely, shooting my load over her buttocks and the small of her back."
                                show palla doggy orgasm at hshake
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                show palla doggy ahegao at hshake
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.sub += 3
            "Choose to fuck on the balcony":
                $ event_room = "balcony"
                "The sound of a solid door between us and the rest of the apartment sounds pretty good right now."
                "Especially if Shawn happens to show up in the middle of what I'm hoping is going to happen next."
                "But there's just something about the idea of doing it with Palla on the balcony."
                "A sense of danger and excitement that I can't ignore, no matter how hard I try."
                mike.say "I think I like the sound of the balcony, Palla..."
                mike.say "So let's head there, okay?"
                "If Palla was hoping that I'd choose her room, she's doing a good job of hiding it."
                show palla normal at startle(0.1, 5)
                "As she simply nods her head with a smile, already beginning to lead the way."
                show palla submissive at startle(0.1, 5)
                palla.say "Whatever you say, [hero.name]."
                palla.say "Come on..."
                palla.say "It's just down here."
                show palla normal
                play sound door_open
                show bg balcony with fade
                "As soon as we reach the door to the balcony, Palla pushes it open."
                "And then she ushers me outside, closing the door behind me."
                "I do the best I can to play it off and act natural."
                "But the truth is that I'm more than a little nervous about being out here, overlooking the city."
                "I'm in the act of taking in the incredible view and telling myself nobody's going to be able to see us up here."
                "But then I see that she's standing silently in front of me, as if waiting for my next order."
                $ hero.morality -= 3
                "And when I don't come out with anything in the next couple of seconds, she coughs gently."
                show palla b submissive at startle(0.1, 5)
                palla.say "Ahem..."
                palla.say "Would you like me to take my clothes off now?"
                show palla flirt
                "Look, I know full well that I'm supposed to be the one taking Palla in hand here."
                "But there's still no way to prepare yourself for a question the likes of that one."
                "Especially when it's coming from a woman as outstandingly beautiful as Palla."
                "So it takes me a moment to be able to shake off the sheer amazement at being asked the question."
                "And even when I do so, I still feel like I'm stumbling over my words the whole time."
                mike.say "Ah..."
                mike.say "Y...yeah, Palla..."
                mike.say "I'd like that - I'd like it a lot!"
                show palla a happy at startle(0.1, 5)
                "Palla greets my answer with a nod and a smile, adding a little curtsey for good measure."
                "And then she starts to do as she's told, slowly stripping off one item of clothing after another."
                "Believe me, it's the kind of show that's impossible to ignore too."
                "Because Palla uses all of her skill as a model, posing and pouting as she does so."
                "It's all that I can do to clumsily start taking off my own clothes at the same time."
                "And I even manage to almost fall over myself as I do that, I'm so enthralled by the show she's putting on."
                hide palla a happy with dissolve
                show palla b naked flirt
                "Finally, when she's taken off the last shred of clothing, Palla turns her back to me."
                "Then she bends over, bracing her hands on something I can't see because I'm too busy staring at her ass."
                show palla a submissive at startle(0.1, 5)
                palla.say "Do you like what you see, master?"
                palla.say "Does what I have to offer meet with your approval?"
                palla.say "Because it's yours to do with as you wish - whatever you desire!"
                show palla flirt
                menu:
                    "Fuck her pussy":
                        "Yanking off the mast of my own clothes, I make straight for Palla."
                        "Part of me still can't believe that she's offering herself up to me like this."
                        "But a more primal part of me isn't even thinking about anything of the sort."
                        "Because it's one hundred percent focussed on the chance to get hold of Palla."
                        "Zeroing in on the exquisite prize that I can seer peeking out from between her buttocks."
                        "I instantly push her against the bay windows."
                        scene bg black
                        show palla stand pleasure balcony dick with fade
                        call check_condom_usage (palla) from _call_check_condom_usage_156
                        if _return == False:
                            return "leave_without_gain"
                        "Like I already said, there's only one thing of Palla's that I want right now."
                        "And every fleeting glimpse of it that I get as she moves her legs makes me all the more sure."
                        "I want that neat little pussy, and I want it as soon as I can get a hold of it!"
                        "For her part, Palla seems to be more than happy to put herself totally in my hands."
                        "She's bent over, pushing her ass out behind her and parting her thighs for me."
                        "Literally laying herself open and making no effort to keep me from touching her anywhere the whim takes me."
                        mike.say "Okay, Palla..."
                        mike.say "Here goes nothing!"
                        palla.say "I'm ready, [hero.name]..."
                        palla.say "Ready for whatever's coming next!"
                        "More than willing to trust Palla's reassurances, I clap my hands onto her haunches."
                        "And then I grip her firmly around the waist, pulling her backwards as I thrust forwards."
                        "The instant effect is that my cock pushes straight between her thighs."
                        "Needless to say I'm more than ready for her by now, hard as a rock."
                        "And so it squeezes through the gap without any problems, making Palla gasp."
                        show palla stand balcony normal -dick at hshake
                        "But the sound soon turns into a deep and helpless moan as the head touches her lips."
                        "I feel a shudder pass through Palla's entire body, and I see her nodding her head."
                        "She doesn't say a single word, or even look back over her shoulder at me."
                        "Yet I know instantly that what I'm seeing is a gesture of complete surrender."
                        show palla stand pleasure at hshake
                        "And it spurs me on the repeat the same motion, rubbing myself against her."
                        "At the same time Palla tries to lower herself down, to make my task easier."
                        "I can already feel that she's seriously aroused, slippery and wet down there."
                        "But I'm definitely not ready for just how relaxed things are getting."
                        "Because the third pass sees things escalate quickly, and become much more intense."
                        "As I make my move, Palla seems to be in the perfect position."
                        "And without hesitation, she opens to the slightest application of pressure."
                        play sexsfx1 slide_in
                        "All at once, her lips part and the head of my cock disappears inside her."
                        "But the force that I put into the movement isn't used up as it happens."
                        "Instead I keep right on going, pushing into Palla until I can go no deeper."
                        "She lowers her head, unable to do anything but surrender to what she's feeling."
                        "And at the same time I'm being overwhelmed by similar sensations."
                        "But where they seem to have cowed Palla, they're bringing me to life."
                        "Without hesitation, I begin to move faster and with more determination than ever."
                        show palla stand at hshake
                        play sexsfx1 fuck_moderate loop
                        "My third thrust follows close on the heels of the third."
                        show palla stand at hshake
                        "And by the time of the fifth, I'm in a state of constant motion."
                        "All I can think about is thrusting into Palla, as hard and fast as I'm able."
                        "My hands are gripping her more tightly than ever, determined to keep her upright."
                        "And her entire body is shaking from the motion of my pounding away at her."
                        show palla stand at hshake
                        "There's no chance in hell of me stopping or even slowing down to check on Palla now."
                        "Which means I'm more thankful than ever for her basically putting herself in my hands."
                        "So I just devote myself to the task at hand, fucking her brains out with all my might."
                        show palla stand at hshake
                        "And not stopping until one or both of us collapses into a heap of helpless, quivering flesh."
                        "I seem to lose all sense of time as I focus solely on hammering away at Palla."
                        "My eyes are staring at her breasts as they sway wildly beneath her."
                        "And my ears are filled with the sound of my thighs slapping against hers."
                        "So when I feel something change inside of me, it comes as a genuine surprise."
                        "Making slow down as I realise that I'm on the verge of cuming."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                if CONDOM:
                                    "Remembering that we chose to use a condom, I give a silent thanks to the gods of contraception."
                                    show palla stand ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla."
                                    "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                    "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                    $ palla.love += 2
                                else:
                                    "There's nothing that I can do to hold on, not even for a second longer."
                                    show palla stand cum ahegao at hshake
                                    play sexsfx1 final_thrust
                                    "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla."
                                    "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                    "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                    $ palla.impregnate()
                                    $ palla.love += 5
                            "Pull out":
                                show palla stand dick
                                "Using the last of my energy, I pull backwards and out of Palla before it happens."
                                show palla stand dick cum ahegao at hshake
                                play sexsfx1 slide_out
                                "A moment later I lose it completely, shooting my load over her buttocks and the small of her back."
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.sub += 2
                    "Fuck her ass":
                        "Yanking off the mast of my own clothes, I make straight for Palla."
                        "Part of me still can't believe that she's offering herself up to me like this."
                        "But a more primal part of me isn't even thinking about anything of the sort."
                        "Because it's one hundred percent focussed on the chance to get hold of Palla."
                        "Zeroing in on the exquisite prize that I can seer peeking out from between her buttocks."
                        "I instantly push her against the bay windows."
                        scene bg black
                        show palla stand balcony dick pleasure with fade
                        "Like I already said, there's only one thing of Palla's that I want right now."
                        "And every fleeting glimpse of it that I get as she moves her legs makes me all the more sure."
                        "I want that neat little butt-hole, and I want it as soon as I can get a hold of it!"
                        "For her part, Palla seems to be more than happy to put herself totally in my hands."
                        "She's bent over, pushing her ass out behind her and parting her thighs for me."
                        "Literally laying herself open and making no effort to keep me from touching her anywhere the whim takes me."
                        mike.say "Okay, Palla..."
                        mike.say "Here goes nothing!"
                        palla.say "I'm ready, [hero.name]..."
                        palla.say "Ready for whatever's coming next!"
                        show palla stand pleasure with fade
                        "More than willing to trust Palla's reassurances, I clap my hands onto her haunches."
                        "And then I grip her firmly around the waist, pulling her backwards as I thrust forwards."
                        "The instant effect is that my cock pushes straight between her thighs."
                        "Needless to say I'm more than ready for her by now, hard as a rock."
                        "And so it squeezes inbetween her buttocks without any problems, making Palla gasp."
                        show palla stand balcony normal -dick at hshake
                        "But the sound soon turns into a deep and helpless moan as the head touches her hole."
                        "I feel a shudder pass through Palla's entire body, and I see her nodding her head."
                        "She doesn't say a single word, or even look back over her shoulder at me."
                        "Yet I know instantly that what I'm seeing is a gesture of complete surrender."
                        "And it spurs me on the repeat the same motion, rubbing myself against her."
                        "At the same time Palla tries to lower herself down, to make my task easier."
                        show palla stand pleasure at hshake
                        "I can already feel that she's seriously aroused, soft and relaxed she is down there."
                        "But I'm definitely not ready for just how relaxed things are getting."
                        "Because the third pass sees things escalate quickly, and become much more intense."
                        "As I make my move, Palla seems to be in the perfect position."
                        "And without hesitation, she opens to the slightest application of pressure."
                        show palla stand normal at hshake
                        play sexsfx1 slide_in
                        "All at once, her muscles relax even further and the head of my cock disappears inside her."
                        "But the force that I put into the movement isn't used up as it happens."
                        "Instead I keep right on going, pushing into Palla until I can go no deeper."
                        "She lowers her head, unable to do anything but surrender to what she's feeling."
                        "And at the same time I'm being overwhelmed by similar sensations."
                        "But where they seem to have cowed Palla, they're bringing me to life."
                        show palla stand at hshake
                        play sexsfx1 fuck_moderate loop
                        "Without hesitation, I begin to move faster and with more determination than ever."
                        show palla stand at hshake
                        "My third thrust follows close on the heels of the third."
                        show palla stand at hshake
                        "And by the time of the fifth, I'm in a state of constant motion."
                        "All I can think about is thrusting into Palla, as hard and fast as I'm able."
                        "My hands are gripping her more tightly than ever, determined to keep her upright."
                        "And her entire body is shaking from the motion of my pounding away at her."
                        "There's no chance in hell of me stopping or even slowing down to check on Palla now."
                        "Which means I'm more thankful than ever for her basically putting herself in my hands."
                        show palla stand at hshake
                        "So I just devote myself to the task at hand, fucking her brains out with all my might."
                        "And not stopping until one or both of us collapses into a heap of helpless, quivering flesh."
                        "I seem to lose all sense of time as I focus solely on hammering away at Palla."
                        "My eyes are staring at her breasts as they sway wildly beneath her."
                        show palla stand at hshake
                        "And my ears are filled with the sound of my thighs slapping against hers."
                        "So when I feel something change inside of me, it comes as a genuine surprise."
                        "Making slow down as I realise that I'm on the verge of cuming."
                        stop sexsfx1
                        menu:
                            "Cum inside":
                                "There's nothing that I can do to hold on, not even for a second longer."
                                show palla stand pleasure cum at hshake
                                "And a moment later I feel it happen, my orgasm sweeping over me and making me lose it inside of Palla's ass."
                                show palla stand ahegao at hshake
                                play sexsfx1 final_thrust
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.love += 3
                            "Pull out":
                                show palla stand pleasure dick
                                play sexsfx1 pop_out
                                "Using the last of my energy, I pull backwards and out of Palla's ass before it happens."
                                show palla stand cum at hshake
                                "A moment later I lose it completely, shooting my load over her buttocks and the small of her back."
                                show palla stand ahegao at hshake
                                "It seems to have a similar effect upon her too, meaning that I have to hold on even tighter than before."
                                "And so together we ride it out, both in the grip of our orgasms, hearts pounding in our chests."
                                $ palla.sub += 3
    stop sound fadeout 1
    stop sexsfx1 fadeout 1
    show expression f"bg {event_room}"
    show palla b naked flirt at center, zoomAt(1, (640, 720))
    with fade
    "I can't remember the last time I felt as exhausted as I do right now."
    "Or as completely and utterly satisfied either."
    "All I want to do is surrender to my fatigue and fall asleep."
    show palla b underwear with dissolve
    "But Palla seems to be making a point of collecting her clothes and beginning to get dressed."
    "So I resign myself to following her lead and begin to do the same thing too."
    "All the time neither of us seems to feel the need to speak a single word."
    "It's like what we just shared has taken us beyond the need for conversation."
    "And at least for a little while, we're able to communicate on a higher level."
    show palla b casual with dissolve
    "I have no idea if this is going to last, or even if it's anything more than my own imagination."
    "But what I do know is that Palla and I just made a very real and very lasting connection."
    scene bg black with dissolve
    $ palla.sexperience += 1
    $ hero.energy -= 2
    $ game.active_date.stay_coffee = False
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
