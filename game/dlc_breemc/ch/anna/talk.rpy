label anna_talk_love_female:
    show anna
    bree.say "You're always so positive and fun, Anna."
    bree.say "But have you ever really fallen in love?"
    if anna.is_visibly_pregnant:
        anna.say "Oh dear, [hero.name]..."
        anna.say "My head's such a mess since I got pregnant!"
        anna.say "I don't have time to think about things like that!"
    elif anna.love >= 50:
        anna.say "Of course I do, [hero.name]!"
        anna.say "What kind of a grouch wouldn't believe in love?!?"
    else:
        anna.say "Hey - what's that supposed to mean?!?"
        anna.say "I'm not some kind of lovey-duvy bimbo!"
    hide anna
    $ anna.love += 1
    return

label anna_talk_sex_female:
    show anna
    bree.say "Ah, Anna..."
    bree.say "[mike.name] always says that you're kind of...fun, you know?"
    bree.say "Fun in the bedroom kind of way?"
    if anna.is_visibly_pregnant:
        anna.say "Phew, [hero.name]!"
        anna.say "I might have been before I got pregnant."
        anna.say "But I don't think I will be again until afterwards!"
    elif anna.love < 40:
        anna.say "Hey - what are you trying to say?"
        anna.say "Did he tell you I was some kind of tramp?!?"
        $ anna.love -= 1
    elif anna.love < 120:
        anna.say "Oh yeah, I've got a reputation alright!"
        anna.say "They say I'm a regular firecracker!"
    else:
        anna.say "Oh yeah - I LOVE IT!"
        anna.say "I know I shouldn't say that, [hero.name]."
        anna.say "But I love having somebody inside of me!"
    $ anna.love += 1
    hide anna
    return

label anna_talk_politics_female:
    show anna
    bree.say "Huh...I don't know who to vote for, Anna!"
    bree.say "Everyone seems to be saying the same things in a different way!"
    anna.say "Bleugh!"
    anna.say "I don't understand all of that stuff."
    anna.say "So I just ignore it all, and that makes me happy!"
    hide anna
    return

label anna_talk_food_female:
    show anna
    bree.say "Ooh, Anna - I found this new flavour of ice-cream yesterday."
    bree.say "It totally blew me away and you have to try it!"
    anna.say "Really, [hero.name]?"
    anna.say "Have you got some of it with you?"
    anna.say "Because if you have, I want to try it right now!"
    hide anna
    return

label anna_talk_travels_female:
    show anna
    bree.say "I keep flicking through travel brochures all the time, Anna."
    bree.say "It's like, I know that I want to take a holiday real soon."
    bree.say "But I can't agree with myself on where I want to go!"
    if anna.is_visibly_pregnant:
        anna.say "Ooh, [hero.name]!"
        anna.say "I can't help you there!"
        anna.say "Moving any where's a chore for me with this massive belly!"
    else:
        anna.say "Meh..."
        anna.say "Going places is over-rated if you ask me!"
        anna.say "I wanna stay where all of my stuff is!"
    $ anna.love += 1
    hide anna
    return

label anna_talk_tv_female:
    show anna
    bree.say "Oh, I've got to get going!"
    bree.say "I want to get in as many episodes of my shows as I can tonight!"
    if anna.is_visibly_pregnant:
        anna.say "Oh, I can't stay awake to watch anything these days!"
        anna.say "I'm asleep and snoring as soon as I collapse onto the sofa..."
    if anna.sub >= 25:
        anna.say "Ooh...ooh..."
        anna.say "What are you watching?"
        anna.say "In fact, forget that - it doesn't matter!"
        anna.say "Can I come along too?!?"
    else:
        anna.say "Boo!"
        anna.say "Boring!"
        anna.say "No TV series is THAT great!"
    $ anna.sub += 1
    hide anna
    return

label anna_talk_sports_female:
    show anna
    bree.say "I actually watched some sports with [mike.name] the other night."
    bree.say "And well...it wasn't as bad as I thought it'd be, Anna!"
    bree.say "I think I might actually be able to get into it...eventually...!"
    anna.say "No, no, no, [hero.name]!"
    anna.say "That's how they get you!"
    anna.say "Watching sports let's them brainwash you!"
    anna.say "The next thing you know you're sitting in a stadium, chanting along with all the other zombies!"
    hide anna
    return

label anna_talk_fashion_female:
    show anna
    bree.say "I love the way you dress, Anna."
    bree.say "It really shows off your..."
    bree.say "Well...your assets - if you know what I mean!"
    anna.say "He, he, he..."
    anna.say "It's okay, [hero.name] - you can say you like my tits!"
    anna.say "I...I mean the way they look in this outfit!"
    hide anna
    return

label anna_talk_books_female:
    show anna
    bree.say "I just finished a great book, Anna."
    bree.say "It was so good - a total page-turner!"
    bree.say "You should SO borrow it and read it yourself."
    anna.say "Nah, [hero.name], I'm cool."
    anna.say "I'm really more of a comic-book girl anyway."
    anna.say "Sometimes I just like to look at the pictures!"
    hide anna
    return

label anna_talk_people_female:
    show anna
    bree.say "I'm not super-keen on socialising all the time, Anna."
    bree.say "But you don't seem to have that problem."
    bree.say "How in the hell do you manage it?"
    anna.say "Oh, it kinda comes naturally, [hero.name]."
    anna.say "And even if it doesn't, I just imagine everyone's naked!"
    anna.say "Well...I usually imagine everyone's naked anyway."
    anna.say "But EXTRA naked in that case!"
    hide anna
    return

label anna_talk_computers_female:
    show anna
    bree.say "Do you have a computer at home, Anna?"
    bree.say "I mean, you're a musician, right?"
    bree.say "So I see you with like a mixing studio on your desktop!"
    anna.say "Oh no...no way!"
    anna.say "I'm totally old-school!"
    anna.say "Plus, computers scare me a little..."
    hide anna
    return

label anna_talk_music_female:
    show anna
    bree.say "What in the hell is that sound?"
    anna.say "It's us - it's The Deathless Harpies!"
    anna.say "Don't we sound as heavy as fuck?!?"
    if anna.love >= 50:
        bree.say "Oh god!"
        bree.say "It's like there's a party in my ears - and everyone's invited!"
        bree.say "What are you waiting for, Anna, turn it up already!"
        anna.say "Oh yeah...I'm on it!"
        anna.say "I knew you had a great taste in music, [hero.name]!"
        $ anna.love += 1
    else:
        bree.say "Oh god!"
        bree.say "Turn it off - NOW!"
        bree.say "That sounds awful!"
        anna.say "Hey!"
        anna.say "There's no need to be so mean!"
        $ anna.love -= 1
    hide anna
    return

label anna_talk_birthday_female:
    show anna
    bree.say "Hey, Anna - Happy Birthday!"
    bree.say "And many happy returns too!"
    if anna.love >= 50:
        anna.say "Aw, thanks, [hero.name]!"
        anna.say "Nobody ever remembers my birthday!"
        $ anna.love += 1
    else:
        anna.say "Yeah, great - I'm a year older!"
        anna.say "Thanks for reminding me!"
        $ anna.love -= 1
    hide anna
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
