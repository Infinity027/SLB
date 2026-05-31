label kleio_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kleio_nvl "Hey, Loverboy - you doing anything right now?"
        kleio_nvl "I got an idea for a great song - heavy as fuck!"
        kleio_nvl "And you've got to hear it!"
    elif texto == 1:
        kleio_nvl "Getting better with that guitar, Loverboy!"
        kleio_nvl "The band's finally starting to sound how I wanted it to!"
        kleio_nvl "Maybe you're not a total screw-up!"
    else:
        kleio_nvl "Hey, Loverboy - are you thinking about me?"
        kleio_nvl "Because I just wanted to know, yeah?"
        kleio_nvl "Not because I'm thinking of you or anything..."
    return

label kleio_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kleio_nvl "Hey, I'm thinking of getting a new tattoo."
        kleio_nvl "There's room on my ass or my tits, okay?"
        kleio_nvl "Where'd you think I should have it?"
    elif texto == 1:
        kleio_nvl "You like the look of me in my shorts and stockings, yeah?"
        kleio_nvl "You want me to tell you how they feel, Loverboy?"
        kleio_nvl "Yeah, you'd like that, wouldn't you?"
    else:
        kleio_nvl "Ah, I don't know what I want to do with myself, Loverboy!"
        kleio_nvl "Half of me wants to pluck at my bass."
        kleio_nvl "The other half feels like plucking my pussy!"
    return

label kleio_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        kleio_nvl "Mmm...my pussy's go hungry it's actually growling!"
        kleio_nvl "You go something to feed it, Loverboy?"
        kleio_nvl "Maybe slip something in there that'll fill it up?"
    elif texto == 1:
        kleio_nvl "I don't think you've seen ALL of my tattoos, Loverboy."
        kleio_nvl "Not the ones below my waist."
        kleio_nvl "So I'm gonna strip off and you can take you time reading them."
        kleio_nvl "And while you're down there - eat my pussy, yeah?"
    else:
        kleio_nvl "Hang around after we finish practice this week, Loverboy."
        kleio_nvl "You remember Sasha splashed out on that new speaker?"
        kleio_nvl "Yeah, well, we're gonna splash on it ourselves!"
        kleio_nvl "By which, of course, I mean you're going to fuck me over it!"
    return

label kleio_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Kleio, you heard the new Feckless album?"
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "It's all I've been listening to since I got it!"
        kleio_nvl "It's not bad."
        kleio_nvl "But it sucks compared to their older stuff."
        if persistent.difficulty >= 0:
            if kleio.love <= 50:
                $ kleio.love += 1
        else:
            $ kleio.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Kleio, you want to meet me down the pub?"
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        kleio_nvl "I'd like to, Loverboy, but I can't."
        kleio_nvl "I'm changing the strings on my bass."
        if persistent.difficulty >= 0:
            if kleio.love <= 50:
                $ kleio.love += 1
        else:
            $ kleio.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Kleio, you know all about tattoos."
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "You think I should get one?"
        kleio_nvl "Yeah, a really big one."
        kleio_nvl "All over your face, to cover up your ugly mug!"
        if persistent.difficulty >= 0:
            if kleio.love <= 50:
                $ kleio.love += 1
        else:
            $ kleio.love += 1
        $ hero.fun += 0.2
    return

label kleio_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Kleio, what are you wearing right now?"
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "Please tell me it's something sexy!"
        if (kleio.love <= 80 or kleio.sexperience == 0) and not hero.charm >= 30:
            kleio_nvl "What am I, dial-a-slut?!?"
            kleio_nvl "Fuck off!"
            $ kleio.love -= 1
        elif kleio.sexperience == 0 or (kleio.love <= 100 and not hero.charm >= 50):
            kleio_nvl "You caught me getting out of the shower, Loverboy!"
            kleio_nvl "So all I have on is my tats and a smile!"
            $ kleio.love += 1
        else:
            kleio_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 100:
                    $ kleio.love += 1
            else:
                $ kleio.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I love the way you play the bass, Kleio."
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "You're so passionate - it's like you're making love to the thing!"
        if (kleio.love <= 80 or kleio.sexperience == 0) and not hero.charm >= 30:
            kleio_nvl "It's not like that at all!"
            kleio_nvl "I'm an artist, my work is pure!"
            $ kleio.love -= 1
        elif kleio.sexperience == 0 or (kleio.love <= 100 and not hero.charm >= 50):
            kleio_nvl "Yeah, I know - it gets me pretty hot!"
            $ kleio.love += 1
        else:
            kleio_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 100:
                    $ kleio.love += 1
            else:
                $ kleio.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "You talk and act so tough, Kleio."
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "Sometimes I think I should arm-wrestle you!"
        if (kleio.love <= 80 or kleio.sexperience == 0) and not hero.charm >= 30:
            kleio_nvl "Try it some time - see how badly I beat your sorry ass!"
            $ kleio.love -= 1
        elif kleio.sexperience == 0 or (kleio.love <= 100 and not hero.charm >= 50):
            kleio_nvl "Yeah, but only because you think it'd lead to something else!"
            $ kleio.love += 1
        else:
            kleio_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 100:
                    $ kleio.love += 1
            else:
                $ kleio.love += 1
        $ hero.fun += 0.3
    return

label kleio_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I love watching you play, Kleio."
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "It's like you're fucking the bass or it's fucking you."
        mchero_nvl "I just can't decide which!"
        if kleio.love <= 100 and not hero.charm >= 40:
            kleio_nvl "Geez...you gotta turn everything into a wank fantasy!"
            $ kleio.love -= 2
        elif kleio.sexperience < 2 or kleio.love <= 150:
            kleio_nvl "Try playing with me while you do me."
            kleio_nvl "I kinda like the idea of being played like my bass!"
            $ kleio.love += 2
        else:
            kleio_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 150:
                    $ kleio.love += 2
                elif kleio.love <= 175:
                    $ kleio.love += 1
            else:
                $ kleio.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Did you get another tattoo, Kleio?"
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "I thought I saw new one last time we fucked?"
        if kleio.love <= 100 and not hero.charm >= 40:
            kleio_nvl "Hey - you should be one hundred percent focused on the job!"
            kleio_nvl "I'm not something you can read when you're bored!"
            $ kleio.love -= 2
        elif kleio.sexperience < 2 or kleio.love <= 150:
            kleio_nvl "What if I did, Loverboy?"
            kleio_nvl "Maybe I should get one that says 'fuck me harder'!"
            $ kleio.love += 2
        else:
            kleio_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 150:
                    $ kleio.love += 2
                elif kleio.love <= 175:
                    $ kleio.love += 1
            else:
                $ kleio.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "You've got a dirty mouth, Kleio."
        if kleio.activity_name == "sleep" and kleio.love < 70:
            kleio_nvl "Leave me alone, I was asleep..."
            $ kleio.love -= 2
            return
        mchero_nvl "But I love putting my cock in it!"
        if kleio.love <= 100 and not hero.charm >= 40:
            kleio_nvl "You want to be careful I don't bite, Loverboy!"
            $ kleio.love -= 2
        elif kleio.sexperience < 2 or kleio.love <= 150:
            kleio_nvl "Filthy lips do naughty tricks!"
            $ kleio.love += 2
        else:
            kleio_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if kleio.love <= 150:
                    $ kleio.love += 2
                elif kleio.love <= 175:
                    $ kleio.love += 1
            else:
                $ kleio.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
