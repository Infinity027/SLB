label bree_ice_cream_reaction_male:
    mike.say "You know what we need to make things better, [bree.name] - ice cream!"
    bree.say "Oh yeah - ice cream makes everything better!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "[bree.name] chooses the same thing, but with her own combination of flavours."
    bree.say "Mmm...this is great!"
    bree.say "I...oops - that's really cold!"
    "I look down, following [bree.name]'s gaze, and my eyes go wide."
    "The ice cream from her cone is dripping and dribbling onto her breasts!"
    bree.say "Oh, this is terrible - you must think I'm such a clutz!"
    mike.say "Ah...yeah, [bree.name]...that's exactly what I'm thinking right now!"
    return

label bree_study_with_intro_male:
    "[bree.name]'s really been hitting the books hard recently, studying almost every chance she gets."
    "And so, being the kind of guy that I am, I just had to ask if she needed a hand."
    "So here we are, surrounded by her books and wading through it all together."
    bree.say "I just wanted to say thanks, [hero.name]."
    bree.say "It's really great of you to help me out like this!"
    mike.say "Don't mention it, [bree.name]."
    mike.say "That's what friends are for, right?"
    "[bree.name] nods happily and then plunges head-first into her books."
    "Pretty soon I'm as engrossed in it as she is too!"
    "I manage to keep up pretty well at first."
    "But then [bree.name] comes up against something that stumps her."
    bree.say "Ah..."
    bree.say "This is driving me crazy!"
    bree.say "What do you think, [hero.name]?"
    "I lean in to get a better look at the page."
    "My cheek almost brushing against [bree.name]'s as I do so."
    return

label bree_study_with_success_male:
    "I take a moment to study the page from top to bottom."
    "And I scan all of the information that's there to be seen."
    "It's then that I notice [bree.name]'s chest in my peripheral vision."
    "I'm tempted to take a closer look, of course I am!"
    "But I know that the problem before me is more important."
    mike.say "Hmm..."
    mike.say "I'm not sure, [bree.name]."
    mike.say "But it kind of reminds me of the problem a couple of pages back."
    mike.say "You remember that one, right?"
    "[bree.name] wrinkles her brow at this."
    "And then she flicks back through the book."
    bree.say "You mean this one?"
    bree.say "Oh yeah, I see it now!"
    bree.say "Thanks, [hero.name]."
    bree.say "I'd never have remembered that myself!"
    mike.say "I'm sure you would have, [bree.name]."
    mike.say "You're smarter than you think!"
    "[bree.name]'s eyes go wide at the compliment."
    "And her cheeks flush with colour too."
    "But all the same, she smiles sweetly at the compliment."
    return

label bree_study_with_failure_male:
    "Almost as soon as I set eyes on the page, I know it's hopeless."
    "All I can see is a jumble of words and symbols."
    "None of it makes any sense to me!"
    "What's worse is that I catch a glimpse of [bree.name]'s chest too."
    "And from that point on, her breasts are all I can think about!"
    mike.say "Erm..."
    mike.say "I dunno, [bree.name]."
    mike.say "Are you even looking at the right way up?"
    "[bree.name] wrinkles her brow at this."
    "And then she looks down at the page too."
    bree.say "Of course it's the right way up!"
    bree.say "Wait...are you..."
    bree.say "You are - you're looking at my boobs!"
    bree.say "No wonder you're not helping!"
    mike.say "No, wait..."
    mike.say "I wasn't..."
    mike.say "I mean I was...but..."
    bree.say "Oh, save it, [hero.name]!"
    bree.say "I can study on my own."
    bree.say "I don't need help from a dumb pervert like you!"
    return

label bree_ask_phone_male:
    mike.say "Ah, [bree.name]..."
    mike.say "Can I have your number?"
    if hero.charm >= 20 - bree.love:
        show bree happy
        $ hero.smartphone_contacts.append("bree")
        bree.say "Of course you can, [hero.name]."
        bree.say "And you can call me anytime too!"
    else:
        show bree annoyed
        $ bree.love -= 1
        $ bree.sub -= 1
        bree.say "What do you need my number for, [hero.name]?"
        bree.say "I mean, we live in the same house!"
    return

