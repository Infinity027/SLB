

label ayesha_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        ayesha_nvl "Hey, I'm wearing my wrestling gear right now."
        ayesha_nvl "The tights that you really like - the one's with the leopard print."
        ayesha_nvl "Just thought you might want to know..."
    elif texto == 1:
        ayesha_nvl "Phew...I just got done working out for the day."
        ayesha_nvl "I'm so sore and covered in sweat right now!"
        ayesha_nvl "But I'll be thinking of you as I soap myself up in the shower..."
    else:
        ayesha_nvl "Tell me more about the book you're reading when we next meet up, yeah?"
        ayesha_nvl "I like people to know that my man's got a big brain on him."
        ayesha_nvl "It's really sexy!"
    return

label ayesha_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        ayesha_nvl "I wanted to ask you something..."
        ayesha_nvl "I have a pair of wrestling tights that'd fit you, yeah?"
        ayesha_nvl "Would you wear them and...well...pin me down?"
        ayesha_nvl "Then fuck me REAL hard?"
    elif texto == 1:
        ayesha_nvl "After my next match, would you peel me out of my ring-gear?"
        ayesha_nvl "And...and then make love to me once you're done?"
        ayesha_nvl "I want to feel you inside of me when I'm tender from the ring."
        ayesha_nvl "And feel you cum in me when my adrenaline's up too!"
    else:
        ayesha_nvl "Can we take a dip in your pool?"
        ayesha_nvl "Maybe when your housemates are all out?"
        ayesha_nvl "I want to take a dip in the water."
        ayesha_nvl "And have you take a dip in me too!"
    return

label ayesha_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Ayesha, how much can you actually lift?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        ayesha_nvl "More than you with one hand!"
        mchero_nvl "Oh...okay, Ayesha - sorry I asked!"
        if persistent.difficulty >= 0:
            if ayesha.love <= 50:
                $ ayesha.love += 1
        else:
            $ ayesha.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Ayesha, you want to come see a boxing match?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "I think I can score us some free tickets!"
        ayesha_nvl "Nah, boxing's a little too real for me - too brutal."
        if persistent.difficulty >= 0:
            if ayesha.love <= 50:
                $ ayesha.love += 1
        else:
            $ ayesha.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Ayesha, you want to go grab a drink?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        ayesha_nvl "Thanks for the offer, but I'm busy right now."
        ayesha_nvl "How about I call you when I'm free?"
        if persistent.difficulty >= 0:
            if ayesha.love <= 50:
                $ ayesha.love += 1
        else:
            $ ayesha.love += 1
        $ hero.fun += 0.2
    return

label ayesha_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "When can I see you again, Ayesha?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "You're all I can think about!"
        mchero_nvl "Your eyes, your lips, your body!"
        if (ayesha.love <= 80 or ayesha.sexperience == 0) and not hero.charm >= 30:
            ayesha_nvl "Stop it - right now!"
            ayesha_nvl "I don't have time for this!"
            $ ayesha.love -= 1
        elif ayesha.sexperience == 0 or (ayesha.love <= 100 and not hero.charm >= 50):
            ayesha_nvl "Stop it - you're making me blush!"
            ayesha_nvl "It'll be soon, I promise!"
            $ ayesha.love += 1
        else:
            ayesha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 100:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "Hey, Ayesha - are you wearing your work-out gear right now?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "The stuff that shows off all of your muscles?"
        if (ayesha.love <= 80 or ayesha.sexperience == 0) and not hero.charm >= 30:
            ayesha_nvl "Don't talk about it like that!"
            ayesha_nvl "Why do you have to make everything dirty?!?"
            $ ayesha.love -= 1
        elif ayesha.sexperience == 0 or (ayesha.love <= 100 and not hero.charm >= 50):
            ayesha_nvl "I might be!"
            ayesha_nvl "And I might be flexing in it right now!"
            $ ayesha.love += 1
        else:
            ayesha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 100:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I'm thinking of your hands all over me, Ayesha."
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "Holding me down and overpowering me!"
        if (ayesha.love <= 80 or ayesha.sexperience == 0) and not hero.charm >= 30:
            ayesha_nvl "That's creepy and wrong!"
            ayesha_nvl "You make it sound like I'm some kind of animal!"
            $ ayesha.love -= 1
        elif ayesha.sexperience == 0 or (ayesha.love <= 100 and not hero.charm >= 50):
            ayesha_nvl "Oh, I could do that!"
            ayesha_nvl "I could tie you up like a pretzel if you'd like?"
            $ ayesha.love += 1
        else:
            ayesha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 100:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 1
        $ hero.fun += 0.3
    return

label ayesha_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I can't wait to feel your arms around me again, Ayesha."
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "You make me feel so safe, so secure."
        mchero_nvl "And your pussy...it's so soft and warm!"
        if ayesha.love <= 100 and not hero.charm >= 40:
            ayesha_nvl "Geez...you make it sound like I'm going to crush the life out of you!"
            $ ayesha.love -= 2
        elif ayesha.sexperience < 2 or ayesha.love <= 150:
            ayesha_nvl "You can have me as soon as I see you!"
            ayesha_nvl "I want your cock in me so badly!"
            $ ayesha.love += 2
        else:
            ayesha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 150:
                    $ ayesha.love += 2
                elif ayesha.love <= 175:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Ayesha...this sounds a bit weird...but hear me out, yeah?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "Could I like...maybe fuck you in your wrestling gear?"
        if ayesha.love <= 100 and not hero.charm >= 40:
            ayesha_nvl "No way is that happening!"
            ayesha_nvl "Do you even know how much that stuff costs?!?"
            $ ayesha.love -= 2
        elif ayesha.sexperience < 2 or ayesha.love <= 150:
            ayesha_nvl "Oh...okay, that was a little unexpected!"
            ayesha_nvl "But...yeah...now I think about it - that sounds pretty kinky!"
            $ ayesha.love += 2
        else:
            ayesha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 150:
                    $ ayesha.love += 2
                elif ayesha.love <= 175:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Ayesha, are you working out right now?"
        if ayesha.activity_name == "sleep" and ayesha.love < 70:
            ayesha_nvl "Leave me alone, I was asleep..."
            $ ayesha.love -= 2
            return
        mchero_nvl "I can just imagine you covered in a sheen of perspiration."
        mchero_nvl "And it's making me SO hard for you!"
        if ayesha.love <= 100 and not hero.charm >= 40:
            ayesha_nvl "Get lost!"
            ayesha_nvl "I don't need you distracting me in the middle of a work-out!"
            $ ayesha.love -= 2
        elif ayesha.sexperience < 2 or ayesha.love <= 150:
            ayesha_nvl "Got it in one - I am working out."
            ayesha_nvl "But since I heard from you, the wettest part of me is my pussy!"
            $ ayesha.love += 2
        else:
            ayesha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if ayesha.love <= 150:
                    $ ayesha.love += 2
                elif ayesha.love <= 175:
                    $ ayesha.love += 1
            else:
                $ ayesha.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
