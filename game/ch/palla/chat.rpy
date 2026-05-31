label palla_desire_0_male:
    call palla_chat_switcher_male ((1, 1, 2, 0, 0)) from _call_palla_chat_switcher_male
    return

label palla_desire_1_male:
    call palla_chat_switcher_male ((1, 1, 1, 2, 0)) from _call_palla_chat_switcher_male_1
    return

label palla_desire_2_male:
    call palla_chat_switcher_male ((1, 1, 2, 3, 1)) from _call_palla_chat_switcher_male_2
    return

label palla_desire_3_male:
    call palla_chat_switcher_male ((1, 1, 1, 2, 2)) from _call_palla_chat_switcher_male_3
    return

label palla_desire_4_male:
    call palla_chat_switcher_male ((1, 1, 0, 1, 2)) from _call_palla_chat_switcher_male_4
    return

label palla_desire_5_male:
    call palla_chat_switcher_male ((1, 1, 0, 1, 3)) from _call_palla_chat_switcher_male_5
    return

label palla_love_0_male:
    call palla_chat_switcher_male ((1, 1, 2, 0, 0)) from _call_palla_chat_switcher_male_6
    return

label palla_love_1_male:
    call palla_chat_switcher_male ((1, 1, 1, 2, 0)) from _call_palla_chat_switcher_male_7
    return

label palla_love_2_male:
    call palla_chat_switcher_male ((1, 1, 2, 3, 1)) from _call_palla_chat_switcher_male_8
    return

label palla_love_3_male:
    call palla_chat_switcher_male ((1, 1, 1, 1, 2)) from _call_palla_chat_switcher_male_9
    return

label palla_love_4_male:
    call palla_chat_switcher_male ((1, 1, 0, 1, 2)) from _call_palla_chat_switcher_male_10
    return

label palla_love_5_male:
    if "palla_chat_gf_talk_male" not in DONE and "palla_event_13" in DONE and palla.is_girlfriend and not palla.flags.minealone:
        call palla_chat_gf_talk_male from _call_palla_chat_gf_talk_male
        $ DONE["palla_chat_gf_talk_male"] = game.days_played
        return

    call palla_chat_switcher_male ((1, 1, 0, 1, 3)) from _call_palla_chat_switcher_male_11
    return

label palla_chat_switcher_male(palla_talk_chances=(1, 1, 2, 0, 0)):
    python:
        result = randint(1, palla_talk_chances[0] + palla_talk_chances[1] + palla_talk_chances[2] + palla_talk_chances[3] + palla_talk_chances[4])
        palla_talk_hooks = ('palla_chat_love_male', 'palla_chat_sex_male', 'palla_chat_bitchy_male', 'palla_chat_cautious_male', 'palla_chat_sexy_male')
        test = 0
        for i in range(0, 5):
            test += palla_talk_chances[i]
            if result <= test:
                renpy.call_in_new_context(palla_talk_hooks[i])
                break
    return

label palla_chat_bitchy_male:
    $ result = randint(1, 8)
    if result == 1:
        palla.say "Audrey can't shut up about you."
        palla.say "I don't see what the fuss is about."
    elif result == 2:
        palla.say "Fuck, do you ever brush your teeth?"
        palla.say "You smell like a dead cat."
    elif result == 3:
        palla.say "I'm bored."
    elif result == 4:
        palla.say "Why do you think you can talk to me? I'm out of your league."
    elif result == 5:
        palla.say "I'm trying to decide what's more annoying. You or high school."
    elif result == 6:
        palla.say "I don't know why Audrey likes you so much. You're kind of an asshole."
    elif result == 7:
        palla.say "The other night I was out at the club and there was this dude who couldn't dance for shit. He tried to dance with me, and he was kind of cute but almost as much of an asshole as you are."
    else:
        palla.say "Did you see that Chanel ad? The blonde with the crooked smile? I don't know how she got that job. I should've gotten that job. I'm prettier than she is."
    return

