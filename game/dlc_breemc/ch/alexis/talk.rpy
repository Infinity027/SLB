label alexis_talk_love_female:
    show alexis
    bree.say "You believe in true love, right, Alexis?"
    bree.say "I mean, not like fairy tale stuff - but the real thing?"
    if alexis.is_visibly_pregnant:
        alexis.say "Of course I do, [hero.name]!"
        alexis.say "How else could I bring a new life into the world?"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "I think it exists, [hero.name] - but it's hard to find."
        alexis.say "I mean, just look at the mess [mike.name] and I made of it back in the day!"
        $ alexis.love += 1
    else:
        alexis.say "Don't be so naive, [hero.name]!"
        alexis.say "Waiting around for true love is only going to get you hurt."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_sex_female:
    show alexis
    bree.say "[mike.name] told me used to be pretty wild back in high school, Alexis."
    bree.say "You know, pretty liberated when it came to the old S...E...X?"
    if alexis.is_visibly_pregnant:
        alexis.say "I...I guess so, [hero.name]."
        alexis.say "Things sure were more simple back then!"
    elif alexis.love >= 50:
        alexis.say "O...M...G, [hero.name]!"
        alexis.say "You have NO idea!"
        alexis.say "And it's not like I've slowed down since then either..."
        $ alexis.sub += 1
    else:
        alexis.say "Yeah, I guess he would say that."
        alexis.say "But I try not to let my past define me."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_politics_female:
    show alexis
    bree.say "I think people overthink politics, Alexis - don't you think?"
    bree.say "It's all pretty simple once you boil it down to the basics."
    if alexis.is_visibly_pregnant:
        alexis.say "You're probably right, [hero.name]."
        alexis.say "But The baby-brain's got me all confused right now!"
    elif alexis.love >= 50:
        alexis.say "You're right, [hero.name]."
        alexis.say "People could learn a lot from you!"
    else:
        alexis.say "I don't know, [hero.name]."
        alexis.say "Politics was never my thing."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_food_female:
    show alexis
    bree.say "Urgh...I'm SO hungry!"
    bree.say "I can't think straight when I'm like this!"
    if alexis.is_visibly_pregnant:
        alexis.say "You should try being pregnant, [hero.name]!"
        alexis.say "It's like hunger's taken over my life."
        alexis.say "And don't get me started on the cravings!"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "Oh no, [hero.name]!"
        alexis.say "You should really eat something."
        alexis.say "You could have low blood-sugar or something!"
        $ alexis.love += 1
    else:
        alexis.say "Then eat something, [hero.name]."
        alexis.say "It's no big deal."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_travels_female:
    show alexis
    bree.say "As soon as I have some serious money, I'm going to go travelling."
    bree.say "I want to see as much of the world as I can, Alexis!"
    if alexis.is_visibly_pregnant:
        alexis.say "That's sweet, [hero.name]."
        alexis.say "But I'm not going anywhere with a baby in my belly!"
    elif alexis.love >= 50:
        alexis.say "Yeah, I know just what you mean."
        alexis.say "It always seems like there's too much to see in one lifetime!"
        $ alexis.love += 1
    else:
        alexis.say "Sure, I could do travel."
        alexis.say "But it's not special without the right travel companion."
    hide alexis
    return

label alexis_talk_tv_female:
    show alexis
    bree.say "I need to spend some quality time with the TV tonight, Alexis."
    bree.say "I've been so busy that I've fallen behind with all of the series I'm streaming!"
    if alexis.is_visibly_pregnant:
        alexis.say "I hear what you're saying, [hero.name]!"
        alexis.say "Anything that lets me put my feet up and rest!"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "Are you serious, [hero.name]?"
        alexis.say "You'd rather fester in front of the TV than spend time with real people?!?"
        $ alexis.love -= 1
    else:
        alexis.say "Each to their own, [hero.name]."
        alexis.say "You do you."
    hide alexis
    return

