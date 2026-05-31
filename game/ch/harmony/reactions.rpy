label harmony_ice_cream_reaction_male:
    if harmony.purity >= LP:
        mike.say "Wow, it's just TOO hot today, Harmony - let's grab some ice cream!"
        harmony.say "You read my mind - I could really go for one right now!"
        "At the ice cream stall, I buy myself a cone with a couple of different scoops."
        "Harmony chooses the same thing, but with her own combination of flavours."
        harmony.say "Oh, darn it - why does this happen to me every single time?!?"
        "Intrigued, I glance over to see what's bothering Harmony."
        "And I'm just in time to see her chest make contact with her cone."
        "One of her breasts literally knocks a scoop of ice cream off the top."
        "And it splatters onto the ground at her feet, making her hop aside to avoid it."
        "I feel sympathy for the loss of her ice cream."
        "But I can't help being impressed by the heft of her cleavage too!"
    else:
        mike.say "Wow, it's just TOO hot today, Harmony - let's grab some ice cream!"
        harmony.say "Mmm...that sounds SO good - race you to the ice cream stand!"
        "At the ice cream stall, I buy myself a cone with a couple of different scoops."
        "Harmony chooses the same thing, but with her own combination of flavours."
        harmony.say "Oh, dear...how on earth could I have let that happen?!?"
        "Intrigued, I glance over to see what's bothering Harmony."
        "And I'm just in time to see her chest make contact with her cone."
        "One of her breasts literally knocks a scoop of ice cream off the top."
        "And it splatters onto the ground at her feet, making her hop aside to avoid it."
        "I look from the ice cream back up to Harmony's face, seeing her knowing smile."
        "And I swallow audibly, realising that what she just did was no accident!"
    return

label harmony_ask_phone_male:
    mike.say "Harmony..."
    mike.say "What's your number?"
    mike.say "Just in case I need to call you."
    if hero.charm >= 20 - harmony.love:
        show harmony happy
        $ hero.smartphone_contacts.append("harmony")
        harmony.say "Here it is, [hero.name]."
        harmony.say "You call me whenever you need to, okay?"
    else:
        show harmony annoyed
        $ harmony.love -= 1
        $ harmony.sub -= 1
        harmony.say "I can't let you have that, [hero.name]."
        harmony.say "You might get tempted to use it."
        harmony.say "To use it for sinful things!"
    return

label harmony_ask_birthday_male:
    mike.say "Ah, Harmony..."
    mike.say "When is your birthday?"
    if hero.charm >= 40 - harmony.love:
        show harmony happy
        $ harmony.flags.birthdayknown = True
        harmony.say "It's Fall 22, [hero.name]."
        harmony.say "So don't you go forgetting that date!"
    else:
        show harmony annoyed
        $ harmony.sub -= 1
        $ harmony.love -= 1
        harmony.say "If you don't know, then I didn't tell you."
        harmony.say "And if I didn't tell you, you aren't supposed to know!"
    return

label harmony_offer_a_drink_male:
    mike.say "Ah..."
    mike.say "You want anything from the bar, Harmony?"
    mike.say "I was just going to grab a drink."
    "Almost the second the words are out of my mouth, Harmony turns to face me."
    if harmony.is_visibly_pregnant:
        show harmony angry
        $ harmony.love -= 10
        harmony.say "What, and hurt the child growing inside of me?!?"
        harmony.say "Have you gone mad, [hero.name]?"
        harmony.say "Are you possessed by spirits of a demonic kind?!?"
        $ hero.cancel_activity()
        hide harmony
    elif (hero.charm >= 60 - harmony.love and harmony.flags.drinks < 2) or date_girl == harmony:
        show harmony happy
        harmony.say "Jesus fucking Christ, [hero.name]!"
        harmony.say "I thought you'd never ask!"
        harmony.say "Get me a vodka - and make it a double too!"
        hide harmony
        show drink harmony
        if harmony.love <= 25:
            $ harmony.love += 1
        elif date_girl == harmony and game.active_date:
            $ game.active_date.score += 5
        call expression harmony.get_chat from _call_expression_240
        hide drink harmony
        $ harmony.set_flag("drinks", 1, "day", mod="+")
    else:
        show harmony annoyed
        harmony.say "Oh my goodness!"
        harmony.say "Don't you know that alcohol is sinful?!?"
        harmony.say "Well, I won't let you corrupt me!"
        $ hero.cancel_activity()
        hide harmony
    return

