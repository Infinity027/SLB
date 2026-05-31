label camila_ice_cream_reaction_male:
    mike.say "Whoa...I can't take much more of this heat, Camila!"
    mike.say "Let's go grab an ice cream to cool down, yeah?"
    camila.say "Nah, I' already cool enough - but don't let me stop you."
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "I hold it up, trying to make Camila change her mind."
    "But she doesn't take the bait, shaking her head and smiling in response."
    "All of this means I feel a little awkward eating an ice cream on my own."
    "But I try my best to hide the feeling, smiling back at Camila as I lick away."
    camila.say "You weren't kidding when you said you wanted an ice cream!"
    camila.say "Kinda makes me wonder what else you'd lick like that!"
    "The moment I realise what Camila's implying, I feel my cheeks flush red."
    return

label camila_ask_phone_male:
    mike.say "Camila, I was wondering..."
    mike.say "Could I get your number?"
    if hero.charm >= 20 - camila.love:
        show camila happy
        $ hero.smartphone_contacts.append("camila")
        camila.say "Yeah, [hero.name], here you go."
        camila.say "And that's my personal number too."
        camila.say "NOT my work number, okay?"
    else:
        show camila annoyed
        $ camila.love -= 1
        $ camila.sub -= 1
        camila.say "I don't give out my personal number, [hero.name]."
        camila.say "Sorry, it's just a cop thing."
    return

label camila_ask_birthday_male:
    mike.say "I wondered about your birthday, Camila."
    mike.say "You never told me when it was?"
    if hero.charm >= 40 - camila.love:
        show camila happy
        $ camila.flags.birthdayknown = True
        camila.say "Tell you what, [hero.name], you've got my card already."
        camila.say "So I'll write it on the back, okay?"
        camila.say "That way you'll always have it to hand - there you go, Winter 3."
    else:
        show camila annoyed
        $ camila.sub -= 1
        $ camila.love -= 1
        camila.say "Hey - never ask a woman that!"
        camila.say "I'm not even that old."
        camila.say "This job takes it's toll, that's all!"
    return

label camila_offer_a_drink_male:
    mike.say "I need to grab another beer."
    mike.say "How about I get you one too, Camila?"
    "Almost the second the words are out of my mouth, Camila turns to face me."
    if camila.is_visibly_pregnant:
        show camila angry
        $ camila.love -= 10
        camila.say "Don't you think this kid of ours has it hard enough?"
        camila.say "They've already got a mom with a dangerous job."
        camila.say "The last thing they need is for me to soak them in booze too!"
        $ hero.cancel_activity()
        hide camila
    elif (hero.charm >= 60 - camila.love and camila.flags.drinks < 2) or date_girl == camila:
        show camila happy
        camila.say "After my last shift, I need as much booze as I can get!"
        camila.say "Make mine a whiskey, and don't be stingy with the size either."
        hide camila
        show drink camila
        if camila.love <= 25:
            $ camila.love += 1
        elif date_girl == camila and game.active_date:
            $ game.active_date.score += 5
        call expression camila.get_chat from _call_expression_218
        hide drink camila
        $ camila.set_flag("drinks", 1, "day", mod="+")
    else:
        show camila annoyed
        camila.say "Geez, [hero.name], I'm back on shift in a couple of hours!"
        camila.say "What are you trying to do - get me kicked off the force?"
        $ hero.cancel_activity()
        hide camila
    return

label camila_slap_ass_intro_male:
    "Normally I'd be scared stiff of doing something like this."
    "The very idea of slapping Camila's ass is tinged with danger."
    "But the way that her backside is moving right now..."
    "Maybe the punishment would be worth it for the sake of the crime?"
    return

label camila_slap_ass_happy_male:
    camila.say "Wha..."
    camila.say "What the hell?!?"
    "Camila spins around and catches me in the act."
    "Her eyes are full of indignation and anger."
    "But there's also disbelief in them too."
    camila.say "Oh, I see how it is, [hero.name]!"
    camila.say "You wanna play good cop, bad cop!"
    camila.say "Well, I get to be BAD cop!"
    return

label camila_slap_ass_angry_male:
    camila.say "Wha..."
    camila.say "What the hell?!?"
    "Camila spins around and catches me in the act."
    "Her eyes are full of indignation and anger."
    "But there's also disbelief in them too."
    camila.say "You should never strike an officer of the law, [hero.name]."
    camila.say "You could end up getting pepper-sprayed."
    camila.say "Or worse..."
    return

