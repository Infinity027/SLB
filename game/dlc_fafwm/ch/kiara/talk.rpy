label kiara_talk_love_male:
    show kiara
    kiara.say "Back home I have no problem talking to people, [hero.name]."
    kiara.say "My people are warm and open about many things - even about the subject of love."
    kiara.say "But here, it feels like people are so close-off and uptight."
    kiara.say "As if to talk of love is a taboo of some kind."
    menu:
        "Not everyone here is like that":
            mike.say "I know what you mean, Kiara, and I wish people weren't so hung-up on that kind of stuff."
            mike.say "But not everyone around here is like that - some of us are into talking about our feelings."
            show kiara smile
            mike.say "Like me, for example, I'd be happy to talk to you about love whenever you want to."
            $ kiara.love += 1
        "Not everyone is as open as you are":
            mike.say "Well that's just how things are in this country, Kiara."
            mike.say "So you might want to keep your thoughts on love to yourself."
            show kiara sad
            mike.say "Better that than offending a whole bunch of people."
            $ kiara.love -= 1
        "You just need someone to teach you how to be around here":
            mike.say "It's only natural that you'd feel awkward in a foreign country, Kiara."
            mike.say "What you need is someone to school you on proper social etiquette."
            show kiara flirt
            mike.say "But don't worry, just take all of your cues from me, and you won't go far wrong."
            $ kiara.sub += 1
    return

label kiara_talk_sex_male:
    show kiara
    kiara.say "Sex is such a natural thing, so central to what it is to be human."
    kiara.say "Without it, none of us would be here today, it is that important."
    kiara.say "That is why I think that we should be talking about it more, don't you agree?"
    menu:
        "It's so refreshing to hear that":
            mike.say "I wish there were more people who thought that way, Kiara."
            mike.say "I'm sure half the problems we have with sex come from being up-tight about it."
            show kiara smile
            mike.say "Talking about something is always the best way to understand it."
            $ kiara.love += 1
        "You have to have some boundaries":
            mike.say "You can't just go bringing up sex in a random conversation, Kiara!"
            mike.say "There are some people who just can't handle that kind of thing."
            show kiara sad
            mike.say "Plus there are those who'll just think you're some kind of sex-crazed loon."
            $ kiara.love -= 1
        "You are so right and I want you to enlighten me further":
            mike.say "You are so right, Kiara - but you know so much more about it than me."
            mike.say "Would...would you be willing to share your wisdom?"
            show kiara mischievous
            mike.say "I promise that I'd be a very attentive pupil."
            $ kiara.sub -= 1
    return

label kiara_talk_politics_male:
    show kiara
    kiara.say "I keep seeing all of these politicians on the TV and speaking on the radio."
    kiara.say "And if I don't catch the name of who it is that happens to be talking..."
    kiara.say "Well, I cannot tell them apart from each other!"
    menu:
        "Politicians are all the same":
            mike.say "You took the words right out of my mouth, Kiara."
            mike.say "Sometimes I think that you could swap one of them's script for the other."
            show kiara smile
            mike.say "And I bet even they wouldn't notice you'd done it."
            $ kiara.love += 1
        "You don't need to worry about politics":
            mike.say "It's probably because you're missing the subtleties of their arguments, Kiara."
            mike.say "You should just forget all about what they're trying to sell you."
            show kiara sad
            mike.say "Just focus all of your attention on looking pretty instead - you'll be happier that way."
            $ kiara.love -= 1
        "I really don't do politics":
            mike.say "I'm way worse than you, Kiara!"
            mike.say "I can't even make sense of what they're promising to do or not do."
            show kiara smile
            mike.say "Maybe you could explain as much as you understand to me?"
            $ kiara.sub -= 1
    return

label kiara_talk_food_male:
    show kiara
    kiara.say "There are so many junk-food restaurants in this city."
    kiara.say "Sometimes I worry that people are losing the ability to cook."
    kiara.say "And who knows what harm the rubbish they eat is doing them?"
    menu:
        "Don't be such a snob":
            mike.say "Well you run a cafe, so you would say that, wouldn't you?"
            mike.say "Plus it's kind of snobbish to think people don't know what they're eating."
            show kiara upset
            mike.say "You can always make up it down the gym too."
            $ kiara.love -= 1
        "You just don't know what's out there":
            mike.say "You don't get out much, do you, Kiara?"
            mike.say "I bet you spend all of your time at the cafe."
            show kiara flirt
            mike.say "You should let me take you out and show you where the good stuff can be found."
            $ kiara.sub += 1
        "I wish you'd feed me every single meal":
            mike.say "You should know what you're talking about, Kiara - you do run a cafe!"
            mike.say "I know that I love eating there every chance I get."
            show kiara smile
            mike.say "In fact, I wish I could eat your food for every meal!"
            $ kiara.sub -= 1
    return