label palla_chat_cautious_male:
    $ result = randint(1, 5)
    if result == 1:
        palla.say "If you weren't a little bit sexy, I wouldn't have anything to do with you."
        mike.say "Wait, was that supposed to be a compliment?"
        palla.say "Not really."
        mike.say "But you think I'm sexy?"
        palla.say "It's a low bar."
        $ palla.love += 1
    elif result == 2 and not palla.flags.minealone:
        palla.say "Have you ever thought about having just one girlfriend?"
        mike.say "What do you mean?"
        palla.say "Oh don't look at me like that, I know you like to get around. It's okay."
        palla.say "I thought about having just one boyfriend but I don't think any one boy can handle me."
        menu:
            "I could":
                mike.say "I could handle you."
                palla.say "Dude, you can barely handle talking to me, let alone me as a girlfriend. You think I'm a bitch now? Hah!"
                $ palla.love += 1
            "Nobody could":
                mike.say "Yeah, nobody could handle you."
                palla.say "Yeah, it's depressing. You'd think some guy, somewhere would have the balls to handle me. Someday."
                $ palla.love += 1
            "3 guys and some rope":
                mike.say "It would take 3 guys and some rope to handle you."
                "She just looks at me, clearly pretending to be angry. I decide to push my luck a little."
                mike.say "Oh man, all three holes and you helpless. That's kind of hot."
                "She swallows, but looks aroused, though she's trying to hide it."
                palla.say "Knock it off, asshole, that's not funny."
                mike.say "Nope, not funny, just hot."
                palla.say "I hate you so much."
                $ palla.love += 1
                $ palla.sub += 1
    elif result == 3 and not palla.flags.babyok:
        palla.say "I hate children."
        mike.say "What brought that up?"
        palla.say "Oh, just everyone always asking me when I'm going to have kids. Never. Fucking never. Little rugrats. Who has time for that?"
        palla.say "Besides, if I ever got pregnant, I'd never get my tummy flat again. It's depressing. What would I do then?"
        mike.say "I don't know. Take care of your kids?"
        palla.say "See the part where I hate the little fuckers."
        mike.say "Right."
        "She looks at me and tilts her head."
        palla.say "Why, do you? You don't strike me as the type to want kids either."
        mike.say "Why's that?"
        palla.say "Well, you strike me as the love 'em and leave 'em type. Or more likely pump 'em and dump 'em."
        mike.say "Ouch! Now what did I ever do to give you that impression?"
        palla.say "I can just tell. I can see into your black, evil soul."
        mike.say "Well, for your information, Miss Know-it-all, I'd like children. With the right person, of course."
        palla.say "What's the right person?"
        mike.say "I don't know. Someone who's hot, obviously. Knows what she wants. Smart. Successful. Funny. You know."
        palla.say "So not really any of the bitches you hang out with."
        mike.say "Did you just self-own?"
        palla.say "Oh. Okay not MOST of the bitches you hang out with."
        mike.say "For the record, I did NOT just say I want to have kids with you."
        palla.say "Oh thank God, because I swear I'd punch you in the face."
        $ palla.love += 1
    elif result == 4 and not palla.flags.managecareer:
        palla.say "Did I ever tell you about my family?"
        mike.say "No, I don't think you have."
        palla.say "Good because I'm not sure you'd want to know them. They certainly wouldn't want to know you."
        mike.say "Damn, you can be a bitch sometimes."
        palla.say "So?"
        mike.say "So now you've got me curious, because I never thought of you as having a family. I kinda thought of you as having emerged from the ooze, fully formed, ready to give the world the finger."
        palla.say "Huh. Better than what I got, I guess. Except maybe my little sister, she's okay. Fuck the rest of them though."
        mike.say "Seriously, is there anybody you like?"
        palla.say "My sister. Audrey. My agent, I guess."
        mike.say "I know I'll regret saying this, but you left me out of that list."
        palla.say "Yes, yes I did."
        mike.say "Why do you talk to me again?"
        palla.say "I have no idea."
        $ palla.love += 1
    else:
        palla.say "I'm impressed that you still put up with me. I mean not as much as I'm impressed that I still put up with you, but even so. I'm a handful, you know."
        mike.say "Oh yes, I've noticed."
        palla.say "Anyway, um, thanks."
        mike.say "Um, yeah. You're welcome?"
        palla.say "So why do you put up with me, anyway?"
        mike.say "Are you drunk?"
        palla.say "Maybe. Maybe not. Answer the question."
        mike.say "I don't know. Maybe it's because every once in awhile, between being a bitch and a mega bitch, you say something sweet."
        palla.say "Uh huh."
        mike.say "And maybe it's because you've got nice tits."
        palla.say "At least you're consistent."
        $ palla.love += 1
    return

