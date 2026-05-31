label alexis_date_amusement_park_male:
    scene bg amusement
    show alexis sadsmile
    with fade
    "I'm having to keep myself from breaking into a run as we finally make it to the amusement park."
    "I just love coming to places like this so much I can't help turning back into a little kid."
    "But even as I try to pick up the pace, I can feel there's something holding me back."
    "And glancing back over my shoulder, I see that it's Alexis, dragging her heels behind me."
    mike.say "Alexis..."
    mike.say "What's the matter?"
    mike.say "Don't you want to get in there and on the rides?!?"
    show alexis sad
    "Alexis responds to this with a shrug and a non-committal grunt."
    show alexis annoyed
    alexis.say "Meh..."
    show alexis whining
    alexis.say "I was never into these kind of places as a kid."
    alexis.say "So why would I start being into them now I'm an adult?"
    show alexis sadsmile
    "Part of me can't believe what I'm hearing, that anyone could be so against an amusement park."
    "Which to me is just like being against having actual fun!"
    "But another part of me knows that I should at least try to be more sympathetic to Alexis."
    "Even if it's only for the sake of actually getting her through the gate and into the place."
    "Because I'm sure that once she's inside, she'll start having fun in spite of herself."
    mike.say "Come on, Alexis..."
    mike.say "Just give it a try, that's all I'm asking."
    mike.say "If you don't like it, the I promise we'll leave."
    show alexis upset
    "Alexis looks at me with narrowed eyes for a moment."
    "Almost like she's trying to decide if I'm being serious."
    show alexis sadsmile
    "But then she lets out a sigh and nods her head."
    show alexis wink
    alexis.say "Okay, [hero.name]…"
    alexis.say "But you have to keep your promise."
    alexis.say "If I don't like it, then we leave."
    show alexis normal
    return

label alexis_date_ferris_wheel_male:
    "I choose to head for the Ferris Wheel first, figuring that it's a classic."
    "So if Alexis likes this ride, I can then try to get her on something more adventurous."
    "True to her word, she lets me lead her into our seats and strap us both in."
    "Then the ride starts up and we're slowly lifted into the air."
    mike.say "Be sure to check out the view, Alexis."
    mike.say "That's the best part of this ride."
    "Alexis does me the favour of nodding to all of this."
    "But I can see that she's not exactly thrilled by the view."
    "And her eyes are kind of glazed over too."
    "Once we reach the top, the ride stops so we can take it all in."
    "But Alexis looks more bored than ever."
    alexis.say "How long do we have to stay up here?"
    alexis.say "I mean, how many times am I supposed to look at the same thing?"
    mike.say "I don't know if there's a set amount of time, Alexis."
    mike.say "Most people really like this part of the ride, you know?"
    mike.say "I never met anyone that wanted to know when it'd be over!"
    alexis.say "Well pardon me for not being most people!"
    alexis.say "I'll try harder not to be an individual in future."
    "After that I decide to keep my mouth shut."
    "And for the rest of the ride we sit there in an awkward silence."
    "One that doesn't get any easier when we're finally off the Ferris Wheel either."
    $ alexis.love -= 2
    $ game.active_date.score -= 20
    return

label alexis_date_merry_go_round_male:
    mike.say "How about we try the Merry-Go-Round, Alexis?"
    mike.say "That's a real staple of the amusement park."
    mike.say "A ride that everyone likes, right?"
    "Alexis rolls her eyes at this."
    "Already making me regret my choice of ride."
    alexis.say "Like I already said, [hero.name]…"
    alexis.say "I'm an adult, not a little kid!"
    "Doing the best I can to ignore the negativity, I lead the way onto the ride."
    "And soon enough we're settled in, waiting for it to get going."
    "I decide that the best thing would be to keep my mouth shut."
    "Maybe that way Alexis will soak up the atmosphere of the ride?"
    "But almost as soon as we start moving, she's complaining again."
    alexis.say "Why do they even have something like this here?"
    alexis.say "Isn't this place supposed to be for adults?"
    alexis.say "All it does is go round and round."
    alexis.say "And it's really slow too!"
    "I keep on nodding my head as Alexis is saying all of this."
    "But the truth is that I'm doing all I can to ignore her."
    "And then the ride finally comes to an end, I'm more than grateful."
    "Because I feel like she's trying to ruin not just this ride."
    "But the very idea of Merry-Go-Rounds in general too!"
    $ alexis.love -= 2
    $ game.active_date.score -= 20
    return

