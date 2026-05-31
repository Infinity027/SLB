label samantha_desire_0_male:
    $ result = randint(1, 5)
    if result == 1 and "samantha_event_B01" not in DONE:
        mike.say "So, do you think you'll ever get married?"
        samantha.say "Well, maybe eventually some fall day, possibly in a big park."
        samantha.say "Simple ceremony."
        samantha.say "We'll write our own vows."
        samantha.say "Band, no DJ."
        samantha.say "People will dance..."
        if (samantha.flags.engaged or "samantha_event_02" not in DONE) and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "I'm not gonna worry about it, but I am not sure Ryan will be up to it."
            mike.say "That's something you should discuss with him."
        elif samantha.is_girlfriend:
            mike.say "Let's hope I'll stand beside you."
        else:
            samantha.say "Nothing hotter than a girl planning out her own imaginary wedding, huh?"
            mike.say "Actually, I think it's cute."
    elif result == 2:
        samantha.say "I totally wanted to come."
        mike.say "Maybe I could help you with that."
        if (samantha.flags.engaged or "samantha_event_02" not in DONE) and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "LOL!"
        else:
            samantha.say "Anytime you want."
            $ samantha.sub += 1
            $ samantha.love += 1
    elif result == 3:
        $ renpy.dynamic("clothes", "colour1", "colour2")
        $ clothes = randchoice(["trouser", "shirt", "cap", "vest"])
        $ colour1 = randchoice(["blue", "red", "yellow"]).capitalize()
        $ colour2 = randchoice(["green", "orange", "pink"])
        samantha.say "Nice [clothes]."
        mike.say "Right? Right?"
        mike.say "Look at those colours."
        mike.say "[colour1] and [colour2], together at last."
        samantha.say "Is it new?"
        mike.say "That's the crazy part."
        mike.say "I've had this [clothes] for like six years."
        mike.say "Until this morning, I wasn't into it at all, but now, it's like my tastes have changed."
        $ samantha.love += 1
    elif result == 4:
        if samantha.is_girlfriend:
            mike.say "You know, I am glad we found each other."
        else:
            mike.say "Maybe it's time to start forming some second impressions."
            samantha.say "You're finally gonna watch Big Trouble in Little China again?"
            mike.say "Not Goonies-- girls."
            mike.say "What if there's someone from my past who I thought was wrong for me at the time, when in fact she is actually a perfect fit?"
            samantha.say "Hold up."
            samantha.say "You know, this isn't a bad idea."
            samantha.say "Let's think [hero.name]'s greatest hits."
            samantha.say "What about Chelsea?"
            "I had so many fond memories of her: The scented oils on her dresser..."
            "The teddy bear collection on her bed..."
            "That one Aladdin song she always listened to..."
            "Her smile..."
            mike.say "Man, I haven't seen her in, like, maybe four years."
            samantha.say "Well, why'd you guys break up?"
            mike.say "I just wasn't looking for a big commitment at the time."
            mike.say "Maybe I should call her."
            mike.say "Wonder if she even remembers me."
        $ samantha.love += 1
    else:
        if randint(1, 2) == 1:
            if (samantha.flags.engaged or "samantha_event_02" not in DONE) and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                samantha.say "Ryan and I went to the pool the other day."
                $ what = randchoice([
                    "He spent the whole time looking at other girls.",
                    "He is so sexy in a swimsuit.",
                    "Don't tell anyone but I blew him in the lockers.",
                    "He made me come with his fingers in the water."
                    ])
                samantha.say "[what]"
                mike.say "Poor you..."
            elif samantha.is_girlfriend:
                samantha.say "I don't know why I am dating you."
            else:
                samantha.say "Even if he cheated on me, I kind of miss my time with Ryan."
                mike.say "Don't worry, there are plenty of snakes in the wood."
                samantha.say "Isn't the expression about fishes?"
                mike.say "Yes, but we both know what you really need is a big snake."
                samantha.say "LOL!"
        else:
            if (samantha.flags.engaged or "samantha_event_02" not in DONE) and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                samantha.say "I hope you'll manage to find someone soon."
            elif samantha.is_girlfriend:
                samantha.say "I am glad we found each other."
            else:
                samantha.say "I hope we'll manage to find someone soon, we are damaged goods you know."
    $ samantha.love += 1
    return

