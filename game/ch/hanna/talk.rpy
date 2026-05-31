label hanna_talk_love_male:
    show hanna
    hanna.say "You ever considered falling in love? What would your lover be?"
    menu:
        "You":
            mike.say "Well, I mean... I never really thought about it too much, until I met you."
            show hanna blush
            hanna.say "W... what? Me? [hero.name] wait, I... you're moving so fast!"
            $ hanna.love += 1
        "Someone else":
            mike.say "Oh yeah, I really think me and this one girl have a real strong connection. It could be the real thing."
            show hanna blush
            hanna.say "Y... you don't say, huh...? Well, she's really lucky."
            $ hanna.sub += 1
        "I don't need love":
            mike.say "Love? Ha. Don't need it."
            mike.say "We're nothing but mammals, and the only 'love' we need is the physical kind."
            mike.say "Know what I'm sayin'."
            hanna.say "Y... you really are a... a beast!"
            $ hanna.sub -= 1
        "Myself":
            mike.say "I've come to learn that you need to love yourself if you're going to love anyone else, and really, I think I love myself so much I don't need anyone else."
            show hanna annoyed
            hanna.say "Oh, well, I mean, you are... you are pretty great but... no one...?"
            $ hanna.love -= 1
    hide hanna
    return

label hanna_talk_sex_male:
    show hanna
    hanna.say "So, like, have you, um... ever had sex with someone before? What... do you like?"
    menu:
        "Love it":
            mike.say "Sex is great. Can't get enough of it! But sometimes, it's hard to find girls who'd want to do it, you know?"
            hanna.say "It's really difficult for you? Wow, I would have never guessed!"
            $ hanna.sub -= 1
        "Want You":
            mike.say "What? Are you asking? Because if you are, then the answer is yes!"
            show hanna blush
            hanna.say "What? Did I say I wanted to? I mean I don't think I did, not that I don't want to, oh geeze!"
            $ hanna.love += 1
        "I am a dom":
            mike.say "You bet. What I'm really looking for right now is to get my real domineering maleness out."
            mike.say "Unleash the beast and really just plow a girl, you know?"
            show hanna blush
            hanna.say "Aah... w... well...that's... something!"
            $ hanna.sub += 1
        "I am a sub":
            mike.say "What I really like is if the woman takes charge."
            mike.say "If she tells me what she wants, I'll listen to her."
            mike.say "Do whatever she asks of me. That's just pure bliss."
            hanna.say "S... so, you like domineering women, then... I see..."
            $ hanna.sub -= 1
    hide hanna
    return

label hanna_talk_politics_male:
    show hanna
    hanna.say "All the troubles out there in the world... I just want to improve myself, you know?"
    hanna.say "Not get tangled in this political mess."
    menu:
        "Agree":
            mike.say "I hear ya. Can't really do anything to the world if my own body is a flubby mess."
            hanna.say "Yeah, I know. But we're never done perfecting ourselves, are we?"
            hanna.say "That's what's so great! Not a care for the world around us, just our own desires."
            hanna.say "If everyone just tried to better themselves, then we'd all be happier!"
            $ hanna.love += 1
        "Disagree":
            mike.say "You can't just ignore everything going on in the world, Hanna."
            mike.say "Even if we spend our whole lives working out, we're still going to leave the world behind for other people to have to deal with."
            show hanna angry
            hanna.say "Well, I can't work out for other people, can I? They just have to work on fixing things themselves."
            $ hanna.love -= 1
        "Both":
            mike.say "Hanna, you know that by helping yourself, you can help others, too."
            hanna.say "Yeah? How do you figure?"
            mike.say "Well, I mean, you're really knowledgeable about personal fitness."
            mike.say "I know I wouldn't be hitting the gym as much if I thought I wouldn't see you."
            mike.say "There are issues about health and fitness in the political world, like getting kids to exercise and eat right."
            hanna.say "Hm...you know, maybe you're right."
            hanna.say "Maybe if I show off more and help spur people in to action."
            $ hanna.sub += 1
        "I don't know":
            mike.say "Yeah, I don't really know about that. I try not to think about it or anything too deep, I guess."
            hanna.say "We're nothing but animals, [hero.name], it's all about surviving."
            $ hanna.sub -= 1
    hide hanna
    return

