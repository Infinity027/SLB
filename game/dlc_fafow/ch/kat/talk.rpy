label kat_talk_love_male:
    show kat
    kat.say "Do...do you believe in love, [hero.name]?"
    show kat shy blush
    kat.say "Oh dear - was that too forward of me?"
    kat.say "I just wanted to know what you think about it, that's all."
    show kat smile -blush
    kat.say "I'd like to think it's real, that it can exist."
    show kat shy
    kat.say "But I'm afraid that makes me sound so naive!"
    menu:
        "Indeed, being open to love is naive":
            show kat normal
            mike.say "Yeah, it kinda does, Kat!"
            mike.say "Makes you sound like one of those sappy girls."
            mike.say "The kind that have a bedroom full of soft-toys."
            mike.say "And are always waiting for their prince to come save them."
            show kat sad
            mike.say "You want to keep that talk about love to yourself!"
            $ kat.love -= 1
        "Being open to love is a worthy risk":
            mike.say "I don't think it makes you naive, Kat."
            show kat smile
            mike.say "You know, it takes a lot of courage to admit something like that."
            mike.say "More than it does to be cynical and claim love doesn't exist."
            mike.say "You just have to be careful who you admit as much too."
            mike.say "You should only ever open up to someone you can trust."
            $ kat.love += 1
        "Being open to love is dangerous":
            mike.say "You shouldn't have admitted that to me, Kat."
            mike.say "Because now I know one of your weaknesses."
            show kat blush
            mike.say "You're one of those romantic dreamers, aren't you?"
            mike.say "The kind that the world likes to crush!"
            mike.say "And you're going to have to be nice to me."
            mike.say "Or else I'll see to it that you do get crushed!"
            $ kat.sub += 1
    hide kat
    return

label kat_talk_love_female:
    show kat
    kat.say "Do...do you believe in love, [hero.name]?"
    show kat shy blush
    kat.say "Oh dear - was that too forward of me?"
    kat.say "I just wanted to know what you think about it, that's all."
    show kat smile -blush
    kat.say "I'd like to think it's real, that it can exist."
    show kat shy
    kat.say "But I'm afraid that makes me sound so naive!"
    menu:
        "Indeed, be open to love is naive":
            show kat normal
            bree.say "Yeah, it kinda does, Kat!"
            bree.say "Makes you sound like one of those sappy girls."
            bree.say "The kind that have a bedroom full of soft-toys."
            bree.say "And are always waiting for their prince to come save them."
            show kat sad
            bree.say "You want to keep that talk about love to yourself!"
            $ kat.love -= 1
        "Be open to love is a worthy risk":
            bree.say "I don't think it makes you naive, Kat."
            show kat smile
            bree.say "You know, it takes a lot of courage to admit something like that."
            bree.say "More than it does to be cynical and claim love doesn't exist."
            bree.say "You just have to be careful who you admit as much too."
            bree.say "You should only ever open up to someone you can trust."
            $ kat.love += 1
        "Be open to love is dangerous":
            bree.say "You shouldn't have admitted that to me, Kat."
            bree.say "Because now I know one of your weaknesses."
            show kat blush
            bree.say "You're one of those romantic dreamers, aren't you?"
            bree.say "The kind that the world likes to crush!"
            bree.say "And you're going to have to be nice to me."
            bree.say "Or else I'll see to it that you do get crushed!"
            $ kat.sub += 1
    hide kat
    return

label kat_talk_sex_male:
    show kat shy
    kat.say "I don't really feel comfortable talking to people about sex, [hero.name]."
    show kat normal
    kat.say "I'm not a prude, and I'm not scared of it - you have to believe me!"
    show kat shy
    kat.say "It's just...complicated."
    kat.say "I guess that's the best way to put it."
    show kat normal
    kat.say "Oh hell - I hope you understand what I'm trying to say?"
    menu:
        "Everybody has a secret garden":
            show kat smile
            mike.say "That's one of the things I love about you, Kat."
            mike.say "You're like, so mysterious!"
            mike.say "And don't worry - you don't have to tell me anything you don't want to."
            mike.say "It's kind of a thrill, you know?"
            mike.say "Like it gives you a power over me!"
            $ kat.sub -= 1
        "It is important to keep no secret":
            show kat sad
            mike.say "Yeah, I don't think I do, Kat."
            mike.say "I've had bad experiences in the past."
            mike.say "Been hurt when girls kept things from me."
            mike.say "Like, you can choose to tell me whatever you want, or not."
            mike.say "But don't ask me to trust you if you're not being honest with me!"
            $ kat.love -= 1
        "It take time to build thrust":
            show kat smile
            mike.say "I think so, Kat..."
            mike.say "Everyone's got things they can't quite put into words."
            mike.say "And you don't have to tell me everything about you all at once!"
            mike.say "Just take your time and think about it."
            mike.say "Explain those things to me when you're ready."
            $ kat.love += 1
    hide kat
    return

