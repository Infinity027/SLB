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

label kleio_intro_condom:
    $ result = randint(1, 3)
    if result == 1:
        "Kleio's so close to me now that I can't think of anything but having her without delay."
    elif result == 2:
        mike.say "Ah, forget about it, Kleio."
        mike.say "That'll kill the whole thing."
        mike.say "Let's live dangerously!"
    else:
        "There's just no way that Kleio can tease me like that and not get what she wants."
        "Because the moment that she starts, it's what I want more than anything in the world too!"
        "And so I pull her down suddenly, feeling the entire length of my cock slide along her lips."
        "Kleio's eyes go wide at the sensation, and she gasps in delighted surprise."
    return

label kleio_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        kleio.say "Put something on that thing, before it goes anywhere near the business entrance!"
    elif result == 2:
        kleio.say "Better put a rubber on it, man - otherwise it's game over!"
    elif result == 3:
        kleio.say "Oh shit..."
        kleio.say "Wait a minute!"
        kleio.say "We should use a condom!"
        mike.say "Huh?"
    else:
        "Kleio stops me before it can slip inside of her."
        mike.say "Huh?"
        mike.say "What are you doing?"
    return

label kleio_force_condom:





    kleio.say "Wait a minute..."
    kleio.say "I got one right here somewhere..."
    "I wait patiently while Kleio retrieves the condom."
    "Putting it on only takes a couple of seconds."
    "And then we're good to go!"
    return

label kleio_pregnant_condom:
    kleio.say "Quit stalling - there is no risk, I can't be double knocked up!"
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

label kleio_mad_condom:
    $ result = randint(1, 3)
    if result == 1:
        "I fumble for a condom from the bedside table, but there's none to be found."
        mike.say "Shit...I ran out!"
        "Kleio gives me a rueful smile as she shakes her head and shrugs whilst climbing off of the bed."
        kleio.say "Sorry, Loverboy - looks like that's all you're getting from me tonight!"
    elif result == 2:
        kleio.say "Yeah, no thanks, Loverboy!"
        kleio.say "When I drive, I wear a seat-belt."
        kleio.say "And when I fuck, he wears a rubber!"
        "Kleio gives me a sharp shove, pushing me off her."
        "Then she slips under my arm and begins to get dressed."
        "Looks like I really blew it this time!"
    else:
        kleio.say "We need a condom, dummy!"
        mike.say "Ah, Kleio!"
        mike.say "Can't we just forget about it this one time?"
        "Kleio looks at me in disgust, shaking her head."
        kleio.say "No we fucking can't!"
        kleio.say "No condom, no cock!"
        "She climbs off of me and starts to get dressed."
        "And nothing I can say or do seems to change her mind."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
