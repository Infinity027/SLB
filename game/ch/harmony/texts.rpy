label harmony_friendly_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        harmony_nvl "I normally think about Jesus or the Holy Bible."
        harmony_nvl "But more and I more I end up thinking about you!"
        harmony_nvl "Oh...I hope that's not a sin!"
    elif texto == 1:
        harmony_nvl "I had a wonderful time on our last date."
        harmony_nvl "You always seem to choose something fun!"
        harmony_nvl "I just don't know how you do it."
    else:
        harmony_nvl "Do you have anything to confess?"
        harmony_nvl "Because I'm always here to listen."
        harmony_nvl "And I might have some things to confess to you too..."
    return

label harmony_flirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        harmony_nvl "Hey, are you doing anything right now?"
        harmony_nvl "Because I have some sins I want to confess to you."
        harmony_nvl "And I need to be on my knees to do it too..."
    elif texto == 1:
        harmony_nvl "I'm thinking of getting myself a nun's habit."
        harmony_nvl "I've always kind of wanted one, you know?"
        harmony_nvl "I think one in black rubber would suit me best."
    else:
        harmony_nvl "Oh...I can't stop thinking about you!"
        harmony_nvl "It's like there's a demon inside of me!"
        harmony_nvl "And it wants you to join it in there too!"
    return

label harmony_dirty_texts:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("texto")
    $ texto = randint(0, 2)
    if texto == 0:
        harmony_nvl "Once I would have been on my knees every night, praying."
        harmony_nvl "But that was before I met you."
        harmony_nvl "Now I want to be on my knees every night, sucking your cock!"
    elif texto == 1:
        harmony_nvl "I'm playing with breasts right now."
        harmony_nvl "Squashing then together like cushions."
        harmony_nvl "And imagining your cock between them!"
    else:
        harmony_nvl "I don't give a fuck about getting into heaven anymore."
        harmony_nvl "For me, heaven is being naked, on my hands and knees."
        harmony_nvl "And with you thrusting your cock into me as hard as you can!"
    return

label harmony_friendly_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Harmony, how in the hell are you today?"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        harmony_nvl "You really shouldn't send me messages like that."
        harmony_nvl "It's naughty and blasphemous!"
        if persistent.difficulty >= 0:
            if harmony.love <= 50:
                $ harmony.love += 1
        else:
            $ harmony.love += 1
        $ hero.fun += 0.2
    elif text_id == 1:
        mchero_nvl "Hey, Harmony, you want to meet up and hang out?"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I'm dying or boredom over here!"
        harmony_nvl "I can't right now."
        harmony_nvl "I'm volunteering at the soup kitchen, remember?"
        if persistent.difficulty >= 0:
            if harmony.love <= 50:
                $ harmony.love += 1
        else:
            $ harmony.love += 1
        $ hero.fun += 0.2
    else:
        mchero_nvl "Hey, Harmony, I've got a great comic-book here."
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "You should totally read it too!"
        harmony_nvl "I don't have time right now."
        harmony_nvl "I'm re-reading the bible!"
        if persistent.difficulty >= 0:
            if harmony.love <= 50:
                $ harmony.love += 1
        else:
            $ harmony.love += 1
        $ hero.fun += 0.2
    return

