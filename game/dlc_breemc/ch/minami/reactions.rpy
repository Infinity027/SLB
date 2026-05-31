label minami_ask_birthday_female:
    bree.say "Ooh, Minami..."
    bree.say "I meant to ask - when is your birthday?"
    if hero.charm >= 40 - minami.love:
        show minami happy
        $ minami.flags.birthdayknown = True
        minami.say "Oh sure, [hero.name]..."
        minami.say "It's Summer 25."
        minami.say "Be sure to write that down!"
    else:
        show minami annoyed
        minami.say "I'm super careful with my personal information."
        minami.say "I only give it out on a need to know basis."
        $ minami.sub -= 1
        $ minami.love -= 1
    return

label minami_ice_cream_reaction_female:
    "I hurry over to the ice-cream booth, already pointing to the flavour that I want for myself."
    "And Minami's only a step behind me, looking every bit as enthusiastic about it too!"
    minami.say "Ooh, [hero.name]..."
    minami.say "What's that called?"
    minami.say "It looks SO good!"
    "I can't help smiling as Minami eyes up my choice of ice-cream."
    "It looks like her eyes are going to pop out of her head any moment!"
    bree.say "It doesn't really have a name, Minami."
    bree.say "It's just everything that I like all together."
    minami.say "That sounds great."
    minami.say "I'll have one of those too!"
    "Minami orders her ice-cream just as mine is ready, still gazing at it with longing."
    "As soon as she has it in her hand, she beams happily, but doesn't start to lick it."
    bree.say "What are you waiting for, Minami?"
    bree.say "I thought you were aching to get your ice-cream?"
    minami.say "I was just waiting for you to start yours, [hero.name]."
    minami.say "It's kind of big - I don't know where to start!"
    "I shake my head, smiling at Minami's confession."
    "Then I close my eyes and take my first lick."
    bree.say "Mmm..."
    bree.say "So, so good!"
    minami.say "Oh yeah..."
    minami.say "You got that right!"
    return

label minami_ask_phone_female:
    bree.say "Could I get your phone number, Minami?"
    bree.say "That way we can keep in touch, yeah?"
    bree.say "And we don't need to use [mike.name] as a go-between!"
    if hero.charm >= 20 - minami.love:
        show minami happy
        $ hero.smartphone_contacts.append("minami")
        minami.say "Here you go, [hero.name]."
        minami.say "Call me so I can get yours too."
        minami.say "We don't want big bro listening in on us, do we?"
    else:
        show minami annoyed
        minami.say "Erm...I don't think so, [hero.name]."
        minami.say "Don't take this personally, but we're not there yet."
        minami.say "I kinda want to keep big bro in the loop, just a little longer."
        $ minami.love -= 1
        $ minami.sub -= 1
    return

label minami_offer_a_drink_female:
    bree.say "Looks like you're running low there, Minami."
    bree.say "You want me to get you another drink?"
    if (hero.charm >= 60 - minami.love and minami.flags.drinks < 2) or date_girl == minami:
        show minami happy
        minami.say "Oh yeah..."
        minami.say "You're right, [hero.name]!"
        minami.say "I'll have the same again."
        hide minami
        show drink minami
        if minami.love <= 25:
            $ minami.love += 1
        elif date_girl == minami and game.active_date:
            $ game.active_date.score += 5
        call expression minami.get_chat from _call_expression_398
        hide drink minami
        $ minami.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show minami annoyed
        minami.say "No thanks, [hero.name]."
        minami.say "I'll get my own drinks, yeah?"
        minami.say "I just don't trust anyone else to get them for me."
        minami.say "It's so easy for someone to spike you."
        $ hero.cancel_activity()
        hide minami
    return

label minami_slap_ass_intro_female:
    "When Minami walks past, I don't know what comes over me."
    "It's just the sight of that pert little ass under such a short skirt."
    "I can't control myself, and it's like I suddenly turn into a horny guy!"
    "Before I know what I'm doing, my hand is swinging towards it."
    "The palm connects with an audible slap, and Minami jumps at the sensation."
    return

label minami_slap_ass_happy_female:
    minami.say "Ouch!"
    minami.say "HEY!"
    minami.say "Did...did you just slap my ass?!?"
    "My cheeks are flushed red and I can't meet Minami's eye."
    bree.say "I...I'm sorry, Minami."
    bree.say "Your ass is so pert and perfect..."
    bree.say "I just couldn't help myself!"
    "Minami smiles and lets out a giggle."
    minami.say "Aww..."
    minami.say "Thanks, [hero.name]!"
    minami.say "That's such a nice compliment."
    return

