label postfight_female:
    scene bg black
    $ renpy.show(f"bg {game.room}")
    $ renpy.show(f"{cheated_girl.id} angry", at_list=[left4])
    $ renpy.show(f"{active_girl.id} angry", at_list=[left4])
    with fade
    "Once the dust has settled, it's clear to see who's come out on top."
    "One of them's laid in a heap on the ground, wondering what the hell just happened."
    "And the other is standing over them, looking pretty pleased with themselves too."
    "I'm still feeling more than a little shaken up from watching an actual fight."
    "And one that was over me too!"
    "But I know that I have to do something in response."
    "So what is it going to be?"
    menu:
        "Throw yourself at the winner":
            "Ah, who am I trying to kid?!?"
            "Someone just beat the hell out of another person to impress me."
            "I hurry over to the victor and leap into their arms."
            bree.say "Oh, wow!"
            bree.say "I had no idea you were so big and strong!"
            if cheated_girl.id == "ryan":
                $ ryan.sub += 2
                ryan.say "You only just noticed that, [hero.name]?"
            elif cheated_girl.id == "jack":
                $ jack.sub += 2
                jack.say "I'd fight whole armies for you, [hero.name]!"
            elif cheated_girl.id == "shawn":
                $ shawn.sub += 2
                shawn.say "You make me into a wild animal, [hero.name]!"
            elif cheated_girl.id == "mike":
                $ mike.sub += 2
                mike.say "You're worth fighting for, [hero.name]!"
            elif cheated_girl.id == "danny":
                $ danny.sub += 2
                danny.say "That's because I'm a REAL man, baby!"
            elif cheated_girl.id == "dwayne":
                $ dwayne.sub += 2
                dwayne.say "I have brains AND brawn, [hero.name] - it's a lethal combination!"
            elif cheated_girl.id == "victor":
                $ victor.sub += 2
                victor.say "I don't know what came over me, [hero.name] - I'm normally very chill!"
            elif cheated_girl.id == "master":
                $ master.sub += 2
                master.say "What master would fail to fight for his favourite pupil?"
            "Just then the defeated suitor chooses to groan and roll over on the ground."
            "Still in the arms of the victor, I look down at them and shake my head."
            bree.say "Geez..."
            bree.say "What did I ever see in a loser like you?"
            if active_girl.id == "ryan":
                $ ryan.love -= 4
                ryan.say "Hey, be nice to me - I just got my ass kicked!"
            elif active_girl.id == "jack":
                $ jack.love -= 4
                jack.say "Urgh...my head feels like there's a PC-gamer living in it!"
            elif active_girl.id == "shawn":
                $ shawn.love -= 4
                shawn.say "Ouch...how am I supposed to stack shelves like this?"
            elif active_girl.id == "mike":
                $ mike.love -= 4
                mike.say "Oooh...we live in the same house - this is so awkward!"
            elif active_girl.id == "danny":
                $ danny.love -= 4
                danny.say "What happened - I thought I was the bad guy?!?"
            elif active_girl.id == "dwayne":
                $ dwayne.love -= 4
                dwayne.say "So this is what having your candy-ass kicked feels like!"
            elif active_girl.id == "victor":
                $ victor.love -= 4
                victor.say "This wasn't supposed to happen to an ice-cold cleaner!"
            elif active_girl.id == "master":
                $ master.love -= 4
                master.say "My...my skills are failing me!"
            "I roll my eyes at the excuses of a loser."
            "And at the same time, I pull the winner even closer."
            $ hero.morality -= 4
        "Rush to check on the loser":
            "Suddenly the reality of the situation hits me."
            "A person just got beaten up pretty badly."
            "And it's all because of me - this is my fault!"
            "I hurry over to where the loser is laid."
            "And I do all I can to help them."
            bree.say "Oh no!"
            bree.say "Are you okay?"
            bree.say "Should I call an ambulance?"
            if active_girl.id == "ryan":
                $ ryan.love += 4
                ryan.say "I...I think I'll live!"
            elif active_girl.id == "jack":
                $ jack.love += 4
                jack.say "I'm okay - I think my defensive layer of blubber helped!"
            elif active_girl.id == "shawn":
                $ shawn.love += 4
                shawn.say "I'll live - but Amy's going to be doing the heavy lifting for a while!"
            elif active_girl.id == "mike":
                $ mike.love += 4
                mike.say "Ouch...I feel like I've been tenderised!"
            elif active_girl.id == "danny":
                $ danny.love += 4
                danny.say "What in the hell happened - I'm supposed to be the bad guy around here!"
            elif active_girl.id == "dwayne":
                $ dwayne.love += 4
                dwayne.say "How...how did that jabroni beat me?!?"
            elif active_girl.id == "victor":
                $ victor.love += 4
                victor.say "Oh, [hero.name] - is my dog okay?"
            elif active_girl.id == "master":
                $ master.love += 4
                master.say "I must enter a healing trance, to restore my body!"
            "As I try to tend to the fallen, I hear a snort behind me."
            "And looking back over my shoulder, I see the supposed winner frowning."
            if cheated_girl.id == "ryan":
                $ ryan.sub -= 2
                ryan.say "What about me?"
                ryan.say "I just beat their ass!"
            elif cheated_girl.id == "jack":
                $ jack.sub -= 2
                jack.say "Erm...what's going on here, [hero.name]?"
                jack.say "I thought I actually won the fight?"
            elif cheated_girl.id == "shawn":
                $ shawn.sub -= 2
                shawn.say "Why are you fussing over them?"
                shawn.say "I'm the one that kicked ass here!"
            elif cheated_girl.id == "mike":
                $ mike.sub -= 2
                mike.say "[hero.name], what's going on here?"
                mike.say "I just literally fought for you!"
            elif cheated_girl.id == "danny":
                $ danny.sub -= 2
                danny.say "What you messing around with that loser for?"
                danny.say "I'm the one that won the fight, baby!"
            elif cheated_girl.id == "dwayne":
                $ dwayne.sub -= 2
                dwayne.say "You seem to have misunderstood the situation, [hero.name]."
                dwayne.say "The winner is this guy here - your's truly!"
            elif cheated_girl.id == "victor":
                $ victor.sub -= 2
                victor.say "Erm...[hero.name]?"
                victor.say "I did win the fight, didn't I?"
            elif cheated_girl.id == "master":
                $ master.sub -= 2
                master.say "Shouldn't you be congratulating me, my dear?"
                master.say "Complementing me on the strength of my discipline?"
            "I turn my back on them with a harumph."
            bree.say "Humph..."
            bree.say "I'm not into thugs and bullies!"
            bree.say "Now leave me alone, or else I'll call the police."
            bree.say "And they can arrest you for assault - and being a massive jerk!"
            $ hero.morality += 2
        "Storm off":
            "What's wrong with these people?"
            "We're living in the twenty-first century."
            "And they're still fighting live savages!"
            "I look from the one of them still standing to the one on the ground."
            "And I shake my head in angry disapproval."
            bree.say "What are you guys?"
            bree.say "Cavemen or something?!?"
            bree.say "Solving problems with your fists!"
            bree.say "One of you could have been seriously hurt!"
            "The supposed winner looks at me with a puzzled expression."
            if cheated_girl.id == "ryan":
                $ ryan.sub -= 1
                ryan.say "What about me?"
                ryan.say "I just beat their ass!"
            elif cheated_girl.id == "jack":
                $ jack.sub -= 1
                jack.say "Erm...what's going on here, [hero.name]?"
                jack.say "I thought I actually won the fight?"
            elif cheated_girl.id == "shawn":
                $ shawn.sub -= 1
                shawn.say "Why are you fussing over them?"
                shawn.say "I'm the one that kicked ass here!"
            elif cheated_girl.id == "mike":
                $ mike.sub -= 1
                mike.say "[hero.name], what's going on here?"
                mike.say "I just literally fought for you!"
            elif cheated_girl.id == "danny":
                $ danny.sub -= 1
                danny.say "What you messing around with that loser for?"
                danny.say "I'm the one that won the fight, baby!"
            elif cheated_girl.id == "dwayne":
                $ dwayne.sub -= 1
                dwayne.say "You seem to have misunderstood the situation, [hero.name]."
                dwayne.say "The winner is this guy here - your's truly!"
            elif cheated_girl.id == "victor":
                $ victor.sub -= 1
                victor.say "Erm...[hero.name]?"
                victor.say "I did win the fight, didn't I?"
            elif cheated_girl.id == "master":
                $ master.sub -= 1
                master.say "Shouldn't you be congratulating me, my dear?"
                master.say "Complementing me on the strength of my discipline?"
            "I shake my head, unable to believe what I'm hearing."
            "Then the apparent loser of their little tussle speaks up too."
            if active_girl.id == "ryan":
                $ ryan.love -= 2
                ryan.say "Hey, be nice to me - I just got my ass kicked!"
            elif active_girl.id == "jack":
                $ jack.love -= 2
                jack.say "Urgh...my head feels like there's a PC-gamer living in it!"
            elif active_girl.id == "shawn":
                $ shawn.love -= 2
                shawn.say "Ouch...how am I supposed to stack shelves like this?"
            elif active_girl.id == "mike":
                $ mike.love -= 2
                mike.say "Oooh...we live in the same house - this is so awkward!"
            elif active_girl.id == "danny":
                $ danny.love -= 2
                danny.say "What happened - I thought I was the bad guy?!?"
            elif active_girl.id == "dwayne":
                $ dwayne.love -= 2
                dwayne.say "So this is what having your candy-ass kicked feels like!"
            elif active_girl.id == "victor":
                $ victor.love -= 2
                victor.say "This wasn't supposed to happen to an ice-cold cleaner!"
            elif active_girl.id == "master":
                $ master.love -= 2
                master.say "My...my skills are failing me!"
            "Urgh..."
            "They're both so pathetic!"
            "It makes me so mad!"
            bree.say "You're both as bad as each other."
            bree.say "And I don't want to see either of you again."
            bree.say "Not until you've learnt to behave like civilised human beings!"
            "I can hear them both protesting as I turn my back on them."
            "But I make an effort not to hear what they're saying."
            "And instead I stride away, leaving them behind me."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
