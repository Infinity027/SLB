label samantha_date_amusement_park_male:
    scene bg amusement
    show samantha normal
    with fade
    "Normally I'm pretty excited to be going to the Amusement Park."
    "Yeah, I know it sounds kind of childish, but it's always been that way for me."
    "But today I'm feeling extra stoked to be walking through the gates."
    "And that's on account of the very special person that's holding my hand right now."
    "Part of me knows that I should at least be trying to play it cool."
    "Yet I just can't keep myself from glancing over at Sam."
    "And every time I do so, the smile on my face seems to get wider still."
    show samantha happy
    samantha.say "Hey!"
    samantha.say "Why do you keep doing that?"
    show samantha normal
    "Damn - caught in the act!"
    "Time to start acting innocent."
    mike.say "Huh?"
    mike.say "Doing what, Sam?"
    "Of course, Sam isn't fooled for a second."
    show samantha talkative
    samantha.say "Don't act all dumb!"
    samantha.say "Why are you grinning at me like a fool?"
    samantha.say "Is there a problem with my makeup?"
    samantha.say "Do I have something smeared on my face?"
    samantha.say "What is it?!?"
    show samantha sadsmile
    "All I can do is shrug."
    "That and come clean."
    mike.say "I just can't stop smiling, Sam."
    mike.say "Because I'm so happy to be doing this with you."
    mike.say "But if it's making you feel awkward, then I'll try to stop."
    "I can see that's not the answer Sam was expecting."
    show samantha happy blush
    "And it looks like she's even blushing a little."
    show samantha talkative
    samantha.say "Oh..."
    samantha.say "No, [hero.name]…"
    samantha.say "If that's the reason, then you can keep on smiling at me all you like!"
    show samantha normal
    "I do just that, squeezing Sam's hand extra tight as we walk into the park together."
    return

label samantha_date_ferris_wheel_male:
    mike.say "Since this is our first time here on a date, I want to do all the classic rides."
    mike.say "So let's ride the Ferris Wheel, Sam..."
    mike.say "What do you say?"
    "Much to my relief, Sam nods at this."
    samantha.say "Sounds like a plan, [hero.name]."
    samantha.say "Plus I haven't been on a Ferris Wheel in years."
    "Together we make our way over to where the queue begins."
    "And we're in luck, as the Ferris Wheel seems to be pretty quiet right now."
    "Which means that we make it to the front of the line in no time at all."
    "Sam steps into the gondola and sits down, patting the bench beside her."
    "And I don't hesitate to follow, sliding across to sit as close as possible."
    "The safety bar comes down and then the ride begins to move."
    "Slowly we climb into the air, taking in the view as we go ever higher."
    "The ride stops for a moment once we reach the top of the wheel."
    "Where Sam and I are treated to an impressive view of the city."
    mike.say "Wow..."
    mike.say "That's quite something!"
    samantha.say "You're right, [hero.name]…"
    samantha.say "We must be able to see for miles up here!"
    mike.say "I think I can see the house over there."
    samantha.say "No way!"
    samantha.say "Point it out to me?"
    "Sam and I spend the rest of the ride trying to spot places we both know."
    "But all too soon the ride begins to move again, and we're returned to the ground."
    $ samantha.love += 1
    $ game.active_date.score += 10
    return

label samantha_date_merry_go_round_male:
    samantha.say "I bet you want to ride the Merry-Go-Round..."
    samantha.say "Don't you, [hero.name]?"
    mike.say "I do?"
    samantha.say "Don't be shy!"
    samantha.say "I wont' judge you, I promise."
    "I look at the ride, and then back at Sam."
    "Because this is the first that I've heard about riding the Merry-Go-Round."
    "And I'm about to flatly deny the idea that I want to get on the thing."
    "But then it strikes me that this would be the perfect way to get Sam on it."
    "So I decide to play along."
    mike.say "Ah..."
    mike.say "You got me, Sam!"
    "Sam smiles and claps her hands as we walk towards the ride."
    samantha.say "I knew it!"
    samantha.say "Oh, [hero.name]…"
    samantha.say "I can read you like a book!"
    "The line for the Merry-Go-Round is a short one."
    "And that means we're soon climbing on and picking our spots."
    "I'm not feeling it at first, fidgeting awkwardly in my seat."
    "But as the ride begins to pick up speed, I feel myself getting into it."
    "Perhaps that has a lot to do with the fact that Sam's enjoying herself too."
    "The looks that we exchange while the ride's in motion tell me as much."
    "So I'm more than happy to play along for the sake of making her happy."
    $ samantha.love += 1
    $ game.active_date.score += 10
    return

