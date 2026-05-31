label sasha_ask_phone_female:
    if game.week_day % 2 == 0:
        bree.say "Sasha, can I get your number?"
        bree.say "I just realised I don't have it!"
    else:
        bree.say "Sasha..."
        bree.say "I just realised something weird."
        bree.say "I don't actually have your number!"
    if hero.charm >= 20 - sasha.love:
        show sasha happy
        $ hero.smartphone_contacts.append("sasha")
        if game.week_day % 2 == 0:
            sasha.say "Sure thing, [hero.name]."
            sasha.say "You can even send me nudes if you really want..."
        else:
            sasha.say "Really, [hero.name]?"
            sasha.say "I thought I gave you that already?"
            "Sasha shakes her head as she pulls out her phone to give me her number."
    else:
        show sasha annoyed
        sasha.say "You don't need my number, [hero.name]."
        sasha.say "Just leave me a note on the noticeboard in the hallway!"
        $ sasha.love -= 1
        $ sasha.sub -= 1
    return

label sasha_ask_birthday_female:
    if game.week_day % 2 == 0:
        bree.say "Sasha..."
        bree.say "When's your birthday?"
    else:
        bree.say "Hey, Sasha..."
        bree.say "Remind me - when is your birthday?"
    if hero.charm >= 40 - sasha.love:
        show sasha happy
        $ sasha.flags.birthdayknown = True
        if game.week_day % 2 == 0:
            sasha.say "Spring 21, [hero.name]."
            sasha.say "So put the date in your diary."
            sasha.say "Because we're gonna party when it comes around!"
        else:
            sasha.say "Geez, [hero.name] - you've got memory like a sieve!"
            sasha.say "It's Spring 21."
            sasha.say "And try to remember it this time!"
    else:
        show sasha annoyed
        if game.week_day % 2 == 0:
            sasha.say "Hey, this colour isn't out of a bottle!"
            sasha.say "And anyway, you're even older than me, [hero.name]!"
        else:
            sasha.say "Yeah, [hero.name]..."
            sasha.say "Thing is, if I wanted you to know it, you would!"
            sasha.say "So ignorance is just gonna have to be bliss!"
        $ sasha.sub -= 1
        $ sasha.love -= 1
    return

label sasha_ice_cream_reaction_female:
    "I don't hold back for a moment, ordering my favourite cone from the ice-cream guys."
    "And I make sure to have them add all the trimmings too!"
    "But Sasha seems to hold back a little, like she's not sure."
    "As soon as I have my cone, I turn to face her."
    bree.say "What's up, Sasha?"
    bree.say "Don't you like ice-cream?"
    sasha.say "Yeah, [hero.name]...sure I do."
    sasha.say "I'm just not as up for it as you are!"
    "I frown and cock my head on one side."
    bree.say "Aw, come on, Sasha!"
    bree.say "Don't be such a Negative Nelly!"
    bree.say "Here, have a lick of mine..."
    "Sasha takes a step back as I shove the cone in her face."
    "But then she relents and sticks out her tongue to lick it."
    sasha.say "Mmm..."
    sasha.say "That's pretty good, [hero.name]!"
    sasha.say "I gotta get me one of those..."
    "I smile as Sasha hurries over to buy her own ice-cream."
    "And then we stroll off together, happily licking away."
    return

label sasha_offer_a_drink_female:
    bree.say "You want a drink, Sasha?"
    bree.say "I feel like grabbing a cold one!"
    bree.say "I can get you one too, if you like?"
    if (hero.charm >= 60 - sasha.love and sasha.flags.drinks < 2) or date_girl == sasha:
        show sasha happy
        sasha.say "Did you just read my mind, [hero.name]?"
        sasha.say "Thanks, I'd love a drink!"
        hide sasha
        show drink sasha
        if sasha.love <= 25:
            $ sasha.love += 1
        elif date_girl == sasha and game.active_date:
            $ game.active_date.score += 5
        call expression sasha.get_chat from _call_expression_399
        hide drink sasha
        $ sasha.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show sasha annoyed
        sasha.say "Nah, [hero.name] - I'm good."
        $ hero.cancel_activity()
        hide sasha
    return

