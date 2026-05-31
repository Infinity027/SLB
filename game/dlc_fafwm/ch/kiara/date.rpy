label kiara_date_eat_a_burger:
    "Kiara looks at her burger as if she expects it to suddenly sprout legs and walk off the plate."
    "But then she shrugs and reaches out to pick it up for the first time, squeezing it gently."
    "I watch as she takes a bite, chews and swallows, then nods as she proceeds to eat the rest."
    return

label kiara_date_buy_drink:
    "As I drain the last few dregs of my drink, I'm already standing up and turning towards the bar."
    mike.say "Looks like it's time for another round."
    mike.say "How about you, Kiara?"
    mike.say "You want a pint of something?"
    if kiara.is_visibly_pregnant:
        "Kiara's eyes go wide with surprise as I ask the question."
        "And at the same time her hands move to her belly, as if to shield it from harm."
        kiara.say "[hero.name], did you forget about something?!?"
        $ kiara.love -= 2
        "Suddenly reminded of the fact she's pregnant, I shake my head."
        mike.say "Oh yeah, sorry!"
        mike.say "Maybe a soft drink or a fruit-juice instead?"
        $ hero.cancel_activity()
    else:
        "Kiara picks up her glass and swills around the remaining liquid inside."
        kiara.say "I think that you are trying to get me drunk!"
        kiara.say "But then so what if you are?"
        kiara.say "I will have another one of these."
        $ kiara.set_flag("drinks", 1, "day", mod="+")
    return

label kiara_date_play_darts:
    "Kiara looks at the darts I hand her like she's not sure what they're for."
    "But once we're standing in front of the board, she lines herself up pretty well."
    "And then I watch as she pulls back her arm and releases the dart with ease."
    "So it seems that I've got a game against a natural on my hands."
    "Which should prove to be an interesting affair."
    return

label kiara_date_pub_play_pool:
    "Kiara takes the cue that I offer her, but she doesn't look confident."
    "And once we start playing the actual game, I can soon see why that is."
    "Let's just say that Kiara's not a natural when it comes to the game."
    "And so I have to make a point of going pretty easy on her."
    "But even so, she doesn't seem to enjoy the game that much."
    return

label kiara_date_buy_a_round:
    "I drain the last dregs of my drink and then push back my chair."
    "Looking around the table, I begin turning towards the bar."
    mike.say "Looks like it's time for another round."
    mike.say "And I think it's my turn to get one in."
    mike.say "So, same again?"
    if kiara.is_visibly_pregnant:
        "Kiara's eyes go wide with surprise as I ask the question."
        "And at the same time her hands move to her belly, as if to shield it from harm."
        kiara.say "[hero.name], did you forget about something?!?"
        $ kiara.love -= 2
        "Suddenly reminded of the fact she's pregnant, I shake my head."
        mike.say "Oh yeah, sorry!"
        mike.say "Maybe a soft drink or a fruit-juice instead?"
        $ hero.cancel_activity()
    else:
        "Kiara picks up her glass and swills around the remaining liquid inside."
        kiara.say "I think that you are trying to get me drunk!"
        kiara.say "But then so what if you are?"
        kiara.say "I will have another one of these."
        $ game.active_date.score += 5
        if "rebel" in kiara.traits:
            $ game.active_date.score += 5
        $ kiara.set_flag("drinks", 1, "day", mod="+")
    return

label kiara_dance_with:
    mike.say "Hey, Kiara - let's dance!"
    kiara.say "What a good idea - let's go!"
    "I reach out my hand and Kiara grab hold of it, almost dragging me onto the dance-floor."
    "And once we're there, she presses herself close to me the whole time."
    "Making sure that the experience is both intense and memorable."
    return

label kiara_date_play_arcade_intro:
    mike.say "Look, Kiara - they've got a new retro arcade cabinet!"
    kiara.say "Oh...are you into that kind of thing?"
    mike.say "You bet I am - let's go play a couple of games."
    kiara.say "I suppose we could, if you insist..."
    "I can hear the reluctance in Kiara's voice, but I choose to ignore it."
    "Because there's no way I'm going to pass up the chance to play the arcade-game."
    "As soon as we're there, I start fishing in my pocket for change."
    "And then I pump the coins into the slot, listening to the sound of the credits piling up."
    mike.say "Okay, just do what I do, okay?"
    kiara.say "I will do my best."
    return

