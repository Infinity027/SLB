label minami_talk_love_male:
    mike.say "Remember when we were kids, Minami, and you used to think the idea of love was gross?"
    mike.say "Did you ever get over that, or are you still creeped out by it?"
    "Minami narrows her eyes and lands a little punch on my arm."
    show minami annoyed
    minami.say "Duh, yeah, big bro!"
    minami.say "I'm not a little girl anymore!"
    $ minami.love -= 1
    return

label minami_talk_sex_male:
    mike.say "Ah, this isn't easy for me to bring up, Minami."
    mike.say "But did Mom and Dad give you the same talk they gave me when I moved out?"
    mike.say "You know...the one about...sex?"
    show minami blush
    "Minami flushes red, but I can see that she's smiling all the same."
    minami.say "Big bro - you're being SO embarrassing!"
    minami.say "You can't know about THAT!"
    $ minami.sub += 1
    return

label minami_talk_politics_male:
    mike.say "The news and the papers really used to bore you when I lived back home."
    mike.say "Have you gotten any more interested in stuff like, I don't know...politics?"
    show minami annoyed
    "Minami rolls her eyes and shakes her head."
    minami.say "Urgh...that's SO boring."
    minami.say "All that stuff is for when you're old and boring too!"
    $ minami.love -= 1
    return

label minami_talk_food_male:
    mike.say "I really thought I'd miss Mom's cooking when I moved out."
    mike.say "But there's so much to choose from in the big city, I soon got over it."
    mike.say "How about you, Minami?"
    show minami happy
    "Minami's eyes light up at the question."
    minami.say "Oh yeah, big bro - I wanna try EVERYTHING!"
    minami.say "All the stuff I could never get at home..."
    $ minami.love += 1
    return

label minami_talk_travels_male:
    mike.say "I used to think that moving to the city would be like living abroad, or something - but it's not."
    mike.say "Now I want to see the world even more than I did before."
    mike.say "You think you'll go back home after college, or maybe go travelling instead?"
    show minami tehe
    "Minami gives me a sweet smile and leans a little closer to me."
    minami.say "I don't mind where I am, big bro."
    minami.say "So long as you're there too!"
    $ minami.love += 1
    return

label minami_talk_tv_male:
    mike.say "We always used to be fighting over the remote control - driving Mom and Dad insane!"
    mike.say "You still the same hopeless TV addict I used to know, Minami?"
    show minami happy
    "Minami nods with some serious enthusiasm."
    minami.say "Oh yeah, you have NO idea!"
    minami.say "Actually, I need to talk to you about the streaming services you guys get here..."
    $ minami.love += 1
    return

label minami_talk_sports_male:
    mike.say "I never remember you being into any sports when we were kids, Minami."
    mike.say "But then most of our home-town teams were pretty lame!"
    show minami annoyed
    "Minami makes a grunting sound and shakes her head."
    show minami angry
    minami.say "Urgh!"
    minami.say "Sports suck - always have, always will."
    $ minami.love -= 1
    return

label minami_talk_fashion_male:
    mike.say "You never seem to wear what the girls I know are wearing, Minami."
    mike.say "Are you even interested in keeping up with the latest trends?"
    "Minami shakes her head at this, chuckling to herself."
    minami.say "I've never been interested in being normal or fitting in."
    show minami tehe
    minami.say "I kinda like being outrageous!"
    $ minami.love += 1
    return

label minami_talk_books_male:
    mike.say "I see you ordered some shelves for your room, Minami."
    mike.say "Are you reading anything decent?"
    show minami happy
    "Minami smiles at my interest in her reading habits."
    minami.say "You know me, big bro."
    minami.say "It's either manga or else it's a text-book!"
    $ minami.love += 1
    return

label minami_talk_people_male:
    mike.say "The city's a lot bigger than the little town we grew up in, Minami."
    mike.say "How are you coping with the crowds and all these people?"
    mike.say "I know I found it tough when I first moved here."
    show minami happy
    "Minami smiles at my question, cocking her head towards me."
    minami.say "There could be a billion people here, or just two, big bro."
    minami.say "And I'd still be okay with it being two if they were you and me!"
    $ minami.love += 1
    return

