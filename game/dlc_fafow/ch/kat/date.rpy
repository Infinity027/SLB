label kat_date_eat_a_burger:
    "Kat gives me a nervous smile as she picks up her burger."
    "And then she gingerly takes a bite, not looking enthusiastic at all."
    "Wait a minute - did I actually ask her if she was vegetarian or not?!?"
    return

label kat_date_buy_drink:
    kat.say "I...I think I'm going to do it."
    kat.say "I'm going to go to the bar and buy a drink for myself this time."
    kat.say "Do you want one too, [hero.name]?"
    if kat.pregnant:
        mike.say "Ah, Kat..."
        mike.say "I don't think that's a good idea!"
        "Kat follows my gaze down to her swollen belly."
        "And her cheeks flush red with embarrassment."
        kat.say "Oh, no...of course not!"
    elif hero.pregnant:
        bree.say "I don't think that's a good idea, Kat!"
        bree.say "Not in my current condition."
        "Kat follows my gaze down to my swollen belly."
        "And her cheeks flush red with embarrassment."
        kat.say "Oh, no...of course not!"
    else:
        "I nod eagerly, pleased to see Kat taking the initiative for once."
        if hero.is_female:
            bree.say "That's a great idea, Kat."
            bree.say "I'll have the same again."
        else:
            mike.say "That's a great idea, Kat."
            mike.say "I'll have the same again."
        "Kat nods and sets off for the bar."
        "And I'm pleased to see the look of confidence on her face as she does so."
        $ game.active_date.score += 5
        if "rebel" in kat.traits:
            $ game.active_date.score += 5
        $ kat.set_flag("drinks", 1, "day", mod="+")
    return

label kat_date_play_darts:
    if hero.is_female:
        bree.say "Let's play darts, Kat."
        bree.say "You play games all the time, so you should be great at it!"
    else:
        mike.say "Let's play darts, Kat."
        mike.say "You play games all the time, so you should be great at it!"
    kat.say "Erm...okay, [hero.name], if that's what you want..."
    "It doesn't take me long to see how wrong that assumption was."
    "Kat clumsily tosses the darts around, almost hitting other people more often than she manages to hit the board."
    return

label kat_date_pub_play_pool:
    if hero.is_female:
        bree.say "Let's play pool, Kat."
        bree.say "You play games all the time, so you should be great at it!"
    else:
        mike.say "Let's play pool, Kat."
        mike.say "You play games all the time, so you should be great at it!"
    kat.say "Erm...okay, [hero.name], if that's what you want..."
    "It doesn't take me long to see how wrong that assumption was."
    "Kat clumsily pokes at the balls with her cue, actually knocking them off the table more than once."
    return

label kat_date_buy_a_round:
    kat.say "I...I think I'm going to do it."
    kat.say "I'm going to go to the bar and buy a round for everyone myself this time."
    kat.say "Are you in, [hero.name]?"
    if kat.pregnant:
        mike.say "Ah, Kat..."
        mike.say "I don't think that's a good idea!"
        "Kat follows my gaze down to her swollen belly."
        "And her cheeks flush red with embarrassment."
        kat.say "Oh, no...of course not!"
        $ hero.cancel_activity()
    elif hero.pregnant:
        bree.say "I don't think that's a good idea, Kat!"
        bree.say "Not in my current condition."
        "Kat follows my gaze down to my swollen belly."
        "And her cheeks flush red with embarrassment."
        kat.say "Oh, no...of course not!"
        $ hero.cancel_activity()
    else:
        "I nod eagerly, pleased to see Kat taking the initiative for once."
        if hero.is_female:
            bree.say "That's a great idea, Kat."
            bree.say "I'll have the same again."
        else:
            mike.say "That's a great idea, Kat."
            mike.say "I'll have the same again."
        "Kat nods and sets off for the bar."
        "And I'm pleased to see the look of confidence on her face as she does so."
        $ game.active_date.score += 5
        if "rebel" in kat.traits:
            $ game.active_date.score += 5
        $ kat.set_flag("drinks", 1, "day", mod="+")
    return

label kat_dance_with:
    if hero.is_female:
        bree.say "Come on, Kat..."
        bree.say "Let's dance!"
    else:
        mike.say "Come on, Kat..."
        mike.say "Let's dance!"
    "Before she can object, I take Kat by the hand and pull her up."
    "She seems awkward and embarrassed at first, clinging to me the whole time."
    "But soon that evolves into us dancing really close together, and it's actually quite a pleasant experience!"
    return

label kat_date_play_arcade_intro:
    if hero.is_female:
        bree.say "Kat, look!"
        bree.say "They have retro arcade cabinets in here!"
    else:
        mike.say "Kat, look!"
        mike.say "They have retro arcade cabinets in here!"
    "At the mere mention of arcade machines, Kat's face lights up."
    kat.say "Where, where?!?"
    kat.say "We have to go play them!"
    "Together we hurry over to the corner where the cabinets are standing."
    "Then we begin desperately counting up the small change we have between us."
    kat.say "This date just went from good to super awesome!"
    if hero.is_female:
        bree.say "You said it, Kat - prepare to have your ass kicked!"
    else:
        mike.say "You said it, Kat - prepare to have your ass kicked!"
    kat.say "Hah...big talk, [hero.name] - let's see if you can back it up!"
    return

label kat_date_play_arcade_win:
    "Kat and I are determined to play each and every one of the games."
    "And as soon as we get into the first one, I get a taste of what I'm up against."
    if hero.is_female:
        bree.say "Whoa..."
        bree.say "You weren't kidding, Kat!"
    else:
        mike.say "Whoa..."
        mike.say "You weren't kidding, Kat!"
    kat.say "What did I tell you, [hero.name]?"
    kat.say "I'm not pulling any punches!"
    "But somehow I manage to dig deep and fight back."
    "Pretty soon I'm beating Kat, hands down!"
    kat.say "What happened?"
    kat.say "Where did you learn to play like that?!?"
    if hero.is_female:
        bree.say "Hail to the king, baby!"
    else:
        mike.say "Hail to the king, baby!"
    return

label kat_date_play_arcade_lose:
    "Kat and I are determined to play each and every one of the games."
    "And as soon as we get into the first one, I get a taste of what I'm up against."
    if hero.is_female:
        bree.say "Whoa..."
        bree.say "You weren't kidding, Kat!"
    else:
        mike.say "Whoa..."
        mike.say "You weren't kidding, Kat!"
    kat.say "What did I tell you, [hero.name]?"
    kat.say "I'm not pulling any punches!"
    "No matter what I do, Kat's always one step ahead of me."
    "And all the tricks I can call on don't seem to help at all."
    if hero.is_female:
        bree.say "What happened?"
        bree.say "Where did you learn to play like that?!?"
    else:
        mike.say "What happened?"
        mike.say "Where did you learn to play like that?!?"
    kat.say "Kneel before your queen, wretch!"
    return

