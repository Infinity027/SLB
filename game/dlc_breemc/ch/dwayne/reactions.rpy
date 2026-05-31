label dwayne_ice_cream_reaction_female:
    bree.say "Phew..."
    bree.say "I'm melting here, Dwayne!"
    bree.say "How are you keeping so damn cool?"
    "Dwayne shoots me one of his most impressive smiles."
    "And then he shrugs his shoulders like it's nothing."
    dwayne.say "What can I say, [hero.name]?"
    dwayne.say "I just know how to take the heat!"
    bree.say "That's alright for you - but I need an ice-cream!"
    "Dwayne nods and then follows me over to the ice-cream stand."
    "We both order, and then he insists on paying as we're handed our ice-creams."
    bree.say "Whoa, Dwayne!"
    bree.say "That thing's huge!"
    "Dwayne laughs at the obvious double meaning as he licks at his ice-cream."
    dwayne.say "Yeah, [hero.name]..."
    dwayne.say "I get that all the time!"
    dwayne.say "You can have a lick - so long as you think you can handle it!"
    "I roll my eyes and shake my head, refusing to rise to the bait."
    return

label dwayne_ask_phone_female:
    bree.say "You should let me have your phone number, Dwayne."
    bree.say "That way I can get hold of you whenever."
    bree.say "No messing around calling someone to get them to call you."
    if hero.charm >= 20 - dwayne.love:
        $ hero.smartphone_contacts.append("dwayne")
        dwayne.say "You mean you don't have it already?"
        dwayne.say "Well we can soon take care of that."
        dwayne.say "Here you go, [hero.name]..."
    else:
        $ dwayne.love -= 1
        $ dwayne.sub -= 1
        dwayne.say "I can't do that, [hero.name]."
        dwayne.say "My number's only given out on a need to know basis."
        dwayne.say "Just call my secretary, and she'll pass on the message, okay?"
    return

label dwayne_ask_birthday_female:
    bree.say "Hey, Dwayne..."
    bree.say "I was wondering when your birthday is?"
    if hero.charm >= 40 - dwayne.love:
        $ dwayne.flags.birthdayknown = True
        dwayne.say "Normally I'd say call my secretary for stuff like that, [hero.name]."
        dwayne.say "But as it's you, I'm willing to make an exception!"
        dwayne.say "It's Summer 2."
    else:
        dwayne.say "Sorry, [hero.name] - that's sensitive information."
        dwayne.say "I can't have my competitors knowing stuff like that."
        dwayne.say "They could use it to ruin my carefully maintained image!"
        $ dwayne.sub -= 1
        $ dwayne.love -= 1
    return

label dwayne_offer_a_drink_female:
    bree.say "Time for another round!"
    bree.say "What are you having, Dwayne?"
    if (hero.charm >= 60 - dwayne.love and dwayne.flags.drinks < 2) or date_girl == dwayne:
        dwayne.say "You want to buy me a drink?"
        dwayne.say "Well okay, [hero.name] - as a modern guy, I'm good with that."
        dwayne.say "I'll have another one of these bad boys!"
        show drink dwayne
        if dwayne.love <= 25:
            $ dwayne.love += 1
        elif date_girl == dwayne and game.active_date:
            $ game.active_date.score += 5
        call expression dwayne.get_chat from _call_expression_390
        hide drink dwayne
        $ dwayne.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        dwayne.say "You want to buy me a drink?"
        dwayne.say "I don't think so, [hero.name]!"
        dwayne.say "I'm the one that buys the drinks around here!"
        $ hero.cancel_activity()
        hide dwayne
    return

label dwayne_slap_ass_intro_female:
    "Dwayne is passing by me, and I get a good look at his ass."
    "And by that I mean a damn fine look at his damn fine ass!"
    "Without thinking of the consequences, I pull back my arm."
    "And then I slap Dwayne squarely on the ass!"
    "The slap makes far more sound than I expected it would."
    return

