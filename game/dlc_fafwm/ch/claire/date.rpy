label claire_date_eat_a_burger:
    "I'm feeling like I could eat a horse when the burgers I ordered arrive."
    "And as soon as the waiter's disappeared, I grab hold of mine and prepare to take a huge bite out of it."
    "The only problem is that, as I do so, I notice Claire poking at her own burger with a knife and fork."
    "As soon as she sees me watching her, she forces a smile onto her face and pops a small morsel into her mouth."
    "But there's no hiding the fact that she's not keen on the burger, and that knowledge kind of ruins my appetite in turn."
    return

label claire_date_buy_drink:
    "I drain the last dregs from my glass and then make to stand up."
    mike.say "Looks like it's time for another drink!"
    mike.say "Are you wanting one too, Claire?"
    if claire.is_visibly_pregnant:
        "Claire shoots me a look of sheer amazement and shakes her head."
        "And that's when I notice her hands protectively clutching her swollen belly."
        claire.say "How many of those things have you had?"
        claire.say "Did they make you forget that I'm pregnant?!?"
        mike.say "Ah, yeah...sorry about that!"
        $ hero.cancel_activity()
    else:
        "Claire looks down at her own glass and then back up at me."
        "And I have to say that I really like the cheeky glint in her eye as she does so."
        claire.say "Are you trying to get me drunk, [hero.name]?"
        claire.say "Because if you are, it's totally working!"
        claire.say "Hurry up and bring me another one of these before I sober up."
        $ game.active_date.score += 5
        $ claire.set_flag("drinks", 1, "day", mod="+")
    return

label claire_date_play_darts:
    "Claire puts on a pained smile as I hand her some darts and lead the way over to the board."
    "But as soon as we start playing, it's pretty obvious that she's not comfortable with this game."
    "And her aim is one of the worst I've ever seen too, as she misses the board with most of her darts."
    "Every one of them shoots off in a random direction, causing shouts and curses from other patrons."
    "All of which makes me keen to keep the game short and bring it to a merciful end as soon as possible."
    return

label claire_date_pub_play_pool:
    "I should have known something was amiss from the way that Claire takes the pool-cue from me."
    "She weighs it and seems to be sizing it up as we approach the table and I let her break."
    "Which she does with alarming skill, sinking balls right from the first shot of the game."
    "After that I hardly manage to get a look in at the table as she cleans up in front of me."
    "And once she's trounced me, Claire doesn't even apologise - the woman's a regular hustler!"
    return

label claire_date_buy_a_round:
    "I'm painfully aware of the fact that I haven't bought a round yet."
    "And so when I finish off my drink and slam down the glass, it's more than a little performative."
    "As is the way that I point to the empty glass and then at the bar."
    mike.say "Aaah!"
    mike.say "Time for another round."
    mike.say "Can I get one for you too, Claire?"
    if claire.is_visibly_pregnant:
        "Claire shoots me a look of sheer amazement and shakes her head."
        "And that's when I notice her hands protectively clutching her swollen belly."
        claire.say "How many of those things have you had?"
        claire.say "Did they make you forget that I'm pregnant?!?"
        mike.say "Ah, yeah...sorry about that!"
        $ hero.cancel_activity()
    else:
        "Claire looks down at her own glass and then back up at me."
        "And I have to say that I really like the cheeky glint in her eye as she does so."
        claire.say "Are you trying to get me drunk, [hero.name]?"
        claire.say "Because if you are, it's totally working!"
        claire.say "Hurry up and bring me another one of these before I sober up."
        $ game.active_date.score += 5
        $ claire.set_flag("drinks", 1, "day", mod="+")
    return

label claire_dance_with:
    "Claire resists a little when I try to pull her towards the dance-floor."
    "But in the end she lets me lead her there and into the throng of moving bodies."
    "And that's when I realise that she's been deliberately misleading me."
    "Because now she's the one taking the lead, and getting as close to me as she possibly can."
    "Pressing her body against mine and leaving me almost breathless as we dance together."
    return

label claire_date_play_arcade_intro:
    mike.say "Hey, look - they have one of those old-school arcade games."
    mike.say "I love those things so much, Claire!"
    mike.say "Let's go play it, yeah?"
    "Claire frowns a little as she follows my gaze over to the vintage arcade-cabinet."
    "And I can sense that she's not nearly as keen on the idea as I am too."
    claire.say "Okay, [hero.name]..."
    claire.say "I suppose we could have one game on it."
    claire.say "But you have to go easy on me, okay?"
    claire.say "Those things aren't exactly my cup of tea!"
    "I'm only half listening to Claire as I pump coins into the slot."
    "And once I'm done, I stand up and nod my head eagerly."
    mike.say "Yeah...sure...whatever you say."
    mike.say "This is going to be so cool!"
    return

label claire_date_play_arcade_win:
    "I'm so engrossed in playing the game that I totally forget that Claire's not good at this kind of thing."
    "And instead I focus all of my attention on winning at any cost."
    "So it doesn't take long for me to pull way ahead of Claire."
    "And by the end of the game, there's no way for her to catch me up."
    mike.say "YEAH!"
    mike.say "I win!"
    mike.say "I am the greatest!"
    claire.say "Erm..."
    claire.say "Well done, I guess."
    "Suddenly embarrassed by my boorish performance, I feel myself cringing."
    "But luckily for me, Claire seems more keen on moving on than telling me off."
    return

label claire_date_play_arcade_lose:
    "I'm so engrossed in playing the game that I totally forget that Claire's not good at this kind of thing."
    "And instead I focus all of my attention on winning at any cost."
    "Which is why it comes as a genuine surprise for me to see that she's beating me hands down!"
    "No matter what I do, Claire pulls way ahead, leaving me in her wake and unable to catch up."
    "Once the game is over, I find myself staring at her in sheer amazement."
    mike.say "What was that?"
    mike.say "What in the hell happened?"
    mike.say "I thought you didn't do video-games?!?"
    claire.say "I said they weren't my cup of tea, [hero.name]."
    claire.say "Not that I was bad at them!"
    return

label claire_dick_reactions:
    if not claire.flags.seendick:
        $ claire.flags.seendick = 1
        "I'm feeling the usual nerves from this being the first time a girl's seen me naked."
        "But it's not helping that Claire's eyes are totally glued on my junk right now."
        mike.say "Ah, Claire..."
        mike.say "Is there a problem down there?"
        mike.say "Because you seem to be staring at it a hell of a lot!"
        show claire normal
        if hero.has_skill("smalldick"):
            "Claire looks up, as if snapped back to reality by my words."
            show dick reactions claire smile
            claire.say "Oh, well..."
            claire.say "I guess that I was expecting it to be a little bigger."
            claire.say "But that's not a deal-breaker, not by any means."
            claire.say "I always say that it's what you do with one that really counts."
        elif hero.has_skill("hung"):
            "Claire looks up, as if snapped back to reality by my words."
            show dick reactions claire smile
            claire.say "Oh, well..."
            claire.say "It's just that it's so...so big!"
            claire.say "Not that I mean it's too big, you understand?"
            claire.say "It's just that I've never had one that size before."
            claire.say "And I'm looking forward to finding out how it feels!"
        hide dick reactions
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