label kat_dick_reactions:
    if not kat.flags.seendick:
        $ kat.flags.seendick = 1
        "I take a deep breath and then I just do it."
        "I let Kat catch a glimpse of my manhood for the first time."
        "Her eyes are already wide with anticipation."
        "But they go wider still when she actually sees it."
        if hero.has_skill("hung"):
            show dick reactions kat scared
            kat.say "Oh..."
            kat.say "Oh my!"
            kat.say "Oh my goodness!"
            mike.say "What's wrong, Kat?"
            mike.say "Don't you like what you see?"
            kat.say "Oh no, it's not that."
            show dick reactions kat smile
            kat.say "It's fine, [hero.name], really."
            kat.say "In fact, it's better than fine."
            kat.say "I just never knew they could be that...that big!"
            $ kat.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions kat mock
            kat.say "Oh..."
            kat.say "Erm..."
            kat.say "Okay then..."
            mike.say "What's wrong, Kat?"
            mike.say "You sound like you were expecting something..."
            mike.say "Well...something different!"
            show dick reactions kat smile
            kat.say "It's fine, [hero.name], really."
            show dick reactions kat mock
            kat.say "I guess it's what you do with it that counts..."
            $ kat.sub -= 10
        hide dick reactions
    return

label kat_date_amusement_park_male:
    scene bg amusement
    show kat talkative
    with fade
    kat.say "Come on, [hero.name]…"
    kat.say "What's the problem back there?"
    kat.say "Don't you want to get into the park?!?"
    show kat smile
    mike.say "Slow down, Kat!"
    mike.say "I can't wind through the crowd like you."
    mike.say "I'm going to get left behind!"
    "Normally it's me having to drag my reluctant companion into the Amusement Park."
    "I don't know what it is about most girls, they just don't seem to be up for the place."
    "And so I guess the fact that Kat's more eager to get in than me means she's different."
    "But luckily for me, it seems like she's actually stopping to let me catch up."
    mike.say "Phew..."
    mike.say "Don't do that to me, Kat!"
    mike.say "I thought I was going to lose you in the crush."
    "Kat waves a hand in the air, dismissing my concerns."
    show kat talkative
    kat.say "Ah, don't be dramatic."
    show kat happy
    kat.say "I'd have found you at the place where they take the lost kids!"
    show kat smile
    mike.say "Hey!"
    mike.say "I'm more than capable of looking out for myself."
    "I try as hard as I can to get my point across."
    "But it seems as though Kat's not listening to me."
    show kat enthusiastic
    "Instead she's looking all around as we walk into the park."
    show kat surprised
    kat.say "Wow..."
    kat.say "There sure are a lot of rides in here."
    show kat enthusiastic
    mike.say "You don't know the half of it, Kat!"
    mike.say "And the best thing is, you have me as your guide."
    mike.say "I come here as often as I can."
    mike.say "So I know the place like the back of my hand."
    show kat happy
    kat.say "That's some big talk on your part."
    kat.say "Let's see if you can back it up."
    show kat smile
    "With that, Kat takes hold of my hand."
    "And she leads me deeper into the park."
    return

label kat_date_ferris_wheel_male:
    mike.say "Let's ride the Ferris Wheel, Kat."
    "Kat frowns at this, not looking convinced."
    kat.say "Are you sure you want to?"
    kat.say "I mean, it's not the most exciting ride, is it?"
    "I shake my head as we walk over to join the queue."
    mike.say "It's a classic."
    mike.say "So you kind of have to tick it off the list."
    kat.say "If you say so..."
    "I get the impression that Kat's still not buying it."
    "So I'm relieved to find that the queue for the Ferris Wheel is short."
    "This means that we soon make it to the front and get into a gondola."
    "We both stay quiet as the safety-bar comes down."
    "And the silence holds as we rise into the air."
    "But when I steal a sideways glance at Kat, I'm encouraged by what I see."
    "Because it looks like she's glancing around as we get ever higher."
    "But who can blame her?"
    "As the view is getting better by the moment."
    "When we reach the top of the wheel, the ride stops."
    "And the view from way up here is simply amazing."
    mike.say "You see what I mean?"
    "Kat shoots me a glance that shows she's been rumbled."
    "But then her face breaks into a grudging smile."
    kat.say "Okay, okay..."
    kat.say "It's worth the effort."
    kat.say "But only for the sake of the view!"
    mike.say "I'm not going to argue with you on that one, Kat."
    "The silence returns as we enjoy the rest of the ride."
    "But this time it's more of an easy, satisfied silence."
    "And once we're off the Ferris Wheel, I'm happy we made the effort to ride it."
    $ kat.love += 1
    $ game.active_date.score += 10
    return

label kat_date_merry_go_round_male:
    mike.say "Short queue for the Merry-Go-Round, Kat..."
    mike.say "We could ride that while we wait for the other rides to quieten down."
    "Kat responds to this by pointing out a nearby bench."
    kat.say "Or we could go sit on that bench over there."
    kat.say "It's closer than the Merry-Go-Round and there's no queue at all."
    kat.say "Plus it's about as exciting as well!"
    "I roll my eyes at Kat's joke."
    mike.say "Ha, ha..."
    mike.say "Very funny, Kat!"
    mike.say "But the bench doesn't move."
    mike.say "So the Merry-Go-Round wins!"
    "Kat shakes her head."
    "But the expression on her face is one of surrender."
    kat.say "Okay, okay..."
    kat.say "But I'm only doing this to kill some time."
    "We walk over to the back of the line and join it."
    "And the queue proves to be as short as it looked."
    "Soon enough we're stepping onto the ride and choosing a spot."
    "Kat and I hold on tight as the whole thing starts to move."
    "And sure, it's a total throw-back in terms of excitement."
    "But I still feel a slight thrill as it gets up to speed."
    "That would probably have faded if the ride had lasted any longer."
    "So I'm kind of relieved to get off it with the feeling intact."
    kat.say "Okay, [hero.name]…"
    kat.say "That beats the bench."
    kat.say "But only just!"
    $ kat.love += 2
    $ game.active_date.score += 20
    return

