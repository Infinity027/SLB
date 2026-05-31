label audrey_ice_cream_reaction_male:
    mike.say "It's so frickin hot today, Audrey - let's go grab an ice cream!"
    audrey.say "Yeah, I feel like I'm going to pass out from the heat!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Audrey chooses a colourful ice lolly, striped and glistening in the sun."
    mike.say "I can't eat those things, Audrey - they give me brain-freeze!"
    audrey.say "Hah - like you've got one to freeze!"
    "I'm about to object to the insult when she starts to suck on it."
    "And then all I can do is watch her in stunned silence."
    "Audrey sucks on the lolly like she means it, working it up and down."
    "I don't know if she's doing it on purpose - but it looks downright erotic!"
    return

label audrey_ask_phone_male:
    mike.say "You have a number, right, Audrey?"
    mike.say "And maybe I could get it, yeah?"
    if hero.charm >= 20 - audrey.love:
        show audrey happy
        $ hero.smartphone_contacts.append("audrey")
        audrey.say "I guess you can have it, [hero.name]."
        audrey.say "You have earned it!"
    else:
        show audrey flirt
        $ audrey.love -= 1
        $ audrey.sub -= 1
        audrey.say "I don't think so, [hero.name]."
        audrey.say "At least not yet."
        audrey.say "Not until you earn it!"
    return

label audrey_ask_birthday_male:
    mike.say "Audrey, I just wanted to ask..."
    mike.say "When's your birthday?"
    if hero.charm >= 40 - audrey.love:
        show audrey happy
        $ audrey.flags.birthdayknown = True
        audrey.say "It's Summer 16, [hero.name]."
        audrey.say "And you'd better not forget it either!"
    else:
        show audrey annoyed
        $ audrey.sub -= 1
        $ audrey.love -= 1
        audrey.say "Ha!"
        audrey.say "I'm not just going to TELL you, [hero.name]."
        audrey.say "You have to figure it out for yourself!"
    return

label audrey_offer_a_drink_male:
    mike.say "How about I get you a drink, Audrey?"
    mike.say "Whatever you like - just name it."
    "Almost the second the words are out of my mouth, Audrey turns to face me."
    if audrey.is_visibly_pregnant:
        show audrey angry
        $ audrey.love -= 10
        audrey.say "Wow, [hero.name], just wow."
        audrey.say "Way to win Father of the Year!"
        audrey.say "This kid's screwed before it's even been born!"
        $ hero.cancel_activity()
        hide audrey
    elif (hero.charm >= 60 - audrey.love and audrey.flags.drinks < 2) or date_girl == audrey:
        show audrey happy
        audrey.say "Geez, I thought you'd never ask!"
        audrey.say "Vodka and tonic - and make it snappy!"
        hide audrey
        show drink audrey
        if audrey.love <= 25:
            $ audrey.love += 1
        elif date_girl == audrey and game.active_date:
            $ game.active_date.score += 5
        call expression audrey.get_chat from _call_expression_211
        hide drink audrey
        $ audrey.set_flag("drinks", 1, "day", mod="+")
    else:
        show audrey annoyed
        audrey.say "Nah, I'll sort myself out, thank you."
        audrey.say "I don't want to die of thirst waiting for you to figure it out!"
        $ hero.cancel_activity()
        hide audrey
    return

label audrey_slap_ass_intro_male:
    "Audrey's ass just looks so good today."
    "The outfit she has on and the way she's walking..."
    "It's all that I can do to tear my eyes away from it!"
    "And so can you really blame me for what I do next?"
    "Which is to give it a firm but gentle slap."
    return

label audrey_slap_ass_happy_male:
    audrey.say "Whoa!"
    audrey.say "What the..."
    "Audrey stops dead in her tracks."
    "But it doesn't take her long to figure out what just happened."
    "She fixes me with a stare."
    audrey.say "You better mean that, [hero.name]."
    audrey.say "And when the time comes..."
    audrey.say "You better be able to back it up too!"
    return

label audrey_slap_ass_angry_male:
    audrey.say "Whoa!"
    audrey.say "What the..."
    "Audrey stops dead in her tracks."
    "But it doesn't take her long to figure out what just happened."
    "She fixes me with a stare."
    audrey.say "You better think real hard, [hero.name]."
    audrey.say "Think real hard before you do that again."
    audrey.say "Because if you don't..."
    audrey.say "You might end up regretting it!"
    return