label samantha_desire_1_male:
    $ result = randint(1, 5)
    if result == 1:
        if game.room == "nightclub":
            samantha.say "These clubs are supposed to be fun, right?"
            samantha.say "Why do I hate them so much?"
            mike.say "Because all of the stuff you're supposed to like usually sucks."
            samantha.say "Like these clubs or cruises."
            mike.say "Or New Year's Eve."
            samantha.say "Or the Super Bowl."
            mike.say "Or parades."
            samantha.say "The Rockettes."
            mike.say "Or parades."
            samantha.say "You said that already."
            mike.say "I really hate parades."
            samantha.say "Okay."
        else:
            samantha.say "You know I hate Sundays..."
            mike.say "Why?"
            samantha.say "It's like the whole world is dead."
            mike.say "But on Monday it's resurrection day!"
    elif result == 2:
        samantha.say "You know, I found sleeping deeply relaxing."
        mike.say "Yeah?"
        samantha.say "And interesting too."
        samantha.say "I find out a lot about myself by sleeping."
        samantha.say "Dreams, they are who I am when I'm too tired to be me."
        mike.say "You may be tired of yourself, but I never get to that point."
        mike.say "You are way too much fun."
    elif result == 3:
        if samantha.flags.nickname == "cupcake":
            mike.say "I tell you, Cupcake you should try new things..."
        else:
            mike.say "I tell you, Samantha you should try new things..."
        samantha.say "I don't know..."
        samantha.say "I heard that if you're too open-minded; your brains will fall out."
        mike.say "Very funny..."
    elif result == 4:
        mike.say "The female mind is certainly a devious one."
        samantha.say "Well, of course it is. It has to deal with the male one."
    else:
        if (samantha.flags.engaged or "samantha_event_02" not in DONE) and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "Ryan and I went to the park yesterday."
            $ what = randchoice([
                "I can't believe he hit on that girl while I was here.",
                "I couldn't stop looking at his ass.",
                "We fucked behind a tree.",
                "He ate my pussy behind a bush."
                ])
            samantha.say "[what]"
            mike.say "Poor you..."
        elif samantha.is_girlfriend:
            samantha.say "You should try harder to be sexy, make me feel desired."
        else:
            samantha.say "Ryan was really an ass."
            mike.say "Yes but you were the best half of it."
            samantha.say "What?"
            mike.say "Your ass was the best part of your couple's butt."
            samantha.say "LOL!"
    $ samantha.love += 1
    return

label samantha_desire_2_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "Last night I was seriously considering whether I was a bisexual or not, but I don't think so."
        samantha.say "Though I'm not sure if I'd like to be and..."
        mike.say "I don't think there's anything wrong with that, if you like a person, you like the person, not their genitals."
        mike.say "But if you are, I definitely want to be a part of it."
    elif result == 2:
        mike.say "If I had a dollar for every time a random woman walked up to me and tried to seduce me, I'd have 50 cents."
        mike.say "That's assuming drag queens are half price."
        samantha.say "I am pretty sure you are exaggerating."
    elif result == 3:
        samantha.say "The most enjoyable book in the world is the phone book."
        samantha.say "Because think of all the sex that went into creating the content."
    elif result == 4:
        mike.say "Yesterday I saved a baby, a boy, a man, and an old man from death, and all by simply not impregnating anybody."
        mike.say "But I don't consider myself a hero."
        mike.say "Merely heroic, and also unable to reach any of my lady friends on the phone."
    else:
        "Samantha is looking at me, biting her lips."
        if randint(1, 2) == 1:
            if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                samantha.say "Ryan told me that you were in love with me when we lived together."
                mike.say "That traitor..."
                mike.say "It was more a crush than anything else."
                mike.say "And I am totally over it."
                samantha.say "Oh, really?"
                $ samantha.love += 1
            elif samantha.is_girlfriend:
                samantha.say "You are pretty good looking you know..."
                mike.say "Thanks, you are a fine piece of ass yourself."
                $ samantha.love += 1
            else:
                samantha.say "Are you really over it?"
                mike.say "Over what?"
                samantha.say "Me."
                $ result = renpy.display_menu([("Yes",1), ("No",2), ("Not sure",3)])
                if result == 1:
                    mike.say "Yes completely."
                    samantha.say "Too bad..."
                    $ samantha.love -= 1
                elif result == 2:
                    mike.say "Not really."
                    samantha.say "Good to know."
                    $ samantha.love += 1
                else:
                    mike.say "I am no sure."
                    samantha.say "Tell me when you are."
                    $ samantha.love += 1
        else:
            samantha.say "Maybe I made a mistake last year..."
            mike.say "What do you mean?"
            samantha.say "Nothing."
    $ samantha.love += 1
    return

