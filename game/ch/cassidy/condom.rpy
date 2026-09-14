label cassidy_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "And of course, that means making sure we use protection!"
        "So I reach for one of the condoms on the bedside table."
        cassidy.say "Hey!"
        cassidy.say "What are you waiting for?!?"
        "Cassidy looks back over her shoulder to see what's holding me up."
        "But when she sees the condom in my hand, she nods eagerly."
        "I hurry to get the thing on, and then we're ready to go."
    elif result == 2:
        "But I resist it's siren call for a moment longer."
        "Which makes Cassidy look over her shoulder to see what's up."
        cassidy.say "What are you..."
        "I hold up the condom that I have in my hand."
        "And it's all the answer Cassidy needs."
        cassidy.say "Oh, I see..."
        cassidy.say "Well, get it on already!"
        "I do as I'm told."
        "And just like that, we're ready to go."
    elif result == 3:
        mike.say "Me too, Cassidy."
        mike.say "But first we need to take precautions."
        cassidy.say "Huh?"
        mike.say "I mean we need to use a condom!"
        cassidy.say "Oh, okay!"
        "Cassidy waits patiently while I grab a condom."
        "Then I slip it on and we're ready to go."
    else:
        "But then I have a sudden flash of memory."
        "And I hold up a hand to stop Cassidy in her tracks."
        "She looks at me hard, not amused at my taking back control."
        cassidy.say "Hey!"
        cassidy.say "What are you doing?!?"
        mike.say "We should use some protection, Cassidy."
        mike.say "After all, we don't want to have any accidents, do we?"
        "I see recognition spread across Cassidy's face."
        "And I know that she feels suitably chastened by my words."
        "Because she just nods quickly, letting me grab a condom."
        "Then she waits patiently as I put it on."
        "As soon as that's done, we're ready to go."
    return

label cassidy_sub_use_condom:
    menu:
        "Use a condom" if hero.has_condom():
            $ CONDOM = hero.use_condom()
        "Ignore her":
            mike.say "No, bitch. You're going to take my cock raw and you're going to like it!"
            return 'sad'
        "Fuck her ass instead":
            return 'anal'
        "I don't have to fuck her" if not hero.has_condom():
            mike.say "I don't have any condoms with me. I'll let it go this time, but only this time. If you don't want my baby you'd better go on the pill."
            cassidy.say "Oh yes, Master, thank you Master. I'll go get the pill tomorrow!"
            $ cassidy.flags.pill = True
            $ cassidy.love += 3
            $ cassidy.sub += 3
            return False
    return True
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