label sasha_slap_ass_intro_female:
    "As soon as I see Sasha's ass, I can't fight the urge."
    "It's so sexy and it moves in just the right way."
    "I have to do it - there's no way I can resist!"
    "A moment later, the palm of my hand connects with her butt!"
    return

label sasha_slap_ass_happy_female:
    "Sasha jumps a little, her eyes going wide with surprise."
    sasha.say "Whoa..."
    sasha.say "Hey, [hero.name]...was that you?!?"
    "A sly smile spreads across Sasha's face as I nod."
    sasha.say "I really need to keep a closer eye on you, girl!"
    return

label sasha_slap_ass_angry_female:
    "Sasha jumps a little, her eyes going wide with surprise."
    sasha.say "HEY!"
    sasha.say "Who the hell..."
    sasha.say "Wait a minute...[hero.name], was that you?!?"
    "I look left and right, realising there's no chance of escape."
    bree.say "Erm, yeah, Sasha - I couldn't help myself!"
    sasha.say "Yeah, well try harder next time."
    sasha.say "Geez...you're getting as bad as a guy!"
    return

label sasha_breakup_female:
    show sasha
    "I take a deep breath and force myself to say what I have to say."
    bree.say "Ah, Sasha..."
    bree.say "We need to talk..."
    "I see Sasha's mood change as soon as I speak the words."
    sasha.say "Oh no..."
    show sasha sad
    sasha.say "I know what that means!"
    bree.say "I'm sorry, Sasha..."
    bree.say "I just feel like things aren't working out between us."
    bree.say "I tried as hard as I could to get around it..."
    "Sasha lets out a weary sigh and nods her head."
    sasha.say "Urgh..."
    sasha.say "But you just can't square the circle, right?"
    "I can only nod sadly and offer up a weak smile."
    "Which earns me the same in return from Sasha."
    "She doesn't even try to argue with me anymore."
    "So I guess it really is over between us."
    return

label sasha_go_steady_intro_female:
    "I take a deep breath and force myself to say what I have to say."
    bree.say "Ah, Sasha..."
    bree.say "I've been having a really good time with you recently..."
    sasha.say "Huh?"
    sasha.say "Oh yeah, [hero.name] - me too!"
    "Sasha's smile seems genuine, and it spurs me on to ask the question."
    bree.say "So I was thinking..."
    bree.say "Maybe we should make it official?"
    bree.say "Like come out and say we're an item?"
    return

label sasha_go_steady_yes_female:
    "Sasha nods at this, sending a wave of relief through my entire body."
    sasha.say "Sure thing, [hero.name]!"
    sasha.say "That's cool with me."
    return

label sasha_go_steady_no_female:
    "Sasha shake her head."
    sasha.say "No, [hero.name]!"
    sasha.say "That's not the right time for this."
    return

label sasha_pet_intro_female:
    "I know I shouldn't do it."
    "I know it's really wrong."
    "And I know that I'm going to regret it too."
    "But somehow I can't seem to stop myself."
    "I just stand up and pat Sasha on top of her head!"
    "I know, I know...she just looks so cute and so perfect!"
    return

label sasha_pet_happy_female:
    sasha.say "Hey!"
    sasha.say "What did I do to deserve that?"
    bree.say "Ah...sorry, Sasha..."
    bree.say "I couldn't help myself!"
    "Sasha shrugs off my apology."
    sasha.say "No big deal, [hero.name]."
    sasha.say "Just don't make a habit of it, yeah?"
    return

label sasha_pet_annoyed_female:
    sasha.say "HEY!"
    sasha.say "What in the hell was that?!?"
    bree.say "Ah...sorry, Sasha..."
    bree.say "I couldn't help myself!"
    "Sasha brushes aside my apology."
    sasha.say "Yeah?"
    sasha.say "Well try harder next time!"
    sasha.say "I'm not a damn dog!"
    return

