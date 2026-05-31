label audrey_date_amusement_park_male:
    scene bg amusement
    show audrey annoyed
    with fade
    "I thought that coming to the Amusement Park with Audrey would be a sure-fire hit."
    "Because everyone likes to spend time in a place like that, right?"
    "Well, apparently everyone except Audrey!"
    audrey.say "Urgh..."
    show audrey whining
    audrey.say "What possessed you to want to come here, [hero.name]?"
    show audrey annoyed
    mike.say "It's fun, Audrey."
    mike.say "Don't you have great memories of places like this?"
    show audrey talkative
    audrey.say "Of course I do."
    show audrey joke
    audrey.say "But they're all from back when I was a kid."
    audrey.say "I've grown up since then!"
    show audrey sadsmile
    "I make a gargantuan effort to ignore how negative Audrey's being right now."
    "All in the hope that she'll change her tune once we're inside and on the rides."
    mike.say "Come on, Audrey..."
    mike.say "At least give it a chance."
    mike.say "Who knows, you might actually find that you like it."
    show audrey normal
    "Audrey fixes me with a singularly unimpressed look."
    "But then she shakes her head and rolls her eyes."
    show audrey talkative
    audrey.say "Okay, okay..."
    audrey.say "I'll do the best I can."
    show audrey joke
    audrey.say "But I get to pick where we go next time."
    return

label audrey_date_ferris_wheel_male:
    mike.say "Let's ride the Ferris Wheel, Audrey."
    mike.say "It's a classic, right?"
    mike.say "The perfect way get into the spirit of the Amusement Park?"
    "Audrey looks up at the Ferris Wheel towering over us."
    "And she seems to be less than impressed by the sight."
    audrey.say "You're seriously into going on that thing?"
    audrey.say "It's just a big wheel that goes round and round!"
    "But even while she's saying all of this, I'm steering us into the queue."
    "And it doesn't take long for us to be seated in one of the gondolas."
    "I do the best I can to keep a smile on my face and show enthusiasm."
    "Even while Audrey spends the same time looking surly and bored."
    "By the time we reach the top, the view really is impressive."
    "And when the ride stops for a moment, I try to big it up."
    mike.say "Check out that view, Audrey!"
    mike.say "Doesn't that make it worth the ride?"
    audrey.say "It's just a view, [hero.name]."
    audrey.say "It's not like they're hard to find."
    audrey.say "All you have to do is climb a hill or a tall building to see one."
    audrey.say "Plus you don't have to pay some greasy guy money for the privilege!"
    $ audrey.love -= 0
    $ game.active_date.score -= 0
    return

label audrey_date_merry_go_round_male:
    "I figure that Audrey's probably no going to be impressed by the big, fancy rides."
    "But maybe the smaller and more charming variety could capture her interest?"
    "So when I catch her glancing sideways at the Merry-Go-Round, I see my chance."
    mike.say "Shall we ride this one, Audrey?"
    mike.say "The queue's not too long."
    "Audrey turns to look at me with surprise on her face."
    "Like she's embarrassed to have been caught showing interest in the ride."
    "But she seems to decide that it's less awkward to admit it than deny it."
    audrey.say "I suppose so, [hero.name]."
    audrey.say "If that's what you want..."
    "I don't wait for a second before leading Audrey over to the ride."
    "And as the queue is so short, we're on it in no time at all."
    "I make sure to hold on tight as the Merry-Go-Round starts to move."
    "But I can't help stealing the occasional glance in Audrey's direction."
    "And I soon see her starting to loosen up and actually enjoy the ride."
    "By the time it's over and we're getting off, she even has a smile on her face!"
    mike.say "Looks like someone's starting to have a good time!"
    audrey.say "Alright, [hero.name]..."
    audrey.say "That wasn't too bad, I admit it."
    audrey.say "But keep that to yourself."
    audrey.say "Because if you tell a soul, I'll deny everything!"
    $ audrey.love += 4
    $ game.active_date.score += 30
    return

label audrey_date_haunted_house_male:
    "As we round a corner, I hear the sounds of moaning, screaming and creepy music."
    "And as a veteran of Amusement Parks, I know that can only mean one thing."
    "Sure enough, a moment later I see the Haunted House looming above us."
    mike.say "Oh wow!"
    mike.say "The Haunted House!"
    mike.say "This is one of my absolute favourites, Audrey!"
    audrey.say "Let me guess..."
    audrey.say "That means we absolutely have to go in there, right?"
    audrey.say "Otherwise your inner child will die of neglect?"
    mike.say "Erm..."
    mike.say "Something like that, Audrey!"
    "I don't give Audrey another chance to piss all over what we're doing."
    "Instead I take hold of her hand and lead us towards the entrance."
    "Once we're inside, I'm instantly transported to a world of creepy wonder."
    "There's a scare waiting to greet us around every corner in there."
    "And the fact that they're almost all cheesy and predictable doesn't matter."
    "Well, at least it doesn't matter to me."
    "Audrey looks more like a kid being dragged around a museum by her parents."
    "And I don't think I see her jump or let out a shriek of fright even once."
    "When we walk out of the exit, she's still looking bored and irritated."
    "Which kind of takes the shine off the experience for me too."
    $ audrey.love -= 2
    $ game.active_date.score -= 10
    return

