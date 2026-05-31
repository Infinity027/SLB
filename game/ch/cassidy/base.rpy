init python:
    Event(**{
    "name": "cassidy_give_phone_number",
    "label": "give_phone_number",
    "girl": "cassidy",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(cassidy,
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
    "name": "cassidy_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(12, 13),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(cassidy,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "cassidy",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_auto_greet",
    "label": "auto_greet",
    "girl": "cassidy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(cassidy,
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
    "name": "cassidy_auto_chat",
    "label": "auto_chat",
    "girl": "cassidy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(cassidy,
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
    "name": "cassidy_are_you_sick",
    "label": "are_you_sick",
    "girl": "cassidy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (cassidy, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_ask_out",
    "label": "ask_out",
    "girl": "cassidy",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(cassidy,
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
    "name": "cassidy_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "cassidy",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(cassidy,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label cassidy_bye(bye_outfit=None):
    call npc_bye_outfit (npc=cassidy, bye_outfit=bye_outfit) from _call_npc_bye_outfit_7
    $ (day, h, activity, bye_outfit) = _return
    if not activity == cassidy.activity:
        if day != game.week_day:
            $ cassidy.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ cassidy.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"cassidy {bye_outfit}")
        if activity["activity"] == "sleep":
            cassidy.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            cassidy.say "I have to go to the bathroom, don't you dare peek!"
        elif activity["activity"] in ["meal"]:
            cassidy.say "I am so hungry..."
        elif activity["activity"] in ["watch"]:
            cassidy.say "I think I'm going to go catch a movie."
        elif activity["activity"] in ["drink"]:
            cassidy.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            cassidy.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            cassidy.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            cassidy.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            cassidy.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            cassidy.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            cassidy.say "I'll go get dressed."
        hide cassidy
    return

label cassidy_cheated(action, cheat_npc=None):
    show cassidy
    if cheat_npc and Harem.together(cheat_npc, cassidy):
        show cassidy wink
        cassidy.say "Aren't you forgetting something?"
        show cassidy
        "And without warning Cassidy kisses me."
        $ cassidy.love += 1
        $ cassidy.flags.kiss += 1
    elif cassidy.status == 'pet':
        if cassidy.love > 120 and cassidy.sub < 75:
            "Cassidy stares at me hard, but I can't tell if she's angry or intrigued. Maybe both."
            $ cassidy.sub += 1
            $ cassidy.love -= 1
    else:
        show cassidy angry

        "Cassidy gives me an angry look and mouths the words \"You're going to regret that\" at me."
        $ cassidy.love -= 5
    hide cassidy
    return

label cassidy_greet:
    if renpy.has_label(f"cassidy_greet_dialogues_{hero.gender}") and not cassidy.flags.greeted:
        scene expression f"bg {game.room}"
        $ cassidy.flags.greeted = TemporaryFlag(True, 1)
        show cassidy
        if cassidy.status == 'mistress':
            cassidy.say "Hello, [hero.name]."
            call expression f"cassidy_greet_dialogues_3_{hero.gender}" from _call_expression_221
        elif cassidy.status == 'pet':
            if cassidy.love < 120:
                cassidy.say "Hi, [hero.name]."
                call expression f"cassidy_greet_dialogues_1_{hero.gender}" from _call_expression_219
            else:
                if cassidy.flags.mikeNickname in nickname_master:
                    cassidy.say "Hello, my [hero.name]!"
                else:
                    cassidy.say "Hello, [hero.name]!"
                call expression f"cassidy_greet_dialogues_2_{hero.gender}" from _call_expression_220
            if cassidy.flags.submissive_interact:
                if randint(0, 1) == 0:
                    cassidy.say "Please, [hero.name] - would your French kiss ALL my lips?"
                else:
                    cassidy.say "Kiss my lips. I mean, all my lips!"
        else:
            if randint(1, 3) == 1:
                cassidy.say "Hi, I guess, [hero.name]."
            else:
                cassidy.say "Oh, it's you, [hero.name]."
            call expression f"cassidy_greet_dialogues_4_{hero.gender}" from _call_expression_222
            if cassidy.flags.submissive_interact:
                if randint(0, 1) == 0:
                    cassidy.say "Please, [hero.name] - would your French kiss ALL my lips?"
                else:
                    cassidy.say "Kiss my lips. I mean, all my lips!"
        hide cassidy
    return

label cassidy_greet_dialogues_1_male:
    mike.say "Hello, my pet!"
    return

label cassidy_greet_dialogues_2_male:
    mike.say "My sweet pet!"
    return

label cassidy_greet_dialogues_3_male:
    mike.say "Hello, Mistress."
    return

label cassidy_greet_dialogues_4_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Cassidy."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Cassidy."
        elif game.hour < 12:
            mike.say "Good morning Cassidy."
        elif game.hour < 19:
            mike.say "Good afternoon Cassidy."
        else:
            mike.say "Good evening Cassidy."
    return

label cassidy_kiss:
    scene expression f"bg {game.room}"

    if cassidy.flags.nokiss:
        if cassidy.status == 'mistress':
            show cassidy angry
            "Cassidy lightly slaps me across the cheek and pushes me away."
            $ cassidy.sub -= 1
            cassidy.say "Did I say you could try to kiss me, [hero.name]?"
            mike.say "Sorry, Mistress."
        else:
            show cassidy
            "Cassidy quickly takes a step back and turns away."
            cassidy.say "Who do you think you are?!"
            $ cassidy.love -= 1
        hide cassidy
        return
    if cassidy.status == 'mistress':
        if not cassidy.flags.kiss:
            $ cassidy.love += 5
            "I step up to Cassidy, slightly afraid she's going to push me away."
            "But she doesn't; instead she stands there passively while I embrace her."
            "When I try to kiss her, though, she pulls her head back, away from me. She puts one finger against my lips."
            call cassidy_kiss_dom from _cassidy_kiss_dom
        else:
            $ cassidy.love += 2
            "When I try to kiss her, she pulls her head back, away from me. She puts one finger against my lips."
            call cassidy_kiss_dom from _cassidy_kiss_dom_2
    else:
        hide cassidy
        if cassidy.lesbian > MAX_LES_GUY_SEX:
            $ cassidy.lesbian -= 1
        show cassidy kiss
        if cassidy.love > 120:
            "I step up to Cassidy and pull her into my arms."
            "She doesn't resist, allowing me to pull her against the length of my body."
            "Her lips open when mine touch hers, allowing my tongue into her mouth to tease and explore."

            "After a moment the kiss ends, and I step back. She gives me a soft, happy smile."
        else:
            "I step up to Cassidy and pull her into my arms."
            "She seems stiff and mildly resistant, so I am firm with her, and she complies."
            "Her lips open when mine touch hers, allowing my tongue into her mouth to tease and explore."
            "After a moment the kiss ends, and I step back. She looks at me with some amount of discomfort."
            "She clearly enjoyed it, but I think she needs more encouragement."
        hide cassidy kiss
        $ cassidy.love += 2
    call check_cheated ("kissing") from _cassidy_kiss_sub
    $ cassidy.flags.kiss += 1
    return

label cassidy_kiss_dom:
    if cassidy.sub > -75:
        cassidy.say "Have you been a good boy lately?"
        mike.say "I suppose...I could be better, Mistress?"
        cassidy.say "That's right. Are you going to be better?"
        mike.say "Yes, Mistress. I'll be a better boy."
        $ cassidy.sub -= 1
    else:
        cassidy.say "Who's been a good boy. You have! You've been a very good boy."
        mike.say "Yes, Mistress."
    hide cassidy
    show cassidy kiss
    $ cassidy.flags.kiss += 1
    "Then she relaxes. Her arms wrap around my neck, pulling me close."
    "Our lips touch, and we drink hungrily from each other. Her grip around my neck is so tight it almost hurts, and I return the gesture."
    "My arms, wrapped around her, pull her as tightly to me as I can. I feel her ample breasts smashed against my chest."
    "Her hips press against mine."
    hide cassidy kiss
    "And then it's over. She steps back and gives me a wry smile, followed by a wink."
    return

label cassidy_ask_fuck_date_male:
    if game.active_date.score >= (100 - cassidy.flags.drinks*5):
        if cassidy.status == 'mistress':
            cassidy.say "This is the part where you take me home and please me all night long, [hero.name]."
            mike.say "I don't know..."
            cassidy.say "Did you have fun?"
            mike.say "Yeah, I guess I did."
            "She takes a hold of my hand and gives it a squeeze."
            if cassidy.love > 120:
                cassidy.say "Don't worry, Sweetie, I'll make sure you have fun too. This won't be {b}just{/b} about me. Only mostly."
                "I look at her and she smiles at me with genuine affection."
                mike.say "Okay."
            else:
                cassidy.say "I promise it'll feel good. I'm pretty good at this, you know, and no one has ever complained when I was done with them."
                "I have to laugh at that."
                mike.say "Fine, then. It might be the one perk of this arrangement is getting to fuck you."
        else:
            if hero.stamina:
                mike.say "Come home with me, my pet."
                if cassidy.love < 120:
                    cassidy.say "Do I have to?"
                    menu:
                        "You do not have a choice":
                            mike.say "You do not have a choice. You are coming home with me."
                            $ cassidy.love -= 5
                            $ cassidy.sub -= 1
                            "Cassidy looks down at the ground and nods."
                            cassidy.say "Yes, Master."
                        "Only if you want to":
                            mike.say "Look, I like what we have, but if you really don't want to, I guess you can go home."
                            $ cassidy.love += 5
                            $ cassidy.sub += 1
                            cassidy.say "Thank you, Master."
                            mike.say "But if you do, I think you'll have fun."
                            cassidy.say "I guess I had a good time tonight. Okay, I'll go."
                else:
                    cassidy.say "Take me home, Master, and ravish me!"
                    mike.say "Gladly!"
            else:
                return False
        return "hero"
    else:
        if cassidy.status == 'mistress':
            cassidy.say "You know, [hero.name], I was looking forward to a good shag tonight, but you were really kind of dull, so I think I'm going to go home and masturbate, instead."
            cassidy.say "Do better, next time. Don't make me punish you."
        else:
            mike.say "Come home with me, my pet."
            cassidy.say "That date was not great. Do I really have to?"
            menu:
                "You do not have a choice":
                    mike.say "You do not have a choice. You are coming home with me."
                    $ cassidy.love -= 20
                    $ cassidy.sub -= 5
                    "Cassidy looks down at the ground and nods."
                    cassidy.say "Yes, Master, if I must."
                    return "hero"
                "Only if you want to":
                    mike.say "Look, I like what we have, but if you really don't want to, I guess you can go home."
                    $ cassidy.love += 5
                    $ cassidy.sub += 1
                    cassidy.say "Thank you, Master."
                    mike.say "But if you do, I think you'll have fun."
                    cassidy.say "I...please, can I go home? I don't feel good. I promise I'll be good next time."
                    mike.say "Okay, Cassidy. This time."
                    cassidy.say "Thank you, Master. I won't forget it!"
        return False

label cassidy_walk_outside:
    scene bg livingroom
    mike.say "Cassidy!"
    mike.say "Here, girl!"
    mike.say "Time for a walk!"
    "Almost as soon as the words are out of my mouth, I hear Cassidy getting up in response."
    "But that doesn't mean I expect her to appear in the seconds that follow, oh no."
    "And that's because I know that she's going to be getting herself ready."
    "And in a very specific way too!"
    "If I'm right, Cassidy should be ready any moment now..."
    cassidy.say "Here I am, [hero.name]!"
    show cassidy naked happy
    cassidy.say "I'm ready - let's go!"
    "It comes as no surprise to me when Cassidy walks in on her hands and knees."
    "And I'm not shocked to see that she's completely naked either."
    "She took just the right amount of time to tear off her clothes."
    "And now all that she has on is the dog-collar around her neck!"
    "I give her a smile and a nod as I reach for the leash that goes with it."
    "Then I clip it in place and give her a gentle tug."
    mike.say "Good girl, Cassidy!"
    mike.say "Come on then..."
    "If she had a tail, Cassidy would be wagging it like crazy now."
    "Instead she beams with pride as I open the front door and lead her outside."
    "It's only a short walk to the park from my place."
    "And the neighbourhood is always dead quiet at this time of night."
    "Plus I know a route that keeps up away from most of the street lights too."
    "If anyone sees me walking Cassidy naked in the middle of the night, I'm not worried."
    "At the best they're going to mistake me for somebody walking a large dog."
    "At the worst they're going to see what I'm actually doing."
    "And then they'll be too freaked to do anything about it."
    "In fact, I'm so sure there's no chance of us being caught, I don't even keep a look-out."
    scene petplay
    show petplay walk cassidy leash
    "Instead I spend most of the walk to the park admiring the sight of Cassidy at my heel."
    "I never thought that a spoilt little princess like her would take to this kind of thing."
    "But she seems to love being made to behave like a dog."
    "And it brings out her personality too."
    "I mean, she doesn't just do all of the stereotypical dog things."
    "Oh no, Cassidy also mixes in a good deal of snootiness too."
    "She behaves like one of those pampered little pooches you see in posh parts of town."
    "Cassidy struts around on all fours almost with her nose in the air."
    "It's like, sure, she sees herself as a dog."
    "But one of the most exclusive and expensive!"
    "I know that Cassidy knows I'm watching her this whole time."
    "Because she starts to almost bounce along at my heel."
    "Every step we take I can see her ass moving from side to side."
    "And her breasts are swaying under her at the same time too!"
    "It's all I can do to keep walking in a straight line towards the park."
    "Somebody walking a real dog would never get distracted like this!"
    "Or at least I hope that they wouldn't..."
    "Once we finally reach the park, I'm relieved to find the place is deserted."
    "So Cassidy and I have the entire place to ourselves."
    show petplay stand cassidy leash
    "I walk onto the grass and then take her off the lead."
    "And Cassidy keeps up the act, running here and there."
    "Hell, she even spends some time showing off by rolling on her back."
    "And she won't stop until I've given her a good belly-rub."
    "I pull out the tennis ball that I have in my pocket."
    "But as soon as I show it to her, Cassidy makes a huffing sound."
    "Then she literally turns her nose up at the thing!"
    "I guess Cassidy thinks that she's too good to play fetch."
    "She struts around for a little while longer on the grass."
    "But soon enough I see an expression of urgency appear on her face."
    "Then Cassidy hurries over to me, eyes wide."
    "She sits up on her haunches, pawing at my leg."
    show petplay stand cassidy leash cassidycloseeyes
    cassidy.say "We have to go back to your place - NOW!"
    cassidy.say "Please, [hero.name], we've got to hurry!"
    mike.say "Whoa, whoa, whoa..."
    mike.say "Wait a minute, Cassidy."
    mike.say "The idea here is that you're the dog and I'm the owner."
    mike.say "So I get to say when and where we go, okay?"
    cassidy.say "But, [hero.name]..."
    cassidy.say "You don't understand - I need to pee!"
    "The admission does make me open my eyes a little wider."
    "But then I glance around the deserted park and shrug."
    mike.say "Just take a piss here, Cassidy."
    mike.say "That's what a dog would do, isn't it?"
    mike.say "I'll even look the other way if you like!"
    "Cassidy looks at me with an expression of horror on her face."
    "It's as if she can tolerate being led around naked on a dog-leash."
    "But somehow pissing in a public place is just too much for her to take."
    cassidy.say "NO!"
    cassidy.say "You have to take me home!"
    cassidy.say "You can't make me go to the bathroom here!"
    menu:
        "Make Cassidy urinate in the park":
            "I shake my head at Cassidy's pleas."
            "I might let her off when it comes to playing fetch."
            "But this is kind of fundamental to being a dog."
            mike.say "Two choices, Cassidy."
            mike.say "Number one, I walk you over to those tree and you go there."
            mike.say "Or number two, we stay right here until nature takes its course."
            mike.say "So which is it going to be?"
            "Cassidy looks over to the trees and then back at me."
            "I can see the pleading look in her eyes."
            "And that must have worked every time when she was charming daddy."
            "But it's not going to work with me."
            "I just cross my arms over my chest and gaze down at her."
            "And in the end I'm proven right, as Cassidy breaks first."
            cassidy.say "Okay, okay..."
            cassidy.say "Take me over to the trees."
            cassidy.say "But you'd better do it fast!"
            "I attach the leash to Cassidy's collar and start to walk towards the trees."
            "Sure, I don't dawdle on the way over there."
            "But it's not like I sprint the distance either."
            "By the time we make it, Cassidy's twitching and wriggling."
            "She looks up at me and I give her a quick nod."
            "Then she crawls over to the nearest tree and points her ass towards it."
            show petplay stand cassidy leash cassidypee
            cassidy.say "Aaah..."
            cassidy.say "That is SO much better!"
            cassidy.say "W...wait a minute - you said you wouldn't watch me!"
            "I can't help chuckling as I watch Cassidy's cheeks turn red."
            "The humiliation of the whole thing almost makes her shake with anger."
            "And it's a perfect reward for me after she's been so petulant too."
            mike.say "I said I'd look the other way if you liked, Cassidy."
            mike.say "You never took me up on that offer before you started pissing."
            mike.say "So I took it that you were okay with me watching you."
            show petplay walk cassidy leash
            "Cassidy mutters and curses under her breath as I walk her out of the park."
            "And she makes the journey back to my place acting more haughty than ever."
            "Not that I mind too much."
            "I kind of like the way she acts like a highly-strung, pedigree bitch!"
            $ cassidy.sub += 2
        "Take Cassidy home":
            "I look around, honestly considering making Cassidy take a leak on the spot."
            "But then I sigh and shake my head, admitting defeat."
            "I already put a collar on the girl and walked her around in the nude."
            "What more is making her piss in the park really going to mean to me?"
            mike.say "Okay, Cassidy..."
            mike.say "Let's head home."
            cassidy.say "Oh, thank you!"
            cassidy.say "Thank you for not making me pee out here!"
            cassidy.say "I'll be a good girl from now on, I promise!"
            "I have no idea just what Cassidy being a good girl would entail."
            "But I'm sure that I can think of something when the time comes."
            "I fasten the leash to her collar again and we start walking back."
            show petplay walk cassidy leash
            "This time I set a faster pace, and Cassidy's forced to keep up."
            "Now and again she looks like she's going to complain or ask me to slow down."
            "But then something seems to stop her and she just keeps on going."
            "I don't know if it's her promise from a few moments ago."
            "Or else the sudden reminder of just how full her bladder is right now."
            "Either way we arrive back at my place in record time."
            "I barely have time to open the front door before Cassidy shoots inside."
            "I let go of the leash, allowing her to dart into the bathroom."
            "And I can't help smiling at the sigh of relief I hear a moment later."
            "Looks like general obedience and toilet-training are something we need to work on."
            "But that can wait for the next time I walk Cassidy."
            "And in the meantime, I can dream up some incentives for her to learn."
            "Maybe some punishments too..."
            $ cassidy.love += 2
    return

label cassidy_propose_male:
    show cassidy
    "I need to get this right like I've never needed to get anything right before in my entire life."
    "In fact, scratch that - I need for this to be absolutely and utterly perfect!"
    "I can't afford for a single thing to go wrong, not when I'm dealing with Cassidy."
    "She's getting to be like a strange kind of addiction for me."
    "The more time I spend with her, the more time I want to spend with her."
    "And when I'm not with her, she's all I can think about until we're together again."
    "That's why I've decided to do everything I can to be around her twenty-four seven."
    "I have a ring that cost me more money than I care to admit stashed in my pocket."
    "I've rehearsed the whole thing in my head until it's stuck in there."
    "Now all I need to do is choose the right moment to pop the question."
    "I figure that if I do that, then Cassidy's almost certain to say yes."
    "In fact, I don't even want to think about the alternative."
    "I don't want to contemplate what happens if Cassidy turns me down..."
    "No, that's just me being negative for no good reason."
    "What I need right now is a positive mental attitude."
    "Well, that and the courage to actually do this thing!"
    cassidy.say "So then I said to her..."
    cassidy.say "I said..."
    show cassidy annoyed
    cassidy.say "[hero.name]!"
    cassidy.say "Are you even listening to me right now?!?"
    "Suddenly the sound of Cassidy's voice snaps me back to reality."
    "I feel like I'm being put on the spot and it makes me panic."
    "For some reason all of my instincts get mixed up."
    "And at what's probably the worst possible moment, I just launch into it."
    "I launch into the speech I had planned for the best possible moment."
    "Before I know it, I'm down on one knee, pulling out the ring."
    mike.say "Cassidy..."
    mike.say "Will you..."
    mike.say "Will you marry me?"
    show cassidy normal
    "If I thought I looked confused, I've got nothing on Cassidy."
    "The whole thing seems to catch her completely off guard."
    "It's like this was the last thing in the world she was expecting to happen."
    "But the problem is that I don't know if that's good or bad!"
    cassidy.say "I..."
    show cassidy annoyed
    cassidy.say "I don't know!"
    "I glance around, my head turning rapidly."
    "All around us people are watching with interest."
    "Some are expecting a nice little romantic scene to play out in front of them."
    "But I'm pretty sure that some are relishing the awkward position I'm in."
    "And they're looking forward to seeing my hopes get squashed like a bug!"
    mike.say "Well..."
    mike.say "Do you think you could, I don't know..."
    mike.say "Maybe put a little thought into it and give me an answer anytime soon?"
    if cassidy.love < 195:
        "I watch as my words sink in, and Cassidy's expression begins to change."
        "And it's then that I begin to realise I've made a terrible mistake."
        "Because the look on her face is getting darker by the moment."
        "Before I can react, Cassidy slaps at the hand holding the ring."
        "It's all I can do to pull it out of the way before she makes me drop it!"
        mike.say "Hey!"
        mike.say "What the hell, Cassidy?!?"
        "By now Cassidy has both of her own hands clenched into fists."
        "And they're planted firmly on her thighs as she glares down at me."
        show cassidy angry
        cassidy.say "How dare you spring something like this on me?"
        cassidy.say "Just come right out and propose to me like this?"
        cassidy.say "If you wanted to surprise me, you should have told me ahead of time!"
        "I hear the words that Cassidy is saying."
        "And on one level they seem to make perfect sense."
        "But then I find myself blinking in confusion."
        "Did she..."
        "Did she actually just say I need to tell her before I surprise her?"
        mike.say "But, Cassidy..."
        mike.say "If I already told you..."
        mike.say "Then it wouldn't be a surprise, would it?"
        "Cassidy rolls her eyes and let's out an irritated grunt."
        "She looks like she's trying to explain something simple to a moron."
        cassidy.say "Urgh..."
        cassidy.say "Give me strength!"
        cassidy.say "You're not supposed to just up and tell me you're going to propose."
        cassidy.say "But you have to drop subtle hints that let me know it's on the cards!"
        cassidy.say "That way I can be ready when it actually happens!"
        mike.say "You do?"
        mike.say "Wow..."
        mike.say "I had no idea!"
        cassidy.say "Well that much is obvious!"
        "I look down at the ring and then back up at Cassidy."
        mike.say "You know, Cassidy..."
        mike.say "You never actually answered the question..."
        cassidy.say "NO!" with vpunch
        cassidy.say "It's a no, [hero.name]."
        cassidy.say "And it'll stay that way until you get a clue!"
        hide cassidy
        "With that, Cassidy storms off in a huff."
        "Which leaves me to get slowly to my feet."
        "As I put the ring away, I can feel everyone staring at me."
        "Well, so much for making sure everything's perfect!"
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    else:
        "I watch as my words sink in, and Cassidy's expression begins to change."
        "And that's when I feel my heart starting to break for her."
        show cassidy happy
        "The look on her face goes from one of confusion to amazement."
        "And it actually looks like she's fighting back tears too!"
        mike.say "Cassidy?"
        mike.say "Are you okay?"
        "Cassidy nods and waves a hand as she tries to speak."
        cassidy.say "Y...yes..."
        cassidy.say "Yes to both questions!"
        "I look at her in confusion for a moment."
        "Then her meaning becomes clear to me."
        "I nod eagerly as I lean forwards."
        "Cassidy thrusts her hand out towards me."
        "And I push the ring onto her finger."
        "She stares at it in amazement, literally lost for words."
        "But that gives me the chance to get to my feet and collect my wits."
        mike.say "You had me scared for a moment back there, Cassidy."
        mike.say "I thought that you were going to say no."
        mike.say "Or even worse, blow up on me!"
        "Cassidy looks up from staring at the ring."
        "And then she shakes her head."
        cassidy.say "What?"
        cassidy.say "You actually think I'd do something like that?!?"
        cassidy.say "No way, [hero.name]!"
        cassidy.say "You just took me by surprise, that's all."
        "I nod and smile, not totally convinced she's telling the whole truth."
        "But there's no way I'm going to poke at an issue like that."
        "Not when Cassidy actually just agreed to marry me!"
        mike.say "Of course not, Cassidy."
        mike.say "I think the nerves just got to me, you know?"
        mike.say "Made me think up crazy things like that."
        "Cassidy nods happily, accepting my explanation."
        "Then she goes back to staring at the ring."
        show cassidy normal
        cassidy.say "So, when do I get the real ring?"
        mike.say "Erm..."
        mike.say "What do you mean, Cassidy?"
        cassidy.say "Well, this isn't the actual ring, is it?"
        cassidy.say "You just got it as a stop-gap, yeah?"
        cassidy.say "Until you get something more fancy?"
        "I stare at Cassidy in utter amazement."
        "My mouth opens and closes, making me look like a stunned fish."
        show cassidy happy
        cassidy.say "Kidding!"
        cassidy.say "I'm only kidding, [hero.name]!"
        cassidy.say "I love this one - it's perfect!"
        "I nod and smile, trying to laugh at Cassidy's joke."
        "But I can still feel my heart hammering in my chest..."
        $ cassidy.set_fiance()
    hide cassidy
    return

label cassidy_ask_date_male:
    if Harem.find(cassidy):
        menu:
            "Ask Cassidy on a date":
                call cassidy_ask_date_alone_male from _call_cassidy_ask_date_alone_male
            "Ask Cassidy, Audrey and Palla on a date" if "bitchy_harem_nightclub_encounter" in DONE:
                call cassidy_ask_date_audrey_cassidy_palla from _call_cassidy_ask_date_audrey_cassidy_palla
    else:
        call cassidy_ask_date_alone_male from _call_cassidy_ask_date_alone_male_1
    return _return

label cassidy_ask_date_audrey_cassidy_palla:
    mike.say "Do you want to get together with Audrey and Palla and have some fun?"
    if cassidy.love >= 160 and cassidy.lesbian >= 9:
        cassidy.say "Fuck yeah!"
        call select_date_time from _call_select_date_time_4
        $ (day, hour, say_string) = _return
        if day == "cancel":
            return
        $ mike.say(say_string)
        if day == "now":
            call bitchy_harem_foursome_appointment_intro from _call_bitchy_harem_foursome_appointment_intro_1
        else:
            $ hero.calendar.add(day, HaremAppointment(hour, "bitchy", ["audrey", "cassidy", "palla"], "bitchy_harem_foursome_appointment_intro"))
        return
    else:
        cassidy.say "I don't feel like it, sorry."
        return False

label cassidy_ask_date_alone_male:
    mike.say "Cassidy, would you like to go on a date with me?"
    if cassidy.love < 50 or cassidy.flags.nodate:
        cassidy.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        cassidy.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
