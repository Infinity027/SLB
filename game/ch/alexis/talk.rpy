init python:
    SpecificTalkSubject(**{
    "name": "alexis_talk_rape",
    "display_name": "About the rape",
    "label": "alexis_talk_rape",
    "duration": 0,
    "icon": "button_alexis",
    "conditions": [
        Not(IsDone("alexis_event_07a")),
        Not(IsDone("alexis_event_07b")),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(alexis,
            IsActive(),
            IsFlag("hired_PI", False),
            IsFlag("policestation", False),
            IsFlag("rapeConfession"),
            ),
        ],
    "do_once": True,
    })

label alexis_talk_rape:
    $ game.flags.hirePI -= 1
    $ alexis.flags.policestation = True
    show alexis
    "I've tried as best I can to come to terms with the revelation that Alexis didn't cheat on me out of choice."
    "And...shit, listen to me - I'm still making this whole thing sound like it's all about me!"
    "What I should be saying is that I'm struggling to come to terms with the awful knowledge that Alexis was raped back in high-school."
    "At first I was just shocked by the news, but then I got mad, wanted to take some kind of revenge on Coach Blank."
    "But what good would that do anyone?"
    "Beating him senseless in the here and now won't change what happened in the past."
    "Sure, it might make me feel good for a short while."
    "But it's not like I'd be doing it for Alexis, as she could have had asked someone to do it long before now."
    "And who knows if the bastard even remembers what he did and who he did it to?"
    "The idea of beating up some old fucker that's lost his memory doesn't exactly fill me with glee."
    "So the only two choices that I can see are keeping Alexis's secret, like she had for so long."
    "Or else going to the police and telling them the whole sorry, sordid story."
    "By the time I next see Alexis, I've spent so long thinking about my choice that I can't keep it in any longer."
    "Almost as soon as we start to talk to one another, I just blurt it out without preparation or preamble..."
    mike.say "Alexis, I know what you said."
    mike.say "And I know that I said I'd do what you said."
    mike.say "But what you said has been bugging me so much that I want to change what I said."
    show alexis confused
    alexis.say "Slow down, [hero.name]!"
    alexis.say "I don't know what the hell you're talking about!"
    "I force myself to stop, take a deep breath and think about what I'm saying."
    mike.say "Alexis...I think you should go to the police."
    show alexis close surprised at vshake
    alexis.say "WHAT?!?"
    mike.say "I think that you should go to the police about Blank, about what he did to you..."
    show alexis close angry
    alexis.say "Fuck sake, [hero.name] - I know WHAT you're talking about!"
    alexis.say "I mean is - what are you even thinking?!?"
    alexis.say "Didn't I say that I wanted you to drop this already?"
    "I hold up my hands to ward off the anger and annoyance that's almost radiating from Alexis right now."
    "There's probably a million and one better ways that I could have brought this up with her."
    "But I've said it now, and all I can do is try as best I can to salvage the situation."
    mike.say "I know, I know...and I'm sorry, okay?"
    mike.say "But just hear me out, Alexis, please?"
    show alexis b close annoyed
    "Alexis makes a frustrated grunting sound and crosses her arms over her chest."
    "And as that's as close as I'm likely to get to a yes from her any time soon, I take it as permission to keep on talking."
    mike.say "Just hear me out."
    mike.say "And if you don't like what I have to say, then I promise I'll never mention it again."
    "Alexis grunts again, but this time she rolls her eyes and shakes her head."
    "Which in her current mood is probably as good as written permission to continue."
    mike.say "Okay, answer me this, Alexis."
    mike.say "Why did you tell me about what Blank did to you now?"
    mike.say "You could have told me back when we were kids, but you didn't."
    mike.say "Why is that?"
    show alexis close sad
    "Alexis opens her mouth to speak, but then stops."
    "The expression on her face goes from sure to uncertain in a matter of seconds."
    alexis.say "I...I used to think it was because I was ashamed."
    alexis.say "That people wouldn't believe me and that they'd think I was a slut."
    alexis.say "That you'd think I was a slut..."
    mike.say "And what happened when you did tell me, Alexis?"
    mike.say "Did I think you were lying or...or a slut?"
    "Alexis lets out a nervous laugh as she shakes her head."
    alexis.say "No...of course not!"
    mike.say "Well, you were wrong about that for so many years."
    mike.say "Couldn't you have been wrong about this too?"
    "Alexis seems to be considering my words, and I think that I'm beginning to talk her round."
    "But then a stab of pain seems to flash in her eyes, and she shakes her head again."
    show alexis close annoyed
    alexis.say "But it's been so many years, [hero.name]."
    alexis.say "What if they ask why I didn't report it at the time?"
    mike.say "Have you seen the news lately, Alexis?"
    mike.say "You can't move for stories of Hollywood big-shots and politicians being on trial for this kind of stuff!"
    mike.say "Right now the police are digging up shit on people from the middle of the last century."
    mike.say "Trust me, if the press gets wind the cops round here are ignoring a case like yours, it'll be open season on them!"
    show alexis close sad
    "Alexis looks at me with an intensity in her eyes that tells me all I need to know."
    "I can see that she's considering the wisdom of my words, but that she's also scared of taking that first step."
    mike.say "Don't worry, Alexis."
    mike.say "I'll be with you every step of the way."
    show alexis close normal
    "At this, she smiles and clasps my hands in her own."
    alexis.say "Okay, [hero.name]."
    alexis.say "I wasn't sure about this - but you convinced me!"
    mike.say "That's great, Alexis."
    mike.say "We'll go down to the local station and ask to speak to someone as soon as we can!"
    "It's only now that the enormity of what I've talked Alexis into truly starts to hit home."
    "Whether they believe her and throw the book at Blank or dismiss her as an attention-seeking skank."
    "I've convinced her to open up a whole new can of worms!"
    return

