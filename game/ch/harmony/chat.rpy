label harmony_desire_0_male:
    harmony.say "Hey, [hero.name] - how did you like Bible study this week?"
    harmony.say "I'd love to know what you got out of it!"
    menu:
        "I liked it" if hero.fun >= 3:
            mike.say "To be honest, Harmony, I was pretty amazed."
            mike.say "There was a lot of stuff we covered that really made sense to me!"
            if harmony.purity >= HP:
                $ harmony.love += 1
            elif harmony.purity < LP:
                $ harmony.love -= 1
        "I hated it":
            mike.say "Ah, I tried, Harmony - honestly I did."
            mike.say "But none of it really meant anything to me."
            if harmony.purity >= HP:
                $ harmony.love -= 1
            elif harmony.purity < LP:
                $ harmony.love += 1
    return

label harmony_desire_1_male:
    if harmony.purity >= VHP:
        harmony.say "I have to say, [hero.name], I'm really impressed that you're keeping up the Bible study."
        menu:
            "Me too" if hero.fun >= 3:
                mike.say "Thanks, Harmony - and thanks for turning me on to it too."
                mike.say "I'm getting so much more out of it than I ever thought possible!"
                $ harmony.love += 1
            "I am not that interested":
                mike.say "Yeah, I don't know about that."
                mike.say "I'm just not sure that it makes any sense to me."
                $ harmony.love -= 1
    else:
        harmony.say "I'm so glad that we can just chat to one another, [hero.name]."
        harmony.say "I used to think I needed a reason to talk to a guy."
        harmony.say "Like it was a sin if we weren't talking about Jesus or something!"
        menu:
            "I like you too" if hero.fun >= 3:
                mike.say "It's a shame that you took so long to come round to thinking that, Harmony."
                mike.say "Because you're a lot of fun to talk to."
                $ harmony.love += 1
            "You should work on your small talk":
                mike.say "I hear you, Harmony, I do."
                mike.say "But your conversational skills need a bit of work!"
                $ harmony.love -= 1
    return

label harmony_desire_2_male:
    if harmony.purity >= VHP:
        harmony.say "It's so great to see you at church on a Sunday, [hero.name]!"
        menu:
            "I agree" if hero.fun >= 3:
                mike.say "It's great to be there, Harmony."
                mike.say "I used to just go out of habit."
                mike.say "But you've helped me to get so much more out of it!"
                $ harmony.love += 1
            "I disagree":
                mike.say "It's great to see you, Harmony."
                mike.say "But I'm just paying lip-service to the whole religion thing these days."
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "I'm really feeling like we're getting closer, [hero.name]."
        harmony.say "You know - like we're becoming good friends?"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I do know what you mean, Harmony."
                mike.say "I really look forward to seeing you, to us spending time together."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "That's cute, Harmony."
                mike.say "But I feel like we hardly even know each other."
                $ harmony.love -= 1
    else:
        harmony.say "I used to like seeing you at church on a Sunday, [hero.name]."
        harmony.say "But now, I feel kind of guilty to admit this..."
        harmony.say "I almost come to church just to be able to see you!"
        $ harmony.love += 1
    return

label harmony_desire_3_male:
    if harmony.purity >= VHP:
        harmony.say "Oh, [hero.name], I'm so proud of you."
        harmony.say "You've committed yourself to walking the path of salvation."
        harmony.say "You really are going to save your soul, I just know it!"
        menu:
            "I agree" if hero.fun >= 3:
                mike.say "I feel so much better since I gave myself to Jesus - mind, body and soul."
                mike.say "But I couldn't have done any of it without you, Harmony!"
                $ harmony.love += 1
            "I disagree":
                mike.say "I think you're just seeing what you want to see, Harmony."
                mike.say "I don't feel any different now to how I did before."
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "Don't take this the wrong way, [hero.name]."
        harmony.say "But I feel like I'm so much closer to you now than when we first met."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "Me too Harmony, me too."
                mike.say "It's like there's a special connection between us, or something."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "That's cute, Harmony."
                mike.say "But I feel like we hardly even know each other."
                $ harmony.love -= 1
    elif harmony.purity < LP:
        harmony.say "We're always talking about exploring new things together, [hero.name]."
        harmony.say "So I was wondering if I could be one of those things too?"
        menu:
            "Flirt" if hero.fun >= 3:
                mike.say "I'd love to explore you, Harmony."
                mike.say "I'm just worried that I'd get lost and never want to be found again!"
                $ harmony.love += 1
            "Blow her off":
                mike.say "Yeah, maybe not, Harmony."
                mike.say "There are probably some things that should stay a mystery."
                mike.say "And for good reason!"
                $ harmony.love -= 1
    else:
        harmony.say "This is going to sound really cheesy, [hero.name]."
        harmony.say "But I feel like meeting you opened up a whole new world of experiences for me!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "It's been just as much fun for me to show all of those things to you."
                mike.say "You made them feel brand new, Harmony."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "That's great for you, Harmony."
                mike.say "But all I got to do was the same old shit!"
                $ harmony.love -= 1
    return