label dwayne_slap_ass_happy_female:
    "Plus Dwayne stops and spins around on the spot."
    dwayne.say "Am I losing my mind here..."
    dwayne.say "Or did you just slap me on the ass, [hero.name]?"
    bree.say "Erm, yeah..."
    bree.say "I guess so!"
    "Dwayne smiles and points a finger at me."
    dwayne.say "That took some serious balls, [hero.name]."
    dwayne.say "And I respect you for it."
    "Dwayne adds a wink, just for good measure."
    return

label dwayne_slap_ass_angry_female:
    "Plus Dwayne stops and spins around on the spot."
    dwayne.say "Am I losing my mind here..."
    dwayne.say "Or did you just slap me on the ass, [hero.name]?"
    bree.say "Erm, yeah..."
    bree.say "I guess so!"
    "Dwayne frowns and shakes his head."
    dwayne.say "Don't ever touch me without my permission, [hero.name]!"
    dwayne.say "I've pressed charges on people for doing less."
    dwayne.say "Man or woman alike, it's all the same to me."
    return

label dwayne_breakup_female:
    bree.say "Urgh..."
    bree.say "I don't know how to say this, Dwayne!"
    dwayne.say "What are you talking about, [hero.name]?"
    dwayne.say "You can say anything to me!"
    "I nod and take a deep breath."
    bree.say "Okay, Dwayne..."
    bree.say "Here goes..."
    bree.say "I don't think this relationship is going anywhere."
    bree.say "And I want to break up with you!"
    if dwayne.love < 50:
        "Dwayne frowns and looks less than pleased with what he's hearing."
        "He shakes his head slowly."
        dwayne.say "You don't get to dump me, [hero.name]."
        dwayne.say "If this relationship is over, it's because I say it's over!"
        bree.say "What are you talking about, Dwayne?"
        bree.say "I'm the one that wants to break up with you!"
        "Dwayne holds up a hand to silence me."
        dwayne.say "Uh-uh, [hero.name]."
        dwayne.say "If you want to speak to me from now on, leave a message with my secretary."
        "With that, Dwayne turns on his heel and walks away."
        hide dwayne
        return "denied"
    "Dwayne frowns and looks less than pleased with what he's hearing."
    "But he still nods his head as he listens to me say my piece."
    dwayne.say "Okay, [hero.name], okay."
    dwayne.say "I don't agree with you, but I respect your position."
    dwayne.say "It takes a lot of guts to speak your mind."
    return

label dwayne_go_steady_intro_female:
    bree.say "We've been having some really great times on our dates recently, right?"
    bree.say "I mean, they've been the best that's happened to me in recent memory!"
    dwayne.say "Of course they have, [hero.name]."
    dwayne.say "And that's because you're dating me!"
    "Dwayne grins and points his thumbs to his beaming face."
    bree.say "Yeah, Dwayne..."
    bree.say "I guess..."
    bree.say "But I think we're getting on so well that we should make it official."
    bree.say "You know, like go steady?"
    return

label dwayne_go_steady_yes_female:
    dwayne.say "Huh...I thought we were doing that already?"
    dwayne.say "But why not, [hero.name]."
    dwayne.say "If it makes you happy, we're officially official."
    return

label dwayne_go_steady_no_female:
    dwayne.say "I don't think we need to do that, [hero.name]."
    dwayne.say "It's just another label, that's all."
    dwayne.say "Don't let society dictate everything in your life!"
    return

label dwayne_pet_intro_female:
    "I keep staring at Dwayne's head whenever he's not looking in my direction."
    "It's just so smooth and shiny, I can't take my eyes off it."
    "Eventually I can't help myself, I can't resist the temptation."
    "I stand up and reach out, patting the top of Dwayne's head."
    dwayne.say "So as I was saying..."
    dwayne.say "Wha...what the hell?!?"
    dwayne.say "[hero.name]...are you patting me on the head?"
    bree.say "Erm...yeah, Dwayne."
    bree.say "It's just so shiny!"
    bree.say "I couldn't help myself..."
    return

