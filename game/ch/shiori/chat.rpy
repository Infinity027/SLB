label shiori_desire_0_male:
    shiori.say "[hero.name] - I just wanted to say...that I'm super happy to be working under you."
    $ shiori.love += 1
    return

label shiori_desire_1_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name] - what do you want me do with all of those files?"
        menu:
            "Archives":
                mike.say "Oh, those...they should go down to the archives, Shiori."
            "Aletta" if Person.is_not_hidden("aletta"):
                mike.say "Don't tackle that yourself, Shiori - take them to Aletta's office."
                $ shiori.sub += 1
            "Me":
                mike.say "Ah, give those to me, Shiori."
                $ shiori.love += 1
                shiori.say "Thank you, [hero.name]."
    else:
        shiori.say "[hero.name], I just wanted to say - you look good dressed casual too."
        menu:
            "It's inappropriate":
                mike.say "Shiori, it's important to maintain the same level of respect for your superiors outside of the office as it is inside of it."
                shiori.say "Oh...I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Thank you":
                mike.say "Thank you for the kind compliment, Shiori."
            "You too":
                mike.say "Thank you, Shiori - so do you."
                $ shiori.love += 1
                shiori.say "Oh...thank you, [hero.name]."
    return

label shiori_desire_2_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name] - I can't find the files for the Murdock case..."
        menu:
            "Archives":
                mike.say "Have you tried looking in the archives?"
            "Aletta" if Person.is_not_hidden("aletta"):
                mike.say "Don't waste your time searching when you'll never find them - ask Aletta instead."
                $ shiori.sub += 1
            "I'll search":
                mike.say "I'm working on that case later today, Shiori - I'll handle finding them myself."
                $ shiori.love += 1
                shiori.say "Okay...thank you, [hero.name]."
    else:
        shiori.say "[hero.name]...do you think this outfit suits me?"
        menu:
            "It's inappropriate":
                mike.say "Shiori, it's important to develop an instinctive appreciation of what is and is not appropriate."
                mike.say "In terms of both work attire and conversational topics to bring up with your superiors."
                shiori.say "I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Not really":
                mike.say "You're not my type, Shiori - so I really couldn't tell you either way."
                $ shiori.love -= 1
            "Yes":
                mike.say "Yes, Shiori - it brings out the best in you, really makes you look cute."
                $ shiori.love += 1
                shiori.say "Wow - thanks, [hero.name]!"
    return

label shiori_desire_3_male:
    if Room.has_tag(game.room, "work") and Person.is_not_hidden("audrey"):
        shiori.say "[hero.name], have you seen Audrey?"
        shiori.say "I've looked, but I can't find her anywhere in the office."
        menu:
            "Archives":
                mike.say "She's not in the office, Shiori - she went down to the archives about twenty minutes ago."
                $ shiori.love += 1
            "Aletta" if Person.is_not_hidden("aletta"):
                mike.say "I don't have time to hunt for her, Shiori - go ask Aletta where she's gotten to."
                $ shiori.sub += 1
            "I'll search":
                mike.say "I need to speak to her anyway, so I'll go find her, Shiori."
        shiori.say "Thanks, [hero.name], that's real kind of you."
    else:
        shiori.say "[hero.name]...erm, do you think that we should maybe...go on a date some time soon?"
        menu:
            "It's inappropriate":
                mike.say "We can't just ignore the fact that we work together, Shiori."
                mike.say "Fraternisation between our respective pay-grades would be completely inappropriate and unprofessional."
                shiori.say "Oh, I see...I'm sorry, [hero.name]."
                $ shiori.sub += 1
            "Not really":
                mike.say "Hmm...I don't think so, Shiori - you're really not up to my usual standards."
                $ shiori.love -= 1
            "Yes":
                mike.say "You know, Shiori - I'd really love to do that."
                $ shiori.love += 1
                shiori.say "You would?!?"
                shiori.say "That's great!"
    return

label shiori_desire_4_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name], I brought you some coffee...just the way you like it."
        menu:
            "Thanks":
                mike.say "Thank you, Shiori - you do take such good care of me."
                $ shiori.love += 1
            "Say nothing":
                mike.say "Whatever, Shiori - just leave it on my desk."
                $ shiori.sub += 1
        $ hero.energy += 1
    else:
        shiori.say "[hero.name], I do worry about your health."
        shiori.say "You work so hard, and you're so skinny - perhaps you should eat more..."
        menu:
            "Not your business":
                mike.say "My personal eating habits really aren't any of your business, Shiori."
                $ shiori.love -= 1
            "Thanks":
                mike.say "It's sweet of you to notice and be concerned for me, Shiori."
                mike.say "I've been very busy lately, and I guess I forgot to take good enough care of myself."
                $ shiori.love += 1
    return