label minami_talk_computers_male:
    mike.say "What kind of computer did you bring with you, Minami?"
    mike.say "One for your studies?"
    mike.say "Or one for gaming?"
    show minami surprised
    "Minami looks almost offended by the question."
    minami.say "Oh come on, big bro."
    show minami tehe
    minami.say "I have one for each - don't you?!?"
    $ minami.love += 1
    return

label minami_talk_music_male:
    mike.say "Hey, Minami - I'm kind of intrigued to know what music you're into."
    mike.say "I mean, you can't still be into stuff like K-Pop, can you!"
    show minami annoyed
    "Minami crosses her arms over her chest and fixes me with a stern gaze."
    minami.say "Hey, you take that back - right now!"
    minami.say "That's a much maligned and misunderstood genre of music!"
    $ minami.love -= 1
    return

label minami_talk_birthday_male:
    show minami
    mike.say "Happy birthday, Minami."
    show minami happy
    mike.say "It's so great to be able to say that to you on the actual day!"
    minami.say "Oh, thanks, big bro!"
    show minami tehe
    minami.say "I didn't think you'd even remember."
    $ minami.love += 5
    hide minami
    return

init:
    define nickname_onii_chan = ["Onii-chan", "onii-chan"]
    define nickname_nii_san = ["Nii-san", "nii-san"]
    define nickname_bro_bro = ["Bro-bro", "bro-bro"]
    define nickname_hero_name = ["[hero.name]"]

label command_nickname_minami:
    menu:

        "Call me Onii-chan" if active_girl.flags.mikeNickname not in nickname_onii_chan and active_girl.love > 100 and "bike" in hero.inventory:
            $ active_girl.flags.mikeNickname = "Onii-chan"
        "Stop calling me Onii-chan" if active_girl.flags.mikeNickname in nickname_onii_chan:
            $ active_girl.flags.mikeNickname = None


        "Call me Nii-san" if active_girl.flags.mikeNickname not in nickname_nii_san and active_girl.love > 100 and "bike" in hero.inventory:
            $ active_girl.flags.mikeNickname = "Nii-san"
        "Stop calling me Nii-san" if active_girl.flags.mikeNickname in nickname_nii_san:
            $ active_girl.flags.mikeNickname = None


        "Call me Bro-bro" if active_girl.flags.mikeNickname not in nickname_bro_bro and active_girl.love > 50:
            $ active_girl.flags.mikeNickname = "Bro-bro"
        "Stop calling me Bro-bro" if active_girl.flags.mikeNickname in nickname_bro_bro:
            $ active_girl.flags.mikeNickname = None


        "Call me [[hero.name]" if active_girl.flags.mikeNickname not in nickname_hero_name and CHEAT == True:
            $ active_girl.flags.mikeNickname = "[hero.name]"
        "Stop calling me [[hero.name]" if active_girl.flags.mikeNickname in nickname_hero_name:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl


label submissive_interact_minami_male:
    mike.say "Hey, Minami..."
    mike.say "The whole fact that we're a couple is pretty wild, huh?"
    show minami happy
    minami.say "Yeah, big bro - it sure is!"
    show minami normal
    mike.say "So I was thinking we should be outrageous in other ways too."
    mike.say "Like maybe you could say hi to me in a really sexy way?"
    mike.say "Edgy too - we should make it really edgy!"
    if minami.sub >= 70 or minami.is_sex_slave:
        show minami talkative
        minami.say "That's such a wild idea, big bro!"
        minami.say "We just HAVE to do it."
        show minami happy
        minami.say "And I can't wait to see the look on people's faces when we do!"
        $ minami.flags.submissive_interact = True
    else:
        show minami whining
        minami.say "I don't know, big bro..."
        minami.say "I'm still getting used to the idea of being more than your adopted sister."
        minami.say "I don't think I'm ready for that kind of thing."
        show minami sad
        mike.say "Okay, Minami - let's forget about it for now."
        $ minami.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