label kat_talk_sex_female:
    show kat shy
    kat.say "I don't really feel comfortable talking to people about sex, [hero.name]."
    show kat normal
    kat.say "I'm not a prude, and I'm not scared of it - you have to believe me!"
    show kat shy
    kat.say "It's just...complicated."
    kat.say "I guess that's the best way to put it."
    show kat normal
    kat.say "Oh hell - I hope you understand what I'm trying to say?"
    menu:
        "Everybody has a secret garden":
            show kat smile
            bree.say "That's one of the things I love about you, Kat."
            bree.say "You're like, so mysterious!"
            bree.say "And don't worry - you don't have to tell me anything you don't want to."
            bree.say "It's kind of a thrill, you know?"
            bree.say "Like it gives you a power over me!"
            $ kat.sub -= 1
        "It is important to keep no secret":
            show kat sad
            bree.say "Yeah, I don't think I do, Kat."
            bree.say "I've had bad experiences in the past."
            bree.say "Been hurt when girls kept things from me."
            bree.say "Like, you can choose to tell me whatever you want, or not."
            bree.say "But don't ask me to trust you if you're not being honest with me!"
            $ kat.love -= 1
        "It take time to build thrust":
            show kat smile
            bree.say "I think so, Kat..."
            bree.say "Everyone's got things they can't quite put into words."
            bree.say "And you don't have to tell me everything about you all at once!"
            bree.say "Just take your time and think about it."
            bree.say "Explain those things to me when you're ready."
            $ kat.love += 1
    hide kat
    return

