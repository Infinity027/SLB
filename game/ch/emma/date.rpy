label emma_date_intro_valentine_male:
    mike.say "Hey, Emma..."
    mike.say "Happy Valentine's day!"
    mike.say "So, how's my amazing valentine tonight?"
    show emma blush
    "Emma flushes red as I shower her with compliments."
    "But she still manages to smile and nod her head."
    emma.say "I...I'm a little nervous, [hero.name]."
    emma.say "But I'm looking forward to our date!"
    return

label emma_date_intro_halloween_male:
    mike.say "Hey, Emma, I just remembered it's Halloween tonight."
    mike.say "We should have dressed up and gone trick or treating."
    mike.say "Or both!"
    show emma annoyed
    "Emma shakes her head at this, looking a little uncomfortable."
    emma.say "Oh no, [hero.name], I couldn't do that."
    emma.say "I'd be WAY too embarrassed!"
    "I'm about to make a joke, but then I hear the sincerity in Emma's voice."
    "When she says it'd be embarrassing, she really means it!"
    mike.say "Okay, Emma - let's just make the most of our date, okay?"
    return

label emma_date_intro_christmas_male:
    mike.say "Happy Christmas, Emma!"
    mike.say "I've been looking forward to tonight forever!"
    show emma happy
    "Emma smiles at this, but I can see that she's nervous."
    emma.say "Oh...okay, [hero.name]."
    emma.say "I'm sure we'll have a great time."
    "I nod and smile too, already toning down my excitement."
    "Because I don't want to put Emma off before we've even gotten started!"
    return

label emma_date_intro_birthday_male:
    mike.say "Happy birthday, Emma!"
    show emma happy
    emma.say "Oh, [hero.name] - you remembered!"
    mike.say "Of course I did, Emma."
    mike.say "Why else would I ask you on a date on your birthday?"
    emma.say "Oh...well...you know how some guys are..."
    mike.say "Ah, forget about all of that, Emma."
    mike.say "Let's just go have some fun, okay?"
    return

label emma_date_intro_mc_birthday_male:
    emma.say "Happy birthday, [hero.name]!"
    emma.say "I think we should celebrate that on our date too."
    mike.say "Wow, Emma..."
    mike.say "You really remembered my birthday?"
    show emma happy
    emma.say "Of course I did, [hero.name]."
    emma.say "You're the man of my dreams."
    emma.say "So I want to know everything about you that's real."
    return

label emma_date_eat_a_burger:
    "Emma blushes when her burger arrives, realising that she has to eat with her hands."
    "But she picks it up all the same, taking an experimental bite and chewing with a thoughtful look on her face."
    "Then she smiles, clearly liking the taste, and takes a much larger bite a moment later."
    return

label emma_date_buy_drink:
    if emma.is_visibly_pregnant:
        $ emma.love -= 10
        emma.say "I can't drink alcohol when I'm pregnant!"
        emma.say "Oh, [hero.name], that's so thoughtless of you!"
        $ hero.cancel_activity()
        hide emma
    else:
        "Emma accepts her drink, but only sips from it occasionally."
        "This gives me the impression that she's not a big-time drinker."
        "Most of the time she clutches the glass in both hands, as if afraid of losing it."
    return

label emma_date_play_darts:
    "From the way she holds the darts, I get the impression Emma's not that familiar with the game."
    "All the same, she seems eager to have a go, aiming them with an exaggerated show of concentration and care."
    "She doesn't come close to winning the game, but she plays doggedly and well for such a newcomer."
    return

label emma_date_pub_play_pool:
    "Emma nods and accepts a cue quite happily as I rack up the balls."
    "She's way better at pool than I thought she'd be too!"
    "Maybe there's a little bit of the hustler under that innocent front she puts on?"
    return

