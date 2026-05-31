label morgan_talk_love_male:
    mike.say "What's your take on love, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan happy
        morgan.say "I think this baby is proof enough that it's real."
        $ morgan.love += 1
    elif morgan.male >= 75:
        morgan.say "I'm not into all of that sappy stuff!"
    elif morgan.male >= 25:
        show morgan happy
        morgan.say "I don't know if I believe in finding Mr Right...but I believe you can find happiness if you look for it."
        $ morgan.love += 1
    elif morgan.sub < 75:
        show morgan happy
        morgan.say "I think that there's someone for everyone."
        morgan.say "But if you're not prepared to look, then you won't find them!"
        $ morgan.love += 1
    else:
        show morgan happy
        morgan.say "Everyone should try to find true love!"
        $ morgan.love += 1
    if morgan.love >= 50:
        $ morgan.male -= 1
    hide morgan
    return

label morgan_talk_sex_male:
    mike.say "Have you got a philosophy when it comes to sex, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan happy
        morgan.say "It can lead you down some pretty life-changing roads."
        $ morgan.sub += 1
    elif morgan.male >= 75:
        show morgan happy
        morgan.say "Keep it fun and keep it casual - no one needs to be tied down when they can be having fun instead!"
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "I've tried to be laid back about it in the past."
        morgan.say "But I definitely get more out of it when it's with someone I care about."
    elif morgan.sub < 75:
        morgan.say "It was always disappointing, before you came back into my life!"
    else:
        morgan.say "I just like to please my partner. On top or on bottom."
        if morgan.sexperience >= 3:
            show morgan blushhappy
            morgan.say "Maybe tonight I can show you..."
        $ morgan.love += 1
    if morgan.sub <= 25:
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_politics_male:
    mike.say "Elections are coming round again - will you be voting, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        morgan.say "Yeah, of course - I have someone else's future to think about now."
    elif morgan.male >= 75:
        show morgan angry
        morgan.say "They're all a bunch of pricks and liars!"
        $ morgan.love += 1
    elif morgan.male >= 25:
        morgan.say "They all talk like they want to do good, but you can't trust them once they're in office."
    else:
        show morgan annoyed
        morgan.say "I think that politicians don't look out for people like me. I wish they did."
        $ morgan.love -= 1
    hide morgan
    return

label morgan_talk_food_male:
    mike.say "Think quickly, Morgan - eat out or takeout?"
    show morgan
    if morgan.is_visibly_pregnant:
        morgan.say "If you want to take me out anytime soon - make it one of those all-you-can-eat buffets."
        show morgan happy
        morgan.say "This baby's got me eating like a horse!"
        $ morgan.love += 1
    elif morgan.male >= 75:
        morgan.say "Takeout, every time - less fuss more food!"
    elif morgan.male >= 25:
        morgan.say "Depends on my mood - sometimes I wanna be wined and dined, sometimes I just want a dirty slice of pizza."
    elif morgan.sub < 75:
        show morgan happy
        morgan.say "I'm a modern girl - but I still like to be taken out for a surprise meal every now and then."
        $ morgan.love += 1
    else:
        show morgan happy
        morgan.say "Ooh, I love to go to a fancy restaurant!"
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_travels_male:
    mike.say "If you could jet off anywhere in the world, where would it be?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan happy
        morgan.say "I'd like for us to go somewhere nice as a family, once the baby's here."
        $ morgan.love += 1
    elif morgan.male >= 75:
        morgan.say "I'd like to do one of those extreme hiking holidays, like through the desert or mountains, or something like that."
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "Hmm...I guess I've always wanted to see Europe - like Paris and Berlin, that sort of thing."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I'm sure you can soak up the culture of a place as well as soaking up some rays on the beach!"
        $ morgan.love += 1
        $ morgan.male -= 1
    else:
        morgan.say "Oh, there's so much fun stuff you can do at Disneyland Paris!"
        $ morgan.love += 1
    hide morgan
    return

