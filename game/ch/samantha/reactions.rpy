label samantha_ice_cream_reaction_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "On a day like this, Cupcake, we need some ice cream!"
    else:
        mike.say "On a day like this, Sam, we need some ice cream!"
    samantha.say "You read my mind - let's go grab some, yeah?"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Sam chooses the same thing, but with her own combination of flavours."
    samantha.say "Mmm...that tastes SO good!"
    samantha.say "Oh...oh, oh, oh...that not so good!"
    "I look down, wondering what's got Sam so upset."
    "And I stare in amazement as I see the ice cream dripping onto her breasts!"
    samantha.say "Oh god - how could I miss my mouth?!?"
    "All I can do is nod in sympathy, afraid to speak in case I say what's really on my mind right now!"
    return

label samantha_ask_phone_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake..."
    else:
        mike.say "Hey, Sam..."
    mike.say "Can I have your phone number?"
    if hero.charm >= 20 - samantha.love:
        show samantha happy
        $ hero.smartphone_contacts.append("samantha")
        samantha.say "I thought you already had it, [hero.name]?"
        samantha.say "Here it is anyway..."
    else:
        show samantha annoyed
        $ samantha.love -= 1
        $ samantha.sub -= 1
        samantha.say "Not really, [hero.name]."
        samantha.say "I just got a new number."
        samantha.say "And I'm kind of keeping it a secret to screen my calls!"
    return

label samantha_ask_birthday_male:
    mike.say "Oh, yeah..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Before I forget, Cupcake - when's your birthday?"
    else:
        mike.say "Before I forget, Sam - when's your birthday?"
    if hero.charm >= 40 - samantha.love:
        show samantha happy
        $ samantha.flags.birthdayknown = True
        samantha.say "You already know that, [hero.name]!"
        samantha.say "But just to remind you - it's Summer 8!"
    else:
        show samantha annoyed
        $ samantha.sub -= 1
        $ samantha.love -= 1
        samantha.say "Urgh..."
        samantha.say "We lived together like forever, [hero.name]!"
        samantha.say "You should already know that!"
    return

label samantha_offer_a_drink_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake..."
    else:
        mike.say "Hey, Sam..."
    mike.say "You want anything from the bar?"
    mike.say "I'm just gonna get another drink."
    "Almost the second the words are out of my mouth, Sam turns to face me."
    if samantha.is_visibly_pregnant:
        show samantha angry
        $ samantha.love -= 10
        samantha.say "Grow up, [hero.name]!"
        samantha.say "I'm pregnant, remember?"
        if not samantha.flags.NPCpregnancy:
            samantha.say "Something you had a hand in too, I seem to recall!"
        $ hero.cancel_activity()
        hide samantha
    elif (hero.charm >= 60 - samantha.love and samantha.flags.drinks < 2) or date_girl == samantha:
        show samantha happy
        samantha.say "Oh, sure thing, [hero.name]."
        samantha.say "Just grab me a beer, okay?"
        hide samantha
        show drink samantha
        if samantha.love <= 25:
            $ samantha.love += 1
        elif date_girl == samantha and game.active_date:
            $ game.active_date.score += 5
        call expression samantha.get_chat from _call_expression_261
        hide drink samantha
        $ samantha.set_flag("drinks", 1, "day", mod="+")
    else:
        show samantha annoyed
        samantha.say "No thank you, [hero.name]."
        samantha.say "I want to stay in control."
        $ hero.cancel_activity()
        hide samantha
    return

label samantha_slap_ass_intro_male:
    "I've always found it hard to watch Sam walking."
    "And by that I don't mean that she's hard to look at."
    "Quite the opposite in fact - I can't take my eyes off of her!"
    "She looks good standing still, but moving she's poetry in motion."
    "And that ass - I just want to reach out and slap it..."
    return

label samantha_slap_ass_happy_male:
    samantha.say "Hey!"
    samantha.say "What the hell?!?"
    samantha.say "That was you, wasn't it, [hero.name]?"
    "There's nobody else it could possibly be."
    "So I just shrug and nod."
    "Sam narrows her eyes and shakes her head."
    "But I can see that she's not mad at me."
    samantha.say "I don't mind you doing that on occasion."
    samantha.say "Just don't make a habit of doing it all the time."

    return

