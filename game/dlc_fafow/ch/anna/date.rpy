label anna_date_amusement_park_male:
    scene bg amusement
    show anna normal
    with fade
    "Normally I'm the one eager to get into the Amusement Park when I visit the place."
    "Having to pull my less enthusiastic date through the gates after me."
    "But today the roles are reversed, as I'm currently doing all I can to keep up to Anna."
    show anna happy
    anna.say "Come on, [hero.name]…"
    anna.say "Why are you going so slowly?!?"
    anna.say "We need to get in there and get on the rides!"
    show anna normal
    "I really am doing all that I can to match Anna's pace, trying my best to do as she asks."
    "But somehow she's managing to take longer strides than me and walk far faster."
    "Even though her legs are a lot shorter than mine!"
    mike.say "I'm going as fast as I can, Anna..."
    mike.say "And the rides aren't going anywhere!"
    show anna talkative
    anna.say "Then we need to get in there before the place closes!"
    show anna normal
    mike.say "What are you talking about?"
    mike.say "The park doesn't close for hours yet..."
    show anna evil
    "It's no use keeping on trying to reason with Anna."
    "My words are falling on deaf ears and doing no good."
    "So I just keep on doing the best I can to keep up."
    "And that also means letting her drag me into the park."
    "But I suppose that I should just be grateful that she's so into the place."
    return

label anna_date_ferris_wheel_male:
    "Anna's enthusiasm continues to grow as she sets eyes on the Ferris Wheel."
    "I feel her grip on my hand tighten as she pulls me towards it too."
    anna.say "Come on, [hero.name]…"
    anna.say "We're riding the Ferris Wheel!"
    mike.say "Oh..."
    mike.say "Okay, Anna."
    "Soon enough we're in the queue for the ride, and then getting onto it."
    "The safety bar comes down, and the ride starts up, raising us into the air."
    "At first, Anna's all giggles and cuddles, clinging to my side."
    "All of which is fine with me, and I return the gesture too."
    "But as we get closer to the top of the wheel, I feel a change in her."
    "Now it's more like Anna's clinging onto me out of genuine fear."
    "Looking down at her, I can see that Anna's gone pale."
    "And her eyes are wide open, like she's staring at something in terror."
    mike.say "Anna..."
    mike.say "Are you okay?"
    mike.say "Because you don't look okay!"
    anna.say "Oh boy..."
    anna.say "I really don't feel good, [hero.name]!"
    anna.say "I think it's being all the way up here."
    mike.say "You mean it's vertigo?"
    mike.say "Why didn't you say that you have a problem with heights?"
    anna.say "I...I don't normally..."
    anna.say "Oooh...I think it's something I ate!"
    "With that, Anna leans over the edge of the gondola with a groan."
    "And then she proceeds to lose the contents of her stomach."
    anna.say "Urgh..."
    "Luckily for us, most of it misses the other people on the Ferris Wheel."
    "Although it does hit the ground pretty close to the queue for the ride..."
    $ anna.love -= 4
    $ game.active_date.score -= 20
    return

label anna_date_merry_go_round_male:
    "I spot as classic Merry-Go-Round as we're walking through the park."
    "And the moment that I do, I get the urge to ride on it."
    mike.say "You see that Merry-Go-Round, Anna?"
    mike.say "That one right there?"
    anna.say "Yeah?"
    anna.say "What about it?"
    mike.say "I think we should go ride it, of course!"
    "Anna gives me a non-committal nod."
    "But that's all I need to put my plan into action."
    "So we hurry over there and join the queue for the ride."
    "It doesn't take long for us to make it to the front and get on."
    "And a few moments later, the ride starts to move."
    "Pretty soon we're going round at a considerable rate."
    "I'm enjoying the sensation of being on the ride."
    "As well as the feeling of nostalgia it inspires in me."
    "But when I look over at Anna, she doesn't seem to share my enthusiasm."
    mike.say "What's wrong, Anna?"
    mike.say "You don't look like you're enjoying yourself."
    anna.say "Ah, it's not like I don't like it, [hero.name]…"
    anna.say "This ride just isn't very exciting, that's all."
    anna.say "I guess I like my rides a little more wild than this."
    $ anna.love -= 0
    $ game.active_date.score -= 0
    return

