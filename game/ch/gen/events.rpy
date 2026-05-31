label call_hire_PI:
    "After a few rings someone picks up."
    "Investigator" "Idem Investigation - to whom I am speaking?"
    mike.say "Ah...I'm [heroname]...[hero.family_name]."
    mike.say "I'd like to hire you to work on a case for me."
    "Investigator" "Sure thing, Mister [hero.family_name]."
    "Investigator" "But you should know, my flat rate is $500."
    "Investigator" "And that's in advance, of course."
    menu:
        "Hire him" if hero.money >= 500:
            mike.say "Okay, okay - I'm fine with that."
        "Don't hire him":
            mike.say "On second thought, maybe I'm not so interested."
            return
    "Investigator" "That's great - let's get down to business, shall we?"
    if alexis.flags.rapeConfession and not alexis.flags.hired_PI:
        mike.say "I need you to find someone for me."
        mike.say "I just sent you some information on your phone."
        "Investigator" "Forgive me, Mister [hero.family_name], but this looks like your high-school year-book."
        mike.say "Well, it was the only place I could find a picture of the guy I need finding."
        "Investigator" "No social media?"
        mike.say "None whatsoever."
        "Investigator" "So it's not a classmate then...someone older?"
        "Investigator" "A teacher, perhaps?"
        mike.say "Gym teacher, actually."
        "Investigator" "You really want me to track down your high-school gym teacher?"
        mike.say "Yes I do."
        "Investigator" "Mind if I ask why?"
        mike.say "Let's just say I have a score to settle!"
        "Investigator" "Which is what, exactly?"
        "Investigator" "I need to know because I'm not taking this job on if all you want is revenge for him making you throw up after working you too hard!"
        mike.say "No, it's nothing like that!"
        mike.say "He...well, let's just say he did a very bad thing."
        mike.say "Something that's left a permanent impression on me..."
        "Investigator" "Ah, I see."
        "Investigator" "And where did he touch you?"
        "Investigator" "If that's not too sensitive of a question..."
        mike.say "No...no, no, no!"
        mike.say "He forced himself on my girlfriend, okay!"
        "Investigator" "I see, I see."
        "Investigator" "His picture's in here?"
        mike.say "Yes - on page 18."
        "Investigator" "'Mr Blank'...not the prettiest of guys, is he?"
        mike.say "You'll get no argument from me on that score!"
        mike.say "So you'll take the case?"
        mike.say "That's great news!"
        "Investigator" "I'll be in touch when I have something for you."
        $ game.flags.hirePI -= 1
        $ alexis.flags.hired_PI = True
        $ alexis.flags.PIDelay = TemporaryFlag(True, 3)
        $ hero.money -= 500
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
