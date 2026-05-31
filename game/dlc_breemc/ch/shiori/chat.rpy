label shiori_desire_0_female:
    shiori.say "[hero.name] - I just wanted to say...that I'm super happy to be working under you."
    $ shiori.love += 1
    return

label shiori_desire_1_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name] - what do you want me do with all of those files?"
        menu:
            "Archives":
                bree.say "Oh, those...they should go down to the archives, Shiori."
            "Aletta":
                bree.say "Don't tackle that yourself, Shiori - take them to Aletta's office."
                $ shiori.sub += 1
            "Me":
                bree.say "Ah, give those to me, Shiori."
                $ shiori.love += 1
                shiori.say "Thank you, [hero.name]."
    else:
        shiori.say "[hero.name], I just wanted to say - you look good dressed casual too."
        menu:
            "It's inappropriate":
                bree.say "Shiori, it's important to maintain the same level of respect for your superiors outside of the office as it is inside of it."
                shiori.say "Oh...I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Thank you":
                bree.say "Thank you for the kind compliment, Shiori."
            "You too":
                bree.say "Thank you, Shiori - so do you."
                $ shiori.love += 1
                shiori.say "Oh...thank you, [hero.name]."
    return

label shiori_desire_2_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name] - I can't find the files for the Murdock case..."
        menu:
            "Archives":
                bree.say "Have you tried looking in the archives?"
            "Aletta":
                bree.say "Don't waste your time searching when you'll never find them - ask Aletta instead."
                $ shiori.sub += 1
            "I'll search":
                bree.say "I'm working on that case later today, Shiori - I'll handle finding them myself."
                $ shiori.love += 1
                shiori.say "Okay...thank you, [hero.name]."
    else:
        shiori.say "[hero.name]...do you think this outfit suits me?"
        menu:
            "It's inappropriate":
                bree.say "Shiori, it's important to develop an instinctive appreciation of what is and is not appropriate."
                bree.say "In terms of both work attire and conversational topics to bring up with your superiors."
                shiori.say "I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Not really":
                bree.say "You're not my type, Shiori - so I really couldn't tell you either way."
                $ shiori.love -= 1
            "Yes":
                bree.say "Yes, Shiori - it brings out the best in you, really makes you look cute."
                $ shiori.love += 1
                shiori.say "Wow - thanks, [hero.name]!"
    return

label shiori_desire_3_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name], have you seen Audrey?"
        shiori.say "I've looked, but I can't find her anywhere in the office."
        menu:
            "Archives":
                bree.say "She's not in the office, Shiori - she went down to the archives about twenty minutes ago."
                $ shiori.love += 1
            "Aletta":
                bree.say "I don't have time to hunt for her, Shiori - go ask Aletta where she's gotten to."
                $ shiori.sub += 1
            "I'll search":
                bree.say "I need to speak to her anyway, so I'll go find her, Shiori."
        shiori.say "Thanks, [hero.name], that's real kind of you."
    else:
        shiori.say "[hero.name]...erm, do you think that we should maybe...go on a date some time soon?"
        menu:
            "It's inappropriate":
                bree.say "We can't just ignore the fact that we work together, Shiori."
                bree.say "Fraternisation between our respective pay-grades would be completely inappropriate and unprofessional."
                shiori.say "Oh, I see...I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Not really":
                bree.say "Hmm...I don't think so, Shiori - you're really not up to my usual standards."
                $ shiori.love -= 1
            "Yes":
                bree.say "You know, Shiori - I'd really love to do that."
                $ shiori.love += 1
                shiori.say "You would?!?"
                shiori.say "That's great!"
    return

label shiori_desire_4_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name], I brought you some coffee...just the way you like it."
        menu:
            "Thanks":
                bree.say "Thank you, Shiori - you do take such good care of me."
                $ shiori.love += 1
            "Say nothing":
                bree.say "Whatever, Shiori - just leave it on my desk."
                $ shiori.sub += 1
        $ hero.energy += 1
    else:
        shiori.say "[hero.name], I do worry about your health."
        shiori.say "You work so hard, and you're so skinny - perhaps you should eat more..."
        menu:
            "Not your business":
                bree.say "My personal eating habits really aren't any of your business, Shiori."
                $ shiori.love -= 1
            "Thanks":
                bree.say "It's sweet of you to notice and be concerned for me, Shiori."
                bree.say "I've been very busy lately, and I guess I forgot to take good enough care of myself."
                $ shiori.love += 1
    return