label bree_ask_birthday_male:
    mike.say "When's your birthday, [bree.name]?"
    mike.say "Seems like something I should know!"
    if hero.charm >= 40 - bree.love:
        show bree happy
        $ bree.flags.birthdayknown = True
        bree.say "Wow..."
        bree.say "I kind of assumed you already knew!"
        bree.say "It's Fall 7, so don't you forget!"
    else:
        show bree annoyed
        $ bree.sub -= 1
        $ bree.love -= 1
        bree.say "Geez, [hero.name] - how long have we been living together?"
        bree.say "It must have come up a hundred times in conversation already!"
        bree.say "Maybe you'd know if you ever listened to me!"
    return

label bree_offer_a_drink_male:
    mike.say "Looks like it's time for another round!"
    mike.say "You getting in on this one, [bree.name]?"
    "Almost the second the words are out of my mouth, [bree.name] turns to face me."
    if bree.is_visibly_pregnant:
        show bree angry
        $ bree.love -= 10
        bree.say "Are you serious?!?"
        bree.say "I can't drink when I'm pregnant!"
        bree.say "What are you thinking?!?"
        $ hero.cancel_activity()
        hide bree
    elif (hero.charm >= 60 - bree.love and bree.flags.drinks < 2) or date_girl == bree:
        show bree happy
        bree.say "Ooh..."
        bree.say "Yeah, that sounds good, [hero.name]."
        bree.say "Can you grab me an Irish Coffee?"
        hide bree
        show drink bree
        if bree.love <= 25:
            $ bree.love += 1
        elif date_girl == bree and game.active_date:
            $ game.active_date.score += 5
        call expression bree.get_chat from _call_expression_216
        hide drink bree
        $ bree.set_flag("drinks", 1, "day", mod="+")
    else:
        show bree annoyed
        bree.say "No way, [hero.name]."
        bree.say "I want to keep to my own pace."
        bree.say "So I'll decide when I want a drink, okay?"
        $ hero.cancel_activity()
        hide bree
    return

label bree_slap_ass_intro_male:
    "I don't know if I ever mentioned this before."
    "But [bree.name]'s ass should come with a health warning!"
    "It just looks so good as she's walking along."
    "I can't help myself - I just have to give it a slap."
    "Just a little one!"
    return

label bree_slap_ass_happy_male:
    bree.say "Whoa!"
    bree.say "What was that?!?"
    "Suddenly I feel [bree.name]'s eyes on me."
    bree.say "[hero.name], was that you?"
    "I nod, fearing what comes next."
    bree.say "Ooh, you naughty boy!"
    bree.say "I should be mad at you."
    bree.say "But it's kind of hot too!"
    return

label bree_slap_ass_angry_male:
    bree.say "Whoa!"
    bree.say "What was that?!?"
    "Suddenly I feel [bree.name]'s eyes on me."
    bree.say "[hero.name], was that you?"
    "I nod, fearing what comes next."
    bree.say "Urgh, you animal!"
    bree.say "Don't treat me like a piece of meat!"
    return

