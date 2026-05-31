label ayesha_ice_cream_reaction_female:
    bree.say "Phew..."
    bree.say "It's TOO hot today, Ayesha!"
    bree.say "We should go grab an ice-cream to cool down."
    "Ayesha nods as she wipes her forehead."
    ayesha.say "Yeah, [hero.name]..."
    ayesha.say "An ice-cream sounds like a really good idea!"
    "Ayesha and I hurry over to the ice-cream stand and order for ourselves."
    "But it's pretty clear that we're both eyeing up the other's choice of ice-cream."
    bree.say "Ayesha..."
    ayesha.say "Yeah, [hero.name]?"
    bree.say "You can lick mine if I can lick yours, deal?"
    "Ayesha can't help snickering at the way I put the question."
    "But all the same, she nods and holds out her ice-cream."
    "I do the same, and we're soon sampling each other's choice."
    bree.say "Mmm!"
    bree.say "That's really good, Ayesha!"
    ayesha.say "Your's isn't too shabby either, [hero.name]!"
    "We keep on swapping licks as we walk away from the stand."
    "Seems like Ayesha and I both have good taste when it comes to ice-cream."
    return

label ayesha_ask_phone_female:
    bree.say "I was going to give you a call the other day, Ayesha."
    bree.say "But then I realised that I don't have your number!"
    bree.say "You want to let me have it now?"
    if hero.charm >= 20 - ayesha.love:
        $ hero.smartphone_contacts.append("ayesha")
        ayesha.say "Sure, [hero.name] - you can't keep asking [mike.name] to call me for you!"
        ayesha.say "In fact, let me have yours first."
        ayesha.say "Then I'll send you a text message so you have the number, okay?"
    else:
        $ ayesha.love -= 1
        $ ayesha.sub -= 1
        ayesha.say "No, [hero.name]..."
        ayesha.say "I like to keep my number private."
        ayesha.say "Just ask [mike.name] to drop me a line in future, yeah?"
    return

label ayesha_ask_birthday_female:
    bree.say "Ayesha, I was meaning to ask..."
    bree.say "When is your birthday?"
    bree.say "Because, well...I wouldn't want to forget it!"
    if hero.charm >= 40 - ayesha.love:
        $ ayesha.flags.birthdayknown = True
        ayesha.say "Oh sure, [hero.name]..."
        ayesha.say "It's Winter 29, just so you know."
    else:
        ayesha.say "Hmm...I don't think so, [hero.name]."
        ayesha.say "If I didn't tell you already, then I'm not ready to have you know!"
        $ ayesha.sub -= 1
        $ ayesha.love -= 1
    return

label ayesha_offer_a_drink_female:
    bree.say "I'm gonna grab another drink."
    bree.say "Are you ready for one too, Ayesha?"
    if (hero.charm >= 60 - ayesha.love and ayesha.flags.drinks < 2) or date_girl == ayesha:
        ayesha.say "Oh yeah..."
        ayesha.say "Looks like I'm done with this one too!"
        ayesha.say "Okay, [hero.name] - get me another one of these."
        show drink ayesha
        if ayesha.love <= 25:
            $ ayesha.love += 1
        elif date_girl == ayesha and game.active_date:
            $ game.active_date.score += 5
        call expression ayesha.get_chat from _call_expression_389
        hide drink ayesha
        $ ayesha.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        ayesha.say "I'd rather not, [hero.name]."
        ayesha.say "I'm in training for a match."
        ayesha.say "So I've got to be careful what I put in my body right now."
        $ hero.cancel_activity()
        hide ayesha
    return

label ayesha_slap_ass_intro_female:
    "I don't think I've ever seen an ass like Ayesha's on a girl before."
    "Only on guys, and even then just the ones that are real beefcakes!"
    "And maybe that's why I don't hesitate to slap it as she walks past."
    "Because most guys actually like it when I do that to them, you know?"
    "But the moment my hand makes contact, Ayesha stops dead in her tracks!"
    return

label ayesha_slap_ass_happy_female:
    ayesha.say "[hero.name]!"
    ayesha.say "Did you just slap my ass?!?"
    bree.say "Erm..."
    bree.say "Yeah, Ayesha - I kinda did!"
    "Ayesha gives me a rueful grin and shakes her head."
    ayesha.say "You'd better know what you're getting into before you do that again, girl!"
    ayesha.say "Or it'll be me spanking YOUR booty!"
    return