label emma_date_buy_a_round:
    if emma.is_visibly_pregnant:
        $ emma.love -= 10
        emma.say "I can't drink alcohol when I'm pregnant!"
        emma.say "Oh, [hero.name], that's so thoughtless of you!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - emma.love and emma.flags.drinks < 2):
        show drink emma
        "I offer to stand the next round out of common decency."
        "But the gesture really doesn't seem to curry any favor with Emma."
        "Huh - maybe she's just not that into sinking one drink after another?"
        $ game.active_date.score += 5
        if "rebel" in emma.traits:
            $ game.active_date.score += 5
        $ emma.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Emma doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label emma_offer_drink:
    show emma
    mike.say "Emma, would you like a drink?"
    if emma.flags.nodrink:
        emma.say "I don't really drink."
        $ hero.cancel_activity()
        hide emma
    elif (hero.charm >= 60 - emma.love and emma.flags.drinks < 2) or date_girl == emma:
        emma.say "Yeah sure."
        hide emma
        show drink emma
        call expression emma.get_chat from _emma_offer_drink
        if emma.love <= 25:
            $ emma.love += 1
        elif date_girl == emma and game.active_date:
            $ game.active_date.score += 5
        hide drink
        $ emma.set_flag("drinks", 1, "day", mod="+")
    else:
        emma.say "Sorry, I don't feel like drinking."
        $ hero.cancel_activity()
        hide emma
    $ emma.set_flag("interact", 1, 1, "+")
    return

label emma_dance_with:
    "Despite my best efforts to make her feel comfortable, Emma freezes up almost the moment we're on the dance-floor."
    "She looks almost alarmed as she clings to me, flinching away from the other couples around us and the sound of the music."
    "I should be annoyed by her awkwardness, but there's just something appealing about the way she looks to me for protection..."
    return

label emma_date_play_arcade_intro_male:
    emma.say "Oh, I can't wait to get my hands on a joystick, [hero.name]!"
    emma.say "It feels like so long since I was in an arcade."
    emma.say "This was SUCH a good idea!"
    "I can't help grinning from ear to ear as Emma pulls me along."
    "In fact, I even resist a little, just to make it last longer!"
    "Of course the truth is that I'm as eager to get started as she is."
    "I'm just not used to bringing a girl along to the arcade that feels the same way."
    mike.say "I'm just glad you said you'd come along, Emma."
    mike.say "Most girls aren't into videogames, or arcades either!"
    emma.say "Well, I guess that means I'm not like most girls."
    emma.say "Ah...there it is!"
    emma.say "That's the one I was looking for..."
    "Emma hurries over to a particular arcade cabinet."
    "And she's feeding coins into it before I can even identify the game!"
    mike.say "'Priby's Fantasyland'?"
    mike.say "I didn't even know that was released in the arcade."
    mike.say "I thought it was a console exclusive!"
    "Emma smiles and shakes her head at this."
    "And she explains it to me like I'm some kind of moron."
    emma.say "Oh no, [hero.name]."
    emma.say "It saw a limited release in Japanese arcades."
    emma.say "But, of course, only a couple of hundred units were translated."
    emma.say "And those are the only ones you see over here in the West."
    "I blink at this, feeling like I've been given a lecture."
    "I'm just not used to being schooled on videogames by someone else!"
    emma.say "Anyway, that's enough talking."
    emma.say "Let's play!"
    return

label emma_date_play_arcade_win_male:
    "Okay, I have a confession to make."
    "I might not have known much about the convoluted history of the game."
    "But I sure as hell played the shit out of it back in the day."
    "And it doesn't take long for Emma to realise that I'm an expert."
    emma.say "Hey!"
    emma.say "How did you know about that shortcut?"
    emma.say "Nobody knows about stuff like that!"
    mike.say "You know how it is, Emma."
    mike.say "A good player keep his cards to his chest!"
    emma.say "That's poker, [hero.name] - not videogames!"
    "Pretty soon the game's eaten up our supply of coins."
    "And before we can go get more, we have to compare scores."
    "Which reveals that my total beats Emma's."
    "Not by much, but just enough to make me the winner."
    emma.say "Wow, [hero.name]."
    emma.say "I thought I was the absolute best at this game!"
    mike.say "All this proves is that I was better today, Emma."
    mike.say "And I'm always up for a rematch."
    "Being a humble winner seems to do the trick."
    "Emma nods and smiles, happily consoled by my words."
    return

