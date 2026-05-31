label victor_ice_cream_reaction_female:
    victor.say "Ah, [hero.name]..."
    victor.say "I'm sweating like crazy today!"
    victor.say "What's up with this heat?"
    "I can't help frowning a little as I look over at Victor."
    "Because the cause of his suffering is pretty obvious."
    if hero.morality >= 25:
        bree.say "You're dressed all in black, you silly thing!"
    elif hero.morality <= -25:
        bree.say "You're all in black - and, I bet you have on black underwear!"
    else:
        bree.say "Victor, you're wearing black from head to toe!"
    bree.say "That might have something to do with it, you think?"
    "Victor shrugs as he wipes the perspiration off his forehead with his sleeve."
    victor.say "What can I say, [hero.name]?"
    victor.say "It kind of comes with the job!"
    "I shake my head as I look around, trying to find a solution."
    "And then it hits me."
    bree.say "Ice-cream - that's what we need!"
    "Taking Victor by the hand, I lead him over to the ice-cream stand."
    "And once we're there, I buy one for each of us."
    victor.say "Whoa..."
    victor.say "That's a whole lot better!"
    victor.say "Thanks, [hero.name]."
    bree.say "Hmm..."
    bree.say "We really need to talk about your wardrobe choices!"
    return

label victor_ask_phone_female:
    "Okay, so I really want to get Victor's number, but I need to make it seem casual."
    "So here goes..."
    if hero.morality >= 25:
        bree.say "Oh, Victor..."
        bree.say "I was wondering if I could get your phone number?"
    elif hero.morality <= -25:
        bree.say "Victor, there's so many naughty things I want to text you about."
        bree.say "But the problem is I don't have your number!"
    else:
        bree.say "Victor, you never gave me your phone number!"
        bree.say "What if I need to call you or something?"
    if hero.charm >= 20 - victor.love:
        show victor happy
        "Victor looks up with a surprised expression on his face."
        "Already pulling his phone out of his pocket with some haste."
        if victor.sub >= 50:
            victor.say "Of course you can have my number, [hero.name]..."
            victor.say "I can't believe I didn't give you it already!"
        elif victor.sub <= -50:
            victor.say "You can have my number, [hero.name]..."
            victor.say "But you can only use it with my express permission!"
        else:
            victor.say "Whoa...I didn't let you have it already?"
            victor.say "Here, let me fix that."
        $ hero.smartphone_contacts.append("victor")
    else:
        show victor annoyed
        $ victor.love -= 1
        $ victor.sub -= 1
        "Victor kind of frowns and shakes his head."
        "And I note that he doesn't pull his phone out either."
        if victor.sub >= 50:
            victor.say "I...I really want to give it to you, [hero.name]..."
            victor.say "But it's, like, against the hitman's code!"
        elif victor.sub <= -50:
            victor.say "I already have your number, [hero.name]."
            victor.say "So I can reach you when I need to."
        else:
            victor.say "Sorry, [hero.name] - but that's sensitive information."
            victor.say "We've just not reached that level of trust yet."
    return

label victor_ask_birthday_female:
    "Okay, so I really want to find out Victor's birthday, but I need to make it seem casual."
    "So here goes..."
    if hero.morality >= 25:
        bree.say "Oh, Victor..."
        bree.say "I was wondering, just when is your birthday?"
    elif hero.morality >= 25:
        bree.say "Victor, there's so many naughty things I want to buy for you."
        bree.say "But the problem is I don't know the date!"
    else:
        bree.say "Victor, you never told me the date of your birthday!"
        bree.say "What if I want to get you special little something?"
    if hero.charm >= 40 - victor.love:
        "Victor looks up with a surprised expression on his face."
        "Already nodding like he's going to divulge the details."
        if victor.sub >= 50:
            victor.say "Of course you can have the date, [hero.name]..."
            victor.say "I can't believe I didn't give you it already!"
        elif victor.sub <= -50:
            victor.say "You can have the date, [hero.name]..."
            victor.say "But you have to clear any birthday gifts with me first!"
        else:
            victor.say "Whoa...I didn't tell you it already?"
            victor.say "Here, let me fix that."
        victor.say "It's Fall 25, [hero.name]."
        $ victor.flags.birthdayknown = True
    else:
        "Victor kind of frowns and shakes his head."
        "And I can tell that I'm not about to get what I want out of him."
        if victor.sub >= 50:
            victor.say "I...I really want to give it to you, [hero.name]..."
            victor.say "But it's, like, against the hitman's code!"
        elif victor.sub <= -50:
            victor.say "I'll tell you what you need to know when you need to know it, [hero.name]."
            victor.say "Until then, that's top secret information!"
        else:
            victor.say "Sorry, [hero.name] - but that's sensitive information."
            victor.say "We've just not reached that level of trust yet."
    return