label harmony_desire_4_male:
    if harmony.purity >= VHP:
        harmony.say "Oh, [hero.name], I have something wonderful to tell you!"
        harmony.say "I was reading the Bible last night, trying to make sense of my feelings for you."
        harmony.say "And I suddenly realised that I love you, in the most pure and sacred way possible!"
        menu:
            "Me too" if hero.fun >= 3:
                mike.say "Oh, Harmony - I feel the same way."
                mike.say "And if the Bible tells us that our love is sanctified by God, who am I to disagree!"
                $ harmony.love += 1
            "Not me":
                mike.say "For heaven's sake, Harmony - that book was written by savages in the stone age."
                mike.say "People have been using it to back up their bullshit for centuries!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "Ah, [hero.name]...I...I don't know how to say this..."
        harmony.say "But I...I think that I'm falling in love with you!"
        menu:
            "I am touched" if hero.fun >= 3:
                mike.say "Wow, Harmony - now I don't know what to say back!"
                mike.say "I kind of feel the same way about you, too."
                $ harmony.love += 1
            "I am irritated":
                mike.say "Well, are you or aren't you, Harmony?"
                mike.say "Because this is the kind of thing that you really need to be sure about!"
                $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "I just love it when you fuck me, [hero.name]."
        harmony.say "But I like it SO much more when you're rough with me!"
        menu:
            "It's your own fault" if hero.fun >= 3:
                mike.say "It's your cute curves, Harmony."
                mike.say "They make me want to conquer you."
                mike.say "To plant my flag as deep into you as I can!"
                $ harmony.sub += 1
            "you are a slut":
                mike.say "Really, Harmony?"
                mike.say "Lately it feels like that's all you can think about."
                $ harmony.sub -= 1
    elif harmony.purity < LP:
        harmony.say "I just wanted to say that..."
        harmony.say "That I love..."
        harmony.say "I love having sex with you, [hero.name]!"
        menu:
            "I love it too" if hero.fun >= 3:
                mike.say "That makes two of us, Harmony."
                mike.say "You're a hell of a lot of fun in that department too!"
                $ harmony.love += 1
            "You are a slut":
                mike.say "Everything can't just be about sex, Harmony!"
                $ harmony.love -= 1
    else:
        harmony.say "I've been feeling like this for a while now, [hero.name]."
        harmony.say "But I wanted to be sure before I said anything."
        harmony.say "So here goes - I...I love you!"
        menu:
            "I am touched" if hero.fun >= 3:
                mike.say "You do?!?"
                mike.say "Harmony - I love you too!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Well, that just made things awkward, Harmony."
                mike.say "Because I can't say that I feel the same way about you!"
                $ harmony.love -= 1
    return

