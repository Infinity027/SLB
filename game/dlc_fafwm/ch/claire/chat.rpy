label claire_desire_0_male:
    claire.say "I'm glad you feel like you can talk to me, [hero.name]."
    claire.say "When you're a woman of my age, so many guys seem to see right through you."
    claire.say "They either just assume I'm married or won't have time for them."
    claire.say "But not you - you're different."
    menu:
        "So are you, Claire" if hero.charm >= 50:
            mike.say "I think that's because I really know you, Claire."
            mike.say "And it's not just because you're my friend's step-mom either."
            mike.say "You're an interesting person in your own right."
            claire.say "You really think so?"
            claire.say "I guess you do see me."
            $ claire.love += 1
        "Well, I have known you a very long time":
            mike.say "Maybe that's just because I've known you for so long, Claire?"
            mike.say "I kind of grew up around you, remember?"
            mike.say "So I'm bound to know you better than the average guy."
            claire.say "Ah...thanks for that."
            claire.say "You're really reminding me how old I am right now!"
            $ claire.love -= 1
        "I know you're older, but that doesn't matter to me":
            mike.say "I know most guys would get hung up on the age difference, Claire."
            mike.say "But not me - because I like the you that's on the inside."
            mike.say "No matter how much time changes you, that always stays the same."
            claire.say "Do you..."
            claire.say "Do you really think I'm that old?"
            $ claire.sub += 1
        "I'm always willing to listen to you, Claire":
            mike.say "I always love talking to you, Claire."
            mike.say "And knowing that you want to talk to me..."
            mike.say "Well, it always made me feel like I was so special - dumb as that sounds!"
            claire.say "Oh no, [hero.name]..."
            claire.say "It's sweet!"
            $ claire.sub -= 1
    return

label claire_desire_1_male:
    claire.say "This is going to sound crazy, [hero.name] - but I think I'm a stereotype."
    claire.say "Like the mom in the film that's all about the teenagers."
    claire.say "Where she's still kind of hot and some of them quite like her!"
    menu:
        "That's really weird, we always thought the same thing" if hero.charm >= 50:
            mike.say "You're not going to believe this, Claire..."
            mike.say "But behind Adam's back, that's how we all saw you!"
            mike.say "Oh...I hope you don't find that offensive?"
            claire.say "Offensive?!?"
            claire.say "Oh no, it's very...very flattering."
            $ claire.love += 1
        "Nah, that's just a Hollywood thing":
            mike.say "I don't think you've got anything to worry about, Claire."
            mike.say "Adam and me were too busy checking out the girls our own age back then."
            mike.say "That whole 'best friend's mom' thing is just a Hollywood thing."
            claire.say "Is it really?"
            claire.say "Well thanks for putting me straight on that one."
            $ claire.love -= 1
        "Those are just exploitative stereotypes":
            mike.say "You shouldn't base your image of yourself on films, Claire."
            mike.say "At the best they're going to be totally naive and silly."
            mike.say "And at the worst, you're setting yourself up to be exploited."
            claire.say "Oh yeah..."
            claire.say "I guess you've got a point."
            $ claire.sub += 1
        "I always knew you saw yourself that way":
            mike.say "You know I always thought you saw yourself that way, Claire."
            mike.say "Like, you were the older woman that secretly wanted a younger guy."
            mike.say "You never wanted to have to be mature or in charge in your relationships."
            claire.say "Oh...I never thought of it that way."
            claire.say "But now that you come to mention it - that makes a lot of sense."
            $ claire.sub -= 1
    return

