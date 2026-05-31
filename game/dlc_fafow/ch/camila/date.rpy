label camila_date_amusement_park_male:
    scene bg amusement
    show camila annoyed
    with fade
    "I'm always keen to take any chance that I get to visit the Amusement Park."
    "Because it takes me back to being a kid, a time when I had no real worries."
    "So what better place to come when I feel the need to escape and have fun?"
    "And I kind of thought the same thing might be true for Camila."
    "But as we walk up to the gates, I'm already starting to think I made a mistake."
    "Because she doesn't look like she's ready to have fun at all."
    "Instead of being relaxed, Camila seems to be shooting glances at everyone we pass."
    "In fact, she seems to be scrutinising them like she's still on duty!"
    mike.say "Camila..."
    mike.say "Will you quit doing that?"
    "The sound of my voice seems to snap Camila out of it."
    show camila surprised
    "And she turns to look me in the eye, confusion on her face."
    camila.say "Huh?"
    camila.say "Doing what?"
    show camila sad
    mike.say "Looking at everyone like they're potential criminals..."
    mike.say "That's what!"
    show camila weird
    camila.say "I was?"
    camila.say "Urgh..."
    camila.say "Sorry, I've been finding it hard to switch-off lately."
    show camila sad
    mike.say "Well that's why we're here - to switch-off and relax."
    show camila happy
    camila.say "Okay, okay..."
    camila.say "But I can't promise that it'll work."
    mike.say "Just do your best, that's all I ask."
    show camila normal
    return

label camila_date_ferris_wheel_male:
    mike.say "Come on, Camila..."
    mike.say "Let's go on the Ferris Wheel."
    mike.say "Nothing to do on that but sit back and relax."
    "Camila looks the Ferris Wheel up and down."
    "Then she shrugs."
    camila.say "Okay, [hero.name]…"
    camila.say "If you say so."
    "We walk the short distance to the queue for the Ferris Wheel."
    "And though we're right at the back, it seems to move pretty quickly."
    "In what feels like no time at all, we're sitting in one of the gondolas."
    "Camila keeps quiet as the safety-bar comes down and we start to move."
    "But as we go higher, I see her begin getting more interested."
    "She's looking this way and that, taking in the view from up here."
    "And by the time we reach the top, Camila's totally fascinated."
    mike.say "Pretty nice view, huh?"
    "Camila nods as I say this, but she doesn't stop looking out."
    camila.say "You got that right."
    camila.say "Reminds me of the time they took me up in on of the force helicopters."
    camila.say "You can see for miles!"
    "I nod and smile, happy to let Camila keep on enjoying the view."
    "Sure, she somehow managed to turn it around to talking about work."
    "But at least she wasn't trying to spot pick-pockets in the crowd or anything like that."
    $ camila.love += 2
    $ game.active_date.score += 20
    return

label camila_date_merry_go_round_male:
    "As soon as I spot the Merry-Go-Round, I just know that we have to ride it."
    "It's one of the classic Amusement Park rides, one that everyone's been on."
    "So that means it should be something that'll connect for Camila too."
    mike.say "Let's ride the Merry-Go-Round, Camila."
    mike.say "That one over there."
    "Camila doesn't look convinced, but she shrugs and does as I ask."
    "We walk over to join the queue, waiting in line until we reach the front."
    "And then we climb onto the ride, finding a place to sit down."
    camila.say "Hmm..."
    camila.say "This seems okay so far."
    camila.say "I think this might be one that I can handle."
    "Encouraged by Camila's words, I nod in agreement."
    "But as the ride starts to turn, I notice there's something wrong."
    "Camila's hands are holding on so tight they're actually turning white."
    "And her jaw is set so that she looks like she's grinding her teeth."
    mike.say "Camila..."
    mike.say "What's the matter?"
    camila.say "It's the ride..."
    camila.say "The way it's turning..."
    camila.say "It's kinda...freaking me out!"
    "All I can do is hold onto Camila until the ride comes to an end."
    "Then I help her off it and support her as we walk over to a bench."
    "She sits down, putting her head between her knees to recover."
    "Which leaves me to marvel at how strange her reaction was."
    "I mean, who would have thought that would be too much for such a tough cop?"
    $ camila.love -= 2
    $ game.active_date.score -= 20
    return

label camila_date_haunted_house_male:
    mike.say "Oh yeah..."
    mike.say "Now we're talking!"
    "Camila seems to sense the enthusiasm in my voice."
    "And she strains to see what's got me so excited."
    camila.say "What is it, [hero.name]?"
    camila.say "A firing range, or something like that?"
    "I shake my head as I make it to the front of the ride."
    mike.say "Even better..."
    mike.say "It's the Haunted House!"
    mike.say "No excuses this time, Camila - we have to ride this!"
    "Camila holds up her hands to show me she's not going to argue."
    "So we join the queue and wait in line for our turn."
    "All the time I'm getting ever more excited."
    "So much so that I almost run in through the door when we're let in."
    "Camila follows behind me at a more sedate pace."
    "And pretty soon I'm jumping and shrieking at the jump-scares inside."
    "I look back once or twice, to check how Camila's doing."
    "But every time I do so, she looks as nonchalant and calm as ever."
    "Once we're out of the Haunted House, my heart is still pounding."
    mike.say "I don't know how you do it, Camila..."
    mike.say "You walked through there like it was nothing at all!"
    camila.say "Well, remember that I've been on raids of in actual crack houses."
    camila.say "And they're kind of a lot more real when it comes to being scary!"
    $ camila.love += 1
    $ game.active_date.score += 10
    return

