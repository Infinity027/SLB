label lavish_date_amusement_park_male:
    scene bg amusement
    show lavish
    with fade
    "As usual, I'm feeling pretty high and energised as we walk towards the gate."
    "But then the chance to go to the Amusement Park always makes me feel like that."
    "I just can't wait to get in there and start hitting the rides that I love."
    "Though my date doesn't seem to have the same levels of energy and enthusiasm."
    "But that's not to say Lavish is hanging back or showing a reluctance to go in there."
    "In fact she's grinning at me the whole time, rolling her eyes at my eagerness."
    show lavish happy
    lavish.say "Are you always like this when you come here, [hero.name]?"
    show lavish normal
    mike.say "Like what, Lavish?"
    mike.say "I don't know what you mean!"
    show lavish happy
    lavish.say "Oh yes you do!"
    lavish.say "You're like a kid on a sugar-rush right now!"
    show lavish normal
    "All I can do is shrug helplessly, because I can't deny it."
    mike.say "What can I say?"
    mike.say "This is one of my favourite places in the entire world."
    mike.say "Somewhere I can just kick back and have pure, unadulterated fun."
    mike.say "And there's not going to be anyone telling me to act my age!"
    show lavish happy
    "Lavish giggles and shakes her head."
    lavish.say "Looks to me like you want to act the age of a little kid!"
    lavish.say "Just remember that we're really both adults, okay?"
    lavish.say "I'm your girlfriend, not your mommy!"
    return

label lavish_date_ferris_wheel_male:
    lavish.say "Oh, look, [hero.name]…"
    lavish.say "They have a Ferris Wheel."
    lavish.say "And it's one of the old kind - like, a classic!"
    "I look up to see the ride that Lavish is pointing to."
    "And the moment I do so, I feel a pang of disappointment."
    "I'd been hoping to be able to hit some of the more modern rides."
    "Or at least some of the more exciting ones."
    "But that thing looks like I could fall asleep on it!"
    mike.say "Lavish..."
    mike.say "Are you..."
    "I don't even get to finish what I was going to say before it happens."
    "Lavish turns and looks me in the eye, hitting me with those big browns she has."
    "It's like a puppy pleading for something it wants, but worse, because she's so hot!"
    "And before I know what I'm doing, the words are spilling out of my mouth."
    mike.say "Of course, Lavish..."
    mike.say "Whatever you want!"
    "Lavish smiles and takes hold of my hand, leading me to the start of the queue."
    "And then we stand patiently in line until our turn to ride the Ferris Wheel comes round."
    "As the safety-bar comes down and we rise into the air, I'm beginning to get into it."
    "Lavish is still holding my hand, and she's positively beaming with happiness."
    "So it's impossible for that not to start rubbing off on me too."
    "When the wheel stops with us at the top, she leans her head on my shoulder."
    "And she lets out a sigh of pure satisfaction."
    lavish.say "Ah..."
    lavish.say "This is perfect, just perfect."
    "Then she turns to place her lips against mine, kissing me gently."
    "I return the gesture, finally feeling glad that we chose to ride the Ferris Wheel."
    "But all too soon I feel the sensation of the ride starting to move again."
    "And I know that we'll soon have to bring the kiss to an end."
    $ lavish.love += 2
    $ game.active_date.score += 20
    return

label lavish_date_merry_go_round_male:
    "I spot the Merry-Go-Round up ahead, and I almost disregard it in favour of something else."
    "After all, it's not a very exciting ride and it's as old as they get."
    "But then I remember that I'm not just here to indulge myself today."
    "I should really be thinking of Lavish as well."
    "And maybe a more sedate kind of ride is more her kind of thing?"
    mike.say "What about the Merry-Go-Round, Lavish?"
    mike.say "You want to take a ride on that?"
    "Lavish looks over at the ride in question."
    "And then she gives me a shrug of her shoulders."
    lavish.say "I guess so."
    lavish.say "If that's what you want."
    "I'm about to say that it's not, but then I remember that I'm not talking to a guy."
    "And I've often found that girls say the opposite of what they actually want."
    "So that must mean Lavish really does want to ride the Merry-Go-Round, right?"
    "I give her a knowing smile, and start walking towards the ride."
    mike.say "Sure, Lavish..."
    mike.say "I want to ride the Merry-Go-Round."
    "With that, we walk over to the queue for the ride and join it."
    "The line isn't long, as it's a less popular attraction."
    "So it's not long before we make it to the front."
    "Lavish and I choose where we want to sit, then we wait for the ride to start."
    "Once it does, I keep glancing over at Lavish, expecting to see her enjoying herself."
    "But every time I do so, she seems to be bored out of her skull!"
    "That makes the length of the ride feel like it's stretching on forever."
    "And even when we get off the thing, it still feels pretty awkward."
    "So maybe I was wrong."
    "Maybe women to sometimes mean exactly what they say!"
    $ lavish.love -= 2
    $ game.active_date.score -= 20
    return