label kiara_date_play_arcade_win:
    "From the moment the game starts, I'm totally in the zone."
    "And I mean it to, my playing is almost perfect - flawless even."
    "But the problem is that Kiara's not picking it up like I'd hoped."
    "She seems to be struggling even to make her sprite move around the screen."
    "Which of course means that it's not long before she's totally vanquished."
    mike.say "YES!"
    mike.say "I win!"
    kiara.say "Is that it?"
    kiara.say "Can we stop playing this game now?"
    mike.say "Erm...yeah, I guess so."
    "Part of me wants to keep on crowing about my victory."
    "But another is getting ever more embarrassed at Kiara's obvious discomfort."
    return

label kiara_date_play_arcade_lose:
    "From the moment the game starts, nothing seems to go right for me."
    "It's a game that I must have played a hundred times in the past."
    "But no matter how hard I try, I just can't get it together."
    "Which means that Kiara's lack of skill and interest really doesn't matter."
    "In fact I'm playing so badly that she actually ends up narrowly beating me!"
    mike.say "Damn it!"
    mike.say "I can't believe that I lost."
    kiara.say "You did?"
    kiara.say "So that mean...I won?"
    kiara.say "Can we stop playing this game now?"
    mike.say "Erm...yeah, I guess so."
    "Luckily for me it seems like Kiara's not interested in celebrating her victory."
    "Which means that I can slink off and try to forget about how badly I just got humiliated."
    return

label kiara_dick_reactions_male:
    if not kiara.flags.seendick:
        $ kiara.flags.seendick = 1
        "I feel more than a little exposed as I'm standing naked in front of Kiara for the first time."
        "Her eyes are wandering all over me, taking everything in with great interest."
        "But when her gaze finally settles on my groin, those eyes suddenly go wide with surprise."
        mike.say "Erm...what's up, Kiara?"
        mike.say "Is there something wrong with what you're seeing down there?"
        if hero.has_skill("hung"):
            "Kiara shakes her head, eyes growing wider still."
            show dick reactions kiara scared
            kiara.say "But it is so...so big!"
            kiara.say "I had not thought one could grow to be so large."
            show dick reactions kiara smile
            kiara.say "I am thrilled at the thought of seeing what it can do."
            kiara.say "But also a little afraid of it too!"
            $ kiara.sub += 10
        elif hero.has_skill("smalldick"):
            "Kiara shrugs and shakes her head."
            show dick reactions kiara mock
            kiara.say "Hmm..."
            kiara.say "Maybe it is a little smaller than I would have liked."
            show dick reactions kiara smile
            kiara.say "But then you will have to rise to the challenge, [hero.name]."
            show dick reactions kiara mock
            kiara.say "You will have to show me how you make the most of it!"
            $ kiara.sub -= 10
        hide dick reactions
    return

label kiara_date_intro_valentine_male:
    return

label kiara_date_intro_halloween_male:
    return

label kiara_date_intro_christmas_male:
    return

label kiara_date_intro_birthday_male:
    return

label kiara_date_intro_mc_birthday_male:
    return

label kiara_date_park_male:
    return

label kiara_date_amusement_park_male:
    scene bg amusement
    show kiara
    with fade
    "I thought that inviting Kiara along to the Amusement Park was a sure-fire thing."
    "That she'd be delighted to visit the place and spend some time on all of the rides."
    "But as we're walking towards the gates, I can see that she's not looking very pleased."
    "In fact the expression on her face is one that would usually make me leave her well enough alone."
    "The only problem with that is the fact we're going in there to spend some time together."
    "So she's only going to get more upset the longer I leave it before asking her what the problem is."
    "Which means I have to take a deep breath and steel myself for whatever reaction is coming my way."
    mike.say "Erm..."
    mike.say "Kiara..."
    kiara.say "Yes?"
    kiara.say "What is it?"
    kiara.say "Is there a problem, huh?"
    "Even knowing that Kiara wasn't happy could not have prepared me for that response."
    "And I almost stumble, stepping backwards and walking into someone walking behind me."
    mike.say "Whoa!"
    mike.say "Settle down, Kiara!"
    "The moment she sees how her reaction has affected me, Kiara's expression softens."
    "And she shakes her head, letting me know that her intention was not to hurt me."
    kiara.say "Oh, I am sorry, [hero.name]."
    kiara.say "I should never have agreed to come here."
    kiara.say "This kind of place is too noisy for me, too crowded, you know?"
    mike.say "Ah...yeah..."
    mike.say "I can see how that might be an issue."
    mike.say "Do you want to...I dunno...go somewhere else?"
    "Kiara screws her face into a frown and shakes her head."
    kiara.say "No, no, no..."
    kiara.say "I am being too dramatic."
    kiara.say "This is not so bad as I make it sound."
    kiara.say "Let us go inside and have some fun, okay?"
    "I nod and hold out my hand for Kiara to take."
    "But as we walk inside, I hope that she really means what she just said."
    "And that she's not just putting on a brave face for my sake alone."
    return

