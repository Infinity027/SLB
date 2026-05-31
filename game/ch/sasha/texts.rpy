label sasha_friendly_texts:
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0 and 'practice_band' in DONE:
        sasha_nvl "You sounded pretty hot at band practice the other night."
        sasha_nvl "I never realised we needed another guitarist so badly!"
        sasha_nvl "And the great thing is that you fit right in too!"
    elif texto == 1 and sasha.flags.last_date_day:
        sasha_nvl "Had a great time on our date - it was a blast!"
        sasha_nvl "But I get to pick where we go next time, okay?"
        sasha_nvl "And I'm gonna blow you away too!"
    else:
        sasha_nvl "Damn it - I can't stop thinking about you!"
        sasha_nvl "What did you do to me?!?"
        sasha_nvl "You'd better be thinking about me too!"
    return

label sasha_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        sasha_nvl "You wanna come up to my room and jam with me?"
        sasha_nvl "We can play with each other in private."
        sasha_nvl "If you get my meaning!"
    elif texto == 1:
        sasha_nvl "I'm buying some new clothes, yeah?"
        sasha_nvl "Just checking you're okay with my choices."
        sasha_nvl "I'm going for skimpy, ripped and black, okay?"
    else:
        sasha_nvl "If you're gonna buy a new Metallikea T-shirt, get the right size, okay?"
        sasha_nvl "The ones you have right now are WAY too big for you."
        sasha_nvl "Make sure you get one that's nice and tight, yeah?"
    return

label sasha_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        sasha_nvl "I'm just jumping in the shower, yeah?"
        sasha_nvl "Don't suppose you want to come and scrub my back?"
        sasha_nvl "Maybe slide a length into me too?"
    elif texto == 1:
        sasha_nvl "Hang back after band practice tonight, yeah?"
        sasha_nvl "I'm feeling like doing something naughty."
        sasha_nvl "How about fucking me up against Kleio's amp?"
    else:
        sasha_nvl "I feel lonely tonight."
        sasha_nvl "Will you come and sleep in my bed with me?"
        sasha_nvl "You can ask me to do anything as a reward..."
    return

label sasha_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Sasha, you want to hang out with me?"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "We could listen to some music, or jam together?"
        sasha_nvl "Can't spare the time right now."
        sasha_nvl "I have to get to band practice!"
        if persistent.difficulty >= 0:
            if sasha.love <= 50:
                $ sasha.love += 1
        else:
            $ sasha.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Sasha, did you use the last of the milk?"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "Because there's none in the fridge, and nobody went to the store!"
        sasha_nvl "Check the chores list, you lazy bastard!"
        sasha_nvl "It's your turn to get the groceries!"
        if persistent.difficulty >= 0:
            if sasha.love <= 50:
                $ sasha.love += 1
        else:
            $ sasha.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Sasha, I got a rare Metallikea album!"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "It's one of the Japanese imports!"
        sasha_nvl "OMG - you're fucking with me?!?"
        sasha_nvl "Drop everything - we have to listen to it now!"
        if persistent.difficulty >= 0:
            if sasha.love <= 50:
                $ sasha.love += 1
        else:
            $ sasha.love += 1
        $ hero.fun += 0.2
    return

label sasha_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Sasha, what are you wearing right now?"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "I hope it's something black and skimpy!"
        if (sasha.love <= 80 or sasha.sexperience == 0) and not hero.charm >= 30:
            sasha_nvl "Oh get a life, man!"
            sasha_nvl "I'm not a damn sex-object!"
            $ sasha.love -= 1
        elif sasha.sexperience == 0 or (sasha.love <= 100 and not hero.charm >= 50):
            sasha_nvl "Nothing special - just an old band T-shirt."
            sasha_nvl "Oh, and my panties too - because I just got up!"
            $ sasha.love += 1
        else:
            sasha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 100:
                    $ sasha.love += 1
            else:
                $ sasha.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "You want to meet up at the pub, Sasha?"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "I'm really craving some alone time with you, yeah?"
        if (sasha.love <= 80 or sasha.sexperience == 0) and not hero.charm >= 30:
            sasha_nvl "I still have a hangover from last night."
            sasha_nvl "So I'm gonna have to pass."
            $ sasha.love -= 1
        elif sasha.sexperience == 0 or (sasha.love <= 100 and not hero.charm >= 50):
            sasha_nvl "Me too!"
            sasha_nvl "I'll meet you there as soon as I can."
            sasha_nvl "And choose somewhere out of sight - I'm feeling frisky!"
            $ sasha.love += 1
        else:
            sasha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 100:
                    $ sasha.love += 1
            else:
                $ sasha.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't stop thinking about you, Sasha!"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "I want you SO badly all the time!"
        if (sasha.love <= 80 or sasha.sexperience == 0) and not hero.charm >= 30:
            sasha_nvl "Jesus - we already live under the same damn roof!"
            sasha_nvl "You're starting to sound like a psycho stalker!"
            $ sasha.love -= 1
        elif sasha.sexperience == 0 or (sasha.love <= 100 and not hero.charm >= 50):
            sasha_nvl "Same here - I wish we lived alone, just us."
            sasha_nvl "Then we wouldn't have to worry about [bree.name] walking in on us!"
            $ sasha.love += 1
        else:
            sasha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 100:
                    $ sasha.love += 1
            else:
                $ sasha.love += 1
        $ hero.fun += 0.3
    return

label sasha_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I want to play you like you play your guitar, Sasha!"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "I want to pluck you until you play a sweet tune!"
        if sasha.love <= 100 and not hero.charm >= 40:
            sasha_nvl "Nah, I think you're gonna be playing solo!"
            $ sasha.love -= 2
        elif sasha.sexperience < 2 or sasha.love <= 150:
            sasha_nvl "What are you waiting for?"
            sasha_nvl "Come and play with my pussy!"
            $ sasha.love += 2
        else:
            sasha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 150:
                    $ sasha.love += 2
                elif sasha.love <= 175:
                    $ sasha.love += 1
            else:
                $ sasha.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "You're all I can think about, Sasha!"
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "I can't wait to get inside you again!"
        if sasha.love <= 100 and not hero.charm >= 40:
            sasha_nvl "Urgh..."
            sasha_nvl "You're not poet, dude!"
            $ sasha.love -= 2
        elif sasha.sexperience < 2 or sasha.love <= 150:
            sasha_nvl "Make it soon, please!"
            sasha_nvl "I love your having your cock inside of me!"
            $ sasha.love += 2
        else:
            sasha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 150:
                    $ sasha.love += 2
                elif sasha.love <= 175:
                    $ sasha.love += 1
            else:
                $ sasha.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "I love your piercings, Sasha."
        if sasha.activity_name == "sleep" and sasha.love < 70:
            sasha_nvl "Leave me alone, I was asleep..."
            $ sasha.love -= 2
            return
        mchero_nvl "But I love piercing you with my cock even more!"
        if sasha.love <= 100 and not hero.charm >= 40:
            sasha_nvl "Nah...that's the kind of prick I don't want in me!"
            $ sasha.love -= 2
        elif sasha.sexperience < 2 or sasha.love <= 150:
            sasha_nvl "I love your having your cock inside of me!"
            sasha_nvl "Mmm...that's the kind of piercing I like!"
            sasha_nvl "The kind I can't get enough of..."
            $ sasha.love += 2
        else:
            sasha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if sasha.love <= 150:
                    $ sasha.love += 2
                elif sasha.love <= 175:
                    $ sasha.love += 1
            else:
                $ sasha.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
