label cassidy_date_amusement_park_male:
    scene bg amusement
    show cassidy b upset
    with fade
    "It can be hard to come up with a plan when you're taking a girl like Cassidy out."
    "Her dad's so rich that she can probably do whatever takes her fancy whenever she wants."
    "So I'm never going to be able to impress her by flashing my far less impressive wad of cash."
    "And that's why I'm trying to make my time with Cassidy genuinely fun and memorable."
    "Because that's the kind of good impression that money can't buy, right?"
    show cassidy b annoyed
    cassidy.say "Urgh..."
    cassidy.say "I still don't know why you wanted us to come here, [hero.name]!"
    show cassidy b sad
    "Although right now I'm beginning to wonder why I'd even bother!"
    mike.say "It's the Amusement Park, Cassidy..."
    mike.say "Everyone loves this place, don't they?"
    show cassidy b upset
    "Cassidy shoots me a withering look as we walk in through the gates."
    "But at least she's not refusing to go inside, so that counts for something."
    show cassidy b normal
    cassidy.say "We never came here much when I was a little girl."
    cassidy.say "Daddy was always at work and mummy was too busy to bring me."
    cassidy.say "Anyway, we hired more impressive stuff than this to have in the garden at my birthday parties!"
    show cassidy b upset
    "I'm not sure if Cassidy is telling the truth."
    "But I decide that it's better to leave it alone."
    "Even if only for the sake of getting her into the park."
    return

label cassidy_date_ferris_wheel_male:
    "I see the curve of the Ferris Wheel, standing out above the other rides."
    "And in that moment I know that we have to ride on it."
    "It's a classic ride, one that should really get Cassidy into the spirit of things."
    mike.say "Let's ride the Ferris Wheel, Cassidy..."
    mike.say "No visit to the Amusement Park is complete without that."
    "Cassidy allows me to lead her over to where the queue begins."
    "But I can tell from the look on her face that she's not impressed."
    cassidy.say "Hurmph..."
    cassidy.say "Do we have to wait in line with everyone else?"
    cassidy.say "Isn't there like, a VIP line or something?"
    "I can see people in the queue shooting us annoyed glances."
    "But luckily for me, things move pretty quickly."
    "And so we're soon getting onto the Ferris Wheel."
    "Cassidy keeps quiet as the safety bar comes down and we start to rise."
    "I'm waiting for her to notice the view we're being treated to."
    "Which is getting better by the second."
    "But even when we reach the top and the ride stops, she's still silent."
    mike.say "Aren't you going to say anything, Cassidy?"
    mike.say "Don't you like the view from up here?"
    cassidy.say "It's not as impressive as the one from Daddy's office!"
    "I open my mouth to say something cutting in return."
    "But then I bite my tongue for the sake of keeping the peace."
    "And my mood goes down at the same time as the Ferris Wheel does."
    $ cassidy.love -= 2
    $ game.active_date.score -= 20
    return

label cassidy_date_merry_go_round_male:
    cassidy.say "Oh..."
    cassidy.say "Those are such pretty ponies!"
    "For a moment I don't actually realise that it's Cassidy saying those words."
    "I'm so used to her pissing on everything at the park I assume it's someone else."
    "But then I look around and see her staring at the Merry-Go-Round."
    "And her eyes are wide with what looks like genuine wonder."
    mike.say "You mean the ones on the Merry-Go-Round?"
    "Cassidy nods as she walks closer to the ride."
    cassidy.say "I always wanted a pony like that when I was little."
    cassidy.say "But Daddy wouldn't buy me one!"
    "Now I am finding it hard to believe what I'm hearing."
    "I'm amazed that Dwayne would deny his little princess a pony!"
    mike.say "Well..."
    mike.say "I can't buy you a real one, Cassidy..."
    mike.say "But I can certainly take you for a ride on one of those."
    "Cassidy nods eagerly, a huge smile spreading across her face."
    "She holds out her hand for me to take, and I lead her over to the ride."
    "As it's one of the older attractions, the queue is pretty short."
    "So we're soon picking out our mounts for the ride."
    "Once the ride starts up, it's tame by modern standards."
    "And I look across at Cassidy, expecting to see her grinning with delight."
    "Instead I see that she's clinging onto her pony, eyes wide with surprise."
    mike.say "Cassidy..."
    mike.say "Are you okay?!?"
    cassidy.say "Y...yeah..."
    cassidy.say "I'm okay..."
    cassidy.say "This is scary...but, like...good scary!"
    "I feel a sense of relief wash over me."
    "Then I settle back to enjoy the rest of the ride."
    "Secure in the knowledge that Cassidy is okay."
    $ cassidy.love += 4
    $ game.active_date.score += 40
    return

