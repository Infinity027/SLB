init python:
    Consumable("skill_book_hypnosis", display_name="Skill book: Hypnosis", price=500, label="hypnosis_skill_book", uses=20, tooltip="A book to learn hypnosis", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])

    InteractActivity(**{
    "name": "hypnosis",
    "display_name": "Use hypnosis",
    "duration": 1,
    "icon": "hypnosis",
    "conditions": [
        HeroTarget(IsGender("male")),
        HasSkill("hypnosis"),
        ActiveTarget(
            Not(IsActivity("sleep")),
            IsGender("female"),
            ),
        ],
    "label": "hypnosis_action",
    "once_day": "ACTIVE",
    })

    SpecificTalkSubject(**{
    "name": "ask_about_hypnosis",
    "display_name": "Ask her consent for hypnosis",
    "label": "hypnosis_talk",
    "duration": 0,
    "icon": "button_hypnosis",
    "conditions": [
        HasSkill("hypnosis"),
        HeroTarget(
            IsGender("male"),
            ),
        ActiveTarget(
            IsGender("female"),
            IsFlag("hypnosisConsent", False),
            ),
        ],
    "do_once": "ACTIVE",
    })

    Event(**{
    "name": "hypnosis_arrested",
    "label": "hypnosis_arrested",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("map")
            ),
        "randint(1, 100) <= hero.flags.hypnosisFailure"
        ],
    "do_once": True
    })

    Event(**{
    "name": "hypnosis_package",
    "label": "hypnosis_package",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsHour(9, 12),
        IsDayOfWeek("12345"),
        HeroTarget(
            MinStat("charm", 100),
            IsGender("male"),
            HasRoomTag("home"),
            ),
        ],
    "do_once": True
    })

label hypnosis_skill_book:
    if hero.has_skill("hypnosis"):
        "I know everything I need to about hypnosis."
    else:
        if hero.has_skill("bookworm"):
            $ game.pass_time(1, True)
        else:
            $ game.pass_time(2, True)
        if not hero.skills.hypnosis.value:
            "Intrigued, I begin to actually read little bits of the book."
            "At first it's only things that catch my interest, like cool diagrams."
            "But pretty soon I'm reading whole chunks of text and really getting into it."
            "It's weird, like learning about hypnotism is hypnotic in and of itself!"
            "In fact, I'm pretty sure that, with a bit of practice, I could pull some of this stuff off."
            "Hmm...I wonder if anyone ever tried to use hypnotism to pick up girls?"
        $ hero.gain_skill("hypnosis", 5)
        $ skill = hero.skills.hypnosis.value
        "I read about hypnosis in the book. ([skill]%%)"
    return

label hypnosis_package:
    scene bg livingroom
    "I normally ignore the sound of the letter-box opening and the mail being pushed through."
    "But today I just happen to be crossing the hall when it happens and I glance over towards the door."
    "Part of my curiosity is because I can see there's a package amongst the letters."
    "So I walk over and pluck it up off the door-mat, wondering who it could be for."
    "Most likely it's a book for Sasha or some of the junk [bree.name]'s always ordering."
    "But when I pick it up, I'm surprised to see that the package is addressed to me!"
    "Intrigued, I tear off the packaging to reveal what's inside."
    "Huh - it is a book after all."
    "But it looks like a pretty old one, bound in leather and worn by the passage of time."
    "That said, somebody's taken good care of it."
    "Flicking through the yellowed pages, nothing seems to be missing or damaged."
    "There's no title on the cover of the book."
    "And the words on the spine are faded beyond recognition."
    "But the title page bears the words 'Techniques in Hypnotism and Mesmerism - a complete guide'."
    "What the hell is someone sending me this for?"
    "As I flick through the book, a note falls out and drops to the floor."
    "Stooping to pick it up, I seem to recognise the handwriting."
    "'This book changed my life, I'm sure it'll change yours too.'"
    "I don't need to read the name signed at the bottom of the note to know it's from my dad."
    "But since when was he even interested in hypnotism?"
    $ hero.gain_item("skill_book_hypnosis")
    return

label hypnosis_arrested:
    show bg street
    if renpy.has_label("mike_achievement_0") and not game.flags.cheat and (game.days_played == 0 or (game.days_played == 1 and game.hour <= 10)):
        call mike_achievement_0 from _call_mike_achievement_0
    "I really should take the time to send my dad a note and thank him for the book he sent me."
    "Learning the basics of hypnosis has been a total revelation for me."
    "In fact, I'd go as far as to say that it's changed my life - and for the better too!"
    "No matter what the issue is, everyone seems to come round to my way of thinking in the end!"
    "Which is why I'm currently striding down the street, feeling like the king of the world."
    show inspector
    "Inspector" "Ah..."
    "Inspector" "Excuse me, sir..."
    mike.say "Huh?"
    "I stop and turn to see a shabby-looking middle-aged man."
    "He's waving a hand at me, like he wants to ask me something."
    mike.say "Oh..."
    mike.say "Sorry, man - I don't give handouts to bums!"
    "The man looks a little surprised at my answer."
    "But then he chuckles and shakes his head."
    "Inspector" "No, sir, no..."
    "Inspector" "I don't want your small-change."
    "As he says this, he fumbles around inside his coat."
    "Oh great, I'm being hassled in the street by a pervert!"
    "But then it's my turn to be surprised, as he produced a police badge."
    "Inspector" "Detective Michaels..."
    "Michaels" "That's me!"
    "Michaels" "And you very much match the description of a young man I'm currently looking for!"
    "I start to back away on pure instinct."
    "Shaking my head and holding up my hands to ward him off."
    mike.say "Oh no!"
    mike.say "No way!"
    "Detective Michaels takes a step forwards, still smiling at me."
    "But I note that he's also shaking his head at the same time."
    "Michaels" "Oh, I can't do that!"
    "Michaels" "You see I'm looking for a guy that's been going around hypnotising people."
    "Michaels" "To be more specific, he's been hypnotising young ladies all over town."
    "Michaels" "And I need to lock him up so that stops happening."
    "I have the book on hypnotism in my pocket, and I pull it out."
    "The detective must think I'm going for a gun."
    "Because he makes to calm the situation down."
    "But then he sees I just have a book, and he lets out a laugh."
    "Michaels" "Put that thing down and come along quietly, son!"
    mike.say "Stay back!"
    mike.say "Or else I'll hypnotise you too!"
    show inspector close
    "What follows is not the most proud or dignified moment of my life."
    "The middle-aged detective and I end up scuffling on the ground."
    "He may be older than me, but the guy's wiry and tough."
    "And before too long I feel him putting cuffs on me."
    "Then he adds insult to injury by sitting on me while he calls for backup."
    scene bg street
    show hypnosis arrest
    with fade
    "Michaels" "Phew..."
    "Michaels" "Just you sit tight, son."
    "Michaels" "They'll be along to collect you soon."
    "Michaels" "Then you can have a nice long rest in a cosy little cell!"
    $ renpy.full_restart()
    return

