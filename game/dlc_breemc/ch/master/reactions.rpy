label master_ice_cream_reaction_female:
    bree.say "Phew..."
    bree.say "It's so hot today, master!"
    bree.say "I feel like I'm going to pass out."
    "The old man snorts and shakes his head at this."
    master.say "Ha!"
    master.say "A student of the martial arts cares not for the weather!"
    master.say "You must learn to endure, my dear."
    "I cast my gaze around as he's saying this."
    "And then my eyes settle on something that could solve my problem."
    bree.say "Ooh!"
    bree.say "How about an ice-cream?"
    "At the mere mention of a frozen treat, the old man's mood changes completely."
    master.say "Ice-cream?"
    master.say "That sounds good!"
    "He seems to forget all about the importance of enduring discomfort."
    "And instead he almost sprints over to the ice-cream stand."
    "We order what we want from the menu."
    "And soon enough we're handed our ice-creams."
    master.say "Mmm..."
    master.say "MMM..."
    master.say "Oh yes..."
    "I try not to watch as the old man licks at his ice-cream."
    "Because it's an almost perverse sight as his tongue goes to work on it."
    "And all the time I can see he's eyeing up my ice-cream too!"
    "So I try to look the other way and think of something, anything else..."
    return

label master_ask_phone_female:
    bree.say "Why don't you let me have your phone number, master?"
    bree.say "It'd make arranging the time and place we meet up so much easier."
    bree.say "Don't you think?"
    if hero.charm >= 20 - master.love:
        $ hero.smartphone_contacts.append("master")
        master.say "That's a wonderful idea, my dear!"
        master.say "That way I can call you up whenever I desire you..."
        master.say "I...I mean desire to see you!"
        master.say "Here you go..."
    else:
        $ master.love -= 1
        $ master.sub -= 1
        master.say "There's no need for that, my dear."
        master.say "If need be, I can contact you with the power of my mind!"
        master.say "Plus I don't share my phone number around."
        master.say "Just in case it ends up in the hands of tele-marketers..."
    return

label master_ask_birthday_female:
    bree.say "You know what, master - you've never actually told me how old you are."
    bree.say "I mean, I can understand an older guy being sensitive about that kind of thing."
    bree.say "But you could at least tell me when your actual birthday is, yeah?"
    if hero.charm >= 40 - master.love:
        $ master.flags.birthdayknown = True
        master.say "You are persistent, my dear!"
        master.say "And that deserves a reward."
        master.say "So I will tell you that my birthday is Summer 3."
    else:
        master.say "Sadly I cannot divulge such information, my dear."
        master.say "There are those skilled in the mystical arts that could use it against me."
        master.say "So I must keep all such information a secret!"
        $ master.sub -= 1
        $ master.love -= 1
    return

label master_offer_a_drink_female:
    bree.say "I'm still feeling thirsty, master."
    bree.say "Would you like me to get you a drink while I go for another?"
    bree.say "My treat, of course!"
    if (hero.charm >= 60 - master.love and master.flags.drinks < 2) or date_girl == master:
        master.say "How kind and thoughtful of you, my dear."
        master.say "I'll have whatever you're having."
        master.say "But make mine a double!"
        show drink master
        if master.love <= 25:
            $ master.love += 1
        elif date_girl == master and game.active_date:
            $ game.active_date.score += 5
        call expression master.get_chat from _call_expression_396
        hide drink master
        $ master.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        master.say "No thank you, my dear."
        master.say "I cannot take the risk of someone spiking my drink."
        master.say "Because I know how easy it is to do that!"
        $ hero.cancel_activity()
        hide master
    return

label master_slap_ass_intro_female:
    "I keep looking at the master's ass, and I can't help giggling."
    "It's so skinny and scrawny, like he's all bone and gristle!"
    "And part of me can't help wondering what it'd be like to slap it..."
    return

label master_slap_ass_happy_female:
    master.say "Ouch!"
    master.say "Hey..."
    master.say "What the..."
    "Did I actually just do it?"
    "Did I slap his ass without a conscious thought?"
    "Looks like I did."
    bree.say "Sorry, master!"
    bree.say "I just couldn't help myself..."
    "The master smiles almost as soon as he hears my confession."
    master.say "That's alright, my dear."
    master.say "Just so long as I know it was you that did it."
    master.say "Feel free to touch as much of me as you want as often as you want to!"
    return