label samantha_desire_3_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "I'm a Pisces, and people say that Pisces make the best lovers."
        samantha.say "That's because Pisces are fish, and it's like my grandpa always used to say:"
        samantha.say "'The next best thing to making love to a mermaid, is having sex with a fish.'"
        $ samantha.love += 1
    elif result == 2:
        samantha.say "I could really suck a dick right now.."
        mike.say "Ergh?"
        samantha.say "Did I say that out loud?"
        $ samantha.love += 1
    elif result == 3:
        if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
            samantha.say "Ryan is always looking at other girls 's asses..."
            samantha.say "Is my ass that bad?"
        else:
            "Samantha looks fidgety, she is doing weird motions."
            mike.say "What are you doing?"
            samantha.say "Exercises to tighten my pussy..."
    elif result == 4:
        mike.say "My throat is sore..."
        mike.say "I tried to eat a banana in one go earlier, I couldn't but I learnt something valuable: Girls that can deep throat are fucking under appreciated!"
        samantha.say "Thanks for the compliment."
    else:
        samantha.say "I am thinking of changing my look."
        if randint(1, 2) == 1:
            samantha.say "What do you think I should try."
            $ result = renpy.display_menu([("Changing your hair color", 2), ("Getting pierced", 3), ("Getting tattoos", 4), ("Getting cum on your face", 1)])
            if result == 1:
                mike.say "I think you would look great with my cum all over your lips."
                if samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                    samantha.say "Oh, really..."
                    if samantha.love >= 100:
                        if "samantha_event_B01" in DONE:
                            samantha.say "I am a married woman, you know... To your friend."
                        else:
                            samantha.say "I have a boyfriend, you know... Your friend."
                        mike.say "A blowjob from you is worth a thousand friends."
                        $ samantha.love += 1
                    else:
                        samantha.say "Better not tell Ryan about that comment."
                        $ samantha.love -= 1
                    $ samantha.love += 1
                elif not samantha.is_girlfriend and samantha.love >= 120:
                    samantha.say "I should try it sometime."
                    mike.say "Just send me a text when you are ready."
                    samantha.say "Ok."
                    $ samantha.love += 1
                else:
                    samantha.say "Next time we are alone, we must do that then."
                    mike.say "Let's get to my room."
                    samantha.say "LOL!"
                    $ samantha.love += 1
            elif result == 2:
                mike.say "Maybe you could try to dye your hair red..."
                samantha.say "Like my friend Jessica?"
                if not Person.is_not_hidden("jessica"):
                    mike.say "I don't know her."
                    samantha.say "She's a nice girl, she works at the flower shop, in the mall."
                samantha.say "Anyway, I think I look best as a blond."
                mike.say "And like this nobody can be fooled into thinking that you have a brain."
                samantha.say "Ha, Ha , Ha... Jerk."
                $ samantha.love += (randint(0, 2) - 1)
            elif result == 3:
                mike.say "Maybe you could try to get a piercing."
                samantha.say "I don't know..."
                if samantha.love >= 80:
                    samantha.say "I already got my navel pierced..."
                    mike.say "I know, and that's damn sexy if you ask me."
                    $ samantha.love += 1
                    if samantha.love >= 100:
                        "Samantha's cheek get a little red."
                        samantha.say "...And both my nipples..."
                        "I swallow slowly..."
                        $ samantha.love += 1
                        if samantha.love >= 120:
                            "Samantha's breath get faster."
                            samantha.say "...And my clit too."
                            "I can feel my pants tightening."
                            $ samantha.love += 1
                    samantha.say "So, I am not sure anymore would be good."
                    samantha.say "It might get too much."
                    "She looks delighted by the effect she had on me."
                $ samantha.love += 1
        else:
            samantha.say "Maybe I'll shave my head."
            if "samantha_event_B01" in DONE and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                mike.say "No, you'd better lose a husband, you would look great without one."
            elif samantha.flags.engaged and not (samantha.flags.cuck_ryan or samantha.flags.knows_ryancheats):
                mike.say "No, you'd better lose a boyfriend, you would look great without one."
            else:
                mike.say "Yeah, and I'll wear makeup."
            samantha.say "Stop kidding..."
    return

