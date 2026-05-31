label emma_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        emma_nvl "It's weird, but you remember how you saw me in a dream?"
        emma_nvl "Well, I was having a really vivid one last night."
        emma_nvl "And you were in it - so now I'm dreaming about you too!"
    elif texto == 1:
        emma_nvl "I was just thinking about you."
        emma_nvl "Well...I tend to do that a lot these days!"
        emma_nvl "Do you find that you think of me like that too?"
    else:
        emma_nvl "I can't wait to go on another date with you!"
        emma_nvl "I had so much fun on the last one."
        emma_nvl "I wonder what we'll get up to on the next one?"
    return

label emma_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        emma_nvl "I feel like I'm going crazy here on my own!"
        emma_nvl "I have to see you again soon - really soon!"
        emma_nvl "I want you that bad!"
    elif texto == 1:
        emma_nvl "I have on that outfit you like right now."
        emma_nvl "You know the one - it makes you get all excited!"
        emma_nvl "Just wanted to let you know!"
    else:
        emma_nvl "Hey, I'm not doing anything right now."
        emma_nvl "You want to hang out with me?"
        emma_nvl "I'm sure we can think of something to do together..."
    return

label emma_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        emma_nvl "I've been thinking about you all the time."
        emma_nvl "Even dreaming about what we did together!"
        emma_nvl "Dreaming about having you inside me!"
    elif texto == 1:
        emma_nvl "You seem to like it when I dress sexy, right?"
        emma_nvl "Because I just wanted to be sure."
        emma_nvl "I like the idea of you wanting me."
        emma_nvl "It makes me go wet down there..."
    else:
        emma_nvl "Your cock looks so good when I see it!"
        emma_nvl "All I can think about is putting it in my mouth!"
        emma_nvl "Will you let me do that - please?!?"
    return

label emma_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Emma, what are you doing right now?"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        emma_nvl "Not much...just chilling."
        mchero_nvl "Me too...me too."
        mchero_nvl "Just wanted to know how you were."
        if persistent.difficulty >= 0:
            if emma.love <= 50:
                $ emma.love += 1
        else:
            $ emma.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Emma, how about we meet up and hang out together?"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "If you're not doing anything, yeah?"
        emma_nvl "I can't right now, sorry."
        emma_nvl "I'm not doing anything, but I am doing stuff!"
        if persistent.difficulty >= 0:
            if emma.love <= 50:
                $ emma.love += 1
        else:
            $ emma.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Emma, I had a really weird dream last night!"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        emma_nvl "Oh yeah?"
        emma_nvl "Was I in it this time?"
        mchero_nvl "Yeah, and you were chasing me, waving a huge banana the whole time!"
        if persistent.difficulty >= 0:
            if emma.love <= 50:
                $ emma.love += 1
        else:
            $ emma.love += 1
        $ hero.fun += 0.2
    return

label emma_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Emma, what are you wearing right now?"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "Tell me in painful, exquisite detail!"
        if (emma.love <= 80 or emma.sexperience == 0) and not hero.charm >= 30:
            emma_nvl "No way!"
            emma_nvl "Stop asking me stuff like this - it's embarrassing!"
            $ emma.love -= 1
        elif emma.sexperience == 0 or (emma.love <= 100 and not hero.charm >= 50):
            emma_nvl "Oh you!"
            emma_nvl "I have on a short skirt and a little top!"
            emma_nvl "Is that enough for you?"
            $ emma.love += 1
        else:
            emma_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if emma.love <= 100:
                    $ emma.love += 1
            else:
                $ emma.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I can't stop thinking about you, Emma."
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "Ever since I saw you in my dream - you're all I want!"
        mchero_nvl "You make me crazy!"
        if (emma.love <= 80 or emma.sexperience == 0) and not hero.charm >= 30:
            emma_nvl "I can't take you being this intense!"
            emma_nvl "Don't turn a dream into nightmare!"
            $ emma.love -= 1
        elif emma.sexperience == 0 or (emma.love <= 100 and not hero.charm >= 50):
            emma_nvl "Me too, me too!"
            emma_nvl "I want to be with you right now!"
            $ emma.love += 1
        else:
            emma_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if emma.love <= 100:
                    $ emma.love += 1
            else:
                $ emma.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I need to see you, Emma!"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "When can we meet up so I can get my hands on you?!?"
        if (emma.love <= 80 or emma.sexperience == 0) and not hero.charm >= 30:
            emma_nvl "I don't know when I'll be free next."
            emma_nvl "Until then, don't call me - I'll call you."
            $ emma.love -= 1
        elif emma.sexperience == 0 or (emma.love <= 100 and not hero.charm >= 50):
            emma_nvl "Settle down!"
            emma_nvl "You'll get your hands on me soon enough!"
            $ emma.love += 1
        else:
            emma_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if emma.love <= 100:
                    $ emma.love += 1
            else:
                $ emma.love += 1
        $ hero.fun += 0.3
    return

label emma_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I keep thinking about the last time we fucked, Emma."
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "And it's making me want to do it again - right now!"
        if emma.love <= 100 and not hero.charm >= 40:
            emma_nvl "Is that all you ever think about?!?"
            $ emma.love -= 2
        elif emma.sexperience < 2 or emma.love <= 150:
            emma_nvl "Behave yourself, you beast!"
            emma_nvl "We'll do it again soon enough!"
            $ emma.love += 2
        else:
            emma_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if emma.love <= 150:
                    $ emma.love += 2
                elif emma.love <= 175:
                    $ emma.love += 1
            else:
                $ emma.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "What kind of panties are you wearing today, Emma?"
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "Describe them to me, yeah?"
        if emma.love <= 100 and not hero.charm >= 40:
            emma_nvl "Oh, grow up!"
            emma_nvl "And stop harassing me!"
            $ emma.love -= 2
        elif emma.sexperience < 2 or emma.love <= 150:
            emma_nvl "Oh, nothing special..."
            emma_nvl "Just those little tiny ones, you know?"
            emma_nvl "The ones that you can see my pussy through!"
            $ emma.love += 2
        else:
            emma_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if emma.love <= 150:
                    $ emma.love += 2
                elif emma.love <= 175:
                    $ emma.love += 1
            else:
                $ emma.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You've got such great lips, Emma."
        if emma.activity_name == "sleep" and emma.love < 70:
            emma_nvl "Leave me alone, I was asleep..."
            $ emma.love -= 2
            return
        mchero_nvl "But I think they'd look even better wrapped around my cock!"
        if emma.love <= 100 and not hero.charm >= 40:
            emma_nvl "Hey - what are you trying to say?"
            emma_nvl "Do you think I talk too much?!?"
            $ emma.love -= 2
        elif emma.sexperience < 2 or emma.love <= 150:
            emma_nvl "Oh, you dirty boy!"
            emma_nvl "I kind of like the thought of that too..."
            $ emma.love += 2
        else:
            emma_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if emma.love <= 150:
                    $ emma.love += 2
                elif emma.love <= 175:
                    $ emma.love += 1
            else:
                $ emma.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