label samantha_date_haunted_house_male:
    mike.say "We have to do the Haunted House, Sam..."
    mike.say "No trip to the Amusement Park is complete without that!"
    "Sam follows me as I make for the back of the queue."
    "But I can sense that she's not sharing my enthusiasm."
    samantha.say "I don't know..."
    samantha.say "It looks pretty scary!"
    "I can't help laughing and shaking my head at this."
    mike.say "Of course it looks scary!"
    mike.say "What would the point be if it wasn't scary?"
    mike.say "Come on, Sam - you'll love it, I promise."
    "Sam still doesn't look convinced."
    "But she joins the line beside me all the same."
    "And I make sure to hold her hand as we move up the queue."
    "Once we step into the Haunted House itself, I take a deep breath."
    "Because I know that I made a big promise to Sam in order to get her in here."
    mike.say "Okay, Sam..."
    mike.say "Take a deep breath and try to stay calm."
    mike.say "Remember that none of this is real, yeah?"
    mike.say "It's all puppets and special effects..."
    samantha.say "AAARGH!"
    samantha.say "Oh god, oh god, oh god..."
    samantha.say "What the fuck is that?!?"
    "Sam begins to jump and scream almost as soon as the first scare hits us."
    "And she only seems to become more terrified as we go deeper into the Haunted House."
    "By the time we make it out of the place, I can feel that she's actually shaking."
    "And I make a vow to listen to her the next time she wants to skip a ride."
    $ samantha.love -= 2
    $ game.active_date.score -= 20
    return

label samantha_date_love_boat_male:
    "I catch Sam staring at the Love Boat ride, like she's totally absorbed by it."
    "And I even have to wave a hand in front of her face to get her attention."
    mike.say "Hey!"
    mike.say "Earth to Sam!"
    mike.say "You want to take a ride on the Love Boat?"
    "Sam seems to be embarrassed that I caught her looking a the ride."
    "But she quickly recovers her composure, shaking her head and laughing."
    samantha.say "What?"
    samantha.say "Ride that thing?"
    samantha.say "We don't have to do that, [hero.name]…"
    samantha.say "You'd probably find it way too boring!"
    mike.say "No way, Sam!"
    mike.say "Come on, let's go join the queue."
    "Sam's blushing openly as we do just that."
    "And it takes her the time were waiting for the ride for her cheeks to fade."
    "But I note that she's smiling as we step into the waiting boat together."
    "And what follows is pretty much what you would expect."
    "She doesn't pounce on me the moment we're shrouded in the darkness."
    show samantha kiss
    $ samantha.flags.kiss += 1
    "Instead we share a long and gentle kiss while in each other's arms."
    "And when we emerge from the other end of the tunnel, Sam's smiling even more."
    $ samantha.love += 2
    $ game.active_date.score += 20
    return

label samantha_date_hedge_maze_male:
    samantha.say "Huh..."
    samantha.say "They have a Hedge Maze here?"
    samantha.say "I thought those were something they had at fancy country houses?"
    "I shake my head as I follow Sam's gaze."
    mike.say "Oh no, Sam..."
    mike.say "They've always had one here, as long as I can remember."
    mike.say "You want to check it out?"
    "Sam kind of shrugs and only half nods her head."
    "But that's enough of a yes for me."
    "We walk over and join the queue for the maze."
    "Which seems to be very short for an attraction in the park."
    "And soon enough we're walking into the maze itself."
    mike.say "Stay close by me while we're in here, Sam."
    mike.say "You wouldn't want to get lost!"
    samantha.say "Erm..."
    samantha.say "Isn't that the entire point of a maze?"
    mike.say "Oh..."
    mike.say "Yeah..."
    mike.say "Good point, Sam - let's get lost!"
    "We spend a good amount of time wandering around inside the maze."
    "And I have to admit that it's a lot more challenging that I expected it to be."
    "I doubt that I'd have found my way out as easily without Sam being there."
    "Though I make sure not to make that fact too obvious to her."
    $ samantha.love += 1
    $ game.active_date.score += 10
    return

label samantha_date_amusement_ice_cream_male:
    samantha.say "Oh, [hero.name]…"
    samantha.say "It's so hot today!"
    samantha.say "I starting to wish we'd gone somewhere cooler, you know?"
    "I'm looking straight at Sam all the time she's saying this."
    "And I know that the words are making sense to me as well."
    "But there's still some part of me that can't bring myself to respond."
    "Because she's wiping the light perspiration from her forehead with the back of her hand."
    "And at the same time she's smiling at me in a way that makes me hotter than the heat of the sun!"
    samantha.say "[hero.name]?"
    samantha.say "Are you even listening to me right now?"
    mike.say "Oh..."
    mike.say "Oh yeah, Sam..."
    mike.say "Sorry about that!"
    "Tearing my eyes away from Sam for a moment, I search around for a solution."
    "And I almost say a literal thank you to the universe when I see an ice-cream stand."
    mike.say "Ice-cream!"
    mike.say "We should get an ice-cream!"
    "Much to my relief, Sam smiles at my suggestion."
    "And she seems to forget all about being annoyed with me too."
    "Because she holds out her hand for me to take."
    "Then lets me lead her the short distance to the ice-cream stand."
    "Once we're there, I buy us one each, and we walk off liking them."
    "So I can finally go back to staring at Sam in an adoring manner."
    "Feeling like I'm living in a dream, as I'm finally getting to do stuff like this with her."
    $ samantha.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
