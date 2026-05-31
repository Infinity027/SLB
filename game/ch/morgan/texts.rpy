label morgan_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        morgan_nvl "What are you doing right now, huh?"
        morgan_nvl "I got off from work a little early."
        morgan_nvl "So I thought that maybe we could meet up?"
    elif texto == 1 and morgan.flags.last_date_day:
        morgan_nvl "I had a great time on our date the other night."
        morgan_nvl "We HAVE to so that again, and soon!"
        morgan_nvl "I don't know how we're going to top it!"
    else:
        morgan_nvl "I think about you all the time now we've met up again."
        morgan_nvl "Even more than I used to when we were apart for so long!"
        morgan_nvl "I was wondering...do you think about me too?"
    return

label morgan_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        morgan_nvl "What to wear, what to wear?"
        morgan_nvl "How about as little as possible?"
        morgan_nvl "You like the sound of that?"
    elif texto == 1:
        morgan_nvl "Hey, can I come over to your place?"
        morgan_nvl "No particular reason...none at all..."
        morgan_nvl "Just thought you might like to do something fun - like me!"
    else:
        morgan_nvl "You're always on my mind!"
        morgan_nvl "If I were a guy, I'd say I was thinking with my dick..."
        morgan_nvl "Fuck - you make me think with my pussy!"
    return

label morgan_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        morgan_nvl "Urgh...I just got off of work and I'm all sweaty!"
        morgan_nvl "That costume they make me wear - it's SO tight!"
        morgan_nvl "Can I come over to your place and grab a quick shower?"
        morgan_nvl "If you say yes, you can grab me while I'm in there too..."
    elif texto == 1:
        morgan_nvl "Oh...you fucked me so hard last time we did it."
        morgan_nvl "And I liked it SO much!"
        morgan_nvl "I swear it feels like you're still inside of me!"
    else:
        morgan_nvl "Sure, I like to dress sexy, wear something you'll like."
        morgan_nvl "But I kind of wonder what's the point in bothering?"
        morgan_nvl "All I want you to do is tear if off of me!"
    return

label morgan_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Morgan, you up to anything right now?"
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "I'm not doing anything myself - wanna hang out?"
        morgan_nvl "Sounds good to me!"
        morgan_nvl "I'll call you back when I can get over, okay?"
        if persistent.difficulty >= 0:
            if morgan.love <= 50:
                $ morgan.love += 1
        else:
            $ morgan.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Morgan, I was just thinking about when we were kids."
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "You ever think about those times?"
        morgan_nvl "No, not really."
        morgan_nvl "I mostly try to forget them."
        if persistent.difficulty >= 0:
            if morgan.love <= 50:
                $ morgan.love += 1
        else:
            $ morgan.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Morgan, what colour is your hair?"
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "You know, naturally?"
        mchero_nvl "I totally forgot!"
        morgan_nvl "Then I'm not telling you!"
        morgan_nvl "See if you can guess..."
        if persistent.difficulty >= 0:
            if morgan.love <= 50:
                $ morgan.love += 1
        else:
            $ morgan.love += 1
        $ hero.fun += 0.2
    return

label morgan_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Morgan, what are you wearing right now?"
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "I bet it's something you look hot in!"
        if (morgan.love <= 80 or morgan.sexperience == 0) and not hero.charm >= 30:
            morgan_nvl "I'm not here for your amusement!"
            morgan_nvl "So piss off!"
            $ morgan.love -= 1
        elif morgan.sexperience == 0 or (morgan.love <= 100 and not hero.charm >= 50):
            morgan_nvl "You can't see me, can you?"
            morgan_nvl "So maybe I'm not wearing anything at all..."
            $ morgan.love += 1
        else:
            morgan_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 100:
                    $ morgan.love += 1
            else:
                $ morgan.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "Hey, Morgan, I'm dying to see you!"
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "Can you sneak out and meet me?"
        if (morgan.love <= 80 or morgan.sexperience == 0) and not hero.charm >= 30:
            morgan_nvl "Stop bugging me!"
            morgan_nvl "I'm too busy for that."
            $ morgan.love -= 1
        elif morgan.sexperience == 0 or (morgan.love <= 100 and not hero.charm >= 50):
            morgan_nvl "That sounds like fun!"
            morgan_nvl "I'll text you as soon as I can, okay?"
            $ morgan.love += 1
        else:
            morgan_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 100:
                    $ morgan.love += 1
            else:
                $ morgan.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't believe you were out of my life for so long, Morgan."
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "Because right now, being with you is all I can think about!"
        if (morgan.love <= 80 or morgan.sexperience == 0) and not hero.charm >= 30:
            morgan_nvl "Maybe you should have kept that to yourself?"
            morgan_nvl "It makes you sound pretty needy and pathetic!"
            $ morgan.love -= 1
        elif morgan.sexperience == 0 or (morgan.love <= 100 and not hero.charm >= 50):
            morgan_nvl "Me too!"
            morgan_nvl "I get all worked up just thinking about you!"
            $ morgan.love += 1
        else:
            morgan_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 100:
                    $ morgan.love += 1
            else:
                $ morgan.love += 1
        $ hero.fun += 0.3
    return

label morgan_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I've got a crazy hard-on from thinking about you, Morgan!"
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "You want to come over and ride it?"
        if morgan.love <= 100 and not hero.charm >= 40:
            morgan_nvl "Nah, you can handle it on your own!"
            $ morgan.love -= 2
        elif morgan.sexperience < 2 or morgan.love <= 150:
            morgan_nvl "Aw, did I do that to you?"
            morgan_nvl "The least I could do is let you stick it in me!"
            $ morgan.love += 2
        else:
            morgan_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 150:
                    $ morgan.love += 2
                elif morgan.love <= 175:
                    $ morgan.love += 1
            else:
                $ morgan.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I wish I had my hands on your body right now, Morgan."
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "I can almost feel your breasts in the palms of my hands!"
        mchero_nvl "Imagine your nipples getting hard as I squeeze them..."
        if morgan.love <= 100 and not hero.charm >= 40:
            morgan_nvl "Stop that - you're making me uncomfortable!"
            $ morgan.love -= 2
        elif morgan.sexperience < 2 or morgan.love <= 150:
            morgan_nvl "Stop it!"
            morgan_nvl "You're turning me on!"
            morgan_nvl "My pussy's getting wet!"
            $ morgan.love += 2
        else:
            morgan_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 150:
                    $ morgan.love += 2
                elif morgan.love <= 175:
                    $ morgan.love += 1
            else:
                $ morgan.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You looked so hot in what you were wearing the other day, Morgan."
        if morgan.activity_name == "sleep" and morgan.love < 70:
            morgan_nvl "Leave me alone, I was asleep..."
            $ morgan.love -= 2
            return
        mchero_nvl "I hope you wear it again soon - it drives me crazy seeing you in it!"
        if morgan.love <= 100 and not hero.charm >= 40:
            morgan_nvl "I don't like it when you do this."
            morgan_nvl "You're putting me under too much pressure!"
            $ morgan.love -= 2
        elif morgan.sexperience < 2 or morgan.love <= 150:
            morgan_nvl "Maybe you will, maybe you won't!"
            morgan_nvl "Maybe next time you see me I won't be wearing anything at all..."
            $ morgan.love += 2
        else:
            morgan_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if morgan.love <= 150:
                    $ morgan.love += 2
                elif morgan.love <= 175:
                    $ morgan.love += 1
            else:
                $ morgan.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