label shiori_desire_5_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name], I see you eating those awful burritos from the cafeteria every day."
        shiori.say "They're so bad for you."
        shiori.say "So I stayed up late last night and made a healthy bento box lunch for you."
        menu:
            "Wow thanks Shiori":
                mike.say "Wow...Shiori - this must have taken you so much effort!"
                mike.say "I'm blown away you'd think enough of me to do this!"
                $ shiori.love += 1
            "Back off":
                mike.say "Really, Shiori - how many times do I have to tell you that my health is my concern, not yours!"
                mike.say "If you want to waste your personal time making packed lunches, then make them for your damn kid!"
                $ shiori.love -= 5
    else:
        shiori.say "[hero.name], you're always eating out and on the go."
        shiori.say "I wish you'd let me cook a nice, wholesome meal for you at home..."
        menu:
            "That sounds great":
                mike.say "That sounds like a great idea, Shiori."
                mike.say "I'd love to try your cooking...and any other home comforts that you'd care to show me..."
                $ shiori.love += 1
            "You're invading my personal space":
                mike.say "Urgh...I hate 'traditional' food - it's always so stodgy and full of MSG!"
                mike.say "You really might as well be trying to poison me with that stuff."
                $ shiori.love -= 1
    return

label shiori_love_0_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name]...would it be possible for me to finish early tonight?"
        menu:
            "No":
                mike.say "I'm sorry, Shiori, but we just have too much work to get through."
                $ shiori.love -= 1
            "Yes":
                mike.say "You work so hard and don't ever complain, Shiori - you deserve a break."
                mike.say "Of course you can leave early - when would you like to go?"
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Thanks, [hero.name]."
    else:
        shiori.say "[hero.name] - you look quite pale."
        shiori.say "Maybe you should drink more milk..."
        menu:
            "Not your business":
                mike.say "Advising me on my health and diet aren't in your job description, Shiori."
                $ shiori.love -= 1
            "Thanks":
                "I glance at my reflection in surprise."
                mike.say "Goodness, you're right - thanks for the advice, Shiori."
                mike.say "Sometime I don't know what I'd do without you to keep an eye on me!"
                $ shiori.love += 1
    return

label shiori_love_1_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name] - I just got a call saying my son is sick."
        shiori.say "Please may I go home to care for him?"
        menu:
            "No":
                mike.say "I'm sorry, Shiori, but we have too much work to get through right now."
                mike.say "If you want to leave, I'll have to deduct the time from your holiday allowance."
                $ shiori.love -= 1
            "Yes":
                mike.say "Of course, Shiori, the boy needs his mother at a time like this."
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Oh, thank you, [hero.name]."
    else:
        shiori.say "[hero.name] - I've never been happier in any other job than I have been working here...with you."
        menu:
            "Not for me":
                mike.say "I can't say the same thing, Shiori - you've been nothing more to me than a genuine liability!"
                $ shiori.love -= 1
            "Thanks":
                mike.say "I feel the same, Shiori - having you around's really made me look forward to a day at work."
                $ shiori.love += 1
    return

label shiori_love_2_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name] - things are really tight for me at the moment...can I have a raise?"
        menu:
            "No":
                mike.say "No way, Shiori - not gonna happen until you shape up your ideas and stop being such a scatter-brained clutz."
                $ shiori.love -= 1
            "Yes":
                mike.say "Well, you've been working for me a while now, and your contract gives me the option of granting you a raise."
                mike.say "So yes, I suppose I can do that."
                $ shiori.love += 1
                $ game.set_flag("worksatisfaction", 5, mod="-")
                shiori.say "Thanks, [hero.name] - you're a really great boss!"
                if shiori.sexperience >= 1:
                    shiori.say "I'll be sure to be extra nice to you in the future [hero.name]."
    else:
        shiori.say "[hero.name] - I've never been happier in any other job than I have been working here...with you."
        menu:
            "Not for me":
                mike.say "I can't say the same thing, Shiori - you've been nothing more to me than a genuine liability!"
                $ shiori.love -= 1
            "Thanks":
                mike.say "I feel the same, Shiori - having you around's really made me look forward to a day at work."
                $ shiori.love += 1
    return

label shiori_love_3_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name] - I'm really glad that we started out as colleagues and became actual friends..."
        menu:
            "We are not":
                mike.say "When did that happen, Shiori?"
                if shiori.sexperience:
                    mike.say "You are just a pretty little thing I use a stress relief."
                    $ shiori.love -= 10
                else:
                    mike.say "Also, technically we're not colleagues - I'm your superior."
                    $ shiori.love -= 1
            "Me too":
                mike.say "I feel the same way, Shiori - you've become much more than just a secretary to me."
                $ shiori.love += 1
                shiori.say "Thank you, [hero.name] - you mean a lot to me, too..."
    else:
        shiori.say "[hero.name] - please be honest...what do you think of me?"
        menu:
            "You are a nice sextoy" if shiori.sexperience >= 1:
                mike.say "I mostly think about just how much I enjoy fucking you."
                $ shiori.sub += 1
                "Shiori blushes and looks down at her feet."
                shiori.say "Th...thank you, [hero.name]."
            "You are my prized sex slave" if shiori.flags.mikeNickname in nickname_master:
                mike.say "I mostly think about how nice and obedient a slave you are."
                $ shiori.sub += 1
                "Shiori blushes and looks down at her feet."
                shiori.say "Th...thank you, [hero.name]."
            "You are a nice person":
                mike.say "I think you're a lovely girl, Shiori - a very special person to know."
                $ shiori.love += 1
            "You are a burden":
                mike.say "To be quite frank, Shiori, you're a professional burden and a damn nuisance in general."
                $ shiori.love -= 1
    return

