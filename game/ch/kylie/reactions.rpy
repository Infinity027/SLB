label kylie_ice_cream_reaction_male:
    mike.say "I'm going to pass out if I don't cool down soon - let's grab some ice cream!"
    kylie.say "Yeah, that sounds like a great idea - I'm crazy hot too!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Kylie chooses the same thing, but with her own combination of flavours."
    show kylie annoyed
    kylie.say "Ah...urgh...what the..."
    mike.say "What's the matter, Kylie?"
    "I look around to see Kylie staring a the end of her own nose."
    "Or more specifically, the blob of ice cream sitting on it."
    kylie.say "How on earth did that get there?!?"
    "I do my best to show sympathy and keep from laughing."
    "But she just looks so silly that I can't help myself."
    return

label kylie_study_with_intro_male:
    "When I found out that Kylie was studying so much, I didn't hesitate to offer my help."
    "I mean, of course I want to actually make sure she does well in her studies."
    "But it's also a chance to spend time alone with a really hot girl, right?"
    "So Kylie gets a helping hand and I get to bask in her hotness - everyone wins!"
    "Or that's what I'm thinking until I see the pile of books she brings along."
    mike.say "Wow..."
    mike.say "This can't be all the stuff you have to study, Kylie!"
    kylie.say "Oh no, [hero.name], of course not!"
    kylie.say "This is just as much of it as I could carry."
    "I don't have an answer for that, so I just shake my head."
    "And luckily for me, Kylie seems to take that as one."
    "She dives straight into the first text-book."
    "And I do my best to keep up."
    "I think that I'm doing okay, that I've got the hang of it."
    "Until Kylie stops and lets out a sigh."
    "It's hard not to notice the way her chest heaves in and out as she does so."
    "And I almost find myself too distracted to notice that she's talking to me."
    kylie.say "I HATE this kind of problem, [hero.name]."
    kylie.say "They make me so mad!"
    "I lean in closer to see what's bothering Kylie."
    "And my eyes go wide at the complexity of I see on the page."
    kylie.say "You see what I mean, [hero.name]?"
    kylie.say "Can you get your head around it?"
    return

label kylie_study_with_success_male:
    "I give Kylie a smile and scrutinise the page for all I'm worth."
    "It takes me a few minutes, but I apply myself to the task one hundred percent."
    "And then the solution just seems to jump out at me."
    mike.say "Look at this, Kylie."
    mike.say "This bit, right here."
    "Kylie follows my finger as I point it out to her."
    "And I watch as a smile slowly spreads across her face."
    show kylie happy
    kylie.say "I see it, [hero.name]!"
    kylie.say "I see what you mean!"
    show kylie at center, zoomAt(1.5, (640, 1040)) with hpunch
    "Without warning, Kylie throws her arms around me."
    "And the next thing I know, she's hugging me with all her strength!"
    mike.say "Whoa..."
    mike.say "Kylie - I need to breathe!"
    show kylie normal
    "Kylie loosens her grip, but only a little."
    "It's almost like she's refusing to let me go!"
    kylie.say "I knew it, [hero.name]!"
    kylie.say "I knew that you were smart!"
    mike.say "Erm..."
    mike.say "Thanks, Kylie!"
    mike.say "You can let me go now."
    mike.say "I mean...you don't HAVE to..."
    return

label kylie_study_with_failure_male:
    "I give Kylie a smile and scrutinise the page for all I'm worth."
    "But it's no use, no matter how hard I try, I just can't figure it out."
    "So all I can do is stall for more time."
    mike.say "Ah..."
    mike.say "I'm thinking, Kylie..."
    mike.say "Really racking my brain here!"
    "I can see the smile on Kylie's face as I sweat over the problem."
    "And I watch as it becomes steadily more strained as time passes."
    kylie.say "Well, [hero.name]?"
    kylie.say "What do you think?"
    kylie.say "You've been staring at it for ages now!"
    mike.say "Erm..."
    mike.say "Maybe we could skip this one, Kylie?"
    mike.say "Come back to it later after we do the next one?"
    show kylie sad
    kylie.say "But the next one is the same, [hero.name]!"
    kylie.say "The only difference is that it's even harder!"
    "All I can do is shrug helplessly at this."
    "Kylie narrows her eyes, scrutinising me closely."
    show kylie normal
    kylie.say "Hmm..."
    kylie.say "I always imagined you were smarter than this!"
    show kylie happy
    kylie.say "Well, I guess nobody's THAT perfect..."
    return

