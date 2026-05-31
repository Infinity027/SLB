label palla_talk_love_male:
    show palla
    call palla_chat_love_male from _call_palla_chat_love
    hide palla
    return

label palla_talk_sex_male:
    show palla
    call palla_chat_sex_male from _call_palla_chat_sex
    hide palla
    return

label palla_talk_politics_male:
    show palla
    $ renpy.dynamic("result")
    $ result = randint(1, 3)
    if result == 1:
        show palla angry
        palla.say "Ugh, politics. Democrats, Republicans, Libertarians. They're all just selfish assholes that'd sell their own mother for a vote."
        "Palla points at herself with both thumbs."
        show palla happy
        palla.say "Vote for me, I got tits! At least when I screw you it'll feel good."
        palla.say "At least until I rip your dick off."
        mike.say "Damn, Palla. Just. Damn."
    elif result == 2:
        show palla angry
        palla.say "I don't vote, there's no point. One guy wants to take 70%% of my taxes, the other one wants to kill the whales and the forests so his buddies can make a buck."
        palla.say "Fuck 'em all."
        show palla happy
        mike.say "I wish I could disagree with you."
    else:
        show palla angry
        palla.say "Ugh. Global warming, hurricanes, war in the middle east, politicians selling off our country to evil billionaires to make a buck."
        palla.say "I can't pay attention to any of it, I'd be depressed all day."
        show palla happy
        palla.say "I'd rather go dancing."
        mike.say "I vote for dancing."
        palla.say "I see what you did there, [hero.name]."
    $ palla.love += 1
    hide palla
    return

label palla_talk_food_male:
    show palla
    $ renpy.dynamic("result")
    $ result = randint(1, 3)
    if result == 1:
        palla.say "I miss candy. I can't eat more than fifteen hundred calories a day or my tummy bulges out. And then nobody wants to hire me."
        show palla happy
        palla.say "Eat some candy for me, [hero.name], so I can pretend to remember what it tastes like."
    elif result == 2:
        palla.say "If I overeat even a little bit, I have to spend an extra half hour or an hour in the gym. I mean, don't get me wrong, I love working out."
        palla.say "But fuck, that just kills so much of your day."
        mike.say "That's fucking depressing."
        show palla happy
        palla.say "It's the job, dude, and I love my job more than I love food."
    else:
        palla.say "The last time I went to one of those Brazilian Steakhouses I ate so much I had to take a week off."
        mike.say "A week off work because of a meal?"
        palla.say "Yeah, it's hard to keep your tummy flat. Even a tiny bit shows, the camera sees everything."
        mike.say "Wow."
        show palla angry
        palla.say "This is where you tell me I have a nice, flat tummy, jerk."
        mike.say "On one hand, I might want to say that, but you called me a jerk, so no."
        show palla happy
        palla.say "I guess that's close enough."
    $ palla.love += 1
    hide palla
    return

label palla_talk_travels_male:
    show palla
    palla.say "I think my favorite place in the world is Paris. That's where all the best fashion shows are."
    palla.say "I wish I were good enough to be in those shows."
    mike.say "Whoa wait a minute, I thought you were Miss Queen Bee Super Model, been everywhere done everything?"
    palla.say "Oh, don't get me wrong I do pretty well but, no, not a super model. Someday, maybe."
    show palla sad
    "Palla doesn't really sound like she believes what she just said. I kind of want to comfort her, but I'm kind of afraid she'll turn into a bitch if I do."
    mike.say "Oh come on, you're a great model."
    palla.say "Oh, fuck off, [hero.name]. You don't have a fucking clue what you're talking about."
    "Yup, there's the bitch."
    mike.say "And you're also a serious bitch sometimes."
    show palla happy
    palla.say "Yeah that part's true."
    $ palla.love += 1
    hide palla
    return

label palla_talk_tv_male:
    show palla
    palla.say "I don't really care about TV, except for fashion shows."
    hide palla
    return

