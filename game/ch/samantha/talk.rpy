label samantha_talk_love_male:
    show samantha
    $ result = randint(1, 4)
    if result == 1:
        mike.say "You know how they say we only use 10 percent of our brains?"
        samantha.say "I think we only use 10 percent of our hearts."
    elif result == 2:
        samantha.say "Love is like jumping out of an airplane with no parachute."
        show samantha happy
        samantha.say "But there's no need to be frightened, because that plane is still on the ground."
    elif result == 3:
        mike.say "If love were a dolphin with wings and a unicorn's horn, being ridden by a blind leprechaun dressed like Rasputin."
        mike.say "Would you believe in second chances for love at first sight?"
    else:
        mike.say "99 percent honesty is the foundation of any relationship."
        show samantha happy
        samantha.say "What do you do with the 1 percent left?"
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_sex_male:
    show samantha
    $ result = randint(1, 3)
    if result == 1:
        mike.say "I saw a gay porno once."
        mike.say "I didn't know until halfway in."
        mike.say "The girls never came."
        mike.say "The girls never came!"
    elif result == 2:
        if samantha.flags.engaged and not (game.flags.ryandead or samantha.flags.knows_ryancheats or samantha.flags.cuck_ryan):
            samantha.say "You know I can taste Ryan's cum even if I blew him more than two hours ago."
            show samantha happy
            samantha.say "Yummy!"
            mike.say "Gross, you just kissed my cheek."
        else:
            "Samantha licks her lips."
            show samantha blush
            samantha.say "...I miss the taste of cum..."
    else:
        samantha.say "You could not be any more wrong."
        samantha.say "You could try, but you would not be successful."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_politics_male:
    show samantha
    $ result = randint(1, 4)
    if result == 1:
        samantha.say "You shouldn't take life to seriously. You'll never get out alive."
        mike.say "That's so much like you."
    elif result == 2:
        mike.say "You know the world is going crazy when the best rapper is a white guy."
        mike.say "The best golfer is a black guy, the tallest guy in the NBA is Chinese."
        mike.say "The Swiss hold the America's Cup, France is accusing the U.S. of arrogance."
        mike.say "Germany doesn't want to go to war."
        mike.say "And the three most powerful men in America are named 'Bush', 'Dick', and 'Colin'."
        mike.say "Need I say more?"
        show samantha happy
        samantha.say "You are so funny."
    elif result == 3:
        mike.say "Every politician has a promising career."
        mike.say "Unfortunately, most of them do not keep those promises."
    else:
        samantha.say "I am quite worried about those climatic events happening all over the world."
        samantha.say "Our planet is running toward the apocalypse."
        mike.say "Don't worry..."
        mike.say "The planet will be fine."
        mike.say "...But the people are fucked."
        samantha.say "That doesn't reassure me."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_food_male:
    show samantha
    $ result = randint(1, 2)
    if result == 1:
        show samantha blush
        samantha.say "Do you know if they make semen flavored food?"
        mike.say "Yuck..."
        mike.say "But I can be your vending machine if you want."
        $ samantha.sub += 1
    else:
        show samantha happy
        samantha.say "I cook with wine, sometimes I even add it to the food."
        $ samantha.love += 1
    hide samantha
    return

label samantha_talk_travels_male:
    show samantha
    $ result = randint(1, 2)
    if result == 1:
        samantha.say "I really want to go to Paris some day."
        mike.say "Why would you do that, it's full of French people."
    else:
        samantha.say "How can you ever be late for anything in London?"
        show samantha happy
        samantha.say "They have a huge clock right in the middle of the town."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_tv_male:
    show samantha
    samantha.say "I don't watch TV that much."
    hide samantha
    return

label samantha_talk_sports_male:
    show samantha
    samantha.say "A blonde golfer goes into the pro shop and looks around frowning."
    samantha.say "Finally the pro asks her what she wants."
    show samantha annoyed
    samantha.say "'I can't find any green golf balls' the blonde golfer complains."
    show samantha normal
    samantha.say "The pro looks all over the shop, and through all the catalogs, and finally calls the manufacturers and determines that sure enough, there are no green golf balls."
    samantha.say "As the blonde golfer walks out the door in disgust, the pro asks her, 'Before you go, could you tell me why you want green golf balls?'"
    show samantha happy
    samantha.say "'Well obviously, because they would be so much easier to find in the sand traps!'"
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_fashion_male:
    show samantha happy
    if randint(1, 2) == 1:
        samantha.say "I have a really good fashion sense but i'm just too poor to prove it."
    else:
        samantha.say "There is a thin line between looking indie and looking homeless."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_books_male:
    show samantha
    samantha.say "I only read children's books."
    hide samantha
    return

label samantha_talk_people_male:
    show samantha
    samantha.say "It's horrible. Some kid called me 'young lady'."
    mike.say "Ugh, I hate when my father calls me that."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_computers_male:
    show samantha
    samantha.say "I like video games, but they're really violent."
    samantha.say "I'd like to play a video game where you help the people who were shot in all the other games."
    show samantha happy
    samantha.say "It'd be called 'Really Busy Hospital'."
    $ samantha.love += 1
    hide samantha
    return

label samantha_talk_music_male:
    show samantha
    samantha.say "I listen to whatever is on the radio."
    hide samantha
    return

init python:
    SpecificTalkSubject(**{
    "name": "samantha_talk_ryan",
    "display_name": "About Ryan",
    "label": "samantha_talk_ryan_male",
    "duration": 0,
    "icon": "button_ryan",
    "conditions": [
        IsDone("samantha_event_D03"),
        Not(IsDone("samantha_event_D04")),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(samantha,
            IsActive(),
            MinStat("love", 140),
            ),
        ],
    "do_once": False,
    "once_week": True,
    })

