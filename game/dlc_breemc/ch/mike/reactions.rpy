label mike_ask_phone_female:
    if game.week_day % 2 == 0:
        bree.say "Hey, [mike.name]..."
        bree.say "When are you gonna let me have your number?"
    else:
        bree.say "Hey, [mike.name]..."
        bree.say "Can I get your phone number?"
        bree.say "You know, for like if I need to call you about house stuff?"
        bree.say "Or like whatever?"
    if hero.charm >= 20 - mike.love:
        $ hero.smartphone_contacts.append("mike")
        if game.week_day % 2 == 0:
            mike.say "Huh?"
            mike.say "I thought you had it already, [hero.name]?"
            mike.say "If not, here you go - of course I want you to have it!"
        else:
            mike.say "You mean you don't have it already?"
            mike.say "Of course you can have it, [hero.name]."
            mike.say "We need be able to contact each other in case of an emergency!"
            mike.say "Like if we run out of toilet paper!"
    else:
        if game.week_day % 2 == 0:
            mike.say "You don't need my number, [hero.name]."
            mike.say "We live in the same house!"
            mike.say "Just knock on my door or something, okay?"
        else:
            mike.say "Geez, [hero.name]..."
            mike.say "Don't we like live under the same roof?"
            mike.say "You can just tell me stuff when you see me."
            mike.say "Or like pin a note to my door, yeah?"
        $ mike.love -= 1
        $ mike.sub -= 1
    return

label mike_ask_birthday_female:
    if game.week_day % 2 == 0:
        bree.say "[mike.name]..."
        bree.say "I was just wondering something."
        bree.say "When is your birthday?"
    else:
        bree.say "So, [mike.name]..."
        bree.say "When IS your birthday?"
        bree.say "You never actually told me the date!"
    if hero.charm >= 40 - mike.love:
        $ mike.flags.birthdayknown = True
        if game.week_day % 2 == 0:
            mike.say "Oh...I thought you already knew, [hero.name]?"
            mike.say "It's Winter 22, just for the record!"
        else:
            mike.say "Huh?"
            mike.say "I didn't?"
            mike.say "No worries, [hero.name]."
            mike.say "It's Winter 22."
    else:
        if game.week_day % 2 == 0:

            mike.say "Why would you want to know that, [hero.name]?"
            mike.say "I'm not that much older than you!"
            mike.say "I'm kind of embarrassed you'd ask!"
        else:
            mike.say "Why so nosey all of a sudden, [hero.name]?"
            mike.say "Just because we live together doesn't mean I have to tell you everything."
            mike.say "It's not like we're married or anything!"
        $ mike.sub -= 1
        $ mike.love -= 1
    return

label mike_ice_cream_reaction_female:
    bree.say "[mike.name]..."
    bree.say "I feel like getting an ice-cream."
    mike.say "Oh yeah, [hero.name]..."
    mike.say "That sounds like a great idea!"
    "I nod, and together we hurry over to the ice-cream stand."
    "[mike.name] orders his choice and I listen carefully to the details."
    "Then I make my own order, and I can see him doing the same thing."
    mike.say "That's a pretty interesting combination, [hero.name]."
    bree.say "I could say the same about yours!"
    bree.say "In fact, I wouldn't mind a lick of it too..."
    mike.say "Sure thing, [hero.name]!"
    mike.say "So long as I can have a lick of yours?"
    "I nod happily, taking my ice-cream once it's ready."
    "Then [mike.name] and I walk away from the booth, eyeing up each other's choices."
    "Soon enough we're exchanging licks and commenting on those same choices too."
    "Both of us laughing and smiling like a couple of kids."
    return

label mike_offer_a_drink_female:
    bree.say "I'm off to the bar for another drink."
    bree.say "I can grab you another while I'm there, [mike.name]."
    bree.say "I think it's my round anyway!"
    if (hero.charm >= 60 - mike.love and mike.flags.drinks < 2) or date_girl == mike:
        mike.say "Okay, [hero.name] - that sounds good!"
        mike.say "I'll have the same again."
        mike.say "But the next round after that's on me!"
        show drink mike
        if mike.love <= 25:
            $ mike.love += 1
        elif date_girl == mike and game.active_date:
            $ game.active_date.score += 5
        call expression mike.get_chat from _call_expression_397
        hide drink mike
        $ mike.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        mike.say "Slow down, [hero.name]!"
        mike.say "You don't have to drink me under the table."
        mike.say "And I don't remember agreeing to do rounds either!"
        $ hero.cancel_activity()
        hide mike
    return

