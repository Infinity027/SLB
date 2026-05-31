label cherie_desire_0_male:
    cherie.say "It's good to be able to talk freely, don't you think?"
    cherie.say "Not only to chat about this and that with someone who's company you enjoy."
    cherie.say "But to know that they are mature and sensitive enough for the subject to become...intimate, no?"
    menu:
        "Friends that get you are the most important kind" if hero.charm >= 50:
            mike.say "I think I get what you're saying, Cherie..."
            mike.say "It's like with some people, you just know that they get you, right?"
            mike.say "You can tell them anything, and know that they won't judge you."
            cherie.say "Yes, [hero.name] - exactly that!"
            cherie.say "And I believe we are like that to each other, you and me."
            $ cherie.love += 1
        "Loose lips sink ships":
            mike.say "I don't know about that, Cherie..."
            mike.say "When I've trusted people in the past, I've gotten hurt."
            mike.say "Makes me watch what I say and what I hear pretty closely."
            cherie.say "Oh dear me..."
            cherie.say "That is so disappointing to hear."
            $ cherie.love -= 1
        "I'm that guy and we're a pretty rare type":
            mike.say "I know that you're talking about me, Cherie..."
            mike.say "And you're right to choose me as a confidant."
            mike.say "Because guys like me don't come along very often - I can tell you that!"
            cherie.say "Oh, is that so?"
            cherie.say "I...I will be sure to keep that in mind."
            $ cherie.sub -= 1
    return

label cherie_desire_1_male:
    cherie.say "Some people are really attracted to my accent, [hero.name]."
    cherie.say "So much so that I wonder if they actually hear what I say."
    cherie.say "And I question if they would find me as agreeable were it the same as yours."
    menu:
        "Your accent makes your words sound like poetry" if hero.charm >= 50:
            mike.say "I wouldn't worry about that, Cherie..."
            mike.say "How could anyone not like your accent?"
            mike.say "It makes every word you say sound like poetry!"
            cherie.say "Oh, you really think so?"
            cherie.say "That is so kind of you to say!"
            $ cherie.love += 1
        "Your accent does make you hard to understand sometimes":
            mike.say "Yeah, I get what you're saying, Cherie."
            mike.say "You really do have a very thick accent."
            mike.say "Hell, sometimes I can't tell what you're saying at all!"
            cherie.say "Oh, I had no idea it was that bad."
            cherie.say "I will have to see what can be done about it..."
            $ cherie.love -= 1
        "Your accent is not for everyone":
            mike.say "Your accent is really hard to get around, Cherie."
            mike.say "Probably best if you keep quiet when we're out in public, yeah?"
            mike.say "That and let me do all of the talking too."
            cherie.say "Oh no - it's that bad?"
            cherie.say "Maybe I should speak up less in public..."
            $ cherie.sub += 1
    return

label cherie_desire_2_male:
    cherie.say "Ah, the life of a married woman can be one of tedious isolation."
    cherie.say "So much time spent alone and with only my thoughts for company."
    cherie.say "If you could only see where they took me, [hero.name] - you would surely blush!"
    menu:
        "You don't have to be alone anymore":
            mike.say "Things aren't like that anymore, Cherie."
            mike.say "And I won't see you cooped up like that either."
            mike.say "Now your thoughts can become reality, if you'd like?"
            cherie.say "Things always sound so much brighter when you describe them."
            cherie.say "The future seems to hold more promise too."
            $ cherie.love += 1
        "I'm the one that's caring for you now" if hero.charm >= 75:
            mike.say "There's no need for you to worry about the world at large, Cherie."
            mike.say "You're free of what was holding you back before, and now you have me."
            mike.say "Someone that won't let another person get close enough to hurt you."
            cherie.say "Oh, [hero.name]..."
            cherie.say "You can be so forceful and yet so magnetic sometimes."
            $ cherie.sub += 1
        "You're free now and your own woman":
            mike.say "You need to put all of that behind you, Cherie."
            mike.say "None of that stuff was anything to do with the real you."
            mike.say "It was just Dwayne trying to make you feel small."
            cherie.say "Thank you for saying so, [hero.name]."
            cherie.say "I thought as much - but it means a great deal to hear you say so."
            $ cherie.sub -= 1
    return

