label ryan_talk_love_female:
    if randint(1, 3) == 3:
        bree.say "You've done the marriage thing, Ryan."
        bree.say "And nobody gets into something like that unless they're serious."
        bree.say "So I guess that means you're a true believer, right?"
        bree.say "Like you believe in true love?"
        ryan.say "Sure I believe in love, [hero.name]."
        ryan.say "In fact, I've got more love to give than anyone I've ever met!"
        ryan.say "So much that it's more than I can give to just one person..."
        $ ryan.love += 1
    else:
        if ryan.sub >= 50:
            "I'm not sure a guy can love just one woman, [hero.name] - that sounds like too much of a challenge!"
        elif ryan.sub <= -50:
            ryan.say "It's so boring and old-fashioned to think a man has to love one woman at a time."
        else:
            ryan.say "People have such a narrow view of what love is - like you can only love one girls at a time."
        menu:
            "No love without some freedom":
                if hero.morality >= 25:
                    bree.say "Oh, I never thought about it like that, Ryan - please, tell me more?"
                elif hero.morality <= -25:
                    bree.say "That's what I've been saying, Ryan - if it feels good, then how can it be wrong?"
                else:
                    bree.say "Yeah, I think people are too narrow-minded about love - it shouldn't be oppressed like that."
                $ ryan.love += 1
            "No love without some exclusivity":
                if hero.morality >= 25:
                    bree.say "Oh no, Ryan - that's the kind of thinking that breaks hearts!"
                elif hero.morality <= -25:
                    bree.say "Yeah, that's just a fancy way of saying you're a slut, Ryan!"
                else:
                    bree.say "Yeah, I get Sam didn't bite when you sold her that line either!"
                $ ryan.love -= 1
            "You have some things to learn about love":
                if hero.morality >= 25:
                    bree.say "Sounds like you don't know what you really want, Ryan!"
                elif hero.morality <= -25:
                    bree.say "Oh, Ryan - you're going to learn so much from me when it comes to the bedroom!"
                else:
                    bree.say "Don't worry, Ryan - I'll teach you what love's really all about."
                $ ryan.sub += 1
            "Surely you have things to share":
                if hero.morality >= 25:
                    bree.say "I don't know much about that kind of thing, Ryan - will you teach me?"
                elif hero.morality <= -25:
                    bree.say "If it involves more horizontal fun, I'm totally up for it!"
                else:
                    bree.say "Sounds like you know what you're talking about, Ryan!"
                $ ryan.sub -= 1
        return

label ryan_talk_sex_female:
    if randint(1, 3) == 3:
        bree.say "It's so romantic to be married to somebody that you love!"
        bree.say "But there is one thing that worries be about it, Ryan..."
        ryan.say "Oh...what's that, [hero.name]?"
        bree.say "Well...it's being with one person all that time."
        bree.say "I'm worried that things might boring...in the bedroom!"
        ryan.say "There's an easy answer to that, [hero.name]."
        ryan.say "You have to keep things fresh in that department."
        ryan.say "Different places, different positions - even different people!"
        $ ryan.love += 1
    else:
        if ryan.sub >= 50:
            ryan.say "I...I don't think Sam ever really understood my needs, [hero.name] - specifically my sexual needs, you know?"
        elif ryan.sub <= -50:
            ryan.say "Sam never really understood my sexual needs, [hero.name] - so she could never satisfy them either."
        else:
            ryan.say "I think I have greater sexual needs than the average guy, [hero.name] - Sam never really got that."
        menu:
            "It is important to take care of the partner's needs":
                if hero.morality >= 25:
                    bree.say "I don't know much about that kind of thing, Ryan - but I'm more than willing to learn."
                elif hero.morality <= -25:
                    bree.say "Well you don't need to worry about that with me, Ryan - I'm pretty insatiable too!"
                else:
                    bree.say "Those are big words, Ryan - I wonder if you can back them up?"
                $ ryan.love += 1
            "Self-centeredness is not a good starting point":
                if hero.morality >= 25:
                    bree.say "Really, Ryan - that doesn't sound like a very caring way to be!"
                elif hero.morality <= -25:
                    bree.say "Huh...maybe she just didn't have an appetite for what you were serving up?"
                else:
                    bree.say "Did you ever stop to think about her appetites, Ryan?"
                $ ryan.love -= 1
            "I think I can manage that":
                if hero.morality >= 25:
                    bree.say "Oh, Ryan - you really need to learn to keep it in your trousers!"
                elif hero.morality <= -25:
                    bree.say "Oh dear, you're really out of your depth, aren't you, Ryan?"
                else:
                    bree.say "Yeah, well maybe Sam should have kept you on a tighter leash!"
                $ ryan.sub += 1
            "I will try not to make the same mistake":
                if hero.morality >= 25:
                    bree.say "I don't know if I can meet your needs, Ryan - but I'll try my best!"
                elif hero.morality <= -25:
                    bree.say "If you want to be satisfied, you've come to the right girl!"
                else:
                    bree.say "Will you let me try to meet those needs, Ryan?"
                $ ryan.sub -= 1
    return