label emma_date_play_arcade_lose_male:
    "Okay, I have a confession to make."
    "Not only do I know almost nothing about the convoluted history of the game."
    "I also never played it all that much back in the day!"
    "And it doesn't take long for Emma to show me up either."
    emma.say "Hey!"
    emma.say "How did you miss that hidden power-up?"
    emma.say "Everyone knows that it's there, [hero.name]!"
    mike.say "Ah...I don't know, Emma!"
    mike.say "I guess it's just been a while since I played this game."
    emma.say "That or you've got amnesia!"
    "Pretty soon the game's eaten up our supply of coins."
    "And before we can go get more, we have to compare scores."
    "Which reveals that Emma's total beats mine."
    "And by that I mean it's not even close!"
    emma.say "Wow, [hero.name]."
    emma.say "You're really bad at this game!"
    mike.say "Well, I never really played it that much, Emma."
    mike.say "I just jumped on because you seemed to love it so much."
    "Emma shakes her head, but I can see that she's smiling."
    emma.say "That's sweet of you, [hero.name]."
    emma.say "But next time, let's pick a game we both like."
    emma.say "Okay?"
    return

label emma_dick_reactions:
    if not emma.flags.seendick:
        $ emma.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions emma scared
            emma.say "Th...that's...big!"
            emma.say "That's VERY big!"
            mike.say "Don't worry, Emma - I'll be gentle."
            emma.say "O...okay..."
            emma.say "So long as you promise not to hurt me..."
            $ emma.sub += 10
            $ emma.love -= 10
        elif hero.has_skill("smalldick"):
            show dick reactions emma smile
            emma.say "Oh, there he is."
            emma.say "Hey there, little guy!"
            mike.say "What do you mean 'little'!"
            emma.say "I didn't mean it like that, [hero.name]."
            emma.say "It's just cute, that's all!"
            $ emma.sub -= 10
            $ emma.love += 10
        hide dick reactions
    return

label emma_halloween_invitation:
    show emma
    "I know that Emma can be a little shy and retiring sometimes."
    "But that doesn't mean I shouldn't invite her to the Halloween party."
    "I mean, it's not like I'm trying to drag her to a busy nightclub."
    "This is just going to be a party at my place with a handful of friends."
    "It should be a chance for her to get to know them and have a good time."
    "No pressure to do anything that she really doesn't want to do."
    "So I bring it up as soon as I get the chance."
    mike.say "Emma..."
    mike.say "We're throwing a Halloween party at my place this year."
    mike.say "You want to come along?"
    show emma a
    show fx exclamation
    "Emma's eyes go a little wide as she thinks about the offer."
    "I can see that she's turning it over in her mind before replying."
    emma.say "What, like a party with games and things?"
    emma.say "Bobbing for apples and stuff like that?"
    "I nod at this, wanting to encourage her."
    mike.say "Yeah, I suppose so."
    mike.say "But kind of more for grown-ups, yeah?"
    "Emma nods."
    emma.say "Oh...I see."
    mike.say "Anyway..."
    mike.say "I wondered if you wanted to come along?"
    mike.say "You could be my date, if you like?"
    if emma.love >= 100:
        "For a moment, I'm sure I know what her answer will be."
        "I'm sure that Emma's building up the courage to say no."
        emma.say "Okay, [hero.name]."
        show emma b
        emma.say "I'll come to your party."
        "Well, colour me surprised!"
        mike.say "You will?"
        mike.say "That's great, Emma!"
        show emma a
        emma.say "But...but wait a minute!"
        emma.say "You said I could be your date, right?"
        "I nod at this."
        mike.say "Erm, yeah, Emma."
        emma.say "That means you'll be with me all night?"
        emma.say "That's what a date does?"
        mike.say "Sure, Emma - if that's what you want."
        emma.say "Okay, [hero.name]."
        show emma b happy
        $ emma.love += 1
        emma.say "I'll come to the party."
        emma.say "So long as you stay with me the whole time."
        "I try as best I can to look serious as I agree to what she wants."
        "But I'm almost laughing inside as I do so."
        "Not only is Emma coming to the party."
        "She's determined to cling to my side all night too."
        "I should buy a lottery ticket - because this is my lucky day!"
        $ game.flags.halloween_girl = "emma"
    else:
        emma.say "Erm..."
        emma.say "It's sweet of you to ask, [hero.name]."
        emma.say "Really, it is."
        "I can already sense a 'but' hanging in the air."
        "So I decide to call it out before she does."
        mike.say "But..."
        emma.say "But I don't like the sound of it."
        emma.say "An entire house full of strangers!"
        "I want to object, to argue with her."
        "But I can see that would be the wrong thing to do."
        "And so I nod in agreement."
        mike.say "If that's how you feel, Emma."
        mike.say "I don't want to force you."
        show emma b happy
        "Emma gives me a weak smile."
        "And I give her one in return."
        emma.say "Thanks for understanding, [hero.name]."
        emma.say "You're the best."
        show emma normal
        mike.say "No worries, Emma."
        "I guess there's nothing else I can do."
        "Other than hope for better luck next time."
    return

