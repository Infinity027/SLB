label kiara_desire_0_male:
    kiara.say "I always think that there is more to the job of a cafe manager then there seems."
    kiara.say "Hiring the staff, doing the paperwork and all of that is just what is seen on the surface."
    kiara.say "What I am really responsible for is the ambiance of the place, the ineffable quality of it's atmosphere."
    menu:
        "I'm certainly getting a good vibe" if hero.charm >= 50:
            mike.say "I don't pretend to know how you do it, Kiara..."
            mike.say "But there's definitely a unique vibe to the place."
            mike.say "I notice it whenever I walk in, and it keeps bringing me back again too."
            kiara.say "You see, I knew that you would understand."
            kiara.say "Because you are a man of refined taste."
            $ kiara.sub += 1
        "Ah get over yourself":
            mike.say "Are yo just saying that to make yourself feel important, Kiara?"
            mike.say "Because it's not like running a cafe is really that had."
            mike.say "Like, not compared to performing open-heart surgery!"
            kiara.say "Thank you for letting me know what you think, [hero.name]."
            kiara.say "I would not like to get ideas above my station in life."
            $ kiara.love -= 1
        "Nobody else notices how hard you work but me":
            mike.say "I know the real reason you're saying all of this, Kiara - because nobody notices how hard you work."
            mike.say "But that's where I'm different, because I do and I appreciate all of the effort you put in."
            mike.say "And I like to think that you do too, and that you go that little bit further for me as a result."
            kiara.say "You really pay that much attention to me?"
            kiara.say "Oh, how flattering it is to know that!"
            $ kiara.love += 1
    return

label kiara_desire_1_male:
    kiara.say "The girls that come into the cafe, and maybe even some of the boys..."
    kiara.say "They are all so young and vibrant, wearing such exciting clothes - and the way they style their hair too!"
    kiara.say "Sometimes it makes me feel my age, like I am becoming so far behind the times."
    menu:
        "Your look is timeless" if hero.charm >= 50:
            mike.say "What are you even talking about, Kiara?"
            mike.say "Those guys change their look every other day."
            mike.say "You don't have to, because your look is timeless."
            kiara.say "Oh, [hero.name] - do you really think so?"
            kiara.say "I am so happy to hear that."
            $ kiara.love += 1
        "Maybe you should freshen things up":
            mike.say "Don't worry about it, Kiara, that's just a natural part of getting older."
            mike.say "You can either try copying the young, hip things and risk looking desperate."
            mike.say "Or you can just own it and accept that you're not cool anymore - your choice."
            kiara.say "Well that was very bluntly put, [hero.name]."
            kiara.say "Maybe next time I will ask for advice from someone else."
            $ kiara.love -= 1
        "They should be looking up to you":
            mike.say "You mean those immature embryos that come in here for bubble tea?"
            mike.say "I hardly notice what they're wearing, Kiara."
            mike.say "And that's because I'm too busy looking at you!"
            kiara.say "Well, I suppose that I do turn heads."
            kiara.say "But I had no idea you were that enamoured of my style..."
            $ kiara.sub += 1
    return

label kiara_desire_2_male:
    kiara.say "Ah...work is so hard, and to be a success in business is so demanding."
    kiara.say "I give everything that my cafe demands from me to make it thrive."
    kiara.say "But inside me there always beats the desire for adventure, the will to dream!"
    menu:
        "I can see that you were meant for more":
            mike.say "I don't think that you're destined to just be the owner of a cafe, Kiara."
            mike.say "You just seem to have something about you, an air of brilliance, or something."
            mike.say "I...I just don't think people will remember you for the cafe, but something bigger."
            kiara.say "That is such a kind thing to say - and insightful too."
            kiara.say "Maybe there is more to you than meets the eye too..."
            $ kiara.love += 1
        "Do I detect a lack of confidence":
            mike.say "That sounds like a complicated way of saying you're on the verge of burning-out, Kiara."
            mike.say "That you've taken on too much with the cafe and you'd be better off living a simpler life."
            mike.say "It's not fashionable to say this - but you might be happier as a home-maker!"
            kiara.say "Hmm...my instinct is to say no, that you are one hundred percent wrong."
            kiara.say "But there is something about the way you put it - maybe I should think this over?"
            $ kiara.sub -= 1
        "I could bask in your greatness all day long" if hero.charm >= 75:
            mike.say "I think you're really onto something there, Kiara."
            mike.say "Like there's a world of potential inside of you, just waiting to come out."
            mike.say "I only hope I can be there when it does!"
            kiara.say "You really think so, [hero.name]?"
            kiara.say "Tell me more about this quality you see inside of me..."
            $ kiara.sub += 1
    return