label kat_date_haunted_house_male:
    kat.say "Huh..."
    kat.say "They have a Haunted House."
    "I turn around to see that Kat's staring at the attraction in question."
    "And I instantly made the decision in my head that we have to do that one next."
    mike.say "I love the Haunted House, Kat!"
    mike.say "Let's go join the queue."
    kat.say "But I haven't done one of those since I was a kid!"
    mike.say "All the more reason to do this one now."
    mike.say "Relive all those great memories, right?"
    "Kat seems to think about it for a moment."
    "Then she nods."
    kat.say "I guess so."
    "I think Kat's more doing it because she can't find a reason not to."
    "Rather than doing it because she can find a good reason in favour of it."
    "But that's good enough for me."
    "So I lead her over to where the queue begins, and we wait for our turn."
    "By the time we get to the front of the line, Kat looks a little nervous."
    "But I take hold of her hand and give it a squeeze."
    mike.say "Don't worry, Kat..."
    mike.say "It's just a ride, remember?"
    "This seems to have the desired effect."
    "As Kat smiles and nods her head."
    "Then we step into the Haunted House, still holding hands."
    "What follows is a text-book trip around a spooky ride."
    "Kat and I jump in all the right places."
    "We scream in all the right spots too."
    "And by the time we come out, my heart is pounding in my chest."
    mike.say "Shit..."
    mike.say "I don't remember it being that scary!"
    kat.say "Yeah, [hero.name]..."
    kat.say "I think that's my curiosity well and truly satisfied!"
    $ kat.love += 2
    $ game.active_date.score += 20
    return

label kat_date_love_boat_male:
    kat.say "Okay, [hero.name]..."
    kat.say "I guess you're going to want to ride the Love Boat?"
    "I do the best I can to sound surprised at the question."
    "Trying to hide the fact that I've been staring at it for ages."
    mike.say "What?"
    mike.say "What was that, Kat?"
    mike.say "Oh, do they have one of those?"
    "Kat shakes her head, not buying it for a moment."
    kat.say "Nice try."
    kat.say "But I know that you want to ride it."
    kat.say "So that's exactly what we're going to do!"
    "I do the best I can to keep up the act as Kat puts her plan into action."
    "She almost drags me over to where the line starts."
    "Then she holds my hand as tight as she possibly can."
    "All to make sure I don't attempt to flee."
    mike.say "Seriously, Kat..."
    mike.say "You've got the wrong end of the stick."
    mike.say "But I'll ride it, if that's what you want."
    mike.say "I'm willing to make that sacrifice for the sake of our relationship."
    "When our turn comes round, Kat all but tosses me into the waiting boat."
    "And then she leaps in beside me, almost turning it over."
    mike.say "Whoa!"
    kat.say "Oh shut up!"
    kat.say "And put that mouth of yours to better use..."
    "I think you can guess what Kat means by that."
    "For all of her supposed reluctance, she's the one that pounces on me!"
    show kat kiss
    $ kat.flags.kiss += 1
    "And we spend the short duration of the ride wrapped in each other's arms."
    "So much so that, by the time it's over, we've both dropped all pretences."
    "Instead we do all we can to make every single second count."
    hide kat
    show kat happy
    $ kat.love += 2
    $ game.active_date.score += 20
    return

label kat_date_hedge_maze_male:
    mike.say "You want to try out the Hedge Maze, Kat?"
    mike.say "Could be fun - kind of like a VR game."
    mike.say "But without the eyewear!"
    "Kat frowns at this."
    "But that seems to have more to do with my pitch than the actual maze itself."
    kat.say "Wouldn't that be an Augmented Reality game?"
    mike.say "Erm..."
    mike.say "If you say so..."
    mike.say "You want to go in there or what?"
    "Kat answers my question by walking over and joining the queue."
    "Which leaves me to hurry along after her."
    "Luckily for us, the maze isn't one of the crazily popular attractions"
    "So it's not long before we find ourselves walking into the entrance."
    "And right from the start I can see that Kat's getting into it."
    kat.say "Oh yeah..."
    kat.say "This reminds me of all those retro games, you know?"
    kat.say "The ones where you're running around in a maze?"
    "It seems a pretty obvious statement to make."
    "I mean we are standing in a maze, after all!"
    "But I do the best I can not to spoil the moment."
    mike.say "Yeah, Kat..."
    mike.say "It's just like that!"
    kat.say "Come on..."
    kat.say "Catch me if you can!"
    "Kat darts off, running into the maze."
    "She disappears around the first corner before I can react."
    "And so she has a real head-start on me when I finally manage to get moving."
    "No matter how hard I try, I can't seem to fully catch up to Kat."
    "She ducks and dives, outmanoeuvering me at every turn."
    "And once we finally reach the exit, we're both totally out of breath."
    "But we're also laughing as hard as we possibly can too."
    $ kat.love += 2
    $ game.active_date.score += 20
    return