label minami_slap_ass_angry_female:
    minami.say "Ouch!"
    minami.say "HEY!"
    minami.say "What the hell, [hero.name]?!?"
    "My cheeks are flushed red and I can't meet Minami's eye."
    bree.say "I...I'm sorry, Minami."
    bree.say "Your ass is so pert and perfect..."
    bree.say "I just couldn't help myself!"
    "Minami frowns and shakes her head."
    minami.say "Well try harder next time, yeah?"
    minami.say "Geez...you're as bad as a guy!"
    return

label minami_breakup_female:
    show minami
    "I take a deep breath and then let it out in a long, weary sigh."
    "The sound is loud enough for Minami to hear it and turn to face me."
    minami.say "Ooh..."
    show minami sad
    minami.say "That doesn't sound good, [hero.name]!"
    bree.say "No, Minami...it's not."
    bree.say "I kind of have something to say to you..."
    "I take another breath, then forge ahead regardless of the consequences."
    bree.say "The thing is, Minami..."
    bree.say "I don't think this thing is working out between us."
    minami.say "What are you saying, [hero.name]?"
    bree.say "I'm saying that we should call it a day, Minami."
    bree.say "I think we should break up."
    "Minami's face drops at the mere mention of ending our relationship."
    "But then she seems to rally, as if there's a chance to change my mind."
    minami.say "Are you sure, [hero.name]?"
    minami.say "Maybe we just need to try a little harder?"
    "I shake my head, hating myself for stifling her hope."
    bree.say "That's the thing, Minami - I have been trying hard."
    bree.say "And I can't try any harder, I just can't!"
    minami.say "Oh...okay, [hero.name]..."
    minami.say "If that's how you feel."
    return

label minami_go_steady_intro_female:
    "I summon up all of my courage, and then I open my mouth to say my piece."
    "Even as I do so, I can feel the fear welling up in my stomach."
    "But I steel myself and press on, determined to say it all the same."
    bree.say "Minami..."
    bree.say "I think we're pretty good together - don't you?"
    bree.say "Like, good enough to make it official?"
    "Minami looks me in the eye, surprise written all over her face."
    return

label minami_go_steady_yes_female:
    minami.say "O...M...G!"
    minami.say "[hero.name], are you REALLY asking me to be your GF?"
    minami.say "Of course I want to make it official!"
    "Minami throws her arms around me and kisses me on the lips."
    "I'm a little overwhelmed at first, but I recover soon enough."
    "And the fear in my stomach is replaced with excitement."
    return

label minami_go_steady_no_female:
    minami.say "FFS..."
    minami.say "[hero.name], you can't be asking me to be your GF?"
    minami.say "I mean, we were just getting to know each other."
    minami.say "We're hardly more than good friends!"
    "I'm instantly disappointed, but I do the best I can to hide it."
    "I nod and try to put a smile on my face, hard as it is."
    "But the fear in my stomach has been replaced with disappointment."
    return

label minami_pet_intro_female:
    "Minami just looks so cute today, I can't believe my eyes."
    "Now I get what people mean when they say someone looks good enough to eat!"
    "In fact, it kind of feels like I'm on autopilot as I smile at her."
    "Which maybe helps to explain what happens next."
    "As I can't help reaching out and patting Minami on the head!"
    "She looks up in surprise, wondering what just happened."
    minami.say "[hero.name]..."
    minami.say "Did you...did you..."
    minami.say "Did you just pat me on the head?"
    bree.say "Erm, yeah...I guess I did!"
    return

label minami_pet_happy_female:
    "Minami smiles and lets out a happy giggle."
    minami.say "Oh, okay..."
    minami.say "You just caught me off guard, that's all!"
    minami.say "It's nice to know who's being nice to me!"
    "I smile too, relieved that she's okay with it."
    return

label minami_pet_annoyed_female:
    "Minami frowns and shakes her head."
    minami.say "That's NOT cool, [hero.name]!"
    minami.say "You can't just do that to me."
    minami.say "I'm not a dog, you know!"
    "I nod, embarrassed at being chewed out by Minami."
    return

