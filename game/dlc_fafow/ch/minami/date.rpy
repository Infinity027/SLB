label minami_date_amusement_park_male:
    scene bg amusement
    show minami normal
    with fade
    "As soon as I see the gates to the Amusement Park, I can't help it."
    "I break into a sprint that quickly becomes a run, desperate to get in there."
    show minami happy
    minami.say "Big Bro!"
    minami.say "Slow down already!"
    show minami normal
    "It's only when I hear her protesting that I remember Minami is with me today."
    "That and the fact she's currently holding onto my hand too."
    "I've been pulling her along with me the whole time I was running!"
    "So I stop instantly, turning to check that she's okay."
    mike.say "Sorry, Minami..."
    mike.say "I guess I kind of got carried away!"
    "Minami takes the chance to catch her breath and straighten her clothes."
    "Then she shakes her head at me, adding a little frown for good measure too."
    show minami happy
    minami.say "I think so, Big Bro..."
    minami.say "But there's no need to run like that."
    minami.say "The Amusement Park isn't going anywhere!"
    show minami normal
    mike.say "I know, I know..."
    mike.say "But you know how I am."
    mike.say "I've always loved coming to places like this."
    mike.say "Ever since we were kids, remember?"
    show minami annoyed
    "Minami cocks her head on one side and looks thoughtful for a moment."
    "Like she's struggling to remember something from so long ago."
    show minami surprised
    minami.say "You have?"
    show minami happy
    minami.say "Funny...I don't seem to recall."
    minami.say "You'd think I'd remember something like that!"
    show minami normal
    "Now that Minami says it, that does seem pretty odd."
    "And I find myself wondering how it could have happened."
    "But then I remember where we are, and the thought vanishes from my head."
    mike.say "Never mind that, Minami..."
    mike.say "Let's get inside and have a good time."
    show minami happy
    minami.say "Whatever you say."
    minami.say "But let's go at my pace this time!"
    return

label minami_date_ferris_wheel_male:
    minami.say "Hey, Big Bro..."
    minami.say "Let's ride the Ferris Wheel!"
    "I can already see the shape of the Ferris Wheel towering above us."
    "And while it's not the most exciting ride in the park, I have no objections."
    "Especially if riding it makes Minami happy too!"
    mike.say "Sure thing, Minami..."
    mike.say "Let's go join the queue."
    "Minami hurries ahead, as if she's afraid we won't be allowed on the ride."
    "And when I manage to catch up with her, she's already standing in the queue."
    minami.say "Hurry up!"
    minami.say "I saved a spot for you right here."
    "Together we stand in line, waiting patiently for our turn."
    "And when it comes round, we step into the waiting gondola."
    "The safety-bar comes down, and then the wheel starts to move."
    "And we're slowly but steadily lifted into the air."
    "Minami's craning her neck as we get higher."
    "Straining to see over the edge of the gondola."
    minami.say "This thing goes pretty high!"
    minami.say "I wonder how high it actually is at the top?"
    "Minami says this as we reach that very spot."
    "And the ride comes to a halt to allow us to enjoy the view."
    mike.say "No idea, Minami."
    mike.say "I think we're supposed to appreciate all that we can see up here."
    mike.say "Not spend the time wondering how high up we are."
    "Minami turns her head to look in the same direction as me."
    "And when she does so, I hear her let out a gasp of appreciation."
    minami.say "Oh yeah..."
    minami.say "That's pretty impressive!"
    "Minami spends the ride back down still looking at the view."
    "And she seems to take something positive away from the ride too."
    "Which I guess makes it worth the effort to ride."
    $ minami.love += 1
    $ game.active_date.score += 10
    return

