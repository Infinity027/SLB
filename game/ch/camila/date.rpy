label camila_date_intro_valentine_male:
    mike.say "I...I've never been a cop's valentine before, Camila."
    mike.say "I have to admit, I'm kind of nervous!"
    "Camila shakes her head and gives me a crooked smile."
    camila.say "There's nothing to it, [hero.name]."
    camila.say "Buy me drinks, laugh at my jokes, and show me a good time."
    camila.say "Do all of that and you're golden!"
    return

label camila_date_intro_halloween_male:
    mike.say "Hey, Camila - you are looking good tonight!"
    mike.say "Did you dress up as a sexy cop for Halloween?"
    "Camila laughs and shakes her head at this."
    camila.say "Nah, [hero.name] - I'm this hot all year round!"
    camila.say "And I normally spend Halloween busting drunken fools in costumes."
    "I don't need to be told when Camila's in the mood to flirt."
    "And right now I can almost feel the heat coming off of her."
    mike.say "Well, officer, I might have to misbehave - just so you can use your cuffs on me!"
    camila.say "Oh yeah - that kind of thing can be arranged!"
    return

label camila_date_intro_christmas_male:
    mike.say "You ready for our date, Camila?"
    "Camila nods, but she can't keep herself from yawning at the same time."
    camila.say "Yeah...yeah...sorry, [hero.name]."
    camila.say "I'm just a little tired, that's all."
    camila.say "Christmas seems to bring out the worst in the criminal element, you know?"
    mike.say "Ah, that sucks, Camila."
    mike.say "I'll do the best I can to take your mind off it."
    return

label camila_date_intro_birthday_male:
    mike.say "Happy birthday, Camila!"
    camila.say "Huh?!?"
    camila.say "Is it that time of year already?"
    camila.say "I'd have forgotten if you hadn't reminded me!"
    mike.say "Oh...okay..."
    mike.say "Is your birthday like...not a big deal?"
    camila.say "Of course it is, [hero.name] - I just have a lot on my mind, as usual."
    camila.say "But let's forget all about that and relax for a while, okay?"
    return

label camila_date_intro_mc_birthday_male:
    camila.say "Happy birthday, [hero.name]!"
    camila.say "So I guess we're celebrating that tonight, huh?"
    mike.say "Ah...yeah, Camila."
    mike.say "But how did you know it was my birthday?"
    mike.say "I don't remember telling you the date."
    camila.say "You didn't - I looked you up in the police records."
    mike.say "Wait...what?!?"
    mike.say "I don't have a criminal record - do I?"
    camila.say "No, but you reported your wallet stolen a while back, remember?"
    camila.say "They took down your details when you went down to the station."
    return

label camila_date_pub_male:
    "Almost the same moment we walk into the pub, I know I made the right choice."
    "It's like I can see and hear Camila breathe out and start to relax."
    "And pretty soon she seems to forget all about her day at work."
    "Instead she's all joking and laughter, the life and soul of the party."
    return

label camila_date_cinema_male:
    camila.say "Ah, this is just what I needed, [hero.name]."
    camila.say "A chance to sit back and forget about the real world!"
    mike.say "Me too, Camila."
    mike.say "Let's grab some popcorn."
    return

label camila_date_familyrestaurant_male:
    "I can see that Camila's not comfortable the moment we walk in the door."
    "And by the time we're seated and looking at the menu, she's frowning."
    "I don't know if it's the noise or the sheer number of people in here."
    "But she definitely looks like she'd rather be anywhere else right now."
    return

label camila_date_restaurant_male:
    "Camila sits down at the table and glances over the menu."
    "But nothing on there seems to catch her eye."
    "It's not like she doesn't want to be here."
    "And yet she just looks really bored all of a sudden!"
    return

label camila_date_amusmentpark_male:
    "Camila stays close to me the whole time we're wandering around the park."
    "She even holds my hand and leans against me too, which feels really good."
    "But she never really seems to relax as we're jostled by the crowds."
    "It's almost like she's still on duty, watching everyone like they're suspects."
    return

label camila_date_ride_the_ferris_wheel:
    mike.say "You want to ride the ferris wheel, Camila?"
    camila.say "Hmm..."
    camila.say "If you want to, [hero.name], I guess..."
    return

