label cherie_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cherie_nvl "I had a great time the other night."
        cherie_nvl "Just wanted to let you know that."
        cherie_nvl "You really know how to treat a lady!"
    elif texto == 1:
        cherie_nvl "I can't seem to get you out of my mind."
        cherie_nvl "I know that makes me sound like a love-sick teenager!"
        cherie_nvl "But that's just how it is!"
    else:
        cherie_nvl "What have you got in mind for our next date?"
        cherie_nvl "I'm really excited to find out what it is!"
        cherie_nvl "And I haven't felt like this in years!"
    return

label cherie_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cherie_nvl "I know I shouldn't be doing this...but what the hell!"
        cherie_nvl "I can't stop thinking about you right now."
        cherie_nvl "And it's making me SO horny!"
    elif texto == 1:
        cherie_nvl "I'm just going through my wardrobe at home."
        cherie_nvl "I think it's time I had a clear-out and got some new outfits."
        cherie_nvl "You like me in stuff that's tight and short, right?"
    else:
        cherie_nvl "I wish you could just drop everything and come over here."
        cherie_nvl "I'm all on my own and I have nobody to keep me company."
        cherie_nvl "I'd love to have you inside of me..."
    return

label cherie_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cherie_nvl "I'm bored, just kicking around the house on my own."
        cherie_nvl "Are you free to come round here for a while?"
        cherie_nvl "If you do, you can stick your cock anywhere you like..."
    elif texto == 1:
        cherie_nvl "Mmm...I can still feel your cock inside me from the last time we did it."
        cherie_nvl "I hope it doesn't disappear before we do it again."
        cherie_nvl "And when we do, you'd better fuck me that hard all over again!"
    else:
        cherie_nvl "We need to come up with a list of exciting places to do it."
        cherie_nvl "I'll add the first one to the list, okay?"
        cherie_nvl "I want to suck your cock on Dwayne's bed!"
    return

label cherie_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Cherie, can you sneak out and meet me?"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "I'm dying to see you again!"
        cherie_nvl "Oh, I can't right now!"
        cherie_nvl "But thanks for asking - you made me feel like a naughty school-girl!"
        if persistent.difficulty >= 0:
            if cherie.love <= 50:
                $ cherie.love += 1
        else:
            $ cherie.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Cherie, how are you doing?"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        cherie_nvl "I'm doing okay, getting by - you know?"
        cherie_nvl "I feel better knowing there's someone out there who cares."
        if persistent.difficulty >= 0:
            if cherie.love <= 50:
                $ cherie.love += 1
        else:
            $ cherie.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Cherie, what's up?"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "I just wanted an excuse to talk to you!"
        cherie_nvl "Aw, that's okay!"
        cherie_nvl "I wanted to talk to you too."
        if persistent.difficulty >= 0:
            if cherie.love <= 50:
                $ cherie.love += 1
        else:
            $ cherie.love += 1
        $ hero.fun += 0.2
    return

label cherie_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Cherie - tell me what you're wearing?"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "I bet it's something sexy, right?"
        if (cherie.love <= 80 or cherie.sexperience == 0) and not hero.charm >= 30:
            cherie_nvl "I'm not going to tell you that!"
            cherie_nvl "I'm not some cheap teenage slut, you know!"
            $ cherie.love -= 1
        elif cherie.sexperience == 0 or (cherie.love <= 100 and not hero.charm >= 50):
            cherie_nvl "Oh my, you're SO naughty!"
            cherie_nvl "You know that you caught me getting dressed?"
            cherie_nvl "I only have on my bra and panties!"
            $ cherie.love += 1
        else:
            cherie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 100:
                    $ cherie.love += 1
            else:
                $ cherie.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I can't wait to see you again, Cherie."
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "When can you sneak out and meet me?"
        if (cherie.love <= 80 or cherie.sexperience == 0) and not hero.charm >= 30:
            cherie_nvl "I can't just drop everything!"
            cherie_nvl "I DO have a life of my own!"
            $ cherie.love -= 1
        elif cherie.sexperience == 0 or (cherie.love <= 100 and not hero.charm >= 50):
            cherie_nvl "Me too!"
            cherie_nvl "Give me a little time."
            cherie_nvl "I promise you it'll be worth it!"
            $ cherie.love += 1
        else:
            cherie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 100:
                    $ cherie.love += 1
            else:
                $ cherie.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't stop thinking about you, Cherie!"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "You're always on my mind!"
        if (cherie.love <= 80 or cherie.sexperience == 0) and not hero.charm >= 30:
            cherie_nvl "You need to back off a little."
            cherie_nvl "You're coming across as very needy right now!"
            $ cherie.love -= 1
        elif cherie.sexperience == 0 or (cherie.love <= 100 and not hero.charm >= 50):
            cherie_nvl "I know, I know!"
            cherie_nvl "You're all I can think about too!"
            $ cherie.love += 1
        else:
            cherie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 100:
                    $ cherie.love += 1
            else:
                $ cherie.love += 1
        $ hero.fun += 0.3
    return

label cherie_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Cherie, do me a favour, yeah?"
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "Put your hand into your panties and stroke your pussy for me!"
        if cherie.love <= 100 and not hero.charm >= 40:
            cherie_nvl "Oh stop it!"
            cherie_nvl "That's totally unacceptable!"
            $ cherie.love -= 2
        elif cherie.sexperience < 2 or cherie.love <= 150:
            cherie_nvl "Oh my goodness, you're SO outrageous!"
            cherie_nvl "Mmm...that feels really nice..."
            cherie_nvl "You make me SO wet!"
            $ cherie.love += 2
        else:
            cherie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 150:
                    $ cherie.love += 2
                elif cherie.love <= 175:
                    $ cherie.love += 1
            else:
                $ cherie.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I'm loving dating a mature woman, Cherie."
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "Having a MILF all of my own is pretty sweet."
        mchero_nvl "And fucking her is best of all!"
        if cherie.love <= 100 and not hero.charm >= 40:
            cherie_nvl "I've told you before - don't call me that!"
            cherie_nvl "It makes me feel ancient!"
            $ cherie.love -= 2
        elif cherie.sexperience < 2 or cherie.love <= 150:
            cherie_nvl "I love being your MILF."
            cherie_nvl "Especially the F in MILF!"
            cherie_nvl "When you put your C in my P!"
            $ cherie.love += 2
        else:
            cherie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 150:
                    $ cherie.love += 2
                elif cherie.love <= 175:
                    $ cherie.love += 1
            else:
                $ cherie.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Keep your pearls on next time we fuck, Cherie."
        if cherie.activity_name == "sleep" and cherie.love < 70:
            cherie_nvl "Leave me alone, I was asleep..."
            $ cherie.love -= 2
            return
        mchero_nvl "I want to grab hold of them like a collar!"
        if cherie.love <= 100 and not hero.charm >= 40:
            cherie_nvl "Erm...I don't think so!"
            cherie_nvl "Do you even know how valuable those things are?!?"
            $ cherie.love -= 2
        elif cherie.sexperience < 2 or cherie.love <= 150:
            cherie_nvl "Oh my...that sounds so kinky!"
            cherie_nvl "Like I'm your bitch!"
            cherie_nvl "And I need to be taught a lesson!"
            $ cherie.love += 2
        else:
            cherie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cherie.love <= 150:
                    $ cherie.love += 2
                elif cherie.love <= 175:
                    $ cherie.love += 1
            else:
                $ cherie.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