label shiori_desire_5_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name], I see you eating those awful burritos from the cafeteria every day."
        shiori.say "They're so bad for you."
        shiori.say "So I stayed up late last night and made a healthy bento box lunch for you."
        menu:
            "Wow thanks Shiori":
                bree.say "Wow...Shiori - this must have taken you so much effort!"
                bree.say "I'm blown away you'd think enough of me to do this!"
                $ shiori.love += 1
            "Back off":
                bree.say "Really, Shiori - how many times do I have to tell you that my health is my concern, not yours!"
                bree.say "If you want to waste your personal time making packed lunches, then make them for your damn kid!"
                $ shiori.love -= 5
    else:
        shiori.say "[hero.name], you're always eating out and on the go."
        shiori.say "I wish you'd let me cook a nice, wholesome meal for you at home..."
        menu:
            "That sounds great":
                bree.say "That sounds like a great idea, Shiori."
                bree.say "I'd love to try your cooking...and any other home comforts that you'd care to show me..."
                $ shiori.love += 1
            "You're invading my personal space":
                bree.say "Urgh...I hate 'traditional' food - it's always so stodgy and full of MSG!"
                bree.say "You really might as well be trying to poison me with that stuff."
                $ shiori.love -= 1
    return

label shiori_love_0_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name]...would it be possible for me to finish early tonight?"
        menu:
            "No":
                bree.say "I'm sorry, Shiori, but we just have too much work to get through."
                $ shiori.love -= 1
            "Yes":
                bree.say "You work so hard and don't ever complain, Shiori - you deserve a break."
                bree.say "Of course you can leave early - when would you like to go?"
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Thanks, [hero.name]."
    else:
        shiori.say "[hero.name] - you look quite pale."
        shiori.say "Maybe you should drink more milk..."
        menu:
            "Not your business":
                bree.say "Advising me on my health and diet aren't in your job description, Shiori."
                $ shiori.love -= 1
            "Thanks":
                "I glance at my reflection in surprise."
                bree.say "Goodness, you're right - thanks for the advice, Shiori."
                bree.say "Sometime I don't know what I'd do without you to keep an eye on me!"
                $ shiori.love += 1
    return

label shiori_love_1_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name] - I just got a call saying my son is sick."
        shiori.say "Please may I go home to care for him?"
        menu:
            "No":
                bree.say "I'm sorry, Shiori, but we have too much work to get through right now."
                bree.say "If you want to leave, I'll have to deduct the time from your holiday allowance."
                $ shiori.love -= 1
            "Yes":
                bree.say "Of course, Shiori, the boy needs his mother at a time like this."
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Oh, thank you, [hero.name]."
    else:
        shiori.say "[hero.name] - I've never been happier in any other job than I have been working here...with you."
        menu:
            "Not for me":
                bree.say "I can't say the same thing, Shiori - you've been nothing more to me than a genuine liability!"
                $ shiori.love -= 1
            "Thanks":
                bree.say "I feel the same, Shiori - having you around's really made me look forward to a day at work."
                $ shiori.love += 1
    return

label shiori_love_2_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name] - things are really tight for me at the moment...can I have a raise?"
        menu:
            "No":
                bree.say "No way, Shiori - not gonna happen until you shape up your ideas and stop being such a scatter-brained clutz."
                $ shiori.love -= 1
            "Yes":
                bree.say "Well, you've been working for me a while now, and your contract gives me the option of granting you a raise."
                bree.say "So yes, I suppose I can do that."
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Thanks, [hero.name] - you're a really great boss!"
                if shiori.sexperience >= 1:
                    shiori.say "I'll be sure to be extra nice to you in the future [hero.name]."
    else:
        shiori.say "[hero.name] - I've never been happier in any other job than I have been working here...with you."
        menu:
            "Not for me":
                bree.say "I can't say the same thing, Shiori - you've been nothing more to me than a genuine liability!"
                $ shiori.love -= 1
            "Thanks":
                bree.say "I feel the same, Shiori - having you around's really made me look forward to a day at work."
                $ shiori.love += 1
    return