label ryan_talk_politics_female:
    if randint(1, 3) == 3:
        bree.say "Nobody seems to want to talk about politics, Ryan."
        bree.say "And I can kind of understand their reasons, you know?"
        bree.say "For most people, politics is almost as sensitive of a subject as religion!"
        ryan.say "Huh...I just don't get that, [hero.name]!"
        ryan.say "I don't care what other people think of my politics."
        ryan.say "And I don't care about their opinions either."
        ryan.say "For me, it's not about debating."
        ryan.say "It's more like explaining why they're wrong and I'm right!"
        $ ryan.love += 1
    else:
        if ryan.sub >= 50:
            ryan.say "I don't really do one side or the other in politics, [hero.name] - I think they're both as bad as each other."
        elif ryan.sub <= -50:
            ryan.say "I don't listen to either side in political debates, [hero.name] - I make up my own mind."
        else:
            ryan.say "I don't like to limit myself in terms of my politics - I think for myself."
        menu:
            "Distrust is the right move":
                if hero.morality >= 25:
                    bree.say "Either side could be wrong, so I guess that makes sense."
                elif hero.morality <= -25:
                    bree.say "Ah, they're all just degenerates and crooks, Ryan - you're right not to trust them!"
                else:
                    bree.say "Politicians are all the same, Ryan - so why would you trust any of them?"
                $ ryan.love += 1
            "Sometimes, someone has to stanp up":
                if hero.morality >= 25:
                    bree.say "Hmm...but sometimes they do make good points - you could miss out on that by not listening."
                elif hero.morality <= -25:
                    bree.say "Huh...most guys who say that are just easy - like, morally loose!"
                else:
                    bree.say "Some people don't have a choice but to choose a side, Ryan - you're pretty privileged in that you can stay neutral!"
                $ ryan.love -= 1
            "It is just about power":
                if hero.morality >= 25:
                    bree.say "Hmm...that does sound like something you'd say if you didn't really understand the issues, Ryan!"
                elif hero.morality <= -25:
                    bree.say "Urgh...there's nothing that kills my libido more than ignorance and apathy!"
                else:
                    bree.say "Yeah, it's easy to stay neutral when you're ignorant about reality, Ryan!"
                $ ryan.sub += 1
            "Such a wise man":
                if hero.morality >= 25:
                    bree.say "That sounds really interesting, Ryan - will you tell me more?"
                elif hero.morality <= -25:
                    bree.say "Now that's what I love - a man with all the angles covered!"
                else:
                    bree.say "Sounds like you've got both sides figured out, Ryan."
                $ ryan.sub -= 1
    return