label samantha_slap_ass_angry_male:
    samantha.say "Hey!"
    samantha.say "What the hell?!?"
    samantha.say "That was you, wasn't it, [hero.name]?"
    "There's nobody else it could possibly be."
    "So I just shrug and nod."
    "Sam narrows her eyes and shakes her head."
    "And I can see that she's pretty mad at me."
    samantha.say "I'd rather you didn't, [hero.name]."
    samantha.say "As it's kind of humiliating."

    return

label samantha_breakup_male:
    show samantha
    "You know the way that you can want something so badly it almost hurts?"
    "But then once you finally manage to get it, the lustre comes off of it?"
    "I hate to admit this, but that's just what's happened with Sam and me."
    "I think I was so amazed to finally be with her that I just went with it."
    "And now I find myself wanting to end it almost as badly as I wanted her to begin with!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake..."
    else:
        mike.say "Sam..."
    mike.say "You're gonna hate me for this..."
    mike.say "But I don't think this is working out!"
    show samantha sad
    "Sam stops dead in her tracks, her face dropping as she does so."
    "She shakes her head and blinks, as if thinking she misheard me."
    samantha.say "You..."
    samantha.say "You can't be serious, [hero.name]?"
    samantha.say "Not after all that we've been through to get here?"
    "All I can do is let out a weary sigh."
    "And then I shake my head too."
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm sorry, Cupcake."
    else:
        mike.say "I'm sorry, Sam."
    mike.say "But that's the way I feel."
    mike.say "And I owe it to you to be honest."
    samantha.say "But I thought we were supposed to be together?"
    samantha.say "And now you tell me that you're bored of me?!?"
    "I hold my hands up at this."
    "And I try to get Sam to calm down."
    if samantha.flags.nickname == "cupcake":
        mike.say "Whoa, Cupcake..."
    else:
        mike.say "Whoa, Sam..."
    mike.say "Hold on a minute there!"
    mike.say "I never said I was bored, not for a minute!"
    show samantha angry
    samantha.say "You didn't need to, [hero.name]."
    samantha.say "It's written all over your face."
    samantha.say "All you ever wanted was the thrill, wasn't it?"
    samantha.say "The excitement of fucking your friend's girl!"
    samantha.say "You were jealous and you used me to get back at him!"
    if samantha.flags.nickname == "cupcake":
        mike.say "No, Cupcake - no way!"
    else:
        mike.say "No, Sam - no way!"
    "But Sam's not listening to me anymore."
    "And she turns her back to me, walking away without looking back."
    samantha.say "Well you got what you wanted, [hero.name]."
    samantha.say "We're done, you and me."
    samantha.say "It's over!"
    return

label samantha_go_steady_intro_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake..."
    else:
        mike.say "Hey, Sam..."
    mike.say "We've been having such a good time together."
    mike.say "I think we should make it official, yeah?"
    return

label samantha_go_steady_yes_male:
    samantha.say "You're right, [hero.name]."
    samantha.say "We have and we should."
    hide samantha
    show samantha kiss
    $ samantha.flags.kiss += 1
    "Sam plants a kiss on my lips to make her point."
    "And it doesn't take long for it to turn more passionate either!"
    return

label samantha_go_steady_no_male:
    samantha.say "I'd like to keep it casual, [hero.name]."
    samantha.say "You know, just a little longer?"
    samantha.say "I'm not ready for commitment just yet."
    return

label samantha_pet_intro_male:
    "I chuckle and give Sam a quick pat on the head."
    "I don't know why, it just seems like the right thing to do."
    "But then I start to worry about how Sam's going to react..."
    return

label samantha_pet_happy_male:
    samantha.say "Oh...oh my..."
    samantha.say "[hero.name]..."
    samantha.say "You never did that to me before."
    samantha.say "But I kinda like it!"
    return

label samantha_pet_annoyed_male:
    samantha.say "Ah, [hero.name]..."
    samantha.say "In all the time I was with him, Ryan never did that to me."
    samantha.say "And you're not going to either!"
    return

label samantha_massage_intro_male:
    mike.say "Ooh..."
    if samantha.flags.nickname == "cupcake":
        mike.say "That looks painful, Cupcake!"
    else:
        mike.say "That looks painful, Sam!"
    mike.say "Would you like me to give you a massage?"
    return

label samantha_massage_accept_male:
    samantha.say "Ouch..."
    samantha.say "You're right, [hero.name], it does hurt."
    samantha.say "And a massage sounds really good right about now too!"
    return

label samantha_massage_refuse_male:
    samantha.say "Ouch..."
    samantha.say "Thanks for the offer, [hero.name]."
    samantha.say "But I think I'll just tough it out, okay?"
    return