label ayesha_slap_ass_angry_female:
    ayesha.say "[hero.name]!"
    ayesha.say "Did you just slap my ass?!?"
    bree.say "Erm..."
    bree.say "Yeah, Ayesha - I kinda did!"
    "Ayesha shakes her head, clearly not happy with me."
    ayesha.say "Geez, [hero.name]..."
    ayesha.say "You're as bad as a guy!"
    ayesha.say "Keep your hands to yourself in future, okay?"
    return

label ayesha_breakup_female:
    bree.say "I don't know how to say this, Ayesha..."
    bree.say "But I think we need to spend some time apart."
    "Ayesha looks at me with surprise."
    "But then she nods and shakes her head."
    ayesha.say "Don't worry, [hero.name]..."
    ayesha.say "I've been here before - more times than I can count."
    ayesha.say "I know when something's not working out."
    ayesha.say "Let's just end it here and now, while we still have some fond memories left."
    return

label ayesha_go_steady_intro_female:
    bree.say "We've been on what, a couple of dates now, Ayesha?"
    ayesha.say "Yeah, [hero.name]..."
    ayesha.say "And your point is?"
    bree.say "Well..."
    bree.say "I think they were pretty good dates."
    ayesha.say "Me too, [hero.name]."
    bree.say "So I was thinking..."
    bree.say "Are we like an item now, Ayesha?"
    bree.say "Like officially a thing?"
    return

label ayesha_go_steady_yes_female:
    ayesha.say "Erm..."
    ayesha.say "I didn't know we had to make it official, [hero.name]!"
    ayesha.say "But yeah, I think we're an item."
    return

label ayesha_go_steady_no_female:
    ayesha.say "Hmm..."
    ayesha.say "I don't think so, [hero.name]."
    ayesha.say "I mean, I like you and we have a lot of fun."
    ayesha.say "But I don't think we're quite there yet."
    return

label ayesha_pet_intro_female:
    "The more time I spend around Ayesha, the more I realise how tall she actually is."
    "I mean, she towers over me, more than any other girl I ever met!"
    "So when she kneels down beside me, I'm surprised to see the top of her head."
    "There's nothing strange about it, apart from the fact I've never seen it before."
    "And so I get the sudden urge to reach out and touch it..."
    ayesha.say "HEY!"
    ayesha.say "[hero.name]..."
    ayesha.say "Did you just pat me on the head?!?"
    bree.say "Erm...yeah..."
    bree.say "I guess I did!"
    return

label ayesha_pet_happy_female:
    ayesha.say "Okay, okay..."
    ayesha.say "I know how tall I am, [hero.name]."
    ayesha.say "But you've done it now."
    ayesha.say "So you can get over it, yeah?"
    return

label ayesha_pet_annoyed_female:
    ayesha.say "Yeah, well..."
    ayesha.say "You'd better no do it again."
    ayesha.say "And I mean it!"
    return

label ayesha_massage_intro_female:
    ayesha.say "Aah..."
    ayesha.say "Damn it!"
    "Ayesha flinches and then holds her side."
    bree.say "Ayesha..."
    bree.say "Are you okay?"
    ayesha.say "Yeah, yeah..."
    ayesha.say "I just pulled something in my last match, that's all."
    ayesha.say "I'll work it out at the gym tomorrow."
    bree.say "Really?"
    bree.say "Because I took a course in massage last semester."
    bree.say "Want me to take a look at it for you?"
    return

label ayesha_massage_accept_female:
    ayesha.say "Why not, [hero.name]."
    ayesha.say "I mean, it's not like you could make it worse!"
    return

label ayesha_massage_refuse_female:
    ayesha.say "Nah, it's okay, [hero.name]."
    ayesha.say "I appreciate the offer."
    ayesha.say "But I want to have a professional take a look."
    return

label ayesha_piercing_nipples_reaction_female:
    "I can see that Ayesha looks a little uncomfortable."
    "It's like she's trying to hide something and not doing a good job!"
    bree.say "Are you okay, Ayesha?"
    ayesha.say "It's...it's my damn nipples, [hero.name]!"
    bree.say "Your nipples?"
    ayesha.say "Yeah, my nipples - I had them pierced!"
    bree.say "WOW!"
    bree.say "Ayesha...that's...so hot!"
    "Ayesha looks at me in surprise for a moment."
    "But then I see her begin to smile."
    ayesha.say "You really think so?"
    ayesha.say "Maybe this wasn't such a bad idea after all!"
    return