label ryan_talk_food_female:
    if randint(1, 3) == 3:
        bree.say "Urgh..."
        bree.say "I hate all of those old stereotypes about women, Ryan!"
        bree.say "Like we're supposed to be able to cook and clean to keep house."
        bree.say "I want people to make dinner for me, not the other way round!"
        ryan.say "Ha, ha..."
        ryan.say "No need to worry about that around me, [hero.name]!"
        ryan.say "I'm better in the kitchen than anyone - man or woman!"
    else:
        bree.say "Mmm...I'm hungry, Ryan - let's eat!"
        if ryan.sub >= 50:
            ryan.say "You mind if I choose what we eat, [hero.name] - I have a delicate stomach, remember?"
        elif ryan.sub <= -50:
            ryan.say "We can eat now, on the condition that I get to choose what and where."
        else:
            ryan.say "So long as you let me choose, [hero.name] - I think I have slightly better taste than you!"
        menu:
            "I thrust your taste":
                if hero.morality >= 25:
                    bree.say "Of course you can choose, Ryan - I can't wait to see what's on the menu!"
                elif hero.morality <= -25:
                    bree.say "Whoa...check out mister big-balls - you'd better be able to make my mouth water, Ryan!"
                else:
                    bree.say "You're a big talker, Ryan - so let's see you put your money where your mouth is!"
                $ ryan.love += 1
            "Why shouldn't I eat what I want?":
                if hero.morality >= 25:
                    bree.say "Oh no, Ryan - I'm very strict about what I eat!"
                elif hero.morality <= -25:
                    bree.say "Get lost, Ryan - I say what goes in this mouth, and nobody else!"
                else:
                    bree.say "You have to be kidding - I get to veto anything I don't like!"
                $ ryan.love -= 1
            "Follow my lead... I'm a woman of wealth and taste ":
                if hero.morality >= 25:
                    bree.say "Hmm...I think you should let me choose - you look like you need to eat something nourishing."
                elif hero.morality <= -25:
                    bree.say "Let me choose, Ryan - I know what feels good inside of you!"
                else:
                    bree.say "Nah, I think I'll choose - you look too pasty to be eating right!"
                $ ryan.sub += 1
            "Your certainly know what you're talking about":
                if hero.morality >= 25:
                    bree.say "Hmm...maybe I could use some advice on a healthy diet?"
                elif hero.morality <= -25:
                    bree.say "Well the last thing you put inside me felt amazing - so who am I to argue?"
                else:
                    bree.say "You're in pretty good shape, Ryan - so I'll take your advice."
                $ ryan.sub -= 1
    return

label ryan_talk_travels_female:
    if randint(1, 3) == 3:
        bree.say "You sound like a pretty cultured guy, Ryan."
        bree.say "Did you read all about stuff in books?"
        bree.say "Or have you actually been to places for real?"
        ryan.say "Oh, please, [hero.name]!"
        ryan.say "Of course I've been places for real!"
        ryan.say "But then how would you know that?"
        ryan.say "It's obvious that you've never been anywhere at all!"
        $ ryan.love -= 1
    else:
        if ryan.sub >= 50:
            ryan.say "Sam and I saw a lot of different places - would you like to visit them with me too?"
        elif ryan.sub <= -50:
            ryan.say "I saw a lot of places with Sam, but now I get to make new memories when I go back there with you."
        else:
            ryan.say "I saw a lot of places with Sam, but now I want to revisit them with you, [hero.name]."
        menu:
            "Travelling is great":
                if hero.morality >= 25:
                    bree.say "Travelling is one of my favourite things, Ryan - we're going to have so much fun together!"
                elif hero.morality <= -25:
                    bree.say "There are so many places I've never made love in, Ryan - let's change that together!"
                else:
                    bree.say "There are so many places in the world that I want to see - you think we can do all of them?"
                $ ryan.love += 1
            "Prefer to go where Sam's shadow is not":
                if hero.morality >= 25:
                    bree.say "Couldn't we go to different places, Ryan - make new memories of our own?"
                elif hero.morality <= -25:
                    bree.say "If you keep on talking about your ex, I'm gonna be really turned-off!"
                else:
                    bree.say "I dunno, Ryan - kind of sounds like you're just taking me to the same places you went with her!"
                $ ryan.love -= 1
            "I will make you forget her":
                if hero.morality >= 25:
                    bree.say "Aww...you need me to go back there with you, Ryan - to help heal those old wounds?"
                elif hero.morality <= -25:
                    bree.say "Just wait until we make love there, Ryan - you'll soon forget all about that frigid bitch!"
                else:
                    bree.say "Sounds like you're still nursing some trauma there, Ryan - but don't worry, I can help with that."
                $ ryan.sub += 1
            "You can be my guide":
                if hero.morality >= 25:
                    bree.say "You'll have to be my guide to all of these places, Ryan - I've never travelled that far!"
                elif hero.morality <= -25:
                    bree.say "Ooh...I want to learn all about those places - and how they do it there too!"
                else:
                    bree.say "Will you show me those places, Ryan - I've never been far from home before."
                $ ryan.sub -= 1
    return

