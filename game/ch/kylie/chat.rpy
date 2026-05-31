label kylie_desire_0_male:
    kylie.say "I'm bored."
    return

label kylie_desire_1_male:
    $ result = randint(1, 3)
    if result == 1:
        kylie.say "I always thought you were too good looking for Alexis."
    elif result == 2:
        kylie.say "Do you think I should dress sexier?"
    else:
        kylie.say "I would do anything for you..."
    $ kylie.love += 1
    return

label kylie_desire_2_male:
    kylie.say "You're so smart..."
    $ kylie.love += 1
    return

label kylie_desire_3_male:
    kylie.say "You know what would be great?"
    kylie.say "Me bearing your child."
    kylie.say "Having a cute mini-you would be so awesome."
    $ kylie.love += 1
    return

label kylie_desire_4_male:
    kylie.say "When I'm around you, I kind of feel like I'm on drugs."
    kylie.say "Not that I do drugs."
    kylie.say "Unless you do drugs, in which case I do them all the time."
    kylie.say "All of them."
    $ kylie.love += 1

    return

label kylie_desire_5_male:
    kylie.say "Promise me you will never leave me or cheat on me."
    $ kylie.love += 1
    return

label kylie_love_0_male:
    kylie.say "I think we are soulmates."
    $ kylie.love += 1
    return

label kylie_love_1_male:
    kylie.say "What would you like me to be?"
    kylie.say "I can be anything or anyone for you."
    $ kylie.love += 1
    return

label kylie_love_2_male:
    kylie.say "I hate when we are not together."
    $ kylie.love += 1

    return

label kylie_love_3_male:
    kylie.say "Without you life would be intolerable."
    $ kylie.love += 1
    return

label kylie_love_4_male:
    kylie.say "What do you say we just get married right now."
    $ kylie.love += 1
    return

label kylie_love_5_male:
    kylie.say "You are probably the best guy ever."
    $ kylie.love += 1
    return

label kylie_good_sweet_talk_male:
    show kylie
    if kylie.love > 133:
        mike.say "I've been so happy since we hooked up, Kylie."
        mike.say "In fact, I can't imagine my life without you!"
        show kylie happy
        kylie.say "I feel the same way too!"
        kylie.say "Life wouldn't be worth living without you..."
    elif kylie.love > 66:
        mike.say "Wow!"
        mike.say "That outfit looks so good on you, Kylie!"
        mike.say "I can't take my eyes off you."
        show kylie happy
        kylie.say "I'm SO happy to hear that!"
        kylie.say "I want you to only have eyes for me."
    else:
        mike.say "You were a pretty annoying kid, Kylie."
        mike.say "But you grew up to be an amazing woman!"
        kylie.say "Thank you, [hero.name]!"
        kylie.say "All I ever wanted was for you to notice me."
    hide kylie
    return

label kylie_bad_sweet_talk_male:
    show kylie
    mike.say "I love how quirky you are, Kylie."
    mike.say "You're kind of crazy in a good way, you know?"
    show kylie angry
    kylie.say "Who told you I was crazy, huh?!?"
    kylie.say "I have certificates to prove I'm not crazy!"
    mike.say "Erm...maybe we should forget I said that?"
    hide kylie
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
