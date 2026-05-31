label bree_date_amusement_park_male:
    scene bg amusement
    show bree smile
    with fade
    "I'm always pretty excited when I get the chance to go to the Amusement Park."
    "I suppose you could say that it brings out the little kid inside of me."
    "And normally I have to contend with how the person I'm going with reacts to that."
    "At the best they'll be amused by how excited I'm getting, while tempering their own reactions."
    "But sometimes you have to deal with someone that gets all grumpy and resentful."
    show bree happy
    "Though on a very rare occasion, I meet my match in terms of excitement."
    show bree talkative
    bree.say "Come on, [hero.name]…"
    bree.say "What are you waiting for?!?"
    show bree smile
    "And yeah, you guessed it - [bree.name]'s one of those rare cases!"
    "It's all that I can do to even keep up to her as she charges towards the entrance."
    "And when she has hold of my hand, she's dragging me after her without mercy."
    "I mean, I understand the desire to get in there and onto the best rides."
    show bree happy
    "But [bree.name]'s even starting to make me wonder if there's such a thing as too much enthusiasm."
    show bree normal
    mike.say "Whoa..."
    mike.say "Calm down, [bree.name]!"
    mike.say "I'm coming as fast as I can - I swear it!"
    show bree talkative
    bree.say "Well your fastest just isn't fast enough!"
    bree.say "You'd better move your ass!"
    return

label bree_date_ferris_wheel_male:
    bree.say "Look, [hero.name]…"
    bree.say "A Ferris Wheel!"
    bree.say "That's such a classic ride!"
    "I look up at the Ferris Wheel as [bree.name] points it out."
    "Squinting to see the people at the very top."
    mike.say "What do you think, [bree.name]?"
    mike.say "You want to ride it?"
    "[bree.name] gives me a nod."
    "And together we hurry to the queue and stand in line."
    "Luckily for us, the ride seems to have a fast turn-over."
    "And so we're soon getting into one of the gondolas."
    "As soon as the safety bar comes down, [bree.name] scoots over to me."
    "And we get nice and close as we begin to climb into the air."
    "At first, [bree.name] seems to be very into the ride."
    "She gazes over the edge of the gondola, taking everything in."
    "Then she turns her attention to the view that's rising into sight."
    "But by the time we get to the top of the wheel, she seems to lose interest."
    "She even sits back in her seat, staring at her feet."
    mike.say "What's up, [bree.name]?"
    mike.say "Are you not liking the height we're at?"
    "[bree.name] looks up at me and shakes her head."
    bree.say "Nah, it's not that."
    bree.say "It's just that once you're up here..."
    bree.say "Well, that's all there is to it."
    bree.say "The ride back down is kind of a let-down!"
    mike.say "Yeah..."
    mike.say "I can't argue with that."
    mike.say "Kind of makes you aware of why they came up with stuff like roller-coasters!"
    $ bree.love -= 0
    $ game.active_date.score -= 0
    return

label bree_date_merry_go_round_male:
    mike.say "They have an old-fashioned Merry-Go-Round."
    mike.say "Like something you'd see in an old film, yeah?"
    bree.say "We should ride it, just for the sake of it."
    bree.say "You know, see what rides were like back in the day?"
    "I nod in agreement, and together we walk over to the queue for the ride."
    "[bree.name] and I don't have to wait in line long before we're at the front."
    "Then we climb onto the Merry-Go-Round and find a place to sit."
    "We wait in silence for the thing to start up."
    "Then we find ourselves going round in a circle."
    "And that's kind of the problem - nothing else happens."
    "Sure, the ride gets a little bit faster."
    "But that's it, and it's still really slow by modern standards."
    "[bree.name] looks over at me and we exchange a meaningful glance."
    "There's really no need for either of us to actually say a word."
    "We both know that it's not going to get any more exciting than this."
    "So from that point on the ride turns into us merely waiting to get off."
    "And when it finally comes to a halt, we jump down in silence."
    "Then we walk away in the same manner too."
    "And I'm pretty sure that [bree.name]'s thinking the same thing as me."
    "That we need to get on something faster and more thrilling."
    "Before the pair of us end up falling into a coma from sheer boredom!"
    $ bree.love += 0
    $ game.active_date.score += 0
    return

label bree_date_haunted_house_male:
    show bree happy
    "As soon as [bree.name] sees and hears the Haunted House, she makes straight for it."
    "And I have to push my way through the crowd to keep up with her as she does so."
    "By the time I manage to make it, she's already joined the queue for the ride."
    mike.say "Phew..."
    mike.say "Slow down a little, [bree.name]!"
    mike.say "You almost left me behind back there."
    bree.say "Sorry, [hero.name]..."
    bree.say "I just saw this thing and knew I had to get in there!"
    "I can't help raising my eyebrows."
    "A little surprised by [bree.name]'s enthusiasm."
    mike.say "I love these kind of things, [bree.name]."
    mike.say "But I thought they'd be a bit, I dunno..."
    mike.say "Old-fashioned for you?"
    "[bree.name] smiles and shakes her head as we reach the head of the queue."
    "And she explains herself as we walk into the Haunted House itself."
    bree.say "I'm used to modern survival horror games."
    bree.say "This is pretty tame in comparison!"
    "I nod, happy to accept [bree.name]'s explanation."
    "That is until we get to one of the first serious jump-scares."
    mike.say "Whoa!"
    mike.say "Fuck me!"
    bree.say "AARGH!"
    bree.say "OH GOD..."
    bree.say "Get me out of here!"
    "[bree.name] leaps at me and wraps herself around my arm as she says this."
    "And then she starts to hustle me forwards before I can protest."
    "In this way I end up being half dragged out of the place and half trying to escape myself."
    "But of course this means that we blunder into every scare between us and the exit."
    "And each one sees [bree.name] squealing and panicking anew."
    "Once we're finally out of there, she still won't let go of my arm."
    mike.say "Erm, [bree.name]..."
    mike.say "You're safe now."
    mike.say "You want to let me go?"
    "[bree.name] shakes her head and clings to me tighter still."
    "So I decide to leave her where she is for the time being."
    $ bree.love -= 2
    $ game.active_date.score -= 20
    return