label bree_breakup_male:
    show bree
    "I've been dreading this moment since I came to my decision."
    "But I know that it's something I just have to do."
    "And I need to do it right now, to get it over with."
    mike.say "[bree.name]..."
    mike.say "There's no easy way to say this..."
    "[bree.name]'s head almost snaps around at the sound of my voice."
    "The tone I'm using and my choice of words catches her attention in an instant."
    "It's almost like one of those whistles that only a dog can hear."
    bree.say "Oh no..."
    bree.say "I don't like the sound of that, [hero.name]!"
    "I do the best I can to ignore the worry in [bree.name]'s voice."
    "If I lose my nerve now, then I don't know if I'll get it back."
    "And so I plough on as best I can, trying to get what I have to say out."
    mike.say "It's us, [bree.name]."
    mike.say "I...I don't think it's working out."
    mike.say "In fact...I think we should call it quits."
    show bree sad
    "[bree.name] shakes her head at this, eyes wide."
    "The look on her face is making this harder than ever."
    bree.say "I can't believe it!"
    bree.say "I can't believe that you're dumping me!"
    bree.say "Urgh..."
    bree.say "I knew I shouldn't have done it."
    bree.say "I should never have got involved with a housemate!"
    "I can hear the anger in [bree.name]'s voice as she sounds off."
    "It's pretty fierce right from the start."
    "But it's getting worse with every word she says too."
    mike.say "It's not the end of the world, [bree.name]."
    mike.say "And it's not like it has to be awkward either."
    mike.say "I mean, we can still be friends, yeah?"
    show bree angry
    "[bree.name] fixes me with a cold, hard stare."
    "One that stops me dead in my tracks."
    bree.say "Oh yeah, [hero.name]?"
    bree.say "And how many of your exes are your friends with?"
    bree.say "Because I don't hang out with mine on a regular basis!"
    bree.say "And on top of that, we also have to live under the same roof!"
    "I try to come up with an answer to that."
    "But my mouth just opens and closes, no words coming out."
    bree.say "Yeah, [hero.name], you keep quiet."
    bree.say "You've said enough already!"
    return

label bree_go_steady_intro_male:
    mike.say "We're pretty great together, [bree.name]."
    mike.say "So we should definitely go steady."
    mike.say "Don't you think?"
    return

label bree_go_steady_yes_male:
    bree.say "Oh, sure thing, [hero.name]!"
    bree.say "I can't believe I didn't think of it myself."
    bree.say "Okay, it's official that we're official!"
    return

label bree_go_steady_no_male:
    bree.say "That sounds good and all, [hero.name]..."
    bree.say "But I'm really not feeling it."
    bree.say "Not where it really matters!"
    return

label bree_pet_intro_male:
    "I feel myself filling up with affection for [bree.name]."
    "So much so that I want to do something to show it."
    "And before I know it, I've reached out and patted her on the head..."
    return

label bree_pet_happy_male:
    bree.say "Wow...that was pretty weird, [hero.name]!"
    bree.say "Weird, but in a good way, you know?"
    bree.say "It kind of made my tummy go all fluttery!"
    return

label bree_pet_annoyed_male:
    bree.say "Oh no..."
    bree.say "You didn't just..."
    bree.say "You did, [hero.name]!"
    bree.say "You petted me like a dog - which is NOT cool!"
    return

label bree_massage_intro_male:
    mike.say "Ooh..."
    mike.say "Your muscles are all knotted-up, [bree.name]!"
    mike.say "You want me to give you a massage?"
    mike.say "You know, free them up a little?"
    return

label bree_massage_accept_male:
    bree.say "Oh..."
    bree.say "Thanks for the offer, [hero.name]."
    bree.say "That sounds like just what I need right now!"
    return

label bree_massage_refuse_male:
    bree.say "Oh..."
    bree.say "No, [hero.name], it's okay."
    bree.say "I get this all the time."
    bree.say "Marathon gaming sessions, yeah?"
    bree.say "It'll sort itself out."
    return

label bree_piercing_nipples_reaction_male:
    bree.say "Oh yeah...this was SO the right thing to do!"
    bree.say "Why did I never think of getting my nipples pierced before?"
    bree.say "Thanks for putting idea in my head, [hero.name]!"
    return

label bree_piercing_navel_reaction_male:
    bree.say "Piercing my belly-button - what a no-brainer!"
    bree.say "Thanks for suggesting I get it done, [hero.name]."
    bree.say "I love it!"
    return

label bree_piercing_clit_reaction_male:
    bree.say "Mmm..."
    bree.say "I can still feel it down there, [hero.name]."
    bree.say "Like I just had it done!"
    bree.say "And it feels SO good!"
    return

label bree_piercing_head_reaction_male:
    bree.say "Ha...I love this thing!"
    bree.say "It makes my tongue feel so funny!"
    bree.say "Thanks for giving me the idea, [hero.name]."
    return

label bree_piercing_nose_reaction_male:
    bree.say "I always wanted one of these!"
    bree.say "But I could never pluck up the courage before."
    bree.say "Thanks for giving me the push I needed, [hero.name]!"
    return

