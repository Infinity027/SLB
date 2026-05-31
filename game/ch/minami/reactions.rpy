label minami_ice_cream_reaction_male:
    mike.say "It's almost too hot to be out here, Minami - we need some ice cream, and quick!"
    minami.say "You're right, big bro - let's go hit the ice cream stand!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Minami chooses the same thing, right down to the combination of flavours."
    mike.say "Hey - are you copying me?"
    minami.say "No way, big bro - are you copying ME?"
    "Minami smiles as she begins to lick at her cone, eyeing me the whole time."
    "Pretty soon I forget all about my ice cream, only remembering it when it begins to melt."
    "All the time my attention is on Minami, as she licks away at her cone."
    "And my mind is dreaming up other things that she could lick with that tongue too!"
    return

label minami_study_with_intro_male:
    "It's not like Minami and I haven't studied together before now."
    "I mean, we grew up in the same house together and went to the same schools."
    "But I guess what is different is the fact that she's now at uni."
    "So the books that she's hitting are that much harder than they used to be."
    "Maybe that's why I said that I'd give her some help."
    minami.say "Thanks for lending me a hand, big bro."
    minami.say "I have SO much work to get through!"
    minami.say "I feel like I'm gonna get buried under all these books!"
    mike.say "No problem, Minami."
    mike.say "It's all part of helping you settle in."
    mike.say "Now, where do we start?"
    "Minami gives me one of her cutest grins."
    "And she opens the page of the first book."
    "I'm smiling right along with her too."
    "Until we get into the swing of things, that is!"
    mike.say "Geez, Minami..."
    mike.say "Are you sure this is the right text-book?"
    mike.say "It seems pretty advanced for your first semester!"
    minami.say "No way, big bro!"
    minami.say "This is the one we use in lectures."
    minami.say "Why - is it too difficult for you?"
    "I force a smile onto my face and laugh it off."
    mike.say "Oh no, it's fine!"
    minami.say "That's good, big bro."
    minami.say "Because I need some help right here."
    "Minami jabs at the page with a finger."
    return

label minami_study_with_success_male:
    "At first I have to fight to keep the smile on my face."
    "But as I get my head around what's on the page, that changes."
    "And pretty soon the smile becomes one hundred percent genuine."
    mike.say "Ah..."
    mike.say "I remember this from my first semester!"
    mike.say "It's just a thing they didn't drill into back in school, that's all."
    "Minami leans in closer as I explain it to her."
    "And I almost get distracted by the sensation of her pressing against me."
    "Her pert little breasts are brushing against my arm."
    "And her breath is tickling my ear."
    minami.say "Huh!"
    minami.say "Is that all it was?!?"
    minami.say "I thought I was going crazy or something!"
    minami.say "You're so SMART, big bro!"
    minami.say "The smartest guy that I ever met!"
    "Minami giggles and leans her weight against me."
    "And I don't know which is better."
    "The feeling of her body against mine."
    "Or the adoration I can hear in her voice."
    return

label minami_study_with_failure_male:
    "I have to fight to keep the smile on my face as I see what she means."
    "All of the other stuff was tough and confusing for sure."
    "But this looks like it was written in an alien language!"
    mike.say "Erm..."
    mike.say "Let me see that..."
    mike.say "I just have to..."
    minami.say "Big bro..."
    minami.say "You don't have a clue, do you?"
    "I look up from the page, still forcing a smile."
    "And straight away I can see that Minami's less than impressed."
    mike.say "What?!?"
    mike.say "No, Minami, no way!"
    mike.say "I'm just a little rusty on this subject - that's all!"
    "Minami rolls her eyes and grunts in frustration."
    "Her arms are crossed over her chest and she looks annoyed."
    minami.say "You're lying, big bro, I can sense it."
    minami.say "Urgh..."
    minami.say "Now I remember why I never asked you for help back home."
    minami.say "Because you're a liar and a dumbass!"
    mike.say "Hey!"
    minami.say "Ah, save it, big bro."
    minami.say "I'm better off studying on my own!"
    return

label minami_ask_phone_male:
    mike.say "Minami, can I have your number?"
    mike.say "You must have changed it when you moved in here!"
    if hero.charm >= 20 - minami.love:
        show minami happy
        $ hero.smartphone_contacts.append("minami")
        minami.say "What?!?"
        minami.say "Did I not give it to you, big bro?"
        minami.say "Silly me - there you go!"
    else:
        show minami annoyed
        $ minami.love -= 1
        $ minami.sub -= 1
        minami.say "Yeah, I know, big bro."
        minami.say "But I'm trying to be more independent."
        minami.say "So you'll have to wait!"
    return