label morgan_talk_tv_male:
    mike.say "There's fuck all on TV right now."
    mike.say "I don't know why I bother with it!"
    show morgan
    if morgan.is_visibly_pregnant:
        morgan.say "I try to watch it, but I fall asleep whenever I lay down on the sofa."
    elif morgan.male >= 75:
        show morgan annoyed
        morgan.say "Don't be such a pussy, man!"
        morgan.say "There's always a game or a fight on one of the channels."
        $ morgan.love -= 1
    elif morgan.male >= 25:
        morgan.say "Just sign up for a streaming service, then you can please yourself."
    elif morgan.sub < 75:
        show morgan happy
        morgan.say "I always prefer to watch TV when I have someone worth snuggling down with..."
        $ morgan.love += 1
    else:
        show morgan happy
        morgan.say "I'll watch anything you want to watch!"
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_sports_male:
    mike.say "Sports, sports, sports - that's all some people ever seem to talk about!"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan annoyed
        morgan.say "Those steroid-brained jocks want to try being pregnant - that'd show how tough they really are!"
        $ morgan.love -= 1
    elif morgan.male >= 75:
        show morgan annoyed
        morgan.say "What do you mean you don't like sports?"
        morgan.say "You're a guy, aren't you?"
        $ morgan.love -= 1
    elif morgan.male >= 25:
        morgan.say "I know - it's like they don't have anything else in their lives of any significant meaning."
        show morgan annoyed
        morgan.say "Sad, really."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I know it's a cliche, but I don't get anything out of them."
        show morgan happy
        morgan.say "And before you say it - yes, I have tried!"
        $ morgan.love += 1
    else:
        morgan.say "I wish I liked sports, to be honest. Watching a bunch of hot guys hitting each other? Should be a turn on, but it just isn't."
        $ morgan.sub += 1
    hide morgan
    return

label morgan_talk_fashion_male:
    mike.say "Do you keep up with what's supposed to be in fashion, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan annoyed
        morgan.say "Don't talk to me about fashion - it's the twenty-first century, and maternity clothes are still basically sacks with head and arm holes!"
        $ morgan.love -= 1
    elif morgan.male >= 75:
        morgan.say "It's important to have a style. That's why I always picked out clothes everyone thought was boyish!"
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        morgan.say "I started changing up my wardrobe a bit. That takes a lot of time."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "Sure, I really want to be a feminist and reject all of that stuff."
        morgan.say "But you can project you want to be without knowing what you look like!"
        $ morgan.male -= 1
    else:
        show morgan blushhappy
        morgan.say "Oh yeah, because I like it when you look at me!"
        $ morgan.love += 1
        $ morgan.sub += 1
        $ morgan.male -= 1
    hide morgan
    return

label morgan_talk_books_male:
    mike.say "Recommend a good book, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        morgan.say "You bet - all I've been doing lately is sprawling around like a whale of an evening and devouring books!"
        $ morgan.love += 1
    elif morgan.male >= 75:
        show morgan annoyed
        morgan.say "Nope - you should do things in life, not read about them."
        $ morgan.love -= 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        show morgan happy
        morgan.say "Yeah, sure - I have far too many books at home."
        morgan.say "I just wish that I had time to read them all!"
        $ morgan.love += 1
        $ morgan.male -= 1
    elif morgan.sub < 75:
        show morgan blush
        morgan.say "Would you be mad with me if I said that I sometimes claim to have read pretty heavy classics, just to look smarter?"
        $ morgan.sub += 1
    else:
        show morgan blush
        morgan.say "I started reading a bit more philosophy lately. Particularly about feminism and gender identity stuff."
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ morgan.male -= 1
    return

label morgan_talk_people_male:
    mike.say "Are you a people person, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan annoyed
        morgan.say "Not really - the pregnancy's made me kinda anti-social."
        $ morgan.love -= 1
    elif morgan.male >= 75:
        show morgan happy
        morgan.say "Sure, I'm always the life and soul of the party!"
        $ morgan.love += 1
    elif morgan.male >= 25:
        morgan.say "Well, that depends rather heavily on the people involved..."
    elif morgan.sub < 75:
        show morgan happy
        morgan.say "I always love talking to everyone."
        $ morgan.sub += 1
    else:
        show morgan happy
        morgan.say "Oh yeah - I'm always being called bubbly and outgoing!"
        $ morgan.love += 1
        $ morgan.male -= 1
    hide morgan
    return

label morgan_talk_computers_male:
    mike.say "Do you keep up to speed with the world of computers, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan annoyed
        morgan.say "I've been getting better since I found myself stuck inside most of the time."
        $ morgan.love -= 1
    elif morgan.male >= 75:
        show morgan happy
        morgan.say "I know how to turn one on and find some decent porn - what more is there to know?"
        $ morgan.male += 1
    elif morgan.male >= 25:
        show morgan happy
        morgan.say "I'm no hacker or anything like that, but I know as much as the next person...maybe a little more, even."
        $ morgan.love += 1
    elif morgan.sub < 75:
        morgan.say "I know enough - just don't ask me to moonlight as an IT technician!"
        $ morgan.sub -= 1
    else:
        morgan.say "I get by. I can surf the internet, use a word processor, and waste time on idle games."
        $ morgan.love -= 1
        $ morgan.sub += 1
        $ morgan.male += 1
    hide morgan
    return

