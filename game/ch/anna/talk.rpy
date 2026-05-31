label anna_talk_love_male:
    mike.say "I guess it's kind of a cliche - but what's your take on love, Anna?"
    show anna happy
    if anna.is_visibly_pregnant:
        anna.say "Of course I believe in love - how couldn't I with our baby growing inside of me?"
    else:
        anna.say "I think love is all around you - ha, there's another cliche!"
        anna.say "Seriously though, you should be able to love whoever you choose."
    $ anna.love += 1
    hide anna
    return

label anna_talk_sex_male:
    mike.say "You're a modern kind of girl, Anna - you're liberated when it comes to sex, right?"
    show anna
    if anna.is_visibly_pregnant:
        "Anna's face shows a comically exaggerated amount of concern and gravity."
        anna.say "It's such a shame that the baby means my pussy's out of bounds for a while."
        show anna wink
        anna.say "Ah well - I guess you'll just have to find somewhere else to fuck me!"
    elif anna.love < 40:
        show anna blush
        "Anna blushes and refuses to meet my eye."
        anna.say "I don't think I know you well enough to feel comfortable talking about it."
        $ anna.love -= 1
    elif anna.love < 80:
        show anna happy
        "Anna smiles and raises her eyebrows."
        anna.say "Oh yeah - my last serious partner was a girl...I swing both ways!"
    elif anna.love < 120:
        show anna happy
        "Anna smiles, a little glimmer of naughtiness showing in her eyes as she does so."
        anna.say "Well, I'm not exactly what you'd call conservative..."
        show anna wink
        "She adds in a whisper."
        anna.say "I kinda like it up the butt!"
        $ anna.sub += 1
    else:
        "Anna looks both ways to check that no one else is listening."
        show anna blush
        anna.say "Don't tell anyone...but I kind of prefer it in the butt."
        $ anna.sub += 1
    hide anna
    return

label anna_talk_politics_male:
    mike.say "Who's gonna get your vote the next time the elections come round, Anna?"
    show anna annoyed
    if anna.is_visibly_pregnant:
        anna.say "I used to just think that they were all shits."
        anna.say "But now that we're going to be parents, I'm scared for our kid's future with them running things."
    else:
        "Anna crosses her arms over her considerable chest and frowns."
        anna.say "They're all the same - just out to fuck us, and not in the good way, either!"
    hide anna
    return

label anna_talk_food_male:
    mike.say "I just can't think of what I want to eat tonight - how about you, Anna?"
    show anna
    if anna.is_visibly_pregnant:
        anna.say "Erm, I think the cravings have started."
        show anna annoyed
        anna.say "I still want sushi, but now I can't have it without peanut butter or ice cream!"
    else:
        anna.say "I just love japanese food - sushi, ramen, whatever!"
        anna.say "It's all good!"
    hide anna
    return

label anna_talk_travels_male:
    mike.say "I'm tired of staring at the same four walls - wouldn't it be great to get away, Anna?"
    show anna
    if anna.is_visibly_pregnant:
        anna.say "I can't even walk across the street, my feet are so swollen!"
        "She flutters her eyelids at me, clearly wanting something."
        show anna wink
        anna.say "Will you give me a foot-rub, [hero.name]?"
    else:
        show anna blush
        "I can see the stars in Anna's eyes as she begins to daydream."
        anna.say "Oh, [hero.name] - wouldn't it be wonderful if the band went on a tour?"
    $ anna.love += 1
    hide anna
    return