label shiori_love_4_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name]... I was wondering if you wanted to, maybe... see me outside of work sometime?"
        menu:
            "I would enjoy fucking you again" if shiori.sexperience >= 1 and shiori.love >= 50:
                mike.say "I was thinking of giving your pussy a pounding soon, would you like that?"
                $ shiori.sub += 1
                $ shiori.love += 1
                shiori.say "Y... Yes [hero.name]."
            "That would be nice":
                mike.say "That'd be nice, Shiori."
                mike.say "I'm sure there's a whole other side of you to discover that's every bit as interesting as the one I get to see at work every day!"
                $ shiori.love += 1
            "No thanks":
                mike.say "Urgh...no thanks, Shiori."
                mike.say "Isn't it enough that I have to put up with you at work every single day already?"
                $ shiori.love -= 1
    else:
        shiori.say "Erm...[hero.name]...I was thinking that it might be nice if we...went for a meal, or something?"
        shiori.say "I mean...if you haven't got anything better to do..."
        menu:
            "Offer some meat" if shiori.sexperience >= 1 and shiori.love >= 50:
                mike.say "I'd love to, Shiori!"
                mike.say "But in the meantime if you are hungry you can have my meat any day."
                $ shiori.love += 1
                $ shiori.sub += 1
                shiori.say "I would love that [hero.name]."
            "I'd love to":
                mike.say "I'd love to, Shiori!"
                mike.say "I so badly want to get to know you away from work and all of the damn office politics!"
                $ shiori.love += 1
            "I don't think so":
                mike.say "I don't think so, Shiori."
                mike.say "You're enough of an embarrassment at work, and I don't need you screwing up my social life."
                $ shiori.love -= 1
    return

label shiori_love_5_male:
    if Room.has_tag(game.room, "work"):
        shiori.say "[hero.name], I sometimes wonder how long I can keep up a professional relationship with you."
        shiori.say "Especially when I feel the way about you that I do!"
        menu:
            "I feel the same way":
                mike.say "I know exactly how you feel, Shiori."
                mike.say "Sometimes I can't work at all, as you're always the first thing on my mind!"
            "What are you talking about":
                mike.say "You know, Shiori, sometimes I feel like we're having two completely different and totally unrelated conversations!"
                mike.say "I've told you before - if you have a problem with your position or me as your boss, take it up with HR!"
    else:
        shiori.say "[hero.name], I can't keep this to myself any longer!"
        shiori.say "I think I'm falling in love with you...and I just have to know if you feel the same way!"
        menu:
            "I love you too, Shiori":
                mike.say "Oh, Shiori - I know how much courage it must have taken for you to come out and say that!"
                mike.say "But it was worth it - because, yes, I feel the same way too!"
                $ shiori.love += 1
            "I think you got the wrong end of the stick":
                mike.say "Erm...Shiori, I think you might have misread my intentions towards you a little there!"
                mike.say "And you went and poured your heart out anyway..."
                mike.say "Ouch...that's awkward!"
                $ shiori.love -= 1
    return

label shiori_good_sweet_talk_male:
    show shiori
    if shiori.love > 133:
        mike.say "I can't believe your husband left you, Shiori."
        mike.say "But I want you to know that I'll never do that."
        mike.say "In fact, I can't imagine being without you!"
        show shiori happy
        shiori.say "Oh, [hero.name]!"
        shiori.say "I love you so much!"
    elif shiori.love > 66:
        mike.say "Did I tell you how beautiful you look today, Shiori?"
        mike.say "I really should do that more often!"
        show shiori blush
        shiori.say "Oh, you're making me blush...oh my!"
        shiori.say "Thank you, [hero.name]!"
    else:
        mike.say "I don't know how you do it, Shiori."
        mike.say "You're a single mother that holds down a job."
        mike.say "And you do both so well - you're amazing!"
        show shiori blush
        shiori.say "I...I am?!?"
        shiori.say "Thank you, [hero.name]!"
    hide shiori
    return

label shiori_bad_sweet_talk_male:
    show shiori
    mike.say "Being a mom really suits you, Shiori."
    mike.say "It gives you a kind of homely vibe!"
    show shiori angry
    shiori.say "You mean it makes me seem fat and frumpy?!?"
    mike.say "Ah, no...that's not what I meant!"
    hide shiori
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