label master_slap_ass_angry_female:
    master.say "Ouch!"
    master.say "Hey..."
    master.say "What the..."
    "Did I actually just do it?"
    "Did I slap his ass without a conscious thought?"
    "Looks like I did."
    bree.say "Sorry, master!"
    bree.say "I just couldn't help myself..."
    "The master frowns at me, his brows knotting as he does so."
    master.say "A pupil must never put their hands on a master."
    master.say "To do so is a show of extreme disrespect."
    master.say "Unless the master demands to be touched..."
    return

label master_breakup_female:
    bree.say "Urgh..."
    bree.say "There's no easy way to say this, master..."
    bree.say "But I think it's time we ended our relationship."
    "The master's head spins around at this."
    "And the next thing I know he's shaking it at me."
    master.say "No, no, no!"
    master.say "There's so much more I have to teach you, my dear!"
    bree.say "Erm, no..."
    bree.say "You're not getting it, master."
    bree.say "I don't mean our master and pupil relationship."
    bree.say "I mean our personal relationship - that's what's over!"
    master.say "But, but, but..."
    bree.say "No, master - don't try your mind-tricks on me."
    bree.say "I've made my decision!"
    return

label master_go_steady_intro_female:
    bree.say "Master..."
    master.say "Yes, my dear?"
    bree.say "I feel like we've been getting on pretty well lately."
    bree.say "Like our relationship is working out, you know?"
    "The master nods and smiles indulgently."
    master.say "Indeed it has."
    master.say "Your focus has improved greatly since then!"
    bree.say "Well..."
    bree.say "Maybe we should make it official then?"
    bree.say "You know, like go steady or something?"
    return

label master_go_steady_yes_female:
    master.say "Why didn't I think of that myself!"
    master.say "Of course we should, my dear."
    master.say "The closer we become the better our bond will be!"
    return

label master_go_steady_no_female:
    master.say "No, my dear."
    master.say "We must retain a certain distance from one another."
    master.say "This will help you to remain focused on your pursuit of excellence."
    return

label master_pet_intro_female:
    "I keep seeing light reflecting off the top of the master's head."
    "Before now I never realised how smooth and shiny it was!"
    "But that means that I now have the urge to touch it."
    "Just for the sake of finding out what it feels like."
    "I can't resist any longer."
    "So I reach out and pat him on top of his head!"
    master.say "What the..."
    master.say "What is the meaning of this?"
    master.say "Why are you patting me on the head?"
    bree.say "Sorry, Master..."
    bree.say "Your head is just so shiny."
    bree.say "I couldn't help myself!"
    return

label master_pet_happy_female:
    "The master smiles almost as soon as he hears my confession."
    master.say "That's alright, my dear."
    master.say "Just so long as I know it was you that did it."
    master.say "Feel free to touch as much of me as you want as often as you want to!"
    return

label master_pet_annoyed_female:
    "The master frowns at me, his brows knotting as he does so."
    master.say "A pupil must never put their hands on a master."
    master.say "To do so is a show of extreme disrespect."
    master.say "Unless the master demands to be touched..."
    return

label master_massage_intro_female:
    master.say "Aieee!"
    "At the sound of the master screeching, I turn around."
    "The first thing I think is that he must be practicing some advanced technique."
    "He's capering on the spot, yelling and waving his arms around at random."
    "But then I see that he keeps on clutching at his neck."
    bree.say "Oh..."
    bree.say "Are you in pain, master?"
    master.say "Yes, yes, yes..."
    master.say "I think my chakras are out of alignment!"
    master.say "Or perhaps my chi is in need of righting!"
    master.say "But maybe I just pulled something in my neck..."
    bree.say "Would you like me to take a look at it?"
    bree.say "I've been told I give a pretty good massage!"
    return

label master_massage_accept_female:
    master.say "Mmm!"
    master.say "That sounds like a fine idea!"
    master.say "Just be sure to get nice and deep, my dear."
    master.say "And don't be afraid to massage around the spot too!"
    return

label master_massage_refuse_female:
    master.say "NO!"
    master.say "My body must only be manipulated by a master of the art of massage!"
    master.say "It is throbbing with the barely suppressed energies of the martial arts."
    master.say "Manipulation by an amateur could release forces of untold destruction!"
    return