label audrey_date_love_boat_male:
    mike.say "Let's take a ride on the Love Boat, Audrey."
    mike.say "It's relaxing and romantic - plus the queue's always short!"
    "Audrey lets out a snort of derision at the idea."
    audrey.say "Ha!"
    audrey.say "That's because the groping grotto's so lame!"
    "I do the best I can not to let Audrey's negativity rub off on me."
    "And I keep on steering us towards the ride at the same time."
    mike.say "At least give it a try."
    mike.say "Then you can say it sucks from personal experience."
    "Audrey lets me have my way."
    "Allowing herself to be seated in a boat, sits back and stays quiet."
    "But I note that she also crosses her arms over her chest and frowns."
    "Which means this might be the least romantic voyage on the Love Boat imaginable!"
    "The whole time we're on the ride, Audrey keeps up her silent vigil."
    "And more than once she gives me a withering stare when I try to sneak closer."
    "Each time I end up sliding back to my side of the boat."
    "And each time I feel just a little more deflated at the effort."
    "Once we get out at the other end, Audrey nods her head."
    audrey.say "Yup, I was right..."
    audrey.say "That was a total wastes of time."
    audrey.say "It wasn't romantic at all!"
    mike.say "Yeah, Audrey..."
    mike.say "I can't imagine why that would be..."
    $ audrey.love -= 2
    $ game.active_date.score -= 10
    return

label audrey_date_hedge_maze_male:
    "I see the queue for the Hedge Maze is smaller than the ones for the bigger rides."
    "And I figure that we could do a trip around the maze for the sake of killing time."
    "Just as a temporary distraction while we wait for the other rides to be less busy."
    mike.say "I say we do the Hedge Maze, Audrey."
    mike.say "It's pretty chill, you know?"
    mike.say "And a change of pace might do us good."
    "Of course, Audrey looks less than convinced."
    audrey.say "I keep telling you, [hero.name]..."
    audrey.say "These rides are quiet because they suck!"
    audrey.say "But if that's what you want, then go ahead."
    "I take Audrey at her word, leading the way into the maze."
    "And a moment later we're surrounded by high hedges."
    "I plunge into the maze, doing the best I can to figure out the way."
    "But it doesn't take long for me to find that I'm totally lost."
    mike.say "Ah..."
    mike.say "This is harder than it looks!"
    mike.say "I don't think I can find the way out of here."
    audrey.say "Great work, [hero.name]."
    audrey.say "First you make me come in here."
    audrey.say "Now you tell me that you've got us well and truly lost!"
    "I do the best I can to ignore Audrey's constant complaining."
    "But she doesn't give up for a second as I try to find the way out."
    "And as you can imagine, that takes a lot longer as a result."
    "So by the time we do make it out of the place, I'm pretty flustered."
    "And I'm also wishing I could have left her in there too!"
    $ audrey.love -= 2
    $ game.active_date.score -= 20
    return

label audrey_date_amusement_ice_cream_male:
    mike.say "Hey, Audrey..."
    mike.say "You want an ice-cream?"
    "I almost wince as soon as the words are out of my mouth."
    "Because I didn't think for a moment before I said that."
    "I just saw the ice-cream stand and blurted it out."
    "And now I'm afraid that Audrey's going to totally destroy me!"
    "But to my immense surprise, she cocks her head on one side and smiles."
    audrey.say "Hmm..."
    audrey.say "You know what, [hero.name]…"
    audrey.say "I kinda think I do."
    "Not wanting to look a gift horse in the mouth, I instantly begin nodding."
    mike.say "That's great, Audrey..."
    mike.say "Let's go see what they have, yeah?"
    "Audrey follows in my wake as I hurry over to the ice-cream stand."
    "And then she picks out the one that she wants."
    audrey.say "I'll have one of those, yeah?"
    "I'm still nodding as I give the server our order."
    "Then I happily hand Audrey her chosen ice-cream and begin to lick my own."
    "But it doesn't take long for me to stop dead, lips parted and tongue out."
    "Because Audrey's licking hers in a way that impossible to ignore."
    "I watch helplessly as her tongue caresses the ice-cream."
    "And the moans that she makes as she swallows each mouthful..."
    "Let's just say that it makes me feel a little hot, and rather awkward."
    "Plus there's the fact that Audrey knows exactly what she's doing right now."
    "Which means that she smiles wickedly as I'm forced to watch the show."
    $ audrey.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