label ayesha_piercing_navel_reaction_female:
    "I can see that Ayesha looks a little uncomfortable."
    "It's like she's trying to hide something and not doing a good job!"
    bree.say "Are you okay, Ayesha?"
    ayesha.say "It's...it's my damn navel, [hero.name]!"
    bree.say "Your navel?"
    bree.say "Oh...you mean your belly-button?"
    ayesha.say "Yeah - I had it pierced!"
    bree.say "WOW!"
    bree.say "Ayesha...that's...so hot!"
    "Ayesha looks at me in surprise for a moment."
    "But then I see her begin to smile."
    ayesha.say "You really think so?"
    ayesha.say "Maybe this wasn't such a bad idea after all!"
    return

label ayesha_piercing_clit_reaction_female:
    "I can see that Ayesha looks a little uncomfortable."
    "It's like she's trying to hide something and not doing a good job!"
    bree.say "Are you okay, Ayesha?"
    ayesha.say "It's...it's my damn clit, [hero.name]!"
    bree.say "Your clit?"
    bree.say "Oh...oh...I see!"
    ayesha.say "Yeah - I had it pierced!"
    bree.say "WOW!"
    bree.say "Ayesha...that's...so hot!"
    "Ayesha looks at me in surprise for a moment."
    "But then I see her begin to smile."
    ayesha.say "You really think so?"
    ayesha.say "Maybe this wasn't such a bad idea after all!"
    return

label ayesha_piercing_tongue_reaction_female:
    "I can see that Ayesha looks a little uncomfortable."
    "It's like she's trying to hide something and not doing a good job!"
    bree.say "Are you okay, Ayesha?"
    ayesha.say "It's...it's my damn tongue, [hero.name]!"
    bree.say "Your tongue?"
    "Ayesha sticks out her tongue to show me what she means."
    bree.say "Oh...oh...I see!"
    ayesha.say "Yeah - I had it pierced!"
    bree.say "WOW!"
    bree.say "Ayesha...that's...so hot!"
    "Ayesha looks at me in surprise for a moment."
    "But then I see her begin to smile."
    ayesha.say "You really think so?"
    ayesha.say "Maybe this wasn't such a bad idea after all!"
    return

label ayesha_movie_liked_reaction_female:
    bree.say "Normally I don't like that kind of movie, Ayesha."
    bree.say "But somehow I just found myself getting into this one."
    bree.say "I feel really weird now that we're out of there."
    bree.say "I was totally engrossed - weren't you?"
    ayesha.say "Oh yeah, [hero.name]!"
    ayesha.say "I was sitting on the edge of my seat at the end."
    ayesha.say "I want to see that one again!"
    return

label ayesha_movie_indifferent_reaction_female:
    bree.say "Normally I don't like that kind of movie, Ayesha."
    bree.say "But somehow I just found myself getting into this one."
    bree.say "I feel really weird now that we're out of there."
    bree.say "I was totally engrossed - weren't you?"
    ayesha.say "Urgh..."
    ayesha.say "It was okay, I guess."
    ayesha.say "But I wouldn't want to sit through it again."
    return

label ayesha_movie_disliked_reaction_female:
    bree.say "Normally I don't like that kind of movie, Ayesha."
    bree.say "But somehow I just found myself getting into this one."
    bree.say "I feel really weird now that we're out of there."
    bree.say "I was totally engrossed - weren't you?"
    ayesha.say "What are you talking about, [hero.name]?"
    ayesha.say "That movie was garbage!"
    ayesha.say "I nearly walked out it was so bad!"
    return