label lavish_date_haunted_house_male:
    "As soon as I see the Haunted House, I make straight for it."
    "Elbowing my way through the crowds, I walk right up to the start of the queue."
    "So the first time Lavish has the chance to say anything about it is then."
    "Right when we're in line for the attraction and inching our way to the entrance."
    lavish.say "Okay..."
    lavish.say "So I take it you want to go in the Haunted House?"
    "I let out a nervous laugh."
    "Because I'm only now becoming aware of just how rude that was of me."
    mike.say "Ah..."
    mike.say "Yeah..."
    mike.say "Sorry, Lavish!"
    mike.say "This is kind of a favourite of mine."
    "Lavish nods, like she's saying that she gets me."
    "But she also keeps the expression on her face as one that says she doesn't share my enthusiasm."
    lavish.say "Well in that case we should definitely go in there."
    lavish.say "But just the once, okay?"
    "I nod at this, eager to accept any condition that lets me go inside."
    "And all the time we're waiting, I'm hoping Lavish will change her opinion."
    "That what she sees in there will make her love it as much as I do."
    "Once we reach the front of the queue, we can finally step into the Haunted House."
    "So I take hold of Lavish's hand and prepare to be scared silly."
    "Which is just what happens, as I enjoy the jump-scares, special effects and cheesy décor."
    "Lavish follows along at my side, experiencing all of this at the same time."
    "But I don't hear her scream or feel my hand being squeezed even once."
    show lavish bored
    "And when we walk out the other end, she has a certain look on her face."
    "One that reminds me she's indulging my vices."
    "That and how I'm not allowed to ask her to do it over again."
    $ lavish.love -= 1
    $ game.active_date.score -= 10
    return

label lavish_date_love_boat_male:
    "The Love Boat - now there's a ride with a promising name!"
    "I bet Lavish and I could have some serious fun in there."
    "So I don't hesitate to suggest as much to her."
    mike.say "We have to ride the Love Boat, Lavish!"
    mike.say "Are we really on a date here if we don't?"
    "Lavish rolls her eyes and shakes her head."
    "And the look that she gives me at the same time is very knowing."
    "But I do note that she doesn't shoot the idea straight down."
    lavish.say "The Love Boat, huh?"
    lavish.say "Now I wonder why you could want to go on that?"
    "Lavish keeps in chuckling to herself as we walk over and stand in line."
    "And it doesn't take us long to get to the front of the queue either."
    "So she's still laughing as we step into a boat and sail away."
    "Part of me is thinking that she's going to keep to her side of the boat."
    "That she won't do any of the stuff I'm expecting to torture me."
    "So it comes as a serious relief when she slides over next to me."
    "And the intimacy that follows is more of the same."
    "It's nothing wanton or crazy, mind you."
    show lavish kiss
    $ lavish.flags.kiss += 1
    "Just a chance to embrace and share a genuine kiss."
    "But it more than makes up for all that I've had to go through to get it."
    "And once we sail out the other end of the tunnel, I feel much better."
    $ lavish.love += 2
    $ game.active_date.score += 20
    return

label lavish_date_hedge_maze_male:
    mike.say "Let's do the Hedge Maze, Lavish..."
    mike.say "Put our brains to the test, yeah?"
    "Lavish doesn't look sold on the idea."
    "I mean, she doesn't openly say no."
    "But she looks less than enthusiastic."
    lavish.say "Really?"
    lavish.say "A maze made out of hedges?"
    mike.say "Give it a chance, okay."
    mike.say "It might be the best thing in the park!"
    "Before Lavish can tell me that it might not too, I hurry over to the maze."
    "This means that she has to follow close on my heels."
    "And by the time she catches up to me, I'm already in the queue."
    "Lavish seems to accept that this means we're going into the maze."
    "So she keeps quiet until it's our turn to walk through the entrance."
    "But once we're in there, it soon becomes clear she's not happy."
    lavish.say "Urgh..."
    lavish.say "Everything looks the same in here!"
    lavish.say "It's bad enough being lost for the sake of it."
    lavish.say "But does it have to be so boring as well?"
    "I'm doing the best I can to ignore Lavish's constant complaints."
    "Because at the same time I'm also trying to find my way out of here."
    "In the end I think I'm going to go mad before I succeed."
    "Yet somehow I manage to do it and lead us out of the exit."
    "Thankfully Lavish seems to cheer up once we're out."
    "And she stops complaining too."
    "While I make a mental note never to take her into a maze again."
    $ lavish.love -= 2
    $ game.active_date.score -= 20
    return

label lavish_date_amusement_ice_cream_male:
    mike.say "Phew..."
    mike.say "I'm feeling pretty hot, Lavish..."
    mike.say "You want to grab an ice-cream?"
    "Lavish looks in the direction of the ice-cream stand."
    "And it doesn't take a mind-reader to see that she's not impressed."
    lavish.say "Hmm..."
    lavish.say "The line looks really long from here."
    lavish.say "All those sweaty bodies too - urgh!"
    mike.say "Okay, so that's a no."
    mike.say "But you mind if I go get one for myself?"
    "Lavish shrugs her shoulders, which I take as permission."
    "So I hurry off to join the queue, already looking at the menu."
    "The queue seems too move far faster than either of us expected."
    "Which means that it's no time at all until I get my ice-cream."
    "And I walk back over to Lavish, already licking at it."
    lavish.say "Hey!"
    lavish.say "That was quick..."
    lavish.say "Oh man, now I wish I'd gotten one too!"
    "Without hesitation, I hold out my ice-cream to Lavish."
    mike.say "I don't mind sharing, Lavish..."
    mike.say "Not if you don't?"
    "The smile that spreads across Lavish's face is pretty amazing."
    "And I can't help smiling back at her as she leans in for a lick."
    "Then we walk away, arm in arm and sharing the ice-cream together."
    $ lavish.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