label samantha_piercing_nipples_reaction_male:
    samantha.say "I never thought piercings were my thing, you know?"
    samantha.say "But I'm really glad you talked me into getting my nipples done, [hero.name]."
    samantha.say "It's like you're helping me to discover new things about myself."
    samantha.say "Things I could never have found out when I was with Ryan!"
    return

label samantha_piercing_navel_reaction_male:
    samantha.say "Huh...I always wanted to get my belly-button pierced."
    samantha.say "But I was afraid that Ryan wouldn't approve."
    samantha.say "So thanks for being a better boyfriend!"
    return

label samantha_piercing_clit_reaction_male:
    samantha.say "I'm SO glad you talked me into doing this, [hero.name]."
    samantha.say "It looks so good and it makes me feels so hot too!"
    samantha.say "I love that you make me discover new things about myself."
    return

label samantha_piercing_head_reaction_male:
    samantha.say "Ooh...it feels so weird to have something in my mouth the whole time..."
    samantha.say "Oh god...that's not what I meant to say...I mean..."
    samantha.say "Well, you know what I mean, [hero.name]!"
    samantha.say "This was a great idea, so thanks!"
    return

label samantha_piercing_nose_reaction_male:
    samantha.say "You know, I always looked at girls with nose piercings and was jealous."
    samantha.say "But I never had the courage to just go out and get one myself."
    samantha.say "I guess that was before I started dating you, [hero.name]!"
    return

label samantha_movie_disliked_reaction_male:
    samantha.say "Eww...that movie was a real stinker, don't you think?"
    return

label samantha_movie_indifferent_reaction_male:
    samantha.say "Yeah, that was kind of a boring movie."
    return

label samantha_movie_liked_reaction_male:
    samantha.say "That was amazing - straight into my all time top ten!"
    return

label samantha_belly_kiss_male:
    show samantha normal at center, zoomAt(1.25, (640, 880))
    "Sam just looks so good today that I feel like I have to kiss her."
    "And I need to do it right now!"
    "So I take hold of Sam's hand and lean in, just like I always do."
    "But then I realise that there's something thing between us."
    "Something that's keeping me from reaching Sam!"
    mike.say "Hey, Sam..."
    mike.say "What gives?"
    show samantha stuned
    "Sam looks around, suddenly seeing what I'm trying to do."
    "And it doesn't take her long to spot what the problem is either."
    show samantha talkative
    samantha.say "Erm..."
    samantha.say "[hero.name]..."
    show samantha sadsmile
    "Sam points down, and I follow her finger."
    "Then I see the shape of her belly, filling the space between us."
    mike.say "Oh..."
    mike.say "Oh right!"
    show samantha happy at startle
    "Sam chuckles to herself as she takes hold of my hands."
    show samantha talkative
    samantha.say "Maybe just let me know next time you'd like a kiss?"
    samantha.say "Otherwise this little one's going to come between us!"
    hide samantha
    show samantha kiss
    with fade
    "Sam leans forwards and plants a kiss on my lips."
    "But even as she does so, I'm thinking about what she just said."
    "So when the kiss comes to an end, I kneel down in front of her."
    hide samantha
    show samantha stuned at center, zoomAt(2.0, (640, 980))
    with fade
    "Sam cocks her head on one side, clearly wondering what I'm doing."
    mike.say "Interesting thing you just said, Sam."
    mike.say "About the kid coming between us."
    mike.say "But I'm not about to let that happen."
    "I lean in and plant a kiss on the curve of Sam's bump."
    "And then I look up at her, making sure to smile as I do so."
    show samantha happy
    mike.say "So if you get a kiss, so does the baby."
    return