label ayesha_abortion_reaction_female:
    "I look up to see Ayesha standing over me, looking like she means business."
    "She has her balled fists planted on her hips and a frown on her face."
    "At first I'm not sure what could be the cause of her apparent disapproval."
    "But when I meet her eye, Ayesha's gaze travels downwards."
    "I follow it, only to find that she's now staring at my belly."
    ayesha.say "You went and did it, didn't you?"
    ayesha.say "You got a termination!"
    "I back off a little way, trying to gather my courage."
    "It's times like this when I remember how large Ayesha actually is."
    "And it's more than a little intimidating!"
    bree.say "Well..."
    bree.say "Yeah, Ayesha..."
    bree.say "I did."
    bree.say "My body, my choice!"
    if ayesha.love >= 150:
        "Ayesha nods her head."
        "And then she throws her arms wide."
        ayesha.say "You look like you could do with a hug!"
        "I'm so surprised by Ayesha's gesture I can't say no."
        "I just nod, and then I feel her powerful arms wrap around me."
        bree.say "Oh..."
        bree.say "Thank you, Ayesha!"
        bree.say "I was so worried you be MAD!"
        "I spit out the last words as Ayesha squeezes me extra hard."
        ayesha.say "Oh no, [hero.name]!"
        ayesha.say "I know how hard this must be for you."
        ayesha.say "I just want to help in any way I can."
        "I nod and then do the best I can to enjoy the hug."
        "Believe it or not, I'm actually getting a lot out of it."
        "Somehow being wrapped in Ayesha's arms makes everything seems better."
    else:
        "Ayesha shakes her head is disapproval."
        ayesha.say "No such luck for the baby, huh?"
        ayesha.say "I guess they just don't get a choice, right?"
        "I shake my head, beginning to get angry with Ayesha."
        "How dare she judge me like that?"
        bree.say "I already told you, Ayesha..."
        bree.say "I can't raise a kid on my own!"
        bree.say "It's not the right time for me to start a family."
        "Ayesha shakes her head, not convinced by my explanation."
        ayesha.say "Maybe you should have thought about that before you went fooling around, [hero.name]?"
        ayesha.say "Now your being irresponsible has ended a life before it even got started!"
        "I open my mouth to argue back, but Ayesha's not listening."
        "She holds up a hand and then turns to walk away."
        "I think about going after her, about grabbing her arm."
        "But then realise that might end in me getting choked out."
        "And so I leave her to walk away in peace."
    return


label ayesha_belly_interaction_female:
    $ ayesha.set_flag("interact", 1, 1, "+")
    show ayesha at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call ayesha_belly_kiss_female from _call_ayesha_belly_kiss_female_1
        "Caress my belly":
            call ayesha_belly_caress_female from _call_ayesha_belly_caress_female_1
        "Listen to the baby":
            call ayesha_belly_listen_female from _call_ayesha_belly_listen_female_1
        "Never mind":
            pass
    return

label ayesha_belly_caress_female:
    show ayesha happy at center, zoomAt(1.5, (640, 1040))
    "I've started to notice just how much people are staring at my bump by now."
    "Like, the bigger it gets, the more their eyes are drawn to it."
    "And I feel like everyone is just waiting to ask for a chance to touch it too."
    "With most people that can get kind of annoying, making me want to ignore them."
    "But there are some that I always feel like I need to make more of an effort with."
    "And Ayesha is most definitely one of those people."
    "So when I catch her staring at my belly, I smile and gently thrust it towards her."
    bree.say "Hey, Ayesha..."
    bree.say "Caught you looking!"
    show ayesha sadsmile
    "The moment that she realises I'm onto her, Ayesha looks embarrassed as hell."
    "In fact she starts backing off and waving a hand in the air as well."
    "Like she's trying to deny that she was even interested in my bump."
    show ayesha surprised
    ayesha.say "What?"
    show ayesha whining
    ayesha.say "Oh...on no, [hero.name]..."
    ayesha.say "I wasn't doing that!"
    show ayesha sadsmile
    "I can't help frowning and following Ayesha as she backs off."
    "Because I don't like how she's trying to distance herself from me right now."
    bree.say "Don't be silly, Ayesha..."
    bree.say "I want you to touch it!"
    show ayesha whining
    ayesha.say "I...I can't, [hero.name]..."
    ayesha.say "What if I'm not gentle enough?"
    show ayesha sad
    "I blink in sheer amazement."
    "Is that really what's making Ayesha back off?"
    bree.say "That's crazy, Ayesha..."
    bree.say "You're a gentle giant outside of the wrestling ring."
    bree.say "And I trust you to be super gentle."
    show ayesha sadsmile
    "This seems to be enough to convince Ayesha."
    "As she steps forwards and reaches out with one hand."
    show ayesha normal
    "Slowly and carefully, she places it on my belly, palm down."
    show ayesha happy
    "And as she does so, I see a smile spread across her face."
    "Without feeling the need to ask, Ayesha then adds her other hand too."
    "And as she moves them over my belly, I feel myself beginning to smile too."
    "From that point on, all I need to do is stand there in silence and watch."
    "Ayesha is as gentle as can be with me, her touch soft and reassuring."
    "So much so that I swear I can feel the trust between us building by the second."
    $ ayesha.love += 2
    return