label kat_talk_politics_male:
    show kat angry
    kat.say "I hate being so young sometimes."
    kat.say "People assume that you don't do stuff like politics."
    kat.say "But what do you expect when nobody's speaking up for us?"
    kat.say "You think any of those guys know what I want?"
    kat.say "You think they care about I think is important?!?"
    menu:
        "Don't be afraid to look for wiser people":
            show kat surprised
            mike.say "We both know that's not true, Kat."
            mike.say "Reality is you just don't understand all that stuff."
            mike.say "But you feel like you have to pretend, or you'll look dumb."
            show kat shy blush
            mike.say "Don't worry though, I won't let on."
            mike.say "Just so long as you're grateful..."
            $ kat.sub += 1
        "Personal opinion is important":
            mike.say "You certainly know your own mind, Kat!"
            show kat smile
            mike.say "And you get really passionate when you're stirred-up too!"
            mike.say "I think you should try telling someone in power how you feel."
            mike.say "It'd be like a breath of fresh air."
            mike.say "You know, really shake things up?"
            $ kat.love += 1
        "Criticism is easy":
            mike.say "Yeah, yeah, yeah..."
            mike.say "I've heard it all before, Kat!"
            mike.say "People like you are always whining about politics."
            mike.say "But next breath, you chicken out and say you won't engage!"
            mike.say "You need to either put up or shut up!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_politics_female:
    show kat angry
    kat.say "I hate being so young sometimes."
    kat.say "People assume that you don't do stuff like politics."
    kat.say "But what do you expect when nobody's speaking up for us?"
    kat.say "You think any of those guys know what I want?"
    kat.say "You think they care about I think is important?!?"
    menu:
        "Don't be afraid to look for wiser people":
            show kat surprised
            bree.say "We both know that's not true, Kat."
            bree.say "Reality is you just don't understand all that stuff."
            bree.say "But you feel like you have to pretend, or you'll look dumb."
            show kat shy blush
            bree.say "Don't worry though, I won't let on."
            bree.say "Just so long as you're grateful..."
            $ kat.sub += 1
        "Personal opinion is important":
            bree.say "You certainly know your own mind, Kat!"
            show kat smile
            bree.say "And you get really passionate when you're stirred-up too!"
            bree.say "I think you should try telling someone in power how you feel."
            bree.say "It'd be like a breath of fresh air."
            bree.say "You know, really shake things up?"
            $ kat.love += 1
        "Criticism is easy":
            bree.say "Yeah, yeah, yeah..."
            bree.say "I've heard it all before, Kat!"
            bree.say "People like you are always whining about politics."
            bree.say "But next breath, you chicken out and say you won't engage!"
            bree.say "You need to either put up or shut up!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_food_male:
    show kat angry
    kat.say "Urgh...I hate having to eat so much!"
    kat.say "Like, it takes so much time and effort."
    kat.say "Sometimes I just think, fuck it, you know?"
    kat.say "And I skip a meal, just don't eat at all."
    show kat normal
    kat.say "I wish there was a pill I could take."
    kat.say "Like a vitamin pill, but with a whole meal in it!"
    menu:
        "Not a bad idea":
            mike.say "I feel like that sometimes, Kat."
            show kat smile
            mike.say "It's a drag being a slave to your stomach!"
            mike.say "Maybe it'd help if you had someone to cook for you?"
            if hero.has_skill("cooking"):
                mike.say "I'm not bad in the kitchen, or so I'm told."
            mike.say "How about I whip you something up?"
            $ kat.love += 1
        "Let me cook for you":
            mike.say "Well, there's an obvious answer to that, Kat!"
            show kat smile
            mike.say "Let me cook for you, yeah?"
            mike.say "I'm pretty good in the kitchen."
            mike.say "And I can drop everything to whip you up a meal."
            mike.say "I'll even bring it over for you any time you like too!"
            $ kat.sub -= 1
        "No real meal is quite sad":
            mike.say "Yeah, that's explain why you're so pale."
            show kat sad
            mike.say "Maybe even why you sound so out of it sometimes too!"
            mike.say "You have to pull yourself together, Kat."
            mike.say "I mean, you already look like you could have Anorexia or something!"
            mike.say "And you can't pull off the heroin chic look either, trust me!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_food_female:
    show kat
    kat.say "Urgh...I hate having to eat so much!"
    kat.say "Like, it takes so much time and effort."
    kat.say "Sometimes I just think, fuck it, you know?"
    kat.say "And I skip a meal, just don't eat at all."
    kat.say "I wish there was a pill I could take."
    kat.say "Like a vitamin pill, but with a whole meal in it!"
    menu:
        "Not a bad idea":
            bree.say "I feel like that sometimes, Kat."
            show kat smile
            bree.say "It's a drag being a slave to your stomach!"
            bree.say "Maybe it'd help if you had someone to cook for you?"
            if hero.has_skill("cooking"):
                bree.say "I'm not bad in the kitchen, or so I'm told."
            bree.say "How about I whip you something up?"
            $ kat.love += 1
        "Let me cook for you":
            bree.say "Well, there's an obvious answer to that, Kat!"
            show kat smile
            bree.say "Let me cook for you, yeah?"
            bree.say "I'm pretty good in the kitchen."
            bree.say "And I can drop everything to whip you up a meal."
            bree.say "I'll even bring it over for you any time you like too!"
            $ kat.sub -= 1
        "No real meal is quite sad":
            bree.say "Yeah, that's explain why you're so pale."
            show kat sad
            bree.say "Maybe even why you sound so out of it sometimes too!"
            bree.say "You have to pull yourself together, Kat."
            bree.say "I mean, you already look like you could have Anorexia or something!"
            bree.say "And you can't pull off the heroin chic look either, trust me!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_travels_male:
    show kat
    kat.say "Right now, I never seem to get to travel anywhere."
    kat.say "It's like I only ever see other places in videogames."
    kat.say "I feel like that's gotta change."
    show kat smile
    kat.say "Like I need to start making memories."
    kat.say "And soon too!"
    menu:
        "Direct experiences are best":
            mike.say "You read my mind, Kat!"
            mike.say "I mean, you can even visit places using VR now."
            mike.say "But it doesn't really count."
            mike.say "Because you know it's not real!"
            mike.say "And if it's not real, why bother at all?"
            $ kat.love += 1
        "Real travels are less safe":
            show kat sad
            mike.say "I don't know about that, Kat."
            mike.say "I mean, you're pretty fragile, aren't you?"
            mike.say "And travelling all over the world is a challenge."
            mike.say "Would you really be up for it?"
            mike.say "Maybe you should just save up for a decent VR headset instead?"
            $ kat.love -= 1
        "Traveling alone is risky":
            show kat normal
            mike.say "Did you ever really think about what it takes, Kat?"
            mike.say "Travelling to far away places on your own?"
            mike.say "Places where you don't speak the language or get the culture?"
            show kat shy
            mike.say "There's so many girls like you that go missing out there too."
            mike.say "Hell, you'd need someone to protect you, someone like me..."
            $ kat.sub += 1
    hide kat
    return

