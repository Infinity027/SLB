label morgan_date_amusement_park_male:
    scene bg amusement
    show morgan normal
    with fade
    "Getting to take Morgan to the Amusement Park feel great on so many levels."
    "On the surface it's just a blast to be able to do something so much fun with her."
    "But deeper down I kind of feel like this is a chance to make up for lost time."
    "I still feel like such a jerk for not realising she was a girl for so many years."
    "Sure, we had some fun together as kids when I was sure she was a guy."
    "But the good times we're having together now are so much better because I know the real her."
    "And it seems like my positive vibes are plain to see."
    show morgan happy
    "Because Morgan looks at me and starts to chuckle as we're walking in through the gate."
    show morgan normal
    mike.say "Hey!"
    mike.say "What's so funny, Morgan?"
    "Morgan shakes her head and gives me a sweet smile."
    "Letting me know that it's affectionate amusement she's feeling."
    show morgan talkative
    if morgan.male >= 66:
        morgan.say "I'm laughing at you, ya big dope!"
        morgan.say "You look like the biggest kid in the world right now."
    elif morgan.male >= 33:
        morgan.say "Don't be offended, [hero.name]."
        morgan.say "You're just adorable when you're in this kind of mood."
    else:
        morgan.say "Oh, I wasn't laughing at you, [hero.name]."
        morgan.say "It just makes me happy to see that you're happy!"
    show morgan normal
    "I guess that's a pretty good explanation, all things considered."
    "So I nod and gesture for Morgan to follow me in through the gates."
    mike.say "I'm in such a good mood because we're going to have a great time, Morgan."
    mike.say "You just wait and see, okay?"
    "Morgan nods, and I feel her take hold of my hand."
    "She gives it a squeeze too, which only makes me feel better."
    "And I'm sure that this is going to the best visit to the Amusement Park yet."
    return

label morgan_date_ferris_wheel_male:
    "I'm still kind of feeling that nostalgia kick I mentioned before."
    "So when I see the Ferris Wheel, it seems like just the thing to me."
    mike.say "Hey, Morgan..."
    mike.say "Let's ride the Ferris Wheel!"
    "Morgan turns in my direction as I say all of this."
    "Which means that she's looking at the Ferris Wheel too."
    morgan.say "The Ferris Wheel?"
    if morgan.male >= 66:
        morgan.say "Sure, if that's what you really want."
    elif morgan.male >= 33:
        morgan.say "Yeah, why not."
    else:
        morgan.say "Oh, I haven't been on one of those since forever!"
    "That's good enough for me, and so I hurry over to the line."
    "Morgan follows close on my heel, and together we join the queue."
    "Luckily for us, the Ferris Wheel is one of the less popular rides."
    "So the line moves quickly and we're soon sitting in a gondola."
    "As soon as the safety-bar comes down, we begin to ascend."
    "And with every second that passes, the view gets better."
    "By the time we get to the top and the ride stops, I can see for miles around."
    mike.say "Pretty impressive, huh?"
    if morgan.male >= 66:
        morgan.say "Not too bad!"
    elif morgan.male >= 33:
        morgan.say "I guess so."
    else:
        morgan.say "Oh my - we're SO high up!"
    "We spend the rest of the time on the ride admiring the view."
    "And then it starts moving again, and we descend slowly to the ground."
    $ morgan.love += 1
    $ game.active_date.score += 10
    return