label shiori_love_3_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name] - I'm really glad that we started out as colleagues and became actual friends..."
        menu:
            "We are not":
                bree.say "When did that happen, Shiori?"
                if shiori.sexperience:
                    bree.say "You are just a pretty little thing I use a stress relief."
                    $ shiori.love -= 10
                else:
                    bree.say "Also, technically we're not colleagues - I'm your superior."
                    $ shiori.love -= 1
            "Me too":
                bree.say "I feel the same way, Shiori - you've become much more than just a secretary to me."
                $ shiori.love += 1
                shiori.say "Thank you, [hero.name] - you mean a lot to me, too..."
    else:
        shiori.say "[hero.name] - please be honest...what do you think of me?"
        menu:
            "You are a nice sextoy" if shiori.sexperience >= 1:
                bree.say "I mostly think about just how much I enjoy fucking you."
                $ shiori.sub += 1
                "Shiori blushes and looks down at her feet."
                shiori.say "Th...thank you, [hero.name]."
            "You are my prized sex slave" if shiori.flags.mikeNickname in nickname_master:
                bree.say "I mostly think about how nice and obedient a slave you are."
                $ shiori.sub += 1
                "Shiori blushes and looks down at her feet."
                shiori.say "Th...thank you, [hero.name]."
            "You are a nice person":
                bree.say "I think you're a lovely girl, Shiori - a very special person to know."
                $ shiori.love += 1
            "You are a burden":
                bree.say "To be quite frank, Shiori, you're a professional burden and a damn nuisance in general."
                $ shiori.love -= 1
    return

label shiori_love_4_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name]... I was wondering if you wanted to, maybe... see me outside of work sometime?"
        menu:
            "I would enjoy fucking you again" if shiori.sexperience >= 1 and shiori.love >= 50:
                bree.say "I was thinking of giving your pussy a pounding soon, would you like that?"
                $ shiori.sub += 1
                $ shiori.love += 1
                shiori.say "Y... Yes [hero.name]."
            "That would be nice":
                bree.say "That'd be nice, Shiori."
                bree.say "I'm sure there's a whole other side of you to discover that's every bit as interesting as the one I get to see at work every day!"
                $ shiori.love += 1
            "No thanks":
                bree.say "Urgh...no thanks, Shiori."
                bree.say "Isn't it enough that I have to put up with you at work every single day already?"
                $ shiori.love -= 1
    else:
        shiori.say "Erm...[hero.name]...I was thinking that it might be nice if we...went for a meal, or something?"
        shiori.say "I mean...if you haven't got anything better to do..."
        menu:
            "Offer some meat" if shiori.sexperience >= 1 and shiori.love >= 50:
                bree.say "I'd love to, Shiori!"
                bree.say "But in the meantime if you are hungry you can have my meat any day."
                $ shiori.love += 1
                $ shiori.sub += 1
                shiori.say "I would love that [hero.name]."
            "I'd love to":
                bree.say "I'd love to, Shiori!"
                bree.say "I so badly want to get to know you away from work and all of the damn office politics!"
                $ shiori.love += 1
            "I don't think so":
                bree.say "I don't think so, Shiori."
                bree.say "You're enough of an embarrassment at work, and I don't need you screwing up my social life."
                $ shiori.love -= 1
    return

label shiori_love_5_female:
    if game.room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
        shiori.say "[hero.name], I sometimes wonder how long I can keep up a professional relationship with you."
        shiori.say "Especially when I feel the way about you that I do!"
        menu:
            "I feel the same way":
                bree.say "I know exactly how you feel, Shiori."
                bree.say "Sometimes I can't work at all, as you're always the first thing on my mind!"
            "What are you talking about":
                bree.say "You know, Shiori, sometimes I feel like we're having two completely different and totally unrelated conversations!"
                bree.say "I've told you before - if you have a problem with your position or me as your boss, take it up with HR!"
    else:
        shiori.say "[hero.name], I can't keep this to myself any longer!"
        shiori.say "I think I'm falling in love with you...and I just have to know if you feel the same way!"
        menu:
            "I love you too, Shiori":
                bree.say "Oh, Shiori - I know how much courage it must have taken for you to come out and say that!"
                bree.say "But it was worth it - because, yes, I feel the same way too!"
                $ shiori.love += 1
            "I think you got the wrong end of the stick":
                bree.say "Erm...Shiori, I think you might have misread my intentions towards you a little there!"
                bree.say "And you went and poured your heart out anyway..."
                bree.say "Ouch...that's awkward!"
                $ shiori.love -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