label palla_chat_sexy_male:
    $ choices = 3
    if not palla.flags.nokiss:
        $ choices += 2
    if palla.sexperience > 3:
        $ choices += 2
    $ result = randint(1, choices)
    if result == 1:
        palla.say "Are you only hanging out with me because I've got nice tits?"
        mike.say "I'll get in trouble if I say yes, won't I?"
        palla.say "Absolutely."
        menu:
            "It's the tits. And the ass.":
                mike.say "It's not just about your tits. You also have a sexy ass. And legs. Actually you're sexy from top to bottom."
                palla.say "That's...a nice save."
                $ palla.love += 1
            "I actually like you":
                mike.say "Okay Palla, I'll bite. I hang out with you because I actually like you."
                palla.say "But I'm a grade A bitch."
                mike.say "A {b}sexy{/b} grade A bitch, and I also know what's really under there."
                palla.say "Oh. Oh. Um. Oh!"
                mike.say "What's the matter, cat got your tongue?"
                palla.say "I guess I wasn't expecting you to say something nice."
                $ palla.love += 2
            "I like a woman on her knees" if palla.sub > 40:
                mike.say "I like a woman on her knees. I like a bitch who can be my bitch. You know?"
                palla.say "And you think I'm your bitch?"
                if palla.sub > 80 or palla.is_sex_slave:
                    mike.say "Yeah, you're my bitch, Bitch."
                else:
                    mike.say "Not yet. I know I haven't earned it yet. But I will."
                "Palla shivers."
                $ palla.sub += 2
    elif result == 2:
        palla.say "I like men who are handsome, strong gentlemen who are chivalrous and pull out a lady's chair and bring her breakfast and recite poetry under the moon."
        palla.say "You're handsome, at least, so 1 out of, uh, what is that 12? Isn't bad."
        mike.say "Ouch, my ego is bruised. No really."
        palla.say "Hey it's a really important 1."
        $ palla.love += 1
    elif result == 3:
        palla.say "I love to dance. The best way to end a night is to turn everything off and just lose myself in the music. It's best with a hot guy who can dance just as well as I can."
        if not hero.has_skill("dance"):
            mike.say "What about with a guy who can't dance?"
            palla.say "Just not the same, but maybe if he's teachable."
        else:
            mike.say "Yeah, the rhythm, the sweat."
            palla.say "It's almost as good as sex."
        $ palla.love += 1

    elif result == 4:
        palla.say "You know, you're a much better kisser than I thought you'd be."
        mike.say "I don't know if I should be happy you think I'm a good kisser or pissed that you assumed I wouldn't be good at it."
        palla.say "Don't get a big head, you're not {b}that{/b} good of a kisser."
        mike.say "Typical."
        palla.say "That's okay, you just need some practice."
        mike.say "Are you offering to be my practice partner?"
        palla.say "Don't get ahead of yourself."
        $ palla.love += 2
    elif result == 5:
        palla.say "You want to hear something weird?"
        mike.say "That depends."
        "Palla goes right on, ignoring my lukewarm answer."
        palla.say "It kind of turns me on, thinking about you and your other girlfriends."
        palla.say "Seriously, sometimes I close my eyes and I imagine you and those roommates of yours, one of them in your arms and one of them on her knees."
        palla.say "Really gets me going."
        menu:
            "Both in my arms, you on your knees":
                mike.say "Better. One of them in each arm, and you on your knees."
                palla.say "Um. Yeah I better go and, um. Fix my makeup."
                $ palla.sub += 1
            "Damn that's hot":
                mike.say "Damn that's hot. Also I'm afraid if I admit it you're going to go \"{b}hah{/b} just kidding what an asshole!\""
                palla.say "Me??"
                mike.say "Yes, you."
                palla.say "Well. Okay I would, but not this time. It's hot, okay?"
                if palla.sexperience > 3:
                    palla.say "And just so you know, I do not care who else you fuck."
                else:
                    palla.say "I've never been a one girl one guy kind of gal."
                $ palla.love += 1
            "I'd never!":
                mike.say "I'd never do anything like that."

                if bree.sexperience < 1 and sasha.sexperience < 1 and audrey.sexperience < 1:
                    palla.say "No? That's too bad. You'd be a whole lot sexier with a little harem."
                    palla.say "You'd better get to work on that."
                    menu:
                        "Sure":
                            mike.say "Sure, I'll get right on that."
                            $ palla.love += 1
                        "I don't want a harem":

                            mike.say "I'm just not interested in a harem. What kind of guy do you think I am?"
                            palla.say "I dunno, I guess I thought you were interesting."
                            $ palla.love -= 1
                        "I only want you":
                            mike.say "You're the only woman I want."
                            "Palla nearly chokes."
                            palla.say "Seriously, [hero.name]?"
                            mike.say "Yeah, seriously!"
                            palla.say "You're one fucked up guy. But okay, I'll play along. For now."
                            $ palla.love += 2
                else:
                    palla.say "Oh don't fucking lie to me, asshole. You're as transparent as glass. And why bother lying about this anyway?"
                    palla.say "I just told you it turns me on, and you lied about it? What, did you think I was trying to trap you?"
                    palla.say "Me? Come on, think, [hero.name]. Ugh. I don't care who you fuck, but I do care if you lie about it."
                    $ palla.love -= 20

    elif result == 6:
        palla.say "You know, [hero.name], I actually like having sex with you."
        mike.say "It would be weird if you didn't since we keep doing it."
        palla.say "You'd be surprised how many people have sex they hate because they think they should."
        mike.say "Okay, maybe."
        palla.say "Anyway, I like what you do to me. Most guys...well anyway, I've never told any guy that, so don't spread that around."
        mike.say "Ah, embarrassed by me?"
        palla.say "No, I just don't like it when people know I like things."
        palla.say "Things like your cock."
        $ palla.love += 1
    else:
        palla.say "The problem with loving men who are assholes is that they always hurt you."
        mike.say "To be fair you like it when I hurt you."
        palla.say "No, I don't mean like that. I mean they fuck you, and use you, and then lose you. And then all you got is a sore ass and a broken heart."
        mike.say "I'm still here."
        palla.say "Yeah, you are. I keep waiting for you to disappear in the night."
        mike.say "Never."
        if palla.love > 190:
            palla.say "I don't remember a time in my life when I wasn't lonely. Even with a guy, because I always knew he would be gone soon."
            palla.say "But I'm not lonely right now."
        else:
            palla.say "Normally I wouldn't let myself care. I'm used to waking up lonely, and I tell myself I can keep doing it."
            palla.say "But right this second I think if you disappear on me now, I'll hunt you down and feed you your own balls."
        $ palla.love += 1
    return

