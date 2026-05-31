label hanna_use_condom:
    $ result = randint(1, 5)
    if result == 1:
        "All the same, that's not permission to throw caution to the wind."
        "And so I reach for a condom, quickly tearing open the packet."
        "Hanna nods with just as much speed, and I know that we're on the same page."
        "A moment later it's on, and we're all good to go."
    elif result == 2:
        "Eager as I am to get things moving, there's no way I'm forgetting to take precautions."
        "And so I pause to grab a condom and tear open the packet."
        "Hanna glances, trying to see what's causing the delay."
        "But as soon as she sees what I'm doing, she nods in agreement."
    elif result == 3:
        "One last thing."
        "I take a step back to where I've discarded my jeans and take the condom out of my pocket, slipping it on."
    elif result == 4 and game.room == "bedroom1":
        "But even though I'm so eager, there's always time to take basic precautions."
        "I reach over and pluck a condom from the bedside table."
        "Hanna looks a little put out by the delay, but she nods all the same."
        "So I hastily rip the packet open with my teeth and put it on."
    else:
        "But then I remember that we need to take precautions."
        mike.say "Wait a second, Hanna."
        mike.say "I think I have a condom in my pocket..."
        hanna.say "You carry them in your pocket?!?"
        mike.say "You'd rather I didn't bother?"
        hanna.say "Point taken!"
        "It only takes me a couple of seconds to get the thing on."
        "Then we're all ready to go."
    return

label hanna_intro_condom:
    $ result = randint(1, 5)
    if result == 1:
        "She looks ready and willing, but then seems to realize something, and draws a sharp, almost inaudible gasp."
        "Blushing madly she end up smiling at me and signing me to come closer."
    elif result == 2:
        "I'm so eager to get things moving that I want to plough straight ahead without delay."
    elif result == 3:
        "I step forward to the bed, like a werewolf stepping up over a sheep, ready to devour her whole."
    elif result == 4:
        "I need to be inside of Hanna so badly right now!"
        "I can't think of anything else."
    else:
        "Her pussy is almost glistening in the light, wet and inviting."
    return

label hanna_warn_condom:
    $ result = randint(1, 4)
    if result == 1:
        hanna.say "Ahem!"
        hanna.say "Isn't there a little something else to do before me?"
    elif result == 2:
        "But as I try to push on, Hanna wriggles a little way out of reach."
        "She looks at me, a question in her eyes."
        "And then I realise that she wants to know why I'm not using a condom."
    elif result == 3:
        hanna.say "Damn it!"
        hanna.say "We need to use a condom!"
        mike.say "Huh?"
    else:
        hanna.say "Wait..."
        "She looks ready and willing, but then seems to realize something, and draws a sharp, almost inaudible gasp, dropping the hand at her mouth suddenly to cover the lips between her legs."
    return

label hanna_force_condom:
    $ result = randint(1, 6)
    if result == 1:
        "Hanna holds up a condom, raising an eyebrow as she does so."
        "I nod, feeling good know that we're on the same page."
        "Grabbing the condom from Hanna, I tear open the packet."
        "A moment later it's on, and we're all good to go."
    elif result == 2:





        hanna.say "Let's use protection."
        "I fumble for a condom from the bedside table, but there's none to be found."
        mike.say "Shit...I ran out!"
        hanna.say "Sorry, another time then..."
        return False
    elif result == 3:
        "Hanna coughs a little, nodding towards her pile of discarded clothes."
        "I follow her gaze, quickly rummaging through her pockets until I find what I'm looking for."
        "It's a condom, and I waste no time in tearing open the packet and slipping it on."
        "Hanna nods in agreement, satisfied and ready to pick up where we left off."
    elif result == 4:
        hanna.say "Of course we do!"
        hanna.say "Don't worry, I have one right here!"
        mike.say "You carry them around on you?!?"
        hanna.say "You'd rather I didn't?"
        mike.say "Point taken!"
        "It only takes me a couple of seconds to get the thing on."
        "Then we're all ready to go."
    elif result == 5:
        "But Hanna's taken the time to think about basic precautions."
        "She holds up one hand to stop me, and then the other with a condom in it."
        "I can't a little put out by the delay, but I nod all the same."
        "I hastily rip the packet open with my teeth and put it on."
    else:
        "Damn."




        hanna.say "Let's use protection."
        "I fumble for a condom from the bedside table, but there's none to be found."
        mike.say "Shit...I ran out!"
        hanna.say "Sorry, another time then..."
        return False
    return

label hanna_mad_condom:
    $ result = randint(1, 4)
    if result == 1:
        mike.say "Huh..."
        mike.say "I thought you were ready to go!"
        "Hanna's face darkens at this, and I can tell instantly that I just fucked up."
        "Hanna kicks out with her legs, catching me painfully in the side of the head."
        mike.say "Argh...shit!"
        "As I cradle my face, she gets up and grabs her scattered clothes."
        hanna.say "Asshole!"
        "I hear, rather than see her leave, slamming the door loudly as she goes."
    elif result == 2:
        mike.say "We don't need to use protection, Hanna."
        mike.say "Plus that's just going to spoil the thrill!"
        "Hanna looks at me with a shocked expression on her face."
        hanna.say "How can you be so irresponsible?!?"
        hanna.say "That's such a mood-killer!"
        "Before I can say anything to object, Hanna's up and getting dressed."
        "And thanks to the skimpiness of her clothes, that doesn't take long!"
        "I have no choice but to do the same and watch as she storms off afterwards."
        "There's no way I can argue with her, not with so many other people still in the gym."
    elif result == 3:
        hanna.say "Hey...wait a minute."
        mike.say "What...what's up?!?"
        hanna.say "Aren't you forgetting something?"
        mike.say "You mean a condom - are you serious?"
        hanna.say "ARE YOU?!?"
        "And with that, she shoves me so hard that I tumble off of her."
        hanna.say "Jesus, [hero.name] - grow up and get a clue!"
    else:
        "I shrug, trying to play it off as something to be amused about."
        mike.say "I could always do you up the ass instead?"
        mike.say "That way we don't need a condom!"
        "Instantly upon hearing my words, Hanna's face twists into a mask of outrage."
        hanna.say "You think this is funny?!?"
        hanna.say "Well here's something to laugh at - I'm going home!"
        "That said, she scrambles away from me and gets to her feet."
        "I try more than once to talk her around."
        "But whenever I as much as open my mouth, Hanna shoots me a murderous stare that shuts me down again."
        "No more than a couple of minutes later, she's gone and I'm all alone in my room."
        "I watch in disappointment as my cock droops before my eyes."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