label kylie_ask_phone_male:
    mike.say "I was going to ask for your number, Kylie."
    mike.say "Would that be okay?"
    if hero.charm >= 20 - kylie.love:
        show kylie happy
        $ hero.smartphone_contacts.append("kylie")
        kylie.say "Of course you can have my number, [hero.name]!"
        kylie.say "And you can call me anytime you like."
        kylie.say "I'll be waiting for your call!"
    else:
        show kylie annoyed
        $ kylie.love -= 1
        $ kylie.sub -= 1
        kylie.say "I don't like to give out my number, [hero.name]."
        kylie.say "It means people can get to know where I am."
        kylie.say "And sometimes that can be...awkward!"
    return

label kylie_ask_birthday_male:
    mike.say "Kylie, I don't think you ever told me..."
    mike.say "When is your birthday?"
    if hero.charm >= 40 - kylie.love:
        show kylie happy
        $ kylie.flags.birthdayknown = True
        kylie.say "Of course..."
        kylie.say "I want you to know EVERYTHING about me!"
        kylie.say "It's Winter 15 - so don't forget it, okay?"
        kylie.say "No need to tell me yours, I know it by heart..."
    else:
        show kylie annoyed
        $ kylie.sub -= 1
        $ kylie.love -= 1
        kylie.say "I can't tell you that, [hero.name]."
        kylie.say "It's...a...a secret!"
        kylie.say "Yeah, a secret - that's it!"
    return

label kylie_offer_a_drink_male:
    mike.say "You want a drink, Kylie?"
    mike.say "Because I was just going to grab one."
    "Almost the second the words are out of my mouth, Kylie turns to face me."
    if kylie.is_visibly_pregnant:
        show kylie angry
        $ kylie.love -= 10
        kylie.say "Alcohol?"
        kylie.say "Are you trying to hurt our baby?!?"
        kylie.say "What are you, [hero.name] - insane?!?"
        $ hero.cancel_activity()
        hide kylie
    elif (hero.charm >= 60 - kylie.love and kylie.flags.drinks < 2) or date_girl == kylie:
        show kylie happy
        kylie.say "Sure, [hero.name], I'll have a Bloody Mary."
        kylie.say "And be sure to make it extra bloody too!"
        kylie.say "I'll just not take my pills tonight..."
        hide kylie
        show drink kylie
        if kylie.love <= 25:
            $ kylie.love += 1
        elif date_girl == kylie and game.active_date:
            $ game.active_date.score += 5
        call expression kylie.get_chat from _call_expression_245
        hide drink kylie
        $ kylie.set_flag("drinks", 1, "day", mod="+")
    else:
        show kylie annoyed
        kylie.say "I can't drink too much, [hero.name]."
        kylie.say "It interferes with my medication..."
        $ hero.cancel_activity()
        hide kylie
    return

label kylie_slap_ass_intro_male:
    "There's no denying the fact that Kylie's got quite some figure."
    "She curves in and out in all the right places."
    "And that ass too - it's a work of art in it's own right."
    "It's so full and round, and the way it moves as she walks!"
    "I just can't resist the chance to give it a gentle slap..."
    return

label kylie_slap_ass_happy_male:
    kylie.say "Who..."
    kylie.say "What..."
    kylie.say "Why..."
    "Kylie turns to face me, narrowing her eyes."
    kylie.say "[hero.name], was that you?!?"
    "All I can do is smile and nod."
    "Kylie's face breaks out into a delighted smile."
    kylie.say "Oh, that's okay then!"
    kylie.say "Slap my ass anytime you like."
    return

label kylie_slap_ass_angry_male:
    kylie.say "Who..."
    kylie.say "What..."
    kylie.say "Why..."
    "Kylie turns to face me, narrowing her eyes."
    kylie.say "[hero.name], was that you?!?"
    "All I can do is smile and nod."
    "Kylie's face turns dark with rage."
    kylie.say "That is NOT okay!"
    kylie.say "Do it again, and it'll be the last thing you ever do!"
    return

