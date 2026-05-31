label hanna_talk_love_female:
    hanna.say "I want to believe in true love, [hero.name]."
    hanna.say "But it's SO hard to save yourself for just one person!"
    hanna.say "Especially when you look like I do."
    hanna.say "And you just know everyone's eyeing you up all the time!"
    menu:
        "I kinda like these looks":
            bree.say "Don't be silly, Hanna!"
            bree.say "Those are two totally different things."
            bree.say "There's nothing wrong with getting admiring looks."
            bree.say "It's not like being unfaithful!"
            $ hanna.love += 1
        "Your outfit matters":
            bree.say "Well...you ARE a bit of a flirt, Hanna!"
            bree.say "You're always wearing tight clothes and flexing in public."
            bree.say "You might want to try toning it down a little?"
            $ hanna.love -= 1
        "Focus on one person":
            bree.say "Well...couldn't you do both, Hanna?"
            bree.say "Just concentrate of keeping the eyes of one person on you?"
            bree.say "That way you can have the best of both worlds!"
            $ hanna.sub += 1
        "Embrace your appearance":
            bree.say "Why would you care about impressing just one person, Hanna?"
            bree.say "I thought you were like a modern woman with a career and all that?"
            bree.say "Who cares if people are always giving you admiring glances?"
            bree.say "That just means you're super hot!"
            $ hanna.sub -= 1
    return

label hanna_talk_sex_female:
    hanna.say "Sex is SO much better when you're in peak physical condition, [hero.name]!"
    hanna.say "You can go longer and harder, and it just feels so good!"
    hanna.say "I kind of feel sorry for people who are out of shape."
    hanna.say "It's like they look terrible, and you know they're bad in bed too!"
    menu:
        "That's mean but...":
            bree.say "Oh Hanna, that's so bad of you to say!"
            bree.say "But you're right."
            bree.say "Working out in the gym pays off in bed!"
            $ hanna.love += 1
        "I don't work out everyday!":
            bree.say "That's so unfair of you, Hanna!"
            bree.say "Not everyone can work out all the time, you know?"
            bree.say "And what about people that can't work out at all, huh?"
            bree.say "You're crapping on them for something they can't help!"
            $ hanna.love -= 1
        "For whom do you train so hard?":
            bree.say "Oh for sure, Hanna!"
            bree.say "But just remember who you're keeping yourself in shape for, yeah?"
            bree.say "The harder you work for them, the happier they'll be!"
            $ hanna.sub += 1
        "I agree":
            bree.say "That's what I love about you, Hanna."
            bree.say "You're totally in control of your own life."
            bree.say "There's nobody telling you to keep in shape."
            bree.say "It's like you're doing it for your own sake, and that's enough."
            $ hanna.sub -= 1
    return

label hanna_talk_politics_female:
    hanna.say "I know that I should be more clued-up when it comes to politics, [hero.name]."
    hanna.say "But I'm so busy running things at the gym, taking on more responsibility."
    hanna.say "By the end of the day I'm physically exhausted."
    hanna.say "And the paperwork is killing my brain too!"
    menu:
        "Take some time to think":
            bree.say "You should really give yourself a break, Hanna."
            bree.say "So what if you're a little out of touch?"
            bree.say "You can always catch up on that sort of thing."
            bree.say "And you're pretty smart too."
            bree.say "You already know who to vote for when the time comes!"
            $ hanna.love += 1
        "Your dog ate your homework too?":
            bree.say "You can make excuses all you like, Hanna."
            bree.say "It doesn't change the fact that you're out of touch."
            bree.say "Nobody's saying you need to become a political activist."
            bree.say "Just take the time to get informed!"
            $ hanna.love -= 1
        "I'm not a huge fan either":
            bree.say "Maybe you're just not the political type, Hanna?"
            bree.say "Some people aren't, you know?"
            bree.say "They're just better off leaving it to other people."
            $ hanna.sub += 1
        "You can handle":
            bree.say "You can always do both, Hanna!"
            bree.say "You're already a tough, in-control woman."
            bree.say "In fact, I'm sure you could do anything you put your mind to!"
            $ hanna.sub -= 1
    return