label minami_ask_birthday_male:
    mike.say "Minami..."
    mike.say "Remind me..."
    mike.say "When is it your birthday?"
    if hero.charm >= 40 - minami.love:
        show minami happy
        $ minami.flags.birthdayknown = True
        minami.say "Oh, big bro, you're so forgetful!"
        minami.say "My birthday is Summer 25, of course!"
    else:
        show minami annoyed
        $ minami.sub -= 1
        $ minami.love -= 1
        minami.say "Oh, big bro, you're such a scatter-brain!"
        minami.say "I must have told you like hundred time...more like a thousand!"
        minami.say "Well, I'm not telling you again!"
    return

label minami_offer_a_drink_male:
    mike.say "Minami, you want a beer?"
    mike.say "I'm just headed to the bar to grab one."
    "Almost the second the words are out of my mouth, Minami turns to face me."
    if minami.is_visibly_pregnant:
        show minami angry
        $ minami.love -= 10
        minami.say "You can't give me beer, big bro!"
        minami.say "It's bad for the baby."
        minami.say "We're going to be parents soon - you need to be more responsible!"
        $ hero.cancel_activity()
        hide minami
    elif (hero.charm >= 60 - minami.love and minami.flags.drinks < 2) or date_girl == minami:
        show minami happy
        minami.say "Ooh..."
        minami.say "Thanks, big bro."
        minami.say "But I want a cocktail - ask if they do a 'Cherry Moon', okay?"
        minami.say "And thanks for thinking of me too!"
        hide minami
        show drink minami
        if minami.love <= 25:
            $ minami.love += 1
        elif date_girl == minami and game.active_date:
            $ game.active_date.score += 5
        call expression minami.get_chat from _call_expression_254
        hide drink minami
        $ minami.set_flag("drinks", 1, "day", mod="+")
    else:
        show minami annoyed
        minami.say "Urgh..."
        minami.say "I'm not a little kid anymore, big bro!"
        minami.say "And I don't need you to do that kind of stuff for me."
        $ hero.cancel_activity()
        hide minami
    return

label minami_slap_ass_intro_male:
    "I love it when I get to walk alongside Minami."
    "Especially when I can sneak a look at the way she moves!"
    "For a petite girl, everything moves like poetry in motion."
    "And her pert little butt is the best of all."
    "In fact, I just can't resist giving it a little slap..."
    return

label minami_slap_ass_happy_male:
    "Minami jumps and lets out a little yelp of surprise."
    "And then she turns to face me, cheeks flushed red."
    minami.say "Big bro!"
    minami.say "Did you just..."
    minami.say "Did you just slap my ass!"
    "I smile and nod, as there's no way to deny it."
    "Minami smiles too, and begins to look bashful."
    minami.say "It...it's okay, big bro."
    minami.say "So long as it's you doing it!"
    return

label minami_slap_ass_angry_male:
    "Minami jumps and lets out a little yelp of surprise."
    "And then she turns to face me, cheeks flushed red."
    minami.say "Big bro!"
    minami.say "Did you just..."
    minami.say "Did you just slap my ass!"
    "I smile and nod, as there's no way to deny it."
    "Minami frowns and turns a deeper shade of red."
    minami.say "Well...well you..."
    minami.say "You just keep your hands off my ass - okay?!?"
    return

label minami_breakup_male:
    show minami
    "There's no right time or place to tell a girl that you want to break up with her."
    "So in the end, you just have to choose your moment and go for it."
    "Ninety nine times out of a hundred, she's going to be mad as hell with you."
    "But still you hope for that ultra-rare one percent chance to come up..."
    mike.say "Erm..."
    mike.say "Minami..."
    mike.say "We need to talk..."
    show minami sad
    "Minami turns to face me the moment that I start speaking."
    "And her face tells me that she's already assumed it's bad news."
    minami.say "Oh no, big bro!"
    minami.say "This is going to suck!"
    minami.say "This is going to suck big-time!"
    "I shake my head and let out a nervous laugh."
    "Doing all that I can to look baffled by her reaction."
    mike.say "I...I haven't said anything yet, Minami!"
    minami.say "You don't have to, big bro."
    minami.say "I know that voice you're using."
    minami.say "You even used it back when we were kids."
    minami.say "And it always meant you were feeling guilty."
    minami.say "That you had to tell me something bad."
    "I have no idea how to answer that."
    "And so I choose to push on with what I have to say."
    mike.say "Well..."
    mike.say "It's about us, Minami."
    mike.say "I think we should split up."
    mike.say "But that doesn't have to be a bad thing!"
    "Minami looks at me in amazement."
    minami.say "How can it be anything else, big bro?"
    minami.say "We went from being brother and sister to lovers!"
    mike.say "Ah... ADOPTED-sister!"
    minami.say "Whatever, big bro!"
    minami.say "We can't go back, not after that!"
    mike.say "Minami..."
    minami.say "Leave me alone, big bro."
    minami.say "I don't want to see you for a while."
    minami.say "Because I need to think about what this means for the both of us..."
    return

