label ryan_desire_0_female:

    if ryan.sub >= 50:
        ryan.say "I always feel like I want to start a conversation with interesting people, [hero.name] - but it can be hard."

    elif ryan.sub <= -50:
        ryan.say "I think people are too afraid of causing offence, [hero.name] - if you have something to say, then say it out loud, right?"
    else:
        ryan.say "I feel like you should be able to strike up a conversation with anyone you find interesting - be totally spontaneous."
    menu:
        "Sure":
            if hero.morality <= -25:
                bree.say "Oh yeah - don't ask, don't get!"
            elif hero.morality >= 25:
                bree.say "I suppose that it's a good thing to be confident, Ryan - if you can pull it off."
            else:
                bree.say "Yeah, I find that people get scared of putting themselves forwards way too much."
            $ ryan.love += 1
        "A little pushy":
            if hero.morality <= -25:
                bree.say "Unless you're all talk and no trousers - that's SO embarrassing!"
            elif hero.morality >= 25:
                bree.say "I don't know, Ryan - I think there's something in respecting people's boundaries."
            else:
                bree.say "Yeah, I get you, but nobody likes a loudmouth!"
            $ ryan.love -= 1
        "A little needy":
            if hero.morality <= -25:
                bree.say "Aww...did you swing it about and nobody noticed?"
            elif hero.morality >= 25:
                bree.say "Don't you think you could be trying too hard - maybe compensating for something?"
            else:
                bree.say "Yeah, but they also say that an empty vessel makes the most noise, right?"
            $ ryan.sub += 1
        "Confidence is the key":
            if hero.morality <= -25:
                bree.say "Oh yeah, Ryan - confidence is SO hot in a guy!"
            elif hero.morality >= 25:
                bree.say "I wish I had your confidence, Ryan - it can be so hard to speak up for yourself!"
            else:
                bree.say "I feel like I could use a boost of confidence myself - you got any more advice?"
            $ ryan.sub -= 1
    return

label ryan_desire_1_female:
    if ryan.sub >= 50:
        ryan.say "You know, [hero.name], some people are jealous of me - I think they're intimidated by my intelligence."
    elif ryan.sub <= -50:
        ryan.say "Believe it or not, [hero.name], I get a lot of haters - I guess I just intimidate a lot of people."
    else:
        ryan.say "You might not believe it, [hero.name], but some don't like me - I think they're jealous of my brains."
    menu:
        "Don't listen to them":
            if hero.morality <= -25:
                bree.say "Don't worry, Ryan - I'm the kind of girl that appreciates a guy with a big one, even when it's his brain!"
            elif hero.morality >= 25:
                bree.say "Well you do sound very smart, Ryan - so I can believe that."
            else:
                bree.say "Ah, just forget about them, Ryan - haters gonna hate, right?"
            $ ryan.love += 1
        "Maybe I can guess why":
            if hero.morality <= -25:
                bree.say "Maybe they think you're trying to compensate for having a small dick?"
            elif hero.morality >= 25:
                bree.say "Hmm...maybe they just don't really like you?"
            else:
                bree.say "Yeah, you can come across as a bit arrogant, you know?"
            $ ryan.love -= 1
        "Maybe you should use your big brain to think about it":
            if hero.morality <= -25:
                bree.say "Being a big brain can be an even bigger turn-off - you get that, right?"
            elif hero.morality >= 25:
                bree.say "Perhaps they don't notice your intelligence, Ryan, and they only see you as domineering?"
            else:
                bree.say "I think you need to ease back on the intelligence and work on the charisma instead."
            $ ryan.sub += 1
        "I alone know who you really are":
            if hero.morality <= -25:
                bree.say "I know they're wrong, Ryan - and I've seen more of you than they ever will!"
            elif hero.morality >= 25:
                bree.say "They're wrong, Ryan, they can't see the real you - not like I can!"
            else:
                bree.say "You can't let people like that pull you down, Ryan - they don't see the real you."
            $ ryan.love += 1
    return

