label kleio_ice_cream_reaction_male:
    mike.say "It's too darn hot today, Kleio - I could use an ice cream to cool down!"
    kleio.say "You said it, Loverboy - let's go get some!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Kleio chooses the same thing, but she opts for chocolate ice cream on hers."
    kleio.say "Argh...what the...will you look at that!"
    "At the sound of Kleio's exclamations, I turn to look in her direction."
    "She's holding up her cone as the ice cream is already starting to melt."
    "It's running down her wrist and arm, even as she tries to lap it up with her tongue."
    "I'm afraid that she's going to see me and notice that I'm staring."
    "But I can't tear my eyes away from the sight of Kleio working her tongue like that!"
    return

label kleio_ask_phone_male:
    mike.say "How about we swap numbers, Kleio?"
    mike.say "I don't have yours in my phone yet."
    if hero.charm >= 20 - kleio.love:
        show kleio happy
        $ hero.smartphone_contacts.append("kleio")
        kleio.say "You don't?"
        kleio.say "Well, we can't have that, can we, Loverboy!"
        kleio.say "There you go."
    else:
        show kleio annoyed
        $ kleio.love -= 1
        $ kleio.sub -= 1
        kleio.say "Yeah, thing is, Loverboy..."
        kleio.say "If it's not in there it's because I don't want it to be!"
    return

label kleio_ask_birthday_male:
    mike.say "Hey, Kleio - your birthday, yeah?"
    mike.say "When in the hell is it?"
    if hero.charm >= 40 - kleio.love:
        show kleio happy
        $ kleio.flags.birthdayknown = True
        kleio.say "Winter 16, like it's always been."
        kleio.say "So remember that date, Loverboy."
        kleio.say "And you better get me something good for a present too!"
    else:
        show kleio annoyed
        $ kleio.sub -= 1
        $ kleio.love -= 1
        kleio.say "How about I don't tell you at all?"
        kleio.say "That way I can keep you on your toes, Loverboy!"
    return

label kleio_offer_a_drink_male:
    mike.say "Hey, Kleio..."
    mike.say "I want another beer."
    mike.say "Should I grab one for you too?"
    "Almost the second the words are out of my mouth, Kleio turns to face me."
    if kleio.is_visibly_pregnant:
        show kleio angry
        $ kleio.love -= 10
        kleio.say "You already knocked me up, you jerk!"
        kleio.say "Now you're trying to screw the baby up too?!?"
        $ hero.cancel_activity()
        hide kleio
    elif (hero.charm >= 60 - kleio.love and kleio.flags.drinks < 2) or date_girl == kleio:
        show kleio happy
        kleio.say "Sounds good to me, Loverboy."
        kleio.say "Like you read my mind!"
        hide kleio
        show drink kleio
        if kleio.love <= 25:
            $ kleio.love += 1
        elif date_girl == kleio and game.active_date:
            $ game.active_date.score += 5
        call expression kleio.get_chat from _call_expression_243
        hide drink kleio
        $ kleio.set_flag("drinks", 1, "day", mod="+")
    else:
        show kleio annoyed
        kleio.say "Like I need you to buy me a beer, Loverboy!"
        kleio.say "I can handle myself and the beer too!"
        $ hero.cancel_activity()
        hide kleio
    return

label kleio_slap_ass_intro_male:
    "My eyes keep getting drawn to Kleio's ass."
    "It's just so tight and pert - I can't stop staring at it!"
    "I know that Kleio's a pretty feisty, modern girl."
    "But something deep down in me makes want to slap that ass."
    "Who knows, maybe she'll see it as ironic?"
    return

label kleio_slap_ass_happy_male:
    kleio.say "Wha..."
    kleio.say "What in the hell was that?!?"
    "It doesn't take long for Kleio to figure out what just happened."
    "And then she fixes me with a hard stare, eyes drilling into my brain."
    kleio.say "You just slapped my ass, didn't you?"
    "All I can do is nod."
    kleio.say "That means I get to slap yours too, Loverboy!"
    return