label victor_offer_a_drink_female:
    if hero.morality >= 25:
        bree.say "I think I can handle one more drink!"
        bree.say "Would you like me to get you one too, Victor?"
    elif hero.morality >= 25:
        bree.say "My round again - better hope I don't get too drunk and outrageous!"
        bree.say "You want one too, Victor?"
    else:
        bree.say "Time for another one!"
        bree.say "You want me to get you one too, Victor?"
    if hero.is_visibly_pregnant:
        if victor.sub >= 50:
            victor.say "Erm...I don't want to be rude, [hero.name]..."
            victor.say "But should you be drinking when you're pregnant?"
        elif victor.sub <= -50:
            victor.say "No, [hero.name], you won't be having another."
            victor.say "Not while you're pregnant."
        else:
            victor.say "I don't want to tell you your business, [hero.name]..."
            victor.say "But drinking so much isn't good for your baby."
    else:
        if victor.sub >= 50:
            victor.say "I'll have one if you think I should, [hero.name]!"
            victor.say "Could you pick a drink for me too?"
        elif victor.sub <= -50:
            victor.say "Aren't you getting a little ahead of yourself, [hero.name]?"
            victor.say "That's the kind of decision I should be making for you."
        else:
            victor.say "Sure, [hero.name], I'll have another one."
            victor.say "Could I get the same again?"
    return

label victor_slap_ass_intro_female:
    "Oh man, you have to see how good Victor's ass looks in those black pants of his!"
    "In fact it looks so good that I don't think I can control myself around it anymore."
    "And before I know what's happening, arm is winding up, pulling backwards."
    "Then my hand goes arcing through the air, on a collision course with the object of my affections."
    "The slap catches Victor totally unawares, a sharp crack resulting from the connection betwixt palm and buttock."
    "In fact the sound is so loud that it kind of reminds me of a gunshot."
    "Which, of course, makes Victor instantly edgy and paranoid."
    if victor.sub >= 50:
        victor.say "Aargh..."
        victor.say "What was that?"
    elif victor.sub <= -50:
        victor.say "Nobody move!"
        victor.say "Not until I know what just happened."
    else:
        victor.say "What the hell?"
        victor.say "What just happened?"
    victor.say "Wait a minute...did you...did you just slap me on the ass?!?"
    if hero.morality >= 25:
        bree.say "Sorry, Victor - I don't know what came over me!"
    elif hero.morality >= 25:
        bree.say "Oh come on, how am I supposed to resist a peach like that?"
    else:
        bree.say "Sorry, Victor - it's just so...peachy!"
    return

label victor_slap_ass_happy_female:
    "I'm almost wincing as I wait for Victor to respond to my confession."
    "And I don't have to wait long to hear it either."
    if victor.sub >= 50:
        victor.say "Oh...thank you, [hero.name]!"
        victor.say "I do try to keep myself in shape."
    elif victor.sub <= -50:
        victor.say "It's great that you appreciate how hot my ass is, [hero.name]..."
        victor.say "But you need to ask permission before you do something like that, okay?"
    else:
        victor.say "Well give me some warning next time, okay?"
        victor.say "I get kind of jumpy when you do unexpected stuff!"
    return