label ryan_desire_2_female:
    if ryan.sub >= 50:
        ryan.say "Being in a relationship is hard, [hero.name] - you have to give up a part of yourself for it."
    elif ryan.sub <= -50:
        ryan.say "Everyone says how much a woman sacrifices in a relationship - but what about the stuff the man gives up?"
    else:
        ryan.say "Everyone wants to be with someone, [hero.name] - but it costs you your independence."
    menu:
        "I guess it's hard to be a man":
            if hero.morality <= -25:
                bree.say "Don't worry, Ryan - I'll pay you back in kind!"
            elif hero.morality >= 25:
                bree.say "I know that, Ryan - and I respect your sacrifice."
            else:
                bree.say "Yeah, I know - guys have it just as hard as girls."
            $ ryan.love += 1
        "Not so strong as a man, right?":
            if hero.morality <= -25:
                bree.say "You know what, Ryan - a victim complex is a real turn-off!"
            elif hero.morality >= 25:
                bree.say "No, Ryan - I don't think most guys get a girl's perspective at all."
            else:
                bree.say "Oh come on, Ryan - you're not one of those whiny kind of guys, are you?"
            $ ryan.love -= 1
        "I will take care of you":
            if hero.morality <= -25:
                bree.say "Show me where it hurts, little guy - I'll kiss it better!"
            elif hero.morality >= 25:
                bree.say "Wow...sounds like you really got screwed over by a girl in the past!"
            else:
                bree.say "Don't worry about it, Ryan - not all girls are as uncaring as that."
            $ ryan.sub += 1
        "I am thankful":
            if hero.morality <= -25:
                bree.say "You're always giving of yourself, Ryan - and I love to be on the receiving end!"
            elif hero.morality >= 25:
                bree.say "I appreciate your sacrifice, Ryan - I really do!"
            else:
                bree.say "It's not fair that guys like you go unappreciated, Ryan."
            $ ryan.sub -= 1
    return

label ryan_desire_3_female:
    if ryan.sub >= 50:
        ryan.say "I'm so tired of doing what people expect, [hero.name] - I wish I had the courage to do what I want instead."
    elif ryan.sub <= -50:
        ryan.say "I've wasted too much time doing what's excepted of me - I'm going to do what I want from now on!"
    else:
        ryan.say "Doing what everyone expects of me never made me happy, [hero.name] - maybe I should do what I want instead?"
    menu:
        "Fulfillment is important":
            if hero.morality <= -25:
                bree.say "I love a guy that's in control, Ryan!"
            elif hero.morality >= 25:
                bree.say "That sounds like an honest way to be, Ryan, and brave too."
            else:
                bree.say "I think if they were honest, most people would admit that's what they already do!"
            $ ryan.love += 1
        "A little egotistical, don't you think":
            if hero.morality <= -25:
                bree.say "A really confident guy wouldn't waste time saying it - he'd just do it."
            elif hero.morality >= 25:
                bree.say "Oh, but isn't that a very selfish thing to do, Ryan - only thinking of yourself?"
            else:
                bree.say "Guys are always saying stuff like that - and it's always so they can do whatever the hell they like."
            $ ryan.love -= 1
        "Are you asking permission?":
            if hero.morality <= -25:
                bree.say "Aww...are you asking me for permission - that's so cute, in a needy kind of way!"
            elif hero.morality >= 25:
                bree.say "Who told you that you couldn't, Ryan - sound like you need permission?"
            else:
                bree.say "Sounds like you'd still need my permission to actually do it, Ryan."
            $ ryan.sub += 1
        "Keep up":
            if hero.morality <= -25:
                "Mmm...I love a man that knows what he wants!"
            elif hero.morality >= 25:
                bree.say "You seem to be more confident than normal, Ryan - like you've made up your mind."
            else:
                "I like how decisive you're being, Ryan - it totally suits you."
            $ ryan.sub -= 1
    return

label ryan_desire_4_female:
    if ryan.sub >= 50:
        ryan.say "I couldn't wait to see you again, [hero.name] - it's like you're always on my mind."
    elif ryan.sub <= -50:
        ryan.say "You have to spend more time with me, [hero.name] - I need you by my side."
    else:
        ryan.say "[hero.name], I haven't stopped thinking about you since we were last together!"
    menu:
        "Together is best":
            if hero.morality <= -25:
                bree.say "Sure thing, Ryan - day or night, either's fine with me."
            elif hero.morality >= 25:
                bree.say "I feel the same way, Ryan - I miss you whenever we're apart."
            else:
                bree.say "I'd love to spend more time with you, Ryan - let's compare diaries."
            $ ryan.love += 1
        "To much attachment is not good":
            if hero.morality <= -25:
                bree.say "Yeah...neediness doesn't do it for me, Ryan!"
            elif hero.morality >= 25:
                bree.say "I don't think so, Ryan - I need my personal space."
            else:
                bree.say "Whoa...when did you start getting so clingy?"
            $ ryan.love -= 1
        "Not surprised":
            if hero.morality <= -25:
                bree.say "I knew that you couldn't resist my charms for very long!"
            elif hero.morality >= 25:
                bree.say "Aww...does someone have a crush on me?"
            else:
                bree.say "Wow, Ryan - you've really fallen for me, haven't you?"
            $ ryan.sub += 1
        "Of course":
            if hero.morality <= -25:
                bree.say "I've got all the time in the world for you, Ryan - so long as you promise to rock mine?"
            elif hero.morality >= 25:
                bree.say "Of course, Ryan - I'll cancel anything that's in my diary right away!"
            else:
                bree.say "Sounds good to me, Ryan - I'd rather be with you than doing almost anything else anyway!"
            $ ryan.sub -= 1
    return