label palla_talk_sports_male:
    show palla
    $ renpy.dynamic("result")
    $ result = randint(1, 3)
    if result == 1:
        palla.say "I work out an hour every day. I need to stay in shape. It's my job."
    elif result == 2:
        palla.say "I play handball twice a week, it keeps my calves strong. Plus it's a sport I can play alone."
        mike.say "But aren't sports meant to be played with other people?"
        palla.say "Yeah, fuck other people. They all suck."
        mike.say "They don't all suck."
        "I knew before I finished saying it what she was going to say."
        show palla annoyed
        palla.say "Everyone sucks. Politicians suck, movie stars suck, farmers suck and assholes out on the street suck. And you suck most of all, [hero.name]."
        mike.say "Well, at least you're consistent."
        "Consistently bitchy, that is."
    else:
        palla.say "You mean sports you watch on TV?"
        mike.say "Or the kind you go to, like at a stadium. Ever go to a football game?"
        palla.say "Well, I was a cheerleader in high school, so yeah, I've been to a few."
        mike.say "So you know all about football then, right?"
        palla.say "No, I know all about jocks though."
        mike.say "Oh, football players. They're kind of assholes."
        palla.say "No, I mean jocks, like their dicks. You know, penises. Mostly I know how the quarterback fucked me the locker room after every win."
        mike.say "Gross, Palla, I thought you had higher standards than that."
        palla.say "Oh, no, that team never won. They sucked so bad you look like a top athlete next to those guys. He never got near me."
        mike.say "..."
        show palla annoyed
        palla.say "Man you're such a sucker."
        mike.say "And you're such a bitch!"
    $ palla.love += 1
    hide palla
    return

label palla_talk_fashion_male:
    show palla
    palla.say "Fashion is my life."
    "Palla then goes on to talk about 2 or 3 different fashion designers, going on at length about how they differ from each other, and who is better."
    "I tune out about two sentences in."
    show palla angry
    palla.say "[hero.name], are you even listening to me?"
    mike.say "Honestly, I lost you when you started talking about moss. Who makes clothes out of moss anyway?"
    palla.say "No, Pyer Moss, he's a...oh never fucking mind, I should've known better than to think you had any class."
    $ palla.love -= 1
    hide palla
    return

label palla_talk_books_male:
    show palla annoyed
    palla.say "Boring. Talk about something else or don't bother talking to me."
    $ palla.love -= 1
    hide palla
    return

label palla_talk_people_male:
    show palla
    $ renpy.dynamic("result")
    $ result = randint(1, 3)
    if result == 1:
        palla.say "I don't have a lot of female friends, except for Audrey."
        palla.say "She's pretty amazing, honestly. I mean, she's almost as hot as I am, for a start, and she doesn't even model."
        palla.say "I don't know why she wastes time at that stupid office of yours. She'd make bank showing off her stuff and getting in the paper."
        palla.say "Instead she's wasted, locked in that dreary office all day, and I'm stuck alone, talking to people like you."
        mike.say "People like me?"
        palla.say "Creeps and assholes who just want to get in my panties."
        mike.say "You're way too much of a bitch for me to actually want to get in your panties."
        show palla happy
        palla.say "Oh good, maybe I'm safe, then."
    elif result == 2:
        palla.say "A few weeks ago I was doing a shoot for one of the major mall magazines. Sorry I can't say who they are yet, I signed an NDA."
        palla.say "Anyway, it was 2 girls and 2 guys and oh my God Kevin was so fucking hot, I swear. He had abs you could bounce a quarter off of."
        palla.say "And his eyes looked just like the ocean. I could sail away in those eyes. But really he had the most amazing shoulders."
        if hero.fitness < 75:
            palla.say "Big and broad and strong, not scrawny like you."
        else:
            palla.say "Just a bit stronger than you, actually, now that I think about it."
        palla.say "And the best part was his accent. From New Zealand, I think--"
        mike.say "Oh enough, I don't want to hear about other guys!"
        show palla happy
        palla.say "Oh, in that case I fucked him twice."
        mike.say "Ugh."
        palla.say "I wonder if he's still single. I doubt it, I'm pretty sure I was his third partner that weekend."
        mike.say "Oh shut up already!"
    else:
        palla.say "Have you ever heard of Cassidy Sloan?"
        mike.say "No, should I have?"
        palla.say "She's one of the hottest new models out of New York this year. Instant star. I wish I was her."
        mike.say "Aren't you already a star?"
        palla.say "I've been at this for five years and I guess I've done okay, but she turns down more offers in a week than I get in a year."
        mike.say "Ouch. Why is she so much better than you?"
        palla.say "I don't know. I mean look at me? I'm a Goddess, and the camera loves me. I don't get it."
        mike.say "Maybe it's because she's nice and you're a stone cold bitch?"
        palla.say "How do you know she's nice?"
        mike.say "You're right, I don't know she's nice. But I do know you're a bitch."
        palla.say "Fair."
    $ palla.love += 1
    hide palla
    return