label hanna_talk_food_female:
    hanna.say "I always feel like I want to go crazy and eat what I like, [hero.name]."
    hanna.say "But my diet's super-healthy and SO important to keeping in shape."
    hanna.say "I really envy people that can just eat whatever they like."
    hanna.say "They're so lucky that they can indulge themselves!"
    menu:
        "That's really impressive!":
            bree.say "You should be proud of yourself, Hanna."
            bree.say "You must have such strong will-power!"
            bree.say "I wish I could be more like you."
            bree.say "Sometimes I dread using the bathroom scales!"
            $ hanna.love += 1
        "Junk food is not that bad":
            bree.say "You don't have to be perfect, Hanna!"
            bree.say "What's the point in torturing yourself like that?"
            bree.say "I mean, are you really doing it to keep in shape?"
            bree.say "Or is it all for the sympathy?"
            $ hanna.love -= 1
        "That what's called self-sacrifice":
            bree.say "Self-denial really helps to make you humble, Hanna."
            bree.say "It means you're shooting for something bigger than yourself."
            bree.say "You know what I mean?"
            $ hanna.sub += 1
        "keep control on your life!":
            bree.say "You should be proud of yourself, Hanna!"
            bree.say "You're one hundred percent in control of your life."
            bree.say "I'd be amazed if you let anyone tell you what to do!"
            $ hanna.sub -= 1
    return

label hanna_talk_travels_female:
    hanna.say "I want to travel so badly, [hero.name]!"
    hanna.say "And I know everyone says that."
    hanna.say "But I'm doing well at the gym right now."
    hanna.say "So I think I have enough saved up to do it."
    hanna.say "It's just getting the time off of work that's the problem!"
    menu:
        "Take some days off":
            bree.say "Most people are just talking about it, Hanna."
            bree.say "At least you have the cash stashed away."
            bree.say "All you need to do is get the time off."
            bree.say "And for the boss's daughter, that shouldn't be hard!"
            $ hanna.love += 1
        "Bad faith!!!":
            bree.say "So what's stopping you asking for the time off, Hanna?"
            bree.say "You're like the boss's daughter, for heaven's sake!"
            bree.say "Your job's still going to be there when you get back."
            bree.say "Sounds to me like you're just making up excuses!"
            $ hanna.love -= 1
        "That's a big step":
            bree.say "I know what you mean, Hanna."
            bree.say "It's about having the courage to take that leap."
            bree.say "There's no shame in being a little afraid."
            bree.say "Maybe you just need someone to take the lead?"
            $ hanna.sub += 1
        "That's just a trip":
            bree.say "You've got nothing to worry about, Hanna!"
            bree.say "You can handle a trip around the world, easy!"
            bree.say "You're a super-confident, professional woman."
            bree.say "There's nothing you can't do if you try."
            $ hanna.sub -= 1
    return

label hanna_talk_television_female:
    hanna.say "Everyone's always gossiping about the TV shows they're watching, [hero.name]."
    hanna.say "But I just don't have the time to sit down and watch any of them myself."
    hanna.say "I'm so busy at the gym, teaching classes and keeping myself in peak condition."
    hanna.say "I've got to admit, it makes me feel a bit left out!"
    menu:
        "You don't need to worry about that":
            bree.say "Why would you say that, Hanna?"
            bree.say "All they're doing is sitting on their asses!"
            bree.say "It's not your fault you have something better to do."
            bree.say "They should be jealous of you!"
            $ hanna.love += 1
        "Stop complaining":
            bree.say "Oh stop fishing for compliments, Hanna!"
            bree.say "I get it already - you're a big fitness freak!"
            bree.say "Not everyone's a fanatic like you are."
            bree.say "But that doesn't make it okay to gloat about it!"
            $ hanna.love -= 1
        "One goal at a time":
            bree.say "I'm sure you've got better things to do than watch TV, Hanna."
            bree.say "It's like you're devoting yourself to one thing and one thing only."
            bree.say "I'm sure a lot of people would find that really attractive..."
            $ hanna.sub += 1
        "That's just a waste of time":
            bree.say "You should be proud that you've got better things to do, Hanna."
            bree.say "You're not wasting your life in front of the TV."
            bree.say "It's like you're the one in control."
            bree.say "And you don't need anyone to tell you what to do."
            $ hanna.sub -= 1
    return