label samantha_talk_ryan_male:
    show samantha
    if "samantha_event_D03" in DONE and "samantha_event_D04" not in DONE and samantha.love >= 140:
        call samantha_event_D04 from _call_samantha_event_D04
    else:
        if "samantha_event_03" not in DONE:
            mike.say "I wanted to talk to you about Ryan."
            samantha.say "He is annoying at times, but so sweet I can't help but forgive him."
        elif "samantha_event_04" not in DONE and "samantha_wedding_flag" not in DONE:
            mike.say "Have you chosen a date for the wedding?"
            samantha.say "No, not yet."
        elif "samantha_event_04" in DONE and not samantha.flags.know_ryancheats:
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake, I have something to tell you..."
            else:
                mike.say "Samantha, I have something to tell you..."
            samantha.say "What's up, you look grim."
            mike.say "I saw Ryan at the nightclub."
            mike.say "He was with another girl..."
            show samantha surprised
            samantha.say "WHAT..."
            samantha.say "THAT..."
            show samantha sad
            samantha.say "Are you sure..."
            samantha.say "Of course you are sure."
            show samantha cry
            samantha.say "How could I have been so stupid..."
            samantha.say "Believing I was special..."
            mike.say "You are special, he is just an ass and don't deserve you."
            samantha.say "Thanks [hero.name], I'll talk with him."
            $ samantha.flags.know_ryancheats = True
        else:
            samantha.say "Ryan, really is an asshole, I prefer not to talk about him."
        $ samantha.love += 1
    hide samantha
    return

label samantha_talk_birthday_male:
    show samantha
    if samantha.flags.nickname == "cupcake":
        mike.say "Happy birthday Cupcake."
    else:
        mike.say "Happy birthday Samantha."
    show samantha happy
    samantha.say "Thank you [hero.name]."
    $ samantha.love += 1
    hide samantha
    return

init:
    define nickname_baby = ["Baby", "baby"]
    define nickname_smooth_rider = ["Smooth rider", "smooth rider"]
    define nickname_sweetheart = ["Sweetheart", "sweetheart"]
    define nickname_muffin = ["Muffin", "muffin"]

label command_nickname_samantha:
    menu:

        "Call me Sugar" if active_girl.flags.mikeNickname not in nickname_sugar and active_girl.love > 140 and "candies" in hero.inventory:
            $ active_girl.flags.mikeNickname = "Sugar"
        "Stop calling me Sugar" if active_girl.flags.mikeNickname in nickname_sugar:
            $ active_girl.flags.mikeNickname = None


        "Call me Baby" if active_girl.flags.mikeNickname not in nickname_baby and active_girl.love > 80 and hero.grooming < 6:
            $ active_girl.flags.mikeNickname = "Baby"
        "Stop calling me Baby" if active_girl.flags.mikeNickname in nickname_baby:
            $ active_girl.flags.mikeNickname = None


        "Call me Smooth rider" if active_girl.flags.mikeNickname not in nickname_smooth_rider and active_girl.love > 60 and active_girl.flags.kiss >= 1:
            $ active_girl.flags.mikeNickname = "Smooth rider"
        "Stop calling me Smooth rider" if active_girl.flags.mikeNickname in nickname_smooth_rider:
            $ active_girl.flags.mikeNickname = None


        "Call me Sweetheart" if active_girl.flags.mikeNickname not in nickname_sweetheart and active_girl.love > 140 and active_girl.status in ["girlfriend", "fiance"]:
            $ active_girl.flags.mikeNickname = "Sweetheart"
        "Stop calling me Sweetheart" if active_girl.flags.mikeNickname in nickname_sweetheart:
            $ active_girl.flags.mikeNickname = None


        "Call me Muffin" if active_girl.flags.mikeNickname not in nickname_muffin and active_girl.love > 40 and "pastry" in hero.inventory:
            $ active_girl.flags.mikeNickname = "Muffin"
        "Stop calling me Muffin" if active_girl.flags.mikeNickname in nickname_muffin:
            $ active_girl.flags.mikeNickname = None


        "From now on I will stop calling you Cupcake" if active_girl.id == "samantha" and samantha.flags.nickname == "cupcake":
            $ samantha.flags.nickname = None
        "From now on I will call you Cupcake" if active_girl.id == "samantha" and samantha.flags.giftslave_collar == True and samantha.flags.nickname is None:
            $ samantha.flags.nickname = "cupcake"
        "Cancel":


            jump command_girl

label submissive_interact_samantha_male:
    mike.say "Ah, Sam..."
    show samantha talkative
    samantha.say "Oh-oh - I know that tone of voice!"
    samantha.say "What do you want, [hero.name]?"
    show samantha normal
    mike.say "Ha...ah...yeah...you know me too well!"
    mike.say "I was just wondering now that we're an item..."
    mike.say "Maybe you'd say so whenever you see me?"
    mike.say "You know, like in a sexy way?"
    if samantha.sub >= 70 or samantha.is_sex_slave:
        show samantha happy
        samantha.say "Well, you have become a massive part of my life."
        samantha.say "You're a part of my daily routine now!"
        show samantha flirt
        samantha.say "So why the hell not?"
        $ samantha.flags.submissive_interact = True
    else:
        show samantha sad
        samantha.say "Ah, I don't think so, [hero.name]."
        samantha.say "I just got out of a marriage that blew up in my face."
        samantha.say "I don't want to take anything for granted right now."
        show samantha gloomy
        mike.say "You've got a point, Sam."
        mike.say "Just forget I mentioned it."
        $ samantha.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
