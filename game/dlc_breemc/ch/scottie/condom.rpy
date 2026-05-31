label scottie_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I shake my head in amazement."
        "Because Scottie's one hundred percent correct!"
        bree.say "Right there on the bedside table, Scottie."
        bree.say "You see them?"
        scottie.say "I sure do, [hero.name]..."
        scottie.say "And I'm on it!"
        "Scottie's as good as his word, leaping off the bed."
        "He grabs one of the condoms and quickly puts it on."
        "Then he climbs back onto the bed, and we're good to go."
    else:
        "But just as I'm about to get started, a thought occurs to me."
        "And it's an important one, so I stop and hold up a hand."
        bree.say "Wait a second, Scottie..."
        bree.say "We really should use some protection."
        "Scottie looks up at me in surprise."
        "But once he gets what I'm saying his confusion disappears."
        scottie.say "Oh yeah..."
        scottie.say "Good thinking, [hero.name]!"
        scottie.say "You've got one, right?"
        "I nod and hop off the bed to retrieve a condom."
        "And once I have it, I'm back in position as quickly as possible."
        "It's on just as quickly too, and we're good to go."
    return







label scottie_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I'm expecting Scottie to get right down to it."
        "So I'm caught off-guard when he pauses instead."
        scottie.say "Wait a minute, [hero.name]..."
        scottie.say "We should use some protection!"
    else:
        "Just as we're about to get started, Scottie starts waving his hands."
        "And I stop so that I can find out what's bothering him."
        bree.say "What's up, Scottie?"
        scottie.say "Erm..."
        scottie.say "We should really use a condom, [hero.name]."
        scottie.say "So we don't have an accident, you know?"
    return

label scottie_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        scottie.say "No worries, [hero.name]..."
        scottie.say "I got this!"
        "Scottie's as good as his word, leaping off the bed."
        "He grabs a condom from his pants pocket and quickly puts it on."
        "Then he climbs back onto the bed, and we're good to go."
    else:
        scottie.say "But don't worry, babe..."
        scottie.say "I always carry one on me."
        scottie.say "Because you never know!"
        "I nod and hop off the bed to retrieve a condom."
        "And once I have it, I'm back in position as quickly as possible."
        "It's on just as quickly too, and we're good to go."
    return

label scottie_mad_condom:
    $ result = randint(1, 2)
    if result == 1:
        bree.say "Scottie..."
        bree.say "You can't be serious?!?"
        bree.say "Just forget about it and fuck me already!"
        "I look back over my shoulder."
        "And I'm shocked to see Scottie climbing off the bed."
        "I turn to follow him, wondering what the hell's going on."
        bree.say "Where are you going?"
        scottie.say "Urgh..."
        scottie.say "I never thought you were that irresponsible, [hero.name]!"
        scottie.say "And it's like, a total turn-off."
        scottie.say "Call me when you mature a little, okay?"
        "I watch in stunned silence as Scottie gets dressed."
        "And the he walks out, leaving me alone and unfulfilled."
        "But what makes it even worse is that he called me irresponsible!"
    else:
        bree.say "Are you serious?"
        bree.say "I thought a guy like you would be more adventurous!"
        bree.say "Don't you want to live dangerously?"
        "Scottie shakes his head as he pushes me off of him."
        "And he's still shaking it as he starts to put on his clothes too."
        scottie.say "Not cool, [hero.name]."
        scottie.say "Seriously not cool."
        scottie.say "I thought you were supposed to be the smart one."
        "All I can do is watch as Scottie gets dressed and lets himself out."
        "And I don't know what hurts more."
        "The fact that I'm going to miss out on the sex."
        "Or the fact a guy as dumb as Scottie just questioned my intelligence."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
