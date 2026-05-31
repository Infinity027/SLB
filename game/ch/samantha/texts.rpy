label samantha_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0 and "samantha_event_A02" in DONE:
        samantha_nvl "Hey there, just a message to say your cupcake's thinking about you!"
        samantha_nvl "And, well...I just hope that..."
        samantha_nvl "I hope you're thinking of me too?"
    elif texto == 1 and samantha.flags.nodate == False:
        samantha_nvl "That date was so much fun!"
        samantha_nvl "You have to let me pick where we go next time though."
        samantha_nvl "I have some great ideas of my own, I promise you!"
    else:
        samantha_nvl "Hey, are you doing anything right now?"
        samantha_nvl "I just found out I have a clear diary."
        samantha_nvl "So we can meet up and do something, if you like?"
    return

label samantha_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ texto = randint(0, 2)
    if texto == 0 and samantha.flags.knows_ryancheats:
        samantha_nvl "You doing anything right now?"
        samantha_nvl "Because I'm not."
        samantha_nvl "So maybe we could do something fun together - if you know what I mean?"
    elif texto == 1 and samantha.flags.knows_ryancheats:
        samantha_nvl "Oh, there's always a part of me that wants to dress smart."
        samantha_nvl "But then I see the way you look at me when I wear less..."
        samantha_nvl "And I like it when you look at me like that!"
    elif texto == 2 and samantha.flags.knows_ryancheats:
        samantha_nvl "Just wanted to say that I'm still glad I dumped Ryan for you."
        samantha_nvl "It's like upgrading to a better model!"
        samantha_nvl "And with you, the ride's so much smoother too!"
    else:
        samantha_nvl "I wanna hang out again with you soon. Text me when you get a chance!"
    return

label samantha_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0 and samantha.flags.knows_ryancheats:
        samantha_nvl "Come over and spend the night with me, yeah?"
        samantha_nvl "I got freaked out being on my own!"
        samantha_nvl "If you do, I'll let you do whatever you like to me..."
    elif texto == 1 and samantha.flags.knows_ryancheats:
        samantha_nvl "You know, I still have my wedding dress in the closet."
        samantha_nvl "I was going to throw it away, or maybe burn it."
        samantha_nvl "But I don't supposed you want to fuck me in it first?"
    else:
        samantha_nvl "What is it with your cock?"
        samantha_nvl "Now I've had it in me, I want it all the damn time!"
        samantha_nvl "Just thinking about it is getting me wet!"
    return

label samantha_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Hey, Cupcake, you want to meet me for a chat, maybe a beer too?"
        else:
            mchero_nvl "Hey, Sam, you want to meet me for a chat, maybe a beer too?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        samantha_nvl "Sorry, I can't right now!"
        samantha_nvl "I'm still at work."
        if persistent.difficulty >= 0:
            if samantha.love <= 50:
                $ samantha.love += 1
        else:
            $ samantha.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Hey, Cupcake, you remember living at my place, right?"
        else:
            mchero_nvl "Hey, Sam, you remember living at my place, right?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "Do you remember where the key to the shed is?"
        samantha_nvl "Are you serious?!?"
        samantha_nvl "I stopped having to give a shit the moment I moved out!"
        if persistent.difficulty >= 0:
            if samantha.love <= 50:
                $ samantha.love += 1
        else:
            $ samantha.love += 1
        $ hero.fun += 0.2
    else:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Hey, Cupcake, what are you doing?"
        else:
            mchero_nvl "Hey, Sam, what are you doing?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        samantha_nvl "Oh, the usual - just waiting around for you to message me at random."
        samantha_nvl "I'm being sarcastic, just for the record."
        if persistent.difficulty >= 0:
            if samantha.love <= 50:
                $ samantha.love += 1
        else:
            $ samantha.love += 1
        $ hero.fun += 0.2
    return

