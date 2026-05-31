label samantha_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "But eager as we both are, that's no excuse to take risks."
        if samantha.flags.nickname == "cupcake":
            mike.say "On the table by the bed, Cupcake..."
        else:
            mike.say "On the table by the bed, Sam..."
        samantha.say "Huh?"
        mike.say "The condoms, they're on the bedside table!"
        samantha.say "Oh yeah - good thinking!"
        "Sam leans over and grabs a condom."
        "Then she opens the packet and slides it onto my cock."
        "That done, we're ready to go."
    elif result == 2:
        "Suddenly I stop in my tracks, slapping my forehead."
        samantha.say "What's the matter, [hero.name]?"
        samantha.say "You get a cramp or something?"
        if samantha.flags.nickname == "cupcake":
            mike.say "No, Cupcake..."
        else:
            mike.say "No, Sam..."
        mike.say "I just remembered we need to use a condom."
        samantha.say "Oh yeah."
        samantha.say "Good thinking!"
        "It only takes me a couple of seconds to grab a condom."
        "And as soon as it's on, we're good to go."
    elif result == 3:
        mike.say "Uh..."
        mike.say "We should..."
        mike.say "We should use a condom!"
        "Sam stops in her tracks, like she'd totally forgotten."
        "And then she nods in agreement."
        samantha.say "Sure, sure - let's get one on there."
        samantha.say "I never had that problem when this was all just in my head!"
        "Sam waits patiently while I grab a condom and tear open the packet."
        "Then she helps me to roll it down over my cock."
        "That done, we're ready to go!"
    else:
        "But first I need to make sure that we take the appropriate precautions."
        "So I hold up a hand as I climb off the bed, heading for the bedside table."
        mike.say "Just a second, Sam..."
        mike.say "I need to grab something."
        "Sam looks up with genuine surprise written all over her face."
        "And who can blame her, as I'm sure no guy ever lost interest in her at this point before."
        if samantha.sub >= 50:
            samantha.say "Where are you going, [hero.name]?"
            samantha.say "Did I do something wrong?"
        else:
            samantha.say "What are you doing?"
            samantha.say "Is something wrong?"
        "By the time Sam's said all of this, I've found what I was looking for."
        "And when I hold up the condom, I see her expression turn into one of relief."
        "She nods eagerly as I return, already tearing open the packet."
        "Then she helps me to get it on, and we're good to go."
    return







label samantha_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        samantha.say "Wait a minute..."
        samantha.say "We need to use a condom!"
    elif result == 2:
        samantha.say "Oh, wait..."
        samantha.say "We should really use a condom!"
    elif result == 3:
        "But then she pauses, as if she's remembered something."
        samantha.say "Whoops!"
        samantha.say "We should use a condom, [hero.name]!"
    else:
        "But before I can go any further, Sam holds up a hand to stop me."
        mike.say "Huh..."
        mike.say "What's up, Sam?"
        if samantha.sub >= 50:
            samantha.say "I'm sorry, [hero.name]..."
            samantha.say "But could we use a condom?"
        else:
            samantha.say "We need a condom, [hero.name]..."
    return

label samantha_force_condom:
    $ result = randint(1, 4)
    if result == 1:
        samantha.say "Don't worry about it."
        samantha.say "I got one!"
        "Sam hops off me and then off the bed."
        "She rummages around in her clothes for a moment."
        "Then she returns holding a condom."
        "Sam climbs back on as she opens the packet."
        "The she slides it onto my cock and we're ready to go."
    elif result == 2:
        samantha.say "It's okay..."
        samantha.say "I have one in my purse!"
        "It only takes me a couple of seconds to grab a condom."
        "And as soon as it's on, we're good to go."
    elif result == 3:
        samantha.say "Don't worry, [hero.name]."
        samantha.say "I've gone through this a thousand times in my head."
        samantha.say "And I planned for all eventualities!"
        "Sam holds up a condom, which she hands over to me."
        "She waits patiently while I grab a condom and tear open the packet."
        "Then Sam helps me to roll it down over my cock."
        "That done, we're ready to go!"
    else:
        "Sam points at the pile of clothes she shed at the side of the bed."
        samantha.say "There's one in my pocket, right there."
        "I can't believe that I forgot to grab one myself."
        "So I make a point of nodding and doing as Sam asks."
        "And it doesn't take me long to find the condom in her pockets."
        "She nods eagerly as I return, already tearing open the packet."
        "Then she helps me to get it on, and we're good to go."
    return