label ryan_talk_tv_female:
    if randint(1, 3) == 3:
        bree.say "I can't wait to get home and watch some TV, Ryan!"
        bree.say "It's like the BEST way to unwind after a long, hard, day!"
        ryan.say "I should have guessed you'd be a couch-potato, [hero.name]!"
        ryan.say "You'd never catch me vegetating in from of the TV."
        ryan.say "I've got far better things to do with my time!"
        $ ryan.love -= 1
    else:
        bree.say "Ooh, I meant to say, Ryan - I've been watching this great new series on..."
        if ryan.sub >= 50:
            ryan.say "No point telling me, [hero.name] - I don't really like the rubbish on TV."
        elif ryan.sub <= -50:
            ryan.say "Let me stop you there, [hero.name] - I don't get on with the kind of garbage they show on TV!"
        else:
            ryan.say "Save your breath, [hero.name] - I don't bother with TV series."
        menu:
            "Maybe I should spent my time better":
                if hero.morality >= 25:
                    bree.say "Yeah, you're probably right - I watch too much TV anyway."
                elif hero.morality <= -25:
                    bree.say "Ah, forget about the TV series - we don't need it to have fun!"
                else:
                    bree.say "Come to think of it, that series is a little bit generic."
                $ ryan.love += 1
            "You should give it a chance":
                if hero.morality >= 25:
                    bree.say "You should really give it a chance, Ryan - you might like it."
                elif hero.morality <= -25:
                    bree.say "Hey, I get some of my best ideas for sexual positions from watching the TV!"
                else:
                    bree.say "You're way to quick to dismiss stuff, Ryan - it's kind of snobby, you know?"
                $ ryan.love -= 1
            "You should be more open minded":
                if hero.morality >= 25:
                    bree.say "Don't knock it until you've tried it, Ryan - that's very disappointing of you!"
                elif hero.morality <= -25:
                    bree.say "Huh...I bet you're as boring in the bedroom as you are in front of the TV!"
                else:
                    bree.say "Geez, Ryan, I didn't think you were that far up your own ass!"
                $ ryan.sub += 1
            "I should give up such trivialities":
                if hero.morality >= 25:
                    bree.say "Oh no...I didn't realise I was filling my head up with garbage!"
                elif hero.morality <= -25:
                    bree.say "You're right, Ryan - I should let you show me something more real...more...physical instead!"
                else:
                    bree.say "I just thought it was a bit formulaic - thanks for cluing me in, Ryan."
                $ ryan.sub -= 1
    return

label ryan_talk_sports_female:
    if randint(1, 3) == 3:
        bree.say "Most guys seem to love sports, Ryan."
        bree.say "Doesn't matter what kind of sport it is either."
        bree.say "They're just like sports, sports, sports!"
        ryan.say "Hmm..."
        ryan.say "I can't say that I identify with that aspect of so-called masculinity, [hero.name]."
        ryan.say "Most guys like that are just using sports to hide the fact they don't have a personality."
        ryan.say "That and a brain no bigger than a pebble too!"
    else:
        bree.say "You're a guy, Ryan - so you love sports, right?"
        if ryan.sub >= 50:
            ryan.say "Oh no, [hero.name] - I'm not into competitive sports!"
        elif ryan.sub <= -50:
            ryan.say "Nah, I'm not a team-player, [hero.name] - I'm an individual, a leader and not a follower!"
        else:
            ryan.say "Not me, [hero.name] - I'm more of an intellectual than a sportsman."
        menu:
            "I like free-spirited men":
                if hero.morality >= 25:
                    bree.say "That's really interesting, Ryan - and pretty deep too."
                elif hero.morality <= -25:
                    bree.say "That's good, Ryan - because I want you all to myself!"
                else:
                    bree.say "So you're more a thinker than a meat-head - I like that."
                $ ryan.love += 1
            "I like men in good shape":
                if hero.morality >= 25:
                    bree.say "Is that because you're too fragile, Ryan?"
                elif hero.morality <= -25:
                    bree.say "Shame, Ryan - I like a really manly man."
                else:
                    bree.say "Huh...I guess you're just not tough enough."
                $ ryan.love -= 1
            "I can get physical for both of us":
                if hero.morality >= 25:
                    bree.say "Don't worry about getting hurt, Ryan - I'll protect you!"
                elif hero.morality <= -25:
                    bree.say "Aww...don't worry, Ryan - I promise that I'll be gentle with you!"
                else:
                    bree.say "Yeah, Ryan, I get it - all those bodies flying around can be pretty scary!"
                $ ryan.sub += 1
            "Let's avoid that":
                if hero.morality >= 25:
                    bree.say "I don't like them either, Ryan - they scare me!"
                elif hero.morality <= -25:
                    bree.say "That suits me fine, Ryan - I want you one-on-one!"
                else:
                    bree.say "I get it, Ryan - you're more of a free-thinker, you don't like taking orders, right?"
                $ ryan.sub -= 1
    return

