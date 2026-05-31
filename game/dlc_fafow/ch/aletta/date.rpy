label aletta_date_amusement_park_male:
    scene bg amusement
    show aletta
    with fade
    "I'm always pretty stoked to get the chance to go to the amusement park."
    "It kind of turns me into a big kid that can't wait to get in there."
    show aletta sadsmile
    "But as we walk through the entrance, I can feel Aletta holding back."
    "She's resisting as I try to pull her in after me."
    "And when I turn around, I see she has a genuine grimace on her face."
    mike.say "What's the matter, Aletta?"
    mike.say "Aren't you excited to be going to the amusement park?"
    show aletta pain
    "Aletta screws her face up into a frown."
    aletta.say "Urgh..."
    show aletta whining
    aletta.say "Cards on the table, [hero.name]…"
    aletta.say "This really isn't my idea of a fun time."
    show aletta sadsmile
    "I can't help looking puzzled at Aletta's confession."
    mike.say "But you like riding fast motorbikes, Aletta."
    mike.say "And shooting stuff too."
    mike.say "I thought you'd love the thrill of the rides here?"
    show aletta talkative
    aletta.say "Those are real things, [hero.name]."
    aletta.say "With real danger involved too."
    aletta.say "So the thrill with them is real."
    show aletta sadsmile
    mike.say "But you don't need real danger to have real fun, Aletta!"
    mike.say "Just give it a chance, and you'll soon see I'm right."
    show aletta dreamy
    "Aletta sighs and gives me a nod."
    "Which at least lets me know that she's willing to give it a try."
    "So I pull her after me into the amusement park."
    "Determined to prove my point to her."
    show aletta normal
    return

label aletta_date_ferris_wheel_male:
    "Maybe the thing Aletta needs is something that's not supposed to be so intense."
    "Maybe a ride on the Ferris Wheel will be enough to ease her into the experience of the park?"
    mike.say "Come on, Aletta..."
    mike.say "Let's ride the Ferris Wheel."
    aletta.say "If you say so."
    aletta.say "But don't get your hopes up..."
    "Soon enough we're sitting in our seats, being strapped in."
    "And I'm already pointing out the wonders of the ride to Aletta."
    mike.say "Just sit back and take in the view, yeah?"
    mike.say "This ride's more about the atmosphere."
    "Aletta stays quiet as the ride gets going."
    "But when we reach the top, she's still silent."
    mike.say "Erm..."
    mike.say "So look at that view, huh?"
    mike.say "Pretty romantic, right?"
    "Aletta shakes her head as she scans the horizon in front of her."
    aletta.say "So we're up really high..."
    aletta.say "So what?"
    aletta.say "The view from my office window is higher and more impressive."
    "That kind of kills it for me, leaving me silent for the rest of the ride too."
    "And once it's over, I'm relieved to get away from the thing."
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return

label aletta_date_merry_go_round_male:
    "The Merry-Go-Round is a classic of the amusement park."
    "Something that everyone remembers fondly from childhood, right?"
    "Well, maybe everyone apart from Aletta!"
    "As soon as we get on the thing she looks like she's bored to death."
    "And things don't get much better once it starts moving."
    mike.say "How are you liking it, Aletta?"
    mike.say "I bet this takes you back?"
    "Aletta rolls her eyes at this and lets out a groan."
    aletta.say "Urgh..."
    aletta.say "What is it with this kind of thing?"
    aletta.say "I'm sitting on my ass, going round in a circle."
    aletta.say "Tell me what's so exciting about that?"
    "I turn my gaze away from Aletta after that."
    "Doing the best I can to look anywhere but at her."
    "It makes the rest of the ride pretty tense and awkward."
    "And the truth is that I'm more than glad when the ride comes to an end."
    "Now the memory of riding a Merry-Go-Round will always be tainted for me."
    "Because I'll always remember Aletta's boredom and endless complaints."
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return