label kat_talk_travels_female:
    show kat
    kat.say "Right now, I never seem to get to travel anywhere."
    kat.say "It's like I only ever see other places in videogames."
    kat.say "I feel like that's gotta change."
    show kat smile
    kat.say "Like I need to start making memories."
    kat.say "And soon too!"
    menu:
        "Direct experiences are best":
            bree.say "You read my mind, Kat!"
            bree.say "I mean, you can even visit places using VR now."
            bree.say "But it doesn't really count."
            bree.say "Because you know it's not real!"
            bree.say "And if it's not real, why bother at all?"
            $ kat.love += 1
        "Real travels are less safe":
            show kat sad
            bree.say "I don't know about that, Kat."
            bree.say "I mean, you're pretty fragile, aren't you?"
            bree.say "And travelling all over the world is a challenge."
            bree.say "Would you really be up for it?"
            bree.say "Maybe you should just save up for a decent VR headset instead?"
            $ kat.love -= 1
        "Traveling alone is risky":
            show kat normal
            bree.say "Did you ever really think about what it takes, Kat?"
            bree.say "Travelling to far away places on your own?"
            bree.say "Places where you don't speak the language or get the culture?"
            show kat shy
            bree.say "There's so many girls like you that go missing out there too."
            bree.say "Hell, you'd need someone to protect you, someone like me..."
            $ kat.sub += 1
    hide kat
    return

label kat_talk_tv_male:
    show kat
    kat.say "I never seem to watch TV like people used to, you know?"
    kat.say "I just binge something, watch it all in one go."
    kat.say "Or else I don't watch anything at all."
    kat.say "Weird, isn't it?"
    kat.say "How you used to have to tune in at a certain time to see stuff?"
    menu:
        "People have forgotten how to be patient":
            show kat sad
            mike.say "That's one of the things I really hate, Kat."
            mike.say "Everything's about instant gratification."
            mike.say "I think it makes people impatient and entitled."
            mike.say "And we don't appreciate stuff as much either."
            mike.say "Maybe things were better back then?"
            $ kat.love -= 1
        "Control and availability are hard to let go":
            show kat smile
            mike.say "Yeah, I know what you mean!"
            mike.say "I kind of remember it being like that when I was a kid."
            mike.say "But even them my folks had a VCR we used all the time."
            mike.say "Waiting for a time to see the next episode of something..."
            mike.say "I don't know if I could handle that!"
            $ kat.love += 1
        "I can't not do it in modern way":
            show kat smile
            mike.say "You're so right, Kat!"
            mike.say "I've tried to watch TV the old-fashioned way."
            mike.say "But I just can't resist the urge to know what happens next!"
            mike.say "I suppose that means I don't have much will-power!"
            mike.say "Not like you..."
            $ kat.sub -= 1
    hide kat
    return

label kat_talk_tv_female:
    show kat
    kat.say "I never seem to watch TV like people used to, you know?"
    kat.say "I just binge something, watch it all in one go."
    kat.say "Or else I don't watch anything at all."
    kat.say "Weird, isn't it?"
    kat.say "How you used to have to tune in at a certain time to see stuff?"
    menu:
        "People have forgotten how to be patient":
            show kat sad
            bree.say "That's one of the things I really hate, Kat."
            bree.say "Everything's about instant gratification."
            bree.say "I think it makes people impatient and entitled."
            bree.say "And we don't appreciate stuff as much either."
            bree.say "Maybe things were better back then?"
            $ kat.love -= 1
        "Control and availability are hard to let go":
            show kat smile
            bree.say "Yeah, I know what you mean!"
            bree.say "I kind of remember it being like that when I was a kid."
            bree.say "But even them my folks had a VCR we used all the time."
            bree.say "Waiting for a time to see the next episode of something..."
            bree.say "I don't know if I could handle that!"
            $ kat.love += 1
        "I can't not do it in modern way":
            show kat smile
            bree.say "You're so right, Kat!"
            bree.say "I've tried to watch TV the old-fashioned way."
            bree.say "But I just can't resist the urge to know what happens next!"
            bree.say "I suppose that means I don't have much will-power!"
            bree.say "Not like you..."
            $ kat.sub -= 1
    hide kat
    return

