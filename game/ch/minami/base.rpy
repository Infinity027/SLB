init python:
    Activity(**{
    "name": "watch_tv_with_minami",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with Minami",
    "max_girls": 1,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            MinStat("fun", 0)),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        InvalidActivities("watch_tv_with_everyone_male"),
        ],
    "label": "minami_tv",
    })

    Activity(**{
    "name": "play_in_the_pool_with_minami",
    "label": "minami_play_pool",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with Minami",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("male")),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 10),
            ),
        PersonTarget(sasha,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    })

    Event(**{
    "name": "minami_give_phone_number",
    "label": "give_phone_number",
    "girl": "minami",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(minami,
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
    "name": "minami_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(minami,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "minami",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "minami_auto_greet",
    "label": "auto_greet",
    "girl": "minami",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(minami,
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
    "name": "minami_auto_chat",
    "label": "auto_chat",
    "girl": "minami",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(minami,
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
    "name": "minami_are_you_sick",
    "label": "are_you_sick",
    "girl": "minami",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (minami, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "minami_ask_out",
    "label": "ask_out",
    "girl": "minami",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(minami,
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
    "name": "minami_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "minami",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "minami_masturbation",
    "priority": 500,
    "label": "minami_masturbation",
    "duration": 1,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsGender("male"),
            IsActivity("knock_bedroom5")),
        PersonTarget(minami,
            Not(IsHidden()),
            IsRoom("bedroom5"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "minami_couch_fun",
    "label": "minami_couch_fun",
    "duration": 1,
    "priority": 0,
    "conditions": [
        'Room.find("livingroom").get_present_girls_ids_by_tag() == ["minami"]',
        PersonTarget(minami,
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                IsRoom("livingroom"),),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "unlock_minami_compliment",
    "label": "unlock_minami_compliment",
    "conditions": [
        PersonTarget(minami,
            MinStat("siscon", 75)
            ),
        ],
    "do_once": True,
    "quit": False,
    })

label minami_couch_fun:
    if game.hour >= 20:
        "It's getting pretty late and I'm sure that I've heard everyone going to bed already."
        "But I'm not feeling in the least bit sleepy myself, and now I have the house to myself."
        "Don't worry, it's not like I'm about to strip off and start walking around naked!"
        "It's just unusual for me to be the only one up and about, so I want to make the most of it."
    else:
        "I'm pretty sure that I've heard everyone going out, leaving the house for myself"
        "Don't worry, it's not like I'm about to strip off and start walking around naked!"
        "It's just unusual for me to be the only one home, so I want to make the most of it."
    "I start by wandering into the kitchen, thinking about fixing myself something to eat."
    scene bg kitchen
    "Walking across the room, I reach out to open the fridge."
    "But that's when I hear a sound coming from the living room."
    "Just for the record, I'm not saying that it made me jump out of my skin."
    "More like I'm suddenly aware that there could be somebody else awake too."
    "I turn and walk towards the living room, intending to see who it is."
    "Not that I'm going to tell them off, as they have every right to be there."
    "I just want to know if they're planning on staying up for a while."
    "If they are, then that'll put a cramp on my plans and I'll have to do something else instead."
    "But as I get closer to the living room door, I start to slow down and move quietly."
    "And that's because I hear the sound again, though more clearly this time."
    "It puts me in mind of a muffled gasp, like somebody'd trying to keep quiet in there too."
    "Now curiosity is starting to get the better of me."
    "Rather than walking into the living room, I creep up to the door."
    scene bg livingroom
    "I can see that the TV's on and there's someone sat on the sofa."
    "Their dark hair makes me think that it's Sasha for a moment."
    "But then I see that the person is far too short and petite for that to be the case."
    "And if it's not Sasha, the it can only be Minami."
    "But what in the hell is she doing in there?"
    "The volume on the TV is turned down low."
    "If she hadn't made those noises, I'd never have known she was there at all."
    "It's then that I hear Minami make the same noise again."
    "The difference is that this time I'm looking straight at her when she does so."
    scene minami mast
    show minami mast livingroom
    "My eyes go wide as I watch Minami's back arch and her head tilt backwards."
    "And I can see the silhouette of a hand moving between her legs."
    "Fucking hell - she's playing with herself!"
    "She's actually masturbating on the sofa!"
    "I can't see what Minami's watching on the TV to get herself off."
    show minami mast spread
    "But that's nowhere near as interesting as the chance to watch her stroking her pussy!"
    "Whoa...wait a minute."
    "Should I really be doing this?"
    menu:
        "Leave":
            "I can't help shuddering at the mere thought of what I was about to do."
            "Actually watching Minami masturbate from out here in the hallway?"
            "No way, I'm better than that!"
            scene bg kitchen
            $ game.room = "kitchen"
            "As quickly and quietly as I can, I turn and hurry away."
        "Stay and watch":
            "I shake my head, suddenly wondering why I was getting so worried just now."
            "So long as Minami doesn't know that I'm here, of course it doesn't matter."
            show minami mast vaginal
            "What she doesn't know can't hurt her, and she's actually helping me out too."
            "Watching her gives me something to keep myself occupied with tonight."
            "And I'm sure I'll sleep well with an image of Minami playing with herself in my mind!"
            "So I lean in closer, trying to get the best view that I possibly can."
            show minami mast spread
            "I guess that Minami hasn't been at it long, because she's going slowly."
            "She's whimpering and moaning as her fingers trace her lips."
            "I watch as her speed picks up, fingers moving ever faster."
            "Now it looks and sounds like she's biting her lip."
            "Her free hand wanders to her chest."
            show minami mast vaginal
            "And then she begins to play with one of her breasts too!"
            "Minami's panting by now, almost squealing as she pleasures herself."
            "Seeing her struggle to keep from making too much sound is amazing."
            menu:
                "Masturbate":
                    "I can almost feel the tension that must be building up inside of her right now!"
                    "My own heart is beating faster as I keep on gazing at her."
                    show minami mast spread
                    "And it should come as no surprise that I'm as hard as a rock too!"
                    "I can't help myself, it's like my hand has a mind of its own."
                    "The first thing I know about it is when I feel my cock against my fingers."
                    "And then I'm going at it just as hard as Minami is herself!"
                    "It feels like we're doing this thing together."
                    show minami mast vaginal
                    "My hand is moving in time with Minami's."
                    "And I swear that we're beginning to breath in time too."
                    "I wonder if she can sense that I'm here, sharing the moment with her."
                    "Suddenly Minami seems to lose control for a moment."
                    "She cries out louder than before, but then stifles the sound."
                    "It's all I can do to keep from crying out too."
                    "Because there's no way I can hold on while watching her cum!"
                    "I tremble as I shoot my load inside of my shorts."
                    "The cum runs down over my fingers and into the palm of my hand."
                    "But I hardly notice as I turn and bolt towards my room."
                    "Once there, I clean myself up and try to make my heart stop pounding."
                    "And I just hope that I can sleep with the image of Minami burned into my mind!"
                    $ hero.fun += 1
                    $ hero.energy -= 1
                "Keep watching":
                    "I can almost feel the tension that must be building up inside of her right now!"
                    "My own heart is beating faster as I keep on gazing at her."
                    show minami mast spread
                    "And it should come as no surprise that I'm as hard as a rock too!"
                    "Suddenly Minami seems to lose control for a moment."
                    "She cries out louder than before, but then stifles the sound."
                    "It's all I can do to keep from crying out too."
                    show minami mast vaginal
                    "And that's because I know Minami's cumming."
                    "Before she's done, I bolt away towards my room."
                    "If I can just keep the image of her like that in my mind's eye."
                    "Then I can put it to good use doing the same thing as Minami too!"
    return

label minami_masturbation:
    $ hero.cancel_activity()
    "I swear that I'm only passing the bottom of the attic stairs on my way to the bathroom when I hear the sound."
    "And normally, I'd never dream of sticking my nose into what Minami gets up to behind her closed bedroom door."
    "Yet this is such an odd sound that I can't help being drawn back to the stairs and then up them."
    "Sure, I'm curious as to just what the hell could be making such a strange noise."
    "But this is my kid sister we're talking about here, and I kind of have a duty to check she's okay."
    "I guess that the fact I sneak up the attic stairs as quietly as I can kind of makes that sound like a lie."
    "Though I console myself with the thought that if Minami is actually fine, I don't want her knowing I was checking up on her."
    "It doesn't take me long to climb to the top of the stairs and find myself in front of Minami's bedroom door."
    "The sound is louder now, and I can begin to make out what could be groan coming from within."
    "She could be in pain or something like that, but then again it could be nothing more than a bad dream."
    menu:
        "Walk away":
            "I think that I've reached the point of no return here."
            "Minami's clearly not in any kind of pressing danger."
            "If she was, then she'd be shouting for help or at least crying out in pain."
            "The only reason to go any further would be to satisfy my own curiosity and nothing else."
            "I might have an obligation to look out for Minami and try to keep her safe as best I can."
            "But that doesn't mean I can just go barging into her room whenever I please."
            "So as quietly as I climbed up them, I walk back down the stairs and to the bathroom."
        "Check what's going on":
            "I know that the right thing to do would be to knock on the door and announce my presence out here."
            "But then maybe the even righter thing to do would have been to just turn around and walk away."
            "So as I'm kind of already committed to having a well-meaning little snoop, I get down on a level with the keyhole."
            "Putting my eye to the hole, I have to squint and blink until my vision adjusts."
            "But within a few moments, I begin to be able to make out the familiar sights of Minami's room."
            "At first I can't tell where she is, until I notice movement from where her bed sits against the wall."
            "My eye is drawn in that direction, and I see her laid on top of the crumpled bedclothes."
            "She seems to be rolling around on the bed, almost writhing on the spot where she's laid."
            "My first thought is that Minami must be having a bad dream or a nightmare."
            "But then she raises her back, letting me see her more of her than before."
            if minami.sexperience % 3 == 2:
                show minami mast anal
            else:
                show minami mast
            "Instantly I notice that her eyes are open and she looks very much awake."
            "She also seems to be very much naked!"
            "Minami's hands are doing something that I can't quite make out."
            "Whatever it is, her groans seem to be just one of the physical reactions it's causing."
            "Is she scratching an itch?"
            "Rubbing cream into something?"
            "Or is she actually...masturbating?!?"
            if minami.sub >= 50 and game.week_day % 2 == 0:
                "I watch in sheer, morbid fascination as Minami's familiar features contort in pleasure."
                "Her fingers are already working away pretty fast, but they're getting faster still."
                "She starts rummaging her bedside table and soon a small pink device replace her fingers."
                show minami mast toy
                "She starts to let out little yelps, almost like the yipping of a small animal."
                "And between them, I can hear her gasping out desperate words."
                minami.say "Ooo..."
                minami.say "Ah, fuck yes..."
                minami.say "I waited so long for this..."
                minami.say "And you're so...big!"
                "I know with every fibre of my being that I shouldn't be watching this."
                "But even so, I can't begin to tear myself away from the keyhole."
                "Worse still, I know that my cock is already rock-hard inside of my shorts."
                minami.say "Oh, big bro..."
                minami.say "It feels SO good inside of me!"
                "Suddenly I can feel a sense of panic rising up inside of me."
            else:
                "I watch in sheer, morbid fascination as Minami's familiar features contort in pleasure."
                "Her fingers are already working away pretty fast, but they're getting faster still."
                "She starts to let out little yelps, almost like the yipping of a small animal."
                "And between them, I can hear her gasping out desperate words."
                if minami.sexperience % 3 != 2:
                    show minami mast spread
                minami.say "Ooo..."
                minami.say "Ah, fuck yes..."
                minami.say "I waited so long for this..."
                minami.say "And you're so...big!"
                "I know with every fibre of my being that I shouldn't be watching this."
                if minami.sexperience % 3 != 2:
                    show minami mast vaginal
                "But even so, I can't begin to tear myself away from the keyhole."
                "Worse still, I know that my cock is already rock-hard inside of my shorts."
                if minami.sexperience % 3 != 2:
                    show minami mast spread
                minami.say "Oh, big bro..."
                minami.say "It feels SO good inside of me!"
                show minami mast vaginal
            "Minami's not just masturbating."
            "She's masturbating over me!"
            "She's masturbating over me, and I'm watching her do it!"
            "Before I can tear my eye away from the keyhole, Minami lets out a genuinely orgasmic cry."
            "Her eyes roll back into her head, which in turn is buried in her pillows."
            "I watch in mute horror as she finishes herself off, rubbing my shorts against her pussy the whole time."
            "As I finally shake myself back to reality and creep off down the stairs, I feel like I'm in a state of shock."
            "But all the same, it's hard to tell out of all I just saw, what affected me the most."
            "Was it the fact that Minami was masturbating over me?"
            "Or the fact that I watched her the whole time she was doing it?"
    return

label minami_cheated(action, cheat_npc=None):
    show minami
    if cheat_npc and Harem.together(cheat_npc, minami):
        show minami flirt
        minami.say "Aren't you forgetting something?"
        show minami
        "And without warning Minami kisses me."
        $ minami.love += 1
        $ minami.flags.kiss += 1
    elif minami.sub >= 75:
        show minami hunt
        show fx heart
        $ minami.sub += 1
        "I see Minami looking at me [action] someone else with envy and lust in her eyes."
    else:
        show minami sad
        show fx anger
        if cheat_npc:
            $ minami.flags.cheatedby = cheat_npc.id
        $ loss = 5
        if minami.flags.girlfriend or minami.flags.fiance:
            $ loss += 5
        $ minami.love -= loss
        "I see Minami looking at me [action] someone else with tears in her eyes..."
    hide minami
    return

label minami_bye(bye_outfit=None):
    call npc_bye_outfit (npc=minami, bye_outfit=bye_outfit) from _call_npc_bye_outfit_15
    $ (day, h, activity, bye_outfit) = _return
    if not activity == minami.activity:
        if day != game.week_day:
            $ minami.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ minami.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"minami {bye_outfit}")
        if activity["activity"] == "sleep":
            minami.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            minami.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            minami.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            minami.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            minami.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            minami.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            minami.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            minami.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            minami.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            minami.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            minami.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            minami.say "I'll go get dressed."
        hide minami
    return

label minami_play_pool:
    show playing water pool minami
    "I play in the pool with Minami."
    $ minami.love += 1
    $ minami.flags.greeted = TemporaryFlag(True, 1)
    return

label minami_tv:
    call minami_greet from _call_minami_greet
    if hero.charm >= 40 - minami.love or minami.activity_name == "tv":
        call watch_tv_with (minami) from _call_watch_tv_with_3
    else:
        show minami
        minami.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide minami
    return

label minami_tv_reaction:
    minami.say "Why not."
    return

label minami_porn_bad_reaction:
    minami.say "Sorry, I don't want to watch this sort of thing."
    return

label minami_greet:
    if renpy.has_label(f"minami_greet_dialogues_{hero.gender}") and not minami.flags.greeted:
        scene expression f"bg {game.room}"
        show minami
        $ minami.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            if minami.flags.mikeNickname:
                minami.say "Hello, [hero.name]."
            else:
                minami.say "Hello, big bro."
        elif result == 2:
            minami.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                if minami.flags.mikeNickname:
                    minami.say "Good morning [hero.name]."
                else:
                    minami.say "Good morning big bro."
            elif game.hour < 19:
                if minami.flags.mikeNickname:
                    minami.say "Good afternoon [hero.name]."
                else:
                    minami.say "Good afternoon big bro."
            else:
                if minami.flags.mikeNickname:
                    minami.say "Good evening [hero.name]."
                else:
                    minami.say "Good evening big bro."
        call expression f"minami_greet_dialogues_{hero.gender}" from _call_expression_253
        if minami.flags.submissive_interact:
            if randint(0, 1) == 0:
                minami.say "Big bro, you wanna break a taboo and make me cum all at once?"
            else:
                minami.say "[hero.name], I might be sick..."
                minami.say "I'm all wet and sweaty..."
                minami.say "You have a PhD or something, don't you?"
                minami.say "I'll probably need a Physical Desweatization..."
        hide minami
    return

label minami_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello sis."
        elif game.hour < 12:
            mike.say "Good morning sis."
        elif game.hour < 19:
            mike.say "Good afternoon sis."
        else:
            mike.say "Good evening sis."
    return

label minami_kiss:
    scene expression f"bg {game.room}"
    if minami.love < 25 and not minami.is_girlfriend and not game.active_date.score >= 75:
        show minami
        "I've been fighting this for so long now, that just looking at Minami for more than a moment makes my heart ache."
        "In the past, it's been enough to remind myself that she's my sister."
        "But now all that I can think of is the fact that she's adopted, that we're not blood relatives."
        "And my desire for her is just too much to keep me from acting any longer..."
        "I find myself leaning in to kiss Minami on the lips."
        "But as soon as she sees what I'm doing, she pulls back and pushes me away."
        "And so she leaves me feeling both ashamed and rejected at the same time."
        $ minami.love -= 5
        $ minami.sub -= 5
        $ minami.siscon -= 10
        hide minami
    elif not minami.flags.kiss:
        hide minami
        $ minami.love += 5
        if minami.lesbian > MAX_LES_GUY_SEX:
            $ minami.lesbian -= 1
        show minami kiss
        "Every rule and law that I can think of tells me that I should only think of Minami as my sister."
        "But my heart is telling me the exact opposite, and to totally ignore then for the sake of its desires."
        "And if I go on like this for too much longer, I think I'm going to go insane!"
        "So that's how I find myself leaning in to kiss Minami on the lips."
        "I close my eyes, fearing the worst reaction possible from her."
        "But much to my surprise, I feel the soft sensation of her lips touching mine."
        "And that's the point of no return, as we kiss each other with ever-increasing passion."
        hide minami kiss
        $ minami.flags.kiss += 1
        $ minami.siscon += 1
    else:
        hide minami
        $ minami.love += 2
        show minami kiss
        "Once we're past the taboo of exchanging kisses, there's no longer anything that can stop us."
        "Minami and I steal every moment that we can to repeat the action, lingering long and lazily."
        "In the back of my mind, I can still hear all of the same lines, repeating over and over again."
        "But now they seem to have lost all of their power to make me feel even an ounce of guilt."
        "As soon as Minami's lips touch my own, it feels like the most natural, wonderful thing possible."
        hide minami kiss
        $ minami.flags.kiss += 1
        $ minami.siscon += 1
    return

label minami_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show minami naked
        if minami.flags.mikeNickname:
            minami.say "[hero.name], can I... Can I please spend the night?"
        else:
            minami.say "Big bro, can I... Can I please spend the night?"
        menu:
            "No":
                mike.say "No, you shouldn't; I have to get up early tomorrow."
                "The sex was beyond incredible."
                "Frowning a little, Minami straightens and collects her clothes in silence."
                minami.say "That's OK, sleep well!"
                "She then grins at me, before leaving."
                $ minami.love -= 3
                call sleep from _call_sleep_44
            "Yes":
                mike.say "Of course you can."
                "I catch a brief moment of joy flash across her face, before she pulls me into a hug, nuzzling into me once again."
                minami.say "Thank you..."
                "I'm not sure why she seems so happy about this, but it looks like I picked the right answer."
                show cuddle minami
                if minami.flags.mikeNickname:
                    minami.say "Sleep well, [hero.name]."
                    mike.say "You too my cute little slave."
                else:
                    minami.say "Sleep well, Big bro."
                    mike.say "You too."
                "We both cuddle in silence, drifting off to sleep in each others arms."
                $ minami.love += 3
                call sleep ("minami") from _call_sleep_45
        $ game.room = "bedroom1"
    return

label minami_propose_male:
    show minami normal
    "I was worried that Minami might pick up on the fact that I'm a bag of nerves today."
    "But for once, her ability to become one hundred percent self-absorbed is actually helping matters."
    "It means that she doesn't notice as I perspire visibly and feel like I have a ten ton weight in my pocket."
    "Instead she just keeps prattling on about whatever silly nonsense is filling her head right now."
    "And she doesn't even notice that I'm only nodding and making a non-committal sound every now and then."
    minami.say "...anyway, they said it wasn't them."
    mike.say "Uh..."
    minami.say "They actually swore on their lives it wasn't them."
    mike.say "Uh-huh..."
    show minami annoyed
    minami.say "Can you believe that, big bro?!?"
    mike.say "Nah..."
    minami.say "But I know it was them, for sure."
    mike.say "Nah-huh..."
    minami.say "Because I have kind of a psychic sense for that kind of thing, yeah?"
    mike.say "Uh..."
    minami.say "It's like I just know when someone's got shit on their mind..."
    show minami normal
    "I've been stuck in this position so long that I'm actually starting to forget why."
    "Ignoring Minami as she prattles on is making me lose track of what was on my mind in the first place."
    "The ring - that's it!"
    "I have to ask her now, before she melts my brain with gossip!"
    mike.say "Ah, Minami..."
    "I drop down onto one knee as I pull the ring out of my pocket."
    mike.say "I was thinking, what with all the stuff that's happened to us..."
    mike.say "Despite all of that..."
    mike.say "Would you marry me?"
    "Something changes the moment the words are out of my mouth."
    "It takes me a few seconds to realise just what it is."
    "And then it dawns on me - Minami's actually stopped talking!"
    mike.say "Minami, are you okay?"
    minami.say "Guh..."
    mike.say "What's the matter?"
    minami.say "Guh-huh..."
    "It's suddenly like we've switched places with one another."
    "Now I'm the one talking and Minami's making vague, incomprehensible sounds."
    "But she seems to shake it off far more quickly than I was able to."
    "Sensing this, I ask the question of her a second time."
    mike.say "Minami, I'm asking you to marry me..."
    if minami.love < 195:
        show minami sad
        "I see a sadness swell in Minami's eyes."
        "And even before she speaks, I can guess what her answer will be."
        minami.say "Oh, big bro..."
        minami.say "Why'd you have to ask me that now, huh?"
        "I shake my head at this."
        mike.say "What do you mean, Minami?"
        mike.say "Surely there's no better time?"
        minami.say "No, big bro, no way."
        minami.say "Not after what Mom and Dad did to us."
        minami.say "It'd just feel like they got their way in the end."
        "I'm still shaking my head, trying to disagree."
        mike.say "N...not if we decide to do it ourselves."
        mike.say "That way we're kinda sticking two fingers up at them - right?"
        show minami normal
        "Minami smiles at this, but it's filled with pain."
        "And it cuts through me like a knife."
        minami.say "Sorry, big bro."
        minami.say "Maybe sometime soon that'll be true."
        minami.say "But not right now."
        "I nod sadly, stuffing the ring back into my pocket and getting to my feet."
        "Minami takes hold of my hand, squeezing it tightly."
        "Maybe she's right and we just need some time to heal."
        "It just feels weird to be the one running after her for a change!"
        $ minami.love -= 25
        $ minami.sub -= 25
    else:
        "I see a sparkle begin to build in Minami's eyes."
        show minami happy
        "She claps her hands together, smiling from ear to ear."
        "And then she actually jumps up and down on the spot!"
        minami.say "Oh, big bro..."
        minami.say "Are you actually serious?!?"
        "I look left and then right, not sure what to say."
        "All I can do is nod and answer honestly."
        mike.say "Of course I am, Minami."
        mike.say "Even after all that's happened."
        mike.say "I love you, and I want to marry you."
        mike.say "Well...if you want marry me too?"
        show fx exclamation
        minami.say "What - are you crazy?!?"
        minami.say "Sure I want to marry you, big bro!"
        minami.say "That's what I always wanted - more now than ever!"
        show minami kiss
        $ minami.flags.kiss += 1
        "Minami throws her arms around my neck and kisses me with a passion."
        "And I grab hold of her, returning the kiss with the same intensity."
        "I can feel all of the tension and anxiety just melting away."
        "Minami said yes, and nothing else matters."
        "But that's when the thought hits me."
        "She didn't actually say the exact word, did she?"
        "I break the kiss, panting to ask the question again."
        hide minami
        show minami happy
        mike.say "S...so...you will?"
        "Minami chuckles and shakes her head at me."
        minami.say "Yes, you moron - I'll marry you!"
        "I can't help beaming as I slide the ring onto her finger."
        "It's actually happening - Minami's going to be my wife!"
        $ minami.set_fiance()
    return

label unlock_minami_compliment:
    $ minami.flags.nosweettalk = False
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