label hypnosis_talk:
    call expression f"{active_girl.id}_greet" from _call_expression_104
    $ renpy.show(active_girl.id)
    if renpy.has_label(f"{active_girl.id}_hypnosis_talk_{hero.gender}"):
        call expression f"{active_girl.id}_hypnosis_talk_{hero.gender}" from _call_expression_107
    else:
        if renpy.has_label(f"{active_girl.id}_hypnosis_talk_intro_{hero.gender}"):
            call expression f"{active_girl.id}_hypnosis_talk_intro_{hero.gender}" from _call_expression_108
        else:
            mike.say "Hey [active_girl.name], I have a question..."
            mike.say "Would it be ok if I used hypnosis on you to alter your behaviour?"
        if active_girl.love >= 75 and active_girl.sub >= 25:
            $ renpy.show(f"{active_girl.id} happy")
            $ active_girl.flags.hypnosisConsent = True
            if renpy.has_label(f"{active_girl.id}_hypnosis_talk_accept_{hero.gender}"):
                call expression f"{active_girl.id}_hypnosis_talk_accept_{hero.gender}" from _call_expression_109
            else:
                active_girl.say "Sure!"
        else:
            $ renpy.show(f"{active_girl.id} annoyed")
            $ active_girl.love -= 10
            if renpy.has_label(f"{active_girl.id}_hypnosis_talk_refuse_{hero.gender}"):
                call expression f"{active_girl.id}_hypnosis_talk_refuse_{hero.gender}" from _call_expression_110
            else:
                active_girl.say "No way!"
    $ renpy.hide(active_girl.id)
    return

label hypnosis_action:
    call expression f"{active_girl.id}_greet" from _call_expression_111
    $ renpy.show(f"{active_girl.id} close")
    "I start hypnotizing [active_girl.name]..."
    if not active_girl.flags.hypnosisConsent and randint(1, 100) <= 25 + active_girl.flags.hypnosisOffset:
        $ renpy.show(f"{active_girl.id} close angry")
        $ active_girl.love -= 10
        active_girl.say "What the fuck are you doing ?"
        mike.say "...Nothing..."
        $ hero.flags.hypnosisFailure += 1
    else:
        $ renpy.show(f"{active_girl.id} close mindless")
        mike.say "Listen to me [active_girl.name]."
        menu:
            "Increase submissiveness" if active_girl.sub < 100:
                mike.say "I think you should be more submissive."
                $ active_girl.sub += 3
                active_girl.say "I should be more submissive..."
            "Increase dominance" if active_girl.sub > -100:
                mike.say "I think you should be more dominant."
                $ active_girl.sub -= 3
                active_girl.say "I should be more dominant..."
            "Increase girl attraction" if active_girl.lesbian < 20:
                mike.say "I think you should like girls more."
                $ active_girl.lesbian += 1
                active_girl.say "Girls are hot and cute..."
            "Decrease girl attraction" if active_girl.lesbian > 0:
                mike.say "I think you should like girls less."
                $ active_girl.lesbian -= 1
                active_girl.say "Girls are not that sexy after all..."
            "Be more innocent" if active_girl.id in ["harmony", "reona"] and active_girl.purity < 100:
                mike.say "I think you should be more innocent."
                active_girl.say "I need to be a good girl..."
                $ active_girl.purity += 3
            "Be sluttier" if active_girl.id == "harmony" and harmony.purity > harmony.purity.min:
                mike.say "I think god wants you to be sluttier."
                $ active_girl.purity -= 3
                active_girl.say "I need to be sluttier to please The Lord..."
            "Be sluttier" if active_girl.id == "reona" and reona.purity > reona.purity.min:
                mike.say "I think you should be sluttier."
                $ active_girl.purity -= 3
                active_girl.say "I need to be sluttier..."
            "Be more masculine" if active_girl.id == "morgan" and morgan.male < 100:
                mike.say "I think you should be more masculine."
                $ active_girl.male += 3
                active_girl.say "I should be more masculine..."
            "Be more feminine" if active_girl.id == "morgan" and morgan.male > 0:
                mike.say "I think you should be more feminine."
                $ active_girl.male -= 3
                active_girl.say "I should be more feminine..."
    $ renpy.hide(active_girl.id)
    return
return