label kylie_breakup_male:
    show kylie
    "I hate the idea of having to break it to a girl that I want to end it with her."
    "Especially a girl as hot and cute as Kylie, who seems to be crazily into me too!"
    "But I just have this gut feeling that there's something missing in our relationship."
    "Some kind of spark, the kind of thing to get the heart pumping, you know?"
    "That's why I think I have to call it off now, before we get too serious."
    if kylie.yandere >= 50 and kylie.love < 50:
        show kylie
        mike.say "I am sorry Kylie but I am not interested in you the way you are in me..."
        if kylie.love >= 25:
            show kylie sad
        mike.say "I hope we can stay friends."
        kylie.say "I know you don't mean it [hero.name]."
        mike.say "..."
        $ kylie.yandere += 25
        hide kylie
        return "denied"
    mike.say "Ah, Kylie..."
    mike.say "I was thinking..."
    "The moment that I begin to speak, Kylie's head snaps around."
    "It's like she's hanging on my every word, eager to hear me out."
    kylie.say "What's that, [hero.name]?"
    kylie.say "What's on your mind?"
    "She seems so interested in what I have to say."
    "Almost like there's nothing as important as the words about to come out of my mouth."
    mike.say "Erm..."
    mike.say "There's no easy way to say this, Kylie."
    mike.say "But I think we need to call it quits."
    show kylie annoyed
    "Kylie stares at me blankly for a couple of seconds."
    "And I'm beginning to think that she hasn't heard or understood me."
    "But then I catch the smallest hint of movement on her face."
    "One of her eyes twitches, like a nervous tic or something."
    "And then she finally speaks."
    show kylie happy
    kylie.say "Oh, [hero.name]..."
    kylie.say "Don't be silly!"
    kylie.say "You don't mean that."
    "It's not an argument against us splitting up."
    "It's not even an appeal for me to think again."
    "Kylie just outright dismissed what I said!"
    mike.say "No, Kylie, no..."
    mike.say "I'm being serious here."
    mike.say "I really want to split up with you!"
    "Kylie smiles and shakes her head."
    "Then she lets out a sigh."
    kylie.say "I know you don't really mean that, [hero.name]."
    kylie.say "It's just that you don't know that you don't mean it yet."
    kylie.say "But you'll soon see that I'm right..."
    "With that, Kylie walks away, smiling over her shoulder at me."
    "I guess that means that we're officially over, right?"
    "But I can't help feeling a chill run down my spine."
    "Because I don't know if Kylie thinks it's over at all!"
    return

label kylie_go_steady_intro_male:
    mike.say "I'm having the best time with you right now, Kylie."
    mike.say "That's why I think it's time we took it to the next level."
    mike.say "How about we go steady?"
    return

label kylie_go_steady_yes_male:
    kylie.say "Oh, yes, [hero.name]!"
    kylie.say "A hundred...no a thousand...no a million times yes!"
    kylie.say "This is how it was meant to be!"
    "Kylie almost pounces on me."
    "Kissing me with a hunger that's almost as scary as it is hot!"
    return

label kylie_go_steady_no_male:
    kylie.say "Oh no, [hero.name], not yet."
    kylie.say "The time isn't right yet."
    kylie.say "But some time it will be."
    kylie.say "And then there'll be no escaping it..."
    return

label kylie_pet_intro_male:
    "I smile and give Kylie a gentle pat on the head."
    "I don't know why I choose that kind of a gesture."
    "And I realise that I have no idea how she'll react either."
    return

label kylie_pet_happy_male:
    kylie.say "Ah..."
    kylie.say "Thank you, [hero.name]!"
    kylie.say "I love it when you praise me!"
    return

label kylie_pet_annoyed_male:
    kylie.say "What the hell?!?"
    kylie.say "What are you even doing?"
    kylie.say "Don't touch me like that!"
    return

label kylie_massage_intro_male:
    mike.say "Oh, Kylie..."
    mike.say "You look so tense!"
    mike.say "Would you like me to give you a massage?"
    mike.say "It usually helps people relax."
    return

label kylie_massage_accept_male:
    kylie.say "That sounds just perfect, [hero.name]."
    kylie.say "You can give me a massage anytime."
    kylie.say "And I'm sure you'll make me feel better."
    return

label kylie_massage_refuse_male:
    kylie.say "DON'T TOUCH ME!"
    kylie.say "I...I mean...please, don't touch me, [hero.name]!"
    kylie.say "I've been known to lash out when I'm in pain."
    return

label kylie_piercing_nipples_reaction_male:
    kylie.say "Mmm..."
    kylie.say "I love the way they look, [hero.name]."
    kylie.say "And I love the fact you love them too."
    kylie.say "It's like I've had my nipples pierced so that I can be chained to you forever!"
    return

label kylie_piercing_navel_reaction_male:
    kylie.say "I think this thing makes my belly-button look pretty sweet."
    kylie.say "And it's a reminder of how we're an item now, [hero.name]."
    kylie.say "Of how you're becoming a part of me too!"
    return

label kylie_piercing_clit_reaction_male:
    kylie.say "Oh...oh wow..."
    kylie.say "This thing feels SO good!"
    kylie.say "And even better, it reminds me of you, [hero.name]!"
    return

label kylie_piercing_head_reaction_male:
    kylie.say "This is great, [hero.name]."
    kylie.say "Every word I say is wrapped around my new piercing."
    kylie.say "And I can't speak a single one without thinking of you!"
    return

label kylie_piercing_nose_reaction_male:
    kylie.say "I love the way this thing looks, [hero.name]!"
    kylie.say "And if you get one too, we can chain ourselves together, huh?"
    kylie.say "Kidding...I was only kidding!"
    return

label kylie_movie_disliked_reaction_male:
    kylie.say "Oooh...I hate it when a film's that bad - it makes me SO angry!"
    return

label kylie_movie_indifferent_reaction_male:
    kylie.say "Boring films are worse than bad ones - they should be slashed to ribbons!"
    return