label cherie_desire_3_male:
    cherie.say "I am so bored with having to be sensible and do as people think I should."
    cherie.say "Would it not be more fun to just do whatever we wanted in the moment?"
    cherie.say "Maybe even, dare I say it...be ruled by our desires?"
    menu:
        "I think you need to be a little more disciplined":
            mike.say "Sounds like the problem you have there is a serious lack of discipline, Cherie."
            mike.say "Might want to take some time out and work on your impulse control, you know?"
            mike.say "You kind of need that if you want to pass yourself off as an adult!"
            cherie.say "Oh, you really think so?"
            cherie.say "Funny, I never thought you were so set in your ways."
            $ cherie.love -= 1
        "Just forget about all of that nonsense and let me choose for you" if hero.charm >= 75:
            mike.say "You shouldn't spend all your time worrying about that kind of stuff, Cherie."
            mike.say "Just forget all about it and let me make those decisions for you, yeah?"
            mike.say "Because I can always think of a million fun things we can do together..."
            cherie.say "Oh...oh my goodness!"
            cherie.say "That does sound rather exciting, [hero.name]!"
            $ cherie.sub += 1
        "Being ruled by your desires sounds nice to me":
            mike.say "I feel the same way, Cherie - like, totally bored and bummed out."
            mike.say "Problem is that I can't seem to think of anything to break myself out of it."
            mike.say "In fact, I'm so desperate that I'd probably do anything you suggested - absolutely anything!"
            cherie.say "Well, if you really mean that, [hero.name]..."
            cherie.say "I'm sure that I could come up with something fun that we'd both enjoy!"
            $ cherie.sub -= 1
    return

label cherie_desire_4_male:
    cherie.say "Oh, [hero.name] - I have been so lonely without you."
    cherie.say "And I hope that your longing for me is just as intense."
    cherie.say "How are you going to greet me once we are together again?"
    menu:
        "Wait until you see what I have planned":
            mike.say "I feel the same way about you too, Cherie..."
            mike.say "But I can't tell you what I have planned, because it'd spoil the surprise."
            mike.say "Just wait and see - I guarantee it'll blow your mind!"
            cherie.say "Well that sounds like something to look forward too."
            cherie.say "I am getting excited already!"
            $ cherie.love += 1
        "Way to pile pressure onto me":
            mike.say "I do have a life of my own, you know, Cherie!"
            mike.say "And that means I can't spend every waking moment thinking about you."
            mike.say "Just be patient and wait until we can do something together, okay?"
            cherie.say "And they say that romance is dead!"
            cherie.say "With some people, it is practically fossilised."
            $ cherie.love -= 1
        "I should be the only thing on your mind":
            mike.say "That's what I like to hear, Cherie - that I'm the only thing on your mind."
            mike.say "Just keep on making sure it stays that way, okay?"
            mike.say "That way I'm all the more motivated to reward your devotion!"
            cherie.say "Oh, [hero.name]..."
            cherie.say "You are so masterful!"
            $ cherie.sub += 1
    return

label cherie_desire_5_male:
    cherie.say "I can no longer hide my desire for you behind polite chit-chat, [hero.name]."
    cherie.say "My needs have become so intense that I must speak them out loud, or else go mad!"
    cherie.say "Tell me that you feel the same, and that you will satisfy me as soon as you are able?"
    menu:
        "Just give me half a damn chance":
            mike.say "You think it's easy for me to keep a lid on what I feel for you?!?"
            mike.say "Cherie, I think about you all the time when we're apart."
            mike.say "About all of the things I'm going to do to you when we're next together!"
            cherie.say "Oh, [hero.name], is that the truth?"
            cherie.say "Because if so, I must have you all the sooner!"
            $ cherie.love += 1
        "This is bordering on an obsession":
            mike.say "Cherie, I love you to the moon and back."
            mike.say "But you need to learn to chill out, okay?"
            mike.say "Otherwise you really are going to drive yourself crazy!"
            cherie.say "I do not think you understand a woman's passion, [hero.name]."
            cherie.say "Keep talking to me like that, and you never will!"
            $ cherie.love -= 1
        "I love it when you talk to me like that":
            mike.say "Oh man - I love it when you talk to me like that, Cherie!"
            mike.say "You sound so full of passion, like you're totally going to take charge."
            mike.say "I just want to throw my arms open wide and let you do whatever you want to me!"
            cherie.say "Is that an invitation, [hero.name]?"
            cherie.say "Because if so, it is one I have a mind to accept."
            $ cherie.sub -= 1
    return

