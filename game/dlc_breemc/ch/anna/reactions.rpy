label anna_ask_birthday_female:
    bree.say "What's the date of your birthday, Anna?"
    bree.say "I always like to know when someone's birthday is and write it down."
    bree.say "I'm such a scatter-brain that I'll forget it if I don't!"
    if hero.charm >= 40 - anna.love:
        $ mike.flags.birthdayknown = True
        anna.say "I know what you mean, [hero.name]!"
        anna.say "I'm pretty forgetful too."
        anna.say "It's Summer 26."
    else:
        anna.say "What's up with that, [hero.name]?"
        anna.say "Are you trying to make me feel old or something?"
        anna.say "You should be ashamed of yourself!"
        $ anna.sub -= 1
        $ anna.love -= 1
    return

label anna_ice_cream_reaction_female:
    bree.say "Hey, Anna..."
    bree.say "Let's grab an ice-cream!"
    anna.say "Oh yeah, [hero.name]!"
    anna.say "That's a great idea."
    "Anna and I hurry over to the ice-cream stand and make our orders."
    "I have my usual, but I watch as Anna's order goes on and on."
    "She seems to be adding almost every topping and extra they have!"
    anna.say "Don't forget the syrup."
    anna.say "Oh, and some of those sprinkles too!"
    "Once she has the thing in her hand, Anna's positively beaming."
    "But I'm worried that the whole thing is going to topple over."
    "Nevertheless, she starts licking away and somehow handles it."
    "And it strikes me that the ice-cream is a little like Anna herself."
    "Small and yet packed full of so much stuff its incredible."
    "You think it won't work, but oddly it does."
    anna.say "What's up, [hero.name]?"
    anna.say "You're not eating your ice-cream."
    bree.say "Oh...I was just taking my time, Anna."
    bree.say "Don't want to get brain-freeze."
    bree.say "And by the way, you have ice-cream on the end of your nose!"
    anna.say "Really?"
    anna.say "Oh, damn it!"
    return

label anna_ask_phone_female:
    bree.say "You wanna swap phone numbers, Anna?"
    bree.say "That way we can get in contact whenever we want."
    bree.say "No need to ask [mike.name] or Sasha to pass on a message!"
    if hero.charm >= 20 - anna.love:
        show anna happy
        $ hero.smartphone_contacts.append("anna")
        anna.say "Good idea, [hero.name]!"
        anna.say "Waiting on those guys really sucks."
        anna.say "Plus I don't want them to hear what I have to say to you!"
        anna.say "Here's my number - now where's yours?"
    else:
        show anna annoyed
        $ anna.sub -= 1
        $ anna.love -= 1
        anna.say "Oh, [hero.name]!"
        anna.say "I know I told you that already."
        anna.say "And I'm not telling you again!"
    return

label anna_offer_a_drink_female:
    bree.say "I was just going to grab a drink from the bar, Anna."
    bree.say "Would you like me to get you one too?"
    bree.say "It's no trouble."
    if (hero.charm >= 60 - anna.love and anna.flags.drinks < 2) or date_girl == anna:
        show anna happy
        anna.say "Ooh..."
        anna.say "I have nearly finished this one."
        anna.say "Okay, [hero.name] - grab me another."
        anna.say "And thanks for thinking of me too!"
        hide anna
        show drink anna
        if anna.love <= 25:
            $ anna.love += 1
        elif date_girl == anna and game.active_date:
            $ game.active_date.score += 5
        call expression anna.get_chat from _call_expression_388
        hide drink anna
        $ anna.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show anna annoyed
        anna.say "Oh no, [hero.name]..."
        anna.say "I haven't finished this one yet."
        anna.say "Wait a minute..."
        anna.say "You're not trying to get me drunk, are you?"
        $ hero.cancel_activity()
        hide anna
    return

label anna_slap_ass_intro_female:
    "As Anna walks past me, I catch sight of her cute little butt."
    "I know, I know - it's not the first time I ever noticed it."
    "But for some reason it just kind of has an effect on me."
    "I can't take my eyes off it and I know that I want it bad!"
    "So before common sense can intervene, I find myself acting."
    "My arm swings and my hand connects with Anna's ass."
    "She yelps and jumps a little way forwards."
    "Then she turns and looks at me, confusion on her face."
    anna.say "[hero.name]!"
    anna.say "You slapped my butt!"
    bree.say "Ah, yeah, Anna..."
    bree.say "I guess I did!"
    return