label mike_slap_ass_intro_female:
    "I don't know if [mike.name] has really tight pants on today."
    "Or maybe it's that he's been working on his ass in the gym."
    "But either way, I can't take my eyes off his butt!"
    "It just looks so good every time he walks past."
    "I wanna squeeze it!"
    "I wanna take a big bite out of it!"
    "I wanna slap it really hard!"
    "A moment later I hear the sound of palm connecting with butt-cheek."
    return

label mike_slap_ass_happy_female:
    "Oh crap - I did it!"
    "I actually slapped [mike.name] on the ass!"
    mike.say "HEY!"
    mike.say "Who slapped my butt?!?"
    mike.say "[hero.name], was that you?"
    bree.say "Erm...yeah...I guess so!"
    "[mike.name] flushes a little red at my admission."
    "But I can see most of the irritation drain out of him."
    mike.say "Oh...okay then..."
    mike.say "I guess I should take it as a compliment."
    mike.say "Normally nobody appreciates my butt!"
    return

label mike_slap_ass_angry_female:
    "Oh crap - I did it!"
    "I actually slapped [mike.name] on the ass!"
    mike.say "HEY!"
    mike.say "Who slapped my butt?!?"
    mike.say "[hero.name], was that you?"
    bree.say "Erm...yeah...I guess so!"
    "[mike.name] flushes red with embarrassment and anger."
    "And he shakes his head to show his disapproval."
    mike.say "You shouldn't behave like that, [hero.name]."
    mike.say "If it's not cool for a guy, then it's not cool for a girl either!"
    bree.say "Okay, mike..."
    bree.say "I'm sorry."
    return

label mike_breakup_female:
    bree.say "Ah, [mike.name]..."
    bree.say "We need to talk!"
    mike.say "Oh no..."
    mike.say "That's never a good thing!"
    "I can only sigh and nod my head."
    bree.say "Yeah...it's not."
    bree.say "It's us, [mike.name]..."
    bree.say "I don't think it's working out, is it?"
    mike.say "You really think so, [hero.name]?"
    bree.say "Yeah, [mike.name], I do."
    bree.say "I think we need to call it a day."
    bree.say "And if we do it now, maybe we can still be friends."
    "[mike.name] looks as crushed and crest-fallen as I expected."
    "And part of me wants to relent and tell him it's okay."
    "But I've come this far and I know that I need to see it through."
    "And in the end, he seems to accept what I'm saying."
    "He nods and lets out a sigh of his own."
    mike.say "Okay, [hero.name]..."
    mike.say "If that's what you think is best..."
    return

label mike_go_steady_intro_female:
    bree.say "We've been getting on so great recently, haven't we, [mike.name]?"
    bree.say "All the dates that we've been on have been super fun, yeah?"
    mike.say "I think so, [hero.name]."
    mike.say "I definitely had a great time when we were hanging out together!"
    bree.say "Sooo..."
    bree.say "I was wondering..."
    bree.say "What if we make things a little more...official?"
    bree.say "Like maybe we could agree to go steady?"
    "[mike.name]'s eyebrows shoot up at the mere mention of the word."
    "And his lips begin to move even before he actually manages to speak."
    return

label mike_go_steady_yes_female:
    mike.say "Y...yeah, [hero.name]..."
    mike.say "I think I'd like that."
    mike.say "I really want to see more of you, as much as I can!"
    mike.say "So that sounds like a great idea."
    return

label mike_go_steady_no_female:
    mike.say "Geez, [hero.name]..."
    mike.say "We already started dating, and it's going well."
    mike.say "Isn't that enough?"
    mike.say "You sound like you want us to get married or something!"
    return