label cassidy_date_haunted_house_male:
    "As soon as I hear the sound-effects coming from the Haunted House, I make straight for it."
    "It's one of my all-time favourite rides, and no visit to the park is complete without it."
    "In fact I'm so eager to get to it that I almost forget I'm holding onto Cassidy's hand."
    "Only remembering when she protests as I pull her through the crowds."
    cassidy.say "Hey!"
    cassidy.say "Slow the hell down!"
    cassidy.say "What's the rush all of a sudden?"
    mike.say "The Haunted House, Cassidy..."
    mike.say "It's my favourite ride!"
    "Cassidy casts her eyes over the frontage as we join the queue."
    "And I can tell that she's not impressed by what she sees."
    cassidy.say "Looks pretty tacky to me."
    cassidy.say "I don't think I'm going to like this."
    mike.say "Just give it a chance, okay?"
    mike.say "Getting scared is a real thrill!"
    "Once we're inside the Haunted House, I'm in my element."
    "I know the effects are cheap and the decor is cheesy."
    "But I still love it as much as ever."
    "Unfortunately the same can't be said for Cassidy."
    "She trudges along behind be, tutting and muttering to herself."
    "I don't think she jumps or lets out a scream even once."
    "Though I do the best I can to ignore her."
    "Which leaves me free to enjoy the experience myself."
    $ cassidy.love -= 1
    $ game.active_date.score -= 10
    return

label cassidy_date_love_boat_male:
    "Spotting the Love Boat ride, I wonder if Cassidy would appreciate a change of pace."
    "Okay, okay...it's more like I figure we could get up to some fun stuff in the darkness."
    "But whatever my motivations, I have to sell the idea to Cassidy first."
    "Which is going to be easier said than done!"
    mike.say "You want to ride the Love Boat, Cassidy?"
    cassidy.say "Love Boat?"
    cassidy.say "What's that?"
    mike.say "You sit in a little boat and it sails through a tunnel."
    mike.say "Just you and me - it's very romantic."
    cassidy.say "Oh..."
    cassidy.say "That sounds just like the gondola rides in Venice!"
    cassidy.say "Let's go do that."
    "Keen to capitalise on Cassidy's enthusiasm, I hustle her over to the ride."
    "We join the queue and soon make it all the way to the front."
    "And once we're in the boat, Cassidy looks around with a frown."
    cassidy.say "Wait a minute..."
    cassidy.say "This isn't like Venice at all."
    cassidy.say "It's just a grotty little boat in a grotty little tunnel!"
    "And that kind of sets the scene for the rest of the ride."
    "I'm forced to sit there while Cassidy reels off her multitudinous complaints."
    "So much so that I'm tempted to jump into the water and make a break for freedom."
    $ cassidy.love -= 2
    $ game.active_date.score -= 20
    return

label cassidy_date_hedge_maze_male:
    mike.say "I think we should try the Hedge Maze, Cassidy."
    mike.say "I hear that it's really hard to find your way back out of there!"
    "Cassidy rolls her eyes as we join the queue for the maze."
    cassidy.say "If it's so hard, why would you want to do it?"
    cassidy.say "I mean, what's the point of getting lost on purpose?"
    "All I can do is shrug and try to ignore the question as we queue up."
    "And once we're inside, I use the maze itself as a distraction."
    "I'm following my instincts as I wind around every corner."
    "With Cassidy trailing behind me, still complaining like before."
    cassidy.say "There hedges are so boring!"
    cassidy.say "We have far better ones in the gardens back home."
    cassidy.say "And you can't get lost around them either!"
    cassidy.say "Hey!"
    cassidy.say "Are you even listening to me?!?"
    "More than once I'm tempted to try giving Cassidy the slip."
    "To leave her trying to find her own way out of the maze."
    "But somehow I manage to resist, instead ignoring her as best I can."
    $ cassidy.love -= 2
    $ game.active_date.score -= 20
    return

label cassidy_date_amusement_ice_cream_male:
    mike.say "It's getting pretty hot, Cassidy..."
    mike.say "You want to take a break?"
    mike.say "Maybe grab an ice-cream?"
    "Cassidy nods the instant I ask the question."
    "And she grabs hold of my hand a moment later."
    cassidy.say "That's a great idea, [hero.name]!"
    cassidy.say "I never had one of those before."
    "I can't help being surprised by Cassidy's admission."
    "And I find myself shaking my head as we stand in line."
    mike.say "Are you serious, Cassidy?"
    mike.say "You never had an ice-cream before?"
    mike.say "Not in your entire life?"
    "Cassidy rolls her eyes and gives me a playful shove."
    cassidy.say "Oh no, of course not!"
    cassidy.say "I've had ice-cream before, silly..."
    cassidy.say "Just never from a place like this."
    cassidy.say "When daddy got me ice-cream, it was always expensive and fancy."
    cassidy.say "But this way looks more...I don't know..."
    cassidy.say "Maybe more cheap, but more exciting!"
    "I can't help staring sideways at Cassidy as we get our ice-creams."
    "So she sees me as being cheaper than her dad."
    "But at the same time I'm apparently more exciting."
    "Which has to be a good thing, right?"
    $ cassidy.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