label harmony_slap_ass_intro_male:
    "It's tough not to notice just how curvy Harmony's body is."
    "That and the way it moves when she walks too."
    "And her ass - especially her ass!"
    "It's like that part of her has a mind of it's own!"
    "In the end, I can't resist slapping it..."
    return

label harmony_slap_ass_happy_male:
    "The force of the gentle tap spreads outwards across Harmony's buttocks."
    "And she seems to feel it in the same way too, jumping in surprise."
    harmony.say "Oh goodness..."
    harmony.say "What in heaven was that?!?"
    "She looks at me, and I can see her mind racing."
    harmony.say "Did you..."
    harmony.say "Did you slap my ass!"
    harmony.say "Oh, [hero.name] - that's SO naughty of you!"
    "Harmony smiles as she says this, letting me know that she approves!"
    return

label harmony_slap_ass_angry_male:
    "The force of the gentle tap spreads outwards across Harmony's buttocks."
    "And she seems to feel it in the same way too, jumping in surprise."
    harmony.say "Oh goodness..."
    harmony.say "What in heaven was that?!?"
    "She looks at me, and I can see her mind racing."
    harmony.say "Did you..."
    harmony.say "Did you slap my ass!"
    harmony.say "How DARE you?!?"
    "Harmony underlines the point by slapping me across the face."
    return

label harmony_breakup_male:
    show harmony
    "Sometimes it's the easiest thing in the world to tell someone it's over."
    "You're even glad to be able to get it off your chest and over with."
    "But that's usually when the other person involved is a real piece of work."
    "It's that much harder when the girl you're trying to dump is pretty nice."
    "So when it comes to someone like Harmony, it's super hard to do!"
    mike.say "Erm..."
    mike.say "Harmony..."
    "The smile that spreads across Harmony's face is so genuine."
    "Like she's simply pleased to be able to have a conversation with me."
    "Which, of course, makes what I have to say next that much more painful!"
    harmony.say "Yes, [hero.name]?"
    harmony.say "What is it?"
    mike.say "I...I need to talk to you about us, Harmony."
    mike.say "About our relationship and where it's going."
    show harmony happy
    "A sudden light appears in Harmony's eyes."
    "And she clasps her hands over her heart."
    harmony.say "Are you..."
    harmony.say "Are you going to propose?!?"
    "There it is - the punch to the gut that ends it for me."
    "Harmony's come to completely the wrong conclusion."
    "And in my state of panic, I start to vomit up my words."
    mike.say "Jesus Titty-Fucking Christ, Harmony!"
    mike.say "I mean I want to break up with you - not marry you!"
    show harmony angry
    "The look on Harmony's face is literally priceless."
    "And she goes from stunned silence to righteous rage in mere seconds."
    harmony.say "I should have known!"
    harmony.say "I should have sensed you were the devil in disguise!"
    harmony.say "You seduced me and now you want to cast me aside!"
    mike.say "Harmony, please!"
    mike.say "It's not like that!"
    "I don't see the slap coming until it's too late."
    "It spins my head around before I even feel the pain."
    harmony.say "Maybe that'll drive the devil out of you, [hero.name]."
    harmony.say "And if not, I'll keep on slapping you until it does!"
    "She raises her hand to strike me again."
    "But by then, I'm already making my escape."
    "As I scurry away, I can hear Harmony shouting after me."
    harmony.say "Get thee behind me, Satan!"
    return

