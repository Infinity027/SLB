label kleio_use_condom:
    $ result = randint(1, 3)
    if result == 1 and game.room == "bedroom1":
        "I pause for a moment to grab a condom from the bedside table."
        "Kleio makes a pouting noise at the interruption, but then begins to purr in approval at the sight of me slipping it on."
    elif result == 2 and game.room == "bedroom1":
        "But I stop before it can slip inside of her."
        kleio.say "Wha..."
        kleio.say "What are you doing?"
        "I grab a condom from the bedside table as way of explanation."
        "And Kleio nods eagerly, urging me on as I rip open the packet and put it on."
    else:
        "But that doesn't mean I'm going to take any unnecessary risks."
        mike.say "Hold on a moment, Kleio."
        mike.say "We really should use a condom."
        kleio.say "Huh...wha..."
        kleio.say "Oh, yeah...you're right!"
        "Kleio waits patiently while I retrieve a condom from my pocket."
        "Putting it on only takes a couple of seconds."
        "And then we're good to go!"
    return

label kleio_pill_condom:
    kleio.say "Quit stalling - there is no risk, I'm on the pill!"
    return

label kleio_no_condom:
    if randint(1, 2) == 1:
        kleio.say "Quit stalling - I'll let you put it inside of me like that!"
    else:
        "For a moment I think Kleio's going to argue with me."
        "But then she nods and begins to urge me on."
        kleio.say "Sure, Loverboy, sure!"
        kleio.say "I was just overthinking it!"
    return
