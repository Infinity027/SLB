label camila_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        camila_nvl "Hey, I wondered if you were free to chat?"
        camila_nvl "I kind of had a hard day at work."
        camila_nvl "And I need to hear a friendly voice."
    elif texto == 1:
        camila_nvl "It's weird, but I keep finding you're on my mind."
        camila_nvl "No matter what I'm doing, I end up thinking about you!"
        camila_nvl "Do you think about me like that?"
    else:
        camila_nvl "You sure picked a great spot for that last date!"
        camila_nvl "You want me to take a turn choosing next time?"
        camila_nvl "Or have you got another great one up your sleeve?"
    return

label camila_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        camila_nvl "Phew...I just got off a pretty heavy raid."
        camila_nvl "It got physical and now I'm bruised...and sweaty too!"
        camila_nvl "Weird thing is, it's making me feel kinda horny..."
    elif texto == 1:
        camila_nvl "I'm getting off my shift in an hour or so."
        camila_nvl "Mind if I come straight over to your place when I'm done?"
        camila_nvl "I promise I'll bring my handcuffs and night-stick with me!"
    else:
        camila_nvl "We had a martial arts guy come show us some holds at the station today."
        camila_nvl "He was great - taught me some pretty cool methods of restraint."
        camila_nvl "You want me to show you some of them when we're alone?"
    return

label camila_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        camila_nvl "Would you put my hand-cuffs on me and then strip me naked?"
        camila_nvl "Then pretend to be a crook that's captured me while we do it?"
        camila_nvl "I know it sounds weird - but the idea turns me on!"
    elif texto == 1:
        camila_nvl "Can I come over and take a swim in your pool after work?"
        camila_nvl "I feel like I could use the chance to unwind, yeah?"
        camila_nvl "Plus, if your housemates are out, I'll suck your cock to say thanks, okay?"
    else:
        camila_nvl "I'm hiding contraband somewhere on my person."
        camila_nvl "And I want you to find it for me, okay?"
        camila_nvl "I want you to do deep on it too, if you know what I mean?"
    return

label camila_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Camila, I just got off work."
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "You want to meet up and just hang out?"
        camila_nvl "Nah, I got switched onto the night shift."
        camila_nvl "No rest for the wicked - not while I'm on the job!"
        if persistent.difficulty >= 0:
            if camila.love <= 50:
                $ camila.love += 1
        else:
            $ camila.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Camila, someone let their dog take a crap on my lawn!"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "Can you...I dunno, arrest them for me or something?"
        camila_nvl "HEY!"
        camila_nvl "That's kind of below my pay grade, you know?!?"
        if persistent.difficulty >= 0:
            if camila.love <= 50:
                $ camila.love += 1
        else:
            $ camila.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Camila, how's the toughest cop on the force doing today?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        camila_nvl "She's doing her best to fight the rising tide of crime."
        camila_nvl "But she's also thinking about this cute guy she knows too!"
        if persistent.difficulty >= 0:
            if camila.love <= 50:
                $ camila.love += 1
        else:
            $ camila.love += 1
        $ hero.fun += 0.2
    return

label camila_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Camila - would you handcuff me and threaten me with your nightstick?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "I think it'd be some pretty kinky fun!"
        if (camila.love <= 80 or camila.sexperience == 0) and not hero.charm >= 30:
            camila_nvl "Keep talking like that and I'll cuff you for real, mister!"
            $ camila.love -= 1
        elif camila.sexperience == 0 or (camila.love <= 100 and not hero.charm >= 50):
            camila_nvl "Be careful what you ask for..."
            camila_nvl "I don't think your manhood can handle my nightstick!"
            $ camila.love += 1
        else:
            camila_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if camila.love <= 100:
                    $ camila.love += 1
            else:
                $ camila.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "Camila...do you have a cop uniform?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "You know...like one you could wear in the bedroom?"
        if (camila.love <= 80 or camila.sexperience == 0) and not hero.charm >= 30:
            camila_nvl "Nah, I don't think so."
            camila_nvl "I'd have to pay to have the stains removed when you were done with it..."
            $ camila.love -= 1
        elif camila.sexperience == 0 or (camila.love <= 100 and not hero.charm >= 50):
            camila_nvl "No, but I could maybe get one?"
            camila_nvl "One with a short skirt and a cropped top?"
            $ camila.love += 1
        else:
            camila_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if camila.love <= 100:
                    $ camila.love += 1
            else:
                $ camila.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "You want to come to a nightclub I just found, Camila?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "It's full of nice, dark corners where nobody can see what we're doing!"
        if (camila.love <= 80 or camila.sexperience == 0) and not hero.charm >= 30:
            camila_nvl "No way, no how, not happening!"
            camila_nvl "I like to be able to see what's going on around me!"
            $ camila.love -= 1
        elif camila.sexperience == 0 or (camila.love <= 100 and not hero.charm >= 50):
            camila_nvl "I like the sound of that!"
            camila_nvl "What happens in the shadows stays in the shadows!"
            $ camila.love += 1
        else:
            camila_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if camila.love <= 100:
                    $ camila.love += 1
            else:
                $ camila.love += 1
        $ hero.fun += 0.3
    return

label camila_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Camila, do me a favour, yeah?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "Put your hand into your panties and stroke your pussy for me!"
        if camila.love <= 100 and not hero.charm >= 40:
            camila_nvl "I'm sure there's a law against this kind of harassment..."
            $ camila.love -= 2
        elif camila.sexperience < 2 or camila.love <= 150:
            camila_nvl "You've not some nerve, mister!"
            camila_nvl "But that does feel good!"
            camila_nvl "And I'm getting SO wet..."
            $ camila.love += 2
        else:
            camila_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if camila.love <= 150:
                    $ camila.love += 2
                elif camila.love <= 175:
                    $ camila.love += 1
            else:
                $ camila.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Camila, could you come over here straight after your get off work?"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "I want to fuck you in your uniform!"
        mchero_nvl "And while you still have the grime of the street on you too!"
        if camila.love <= 100 and not hero.charm >= 40:
            camila_nvl "Jesus, man - do you think of anything else?!?"
            camila_nvl "Just watch some porn and jerk-off!"
            $ camila.love -= 2
        elif camila.sexperience < 2 or camila.love <= 150:
            camila_nvl "Hmm...I DO get a little horny when I'm done working."
            camila_nvl "But you'd better be ready for me - and fuck me hard!"
            $ camila.love += 2
        else:
            camila_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if camila.love <= 150:
                    $ camila.love += 2
                elif camila.love <= 175:
                    $ camila.love += 1
            else:
                $ camila.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Camila, I've got a nightstick right here with your name on it!"
        if camila.activity_name == "sleep" and camila.love < 70:
            camila_nvl "Leave me alone, I was asleep..."
            $ camila.love -= 2
            return
        mchero_nvl "It's extendable too!"
        if camila.love <= 100 and not hero.charm >= 40:
            camila_nvl "You want me to bring a real one over there, huh?"
            camila_nvl "We can see how you like one shoved up your hole!"
            $ camila.love -= 2
        elif camila.sexperience < 2 or camila.love <= 150:
            camila_nvl "It'd better be a big one, and hard too!"
            camila_nvl "I tested my last one to destruction!"
            $ camila.love += 2
        else:
            camila_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if camila.love <= 150:
                    $ camila.love += 2
                elif camila.love <= 175:
                    $ camila.love += 1
            else:
                $ camila.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
