label master_use_condom:
    $ result = randint(0, 1)
    if result == 0:
        "We're really getting into it now, both of us narrowing our focus towards one goal."
        "And part of me feels like this is all an extension of the training I've been put through."
        "But then that same clarity of thought and vision seems to make some thing crystal clear to me."
        "And I hold up a hand, stopping the master in his tracks."
        master.say "Eh?"
        master.say "What...what's the matter?"
        if hero.morality >= 25:
            bree.say "Wait a second..."
            bree.say "I need to go grab something!"
        elif hero.morality <= -25:
            bree.say "Hold your horses, you randy old goat!"
            bree.say "This will only take a second."
        else:
            bree.say "Just a moment, Master..."
            bree.say "We almost forgot something important!"
        "The old man watches closely as I jump up and head over to where my clothes lie in a heap on the floor."
        "A quick search soon puts what I'm looking for in my hand, and I hold it up as I return to him."
        master.say "Oh...a condom!"
        master.say "Of course, of course..."
        "It only takes me a few more seconds to tear open the packaging and put the thing on him."
        "Then we're all ready to go."
    else:
        "But before we go any further, I remember that we need to be careful."
        "So I pause to reach over to the bedside table, looking for what I need."
        master.say "Eh?"
        master.say "What...what are you doing?"
        "I don't bother to turn my head to give the Master my answer."
        "Instead I keep right on with the task at hand."
        if hero.morality >= 25:
            bree.say "Nothing to worry about - just getting some protection."
        elif hero.morality <= -25:
            bree.say "Hang on - you're not going any further without a rubber on that thing!"
        else:
            bree.say "Just a second - I'm grabbing a condom."
        "Once I have the condom in my hand, I turn back and let the Master see it."
        "That seems to satisfy him, as he nods eagerly."
        "Then all that we have to do is get the thing on him and we're good to go."
    return

label master_intro_condom:
    $ result = randint(0, 1)
    if result == 0:
        "We're really getting into it now, both of us narrowing our focus towards one goal."
        "And part of me feels like this is all an extension of the training I've been put through."
        "But then the old man gets an odd look on his face, like something just occurred to him."
        "And he holds up a hand, stopping me in my tracks and making me frown."
    else:
        "But before I can do anything more, the Master seems to come to his senses."
        "He holds up a hand to stop me, shaking his head as he does so."

    return

label master_mad_nocondom:
    $ result = randint(0, 1)
    if result == 0:
        master.say "We need to use some protection"
        "I can't help shaking my head and furrowing my brow in frustration."
        if hero.morality >= 25:
            bree.say "We don't have to use a condom, do we?"
            bree.say "Can't we just do it without one this time?"
        elif hero.morality <= -25:
            bree.say "No way, not happening!"
            bree.say "Either ride me bareback, or this horny mare is throwing you off!"
        else:
            bree.say "No way!"
            bree.say "Just get on with it and forget the condom."
        "The master surprises me by shaking his head and as he gets up."
        "Then he walks away and starts to put his clothes back on."
        master.say "My dear, I thought that you were wiser than that."
        master.say "But it seems that my lessons have not sunk in."
        if hero.morality >= 25:
            bree.say "Master, no - come back!"
        elif hero.morality <= -25:
            bree.say "Hey, get back here and do your duty!"
        else:
            bree.say "What are you doing?"
        "But no matter what I say, it doesn't have any affect on him."
        "Instead the old man dresses himself and then walks out on me."
        "Leaving me laying there alone, and all for the sake of one lousy condom."
    else:
        master.say "Wait a moment, my dear..."
        master.say "We need to use some protection!"
        if hero.morality >= 25:
            bree.say "Can't we just forget it this one time, Master?"
        elif hero.morality <= -25:
            bree.say "Forget the fucking condom and fuck me bareback!"
        else:
            bree.say "Ah, just forget it this once, okay?"
        "I'm not at all prepared for the look of shock and revulsion that appears on the old man's face."
        "As if my words are the most preposterous and insane thing he's ever heard."
        "And I'm also not ready for it when he reaches up and shoves me off him either."
        bree.say "Wha..."
        bree.say "WHOA!"
        "I go tumbling backward, almost rolling right off the bed."
        "At the same time, the Master leaps up and begins puling on his clothes."
        "And once I've managed to get myself upright again, he's pretty much dressed."
        master.say "Have my lessons taught you nothing, girl?"
        master.say "How can you be so foolish?"
        if game.calendar.is_today(*master.birthday):
            master.say "And not only that, you've totally ruined my birthday too!"
        "Before I can argue or even say a word, he's reached the door."
        "He storms straight out and I hear his feet pounding down the stairs."
        "That's followed by the sound of the front-door slamming shut."
        "Letting me know that he's really gone, and that I totally blew it."
    return