label mike_pet_intro_female:
    "I feel a sudden burst of affection for [mike.name]."
    "So much so that I don't even stop to think what I'm doing."
    "I just reach out and pat him on top of the head."
    "It's only once and it's very light."
    "But the effect is immediate and quite dramatic."
    mike.say "HEY!"
    mike.say "Who patted me on the head?!?"
    mike.say "[hero.name], was that you?"
    bree.say "Erm...yeah...I guess so!"
    return

label mike_pet_happy_female:
    "[mike.name] flushes a little red at my admission."
    "But I can see most of the irritation drain out of him."
    mike.say "Oh...okay then..."
    mike.say "I guess I should take it as a compliment."
    mike.say "But maybe just say it with words next time!"
    return

label mike_pet_annoyed_female:
    "[mike.name] flushes red with embarrassment and anger."
    "And he shakes his head to show his disapproval."
    mike.say "You shouldn't behave like that, [hero.name]."
    mike.say "If it's not cool for a guy, then it's not cool for a girl either!"
    bree.say "Okay, mike..."
    bree.say "I'm sorry."
    return

label mike_massage_intro_female:
    mike.say "Ouch!"
    mike.say "Man, that hurts!"
    bree.say "Ooh...what's up, [mike.name]?"
    bree.say "You look like you're in some serious pain!"
    mike.say "Yeah, [hero.name]..."
    mike.say "I hit the gym pretty hard the other day."
    mike.say "And I think I pulled something in my back!"
    bree.say "You want me to take a look at it?"
    bree.say "I give pretty good massages."
    return

label mike_massage_accept_female:
    mike.say "Would you, [hero.name]?"
    mike.say "I was gonna see if I could get someone to look at it for me."
    mike.say "You know, like a professional?"
    mike.say "But maybe you could help me out until I do."
    return

label mike_massage_refuse_female:
    mike.say "Oh no, [hero.name]!"
    mike.say "I appreciate the offer."
    mike.say "But I need to get this sorted out by a professional."
    mike.say "I know you've got good intentions."
    mike.say "But you could end up making it worse by accident."
    return

label mike_piercing_nipples_reaction_female:
    "I see [mike.name]'s wearing a particularly tight T-shirt today."
    "So I don my usual thing of trying to check him out on the sly."
    "Hey - don't judge me!"
    "He's been working out at the gym and I'm only human!"
    "But then I do a double-take."
    bree.say "Whoa..."
    bree.say "[mike.name], did you..."
    mike.say "Yeah, [hero.name] - I got my nipples pierced."
    mike.say "You like?"
    bree.say "Oh yeah!"
    bree.say "It looks really hot!"
    "[mike.name] smiles, delighted at my reaction."
    mike.say "Maybe you can check them out in the flesh later!"
    return

label mike_piercing_navel_reaction_female:
    "I see [mike.name]'s wearing a particularly tight T-shirt today."
    "So I don my usual thing of trying to check him out on the sly."
    "Hey - don't judge me!"
    "He's been working out at the gym and I'm only human!"
    "But then I do a double-take."
    bree.say "Whoa..."
    bree.say "[mike.name], did you..."
    mike.say "Yeah, [hero.name] - I got my belly button pierced."
    mike.say "You like?"
    bree.say "Oh yeah!"
    bree.say "It looks really hot!"
    "[mike.name] smiles, delighted at my reaction."
    mike.say "Maybe you can check them it in the flesh later!"
    return

label mike_piercing_dick_reaction_female:
    "I see [mike.name]'s wearing a particularly tight pair of pants today."
    "So I don my usual thing of trying to check him out on the sly."
    "Hey - don't judge me!"
    "He's been working out at the gym and I'm only human!"
    "But then I do a double-take."
    bree.say "Whoa..."
    bree.say "Something looks different down there..."
    bree.say "[mike.name], did you..."
    mike.say "Yeah, [hero.name] - I finally got my dick pierced."
    mike.say "You like?"
    bree.say "Oh yeah!"
    bree.say "It looks really hot!"
    "[mike.name] smiles, delighted at my reaction."
    mike.say "Maybe you can check them it in the flesh later!"
    return