label hanna_talk_food_male:
    show hanna
    hanna.say "Alright, [hero.name], here's a real test. What's your diet like?"
    menu:
        "Whatever":
            mike.say "Eh, I don't really care. Just eat whatever I want and exercise to keep the muscle up."
            hanna.say "Oh, come on! You can't maintain an amazing body by exercise alone!"
            hanna.say "You have to know what you're putting into your body before you can properly get it out!"
            $ hanna.sub -= 1
        "Junk Food":
            mike.say "Just get me the junkiest stuff you can find. Fast food, pizza, burgers, whatever!"
            hanna.say "Haha, I hear you there."
            hanna.say "But if you're ever taking me to a place to really pig out, then you HAVE to work out for HOURS afterwards."
            hanna.say "It's a great excuse to spend more time in the gym!"
            $ hanna.love -= 1
        "Healthy Eating":
            mike.say "I'm more of a seafood and salad type of guy."
            show hanna surprised
            hanna.say "What? ALL the time?"
            show hanna normal
            hanna.say "Come on, how are you supposed to work out if you're only eating 400 calories a day?"
            show hanna happy
            hanna.say "Food is great! We just have to make sure we earn it, first."
            $ hanna.love += 1
        "I'm a Vegan":
            mike.say "Actually, I'm Vegan."
            show hanna surprised
            hanna.say "Wut...?"
            $ hanna.sub += 1
    hide hanna
    return

label hanna_talk_travels_male:
    show hanna
    hanna.say "So, would you ever want to go anywhere?"
    menu:
        "Hiking trail":
            mike.say "Now that you mention it, getting fit for a hiking trail might be really fun."
            mike.say "Camping out, being in nature, showing off how well my body can handle the exertion."
            show hanna happy
            hanna.say "Hm... yeah, maybe that could be fun sometime!"
            $ hanna.love += 1
        "Different country":
            mike.say "Really, I just want to see the world. Take in some different culture, you know?"
            mike.say "Like maybe go to Italy and see the marble statues up close."
            hanna.say " Hm... I dunno. They may be good inspiration of the human body, but I think I'd make them jealous."
            $ hanna.sub += 1
        "Theme park":
            mike.say "There's this big theme park I've always wanted to see as a kid. All the funnel cake and rides? Sign me up!"
            show hanna annoyed
            hanna.say "Eh, you sit too much when you're on theme park rides."
            hanna.say "There's no thrill in sitting. My body's my best means of transportation!"
            $ hanna.love -= 1
        "Nope":
            mike.say "Nah. I like where I am. My own little world is great."
            hanna.say "Hm... I dunno. I think I'd like to test my skills sometime."
            hanna.say "Work up a REAL sweat out in the summer time somewhere nice and humid..."
            $ hanna.sub -= 1
    hide hanna
    return

label hanna_talk_tv_male:
    show hanna
    hanna.say "It's funny. I haven't really watched anything recently."
    hanna.say "Not that I don't care, but I'm in here most of the time, and I get 'in the zone' you know? What about you?"
    menu:
        "In the Zone":
            mike.say "Hm, yeah, I see what you mean. I'm so busy, I don't really watch a lot of stuff, either."
            show hanna happy
            hanna.say "Haha, yeah. There's lots of ways to entertain ourselves, aren't there?"
            $ hanna.love += 1
        "Soap Opera":
            mike.say "I just can't live without my stories. Will Alfonso propose to Lisa before she secretly marries his twin brother? I just have to find out!"
            show hanna annoyed
            hanna.say "The only kind of soap I care about is body wash, and even then, it's just to work up a good sweat from square one."
            $ hanna.love -= 1
        "Netflix and Chill":
            mike.say "I'm more of a binger than a schedule guy. Should come to my house sometime, we can chill."
            show hanna annoyed
            hanna.say "Chill? Sorry, [hero.name], I like it hot and humid!"
            $ hanna.love -= 1
        "Super Hero":
            mike.say "I'm really looking forward to the newest crossover on tonight."
            mike.say "Those super hero shows really know how to match the comics!"
            show hanna annoyed
            hanna.say " Ah, they are power fantasies for those who dont work hard to get their bodies in tip-top shape."
            $ hanna.love -= 1
    hide hanna
    return