label kat_talk_sports_male:
    show kat smile
    kat.say "I just love the fact esports are getting more attention now."
    kat.say "Even some of the big news networks seem to be covering them."
    kat.say "The people that compete at those levels are pretty amazing."
    kat.say "And they've been ignored for too long!"
    kat.say "Don't you think, [hero.name]?"
    menu:
        "Reality is harsh":
            mike.say "You know, I always find gamers interesting, Kat."
            mike.say "They're all-powerful in their own little bubble."
            show kat surprised
            mike.say "But outside of it, they're utterly helpless!"
            mike.say "It's like they can't handle the real world."
            show kat shy
            mike.say "And they need someone to look after them..."
            $ kat.sub += 1
        "Esport is sport as well":
            show kat happy
            mike.say "I agree one hundred percent!"
            mike.say "Anyone that's at their level deserves to be recognised."
            mike.say "People have to stop assuming it's just people playing games."
            mike.say "Those guys and girls work so damn hard."
            mike.say "It way beyond time they got credit for that!"
            $ kat.love += 1
        "It is just a fad":
            show kat sad
            mike.say "Ah...I think it's just another fad."
            mike.say "The mainstream's always getting infatuated with nerd culture."
            mike.say "Comic-book movies one minute, video-games the next."
            mike.say "They'll move on as soon as the next thing comes along."
            mike.say "And after all, it is only people playing games!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_sports_female:
    show kat smile
    kat.say "I just love the fact esports are getting more attention now."
    kat.say "Even some of the big news networks seem to be covering them."
    kat.say "The people that compete at those levels are pretty amazing."
    kat.say "And they've been ignored for too long!"
    kat.say "Don't you think, [hero.name]?"
    menu:
        "Reality is harsh":
            bree.say "You know, I always find gamers interesting, Kat."
            bree.say "They're all-powerful in their own little bubble."
            show kat surprised
            bree.say "But outside of it, they're utterly helpless!"
            bree.say "It's like they can't handle the real world."
            show kat shy
            bree.say "And they need someone to look after them..."
            $ kat.sub += 1
        "Esport is sport as well":
            show kat happy
            bree.say "I agree one hundred percent!"
            bree.say "Anyone that's at their level deserves to be recognised."
            bree.say "People have to stop assuming it's just people playing games."
            bree.say "Those guys and girls work so damn hard."
            bree.say "It way beyond time they got credit for that!"
            $ kat.love += 1
        "It is just a fad":
            show kat sad
            bree.say "Ah...I think it's just another fad."
            bree.say "The mainstream's always getting infatuated with nerd culture."
            bree.say "Comic-book movies one minute, video-games the next."
            bree.say "They'll move on as soon as the next thing comes along."
            bree.say "And after all, it is only people playing games!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_fashion_male:
    show kat
    kat.say "Fashion's a weird thing when you're a geek."
    kat.say "People outside of the geek-sphere just don't get it."
    show kat smile
    kat.say "Like when you put all of your effort into getting a retro Space Wars T-shirt."
    kat.say "One that's based on the original screenplay and concept art."
    show kat angry
    kat.say "And they totally think it's the same as the one their kid-brother got from a chain-store!"
    menu:
        "Geek references can be tricky":
            show kat smile
            mike.say "Yeah, Kat - I totally hear you!"
            mike.say "I do the best I can to be tuned into that stuff."
            mike.say "But sometimes I worry that I don't get it."
            mike.say "Sounds like you do though."
            mike.say "Maybe you could show me how you manage it?"
            $ kat.sub -= 1
        "This is not serious stuff anyway":
            show kat surprised
            mike.say "Ah, you can get too wrapped up in all that stuff, Kat!"
            mike.say "Sometimes you need to take a step back."
            mike.say "Try to see that stuff like normal people do."
            show kat angry
            mike.say "I mean, after all..."
            mike.say "You wouldn't want people to know you're a nerd!"
            $ kat.love -= 1
        "Without passion how non-geeks could understand?":
            show kat normal
            mike.say "Non-geeks are never going to get it, Kat."
            mike.say "You know, I kind of feel sorry for them."
            mike.say "They think they get stuff like Space Wars."
            show kat smile
            mike.say "But they don't UNDERSTAND it!"
            mike.say "They don't get that it has a deep, spiritual meaning!"
            $ kat.love += 1
    hide kat
    return