label audrey_breakup_male:
    show audrey
    "I'm dreading the moment that I have to tell Audrey what's on my mind."
    "She's pretty feisty at the best of times, with a quick temper too."
    "But this is one of those things for which there's never a right time."
    "So fuck it, here goes..."
    mike.say "Ah, Audrey..."
    mike.say "There's no easy way to say this..."
    mike.say "But I don't think I want to date you anymore!"
    show audrey sad
    "I have no idea what Audrey was about to say before I spoke up."
    "But the bombshell seems to have stopped her dead in her tracks."
    audrey.say "I..."
    audrey.say "I'm sorry..."
    audrey.say "I must have heard that wrong, [hero.name]."
    audrey.say "I thought you just said it was over between us!"
    "I let out a meek chuckle and shake my head."
    mike.say "No, Audrey."
    mike.say "You heard me alright."
    mike.say "I don't want to see you anymore."
    mike.say "At least not in a romantic sense..."
    "Audrey looks visibly shaken for a moment."
    "As if her usually unflappable confidence has taken a hit."
    "But then she shakes her own head."
    show audrey angry
    "And her confidence seems to come flooding back."
    audrey.say "Oh no, [hero.name]."
    audrey.say "No way."
    audrey.say "YOU don't get to dump ME!"
    audrey.say "That's not how this thing between us works, you get that?"
    "I can't help feeling a little sorry for Audrey."
    "Normally this kind of thing makes her look like she's the one in control."
    "But right now she just seems desperate to put her own spin on things."
    audrey.say "Actually, you've done me a favour."
    mike.say "Erm..."
    mike.say "I have?"
    audrey.say "Yes, because I was going to dump you anyway."
    audrey.say "And you just proved I was right all along."
    "Audrey seems to consider that an end to the matter."
    "As she turns on her heel and walks away."
    mike.say "Okay..."
    mike.say "I'll see you at work, I guess..."
    "Which, I suspect, is going to me more than a little awkward."
    return

label audrey_go_steady_intro_male:
    mike.say "Hey, Audrey..."
    mike.say "I was just wondering..."
    mike.say "It's about time we admitted we're going steady, right?"
    return

label audrey_go_steady_yes_male:
    audrey.say "Hmm..."
    audrey.say "I guess that we could say that, [hero.name]."
    audrey.say "You've earned it!"
    return

label audrey_go_steady_no_male:
    audrey.say "Uh-uh, [hero.name]!"
    audrey.say "I don't think we're there yet."
    audrey.say "You're going to have to work harder to earn it!"
    return

label audrey_pet_intro_male:
    "Part of me knows that this is a dangerous path to tread."
    "But another part of me can't resist seeing what happens."
    "So I pat Audrey on the head and wait to see her reaction..."
    return

label audrey_pet_happy_male:
    audrey.say "Wha..."
    audrey.say "What did you do?"
    audrey.say "B...because I kinda liked it!"
    return

label audrey_pet_annoyed_male:
    audrey.say "Wha..."
    audrey.say "What did you do?"
    audrey.say "Whatever it was, you'd better not do it again!"
    return

label audrey_massage_intro_male:
    mike.say "You're more cranky than usual, Audrey."
    mike.say "Would you like a massage or something like that?"
    mike.say "It could help you chill out."
    return

label audrey_massage_accept_male:
    audrey.say "I'M NOT CRANKY!"
    audrey.say "Ah, shit...I guess I am!"
    audrey.say "Yeah, [hero.name], that massage sounds like a good idea..."
    return

label audrey_massage_refuse_male:
    audrey.say "I...am...not...cranky!"
    audrey.say "And if you touch me with anything at all..."
    audrey.say "Well, I'll...I'll break it off!"
    return

label audrey_piercing_nipples_reaction_male:
    audrey.say "You know, I hate to admit when I'm wrong and you're right."
    audrey.say "But piercing my nipples was a great idea, [hero.name]!"
    audrey.say "Seems you do have them...once in a while!"
    return

label audrey_piercing_navel_reaction_male:
    audrey.say "I should have had my belly-button pierced years ago!"
    audrey.say "And, yeah...I admit it, [hero.name]."
    audrey.say "This was a good idea, and it was one of yours!"
    return

label audrey_piercing_clit_reaction_male:
    audrey.say "Why didn't I think of this myself?"
    audrey.say "It feels great, like I have a secret weapon in my panties!"
    audrey.say "You outdid yourself this time, [hero.name]!"
    return

label audrey_piercing_head_reaction_male:
    audrey.say "I'm glad you talked me into getting this thing, [hero.name]."
    audrey.say "But just to warn you, it doesn't change anything."
    audrey.say "I'm still going to use my tongue to speak my mind."
    audrey.say "And for other fun things too!"
    return