label camila_date_waterpark_male:
    "Camila makes a show of smiling at me as we walk into the water."
    "But none of the stuff that I enjoy seems to capture her interest."
    "And pretty soon, I start to feel like a kid dragging an adult after myself!"
    return

label camila_date_park_male:
    camila.say "Geez, I remember busting this one guy over there, by the lake!"
    mike.say "Ah, yeah, Camila - that's great..."
    camila.say "And there was a bunch of hookers that used to hang around right around here."
    camila.say "I busted their asses too!"
    mike.say "That's really nice."
    mike.say "So romantic, Camila..."
    return

label camila_date_eat_a_burger:
    "Camila grabs the burger with both hands, biting into it a second later."
    "She devours the mouthful and takes another before I've even picked mine up!"
    "That said, the look of delight on her face as she does so is pretty cute."
    "And so is the way she grins up at me when she realises I'm watching her."
    return

label camila_date_buy_drink:
    if camila.is_visibly_pregnant:
        show camila angry
        $ camila.love -= 10
        camila.say "Don't you think this kid of ours has it hard enough?"
        camila.say "They've already got a mom with a dangerous job."
        camila.say "The last thing they need is for me to soak them in booze too!"
        $ hero.cancel_activity()
        hide camila
    else:
        camila.say "Ah, thanks, [hero.name]."
        camila.say "I needed that!"
        mike.say "No kidding, Camila."
        mike.say "You almost drank it down in one!"
    return

label camila_date_play_darts:
    "Camila nods and walks over to the board when I suggest playing darts."
    "But she doesn't seem to be enjoying herself the whole time we play."
    "And I don't know if I beat her because she's bad at the game or just not trying."
    return

label camila_date_pub_play_pool:
    "Camila shrugs and agrees to a game of pool when I point out that the table's free."
    "But she plays like it's just something that she's doing to humour me."
    "And so the game quickly becomes a chore."
    return

label camila_date_buy_a_round:
    if camila.is_visibly_pregnant:
        show camila angry
        $ camila.love -= 10
        camila.say "Don't you think this kid of ours has it hard enough?"
        camila.say "They've already got a mom with a dangerous job."
        camila.say "The last thing they need is for me to soak them in booze too!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - camila.love and camila.flags.drinks < 2):
        show drink camila
        camila.say "Ah, where are you going, [hero.name]?"
        mike.say "To get another round, Camila."
        camila.say "No, you're not."
        camila.say "It's my round!"
        $ game.active_date.score += 5
        if "rebel" in camila.traits:
            $ game.active_date.score += 5
        $ camila.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Camila doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label camila_dance_with:
    "I practically have to drag Camila up and out of her seat to get her to dance."
    "And even when we're up there, she still moves like she's being pulled around."
    "More than once she actually manages to step on my feet."
    "Which makes the whole experience pretty painful, in more ways than one!"
    return

label camila_date_play_arcade_intro_male:
    camila.say "Ah, [hero.name]..."
    camila.say "This place is full of kids!"
    camila.say "Can't we go do something more adult?"
    "I tear my attention away from the flashing lights and enticing noises of the arcade."
    "And I manage to do so for just long enough to see that Camila doesn't look happy."
    mike.say "I know this isn't your kind of thing, Camila."
    mike.say "But just give it a chance, okay?"
    mike.say "I truly believe that there's a videogame for everyone!"
    camila.say "Honestly, [hero.name], I doubt that!"
    "I cast my gaze around, looking for something Camila might actually like."
    "The racing games look too much like people speeding."
    "And the fighting games like brawls she might have broken up in the past."
    "But then I spot a light-gun game that might be the answer to my prayers."
    mike.say "What about this one, Camila?"
    mike.say "'Virtual Cop' - it's got you written all over it!"
    "Camila stands in front of the arcade cabinet, arms crossed over her chest."
    "She wrinkles her nose and shakes her head, clearly not impressed."
    camila.say "Okay, [hero.name], here's the deal..."
    camila.say "If I play this one game with you, can we get out of here?"
    "I nod in response, already pumping coins into the slot."
    "Then I straighten up, handing one of the light-guns to Camila."
    mike.say "Here we got, partner."
    mike.say "Let's bring justice to these mean streets!"
    "Camila rolls her eyes and shakes her head at this."
    "But I can see a grudging smirk on her face too."
    "So if I'm lucky, this might not be a disaster after all..."
    return