label hanna_talk_sports_male:
    show hanna
    hanna.say "So, you training for any sports? Or do you just like watching some?"
    menu:
        "Nope.":
            mike.say "Nah, I'm more into just training to keep myself in shape."
            hanna.say "Huh, yeah, nothing wrong with that."
        "E-sports and speedrunning":
            mike.say "Well, I really like watching e-sports and speedrunning."
            show hanna annoyed
            hanna.say " Oh, please, you get more exercise from fapping than you do from clicking a mouse!"
            $ hanna.love -= 1
        "Running":
            mike.say "I'm actually looking to try one of those upcoming races."
            show hanna happy
            hanna.say "Oh, yeah? Those sound like fun!"
            $ hanna.love += 1
        "Sex":
            mike.say "Honestly, I'm just keeping my fitness up just so I can last longer in bed."
            show hanna blush
            hanna.say "Y... you want to... increase your endurance... for... for sex?"
            mike.say "Is that a problem?"
            hanna.say "N... no, but, it's not really a sport, even if its a good cause!"
            $ hanna.sub += 1
    hide hanna
    return

label hanna_talk_fashion_male:
    show hanna
    hanna.say "Honestly, I haven't thought about what to wear out to dates or stuff."
    hanna.say "What do you think would look good on me."
    menu:
        "Cute":
            mike.say "Maybe you should try on something cute? It would suit you quite nicely."
            show hanna surprised blush
            hanna.say "Cute? A girl like me being cute? Never really thought about it before..."
            $ hanna.love += 1
        "Slutty":
            mike.say "Might as well show yourself off. Be a total slut, and show off that body of yours."
            show hanna happy
            hanna.say "Hehe, you know what? Yeah? Let them see my guns and my pack!"
            $ hanna.sub += 1
        "Sweaty":
            mike.say "Whatever it is, you'd better have worked up a good sweat in it."
            show hanna blush
            hanna.say "You want me to work out and just meet you without showering? C... could you do the same?"
            $ hanna.love += 1
        "Nothing":
            mike.say "Ever consider wearing nothing at all?"
            show hanna annoyed
            hanna.say "Come on! Be serious if you're going to ask me somewhere."
            $ hanna.love -= 1
    hide hanna
    return

label hanna_talk_books_male:
    show hanna
    hanna.say " You know, I could take or leave books. Do you have anything in mind?"
    menu:
        "Fantasy":
            mike.say "Well, if you got a bunch of free time, there's a fantasy epic that's pretty big right now."
            mike.say "It's 100,000 pages long from Book one to book twel-"
            show hanna annoyed
            hanna.say "Ugh, no thanks! I can't sit still that long, and you can't run a treadmill and read a book at the same time."
            hanna.say "That's dangerous."
            $ hanna.love -= 1
        "Fitness":
            mike.say "Have you considered books on better fitness?"
            hanna.say "That could be pretty cool, I guess. Not that I don't already know everything there is to know."
            $ hanna.love += 1
        "Romance":
            mike.say "Have you considered trying out some romance novels."
            hanna.say "Not really my thing."
            hanna.say "I'm not exactly the kinda girl who gets off to those guys with open shirts sweeping me off my feet."
            hanna.say "I got more... particular tastes."
        "Comics":
            mike.say "Can't go wrong with comic books. There's this one series about a runner who-"
            hanna.say "Comics, hey yeah! I could look at the pictures and I wouldn't have to worry about wasting my time reading!"
            mike.say "That's not really how they work, you... nevermind."
    hide hanna
    return

label hanna_talk_people_male:
    show hanna
    hanna.say "So, what's it like being a 'people person'."
    menu:
        "Love people":
            mike.say "Well, if I wasn't so interested in meeting new people, I wouldn't have talked to you, would I?"
            mike.say "It's great to meet new people. Friends, lovers, whatever I can find."
            hanna.say "Hmm... you don't say...? Really don't want to take time from my exercise, though..."
        "Hate people":
            mike.say "I wouldn't know. I hate people in general. It's really only a small amount I care about."
            hanna.say "You don't say? Interesting."
        "Depends":
            mike.say "It really depends on the people I interact with. I can take people or leave people."
            mike.say "It's the most interesting people I seek out."
            show hanna happy
            hanna.say "Guess I should be thankful you find me interesting, then!"
            $ hanna.love += 1
        "How about you":
            mike.say "I'm more interested in why you don't consider yourself one."
            show hanna blush
            hanna.say "Ah, interested in me, are you? Eh, I like bodies, physicality, that raw power humans are capable of!"
            $ hanna.love += 1
    hide hanna
    return