label anna_slap_ass_happy_female:
    "To my great relief, Anna's face breaks into a smile."
    anna.say "I guess it must look pretty good then!"
    "She makes a point of shaking her backside at me."
    "And then she giggles, which only makes her cuter still."
    return

label anna_slap_ass_angry_female:
    "Anna frowns, crossing her arms over her chest."
    anna.say "[hero.name], that is NOT okay!"
    anna.say "You can't just go round slapping people's butts!"
    anna.say "So don't you ever do that again, you hear?"
    bree.say "Ah...yeah, Anna...I hear you."
    return

label anna_breakup_female:
    bree.say "Anna..."
    bree.say "There's no easy way to say this..."
    bree.say "So I'm just going to come right out and say it."
    "Anna looks at me with wide eyes and a worried expression."
    anna.say "Oh, [hero.name]!"
    anna.say "I don't like the sound of this..."
    bree.say "Yeah, yeah..."
    bree.say "It's us, Anna - I don't think it's working out."
    bree.say "In fact, I think we need to call it a day."
    bree.say "And we should do it now, while we can still come out of it friends."
    anna.say "You...you really think that, [hero.name]?"
    anna.say "I guess we're over then!"
    return

label anna_go_steady_intro_female:
    bree.say "Hey, Anna..."
    bree.say "I've been thinking..."
    "Anna smiles and lets out a playful chuckle."
    anna.say "Oh no!"
    anna.say "That's never a good sign, [hero.name]!"
    bree.say "Anna!"
    bree.say "I'm being serious here!"
    bree.say "I was thinking that we get on well, right?"
    bree.say "I mean, we've been having a good time together."
    bree.say "So why don't we kind of...make it official?"
    anna.say "Oh..."
    anna.say "You mean like go steady?"
    bree.say "Yeah, Anna - that's exactly what I mean."
    return

label anna_go_steady_yes_female:
    anna.say "Why didn't you just come out and say that, [hero.name]?"
    anna.say "Of course we should go steady."
    anna.say "That's a great idea!"
    return

label anna_go_steady_no_female:
    anna.say "Oh no, [hero.name]!"
    anna.say "We can't make it official, not yet."
    anna.say "That's just like tempting fate, you know?"
    anna.say "Like we're asking things to go wrong!"
    return

label anna_pet_intro_female:
    "Anna just looks so adorably cute today, I could just eat her up!"
    "In fact, as she walks past me, I can't resist patting her on the head."
    "It's just a light tap, a show of the affection that I feel for her."
    "But the moment I do it, Anna stops on the spot, looking confused."
    "She glances upwards and then looks me straight in the eye."
    anna.say "[hero.name]!"
    anna.say "You slapped you patted me on the head!"
    bree.say "Ah, yeah, Anna..."
    bree.say "I guess I did!"
    return

label anna_pet_happy_female:
    "Anna's face breaks into a smile as she shakes her head."
    anna.say "You're only doing that because I'm short!"
    anna.say "You just wait, [hero.name] - I'll get you back somehow!"
    return

label anna_pet_annoyed_female:
    "Anna frowns, crossing her arms over her chest."
    anna.say "[hero.name], that is NOT okay!"
    anna.say "You can't just go round patting people on the head!"
    anna.say "And it's not okay to exploit the vertically-challenged either!"
    anna.say "So don't you ever do that again, you hear?"
    bree.say "Ah...yeah, Anna...I hear you."
    return

label anna_massage_intro_female:
    anna.say "Ow, ow, ow, ow!"
    anna.say "Ooh...ouch!"
    bree.say "Oh, Anna..."
    bree.say "I felt that!"
    anna.say "Yeah...I pulled a muscle at band practice!"
    anna.say "And it hurts real bad, [hero.name]!"
    bree.say "You want me to give you a massage?"
    bree.say "I'm told I'm pretty good, and it might help ease the pain."
    return