label camila_breakup_male:
    show camila
    "It's hard enough to find the courage to tell a girl that you want to end it with her."
    "But when the girl in question just so happens to be a super-tough cop..."
    "Well, then you have the fear that she'll kick your ass for your trouble too!"
    "But I can't just smile and pretend everything's cool with Camila and me."
    "So I have to swallow my fears and face up to telling her the bad news."
    mike.say "Camila..."
    mike.say "Here's the thing..."
    "Almost the same moment that I begin to speak, Camila turns to face me."
    "That's what makes me trail off before actually telling her I want to break up."
    "She's looking at me with that serious, hardened cop face that she has."
    camila.say "Hmm..."
    camila.say "Come on then, [hero.name]."
    camila.say "Out with it."
    "Suddenly I feel like I'm in the interview room, being grilled hard."
    "I swallow nervously, looking this way and that."
    "But Camila just keeps right on staring at me, looking into my very soul."
    "And I can see that there's no way of escaping her gaze."
    mike.say "It's about us, Camila."
    mike.say "You and me."
    mike.say "I don't think I want to do this anymore..."
    show camila annoyed
    "I only just manage to keep from wincing as I admit the truth."
    "I know deep down that Camila won't lash out at me."
    "Sure, she's a tough cop - but she's not a rotten one."
    "And in the end, all I see is a slight flicker in her face."
    "Maybe a twitch of her eye as she fights to keep herself under control."
    camila.say "Let me get this straight, [hero.name]."
    camila.say "You want to dump me?"
    camila.say "Even after all that we've been through together?"
    mike.say "I...I know how it looks, Camila."
    mike.say "And I'm still grateful for all that you did to help me."
    mike.say "But I can't ignore my feelings."
    mike.say "And I don't want to lie to you either!"
    "Camila's stare seems to soften for a moment."
    "And it seems that I've managed to reach her with my words."
    "But then she stiffens, and the tough cop mask is back on her face again."
    camila.say "Whatever, [hero.name]."
    camila.say "I don't need your pity."
    camila.say "And if you need to call the police anytime in the future..."
    camila.say "Well, you be sure to ask for anyone else but me."
    camila.say "Because I never want to see you again!"
    return

label camila_go_steady_intro_male:
    mike.say "I've been thinking, Camila..."
    mike.say "We really should go steady."
    mike.say "It makes sense, yeah?"
    return

label camila_go_steady_yes_male:
    camila.say "Why didn't I think of that myself, [hero.name]?!?"
    camila.say "Of course we should."
    camila.say "Consider us official!"
    "Camila underlines the point by punching me on the arm."
    "Sure, it hurts - but I smile through the pain."
    return

label camila_go_steady_no_male:
    camila.say "Whoa!"
    camila.say "Slow down there, [hero.name]."
    camila.say "You're still a rookie to my hardened veteran!"
    return

label camila_pet_intro_male:
    "I regret it the moment that the palm of my hand touches Camila's head."
    "But by then, it's too late to take it back or claim it was a mistake."
    "I just patted a tough cop on the head, and now I'm facing the consequences!"
    return

label camila_pet_happy_male:
    camila.say "Wha..."
    camila.say "That...feels so good, [hero.name]!"
    camila.say "That means I'm a good girl, right?!?"
    return

label camila_pet_annoyed_male:
    camila.say "Whoa..."
    camila.say "You've got some balls on you, Mister!"
    camila.say "But do that again, and you sure as hell won't!"
    return

label camila_massage_intro_male:
    mike.say "You must have had a hard day on the beat, Camila."
    mike.say "Your muscles are like a bunch of rocks!"
    mike.say "Would you like me to give you a massage?"
    return

label camila_massage_accept_male:
    camila.say "You know what, [hero.name], that sounds kinda nice."
    camila.say "Just be careful to work my scars too."
    camila.say "Because they can get real sore!"
    return

label camila_massage_refuse_male:
    camila.say "Nah, I can handle it, [hero.name]."
    camila.say "You gotta be tough in this job."
    camila.say "Massages aren't gonna fix anything!"
    return

label camila_piercing_nipples_reaction_male:
    camila.say "Huh...I was worried this would be too girly for me."
    camila.say "But now I've had my nipple pierced...well..."
    camila.say "It feels really hot!"
    return

label camila_piercing_navel_reaction_male:
    camila.say "I'm kinda glad this is going to be covered up when I'm on duty."
    camila.say "But other than that, I really love it!"
    camila.say "Thanks for talking me into it, [hero.name]."
    return

label camila_piercing_clit_reaction_male:
    camila.say "Oh fuck..."
    camila.say "I can feel this thing rubbing on my clit when I walk!"
    camila.say "It feels so good...I just hope I can keep my mind on the job!"
    return

