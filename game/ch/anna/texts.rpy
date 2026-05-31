label anna_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        anna_nvl "Hey, what are you thinking about right now?"
        anna_nvl "Because all I got on my mind is you!"
        anna_nvl "I hope you're thinking about me too!"
    elif texto == 1:
        anna_nvl "You sounded great at practice the other day."
        anna_nvl "The band's so much better since you joined!"
        anna_nvl "We sound so badass!"
    else:
        anna_nvl "When are you gonna be free to hang out?"
        anna_nvl "It feels like forever since we spent time together!"
        anna_nvl "I really miss you!"
    return

label anna_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        anna_nvl "Aw...I'm so bored right now!"
        anna_nvl "I've got nothing to do that's fun!"
        anna_nvl "Can you think of anything I could do to have fun?"
    elif texto == 1:
        anna_nvl "Ooh...my bra's so tight - it's squeezing me!"
        anna_nvl "Seriously, I think my tits are going to pop out of it!"
        anna_nvl "Can you imagine how that would look?!?"
    else:
        anna_nvl "I love watching you play the guitar!"
        anna_nvl "It's silly, but sometimes I kinda get jealous..."
        anna_nvl "Like I wanna be your guitar and have you play me!"
    return

label anna_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        anna_nvl "Ooh...I've got an itchy butt!"
        anna_nvl "You want to scratch it for me?"
        anna_nvl "A hard cock up there should hit the spot!"
    elif texto == 1:
        anna_nvl "Hmm...I wonder what would look good on my chest?"
        anna_nvl "Oh yeah, I know!"
        anna_nvl "You shooting your load over it!"
    else:
        anna_nvl "Hey, I saw you sniffing my drum-stool after band practice!"
        anna_nvl "That's SO not out of order!"
        anna_nvl "You should be licking out my pussy instead!"
    return

label anna_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Anna, did you hear the new Metallikea album yet?"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        anna_nvl "Of course I did - I played it a hundred times already!"
        anna_nvl "It's metalicious!"
        if persistent.difficulty >= 0:
            if anna.love <= 50:
                $ anna.love += 1
        else:
            $ anna.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Anna, you want to go for a beer?"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        anna_nvl "Urgh...can't right now."
        anna_nvl "I have to study for a test!"
        if persistent.difficulty >= 0:
            if anna.love <= 50:
                $ anna.love += 1
        else:
            $ anna.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Anna, I found a really cool retro metal T-shirt."
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "Remind me how big your tits are?"
        anna_nvl "Hey - my chest isn't that big!"
        if persistent.difficulty >= 0:
            if anna.love <= 50:
                $ anna.love += 1
        else:
            $ anna.love += 1
        $ hero.fun += 0.2
    return

label anna_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Anna, what are you wearing right now?"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "I bet it's something sexy, right?"
        if (anna.love <= 80 or anna.sexperience == 0) and not hero.charm >= 30:
            anna_nvl "Hey, that's creepy!"
            anna_nvl "I don't call you up and ask questions like that!"
            $ anna.love -= 1
        elif anna.sexperience == 0 or (anna.love <= 100 and not hero.charm >= 50):
            anna_nvl "Oh yeah - and it's skimpy too!"
            anna_nvl "It looks so it makes me want to shake everything up and down!"
            $ anna.love += 1
        else:
            anna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if anna.love <= 100:
                    $ anna.love += 1
            else:
                $ anna.love += 1
        $ hero.fun += 0.3
    elif text_id == 1:
        mchero_nvl "I just can't get your ass out of my mind, Anna!"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "It's so round, so pert, so perfect!"
        if (anna.love <= 80 or anna.sexperience == 0) and not hero.charm >= 30:
            anna_nvl "There ARE other parts of my body, you know?!?"
            $ anna.love -= 1
        elif anna.sexperience == 0 or (anna.love <= 100 and not hero.charm >= 50):
            anna_nvl "He he...I'll keep it safe until you see it again!"
            $ anna.love += 1
        else:
            anna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if anna.love <= 100:
                    $ anna.love += 1
            else:
                $ anna.love += 1
        $ hero.fun += 0.3
    else:
        mchero_nvl "I want to take you to a metal club, Anna."
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "Somewhere we can dance together all night."
        if (anna.love <= 80 or anna.sexperience == 0) and not hero.charm >= 30:
            anna_nvl "Oh no - I always get squished in the mosh-pit!"
            $ anna.love -= 1
        elif anna.sexperience == 0 or (anna.love <= 100 and not hero.charm >= 50):
            anna_nvl "Oooh...I want to get hot and sweaty with you!"
            $ anna.love += 1
        else:
            anna_nvl "You make me blush :$"
            if persistent.difficulty >= 0:
                if anna.love <= 100:
                    $ anna.love += 1
            else:
                $ anna.love += 1
        $ hero.fun += 0.3
    return

label anna_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "I can't stop thinking about your ass, Anna!"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "How good it looks, how it moves..."
        mchero_nvl "And how good it'd feel to stick my cock in it!"
        if anna.love <= 100 and not hero.charm >= 40:
            anna_nvl "Eww...what is it with you and my ass?!?"
            $ anna.love -= 2
        elif anna.sexperience < 2 or anna.love <= 150:
            anna_nvl "You think it'd feel good?"
            anna_nvl "You've got no idea how much better it'd feel for me!"
            $ anna.love += 2
        else:
            anna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if anna.love <= 150:
                    $ anna.love += 2
                elif anna.love <= 175:
                    $ anna.love += 1
            else:
                $ anna.love += 2
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "I got such a need for you right now, Anna!"
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "My cock's hard just thinking about you!"
        if anna.love <= 100 and not hero.charm >= 40:
            anna_nvl "Then take a cold shower!"
            $ anna.love -= 2
        elif anna.sexperience < 2 or anna.love <= 150:
            anna_nvl "Stop it...you're making my pussy wet!"
            anna_nvl "Mmm...I'm gonna have to start touching myself!"
            $ anna.love += 2
        else:
            anna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if anna.love <= 150:
                    $ anna.love += 2
                elif anna.love <= 175:
                    $ anna.love += 1
            else:
                $ anna.love += 2
        $ hero.fun += 0.2
    else:
        mchero_nvl "Squeeze your tits and tell me how it feels, Anna."
        if anna.activity_name == "sleep" and anna.love < 70:
            anna_nvl "Leave me alone, I was asleep..."
            $ anna.love -= 2
            return
        mchero_nvl "I want to imagine I'm playing with them right now!"
        if anna.love <= 100 and not hero.charm >= 40:
            anna_nvl "Hey - I'm not playing with myself to get you off!"
            $ anna.love -= 2
        elif anna.sexperience < 2 or anna.love <= 150:
            anna_nvl "Ooh...they're so soft, nice and heavy too!"
            anna_nvl "And my nipples are getting so hard!"
            $ anna.love += 2
        else:
            anna_nvl "You make me so wet :$"
            if persistent.difficulty >= 0:
                if anna.love <= 150:
                    $ anna.love += 2
                elif anna.love <= 175:
                    $ anna.love += 1
            else:
                $ anna.love += 2
        $ hero.fun += 0.2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
