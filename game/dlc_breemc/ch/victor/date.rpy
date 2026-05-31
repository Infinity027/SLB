label victor_date_eat_a_burger_female:
    "I'm not sure how victor's going to react to the burger that I ordered for him."
    "But as soon as mine arrives, I hear the sound of my stomach growling with hunger."
    "And I can't resist grabbing it and beginning to devour the whole thing."
    "Victor looks at me, wide-eyed with amazement, I assume at my evident appetite."
    "Then he starts to eat himself, at a much slower pace, but showing appreciation for the food."
    return

label victor_date_buy_drink_female:
    if hero.morality >= 25:
        bree.say "I think I can handle one more drink!"
        bree.say "Would you like me to get you one too, Victor?"
    elif hero.morality <= 25:
        bree.say "Time for another one!"
        bree.say "You want me to get you one too, Victor?"
    else:
        bree.say "My round again - better hope I don't get too drunk and outrageous!"
        bree.say "You want one too, Victor?"
    if hero.is_visibly_pregnant:
        if victor.sub >= 50:
            victor.say "Erm...I don't want to be rude, [hero.name]..."
            victor.say "But should you be drinking when you're pregnant?"
        elif victor.sub <= -50:
            victor.say "No, [hero.name], you won't be having another."
            victor.say "Not while you're pregnant."
        else:
            victor.say "I don't want to tell you your business, [hero.name]..."
            victor.say "But drinking so much isn't good for your baby."
    else:
        if victor.sub >= 50:
            victor.say "I'll have one if you think I should, [hero.name]!"
            victor.say "Could you pick a drink for me too?"
        elif victor.sub <= -50:
            victor.say "Aren't you getting a little ahead of yourself, [hero.name]?"
            victor.say "That's the kind of decision I should be making for you."
        else:
            victor.say "Sure, [hero.name], I'll have another one."
            victor.say "Could I get the same again?"
    return

label victor_date_play_darts_female:
    "The moment victor lines up to take his first shot, I realise the mistake I've made."
    "I mean, what was I thinking - playing darts with a genuine, bona fide assassin?"
    "All I can do is watch as he hits the bullseye with each of his darts in turn."
    "Using the dead-eye accuracy that I've seen him display with a pistol to win the game."
    "So I make a mental note not to challenge him to this kind of game again."
    return

label victor_date_pub_play_pool_female:
    "Victor's so good at what he does, I was kind of expecting him to wipe the floor with me."
    "But somehow those dead-eye skills with a pistol don't seem to translate into the game of pool."
    "I watch as he fouls on the cue-ball multiple times and misses some pretty easy shots."
    "And it's not like he's letting me win either, as it's impossible to pretend to be that bad."
    "So as soon as I win the game, I make a mental note not to challenge him to another."
    return

label victor_date_buy_a_round_female:
    if hero.morality >= 25:
        bree.say "I think it's my round!"
        bree.say "Would you like me to get you one too, Victor?"
    if hero.morality <= 25:
        bree.say "Time for another round!"
        bree.say "You want me to get you one too, Victor?"
    else:
        bree.say "My round again - better hope I don't get too drunk and outrageous!"
        bree.say "You want one too, Victor?"
    if hero.is_visibly_pregnant:
        if victor.sub >= 50:
            victor.say "Erm...I don't want to be rude, [hero.name]..."
            victor.say "But should you be drinking when you're pregnant?"
        elif victor.sub <= -50:
            victor.say "No, [hero.name], you won't be having another."
            victor.say "Not while you're pregnant."
        else:
            victor.say "I don't want to tell you your business, [hero.name]..."
            victor.say "But drinking so much isn't good for your baby."
    else:
        if victor.sub >= 50:
            victor.say "I'll have one if you think I should, [hero.name]!"
            victor.say "Could you pick a drink for me too?"
        elif victor.sub <= -50:
            victor.say "Aren't you getting a little ahead of yourself, [hero.name]?"
            victor.say "That's the kind of decision I should be making for you."
        else:
            victor.say "Sure, [hero.name], I'll have another one."
            victor.say "Could I get the same again?"
    return

label victor_dance_with_female:
    "As soon as I hear one of my favourite songs start playing, I'm up and ready to dance."
    "And I make sure to grab hold of Victor, so that he's yanked up and comes with me."
    "I can see the look of fear in his eyes as I pull him onto the dance-floor too."
    "And as soon as we start actually dancing, the reason becomes pretty apparent."
    "Because he jerks around like he's being hit with electric shocks the whole time."
    "So apparently that smoothness and dexterity he does his job with doesn't translate."
    "Because he has to be one of the worst dancers I've ever seen in my life!"
    return

label victor_date_play_arcade_intro_female:
    bree.say "Come on, Victor - let's play that arcade cabinet."
    victor.say "Ah...are you sure, [hero.name]?"
    bree.say "Yeah, it's 'Deadly Cops', classic light-gun game."
    bree.say "With your skills, you should be great at it."
    "Victor nods as I lead him over to the cabinet."
    "And he stands there in silence as I pump in the coins."
    "But when I shove one of the plastic guns into his hand, he seems to perk up a little."
    victor.say "Huh..."
    victor.say "Lighter than the real thing, but I can work with that."
    return

label victor_date_play_arcade_win_female:
    "The game begins and I jump straight into it, shooting and shouting."
    "Aiming for the bank-robbers and other villains that pop up on the screen."
    "There's no time for me to look around and see how well Victor's doing."
    "But once the game is over, that becomes all too apparent."
    bree.say "Wow, Victor..."
    bree.say "You really suck at this!"
    bree.say "How is that even possible?"
    victor.say "Ah, well..."
    victor.say "It is, like, a videogame, [hero.name]!"
    victor.say "The real thing is a little different."
    return

label victor_date_play_arcade_lose_female:
    "The game begins and I jump straight into it, shooting and shouting."
    "Aiming for the bank-robbers and other villains that pop up on the screen."
    "There's no time for me to look around and see how well Victor's doing."
    "But once the game is over, that becomes all too apparent."
    bree.say "Wow, Victor..."
    bree.say "You're really good at this!"
    bree.say "How is that even possible to get a score that high?"
    victor.say "Ah, well..."
    victor.say "This is kind of what I do, [hero.name]..."
    victor.say "And I guess they made the game really true to life."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