label alexis_date_haunted_house_male:
    mike.say "Let's go in the Haunted House, Alexis..."
    mike.say "You love horror movies, right?"
    "Alexis takes one look at the Haunted House."
    "And then she shakes her head."
    alexis.say "Sure I like scary movies."
    alexis.say "But why would that mean I want to go in there?"
    alexis.say "It looks cheap and cheesy as hell!"
    mike.say "Just indulge me, okay?"
    mike.say "Who knows, you might actually like it."
    "Alexis shrugs and lets me lead her into the Haunted House."
    "But as we walk through it, she doesn't get into the spirit of the place."
    "I find myself jumping at scares round every corner."
    "Yet Alexis seems less than impressed the whole time."
    "It's like she knows just where each scare is going to come."
    "And she's already bored with it before the thing even happens."
    "By the time we're walking out of the Haunted House, she's drained my enthusiasm too."
    "And I feel like I might as well not have bothered going inside in the first place."
    alexis.say "Yeah, that was every bit as lame as I thought it was going to be."
    alexis.say "Total waste of time!"
    mike.say "Maybe next time they'll actually kill some one for real?"
    mike.say "I know that I felt like I was dying in there!"
    alexis.say "Huh?"
    alexis.say "What was that?"
    mike.say "Oh, never mind."
    mike.say "I was just thinking out loud..."
    $ alexis.love -= 2
    $ game.active_date.score -= 20
    return

label alexis_date_love_boat_male:
    "I see the sign for the love boat, and a light goes on in my head."
    "Quiet, relaxed and intimate - just the ride for a mature adult."
    "Perhaps that's the one for Alexis?"
    mike.say "Let's try the Love Boat, Alexis."
    mike.say "I haven't been on one of those in ages!"
    "Alexis opens her mouth to say something."
    "And I'm guessing it was going to be a complaint."
    "But then she stops and seems to actually think about it."
    alexis.say "Hmm..."
    alexis.say "Why not?"
    alexis.say "That does sound a lot more grown-up."
    "Alexis and I hurry over to the entrance of the ride."
    "And soon enough we're settling down into one of the boats."
    "As it begins to move and we sail into the darkness, Alexis leans in close."
    "I can feel her pressing herself against me, and I return the gesture."
    "Pretty soon my arms are wrapped tightly around her."
    show alexis kiss
    $ alexis.flags.kiss += 1
    "And we make good use of the privacy that the ride offers."
    "All of this means that, when we emerge at the other end, Alexis is beaming."
    "And her smile doesn't fade once we're off the ride either."
    hide alexis
    show alexis normal
    with fade
    alexis.say "I have to admit..."
    alexis.say "That was a pretty fun ride."
    alexis.say "Maybe there's hope for this place after all."
    $ alexis.love += 2
    $ game.active_date.score += 20
    return

label alexis_date_hedge_maze_male:
    mike.say "We could try the Hedge Maze, Alexis?"
    mike.say "That's a pretty cerebral ride, right?"
    mike.say "I mean, you really have to use your head!"
    "Alexis shrugs as she allows me to lead her to the ride."
    alexis.say "I suppose we could give it a try."
    alexis.say "After all, what have we got to lose?"
    mike.say "That's the spirit, Alexis!"
    mike.say "You'll soon see how much fun it is."
    "But once we're actually inside, I'm soon regretting my words."
    "I find myself leading Alexis down endless corridors of green."
    "And pretty soon I'm hopelessly lost, without a clue as to where we are."
    "Alexis seems happy to trudge along after me at first."
    "Though soon she seems to reach the end of her patience."
    alexis.say "[hero.name]…"
    alexis.say "You're lost, aren't you?"
    mike.say "I'm not lost..."
    mike.say "I just don't exactly know where I am!"
    alexis.say "Just follow me, okay?"
    "I do as I'm told, following on Alexis's heels."
    "And within what feels like seconds, she find the way out."
    alexis.say "There you go..."
    alexis.say "So easy a child could do it!"
    "All I can do is nod, feeling my embarrassment building."
    "I just hope that Alexis is willing to forget what just happened."
    "And won't keep bringing it up to humiliate me."
    $ alexis.love -= 2
    $ game.active_date.score -= 20
    return

label alexis_date_amusement_ice_cream_male:
    mike.say "I'm loving being here at the amusement park, Alexis..."
    mike.say "You know what would make it even better?"
    mike.say "What'd make it feel just like when we came here as kids?"
    "Alexis looks at me with a thoughtful expression on her face."
    "The I see inspiration flash in her eyes."
    alexis.say "You going on the roller-coaster and getting sick?"
    alexis.say "You remember that, right?"
    alexis.say "The time you went green and threw-up while we were upside down?"
    mike.say "Erm..."
    mike.say "I don't think that was me, Alexis..."
    mike.say "You must be mixing me up with someone else!"
    mike.say "Anyway..."
    mike.say "I meant that we should get ice-cream, yeah?"
    "Luckily for me, the suggestion seems to make Alexis forget about her recollections."
    "And she nods eagerly, leading the way to the ice-cream stand."
    alexis.say "Oh yeah, that is a good idea!"
    alexis.say "Come on, [hero.name] - I want a cone!"
    "I nod as I tell the server what the both of us want."
    "And soon enough I'm handing Alexis her ice-cream and licking my own."
    alexis.say "Mmm..."
    alexis.say "I haven't had an ice-cream in way too long!"
    alexis.say "But you're not getting out of it by distracting me, [hero.name]."
    alexis.say "It really was you that barfed on the roller-coaster."
    alexis.say "I remember because it was on that picture they take of you."
    alexis.say "The one you can buy at the souvenir stand later on."
    mike.say "Erm..."
    mike.say "You didn't actually buy a copy, did you?"
    alexis.say "Now wouldn't you like to know!"
    $ alexis.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