label samantha_desire_4_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "I lost a little weight over the weekend."
        samantha.say "I cut my fingernails."
    elif result == 2:
        samantha.say "A guy and a girl can be just friends, but at one point or another, they will fall for each other..."
        samantha.say "Maybe temporarily, maybe at the wrong time, maybe too late, or maybe forever."
    elif result == 3:
        samantha.say "Man may have discovered fire, but women discovered how to play with it."
    elif result == 4:
        samantha.say "Well, it seems to me that the best relationships - the ones that last - are frequently the ones that are rooted in friendship."
        samantha.say "You know, one day you look at the person and you see something more than you did the night before."
        samantha.say "Like a switch has been flicked somewhere. And the person who was just a friend is..."
        samantha.say "Suddenly the only person you can ever imagine yourself with."
    elif result == 5:
        samantha.say "I would give anything if you were two people, so I could call up the one who is my friend and tell her about the one I like so much."
    $ samantha.love += 1
    return

label samantha_desire_5_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "I suffer from girlnextdooritis where the guy you love is friends with you and that's it."
    elif result == 2:
        samantha.say "Try not to think about me sucking you."
    elif result == 3:
        samantha.say "I had a naughty dream last night and guess who was in it?"
        samantha.say "I'll give you a hint. I'm talking to him right now."
    elif result == 4:
        samantha.say "Have you ever had a wet dream with me in it? Be honest..."
    else:
        samantha.say "If you could do anything you want to me, what would you do?"
    $ samantha.love += 1
    return

label samantha_love_0_male:
    $ result = randint(1, 6)
    if game.flags.gaymistake == 1:
        "I'd like to say that I'm mature and comfortable enough in my skin that Audrey's words slide right off of me."
        "But it'd be closer to the truth to say that they get right under it, and begin to irritate me almost straight away."
        "I find myself consciously trying to keep from doing anything that could be taken as mincing around."
        "And more than once I catch myself actually speaking in a deep and almost ridiculous tone of voice too."
        "A part of me can't believe that I'm acting in such a typically paranoid manner."
        "I'm a modern guy that's got no problem with that kind of thing whatsoever."
        "So why in the hell had being mistaken for a gay guy made me react like this?"
        "All I wanted to do was look good and dress well - surely I don't need to wear a sign, do I?!?"
        "I keep on telling myself that it's probably just Audrey and this Gregory guy she mentioned."
        "Surely it's not a vibe that I go around giving off to everyone that I meet?"
        "With this on my mind, I bring the subject up with Sam the next time I see her."
        mike.say "You will not believe what happened to me at work the other day."
        samantha.say "Really...what was it?"
        "I can sense that Sam knows I have an axe to grind."
        "But she's the kind of friend that's always ready to listen and offer sympathy."
        mike.say "Okay, listen to this."
        mike.say "So Audrey - that's this girl that I work with - comes into my office, right."
        "Sam nods."
        mike.say "And she starts telling me about how it's not fair I'm single."
        "Sam raises her eyebrows at this, but I press on regardless."
        mike.say "So, of course, I think she's coming on to me."
        samantha.say "Of course."
        mike.say "But then she tells me about this guy called Gregory."
        mike.say "How he's checked me out and she can set us up on a date!"
        "Sam keeps on looking straight at me for a couple of seconds."
        "Clearly she's expecting there to be more to the story."
        "When she realises that there's not, her expression quickly becomes sympathetic."
        samantha.say "Oh...oh no..."
        samantha.say "That's terrible, [hero.name]!"
        samantha.say "How could she think that?"
        "I nod, trying to convince myself that was the reaction I wanted out of her."
        mike.say "I know, right?"
        mike.say "How could she even think I was gay?"
        mike.say "I mean, you don't - do you?"
        mike.say "Think I'm gay, that is?"
        "Sam frowns and shakes her head, perhaps with a little too much vigour."
        samantha.say "No...no..."
        samantha.say "At least...not any more..."
        mike.say "Wait, what..."
        mike.say "What do you mean 'not any more'?!?"
        "Sam squirms under my gaze, clearly trying to pick her next words carefully."
        samantha.say "Well..."
        samantha.say "There was a little period where I might have a vague suspicion of something."
        "I look at her in askance, making her struggle all the more to justify herself."
        samantha.say "It was just when I first moved in with you and Ryan."
        samantha.say "And he soon put me right on that score."
        samantha.say "Now I couldn't imagine you in hot-pants...honestly."
        mike.say "But...but...how in the hell?!?"
        samantha.say "It's just...you do take better care of yourself than most guys, [hero.name]."
        samantha.say "You know - you dress well, work-out and have your hair cut every fourteen days without fail."
        mike.say "That's just because I take pride in my appearance!"
        mike.say "Do I have to be a gross, hairy slob for people to think I'm straight?!?"
        samantha.say "[hero.name], have you ever thought this Audrey might be winding you up on purpose?"
        mike.say "Wha..."
        mike.say "Ah, no...I guess not."
        samantha.say "Think about it - this Gregory wasn't there, was he?"
        samantha.say "And that's awfully convenient for her, you know?"
        samantha.say "Not to have to explain why she didn't know you were actually straight."
        mike.say "When you put it that way..."
        samantha.say "Isn't it!"
        samantha.say "For all you know, she could never have spoken to the guy."
        samantha.say "So he might not even know you exist!"
        mike.say "Hey, wait a minute!"
        mike.say "Are you saying that I'm not good enough for a guy like Gregory?"
        "Sam rolls her eyes, showing just how ridiculous she finds that question to be."
        samantha.say "Let's just forget about it, [hero.name]."
        samantha.say "How about that?"
        "I nod, still feeling a little hurt that Gregory's supposed crush on me might be a mere fiction."
        $ game.flags.gaymistake = 2
    elif result == 1:
        mike.say "Sometimes, my neck gets sore."
        samantha.say "Why?"
        mike.say "Because my brain is so big."
        "Samantha smirks a little."
    elif result == 2:
        samantha.say "When you stop expecting people to be perfect, you can like them for who they are."
    elif result == 3:
        mike.say "Why is it, I feel I've known you so many years?"
        samantha.say "Because I like you, and I don't want anything from you."
    elif result == 4:
        samantha.say "Every man I meet wants to protect me."
        samantha.say "I can't figure out what from."
    elif result == 5:
        samantha.say "What did Cinderella do when she got to the ball?"
        mike.say "Gagged."
    else:
        mike.say "The most painful thing is losing yourself in the process of loving someone too much, and forgetting that you are special too."
    $ samantha.love += 1
    return