label cherie_love_0_male:
    cherie.say "Fate is a strange and unknowable thing, is it not?"
    cherie.say "For instance, if you had never been employed by Dwayne, we would not have met."
    cherie.say "So maybe we have to admit that good things happen because of bad people?"
    menu:
        "I was certainly the lucky one":
            mike.say "I don't know if I believe in fate and luck and all that stuff, Cherie."
            mike.say "But I'm kind of amazed at the chances of us ever meeting in life."
            mike.say "That's one of the things that makes me so grateful to know someone as special as you."
            cherie.say "Oh, [hero.name], I feel the same way about you."
            cherie.say "A friend so special is something to be thankful for."
            $ cherie.love += 1
        "Fate delivered you into my hands":
            mike.say "If you believe that, Cherie, then you must believe you were meant for me."
            mike.say "Like, you were with Dwayne, and now you're not - because of me."
            mike.say "Sounds like fate's trying to send you a message!"
            cherie.say "You know, I never thought of it that way."
            cherie.say "But now I see that you might be onto something."
            $ cherie.sub += 1
        "Fate delivered me into your hands":
            mike.say "I totally get what you mean, Cherie - like, fate delivered me to you."
            mike.say "And it feels to me like there's nothing I could have done to resist."
            mike.say "Even if I'd tried, it would have still laid me out at your feet!"
            cherie.say "You know, I never thought of it that way."
            cherie.say "But now I see that you might be onto something."
            $ cherie.sub -= 1
    return

label cherie_love_1_male:
    cherie.say "You have been so kind to me recently, [hero.name], and so attentive."
    cherie.say "Sending me messages just to ask how I'm feeling, and always so interested in what I have to say."
    cherie.say "You really are making me feel that you're the best friend I have to call upon."
    menu:
        "It just feels natural":
            mike.say "I can't explain it, Cherie - I just enjoy talking to you about anything!"
            mike.say "And it makes me feel happy to know what you're doing okay as well."
            mike.say "So I'm sorry, but I won't be stopping with the pestering any time soon!"
            cherie.say "On the contrary, {i}mon ami{/i}, I would not change a thing."
            cherie.say "Our talks are fast becoming the highlight of my day!"
            $ cherie.love += 1
        "You don't always have to reply":
            mike.say "I'm just checking up on you, Cherie, trying to be a good friend, yeah?"
            mike.say "And for the record, you don't always have to send me a response."
            mike.say "You can just read the message and send me an emoji or something."
            cherie.say "Oh...I see."
            cherie.say "My mistake to think there was more to them than that."
            $ cherie.love -= 1
        "I hang on your every message":
            mike.say "It's weird, Cheri, but I feel like your messages have become the highlight of my day."
            mike.say "As soon as my phone vibrates, I pull it out, hoping that it's a new message from you."
            mike.say "And if I see that it's not...well, my mood just sinks - it goes right down the toilet!"
            cherie.say "Are you being serious with me?!?"
            cherie.say "I had no idea that I was such an influence on your life."
            $ cherie.sub -= 1
    return

label cherie_love_2_male:
    cherie.say "Do you not think it is strange, {i}mon ami{/i}..."
    cherie.say "I was once your employer's wife, and you were his employee."
    cherie.say "But now, the two of us, we are...friends, yes?"
    menu:
        "I hope we're way more than that":
            mike.say "Just friends?!?"
            mike.say "Cherie, I thought that we were way more than that!"
            mike.say "What am I doing wrong to make you think like that?"
            cherie.say "Oh, of course we are more than simply friends."
            cherie.say "I simply did not want to assume too much."
            $ cherie.love += 1
        "I guess you could call us that":
            mike.say "I guess that's what you could call our relationship, Cherie."
            mike.say "I don't like it when people get ahead of themselves in relationships."
            mike.say "So I definitely wouldn't say it was any more than that."
            cherie.say "Oh, so that is how you feel about me?"
            cherie.say "I will have to keep that in mind..."
            $ cherie.love -= 1
        "Oh we're going to be much more than that":
            mike.say "We might only be friends right now, Cherie..."
            mike.say "But I plan on us being much more than that real soon!"
            mike.say "And you're not going to want to say no to anything I have in mind."
            cherie.say "Oh, {i}mon ami{/i}..."
            cherie.say "I never knew you could be so...so forceful!"
            $ cherie.sub += 1
    return

