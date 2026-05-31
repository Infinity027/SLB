label hanna_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        hanna_nvl "I can't keep my mind on my work-out today."
        hanna_nvl "You're distracting me every time I think of you!"
        hanna_nvl "And that's just when you're not here with me!"
    elif texto == 1:
        hanna_nvl "I've got a little spare time between classes right now."
        hanna_nvl "And I wondered if you wanted to chat for a while?"
        hanna_nvl "Unless you're busy or you have something better to do..."
    else:
        hanna_nvl "Good call on our date the other night."
        hanna_nvl "That's something I'd never have thought of doing!"
        hanna_nvl "Gonna be hard to top that on the next one!"
    return

label hanna_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        hanna_nvl "I just finished my last class of the day."
        hanna_nvl "I'm all sweaty, and my work-out gear's sticking to me!"
        hanna_nvl "I don't know why - but my nipples are super-hard too!"
    elif texto == 1:
        hanna_nvl "I'm picking out my clothes for our next date."
        hanna_nvl "I don't know where you were wanting to go."
        hanna_nvl "But I can pull off cycling shorts and a tube-top, right?"
    else:
        hanna_nvl "You doing anything right now?"
        hanna_nvl "If not, come over here and we can work-out together."
        hanna_nvl "I know a really fun way to burn some weight off!"
    return

label hanna_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        hanna_nvl "I look good in this outfit, right?"
        hanna_nvl "Good enough to eat, yeah?"
        hanna_nvl "Good enough to fuck?"
    elif texto == 1:
        hanna_nvl "I didn't burn off quite enough at the gym today."
        hanna_nvl "So help a girl out, yeah?"
        hanna_nvl "Fuck me until I sweat?"
        hanna_nvl "That way I can make up the difference."
    else:
        hanna_nvl "Hey, you look really good today!"
        hanna_nvl "And that's not fair - I'm supposed to get all the attention!"
        hanna_nvl "You're going to have to make it up to me somehow..."
        hanna_nvl "Maybe by going down on me?"
    return

label hanna_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Hanna, what are you up to right now?"
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        hanna_nvl "Just grabbing an extra workout session at the gym."
        hanna_nvl "You want to come join me?"
        mchero_nvl "Ah...I think I'll pass."
        if persistent.difficulty >= 0:
            if hanna.love <= 50:
                $ hanna.love += 1
        else:
            $ hanna.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Hanna, since we're friends and all that..."
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "I was wondering if you might let me off my gym fees?"
        mchero_nvl "You know, as a favour?"
        hanna_nvl "I'm going to pretend I didn't read that, okay?"
        if persistent.difficulty >= 0:
            if hanna.love <= 50:
                $ hanna.love += 1
        else:
            $ hanna.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Hanna, you want to hang out in the park?"
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "We could go for a stroll or sit on the grass, or something."
        hanna_nvl "Nah, the weather's not decent enough."
        hanna_nvl "There'll be nobody to see me there!"
        if persistent.difficulty >= 0:
            if hanna.love <= 50:
                $ hanna.love += 1
        else:
            $ hanna.love += 1
        $ hero.fun += 0.2
    return

