label jack_date_amusement_park_female:
    scene bg amusement
    show jack
    with fade
    "Usually I'm the one that's champing at the bit to get into the Amusement Park."
    "So I'm used to having to look over my shoulder as I drag my date along behind me."
    "But this is my first time at the park with Jack, and it looks like I've met my match."
    "Because the rush to get through the gates is pretty much turning into a race!"
    show jack smile
    jack.say "Hey, [hero.name]..."
    jack.say "Why so slow?"
    show jack normal
    bree.say "Hah!"
    bree.say "Nice try, Jack..."
    bree.say "But that won't work on me!"
    "Both Jack and I are running as fast as we possibly can."
    "At the same time we're weaving around everyone that happens to be in our path."
    "And our words are in danger of becoming panting gasps as we suck in our breath."
    "Leaning forwards, I force one last burst of speed out of my already tired legs."
    "Which I'm sure puts me inside of the gates a few mere seconds before Jack."
    bree.say "Yes!"
    bree.say "I did it..."
    bree.say "Suck on that!"
    show jack sad
    "Jack's leaning forwards, hands on his knees and gasping for breath."
    "But somehow he still manages to find the energy to be outraged by my victory celebrations."
    show jack whining
    jack.say "Urgh..."
    jack.say "What are you..."
    jack.say "What are you talking about?"
    show jack happy
    jack.say "I so beat you!"
    show jack normal
    "I shake my head, trying to laugh off Jack's objections."
    bree.say "Dream on, Jack..."
    bree.say "You were miles behind me back there."
    show jack smile
    jack.say "I don't know what you're trying to pull, [hero.name]..."
    jack.say "But I'm not above asking the guy on the gate for his opinion."
    show jack normal
    "That seems to be one step too far for me."
    "So I hold up a hand to stop Jack from saying any more."
    bree.say "Okay, okay..."
    bree.say "Let's get some perspective here."
    bree.say "We should be having fun on the rides."
    bree.say "Not arguing over silly stuff like this."
    "Jack nods."
    show jack smile
    jack.say "You're right, [hero.name]..."
    show jack happy
    jack.say "Bet I can make it onto the first ride before you!"
    show jack happy
    bree.say "WHAT?!?"
    bree.say "There's no way that's going to happen!"
    "Jack hurries off into the park, weaving through the crowds."
    "And I hurry after him, determined not to be outdone."
    return

label jack_date_ferris_wheel_female:
    jack.say "What about the Ferris Wheel?"
    jack.say "We could ride that?"
    "I look up at the Ferris Wheel towering above us."
    "And then I take look at the queue below it too."
    bree.say "Huh..."
    bree.say "Not the most exciting thing in the park."
    bree.say "But the queue's short..."
    bree.say "So it kind of balances out."
    show jack wink
    "Jack and I exchange a nod of agreement."
    "Then we walk over to join the back of the line."
    show jack smile
    "It's not long before we make it to the front of the queue."
    "So we step into the waiting gondola and sit down."
    "Once the safety-bar is in place, we start to rise."
    "As soon as the wheel clears the level of the rides, everything changes."
    "We're treated to a view that just gets better by the second."
    "And when the wheel stops as we reach the top, it's just incredible."
    jack.say "Oh man..."
    jack.say "I think I can see my house from here!"
    jack.say "Look, [hero.name] - right over there."
    bree.say "I see it, Jack."
    bree.say "Mine's over here..."
    bree.say "You see?"
    "Jack strains to see where I'm pointing."
    jack.say "Oh wow..."
    jack.say "There's a lot of lights on at your place!"
    bree.say "That'll be [mike.name]."
    bree.say "He wanders from one room to the next..."
    bree.say "Always leaving the lights on behind him."
    jack.say "Ha, ha..."
    jack.say "Yeah, he can be a jerk!"
    "We keep on chatting as the wheel brings us back down to earth."
    "And it feels nice to be able to take some time out for a while."
    "Especially in a place as loud and manic as the Amusement Park."
    $ jack.love += 1
    $ game.active_date.score += 10
    return