label kiara_talk_travels_male:
    show kiara
    kiara.say "I think that it's good to leave your home country and travel the world."
    kiara.say "Whether you stay for a short while, or choose to remain in a foreign place for years..."
    kiara.say "It broadens the mind, enriches the soul and makes you appreciate people so much more."
    menu:
        "It certainly made me appreciate you":
            mike.say "Travelling always sounds like such a great thing to do."
            mike.say "And I can't argue with you when you say it helps to appreciate people."
            show kiara smile
            mike.say "Because without it, I'd never have had the chance to appreciate you."
            $ kiara.love += 1
        "Travelling sounds like such a chore":
            mike.say "Who needs to travel when you have everything you need right here?"
            mike.say "Sounds like a whole lot of wasted effort if you ask me."
            show kiara unhappy
            mike.say "And you need to have all the right paperwork - like, is your visa still valid?"
            $ kiara.love -= 1
        "That sounds romantic and naive":
            mike.say "All of that sounds so lovely and romantic, Kiara."
            mike.say "But the reality is that you need someone who knows the place, a native guide, yeah?"
            show kiara sad
            mike.say "Otherwise you're pretty exposed and vulnerable in a foreign country."
            $ kiara.sub += 1
    return

label kiara_talk_tv_male:
    show kiara
    kiara.say "I confess that I do not have the time for television these days."
    kiara.say "There are so many channels and so many series whenever I happen to look."
    kiara.say "It is so confusing that I usually end up reading a book instead."
    menu:
        "You're so mature and sophisticated":
            mike.say "You know that really doesn't surprise me at all, Kiara."
            mike.say "You always came across to me as the more intellectual type."
            show kiara smile
            mike.say "The kind of person with an enquiring mind and a voracious intellect too."
            $ kiara.love += 1
        "You're just out of touch":
            mike.say "Sounds like you've just decided to give up on the whole thing, Kiara!"
            mike.say "I mean sure, there's a lot to choose from - but a lot of it is absolute gold."
            show kiara sad
            mike.say "You're just cheating yourself out of great entertainment if you give up on it."
            $ kiara.love -= 1
        "Would you choose something for me to read":
            mike.say "I wish that I could be like you, Kiara."
            mike.say "But I'm such a sucker for flashy new TV series!"
            show kiara smile
            mike.say "Actually, would you recommend me a book to read?"
            $ kiara.sub -= 1
    return

label kiara_talk_sports_male:
    show kiara
    kiara.say "They love sports here and they love sports back home in my country."
    kiara.say "Some people you meet, it seems like sport is the only thing in their lives."
    kiara.say "Personally, I think they are into sports because they don't have anything else."
    menu:
        "There's so much more to life":
            mike.say "You're right, Kiara - there's so much more to life than sports."
            mike.say "Some of the folks I know, they act like it's the end of the world when their team loses."
            show kiara smile
            mike.say "I always assume they're compensating for something."
            $ kiara.love += 1
        "You just don't get it":
            mike.say "People who say that are usually covering up their lack of knowledge, Kiara."
            mike.say "Next time there's a game on the TV, we'll sit down and watch it together."
            show kiara upset
            mike.say "Trust me, once you shut up and listen to me explain it all, you'll soon understand the appeal."
            $ kiara.love -= 1
        "I was never very good at sports":
            mike.say "I hate people that talk about sports, Kiara."
            mike.say "It reminds me of always being picked last in gym class."
            mike.say "And I worry that it's left me meek and needy."
            show kiara smile
            mike.say "Needing someone like you to protect me!"
            $ kiara.sub -= 1
    return

label kiara_talk_fashion_male:
    show kiara
    kiara.say "Fashion is not about trends - trends are things that come and go."
    kiara.say "No, fashion is about style, about classic looks that endure."
    kiara.say "And this is the key to remaining in fashion no matter what the current trend."
    menu:
        "Or maybe you're just out of touch":
            mike.say "I don't know, Kiara - that kind of sounds like an excuse to me."
            mike.say "Like the kind of thing someone that's lost their touch would say."
            show kiara upset
            mike.say "You know, to convince themselves that they weren't too old for what they're wearing?"
            $ kiara.love -= 1
        "I think you might need a second opinion":
            mike.say "Look, Kiara - if you want me to approve what you're wearing, then just say so."
            mike.say "There's no need to beat around the bush looking for compliments all the time."
            show kiara flirt
            mike.say "Just send me a photo of what you're thinking of wearing, and I'll say yes or no in future."
            $ kiara.sub += 1
        "You're a style icon":
            mike.say "I think your look is totally timeless, Kiara."
            mike.say "Like an old-fashioned movie star or something, yeah?"
            show kiara smile
            mike.say "Hell, I'm even thinking of asking you to advise me on my wardrobe choices!"
            $ kiara.love += 1
    return

