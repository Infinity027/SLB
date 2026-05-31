label angela_desire_0_female:
    angela.say "I know that I'm supposed to be a older and wiser than you guys."
    angela.say "But so much of what I used to take for granted was fake memories."
    angela.say "Even when it comes to stuff in...well, in the bedroom!"
    menu:
        "It's so weird":
            bree.say "Eww, Angela - this is SO weird!"
            bree.say "You're still [mike.name]'s mom to me."
            bree.say "And you're freaking me out!"
            $ angela.love -= 1
        "That must be hard":
            bree.say "That must be hard on you, Angela."
            bree.say "I can't imagine what it must be like."
            bree.say "But I'll do anything I can to help."
            bree.say "All you have to do is ask - even about stuff in the bedroom!"
            $ angela.love += 1
        "Don't worry":
            bree.say "Don't you worry about that, Angela."
            bree.say "I can be the big sister when it comes to things like that."
            bree.say "I can teach you so much stuff about the bedroom."
            bree.say "And every other room around the house too!"
            $ angela.sub += 1
    return

label angela_desire_1_female:
    angela.say "I feel like I'm starting all over again, [hero.name]!"
    angela.say "Like I'm back in my teens or early twenties."
    angela.say "My social life is all about meeting new people and dating."
    menu:
        "I understand you're lost":
            bree.say "I guess it makes sense that you don't know what to do with yourself, Angela."
            bree.say "I mean, you had [mike.name]'s dad controlling you for most of your life, right?"
            bree.say "You're probably just looking for somebody else to take his place."
            bree.say "You know, rather than be in control of your own life for once?"
            $ angela.sub -= 1
        "I know what you mean":
            bree.say "I know exactly what you mean, Angela."
            bree.say "And I hope you're having a good time with all that."
            bree.say "Because I'm loving the fact I can hang out with you."
            bree.say "It's like I've found a totally new friend!"
            $ angela.love += 1
        "You're not a teenager anymore":
            bree.say "Yeah, well you're not pulling off the look of a teenager, Angela!"
            bree.say "And you want to be careful acting like one too."
            bree.say "Trust me - the last thing anyone wants to see is a grown woman acting like a little girl!"
            $ angela.love -= 1
    return

label angela_desire_2_female:
    angela.say "I think I'm starting to like being single again, [hero.name]."
    angela.say "At first I was really embarrassed when I caught guys checking me out."
    angela.say "But I guess that was just because I'm so used to being married."
    angela.say "Now it's really starting to make me feel good about myself!"
    menu:
        "That's great":
            bree.say "That's great news, Angela!"
            bree.say "And you shouldn't be ashamed of it either."
            bree.say "You're mature in the best possible way."
            bree.say "Like a fine wine, you know?"
            $ angela.love += 1
        "Guys only?":
            bree.say "I hope you're getting checked out by the girls too, Angela!"
            bree.say "This is the twenty-first century you know?"
            bree.say "And guys aren't the only option."
            $ angela.sub += 1
        "Be careful":
            bree.say "Yeah, I wouldn't read too much into that, Angela."
            bree.say "Some guys are into older women because it's a kink."
            bree.say "But most of them just think that they're desperate."
            $ angela.love -= 1
    return

label angela_desire_3_female:
    angela.say "You know, I used to think that I was pretty worldly, [hero.name]."
    angela.say "But since I've been back out there dating..."
    angela.say "Well, let's just say I've had my eyes opened."
    angela.say "And I've seen some pretty crazy stuff!"
    menu:
        "Don't worry":
            bree.say "Oh, that's nothing to do with you being out of the game, Angela!"
            bree.say "I find it hard to keep up as well."
            bree.say "Maybe we could compare notes some time?"
            bree.say "You could probably teach me something new!"
            $ angela.love += 1
        "There's space for improvement":
            bree.say "Yeah, I can see how that's be a problem, Angela."
            bree.say "You're probably so out of touch it's not even funny!"
            bree.say "Good luck trying to get up to speed too!"
            $ angela.love -= 1
        "I can help":
            bree.say "Oh, there's no need to worry about that kind of thing, Angela."
            bree.say "Not when you've got somebody like me to teach you all you need to know!"
            bree.say "Just let me know when you're ready for a lesson."
            bree.say "And I'll soon whip you into shape!"
            $ angela.sub += 1
    return