label kat_halloween_invitation:
    show kat
    "I'm more than itching to get Kat on board with the idea of the Halloween party at my place."
    "Which means that I'm practically falling over myself to mention it to her when we next meet up."
    "But at the very last moment I feel that familiar pang of concern about just blurting it out."
    "What if I make the whole thing sound lame?"
    "What if she's totally past dressing up on Halloween?"
    "Argh...now my mind's going into over-drive!"
    "I'm going to have to come at it from another angle..."
    show kat talkative at center, zoomAt(1.5, (640, 1040)) with vpunch
    kat.say "Are you feeling okay?"
    show kat smile
    "The sound of Kat's voice snaps me out of my mental spiral."
    "And I come back to reality to find that she's beaten me to the punch."
    mike.say "Huh?"
    mike.say "What was that?"
    show kat sadsmile
    kat.say "I asked if you were feeling okay..."
    kat.say "Because you look like something's bothering you!"
    show kat normal
    "I take a moment to fill my lungs and then let it all out in a long breath."
    "Once I've done that, I feel better able to face the question."
    "And maybe able to turn it towards my own query too."
    mike.say "Oh yeah..."
    mike.say "I was just wondering..."
    mike.say "Are you doing anything on Halloween?"
    show kat confused
    "Kat greets the question with a nonchalant shrug."
    "And she screws up her lips as she thinks about her response."
    show kat talkative
    kat.say "Well..."
    kat.say "I had thought about livestreaming on the actual night."
    kat.say "Do some classic survival horror stuff, you know?"
    show kat talkative
    kat.say "But I haven't decided yet."
    kat.say "Are you doing something for it?"
    show kat smile
    "There it is, the chance I've been waiting for."
    mike.say "Ah, yeah, Kat..."
    mike.say "My housemates and I are throwing a Halloween party."
    mike.say "And...I was wondering..."
    mike.say "Would you like to come along?"
    if kat.love >= 100:
        "Kat seems to be thinking about it."
        "Perhaps a little longer and deeper than I'd have liked."
        "But then she puts me out of my misery by nodding her head."
        show kat talkative
        kat.say "I don't normally go in for that kind of thing."
        kat.say "But as it's you, [hero.name]…"
        kat.say "I think I could make an exception."
        show kat smile
        "As it's me!"
        "Did you just hear that?!?"
        "She said because it's me!"
        mike.say "I..."
        mike.say "Erm..."
        mike.say "Yeah...that's great news, Kat!"
        "I go silent for a moment, by brain seeming to cut out."
        "Because I'm sure there's something else that I needed to say."
        show kat talkative
        kat.say "And this party is happening when, exactly?"
        kat.say "I'm guessing Halloween night?"
        show kat smile
        mike.say "Oh..."
        mike.say "Oh yeah, of course!"
        mike.say "It's a costume party, so you'll want to dress up."
        mike.say "Maybe make it kind of sexy?"
        mike.say "Or scary - scary is good too..."
        mike.say "Scary and sexy?"
        "Kat chuckles at my babbling."
        show kat talkative
        kat.say "Okay, okay..."
        kat.say "I think I get it."
        kat.say "See you on Halloween."
        $ game.flags.halloween_girl = "kat"
    else:
        "Kat sighs and shakes her head."
        show kat sadsmile
        kat.say "Meh..."
        show kat annoyed
        kat.say "I'm not really into Halloween that way, you know?"
        kat.say "Like the way they've tried to make it a second Christmas?"
        show kat sad
        "Of course that's not the answer that I wanted to hear."
        "But I do the best I can to hide the fact."
        mike.say "Oh no, it's nothing like that!"
        mike.say "We're getting together to celebrate the spirit of the holiday."
        mike.say "I'm totally against the commercialisation of it too!"
        show kat normal
        "Kat narrows her eyes at me."
        "And I get the feeling that I'm being examined."
        "Kind of like a bug under a microscope!"
        show kat smile
        kat.say "Oh really?"
        kat.say "So there's no plastic skeletons?"
        show kat upset
        mike.say "Erm..."
        show kat smile
        kat.say "No Jack-O-Lanterns that plug into the mains?"
        show kat upset
        mike.say "Well..."
        show kat smile
        kat.say "No polystyrene gravestones in the front yard?"
        show kat upset
        mike.say "Maybe?"
        "Kat shakes her head a second time."
        "But now I get the feeling it's with more finality."
        show kat talkative
        kat.say "I think I'll stick to the original plan."
        kat.say "But don't let that stop you enjoying yourself, okay?"
        show kat smile
        "And just like that, my plans go up in flames."
    return

label kat_halloween_arrival:
    scene bg house
    with fade
    "I'm not really paying attention as I open the door to whoever's out there."
    "And I pay for it as I open the front door without looking in the same direction."
    play sound woosh_punch
    "Because a huge metal ball covered in spikes flies straight past my face."
    "I leap back into the house on pure instinct alone, wailing in alarm."
    with hpunch
    mike.say "Aargh!"
    mike.say "What the hell?!?"
    play sound woosh_punch
    "As the ball takes a second swing, I see someone standing on the doorstep."
    show kat halloween angry at center, zoomAt(1.0, (940, 720))
    show kat at center, traveling(1.25, 0.3, (640, 880))
    pause 0.3
    with hpunch
    kat.say "What's that I smell on you?"
    kat.say "Is that the Witch Scent?!?"
    show kat halloween upset
    "Even though she's practically shouting at me, I still recognise Kat's voice."
    "And as she steps into the house, still swinging the ball, I get a better look at her."
    "Kat's wearing what looks like an old-fashioned maid's uniform."
    "Most of the dress is black."
    "But there are bits picked out in white, lacy material too."
    "The hair on one side of her face has been allowed to hang over her eye."
    "And on the other it's been pinned up out of the way."
    "I hold up a hand, trying to stop Kat advancing on me."
    "Not to mention discouraging a second swing of the ball, which I can now see is hanging on a long chain."
    show kat smile b
    mike.say "Okay, okay..."
    mike.say "I get it, Kat..."
    show kat stuned b
    mike.say "You're Ram, yeah?"
    "As soon as the words are out of my mouth, I know I've made a mistake."
    "Kat pretty much stamps a foot on the floor as she frowns art me."
    show kat shocked b
    kat.say "Ram?"
    show kat offended a
    kat.say "Are you kidding me?!?"
    kat.say "I'm supposed to be Rem!"
    show kat angry a
    kat.say "Urgh..."
    kat.say "Did you even watch the anime?"
    show kat upset
    "Kat has me on the back-foot right now."
    "And I'm afraid she's going to start spinning the weapon again."
    "All of which means I need to do something, and quick!"
    menu:
        "Maybe not with as much attention as needed...":
            "I decide that the best thing would be to deescalate the situation."
            "And so I make a point of letting the whole thing drop."
            "As the night going well is more important to me than being proven right."
            mike.say "Sorry, Kat..."
            show kat normal
            mike.say "I guess I wasn't paying close enough attention!"
            "My admission seems to be just what Kat was looking for."
            "As her mood improves almost as soon as I've said two words."
            show kat smile b
            $ kat.love += 1
            kat.say "Oh, it's okay, [hero.name]…"
            kat.say "I suppose they are identical twins!"
            show kat defiant
            kat.say "So..."
            kat.say "What do you think of my outfit?"
            show kat shy c at center, zoomAt(1.25, (540, 880)) with ease
            "Kat gives me a quick twirl."
            show kat c at center, zoomAt(1.25, (740, 880)) with ease
            "And as she does so, I realise that I haven't seen the half of it."
            show kat c at center, zoomAt(1.25, (640, 880)) with ease
            "Kat's costume is great, really detailed and accurate."
            "But what's even better is that it looks so good on her!"
            "So good that it's all I can do to keep my hands to myself."
            show kat annoyed blush a
            kat.say "Are we going to stand around here all night?"
            show kat normal a
            mike.say "What?"
            mike.say "Oh..."
            mike.say "Oh no..."
            mike.say "Sure, Kat - let's go get you a drink."
        "Of course, but they're so alike!":
            "I decide that the best thing is to give as good as I've been getting."
            "Kat already swung her huge weapon at me more than once."
            "And now she's insulting my knowledge of anime too!"
            "All of that deserves some serious retaliation on my part."
            mike.say "Come on, Kat..."
            mike.say "They're identical twins!"
            mike.say "It's hard enough to tell the difference at the best of times."
            mike.say "Never mind when someone's swinging a spiked ball in your face!"
            show kat upset c
            "Kat frowns at this, crossing her arms over her chest."
            show kat angry c
            kat.say "I'll have you know that this is Rem's mace!"
            show kat upset c
            "She thrusts the weapon at me as if that much should be self-evident."
            "And now I can see that it's mostly made of foam and rubber."
            "But none of that does much to improve my mood."
            mike.say "No, Kat..."
            mike.say "A mace has a handle."
            mike.say "What you have there is more like a morning star or a flail!"
            show kat annoyed b
            $ kat.love -= 3
            "Kat rolls her eyes and snorts at my retort."
            "Shoving the prop weapon into my hands as she shoves her way past."
            show kat angry b
            kat.say "Who cares what it is?"
            kat.say "I thought this was supposed to be a party, not a nit-picker's convention!"
            show kat upset b
            "I groan as I follow Kat into the house."
            "Already starting to think that this could be a very long night."
    scene bg black with dissolve
    pause 1
    return