label kleio_slap_ass_angry_male:
    kleio.say "Wha..."
    kleio.say "What in the hell was that?!?"
    "It doesn't take long for Kleio to figure out what just happened."
    "And then she fixes me with a hard stare, eyes drilling into my brain."
    kleio.say "You just slapped my ass, didn't you?"
    "All I can do is nod."
    kleio.say "What do you think I am, [hero.name] - a piece of meat?!?"
    kleio.say "Do it again and I'll break your damn arm!"
    return

label kleio_breakup_male:
    show kleio
    "I can almost feel myself wincing as I get ready to say what I have to say."
    "But I know that there's no way I can get away without actually saying it."
    "Sure, it's not a fun thing to admit, and it makes me feel like a jerk."
    "But there's no way I can carry on without getting it out there."
    mike.say "Kleio..."
    mike.say "I think we need to talk..."
    mike.say "Well, I need to talk to you..."
    mike.say "That is I..."
    "Kleio cocks her head on one side as she looks at me."
    "At first she has a confused look on her face."
    "But as I stutter and stammer away, that soon begins to change."
    "Before too long, she's nodding and rolling her eyes."
    "And then she holds up a hand to stop me talking."
    show kleio annoyed
    kleio.say "Hold on a minute, Loverboy."
    kleio.say "I've been around the block more than once, yeah?"
    kleio.say "And I think I know the tune you're trying to play!"
    kleio.say "We're headed for dumpsville, right?"
    kleio.say "Population me!"
    "For a moment my mouth keeps on moving, but no words come out."
    "Then I stop trying to speak and just nod, which seems to help."
    mike.say "I...I know it sucks, Kleio."
    mike.say "But I want to be honest with you."
    mike.say "I just don't think it's working out between us."
    "Kleio groans and pushes her hand through her hair."
    show kleio angry
    kleio.say "You're damn right it sucks, Loverboy!"
    kleio.say "I went out on a limb for you, opened myself up to you."
    kleio.say "And all that's got me is used up and tossed aside!"
    mike.say "It's not like that, Kleio!"
    kleio.say "Hey, don't you do that, [hero.name]!"
    kleio.say "Don't you try to tell me how I feel!"
    kleio.say "Urgh...men!"
    kleio.say "I should SO have stuck to girls!"
    mike.say "Kleio, I..."
    kleio.say "Ah, save your breath, [hero.name]."
    kleio.say "Save it for someone who gives a damn!"
    return

label kleio_go_steady_intro_male:
    mike.say "Hey, Kleio, why don't we go steady?"
    mike.say "I mean, I know you're not into all that traditional stuff..."
    mike.say "But we could call it something else maybe?"
    return

label kleio_go_steady_yes_male:
    kleio.say "Enough with the mushiness, Loverboy!"
    kleio.say "We can just say it's official, yeah?"
    hide kleio
    show kleio kiss
    $ kleio.flags.kiss += 1
    "Kleio makes her point by grabbing my collar."
    "And then she yanks me in for a kiss on the lips."
    return

label kleio_go_steady_no_male:
    kleio.say "Urgh..."
    kleio.say "You know I hate it when you're all mushy, Loverboy!"
    kleio.say "And I don't think we're quite there yet..."
    return

label kleio_pet_intro_male:
    "Without thinking, I reach out and pat Kleio on the head."
    "The second I realise what I've done, I start to panic."
    "What in the hell was I even thinking?!?"
    return

label kleio_pet_happy_male:
    kleio.say "You wanna toss me a bone too, Loverboy?"
    kleio.say "You know you're lucky I like you so much."
    kleio.say "Otherwise I'd never let you get away with shit like that!"
    return

label kleio_pet_annoyed_male:
    kleio.say "Oh, hell no!"
    kleio.say "No fucking way!"
    kleio.say "You do that to me again, Loverboy, and you're dead meat!"
    return

label kleio_massage_intro_male:
    mike.say "Ooh..."
    mike.say "Your muscles look all tight and knotted, Kleio!"
    mike.say "You know what might help?"
    mike.say "Me giving you one of my patented miracle massages!"
    return

label kleio_massage_accept_male:
    kleio.say "You know what, Loverboy..."
    kleio.say "That does sound like a pretty good idea!"
    kleio.say "Come over here and put your hands all over me..."
    return

label kleio_massage_refuse_male:
    kleio.say "Jesus, Loverboy..."
    kleio.say "The last thing I need right now is your hands all over me!"
    kleio.say "Knowing you, I'll be snarled up worse than I was when you started!"
    return