label jack_date_merry_go_round_female:
    show jack normal
    bree.say "That's a really old Merry-Go-Round!"
    bree.say "Like, one of the oldest I've ever seen."
    bree.say "I wonder how they manage to keep it going?"
    "Jack shakes his head at my question."
    "But I don't know if that's because he doesn't know the answer."
    "Or if he's just choosing to ignore it as he makes straight for the ride."
    jack.say "Does any of that matter, [hero.name]?"
    jack.say "We're still going to ride it."
    jack.say "Aren't we?"
    "Now it's my turn to be presented with a question I'm not ready for."
    "And the result is that I find myself being bundles onto the ride."
    "Because I'm still not really sire what's going on around me."
    bree.say "You..."
    bree.say "You really want to ride this?"
    bree.say "I thought it was for kids?"
    "Jack jumps onto one of the horses and pats the one next to his."
    "So I sit down, still waiting for an answer to my question."
    jack.say "No way, [hero.name]!"
    jack.say "This ride's for kids of all ages!"
    "The ride begins to move as Jack finishes speaking."
    "And it starts with a lurch too."
    "So I find myself hanging on for dear life."
    "Jack seems to interpret this as me getting into the spirit of the ride."
    "He does the same thing, grabbing the pole and bouncing up and down."
    "He's laughing and whooping, almost like he's pretending to be a cowboy."
    jack.say "Whoo!"
    jack.say "Ha, ha..."
    jack.say "Yippee!"
    "It's impossible to keep a straight face as Jack acts like a clown."
    "And I find myself laughing along with him throughout the ride."
    "When it comes to a stop and we get off, he finally stops acting the fool."
    "And I can see a look of embarrassment spreading over his face."
    jack.say "Erm..."
    jack.say "Sorry, [hero.name]..."
    jack.say "I guess I got a little carried away!"
    show jack perv
    "By way of answer, I grab hold of his arm and pull him close to me."
    "This seems to ease Jack's embarrassment as we walk away together."
    $ jack.love += 2
    $ game.active_date.score += 20
    return

label jack_date_haunted_house_female:
    "Jack and I are walking through the crowds, talking about everything and nothing."
    "But our conversation is interrupted by the sound of a blood-curdling scream."
    show jack surprised
    jack.say "Argh!"
    jack.say "What was that?!?"
    "I can't help chuckling at Jack's reaction."
    "Because I know exactly what we just heard."
    bree.say "Relax, Jack..."
    bree.say "That was just the Haunted House."
    bree.say "You see?"
    bree.say "Right over there."
    "Jack looks in the direction I'm pointing and sees the Haunted House."
    "It's the typical affair of spooky stuff and special effects."
    "But oddly he doesn't seem too comforted by the sight."
    jack.say "Oh..."
    jack.say "Oh yeah, of course..."
    jack.say "I kind of knew it was just the Haunted House."
    "I'm not exactly convinced by Jack's reaction."
    "But now that I've seen the Haunted House myself, I'm itching to get in there."
    "So I make straight for it, assuming that Jack's going to follow me."
    jack.say "[hero.name]..."
    jack.say "Where are you going?"
    bree.say "To join the queue of course."
    bree.say "Come on, Jack!"
    "Jack begins to follow me."
    "But I can see that he's pretty nervous."
    bree.say "Wait a minute..."
    bree.say "You're not scared, are you?"
    jack.say "What?!?"
    jack.say "Me, scared?"
    jack.say "That's nonsense, [hero.name]!"
    show jack normal
    "As if to prove his point, Jack strides over to join the queue."
    "And he manages to keep looking confident right until it's our turn to go in."
    "Then I see him take a deep breath, as if steeling himself for what lies ahead."
    "I walk into the Haunted House, ready to be scared in a good way."
    "But the first time something jumps out at us, Jack's true nature is revealed."
    jack.say "OH MY GOD!"
    jack.say "[hero.name], save me!"
    "I spend the rest of the time in there with Jack cowering behind me."
    "And he shrieks at almost everything in the place too!"
    "By the time we get out again, he's a nervous wreck."
    "Shuddering and flinching as he jumps at the slightest sound."
    $ jack.love -= 2
    $ game.active_date.score -= 20
    return

