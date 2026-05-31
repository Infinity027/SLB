label ayesha_ice_cream_reaction_male:
    mike.say "I'm dying from this heat, Ayesha - let's grab an ice cream?"
    ayesha.say "Huh...I hadn't noticed - but sure, we can do that."
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Ayesha gets herself a cone too, but hers is just one scoop of pink ice cream."
    mike.say "Wow, I needed this, Ayesha!"
    mike.say "Is there something wrong with your cone?"
    ayesha.say "Ah...no - I'm just not an ice cream kind of person, you know?"
    "I nod at this, but I can't help raising my eyebrows too."
    "Funny, I thought everyone loved ice cream?"
    return

label ayesha_ask_phone_male:
    mike.say "I was wondering if I could get your number, Ayesha?"
    mike.say "So how about it?"
    if hero.charm >= 20 - ayesha.love:
        show ayesha happy
        $ hero.smartphone_contacts.append("ayesha")
        ayesha.say "Sure, [hero.name], I'd love you to call me."
        ayesha.say "Here you go."
    else:
        show ayesha annoyed
        $ ayesha.love -= 1
        $ ayesha.sub -= 1
        ayesha.say "I don't think so, [hero.name]."
        ayesha.say "It's nothing personal."
        ayesha.say "I just don't think we're there yet."
    return

label ayesha_ask_birthday_male:
    mike.say "Oh, I meant to ask..."
    mike.say "When is your birthday, Ayesha?"
    if hero.charm >= 40 - ayesha.love:
        show ayesha happy
        $ ayesha.flags.birthdayknown = True
        ayesha.say "Didn't I tell you that already?"
        ayesha.say "Huh...I must have forgotten."
        ayesha.say "It's Winter 29, don't forget!"
    else:
        show ayesha annoyed
        $ ayesha.sub -= 1
        $ ayesha.love -= 1
        ayesha.say "You shouldn't ask a girl her age, [hero.name]!"
        ayesha.say "And anyway, it's the muscles that make me look that way."
        ayesha.say "I'm not old...just...just more developed!"
    return

label ayesha_offer_a_drink_male:
    mike.say "I need a drink, Ayesha!"
    mike.say "You want one too?"
    "Almost the second the words are out of my mouth, Ayesha turns to face me."
    if ayesha.is_visibly_pregnant:
        show ayesha angry
        $ ayesha.love -= 10
        ayesha.say "You want me to drink?"
        ayesha.say "When I'm pregnant with your own child?!?"
        ayesha.say "Unbelievable!"
        $ hero.cancel_activity()
        hide ayesha
    elif (hero.charm >= 60 - ayesha.love and ayesha.flags.drinks < 2) or date_girl == ayesha:
        show ayesha happy
        ayesha.say "Ah, yeah..."
        ayesha.say "Could you grab me a white wine?"
        hide ayesha
        show drink ayesha
        if ayesha.love <= 25:
            $ ayesha.love += 1
        elif date_girl == ayesha and game.active_date:
            $ game.active_date.score += 5
        call expression ayesha.get_chat from _call_expression_215
        hide drink ayesha
        $ ayesha.set_flag("drinks", 1, "day", mod="+")
    else:
        show ayesha annoyed
        ayesha.say "Urgh..."
        ayesha.say "No, I do not!"
        ayesha.say "Can't you have fun without alcohol?"
        $ hero.cancel_activity()
        hide ayesha
    return

label ayesha_slap_ass_intro_male:
    "I never really considered a muscular ass before."
    "But Ayesha's almost hypnotic as she walks along."
    "Everything rolls and ripples under her skin."
    "And I can feel the sight of it making me hot under the collar!"
    "I just can't help wondering - what would it feel like?"
    "What would it feel like if I just slapped it a little?"
    return

label ayesha_slap_ass_happy_male:
    "Ayesha doesn't make a sound as I slap her ass."
    "She just stops in her tracks, eyes going wide."
    "Slowly she turns her gaze towards me."
    "And I realise that I'm holding my breath!"
    ayesha.say "Wow..."
    ayesha.say "Nobody ever did that to me before!"
    ayesha.say "But you can do it again, [hero.name]!"
    "I breathe out, feeling an immense relief."
    "And not a little turned on too!"
    return