label victor_slap_ass_angry_female:
    "I'm almost wincing as I wait for Victor to respond to my confession."
    "And I don't have to wait long to hear it either."
    if victor.sub >= 50:
        victor.say "You really shouldn't do that to me, [hero.name]..."
        victor.say "It's, like, a form of abuse!"
    elif victor.sub <= -50:
        victor.say "Well don't do it again, okay?"
        victor.say "You can't just put your hands on me without my permission."
    else:
        victor.say "Well I'd rather you didn't, [hero.name]..."
        victor.say "It's kind of taking liberties, you know?"
    return

label victor_breakup_female:
    "I can already feel the strain on my heart that I knew this was going to cause me."
    "The inevitable pain that was always going to come when I finally faced up to it."
    "But it's not going to go away even if I choose to run away from it now."
    "So I just take a deep breath and push myself to do what I know needs to be done."
    if hero.morality >= 25:
        bree.say "Victor, there's something I have to tell you..."
    if hero.morality <= -25:
        bree.say "Okay, big boy, I'm just gonna come right out and say it..."
    else:
        bree.say "Victor, there's no easy way to say this..."
    bree.say "This isn't working - so I think we need to end it."
    "I don't know what I was expecting Victor to do once I got the words out."
    "Maybe for him to blow up, or start pleading with me to stay."
    "But instead he just stares at me, like I slapped him in the face."
    if victor.sub >= 50:
        victor.say "W...well, if that's what you want, [hero.name]..."
        victor.say "I don't know how I'll cope - but you're the boss."
    elif victor.sub <= -50:
        victor.say "What the hell, [hero.name]?"
        victor.say "I thought you were really happy?"
        victor.say "Huh...I guess I was wrong!"
    else:
        victor.say "Oh no, [hero.name] - you can't be serious?"
        victor.say "But if that's what you want...then I guess that's how it has to be."
    bree.say "Yeah, Victor..."
    bree.say "I really think it has to be this way."
    bree.say "But if we're lucky, maybe we'll still be able to be friends."
    return

label victor_go_steady_intro_female:
    "There's only one way to do this thing, and that's to just do it."
    "So I take a deep breath, steel myself for the challenge, and then just do it."
    if hero.morality >= 25:
        bree.say "Victor, I think we've been getting on well recently."
        bree.say "So I was wondering if...maybe...we could go steady?"
    if hero.morality <= -25:
        bree.say "Victor, I love what we have right now..."
        bree.say "But I want more - I want to go steady!"
    else:
        bree.say "We've been getting on really well, haven't we, Victor?"
        bree.say "Maybe even well enough to...I don't know...go steady?"
    return

label victor_go_steady_yes_female:
    "Almost as soon as I mention the idea of going steady, Victor's eyes light up."
    "Like he's really tuned into the notion of what I'm suggesting."
    if victor.sub >= 50:
        victor.say "Is that what you want, [hero.name]?"
        victor.say "Then it's what I want to - so let's go steady!"
    elif victor.sub <= -50:
        victor.say "Funny you should say that, [hero.name]..."
        victor.say "I was just about to say we were going to do that."
    else:
        victor.say "I think we've been getting on like a house on fire, [hero.name]."
        victor.say "So yeah, I'm up for going steady if you are."
    return

label victor_go_steady_no_female:
    "Almost as soon as I mention the idea of going steady, Victor's eyes go wide."
    "Like he's totally freaked out by the mere notion of what I'm suggesting."
    if victor.sub >= 50:
        victor.say "Oh no, [hero.name], I don't think that would work out."
        victor.say "Because I haven't proven myself worthy of you yet!"
    elif victor.sub <= -50:
        victor.say "No way, [hero.name], we're not even close that kind of commitment yet."
        victor.say "And I'll be the one to decide when we are too!"
    else:
        victor.say "I'm not sure we're ready for that yet, [hero.name]."
        victor.say "Maybe we just give it a little longer, yeah?"
    return