label samantha_belly_caress_male:
    show samantha normal at center, zoomAt(1.25, (640, 880))
    "Sometimes I have to actually pinch myself when Sam walks into the room."
    "Pinch myself in order to remember that we really are together now, and that I'm not dreaming."
    "But now that she's pregnant too, I find myself doing it twice as often."
    "Because the whole thing just feels like it's too damn perfect to be real."
    with hpunch
    mike.say "Ouch!"
    show samantha sad at center, traveling(1.5, 0.3, (640, 1040))
    "The moment that Sam hears me cry out in pain, she comes rushing over."
    "A look of worry on her face as she cradles her belly like the precious load it is."
    show samantha surprised
    samantha.say "[hero.name]…"
    samantha.say "What's the matter?"
    samantha.say "Are you okay?"
    show samantha sad
    mike.say "Oh..."
    mike.say "I was nothing, Sam, nothing at all."
    mike.say "I just...bit my tongue..."
    mike.say "That's it, I bit my tongue!"
    "I watch as Sam's eyes travel down to my arm."
    show samantha stuned
    "And then I see them go wide as she takes in the red mark that's plain to be seen there."
    "Sam points a finger at it while she looks me in the eye, bafflement written all over her face."
    show samantha surprised
    samantha.say "Are you doing what I think you're doing?"
    samantha.say "Are you actually pinching yourself?"
    show samantha sadsmile
    "The idea of it sounds so stupid when Sam says it like that."
    "I almost feel like laughing at the idea and waving it all away."
    "But there's something in her eyes that tells me it won't work."
    mike.say "Erm..."
    mike.say "Yeah, Sam, I was..."
    mike.say "This is going to sound crazy, but I was checking everything's real!"
    show samantha happy at startle
    "Sam puts a hand over her mouth as she chuckles to herself."
    show samantha talkative
    samantha.say "Oh, [hero.name]..."
    samantha.say "That's the silliest thing I've ever heard!"
    show samantha happy
    samantha.say "But it's probably the sweetest too."
    show samantha normal
    "Sam reaches out and takes hold of my hands."
    "And I offer no resistance as she places them on her stomach."
    show samantha happy
    samantha.say "You can do this whenever you need to, [hero.name]."
    samantha.say "And you can keep your hands here until you're convinced..."
    samantha.say "Until you're convinced that the both of us are real."
    return

label samantha_belly_listen_male:
    show samantha talkative at center, zoomAt(1.25, (640, 880))
    samantha.say "[hero.name]..."
    samantha.say "Would you come over here for a minute?"
    show samantha normal
    "I look over to Sam, interest written all over my face."
    "Because I'm always intrigued by what she wants or what she's doing."
    mike.say "I'm coming, Sam..."
    mike.say "What do you need?"
    show samantha at center, traveling(1.5, 0.3, (640, 1040))
    "Sam's already hiking up the front of her top as I make it over to her."
    "And she doesn't hesitate to thrust her belly towards me a second later."
    show samantha talkative
    samantha.say "Here you go..."
    samantha.say "Get a good hold of my bump!"
    show samantha normal
    "I do as I'm told, putting my hands straight onto Sam's belly."
    "Which is no chore for me, as I love to get my hands on it whenever I can."
    mike.say "Erm..."
    mike.say "What exactly are we doing here, Sam?"
    mike.say "I mean, if you just want me to stroke your belly..."
    mike.say "That's totally fine by me..."
    show samantha talkative
    samantha.say "That's not it at all, [hero.name]."
    samantha.say "I want you to listen to the baby."
    samantha.say "To put your ear right here..."
    show samantha normal
    "Sam puts her hand on her belly to show me where she means."
    show samantha talkative
    samantha.say "And listen really closely, okay?"
    samantha.say "So you can tell me what they're doing."
    show samantha normal
    "I shrug as I finally come to understand what's going on around here."
    mike.say "Okay, Sam..."
    mike.say "I'm not sure if it'll work, you know?"
    mike.say "Because they use all that technical stuff to do it at the hospital, remember?"
    "I get the impression that Sam's hardly listening to me right now."
    show samantha normal at center, traveling(2.0, 1.0, (640, 980))
    "So I just get down on my knees and do as I'm told."
    mike.say "Right, Sam..."
    mike.say "Here goes!"
    "At first I'm not surprised that I can't hear a thing."
    "And I'm just about to tell Sam as much."
    "But then I swear that I actually hear something in there."
    "It's faint, and I have to really concentrate."
    "But it's definitely there!"
    mike.say "Oh..."
    mike.say "Oh wow..."
    mike.say "I can hear them in there!"
    show samantha surprised
    samantha.say "You can?"
    samantha.say "That's great news!"
    samantha.say "So?"
    mike.say "So what?"
    samantha.say "So what are they doing?"
    mike.say "They're tapping out Morse Code, Sam!"
    samantha.say "Are they really?!?"
    "I shake my head in amusement."
    mike.say "Of course not, Sam!"
    mike.say "How am I supposed to know what they're doing?"
    mike.say "Apart from moving around, totally at random!"
    show samantha happy
    "Sam's cheeks flush as she realises how silly the question sounds."
    "But she listens closely as I describe what I can hear in minute detail."
    "Which seems to be more than enough to satisfy her."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