label claire_desire_2_male:
    claire.say "I know you shouldn't expect life to be a fairytale, [hero.name]."
    claire.say "But even knowing that, Hector kind of turned out to be a disappointment."
    claire.say "Sometimes I think he saw me as more of a domestic servant than a wife!"
    menu:
        "That guy never appreciated you" if hero.charm >= 50:
            mike.say "I know it's easy for me to stick the boot into that guy."
            mike.say "But what kind of a chump would treat you like that, Claire?"
            mike.say "You're, like, what every guy should dream of in a wife!"
            claire.say "Oh, [hero.name] - you really think so?"
            claire.say "Hector never gave me compliments like that!"
            $ claire.love += 1
        "Life isn't all fun and games":
            mike.say "This might not be the answer you're looking for, Claire."
            mike.say "But sometimes life isn't all fun and games, you know?"
            mike.say "You have to learn to ride out the bad times."
            claire.say "Huh...that sounds familiar."
            claire.say "Just like what Hector used to say!"
            $ claire.love -= 1
        "That won't happen if you're mine":
            mike.say "Well then he was a total moron, Claire!"
            mike.say "If a woman devoted herself to me, like a wife should..."
            mike.say "Then I'd make her feel like a total goddess."
            claire.say "You...you'd do that?"
            claire.say "So, tell me more about what devoting myself to you would entail..."
            $ claire.sub += 1
        "I think you were just too much for him":
            mike.say "Did you ever think it was because you intimidated him, Claire?"
            mike.say "Like, he wasn't man enough to realise that you were the one in charge?"
            mike.say "Because I'm not that guy - I totally get that you're an alpha female."
            claire.say "You think I should be the one in charge?"
            claire.say "Well, that would be an interesting thing to try..."
            $ claire.sub -= 1
    return

label claire_desire_3_male:
    claire.say "There are so many other wives and mothers in the neighbourhood that have just given up on life."
    claire.say "But I promised myself a long time ago that I wasn't just going to settle for comfort and stability."
    claire.say "That if the chance came along for something that was passionate and real, I'd grab it - and damn the consequences!"
    menu:
        "You have to grab the bull by the horns" if hero.charm >= 50:
            mike.say "I couldn't agree more, Claire - you'd be giving up if you did anything else."
            mike.say "Who wants to spend the rest of their life comfortable and secure, but totally bored."
            mike.say "That's only one step away from actually being dead!"
            claire.say "So you agree with me, [hero.name]?"
            claire.say "Maybe I've found someone I can live my philosophy with?"
            $ claire.love += 1
        "That's a good way to end up in the gutter":
            mike.say "I don't know if I'd be as bold as that, Claire."
            mike.say "There's a lot to be said for having stability in your life."
            mike.say "It might not be exciting, but it's guaranteed to be there when you need it."
            claire.say "So you don't share my take on this one, [hero.name]?"
            claire.say "Probably a good thing I found out now, rather than further down the line."
            $ claire.love -= 1
        "For that to work, you need to devote yourself to someone":
            mike.say "Sounds like what you really need is a strong, dynamic man in your life, Claire."
            mike.say "If that were me, I'd make sure that you were never bored, not for a moment."
            mike.say "But the flip-side would be that you'd need to be totally devoted to me, to do whatever I asked of you."
            claire.say "You'd really do that for me?"
            claire.say "In that case, doing as I'm told doesn't sound too hard..."
            $ claire.sub += 1
        "I love it when you take charge like that":
            mike.say "I love it when you talk like that, Claire..."
            mike.say "Like, you know exactly what you want, and I just know you're going to get it too."
            mike.say "And if you wanted me - I wouldn't be able to say no!"
            claire.say "Is that a fact?"
            claire.say "Well then, I might have to think about making certain demands of you..."
            $ claire.sub -= 1
    return

label claire_desire_4_male:
    claire.say "Oh, [hero.name] - I hate living out here in the suburbs, so far away from you!"
    claire.say "Maybe I could get a place in the city, or come stay with you more often?"
    claire.say "Or perhaps we could see if there's somewhere around here we could afford together?"
    menu:
        "We do need to sort out your living arrangements" if hero.charm >= 50:
            mike.say "I know how you feel, Claire - we're way too far apart right now."
            mike.say "I think we should do whatever gets you closer to me soonest."
            mike.say "Then we can think about a more long-term solution."
            claire.say "That works for me, [hero.name]..."
            claire.say "I already packed my overnight bag!"
            $ claire.love += 1
        "I think we need to take things slowly":
            mike.say "Hold your horses, Claire - this is a big decision."
            mike.say "We need to be sure of everything before we commit."
            mike.say "Make sure we're both on the same page, you know?"
            claire.say "On the same page?!?"
            claire.say "I'm starting to wonder if we're even reading the same book!"
            $ claire.love -= 1
        "I want you close by and on call":
            mike.say "I think that's a great idea, Claire - so long as you're there when I need you."
            mike.say "Maybe the best thing would be if I moved you into a room in the house with me?"
            mike.say "That way I can handle all of the legal arrangements and be in charge of everything."
            claire.say "That would make things simpler for me, [hero.name]..."
            claire.say "Anything to be closer to you!"
            $ claire.sub += 1
        "I'll go wherever you tell me to":
            mike.say "Just tell me what works best for you, Claire."
            mike.say "I'll move somewhere in the city or come back to the suburbs if that's what it takes."
            mike.say "Anything to be closer to you!"
            claire.say "Well, I am kind of settled here in the sticks."
            claire.say "So maybe it makes more sense to do things that way."
            $ claire.sub -= 1
    return

