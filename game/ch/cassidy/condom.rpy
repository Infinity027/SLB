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







label cassidy_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        "Cassidy looks back over her shoulder at me."
        cassidy.say "Aren't we forgetting something?"
        cassidy.say "You were going to use protection, right?"
    elif result == 2:
        "Cassidy looks back over her shoulder at me."
        "And I can see that she's expecting me to do something."
        cassidy.say "Erm, hello?"
        cassidy.say "What about some protection?"
    elif result == 3:
        cassidy.say "Oh wait..."
        cassidy.say "Shouldn't we use a condom?"
    else:
        "Suddenly, Cassidy holds up a hand."
        "And she stops stroking my cock against her pussy too."
        mike.say "Hey, Cassidy!"
        mike.say "What's up?!?"
        cassidy.say "I just remembered, [hero.name]."
        cassidy.say "We should use some protection!"
    return

label cassidy_force_condom:
    $ result = randint(1, 4)
    if result == 1:
        mike.say "Now that you mention it, Cassidy..."
        mike.say "I guess we should!"
        "Cassidy rolls her eyes at me."
        "And then she reaches off the bed to where her clothes are piled on the floor."
        cassidy.say "Good thing one of us thought ahead!"
        "She hands me a condom, and I hurry to put it on."
        "And just like that, we're ready to go."
    elif result == 2:
        "Before I can make myself look like an unprepared goof, Cassidy comes to the rescue."
        "She lean off the bed and reaches down to where she left her clothes in a pile on the floor."
        "Then she pops back up with a condom in her hand, which she passes to me."
        "I hurry to get the thing on, and then we're ready to go."
    elif result == 3:
        cassidy.say "Don't worry, [hero.name]."
        cassidy.say "I've got one right here!"
        "Cassidy hops off me and goes to grab the condom."
        "As soon as she has it, I lie back and let her slip it on."
        "Once that's done, we're good to go."
    else:
        "Before I can say another word, Cassidy produces a condom."
        "I have no idea where it came from, and I'm not about to ask."
        "I just take it from her and proceed to put it on."
        "Cassidy waits patiently as I put it on."
        "As soon as that's done, we're ready to go."
    return

label cassidy_mad_condom:
    $ result = randint(1, 4)
    if result == 1:
        mike.say "Erm..."
        mike.say "Funny thing, Cassidy..."
        mike.say "I kind of wasn't!"
        "Cassidy looks at me in horror."
        "And then she hops off the bed."
        cassidy.say "If that's what you think of me, [hero.name]..."
        if game.hour >= 20:
            cassidy.say "Then you can forget about sex tonight!"
        else:
            cassidy.say "Then you can forget about sex today!"
        "With that, she pulls on her clothes and storms out of the room."
    elif result == 2:
        mike.say "Aw, come on, Cassidy!"
        mike.say "I thought you were dying to get down to it?!?"
        mike.say "I can just pull out before I cum!"
        "Cassidy rolls her eyes and shakes her head."
        "And she climbs straight off me without saying a word."
        "I roll over and watch as she begins to pull on her clothes."
        mike.say "Y...you're leaving?"
        cassidy.say "Well-spotted, [hero.name]."
        cassidy.say "What gave it away?"
        "All I can do is lay there as she finishes dressing and storms out."
        "My cock drooping with disappointment the whole time."
    elif result == 3:
        mike.say "Are you serious, Cassidy?"
        mike.say "I thought we were being naughty here?"
        mike.say "You know, spontaneous!"
        cassidy.say "Urgh..."
        cassidy.say "That's not naughty, [hero.name]."
        cassidy.say "That's just dumb!"
        "Cassidy sighs as she climbs off me and starts to get dressed."
        cassidy.say "And thanks for killing the mood, asshole!"
        "I keep on protesting and pleading."
        "But it doesn't do me any good."
        "As soon as she's dressed, Cassidy storms out."
        "And I'm left alone in my office, just like before."
    else:
        mike.say "Huh?!?"
        mike.say "Can't we just forget it this once, Cassidy?"
        mike.say "Stopping now's really going to kill the mood!"
        "Cassidy looks at me in sheer disgust."
        "And then she climbs off of me and the bed."
        cassidy.say "No, I think you just did that yourself, [hero.name]!"
        cassidy.say "And I think I'll be going home now too."
        "Nothing I can say changes Cassidy's mind."
        "And pretty soon she's dressed."
        "Then she storms out of the door, leaving me alone."
    return

label cassidy_sub_warn_condom:
    "Cassidy's eyes get big when she realizes what I'm doing."
    cassidy.say "No! I can't get pregnant! Please don't do this to me! I'm begging you!"
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