label kiara_desire_3_male:
    kiara.say "Being the boss is hard, you know what I mean?"
    kiara.say "You are responsible for the cafe, all of the staff and pleasing the customers."
    kiara.say "But sometimes I get tired of the responsibility, and of always giving out orders."
    menu:
        "If you can't handle the heat":
            mike.say "Yeah, but I bet having the biggest wage packet at the end of the month helps, right?"
            mike.say "Seriously, Kiara, I never buy it when the boss starts playing the violin music."
            mike.say "Because if you really hated it, you'd just up and quit, go get another job."
            kiara.say "You make everything sound so simple, [hero.name]."
            kiara.say "Not least yourself."
            $ kiara.sub -= 1
        "Are you saying that you can't cope":
            mike.say "Look, Kiara, I know that there's pressure on working women to be strong."
            mike.say "But what's the point of that if it just makes you miserable all the time?"
            mike.say "And if you need someone to take the reigns, then you can always ask me."
            kiara.say "Well, when you put it like that..."
            kiara.say "Maybe I could use a little help with the load."
            $ kiara.sub += 1
        "Are you kidding you're great at this" if hero.charm >= 75:
            mike.say "Are you kidding, Kiara - you're great at this!"
            mike.say "You've got that place running like a well-oiled machine."
            mike.say "And I'll let you in on a little secret - I kinda wish you were my boss and ordered me around too!"
            kiara.say "Well, when you put it like that..."
            kiara.say "And you know that I can give orders to you without being your boss, yes?"
            $ kiara.love += 1
    return

label kiara_desire_4_male:
    kiara.say "Managing the cafe has been harder than usual today, [hero.name]."
    kiara.say "And it is all because I cannot keep myself from thinking of you."
    kiara.say "When we finally are together, you must see if you can live up to my flights of fantasy!"
    menu:
        "I like a challenge":
            mike.say "Oh wow, Kiara - it's so hot hearing you tell me that!"
            mike.say "But I'm not just going to live up to your fantasies."
            mike.say "No, I'm going to try my best to exceed them!"
            kiara.say "Oh, [hero.name], you are such a passionate beast."
            kiara.say "Wilder than my wildest imagination!"
            $ kiara.love += 1
        "Way to pile on the pressure":
            mike.say "Don't you think that's a little bit selfish, Kiara?"
            mike.say "You know, piling all of the pressure on me like that?"
            mike.say "You're not the only one with a job and responsibilities!"
            kiara.say "That maybe so, [hero.name]..."
            kiara.say "But it would seem I am the only one of us with any romance in their soul!"
            $ kiara.love -= 1
        "Just tell me what you want and I'll do it":
            mike.say "I love that you're thinking about me, Kiara."
            mike.say "And I want to repay you by making your fantasies into reality."
            mike.say "When we get together, just tell me what you want, and I'll make it happen."
            kiara.say "Oh, [hero.name], you make me feel like a princess."
            kiara.say "A princess with a hero to attend to her every whim!"
            $ kiara.sub += 1
    return

label kiara_desire_5_male:
    kiara.say "I cannot contain the feelings that are bubbling up inside of me for you, [hero.name]."
    kiara.say "Either I will close the cafe and come running to you, wherever you are."
    kiara.say "Or else you must come to me, and I will lock the door while we are locked in each other's embrace!"
    menu:
        "I'm already on the move":
            mike.say "Kiara, you don't know what it does to me, hearing you talk like that!"
            mike.say "Stay right where you are and don't move an inch until I get there, okay?"
            mike.say "Oh...but if you're at the cafe, then you might want to get the customers out of there - and fast!"
            kiara.say "Oh, [hero.name], this is so exciting!"
            kiara.say "I will toss them out into the street with my own hands if I have to, this I promise."
            $ kiara.love += 1
        "I'll be there when I can make it":
            mike.say "Kiara, you're getting me so fucking horny right now!"
            mike.say "But you're going to have to wait until I can make it to you."
            mike.say "Something's come up - and I'm not trying to sound rude either!"
            kiara.say "Well you had better be quick about it, [hero.name]."
            kiara.say "Because I need release, and I will have it, one way or another!"
            $ kiara.love -= 1
        "I'm on my way mistress":
            mike.say "I'm literally dropping everything and coming right now."
            mike.say "Also you might want to text me a list of all the things you want me to do?"
            mike.say "I can commit it to memory on the way over and then make all of it happen for real!"
            kiara.say "Oh, [hero.name], you are so attentive and so efficient."
            kiara.say "Not to mention obedient!"
            $ kiara.sub -= 1
    return

