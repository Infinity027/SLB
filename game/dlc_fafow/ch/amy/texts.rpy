label amy_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        amy_nvl "I'm getting off work early today."
        amy_nvl "And I don't have anything planned either."
        amy_nvl "Don't suppose you want to hang out?"
    elif texto == 1:
        amy_nvl "I had a blast on our date the other night."
        amy_nvl "When can we do it again?"
    else:
        amy_nvl "I can't stop thinking about you!"
        amy_nvl "It's like you're stuck inside of my head!"
        amy_nvl "Are you thinking about me too?"
    return

label amy_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        amy_nvl "Thinking about you while I'm getting dressed."
        amy_nvl "Picking out all the stuff that you like to see me in."
        amy_nvl "Short skirt, stockings, boots!"
    elif texto == 1:
        amy_nvl "Come hang out with me at work?"
        amy_nvl "Save me from dying of loneliness?"
        amy_nvl "Horniness too..."
    else:
        amy_nvl "You didn't tell me you were in the Deathless Harpies!"
        amy_nvl "I...kind of need to talk to you about that band."
        amy_nvl "And it's going to be a bit of a long talk too..."
    return

label amy_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        amy_nvl "I can't wait to get off work today."
        amy_nvl "Because when I do, I'm coming straight over to your place."
        amy_nvl "And you'd better be ready to fuck!"
    elif texto == 1:
        amy_nvl "You like me in that really short skirt, yeah?"
        amy_nvl "Well, how about I wear it with no panties?"
        amy_nvl "Would you like that?"
    else:
        amy_nvl "You think if we're quiet, you could fuck me at work?"
        amy_nvl "I kinda want to do it in one of the aisles, you know?"
        amy_nvl "While people are watching and they don't know what we're doing!"
    return

label amy_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Amy, how's work going?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "Did Shawn bore you to death yet?"
        amy_nvl "Urgh...not yet."
        amy_nvl "But he's trying real hard!"
        if persistent.difficulty >= 0:
            if amy.love <= 50:
                $ amy.love += 1
        else:
            $ amy.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Amy, you free to hang out?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "Maybe do something fun?"
        amy_nvl "Sorry, no can do."
        amy_nvl "Shawn's made me take an extra shift!"
        if persistent.difficulty >= 0:
            if amy.love <= 50:
                $ amy.love += 1
        else:
            $ amy.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Amy, how are you liking the hot weather?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        amy_nvl "I'm wearing black and heavy make-up - so what do you think?!?"
        amy_nvl "I feel like I'm melting!"
        if persistent.difficulty >= 0:
            if amy.love <= 50:
                $ amy.love += 1
        else:
            $ amy.love += 1
        $ hero.fun += 0.2
    return

label amy_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Amy - do you happen to have those shorts on today?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "The ones that you wear with the ripped stockings?"
        if (amy.love <= 80 or amy.sexperience == 0) and not hero.charm >= 30:
            amy_nvl "No, they're in the wash, and it's not laundry day until next week."
            $ amy.love -= 1
        elif amy.sexperience == 0 or (amy.love <= 100 and not hero.charm >= 50):
            amy_nvl "I do...but it's such a shame - I have to keep bending over in them all the time!"
            $ amy.love += 1
        else:
            amy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if amy.love <= 100:
                    $ amy.love += 1
            else:
                $ amy.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I have to see you again, Amy!"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "I might even have to come down there and just watch you work!"
        if (amy.love <= 80 or amy.sexperience == 0) and not hero.charm >= 30:
            amy_nvl "Ew...that's kind of creepy, you know?"
            $ amy.love -= 1
        elif amy.sexperience == 0 or (amy.love <= 100 and not hero.charm >= 50):
            amy_nvl "Oh my...I can feel your eyes on me already!"
            $ amy.love += 1
        else:
            amy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if amy.love <= 100:
                    $ amy.love += 1
            else:
                $ amy.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "Let's go to a goth club, Amy."
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "Somewhere we can dance all night, get hot and sweaty!"
        if (amy.love <= 80 or amy.sexperience == 0) and not hero.charm >= 30:
            amy_nvl "Goth's a way of life, you know?"
            amy_nvl "Not just a thrill for when you're horny!"
            $ amy.love -= 1
        elif amy.sexperience == 0 or (amy.love <= 100 and not hero.charm >= 50):
            amy_nvl "I know just the place - but only so long as you dance REALLY close to me!"
            $ amy.love += 1
        else:
            amy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if amy.love <= 100:
                    $ amy.love += 1
            else:
                $ amy.love += 1
        $ hero.fun += 0.3
    return

label amy_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Amy, tell me something..."
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "Do you have official goth underwear?"
        if amy.love <= 100 and not hero.charm >= 40:
            amy_nvl "What?!?"
            amy_nvl "Of course not!"
            $ amy.love -= 2
        elif amy.sexperience < 2 or amy.love <= 150:
            amy_nvl "Of course I do!"
            amy_nvl "They're black and slinky..."
            amy_nvl "And there's even a skull on top of my pussy!"
            $ amy.love += 2
        else:
            amy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if amy.love <= 150:
                    $ amy.love += 2
                elif amy.love <= 175:
                    $ amy.love += 1
            else:
                $ amy.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Amy, how about I come over there right now?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "I want to park my batmobile in your batcave - you know what I mean?!?"
        if amy.love <= 100 and not hero.charm >= 40:
            amy_nvl "Eww..."
            amy_nvl "Don't talk about my pussy like that!"
            $ amy.love -= 2
        elif amy.sexperience < 2 or amy.love <= 150:
            amy_nvl "Oh my..."
            amy_nvl "I'd better have Alfred make it look nice for you!"
            $ amy.love += 2
        else:
            amy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if amy.love <= 150:
                    $ amy.love += 2
                elif amy.love <= 175:
                    $ amy.love += 1
            else:
                $ amy.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Amy, how many of those really short skirts do you have?"
        if amy.activity_name == "sleep" and amy.love < 70:
            amy_nvl "Leave me alone, I was asleep..."
            $ amy.love -= 2
            return
        mchero_nvl "Because I'd like to fuck you in every one of them!"
        if amy.love <= 100 and not hero.charm >= 40:
            amy_nvl "Oh, nice one!"
            amy_nvl "Way to make me feel like a sex-object!"
            $ amy.love -= 2
        elif amy.sexperience < 2 or amy.love <= 150:
            amy_nvl "Now there's a challenge!"
            amy_nvl "I might just have to keep buying more of them!"
            $ amy.love += 2
        else:
            amy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if amy.love <= 150:
                    $ amy.love += 2
                elif amy.love <= 175:
                    $ amy.love += 1
            else:
                $ amy.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