label jack_date_love_boat_female:
    bree.say "We should ride the Love Boat next."
    bree.say "Don't you think?"
    show jack sad
    "I make a point of nodding towards the ride in question."
    "Sure that Jack's going to be up for riding it with me."
    "But instead, he shakes his head and points at the other rides."
    jack.say "No way, [hero.name]!"
    jack.say "That ride's old and boring."
    jack.say "I want to ride something new and exciting."
    jack.say "Like the..."
    jack.say "Oof!"
    show jack surprised
    "Jack grunts as I take him firmly by the hand and start to walk."
    "And as I pull him towards the Love Boat, he seems to finally get it."
    jack.say "Oh..."
    jack.say "Okay, okay..."
    jack.say "I get it, [hero.name], I get it!"
    "Without a word, I almost toss him into the waiting boat."
    "And then I jump in beside him, making it rock dangerously."
    jack.say "Whoa..."
    bree.say "Don't be such a pussy, Jack!"
    bree.say "Now get over here..."
    bree.say "And show me what kind of a man you really are."
    "I'm pleased to say that as we sail into the gloom, Jack does as he's told."
    "And I reap the benefits of that for the rest of the ride."
    $ jack.love += 1
    $ game.active_date.score += 10
    return

label jack_date_hedge_maze_female:
    jack.say "You want to do the Hedge Maze, [hero.name]?"
    show jack surprised
    "I look up at the question, kind of taken by surprise."
    "The Hedge Maze wasn't one of the attractions I had on my list."
    "But there's nothing to turn me off the idea of doing it."
    bree.say "You sure you want to do that one, Jack?"
    bree.say "It's just a bunch of hedges!"
    "Jack shakes his head at this."
    jack.say "It's much more than that..."
    jack.say "It's a classic mental challenge."
    jack.say "A three dimensional puzzle."
    bree.say "Okay, Jack..."
    show jack normal
    bree.say "No need give me the hard-sell."
    bree.say "Let's check it out."
    "The Hedge Maze doesn't seem to be one of the more popular attractions."
    "This means that the queue is short and we're soon at the front of the line."
    "We step inside, finding ourselves surrounded by towering hedges on two sides."
    "And from there we do the best we can to navigate the confusing passages of the maze."
    "I have to admit that it's harder than I expected it to be."
    "More than once I find myself totally lost and unsure of where to go next."
    "So I'm thankful that Jack seems to have a better sense of direction than me."
    "In the end he's the one that actually finds the way out."
    "And I'm glad to be out of the place."
    "Because I found it more frustrating than fun."
    $ jack.love += 1
    $ game.active_date.score += 10
    return

label jack_date_amusement_ice_cream_female:
    bree.say "Hey, Jack..."
    bree.say "Do you think we should..."
    "Before I can finish what I was going to say, Jack jumps in and cuts me off."
    jack.say "Go get ice-cream?!?"
    jack.say "[hero.name], that's totally amazing..."
    jack.say "You literally just read my mind!"
    "I look from Jack to the ice-cream stand, right there in front of us."
    "And for the life of me, I can't actually think what else I could have about to say."
    "Because there's literally nothing else within sight but other amusement park patrons."
    bree.say "Erm..."
    bree.say "Yeah, Jack..."
    bree.say "But I don't think you were reading my..."
    bree.say "WHOA!"
    "Jack cuts me off for a second time."
    "But on this occasion it's because he grabs me by the hand."
    "And the very next moment rushes off towards the ice-cream stand."
    "His grip on me so firm that I have no choice but to follow in his wake."
    "As soon as we're there, Jack's waving to get the server's attention."
    jack.say "Hi..."
    jack.say "Hey..."
    jack.say "I'll have one of those!"
    jack.say "And what about you, [hero.name]?"
    jack.say "What do you want?"
    "I'm still kind of disoriented from being dragged to the ice-cream stand."
    "So I find myself shrugging and shaking my head."
    bree.say "I don't know, Jack..."
    bree.say "I guess I'll just have whatever you're having?"
    jack.say "Great choice, [hero.name]!"
    "Soon enough we're walking away with our ice-creams."
    "And I'm still lost for words as we do so."
    "Though this time it's more from the tottering tower of ice-cream in my hand."
    "I'm staring at it in fear that I'll lose my balance any moment."
    "And that I'll send the entire thing tumbling to the ground."
    $ jack.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