label morgan_date_merry_go_round_male:
    mike.say "Hey, Morgan..."
    mike.say "They still have an old-fashioned Merry-Go-Round!"
    "Morgan nods as I point out the ride to her."
    if morgan.male >= 66:
        morgan.say "Geez - I haven't seen one of those in a long time!"
    elif morgan.male >= 33:
        morgan.say "Wow - I didn't think there were any of those left!"
    else:
        morgan.say "Goodness - just like the ones I remember from being a kid!"
    morgan.say "Do you want to ride it?"
    "I shrug as Morgan asks me the question."
    "I wasn't seriously considering it before now."
    "But if Morgan's interested in riding it, then so am I."
    mike.say "I'm up for it, Morgan."
    mike.say "Plus the queue looks short."
    mike.say "Shouldn't take long for us to get on it."
    "Morgan nods in agreement, and we walk over to the ride."
    "We join the back of the queue and quickly make it to the front."
    "Then we climb onto the Merry-Go-Round."
    "Picking where we want to sit, we hold on tight."
    "And when the ride starts to move, that's a good thing."
    "Because the Merry-Go-Round moves far faster than I was expecting."
    "But that's balanced out by the fact that the ride's not too long."
    "Which is probably a good thing, because it keeps the thing from getting old."
    "And it means that we're still feeling the nostalgia buzz as we get off too."
    $ morgan.love += 1
    $ game.active_date.score += 10
    return

label morgan_date_haunted_house_male:
    mike.say "Oh man..."
    mike.say "The Haunted House looks amazing!"
    mike.say "Come on, Morgan - we have to do the Haunted House!"
    "I don't even wait for Morgan to say anything in return."
    "Instead I just start walking straight over to the Haunted House."
    "It's only when I reach the queue that I realise she's not beside me."
    "And turning around, I see that she's actually hanging back."
    mike.say "What's the matter, Morgan?"
    mike.say "Don't you want to do this ride?"
    morgan.say "I don't know, [hero.name]..."
    if morgan.male >= 66:
        morgan.say "All that spooky stuff was never my kind of thing, you know?"
    elif morgan.male >= 33:
        morgan.say "I never really liked horror movies!"
    else:
        morgan.say "It looks really scary!"
    "If this had been any other ride, then I'd have backed right off."
    "But I always loved the Haunted House so much."
    "And I'm sure that Morgan's not as reluctant as she claims."
    mike.say "Trust me, Morgan..."
    mike.say "It'll be fine."
    mike.say "There things are never as scary as they seem."
    "Morgan doesn't look totally convinced."
    "But she nods and joins me in the queue all the same."
    "I spend the rest of the time we're in the queue trying to reassure her."
    "And I'm feeling pretty confident I've succeeded as we walk into the Haunted House."
    "So when the first scare hits, I'm totally unprepared for Morgan's reaction."
    if morgan.male >= 66:
        morgan.say "What the actual fuck?!?"
    elif morgan.male >= 33:
        morgan.say "OH GOD!"
    else:
        morgan.say "EEK!"
    "Morgan grabs hold of my hand and proceeds to run for all she's worth."
    "This means that I get dragged along behind her through the Haunted House."
    "The whole walk through the ride is reduced to a blur of sounds and images."
    "And she doesn't stop until we shoot out of the exit."
    "Afterwards, while Morgan puts her head between her knees, I take stock."
    "Because I seriously think I need to listen the next time she objects to something like this!"
    $ morgan.love -= 2
    $ game.active_date.score -= 20
    return

label morgan_date_love_boat_male:
    "As soon as I lay eyes on the Love Boat, I know that we have to ride it."
    "But I also know that I need to be clever in terms of how I pitch it to Morgan."
    "Like, I can't just come out and say that I want to ride it."
    "Because she'll just call me on it..."
    morgan.say "Do you want to ride it?"
    "Morgan's question catches me totally off-guard."
    "And she rerails my train of thought too."
    mike.say "Huh?"
    mike.say "Ride what?"
    "Morgan shoots me a wry smile and points at the Love Boat."
    if morgan.male >= 66:
        morgan.say "Don't be such a pussy - just ask me already!"
    elif morgan.male >= 33:
        morgan.say "You can ask me to ride the Love Boat, if that's what you want?"
    else:
        morgan.say "Why don't you just ask me to ride it - because I might say yes!"
    mike.say "You..."
    mike.say "You want to ride the Love Boat?"
    "By way of an answer, Morgan takes hold of my hand."
    "And then she walks me over to where the line begins."
    "After that we stand patiently in line until our turn comes round."
    "Then we step into the waiting boat, which soon sails into the tunnel."
    "What follows is an extremely pleasant few minutes alone with Morgan."
    "A time in which I get to truly understand the wonders of the Love Boat."
    "And once we emerge from the other end, I feel like a new man."
    "More relaxed and laid back than I've felt in a very long time."
    $ morgan.love += 2
    $ game.active_date.score += 20
    return