label minami_massage_intro_female:
    bree.say "Ouch, Minami..."
    bree.say "I felt that!"
    minami.say "Ooh...yeah, [hero.name]!"
    minami.say "I guess I must have pulled something!"
    bree.say "You want me to give you a massage?"
    bree.say "I'm told that I'm pretty good at it!"
    return

label minami_massage_accept_female:
    minami.say "Would you, [hero.name]?"
    minami.say "That sounds like a really good idea."
    minami.say "How soon can you fit me in?"
    bree.say "I can do you right now, Minami."
    bree.say "We just need to find somewhere to do it..."
    return

label minami_massage_refuse_female:
    minami.say "Oh no...no way!"
    bree.say "Are you sure?"
    bree.say "I do know what I'm doing - I promise!"
    minami.say "No, [hero.name], seriously!"
    minami.say "I let big bro do me once."
    minami.say "And I was in pain for a week!"
    return

label minami_piercing_nipples_reaction_female:
    "Minami strides up to me, thrusting her chest out in front of her."
    "My eyes go wide at the sight of her impressive little chest."
    "And then they go wider still as I see the new additions."
    bree.say "Whoa..."
    bree.say "Minami, you got them done?"
    "Minami nods and smiles, clearly pleased with my reaction."
    minami.say "Oh yeah - I got both nipples pierced!"
    minami.say "You like?"
    bree.say "Sure I do, Minami."
    bree.say "They look amazing!"
    "Minami giggles at my obvious fascination with her chest."
    "But all I can think about is getting my hands on them."
    return

label minami_piercing_navel_reaction_female:
    "Minami strides up to me, thrusting her belly out in front of her."
    "My eyes go wide at the sight of her perfectly flat stomach."
    "And then they go wider still as I see the new addition."
    bree.say "Whoa..."
    bree.say "Minami, you got it done?"
    "Minami nods and smiles, clearly pleased with my reaction."
    minami.say "Oh yeah - I got it pierced!"
    minami.say "You like?"
    bree.say "Sure I do, Minami."
    bree.say "It looks amazing!"
    "Minami giggles at my obvious fascination with her belly button."
    "But all I can think about is getting my hands on it."
    return

label minami_piercing_clit_reaction_female:
    "Minami strides up to me with a smile on her face."
    "She holds my eye, then draws them downwards."
    "And then she all but points to her groin."
    bree.say "Whoa..."
    bree.say "Minami, you got it done?"
    "Minami nods and smiles, clearly pleased with my reaction."
    minami.say "Oh yeah - I got it pierced!"
    minami.say "You want to see?"
    bree.say "Sure I do, Minami."
    bree.say "It must feel amazing!"
    "Minami giggles at my obvious fascination with her new addition."
    "But all I can think about is getting my hands on it."
    minami.say "Oh yeah, [hero.name]..."
    minami.say "It feels SO fucking hot!"
    return

label minami_piercing_head_reaction_female:
    "Minami strides up to me with a smile on her face."
    "My eyes go wide as she boldly sticks her tongue out at me."
    "And then they go wider still as I see the new addition."
    bree.say "Whoa..."
    bree.say "Minami, you got it done?"
    "Minami nods and smiles, clearly pleased with my reaction."
    minami.say "Oh yeah - I got it pierced!"
    minami.say "You like?"
    bree.say "Sure I do, Minami."
    bree.say "It looks amazing!"
    "Minami giggles at my obvious fascination with her tongue."
    "But all I can think about is how it's going to feel."
    "All I want to do right now is kiss Minami until my own tongue is numb!"
    return

label minami_movie_liked_reaction_female:
    bree.say "WOW!"
    bree.say "That was like the best film I've seen in forever!"
    bree.say "Right, Minami?"
    minami.say "You bet, [hero.name]!"
    minami.say "I want to see it again as soon as I can."
    minami.say "So many new cosplay ideas too!"
    return

label minami_movie_indifferent_reaction_female:
    bree.say "WOW!"
    bree.say "That was like the best film I've seen in forever!"
    bree.say "Right, Minami?"
    minami.say "Ah...it was okay, I guess."
    minami.say "But I could wait a while to see it again."
    return

label minami_movie_disliked_reaction_female:
    bree.say "WOW!"
    bree.say "That was like the best film I've seen in forever!"
    bree.say "Right, Minami?"
    minami.say "Oh no, [hero.name]!"
    minami.say "How can you even say that?"
    minami.say "That movie was such a stinker!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