label kiara_talk_books_male:
    show kiara
    kiara.say "I have just finished the most amazing book, just amazing."
    kiara.say "It was so enthralling that I could not put it down until it was done."
    kiara.say "Would you like to know what the title was?"
    menu:
        "I love to read":
            mike.say "I'd certainly love to know what the book's called, Kiara."
            mike.say "But I can't promise that I'll find the time to read it."
            show kiara smile
            mike.say "Because I'm always in the middle of a book or two myself."
            $ kiara.love += 1
        "I'll wait for the movie":
            mike.say "Nah, I'll pass - it's probably some weird, foreign book anyway."
            mike.say "I'm more into reading comic-books these days anyway."
            show kiara pout
            mike.say "Plus if it's any good they'll make it into a film, and I can watch that."
            $ kiara.love -= 1
        "I devour books":
            mike.say "I'm getting through a few books a week at the moment, Kiara."
            mike.say "So it'd probably be easier if I recommended some titles to you."
            show kiara smile
            mike.say "Be warned though, my tastes are pretty high-brow and challenging!"
            $ kiara.sub += 1
    return

label kiara_talk_people_male:
    show kiara
    kiara.say "When you run a cafe like mine, you get to meet a lot of people."
    kiara.say "They come from all different walks of life, from different places."
    kiara.say "But the strange thing is that you realise, they are all basically the same, no?"
    menu:
        "That is so profound":
            mike.say "I suppose you'd know better than I would, Kiara."
            mike.say "But that does sound like it makes perfect sense."
            show kiara smile
            mike.say "In fact, it's almost poetic and philosophical at the same time."
            $ kiara.love += 1
        "You haven't met everyone":
            mike.say "Yeah, but that's just based on the people coming into your cafe, right?"
            mike.say "Like, what if there's a specific type of person that is turned-off by the place?"
            mike.say "And what if they're totally different to the people that like it?"
            show kiara upset
            mike.say "Then your little nugget of wisdom sounds pretty dumb!"
            $ kiara.love -= 1
        "You must be so wise":
            mike.say "I love it when you philosophise, Kiara - it's so impressive."
            mike.say "You must have gained so much wisdom running a place like your cafe."
            show kiara smile
            mike.say "Would you mind teaching some of it to me?"
            $ kiara.sub -= 1
    return

label kiara_talk_computers_male:
    show kiara
    kiara.say "I know that these days the world must have computers for it to run."
    kiara.say "But that does not mean that I have to like them."
    kiara.say "Complicated, high-maintenance and easily made to go haywire - they are impossible!"
    menu:
        "That sounds familiar":
            mike.say "That's pretty funny, Kiara, you describing them like that."
            mike.say "Because if you hadn't mentioned you were talking about computers..."
            show kiara upset
            mike.say "Well, I could just as easily have believed you were talking about yourself!"
            $ kiara.love -= 1
        "Oh I see that you don't understand them":
            mike.say "Why didn't you just say that you don't understand them, Kiara?"
            mike.say "It's not a big deal, as loads of people your age struggle with new technology."
            show kiara pout
            mike.say "Just show me what's confusing you, and I'll make it as simple as I can, okay?"
            $ kiara.sub += 1
        "I long for a more simple life":
            mike.say "I'll let you in on a little secret, Kiara - I hate computers too!"
            mike.say "I just feel like someone of my generation isn't allowed to say so."
            show kiara smile
            mike.say "Would you tell me all about what you think is wrong with them?"
            $ kiara.love += 1
    return

label kiara_talk_music_male:
    show kiara
    kiara.say "Music is like fashion, in my opinion - the true classics are timeless."
    kiara.say "There will always be new music that is selling and going to the top of the charts."
    kiara.say "But where are the new classics to come from - where is the new Bowie, Marley or Simone?"
    menu:
        "Nothing beats the classics":
            mike.say "I know what you mean, Kiara - and there is a real difference."
            mike.say "Like when you're in a place and a song comes on that you've known since you were a kid."
            show kiara smile
            mike.say "And suddenly everyone is singing along, no matter what their age - it's magical."
            $ kiara.love += 1
        "You just don't know what's hot":
            mike.say "That's such a stereotypical answer, Kiara!"
            mike.say "Tells me that you're massively out of touch too."
            show kiara pout
            mike.say "Someone needs to let me educate them on the subject of modern music."
            $ kiara.sub += 1
        "Would you come and vet my record collection":
            mike.say "Sounds like you really know what you're talking about, Kiara."
            mike.say "I don't suppose you want to come over and go through my record collection?"
            show kiara smile
            mike.say "You could tell me what I need to add to it and what need to be thrown out too."
            $ kiara.sub -= 1
    return

label kiara_talk_birthday_male:
    show kiara
    mike.say "Happy birthday, Kiara..."
    mike.say "And many happy returns too!"
    kiara.say "Oh, thank you so much, [hero.name]."
    kiara.say "It is so kind and thoughtful of you to remember the date."
    return

label command_nickname_kiara:
    menu:

        "Call me Sugar" if active_girl.flags.mikeNickname not in nickname_sugar and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Sugar"
        "Stop calling me Sugar" if active_girl.flags.mikeNickname in nickname_sugar:
            $ active_girl.flags.mikeNickname = None


        "Call me Honey" if active_girl.flags.mikeNickname not in nickname_honey and hero.flags.office_boss == "mike":
            $ active_girl.flags.mikeNickname = "Honey"
        "Stop calling me Honey" if active_girl.flags.mikeNickname in nickname_honey:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