label kiara_date_ferris_wheel_male:
    show kiara
    mike.say "Let's ride the Ferris Wheel, Kiara..."
    mike.say "Well, if you want to?"
    mike.say "I mean, do you want to?"
    "Kiara gives me one of her signature shrugs."
    "And she underlines her nonchalance with a shake of the head too."
    kiara.say "If that's what you want, [hero.name]…"
    kiara.say "Then sure, we can ride it."
    "Not the most enthusiastic of answers."
    "But I'm not about to turn it down either."
    "So with a nod, I take hold of Kiara's hand."
    "Then I lead her over to the back of the queue, and we wait for our turn."
    "Which isn't long in coming around, so we're soon stepping into a gondola."
    "And once the safety-bar comes down, we begin to rise into the air."
    "I keep on trying to impress upon Kiara how amazing the ride is."
    "Shooting smiles in her direction and gently nudging her too."
    "But by the time we reach the top of the wheel, I know it's not working."
    "The ride stops so that we can enjoy the view."
    "And I feel like this is a good time to ask Kiara what the problem could be."
    mike.say "What's wrong, Kiara?"
    mike.say "Are you afraid of heights or something?"
    kiara.say "No, [hero.name]…"
    kiara.say "That's not it."
    mike.say "Don't you like the view from up here?"
    mike.say "Because it looks pretty stunning to me!"
    "Kiara lets out a sigh and shakes her head."
    kiara.say "Oh, [hero.name]…"
    kiara.say "When you have seen the sun set over Paris from the top of the Eiffel Tower."
    kiara.say "Only then will you understand why all other views pale into insignificance!"
    "All I can do is nod and turn my attention back to the apparently substandard view."
    "Because there's no way I can compete with that!"
    $ kiara.love -= 1
    $ game.active_date.score -= 10
    return

label kiara_date_merry_go_round_male:
    show kiara
    "I see Kiara staring intently at something, her eyes wide with interest."
    "So I do the best I can to follow her line of sight, trying to see what's so interesting."
    "The only thing she can be so fixated on is the Merry-Go-Round over there."
    "It's the old-fashioned kind, with gilded poles supporting painted horses."
    "Not my idea of an exciting ride, but if it floats Kiara's boat..."
    mike.say "You like the look of the Merry-Go-Round, Kiara?"
    "At the sound of my voice, Kiara turns around."
    "She seems a little caught off-balance, like she was just miles away."
    kiara.say "Oh..."
    kiara.say "Oh yes, [hero.name]…"
    kiara.say "Now this is something that I do remember."
    kiara.say "Something that we used to have back home in France."
    "Of really?"
    "Let me guess, that means it's going to be the best thing ever."
    "At least in Kiara's mind!"
    "But that's no reason for me to look a gift horse in the mouth."
    "If you'll pardon the pun..."
    mike.say "Then we should totally ride it, Kiara."
    mike.say "Come on!"
    "I make straight for the back of the queue, with Kiara following close behind."
    "And we're lucky that this is an older ride too, as it means the line is short."
    "Soon enough we're at the front and taking our turn on the Merry-Go-Round."
    "Kiara seems to take a great deal of time and care in picking her horse."
    "But once she's found the one she wants, she sits down and holds onto the pole."
    "Not being so picky, I only want to be on the horse next to her."
    "So once I am, we're all ready to go."
    "The ride begins to move turn, slowly at first, but getting ever faster."
    "And soon it's moving at a pretty impressive rate."
    "So much so that I have to hold on tight to keep from falling off."
    "At the same time as I'm doing this, I can hear laughter beside me."
    "And when I look around, I see Kiara, her face a picture of delight."
    kiara.say "This is fabulous!"
    kiara.say "I feel so free, so liberated..."
    kiara.say "Like I am a little girl again!"
    $ kiara.love += 2
    $ game.active_date.score += 20
    return

label kiara_date_haunted_house_male:
    show kiara
    mike.say "Hey, Kiara..."
    mike.say "There's the Haunted House!"
    mike.say "It's one of my favourites."
    "Kiara follows as I walk over to the Haunted House."
    "And I see her looking up at the ghosts and skeletons that adorn the exterior of the ride."
    "If I had to choose a word to describe her expression, it'd probably be unimpressed."
    kiara.say "This one is your favourite?"
    kiara.say "The one that looks like something for children on Halloween?"
    mike.say "Oh come on, Kiara..."
    mike.say "Don't tell me there are no Haunted Houses in France!"
    kiara.say "Of course there are, [hero.name]."
    kiara.say "But all of ours are centuries old and filled with real spirits!"
    kiara.say "This is just, how you say...cheap crap!"
    "I frown at Kiara and walk over to join the end of the line."
    "Then I stand with my arms crossed, looking at her in defiance."
    mike.say "Well I don't care what you think of it."
    mike.say "I'm going inside!"
    "Kiara chuckles and shakes her head at this."
    "But she walks over to join me all the same."
    kiara.say "Oh, [hero.name]..."
    kiara.say "You are so funny when you get this childish!"
    "I do the best I can to take that as a compliment."
    "And I soon forget all about it once we're inside the Haunted House."
    "As usual, I have a great time walking through it."
    "I'm running one moment and dodging the jump-scares the next."
    "All the while, Kiara is walking just behind me."
    "Shaking her head in disbelief that I'm enjoying it all so much."
    $ kiara.love -= 1
    $ game.active_date.score += 10
    return

