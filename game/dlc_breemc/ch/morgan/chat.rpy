label morgan_desire_0_female:
label morgan_desire_1_female:
label morgan_desire_2_female:
label morgan_desire_3_female:
label morgan_desire_4_female:
label morgan_desire_5_female:
label morgan_love_0_female:
label morgan_love_1_female:
label morgan_love_2_female:
label morgan_love_3_female:
label morgan_love_4_female:
label morgan_love_5_female:
    call expression conditional_choice_picker(MORGAN_CHATS_FEMALE) from _morgan_love_5
    return

define MORGAN_CHATS_FEMALE = {"morgan_chat_hang_female": (True, 1),
                              "morgan_chat_bike_female": ("morgan.male >= 50", 1),
                              "morgan_chat_bike2_female": ("morgan.male < 50", 1),
                              "morgan_chat_tough_female": ('morgan.male > 50', 1),
                              "morgan_chat_feelings_female": ("morgan.love >= 140 and morgan.sexperience >= 1", 1),
                              "morgan_chat_sexuality_female": ('morgan.male < 70 and morgan.love >= 40', 1),
                              "morgan_chat_skin_female": ('morgan.male < 50', 1),
                              "morgan_chat_love_you_female": ("morgan.love >= 160 and morgan.sexperience >= 2", 1),
                              "morgan_chat_jack_female": (True, 1),
                              "morgan_chat_alexis_female": ("morgan.love >= 60", 1),
                              "morgan_chat_kylie_female": (True, 1),
                              "morgan_chat_girl_female": ("morgan.male >= 50", 1),
                              "morgan_chat_girl2_female": ("morgan.male < 50", 1),
                              "morgan_chat_lovers_female": ("morgan.love >= 120 and morgan.sexperience >= 3", 1),
                              "morgan_chat_friends_lovers_female": ("morgan.love >= 120 and morgan.sexperience >= 3", 1)
                              }


label morgan_chat_hang_female:
    morgan.say "God, I used to love just hanging out back when we were kids."
    morgan.say "It felt like having nothing to do was actually doing something back then."
    menu:
        "We had so much fun":
            bree.say "Just kicking back and wasting time was so sweet back in the day."
            $ morgan.male += 1
            $ morgan.love += 1
        "I guess we grew out of that":
            bree.say "We kind of grew out of that though, didn't we?"
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I should have learned more about you":
            bree.say "All that time together and I didn't know a thing about you, Morgan..."
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_bike_female:
    morgan.say "You remember the bike races that we used to have around the neighborhood?"
    morgan.say "That one time that Jack fell off, scraped his knees up and wailed like a little pussy?"
    menu:
        "You were some rider!":
            bree.say "You were some mean rider, Morgan - it was you that drove Jack off of the road!"
            morgan.say "He should've stayed out of my way more!"
            $ morgan.male += 1
        "I ride an exercise bike":
            bree.say "No - sad to say the closest I get these days is the exercise bike at the gym!"
            morgan.say "Sucks getting old, doesn't it?"
            $ morgan.male -= 1
            $ morgan.love += 1
    return

label morgan_chat_bike2_female:
    morgan.say "Ah, I can remember riding around on our bikes together forever!"
    morgan.say "Sometimes I just wanted to ride away and never come back."
    menu:
        "Where would you have gone?":
            bree.say "Where would you have gone?"
            morgan.say "I don't know. Anywhere? Just not home."
            $ morgan.male += 1
        "But you stayed!":
            bree.say "But you stayed! And it's good because I would have missed you, I think."
            morgan.say "That's sweet!"
            $ morgan.male -= 1
            $ morgan.love += 1
    return


label morgan_chat_tough_female:
    morgan.say "I guess I was always trying to be as tough as the boys when I was little."
    morgan.say "I just wanted to be accepted by you boys."
    menu:
        "I liked it when you acted all tough":
            bree.say "You acted all tough and completely fooled me, Morgan."
            $ morgan.male += 1
        "You didn't need to pretend":
            bree.say "You didn't need to pretend to be tough, Morgan! We liked you for who you are."
            $ morgan.male -= 1
            $ morgan.love += 1
        "And it didn't work":
            bree.say "And it didn't work. I remember a lot of the boys laughed at you for it!"
            $ morgan.male -= 1
            $ morgan.love -= 1
    return