label kat_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    "I can't have been gone more than a couple of minutes, just grabbing punch for Kat and myself."
    "But as I thread my way back to her though the knots of guests, I Kat waving for my attention."
    "And as I get closer, I notice that she has a pretty desperate look on her face as well!"
    "So in danger of spilling the punch, I begin hopping and twisting my way through the crowd."
    "At first I'm worried that I'll be walking into the middle of a bad situation."
    "Like someone's going to be hitting on Kat, or have said something that's deeply offended her."
    "But when I actually arrive on the scene, I find myself staring at the back of Jack's head."
    show kat halloween shy a at center, zoomAt(1.0, (440, 730))
    show jack halloween perv at center, zoomAt(1.0, (840, 760))
    with fade
    jack.say "Oh man..."
    show jack at center, traveling(1.0, 2.0, (740, 760))
    jack.say "When I saw your costume, I just freaked!"
    jack.say "That is like, totally one of my favourite anime at the moment!"
    show jack guilty
    "I can see that he's leaning in close to Kat as he says all of this."
    "So close that he's invading her personal space more with each passing second."
    if 'kat_jack_07' in DONE:
        "I guess Jack's thinking that we're all in some kind of relationship or something."
        "And he can't see past that to read that Kat's looking pretty uncomfortable."
    "But now that I'm almost as close as Jack is, Kat finally has the help she wanted."
    "And she lurches around him, already reaching out for the cup of punch in my hand."
    $ kat.love += 1
    show kat afraid a
    kat.say "[hero.name]…"
    kat.say "There you are!"
    show kat timid a
    kat.say "I thought you'd gone off and left me all on my own for the night!"
    if 'kat_jack_07' in DONE:
        kat.say "And you never told me Jack was going to be here too."
    show jack blank
    "At the sight of me, Jack seems to deflate a little."
    "Especially as Kat all but clings onto my arm as she says all of this."
    show jack lying
    jack.say "Oh..."
    jack.say "Hey, [hero.name]…"
    show jack smile
    jack.say "I guess I met your date for the night, huh?"
    show jack embarrassed
    if 'kat_jack_07' in DONE:
        jack.say "I mean, we could always hang out together, right?"
        jack.say "Because we already hooked up that one time, remember?"
    "I look from one of them to the other, weighing up the situation."
    "And I can see that Kat's expecting me to shoo Jack away from her."
    "But on the other hand, Jack's clearly waiting for me to speak up for him."
    menu:
        "Jack... Remember what we said about cosplayers?":
            "Yet there's no question as to where my allegiances lie tonight."
            "Jack might be one of my best friends, perhaps the best of all."
            "But Kat's here as my date."
            "And this might make me sound like a total jerk, but I want her to myself!"
            "At least as much as I can at a house party I'm supposed to be hosting."
            mike.say "Yeah, Jack..."
            mike.say "Kat's my date."
            mike.say "And I get it, you really like her costume."
            show jack normal
            "Jack nods, at first taking what I say as my agreeing with him."
            show jack guilty
            mike.say "But you remember what happened when we went to that last convention?"
            mike.say "The time I had to spend talking them out of banning you for life?"
            mike.say "Not to mention all those cosplayers that wanted to have you arrested!"
            "Jack's expression changes dramatically as I remind him of past events."
            "And pretty soon he's shaking his head, rather than nodding."
            show fx drop at right4
            jack.say "Oh..."
            show jack lying at center, zoomAt(1.0, (840, 760)) with ease
            jack.say "Oh yeah, [hero.name]!"
            hide fx
            jack.say "I remember you telling me about things I can say in my head."
            jack.say "And things I shouldn't say to ladies dressed as hot anime characters!"
            show jack annoyed
            mike.say "And this, Jack..."
            mike.say "Is another one of those times!"
            show jack surprised
            show fx exclamation at right5
            jack.say "It is?!?"
            jack.say "Oops!"
            hide fx
            show jack embarrassed
            "With that, Jack looks around, as if checking for anyone watching him."
            hide jack with easeoutright
            "Then he scuttles off, leaving Kat and I alone to drink our punch."
            show kat whining b at center, zoomAt(1.0, (640, 730)) with ease
            kat.say "I'm sorry, [hero.name]…"
            if 'kat_jack_07' in DONE:
                kat.say "The threesome was fun."
                kat.say "But I just want to spend some time with you tonight."
            else:
                kat.say "I didn't know he was your friend."
            show kat sad b
            "I shrug as I watch Jack finally make himself scarce."
            mike.say "Don't worry about it, Kat..."
            $ kat.love += 2
            show kat busted blush b
            mike.say "He just gets that way around hot girls in cute costumes."
            mike.say "He'll have forgotten all about it in half an hour, trust me."
        "Yep, that gorgeous anime girl is with me!":
            "Normally I'd be wanting to shoo Jack off, so I can have Kat all to myself."
            "But he's clearly bowled over by the mere sight of her in that costume."
            "And that means I can easily bask in her reflected glory too."
            mike.say "Oh yeah, Jack..."
            mike.say "Kat's here with me tonight."
            show kat smile b
            "I see Kat smile as I step in and state all of that plainly."
            "But then I see that she's expecting me to say more."
            "So I do just that."
            show kat stuned a
            mike.say "Doesn't she look super-hot?"
            "Jack begins nodding like crazy as soon as make the statement."
            "But Kat just stares at me in what looks like sheer amazement."
            show jack perv
            jack.say "Oh boy, oh boy, oh boy!"
            jack.say "You bet she does, [hero.name]..."
            show jack happy
            jack.say "You're such a lucky guy!"
            show jack normal
            "Kat waves a hand in the air, appealing for my attention."
            $ kat.love -= 2
            show kat offended a
            kat.say "Hello!"
            kat.say "I'm standing right here!"
            kat.say "Why aren't you both talking to me?"
            show kat normal
            "Jack's too wrapped up in his own delight to listen to Kat."
            "And I'm too busy buffing my ego to notice her growing frustration."
            show jack happy
            jack.say "Wow..."
            jack.say "I bet you can't wait to dance with her, yeah?"
            mike.say "Actually, Jack..."
            mike.say "I'm just taking a rest and having a drink."
            show jack smile
            show kat stuned a
            show fx exclamation at left
            mike.say "Why don't you and Kat have a dance together?"
            $ kat.love -= 2
            kat.say "What the..."
            show jack happy
            show kat shocked a
            "Before Kat can object, Jack grabs hold of her wrist."
            hide kat
            hide jack
            "And then I watch as she's unceremoniously dragged onto the make-shift dancefloor."
            "The expression on her face darkening every time they pass me by."
    scene bg black with dissolve
    pause 1
    return