label ayesha_slap_ass_angry_male:
    "Ayesha doesn't make a sound as I slap her ass."
    "She just stops in her tracks, eyes going wide."
    "Slowly she turns her gaze towards me."
    "And I realise that I'm holding my breath!"
    ayesha.say "Wow..."
    ayesha.say "Nobody ever did that to me before!"
    ayesha.say "And YOU better not do it again, either!"
    "I let out my held breath in a fearful gasp."
    "And I nod hastily to show that I got the message too!"
    return

label ayesha_breakup_male:
    show ayesha
    "I can't help feeling a little intimidated as I get ready to talk to Ayesha."
    "I know that she's not really going to go into beast mode on me or tie me up in knots."
    "But I still have some bad news to deliver, and I don't know how she'll react to it."
    "So I take a deep breath and try to say it like I would to any other girl..."
    mike.say "Ayesha..."
    mike.say "There's something I need to tell you..."
    "I don't know if I pitched the tone of my voice right just now."
    "Or if Ayesha just doesn't catch a hint of what I'm getting at."
    "Hell, I don't even know if I wanted her to guess at it either!"
    "Whatever the case, she smiles at me and nods."
    ayesha.say "Yeah, [hero.name]?"
    ayesha.say "What's that?"
    mike.say "You see..."
    mike.say "I don't think this is going anywhere, Ayesha."
    mike.say "You and me, that is."
    mike.say "I'm sorry, but I think we should break-up."
    show ayesha sad
    "Ayesha doesn't say anything at first."
    "In fact she doesn't seem to as much as move a muscle."
    "And in the silence that follows, I can't help thinking the worst."
    "I'm actually on the brink of closing my eyes and cowering."
    "Expecting to end up like one of her foes in a pro-wrestling match."
    "And it's then that I see her lip quiver and a drop of water in the corner of her eye."
    "Ayesha actually sniffles and then bursts into a flood of tears."
    ayesha.say "You...you bastard!"
    ayesha.say "How could you do this to me?!?"
    ayesha.say "I opened myself up to you, [hero.name], trusted you."
    ayesha.say "I thought you were different to all the other guys!"
    "I look around almost in a state of panic."
    "Because I realise I have no idea how to comfort Ayesha."
    "What am I supposed to do?"
    "Pat a girl with arms bigger than my legs on the shoulder?"
    "Tell her it'll all be okay?"
    mike.say "I'm sorry, Ayesha."
    mike.say "I just wanted to be honest with you."
    mike.say "I never meant to hurt you!"
    "Ayesha sniffles and turns her head away from me."
    ayesha.say "Well you did."
    ayesha.say "And now I never want to see you again!"
    return

label ayesha_go_steady_intro_male:
    mike.say "Ayesha..."
    mike.say "I was thinking just now..."
    mike.say "Isn't it about time that we went steady?"
    mike.say "You know, officially?"
    return

label ayesha_go_steady_yes_male:
    ayesha.say "Of course we should, [hero.name]!"
    ayesha.say "I'd love to take this to the next level..."
    "Ayesha wraps her arms around me, like a couple of amorous pythons."
    "And then she pulls me in for a kiss, which is long and lingering."
    return

label ayesha_go_steady_no_male:
    ayesha.say "I...I don't think I'm ready, [hero.name]."
    ayesha.say "Maybe sometime soon."
    ayesha.say "But not right now."
    return

label ayesha_pet_intro_male:
    "I don't know why I do it, what motivates the move inside of me."
    "I just do it before there's a chance to think about the fallout."
    "My hand reaches out and I pat Ayesha on the top of her head..."
    return

label ayesha_pet_happy_male:
    ayesha.say "Wha...what was that?"
    ayesha.say "It felt...really good!"
    ayesha.say "Would...would you do it again, [hero.name]?"
    return

