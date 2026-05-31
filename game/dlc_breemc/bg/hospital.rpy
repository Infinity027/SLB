init python:
    Activity(**{
    "name": "Artificial insemination",
    "display_name": "Get an artificial insemination",
    "duration":2,
    "rooms": "hospital",
    "money_cost": 500,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            Not(OnDate()),
            IsFlag("pregnant", False),
            ),
        "not hero.calendar.find(label='breemc_clinic_insemination')",
        ],
    "label": "breemc_appointment_clinic_insemination",
    "icon": "insemination",
    "once_day": True,
    })

    Activity(**{
    "name": "Abort pregnancy",
    "display_name": "Get an abortion",
    "duration":12,
    "rooms": "hospital",
    "money_cost": 500,
    "conditions": [
        HeroTarget(
                IsGender("female"),
                IsFlag("foundpreg"),
                MaxFlag("pregnant", 45),
                Not(IsFlag("happypreg"))
                ),
        ],
    "label": "abort_pregnancy",
    "icon": "abortion",
    "once_day": True,
    })

    InteractEvent(**{
    "name": "abortion_reaction_female",
    "label": "abortion_reaction_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsFlag("abort_pregnancy", True),
            Not(OnDate()),
            ),
        ActiveTarget(
            IsFlag("toldpreg", True),
            ),
        ],
    "do_once": False,
    })

label abort_pregnancy:
    "God, I never thought I'd be doing something like this."
    "But I guess that most people in my position thought the same at some point."
    "Suddenly you realise that you always thought they were dumb or careless."
    "But the reality is that you're just the same as them."
    "And anyone could end up here, it's just a matter of chance."
    "I find myself standing outside the clinic, almost frozen to the spot."
    "And it takes a massive amount of willpower to make me walk inside."
    "Once I manage that, I want to keep the momentum going."
    "So I hurry over to the reception desk and catch someone's eye."
    bree.say "I..."
    bree.say "I'm here for a..."
    show aletta a work at flip, center, zoomAt (1.25, (650, 950)), blacker with dissolve
    "The receptionist looks up at me as I begin to falter."
    "And there's no judgement on their face as they step in to stop me."
    "Receptionist" "Of course..."
    "Receptionist" "If I could just take some details?"
    "I appreciate the way they stop me before I actually have to say the word."
    "But then they must be used to this kind of thing, as they deal with it on a daily basis."
    "I give the receptionist my details, and they tap them into a keyboard."
    "Receptionist" "All done."
    "Receptionist" "Would you like to take a seat?"
    "Receptionist" "Someone will be along to collect you soon."
    hide aletta with dissolve
    "I nod and shuffle over to the seats in the reception area."
    "The place is nice and clean, and there's a stack of well-thumbed magazines."
    "But reading is that last thing on my mind as I sit there waiting."
    "It feels like it takes forever, but in reality only a few minutes could have passed."
    "But I'm glad all the same when a nurse walks over to me."
    "Nurse" "[hero.name]?"
    bree.say "Yes, that's me."
    "Nurse" "Would you come with me, please?"
    "I get up and stick close to the nurse as she leads me away."
    "And then I follow her into a consulting room."
    scene doctor_fuck_bg
    show victor at flip, center, zoomAt (1.5, (640, 1140)), blacker
    with fade
    "The doctor behind the desk smiles and gestures for me to take a seat."
    "Doctor" "I just need to fill in a few forms before we proceed."
    "Doctor" "This won't take long."
    "I nod and do as the doctor asks."
    "But all the time I'm staring at the door behind them."
    "That must be the way to the room where...where it's going to happen."
    "All too soon the formalities are concluded."
    scene bg hospital with fade
    "Then the doctor shows me into the next room."
    "I'm not going to say what happens next."
    "Save to say that it's clean, kind and efficient."
    "And it feels like it totally destroys my soul too."
    "The rest of my time at the clinic is a blur."
    "People talk to me and I have to sign more forms."
    "But I don't really hear what's being said or understand why."
    "And I walk out onto the street feeling numb and hollow."
    "Knowing that I never want to go through that experience again."
    $ hero.unpreg()
    $ hero.fun -= 10
    if hero.morality >= 75:
        $ hero.morality -= 50
    elif hero.morality >= 50:
        $ hero.morality -= 25
    elif hero.morality >= 25:
        $ hero.morality -= 10
    $ hero.flags.abort_pregnancy = True
    return

