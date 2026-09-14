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
