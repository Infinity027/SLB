label alexis_desire_0_male:
    alexis.say "[hero.name], do you ever wish we could just go back to when we were in high school together?"
    alexis.say "You know, like have all that time over again?"
    menu:
        "Agree":
            mike.say "Yeah, it'd sure be nice to know then what I know now."
        "Disagree":
            mike.say "What - are you kidding me?!?"
            mike.say "I hated school, every damn minute of it until I got out of that place!"
            $ alexis.love -= 1
    return

label alexis_desire_1_male:
    alexis.say "What do you think of the cut on my top, [hero.name]?"
    alexis.say "I hope you don't think I'm showing off too much skin..."
    menu:
        "Admire the view":
            mike.say "N...no...no way, Alexis..."
            mike.say "I think it's very...flattering on you!"
            $ alexis.love += 1
        "Disapprove":
            mike.say "Now that you come to mention it, Alexis."
            mike.say "There is something to be said for a bit of modesty..."
            $ alexis.sub += 1
    return

label alexis_desire_2_male:
    alexis.say "Urgh, I'm so jealous of guys sometimes - you always grow into your looks."
    alexis.say "Like you, [hero.name] - you just seem to get better with age!"
    menu:
        "Be flattered":
            mike.say "Aww, I'm not really that good looking, Alexis - am I?"
            $ alexis.love += 1
        "Be offended":
            mike.say "Oh, thanks, Alexis!"
            mike.say "Am I supposed to take that as you're saying I was an ugly kid, or that I'm past it now?"
            $ alexis.sub += 1
    return

label alexis_desire_3_male:
    alexis.say "I've always been kinda jealous of Kylie."
    alexis.say "Younger siblings always seem to have an easier ride in life - don't they?"
    menu:
        "Disagree":
            mike.say "I think Kylie must have envied growing up in your shadow, Alexis."
            mike.say "She's a sweet girl, but she can't hold a torch to you."
            $ alexis.love += 1
        "Agree and compliment Kylie":
            mike.say "It's no wonder Kylie seems to waltz through life, Alexis."
            mike.say "Especially when you consider that she was the one of you that got all of the looks!"
            $ alexis.sub += 1
            $ kylie.love += 1
    return

label alexis_desire_4_male:
    alexis.say "You know, back when I first called you up, I wasn't sure I was doing the right thing."
    alexis.say "But since then, I've come to realise it was one of the best decisions I could have made."
    menu:
        "Agree":
            mike.say "Well, I'm certainly glad that you didn't give in to your doubts, Alexis."
            mike.say "I feel like we were always supposed to hook up again, even after all this time."
            $ alexis.love += 1
        "Disagree":
            mike.say "Meh - I think I'm still back where you were when you called me, if I'm honest."
            mike.say "Things are never as good in the flesh as you remember them being."
            $ alexis.sub += 1
    return

label alexis_desire_5_male:
    alexis.say "Oh, [hero.name] - I can't believe that we're together again."
    alexis.say "I feel like there's nothing that could tear me away from you a second time!"
    menu:
        "Agree":
            mike.say "Whatever tried to tear us apart would have to deal with me hanging onto you too, Alexis!"
            $ alexis.love += 1
        "Disagree":
            mike.say "I dunno, Alexis - I feel like I'm just getting a nostalgia kick out of all of this."
            mike.say "Where's the fun in living in the past all of the time?"
            $ alexis.love -= 1
    return

label alexis_love_0_male:
    alexis.say "Hey, [hero.name] - you remember that dumb dance that was all the craze one summer back in high school?"
    "Alexis demonstrates what she claims to be the dance in question, though it seems to be more of an excuse to flash her breasts and backside at me."
    menu:
        "Flirt back":
            mike.say "Vaguely - but I think you need to come closer and show me that again."
            mike.say "Maybe come real close and show me..."
            $ alexis.love += 1
        "Blow her off":
            mike.say "Yes, I do."
            mike.say "And the only thing that could look more stupid than you did doing it back then is you doing it now!"
            $ alexis.sub += 1
    return