label palla_chat_love_male:
    mike.say "What's your take on love?"
    if palla.love < 40:
        palla.say "Love is for for suckers. I don't believe in love. You just get your heart broken."
        "Palla looks sad, like there's a story there."
        mike.say "Do you want to talk about it?"
        palla.say "Fuck off."
        mike.say "That's a no, then."
        $ palla.love -= 1
    elif palla.love < 80:
        palla.say "Love is for users. We use love to control the ones we say we love. We fuck them once and then we fuck them again."
        palla.say "In the end, all you get is fucked."
        mike.say "Damn, Palla, that's depressing."
        palla.say "Well, you asked."
    elif palla.love < 120 or palla.sexperience < 3:
        palla.say "I know I said I don't believe in love, but sometimes I wish a guy would romance me, the old fashioned way."
        mike.say "What do you mean?"
        palla.say "Flowers, candy, serenading at the window. And dancing until the sun comes up."
        mike.say "Huh, I don't remember ever hearing about that last part."
        palla.say "It's what the witches used to do."
        mike.say "Oh, that explains it. You're definitely a witch."
        palla.say "And fuck you too, asshole."
        $ palla.love += 1
    elif palla.love < 160:
        "Palla looks me right in the eyes and her expression softens."
        palla.say "I think I might be falling for you, [hero.name]."
        mike.say "Wow."
        "Palla looks at me and her eyes slowly start to narrow."
        mike.say "Am I supposed to say something?"
        palla.say "If you want me in your bed any time soon, you fucking better."
        "I laugh a little, but gently, not in a way to mock her. That could be bad for her right now."
        mike.say "Yeah, I like you too."
        palla.say "{b}Like{/b}?!"
        mike.say "Fine, I think you're a hot, sexy charming bitch and I love fucking you, and hanging out with you."
        palla.say "And dancing?"
        if hero.has_skill("dance"):
            mike.say "Oh fuck yeah, the dancing might be the best part."
            palla.say "I guess that'll do."
        else:
            mike.say "Oh and the dancing too, I guess. But really it's the fucking."
            palla.say "[hero.name], you're as romantic as a tractor. A sexy tractor, but a tractor nonetheless."
            mike.say "You say the sweetest things, bitch!"
        $ palla.love += 1
    else:
        if palla.is_sex_slave:
            palla.say "I'm definitely in love with you. And only you, Master."
            mike.say "I love you too, my sexy, sassy slave."
            palla.say "I hope you'll fuck me again soon?"
            mike.say "Bet on it."
        else:
            "Palla looks at me with deeply serious eyes."
            palla.say "I love you, [hero.name]."
            palla.say "And you don't even need to say it back."
            mike.say "You're the best thing that's ever happened to me."
            "A pause for half a second, and let a smile curl up at one corner of my lip."
            mike.say "Bitch."
            "Palla laughs merrily."
            palla.say "I love you even if--no, because of that. Fuck me again soon!"
        $ palla.love += 1
    return