label kylie_movie_liked_reaction_male:
    kylie.say "I loved that film so much - I want to keep watching it forever, just me and you!"
    return

label kylie_belly_kiss_male:
    show kylie at center, zoomAt(1.25, (640, 880))
    "I don't know where the instinct comes from to do it."
    "One moment I'm totally fine, and the next it just pops right in there."
    "But as soon as it does, I know that I have to go through with it."
    "So the next time that Kylie pulls up her top to let me touch her bump, I make my move."
    show kylie at center, traveling(2.0, 1.0, (640, 980))
    "Instead of simply touching her belly with my hand, I lean all the way in."
    "And then I plant a kiss on the curve."
    show kylie smile
    kylie.say "Oh..."
    kylie.say "Oh, [hero.name]!"
    show kylie at center, traveling(2.0, 1.0, (640, 1290))
    "I look up, worried that I've stepped over some invisible line."
    "That Kylie's going to want to keep me from touching her belly in future."
    mike.say "Are you okay, Kylie?"
    mike.say "I don't know why I did that..."
    mike.say "It just felt like the natural thing to do!"
    show kylie impressed
    "Kylie's pale cheeks look a little flushed with colour."
    "And she blinks while she listens to my faltering explanation."
    "But then she shakes her head."
    show kylie happy
    kylie.say "No, [hero.name]..."
    kylie.say "That was really sweet."
    kylie.say "I really likes it!"
    show kylie smile at center, traveling(2.0, 1.0, (640, 980))
    "Nodding and feeling a sense of relief, I lean in again."
    "And this time I kiss Kylie's belly with a renewed sense of confidence."
    return

label kylie_belly_caress_male:
    show kylie at center, zoomAt(1.25, (640, 880))
    "I can't take my eyes off of Kylie as she sits there holding onto her belly."
    "She seems to be totally fixated on it, not interested in anything else at all."
    "Her hands are constantly moving over the surface of it too, stroking and caressing it."
    "Sometimes I could even swear that she's whispering stuff to it too!"
    mike.say "Erm..."
    mike.say "Kylie..."
    show kylie smile
    "Kylie pauses to look up at me."
    "And when she does, I can't ever remember seeing her so happy before."
    show kylie happy
    kylie.say "Yeah, [hero.name]..."
    show kylie talkative
    kylie.say "What is it?"
    show kylie normal
    "My eyes shoot down to the curve of Kylie's belly."
    "And then they come back up to look her in the eye again."
    mike.say "I don't suppose I could..."
    mike.say "Maybe have a little..."
    show kylie at center, traveling(1.5, 0.5, (640, 1040))
    "I hardly realise that I'm reaching out with my hand as I say all of this."
    "And the motion must be purely unconscious, based on instinct alone."
    show kylie smile with vpunch
    "Because I can't help jumping a little when Kylie reaches out and takes my hand."
    "Then without saying a word, she guides it to her belly and holds it there."
    "It doesn't take long for me to feel a sudden movement in there too."
    "And this time, when I look up, my smile's almost as big as Kylie's."
    return

label kylie_belly_listen_male:
    show kylie at center, zoomAt(1.25, (640, 880))
    mike.say "Kylie..."
    mike.say "You mind if I try something?"
    mike.say "You know, with your bump?"
    show kylie stuned
    "Kylie cocks her head on one side as she listens to me."
    "Clearly she's intrigued by what I could have in mind."
    show kylie talkative
    kylie.say "Try me, [hero.name]…"
    kylie.say "I'm sure it'll be okay."
    show kylie smile
    kylie.say "You know, so long as it's not super-weird!"
    show kylie normal
    "I wrinkle my eyebrows and wave away her concerns."
    mike.say "Hey, it's me..."
    mike.say "How weird could it be?"
    show kylie annoyed
    "But from the look on Kylie's face, I sense I might have made a mistake there."
    mike.say "Don't answer that!"
    show kylie normal
    mike.say "Okay, cards on the table..."
    mike.say "We had the ultrasound at the hospital, right?"
    mike.say "Well, I want to see what I can hear on my own."
    show kylie normal
    "Kylie shrugs and hikes up her top."
    "Which of course means that her huge belly is instantly on show."
    show kylie smile
    kylie.say "It's all yours."
    show kylie normal at center, traveling(2.0, 1.0, (640, 980))
    "Kylie gestures to her belly as I lean in closer."
    "Putting my ear to her bump, I hold up a hand for silence."
    "At first I can't hear a thing, but then I detect a subtle sound."
    mike.say "That's it, right there..."
    mike.say "I can hear it, Kylie..."
    mike.say "I can hear the baby!"
    show kylie happy
    "I can hear Kylie chuckling at my enthusiasm."
    "But that doesn't bother me in the slightest."
    "Because this is worth so much more then trying to look nonchalant and cool."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