label bree_date_love_boat_male:
    "I see the sign for the Love Boat ride, and I begin to steer us towards it."
    "But it's not like I can fool [bree.name] for very long, and she's soon onto me."
    bree.say "Oh look, the Love Boat."
    bree.say "What a coincidence!"
    "I hold up my hands, surrendering to her without protest."
    mike.say "Okay, [bree.name]..."
    mike.say "You got me!"
    mike.say "But seriously, you want to take a ride on this?"
    mike.say "It could be fun."
    "[bree.name] smiles and shakes her head."
    bree.say "It could also be a chance for you to misbehave!"
    bree.say "I'll go on it with you, [hero.name]."
    bree.say "So long as you promise to be a good boy?"
    "I nod in agreement, happy to accept [bree.name]'s conditions."
    "Because it actually means we're going on the ride."
    "And I'm sure that I can be charming enough to change her mind."
    "Once we're in the boat and sailing towards the darkness, I make my move."
    show bree kiss
    $ bree.flags.kiss += 1
    "[bree.name]'s receptive to a little innocent kissing and cuddling."
    "But when I do try to push my luck, I get a short, sharp slap for my troubles."
    "Not wanting to earn another one, I make sure to keep things safe after that."
    hide bree
    show bree happy
    "Though when we get off the ride, I can still feel where [bree.name] slapped me."
    "And the knowing smile on her face tells me that she knows it too."
    $ bree.love += 1
    $ game.active_date.score += 10
    return

label bree_date_hedge_maze_male:
    "As soon as [bree.name] sees the sign for the Hedge Maze, she looks intrigued."
    "Which seems odd to me, as it's not the kind of thing I'd imagine her being into."
    "I mean, it's just a bunch of hedges that serve as walls."
    "She always struck me as being into more complicated, modern stuff."
    mike.say "You really want to do that one, [bree.name]?"
    mike.say "It's just a maze made out of hedges!"
    "[bree.name] shakes her head at this."
    bree.say "I don't think so, [hero.name]."
    bree.say "I think it's more like an old-fashioned escape-room."
    bree.say "You know what I mean?"
    "I can kind of see what [bree.name]'s getting at."
    "So I nod."
    mike.say "Yeah..."
    mike.say "Kind of, I guess."
    "[bree.name] and I join the queue for the maze, and pretty soon we're inside."
    "But to me it still looks like a lot of plants packed really close together."
    "I turn to [bree.name], meaning to say as much to her."
    "But I just have time to see her darting off around a corner."
    mike.say "H...hey!"
    mike.say "Wait for me!"
    "There's no time for me to even think about what I'm doing."
    "All I know is that I don't want to get lost in the maze."
    "So I hurry after [bree.name], doing the best I can to keep right on her heels."
    "Which is easier said than done, as she twists and turns as much as the maze!"
    "[bree.name] looks this way and that as she goes, clearly enjoying herself."
    "And once she finds the exit, she actually jumps up and punches the air."
    bree.say "Yeah!"
    bree.say "I did it - I found my way out!"
    mike.say "Y...yeah..."
    mike.say "Great..."
    mike.say "Just...just let me...catch my breath!"
    $ bree.love += 2
    $ game.active_date.score += 20
    return

label bree_date_amusement_ice_cream_male:
    mike.say "Hey, [bree.name]..."
    mike.say "I'm feeling pretty hot!"
    mike.say "You want to grab an ice-cream?"
    "Much to my surprise, [bree.name] shakes her head at the question."
    bree.say "No way, [hero.name]!"
    bree.say "I'm having too much fun to stop now."
    bree.say "And it's not like I can take an ice-cream on the rides with me, is it?"
    "I shrug my shoulders as I walk over to the queue for the ice-cream stand."
    mike.say "I don't know about that, [bree.name]..."
    mike.say "The lines are getting pretty long."
    mike.say "I reckon I could eat one before we get on the next ride."
    "[bree.name] gives me a defiant look and points to a nearby ride."
    bree.say "Okay, [hero.name], you're on."
    bree.say "You queue for the ice-cream and I'll queue for the ride."
    bree.say "And I bet I'm on there before you're done eating it."
    "With that, [bree.name] turns on her heel and hurries off to the ride in question."
    "Which leaves me to do the same at the ice-cream stand."
    "I'm not too concerned about winning the bet, because I want the ice-cream anyway."
    "But all the same I keep on looking over my shoulder to see how [bree.name]'s doing."
    "At first she seems confident, but that changes as I get to the front of the queue."
    "And by the time I stroll over to her with my ice-cream, she's nowhere near the front."
    mike.say "Hey, [bree.name] - still in line, huh?"
    mike.say "Phew...you look hot!"
    mike.say "If only you had a delicious, frozen treat to cool you down."
    "I take a long lick of my ice-cream, enjoying the frustration on [bree.name]'s face."
    "And it doesn't take long for her to break either."
    bree.say "Urgh..."
    bree.say "You swine..."
    bree.say "Gimmie that thing, right now!"
    "I can't help smiling as [bree.name] grabs the ice-cream and licks at it furiously."
    "And sacrificing half of it to be proven right feels like an acceptable sacrifice."
    $ bree.love += 0
    $ game.active_date.score += 0
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