label samantha_love_1_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "Insanity is doing the same thing, over and over again, but expecting different results."
    elif result == 2:
        samantha.say "Women and cats will do as they please, and men and dogs should relax and get used to the idea."
    elif result == 3:
        samantha.say "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it."
    elif result == 4:
        samantha.say "The statistics on sanity are that one out of every four people is suffering from a mental illness."
        samantha.say "Look at your 3 best friends."
        samantha.say "If they're okay, then it's you."
    else:
        samantha.say "My motto is get out before they go down."
        mike.say "That is so not my motto."
    $ samantha.love += 1
    return

label samantha_love_2_male:
    $ result = randint(1, 5)
    if result == 1:
        mike.say "When you're in jail, a good friend will be trying to bail you out."
        mike.say "A best friend will be in the cell next to you saying, 'Damn, that was fun'."
        samantha.say "No, a best friend would have stopped you from doing a stupid thing altogether."
    elif result == 2:
        samantha.say "Some humans would do anything to see if it was possible to do it."
        samantha.say "If you put a large switch in some cave somewhere, with a sign on it saying 'End-of-the-World Switch. PLEASE DO NOT TOUCH', the paint wouldn't even have time to dry."
    elif result == 3:
        samantha.say "I generally avoid temptation unless I can't resist it."
    elif result == 4:
        samantha.say "How can you tell when a blonde is dating?"
        mike.say "I don't know."
        samantha.say "By the buckle print on her forehead."
        samantha.say "How can you tell who is a blonde's boyfriend?"
        mike.say "Still don't know."
        samantha.say "He's the one with the belt buckle the matches the impression in her forehead."
    else:
        if not samantha.flags.birthdayknown:
            if samantha.flags.nickname == "cupcake":
                mike.say "Hey Cupcake, when is your birthday?"
            else:
                mike.say "Hey Samantha, when is your birthday?"
            samantha.say "It's on the [samantha.birthday[1]] of [samantha.birthday[0]]."
            samantha.say "Are you planning on getting me a gift?"
            mike.say "Maybe..."
            $ samantha.flags.birthdayknown = True
        else:
            mike.say "I'm not so good with giving advice."
            mike.say "Can I interest you in a sarcastic comment?"
    $ samantha.love += 1
    return