label camila_date_play_arcade_win_male:
    "I'm an old hand at this game, on console and in the arcade."
    "And so I have no problem gunning down the hoods that pop up on the screen."
    "But right from the start, Camila seems to be having issues."
    camila.say "What the hell?!?"
    camila.say "I had that guy nailed!"
    camila.say "He never should have gotten that shot off!"
    "I risk a sideways glance at Camila."
    "And I see that she's fuming, jaw clenched tight."
    mike.say "Loosen up a little, Camila."
    mike.say "This is a game, remember?"
    mike.say "You're supposed to be having fun!"
    "All that I get in the way of response is muttering and cursing."
    "And for the rest of the game, Camila fumes and snorts away."
    "I wouldn't be surprised to see steam coming out of her ears and nostrils, she's that mad!"
    "Once we're done, she slams the light-gun into the holster on the side of the cabinet."
    camila.say "There, I played your dumb game."
    camila.say "Are you happy now?!?"
    mike.say "Yeah, Camila, I am."
    mike.say "It was fun to play at being your partner."
    mike.say "Because I could never be as tough as you in real life!"
    "Camila opens her mouth to speak, but then no words come out."
    "And it's then I realise she's actually blushing."
    camila.say "Ah...you jerk!"
    camila.say "You always know just what to say to me, [hero.name]."
    return

label camila_date_play_arcade_lose_male:
    "I chose this game in the hope that it might appeal to Camila."
    "But it's not one that I've played much before now."
    "And that soon starts to show."
    camila.say "[hero.name], cover me!"
    camila.say "I'm going in - and I NEED backup!"
    camila.say "Where in the hell is that backup?!?"
    "I risk a sideways glance at Camila."
    "And I see that she's focused like a laser on the game."
    "Staring down the sights of her light-gun as if her life depends on it!"
    mike.say "Loosen up a little, Camila."
    mike.say "This is a game, remember?"
    mike.say "You're supposed to be having fun!"
    camila.say "What are you talking about, [hero.name]?"
    camila.say "This IS fun!"
    camila.say "Suck on that, you piece of filth!"
    "I'm pretty sure that she meant that insult for an enemy in the game."
    "But all the same, I look straight ahead and focus on shooting away."
    "Once we're done, Camila slams the light-gun into the holster on the side of the cabinet."
    camila.say "There, I played your dumb game."
    camila.say "Are you happy now?!?"
    mike.say "Well, yeah, Camila."
    mike.say "You were pretty awesome - a real badass!"
    "And it's then I realise she's actually blushing."
    camila.say "Ah...you jerk!"
    camila.say "You always know just what to say to me, [hero.name]."
    return