label samantha_mad_condom:
    $ result = randint(1, 4)
    if result == 1:
        if samantha.flags.nickname == "cupcake":
            mike.say "Are you serious, Cupcake?"
        else:
            mike.say "Are you serious, Sam?"
        mike.say "One minute you're begging for it..."
        mike.say "And the next you're asking me to use a condom?"
        samantha.say "Yeah, [hero.name]."
        samantha.say "That's exactly what I'm doing!"
        samantha.say "Are you saying you won't wear one?"
        mike.say "No, I won't - let's just get on with it!"
        "Sam shakes her head as she hops off me and then off the bed."
        "She starts gathering up her clothes and getting dressed."
        samantha.say "If that's your attitude, I'll get off some other way!"
        mike.say "What?"
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, come back!"
        else:
            mike.say "Sam, come back!"
        "But it's no good."
        "Sam just ignores me as she dresses herself."
        "Then she walks out, slamming the door behind her."
    elif result == 2:
        if samantha.flags.nickname == "cupcake":
            mike.say "What are you talking about, Cupcake?"
        else:
            mike.say "What are you talking about, Sam?"
        mike.say "One minute you're begging me to fuck you."
        mike.say "The next you're telling me to stop!"
        samantha.say "Why are you being like that, [hero.name]?"
        samantha.say "All I'm asking is for you to use a condom."
        samantha.say "Geez...you can be such a jerk sometimes!"
        "Sam rolls off the bed and starts to get dressed."
        mike.say "Aw..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Come on, Cupcake!"
        else:
            mike.say "Come on, Sam!"
        samantha.say "Forget it, [hero.name]."
        samantha.say "You really killed the mood for me."
        "Once she's dressed, Sam storms out of the room."
        "Which lets me know she's not bluffing."
    elif result == 3:
        "I can't believe that she's stopped us for something so dumb!"
        "And the frustration that I'm feeling comes bursting out of me."
        if samantha.flags.nickname == "cupcake":
            mike.say "You've got to be kidding, Cupcake!"
        else:
            mike.say "You've got to be kidding, Sam!"
        mike.say "Just forget about the condom already!"
        "Sam's mouth drops open in horror."
        "And she drops my cock at the same time too."
        samantha.say "You know what, [hero.name]..."
        samantha.say "Sometimes your fantasies don't translate to real life!"
        "With that, she climbs off the bed and starts to get dressed."
        samantha.say "Sam...what are you..."
        mike.say "Oh come on!"
        "But no matter what I say or how much I plead, it does no good."
        "Soon enough, Sam's dressed and walking out the door."
        "Leaving me alone with a drooping cock and aching balls."
    else:
        mike.say "Ah, just forget about it, Sam..."
        mike.say "We can do it bare-back just this once."
        "The moment the words are out of my mouth, I realise that I just fucked up badly."
        "Because Sam stares at me in amazement as she starts to roll out from under me."
        "And before I can do a thing about it, she's off the bed and gathering up her clothes."
        mike.say "Sam, wait..."
        mike.say "I...I think you're overreacting!"
        "Rather than having the effect I wanted, this only seems to make things worse."
        "As Sam glares at me as she hastily pulls on her clothes."
        if samantha.sub >= 50:
            samantha.say "I love you, [hero.name]..."
            samantha.say "But that doesn't mean you can treat me like this!"
        else:
            samantha.say "Are you serious?!?"
            samantha.say "I thought you had more respect for me than that!"
        "I open my mouth to argue, but Sam instantly turns her back on me and makes for the door."
        "And then she storms out, still only half dressed."
        "Leaving me alone and totally frustrated with myself."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
