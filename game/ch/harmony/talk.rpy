init python:
    VHP = 90
    HP = 60
    AP = 50
    LP = 40
    VLP = 10

label harmony_talk_love_male:
    mike.say "Be honest, harmony - what's your take on love?"
    if harmony.purity >= VHP:
        harmony.say "Oh, [hero.name] - of course I believe in love!"
        show harmony happy
        harmony.say "God loves all of his children, and so we should love each other too!"
    elif harmony.purity >= HP:
        harmony.say "I believe in true love, really I do."
        show harmony happy
        harmony.say "It's the most beautiful thing I can imagine existing between two people!"
    elif harmony.purity < VLP:
        harmony.say "Forget all of that gushing, sentimental crap."
        show harmony blush
        harmony.say "There's no way I could love someone without a massive cock!"
        $ harmony.purity -= 1
    elif harmony.purity < LP:
        harmony.say "Well...there's two kinds of love, isn't there?"
        harmony.say "Love like you get in poetry and on Valentines cards - and then there's the OTHER kind of love!"
        harmony.say "And I don't see why you can't have both!"
    else:
        harmony.say "It's not easy - but I believe love's real."
        harmony.say "You just have to work hard for it, like anything worth having in life."
    $ harmony.love += 1
    return

label harmony_talk_sex_male:
    mike.say "When it comes to sex, are you a modern girl, or more traditional?"
    if harmony.purity >= VHP:
        show harmony angry
        harmony.say "Temptation was the original sin!"
        harmony.say "We should never give in to temptation."
        $ harmony.love -= 1
    elif harmony.purity >= HP:
        show harmony annoyed
        harmony.say "That's hardly an appropriate subject for you to be asking me about!"
        harmony.say "Especially as we're not married - or even engaged."
        $ harmony.love -= 1
    elif harmony.purity < VLP:
        harmony.say "I can't believe what a prude I used to be!"
        show harmony blush
        harmony.say "I guess a big, hard cock inside of me was just what I needed to get over that..."
        $ harmony.love += 1
    elif harmony.purity < LP:
        harmony.say "I used to be really uptight about anything to do with sex."
        show harmony happy
        harmony.say "But since I met you, I've been turned onto it in a big way!"
        $ harmony.love += 1
    else:
        harmony.say "Oh, [hero.name], stop it - you're embarrassing me!"
        $ harmony.sub += 1
    return

label harmony_talk_politics_male:
    mike.say "What side of the political divide are you on, Harmony?"
    if harmony.purity >= HP:
        harmony.say "You shouldn't judge a politician on their policies."
        harmony.say "Only on if they've got good, Christian values."
    else:
        show harmony angry
        harmony.say "Urgh...politics is a real turn-off!"
        harmony.say "I'd rather we talk about something else."
    $ harmony.love -= 1
    return

label harmony_talk_food_male:
    mike.say "You ever feel like going out and grabbing something to eat, Harmony?"
    if harmony.purity >= HP:
        harmony.say "I...I want to, really I do..."
        show harmony annoyed
        harmony.say "But gluttony is one of the Seven Deadly Sins!"
    elif harmony.purity >= VLP:
        harmony.say "Ah...yeah, sure I do."
        harmony.say "But the problem is that I think about it a little TOO much!"
    else:
        harmony.say "I don't know about that."
        show harmony blush
        harmony.say "But NOTHING tastes better than your cock, [hero.name]!"
    $ harmony.sub += 1
    return

label harmony_talk_travels_male:
    mike.say "Okay, Harmony - you have a plane ticket to anywhere in the world, so where do you go?"
    if harmony.purity >= VHP:
        harmony.say "Oh, that's easy."
        harmony.say "I'd fly straight to Rome, or maybe Jerusalem."
        show harmony happy
        harmony.say "Just imagine being somewhere so holy and touched by the hand of God!"
    elif harmony.purity >= LP:
        harmony.say "I've always thought about going to Africa."
        harmony.say "No for a holiday, but as a volunteer, you know - for a charity or something like that?"
    else:
        harmony.say "Who cares where the plane ends up flying to?"
        show harmony blush
        harmony.say "So long as it's in the air long enough for me to get fucked in the bathroom!"
    $ harmony.love += 1
    return