label abortion_reaction_female:
    $ renpy.show(f"{active_girl.id}")
    if renpy.has_label(f"{active_girl.id}_abortion_reaction_{hero.gender}"):
        call expression f"{active_girl.id}_abortion_reaction_{hero.gender}" from _call_expression_470
        $ active_girl.flags.toldpreg = False
        $ active_girl.flags.know_is_father = False
    $ renpy.hide(f"{active_girl.id}")
    return

label breemc_appointment_clinic_insemination:
    scene bg hospital
    "The reception area is bustling with activity."
    "People are waiting in line to speak to the receptionist. I'm nervous when I approache the desk."
    "My mind races with worry, imagining various outcomes of the upcoming procedure."
    show aletta a work at flip, center, zoomAt (1.25, (650, 950)), dark, dark, dark, dark, dark with dissolve
    bree.say "Hello..."
    "Receptionist" "Hi, how can I help you?"
    bree.say "Um, hi. I want to make an appointment for an... artificial insemination."
    "Receptionist" "Sure, could you please provide me some information?"
    "I nervously give all information needed."
    "Receptionist" "Alright, let me check for availability..."
    "Receptionist" "How about next week, the next [game.calendar.get_future_day_of_week_name(game.days_played + 7)] in the morning?"
    bree.say "That would be great, I guess. Thank you."
    "Receptionist" "Alright then, if you have any questions or need assistance in the future, don't hesitate to reach out."
    "I smile at the receptionist and heads towards the exit."
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((9, 12), [], "Hospital: clinic insemination", "breemc_clinic_insemination", "breemc_clinic_insemination_missed"))
    return

label breemc_clinic_insemination_missed:
    "I missed my appointment at the clinic for my insemination... Maybe I didn't want to after all."
    return