label hanna_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Hanna, I'm thinking about you right now."
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "How about you help me out and tell me what you're wearing?"
        if (hanna.love <= 80 or hanna.sexperience == 0) and not hero.charm >= 30:
            hanna_nvl "I don't have time to help you get off!"
            hanna_nvl "I have a workout schedule to keep!"
            $ hanna.love -= 1
        elif hanna.sexperience == 0 or (hanna.love <= 100 and not hero.charm >= 50):
            hanna_nvl "I'm wearing my lycra, because I'm working out."
            hanna_nvl "It's SO tight and it feels SO against my body!"
            $ hanna.love += 1
        else:
            hanna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 100:
                    $ hanna.love += 1
            else:
                $ hanna.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I'm going mad being away from you, Hanna!"
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "All I can think about is touching your body!"
        mchero_nvl "When can I see you again?"
        if (hanna.love <= 80 or hanna.sexperience == 0) and not hero.charm >= 30:
            hanna_nvl "You're being really needy right now."
            hanna_nvl "And I'm just not into that."
            $ hanna.love -= 1
        elif hanna.sexperience == 0 or (hanna.love <= 100 and not hero.charm >= 50):
            hanna_nvl "I feel the same way!"
            hanna_nvl "I'll be with you as soon as I can!"
            $ hanna.love += 1
        else:
            hanna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 100:
                    $ hanna.love += 1
            else:
                $ hanna.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "You want to go for a walk in the woods, Hanna?"
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "It's great exercise - and maybe we could do more?"
        mchero_nvl "Some extreme physical exercise once we're alone?"
        if (hanna.love <= 80 or hanna.sexperience == 0) and not hero.charm >= 30:
            hanna_nvl "I'm not going into the woods to have you feel me up!"
            hanna_nvl "I know what it feels like to sit in poison ivy!"
            $ hanna.love -= 1
        elif hanna.sexperience == 0 or (hanna.love <= 100 and not hero.charm >= 50):
            hanna_nvl "I like the sound of that!"
            hanna_nvl "Burning off some excess weight in the bosom of mother nature!"
            $ hanna.love += 1
        else:
            hanna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 100:
                    $ hanna.love += 1
            else:
                $ hanna.love += 1
        $ hero.fun += 0.3
    return

label hanna_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "How did your workout go, Hanna?"
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "I keep thinking about how slippery and shiny you must be when you're done!"
        if hanna.love <= 100 and not hero.charm >= 40:
            hanna_nvl "Hey, I work out to keep in shape!"
            hanna_nvl "Not to give you something to wank over!"
            $ hanna.love -= 2
        elif hanna.sexperience < 2 or hanna.love <= 150:
            hanna_nvl "Oh yeah...I'm SO sweaty that I'm dripping!"
            hanna_nvl "You could just slide straight into me..."
            $ hanna.love += 2
        else:
            hanna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 150:
                    $ hanna.love += 2
                elif hanna.love <= 175:
                    $ hanna.love += 1
            else:
                $ hanna.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I'm just thinking about you in your work-out gear, Hanna."
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "You know - the stuff that's so tight everything's on show?"
        if hanna.love <= 100 and not hero.charm >= 40:
            hanna_nvl "So that's why you like me to wear that stuff, huh?"
            hanna_nvl "Consider yourself busted, mister!"
            $ hanna.love -= 2
        elif hanna.sexperience < 2 or hanna.love <= 150:
            hanna_nvl "Oh, I know the ones you mean!"
            hanna_nvl "They feel SO tight against my pussy!"
            hanna_nvl "So tight it makes me horny..."
            $ hanna.love += 2
        else:
            hanna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 150:
                    $ hanna.love += 2
                elif hanna.love <= 175:
                    $ hanna.love += 1
            else:
                $ hanna.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You should do a workout video, Hanna."
        if hanna.activity_name == "sleep" and hanna.love < 70:
            hanna_nvl "Leave me alone, I was asleep..."
            $ hanna.love -= 2
            return
        mchero_nvl "It'd be SO hot to see you stretching and bending over!"
        if hanna.love <= 100 and not hero.charm >= 40:
            hanna_nvl "Yeah, and help you play with yourself too!"
            $ hanna.love -= 2
        elif hanna.sexperience < 2 or hanna.love <= 150:
            hanna_nvl "That's such a idea!"
            hanna_nvl "You could help me practice too."
            hanna_nvl "Help me work on those certain muscles between my legs..."
            $ hanna.love += 2
        else:
            hanna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if hanna.love <= 150:
                    $ hanna.love += 2
                elif hanna.love <= 175:
                    $ hanna.love += 1
            else:
                $ hanna.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