label ryan_talk_fashion_female:
    if randint(1, 3) == 3:
        bree.say "I think my wardrobe needs a bit of a refresh!"
        bree.say "It's starting to look like the clothes that time forgot!"
        ryan.say "I can't believe you girls are so obsessed with the latest trend, [hero.name]!"
        ryan.say "You should try to do what I do - make your look a timeless classic."
        ryan.say "That way you never have to worry about your wardrobe going out of fashion!"
        $ ryan.love -= 1
    else:
        if ryan.sub >= 50:
            ryan.say "I try not to be influenced by fashion, [hero.name] - I stick to the safe classics instead."
        elif ryan.sub <= -50:
            ryan.say "I keep my wardrobe timeless, [hero.name] - every last thing in there's a classic!"
        else:
            ryan.say "Fashion's for chumps, [hero.name] - if you stick to the classics, how can you ever be out of style?"
        menu:
            "That's why you have so much class":
                if hero.morality >= 25:
                    bree.say "That must make things far easier, Ryan - I guess you're pretty smart!"
                elif hero.morality <= -25:
                    bree.say "Just make sure those classics come off easily, and I'll be happy!"
                else:
                    bree.say "Yeah, I can see how that would make things far more simple."
                $ ryan.love += 1
            "You're confusing class and style ":
                if hero.morality >= 25:
                    bree.say "Oh, Ryan - you really don't know how out of fashion you really are!"
                elif hero.morality <= -25:
                    bree.say "The only stylish thing you own is your birthday suit!"
                else:
                    bree.say "Yeah, Ryan - that's a great way to end up dressing like a clown!"
                $ ryan.love -= 1
            "I am good at that":
                if hero.morality >= 25:
                    bree.say "You know, Ryan, if you want fashion advice, all you have to do is ask."
                elif hero.morality <= -25:
                    bree.say "Hah...you're like the emperor that was butt-naked in that story - you don't have a clue!"
                else:
                    bree.say "Yeah, that's what all the guys I know that don't have a clue say!"
                $ ryan.sub += 1
            "You could give me fashion advice":
                if hero.morality >= 25:
                    bree.say "Really, Ryan - then maybe you could strip down my wardrobe?"
                elif hero.morality <= -25:
                    bree.say "Okay, Ryan - tell me what to lose, and I'll take it off right now!"
                else:
                    bree.say "If you're that good, then you should come shopping with me in future!"
                $ ryan.sub -= 1
    return

label ryan_talk_books_female:
    if randint(1, 3) == 3:
        bree.say "You sound like a pretty smart guy, Ryan."
        bree.say "And that usually means you're pretty well-read too."
        bree.say "Got any hot picks on what I should be reading right now?"
        ryan.say "Ha, ha...that's so cute, [hero.name]!"
        ryan.say "You're right, of course - I am always reading."
        ryan.say "I practically devour books!"
        ryan.say "But the idea that you could keep up with me - now that is funny!"
        $ ryan.love += 1
    else:
        bree.say "Hey, Ryan, I'm looking for recommendations - read any good books latterly?"
        if ryan.sub >= 50:
            ryan.say "Oh no, [hero.name], I couldn't give you a recommendation - my reading material might be too complex for you."
        elif ryan.sub <= -50:
            ryan.say "I would, [hero.name], but it's too much of a chore - you see most people can't handle the level of complexity at which I read!"
        else:
            ryan.say "Oh, I never recommend people books, [hero.name] - they always come back complaining they were too much of a challenge!"
        menu:
            "You are so smart":
                if hero.morality >= 25:
                    bree.say "Wow...then I'd better go ask someone less intelligent, like [mike.name]!"
                elif hero.morality <= -25:
                    bree.say "Well, you should let me put you back in touch with your more basic, animal side!"
                else:
                    bree.say "Ouch...that must be tough on you, Ryan!"
                $ ryan.love += 1
            "You are not that smart":
                if hero.morality >= 25:
                    bree.say "Oh, Ryan - you're always trying to look so smart, it's really funny!"
                elif hero.morality <= -25:
                    bree.say "It's your body I'm after, not your brain!"
                else:
                    bree.say "Oh stop trying to show off, Ryan - you're not that smart!"
                $ ryan.love -= 1
            "Still, you are not smart enough":
                if hero.morality >= 25:
                    bree.say "I know what you're doing, Ryan - trying to seem clever to hide your basic feelings of inadequacy."
                elif hero.morality <= -25:
                    bree.say "Aww...if only your dick was as big as your ego, Ryan!"
                else:
                    bree.say "You know they say you have to be smart to worry you might be dumb, don't you, Ryan?"
                $ ryan.sub += 1
            "It must be hard being so smart":
                if hero.morality >= 25:
                    bree.say "Wow...it must be hard being so smart, so tiring to deal with dumb people."
                elif hero.morality <= -25:
                    bree.say "You handle the mental stuff, Ryan, and leave the physical side of things to me!"
                else:
                    bree.say "Maybe I could get on with the books you read if you explained them to me?"
                $ ryan.sub -= 1
    return