label sasha_massage_intro_female:
    bree.say "Ooh, Sasha..."
    bree.say "That looks REALLY painful!"
    "Sasha nods in agreement and instantly regrets it."
    sasha.say "Argh..."
    sasha.say "Yeah, [hero.name]..."
    sasha.say "I pulled something at band practice the other day!"
    bree.say "You want me to see if I can help out at all?"
    bree.say "I'm told I give a pretty good massage!"
    return

label sasha_massage_accept_female:
    sasha.say "Would you?"
    sasha.say "Urgh..."
    sasha.say "That'd be amazing, [hero.name]!"
    sasha.say "How soon can you do it?"
    sasha.say "I'm kind of desperate here!"
    return

label sasha_massage_refuse_female:
    sasha.say "Oh no - no way!"
    sasha.say "Thanks for the offer, [hero.name]."
    sasha.say "But this is a bad one."
    sasha.say "I think I need to see a professional!"
    return

label sasha_piercing_nipples_reaction_female:
    "I can see that Sasha's got something that she wants to show me."
    "She keeps glancing down at her chest all the time, then back up at me."
    "I'm surprised she hasn't just whipped her top of and flashed me yet!"
    sasha.say "You can see them, right?"
    sasha.say "You like them, yeah?"
    bree.say "What are you talking about, Sasha?"
    sasha.say "My nipples, [hero.name]!"
    sasha.say "I got them pierced!"
    "My eyes pop open at the mere mention of nipple piercings."
    "And my mind is already filling up with the possibilities."
    bree.say "Oh wow, Sasha!"
    bree.say "That's great!"
    bree.say "I can't wait to see them..."
    return

label sasha_piercing_navel_reaction_female:
    "I can see that Sasha's got something that she wants to show me."
    "She keeps glancing down at her belly all the time, then back up at me."
    "I'm surprised she hasn't just whipped her top of and flashed me yet!"
    sasha.say "You can see it, right?"
    sasha.say "You like it, yeah?"
    bree.say "What are you talking about, Sasha?"
    sasha.say "My belly button, [hero.name]!"
    sasha.say "I got it pierced!"
    "My eyes pop open at the mere mention of piercings."
    "And my mind is already filling up with the possibilities."
    bree.say "Oh wow, Sasha!"
    bree.say "That's great!"
    bree.say "I can't wait to see it..."
    return

label sasha_piercing_clit_reaction_female:
    "I can see that Sasha's got something that she wants to show me."
    "She keeps glancing down at her groin all the time, then back up at me."
    "I'm surprised she hasn't just pulled down her pants and flashed me yet!"
    sasha.say "You can see it, right?"
    sasha.say "You like it, yeah?"
    bree.say "What are you talking about, Sasha?"
    sasha.say "My clit, [hero.name]!"
    sasha.say "I got it pierced!"
    "My eyes pop open at the mere mention of piercings."
    "And my mind is already filling up with the possibilities."
    bree.say "Oh wow, Sasha!"
    bree.say "That's great!"
    bree.say "I can't wait to see it..."
    return

label sasha_piercing_head_reaction_female:
    "I can see that Sasha's got something that she wants to show me."
    "She keeps pursing her lips, like she wants to open her mouth wide."
    "Then she suddenly sticks her tongue out at me!"
    sasha.say "You can see it, right?"
    sasha.say "You like it, yeah?"
    bree.say "What are you talking about, Sasha?"
    sasha.say "My tongue, [hero.name]!"
    sasha.say "I got it pierced!"
    "Sasha sticks her tongue out again, and now I see what she means."
    "My eyes go wide at the sight of the piercing in the middle of it."
    "And my mind is already filling up with the possibilities."
    bree.say "Oh wow, Sasha!"
    bree.say "That's great!"
    bree.say "I can't wait to find out what it feels like..."
    return