label anna_talk_tv_male:
    show anna
    if "anna_event_01" in DONE and anna.love >= 60 and game.hour <= 18 and not "anna_event_02" in DONE and not anna.flags.horrorMovieDate:
        mike.say "Ah, Anna..."
        anna.say "Hmm...yeah, [hero.name]?"
        mike.say "How about you come around to my place and watch some horror movies {b}tonight{/b}?"
        anna.say "Sure!"
        mike.say "I have a pretty great TV and all that..."
        anna.say "Okay, sure!"
        mike.say "I mean, you don't have to say yes right away - or not at all, if you're not up for it!"
        show anna blush
        anna.say "Geez, [hero.name] - I said yes like twice already!"
        mike.say "Oh...okay...it's a date then?"
        $ anna.love += 1
        $ anna.flags.horrorMovieDate = True
    elif anna.is_visibly_pregnant:
        mike.say "I feel like chilling out and watching some TV - any recommendations, Anna?"
        anna.say "I used to be crazily into horror movies."
        show anna annoyed
        anna.say "But since we got pregnant, I just can't stomach them anymore."
    else:
        mike.say "I feel like chilling out and watching some TV - any recommendations, Anna?"
        anna.say "Oh, it has to be horror movies, all the way."
        show anna evil
        anna.say "The more likely to make me jump and scream, the better!"
        $ anna.sub += 1
    hide anna
    return

label anna_talk_sports_male:
    mike.say "There's just so much sport around these days, it kinda passes me by - how about you, Anna?"
    show anna
    if anna.is_visibly_pregnant:
        anna.say "I can't even see my toes right now, [hero.name], never mind touch them!"
    else:
        show anna annoyed
        "Anna wrinkles her nose in apparent distaste for the subject."
        anna.say "Eww, no - I hate sports, and I am so not into jocks..."
        $ anna.love -= 1
    hide anna
    return

label anna_talk_fashion_male:
    mike.say "You never seem to be interested in the latest fashions, Anna."
    show anna
    if anna.is_visibly_pregnant:
        anna.say "I saw these really cool maternity tops with band logos on them the other day!"
    else:
        anna.say "I believe that fashion is a statement of who you are and what you think."
        show anna angry
        anna.say "If you follow the herd, you're pretty much saying you're a sheep."
        $ anna.love -= 1
    hide anna
    return

label anna_talk_books_male:
    mike.say "I've never seen you with a book, Anna - do you read much?"
    show anna
    if anna.is_visibly_pregnant:
        anna.say "I try to read in bed at night."
        anna.say "But I'm usually so burnt out that I fall straight to sleep."
    else:
        show anna happy
        anna.say "Oh yeah, I just don't carry books around with me all the time."
        anna.say "I love reading philosophy, Spinoza is my favorite right now."
        $ anna.love += 1
    hide anna
    return

label anna_talk_people_male:
    mike.say "Is it just me, Anna, or are most of the people in the world assholes?"
    show anna
    "Anna frowns a little at my comment."
    if anna.is_visibly_pregnant:
        anna.say "I used to think that people were basically good."
        anna.say "But now I have the baby to worry about, I keep seeing the worst in everyone."
    else:
        show anna angry
        $ anna.love -= 1
        anna.say "Hey, [hero.name], that's a pretty negative thing to think!"
        anna.say "I think that everyone is basically good deep down, they just hide it well."
    hide anna
    return

label anna_talk_computers_male:
    mike.say "I just got a new laptop - are you into computers, Anna?"
    show anna
    anna.say "Oh no - I am not good with computers!"
    show anna annoyed
    anna.say "It's like they know it too, and hold some kind of grudge against me."
    hide anna
    return

label anna_talk_music_male:
    show anna
    anna.say "I LOVE music, what's your favorite band?"
    menu:
        "Disrupted":
            mike.say "Disrupted are probably right up there, maybe my favourite."
            show anna blush
            anna.say "Oh my god, David Draiman is so hot!"
            $ anna.sub += 1
        "One and a half direction":
            mike.say "One and a half direction of course - what else!"
            show anna annoyed
            anna.say "Eww...sorry I asked!"
            $ anna.love -= 1
        "Tendancious B":
            mike.say "And blasting forth with three part harmony!"
            mike.say "Tendancious B of course."
            show anna happy
            anna.say "Oh man they are so funny - I nearly pissed myself the first time I heard that album, honestly."
            $ anna.love += 1
        "Metallikea" if hero.has_skill("guitar"):
            mike.say "Metallikea - no one else even comes close."
            show anna blush
            anna.say "Best...metal...band...ever!"
            anna.say "Up to the Black album, at least."
            mike.say "I don't know - I have a soft spot for some of the tracks off of Load and Re-Load..."
            show anna evil
            "Anna looks at me with an expression of mock outrage, grinning all the same."
            $ anna.love += 1
            $ anna.sub += 1
    hide anna
    return