label ryan_talk_people_female:
    if randint(1, 3) == 3:
        bree.say "You seem to be the sociable type, Ryan."
        bree.say "Like you'll talk to anyone, no matter where you are."
        bree.say "So that must mean you're a real people-person, right?"
        ryan.say "Oh, [hero.name], [hero.name], [hero.name]...what am I going to do with you?"
        ryan.say "People are just like pet dogs."
        ryan.say "All you have to do is smile and pet them."
        ryan.say "And they think that means you love them!"
        $ ryan.love -= 1
    else:
        if ryan.sub >= 50:
            ryan.say "I don't think most people are very nice, [hero.name] - most of them are pretty awful."
        elif ryan.sub <= -50:
            ryan.say "You have to assert yourself over people, [hero.name] - otherwise they'll drain your energy with their negative qualities."
        else:
            ryan.say "Most people aren't worth the effort, [hero.name] - they're just out for themselves."
        menu:
            "People suck":
                if hero.morality >= 25:
                    bree.say "Thank you, Ryan - I hope you'll help me to spot those bad sorts?"
                elif hero.morality <= -25:
                    bree.say "That's good advice, Ryan - I'll reward you in bed tonight!"
                else:
                    bree.say "Yeah, Ryan - I think most people suck too."
                $ ryan.love += 1
            "People are not that bad":
                if hero.morality >= 25:
                    bree.say "That's awful, Ryan - I believe everyone is basically good!"
                elif hero.morality <= -25:
                    bree.say "You shouldn't judge a man until you've ridden a mile on his manhood!"
                else:
                    bree.say "That's a pretty negative attitude, Ryan - totally cynical!"
                $ ryan.love -= 1
            "There is trauma there":
                if hero.morality >= 25:
                    bree.say "Oh, Ryan - you must have been seriously hurt to think like that!"
                elif hero.morality <= -25:
                    bree.say "Ryan, you need some serious healing - of the sexual kind!"
                else:
                    bree.say "Geez, Ryan - you sound pretty damaged, like you need to talk to a therapist!"
                $ ryan.sub += 1
            "Avoiding people keep you safe":
                if hero.morality >= 25:
                    bree.say "Really, Ryan - if that's so, then I hope you'll help me avoid them?"
                elif hero.morality <= -25:
                    bree.say "I know, Ryan - will you protect me from them if I devote myself to you?"
                else:
                    bree.say "I know that lousy people drain me, Ryan - like, I want to avoid them!"
                $ ryan.sub -= 1
    return