label dwayne_pet_happy_female:
    "I watch as Dwayne's face breaks into a huge smile."
    "He laughs and waves me away as though it's nothing."
    dwayne.say "Of course it is, [hero.name]."
    dwayne.say "I maintain a strict regime to maximise the health of my scalp."
    dwayne.say "You wouldn't believe how many people ask me to touch it!"
    return

label dwayne_pet_annoyed_female:
    "I watch as Dwayne's face darkens."
    "He shakes his head in disapproval."
    dwayne.say "I don't appreciate people drawing attention to my baldness, [hero.name]."
    dwayne.say "Premature baldness is a condition without a cure."
    dwayne.say "And as such deserves the same respect as any other medical condition!"
    return

label dwayne_massage_intro_female:
    dwayne.say "Argh..."
    dwayne.say "Son of a..."
    bree.say "Ooh, Dwayne..."
    bree.say "That looks painful!"
    "Dwayne shakes his head and offers me a smile."
    "Though he still looks to be in some serious pain."
    dwayne.say "What, this?"
    dwayne.say "No, [hero.name] - it's just an old twitch in the muscles, that's all."
    bree.say "You sure, Dwayne?"
    bree.say "Because I could always take a look at it for you?"
    bree.say "I give a pretty good massage..."
    return

label dwayne_massage_accept_female:
    "At the mention of me giving him a massage, Dwayne's interest increases."
    "He raises an eyebrow as he strokes his chin."
    dwayne.say "You know what, [hero.name]..."
    dwayne.say "That sounds like a great idea!"
    dwayne.say "Just let me take off my shirt..."
    return

label dwayne_massage_refuse_female:
    "Dwayne shakes his head and holds up a hand to ward me off."
    "And even as he does so, he winces from the pain a second time."
    dwayne.say "Ah...no, [hero.name]..."
    dwayne.say "I never put myself in the hands of an amateur."
    dwayne.say "That's a rule I won't break."
    return

label dwayne_piercing_nipples_reaction_female:
    "From the moment Dwayne comes striding up, I know he's got something to show off."
    "He's thrusting his chest out in front of him, like he wants the world to see it."
    dwayne.say "You see them, right, [hero.name]?"
    dwayne.say "You like them, right?"
    bree.say "Like what, Dwayne?"
    dwayne.say "My nipples of course!"
    dwayne.say "I just had them pierced!"
    "Now that I know what this is all about, I can see them clearly."
    "And they do look pretty hot!"
    bree.say "Oh yeah, Dwayne..."
    bree.say "They look really good!"
    return

label dwayne_piercing_navel_reaction_female:
    "From the moment Dwayne comes striding up, I know he's got something to show off."
    "He's thrusting his chest out in front of him, like he wants the world to see it."
    dwayne.say "You see it, right, [hero.name]?"
    dwayne.say "You like it, right?"
    bree.say "Like what, Dwayne?"
    dwayne.say "My navel of course!"
    dwayne.say "I just had it pierced!"
    "Now that I know what this is all about, I can see it clearly."
    "And it does look pretty hot!"
    bree.say "Oh yeah, Dwayne..."
    bree.say "It looks really good!"
    return

label dwayne_piercing_dick_reaction_female:
    "From the moment Dwayne comes striding up, I know he's got something to show off."
    "He's thrusting his chest out in front of him, like he wants the world to see it."
    dwayne.say "You see it, right, [hero.name]?"
    dwayne.say "You like it, right?"
    bree.say "Like what, Dwayne?"
    dwayne.say "My dick of course!"
    dwayne.say "I just had it pierced!"
    "Now that I know what this is all about, I can see it clearly."
    "And it does look pretty hot!"
    bree.say "Oh yeah, Dwayne..."
    bree.say "It looks really good!"
    return