label anna_talk_birthday_male:
    show anna
    mike.say "Hey - Happy birthday Anna!"
    show anna happy
    anna.say "Aw, thanks [hero.name] - you remembered!"
    $ anna.love += 1
    hide anna
    return

init python:
    SpecificTalkSubject(**{
    "name": "anna_talk_kleio",
    "display_name": "About Kleio",
    "label": "anna_talk_kleio",
    "duration": 0,
    "icon": "button_kleio",
    "conditions": [
        IsDone("anna_event_06", "kleio_talk_anna"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(anna,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label anna_talk_kleio:
    "As much as I try to put the matter out of my mind, I still find myself dwelling on Anna's argument with Kleio."
    "Don't judge me too harshly on this one, but Kleio does actually have a point."
    "Sure, she'll have been as subtle as a donkey's dick when she came to make it."
    "But Anna is pretty meek and doesn't stand up for herself when it comes to a fight."
    "So the irony is that this probably won't get sorted for the very reason Kleio laid into her to begin with."

    anna.say "Uh...hey, [hero.name]."
    mike.say "Hey, Anna."
    mike.say "Did you manage to have it out with Kleio yet?"
    "There's a pregnant pause on the other end of the line."
    "And then Anna speaks in a weary tone of voice."
    show anna annoyed
    anna.say "No..."
    anna.say "No, I didn't."
    mike.say "Okay, Anna, we need to talk about this."
    anna.say "Do you mean..."
    anna.say "Is this one of those intervention things?"
    mike.say "Let's not get too dramatic, Anna."
    mike.say "I just think we need to talk, that's all."
    "I hear Anna sigh heavily."



    anna.say "Okay..."


    anna.say "Let's get it over with..."
    mike.say "Don't be like that, Anna."
    mike.say "I know how important your friendship with Kleio really is to you."
    if not Harem.together(anna, kleio):
        mike.say "And you can't have stayed friends this long if there wasn't something in it too."
        mike.say "I mean you're in a band together, for god's sake."
        mike.say "This can't be the first time that you've clashed like this, can it?"
        "Anna looks away at this, either unwilling or unable to meet my eye."
        mike.say "Come on, Anna..."
        show anna normal
        anna.say "Okay, I admit it."
        anna.say "We've fallen out before."
        anna.say "But..."
        mike.say "But what, Anna?"
        show anna annoyed
        "Anna makes a frustrated sound at this."
        "Actually shaking her head and stamping her feet as well."
        anna.say "Okay, okay..."
        anna.say "But before I didn't have you to tell about it, [hero.name]."
        "It takes me a couple of seconds to make sense of this admission."
        "But then I have to shake my own head before I can reply."
        mike.say "Anna, are you actually saying what I think you're saying?"
        mike.say "That you haven't tried to patch things up with Kleio because of me?"
        mike.say "Because you've been liking the sympathy?"
        anna.say "I'm so sorry, [hero.name]!"
        show anna blush
        anna.say "You have to understand - no one else listens to me!"
        anna.say "All Sasha does is tell me to grow a pair!"
        "I sigh in frustration, but then I can't help starting to laugh."
        "The whole thing just sounds so ridiculous now that I've dug down to the bottom of it."
        "It's just a storm in a teacup, and Anna is getting off on my being a shoulder to cry on."
        mike.say "Okay, Anna - I'm calling time on this thing."
        mike.say "You and Kleio need to get together and have it out."
        mike.say "And if you don't, then I really am going to be mad at you."
        show anna normal
        "Anna looks down at her feet again, nodding like a scolded child."
        anna.say "Okay, [hero.name]."
        anna.say "I'll call her right now."
        "I nod at this, hoping that I've prodded Anna into doing the right thing."
    else:
        $ anna.love += 5
        mike.say "It's important to me too."
        mike.say "And so is the relationship that we all have together."
        mike.say "I don't want to see that ruined over a silly little argument."
        show anna blush
        "Anna looks away at this, suddenly unwilling to meet my eye."
        "But I can see her cheeks colouring, letting me know I've hit a nerve."
        mike.say "Come on, Anna."
        mike.say "I don't want to lose the two of you."
        "Suddenly, Anna turns around again."
        show anna cry -blush
        "And I can see the beginning of tears in the corner of her eyes."
        anna.say "Oh, [hero.name]..."
        anna.say "I'm so sorry!"
        "The apology catches me off guard, as I hadn't been expecting it."
        mike.say "It's okay, Anna."
        mike.say "But don't you think Kleio's the one you should be apologising to?"
        "At this, Anna shakes her head and starts to make a little wailing sound."
        anna.say "No, [hero.name], you don't understand."
        anna.say "I wasn't angry at Kleio - I was jealous!"
        mike.say "What do you mean, Anna?"
        mike.say "What made you jealous of her?"
        "Tears are running down Anna's face as she starts to spill her guts."
        anna.say "When Kleio said I was shy and meek, it made me scared."
        anna.say "Scared that you'd get tired of me."
        anna.say "And that you'd like her more..."
        "So that's what this argument and the fallout is really about."
        "Anna thought that Kleio and I were going to get tired of her."
        mike.say "So you told me all about it for the sympathy, am I right?"
        "Anna nods sadly, sniffling the whole time."
        mike.say "Anna, I adore you every bit as much as I do Kleio."
        show anna normal
        anna.say "R...really?"
        mike.say "Really."
        mike.say "You're like sugar and spice, sweet and sour."
        show anna blush
        "Anna can't help giggling at this, wiping away the tears in her eyes."
        anna.say "And Kleio's sour, right?"
        mike.say "What do you think?"
        show anna happy
        "Anna giggles again, nodding happily."
        mike.say "So you'll talk to Kleio?"
        show anna normal
        "Anna nods again."
        "And I nod too, hoping that I've saying what I think you're saying?"
    $ anna.love += 5
    hide anna
    return

init:
    define nickname_superstar = ["Superstar", "superstar"]

label command_nickname_anna:
    menu:

        "Call me Superstar" if active_girl.flags.mikeNickname not in nickname_superstar and game.flags.band_reputation >= 100:
            $ active_girl.flags.mikeNickname = "Superstar"
        "Stop calling me Superstar" if active_girl.flags.mikeNickname in nickname_superstar:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_anna_male:
    mike.say "Hey, Anna..."
    show anna talkative
    anna.say "Yeah, [hero.name]?"
    show anna normal
    mike.say "You like it both ways, right?"
    mike.say "Front and back door too?"
    show anna happy
    anna.say "You know I do!"
    show anna normal
    mike.say "Well, how about you say so whenever you see me?"
    mike.say "How about you tell me how much you like it?"
    if anna.sub >= 70 or anna.is_sex_slave:
        show anna blush
        anna.say "Aww...[hero.name]!"
        anna.say "That's SO naughty of you."
        anna.say "But if that's what you want - sure, I'll do it!"
        $ anna.flags.submissive_interact = True
    else:
        show anna worried
        anna.say "Eww...[hero.name]!"
        anna.say "That's kinda gross."
        show anna sadsmile
        mike.say "Ah, yeah...I guess so, Anna."
        mike.say "Maybe we forget about that idea..."
        $ anna.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
