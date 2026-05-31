label audrey_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ texto = randint(0, 2)
    if texto == 0:
        audrey_nvl "You want to come grab a coffee with me?"
        audrey_nvl "I'm dying of boredom at work right now!"
        audrey_nvl "Don't leave me here to die a slow death!"
    elif texto == 1:
        audrey_nvl "You're thinking about me right now, yeah?"
        audrey_nvl "I just need to know that you are, okay?"
        audrey_nvl "Not because I'm thinking of you or anything..."
    else:
        audrey_nvl "You know what, that last date was pretty okay!"
        audrey_nvl "I mean, it wasn't the most amazing time I've ever had..."
        audrey_nvl "But I'd be up for doing it again, if you are?"
    return

label audrey_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ texto = randint(0, 2)
    if texto == 0 and Person.is_not_hidden("shiori") and Person.is_not_hidden("lavish"):
        audrey_nvl "Did I see you flirting with Lavish and Shiori today?"
        audrey_nvl "I'd better not have, or else they're in deep shit!"
        audrey_nvl "You're mine and those two bitches can back off!"
    elif texto == 1:
        audrey_nvl "Did you wear that shirt just to fuck with me?!?"
        audrey_nvl "Because if you did, that's not fucking fair!"
        audrey_nvl "You look SO good in it!"
    else:
        audrey_nvl "You'd better pay me some attention soon!"
        audrey_nvl "If you don't, then I'll cause a scene in the middle of the office!"
        audrey_nvl "You're making me so desperate - you don't know what I'm capable of..."
    return

label audrey_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ texto = randint(0, 2)
    if texto == 0:
        audrey_nvl "Work sucks...it's like the worst thing ever!"
        audrey_nvl "Want to do something that doesn't suck?"
        audrey_nvl "Well, it does - but it involves me sucking your cock!"
    elif texto == 1:
        audrey_nvl "I wish I could walk into the office naked some days."
        audrey_nvl "That and have you spank me while everyone watched!"
        audrey_nvl "Oh fuck...I've made myself want it now!"
        audrey_nvl "Seriously, where's your cock when I need it?!?"
    else:
        audrey_nvl "I'm going to be wearing something tight and short next time you see me."
        audrey_nvl "Something that I know is going to make you hard as a rock and want me."
        audrey_nvl "Your job is to pounce on me the moment you get the chance."
        audrey_nvl "Think you can handle that?"
    return

label audrey_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Audrey, you want to grab some lunch?"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "I could really go for a sandwich right now!"
        audrey_nvl "Yeah, I think I'll pass."
        audrey_nvl "I've seen you eat a sandwich, and the thought of it ruins my appetite!"
        if persistent.difficulty >= 0:
            if audrey.love <= 50:
                $ audrey.love += 1
        else:
            $ audrey.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Audrey, I didn't see you at work today."
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "Are you sick?"
        audrey_nvl "Yeah - sick of work!"
        if persistent.difficulty >= 0:
            if audrey.love <= 50:
                $ audrey.love += 1
        else:
            $ audrey.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Audrey, I just heard a great joke!"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        audrey_nvl "Me too..."
        audrey_nvl "In fact I'm listening to it right now!"
        if persistent.difficulty >= 0:
            if audrey.love <= 50:
                $ audrey.love += 1
        else:
            $ audrey.love += 1
        $ hero.fun += 0.2
    return