label palla_chat_sex_male:
    mike.say "What's your take on sex?"
    if palla.love < 40:
        if hero.grooming < 6:
            palla.say "Don't talk about sex, you smell like the sewer backed up."
            if game.room != palla.room:
                mike.say "How do you know that on the phone?"
                palla.say "I can smell you from all the way over here! Ugh go shower already! Gross!"
            else:
                mike.say "Damn you can be a bitch sometimes."
                palla.say "I'd be less of a bitch if you showered."
                mike.say "I doubt that."
        else:
            palla.say "Gross! Not with you, that's for sure!"
    elif palla.love < 120:
        palla.say "Sex is overrated. Every man wants sex, hell half the women I know want to have sex with me."
        palla.say "I mean I get it, I'm as hot as the sun if the sun were a smokin' hot redhead, but still."
        palla.say "Can't you guys ever think of anything else?"
        mike.say "I never said you were hot."
        palla.say "You didn't have to, I can tell by the way you stare at my tits all day."
        mike.say "Really you're so full of yourself."
        palla.say "Yeah, and I bet you wish I was full of you."
        "I hate to admit when I don't have a come back, but."
        "I don't have a comeback."
        "Palla laughs at my discomfort."
        palla.say "One point for the hot bitch, and the loser needs a beer."
        $ palla.love += 1
    else:
        $ renpy.dynamic("result")
        $ result = randint(1, 3)
        if result == 1:
            palla.say "I once fucked my photographer. I know, I shouldn't have done it, but he had an eye like no other."
            palla.say "He was able to get the best shots out of me with just a word or a look. Damn he was hot."
            palla.say "And he had the biggest dick. I swear my cunt ached for three days after he fucked me, but oh my god did I come so hard."
            palla.say "Fuck that was hot."
            mike.say "I'm pretty sure I didn't want to hear about another guy you fucked."
            palla.say "Too bad, it's part of the package. Don't want hear about it, don't ask."
            mike.say "Ugh, you're such a bitch."
            palla.say "Damn straight."
        elif result == 2:
            palla.say "This last trip in Belize, me and one of the other girls, this blonde from...oh fuck where was she from? Czech Republic or something like that?"
            palla.say "Fuck, I don't remember. Anyway she didn't speak a word of English, and she had these really great shoulders, and legs that went for miles."
            palla.say "Anyway, she and I are working the camera like crazy and some guy shouted he wished he could have a threesome with us."
            palla.say "Oh it was beautiful. At the same time we both flipped him 2 birds, and everyone busts up laughing."
            palla.say "And then, oh god she turned and kissed me, right there. On the mouth, tongue down my throat and everything."
            palla.say "I swear I'll kill Juan if those pictures ever get out."
            mike.say "Yeah, but tell me more about the blonde!"
            "Palla looks at me sideways."
            palla.say "What, do you want to hear that we went back to the hotel and had hot hot lesbian sex?"
            mike.say "Yes, I'd like to hear that you went and had hot hot lesbian sex."
            palla.say "Maybe we did, maybe we didn't. I ain't tellin'."
            mike.say "Damn, that actually was going to be a pretty good story too, right until the end."
            palla.say "I will say, though, I'll never forget her tongue."
            "Palla waggles her eyebrows at me."
        else:
            palla.say "Tell me, [hero.name], why are guys so fucked up about sex? I mean really, it's like you get a pair of these nice tits in your face and that's all you can think about. Tits tits tits!"
            mike.say "Fuck, Palla, have you {b}seen{/b} your tits?"
            palla.say "Well, yeah, they're hot."
            mike.say "Well, there you go!"
            palla.say "Seriously, [hero.name], I don't spend hours looking in the mirror thinking how much I'd like to caress these babies."
            mike.say "No, you spend hours looking in the mirror thinking how much you'd like {b}me{/b} to caress those babies."
            "Palla looks at me, actually surprised."
            palla.say "Ok, fine, you win this round."
            mike.say "And here I thought you were going to call me a creep."
            palla.say "Enh, you earned this one."
    $ palla.love += 1
    return