label minami_go_steady_intro_male:
    mike.say "I don't think we have anything to hide, Minami."
    mike.say "In fact, I think we should celebrate what he have together."
    mike.say "So what do you say we go steady?"
    return

label minami_go_steady_yes_male:
    minami.say "You read my mind, big bro!"
    minami.say "And who cares what anyone else thinks?"
    minami.say "You're all I need..."
    hide minami
    show minami kiss
    $ minami.flags.kiss += 1
    "Minami leaps up and wraps her arms around me."
    "I barely have time to catch her before she's kissing me!"
    return

label minami_go_steady_no_male:
    minami.say "I don't think I'm ready yet, big bro."
    minami.say "I will be soon, but not right now."
    minami.say "You understand, right?"
    return

label minami_pet_intro_male:
    "I pat Minami on the head almost on a whim."
    "She's that much shorter than me it's quite easy."
    "But almost as soon as I do it, I begin to worry."
    "I mean, how is she going to react to that?"
    return

label minami_pet_happy_male:
    minami.say "Oh...a pat on the head!"
    minami.say "That means you're really pleased with me."
    minami.say "Right, big bro?"
    return

label minami_pet_annoyed_male:
    minami.say "Hey, big bro!"
    minami.say "What the hell was that for?"
    minami.say "You can't lord it over me like you did when we were kids!"
    return

label minami_massage_intro_male:
    mike.say "Looks like you're carrying a little tension around there, Minami."
    mike.say "Muscles are all knotted up, you know?"
    mike.say "How about a quick massage to loosen you up?"
    return

label minami_massage_accept_male:
    minami.say "Ooh...ouch!"
    minami.say "You're right, big bro!"
    minami.say "I need one of your famous miracle massages."
    minami.say "And I need it right now!"
    return

label minami_massage_refuse_male:
    minami.say "Hey!"
    minami.say "You're just using that as an excuse."
    minami.say "Well it's not going to work, big bro."
    minami.say "You're not getting your hands on me!"
    return

label minami_piercing_nipples_reaction_male:
    minami.say "Oh, I love them, big bro!"
    minami.say "They make my nipples look so hot, and makes me feel so naughty."
    minami.say "But the best thing of all is knowing that you like it too!"
    return

label minami_piercing_navel_reaction_male:
    minami.say "Aw...this thing makes my belly-button look so cute!"
    minami.say "Thanks for convincing me to get it done, big bro."
    minami.say "It's going to look SO good when I wear my bikini!"
    return

label minami_piercing_clit_reaction_male:
    minami.say "Oh my, big bro!"
    minami.say "I can still feel it down there!"
    minami.say "And it's...it's making me horny!"
    return

label minami_piercing_head_reaction_male:
    minami.say "Oh, I want to stick my tongue out at everyone, big bro!"
    minami.say "Just so I can see the look on their faces!"
    minami.say "This thing makes me feel so naughty!"
    return

label minami_piercing_nose_reaction_male:
    minami.say "Ooh...it looks SO cute!"
    minami.say "I always wanted one of these, big bro!"
    minami.say "But Mom and Dad always said no."
    minami.say "That's why I love you so much - you always say yes!"
    return

label minami_movie_disliked_reaction_male:
    minami.say "Eww...that film was terrible - and it ruined the original for me too!"
    return

label minami_movie_indifferent_reaction_male:
    minami.say "It was all kind of meh and whatever - you know what I mean, big bro?"
    return

label minami_movie_liked_reaction_male:
    minami.say "O...M...G...Best film EVER!"
    return