label camila_date_love_boat_male:
    show camila flirt
    "I spot the entrance to the Love Boat, and I can't help looking back at Camila."
    "Because I'm already imagining what we could get up to in the privacy of the ride."
    mike.say "How about the Love Boat, Camila?"
    mike.say "You fancy taking a ride on that?"
    "I can see from the look on Camila's face she's onto me."
    "But all the same she doesn't seem to be adverse to the idea."
    camila.say "You sure we need to go on a ride like that, [hero.name]?"
    camila.say "Am I that hard to get your hands on in a dark place?"
    "With that, Camila strides past me and into the ride."
    "Leaving me to hurry after her as she climbs into the boat."
    "Once we're both sitting down, we sail into the dark tunnel."
    show camila kiss
    $ camila.flags.kiss += 1
    "And Camila's true to her word, pulling me close and kissing me."
    "But when I try to subtly explore with my hands, I feel her grab my wrists."
    "Then she whispers in my ear."
    camila.say "Oh no..."
    camila.say "That's all you're getting in here, [hero.name]."
    camila.say "Try that again, and I'll dump you overboard!"
    "I nod, not doubting her sincerity for a moment."
    "And my reward is Camila kissing me with a passion for the rest of the ride."
    "Which is vastly preferable to being tossed into the freezing water instead."
    $ camila.love += 2
    $ game.active_date.score += 20
    return

label camila_date_hedge_maze_male:
    "I see the sign for the Hedge Maze, and I figure that has to be a winner."
    "After all, it's just a load of hedges arranged in a pattern, right?"
    "There are no moving parts, no heights and no jump-scares involved."
    "It's a ride that nobody could have a problem with."
    mike.say "The Hedge Maze, Camila..."
    mike.say "Let's try that out, yeah?"
    "Camila stares at the sign for a moment."
    "Then she gives a quick nod."
    camila.say "Sounds pretty chilled."
    camila.say "I'm up for it."
    "Pleased to have found something Camila likes, I make straight for the queue."
    "And we make swift progress towards the front."
    "After all, this is a smaller, less popular attraction."
    "Once we're inside, I get down to the task of reaching the centre."
    "And then the next one will be finding the way back out again."
    "But almost from the start, Camila doesn't seem comfortable."
    "She keeps looking this way and that, like she's disoriented."
    mike.say "Are you okay, Camila?"
    mike.say "You seem to be a little tense!"
    camila.say "I..."
    camila.say "I don't like this place, [hero.name]."
    camila.say "All of the twisting paths that don't seem to go anywhere..."
    camila.say "They're starting to stress me out!"
    "I can see that Camila's not kidding, so I do the best I can to get her out."
    "This means cutting short my time in the maze, obviously."
    "But she definitely looks like she needs help."
    "I can only guess that she's used to things making sense."
    "To things being rational in her position as a cop."
    "So the maze being deliberately designed to screw with all that..."
    "Well it must have been enough to throw her off pretty badly."
    $ camila.love -= 2
    $ game.active_date.score -= 10
    return

label camila_date_amusement_ice_cream_male:
    mike.say "Erm..."
    mike.say "Camila..."
    mike.say "Can I go get an ice-cream?"
    "Camila turns to look me in the eye as I ask the question."
    "And I can see that she has a puzzled look on her face as she does so."
    camila.say "Huh?"
    camila.say "What kind of a question is that?"
    camila.say "You make it sound like I have something against ice-cream!"
    "I can already feel myself starting to blush as Camila puts me on the spot."
    "And yeah, she's right - it is kind of a dumb question."
    "But there's a reason I'm asking it, even if it's hard to admit."
    mike.say "I...I just thought you might not approve, Camila..."
    mike.say "You know, because you're a big, tough cop?"
    mike.say "Like, maybe being seen eating ice-cream might ruin your image, or something?"
    "Camila raises an eyebrow at this."
    "Then she sniggers and follows it with a burst of laughter."
    camila.say "HA!"
    camila.say "Oh man...I'm with the actual police, [hero.name]..."
    camila.say "Not the fun police!"
    "Before I know what's happening, Camila has a hold of my arm."
    "And then she's dragging me towards the ice-cream stand."
    "Once there she orders us both an ice-cream."
    "Then we stroll away, licking at our frozen treats."
    "And even as she's engrossed in the task, I can still hear Camila chuckling to herself."
    "As well as feeling the burn of my own embarrassment too."
    $ camila.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