label minami_date_merry_go_round_male:
    mike.say "That Merry-Go-Round looks like something out of the past!"
    mike.say "I mean, I wonder how old that this must be."
    "Minami seems to hear a least a part of what I'm saying."
    "But I can't be sure that she got all of it though."
    "Because she doesn't offer any kind of answer to my question."
    minami.say "Ooh!"
    minami.say "Look at all the pretty horses, Big Bro!"
    minami.say "We have to ride this one!"
    "Once Minami starts talking like that, I know there's no point resisting."
    "Her mind's made up and there won't be any changing it, no matter what."
    "So when she holds out her hand, I just take it and walk over there with her."
    "We join the back of the queue and wait in line with everyone else."
    "And soon enough we find our way to the front of the queue."
    "Minami and I climb onto the Merry-Go-Round and look for where to sit."
    "Obviously she takes far more time than is strictly necessary to choose."
    "It honestly feels like Minami looks over every single horse on the thing."
    "Maybe she even does it twice!"
    "The ride is almost starting by the time she chooses."
    "And I barely have the chance to leap onto the horse next to her own."
    "I swear that the ride is moving before my ass touches the saddle."
    "So I have to hurry to cling on as we start to turn around."
    "I think that if I'd been able to sit down normally, it would have been okay."
    "But as it is, the speed that the Merry-Go-Round gets up to feels crazy."
    "And I spend the rest of the ride feeling like I'm going to fly off at any moment."
    show minami happy
    "Once the ride is over, Minami hops off happily, grinning from ear to ear."
    "Whereas I stagger off it, my legs feeling like jelly."
    $ minami.love += 2
    $ game.active_date.score += 20
    return

label minami_date_haunted_house_male:
    mike.say "Oh man..."
    mike.say "They have a Haunted House!"
    mike.say "We are SO going in there!"
    "I make straight for the Haunted House, attracted by the spooky decor and sound effects."
    "But I sense that Minami's holding back, so I stop and turn around to see what the problem is."
    "And that's when I see that she's staring, wide-eyed at the Haunted House."
    mike.say "What's wrong, Minami?"
    mike.say "You look like you've seen a ghost!"
    "I realise how dumb that sounds the moment the words leave my mouth."
    "I mean, she's staring at a bloody Haunted House!"
    "But all the same, Minami doesn't seem to pick up on it."
    minami.say "You want me to go in there?!?"
    minami.say "Oh, Big Bro - you know I get scared easily."
    minami.say "And that ride looks super scary!"
    "I can see that Minami's not just saying all of that to be awkward."
    "She really does look terrified at the prospect of going into the Haunted House."
    "And if it were any other ride, I'd give up on the idea for her sake alone."
    "But this is the Haunted House, and I desperately want to get in there!"
    mike.say "Don't worry about it, Minami..."
    mike.say "This place is one of those old-fashioned Haunted Houses."
    mike.say "Everything will be lame and fake in there."
    minami.say "You really mean that?"
    minami.say "It won't be scary?"
    mike.say "Minami, I doubt you'll scream once!"
    "Minami seems to be reassured by this, and together we join the queue."
    "And her confidence lasts as we stand in line and get closer to the entrance."
    "In fact, I think I can pinpoint the exact point when it disappears."
    "And that's the very moment the first scare hits us inside the Haunted House."
    "Minami instantly shrieks and leaps out of her skin."
    "In fact she almost jumps right into my arms."
    "This means that I have to almost carry her through the rest of the Haunted House."
    "And when we get out of the other end, Minami's a quivering wreck."
    "I hurry to get her sat down, trying to calm her nerves."
    "All while regretting the lengths I went to in order to talk in into the place."
    $ minami.love -= 2
    $ game.active_date.score -= 20
    return

