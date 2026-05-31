label palla_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        palla_nvl "No reason for the message...none at all."
        palla_nvl "Just wondering what you were thinking about right now?"
        palla_nvl "Not that I'm thinking about you, obviously..."
    elif texto == 1:
        palla_nvl "I have to admit you pulled off a pretty good date the other night."
        palla_nvl "I mean, I've had better - of course I have!"
        palla_nvl "But I just thought you deserved to know that..."
    else:
        palla_nvl "Look, I don't often do this - so don't get used to it!"
        palla_nvl "But something I had in the diary's been cancelled."
        palla_nvl "And...well...do you want to meet up and do something with me?"
    return

label palla_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        palla_nvl "I put SO much effort into how I dress, you know?"
        palla_nvl "But all you ever seem to notice is how much skin I'm showing."
        palla_nvl "I wonder why that could be..."
    elif texto == 1:
        palla_nvl "You really should let me give your wardrobe an overhaul."
        palla_nvl "You have so many clothes that just have to go."
        palla_nvl "And you need more stuff that's nice and tight too!"
    else:
        palla_nvl "You doing anything right now?"
        palla_nvl "Because if not, you could come over to my place."
        palla_nvl "And I can put on a private fashion show, just for you..."
    return

label palla_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        palla_nvl "I've got another fashion show in mind for you."
        palla_nvl "Only this time you get to undress the model."
        palla_nvl "Then you can do whatever you want with her..."
    elif texto == 1:
        palla_nvl "It's not fair, all I can think about is your cock!"
        palla_nvl "It fits inside of me so well, so perfectly!"
        palla_nvl "Like Cinderella's damn glass slipper!"
    else:
        palla_nvl "Don't wear pants with button-up flies when I see you next."
        palla_nvl "I want to suck your cock SO badly!"
        palla_nvl "I'll just end up tearing them off to get at it!"
    return

label palla_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Palla, you want to hang out with me?"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        palla_nvl "For your information, I do not hang out!"
        palla_nvl "I socialise in places where it's fashionable to be seen."
        if persistent.difficulty >= 0:
            if palla.love <= 50:
                $ palla.love += 1
        else:
            $ palla.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Palla, you think I should change my look?"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        palla_nvl "I think you need a complete make-over."
        palla_nvl "That and to burn every item of clothing you own right now!"
        if persistent.difficulty >= 0:
            if palla.love <= 50:
                $ palla.love += 1
        else:
            $ palla.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Palla, you want to come check out that new thrift store?"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "Someone told me they have some sweet, old-school metal T-shirts!"
        palla_nvl "Why don't we just do down to the garbage dump and root around in the trash?"
        if persistent.difficulty >= 0:
            if palla.love <= 50:
                $ palla.love += 1
        else:
            $ palla.love += 1
        $ hero.fun += 0.2
    return

label palla_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "What are you wearing right now, Palla?"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "I'm trying my best to imagine it!"
        if (palla.love <= 80 or palla.sexperience == 0) and not hero.charm >= 30:
            palla_nvl "The height of fashion - what else?!?"
            $ palla.love -= 1
        elif palla.sexperience == 0 or (palla.love <= 100 and not hero.charm >= 50):
            palla_nvl "Something stylish and sexy, of course!"
            palla_nvl "And revealing enough to make you sweat!"
            $ palla.love += 1
        else:
            palla_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if palla.love <= 100:
                    $ palla.love += 1
            else:
                $ palla.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "You want to come over and spend some quality time with me, Palla?"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "Some time alone, if you know what I mean?"
        if (palla.love <= 80 or palla.sexperience == 0) and not hero.charm >= 30:
            palla_nvl "I'd rather be seen in last seasons styles!"
            $ palla.love -= 1
        elif palla.sexperience == 0 or (palla.love <= 100 and not hero.charm >= 50):
            palla_nvl "Sounds intriguing!"
            palla_nvl "You'd better make sure it lives up to the hype!"
            $ palla.love += 1
        else:
            palla_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if palla.love <= 100:
                    $ palla.love += 1
            else:
                $ palla.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't stop thinking about you, Palla!"
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "I have to know when I can get my hands on you again!"
        if (palla.love <= 80 or palla.sexperience == 0) and not hero.charm >= 30:
            palla_nvl "Hmm...I think I maybe too exclusive for you!"
            $ palla.love -= 1
        elif palla.sexperience == 0 or (palla.love <= 100 and not hero.charm >= 50):
            palla_nvl "That's to be expected."
            palla_nvl "After all, you're only human!"
            $ palla.love += 1
        else:
            palla_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if palla.love <= 100:
                    $ palla.love += 1
            else:
                $ palla.love += 1
        $ hero.fun += 0.3
    return

label palla_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Palla, you're a fashion guru."
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "So you have to have really hot underwear too, yeah?"
        mchero_nvl "Just thinking about it is making me hard!"
        if palla.love <= 100 and not hero.charm >= 40:
            palla_nvl "I don't dress for your titillation!"
            $ palla.love -= 2
        elif palla.sexperience < 2 or palla.love <= 150:
            palla_nvl "Sure, I have a ton of sexy lingerie."
            palla_nvl "But sometimes the best is none at all..."
            $ palla.love += 2
        else:
            palla_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if palla.love <= 150:
                    $ palla.love += 2
                elif palla.love <= 175:
                    $ palla.love += 1
            else:
                $ palla.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "You always look good, Palla."
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "But you'd look so much better on my cock!"
        if palla.love <= 100 and not hero.charm >= 40:
            palla_nvl "Hmm...I don't think you have anything in my size!"
            $ palla.love -= 2
        elif palla.sexperience < 2 or palla.love <= 150:
            palla_nvl "Mmm...that sounds good!"
            palla_nvl "I'd like to try it on for size!"
            $ palla.love += 2
        else:
            palla_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if palla.love <= 150:
                    $ palla.love += 2
                elif palla.love <= 175:
                    $ palla.love += 1
            else:
                $ palla.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Palla, I should be working right now."
        if palla.activity_name == "sleep" and palla.love < 70:
            palla_nvl "Leave me alone, I was asleep..."
            $ palla.love -= 2
            return
        mchero_nvl "But all I can think about is fucking you!"
        if palla.love <= 100 and not hero.charm >= 40:
            palla_nvl "You're only human."
            palla_nvl "Keep on dreaming!"
            $ palla.love -= 2
        elif palla.sexperience < 2 or palla.love <= 150:
            palla_nvl "Well, you're only human!"
            palla_nvl "And we can see about making your dreams come true soon enough!"
            $ palla.love += 2
        else:
            palla_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if palla.love <= 150:
                    $ palla.love += 2
                elif palla.love <= 175:
                    $ palla.love += 1
            else:
                $ palla.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
