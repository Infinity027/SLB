label shiori_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        shiori_nvl "Sorry to keep messaging you all the time."
        shiori_nvl "But I can't stop thinking about you!"
        shiori_nvl "Are you thinking about me too?"
    elif text_id == 1:
        shiori_nvl "I couldn't keep my mind on work today - not at all!"
        shiori_nvl "Every time you looked at me..."
        shiori_nvl "Oh...it makes me so happy!"
    else:
        shiori_nvl "Thank you SO much for taking me on a date the other night!"
        shiori_nvl "It was wonderful to spend so much time with you."
        shiori_nvl "I hope we can do it again pretty soon?"
    return

label shiori_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        shiori_nvl "I...I just wanted to tell you something."
        shiori_nvl "I have on that outfit you like...the one that's pretty low-cut?"
        shiori_nvl "And...I like to think about you checking me out in it too!"
    elif text_id == 1:
        shiori_nvl "Oh...I can't get a thing done in the office today!"
        shiori_nvl "Every time I see you, I can't think straight!"
        shiori_nvl "You make me feel so bad...because I want you to touch me - down there!"
    else:
        shiori_nvl "You...you really like my breasts - don't you?"
        shiori_nvl "Would you like me to...to touch them for you?"
        shiori_nvl "I can tell you what it feels like, if you'd like?"
    return

label shiori_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        shiori_nvl "Oh dear...I don't think I can keep it in any more!"
        shiori_nvl "I want you so badly, it's making me crazy!"
        shiori_nvl "I need to have your cock in me again!"
    elif text_id == 1:
        shiori_nvl "I'll wear that really tight, short dress again if you like?"
        shiori_nvl "The one that I feel like I'm going to pop out of?"
        shiori_nvl "I like the way you look at me when I wear it..."
        shiori_nvl "It...it makes me wet!"
    else:
        shiori_nvl "I miss you so badly!"
        shiori_nvl "I want to wake up next to you!"
        shiori_nvl "I want to wake up with you in me..."
    return

label shiori_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Shiori, you want to meet up and hang out?"
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "I'd really like to see you!"
        shiori_nvl "Sorry, I can't make it."
        shiori_nvl "Kanta has a temperature - I'm worried he's sick!"
        if persistent.difficulty >= 0:
            if shiori.love <= 50:
                $ shiori.love += 1
        else:
            $ shiori.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Shiori, I just got off work."
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "Fancy grabbing a drink?"
        shiori_nvl "Not tonight, sorry."
        shiori_nvl "I have to work my second job."
        if persistent.difficulty >= 0:
            if shiori.love <= 50:
                $ shiori.love += 1
        else:
            $ shiori.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Shiori, you want to come over and watch some anime?"
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        shiori_nvl "I don't like children's cartoons!"
        shiori_nvl "But Kanta might like it?"
        if persistent.difficulty >= 0:
            if shiori.love <= 50:
                $ shiori.love += 1
        else:
            $ shiori.love += 1
        $ hero.fun += 0.2
    return

label shiori_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I want to know what you're wearing, Shiori."
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "Tell me so that I can get a good mental image?"
        if (shiori.love <= 80 or shiori.sexperience == 0) and not hero.charm >= 30:
            shiori_nvl "That sounds creepy - I won't do it!"
            $ shiori.love -= 1
        elif shiori.sexperience == 0 or (shiori.love <= 100 and not hero.charm >= 50):
            shiori_nvl "Okay...if that's what you want?"
            shiori_nvl "I only have on my nightie right now..."
            shiori_nvl "And...well...it's pretty short - you can even see my butt!"
            $ shiori.love += 1
        else:
            shiori_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 100:
                    $ shiori.love += 1
            else:
                $ shiori.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I miss you, Shiori - real bad!"
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "All I can think about is holding you!"
        mchero_nvl "Holding you and what comes next..."
        if (shiori.love <= 80 or shiori.sexperience == 0) and not hero.charm >= 30:
            shiori_nvl "Oh dear...I don't have time for this!"
            shiori_nvl "I have so much work to do!"
            $ shiori.love -= 1
        elif shiori.sexperience == 0 or (shiori.love <= 100 and not hero.charm >= 50):
            shiori_nvl "Oh dear...me too!"
            shiori_nvl "I can imagine being wrapped in your big, strong arms!"
            shiori_nvl "And...and other things too!"
            $ shiori.love += 1
        else:
            shiori_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 100:
                    $ shiori.love += 1
            else:
                $ shiori.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I have to see you soon, Shiori!"
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "Can you come over here so we can be together?"
        if (shiori.love <= 80 or shiori.sexperience == 0) and not hero.charm >= 30:
            shiori_nvl "Oh...that's SO selfish of you!"
            shiori_nvl "You know I can't shirk my responsibilities!"
            $ shiori.love -= 1
        elif shiori.sexperience == 0 or (shiori.love <= 100 and not hero.charm >= 50):
            shiori_nvl "Oh...just thinking about you makes me feel...all funny!"
            shiori_nvl "I'll be there just as soon as I can!"
            $ shiori.love += 1
        else:
            shiori_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 100:
                    $ shiori.love += 1
            else:
                $ shiori.love += 1
        $ hero.fun += 0.3
    return

label shiori_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I'm sitting here thinking about you, Shiori."
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "I'm thinking how much I want my cock inside of you!"
        if shiori.love <= 100 and not hero.charm >= 40:
            shiori_nvl "Is that all I am to you?!?"
            shiori_nvl "I thought you loved me?"
            $ shiori.love -= 2
        elif shiori.sexperience < 2 or shiori.love <= 150:
            shiori_nvl "Oh...oh my..."
            shiori_nvl "That would feel so good!"
            shiori_nvl "I can almost feel you in me too!"
            $ shiori.love += 2
        else:
            shiori_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 150:
                    $ shiori.love += 2
                elif shiori.love <= 175:
                    $ shiori.love += 1
            else:
                $ shiori.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I wish you could go topless all the time, Shiori."
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "Your breasts just make me so horny!"
        if shiori.love <= 100 and not hero.charm >= 40:
            shiori_nvl "Don't say that!"
            shiori_nvl "People already stare at my chest!"
            $ shiori.love -= 2
        elif shiori.sexperience < 2 or shiori.love <= 150:
            shiori_nvl "They do?!?"
            shiori_nvl "Oh, I wish I could do that for you!"
            shiori_nvl "I'd have them out all the time!"
            $ shiori.love += 2
        else:
            shiori_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 150:
                    $ shiori.love += 2
                elif shiori.love <= 175:
                    $ shiori.love += 1
            else:
                $ shiori.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "It's pretty hot that you strip on the side, Shiori."
        if shiori.activity_name == "sleep" and shiori.love < 70:
            shiori_nvl "Leave me alone, I was asleep..."
            $ shiori.love -= 2
            return
        mchero_nvl "You want to come dance on my pole a while?"
        if shiori.love <= 100 and not hero.charm >= 40:
            shiori_nvl "You know I don't like to talk about that!"
            shiori_nvl "I'm so ashamed of dancing for money!"
            $ shiori.love -= 2
        elif shiori.sexperience < 2 or shiori.love <= 150:
            shiori_nvl "Oh yes...yes I do!"
            shiori_nvl "So long as you mean your cock, right?"
            $ shiori.love += 2
        else:
            shiori_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if shiori.love <= 150:
                    $ shiori.love += 2
                elif shiori.love <= 175:
                    $ shiori.love += 1
            else:
                $ shiori.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