label emma_halloween_arrival:
    scene bg house
    with wiperight
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But I get caught out again as a flurry of blades flash before my eyes."
    mike.say "Aargh!"
    mike.say "What the hell?!?"
    with hpunch
    "I stumble back into the hallway, almost falling on my ass."
    show emma halloween hat a
    "It's only when I manage to regain my balance that I see what's happening."
    emma.say "Oops..."
    emma.say "Sorry, [hero.name]."
    emma.say "I was just trying to surprise you!"
    "I see Emma standing on the doorstep."
    "She has one hand over her mouth and a bladed glove on the other."
    "Suddenly the stripey jumper and fedora that she's wearing make sense."
    mike.say "You..."
    mike.say "You're supposed to be Frederick Booger?!?"
    "Emma nods, cheering up at my guessing what she's dressed as."
    show emma b
    emma.say "Yeah, that's right!"
    emma.say "Pretty neat, huh?"
    menu:
        "Compliment":
            mike.say "The costume's great, Emma."
            mike.say "It's just that movie gave me nightmares!"
            show emma a
            "Emma's eyes go wide at the admission."
            "And she shakes her head hastily."
            emma.say "Oh god..."
            emma.say "I'm SO sorry, [hero.name]."
            emma.say "I had no idea."
            "I shake my head, dismissing her concerns."
            mike.say "Don't worry about it."
            mike.say "I was just a kid at the time."
            mike.say "I've grown out of it since then."
            "Emma nods, looking relieved."
            emma.say "Are you sure, [hero.name]?"
            emma.say "Because I can always take it off?"
            mike.say "How about we save that for later?"
            mike.say "Maybe when we get some time alone?"
            "Emma looks puzzled for a moment."
            "But then realisation dawns."
            show emma blush
            $ emma.love += 1
            "And she giggles with embarrassment."
        "Criticise":
            mike.say "Yeah, well..."
            mike.say "That movie gave me nightmares as a kid!"
            show emma a
            "Emma's eyes go wide at the admission."
            "And she shakes her head hastily."
            emma.say "Oh god..."
            emma.say "I'm SO sorry, [hero.name]."
            emma.say "I had no idea."
            mike.say "Ah..."
            mike.say "It's not something I like to talk about."
            mike.say "It still kind of creeps me out, big time."
            show emma sad
            "Emma bites her lip, unsure of what to do next."
            emma.say "Can I...still come in?"
            mike.say "Sure...sure..."
            mike.say "I'll just have to think about something else."
            "Oh shit."
            "This is going to be awkward..."
    scene bg black with dissolve
    pause 1
    return