label camila_halloween_invitation:
    show camila
    "I know that I want to invite Camila to the Halloween party."
    "In fact there's no other girl that I can imagine asking to come."
    "I just don't know how to go about it."
    "Anyone else I'd probably just come out and ask."
    "But Camila's a tough cop, and she can be kind of intimidating."
    "How do I pitch something like a costume party to her?"
    "What if she thinks it's silly and childish?"
    "But she takes the decision out of my hands the next time we meet."
    "Mainly because I've forgotten how good of a detective she is!"
    show camila bored
    camila.say "Come on, [hero.name]."
    camila.say "Out with it!"
    mike.say "Huh?"
    mike.say "Out with what, Camila?"
    "Camila narrows her eyes and shakes her head."
    "Then she chuckles to herself."
    camila.say "I know all the signs."
    camila.say "You've got something on your mind!"
    "Caught bang to rights, there's no point denying it."
    mike.say "Ah..."
    mike.say "Okay, Camila - you got me."
    mike.say "We're having a Halloween party at my place."
    mike.say "And I wanted you to come along."
    show camila normal
    "Camila raises an eyebrow at this."
    "Which at least means she's intrigued by the idea, right?"
    mike.say "It's a costume party too."
    mike.say "So you'd have to get dressed up!"
    if camila.love >= 100:
        show camila flirt
        "I don't know if it's the mention of costumes."
        "Or else Camila's just had time to turn the idea over in her mind."
        "But her lips curl into a smile a moment later."
        $ camila.love += 1
        camila.say "You know what - that sounds like fun!"
        camila.say "Halloween's always insane down at the precinct."
        camila.say "Something about that holiday brings out the crazies!"
        camila.say "But I can't recall the last time I was off duty this time of year."
        show camila happy
        camila.say "So I'll call in a favour and come to your party."
        "I can't keep the smile from spreading across my face."
        mike.say "That's great, Camila!"
        mike.say "Any ideas for your costume?"
        show camila normal
        "Camila cocks her head on one side as she considers the question."
        show camila flirt
        "And then a slow smile spreads across her face too."
        camila.say "Oh, I've got a good one."
        camila.say "But I want to keep it a surprise."
        camila.say "Let's just say that I love some sci-fi movies too!"
        "I desperately want to pump Camila for more details."
        "But if she's determined to keep it a secret then I'd be wasting my time."
        "Instead I console myself with the knowledge that she's coming to the party."
        "And I'm already getting excited to see what she actually comes along dressed as on the night."
        $ game.flags.halloween_girl = "camila"
    else:
        "I don't know if it's the mention of costumes."
        "Or else Camila's just had time to turn the idea over in her mind."
        "But she curls her lip and shakes her head a moment later."
        camila.say "Nah, [hero.name]."
        camila.say "I don't think I can make it."
        mike.say "Are you sure, Camila?"
        mike.say "I haven't actually told you the date yet!"
        "I keep a smile on my face through sheer force of will."
        "All the time afraid of coming over as desperate."
        show camila bored
        camila.say "It probably won't make a difference if you do."
        camila.say "Halloween's always insane down at the precinct."
        camila.say "Something about that holiday brings out the crazies!"
        camila.say "In fact, I can't remember the last time I wasn't working my ass of this time of year."
        "I nod, trying to cover up my disappointment."
        "But my enthusiasm for the party is already draining away."
        mike.say "Okay, Camila."
        mike.say "I guess it can't be helped."
        show camila sad
        "Sensing my change of mood, Camila tries to make amends."
        camila.say "I'm sorry, [hero.name]."
        show camila normal
        camila.say "Look, I'll try to swing by for a couple of minutes if I can."
        camila.say "But I can't promise anything."
        "I nod and smile, realising that it's better than nothing."
    return

