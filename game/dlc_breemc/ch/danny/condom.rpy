label danny_use_condom:
    $ renpy.dynamic(result=randint(0, 1))
    if result == 0:
        "Even as Danny's saying all of that, I'm remembering something."
        "Something that makes me wave a hand in the air and pull out of his grip."
        danny.say "Huh..."
        danny.say "Where'd you think you're going?"
        bree.say "I just want to grab a condom, Danny..."
        bree.say "It'll only take a minute, I promise."
        "Danny's attitude changes as soon as I mention using protection."
        "And he nods, allowing me to quickly grab a condom."
        "All it takes is a few seconds to get it out and on."
        "Then I'm back in position again."
    else:
        "But it's then that I realise I forgot something important."
        bree.say "WAIT!"
        danny.say "Huh?"
        danny.say "What the hell?!?"
        "Danny's instinctively taken his hands off me and backed up a little."
        "So I use the chance to leap to my feet and go looking for a certain something."
        bree.say "Condoms, Danny..."
        bree.say "We need a condom, yeah?"
        "As soon as I find one, I hold it up."
        "Which gets a nod from Danny."
        danny.say "Oh..."
        danny.say "Good call!"
        "I hand it over and Danny gets on with the task of putting the thing on."
        "And within seconds we're ready to go again."
    return







label danny_warn_condom:
    $ renpy.dynamic(result=randint(0, 1))
    if result == 0:
        "I'm expecting Danny to get things started right away."
        "So it comes as a big surprise when he stops and lets me go."
        bree.say "Hey..."
        bree.say "What are you doing?"
        danny.say "I just remembered we need to use protection."
    else:
        "Which makes what he does next all the more inexplicable."
        danny.say "Wait, [hero.name]..."
        danny.say "We forgot to use a condom!"
    return

label danny_force_condom:
    $ renpy.dynamic(result=randint(0, 1))
    if result == 0:
        "I watch in amazement as Danny retrieves a condom from his pants."
        "All it takes is a few seconds to get it out and on."
        "Then Danny's back in position again."
        "But I'm still amazed he's so safety conscious."
        "Especially for a supposedly legit bad boy!"
    else:
        danny.say "Don't worry..."
        danny.say "I got one right here."
        "Danny hurries off to grab the condom."
        "Then he returns already tearing open the packet."
        "And within seconds we're ready to go again."
    return

label danny_mad_condom:
    $ renpy.dynamic(result=randint(0, 1))
    if result == 0:
        "I shake my head in amazement."
        "Isn't he supposed to be the bad boy here?"
        if hero.morality >= 25:
            bree.say "Oh, Danny..."
            bree.say "And I thought you were so rugged!"
        elif hero.morality <= -25:
            bree.say "There's not time for that..."
            bree.say "Get over here and fuck me - right now!"
        else:
            bree.say "Are you serious, Danny?"
            bree.say "I thought we were living dangerously here?"
        "Danny shakes his head and starts to pull on his pants."
        danny.say "I might be a bad guy, [hero.name]..."
        danny.say "But I'm not stupid!"
        danny.say "How about you give me a call when you've grown up some, yeah?"
        "With that, Danny scoops up the rest of his clothes and walks out."
        "Leaving me alone and feeling more then a little frustrated."
    else:
        bree.say "Are you kidding me?"
        bree.say "I thought you were a bad boy?!?"
        danny.say "I am, [hero.name]..."
        danny.say "But I'm not a stupid one!"
        "I can't believe what I'm hearing."
        bree.say "Oh, come on!"
        bree.say "Forget about the condom already."
        "Danny shakes his head as he starts to get to his feet."
        danny.say "Really, [hero.name]?"
        danny.say "I thought you were smarter than that."
        "I watch as Danny starts to get dressed."
        bree.say "What are you doing?"
        bree.say "Come back here, right now..."
        bree.say "You've got a job to do, mister!"
        "But it's no good."
        "Danny just ignores my protests."
        "And once he's dressed, he walks out of the room."
        "Leaving me alone, unfulfilled and utterly frustrated."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