label audrey_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I couldn't concentrate at work today, Audrey."
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "My heart was pounding in my chest whenever I saw you walk by!"
        if (audrey.love <= 80 or audrey.sexperience == 0) and not hero.charm >= 30:
            audrey_nvl "That's like sexual harassment, you know?"
            audrey_nvl "Maybe keep that to yourself next time?"
            $ audrey.love -= 1
        elif audrey.sexperience == 0 or (audrey.love <= 100 and not hero.charm >= 50):
            audrey_nvl "I like the sound of that!"
            audrey_nvl "I'll be sure to do it more often now I know!"
            $ audrey.love += 1
        else:
            audrey_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 100:
                    $ audrey.love += 1
            else:
                $ audrey.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "What are you wearing right now, Audrey?"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "Give me a good mental picture!"
        if (audrey.love <= 80 or audrey.sexperience == 0) and not hero.charm >= 30:
            audrey_nvl "Hah - like I'm gonna tell you that!"
            audrey_nvl "Dream on, loser!"
            $ audrey.love -= 1
        elif audrey.sexperience == 0 or (audrey.love <= 100 and not hero.charm >= 50):
            audrey_nvl "The outfit I wore in the office today, yeah?"
            audrey_nvl "The one you're always checking me out in!"
            $ audrey.love += 1
        else:
            audrey_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 100:
                    $ audrey.love += 1
            else:
                $ audrey.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "You want to grab a bite to eat after work, Audrey?"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "I know a quiet little place where we can be alone!"
        if (audrey.love <= 80 or audrey.sexperience == 0) and not hero.charm >= 30:
            audrey_nvl "No way!"
            audrey_nvl "I have to put up with you all day at work already!"
            $ audrey.love -= 1
        elif audrey.sexperience == 0 or (audrey.love <= 100 and not hero.charm >= 50):
            audrey_nvl "Sounds to me."
            audrey_nvl "We can flirt without anyone seeing us!"
            $ audrey.love += 1
        else:
            audrey_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 100:
                    $ audrey.love += 1
            else:
                $ audrey.love += 1
        $ hero.fun += 0.3
    return

label audrey_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I can't keep my mind on my work, Audrey."
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "All I can think about is fucking you over my desk!"
        if audrey.love <= 100 and not hero.charm >= 40:
            audrey_nvl "Urgh...it's enough I have to work in this dump."
            audrey_nvl "I don't need your slobbering texts on top of that!"
            $ audrey.love -= 2
        elif audrey.sexperience < 2 or audrey.love <= 150:
            audrey_nvl "I like the sound of that!"
            audrey_nvl "Imagine me moaning the whole time!"
            audrey_nvl "Just loving having your cock inside of me!"
            $ audrey.love += 2
        else:
            audrey_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 150:
                    $ audrey.love += 2
                elif audrey.love <= 175:
                    $ audrey.love += 1
            else:
                $ audrey.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "What are you wearing, Audrey?"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "I want to picture you while I jerk-off!"
        if audrey.love <= 100 and not hero.charm >= 40:
            audrey_nvl "No way!"
            audrey_nvl "I'm not helping you wank!"
            $ audrey.love -= 2
        elif audrey.sexperience < 2 or audrey.love <= 150:
            audrey_nvl "Fuck that - imagine me talking it all off, yeah?"
            audrey_nvl "Then shoving my tits in your face!"
            $ audrey.love += 2
        else:
            audrey_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 150:
                    $ audrey.love += 2
                elif audrey.love <= 175:
                    $ audrey.love += 1
            else:
                $ audrey.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "When can you get over here and suck my cock, Audrey?"
        if audrey.activity_name == "sleep" and audrey.love < 70:
            audrey_nvl "Leave me alone, I was asleep..."
            $ audrey.love -= 2
            return
        mchero_nvl "It feels like forever since you last did that!"
        if audrey.love <= 100 and not hero.charm >= 40:
            audrey_nvl "Geez...you sound SO needy!"
            audrey_nvl "That's not the way to turn a girl on..."
            $ audrey.love -= 2
        elif audrey.sexperience < 2 or audrey.love <= 150:
            audrey_nvl "Looks like I need to come up with the goods!"
            audrey_nvl "Don't worry - I'll be sucking it as soon as I can!"
            $ audrey.love += 2
        else:
            audrey_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if audrey.love <= 150:
                    $ audrey.love += 2
                elif audrey.love <= 175:
                    $ audrey.love += 1
            else:
                $ audrey.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