label mike_piercing_head_reaction_female:
    "[mike.name] opens his mouth as soon as he sees me."
    "I think he's going to say something to me."
    "But then he just sticks his tongue out instead!"
    bree.say "Well that's pretty rude!"
    bree.say "Whoa...wait a minute!"
    bree.say "[mike.name], did you..."
    mike.say "Yeah, [hero.name] - I finally got my tongue pierced."
    mike.say "You like?"
    bree.say "Oh yeah!"
    bree.say "It looks really hot!"
    "[mike.name] smiles, delighted at my reaction."
    mike.say "Maybe you can check them it in the flesh later!"
    return

label mike_movie_liked_reaction_female:
    bree.say "Wow!"
    bree.say "Best...film...ever!"
    bree.say "I need to see it again, [mike.name]!"
    bree.say "That's an instant classic!"
    mike.say "You don't need to tell me, [hero.name]!"
    mike.say "I was totally blown away by it."
    mike.say "After that, being back in reality sucks!"
    return

label mike_movie_indifferent_reaction_female:
    bree.say "Wow!"
    bree.say "Best...film...ever!"
    bree.say "I need to see it again, [mike.name]!"
    bree.say "That's an instant classic!"
    mike.say "Aah...I dunno, [hero.name]."
    mike.say "It was okay, I guess..."
    mike.say "But I don't think it was really that special, you know?"
    return

label mike_movie_disliked_reaction_female:
    bree.say "Wow!"
    bree.say "Best...film...ever!"
    bree.say "I need to see it again, [mike.name]!"
    bree.say "That's an instant classic!"
    mike.say "Were we even watching the same film, [hero.name]?!?"
    mike.say "That was totally rotten from start to finish!"
    mike.say "How can you even think it was good?"
    return

label mike_abortion_reaction_female:
    "[mike.name]'s been looking at me in a funny way for a while now."
    "But whenever I try to catch his eye, he looks away again."
    "It's just starting to get a little frustrating."
    "And that's when he chooses to change tactics."
    mike.say "[hero.name]..."
    bree.say "Yeah, [mike.name]?"
    mike.say "I...don't know how to ask you this..."
    mike.say "But...you're not pregnant anymore - are you?"
    "Urgh...I knew this conversation was coming sooner or later."
    "The only surprise is that [mike.name]'s being so observant."
    "He's usually one of those guys that's oblivious to everything."
    bree.say "Yeah, you're right."
    bree.say "I hate to admit it, [mike.name]."
    bree.say "But I chose to have a termination."
    bree.say "I just know I wouldn't have been able to cope."
    "I pause, expecting him to say something in response."
    "But he just stares at me, as if he doesn't know what to say."
    bree.say "I hope you don't think any less of me..."
    if (mike.flags.know_is_father and mike.love >= 150) or mike.love <= 150:
        mike.say "Think any less of you?!?"
        mike.say "[hero.name], you just told me you killed a kid!"
        "My jaw drops open as [mike.name] hurls the accusation at me."
        "I thought I was ready for him to be disapproving."
        "But I couldn't have been prepared for what he just said."
        bree.say "How can you say that, [mike.name]?"
        bree.say "You know that it's not the same thing!"
        "[mike.name] shakes his head at me."
        mike.say "It was a human life, [hero.name]!"
        mike.say "And you chose to end it!"
        bree.say "What are you saying?"
        bree.say "You think it was easy?"
        bree.say "You think I just did it on a whim?!?"
        mike.say "Of course not, [hero.name]!"
        mike.say "But..."
        "I hold up a hand, cutting [mike.name] off."
        "And then I turn my back on him and walk away."
        "Maybe he'll be more reasonable when he's had some time to digest it."
        "And maybe not."
        "But either way, I'm not listening to anymore of that."
    else:
        mike.say "Oh no, [hero.name]!"
        mike.say "I think you were brave to make that choice."
        "He pauses to look down at his feet, then back up at me."
        mike.say "And I think it was the right one too."
        mike.say "I mean...I'd have tried to help if you'd kept it."
        mike.say "But I do think this is the right decision."
        "I feel a flood of relief pass through me."
        "Because I've already had arguments with people my decision."
        "And I was ready to be pulled into another one here and now."
        bree.say "Thanks, [mike.name]..."
        bree.say "That means a lot - more than you can know."
        bree.say "Some people haven't been so understanding."
        "[mike.name] nods, but his expression is kind of sad."
        mike.say "I'm just trying to be a good friend, [hero.name]."
        mike.say "I guess you don't need people judging you right now."
    return