label camila_halloween_arrival:
    scene bg house
    "Opening the door, I find myself staring down the barrel of a gun!"
    "Instinct takes over and I leap backwards, yelping in surprise."
    mike.say "Argh..."
    mike.say "Take all the candy you want!"
    mike.say "Just don't shoot me - please!"
    "I can't see what reaction this inspires in the person holding the gun."
    "And that's because I'm too busy cowering behind the door to look!"
    "But I hear them laughing, and then I recognise their voice."
    camila.say "Geez, [hero.name], calm down."
    camila.say "It's not even a real gun!"
    mike.say "Camila?"
    "I peep around the door to confirm my suspicions."
    show camila halloween bored
    "And what I see leaves me lost for words."
    camila.say "Not tonight."
    show camila happy
    camila.say "Tonight I'm Robo-Camila!"
    camila.say "The future of law-enforcement!"
    "I must have seen the movie a hundred times in the past."
    "But I never saw Robofficer looking like this before!"
    "Camila's done out head to toe in chrome plating."
    "And everything else apart from her face is covered in black rubber."
    "She even spins the gun around on her finger before holstering it too!"
    "Camila's eyes are hidden behind the visor of her helmet."
    "But the smile on her face is impossible to miss."
    "She's enjoying the way that I'm checking her out right now."
    show camila normal
    camila.say "Well - what do you think?"
    menu:
        "Compliment":
            "All thought of having the gun shoved in my face disappears in an instant."
            "And all I want to do is stare at Camila in that tight, shiny costume!"
            mike.say "It...it's amazing, Camila."
            mike.say "I'd have never guessed chrome looked so good on you!"
            $ camila.love += 1
            show camila flirt
            "Camila's cheeks flush at my obvious approval for her costume."
            "Not enough to be noticeable to most people and ruin her tough image."
            "But I know her well enough by now to be able to spot the signs."
            show camila normal
            camila.say "I don't know if I'd be comfortable wearing this on the job."
            camila.say "But it does make me feel kind of powerful."
            show camila flirt
            camila.say "And...well, pretty sexy too!"
            mike.say "How do you think it makes me feel, Camila?"
            mike.say "I'm worried I'll never be able to look at a household appliance the same way again!"
            "Camila snorts with laughter."
            camila.say "Forget those little tramps, [hero.name]."
            camila.say "They're not programmed to do the stuff I am!"
        "Criticize":
            "Camila looks hot as hell in that costume."
            "But I'm still pissed at having a gun shoved in my face."
            "So she's not going to be getting a compliment from me just yet!"
            mike.say "I think you shouldn't point guns at people, Camila!"
            mike.say "Don't they teach you stuff like that at cop school?"
            $ camila.love -= 1
            show camila bored
            "Again, I can't see Camila's eyes behind her visor."
            "Yet I can tell she's rolling them from the way she moves her head."
            camila.say "Forget cop school, [hero.name]."
            camila.say "Didn't they teach you anything at dating school?"
            camila.say "Like complimenting your date when she's tried real hard?"
            "Camila's words serve to dispel my irritation in an instant."
            "And now I'm starting to feel ashamed for being so prissy with her."
            mike.say "Okay, Camila - I'm sorry."
            mike.say "The costume's incredible."
            mike.say "And you look amazing."
            show camila normal
            "Camila curls her mouth as she walks past me into the house."
            camila.say "Hmm..."
            camila.say "That'll do...for a start."
    scene bg black with dissolve
    pause 1
    return

label camila_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    scottie.say "Whoa!"
    scottie.say "Robofficer makes a hot girl!"
    scottie.say "I'd love to put my memory stick in your USB socket, baby!"
    "At the mention of the cyborg cop, my head snaps around."
    show camila halloween annoyed at left
    show scottie halloween perv at right
    "And I'm rewarded with the sight of Scottie leaning over Camila."
    "He's leering at her, obviously turned on by her costume."
    "But she's looking up at him with a frown that I know all too well."
    "I have to make it over there before Camila does something Scottie will regret!"
    camila.say "Nah, you can keep your downloads, buddy."
    camila.say "I don't want to catch a computer virus!"
    scottie.say "Ow...ow, ow, ow!"
    scottie.say "Oh god...not there!"
    scottie.say "Please let me go!"
    "I can't see where Camila's hand just ended up."
    "But from the way Scottie's bent over double, it's not hard to guess!"
    menu:
        "Defend Camila":
            mike.say "You know she's a real cop, right, Scottie?"
            mike.say "She could whip out her badge and bust your ass!"
            show scottie sad
            show camila normal
            "Camila lets go of Scottie a moment later."
            "Perhaps thanks to the terrified look on his face."
            scottie.say "No..."
            scottie.say "I had no idea - I swear!"
            scottie.say "Please don't arrest me, Robofficer Lady!"
            hide scottie
            show camila at center
            "As Scottie hobbles away clutching his groin, Camila turns to face me."
            camila.say "I didn't actually bring my badge tonight."
            camila.say "And the gun came with the costume."
            "I make a point of looking a little disappointed at this."
            mike.say "But you did remember to bring your handcuffs, right?"
            mike.say "If not, I can maybe scare up a pair..."
            $ camila.love += 2
            show camila flirt
            "Camila grins and rewards me with a playful jab in the ribs."
            "After which I smile, trying to make out like it didn't hurt at all."
        "Defend Scottie":
            mike.say "Camila!"
            mike.say "What are you doing?!?"
            "Camila looks around to see me hurrying over."
            "She lets go of Scottie a moment later."
            "But it's more from surprise than any sense of guilt on her part."
            hide scottie
            show camila angry at center
            "As Scottie hobbles away clutching his groin, Camila turns to face me."
            camila.say "What am I doing?!?"
            camila.say "That guy was being a total creep."
            camila.say "He's lucky I didn't pull that thing off!"
            mike.say "Jesus, Camila - this is supposed to be a party!"
            mike.say "Can't you act like you're off duty for once?"
            $ camila.love -= 2
            "Camila shoots me an annoyed glance by way of answer."
            "And can almost feel the force of it like a slap to the face."
    scene bg black with dissolve
    pause 1
    return