label ayesha_pet_annoyed_male:
    ayesha.say "Oh no..."
    ayesha.say "Tell me you didn't just do that, [hero.name]."
    ayesha.say "Tell me you didn't just pat me on the head like a dog!"
    return

label ayesha_massage_intro_male:
    mike.say "Whoa, Ayesha!"
    mike.say "Your shoulders are knotted like a bunch of ropes!"
    mike.say "Would you like me to give you a massage?"
    return

label ayesha_massage_accept_male:
    ayesha.say "Would I ever, [hero.name]!"
    ayesha.say "And don't go easy on me either."
    ayesha.say "Really work those kinks out!"
    return

label ayesha_massage_refuse_male:
    ayesha.say "No, don't bother, [hero.name]."
    ayesha.say "You might end up making the knotting worse!"
    ayesha.say "What I need is to see a professional for a sports massage."
    return

label ayesha_piercing_nipples_reaction_male:
    ayesha.say "I...I really like the way it feels, [hero.name]."
    ayesha.say "Thank you for convincing me to get my nipples pierced."
    ayesha.say "I'd never have been able to go through with it if you weren't with me!"
    return

label ayesha_piercing_navel_reaction_male:
    ayesha.say "Huh!"
    ayesha.say "This thing really makes my belly-button look...cute!"
    ayesha.say "Thanks for talking me into doing it."
    return

label ayesha_piercing_clit_reaction_male:
    ayesha.say "Oh...oh my...oh my god!"
    ayesha.say "It feels so strange...but SO good too!"
    ayesha.say "I just wonder what it'll feel like when I take a body-slam?"
    return

label ayesha_piercing_head_reaction_male:
    ayesha.say "Wow...this thing feels weird against my teeth!"
    ayesha.say "But don't get me wrong - I do love it, [hero.name]."
    ayesha.say "Maybe you could help me get used to it?"
    ayesha.say "Maybe with a little bit of gentle kissing?"
    return

label ayesha_piercing_nose_reaction_male:
    ayesha.say "I was worried this would make me look like a big, fat cow."
    ayesha.say "You know, with a ring through my nose?"
    ayesha.say "But...I really like it!"
    return

label ayesha_movie_disliked_reaction_male:
    ayesha.say "Ah...I have to confess, I really didn't like that movie at all!"
    return

label ayesha_movie_indifferent_reaction_male:
    ayesha.say "I...I guess it was okay, but it wasn't anything special."
    return

label ayesha_movie_liked_reaction_male:
    ayesha.say "That movie was great, I loved every minute - didn't you?!?"
    return

label ayesha_belly_kiss_male:
    show ayesha at center, zoomAt(1.25, (640, 880))
    "Ayesha seems to be getting more used to the idea of walking around with a pregnant belly."
    "Plus she's also warming to the idea of people wanting to walk up to her an touch it too."
    "But I get the impression that she still thinks she's ruined her physique with the bump."
    "Which is understandable, when you consider way that she kept in shape for her career."
    "So I feel the need to make a point of reminding her that she's still my hot Amazonian goddess."
    show ayesha whining
    ayesha.say "Oh boy..."
    ayesha.say "I have never felt this bloated in my entire life."
    ayesha.say "Not even bulking season was ever this bad!"
    show ayesha sad
    "I have no idea what that is, and I know better than to ask."
    "Because pregnancy hormones can do weird things to Ayesha's moods."
    show ayesha normal at center, traveling(2.0, 0.5, (640, 980))
    "Instead I lean in and plant a kiss on the top of her bump."
    show ayesha upset at center, traveling(1.5, 0.5, (640, 1040))
    "Which makes Ayesha frown with suspicion."
    show ayesha surprised
    ayesha.say "Hey..."
    ayesha.say "What do you think you're doing?"
    show ayesha upset
    mike.say "Oh, you know how it is, Ayesha."
    mike.say "I have to kiss every part of you that's beautiful."
    mike.say "I kissed your belly when your abs were ripped."
    mike.say "And I'm kissing it now that you're carrying my baby."
    show ayesha blush
    "I can see Ayesha starting to flush with embarrassment."
    ayesha.say "You..."
    ayesha.say "You don't mean that, [hero.name]…"
    ayesha.say "You're just saying that to make me feel better!"
    show ayesha curious at center, traveling(2.0, 0.5, (640, 980))
    "I shake my head as I lower it down again."
    "And then I start kissing Ayesha's belly again."
    show ayesha surprised
    ayesha.say "Oh..."
    ayesha.say "Oh my..."
    show ayesha flirt
    ayesha.say "Actually, that's pretty nice!"
    ayesha.say "You...you can keep going...if you really want to?"
    return