label mike_belly_interaction_female:
    $ mike.set_flag("interact", 1, 1, "+")
    show mike at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call mike_belly_kiss_female from _call_mike_belly_kiss_female_1
        "Caress my belly":
            call mike_belly_caress_female from _call_mike_belly_caress_female_1
        "Listen to the baby":
            call mike_belly_listen_female from _call_mike_belly_listen_female_1
        "Never mind":
            pass
    return

label mike_belly_caress_female:
    show mike normal at center, zoomAt(1.5, (640, 1040))
    "I've always been fond of being the centre of attention, even if I'd never admit as much."
    "Even more so when that attention is coming from a guy that I really like a hell of a lot."
    "So when I notice that [mike.name] can't take his eyes off me, it's like the best of both worlds."
    "I mean sure, I know that he's starting at my bump right now."
    "But that's a part of me, so it still counts just the same!"
    bree.say "Hey, [mike.name]..."
    bree.say "You like what you see?"
    show mike surprised
    "As soon as he hears my voice, [mike.name] looks up, surprise written all over his face."
    "But I'm relieved to see that it only takes a moment for that expression to pass."
    show mike smile
    "And then he smiles at me, shrugging his shoulders as he does so."
    show mike happy
    mike.say "You got me, [hero.name]..."
    mike.say "I just can't take my eyes of your bump!"
    mike.say "You know, I never thought we'd have a baby in this house."
    show mike smile
    "I'm pleased with [mike.name]'s reaction on account of how simple and honest it is."
    "He's not trying to hide the fact that he's fascinated by my bump."
    "Or being weird about it now that I've gotten wise to what's going on."
    "He's just owning it and being honest with me, which seems to be a pretty rare reaction."
    "And so I choose to reward him by being just as forward and honest in return."
    "Which in this case involves pulling up the hem of my top and thrusting out my belly."
    bree.say "If you're that interested in it, [mike.name]..."
    bree.say "Would you like to touch it?"
    show mike surprised
    "[mike.name]'s eyes go wide the moment he realises what I'm suggesting."
    "And he nods eagerly, already raising up his hands in anticipation."
    mike.say "Oh wow..."
    mike.say "Are you serious?"
    show mike smile
    "By way of an answer, I push my belly forwards a little more."
    "Which in this case is more than enough to press it against the palms of his hands."
    show mike surprised
    "Now [mike.name]'s eyes are wider than ever, and his mouth is hanging open too."
    mike.say "Oh man..."
    mike.say "This is totally amazing, [hero.name]!"
    mike.say "I never wanted to touch you so much!"
    mike.say "Ah...I...I mean..."
    show mike happy
    mike.say "Like, I still wanted to touch you before you were pregnant."
    mike.say "But, but...not in a creepy way, yeah?"
    show mike smile
    "I can't help chuckling and shaking my head as [mike.name] stumbles over his words."
    "But I put my hands on his wrists and make sure that he doesn't take his hands away."
    "Because he really shouldn't miss out, just because he's stumbling over his own words."
    $ mike.love += 2
    return