label harmony_desire_5_male:
    if harmony.purity >= VHP:
        harmony.say "I've thought about this long and hard, [hero.name]."
        harmony.say "I've read my Bible and prayed too."
        harmony.say "And now I'm sure that you're my one and only true soulmate!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I feel the exact same way about you too, Harmony."
                mike.say "It's like God made us just so that we could find each other!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "You're crazy, Harmony."
                mike.say "And worst of all, you're just using the word of God to back you up!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "[hero.name], please don't be scared - but I have something I need to tell you."
        harmony.say "This might sound sudden, but I think that you just might be the one for me..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "No, Harmony...it's okay."
                mike.say "I think that I've been feeling the same way about you as well."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "I know it must have been hard for you to admit that, Harmony."
                mike.say "But I have to be honest too."
                mike.say "I don't think we've known each other long enough to be sure of just how we feel yet."
                $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "I'm in love, [hero.name] - and I can't live without it!"
        harmony.say "I'm head over heels in love with your cock!"
        harmony.say "I only feel complete when I have it inside of me!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "Your pussy's got me feeling the same way, Harmony!"
                mike.say "All it wants is to get hard and then get into you!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Jesus Fucking Christ, Harmony - I'm a human being, not a piece of meat!"
                mike.say "When did you turn into such a cock-hungry whore?!?"
                $ harmony.love -= 1
    elif harmony.purity < LP:
        harmony.say "I think that I love you, [hero.name]."
        harmony.say "But I KNOW that I love it when you make love to me!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "We've got the best of both worlds, Harmony."
                mike.say "We love each other, and we love to love each other too!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Huh...it's fun to be with you, Harmony."
                mike.say "But sometimes I'm not sure if you love me or just the sex..."
                $ harmony.love -= 1
    else:
        harmony.say "I feel like I can be straight up and honest with you, [hero.name]."
        harmony.say "So I'll just come out and say it - I think that I want to spend the rest of my life with you..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "You can, Harmony - on both counts."
                mike.say "I want to spend my life with you as well."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "I appreciate your honesty, Harmony."
                mike.say "And so I'll be just as honest in return."
                mike.say "You might well feel that way about me, but I'm just not there yet when it comes to you."
                $ harmony.love -= 1
    return

label harmony_love_0_male:
    harmony.say "Tell me, [hero.name] - what do you think about God?"
    menu:
        "I believe in god":
            mike.say "I believe in God - but I don't feel like I have a personal relationship with him."
            $ harmony.love += 1
        "I don't know":
            mike.say "Honestly, I don't know whether I believe in God or not..."
        "I don't believe in god":
            mike.say "Sure, I sing along in church and all that, but I think that God's probably just made up."
            $ harmony.love -= 1
    return

label harmony_love_1_male:
    if harmony.purity >= VHP:
        harmony.say "You know, [hero.name], it'd be great to see you at church EVERY Sunday."
        menu:
            "Agree" if hero.fun >= 3:
                mike.say "Well, I have been getting a lot out of it when I come along."
                mike.say "Maybe I should start making the effort to do just that."
                $ harmony.love += 1
            "Disagree":
                mike.say "I don't know about that, Harmony."
                mike.say "My life's pretty hectic as it is right now."
                mike.say "The last thing I need is more hassle."
                $ harmony.love -= 1
    else:
        harmony.say "You know, I used to want to see more of you in church."
        harmony.say "But more and more recently, I just feel happy to see more of you wherever!"
        menu:
            "Agree" if hero.fun >= 3:
                mike.say "I know just what you mean, Harmony."
                mike.say "It was like when I went to Church and you weren't there, I really wasn't interested at all!"
                $ harmony.love += 1
            "Disagree":
                mike.say "Wow, Harmony, just wow!"
                mike.say "You make it sound like you just went to church to pick up guys..."
                $ harmony.love -= 1
    return

label harmony_love_2_male:
    if harmony.purity >= VHP:
        harmony.say "It's great seeing you at church and for Bible study, [hero.name]."
        harmony.say "But do you ever think about us spending time together doing, I don't know...something else?"
        menu:
            "I would like that" if hero.fun >= 3:
                mike.say "I do love the time that we spend together, Harmony."
                mike.say "But I'd be lying if I said that my mind was always on Jesus when we are."
                mike.say "It makes me feel guilty to admit it, but sometimes I'm thinking about doing other things...with you!"
                $ harmony.love += 1
            "No":
                mike.say "Harmony, you should be ashamed of yourself!"
                mike.say "Here I was all this time, thinking that you were contemplating God."
                mike.say "When in reality, you were allowing yourself to be tempted!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "So you ever think we could spend time together outside of church, [hero.name]?"
        harmony.say "Like, I don't know, maybe go out for a meal at a nice restaurant?"
        menu:
            "That would be nice" if hero.fun >= 3:
                mike.say "You're right, Harmony - I can't believe I didn't think that myself!"
                mike.say "I'd love to get to know more about you, beside what I can learn in church..."
                $ harmony.love += 1
            "Tell her she should not eat that much":
                mike.say "Of all the things you could have suggested, you came up with a meal in a restaurant?"
                mike.say "I think the LAST thing that you need is feeding up, Harmony!"
                $ harmony.love -= 1
    else:
        harmony.say "I'd like to maybe do some things that normal people do, [hero.name]."
        harmony.say "You know, maybe you could take me to the beach some time soon?"
        menu:
            "Agree" if hero.fun >= 3:
                mike.say "That sounds like a great idea, Harmony!"
                mike.say "I'm sure you look amazing in a swimsuit..."
                $ harmony.love += 1
            "Tell her she's too fat":
                mike.say "Really, the beach?!?"
                mike.say "Aren't you afraid of being mistaken for a beached whale and rolled back into the sea?"
                $ harmony.love -= 1
    return