label kat_talk_fashion_female:
    show kat
    kat.say "Fashion's a weird thing when you're a geek."
    kat.say "People outside of the geek-sphere just don't get it."
    show kat smile
    kat.say "Like when you put all of your effort into getting a retro Space Wars T-shirt."
    kat.say "One that's based on the original screenplay and concept art."
    show kat angry
    kat.say "And they totally think it's the same as the one their kid-brother got from a chain-store!"
    menu:
        "Geek references can be tricky":
            show kat smile
            bree.say "Yeah, Kat - I totally hear you!"
            bree.say "I do the best I can to be tuned into that stuff."
            bree.say "But sometimes I worry that I don't get it."
            bree.say "Sounds like you do though."
            bree.say "Maybe you could show me how you manage it?"
            $ kat.sub -= 1
        "This is not serious stuff anyway":
            show kat surprised
            bree.say "Ah, you can get too wrapped up in all that stuff, Kat!"
            bree.say "Sometimes you need to take a step back."
            bree.say "Try to see that stuff like normal people do."
            show kat angry
            bree.say "I mean, after all..."
            bree.say "You wouldn't want people to know you're a nerd!"
            $ kat.love -= 1
        "Without passion how non-geeks could understand?":
            show kat normal
            bree.say "Non-geeks are never going to get it, Kat."
            bree.say "You know, I kind of feel sorry for them."
            bree.say "They think they get stuff like Space Wars."
            show kat smile
            bree.say "But they don't UNDERSTAND it!"
            bree.say "They don't get that it has a deep, spiritual meaning!"
            $ kat.love += 1
    hide kat
    return

label kat_talk_books_male:
    show kat
    kat.say "People are always getting on at me to read more books."
    kat.say "Like I'm gonna get brain cancer or something if I don't!"
    kat.say "But I must, like, read so much more than they do online."
    kat.say "And the internet is SO much better for staying informed."
    kat.say "I mean, don't they say print is dead?!?"
    menu:
        "Distrust people deciding for you what's good or not":
            mike.say "Ah, don't listen to them, Kat!"
            mike.say "Those people are out of touch."
            show kat smile
            mike.say "They don't get how great the internet is for that kind of thing."
            mike.say "And most of them don't understand it either."
            mike.say "So they act all snobby to try to cover it up!"
            $ kat.love += 1
        "Books are challenging":
            show kat smile
            mike.say "Books are pretty intimidating, aren't they?"
            mike.say "Page after page of words, and no pictures in sight."
            mike.say "And even when you do manage to read one, it's not enough."
            mike.say "How do you even know that you understood what you read?"
            show kat shy
            mike.say "Better to leave all that stuff to me, Kat!"
            $ kat.sub += 1
        "Reading a book is a peculiar pleasure... Try again":
            mike.say "I kind of get what they mean, Kat."
            mike.say "The internet and games are great."
            mike.say "But there's nothing like getting lost in a good book!"
            mike.say "Somehow the words get into your head like nothing else."
            show kat sad
            mike.say "You really should try it some time."
            $ kat.love -= 1
    hide kat
    return

label kat_talk_books_female:
    show kat
    kat.say "People are always getting on at me to read more books."
    kat.say "Like I'm gonna get brain cancer or something if I don't!"
    kat.say "But I must, like, read so much more than they do online."
    kat.say "And the internet is SO much better for staying informed."
    kat.say "I mean, don't they say print is dead?!?"
    menu:
        "Distrust people deciding for you what's good or not":
            bree.say "Ah, don't listen to them, Kat!"
            bree.say "Those people are out of touch."
            show kat smile
            bree.say "They don't get how great the internet is for that kind of thing."
            bree.say "And most of them don't understand it either."
            bree.say "So they act all snobby to try to cover it up!"
            $ kat.love += 1
        "Books are challenging":
            show kat smile
            bree.say "Books are pretty intimidating, aren't they?"
            bree.say "Page after page of words, and no pictures in sight."
            bree.say "And even when you do manage to read one, it's not enough."
            bree.say "How do you even know that you understood what you read?"
            show kat shy
            bree.say "Better to leave all that stuff to me, Kat!"
            $ kat.sub += 1
        "Reading a book is a peculiar pleasure... Try again":
            bree.say "I kind of get what they mean, Kat."
            bree.say "The internet and games are great."
            bree.say "But there's nothing like getting lost in a good book!"
            bree.say "Somehow the words get into your head like nothing else."
            show kat sad
            bree.say "You really should try it some time."
            $ kat.love -= 1
    hide kat
    return

