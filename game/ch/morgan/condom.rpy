label morgan_use_condom:
    $ result = randint(1, 5)
    if result == 1 and game.room == "bedroom1":
        "Just because I'm calling the shots, that doesn't mean I don't need to be careful."
        "I keep one hand firmly clamped on a buttock and use the other to reach out for a condom from the bedside table."
        "All I hear from Morgan as I pull away for a moment to put it on is a slight gasp."
        "And then another as I get back into the same position as before."
    elif result == 2 and game.room == "bedroom1":
        "But all the same, there's no excuse for being too hasty and coming to regret it later - if you'll excuse the pun."
        "And seeing as how Morgan is being so nice and obedient, she can just wait there a couple of seconds longer."
        "So I have no qualms about grabbing a condom from the beside table and stretching it over my cock."
        "If anything, the need for her to wait only serves to heighten Morgan's desire for what I have in store for her next."
    elif result == 3 and game.room == "bedroom1":
        "As eager as I am to make Morgan blush a whole lot more, I'm not about to take any risks."
        "Grabbing a condom from the bedside table, I see her nod in approval."
        morgan.say "Oops - we can't forget that, now can we?"
        morgan.say "We don't want to hear the patter of tiny feet by accident!"
    elif result == 4 and game.room == "bedroom1":
        mike.say "Okay, Morgan, okay."
        mike.say "Just hold on while I take care of something real quick!"
        "Morgan leans back, a quizzical look on her face and her hands crossed over her chest."
        "I grab for one of the condoms off of the bedside table and begin to fumble it onto my cock."
        morgan.say "Ah - playing it safe I see?"
        morgan.say "Here, let me help you with that!"
        "I lie back and watch as Morgan smooths the condom down over my cock, stroking it smooth with a smile on her face the whole time."
    else:
        "I take a moment to grab a condom and pull it down over my cock."
        "I know I'm stalling for time, and the subtle chuckle from Morgan says she knows it too."
        "But almost as soon as it's in place, my mind's made up."
        "And it's well before time that she found out what I've decided on too."
    return







label morgan_warn_condom:
    if morgan.male >= 50:
        morgan.say "Whoa...what the fuck!"
        "I come to a complete halt as Morgan's tone and expression make it clear I can go no further."
        morgan.say "You're not sticking that thing inside of me without a condom, man!"
    else:
        morgan.say "Oh, [hero.name]...you bad boy!"
        "I stop dead in my tracks, suddenly aware of the chiding tone in Morgan's voice."
        morgan.say "You can't come in without protection!"
    return

label morgan_force_condom:
    if morgan.male >= 50:
        "She reaches for her jacket, which just so happens to be within grabbing distance."
        "Her hand comes back a moment later, clutching a condom."
        morgan.say "If you'd be so kind?!?"
    else:
        "She reaches for her jacket, which is atop a pile of clothes within grabbing distance."
        "And then she offers me the condom she's recovered."
        morgan.say "You can come on in once you're properly dressed!"
    return







label morgan_no_condom:
    "I'm too lost in the moment to be thinking about anything other than sinking down atop Morgan right now."
    "She seems to feel the exact same way, eagerly welcoming me as I come to her, wrapping herself around me."
    "I can't imagine how long she's been waiting for this moment, and the last thing that I want is to deny it to her any longer."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