label emma_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween a annoyed at right5
    show emma halloween a at left5
    with fade
    sasha.say "Geez..."
    sasha.say "What's the matter with you?"
    sasha.say "I was only trying to start a conversation!"
    "I turn around to see Sasha shaking her head at Emma."
    "And while the former looks pissed, the latter seems terrified!"
    mike.say "Hey, Sasha..."
    mike.say "Hey, Emma..."
    mike.say "What's going on?"
    "Emma looks relieved to see me."
    "She hurries to my side, almost hiding behind me."
    sasha.say "It's your date, [hero.name]."
    sasha.say "She's scared by the sound of my voice!"
    menu:
        "Defend Emma":
            mike.say "Hey, Sasha."
            mike.say "That's not fair!"
            mike.say "Emma's just a little shy, that's all."
            emma.say "Y...yeah, [hero.name]."
            emma.say "I have social anxiety issues!"
            "Sasha shakes her head at this."
            sasha.say "I was just trying to be friendly."
            sasha.say "You know - be a good host?"
            mike.say "Just leave Emma to me, Sasha."
            mike.say "I think she's had all of the hosting that she can take from you!"
            hide sasha
            show emma halloween a at center
            with moveoutleft
            $ sasha.love -= 2
            $ emma.love += 2
            "Sasha harumphs and storms off into the crowd."
            "But I can feel Emma clinging to me still."
            "And it's a very pleasant sensation indeed."
        "Defend Sasha":
            mike.say "Emma, what the hell?"
            mike.say "Sasha was only trying to be friendly."
            mike.say "You know - being a good host?"
            show emma sad
            "Emma shakes her head at this."
            emma.say "Y...you know I have issues, [hero.name]."
            emma.say "Social anxiety...we talked about it!"
            mike.say "But you still came to the party, Emma!"
            mike.say "If it's as bad as you say, then you shouldn't be here!"
            $ emma.love -= 4
            "Emma looks at me, a hurt expression in her eyes."
            emma.say "I...I'm sorry, [hero.name]."
            emma.say "I'll try harder in future - I promise!"
            "I nod and force a smile onto my face."
            "But I'm still not convinced that she actually means it."
    scene bg black with dissolve
    pause 1
    return

label emma_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show emma halloween b happy
    with fade
    "Emma's happily chatting away to me about some random subject."
    "I'm nodding and trying as best I can to keep up with her."
    "I but keep glancing across to the makeshift dance-floor."
    "My foot just won't stop tapping to the beat!"
    mike.say "Emma..."
    show emma normal
    emma.say "Oh...yes, [hero.name]?"
    mike.say "You want to dance?"
    show emma a
    show fx exclamation
    "I see Emma's eyes go wide at the idea."
    "She stares at the dance-floor, almost like she's afraid of it."
    emma.say "I...I don't know."
    emma.say "I guess we could."
    emma.say "If that's what you want..."
    menu:
        "Dance":
            mike.say "Of course I want to dance, Emma."
            mike.say "This is a party - a chance to have fun!"
            hide emma
            show dance emma halloween
            with fade
            "Emma lets me lead her onto the dance-floor."
            "And I can see that she's trying her best."
            "But it doesn't take long for me to realise there's something wrong."
            "Emma finches whenever another body comes close to her."
            "Sure, it means that she presses herself closer to me."
            $ emma.love -= 2
            "But that's no consolation for the look of discomfort on her face."
            "And the worst thing knowing that I've almost forced it on her too."
            "I don't want to cut the dance short."
            "As that would only serve to draw more attention."
            "So I have to ride it out until the song comes to an end."
            "And while that might only be a couple of minutes."
            "It feels like an eternity!"
        "Do not dance":
            "I almost strike my forehead in frustration with myself."
            "What in the hell was I thinking?"
            "Emma's the shyest girl I've ever met."
            "And I just asked her to put herself on public display!"
            mike.say "You know what, Emma - forget about it."
            emma.say "R...really?!?"
            mike.say "Yeah, it already looks crowded."
            mike.say "And I'm having a good time just talking to you."
            show emma happy
            $ emma.love += 2
            "Emma's face lights up at this."
            "She practically beams with happiness."
            emma.say "That's great, [hero.name]."
            emma.say "Because I'm having a good time too!"
            emma.say "I'm usually nervous at parties."
            emma.say "But with you it's different!"
            "I nod, letting Emma know that we're on the same page."
            "And on the inside, I'm glad to have read her so well."
    scene bg black with dissolve
    pause 1
    return