label victor_pet_intro_female:
    "I know that Victor's like this hard-nosed, edgy hitman type of guy."
    "But at the same time he's just so cute that I want to reach out and pet him."
    "And so that's exactly what I do - put out my hand and pat the top of his head."
    "The moment I do so, Victor tenses and pulls off one of those cool martial arts stances."
    if victor.sub >= 50:
        victor.say "[hero.name], there could be danger afoot - do get behind me!"
    elif victor.sub <= -50:
        victor.say "[hero.name], get your ass behind me - there's danger afoot!"
    else:
        victor.say "Huh...what was that?"
        victor.say "Is there someone trying to get the drop on me?"
    if hero.morality >= 25:
        bree.say "Erm...no, there isn't."
        bree.say "I just kind of...patted you on the head, that's all!"
    elif hero.morality >= 25:
        bree.say "Geez, if that's what happens when I pat you on the head..."
        bree.say "I'd better scrap my plans to slap you on the ass!"
    else:
        bree.say "Don't be silly, Victor..."
        bree.say "That was just me patting you on the head!"
    return

label victor_pet_happy_female:
    "Almost as soon as he hears my explanation, the expression on Victor's face changes."
    "Where before he was tense and alert, he now becomes calm and his face practically beams."
    if victor.sub >= 50:
        victor.say "Oh...well that's different, obviously..."
        victor.say "You can pat me any time you like, [hero.name]!"
    elif victor.sub <= -50:
        victor.say "Patting and petting is totally fine, [hero.name]..."
        victor.say "But you need to ask my permission in future, okay?"
    else:
        victor.say "Oh...sorry if I acted tense just now, [hero.name]..."
        victor.say "I'm still getting used to all this couple stuff!"
    return

label victor_pet_annoyed_female:
    "Almost as soon as he hears my explanation, the expression on Victor's face hardens."
    "And I can stell that he's not at all impressed with my patting him on the head."
    if victor.sub >= 50:
        victor.say "It's not fair you doing that, [hero.name]..."
        victor.say "You, like, made me feel like a household pet!"
    elif victor.sub <= -50:
        victor.say "You can't do that to me, [hero.name]..."
        victor.say "In my line of work, I could react without even thinking!"
    else:
        victor.say "That's not cool, [hero.name]..."
        victor.say "I'm like a coiled spring - I could go off any second!"
    return

label victor_massage_intro_female:
    "Victor goes to make a perfectly normal movement, but stops in the middle of it."
    "And I can see that he's wincing in pain, but trying to hide it from me at the same time."
    victor.say "Argh!"
    if hero.morality >= 25:
        bree.say "Ooh...that looks painful!"
        bree.say "Would you like me to give you a massage?"
    elif hero.morality >= 25:
        bree.say "Man, that looks painful."
        bree.say "I could look at it if you like?"
        bree.say "I'm really good at pulling muscles!"
    else:
        bree.say "Ouch, Victor - looks like you pulled something there."
        bree.say "I give a pretty good massage, if you're interested?"
    return

label victor_massage_accept_female:
    "Victor nods slowly as he rubs the point where he's feeling the pain."
    victor.say "Yeah, I must have pulled a muscle on my last job."
    if victor.sub >= 50:
        victor.say "Of course you can give me a massage, [hero.name]."
        victor.say "Would you like to do it right now?"
    elif victor.sub <= -50:
        victor.say "Sounds like a good idea, [hero.name]..."
        victor.say "Just be sure to hit the right spot, okay?"
    else:
        victor.say "That sounds like a great idea, [hero.name]..."
        victor.say "I could use all he help I can get!"
    return

label victor_massage_refuse_female:
    "Victor seems to back off instinctively as soon as I suggest a massage."
    "Even though the movement that entails is obviously causing him even more pain."
    if victor.sub >= 50:
        victor.say "No, please, [hero.name]..."
        victor.say "I'm in enough pain already!"
    elif victor.sub <= -50:
        victor.say "Don't even think about touching me, [hero.name]!"
        victor.say "An amateur messing with my finely-tuned body could end my career."
    else:
        victor.say "Ah, no, [hero.name], I think I'll pass."
        victor.say "I should really get a professional to look at it."
    return

