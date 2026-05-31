init python:
    Event(**{
    "name": "emma_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "emma",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label emma_birthday_gift_male:
    show emma
    if emma.flags.birthdayknown:
        mike.say "Happy birthday, Emma!"
        emma.say "How sweet, you remembered my birthday!"
    else:
        emma.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ emma.flags.birthdayknown = True
    return

label emma_gift_swimsuit_male:
    show emma happy
    emma.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if emma.sub >= 60:
        show emma blush
        "Emma squeaks at opening my gift."
        emma.say "Thank you [hero.name]."
        $ emma.flags.sexyswimsuit = True
    else:
        show emma annoyed
        $ emma.love -= 4
        emma.say "Thanks but no thanks [hero.name], I thought you were better than this."
        $ hero.cancel_activity()
    return

label emma_gift_sexy_dress_male:
    show emma happy
    emma.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if emma.sub >= 30:
        show emma blush
        emma.say "Thank you [hero.name]."
        $ emma.flags.sexydate = True
        $ emma.flags.sluttydate = False
    else:
        show emma annoyed
        $ emma.love -= 4
        emma.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label emma_gift_slutty_dress_male:
    "Normally I'd be pretty excited to have a surprise gift for a girl I'm dating."
    "Looking forward to seeing the surprise on their face when I whip it out in front of them."
    "Ah...yeah...that might have come out a little wrong!"
    "What I mean is that I have a gift for her, wrapped up in a nice, fancy box."
    "But the problem is that I've decided to take a little bit of a risk with this one."
    "Which is kind of compounded by the fact that Emma can be..."
    "Well...she can be a little more shy and retiring that the average girl."
    "But one thing that she's most certainly not is unaware of her surroundings."
    "As she seems to spot what I'm up to the moment she lays eyes on me!"
    show emma talkative
    emma.say "[hero.name]..."
    emma.say "Call me nosy if you like..."
    emma.say "But I can't help wondering - what's that behind your back?"
    show emma normal
    "I do the best I can to feign ignorance, frowning and shaking my head."
    mike.say "What are you talking about, Emma?"
    mike.say "There's nothing to see back there."
    "Emma does the best she can to look over my shoulder."
    "But I keep the act up, turning to keep her in front of me."
    show emma whining
    emma.say "Stop it, [hero.name]..."
    emma.say "Don't be so mean to me!"
    show emma normal
    "Finally I decide that Emma's been tortured enough."
    "And so I relent, pulling out the box and handing it over to her."
    mike.say "Okay, okay...I admit it."
    mike.say "I do have a little something for you."
    show emma happy
    "Emma's face lights up as she takes the box from me."
    play sound [paper_ripping_2, paper_ripping_1]
    "And she doesn't hesitate to start unwrapping it too."
    emma.say "Oh wow..."
    emma.say "I can't wait to see what it is!"
    "Emma's amazement only seems to increase as she pulls out what's inside."
    show emma stuned
    "Her eyes going wide as a slinky, daring dress unfolds in her hands."
    mike.say "So..."
    mike.say "What do you think?"
    mike.say "Pretty nice, right?"
    if emma.sub >= 70:
        "Emma's eyes are still wide as she turns to look at me."
        "Filled with disbelief and not a little intrigue too."
        show emma talkative
        emma.say "You're serious, [hero.name]?"
        emma.say "You really think I could pull something like this off?"
        show emma normal
        "I don't hesitate to nod."
        mike.say "You totally could, Emma."
        mike.say "I wouldn't have bought it for you if I didn't believe that."
        "Emma's slowly starting to nod too."
        "As if my confidence is infectious."
        show emma talkative
        emma.say "I mean, I always wanted to try it..."
        emma.say "But I was never confident enough."
        emma.say "Though, if you believe I can do it..."
        show emma blush
        mike.say "Emma, I believe you can do anything..."
        mike.say "Anything at all!"
        "Well, it'd be more honest to say I believe she'll look super-hot in that dress."
        "Aside from that, I'd want to look at other goals on a case-to-case basis."
        "But that's not the kind of talk that'll get Emma's ass into the dress."
        "And right now, the lines I'm giving her seem to be working pretty well."
        show emma happy
        emma.say "You're right, [hero.name]..."
        emma.say "I've been holding back too long."
        emma.say "So I'm going to wear this damn sexy dress."
        emma.say "And anyone that doesn't like it can..."
        emma.say "They can go to hell!"
        mike.say "That's the spirit, Emma - you go for it!"
        $ emma.flags.sexydate = False
        $ emma.flags.sluttydate = True
    else:
        "Emma's eyes are still wide as she turns to look at me."
        "But I can see that now the emotion in them is horror, rather than amazement."
        show emma angry
        emma.say "Pretty nice?"
        emma.say "How can you think this is pretty nice?!?"
        emma.say "This is the kind of thing a stripper would wear!"
        emma.say "Is that really what you think of me?"
        show emma upset
        "I'm already shaking my head as I struggle to explain myself."
        mike.say "NO!"
        mike.say "Of course not, Emma..."
        mike.say "It's not exactly like something a stripper would wear."
        mike.say "I mean sure, it's skimpy in places."
        mike.say "But their stuff tends to have more tassels and show more ass."
        "Emma tosses the dress at me as she backs away."
        show emma angry
        emma.say "That's not helping, [hero.name]!"
        emma.say "I...I think I need to get some air."
        show emma upset
        mike.say "Don't worry, I know just the place."
        show emma angry
        emma.say "No, I need to be somewhere you're not!"
        show emma upset
        "With that, Emma turns on her heel and hurries away."
        "Leaving me to reflect on how I just took a massive risk."
        "And it most definitely did not pay off."
        $ emma.love -= 10
        $ hero.cancel_activity()
    return

label emma_gift_collar_male:
    show emma
    "I've been thinking about my relationship with Emma for a while now."
    "And I mean really thinking about it, seriously and in a depth!"
    "I feel like we're at a point where I need to make a gesture, you know?"
    "To do something that'll show her how committed I am and how much I love her."
    "I know that giving her a gift is a massive cliche."
    "And making it something to wear takes the cliche to the next level too."
    "But I really feel like I've put a lot of thought into this."
    "Like the gift that I've settled on for Emma will sum everything up."
    "It'll let her know how special she is to me."
    "And it'll also be a constant reminder of our unique relationship."
    "Once I have the box containing the gift in my hand, everything's ready."
    "I'm positively itching to hand it over and see her reaction."
    "All I have to do is choose the right moment..."
    show emma annoyed
    emma.say "Erm, [hero.name]..."
    emma.say "Why are you acting so weird?"
    mike.say "Huh?"
    mike.say "What are you talking about, Emma?"
    mike.say "I'm acting perfectly normal!"
    "Emma narrows her eyes and shakes her head."
    "Which pretty much lets me know that she's not buying it."
    show emma normal
    emma.say "No you're not."
    emma.say "You're being all shifty and evasive."
    emma.say "It's like you're trying to hide something from me!"
    "Oh no - I'm straying into the danger zone!"
    "She's starting to think I'm not telling her some kind of bad news."
    "If I'm going to do this thing, then I have to do it now!"
    mike.say "Okay, Emma, okay..."
    mike.say "You got me."
    mike.say "I am keeping something from you."
    mike.say "But it's just that I got you a gift."
    mike.say "And I wanted it to be a surprise!"
    "As soon as the words are out of my mouth, I see a change in Emma."
    "Where before she was suspicious, now she begins to look embarrassed."
    "Her cheeks flush as she looks down at the gift-box in my hands."
    show emma happy
    emma.say "Oh, [hero.name]..."
    emma.say "Now I feel like such a moron!"
    emma.say "I should have known you had something so sweet in mind!"
    "I feel my mood beginning to lift at the same time as Emma's."
    "And yeah, it does feel good to have proven her wrong."
    "I just can't wait to see the look on her face when she opens it!"
    "Emma eagerly accepts the box and tears off the wrapping."
    "Then she opens it and peeks inside, wanting to see what I got her."
    emma.say "Oh..."
    emma.say "Oh my..."
    show emma normal
    emma.say "Oh my goodness!"
    "Emma's eyes are as wide as I've ever seen them right now."
    "She's holding up my gift, a slender collar of purple leather."
    "It's buckle and the heart-shaped decoration in the middle are gold in colour."
    "The bell hanging from it is the same colour too."
    "And if I've got my measurements right, it should fit her perfectly."
    mike.say "Well..."
    mike.say "What do you think, Emma?"
    mike.say "I feel like you've been giving me signals all the time we've been together."
    mike.say "You remind me of a cute little kitten, one that like to be pampered too."
    mike.say "And when you wear that collar, everyone else will know that."
    mike.say "It'll be like you're declaring it to the rest of the world!"
    "Emma stares at me in complete silence as I say all of this."
    "And it's hard for me to read what effect my words are having on her."
    "But then she slowly starts to speak..."
    emma.say "[hero.name]..."
    if emma.sub >= 90:
        emma.say "How could you know that about me?!?"
        emma.say "I've always had that feeling."
        emma.say "It's been deep down inside of me forever."
        emma.say "But I never knew how to describe it before now!"
        "I can feel my head nodding faster and faster as Emma explains herself."
        "This is turning out better than I could have hoped."
        mike.say "Y...you mean you like it?"
        emma.say "Oh, [hero.name]..."
        show emma happy
        emma.say "I absolutely love it!"
        emma.say "Put it on me, okay?"
        "Emma hands me the collar and turns around to let me do as she asks."
        "Luckily for me, it fits perfectly, sitting comfortably around her neck."
        $ emma.set_sex_slave()
        show emma blush
        emma.say "Well, [hero.name]..."
        emma.say "How do I look?"
        emma.say "Purr, purr, purr..."
        emma.say "Am I cute enough to be your little kitty cat?"
        "Emma bats at the air with her hands."
        "And then she pretends to clean herself like a cat."
        "All the time the little gold bell on the collar is tinkling away like crazy."
        "She's already starting to turn me on!"
        "I wonder if I can get her to act like that in private?"
        "Maybe in my bedroom..."
        "But I decide to keep that thought to myself for the time being."
        "No sense in spoiling the moment by pushing my luck too far."
        mike.say "You look perfect, Emma."
        mike.say "Like the cutest cat ever!"
        show emma happy
        "Emma smiles and then throws her arms around me."
        "I return the hug, lifting her off the ground a little too."
        "But the whole time I'm worried that she's going to feel how hard she's making me right now!"
        $ emma.love += 2
        $ emma.sub += 5
    else:
        emma.say "How could you buy me something like this?!?"
        emma.say "It's the kind of thing an...an animal wears!"
        emma.say "Is that really how you see me?"
        show emma fear
        emma.say "Like I'm your pet?!?"
        "I wave my hands in the air, trying to dismiss Emma's questions."
        "I can't believe that she's taking it like this."
        "Like my gift is some kind of insult!"
        mike.say "No, no, no..."
        mike.say "You've got it all wrong, Emma!"
        mike.say "This is a good thing, yeah?"
        mike.say "It means that I get you on a fundamental level!"
        "Emma doesn't dignify that with an answer."
        show emma angry
        "She just flings the collar down at my feet with a snort."
        "The little gold bell rings pathetically as it hits the ground."
        "And then she turns on her heel and storms off."
        hide emma
        "I watch her go as I bend down to pick up the collar."
        "Part of me still not really able to understand what just happened."
        "How come she didn't see what I was getting at?"
        "Did I get it that badly wrong?"
        "Did I completely misread Emma?"
        "No, of course not."
        "I'm really good when it comes to this kind of thing."
        "It must be Emma that's at fault here."
        "I just need a chance to talk her round, that's all..."
        $ emma.love -= 20
        $ emma.sub -= 10
        $ hero.cancel_activity()
    return

label emma_give_male:
    "She hands me a box, obviously from a pastry shop."
    mike.say "Thanks."
    $ hero.gain_item("cake")
    return

label emma_give_valentine_male:
    "Emma walks hesitantly towards me."
    call emma_greet from _call_emma_greet_7
    show emma blush
    emma.say "Happy valentine's day [hero.name]..."
    "Emma hands me a box of chocolates."
    mike.say "Thank you, Emma."
    $ hero.gain_item("valentine_chocolates")
    return

label emma_give_birthday_male:
    "Emma walks towards me."
    call emma_greet from _call_emma_greet_8
    show emma happy
    emma.say "Happy birthday [hero.name]!"
    call emma_give_male from _call_emma_give_male
    return

label emma_give_christmas_male:
    "Emma walks towards me."
    call emma_greet from _call_emma_greet_9
    show emma happy
    emma.say "Merry Christmas [hero.name]."
    call emma_give_male from _call_emma_give_male_1
    return

label emma_gift_butt_plug_male:
    show emma happy
    emma.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if emma.sub <= 50 or not emma.sexperience:
        show emma annoyed
        emma.say "..."
        emma.say "Keep it... I don't want it so keep it."
        emma.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        emma.say "It's perfect!"
        emma.say "Thanks [hero.name], I'll make a good use of it."
        $ emma.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