label hanna_talk_computers_male:
    show hanna
    hanna.say "Ugh, I hate having to work the computer at work."
    hanna.say "It's just so confusing. Click this, type that."
    hanna.say "Wy can't we just... remember all this stuff? It's good brain exercise."
    menu:
        "Teach":
            mike.say "I could teach you sometime. I'm pretty good with computers."
            show hanna surprised blush
            hanna.say "Eh, I don't know. Is that really how you'd want to spend time with me? Really?"
            $ hanna.love += 1
        "Agree":
            mike.say "Yeah, computers are really getting in the way of real, physical interaction."
            hanna.say "You said it. All interaction should be physical. No exceptions."
        "Doubt":
            mike.say "Come on, you can't be THAT bad with computers."
            show hanna angry
            hanna.say "What, are you calling me a liar!?"
            $ hanna.love -= 1
    hide hanna
    return

label hanna_talk_music_male:
    show hanna
    hanna.say "So, what do you do during training? Listen to any songs or something?"
    menu:
        "No":
            mike.say "Would you believe I don't usually? It really breaks my focus, you know?"
            show hanna happy
            hanna.say "I see. Yeah, I wonder if I could hold out for as long as I do without anything to distract myself with. Usually, it's not stuff I listen to..."
            $ hanna.love += 1
        "Inspirational 80s media":
            mike.say "I have to blast the stuff from those old Underdog sports movies."
            mike.say "You know, the kinds of things that played in the 70s and 80s?"
            hanna.say "Wow, how old are you?"
        "Anime soundtracks":
            mike.say "The thumpin' beats of anime openings always get me in the mood."
            hanna.say "What's an anime...?"
        "Rock, metal":
            mike.say "Gotta go with rock and metal. Really gets the primal feelings out there."
            hanna.say "Hm... you need to take care of your body, including your ears, [hero.name]."
    hide hanna
    return

label hanna_talk_birthday_male:
    show hanna
    mike.say "Happy birthday Hanna."
    show hanna happy
    hanna.say "Thank you [hero.name]."
    $ hanna.love += 1
    hide hanna
    return

init:
    define nickname_champ = ["Champ", "champ"]
    define nickname_partner = ["Partner", "partner"]

label command_nickname_hanna:
    menu:

        "Call me Champ" if active_girl.flags.mikeNickname not in nickname_champ and hero.fitness > 80:
            $ active_girl.flags.mikeNickname = "Champ"
        "Stop calling me Champ" if active_girl.flags.mikeNickname in nickname_champ:
            $ active_girl.flags.mikeNickname = None


        "Call me Partner" if active_girl.flags.mikeNickname not in nickname_partner and active_girl.status in ["girlfriend"]:
            $ active_girl.flags.mikeNickname = "Partner"
        "Stop calling me Partner" if active_girl.flags.mikeNickname in nickname_partner:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_hanna_male:
    mike.say "Ah, Hanna..."
    show hanna talkative
    hanna.say "Yeah, [hero.name]?"
    show hanna normal
    mike.say "You know when you say hi to me?"
    mike.say "I was wondering if you could say something else instead?"
    show hanna talkative
    hanna.say "Like what, exactly?"
    show hanna normal
    mike.say "I was thinking something like how much you like to show off."
    mike.say "Maybe like you want me to show you off in public?"
    if hanna.sub >= 70 or hanna.is_sex_slave:
        show hanna talkative blush
        hanna.say "I...I do kinda like people to have their eyes on me."
        hanna.say "That sounds a pretty good idea."
        show hanna happy
        hanna.say "Okay - I'll do it!"
        $ hanna.flags.submissive_interact = True
    else:
        show hanna whining
        hanna.say "I like to look good, [hero.name]."
        hanna.say "But I'm not some dog you can show off!"
        show hanna annoyed
        mike.say "Of course not, Hanna!"
        mike.say "Just forget about it, okay?"
        $ hanna.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