label anna_massage_accept_female:
    anna.say "Would you, [hero.name]?"
    anna.say "I need some help!"
    anna.say "I'd be really grateful if you could!"
    return

label anna_massage_refuse_female:
    anna.say "No, no, no..."
    anna.say "I already got burned like that the last time!"
    anna.say "Kleio once gave me what she claimed was a massage."
    anna.say "And it was more like being beaten up!"
    return

label anna_piercing_nipples_reaction_female:
    "Anna's smiling as she walks up to me, like she's got something to show off."
    "But then I notice that she's thrusting her chest out in front of her too."
    "And a closer inspection reveals just what that something actually is."
    bree.say "Whoa, Anna!"
    bree.say "You had them pierced?"
    anna.say "Oh yeah, [hero.name] - both of them!"
    anna.say "What do you think?"
    "I shake my head, fascinated by the sight of Anna's breasts."
    bree.say "They're great, Anna - so sexy!"
    "Anna nods and giggles, happy with my compliments."
    anna.say "They sure are, [hero.name]."
    anna.say "And they make me feel pretty sexy too!"
    return

label anna_piercing_navel_reaction_female:
    "Anna's smiling as she walks up to me, like she's got something to show off."
    "But then I notice that she's thrusting her stomach out in front of her too."
    "And a closer inspection reveals just what that something actually is."
    bree.say "Whoa, Anna!"
    bree.say "You had it pierced?"
    anna.say "Oh yeah, [hero.name] - I finally did it!"
    anna.say "What do you think?"
    "I shake my head, fascinated by the sight of Anna's belly button."
    bree.say "It's great, Anna - so sexy!"
    "Anna nods and giggles, happy with my compliments."
    anna.say "It sure is, [hero.name]."
    anna.say "And it makes me feel pretty sexy too!"
    return

label anna_piercing_clit_reaction_female:
    "Anna's smiling as she walks up to me, like she's got something to show off."
    "But then I notice that she's thrusting her crotch out in front of her too."
    "Which gives me a pretty good clue as to what she's so pleased with."
    bree.say "Whoa, Anna!"
    bree.say "You had it pierced?"
    anna.say "Oh yeah, [hero.name] - I finally did it!"
    anna.say "I got my clit done!"
    anna.say "What do you think?"
    "I shake my head, already picturing what it must look like."
    bree.say "It sounds great, Anna - so sexy!"
    "Anna nods and giggles, happy with my compliments."
    anna.say "It sure is, [hero.name]."
    anna.say "And it makes me feel pretty sexy too!"
    return

label anna_piercing_head_reaction_female:
    "Anna's smiling as she walks up to me, like she's got something to show off."
    "But then she sticks her tongue out at me."
    "And a closer inspection reveals just what that something actually is."
    bree.say "Whoa, Anna!"
    bree.say "You had it pierced?"
    anna.say "Oh yeah, [hero.name] - I finally did it!"
    anna.say "What do you think?"
    "I shake my head, fascinated by the sight of Anna's tongue piercing."
    bree.say "It's great, Anna - so sexy!"
    "Anna nods and giggles, happy with my compliments."
    anna.say "It sure is, [hero.name]."
    anna.say "And it makes me feel pretty sexy too!"
    return

label anna_movie_liked_reaction_female:
    bree.say "That movie was pretty amazing!"
    bree.say "Right, Anna?"
    bree.say "I made the right call wanting to see it."
    anna.say "You sure did, [hero.name]!"
    anna.say "I wasn't sure it'd be decent, but it was great!"
    anna.say "You should always pick the film we see from now on."
    return

label anna_movie_indifferent_reaction_female:
    bree.say "That movie was pretty amazing!"
    bree.say "Right, Anna?"
    bree.say "I made the right call wanting to see it."
    anna.say "Hmm..."
    anna.say "I guess it was okay, [hero.name]."
    anna.say "But I still wonder what the one I wanted to see was like..."
    return

label anna_movie_disliked_reaction_female:
    bree.say "That movie was pretty amazing!"
    bree.say "Right, Anna?"
    bree.say "I made the right call wanting to see it."
    anna.say "Eww...no way, [hero.name]!"
    anna.say "That movie was a real stinker!"
    anna.say "I just knew we should have seen the one I wanted to see instead."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