label kat_talk_people_male:
    show kat angry
    kat.say "People are always saying that I'm anti-social."
    kat.say "They accuse me of not having any social skills."
    show kat normal
    kat.say "But is that really a bad thing?"
    kat.say "I have skills in other things, lots of them."
    kat.say "What's so special about people skills anyway?"
    menu:
        "It doesn't matter":
            mike.say "You shouldn't be so worried about what other people think, Kat."
            mike.say "If someone's judging you like that, they're being unfair."
            show kat smile
            mike.say "Everyone's different, we all know that."
            mike.say "And we all have strengths and weaknesses."
            mike.say "Some of us appreciate your strengths too!"
            $ kat.love += 1
        "There is a minimum sociability to practice":
            show kat sad
            mike.say "You could try a little harder, Kat."
            mike.say "Sometimes I think you don't get out enough."
            mike.say "Smile every now and then."
            mike.say "Strike up a conversation."
            mike.say "And if you don't feel like it, then just pretend!"
            $ kat.love -= 1
        "You seems to me a lot more skilled than you think":
            show kat smile
            mike.say "I feel the same way, Kat."
            mike.say "And I think you're better at it than me!"
            mike.say "Sometimes I wish I didn't have to speak to anyone."
            mike.say "Oh, except you!"
            mike.say "I can always talk to you!"
            $ kat.sub -= 1
    hide kat
    return

label kat_talk_people_female:
    show kat angry
    kat.say "People are always saying that I'm anti-social."
    kat.say "They accuse me of not having any social skills."
    show kat normal
    kat.say "But is that really a bad thing?"
    kat.say "I have skills in other things, lots of them."
    kat.say "What's so special about people skills anyway?"
    menu:
        "It doesn't matter":
            bree.say "You shouldn't be so worried about what other people think, Kat."
            bree.say "If someone's judging you like that, they're being unfair."
            show kat smile
            bree.say "Everyone's different, we all know that."
            bree.say "And we all have strengths and weaknesses."
            bree.say "Some of us appreciate your strengths too!"
            $ kat.love += 1
        "There is a minimum sociability to practice":
            show kat sad
            bree.say "You could try a little harder, Kat."
            bree.say "Sometimes I think you don't get out enough."
            bree.say "Smile every now and then."
            bree.say "Strike up a conversation."
            bree.say "And if you don't feel like it, then just pretend!"
            $ kat.love -= 1
        "You seems to me a lot more skilled than you think":
            show kat smile
            bree.say "I feel the same way, Kat."
            bree.say "And I think you're better at it than me!"
            bree.say "Sometimes I wish I didn't have to speak to anyone."
            bree.say "Oh, except you!"
            bree.say "I can always talk to you!"
            $ kat.sub -= 1
    hide kat
    return

label kat_talk_computers_male:
    show kat
    kat.say "People should be more aware of computers."
    kat.say "And of the people that write the programs they use."
    kat.say "Computers run almost everything that's important."
    kat.say "Without them, everyone would be screwed."
    show kat angry
    kat.say "But to most people, it's just nerd stuff!"
    menu:
        "Trying to wake people is a waste of time":
            mike.say "Computers might be really important to you, Kat."
            mike.say "But you're never going to convince people to see it your way."
            mike.say "Most of them are too self-absorbed to care."
            mike.say "So you're wasting your time getting angry."
            mike.say "And my time telling me all about it!"
            $ kat.love -= 1
        "People need to understand the things that govern their lives":
            show kat smile
            mike.say "You're so right, Kat."
            mike.say "The modern world would just fall apart without them."
            mike.say "And everyone's got a computer of their own."
            mike.say "But they still don't understand them."
            mike.say "It'd be funny if it wasn't so maddening!"
            $ kat.love += 1
        "Don't care about them":
            mike.say "People like that are never going to agree with you, Kat."
            mike.say "Best just to forget about them."
            mike.say "In fact, why not avoid them completely?"
            show kat smile
            mike.say "I can handle the real world for you."
            mike.say "All you have to do is live inside your head..."
            $ kat.sub += 1
    hide kat
    return

label kat_talk_computers_female:
    show kat
    kat.say "People should be more aware of computers."
    kat.say "And of the people that write the programs they use."
    kat.say "Computers run almost everything that's important."
    kat.say "Without them, everyone would be screwed."
    show kat angry
    kat.say "But to most people, it's just nerd stuff!"
    menu:
        "Trying to wake people is a waste of time":
            bree.say "Computers might be really important to you, Kat."
            bree.say "But you're never going to convince people to see it your way."
            bree.say "Most of them are too self-absorbed to care."
            bree.say "So you're wasting your time getting angry."
            bree.say "And my time telling me all about it!"
            $ kat.love -= 1
        "People need to understand the things that govern their lives":
            show kat smile
            bree.say "You're so right, Kat."
            bree.say "The modern world would just fall apart without them."
            bree.say "And everyone's got a computer of their own."
            bree.say "But they still don't understand them."
            bree.say "It'd be funny if it wasn't so maddening!"
            $ kat.love += 1
        "Don't care about them":
            bree.say "People like that are never going to agree with you, Kat."
            bree.say "Best just to forget about them."
            bree.say "In fact, why not avoid them completely?"
            show kat smile
            bree.say "I can handle the real world for you."
            bree.say "All you have to do is live inside your head..."
            $ kat.sub += 1
    hide kat
    return

