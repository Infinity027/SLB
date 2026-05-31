label emma_date_amusement_park_male:
    scene bg amusement
    show emma blush
    with fade
    "Sometimes when I take a girl to the Amusement Park, it feels like I have to drag them in there."
    "Like no matter how much fun they are, they just can't enjoy a place like this in the way I can."
    "But then I made the decision to bring Emma here - and now I'm the one struggling to keep up!"
    show emma happy
    emma.say "Come on, [hero.name]…"
    emma.say "What are you waiting for?"
    show emma blush
    mike.say "I..."
    mike.say "I'm coming...as fast...as I can!"
    mike.say "Just slow down a little, maybe?"
    "Emma pauses for a moment."
    "Just long enough to look back over her shoulder."
    "And I can see from the look on her face that she's not very sympathetic."
    show emma happy
    emma.say "No time for that now."
    emma.say "At this rate they'll be closing before we do all the decent rides!"
    emma.say "So pick up your feet and follow me!"
    show emma blush
    "With that, Emma turns her back on me and literally runs through the gates."
    "Leaving me to huff and puff as I try to sprint after her."
    "Who knows, maybe the girl being less enthusiastic than me is actually a good thing?"
    return

label emma_date_ferris_wheel_male:
    mike.say "Hey, Emma..."
    mike.say "You want to ride the Ferris wheel?"
    "Emma looks up at the ride as I ask the question."
    "Then she shrugs and nods her head."
    emma.say "I guess so."
    emma.say "At least the queue looks short for this one."
    "Not the most enthusiastic response."
    "But it's good enough for me."
    "Together we join the back of the queue, waiting patiently."
    "And it seems that Emma was right, as we soon make our way to the front."
    "Emma and I settle into our gondola and the safety bar comes down."
    "Then the ride begins to move, and we rise slowly into the air."
    "I can't help being fascinated by the view as it's revealed to me."
    "And it gets steadily better the higher we go."
    "Until the ride comes to a halt at the top and we can see for literally miles."
    mike.say "Wow..."
    mike.say "What a view!"
    "I'm expecting a response from Emma."
    "But when none comes, I try to nudge her again."
    mike.say "It's amazing!"
    mike.say "Don't you think so, Emma?"
    emma.say "Meh..."
    emma.say "You can see for miles, so what?"
    emma.say "I could look all of this up on the internet."
    $ emma.love -= 2
    $ game.active_date.score -= 20
    return

label emma_date_merry_go_round_male:
    mike.say "Hey, Emma..."
    mike.say "Let's go ride the Merry-Go-Round!"
    "Emma looks the ride in question up and down."
    "Then she shrugs and nods her head."
    emma.say "I guess so."
    emma.say "At least this one's going to be over quickly."
    "Not the most enthusiastic response."
    "But beggars can't be choosers, or so they say."
    "Together we join the back of the queue, standing quietly."
    "And we soon make our way to the front."
    "Emma and I find the places where we want to sit for the ride."
    "Then the ride begins to move, and turn around ever faster."
    "This really takes me back to being a kid."
    "And I can't keep a smile from spreading across my face."
    mike.say "How about this, Emma?"
    mike.say "Isn't it great?"
    "Emma kind of curls her lips and then shakes her head."
    emma.say "It's okay, I guess..."
    emma.say "But we're really just going round in circles."
    mike.say "Erm..."
    mike.say "I can't argue with that!"
    $ emma.love += 0
    $ game.active_date.score += 0
    return

label emma_date_haunted_house_male:
    mike.say "Look, Emma..."
    mike.say "It's the Haunted House - my favourite!"
    mike.say "We absolutely have to go in there!"
    "The moment I mention it, Emma looks horrified."
    "She shakes her head while clinging onto my arm."
    "And she actually tries to pull me away from the Haunted House."
    emma.say "Oh no..."
    emma.say "No way, [hero.name]!"
    emma.say "I hate stuff like that!"
    "Part of me knows that I should be more sympathetic to Emma's concerns."
    "And if it were any other ride in the park I'd be just that."
    "But the Haunted House is the exception that proves the rule."
    "And there's no keeping me out of the place."
    mike.say "Don't worry, Emma..."
    mike.say "I'll keep you safe, I promise."
    "Emma still doesn't look convinced."
    "But she lets me lead her over to the queue all the same."
    "She clings onto my arm the whole time we're waiting to go in."
    "And as soon as we're inside and the scares start coming, she's terrified."
    "Never mind clinging onto me, she all but leaps into my arms."
    "By the time we make it out the other end, she's literally quaking with fear."
    "And I'm beginning to wonder if I did the right thing insisting we go in there."
    $ emma.love -= 2
    $ game.active_date.score -= 20
    return