label ryan_desire_5_female:
    if ryan.sub >= 50:
        ryan.say "I can't even try to hide it anymore, [hero.name] - I am one hundred percent yours!"
    elif ryan.sub <= -50:
        ryan.say "I'm not going to hide it anymore, [hero.name] - I need you to be mine!"
    else:
        ryan.say "I'm not even going to try to hide it anymore, [hero.name] - I'm crazy about you!"
    menu:
        "Me too":
            if hero.morality <= -25:
                bree.say "Phew...that's a load off, Ryan - me too!"
            elif hero.morality >= 25:
                bree.say "That's a relief, Ryan - because I feel the exact same way!"
            else:
                bree.say "It's about time, Ryan - because I feel the same way!"
            $ ryan.love += 1
        "Calm down":
            if hero.morality <= -25:
                bree.say "Wow...that's pretty needy!"
            elif hero.morality >= 25:
                bree.say "Oh no, I'm not sure I can handle that level of intensity!"
            else:
                bree.say "Would you mind not, Ryan - because I'm not quite there yet."
            $ ryan.love -= 1
        "It is how I want you to be":
            if hero.morality <= -25:
                bree.say "Oh, Ryan, now I have you in my power - and I can make you do anything I want!"
            elif hero.morality >= 25:
                bree.say "Oops...looks like you lost control of your emotions there!"
            else:
                bree.say "So you're madly in love with me - that means I own your ass!"
            $ ryan.sub += 1
        "YES! Sorry... yes":
            if hero.morality <= -25:
                bree.say "Mmm...Ryan, you had me after the first couple of words!"
            elif hero.morality >= 25:
                "Oh, Ryan...nobody's ever said that to me before - it makes me feel so special!"
            else:
                bree.say "That's so honest of you, Ryan - you must really mean every word!"
            $ ryan.sub -= 1
    return

label ryan_love_0_female:
    if ryan.sub >= 50:
        ryan.say "Isn't it weird, [hero.name] - how we met by such a random chance?"
    elif ryan.sub <= -50:
        ryan.say "I keep thinking that us meeting was so random - like there had to be something pulling us together."
    else:
        ryan.say "Think about it, [hero.name] - us meeting at all was totally random."
    menu:
        "It was meant to be":
            if hero.morality <= -25:
                bree.say "Like attracts like, Ryan - we were bound to come together sooner or later."
            elif hero.morality >= 25:
                bree.say "It is weird, isn't it - almost like fate intervened?"
            else:
                bree.say "I think we were kind of drawn together, don't you?"
            $ ryan.love += 1
        "As if it was a pure coincidence":
            if hero.morality <= -25:
                bree.say "Don't try to make it about anything other than my butt, Ryan!"
            elif hero.morality >= 25:
                bree.say "I don't know, Ryan - you seem to gravitate towards the ladies."
            else:
                bree.say "Maybe it was more to do with me being a girl and your wandering eye?"
            $ ryan.love -= 1
        "You had no chance to escape":
            if hero.morality <= -25:
                bree.say "Nah, I could see how much you wanted to know more the first time you set eyes on me!"
            elif hero.morality >= 25:
                bree.say "Oh, Ryan - it is like you just couldn't resist befriending me, isn't it?"
            else:
                bree.say "Yeah, I knew you wanted to get to know me the moment we first met!"
            $ ryan.sub += 1
        "I had no chane to escape":
            if hero.morality <= -25:
                bree.say "You have got a certain animal magnetism!"
            elif hero.morality >= 25:
                bree.say "I can't explain it, Ryan - it's like you're too charming to ignore!"
            else:
                bree.say "Yeah, you're certainly a charmer, Ryan!"
            $ ryan.sub -= 1
    return

