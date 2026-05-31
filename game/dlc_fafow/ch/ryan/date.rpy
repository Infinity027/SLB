label ryan_date_amusement_park_female:
    scene bg amusement
    show ryan smile
    with fade
    ryan.say "What's the hurry, [hero.name]?"
    ryan.say "The rides in there aren't going anywhere."
    ryan.say "So what's the point in rushing to get into the place?"
    show ryan normal
    "I turn my head to stare at Ryan, unable to believe what I'm hearing."
    "How can anyone not want to hurry to get into the Amusement Park?"
    "For me, it's one of the most amazing places in the whole of the city."
    "Somewhere that I go to have pure, unadulterated fun."
    bree.say "I dunno, Ryan..."
    bree.say "I could ask how you can be such a killjoy, you know?"
    bree.say "You need to lighten up, because we're here to have fun!"
    show ryan annoyed
    "Ryan can't help rolling his eyes and making a tutting sound."
    "Like he's a parent telling off a disobedient child."
    show ryan smile
    ryan.say "The last time I remember coming to a place like this, I was a kid."
    ryan.say "Since then, I've kind of moved on to doing more mature things for fun."
    show ryan evil
    ryan.say "I don't suppose this is the kind of place they have a bar?"
    ryan.say "You know, where parents can go while their kids are on the rides?"
    show ryan normal
    "I shake my head, totally amazed by what Ryan's asking."
    show ryan sad
    bree.say "No there is not!"
    bree.say "We're here to go on the rides, Ryan."
    bree.say "We can go to the pub afterwards, if that's what you want."
    show ryan smile
    ryan.say "Okay, okay..."
    ryan.say "At least that gives me something to look forward to."
    return

label ryan_date_ferris_wheel_female:
    bree.say "Let's ride the Ferris Wheel, Ryan..."
    bree.say "The queue's short and it's moving fast."
    "Ryan almost sniffs as he looks over at the ride in question."
    "But he walks over to it with me all the same."
    ryan.say "Well of course it is, [hero.name]..."
    ryan.say "That has to be the oldest ride in the park!"
    "The queue turns out to be just as short and fast as I thought."
    "Which means that we're soon getting into a gondola."
    "The safety-bar comes down, and we start to rise into the air."
    "The higher we get, the better the view seems to become."
    "And I'm kind of hoping that'll be enough to impress Ryan."
    "But I wait until we get to the very top to say anything."
    "Because that's when the ride pauses for a moment."
    "And we're treated to a panoramic view of the entire city."
    bree.say "Wow..."
    bree.say "Now that's worth the effort, isn't it?"
    bree.say "You don't get to see a view like that every day!"
    ryan.say "What are you talking about, [hero.name]?"
    ryan.say "There are buildings in the city far taller than this."
    ryan.say "And I could climb to the top of any one of them, any time I want!"
    ryan.say "Plus I wouldn't have to pay for the privilege."
    "Well that more than kills the mood."
    "And I spend the rest of the ride in silence."
    "Deliberately looking the other way and avoiding eye-contact."
    $ ryan.love -= 2
    $ game.active_date.score -= 20
    return

label ryan_date_merry_go_round_female:
    "I've been clinging onto the pole on the Merry-Go-Round for the whole ride."
    "And every moment that it lasted, my eyes have been facing forwards too."
    "Anything to keep from having to look over at Ryan, on the horse next to me."
    "Because the last time I made that mistake, I was met with a frosty glare."
    "But I'm hoping that by the time the ride comes to an end, his mood will have changed."
    "Because everyone love a ride on the Merry-Go-Round, right?"
    "It's a total good, guaranteed to improve your mood."
    "Apparently not, because Ryan gets off the thing in a worse mood than when he got on it!"
    ryan.say "Remind me again why I agreed to ride that thing, [hero.name]?"
    bree.say "Erm..."
    bree.say "Because I asked you to?"
    ryan.say "Oh yeah, that was the reason."
    ryan.say "And thanks to you I'm bored stupid."
    ryan.say "Plus I have the added pleasure of a dead ass too!"
    "Now that I wasn't expecting."
    "So I can't help looking around to see what Ryan means."
    "And as soon as I see that he's limping and staggering, I can't help it."
    "I just burst out laughing, as he looks so ridiculous."
    bree.say "Ha, ha..."
    bree.say "Oh man!"
    bree.say "That is so funny!"
    ryan.say "Well I'm glad that you find it amusing, [hero.name]."
    ryan.say "My buttocks are as numb as rocks right now!"
    $ ryan.love -= 1
    $ game.active_date.score -= 10
    return