label bree_movie_disliked_reaction_male:
    bree.say "Huh...that was a massive pile of suck!"
    return

label bree_movie_indifferent_reaction_male:
    bree.say "That movie was SO boring - like nothing happened the whole time we were watching it!"
    return

label bree_movie_liked_reaction_male:
    bree.say "Oh...my...god - that was literally like the BEST thing ever!"
    return

label bree_belly_kiss_male:
    show bree smile at center, zoomAt(1.25, (640, 880))
    bree.say "[hero.name]..."
    bree.say "Would you do a little something for me?"
    show bree normal
    "I recognise the tone of voice that [bree.name]'s using right now."
    "It's sweet and innocent, while also a little wheedling too."
    "And it almost always means she wants something."
    "But specifically something that she thinks I might say no to."
    mike.say "Well, [bree.name]..."
    mike.say "That depends on what it is you're wanting."
    show bree annoyed
    "I can see that's not the answer [bree.name] was hoping for."
    show bree normal
    "But she does the best that she can to hide her disappointment."
    show bree smile
    "And instead she treats me to a pleasant smile."
    show bree talkative
    bree.say "Oh, it's nothing too taxing..."
    bree.say "I just wanted you to come over here and give me a kiss."
    show bree happy
    bree.say "That's pretty doable, right?"
    show bree normal
    "All I can do is shrug in response to that."
    "Because it does sound like a vey reasonable request."
    show bree at center, traveling(1.5, 0.5, (640, 1040))
    "So I walk straight over there, already puckering my lips."
    "But when I lean in for the kiss, [bree.name] puts a finger to my mouth."
    show bree talkative
    bree.say "Oh no..."
    bree.say "I meant that I wanted you to kiss my belly!"
    show bree normal
    "I can't help frowning as she pulls back her finger."
    mike.say "Your belly?"
    mike.say "Are you serious?"
    show bree gloomy
    "[bree.name] looks a little hurt at the question."
    show bree talkative
    bree.say "Well, yeah..."
    bree.say "It's just something my dad used to do for my mom."
    bree.say "They always told me it was to keep me safe when I was in her belly!"
    show bree hesitating blush
    bree.say "And...it'd mean a lot to me to have it as a kind of tradition."
    show bree normal
    "I can see from the look on [bree.name]'s face that she's totally serious."
    "And that it means as much to her as she's saying."
    "So I'd have to be a total asshole to turn her down, right?"
    show bree at center, traveling(2.0, 0.5, (640, 980))
    "Which is why I lean down and plant a kiss on the curve of her belly."
    "I hear [bree.name] let out a squeal of delight and clap her hands."
    "So I decide to keep on going, planting more all over it."
    show bree happy
    "All of which seems to make her happier than ever."
    "And I have to admit that it's not an unpleasant experience for me."
    "One that I'd very much like to repeat in the near future too."
    return