label kiara_love_0_male:
    kiara.say "Fate was kind to me when you decided to come into my cafe and order a hot beverage, [hero.name]."
    kiara.say "Because I have grown to enjoy our conversations and the laughter we share together."
    kiara.say "I am glad that you did not choose to get your coffee from somewhere else."
    menu:
        "I never used to be so loyal":
            mike.say "You know it really is pretty weird I kept coming back, Kiara."
            mike.say "I used to have a ton of those half-filled loyalty cards from all sorts of places."
            mike.say "But there's just something about your cafe that keeps me coming back."
            kiara.say "Ah, you are vague on the subject because you are a gentleman."
            kiara.say "But I think we both have a suspicion of what the reason could be..."
            $ kiara.sub -= 1
        "Kiara, I want you to serve me coffee all day long":
            mike.say "Kiara, if I could, I'd take you home and have you serve me coffee there too!"
            mike.say "There's just something about getting it from you that feels right."
            mike.say "Even if I can't quite figure out what it is..."
            kiara.say "Oh, [hero.name]..."
            kiara.say "I would serve you coffee first thing in the morning - and last thing at night with pleasure!"
            $ kiara.love += 1
        "You could order me into your cafe":
            mike.say "I don't know how to explain it, Kiara..."
            mike.say "Part of me feels like you could order me into your cafe."
            mike.say "Like I'd be powerless to resist your command!"
            kiara.say "Is that so?"
            kiara.say "Well maybe that is something I should try some time..."
            $ kiara.sub += 1
    return

label kiara_love_1_male:
    kiara.say "I am seeing you so often in the cafe these days, [hero.name]..."
    kiara.say "Are you that desperate to fill up your loyalty card and claim your free coffee?"
    kiara.say "Or maybe there is some other reason that you come so regularly?"
    menu:
        "You got me":
            mike.say "Ah...yeah, Kiara...I have a confession to make."
            mike.say "It's not the coffee that brings me back, it's the staff around here."
            mike.say "Or to be more precise, the senior member of staff!"
            kiara.say "Oh, but you do not need to be shy about that, [hero.name]."
            kiara.say "I am very flattered by your attention."
            $ kiara.love += 1
        "It's the caffeine hit":
            mike.say "Ha...don't read too much into it, Kiara."
            mike.say "I'm here for the caffeine hit you guys deliver."
            mike.say "The rest of this just doesn't register in my head!"
            kiara.say "Oh, is that so?"
            kiara.say "And here I was thinking that we had something special."
            $ kiara.love -= 1
        "I know that it's not just me":
            mike.say "Oh come on, Kiara, stop trying to pin it all on me!"
            mike.say "I've seen how quickly you scoot over here whenever I come in."
            mike.say "Don't tell me you serve all your customers in person."
            kiara.say "Well...of course not!"
            kiara.say "I only do that for the special ones..."
            $ kiara.sub += 1
    return

label kiara_love_2_male:
    kiara.say "I have to say that this is rare for me, [hero.name]..."
    kiara.say "For one of my regulars to become more than that, to grow into a friend."
    kiara.say "But I feel that there is a genuine connection between us, would you not agree?"
    menu:
        "Oh definitely":
            mike.say "Oh I definitely would, Kiara!"
            mike.say "It might have started off with you selling me coffee."
            mike.say "But there's much more to our friendship now."
            kiara.say "Exactly so, [hero.name]..."
            kiara.say "And I hope that our relationship will grow stronger still."
            $ kiara.love += 1
        "Let's not get ahead of ourselves":
            mike.say "We've definitely become more than we used to be, Kiara."
            mike.say "But let's not go getting ahead of ourselves, yeah?"
            mike.say "If we're going to be friends, then let it develop naturally."
            kiara.say "Hmm...maybe I was not clear enough just now?"
            kiara.say "Maybe calling you a friend gave the wrong impression..."
            $ kiara.love -= 1
        "I really hope so":
            mike.say "Oh, Kiara - I'm so glad that you said that!"
            mike.say "I've wanted to be more than your customer for so long now."
            mike.say "And maybe I could be more...if you'll let me?"
            kiara.say "Oh my goodness, you are so eager to please!"
            kiara.say "I had no idea that you would be so...biddable."
            $ kiara.sub -= 1
    return