label cherie_love_3_male:
    cherie.say "Now that we are getting to know each other, I feel like a weight had been lifted off of me."
    cherie.say "I am no longer just the wife of your boss, and I can introduce you to the real person inside."
    cherie.say "And I feel that there is much we have yet to discover about each other, no?"
    menu:
        "I want to get to know the real you":
            mike.say "You took the words right our of my mouth, Cherie."
            mike.say "Like, I want to find out all about you, what really makes you tick."
            mike.say "And I want to have you do the same thing with me too."
            cherie.say "Do not worry, {i}mon ami{/i}, we have all the time in the world."
            cherie.say "And I think that before too long, we will know each other from the inside out!"
            $ cherie.love += 1
        "I think boundaries are important":
            mike.say "I'm all for getting to know you better, Cherie."
            mike.say "But I think we need to have strong boundaries in place first."
            mike.say "It's important that neither of us impinges on the other's personal space."
            cherie.say "My goodness, what passion you have!"
            cherie.say "And the heart of a meek, little mouse too..."
            $ cherie.love -= 1
        "I want to be the person you need me to be":
            mike.say "I want to find out all there is to know about you, Cherie..."
            mike.say "Because I plan on being the only person that you need from now on."
            mike.say "I want to mould myself to your needs and give you whatever you desire!"
            cherie.say "You...you would do that...for me?!?"
            cherie.say "{i}Mon ami{/i}, nobody has ever offered so much of themselves to me!"
            $ cherie.sub -= 1
    return

label cherie_love_4_male:
    cherie.say "Often I stop and reflect on how thankful I am for your friendship, {i}mon ami{/i}."
    cherie.say "I do not say this lightly, but I think I could not have coped without you."
    cherie.say "And now I would not be able to imagine my life going on without you as a part of it."
    menu:
        "I feel the same way about you":
            mike.say "It really moves me to hear you admit that, Cherie."
            mike.say "And I have to confess that...that I feel the same way about you."
            mike.say "I feel that you've become way more than just a friend to me."
            cherie.say "Oh, [hero.name] - I feel that way too!"
            cherie.say "I was just afraid to be the one to say it first."
            $ cherie.love += 1
        "You're strong so you would have coped":
            mike.say "I'm flattered by that, Cherie - but I don't think I'm anything special."
            mike.say "You're a strong, independent woman, and you just needed reminding of that."
            mike.say "I think you'd have made it through in the end either way."
            cherie.say "I...I suppose I should thank you for the compliment, {i}mon ami{/i}."
            cherie.say "Even if you are deaf to the message I was trying to impart..."
            $ cherie.love -= 1
        "Fate delivered you into my hands and now I won't let go":
            mike.say "You might say that it was fate delivering you into my hands, Cherie."
            mike.say "And now that I have you, there's no way I'm ever going to let go again."
            mike.say "Because you know that you need me, that you couldn't cope without me."
            cherie.say "Alas, {i}mon ami{/i}, I fear that you are right."
            cherie.say "I am more yours than I have ever been the property of another man!"
            $ cherie.sub += 1
    return

label cherie_love_5_male:
    cherie.say "I cannot keep my feeling inside of me for one moment longer."
    cherie.say "I am in love with you, {i}mon ami{/i}, mind, body and soul!"
    cherie.say "And whether or not you feel the same way, I must speak the words openly."
    menu:
        "I love you too" if hero.charm >= 75:
            mike.say "Oh, Cherie - I love you too, more than my own life!"
            mike.say "I've wanted to say so for so long now it hurts."
            mike.say "And I can't believe you were doing the same this whole time."
            cherie.say "Ah, {i}mon ami{/i}, we are both fools for love."
            cherie.say "But now, at least we will be fools together."
            $ cherie.love += 1
        "Do you have to be so dramatic":
            mike.say "Cherie, settle down before someone complains!"
            mike.say "Look, I like you too - a lot, and you know that."
            mike.say "But you can't go around behaving like that in public!"
            cherie.say "You are more concerned with being embarrassed than with true love?!?"
            cherie.say "Is your heart really nothing more than a cold, dead piece of coal?"
            $ cherie.love -= 1
        "I want to devote the rest of my life to you":
            mike.say "I love you too, Cherie - more than you can possibly know."
            mike.say "In fact, I want to spend the rest of my life making you happy."
            mike.say "Just tell me what it is that you want, and I'll do it - anything at all!"
            cherie.say "{i}Mon ami{/i}, this is so big of a thing to offer me."
            cherie.say "I will have to think about it...but I am sure I will come up with something."
            $ cherie.sub -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