label aletta_date_haunted_house_male:
    mike.say "The Haunted House looks great, Aletta!"
    mike.say "It's got so many floors..."
    mike.say "And I bet they're all packed with scares!"
    "Aletta doesn't resist as I lead her towards the entrance."
    "But the look on her face tells me that she's less than impressed."
    aletta.say "You really want to go in there?"
    aletta.say "It looks like something for kids on Halloween!"
    "I do the best I can to ignore Aletta's withering comments."
    "And soon enough we're inside the Haunted House."
    "I know full well that this is all for show."
    "And that there are going to be cheesy things leaping out at us."
    "But somehow I still manage to jump and even screams as we walk around."
    "The problem is that everything I do seems to annoy Aletta even more."
    "She spends the whole time groaning and rolling her eyes."
    "I even find that she can guess when all of the scares are coming."
    aletta.say "Fake werewolf from the right..."
    mike.say "Aargh!"
    mike.say "Look at his fangs!"
    aletta.say "Plastic skeleton from the left..."
    mike.say "Whoa!"
    mike.say "I've got a bone to pick with that guy!"
    "No matter how hard I try, Aletta pisses on everything."
    "And she doesn't stop complaining even when we get out of there."
    aletta.say "That was so lame, [hero.name]."
    aletta.say "A total waste of time and money!"
    mike.say "Okay, Aletta..."
    mike.say "Point taken!"
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return

label aletta_date_love_boat_male:
    mike.say "So you don't like fake thrills."
    mike.say "What about the Love Boat, Aletta?"
    mike.say "That's supposed to be more sedate."
    aletta.say "I suppose we could give it a go."
    "Aletta follows in my wake as we join the queue."
    "And she sits in the boat without complaining too much."
    "But as soon as the ride begins, she can't hold back any longer."
    aletta.say "So this is it?"
    aletta.say "We just sit in a crappy boat?"
    aletta.say "And we sail down a badly-lit tunnel?"
    mike.say "Erm..."
    mike.say "It's supposed to be romantic, Aletta."
    mike.say "You know, like a chance to spend some time together?"
    mike.say "In private?"
    "Aletta makes a huffing noise as she looks around."
    aletta.say "Humph..."
    aletta.say "In that case they might have wanted to clean it up a little."
    aletta.say "The water smells like an open sewer."
    aletta.say "And the paint is peeling off everything too!"
    mike.say "I don't think they expect you to notice stuff like that."
    mike.say "Most people are too busy making out."
    aletta.say "Well I won't be doing that."
    aletta.say "Not with so much to put me off!"
    mike.say "Yeah..."
    mike.say "There's something putting me off too."
    mike.say "But I can't quite put my finger on it..."
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return

label aletta_date_hedge_maze_male:
    "I spot the Hedge Maze and make a point of pulling Aletta towards it."
    mike.say "Let's try the Hedge Maze, Aletta..."
    mike.say "See if you can find your way out of it!"
    aletta.say "Whoa..."
    aletta.say "Slow down, [hero.name]!"
    aletta.say "It's just a bunch of overgrown weeds!"
    "I do the best I can to ignore Aletta's complaints as I pull her inside."
    "Because I figure that she'll soon get into the spirit of the maze."
    "But as I lead her deeper into it, her mood doesn't seem to improve."
    mike.say "Wow..."
    mike.say "I'm like, totally lost!"
    mike.say "How about you, Aletta?"
    "Aletta rolls her eyes and shakes her head."
    "Like she's talking to a total idiot."
    aletta.say "You didn't memorise the route we took when we came in?"
    aletta.say "Seriously, [hero.name], it's just a matter of memory."
    aletta.say "I doubt most children would find it that hard to do!"
    mike.say "Erm..."
    mike.say "I didn't think of that, Aletta..."
    mike.say "I was kind of too busy having actual fun!"
    aletta.say "Well that's where you slipped up, isn't it?"
    aletta.say "Pay more attention to your surroundings next time!"
    mike.say "Okay, Aletta..."
    mike.say "More attention, less fun."
    mike.say "That sounds great..."
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return

label aletta_date_amusement_ice_cream_male:
    "I'm starting to feel hot and bothered as we push through the crowds at the amusement park."
    "And it feels like I need to do something in order to change the pace for a while."
    "So when I see an ice-cream stand up ahead, I make straight for it."
    mike.say "Those ice-creams look amazing, Aletta..."
    mike.say "What do you say we go grab a couple?"
    "Aletta makes a snorting sound and wrinkles her nose."
    "Both of which don't exactly fill me with hope."
    aletta.say "Urgh..."
    aletta.say "Are you serious, [hero.name]?"
    aletta.say "Those things are just chemicals and empty calories!"
    aletta.say "Plus I don't want ice-cream dripping on my clothes."
    "Aletta has a hold of my hand as she says all of this."
    "And I can already feel her steering me away from the ice-cream stand."
    "But as I don't want to start an argument and ruin the date, there's nothing I can do."
    "So I'm forced to watch as the ice-cream stand disappears into the distance."
    "And the hot, sweaty crowds swallow us up again."
    $ aletta.love -= 2
    $ game.active_date.score -= 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
