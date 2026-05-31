label harmony_date_amusement_park_male:
    if harmony.purity >= HP:
        scene bg amusement
        with fade
        show harmony b happy
        "I was in two minds as to whether I should ask Harmony to come to the Amusement Park with me."
        "Because it's kind of a wild thing to do, spending the entire day on the rides."
        "And I was worried that she might think it was a waste of time, or too self-indulgent."
        "But from the smile on Harmony's face as we walk through the gate, it looks like I was wrong."
        mike.say "You seem like you're looking forward to this, Harmony..."
        mike.say "Do you come to the Amusement Park often?"
        harmony.say "Oh goodness me, no!"
        harmony.say "I can't remember the last time I came to a place like this."
        mike.say "You mean you never went to an Amusement Park before?"
        "Harmony looks thoughtful for a moment, like she's trying to recall."
        harmony.say "Hmm..."
        harmony.say "I might have, once or twice."
        harmony.say "But I don't really remember it that well."
        mike.say "So this is almost like the first time you've been here?"
        "Harmony thinks about this, and then she nods."
        harmony.say "I suppose you could say that, [hero.name]."
        harmony.say "And I that sort of makes this a special occasion too!"
        "I nod too, doing all I can to echo that sentiment."
        mike.say "You got it, Harmony..."
        mike.say "Let's make this a day to remember."
        mike.say "So that you'll never forget coming here again!"
    else:
        scene bg amusement
        with fade
        show harmony a happy
        "I wasn't sure about inviting Harmony along to the Amusement Park with me today."
        "Not because I'm worried about her thinking it's a sinful kind of place."
        "I think we're past the point of pretending that she's the same girl I met back at the church!"
        "No, it was more because I wasn't sure this place would be wild enough for her."
        "But as we're walking in through the gate, I see that Harmony's smiling."
        mike.say "You're looking forward to this, Harmony?"
        mike.say "Does that mean you like Amusement Parks?"
        "Harmony chuckles and shakes her head."
        harmony.say "Oh, I'm looking forward to it alright."
        harmony.say "But I don't remember ever coming here before now."
        "Now that is a statement that catches me off-guard."
        "And I have to shake my head as I try to make sense of it."
        mike.say "Are you sure, Harmony?"
        mike.say "I thought everyone had been to an Amusement Park!"
        mike.say "Once time at least."
        "This time it's Harmony that shakes her head."
        harmony.say "Nope - not me."
        harmony.say "My parents were convinced these places were sinful."
        harmony.say "Filled to the brim with temptations, they said."
        harmony.say "And now I get the chance to see if they were right!"
    return

label harmony_date_ferris_wheel_male:
    mike.say "Hey, Harmony..."
    mike.say "Let's ride the Ferris Wheel."
    "Harmony looks up at the Ferris Wheel towering above us."
    "But the only thing she gives me in way of a reaction is a slight shrug."
    harmony.say "I guess so, [hero.name]."
    harmony.say "I mean, if you want to."
    "I can't help feeling a little let down by Harmony's reaction."
    "I assumed the fact she's never really been to a place like this would make a difference."
    "Like she'd be eager to try out all the rides that she never got to enjoy as a kid."
    "But I resolve to do the best I can to make up for it."
    "Maybe that way my own enthusiasm will start to rub off on her."
    "Harmony and I join the queue, waiting for our turn to come round."
    "And when it does we climb into the gondola and pull down the safety bar."
    mike.say "The view from the top of this thing is amazing, Harmony."
    mike.say "Just wait until you see it!"
    "Harmony gives me a polite smile and a little nod."
    "But once we do get to the top, she shows no sign of amazement."
    mike.say "So?"
    mike.say "What do you think?"
    harmony.say "It's a really nice view, [hero.name]."
    harmony.say "But it's not like I haven't seen it before."
    harmony.say "I mean, I've been on the top floor of tall buildings."
    harmony.say "So none of it's new to me!"
    $ harmony.love -= 0
    $ game.active_date.score -= 0
    return