label harmony_talk_tv_male:
    mike.say "You keep up with TV in general, Harmony - or just the latest box-sets?"
    if harmony.purity >= VHP:
        harmony.say "I don't watch much mainstream TV, because it's almost always sinful."
        harmony.say "But there is this one Televangelist, and I just can't bear to miss his show."
        show harmony happy
        harmony.say "Maybe we could watch it together sometime?"
    elif harmony.purity >= HP:
        harmony.say "I used to watch a lot of those evangelical TV shows."
        harmony.say "But recently, I've just been, well - turned off by them, I guess."
        show harmony annoyed
        harmony.say "For some reason, I can't help thinking that they're all hypocrites!"
    elif harmony.purity < VLP:
        show harmony happy
        harmony.say "Oh, porn is SO GOOD!"
        harmony.say "I can't believe that I only just started watching this stuff!"
        harmony.say "I want to watch it ALL the time!"
    elif harmony.purity < LP:
        harmony.say "I used to like the naughty stuff in that show with the dragons - it was a real turn-on!"
        harmony.say "But just recently, I actually started watching a little bit of porn!"
        show harmony happy
        harmony.say "Can you believe that?!?"
    else:
        harmony.say "I just keep finding more and more stuff that I like on the TV these days."
        harmony.say "Historical dramas and stuff like that are the best."
        show harmony happy
        harmony.say "But I do like that show with the dragons in it, for some reason..."
    $ harmony.love += 1
    return

label harmony_talk_sports_male:
    mike.say "You play any sports, Harmony?"
    if harmony.purity >= VHP:
        harmony.say "Ah, no...I don't."
        show harmony annoyed
        harmony.say "But I know that I should, and that sloth is a terrible, terrible sin!"
    elif harmony.purity >= HP:
        harmony.say "Erm, no...no, I don't."
        harmony.say "I really should though, as I do want to be healthier in general!"
    elif harmony.purity < VLP:
        harmony.say "No, I don't - and I used to worry about it a hell of a lot too - my weight, that is."
        harmony.say "But then I just learned to stop caring and get over it."
        harmony.say "After all, men like big tits and an ass they can rest a drink on - right?"
    elif harmony.purity < LP:
        harmony.say "No...but I'm sure you could teach me how to play some, [hero.name]."
        harmony.say "There must be lots of fun ways we could work up a sweat together!"
    else:
        harmony.say "No, I don't - and I know that I should!"
        show harmony annoyed
        harmony.say "I do look in the mirror regularly, so believe me, I can see that I need to lose weight."
    $ harmony.love -= 1
    return

label harmony_talk_fashion_male:
    mike.say "Are you up on the latest trends, Harmony?"
    if harmony.purity >= VHP:
        show harmony annoyed
        harmony.say "Urgh, I should think not!"
        harmony.say "Vanity is one of the most heinous of sins!"
    elif harmony.purity >= HP:
        harmony.say "Who, me?"
        harmony.say "Oh no, I'm not really interested in that sort of thing."
    elif harmony.purity < VLP:
        harmony.say "Only if it gets guys to look at me in that certain way!"
        harmony.say "I can't believe that I used to be shy about things like that too!"
    elif harmony.purity < LP:
        harmony.say "I really shouldn't be telling you this..."
        harmony.say "But if you promise that you won't laugh?"
        harmony.say "I've...I've been buying some sexy underwear and...and liking the feel of it too!"
    else:
        harmony.say "I don't follow fashion like it's a religion or anything, no."
        harmony.say "But I have been seeing more things that catch my eye in the shops just recently."
    return

label harmony_talk_books_male:
    mike.say "Read any good books lately, Harmony?"
    if harmony.purity >= HP:
        harmony.say "I'm always reading from the Bible."
        harmony.say "All the truth and wisdom that a person needs can be found within it's pages."
        harmony.say "If only people would realise that, life would be so much simpler for us all!"
        $ harmony.love += 1
    elif harmony.purity < LP:
        harmony.say "Yeah...but nah."
        harmony.say "I'm not really that interested."
    else:
        harmony.say "Before now I'd have said not."
        harmony.say "But I picked up one of those women's magazines the other day, just on a whim."
        harmony.say "And there was actually a couple of articles that, once I started reading, I couldn't put down."
        $ harmony.love += 1
    return

