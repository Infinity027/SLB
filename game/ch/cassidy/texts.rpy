label cassidy_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cassidy_nvl "Hey, when are you going to answer my messages?!?"
        cassidy_nvl "I'm not, like, desperate to hear from you..."
        cassidy_nvl "It's just polite to answer them, you know?"
    elif texto == 1:
        cassidy_nvl "I had a great time on our date the other night."
        cassidy_nvl "You made me feel really special!"
        cassidy_nvl "I can't wait to see you again too!"
    else:
        cassidy_nvl "Do you think about me a lot?"
        cassidy_nvl "Because it's weird - I think about you all the time!"
        cassidy_nvl "And I don't know why..."
    return

label cassidy_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cassidy_nvl "Hey, I'm picking an outfit for our next date."
        cassidy_nvl "And I was thinking of covering up for a change..."
        cassidy_nvl "Just kidding - I'm going to show off more flesh then last time!"
    elif texto == 1:
        cassidy_nvl "I want to get the biggest kick I can when I see you next."
        cassidy_nvl "So I'm thinking of the baddest things we can get up to."
        cassidy_nvl "Things that's make my parents die if they ever found out!"
    else:
        cassidy_nvl "I miss you - when can we get together, huh?"
        cassidy_nvl "I want to feel your hands all over me."
        cassidy_nvl "And I want you inside of me too!"
    return

label cassidy_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        cassidy_nvl "Hey, can you come over here?"
        cassidy_nvl "I just had THE best idea ever!"
        cassidy_nvl "Let's do it on my Mommy and Daddy's bed!"
    elif texto == 1:
        cassidy_nvl "Please put your cock in me again!"
        cassidy_nvl "It feels so good when we fuck!"
        cassidy_nvl "You make me feel like a real woman!"
    else:
        cassidy_nvl "Being all on my own sucks!"
        cassidy_nvl "I'm having to use one of my vibrators right now!"
        cassidy_nvl "But it's not as good as your cock!"
    return

label cassidy_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Cassidy, you want to meet up and hang out?"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        cassidy_nvl "I do, I really do!"
        cassidy_nvl "But I have to study - boo!"
        if persistent.difficulty >= 0:
            if cassidy.love <= 50:
                $ cassidy.love += 1
        else:
            $ cassidy.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Cassidy, what are you doing right now?"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        cassidy_nvl "Not much...just sitting around, thinking about this guy I know..."
        cassidy_nvl "Can you guess what his name is?"
        if persistent.difficulty >= 0:
            if cassidy.love <= 50:
                $ cassidy.love += 1
        else:
            $ cassidy.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Cassidy, I'm bored."
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "Tell me a joke or something - make me laugh."
        cassidy_nvl "No way!"
        cassidy_nvl "What do you think I am - a comedian?"
        if persistent.difficulty >= 0:
            if cassidy.love <= 50:
                $ cassidy.love += 1
        else:
            $ cassidy.love += 1
        $ hero.fun += 0.2
    return

label cassidy_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Cassidy, what are you wearing right now?"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "I'm thinking that it's something sexy, yeah?"
        if (cassidy.love <= 80 or cassidy.sexperience == 0) and not hero.charm >= 30:
            cassidy_nvl "Eww...that's SO creepy!"
            cassidy_nvl "I'm not telling you that!"
            $ cassidy.love -= 1
        elif cassidy.sexperience == 0 or (cassidy.love <= 100 and not hero.charm >= 50):
            cassidy_nvl "You're SO bad!"
            cassidy_nvl "I was just in the pool - so all I have on is my bikini!"
            $ cassidy.love += 1
        else:
            cassidy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 100:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "Can you meet me somewhere, Cassidy?"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "I'm desperate to get my hands on you!"
        if (cassidy.love <= 80 or cassidy.sexperience == 0) and not hero.charm >= 30:
            cassidy_nvl "Huh...and they say romance is dead!"
            cassidy_nvl "Why not just say you want to hump my leg like a dog?"
            $ cassidy.love -= 1
        elif cassidy.sexperience == 0 or (cassidy.love <= 100 and not hero.charm >= 50):
            cassidy_nvl "I can feel them all over me already!"
            cassidy_nvl "I'll sneak out as soon as I can!"
            $ cassidy.love += 1
        else:
            cassidy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 100:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I need to see you again soon, Cassidy."
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "You're like a drug that I can't get enough of!"
        if (cassidy.love <= 80 or cassidy.sexperience == 0) and not hero.charm >= 30:
            cassidy_nvl "Ah...that's a mean thing to say!"
            cassidy_nvl "Drugs are - and I'm a good girl!"
            $ cassidy.love -= 1
        elif cassidy.sexperience == 0 or (cassidy.love <= 100 and not hero.charm >= 50):
            cassidy_nvl "That's me - expensive and totally addictive!"
            $ cassidy.love += 1
        else:
            cassidy_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 100:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 1
        $ hero.fun += 0.3
    return

label cassidy_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Cassidy, I can't keep my mind on anything else."
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "All I can think about is getting my cock inside of you!"
        if cassidy.love <= 100 and not hero.charm >= 40:
            cassidy_nvl "That's SO crude!"
            cassidy_nvl "Can't you be nicer to me?"
            $ cassidy.love -= 2
        elif cassidy.sexperience < 2 or cassidy.love <= 150:
            cassidy_nvl "Oh man...you've got a one-track mind!"
            cassidy_nvl "But you've got my pussy all wet - so maybe I do too!"
            $ cassidy.love += 2
        else:
            cassidy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 150:
                    $ cassidy.love += 2
                elif cassidy.love <= 175:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Cassidy, when can you get over here?"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "I need you to suck my cock as soon as you can!"
        if cassidy.love <= 100 and not hero.charm >= 40:
            cassidy_nvl "Erm...rude!"
            cassidy_nvl "That means you don't get oral from me!"
            $ cassidy.love -= 2
        elif cassidy.sexperience < 2 or cassidy.love <= 150:
            cassidy_nvl "Why didn't you just say that in the first place!"
            cassidy_nvl "I'll be over there as soon as I can."
            cassidy_nvl "So you'd better be nice and hard!"
            $ cassidy.love += 2
        else:
            cassidy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 150:
                    $ cassidy.love += 2
                elif cassidy.love <= 175:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You're such a little bitch, Cassidy!"
        if cassidy.activity_name == "sleep" and cassidy.love < 70:
            cassidy_nvl "Leave me alone, I was asleep..."
            $ cassidy.love -= 2
            return
        mchero_nvl "I should put you over my knee and spank you hard!"
        if cassidy.love <= 100 and not hero.charm >= 40:
            cassidy_nvl "Huh...daddy never spanked me, not once!"
            cassidy_nvl "So you think I'm going to let you do that to me?!?"
            $ cassidy.love -= 2
        elif cassidy.sexperience < 2 or cassidy.love <= 150:
            cassidy_nvl "Oh...you want to punish me?!?"
            cassidy_nvl "I'll have to be extra naughty so you do it extra hard!"
            $ cassidy.love += 2
        else:
            cassidy_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if cassidy.love <= 150:
                    $ cassidy.love += 2
                elif cassidy.love <= 175:
                    $ cassidy.love += 1
            else:
                $ cassidy.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