label claire_desire_5_male:
    claire.say "Hector never even spoke about his feelings when we were together, and I got into the same habit too."
    claire.say "But I'm not going to let the same thing happen to us, [hero.name]."
    claire.say "I want you, and I need you - those are things I'm never going to apologise for saying out loud!"
    menu:
        "Let's make the whole world hear our love" if hero.charm >= 50:
            mike.say "We're going to broadcast it to the world, Claire..."
            mike.say "Wherever we go, people are going to know how we feel about each other."
            mike.say "And if they don't like it, then...then they can go to hell!"
            claire.say "Oh, [hero.name], you're so passionate and alive!"
            claire.say "Just being with you makes me come over all funny."
            $ claire.love += 1
        "Would you mind toning it down a little?":
            mike.say "I hate to admit it, Claire..."
            mike.say "But Hector might have had a point, just this once."
            mike.say "There's no need to shove what we have in everyone's faces."
            claire.say "I hate it when you take Hector's side."
            claire.say "Because you sound just like him!"
            $ claire.love -= 1
        "So long as you remember to always do as you're told":
            mike.say "It really makes me happy to see you happy, Claire."
            mike.say "But just remember, that happiness is based on you doing as you're told."
            mike.say "So long as you keep doing that, you get to keep me happy."
            claire.say "Oh...oh yes, [hero.name], of course!"
            claire.say "Your happiness is the source of my happiness too."
            $ claire.sub += 1
        "I'll never hide just how much I love you":
            mike.say "I'll never hide how much I love you, Claire..."
            mike.say "As long as that's what you want, I'll proclaim it to the world."
            mike.say "Or if you like, I'll keep it the most precious of secrets."
            claire.say "Oh, [hero.name], aren't you just the sweetest?"
            claire.say "And the most obedient too!"
            $ claire.sub -= 1
    return

label claire_love_0_male:
    claire.say "I don't know if I'll ever really understand love, [hero.name]."
    claire.say "I mean, I thought that I was in love with Hector when we first met."
    claire.say "But it didn't take me long to realise that whatever we had wasn't really what I thought it was."
    menu:
        "I think love is hard to define":
            mike.say "Love's never looked or felt like what you see in the movies or hear about in songs to me."
            mike.say "I think that it might mean different things for different people."
            mike.say "Maybe look and feel different for them too, you know?"
            claire.say "That's really interesting, [hero.name]..."
            claire.say "Makes me think you could love different people in different ways."
            $ claire.love += 1
        "I don't think most people know what love is":
            mike.say "I don't think most people really know what love is, Claire."
            mike.say "Like, they think it's something they've seen in a movie or heard about in a song."
            mike.say "Maybe what you had with Hector really was love, but you just didn't recognise it."
            claire.say "You know what, [hero.name]..."
            claire.say "Sometimes I wonder if you're even listening to me at all!"
            $ claire.love -= 1
        "I'll help you learn what love is":
            mike.say "Sounds like you just need to learn to recognise love, Claire."
            mike.say "But don't worry, you have me in your life now."
            mike.say "I'll help you to spot it in future."
            claire.say "You'd do that for me?"
            claire.say "You're a good friend, [hero.name]."
            $ claire.sub += 1
        "I'm even more clueless when it comes to love":
            mike.say "It scares me when you say things like that, Claire."
            mike.say "Because I always thought you knew so much more than me."
            mike.say "But if you don't, then what chance have I got?"
            claire.say "Oh, you poor thing!"
            claire.say "Maybe I need to focus my thoughts, if only for your sake?"
            $ claire.sub -= 1
    return