label kat_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show kat halloween surprised c at center, zoomAt(1.25, (640, 880))
    with fade
    kat.say "What is that music?"
    kat.say "I know that track from somewhere!"
    show kat stuned
    "I look around to see Kat standing still and listening intently."
    "In fact she kind of looks like she's spellbound by what she's hearing."
    mike.say "Erm..."
    mike.say "I dunno, Kat..."
    if not bree.is_gone_forever:
        mike.say "[bree.name] was the one that put the playlist together."
    elif not sasha.is_gone_forever:
        mike.say "Sasha was the one that put the playlist together."
    show kat enthusiastic c
    "All of a sudden, Kat's face lights up."
    "And she nods her head intently."
    show kat surprised c
    kat.say "I know what it is..."
    if not bree.is_gone_forever:
        show kat enthusiastic c
        kat.say "And [bree.name] is a total legend!"
    elif not sasha.is_gone_forever:
        kat.say "And your friend, Sasha..."
        show kat enthusiastic c
        kat.say "She's a total legend!"
    show kat defiant
    "Without asking permission, Kat grabs hold of my hand."
    show kat smileclosed b at center, traveling(1.5, 0.3, (640, 1040))
    "And then she starts pulling me towards the makeshift dancefloor."
    "I'm carried along behind her more out of genuine surprise than anything else."
    "Which means when I start to put on the breaks, it's out of sheer instinct alone."
    mike.say "Whoa..."
    mike.say "Slow down a little, Kat..."
    mike.say "You haven't even told me what this music even is!"
    "Kat doesn't seem to take my temporary refusal all that well."
    "As she turns around and gives me another firm tug towards the dancefloor."
    show kat happy b
    kat.say "It's a track from the soundtrack to one of my favourite games of all time!"
    kat.say "Now do you see why we have to dance to it?!?"
    show kat smile b
    menu:
        "Alright, alright! I'll dance with you.":
            "I nod my head and let Kat pull me onto the dancefloor behind her."
            "If it had been anyone else, I might well have flatly refused."
            "I don't know the track, and usually you can't dance to music from a videogame."
            "But I want to do all I can to make a good impression on Kat."
            "Plus if I don't, she might go and dance with Jack."
            "Or even worse, with Scottie!"
            hide kat
            show dance kat halloween
            with fade
            "Once we're out there, I do the best I can to actually dance."
            "But in the end I have to try and follow Kat's example."
            "It's awkward to begin with, but I get it with time."
            "And once I do, everything seems to get easier."
            "Kat clearly appreciates the effort I'm making too."
            "Because she dances close to me for the entire length of the track."
            hide dance
            show kat halloween smileclosed blush at center, zoomAt(1.5, (640, 1040))
            with fade
            "And when it's finished, she leans her head on my shoulder."
            "Not to mention the rest of her body against mine too!"
            kat.say "Mmm..."
            show kat happy
            kat.say "That was really nice."
            show kat talkative a
            kat.say "You know, almost romantic?"
            show kat smile a
            mike.say "Almost romantic, but not quite?"
            "Kat chuckles and shakes her head."
            $ kat.love += 4
            show kat smileclosed b -blush
            kat.say "This is a Halloween house party, [hero.name]…"
            kat.say "Not a fairy-tale ballroom!"
            show kat smile
            "I can't help chuckling and nodding my head too."
            "Because Kat's right, and I'm over-thinking things."
            "So instead I just try to focus on the moment."
            "Enjoying it for what it is and however long it lasts."
        "Sorry but I'm not dancing on a music I don't know...":
            "As soon as Kat tells me what the music actually is, I shake my head."
            show kat stuned a
            "And I pull my hand out of her grip too, just to make my intentions clear."
            mike.say "Nah..."
            mike.say "I think I'll pass on this one."
            show kat confused b
            "Kat shakes her head in disbelief."
            show kat surprised b
            kat.say "You actually mean that?"
            kat.say "You're going to turn me down for a dance?"
            kat.say "When it's a track I really like?"
            show kat sad
            "Now it's my turn to shake my head."
            "Because it seems to me that Kat's overreacting."
            mike.say "Not for any track, Kat..."
            mike.say "Just this one."
            mike.say "For one thing, I don't know it."
            mike.say "And for another it's from a videogame."
            mike.say "So it wasn't meant to be danced to!"
            $ kat.love -= 4
            show kat sad a
            "Kat lets out a huff of annoyance."
            hide kat with easeoutleft
            "Then she turns her back on me and walks onto the dancefloor alone."
            "Which means I have to stand there and watch as she dances with First Jack and then Scottie."
            "What's worse, I can't bring myself to go out there and stop any of it happening."
            "Because that would be like admitting that I was wrong."
    scene bg black with dissolve
    pause 1
    return