label harmony_go_steady_intro_male:
    mike.say "I'm really enjoying spending time with you, Harmony."
    mike.say "It's always the highlight of my day."
    mike.say "So why don't we make it official and go steady?"
    return

label harmony_go_steady_yes_male:
    harmony.say "You're SO right, [hero.name]."
    harmony.say "We should make a commitment to each other."
    harmony.say "Let's do it!"
    return

label harmony_go_steady_no_male:
    harmony.say "Oh, I don't think so, [hero.name]."
    harmony.say "I feel the same way about you too."
    harmony.say "But I don't want to rush things."
    return

label harmony_pet_intro_male:
    "I don't know why I do it, but I reach out and pat Harmony on the head."
    "It just feels like the right thing to do in the moment."
    "But as soon as it's done, I start to wonder if it actually is..."
    return

label harmony_pet_happy_male:
    harmony.say "Oh..."
    harmony.say "Thank you, [hero.name]!"
    harmony.say "You don't need to remind me of my place."
    return

label harmony_pet_annoyed_male:
    harmony.say "Wha..."
    harmony.say "What on earth are you doing, [hero.name]?"
    harmony.say "How dare you treat me like that?!?"
    return

label harmony_massage_intro_male:
    mike.say "Hmm..."
    mike.say "You look kind of tense, Harmony."
    mike.say "I could give you a massage if you like?"
    mike.say "You know, help you to loosen up a little?"
    return

label harmony_massage_accept_male:
    harmony.say "Mmm..."
    harmony.say "I am really knotted up right now."
    harmony.say "And a massage does sound nice."
    harmony.say "Okay, [hero.name], go ahead!"
    return

label harmony_massage_refuse_male:
    harmony.say "Urgh..."
    harmony.say "I'm in pain, [hero.name]!"
    harmony.say "Don't use it as an excuse to feel me up!"
    return

label harmony_piercing_nipples_reaction_male:
    harmony.say "I used to think this kind of thing was just downright wicked."
    harmony.say "But since I met you, [hero.name], all that's changed."
    harmony.say "Now having my nipples pierced, it feels like a badge of honour."
    harmony.say "Like I've been branded as a bad girl!"
    return

label harmony_piercing_navel_reaction_male:
    harmony.say "You're sure this doesn't make my belly look big?"
    harmony.say "Because I really like the way it looks, [hero.name]."
    harmony.say "It makes me feel really sexy too!"
    return

label harmony_piercing_clit_reaction_male:
    harmony.say "To think, I actually used to be scared of my pussy."
    harmony.say "And now here I am, getting it pierced!"
    harmony.say "And it's all thanks to you, [hero.name]!"
    return

label harmony_piercing_head_reaction_male:
    harmony.say "I used to use my tongue to read the bible and sing hymns."
    harmony.say "I can't believe I've actually had it pierced!"
    harmony.say "You're SUCH a bad influence on me, [hero.name]!"
    harmony.say "And I love it!"
    return

label harmony_piercing_nose_reaction_male:
    harmony.say "Oh wow...I feel a little bit like an animal, [hero.name]!"
    harmony.say "Like you could put a ring in my nose and lead me around!"
    harmony.say "Ooh...I kind of like the way that sounds..."
    return

label harmony_movie_disliked_reaction_male:
    if harmony.purity >= VHP:
        harmony.say "Hmm...I don't approve of movies like that, they're a very bad influence, very wicked!"
    elif harmony.purity >= HP:
        harmony.say "Hmm...I don't approve of movies like that, they're a very bad influence, very wicked!"
    elif harmony.purity < VLP:
        harmony.say "Urgh...we could have spent that time making out - or something even more fun!"
    elif harmony.purity < LP:
        harmony.say "No...I didn't like that movie at all!"
    else:
        harmony.say "No...I didn't like that movie at all!"
    return