label harmony_talk_people_male:
    mike.say "Hey, Harmony - hear any juicy gossip recently?"
    if harmony.purity >= VHP:
        harmony.say "I don't know about that."
        show harmony happy
        harmony.say "But I can tell you that the new priest at my church is AWESOME!"
    elif harmony.purity >= HP:
        show harmony annoyed
        harmony.say "Shame on you, [hero.name]!"
        harmony.say "You should know better than to pry into other people's business."
    elif harmony.purity < VLP:
        harmony.say "I'm not interested in the slightest - unless you have some dirt on the guys I see on TV?"
        harmony.say "They're so hot and manly that I'd kill to know what they get up to..."
    elif harmony.purity < LP:
        harmony.say "Oh, I WISH that I had!"
        harmony.say "I just LOVE to hear something that's dripping with scandal!"
    else:
        harmony.say "I know that it's wrong, and really I shouldn't."
        harmony.say "But I do like a little bit of juicy gossip here and there!"
    return

label harmony_talk_computers_male:
    mike.say "Spend much time with computers, Harmony?"
    harmony.say "I'm not really interested in computers."
    $ harmony.love -= 1
    return

label harmony_talk_music_male:
    mike.say "What kind of music are you into, Harmony?"
    if harmony.purity >= VHP:
        harmony.say "I only really have time for religious music."
        harmony.say "Anything else is a distraction from the will of the Almighty."
    elif harmony.purity < LP:
        harmony.say "If you'd asked me before now, I'd have said I didn't care."
        harmony.say "But whenever I dance, I keep finding myself falling in love with music."
        harmony.say "Or maybe with the way that men can't help watching me on the dance-floor!"
    else:
        harmony.say "Huh, it's weird - I'm not really that interested in music."
    return

label harmony_talk_birthday_male:
    show harmony happy
    harmony.say "Thank you for remembering."
    $ harmony.love += 3
    hide harmony
    return

init:
    define nickname_my_friend = ["My friend", "my friend"]
    define nickname_stallion = ["Stallion", "stallion"]
    define nickname_demon = ["Demon", "demon"]
    define nickname_my_angel = ["My angel", "my angel"]

label command_nickname_harmony:
    menu:

        "Call me My friend" if active_girl.flags.mikeNickname not in nickname_my_friend and harmony.purity >= HP:
            $ active_girl.flags.mikeNickname = "My friend"
        "Stop calling me My friend" if active_girl.flags.mikeNickname in nickname_my_friend:
            $ active_girl.flags.mikeNickname = None


        "Call me Stallion" if active_girl.flags.mikeNickname not in nickname_stallion and harmony.purity <= LP:
            $ active_girl.flags.mikeNickname = "Stallion"
        "Stop calling me Stallion" if active_girl.flags.mikeNickname in nickname_stallion:
            $ active_girl.flags.mikeNickname = None


        "Call me Demon" if active_girl.flags.mikeNickname not in nickname_demon and harmony.purity <= VLP and active_girl.sub > 80:
            $ active_girl.flags.mikeNickname = "Demon"
        "Stop calling me Demon" if active_girl.flags.mikeNickname in nickname_demon:
            $ active_girl.flags.mikeNickname = None


        "Call me My angel" if active_girl.flags.mikeNickname not in nickname_my_angel and harmony.purity <= VHP and active_girl.love > 160:
            $ active_girl.flags.mikeNickname = "My angel"
        "Stop calling me My angel" if active_girl.flags.mikeNickname in nickname_my_angel:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_harmony_male:
    mike.say "Hey, Harmony..."
    mike.say "I had a great idea."
    show harmony talkative
    harmony.say "Ooh, tell me all about it, [hero.name]!"
    show harmony normal
    mike.say "Well, I know how you're keen on Jesus."
    mike.say "And I know that you like a certain part of my anatomy..."
    show harmony talkative
    harmony.say "Ah...I think I can guess where this is going!"
    show harmony normal
    mike.say "So how about you telling me that you want to worship my cock?"
    if harmony.sub >= 70 or harmony.is_sex_slave:
        show harmony blush
        harmony.say "Oh, that is SO wicked of you!"
        harmony.say "But it's the truth, and it'd be a sin to lie."
        harmony.say "So I guess I have no choice but to say it!"
        $ harmony.flags.submissive_interact = True
    else:
        show harmony angry
        harmony.say "What kind of a crazy idea is that?!?"
        harmony.say "It must be blasphemous in at least a dozen different ways!"
        show harmony upset
        mike.say "Okay, okay..."
        mike.say "I'll take that as a no."
        $ harmony.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