label minami_date_love_boat_male:
    minami.say "Oh, Big Bro..."
    minami.say "There's the Love Boat!"
    minami.say "Can we go on it?"
    minami.say "Please, please, please?"
    "For all that she's asking the question, Minami's not exactly waiting for an answer."
    "Because she's dragging me towards the ride in question even as she's asking it."
    "And I'm resisting, more from being bamboozled by her eagerness than anything else."
    mike.say "Whoa..."
    mike.say "Slow down, Minami!"
    mike.say "Are you sure you want to go on the Love Boat?"
    mike.say "You do know that it's just a ride in a boat, yeah?"
    "Minami stops pulling me for a moment."
    "And the expression on her face becomes a strange mixture of emotions."
    "At once it seems amused, knowing and more than a little embarrassed."
    minami.say "Of course I know that, Big Bro!"
    minami.say "But it's different when it's a ride with you..."
    "The way that Minami looks at me then is what seals the deal."
    "Because I can see the promise of all she has in mind, right there in her eyes."
    "Without another word, I turn and start to walk towards the ride."
    "It takes a moment for Minami to recover, but then she eagerly follows along with me."
    "Luckily for me, the queue is short and we make it to the front in record time."
    "And I almost leap into the boat when the moment comes."
    "Minami manages to keep herself under control until we're out of sight."
    show minami kiss
    $ minami.flags.kiss += 1
    "But then she's all over me, kissing, caressing and cuddling like crazy!"
    "I might be overwhelmed for a few seconds, but then I return the favour."
    "And we spend the whole ride exploring each other with a determined passion."
    "Once the ride comes to an end, Minami is draped across me."
    hide minami
    show minami b hunt
    "She lets out a satisfied sigh, and hugs me again."
    minami.say "Oh, Big Bro..."
    minami.say "I love you!"
    mike.say "So do I, Minami!"
    $ minami.love += 3
    $ game.active_date.score += 30
    return

label minami_date_hedge_maze_male:
    minami.say "A Hedge Maze!"
    minami.say "I never went in one of those."
    minami.say "Can we try it out?"
    "I take a look at the Hedge Maze and then nod my head."
    mike.say "Sure we can, Minami."
    mike.say "Let's go join the queue."
    "Minami smiles as she takes hold of my hand."
    "And we do just that, standing where it starts."
    "The Maze doesn't seem to be the most popular attraction in the park."
    "Because the line is short and we're soon at the front."
    "Once we're actually in the maze, Minami seems to come to life."
    "She instantly darts off around the first corner."
    "And she shouts for me to follow her."
    minami.say "Come on, Big Bro..."
    minami.say "Catch me if you can!"
    mike.say "Hey..."
    mike.say "Wait for me!"
    "I run after Minami as fast as I can."
    "But she's still too quick for me, and slips out of sight."
    "This leaves me hunting around every corner of the maze."
    "Looking for Minami wherever she could be hiding."
    "But no matter what I do, I can't seem to find her."
    "That is until she sneaks up on me from behind."
    minami.say "Boo!"
    minami.say "Tag - you're it!"
    "Minami shoots off before I can turn around."
    "And that's how it is until she gets tired of tormenting me."
    "So by the tome we're walking out of the maze, I'm dazed and confused."
    "But Minami seems to be delighted at how she's been able to torment me."
    "Talking constantly about how she wants to go around the maze again."
    $ minami.love += 3
    $ game.active_date.score += 30
    return

label minami_date_amusement_ice_cream_male:
    minami.say "Hey, big bro..."
    minami.say "I'm feeling kinda hot, you know?"
    minami.say "Like I need to cool down?"
    mike.say "You don't have to tell me, Minami..."
    mike.say "I'm totally aware of just how hot you are!"
    "Minami pulls a ironic grin and shakes her head."
    "Then she lands a playful slap on my shoulder."
    minami.say "Oh, that's SO lame!"
    minami.say "Come on..."
    minami.say "You can buy me an ice-cream to make up for it."
    "Minami takes hold of my hand and leads me over to the ice-cream stand."
    "There's no queue when we get there, so we get served straight away."
    mike.say "Can I get two ice-creams, please?"
    minami.say "Actually, forget about buying two."
    minami.say "Just get a large one, big bro."
    minami.say "Then we can share."
    "I shrug and nod, doing as Minami says."
    "But it's only when we walk away from the stand that I really get it."
    "Because that's when Minami leans in real close to lick the ice-cream."
    "So close that our cheeks are practically touching the whole time."
    "Which makes eating the ice-cream so much more intimate and enjoyable."
    $ minami.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