label breemc_clinic_insemination(appointment=None):
    scene bg hospital
    "I'm pretty nervous as I turn up for the appointment at the clinic."
    "More than once I get the urge to turn around and run right out of there."
    "But I force myself to get a grip and see it through despite my fears."
    "After all, this is the twenty-first century, not the middle ages."
    "Women do this kind of thing all the time, it's nothing shameful."
    "With that in mind, I stride up to the reception desk."
    bree.say "Erm..."
    bree.say "Hello..."
    bree.say "I have an appointment to see someone here?"
    show aletta a work at flip, center, zoomAt (1.25, (650, 950)), dark, dark, dark, dark, dark with dissolve
    "The receptionist looks up and smiles at me."
    "But I can tell it's that certain kind of professional smile."
    "There's nothing personal or genuine about it."
    "Receptionist" "If I could just take a name please..."
    "I give them my details and they nod, searching for my details."
    "Receptionist" "Here you are..."
    "Receptionist" "Take a seat, and someone will be down to collect you soon."
    hide aletta with dissolve
    "I nod and shuffle over to the seats provided."
    "There's the usual pile of well-thumbed magazines."
    "But I don't feel in the mood to read any of them."
    "And I doubt that they'd be enough to distract me right now."
    show emma blazer a at flip, center, zoomAt (1.25, (650, 850)), dark, dark, dark, dark, dark with dissolve
    "Nurse" "You must be [hero.name], yes?"
    "Hearing someone say my name, I look up."
    "And I see the smiling face of an impossibly pretty nurse."
    bree.say "Y...yes..."
    bree.say "That's me!"
    "Nurse" "The doctor will see you now."
    "Nurse" "This way please..."
    "The nurse beckons for me to follow her, and I almost leap out of my seat."
    "Then I stick close to her heels as she leads me into a private consulting room."
    show emma blazer a at flip, right, zoomAt (1.25, (850, 850)), dark, dark, dark, dark, dark with easeinright
    hide emma blazer a with dissolve
    scene doctor_fuck_bg
    "Inside I'm confronted by a slightly older woman sitting behind a desk."
    show laura teaser with dissolve
    "If anything, she's even prettier than the nurse, but with an air of authority."
    "Wait...is she..."
    "Is she the doctor?!?"
    "As if sensing my surprise, she smiles and gestures to a seat."
    "Doctor" "Please, sit down."
    show fx question
    "Doctor" "Not what you were expecting?"
    "I shake my head, suddenly feeling pretty stupid."
    "I mean, why shouldn't the doctor be a woman?"
    bree.say "I'm sorry, doctor!"
    bree.say "I feel so silly..."
    bree.say "I don't know why I was expecting a man!"
    "The doctor smiles and shakes her head, dismissing my apology."
    "Doctor" "No offence taken..."
    "She pauses to check her notes."
    "Doctor" "...[hero.name]!"
    "Doctor" "But I assure you, I'm as good as any male doctor you could find."
    bree.say "Of course!"
    "The doctor consults her notes a second time."
    "Doctor" "So..."
    "Doctor" "You're here for artificial insemination, yes?"
    "I can't help flushing a little as the procedure is named."
    bree.say "Erm..."
    bree.say "Yes, that's the one!"
    "Doctor" "There's no need to be embarrassed, [hero.name]."
    "Doctor" "You're choosing a perfectly valid method of becoming pregnant."
    "Doctor" "Many modern women prefer this to the more, shall we say...traditional method!"
    "I nod and smile, trying to use her words to assure myself."
    "Doctor" "Anyway..."
    "Doctor" "Here's our brochure."
    "She hands me a glossy book that looks very professional."
    "But the sight of it makes me frown."
    bree.say "Oh no, that's okay."
    bree.say "I already chose what I want to have done."
    "The doctor chuckles and shakes her head."
    "Doctor" "No, no, [hero.name]..."
    "Doctor" "This is a brochure of our sperm donors!"
    "Doctor" "All fine specimens of manhood, I assure you."
    "I nod and begin to flick through the pages."
    "But I can feel my cheeks flushing at the same time."
    "This seems so weird, choosing a guy's...well, his little guys."
    "And doing it anonymously, like I was shopping for shoes in a catalogue!"
    "In the end I just pick one that sounds good on paper."
    bree.say "I'd like this one, please."
    "The doctor notes my choice."
    "And then she raises an eyebrow as she reads the details."
    "Doctor" "Oh really?"
    "Doctor" "I had no idea you were into that kind of thing..."
    "I open my mouth to ask what she means."
    "But the doctor is already filling in forms."
    "I'm surprised a moment later when the nurse reappears."
    scene doctor_fuck_bg at blur(16), dark, dark with dissolve
    "And she leads me off into a rather more clinical room."
    "Erm...okay..."
    "This is the part where it actually happens."
    "And no, I'm not going to go into details!"
    "Let's just say it's all professional and efficient."
    $ artificial_impregnate()
    $ hero.energy = 2
    $ hero.hunger = 2
    $ hero.grooming = 2
    $ hero.fun = 2
    "But afterwards I still can't help feeling like livestock!"
    scene bg hospital with dissolve
    "Once the procedure is over, there's just some formalities to be dealt with."
    "I get poked and prodded, asked a bunch of questions and they tell me when to come back."
    "Then I walk out of the place, feeling pretty freaked out by the whole experience."
    "I mean, I might actually have a person growing inside of me right now!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
