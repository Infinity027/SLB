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







label emma_warn_condom:


    "Emma waves her hands in the air to get my attention."
    emma.say "Stop...wait a second!"
    emma.say "We need to use a condom."
    return

label emma_force_condom:



    emma.say "Don't worry, I've got one!"
    "Emma produces a condom and hands it over."
    "Then she waits patiently as I put it on."
    "That done, we're ready to go."
    return

label emma_mad_condom:



    mike.say "We don't HAVE to, Emma."
    mike.say "We could just forget about it this once."
    "Emma looks suddenly offended."
    "She shakes her head disapprovingly."
    emma.say "I can't believe you'd say that!"
    emma.say "That's so irresponsible!"
    "Emma climbs off of me and then off the bed too."
    "She snatches up her clothes and begins to get dressed."
    "All I can do is watch her as my cock shrinks."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