label camila_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show camila halloween happy
    with dissolve
    "Camila takes hold of my hand as soon as a certain song starts to play."
    "As always, her grip is surprisingly strong."
    "And it's not immediately obvious why she's grabbed hold of me."
    camila.say "I love this one!"
    camila.say "Come on, [hero.name] - let's dance."
    "I take a step back and look Camila up and down."
    "Not for the first time I see how completely her costume covers her body."
    mike.say "Are you sure that's a good idea, Camila?"
    mike.say "I can hardly see you under all that stuff!"
    show camila flirt
    "Camila waves my concerns away with her free hand."
    camila.say "Don't worry about me."
    camila.say "Just worry about keeping up!"
    menu:
        "Agree":
            "Camila seems determined to dance, with or without me."
            "But if she does end up landing on her ass, she'll need help."
            "I should be there to lend a hand, no matter what."
            $ camila.love += 2
            mike.say "Sure, Camila."
            mike.say "Show me what you've got!"
            hide camila
            show dance camila halloween
            "I follow her onto the dance-floor."
            "Any moment I expect her to trip and fall."
            "Or at least to bump into something or someone."
            "But then my mouth drops open as I see Camila start to move."
            "The music has a techno beat, and she moves in time to it."
            "Her limbs seem stiff, yet still move logically."
            "She's doing that old-fashioned robot dancing!"
            "The kind you used to see back in the 1980's!"
            "Pretty soon everyone is watching Camila as she dances."
            "And then they're clapping, urging her on."
            "But I've got the best spot in the house."
            "Because I'm the one actually dancing with her!"
            "Camila's grin tells me she knew what I was thinking."
            "And all I can do is shake my head and smile too."
        "Refuse":
            "I guess I can't stop Camila if she wants to humiliate herself."
            "But if I sit this one out, then I can at least say I told her so."
            mike.say "No, Camila - I'm good."
            mike.say "But you go ahead and enjoy yourself."
            $ camila.love -= 2
            show camila annoyed
            "Camila looks more than a little disappointed."
            hide camila
            "But then she shakes her head and hurries away to dance."
            "I watch in silence, waiting for something to go wrong."
            "Any moment I expect her to trip and fall."
            "Or at least to bump into something or someone."
            "But then my mouth drops open as I see Camila start to move."
            "The music has a techno beat, and she moves in time to it."
            "Her limbs seem stiff, yet still move logically."
            "She's doing that old-fashioned robot dancing!"
            "The kind you used to see back in the 1980's!"
            "Pretty soon everyone is watching Camila as she dances."
            "And then they're clapping, urging her on."
            "But all I can do is watch from the side-lines."
            "The whole time feeling like I just missed out on something special."
    scene bg black with dissolve
    pause 1
    return