label kleio_piercing_nipples_reaction_male:
    kleio.say "Well, what do ya reckon, Loverboy?"
    kleio.say "I know they're not the first one's I ever got."
    kleio.say "But they sure do make my nipples look good."
    kleio.say "And there's still plenty of room for more too!"
    return

label kleio_piercing_navel_reaction_male:
    kleio.say "I shoulda had this done years ago."
    kleio.say "My belly-button was made for this shit!"
    kleio.say "Thanks for nudging me in the right direction, Loverboy!"
    return

label kleio_piercing_clit_reaction_male:
    kleio.say "Mmm..."
    kleio.say "I just love the way this thing makes me feel down there!"
    kleio.say "I'm getting hot just thinking about it!"
    kleio.say "Thanks for giving me the idea, Loverboy."
    return

label kleio_piercing_head_reaction_male:
    kleio.say "People are always telling me my tongue's gonna get me into trouble."
    kleio.say "But you're the only person that ever wanted me to make more of it."
    kleio.say "So I guess that means you like what I do with it, Loverboy!"
    return

label kleio_piercing_nose_reaction_male:
    kleio.say "Yeah, this is SO rock n' roll!"
    kleio.say "I feel like I'm in the fucking Sex Pistols!"
    kleio.say "Great idea, Loverboy!"
    return

label kleio_movie_disliked_reaction_male:
    kleio.say "Jesus wept - that was a massive pile of shit!"
    return

label kleio_movie_indifferent_reaction_male:
    kleio.say "Well, that was enough to bore me to tears!"
    return

label kleio_movie_liked_reaction_male:
    kleio.say "WOW...I mean, just WOW - that was something else!"
    return

label kleio_belly_kiss_male:
    show kleio annoyed at center, zoomAt(1.25, (640, 880))
    "I can tell that Kleio's feeling a little bit needy today."
    "But I also know that she's not the kind of girl to admit as much."
    "So I have to put up with some passive aggressive pouting for a while."
    "At least until I can spare the time to do something about it."
    mike.say "Hmm..."
    mike.say "I knew there was something that I'd forgotten to do."
    show kleio normal
    "At the sound of my voice, Kleio looks up."
    "Her expression letting me know that I've piqued her interest."
    show kleio talkative
    kleio.say "Huh?"
    kleio.say "What did you forget?"
    show kleio normal
    "I kind of half ignore Kleio as I walk over to where she's sitting."
    show kleio at center, traveling(1.5, 5.0, (640, 1040))
    "But I keep on talking, making it sound like I'm still really talking to myself."
    mike.say "How could I forget about that one person in my life?"
    mike.say "The one person that's always on my mind?"
    show kleio upset
    "By now, Kleio's eyes are focussed on me like a pair of laser-beams."
    "She's nodding her head, visibly willing me to say more."
    show kleio talkative
    kleio.say "Yeah..."
    kleio.say "And that person would be?"
    kleio.say "Would be who, exactly?"
    show kleio upset
    "By now I'm standing right in front of Kleio."
    show kleio b stuned
    "And she's looking up at me expectantly."
    "Though I've made a point of not looking her in the eye yet."
    "Then I part my hands, like I'm going to embrace her any moment."
    "And as I step forwards, Kleio does the same."
    show kleio b surprised at center, traveling(2.0, 1.0, (640, 980))
    "But then she's taken by surprise as I sink down onto one knee."
    "She looks down just in time to see me embrace her belly."
    mike.say "Ah..."
    mike.say "My beloved, unborn child!"
    show kleio b normal
    kleio.say "Erm, Loverboy..."
    show kleio b seductive
    kleio.say "Did I ever tell you that you're a fucking asshole?"
    mike.say "Well, yeah, Kleio..."
    mike.say "Pretty often, actually!"
    return