label ryan_love_1_female:
    if ryan.sub >= 50:
        ryan.say "You've been a really good friend recently, [hero.name] - really supported me."
    elif ryan.sub <= -50:
        ryan.say "I really needed you recently, [hero.name] - and you didn't let me down."
    else:
        ryan.say "Thanks for being there these last few days, [hero.name] - it's been tough."
    menu:
        "Just the right thing to do":
            if hero.morality <= -25:
                bree.say "Ah, it's no trouble to help out someone as cute as you!"
            elif hero.morality >= 25:
                bree.say "Of course, Ryan - isn't that what friends are for?"
            else:
                bree.say "I just wanted to be a good friend, Ryan - you'd do the same for me."
            $ ryan.love += 1
        "You are exhausting":
            if hero.morality <= -25:
                bree.say "You think I was doing that for free - I need compensating with affection!"
            elif hero.morality >= 25:
                bree.say "Yeah, you took a little more than I'm comfortable with - so I need to back off from you for a while."
            else:
                bree.say "I feel like I burnt myself out though - so maybe lay off me for a while?"
            $ ryan.love -= 1
        "It's clear you needed me":
            if hero.morality <= -25:
                bree.say "You don't always have to be strong, Ryan - you can let me be the one in charge, if you like?"
            elif hero.morality >= 25:
                bree.say "It's okay, Ryan - it really looked like you could use the support."
            else:
                bree.say "I know you hide it, Ryan - but it's obvious you're kind of struggling."
            $ ryan.sub += 1
        "I hope you're strong enough to return the favor":
            if hero.morality <= -25:
                bree.say "The truth is that I want you to be strong, Ryan - so you can take me firmly in hand!"
            elif hero.morality >= 25:
                bree.say "I...I kind of hoped you'd do the same for me, Ryan?"
            else:
                bree.say "I'm not that strong, Ryan - you might have to return the favour!"
            $ ryan.sub -= 1
    return

label ryan_love_2_female:
    if ryan.sub >= 50:
        ryan.say "It's not easy for a guy to have female friends, [hero.name] - but here we are."
    elif ryan.sub <= -50:
        ryan.say "Guys and girls not being able to maintain a platonic relationship - that's rubbish!"
    else:
        ryan.say "They say a guy and a girl can't be friends, but we proved them wrong."
    menu:
        "We are more than friends":
            if hero.morality <= -25:
                bree.say "Yeah, but 'friends' can always evolve into 'friends with benefits'!"
            elif hero.morality >= 25:
                bree.say "I'll say so, Ryan - you're one of my very best friends!"
            else:
                bree.say "I think you just have to be emotionally mature to make it work, like we are."
            $ ryan.love += 1
        "You? Friend with a girl?":
            if hero.morality <= -25:
                bree.say "Yeah, that's just something guys say - they always want more."
            elif hero.morality >= 25:
                bree.say "Are we really just friends, Ryan - especially after what happened with poor Sam?"
            else:
                bree.say "Yeah...I wonder what Sam would say about that?"
            $ ryan.love -= 1
        "Sure. Friendship is what you need":
            if hero.morality <= -25:
                bree.say "Don't worry, Ryan - I can sense what you really need."
            elif hero.morality >= 25:
                bree.say "Aww...it's cute that you consider me a friend!"
            else:
                bree.say "Yeah...you really need a friend right now, don't you?"
            $ ryan.sub += 1
        "You are my special friend":
            if hero.morality <= -25:
                bree.say "I've never had a friend that made me feel the way you do, Ryan!"
            elif hero.morality >= 25:
                bree.say "I'd say you're one of my very best friends, Ryan."
            else:
                bree.say "I don't know if I could manage that with any other guy, Ryan."
            $ ryan.sub -= 1
    return

label ryan_love_3_female:
    if ryan.sub >= 50:
        ryan.say "I feel like we're really starting to get to know each other now, [hero.name] - to explore our relationship and what it means."
    elif ryan.sub <= -50:
        ryan.say "I feel like I'm really getting to know you now, [hero.name] - like I understand you better all the time."
    else:
        ryan.say "Our friendship is getting stronger all the time, isn't it - like, we're discovering how compatible we really are?"
    menu:
        "I think so":
            if hero.morality <= -25:
                bree.say "I understand what part of you I want better every day!"
            elif hero.morality >= 25:
                bree.say "I think we really are getting closer, Ryan - in a meaningful way too."
            else:
                bree.say "It's weird, but I seem to be tuning into you more every day!"
            $ ryan.love += 1
        "It is one step":
            if hero.morality <= -25:
                bree.say "I'm enjoying the ride, Ryan - but I can always press the emergency stop, button."
            elif hero.morality >= 25:
                bree.say "But I still don't know if I can really trust you, Ryan, not really."
            else:
                bree.say "You're fun, Ryan, but I don't know if I fully trust you - isn't that what Sam did?"
            $ ryan.love -= 1
        "I'll take care of you":
            if hero.morality <= -25:
                bree.say "Don't worry, I know Sam hurt you - but my touch can heal the pain, I promise."
            elif hero.morality >= 25:
                bree.say "I know that you needed to heal after Sam, and I'm here for as long as that takes."
            else:
                bree.say "It can't have been hard after what happened with you and Sam - but I'm here for you."
            $ ryan.sub += 1
        "Totally agree":
            if hero.morality <= -25:
                bree.say "Are you reading my mind, Ryan - like, what position am I thinking about right now?"
            elif hero.morality >= 25:
                bree.say "You always seem to get me, Ryan - like you just know what I'm thinking!"
            else:
                bree.say "It's weird, but you always seem to be able to read me - like it's a gift."
            $ ryan.sub -= 1
    return