label anna_date_haunted_house_male:
    "I hear the sound of groans and screams from up ahead."
    "And then I see the familiar shape of the Haunted House."
    "As we get closer still, I can see all the creepy stuff hanging off it too."
    anna.say "What are you looking at, [hero.name]?"
    mike.say "The Haunted House over there, Anna."
    mike.say "I always loved going in those when I was a kid."
    anna.say "Then why don't we go in that one right now?"
    mike.say "You want to?"
    anna.say "Isn't that what I just said?"
    mike.say "Okay, Anna - let's go!"
    "Anna and I join the queue for the Haunted House."
    "And soon enough we're inside, walking the narrow corridors."
    "It's just like I remember it being when I was a kid."
    "Dimly lit and crammed full of spooky shit that leaps out at you."
    "Sure, most of it looks pretty cheesy to my now adult eyes."
    "But the sheer hit of nostalgia it represents makes up for that."
    "In fact I'm so caught up in the moment that I don't notice Anna's reaction."
    "The fact that she looks pretty blasé doesn't hit me until we're at the exit."
    mike.say "Are you okay, Anna?"
    mike.say "You seemed miles away in there."
    anna.say "Oh no, I'm fine..."
    anna.say "I was just never into those things myself."
    anna.say "But I wanted you to be able to indulge yourself."
    $ anna.love += 1
    $ game.active_date.score += 10
    return

label anna_date_love_boat_male:
    "I see that the queue for the Love Boat ride is pretty short."
    "So I guess most of the people here are riding the more exciting attractions right now."
    "But that could work out well for Anna and me."
    mike.say "Anna..."
    mike.say "You want to ride the Love Boat?"
    anna.say "Seriously?"
    anna.say "That ride goes slower than I can walk!"
    mike.say "Yeah, I know."
    mike.say "But the queue's real short."
    mike.say "You see?"
    "Anna shrugs and allows me to steer her towards the ride in question."
    "Then we join the queue and eventually find ourselves in a boat of our own."
    "As slowly as Anna predicted, we float off down the dimly-lit tunnel."
    "And yeah, in the privacy in affords us, we get up to some pretty fun stuff."
    "No, nothing that involves the inserting of organs into each other!"
    "You people have such filthy minds..."
    show anna kiss
    $ anna.flags.kiss += 1
    "We just get into some intense kissing and cuddling."
    "But when we emerge, Anna seems as apathetic as she was when we went in there."
    show anna -kiss
    mike.say "You okay, Anna?"
    mike.say "Because you look a little bored!"
    anna.say "Nah, I'm fine."
    anna.say "That was just a bit tame for my tastes."
    $ anna.love -= 0
    $ game.active_date.score -= 0
    return

label anna_date_hedge_maze_male:
    mike.say "There's the Hedge Maze, Anna."
    mike.say "Let's go check it out, yeah?"
    "Anna follows my gaze."
    "But she doesn't look convinced."
    anna.say "Really?"
    anna.say "It's just a bunch of hedges!"
    mike.say "Oh come on, Anna."
    mike.say "These things have been around for centuries."
    mike.say "There must be something to them to have lasted that long."
    "Anna shrugs at this."
    anna.say "Okay, [hero.name]…"
    anna.say "Let's give it a try."
    "Anna shrugs and allows me to steer her towards the ride in question."
    "Then we join the queue and eventually find ourselves wandering the maze."
    "I'm doing the best I can to keep track of where we are."
    "But with each twist and turn, I can feel myself getting more disoriented."
    "Soon enough I have no idea where we are or which turn to take next."
    "When we finally find our way out, it comes as a genuine relief."
    "But when we emerge, Anna seems as apathetic as she was when we went in there."
    mike.say "You okay, Anna?"
    mike.say "Because you look a little bored!"
    anna.say "Nah, I'm fine."
    anna.say "That was just a load of hedges..."
    anna.say "And it was so boring!"
    $ anna.love -= 1
    $ game.active_date.score -= 10
    return


label anna_date_amusement_ice_cream_male:
    mike.say "Hey, Anna..."
    mike.say "I could really use something to cool me down right now."
    mike.say "You want to grab an ice-cream?"
    "The moment Anna hears the words, I see her eyes light up."
    "She starts nodding as she grabs hold of my hand."
    "Then she's literally pulling me towards the ice-cream stand."
    anna.say "You had me at 'cool down', [hero.name]..."
    anna.say "I frickin love ice-cream!"
    mike.say "Huh?"
    mike.say "How could I have had you at 'cool down'?"
    mike.say "I never mentioned ice-cream until I said the words!"
    "Anna shakes her head as we make it to the front of the queue."
    anna.say "Ah, stop overthinking everything, [hero.name]..."
    anna.say "Just make with the ice-cream already!"
    "I hand over the money and the ice-cream seller gives us our frozen treats."
    "Then I watch as Anna attacks hers like it's going to melt in seconds."
    mike.say "Slow down, Anna..."
    mike.say "Otherwise you'll give yourself..."
    anna.say "AAARGH!"
    anna.say "Brain freeze!"
    $ anna.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