label palla_chat_gf_talk_male:
    $ palla.flags.gftalk = True
    palla.say "So, how's it going with your other bitches, [hero.name]?"
    mike.say "Oh, great. How's it going with your other guys?"
    palla.say "Oh. Un, fine! Good actually, I guess."
    "Huh. Her tone did not match her words there. It sounded anything but fine."
    mike.say "Something wrong? Did something go badly?"
    palla.say "No, everything's great! I, uh. Yeah, had a great date the other night!"
    mike.say "With who?"
    palla.say "Oh, some, just some guy."
    mike.say "Shawn?"
    palla.say "Ew, no. Just some guy."
    mike.say "What's his name?"
    palla.say "Uh, Michael."
    mike.say "Why are you lying?"
    palla.say "Oh for fuck's sake, [hero.name], is it you business?"
    mike.say "It's not my business, but our relationship is open, right? It requires honesty."
    palla.say "Oh {b}fine{/b}! Nobody, okay? I haven't actually dated anyone else."
    mike.say "Why not?"
    palla.say "I don't...actually want to."
    mike.say "Oh."
    mike.say "Oh!"
    mike.say "Wait. Why not?"
    palla.say "I don't know. Other guys just haven't really interested me."
    if palla.sexperience > 5:
        palla.say "Besides, you work me hard enough, I'm too sore for anyone else right now."
    mike.say "Huh."
    mike.say "So, does that mean you want to be exclusive?"
    palla.say "No!"
    mike.say "You're not convincing me."
    "Silence."
    mike.say "So?"
    palla.say "I mean, exclusive with you? Gross."
    mike.say "Nice. I mean I know you feel free to speak your mind, but my ego isn't unbreakable."
    palla.say "Fine, not gross. Just..."
    mike.say "I know, I know."
    palla.say "Do you want me to?"
    "One last chance! Do I want her to be exclusive?"
    menu:
        "Yes!":
            mike.say "I...yeah, I kind of do."
            $ palla.flags.minealone = True
            palla.say "Well. We'll see, I guess."
            mike.say "Oh no, don't you dare pull that bullshit on me. You don't get to ask that and weasel out of it if I answer wrong."
            palla.say "Oh my God! You're so needy!"
            mike.say "Yeah, fuck you too. So that settles it, you're not seeing anyone else now."
            palla.say "Uh. Did I say that?"
            mike.say "You're about to."
            palla.say "Stop telling me what to do!"
            mike.say "Palla..."
            palla.say "Fine. I won't see anyone else. I wasn't going to, anyway. There, happy?"
        "No":
            mike.say "Well, you're not seeing anyone else anyway, so it looks like there's no real competition anyway."
            palla.say "Full of yourself, aren't you?"
            mike.say "You're the one full of me, babe."
            palla.say "Ugh. Just for that, I'm going to find someone and go out. I'll suck the guy off {b}just{/b} for that stupid line."
            mike.say "Yeah, and you'll be thinking of me the whole time."
            palla.say "In your dreams."
            "She will, though. She will be thinking of me."
    return

label palla_good_sweet_talk_male:
    show palla
    if palla.love > 133:
        mike.say "I'm the luckiest guy in the world, Palla."
        mike.say "You'd look good on the arm of a movie-star."
        mike.say "But you're with me instead!"
        palla.say "I know what you mean."
        palla.say "You really are lucky to have me!"
    elif palla.love > 66:
        mike.say "I don't know how you do it, Palla."
        mike.say "You must have the perfect outfit for every occasion!"
        show palla happy
        palla.say "It's sweet of you to say so."
        palla.say "I do - but it's SUCH hard work!"
    else:
        mike.say "Whoa..."
        mike.say "You really know how to turn heads, Palla!"
        mike.say "Everyone's looking at you!"
        palla.say "Thanks for noticing, [hero.name]."
        palla.say "It's a burden I have to bear constantly!"
    hide palla
    return

label palla_bad_sweet_talk_male:
    show palla
    mike.say "Wow, Palla - you wear some crazy stuff!"
    show palla angry
    palla.say "Hey!"
    palla.say "I follow the latest fashions, like a religion!"
    palla.say "So that's blasphemy!"
    mike.say "Oops...maybe I should confess my sins?"
    hide palla
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