label angela_desire_4_female:
    angela.say "I can't believe I was scared to be single again after all this time."
    angela.say "Because I'm having so much fun being back on the dating scene again."
    angela.say "I feel like I'm making up for all those years I lost."
    angela.say "And it's really challenging me too."
    angela.say "You know, expanding my mind?"
    menu:
        "That's cute":
            bree.say "Aww, that's so cute, Angela!"
            bree.say "You're like a lock-in that's finally gone outside."
            bree.say "I mean, you're still pretty screwed-up."
            bree.say "But you're trying so hard to be normal!"
            $ angela.love -= 1
        "I understand":
            bree.say "I know exactly what you mean, Angela."
            bree.say "And I kind of feel privileged to have seen it happen too."
            bree.say "It's like we've been on a journey together."
            bree.say "You know what I mean?"
            $ angela.love += 1
        "That's just the beginning":
            bree.say "Yeah, I'd have thought you'd get a handle on it quicker, Angela."
            bree.say "I mean, you've definitely made some serious progress."
            bree.say "But you do still have a long way to go!"
            $ angela.sub -= 1
    return

label angela_desire_5_female:
    angela.say "Wow, [hero.name] - I kind of feel like a whole new woman!"
    angela.say "Like I've left the person I was in the past behind me."
    angela.say "And I'm so much more in touch with my own desires too."
    angela.say "It's like I know what they are in such detail."
    angela.say "I'm not ashamed of them either."
    angela.say "I know they're something natural, and not just me being selfish!"
    menu:
        "You're sweet":
            bree.say "Oh, Angela - that's so sweet!"
            bree.say "But you know the real problem was never that you were being controlled."
            bree.say "It was just that you were in the power of the wrong person."
            bree.say "And now that you have me in your life, all that's changed!"
            $ angela.sub += 1
        "That's a point of view":
            bree.say "Yeah, I get that you're not crazy any more, Angela."
            bree.say "But maybe you want to spend some time working on other stuff too?"
            bree.say "Because your personality could use a little help!"
            $ angela.love -= 1
        "You seem happy":
            bree.say "I can't believe how far you've come, Angela."
            bree.say "It's almost like you're a totally different person now."
            bree.say "You seem so much happier and together."
            bree.say "And I just love being around you too."
            $ angela.love += 1
    return

label angela_love_0_female:
    angela.say "It's been pretty hard for me these past few months, [hero.name]."
    angela.say "Everything seems to have changed so fast, I'm running to keep up."
    angela.say "But I just wanted to say that you've really helped me out."
    angela.say "You've been a really good friend to me."
    menu:
        "Thank you":
            bree.say "Aw...thank you, Angela."
            bree.say "I was just trying to help out."
            bree.say "But I do see you as a friend."
            bree.say "You kind of just fit right in."
            $ angela.love += 1
        "It's normal":
            bree.say "That's nice of you to say, Angela."
            bree.say "But I'd have done the same for anyone."
            bree.say "It's not like you're a special case!"
            $ angela.love -= 1
        "You needed help":
            bree.say "Well, you kind of looked like you needed help, Angela!"
            bree.say "You did fall apart a bit when everything happened, didn't you?"
            bree.say "But that's okay - some people just aren't strong in a crisis."
            $ angela.sub -= 1
    return

label angela_love_1_female:
    bree.say "How are you doing now, Angela?"
    bree.say "You seem to be brighter than I've seen you in a while!"
    angela.say "Oh, bless you for asking, [hero.name]!"
    angela.say "I should have known you'd be thoughtful enough to ask."
    menu:
        "Thank you":
            bree.say "Oh, thank god for that!"
            bree.say "You been SO needy this past few weeks."
            bree.say "Maybe I can stop having to look out for you the whole time!"
            $ angela.love -= 1
        "No problem":
            bree.say "It's no trouble, really, Angela."
            bree.say "I'd be doing the same for any of my friends."
            bree.say "Just let me know if you need anything, okay?"
            $ angela.love += 1
        "I enjoyed it":
            bree.say "It's no trouble, Angela."
            bree.say "In fact, I've really enjoyed look out for you all this time."
            bree.say "It's almost like I get a kick out of you needing me so much!"
            bree.say "How weird is that?"
            $ angela.sub += 1
    return

