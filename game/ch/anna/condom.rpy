label anna_use_condom:
    $ result = randint(1, 4)
    if result == 1 and game.room == "bedroom1":
        mike.say "But you just hold on while I put the safety on it first!"
        "Anna giggles again as I fumble blindly for the condoms on the bedside table, not wanting to take my eyes off of her."
        "I slide the condom on hastily, not wanting to wait a second longer than necessary."
    elif result == 2 and game.room == "bedroom1":
        "As willing and suggestible as she is, that's no reason not to be careful while I have my fun with Anna."
        "So I pause for a moment to pick up a condom from the bedside table and pull it on before going any further."
        "Looking back over her shoulder, Anna sees what's keeping me, and makes no attempt to object to the delay."
    elif result == 3 and game.room == "bedroom1":
        "I see a few condoms on the bedside dresser and snatch one when I'm in range."
        "Anna watches me intently as I roll onto my back and slide the condom down over my now very erect cock."
        "It's hard to concentrate, as she's watching me like a hungry animal, waiting for the right moment to pounce."
    else:
        "But I have to make sure we play it safe."
        "So I hold up a hand to stop Anna in her tracks."
        mike.say "Wait a minute, Anna."
        mike.say "We should use some protection."
        "Anna looks at me and blinks, like it'd totally slipped her mind."
        "Then she nods, urging me to take care of it as soon as I can."
        "I take the hint, grabbing a condom and slipping it on in record time."
        "That done, we're ready to go."
    return

label anna_intro_condom:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "It's fully-charged and ready to go!"
    elif result == 2:
        "I'm sure a less suggestible and easily lead girl would have stopped me dead in my tracks without a condom."
        "But with Anna, there's no such problem, as she seems happy to leave any responsibility in my hands alone."
        "Eager to take full advantage of her being so easy, I don't hesitate to leap straight onto her."
    else:
        "I roll slightly onto my back, and my very erect cock pulls the sheets with it like a tentpole."
        "Anna watches my cock, and not me, eyeing it up like it's all she cares about in the world right now."
        "I can't shake the feeling that she's already imagining how it'll feel once it's inside of her."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