label alexis_talk_love_male:
    show alexis
    mike.say "Do you even believe that love exists, Alexis?"
    alexis.say "People like to get all flowery and poetic about it."
    if alexis.is_visibly_pregnant:
        show alexis blush
        "Alexis puts her hands to her belly, her face showing a sudden surge of emotion."
        alexis.say "I didn't...but things like this can really change the way you look at things."
        $ alexis.love += 1
    elif alexis.love >= 50:
        show alexis blush
        alexis.say "I'd like to - but sometimes life makes you lose faith in happy endings."
        $ alexis.love += 1
    else:
        show alexis sad
        alexis.say "But they all really know it's really just a matter of getting what you want."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_sex_male:
    show alexis
    mike.say "What's sex all about for you, Alexis?"
    if alexis.is_visibly_pregnant:
        alexis.say "I used to think that sex was just a weapon that I could use against people."
        alexis.say "But now I can see how wrong I was..."
    elif alexis.love >= 50:
        alexis.say "You can use it as a tool...or like a weapon."
        show alexis blush
        alexis.say "To defend yourself or lash out at people..."
        $ alexis.sub += 1
    else:
        alexis.say "It's a transaction between two people, just like any other."
        alexis.say "I have something they want, so they have to offer me something in return."
    hide alexis
    return

label alexis_talk_politics_male:
    show alexis
    mike.say "Alexis, do you have a political stance?"
    if alexis.is_visibly_pregnant:
        alexis.say "I never really engaged with politics before now."
        alexis.say "But with a kid on the way, I keep finding it pressing on my mind all the more."
    elif alexis.love >= 50:
        show alexis sad
        alexis.say "I find it hard to trust most people...so how can I trust a damn politician?"
    else:
        show alexis happy
        alexis.say "I'm a Libertarian - I believe in survival of the fittest, every man or woman for themselves."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_food_male:
    show alexis
    mike.say "Any special dietary requirements, Alexis?"
    if alexis.is_visibly_pregnant:
        show alexis happy
        alexis.say "I used to be real picky - but now I seem to want to eat anything put in front of me!"
        $ alexis.love += 1
    elif alexis.love >= 50:
        alexis.say "I've spent so long eating what I think people should believe I like..."
        show alexis confused
        alexis.say "I feel as though I don't remember what I really do like anymore."
        $ alexis.love += 1
    else:
        alexis.say "None - so long as it's up to my standards."
        alexis.say "Let's just say I won't be taken anywhere with less than four stars."
    hide alexis
    return