label harmony_movie_indifferent_reaction_male:
    if harmony.purity >= VHP:
        harmony.say "Well...I suppose the best you could say was that it's inoffensive?"
    elif harmony.purity >= HP:
        harmony.say "Well...I suppose the best you could say was that it's inoffensive?"
    elif harmony.purity < VLP:
        harmony.say "That was SO boring - I could have been playing with your cock instead!"
    elif harmony.purity < LP:
        harmony.say "Yeah...that was kind of boring!"
    else:
        harmony.say "Yeah...that was kind of boring!"
    return

label harmony_movie_liked_reaction_male:
    if harmony.purity >= VHP:
        harmony.say "That was glorious...what an experience - I was transported!"
    elif harmony.purity >= HP:
        harmony.say "That was glorious...what an experience - I was transported!"
    elif harmony.purity < VLP:
        harmony.say "I loved that movie - it made me feel SO horny!"
    elif harmony.purity < LP:
        harmony.say "What a great movie - I loved it!"
    else:
        harmony.say "What a great movie - I loved it!"
    return

label harmony_belly_kiss_male:
    show harmony at center, zoomAt(1.25, (640, 880))
    "I lean in to plant a kiss on Harmony's lips."
    "Closing my eyes in anticipation of the kiss that should follow."
    hide harmony
    show harmony kiss
    with fade
    if harmony.purity >= HP:
        "And then I feel Harmony's lips pressing against my own."
        "Softly and demurely, reminding me of how divine she is."
    elif harmony.purity >= VLP:
        "And then Harmony presses her lips hungrily against mine."
        "She moves too quickly for me to be able to resist, slipping her tongue into my mouth."
        "Not that I'm complaining or would want to resist for a moment!"
    else:
        "And then I feel them pressing against mine."
        "As well as her lips parting just a little."
        "But there's a sudden thrill as she slips a bit of tongue in there too!"
    "The kiss lingers on for a long time, something that pleases me a great deal."
    hide harmony kiss
    show harmony stuned at center, zoomAt(1.25, (640, 880))
    with fade
    "But when it finally comes to an end, I'm just not ready to quit indulging myself."
    show harmony at center, traveling(2.0, 1.0, (640, 980))
    "And so I take a deep breath and begin to kneel down in front of Harmony."
    "Who obviously looks surprised as hell, not knowing what I'm doing."
    show harmony surprised
    if harmony.purity >= HP:
        harmony.say "[hero.name]…"
        harmony.say "Whatever are you doing?!?"
    elif harmony.purity >= VLP:
        harmony.say "Well, well, well..."
        harmony.say "You'd better be going down there to do something naughty to me!"
    else:
        harmony.say "Okay, [hero.name]…"
        harmony.say "What are you up to?"
    "I have a smile on my face as Harmony questions me."
    "Because what I have in mind seems perfectly natural to me."
    "And I'm sure that she's going to love it too."
    "Lifting her top enough to reveal her belly, I begin to kiss it gently."
    show harmony blush
    "Harmony almost instantly begins to gasp and coo at the sensation."
    "And I take the fact she's not telling me to stop as permission to continue."
    "Which is great for me, as I'm enjoying this as much as she seems to be."
    "Getting up close to our unborn child while lavishing attention on their mother."
    "I mean, can you imagine a more perfect picture than that?"
    return

