label hanna_date_amusement_park_male:
    scene bg amusement
    with fade
    "As always, I'm excited to be going to the amusement park."
    "In fact I'm already thinking about what rides I want to hit."
    "That and the best route to take in order to maximise my time here."
    "Which is why it comes as a surprise to me when I look around and find I'm alone."
    "I mean, I have come to the park on my own before and it's never been an issue."
    "But right now I know that I'm not supposed to be on my own."
    "Because the last time I checked, my date was right by my side!"
    mike.say "Hanna..."
    mike.say "Where's you go?"
    "Turning around, the mystery is soon solved."
    show hanna with easeinleft
    "As I see Hanna walking along a few paces behind me."
    mike.say "There you are!"
    mike.say "Come on, Hanna, hurry up!"
    show hanna surprised
    hanna.say "huh?"
    hanna.say "What's the hurry, [hero.name]?"
    hanna.say "Is the park about to close or something?"
    show hanna normal
    mike.say "Of course not, we've got plenty of time."
    mike.say "But we need to make the most of it all the same!"
    show hanna confused
    "Hanna frowns a little, like she doesn't totally agree with me."
    show hanna normal
    "But she nods her head and picks up the pace all the same."
    "I feel worried that she might not be as up for the Amusement park as I am."
    "But I reassure myself that her mood will change once we're inside."
    "Because who can resist the thrill of a place like this?"
    return

label hanna_date_ferris_wheel_male:
    mike.say "Let's ride the Ferris Wheel, Hanna."
    mike.say "That one right over there."
    "Hanna's eyes follow the direction that I'm pointing in."
    "And as soon as she spots the ride, she shrugs."
    hanna.say "Sure, why not."
    hanna.say "I haven't been on one of those things in years."
    "Hanna doesn't sound too excited at the prospect."
    "But at least she didn't say no."
    "Which has to count for something, right?"
    "Deciding not to look a gift horse in the mouth, I lead her straight over there."
    "We join the back of the queue and soon find that it's moving pretty quickly."
    "Which means that we're at the front in what feels like record time."
    "I motion for Hanna to step into the gondola first."
    "And then I hop in after her, sitting down before the safety bar descends."
    "She has a smile on her face as we start to ascend."
    "My eyes keep on darting between the view and Hanna's expression."
    "But it never seems to change from mild interest to anything more intense."
    "Once we reach the top of the wheel, the ride stops for a moment."
    mike.say "Quite a view, huh?"
    hanna.say "I guess you can't argue with that."
    "I'm waiting for Hanna to say more."
    "But instead she remains silent as the ride starts to move again."
    "So Hanna didn't like that ride - but she didn't hate it either."
    "Which means that things are pretty much even."
    "And I'll have to try harder with the next choice of ride."
    $ hanna.love -= 0
    $ game.active_date.score -= 0
    return

label hanna_date_merry_go_round_male:
    "As soon as I see the Merry-Go-Round, I know that we have to ride it."
    "I mean sure, it's not the most modern or exciting ride in the park."
    "But it's a classic, one that everybody remembers from their childhood."
    "So riding it should really hit Hanna in the nostalgia spot."
    "And once that happens, then she's sure to start having some serious fun."
    mike.say "Hey, Hanna..."
    mike.say "I want to take you on the Merry-Go-Round next."
    hanna.say "The Merry-Go-Round?"
    hanna.say "Are you sure?!?"
    mike.say "Trust me, it's seriously under-rated."
    "Hanna doesn't seem convinced."
    "But she nods in agreement all the same."
    "And she offers no resistance as I steer her towards the ride."
    "It's not exactly the most popular attraction in the park."
    "Which means that the queue is small and moves quickly."
    "So we soon find ourselves climbing into our chosen spots."
    "As the ride starts to move, I keep on stealing glances at Hanna."
    "Before she looked pretty neutral, but now that's changed."
    "Because each time I look in her direction, she seems even more unhappy."
    mike.say "What's the matter, Hanna?"
    mike.say "Is the ride going too fast for you?"
    hanna.say "Too fast!"
    hanna.say "Ha!"
    hanna.say "It feels like it hasn't even got started yet."
    hanna.say "Urgh...this is SO boring!"
    hanna.say "I can't believe I let you talk me into riding it."
    $ hanna.love -= 2
    $ game.active_date.score -= 20
    return

label hanna_date_haunted_house_male:
    "The moment that I hear the familiar wailing sound, I'm sold."
    "The Haunted House has always been one of my absolute favourite attractions."
    "And now I get the chance to share it with Hanna too!"
    mike.say "Hanna..."
    mike.say "Hanna..."
    hanna.say "Let me guess..."
    hanna.say "You just have to go do the Haunted House?"
    "I nod eagerly, not even bothering to reply with words."
    hanna.say "Okay, whatever..."
    hanna.say "WHOA..."
    "Without giving her the chance to say another word, I leap into action."
    "I grab Hanna by the hand and pull her towards the Haunted House."
    "And I'm so excited that I hardly remember the time we're standing in line."
    "To me it feels like the very next moment we're inside and enjoying ourselves."
    "Or to be more precise, I'm enjoying myself."
    "I keep trying to check on how Hanna's doing."
    "And when I can manage it, I notice that she doesn't seem impressed."
    "It's not like she's annoyed or desperate to get out of the place."
    "But she really doesn't look like she's having a good time either."
    "Once we walk out of the exit, I make a point of finding out more."
    mike.say "You didn't seem to jump or scream once, Hanna!"
    mike.say "What's up with that?"
    "Hanna shrugs and makes a non-committal sound."
    hanna.say "Ah..."
    hanna.say "I don't know, [hero.name]."
    hanna.say "I just never found that kind of thing scary."
    hanna.say "I guess they're just too tacky and predictable!"
    $ hanna.love += 0
    $ game.active_date.score += 0
    return