label harmony_flirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Harmony, what are you wearing right now?"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I bet it's something sexy, right?"
        if harmony.purity >= VHP:
            harmony_nvl "Oh, you beast!"
        elif harmony.purity >= HP:
            harmony_nvl "Oh, you beast!"
        elif harmony.purity < VLP:
            harmony_nvl "Oh, I have clothes on - but I'm not wearing any underwear!"
            $ harmony.purity -= 1
        elif harmony.purity < LP:
            harmony_nvl "Oh, I have clothes on - but I'm not wearing any underwear!"
        else:
            harmony_nvl "Stop it - you're making me blush!"
        $ harmony.love += 1
    elif text_id == 1:
        mchero_nvl "I can't get you out of my head, Harmony!"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I want to touch you so badly!"
        if harmony.purity >= VHP:
            harmony_nvl "Oh dear - I think you've been possessed by a demon!"
        elif harmony.purity >= HP:
            harmony_nvl "Oh dear - I think you've been possessed by a demon!"
        elif harmony.purity < VLP:
            harmony_nvl "Oh, you can touch me all you like when see me next!"
            $ harmony.purity -= 1
        elif harmony.purity < LP:
            harmony_nvl "Oh, you can touch me all you like when see me next!"
        else:
            harmony_nvl "Hey - be nice, Mister!"
        $ harmony.love += 1
    else:
        mchero_nvl "You want to sneak out and grab some time together, Harmony?"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I've got a real need to hold you in my arms!"
        if harmony.purity >= VHP:
            harmony_nvl "You're not getting your hands on me, you animal!"
        elif harmony.purity >= HP:
            harmony_nvl "You're not getting your hands on me, you animal!"
        elif harmony.purity < VLP:
            harmony_nvl "I'll be along as soon as I can - and you'd better do more than just hold me!"
            $ harmony.purity -= 1
        elif harmony.purity < LP:
            harmony_nvl "I'll be along as soon as I can - and you'd better do more than just hold me!"
        else:
            harmony_nvl "I'll see if I can slip away - but you better behave yourself!"
        $ harmony.love += 1
    return

label harmony_dirty_texts_male:
    $ nvl_mode = "phone"
    nvl clear
    $ renpy.dynamic("text_id")
    $ text_id = randint(0, 2)
    if text_id == 0:
        mchero_nvl "Hey, Harmony, I've got something for you!"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "It's hard, long and it's straining my shorts!"
        if harmony.purity >= VHP:
            harmony_nvl "You filthy beast!"
            $ harmony.love -= 1
        elif harmony.purity >= HP:
            harmony_nvl "You filthy beast!"
            $ harmony.love -= 1
        elif harmony.purity < VLP:
            harmony_nvl "Ooh..."
            harmony_nvl "I've got somewhere soft and wet you can put it!"
            $ harmony.love += 1
        elif harmony.purity < LP:
            harmony_nvl "Ooh..."
            harmony_nvl "I've got somewhere soft and wet you can put it!"
            $ harmony.love += 1
        else:
            harmony_nvl "You should take your act on tour!"
            $ harmony.sub += 1
    elif text_id == 1:
        mchero_nvl "I can't stop thinking about your tits, Harmony!"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I just want to bury my head between them!"
        if harmony.purity >= VHP:
            harmony_nvl "Keep away from me, you animal!"
            $ harmony.love -= 1
        elif harmony.purity >= HP:
            harmony_nvl "Keep away from me, you animal!"
            $ harmony.love -= 1
        elif harmony.purity < VLP:
            harmony_nvl "You can put whatever you like between them!"
            $ harmony.love += 1
        elif harmony.purity < LP:
            harmony_nvl "You can put whatever you like between them!"
            $ harmony.love += 1
        else:
            harmony_nvl "Wow - how many girls can say they have THREE tits!"
            $ harmony.sub += 1
    else:
        mchero_nvl "Wow...you were really wearing that dress the other day, Harmony!"
        if harmony.activity_name == "sleep" and harmony.love < 70:
            harmony_nvl "Leave me alone, I was asleep..."
            $ harmony.love -= 2
            return
        mchero_nvl "I could see every inch of you - it was all on show!"
        mchero_nvl "When can I peel that thing off you and see you naked again?!?"
        if harmony.purity >= VHP:
            harmony_nvl "Oh dear...I think you've been possessed by the devil!"
            $ harmony.love -= 1
        elif harmony.purity >= HP:
            harmony_nvl "Oh dear...I think you've been possessed by the devil!"
            $ harmony.love -= 1
        elif harmony.purity < VLP:
            harmony_nvl "Whenever you like!"
            harmony_nvl "Just ask and you can have me..."
            $ harmony.love += 1
        elif harmony.purity < LP:
            harmony_nvl "Whenever you like!"
            harmony_nvl "Just ask and you can have me..."
            $ harmony.love += 1
        else:
            harmony_nvl "We'll just have to wait and see, won't we!"
            $ harmony.sub += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