label ayesha_belly_kiss_female:
    show ayesha talkative at center, zoomAt(1.5, (640, 1040))
    ayesha.say "Erm..."
    ayesha.say "[hero.name]..."
    ayesha.say "There's something I wanted to ask you."
    ayesha.say "But I don't know how to even start."
    ayesha.say "So I'm just going to come straight out and say it."
    show ayesha normal
    "I look up, unable to hide the interest that Ayesha's words have inspired in me."
    "As usual, she looks like she's been thinking about something very deeply."
    "And the fact that she can't just bury it in the back of her mind is plain to see."
    "All of which makes me remember why she's so very special to me."
    bree.say "Okay, Ayesha..."
    bree.say "I'm listening, so hit me with it!"
    show ayesha sadsmile
    "My response doesn't seem to do anything to help with Ayesha's confidence."
    "If anything, it seems to make her even more nervous than before."
    show ayesha blush
    ayesha.say "I...I..."
    ayesha.say "I wanted to kiss it..."
    ayesha.say "Your belly, that is - I wanted to kiss it!"
    ayesha.say "But if that's too weird, then you don't have to..."
    show ayesha sadsmile
    "I can already feel the smile spreading across my face."
    "And I'm nodding even before I open my mouth to respond."
    bree.say "That's not weird at all, Ayesha."
    bree.say "You know that I like the idea of you kissing me all over."
    bree.say "So planting one on my belly is no different."
    "I emphasize my point by pushing out my bump."
    "And making sure that it's pointing towards Ayesha as I do so."
    "She nods slowly, and begins to reach out in the same manner."
    show ayesha happy at center, zoomAt(1.5, (640, 1240)) with ease
    "I watch as Ayesha lowers herself down onto one knee."
    show ayesha at center, traveling(2.5, 0.3, (640, 1940))
    "Then she leans forwards and closes her eyes."
    "The touch of her lips is so gentle that I don't feel it at first."
    "But as she moves them from one spot to another, the kisses begin to reach me."
    "And from that moment on, I'm transported to a world of subtle bliss."
    "I swear that I can feel the baby moving inside of me as Ayesha kisses me."
    "Almost like it senses her presence as a trusted, loving protector."
    "And the notion of that makes me tingle, deep down inside."
    "Soon every kiss is reaching the very core of my being."
    "Touching me on an emotional level as well as a physical one."
    "And it's something that I don't want to feel end any time soon."
    $ ayesha.love += 3
    return

label ayesha_belly_listen_female:
    show ayesha normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Ayesha..."
    bree.say "Would you mind doing me a little favour?"
    "I try to make myself sound as casual and reasonable as I possibly can."
    "Because I don't want to spook Ayesha before she's even heard what I want."
    "And it seems like I made the right decision too."
    show ayesha stuned
    "As Ayesha still looks up in the manner of a deer caught in the headlights of a car."
    show ayesha surprised
    ayesha.say "Huh?"
    ayesha.say "What is it, [hero.name]?"
    ayesha.say "What do you want?"
    show ayesha stuned
    "I keep on smiling as I put my hands onto the curve of my belly."
    "And at the same time I make a point of looking down at it."
    bree.say "Oh, nothing big, Ayesha."
    bree.say "I just wondered if you'd come over here and listen to my belly?"
    "Ayesha's already started to walk over to me as I ask the question."
    "But I can see her eyes going wide as she realises the implications."
    show ayesha surprised
    ayesha.say "You want me to listen to your belly?"
    ayesha.say "What for, [hero.name]?"
    ayesha.say "Do you think there's something wrong with the baby?"
    show ayesha stuned
    "I shake my head, keen to dismiss any such talk."
    bree.say "No, no, no..."
    bree.say "It's just been a while since I went for my last scan."
    bree.say "And I want to know if there's anything new to hear."
    show ayesha normal at center, traveling(2.5, 0.3, (640, 1940))
    "Ayesha shrugs and starts to lean in towards my belly."
    show ayesha talkative
    ayesha.say "Okay, [hero.name]..."
    ayesha.say "Here goes..."
    show ayesha normal
    "As soon as Ayesha has her ear against my belly, I clamp my mouth shut."
    "Doing all I can too keep quiet as she strains to hear anything inside of me."
    "At first I think Ayesha's going to call it quits and say she can't hear a thing."
    show ayesha curious
    "But then I see a change in her body-language, like her interest is being piqued."
    "It comes almost at the same moment that I feel the baby move too."
    "Ayesha places her hands on my belly, like she's trying to hold me still."
    "And she presses her ear against it with even more pressure than before."
    show ayesha happy
    ayesha.say "I...I can hear them!"
    ayesha.say "I mean...I don't know what they're doing in there..."
    ayesha.say "But they're moving around all over the place, and they sound fine!"
    "I nod and smile again, not feeling the need to say another word."
    "So instead I just stand there and let Ayesha follows the sounds with her ear."
    "Because the experience seems to be doing the both of us such a lot of good."
    $ ayesha.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