label audrey_piercing_nose_reaction_male:
    audrey.say "Be honest with me, [hero.name]..."
    audrey.say "Do you think it's too much?"
    audrey.say "I mean...I like it, I do."
    audrey.say "Actually, what am I talking about - it's fucking great!"
    return

label audrey_call_in:
    if "audrey_event_09" not in DONE and "audrey_event_08" in DONE and Room.has_tag(game.room, 'mcoffice') and not audrey.hidden and Room.has_tag(audrey.room, 'work') and audrey.love >= 160:
        call audrey_event_09_intro from _call_audrey_event_09_intro
    else:
        if audrey.flags.nickname == "toy":
            mike.say "Toy can you come to my office?"
        else:
            mike.say "Audrey can you come to my office?"
        show audrey
        audrey.say "Yes [hero.name]?"
    return

label audrey_movie_disliked_reaction_male:
    audrey.say "Well, that's the last time I let YOU choose the movie - that was a pile of garbage!"
    return

label audrey_movie_indifferent_reaction_male:
    audrey.say "That was so boring - even a really BAD film would have been better!"
    return

label audrey_movie_liked_reaction_male:
    audrey.say "I can't believe you chose such a great movie - what are the odds of that?!?"
    return

label audrey_belly_kiss_male:
    show audrey talkative at center, zoomAt(1.25, (640, 880))
    audrey.say "[hero.name]…"
    audrey.say "Get over here!"
    show audrey yawn
    "I see Audrey puckering her lips and winking at me."
    "Which can only mean that she wants to be kissed."
    show audrey at center, traveling(1.5, 0.5, (640, 1040))
    "So I hurry straight over, already preparing my own lips."
    show audrey stuned with hpunch
    "But before I can reach her, something gets in the way."
    mike.say "What the..."
    show audrey awkward
    audrey.say "Ah, damn it!"
    show audrey annoyed
    "I look down to see what's come between us."
    "And I'm surprised to see that it's the curve of Audrey's belly."
    "By now it's gotten big enough to keep us well apart."
    mike.say "Whoops!"
    mike.say "Looks like I can't deliver, Audrey."
    show audrey frown
    "Audrey frowns, showing her frustration with the situation."
    with hpunch
    "Then she pushes her belly against me, harder still."
    show audrey mock
    audrey.say "Well this is kind of your fault, [hero.name]."
    audrey.say "So you'd better think up a solution, and fast!"
    show audrey annoyed
    "I'm nodding before I've even managed to get my brain in gear."
    "Trying to think of a practical way to solve the problem."
    "And then it hits me."
    "Perhaps not the perfect solution, but it just might work."
    show audrey normal at center, traveling(2.0, 1.0, (640, 980))
    "Getting down on one knee, I lean my head forwards."
    "Audrey watches as best she can over the curve of her belly."
    "And I can tell that she's interested in seeing what I've come up with."
    "So I don't hesitate to start kissing her belly, right around the navel."
    "At first I can hear Audrey gasping and tutting, as though she's not happy."
    show audrey happy
    "But the more I plant kisses on her belly, the more the sounds begin to soften."
    "Soon enough Audrey's cooing and sighing with what sounds like genuine satisfaction."
    "And I can even feel her beginning to push her belly against me."
    "Which I choose to take as an invitation to kiss her even more."
    return

label audrey_belly_caress_male:
    show audrey angry at center, zoomAt(1.25, (640, 880))
    audrey.say "Hey, [hero.name]…"
    audrey.say "What in the hell are you looking at?!?"
    show audrey upset with vpunch
    "At the sound of Audrey's voice, I almost leap out of my skin."
    "It doesn't help matters that I was staring at her when she caught me in the act."
    "Or to be more specific, I was taking the chance to have a long look at her belly."
    mike.say "Erm..."
    mike.say "What..."
    mike.say "What are you talking about, Audrey?"
    mike.say "I wasn't looking at anything, I swear it!"
    show audrey frown at center, traveling(1.5, 0.5, (640, 1040))
    "Audrey narrows her eyes as she advances on me."
    "And it looks like she's not in the mood to let me off lightly."
    show audrey angry
    audrey.say "Yes you were, you lying little worm!"
    audrey.say "You were staring at this weren't you?"
    show audrey frown
    "Audrey slaps her belly as she gets closer to me."
    "Thrusting it out in front of her at the same time."
    show audrey mock
    audrey.say "I bet you were patting yourself on the back, huh?"
    audrey.say "Thinking what a big, virile man you are."
    audrey.say "Telling yourself you should brag to your buddies the next time you see them!"
    show audrey frown
    "I can't believe that I'm doing this."
    "But I'm actually cowering away from Audrey right now."
    "Like she's really intimidating me!"
    mike.say "No, Audrey..."
    mike.say "I wasn't, I swear it!"
    show audrey mock at center, zoomAt(1.5, (640, 1040))
    audrey.say "Well why the hell not?!?"
    show audrey normal at stepback(speed=0.1, h=-10, v=-20)
    "Audrey pushes her belly up against me as she says this."
    mike.say "Huh?"
    mike.say "What do you mean?"
    show audrey happy at startle
    "Audrey chuckles and shakes her head as her whole demeanour changes."
    show audrey normal at center, traveling(1.75, 1.0, (640, 880))
    "Then she reaches out and takes hold of my hands, placing them on her belly."
    show audrey happy
    audrey.say "Oh, [hero.name]…"
    audrey.say "You are so easy to wind up!"
    audrey.say "And for that, you can stare at my belly all you like."
    show audrey normal
    "I find myself beginning to smile too."
    "Realising that Audrey is fucking with me right now."
    return