label minami_belly_kiss_male:
    show minami sad at center, zoomAt(1.25, (640, 880))
    minami.say "Phew..."
    minami.say "How much bigger am I going to get?"
    minami.say "I already feel like a big, fat whale!"
    show minami sad
    "I turn to see Minami thrusting out her swollen belly."
    "She's holding onto it and looking more than a little pouty."
    "And I can see from the expression on her face that she's not exactly happy."
    mike.say "I think you're about as big as you're going to get, Minami."
    mike.say "But I'd hardly say that you looked like whale."
    "Minami doesn't seem convinced by my words."
    show minami annoyed
    "She crosses her arms over her belly and frowns."
    minami.say "How can you say that?"
    minami.say "Of course I look like one - I'm totally huge and gross!"
    show minami normal at center, traveling(1.5, 0.3, (640, 1040))
    "I shake my head as I step closer to Minami."
    "And at the same time I reach out to put my hands on her belly."
    mike.say "You don't look like a whale to me, Minami."
    mike.say "And that's because I never wanted to kiss a whale."
    show minami at center, traveling(2.0, 1.0, (640, 980))
    "To make my point, I lean in closer and place my lips on Minami's belly."
    show minami surprised
    "I can already hear her gasping in surprise."
    show minami happy
    "But it's when she starts to giggle with delight that I know I've achieved my goal."
    return

label minami_belly_caress_male:
    show minami vangry at center, zoomAt(1.25, (640, 880))
    minami.say "Big Bro..."
    minami.say "Come quick!"
    show minami normal
    "Already on edge thanks to Minami being pregnant, I leap up at the sound of her voice."
    show minami normal at center, traveling(1.5, 0.3, (640, 1040))
    "And then I hurry over to where she's standing, ready to tackle whatever the problem is."
    mike.say "I'm here, Minami..."
    mike.say "What's the matter?"
    mike.say "Are you going into labour or something?"
    show minami annoyed
    "Minami doesn't dignify that with an answer."
    "Instead she just grabs hold of my hand."
    "And then she presses it gently against her belly."
    mike.say "Huh..."
    mike.say "What the..."
    show minami normal
    "It's just then that I feel the sensation of something moving under my hand."
    "And when that happens, I don't need anyone else to explain it to me."
    mike.say "Oh..."
    mike.say "Oh man..."
    mike.say "That's..."
    show minami happy
    "Minami nods happily, beaming up at me."
    minami.say "Yes, big bro..."
    minami.say "That's the baby moving inside me."
    minami.say "Our baby!"
    "By now I'm smiling too, nodding my head like crazy."
    return

label minami_belly_listen_male:
    show minami at center, zoomAt(1.25, (640, 880))
    mike.say "You mind if I try something out, Minami?"
    mike.say "You know, with the belly?"
    show minami stuned
    "Minami looks up at me, surprise on her face."
    show minami surprised
    minami.say "What are you going to do, big bro?"
    minami.say "Please tell me it's nothing weird?"
    show minami normal
    "I shake my head at her concerns."
    mike.say "Of course not, Minami."
    mike.say "I'm not some kind of weirdo!"
    mike.say "All I want to do is listen to your bump."
    mike.say "See if I can hear anything, that's all."
    show minami annoyed
    "Minami seems to think about it for a moment."
    show minami normal
    "Then she nods her head."
    "And at the same time she pulls up her top too."
    show minami talkative
    minami.say "Okay..."
    minami.say "That's not TOO weird, I guess."
    show minami at center, traveling(2.0, 1.0, (640, 980))
    "I shake my head as I lean in and put my ear against her belly."
    mike.say "It's not weird at all, Minami!"
    mike.say "The doctors at the hospital are always doing this."
    show minami talkative
    minami.say "Yeah, but they're doctors..."
    minami.say "You know, professionals?"
    show minami annoyed
    "I wave away Minami's concerns as I begin to hear something."
    mike.say "Oh wow..."
    show minami talkative
    minami.say "What is it, big bro?"
    minami.say "What can you hear?"
    show minami normal
    mike.say "I...I think the baby's reciting Shakespeare!"
    show minami surprised
    minami.say "WHAT?!?"
    show minami stuned
    mike.say "Of course not!"
    mike.say "I was just joking."
    mike.say "It's subtle...kind of like when you hear whale-song."
    show minami happy
    minami.say "Ooh..."
    minami.say "That sounds amazing."
    minami.say "I wish there was some way I could listen too."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