label morgan_chat_sexuality_female:
    morgan.say "When we were kids, I didn't really understand my sexuality. I liked you and Jack."
    morgan.say "But I was also interested in girls."
    morgan.say "I tried so hard to fit in with all of you, but it really never worked out."
    menu:
        "You just needed to try harder":
            bree.say "You just needed to try harder. It's hard for people getting mixed messages!"
            $ morgan.male += 1
            $ morgan.love -= 1
        "You just needed to be yourself":
            bree.say "You tried too hard! You just needed to be yourself. The real you is a lot of fun."
            $ morgan.male -= 1
            $ morgan.love += 1
        "You didn't really know who you were":
            bree.say "I couldn't see it at the time, but looking back I can see how you confused you used to be!"
            $ morgan.male -= 1
            $ morgan.love -= 1
    return

label morgan_chat_skin_female:
    morgan.say "I feel more at ease in my skin than ever right now. That tough act was just an act."
    morgan.say "And I'm glad that you helped me see that!"
    menu:
        "I like the old you better":
            bree.say "Honestly I like the old you better."
            $ morgan.male += 1
            $ morgan.love -= 1
        "You seem more confident":
            bree.say "It was worth the wait - you're pretty fun to be around these days, Morgan!"
            $ morgan.male -= 1
            $ morgan.love += 1
        "You didn't really know who you were":
            bree.say "I couldn't see it at the time, but looking back I can see how you confused you used to be!"
            $ morgan.male -= 1
            $ morgan.love -= 1
    return


label morgan_chat_feelings_female:
    if morgan.male >= 50:
        morgan.say "You know, I'm not that good at talking about my feelings."
        morgan.say "But hooking up with you again's really reminded me of how much I used to have a crush on you!"
    elif morgan.sub <= 75:
        morgan.say "It's weird, but I never thought that I'd have a chance to do all of the things that I always wanted to do with you, [hero.name]!"
    else:
        morgan.say "Oh, [hero.name] - since we met up again, you've rekindled all of the old feelings I used to have for you!"
    menu:
        "I'm no good at this shit either!" if morgan.male >= 50:
            bree.say "It's hard for me to say it too, Morgan - but I'm loving having you back around too."
            $ morgan.male += 1
        "It's like a second chance":
            bree.say "I feel the same way, Morgan - like we've been given a second chance."
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "You can tell me anything":
            bree.say "You don't have to be afraid to open up to me, Morgan!"
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_love_you_female:
    if morgan.male >= 50:
        morgan.say "[hero.name]...this is hard for me to say...real hard."
        morgan.say "But, I think I love you - more now than I ever did when we were kids..."
    elif morgan.sub <= 75:
        morgan.say "It's hard to say this, [hero.name] - but I think I'm I'm in love with you!"
    else:
        morgan.say "Oh, [hero.name] - I always loved you when we were young."
        morgan.say "And now that we're together again, I've fallen for you all over again - it's like some kind of fairy-tale come true!"
    menu:
        "Geez, I sorta feel the same way too!":
            bree.say "Ah...this is gonna make me sound stupid, Morgan - but I think I love you too!"
            $ morgan.male += 1
        "It was simply meant to be!":
            bree.say "I think it's fate, Morgan, destiny - it was written in the stars that we're supposed to be together!"
            $ morgan.male -= 1
            $ morgan.love += 1
    return

