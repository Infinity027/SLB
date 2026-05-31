init python:
    SpecificTalkSubject(**{
    "name": "Ask about Viktor",
    "label": "camila_talk_viktor",
    "priority": 500,
    "icon": "button_victor",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(camila,
            IsActive(),
            MinStat("love", 50),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "Ask about her nipple",
    "label": "camila_talk_nipple",
    "priority": 500,
    "icon": "button_camila",
    "conditions": [
        IsNotDone("camila_talk_shark"),
        HeroTarget(IsGender("male")),
        PersonTarget(camila,
            IsActive(),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "Ask about her scars",
    "label": "camila_talk_scars",
    "priority": 500,
    "icon": "button_camila",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(camila,
            IsActive(),
            MinStat("love", 100),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "Chit chat",
    "label": "camila_talk_shark",
    "priority": 500,
    "icon": "button_camila",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach", "date_nudistbeach")),
        PersonTarget(camila,
            IsActive(),
            MinStat("love", 25),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "camila_talk_investigation",
    "display_name": "About the investigation",
    "label": "camila_talk_investigation_male",
    "duration": 0,
    "icon": "button_investigate",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("underinvestigation"),
            MaxFlag("workinvestigation", 99)
            ),
        PersonTarget(camila,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label camila_talk_love_male:
    show camila
    mike.say "Do you have much time for romance, Camila?"
    mike.say "Or are you married to the police force?"
    "Camila chuckles, curling her lip in an ironic manner."
    camila.say "You watch too many cop shows, [hero.name]!"
    show camila annoyed
    camila.say "But no..."
    camila.say "My personal life takes a backseat most of the time."
    $ camila.love -= 1
    hide camila
    return

label camila_talk_sex_male:
    show camila
    mike.say "It must be hard to turn off at the end of the day."
    mike.say "You know, being a cop?"
    "Camila nods."
    "But she looks at me like she knows there's another question coming her way."
    mike.say "Hard to, well..."
    mike.say "Change gears and think of stuff like, say...sex?"
    show camila flirt
    camila.say "Nah."
    camila.say "I find a hard day at work makes me pretty horny!"
    $ camila.love += 2
    hide camila
    return

label camila_talk_politics_male:
    show camila
    mike.say "What's your stance on politics, Camila?"
    show camila annoyed
    "My question makes Camila snort derisively."
    camila.say "Don't talk to me about politics, [hero.name]."
    show camila angry
    camila.say "Politicians are all the same - self-serving scumbags!"
    camila.say "None of them would last an hour on the streets."
    $ camila.love -= 1
    hide camila
    return

label camila_talk_food_male:
    show camila
    mike.say "You like to eat out much, Camila?"
    show camila annoyed
    "Camila wrinkles her nose at the question."
    camila.say "I grab a hotdog from a street vendor most days."
    camila.say "That what you mean?"
    $ camila.love -= 1
    hide camila
    return

label camila_talk_travels_male:
    show camila
    mike.say "I guess we all have a list of places we want to visit."
    mike.say "You know, Camila - places to see before we die?"
    show camila blush
    "Camila looks at me a little oddly, like she's confused."
    camila.say "Uh...no, [hero.name], I don't!"
    camila.say "But now you mention it..."
    camila.say "Maybe I should!"
    $ camila.love += 1
    hide camila
    return

label camila_talk_tv_male:
    show camila
    mike.say "I binged a pretty good detective series the other day, Camila."
    mike.say "You really should check it out."
    show camila bored
    "Camila laughs out loud at the suggestion."
    camila.say "Nah, [hero.name] - I live that shit every day!"
    camila.say "Do you go home and watch stuff about some guy that works in an office?!?"
    $ camila.love -= 1
    hide camila
    return

label camila_talk_sports_male:
    show camila
    mike.say "I caught the end of the game at the pub last night, Camila."
    mike.say "Did you manage to see the first half?"
    show camila annoyed
    "Camila sighs and shakes her head, looking a little deflated."
    camila.say "Nah, I was on shift the whole time."
    show camila -annoyed
    camila.say "I try to catch up when I can."
    camila.say "But it's just not the same as watching live."
    $ camila.love += 1
    hide camila
    return

label camila_talk_fashion_male:
    show camila
    mike.say "You don't seem that worried about fashion, Camila."
    show camila annoyed
    camila.say "Why, [hero.name]?"
    camila.say "Is that a problem?"
    mike.say "NO!"
    mike.say "No, of course not!"
    show camila -annoyed
    "Camila nods, clearly enjoying the discomfort she's causing me to feel."
    camila.say "Let's just say you don't get much respect as a female cop to begin with."
    camila.say "So prancing around in a pretty dress doesn't help matters!"
    $ camila.love -= 1
    hide camila
    return

label camila_talk_books_male:
    show camila
    mike.say "Read any good books lately, Camila?"
    "Camila cocks her head on one side."
    "It seems the question catches her off-guard."
    camila.say "Um, yeah, actually..."
    camila.say "I sometimes get the chance to read on stakeouts."
    show camila annoyed
    camila.say "It's just...people tend to assume I don't like that kind of thing!"
    $ camila.love -= 1
    hide camila
    return

label camila_talk_people_male:
    show camila
    mike.say "You must meet a lot of interesting people, Camila."
    mike.say "You know, being a cop?"
    show camila annoyed
    "Camila shakes her head at this, dismissing the notion."
    camila.say "Nah, most people are the shits."
    camila.say "It's real rare that I meet someone I like that much."
    $ camila.love -= 1
    hide camila
    return

label camila_talk_computers_male:
    show camila
    mike.say "I got a new FPS for the Zbox the other day, Camila."
    mike.say "It's a real adrenaline rush, you know?"
    "Camila chuckles and shakes her head."
    show camila annoyed
    "And the look she gives me is more than a little condescending."
    camila.say "More thrilling than shooting a real gun at real perps?"
    camila.say "I don't think so, [hero.name]!"
    $ camila.love -= 1
    hide camila
    return

label camila_talk_music_male:
    show camila
    mike.say "You ever listen to music, Camila?"
    mike.say "Like when you're out patrolling the streets?"
    camila.say "You mean beats on the beat?"
    "I can't help smiling at the lame joke."
    show camila annoyed
    camila.say "Nah, [hero.name]."
    camila.say "I'm usually too focused on the job."
    $ camila.love -= 1
    hide camila
    return

label camila_talk_birthday_male:
    show camila close
    mike.say "Happy birthday, Camila."
    mike.say "It's not much, just a little something I saw the other day."
    mike.say "It made me think of you..."
    show camila blush
    camila.say "Oh, geez, [hero.name]."
    camila.say "I'd forgotten all about my birthday!"
    camila.say "I was so busy...but you remembered!"
    $ camila.love += 5
    hide camila
    return

label camila_talk_viktor:
    show camila close
    mike.say "Ah, Camila..."
    mike.say "Who's 'Viktor'?"
    mike.say "Is he an ex of yours?"
    "Camila laughs and shakes her head at this."
    camila.say "Fuck, no, [hero.name]!"
    camila.say "He's a gangland killer, real nasty piece of work too."
    camila.say "I've been on his trail for years."
    camila.say "But one day I'll catch him and nail his ass to the wall!"
    $ camila.love += 2
    hide camila
    return

label camila_talk_nipple:
    show camila close
    mike.say "Erm, Camila..."
    mike.say "I have to ask - what happened to your..."
    mike.say "Well, to your breast?"
    "Camila looks down at her chest and then back up at me."
    "For a moment it seems like she has no clue what I mean."
    "But then she nods as she gets my drift."
    camila.say "Oh, you mean my nipple, right?"
    show camila flirt
    camila.say "Shark, great white, bit it clean off!"
    $ camila.love += 2
    hide camila
    return

label camila_talk_scars:
    show camila close
    mike.say "Whoa, Camila - you have a lot of scars!"
    "Camila chuckles and nods."
    camila.say "Yeah, I guess."
    camila.say "I lose track of where most are from."
    camila.say "Apart from this one."
    "She points to a particularly large and brutal-looking scar."
    show camila flirt
    camila.say "Bear gave me that one when I rescued a dog from him while hiking in the forest!"
    $ camila.love += 2
    hide camila
    return

label camila_talk_shark:
    show camila close
    mike.say "I just love the look of the ocean at night, Camila."
    mike.say "You ever think about taking a swim under the stars?"
    "Camila shakes her head at this, giving me a serious stare as she does so."
    camila.say "No way, [hero.name]."
    camila.say "You do know there are sharks out there, right?"
    mike.say "You're kidding?!?"
    "Camila raises one eyebrow as she weighs one of her breasts in her hand."
    show camila flirt
    camila.say "What, you think I bit the nipple off of my own tit?"
    $ camila.love += 2
    hide camila
    return

label camila_talk_investigation_male:
    show camila
    "Camila shakes her head as she regards me."
    show camila happy
    "And she can't suppress a knowing chuckle either."
    show camila wink
    camila.say "Oh-oh!"
    camila.say "I've seen that look before."
    camila.say "Usually on someone I'm grilling in an interview room!"
    "I close my eyes for a moment, taking the time to breath deeply."
    "Then I nod and look Camila straight in the eye."
    "There's no point in denying it, so I'd better get to the point."
    mike.say "Yeah..."
    mike.say "There is something that's been on my mind."
    mike.say "Something that I wanted to talk to you about."
    show camila normal
    "Camila nods, suddenly looking more serious."
    "And I can't help finding her interest reassuring."
    camila.say "Hmm..."
    camila.say "Sounds serious!"
    camila.say "You'd better hurry up and tell me all about it, [hero.name]."
    mike.say "Okay, okay..."
    "I instinctively lean in closer as I start to spill my guts."
    "And it's all I can do to keep from whispering too."
    mike.say "I...I'm in some trouble at work, Camila."
    camila.say "What did you do now, [hero.name]?"
    camila.say "Get caught stealing some stationary?"
    camila.say "Or did you flirt with the wrong secretary, huh?"
    mike.say "Ah..."
    mike.say "It's a little more serious than that, Camila!"
    mike.say "They're saying that I embezzled money!"
    show camila surprised
    "Camila stares at me in surprise."
    camila.say "Well..."
    camila.say "Did you?"
    mike.say "Of course not, Camila!"
    mike.say "The money was just..."
    mike.say "It was just resting in my account, that's all!"
    show camila annoyed
    "Camila frowns, like she's having a hard time believing me."
    camila.say "I've got to admit, [hero.name]..."
    camila.say "I never heard that one before!"
    mike.say "Whatever, Camila..."
    mike.say "I just need your help, okay?"
    mike.say "Can you do anything?"
    if camila.love >= 100:
        $ camila.set_counter("investigationcallback")
        show camila flirt
        "Camila gives me a wry smile."
        camila.say "So you're an innocent, yeah?"
        camila.say "A victim of false accusations?"
        "I feel myself starting to sweat anew."
        "Why is she doing this to me?"
        "I feel like Camila's enjoying the chance to watch me squirm!"
        mike.say "I am, Camila - I swear it!"
        mike.say "Will you help me or not?!?"
        show camila happy
        camila.say "Settle down, [hero.name]!"
        camila.say "Of course I'll help you."
        show camila normal
        camila.say "And for the record, I'm not going to dump you - even if you did it!"
        camila.say "You don't stay a cop as long as I have without getting used to shades of grey."
        camila.say "If you were accused of murder, then maybe it'd be different..."
        mike.say "No, Camila - no murder charges here!"
        mike.say "Just plain old boring embezzlement!"
        camila.say "Okay, okay..."
        camila.say "I'll have to talk to some colleagues in the financial crime department."
        camila.say "White collar crime isn't my area of expertise."
        camila.say "But they should be able to prove this is all just a misunderstanding."
        "For the first time in what feels like forever, my spirits actually begin to lift."
        mike.say "Oh god..."
        mike.say "Thank you, Camila!"
        mike.say "I'll be forever in your debt for this!"
        show camila flirt
        "Suddenly the wry smile is back on Camila's face."
        camila.say "You bet you will, [hero.name]!"
        camila.say "After this, I'm gonna own your ass!"
    else:
        show camila sad
        "Camila shakes her head, and I feel my hope vanish."
        camila.say "This really isn't my area of expertise, you know?"
        camila.say "I work the streets, [hero.name]."
        camila.say "This is financial crime - white collar stuff."
        mike.say "But surely you know someone that can help, Camila?"
        mike.say "You're a cop, so you must know other cops, right?"
        show camila normal
        "Camila holds up a hand, signalling that the conversation is over."
        camila.say "Like I already said, [hero.name]..."
        camila.say "It's not my area of responsibility."
        camila.say "Plus it'd look pretty suspicious if I stuck my nose in."
        camila.say "You know, what with us being so close and all?"
        "I'm about to open my mouth and continue arguing."
        show camila weird
        "But Camila raises her eyebrows in that particular manner."
        "You know what I mean - the one that says 'you'd better drop this!'."
        "And so all I can do is nod."
        mike.say "Okay, Camila, okay..."
        mike.say "I get the message."
        show camila happy
        "Camila smiles and nods."
        camila.say "Glad to know we're on the same page, [hero.name]."
        show camila normal
        camila.say "And anyway, you already told me it's all a mistake, right?"
        camila.say "So what have you got to be scared of?"
        "I force a nervous smile onto my face and nod."
        mike.say "Ah...yeah, Camila!"
        mike.say "That's right..."
    return

init:
    define nickname_papi_chulo = ["Papi Chulo", "papi chulo","papi Chulo", "Papi chulo"]
    define nickname_papi = ["Papi", "papi"]
    define nickname_guapo = ["Guapo", "guapo"]
    define nickname_hermoso = ["Hermoso", "hermoso"]

label command_nickname_camila:
    menu:

        "Call me Papi Chulo" if active_girl.flags.mikeNickname not in nickname_papi_chulo and active_girl.love > 100 and active_girl.sub > 75:
            $ active_girl.flags.mikeNickname = "Papi Chulo"
        "Stop calling me Papi Chulo" if active_girl.flags.mikeNickname in nickname_papi_chulo:
            $ active_girl.flags.mikeNickname = None


        "Call me Papi" if active_girl.flags.mikeNickname not in nickname_papi and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Papi"
        "Stop calling me Papi" if active_girl.flags.mikeNickname in nickname_papi:
            $ active_girl.flags.mikeNickname = None


        "Call me Guapo" if active_girl.flags.mikeNickname not in nickname_guapo and active_girl.love > 50 and hero.fitness > 50:
            $ active_girl.flags.mikeNickname = "Guapo"
        "Stop calling me Guapo" if active_girl.flags.mikeNickname in nickname_guapo:
            $ active_girl.flags.mikeNickname = None


        "Call me Hermoso" if active_girl.flags.mikeNickname not in nickname_hermoso and active_girl.love > 50 and hero.charm > 50:
            $ active_girl.flags.mikeNickname = "Hermoso"
        "Stop calling me Hermoso" if active_girl.flags.mikeNickname in nickname_hermoso:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl


label submissive_interact_camila_male:
    mike.say "Hey, Camila..."
    mike.say "You know what'd be fun?"
    "Camila raises an eyebrow at the question."
    show camila flirt
    camila.say "I don't know, [hero.name]."
    camila.say "But I guess you're going to tell me?"
    show camila normal
    mike.say "Well, what if you had a catchphrase - like cops in the movies?"
    mike.say "But your's was something about how much you're into me?"
    if camila.sub >= 70 or camila.is_sex_slave:
        show camila blush
        camila.say "You know, that actually sounds like a cute idea."
        camila.say "It could be one of those little things that only know about."
        camila.say "Let me think about it and I'll see what I can come up with."
        $ camila.flags.submissive_interact = True
    else:
        show camila angry
        camila.say "Are you serious, [hero.name]?"
        camila.say "I'm a serious cop, not a character in some videogame!"
        show camila annoyed
        mike.say "Sorry, Camila..."
        mike.say "I don't know what I was thinking!"
        $ camila.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