label master_piercing_nipples_reaction_female:
    "When the master walks up, I can see that his shirt is open."
    "And to me, that makes it seem like he's trying to show something off."
    master.say "Hello, my dear..."
    master.say "Isn't it a beautiful day?"
    bree.say "You seem very happy, master."
    bree.say "Almost like you have something to show me!"
    "The old man beams and thrusts his chest forwards."
    "And it's then that I see his nipples have been pierced!"
    bree.say "Oh, master!"
    bree.say "Very adventurous of you!"
    "He keeps on smiling as he shows them off to me."
    "Clearly basking in my apparent approval."
    return

label master_piercing_navel_reaction_female:
    "When the master walks up, I can see that his shirt is open."
    "And to me, that makes it seem like he's trying to show something off."
    master.say "Hello, my dear..."
    master.say "Isn't it a beautiful day?"
    bree.say "You seem very happy, master."
    bree.say "Almost like you have something to show me!"
    "The old man beams and thrusts his chest forwards."
    "And it's then that I see his belly button been pierced!"
    bree.say "Oh, master!"
    bree.say "Very adventurous of you!"
    "He keeps on smiling as he shows it off to me."
    "Clearly basking in my apparent approval."
    return

label master_piercing_dick_reaction_female:
    "When the master walks up, I can see that his shirt is open."
    "And to me, that makes it seem like he's trying to show something off."
    master.say "Hello, my dear..."
    master.say "Isn't it a beautiful day?"
    bree.say "You seem very happy, master."
    bree.say "Almost like you have something to show me!"
    "The old man beams and thrusts his chest forwards."
    master.say "A little lower, my dear..."
    bree.say "Oh, master!"
    bree.say "You had your manhood pierced?"
    bree.say "Very adventurous of you!"
    "He keeps on smiling as he shows it off to me."
    "Clearly basking in my apparent approval."
    return

label master_piercing_head_reaction_female:
    "When the master walks up, I can see that his shirt is open."
    "And to me, that makes it seem like he's trying to show something off."
    master.say "Hello, my dear..."
    master.say "Isn't it a beautiful day?"
    bree.say "You seem very happy, master."
    bree.say "Almost like you have something to show me!"
    "The old man beams and thrusts his chest forwards."
    master.say "A little higher, my dear..."
    "As I look upwards, the master sticks out his tongue."
    bree.say "Oh, master!"
    bree.say "You had your tongue pierced?"
    bree.say "Very adventurous of you!"
    "He keeps on smiling as he shows it off to me."
    "Clearly basking in my apparent approval."
    return

label master_movie_liked_reaction_female:
    bree.say "That movie was the greatest!"
    bree.say "It had everything - fights, explosions and romance!"
    bree.say "What did you think, master?"
    "The old man nods his head with evident enthusiasm."
    master.say "I would have liked more explosions."
    master.say "And definitely more flesh on show."
    master.say "But yes, it was a very enjoyable film."
    return

label master_movie_indifferent_reaction_female:
    bree.say "That movie was the greatest!"
    bree.say "It had everything - fights, explosions and romance!"
    bree.say "What did you think, master?"
    "The old man grumbles and shakes his head."
    master.say "Hmm..."
    master.say "It wasn't bad."
    master.say "But there wasn't enough flesh on show!"
    return

label master_movie_disliked_reaction_female:
    bree.say "That movie was the greatest!"
    bree.say "It had everything - fights, explosions and romance!"
    bree.say "What did you think, master?"
    "The old man shakes his head and grumbles."
    master.say "What are you talking about?"
    master.say "That film was the worst!"
    master.say "The martial arts were as fake as the boobies!"
    master.say "And there weren't enough fake boobies too!"
    return

