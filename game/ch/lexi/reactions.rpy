label lexi_ice_cream_reaction_male:
    mike.say "Geez, it's just too damn hot today - we should grab some ice cream!"
    lexi.say "Now you're talking - let's go get some right now!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "lexi chooses a colourful ice lolly, striped and glistening in the sun."
    mike.say "I can't eat those things, Lexi - they give me brain-freeze!"
    lexi.say "Not me - I frickin love 'em!"
    "I'm about to say more when I see the way Lexi's licking it."
    "And the words just die in my throat as I look on in silence."
    "Lexi goes to work on the ice lolly as if her life depended on it."
    "I just know she's doing it on purpose, and loving the fact that I'm watching her too!"
    return

label lexi_ask_phone_male:
    mike.say "Can I get your number, Lexi?"
    mike.say "I'd really like to call you some time!"
    if hero.charm >= 20 - lexi.love:
        show lexi happy
        $ hero.smartphone_contacts.append("lexi")
        lexi.say "Sure thing, [hero.name]!"
        lexi.say "You can have your own Lexi Hotline!"
        lexi.say "And I can get some juicy dick pics..."
    else:
        show lexi annoyed
        $ lexi.love -= 1
        $ lexi.sub -= 1
        lexi.say "Nah, not my private number, [hero.name]."
        lexi.say "I need that for running my business!"
    return

label lexi_ask_birthday_male:
    mike.say "Your birthday, Lexi."
    mike.say "You never told me when it was!"
    if hero.charm >= 40 - lexi.love:
        show lexi happy
        $ lexi.flags.birthdayknown = True
        lexi.say "Ah, I party whatever the date is, [hero.name]!"
        lexi.say "But just for the record, it's Summer 5."
    else:
        show lexi annoyed
        $ lexi.sub -= 1
        $ lexi.love -= 1
        lexi.say "Hey?!?"
        lexi.say "What are you getting at?"
        lexi.say "I live hard and I play hard too."
        lexi.say "And that can take it's toll on a girl!"
    return

label lexi_offer_a_drink_male:
    mike.say "Hey!"
    mike.say "Lexi!"
    mike.say "Beer?"
    "Almost the second the words are out of my mouth, Lexi turns to face me."
    if lexi.is_visibly_pregnant:
        show lexi angry
        $ lexi.love -= 10
        lexi.say "Hey, my mom drank while she was having me."
        lexi.say "And some people said it made me turn out bad!"
        lexi.say "I want things to be different for our kid."
        $ hero.cancel_activity()
        hide lexi
    elif (hero.charm >= 60 - lexi.love and lexi.flags.drinks < 2) or date_girl == lexi:
        show lexi happy
        lexi.say "You sure know how to treat a lady, [hero.name]!"
        lexi.say "Toss one my way, yeah?"
        hide lexi
        show drink lexi
        if lexi.love <= 25:
            $ lexi.love += 1
        elif date_girl == lexi and game.active_date:
            $ game.active_date.score += 5
        call expression lexi.get_chat from _call_expression_252
        hide drink lexi
        $ lexi.set_flag("drinks", 1, "day", mod="+")
    else:
        show lexi annoyed
        lexi.say "Oh no - no way!"
        lexi.say "I've had my drink spiked WAY too many times to fall for that!"
        $ hero.cancel_activity()
        hide lexi
    return

label lexi_slap_ass_intro_male:
    "It's not just that Lexi has an incredibly hot body."
    "She also walks in a way that shows it all off too."
    "Every part of her moves in a way that attracts my eye."
    "But her ass in particular - that's what fascinates me."
    "I just can't resist the urge to slap it..."
    return

label lexi_slap_ass_happy_male:
    lexi.say "Whoa..."
    lexi.say "Who's touching the merchandise?!?"
    lexi.say "[hero.name], was that you?"
    "There's no point denying it."
    "So I just shrug and then nod."
    lexi.say "Well, I can't say I blame you."
    lexi.say "Just make it a little harder next time, okay?"
    lexi.say "A girl likes it nice and hard..."
    return

label lexi_slap_ass_angry_male:
    lexi.say "Whoa..."
    lexi.say "Who's touching the merchandise?!?"
    lexi.say "[hero.name], was that you?"
    "There's no point denying it."
    "So I just shrug and then nod."
    lexi.say "Well don't do it again, yeah?"
    lexi.say "I don't want people thinking I'm spoken for."
    lexi.say "A girl's got to make a living..."
    return

