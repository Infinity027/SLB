init python:


    Job(**{
    "id": "nova",
    "name": "Nova Sportswear",
    "description": "Nova Sportswear is an obscure internet-only brand that is probably cheap Chinese knockoffs of better brands. They do not pay well but are willing to hire!",
    "label": "palla_find_nova",
    "income": 50,
    "career_gain": (1, "12345"),
    "career_max": 10,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            ),
        ],
})


    Job(**{
    "id": "heirloom",
    "name": "Heirloom",
    "description": "Heirloom is a standard department store brand with little style or glamour, but it's a mainstream job that will pay the bills.",
    "label": "palla_find_heirloom",
    "income": 200,
    "career_gain": (2, "12345"),
    "career_max": 25,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 10),
            ),
        ],
})

    Job(**{
    "id": "boreale",
    "name": "Boréale",
    "description": "Boréale is a mass market brand sold at the lowest possible price. They pay poorly but are everywhere, so career advancement is faster.",
    "label": "palla_find_boreale",
    "income": 100,
    "career_gain": (4, "12345"),
    "career_max": 50,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 10),
            ),
        ],
})


    Job(**{
    "id": "chronicle",
    "name": "Chronicle Clothing",
    "description": "Chronicle Clothing is a mainstream line of clothing sold at upscale department stores. It has broad visibility in the modelling world.",
    "label": "palla_find_chronicle",
    "income": 500,
    "career_gain": (2, "12345"),
    "career_max": 60,
    "difficulty": 10,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 15),
            ),
        ],
})

    Job(**{
    "id": "spellbound",
    "name": "Spellbound Fashion",
    "description": "Spellbound Fashion markets specifically to women who want to dress to impress.",
    "label": "palla_find_spellbound",
    "income": 750,
    "career_gain": (1, "1234"),
    "career_max": 75,
    "difficulty": 25,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 15),
            ),
        ],
})

    Job(**{
    "id": "flair",
    "name": "Flair",
    "description": "Flair targets the wealthy 18-21 crowd, trying to stay ahead of current trends and set the market. People who wear Flair get noticed!",
    "label": "palla_find_flair",
    "income": 350,
    "career_gain": (4, "12345"),
    "career_max": 75,
    "difficulty": 25,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 15),
            ),
        ],
})



    Job(**{
    "id": "grandeur",
    "name": "Grandeur",
    "description": "Grandeur is overpriced fashion for people who don't truly understand what fashion is. It has big money support, but it's not considered fashionable by the truly \"in\" crowds.",
    "label": "palla_find_grandeur",
    "income": 1250,
    "career_gain": (1, "12345"),
    "career_max": 90,
    "difficulty": 40,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 35),
            ),
        ],
})

    Job(**{
    "id": "prodigy",
    "name": "Prodigy",
    "description": "Prodigy is an extremely new line of eveningwear, with an emphasis on elegant and subtle. It's unclear whether the line will take off.",
    "label": "palla_find_prodigy",
    "income": 1000,
    "career_gain": (4, "134"),
    "career_max": 90,
    "difficulty": 45,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 35),
            ),
        ],
})

    Job(**{
    "id": "escape",
    "name": "Escape Collection",
    "description": "The Escape Collection has been around for decades. While the younger, hipper crowd thinks of it as old hat, the older, wealthy crowds flock to it.",
    "label": "palla_find_escape",
    "income": 1500,
    "career_gain": (1, "12345"),
    "career_max": 90,
    "difficulty": 50,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 35),
            ),
        ],
})



    Job(**{
    "id": "minds_eye",
    "name": "Mind's Eye Couture",
    "description": "Mind's Eye Couture has been on the leading edge of fashion for at least a decade, remaking themselves almost completely every two years. People who wear this are wealthy and want you to know it.",
    "label": "palla_find_minds_eye",
    "income": 1750,
    "career_gain": (1, "12345"),
    "career_max": 95,
    "difficulty": 60,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 50),
            ),
        ],
})

    Job(**{
    "id": "aurore",
    "name": "Couture par Aurore",
    "description": "The brain child of noted French fashion designer Georges Solé, Couture par Aurore is the height of modern fashion. It doesn't get more elegant than Aurore.",
    "label": "palla_find_aurore",
    "income": 2250,
    "career_gain": (1, "12345"),
    "career_max": 100,
    "difficulty": 70,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 50),
            ),
        ],
})

    Job(**{
    "id": "anomalie",
    "name": "Anomalie",
    "description": "Accessoires par Anomalie includes an elegant line of accessories for the sophisticated, incredibly wealthy woman.",
    "label": "palla_find_anomalie",
    "income": 2000,
    "career_gain": (1, "12345"),
    "career_max": 100,
    "difficulty": 70,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            MinStat("career", 50),
            ),
        ],
})


    Job(**{
    "id": "hawtbitches",
    "name": "hawtbitches.com",
    "description": "What can you say about a website called hawtbitches.com? It's not classy, but it's still modelling.",
    "label": "palla_find_hawtbitches",
    "income": 500,
    "career_gain": (2, "12345"),
    "career_max": 50,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            IsFlag("pornmaybe"),
            ),
        ],
})

    Job(**{
    "id": "sexypalla",
    "name": "sexypalla.xxx",
    "description": "Enough paying customers think Palla is hot enough that Palla has been offered her own website.",
    "label": "palla_find_sexypalla",
    "income": 1000,
    "career_gain": (2, "12345"),
    "career_max": 60,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            IsFlag("pornnudes"),
            MinStat("career", 25),
            ),
        ],
})

    Job(**{
    "id": "onlychix",
    "name": "onlychix.xxx",
    "description": "onlychix.xxx offers hot girl on girl action, specializing in femdom and other fetishes",
    "label": "palla_find_onlychix",
    "income": 1500,
    "career_gain": (2, "134"),
    "career_max": 75,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            IsFlag("pornnudes"),
            MinStat("career", 50),
            ),
        ],
})

    Job(**{
    "id": "fucktoybitches",
    "name": "fucktoybitches.adult",
    "description": "fucktoybitches.adult specializes in two, three and four man gangbangs of the hottest girls",
    "label": "palla_find_fucktoybitches",
    "income": 2000,
    "career_gain": (1, "12345"),
    "career_max": 90,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            IsFlag("pornsex"),
            MinStat("career", 60),
            ),
        ],
})

    Job(**{
    "id": "pallapoundin",
    "name": "Palla Poundin",
    "description": "Palla Poundin is Palla's stage name, where she is a star in her own right. It isn't glamorous, but it is fame.",
    "label": "palla_find_pallapoundin",
    "income": 2500,
    "career_gain": (1, "12345"),
    "career_max": 100,
    "conditions": [
        PersonTarget(palla,
            IsActive(),
            IsFlag("pornfuck"),
            MinStat("career", 90),
            ),
        ],
})

    Event(**{
    "name": "palla_fired_check",
    "label": "palla_fired_check",
    "conditions": [
        PersonTarget(palla,
            IsFlag("career"),
            Not(IsFlag("job", False)),
            IsDayOfWeek("12345"),
            ),
        ],
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "palla_fired_talk_01",
    "label": "palla_fired_talk_01",
    "conditions": [
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsFlag("career"),
            IsFlag("fired"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "palla_fired_talk_02",
    "label": "palla_fired_talk_02",
    "conditions": [
        IsDone("palla_fired_talk_01"),
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsFlag("career"),
            IsFlag("fired"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "palla_fired_talk_03",
    "label": "palla_fired_talk_03",
    "conditions": [
        IsDone("palla_fired_talk_02"),
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsFlag("career"),
            IsFlag("fired"),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "palla_career_event_01",
    "label": "palla_career_event_01",
    "conditions": [
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            MinStat("career", 10)
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "palla_career_event_02",
    "label": "palla_career_event_02",
    "conditions": [
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            MinStat("career", 15)
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "palla_career_event_03",
    "label": "palla_career_event_03",
    "conditions": [
        IsHour(7, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            MinStat("career", 35)
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "palla_career_event_04",
    "label": "palla_career_event_04",
    "conditions": [
        IsHour(10, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            MinStat("career", 50),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "palla_career_event_05",
    "label": "palla_career_event_05",
    "conditions": [
        IsHour(10, 22),
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            Not(IsPresent()),
            MinStat("love", 160),
            MinStat("career", 75),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_hawtbitches",
    "label": "palla_event_hawtbitches",
    "conditions": [
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsActive(),
            IsFlag("hawtbitchestalk")
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_onlychix",
    "label": "palla_event_onlychix",
    "conditions": [
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsActive(),
            IsFlag("onlychixtalk")
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "palla_event_fucktoybitches",
    "label": "palla_event_fucktoybitches",
    "conditions": [
        HeroTarget(Not(OnDate())),
        PersonTarget(palla,
            IsActive(),
            IsFlag("fucktoybitchestalk")
            ),
        ],
    "do_once": True,
    })



label palla_new_job(job):
    $ palla.flags.schedule = "working"
    if job.id == 'hawtbitches':
        $ palla.flags.pornnudes = True
    elif job.id == 'onlychix':
        $ palla.flags.pornsex = True
    elif job.id == 'fucktoybitches':
        $ palla.love -= 20
        $ palla.flags.pornfuck = True
    return

label palla_fired_check:
    $ renpy.dynamic("job")
    $ job = JOBS.get(palla.flags.job)
    if not job:
        return



    if job.difficulty >= 10 and job.difficulty + randint(1, 10) > palla.career:
        "Palla was fired from her job at [job.name]."
        $ palla.flags.job = False
        $ palla.flags.fired = True
        $ palla.flags.firedcount += 1
        if job.id in AVAILABLE_JOBS['palla']:
            $ AVAILABLE_JOBS["palla"].remove(job.id)
        $ palla.flags.schedule = "default"

    return


label palla_fired_talk_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    palla.say "Hey, [hero.name]. I got fired today."
    mike.say "Yeah, I heard. What happened?"
    palla.say "I don't know. There was a PA that said something, I don't even remember what."
    mike.say "What's a PA?"
    palla.say "Production Assistant. They're the ones that do...basically everything that isn't somebody's specific job. Anyway, I don't remember what he said."
    palla.say "But I yelled at him for it. And he apologized and I thought it was done."
    palla.say "And at the end of the day the director told me they wanted to go in a different direction."
    palla.say "And I thought I was doing so well, too! I can't believe they did that!"
    "I sigh."
    mike.say "Palla, when you're at a shoot, are you in charge?"
    palla.say "I'm the talent!"
    mike.say "Sure, but are you the one who tells the crew what to do?"
    palla.say "No, I guess that's not my job."
    mike.say "If you have a problem with someone in the crew, you have to take it to whoever's in charge. That's the director, right?"
    palla.say "It depends on the crew, but yeah, the photo director or the photographer himself."
    mike.say "It's hard, but this is your job, not mine. You have to hold your tongue sometimes."
    palla.say "I do! I hold my tongue {b}all the time{/b}! It's exhausting!"
    mike.say "Well, you have to hold your tongue a little more. Unless you want to find a new career."
    "Palla sighs."
    palla.say "Well. Now what?"
    mike.say "I'll see if I can find you something new."
    palla.say "Thanks. And, [hero.name]? I'm sorry. I'll do better next time, I promise!"
    $ palla.flags.fired = False
    return


label palla_fired_talk_02:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    "Oh look, it's Palla. I know what this will be about."
    palla.say "Hey, [hero.name]. I got fired today. Again."
    mike.say "Palla, is this going to be a pattern?"
    palla.say "I swear, it was not my fault this time!"
    "I take a deep breath. I can't wait for the explanation here."
    mike.say "What happened this time?"
    palla.say "I don't honestly know! Everything was going great, I thought! The photographer was having some trouble with lighting, so the shoots kept running over time."
    palla.say "And I guess they blamed me or something? It doesn't make any sense."
    mike.say "Really? You didn't yell at anyone or anything?"
    palla.say "No! I actually held my tongue. For you!"
    mike.say "Huh."
    mike.say "So did they say anything? Give you any reason at all?"
    palla.say "They said they felt I was difficult to work with and my attitude was not in keeping with their blah blah blah, and that my skills weren't worth my attitude."
    mike.say "I thought you held your tongue?"
    palla.say "I swear! I did! I don't remember doing anything that was difficult. I don't know. Maybe the shoots running long were my fault somehow?"
    mike.say "You better figure that out. This is the second job you've lost. It was hard enough finding the jobs you've had."
    palla.say "I know, I know."
    mike.say "I'll see if I can find you something else."
    palla.say "Thanks, [hero.name]. I'll...I don't know. I'll see if I can figure out what went wrong."
    $ palla.flags.fired = False
    return


label palla_fired_talk_03:
    play sound cell_vibrate loop
    "Oh look, it's Palla. I know what this will be about."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    palla.say "I know what you're going to say, [hero.name]. And you're right. I'm a fuckup."
    mike.say "Huh. You didn't know what I was going to say."
    palla.say "Well. It's true. I'm a fuckup."
    mike.say "Should I ask what happened?"
    palla.say "No."
    mike.say "That bad, huh?"
    palla.say "I...I'm sorry, [hero.name]. I tried to hold my tongue, but I had to defend myself. The shit those girls were saying. You would've yelled at them too."
    mike.say "Maybe. I guess. Still, it's another job you've lost."
    palla.say "Are you going to find me something else?"
    mike.say "I'll try. We're not going to have a lot of choices, though."
    palla.say "I know."
    mike.say "Have you thought about doing nudes?"
    palla.say "No! I'm a serious model!"
    mike.say "Seriously batshit crazy, maybe. Look, I'll find you what I can."
    palla.say "Ugh. Do you really think I should do nudes?"
    if palla.love >= 160 or palla.sub >= 70:
        palla.say "I mean, I'd do them for you, privately, but that's not the same."
    palla.say "I'm just not sure I want every gross dude in the country ogling my bare tits."
    menu:
        "If it keeps your career going...":
            mike.say "Well. If we get low on options, it may be what keeps you in the business."
            palla.say "I guess. No promises, okay?"
            $ palla.flags.pornmaybe = True
        "You're right, those tits are for me to ogle":
            mike.say "You're right, those tits are for me to ogle."
            palla.say "I can't decide if I think that's sweet or awful."
            mike.say "Let's go with sweet."
            palla.say "If you say so."
    mike.say "Anyway, I'll see what else I can find for you."
    $ palla.flags.fired = False
    return

label palla_event_hawtbitches:
    show palla
    mike.say "So, Palla, I found a nude modelling job that you can do."
    show palla annoyed
    palla.say "Ugh. I thought I said no nudes?"
    mike.say "You said no promises, not no."
    palla.say "Are you really going to make me do this?"
    mike.say "If there's no other options?"
    palla.say "Ugh. You're sure you want...everyone else looking at this?"
    mike.say "Well. No, but."
    show palla normal
    palla.say "If you really, really want me to, I'll do the job. But I won't like it."
    mike.say "Okay. I'll let you know if I decide to put you on the job."
    hide palla
    call job_add ('palla', 'hawtbitches') from _call_job_add
    return

label palla_event_onlychix:
    mike.say "Palla, you've doing great at the nude modelling. How do you feel about lesbian porn?"
    palla.say "I'm not comfortable with porn, [hero.name], lesbian or otherwise. It's...not really what I want to be doing."
    mike.say "The money's really good, though, and you could really break out doing this."
    palla.say "No, [hero.name]."
    menu:
        "I insist, you need this" if palla.sub >= 60:
            mike.say "Palla, no. I mean it. You really should do this."
            palla.say "Fine, if that's really what you want me to do. I just...I dunno. I hope it doesn't ruin. You know. Us."
            mike.say "Oh, trust me, you and another girl? That'll be hot."
            palla.say "I guess."
            call job_add ('palla', 'onlychix') from _call_job_add_1
        "Okay, no porn":
            mike.say "Okay, no porn. We'll make do with what you're already doing."
    return

label palla_event_fucktoybitches:
    mike.say "Palla, you've been offered a job doing serious porn. They say they can make you a huge porn star, one of the biggest, but you'll have to do group stuff with a bunch of guys. They think you have real talent, though."
    palla.say "I don't...I don't really like doing the porn stuff, [hero.name]. Do you think you can get me back to modelling?"
    mike.say "But this is great for your career!"
    palla.say "Please, don't...don't make me."
    menu:
        "You're doing this" if palla.sub >= 80:
            mike.say "No. Palla, you're doing this. I insist. You hired me for this, and I'm getting your career on track!"
            palla.say "But it's not the career I want!"
            mike.say "It's the career you have."
            palla.say "I...I...fine. If you really, really want me to."
            call job_add ('palla', 'fucktoybitches') from _call_job_add_2
        "Okay, no more porn":
            mike.say "Okay, we will find another way to make this work."
    return

label palla_career_event_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    "When I answer my phone, I hear Palla's voice sounding excited."
    palla.say "[hero.name]! [hero.name]! I can't believe it, but I think you being my agent is actually working! Can you find me something else, though?"
    palla.say "Nova isn't cutting it. It doesn't pay enough and isn't going anywhere. But some of the other girls and I have talked and I think you might be able to find some openings."
    mike.say "Sure, Palla! I'll make some phone calls!"
    palla.say "Thank you so much!"
    if palla.love >= 180:
        palla.say "Love you!"
    return

label palla_career_event_02:
    "Palla's career is starting to move forward. I should see if there are more jobs now."
    return

label palla_career_event_03:
    "Palla's career is really taking off. I should see if there are more jobs now."
    return


label palla_career_event_04:
    play sound cell_vibrate loop
    "My phone buzzes."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    mike.say "Hey Palla!"
    palla.say "Hey, [hero.name]! I just wanted to call and thank you! I can't believe how much work I'm getting lately, and...it feels good. I mean, really good."
    palla.say "My whole life, something's been missing. I've tried so hard and I couldn't do it on my own. You helped me."
    palla.say "I just...oh crap I'm getting awkward, I'm sorry."
    mike.say "It's okay, Palla! I'm really happy things are going well for you now!"
    palla.say "And it's all thanks to you. I...I'm so glad you're in my life."
    mike.say "I'm glad you're in mine too. You definitely have made life interesting!"
    if palla.love >= 160:
        palla.say "I love you, [hero.name]! Talk to you later!"
    else:
        palla.say "I have to go, work calls. Talk to you later!"
    return


label palla_career_event_05:
    play sound cell_vibrate loop
    "My phone buzzes."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Palla")
    if not result:
        $ hero.cancel_event()
        $ palla.love -= 5
        return
    mike.say "Palla, my love, it's good to hear from you!"
    palla.say "Hey now, don't get all mushy on me."
    mike.say "Fine. What's up, bitch?"
    "Palla laughs."
    palla.say "I just have a couple of minutes in between shots here, but I was thinking about you."
    mike.say "I thought you didn't want me to get sappy?"
    palla.say "That's because I wanted to be sappy and if we're both sappy the sheer weight of it will tear a hole in the universe."
    mike.say "That would be bad."
    palla.say "Right? Anyway, I just..."
    if palla.flags.minealone:
        palla.say "I just...I just wanted to say I'm yours forever."
    else:
        palla.say "I just wanted to say that I want to be with you forever."
    mike.say "Well fuck, Palla, how can I respond to that without being sappy?"
    palla.say "Fine, you can be sappy {b}just this once{/b}!"
    mike.say "I love you, Palla. You're the spice that makes life taste good."
    palla.say "Oh yeah? Maybe I'll give you something that tastes good...later!"
    mike.say "Tease!"
    palla.say "You love it! Oh, there's my call, gotta go! Love you, bye!"
    return

label palla_find_nova:
    "I call around to a few of my contacts. Eventually I find an opening that's willing to give Palla a try, for a company called Nova Sportswear."
    "It doesn't pay nearly enough but she's been out of work too long. This will get her some recognition. I should contact them and sign Palla up."
    call job_add ('palla', 'nova') from _call_job_add_3
    return

label palla_find_heirloom:
    "Palla's success at Nova has opened another door. Heirloom has offered her a position modelling for their department store catalog."
    call job_add ('palla', 'heirloom') from _call_job_add_4
    return

label palla_find_boreale:
    "Palla's success at Nova has opened another door. Boréale has offered her a position. The pay is terrible but it's good solid work with a lot of reach."
    call job_add ('palla', 'boreale') from _call_job_add_5
    return

label palla_find_chronicle:
    "Palla's starting to turn some heads and getting more notice. The Chronicle Collection wants her now."
    call job_add ('palla', 'chronicle') from _call_job_add_6
    return

label palla_find_spellbound:
    "Spellbound Fashion said they'd like to give Palla a try. I'm not sure she's quite ready for that, I should make sure her career is really stable before she tries something with that much cachet."
    call job_add ('palla', 'spellbound') from _call_job_add_7
    return

label palla_find_flair:
    "Flair has agreed to give Palla a go. If she can handle working there, it will be great for her career!"
    call job_add ('palla', 'flair') from _call_job_add_8
    return

label palla_find_grandeur:
    "A position at Grandeur is available. They're overpriced but they demand excellence. I need to make sure Palla is ready before I give her a position there."
    call job_add ('palla', 'grandeur') from _call_job_add_9
    return

label palla_find_prodigy:
    "A position at Prodigy is available. They're new on the scene, and there will be a lot of exposure but a lot of trouble if Palla can't behave."
    "I need to make sure Palla is ready before I give her a position there."
    call job_add ('palla', 'prodigy') from _call_job_add_10
    return

label palla_find_escape:
    "One of the most prestigious lines, the Escape Collection, wants Palla to model their clothing."
    call job_add ('palla', 'escape') from _call_job_add_11
    return

label palla_find_minds_eye:
    "Mind's Eye Couture has taken notice of Palla's success. They've offered her a position. She'll have to be superb, though!"
    call job_add ('palla', 'minds_eye') from _call_job_add_12
    return

label palla_find_aurore:
    "One of the most famous fashion designers in the world, the man behind Couture par Aurore, has taken notice of Palla's success and they've offered her a position."
    "I need to be sure she's ready before I put her in that position."
    call job_add ('palla', 'aurore') from _call_job_add_13
    return

label palla_find_anomalie:
    "Accessoires par Anomalie represents the best of the best. The only position that might possibly be equivalent to Couture par Aurore. If she can handle this job, she has a serious career going."
    call job_add ('palla', 'anomalie') from _call_job_add_14
    return

label palla_find_hawtbitches:
    "Since Palla and I agreed that she might be willing to do nude modelling, I did a search, and I can get her something at a site called hawtbitches.com."
    "She probably isn't going to like it, and I'll need to talk to her about it first."
    $ palla.flags.hawtbitchestalk = True
    return

label palla_find_sexypalla:
    "Palla's seen some success at hawtbitches and now they want to offer her her own website!"
    call job_add ('palla', 'sexypalla') from _call_job_add_15
    return

label palla_find_onlychix:
    "Oh wow. I just got an offer for Palla to do girl on girl porn for a site called onlychix. I wonder if she'd be up for that."
    $ palla.flags.onlychixtalk = True
    return

label palla_find_fucktoybitches:
    "Now that Palla's gotten a taste of lesbian porn, a pretty bad site named fucktoybitches wants her."
    "It looks pretty rough, but the money is great, and they promise they can make her into a full fledged porn star."
    $ palla.flags.fucktoybitchestalk = True
    return

label palla_find_pallapoundin:
    if renpy.has_label("palla_achievement_5") and not game.flags.cheat:
        call palla_achievement_5 from _call_palla_achievement_5
    "Palla's been offered the lead role in what they hope will be the first in a series of movies."
    "She starts off as the bored, rich housewife who fucks the pool guy and ends up travelling around the world collecting cocks."
    call job_add ('palla', 'pallapoundin') from _call_job_add_16
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