label alexis_love_1_male:
    alexis.say "Mmm...I think I have a kink in my shoulders or something."
    alexis.say "[hero.name], would you be a lifesaver and give it a rub for me?"
    menu:
        "Give Alexis a massage":
            mike.say "Sure, just pull down the straps of your top - best to do the same with your bra too."
            mike.say "I'm sure I have some oil around here somewhere..."
            $ alexis.love += 1
        "Refuse to give Alexis a massage":
            mike.say "Oh no, I don't have any idea what I'm doing when it comes to that kind of thing."
            mike.say "I could make it ten times worse - you should really go see a professional."
            $ alexis.love -= 1
    return

label alexis_love_2_male:
    pass
    alexis.say "Brr...I'm really feeling cold, [hero.name]!"
    alexis.say "Can I cuddle up to you - just for the warmth?"
    menu:
        "Agree to let Alexis cuddle":
            mike.say "You should have said so sooner, Alexis."
            mike.say "Come over here, as close as you like - maybe I could give you a quick rub to get the blood flowing again?"
            $ alexis.love += 1
        "Refuse to let Alexis cuddle":
            mike.say "Erm, no...I don't think so - I like my personal space to stay uninvaded."
            mike.say "Maybe put on a sweater or something?"
            $ alexis.love -= 1
    return

label alexis_love_3_male:
    alexis.say "[hero.name]...you told me that you lived with two girls."
    alexis.say "But you never told me that they were both so hot..."
    menu:
        "Reassure Alexis":
            mike.say "What - you mean [bree.name] and Sasha?!?"
            mike.say "I'm guessing you've never seen either of them first thing in the morning!"
            mike.say "Or had to use the bathroom after one of them either..."
            $ alexis.love += 1
        "Don't reassure Alexis":
            mike.say "Oh, I know exactly what you mean, you don't need to tell me about it!"
            mike.say "It's even harder when they're wandering around in their skimpy little pyjamas before going to bed!"
            mike.say "And when they decide to go for a dip in the pool - forget it!"
            $ alexis.sub += 1
    return

label alexis_love_4_male:
    alexis.say "You know, even a year ago, if someone had told me I'd be back in a relationship with you, I wouldn't have believed them!"
    alexis.say "I'd have called it a miracle...or a dream."
    menu:
        "Agree with Alexis":
            mike.say "Well, I hope that two people can share a dream."
            mike.say "Because I never want to be without you, awake or sleeping."
            $ alexis.love += 1
        "Disagree with Alexis":
            mike.say "Hah, what a dream - a nightmare, more like!"
            $ alexis.love -= 1
    return

label alexis_love_5_male:
    alexis.say "You know, part of me never truly believed that you could ever forgive me for what I did to you."
    alexis.say "But another part of me never stopped loving you, no matter what."
    menu:
        "Agree with Alexis":
            mike.say "I think the part of you that hurt me died a long time ago, Alexis."
            mike.say "And I love every other part of you that's come back to me."
            $ alexis.love += 1
        "Disagree with Alexis":
            mike.say "Sickly sweet little speech about how you feel, Alexis."
            mike.say "Problem is that's only how things are inside of your empty little head."
            $ alexis.sub += 1
    return

label alexis_good_sweet_talk_male:
    show alexis
    if alexis.love > 133:
        mike.say "I want to say that I wish we'd never split up in high-school, Alexis."
        mike.say "But things have been so much better since we got back together."
        mike.say "I don't think I'd change a thing!"
        show alexis happy
        alexis.say "That means a lot, [hero.name]!"
    elif alexis.love > 66:
        mike.say "It feels strange to be dating you again, Alexis."
        mike.say "But it's a good kind of strange, you know?"
        mike.say "It's really exciting!"
        show alexis flirt
        alexis.say "I like the sound of that!"
    else:
        mike.say "I'm so glad we were reunited, Alexis."
        mike.say "I think I'd forgotten what a good friend you were to me!"
        show alexis blush
        alexis.say "That's so sweet of you to say!"
        alexis.say "I feel the same way too."
    hide alexis
    return

label alexis_bad_sweet_talk_male:
    show alexis
    mike.say "You're always up for some fun, right, Alexis?"
    show alexis angry
    alexis.say "Oh really?"
    alexis.say "Is that a nice way of saying I like to sleep around?"
    mike.say "No...no way, Alexis!"
    hide alexis
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