label sasha_movie_liked_reaction_female:
    bree.say "Wow..."
    bree.say "That was a great movie - right, Sasha?"
    "Sasha nods, not hesitating to agree with me."
    sasha.say "You're right there, [hero.name]!"
    sasha.say "I wish we could go right back in there and see it again!"
    return

label sasha_movie_indifferent_reaction_female:
    bree.say "Wow..."
    bree.say "That was a great movie - right, Sasha?"
    "Sasha shrugs and makes a non-committal sound."
    sasha.say "Meh..."
    sasha.say "It was okay, I guess."
    sasha.say "I wouldn't rush to see it again."
    return

label sasha_movie_disliked_reaction_female:
    bree.say "Wow..."
    bree.say "That was a great movie - right, Sasha?"
    "Sasha shakes her head and shudders."
    sasha.say "Urgh..."
    sasha.say "No way, [hero.name] - that movie was utter garbage!"
    sasha.say "I can't believe you talked me into seeing it."
    return

label sasha_abortion_reaction_female:
    sasha.say "[hero.name]..."
    sasha.say "We really need to talk!"
    "I jump a little at the sound of Sasha's voice."
    "But part of me is already sure I know what this is about."
    "I mean it's not like Sasha isn't female."
    "She was going to notice sooner or later."
    bree.say "Yeah, Sasha?"
    bree.say "What do you want to talk about?"
    sasha.say "Oh, come on, [hero.name]!"
    sasha.say "You can pull that shit with [mike.name]."
    sasha.say "But it's not going to work on me!"
    sasha.say "You were pregnant, and now you're not."
    "I hesitate for a moment, but then I nod."
    "As there doesn't seem to be any point in trying to hide it."
    bree.say "You got me, Sasha."
    sasha.say "So what in the hell happened?!?"
    bree.say "I couldn't go through with it."
    bree.say "That's what happened."
    bree.say "I got a termination."
    if sasha.love >= 150:
        sasha.say "Urgh..."
        sasha.say "That sounds awful, [hero.name]."
        sasha.say "It must have been hard."
        "I nod, already feeling tears welling in my eyes."
        "It's just such a relief to hear that someone understands."
        bree.say "I feel like a monster, Sasha."
        bree.say "But I just knew I couldn't cope."
        "Sasha nods as she puts an arm around me."
        sasha.say "It's going to be okay, [hero.name]."
        sasha.say "It might not feel like it now."
        sasha.say "But it will."
        sasha.say "Just give it time."
        "I nod and try to smile."
        "Even though it's the last thing I feel like doing."
    else:
        sasha.say "You did WHAT?!?"
        sasha.say "No way, [hero.name]!"
        sasha.say "Tell me I didn't hear that!"
        "Part of me feels shocked at Sasha's reaction."
        "But another part of me is instantly enraged by it too."
        "And that's the side of me that wins out."
        bree.say "You think I'd joke about something like that?!?"
        bree.say "It was the hardest decision I ever had to make."
        bree.say "And I could use some understanding from you!"
        "Sasha shakes her head at this."
        "And it looks like she's going to double down instead."
        sasha.say "You could have asked for help, [hero.name]."
        sasha.say "You have friends that would have been there."
        sasha.say "Shit, you could have put the kid up for adoption!"
        bree.say "That's easy for you to say, Sasha."
        bree.say "You weren't the one that was pregnant!"
        "I hold up a hand, cutting Sasha off."
        "And then I turn my back and walk away."
    return


label sasha_belly_interaction_female:
    $ sasha.set_flag("interact", 1, 1, "+")
    show sasha at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call sasha_belly_kiss_female from _call_sasha_belly_kiss_female_1
        "Caress my belly":
            call sasha_belly_caress_female from _call_sasha_belly_caress_female_1
        "Listen to the baby":
            call sasha_belly_listen_female from _call_sasha_belly_listen_female_1
        "Never mind":
            pass
    return