label bree_belly_caress_male:
    show bree vangry at center, zoomAt(1.25, (640, 880))
    bree.say "Urgh..."
    bree.say "Phew..."
    show bree talkative
    bree.say "[hero.name]..."
    bree.say "Could you..."
    show bree sad
    "I turn around to see [bree.name] staggering towards me, hands on her belly."
    "At first I feel a surge of panic rising in me, thinking she's unwell."
    "But then I see that it's just general exhaustion."
    "The specific kind that comes along with being heavily pregnant."
    show bree at center, traveling(1.5, 0.5, (640, 1040))
    "All the same, I rush over to her side and do all I can to help."
    mike.say "[bree.name]..."
    mike.say "Are you okay?"
    mike.say "Do you need some air?"
    mike.say "Or maybe to sit down?"
    show bree sadsmile
    "[bree.name] gives me a weak smile."
    "And I can see that she's grateful for my attention."
    show bree smile
    bree.say "That all sounds good."
    bree.say "But what I'd really like is for you to carry the baby for me..."
    bree.say "Or at least maybe split it fifty-fifty!"
    show bree normal at center, traveling(1.75, 1.0, (640, 880))
    "I give [bree.name] a helpless smile as she leans her weight on me."
    "Feeling powerless to do anything about what's ailing her."
    "Which I guess is a common feeling for guys during a pregnancy."
    mike.say "Oh, [bree.name]..."
    mike.say "If I could, I'd do it in an instant."
    mike.say "You know I hate to see you suffering like this, right?"
    show bree normal
    "[bree.name] nods, letting me know that she's on the same wavelength."
    show bree talkative
    bree.say "Sure would be nice to be able to share the burden with you."
    bree.say "I mean, it's not all bad, you know?"
    bree.say "That way you wouldn't miss out on feeling them move inside of you."
    show bree normal at center, zoomAt(1.75, (640, 880))
    "By way of an answer, I put a hand on [bree.name]'s belly."
    "And I caress the curve gently, feeling pride and contentment as I do so."
    mike.say "I guess that I'll just have to settle for helping where I can."
    mike.say "At least until medical science advances enough to make your wishes come true."
    show bree smile at startle
    "[bree.name] chuckles and puts her hand on top of mine."
    "Then she twines her fingers together with my own."
    bree.say "I think I'll make it through without a medical miracle."
    bree.say "At least so long as I have you around to help me, [hero.name]."
    mike.say "That, [bree.name], is one thing that you can always be sure of."
    "As I say this, our hands are still moving over [bree.name]'s belly."
    "And she lets out a tired, yet satisfied sigh."
    return

label bree_belly_listen_male:
    show bree surprised at center, zoomAt(1.25, (640, 880))
    bree.say "Ooh..."
    bree.say "Oh wow..."
    bree.say "This is so weird!"
    show bree stuned at center, traveling(1.5, 0.5, (640, 1040))
    "[bree.name] hurries over to me, hands on her belly."
    "Then, without warning, she thrusts it out towards me."
    "Which means I have to reach out with my own hands to grab hold of it."
    mike.say "Whoa, [bree.name]..."
    mike.say "Watch where you're pointing that thing!"
    mike.say "It's getting big enough to be classed as an offensive weapon."
    show bree annoyed
    "[bree.name] gives me a frown and shakes her head."
    show bree vangry
    bree.say "The only thing that's offensive around here is your attitude, [hero.name]!"
    bree.say "I come over here, wanting to let you feel the baby moving..."
    bree.say "And all I get in return is hassle!"
    show bree angry
    "Seeing that I might have been a little harsh, I decide to change course."
    "Which means putting a big smile on my face."
    "As well as caressing [bree.name]'s belly at the same time."
    mike.say "Well why didn't you just say that?"
    mike.say "Of course I want to feel the baby moving!"
    show bree normal
    "I'm about to make good on my words and feel for the baby."
    "But then something unexpected reaches my ear."
    show bree at center, traveling(2.0, 0.5, (640, 980))
    "And I can't help leaning in closer."
    "Before I know it, I have an ear against [bree.name]'s belly."
    show bree hesitating
    bree.say "Erm..."
    bree.say "What are you doing?"
    bree.say "Are your ears more sensitive than your hands now?"
    show bree normal
    mike.say "Sssh!"
    mike.say "I think I can hear the baby moving in there."
    "I see that [bree.name]'s glancing down at me over the curve of her belly."
    "And from the look on her face, she seems sceptical to say the least."
    bree.say "Is that even possible?"
    bree.say "Like, they used an ultrasound scanner at the hospital!"
    mike.say "Yeah, [bree.name]..."
    mike.say "And that's just a fancy, scientific term for sound."
    mike.say "Plus..."
    "Just then I swear that I hear something inside of [bree.name]."
    "Like something moving in water."
    mike.say "Oh wow..."
    mike.say "[bree.name], I can hear the baby!"
    bree.say "Yeah..."
    show bree smile
    bree.say "This might be a good time to tell you - I ate something spicy for lunch!"
    mike.say "I don't think that's it, [bree.name]..."
    mike.say "I think I really can hear the baby!"
    bree.say "If you say so."
    bree.say "But don't be surprised if I blame other noises from down there on the baby in future..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