label kiara_love_3_male:
    kiara.say "It feels like a breath of fresh air to be able to be open and honest with you, [hero.name]."
    kiara.say "You know, now that we are seeing one another and not still merely friends?"
    kiara.say "I feel that we can really begin to explore the deepest parts of each other's soul."
    menu:
        "I want to explore your mysteries":
            mike.say "I know exactly what you mean, Kiara..."
            mike.say "All the time we were getting to know each other, you were so damn mysterious to me."
            mike.say "And now I can't wait to start discovering what you're hiding behind those big, dark eyes of yours!"
            kiara.say "Be careful when you stare into the depths, [hero.name], for they stare back into you."
            kiara.say "And who knows what you may find swimming in the depths of my eyes!"
            $ kiara.love += 1
        "I think I know what I'm going to find":
            mike.say "Oh, I think I always had a good idea of what I was going to find, Kiara."
            mike.say "I feel like I was tuning into you from the moment that we first met."
            mike.say "And now I have you in the palm of my hand!"
            kiara.say "Oh, [hero.name], you sound so confident all of a sudden!"
            kiara.say "I don't know if I have the power to resist you for a moment."
            $ kiara.sub += 1
        "I'm yours to explore":
            mike.say "Just ask me anything you want to know, Kiara, anything at all."
            mike.say "Because I don't think there's any way that I could say no."
            mike.say "You could reach into my chest and just pull my heart straight out."
            kiara.say "Oh my goodness, maybe that would be a little too extreme!"
            kiara.say "But I certainly approve of the sentiment..."
            $ kiara.sub -= 1
    return

label kiara_love_4_male:
    kiara.say "You know that in all the time I have managed the cafe, I never thought this would happen."
    kiara.say "I never thought that a customer would come walking in and then walk away with my heart."
    kiara.say "But nevertheless, it has come to pass and here we both are!"
    menu:
        "This is fate":
            mike.say "I don't normally go in for this kind of thing, Kiara..."
            mike.say "But I can't help thinking that this was meant to be, that it was fate."
            mike.say "Because I don't know how else to explain how perfectly it all worked out."
            kiara.say "I could not have said it better myself."
            kiara.say "Some things are just meant to be."
            $ kiara.love += 1
        "We just got lucky, that's all":
            mike.say "Geez...why do you have to make a big thing out of it, Kiara?"
            mike.say "Can't you just be happy that we found each other?"
            mike.say "Isn't that enough without making it into a fairytale?"
            kiara.say "Now I understand why they say that romance is dead."
            kiara.say "I have seen it killed, embalmed and then buried!"
            $ kiara.love -= 1
        "You were always meant to be mine":
            mike.say "I think you're right, Kiara - this was meant to be."
            mike.say "It's fate sending you a message, telling you that you were made for me."
            mike.say "By which I mean for me and nobody else!"
            kiara.say "I...I suppose that you have a point, [hero.name]."
            kiara.say "And it would be an ungrateful thing to go against what fate has decreed for us..."
            $ kiara.sub += 1
    return

label kiara_love_5_male:
    kiara.say "I have come too far and gone through too much to hide my feelings now."
    kiara.say "From this point on, I will give voice to my emotions when I have the need."
    kiara.say "And most of all, [hero.name], I will say that I love you as often as I am able!"
    menu:
        "As will I, my love":
            mike.say "And every time you utter those words, my heart will ache for that love."
            mike.say "Because I feel the same way about you, my love."
            mike.say "I love you, Kiara, and I want the whole world to know it!"
            kiara.say "They will, my love, believe me they will."
            kiara.say "Because it will be plain to see as long as we are together!"
            $ kiara.love += 1
        "Okay, okay, I get the message":
            mike.say "Okay, okay, Kiara - I get the message!"
            mike.say "You got me, yeah, so there's no need to run it into the ground."
            mike.say "Just try and chill out a little, yeah?"
            kiara.say "I...I was only trying to be loving, [hero.name]."
            kiara.say "I had no idea that you were so embarrassed by such things."
            $ kiara.love -= 1
        "I am yours forever":
            mike.say "No, Kiara - I should be the one declaring that about you!"
            mike.say "I want everyone we meet to know that I'm the luckiest guy in the world."
            mike.say "That I'm like, one hundred percent devoted to you!"
            kiara.say "Well, if that's the way you feel, [hero.name]..."
            kiara.say "It would be churlish of me to stop you."
            $ kiara.sub -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