label master_mad_condom:
    master.say "Hmm..."
    master.say "Did we forget something?"
    "Almost as soon as he asks the question, I realise he's right."
    "There is one thing that we've forgotten."
    "And it's an important thing too."
    if hero.morality >= 25:
        bree.say "Wait a second..."
        bree.say "I need to go grab a condom!"
    elif hero.morality <= -25:
        bree.say "Hold your horses, you randy old goat!"
        bree.say "I need to go grab a condom."
    else:
        bree.say "Just a moment, Master..."
        bree.say "We almost forgot to use protection!"
    "The old man frowns as I tell him what I need."
    "And then he shakes his head as he gets up and walks away."
    master.say "My dear, I thought that you were wiser than that."
    master.say "But it seems that my lessons have not sunk in."
    if hero.morality >= 25:
        bree.say "Master, no - come back!"
    elif hero.morality <= -25:
        bree.say "Hey, get back here and do your duty!"
    else:
        bree.say "What are you doing?"
    "But no matter what I say, it doesn't have any affect on him."
    "Instead the old man dresses himself and then walks out on me."
    "Leaving me laying there alone, and all for the sake of one lousy condom."
    "But maybe if he's not willing to take precautions, I shouldn't be that upset."
    return

label master_force_condom:
    $ result = randint(0, 1)
    if result == 0:
        master.say "Whoa, whoa..."
        master.say "Wait a moment, my dear..."
        if hero.morality >= 25:
            bree.say "What is it, Master?"
            bree.say "What could be more important than what we're about to do?"
        elif hero.morality <= -25:
            bree.say "You'd better have a good reason for tapping the breaks, old man."
            bree.say "Because nobody stops this train when it's bound for booty-city!"
        else:
            bree.say "Are you serious?"
            bree.say "You want to stop now?!?"
        "I watch closely as the old man jumps up and heads over to where his clothes lie in a heap on the floor."
        "He roots around in the pockets for a few seconds, then hold up what he was looking for."
        "Then he returns, holding it out for me to take from him."
        if hero.morality >= 25:
            bree.say "A condom - why didn't you just say that was what you wanted?"
        elif hero.morality <= -25:
            bree.say "Jeez...just tell me next time you want to use a condom, okay?"
        else:
            bree.say "Oh, right - a condom!"
        "It only takes me a few more seconds to tear open the packaging and put the thing on him."
        "Then we're all ready to go."
    else:
        master.say "Wait a moment, my dear..."
        master.say "We need to use some protection!"
        "Before I can say a word in response, he points to his clothes, which are in a pile a the side of the bed."
        master.say "I have one in my pocket..."
        master.say "Just over there."
        "From my current position, I can easily lean over and reach them."
        "So I follow his directions and soon find the condom in one of his pockets."
        "Once I have it in my hand, I turn back and let the Master see it."
        "That seems to satisfy him, as he nods eagerly."
        "Then all that we have to do is get the thing on him and we're good to go."
    return

label master_mad_condom_female:
    master.say "Hmm..."
    master.say "Did we forget something?"
    "Almost as soon as he asks the question, I realise he's right."
    "There is one thing that we've forgotten."
    "And it's an important thing too."
    if hero.morality >= 25:
        bree.say "Wait a second..."
        bree.say "I need to go grab a condom!"
    elif hero.morality <= -25:
        bree.say "Hold your horses, you randy old goat!"
        bree.say "I need to go grab a condom."
    else:
        bree.say "Just a moment, Master..."
        bree.say "We almost forgot to use protection!"
    "The old man frowns as I tell him what I need."
    master.say "No time for that now..."
    master.say "Just get on with it already!"
    "I can't believe what I'm hearing, and it makes me pull away from him."
    "Before I know it, I'm up and walking over to where I left my clothes."
    master.say "What...what are you doing?!?"
    if hero.morality >= 25:
        bree.say "No condom, no nothing!"
    elif hero.morality <= -25:
        bree.say "You're not coming near me without a condom on that thing!"
    else:
        bree.say "I'm not doing it without protection."
    "The old man keeps on pleading his case as I pull on my clothes."
    "But he doesn't seem willing to back down on the no condom position he's adopted."
    "And so I just ignore him, walking out as soon as I'm fully dressed."
    "Hopefully this will teach him a lesson, and he'll do as he's told next time."
    return

label master_mad_nocondom_female:
    master.say "Whoa, whoa..."
    master.say "Wait a moment, my dear..."
    if hero.morality >= 25:
        bree.say "What is it, Master?"
        bree.say "What could be more important than what we're about to do?"
    elif hero.morality <= -25:
        bree.say "You'd better have a good reason for tapping the breaks, old man."
        bree.say "Because nobody stops this train when it's bound for booty-city!"
    else:
        bree.say "Are you serious?"
        bree.say "You want to stop now?!?"
    master.say "A condom, my dear..."
    master.say "We need to use protection!"
    "I can't believe what I'm hearing, and it makes me pull away from him."
    "Before I know it, I'm up and walking over to where I left my clothes."
    master.say "What...what are you doing?!?"
    if hero.morality >= 25:
        bree.say "I'm not wearing one of those ugly things!"
    elif hero.morality <= -25:
        bree.say "Too late, this train's being rerouted!"
    else:
        bree.say "I want to do it, not mess around with one of those things!"
    "The old man keeps on pleading his case as I pull on my clothes."
    "But he doesn't seem willing to back down on the no condom position he's adopted."
    "And so I just ignore him, walking out as soon as I'm fully dressed."
    "Hopefully this will teach him a lesson, and he'll do as he's told next time."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