label victor_piercing_nipples_reaction_female:
    if victor.sub >= 50:
        victor.say "Surprise, [hero.name] - I finally did it..."
        victor.say "I got my nipples pierced!"
    elif victor.sub <= -50:
        victor.say "Check this out, [hero.name]..."
        victor.say "I got the most awesome piercings for my nipples!"
    else:
        victor.say "Well, [hero.name] - I went ahead and did it..."
        victor.say "I finally got my nipples pierced!"
    "As if he needs to prove the point to be believed, Victor pulls up his top."
    "And I get an eyeful of the piercings that he's talking about."
    if hero.morality >= 25:
        bree.say "Oh...that's very nice, Victor!"
    elif hero.morality >= 25:
        bree.say "Mmm...really sexy, Victor!"
    else:
        bree.say "Wow...those look great!"
    return

label victor_piercing_navel_reaction_female:
    if victor.sub >= 50:
        victor.say "Surprise, [hero.name] - I finally did it..."
        victor.say "I got my navel pierced!"
    elif victor.sub <= -50:
        victor.say "Check this out, [hero.name]..."
        victor.say "I got the most awesome piercing for my navel!"
    else:
        victor.say "Well, [hero.name] - I went ahead and did it..."
        victor.say "I finally got my navel pierced!"
    "As if he needs to prove the point to be believed, Victor pulls up his top."
    "And I get an eyeful of the piercing that he's talking about."
    if hero.morality >= 25:
        bree.say "Oh...that's very nice, Victor!"
    elif hero.morality >= 25:
        bree.say "Mmm...really sexy, Victor!"
    else:
        bree.say "Wow...that looks great!"
    return

label victor_piercing_dick_reaction_female:
    if victor.sub >= 50:
        victor.say "Surprise, [hero.name] - I finally did it..."
        victor.say "I got my dick pierced!"
    elif victor.sub <= -50:
        victor.say "Check this out, [hero.name]..."
        victor.say "I got the most awesome piercing for my dick!"
    else:
        victor.say "Well, [hero.name] - I went ahead and did it..."
        victor.say "I finally got my dick pierced!"
    "As if he needs to prove the point to be believed, Victor pulls out his waistband."
    "And I get an eyeful of the piercing that he's talking about."
    if hero.morality >= 25:
        bree.say "Oh...that's very nice, Victor!"
    elif hero.morality >= 25:
        bree.say "Mmm...really sexy, Victor!"
    else:
        bree.say "Wow...that looks great!"
    return

label victor_piercing_head_reaction_female:
    if victor.sub >= 50:
        victor.say "Surprise, [hero.name] - I finally did it..."
        victor.say "I got my tongue pierced!"
    elif victor.sub <= -50:
        victor.say "Check this out, [hero.name]..."
        victor.say "I got the most awesome piercing for my tongue!"
    else:
        victor.say "Well, [hero.name] - I went ahead and did it..."
        victor.say "I finally got my tongue pierced!"
    "As if he needs to prove the point to be believed, Victor sticks out his tongue."
    "And I get an eyeful of the piercing that he's talking about."
    if hero.morality >= 25:
        bree.say "Oh...that's very nice, Victor!"
    elif hero.morality >= 25:
        bree.say "Mmm...really sexy, Victor!"
    else:
        bree.say "Wow...that looks great!"
    return

label victor_piercing_nose_reaction_female:
    if victor.sub >= 50:
        victor.say "Surprise, [hero.name] - I finally did it..."
        victor.say "I got my nose pierced!"
    elif victor.sub <= -50:
        victor.say "Check this out, [hero.name]..."
        victor.say "I got the most awesome piercing for my nose!"
    else:
        victor.say "Well, [hero.name] - I went ahead and did it..."
        victor.say "I finally got my nose pierced!"
    "As if he needs to prove the point to be believed, Victor thrusts his nose towards me."
    "And I get an eyeful of the piercing that he's talking about."
    if hero.morality >= 25:
        bree.say "Oh...that's very nice, Victor!"
    elif hero.morality >= 25:
        bree.say "Mmm...really sexy, Victor!"
    else:
        bree.say "Wow...that looks great!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