label samantha_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Mmm...when am I going to get to taste my cupcake again?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Because I want to lick your frosting right off, Cupcake!"
        else:
            mchero_nvl "Because I want to lick your frosting right off, Sam!"
        if (samantha.love <= 80 or samantha.sexperience == 0) and not hero.charm >= 30:
            samantha_nvl "Ew...that sounded so creepy!"
            samantha_nvl "It was a definite turn-off."
            $ samantha.love -= 1
        elif samantha.sexperience == 0 or (samantha.love <= 100 and not hero.charm >= 50):
            samantha_nvl "So, you got a sweet tooth for me, huh?"
            samantha_nvl "You better be able to handle the sugar rush!"
            $ samantha.love += 1
        else:
            samantha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 100:
                    $ samantha.love += 1
            else:
                $ samantha.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Hey, Cupcake, tell me what you're wearing?"
        else:
            mchero_nvl "Hey, Sam, tell me what you're wearing?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "It's something sexy, right?"
        if (samantha.love <= 80 or samantha.sexperience == 0) and not hero.charm >= 30:
            samantha_nvl "Clothes, okay - I'm wearing clothes!"
            samantha_nvl "How's that for an answer?"
            $ samantha.love -= 1
        elif samantha.sexperience == 0 or (samantha.love <= 100 and not hero.charm >= 50):
            samantha_nvl "You should be asking about what I'm wearing UNDER my clothes."
            samantha_nvl "That's where all the stuff is!"
            $ samantha.love += 1
        else:
            samantha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 100:
                    $ samantha.love += 1
            else:
                $ samantha.love += 1
        $ hero.fun += 0.3
    else:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "Cupcake, I can't think about anything but you!"
        else:
            mchero_nvl "Sam, I can't think about anything but you!"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "You're on my mind - day and night!"
        if (samantha.love <= 80 or samantha.sexperience == 0) and not hero.charm >= 30:
            samantha_nvl "Whoa...maybe back off a bit there?"
            samantha_nvl "I don't think I'm ready for you being that needy!"
            $ samantha.love -= 1
        elif samantha.sexperience == 0 or (samantha.love <= 100 and not hero.charm >= 50):
            samantha_nvl "I'm the same - I think about you all the time!"
            samantha_nvl "And about what I want you to do to me too..."
            $ samantha.love += 1
        else:
            samantha_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 100:
                    $ samantha.love += 1
            else:
                $ samantha.love += 1
        $ hero.fun += 0.3
    return

label samantha_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "I'm thinking about the last time we fucked, Cupcake."
        else:
            mchero_nvl "I'm thinking about the last time we fucked, Sam."
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "And the memory of being inside you..."
        mchero_nvl "It's making me so hard!"
        if samantha.love <= 100 and not hero.charm >= 40:
            samantha_nvl "Stop that now!"
            samantha_nvl "You couldn't have picked a worse time!"
            $ samantha.love -= 2
        elif samantha.sexperience < 2 or samantha.love <= 150:
            samantha_nvl "Oh...stop it!"
            samantha_nvl "You're making me want it again!"
            $ samantha.love += 2
        else:
            samantha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 150:
                    $ samantha.love += 2
                elif samantha.love <= 175:
                    $ samantha.love += 1
            else:
                $ samantha.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "I love knowing I have you and Ryan doesn't, Cupcake."
        else:
            mchero_nvl "I love knowing I have you and Ryan doesn't, Sam."
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "Every time we fuck, it's like we're sticking it to him!"
        if samantha.love <= 100 and not hero.charm >= 40:
            samantha_nvl "Is that all I am to you?"
            samantha_nvl "A chance to get back at Ryan?!?"
            $ samantha.love -= 2
        elif samantha.sexperience < 2 or samantha.love <= 150:
            samantha_nvl "Oh yeah...I know what you mean!"
            samantha_nvl "We have to fuck again - when can you get over here?"
            $ samantha.love += 2
        else:
            samantha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 150:
                    $ samantha.love += 2
                elif samantha.love <= 175:
                    $ samantha.love += 1
            else:
                $ samantha.love += 2
        $ hero.fun += 0.2
    else:
        if samantha.flags.nickname == "cupcake":
            mchero_nvl "What are you wearing right now, Cupcake?"
        else:
            mchero_nvl "What are you wearing right now, Sam?"
        if samantha.activity_name == "sleep" and samantha.love < 70:
            samantha_nvl "Leave me alone, I was asleep..."
            $ samantha.love -= 2
            return
        mchero_nvl "I'm stroking my cock and thinking about you!"
        if samantha.love <= 100 and not hero.charm >= 40:
            samantha_nvl "I'm in the kitchen right now."
            samantha_nvl "So what do you think I have on?"
            samantha_nvl "A damn bikini?!?"
            $ samantha.love -= 2
        elif samantha.sexperience < 2 or samantha.love <= 150:
            samantha_nvl "I'm baking right now, so I have my apron on."
            samantha_nvl "Well...that and nothing else!"
            $ samantha.love += 2
        else:
            samantha_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if samantha.love <= 150:
                    $ samantha.love += 2
                elif samantha.love <= 175:
                    $ samantha.love += 1
            else:
                $ samantha.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