label hanna_date_love_boat_male:
    "Spotting the Love Boat up ahead, I feel myself getting an idea."
    "A ride as quiet and sedate as that might be just what Hanna needs."
    "The chance to get away from the crowds and really relax for a while."
    "Plus it has the added advantage of giving us some private time together."
    "So it's a winner on all fronts!"
    mike.say "Let's ride the Love Boat, Hanna."
    mike.say "Really take the weight off for a while, huh?"
    "Hanna raises an eyebrow as soon as she hears my suggestion."
    "And I get the impression that she see's seen right through me."
    hanna.say "Oh really?"
    hanna.say "Now I wonder why you'd want to do that?"
    hanna.say "It's not exactly the most thrilling ride in the park..."
    hanna.say "Now is it?"
    "I do the best I can to laugh off Hanna's question."
    "But to my surprise, she seems to be up for the ride anyway."
    "As she takes hold of my arm and leads me over there."
    "Soon enough we're stepping into a boat of our own."
    "And then we're sailing off into the darkness of the tunnel."
    show hanna kiss
    $ hanna.flags.kiss += 1
    "Once we're alone, Hanna doesn't hesitate to take advantage."
    "So by the time we emerge from the other end, I'm more than happy."
    "But she seems less enthusiastic."
    show hanna normal
    mike.say "What's the matter, Hanna?"
    mike.say "Didn't you enjoy the ride?"
    "Hanna lets out a sight and shakes her head."
    hanna.say "Hmm..."
    hanna.say "It was nice, [hero.name]."
    show hanna sad
    hanna.say "But I kinda prefer it when people can see us."
    show hanna normal
    $ hanna.love += 2
    $ game.active_date.score += 20
    return

label hanna_date_hedge_maze_male:
    mike.say "Let's walk around the Hedge Maze, Hanna..."
    mike.say "See which one of us can find the way out first!"
    "Hanna looks up at the sign for the attraction with genuine interest."
    hanna.say "Oh..."
    hanna.say "I never knew they had anything like this here."
    hanna.say "You know, I've never been in a real maze too!"
    "That's all I need to hear in order to make up my mind."
    mike.say "Come on then - let's fix that!"
    "Hanna follows me as I make my way over to the queue."
    "And then we wait in line until it's our turn to enter."
    "Soon enough we're surrounded on two sides by high hedges."
    "Trying to make sense of the path that we're walking."
    "Or at least I am."
    "After a couple of turns, I can feel Hanna clinging onto me."
    "In fact, her grip's starting to get tight enough to actually hurt!"
    mike.say "Ouch!"
    mike.say "Hanna..."
    mike.say "Ease off a little!"
    hanna.say "I...I don't like it..."
    hanna.say "I don't like it in here..."
    hanna.say "I want to get out - NOW!"
    "At Hanna's urging, I start to pick up the pace."
    "I'm nodding to show that I understand as I search for the exit."
    "But even so, she's almost clinging to my back once I actually find it."
    hanna.say "Oh god..."
    hanna.say "I am so glad to be out of there!"
    mike.say "What was that, Hanna?"
    mike.say "I didn't think you were claustrophobic!"
    hanna.say "I can't explain it, [hero.name]..."
    hanna.say "I was just scared we were never going to make it out of the place."
    $ hanna.love -= 2
    $ game.active_date.score -= 20
    return

label hanna_date_amusement_ice_cream_male:
    mike.say "I'm feeling a little hot, Hanna..."
    mike.say "You want to go grab an ice-cream to cool down?"
    "Hanna turns to look at me as I make the suggestion."
    "And I see that she has an ironic smile on her face as she does so."
    hanna.say "Oh, [hero.name]…"
    hanna.say "You should know better than that!"
    hanna.say "I work so hard to keep myself in shape."
    hanna.say "And ice-cream is full of nasty stuff I try to avoid."
    "I can't help showing my disappointment as I glance over at the ice-cream stand."
    "Watching everyone buying one walking away and happily licking at their purchases."
    "In fact I seem to paying way more attention to them than I am to Hanna right now."
    hanna.say "[hero.name]…"
    hanna.say "Are you even listening to me?"
    hanna.say "Wait..."
    hanna.say "You're not looking at those girls with ice-creams, are you?"
    "Before Hanna asked the question, I genuinely wasn't."
    "I was more interested in the ice-creams themselves."
    "But the jealous tone of her voice gives me the opportunity I need."
    mike.say "I can't help it, Hanna..."
    mike.say "They just look so..."
    mike.say "So good...good enough to lick themselves!"
    "A moment later I know that my plan's working."
    "Because I feel the sensation of Hanna grabbing my wrist."
    "And then she practically marches me over to the ice-cream stand."
    hanna.say "Give me one of those - NOW!"
    "The server jumps to do as they're told."
    "And soon enough, Hanna and I have ice-creams of our own."
    "Not only that, I get to watch as she makes an exhibition of herself eating it too."
    "A sight that's so distracting, I almost drop my ice-cream on more than one occasion."
    $ hanna.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