label hanna_talk_sports_female:
    hanna.say "Sometimes I just don't know what I'd do without sports, [hero.name]!"
    hanna.say "It feels so good to have something that I can just rely on, you know?"
    hanna.say "Something that's always there for me when I need it."
    hanna.say "In can just turn my brain off and forget about everything else when I watch it."
    menu:
        "That's your thing":
            bree.say "Sounds like you love sports the same way I love videogames, Hanna."
            bree.say "It's something that doesn't demand anything from you, right?"
            bree.say "And it's yours too, nobody can take it away from you either."
            bree.say "I think everybody needs something like that."
            $ hanna.love += 1
        "You remind me of someone":
            bree.say "Urgh...you sound just like a guy, Hanna!"
            bree.say "In fact, you sound exactly like my Dad!"
            bree.say "He uses sports to cover up the fact he hasn't got a life!"
            bree.say "That and as an excuse to sit on his ass drinking beer!"
            $ hanna.love -= 1
        "Guys should like you":
            bree.say "I bet that makes you SO attractive to guys, Hanna!"
            bree.say "The ability to sit through a long, boring game without complaining."
            bree.say "That must be a dream come true for them!"
            $ hanna.sub += 1
        "You don't have issue with guys?":
            bree.say "But don't you find that guys hate girls that are into sport, Hanna?"
            bree.say "It's kind of like you're cutting in on their private realm."
            bree.say "I bet they secretly resent the fact you're into sports too..."
            $ hanna.sub -= 1
    return

label hanna_talk_fashion_female:
    hanna.say "It can be hard to keep up with fashion in my line of work, [hero.name]."
    hanna.say "You need to be wearing something fitted and stretchy all the time."
    hanna.say "And even when you're off work, you feel the need to wear something that shows off your body."
    hanna.say "Because it's kind of an advertisement when you're a fitness instructor, you know?"
    menu:
        "Sporty outfits suits you well":
            bree.say "I see what you mean, Hanna."
            bree.say "You can't just wear a baggy T-shirt and sweat-pants!"
            bree.say "Lucky for you that tight stuff never seems to go out of fashion."
            $ hanna.love += 1
        "Hum... Really?":
            bree.say "Ah, come off it, Hanna!"
            bree.say "You love wearing as little as you can get away with!"
            bree.say "I bet you'd walk around in a bikini if you could find an excuse."
            bree.say "Maybe even your underwear!"
            $ hanna.love -= 1
        "Even for a special person?":
            bree.say "I get where you're coming from, Hanna."
            bree.say "You just need to be sure you're doing it for the right person."
            bree.say "I mean, you wouldn't want your significant other to get the wrong idea."
            bree.say "Like you were trying to get attention from another girl or guy and not them, right?"
            $ hanna.sub += 1
        "Fashion's a pain in the ass":
            bree.say "This is the twenty-first century, Hanna!"
            bree.say "You should be able to wear whatever the hell you like."
            bree.say "And you don't need to justify it to anyone else."
            $ hanna.sub -= 1
    return

label hanna_talk_books_female:
    hanna.say "When you're a gym bunny, people always assume that you're dumb too, [hero.name]."
    hanna.say "Like some people even think that I don't read books - can you believe that?!?"
    hanna.say "I mean, sure, I don't read classic literature and that kind of stuff."
    hanna.say "But I love sports biographies and fitness magazines."
    menu:
        "As long as you enjoy your readings":
            bree.say "Urgh...people are so judgemental, Hanna!"
            bree.say "The important thing is that you're reading something."
            bree.say "You shouldn't have to read stuff you don't like to please them."
            bree.say "What would be the point in that?"
            $ hanna.love += 1
        "Did you ever try something else?":
            bree.say "It's great that you're reading something, Hanna."
            bree.say "But you might want to try getting out of your comfort zone, you know?"
            bree.say "Challenging yourself is a good thing."
            bree.say "It broadens your mind too."
            $ hanna.love -= 1
        "I understand":
            bree.say "You're never going to be able to please everybody, Hanna."
            bree.say "That's just a waste of time and effort."
            bree.say "Better to spend your time trying to please one person instead."
            bree.say "One person that's really special."
            $ hanna.sub += 1
        "Fuck them!":
            bree.say "That's great, Hanna!"
            bree.say "You know what you like and that's the end of it!"
            bree.say "You shouldn't change who you are to please other people."
            bree.say "They should appreciate you for who you are right now!"
            $ hanna.sub -= 1
    return