label morgan_talk_music_male:
    mike.say "I'm thinking of going to the record store - you interested, Morgan?"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan annoyed
        morgan.say "Urrgh...count me out if it involves prolonged periods of walking and standing!"
        $ morgan.love -= 1
    elif morgan.male >= 75:
        morgan.say "I don't really like Jack's idea of metal, but maybe something a bit more modern that rocks out."
        $ morgan.love += 1
        $ morgan.sub -= 1
        $ morgan.male += 1
    elif morgan.male >= 25:
        show morgan happy
        morgan.say "Yeah, my ex and I used to spend hours looking at old records. I love vinyl!"
        $ morgan.love += 1
    elif morgan.sub < 75:
        show morgan happy
        morgan.say "I'm always up to look for something new and different. I want stuff I've never heard before..."
        $ morgan.love += 1
    else:
        show morgan happy
        morgan.say "Yes! I can spend hours looking at old, weird stuff, trying to find something inspiring!"
        $ morgan.love += 1
        $ morgan.male -= 1
    hide morgan
    return

label morgan_talk_birthday_male:
    mike.say "Happy birthday, Morgan!"
    show morgan
    if morgan.is_visibly_pregnant:
        show morgan sad
        "Morgan bursts into tears at the mere mention of her birthday."
        morgan.say "Oh god, I'm so old!"
        morgan.say "And there mood swings are no fun either!"
    elif morgan.male >= 75:
        show morgan annoyed
        morgan.say "Geez, calm down - it happens every year, nothing to get worked up about!"
    elif morgan.male >= 25:
        show morgan happy
        morgan.say "Aw, thanks [hero.name] - it means a lot that you remembered."
        $ morgan.love += 3
    elif morgan.sub < 75:
        show morgan surprised
        morgan.say "You remembered?"
        show morgan blushhappy
        morgan.say "Well, now I feel really special!"
        $ morgan.love += 3
    else:
        show morgan happy
        morgan.say "Yay, thanks [hero.name] - I'm so excited!"
        $ morgan.love += 3
    hide morgan
    return

init:
    define nickname_dude = ["Dude", "dude"]
    define nickname_dearest = ["Dearest", "dearest"]
    define nickname_brah = ["Brah", "brah"]

label command_nickname_morgan:
    menu:

        "Call me Dude" if active_girl.flags.mikeNickname not in nickname_dude and morgan.male > 60:
            $ active_girl.flags.mikeNickname = "Dude"
        "Stop calling me Dude" if active_girl.flags.mikeNickname in nickname_dude:
            $ active_girl.flags.mikeNickname = None


        "Call me Dearest" if active_girl.flags.mikeNickname not in nickname_dearest and morgan.male < 40:
            $ active_girl.flags.mikeNickname = "Dearest"
        "Stop calling me Dearest" if active_girl.flags.mikeNickname in nickname_dearest:
            $ active_girl.flags.mikeNickname = None


        "Call me Brah" if active_girl.flags.mikeNickname not in nickname_brah and active_girl.sub > 75:
            $ active_girl.flags.mikeNickname = "Brah"
        "Stop calling me Brah" if active_girl.flags.mikeNickname in nickname_brah:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_morgan_male:
    mike.say "Hey, Morgan..."
    mike.say "It's a pretty crazy story, isn't it - how we got here?"
    show morgan talkative
    morgan.say "You can say that again, [hero.name]!"
    show morgan normal
    mike.say "I was thinking - maybe we should keep that crazy alive?"
    mike.say "Maybe you could mention it when you say hi to me?"
    mike.say "How you want to prove to me again that you're all woman?"
    if morgan.sub >= 70 or morgan.is_sex_slave:
        show morgan blushhappy
        morgan.say "Well, I DO like it when you remind me that I'm a woman..."
        morgan.say "So what the hell, [hero.name] - let's do it!"
        morgan.say "I don't want anyone to mistake me for a boy again."
        $ morgan.flags.submissive_interact = True
    else:
        show morgan whining
        morgan.say "Don't you think that's just a little bit insensitive, [hero.name]?"
        morgan.say "That's an issue that I've struggled with for years."
        morgan.say "One that's kind of shaped the person I've grown to become."
        show morgan sad
        mike.say "Ah...when you put it like that, Morgan..."
        mike.say "Maybe you're right and we should forget about it."
        $ morgan.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
