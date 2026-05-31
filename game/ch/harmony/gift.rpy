init python:
    Equip("crucifix", type="accessory", effects={"religious": 20, "innocent": 20, "charm": 5})
    Equip("bible", type="accessory", effects={"religious": 20, "innocent": 20, "charm": 5})

    Event(**{
    "name": "harmony_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "harmony",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label harmony_give_male:
    if "crucifix" not in hero.inventory:
        $ gift = "crucifix"
        "She hands me a small box."
        mike.say "Wow!\nThat crucifix is beautiful!"
        mike.say "Thank you so much."
    elif harmony.love >= 50 and "bible" not in hero.inventory:
        $ gift = "bible"
        "She hands me a book."
        mike.say "Oh a bible..."
        harmony.say "You're welcome [hero.name]."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label harmony_give_valentine_male:
    "Harmony walks hesitantly towards me."
    call harmony_greet from _call_harmony_greet_7
    show harmony
    harmony.say "Happy valentine's day [hero.name]..."
    "Harmony throws a box of chocolates towards me."
    mike.say "Thank you, Harmony."
    $ hero.gain_item("valentine_chocolates")
    return

label harmony_give_birthday_male:
    "Harmony walks towards me."
    call harmony_greet from _call_harmony_greet_8
    show harmony happy
    harmony.say "Happy birthday [hero.name]!"
    call harmony_give_male from _call_harmony_give_male
    return

label harmony_give_christmas_male:
    "Harmony walks towards me."
    call harmony_greet from _call_harmony_greet_9
    show harmony happy
    harmony.say "Merry Christmas [hero.name]."
    call harmony_give_male from _call_harmony_give_male_1
    return

label harmony_birthday_gift_male:
    show harmony
    if harmony.flags.birthdayknown:
        mike.say "Happy birthday Harmony."
        harmony.say "How sweet, you remembered my birthday!"
    else:
        harmony.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ harmony.flags.birthdayknown = True
    return

label harmony_gift_swimsuit_male:
    show harmony happy
    harmony.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if harmony.sub >= 60 and not harmony.purity >= 25:
        show harmony blush
        harmony.say "Thank you [hero.name]."
        $ harmony.flags.sexyswimsuit = True
    else:
        show harmony angry
        $ harmony.love -= 4
        harmony.say "Thanks but I can't wear this [hero.name], it's ungodly..."
        harmony.say "Even worse than being naked..."
        $ hero.cancel_activity()
    return

label harmony_gift_collar_male:
    "I like to think that I'm not one of those guys that doesn't get women, you know?"
    "Those assholes that think they know their girlfriends and actually don't have a clue."
    "So I try to listen out for all of those little hints that women are always dropping."
    "The ones that are so very easy for a guy to misinterpret as just something they say."
    "And yet are a woman's way of testing whether or not you listen to what they really tell you."
    "Sometimes I get it right, and sometimes I don't."
    "But right now, when it comes to Harmony, I think I've nailed it."
    "I've been getting a certain kind of vibe off of her recently."
    "Sensing that she's getting into a certain kind of thing."
    "And if I'm right, the gift that I have for her is just the thing."
    "Well...I hope I'm right!"
    "But she's already seen the box."
    "So there's no going back now..."
    show harmony happy
    harmony.say "Oh, [hero.name]."
    harmony.say "Is that something for me?"
    mike.say "Ah, yeah, Harmony."
    mike.say "I got you a little something."
    "She gives me a demure smile as she accepts the box."
    "One of those smiles that does things to me!"
    show harmony blush
    harmony.say "Aw, that's so sweet of you!"
    if not game.calendar.is_today(*harmony.birthday):
        harmony.say "You know it's not my birthday for ages, right?"
        mike.say "I know, Harmony."
        mike.say "But there's no law says I can't buy you a gift."
    harmony.say "Oh, its a..."
    harmony.say "A collar!"
    "Harmony holds up the red leather collar that was in the box."
    "It has a frill around the underside and 'Sinner' printed in bold lettering upon it."
    mike.say "Well, I already know what a bad girl you're turning into, Harmony."
    mike.say "This should let everyone else know it too!"
    if harmony.sub < 90 or harmony.purity > 15:
        "Harmony stares at me in silence."
        "As though she just doesn't know what to say."
        "I'm getting more worried with each second that passes."
        "And I swear that I can see tears already welling in the corner of her eyes too."
        show harmony angry
        harmony.say "You...you BEAST!"
        harmony.say "Is this really what you think of me?!?"
        "Before I can say as much as a word, she hurls the collar and box at me."
        with hpunch
        "They hit me square in the face, making me yelp in pain."
        mike.say "Ow..."
        mike.say "Hey, Harmony - what the hell?!?"
        hide harmony
        "But by the time my vision has cleared, it's too late."
        "All I can see of Harmony is her back as she hurries away."
        "And all that I can hear is the sound of her sobbing as it fades into the distance."
        "Maybe I'm not so good at listening to women as I thought..."
        $ harmony.love -= 20
        $ harmony.sub -= 10
        $ harmony.purity += 10
        $ hero.cancel_activity()
    else:
        "I see Harmony's eyes go wide with surprise."
        "But the fact that she's smiling too reassures me she's not horrified."
        "In fact, she seems to be over the moon with my gift."
        show harmony happy
        harmony.say "Oooh, a dog collar."
        harmony.say "That's SO naughty!"
        harmony.say "Does that mean I'm like your pet now, or something?"
        "The way Harmony looks at me as she says this..."
        "Well, let's just say it makes me go weak at the knees!"
        mike.say "Ah...yeah, Harmony."
        mike.say "If...if that's what you want?"
        show fx exclamation
        harmony.say "Yay!"
        harmony.say "Put it on, [hero.name] - quickly!"
        harmony.say "I want everyone to know that I'm your pet!"
        $ harmony.set_sex_slave()
        "I hurry to do as Harmony commands, despite the fact I'm supposed to be the one in charge!"
        hide harmony
        show harmony happy
        harmony.say "Mmm..."
        harmony.say "It's nice and tight - to remind me who's my master!"
        harmony.say "And to remind me that I have to be a good little girl for him too..."
        $ harmony.love += 2
        $ harmony.sub += 5
        $ harmony.purity -= 5
    return

label harmony_gift_sexy_dress_male:
    show harmony normal
    "I've been waiting to give Harmony the gift that I got her from the moment I walked out of the store."
    "And I'm so excited when she shows up to meet me that I almost hand it straight over the moment I see her."
    "But thanks to some unknown reserve of willpower, I manage to hang on in there and greet her normally."
    "Well, as normally as I can pull off under the circumstances..."
    mike.say "Hey, Harmony..."
    mike.say "I'm so glad you could make it!"
    mike.say "You look amazing, by the way!"
    "Harmony takes a step back at this and eyes me with evident suspicion."
    show harmony mean
    "Then she cocks her head on one side and raises an eyebrow."
    if 'religious' in harmony.traits:
        harmony.say "Hmm..."
        harmony.say "What have I told you about making lascivious comments in public, [hero.name]?"
    elif 'slutty' in harmony.traits:
        harmony.say "Ah-hah!"
        harmony.say "Classic diversionary tactics - which usually means a guy wants something!"
    else:
        harmony.say "Oh-oh..."
        harmony.say "Blurting out compliments and looking shifty, are we?"
    show harmony normal
    harmony.say "So come on, [hero.name]..."
    harmony.say "What are you up to?"
    "I open my mouth, thinking to make up some kind of excuse and get out of it."
    "But then I realise - what's the point of wasting my breath?"
    "I wanted an excuse to give Harmony the dress before she spoke up."
    "So why not take advantage of the one she's handing to me now?"
    mike.say "Okay, Harmony..."
    mike.say "You got me, bang to rights!"
    mike.say "Here you go."
    "As soon as I hand over the box, Harmony's expression changes."
    "All trace of suspicion is gone, and she looks delighted with me."
    harmony.say "Oh, [hero.name]..."
    show harmony happy
    harmony.say "You bought me a gift?"
    harmony.say "You really shouldn't have!"
    mike.say "Yeah, yeah...whatever!"
    mike.say "Well I did - so hurry up and open it already!"
    "Harmony nods eagerly, already opening the box."
    "Reaching inside, she pulls out the dress I chose for her."
    "And she stares at it in a stunned silence."
    show harmony normal
    mike.say "Well, Harmony..."
    mike.say "What do you think?"
    if harmony.sub >= 30 and 'religious' not in harmony.traits:
        "Harmony finally stops studying the dress and looks up at me."
        show harmony happy
        "And from the smile spreading across her face, I know it's good news!"
        if 'slutty' in harmony.traits:
            harmony.say "YES!"
            harmony.say "Thank you so much, [hero.name]!"
            harmony.say "I've been dreaming about getting one of these!"
        else:
            harmony.say "You know what, [hero.name]..."
            harmony.say "I always wanted to own something like this."
            harmony.say "I just never could find the courage."
            harmony.say "But if you think I can pull it off - then I know that I can!"
        harmony.say "And I can't wait for you to see me in it!"
        "The way that Harmony's looking at me right now..."
        "It's already making me feel all hot under the collar!"
        mike.say "Y...yeah, Harmony..."
        mike.say "I'm looking forward to that too!"
        show harmony blush
        "I'm still a little flustered when Harmony leans in to kiss me on the cheek."
        "And that's because my mind is already filling up with possibilities."
        "Now I have to figure out a way to get Harmony into the dress."
        "And as soon as possible!"
        $ harmony.flags.sexydate = True
        $ harmony.flags.sluttydate = False
    else:
        show harmony annoyed
        "Harmony shakes her head, a frown already curling her lip."
        "Then she makes her feelings known by thrusting the dress back into my hands."
        "There's really no other way of reading a reaction like that!"
        show harmony sad
        if 'religious' in harmony.traits:
            harmony.say "What's gotten into you, [hero.name]?"
            harmony.say "How could I ever wear something as sinful as that?!?"
        elif 'slutty' in harmony.traits:
            harmony.say "What the hell, [hero.name]?"
            harmony.say "You think that I should cover up more?"
            harmony.say "That I should dress like some kind of fucking nun?!?"
        else:
            harmony.say "Urgh..."
            harmony.say "That's SO slutty, [hero.name]!"
            harmony.say "Is that really how you see me?"
        "I'm so stunned by Harmony's reaction I can't get my words out."
        "And for a few seconds my mouth just moves while I remain silent."
        "Finally I manage to get my brain and my mouth in gear."
        "But it doesn't seem to improve matters that much when I do."
        mike.say "Aw, come on, Harmony!"
        mike.say "It's not that bad."
        mike.say "I mean sure, it's a little revealing."
        mike.say "But it's just making the most of your full figure."
        harmony.say "Oh no..."
        harmony.say "Tell me you didn't just say that!"
        harmony.say "Tell me you didn't say I have a fuller figure!"
        harmony.say "That's just code for saying I'm FAT!"
        "Harmony turns her back on me and storms off."
        "Leaving me standing there with the crumpled dress in my hands."
        $ harmony.love -= 4
        $ hero.cancel_activity()
    return

label harmony_gift_slutty_dress_male:
    "Normally the task of buying a present for a girl is a potential minefield."
    "But when the girl just so happens to be one like Harmony..."
    "Well, it's more like the mines are replaced with nuclear warheads."
    "One wrong move and you run the risk of being totally obliterated in the blast."
    "Though that doesn't mean I'm not going to at least try."
    "Especially when I've seen something as amazing as what's in the box behind my back."
    "The only problem is that it's way too large to stay hidden back there."
    "And so Harmony's already spotted it and is trying to sneak a better look."
    show harmony talkative
    harmony.say "What's that you have there, [hero.name]?"
    show harmony normal
    mike.say "Huh?"
    mike.say "What are you talking about, Harmony?"
    "This conversation is going on as Harmony tries to duck behind me."
    "And, in turn, I do the best I can to stay facing her."
    show harmony whining
    harmony.say "[hero.name]!"
    harmony.say "Will you...stop...teasing me?"
    harmony.say "I can see it...behind your back!"
    show harmony embarrassed
    "I scoot out of Harmony's reach and take a neat step backwards."
    "At the same time extending a hand to make her keep her distance."
    mike.say "Okay, Harmony..."
    mike.say "You got me."
    mike.say "This is for you."
    "I bring the box out from behind my back and hold it out."
    "Waiting until Harmony takes it from me, a smile on her face."
    show harmony talkative
    harmony.say "Ooh..."
    harmony.say "You really shouldn't have."
    harmony.say "But that doesn't mean I don't want it!"
    show harmony happy
    play sound [paper_ripping_1, paper_ripping_2]
    "It's hard not to hold my breath as I wait for Harmony to tear off the wrapping paper."
    "And I swear that me heart skips a beat when she actually opens the box underneath."
    show harmony normal
    "But the look on her face when she pulls out the dress inside is more impactful still."
    "Because the garment is one of the most daring and dangerous I've ever seen."
    "One that, as soon as I pictured Harmony in it, I just knew that I had to buy."
    mike.say "So..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    if harmony.sub >= 70 and 'religious' not in harmony.traits:
        show harmony happy
        "I watch as Harmony's lips twist into a smile."
        "One that's so wicked in nature, I almost can't believe it's real."
        harmony.say "Let me guess..."
        harmony.say "You saw this, and you thought of me?"
        show harmony mean
        "My eyes go wide as I feel like Harmony is reading my mind."
        mike.say "Yeah, Harmony..."
        mike.say "That's exactly what happened!"
        "Harmony's smile becomes wider still."
        "And I can see a fire beginning to burn in her eyes too."
        show harmony happy
        harmony.say "You imagined it covering my body..."
        harmony.say "Clinging so tightly that it left nothing to the imagination..."
        harmony.say "Of reaching out and touching me, to feel the sensation made flesh?"
        show harmony blush
        "I hear the sound of myself swallowing as Harmony's words weave their spell."
        "As she conjures images from my subconscious mind that haunt and compel me."
        mike.say "Erm..."
        mike.say "You could say that!"
        "Harmony gives me a wink as she deftly folds the dress up again."
        "And she adds a nod as she slips it neatly back into the box."
        show harmony talkative
        harmony.say "Don't worry, [hero.name]…"
        harmony.say "You'll get to see me in it soon enough."
        show harmony blush
        harmony.say "And when you do, I promise to make all your dreams come true!"
        $ harmony.flags.sluttydate = True
        $ harmony.flags.sexydate = False
    else:
        show harmony annoyed
        "Harmony's eyes go wide, and they seem to flare with anger."
        "Then she tosses the dress down on the ground and stamps on it."
        mike.say "Hey..."
        mike.say "That was bloody expensive!"
        mike.say "And if you don't want it, I have to return it in good condition."
        "I make a move to pick up the dress before it gets too damaged."
        "But the moment I do, Harmony leers at me, kind of like an enraged beast."
        show harmony angry
        harmony.say "You think I care about you getting a refund?!?"
        harmony.say "Money and sex, that's all you have on your mind!"
        harmony.say "How could you think I'd ever wear something like that?"
        show harmony upset
        "Harmony emphasizes her point by slamming her foot down onto the dress again."
        "And then she underlines it by grinding it under her heel."
        "All I can do is stand there and watch as she vents her rage upon it."
        "That and wince at the notion of the money it cost me."
        "As well as the thought that I'm not going to get any of it back too."
        $ harmony.love -= 10
        $ hero.cancel_activity()
    return

label harmony_gift_butt_plug_male:
    show harmony happy
    harmony.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if harmony.sub <= 50 or not harmony.purity <= 25 or not harmony.sexperience:
        show harmony annoyed
        harmony.say "..."
        harmony.say "Keep it... I don't want it so keep it."
        harmony.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show harmony blush
        harmony.say "It's perfect!"
        harmony.say "Thanks [hero.name], I'll make a good use of it."
        $ harmony.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