label dwayne_piercing_tongue_reaction_female:
    "From the moment Dwayne comes striding up, I know he's got something to show off."
    "He's thrusting his chin out, like he wants the world to see it."
    dwayne.say "You see it, right, [hero.name]?"
    dwayne.say "You like it, right?"
    bree.say "Like what, Dwayne?"
    dwayne.say "My tongue of course!"
    dwayne.say "I just had it pierced!"
    "Dwayne opens his mouth and sticks out his tongue."
    "Now that I know what this is all about, I can see it clearly."
    "And it does look pretty hot!"
    bree.say "Oh yeah, Dwayne..."
    bree.say "It looks really good!"
    return

label dwayne_movie_liked_reaction_female:
    bree.say "That was a great movie, Dwayne."
    bree.say "I was on the edge of my seat the whole time!"
    "Dwayne nods his head as I gush about the film we just saw."
    dwayne.say "It was something else, [hero.name]."
    dwayne.say "Great acting, great story, great movie!"
    return

label dwayne_movie_indifferent_reaction_female:
    bree.say "That was a great movie, Dwayne."
    bree.say "I was on the edge of my seat the whole time!"
    "Dwayne looks less than impressed, shaking his head."
    dwayne.say "It wasn't bad, [hero.name]."
    dwayne.say "But it wasn't that good either."
    dwayne.say "We should watch stuff like that in my home cinema!"
    return

label dwayne_movie_disliked_reaction_female:
    bree.say "That was a great movie, Dwayne."
    bree.say "I was on the edge of my seat the whole time!"
    "Dwayne shakes his head as I keep on gushing about the film."
    dwayne.say "Were we watching different movies, [hero.name]?"
    dwayne.say "That was awful from start to finish!"
    dwayne.say "Complete garbage!"
    return

label dwayne_abortion_reaction_female:
    "I have the strangest feeling that I'm being watched."
    "So much so that I look up to see if I'm right."
    "And I find myself looking straight into Dwayne's face."
    "Just in time to see him raise that damn eyebrow at me."
    bree.say "Erm..."
    bree.say "Hey, Dwayne!"
    bree.say "Is there something I can help you with?"
    dwayne.say "Don't play the innocent with me, [hero.name]."
    dwayne.say "I'm not the kind of guy you're used to dealing with."
    bree.say "You're not?"
    dwayne.say "You know what I mean, [hero.name]."
    dwayne.say "The kind of guy that wouldn't have noticed you were pregnant in the first place."
    dwayne.say "And so would have no chance in hell of noticing that you're now not pregnant."
    "I force a nervous smile onto my face."
    "And I decide that I have to nod in agreement."
    "Because it's pretty obvious that he's onto me."
    bree.say "Ah..."
    bree.say "About that..."
    bree.say "I was going to tell you - when the time was right!"
    if (dwayne.flags.know_is_father and dwayne.love >= 150) or dwayne.love <= 150:
        "Dwayne's mouth twists into a frown."
        "And he shakes his head slowly."
        dwayne.say "The right time would have been BEFORE you did it, [hero.name]."
        dwayne.say "Not afterwards when you'd made all the calls yourself."
        "I can feel Dwayne's words cutting me like a knife."
        "And the guilt is already beginning to twist my gut."
        "But I still feel like I have to stand up for myself."
        bree.say "This is my body, Dwayne!"
        bree.say "So it was always going to be my decision."
        bree.say "And I won't be made to feel like a criminal!"
        dwayne.say "All I hear is me, me, me!"
        dwayne.say "You talk about your rights, [hero.name]."
        dwayne.say "But you don't seem to give a damn about anybody else's rights!"
        "I make to argue the point, but I find that I can't."
        "Dwayne's struck a blow that leaves me speechless."
        "So he's free to turn on his heel and walk away."
        "Leaving me alone with only my guilty thoughts for company."
    else:
        "I watch the stern and serious expression fade from Dwayne's face."
        "And then it actually becomes sympathetic and knowing."
        dwayne.say "That must have been a hard thing to do, [hero.name]."
        dwayne.say "But it was probably for the best."
        bree.say "You..."
        bree.say "You really mean that, Dwayne?"
        "Dwayne nods slowly."
        dwayne.say "You're not a monster, [hero.name]."
        dwayne.say "And you wouldn't have done it lightly."
        dwayne.say "Actually I think it was a pretty brave thing to do."
        "I can't describe how good it feels to hear him say that."
        "The relief that comes from having someone understand."
        bree.say "Thank you, Dwayne."
        bree.say "That means a lot."
        "Dwayne doesn't say a thing in response."
        "He just nods and smiles, like he knows that's enough."
    return


