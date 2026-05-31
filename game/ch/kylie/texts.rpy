label kylie_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kylie_nvl "Hey, I just wondered if you were thinking about me?"
        kylie_nvl "Because I'm thinking about you all the time!"
        kylie_nvl "In fact, you're the only thing on my mind!"
    elif texto == 1:
        kylie_nvl "I can't wait to go out on another date with you."
        kylie_nvl "The last one was just perfect - so perfect!"
        kylie_nvl "Just like I always imagined it would be!"
    else:
        kylie_nvl "Hey, are you free right now?"
        kylie_nvl "Would you like to hang out with me?"
        kylie_nvl "Because you wouldn't believe how close I am to you..."
    return

label kylie_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kylie_nvl "I'm always thinking about you, you know that, right?"
        kylie_nvl "Almost every single moment of the day!"
        kylie_nvl "I'm thinking about your hands touching me all over!"
    elif texto == 1:
        kylie_nvl "You like it when I wear short skirts, don't you?"
        kylie_nvl "Because I just have to have your eyes on me!"
        kylie_nvl "Knowing you're looking at me...it...it turns me on!"
    else:
        kylie_nvl "Are you doing anything right now?"
        kylie_nvl "Because I'm not - so I could come over to your place."
        kylie_nvl "Then you can do whatever you want to me..."
    return

label kylie_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kylie_nvl "When can I come over there and get a hold of you?!?"
        kylie_nvl "I feel like I haven't seen you in ages!"
        kylie_nvl "I need you inside of me, or else I'll go crazy!"
    elif texto == 1:
        kylie_nvl "Oh, you should see how my butt looks in this outfit!"
        kylie_nvl "It's so round and it sways when I walk too!"
        kylie_nvl "Seriously, my ass could only look better with your cock in it!"
    else:
        kylie_nvl "Mmm...I have my hand in my panties right now."
        kylie_nvl "I'm thinking about you while I touch myself."
        kylie_nvl "And it's making me SO wet!"
    return

label kylie_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Kylie, I can't do anything right now."
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        kylie_nvl "I know - that looks like a lot of coursework!"
        mchero_nvl "Huh?!?"
        mchero_nvl "How did you know I was studying?"
        kylie_nvl "Lucky guess...I'm not watching you or anything..."
        if persistent.difficulty >= 0:
            if kylie.love <= 50:
                $ kylie.love += 1
        else:
            $ kylie.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Kylie, how are you doing with your studies?"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "Let me know if you need anymore help."
        kylie_nvl "Thanks for the offer - I need all the help I can get!"
        if persistent.difficulty >= 0:
            if kylie.love <= 50:
                $ kylie.love += 1
        else:
            $ kylie.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Kylie, you want to meet up?"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "We could hang out and just chill, or do whatever you like."
        kylie_nvl "Sounds great - and I know exactly where to find you!"
        if persistent.difficulty >= 0:
            if kylie.love <= 50:
                $ kylie.love += 1
        else:
            $ kylie.love += 1
        $ hero.fun += 0.2
    return

label kylie_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Kylie, I can't stop thinking about you!"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "Just the thought of you drives me crazy!"
        if (kylie.love <= 80 or kylie.sexperience == 0) and not hero.charm >= 30:
            kylie_nvl "Hey - a little less of the crazy please!"
            $ kylie.love -= 1
        elif kylie.sexperience == 0 or (kylie.love <= 100 and not hero.charm >= 50):
            kylie_nvl "Wonderful - that's just how it should be!"
            $ kylie.love += 1
        else:
            kylie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 100:
                    $ kylie.love += 1
            else:
                $ kylie.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "What are you wearing right now, Kylie?"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "I've got that body of your's on my mind!"
        if (kylie.love <= 80 or kylie.sexperience == 0) and not hero.charm >= 30:
            kylie_nvl "What...can't you see me from there?"
            kylie_nvl "Damn it...I mean obviously you can't see me!"
            kylie_nvl "It's not like I'm spying on you or anything..."
            $ kylie.love -= 1
        elif kylie.sexperience == 0 or (kylie.love <= 100 and not hero.charm >= 50):
            kylie_nvl "You don't need to know that."
            kylie_nvl "Just that it's clinging to me and I'm stroking myself through it right now!"
            $ kylie.love += 1
        else:
            kylie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 100:
                    $ kylie.love += 1
            else:
                $ kylie.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "Let's go to a nightclub, Kylie."
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "But I want you to wear that white dress, yeah?"
        mchero_nvl "I think you'd look great dancing in that!"
        if (kylie.love <= 80 or kylie.sexperience == 0) and not hero.charm >= 30:
            kylie_nvl "I don't like nightclubs."
            kylie_nvl "There are always too many other girls looking at you!"
            $ kylie.love -= 1
        elif kylie.sexperience == 0 or (kylie.love <= 100 and not hero.charm >= 50):
            kylie_nvl "Sure thing!"
            kylie_nvl "You can see it for real!"
            $ kylie.love += 1
        else:
            kylie_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 100:
                    $ kylie.love += 1
            else:
                $ kylie.love += 1
        $ hero.fun += 0.3
    return

label kylie_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "You're always on my mind, Kylie!"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "All I can think about is how much I want to fuck you!"
        if kylie.love <= 100 and not hero.charm >= 40:
            kylie_nvl "That's not enough for me!"
            kylie_nvl "I need to be more to you than that!"
            $ kylie.love -= 2
        elif kylie.sexperience < 2 or kylie.love <= 150:
            kylie_nvl "That's how it should be!"
            kylie_nvl "Just imagine putting your cock in me!"
            kylie_nvl "I'm getting wet just picturing it!"
            $ kylie.love += 2
        else:
            kylie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 150:
                    $ kylie.love += 2
                elif kylie.love <= 175:
                    $ kylie.love += 1
            else:
                $ kylie.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "You've got such a sexy ass, Kylie!"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "I wish it was sitting on my lap right now!"
        if kylie.love <= 100 and not hero.charm >= 40:
            kylie_nvl "I want to hold your hand and be at your side."
            kylie_nvl "Not sit on your lap like a child!"
            $ kylie.love -= 2
        elif kylie.sexperience < 2 or kylie.love <= 150:
            kylie_nvl "Oh really?"
            kylie_nvl "And I wonder where something else would be?"
            kylie_nvl "Would it happen to be inside of my pussy?"
            $ kylie.love += 2
        else:
            kylie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 150:
                    $ kylie.love += 2
                elif kylie.love <= 175:
                    $ kylie.love += 1
            else:
                $ kylie.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You need some help with your studies, Kylie?"
        if kylie.activity_name == "sleep" and kylie.love < 70:
            kylie_nvl "Leave me alone, I was asleep..."
            $ kylie.love -= 2
            return
        mchero_nvl "I could come over there and eat you out while you work!"
        if kylie.love <= 100 and not hero.charm >= 40:
            kylie_nvl "I don't have time for this right now."
            kylie_nvl "I'm behind in my studies as it is!"
            $ kylie.love -= 2
        elif kylie.sexperience < 2 or kylie.love <= 150:
            kylie_nvl "Mmm...that sounds like a great idea!"
            kylie_nvl "When can you come over and get let me sit on your face?"
            $ kylie.love += 2
        else:
            kylie_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kylie.love <= 150:
                    $ kylie.love += 2
                elif kylie.love <= 175:
                    $ kylie.love += 1
            else:
                $ kylie.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