label ryan_love_4_female:
    if ryan.sub >= 50:
        ryan.say "I know we haven't know each other long, [hero.name] - but you're already the most important person in my life!"
    elif ryan.sub <= -50:
        ryan.say "I've never met a girl that I knew I had to have so soon before, [hero.name] - you must be mine!"
    else:
        ryan.say "This has been a whirlwind affair, [hero.name] - and it's made you the centre of my universe!"
    menu:
        "You're important as well":
            if hero.morality <= -25:
                bree.say "Oh yeah, I know that feeling - it hits me in a very specific spot!"
            elif hero.morality >= 25:
                bree.say "I feel the same way about you, Ryan - we're bound together!"
            else:
                bree.say "You've become so important to me too, Ryan - I can't imagine not being your friend."
            $ ryan.love += 1
        "You're going a little to fast":
            if hero.morality <= -25:
                bree.say "You're good, Ryan - but you're not the only game in town."
            elif hero.morality >= 25:
                bree.say "Slow down there, Ryan - you're getting ahead of yourself!"
            else:
                bree.say "I think a lot of you too, Ryan - but I'm not going to offer myself up as a living sacrifice just yet!"
            $ ryan.love -= 1
        "You're cute":
            if hero.morality <= -25:
                bree.say "Hmm...I wonder just how devoted to me you really are?"
            elif hero.morality >= 25:
                bree.say "It's flattering to know that you need me so much, Ryan."
            else:
                bree.say "Yeah...you've really fallen hard for me, haven't you?"
            $ ryan.sub += 1
        "You're making me blush'":
            if hero.morality <= -25:
                bree.say "Oh, Ryan...you are making me SO hot right now!"
            elif hero.morality >= 25:
                bree.say "Oh my goodness...nobody ever said anything like that to me before!"
            else:
                bree.say "That's a really bold thing to say, Ryan - you must really mean it!"
            $ ryan.sub -= 1
    return

label ryan_love_5_female:
    if ryan.sub >= 50:
        ryan.say "I can't avoid it any longer, [hero.name] - I love you more than anything!"
    elif ryan.sub <= -50:
        bree.say "I can't do anything but say it out loud - [hero.name], you must be mine!"
    else:
        ryan.say "No more dodging the truth and playing it down - [hero.name], I love you!"
    menu:
        "Me too":
            if hero.morality <= -25:
                bree.say "Ooh...I can't wait until you show me just how much you love me!"
            elif hero.morality >= 25:
                bree.say "Oh, Ryan - we're totally on the same page!"
            else:
                bree.say "Me too, Ryan - it's time we went public!"
            $ ryan.love += 1
        "Let's slow down a little":
            if hero.morality <= -25:
                bree.say "Ah, yeah...can I have the physical passion and skip the emotional torment and suffering?"
            elif hero.morality >= 25:
                bree.say "Are you sure you're ready for that, Ryan - look what happened to your last serious relationship!"
            else:
                bree.say "I think we need to reign it in a little, Ryan - you crashed and burned the last time you did this!"
            $ ryan.love -= 1
        "I am pleased to hear that":
            if hero.morality <= -25:
                bree.say "You can have what you want, once I get what I want, Ryan - so why don't you get down on your knees?"
            elif hero.morality >= 25:
                bree.say "That's a good place to start, Ryan - now we can get to work on ironing out all of your little...kinks!"
            else:
                bree.say "You can have all of this good stuff, Ryan - so long as I'm the one wearing the pants in the relationship."
            $ ryan.sub += 1
        "I am so happy right now":
            if hero.morality <= -25:
                bree.say "Are you serious, Ryan - because if you are, then you can have as much of me as you want and whenever you like!"
            elif hero.morality >= 25:
                bree.say "Oh, Ryan - do you really mean that, are you going to make me the happiest girl in the world?"
            else:
                bree.say "Whoa...that's kind of mind-blowing, Ryan - you're going to have to help me make sense of it all!"
            $ ryan.sub -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
