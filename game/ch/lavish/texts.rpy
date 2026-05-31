label lavish_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lavish_nvl "I get off work in a little while."
        lavish_nvl "And I could do with a chance to unwind."
        lavish_nvl "You want to meet me for a coffee, or maybe something stronger?"
    elif texto == 1:
        lavish_nvl "I have to admit, I had a great time on our last date."
        lavish_nvl "You really put some thought into it, which is sweet."
        lavish_nvl "I'm so looking forward to seeing what you pull off next!"
    else:
        lavish_nvl "Hey, no real reason for messaging - I was just thinking about you."
        lavish_nvl "In fact, I've been thinking about you a lot recently."
        lavish_nvl "And I kind of hope you're thinking of me too..."
    return

label lavish_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lavish_nvl "I...I don't know what's wrong with me today."
        lavish_nvl "I just can't concentrate on my work!"
        lavish_nvl "All I can think of is the last time we made love..."
    elif texto == 1:
        lavish_nvl "Remember, I might be wearing something smart and sensible."
        lavish_nvl "But I always have something on underneath that's slinky and sexy!"
        lavish_nvl "Something that I'm wearing just for you!"
    else:
        lavish_nvl "Ah...work really took it out of me today!"
        lavish_nvl "You mind if I come over to your place to unwind tonight?"
        lavish_nvl "Maybe you could even give me a massage, or something like that?"
    return

label lavish_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lavish_nvl "Oh...I can't keep my mind on my work!"
        lavish_nvl "I keep thinking about you all the time!"
        lavish_nvl "Well...you and what I want you to do to me..."
    elif texto == 1:
        lavish_nvl "I put on some really nice lingerie today, just for you!"
        lavish_nvl "I really want to show it off, but I can't in the office!"
        lavish_nvl "Maybe we could meet up in the stationary cupboard?"
        lavish_nvl "Then you could show me how much you like it..."
    else:
        lavish_nvl "Can I come over and use your pool?"
        lavish_nvl "But...the thing is...I need to know your housemates aren't in."
        lavish_nvl "Because...well...I want to swim naked for you!"
    return

label lavish_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Lavish, are you free to meet up?"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        lavish_nvl "Sorry, I can't make it."
        lavish_nvl "I'm working late in the office tonight!"
        if persistent.difficulty >= 0:
            if lavish.love <= 50:
                $ lavish.love += 1
        else:
            $ lavish.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Lavish, you work too hard!"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "Let me take you out for a drink and a chance to relax, huh?"
        lavish_nvl "That sounds really nice."
        lavish_nvl "Just let me finish off one last piece of work first..."
        if persistent.difficulty >= 0:
            if lavish.love <= 50:
                $ lavish.love += 1
        else:
            $ lavish.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Lavish, how are you doing?"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        lavish_nvl "I'm feeling pretty worn out."
        lavish_nvl "I actually fell asleep at my desk today!"
        lavish_nvl "Can you believe that?"
        if persistent.difficulty >= 0:
            if lavish.love <= 50:
                $ lavish.love += 1
        else:
            $ lavish.love += 1
        $ hero.fun += 0.2
    return

