label alexis_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        alexis_nvl "Just messaging you to say hi!"
        alexis_nvl "Message me back if you feel like chatting."
        alexis_nvl "Or just to say hi back?"
    elif texto == 1:
        alexis_nvl "That place you took me the other night was pretty great."
        alexis_nvl "You sure have great taste when it comes to planning a date."
        alexis_nvl "I might have to let you plan all of them in future!"
    else:
        alexis_nvl "Thinking about you all the time right now."
        alexis_nvl "How weird is that?"
        alexis_nvl "After all this time - it's like we just picked up where we left off!"
    return

label alexis_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        alexis_nvl "Thinking about you right now, yeah?"
        alexis_nvl "Thinking about what we're going to do when we're together."
        alexis_nvl "Thinking that we should have some serious fun!"
    elif texto == 1:
        alexis_nvl "I was remembering what we used to get up to in high-school, yeah?"
        alexis_nvl "We were pretty wild back then, got away with some crazy shit!"
        alexis_nvl "You think we could do that again, maybe even top it?"
    else:
        alexis_nvl "Ooh...wear that T-shirt again when have a date, okay?"
        alexis_nvl "You know that one, right?"
        alexis_nvl "It REALLY shows off your biceps!"
    return

label alexis_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        alexis_nvl "I'm feeling super horny today!"
        alexis_nvl "So get over here and do your duty, okay?"
        if alexis.flags.story == 2:
            alexis_nvl "Or I'll find a way to do it myself!"
        else:
            alexis_nvl "Or I'll find somebody else that will!"
    elif texto == 1:
        alexis_nvl "You want to fuck me in a bathroom, huh?"
        alexis_nvl "I never got fucked by you in a bathroom before!"
        alexis_nvl "I...I mean I never got fucked in a bathroom before..."
    else:
        alexis_nvl "Mmm...I just want to curl up in bed with you right now."
        alexis_nvl "Spend all day cuddled up to you, like we used to in high-school."
        alexis_nvl "Oh, and fuck like we used to back then too!"
    return

label alexis_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Alexis, I'm not doing anything right now."
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "You want to come over here and hang out?"
        alexis_nvl "Sorry, can't make it - working."
        if persistent.difficulty >= 0:
            if alexis.love <= 50:
                $ alexis.love += 1
        else:
            $ alexis.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Alexis, I found an old high-school photo of us all!"
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "It's the year you had those braces fitted!"
        alexis_nvl "Urgh - I hate that picture!"
        alexis_nvl "Wait a minute - isn't that the year you got all that acne?"
        if persistent.difficulty >= 0:
            if alexis.love <= 50:
                $ alexis.love += 1
        else:
            $ alexis.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Alexis, you were pretty drunk the other night!"
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        alexis_nvl "Speak for yourself!"
        alexis_nvl "I was the one rubbing your back while you puked!"
        if persistent.difficulty >= 0:
            if alexis.love <= 50:
                $ alexis.love += 1
        else:
            $ alexis.love += 1
        $ hero.fun += 0.2
    return

label alexis_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Alexis, let me ask you a question."
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "What are you wearing right now?"
        if (alexis.love <= 80 or alexis.sexperience == 0) and not hero.charm >= 30:
            alexis_nvl "I don't have time for this right now!"
            $ alexis.love -= 1
        elif alexis.sexperience == 0 or (alexis.love <= 100 and not hero.charm >= 50):
            alexis_nvl "Something tight and slinky, and it shows off ALL of my curves!"
            $ alexis.love += 1
        else:
            alexis_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 100:
                    $ alexis.love += 1
            else:
                $ alexis.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "You remember all the dates we went on, back in high-school?"
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "We got up to some pretty wild stuff!"
        if (alexis.love <= 80 or alexis.sexperience == 0) and not hero.charm >= 30:
            alexis_nvl "Why do you always have to go dragging up the past?"
            alexis_nvl "Just leave it alone!"
            $ alexis.love -= 1
        elif alexis.sexperience == 0 or (alexis.love <= 100 and not hero.charm >= 50):
            alexis_nvl "We'll do it all again the next time I see you."
            alexis_nvl "After we're done, you can tell me how my memory is!"
            $ alexis.love += 1
        else:
            alexis_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 100:
                    $ alexis.love += 1
            else:
                $ alexis.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't stop thinking about you, Alexis!"
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "And I can't wait to see you again."
        if (alexis.love <= 80 or alexis.sexperience == 0) and not hero.charm >= 30:
            alexis_nvl "You're so needy - it's kind of pathetic!"
            $ alexis.love -= 1
        elif alexis.sexperience == 0 or (alexis.love <= 100 and not hero.charm >= 50):
            alexis_nvl "Me too - and I want it to be REALLY memorable when we do!"
            $ alexis.love += 1
        else:
            alexis_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 100:
                    $ alexis.love += 1
            else:
                $ alexis.love += 1
        $ hero.fun += 0.3
    return

label alexis_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Alexis, what kind of underwear have you got on?"
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "I want to get a good mental image of you in it!"
        if alexis.love <= 100 and not hero.charm >= 40:
            alexis_nvl "Oh give it a rest!"
            alexis_nvl "I don't have time for this."
            $ alexis.love -= 2
        elif alexis.sexperience < 2 or alexis.love <= 150:
            alexis_nvl "Mmm...it's pretty skimpy and slinky!"
            alexis_nvl "Almost like I'm wearing nothing at all..."
            $ alexis.love += 2
        else:
            alexis_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 150:
                    $ alexis.love += 2
                elif alexis.love <= 175:
                    $ alexis.love += 1
            else:
                $ alexis.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I'm thinking about the last time you sucked my cock, Alexis."
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "It felt so good that I can't wait until you do it again!"
        if alexis.love <= 100 and not hero.charm >= 40:
            alexis_nvl "Really?!?"
            alexis_nvl "Is that all you think about?"
            $ alexis.love -= 2
        elif alexis.sexperience < 2 or alexis.love <= 150:
            alexis_nvl "Oh...you reminded me of it too!"
            alexis_nvl "Now I can't wait to suck it again myself!"
            $ alexis.love += 2
        else:
            alexis_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 150:
                    $ alexis.love += 2
                elif alexis.love <= 175:
                    $ alexis.love += 1
            else:
                $ alexis.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "I hate to admit it, Alexis."
        if alexis.activity_name == "sleep" and alexis.love < 70:
            alexis_nvl "Leave me alone, I was asleep..."
            $ alexis.love -= 2
            return
        mchero_nvl "But sometimes the idea of you with other guys..."
        mchero_nvl "Well...it really turns me on!"
        if alexis.love <= 100 and not hero.charm >= 40:
            alexis_nvl "Wow...just wow!"
            alexis_nvl "That's SO pathetic!"
            $ alexis.love -= 2
        elif alexis.sexperience < 2 or alexis.love <= 150:
            alexis_nvl "Oh, but you know I'm always thinking of you, right?"
            alexis_nvl "Even when they're cocks are inside of me!"
            $ alexis.love += 2
        else:
            alexis_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if alexis.love <= 150:
                    $ alexis.love += 2
                elif alexis.love <= 175:
                    $ alexis.love += 1
            else:
                $ alexis.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