label hanna_talk_people_female:
    hanna.say "Urgh...I feel like I'm gonna burn-out, [hero.name]!"
    hanna.say "I spend SO much time smiling and being nice with the members at the gym."
    hanna.say "By the end of the day, I swear my face is aching from grinning at them!"
    hanna.say "But I guess that's just part of the job, right?"
    menu:
        "Let someone else dealing with members":
            bree.say "Oh no, Hanna...you can't think like that!"
            bree.say "I mean, I get that you're dealing with customers all the time."
            bree.say "But you need to cut yourself some slack."
            bree.say "Maybe spend some time working behind the scenes?"
            $ hanna.love += 1
        "You can quit!":
            bree.say "Well, nobody's forcing you to do the job, Hanna!"
            bree.say "You could always quit and get another one that's less client-facing."
            bree.say "Otherwise you're just flogging yourself the whole time!"
            bree.say "That and moaning about it for sympathy..."
            $ hanna.love -= 1
        "Ever try to slow down?":
            bree.say "I think you're overthinking it, Hanna."
            bree.say "Maybe if you lowered your expectations, you'd cope better?"
            bree.say "After all, nobody likes a complainer, do they?"
            $ hanna.sub += 1
        "React!!!":
            bree.say "I think you know that you have to make a change, Hanna."
            bree.say "You're just asking me for an excuse to do it!"
            bree.say "You need to stand up for yourself and make a change."
            bree.say "Take control of your own life!"
            $ hanna.sub += 1
    return

label hanna_talk_computers_female:
    hanna.say "I hate it when I have to do admin work at the gym, [hero.name]!"
    hanna.say "My thing is getting physical and helping people work-out."
    hanna.say "I'm just no good with sitting down and using a computer."
    hanna.say "And I swear the things always go wrong when I'm near them too!"
    menu:
        "I can help":
            bree.say "Don't feel bad, Hanna - not everyone's naturally good with technology."
            bree.say "But I'm sure you're better with computers than you think."
            bree.say "Maybe I could give you a few pointers?"
            bree.say "Would that help at all?"
            $ hanna.love += 1
        "Pitiful":
            bree.say "Oh come on, Hanna - computers are SO easy to use these days!"
            bree.say "It sounds to me like you're just scared of them or something."
            bree.say "Book yourself on a course for technophobes and sort yourself out."
            bree.say "Because computers aren't going away any time soon!"
            $ hanna.love -= 1
        "Everybody has a limit":
            bree.say "I kind of admire you for admitting that, Hanna."
            bree.say "Most modern women are always trying to do it all."
            bree.say "It's kind of refreshing to hear someone admit they have limits."
            $ hanna.sub += 1
        "Complaining doesn't suits you":
            bree.say "Wow...I never thought I'd hear you admit defeat, Hanna!"
            bree.say "Normally you seem like you could take on anything and win."
            bree.say "Are you sure that you're not selling yourself short there?"
            $ hanna.sub -= 1
    return

label hanna_talk_music_female:
    hanna.say "Music's really important to me, [hero.name]."
    hanna.say "I listen to it all the time when I'm working out."
    hanna.say "And we're always playing it at the gym."
    hanna.say "You know, pumping tunes to get your heart pumping too?"
    menu:
        "It looks like my playlist":
            bree.say "I know the exact kind of music you mean, Hanna!"
            bree.say "Stuff that makes you feel like you've got to move."
            bree.say "Almost like you don't have any choice!"
            $ hanna.love += 1
        "That's just noise":
            bree.say "That's not really music, Hanna!"
            bree.say "It's more like feedback with a beat!"
            bree.say "I don't know how you can listen to it."
            bree.say "You should try out some other stuff away from the gym."
            $ hanna.love -= 1
        "I also always listen the same songs":
            bree.say "It's good that you know what you like, Hanna."
            bree.say "That way you don't have to even think about it."
            bree.say "It's like the decisions already made."
            $ hanna.sub += 1
        "So, you're the gym DJ?":
            bree.say "You get to pick the music they play at the gym, right?"
            bree.say "I mean, it's like your choice of track?"
            bree.say "That must feel great - like you're in charge!"
            $ hanna.sub -= 1
    return

label hanna_talk_birthday_female:
    bree.say "Happy Birthday, Hanna!"
    bree.say "And many happy returns too!"
    hanna.say "Oh...thanks, [hero.name]!"
    hanna.say "I had no idea you knew it was today..."
    $ hanna.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
