init python:
    Event(**{
    "name": "office_event_01",
    "label": "office_event_01",
    "duration": 1,
    "conditions": [
        "'fafwm' not in DLCS",
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("dwaynedead"),
            IsFlag("cherie_ceooffer", False),
            ),
        ],
    "do_once": True,
    })

    Activity(**{
    "name": "blissard_meeting_spy_camera",
    "display_name": "Place spy camera",
    "max_girls": 0,
    "rooms": "mcoffice",
    "conditions": [
        HeroTarget(
            IsFlag("isceo"),
            IsFlag("workonblissard"),
            ),
        InInventory("spy_camera"),
        ],
    "label": "blissard_meeting_spy_camera",
    "icon": "spycamera",
    "do_once": True,
    })

    Event(**{
    "name": "office_harem_pimping_meeting",
    "label": "office_harem_pimping_meeting",
    "duration": 4,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("work_personal", "workhard_personal"),
            HasRoomTag("mcoffice"),
            IsFlag("isceo"),
            IsFlag("workonblissard", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_shiori_showdown",
    "priority": 500,
    "label": "office_audrey_shiori_showdown",
    "conditions": [
        "not Harem.find_by_name('office') or Harem.together(audrey, lavish, name='office')",
        IsTimeOfDay("morning"),
        HeroTarget(
            Not(OnDate()),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            IsFlag("isceo"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 140),
            MinStat("sub", 25),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        "Person.showdown(audrey, shiori)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_shiori_02",
    "priority": 500,
    "label": "office_audrey_shiori_02",
    "conditions": [
        TogetherInHarem('office', 'audrey', 'shiori'),
        IsDone("office_audrey_shiori_showdown"),
        IsTimeOfDay("morning"),
        HeroTarget(
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            IsFlag("officeharemaudshidelay", False),
            HasStamina(),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_lavish_showdown",
    "priority": 500,
    "label": "office_audrey_lavish_showdown",
    "conditions": [
        "not Harem.find_by_name('office') or Harem.together(audrey, shiori, name='office')",
        HeroTarget(
            IsRoom("date_restaurant"),
            IsFlag("isceo"),
            ),
        PersonTarget(lavish,
            OnDate(),
            MinStat("love", 120),
            MinStat("sub", 25),
            ),
        PersonTarget(audrey,
            Not(IsHidden())
            ),
        "Person.showdown(audrey, lavish)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_lavish_01",
    "priority": 500,
    "label": "office_audrey_lavish_01",
    "duration": 2,
    "conditions": [
        TogetherInHarem('office', 'audrey', 'lavish'),
        IsDone("office_audrey_lavish_showdown"),
        HeroTarget(
            Not(OnDate()),
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("officeharemaudlavdelay", False),
            HasStamina(),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_lavish_shiori_01",
    "priority": 500,
    "label": "office_lavish_shiori_01",
    "duration": 2,
    "conditions": [
        TogetherInHarem('office', 'lavish', 'shiori'),
        IsDone("office_audrey_shiori_02", "office_audrey_lavish_01"),
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            HasStamina(),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_lavish_shiori_showdown",
    "priority": 500,
    "label": "office_audrey_lavish_shiori_showdown",
    "conditions": [
        IsDone("office_audrey_shiori_02",
               "office_audrey_lavish_01",
               "office_lavish_shiori_01"),
        HeroTarget(
            IsRoom("date_beach", "date_nudistbeach"),
            IsFlag("isceo"),
            ),
        PersonTarget(audrey,
            OnDate(),
            ),
        PersonTarget(lavish,
            Not(IsHidden())
            ),
        PersonTarget(shiori,
            Not(IsHidden())
            ),
        "Person.showdown(audrey, lavish, shiori)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_audrey_lavish_shiori_01",
    "priority": 500,
    "label": "office_audrey_lavish_shiori_01",
    "duration": 2,
    "conditions": [
        TogetherInHarem('office', 'audrey', 'lavish', 'shiori'),
        IsDone("office_audrey_lavish_shiori_showdown"),
        HeroTarget(
            Not(OnDate()),
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("officeharemfourdelay", False),
            HasStamina(),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_aletta_audrey_lavish_shiori_showdown",
    "priority": 500,
    "label": "office_aletta_audrey_lavish_shiori_showdown",
    "conditions": [
        TogetherInHarem('office', 'audrey', 'lavish', 'shiori'),
        IsDone("office_audrey_lavish_shiori_01"),
        HeroTarget(
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("isceo"),
            HasStamina(),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        'Person.showdown(aletta, audrey, shiori, lavish)',
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_aletta_audrey_lavish_shiori_01",
    "priority": 500,
    "label": "office_aletta_audrey_lavish_shiori_01",
    "conditions": [
        TogetherInHarem('office', 'aletta', 'audrey', 'lavish', 'shiori'),
        IsDone("office_aletta_audrey_lavish_shiori_showdown"),
        HeroTarget(
            Not(OnDate()),
            IsActivity("work_personal", "workhard_personal"),
            IsFlag("officeharemfivedelay", False),
            HasStamina(),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_lavish_shiori_showdown",
    "priority": 500,
    "label": "office_lavish_shiori_showdown",
    "conditions": [
        'not Harem.together("lavish", "shiori")',
        HeroTarget(HasRoomTag("work")),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        Or(
            PersonTarget(lavish,
                MaxStat("sub", 49)
                ),
            PersonTarget(shiori,
                MaxStat("sub", 49)
                ),
            ),
        "Person.showdown(lavish, shiori)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_aletta_lavish_showdown",
    "priority": 500,
    "label": "office_aletta_lavish_showdown",
    "conditions": [
        'not Harem.together("aletta", "lavish")',
        HeroTarget(HasRoomTag("work")),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        Or(
            PersonTarget(aletta,
                MaxStat("sub", 49)
                ),
            PersonTarget(lavish,
                MaxStat("sub", 49)
                ),
            ),
        "Person.showdown(aletta, lavish)",
        ],
    "do_once": True,
    })

    Event(**{
    "name": "office_aletta_shiori_showdown",
    "priority": 500,
    "label": "office_aletta_shiori_showdown",
    "conditions": [
        'not Harem.together("aletta", "shiori")',
        HeroTarget(HasRoomTag("work")),
        PersonTarget(aletta,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        Or(
            PersonTarget(aletta,
                MaxStat("sub", 49)
                ),
            PersonTarget(shiori,
                MaxStat("sub", 49)
                ),
            ),
        "Person.showdown(aletta, shiori)",
        ],
    "do_once": True,
    })

label office_event_01:
    if hero.flags.isceo:
        scene bg ceo
    else:
        scene bg personal
    "I've been making a conscious effort to lose myself in work over the past few days."
    "And it seems to have been working, as my thoughts are focused on the job alone."
    "Maybe it would have been enough to do the trick as well."
    "That is if I hadn't heard a deliberate cough and looked up from my desk."
    "The door to my office is open."
    show cherie at center, zoomAt(1.0, (240, 720)) with dissolve
    "And I have no trouble recognising the figure standing in the doorway."
    mike.say "Oh..."
    mike.say "Hi, Cherie."
    mike.say "What can I do for you?"
    show cherie amused
    "Cherie doesn't answer at first, just raises a single eyebrow at the question."
    "I'm doing the best I can to sound simply surprised to see her in my office."
    "But we both know that there's far more going on under the surface."
    "Why else would the former CEO's wife come calling on someone of my pay-grade?"
    show cherie talkative
    cherie.say "I was just passing, [hero.name], that's all."
    cherie.say "And it's more what I can do for you..."
    show cherie normal at center, zoomAt(1.0, (300, 720)) with ease
    pause 0.1
    show cherie at center, traveling(1.5, 10.0, (640, 1040))
    "Cherie closes the door behind her and then walks the short distance to my desk."
    "Well, I say she walks it."
    "But a woman like her never just walks anywhere."
    "In reality, Cherie sashays over to my desk."
    "And every step shows off the goods she has on show as they jostle beneath her clothes."
    show cherie talkative
    cherie.say "I won't lie to you, [hero.name]."
    cherie.say "And I won't beat about the bush either."
    show cherie smile
    mike.say "Y...you won't?"
    show cherie at center, zoomAt(1.5, (680, 1040)) with ease
    "Cherie perches herself on the edge of my desk."
    show cherie at center, traveling(1.75, 0.3, (640, 1140))
    "And then she leans in close enough for me to smell the scent of her."
    "Close enough to see her chest rise and fall as I glance down her dress too!"
    show cherie talkative
    cherie.say "No, I want us to be totally candid with one another."
    cherie.say "At a time like this, it's important that we're of one mind."
    cherie.say "And one body too..."
    show cherie smile
    mike.say "Sure thing, Cherie."
    mike.say "Whatever you say!"
    "Cherie nods, seemingly happy with my response."
    show cherie whining
    cherie.say "Dwayne's death has left a massive hole, [hero.name]."
    cherie.say "A massive, gaping hole that's just begging to be filled!"
    show cherie sadsmile
    "I nod again, faster this time."
    "That's the effect her words are having on me."
    show cherie happy
    cherie.say "And I think you're just the man to fill that hole."
    cherie.say "So what do you say, [hero.name]?"
    cherie.say "Will you fill my hole?"
    cherie.say "Will you step up and become the new CEO of this company?"
    show cherie normal
    "Wait a second - did she just say what I think she did?"
    "Did Cherie just say she wants to make me the head of the company?!?"
    menu:
        "Agree":
            "She is - Cherie's actually offering me Dwayne's job!"
            "And if she's offering me that, what else comes with it too?"
            "Maybe this is just karma, you know?"
            "The cosmos finally paying me back for all the shit I've been through."
            mike.say "You mean it, Cherie?"
            mike.say "You want me to step into Dwayne's shoes and run the company?"
            "Cherie chuckles at my eagerness."
            show cherie at center, traveling(2.0, 0.3, (640, 1340))
            "She leans in closer, stroking my cheek."
            "I can feel the warmth of her breath on my face."
            "It's like she's teasing me, using herself to show what's on offer."
            "And all I have to do is reach out and take it!"
            show cherie talkative
            cherie.say "Well, not exactly like Dwayne."
            cherie.say "For one thing, I'll be taking a far more hands on role."
            cherie.say "So I'll be there for you, whenever you need me."
            show cherie happy
            cherie.say "You could think of me as a resource."
            cherie.say "Put me to any use that you wanted..."
            show cherie normal
            "It takes me a short while to realise that Cherie's stopped talking."
            "As well as that she's now waiting for my response."
            "I seem to have been staring at her chest the whole time."
            show cherie talkative
            cherie.say "Well, [hero.name] - do you want the job?"
            show cherie normal
            mike.say "Of course I do, Cherie."
            mike.say "I'd have to be insane to turn down a woman like you..."
            mike.say "A chance like this...I...I mean a chance like this!"
            show cherie smile
            "Cherie's smile is slow and wide, like that of a satisfied cougar."
            show cherie normal at center, traveling(2.25, 0.3, (640, 1380))
            "She cups my chin in the palm of her hand, pulling me closer still."
            "And then plants a kiss upon my forehead."
            show cherie happy at center, traveling(2.0, 0.3, (640, 1340))
            cherie.say "That's wonderful, [hero.name]."
            cherie.say "You've made the right decision."
            show cherie smile at center, traveling(1.0, 0.5, (340, 720))
            "Cherie stands up and walks slowly out of my office."
            hide cherie with easeoutleft
            "I wait until she's gone to let out a gasp of amazement."
            "Is this really happening?"
            "Am I actually going to become CEO of the whole company?!?"
            $ hero.flags.isceo = True
            if aletta.status == "boss":
                $ aletta.status = "employee"
            if audrey.status == "coworker":
                $ audrey.status = "employee"
            if lavish.status == "coworker":
                $ lavish.status = "employee"
            $ hero.flags.workonblissard = TemporaryFlag(True, 7)
            $ game.flags.capped_promotion = False
        "Refuse":
            "What in the hell is she thinking?"
            "There's no way that I'm qualified for a promotion the likes of that!"
            "And what about the way it ended for the last guy in that position?"
            "Whatever the official verdict on Dwayne's death says, he's still dead."
            "And the chances are that if he hadn't been the CEO, he'd still be alive right now!"
            mike.say "It's not like I'm not flattered."
            mike.say "But no way, Cherie."
            mike.say "I can't take on that kind of responsibility."
            show cherie at center, traveling(2.0, 0.3, (640, 1340))
            "Cherie leans in closer still, stroking me under the chin."
            "She's so close right now that she's almost touching me."
            "Almost but not quite - like she's showing me what's just within reach."
            "If only I have the courage to reach out and take it..."
            show cherie talkative
            cherie.say "It's not like that, [hero.name]."
            cherie.say "I'd be there every step of the way."
            cherie.say "Available for your every need."
            cherie.say "I'd let you put me to any use you wanted..."
            show cherie normal
            "I thrust myself backwards in my chair until it hits the wall."
            mike.say "NO!"
            mike.say "I mean...no, Cherie."
            mike.say "The company is yours now."
            mike.say "You need to appoint someone that's up to the job."
            show cherie sadsmile
            "Cherie looks disappointed at this."
            show cherie at center, traveling(1.5, 0.3, (640, 1040))
            "She shakes her head as she pulls away from me and stands up again."
            show cherie whining
            cherie.say "If that's the way you feel, [hero.name]."
            cherie.say "But I think you'll find that you're making a mistake..."
            show cherie at center, traveling(1.0, 0.5, (340, 720))
            "Still shaking her head at my decision, Cherie walks out of my office."
            hide cherie with easeoutleft
            "I wait until she's gone to let out a weary breath."
            "I'm sure that she thought she was showing her gratitude."
            "But there's no way I want to be where the buck stops in this company!"
    $ hero.replace_activity()
    return

label blissard_meeting_spy_camera:
    show chibi spy
    "It takes a little while, but I find a good spot for the camera that can see the entire room, and is nearly impossible to see if you're not looking for it."
    $ hero.lose_item('spy_camera')
    $ game.flags.blissardspy = True
    return

label office_harem_pimping_meeting:
    scene expression f"bg {game.room}"
    $ hero.replace_activity()
    "I feel like I've been holding my breath the entire time that I've been in this damn meeting."
    "It's all that I've been working on for the past few weeks, and this is the moment of truth."
    "Either I land the deal with Blissard Games, or I crash and burn."
    "And in the case of the latter, I can kiss my 10K bonus goodbye too."
    "Which is more than enough motivation to make me move heaven and earth for the sake of the deal!"
    "So far, things seem to be going well, no major signs of dissatisfaction from the other side."
    show victor as tom zorder 3 at right5, blacker
    show ryan tux smile as dick zorder 2 at left5, blacker
    show shawn as harry zorder 1 at center, blacker
    with dissolve
    "All three of the guys they sent over are pouring over the paperwork I've handed them."
    "And they seemed to be paying attention throughout the presentation too."
    "I have a pen in one hand and the contracts in the other."
    "All I need to do now is wait for Tom, Dick and Harry to sign on the dotted line..."
    show victor as tom at right5, blacker, startle
    "Tom" "Well, what do you guys think?"
    show ryan as dick at left5, blacker, startle
    "Dick" "Everything seems to be in order, Tom."
    show shawn as harry at center, blacker, startle
    "Harry" "I'm with Dick - no problems for me either."
    "I watch as Tom exchanges nods with his colleagues and then looks over towards me."
    "It's all I can do to keep from thrusting the contract straight under his nose right then."
    "But I know how these things go."
    "There's likely going to be some more small talk to endure."
    show victor as tom at right5, blacker, startle
    "Tom" "I won't lie to you, [hero.name]."
    "Tom" "We like what we've seen here today."
    show ryan as dick at left5, blacker, startle
    "Dick" "I'll say we do!"
    show shawn as harry at center, blacker, startle
    "Harry" "We like it a hell of a lot!"
    mike.say "Th...that's great!"
    mike.say "So you're ready to sign the contracts, yeah?"
    mike.say "As soon as we do that, it's a done deal."
    "Tom smiles broadly, and I hope at my enthusiasm."
    "He looks at Dick and Harry, both of whom smile too."
    "And then he looks back at me again."
    show victor as tom at right5, blacker, startle
    "Tom" "Oh sure, [hero.name]."
    "Tom" "We're itching to sign, of course we are."
    "Tom" "But first, how about we talk about another itch?"
    "I can't help showing the fact that I'm puzzled by what Tom just said."
    "We've been through everything in painstaking detail already."
    "Surely there's nothing he's noticed that I could have missed?"
    mike.say "I...I'm not sure I follow, Tom."
    mike.say "What's this itch you're talking about?"
    show victor as tom at right5, blacker, startle
    "Tom" "You know how it is, [hero.name]."
    show ryan as dick at left5, blacker, startle
    "Dick" "All of the paperwork is just a formality."
    show shawn as harry at center, blacker, startle
    "Harry" "What we're talking about is more a matter of corporate hospitality."
    "Harry" "Just scratching an itch, you understand?"
    "At the mention of hospitality, my eyes dart over to the platter on the table."
    "It's still covered in the remains of the working lunch that I ordered in for the meeting."
    "All of the food on it was devoured as we poured over the paperwork."
    "Tom follows my eye, and then lets out a laugh as he shakes his head."
    show victor as tom at right5, blacker, startle
    "Tom" "No, [hero.name] - not that kind of hospitality!"
    "Dick" "Like we already said, we like what we've seen today."
    "Harry" "Specifically, we like the look of your female colleagues, [hero.name]."
    "I blink maybe half a dozen times before the meaning of his words sink in."
    "And then my eyes go wide as I realise they're not simply paying the girls a compliment."
    mike.say "Y...you're not asking for their numbers, are you?"
    "Tom, Dick and Harry shake their heads as one."
    mike.say "You want more than that, don't you?"
    "The three of them nod again, but this time their smiles are wolfish."
    if not shiori.hidden:
        show victor as tom at right5, blacker, startle
        "Tom" "Myself, I like the look of the little cutie with the huge tits."
        "He must mean Shiori."
        "Tom" "How about you guys?"
    if not audrey.hidden:
        "Dick" "I like the one with the long, dark hair."
        "Dick" "I'm getting hard just thinking about her!"
        "That must be Audrey."
    if not lavish.hidden:
        "Harry" "Oh, man - that girl with the bob and the huge eyes."
        "Harry" "I'd buy that for a dollar!"
        "That can only be Lavish he's talking about."
    show victor as tom at right5, blacker, startle
    "Tom" "I don't know how you can concentrate with those girls in the office, [hero.name]!"
    "Tom" "You let us have some serious fun with them, and this thing's in the bag."
    "I swallow hard, realising that they're totally serious."
    "I want to land the deal and earn my 10K."
    "But I'm going to have to pimp out my colleagues to do it!"
    menu:
        "Offer all three" if not (audrey.hidden or lavish.hidden or shiori.hidden):
            "But then why not?"
            "After all, I'm the one that's sweated blood for this deal."
            "And every one of them is going to benefit from it too."
            "So in a way, all they'd be doing is earning their share of the profits."
            mike.say "Okay, guys - you've got a deal."
            mike.say "Just wait here while I go talk to the girls, okay?"
            "Tom, Dick and Harry exchange looks of naked anticipation as I get up to leave."
            "Now all I have to do is convince three of my female co-workers this is a good idea!"
            call office_harem_pimping_audrey_lavish_shiori from _call_office_harem_pimping_audrey_lavish_shiori
        "Offer Shiori" if not shiori.hidden:
            "Tom's the guy in charge here, that's been obvious from the start."
            "Maybe I can work on that to make things easier for me?"
            "And if all he wants is Shiori, then maybe the others will just fall in line."
            mike.say "Three girls in here's going to get way too crowded, trust me."
            mike.say "And anyway, Shiori can handle all three of you guys."
            mike.say "That's the girl you like the look of, Tom."
            "Dick and Harry are about to object, but Tom ignores them."
            show victor as tom at right5, blacker, startle
            "Tom" "Whatever you say, [hero.name]."
            "Tom" "But she'd better be as good as three girls!"
            "They exchange looks of naked anticipation as I get up to leave."
            "Now all I have to do is convince Shiori this is a good idea!"
            call office_harem_pimping_shiori from _call_office_harem_pimping_shiori
        "Offer Audrey" if not audrey.hidden:
            "All of them want a different girl, which could get messy."
            "But Dick showed particular interest in Audrey just now."
            "So maybe I can sell her to the other two as well?"
            mike.say "You're the one with the best eye, Dick."
            mike.say "Audrey's the prize slut around here."
            mike.say "Why, I bet she could handle all three of you!"
            "Tom and Harry look like they're about to object."
            "But Dick takes the bait before they can shut him up."
            "Dick" "That sounds great, [hero.name]!"
            "Dick" "We'll take her over the other two."
            "Tom and Harry stare daggers at Dick, but he seems not to notice."
            "Now all I have to do is convince Audrey this is a good idea!"
            call office_harem_pimping_audrey from _call_office_harem_pimping_audrey
        "Offer Lavish" if not lavish.hidden:
            "All of them want a different girl, which could get messy."
            "But Harry showed particular interest in Lavish just now."
            "So maybe I can sell her to the other two as well?"
            mike.say "You're the one with the best eye, Harry."
            mike.say "Lavish might look innocent, but she's a slut underneath it all."
            mike.say "Why, I bet she could handle all three of you!"
            "Tom and Dick look like they're about to object."
            "But Harry takes the bait before they can shut him up."
            "Harry" "That sounds great, [hero.name]!"
            "Harry" "We'll take her over the other two."
            "Tom and Dick stare daggers at Harry, but he seems not to notice."
            "Now all I have to do is convince Lavish this is a good idea!"
            call office_harem_pimping_lavish from _call_office_harem_pimping_lavish
        "Offer Aletta" if not aletta.hidden:
            "All of them want a different girl, which could get messy."
            "But what if there's another choice entirely?"
            "None of them have laid eyes on Aletta yet."
            "And she's practically a salary man's wet dream!"
            mike.say "Trust me, you don't want to waste your time on those little sluts."
            mike.say "You'd be lowering yourself, fucking beneath your grade."
            mike.say "The girl you want is Aletta, real corporate skirt."
            mike.say "Hell, I bet she could handle all three of you at once!"
            "Tom, Dick and Harry exchange meaningful glances."
            "And I can see that the idea appeals to them."
            "They probably get to fuck the clerical staff back at Blissard all the time."
            "But what I'm offering them is more of a delicacy, far rarer prey."
            show victor as tom at right5, blacker, startle
            "Tom" "Whatever you say, [hero.name]."
            "Tom" "But she'd better be as good as three girls!"
            "Great - now all I have to do is convince Aletta this is a good idea!"
            call office_harem_pimping_aletta from _call_office_harem_pimping_aletta
        "Refuse":
            "Fuck, I always thought this kind of sleazy shit just happened in the movies."
            "But these guys are acting like it's no big deal, just part of the negotiations."
            "If I do this, how am I going to be able to look myself in the mirror?"
            "That money's going to feel tainted, and I'm going to feel like a pimp!"
            "No, fuck these guys!"
            "Who in the hell do they think they are!"
            mike.say "I don't know how things work over at Blissard, Tom."
            mike.say "But here we take a pretty dim view of sexual harassment and exploitation."
            "At this, Tom, Dick and Harry's expressions darken."
            "Tom shoves the paperwork before them back at me in an aggressive manner."
            show victor as tom at right5, blacker, startle
            "Tom" "Don't be stupid, [hero.name]."
            "Tom" "This deal's all but in the bag."
            "Dick" "Yeah, [hero.name], be reasonable."
            "Dick" "All we want is some pussy."
            "Harry" "You really want to be the guy that blew the deal?"
            "Harry" "And over what - a couple of paper-pushing sluts?!?"
            "Before I was just shocked at the notion of what they're suggesting."
            "But now I'm actually starting to get mad."
            if game.flags.blissardspy:
                mike.say "I'm so glad that you chose those particular words, guys."
                mike.say "It makes what I have to do next so much easier!"
                "Tom, Dick and Harry look at each other in a puzzled manner."
                mike.say "Smile for the camera, boys!"
                show victor as tom at right5, blacker, startle
                "Tom" "What the hell is this?"
                "Dick" "You were recording this whole time?"
                "Harry" "Y...you're not serious?"
                mike.say "No one else has to see what the camera's recorded, gentlemen."
                mike.say "Provided, of course, that we seal the deal before you walk out that door!"
                show victor as tom at right5, blacker, startle
                "Tom" "You asshole - this is blackmail!"
                mike.say "I guess it is!"
                mike.say "So what is it going to be, huh?"
                "One by one, Tom, Dick and Harry line up so sign the contracts."
                "They curse and swear under their breath, but they do it all the same."
                "Once they're gone, I lean back in my seat, feeling pretty pleased with myself."
                "I got the deal, secured my 10K and all without pimping out my female colleagues."
                "Not bad for a day's work!"
                $ game.flags.blissardsealed = True
                $ hero.money += 10000
                return
            else:
                mike.say "Okay, this meeting's officially over."
                mike.say "Get out of here right now."
                mike.say "Do it before I call security and have them throw your asses out!"
                "Tom, Dick and Harry get up to leave, shaking their heads in disbelief."
                "But not before Tom takes the time to tear up the contracts and toss them aside."
                "I don't rise to the bait, simply keeping quiet as they file out."
                "Sure, it feels pretty shitty to be 10K worse off right now."
                "But I know that it was the price of keeping my colleagues safe from those creeps."
                $ game.flags.blissardoff = True
    if not game.flags.blissardoff:
        call office_harem_pimping_afterwards from _call_office_harem_pimping_afterwards
    return

label office_harem_pimping_aletta:
    scene bg black
    show bg alettaoffice
    "As if things weren't bad enough with the guys from Blissard wanting a fuck to seal the deal."
    "I have to go and suggest that they indulge themselves with Aletta, rather than the girls they wanted!"
    "What in the hell was I thinking when I sold them on that idea?"
    "At least in the case of Audrey, Lavish and Shiori I could have tried to pull rank on them."
    "Aletta's not the kind of person that I can just boss around either."
    "So I have no idea just how I'm going to get her to agree to this!"
    show aletta work
    "And I still don't when I bump into her a few moments later."
    "Aletta raises an eyebrow at the sight of me."
    show aletta surprised at startle
    aletta.say "Oh, [hero.name], I wasn't expecting to see you here."
    show aletta normal
    show fx question
    aletta.say "Shouldn't you be in the meeting room right now?"
    mike.say "Erm, yeah..."
    mike.say "It's all over and done with, save for the signatures."
    show aletta dreamy
    aletta.say "Hmm..."
    aletta.say "Isn't that the most important part?"
    aletta.say "Nothing's final until they sign the contracts, after all."
    show aletta normal
    mike.say "Well, there's a small problem with that."
    mike.say "The guys from Blissard, they want something before they'll sign!"
    show aletta dreamy
    "Aletta takes a moment to look around the office."
    show aletta normal
    "And then she looks back at me in a pointed manner."
    aletta.say "And I take it what they want is out here?"
    "I can feel a lump building in my throat."
    "I swallow hard, knowing there's no way out of this."
    "At least not if I want to keep my bonus!"
    mike.say "Yeah, Aletta, you could say that."
    mike.say "You could also say that I'm kind of looking at it right now too!"
    show aletta annoyed
    "Aletta blinks at this, not fully understanding what I mean."
    show fx question
    aletta.say "What are you talking about, [hero.name]?"
    aletta.say "Do you need me to help you close the deal?"
    aletta.say "I have had some serious experience as a negotiator in the past."
    show aletta normal
    mike.say "Ah, not exactly, Aletta."
    mike.say "But you could help me close the deal if you..."
    mike.say "Well, if you agree to show the guys from Blissard a good time?"
    show aletta dreamy
    aletta.say "What do you mean by 'a good time', [hero.name]?"
    aletta.say "Sing them a song?"
    aletta.say "Do a little dance?"
    "I'm wincing even before the words are out of my mouth."
    "Like I expect Aletta to slap me the moment she hears what I have to say."
    mike.say "No, Aletta."
    mike.say "I was more meaning let them have sex with you..."
    if aletta.sub >= 75:
        "It's right about now that I begin to remember the other side to Aletta."
        "The one that she tries so hard to keep hidden from everyone else."
        "The same side of her that would probably jump at the chance to be used by a stranger."
        "And maybe turn somersaults at the chance to make that three strangers!"
        mike.say "Great way to release some of that tension you have, Aletta."
        mike.say "You know, burn off the stress that you're always telling me about..."
        "I watch as Aletta glances around the office again."
        "But this time I can see that she's doing it because she's self-conscious."
        "Her eyes are growing wider by the moment, cheeks flushing red."
        show aletta normal blush
        aletta.say "I...I don't know what you mean, [hero.name]."
        aletta.say "I could never do anything like that..."
        mike.say "Oh come on, Aletta."
        mike.say "After the things that you've had me do to you?"
        mike.say "Right here in this very same office?"
        mike.say "I'd have thought you were just the woman for the job!"
        show aletta at center, zoomAt(2, (640, 1380))
        "Aletta leans in as close as she dares."
        "And then she whispers, almost hisses, into my ear."
        show aletta flirt
        aletta.say "Alright, [hero.name], alright!"
        aletta.say "You know me too well."
        aletta.say "But this is a one off, okay?"
        aletta.say "You can't just pimp me out every time you need to close a deal!"
        mike.say "I get it, Aletta."
        mike.say "This is a one-off."
        mike.say "And nobody else needs to know about it - trust me."
        "Aletta nods and grabs hold of my arm."
        "And then she almost drags me in the direction of the meeting room."
        call foursome_office_aletta from _call_foursome_office_aletta
    elif hero.charm >= 90:
        "Maybe I've been coming at this from the wrong direction."
        "I've been making this about Aletta helping me."
        "When it would have made more sense to make it about her instead."
        mike.say "All joking aside, Aletta."
        mike.say "I really do need your help!"
        show aletta annoyed
        show fx question
        aletta.say "Why is that, [hero.name]?"
        aletta.say "Because you won't let those guys fuck you?"
        mike.say "No, Aletta, that's not what I mean."
        mike.say "Look, we both know that you should have been in on this from the start."
        mike.say "If you'd been helping me out, then it wouldn't have come to this."
        show aletta normal
        "Aletta leans back a little way, screwing her face up as she does so."
        "I can tell that she likes what she's hearing."
        "But maybe she's still a little sceptical."
        show aletta dreamy
        aletta.say "Are you being serious, [hero.name]?"
        aletta.say "Because you're damn right, of course."
        aletta.say "But you're not usually the kind of guy to come out and admit the truth!"
        mike.say "Of course I mean it, Aletta!"
        mike.say "I mean, look at the mess that I've made of things."
        mike.say "You'd never have ended up offering them sex with one of your co-workers!"
        show aletta normal
        aletta.say "Well, that IS true."
        "I can tell from the tone of her voice that Aletta's taken the bait."
        "She's changed from being angry with me to looking at things in a removed, clinical manner."
        "When she's like this, Aletta's all business and there's no room for emotions whatsoever!"
        aletta.say "But you've backed yourself into a corner with this sex clause, [hero.name]."
        aletta.say "You'll never be able to renegotiate from this position."
        mike.say "So what you're saying is that I'm screwed - if you pardon the pun!"
        mike.say "They've won and I've lost..."
        aletta.say "Well, with an attitude like that you sure have!"
        aletta.say "But if these guys get what they want, they're going to become distracted."
        aletta.say "Then you can catch them unawares and take them for all they're worth!"
        mike.say "But, Aletta..."
        mike.say "That would mean..."
        show aletta at center, zoomAt(2, (640, 1380)) with hpunch
        "Before I can say anything more, Aletta grabs hold of my wrist in an iron grip."
        "She actually hurts me as she begins to drag be across the office and back to the meeting room."
        aletta.say "It's not about the sex anymore, [hero.name]."
        aletta.say "You have to be able to see past that - see the bigger picture."
        aletta.say "This is about the deal, and not letting these guys screw you over."
        aletta.say "Because if they do, then they're not just screwing you and me."
        aletta.say "They're screwing the whole damn company!"
        $ aletta.flags.blissardbribe = True
        call foursome_office_aletta from _call_foursome_office_aletta_1
    else:
        "And I was quite right to brace myself for a blow too."
        play sound punch_hard
        pause 0.2
        with hpunch
        "That's because Aletta stings me with a good one mere seconds later."
        "It's so hard that I actually see stars for a moment afterwards too!"
        show aletta angry
        aletta.say "I'm going to pretend that I didn't hear that, [hero.name]."
        aletta.say "And you're going to pretend that this conversation never happened."
        aletta.say "Because if you don't, I'll do more than slap you next time."
        hide aletta with dissolve
        "I can't help but nod repeatedly as I nurse my stinging cheek."
        "And all I can think is that I probably got off lightly too!"
        "After all, Aletta would have been well within her rights to cause a scene."
        "That and call HR the moment she was done screaming at me as well!"
        "She turns on her heel with a testy snort and walks off in the other direction."
        "Which leaves me to wonder how I could have been so stupid."
        "That and how I'm going to miss that 10K bonus!"
        $ aletta.sub -= 25
        $ aletta.love -= 50
        $ game.flags.blissardoff = True
    return

label office_harem_pimping_audrey:
    scene bg black
    show bg office
    "I'm dreading the task ahead from the very moment that I hear the door swing closed behind me."
    "Couldn't I have chosen any of the other girls in the office to do this thing?"
    "Sure, Lavish, Shiori or even Aletta would have been hard to sell on it."
    "But Audrey?"
    "What was I even thinking?!?"
    "I know that she likes to cause trouble around here."
    "But this is a different thing entirely."
    "This is me asking her to get up to shenanigans for my own benefit."
    "And being that she's one for making mischief, Audrey's as likely to say no just for the hell of it!"
    show audrey work
    "That's probably why she spots that I'm nervous as soon as she lays eyes on me..."
    show audrey annoyed
    audrey.say "Oh-oh, someone's looking especially shifty today!"
    audrey.say "I take it that means the meeting isn't going too well, [hero.name]?"
    "I swallow audibly, trying to assert myself and take control of the situation."
    show audrey normal
    mike.say "No need to worry about that, Audrey."
    mike.say "I've actually got them on the verge of signing."
    mike.say "That's what I wanted to talk to you about..."
    "Only now does Audrey cock her head on one side and look at me with real interest."
    show audrey annoyed
    audrey.say "So why are you out here talking to me, [hero.name]?"
    audrey.say "Shouldn't you be in there making sure the ink's dry on it?"
    mike.say "Well, that's the thing, Audrey."
    mike.say "I kind of need your help to make them sign."
    mike.say "It's just a formality, but they want to see you in there..."
    show audrey frown
    "Audrey frowns at this, still regarding me with suspicion."
    audrey.say "Can't they see me from the other side of the office?"
    audrey.say "You know, this is getting pretty weird, [hero.name]!"
    mike.say "Ah...no, Audrey."
    mike.say "It's the amount of you they want to see."
    mike.say "Which is all of you - specifically without your clothes on."
    "Any other girl in the office I would have expected to freak out at that admission."
    show audrey joke
    "But not Audrey, who proves me right when her expression becomes suddenly sly and amused."
    audrey.say "Do you mean what I think you mean?"
    show fx exclamation
    audrey.say "You dirty motherfucker!"
    audrey.say "You offered me up to them as a sweetener, didn't you?"
    mike.say "No!"
    mike.say "Well...not exactly."
    mike.say "They noticed you on their way into the office."
    mike.say "And they...liked what they saw!"
    mike.say "All I really did was agree to ask."
    audrey.say "Ask what, [hero.name]?"
    audrey.say "Come on, I want to hear you say it out loud!"
    mike.say "Okay, Audrey - I agreed to ask if you'd fuck them."
    mike.say "There, I said it - are you happy now?"
    if audrey.sub >= 75:
        "It might not be obvious to someone that doesn't know her as well as I do."
        show audrey flirt
        "But I can see the actual moment when Audrey drops the act and really considers it."
        "I've found that her facade of confidence and defiance is actually just that - a facade."
        "Underneath it she's pretty insecure and in need of validation."
        "So me offering her the chance to curry favour by letting them fuck her..."
        audrey.say "O...okay, [hero.name]."
        audrey.say "I'll do it."
        audrey.say "But only because you asked me to, yeah?"
        "I nod with a smile on my face."
        mike.say "Thank you, Audrey."
        mike.say "You're an asset to the company."
        mike.say "And a very good girl to boot!"
        show audrey flirt blush
        "Audrey's cheeks flush red at my compliments."
        "She hurries to follow me as I lead the way back to the meeting room."
        "And the whole time I'm amazed at how easy she is to manipulate."
        "That is, once you know where and how to yank her chain."
        call foursome_office_audrey from _call_foursome_office_audrey
    elif hero.charm >= 90:
        audrey.say "You see the thing is, I'm just not motivated - you know?"
        audrey.say "I get it that you are, what with your bonus and all."
        show audrey frown
        show fx question
        audrey.say "But me - what do I care?"
        "I stare at Audrey open-mouthed as I realise what she's hinting at."
        "The manipulative little bitch wants a cut of my 10K bonus!"
        "But then she does kind of have me at a disadvantage right now."
        "So all I can do is sigh and nod wearily."
        mike.say "Okay, Audrey."
        mike.say "I see where this is going."
        mike.say "Would five grand be enough to motivate you?"
        "Audrey smiles sweetly at this, nodding her head."
        show audrey normal
        audrey.say "It's a start, [hero.name]."
        audrey.say "You do that and I'll do them!"
        mike.say "Fine, fine..."
        mike.say "It's a deal."
        "Audrey nods and lets me lead her back towards the meeting room."
        "Sure, it just cost me ten percent to get the deal done."
        "But from where I'm standing, that's a sound investment."
        "Especially when the alternative is a big, fat zero!"
        $ audrey.flags.blissardbribe = True
        call foursome_office_audrey from _call_foursome_office_audrey_1
    else:
        show audrey happy
        "Audrey snorts a filthy laugh and shakes her head."
        show audrey normal
        "Her arms are crossed over her chest and her stance is now defensive."
        audrey.say "I'm happy that I made you say it, but that's all."
        audrey.say "And if you think I'm going in there to fuck those guys..."
        show audrey joke
        audrey.say "Well, you must be dumber than you look!"
        "What the hell?!?"
        "She put me through all of that just to say no?"
        mike.say "Audrey, please!"
        mike.say "This deal is so important to the company..."
        show audrey happy
        "Audrey cuts me off in mid-flow."
        "She laughs again as she shakes her head."
        show audrey joke
        audrey.say "Yeah, [hero.name], it's important to them - and you."
        show audrey angry
        show fx anger
        audrey.say "But me, what do I care?"
        audrey.say "I'm not the one with a bonus riding on it!"
        "With that, she turns her back on me and walks away."
        "And I can see my chances of getting that 10K walking away too!"
        $ audrey.sub -= 5
        $ audrey.love -= 5
        $ game.flags.blissardoff = True
    return

label office_harem_pimping_lavish:
    scene bg black
    show bg office
    "It takes a couple of steps from the door of the meeting room for me to actually start panicking."
    "Well, maybe not having a full-on attack of anxiety, nothing so dramatic."
    "But what I'm feeling right now is more than enough to make me aware of the position I've put myself in."
    "Do I really want that 10K bonus badly enough to do this?"
    "To actually walk up to Lavish and ask her to let these guys have their way with her?"
    "I shake my head as I walk through the office looking for the girl in question."
    "No, it's not just about the money, of course not."
    "It's about the need to close the deal here."
    "The need to be ruthless enough to get it done no matter what the cost."
    "Yeah, [hero.name], just keep telling yourself that."
    "And maybe you'll start to believe it as well!"
    show lavish work with dissolve
    "Just then, Lavish walks out of a door and almost collides with me."
    "Maybe it's my need to find her that does it."
    "Or maybe it's just one of those weird coincidences."
    "Either way, I jump on the chance before my conscience can get the better of me."
    show lavish surprised at startle
    lavish.say "Oh...[hero.name]!"
    lavish.say "Sorry, I wasn't looking where I was going..."
    mike.say "No worries, Lavish - neither was I!"
    mike.say "Actually, there was something that I needed to talk to you about..."
    show lavish normal
    lavish.say "Sure, [hero.name], I'm not rushing to meet a deadline or anything."
    show lavish happy
    lavish.say "By which I don't mean that I'm slacking off!"
    "I wave away Lavish's attempt at making a joke out of it."
    "I can't allow myself to get distracted with office banter right now."
    mike.say "Forget about it, Lavish."
    mike.say "This is a serious matter."
    mike.say "But it's kind of serious in a different way."
    show lavish normal
    "Lavish nods, trying to look like she's intent on hearing what I have to say."
    "But I can see from the way her eyes widen that she's already fearing the worst."
    mike.say "You know I've been trying to close this deal, right?"
    mike.say "And that the guys from Blissard are here to do that today?"
    show lavish annoyed
    lavish.say "Of course, [hero.name]."
    lavish.say "You've been working so hard on it too!"
    mike.say "Well, we've kinda hit bump in the road."
    show fx question
    lavish.say "Oh no!"
    mike.say "Oh yeah!"
    mike.say "They want one more thing before they'll sign on the dotted line."
    show lavish surprised
    "Lavish looks at me, her eyes now seeming impossibly large."
    lavish.say "What do they want?"
    "I take a deep breath and do all I can to prepare myself."
    "Here goes nothing..."
    mike.say "They...they want you, Lavish."
    lavish.say "M...me?"
    lavish.say "What do you mean they want me?"
    mike.say "Come on, Lavish."
    mike.say "Don't play innocent with me."
    mike.say "They saw you on their way in here and they went crazy."
    show lavish surprised at center, vshake
    show fx exclamation
    lavish.say "You mean they want to...to have SEX with me?!?"
    mike.say "Look, Lavish, I know this kind of thing isn't supposed to happen."
    mike.say "But this is the real world, and sometimes we have to do whatever it takes!"
    if lavish.sub >= 75:
        "Lavish looks down at her feet, as though my words have really affected her."
        "She nods, still not lifting her gaze up as she does so."
        show lavish embarrassed
        lavish.say "O...okay, [hero.name]."
        lavish.say "If you say so..."
        "I'd thought that if I could just get Lavish to agree to it then I'd feel better."
        "But the way that she caves in and becomes meek just makes me feel that much more guilty."
        "Nevertheless, I'm committed now."
        "And so I push down my feelings of guilt and press on regardless."
        mike.say "Good girl, Lavish."
        mike.say "I knew that I could rely on you."
        "Lavish nods again as she lets me point her in the direction of the meeting room."
        "But she doesn't say another word the entire time we're walking towards the door."
        "Which leaves me alone with the guilt that I'm feeling at making her do this..."
        call foursome_office_lavish from _call_foursome_office_lavish
    elif hero.charm >= 90:
        "Maybe the trick here is that I need to make this more appealing to Lavish?"
        "After all, I just said that this is for the sake of the deal with Blissard."
        "So what if I give her a practical motivation to do what I want?"
        mike.say "Okay, Lavish, let's get serious for a minute."
        mike.say "You want to get on here, don't you?"
        mike.say "You have ambitions to climb the corporate ladder, right?"
        show lavish normal
        "Lavish nods slowly as she waits to see just where this is going."
        mike.say "Well it helps to have people in your debt."
        mike.say "To have someone above you that owes you a favour."
        "Lavish nods again, and I think I can see recognition on her face."
        show lavish embarrassed
        lavish.say "If I do this, you'll..."
        lavish.say "You'll do something for me?"
        mike.say "That's it exactly, Lavish."
        mike.say "The next time you go for a raise or a promotion."
        mike.say "I'll move heaven and earth to make sure you get it, okay?"
        show lavish flirt
        "Lavish looks me straight in the eye, like she's trying to gaze into my soul."
        "It makes me feel more than a little nervous, but I endure it as best I can."
        "For a while, I'm convinced that she's going to open her mouth and say no."
        show lavish normal
        lavish.say "Ah..."
        lavish.say "Okay, [hero.name], okay."
        lavish.say "But this stays between you and me."
        lavish.say "Well...you, me and the guys from Blissard, yeah?"
        "I can't help letting out a sigh of relief at Lavish saying yes."
        "But I nod in agreement all the same, eager to seal the deal."
        mike.say "You have my word, Lavish."
        mike.say "No one else will ever know about it."
        "Lavish nods at this, still looking more than a little nervous."
        "She lets me point her in the direction of the meeting room."
        "But she doesn't say another word the entire time we're walking towards the door."
        "Which leaves me alone with the guilt that I'm feeling at making her do this..."
        $ lavish.flags.blissardbribe = True
        call foursome_office_lavish from _call_foursome_office_lavish_1
    else:
        show lavish annoyed
        "All of a sudden, Lavish seems to shake off the initial shock of what I just proposed."
        "In that short time, she goes from being scared to looking at me in a defiant manner."
        "And when she shakes her head and takes a confident stance, I pretty much know it."
        "She's not going to let herself get fucked, which means that I'm fucked myself!"
        show lavish angry
        lavish.say "No, [hero.name], we don't have to do things like that."
        lavish.say "And I'm not going to be treated like this in the workplace either!"
        mike.say "Whoa, Lavish, come on..."
        show fx anger
        lavish.say "No, I will not!"
        lavish.say "What's going to happen is that we're going to forget this ever happened."
        lavish.say "Because if you don't, I'm sure HR will be very interested in hearing about it!"
        hide lavish with dissolve
        "And with that, Lavish turns her back on me and storms away."
        "I watch her disappear, taking all hope of getting that 10K bonus with her."
        $ lavish.sub -= 5
        $ lavish.love -= 5
        $ game.flags.blissardoff = True
    return

label office_harem_pimping_shiori:
    scene bg black
    show bg office
    "It's only when I close the door behind me and hurry off to find Shiori that I actually start to think about this."
    "Am I actually going to walk up to one of the girls that works under me and ask her to put out for these guys?"
    "Even with that thought inside of my head, I don't stop and march right back in there to tell them no way."
    "So I guess the answer to the question is yes, I am going to go through with it!"
    show shiori work at center, zoomAt(1.25, (840, 980)) with dissolve
    "When I find Shiori, she's sitting at her desk, flicking through a magazine."
    "She doesn't seem to notice me walk up, and so I cough quietly to get her attention."
    mike.say "Ahem..."
    hide shiori
    show shiori work surprised at center, zoomAt(1.25, (840, 980)), vshake
    "At the sound of my coughing, Shiori literally jumps out of her seat."
    "She also lets out a little yelp of alarm, already trying to hide her magazine."
    show shiori embarrassed
    shiori.say "Ooh...oh dear!"
    shiori.say "[hero.name], this isn't what it looks like!"
    "I'm quick to wave away Shiori's more than evident concern."
    "Sure, I could try to use the fact I caught her skiving off work to blackmail her."
    "But somehow that seems a petty way to go about talking her into what I have in mind."
    mike.say "Don't worry about it, Shiori."
    mike.say "You work hard enough to deserve a break."
    show fx question at right5
    shiori.say "I...I do?"
    mike.say "Sure you do, Shiori."
    mike.say "You're one of the few people around here that I know I can always rely on."
    show shiori normal
    "I feel a little guilty buttering Shiori up like this."
    "But I know that she's needy enough to fall for that kind of line."
    mike.say "In fact, I know that I can come to you when I really need help."
    mike.say "Isn't that right, Shiori?"
    "It's only the merest hint of there being a way to curry favour with me."
    "But all the same, Shiori sits up and pays attention like an eager little puppy."
    show shiori normal
    shiori.say "Do...do you need me to do something, [hero.name]?"
    show shiori happy
    shiori.say "Just say the word and I can do it right away!"
    "A part of me is beginning to feel guilty at just how easy this seems to be."
    "But I push my guilt down, trying to smother it with the thought of that sweet 10K bonus."
    mike.say "Well, Shiori, you know that I've been trying to close this deal with Blissard?"
    show shiori normal
    shiori.say "Oh yes, of course - you've been working so hard recently!"
    mike.say "Well, we're just about to sign the contracts."
    "Shiori nods eagerly."
    mike.say "But there's a slight problem."
    mike.say "One that needs to be sorted before we can do that."
    show shiori annoyed
    shiori.say "Oh no, that's terrible news!"
    mike.say "You see the thing is, Shiori, everyone's really tired."
    mike.say "The negotiations have left us all totally drained."
    mike.say "So I need you to provide some...refreshment for the guys from Blissard."
    "Shiori cocks her head on one side at this."
    show shiori normal
    shiori.say "But, [hero.name], you didn't need to come out here to ask me for that!"
    shiori.say "You could have just called me or sent an email."
    "I shake my head, still trying to look discreet and reasonable."
    "You know - not like a guy about to pimp out one of his female co-workers for his own financial gain?"
    mike.say "Not that kind of refreshment, Shiori."
    mike.say "I mean the kind where everyone gets naked."
    show shiori surprised
    "Shiori's eyes go wide, making her look even more like an innocent little puppy."
    show shiori embarrassed
    shiori.say "Oh...I...I see."
    shiori.say "You want me to have sex with those men, [hero.name]?"
    mike.say "Ah...well...yeah, Shiori."
    mike.say "When you put it like that..."
    "Shiori bites her lip and looks up at me, wringing her hands as she does so."
    if shiori.sub >= 75:
        "Shiori looks at me with those puppy-dog eyes of hers."
        "And if I didn't know her better, I'd think she was on the brink of tears."
        "But I've come to know her very well in the time that she's been working here."
        "And one thing that I know all to well is that Shiori gets off on being told what to do."
        mike.say "Okay, Shiori, okay."
        mike.say "Would it be easier for you if I ordered you to do it?"
        "A sudden thrill seems to pass through Shiori's body at the mere mention of the word."
        "She sits up straighter in her seat, looking at me that much more intently than before."
        show shiori blush
        shiori.say "Oh, b...but, [hero.name]..."
        shiori.say "You wouldn't...would you?"
        shiori.say "Because as my boss, I'd have to obey!"
        "Ah, now we're getting somewhere."
        "Shiori's playing the part of the innocent little office girl."
        "Which means I have to be the domineering boss that gives her no choice in the matter!"
        mike.say "I didn't want to have to do this, Shiori."
        mike.say "But you've left me without a choice."
        mike.say "Get your ass into that meeting room and fuck those guys!"
        show shiori sad at center, zoomAt(1.0, (840, 840)) with ease
        "Shiori gets slowly to her feet, avoiding my eye as she does so."
        "She nods and almost bows as she hurries ahead of me towards the meeting room."
        "And I follow close on her heels, making sure that nobody overheard our conversation."
        "All the time I'm telling myself that I'll be sure to make it up to her."
        "But despite her protests, part of me wonders if Shiori is secretly enjoying this..."
        call foursome_office_shiori from _call_foursome_office_shiori
    elif hero.charm >= 90:
        "Ah, shit - I'm going to regret this, I just know it."
        "But what other choice do I have right now?"
        "I have to hit Shiori where it hurts, where she's most vulnerable."
        "I just hope I can still look at myself in the mirror when this is all over!"
        mike.say "Ah...I didn't want to have to do this, Shiori."
        mike.say "But if you don't, then you're fired."
        hide shiori
        show shiori work surprised at center, zoomAt(1.25, (840, 980)), vshake
        "Shiori all but collapses into a pathetic heap in front of me."
        "She grabs hold of my hands and begins to plead for all she's worth."
        show shiori sad
        shiori.say "Oh, [hero.name], please!"
        shiori.say "You...you can't possibly fire me for that - can you?!?"
        mike.say "No, Shiori."
        mike.say "But I could easily fire your ass for all the other shit."
        mike.say "You know, all the shit that I overlook because I was being good to you?"
        mike.say "All those times you screwed up because your head was somewhere else?"
        "Shiori swallows nervously, and then she looks down at the floor."
        "When she nods her head in a slow, sad manner, I know it's worked."
        show shiori embarrassed
        shiori.say "Y...yes, [hero.name]."
        shiori.say "I understand..."
        show shiori sad at center, zoomAt(1.0, (840, 840)) with ease
        "With her head still hung low, Shiori walks meekly towards the meeting room."
        "And I follow close on her heels, the guilt already building in my gut..."
        $ shiori.flags.blissardbribe = True
        call foursome_office_shiori from _call_foursome_office_shiori_1
    else:
        "Shiori's eyes seem to grow wider still, and I can see tears welling in them too."
        "Suddenly she bursts into a fit of wailing that's the loudest thing in the whole office."
        show shiori sad at center, zoomAt(1.0, (840, 840)) with move
        pause 0.2
        show shiori work sad at right5
        "Before I can even begin to try to sooth her, Shiori's up and backing away from me."
        show shiori annoyed
        shiori.say "I...I'm so sorry, [hero.name]."
        shiori.say "But I can't...I just can't do it!"
        hide shiori with moveoutright
        "With that, Shiori turns her back on me and literally runs out of the office."
        "It's only now that I take the time to look around me."
        "And when I do, I see that everyone has stopped what they're doing to stare at me."
        "Feeling the intense weight of all those eyes on me, I start to walk back to the meeting room."
        "Maybe in the short time it takes me to walk from here to there I'll have thought up a decent excuse."
        "But whatever I can cook up, it's not going to be as painful as the loss of that 10K bonus..."
        $ shiori.sub -= 5
        $ shiori.love -= 5
        $ game.flags.blissardoff = True
    return

label office_harem_pimping_audrey_lavish_shiori:
    scene bg black
    show bg office
    "The whole idea seemed so plain and simple while I was talking about it with Tom, Dick and Harry."
    "But the moment I step out of the room, the reality of the situation fully dawns on me for the first time."
    "I just agreed to talk not one, but three of my female co-workers into fucking three complete strangers!"
    "I shake my head and decide that now is simply not the time to be thinking about the finer details."
    "All I can do is focus on the task at hand and remember why I agreed to this in the first place."
    "I just hope that 10K is actually worth it once it's in the bank!"
    show shiori work at left
    show lavish work
    show audrey work at right
    "Luckily for me, I manage to find Audrey, Lavish and Shiori chatting by the water-cooler."
    mike.say "Ah...hey, girls!"
    mike.say "What's happening with you three?"
    show shiori happy
    "Shiori practically lights up at the sound of my voice, smiling sweetly at me."
    show lavish wink
    "Lavish looks pretty pleased to see me, even if she's not as fawning as Shiori."
    show audrey frown
    "But Audrey eyes me with evident suspicion, looking at me sideways as she does so."
    shiori.say "Oh, good morning, [hero.name]."
    show lavish normal
    lavish.say "We were just chatting while we had a glass of water, that's all."
    lavish.say "We'll be back at work in a couple of minutes, okay?"
    audrey.say "Wait a minute, [hero.name]."
    show fx question at right
    audrey.say "What do you actually want, huh?"
    show shiori surprised
    show lavish surprised
    "Lavish and Shiori look at Audrey, surprised by her questioning me."
    mike.say "I...I don't know what you mean, Audrey!"
    mike.say "I was just passing and thought I'd say hi, that's all."
    show audrey annoyed
    show fx exclamation at right
    audrey.say "Bullshit!"
    audrey.say "You've been working us all to death over this big deal of yours."
    audrey.say "And today's the final meeting, so you should be sweating bullets."
    audrey.say "Instead you're out here being all nicey nicey with the little people!"
    "I look around, worried that someone might be listening in on the conversation."
    "Audrey's blown my cover, so I need to get this over with as quickly as possible."
    mike.say "Okay, okay - you got me."
    mike.say "They're about to sign, but there's a catch."
    show shiori sad
    show lavish sad
    show audrey sad
    "All three of the girls look at me with raised eyebrows."
    "They're obviously wondering what this has to do with them."
    mike.say "The guys from Blissard saw you three when they arrived."
    mike.say "And they were so impressed that they want you to...entertain them."
    show audrey scared
    audrey.say "You HAVE to be joking!"
    show lavish surprised
    lavish.say "Oh no..."
    show shiori embarrassed
    shiori.say "What's so bad about that?"
    shiori.say "Do we have to sing them a song or something?"
    "Lavish leans in to whisper into Shiori's ear."
    "And then her expression changes dramatically."
    show shiori surprised at left, startle
    shiori.say "Oh...oh dear!"
    if (audrey.sub >= 75 and lavish.sub >= 75 and shiori.sub >= 75) or ((audrey.sub >= 75 or lavish.sub >= 75 or shiori.sub >= 75) and hero.charm >= 90):
        if audrey.sub < 75:
            $ audrey.flags.blissardbribe = True
        if shiori.sub < 75:
            $ shiori.flags.blissardbribe = True
        if lavish.sub < 75:
            $ lavish.flags.blissardbribe = True
        show shiori annoyed
        show lavish annoyed
        show audrey annoyed
        "I can see all three of them are exchanging nervous glances."
        "Audrey might have rooted out my true motive quickly enough."
        "But I note that none of them have come out and said no."
        "Maybe if I can get in there and push them in just the right direction..."
        mike.say "You know, I am above your pay grades."
        mike.say "So I could just tell you to do it..."
        show shiori sad
        show fx exclamation at left
        shiori.say "Oh no!"
        show lavish surprised
        show fx exclamation
        lavish.say "You...you wouldn't!"
        show audrey angry
        show fx exclamation at right
        audrey.say "What?!?"
        audrey.say "You can't do that!"
        mike.say "But you wouldn't just be doing it for me."
        mike.say "You'd be doing it for the company too."
        mike.say "And that kind of thing goes a long way."
        mike.say "It's the kind of thing those above you remember."
        mike.say "When there are perks and promotions on offer..."
        "Shiori would probably have done it if I just told her to."
        "So there's no need to worry about having her in the bag."
        "Lavish is less easy to boss about."
        "But I can see that she's scared saying no could ruin her career."
        "Audrey's the one that's going to be the key."
        "If I can win her over, then the others should follow right along."
        audrey.say "So..."
        show audrey frown
        audrey.say "You're saying that you would owe us a favour, right?"
        mike.say "You could say that, Audrey."
        audrey.say "Then I say what the hell -let's do it."
        show lavish normal
        lavish.say "Are you sure this is a good idea, Audrey?"
        show shiori normal
        shiori.say "It sounds a bit scary!"
        show audrey flirt
        audrey.say "Don't worry about it, you guys."
        audrey.say "Just follow my lead and you'll be fine."
        "Lavish and Audrey still look nervous."
        "But they nod their heads meekly in the face of Audrey's confidence."
        "With them in line, she nods to me and I nod in return."
        "Well, here goes nothing."
        "I just hope that 10K is worth it!"
        call sixsome_office_audrey_lavish_shiori from _call_sixsome_office_audrey_lavish_shiori
    else:
        mike.say "Aw, come on, guys!"
        mike.say "Think of it as a show of corporate loyalty, perhaps?"
        mike.say "You'd be doing it for the entire company!"
        "Lavish and Shiori still look shocked at the very idea."
        "But Audrey doesn't hold back for a minute."
        show audrey normal at right
        audrey.say "You mean we'd be doing it for you, [hero.name]."
        audrey.say "Don't think I don't know all about your bonus that's riding on it!"
        "I start trying to explain myself, or at least cook up a decent lie."
        "But I can already see the looks of shock growing on Lavish and Shiori's faces."
        show lavish annoyed
        lavish.say "Really?"
        lavish.say "So that's what this is all about?"
        shiori.say "Oh, [hero.name]..."
        shiori.say "Is that true?"
        audrey.say "I think we'll forget all about this conversation, right?"
        audrey.say "Or else someone might tell HR all about it..."
        hide audrey
        hide lavish
        hide shiori
        with dissolve
        "All three of them turn their backs on me at once."
        "And then they walk away, as I watch my 10K disappear along with them."
        $ game.flags.blissardoff = True
    return

label foursome_office_aletta:
    scene expression f"bg {game.room}"
    "I hold the door open for Aletta, thinking that I'll make this as easy for her as I can."
    show aletta work zorder 4 at left with easeinleft
    "But she simply breezes past me, meaning that I have to hop aside to let her pass."
    "The moment that I close the door behind me, I can hear the reaction of the guys from Blissard."
    show victor as tom zorder 3 at right, blacker, startle
    show ryan tux smile as dick zorder 2 at left4, blacker
    show shawn as harry zorder 1 at right4, blacker
    with dissolve
    "Tom" "Oh well, what do we have here?"
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "You weren't kidding about this one, [hero.name]!"
    show shawn as harry at right4, blacker, startle
    "Harry" "Wow - she can climb my corporate ladder all she wants!"
    show aletta dreamy
    "Aletta makes a sniffing sound at this."
    show aletta annoyed
    "She regards Tom, Dick and Harry over the top of her glasses, studying them intently."
    "And it only takes a couple of seconds for them to start looking distinctly nervous under her gaze."
    show victor as tom at right, blacker, startle
    "Tom" "Ah, what's going on here, [hero.name]?"
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "Yeah, why is she looking at us like that?"
    show shawn as harry at right4, blacker, startle
    "Harry" "I don't know if I like this..."
    "I step forwards a little, smiling at Aletta."
    "All the time I'm feeling as nervous as the guys from Blissard look."
    mike.say "Um...Aletta?"
    mike.say "You remember what we agreed, right?"
    show aletta embarrassed
    "Aletta sniffs for a second time, but nods all the same."
    aletta.say "Of course I do, [hero.name]."
    aletta.say "I was just taking the time to size up the opposition."
    show aletta at center with ease
    "With that, she strides towards the guys from Blissard."
    "Without needing to say anything more, Aletta seems to take control of the situation."
    "She regards Tom, Dick and Harry with the same disdainful look."
    "But now she's beginning to unbutton her blouse at the same time."
    show aletta topless
    aletta.say "Understand one thing, gentlemen."
    aletta.say "What I'm about to do is for the sake of the deal."
    aletta.say "That's all there is to it."
    "Tom, Dick and Harry are all nodding as they watch Aletta strip off her clothes."
    "They seem to be entranced by the force of her personality."
    "And they don't seem to care that she's clearly talking down to them all the while."
    aletta.say "The only reason I'm letting you put your hands on me is to close the deal."
    aletta.say "I want you to remember that the whole time we're doing this."
    aletta.say "Outside of this room, in the real world, this would be impossible."
    aletta.say "In the real world, you maggots are beneath me!"
    show aletta naked
    "All four of them are naked now, the guys approaching Aletta slowly."
    "I watch in fascinated silence as Tom lies down on the floor in front of her."
    "Aletta allows herself to be guided down by the other two."
    "And they steer her straight onto Tom's already stiff cock."
    "Aletta let's out a slight yelp as it presses against the lips of her pussy."
    if renpy.has_label("office_harem_achievement_4") and not game.flags.cheat:
        call office_harem_achievement_4 from _call_office_harem_achievement_4
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show expression "office aletta foursome " + game.room
    with dissolve
    "Then she stifles it as gravity takes care of the rest."
    "For a moment I think she's going to close her eyes as she sinks down onto it."
    "But she proves me wrong by looking up and catching my eye."
    "Aletta holds my gaze the whole time that she's letting Tom enter her."
    "And she's still doing so when Dick eagerly begins to push his cock into her ass."
    "Not even Harry roughly shoving his member into her face can make her look away."
    "Instead, Aletta keeps right on looking at me as she parts her lips and begins to suck it."
    "I swallow loudly as all three of them start to indulge themselves."
    "Pretty soon Aletta is being pushed and pulled in three directions at once."
    "None of the guys from Blissard can see the expression on her face."
    "They're all much too busy sticking their cocks into her to even notice."
    "But I can see that the previously superior and aloof Aletta has vanished."
    show office aletta foursome ahegao
    "Now her eyes are wide and her cheeks have flushed a deep shade of red."
    "Anyone else might think that's all just on account of what she's being put through."
    "But I know Aletta well enough to be aware of the truth."
    "There's a part of her that she normally keeps well hidden."
    "The part of her that secretly longs to be humiliated in just such a manner."
    "And it's not just that she's getting used by three guys at once."
    "I can see that a lot of the thrill she's getting out of this is thanks to my being here."
    "Aletta might actually be most turned on by being humiliated in front of me!"
    "I can't make myself look away either, feeling compelled to watch."
    "Tom, Dick and Harry aren't holding back or being gentle either."
    "Aletta has a cock in every hole, and they're all going at her hard."
    "Their bodies move so that she's being thrust into from three directions at once."
    "And as if that wasn't enough, their hands and mouths are everywhere too!"
    "Pretty soon Aletta's skin is slick with sweat and their saliva."
    with hpunch
    "The situation only becoming worse as they come one after the other."
    show office aletta foursome cum with hpunch
    "None of them have a moment's care for where they shoot their respective loads."
    with hpunch
    "This means that Aletta's pussy, ass and mouth are all dripping with cum."
    "Once it's over, they let Aletta fall to the floor, panting and spent."
    scene expression f"bg {game.room}"
    with fade
    "Tom" "Ah...phew..."
    "Tom" "A deal's a deal, right?"
    "Before any of them have even put their clothes back on, they walk to the table."
    "One after another they sign the papers, just as we agreed."
    "All the time my gaze flits between the guys from Blissard and Aletta."
    "They're all smiles and winks as they pull on their clothes."
    show aletta b naked embarrassed blush at center, zoomAt(1.0, (640, 940)) with dissolve
    "But she's still sitting on the floor as she fumbles for her own clothing."
    "I force a smile onto my face, trying to hide the mixed emotions in my gut."
    "Sure, I got what I wanted."
    "But was it worth the cost to Aletta?"
    $ aletta.sub += 2
    return

label foursome_office_audrey:
    scene expression f"bg {game.room}"
    "Audrey practically strides into the room as I hold the door open for her."
    show audrey work zorder 4 at left with easeinleft
    "She regards Tom, Dick and Harry with an almost disdainful look as she stands before them."
    show victor as tom zorder 3 at right, blacker, startle
    show ryan tux smile as dick zorder 2 at left4, blacker
    show shawn as harry zorder 1 at right4, blacker
    with dissolve
    "Which of course only serves to make them all the more eager to get down to business."
    "I hastily close the door behind us, praying that nobody walks in before we get this over with."
    show victor as tom at right, blacker, startle
    "Tom" "Whoa, Dick!"
    "Tom" "We should listen to you more often!"
    show shawn as harry at right4, blacker, startle
    "Harry" "I'll say - she's hot as hell!"
    "Dick takes the chance to bask in the reflected glory of being the one to eye up Audrey."
    "But Audrey herself seems less than impressed with the revealing of her admirer."
    show audrey joke
    audrey.say "You think he's that great, huh?"
    audrey.say "Then why don't you fuck him instead of me?"
    "I'm pretty sure Audrey meant that to sting the guys from Blissard."
    "But all it does is get them even more excited at what lies ahead."
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "You guys see what I mean?"
    "Dick" "I knew this little whore was filthy the moment I laid eyes on her!"
    show audrey annoyed
    "At the mention of the word 'whore', I see irritation flare in Audrey's eyes."
    "She rounds on me the next instant, hands clenched into fists at her sides."
    show audrey angry
    audrey.say "What's that supposed to mean, [hero.name]?"
    audrey.say "Did you tell them you were going to pay me to do this?!?"
    mike.say "No, Audrey!"
    mike.say "I swear I didn't say a word about that!"
    "I'm about to say more when Tom walks between Audrey and myself."
    "He gives her what can only be described as a shit-eating grin."
    "And I can tell that he's loving every moment of this."
    show victor as tom at right, blacker, startle
    "Tom" "He's telling the truth, Audrey."
    "Tom" "But knowing you're doing this for the money..."
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "That makes it all the more sweet for us!"
    show shawn as harry at right4, blacker, startle
    "Harry" "Yeah - it means we know you've been bought and sold!"
    show victor as tom at right, blacker, startle
    "Tom" "So what's it going to be?"
    "Tom" "Do you want your cut or not?"
    "Audrey shoots me one last, venomous look."
    "And then I see her force a change onto her face."
    show audrey flirt
    "Her frown transforms into a dirty, knowing grin."
    "She turns her gaze to Tim as she begins to strip off her clothes."
    show audrey topless
    audrey.say "Oh, don't worry - we'll get it on."
    audrey.say "After all, haven't I already been paid for?"
    show audrey naked
    "Tom, Dick and Harry nod eagerly as they follow Audrey's lead."
    "In no more than a minute, all of them are naked and ready to get it on."
    "Tom sits himself down and beckons Audrey towards him."
    "She does as she's told without question."
    "All the time being sure to eye his already stiff cock as she does so."
    "Even before she's down low enough to get it in her mouth, the others make their own moves too."
    "Dick thrusts his cock against Audrey's pussy, shoving her onto Tom's."
    "And almost as soon as he's inside of her, Harry plunges his own member into her ass too."
    if renpy.has_label("office_harem_achievement_4") and not game.flags.cheat:
        call office_harem_achievement_4 from _call_office_harem_achievement_4_1
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show expression "office audrey foursome " + game.room
    with dissolve
    "Audrey might have walked in here with the idea she was taking the initiative."
    "But now she has three cocks thrust into three hole all at once."
    "There's nothing she can do but go along with what's happening to her."
    "Tom, Dick and Harry don't waste any time either."
    "As soon as they're inside of Audrey, they begin to thrust and pump away without mercy."
    "All I can do is watch things unfold with a kind of horrified fascination."
    "I'm used to seeing Audrey as the sarcastic, cutting girl around the office."
    show office audrey foursome ahegao
    "But it doesn't take long for her to be reduced to a gasping mess."
    "Tom, Dick and Harry seem to be having a great time."
    "Though I can't be sure the same can be said for Audrey."
    "To me it looks like she's being used simply for their gratification."
    "But I have money riding on this, so I keep my mouth shut the whole time."
    "Surely the easiest thing would be for me to look away until it's all over."
    "And yet I can't do it, as Audrey looks up at me and catches my eye."
    "I don't know if she's doing so to make me feel guilty."
    "Or if she genuinely thinks that I might do something to interfere."
    "But either way, I just keep on holding her eye the whole way through."
    with hpunch
    "Tom is the first to shoot his load, letting it go straight in Audrey's face."
    show office audrey foursome cum with vpunch
    "As if following his lead, Dick and Harry cum moments later."
    "They seem to lose interest in Audrey the very second it's over."
    scene expression f"bg {game.room}"
    with fade
    "And she's left to pant and gasp on the floor as they pat each other on the back."
    "Tom" "Ah...phew..."
    "Tom" "A deal's a deal, right?"
    "Before any of them have even put their clothes back on, they walk to the table."
    "One after another they sign the papers, just as we agreed."
    "All the time my gaze flits between the guys from Blissard and Audrey."
    "They're all smiles and winks as they pull on their clothes."
    show audrey b naked happy blush facecum at center, zoomAt(1.0, (640, 940)) with dissolve
    "But she's still sitting on the floor as she fumbles for her own clothing."
    "I force a smile onto my face, trying to hide the mixed emotions in my gut."
    "Sure, I got what I wanted."
    "But was a grand worth what Audrey just went through?"
    $ audrey.sub += 2
    return

label foursome_office_lavish:
    scene expression f"bg {game.room}"
    "I keep my eyes on Lavish as I open the door and let her into the meeting room."
    show lavish work zorder 4 at left with easeinleft
    "She does the best she can to appear confident and relaxed as I close it behind me again."
    "But it's not hard to see that she's actually more than a little scared right now."
    "And while that doesn't really help me, I can't help sympathising with Lavish."
    show victor as tom zorder 3 at right, blacker
    show ryan tux smile as dick zorder 2 at left4, blacker
    show shawn as harry zorder 1 at right4, blacker
    with dissolve
    "Especially when I glance over and see Tom, Dick and Harry leering at her."
    "Lavish gives them a smile and even tries to wave a friendly hello."
    "But they're already looking at her like wolves eyeing up a lost lamb."
    show victor as tom at right, blacker, startle
    "Tom" "Wow, Harry!"
    "Tom" "I should listen to you more often!"
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "Yeah, man - she's something else!"
    show shawn as harry at right4, blacker, startle
    "Harry" "What did I tell you guys?!?"
    "Harry" "She's sexy as hell!"
    "I force a smile onto my face, trying to look like this is going well."
    "But the truth is I'm already feeling bad for Lavish as they salivate over her."
    "I guess it's too late to back out of this thing now..."
    "For her own part, Lavish looks like she's got the smile stapled onto her face."
    "She seems as committed to this as I am, keen to earn the promotion I've promised her."
    show lavish normal blush
    lavish.say "Aww..."
    lavish.say "It...it's so kind of you to say so!"
    "This elicits a round of laughter from Tom, Dick and Harry."
    "By now they're already pulling off their ties and unbuttoning their shirts."
    show victor as tom at right, blacker, startle
    "Tom" "Oh, we can be kind."
    "Tom" "But maybe that's not what you really want?"
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "Yeah, little lady - maybe you want us to be bad?"
    show shawn as harry at right4, blacker, startle
    "Harry" "Oh man - please say you want us to be bad!"
    show lavish happy
    "Lavish laughs again, putting on a brave face."
    "But this time I really can hear the nerves that are gripping her."
    "She looks at me over her shoulder, as if appealing for help."
    "And all I do is give her an encouraging nod and a weak smile of my own."
    "Lavish nods in response and begins to walk over to the guys from Blissard."
    show lavish topless
    "She goes slowly, stripping off her clothes at much the same pace."
    "This draws out the time it takes her to reach them."
    show lavish naked
    "But it also means they spend that much longer lusting over her as she approaches!"
    "Tom sits down, gesturing for Lavish to turn her back to him."
    "And then he guides her down into his lap, making her sit on his cock."
    "Lavish yelps and bites her lip as she feels it pressing between her buttocks."
    "But Dick soon puts an end to that as he thrusts his own cock into her mouth."
    "I see Lavish's eyes go wide with shock as she struggles to open wide enough."
    "In fact, she's so distracted that Harry takes her by complete surprise a moment later."
    "That's when he steps up and plunges his member into Lavish's pussy."
    if renpy.has_label("office_harem_achievement_4") and not game.flags.cheat:
        call office_harem_achievement_4 from _call_office_harem_achievement_4_2
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show expression "office lavish foursome " + game.room
    with dissolve
    "All I can see in her eyes is confusion as they get down to it."
    "So I can only guess how much resistance Lavish's body puts up."
    "Whatever urge there was in her to fight, she can't keep it up forever though."
    "And soon enough, each of the cocks sinks ever deeper into her body."
    "It's a position that I never imagined I'd see Lavish in."
    "Sure, I've spent more than a little time picturing her in compromising positions."
    "Who wouldn't, as she's a stunning girl."
    "But Tom, Dick and Harry are treating her body like an amusement park!"
    "Lavish's legs are hauled up into the air and she bobs on Tom's lap."
    "I'm not even sure that she knows where she is or what's happening anymore!"
    "But at least that's a small mercy for me."
    show office lavish foursome ahegao
    "Lavish looks so confused that she can't hope to cast her gaze my way."
    "If she did, then she couldn't fail to see the growing expression of guilt I'm wearing."
    "I was only half-serious when I promised to make sure that she got some kind of reward."
    "But that was then, and now I'm thinking that I'm going to have to make good on it."
    "Otherwise I've just allowed her to be exploited for nothing other than my own gain!"
    "All too soon I see the guys from Blissard start to cum."
    with hpunch
    "Tom goes first, like the other two need his permission before they shoot their own loads."
    show office lavish foursome cum with vpunch
    "He doesn't hesitate to fill Lavish's ass, the cum seeping out around his cock."
    with hpunch
    "Dick goes next, and soon enough her lips are dribbling cum as well."
    "Harry finishes off last of all, thrusting in and out of Lavish's pussy the whole time."
    scene expression f"bg {game.room}"
    with fade
    "Now they've had their way with her, they let Lavish slide onto the floor."
    "And for the moment, she lies there, panting and utterly exhausted."
    "Tom" "Ah...phew..."
    "Tom" "A deal's a deal, right?"
    "Before any of them have even put their clothes back on, they walk to the table."
    "One after another they sign the papers, just as we agreed."
    "All the time my gaze flits between the guys from Blissard and Lavish."
    "They're all smiles and winks as they pull on their clothes."
    show lavish b naked embarrassed blush at center, zoomAt(1.0, (640, 940)) with dissolve
    "But she's still sitting on the floor as she fumbles for her own clothing."
    "I force a smile onto my face, trying to hide the mixed emotions in my gut."
    "Sure, I got what I wanted."
    "But how am I ever going to be able to pay Lavish back for what she's been through?"
    $ lavish.sub += 2
    return

label foursome_office_shiori:
    scene expression f"bg {game.room}"
    "I have to all but lead Shiori in through the door of the meeting room, holding her hand the entire time."
    show shiori work zorder 4 at left with easeinleft
    "She actually clings onto me the whole time, looking for all the world like a deer caught in the headlights of a car."
    show victor as tom zorder 3 at right, blacker
    show ryan tux smile as dick zorder 2 at left4, blacker
    show shawn as harry zorder 1 at right4, blacker
    with dissolve
    "Tom, Dick and Harry don't exactly help matters either, leering and laughing the moment that they lay eyes on her."
    "And I can actually feel Shiori begin to quake a little as she presses herself against me."
    show victor as tom at right, blacker, startle
    "Tom" "What did I tell you guys?"
    "Tom" "This is the one we wanted!"
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "Whoa - will you look at the size of those tits!"
    show shawn as harry at right4, blacker, startle
    "Harry" "And the ass that goes with them too!"
    "I walk a little further into the room, steering Shiori towards the guys from Blissard."
    "She resists at first, looking up at me with pleading eyes."
    "But then she seems to realise that I'm not going to relent."
    show shiori embarrassed
    shiori.say "D...do I really have to do this, [hero.name]?"
    shiori.say "Isn't there some other way?"
    "The pleading tone of Shiori's voice only serves to make Tom, Dick and Harry that much more keen."
    "And they come to meet me halfway, already pulling at their ties and unbuttoning their shirts."
    show victor as tom at right, blacker, startle
    "Tom" "Don't worry, [hero.name]."
    show ryan tux smile as dick at left4, blacker, startle
    "Dick" "Yeah, we'll take good care of her."
    show shawn as harry at right4, blacker, startle
    "Harry" "You'll get her back in one piece!"
    "I take a deliberate step backwards while pushing Shiori out in front of me."
    "She gives me one last look over her shoulder."
    "But then she seems to realise that I'm not going to change my mind."
    mike.say "Just be gentle with her, okay?"
    "Tom, Dick and Harry all nod at this."
    "But their smiles betray their amusement at me even asking such a thing."
    if shiori.flags.blissardbribe:
        "After all, I've just agreed to basically blackmail Shiori into having sex with them."
        "So it's a little late for me to begin pleading with these guys to be nice to her too!"
    show shiori topless
    "Shiori begins to strip off her clothes, but her efforts are too slow."
    "The guys from Blissard soon take charge of undressing her."
    "And there's nothing Shiori can do but endure their hands being all over her."
    show shiori naked
    "Tom guides Shiori over to the seats at the edge of the room."
    "And once there he pushes her down, not gently and yet not with enough force to be called a shove."
    "Shiori falls on her belly, eyes wide as she looks back over her shoulder at him."
    "I can see the look of enjoyment in Tom's eyes as he lifts one of her legs."
    "And it only becomes more pronounced as her begins to push his cock against Shiori's pussy."
    "She whimpers at the sensation, but only until Dick turns her head to face him."
    "The moment he does so, Shiori's presented with the sight of his own cock."
    "And when he thrusts it between her open lips, her eyes go as wide as saucers."
    "As the two of them begin to work her from both ends, Shiori has no choice but to surrender."
    "Even when Harry guides one of her hands to his cock and makes her start to stroke it."
    "Rather than flinching away, Shiori instead takes hold of the shaft without protest."
    if renpy.has_label("office_harem_achievement_4") and not game.flags.cheat:
        call office_harem_achievement_4 from _call_office_harem_achievement_4_3
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show expression "office shiori foursome " + game.room
    with dissolve
    "I should be relieved that she's doing as she's told."
    "After all, it means that I'm on course to seal the deal and get my bonus."
    "But it feels like it was a lot easier to dream this thing up than to actually watch it happening."
    "Of course, Tom, Dick and Harry are having a hell of a time as they indulge themselves."
    "But it's the way that Shiori just seems to be accepting it all that really gets to me."
    show office shiori foursome ahegao
    "Maybe I could have dealt with the things that they're making her do."
    "After all, that's just sex, the kind of thing that happens all the time in the bedroom."
    "No, it's the way that Shiori's being used that's really getting to me."
    "I know that she's not had the most pleasant time of it in her personal life."
    "And she's come out of it behaving pretty much like a human doormat."
    "Now I've added to that for the sake of lining my own pockets!"
    "Pretty soon I can see the first signs that Tom's about to cum."
    with hpunch
    "He groans as he shoots his load into Shiori, and the others seem to follow his lead."
    show office shiori foursome cum with hpunch
    "A second later, Dick fills Shiori's already stuffed mouth."
    with hpunch
    "And then Harry's cock spurts in her hand, his cum running over her fingers."
    scene expression f"bg {game.room}"
    with fade
    "Once it's over, they leave Shiori gasping on the seat."
    "Tom" "Ah...phew..."
    "Tom" "A deal's a deal, right?"
    "Before any of them have even put their clothes back on, they walk to the table."
    "One after another they sign the papers, just as we agreed."
    "All the time my gaze flits between the guys from Blissard and Shiori."
    "They're all smiles and winks as they pull on their clothes."
    show shiori b naked embarrassed blush cumface at center, zoomAt(1.0, (640, 940)) with dissolve
    "But she's almost gasping as she fumbles for her own clothing."
    "I force a smile onto my face, trying to hide the mixed emotions in my gut."
    "Sure, I got what I wanted."
    "But was it worth the cost to Shiori?"
    $ shiori.sub += 2
    return

label sixsome_office_audrey_lavish_shiori:
    scene expression f"bg {game.room}"
    "I open the door to the meeting room so that Audrey, Lavish and Shiori can troop in before me."
    show audrey work zorder 4 at left4
    show lavish work zorder 2 at left
    show shiori work zorder 3 at top_mostleft
    with easeinleft
    "And even before I can follow them and close it behind me, I can hear the reaction they receive."
    show victor as tom zorder 3 at top_mostright, blacker
    show ryan tux smile as dick zorder 2 at right4, blacker
    show shawn as harry zorder 1 at right, blacker
    with dissolve
    "The guys from Blissard are laughing and even clapping their hands together at the sight of them."
    "I try to smile and look just as upbeat as I walk over to where everyone's standing."
    "But there's still a part of me that feels more like a pimp than a guy about to close a deal!"
    show shawn as harry at right, blacker, startle
    "Harry" "Wow...just, wow!"
    "Harry" "You really came through on this one!"
    show ryan tux smile as dick at right4, blacker, startle
    "Dick" "I'll say he did."
    "Dick" "They're even better than I remember!"
    "Tom" "Our companies should work together more often, [hero.name]."
    "Tom" "This could be the start of a very productive relationship!"
    "Shiori and Lavish look like a pair of deer in the headlights of a car right now."
    "But I can see that Audrey's already prickling at the way she's being stared at."
    show audrey at center with ease
    "Luckily for me, she steps forward and takes the lead a moment later..."
    show audrey annoyed
    audrey.say "So these are the bunch of limp-dicks you told us about, huh?"
    audrey.say "The ones you need us to take care of?"
    mike.say "Ah, yeah, Audrey - that's right."
    mike.say "So if you girls wouldn't mind..."
    "Audrey rolls her eyes at my imploring her."
    "And then she looks at Shiori and Lavish with her hands on her hips."
    audrey.say "Come on, you two."
    audrey.say "Let's get this over with."
    audrey.say "I bet these guys will shoot their loads in a minute anyway!"
    "Shiori and Lavish nod, but they still look nervous as hell."
    "And if anything, Tom, Dick and Harry seem amused at Audrey's opinion of them."
    "The guys from Blissard begin to undo their ties and unbutton their shirts."
    show audrey topless
    show lavish topless
    show shiori topless
    "But the girls are a lot less enthusiastic to start stripping off their clothes."
    "This means that the guys are naked when they come to claim their prizes."
    "Harry takes Lavish by the hand, guiding her to suck his cock as he sits down."
    "Dick wastes no time in pushing Audrey onto the floor and finding her pussy."
    "But when Tom reaches out to take Shiori by the hand, she pulls back from him."
    "Tom" "Hey there, don't be scared of me!"
    "Tom" "Just let go and think pleasant thoughts."
    "Tom" "Do that and you might actually enjoy it!"
    "With more than a little reluctance, Shiori is lead over to the seats."
    "Once there, Tom sits down and guides her onto his lap."
    "Shiori has no choice but to straddle his thighs and lower herself onto his cock."
    if renpy.has_label("office_harem_achievement_4") and not game.flags.cheat:
        call office_harem_achievement_4 from _call_office_harem_achievement_4_4
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show expression "office sixsome " + game.room
    with dissolve
    "I almost have to blink to be able to believe what I'm seeing."
    "All it's taken is the space of less than half an hour."
    "And in that time, Audrey, Lavish and Shiori have gone from working in the office to this!"
    "It hardly seems to matter that they were less than keen to do it either."
    "As the guys from Blissard are more than making up for their lack of enthusiasm."
    show office sixsome lavishahegao
    "Harry is getting his cock sucked with increasing fervour by Lavish."
    show office sixsome audreyahegao
    "Dick is living up to his name as he pounds away mercilessly at Audrey's pussy."
    show office sixsome shioriahegao
    "And Tom can't help smiling at me over his shoulder as he has his way with Shiori."
    "I can't help thinking it's an ironic way for all of this to end."
    "I mean, I must have sunk almost all of my energy into making this deal happen."
    "But at the very last, it took all the energy that the girls had to actually get it done!"
    "I try to force a smile onto my face, telling myself that it's all going to plan."
    "Yet the more I have to stand here and listen to the sounds around me, the harder it gets."
    "I might walk away from this with the bonus that I was so keen to earn."
    "But will I ever be able to look Audrey, Lavish and Shiori in the eye again?"
    "Will I always be the guy that pimped them to seal a deal?"
    "The sound of Tom groaning as he cums is enough to snap me out of it."
    show office sixsome shioricum with vpunch
    "Shiori moans and whimpers as he shoots his load into her."
    "And then, as if they had to wait for permission, the others follow his lead."
    show office sixsome audreycum with hpunch
    "Dick loses himself inside of Audrey, who almost claws at the carpet the whole time."
    show office sixsome lavishcum with vpunch
    "Then Harry spatters Lavish's cheeks and nose with cum too."
    scene expression f"bg {game.room}"
    with fade
    "Once it's over, they leave the girls on the other side of the room, panting and spent."
    "Tom" "Ah...phew..."
    "Tom" "A deal's a deal, right?"
    "Before any of them have even put their clothes back on, they walk to the table."
    "One after another they sign the papers, just as we agreed."
    "All the time my gaze flits between the guys from Blissard and my female co-workers."
    "They're all smiles and winks as they pull on their clothes."
    show shiori b naked embarrassed blush zorder 2 at center, zoomAt(1.0, (840, 940))
    show lavish b naked embarrassed blush zorder 1 at center, zoomAt(1.0, (640, 940))
    show audrey b naked happy blush zorder 3 at center, zoomAt(1.0, (440, 940))
    with dissolve
    "But Audrey, Lavish and Shiori are all silent as they pull on their own clothing."
    "I force a smile onto my face, trying to hide the mixed emotions in my gut."
    "Sure, I got what I wanted."
    "But was it worth the cost to those three?"
    $ audrey.sub += 2
    $ lavish.sub += 2
    $ shiori.sub += 2
    return

label office_harem_pimping_afterwards:
    scene expression f"bg {game.room}"
    with fade
    "Once the ink is dry on the contracts and everyone's fully dressed, things feel almost normal again."
    show victor as tom zorder 3 at right5, blacker
    show ryan tux smile as dick zorder 2 at left5, blacker
    show shawn as harry zorder 1 at center, blacker
    with dissolve
    "Tom, Dick and Harry wait until it's just the four of us before they actually start talking."
    "It feels a little odd, but I guess that they don't want to discuss business in front of anyone else."
    "Tom wastes no time in walking over and slapping me pretty hard on the back."
    "I'm not expecting it, and so I can't help staggering forwards a little way."
    "But I manage to smile all the same, trying my best to look as pleased as the guys from Blissard."
    show victor as tom at right5, blacker, startle
    "Tom" "There you go, [hero.name] - it's a done deal!"
    "Tom" "And it's all thanks to you."
    mike.say "Well, I don't know about that..."
    show ryan tux smile as dick at left5, blacker, startle
    "Dick" "Ah, cut the false modesty, [hero.name]."
    "Dick" "We know this was your baby from day one!"
    mike.say "Ah, if you say so..."
    show shawn as harry at center, blacker, startle
    "Harry" "Of course we do, [hero.name]."
    "Harry" "This thing would have been dead in the water if not for you!"
    "It's only now that they're getting ready to leave that their words actually start to sink in."
    "I guess that they're right - I was the one that did all of the work on our side of the deal."
    "Maybe I shouldn't be so shy about taking pride in what I just pulled off?"
    show victor as tom at right5, blacker, startle
    "Tom" "Not many guys would have the balls to do what you did."
    "Tom" "You know, what with the way society's getting so woke?"
    show ryan tux smile as dick at left5, blacker, startle
    "Dick" "But you didn't let that stop you, eh?"
    show shawn as harry at center, blacker, startle
    "Harry" "And we respect that in a man!"
    "It's right about now that my guilt chooses to surface."
    "The moment that I realise they're not really praising my negotiating skills at all."
    "What they're actually impressed by was the fact I agreed to let them indulge themselves just now."
    "That I was prepared to offer them a chance to fuck my female co-workers in order to seal the deal!"
    "All I can do is nod and smile, hoping that they'll hurry up and get the hell out of here."
    "Sure I have the promise of that large bonus dropping into my bank account pretty soon."
    "But I also have to walk out of this room and face the rest of the office."
    "By now, everyone must know what went down in here."
    "This place practically runs on gossip, there's no keeping a secret!"
    mike.say "Ha..."
    mike.say "Yeah, that's me!"
    mike.say "Whatever it takes to get the job done!"
    hide victor
    hide ryan
    hide shawn
    with easeoutleft
    "Tom, Dick and Harry file out of the meeting room."
    "Which leaves me with only my feelings of guilt for company."
    "I can't stay in here forever."
    "But I'm sure I'll pluck up the courage to leave sooner, rather than later..."
    $ game.flags.blissardsealed = True
    if shiori.flags.blissardbribe:
        $ shiori.love -= 50
    if aletta.flags.blissardbribe:
        $ aletta.love -= 50
    if lavish.flags.blissardbribe:
        $ lavish.love -= 50
    if audrey.flags.blissardbribe:
        $ hero.money += 5000
    else:
        $ hero.money += 10000
    return

label office_audrey_shiori_showdown:
    "I've gotten to be able to rely upon Shiori walking through the door every morning with my coffee."
    "Seriously, the girl is more accurate than a Swiss watch when it comes to keeping the time!"
    "And most days, I'm so buried in my work that I need the coffee like fuel to keep me going."
    "Usually I hardly look up to acknowledge that Shiori's even walked into the room to drop it off."
    "But I do confess to sneaking an appreciative look at the way her ass moves on the way out again!"
    "So this morning, when the door opens around the time I'm expecting my coffee, I do look up."
    "And that's because it can't be Shiori, as whoever just walked into my office didn't bother to knock."
    "That's one thing that Shiori always does - knocks and asks my permission to enter."
    show audrey work at left with moveinleft
    audrey.say "Good morning, [hero.name]..."
    "I was almost sure of who it was, even before I heard the sound of her voice."
    mike.say "Hello, Audrey."
    mike.say "To what do I owe the pleasure of your presence?"
    show audrey happy
    "Audrey smiles, obviously picking up on the slight tone of irritation in my own voice."
    show audrey at center with move
    "She lets the door close behind her, kicking it with her heel before walking towards my desk."
    audrey.say "Oh, don't be like that, [hero.name]!"
    audrey.say "There's a million innocent reasons I might need to be here."
    show audrey joke
    audrey.say "And probably some not so innocent ones too!"
    show audrey a at center, zoomAt(1.5, (740, 1040)) with fade
    "By now, Audrey's sauntered over to my desk and walked around the side."
    "I lean back in my chair, crossing my arms over my chest as she gets closer."
    "I'm trying hard to keep the look on my face cynical and unimpressed."
    show audrey a at center, zoomAt(1.75, (940, 1190)) with fade
    "But the closer she gets, the harder it becomes to pull it off."
    mike.say "Ahem..."
    mike.say "This IS an office, Audrey."
    mike.say "Did you need to see me about anything work-related at all?"
    "Audrey nods as she perches herself on the edge of the desk."
    show audrey a at center, zoomAt(2.0, (840, 1340)) with fade
    "And then she leans in closer, until her eyes are level with mine."
    show audrey a flirt
    audrey.say "Sure it's work-related, [hero.name]."
    audrey.say "All I have on my mind is your stress levels."
    audrey.say "Stress and how it's affecting your productivity."
    mike.say "How so, Audrey?"
    show audrey a normal
    audrey.say "Well..."
    audrey.say "You do drink a lot of coffee."
    audrey.say "And that's not helping matters."
    audrey.say "I was thinking of showing you another way to relieve stress..."
    "It's right about now that I feel Audrey's hand on my groin."
    "She must had slipped it down there while she was looking me in the eye!"
    "My eyes go wide and I gasp in surprise as much from the sensation."
    "Audrey doesn't hesitate to squeeze harder, massaging my cock through my pants."
    "And it's not like I can keep myself from getting hard as she does so."
    show audrey a flirt
    audrey.say "See - I knew you'd like my idea."
    audrey.say "It's caffeine-free, and it's fun for the both of us too!"
    "A moment later, Audrey has my flies open and my cock in her hand."
    "Part of me thinks that I should be putting a stop to what she's doing."
    "But a larger part of me is almost panting at the prospect of letting her continue."
    audrey.say "That's right, [hero.name]."
    audrey.say "Just put yourself in my hands..."
    "Just then there's the sound of someone knocking at the door."
    "My head jerks up, but Audrey doesn't seem concerned in the slightest."
    shiori.say "Coffee time, [hero.name]."
    shiori.say "Hot and creamy - just the way you like it!"
    mike.say "Shiori..."
    mike.say "Wait..."
    show shiori work happy at left with easeinleft
    "At the sound of my voice, Shiori opens the door and walks straight in."
    "She must be so used to me giving her permission to enter that she's on auto-pilot!"
    shiori.say "Here you go, [hero.name]."
    shiori.say "This should keep your pecker up..."
    show shiori surprised at left, startle
    "Luckily for me, Shiori covers her mouth with her hands before she cries out."
    "This means that the only sound is the tray hitting the floor as she drops it."
    mike.say "Shiori..."
    mike.say "Oh my god..."
    mike.say "This isn't what it looks like!"
    "What in the hell am I saying?"
    "Shiori would have to be an idiot to believe that!"
    "This is exactly what it looks like - me letting Audrey jerk me off in my office!"
    show audrey joke
    audrey.say "Oh, Shiori - I'm so sorry."
    audrey.say "I had NO idea you were going to walk in on us!"
    "Audrey's voice sounds sincere, but I have my doubts the moment she speaks."
    "I notice that she didn't let go of me or jump away when Shiori walked in just now."
    "In fact, she only just let go of my cock as she started talking."
    "And then there's the matter of her not knowing we'd be disturbed."
    "Plus she said she's been watching my coffee habit."
    "Which means she must have been watching Shiori's routine too."
    "How could she not have known Shiori would be bringing me coffee right about now?"
    "Also, I note she said she was sorry for Shiori seeing what we were doing."
    "Not that she was sorry to have been doing it in the first place."
    "But I can't confront Audrey with my suspicions right now."
    "As I have to deal with some rather more pressing matters."
    show shiori sad
    "Firstly that Shiori's about to burst into tears."
    "And secondly that I'm sitting here with my cock out."
    hide audrey
    hide shiori
    show audrey work at right5
    show shiori work sad at left5
    with fade
    "Stuffing it back into my pants, I get up and try to comfort Shiori."
    mike.say "Shit, Shiori..."
    mike.say "I didn't want you to find out about Audrey and me like this!"
    mike.say "I'm sorry - I should have told you sooner."
    "Shiori gazes at me with huge, red-rimmed eyes."
    shiori.say "I...I thought we were..."
    shiori.say "I thought I was..."
    show audrey normal
    "But Audrey makes a sudden gasping sound."
    audrey.say "Wow...are you two..."
    audrey.say "Oh my god - I didn't know you had a thing going on!"
    audrey.say "This must be SO awkward for the two of you!"
    "I feel like picking up a heavy object and throwing it in Audrey's general direction."
    "But when she speaks again, I can hear that the tone of her voice has changed subtly."
    "Now, rather than insincerely apologetic, she's beginning to sound sly."
    show audrey flirt
    audrey.say "You know, there's no reason we have to get all dramatic about this."
    audrey.say "We're all adults, after all."
    audrey.say "And this IS the twenty-first century..."
    show shiori embarrassed
    shiori.say "Wh...what are you saying, Audrey?"
    mike.say "Yeah, Audrey - what are you getting at?"
    show audrey happy
    "Audrey smiles as she slinks over to where Shiori and I are standing."
    hide audrey
    hide shiori
    show audrey work at center, zoomAt(1.75, (940, 1190))
    show shiori work surprised at center, zoomAt(1.75, (340, 1190))
    with fade
    "She wraps one arms around my waist and the other around Shiori's."
    show audrey work at center, zoomAt(1.75, (840, 1190))
    show shiori work at center, zoomAt(1.75, (440, 1190))
    with move
    with hpunch
    "And then she pulls us all into a three-way embrace."
    show audrey flirt
    audrey.say "What I'm saying is that we can make this work for all of us."
    audrey.say "Shiori, we both like [hero.name]."
    audrey.say "[hero.name] - I know you like both of us too."
    audrey.say "And well..."
    audrey.say "I'm not immune to your charms either, Shiori..."
    "Audrey lets the statement hang in the air as she gives Shiori a languid smile."
    "And even someone as naive and pure as Shiori can't help but catch her meaning."
    show shiori annoyed blush
    "Shiori's cheeks flush red with an alarming speed, and she can't meet Audrey's eye."
    shiori.say "I...I could never..."
    shiori.say "Not...not unless..."
    show shiori normal blush
    shiori.say "Unless it was what you wanted, [hero.name]?"
    if all([person.love >= 140 and person.sub >= 25 for person in [audrey, shiori]]):
        "I'm suddenly reminded of just how submissive and obedient Shiori actually is."
        "I bet if I were to suggest it..."
        mike.say "Actually, Shiori..."
        mike.say "I think Audrey's idea is perfect."
        mike.say "It'd mean we all get what we want and nobody's left out."
        show shiori surprised
        "Shiori's eyes are wider than I've ever seen them by now."
        "And I'm pretty sure she's actually trembling with trepidation."
        show shiori embarrassed
        "But all the same, she nods dutifully."
        "And then she bows her head, showing that she accepts my decision."
        show shiori normal blush
        shiori.say "Y...yes, [hero.name]."
        shiori.say "I'll do as you wish."
        "Audrey nudges Shiori in the ribs."
        show audrey joke
        "And she has a wicked look on her face as she does so."
        audrey.say "Aw, come on, Shiori."
        audrey.say "You look like you just got bad news."
        audrey.say "This is gonna be fun for all of us, girl!"
        audrey.say "After all - two's company, but three's an orgy!"
        "Shiori looks up and manages a meek smile."
        "But I can see that she's still intimidated by the idea of a threesome."
        mike.say "I know what, Audrey."
        mike.say "Why don't you and Shiori finish what you started?"
        mike.say "It might be just the kind of bonding experience you need."
        show shiori surprised
        "Shiori looks at me in surprise, almost shaking her head."
        "But the look on Audrey's face is one of complete agreement."
        show audrey happy
        audrey.say "That's perfect, [hero.name]!"
        audrey.say "Come on, Shiori - let's get on with it!"
        "Before she can say another word, Audrey has the other girl by the wrist."
        show shiori embarrassed
        "She guides Shiori's hand down below my waist."
        "Shiori nods as they stand to either side of me."
        "And then Audrey wastes no time in undoing my pants and pulling out my cock."
        "Shiori looks up at me, and I nod down at her."
        show shiori normal
        "She smiles, more genuinely this time I think, and nods in return."
        "I lean my head back, feeling like a king surveying his kingdom."
        "Audrey works my cock with her usual expert touch."
        "She's rough, but not too rough."
        "And Shiori follows her lead, carefully handling me when told."
        "Perhaps it's the sight of them working together that does it."
        "Watching as a smile spreads across Shiori's face and she forgets herself."
        "Maybe that's what pushes me over the edge so quickly?"
        with vpunch
        "I can't help smiling as I shoot my load a moment later."
        "And I watch as it runs down over Audrey and Shiori's fingers."
        show audrey happy
        show audrey surprised
        "Audrey bursts out laughing, but Shiori looks shocked."
        show shiori happy
        "But then she begins to laugh too, and everything feels right."
        "Perhaps Audrey is right."
        "Perhaps this could be the best thing for all three of us..."
        $ game.flags.officeharemaudshidelay = TemporaryFlag(True, 1)
        $ Harem.join_by_name("office", "audrey", "shiori")
    else:
        "Secretly I'm grateful for Shiori being so meek and obedient right now."
        "Mainly because it means she's handed the power of choice back to me."
        "Audrey needs to be taken in hand, brought to heel."
        "And the first thing to do is nip this problem in the bud!"
        mike.say "No, Shiori."
        mike.say "It's not something that I want."
        mike.say "You run along now, and we'll talk later."
        show shiori normal
        "Shiori looks instantly relieved and sets about picking up the spilt contents of the tray."
        "I hear Audrey begin to protest, but I've been given a confidence boost by Shiori's reaction."
        "This means that I round on Audrey and cut her off before she has the chance to speak."
        mike.say "And as for you, Audrey..."
        mike.say "You can hang around for a while."
        mike.say "As we have something to finish off..."
        hide audrey
        hide shiori
        show audrey work at right4
        show shiori work at left4
        with fade
        pause 0.4
        hide shiori with moveoutleft
        "As Shiori hurries out of the office, I walk back over to my desk."
        "Audrey crosses her arms over her chest and lets out an annoyed huff."
        show audrey annoyed
        audrey.say "That could have been a lot of fun, you know?"
        audrey.say "A nice little arrangement for the three of us!"
        "I shake my head slowly, dismissing Audrey's complaint."
        mike.say "Yeah, Audrey, I know."
        mike.say "But it'd have been what you wanted."
        mike.say "So you'd always have the upper hand."
        mike.say "This way I can comfort Shiori and keep her sweet."
        mike.say "And then I can have both of you whenever I want."
        show audrey normal
        "Audrey tries her best not to look surprised at this idea."
        "I know that she likes to feel as though she's the one in control."
        "But I also know that she loves the idea of us doing it at work too!"
        audrey.say "Well..."
        audrey.say "What makes you think you can have us both, huh?"
        "Without answering, I unzip my flies."
        mike.say "Remember I told Shiori we had something to take care of?"
        mike.say "Now get over here and finish what you started!"
        "For a moment I think that Audrey's going to tell me to go to hell."
        show audrey a at center, zoomAt(2.0, (840, 1340)) with fade
        "But then she shakes her head and hurries to do as she's told."
        "She mutters the whole time she's doing it, but that doesn't put me off."
        "In fact it feels so good to be bossing Audrey about that makes it feel even better!"
        "Audrey works my cock with her usual expert touch."
        "She's rough, but not too rough."
        "But in the end, it's the look of resentment in her eyes that does it for me."
        with vpunch
        "I can't help smiling as I shoot my load a moment later."
        "And I watch as it runs down over Audrey's fingers."
        "The whole time I'm feeling like I managed to put her in her place too!"
        $ shiori.love -= 5
        $ shiori.sub -= 2
        $ audrey.love -= 5
        $ audrey.sub -= 2
    $ game.pass_time(1)
    $ hero.cancel_activity()
    return

label office_audrey_shiori_02:
    "I've had my head buried so deep in my work recently that I've not thought of anything else."
    "And so it comes as a genuine surprise to look up and see Audrey and Shiori standing in the doorway."
    "Taking a quick glance at my watch, I shake my head and ask the inevitable question."
    show audrey work at top_mostleft
    show shiori work at left
    with dissolve
    mike.say "Huh..."
    mike.say "Didn't you guys bring me my morning coffee already?"
    show audrey annoyed
    "Audrey's face instantly twists into an irritated and amazed expression."
    show shiori embarrassed at left4 with ease
    "But Shiori covers her mouth with one hand, giggling at the question."
    shiori.say "Oh, [hero.name]."
    shiori.say "You're so funny!"
    shiori.say "I already brought you some coffee!"
    audrey.say "Yeah, [hero.name], you're a regular riot."
    audrey.say "You should do stand-up!"
    show audrey normal
    play sound door_slam
    "Audrey says this as she slams the door and locks it behind her."
    "And it's only when she does this that I snap out of my funk."
    "Now I realise what the pair of them are here for!"
    mike.say "Oh..."
    mike.say "Oh, now I get it!"
    mike.say "You two want to..."
    show audrey at left5
    show shiori at right5
    with ease
    "Audrey nods as she walks over to my desk."
    mike.say "With me..."
    hide audrey
    hide shiori
    show audrey work at center, zoomAt(1.5, (440, 1040))
    show shiori work at center, zoomAt(1.5, (840, 1040))
    with fade
    "Shiori nods too as she follows at Audrey's side."
    mike.say "Right here and now!"
    show audrey flirt
    audrey.say "Yeah, [hero.name], we do."
    show shiori flirt
    shiori.say "Audrey said it'd be a nice surprise for you!"
    audrey.say "So long as you're not too busy..."
    "I'm up and out of my chair as quickly as I can."
    "And then I'm hurrying to meet the pair of them."
    mike.say "No, no, no..."
    mike.say "I think I have a slot in my schedule!"
    audrey.say "Let us fill it for you."
    audrey.say "And you can fill one of us in return!"
    "Shiori covers her mouth and giggles again."
    show audrey topless
    show shiori topless
    with dissolve
    "But the three of us are already stripping off in anticipation of what's to come next."
    "I feel like slapping myself right now!"
    "How could I have forgotten that the three of us decided to get together like this?"
    show audrey naked
    show shiori naked
    with dissolve
    "All thought of the work on my desk is forgotten as I gaze at Audrey and Shiori."
    "And I can already feel my cock getting hard at the thought of what lies ahead."
    "The only question is who's going to be on the receiving end of it?"
    "Will it be Audrey or Shiori?"
    call office_audrey_shiori_fuck from _call_office_audrey_shiori_fuck
    return

label office_audrey_shiori_fuck:
    menu:
        "Fuck Audrey":
            call office_threesome_audreyfuck_shiori from _call_office_threesome_audreyfuck_shiori
        "Fuck Shiori":
            call office_threesome_shiorifuck_audrey from _call_office_threesome_shiorifuck_audrey
    $ game.pass_time(2)
    $ hero.cancel_activity()
    return

label office_threesome_shiorifuck_audrey:
    "I stare long and hard at the sight of Audrey now that she's naked."
    "But the moment that I tear my eyes away and look at Shiori, it's settled."
    "She just looks so cute and innocent, standing there in front of me."
    "And suddenly there's nothing that I want more than to be inside of her!"
    mike.say "Shiori..."
    mike.say "Come over here..."
    show shiori surprised
    "I see Shiori's eyes go wide and she gasps in surprise."
    "Which, of course only serves to make me want her all the more."
    show shiori normal blush
    "She nods, conquering her fears, and reaches out to take my hand."
    "Part of me was expecting Audrey to protest that I didn't choose her."
    "But she seems to be on her best behaviour, smiling as Shiori comes to me."
    "I sit on the edge of the desk, spreading my legs wide."
    "And I turn Shiori around so that she has her back to me."
    "She looks over her shoulder, biting her lip in anticipation."
    "But I'm more than a little distracted right now."
    "And that's because Shiori's ripe for the taking."
    scene office threesome shiorifuck audrey with fade
    "I just need to decide where I want to stick it..."
    menu:
        "Fuck her ass" if shiori.flags.anal:
            "I know that Shiori's more than a little nervous."
            "But we're already having a threesome in my office."
            "And in the middle of the day too!"
            "So why hold back?"
            "Why not make this as exciting as possible?"
            "With that in mind, I reach out and take a firm hold of Shiori's shapely buttocks."
            "She squeals in genuine surprise, leaping forward a little."
            "But I don't allow her the chance to escape."
            "As soon as I have hold of her, I pull her backwards and onto my cock."
            show office threesome shiorifuck audrey anal
            "She's as tight as I expected, but that's all part of the thrill."
            "And I just keep on pushing into her, ignoring the protests of her muscles."
            shiori.say "Oh..."
            shiori.say "Oh, [hero.name]..."
            shiori.say "That's...that's my ass!"
            "Shiori lets out a sensual moan as her muscles finally submit."
            show office threesome shiorifuck audrey pleasure anal
            "And the sensation of her sinking onto my cock almost finishes me right there!"
            shiori.say "Mmm..."
            shiori.say "[hero.name]..."
            shiori.say "What are you doing to me?!?"
            shiori.say "I don't know what it is - but don't stop!"
            shiori.say "I love it!"
            "Taken by a sudden notion, I bend forwards and slip my hands under Shiori's thighs."
            "She squeals a second time as I lift her into the air, my cock still deep inside of her."
            "Once I have her in my arms, I fold Shiori in half, locking my hands behind her head."
            "And then I lean back over the desk, working her up and down upon my cock."
            "The whole time I'm doing this, Shiori moans with helpless pleasure."
            show office threesome shiorifuck audrey anal aud b
            "I've almost forgotten that Audrey was still in the room with us."
            show office threesome shiorifuck audrey anal aud a
            "But she's not the kind of girl to sit back and let herself be ignored."
            show office threesome shiorifuck audrey anal aud a suck
            "And it's my turn to jump in shock when I feel the sensation of her sucking my balls!"
            "The motion sends Shiori up in the air for a moment."
            "And then she comes back down again, pushing my cock into her even harder than before."
            "I hear what sounds like a wicked chuckle from Audrey, and then she redoubles her efforts."
            "All of which means that I'm fucking Shiori that much harder as a result!"
            "As tight as I'm holding onto her, she's beginning to wriggle and squirm."
            "And I realise that she's cumming a moment later."
            "With Audrey working my balls and Shiori grinding herself on my cock, I can't hold on."
            "I'm going to cum too!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_shiori" not in DONE:
                call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori
            else:
                menu:
                    "Cum inside":
                        "With one last thrust, I shoot my load into Shiori."
                        "I'm in as deep as I can possibly go when I cum."
                        "Which means that she takes it all, with nothing held back."
                        show office threesome shiorifuck audrey aud a suck creampie
                        shiori.say "Aaah..."
                        shiori.say "[hero.name]..."
                        shiori.say "You're...cumming...in...me!"
                        "All I can do is hold onto Shiori as I fill her."
                        "That and hope that nobody hears the sound of her cries."
                        "Those same cries become quieter as I finish cumming."
                        "And at the same time, Shiori slides off of me and flops to the floor."
                        "She lies there panting, soaked in sweat."
                        "The cum is already starting to seep out."
                        "It pools and then begins to soak into the carpet."
                    "Cum outside":
                        "I manage to lift Shiori off of my cock just before I shoot my load into her."
                        "It pops out of her with an audible sound, and she wails in surprise."
                        show office threesome shiorifuck audrey aud c creampie outside -anal -vaginal
                        shiori.say "Oh..."
                        shiori.say "[hero.name]..."
                        shiori.say "Don't stop now!"
                        "I'm too tied up to tell Shiori that I don't intend to."
                        "All I can do is hold onto her as I cum."
                        "Shiori takes the whole thing over her chest and belly."
                        show office threesome shiorifuck audrey cum onbody
                        "White stripes of sticky cum crisscross her breasts."
                        "And she writhes the whole time, rubbing it over her already slick skin."
                        "Shiori slides out of my arms and flops to the floor."
                        "She lies there panting, soaked in sweat."
                    "Share the love" if "office_cumshare_audrey_shiori" in DONE:
                        call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_1
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "Sure, we're getting up to some pretty wild stuff here."
            "A threesome in my office and in the middle of the day."
            "But that doesn't mean I can do whatever I like."
            "I have to think of Shiori and how nervous she seems."
            "With that in mind, I reach out and take a gentle hold of her haunches."
            "Shiori lets out a little squeal of surprise."
            "But she settles into my grasp a moment later without protest."
            "I pull her slowly towards me, feeling my cock slip between her legs."
            "And then I feel it slide along the lips of her pussy."
            show office threesome shiorifuck audrey vaginal
            "For all that she's nervous, Shiori's already nice and wet!"
            "All it takes is a gentle push..."
            "Then I feel myself sinking into her."
            shiori.say "Oh..."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You feel SO good inside of me!"
            "The sound of Shiori's voice is so genuine and sensual."
            show office threesome shiorifuck audrey pleasure vaginal
            "I almost shoot my load inside of her as I listen to it!"
            shiori.say "Mmm..."
            shiori.say "[hero.name]..."
            shiori.say "What are you doing to me?!?"
            shiori.say "You're filling me up!"
            "Taken by a sudden notion, I bend forwards and slip my hands under Shiori's thighs."
            "She squeals a second time as I lift her into the air, my cock still deep inside of her."
            "Once I have her in my arms, I fold Shiori in half, locking my hands behind her head."
            "And then I lean back over the desk, working her up and down upon my cock."
            "The whole time I'm doing this, Shiori moans with helpless pleasure."
            show office threesome shiorifuck audrey vaginal aud b
            "I've almost forgotten that Audrey was still in the room with us."
            show office threesome shiorifuck audrey vaginal aud a
            "But she's not the kind of girl to sit back and let herself be ignored."
            show office threesome shiorifuck audrey vaginal aud a suck
            "And it's my turn to jump in shock when I feel the sensation of her sucking my balls!"
            "The motion sends Shiori up in the air for a moment."
            "And then she comes back down again, pushing my cock into her even harder than before."
            "I hear what sounds like a wicked chuckle from Audrey, and then she redoubles her efforts."
            "All of which means that I'm fucking Shiori that much harder as a result!"
            "As tight as I'm holding onto her, she's beginning to wriggle and squirm."
            "And I realise that she's cumming a moment later."
            "With Audrey working my balls and Shiori grinding herself on my cock, I can't hold on."
            "I'm going to cum too!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_shiori" not in DONE:
                call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_2
            else:
                menu:
                    "Cum inside":
                        "With one last thrust, I shoot my load into Shiori."
                        with hpunch
                        "I'm in as deep as I can possibly go when I cum."
                        with hpunch
                        "Which means that she takes it all, with nothing held back."
                        show office threesome shiorifuck audrey vaginal aud a suck creampie with hpunch
                        shiori.say "Aaah..."
                        shiori.say "[hero.name]..."
                        shiori.say "You're...cumming...in...me!"
                        "All I can do is hold onto Shiori as I fill her."
                        "That and hope that nobody hears the sound of her cries."
                        "Those same cries become quieter as I finish cumming."
                        "And at the same time, Shiori slides off of me and flops to the floor."
                        "She lies there panting, soaked in sweat."
                        "The cum is already starting to seep out."
                        "It pools and then begins to soak into the carpet."
                    "Cum outside":
                        "I manage to lift Shiori off of my cock just before I shoot my load into her."
                        "It pops out of her with an audible sound, and she wails in surprise."
                        show office threesome shiorifuck audrey aud c creampie outside -anal -vaginal
                        shiori.say "Oh..."
                        shiori.say "[hero.name]..."
                        shiori.say "Don't stop now!"
                        "I'm too tied up to tell Shiori that I don't intend to."
                        "All I can do is hold onto her as I cum."
                        "Shiori takes the whole thing over her chest and belly."
                        show office threesome shiorifuck audrey aud b cum onbody with vpunch
                        "White stripes of sticky cum crisscross her breasts."
                        "And she writhes the whole time, rubbing it over her already slick skin."
                        "Shiori slides out of my arms and flops to the floor."
                        "She lies there panting, soaked in sweat."
                    "Share the love" if "office_cumshare_audrey_shiori" in DONE:
                        call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_3
    $ shiori.sexperience += 1
    return

label office_threesome_audreyfuck_shiori:
    "For a moment, I seriously think about making Shiori the focus of all my attention."
    "She seems so nervous, and she's kind of being thrown in at the deep end."
    "But then I catch Audrey's eye, and the matter's settled."
    "She just looks at me in that half alluring, half infuriating way she has."
    "And just like that, she's the only thing in the world that I want."
    "Anyway, maybe Shiori needs to be eased into something like this?"
    "And if I fuck Audrey instead of her, she can watch and learn too."
    "But how to make her aware of my intentions?"
    "I smile as the thought occurs to me."
    play sound spank
    with hpunch
    "The sound of my hand connecting with Audrey's ass is louder than even I expected."
    show audrey surprised at startle
    show shiori surprised at startle
    "Both she and Shiori jump at the unexpected noise, but only Audrey feels the slap."
    show shiori annoyed blush
    audrey.say "Ow..."
    audrey.say "Whoa..."
    show audrey angry
    audrey.say "What the hell?!?"
    "I cock my head on one side, giving Audrey an unimpressed look."
    mike.say "Ah, come on, Audrey."
    mike.say "Don't try to play the innocent with me."
    mike.say "We both know that you're partial to a spanking."
    "Shiori stares at Audrey, her mouth hanging open in shock."
    show audrey annoyed
    "Audrey begins to say something, but then she stops in her tracks."
    show audrey annoyed blush
    "Something strange starts to happen to her cheeks, like they're changing colour."
    "Anyone else and I wouldn't have been surprised in the slightest."
    "But I've never seen Audrey's cheeks turn red before, never seen her blush!"
    "Is she actually embarrassed to admit something like that in front of Shiori?!?"
    audrey.say "I...I..."
    audrey.say "I suppose I...kinda liked it..."
    "Keen to keep the momentum going in my direction, I push Audrey towards the desk."
    "She comes without any resistance, letting me guide her up and onto it."
    "Once there, I make her crouch down so that she's at just the right height."
    scene office threesome audreyfuck shiori
    show office threesome audreyfuck shiori
    with fade
    "And then I probe between her legs with my now stiff cock."
    "I can already feel that Audrey's getting excited down there."
    "But should I go for the obvious choice?"
    "Or maybe get creative?"
    menu:
        "Fuck her ass":
            "I've already gotten a thrill from giving Audrey a little tap on the ass."
            "And it's a feeling that just won't quit, making me want more."
            "Which is why I part her buttocks just a little."
            "Just wide enough for me to slide my cock between them."
            "Audrey stiffens almost as soon as she feels what I'm doing."
            show office threesome audreyfuck shiori lookback
            audrey.say "Hey!"
            audrey.say "Who said you could..."
            "But it's not like I stop what I'm doing to listen."
            show office threesome audreyfuck shiori pleasure anal
            audrey.say "Ah..."
            audrey.say "Oh...oh my god!"
            "The muscles of Audrey's ass put up more of a fight than she does herself."
            "They resist even as I can hear her melting into a puddle of liquid pleasure."
            audrey.say "Okay...okay..."
            audrey.say "You can do that to me..."
            audrey.say "You can do whatever you want..."
            show office threesome audreyfuck shiori anal
            audrey.say "Just don't stop!"
            "The sensation of pushing my way into Audrey is incredible."
            "And when her muscles can fight no more, it just gets better."
            "Once I'm as deep inside of her as I can go, I begin to speed up."
            "The effect on her is instant and dramatic."
            "Audrey seems to lose the ability to speak."
            show office threesome audreyfuck shiori ahegao
            "Instead she moans and pants as I thrust in and out of her."
            "But then I catch sight of Shiori, watching me with a look of fascination in her eyes."
            "And I realise that I don't have to keep up with Audrey, just impress Shiori."
            "This lifts a weight off of my shoulders, and I redouble my efforts."
            "As I thrust in and out of Audrey, I see Shiori creeping closer."
            "She crawls onto the desk and positions herself in front of the other girl."
            "I watch as curiosity seems to get the better of her usual meekness."
            "And she reaches out with one hand to touch Audrey."
            "I don't know what Shiori was expecting to happen."
            "But I'm willing to be it wasn't Audrey beating her to the punch."
            "Before Shiori knows what's happening, Audrey's hand is between her thighs."
            show office threesome audreyfuck shiori orgasm
            "Shiori yelps in surprise and fear as she feels her pussy being rubbed with vigour."
            "I watch the expression of shock become one of surrender on Shiori's face."
            "And I can only imagine what the look on Audrey's must be like right now!"
            "On top of all that, I can feel myself cumming too!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_shiori" not in DONE:
                call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_4
            else:
                menu:
                    "Cum inside":
                        "Staring at Shiori, I can't hope to pull out in time."
                        "And so I feel myself lose it inside of Audrey instead."
                        with hpunch
                        "She bucks and squirms the whole time, squeezing Shiori as she does so."
                        show office threesome audreyfuck shiori creampie with hpunch
                        audrey.say "Ah..."
                        audrey.say "Yeah..."
                        audrey.say "I want it, [hero.name]..."
                        audrey.say "I want it all!"
                        "Only when I've finished and let go of her does Audrey stop."
                        "Without my support, she collapses sideways onto the desk."
                        "Released from her grip too, Shiori topples over backwards."
                        "The only one left standing is me."
                        "And my legs are already starting to feel like rubber."
                    "Pull out":
                        "I just manage to pull my cock out of Audrey before it's too late."
                        show office threesome audreyfuck shiori outside -anal -vaginal
                        "But she doesn't seem too happy with that choice, groaning as I do so."
                        audrey.say "No..."
                        hide office threesome audreyfuck shiori
                        show office threesome audreyfuck shiori creampie outside
                        audrey.say "No, no, no..."
                        audrey.say "Not yet...not yet!"
                        show office threesome audreyfuck shiori cum onbody
                        show office threesome audreyfuck shiori cum onass
                        with hpunch
                        "All I can do is gasp as I shoot my load over Audrey's back."
                        with hpunch
                        "Cum spatters down on her back in uneven lines."
                        "And then it starts to run down towards her buttocks."
                        "Without my support, she collapses sideways onto the desk."
                        "Released from her grip too, Shiori topples over backwards."
                        "The only one left standing is me."
                        "And my legs are already starting to feel like rubber."
                    "Share the love" if "office_cumshare_audrey_shiori" in DONE:
                        call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_5
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            "Audrey's ass is always an appealing prospect, especially after a spanking."
            "But her pussy is just there for the taking, glistening and wet."
            "All it takes is a little push forwards, a little bit of a thrust..."
            "And just like that, I'm sinking into her."
            show office threesome audreyfuck shiori vaginal
            "In one smooth motion I go as deep as I possibly can."
            "And I feel Audrey shudder as I do so."
            show office threesome audreyfuck shiori pleasure
            audrey.say "Mmm..."
            audrey.say "Oh...oh god..."
            audrey.say "You can do that to me anytime..."
            audrey.say "You don't even need to ask!"
            "The fact that Audrey was all ready for me means I don't have to go slow."
            "Instead I can pick up speed almost as soon as we get started."
            "And I don't waste any time building it up either."
            "Audrey takes everything that I have to give, soaking it up like a sponge."
            "It seems like no matter how much I give her, she still wants more!"
            "For a moment I begin to feel a little intimidated."
            show office threesome audreyfuck shiori ahegao
            "I'm worried that I won't be able to keep up this pace for too long."
            "But then I catch sight of Shiori, watching me with a look of fascination in her eyes."
            "And I realise that I don't have to keep up with Audrey, just impress Shiori."
            "This lifts a weight off of my shoulders, and I redouble my efforts."
            "As I thrust in and out of Audrey, I see Shiori creeping closer."
            "She crawls onto the desk and positions herself in front of the other girl."
            "I watch as curiosity seems to get the better of her usual meekness."
            "And she reaches out with one hand to touch Audrey."
            "I don't know what Shiori was expecting to happen."
            "But I'm willing to be it wasn't Audrey beating her to the punch."
            "Before Shiori knows what's happening, Audrey's hand is between her thighs."
            show office threesome audreyfuck shiori orgasm
            "Shiori yelps in surprise and fear as she feels her pussy being rubbed with vigour."
            "I watch the expression of shock become one of surrender on Shiori's face."
            "And I can only imagine what the look on Audrey's must be like right now!"
            "On top of all that, I can feel myself cumming too!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_shiori" not in DONE:
                call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_6
            else:
                menu:
                    "Cum inside":
                        "Staring at Shiori, I can't hope to pull out in time."
                        "And so I feel myself lose it inside of Audrey instead."
                        with hpunch
                        "She bucks and squirms the whole time, squeezing Shiori as she does so."
                        show office threesome audreyfuck shiori creampie with hpunch
                        audrey.say "Ah..."
                        audrey.say "Yeah..."
                        audrey.say "I want it, [hero.name]..."
                        audrey.say "I want it all!"
                        "Only when I've finished and let go of her does Audrey stop."
                        "Without my support, she collapses sideways onto the desk."
                        "Released from her grip too, Shiori topples over backwards."
                        "The only one left standing is me."
                        "And my legs are already starting to feel like rubber."
                    "Pull out":
                        "I just manage to pull my cock out of Audrey before it's too late."
                        show office threesome audreyfuck shiori outside -anal -vaginal
                        "But she doesn't seem too happy with that choice, groaning as I do so."
                        audrey.say "No..."
                        hide office threesome audreyfuck shiori
                        show office threesome audreyfuck shiori creampie outside
                        audrey.say "No, no, no..."
                        audrey.say "Not yet...not yet!"
                        show office threesome audreyfuck shiori cum onbody
                        show office threesome audreyfuck shiori cum onass
                        with hpunch
                        "All I can do is gasp as I shoot my load over Audrey's back."
                        with hpunch
                        "Cum spatters down on her back in uneven lines."
                        "And then it starts to run down towards her buttocks."
                        "Without my support, she collapses sideways onto the desk."
                        "Released from her grip too, Shiori topples over backwards."
                        "The only one left standing is me."
                        "And my legs are already starting to feel like rubber."
                    "Share the love" if "office_cumshare_audrey_shiori" in DONE:
                        call office_cumshare_audrey_shiori from _call_office_cumshare_audrey_shiori_7
    $ audrey.sexperience += 1
    return

label office_cumshare_audrey_shiori:
    "At the very last moment, Audrey seems to find a last reserve of energy."
    "She begins directing traffic, ordering Shiori and me here and there."
    "And it's only as I start to shoot my load that I see what she was doing."
    scene office cumshare audrey shiori
    "She and Shiori are kneeling in front of me, looking up with expectant faces."
    show office cumshare audrey shiori audreyopen
    "Audrey already has her mouth open, knowing what's about to happen."
    show office cumshare audrey shiori shiorilookdown
    "But it takes Shiori a split-second too long to realise she should be doing that too."
    show office cumshare audrey shiori cumshot cum shiorionface with vpunch
    "This means that when I do cum, it hits her in the side of the face."
    show office cumshare audrey shiori cumshot cum shioriopen with vpunch
    "Time seems to slow down, and I see every tiny chance in her expression."
    "From surprise as the first drops hit her to horror as her entire face is striped."
    "In contrast, Audrey has a smug, knowing smile on her face as she takes her share."
    show office cumshare audrey shiori cumshot cum audreyonface with vpunch
    "The cum hits her just as it does Shiori, but the difference is she's ready for it."
    show office cumshare audrey shiori cumshot cum audreyinmouth shioriinmouth with vpunch
    "And then she chuckles at the sight of Shiori, who's grimacing and wailing."
    show office cumshare audrey shiori -cumshot
    shiori.say "Audrey..."
    shiori.say "Why didn't you tell me?!?"
    shiori.say "Some of it went in my mouth!"
    audrey.say "Don't worry, Shiori."
    audrey.say "You'll get used to it soon enough!"
    "I shake my head and roll my eyes a little, trying to sympathise."
    "But then I can't help joining in the laughter too."
    "Eventually, Shiori shrugs."
    shiori.say "I...I guess it is kind of funny."
    shiori.say "It's the first time you've ever served me a drink, [hero.name]!"
    $ DONE["office_cumshare_audrey_shiori"] = game.days_played
    return

label office_audrey_lavish_showdown:
    scene bg restaurant
    "I should be over the moon right now, wallowing in my own good fortune."
    "After all, it's taken me ages to convince Lavish to go out on a date with me."
    "And here we are, sitting at a table in a fancy restaurant, actually doing it!"
    "But for some reason I just can't seem to get her to switch off and relax."
    "No sooner has the waiter taken our orders than she seems to want to talk about work!"
    show lavish date zorder 2 at center, zoomAt (1.5, (640, 1140))
    lavish.say "Look, I'm not trying to undermine Shiori here."
    lavish.say "She's sweet, and she tries SO hard."
    lavish.say "But I'm sure she's the reason we're so inefficient..."
    mike.say "Ah..."
    mike.say "Lavish..."
    mike.say "Could we maybe drop the office talk?"
    mike.say "I mean, this IS supposed to be a date!"
    show lavish sad
    lavish.say "Oh...okay, [hero.name]."
    lavish.say "Sorry - I just have work on my mind most of the time!"
    show lavish normal
    lavish.say "How about I just put it all in an email, huh?"
    "Lavish punctuates this with one of her most devastating smiles."
    "And all I can do is nod as a dumb smile spreads across my own face."
    "She's so beautiful that she could literally get away with murder!"
    mike.say "It's okay, Lavish, really."
    mike.say "I was just looking forward to getting to know you."
    mike.say "I mean the real you - the person you are outside of work."
    "Lavish chuckles at this, fluttering her eyelids at me."
    "And I can pretty much feel my heart leap inside my chest as she does so."
    "Wow - is she really having that kind of effect on me?"
    show lavish blush
    lavish.say "Aw..."
    lavish.say "That's so nice to hear, [hero.name]."
    show lavish -blush
    lavish.say "But I'm usually so caught up in my work, you know what I mean?"
    lavish.say "There's not much time for anything else!"
    mike.say "Oh no, Lavish."
    mike.say "That can't be true!"
    show lavish at startle
    audrey.say "Yeah, Lavish, he's right."
    audrey.say "So quit being modest and spill your guts!"
    hide lavish with dissolve
    "At the sound of a familiar voice, Lavish and I glance around as one."
    show audrey date at right with easeinright
    "And there's Audrey, as large as life."
    "The surprise that's written all over our faces doesn't seem to bother Audrey."
    hide audrey
    show lavish date surprised zorder 2 at center, zoomAt (1.5, (440, 1140))
    show audrey date flirt zorder 1 at center, zoomAt (1.5, (940, 1140))
    with hpunch
    "She just pulls a chair from a nearby table and sits down with us."
    show audrey annoyed
    audrey.say "Sorry I'm late."
    audrey.say "My uber took forever to find this place."
    show audrey normal
    audrey.say "So...what did I miss?"
    "I glance from Audrey to Lavish and back again."
    "But nobody else seems to be about to ask the obvious question."
    mike.say "Erm, Audrey..."
    mike.say "I hope you don't mind me asking this..."
    mike.say "But what in the hell are you doing here?"
    show audrey surprised
    "Audrey leans back in her chair, head cocked to one side."
    "She has a look of confusion on her face as she does so."
    audrey.say "Huh?"
    audrey.say "I thought you said this was the place, [hero.name]?"
    show audrey normal
    audrey.say "Anyway, where's everyone else?"
    audrey.say "Are they late too?"
    show lavish bored
    lavish.say "Oh dear, Audrey."
    lavish.say "You must not have understood."
    lavish.say "Tonight was just for [hero.name] and me!"
    lavish.say "I feel so embarrassed for you!"
    show audrey surprised
    "Audrey's mouth hangs open as Lavish tries to explain the situation to her."
    "But I can't help smelling a rat as I study Audrey's face."
    "I know her too well to believe that she was simply mistaken."
    audrey.say "Oh no..."
    audrey.say "You mean this wasn't an outing for the whole office?!?"
    show audrey awkward
    audrey.say "Well now I feel awful!"
    audrey.say "Tell you what - I'll leave you to it."
    hide audrey
    show audrey date happy zorder 1 at right5, vshake
    "With that, Audrey stands up and gives us a little wave."
    hide audrey with easeoutright
    "I'm still suspicious of her, but I'm also eager to placate Lavish too."
    show lavish date at center, zoomAt (1.5, (440, 1140)) with fade
    "And so the moment that I can, I turn my attention to her."
    "Maybe I can still salvage this thing if I focus on the girl I'm supposed to be on a date with!"
    mike.say "I'm so sorry, Lavish."
    mike.say "She must have overheard us making plans and got the wrong idea."
    "Lavish shakes her head, dismissing my apology."
    lavish.say "There's no need to say sorry, [hero.name]."
    show lavish happy
    lavish.say "It's actually pretty funny!"
    mike.say "I suppose it is!"
    "Lavish laughs and I find myself joining in."
    "Maybe she's right and this is going to be something we look back on and laugh."
    "But then I feel something moving under the table."
    "Something between my thighs that's touching my groin!"
    "I look up at Lavish, noting the smile on her face."
    "Is she...is she giving me a foot-job right now?"
    "As discreetly as I can manage, I lift the edge of the tablecloth."
    "Looking down I fully expect to see Lavish's foot between my legs."
    "And so it comes as a genuine shock to see Audrey's face looking up at me instead!"
    scene expression f"bg {game.room}" at blur(8), dark, dark
    show audrey b date flirt at center, zoomAt (2.5, (640, 1640)), dark
    with wipeup
    "She gives me a devilish smile and holds a finger to her lips."
    "Then she busies herself with the task of unzipping my pants!"
    menu:
        "Do not stop Audrey":
            "I open my mouth, meaning to cry out in alarm."
            "But then I stop myself before I can form the words."
            "How can I leap up and say something like that?"
            "In the middle of a date and a crowded restaurant?!?"
            "Damn it - Audrey's got me right where she wants me!"
            scene bg restaurant
            show lavish date zorder 2 at center, zoomAt (1.5, (640, 1140))
            with wipedown
            "I drop the edge of the tablecloth and smile up at Lavish."
            "Maybe if I can just ride this out it'll be okay."
            show lavish sad
            lavish.say "Are you okay, [hero.name]?"
            lavish.say "You look a little distracted."
            mike.say "I'm okay, Lavish."
            mike.say "Just a little freaked out..."
            "It's now that I feel Audrey pull my cock out of my pants."
            "She squeezes it hard and then I feel her lips close around it."
            show lavish flirt
            "I can't help enjoying the sensation, and I'm soon as hard as a rock."
            "Audrey licks, sucks and caresses me like her life depends on it."
            "And it's all I can do to keep on nodding and smiling as Lavish talks."
            "I don't dare open my mouth for fear of groaning from Audrey's attentions."
            "It doesn't take long for me to feel myself cumming."
            with vpunch
            "And I stiffen in my seat as I shoot my load into Audrey's mouth."
            "I just about manage to smile as it happens."
            "Because as far as I'm concerned, the ordeal's now over - right?"
            "But then I see the edge of the tablecloth moving."
            show lavish surprised
            show audrey date joke zorder 1 at center, zoomAt (1.25, (1040, 1140)) with moveinbottom
            "And Audrey crawls out from under the table."
            show audrey at center, zoomAt (1.25, (1040, 840)) with move
            "She gets to her feet as Lavish looks on in shock."
            hide lavish
            hide audrey
            show audrey kiss date with fade
            $ audrey.flags.kiss += 1
            "Then she leans in to kiss me full on the lips."
            "Audrey's mouth is still full of my cum as she does this."
            "And she makes no effort to keep it from spilling over her lips."
            hide audrey
            show audrey date flirt at right
            show lavish date surprised at left4
            "Once the kiss is over, she smiles at Lavish and sits herself down on my lap."
            audrey.say "Mmm..."
            audrey.say "No need to show me a menu."
            audrey.say "[hero.name] here just filled me up nicely!"
            lavish.say "What...what is she saying?!?"
            audrey.say "I'm saying I just sucked him off under the table, Lavish."
            if audrey.flags.mikeNickname in nickname_master:
                audrey.say "Because that's what sex slaves do and that's what I am to him!"
            else:
                audrey.say "And he loved every fucking second of it too!"
            "Lavish shakes her head at this, starting to get up."
            show lavish sad
            lavish.say "I...I think I should go..."
            mike.say "No, Lavish..."
            mike.say "This isn't what you think!"
            show audrey annoyed
            "Audrey rolls her eyes as she gets up from my lap and pushes Lavish back down."
            audrey.say "Oh...I'm so sorry, Lavish."
            audrey.say "I just saw that the two of you were going on a date and..."
            show audrey blush
            audrey.say "And I just went crazy with jealousy."
            show audrey date normal
            audrey.say "I HAVE to have him, Lavish."
            audrey.say "Will you share him with me?"
            audrey.say "Please - I'm begging you?!?"
            lavish.say "I...I suppose..."
            show lavish normal blush
            lavish.say "Maybe we could?"
            show audrey happy
            "Audrey smiles and throws her arms around the other girl."
            audrey.say "Oh, thank you, Lavish."
            audrey.say "You just saved my life!"
            "All I can do is watch and shake my head."
            "I simply can't believe how much of a manipulator Audrey really is!"
            $ game.flags.officeharemaudlavdelay = TemporaryFlag(True, 2)
            $ Harem.join_by_name("office", "audrey", "lavish")
        "Stop Audrey":
            mike.say "Audrey!"
            mike.say "What are you doing down there?!?"
            "I leap out of my seat as I yell in alarm."
            scene bg restaurant
            show lavish date surprised zorder 1 at center, zoomAt (1.5, (640, 1140))
            with vpunch
            "Unfortunately, this also results in the table being turned over."
            with hpunch


            "Everything on it is sent crashing to the ground."
            hide lavish
            show lavish date surprised at left4, vshake
            "Lavish lets out a cry of alarm and leaps up too."
            show audrey date joke zorder 2 at center, zoomAt (1.25, (1040, 1140)) with moveinbottom
            "All of which leaves Audrey crouching between us on the floor."
            audrey.say "Well..."
            audrey.say "This is a little awkward!"
            lavish.say "Wh...what's going on?"
            lavish.say "I don't understand, [hero.name]."
            lavish.say "Why is she under the table?!?"
            "Luckily for me, my pants are still zipped up."
            "So nobody else see what Audrey was up to."
            mike.say "I have no idea, Lavish!"
            mike.say "I honestly thought she'd left."
            audrey.say "There we are - found it!"
            hide audrey
            show audrey date at right
            with dissolve
            "Lavish and I watch in amazement as Audrey gets to her feet."
            "Only now can I see that she's holding an earring in her hand."
            "She's actually got the audacity to pretend she was looking for lost jewellery!"
            audrey.say "Well, now I really can be leaving."
            show audrey flirt
            audrey.say "Enjoy the rest of your date!"
            hide audrey with moveoutright
            "With that, Audrey turns on her heel and walks out of the restaurant."
            "Which leaves Lavish and me in the middle of the chaos she's caused."
            "And all we can do is stare at each other in stunned silence."
    $ game.pass_time(1)
    $ hero.cancel_activity()
    return

label office_audrey_lavish_01:
    "I don't know what's up with me today, I just can't get my head into my work."
    "Maybe I got out of the wrong side of the bed, or I'm just in a shitty mood."
    "But whatever the reason, I'm in a funk and I can't seem to shake it off."
    "With a resigned sigh, I lean back in my chair and put my hands behind my head."
    "Maybe I'm going about this the wrong way."
    "Maybe, rather than forcing myself to work, I should be trying to relax instead."
    "It's right about then that a thought occurs to me."
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "Picking up the phone on my desk, I punch in an internal extension."
    lavish.say "Yes, [hero.name]?"
    lavish.say "Is there something I can do for you?"
    mike.say "Yeah, Lavish, there is."
    mike.say "Would you mind stepping into my office for a moment?"
    lavish.say "Of course."
    lavish.say "I'll be right there."
    "I can't help smiling as Lavish puts down the phone."
    "She's so efficient and eager to please."
    "Not like some people that I could mention."
    "Speaking of which..."
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "I press down the receiver and then dial another extension."
    audrey.say "Urgh..."
    audrey.say "What is it now?!?"
    mike.say "And a very good morning to you too, Audrey."
    audrey.say "Whatever, [hero.name]."
    mike.say "Look, just shut your mouth, Audrey."
    mike.say "And get your ass in my office - right now!"
    "All I hear on the other end of the line is a muffled muttering."
    "I don't doubt most of it is insults directed at me."
    "But the important thing is that Audrey slams down the phone without open protest."
    "And that means that she's sullenly resolved to doing as she's told."
    "All I have to do now is sit back and wait for my guests to arrive."
    "Of course, the first one to turn up is Lavish."
    play sound door_knock
    "She knocks and then politely waits for permission to enter."
    mike.say "Come in, Lavish."
    show lavish work at left with moveinleft
    lavish.say "Hello, [hero.name]."
    lavish.say "I came as fast as I could!"
    show lavish at right5 with move
    "Lavish hurries over to my desk, notepad and dictaphone in hand."
    show audrey work annoyed at left with moveinleft
    audrey.say "Okay, here I am."
    show audrey at left5 with move
    audrey.say "I hope you're happy now!"
    show lavish annoyed
    "At the sound of Audrey's voice, Lavish stops in her tracks."
    "She looks at the other girl and then at me, wanting an explanation."
    show lavish normal
    lavish.say "Uhm..."
    lavish.say "Should I maybe come back later?"
    mike.say "No, Lavish, no."
    mike.say "I need the both of you here for what I have in mind."
    "Lavish still looks more than a little puzzled."
    "But Audrey seems to have no such trouble reading my true intentions."
    show audrey flirt
    audrey.say "Why didn't you just say so, [hero.name]?"
    audrey.say "I'd have come running if I knew that was what you had in mind!"
    lavish.say "I...I don't understand..."
    audrey.say "Jesus, Lavish - how naive are you?"
    audrey.say "He's called us in here to give him some executive relief!"
    show lavish blush surprised
    "At this, Lavish's eyes go wide and she covers her mouth with her hands."
    show audrey mock
    "Audrey rolls her own eyes and chuckles, amused by the other girl's surprise."
    audrey.say "Didn't we discuss this already, Lavish?"
    show audrey flirt
    show lavish normal
    audrey.say "Just think of it as career advancement, yeah?"
    audrey.say "Sure, [hero.name]'s fucking you."
    audrey.say "But that means he owes you as well!"
    "When she puts it that way, this doesn't sound as much fun!"
    "And so I make an effort to move things along and stop that kind of talk."
    mike.say "So we're agreed then?"
    mike.say "We're doing this thing?"
    "By way of answer, Audrey turns and begins to undress Lavish."
    show lavish naked
    "Lavish shrinks back at first, but then slowly starts to return the favour."
    show audrey naked
    "I watch them as I strip off my own clothes, enjoying the show they're putting on."
    "I can already feel the funk lifting and my stress melting away."
    "But now I have a choice to make."
    "Which one of them am I actually going to fuck?"
    call office_audrey_lavish_fuck from _call_office_audrey_lavish_fuck
    return

label office_audrey_lavish_fuck:
    menu:
        "Fuck Audrey":
            call office_threesome_audreyfuck_lavish from _call_office_threesome_audreyfuck_lavish
        "Fuck Lavish":
            call office_threesome_lavishfuck_audrey from _call_office_threesome_lavishfuck_audrey
    $ game.pass_time(2)
    $ hero.cancel_activity()
    return

label office_threesome_audreyfuck_lavish:
    "I can sense that Lavish is still more than a little nervous."
    "And so it makes sense for me to ensure that Audrey's the centre of attention instead."
    "So I waste no time in taking a hold of her hand and guiding her down onto all fours."
    scene office threesome audreyfuck lavish
    show office threesome audreyfuck lavish outside
    with fade
    "Audrey looks pleased to be the one that's taking the lead."
    "But I still wonder if she was secretly looking forward to watching the same happen to Lavish."
    "I don't know which of the two urges is stronger in Audrey."
    "The need to indulge her own appetites or the desire to torture someone else!"
    "Either way, Audrey offers no resistance as she lies down on her back."
    "Instead she smiles over her shoulder at me the whole time."
    show office threesome audreyfuck lavish lookback
    audrey.say "Don't worry, Lavish."
    audrey.say "You just sit back and relax."
    audrey.say "[hero.name] and I are gonna show you how it's done!"
    "I spare a moment to glance at Lavish."
    "She's crouched down a little way from Audrey's head."
    "She still looks nervous, unsure about what happens next."
    "But I swear that I can see the beginnings of genuine interest in her eyes too."
    mike.say "She's right, Lavish."
    mike.say "It's going to be okay."
    mike.say "I'll make sure it's okay."
    "Lavish rewards my words with a sweet smile."
    "And I can't help smiling back at her."
    audrey.say "Hello!"
    audrey.say "You mind looking my way once in a while?!?"
    audrey.say "I am the one you're supposed to be fucking here!"
    "A suitably barbed response springs to mind."
    "But I keep my mouth closed as I turn my attention back to Audrey."
    "Sometimes, actions speak louder than words."
    "And my next action is to choose exactly where I put a certain something..."
    menu:
        "Fuck her ass":
            "I should make it clear that I'm not actually mad at Audrey right now."
            "Nor is she getting under my skin any more than usual."
            "I just feel that she needs taking down a peg or two."
            "And that Lavish needs to see that I have some say in this thing too."
            scene office threesome audreyfuck lavish
            $ audrey.sub += 1
            "Which is why I take a firm hold of her buttocks a moment later."
            "Audrey stiffens a little at the sensation."
            "I have no idea if she suspects what I have in mind."
            "But even if she does, I don't give her the chance to object."
            audrey.say "Whoa..."
            audrey.say "What are you..."
            show office threesome audreyfuck lavish lookback
            audrey.say "Where are you putting that..."
            "Audrey wriggles and squirms as I push my cock into her ass."
            "But for all her efforts, she only succeeds in helping push it deeper."
            audrey.say "Ah..."
            audrey.say "Oh...you..."
            show office threesome audreyfuck lavish pleasure
            audrey.say "You shit...don't stop!"
            "By now I'm as deep inside of Audrey as I can possibly go."
            "And I'm loving every moment of feeling her around my cock."
            "The fact that she clearly feels the same way is a massive turn-on too."
            "And the way that she's urging me on makes me hold nothing back."
            "Before I know it, I'm pounding away without mercy."
            "Nothing that I see or hear from Audrey stops me either."
            "She takes all that I have to give, soaking it up like a sponge."
            "One moment she's moaning with pleasure."
            "The next she's demanding that I fuck her harder than ever!"
            "In the middle of all this, I forget about everything else."
            "The only thing that seems to exist is Audrey."
            "Well, Audrey and my need to keep on fucking her to the very end!"
            "It's then that I feel the strangest sensation."
            "The feeling of someone touching, softly and gently."
            "I look down to see Lavish has her hands upon my chest."
            "It's such a contrast to the way I'm pounding Audrey."
            "Her touch is so gentle it almost feels unreal."
            "And then she plants her lips over mine..."
            "Lavish kissed me gently and with a subtle passion."
            "Her tongue darts into my mouth as she presses closer."
            "And I can't help leaning into the kiss with passion."
            "Just as much passion as I'm putting into fucking Audrey too."
            "Either one of these things would have been enough to finish me off."
            "But all together I'm lucky to be able to last more than a couple of seconds!"
            "And I just know I'm about to cum!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_lavish" not in DONE:
                call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish
            else:
                menu:
                    "Cum inside":
                        "Lavish's kiss has me so distracted that I totally forget myself."
                        "That means I keep right on thrusting into Audrey to the very end."
                        $ audrey.sub += 2
                        show office threesome audreyfuck lavish ahegao with hpunch
                        "I shoot my load into her without holding a single thing back."
                        show office threesome audreyfuck lavish creampie with hpunch
                        "And she writhes on the end of my cock the whole time."
                        audrey.say "Yeah..."
                        audrey.say "That's what I want!"
                        audrey.say "I want all of it!"
                        "My hands are still all over Lavish as this happens."
                        "And so as soon as her arms and legs give way, Audrey collapses to the floor."
                        "She lies there panting, a heap of sweat-soaked limbs."
                        "Still twitching as Lavish and I look down on her prone form."
                    "Pull out":
                        "I'm so into kissing Lavish that I don't notice what's happening to Audrey."
                        "All it takes is a simple twist of the waist when I'm going backwards."
                        show office threesome audreyfuck lavish outside
                        "And the result is that my cock slides the whole way out of her."
                        $ audrey.love -= 2
                        show office threesome audreyfuck lavish lookback
                        audrey.say "H...hey..."
                        audrey.say "Wh...what happened?!?"
                        audrey.say "You were supposed to cum in me!"
                        show office threesome audreyfuck lavish pleasure cumshot with hpunch
                        "I shoot my load almost the same second that Audrey's finished talking."
                        $ audrey.sub += 2
                        show office threesome audreyfuck lavish outside cum onbody with hpunch
                        "It rains down over her back and buttocks, spattering her sweaty skin."
                        "Audrey yelps and jumps in surprise, looking back over her shoulder."
                        "And I do feel a little guilty as she sees me still kissing Lavish."
                        "But the feeling of release and the sensation of what I'm doing..."
                        "Well, it's just too good for me to even think of stopping for an instant."
                    "Share the love" if "office_cumshare_audrey_lavish" in DONE:
                        call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_1
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            "I want to get this thing started as soon as possible."
            "I'm aware of how wet Audrey looks between her thighs right now."
            "And the fact that Lavish is looking on, waiting to see what I do next."
            "Also, I really can't wait to have my way with Audrey too!"
            "That's why I don't waste any time trying to get creative."
            scene office threesome audreyfuck lavish
            $ audrey.love += 2
            "I just probe for Audrey's pussy and then pull her backwards."
            audrey.say "Whoa..."
            show office threesome audreyfuck lavish lookback
            audrey.say "Steady on there, [hero.name]!"
            audrey.say "We're all gonna get what we want..."
            "Audrey must have been more excited than I thought."
            "Because she offers me no resistance at all."
            "One moment the head of my cock is rubbing against her lips."
            show office threesome audreyfuck lavish pleasure
            "And the next it's slipped inside of her in one smooth motion."
            "All the force that was supposed to get me in there keeps me going."
            "Which means that I don't stop until I'm balls deep in Audrey."
            audrey.say "Oh...shit..."
            audrey.say "Yes...that's it..."
            audrey.say "Fill me up, [hero.name]..."
            audrey.say "All the way!"
            "By now I'm as deep inside of Audrey as I can possibly go."
            "And I'm loving every moment of feeling her around my cock."
            "The fact that she clearly feels the same way is a massive turn-on too."
            "And the way that she's urging me on makes me hold nothing back."
            "Before I know it, I'm pounding away without mercy."
            "Nothing that I see or hear from Audrey stops me either."
            "She takes all that I have to give, soaking it up like a sponge."
            "One moment she's moaning with pleasure."
            "The next she's demanding that I fuck her harder than ever!"
            "In the middle of all this, I forget about everything else."
            "The only thing that seems to exist is Audrey."
            "Well, Audrey and my need to keep on fucking her to the very end!"
            "It's then that I feel the strangest sensation."
            "The feeling of someone touching, softly and gently."
            "I look down to see Lavish has her hands upon my chest."
            "It's such a contrast to the way I'm pounding Audrey."
            "Her touch is so gentle it almost feels unreal."
            "And then she plants her lips over mine..."
            "Lavish kissed me gently and with a subtle passion."
            "Her tongue darts into my mouth as she presses closer."
            "And I can't help leaning into the kiss with passion."
            "Just as much passion as I'm putting into fucking Audrey too."
            "Either one of these things would have been enough to finish me off."
            "But all together I'm lucky to be able to last more than a couple of seconds!"
            "And I just know I'm about to cum!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_lavish" not in DONE:
                call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_2
            else:
                menu:
                    "Cum inside":
                        "Lavish's kiss has me so distracted that I totally forget myself."
                        "That means I keep right on thrusting into Audrey to the very end."
                        $ audrey.love += 4
                        show office threesome audreyfuck lavish ahegao with hpunch
                        "I shoot my load into her without holding a single thing back."
                        show office threesome audreyfuck lavish creampie with hpunch
                        "And she writhes on the end of my cock the whole time."
                        audrey.say "Yeah..."
                        audrey.say "That's what I want!"
                        audrey.say "I want all of it!"
                        "My hands are still all over Lavish as this happens."
                        "And so as soon as her arms and legs give way, Audrey collapses to the floor."
                        "She lies there panting, a heap of sweat-soaked limbs."
                        "Still twitching as Lavish and I look down on her prone form."
                    "Pull out":
                        "I'm so into kissing Lavish that I don't notice what's happening to Audrey."
                        "All it takes is a simple twist of the waist when I'm going backwards."
                        show office threesome audreyfuck lavish outside
                        "And the result is that my cock slides the whole way out of her."
                        $ audrey.love -= 2
                        show office threesome audreyfuck lavish lookback
                        audrey.say "H...hey..."
                        audrey.say "Wh...what happened?!?"
                        audrey.say "You were supposed to cum in me!"
                        show office threesome audreyfuck lavish pleasure cumshot with hpunch
                        "I shoot my load almost the same second that Audrey's finished talking."
                        $ audrey.sub += 2
                        show office threesome audreyfuck lavish outside cum onbody with hpunch
                        "It rains down over her back and buttocks, spattering her sweaty skin."
                        "Audrey yelps and jumps in surprise, looking back over her shoulder."
                        "And I do feel a little guilty as she sees me still kissing Lavish."
                        "But the feeling of release and the sensation of what I'm doing..."
                        "Well, it's just too good for me to even think of stopping for an instant."
                    "Share the love" if "office_cumshare_audrey_lavish" in DONE:
                        call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_3
    $ audrey.sexperience += 1
    return

label office_threesome_lavishfuck_audrey:
    "It'd be the easiest thing in the world to just screw Audrey right now."
    "I can tell just by looking at her that she's almost desperate for it."
    "Lavish, on the other hand, still looks nervous as hell."
    "But maybe this is one of those times when the obvious isn't the way to go?"
    "Maybe what Lavish really needs is to be thrown in at the deep end."
    "With this in mind, I place my hands gently upon her shoulders."
    show lavish surprised
    lavish.say "Wh...what are you doing?!?"
    show audrey frown
    audrey.say "Hey, how come she gets the first ride?"
    "I keep looking Lavish straight in the eyes."
    "And I try to tune Audrey out the best I can too."
    mike.say "It's okay, Lavish."
    mike.say "Just keep looking at me."
    show lavish normal
    "Lavish nods, her eyes wide the whole time."
    "But she doesn't resist as I guide her down onto the floor."
    "And she keeps on looking up at me once she's laid on her back."
    scene office threesome lavishfuck audrey
    show office threesome lavishfuck audrey audahegao lavlookfront
    with fade
    "Still holding her eye, I lower myself over Lavish."
    "She opens her legs to let me come closer still."
    "And she bites her lip as she feels me pressing down on her."
    "All the while, I can hear Audrey muttering to herself in the background."
    "But she does nothing more than sitting down close to Lavish's head."
    "I'm thankful for the fact, as it means that I can devote myself to the task at hand."
    "Lavish is still looking up at me."
    "Her face is a picture of beauty, wide-eyed and completely open."
    "And it's made all the more compelling thanks to her obvious trepidation."
    "She doesn't need to tease me or play hard to get."
    "Just looking into those huge eyes is getting me hard!"
    "But what about where this is going?"
    "I need to decide just what I'm going to do with her..."
    menu:
        "Fuck her ass":
            "Yeah, yeah - I know what you're thinking."
            "I've been going on about how nervous Lavish is right now."
            "How could I even think about taking her up the ass after that - right?"
            "Well maybe that's the best thing for me to do."
            "It breaks her in right where I want her to be."
            "And hopefully it wakes her up to a whole new world of possibilities."
            "With that in mind, I take a deep breath..."
            show office threesome lavishfuck audrey audahegao anal
            $ lavish.sub += 1
            lavish.say "Ooh..."
            lavish.say "[hero.name], what are you..."
            show office threesome lavishfuck audrey audahegao lavlookfront anal
            lavish.say "Where are you going?"
            "There's obvious confusion growing in Lavish's tone."
            show office threesome lavishfuck audrey audhappy lavlookfront anal
            "And Audrey picks up on it instantly."
            "She moves in closer, leaning gently on Lavish's shoulders."
            audrey.say "It's okay, Lavish."
            audrey.say "You're gonna love this - trust me!"
            "I have just enough time to see worry on Lavish's face."
            show office threesome lavishfuck audrey audhappy anal
            "And then I'm pushing my way into her ass."
            "It's every bit as tight and sweet and I thought."
            "Lavish's muscles fight to keep me out."
            "But there's no way I'm holding back now."
            lavish.say "You're...you're in my..."
            lavish.say "My ass...that's my ass!"
            "Audrey leans forwards, keeping Lavish from sitting up."
            "And then I'm deep enough into her that it doesn't matter."
            lavish.say "Oh...my...god..."
            lavish.say "I...I...never thought..."
            lavish.say "Never thought it could feel so good!"
            lavish.say "Please, don't stop!"
            "I do as I'm told, beginning to move faster inside of Lavish."
            "She responds in kind, taking everything that I have to give."
            "Soon lavish begins to throw her head backwards."
            "She writhes on the floor, as if her body is being overloaded."
            "Her moans are getting louder by the second."
            "And I'm actually starting to worry someone might hear her outside of my office!"
            "Audrey seems to sense my concern."
            "Either that or she's tired of being left out of the action."
            show office threesome lavishfuck audrey licking audhappy anal
            "And she wastes no time in straddling Lavish's head."
            "That done, Audrey lowers herself onto the other girl's face."
            "There's nothing that Lavish can do to keep it from happening."
            "Her lips from meeting those of Audrey's pussy."
            "And then she's struggling to push it away with her mouth."
            "I watch in fascination as it slowly transforms into an erotic act."
            "It's like Lavish can't keep her lips from kissing, her tongue from caressing."
            show office threesome lavishfuck audrey licking anal
            "And now it's Audrey's turn to begin moaning as her pussy is licked and explored."
            "Audrey's hands run up and down her own body, squeezing and pinching."
            "But when she begins to massage her breasts..."
            "It's then that I can feel something stirring inside of me!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_lavish" not in DONE:
                call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_4
            else:
                menu:
                    "Cum inside":
                        "I'm hypnotised by the sight of what Audrey's doing."
                        "So much so that I can't even think about pulling out of Lavish."
                        $ lavish.sub += 2
                        show office threesome lavishfuck audrey licking audahegao anal creampie with hpunch
                        "And so I shoot my load inside of her a few moments later."
                        "The effect is instant and dramatic."
                        "Lavish bucks on the end of my cock, shaking and wriggling."
                        "But this also means that she doubles down on Audrey too!"
                        "In the end, all three of us are lost in our orgasms."
                        "We somehow manage to cum all at the same time."
                        "And once it's all over, we collapse as a threesome too!"
                    "Pull out":
                        "Maybe it's because I want to reach out and touch Audrey's breasts for myself."
                        "Or maybe I'm just so entranced that I don't pay enough attention to Lavish."
                        "Whatever the reason, the end result is still the same."
                        scene office threesome lavishfuck audrey
                        show office threesome lavishfuck audrey licking
                        "My cock slides out of Lavish the very second before I cum."
                        show office threesome lavishfuck audrey licking audahegao cumshot with hpunch
                        "This means that I shoot my load straight out in front of me."
                        show office threesome lavishfuck audrey licking dickcum cum onbody with hpunch
                        "Most of it hits Audrey square in the chest."
                        show office threesome lavishfuck audrey dickcum cum onbody
                        "Which means that she can't help rubbing it over her breasts too!"
                        with hpunch
                        "And the rest rains down on Lavish's belly."
                        "She almost jumps out from under Audrey at the sensation, gasping for breath as she does so."
                        "And once it's all over, we all collapse onto the floor."
                        "Each one of us exhausted, panting and bathed in sweat."
                        $ lavish.sub += 1
                    "Share the love" if "office_cumshare_audrey_lavish" in DONE:
                        call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_5
            $ lavish.flags.anal += 1
        "Fuck her pussy":
            "I need to make sure that Lavish enjoys this, that she wants to do it again."
            "And so I don't hesitate to aim straight for her pussy as soon as I have the chance."
            show office threesome lavishfuck audrey audhappy lavlookfront
            "Audrey shuffled closer as I do so, putting her hands on Lavish's shoulders."
            audrey.say "Relax, Lavish."
            audrey.say "You're gonna love it."
            audrey.say "But you already know that, don't you?"
            "I just have enough time to see Lavish's cheeks flush at this."
            show office threesome lavishfuck audrey audhappy vaginal
            $ lavish.love += 2
            "And then, in the moment that she's looking at Audrey, I'm inside of her."
            "Audrey must have been right when she suspected Lavish of being ready for me."
            "Because there's only the smallest token of resistance before she lets me in."
            "All the same, the sensation of it is incredible from the first."
            "Lavish is neat and tight, her pussy squeezing me like a clenched fist."
            "So much so that I almost cum as soon as I'm as deep as I can go!"
            lavish.say "Mmm..."
            lavish.say "Oh, [hero.name]..."
            lavish.say "She's right - I love it!"
            "Trying with all my might to hold it in, I start moving inside of Lavish."
            "Every time I go back and forth, it feels better and better."
            "And she moves beneath me like she's feeling the same thing too."
            "Lavish gasps and moans the whole time."
            "Those eyes are looking up at me, wider than ever."
            "But now they seem to be asking me for more."
            "They seem to be asking me to fuck her ever harder!"
            "I do as I'm told, beginning to move faster inside of Lavish."
            "She responds in kind, taking everything that I have to give."
            "Soon lavish begins to throw her head backwards."
            "She writhes on the floor, as if her body is being overloaded."
            "Her moans are getting louder by the second."
            "And I'm actually starting to worry someone might hear her outside of my office!"
            "Audrey seems to sense my concern."
            "Either that or she's tired of being left out of the action."
            show office threesome lavishfuck audrey licking audhappy vaginal
            "And she wastes no time in straddling Lavish's head."
            "That done, Audrey lowers herself onto the other girl's face."
            "There's nothing that Lavish can do to keep it from happening."
            "Her lips from meeting those of Audrey's pussy."
            "And then she's struggling to push it away with her mouth."
            "I watch in fascination as it slowly transforms into an erotic act."
            "It's like Lavish can't keep her lips from kissing, her tongue from caressing."
            show office threesome lavishfuck audrey licking vaginal
            "And now it's Audrey's turn to begin moaning as her pussy is licked and explored."
            "Audrey's hands run up and down her own body, squeezing and pinching."
            "But when she begins to massage her breasts..."
            "It's then that I can feel something stirring inside of me!"
            if hero.sexperience >= 25 and "office_cumshare_audrey_lavish" not in DONE:
                call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_6
            else:
                menu:
                    "Cum inside":
                        "I'm hypnotised by the sight of what Audrey's doing."
                        "So much so that I can't even think about pulling out of Lavish."
                        $ lavish.love += 4
                        show office threesome lavishfuck audrey licking audahegao vaginal creampie with hpunch
                        "And so I shoot my load inside of her a few moments later."
                        "The effect is instant and dramatic."
                        "Lavish bucks on the end of my cock, shaking and wriggling."
                        "But this also means that she doubles down on Audrey too!"
                        "In the end, all three of us are lost in our orgasms."
                        "We somehow manage to cum all at the same time."
                        "And once it's all over, we collapse as a threesome too!"
                    "Pull out":
                        "Maybe it's because I want to reach out and touch Audrey's breasts for myself."
                        "Or maybe I'm just so entranced that I don't pay enough attention to Lavish."
                        "Whatever the reason, the end result is still the same."
                        scene office threesome lavishfuck audrey
                        show office threesome lavishfuck audrey licking
                        "My cock slides out of Lavish the very second before I cum."
                        show office threesome lavishfuck audrey licking audahegao cumshot with hpunch
                        "This means that I shoot my load straight out in front of me."
                        show office threesome lavishfuck audrey licking dickcum cum onbody with hpunch
                        "Most of it hits Audrey square in the chest."
                        show office threesome lavishfuck audrey dickcum cum onbody
                        "Which means that she can't help rubbing it over her breasts too!"
                        with hpunch
                        "And the rest rains down on Lavish's belly."
                        "She almost jumps out from under Audrey at the sensation, gasping for breath as she does so."
                        "And once it's all over, we all collapse onto the floor."
                        "Each one of us exhausted, panting and bathed in sweat."
                        $ lavish.sub += 1
                    "Share the love" if "office_cumshare_audrey_lavish" in DONE:
                        call office_cumshare_audrey_lavish from _call_office_cumshare_audrey_lavish_7
    $ lavish.sexperience += 1
    return

label office_cumshare_audrey_lavish:
    "I'm all ready to shoot my load, and thinking of nothing else at all."
    "But then I look down and see that somebody has other ideas."
    "Before I can even open my mouth to object, Audrey's already taken charge."
    scene office cumshare audrey lavish with fade
    "She hurries Lavish along, making her kneel in front of me."
    "And then Audrey joins her, sitting there and waiting for the moment I cum!"
    show office cumshare audrey lavish cumshot with hpunch
    "When it happens, they're both so close that it hits them straight in the face."
    with hpunch
    "Lavish yelps and waves her hands in alarm."
    show office cumshare audrey lavish dickcum cum onfaces
    "But she's too late to keep it from striping her nose and cheeks."
    "Audrey makes no such efforts, instead opening her mouth wide."
    "The cum hits her in the same places, but also lands in her mouth too."
    show office cumshare audrey lavish dickcum cum onfaces cum share
    "And then she surprised Lavish by taking hold of her cheeks and kissing her."
    "It all happens too fast for the other girl to resist."
    "Meaning that I'm treated to the sight of them licking and lapping at each other."
    "And the whole time they're doing it, cum is strung between their lips and tongues."
    $ audrey.love += 4
    $ lavish.love += 4
    $ DONE["office_cumshare_audrey_lavish"] = game.days_played
    return

label office_lavish_shiori_01:
    "It still feels weird to be the guy sitting in the big chair, the one behind the CEO's desk."
    "And for a while now I've kind of been just going through the motions without thinking about it."
    "I'm acting like someone's going to walk into my office and tell me it's all been a big joke."
    "But it's been days since I was put in charge of the company, and I'm still here."
    "So maybe it's time I started acting like I really believe that I'm the guy in charge?"
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "With that in mind, I lean over and pick up the phone on my desk."
    lavish.say "Lavish speaking - what's the nature of the call?"
    mike.say "Ah, hey, Lavish?"
    lavish.say "Yes, Mister [hero.family_name]?"
    "On the other end of the line, Lavish sounds alert and efficient as ever."
    "I can almost imagine her sitting up to attention at her desk as she speaks."
    mike.say "Would you mind coming up here for a moment?"
    mike.say "I have something I need to discuss with you."
    lavish.say "Of course - I'll be there ASAP."
    "I hear Lavish put the phone down, but I don't do the same on my end."
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "Instead I end the call and quickly dial another extension on the same floor."
    shiori.say "Erm...hello..."
    shiori.say "Shiori here..."
    "In contrast to Lavish, Shiori sounds meek and nervous."
    "But that just serves to make me smile."
    "I adore her innocence and shyness as much as I do Lavish's poise and confidence."
    mike.say "Shiori, could I see you in my office?"
    shiori.say "Ah...I..."
    shiori.say "Am I...in trouble?"
    mike.say "No, Shiori, you're not in trouble!"
    mike.say "I just need to see you about a little something, okay?"
    shiori.say "Oh...okay!"
    shiori.say "I'm coming!"
    "This time I put down the receiver as soon as Shiori does the same."
    "I can't help shaking my head and chuckling."
    "The pair of them are so different it's almost unreal."
    "But there's no time to do anymore."
    play sound door_knock
    "As a moment later, I hear a knock on my office door."
    mike.say "Come in!"
    show lavish work at left
    show shiori work at top_mostleft
    with easeinleft
    "At the sound of my voice, Lavish and Shiori let themselves in."
    "They both have a look of confusion on their faces as they enter the office."
    "No doubt they're each wondering what the other is doing here."
    mike.say "Hey, guys - get over here."
    mike.say "And close the door behind you too!"
    show lavish work at center
    show shiori work at left
    with ease
    "Shiori attends to the door while Lavish hurries over."
    show lavish work at right5
    show shiori work at left5
    with ease
    "A moment later, Shiori joins her in front of my desk."
    "I can see that they want to ask why they're both here."
    "But neither of them is going to be the first to speak."
    "Not now that I'm the big boss."
    "Ah...it's good to be king!"
    mike.say "Glad you two could join me."
    mike.say "Because I've been looking back over my diary."
    mike.say "And it seems to me that we've not had the chance to work together much."
    mike.say "Sure, we've been in the same building and attended the same meetings."
    mike.say "But we've never had the time to work closely together, just the three of us."
    "I raise my eyebrows as I say this, trying to make my intentions plain."
    show lavish surprised
    "Lavish seems to grasp the undertone of my words almost immediately."
    "I can see that she's more than a little surprised."
    show lavish normal blush
    "But she quickly shakes it off and nods eagerly."
    "Shiori is another matter entirely."
    "She nods as well, but I can see that she's not getting it."
    shiori.say "Wh...what are we going to be working on, [hero.name]?"
    show lavish annoyed blush at center with ease
    "Lavish leans in close to Shiori, nudging her in the ribs."
    show lavish flirt
    lavish.say "Team-building, Shiori."
    lavish.say "Like right here and now - across the desk!"
    show shiori surprised blush at startle
    "I see Shiori's eyes go wide and her mouth drop open in surprise."
    "Her cheeks flush red and she looks for Lavish to me and back again."
    shiori.say "Oh..."
    shiori.say "Oh my!"
    "But for all of her embarrassment, I see Shiori nod too."
    show lavish normal blush naked zorder 2 at center, zoomAt(1.25, (840, 900))
    show shiori normal naked zorder 1 at center, zoomAt(1.25, (440, 900))
    with fade
    "So it looks like we're all on-board for the team-building exercise."
    "The only question now is which one of them?"
    "Who gets to take delivery of my motivational material?"
    call office_lavish_shiori_fuck from _call_office_lavish_shiori_fuck
    return

label office_lavish_shiori_fuck:
    menu:
        "Fuck Lavish":
            call office_threesome_lavishfuck_shiori from _call_office_threesome_lavishfuck_shiori
        "Fuck Shiori":
            call office_threesome_shiorifuck_lavish from _call_office_threesome_shiorifuck_lavish
    $ game.pass_time(2)
    $ hero.cancel_activity()
    return

label office_threesome_lavishfuck_shiori:
    "Maybe what Shiori needs is for someone else to take the lead?"
    "And it's with that thought in mind I reach out and grab Lavish's hand."
    "She nods eagerly and allows me to lead her over to the couch."
    "Once there, I lay myself down and beckon for her to follow."
    show lavish normal blush naked at center, zoomAt(1.75, (840, 1140)) with dissolve
    "Lavish doesn't need to be told twice, and is soon straddling my waist."
    "For a moment I'm only able to stare up at the sight of her breasts above me."
    "But then I shake my head and glance over to look for Shiori."
    "She's standing a few feet away from the couch, looking lost."
    "I see her glance at Lavish and myself, then look away."
    lavish.say "Come on, Shiori - get over here!"
    mike.say "Yeah, Shiori - I didn't ask you up here just to watch!"
    show shiori surprised blush naked at startle
    "Shiori almost jumps at the sound of us calling her over."
    show shiori normal
    "But then she visibly steels herself and nods."
    shiori.say "O...okay..."
    shiori.say "I'm coming!"
    "Lavish turns so that she has her back to me."
    "And as soon as she's done moving, she takes hold of my cock."
    hide shiori
    hide lavish
    show office threesome lavishfuck shiori normal outside
    with fade
    "Needless to say I'm already more than a little excited right now."
    "So there's not much that she needs to do in the way of getting me hard!"
    "Instead she starts to stroke it gently with one hand."
    "And at the same time she rubs the lips of her pussy against it too."
    lavish.say "Mmm..."
    lavish.say "This thing feels good..."
    lavish.say "But I bet it'll feel SO much better inside of me!"
    "All I can do is gasp at the sensations I'm feeling."
    "That and nod desperately in agreement."
    menu:
        "Fuck her pussy":
            "I'm pretty sure that Lavish and I are on the exact same wavelength."
            "And so I don't even try to tell her what I want to happen next."
            "Instead I just lay back and let her take over, trusting that I'm right."
            $ lavish.love += 2
            show office threesome lavishfuck shiori -outside -normal vaginal pleasure
            "And when I feel her pushing down on my cock, that trust pays off big time."
            "Lavish's pussy is already nice and slick, all ready for me."
            "Which means that there's only a few seconds of resistance."
            lavish.say "Ah..."
            lavish.say "Oh yeah..."
            "With that, her lips part and she slides down onto me."
            "Gravity does most of the work, pulling her weight downwards."
            "All I have to do is lay there and let it happen."
            "Lavish moans and sighs as my cock is pushed inside of her."
            show office threesome lavishfuck shiori -pleasure normal
            "She slowly turns her head to look back over her shoulder."
            "And that's when Shiori leans in to plant a kiss on her lips."
            "I see Lavish's eyes go wide with surprise."
            "But if anything, Shiori seems more surprised by her own actions."
            "For a moment the normally shy and retiring girl looks like she regrets the move."
            show office threesome lavishfuck shiori saliva
            "Which is when Lavish returns the kiss with renewed intensity."
            "I can only watch as these two hot girls come closer together."
            "That is until Shiori is forced to straddle me too."
            "She plants her knees to either side of my head."
            "And that means she's laid wide open!"
            show office threesome lavishfuck shiori pleasure
            "Putting a firm hand on each of her thighs, I pull Shiori down."
            "She makes a muffled squealing sound as I begin to lick around her lips."
            "But Lavish doesn't seem to want to let her go just yet."
            "And so Shiori remains trapped as I explore her pussy with my tongue."
            "At the same time, Lavish is wriggling and writhing on my cock."
            "The more I probe Shiori, the more she pouts from the sensation."
            "And the more she pouts, the more Lavish seems to get off on it all."
            "Pretty soon the three of us are caught in a perfect loop."
            "Whatever one of us does, it pushes the other two further."
            "And they in turn redouble their efforts again."
            "But even so, there's no way this can go on forever."
            "And soon enough, I can feel myself about to cum..."
            if hero.sexperience >= 25 and "office_cumshare_lavish_shiori" not in DONE:
                call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori
            else:
                menu:
                    "Cum inside":
                        "It's not like I have much choice in the matter."
                        "Lavish is straddling my middle right now."
                        "And Shiori's pretty much sitting on my face too!"
                        show office threesome lavishfuck shiori creampie with vpunch
                        "So when I lose it, I do so deep inside of Lavish."
                        $ lavish.love += 4
                        show office threesome lavishfuck shiori -pleasure ahegao with vpunch
                        "She breaks the kiss to cry out as I push up from below."
                        "At the same time my tongue goes deeper than ever before into Shiori."
                        "Now it sounds like the both of them are cumming at once!"
                        "And all I can do is ride it out to the end."
                        "Well, that and try to keep from being suffocated by Shiori's ass!"
                    "Pull out":
                        "I literally have two girls sitting on top of me right now."
                        "So I have to use all of my remaining strength to make it happen."
                        show office threesome lavishfuck shiori -vaginal outside -pleasure ahegao
                        "But somehow I manage to wriggle my cock out of Lavish in time."
                        show office threesome lavishfuck shiori cumshot with vpunch
                        "She breaks off the kiss with Shiori to cry out at the sensation."
                        show office threesome lavishfuck shiori -cumshot dickcum with vpunch
                        "Which means that Shiori literally sits on my face a second later!"
                        "All of this means that I hear, rather than see what happens next."
                        "It's only when I finally manage to tumble Shiori off me that I can see again."
                        "And I'm treated to the image of Lavish, red-faced and panting."
                        "She stares back at me as every drop of my cum drips from her breasts and belly."
                    "Share the love" if "office_cumshare_lavish_shiori" in DONE:
                        call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_1
        "Fuck her ass":
            "Sure, I might be agreeing with Lavish."
            "But that doesn't mean that we want exactly the same thing."
            "Which is why I reach out and take a firm hold of her a moment later."
            lavish.say "Ah..."
            lavish.say "What's up..."
            lavish.say "What are you..."
            "I smile as Lavish glances back over her shoulder at me."
            "A little because of the look on her face."
            "And perhaps more so because I feel my cock slide between her buttocks."
            mike.say "Don't worry, Lavish."
            mike.say "Just a slight change of plan!"
            show office threesome lavishfuck shiori -outside
            "With that, I pull her down and onto my cock."
            "Instantly she stiffens and I feel her muscles resist."
            lavish.say "Oh shit..."
            lavish.say "Are you really..."
            lavish.say "I...I guess you are!"
            "Lavish pants as gravity begins to do the work for me."
            "The muscles of her ass hold out at first, quaking and twitching."
            $ lavish.sub += 1
            show office threesome lavishfuck shiori -normal pleasure
            "Then I feel them surrender, and the expression on her face change too."
            "Lavish closes her eyes, nodding almost frantically."
            "And that lets me know that she's resigned to letting me have my way."
            "I can't help smiling as I feel Lavish begin to ride my cock."
            "But then my mouth drops open as Shiori leans in to kiss her lips."
            show office threesome lavishfuck shiori -pleasure normal
            "Lavish's eyes open instantly, her face a picture of surprise."
            "And Shiori too looks just as amazed at what she's doing."
            "I almost think that she's going to pull back and run."
            show office threesome lavishfuck shiori saliva
            "Until Lavish returns the gesture hungrily."
            "I find myself watching as they come closer together."
            "Shiori clambers over me until she's straddling my chest."
            "She puts a knee down on either side of my head."
            "And it's then that I realise her pussy is inches from my face!"
            "I don't hesitate to grab hold of her thighs and pull her downwards."
            show office threesome lavishfuck shiori -normal pleasure
            "Shiori lets out a muffled yelp as I begin to lick around the edges."
            "But she doesn't move an inch, as Lavish keeps on kissing her."
            "Instead she stays rooted to the spot, quivering the whole time."
            "For her part, I can still feel Lavish riding my cock."
            "And that makes me push further into Shiori's pussy."
            "She in turn pouts and pants, the sound exciting Lavish."
            "It's like each one of us is driving the others ever harder."
            "Like we're caught in some kind of passionate loop."
            "Everything we do just makes it all the more intense."
            "Part of me wishes that this could go on forever."
            "But I'm only human, and I know I'm about to lose it..."
            if hero.sexperience >= 25 and "office_cumshare_lavish_shiori" not in DONE:
                call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_2
            else:
                menu:
                    "Cum inside":
                        "There's not much room to choose what happens next."
                        "Lavish is pinning down my middle with all her weight."
                        "On top of that, Shiori's sitting on my face!"
                        show office threesome lavishfuck shiori creampie with vpunch
                        "So when I lose it, I shoot my load inside of Lavish's ass."
                        $ lavish.sub += 2
                        show office threesome lavishfuck shiori -pleasure ahegao with vpunch
                        "And my pushing upwards is finally enough to break the kiss."
                        "Holding my breath, I push my tongue even deeper into Shiori."
                        "It sounds like the pair of them are cumming at the same time."
                        "But all I can do is hang on until the end."
                        "Hang on and do my best not to get smothered by Shiori's butt!"
                    "Pull out":
                        "Lavish and Shiori are literally sitting on me right now."
                        "And so it takes all of the strength I have left to pull out."
                        "I must have no more than a second once it's out of Lavish."
                        show office threesome lavishfuck shiori outside -pleasure ahegao
                        "And I know that I've done it when I hear her wail at the sensation."
                        show office threesome lavishfuck shiori cumshot with vpunch
                        "Lavish breaks the kiss, and in doing so pushes Shiori backwards."
                        show office threesome lavishfuck shiori -cumshot dickcum with vpunch
                        "And her ample buttocks smother my face."
                        "Struggling for breath, I send Shiori tumbling off of me."
                        "And only then do I see the image of Lavish, flushed and panting."
                        "Every drop of cum that I let go dripping off of her pert breasts and flat belly."
                    "Share the love" if "office_cumshare_lavish_shiori" in DONE:
                        call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_3
            $ lavish.flags.anal += 1
    $ lavish.sexperience += 1
    return

label office_threesome_shiorifuck_lavish:
    "As good as Lavish looks right now, my eye keeps on getting drawn towards Shiori."
    "She's demure and even a little submissive, where Lavish is self-assured and confident."
    "I keep telling myself that it's not her meekness that makes me want Shiori so much."
    "No, it's the fact that she just makes me want to take care of her, to protect her."
    "Well...that and to fuck her until she begs for mercy!"
    show shiori normal blush naked zorder 3 at center, zoomAt(1.75, (440, 1140)) with dissolve
    "That's why I make straight for her as soon as we're all undressed."
    show shiori surprised blush
    "Shiori looks instantly surprised and unsure of herself."
    show lavish flirt blush naked at center, zoomAt(1.75, (840, 1140)) with dissolve
    "But Lavish seems to pick up on the situation almost instantly."
    "And rather than protesting, she does all she can to make things go as I'd planned."
    "I watch as Lavish takes Shiori by the hand, laying herself down on the floor before me."
    "Shiori allows herself to be led, lowering herself onto the floor beside Lavish."
    "It's only now that I step in and take over, guiding Shiori into position."
    hide shiori
    hide lavish
    show office threesome shiorifuck lavish blush
    with fade
    "I'm standing at Lavish's head, looking down over her."
    "And I keep Shiori moving until has her back to me, straddling the other girl's chest."
    "Shiori divides her attention between Lavish and I."
    "One moment staring back over her shoulder at me."
    "And the next gazing down at Lavish."
    "I nod and smile, trying to reassure and encourage her."
    "But I can already see the look of anticipation spreading across Lavish's face below."
    show office threesome shiorifuck lavish -lookback pleasure
    "Almost as soon as Shiori is in place, Lavish sticks out her tongue."
    "It darts between the other girl's thighs, licking at her exposed lips."
    shiori.say "Ah...ah..."
    shiori.say "Oh...Oh, Lavish!"
    shiori.say "What are you doing to me?!?"
    "I hear Lavish let out a wicked chuckle as she stops licking."
    "After all, she can't use her tongue for two things at once!"
    lavish.say "What do you think I'm doing, Shiori?"
    lavish.say "I'm licking your pussy!"
    lavish.say "Which, by the way, tastes very nice."
    show office threesome shiorifuck lavish -pleasure lookback
    "Shiori looks back over her shoulder at me."
    "She has a look of helplessness on her face."
    "And that only serves to make me want her all the more!"
    "Lavish is right - Shiori's pussy sounds irresistible."
    "But then a thought occurs to me."
    "What if I were to go for Shiori's ass instead?"
    "It's every bit as enticing as her pussy."
    "And that would mean Lavish could keep right on using her tongue too."
    "Ah, decisions, decisions!"
    "I guess that's just something that comes along with being the boss."
    menu:
        "Fuck her pussy":
            "But then one of the perks of being the boss is getting your own way."
            "Lavish is just going to have to find another way of entertaining herself."
            "Because I want Shiori's pussy all to myself."
            "And what the big boss wants, he gets!"
            "Without warning, I take a firm hold of Shiori."
            $ shiori.love += 2
            show office threesome shiorifuck lavish -lookback pleasure -outside vaginal
            "My hands on her haunches, I push my cock between her thighs."
            shiori.say "Ooh..."
            shiori.say "Oh, [hero.name]!"
            shiori.say "It's so big..."
            show office threesome shiorifuck lavish -pleasure lookback
            shiori.say "I'm scared...but I want you in me so badly!"
            "I don't know if Shiori's genuinely scared right now."
            "Or else she's putting on an act that she knows I'll like."
            "But either way I can't hope to form a single word in response."
            "All I can do is thrust my cock against her pussy."
            show office threesome shiorifuck lavish -lookback pleasure
            "I'm pushing as hard as I can, becoming desperate to have her."
            "Shiori moans and squeals as I feel myself sink into her."
            "There's just enough resistance to make it that much more intense."
            "And then her body surrenders to me, and I'm inside."
            "I push all the way into her, as deep as I can possibly go."
            shiori.say "Mmm..."
            shiori.say "I'm so full..."
            shiori.say "[hero.name], please..."
            shiori.say "Fuck me!"
            "It's not like I need Shiori to ask!"
            "The moment that she's finished speaking, I leap into action."
            "There's no starting slow and building up speed."
            "Instead I begin to pound Shiori without mercy."
            "She wails and cries out, giving voice to what she's taking."
            "And the only thing louder is the sound of skin slapping against skin."
            "My groin hammers against Shiori's ample buttocks and thighs."
            "Which absorb each and every impact, wobbling and rippling the whole time."
            "Suddenly I feel an intense sensation, like someone's squeezing my balls."
            "All it takes is a glance downwards to see that I'm half right."
            "Lavish has a hold of me alright, but she's not squeezing them."
            "Instead she has one of them in her mouth, sucking and caressing it."
            "I was already panting from the effort of fucking Shiori so hard."
            "But now I can hear myself starting to gasp as Lavish goes to work on me too."
            "And what she's doing has an almost immediate effect, like she pushed a button."
            "I know that it's only going to be a moment before I cum!"
            if hero.sexperience >= 25 and "office_cumshare_lavish_shiori" not in DONE:
                call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_4
            else:
                menu:
                    "Cum inside":
                        "There's nothing I can do to keep it from happening."
                        "And so I don't even try, I just surrender to it."
                        $ shiori.love += 4
                        show office threesome shiorifuck lavish -pleasure ahegao creampie with hpunch
                        "With one final thrust, I shoot my load into Shiori."
                        with hpunch
                        "She moans and whimpers as she takes it."
                        "And I can feel her cum too as she quivers on the end of my cock."
                    "Pull out":
                        "All I can do is use the last of my energy to pull out before I lose it."
                        show office threesome shiorifuck lavish -pleasure ahegao -vaginal outside
                        "Shiori moans as the length of my cock is dragged out of her pussy."
                        show office threesome shiorifuck lavish cumshot with hpunch
                        "And then she yelps in surprise as I shoot my load over her."
                        show office threesome shiorifuck lavish -cumshot dickcum with hpunch
                        "Cum spatters over her buttocks and back, some missing her entirely."
                        "That which does rains down on Lavish's face below."
                        "And she licks her lips, catching every drop that she can."
                    "Share the love" if "office_cumshare_lavish_shiori" in DONE:
                        call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_5
        "Fuck her ass" if shiori.flags.anal:
            "This is supposed to be a team-building exercise."
            "So I guess I should do all I can to get Lavish involved too."
            "After all, a good boss knows to motivate his employees!"
            "Without warning, I take a firm hold of Shiori."
            $ shiori.sub += 1
            show office threesome shiorifuck lavish -lookback pleasure -outside anal
            "My hands on her haunches, I push my cock between her buttocks."
            shiori.say "Ooh..."
            shiori.say "Oh, [hero.name]!"
            shiori.say "It's so big..."
            show office threesome shiorifuck lavish -pleasure lookback
            shiori.say "I'm scared...but I want you in me so badly!"
            "I want the same thing, but not in the way that Shiori's thinking!"
            "All it takes is one firm push to plant the head."
            "I feel the resistance of Shiori's ass."
            "But that just makes me want to get in there all the more."
            shiori.say "Oh...oh my..."
            shiori.say "[hero.name]..."
            shiori.say "You're in my...my butt!"
            "I don't stop for an instant."
            "I just keep on pushing for all I'm worth."
            "Shiori's ass is so tight, it feels amazing."
            "And her buttocks are so soft too!"
            "A moment later, I feel her muscles surrender."
            show office threesome shiorifuck lavish -lookback pleasure
            shiori.say "Mmm..."
            shiori.say "That feels good..."
            shiori.say "Please, [hero.name]..."
            shiori.say "Please fuck my ass!"
            "It's not like I need Shiori to ask!"
            "The moment that she's finished speaking, I leap into action."
            "I hit the ground running, beginning to pound her a moment later."
            "The second I do so, Shiori begins to moan and wail."
            "That sound pushes me even further, turning me on every time I hear it."
            "It's the sound of Shiori giving in to me completely."
            "The sound of her surrendering to what I'm doing to her body."
            "At the same time, lavish begins to lick at her pussy again."
            "This means that Shiori is trapped between the two of us."
            "Every movement that she makes away from one is towards the other."
            "And so she soon finds herself stuck in a state of limbo."
            "As I thrust into her from behind, she's pushed forwards."
            "This means her pussy is thrust into Lavish's face."
            "Of course, the other girl takes the opportunity to probe with her tongue."
            "The sensation of this makes Shiori pull backwards."
            "And this forces my cock deeper into her still."
            "Soon she's overwhelmed, trembling as she cums."
            "There's nothing I can do to hold on when this happens."
            "And I can feel myself cumming too!"
            if hero.sexperience >= 25 and "office_cumshare_lavish_shiori" not in DONE:
                call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_6
            else:
                menu:
                    "Cum inside":
                        "There's no way that I can hang on even for another second."
                        "And so I just accept the inevitable and keep on going."
                        $ shiori.sub += 2
                        show office threesome shiorifuck lavish creampie with hpunch
                        "I make one that thrust and shoot my load into Shiori's ass."
                        show office threesome shiorifuck lavish -pleasure ahegao with hpunch
                        "Her muscles quiver and she lets out a new round of moans."
                        "She seems to cum again as it happens too."
                        "Pushing her pussy into Lavish below."
                    "Pull out":
                        show office threesome shiorifuck lavish -anal outside
                        "I use the last of my strength to yank my cock out of Shiori's ass."
                        show office threesome shiorifuck lavish -pleasure ahegao
                        "She moans at the sensation of it popping out of her too."
                        show office threesome shiorifuck lavish cumshot with hpunch
                        "But then she cries out in surprise as I shoot my load over her."
                        show office threesome shiorifuck lavish -cumshot dickcum with hpunch
                        "Cum spatters over her buttocks and back, some missing her entirely."
                        "That which does rains down on Lavish's face below."
                        "And she licks her lips, catching every drop that she can."
                    "Share the love" if "office_cumshare_lavish_shiori" in DONE:
                        call office_cumshare_lavish_shiori from _call_office_cumshare_lavish_shiori_7
            $ shiori.flags.anal += 1
    $ shiori.sexperience += 1
    return

label office_cumshare_lavish_shiori:
    "Before I can shoot my load, I somehow manage to wriggle out from under Lavish and Shiori."
    show office cumshare lavish shiori
    "I kneel on the sofa, with the pair of them staring up at me with wide, eager eyes."
    "Of course, it's Lavish that takes the hint first, sitting up and paying attention."
    "A moment later she begins to kiss and lick the head of my cock with enthusiasm."
    "Shiori is slower to act, but soon rushes to copy Lavish as well."
    "For the last few moments before I cum, they work away at my cock."
    "But even so, I can't hold on any longer, and I cum without warning."
    if lavish.sub >= 40:
        $ lavish.love += 4
        show office cumshare lavish shiori lavishbj blowjob cum lavsuck with hpunch
        $ hero.energy -= 1
        "Quick as a flash, Lavish is there to catch the cum as it shoots forth."
        with hpunch
        "She laps away hungrily, letting more than a single drop escape her lips."
        "I watch her with wide eyes as she seems to be savouring the taste of it too!"
        if shiori.sub >= 40:
            show office cumshare lavish shiori lavishbj blowjob cum lavsuck saliva
            "It's about then that I realise Shiori is waiting by her side."
            show office cumshare lavish shiori -lavishbj -blowjob dickcum lavnormal share
            "And she looks like she wants to claim a portion for herself..."
            if hero.energy > 0:
                "Luckily for Shiori, I'm nowhere near spent yet."
                $ shiori.love += 4
                show office cumshare lavish shiori -dickcum shioribj blowjob cum shisuck share saliva
                $ hero.energy -= 1
                "As soon as Lavish moves aside, she gets her share of the action."
                "Sure, it might not be as much as Lavish got beforehand."
                show office cumshare lavish shiori shioribj blowjob cum shisuck share dripping
                "But Shiori looks just as pleased to be getting it, maybe even more so!"
                "And like Lavish, she swallows as much as she can."
                if hero.energy > 0:
                    "So turned on to see both of them hungrily drinking my cum, I found myself getting even harder even though I came a few seconds ago."
                    show office cumshare lavish shiori -shioribj -blowjob dickcum shinormal cum share dripping
                    "I pull my cock out from Shiori's mouth to let my cum drip on them."
                    show office cumshare lavish shiori outside cumshot dickcum lavsuck shisuck cum share dripping
                    "Streamers of hot, sticky cum shoot out, hitting them both in the face."
                    $ lavish.sub += 2
                    $ shiori.sub += 2
                    show office cumshare lavish shiori -cumshot dickcum lavsuck shisuck cum share dripping onbody
                    "Lavish and Shiori both yelp in surprise as it spatters across their cheeks."
                    show office cumshare lavish shiori dickcum cum share dripping lavnormal shinormal onbody
                    "And then they gaze up at me as it begins to run down to their chins."
            else:
                "But it looks like Shiori's out of luck this time."
                "There's just nothing left by the time Lavish moves aside."
                "Shiori looks up at me with an expectant expression on her face."
                "And all I can do is shrug and shake my head."
                "Sure, she offers me a meek little smile."
                "But I can see that she's pretty disappointed at being left out."
                $ shiori.love -= 4
    else:
        show office cumshare lavish shiori cumshot lavsuck shisuck with hpunch
        "Streamers of hot, sticky cum shoot out, hitting them both in the face."
        $ lavish.love += 4
        $ shiori.love += 4
        show office cumshare lavish shiori -cumshot dickcum cum onbody with hpunch
        "Lavish and Shiori both yelp in surprise as it spatters across their cheeks."
        show office cumshare lavish shiori lavnormal shinormal
        "And then they gaze up at me as it begins to run down to their chins."
    $ DONE["office_cumshare_lavish_shiori"] = game.days_played
    return

label office_audrey_lavish_shiori_showdown:
    scene bg beach
    "There was a time when I couldn't have imagined taking a day out to hit the beach with Audrey."
    "I mean, she can be such an annoying bitch around the office without even putting in that much effort!"
    "The last thing I ever wanted to do when she was winding me up was spend time with her out of work."
    "But I guess that was just because I'd never really gotten to know her out of that one setting."
    "Nobody's the same person all the time or in every place they spend some of that time."
    show audrey swimsuit happy with dissolve
    "Take right now for example - Audrey's all sweetness and light as we spread out our things."
    "She seems genuinely happy to be here with me."
    "It's almost like the Audrey I remember from the office is an entirely different person!"
    show audrey normal
    audrey.say "Hurry up, [hero.name]!"
    audrey.say "What's taking you so long?"
    mike.say "Whoa, Audrey - settle down there!"
    mike.say "What's the big rush anyway?"
    "I stop what I'm doing for a moment and survey the beach around us."
    "The spot we've chosen is a good distance from the nearest person that's also on the sand."
    "And on top of that, we seem to have chosen a day when almost nobody else thought to come here."
    show audrey happy
    audrey.say "Ah...nothing, [hero.name], nothing..."
    audrey.say "I'm just excited, that's all!"
    show audrey at left with ease
    audrey.say "I can't wait to get into the water."
    "I can't help narrowing my eyes at this, suspicious of Audrey's explanation."
    "But then I can understand that she might be a little nervous underneath it all."
    "Getting to know someone outside of work can be daunting."
    "So maybe I'm being a little hard on her."
    mike.say "Okay, Audrey."
    mike.say "I'll speed things up a little."
    "I busy myself with the last few tasks that need to be completed."
    "Which means that I have my head down for the best part of the next few minutes."
    "But when I finally look up again, I'm surprised to discover we have company."
    show lavish swimsuit happy at right5 with moveinright
    lavish.say "Looks like you guys beat us to it!"
    show shiori swimsuit happy at top_mostright with moveinright
    shiori.say "Oh...I hope we're not too late?"
    shiori.say "We came as soon as I'd dropped Kanta off at school!"
    "Lavish and Shiori stand there in front of me, all smiles."
    "I can tell that they're waiting for me to say something."
    "But I'm so taken aback to see them there that I just stare at them in silence."
    show lavish annoyed
    lavish.say "Erm, Audrey..."
    lavish.say "Why is he looking at us like that?"
    show shiori surprised
    shiori.say "Is poor [hero.name] okay?"
    shiori.say "He hasn't got sunstroke, has he?"
    show audrey joke at left4 with ease
    "Audrey steps between the other two girls and me."
    "She's shaking her head, dismissing their concerns."
    "And I note that she doesn't look surprised to see them in the slightest."
    audrey.say "Nah...no way!"
    audrey.say "Of course he's glad to see you."
    audrey.say "He's just dumbstruck at how good you all look in your swimsuits - that's all!"
    show lavish normal
    "Lavish nods at this."
    "Though she looks less than convinced by Audrey's hasty explanation."
    show shiori happy
    "But Shiori grins at the implied compliment."
    "She clasps her hands together over her considerable cleavage."
    shiori.say "You really like it, [hero.name]?"
    shiori.say "You don't think it's too much?"
    mike.say "Ah...no, Shiori."
    mike.say "It's very flattering on you..."
    mike.say "Audrey, could I have a word with you?"
    show audrey zorder 66 at center, zoomAt(1.85, (440, 1200))
    "Lavish and Shiori begin dropping their things with ours."
    "And while they're distracted, I lean in and whisper to Audrey."
    mike.say "Do you know why this is turning into an office outing?"
    mike.say "Because they seem to think that there was an open invitation!"
    "Audrey shakes her head."
    "And she has the worst impression of innocence I've ever seen on her face as she does so."
    show audrey annoyed
    audrey.say "I thought that I'd invite them along, [hero.name]."
    audrey.say "I told them that it'd be a great chance for some bonding."
    audrey.say "A chance for the four of us to get a little more intimate."
    "Though I was whispering just now, Audrey speaks out loud."
    show lavish annoyed
    show shiori annoyed
    "Which means that Lavish and Shiori can hear every word she says."
    "I can see from the looks on their faces that they're listening in."
    "And they've both picked up words like 'intimate' and 'bonding' too."
    "Right now both of them are probably worried."
    "Worried that our dirty little secrets are under threat of being revealed!"
    show lavish angry
    lavish.say "What does she mean, [hero.name]?"
    show shiori angry
    shiori.say "Yeah, [hero.name], what's going on?"
    hide audrey
    show audrey swimsuit surprised at left4 with dissolve
    audrey.say "Wait a minute - you mean you don't know?"
    audrey.say "I mean, we all know what we know."
    audrey.say "But I thought you two both knew what [hero.name] and I know too!"
    show shiori annoyed
    shiori.say "Oh...please stop it, Audrey."
    shiori.say "You're making my head spin!"
    lavish.say "Wait a minute..."
    lavish.say "Are you saying what I think you're saying?"
    show audrey mock
    audrey.say "I won't know until you say it, lavish."
    mike.say "Lavish..."
    mike.say "Be careful..."
    show lavish surprised
    lavish.say "That [hero.name]'s been sleeping with all of us."
    lavish.say "All at the same time too!"
    show shiori surprised
    show audrey surprised
    "The look of shock and horror on Audrey's face is almost perfect."
    "Far more convincing than her earlier attempt at innocence."
    audrey.say "Oh my god!"
    audrey.say "That's not what I meant at all, lavish!"
    audrey.say "But now that you come to mention it..."
    show audrey flirt
    "And just like that, Audrey's got everyone right where she wants them."
    "Lavish and Shiori gasp and turn on me almost as one."
    "I hold my hands up, looking like I'm trying to appeal for calm."
    "But the truth is that I'm more than a little scared of being attacked!"
    mike.say "Okay, okay..."
    mike.say "I know this looks bad."
    mike.say "But I think Audrey had a point earlier - we should be bonding."
    show lavish normal
    lavish.say "What are you talking about?"
    show shiori embarrassed
    shiori.say "Yeah - I don't understand!"
    mike.say "Look..."
    mike.say "We all work well together, right?"
    mike.say "And we've all been having fun together too, yeah?"
    show shiori annoyed
    "Lavish and Shiori look at each other awkwardly."
    "And I can see that they're beginning to blush."
    show lavish embarrassed blush
    lavish.say "I...I have kind of liked being with you and Audrey."
    show shiori normal blush
    shiori.say "It's scary...but good scary, you know?"
    show audrey happy
    audrey.say "So what's the problem, you guys?"
    audrey.say "Why don't we all just come clean and admit it?"
    audrey.say "We'd have SO much more fun if we jumped into bed together!"
    if all([person.love >= 140 and person.sub >= 25 for person in [audrey, lavish, shiori]]):
        lavish.say "Well, it hasn't held back my career so far."
        lavish.say "And it does sound pretty interesting..."
        shiori.say "I suppose so."
        shiori.say "I does kind of make sense..."
        "Lavish and Shiori both stop and look at each other."
        "They seem surprised to hear themselves in agreement."
        lavish.say "So..."
        show lavish flirt
        lavish.say "You're okay with this, Shiori?"
        shiori.say "I think so, Lavish."
        show shiori flirt
        shiori.say "Are you?"
        lavish.say "I guess I am!"
        "Audrey lets out a groan and rolls her eyes."
        audrey.say "Urgh..."
        audrey.say "You could at least sound happy about it."
        audrey.say "After all - this is going to be great!"
        show lavish happy
        show shiori happy
        "Lavish and Shiori both smile at this."
        "But I can already see them looking to me for support."
        mike.say "Audrey's right, guys."
        mike.say "I get it that you're a little scared."
        mike.say "But I'll make sure this is good for all of us, okay?"
        lavish.say "If I have your word, [hero.name]."
        shiori.say "I know I can trust you, [hero.name]."
        "I nod and smile in return."
        "The whole time hoping that I can be as good as my word."
        "Audrey shakes her head at the three of us."
        audrey.say "Geez..."
        audrey.say "What have I let myself in for with you prudes?!?"
        $ game.flags.officeharemfourdelay = TemporaryFlag(True, 2)
        $ Harem.join_by_name("office", "audrey", "lavish", "shiori")
        $ game.active_date.score = 85
    elif shiori.love > lavish.love and shiori.love >= 120:
        shiori.say "I suppose so."
        show shiori flirt
        shiori.say "I does kind of make sense..."
        show lavish annoyed -blush
        lavish.say "Oh no...no way!"
        "Lavish takes a decisive step away from the rest of us."
        "The whole time she's shaking her head and waving her arms."
        lavish.say "I might have been able to handle fooling around at work."
        lavish.say "Even with more than one co-worker at a time."
        lavish.say "But this is turning into some kind of weird sex-cult!"
        show shiori normal -blush
        show audrey normal -blush
        "She's already beginning to gather up her things as she says this."
        mike.say "Lavish, please..."
        "At the sound of my voice, Lavish stands up."
        "And then she cuts me off dead."
        show lavish angry
        lavish.say "Don't try and stop me, [hero.name]."
        lavish.say "My mind's made up."
        lavish.say "I can't work in the same office as you anymore."
        lavish.say "If none of you ever mention this to me again, I'll do the same."
        lavish.say "I'll keep quiet and let you do all the perverse shit you want."
        lavish.say "But if I have to hear about it one more time, I go to the HR department!"
        hide lavish with moveoutright
        "And with that, Lavish turns and storms off down the beach."
        "Shiori and I watch her go in silence."
        "But Audrey pipes up as soon as Lavish is out of earshot."
        audrey.say "Geez..."
        audrey.say "What a prude!"
        $ lavish.set_gone_forever()
        $ game.flags.officeharemfourdelay = TemporaryFlag(True, 2)
        $ Harem.join_by_name("office", "audrey", "shiori")
        $ game.active_date.score = 60
    elif lavish.love > shiori.love and lavish.love >= 120:
        show lavish flirt
        lavish.say "Well, it hasn't held back my career so far."
        lavish.say "And it does sound pretty interesting..."
        show shiori surprised -blush
        shiori.say "Oh, Lavish - what are you even saying?!?"
        "Shiori claps her hands on her cheeks in horror."
        "And she's already backing away from the rest of us."
        show lavish normal -blush
        show audrey normal -blush
        shiori.say "Don't you see what's happening, Lavish?"
        shiori.say "[hero.name] is using his sexual charms on us."
        shiori.say "He's like some kind of hypnotist or magician!"
        shiori.say "Who knows what he'll make us do next!"
        "Shiori turns and starts to grab her things off of the sand."
        mike.say "Shiori, please..."
        mike.say "I think you might be overreacting a little bit!"
        "At the sound of my voice close to her ear, Shiori springs up."
        "She waves a flip-flop at me, brandishing it like a weapon."
        show shiori angry
        shiori.say "Get back!"
        shiori.say "Don't use your powers on me again!"
        shiori.say "I have to go...find somewhere else to work!"
        hide shiori with moveoutright
        "And with that, Shiori turns and scuttles off down the beach."
        "Lavish and I watch her go in silence."
        "But Audrey pipes up as soon as Shiori is out of earshot."
        audrey.say "Geez..."
        audrey.say "What a weirdo!"
        $ shiori.set_gone_forever()
        $ game.flags.officeharemfourdelay = TemporaryFlag(True, 2)
        $ Harem.join_by_name("office", "audrey", "lavish")
        $ game.active_date.score = 60
    else:
        show lavish surprised -blush
        lavish.say "Oh no...no way!"
        show shiori surprised -blush
        shiori.say "[hero.name], how could you?!?"
        "As one, Lavish and Shiori start backing away from me."
        lavish.say "This is turning into some kind of weird sex-cult!"
        shiori.say "[hero.name] is using his sexual charms on us."
        shiori.say "He's like some kind of hypnotist or magician!"
        "Lavish and Shiori begin gathering up their things."
        mike.say "Lavish, Shiori..."
        mike.say "Please, just hear me out?"
        "At the sound of my voice, they both leap up."
        "Lavish shakes her head at me."
        "And Shiori waves a flip-flop at me, brandishing it like a weapon."
        show shiori angry
        shiori.say "Get back!"
        shiori.say "Don't use your powers on me again!"
        show lavish angry
        lavish.say "Don't try and stop us, [hero.name]."
        lavish.say "We can't work in the same office as you anymore."
        lavish.say "If you and Audrey never mention this again, we'll do the same."
        lavish.say "We'll keep quiet and let you do all the perverse shit you want."
        lavish.say "But if we have to hear about it one more time, we go to the HR department!"
        hide shiori
        hide lavish
        with moveoutright
        "And with that, they turn and hurry off down the beach together."
        "I watch them go in silence, but Audrey pipes up at my side."
        audrey.say "Wow..."
        audrey.say "What a couple of prudes!"
        $ shiori.set_gone_forever()
        $ lavish.set_gone_forever()
        $ game.active_date.score = 0
    $ game.pass_time(1)
    $ hero.cancel_activity()
    return

label office_audrey_lavish_shiori_01:
    "I've been waiting to do this ever since we had the little gathering on the beach."
    "You remember - the one where it came out that I'd been seeing all three of the girls?"
    "Audrey, Lavish and Shiori at the same time?"
    "And rather than being outed as some kind of epic cheater, things went the other way?"
    "Well, now the time has come for me to make good on the arrangement that we all came to."
    play sound "<from 0 to 4>sd/SFX/phone/phone_calling.ogg"
    "I pick up the phone and dial the code for Audrey's extension."
    audrey.say "Yeah, [hero.name] - what is it?"
    "I can't help smiling at the sound of Audrey's familiar rudeness."
    "That and knowing that she's likely to change her tune momentarily."
    mike.say "Audrey, I wonder if you'd mind stepping into my office for a moment."
    audrey.say "Urgh..."
    audrey.say "Can't you get Lavish or Shiori to do it?"
    audrey.say "I'm kind of busy right now!"
    mike.say "Well, here's the thing, Audrey."
    mike.say "What I had in mind needs all three of you."
    mike.say "So you could send Lavish and Shiori in on their own..."
    "It doesn't take more than a second for Audrey to catch on."
    "And then I see the instant change in attitude that I predicted."
    audrey.say "Oh...I get it!"
    audrey.say "Why didn't you just say so?"
    audrey.say "I'll just go round them up - okay?"
    "And with that, Audrey hangs up the phone."
    "I shake my head as I do the same, the smile on my face that much wider."
    "Audrey's as good as her word."
    show audrey work at left with easeinleft
    "And I don't have to wait long before she comes bustling into my office."
    "She doesn't knock, but then she never bothers to knock."
    "Lavish or Shiori would have knocked."
    show audrey work at right4
    show lavish work at left
    show shiori work embarrassed at top_mostleft
    with easeinleft
    "And I can see that fact in their eyes as they file in behind Audrey."
    "But what's of more interest to me right now is what else I can see in there."
    "Sure, I expected them to be nervous when we tried this out for the first time."
    "I admit, Shiori much more so than Lavish."
    "And yet I can see intrigue in Lavish as she looks at me."
    "Even Shiori seems to have a determination underneath her obvious nerves."
    show audrey work at right
    show lavish work at center
    show shiori work at left
    with ease
    "That's good, and it makes the smile on my own face all the more genuine."
    "I don't think I could have gotten into this thing otherwise."
    "Not if either of them was actually terrified at the prospect."
    show audrey flirt
    audrey.say "Here we are, boss."
    lavish.say "Yeah, let's do this thing."
    show shiori normal blush
    shiori.say "I...I'm ready too."
    shiori.say "If you promise to be gentle with me?"
    show audrey topless
    "Audrey can't help letting out a giggle as she begins to strip off."
    "But I'm more keen to ensure that everyone is as comfortable as possible."
    mike.say "Don't worry, Shiori."
    mike.say "The idea is for us all to have fun."
    mike.say "I won't ask you to do anything you don't want to, okay?"
    show shiori topless
    "Shiori nods and then begins to take off her own clothes."
    show lavish topless
    "Lavish had already started to do so as I was reassuring Shiori."
    "And so that leaves me to hurry after the others."
    "By the time I manage to strip off the last of my clothes, they're all done."
    show audrey naked
    show lavish naked
    show shiori naked
    "The three of them stand there before me, naked and ready to go."
    "But I still haven't spared a thought for who goes where..."
    call office_audrey_lavish_shiori_fuck from _call_office_audrey_lavish_shiori_fuck
    return

label office_audrey_lavish_shiori_fuck:
    menu:
        "Fuck Audrey":
            call office_foursome_cowgirl from _call_office_foursome_cowgirl
        "Fuck Lavish":
            call office_foursome_standing from _call_office_foursome_standing
        "Fuck Shiori":
            call office_foursome_reverse_cowgirl from _call_office_foursome_reverse_cowgirl
    $ game.pass_time(2)
    $ hero.cancel_activity()
    return

label office_foursome_cumshare:
    "Before I can move a muscle, even before I can shoot my load, Audrey springs into action."
    scene office foursome cumshare audrey lavish shiori with fade
    "She grabs hold of my cock, wrapping her lips around the head."
    "Lavish seems to understand what's happening, and begins to caress my balls."
    "But Shiori simply looks on with a puzzled expression on her face."
    "She opens her mouth, presumably to ask what's going on."
    "And that's the very same moment that Audrey opens hers too."
    show office foursome cumshare audrey lavish shiori cumshot with hpunch
    "As soon as her lips are off of my cock, it goes off like a cork popping out of a bottle."
    show office foursome cumshare audrey lavish shiori cum
    show office foursome cumshare audrey lavish shiori dickcum
    with hpunch
    $ audrey.love += 4
    $ lavish.love += 4
    $ shiori.love += 4
    "Audrey is closest, so she gets the largest part of it square in the face."
    "Lavish takes a little less thanks to being do low down as I shoot my load."
    "But even though Shiori's nowhere near the centre of the action, she makes the most noise."
    shiori.say "Ah..."
    shiori.say "Oh god..."
    shiori.say "It hit me...in the face!"
    "Shiori wrinkles her nose and sticks out her tongue in disgust."
    "But she regrets it a moment later when Audrey and Lavish kiss her at the same time."
    "Lets out a muffled wail as they pass on some of the cum that landed in their mouths too!"
    "And I can't help joining in, chuckling as I shake my head at their antics."
    $ DONE["office_foursome_cumshare"] = game.days_played
    return

label office_foursome_reverse_cowgirl:
    "I want to be into this thing like crazy, ready and raring to go."
    "I mean, who wouldn't want to be doing this with three hot girls?"
    "But there's a part of me that just can't keep worrying about Shiori."
    "Audrey's cocky and Lavish is quietly confident, even in the face of a foursome."
    "But Shiori still looks nervous as hell at the prospect of what lies ahead."
    "I can't help wanting to make it all okay for her, to protect her."
    "And so it's a no-brainer that I reach out and take hold of her hand."
    "Shiori yelps and jumps a little as I do so, betraying her nerves."
    $ shiori.love += 2
    shiori.say "Ooh!"
    shiori.say "Oh...I'm sorry, [hero.name]."
    shiori.say "You made me jump!"
    "I smile at her apology, shaking my head a little."
    "She's so sweet and innocent that I can't help giving her all of my attention."
    mike.say "It's okay, Shiori."
    mike.say "Just come over here with me, okay?"
    "Shiori nods at this, her huge eyes fixed upon me."
    "And she doesn't take them off of me for a moment as I lead her over to the sofa."
    "I'm only vaguely aware of Audrey and Lavish following us over there too."
    "They hold back as I sit down and Guide Shiori onto my lap."
    menu:
        "Use a condom" if hero.has_condom():
            $ CONDOM = hero.use_condom()
        "Do not use a condom":
            $ CONDOM = False
    scene office foursome shiorifuck audrey lavish
    show office foursome shiorifuck audrey lavish lookback
    with fade
    if CONDOM:
        show office foursome shiorifuck audrey lavish lookback condom
    "She smiles at first, still holding my eye."
    "But then she feels something brush against her and looks down."
    "Which means that she's staring straight at the tip of my cock!"
    shiori.say "Oh, [hero.name]!"
    shiori.say "It's...so big!"
    shiori.say "Is it all for me?"
    "How can she be so humble and innocent?"
    "Is it all just an act?"
    "She's as cute as hell, with a body that kills me just to look at it."
    "How can she not know that she makes me this hard without even trying?!?"
    mike.say "It's all your's, Shiori."
    mike.say "If you'll let me give it to you?"
    "Shiori's cheeks blush with colour at this."
    "And she covers her mouth to stifle a giggle."
    shiori.say "Okay, [hero.name]."
    shiori.say "I'll try my best - I promise!"
    "With that, Shiori guides my hands to her waist."
    "And then she puts her own hands on my shoulders."
    "She looks down on me with a smile, literally putting herself in my hands..."
    menu:
        "Fuck her ass" if shiori.flags.anal and hero.sexperience >= 20:
            "Maybe it sounds odd, but my first instinct is to part Shiori's buttocks."
            "And once they're spread nice and wide, I aim my cock straight for her ass."
            show office foursome shiorifuck audrey lavish anal
            "Sure, it might sound like an odd thing to do when she's so nervous."
            "But I figure the best thing is to make Shiori face her fears."
            "Plus, it makes the whole thing that much more fun for me too!"
            shiori.say "Ah..."
            shiori.say "Erm... [hero.name]..."
            show office foursome shiorifuck audrey lavish lookback
            shiori.say "I think you're a little lost!"
            "By way of answer, I pull Shiori down and onto me."
            "The movement is sudden and unexpected, taking her by surprise."
            show office foursome shiorifuck audrey lavish pleasure
            "And before she knows it, I'm already too deep into her ass to stop."
            $ shiori.sub += 2
            shiori.say "Oooh..."
            shiori.say "Oh, [hero.name], what are you doing to me?!?"
            "Shiori wriggles in my lap, her huge breasts quivering."
            "But all she manages to do is sink further down and onto my cock."
            shiori.say "Oh...oh my..."
            shiori.say "You're so wicked...so wicked..."
            "Shiori can call me wicked all she wants."
            "But I note that she doesn't once ask me to stop!"
            "I begin to thrust in and out of Shiori."
            "I go slowly at first, but soon begin to pick up speed."
            "And she matches me every step of the way."
            "At first, Shiori is meek and almost quiet as she rides my cock."
            "But as I pick up the pace, she becomes ever more animated."
            "Soon enough there's nothing she can do to keep herself contained."
            "And she's bucking in my lap, bouncing up and down the whole time."
            "All I can do is stare up at her, almost hypnotised by the look on her face."
            "Shiori seems to be almost in a trance, lost in the moment."
            "But then, without warning, her eyes burst open and her so does her mouth!"
            show office foursome shiorifuck audrey lavish lookback
            shiori.say "Ow..."
            shiori.say "Ooh..."
            shiori.say "Who did that?!?"
            "Shiori and I are both looking around now."
            "Both trying to figure out what's going on."
            "It's then that I spot Audrey to one side and Lavish to the other."
            "They're crouched down around Shiori's ass, mischievous faces smiling back at me."
            "I watch as they playfully bite and lick at the other girl's buttocks."
            show office foursome shiorifuck audrey lavish pleasure
            shiori.say "Hey..."
            shiori.say "No..."
            shiori.say "Stop that, right now!"
            "I might have said something myself too."
            "Though I can't say that it'd have been to tell them to stop!"
            "But Shiori's wriggling and squirming on top of me right now."
            "I can tell that she's just trying to avoid Audrey and Lavish."
            "But it's having a very different effect on me!"
            "Shiori bounces up and down on my cock, all of her weight squeezing me."
            "I can't hold it in any longer."
            "She's going to make me cum!"
            if hero.sexperience >= 30 and "office_foursome_cumshare" not in DONE:
                call office_foursome_cumshare from _call_office_foursome_cumshare
            else:
                menu:
                    "Cum inside":
                        "Even if I wanted to pull out of Shiori, she's making it all but impossible."
                        "And at the very moment I shoot my load, she pushes all her weight down on me."
                        with hpunch
                        "This means that I'm as deep inside of her as I can go when I cum."
                        if not CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm cum
                            $ shiori.sub += 2
                        else:
                            show office foursome shiorifuck audrey lavish orgasm
                        with hpunch
                        "Shiori let's out a wail at the sensation, grinding herself against me."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Pull out":
                        "I wait until the moment Shiori's in just the right place..."
                        if not CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm outside
                        else:
                            show office foursome shiorifuck audrey lavish orgasm outside condom
                        "And then I pull my cock out of her in one smooth motion."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        if CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm
                            "Understanding that I'm about to cum, Audrey and Lavish act together to remove the rubber I put earlier."
                        show office foursome shiorifuck audrey lavish orgasm cumshot with vpunch
                        $ shiori.love += 4
                        "Shiori wails as I shoot my load."
                        hide office foursome shiorifuck audrey lavish orgasm cumshot
                        show office foursome shiorifuck audrey lavish orgasm asscum
                        with vpunch
                        "It hits her belly and the underside of her heavy breasts."
                        "But thanks to them being so large, it can't reach any higher."
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Share the love" if "office_foursome_cumshare" in DONE:
                        call office_foursome_cumshare from _call_office_foursome_cumshare_1
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "I'm not about to change direction and shock Shiori now."
            "And so I gently guide her down and onto my cock."
            "She pants and then bites her lip as it slides along her pussy."
            "But the pants become a moan a few seconds later."
            show office foursome shiorifuck audrey lavish vaginal
            "Because that's the moment I choose to pull her down and onto me."
            "There's a token of resistance from Shiori's body."
            "And then I'm inside of her for real."
            "She sinks down, taking the whole length of my cock."
            "She doesn't stop until I'm balls deep in her."
            $ shiori.love += 2
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're so big!"
            shiori.say "You've filled me up!"
            "Shiori's smile is broad and looks completely genuine."
            "Her eyes are as wide as I've ever seen them right now."
            "She looks like having my cock inside of her is the greatest experience of her life!"
            "And that just makes me all the more determined to ensure that it really is."
            "I begin to thrust in and out of Shiori."
            "I go slowly at first, but soon begin to pick up speed."
            "And she matches me every step of the way."
            "At first, Shiori is meek and almost quiet as she rides my cock."
            "But as I pick up the pace, she becomes ever more animated."
            "Soon enough there's nothing she can do to keep herself contained."
            "And she's bucking in my lap, bouncing up and down the whole time."
            "All I can do is stare up at her, almost hypnotised by the look on her face."
            "Shiori seems to be almost in a trance, lost in the moment."
            "But then, without warning, her eyes burst open and her so does her mouth!"
            show office foursome shiorifuck audrey lavish lookback
            shiori.say "Ow..."
            shiori.say "Ooh..."
            shiori.say "Who did that?!?"
            "Shiori and I are both looking around now."
            "Both trying to figure out what's going on."
            "It's then that I spot Audrey to one side and Lavish to the other."
            "They're crouched down around Shiori's ass, mischievous faces smiling back at me."
            "I watch as they playfully bite and lick at the other girl's buttocks."
            show office foursome shiorifuck audrey lavish pleasure
            shiori.say "Hey..."
            shiori.say "No..."
            shiori.say "Stop that, right now!"
            "I might have said something myself too."
            "Though I can't say that it'd have been to tell them to stop!"
            "But Shiori's wriggling and squirming on top of me right now."
            "I can tell that she's just trying to avoid Audrey and Lavish."
            "But it's having a very different effect on me!"
            "Shiori bounces up and down on my cock, all of her weight squeezing me."
            "I can't hold it in any longer."
            "She's going to make me cum!"
            if hero.sexperience >= 30 and "office_foursome_cumshare" not in DONE:
                call office_foursome_cumshare from _call_office_foursome_cumshare_2
            else:
                menu:
                    "Cum inside":
                        "Even if I wanted to pull out of Shiori, she's making it all but impossible."
                        "And at the very moment I shoot my load, she pushes all her weight down on me."
                        with vpunch
                        "This means that I'm as deep inside of her as I can go when I cum."
                        if not CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm cum
                            $ shiori.love += 4
                            $ shiori.impregnate()
                        else:
                            show office foursome shiorifuck audrey lavish orgasm
                        with vpunch
                        "Shiori let's out a wail at the sensation, grinding herself against me."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Pull out":
                        "I wait until the moment Shiori's in just the right place..."
                        if not CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm outside
                        else:
                            show office foursome shiorifuck audrey lavish orgasm outside condom
                        "And then I pull my cock out of her in one smooth motion."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        if CONDOM:
                            show office foursome shiorifuck audrey lavish orgasm
                            "Understanding that I'm about to cum, Audrey and Lavish act together to remove the rubber I put earlier."
                        show office foursome shiorifuck audrey lavish orgasm cumshot with vpunch
                        $ shiori.love += 4
                        "Shiori wails as I shoot my load."
                        hide office foursome shiorifuck audrey lavish orgasm cumshot
                        show office foursome shiorifuck audrey lavish orgasm asscum
                        with vpunch
                        "It hits her belly and the underside of her heavy breasts."
                        "But thanks to them being so large, it can't reach any higher."
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Share the love" if "office_foursome_cumshare" in DONE:
                        call office_foursome_cumshare from _call_office_foursome_cumshare_3
    $ shiori.sexperience += 1
    return

label office_foursome_standing:
    "The easiest thing here would be to beat a path straight for Audrey."
    "And that's because I know that she's the most up for it right now."
    "Or maybe I should be taking Shiori in hand instead?"
    "She is the one that looks the most nervous at what lies ahead."
    "But what about Lavish?"
    "Where does she figure in all of this?"
    "She's not as eager as Audrey or as meek as Shiori."
    "Perhaps that's what makes her the perfect choice of the three?"
    "If I choose her, then I can put Audrey in her place a little."
    "And I can take some of the pressure off of Shiori as well."
    "But it's not like Lavish is the poorer choice in comparison to either of them."
    "A fact that I'm reminded of the very moment that she realises I have my eye on her."
    "I come up behind Lavish, placing my hands carefully upon her waist."
    "She looks over her shoulder at me the whole time."
    "Her thick, black hair falls over one of her eyes."
    "And I can just make out the tinge of a blush on her cheeks."
    lavish.say "Y...you want me?"
    "I nod at this, trying to look like a strong and confident alpha male."
    "But the truth is that I'm afraid to speak my answer in case it come out as a squeak."
    "Being up close to Lavish like this is just that disarming!"
    $ lavish.love += 2
    lavish.say "Oh..."
    lavish.say "Okay, [hero.name]."
    lavish.say "I'm all yours!"
    "I feel like Lavish is talking me harder with every word she says."
    "She's so quiet and so willing to put herself in my hands."
    "But the truth is I feel like an obedient dog that's at her command."
    "I gently push my cock between Lavish's thighs."
    "And it doesn't take me long to feel that she's excited as well."
    "I'm all ready to simply push a little harder."
    "Ready to just find my way inside of her and enjoy the ride."
    audrey.say "Hey, Lavish."
    audrey.say "You look like you could use a hand there!"
    "Without asking for permission, Audrey steps up and gets involved."
    "She lifts one of Lavish's legs, exposing her completely."
    lavish.say "Whoa..."
    lavish.say "I can't..."
    lavish.say "I'm going to fall..."
    shiori.say "Don't worry, Lavish."
    shiori.say "I've got you!"
    scene office foursome lavishfuck audrey shiori
    "Quick as a flash, Shiori is on Lavish's other side."
    "She takes hold of the other girl, supporting her weight."
    "There's now no chance of Lavish toppling over."
    "And everyone's wrapped up together, whether we like it or not!"
    audrey.say "Okay..."
    audrey.say "Now where were we?!?"
    "I make eye-contact with Lavish, waiting for her to tell me what she wants."
    "She bites her lip, but then nods quickly, urging me on."
    "The only question is, what am I going to do with her?"
    menu:
        "Fuck her ass":
            "I could keep things simple."
            "But then where's the fun in that?"
            "I mean, we're having a foursome at work."
            "In my office."
            "In the middle of the day!"
            "I think the time to be conservative is long gone."
            "Which is why I pull back just a little."
            "Just enough to slip my cock between Lavish's buttocks."
            show office foursome lavishfuck audrey shiori anal
            lavish.say "Ooh!"
            lavish.say "[hero.name]..."
            lavish.say "What are you doing?!?"
            "I know that I can't stop and explain myself."
            "That would kill the moment, end this whole thing."
            "And so I ignore Lavish's question and press on."
            "Her ass reacts in the exact same way."
            "Lavish's muscles pucker and tighten, trying to keep me out."
            "But the fact her leg has been lifted and her thighs spread works to my advantage."
            "She has to lift herself to escape, and the moment that she can't keep it up..."
            lavish.say "I...I..."
            lavish.say "I don't think I..."
            lavish.say "Oh...I do...I like it!"
            "Lavish finally surrenders."
            "She allows herself to sink down onto my cock."
            "And the feeling is just incredible."
            "I came to this thing full of the best possible intentions."
            "The idea was to make love to Lavish, of course."
            "But also to make sure that everyone got something out of this."
            "The problem is that all of that's gone from my mind in an instant."
            "And all I can think about is how much I want to fuck Lavish right now!"
            "I know that I should start out slow and build up speed."
            "But it only takes a couple of seconds for me to get carried away."
            "Before she has time to match my rhythm, I'm pounding away on Lavish."
            "And the fact that she's being held up by the others means she can't resist."
            "Pretty soon Lavish is panting and gasping as I thrust in and out of her."
            "Even if she was of a mind to object, she's too busy moaning to do so."
            "Audrey and Shiori do their best to keep her upright."
            "And all the while Lavish wriggles and writhes in their arms."
            "I can see worry mixed with curiosity in Shiori's eyes."
            "At the same time, Audrey watches with amusement and not a little jealousy too."
            "But I try to tear my attention away from them and focus solely on Lavish."
            "I can't keep this up much longer."
            "I'm going to lose it any moment..."
            if hero.sexperience >= 30 and "office_foursome_cumshare" not in DONE:
                call office_foursome_cumshare from _call_office_foursome_cumshare_4
            else:
                menu:
                    "Cum inside":
                        "I'm so deep in Lavish that I can't hope to pull out in time."
                        show office foursome lavishfuck audrey shiori orgasm cum with hpunch
                        $ lavish.sub += 2
                        "And so when I do cum, it explodes inside of her."
                        lavish.say "Oh shit..."
                        lavish.say "Oh shit..."
                        lavish.say "Mmm..."
                        "Audrey and Shiori keep her upright the whole time."
                        "And Lavish rides my cock until the very last second."
                        "Only when her head finally sags do they lower her to the floor."
                        "Lavish lies there, a heap of sweaty, quivering limbs."
                    "Pull out":
                        "Trusting Audrey and Shiori to keep Lavish upright, I pull myself out of her."
                        show office foursome lavishfuck audrey shiori orgasm
                        "As I do so, she seems to realise what's happening."
                        lavish.say "Wha..."
                        lavish.say "What are you..."
                        show office foursome lavishfuck audrey shiori orgasm outside cum with hpunch
                        "But almost as soon as my cock is out of her, I shoot my load."
                        with hpunch
                        "Streamers of hot, sticky cum strip Lavish's back and buttocks."
                        show office foursome lavishfuck audrey shiori orgasm dickcum with hpunch
                        $ lavish.love += 4
                        "And she wails in surprise."
                        "Audrey and Shiori keep her upright the whole time."
                        "And Lavish rides my cock until the very last second."
                        "Only when her head finally sags do they lower her to the floor."
                        "Lavish lies there, a heap of sweaty, quivering limbs."
                    "Share the love" if "office_foursome_cumshare" in DONE:
                        call office_foursome_cumshare from _call_office_foursome_cumshare_5
            $ lavish.flags.anal += 1
        "Fuck her pussy":
            menu:
                "Use a condom" if hero.has_condom():
                    $ CONDOM = hero.use_condom()
                "Do not use a condom":
                    $ CONDOM = False
            "We already have four pairs of hands in this thing."
            "So that's all the more reason to keep things simple."
            "And all it takes is a little thrust below the waist..."
            show office foursome lavishfuck audrey shiori vaginal
            if CONDOM:
                show office foursome lavishfuck audrey shiori vaginal condom
            $ lavish.love += 2
            lavish.say "Oh!"
            lavish.say "[hero.name]..."
            lavish.say "That feels SO good!"
            "It's not like I needed anyone to tell me that!"
            "My cock slips inside of Lavish smoothly."
            "And I don't stop until I'm balls deep in her."
            "The sounds that she makes at the same time are almost as good as it feels."
            "With Audrey and Shiori holding her up, I'm free to enjoy myself."
            "And Lavish is too!"
            lavish.say "P...please, [hero.name]..."
            lavish.say "I...I want more!"
            lavish.say "Please...fuck me?"
            "How can I refuse a request like that and still call myself a gentleman?"
            "And so I take a firm hold of Lavish, pulling her against me."
            "She moans and whimpers in anticipation."
            "I came to this thing full of the best possible intentions."
            "The idea was to make love to Lavish, of course."
            "But also to make sure that everyone got something out of this."
            "The problem is that all of that's gone from my mind in an instant."
            "And all I can think about is how much I want to fuck Lavish right now!"
            "I know that I should start out slow and build up speed."
            "But it only takes a couple of seconds for me to get carried away."
            "Before she has time to match my rhythm, I'm pounding away on Lavish."
            "And the fact that she's being held up by the others means she can't resist."
            "Pretty soon Lavish is panting and gasping as I thrust in and out of her."
            "Even if she was of a mind to object, she's too busy moaning to do so."
            "Audrey and Shiori do their best to keep her upright."
            "And all the while Lavish wriggles and writhes in their arms."
            "I can see worry mixed with curiosity in Shiori's eyes."
            "At the same time, Audrey watches with amusement and not a little jealousy too."
            "But I try to tear my attention away from them and focus solely on Lavish."
            "I can't keep this up much longer."
            "I'm going to lose it any moment..."
            if hero.sexperience >= 30 and "office_foursome_cumshare" not in DONE:
                call office_foursome_cumshare from _call_office_foursome_cumshare_6
            else:
                menu:
                    "Cum inside":
                        "I'm so deep in Lavish that I can't hope to pull out in time."
                        if not CONDOM:
                            show office foursome lavishfuck audrey shiori orgasm cum
                            $ lavish.love += 4
                            $ lavish.impregnate()
                        else:
                            show office foursome lavishfuck audrey shiori orgasm
                        with hpunch
                        "And so when I do cum, it explodes inside of her."
                        lavish.say "Oh shit..."
                        lavish.say "Oh shit..."
                        lavish.say "Mmm..."
                        "Audrey and Shiori keep her upright the whole time."
                        "And Lavish rides my cock until the very last second."
                        "Only when her head finally sags do they lower her to the floor."
                        "Lavish lies there, a heap of sweaty, quivering limbs."
                    "Pull out":
                        "Trusting Audrey and Shiori to keep Lavish upright, I pull myself out of her."
                        show office foursome lavishfuck audrey shiori orgasm
                        "As I do so, she seems to realise what's happening."
                        lavish.say "Wha..."
                        lavish.say "What are you..."
                        show office foursome lavishfuck audrey shiori orgasm outside cum with hpunch
                        "But almost as soon as my cock is out of her, I shoot my load."
                        with hpunch
                        "Streamers of hot, sticky cum strip Lavish's back and buttocks."
                        if not CONDOM:
                            show office foursome lavishfuck audrey shiori orgasm dickcum
                            $ lavish.love += 4
                        "And she wails in surprise."
                        "Audrey and Shiori keep her upright the whole time."
                        "And Lavish rides my cock until the very last second."
                        "Only when her head finally sags do they lower her to the floor."
                        "Lavish lies there, a heap of sweaty, quivering limbs."
                    "Share the love" if "office_foursome_cumshare" in DONE:
                        call office_foursome_cumshare from _call_office_foursome_cumshare_7
    $ lavish.sexperience += 1
    return

label office_foursome_cowgirl:
    "Maybe it's the more wicked side of me coming through, but I can't help it."
    "I just make a beeline straight for Audrey, almost ignoring the other girls."
    "After all, she's kind of been the driving force behind us all coming together."
    "So it kind of makes sense that she should be the centre of attention the first time we do it."
    menu:
        "Use a condom" if hero.has_condom():
            $ CONDOM = hero.use_condom()
        "Do not use a condom":
            $ CONDOM = False
    mike.say "Audrey..."
    mike.say "Come on over here."
    "Audrey looks up and meets my eye, her mouth hanging open as she does so."
    "For just the fraction of a second, I think that I can see trepidation in her eyes."
    "But then she seems to shake it off and becomes the Audrey we all know so well."
    $ audrey.love += 2
    audrey.say "Sure thing, [hero.name]."
    audrey.say "Let's show them how it's done!"
    "Lavish and Shiori exchange a knowing glance at this."
    "But whatever they're thinking, they keep to themselves."
    "Audrey takes my hand and allows me to lead her over to the couch."
    "Once there, I turn her around so that she has her back to me."
    "I sit down on the couch as she looks back over her shoulder."
    "She seems to be waiting for me to tell her what to do next."
    "But once Audrey's gaze settles on my already stiff cock, she takes matters into her own hands."
    show office foursome audreyfuck lavish shiori lookdown
    if CONDOM:
        show office foursome audreyfuck lavish shiori lookdown condom
    "She lowers herself backwards and down onto my lap, aiming for my manhood."
    "And it's at this point that Lavish and Shiori get involved too."
    "Flanking Audrey to each side, they support her as she straddles my lap."
    "A moment later I feel the tip of my cock brush between her legs."
    "And I'm treated to the sound of Audrey yelping at the sensation as well."
    audrey.say "Oh..."
    audrey.say "I...I mean ah..."
    audrey.say "There it is!"
    "I can hear the tell-tale signs in Audrey's voice right now."
    "And they're betraying the fact that she's trying to sound like she's in control."
    "But the truth is that I have her in the palm of my hand."
    "I can pretty much do whatever I want with her."
    "And now seems to be as good a time as any to remind her of that..."
    menu:
        "Fuck her ass":
            $ fchoice = 'anal'
            "If Audrey wants my cock so badly, then I see no reason to deny her."
            "But she never really said where she wanted it just now."
            "So maybe I should surprise her?"
            "I take a firm hold of Audrey around the waist."
            "And then I pull her downwards in just such a way..."
            audrey.say "Wha..."
            audrey.say "Wait a sec..."
            audrey.say "Mmm..."
            show office foursome audreyfuck lavish shiori anal pleasure
            audrey.say "Oh shit...you shit!"
            "My cock is deep inside of Audrey's ass before she's finished talking."
            "I can feel every moment of her muscles as they clamp around me."
            "But I keep right on pushing until the moment they finally surrender."
            $ audrey.sub += 2
            show office foursome audreyfuck lavish shiori anal lookdown
            audrey.say "Oh yeah..."
            audrey.say "That's good..."
            audrey.say "Just like that!"
            "Audrey's muscles seem to pull the rest of her after them."
            "And as they melt so does she, letting me move inside of her."
        "Fuck her pussy":
            "I take a firm hold of Audrey around the waist and pull her down."
            "The lips of her pussy press against the head of my cock."
            "She's slick and ready for me, but it slithers here and there."
            "For a moment I think that I'm going to miss the target completely."
            "But then I feel Audrey wriggling and squirming in my lap."
            "She pushes herself down..."
            show office foursome audreyfuck lavish shiori vaginal
            "And then I'm inside of her in one smooth motion."
            show office foursome audreyfuck lavish shiori lookdown
            $ audrey.love += 2
            audrey.say "Whoa..."
            audrey.say "Hello, big boy!"
            audrey.say "Now, let's see what you've got..."
            "As if the feeling of being this deep into Audrey wasn't enough."
            "The way she's talking makes it feel that much better too!"
            "Somehow, she makes me feel like she's about to ride a rollercoaster!"
            "And all I want to do is make sure that she has the ride of her life."
    show office foursome audreyfuck lavish shiori pleasure
    "Lavish and Shiori make sure to keep a firm hold on Audrey as I begin to move."
    "She already has her hands braced behind her, but it's not going to be enough."
    "Right from the start, Audrey's bouncing up and down in my lap."
    "She's really managed to get my blood up for this."
    "And there's no way that I'm going to slow down before it's over!"
    "Every time I thrust into Audrey, I try to go as deep as I can."
    "And every time I do so, I hear her moan with helpless delight."
    "She's not just pushing her hands against me now."
    "I can feel her fingers pressing into my skin, clinging onto me."
    show office foursome audreyfuck lavish shiori fx
    "It hurts more than a little, but that just pushes me on harder than before."
    "From where I'm sitting, I can see Lavish and Shiori pretty well."
    "While Audrey's pinned to the spot, they're free to do as they please."
    "And the hands that they're not using to hold onto her are roaming all over her!"
    "The look on Shiori's face is one of wide-eyed curiosity."
    "She almost seems afraid to touch Audrey at all."
    "Lavish is another case entirely, watching Audrey with a smile."
    "Her free hand is already caressing the breast closest to her."
    "And I hear Audrey whimper as she begins to pinch at the nipple too!"
    "As if given confidence by Lavish's example, Shiori become bolder now."
    "She mirrors the other girl's actions, starting to stroke Audrey's other breast."
    "It's hard to tell which is turning me on more."
    "Being inside of Audrey or watching Lavish and Shiori play with her!"
    "Okay, okay...it's probably the first one."
    "But the second is definitely taking it to the next level!"
    "At this rate, I don't think I can hold on much longer..."
    if hero.sexperience >= 30 and "office_foursome_cumshare" not in DONE:
        call office_foursome_cumshare from _call_office_foursome_cumshare_8
    else:
        menu:
            "Cum inside":
                hide office foursome audreyfuck lavish shiori fx
                if not CONDOM:
                    show office foursome audreyfuck lavish shiori creampie
                    $ audrey.love += 4
                    $ audrey.impregnate()
                with vpunch
                "With one final push, I shoot my load inside of Audrey."
                show office foursome audreyfuck lavish shiori ahegao creampie with vpunch
                "And she arches her back from the sensation, bending like a bow."
                "Lavish and Shiori are holding onto her for real now."
                "And without them, there's every chance she could fall off!"
                "Audrey rides out every last moment, bucking and tossing her head."
                "And then she slides sideways, falling into the arms of the other girls."
            "Pull out":
                "Audrey's still wriggling as I'm about to cum."
                show office foursome audreyfuck lavish shiori ahegao outside cumshot -vaginal with vpunch
                "And I take advantage of this to slide out from under her a second before it happens."
                with vpunch
                "She wails in surprise at the sensation and then again as it sprays over her."
                with vpunch
                "The cum lands on her breasts and belly, as well as Lavish and Shiori's hands too."
                "Audrey stays upright for a moment, bucking and tossing her head."
                "And then she slides sideways, falling into the arms of the other girls."
            "Share the love" if "office_foursome_cumshare" in DONE:
                call office_foursome_cumshare from _call_office_foursome_cumshare_9
    $ audrey.sexperience += 1
    return

label office_aletta_audrey_lavish_shiori_showdown:
    scene bg alettaoffice
    "I hate most kinds of meetings that pop up in the course of me trying to do my job."
    "But team meetings have to be the worst kind of all, the ones that put me straight to sleep."
    "All that time spent sitting in a room listening to someone droning on and on about whatever."
    "Why can't they just stick it in an email?"
    "Why do they have to waste an hour of my life I'm never getting back?"
    show aletta work at mostright5 with dissolve
    "Right now it's Aletta that's torturing me."
    "Draining my will to live with a presentation and slide-show."
    show lavish work zorder 1 at center, zoomAt(1, (180, 840)) with dissolve
    "I glance across the room, seeing that Lavish is sitting up and paying attention."
    show shiori work zorder 66 at center, zoomAt(1, (440, 840)) with dissolve
    "Shiori's at least pretending to do the same, but her mind seems to be elsewhere."
    show audrey work annoyed zorder 2 at center, zoomAt(1, (700, 840)) with dissolve
    "And then my eyes settle on Audrey, who looks just as bored senseless as I am."
    "But the difference is that she doesn't seem to be trying to hide the fact."
    "As soon as she sees me looking in her direction, Audrey perks up."
    "She holds my eye as she pulls off an exaggerated yawn."
    "And then she puts her fingers to her forehead, pretending to blow her brains out."
    "It's unprofessional and more than a little childish."
    "But I'm so bored that I can't help chuckling all the same."
    show aletta sad
    aletta.say "Ahem..."
    "At the sound of Aletta clearing her throat, I instantly stop laughing."
    "My head snaps around to see that she's stopped her presentation."
    "And worse, she's staring straight at me!"
    show aletta angry
    aletta.say "Did you have something you wanted to add, [hero.name]?"
    aletta.say "An insightful observation or a fresh take on things, maybe?"
    "I squirm in my seat as Aletta interrogates me in front of the others."
    "And I note with some annoyance that Audrey isn't about to help me either."
    mike.say "Ah...no, Aletta."
    mike.say "I was just...just clearing my throat."
    mike.say "Sorry..."
    show aletta annoyed
    "Aletta raises her eyebrows."
    "She looks singularly unimpressed with my explanation."
    show aletta normal
    "Right now she reminds me of every strict teacher I can remember from school!"
    aletta.say "Thank you, [hero.name]."
    aletta.say "Now, if I might continue..."
    aletta.say "The dictionary defines 'polyamory' as the practice of engaging in multiple romantic and sexual relationships."
    aletta.say "And doing so with the consent of all the people involved..."
    "Suddenly I feel the mood in the room change."
    show audrey mindless
    show shiori mindless at startle
    show lavish mindless
    "Now all four of us are sitting up in our seats, straining to listen."
    "Where in the hell is this going?"
    "Why is Aletta talking about polyamory?"
    "Is she onto the fact that we're all fucking together at work?!?"
    show shiori annoyed blush
    show lavish bored blush
    show audrey annoyed blush
    "I see glances being exchanged between Audrey, Lavish and Shiori."
    "But nobody seems eager to speak up and challenge Aletta just yet."
    aletta.say "As you already know, the practice was recently made legal."
    aletta.say "And at the time, opinion was that it could potentially harm business."
    aletta.say "The thought was that relationships of this kind could distract from work."
    "There's a collective intake of breath in the room."
    "Is Aletta about to label our secret foursome a detriment to the company?"
    aletta.say "But studies seem to actually show the opposite to be true."
    aletta.say "Companies where employees admitted to such relationships are more efficient."
    aletta.say "It seems that the more intimate the employees are, the more productive they become."
    "And with that, the collective breath is let out again."
    "We must be in the clear on this one, right?"
    "Didn't Aletta just say that it means we're more efficient?"
    "And anyway, she's not actually asking us to out ourselves - is she?"
    "I don't know why, but the thought makes me look over towards Audrey."
    "And when I do, I feel my heart sink."
    "She has a look on her face that reminds me of a cat."
    "A cat that's just seen a baby bird fall out of a nest."
    "A cat that also knows there's nobody around to stop it from indulging itself too!"
    show audrey happy
    audrey.say "Well, that must mean our productivity is up too then, right?"
    "Aletta blinks as she stares at Audrey."
    "And I don't know if it's the random nature of the question that's throwing her."
    "That or the fact she's not used to Audrey making a positive contribution of any kind."
    aletta.say "I'm sorry..."
    show aletta annoyed
    aletta.say "But what's it got to do with your productivity?"
    "Everyone else seems to move in slow-motion."
    "Lavish, Shiori and I all trying to speak before Audrey can answer."
    audrey.say "Well, we're all polyamorous - aren't we, guys?"
    audrey.say "Present company excepted, Aletta."
    "Aletta blinks and shakes her head."
    "Then she blinks again as her brain tries to process this new information."
    aletta.say "You mean..."
    aletta.say "You're all..."
    show aletta surprised at startle
    show shiori blush embarrassed
    show lavish blush annoyed
    aletta.say "I...I had no idea!"
    mike.say "Nobody else knew, Aletta."
    mike.say "Nobody else was supposed to know!"
    "Audrey suddenly gasps, doing her best to look embarrassed and ashamed of herself."
    show audrey surprised
    audrey.say "Oh, I'm SO sorry, guys!"
    audrey.say "I just thought this was a great chance for us all to come out of the closet!"
    audrey.say "I mean, you won't tell, will you Aletta?"
    show aletta normal blush
    aletta.say "I...I couldn't say..."
    audrey.say "You could even join in - couldn't she, [hero.name]?"
    show lavish normal
    show shiori normal
    show audrey normal
    show aletta normal
    "Suddenly all attention is on me, four pairs of eyes burning into my brain."
    show lavish angry
    lavish.say "Are you going to let her do that, [hero.name]?"
    show shiori surprised
    shiori.say "What's happening, [hero.name]?"
    shiori.say "I'm scared!"
    "I try to think straight, to tune out their voices."
    "There's already four of us in this relationship."
    "Is there really room for one more?"
    "But then, what's the difference between four and five?"
    "And Aletta's sure to keep it quiet once she's on board too."
    mike.say "I'm cool with it if you are, Aletta."
    mike.say "And it could make you more efficient too."
    mike.say "If you ask me, it's a win-win situation!"
    show lavish normal
    show audrey normal
    show shiori normal
    "I can almost see gears turning in Aletta's mind."
    "I just hope they're turning in the right direction..."
    if aletta.love >= 140 and aletta.sub >= 25:
        show aletta flirt
        aletta.say "Y...you are technically correct."
        aletta.say "And that's the best kind of correct there is..."
        "Aletta looks down at the table for a moment."
        "She seems to be gathering her strength to say something."
        aletta.say "Okay, [hero.name]."
        aletta.say "I'll try it."
        show aletta happy at mostright4 with move
        aletta.say "I want in on the action."
        "Audrey screws up her face and puts hand to her ear."
        show audrey flirt at right4 with move
        audrey.say "Ah, what was that, Aletta?"
        show lavish flirt at mostleft4 with move
        lavish.say "I don't think I heard you clearly either..."
        show shiori flirt at left4 with move
        shiori.say "He, he...yeah, Aletta - speak up!"
        "Aletta groans as she's put through the mill by the other girls."
        "But there seems to be no way out of it for her."
        "No way other than to give them what they want."
        show aletta annoyed
        aletta.say "Urgh...how childish!"
        aletta.say "Alright, I'll say it..."
        aletta.say "I want to become part of your relationship."
        show aletta normal blush
        aletta.say "If you'll please have me?"
        show audrey happy
        audrey.say "Yeah, Aletta - we can squeeze in a little one!"
        show lavish happy
        lavish.say "Welcome aboard - you'll love it."
        show shiori happy
        shiori.say "[hero.name] is okay with it, so I am too!"
        mike.say "So it's agreed then?"
        mike.say "Aletta's in."
        mike.say "And we're officially what - a fivesome?"
        "Aletta shakes her head at this."
        aletta.say "Don't try to overthink it, [hero.name]."
        aletta.say "You'll only end up hurting yourself!"
        "All four of them burst into laughter at my expense."
        "And I can't help hoping that this isn't the shape of things to come!"
        $ game.flags.officeharemfivedelay = TemporaryFlag(True, 1)
        $ Harem.join_by_name("office", "aletta")
    else:
        show aletta normal -blush
        aletta.say "No, I couldn't possibly do that."
        aletta.say "It...it wouldn't be efficient."
        show lavish sad -blush
        "Lavish screws her face up and cocks her head on one side."
        "It looks like she's not convinced by Aletta's explanation."
        lavish.say "But, I thought you were all about productivity, Aletta?"
        lavish.say "I've certainly found that it's got me more motivated."
        show shiori sad -blush
        "Shiori leans in closer to me, like she's looking for protection."
        shiori.say "Maybe she thinks she's too good for the likes of us?"
        shiori.say "Don't listen to her, [hero.name]."
        shiori.say "It's you that's too good for her!"
        show audrey annoyed -blush
        "Audrey shakes her head, as if she knows the answer."
        audrey.say "Nah, Shiori - that's not it."
        audrey.say "Aletta here doesn't like to share."
        audrey.say "She wants to be the alpha bitch!"
        "At this, Aletta stands up shakes her head."
        show aletta angry at startle
        aletta.say "I...I've never heard such rubbish."
        aletta.say "This discussion is over - OVER!"
        aletta.say "I should report all of you to HR!"
        mike.say "Ah, Aletta..."
        mike.say "You said it yourself - polyamory is actually legal."
        show aletta embarrassed blush
        "Aletta's face flushes red with embarrassment."
        "Her mouth moves, but no words come out."
        "And then she turns on her heel and storms out of the meeting room."
        hide aletta with moveoutright
        "All I can do is shrug at the others."
        mike.say "With a temper like that, maybe we're better off without her?"
        $ aletta.love -= 5
        $ aletta.sub -= 2
    return

label office_aletta_audrey_lavish_shiori_01:
    "The last thing that I needed this morning was another damn meeting."
    "But there it was, staring me in the face when I checked my schedule."
    "I'm sitting in one of the seats around the table, clutching my coffee."
    "And as the others start to file in, I can see they feel the same way too."
    show audrey frown at mostleft4 with moveinleft
    "Audrey stalks into the room with a face like thunder."
    "She doesn't say a word, just grumbles and mutters under her breath."
    show shiori sad at left
    show audrey at center
    with moveinleft
    "Shiori hurries in looking tired and more than a little harassed."
    show shiori normal
    show audrey work annoyed zorder 2 at center, zoomAt(1, (700, 840)) with ease
    "But she still remembers her manners and forces a smile onto her face."
    shiori.say "Oh..."
    shiori.say "Good morning, [hero.name]."
    mike.say "Morning, Shiori."
    "Even this short greeting is enough to cheer Shiori up."
    show shiori work zorder 66 at center, zoomAt(1, (440, 840)) with ease
    "And she happily chooses a seat as close to me as possible."
    show lavish normal at left with easeinleft
    "Lavish walks in looking efficient and ready for the meeting."
    "But even she looks a little tired underneath her usual professional demeanour."
    show lavish work zorder 1 at center, zoomAt(1, (180, 840)) with ease
    lavish.say "Good morning everyone."
    lavish.say "Do any of you know what this meeting is about?"
    "Everyone exchanges glances and then we all begin to shrug."
    mike.say "I have no idea, Lavish."
    shiori.say "Erm...I don't know either, Lavish."
    shiori.say "Sorry!"
    show audrey annoyed
    audrey.say "It's about torturing us, obviously!"
    audrey.say "What else?!?"
    aletta.say "Ah, you're all present and accounted for - that's good."
    "Everyone looks up and turns their heads towards the new voice."
    show aletta a normal at center, zoomAt(1, (1180, 740)) with dissolve
    "And standing there, framed in the doorway, is Aletta."
    "She has her hands on her hips and looks ready for anything."
    mike.say "Ah..."
    mike.say "Hey, Aletta."
    mike.say "So you're the one that called this meeting?"
    show aletta a normal at top_mostright with ease
    "Aletta strides into the room, letting the door close behind her."
    "She stops at the head of the table, assuming a commanding position."
    aletta.say "Of course I was."
    aletta.say "But I wouldn't call this a meeting."
    show aletta annoyed
    aletta.say "That makes it sound so formal!"
    mike.say "I don't know what you mean, Aletta."
    mike.say "If this isn't a meeting, then what is it, exactly?"
    show aletta embarrassed
    aletta.say "I thought that we discussed this in the last actual meeting?"
    aletta.say "Me getting involved in your sordid little relationship?"
    "I glance around at the others, stunned by what Aletta just said."
    "And I can see that their reactions are pretty much the same."
    show shiori surprised at startle
    shiori.say "You mean..."
    show lavish surprised at startle
    lavish.say "You called us all here..."
    show audrey surprised at startle
    audrey.say "To have SEX?!?"
    show aletta normal
    "Aletta raises a quizzical eyebrow at this."
    show aletta annoyed
    aletta.say "I have to say that I'm disappointed with your lack of enthusiasm."
    aletta.say "I was told that this would help achieve a boost to my productivity levels."
    show aletta normal
    aletta.say "So why wouldn't I approach it like any other activity that does the same thing?"
    mike.say "Erm..."
    mike.say "Maybe because it's supposed to be fun too?"
    show aletta annoyed
    "Aletta sniffs haughtily as she turns her attention to me."
    aletta.say "Well, that has yet to be seen."
    aletta.say "So what are you all waiting for?"
    aletta.say "Let's get our clothes off and get on with it!"
    "I nod and begin to do as Aletta demands."
    "Not because I like her being in charge, you understand."
    "More because I want to show willing and do all I can to make this thing work."
    "Slowly, Audrey, Lavish and Shiori start to follow my lead."
    show aletta b naked flirt blush at right
    show audrey b naked flirt blush at right4
    show lavish b naked flirt blush at left
    show shiori b naked flirt blush at left4
    with ease
    "But once we're all undressed and ready to go, I feel it's time to act."
    "And so I step up and reach out for the girl that I have in mind."
    "This is one thing that I'm not going to let Aletta dictate!"
    call office_aletta_audrey_lavish_shiori_fuck from _call_office_aletta_audrey_lavish_shiori_fuck
    return

label office_aletta_audrey_lavish_shiori_fuck:
    menu:
        "Fuck Aletta":
            call office_fivesome_alettafuck_audrey_lavish_shiori from _call_office_fivesome_alettafuck_audrey_lavish_shiori
        "Fuck Audrey":
            call office_fivesome_audreyfuck_aletta_lavish_shiori from _call_office_fivesome_audreyfuck_aletta_lavish_shiori
        "Fuck Lavish":
            call office_fivesome_lavishfuck_aletta_audrey_shiori from _call_office_fivesome_lavishfuck_aletta_audrey_shiori
        "Fuck Shiori":
            call office_fivesome_shiorifuck_aletta_audrey_lavish from _call_office_fivesome_shiorifuck_aletta_audrey_lavish
    if renpy.has_label("office_harem_achievement_2") and not game.flags.cheat:
        call office_harem_achievement_2 from _call_office_harem_achievement_2
    $ game.pass_time(2)
    $ hero.cancel_activity()
    return

label office_fivesome_alettafuck_audrey_lavish_shiori:
    "The last thing that I want to do right now is put Aletta in charge."
    "I know full well that she likes to be the alpha bitch in any given situation."
    "And I might have been tempted to let her take the lead with the other girls."
    "But I certainly don't want her getting the upper hand on me too!"
    "The obvious thing would be to choose Audrey, Lavish or Shiori over her."
    "But maybe the best thing here would be to use some reverse psychology?"
    mike.say "This is Aletta's first time."
    mike.say "So I think she should be the one that gets to take a ride."
    "Lavish and Shiori are quick to nod in agreement."
    show lavish normal
    lavish.say "I'm okay with that."
    show shiori normal
    shiori.say "Sure thing, [hero.name]."
    show audrey annoyed
    "But I see the signs of protest on Audrey's face."
    "In response, I look at her with wide eyes and shake my head."
    "Luckily for me, she seems to get the message and backs down."
    audrey.say "Whatever..."
    show audrey normal
    "Aletta seems too preoccupied to pick up on those vibes."
    "And she simply accepts the invitation as if it were inevitable."
    aletta.say "Of course, [hero.name]."
    aletta.say "It makes perfect sense that I should be front and centre."
    aletta.say "We should start as we mean to go on."
    "I give Aletta a smile and a nod."
    "But the whole time I'm trying to keep a straight face."
    "If this works out the way I'm planning, she'll soon be eating those words!"
    "I lie down on my back, feeling the plush pile of the carpet beneath me."
    "And then I beckon for Aletta to join me."
    "She doesn't hesitate for a moment, striding over with confidence."
    scene office fivesome alettafuck audrey lavish shiori with fade
    "Aletta lowers herself down, straddling my thighs as she does so."
    "Of course my cock is already good and hard by now."
    "How could it not be when I'm surrounded by four hot, naked girls?"
    "And Aletta can't help eyeing it up even as she tries to look superior."
    "Audrey, Lavish and Shiori gather to each side of us."
    "For now they seem content to simply watch."
    "But I suspect that they're ready to jump in at a moment's notice."
    "Now that everyone's in place, I have a decision to make."
    "And that's exactly where I'm going to put it..."
    menu:
        "Fuck her ass":
            $ aletta.sub += 2
            "I've been careful to make it look like Aletta is the one in charge here."
            "And so far it seems that she's been getting exactly what she wants."
            "But now I sense that it's time for me to put my actual plan into action."
            "Which is why I turn my head and catch Audrey's eye."
            "I don't say anything out loud."
            "But instead I mouth the word 'ass' to her."
            "And when I see a wicked grin spread across her face, I know Audrey is on board."
            "Playing it straight, I rub the head of my cock against Aletta's pussy."
            "She moans at the sensation, closing her eyes to better savour it."
            "As soon as she does so, I aim my cock between her legs and part her buttocks."
            "Aletta's eyes snap open, and she lets out a wail of alarm."
            aletta.say "[hero.name]..."
            aletta.say "What's going on?!?"
            aletta.say "What are you..."
            "Before Aletta can move a muscle, Audrey and the others step in."
            "They don't take hold of her in an obvious manner."
            "Instead they support her as if she were in danger of toppling over."
            "But the effect is much the same, pinning Aletta down."
            "I take full advantage of the opportunity they've given me."
            show office fivesome alettafuck audrey lavish shiori anal
            "And I thrust the head of my cock into Aletta's ass."
            aletta.say "Oh shit..."
            aletta.say "Oh shit..."
            aletta.say "Oooh...my...god!"
            "At the same time as her muscles surrender, so does Aletta."
            "Her protests melt into moans of pleasure as she sinks down on my cock."
            "And what makes it that much better is the fact that she's flushed red."
            "Embarrassment is written all over her face as she takes it."
            "But there's nothing that she can do to hide how much she's loving it too!"
            "It's not long before the others are able to let go of Aletta."
            "She's riding my cock so hard by now that I doubt they could pull her off if they tried!"
            "And so they each put their hands to better use, touching and caressing her all over."
            show office fivesome alettafuck audrey lavish shiori pleasure
            "Aletta's so consumed by the feeling of my cock inside her that she doesn't object."
            "But I can see the blush is still on her cheeks as the other girls play with her."
            "The thing is that she's not the only one more interested in the main show."
            "And as much as it's a turn-on to see them at work, I'm drawn back to Aletta."
            "Pretty soon Audrey, Lavish and Shiori have faded into the background."
            "All I can do is look up at Aletta, watching her ride me."
            "I can feel myself getting closer to cumming every second."
            "And then it happens..."
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori
            else:
                menu:
                    "Cum inside":
                        "With one final thrust, I push as deep into Aletta as possible."
                        show office fivesome alettafuck audrey lavish shiori cum with vpunch
                        "She throws back her head as I cum inside of her, not holding anything back."
                        show office fivesome alettafuck audrey lavish shiori ahegao with vpunch
                        "Now Audrey, Lavish and Shiori have to hold her up for real."
                        "They support Aletta as she rides out the last moments."
                        "And then they lay her down on the ground, panting and spent."
                    "Pull out":
                        show office fivesome alettafuck audrey lavish shiori -anal -vaginal
                        "I use the last of my energy to pull my cock out of Aletta before it's too late."
                        "She makes a sound of vague protest at the sensation, throwing back her head."
                        show office fivesome alettafuck audrey lavish shiori ahegao
                        "Now Audrey, Lavish and Shiori have to hold her up for real."
                        "They support Aletta as she rides out the last moments."
                        show office fivesome alettafuck audrey lavish shiori cum with vpunch
                        "And all eyes are on her as the cum spatters down on her belly and breasts."
                        with vpunch
                        "And then they lay her down on the ground, panting and spent."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_1
            $ aletta.flags.anal += 1
        "Fuck her pussy":
            $ aletta.love += 4
            "I need to make it clear that Aletta's not the one in charge here."
            "But at the same time I have to make this fun for everyone involved too."
            "I can't make an example out of Aletta, or else what's the point of letting her in on this?"
            "I turn my head and catch Audrey's eye."
            "I don't say anything out loud."
            "But instead I mouth the words 'hold her'."
            "And when I see a wicked grin spread across her face, I know Audrey is on board."
            "I rub the head of my cock against Aletta's pussy."
            "She moans at the sensation, closing her eyes to better savour it."
            aletta.say "Ah..."
            aletta.say "That's good, [hero.name]..."
            aletta.say "You're doing well so far..."
            "Before Aletta can say another word, Audrey and the others step in."
            "They don't take hold of her in an obvious manner."
            "Instead they support her as if she were in danger of toppling over."
            "But the effect is much the same, keeping Aletta in place."
            "I take full advantage of the opportunity they've given me."
            "Pulling Aletta down and onto me, I push my cock into her pussy."
            show office fivesome alettafuck audrey lavish shiori vaginal
            aletta.say "Wha..."
            aletta.say "What are you..."
            aletta.say "Oh...oh my god!"
            "Aletta resists for no more than a few seconds."
            "And then I'm inside of her, sinking as deep as I can."
            "I see her cheeks flush red as this happens, note the embarrassment in her eyes."
            "Aletta wants to protest, to complain at the way the others are holding her."
            "But the problem is that she's enjoying herself too much!"
            "It's not long before the others are able to let go of Aletta."
            "She's riding my cock so hard by now that I doubt they could pull her off if they tried!"
            "And so they each put their hands to better use, touching and caressing her all over."
            show office fivesome alettafuck audrey lavish shiori pleasure
            "Aletta's so consumed by the feeling of my cock inside her that she doesn't object."
            "But I can see the blush is still on her cheeks as the other girls play with her."
            "The thing is that she's not the only one more interested in the main show."
            "And as much as it's a turn-on to see them at work, I'm drawn back to Aletta."
            "Pretty soon Audrey, Lavish and Shiori have faded into the background."
            "All I can do is look up at Aletta, watching her ride me."
            "I can feel myself getting closer to cumming every second."
            "And then it happens..."
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_2
            else:
                menu:
                    "Cum inside":
                        "With one final thrust, I push as deep into Aletta as possible."
                        show office fivesome alettafuck audrey lavish shiori cum with vpunch
                        "She throws back her head as I cum inside of her, not holding anything back."
                        show office fivesome alettafuck audrey lavish shiori ahegao with vpunch
                        "Now Audrey, Lavish and Shiori have to hold her up for real."
                        "They support Aletta as she rides out the last moments."
                        "And then they lay her down on the ground, panting and spent."
                    "Pull out":
                        show office fivesome alettafuck audrey lavish shiori -anal -vaginal
                        "I use the last of my energy to pull my cock out of Aletta before it's too late."
                        "She makes a sound of vague protest at the sensation, throwing back her head."
                        show office fivesome alettafuck audrey lavish shiori ahegao
                        "Now Audrey, Lavish and Shiori have to hold her up for real."
                        "They support Aletta as she rides out the last moments."
                        show office fivesome alettafuck audrey lavish shiori cum with vpunch
                        "And all eyes are on her as the cum spatters down on her belly and breasts."
                        with vpunch
                        "And then they lay her down on the ground, panting and spent."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_3
    $ aletta.sexperience += 1
    return

label office_fivesome_audreyfuck_aletta_lavish_shiori:
    "Maybe the best solution is to show Aletta that being a big mouth doesn't mean you're in charge?"
    "That way she can sit back and see how things play out, learn that we all play together."
    "Which means that the one I need to be making the centre of attention is Audrey."
    "After all, she's almost as forward and bossy as Aletta when she lets go."
    "And so I reach out and take hold of Audrey's hand."
    "A smile instantly spreads across her face, and she nods to the other girls."
    "And she offers no resistance whatsoever as I lay down on the floor."
    "Instead, Audrey all but pounces on me the moment I'm flat on my back!"
    scene office fivesome audreyfuck aletta lavish shiori
    audrey.say "This must be pretty weird - huh, Aletta?"
    audrey.say "Someone else giving the presentation?"
    audrey.say "Showing you how it's done?"
    "Aletta doesn't dignify Audrey's questions with a reply."
    "She simply snorts as if unimpressed and crosses her arms over her bare breasts."
    "Lavish and Shiori come closer, as if this is really becoming a presentation of some kind."
    "And now all three of them are leaning in, waiting to see what happens next."
    "Feeling a little under pressure all of a sudden, I try to get things moving."
    "And so I take a firm hold of Audrey's haunches and pull her downwards."
    "But the question occurs to me - just where am I going to put it?"
    menu:
        "Fuck her ass":
            $ audrey.sub += 2
            "What with Audrey opening her big mouth just now, I really can't resist the urge."
            "All I can think of is doing something that will pay her back and still be fun too."
            "Which is why I change the angle that my cock is pointing just enough..."
            "And then it slips between her buttocks neatly and without her even noticing."
            "The fist thing that Audrey knows about it is the sensation of the head pressing on her ass."
            audrey.say "Hey..."
            audrey.say "What gives?!?"
            audrey.say "Nobody said anything about..."
            "I use the brief moment in which she's caught off-guard to my advantage."
            "All it takes is one sharp thrust, and we're in business."
            "Audrey lets out a cry of surprise as she feels me push into her ass."
            "But by that time it's too late for her to do anything but surrender."
            audrey.say "Oh you..."
            audrey.say "My...my ass..."
            audrey.say "Mmm...my ass..."
            "All that Audrey can do is brace herself and hold on for the ride."
            "And as I start to move inside of her, it only becomes more intense."
            "Soon enough she's literally clinging onto me for dear life."
            show office fivesome audreyfuck aletta lavish shiori pleasure
            "All of which makes me pick up speed as soon as I'm able."
            "I can't help enjoying the sight of Audrey in the grip of such sensations."
            "The more she shakes and tosses her head, the more effort I expend."
            "I'm so engrossed in Audrey that I had completely forgotten about the others."
            "But then I see Aletta leaning in a little closer than before."
            "Her air of authority is so natural and complete that Lavish and Shiori follow her lead."
            "Aletta reaches out to touch Audrey, caressing her breasts as she bounces up and down."
            "There's nothing that Audrey can do about it."
            "And she's too preoccupied to object with a single word."
            "So all she can do is watch as Lavish and Shiori join in too."
            "By now all three of the other girls are playing with Audrey."
            "And I can see that her cheeks are flushing with embarrassment as a result."
            "None of it is enough to make me slow down the pace."
            "It's actually making me work that much harder as I pound away at her!"
            "But the final moment of Audrey's humiliation comes when Aletta holds up her phone."
            "I don't know if she's filming us or taking photos, and I really don't care."
            "It's Audrey that seems to be more affected by this turn of events."
            "And when Lavish and Shiori again take their cue from Aletta, her cheeks begin to turn crimson."
            "The effect on me is quite different, and I get a genuine thrill from watching."
            "There's nothing Audrey can do to escape, my hands holding her firmly."
            "And my grip becomes firmer still as I feel myself starting to cum..."
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_4
            else:
                menu:
                    "Cum inside":
                        with vpunch
                        "I shoot my load into Audrey to the sound of camera's clicking."
                        show office fivesome audreyfuck aletta lavish shiori ahegao with vpunch
                        "The experience is made that much more intense as she turns this way and that."
                        with vpunch
                        "Only when I'm utterly spent do I loosen my grip on her."
                        "And once I'm no longer holding her up, Audrey slides off of me onto the floor."
                        "She lies there as the others continue to take photos, her chest rising and falling the whole time."
                    "Pull out":
                        "I lift Audrey up, just enough to let my cock slip out of her."
                        with vpunch
                        "Then I shoot my load over her belly and breasts."
                        with vpunch
                        "The cum spatters over her in thick, sticky streamers."
                        "And the others keep on snapping photos the whole time."
                        "Only when I'm utterly spent do I loosen my grip on her."
                        show office fivesome audreyfuck aletta lavish shiori ahegao
                        "And once I'm no longer holding her up, Audrey slides off of me onto the floor."
                        "She lies there, her chest rising and falling."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_5
            $ audrey.flags.anal += 1
        "Fuck her pussy":
            $ audrey.love += 4
            "There's no reason to beat around the bush - if you'll pardon the pun."
            "As it looks like Audrey is more than ready to get down to business."
            "And so I don't waste any time in pushing the head of my cock against her pussy."
            "Audrey giggles in delight, and then looks down at me."
            "She bites her lip and her eyes close slowly, betraying all that she's feeling."
            "There's no more than a token of resistance, and then I'm inside of her."
            "And she sinks down slowly, taking me into her an inch at a time."
            audrey.say "Mmm..."
            audrey.say "That feels so good..."
            audrey.say "I love having you inside of me..."
            "As much as I wanted to make this about all of us, Audrey has be fixated on her."
            "The sight of her as she begins to ride my cock."
            "That and the sensation of her squeezing it as she does so..."
            "All of it means that I can't help but give her all of my attention."
            "Soon Audrey starts to pick up speed."
            "And then she's almost leaping up and down in my lap."
            show office fivesome audreyfuck aletta lavish shiori pleasure
            audrey.say "Oh...you're..."
            audrey.say "You're so big..."
            audrey.say "You're too much for me!"
            "And when she's talking about me like that - can you blame me?!?"
            "I'm so engrossed in Audrey that I had completely forgotten about the others."
            "But then I see Aletta leaning in a little closer than before."
            "Her air of authority is so natural and complete that Lavish and Shiori follow her lead."
            "Aletta reaches out to touch Audrey, caressing her breasts as she bounces up and down."
            "There's nothing that Audrey can do about it."
            "And she's too preoccupied to object with a single word."
            "So all she can do is watch as Lavish and Shiori join in too."
            "By now all three of the other girls are playing with Audrey."
            "And I can see that her cheeks are flushing with embarrassment as a result."
            "None of it is enough to make me slow down the pace."
            "It's actually making me work that much harder as I pound away at her!"
            "But the final moment of Audrey's humiliation comes when Aletta holds up her phone."
            "I don't know if she's filming us or taking photos, and I really don't care."
            "It's Audrey that seems to be more affected by this turn of events."
            "And when Lavish and Shiori again take their cue from Aletta, her cheeks begin to turn crimson."
            "The effect on me is quite different, and I get a genuine thrill from watching."
            "There's nothing Audrey can do to escape, my hands holding her firmly."
            "And my grip becomes firmer still as I feel myself starting to cum..."
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_6
            else:
                menu:
                    "Cum inside":
                        with vpunch
                        "I shoot my load into Audrey to the sound of camera's clicking."
                        show office fivesome audreyfuck aletta lavish shiori ahegao with vpunch
                        "The experience is made that much more intense as she turns this way and that."
                        with vpunch
                        "Only when I'm utterly spent do I loosen my grip on her."
                        "And once I'm no longer holding her up, Audrey slides off of me onto the floor."
                        "She lies there as the others continue to take photos, her chest rising and falling the whole time."
                    "Pull out":
                        "I lift Audrey up, just enough to let my cock slip out of her."
                        with vpunch
                        "Then I shoot my load over her belly and breasts."
                        show office fivesome audreyfuck aletta lavish shiori ahegao with vpunch
                        "The cum spatters over her in thick, sticky streamers."
                        "And the others keep on snapping photos the whole time."
                        "Only when I'm utterly spent do I loosen my grip on her."
                        "And once I'm no longer holding her up, Audrey slides off of me onto the floor."
                        "She lies there, her chest rising and falling."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_7
    $ audrey.sexperience += 1
    return

label office_fivesome_lavishfuck_aletta_audrey_shiori:
    "Choosing Aletta seems wrong on her first time with the rest of us."
    "Choosing Audrey is pretty much like putting her in charge of the whole thing."
    "And choosing Shiori would feel like throwing her to the lions!"
    "Which is why my mind is made up as soon as my gaze falls on Lavish."
    "For a moment I feel kind of guilty - like she's the default choice."
    "But then my eyes travel downwards from her face and back up again."
    "Whoa...that's quite a package!"
    "There's no way that Lavish could ever be the last option."
    "I can feel my cock getting hard just looking at her!"
    "Lavish can't help but notice the way that I'm sizing her up."
    show lavish blush normal
    "And she gives me a demure smile while looking away."
    lavish.say "[hero.name]..."
    lavish.say "Why are you looking at me like that?"
    "Aletta and Audrey both let out a snort of laughter at this."
    "And even Shiori seems puzzled by Lavish's apparent naivety."
    audrey.say "Because you're gonna be the star of the show, Lavish!"
    aletta.say "Unless you don't think that you can handle the pressure?"
    "Lavish stares at Aletta and Audrey for a moment."
    show lavish flirt
    "But then I see her jaw tighten and a look of resolve fill her eyes."
    "She reaches out and takes hold of my hand."
    "Which is as good as saying that she's ready to go!"
    hide lavish
    hide aletta
    hide audrey
    hide shiori
    show office fivesome lavishfuck aletta audrey shiori lookdown
    with fade
    "I start to lower myself onto the floor, guiding Lavish down with me."
    "But she surprises me by pushing faster and with more force."
    "This means that I land on the floor with Lavish atop me."
    "I hear myself gasp as she grabs hold of my cock, squeezing it hard."
    mike.say "Whoa..."
    mike.say "Hold on there, Lavish!"
    "But it's like she can't hear me at all."
    "Lavish clambers over me, still holding onto my dick."
    "She's obviously got something to prove to me and the others."
    "And probably to herself as well!"
    audrey.say "You go get it, Lavish!"
    shiori.say "Oh dear - please don't hurt [hero.name]!"
    show office fivesome lavishfuck aletta audrey shiori halfchub lookdown
    aletta.say "Hmm..."
    aletta.say "Someone's quite the little go-getter!"
    "I struggle to regain some measure of control as Lavish mounts me."
    "She's already aiming my cock between her legs."
    show office fivesome lavishfuck aletta audrey shiori outside lookdown
    "And I realise that if I don't assert myself soon, I'm just a passenger along for the ride!"
    "So as she comes ever closer to steering me home, I resolve to take action."
    "It's going to go inside of Lavish, that's for sure."
    "But I'm going to be the one to choose exactly where it goes..."
    menu:
        "Fuck her ass":
            "I'm feeling the need to get back a measure of control here."
            "And so I resolve to give Lavish exactly what she wants."
            "Only just not in the place where she's expecting to get it."
            "All it takes is a slight shift in my position, and then I'm ready."
            "Without hesitating, I pull Lavish down and onto my cock."
            show office fivesome lavishfuck aletta audrey shiori anal pleasure
            $ lavish.sub += 2
            "And my cock begins to push straight into her ass."
            "I see her eyes go wide the second she realises what's going on."
            lavish.say "Oh..."
            lavish.say "Oooh..."
            lavish.say "My...my ass!"
            "She tries to raise herself up."
            "But all of a sudden, Aletta and Audrey are on either side of her."
            "All smiles of encouragement, they gently push her back down again."
            show office fivesome lavishfuck aletta audrey shiori lookdown
            lavish.say "What are you..."
            lavish.say "Oh my god...don't..."
            lavish.say "Mmm...don't stop!"
            "Now I can feel the motion of Lavish's body change completely."
            "Where before she was resisting, she now surrenders herself willingly."
            "The muscles around my cock are no exception, melting as she sinks downwards."
            "Now that we're both on the same page, the pace begins to quicken."
            "Lavish is riding my cock with more passion with each second that passes."
            "And I'm thrusting in and out of her with as much vigour too."
        "Fuck her pussy":
            "I figure that setting the pace is a good way to assert myself."
            "And so I waste no time on pulling Lavish down and onto my cock."
            "Her pussy is already slick and slippery as I feel it against the head."
            "So there's nothing to stop me from pushing my way inside of her."
            show office fivesome lavishfuck aletta audrey shiori vaginal pleasure
            $ lavish.love += 2
            "Lavish moans as her lips part slowly, letting me slide in there."
            lavish.say "Oh yeah..."
            lavish.say "That's it..."
            lavish.say "That's what I want!"
            "Aletta and Audrey lean in close, eager to watch the show."
            "Shiori hesitates for a moment, but then comes closer too."
            "Even she seems to be fascinated by the sight of Lavish succumbing to her desires."
            lavish.say "Oh shit..."
            lavish.say "[hero.name]..."
            show office fivesome lavishfuck aletta audrey shiori lookdown
            lavish.say "More...I want more..."
            "I feel the motion of Lavish's body change as she makes this plea."
            "She seems to bear down on me from above, pressing her weight onto me."
            "Before she was happy to let me set the pace, to let me fuck her."
            "But now she's riding me like her life depends on it!"
            show office fivesome lavishfuck aletta audrey shiori pleasure
            "Suddenly it's not about me setting the pace at all."
            "Lavish is threatening to leave me standing."
            "And I have to up my game in order to give her what she wants!"
    "I try as best I can to match the energy that Lavish is putting into it."
    "But it doesn't take long before I can feel the sweat standing out on my forehead."
    show office fivesome lavishfuck aletta audrey shiori insert
    "The more effort I put into thrusting in and out of Lavish, the more she seems to want!"
    "Everything that I give her is soaked up like water into a sponge."
    "And the whole time that I'm inside of her she's asking for more."
    "I catch glimpses of Aletta, Audrey and Shiori out of the corner of my eye."
    "And they seems to be as fascinated and turned-on as I am."
    "Shiori reaches out to stroke Lavish's breasts."
    "And Aletta and Audrey seem to have put aside their differences for the moment."
    "They watch Lavish as they play with each other almost as an afterthought."
    "I try to ignore the distraction and focus my attentions solely on Lavish."
    "And then I begin to realise what's pushing her so hard right now."
    "Lavish arches her back and begins to moan like never before."
    "It's like she's gathering all of her energy for something big."
    "And then she cums, clinging to me as if for dear life!"
    "There's no way that I can ride it out."
    "Lavish squeezes my own climax out of me, right there and then!"
    if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_8
    else:
        menu:
            "Cum inside":
                "There's no time to even think about pulling out."
                $ lavish.love += 4
                show office fivesome lavishfuck aletta audrey shiori ahegao creampie with vpunch
                "And so I fill Lavish with everything that I have a moment later."
                with vpunch
                "I don't think I could be any deeper inside of her."
                "Which means that she takes everything that I have to give."
                "Lavish sways above me, reeling from the effects of both orgasms."
                "And then she collapses onto me, a mess of limp muscles and sweaty limbs."
            "Pull out":
                show office fivesome lavishfuck aletta audrey shiori lookdown outside
                "In a feat worthy of Houdini, I somehow manage to pull out."
                "Lavish writhes in my grasp, trying to climb back on."
                show office fivesome lavishfuck aletta audrey shiori pleasure cumshot with vpunch
                "But as she does so, I shoot my load over her."
                $ lavish.love += 4
                show office fivesome lavishfuck aletta audrey shiori pleasure flaccid dickcum cum onbody with vpunch
                "The cum hits her breasts and belly, running over my hands too."
                "And this makes it harder than ever to hold onto her."
                "Lavish sways above me, still reeling from the effects of her orgasm."
                "And then she collapses onto me, a mess of limp muscles and sweaty limbs."
            "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_9
    $ lavish.sexperience += 1
    return

label office_fivesome_shiorifuck_aletta_audrey_lavish:
    "I want to be into this thing like crazy, ready and raring to go."
    "I mean, who wouldn't want to be doing this with three hot girls?"
    "But there's a part of me that just can't keep worrying about Shiori."
    "Audrey's cocky and Lavish is quietly confident, even in the face of a foursome."
    "But Shiori still looks nervous as hell at the prospect of what lies ahead."
    "I can't help wanting to make it all okay for her, to protect her."
    "And so it's a no-brainer that I reach out and take hold of her hand."
    show shiori normal
    "Shiori yelps and jumps a little as I do so, betraying her nerves."
    shiori.say "Ooh!"
    shiori.say "Oh...I'm sorry, [hero.name]."
    shiori.say "You made me jump!"
    "I smile at her apology, shaking my head a little."
    "She's so sweet and innocent that I can't help giving her all of my attention."
    mike.say "It's okay, Shiori."
    mike.say "Just come over here with me, okay?"
    show shiori blush
    "Shiori nods at this, her huge eyes fixed upon me."
    "And she doesn't take them off of me for a moment as I lead her over to the sofa."
    "I'm only vaguely aware of Audrey and Lavish following us over there too."
    "They hold back as I sit down and Guide Shiori onto my lap."
    scene office fivesome shiorifuck aletta audrey lavish with fade
    "She smiles at first, still holding my eye."
    "But then she feels something brush against her and looks down."
    "Which means that she's staring straight at the tip of my cock!"
    shiori.say "Oh, [hero.name]!"
    shiori.say "It's...so big!"
    shiori.say "Is it all for me?"
    "How can she be so humble and innocent?"
    "Is it all just an act?"
    "She's as cute as hell, with a body that kills me just to look at it."
    "How can she not know that she makes me this hard without even trying?!?"
    mike.say "It's all your's, Shiori."
    mike.say "If you'll let me give it to you?"
    "Shiori's cheeks blush with colour at this."
    "And she covers her mouth to stifle a giggle."
    shiori.say "Okay, [hero.name]."
    shiori.say "I'll try my best - I promise!"
    "With that, Shiori guides my hands to her waist."
    "And then she puts her own hands on my shoulders."
    "She looks down on me with a smile, literally putting herself in my hands..."
    menu:
        "Fuck her ass" if shiori.flags.anal:
            "Maybe it sounds odd, but my first instinct is to part Shiori's buttocks."
            $ shiori.sub += 1
            show office fivesome shiorifuck aletta audrey lavish anal
            "And once they're spread nice and wide, I aim my cock straight for her ass."
            "Sure, it might sound like an odd thing to do when she's so nervous."
            "But I figure the best thing is to make Shiori face her fears."
            "Plus, it makes the whole thing that much more fun for me too!"
            shiori.say "Ah..."
            shiori.say "Erm...[hero.name]..."
            shiori.say "I think you're a little lost!"
            "By way of answer, I pull Shiori down and onto me."
            "The movement is sudden and unexpected, taking her by surprise."
            "And before she knows it, I'm already too deep into her ass to stop."
            shiori.say "Oooh..."
            shiori.say "Oh, [hero.name], what are you doing to me?!?"
            "Shiori wriggles in my lap, her huge breasts quivering."
            "But all she manages to do is sink further down and onto my cock."
            shiori.say "Oh...oh my..."
            shiori.say "You're so wicked...so wicked..."
            "Shiori can call me wicked all she wants."
            "But I note that she doesn't once ask me to stop!"
            "I begin to thrust in and out of Shiori."
            "I go slowly at first, but soon begin to pick up speed."
            "And she matches me every step of the way."
            "At first, Shiori is meek and almost quiet as she rides my cock."
            "But as I pick up the pace, she becomes ever more animated."
            "Soon enough there's nothing she can do to keep herself contained."
            "And she's bucking in my lap, bouncing up and down the whole time."
            "All I can do is stare up at her, almost hypnotised by the look on her face."
            "Shiori seems to be almost in a trance, lost in the moment."
            show office fivesome shiorifuck aletta audrey lavish ahegao
            "But then, without warning, her eyes burst open and her so does her mouth!"
            shiori.say "Ow..."
            shiori.say "Ooh..."
            shiori.say "Who did that?!?"
            show office fivesome shiorifuck aletta audrey lavish pleasure
            "Shiori and I are both looking around now."
            "Both trying to figure out what's going on."
            "It's then that I spot Audrey to one side and Lavish to the other."
            "They're crouched down around Shiori's ass, mischievous faces smiling back at me."
            "I watch as they playfully bite and lick at the other girl's buttocks."
            shiori.say "Hey..."
            shiori.say "No..."
            shiori.say "Stop that, right now!"
            "I might have said something myself too."
            "Though I can't say that it'd have been to tell them to stop!"
            "But Shiori's wriggling and squirming on top of me right now."
            "I can tell that she's just trying to avoid Audrey and Lavish."
            "But it's having a very different effect on me!"
            "Shiori bounces up and down on my cock, all of her weight squeezing me."
            "I can't hold it in any longer."
            "She's going to make me cum!"
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_10
            else:
                menu:
                    "Cum inside":
                        "Even if I wanted to pull out of Shiori, she's making it all but impossible."
                        $ shiori.sub += 2
                        show office fivesome shiorifuck aletta audrey lavish ahegao creampie with vpunch
                        "And at the very moment I shoot my load, she pushes all her weight down on me."
                        with vpunch
                        "This means that I'm as deep inside of her as I can go when I cum."
                        "Shiori let's out a wail at the sensation, grinding herself against me."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Pull out":
                        "I wait until the moment Shiori's in just the right place..."
                        show office fivesome shiorifuck aletta audrey lavish ahegao cumshot with vpunch
                        "And then I pull my cock out of her in one smooth motion."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        with vpunch
                        "Shiori wails as I shoot my load."
                        $ shiori.love += 4
                        show office fivesome shiorifuck aletta audrey lavish ahegao cum onbody with vpunch
                        "It hits her belly and the underside of her heavy breasts."
                        "But thanks to them being so large, it can't reach any higher."
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_11
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "I'm not about to change direction and shock Shiori now."
            $ shiori.love += 2
            show office fivesome shiorifuck aletta audrey lavish vaginal
            "And so I gently guide her down and onto my cock."
            "She pants and then bites her lip as it slides along her pussy."
            "But the pants become a moan a few seconds later."
            "Because that's the moment I choose to pull her down and onto me."
            "There's a token of resistance from Shiori's body."
            "And then I'm inside of her for real."
            "She sinks down, taking the whole length of my cock."
            "She doesn't stop until I'm balls deep in her."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're so big!"
            shiori.say "You've filled me up!"
            "Shiori's smile is broad and looks completely genuine."
            "Her eyes are as wide as I've ever seen them right now."
            "She looks like having my cock inside of her is the greatest experience of her life!"
            "And that just makes me all the more determined to ensure that it really is."
            "I begin to thrust in and out of Shiori."
            "I go slowly at first, but soon begin to pick up speed."
            "And she matches me every step of the way."
            "At first, Shiori is meek and almost quiet as she rides my cock."
            "But as I pick up the pace, she becomes ever more animated."
            "Soon enough there's nothing she can do to keep herself contained."
            "And she's bucking in my lap, bouncing up and down the whole time."
            "All I can do is stare up at her, almost hypnotised by the look on her face."
            "Shiori seems to be almost in a trance, lost in the moment."
            show office fivesome shiorifuck aletta audrey lavish ahegao
            "But then, without warning, her eyes burst open and her so does her mouth!"
            shiori.say "Ow..."
            shiori.say "Ooh..."
            shiori.say "Who did that?!?"
            show office fivesome shiorifuck aletta audrey lavish pleasure
            "Shiori and I are both looking around now."
            "Both trying to figure out what's going on."
            "It's then that I spot Audrey to one side and Lavish to the other."
            "They're crouched down around Shiori's ass, mischievous faces smiling back at me."
            "I watch as they playfully bite and lick at the other girl's buttocks."
            shiori.say "Hey..."
            shiori.say "No..."
            shiori.say "Stop that, right now!"
            "I might have said something myself too."
            "Though I can't say that it'd have been to tell them to stop!"
            "But Shiori's wriggling and squirming on top of me right now."
            "I can tell that she's just trying to avoid Audrey and Lavish."
            "But it's having a very different effect on me!"
            "Shiori bounces up and down on my cock, all of her weight squeezing me."
            "I can't hold it in any longer."
            "She's going to make me cum!"
            if hero.sexperience >= 50 and "office_fivesome_cumshare_aletta_audrey_lavish_shiori" not in DONE:
                call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_12
            else:
                menu:
                    "Cum inside":
                        "Even if I wanted to pull out of Shiori, she's making it all but impossible."
                        $ shiori.love += 4
                        show office fivesome shiorifuck aletta audrey lavish ahegao creampie with vpunch
                        "And at the very moment I shoot my load, she pushes all her weight down on me."
                        with vpunch
                        "This means that I'm as deep inside of her as I can go when I cum."
                        "Shiori let's out a wail at the sensation, grinding herself against me."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Pull out":
                        "I wait until the moment Shiori's in just the right place..."
                        show office fivesome shiorifuck aletta audrey lavish ahegao cumshot with vpunch
                        "And then I pull my cock out of her in one smooth motion."
                        shiori.say "Oh god..."
                        shiori.say "Oh, [hero.name]!"
                        with vpunch
                        "Shiori wails as I shoot my load."
                        $ shiori.love += 4
                        show office fivesome shiorifuck aletta audrey lavish ahegao cum onbody with vpunch
                        "It hits her belly and the underside of her heavy breasts."
                        "But thanks to them being so large, it can't reach any higher."
                        "Shiori arches her back for a moment, straining with her own orgasm."
                        "And then she collapses on top of me, panting and gasping for breath."
                    "Share the love" if "office_fivesome_cumshare_aletta_audrey_lavish_shiori" in DONE:
                        call office_fivesome_cumshare_aletta_audrey_lavish_shiori from _call_office_fivesome_cumshare_aletta_audrey_lavish_shiori_13
    $ shiori.sexperience += 1
    return

label office_fivesome_cumshare_aletta_audrey_lavish_shiori:
    "Before I have the chance to shoot my load, everyone else is suddenly in motion around me."
    "In the confusion, I can't tell if they're doing this naturally or if someone is directing traffic."
    show office fivesome cumshare aletta audrey lavish shiori dick onaudrey
    "Either way, the end result is the same, as the girls all crowd around my cock."
    "Aletta, Audrey, Lavish and Shiori all stare up at me, waiting patiently."
    show office fivesome cumshare aletta audrey lavish shiori dick fx onaudrey
    "Their mouths are open and their tongues are out."
    "It's at once a weird moment and a massive turn-on."
    "But I don't have more than a few seconds to contemplate the situation."
    $ cum_aletta = False
    $ cum_audrey = False
    $ cum_lavish = False
    $ cum_shiori = False
    $ maxcum = 4
    $ sentences = [
        "But I can't let [girlname] down. I'm taking every last bit of energy to give some to her.",
        "[girlname] is not to be outdone. I'm so turn on by the situation that I find myself cumming on her after a short moment.",
        "I find the energy to spray my seeds on [girlname]'s face too!",
        "I shoot my load a moment later!"]
    $ stored_attribute = ""
    while maxcum > 0 and hero.energy > 0:
        menu:
            "Cum on Aletta" if not cum_aletta:
                $ girlname = "Aletta"
                scene expression "office fivesome cumshare aletta audrey lavish shiori onaletta dick fx cumshot" + stored_attribute with hpunch
                $ renpy.say("",sentences.pop())
                $ stored_attribute += " cum_face_onaletta cum_mouth_onaletta"
                show expression "office fivesome cumshare aletta audrey lavish shiori onaletta dick" + stored_attribute
                $ aletta.love += 4
                if maxcum == 4:
                    "And I see it lands on Aletta's tongue!"
                "She almost purrs, like a cat that's got the cream."
                $ hero.energy -= 1
                $ maxcum -= 1
                $ cum_aletta = True
            "Cum on Audrey" if not cum_audrey:
                $ girlname = "Audrey"
                scene expression "office fivesome cumshare aletta audrey lavish shiori onaudrey dick fx cumshot" + stored_attribute with hpunch
                $ renpy.say("",sentences.pop())
                $ stored_attribute += " cum_face_onaudrey cum_mouth_onaudrey"
                show expression "office fivesome cumshare aletta audrey lavish shiori onaudrey dick" + stored_attribute
                $ audrey.love += 4
                if maxcum == 4:
                    "And I see it lands on Audrey's tongue!"
                "She uses her tongue to play with the thick liquid."
                $ hero.energy -= 1
                $ maxcum -= 1
                $ cum_audrey = True
            "Cum on Lavish" if not cum_lavish:
                $ girlname = "Lavish"
                scene expression "office fivesome cumshare aletta audrey lavish shiori onlavish dick fx cumshot" + stored_attribute with hpunch
                $ renpy.say("",sentences.pop())
                $ stored_attribute += " cum_face_onlavish cum_mouth_onlavish"
                show expression "office fivesome cumshare aletta audrey lavish shiori onlavish dick" + stored_attribute
                $ lavish.love += 4
                if maxcum == 4:
                    "And I see it lands on Lavish's tongue!"
                "She giggles as she lap at the cum."
                $ hero.energy -= 1
                $ maxcum -= 1
                $ cum_lavish = True
            "Cum on Shiori" if not cum_shiori:
                $ girlname = "Shiori"
                scene expression "office fivesome cumshare aletta audrey lavish shiori onshiori dick fx cumshot" + stored_attribute with hpunch
                $ renpy.say("",sentences.pop())
                $ stored_attribute += " cum_face_onshiori cum_mouth_onshiori"
                show expression "office fivesome cumshare aletta audrey lavish shiori onshiori dick" + stored_attribute
                $ shiori.love += 4
                if maxcum == 4:
                    "And I see it lands on Shiori's tongue!"
                "She lets out a little cry of alarm."
                $ hero.energy -= 1
                $ maxcum -= 1
                $ cum_shiori = True
    "All I can do is look on, panting and exhausted from my efforts."
    $ DONE["office_fivesome_cumshare_aletta_audrey_lavish_shiori"] = game.days_played
    return

label office_lavish_shiori_showdown:
    show lavish sad at left5
    show shiori sad at top_mostleft
    with moveinleft
    "As soon as I see Lavish and Shiori approaching, my imagination starts to run wild."
    "I mean, can you blame me for that?"
    "Even if we weren't fucking both of them at the same time."
    "And all I can think about is the stuff that I've gotten up to with them."
    "That and what we might get up to when the next chance comes our way."
    "It's only when they get closer that I begin to realise there's something wrong."
    show lavish angry at right4 with move
    "Lavish is striding towards me like she's about to go into battle."
    show shiori at left5 with ease
    "And Shiori seems to be trailing in her wake, eyes red and puffy from crying."
    "On their own, neither would be that unusual."
    "But together and converging on me, it's enough to make me start worrying."
    mike.say "Ah..."
    mike.say "Hey, Lavish...Shiori..."
    mike.say "Is there something the matter?"
    "Lavish comes to a halt in front of me."
    "She plants one hand on her hip."
    "And then she uses the other one to jab a finger at my face."
    lavish.say "You bet there's something the matter, Mister!"
    lavish.say "You've got some explaining to do, [hero.name]."
    "While I'm still reeling from that opening salvo, Shiori pipes up too."
    shiori.say "Oh, [hero.name]!"
    shiori.say "How could you do that to me?!?"
    shiori.say "I trusted you..."
    shiori.say "I thought you loved me!"
    "I take a step backwards, overwhelmed by an attack on two fronts."
    "My head is shaking, more from confusion than denial."
    "Neither of them has said what I'm supposed to have done."
    "But I'm beginning to form a pretty good guess at what it is."
    mike.say "W...wait a second..."
    mike.say "I...I can explain..."
    "Lavish shakes her head too."
    "She jabs her finger painfully into my chest."
    lavish.say "Oh no."
    lavish.say "No more talking from you."
    lavish.say "That's how we got tricked in the first place."
    show fx anger at right4
    lavish.say "And all the time you were screwing us behind the other's back!"
    shiori.say "Yes, that's right!"
    shiori.say "You tricked us both - cast a spell on us with words!"
    show lavish annoyed
    "Lavish turns away from me for a moment, rolling her eyes at Shiori."
    "She clearly wants to keep on target, focused on chewing me out."
    "And Shiori's drama isn't helping at all."
    lavish.say "Whatever, Shiori, whatever."
    show lavish angry
    lavish.say "Long and short of it is that I quit."
    lavish.say "I already tendered my resignation."
    lavish.say "And you should do the same, Shiori."
    "With that said, Lavish seems to consider the conversation over."
    "She turns on her heel with a snort of derision and begins to walk away."
    hide lavish with moveoutleft
    "Shiori doesn't seem to notice this at first."
    "Instead she stands there, staring at me in silence."
    "But then reality catches up with her, and she jumps in shock."
    "Without another word, she scurries after Lavish."
    hide shiori with easeoutleft
    "And just like that, I'm left standing there alone."
    "I have no idea how Lavish and Shiori found me out."
    "But I can be sure that we're already hot gossip around the office."
    "If I keep my head down and try to stay out of sight, maybe it'll blow over?"
    "Yeah, sure - maybe in a year or two!"
    $ lavish.love -= 20
    $ shiori.love -= 20
    $ lavish.set_gone_forever()
    return

label office_aletta_lavish_showdown:
    show aletta normal at left5
    show lavish normal at top_mostleft
    with moveinleft
    "Looking up I see Aletta and Lavish hurrying towards me."
    "The sight makes me crack a smile without even thinking about it."
    "After all, with two hot girls approaching, who wouldn't?"
    "Especially knowing that I'm fucking both of them!"
    "But as they come closer, the smile begins to fade from my lips."
    show aletta angry at right5
    show lavish angry at left5
    with ease
    "Aletta looks like she's on the warpath for some reason."
    "And Lavish seems to be channelling the same emotion too."
    "This can't be good."
    mike.say "Ah..."
    mike.say "Hey, girls..."
    mike.say "What's up?"
    "Aletta looks like she's about to speak."
    "But then, to her surprise and mine, Lavish leaps in first."
    show lavish at startle
    lavish.say "Don't 'hey girls' us, [hero.name]."
    lavish.say "Did you think we wouldn't find out?"
    lavish.say "Did you think you could keep on fooling us forever?!?"
    "I try as best I can to make my shock look like confusion."
    "But of course I know exactly what she's talking about."
    "And yeah, I did kind of hope that they'd never find out."
    aletta.say "You betrayed our trust, [hero.name]."
    aletta.say "You humiliated us in front of our colleagues."
    aletta.say "Sleeping with us both behind our backs - how could you?!?"
    "My lips move for a moment, no words coming out."
    "I could try to deny it all, call it a pack of lies."
    "But the pair of them look almost ready to commit violence."
    "Maybe a better idea would be to come clean?"
    "Sure, they might slap me or kick me in the balls."
    "But at least then there's a tiny chance of this blowing over, right?"
    mike.say "Okay, okay..."
    mike.say "I admit it."
    mike.say "But it's not like you make it sound!"
    show lavish angry at left5, vshake
    lavish.say "WHAT?"
    lavish.say "You're not even going to try and deny it?!?"
    mike.say "I...I..."
    "Aletta cuts me off before I can say another word."
    show aletta at startle
    if game.flags.isceo:
        aletta.say "No need to bullshit me, [hero.name]."
        aletta.say "I quit!"
        aletta.say "I refuse to work in the same environment as a sleaze like you!"
        aletta.say "And you should do the same, Lavish."
    else:
        aletta.say "Don't try to talk your way out of this, [hero.name]."
        aletta.say "You're fired!"
        aletta.say "There's no place in this company for a sleaze like you!"
        $ game.flags.fired = True
        $ game.flags.job_day = False
        $ Room.find('office').hide()
    mike.say "Aletta, please..."
    aletta.say "Don't try to change my mind, [hero.name]."
    aletta.say "You're lucky I haven't taken legal action."
    lavish.say "Yeah, and the same goes for me too, [hero.name]."
    lavish.say "I can't work in an environment like this."
    lavish.say "I've already handed in my letter of resignation."
    hide lavish
    hide aletta
    with moveoutleft
    "With that, the pair of them turn their backs to me."
    "I can only stand there in silence, watching as they stride away."
    "Part of me wants to look around, to see if there were any witnesses."
    "Because that's all I'd need right now to make my humiliation complete."
    $ aletta.love -= 20
    $ lavish.love -= 20
    if game.flags.isceo:
        $ aletta.set_gone_forever()
    $ lavish.set_gone_forever()
    return

label office_aletta_shiori_showdown:
    show aletta angry at left5
    show shiori sad at top_mostleft
    with moveinleft
    "Normally when I see Aletta and Shiori heading my way together, I'd be delighted."
    "And that's because it usually means the chance to get up to something enjoyable with at least one of them."
    "But this time it's different, and I know it from the looks on their faces."
    show aletta at right5
    show shiori at left5
    with ease
    "Shiori looks upset, like she's on the verge of tears, which is nothing new."
    "It's Aletta that's worrying me more, even starting to scare me."
    "She has that look of a woman on the warpath, like she's out for blood."
    "And I have a sinking feeling that the blood in question is mine!"
    mike.say "Erm..."
    mike.say "Hey, Aletta...Shiori..."
    mike.say "What can I do for you two?"
    "The sound of my voice only seems to make Aletta's mood worse."
    "She tenses, and for a moment I honestly think she's going to slap me."
    "But then Shiori steals her thunder by bursting into a flood of tears."
    shiori.say "Oh, [hero.name]..."
    shiori.say "I trusted you!"
    shiori.say "How could you do this to me?"
    shiori.say "How could you be so cruel?!?"
    "I take an instinctive step backwards, shaking my head."
    mike.say "What are you talking about, Shiori?"
    mike.say "What did I do?"
    "Rather than answering me, Shiori continues blubbing."
    "And so it falls to Aletta to speak for the pair of them."
    aletta.say "Don't play dumb, [hero.name]."
    aletta.say "You've been seeing us both behind each other's backs."
    aletta.say "Did you think that we wouldn't find out?!?"
    "I fight the instinct to say that I'd hoped they wouldn't."
    "After all, I'd kind of like to keep my head attached to my body."
    "But shit, they found me out!"
    mike.say "Look, girls..."
    mike.say "I can explain..."
    "Aletta cuts me off before I can say another word."
    show aletta at startle
    if game.flags.isceo:
        aletta.say "No need to bullshit me, [hero.name]."
        aletta.say "I quit!"
        aletta.say "I refuse to work in the same environment as a sleaze like you!"
        aletta.say "And you should do the same, Shiori."
    else:
        aletta.say "Don't try to talk your way out of this, [hero.name]."
        aletta.say "You're fired!"
        aletta.say "There's no place in this company for a sleaze like you!"
        $ game.flags.fired = True
        $ game.flags.job_day = False
        $ Room.find('office').hide()
    mike.say "Aletta, please..."
    aletta.say "Don't try to change my mind, [hero.name]."
    aletta.say "You're lucky I haven't taken legal action."
    "If Aletta had been expecting solidarity from Shiori, she doesn't get it."
    "The other girl just keeps on sobbing and rubbing her eyes."
    hide shiori
    hide aletta
    with moveoutleft
    "All I can do is watch as they both walk away."
    "Well, that and hope that nobody else saw the unpleasant exchange."
    $ aletta.love -= 20
    $ shiori.love -= 20
    if game.flags.isceo:
        $ aletta.set_gone_forever()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