label harmony_date_merry_go_round_male:
    mike.say "The Merry-Go-Round!"
    mike.say "You have to ride on that one, Harmony."
    "Harmony takes a look a the ride in question as I point it out to her."
    "But from the look on her face, she doesn't seem convinced."
    harmony.say "Are you sure, [hero.name]?"
    harmony.say "It kind of looks like a kid's ride to me!"
    "I can tell that Harmony's not into the idea."
    "But I'm having none of it."
    mike.say "It's not just for kids, Harmony."
    mike.say "This is a ride for everyone."
    mike.say "A ride that everyone remembers fondly."
    "Before Harmony can object for a second time, I leap into action."
    "Pulling her after me, I make for the back of the queue."
    "Harmony allows me to have my way, and soon we're waiting in line."
    "Then when we get to the head of the queue, we climb onto the ride."
    "I keep shooting smiles at Harmony as it starts to move."
    "All the time hoping that she's going to get into it."
    "But even when the ride begins to pick up speed, it doesn't seem to help."
    "Harmony looks more than a little bored and distracted the whole time."
    "And once we're getting off, she seems glad that it's over."
    mike.say "Erm..."
    mike.say "How was it, Harmony?"
    harmony.say "I don't care what you say, [hero.name]…"
    harmony.say "That's definitely a ride for kids."
    harmony.say "Can we please ride something a little more adult next?"
    $ harmony.love -= 1
    $ game.active_date.score -= 10
    return

label harmony_date_haunted_house_male:
    mike.say "Look, Harmony..."
    mike.say "They have a Haunted House!"
    mike.say "That's like my favourite thing!"
    "I don't give Harmony time to respond to what I just said."
    "Instead I hurry straight over to the Haunted House."
    "Which leaves her to follow along behind me."
    harmony.say "That's your favourite thing here?"
    harmony.say "Something that's all spooky and nasty?!?"
    mike.say "What are you talking about, Harmony?"
    mike.say "It's no more extreme than the stuff you see on Halloween."
    "Harmony fixes me with a withering stare."
    harmony.say "Trust me, [hero.name]…"
    harmony.say "I had the strictest religious upbringing you can imagine."
    harmony.say "You think I spent much time trick or treating?"
    mike.say "Oh come on, Harmony..."
    mike.say "You'll love it, I promise."
    "Harmony doesn't look convinced, but we join the queue anyway."
    "And soon enough we're walking through the entrance of the Haunted House."
    "Almost as soon as we turn the first corner, something jumps out in front of us."
    "The second that happens, Harmony let's out a piercing scream."
    "And she almost leaps into my arms."
    "Which for a girl with those curves is quite a feat!"
    "This sets the precedent for what follows as we hurry along."
    "Each and every scare seems to scare Harmony out of her wits."
    "And by the time we come out of the other end, she's a quivering wreck."
    "I do the best I can to comfort her, assuring her that it's all over."
    "But I know that taking her in there was a huge mistake."
    $ harmony.love -= 2
    $ game.active_date.score -= 20
    return

label harmony_date_love_boat_male:
    if harmony.purity >= HP:
        harmony.say "What's that ride, [hero.name]?"
        harmony.say "That one right there?"
        "I look in the direction Harmony's pointing."
        mike.say "Oh yeah..."
        mike.say "That's the Love Boat, Harmony."
        "I'm expecting that to explain everything."
        "But instead Harmony just stares at me blankly."
        mike.say "You know, the Tunnel of Love?"
        mike.say "Two people, in a boat, sailing through a dimly-lit tunnel?"
        "I raise my eyebrows as I say all of this."
        "And thankfully that seems to have the desired effect."
        harmony.say "Oh..."
        harmony.say "Oh, I see!"
        harmony.say "What are we waiting for?"
        "I look down to see that Harmony's taken hold of my hand."
        "And before I can say another word, she yanks me towards the ride."
        "Luckily for us, the queue is pretty short."
        "So we're climbing into our boat in record time."
        "And Harmony only just waits for us to be out of sight."
        "Then she leans in, wrapping her arms around me."
        "What follows is one of the most pleasant experiences of my life."
        "And it'll certainly always be one of my favourite memories of this place."
        "So much so that I'm disappointed when the ride comes to an end."
        "And I almost suggest that we ride it again as soon as it does."
    else:
        harmony.say "What's that ride, [hero.name]?"
        harmony.say "That one right there?"
        "I look in the direction Harmony's pointing."
        mike.say "Oh yeah..."
        mike.say "That's the Love Boat, Harmony."
        "At the mere mention of the word, Harmony's eyes light up."
        "I look down to see that she's taken hold of my hand."
        "And before I can say another word, Harmony yanks me towards the ride."
        harmony.say "Now this is my kind of ride!"
        harmony.say "Just wait until I get you inside!"
        "Luckily for us, the queue is pretty short."
        "So we're climbing into our boat in record time."
        "And Harmony only just waits for us to be out of sight."
        "Then she practically pounces on me, wrapping me in her arms."
        "For the rest of the ride, Harmony is all over me."
        show harmony kiss
        $ harmony.flags.kiss += 1
        "She takes full advantage of the fact we can't be seen."
        "Smothering me with kisses and exploring every inch of my body with her hands."
        "I barely have the chance to make sense of what's happening to me."
        "And the darkness means I never know what she's going to do next."
        "More than once I'm sure that Harmony's going to tip over the boat."
        "I swear that I feel the sensation of cold water splashing over me."
        "And I'm almost relived when we emerge from the ride."
        "Because I know that I've been spared the fate of being drowned."
    $ harmony.love += 2
    $ game.active_date.score += 20
    return

