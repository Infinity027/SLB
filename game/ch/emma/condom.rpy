label emma_use_condom:
    $ result = randint(1, 2)
    if result == 1 and game.room == "bedroom1":
        mike.say "Hold on, Emma."
        mike.say "We should play it safe."
        "Emma looks over her shoulder."
        "And there's confusion on her face."
        "So I point at the condoms on the bedside table."
        emma.say "Oh, I get it!"
        "Emma waits patiently as I put one on."
        "Then she nods in satisfaction."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Emma in her tracks."
        mike.say "Wait a minute, Emma."
        mike.say "We should use some protection."
        "Emma looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return