label harmony_love_3_male:
    if harmony.purity >= VHP:
        harmony.say "[hero.name], I really feel like I want to know you better."
        harmony.say "Like I want to get to know your soul..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I feel exactly the same way, Harmony."
                mike.say "If we know each other's souls, then there's nothing we don't know about each other!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Geez, Harmony - I'm not sure I'm comfortable with anyone knowing me that deeply."
                mike.say "Not even myself!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "You know [hero.name], I feel like I'd like to get to know you better."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I know what you mean, Harmony."
                mike.say "It feels like we spend so much time together and yet never actually talk about ourselves."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Why does everyone have to be like that these days, always wanting to break down boundaries and share?"
                mike.say "Life's so much easier when we keep things in neat little boxes!"
                $ harmony.love -= 1
    elif harmony.purity < LP:
        harmony.say "You know what, [hero.name] - I think that we need to get to know each other better."
        harmony.say "Specifically, I think that we should get to know each other in the most literal sense possible..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "Wow, Harmony - I've been waiting to hear you say that for so long!"
                mike.say "I want to know every single inch of your body..."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Ah...that's a tempting offer, Harmony."
                mike.say "But there's just so much of you to explore - I'm afraid it would take an entire lifetime!"
                $ harmony.love -= 1
    else:
        harmony.say "I think it'd be a good thing for us to get to know each other better."
        harmony.say "Really find out what we have in common..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "You're right, we should do just that."
                mike.say "I feel like we've come so far that we owe it to ourselves, as friends."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "I think we have a pretty decent relationship right now, Harmony."
                mike.say "Are you sure you want to jeopardise that by sharing all of our deepest, darkest secrets?"
                $ harmony.love -= 1
    return

label harmony_love_4_male:
    if harmony.purity >= VHP:
        harmony.say "I have to say, [hero.name] - I've never really met anyone like you."
        harmony.say "And I'm so happy to know that I've helped to bring you into God's hands too!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I couldn't have done any of it without you, Harmony."
                mike.say "I was truly a lost sheep, until you came along and found me!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Huh...it kind of feels like you're trying to take credit for me finding God, Harmony!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "I feel like something out of a cheap movie even thinking this, but it's true all the same."
        harmony.say "I don't think I've ever met someone quite like you, [hero.name]..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I guess sometimes the Hollywood cliches are true, Harmony."
                mike.say "Because I feel the same way about you!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "I think this movie has an unexpected twist in it, Harmony."
                mike.say "Because I just don't feel the same way!"
                $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "Oh god, but I love it when you fuck me, [hero.name]!"
        harmony.say "I can't think straight when you're inside of me."
        harmony.say "And when you're not, all I can think about is the next time you will be!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "And you think that I can keep my mind on anything else when I'm not fucking you?"
                mike.say "The only thing better than the memory of being in you is actually being in you!"
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "To be honest, Harmony, I can't actually remember what it feels like when we fuck."
                mike.say "I spend most of the time terrified that you're going to roll over and crush me to death!"
                $ harmony.love -= 1
    elif harmony.purity < LP:
        harmony.say "I kind of feel bad saying this, [hero.name]."
        harmony.say "But I'm SO happy to be your girlfriend!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I guess that's because you make me feel the same way, Harmony!"
                mike.say "I feel lucky every time I remember you're mine."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Well, I guess that's only natural, Harmony."
                mike.say "You really should be grateful that you've got a guy the likes of me!"
                $ harmony.love -= 1
    else:
        harmony.say "Did I ever tell you how happy I am we became more than just good friends?"
        harmony.say "I'm so glad that I can call you my boyfriend, [hero.name]!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "You were a great friend, Harmony."
                mike.say "But you're an even better girlfriend."
                $ harmony.love += 1
            "I don't feel the same":
                mike.say "Yeah, I know..."
                mike.say "But we really had some great times when we were just friends!"
                $ harmony.love -= 1
    return

