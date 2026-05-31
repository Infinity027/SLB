label kiara_use_condom:
    $ result = randint(1, 2)
    if result == 1:
        "But then I remember that there's something else I need to take care of first."
        "And so I quickly make to roll out from under Kiara and retrieve it from my bedside table."
        "Though I only manage to wriggle once before she pins me down with all of her weight."
        if kiara.sub >= 25:
            kiara.say "Wait..."
            kiara.say "What are you doing?"
        elif kiara.sub < -25:
            kiara.say "Oh no, no, no..."
            kiara.say "I did not give you permission to go anywhere!"
        else:
            kiara.say "[hero.name]…"
            kiara.say "What could be more important than this?"
        "I smile and shake, my head, trying to assure her there's nothing wrong."
        mike.say "Whoa..."
        mike.say "Calm down, Kiara - I just want to get a condom!"
        "I gesture the bedside table to make my point."
        "And that seems to be more than enough to reassure her."
        "Because her mood seems to improve and she nods her head eagerly, letting me up."
        "Hell, she even helps me to open the packet and get the thing on."
        "And with that done, we're back in business."
    else:
        "I'm all ready to go, fixated on my target and not about to let anything get in my way."
        "But then I stop in my tracks, as I suddenly remember something important that I've forgotten."
        "Kiara seems to notice this instant change in mood, and waves to get my attention."
        kiara.say "What is it, [hero.name]?"
        kiara.say "Is there something wrong?"
        "I shake my head as I make to get up, trying to reassure Kiara everything's fine."
        mike.say "Nothing to worry about, Kiara..."
        mike.say "I just need to take care of something."
        mike.say "Won't take a minute, I promise."
        "Kiara looks like she's about to say more, but I'm already up and off."
        "But true to my word, it only takes me a moment to find what I'm looking for."
        mike.say "Ta da!"
        kiara.say "A condom?"
        kiara.say "Oh yes, that is a good idea."
        "Kiara nods as I hurry back to her and hand it over."
        "She tears open the packet and helps me to get it on."
        "Then we're all set, back in position and ready to go."
    return

label kiara_intro_condom:
    "I'm all ready to go, feeling like I want nothing more than to get it on with Kiara."
    "And it looks like she's feeling the same way too, hanging onto me as if her life depended on it."
    "But just as I'm getting ready to pull the trigger, the expression on her face changes."
    "At the same time she holds up a hand to stop me."
    kiara.say "No, [hero.name] - you have to wait!"
    return

label kiara_warn_condom:
    $ result = randint(1, 2)
    if result == 1:
        "I'm all ready to go for it, but then Kiara holds up a hand to stop me."
        if kiara.sub >= 25:
            kiara.say "Please, [hero.name]…"
            kiara.say "There is something that we have forgotten."
        elif kiara.sub < -25:
            kiara.say "Stop right there, [hero.name]…"
            kiara.say "No sex until we handle something first!"
        else:
            kiara.say "Wait a moment, [hero.name]…"
            kiara.say "There is something we should do first."
        "I blink in surprise and shake my head."
        mike.say "Huh?"
        mike.say "What is it, Kiara?"
        mike.say "What's the problem?"
        kiara.say "Protection..."
        kiara.say "We need to use protection."
    else:
        "Feeling more than a little exasperated by the delay, I demand to know the reason for the hold-up."
        mike.say "What's the matter, Kiara?"
        mike.say "I thought that we were ready to get it on?"
        "Kiara nods, as if she's trying to reassure me, but still holds me at bay."
        kiara.say "And we will, we will - but not until we use protection."
        kiara.say "We cannot do it without a condom!"
    return

label kiara_force_condom:
    $ result = randint(1, 2)
    if result == 1:
        if kiara.sub >= 25:
            kiara.say "But it is okay, I have brought some."
        elif kiara.sub < -25:
            kiara.say "So you can go and fetch it now."
        else:
            kiara.say "Which is why I remembered to bring some."
        "Kiara points to the pile of clothes she shed just a few minutes ago."
        "And I don't hesitate to hop off the bed as soon as she lets me up so I can hurry over to them."
        "It only takes me a few moments to locate the condom."
        "And once I have it, I hurry back to the bed."
        "Kiara nods eagerly all the time I'm fetching the condom."
        "Hell, she even helps me to open the packet and get the thing on."
        "And with that done, we're back in business."
    else:
        kiara.say "But do not worry, because I have one right here."
        "Before I can say another word, Kiara leaps up and hurries over to her stuff."
        "She rummages through it until she finds what she's looking for."
        "I nod eagerly as Kiara hurries back over with the condom."
        "She tears open the packet and helps me to get it on."
        "Then we're all set, back in position and ready to go."
    return

label kiara_mad_condom:
    $ result = randint(1, 2)
    if result == 1:
        mike.say "Are you serious?"
        mike.say "Just forget about the damn condom, okay?"
        "Kiara's expression suddenly becomes one of astonishment."
        "And then just as quickly it turns into one of annoyance."
        "So much so that she doesn't need to say a word to make me back off."
        "The moment that I'm far enough away, Kiara hops off the bed."
        "And I'm forced to watch in dismay as she starts to put on her clothes."
        mike.say "Kiara..."
        mike.say "Where are you going?"
        if kiara.sub >= 25:
            kiara.say "You know that I would do anything you ask, [hero.name]."
            kiara.say "Anything but let you forget about the condom!"
        elif kiara.sub < -25:
            kiara.say "If you don't wear the condom, you don't get me."
            kiara.say "Maybe this way you will learn your lesson."
        else:
            kiara.say "No condom, no Kiara..."
            kiara.say "It is as simple as that."
        "By the time Kiara's finished lecturing me, she's already dressed."
        "And she doesn't give me a chance to respond either."
        "Because she just storms straight out before I can say another word."
    else:
        mike.say "Oh come on, Kiara!"
        mike.say "You can't be serious about this?"
        mike.say "Let's just forget about the condom this one time, yeah?"
        mike.say "We can use one the next time, I promise."
        "Kiara looks at me like I just suggested we abduct and murder someone."
        "And she doesn't hesitate to push me away as she gets up a moment later."
        kiara.say "I cannot believe that you would even suggest such a thing, [hero.name]."
        kiara.say "But if that is really how you feel, then we can go no further."
        mike.say "Kiara, please - just come back?"
        mike.say "Can't we talk about this?"
        "But no matter what I say, it doesn't seem to have any effect on Kiara."
        "Instead she keeps right on grabbing her clothes and pulling them on."
        "And as soon as she's wearing enough to be considered halfway decent, she heads out of the door."
        "Which leaves me alone, frustrated and unfulfilled in the extreme."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
