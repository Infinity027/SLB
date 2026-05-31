label bree_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        bree_nvl "We got some serious sun happening today."
        bree_nvl "That means it's time to break out the bikini!"
        bree_nvl "You want to come join me in the pool?"
    elif texto == 1:
        bree_nvl "You've got to get back here and see this!"
        bree_nvl "Seriously, you're not going to believe it!"
        bree_nvl "You have to see what I unlocked on this game!"
    else:
        bree_nvl "I just wanted to drop you a line and say hi."
        bree_nvl "No particular reason why, I gotta admit."
        bree_nvl "I was just thinking about you, that's all!"
    return

label bree_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        bree_nvl "Ah, I'm getting tired of playing on the Zbox."
        bree_nvl "I've beaten this game so many times already!"
        bree_nvl "Why don't you come play with me instead?"
    elif texto == 1:
        bree_nvl "Guess where I am right now."
        bree_nvl "I'll give you a clue - I have my swimsuit on and the water's just perfect!"
        bree_nvl "Come see if you can find me, yeah?"
    else:
        bree_nvl "I'm thinking of going shopping for some new outfits later."
        bree_nvl "And I was just wondering if you had any advice for what I should get?"
        bree_nvl "You like me in stuff that's skimpy and revealing, right?"
    return

label bree_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        bree_nvl "My eyes are tired - I need to quit playing this game!"
        bree_nvl "Maybe I'll play with myself instead..."
        bree_nvl "Or I could play on your joystick instead?"
    elif texto == 1:
        bree_nvl "Hey, I'm taking a dip in the pool out back."
        bree_nvl "You want to come see what I'm not wearing right now?"
        bree_nvl "Maybe even play a fun game under the water?"
    else:
        bree_nvl "I watched a scary movie and now I'm freaked out!"
        bree_nvl "Can I sleep with you in your bed tonight?"
        bree_nvl "As a reward, you can do whatever you want to me, okay?"
    return

label bree_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, [bree.name], did you download that new DLC yet?"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "I'm itching to play it!"
        bree_nvl "Of course I did!"
        bree_nvl "I'm playing it right now!"
        if persistent.difficulty >= 0:
            if bree.love <= 50:
                $ bree.love += 1
        else:
            $ bree.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, [bree.name], could you check the bathroom out?"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "I think somebody blocked the toilet!"
        bree_nvl "Eww...gross!"
        bree_nvl "And don't think I don't know it was you!"
        if persistent.difficulty >= 0:
            if bree.love <= 50:
                $ bree.love += 1
        else:
            $ bree.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, [bree.name], wanna go for a dip in the pool?"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "I'll be home soon and I feel like a swim."
        bree_nvl "You do you, but I'll pass."
        bree_nvl "I think it's gonna rain anyway."
        if persistent.difficulty >= 0:
            if bree.love <= 50:
                $ bree.love += 1
        else:
            $ bree.love += 1
        $ hero.fun += 0.2
    return

label bree_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I think someone should make a game where you're one of the characters, [bree.name]."
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "I'd play it all the time!"
        if (bree.love <= 80 or bree.sexperience == 0) and not hero.charm >= 30:
            bree_nvl "Ah, go play with yourself instead!"
            $ bree.love -= 1
        elif bree.sexperience == 0 or (bree.love <= 100 and not hero.charm >= 50):
            bree_nvl "So you want to play with me, huh?"
            bree_nvl "I think I like the sound of that!"
            $ bree.love += 1
        else:
            bree_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if bree.love <= 100:
                    $ bree.love += 1
            else:
                $ bree.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "What are you wearing, [bree.name]?"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "You mind telling me - in great detail?"
        if (bree.love <= 80 or bree.sexperience == 0) and not hero.charm >= 30:
            bree_nvl "Eww...stop being such a perv!"
            bree_nvl "You can see what I'm wearing anytime - we DO live in the same house!"
            $ bree.love -= 1
        elif bree.sexperience == 0 or (bree.love <= 100 and not hero.charm >= 50):
            bree_nvl "I'm still in my pyjamas right now."
            bree_nvl "Well, I mean my panties and a T-shirt - that's all!"
            $ bree.love += 1
        else:
            bree_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if bree.love <= 100:
                    $ bree.love += 1
            else:
                $ bree.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "We need to get some time together, [bree.name]."
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "Time away from the house so we can really be alone!"
        if (bree.love <= 80 or bree.sexperience == 0) and not hero.charm >= 30:
            bree_nvl "I think I'd prefer that you were on your own!"
            bree_nvl "Somewhere far away from me too!"
            $ bree.love -= 1
        elif bree.sexperience == 0 or (bree.love <= 100 and not hero.charm >= 50):
            bree_nvl "I know just what you mean!"
            bree_nvl "Somewhere Sasha can't walk in on us!"
            $ bree.love += 1
        else:
            bree_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if bree.love <= 100:
                    $ bree.love += 1
            else:
                $ bree.love += 1
        $ hero.fun += 0.3
    return

label bree_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, [bree.name], I'm feeling pretty horny!"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "What are you doing right now?"
        if bree.love <= 100 and not hero.charm >= 40:
            bree_nvl "Eww...why'd you text me when you're horny?"
            bree_nvl "Can't you take care of it yourself?"
            $ bree.love -= 2
        elif bree.sexperience < 2 or bree.love <= 150:
            bree_nvl "I'm grinding on a JRPG."
            bree_nvl "But I'd rather be grinding on your cock!"
            $ bree.love += 2
        else:
            bree_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if bree.love <= 150:
                    $ bree.love += 2
                elif bree.love <= 175:
                    $ bree.love += 1
            else:
                $ bree.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I'm remembering the last time you took a dip in the pool, [bree.name]."
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "And the memory of you in your swimsuit...it's making me hard!"
        if bree.love <= 100 and not hero.charm >= 40:
            bree_nvl "All the more reason not to swim when you're around!"
            $ bree.love -= 2
        elif bree.sexperience < 2 or bree.love <= 150:
            bree_nvl "Well, I'm touching myself right now, between the legs!"
            bree_nvl "Doesn't that make you even harder?"
            $ bree.love += 2
        else:
            bree_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if bree.love <= 150:
                    $ bree.love += 2
                elif bree.love <= 175:
                    $ bree.love += 1
            else:
                $ bree.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "I never had a blowjob like the last one you gave me, [bree.name]!"
        if bree.activity_name == "sleep" and bree.love < 70:
            bree_nvl "Leave me alone, I was asleep..."
            $ bree.love -= 2
            return
        mchero_nvl "You didn't just blow me, you blew my mind too!"
        if bree.love <= 100 and not hero.charm >= 40:
            bree_nvl "Yeah, well...it was kind of boring for me, you know?"
            $ bree.love -= 2
        elif bree.sexperience < 2 or bree.love <= 150:
            bree_nvl "Mmm...stop reminding me!"
            bree_nvl "You're making me want to suck it all over again!"
            $ bree.love += 2
        else:
            bree_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if bree.love <= 150:
                    $ bree.love += 2
                elif bree.love <= 175:
                    $ bree.love += 1
            else:
                $ bree.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