label harmony_love_5_male:
    if harmony.purity >= VHP:
        harmony.say "I feel like I know you, [hero.name] - body, mind and soul."
        harmony.say "If you were to propose to me one day, I think I'd be inclined to say yes!"
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "Oh, Harmony!"
                mike.say "God willing, that day will not be too long in coming!"
                $ harmony.love += 1
            "[hero.name] tells Harmony that he does not feel the same way":
                mike.say "Yeah, well...I wouldn't go holding your breath!"
                $ harmony.love -= 1
    elif harmony.purity >= HP:
        harmony.say "I think you're great father material, [hero.name]."
        harmony.say "It'd be wonderful to start a family with you when the time comes..."
        menu:
            "I feel the same" if hero.fun >= 3:
                mike.say "I really hope that time isn't long in coming around, Harmony."
                $ harmony.love += 1
            "[hero.name] tells Harmony that he does not feel the same way":
                mike.say "Ah...you might find that time's actually in the middle of a month of Sundays!"
                $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "Ah, fuck it, [hero.name] - I can't deny it any longer."
        harmony.say "All I want is to be your fuck-toy!"
        harmony.say "I want you to use me - whenever, wherever and however you please!"
        menu:
            "Agree" if hero.fun >= 3:
                mike.say "If that's the way you want it, Harmony..."
                mike.say "And I have a whole head full of ideas as to how to use you!"
                $ harmony.love += 1
            "Be disgusted":
                mike.say "Urgh...you really have sunk to a new low, haven't you?"
                mike.say "Just what happened to turn you into this much of a degenerate slut?"
                $ harmony.love -= 1
    elif harmony.purity < LP:
        harmony.say "I think we're ready to take the next step in our relationship, [hero.name]."
        harmony.say "What do you say to the idea of us moving in together?"
        menu:
            "Good idea" if hero.fun >= 3:
                mike.say "I love it, Harmony!"
                mike.say "How soon can you have your things packed?"
                $ harmony.love += 1
            "No":
                mike.say "I'm not sure I'm ready for that, Harmony."
                mike.say "I just don't know if my bed could cope."
                mike.say "Or the floorboards!"
                $ harmony.love -= 1
    else:
        harmony.say "I think that we make a pretty good partnership, [hero.name]."
        harmony.say "How about we make it official and go steady?"
        menu:
            "I'd love to" if hero.fun >= 3:
                mike.say "I feel like we already are, Harmony!"
                mike.say "So why not."
                $ harmony.love += 1
            "No":
                mike.say "Ah, I don't know about that, Harmony..."
                mike.say "Sounds like if we did that, we'd be gathering momentum."
                mike.say "And I'm afraid that I'll end up getting squashed - if you know what I mean?"
                $ harmony.love -= 1
    return

label harmony_good_sweet_talk_male:
    show harmony
    if harmony.love > 133:
        mike.say "You're so HOT, Harmony!"
        mike.say "I can't help thinking about what I want to do to you next!"
        show harmony blush
        harmony.say "Sssh...somebody might hear you!"
        harmony.say "Whisper it to me, before I blush as red as a tomato!"
    elif harmony.love > 66:
        mike.say "I love the way you look, Harmony."
        mike.say "It shows off just how beautiful your figure really is."
        show harmony happy
        harmony.say "I...I shouldn't be proud or wanton, I know that."
        harmony.say "But it does make me happy to hear you say that!"
    else:
        mike.say "It's great to get to spend time with you away from church, Harmony."
        mike.say "It means I can get to know the real you."
        harmony.say "Aw, thank you!"
        harmony.say "I value your friendship too."
    hide harmony
    return

label harmony_bad_sweet_talk_male:
    show harmony
    mike.say "I knew you never believed in any of that religious stuff, Harmony."
    mike.say "Not really!"
    show harmony angry
    harmony.say "Hey!"
    harmony.say "Are you calling me some kind of hypocrite?"
    harmony.say "A liar?!?"
    mike.say "Ah, no...not exactly!"
    hide harmony
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
