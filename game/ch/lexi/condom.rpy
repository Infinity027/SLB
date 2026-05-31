label lexi_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        "My cock's more than ready to go right now."
        "But I need to take a moment, just to be safe."
        "I grab a condom from the bedside table, and slip it on."
        if lexi.flags.drugs:
            "Lexi's glazed eyes hardly seem to register the momentary delay anyway."
        else:
            "Lexi seems impatient for me to get started, but doesn't complain at the delay."
    elif result == 2 and game.room == "bedroom1":
        lexi.say "Mmm..."
        lexi.say "I want this in me so bad!"
        mike.say "Yeah, but wait a minute..."
        mike.say "We should use a condom!"
        "Lexi nods in agreement."
        "But I know that I've got to do this quickly."
        "Luckily for me I have a stash in a nearby drawer."
        "And I can grab one really fast."
        "As soon as it's on, we're ready to go."
    elif result == 3 and game.room == "bedroom1":
        mike.say "Hold on a minute, Lexi."
        lexi.say "Huh..."
        lexi.say "What's the hold-up?!?"
        "I reach over to the bedside table and snatch up a condom."
        "As soon as she sees it in my hand, Lexi nods and lets me get on with it."
        "A second or two later, it's on and we're ready to go for real."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Lexi in her tracks."
        mike.say "Wait a minute, Lexi."
        mike.say "We should use some protection."
        "Lexi looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return







label lexi_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        lexi.say "Whoa, hold on a minute there!"
        "I stop in my tracks, looking down at Lexi in surprise."
    elif result == 2:
        lexi.say "Wait a minute, [hero.name]."
    elif result == 3:
        lexi.say "Oh, wait..."
        lexi.say "We should use a condom!"
    else:
        lexi.say "Not so fast, cowboy!"
        lexi.say "Aren't you going to put something on that thing first?"
    return

label lexi_force_condom:
    $ result = randint(1, 3)
    if result == 1:
        "She nods towards the bedside table, to the pile of condoms atop it."
        lexi.say "Aren't you going to put one of those on first?"
        "I nod in agreement, quickly grabbing one and doing as she asks."
        "No sense in taking risks, even when we're both so up for it."
    elif result == 2:
        lexi.say "Don't worry..."
        lexi.say "I got one!"
        "Lexi hops off the table and grabs her condom."
        "Then she hurries back to her former position."
        "As soon as it's on, we're ready to go."
    else:
        lexi.say "No protection means no pussy!"
        "Lexi reaches out and snatches up a condom."
        "As soon as she sees it in her hand, I nod and take it from her."
        "A second or two later, it's on and we're ready to go for real."
    return

label lexi_mad_condom:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Huh...what?"
        mike.say "When did you become such a saint, Lexi?"
        "Lexi snorts at this, pulling her pussy away from my bobbing cock."
        lexi.say "Saint or not - you're not putting that thing in me without a rubber!"
        "And with that, she rolls out from under me and off the bed."
    elif result == 2:
        mike.say "You can't be serious, Lexi!"
        mike.say "Two seconds ago you were begging me to fuck you."
        mike.say "Let's just do it already!"
        "Lexi makes a scoffing sound."
        "And then she shoves me on the shoulder."
        "The blow pushes me back and allows her to jump off the table."
        lexi.say "I might like to fuck, [hero.name]..."
        lexi.say "But that doesn't mean I'm stupid."
        lexi.say "You, on the other hand..."
        "I watch helplessly as she gets dressed and walks out on me."
        "And all because I wouldn't use a damn condom!"
    else:
        lexi.say "No protection means no pussy!"
        mike.say "Lexi, you have to be joking!"
        lexi.say "No way, I'm deadly serious."
        mike.say "I'd have thought you of all people..."
        lexi.say "What - that I'm a slut you can cum in whenever you like?!?"
        lexi.say "FUCK YOU!"
        "With that, Lexi shoves me off of her and clambers off the bed."
        "She grabs her clothes and storms out, leaving me alone with a raging erection."
    return

label lexi_drugs_condom:
    "Lexi's eyes are glazed over by now, meaning she's hardly aware of what's going on."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