label alexis_talk_sports_female:
    show alexis
    bree.say "I keep on trying to get into sports, Alexis."
    bree.say "I mean, it's not really my kind of thing."
    bree.say "But it's good to make the effort, right?"
    if alexis.is_visibly_pregnant:
        alexis.say "I don't know, [hero.name]."
        alexis.say "It's not like I have a dog in that fight..."
    elif alexis.love >= 50:
        alexis.say "Urgh, [hero.name]!"
        alexis.say "You shouldn't change who you are for the approval of other people!"
        $ alexis.love -= 2
    else:
        alexis.say "I really don't like sports, [hero.name]."
        alexis.say "So it's kind of disappointing to hear you say that!"
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_fashion_female:
    show alexis
    bree.say "I kinda want to make people believe that I just wear whatever, you know?"
    bree.say "But the truth is that I spend a lot of time picking out my clothes!"
    if alexis.is_visibly_pregnant:
        alexis.say "Oh hell, [hero.name] - I wish I had that choice!"
        alexis.say "It's hard enough finding stuff that fits when you're pregnant."
        alexis.say "Or stuff that's comfortable too!"
    elif alexis.love >= 50:
        alexis.say "Oh, [hero.name]..."
        alexis.say "What are you like?"
    else:
        alexis.say "You know what, [hero.name] - I like that about you!"
        alexis.say "It kind of shows that you have hidden depths."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_books_female:
    show alexis
    bree.say "Why do we girls have to carry such little bags, Alexis?"
    bree.say "You just can't get a purse big enough to fit a book into!"
    if alexis.is_visibly_pregnant:
        alexis.say "You should try being pregnant, [hero.name]."
        alexis.say "I have to haul my stuff around in a bag the size of a sack!"
    elif alexis.love >= 50:
        alexis.say "You're right, [hero.name] - it does suck!"
        alexis.say "It's like they're deliberately trying to hide how smart you are!"
        $ alexis.love += 1
    else:
        alexis.say "Is it really that big of a deal, [hero.name]?"
        alexis.say "Just download an e-book onto your mobile like a normal person!"
    hide alexis
    return

label alexis_talk_people_female:
    show alexis
    bree.say "I do the best I can to see the good in most people, Alexis."
    bree.say "But do you ever feel like some of them are...I don't know...a lost cause?"
    if alexis.is_visibly_pregnant:
        alexis.say "I don't know about that, [hero.name]."
        alexis.say "I kind of lost interest in what other people think since I got pregnant!"
    elif alexis.love >= 50:
        alexis.say "Urgh...I know exactly what you mean, [hero.name]!"
        alexis.say "You just end up smiling through gritted teeth, right?"
        alexis.say "And you're thinking how can they be such jerks!"
        $ alexis.love += 1
    else:
        alexis.say "I don't know, [hero.name]."
        alexis.say "Sometimes the problem is with you, and not the other person..."
    hide alexis
    return

label alexis_talk_computers_female:
    show alexis
    bree.say "Can you imagine life without computers, Alexis?"
    bree.say "I mean, they're in everything these days!"
    bree.say "We'd be back to the stone-age without them!"
    if alexis.is_visibly_pregnant:
        alexis.say "I don't care about computers, [hero.name]."
        alexis.say "So long as they work when I need them."
        alexis.say "And there's somebody else to fix them if they go wrong!"
    elif alexis.love >= 50:
        alexis.say "People did manage okay without them, [hero.name]!"
        alexis.say "You should try to remember that."
        $ alexis.sub -= 1
    else:
        alexis.say "[hero.name], you can't expect computers to do everything for you!"
        alexis.say "What would you do if they all stopped working tomorrow, huh?"
        alexis.say "Did you ever think of that?"
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_music_female:
    show alexis
    bree.say "You've got to hear this new song, Alexis!"
    bree.say "I just can't get it out of my head!"
    if alexis.is_visibly_pregnant:
        alexis.say "Maybe later, [hero.name]."
        alexis.say "I'm trying to expose my baby to classical music."
        alexis.say "And that doesn't sound classical to me!"
    elif alexis.love >= 50:
        alexis.say "Okay, [hero.name], okay."
        alexis.say "That does sound kind of catchy!"
        $ alexis.sub += 1
    else:
        alexis.say "Nah, [hero.name] - I think I'll pass."
        alexis.say "I know my own taste in music pretty well."
        alexis.say "I don't need anyone to help me find a song I like."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_birthday_female:
    show alexis
    bree.say "Happy Birthday, Alexis!"
    bree.say "Many happy returns!"
    if alexis.love >= 50:
        alexis.say "Oh, that's so sweet of you, [hero.name]!"
        alexis.say "How did you know?"
        $ alexis.love += 1
    else:
        alexis.say "Wait a minute, [hero.name] - I never told you my birthday!"
        alexis.say "Have you been snooping around behind my back?!?"
    hide alexis
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