label master_abortion_reaction_female:
    "I'm starting to wonder if the Master's teachings are finally working."
    "Or if some of the mystical power he claims to possess is rubbing off on me."
    "Because I can almost sense him studying me before I look up and see him."
    "And when I do, he flinches a little, like he wasn't expecting it!"
    bree.say "Is there something the matter, Master?"
    bree.say "You look like you want to ask me something."
    "The old man does his best to look like he's not flustered."
    "But the act isn't good enough to fool me."
    "Not now that I know him so well."
    master.say "Ah yes, my dear..."
    master.say "I sensed something in your aura just now!"
    bree.say "My aura?"
    master.say "Yes, a certain change in the vital energies..."
    master.say "Are you not...pregnant anymore?"
    "Oh, so that's what all of this is about."
    "There doesn't seem to be any point in denying it."
    "So I just decide to tell him the truth."
    bree.say "Yes, master..."
    bree.say "I went to a clinic."
    bree.say "And I had a termination."
    if (master.flags.know_is_father and master.love >= 150) or master.love <= 150:
        "The old man stares at me for a moment."
        "But then his expression darkens."
        "And he shakes his head in obvious disappointment."
        master.say "Ah..."
        master.say "It seems that my teachings have been in vain!"
        master.say "Because you have chosen an unwise path."
        "I can't help frowning at this."
        "Who in the hell does he think he is?"
        "This guy's supposed to be teaching me martial arts."
        "It's not like he's in charge of my life!"
        bree.say "Excuse me!"
        bree.say "But I don't need you to lecture me on that kind of stuff!"
        bree.say "If I want to chop through a plank of wood, I'll come to you."
        bree.say "But what happens to my body is my business, thank you!"
        "The Master makes a rueful sound in response to this."
        master.say "My dear..."
        master.say "I fear you have strayed from the path of wisdom!"
    else:
        "The old man stares at me for a moment."
        "And then he lets out a sigh of relief."
        master.say "Oooh..."
        master.say "Thank the heavens!"
        master.say "I believe you've made the right decision."
        "I nod, but can't help feeling a little surprised."
        "Because his reaction seems at odds with his teachings."
        bree.say "You really do, master?"
        bree.say "I thought you'd lecture me about the sanctity of life, or something?"
        master.say "That's all well and good, my dear."
        master.say "But it's a different matter when you're the one saddled with it!"
        master.say "This way is better, believe me."
        master.say "Plus, there's nothing to interfere with your studies!"
        "I smile and nod."
        "But I can't help thinking he's gloating a little."
        "Which isn't very becoming of a man in his position."
    return


label master_belly_interaction_female:
    $ master.set_flag("interact", 1, 1, "+")
    show master at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call master_belly_kiss_female from _call_master_belly_kiss_female_1
        "Caress my belly":
            call master_belly_caress_female from _call_master_belly_caress_female_1
        "Listen to the baby":
            call master_belly_listen_female from _call_master_belly_listen_female_1
        "Never mind":
            pass
    return

label master_belly_caress_female:
    show master happy at center, zoomAt(1.5, (640, 1040))
    "It's not hard to spot the interest that the Master seems to be showing in my swollen belly."
    "I mean he seems to spend most of his time staring at the opposite sex anyway."
    "But right now the only thing he has eyes for is the bulge that's sticking out in front of me."
    "Whenever I look in his direction, he all but confirms my suspicions too."
    "Because he's quick to look away and pretend to be interested in anything else nearby."
    bree.say "Master..."
    bree.say "You do know that you don't need to pretend, right?"
    "The old man instantly falls back on his usual tactic of looking surprised when I speak to him."
    "In fact he seems to be putting in a little too much effort, as he practically leaps up into the air."
    show master surprised at startle
    master.say "What?"
    master.say "What was that?"
    master.say "I have no idea what you're talking about!"
    show master normal
    "Even as he's saying all of this, I can see where his eyes are going."
    "He's trying to hold my eye, but his are visibly creeping downwards."
    "And every time he realises this, he drags them back up again."
    bree.say "I really don't know why you're making such a fuss about it."
    bree.say "I mean, it's not like I haven't been showing it off since I got pregnant."
    bree.say "And if you want to touch it, all you have to do is ask."
    "I underline my point by thrusting my belly in his general direction."
    show master happy at center, traveling(1.25, 0.3, (640, 880))
    "Which is more than enough to make the Master leap back again."
    show master happy
    master.say "Oh..."
    master.say "I...I didn't want to just touch it, my dear."
    master.say "I wanted to offer you the benefit of my esoteric talents."
    show master normal
    bree.say "Esoteric what-now?!?"
    show master happy
    master.say "A massage that will harness your chi and align your chakras."
    master.say "Plus it's good for your back and feet too."
    master.say "Which I hear pregnant women are martyrs to?"
    show master normal
    "I nod eagerly, because he's not wrong."
    "And this seems to be what the old man was wanting to hear."
    show master happy at center, traveling(1.5, 0.3, (640, 1040))
    "Because a moment later he puts his hands on my bump."
    "Then he proceeds to perform what I suppose is a massage, at least in his book."
    "In reality it feels more like a prolonged session of just caressing my belly."
    "Which is totally fine with me, as that's what I thought he wanted to do in the first place."
    "So in the end, everyone is happy."
    $ master.love += 2
    return