label kiara_date_love_boat_male:
    show kiara
    "As soon as I see the sign for the Love Boat, I just know that we have to ride it."
    "Any chance to be alone with Kiara sounds good to me, far too good to be missed."
    "And she's sure to be up for it, as she's such a romantic kind of woman too!"
    mike.say "Let's go on the Love Boat next, Kiara."
    kiara.say "Love Boat?!?"
    kiara.say "What exactly is there to love about it, huh?"
    "I'm more than a little thrown by Kiara's reaction."
    "Instead of being up for it, she seem to be looking at the ride in disdain."
    mike.say "Erm..."
    mike.say "Well..."
    mike.say "It's romantic, Kiara!"
    "Kiara doesn't dignify this with an answer."
    "Instead she raises her eyebrows at me."
    "Which seems to say that my explanation's not good enough."
    mike.say "You and me, together in a little boat?"
    mike.say "Alone and in the darkness?"
    mike.say "With nobody to see what we're doing?"
    "Kiara shakes her head as we walk over to the queue for the ride."
    kiara.say "Oh, [hero.name]..."
    kiara.say "Whatever am I going to do with you?"
    kiara.say "Romance should not be hidden and passion should not be confined to the darkness!"
    kiara.say "When will you learn this?!?"
    "Needless to say the ride in the Love Boat is less than romantic."
    "Kiara continues to lecture me about how boring the whole thing is."
    "And then she moves on to telling me that I need to be more liberated."
    "All of which means I'm pretty relieved when the ride is finally over."
    $ kiara.love -= 1
    $ game.active_date.score -= 10
    return

label kiara_date_hedge_maze_male:
    show kiara
    "Maybe what we need next is a change of pace?"
    "Most of the rides here are pretty crazy and exciting."
    "But the Hedge Maze looks way more chilled-out."
    mike.say "You want to do the Hedge Maze, Kiara?"
    mike.say "Could be fun, yeah?"
    "Kiara looks genuinely surprised to see the maze there in front of us."
    "She gives a shrug and then nods her head."
    kiara.say "Why not?"
    kiara.say "Let's give it a try."
    "That's good enough for me."
    "And so we hurry over to join the back of the line."
    "What with all the more impressive rides, the queue is pretty short."
    "Which means it's not long before we're walking into the maze."
    "Kiara and I spend the rest of our time in there walking the passages."
    "And we seem to become more lost with each corner we turn."
    "More than once I think we've totally turned around on ourselves."
    "But by putting our heads together, we finally manage to find a way out."
    "Afterwards we're calmer than before, but I don't feel an urge to go back in there."
    "Maybe once around a maze like that is all you really need."
    $ kiara.love += 1
    $ game.active_date.score += 10
    return


label kiara_date_amusement_ice_cream_male:
    mike.say "So..."
    mike.say "Would you like an ice-cream, Kiara?"
    "I'm expecting Kiara to just flat out say no to the idea."
    "After all, she's used to the better things in life, right?"
    "So an ice-cream from a crappy little stand isn't really going to impress, now is it?"
    "But to my genuine surprise, she seems almost intrigued by the idea."
    kiara.say "Why of course, [hero.name]..."
    kiara.say "So long as we can share one, yes?"
    "I wasn't expecting Kiara to make such a suggestion."
    "But at least she said yes to the idea."
    mike.say "Sure thing, Kiara..."
    mike.say "Let's go join the queue."
    "Kiara happily takes my hand when I extend it to her."
    "And soon enough we're ordering the ice-cream she wants."
    "I let her hold it, but she instantly puts her hand around mine."
    "And as we walk away, she makes sure to lean in close."
    "This means that our cheeks are almost touching as we lick away."
    "And now I can see why she wanted to do it this way."
    "Kiara's turned simply sharing an ice-cream into an intimate experience."
    "One that I'm going to remember for a very long time to come."
    "And all for just the cost of an ice-cream cone."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
