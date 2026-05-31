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

label alexis_intro_condom:
    "I'm all set to go right ahead and make myself known to Alexis."
    return

label alexis_warn_condom:
    "But then I hear the sound of her coughing, and stop dead in my tracks."
    alexis.say "Erm...aren't we forgetting something?"
    return

label alexis_force_condom:
    "With one eyebrow raised, Alexis holds up a condom."
    alexis.say "At least one of us is thinking ahead!"
    "I reach out and grab a condom from the her."
    "Alexis waits patiently for me to open the packet and slip it on."
    "Her face showing no signs of impatience, only approval, as she does so."
    return

label alexis_mad_condom:
    "I look at her blankly, and then shake my head in confusion."
    "This doesn't go down well, as she frowns and begins to crawl out from under me."
    mike.say "Alexis?"
    mike.say "Alexis...what's the problem?!?"
    alexis.say "I'm not some dumb, over-sexed teenager, [hero.name]."
    alexis.say "If you're not gonna use a condom, then you're not coming any closer!"
    "And with that, she gathers up her clothes and storms out of the room."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