label kat_halloween_sex:
    scene bg livingroom
    with fade
    "It's getting a little late by now and the party is naturally beginning to wind down."
    "Only a few people are still dancing, most have wandered off to chat in small groups."
    "And on top of that, most of the alcohol in the house seems to have been drunk too."
    "Which means that voices are being raised at the same time inhibitions are going down."
    "But on top of all this, I seem to have managed to lose Kat somewhere along the way."
    "So I'm currently wandering around the house, doing the best I can to find her."
    scene bg secondfloor with fade
    "I keep opening all of the doors that I pass, calling into the rooms beyond."
    scene bg houselibrary with fade
    mike.say "Kat?"
    scene bg firstfloorbathroom with fade
    mike.say "Kat?"
    mike.say "Are you in there?"
    scene bg livingroom with fade
    "It's only when I'm a couple of doors from my own room that I hear a response."
    "But the weird thing is that it's not coming from within the room I'm looking in."
    kat.say "Psst…"
    kat.say "Psst!"
    kat.say "Over here!"
    "With a frown on my face, I look around, trying to find where Kat's voice is coming from."
    show kat halloween blush at center, zoomAt (1.25, (40, 880)) with easeinleft
    "And it doesn't take me long to spot her head, poking out of a door at waist height."
    "But what really throws me is the fact that Kat's peeking out of my bedroom door!"
    "I hurry over, eager to see what on earth made her disappear off into that room in particular."
    mike.say "Kat..."
    mike.say "So that's where you've gotten to?"
    "I'm about to say more, but Kat cuts me off."
    show kat upset
    kat.say "Ssshh!"
    kat.say "You're not going to believe what I found in here..."
    show kat defiant
    kat.say "There's a whole bedroom behind this door - and nobody's using it!"
    mike.say "Erm..."
    mike.say "Yeah, Kat..."
    mike.say "I would believe it."
    mike.say "Because it's my room..."
    show kat halloween blush at center, traveling (1.75, 0.1, (240, 1200))
    mike.say "Whoa!" with hpunch
    "Kat cuts me off again, but this time by pushing the door open with one hand."
    "Then she uses the other to physically drag me into my own bedroom."
    "The move comes as such a surprise that I don't even have time to react."
    hide kat with easeoutleft
    pause 0.1
    scene bg bedroom1
    show kat halloween defiant blush at center, zoomAt(1.75, (640, 1200))
    with hpunch
    "One moment I'm standing outside the door, the next I'm stumbling into the room."
    show kat at center, traveling(1.5, 0.1, (1040, 1040))
    "As soon as I'm over the threshold, Kat lets go of me."
    "She does this so that she can push herself bodily against the door."
    play sound door_slam
    with hpunch
    "And it slams shut as I almost fall flat on my face."
    "The only thing that stops me is the bed, which I collide with."
    "So at least I fall onto that, rather than the floor."
    "Instantly I flip myself onto my back, looking around for Kat."
    show kat halloween defiant blush at center, zoomAt(1.5, (640, 1040)) with ease
    pause 0.3
    hide kat
    show kat halloween defiant blush at center, zoomAt(1.5, (640, 1220)), swing(1.0, 1.0, 1.0, -3.0, 2.0)
    "Then I see her, walking towards me now the door is firmly closed."
    "And for the first time I can see that she's a little unstable on her feet."
    show kat talkative
    kat.say "Oh great..."
    kat.say "You found the bed!"
    show kat smile
    mike.say "How could I not, Kat?"
    mike.say "This is my bed!"
    show kat stuned
    "Kat's eyebrows shoot up at this, like it's a great revelation."
    show kat surprised
    kat.say "It is?!?"
    show kat smileclosed
    kat.say "What a lucky coincidence!"
    kat.say "That means nobody's going to walk in on us..."
    show kat smileclosed
    "She gives me what I think is supposed to be a sexy wink."
    show kat smile
    "Bit it kind of ends up looking more like she has something stuck in her eye."
    mike.say "Erm..."
    mike.say "Kat?"
    show kat happy
    kat.say "Yeah?"
    show kat smile
    mike.say "You're drunk!"
    show kat defiant
    kat.say "Oh yeah?"
    kat.say "Well you're nerdy...and sexy..."
    kat.say "You're a sexy nerd - and I want some of that action!"
    show kat smile
    "I'm starting to wonder just how much of the punch Kat managed to down tonight."
    "But then I see that she's not falling down drunk, and she's not slurring her speech either."
    "So I guess there's nothing stopping me from giving her exactly what she wants."
    "Plus it also helps that happens to be what I want too!"
    "I pat the mattress next to where I'm laid, inviting Kat to join me."
    mike.say "Then why don't you come and get some?"
    show kat enthusiastic
    "At the mere suggestion of gettin what she wants, Kat's face lights up."
    "She almost claps her hands together as she hurries to the bed."
    hide kat
    show kat halloween defiant blush at center, zoomAt(1.5, (640, 1040))
    show kat at center, traveling(1.75, 0.2, (640, 1200))
    pause 0.2
    show kat shocked with vpunch
    "And in her haste to reach me, she trips and tumbled onto it too."
    "But luckily for her, there's already someone there to catch her."
    kat.say "Oooh..."
    kat.say "Whoops..."
    "I manage to wrap my arms around Kat as she lands on top of me."
    "So we end up in a tangle of limbs as we bounce on the mattress."
    show kat surprised with vpunch
    kat.say "Oh..."
    show kat smile
    kat.say "Hi there, [hero.name]..."
    show kat defiant
    kat.say "Now come to momma!"
    hide kat
    show kat kiss halloween
    with fade
    "Without any further warning, Kat leans forward and clamps her lips over mine."
    "Then she closes her eyes and begins to kiss me hungrily."
    "At the same time I can feel her hands all over my body."









    "This only seems to make Kat hornier still."
    "Because she proceeds to stick her tongue almost down my throat."
    "And she grabs hold of my groin, squeezing it hard."
    "For a moment I actually thinks she's going to try and tear out the front of my pants."
    "But then I'm relieved to feel her locate the button and zipper."
    "After that, there's the desperate rush to get naked below the waist too."
    hide kat
    show kat halloween defiant blush at center, zoomAt(1.5, (640, 1040))
    with fade
    "The very second that happens, Kat puts her hands on my shoulders."
    "Then she raises herself up so that she's looming over me."
    "Putting her weight onto her elbows to free her hands, Kat makes a grab for something."
    "And it comes as little surprise to me when I find that what she's snatched is my cock!"
    "The sensation sends a jolt through my entire body, which in turn shakes the bed."
    mike.say "Argh..."
    mike.say "Whoa..."
    mike.say "Careful with that thing, Kat..."
    mike.say "It's the only one I've got!"
    "Kat chuckles at this, almost as if she thinks I'm joking."
    show kat at center, traveling(1.75, 0.2, (640, 1200))
    "Then she leans forwards, tugging on it even harder than before."
    show kat talkative
    kat.say "Come on, [hero.name]..."
    kat.say "Cut the crap!"
    kat.say "We both know this is a dream come true for you, right?"
    kat.say "The chance to make love to one of your favourite manga girls?"
    show kat smile
    "I have to admit that I'm starting to get seriously turned on by Kat's assertiveness here."
    "So much so that I resist the urge to tell her that Rem's far from a favourite of mine!"
    "I mean, she's okay."
    "But there are other characters that I'm far more into."
    "Though admitting as much here would probably blow my chances!"
    mike.say "Ah..."
    mike.say "Yeah, Kat..."
    "As soon as I say her name, Kat squeezes my cock cruelly hard."
    "And she raises a questioning eyebrow."
    mike.say "I..."
    mike.say "I mean...yeah, REM!"
    show kat happy
    "A knowing smile spreads slowly across Kat's face."
    "And she nods her head with visible satisfaction."
    show kat talkative
    kat.say "That's better!"
    kat.say "Now let's get things started..."
    show kat smile
    "Kat seems to be trying to take off my clothes without looking."
    "And I quickly decide to help her rather to get rid off her own costume."
    scene bg black
    show kat doggy halloween mike mouth_pleasure up
    with fade
    "I'm about to say something positive, when Kat turns her back and pushes her butt against me."
    "Before now I had no idea just how horny she was feeling."
    "Or how much she'd worked herself up for what we're about to do."
    "So when I start to sink straight into her, it comes as quite a surprise."
    "Kat's reaction is quite different to mine, as she seems to take it in her stride."
    show kat doggy mouth_hurt at stepback(speed=0.1, h=-10, v=5)
    play sexsfx1 slide_in
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    "Sure, she gasps at the sensation of my cock beginning to sink into her."
    "But it's easy to tell that she was anticipating all of this."
    show kat doggy eyes_close mouth_pleasure at stepback(speed=0.1, h=-10, v=5)
    play sexsfx1 fuck_calm loop
    play sound "sd/moans/sasha/sasha_panting.ogg" loop volume 10
    "Which means she starts to ride me almost as soon as I'm inside of her."
    "My surprise soon turns into sheer arousal as Kat takes the lead."
    "It doesn't seem to matter that she's one step ahead of me right now."
    show kat doggy at stepback(speed=0.1, h=-10, v=5)
    "I'm following her example willingly, rather than being pulled along in her wake."
    "It hardly occurs to me that I'm nodding my head as I look at her."
    "And I only really become aware of it myself when she starts to copy me."
    show kat doggy mouth_open at stepback(speed=0.1, h=-10, v=5)
    kat.say "Yeah..."
    kat.say "That's right..."
    kat.say "You want to give the Oni what she desires, don't you?"
    kat.say "No matter what she asks of you, it'll be granted?"
    show kat doggy mouth_pleasure
    "I'm still nodding away eagerly as Kat says all of this."
    "And why wouldn't I be?"
    show kat doggy at stepback(speed=0.1, h=-10, v=5)
    "She's bouncing up and down on my cock the whole time."
    "Which means that my brain is flooded with good sensations."
    "Hell, right now I'd probably agree to anything she asked me!"
    mike.say "Oh...yeah..."
    mike.say "Rem...gets..."
    mike.say "What...Rem...wants..."
    "Kat stops her own nodding."
    show kat doggy eyes_open
    "And she leans in so close I can see the patterns in the iris of her eyes."
    show kat doggy mouth_open
    kat.say "What Rem wants..."
    kat.say "Is to be fucked..."
    kat.say "Harder!"
    show kat doggy mouth_pleasure
    play sexsfx1 fuck_moderate loop
    play sound "sd/moans/sasha/sasha_moans_hard_medium.ogg" loop volume 10
    "Somehow Kat's demand seems to totally bypass my conscious mind."
    "Maybe I'm more drunk than I realised and acting on impulse."
    "Or maybe she's just asking me to do the exact thing I want."
    "Either way, my hands reach up and clamp onto her haunches."
    show kat doggy down at stepback(speed=0.1, h=-10, v=5)
    pause 0.1
    show kat doggy at stepback(speed=0.1, h=-10, v=5)
    "And as soon as I have a firm grip on her, I begin to pick up speed."
    "Before now I'd been happy to lie back and let Kat take the lead."
    "But suddenly she seems to have lit a fire under my ass."
    play sexsfx1 fuck_speed loop
    play sound "sd/moans/sasha/sasha_moans_hard_medium.ogg" loop volume 10
    show kat doggy speed eyes_up mouth_open tongueout at stepback(speed=0.1, h=-10, v=5)
    pause 0.1
    show kat doggy at stepback(speed=0.1, h=-10, v=5)
    "Because I can't keep from going harder and faster."
    "Soon it's not that I'm simply holding onto her waist for purchase."
    "Instead it's more like I'm the one holding her up altogether."
    "Kat struggles to stay propped up on her elbows, until finally she gives up."
    "And then she simply slumps down onto my bed."
    "Her head lands on my pillow, nestling there as I keep right on going."
    "Kat might have been coherent enough to issue orders at the start."
    play sexsfx1 fuck_sprint loop
    play sound "sd/moans/sasha/sasha_moans_hard_orgasm.ogg" loop volume 10
    "But by the time I feel her body starting to quiver from her orgasm, she's helpless."
    show kat doggy cum with hpunch
    "Simply clinging onto me for all she's worth as I lose it too."
    show kat doggy eyes_up mouth_pleasure with hpunch
    "The best Kat can manage is a series of moans at it all happens."
    with hpunch
    "And then I feel her almost curling into a ball under me."
    show kat doggy -speed with hpunch
    play sexsfx1 final_thrust
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    "I don't know if Kat's asleep or just lying still."
    "Either way I'm not about to disturb her by asking."
    "So instead I do the best that I can to make myself comfortable."
    "Then I wait patiently for sleep to come and claim me."
    stop sexsfx1 fadeout 0.5
    stop sound fadeout 0.5
    "Something that doesn't take long, thanks to my body being exhausted."
    "My mind too fades into welcome slumber, and then I'm lost in my dreams."
    $ kat.sexperience += 1
    $ game.pass_time(1)
    return

label kat_date_amusement_ice_cream_male:
    kat.say "Oooh..."
    kat.say "Ice-cream!"
    "Before I can really get a handle on what's going on, Kat grabs my hand."
    "Then she drags me after her through the crowd with scary show of strength."
    "And it's not until we're standing in the queue for the ice-cream stand that she stops."
    mike.say "Whoa..."
    mike.say "Erm..."
    mike.say "Okay..."
    mike.say "So I guess we're getting ice-cream?"
    "Kat looks at me like I'm the biggest buzz-kill imaginable."
    kat.say "Of course we're getting ice-cream!"
    kat.say "We have to get ice-cream..."
    kat.say "What trip to the amusement park would be complete without it?!?"
    "I still feel like my head is spinning as we get to the front of the queue."
    "But somehow I still manage to make out the menu and point to what I want."
    "Then I feel an ice-cream being shoved into my hand, and I'm marched away again."
    "I kind of think that I'm enjoying the thing as I eat it afterwards."
    "Though there's still the vague sensation of my being on autopilot."
    "And I don't dare to speak up about it either, just keeping quiet."
    "Because in the end, there are worse things than being forced to eat ice-cream!"
    $ kat.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