label alexis_talk_travels_male:
    show alexis
    mike.say "I think I have enough stashed away for a foreign holiday this year - any tips, Alexis?"
    if alexis.is_visibly_pregnant:
        alexis.say "Don't ask me - I can't go too far afield in this condition!"
    elif alexis.love >= 50:
        show alexis blush
        alexis.say "All I really want is to be alone somewhere quiet...with someone that loves me."
        $ alexis.love += 1
    else:
        alexis.say "You need to book somewhere that's exclusive and fashionable."
        alexis.say "And not let the expense put you off making a real statement."
    hide alexis
    return

label alexis_talk_tv_male:
    show alexis
    mike.say "I'm not watching anything on TV right now, how about recommending something, Alexis?"
    if alexis.is_visibly_pregnant:
        alexis.say "I have the same problem now that I can't get out as much."
        show alexis flirt
        alexis.say "Maybe we could find something to watch together?"
        $ alexis.love += 1
    elif alexis.love >= 50:
        show alexis sad
        alexis.say "I used to always end up watching TV alone...it still reminds me of being so lonely."
        $ alexis.love -= 1
    else:
        alexis.say "I don't watch too much TV...I have better things to do with my time."
    hide alexis
    return

label alexis_talk_sports_male:
    show alexis
    mike.say "You were always quite keen on sports, Alexis - or at least the sporting type when it came to guys..."
    mike.say "Did you keep that up after we left school?"
    if alexis.is_visibly_pregnant:
        alexis.say "[hero.name], seriously - I already look like a football and I'm getting kicked all the time."
        alexis.say "The last thing I want is to watch a real one being kicked around!"
    elif alexis.love >= 50:
        show alexis angry
        alexis.say "I really don't like sports and I don't want to talk about it!"
        alexis.say "It's not a good subject for me...please let's talk about something else?"
        $ alexis.love -= 2
    else:
        show alexis angry
        alexis.say "No...no, I didn't."
        alexis.say "I don't...it's not something I want to talk about."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_fashion_male:
    show alexis
    mike.say "I don't think I've seen you in the same outfit twice, Alexis."
    mike.say "How can you afford it?"
    if alexis.is_visibly_pregnant:
        alexis.say "Nothing fits me anymore."
        alexis.say "At one time it would have bothered me - but now I have bigger things to worry about."
    elif alexis.love >= 50:
        alexis.say "I've always used clothes kind of like armour...like a shield."
        alexis.say "If people only see your clothes, they tend to ignore the person beneath them..."
    else:
        alexis.say "I've never been shy of accepting genuine generosity from an admirer."
        show alexis happy
        alexis.say "If you value yourself, others will see value in you too."
        $ alexis.love += 1
    hide alexis
    return

label alexis_talk_books_male:
    mike.say "What's on your bookshelf, Alexis?"
    show alexis
    if alexis.is_visibly_pregnant:
        alexis.say "Just stuff on caring for the baby."
    elif alexis.love >= 50:
        alexis.say "I read a lot of stuff to try and help with my demons."
        show alexis sad
        alexis.say "Sometimes it helps - but not always..."
        $ alexis.love += 1
    else:
        alexis.say "I don't have time for fiction."
        alexis.say "Most of what I read is self-help and books on psychology."
    hide alexis
    return

label alexis_talk_people_male:
    show alexis
    mike.say "You have a general philosophy for dealing with other people, Alexis?"
    if alexis.is_visibly_pregnant:
        alexis.say "I hope there really are good people in the world, for the baby's sake."
    elif alexis.love >= 50:
        show alexis sad
        alexis.say "When people hurt me in the past, I always pushed them away."
        show alexis normal
        alexis.say "In the end I started doing the same to people that didn't want to hurt me too."
        show alexis blush
        alexis.say "Maybe, with your help, I can break that cycle?"
        $ alexis.love += 1
    else:
        alexis.say "People are basically shit - you need to keep that in mind in order to get what you want out of them."
    hide alexis
    return