label morgan_date_hedge_maze_male:
    mike.say "Shall we do the Hedge Maze next?"
    mike.say "Give our brains a well-needed workout?"
    "Morgan glances over at the entrance to the Hedge Maze."
    "But the look on her face isn't one of enthusiasm."
    if morgan.male >= 66:
        morgan.say "Hey - my brain's in pretty good shape already!"
    elif morgan.male >= 33:
        morgan.say "I don't know - I never got on with that kind of thing."
    else:
        morgan.say "I can think of better ways to train my brain!"
    mike.say "Oh come on, Morgan..."
    mike.say "It'll be fun."
    mike.say "And it won't eat up too much time either."
    morgan.say "Okay, okay..."
    morgan.say "But this was your idea, remember!"
    "Morgan and I join the queue and quickly move towards the front."
    "And once we're in there, we find ourselves flanked by high hedges."
    "It's surprisingly dark inside the maze and it looks pretty intimidating."
    "But I tell myself that's just for effect, and start wandering around."
    mike.say "I think it's this way, Morgan..."
    mike.say "Come on - try to keep up!"
    if morgan.male >= 66:
        morgan.say "Don't tell me what to do!"
        morgan.say "Urgh...I hate this so much!"
    elif morgan.male >= 33:
        morgan.say "I'm doing the best I can!"
        morgan.say "I never wanted to come in here in the first place, remember?"
    else:
        morgan.say "[hero.name], I don't like this..."
        morgan.say "Hurry up and find the way out!"
    "I don't need to be told twice."
    "So I step up my efforts to get us out of the maze."
    "And it's only once I do that I feel safe from Morgan's ire."
    "Next time I'll be sure to listen to her when she objects to something."
    $ morgan.love -= 2
    $ game.active_date.score -= 20
    return

label morgan_date_amusement_ice_cream_male:
    mike.say "Phew..."
    mike.say "When did the weather turn so hot, Morgan?"
    mike.say "We should grab an ice-cream, try to cool down, yeah?"
    "Morgan looks around as I suggest we get an ice-cream."
    "And I can see that she's already fanning herself with one hand."
    if morgan.male >= 66:
        morgan.say "I could go for an ice-cream, if you want..."
        morgan.say "But it's not like I'm that hot, really."
    elif morgan.male >= 33:
        morgan.say "I hear you, [hero.name].."
        morgan.say "Let's go get one, pronto!"
    else:
        morgan.say "Ooh, that sounds like a good idea, [hero.name]..."
        morgan.say "Shall we go and get one?"
    "I nod and take hold of Morgan's hand."
    "Then I lead her through the crowds to the ice-cream stand."
    "Soon enough we're standing in line, waiting to be served."
    "And once the server has our order, it's not long before we get the ice-creams."
    if morgan.male >= 66:
        morgan.say "Yes!"
        morgan.say "This is gonna be so sweet."
    elif morgan.male >= 33:
        morgan.say "Oh, man..."
        morgan.say "I've been waiting for this!"
    else:
        morgan.say "Yay!"
        morgan.say "I totally love ice-cream."
    "I'm licking away at my own ice-cream the whole time."
    "But I can't help taking time to glance over at Morgan too."
    "Enjoying the sight of her eating her ice-cream almost as much as I am the taste of mine."
    $ morgan.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