label samantha_love_3_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "How does a guy know if he has a high sperm count?"
        mike.say "Don't know."
        samantha.say "If the girl has to chew, before she swallows."
    elif result == 2:
        samantha.say "You know..."
        mike.say "What?"
        samantha.say "Don't tell but I have this weird kink, like sexual..."
        samantha.say "I like sucking dick almost as much as being fucked..."
        mike.say "Interesting."
    elif result == 3:
        samantha.say "I went to the movie theatre the other day.."
        samantha.say "There was a girl blowing her boyfriend there..."
        samantha.say "I saw her get his cum splattered all over her face."
        samantha.say "She cleaned it up with her tongue and fingers..."
        samantha.say "That was so hot."
    elif result == 4:
        samantha.say "I could totally eat a banana right now."
    else:
        samantha.say "So do you have a girlfriend?"
    $ samantha.love += 1
    return

label samantha_love_4_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "What's the difference between a blonde and a mosquito?"
        mike.say "Don't know."
        samantha.say "One stops sucking when you smack it."
    elif result == 2:
        samantha.say "I never tried anal sex..."
        mike.say "You know, we could fix that."
    elif result == 3:
        samantha.say "I kind of like blonde jokes."
        mike.say "I noticed."
    elif result == 4:
        samantha.say "Don't you think girls that are honest with their desires are the sexiest?"
    else:
        samantha.say "I would totally eat a twinkie..."
    $ samantha.love += 1
    return

label samantha_love_5_male:
    $ result = randint(1, 5)
    if result == 1:
        samantha.say "What's the definition of trust?"
        mike.say "Don't know."
        samantha.say "Two cannibals giving each other a blowjob."
    elif result == 2:
        samantha.say "You know I don't have any gag reflex?"
    elif result == 3:
        samantha.say "I watched porn the other day, that girl had her whole face covered with the cum from a dozen guys."
        samantha.say "I thought she looked like me a little."
    elif result == 4:
        samantha.say "So, how is life with your roommates?"
    else:
        samantha.say "I don't think I ever had a closer friend than you."
    $ samantha.love += 1
    return

label samantha_good_sweet_talk_male:
    show samantha
    if "samantha_event_02" in DONE and not samantha.flags.engaged:
        if samantha.flags.nickname == "cupcake":
            mike.say "Part of me still can't believe we're finally together, Cupcake."
        else:
            mike.say "Part of me still can't believe we're finally together, Sam."
        mike.say "I'd pinch myself, but I'm afraid I might wake up!"
        show samantha happy
        samantha.say "Me too, [hero.name]."
        samantha.say "It was a long road getting here."
        show samantha normal
        samantha.say "But it was worth it!"
    elif samantha.love > 66:
        mike.say "You know why I call you my cupcake, Sam?"
        mike.say "Because you're sweet and you make everything better!"
        show samantha happy
        samantha.say "Oh, stop it!"
        show samantha flirt
        samantha.say "Actually don't - I love it when you talk like that about me!"
    else:
        if samantha.flags.nickname == "cupcake":
            mike.say "I'm so glad we didn't lose contact when you moved out, Cupcake."
        else:
            mike.say "I'm so glad we didn't lose contact when you moved out, Sam."
        mike.say "I don't know what I'd do without a friend like you."
        show samantha blush
        samantha.say "Aww...that's so sweet!"
        samantha.say "I feel the same way about you too."
    hide samantha
    return

label samantha_bad_sweet_talk_male:
    show samantha
    if samantha.flags.nickname == "cupcake":
        mike.say "Why did I spend all that time looking for love, Cupcake?"
    else:
        mike.say "Why did I spend all that time looking for love, Sam?"
    mike.say "When you were right there under my nose!"
    show samantha annoyed
    samantha.say "Whoa...you make it sound like I was there for the taking!"
    samantha.say "Like you were waiting in line for a chance to ride me!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Erm, no...that's not what I meant, Cupcake!"
    else:
        mike.say "Erm, no...that's not what I meant, Sam!"
    hide samantha
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