label sasha_belly_caress_female:
    show sasha normal at center, zoomAt(1.5, (640, 1040))
    "I can see that Sasha's staring at me right now, like she can't take her eyes off my bump."
    "Sure, every time I glance in her direction, she looks away and tries to pretend like she's not."
    "As if that was ever going to be enough to convince me that she wasn't staring in the first place!"
    "But no matter how many times we play this little game, she doesn't seem to gain enough courage to say a word."
    "So in the end, I decide to be the one that's going to speak up and say something about it."
    bree.say "Sasha..."
    bree.say "Will you quit staring at my belly?"
    bree.say "You're kinda making me nervous!"
    show sasha stuned at center, traveling(1.25, 0.1, (640, 880))
    "As soon as Sasha realises I'm onto her, she jumps back in alarm."
    "And she starts shaking her head, almost like she's going to deny it."
    show sasha whining
    sasha.say "I..."
    sasha.say "I'm sorry, [hero.name]."
    sasha.say "It's just that...well..."
    sasha.say "I was on only child, you know?"
    show sasha sadsmile
    "I can't help raising my eyebrows at this."
    "Because it's something I genuinely didn't know about Sasha."
    bree.say "No, Sasha..."
    bree.say "You never told me that before now."
    "Sasha shrugs and shakes her head."
    show sasha shout
    sasha.say "Well I was..."
    sasha.say "So I never really got to be around someone that was pregnant before now."
    show sasha normal
    "Sasha seems to be losing her concentration as she tells me all of this."
    "Because I can see her eyes drifting back to my belly again."
    "And I think I know where this is going too."
    bree.say "Would you like to touch it?"
    bree.say "You can if you'd like."
    show sasha stuned
    "Now Sasha looks up at me, straight into my eyes too."
    show sasha surprised
    sasha.say "Are you serious?"
    show sasha shout
    sasha.say "Of course I want to touch it!"
    show sasha normal
    "I can't help smiling as I lift up my top to reveal the curve of my belly."
    "And I feel an immense sense of pride as I thrust it towards Sasha too."
    show sasha shy at center, traveling(1.5, 0.3, (640, 1040))
    "She reaches out slowly at first, as if worried that I might change my mind."
    "That I might snatch it away when her fingers are withing mere inches of it."
    "But I'm not out to play games with Sasha, so I keep myself totally still."
    "And that means I feel the coolness of her fingers as they touch my skin."
    "I'm careful to keep quiet as Sasha begins to stroke them over it."
    "But the real pleasure comes from watching the expression on her face change."
    "Soon enough it goes from one of hesitation to amazement."
    show sasha happy
    "And from there her mood seems to only get better as her smile widens."
    "Something that I can feel being reflected in my own face too."
    $ sasha.love += 2
    return