label dwayne_belly_interaction_female:
    $ dwayne.set_flag("interact", 1, 1, "+")
    show dwayne at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call dwayne_belly_kiss_female from _call_dwayne_belly_kiss_female_1
        "Caress my belly":
            call dwayne_belly_caress_female from _call_dwayne_belly_caress_female_1
        "Listen to the baby":
            call dwayne_belly_listen_female from _call_dwayne_belly_listen_female_1
        "Never mind":
            pass
    return

label dwayne_belly_caress_female:
    show dwayne happy at center, zoomAt(1.5, (640, 1040))
    dwayne.say "Well hello there, beautiful..."
    dwayne.say "How's the most gorgeous person in my life doing today?"
    show dwayne normal
    "I'm totally unprepared for Dwayne striding up to me out of nowhere."
    with vpunch
    "And the sound of his booming voice is more than enough to make me jump."
    "So with both hands on my bump, I literally leap forward a few feet."
    bree.say "Whoa..."
    bree.say "Dwayne..."
    bree.say "You scared the life out of me!"
    "I take a breath and do the best I can to get myself back under control."
    bree.say "But thanks for the compliment."
    bree.say "That was very sweet of you!"
    "It's only now that I notice Dwayne's not actually looking in my direction."
    "Instead he's gazing down at my belly, eyes fixated on the curve of it."
    "And he has a hand placed on it too, gently caressing the shape."
    show dwayne shout
    dwayne.say "Huh?"
    dwayne.say "Did you say something, [hero.name]?"
    show dwayne happy
    dwayne.say "I was totally tied up in praising my unborn child here!"
    show dwayne normal
    "I blink a couple of times as realisation begins to set in."
    "All of those gushing compliments and sweet words weren't meant for me."
    "Dwayne was totally fixated on the baby in my belly!"
    "I can already feel my cheeks starting to flush red from embarrassment."
    "And part of me wishes that the ground would open and swallow me up."
    "At least that way I could hide how stupid I feel right now."
    "Luckily for me it seems that Dwayne's non the wiser himself."
    "So I force a smile onto my face and shake my head."
    bree.say "Oh no, it was nothing at all..."
    bree.say "No need to worry about it, Dwayne!"
    show dwayne smile
    "This seems to be more than enough to satisfy Dwayne."
    "As he nods and then turns his attention back to my belly."
    "Well, he turns his attention to the baby that's growing inside of it."
    "Which leaves me to ponder how all of that just made me feel."
    "I mean, am I really getting jealous of the attention Dwayne's giving our baby?"
    "The thought kind of worries me a little, making me concerned for the future."
    "What if I start to resent the kid, to crave the attention that they'll be getting?"
    "Urgh...why does everything have to be so darn complicated?"
    $ dwayne.love += 2
    return

