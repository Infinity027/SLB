label alexis_use_condom:
    $ result = randint(1, 2)
    if result == 1 and game.room == "bedroom1":
        "But first I just need to take a little time out to be sensible."
        "And so I reach over and grab a condom from the bedside table."
        "Alexis waits patiently for me to open the packet and slip it on."
        "Her face showing no signs of impatience as she does so."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Alexis in her tracks."
        mike.say "Wait a minute, Alexis."
        mike.say "We should use some protection."
        "Alexis looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return