label sasha_belly_kiss_female:
    show sasha shy at center, zoomAt(1.5, (640, 1040))
    "Sasha seems to be a little more comfortable around me now that we've addressed the elephant in the room."
    "That being the fact that I'm hauling around an ever-expanding pregnant belly right now."
    "And the fact that she was itching to be able too touch the thing, but didn't know how to ask."
    "So now she's been allowed to touch it, I thought that I was in for an easier time of it."
    show sasha embarrassed
    "But the next time that Sasha puts a hand on my bump, I see that look on her face again."
    "Though this time I'm not in the mood to beat about the bush, so I straight up call her on it."
    bree.say "What's the matter now, Sasha?"
    bree.say "I thought we'd worked out all of your issues with my belly?"
    show sasha sadsmile
    "Sasha instantly puts on a forced smile, trying to play it down."
    show sasha surprised at center, zoomAt(1.5, (640, 1040))
    sasha.say "Huh?"
    sasha.say "What are you talking about, [hero.name]?"
    show sasha sadsmile
    "This time I don't even bother to say another word."
    "Instead I fix Sasha with a particularly hard stare instead."
    "And it seems to have the desired effect pretty quickly."
    show sasha shout
    sasha.say "Okay, okay..."
    sasha.say "I'll tell you what's the matter."
    sasha.say "So long as you stop looking at me like that!"
    show sasha normal
    "I do as she asks, waiting to hear the explanation that follows."
    show sasha shout blush
    sasha.say "I..."
    sasha.say "I was just wondering if..."
    sasha.say "If I could...well, if I could kiss it?"
    show sasha sadsmile
    "I feel my eyebrows shoot up as Sasha asks the question."
    "But she seems to take this as confirmation of my disapproval."
    show sasha whining
    sasha.say "I know, I know..."
    sasha.say "Too weird, right?"
    show sasha sadsmile
    bree.say "No, Sasha..."
    bree.say "It sounds really sweet!"
    show sasha surprised
    "Sasha watches with surprise written all over her face as I nod in agreement."
    "Then I lift up my shirt to show her that I'm being serious."
    show sasha shy at center, traveling(2.5, 0.3, (640, 1940))
    "She leans in, just like before, watching me for any sign of mischief."
    "But I'm totally serious, and I don't move a muscles as she comes closer."
    show sasha happy
    "Finally Sasha's close enough to close her eyes and purse her lips."
    "Then she proceeds to plant a series of gentle kisses on my bump."
    "The sensation is really pleasant, like being tickled, rather than kissed."
    "And I feel a tingling sensation travel outwards, reaching every part of my body."
    $ sasha.love += 3
    return

label sasha_belly_listen_female:
    show sasha surprised blush at center, zoomAt(1.5, (640, 1040))
    sasha.say "WHOA!"
    show sasha stuned
    "Sasha has her hands on my bump at the perfect moment to feel the baby move."
    "By now it's something that I'm starting to get used to, feeling it every day."
    "But I can understand the look of surprise and amazement on her face as she feels it for the first time."
    bree.say "Pretty crazy, huh?"
    show sasha surprised
    sasha.say "Totally amazing!"
    show sasha stuned
    "Sasha's shaking her head as she begins to lean in closer still."
    "And she points to her ear as she does so, making her intentions clear."
    sasha.say "You mind if I..."
    sasha.say "If I try to listen?"
    "I have no idea of that's even possible with just a human ear."
    "But I'm loving the look of fascination on Sasha's face right now."
    "And the last thing that I want is to damped her enthusiasm."
    "So I give her a quick shrug and a nod of the head."
    bree.say "Go right ahead, Sasha..."
    bree.say "Just be sure to let me know what you hear, okay?"
    show sasha shy at center, traveling(2.5, 0.3, (640, 1940))
    "Sasha's nodding too, as she put her ear against my belly."
    "Then she makes a point of waving her hand in the air."
    "And I take that to mean she wants me to be quiet while she listens."
    show sasha happy
    "We sit there for a what can only be a couple of minutes."
    "Though it feels like a much longer span of time."
    "Pretty soon I'm beginning to think that the baby's not going to oblige."
    "That they must have fallen asleep in there and Sasha's listening in vain."
    "But then I feel a sudden movement from down below."
    "In truth I have no idea which of them actually moves first."
    show sasha normal
    "Because Sasha and the baby seem to come alive in the same moment."
    show sasha shout
    sasha.say "There it is..."
    sasha.say "I can hear them moving - and I can feel them too!"
    show sasha normal
    bree.say "Ah, yeah..."
    bree.say "I know all about it, Sasha."
    bree.say "The baby is inside of me, remember?"
    "But my question goes unanswered, as Sasha's too busy to even hear it."
    "Instead all of her attention is taken up with pressing her ear to my belly."
    "She follows the baby this way and that, straining to make out all that she can."
    "And at the end of the day, what she can actually hear doesn't seem to matter."
    "Because it's more important for the sake of bonding than anything else."
    $ sasha.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
