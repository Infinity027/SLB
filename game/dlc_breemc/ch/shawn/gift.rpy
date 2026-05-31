init python:
    Item("spathiphyllum")

    Event(**{
    "name": "shawn_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(shawn,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "shawn",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

    Event(**{
    "name": "shawn_give_collar_female",
    "label": "shawn_give_collar_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            ),
        PersonTarget(shawn,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sexperience", 1),
            MaxStat("sub", -50),
            ),
        ],
    "girl": "shawn",
    "do_once": True,
    })

label shawn_give_female:








    if "spathiphyllum" not in hero.inventory:
        $ gift = "spathiphyllum"
        "He hands me a plant."
        bree.say "How did you know I like Peace Lily?"
        shawn.say "I dont. It's just that I used to carry one of them everywhere I go. Just though you might want to do the same."
        bree.say "Strange, but thanks anyway!"
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label shawn_give_birthday_female:
    shawn.say "Happy birthday, [hero.name]!"
    shawn.say "And here's your present too."
    bree.say "Thank you, Shawn!"
    bree.say "It's so thoughtful of you to remember the date."
    shawn.say "Not when it comes to you, [hero.name]."
    shawn.say "You're always the first thing I think of."
    call shawn_give_female from _call_shawn_give_female
    return

label shawn_give_christmas_female:
    shawn.say "Merry Christmas, [hero.name]!"
    shawn.say "Here's your present."
    shawn.say "I managed to get hold of it early too."
    bree.say "Oh, Shawn!"
    bree.say "This is the game I've been dying to play!"
    shawn.say "Yeah, well...everyone thinks my job's not up to much."
    shawn.say "But it does mean that I can get cool stuff for a cool girl!"
    call shawn_give_female from _call_shawn_give_female_1
    return

label shawn_give_valentine_female:
    shawn.say "Happy valentine's day, [hero.name]!"
    shawn.say "I got you a gift as well."
    bree.say "Oh, Shawn - you shouldn't have!"
    bree.say "I didn't know we were doing gifts."
    bree.say "Now I feel like I'm letting my side down!"
    shawn.say "Don't worry about it, [hero.name]."
    shawn.say "I just wanted to let you know how special you are."
    shawn.say "And how glad I am to have you as my valentine too."
    $ hero.gain_item("valentine_chocolates")
    return

label shawn_gift_collar_female:
    scene expression f"bg {game.room}"
    with fade
    "I feel like I've discovered a whole new side to Shawn since I started taking charge of our relationship."
    "At first I thought that he was just one of those geeky guys that would never stand up for himself, you know?"
    "But now I know that it goes much deeper, that Shawn really craves being put in his place on an unconscious level."
    "And I'm becoming ever more comfortable with playing up to that, to making sure that I gently dominate him."
    "So much so that I feel like there should be a way for people to know how our relationship will work from now on."
    "A kind of visual symbol of Shawn's place beneath me, as well as my dominance over him."
    "And I think I know just the thing to neatly do both at once."
    "So the next time that Shawn and I meet up, I have it ready to present to him."
    show shawn nice with fade
    shawn.say "Hi, [hero.name]..."
    shawn.say "Hey..."
    shawn.say "What's that you have there?"
    show shawn smile
    "I do the best I can to play innocent."
    "Because I kind of enjoy teasing Shawn a little."
    bree.say "Hey, Shawn..."
    bree.say "I have no idea what you could be talking about!"
    show shawn nice
    shawn.say "Oh come on..."
    shawn.say "I know you have something for me, [hero.name]..."
    shawn.say "I can see that you've even had it gift-wrapped!"
    show shawn smile
    "I make a show of pretending to admit defeat."
    bree.say "Okay, Shawn..."
    bree.say "You got me!"
    "I smile as I hold out the box."
    "And I keep it up as Shawn eagerly takes it from me."
    "Because if I've read the situation right, he'll soon be smiling too."
    play sound [paper_ripping_2, paper_ripping_1]
    "So I watch with baited breath as he tears off the wrapping paper and reaches inside."

    if shawn.sub >=90:
        "Shawn holds up the collar like it's made of pure gold."
        "His eyes going wide as he sees that his name is engraved on the medallion."
        shawn.say "[hero.name]..."
        shawn.say "How did you know?"
        "He's already struggling to put the thing on as he says all of this."
        "Shaking his head as he does so."
        bree.say "I've always wanted one of these..."
        bree.say "But I never thought I'd have the courage to ask for it!"
        "I can't help smiling as I hurry to help Shawn fix the collar in place."
        "And as soon as it's fastened around his neck, I step back to admire my work."
        bree.say "So..."
        bree.say "You like it?"
        show shawn happy
        "Shawn nods eagerly, adjusting the collar around his neck."
        "And I can see that he has a huge smile on his face too."
        show shawn nice
        shawn.say "I love it, [hero.name]!"
        shawn.say "You taking charge of things recently..."
        shawn.say "It's just felt so right, you know?"
        shawn.say "I'm much happier with you taking the lead."
        shawn.say "And this makes it official, right?"
        show shawn smile
        "I nod."
        bree.say "You don't have to start calling me 'Mistress' just yet."
        bree.say "But the collar is kind of the first step."
        show shawn nice
        shawn.say "Okay, [hero.name]..."
        shawn.say "One step at a time, I guess."
        show shawn smile
        "But there's part of me that doesn't think it'll take too long."
        "Because Shawn looks happier and more contented than he has in good while."
        "And I think this is something that he's really going to enjoy."
        $ hero.morality -= 1
        $ shawn.set_sex_slave()
    else:

        show shawn stuned
        "Shawn holds up the collar to examine it."
        "And I can already see the look of confusion on his face."
        show shawn surprised
        shawn.say "Erm..."
        shawn.say "What's this supposed to mean, [hero.name]?"
        shawn.say "Are we getting a puppy or something?"
        show shawn stuned
        "I can already feel myself starting to blush as Shawn misses the point."
        "So I take the collar from him and hold up the medallion for him to see."
        bree.say "No, we are not getting a puppy!"
        bree.say "Would I want to call the dog 'Shawn' if we did?"
        "Shawn shakes his head at this."
        show shawn complain
        shawn.say "Of course not, [hero.name]..."
        shawn.say "That'd be really confusing!"
        show shawn upset
        "I keep on looking hard at Shawn as he says all of this."
        "Almost like I'm willing his brain to start turning over."
        show shawn stuned
        "And eventually I see recognition in his eyes."
        show shawn surprised
        shawn.say "Wait..."
        shawn.say "This is for me?!?"
        show shawn stuned
        bree.say "Yes, Shawn..."
        bree.say "You've been so happy with me taking charge recently."
        bree.say "So I thought that we could make the arrangement official."
        bree.say "You don't have to start calling me 'Mistress' just yet."
        bree.say "But the collar is kind of the first step."
        show shawn upset
        "Shawn surprises me by thrusting the collar back into my hands."
        "And when I look up, I can see that he's shaking his head."
        show shawn vangry
        shawn.say "[hero.name], I might have liked you taking charge of things."
        shawn.say "But that doesn't mean I want to be used as a bloody doormat."
        shawn.say "And I certainly don't want to be treated like a dog either!"
        show shawn upset
        "I find myself blinking and shaking my head in confusion."
        bree.say "But, but, but..."
        bree.say "I thought you were into being dominated?!?"
        show shawn vangry
        shawn.say "Well you thought wrong!"
        shawn.say "And you've given me a lot to think about too, [hero.name]."
        hide shawn with easeoutright
        $ shawn.love -= 10
        "With that, Shawn turns on his heel and begins to walk away."
        "I think about calling after him, but then decide against it."
        "Probably the best thing I can do right now is give him some space."
        "That and hope I haven't done irreparable damage to our relationship."
        $ hero.cancel_activity()
    scene bg black with dissolve
    return

label shawn_give_collar_female:
    scene expression f"bg {game.room}"
    with fade
    "When Shawn calls me up and says that he has a surprise for me, I'm more than eager to see what it is."
    "And so I hurry along to the place where we've agreed to meet feeling pretty excited by the whole thing."
    "Not least because I've noticed the beginning of a subtle change in Shawn recently."
    "When we first met, he was really lacking in confidence around me, very unsure of himself."
    "I just took that as part and parcel of Shawn being a bit of a nerd, and not confident around women."
    "But recently he seems to have begun to grown in confidence and become more forward around me."
    "I mean, it's not like he's turned into an alpha-male type of guy overnight."
    "But he has started speaking his mind more and making suggestions when we're together."
    "Whereas in the past he would have always left the decisions up to me."
    "So you can understand why I'm intrigued to see what he's got in store for me."
    "As soon as I see Shawn, I wave and call to him."
    bree.say "Hi, Shawn!"
    bree.say "I got here as soon as I could."
    show shawn smile at center, zoomAt(1.25, (640, 900)) with fade
    "Shawn turns to face me, a smile on his face as he waves a greeting."
    "Which is the first thing that tells me he's gained even more confidence."
    "Because in the past he would have been the one coming running to me."
    "I mean, it's not that Shawn looks disinterested in me right now."
    "Just that he's not gushing over me like he would have at one time."
    show shawn nice
    shawn.say "Hi, [hero.name]..."
    shawn.say "I'm so glad you could make it."
    hide shawn
    show shawn kiss
    with fade
    "Shawn leans in and plants a kiss on my lips."
    "It's not without affection, but it's not desperately passionate either."
    bree.say "Erm..."
    hide shawn
    show shawn smile
    with fade
    bree.say "Y...yeah..."
    bree.say "I had to drop everything and come running..."
    bree.say "So apologies if I look a little harassed!"
    show shawn happy
    "Shawn smiles and shakes his head."
    show shawn nice
    shawn.say "Don't be silly, [hero.name]..."
    shawn.say "You look as beautiful as always."
    shawn.say "But I do have something here that might add to your look!"
    show shawn smile
    "I can't help clasping my hands to my chest as Shawn produces a package."
    "It's wrapped in the prettiest paper and has a big bow on it too."
    "Sure, it looks a little too big to be a ring - but that would be getting ahead of myself."
    "And it's rude to look a gift horse in the mouth, so I smile and begin to play my part."
    bree.say "Oh, Shawn..."
    bree.say "Is that for me?"
    bree.say "You really shouldn't have!"
    shawn.say "Don't say that until you've opened it, [hero.name]!"
    "I nod in agreement as I take the package from Shawn."
    play sound [paper_ripping_2, paper_ripping_1]
    "But then all of my attention is focussed on tearing off the paper."
    "Then I open the box and pull out..."
    bree.say "A dog collar?!?"
    "I look from the collar in my hand to Shawn."
    bree.say "Did you mix my gift up with one for a four-legged friend of yours?"
    show shawn talkative
    shawn.say "Oh no, [hero.name]..."
    shawn.say "That's for you."
    shawn.say "You've been so obedient recently, doing whatever you're told."
    shawn.say "So I thought that you'd appreciate something to reflect that."
    show shawn nice
    shawn.say "You can even call me 'Master', if you like?"
    show shawn smile
    menu:
        "Accept the collar":
            "Without thinking, I undo the collar and begin to put it around my neck."
            show shawn stuned
            "Shawn seems surprised by this at first, but then hurries to help."
            show shawn talkative
            shawn.say "Does this..."
            shawn.say "Does this mean you like it, [hero.name]?"
            show shawn sadsmile
            "Now that the collar is fastened around my neck, I look up."
            "And again, without needing to think, I find myself nodding."
            bree.say "It's so weird, Shawn..."
            bree.say "The moment I saw the collar, I knew it was for me."
            bree.say "And somehow I knew that it was right too!"
            show shawn happy
            "I can see that Shawn looks totally relieved at my answer."
            "Even though he's doing the best he can to seem totally in charge of the situation."
            show shawn nice
            shawn.say "Well, [hero.name]..."
            shawn.say "I just felt that was the way things had been going recently."
            shawn.say "What with me asserting my masculinity and you seeming to like it."
            shawn.say "I was worried this might seem a bit too much, you know?"
            show shawn smile
            "I shake my head, still fingering the collar as I do so."
            bree.say "Oh no, Shawn..."
            bree.say "This is perfect."
            bree.say "It tells everyone that I'm yours."
            bree.say "And it reminds me of that too!"
            show shawn happy
            "Shawn smiles, almost like he can't believe his luck."
            "Because everything seems to be turning out how he wanted."
            show shawn nice
            shawn.say "So..."
            shawn.say "About the idea of you calling me 'Master'?"
            show shawn smile
            bree.say "What about it..."
            bree.say "Oh Master of mine?"
            $ hero.morality -= 1
            $ hero.flags.collared = True
        "Do not accept the collar":
            show shawn stuned with vpunch
            "Without thinking, I toss the whole lot back in Shawn's face."
            "And by that I mean I throw the collar and box at him."
            "Then I let him know exactly what I think of his gift too."
            bree.say "Have you gone crazy, Shawn?"
            bree.say "Okay, I noticed that you were getting more confident around me."
            bree.say "But that doesn't mean I want to be treated like a damn dog!"
            bree.say "What was next on the agenda?"
            bree.say "Making me eat off the damn floor?!?"
            $ hero.morality += 1
            $ shawn.sub -= 10
            "All of the confidence Shawn's gained seems to suddenly desert him."
            "Because he's almost cowering away from me as I verbally eviscerate him."
            show shawn surprised
            shawn.say "P...please, [hero.name]..."
            shawn.say "It's not like that, honestly..."
            shawn.say "I must have misread the situation, that's all!"
            show shawn sadsmile
            "I can see that Shawn's doing the best he can to apologise."
            "And he does look like he's genuinely sorry for the misunderstanding."
            "But the problem is that I'm way too angry to be able to calm down right now."
            bree.say "That's putting it fucking mildly, Shawn!"
            bree.say "I'd say you totally put your foot in it."
            bree.say "Maybe even torpedoed this whole damn relationship!"
            show shawn sad
            "The mere sight of Shawn's face is making me so mad."
            "I know that I have to get away from him if I want to calm down."
            hide shawn with fade
            "So with that in mind, I turn on my heel and begin to walk away."
            "Luckily for the both of us, Shawn doesn't try to follow me or plead his case."
            "Once I've blown off enough steam, it probably won't seem so bad."
            "But until then I need to put some distance between us."
            "Or else he might find himself having to remove that damn collar from a very intimate orifice."
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