label mike_belly_kiss_female:
    show mike happy at center, zoomAt(1.5, (640, 1040))
    mike.say "Ah, [hero.name]..."
    mike.say "I wanted to ask you something."
    show mike normal
    "I can tell from the tone of [mike.name]'s voice that he's itching to ask me for something."
    "But it's also plain to hear that he's worried about actually doing it."
    "So I'm guessing that he's going to need some help to get the question out."
    bree.say "I'm listening, [mike.name]..."
    bree.say "What was it you wanted to ask me?"
    bree.say "Whatever it is, I'm sure it'll be okay."
    "Even as I'm saying this, an idea occurs to me."
    "One that's so obvious I'm amazed I didn't think of it already."
    bree.say "Oh..."
    bree.say "Do you want to touch my bump again?"
    bree.say "Is that it?"
    "For a moment there I was sure that I'd solved the issue."
    "I thought that [mike.name] was going to just breathe a sigh of relief and it'd all be sorted."
    "But instead he looks more embarrassed and awkward than ever."
    show mike blush
    mike.say "Erm..."
    mike.say "No, [hero.name]..."
    mike.say "I was wondering if it'd be okay for me to...to kiss it?"
    show mike down
    "As soon as the words are out of [mike.name]'s mouth, he starts backing off."
    "He's shaking his head and looking like he's dismissing the idea already."
    show mike blush
    mike.say "Of course you don't have to..."
    mike.say "I mean, it's a crazy idea, right?"
    mike.say "Totally weird and inappropriate!"
    bree.say "No way, [mike.name]..."
    bree.say "I think it's a really sweet thing to ask."
    show mike normal
    "[mike.name] stops and stares at me."
    show mike surprised
    mike.say "You do?!?"
    show mike normal
    "I nod and smile as I pull up my too, revealing my belly."
    "And then I point at a particular spot, just above my navel."
    bree.say "Oh yeah, I do!"
    bree.say "And this is a good spot, right here."
    show mike smile at center, traveling(2.5, 0.3, (640, 1940))
    "[mike.name] nods and instantly gets down onto one knee."
    "He puts his hands on my belly and leans in quickly."
    "And the next thing I know, he's planting kisses on it for all he's worth."
    "I can't help smiling as I look down at what he's doing."
    "The kisses are gentle and make me feel so special, almost like he's worshipping me!"
    "And I'm already wondering if he might want to make this a more regular thing."
    $ mike.love += 3
    return

label mike_belly_listen_female:
    show mike normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Ooh..."
    bree.say "Oh man..."
    bree.say "[mike.name], you have to come and feel this!"
    "I have both of my hands on my belly as I'm saying all of this."
    "But I'm looking straight at [mike.name], trying to get him to pay attention."
    "Luckily for me, the fact that I'm pregnant means he's on high alert."
    "And the moment he hears me calling, he sits up and then hurries over."
    show mike surprised
    mike.say "[hero.name]..."
    mike.say "What's the matter?"
    mike.say "Are you okay?"
    mike.say "Is the baby okay?"
    show mike sad
    "I lift one hand and wave it vaguely in the air, trying to get him to calm down."
    "Because it's nothing nearly as dramatic as he seems to think it is."
    bree.say "Stop panicking, [mike.name]!"
    bree.say "The baby's just moving around a lot, that's all."
    bree.say "I thought that you might want to come and feel it."
    show mike normal
    "[mike.name]'s mood changes in the space of mere moments."
    "Before he was worried and doing probably anticipating a trip to the hospital."
    "But now he's staring down at my belly with renewed interest."
    show mike happy
    mike.say "You know what, [hero.name]..."
    mike.say "I wonder if I could actually hear them in there?"
    show mike normal
    "The moment I hear him pitch the idea, my brain just says no."
    "But he just looks so enthusiastic and into it that I can't say as much."
    bree.say "Erm..."
    bree.say "Sure, [mike.name]..."
    bree.say "Why not!"
    show mike smile at center, traveling(2.5, 0.3, (640, 1940))
    "[mike.name] looks happier than ever as he bends over in front of me."
    "And I just stand there, watching his progress the whole time."
    "I can feel that the baby is still moving around in there."
    "So at least there'll be something for him to feel, if nothing else."
    show mike happy at center, zoomAt(2.5, (640, 1940))
    mike.say "Ah..."
    mike.say "I...I think..."
    show mike surprised at startle
    mike.say "Ouch!"
    "[mike.name] stands up quickly, meaning I have to step back a little."
    "And even so he still comes pretty close to hitting my jaw with the top of his head."
    mike.say "[hero.name]..."
    mike.say "You're not going to believe this..."
    mike.say "But the kid kicked me - they kicked me in the side of the head!"
    show mike smile
    bree.say "That's...great?"
    "[mike.name] nods happily as he bends back down again."
    show mike happy
    mike.say "It's amazing!"
    mike.say "I wonder if I can get them to do it again?"
    $ mike.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