label kat_talk_music_male:
    show kat sad
    kat.say "I don't really care about the latest music, [hero.name]."
    kat.say "To me it just sounds like a load of garbage!"
    show kat smile
    kat.say "Now video-game sound-tracks, that's different."
    show kat happy
    kat.say "I can't get enough of those!"
    kat.say "They're like modern classical music!"
    menu:
        "Can you give some advice?":
            mike.say "I do like that kind of thing, Kat."
            mike.say "But it sounds like you know far more than me!"
            show kat smile
            mike.say "Can you bring me up to speed?"
            mike.say "You know, tell me what I need to be listening to?"
            mike.say "I trust your advice completely!"
            $ kat.sub -= 1
        "I like them too":
            show kat smile
            mike.say "You've got a point, Kat."
            mike.say "I still have tracks from video-games stuck in my head."
            mike.say "Even ones from when I was a kid!"
            show kat happy
            mike.say "They're criminally overlooked."
            mike.say "And that's not fair!"
            $ kat.love += 1
        "Really?":
            mike.say "Movie sound-tracks, maybe."
            mike.say "But video-games?"
            show kat surprised
            mike.say "You have to be kidding, Kat!"
            mike.say "It's all beeps and boops."
            show kat sad
            mike.say "That's not real music!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_music_female:
    show kat sad
    kat.say "I don't really care about the latest music, [hero.name]."
    kat.say "To me it just sounds like a load of garbage!"
    show kat smile
    kat.say "Now video-game sound-tracks, that's different."
    show kat happy
    kat.say "I can't get enough of those!"
    kat.say "They're like modern classical music!"
    menu:
        "Can you give some advice?":
            bree.say "I do like that kind of thing, Kat."
            bree.say "But it sounds like you know far more than me!"
            show kat smile
            bree.say "Can you bring me up to speed?"
            bree.say "You know, tell me what I need to be listening to?"
            bree.say "I trust your advice completely!"
            $ kat.sub -= 1
        "I like them too":
            show kat smile
            bree.say "You've got a point, Kat."
            bree.say "I still have tracks from video-games stuck in my head."
            bree.say "Even ones from when I was a kid!"
            show kat happy
            bree.say "They're criminally overlooked."
            bree.say "And that's not fair!"
            $ kat.love += 1
        "Really?":
            bree.say "Movie sound-tracks, maybe."
            bree.say "But video-games?"
            show kat surprised
            bree.say "You have to be kidding, Kat!"
            bree.say "It's all beeps and boops."
            show kat sad
            bree.say "That's not real music!"
            $ kat.love -= 1
    hide kat
    return

label kat_talk_birthday_male:
    show kat
    mike.say "Happy birthday, Kat!"
    mike.say "Hope you have a good one!"
    show kat surprised
    kat.say "You remembered my birthday?"
    show kat blush
    kat.say "Wow..."
    show kat happy
    $ kat.love += 5
    kat.say "No one remembers my birthday!"
    hide kat
    return

label kat_talk_birthday_female:
    show kat
    bree.say "Happy birthday, Kat!"
    bree.say "Hope you have a good one!"
    show kat surprised
    kat.say "You remembered my birthday?"
    show kat blush
    kat.say "Wow..."
    show kat happy
    $ kat.love += 5
    kat.say "No one remembers my birthday!"
    hide kat
    return

init:
    define nickname_gamer = ["Gamer", "gamer"]

    define nickname_player_two = ["Player Two", "player two"]

label command_nickname_kat:
    menu:

        "Call me Gamer" if active_girl.flags.mikeNickname not in nickname_gamer and active_girl.love > 50:
            $ active_girl.flags.mikeNickname = "Gamer"
        "Stop calling me Gamer" if active_girl.flags.mikeNickname in nickname_gamer:
            $ active_girl.flags.mikeNickname = None


        "Call me Player One" if active_girl.flags.mikeNickname not in nickname_player_one and active_girl.sub > 80:
            $ active_girl.flags.mikeNickname = "Player One"
        "Stop calling me Player One" if active_girl.flags.mikeNickname in nickname_player_one:
            $ active_girl.flags.mikeNickname = None


        "Call me Player Two" if active_girl.flags.mikeNickname not in nickname_player_two:
            $ active_girl.flags.mikeNickname = "Player Two"
        "Stop calling me Player Two" if active_girl.flags.mikeNickname in nickname_player_two:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