label alexis_talk_computers_male:
    show alexis
    mike.say "Alexis - are you up to speed with computers, the internet and all that stuff?"
    if alexis.is_visibly_pregnant:
        alexis.say "No, but I figure I can just wait for the baby to get a bit older and then start educating me."
    elif alexis.love >= 50:
        alexis.say "I know as much as anyone - but I'm no computer expert!"
    else:
        show alexis annoyed
        alexis.say "I know as much as I need to know in order to get by."
        alexis.say "And that's about all I care to know too."
        $ alexis.love -= 1
    hide alexis
    return

label alexis_talk_music_male:
    show alexis
    mike.say "Have you got a playlist of your favourite music, Alexis?"
    if alexis.is_visibly_pregnant:
        alexis.say "I want to listen to something soothing - I don't care what!"
    elif alexis.love >= 50:
        alexis.say "I've spent so long liking things to make people like me that I can't remember what I like for real!"
    else:
        alexis.say "No, but I like to have the latest tech to play it on."
    hide alexis
    return

label alexis_talk_birthday_male:
    show alexis
    mike.say "Happy birthday, Alexis!"
    if alexis.love >= 50:
        show alexis surprised
        alexis.say "Oh, [hero.name] - you're the only person that remembered!"
        show alexis happy
        alexis.say "And that's the best gift I can imagine."
        $ alexis.love += 1
    else:
        alexis.say "Ah, how sweet of you to remember!"
        alexis.say "Now, what did you get for me?"
    hide alexis
    return

init:
    define nickname_wallet = ["Wallet", "wallet"]
    define nickname_cuck = ["Cuck", "cuck"]
    define nickname_dark_knight = ["Dark knight", "dark knight", "Dark Knight", "dark Knight"]

label command_nickname_alexis:
    menu:

        "Call me Wallet" if active_girl.flags.mikeNickname not in nickname_wallet and hero.money > 10000:
            $ active_girl.flags.mikeNickname = "Wallet"
        "Stop calling me Wallet" if active_girl.flags.mikeNickname in nickname_wallet:
            $ active_girl.flags.mikeNickname = None


        "Call me Cuck" if active_girl.flags.mikeNickname not in nickname_cuck and active_girl.flags.cheatokay:
            $ active_girl.flags.mikeNickname = "Cuck"
        "Stop calling me Cuck" if active_girl.flags.mikeNickname in nickname_cuck:
            $ active_girl.flags.mikeNickname = None


        "Call me Dark knight" if active_girl.flags.mikeNickname not in nickname_dark_knight and active_girl.flags.coachVictory == True:
            $ active_girl.flags.mikeNickname = "Dark knight"
        "Stop calling me Dark knight" if active_girl.flags.mikeNickname in nickname_dark_knight:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_alexis_male:
    mike.say "Alexis, I was thinking..."
    mike.say "You like my cock, right?"
    show alexis happy at startle
    "Alexis giggles at the strangeness of the question."
    show alexis smile
    alexis.say "Yeah, [hero.name] - I guess so!"
    show alexis normal
    mike.say "Well...I was thinking you could say so."
    mike.say "Say how much you want it inside of you?"
    mike.say "Whenever you greet me?"
    if alexis.sub >= 70 or alexis.is_sex_slave:
        show alexis talkative blush
        alexis.say "If...if that's what you'd like, [hero.name]."
        show alexis smile
        alexis.say "Of course I could."
        alexis.say "Every time I see you I'll tell you how much I want it!"
        $ alexis.flags.submissive_interact = True
    else:
        show alexis whining
        alexis.say "Erm...I don't think so, [hero.name]."
        alexis.say "I mean, I DO like it - but not that much!"
        show alexis sadsmile
        mike.say "Okay, Alexis - it was just an idea anyway..."
        $ alexis.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