label ayesha_belly_caress_male:
    show ayesha annoyed at center, zoomAt(1.25, (640, 880))
    "I keep stealing glances at Ayesha's belly as she cradles it in her hands."
    "But every time she catches me looking at her, I have to turn my head away."
    show ayesha sadsmile
    "Because I can almost feel awkwardness that's radiating from her right now."
    "Like she's totally embarrassed about the shape of her body."
    "And she feels like I'm staring at her because she's gotten fat, or something crazy like that."
    "In the end I decide that I have to say something, to make myself clear."
    "Otherwise I fear she's going to develop a complex over it or something."
    show ayesha curious
    mike.say "Ayesha..."
    mike.say "I'd like to feel your bump."
    mike.say "If you're okay with that?"
    show ayesha sadsmile
    "Ayesha looks up at me, and I can see a battle going on inside her head."
    "On the one hand, she wants to tell me to get lost, to leave her well alone."
    "But on the other she's also desperate for me to show her attention too."
    "Because I know that she wants to be a good mother and parent."
    show ayesha blush
    ayesha.say "I..."
    ayesha.say "I suppose it'd be okay."
    show ayesha at center, traveling(1.75, 1.0, (640, 880))
    "I kneel down slowly in front of her, reaching out with my hand."
    "Then I gently trace the curve of her belly until I feel something."
    "And when the baby chooses that moment to kick, I can't help myself."
    "I look up at Ayesha with the most genuine smile possible on my face."
    show ayesha happy
    "It's in that moment she seems to realise how I genuinely feel about all of this."
    "And she reaches down, putting her hand atop mine."
    "A gesture that speaks volumes, telling me more than words ever could."
    return

label ayesha_belly_listen_male:
    show ayesha surprised at center, zoomAt(1.25, (640, 880))
    ayesha.say "Oh..."
    ayesha.say "I think..."
    show ayesha happy
    ayesha.say "Yeah, the baby's moving."
    ayesha.say "Actually...they're really going for it!"
    show ayesha at center, traveling(1.75, 1.0, (640, 880))
    "I hurry over to see what Ayesha means, eager to get in on the action."
    "And as soon as I'm close enough, I can see that she's not kidding."
    "Her belly is jiggling and bopping like crazy!"
    mike.say "Whoa..."
    mike.say "It looks like they're practicing all your best moves in there!"
    mike.say "This kid is going to be a badass wrestler, just like their momma!"
    "I can see that Ayesha's a little bashful about my gushing over her and the baby."
    "But also that there's a real glimmer in her eyes right now."
    "And that she doesn't tell me to stop either."
    "But I'm not satisfied with just seeing the action."
    "I want to hear it too."
    show ayesha at center, traveling(2.0, 0.5, (640, 980))
    "So I kneel down and put an ear to Ayesha's belly."
    "She watches me with interest, straining to see as much as she can."
    show ayesha talkative
    ayesha.say "What do you hear?"
    ayesha.say "Tell me already!"
    show ayesha normal
    mike.say "Oh man..."
    mike.say "They're really going for it in there..."
    mike.say "It sounds like an underwater Battle Royal!"
    "I push my ear closer, but then I feel something slam into the side of my head."
    "It's not a blow hard enough to stagger me, but it's enough to make me pull away my head."
    mike.say "Did..."
    mike.say "Did the baby just hit me in the head?!?"
    show ayesha talkative
    ayesha.say "Well, [hero.name]..."
    show ayesha happy
    ayesha.say "You did say they were taking after their momma!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