label dwayne_belly_kiss_female:
    show dwayne normal at center, zoomAt(1.5, (640, 1040))
    "Dwayne surprises me by stepping up and wrapping his arms around my waist."
    hide dwayne
    show dwayne kiss
    with fade
    "Then he pulls me closer so that he can lean in and plant a kiss on my lips."
    "It's unexpected, but incredibly welcome, so I don't hesitate to return the gesture."
    "And even when it comes to a natural end, I keep a hold of him for a little longer."
    hide dwayne
    show dwayne normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Which is when he seems to notice the presence of my belly between us."
    bree.say "Oops..."
    bree.say "I guess we can't get as close as we used to!"
    show dwayne smile
    "Dwayne shakes his head, giving me one of those incredible smiles of his."
    "The kind that make his teeth look like slabs of pure alabaster."
    show dwayne happy
    dwayne.say "It's no problem, [hero.name]..."
    dwayne.say "We just need to make room for a new addition, that's all."
    show dwayne smile
    "As if to prove his point, Dwayne lets me go."
    show dwayne at center, zoomAt(1.5, (640, 1240)) with ease
    "And then he sinks down onto one knee."
    "I watch him with interest as he lifts up my top."
    "Of course this reveals the curve of my belly."
    show dwayne at center, traveling(2.5, 0.3, (640, 1940))
    "And Dwayne leans in to plant a kiss on it."
    "I can feel it in pretty much the same way as the one on my lips."
    "The gentle sensation of his own lips, caressing my sensitive skin."
    "But unlike the first kiss, this one seems to be going on and on."
    "Dwayne moves slowly over my belly, paying attention to every spot he touches."
    "And the more he kisses, the more I can feel the warmth growing inside of me."
    "I don't want him to stop, but I also don't want to say a single word."
    "Because I'm afraid that doing so would break the spell and spoil the moment."
    "So instead I do the best I can to keep quiet the whole time."
    "Which means that pretty soon I'm biting my lip as I struggle to contain myself."
    "The kisses that Dwayne's laying on me just feel so damn good."
    "I want to ask him to keep on going, to kiss me in other places too."
    "But I keep a firm hold on myself and press my lips together."
    "All the time feeling like I'm no more than a few seconds away from exploding."
    "And I have no idea if Dwayne even knows what he's doing to me right now."
    "Because my silence also means that he's left in blissful ignorance."
    $ dwayne.love += 3
    return

label dwayne_belly_listen_female:
    show dwayne shout at center, zoomAt(1.5, (640, 1040))
    dwayne.say "Hey, [hero.name]..."
    dwayne.say "What's going on in that belly of yours?"
    dwayne.say "The baby looks like they're doing flips and somersaults!"
    show danny smile
    "I'm already holding my belly in both hands when Dwayne asks the question."
    "Because nobody knows better than I do what's going on in there right now."
    bree.say "Urgh..."
    bree.say "They're just extra lively today, Dwayne."
    bree.say "It happens sometimes, and you never know the reason."
    "Dwayne nods at my answer."
    "But I can see that he's not satisfied with it."
    "Because he keeps on staring at my belly the whole time."
    dwayne.say "Hmm..."
    show dwayne shout
    dwayne.say "Do you mind if I..."
    show dwayne normal
    "Dwayne kind of points at my belly, still pretty distracted."
    "I shrug and hold up my hands."
    bree.say "Sure, Dwayne..."
    bree.say "Help yourself."
    "My permission seems to be beside the point."
    show dwayne at center, zoomAt(1.5, (640, 1240)) with ease
    "As Dwayne's already leaning in to listen to my belly as I grant it."
    "And most of his attention seems to be on the task itself, rather than me."
    "So I resign myself to staring down over the curve of my belly."
    show dwayne at center, traveling(2.5, 0.3, (640, 1940))
    "I watch as he presses his ear against it, listening intently."
    "And I follow him as he moves here and there, chasing the sounds."
    bree.say "So..."
    bree.say "What's going on down there, Dwayne?"
    bree.say "Can you hear anything?"
    dwayne.say "Hmm..."
    show dwayne shout
    dwayne.say "It's hard to be specific, [hero.name]."
    dwayne.say "I can hear a lot of things right now."
    dwayne.say "But it's hard to be sure of just what they are."
    show dwayne normal
    "I keep on nodding as Dwayne explains himself to me."
    "All the time hoping that he's going to be more specific."
    show dwayne happy
    dwayne.say "The best I can really say is that I can probably hear the baby."
    dwayne.say "Because some of the sounds must be coming from them."
    dwayne.say "But someone swimming underwater in another room is the best you're going to get!"
    show danny smile
    "I let out a frustrated sigh and nod my head, because Dwayne's right."
    "That really is the best I'm going to get."
    $ dwayne.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