label master_belly_kiss_female:
    show master happy at center, zoomAt(1.5, (640, 1040))
    master.say "My dear..."
    master.say "I was just wondering if I could kiss you?"
    show master normal
    "I look up with surprised written all over my face as I hear the Master's words."
    "It's not that the suggestion is a crazy one or something that I've never heard him ask of me before."
    "No, what makes me pause is more the fact that he's asking in such an oddly formal way, even for him."
    bree.say "Erm..."
    bree.say "Of course you can, Master."
    bree.say "All you have to do is ask."
    "The old man looks at me with an expectant expression on his face."
    show master happy
    master.say "Well?"
    show master normal
    bree.say "Well what?"
    show master happy
    master.say "Well I did already ask!"
    show master normal
    bree.say "Oh yeah..."
    bree.say "I guess you did!"
    "I feel like such a dumbass for not picking up on that."
    scene expression f"bg {game.room}" at blur(16), dark, dark with wipedown
    "And so in my hurry to make up for it, I close my eyes and pucker my lips."
    "Then I stand there, waiting for the Master to make the most of the offer."
    "But as the seconds pass, nothing seems to be happening."
    "That is until I feel the sensation of something against my belly."
    "Then there's the unmistakable sound of someone smacking their lips."
    scene expression f"bg {game.room}"
    show master at center, zoomAt(2.5, (640, 1940))
    with wipeup
    "Opening my eyes and looking down, I see the Master on his knees in front of me."
    "I watch in amazement as he plants one kiss after another on the curve of my belly."
    "And my first instinct is to open my mouth and ask him what the hell he's doing."
    "But then I remember that he never expressly stated where he wanted to kiss me."
    "And the sensation of his lips on my belly is actually quite pleasant."
    "So instead of speaking up, I decide to just leave him to it."
    "The Master seems to be totally tied up in the task, not showing any sign of stopping."
    "Part of me wonders if he's going to plant a kiss on every square inch of my belly."
    "And I kind of wish there was a way that I could tell how close he's coming to that."
    $ master.love += 3
    return

label master_belly_listen_female:
    show master happy at center, zoomAt(1.5, (640, 1040))
    master.say "Would you mind taking off your top, my dear?"
    master.say "I want to do something to you..."
    master.say "And it's getting in the way!"
    show master normal
    "I have to stop and go back over what the Master just said to me."
    "Because the first time I ran it through my brain, it didn't make sense."
    bree.say "Wait a minute..."
    bree.say "Did I just hear you right?"
    bree.say "You want me to take my top off?"
    "The Master nods happily."
    show master happy
    master.say "That's right, my dear."
    master.say "Or else just lift it up a way?"
    master.say "Otherwise I can't get to your belly."
    show master normal
    "I look at him blankly for a moment, again trying to understand what he wants."
    bree.say "My belly?"
    bree.say "I thought..."
    bree.say "I thought you were asking me to get naked or something!"
    show master surprised
    "The Master looks at me in genuine surprise."
    master.say "Why..."
    master.say "There's no need for that!"
    show master happy
    master.say "I only wanted to listen to your belly, my dear."
    master.say "But if you'd prefer to be naked..."
    show master normal
    "I'm already shaking my head as he says this."
    "And I'm lifting the hem of my top too."
    bree.say "No, no..."
    bree.say "Just popping my belly out will be fine!"
    "The old man shrugs and seems to be happy letting the matter drop."
    "Instead he prepares himself for the task at hand."
    show master at center, traveling(2.5, 0.3, (640, 1940))
    "I watch with genuine interest as he leans his head closer."
    "And then he places his ear against the curve of my belly."
    bree.say "So..."
    bree.say "You really think you'll be able to hear something?"
    show master upset
    "The Master makes an irritable tutting sound in response to my question."
    "And he waves a hand in the air at the same time, scolding me for distracting him."
    show master normal
    "Suitably chastened, I shut my mouth and resign myself to just watching."
    show master happy
    master.say "Ooh..."
    master.say "There you are!"
    master.say "Now, what are you up to, you little tyke!"
    "I can't help beginning to smile as the Master follows whatever he can hear."
    "The old man shifts from side to side and up and down as he follows the baby."
    "All the time he's chuckling to himself and nodding happily."
    "Which I guess means that he likes the sound of what he's hearing."
    $ master.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
