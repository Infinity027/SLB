label lexi_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lexi_nvl "Hey, you showed me a really good time the other night!"
        lexi_nvl "In fact, I think I'm still a little hung-over!"
        lexi_nvl "Can't wait to see what you come up with next."
    elif texto == 1:
        lexi_nvl "Why can't I stop thinking about you?"
        lexi_nvl "It's like I can't get a thing done with you in my head!"
        if hero.is_male:
            lexi_nvl "You've got a lot to answer for, mister!"
        else:
            lexi_nvl "You've got a lot to answer for, miss!"
    else:
        lexi_nvl "Hey, I've got some time on my hands right now."
        lexi_nvl "You want to meet up and do something with me?"
        lexi_nvl "No pressure - just thought we could have some fun, yeah?"
    return

label lexi_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lexi_nvl "Geez...I feel so fucking horny today!"
        lexi_nvl "I dunno what's the matter with me."
        lexi_nvl "Just thought you'd like to know that!"
    elif texto == 1:
        lexi_nvl "Urgh...I'm freezing my ass off today, it's so cold!"
        lexi_nvl "Maybe I should have worn more clothes?"
        lexi_nvl "Nah - that's mean nobody could see my ass and my tits!"
    else:
        lexi_nvl "You got those tight pants on today, huh?"
        if hero.is_male:
            lexi_nvl "The ones that show off your junk?"
        else:
            lexi_nvl "The ones that show off your slit?"
        lexi_nvl "Mmm...I love the look of you in those!"
    return

label lexi_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        lexi_nvl "You know, I'm SO good to you!"
        lexi_nvl "With most guys I charge for it."
        lexi_nvl "But I let you have it for free!"
    elif texto == 1:
        lexi_nvl "I can't stop thinking about you right now!"
        lexi_nvl "When can you get over here?"
        if hero.is_male:
            lexi_nvl "I need your cock in my pussy!"
        else:
            lexi_nvl "I need you in my pussy!"
    else:
        if hero.is_male:
            lexi_nvl "I loved it when I sucked your cock in that alley."
        else:
            lexi_nvl "I loved it when I licked your pussy in that alley."
        lexi_nvl "I want to do it someplace like that again."
        lexi_nvl "But this time, I wanna be fucked up against the wall!"
    return

label lexi_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Lexi, what are you doing right now?"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "I'm free, if you want to hang out."
        lexi_nvl "I'd love to, but I can't."
        lexi_nvl "I got some business needs handling!"
        if persistent.difficulty >= 0:
            if lexi.love <= 50:
                $ lexi.love += 1
        else:
            $ lexi.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Lexi, how much does a trailer like yours cost?"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        lexi_nvl "How the hell should I know?"
        lexi_nvl "You think I pay my rent with actual money?!?"
        if persistent.difficulty >= 0:
            if lexi.love <= 50:
                $ lexi.love += 1
        else:
            $ lexi.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Lexi, did I see you on the news last night?"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        lexi_nvl "Yeah, could be that you did."
        lexi_nvl "Geez...I hope they didn't use my old mugshot."
        lexi_nvl "I look so much better in the new one!"
        if persistent.difficulty >= 0:
            if lexi.love <= 50:
                $ lexi.love += 1
        else:
            $ lexi.love += 1
        $ hero.fun += 0.2
    return

label lexi_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Lexi, tell me what you have on right now?"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "I bet it's something sexy, right?"
        mchero_nvl "Revealing too!"
        if (lexi.love <= 80 or lexi.sexperience == 0) and not hero.charm >= 30:
            lexi_nvl "Piss off - you're not getting it for free!"
            $ lexi.love -= 1
        elif lexi.sexperience == 0 or (lexi.love <= 100 and not hero.charm >= 50):
            lexi_nvl "Oh yeah - I'm showing everything off!"
            lexi_nvl "Leaving nothing to the imagination!"
            $ lexi.love += 1
        else:
            lexi_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 100:
                    $ lexi.love += 1
            else:
                $ lexi.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I can't stop thinking about you, Lexi!"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "When can we get together again?!?"
        if (lexi.love <= 80 or lexi.sexperience == 0) and not hero.charm >= 30:
            lexi_nvl "I'm pretty busy, so you'll just have to wait."
            $ lexi.love -= 1
        elif lexi.sexperience == 0 or (lexi.love <= 100 and not hero.charm >= 50):
            lexi_nvl "Aww...it won't be much longer!"
            lexi_nvl "Absence makes the cock grow harder!"
            $ lexi.love += 1
        else:
            lexi_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 100:
                    $ lexi.love += 1
            else:
                $ lexi.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I want to make love to you, Lexi!"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "I want to make your trailer rock back and forth!"
        if (lexi.love <= 80 or lexi.sexperience == 0) and not hero.charm >= 30:
            lexi_nvl "No way - my trailer's already fucked as it is!"
            $ lexi.love -= 1
        elif lexi.sexperience == 0 or (lexi.love <= 100 and not hero.charm >= 50):
            lexi_nvl "Sounds like fun!"
            lexi_nvl "But you'd better make me groan more than the damn trailer!"
            $ lexi.love += 1
        else:
            lexi_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 100:
                    $ lexi.love += 1
            else:
                $ lexi.love += 1
        $ hero.fun += 0.3
    return

label lexi_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Can't get you out of my head, Lexi!"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "So I need to get my cock into your pussy!"
        if lexi.love <= 100 and not hero.charm >= 40:
            lexi_nvl "Get to the back of the queue!"
            lexi_nvl "I got people that'll pay me for that kind of thing!"
            $ lexi.love -= 2
        elif lexi.sexperience < 2 or lexi.love <= 150:
            lexi_nvl "You sure know how to charm a girl!"
            lexi_nvl "I'm getting wet just reading about it!"
            $ lexi.love += 2
        else:
            lexi_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 150:
                    $ lexi.love += 2
                elif lexi.love <= 175:
                    $ lexi.love += 1
            else:
                $ lexi.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "What are you wearing right now, Lexi?"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "Must be something pretty skimpy, right?"
        mchero_nvl "Something that shows off your butt?"
        if lexi.love <= 100 and not hero.charm >= 40:
            lexi_nvl "Piss off!"
            lexi_nvl "I'm hung over!"
            $ lexi.love -= 2
        elif lexi.sexperience < 2 or lexi.love <= 150:
            lexi_nvl "I'm still in bed."
            lexi_nvl "So I don't have a stitch on..."
            $ lexi.love += 2
        else:
            lexi_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 150:
                    $ lexi.love += 2
                elif lexi.love <= 175:
                    $ lexi.love += 1
            else:
                $ lexi.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "I want to buy shares in your butt, Lexi!"
        if lexi.activity_name == "sleep" and lexi.love < 70:
            lexi_nvl "Leave me alone, I was asleep..."
            $ lexi.love -= 2
            return
        mchero_nvl "That way I can fuck it whenever I want!"
        if lexi.love <= 100 and not hero.charm >= 40:
            lexi_nvl "You couldn't afford to buy my ass!"
            lexi_nvl "Trust me, it's prime real-estate!"
            $ lexi.love -= 2
        elif lexi.sexperience < 2 or lexi.love <= 150:
            lexi_nvl "You don't need to buy it!"
            lexi_nvl "Just stick a cock in it and claim it for yourself!"
            $ lexi.love += 2
        else:
            lexi_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if lexi.love <= 150:
                    $ lexi.love += 2
                elif lexi.love <= 175:
                    $ lexi.love += 1
            else:
                $ lexi.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
