init python:
    Activity(**{
    "name": "study_female",
    "label": "study_classroom_female",
    "fun": -1,
    "knowledge": 1,
    "duration": 2,
    "rooms": "classroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsFlag("graduated", False),
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 4),
            ),
        ],
    "display_name": "Study",
    "icon": "study",
    })

label study_classroom_female:
    show chibi study

    if not "study_female" in DONE:
        "So according to this I must attend class every day and do my homeworks every week if I want to get good grades."
        "In addition there are exams at the end of each weeks..."
        "Student life sure is tough."
        $ hero.flags.studies_starting_day = game.days_played
        $ hero.flags.test_scores = []
        $ hero.flags.validated_semesters = 0
        $ hero.flags.studies = hero.knowledge / (len(hero.flags.test_scores) + hero.flags.validated_semesters + 1)
    else:

        if DONE.get("study_female", game.days_played) < game.days_played:
            if hero.flags.validated_semesters > 5:
                "I got my diploma!!!!"
                $ hero.flags.graduated = True
                hide chibi
                return
            elif game.week_day == 5:
                if game.days_played - hero.flags.last_test > 7:
                    $ hero.flags.studies *= 0.5
                "Today is exam day!"
                $ test_score = min([100, int(hero.flags.studies * hero.energy / 10.0)])
                $ hero.flags.test_scores.append(test_score)
                $ hero.flags.studies = hero.knowledge / (len(hero.flags.test_scores) + hero.flags.validated_semesters + 1)
                $ hero.flags.last_test = game.days_played
                "I got a [test_score]%% on my test!"
                hide chibi
                return
            elif len(hero.flags.test_scores) >= 4:
                "The semester results are here..."
                $ result = int(sum(hero.flags.test_scores) / len(hero.flags.test_scores))
                if result >= 80:
                    "I validated that semester!"
                    $ hero.flags.validated_semesters += 1
                elif result <= 50:
                    "I failed that semester so bad..."
                else:
                    "I failed that semester."
                $ hero.flags.test_scores = []
                $ hero.flags.studies = hero.knowledge / (len(hero.flags.test_scores) + hero.flags.validated_semesters + 1)
    $ hero.flags.studies += 10
    call study_classroom from _call_study_classroom
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