label claire_love_1_male:
    claire.say "I just wanted to thank you for being there for me recently, [hero.name]."
    claire.say "I seem to have lost contact with most of my old friends, and Hector's no help."
    claire.say "So your calls and messages have been like a ray of light in the darkness."
    menu:
        "It's been my pleasure to chat to you":
            mike.say "I hope you don't think I was doing it out of pity or obligation, Claire?"
            mike.say "Because chatting with you has been really cheering me up too."
            mike.say "I feel like I've found myself a totally new friend!"
            claire.say "You really mean that?"
            claire.say "Then it's decided - we're definitely best friends!"
            $ claire.love += 1
        "I just thought you could use a boost":
            mike.say "Don't mention it, Claire, it was really nothing."
            mike.say "I just saw that you were feeling down, you know?"
            mike.say "I'd have done the same thing for anyone else."
            claire.say "Oh...is that so?"
            claire.say "Well, at least I know where I stand."
            $ claire.love -= 1
        "I know how isolated you are right now":
            mike.say "I know how isolated a woman in your position can become, Claire."
            mike.say "And part of me wonders if I might be your only real friend right now."
            mike.say "But if that's the case, then I want you to know I'm here for you."
            claire.say "That means a lot, [hero.name]..."
            claire.say "More than you can know!"
            $ claire.sub += 1
        "Your messages have become the highlight of my day":
            mike.say "It's been my pleasure to be able to chat with you, Claire."
            mike.say "In fact, your messages have become the highlight of my day!"
            mike.say "Like, I keep checking my phone all the time for the next one."
            claire.say "Really, [hero.name] - they mean that much to you?"
            claire.say "I had no idea I was that big a part of your life."
            $ claire.sub -= 1
    return

label claire_love_2_male:
    claire.say "Part of me still can't believe that you were once just my stepson's friend to me."
    claire.say "But now you've become so much more than that, a friend in your own right."
    claire.say "And maybe, dare I say it - something more than that?"
    menu:
        "I always wanted more":
            mike.say "Don't take this the wrong way, Claire - but I always wanted to know you."
            mike.say "But now that I do...well, I feel like I want more than just friendship too."
            mike.say "Just chatting and sharing the occasional message isn't enough!"
            claire.say "Oh, [hero.name], you're making me hot under the collar!"
            claire.say "Just knowing that we want the same thing."
            $ claire.love += 1
        "I think we need to take things slowly":
            mike.say "I really do think of you as a friend, Claire."
            mike.say "But I think we need to work on that before we become more."
            mike.say "Otherwise we could go too far too fast."
            claire.say "Oh...I see."
            claire.say "Sure, [hero.name], we can take it slowly."
            $ claire.love -= 1
        "You always knew we were going to be more":
            mike.say "You think I didn't see the way you used to look at me, Claire?"
            mike.say "I never said anything, but I always knew that you wanted me."
            mike.say "And when we became friends, I knew it'd only be a matter of time until it turned into more."
            claire.say "Oh, [hero.name]...you knew?"
            claire.say "I...I feel like you have me in the palm of your hand!"
            $ claire.sub += 1
        "I always wanted to be in your power":
            mike.say "Don't take this the wrong way, Claire - but I always hoped you wanted me!"
            mike.say "I longed for you to just reach out and claim me as your own."
            mike.say "And if you do that now, then I won't be able to resist you - not for a second."
            claire.say "[hero.name], you're serious - you'd give yourself to me?"
            claire.say "Then maybe I should take what's on offer!"
            $ claire.sub -= 1
    return

label claire_love_3_male:
    claire.say "Doesn't it feel good to be just Claire and [hero.name]?"
    claire.say "We're not a stepmom and her stepson's friend anymore."
    claire.say "Now we get to learn all about who the other person really is!"
    menu:
        "I always thought there was much more to you":
            mike.say "I always wanted to know who you really were, Claire."
            mike.say "Not Adam's mom or Hector's wife - the real Claire beyond all of that."
            mike.say "And I feel like I'm going to have so much fun finding out too!"
            claire.say "You really think so?"
            claire.say "Ooh...I hope she's all you expected, and more!"
            $ claire.love += 1
        "Is the real you still in there?":
            mike.say "I've got to admit, Claire - that does worry me."
            mike.say "Because I don't know if the real you is still in there."
            mike.say "Like, what if she got used up looking after Adam and Hector?"
            claire.say "Well that's not a very nice thing to say, is it?"
            claire.say "You make me sound like a dried-up old husk!"
            $ claire.love -= 1
        "Now we can have the relationship I always wanted":
            mike.say "We could never really connect before, Claire - not in the way I wanted to."
            mike.say "But now all of that's behind us, I can make sure we have the relationship I always desired."
            mike.say "And I can start to bring out the parts of you that Adam and Hector always made you hide."
            claire.say "That sounds...kind of scary..."
            claire.say "Scary, but exciting!"
            $ claire.sub += 1
        "I want to be more than just your friend, mistress":
            mike.say "I want to be far more than just your friend, Claire."
            mike.say "And I want to give more of myself to you than just my friendship."
            mike.say "In fact, I want to give myself to you totally - if you'll let me?"
            claire.say "That's a lot to give a girl, [hero.name]!"
            claire.say "But I really like the idea of giving it a try."
            $ claire.sub -= 1
    return