label lavish_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Lavish, I can't stop thinking about you!"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "Tell me what you're wearing right now?"
        if (lavish.love <= 80 or lavish.sexperience == 0) and not hero.charm >= 30:
            lavish_nvl "I don't have time for this!"
            lavish_nvl "I'm trying to work!"
            $ lavish.love -= 1
        elif lavish.sexperience == 0 or (lavish.love <= 100 and not hero.charm >= 50):
            lavish_nvl "Okay...but I have to make it quick!"
            lavish_nvl "I'm in one of my smartest work outfits."
            lavish_nvl "But I have REALLY naughty underwear on!"
            $ lavish.love += 1
        else:
            lavish_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 100:
                    $ lavish.love += 1
            else:
                $ lavish.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "You want to meet up, Lavish?"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "I've got some spare time on my hands."
        mchero_nvl "And I'd really like my hands to spend it on you!"
        if (lavish.love <= 80 or lavish.sexperience == 0) and not hero.charm >= 30:
            lavish_nvl "I'm busy - so you'll have to handle yourself!"
            $ lavish.love -= 1
        elif lavish.sexperience == 0 or (lavish.love <= 100 and not hero.charm >= 50):
            lavish_nvl "That sounds really nice!"
            lavish_nvl "I'll be there as soon as I can!"
            $ lavish.love += 1
        else:
            lavish_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 100:
                    $ lavish.love += 1
            else:
                $ lavish.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "It's so hard to keep my mind on my work, Lavish."
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "Every time you walk by, I can't keep my mind on anything else!"
        if (lavish.love <= 80 or lavish.sexperience == 0) and not hero.charm >= 30:
            lavish_nvl "That's SO unprofessional of you!"
            lavish_nvl "Maybe one of us should think about working somewhere else?"
            $ lavish.love -= 1
        elif lavish.sexperience == 0 or (lavish.love <= 100 and not hero.charm >= 50):
            lavish_nvl "Just do your best to pretend you're working, okay?"
            lavish_nvl "That's what I do when I'm thinking about you..."
            $ lavish.love += 1
        else:
            lavish_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 100:
                    $ lavish.love += 1
            else:
                $ lavish.love += 1
        $ hero.fun += 0.3
    return

label lavish_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Lavish, what are you wearing at the office today?"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "I bet you have some sexy underwear on, right?"
        mchero_nvl "Just thinking about it makes me hard!"
        if lavish.love <= 100 and not hero.charm >= 40:
            lavish_nvl "Will you stop it?!?"
            lavish_nvl "I can't work like this!"
            $ lavish.love -= 2
        elif lavish.sexperience < 2 or lavish.love <= 150:
            lavish_nvl "I look pretty professional, sure."
            lavish_nvl "But it's stockings and suspenders underneath!"
            lavish_nvl "All the better to get your cock standing to attention!"
            $ lavish.love += 2
        else:
            lavish_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 150:
                    $ lavish.love += 2
                elif lavish.love <= 175:
                    $ lavish.love += 1
            else:
                $ lavish.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I was just remembering the last time you sucked my cock."
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "Your lips look so beautiful wrapped around it!"
        if lavish.love <= 100 and not hero.charm >= 40:
            lavish_nvl "Is that all you want me to do with my mouth?"
            lavish_nvl "I can speak, you know?!?"
            $ lavish.love -= 2
        elif lavish.sexperience < 2 or lavish.love <= 150:
            lavish_nvl "I try to do a job, whatever the task."
            lavish_nvl "Especially when it comes to giving you oral!"
            $ lavish.love += 2
        else:
            lavish_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 150:
                    $ lavish.love += 2
                elif lavish.love <= 175:
                    $ lavish.love += 1
            else:
                $ lavish.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Lavish, stroke your pussy for me, yeah?"
        if lavish.activity_name == "sleep" and lavish.love < 70:
            lavish_nvl "Leave me alone, I was asleep..."
            $ lavish.love -= 2
            return
        mchero_nvl "I want you to tell me how it feels!"
        if lavish.love <= 100 and not hero.charm >= 40:
            lavish_nvl "You have to be kidding!"
            lavish_nvl "I'm not playing with myself for your amusement!"
            $ lavish.love -= 2
        elif lavish.sexperience < 2 or lavish.love <= 150:
            lavish_nvl "It's warm and soft..."
            lavish_nvl "It feels good!"
            lavish_nvl "Oh...it's getting wet too!"
            $ lavish.love += 2
        else:
            lavish_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lavish.love <= 150:
                    $ lavish.love += 2
                elif lavish.love <= 175:
                    $ lavish.love += 1
            else:
                $ lavish.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
