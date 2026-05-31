label aletta_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        aletta_nvl "When are you going to return my messages?"
        aletta_nvl "I need to talk to you about something important!"
        aletta_nvl "And...well...it's not work-related..."
    elif texto == 1:
        aletta_nvl "I know I should really be working right now."
        aletta_nvl "But I can't stop thinking about you!"
        aletta_nvl "What have you done to me?"
    else:
        aletta_nvl "I had a really great time on our last date."
        aletta_nvl "Let me know when we can do it again, okay?"
        aletta_nvl "And try not to keep me waiting for a reply!"
    return

label aletta_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        aletta_nvl "Urgh...this meeting is so boring!"
        aletta_nvl "My mind keeps wandering off..."
        aletta_nvl "I keep thinking about doing something fun and naughty with you instead!"
    elif texto == 1:
        aletta_nvl "I've been riding my bike pretty hard today."
        aletta_nvl "And when I went over some speedbumps, it was pretty intense!"
        aletta_nvl "It rubbed me so hard down there - it almost made me cum!"
    else:
        aletta_nvl "I'm wearing that underwear you like today."
        aletta_nvl "The set with the stockings and suspenders?"
        aletta_nvl "Just wanted you to get a good mental image of that..."
    return

label aletta_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        aletta_nvl "Urgh...you're getting inside of my head!"
        aletta_nvl "I'm bored at work - and I'm NEVER bored at work!"
        aletta_nvl "All I can think about is you fucking me over this damn desk!"
    elif texto == 1:
        aletta_nvl "I'm picking out my panties, bra and stockings."
        aletta_nvl "Then I'm putting my riding leathers on over the top."
        aletta_nvl "And I want you to take them off again when I get to your place, okay?"
    else:
        aletta_nvl "I'm at the shooting range, getting in some practice."
        aletta_nvl "How about I come over after I'm done?"
        aletta_nvl "Then you can practice shooting your load into me?"
    return

label aletta_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Aletta, going on a coffee run."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "You want some hot joe?"
        aletta_nvl "No thanks - I don't need caffeine to keep me awake!"
        if persistent.difficulty >= 0:
            if aletta.love <= 50:
                $ aletta.love += 1
        else:
            $ aletta.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Aletta, I just saw a guy on a Kusakowa 500 ride past!"
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "It was so loud it rattled my teeth!"
        aletta_nvl "Really?"
        aletta_nvl "I wish I'd been there to see it!"
        if persistent.difficulty >= 0:
            if aletta.love <= 50:
                $ aletta.love += 1
        else:
            $ aletta.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Aletta, you know all about guns, right?"
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "I was thinking about applying for a licence of my own."
        aletta_nvl "You'd have to learn to shoot straight first!"
        if persistent.difficulty >= 0:
            if aletta.love <= 50:
                $ aletta.love += 1
        else:
            $ aletta.love += 1
        $ hero.fun += 0.2
    return

label aletta_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Aletta, I can't stop thinking about you."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "What are you wearing right now?"
        if (aletta.love <= 80 or aletta.sexperience == 0) and not hero.charm >= 30:
            aletta_nvl "A frown on my face - because you're distracting me from my work!"
            $ aletta.love -= 1
        elif aletta.sexperience == 0 or (aletta.love <= 100 and not hero.charm >= 50):
            aletta_nvl "A tight, pencil skirt, with black stockings underneath!"
            $ aletta.love += 1
        else:
            aletta_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 100:
                    $ aletta.love += 1
            else:
                $ aletta.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I'd love you to take me for another ride on your bike, Aletta."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "Clinging onto you like that - it felt really good!"
        if (aletta.love <= 80 or aletta.sexperience == 0) and not hero.charm >= 30:
            aletta_nvl "No can do - my bike is in the shop for repairs."
            $ aletta.love -= 1
        elif aletta.sexperience == 0 or (aletta.love <= 100 and not hero.charm >= 50):
            aletta_nvl "I'll go faster next time - so you'll have to hold me tighter!"
            $ aletta.love += 1
        else:
            aletta_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 100:
                    $ aletta.love += 1
            else:
                $ aletta.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I can't get a shred of work done today, Aletta."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "Not after I saw you walk past my office door!"
        if (aletta.love <= 80 or aletta.sexperience == 0) and not hero.charm >= 30:
            aletta_nvl "Then close the blinds and try harder!"
            $ aletta.love -= 1
        elif aletta.sexperience == 0 or (aletta.love <= 100 and not hero.charm >= 50):
            aletta_nvl "You have to work hard, otherwise I can't reward you!"
            $ aletta.love += 1
        else:
            aletta_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 100:
                    $ aletta.love += 1
            else:
                $ aletta.love += 1
        $ hero.fun += 0.3
    return

label aletta_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Where are you right now, Aletta?"
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "Because I'm sitting here with a stiff one from thinking about you!"
        if aletta.love <= 100 and not hero.charm >= 40:
            aletta_nvl "Where the hell do you think I am?"
            aletta_nvl "I'm at work and I don't have time for this!"
            $ aletta.love -= 2
        elif aletta.sexperience < 2 or aletta.love <= 150:
            aletta_nvl "I'm at work, sitting at my desk."
            aletta_nvl "But nobody can see I have my hand in my panties, stroking my pussy!"
            $ aletta.love += 2
        else:
            aletta_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 150:
                    $ aletta.love += 2
                elif aletta.love <= 175:
                    $ aletta.love += 1
            else:
                $ aletta.love += 2
        $ hero.fun += 0.2
    elif text_id == 1 and aletta.flags.sidestory:
        mchero_nvl "Your bike's pretty cool, Aletta."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "And I kind of got turned on riding it!"
        mchero_nvl "But I don't think I could handle all that horsepower!"
        if aletta.love <= 100 and not hero.charm >= 40:
            aletta_nvl "You're probably not man enough."
            aletta_nvl "That's the problem!"
            $ aletta.love -= 2
        elif aletta.sexperience < 2 or aletta.love <= 150:
            aletta_nvl "Oh, I think you could learn."
            aletta_nvl "How about you practice riding me until you do?"
            $ aletta.love += 2
        else:
            aletta_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 150:
                    $ aletta.love += 2
                elif aletta.love <= 175:
                    $ aletta.love += 1
            else:
                $ aletta.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You're always tied to your desk, Aletta."
        if aletta.activity_name == "sleep" and aletta.love < 70:
            aletta_nvl "Leave me alone, I was asleep..."
            $ aletta.love -= 2
            return
        mchero_nvl "I wish you'd let me tie you to it - then fuck you good and hard!"
        if aletta.love <= 100 and not hero.charm >= 40:
            aletta_nvl "Yeah, that's not going to happen anytime soon, is it?"
            $ aletta.love -= 2
        elif aletta.sexperience < 2 or aletta.love <= 150:
            aletta_nvl "That sounds like a great way to burn off some stress!"
            aletta_nvl "So long as you promise to spank my ass too, okay?"
            $ aletta.love += 2
        else:
            aletta_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if aletta.love <= 150:
                    $ aletta.love += 2
                elif aletta.love <= 175:
                    $ aletta.love += 1
            else:
                $ aletta.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