label angela_love_2_female:
    angela.say "Are you sure you want to spend so much time hanging out with me, [hero.name]?"
    angela.say "I mean, you're so young and carefree."
    angela.say "I love that you do it, really I do."
    angela.say "But I'm getting worried that I'm holding you back!"
    menu:
        "That's not true":
            bree.say "Don't be silly, Angela - age doesn't even come into it."
            bree.say "You're just like one of my regular friends."
            bree.say "In fact, you're probably even better than them."
            bree.say "And I love hanging out with you!"
            $ angela.love += 1
        "You don't":
            bree.say "What are you talking about, Angela?"
            bree.say "You're an empowered woman that's in her prime!"
            bree.say "There's no way I could hold you back if I wanted to!"
            $ angela.sub -= 1
        "Meh...":
            bree.say "Thank god you were the one to say it, Angela!"
            bree.say "I do feel like I've been propping you up all this time."
            bree.say "What I really need is a chance to reconnect with my real friends."
            bree.say "You know, the ones I really want to spend time with?"
            $ angela.love -= 1
    return

label angela_love_3_female:
    angela.say "I feel really stupid saying this, [hero.name]."
    angela.say "But it's like you're becoming my best friend."
    angela.say "I'm getting so much from hanging out with you."
    angela.say "Don't you think we're a great match?"
    menu:
        "About that":
            bree.say "Yeah, I was going to talk to you about that."
            bree.say "I do feel like you've been getting a little clingy of late."
            bree.say "Maybe it'd do us both good to have some space?"
            bree.say "And by that I mean you backing off!"
            $ angela.love -= 1
        "I think so":
            bree.say "I think it's more than that, Angela."
            bree.say "In fact, I think you couldn't be without me."
            bree.say "Like if I clicked my fingers, you'd come running to me!"
            bree.say "And you like being in that position, don't you?"
            $ angela.sub += 1
        "I agree":
            bree.say "I know exactly what you mean, Angela."
            bree.say "I just didn't know how to say it myself!"
            bree.say "Also, I kinda like having a bestie that's older than me."
            bree.say "It makes me feel all sophisticated and grown-up!"
            $ angela.love += 1
    return

label angela_love_4_female:
    angela.say "I feel like I'm on a voyage of discovery, [hero.name]."
    angela.say "Like I'm finding out who I am for the very first time."
    angela.say "Before now, I never knew that I could have feelings for another woman."
    angela.say "A woman like you..."
    menu:
        "That make us even":
            bree.say "Me neither, Angela."
            bree.say "But I guess that's just how life is."
            bree.say "It takes you by surprise."
            bree.say "But it does that in the most amazing and unexpected ways!"
            $ angela.love += 1
        "I know what you mean":
            bree.say "I know what you mean, Angela."
            bree.say "You've been on an incredible journey."
            bree.say "You started out as a woman that was being totally controlled."
            bree.say "But now I can't imagine anybody making you do something you didn't want to!"
            $ angela.sub -= 1
        "I'm not so sure":
            bree.say "Yeah, well..."
            bree.say "You might be jumping to the wrong conclusion there, Angela!"
            bree.say "I'm cool with being friends and all that."
            bree.say "But I don't know if I want to be more than that!"
            $ angela.love -= 1
    return

label angela_love_5_female:
    angela.say "There's no sense in me denying my feelings anymore, [hero.name]."
    angela.say "I've totally fallen for you, head over heels!"
    angela.say "All I know is that I can't keep it hidden any longer."
    angela.say "That and the fact I'm hoping you feel the same way too!"
    menu:
        "About that":
            bree.say "Yeah, well..."
            bree.say "Maybe you should have tried a little harder, Angela!"
            bree.say "The world inside of your head isn't the same as the one out here!"
            $ angela.love -= 1
        "I feel the same":
            bree.say "You don't know how long I've been waiting for you to say that, Angela!"
            bree.say "I feel the same way, on hundred percent!"
            bree.say "I'm so happy that you finally came out and said it!"
            $ angela.love += 1
        "I know just what you mean":
            bree.say "I know just what you mean, Angela."
            bree.say "Your proper place is right here, by my side."
            bree.say "Hanging on my every word like your life depends on it!"
            $ angela.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
