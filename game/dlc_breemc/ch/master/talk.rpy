label master_talk_love_female:
    show master
    bree.say "Tell me, O great master..."
    bree.say "Is there room in the world of martial arts for..."
    bree.say "Well...for love?"
    master.say "He, he, he..."
    master.say "Why of course there is, my dear!"
    master.say "Mastery of the carnal arts is as important as that of the martial and spiritual!"
    master.say "And when the time is right, I hope to instruct you in those too!"
    $ master.love += 1
    hide master
    return

label master_talk_sex_female:
    show master
    bree.say "I guess that making love is pretty good exercise, right, Master?"
    bree.say "I mean, it works all of your muscles and burns fat."
    bree.say "So it has to help!"
    master.say "Your wisdom grows greater with each day that passes, my dear!"
    master.say "Indeed, sex is not only good, it is essential!"
    master.say "You must indulge as often and as intensely as possible!"
    $ master.love += 1
    hide master
    return

label master_talk_politics_female:
    show master
    bree.say "What with you training my body and my mind, things seem much more clear to me."
    bree.say "But what other wisdom can you impart, my master?"
    bree.say "Like, what way should I vote in the elections?"
    master.say "Bah!"
    master.say "Those are base and immoral concerns!"
    master.say "Politicians are corrupt and often perverted people!"
    bree.say "Hmm..."
    bree.say "I wonder you can teach me about hypocrisy..."
    $ master.love -= 1
    hide master
    return

label master_talk_food_female:
    show master
    bree.say "Ooh..."
    bree.say "I'm sorry, master - but I'm SO hungry right now!"
    bree.say "And I know that I should be ignoring such base instincts."
    master.say "Good heavens no, my dear!"
    master.say "That's your divine young body trying to tell you something."
    master.say "It's crying out to have it's appetites sated!"
    master.say "And it's your duty to make sure those appetites are satisfied - whatever they might be..."
    hide master
    return

label master_talk_travels_female:
    show master
    bree.say "You must have travelled far and wide, my master."
    bree.say "Tell me, what hidden temples and forbidden valleys did you see on your quest for enlightenment?"
    master.say "Hah!"
    master.say "One does not need to wander the world to find enlightenment, my dear."
    master.say "I have seen all that I need to see right here, hiding in the dunes by the beach."
    master.say "And some of the things I have seen helped to turn my beard white!"
    hide master
    return

label master_talk_tv_female:
    show master
    bree.say "I guess that you don't watch much television, master?"
    bree.say "It would be a distraction from spiritual matters, right?"
    master.say "Precisely, my dear!"
    master.say "Television is a trap of the physical world, one which we must overcome!"
    master.say "Now videotapes of nude ladies doing naughty things to each other - that is a different matter entirely..."
    $ master.love -= 1
    hide master
    return

label master_talk_sports_female:
    show master
    bree.say "Sports are good, right, my master?"
    bree.say "Like, they should help me in my pursuit of physical perfection?"
    master.say "No, no, no!"
    master.say "Professional sports are your enemy!"
    master.say "They require your mentor to fill in forms and admit any...past offences or convictions!"
    master.say "Now pole-dancing, on the other hand..."
    $ master.love += 1
    hide master
    return

label master_talk_fashion_female:
    show master
    bree.say "I was wondering what I should wear when we train, master?"
    bree.say "Maybe I should buy some new tracksuits or a Karate gi?"
    master.say "Bah!"
    master.say "The catwalk is the path to spiritual oblivion!"
    master.say "You must unburden yourself of it's shackles!"
    master.say "Basically, wear as little as possible, my dear."
    master.say "And make sure what you do wear is made of lycra..."
    hide master
    return

label master_talk_books_female:
    show master
    bree.say "Can you recommend any good books for me to study, my master?"
    bree.say "Surely you must have read much about mysticism and magic?"
    master.say "Books concern what has been and what is now in the past, my dear."
    master.say "You must learn to focus on the present and what happens in the moment."
    master.say "The obvious exception being nudie magazines..."
    $ master.love -= 1
    hide master
    return

label master_talk_people_female:
    show master
    bree.say "I was thinking that I might go to a spiritual retreat, master."
    bree.say "You know, get away from other people for a couple of days?"
    master.say "No, no, no!"
    master.say "You must not isolate yourself, my dear!"
    master.say "You must embrace intercourse with your fellow beings!"
    master.say "Intercourse of all kinds..."
    hide master
    return

label master_talk_computers_female:
    show master
    bree.say "I've been following your teachings to the letter, master."
    bree.say "And it's weird - I haven't been on my laptop in days!"
    bree.say "That's good, right?"
    master.say "No, my dear, it is not!"
    master.say "You must not isolate yourself from the real world."
    master.say "And not from something as wonderful as a computer!"
    master.say "On which you can see such...enlightening images..."
    $ master.love += 1
    hide master
    return

label master_talk_music_female:
    show master
    bree.say "Oh, I was just listening to some music, my master."
    bree.say "But I'll turn it off, okay?"
    bree.say "I don't want it to distract me from your teachings!"
    master.say "No need, my dear, no need!"
    master.say "Especially if it's something that gets you moving."
    master.say "And makes you jiggle in that particular way..."
    hide master
    return

label master_talk_birthday_female:
    show master
    bree.say "Happy Birthday, master!"
    bree.say "Have an enlightened one!"
    master.say "Huh?!?"
    master.say "How did you find that out?"
    master.say "I thought my records were still sealed under that court order!"
    $ master.love += 3
    hide master
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