label camila_piercing_head_reaction_male:
    camila.say "Geez...I'm gonna have to keep my tongue in my mouth while I'm on duty!"
    camila.say "But that's just kind of a given, yeah?"
    camila.say "Truth is, I really love the feel of this thing!"
    return

label camila_piercing_nose_reaction_male:
    camila.say "You know, I wasn't sure at first."
    camila.say "But now I'm looking at it...and I like it."
    camila.say "This thing is pretty bad-ass!"
    return

label camila_movie_disliked_reaction_male:
    camila.say "Ah...I have to confess, I hated that film - it was awful!"
    return

label camila_movie_indifferent_reaction_male:
    camila.say "That film was boring, like being on a stakeout where there's no action!"
    return

label camila_movie_liked_reaction_male:
    camila.say "That movie had everything, it was SO great - I can't wait to see it again!"
    return

label camila_belly_kiss_male:
    show camila talkative at center, zoomAt(1.25, (640, 880))
    camila.say "[hero.name]…"
    camila.say "You know that I can see you, right?"
    camila.say "And that I know exactly what you're thinking too?"
    show camila normal with vpunch
    "At the sound of Camila's voice, I almost jump out of my skin."
    "And I go and make things worse for myself by instantly starting to deny everything."
    "Which is obviously the perfect way to make myself look totally guilty in her eyes."
    mike.say "Huh?"
    mike.say "What are you talking about, Camila?"
    mike.say "I have no idea what you could possibly mean!"
    show camila annoyed
    "Camila fixes me with one of her hardest stares."
    "The kind that are almost guaranteed to make me start sweating on the spot."
    "And at the same time she points to her bump."
    show camila talkative
    camila.say "You were looking at this, weren't you?"
    camila.say "Staring at my belly with one thing in mind."
    camila.say "Just wanting to bend down and kiss it, aren't you?"
    show camila annoyed
    "I think about keeping on denying the accusation."
    "But the truth of the matter is that Camila's onto me."
    "And she's way more experienced when it comes to interrogation."
    "She's sure to get a confession out of me with no effort at all."
    "So what's the point in even trying to deceive her?"
    mike.say "Okay, Camila..."
    mike.say "You got me."
    mike.say "I want to kiss it real bad!"
    show camila normal
    "Camila narrows her eyes as I confess everything to her."
    "And then she does something that I wasn't expecting at all."
    show camila at center, traveling(2.0, 0.5, (640, 980))
    "She pulls up her shirt, and thrusts her belly towards me."
    show camila talkative
    camila.say "Okay then..."
    show camila happy
    camila.say "Get on with it already."
    camila.say "But you'd better make me believe that you mean it!"
    show camila normal
    "For a moment I'm sure that Camila can't be serious."
    "That she must be trying to trick me somehow."
    "But then she almost barges her stomach into me."
    "And that's enough to spur me into action."
    "Getting down on my knees, I take her belly in both hands."
    "Then I plant my lips on it, kissing away for all I'm worth."
    "Camila looks down over the curve of her belly as I do so."
    "Nodding and smiling in approval at my efforts."
    "Not that I'm having to fake the enthusiasm at all."
    "Her belly feels so good in my hands, so right."
    "And kissing it makes me feel happy in a way that's hard to explain."
    "Almost like I'm holding the key to our happiness in my hands the whole time."
    return