label lexi_breakup_male:
    show lexi
    "This should be an easy task, right?"
    "I mean Lexi's not the kind of girl that's shy about things."
    "And she's made a living out of being free with her body too."
    "So she shouldn't be too thrown by the fact that I want to break up with her."
    "She's surely going to take it all in her stride..."
    mike.say "Hey, Lexi..."
    mike.say "I was just thinking..."
    mike.say "Maybe we should call it quits, you know?"
    "Lexi stops dead in her tracks."
    "Her jaw drops open."
    "And she looks at me with a shocked expression on her face."
    show lexi annoyed
    lexi.say "Y...you're just dropping this on me now, [hero.name]?"
    lexi.say "Telling me something like that out of the blue?"
    lexi.say "You sound so casual too - like it's no big deal!"
    "I'm more than a little taken aback by Lexi's reaction."
    "She seems genuinely upset, offended even!"
    mike.say "I...I don't get it, Lexi."
    mike.say "I thought you'd be cool with it."
    mike.say "I mean...in your line of work..."
    "I see anger flare suddenly in Lexi's eyes."
    "And I know that I've misjudged the situation badly."
    "Lexi plants her hands on her hips, almost squaring up to me."
    show lexi angry
    lexi.say "Why don't you just come out and say it, [hero.name]?"
    lexi.say "You think I'm just some cheap-ass whore, don't you?"
    lexi.say "And that means you can fuck me while it's fun."
    lexi.say "Then toss me aside when you've gotten bored!"
    mike.say "No, Lexi!"
    mike.say "It's not like that!"
    mike.say "I just thought you were more laid back!"
    lexi.say "You think that I am what I do for money, [hero.name]?"
    lexi.say "I'm a human being, and I have real feelings."
    lexi.say "I thought you got that, I really did!"
    lexi.say "But you're no different to Danny."
    lexi.say "You see the same thing he did when you look at me."
    lexi.say "All you see is a pair of tits and a pussy."
    lexi.say "And you ain't gonna be seeing any of me anymore!"
    return

label lexi_go_steady_intro_male:
    mike.say "I'm having a great time with you, Lexi."
    mike.say "So great that I think we should it further."
    mike.say "I think we should make this thing exclusive."
    return

label lexi_go_steady_yes_male:
    lexi.say "Normally I'd say you could go fuck yourself, [hero.name]."
    lexi.say "But with you...I dunno...it's kind of different."
    lexi.say "I think I'd actually like that!"
    hide lexi
    show lexi kiss
    $ lexi.flags.kiss += 1
    "Lexi underlines her point by pulling me into a kiss."
    "A hot, heavy and dirty kiss that tells me all I need to know!"
    return

label lexi_go_steady_no_male:
    lexi.say "You can go fuck yourself, [hero.name]!"
    lexi.say "We're doing pretty great, you and me."
    lexi.say "But we're not there yet!"
    return

label lexi_pet_intro_male:
    "I pat Lexi on the head even before I truly realise I'm doing it."
    "And the truth is that I don't know why I'm doing it at all."
    "It's not like I do it all the time, or that I know how she'll take it!"
    return

label lexi_pet_happy_male:
    lexi.say "Aw..."
    lexi.say "That's kind of sweet, [hero.name]."
    lexi.say "Like I'm you little pet bitch or something!"
    return

label lexi_pet_annoyed_male:
    lexi.say "Ah...what's that about, [hero.name]?"
    lexi.say "You trying to tell me I'm your bitch?"
    lexi.say "That you want to treat me like a dog?"
    return

label lexi_massage_intro_male:
    mike.say "Jesus Christ, Lexi!"
    mike.say "Did you pull a muscle or something?"
    mike.say "I can give you a massage if you did."
    return

label lexi_massage_accept_male:
    lexi.say "Ah..."
    lexi.say "I dunno how I did it, [hero.name]."
    lexi.say "But that sounds like a great offer."
    lexi.say "And don't bother being gentle either!"
    return

label lexi_massage_refuse_male:
    lexi.say "Ah..."
    lexi.say "Fuck sake, [hero.name]!"
    lexi.say "Can't you keep your hands off of me just this once?"
    lexi.say "I don't want anyone touching me right now!"
    return

label lexi_piercing_nipples_reaction_male:
    lexi.say "Ooh...oh...wow!"
    lexi.say "I can feel it whenever they move!"
    lexi.say "I don't know why I waited so long to get my nipples pierced!"
    return

label lexi_piercing_navel_reaction_male:
    lexi.say "Oh god, I'm such a scatter-brain, [hero.name]!"
    lexi.say "I actually thought I already had my belly-button pierced!"
    lexi.say "Can you believe that?!?"
    return

label lexi_piercing_clit_reaction_male:
    lexi.say "Oooh...I like the way it feels, [hero.name]!"
    lexi.say "Like it's reminding me I have a pussy all the time!"
    lexi.say "It makes me feel SO sexy..."
    return

label lexi_piercing_head_reaction_male:
    lexi.say "Oh yeah - why did I wait so long to do this, [hero.name]?"
    lexi.say "It feels so good when I roll my tongue!"
    lexi.say "Imagine how it's going to feel when I give you a BJ!"
    return

label lexi_piercing_nose_reaction_male:
    lexi.say "I love it, [hero.name]!"
    lexi.say "Maybe I should get even more piercings!"
    lexi.say "If I can just think where to put them..."
    return

label lexi_movie_disliked_reaction_male:
    lexi.say "Urgh...that was awful - we should have fooled around in there instead!"
    return

label lexi_movie_indifferent_reaction_male:
    lexi.say "I was bored stiff - that film really put me to sleep!"
    return

label lexi_movie_liked_reaction_male:
    lexi.say "I could watch that shit all over again -right now!"
    return