label emma_date_love_boat_male:
    emma.say "Oh look, [hero.name]…"
    emma.say "They have a Love Boat!"
    emma.say "I'd love to ride one of those!"
    "For a moment, all I can do is stare at Emma in sheer amazement."
    "And it takes her a few seconds to realise why."
    emma.say "[hero.name], why are you looking at me like that?"
    emma.say "Seriously, what's the matter?"
    mike.say "Just say you want to ride the Love Boat, Emma!"
    mike.say "I'm a guy, you're a girl."
    mike.say "We're a couple, yeah?"
    mike.say "And the ride is right there!"
    "Suddenly Emma seems to realise what I'm say."
    "And she begins to turn a deep shade of red."
    "But that's not all she does."
    "As she also takes hold of my hand and hurries over to the ride."
    "We join the queue and soon we're stepping into one of the boats."
    "Emma leans against me as we sail into the darkness of the tunnel."
    "And from there the ride is a pleasant experience for the both of us."
    "I'm not going to tell you what we get up to, that's private."
    "But Emma's not the only one looking red and flushed when we come out the other end."
    "So make of that what you will."
    $ emma.love += 4
    $ game.active_date.score += 40
    return

label emma_date_hedge_maze_male:
    mike.say "Emma..."
    mike.say "You want to have a walk around the Hedge Maze?"
    show emma annoyed
    "Emma looks around, seeing the sign for the maze for the first time."
    "Then she shakes her head at me."
    emma.say "I'm not that bothered, [hero.name]."
    emma.say "But we can check it out if that's what you want."
    "Not really an eager response."
    "But I guess it'll have to do."
    "We join the back of the queue, waiting patiently."
    "And it seems as though everyone else is as blasé about the ride as Emma."
    "Because it's really short and moves super-quick too."
    "Before I know it, we're inside the maze."
    "Where we find ourselves flanked by thick, tall hedges."
    mike.say "Come on, Emma..."
    mike.say "Let's find our way out of here!"
    "Emma sighs as I begin to explore the maze."
    "But she follows on my heels the whole time."
    "Though that could just be on account of not wanting to get lost in here."
    "And soon enough I find the way out again, leading us back into the park."
    mike.say "Oh..."
    mike.say "Looks like that's it."
    emma.say "Thank god for that."
    emma.say "I was worried I might explode with excitement at any moment."
    $ emma.love += 0
    $ game.active_date.score += 0
    return

label emma_date_amusement_ice_cream_male:
    mike.say "Hey, Emma..."
    mike.say "You want to grab an ice-cream?"
    "I ask the question because I really would like one myself."
    "But also because I can see that Emma's kind of struggling with the heat."
    "And so I sense the chance to kill two birds with one stone."
    emma.say "Oh..."
    emma.say "I..."
    emma.say "I don't know about that, [hero.name]..."
    "Without a conscious thought, I've already started to walk towards the ice-cream stand."
    "Which of course means that Emma is obliged to walk that way too, tyring to keep up."
    mike.say "Are you sure?"
    mike.say "It'd really cool you down."
    emma.say "But they're so messy, yeah?"
    emma.say "And there's all these people watching too!"
    "I'm now in the queue and rapidly moving towards the front."
    "So the best I can do is shrug and just order for myself."
    "Which means that I'm soon holding my ice-cream in front of Emma."
    emma.say "Oh dear..."
    emma.say "That really does look pretty good!"
    "I hold it out to her, offering her the chance to lick it."
    "Emma looks around, as if she's afraid of being seen."
    "But then she seems to have a surge of confidence."
    "Because she closes her eyes and leans forwards."
    "Then she takes a pretty big lick of the ice-cream."
    "Which breaks the ice, if you'll pardon the pun."
    "And from that moment on, we share the ice-cream."
    $ emma.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
