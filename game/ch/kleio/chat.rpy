label kleio_desire_0_male:

    if kleio.love < 30:
        kleio.say "What do you want dumbass?"
    else:
        kleio.say "What's up [hero.name]?"

    return

label kleio_desire_1_male:

    if kleio.love < 60:
        kleio.say "You think because you're not half bad looking you deserve something special?"
    else:
        kleio.say "You know, I think you're not half bad looking..."

    return

label kleio_desire_2_male:

    if kleio.love < 90:
        kleio.say "Don't go thinking I'll fall for you just because you know how to smile."
    else:
        kleio.say "Stop smiling like that, it's embarrassing."
    $ kleio.love += 1

    return

label kleio_desire_3_male:

    if kleio.love < 120:
        kleio.say "I love Disrupted, such a great band..."
    else:
        kleio.say "You should take me to a Distubed concert sometime."
    $ kleio.love += 1

    return

label kleio_desire_4_male:

    if kleio.love < 150:
        kleio.say "I feel nervous around you sometimes."
    else:
        kleio.say "Why isn't your dick in my pussy right now?"
    $ kleio.love += 1

    return

label kleio_desire_5_male:

    if kleio.love < 180:
        kleio.say "What do you say we go somewhere quiet?"
    else:
        kleio.say "I miss the feeling of you fucking me."
    $ kleio.love += 1

    return

label kleio_love_0_male:

    if kleio.love < 30:
        kleio.say "Get the hell away from me."
    else:
        kleio.say "What are you listening to these days?"
    $ kleio.love += 1

    return

label kleio_love_1_male:

    if kleio.love < 60:
        kleio.say "Fuck off."
    else:
        kleio.say "I am glad I met you, you're quite the nice guy for a dork."
    $ kleio.love += 1

    return

label kleio_love_2_male:

    if kleio.love < 90:
        kleio.say "So you play World of Warcraft or what?"
    else:
        kleio.say "Fuck I am bored."
    $ kleio.love += 1

    return

label kleio_love_3_male:

    if kleio.love < 120:
        kleio.say "Is there a school for guys like you to learn how to talk to girls like me?"
    else:
        kleio.say "I know I am too good for you, but I might make an exception."
    $ kleio.love += 1

    return

label kleio_love_4_male:

    if kleio.love < 150:
        kleio.say "So are we a couple?"
    else:
        kleio.say "I think I might be falling for you..."
    $ kleio.love += 1

    return

label kleio_love_5_male:

    if kleio.love < 180:
        kleio.say "Yeah, yeah, I am in love, so what?"
    else:
        kleio.say "Please fuck me as soon as we are alone..."
    $ kleio.love += 1

    return

label kleio_good_sweet_talk_male:
    show kleio
    if kleio.love > 133:
        mike.say "Did I ever tell you that you're fucking fierce, Kleio?"
        mike.say "Because you are...and I love it!"
        show kleio happy
        kleio.say "Aww...thanks, Loverboy!"
        kleio.say "I love that you love that I'm spikey!"
    elif kleio.love > 66:
        mike.say "You ever thought about getting more tattoos, Kleio?"
        mike.say "Because the ones you have look pretty good on you!"
        show kleio happy
        kleio.say "Thanks, Loverboy!"
        kleio.say "Just call me the illustrated woman!"
    else:
        mike.say "Whoa, Kleio - you've got some balls!"
        mike.say "But in a good way, you know?"
        show kleio happy
        kleio.say "Ha, ha..."
        kleio.say "Thanks for the compliment!"
    hide kleio
    return

label kleio_bad_sweet_talk_male:
    show kleio
    mike.say "Some people might think you've got a foul mouth, Kleio."
    mike.say "But not me - I think it's cute!"
    show kleio angry
    kleio.say "What the fuck's that supposed to mean, Loverboy?"
    kleio.say "Where'd you fucking get off calling me cute?!?"
    mike.say "Erm...sorry, Kleio..."
    hide kleio
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