label camila_belly_caress_male:
    show camila upset at center, zoomAt(1.25, (640, 880))
    "I can see that Camila's getting into that mood again."
    "The one where she starts acting like a bear with a sore head."
    "And I start to worry that she's going to end up shooting someone."
    mike.say "Erm..."
    mike.say "How are you doing, Camila?"
    mike.say "You remember what the doctor said about relaxing, right?"
    show camila at startle
    "At the sound of my voice, Camila's head spins around."
    "And she fixes me with a really mean stare."
    "Seriously, it's the kind that I've seen her give to actual criminals while on the beat!"
    show camila angry
    camila.say "What in the hell is that supposed to mean, huh?"
    camila.say "Are you trying to say that I'm stressed?"
    camila.say "That I can't handle being pregnant?"
    show camila upset
    "I'm shaking my head and doing all I can to deflect the accusation."
    "All while wondering if Camila has her side-arm in the house and within easy reach."
    mike.say "No, Camila..."
    mike.say "I...I..."
    show camila angry
    camila.say "Because if you are..."
    show camila whining
    camila.say "Then you're totally right!"
    camila.say "Urgh...I'm a mess!"
    show camila sad
    "I stand there in amazement as I watch Camila melt into a flood of tears."
    "She's literally the toughest woman that I've ever met in my entire life."
    "And now there are tears streaming down her cheeks."
    show camila whining
    camila.say "[hero.name]…"
    camila.say "I can't handle this!"
    show camila sad at center, traveling(1.75, 0.5, (640, 1190))
    "Without stopping to think, I hurry over to Camila."
    "And I don't hesitate to throw my arms around her."
    "She collapses against my shoulder, still sobbing and blubbering."
    "Then she thrusts her swollen belly towards me, pointing down at it."
    show camila whining
    camila.say "This is worse than any punk I ever had to bust..."
    camila.say "Way scarier too!"
    show camila sad
    "Instinctively I reach out with a hand, placing it on Camila's belly."
    "And then I start to stroke the curve, loving the feel of it against my palm."
    mike.say "Yeah, Camila, I know it is."
    mike.say "But you've got a partner in this, just like you do at work."
    mike.say "You and me, we're a team, yeah?"
    show camila normal
    "Camila looks up at me, a smile on her face."
    "And she nods as she begins to wipe away the tears."
    show camila sadsmile
    camila.say "I'm sorry, [hero.name]…"
    camila.say "I've gone all soft and emotional!"
    mike.say "No need to apologise, Camila."
    mike.say "I'm sure you'll be back to being tougher than me soon enough."
    return

label camila_belly_listen_male:
    show camila angry at center, zoomAt(1.25, (640, 880))
    camila.say "Hey, [hero.name]…"
    camila.say "Get over here and help me with something, yeah?"
    show camila annoyed
    "Camila's using the tone of voice that I remember hearing most when she's on duty."
    "The commanding one that lets you know there's no real point in trying to say no."
    "Because she's going to get what she wants, one way or another."
    "So the most sensible thing to do is just nod, smile and give her whatever she wants."
    show camila at center, zoomAt(1.5, (640, 1040))
    mike.say "Sure thing, Camila..."
    mike.say "What's up?"
    "As soon as I make it over to Camila, she gets right down to business."
    "Which seems to involve pulling up her top and thrusting out her belly."
    "In fact she thrusts it right into the palms of my outstretched hands."
    show camila talkative
    camila.say "Get in real close and have a listen, yeah?"
    camila.say "I want to know what's going on in there!"
    show camila normal
    "I can't help giving Camila a puzzled look at this."
    "Something that I know isn't going to go down well."
    "But I feel like the request is so weird that I have to be honest."
    mike.say "You want me to do what?"
    show camila talkative
    camila.say "To listen to my belly, then tell me what you hear."
    show camila angry
    camila.say "Geez, [hero.name]…"
    camila.say "What's so strange about that?"
    show camila annoyed
    mike.say "I dunno, Camila..."
    mike.say "Maybe that you make it sound like some kind of stakeout?"
    mike.say "I mean what do you think the baby's going to be doing in there anyway?"
    show camila normal at stepback(speed=0.1, h=-10, v=-20)
    "Camila frowns and makes to pull her belly away from me."
    show camila whining
    camila.say "Well if that's how you're going to be..."
    camila.say "Maybe I don't want your help after all!"
    show camila annoyed
    "I can't help tightening my grip on her belly as she says this."
    show camila at center, traveling(2.0, 0.5, (640, 980))
    "That and beginning to get down on one knee to do as she asks."
    "Because I'd rather make a fool of myself than have Camila think I'm not helping."
    mike.say "Okay, okay..."
    mike.say "Just let me get into position, yeah?"
    "I see a knowing smile spread across Camila's face."
    "The kind that she gets when she's sure that means she knows she's in control."
    "Camila raises an eyebrow and nods too, giving me permission to do what she wants me to do anyway."
    "Putting my ear against her belly, I struggle to make out the sounds coming from within."
    camila.say "Well?"
    camila.say "What can you hear?"
    mike.say "Oh man..."
    mike.say "This is pretty wild!"
    camila.say "What?"
    show camila annoyed
    camila.say "What is?!?"
    mike.say "It sounds like..."
    mike.say "Like he's on a police radio, issuing an APB!"
    "I feel Camila's hand slap me on the side of the head before she starts telling me off."
    "But it's worth the slap for the sake of winding her up like that!"
    show camila happy
    camila.say "[hero.name]!"
    camila.say "Can't you be serious for five seconds?!?"
    mike.say "What do you want me to say, Camila?"
    mike.say "It sounds like the baby is moving around in there, that's all!"
    camila.say "Then why not just say that?"
    mike.say "Well, because it's funnier this way!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