label palla_talk_computers_male:
    show palla annoyed
    palla.say "Not interested."
    $ palla.love -= 1
    hide palla
    return

label palla_talk_music_male:
    show palla
    palla.say "Anything you can dance to. Ever heard of Griz? How about Hot Chip?"
    mike.say "Hm, no."
    palla.say "Well you're fucking useless. How do you get up in the mornings?"
    mike.say "Well I get up and put on my pants and go get in my car, unlike you and the broom you ride to work."
    palla.say "Nice, [hero.name]."
    hide palla
    return

label palla_talk_birthday_male:
    show palla
    mike.say "Happy birthday Palla."
    show palla sad
    palla.say "Thank you."
    "Palla looks surprisingly unhappy for someone having a birthday."
    mike.say "Uh, Palla, did I do something wrong?"
    palla.say "No, no, it's not you."
    mike.say "Really? That's a first."
    show palla normal
    "Palla cracks a smile."
    mike.say "What's wrong then?"
    show palla sad
    palla.say "Just...another year older. Another year until I start getting wrinkles, and flab, and then nobody will want to hire me, and then what will I do?"
    "I wanted to tell her she could live on pure bitchiness, but she seemed genuinely upset, so I decided against it."
    mike.say "Even if you get a few wrinkles, you're going to be sexy for decades. I wouldn't worry about it."
    show palla happy
    palla.say "Wait, [hero.name], did you just say something nice to me?"
    mike.say "Well it IS your birthday, after all."
    palla.say "I guess it is. Thanks!"
    $ palla.love += 3
    hide palla
    return

init python:
    SpecificTalkSubject(**{
    "name": "palla_talk_shawn",
    "display_name": "About Shawn",
    "label": "palla_talk_shawn_male",
    "duration": 0,
    "icon": "button_shawn",
    "conditions": [
        IsDone("palla_event_10"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(palla,
            IsActive(),
            IsFlag("talkedshawn", False)
            ),
        ],
    "do_once": True,
    })

label palla_talk_shawn_male:
    $ palla.flags.talkedshawn = True
    show palla
    mike.say "Hey Palla, who's Shawn?"
    palla.say "Who?"
    mike.say "Blonde guy with a goatee? Kind of nerdy."
    show palla angry
    palla.say "Why the fuck do you care?"
    "Whoa, that was unexpected. She's really angry, and all I did was say his name. What the hell?"
    mike.say "Just curious, I guess?"
    palla.say "Well, mind your own fucking business, asshole!"
    if palla.flags.slavepath:
        mike.say "Hey! Who you're seeing IS my business, bitch!"
        palla.say "Seeing? I'm not seeing him."
        mike.say "Then what?"
    else:
        mike.say "Hey, I'm just curious who else you're seeing. We're a thing, right? An item? Aren't I allowed to care about this stuff?"
        palla.say "No, my personal business is just, that, personal."
        mike.say "What the fuck?"
    palla.say "I already said, none of your fucking business."
    "And then Palla completely storms off."
    $ hero.cancel_activity()
    $ palla.hide()
    $ palla.set_counter("shawnencounter")
    hide palla
    return

init:
    define nickname_fuckface = ["Fuckface", "fuckface"]

label command_nickname_palla:
    menu:

        "Call me Fuckface" if active_girl.flags.mikeNickname not in nickname_fuckface and active_girl.love < 50:
            $ active_girl.flags.mikeNickname = "Fuckface"
        "Stop calling me Fuckface" if active_girl.flags.mikeNickname in nickname_fuckface:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_palla_male:
    mike.say "Hey, Palla..."
    mike.say "I was just thinking..."
    show palla surprised
    palla.say "Oh yeah?"
    palla.say "About what?"
    show palla
    mike.say "Well...about you greeting me in a sexy way."
    mike.say "Maybe telling me how hot I make you feel?"
    if palla.sub >= 70 or palla.is_sex_slave:
        show palla whining blush
        palla.say "Ah...I...I..."
        palla.say "I want to say no...but I can't!"
        show palla submissive
        palla.say "Urgh...you make me so crazy and so hot at the same time!"
        $ palla.flags.submissive_interact = True
    else:
        show palla vangry
        palla.say "Eww...don't be such a pig, [hero.name]!"
        palla.say "I'll do no such thing!"
        show palla angry
        mike.say "Ah...okay, Palla..."
        mike.say "We'll put that idea on ice for now."
        $ palla.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