label audrey_belly_listen_male:
    show audrey talkative at center, zoomAt(1.25, (640, 880))
    audrey.say "[hero.name]…"
    audrey.say "Come and listen to my belly!"
    show audrey normal
    "I can't help looking up with genuine interest as Audrey makes the demand of me."
    "She's a little distance from me right now, holding her bump with both hands."
    "And she's also staring down at it with an intense look of interest on her face."
    show audrey at center, traveling(1.5, 0.5, (640, 1040))
    "So wanting to be a good boyfriend and expecting father, I hurry over."
    mike.say "What's the matter, Audrey?"
    mike.say "There's nothing wrong with the baby, is there?"
    "Audrey shakes her head as she looks up at me."
    "Which is an instant source of relief."
    show audrey talkative
    audrey.say "No, nothing like that."
    audrey.say "The little bugger's just moving around like crazy in there."
    audrey.say "I want you to have a listen, see what you can make of it."
    show audrey normal at center, traveling(1.75, 2.0, (640, 880))
    "I shrug as I begin to get down on one knee in front of Audrey."
    mike.say "I'm not sure what I can make out."
    mike.say "But if that's what you want..."
    "Audrey nods eagerly."
    show audrey talkative
    audrey.say "It is, it is..."
    audrey.say "So get on with it already!"
    show audrey happy
    audrey.say "Less talking and more listening!"
    show audrey at center, traveling(2.0, 0.5, (640, 980))
    "I wave Audrey's commands away as I put an ear to her belly."
    "It takes a moment for me to properly adjust my senses after that."
    "To blot out the sounds of everything else and concentrate on the belly."
    "But once I do, it's like plugging into a whole different world."
    mike.say "Whoa..."
    show audrey surprised
    audrey.say "What is it?"
    audrey.say "What can you hear?!?"
    show audrey normal
    mike.say "It's like one of those meditation tapes, Audrey..."
    mike.say "Like when you listen to whale sounds and stuff..."
    mike.say "To relax, yeah?"
    show audrey annoyed
    audrey.say "Urgh..."
    audrey.say "Not only has this kid made me fat..."
    audrey.say "They've also turned me into some kind of hippie sound system too!"
    return

label audrey_ask_hot_coffee_male:
    if audrey.is_sex_slave:
        audrey.say "Sir… no games tonight. Just me, the way you’ve taught me."
        mike.say "Then show me your focus."
        audrey.say "Yes, Sir. I’m yours to guide, not to fight."
        mike.say "And you trust that completely?"
        audrey.say "With every breath."
    elif audrey.sub >= 50:
        audrey.say "So… about that hot coffee, Sir… your place or mine?"
        mike.say "You offering or provoking?"
        audrey.say "Both. You know I like a little pushback before I behave."
    else:
        if randint(0, 1):
            audrey.say "So… are we having that ‘hot coffee’ at your place or mine?"
            mike.say "Depends. You actually planning to drink it?"
            audrey.say "Maybe. Maybe I’ll just let it cool on the sheets."
            mike.say "That sounds messy."
            audrey.say "Guess you’ll have to find out, huh?"
        else:
            show audrey talkative
            audrey.say "You know, I live just a few blocks from here."
            show audrey shy
            mike.say "Is that an invitation or a warning?"
            show audrey talkative
            audrey.say "Depends. You could come by… hang out a bit. I’ve got wine, bad movies, and zero self-control."
            show audrey normal
            mike.say "Sounds dangerous."
            show audrey joke
            audrey.say "Only if you’re lucky."
            show audrey normal
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