label lexi_belly_kiss_male:
    show lexi normal at center, zoomAt(1.25, (640, 880))
    lexi.say "Ha!"
    lexi.say "Gut barge!"
    show lexi a smile at center, traveling(1.5, 0.3, (640, 1040))
    mike.say "What the..."
    with hpunch
    "Before I can even get a handle on what's happening, Lexi collides with me."
    "Not hard enough to send me flying or even move me as much as a couple of inches."
    "In truth, all she really does it push herself against me a little for effect."
    show lexi bored
    lexi.say "Hey, no fair!"
    lexi.say "What's the point in having a big belly if I can't use it like a sumo wrestler?"
    show lexi smile
    mike.say "Well there is a difference, Lexi."
    mike.say "For one thing, a sumo wrestler's not pregnant when they do that!"
    with hpunch
    "Lexi pushes her belly against me again."
    "But I see that this time she's kind of pouting too."
    show lexi bored
    lexi.say "Urgh..."
    lexi.say "Damn it..."
    show lexi sadsmile
    lexi.say "I'm so fat that I can't even reach you for a kiss!"
    show lexi sad
    mike.say "No worries, Lexi."
    mike.say "I know a way around that."
    show lexi a at center, traveling(2.0, 1.0, (640, 980))
    "Putting both hands on Lexi's belly, I bend over."
    "And then I plant a kiss on the curve of it."
    show lexi a surprised
    lexi.say "Ooh..."
    lexi.say "That tickles..."
    lexi.say "Do it again!"
    show lexi a smile
    "I do as I'm told, planting more kisses on Lexi's belly."
    "All the time I'm doing so, I can hear the sound of her giggling with delight."
    "It's a joyful sound, one that can't help but lift my spirits too."
    show lexi a flirt
    lexi.say "Oh man..."
    lexi.say "I thought that being pregnant would totally kill my sex-drive."
    lexi.say "But you're making me feel so damn horny right now!"
    return

label lexi_belly_caress_male:
    show lexi normal at center, zoomAt(1.25, (640, 880))
    "It's not like I didn't get to see a lot of Lexi's belly before she was pregnant."
    "She was always wandering around in cropped tops that showed it off to the world."
    "And now that she's swelling up like a balloon in that department, nothing's changed."
    "Lexi spends most of the time with her belly bared for all to see."
    "Which means I'm spending more time than ever staring at it."
    show lexi flirt
    lexi.say "Admiring your handiwork, huh?"
    lexi.say "Checking out what you did to my formerly hot body?"
    show lexi smile
    "Lexi has her hands crossed over the top of her belly."
    show lexi a at center, traveling(1.5, 0.3, (640, 1040))
    "And she's pretty much thrusting it towards me."
    "But I can tell from the tone of her voice that she's not for real."
    "So I don't hesitate to put both my hands on her bump."
    "And then I make a point of caressing it fondly."
    mike.say "Pretty much, Lexi."
    mike.say "And I think I made a pretty good job of it too!"
    show lexi happy
    "Lexi shoots me a look of mock-outrage."
    "But at the same time I note that she's beginning to lean against me."
    "And within no more than a few seconds, her arms are wrapped around me too."
    "I feel the weight of her head as she places it on my shoulder."
    "But I just keep on caressing the curve of her belly."
    "Because I'm enjoying all of these sensations far too much to even think of moving."
    return

label lexi_belly_listen_male:
    show lexi a smile at center, zoomAt(1.25, (640, 880))
    pause 0.1
    show lexi a at center, traveling(2.0, 1.0, (640, 980))
    mike.say "Keep still, Lexi..."
    mike.say "I won't hear anything at this rate!"
    "I have my ear pressed to the curve of Lexi's stomach."
    "And I'm determined to make her sit still and keep quiet."
    "Because I want to find out if I can hear the baby moving in there."
    show lexi a bored
    lexi.say "This is a dumb idea, [hero.name]."
    lexi.say "They needed all that high-tech stuff to do it in the hospital."
    lexi.say "So how are you gonna be able to do it with just your ear?"
    show lexi a annoyed
    "I do the best I can to ignore Lexi as I strain to hear anything."
    "And I wave a hand vaguely in the air in an effort to shut her up too."
    "But a moment later I'm rewarded with the sound of something against my ear."
    "So both of my hands are holding onto the belly, trying to hold it still."
    show lexi a smile
    mike.say "There..."
    mike.say "There it is..."
    mike.say "Like the sound of someone swimming around in there!"
    show lexi a surprised
    lexi.say "You're shitting me?!?"
    lexi.say "Move over - I want to hear it too!"
    show lexi a smile
    mike.say "Lexi, how are you going to listen to your own belly?"
    mike.say "It'd be like me..."
    mike.say "I don't know..."
    mike.say "Giving myself a blow-job or something!"
    show lexi a annoyed
    "Lexi lets out a sulky, muttering sound at this."
    show lexi a bored
    lexi.say "Humph..."
    lexi.say "It's not so hard."
    show lexi a wink
    lexi.say "I once knew a guy who could do that!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