label harmony_belly_caress_male:
    show harmony at center, zoomAt(1.25, (640, 880))
    "I knew that I was getting into a relationship with a full-figured girl when I met Harmony."
    "Something that I was totally fine with, as she's the perfect image of womanhood."
    "But the one thing I never thought of was how being pregnant would affect that."
    "And I could never have been prepared for the fact that it's totally blowing my mind!"
    "Harmony was like something out of a classical art gallery before."
    "But now it's like she's ascended into heaven and become an actual, bona fide goddess!"
    "Not only have her curves become curvier, but it's like she's glowing the whole time."
    "I mean, is there something sexy pregnant women give off?"
    "Kind of like sexy radiation or something?"
    show harmony talkative
    if harmony.purity >= HP:
        harmony.say "Oh, [hero.name]…"
        harmony.say "You're looking at me in that way again!"
    elif harmony.purity >= VLP:
        harmony.say "Mmm..."
        harmony.say "I love it when you look at me like that, [hero.name]…"
        harmony.say "It makes me want to get pregnant all over again!"
    else:
        harmony.say "I can see what you're doing, [hero.name]…"
        harmony.say "You're staring at me again!"
    show harmony normal
    "I can feel myself starting to sweat under Harmony's gaze."
    "And I mean sure, it's not like she's telling me off or anything..."
    "But I still have that desperate need to be close to her."
    "To be able to touch that incredible body."
    show harmony at center, traveling(1.5, 1.0, (640, 1040))
    "So I slide over to her, trying to look as innocent as possible."
    "And while I hold her eye, I reach out with one hand."
    show harmony stuned
    "I can feel myself holding my breath as I place it on the curve of Harmony's belly."
    "For a moment I think that she's going to push it away."
    "To tell me that I should keep my hands to myself."
    show harmony happy
    "But instead the touch seems to mollify Harmony in short order."
    "And I watch as she puts her hand atop mine."
    "Then she leans her head on my shoulder, letting out a gentle sigh."
    "I think about asking her if she's okay, if she needs anything."
    "But then I realise that this is one of those times when it's best to keep quiet."
    "A little island of tranquillity in the crazy sea of life."
    "So instead I sit back and do all that I can to enjoy it instead."
    return

label harmony_belly_listen_male:
    show harmony at center, zoomAt(1.25, (640, 880))
    pause 0.2
    show harmony at center, traveling(2.0, 1.0, (640, 980))
    "I lean in close to the curve of Harmony's belly, putting my ear to it."
    show harmony embarrassed
    "And the moment I do, I can almost feel her eyes on me."
    "Which I guess is fair enough when I'm listening closely to a part of her anatomy."
    "But all the same, I can't help kind of chuckling to myself at the same time."
    "Imagining the look on her face as she strains to see what I'm doing down here."
    harmony.say "Ah, [hero.name]…"
    harmony.say "What are you..."
    harmony.say "What are you doing down there?"
    "I wave a hand in an attempt to keep Harmony quiet."
    "As it's already hard enough to hear anything inside of her belly."
    mike.say "Ssssh!"
    mike.say "I'm trying to hear the baby moving in there, Harmony..."
    mike.say "And right now, all I can hear is you asking me questions!"
    show harmony annoyed
    "I feel Harmony move a little as I tell her off."
    "Probably feeling quite put out at the tone of my voice."
    show harmony normal
    "But it doesn't take he long to recover enough to keep on asking more questions."
    "Only this time her voice comes in a whisper."
    harmony.say "Can..."
    harmony.say "Can you hear anything yet?"
    "I'm about to say no and ask her to shut up all over again."
    "But then I feel something move against my ear."
    "And a series of weird sounds follow along with it."
    mike.say "Whoa..."
    mike.say "There they go!"
    mike.say "They're on the move, Harmony!"
    "I keep on pressing my ear to Harmony's belly, trying to follow the sounds."
    "And I have no idea if I manage to keep up with the way the baby's moving."
    "But that's hardly the point, as the experience in itself feels worthwhile in it's own right."
    show harmony happy
    "So I keep on moving my ear over Harmony's belly, all the time trying to keep her in the loop."
    "I don't know if my descriptions of what I can hear are helpful, or even if they make any sense."
    "But she listens intently all the same, asking me questions along the way that I struggle to answer."
    "And once it's all over, I feel like we've been on a strange little journey together."
    "Not for the first time, and I'm sure not for the last either."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