label morgan_chat_jack_female:
    if morgan.male >= 50:
        morgan.say "Do you remember that first summer that Jack started growing his hair and listening to heavy metal?"
    else:
        morgan.say "Do you remember when Jack had all that greasy hair and blew our eardrums out with the heavy metal?"
    menu:
        "He never looked back":
            bree.say "Yeah, and he's never looked back since - that guy'll be metal until the day he dies!"
            $ morgan.male += 1
        "He's still following his vision":
            bree.say "Well, he was always a kind of all or nothing guy - and I guess he still is!"
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "He's still a greasy slob":
            bree.say "Yeah, he never got any less greasy and spotty - just bigger and fatter!"
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_alexis_female:
    morgan.say "You know, I never forgave Alexis for what she did to you back in high school."
    morgan.say "I came real close to punching her in the mouth, more than once..."
    menu:
        "You could have given her one from me":
            bree.say "I wouldn't have stopped you from hitting her, Morgan - in fact, you could have given her one from me, too!"
            $ morgan.male += 1
        "It was a long time ago":
            bree.say "Thanks, Morgan - I appreciate that."
            bree.say "But it was a long time ago, and I'd rather concentrate on the here and now."
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I don't think violence is the answer":
            bree.say "Don't ever sink to her level, Morgan - or else you'd be as bad as her!"
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_kylie_female:
    morgan.say "Kylie always used to freak me out when she was a little kid."
    morgan.say "The way she'd stare at you with those cold, dead eyes!"
    menu:
        "She hasn't changed much":
            bree.say "You should see her now - she hasn't changed all that much!"
            $ morgan.male += 1
        "She has a strange vibe":
            bree.say "I know what you mean - she's pretty intense!"
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "Don't worry, I'll protect you":
            bree.say "She's still pretty creepy, Morgan - but don't worry, I'll keep her away from you."
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_girl_female:
    morgan.say "You were always reckless and impatient when we were kids, [hero.name]."
    morgan.say "I often wonder if that's why you never noticed I was a girl!"
    menu:
        "You were a handful too!":
            bree.say "Hey, you were a handful too, Morgan -- and you still are now!"
            $ morgan.male += 1
        "I guess I just didn't really see you":
            bree.say "I guess I just didn't really see you -- but I see you clearly enough right now!"
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "I wish I had slowed down!":
            bree.say "If only I'd slowed down long enough, Morgan - I'd have seen how truly special you are!"
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1

label morgan_chat_girl2_female:
    morgan.say "Be honest, [hero.name]..."
    morgan.say "Did you not realise I was a girl because I was a tomboy?"
    morgan.say "Or because you always had your head in the clouds?"
    menu:
        "You weren't just a tomboy!":
            bree.say "You weren't just a tomboy, sometimes you really did act like a boy!"
            $ morgan.male += 1
        "A little bit of both":
            bree.say "A little bit of both -- but I see you clearly enough right now!"
            $ morgan.male -= 1
            $ morgan.love += 1
    return

label morgan_chat_lovers_female:
    morgan.say "It's pretty weird, [hero.name] - how we went from kids that were friends to adults that are lovers."
    morgan.say "Don't you think?"
    morgan.say "The little girl that loved the little boy that thought she was a little boy too but then found out she was a girl and then fell in love with each other?"
    menu:
        "Does that make me gay?":
            bree.say "Hey if I thought you were a boy and I'm with you, does that make me gay?"
            morgan.say "No, but it would be okay if it did."
            $ morgan.male += 1
        "What are the chances":
            bree.say "I could never have imagined it, Morgan."
            bree.say "I'm just glad that it did."
            $ morgan.male -= 1
            if morgan.male > 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
        "It's like happy ever after!":
            bree.say "It makes me feel like I'm living in an enchanted storybook!"
            $ morgan.male -= 1
            if morgan.male <= 50:
                $ morgan.love += 1
            else:
                $ morgan.love -= 1
    return

label morgan_chat_friends_lovers_female:
    morgan.say "I like that we were friends before we were lovers, [hero.name]."
    morgan.say "I could never be without you as either, and I want to keep you as both."
    menu:
        "We'll always be both":
            bree.say "Each one makes the other even stronger, Morgan."
            $ morgan.male += 1
        "I think we were meant to be":
            bree.say "I'd like to think that we were meant to find each other again."
            bree.say "That's how it feels to me!"
            $ morgan.male -= 1
            $ morgan.love += 1
        "Friends with benefits":
            bree.say "We're like a two-for-one -- friends with benefits!"
            $ morgan.male -= 1
            $ morgan.love -= 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