label camila_halloween_sex:
    scene bg bedroom1
    show camila halloween flirt
    with fade
    "Camila's been enjoying herself all night, playing the part of a law-enforcing cyborg."
    "She's even got the mannerisms of the original character down pretty well too."
    "But what really makes me smile is the fact that she's totally able to let her guard down."
    "Camila never seems to drop her tough cop demeanour most of the time."
    "And it can often feel like she's always on duty, even when she's not."
    "So seeing her get into goofing around for laughs like that is pretty amazing."
    "She even stays in character once we've managed to sneak away to my bedroom."
    camila.say "My sensors detect dirty laundry, soiled bedclothes..."
    camila.say "And the smell of sexual frustration!"
    mike.say "Hey, Camila!"
    mike.say "That's not the way to make small-talk."
    "Camila turns to face me, still moving like a robot."
    "She looks me up and down, her eyes hidden by her helmet."
    camila.say "I have been programmed to interpret human body-language."
    camila.say "And my databanks tell me that you are very horny right now."
    camila.say "Also that you wish to mate with me."
    "This should be the least sexy thing that I can imagine."
    "But Camila's already making me sweat."
    "And I'm getting pretty hard too!"
    mike.say "Ah..."
    mike.say "Aren't you basically owned by the police?"
    mike.say "I mean...I don't want to be arrested for soiling department property!"
    show camila close
    "Camila closes the distance between us in the blink of an eye."
    "I can't help yelping as I leap backwards and fall onto the bed."
    camila.say "Your attempts at humour are unsuccessful."
    camila.say "Cease them and remove your clothing at once!"
    camila.say "Copulation will commence in exactly one minute."
    hide camila
    show camila halloween flirt
    "I nod frantically, trying to remove my clothes at the same time."
    "And my efforts are hampered thanks to my eyes being on Camila the whole time."
    "She stands over me, unfastening her costume at strategic points."
    "Parts of it fall away, revealing that she's naked beneath it."
    "But she makes a point of keeping her helmet on while she does so."
    "Camila then crawls onto the bed, lowering herself onto all fours."
    show camila doggy with fade
    "She looks back over her shoulder at me."
    "And then she begins to issue more orders."
    camila.say "This unit is ready for physical interface."
    camila.say "Insert your cock into the appropriate hole."
    "I scurry over to where Camila's waiting for me."
    "My stiff cock swaying as I hurry to reach her."
    "I have no idea how she's managing to get me so hot."
    "She's showing all the sensuality of a refrigerator."
    "But I still want to fuck her more than anything in the world right now!"
    camila.say "You are cleared to begin copulation."
    "I waste no time on gripping Camila by the haunches."
    show camila doggy inside surprised
    "And then I push my cock between her thighs."
    "She tries to keep up the act as I push into her."
    "But she can't help moaning with pleasure as I fill her pussy."
    "It's already slick and soft, letting me know that she's as turned-on as me!"
    "Intrigued to see how long she can keep it up, I take hold of her wrists."
    "Pulling them backwards, I thrust into Camila at the same time."
    show camila doggy pleasure

    "The effect is both instant and dramatic."


    "Before too long, I'm almost riding her."
    "Camila sways back and forth as I pull and push her."
    "I can see that her tongue is hanging out of her mouth."
    "And I guess that her eyes are rolling upwards behind her visor."
    "Her exposed breasts are swinging in time with my motions."
    "The sound of my skin slapping against Camila's skin is almost as loud as her moans."
    "There's nothing slow or gentle about it, we're fucking as fast as we can."
    "The foreplay was all the flirting that we did earlier in the night."
    "And now all we can think about is going at it with everything we have."
    mike.say "Oh fuck..."
    mike.say "Camila..."
    mike.say "I'm gonna cum!"
    camila.say "Ah..."
    camila.say "Your...prime...directive..."
    camila.say "Is to...is to cum...cum in me!"
    show camila ahegao with hpunch
    "A moment later, I do exactly as I'm told."
    with hpunch
    "Camila bucks and twists, but I keep a firm hold of her."
    with hpunch
    "Every spurt that shoots out of me hits her like an electric shock."
    "But once I'm done cumming, she begins to relax again."
    "Camila's head droops forwards, her body going limp."
    "And I gently lower her down onto her stomach, my cock popping out in the process."
    "She makes no effort to move or even say a single word."
    "So I just assume that she needs some time to reboot her systems."
    "And I leave her to it."
    $ camila.sexperience += 1
    $ game.pass_time(1)
    return

label camila_dick_reactions:
    if not camila.flags.seendick:
        $ camila.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions camila smile
            camila.say "Whoa...hello there!"
            mike.say "You like what you see, Camila?"
            mike.say "Like, it's big enough for you?"
            camila.say "Let's just say it's like a roller-coaster, [hero.name]."
            show dick reactions camila tasty
            camila.say "I wanna stand in line to ride it!"
            $ camila.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions camila disgusted
            camila.say "Geez, [hero.name] - is that it?!?"
            mike.say "Wh...what do you mean, Camila?"
            mike.say "Is it too small?"
            camila.say "For a cigarette butt, no."
            camila.say "For a cock, yes!"
            $ camila.sub -= 10
        hide dick reactions
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