label claire_love_4_male:
    claire.say "I don't think I could have made it through everything that's happened without you, [hero.name]."
    claire.say "Hector's been a dead loss, and Adam's sweet - but he's my stepson, and nothing more than that to me."
    claire.say "But you...well, you've been a friend, a shoulder to cry on - you've been my rock!"
    menu:
        "And I always will be":
            mike.say "I've just tried to be the best friend that I could, Claire."
            mike.say "And I'll always be there for you, whenever you need me to be."
            mike.say "Because I can't imagine my life without you in it now."
            claire.say "Oh, [hero.name] - I don't deserve you!"
            claire.say "But I don't know what I'd do without you."
            $ claire.love += 1
        "You were just going through a bad patch, that's all":
            mike.say "Ah, don't get yourself all bent out of shape, Claire."
            mike.say "We all go through a rough-patch now and then."
            mike.say "I didn't do anything for you I wouldn't have done for any of my other friends."
            claire.say "Oh...I see."
            claire.say "I seem to have misread the situation, don't I?"
            $ claire.love -= 1
        "It's okay, I know how much you need me":
            mike.say "It's okay, Claire, I can see how hard this has been on you."
            mike.say "And helping to build you back up has been my pleasure, really."
            mike.say "But I know how shaky you still are, even though you try so hard to hide it."
            claire.say "You...you noticed that?"
            claire.say "Oh, [hero.name], you seem to know me better than I know myself!"
            $ claire.sub += 1
        "It was you that pulled me through!":
            mike.say "What are you talking about, Claire?"
            mike.say "You were the one that kept me going!"
            mike.say "I don't know if I'd even be here were it not for you."
            claire.say "Wow, [hero.name]..."
            claire.say "I didn't realise how hard you'd fallen for me!"
            $ claire.sub -= 1
    return

label claire_love_5_male:
    claire.say "I've spent too many years of my life not being honest about my feelings, [hero.name]."
    claire.say "So I'm not going to waste another moment being anything other than totally open."
    claire.say "And that starts with admitting, out loud, that I am one hundred percent in love with you!"
    menu:
        "Me too, so let's tell the whole world":
            mike.say "You don't know how good it feels to hear you say that, Claire!"
            mike.say "Because I can feel the love I have for your bursting out of me."
            mike.say "And if I keep it in any longer, I might just explode!"
            claire.say "Oh, [hero.name], we can't have that."
            claire.say "I want all of your love to explode over me!"
            $ claire.love += 1
        "Could you be just a little more discreet?":
            mike.say "That's all very nice, Claire, and I'm happy for you."
            mike.say "But do you have to put on such a performance in public?"
            mike.say "I'm kind of a private guy, you know!"
            claire.say "You call that private?"
            claire.say "Repressed is what I call it!"
            $ claire.love -= 1
        "Of course you do, it's only natural":
            mike.say "Well of course you do, Claire, it's only natural."
            mike.say "Falling for me tends to have that effect on a girl."
            mike.say "And doesn't it look adorable on you too?"
            claire.say "It...it does?"
            claire.say "Oh god...why am I blushing so much?"
            $ claire.sub += 1
        "No, I should be the one shouting it out loud!":
            mike.say "Save your voice, Claire - I should be the one shouting it out!"
            mike.say "I should be telling the whole world that I'm the luckiest guy in the world."
            mike.say "Because I caught the eye of the most beautiful woman in the whole world!"
            claire.say "Oh, [hero.name], you say that with such conviction too."
            claire.say "So much so that I'm starting to believe it as well..."
            $ claire.sub -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