label emma_halloween_sex:
    if not emma_too_small(10):
        scene bg livingroom
        with dissolve
        "The party's winding down by now, the dancing giving way to people just chilling out."
        "Most of the guests seem to be drunk and tired, wanting to chat and relax."
        "And so this seems like the perfect time to shrug off the role of host."
        "Finally I can reward myself for a hard night's work and indulge too."
        "And I know just what I want to indulge in, as well as with whom..."
        show emma halloween b
        mike.say "Hey, Emma."
        show emma halloween a
        emma.say "Ooh..."
        emma.say "Sorry, [hero.name] - did you say something?"
        emma.say "I was almost falling asleep!"
        mike.say "Well don't drop off just yet."
        mike.say "Not before we get the chance to have some fun!"
        show fx question
        "Emma looks a little puzzled at this."
        emma.say "What do you mean?"
        emma.say "Isn't that what we've been doing all night?"
        mike.say "Yeah, I know that, Emma."
        mike.say "But I mean a different kind of fun."
        mike.say "You know what I mean?"
        show fx exclamation
        show emma halloween a blush
        emma.say "Oh...OH!"
        "Emma's cheeks flush red as she catches my meaning."
        "She looks this way and that, as if afraid someone might overhear."
        emma.say "Are you sure, [hero.name]?"
        emma.say "What if someone hears us?"
        "I shake my head, dismissing her concerns."
        "Sure, I could let her reluctance bother me."
        "But that's just one of Emma's little quirks."
        "Her innocence makes her seem that much cuter."
        mike.say "No worries, Emma."
        mike.say "We can sneak off to my room."
        mike.say "Nobody's going to notice we're gone."
        show emma blush
        "At this, Emma nods and giggles."
        show emma b
        "She takes hold of my hand and lets me lead the way."
        "And I don't waste any time making for my bedroom."
        "Once there, Emma waits patiently for me to open the door."
        scene bg bedroom1
        show emma halloween b blush
        with fade
        "And then she hurries inside, as if still afraid of being caught."
        "I lead her over to the side of the bed and she follows without protest."



        "She climbs backwards onto the bed without a word from me."
        "And I can see a look of anticipation growing on her face."
        "I don't waste a second in pulling off my own costume."
        "That done, I climb onto the bed too."
        "But I'm careful to approach her slowly and with care."
        show emma missionary halloween with fade
        "Sure, part of the reason for that is me wanting to reassure her."
        "But it's also because I want to take my time about it too."
        "Watching Emma as she waits for me to reach her..."
        "Well, let's just say that it's quite an ego-rub!"
        show emma missionary mike
        "Emma parts her legs as I lie atop her."
        "And I gently slide my hand between her thighs."
        "My fingers trace the outline of her lips, gently teasing her."
        "She whimpers at the sensation, but doesn't tell me to stop."
        "Pretty soon I can feel that she's opening up down there."
        "She's slick and slippery, wanting more than just my fingers."
        emma.say "Ah..."
        emma.say "I...I'm ready."
        emma.say "Please...can I have it?"
        show emma missionary mikehand
        "As gently as I teased her with my fingers, I give Emma what she wants."
        "There's resistance at first, but only for a moment."
        "It's the kind that only makes what follows more intense."
        show emma missionary vaginal pleasure
        "And when it passes, I sink deep into Emma."
        "I don't stop until my cock's as far in as it can go."
        "She moans the entire time, urging me on in my efforts."
        "Not that I need to the motivation!"
        "It's only as I begin to pick up speed that I notice a change in her."
        "Slowly at first, but then building with each second that passes."
        "Emma starts to lose the trepidation and shyness she had before."
        "And as she begins to give in to the experience, she comes alive."
        "Gone is the timid persona that she had when we started."
        "And in it's place I see her true appetite begin to show."
        "Emma nods almost desperately as I thrust in and out of her."
        "She holds onto me as if she's determined to ride me to the last."
        "And her formerly demure moans are now sounds of deep hunger too."
        emma.say "Oh yeah..."
        emma.say "That's it..."
        emma.say "I love...your cock...inside me!"
        "I don't know if it's a coincidence or if Emma pushes me over the edge."
        "But either way, I can feel myself about to lost it!"
        show emma missionary ahegao with vpunch
        "With one last thrust, I push as deep inside of her as I can go."
        show emma missionary creampie with vpunch
        "And then I shoot my load into her."
        with vpunch
        "Emma cums before I'm done, squirming and wriggling around my cock."
        "And as she sinks into the warmth of the afterglow, she becomes her former self."
        "Her face is demure, her smile satisfied and sated."
        $ emma.sexperience += 1
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
