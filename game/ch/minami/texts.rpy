label minami_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        minami_nvl "I had a great time with you the other night, big bro."
        minami_nvl "Where did you learn to be so much fun?"
        minami_nvl "And when are we going to do it again?"
    elif texto == 1:
        minami_nvl "I think about you all the time, big bro."
        minami_nvl "It's like you're always on my mind!"
        minami_nvl "I hope you're thinking of me too..."
    else:
        minami_nvl "Hey, big bro, I just got done studying."
        minami_nvl "You want to come hang out in my room?"
        minami_nvl "Or we could meet up somewhere else, if you like?"
    return

label minami_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        minami_nvl "Just getting in the shower, big bro - so don't go flushing the toilet!"
        minami_nvl "I don't want to get frozen while I'm lathering myself up."
        minami_nvl "Just think of how hard that would make my nipples!"
    elif texto == 1:
        minami_nvl "I have a skirt I need to show you when you get home, big bro."
        minami_nvl "I think it might be too short for me to wear outside of the house!"
        minami_nvl "So you're gonna have to watch me bending over in it, okay?"
    else:
        minami_nvl "You should SO get into cosplay with me, big bro."
        minami_nvl "We could go to conventions together, have matching outfits."
        minami_nvl "And I think you'd look pretty hot in lycra too..."
    return

label minami_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        minami_nvl "Hey, big bro, guess what?"
        minami_nvl "I've got my Lunar Mariner costume on - the one with the short skirt!"
        minami_nvl "But I forgot to put on my panties!"
        minami_nvl "Wanna come fuck me in it?"
    elif texto == 1:
        minami_nvl "Ah...I should SO be studying right now, big bro."
        minami_nvl "But I can't concentrate on my books."
        minami_nvl "All I can think about is how good your cock feels inside of me!"
    else:
        minami_nvl "Hey, big bro, the sun's out and there's nobody else home."
        minami_nvl "I'm gonna jump in the pool and swim naked!"
        minami_nvl "You want to come join me?"
        minami_nvl "Then maybe cum in me?"
    return

label minami_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Minami, what are you doing right now?"
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "Want to watch some anime with me?"
        minami_nvl "I want to, big bro, but I can't."
        minami_nvl "I have SO much studying to do!"
        if persistent.difficulty >= 0:
            if minami.love <= 50:
                $ minami.love += 1
        else:
            $ minami.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Minami, you remember all my old action figures, right?"
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "What did mom do with them when I moved out?"
        minami_nvl "Oh, I meant to tell you, big bro."
        minami_nvl "She threw them out in the trash!"
        mchero_nvl "OMG!"
        if persistent.difficulty >= 0:
            if minami.love <= 50:
                $ minami.love += 1
        else:
            $ minami.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Minami, could you pick me something up from the store?"
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "I'd go myself, but I'm kind of in the middle of something!"
        minami_nvl "No way, big bro!"
        minami_nvl "I'm not your servant!"
        if persistent.difficulty >= 0:
            if minami.love <= 50:
                $ minami.love += 1
        else:
            $ minami.love += 1
        $ hero.fun += 0.2
    return

label minami_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "What are you wearing right now, Minami?"
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "It's the sailor suit isn't it?"
        mchero_nvl "Please tell me it is - the one with the short skirt!"
        if (minami.love <= 80 or minami.sexperience == 0) and not hero.charm >= 30:
            minami_nvl "Eww...gross!"
            minami_nvl "I don't just dress up for your benefit, you pervert!"
            $ minami.love -= 1
        elif minami.sexperience == 0 or (minami.love <= 100 and not hero.charm >= 50):
            minami_nvl "He he he...it might be, big bro!"
            minami_nvl "And if you're lucky, I might still have it on when you get home..."
            $ minami.love += 1
        else:
            minami_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if minami.love <= 100:
                    $ minami.love += 1
            else:
                $ minami.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I was watching some anime, Minami."
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "And you could SO be the star of the show."
        mchero_nvl "You're way cuter than she is!"
        if (minami.love <= 80 or minami.sexperience == 0) and not hero.charm >= 30:
            minami_nvl "Hey!"
            minami_nvl "You're only saying that because you want to be able to turn me off when you're done with me!"
            $ minami.love -= 1
        elif minami.sexperience == 0 or (minami.love <= 100 and not hero.charm >= 50):
            minami_nvl "I'm better than an anime girl, big bro!"
            minami_nvl "You can cuddle me for real..."
            $ minami.love += 1
        else:
            minami_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if minami.love <= 100:
                    $ minami.love += 1
            else:
                $ minami.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "Meet me at the pub, Minami."
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "I want to spend some time getting intimate with you in the snug!"
        if (minami.love <= 80 or minami.sexperience == 0) and not hero.charm >= 30:
            minami_nvl "Urgh...not that dump!"
            minami_nvl "They always ask me for ID!"
            $ minami.love -= 1
        elif minami.sexperience == 0 or (minami.love <= 100 and not hero.charm >= 50):
            minami_nvl "Okay, big bro - so long as you buy me a drink!"
            $ minami.love += 1
        else:
            minami_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if minami.love <= 100:
                    $ minami.love += 1
            else:
                $ minami.love += 1
        $ hero.fun += 0.3
    return

label minami_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Minami, I can't keep you out of my head!"
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "My cock is so hard for you in those short skirts you wear!"
        if minami.love <= 100 and not hero.charm >= 40:
            minami_nvl "Hey - I don't dress for your perverted pleasure!"
            $ minami.love -= 2
        elif minami.sexperience < 2 or minami.love <= 150:
            minami_nvl "Oh, I like to hear you're hard for me, big bro!"
            minami_nvl "You lift up my skirt with your cock."
            minami_nvl "And I'll pull down my panties for you!"
            $ minami.love += 2
        else:
            minami_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if minami.love <= 150:
                    $ minami.love += 2
                elif minami.love <= 175:
                    $ minami.love += 1
            else:
                $ minami.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Your tits are perfect, Minami."
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "I just want to suck on your nipples all day!"
        if minami.love <= 100 and not hero.charm >= 40:
            minami_nvl "No way, big bro - you'll make them sore!"
            $ minami.love -= 2
        elif minami.sexperience < 2 or minami.love <= 150:
            minami_nvl "Big bro!"
            minami_nvl "You're making them go all hard!"
            minami_nvl "Now you HAVE to suck them for me!"
            $ minami.love += 2
        else:
            minami_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if minami.love <= 150:
                    $ minami.love += 2
                elif minami.love <= 175:
                    $ minami.love += 1
            else:
                $ minami.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Wait until [bree.name] and Sasha are asleep tonight, then sneak into my room."
        if minami.activity_name == "sleep" and minami.love < 70:
            minami_nvl "Leave me alone, I was asleep..."
            $ minami.love -= 2
            return
        mchero_nvl "I want to fuck you until we pass out, then do it again in the morning!"
        if minami.love <= 100 and not hero.charm >= 40:
            minami_nvl "No way - not tonight!"
            minami_nvl "I have to study, and it's going to be an all-nighter!"
            $ minami.love -= 2
        elif minami.sexperience < 2 or minami.love <= 150:
            minami_nvl "Okay, big bro, I can't wait!"
            minami_nvl "I can feel myself getting wet just thinking about it!"
            $ minami.love += 2
        else:
            minami_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if minami.love <= 150:
                    $ minami.love += 2
                elif minami.love <= 175:
                    $ minami.love += 1
            else:
                $ minami.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