label ryan_date_haunted_house_female:
    bree.say "Come on, Ryan..."
    bree.say "I want to do the Haunted House next!"
    "I look back over my shoulder to make sure Ryan's following."
    "And I see that he's dutifully trudging along behind me."
    ryan.say "Urgh..."
    ryan.say "Do we have to, [hero.name]?"
    ryan.say "That place looks like the absolute worst of Halloween!"
    "I do the best I can to ignore Ryan's negativity."
    "Instead I join the back of the line and motion for him to stand by me."
    "Then I tune out the rest of his complaints as we move up the queue."
    "I don't check back into reality until we're about to step into the Haunted House."
    "And the first thing that I hear when I do is the sound of Ryan ranting on."
    ryan.say "I mean..."
    ryan.say "It's cheap, tacky and vulgar in the extreme."
    ryan.say "And the last thing in the world that it could be is scary!"
    bree.say "Wow!"
    bree.say "Have you been complaining this whole time?"
    ryan.say "Of course I have!"
    ryan.say "Haven't you been listening to a word I've said?"
    bree.say "Nope..."
    bree.say "Can't say that I have!"
    "With that, I walk into the Haunted House."
    "Ryan follows on my heels."
    "But I get the impression that's more so he can keep on complaining."
    "In fact he manages to do that the whole way around the Haunted House."
    "And I don't think that he even notices all the stuff that leaps out at us."
    "He only seems to stop once we walk out of the exit."
    "Which is when he does a double-take, looking around him in genuine surprise."
    ryan.say "Wait..."
    ryan.say "How did we get out here?"
    ryan.say "Did we even go into the Haunted House?"
    bree.say "Looks like you complained so much you missed it all!"
    $ ryan.love -= 2
    $ game.active_date.score -= 20
    return

label ryan_date_love_boat_female:
    bree.say "You want to ride the Love Boat, Ryan?"
    bree.say "It sounds romantic, right?"
    "Ryan looks at the ride in question."
    "And the expression on his face is one of disgust."
    "Like he's examining something on the sole of his shoe."
    ryan.say "'Love Boat'!"
    ryan.say "It's just a rickety boat in a dark tunnel, that's all."
    bree.say "At least give it a try."
    bree.say "Maybe it'll surprise you."
    ryan.say "I highly doubt that!"
    "For all of his negativity, Ryan still follows me over to the ride."
    "And he joins the queue as well, standing in line to wait our turn."
    "He even steps into the boat when we're ushered onto the ride too."
    "Though the bored look on his face speaks volumes."
    "I had been hoping for something pleasant to happen once we were on here."
    "That maybe the chance to be alone together would change something in Ryan."
    "You know, that he might actually start to behave in a romantic way?"
    "But instead I'm treated to another round of endless complaining."
    ryan.say "You know what..."
    ryan.say "This boat doesn't feel safe to me."
    ryan.say "And I don't like the look of that water either."
    ryan.say "Urgh...it smells even worse than it looks!"
    ryan.say "I'm going to complain the moment we get off this thing."
    bree.say "That's great, Ryan..."
    bree.say "Just perfect!"
    bree.say "And they say romance is dead!"
    $ ryan.love -= 2
    $ game.active_date.score -= 20
    return

label ryan_date_hedge_maze_female:
    ryan.say "Oh, isn't this magical!"
    ryan.say "I really feel transported to another world..."
    ryan.say "One made totally out of severely trimmed bushes!"
    "Getting tired of Ryan's sarcastic comments, I stop dead."
    "Then I turn on my heel, sticking a finger in his face."
    bree.say "Okay, Ryan..."
    bree.say "That's enough of that."
    bree.say "I get that you're not having fun, yeah."
    bree.say "But the least you could do is shut up and help me find the way out!"
    "Ryan recoils from my withering tirade."
    "Actually looking like he regrets annoying me so much."
    "He holds up his hands, warding off any further attacks."
    "But that doesn't mean that he actually starts helping."
    "Instead Ryan seems to fall into a sullen silence."
    "And he sulks the rest of the way around the maze."
    "But at least it's a small mercy that he's actually shut up."
    "Because that gives me the mental space I need to get my brain in gear."
    "That done, it's not long before I start to make progress."
    "And soon enough I find the exit, leading us out of the maze."
    "I shoot Ryan a triumphant look as I stride out of there."
    "And he at least has the good grace to look a little ashamed of himself."
    $ ryan.love -= 2
    $ game.active_date.score -= 20
    return

label ryan_date_amusement_ice_cream_female:
    bree.say "Hmmm..."
    bree.say "You know what, Ryan..."
    bree.say "I could really murder an ice-cream right now."
    bree.say "You want me to get you one too?"
    "I'm expecting a pretty simple answer from Ryan."
    "Like a yes or no, and for that to be the end of it."
    "But instead he gives me this weird, quizzical look."
    ryan.say "You know, [hero.name]..."
    ryan.say "There's no need to pussyfoot around."
    ryan.say "If you want me to buy you an ice-cream, you only have to ask!"
    "I frown at Ryan, wondering what the hell he's talking about."
    bree.say "Erm..."
    bree.say "I don't want you to buy me one, Ryan..."
    bree.say "I'm going to buy one for myself."
    bree.say "Just wondered if you wanted one too, yeah?"
    "Ryan shakes his head and lets out a chuckle."
    "At the same time he starts walking towards the nearest ice-cream stand."
    ryan.say "No need to talk in code, [hero.name]..."
    ryan.say "I'll buy you the damn ice-cream!"
    "I follow on his heels, shaking my head."
    bree.say "What are you talking about?"
    bree.say "That wasn't code!"
    "By now Ryan's at the front of the line, ordering the ice-creams."
    "And he waves away my complaints as he hands one of them to me."
    ryan.say "There you go, [hero.name]..."
    ryan.say "Now that wasn't so hard, was it?"
    ryan.say "Just come straight out and ask next time!"
    "I narrow my eyes and shoot Ryan an evil glare."
    "But my face is almost hidden behind my ice-cream."
    "So he doesn't see my burning look of disapproval."
    $ ryan.love -= 2
    $ game.active_date.score -= 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
