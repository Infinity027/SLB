label lexi_talk_love_male:
    show lexi
    if lexi.love < 50:
        show lexi annoyed
        lexi.say "Love sucks..."
        lexi.say "That's why I love to do it so much."
        $ lexi.love -= 1
    else:
        show lexi wink
        lexi.say "I do hope that I will meet my prince in shining armor sometime."
        $ lexi.love += 1
    hide lexi
    return

label lexi_talk_sex_male:
    show lexi happy
    lexi.say "Sex on drugs is the best sex there is."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_politics_male:
    show lexi bubblegum
    pause 2
    show lexi annoyed
    lexi.say "What?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_food_male:
    show lexi wink
    lexi.say "My favorite food is man milk, straight from the source."
    $ lexi.sub += 1
    hide lexi
    return

label lexi_talk_travels_male:
    show lexi annoyed
    lexi.say "I went to Vegas once, for work."
    $ lexi.love -= 1
    hide lexi
    return

label lexi_talk_tv_male:
    show lexi happy
    lexi.say "I love reality shows."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_sports_male:
    show lexi
    lexi.say "What? No."
    hide lexi
    return

label lexi_talk_fashion_male:
    show lexi happy
    lexi.say "A girl needs to dress to attract the eye."
    $ lexi.love += 1
    hide lexi
    return

label lexi_talk_books_male:
    show lexi angry
    lexi.say "Are you kidding me?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_people_male:
    show lexi
    lexi.say "People?"
    hide lexi
    return

label lexi_talk_computers_male:
    show lexi angry
    lexi.say "Seriously?"
    $ lexi.love -= 2
    hide lexi
    return

label lexi_talk_music_male:
    show lexi
    lexi.say "R&B I guess..."
    hide lexi
    return

label lexi_talk_birthday_male:
    show lexi happy
    lexi.say "Thank you so much for remembering!"
    $ lexi.love += 3
    hide lexi
    return

init:
    define nickname_naughty_boy = ["Naughty boy", "naughty boy"]
    define nickname_studmuffin = ["Studmuffin", "studmuffin"]

label command_nickname_lexi:
    menu:

        "Call me Naughty boy" if active_girl.flags.mikeNickname not in nickname_naughty_boy and active_girl.flags.peeped_count >= 1:
            $ active_girl.flags.mikeNickname = "Naughty boy"
        "Stop calling me Naughty boy" if active_girl.flags.mikeNickname in nickname_naughty_boy:
            $ active_girl.flags.mikeNickname = None


        "Call me Studmuffin" if active_girl.flags.mikeNickname not in nickname_studmuffin and active_girl.flags.kiss >= 1:
            $ active_girl.flags.mikeNickname = "Studmuffin"
        "Stop calling me Studmuffin" if active_girl.flags.mikeNickname in nickname_studmuffin:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_lexi_male:
    show lexi smile
    mike.say "Hey, Lexi..."
    mike.say "You're open-minded, right?"
    mike.say "I mean, you like to have fun?"
    show lexi normal
    lexi.say "Sure, [hero.name]."
    lexi.say "I did last time I checked."
    show lexi smile
    mike.say "Then how about we spice things up when you say hi to me?"
    mike.say "Like maybe offer me a piece of your ass or something like that?"
    if lexi.sub >= 70 or lexi.is_sex_slave:
        show lexi flirt
        lexi.say "Well, I do like letting you have a piece of it!"
        lexi.say "And if it makes you happy, then it makes me happy too."
        show lexi happy
        lexi.say "Alright, I'm in!"
        $ lexi.flags.submissive_interact = True
    else:
        show lexi angry
        lexi.say "Hah...no chance, [hero.name]!"
        lexi.say "That's the kind of treatment I charge a fee for."
        lexi.say "And you need to earn some serious credit to afford it!"
        show lexi annoyed
        mike.say "Oh, I see...okay, Lexi - let's forget about it."
        $ lexi.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