label ryan_talk_computers_female:
    if randint(1, 3) == 3:
        bree.say "Do you work with computers, Ryan?"
        bree.say "Or do you just rely on them at home?"
        ryan.say "Urgh..."
        ryan.say "Computers are just machines, [hero.name]."
        ryan.say "They're just a way of getting things done."
        ryan.say "I can never understand why people are so obsessed with them!"
    else:
        bree.say "My laptop's playing up again."
        bree.say "I'm gonna take it to the electronics store - let that guy Shawn take a look at it."
        if ryan.sub >= 50:
            ryan.say "Let me look at it first, [hero.name] - those places will try to rip you off."
        elif ryan.sub <= -50:
            ryan.say "Those places are just scams, [hero.name] - they'll probably load your computer up with even more viruses!"
        else:
            ryan.say "I bet I can figure it out, [hero.name] - and I won't charge you for it either!"
        menu:
            "You can have a look":
                if hero.morality >= 25:
                    bree.say "Sure you can have a look, Ryan - be my guest."
                elif hero.morality <= -25:
                    bree.say "You can service the laptop - and then service me too!"
                else:
                    bree.say "I suppose it wouldn't hurt to let you take a look first."
                $ ryan.love += 1
            "I prefer to leave it to a professionnal":
                if hero.morality >= 25:
                    bree.say "Oh no, Ryan - letting you mess with it could invalidate the warranty!"
                elif hero.morality <= -25:
                    bree.say "You can't even service me properly, Ryan - so I'm not letting you near my laptop!"
                else:
                    bree.say "Nah, I really want a professional to take a look at it."
                $ ryan.love -= 1
            "You're not qualified":
                if hero.morality >= 25:
                    bree.say "Don't be silly, Ryan - you're not qualified!"
                elif hero.morality <= -25:
                    bree.say "Ryan, you can't even find my clit - so how are you going to fix a fucking laptop?!?"
                else:
                    bree.say "Nah, I don't want an enthusiastic amateur making it worse!"
                $ ryan.sub += 1
            "You save me here":
                if hero.morality >= 25:
                    bree.say "Ooh...thanks for the warning, Ryan - good thing I spoke to you first."
                elif hero.morality <= -25:
                    bree.say "Good point, Ryan - remind to me reward you the next time we're alone!"
                else:
                    bree.say "You know, Ryan, I'd never have thought of that - so thanks!"
                $ ryan.sub -= 1
    return

label ryan_talk_music_female:
    if randint(1, 3) == 3:
        bree.say "Are you into the classics when it comes to music, Ryan?"
        bree.say "Or do you make an effort to keep up with all the news stuff?"
        ryan.say "I don't really get music, [hero.name]."
        ryan.say "Never understood what all the fuss is about!"
        ryan.say "All of it sounds the same to me."
    else:
        bree.say "Ooh...I like that girl's T-shirt - what band is that?"
        if ryan.sub >= 50:
            ryan.say "Huh...I bet she's not even into that band, not really!"
        elif ryan.sub <= -50:
            ryan.say "I hate people that aren't real fans - bet she can't even name five of their songs!"
        else:
            ryan.say "Ha...bet you she's one of those people that's not even a proper fan!"
        menu:
            "Fake fans are the worst":
                if hero.morality >= 25:
                    bree.say "Oh, I totally get that - music is something special, it should be cherished!"
                elif hero.morality <= -25:
                    bree.say "Man, if that's true, she'd be the WORST groupie!"
                else:
                    bree.say "Urgh...I hope not - fake fans are the absolute worst!"
                $ ryan.love += 1
            "That's just elitist":
                if hero.morality >= 25:
                    bree.say "Oh, Ryan - why do you have to be so judgemental all the time?"
                elif hero.morality <= -25:
                    bree.say "Oh, because being a gate-keeping asshole is going to get your dick sucked!"
                else:
                    bree.say "That's just elitist bullshit, Ryan, totally cringe!"
                $ ryan.love -= 1
            "You're so full of yourself":
                if hero.morality >= 25:
                    bree.say "Aww...Ryan, you don't have to try so hard to convince me you're deep!"
                elif hero.morality <= -25:
                    bree.say "You don't have to keep trying to impress me, Ryan - it won't make me any more likely to screw you!"
                else:
                    bree.say "Come on, Ryan - I know that your artistic temperament is totally performative!"
                $ ryan.sub += 1
            "You're so right":
                if hero.morality >= 25:
                    bree.say "You are SO right, Ryan - I hate fake fandom."
                elif hero.morality <= -25:
                    bree.say "Yeah, she's not sincere, Ryan, not passionate either - not like I am!"
                else:
                    bree.say "Yeah, I guess you're right, Ryan - fake fans are the worst!"
                $ ryan.sub -= 1
    return

label ryan_talk_birthday_female:
    if hero.morality >= 25:
        bree.say "Happy birthday, Ryan - hope you have a great day!"
    elif hero.morality <= -25:
        bree.say "Happy birthday, Ryan - I'll give a special gift later, when we're alone!"
    else:
        bree.say "Happy birthday, Ryan!"
    bree.say "Did I get the date right?"
    ryan.say "You did, [hero.name]."
    ryan.say "Well done for remembering!"
    $ ryan.love += 3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