label harmony_date_hedge_maze_male:
    mike.say "Let's do the Hedge Maze next, Harmony..."
    mike.say "What do you say?"
    "Harmony looks less than impressed at my suggestion."
    "She crosses her arms and shakes her head."
    harmony.say "Urgh..."
    harmony.say "Do we have to?"
    harmony.say "That sounds so boring!"
    "Normally I'd be willing to listen to what Harmony has to say."
    "But today I'm determined to prove to her how fun this place is."
    "Plus I've just spotted that the line for the maze is pretty short too."
    mike.say "Don't be silly, Harmony..."
    mike.say "I'm sure you'll love the maze."
    "Without giving Harmony a chance to protest, I walk over to the maze."
    "And once I join the queue, she seems to realise that I'm serious."
    "Because she grudgingly walks over to join me standing in the queue."
    "Once we're inside, I do everything in my power to make it fun."
    "I try hard to memorise our route, getting Harmony involved too."
    "But it's no good, as she pouts the entire way round the maze."
    "And by the time we find our way out, Harmony's in a foul mood."
    "I mean, if a little thundercloud actually appeared above her head, I wouldn't be surprised!"
    $ harmony.love -= 0
    $ game.active_date.score -= 0
    return


label harmony_date_amusement_ice_cream_male:
    mike.say "Phew..."
    mike.say "It's way hotter here than I expected it to be, Harmony."
    mike.say "I don't know if it's the weather or just the number of people!"
    "Harmony nods as she looks around, fanning herself with one hand."
    if harmony.purity >= HP:
        harmony.say "It might be hot, like you say..."
        harmony.say "But that's no excuse for how much flesh some of them are showing off!"
    elif harmony.purity < LP:
        harmony.say "Urgh...I wish I'd worn less, [hero.name]…"
        harmony.say "It's hotter than you in your birthday suit!"
    else:
        harmony.say "You're not wrong, [hero.name]…"
        harmony.say "I feel like I'm melting!"
    "I'm about to say something else."
    "No doubt something smart and witty, as always."
    "When I spot a potential solution to the problem."
    mike.say "Check it out, Harmony..."
    mike.say "There's an ice-cream stall over there."
    mike.say "Let's go grab one, yeah?"
    "Harmony nods eagerly and takes hold of my hand."
    "Then I lead through the thronging crowds to the stand."
    mike.say "Okay, Harmony..."
    mike.say "What do you want?"
    if harmony.purity >= HP:
        harmony.say "A vanilla cone please..."
        harmony.say "With no sprinkles or sauce!"
        "I grimace as Harmony orders the plainest ice-cream possible."
        "But she seems to be pleased with what the server hands over."
        "So I decide not to question her decision."
        $ harmony.love += 2
        $ game.active_date.score += 10
    elif harmony.purity < LP:
        harmony.say "I want one of those bad boys..."
        harmony.say "With all the trimmings too!"
        "My eyes bugle as Harmony orders the largest thing they have."
        "And she insists that the server overload it with sprinkles and sauce too."
        "Then I watch in sheer amazement as she licks away at the teetering tower of ice-cream."
        "And I can't help feeling more than a little turned on by the site too."
        $ harmony.love += 1
        $ game.active_date.score += 20
    else:
        harmony.say "I think we should have one of those, [hero.name]…"
        harmony.say "And then we can share it, yeah?"
        "I nod happily as I order the ice-cream Harmony suggests."
        "Then we walk away together, each holding onto it with one hand."
        "And I enjoy every moment of leaning in close to lick it too."
        $ harmony.love += 1
        $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