label kleio_belly_caress_male:
    show kleio b happy at center, zoomAt(1.25, (640, 880))
    kleio.say "Hey, Loverboy..."
    kleio.say "Get a load of this!"
    mike.say "Huh..."
    mike.say "What the..."
    show kleio b surprised at center, traveling(2.0, 1.0, (640, 980))
    "I look up just in time to see something huge, round and pink looming over me."
    "And then it closes in, slamming straight into my face and totally smothering me."
    mike.say "Mmmph..."
    mike.say "Urgh..."
    mike.say "Kleio..."
    mike.say "That can't be good for the baby!"
    "Of course the huge pink thing is Kleio's belly."
    "Which by now is so big she looks like she's about to pop."
    "And she's making no effort to cover it up either."
    "Still wearing cropped tops that allow it to stick out in front of her."
    "But rather than seeing it as an affront, Kleio seems to revel in it."
    "And she takes every opportunity she can to shove it in my face, like just now."
    show kleio b talkative
    kleio.say "Ah, lighten up already!"
    kleio.say "We're gonna be up to our armpits in shitty nappies soon enough."
    kleio.say "You should have fun while you still got the chance."
    show kleio b normal
    "I'm standing up and shoving Kleio's belly out of my face."
    "But I'm also thinking about what she's saying."
    "And I guess that she really does have a point."
    mike.say "You know what, Kleio..."
    mike.say "You're right."
    "I put my hands on her belly and gently stroke it as I speak."
    mike.say "And when am I going to get a chance to do this again?"
    "Kleio gives me a quizzical look."
    show kleio b surprised
    kleio.say "Huh?"
    kleio.say "To do what?"
    mike.say "To date a human beach-ball, what else?"
    show kleio b punk
    "I manage to duck the first slap from Kleio."
    "But the second one catches me on the way back."
    show kleio b happy
    "Though I can hear her laughing all the same."
    "So I know that she really does appreciate the joke."
    return

label kleio_belly_listen_male:
    show kleio talkative at center, zoomAt(1.25, (640, 880))
    kleio.say "Hey, Loverboy..."
    kleio.say "Get over here and help me with your kid!"
    show kleio normal
    "Naturally my ears prick up as soon as Kleio mentions the baby."
    show kleio at center, traveling(1.5, 0.3, (640, 1040))
    "And I hurry over to her as quickly as I can."
    mike.say "What's the matter, Kleio?"
    mike.say "Is the baby okay?"
    mike.say "Do you need me to run you to the hospital?"
    show kleio stuned
    "Kleio looks at me like I have steaming turds hanging out of my mouth."
    "And she shakes her head, like I'm some kind of moron."
    show kleio surprised
    kleio.say "What?"
    show kleio talkative
    kleio.say "No, you dumbass!"
    kleio.say "I want you to listen to what they're doing in there."
    show kleio happy
    kleio.say "I swear the little bastard is farting!"
    show kleio normal
    "Now it's my turn to look at Kleio like she's talking shit."
    mike.say "You think the baby's breaking wind?"
    mike.say "Can they even do that?!?"
    "Kleio shakes her head and points at her bump."
    show kleio annoyed
    kleio.say "Do I look like a doctor?"
    kleio.say "How the fuck would I know?!?"
    show kleio talkative
    kleio.say "I just keep feeling something going on in there."
    kleio.say "And it feels like farting in the bath!"
    kleio.say "Like underwater!"
    show kleio normal
    "I feel like there's a whole other conversation to be had right there."
    "But for the moment I do the best I can to stop thinking about it."
    show kleio b at center, traveling(2.0, 1.0, (640, 980))
    "And instead I lean forwards and put my ear against Kleio's belly."
    "It takes me a few seconds to tune myself into the odd sounds it's making."
    "But when I do, they sound just like the normal things I'd expect to hear."
    mike.say "Nope..."
    mike.say "Sounds fine to me."
    show kleio b annoyed
    kleio.say "Huh..."
    kleio.say "I thought it might have been the spicy stuff I ate last night?"
    show kleio b talkative
    kleio.say "Like, maybe the baby didn't like it or something?"
    show kleio b normal
    "I stand up and shake my head."
    "Because that sounds like mystery solved to me."
    mike.say "More like you're the one having an adverse reaction to it, Kleio!"
    "Kleio starts to turn red as soon as she hears what I have to say."
    show kleio a annoyed blush at center, traveling(1.25, 1.0, (640, 880))
    "And I know that I'm right when she turns on her heel and scurries away."
    "Choosing to flee the scene of the crime, rather than face her accuser."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
