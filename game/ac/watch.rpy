label watch_tv_with(*people):

    $ people = [Person.find(person) for person in people]
    if len(people) == 0 or any([True for person in people if person is None]):
        $ hero.cancel_activity()
        return


    scene bg livingroom
    if len(people) == 1:
        $ renpy.show(people[0].id)
    else:
        $ renpy.show(people[0].id, at_list=[left])
        $ renpy.show(people[1].id, at_list=[right])
        if len(people) > 2:
            $ renpy.show(people[2].id)

    call expression f"watch_tv_with_dialogues_1_{hero.gender}" from _call_expression_188
    if len(people) == 1 and renpy.has_label(people[0].id + "_tv_reaction"):
        call expression people[0].id + "_tv_reaction" from _call_expression_189
    $ renpy.dynamic("choices", "genre")
    $ choices = [(movie.description, movie.id) for movie in Movie.all_movies()]
    $ genre = renpy.call_screen("select", choices)
    if genre == "None":
        $ hero.cancel_activity()
        return


    python:
        for person in people:
            person.set_flag("daily_interact", 1, 1, "+")


    scene bg livingroom
    show expression f"watch tv {' '.join(person.id for person in people)}"
    if genre == "action":
        $ renpy.say("", randchoice([
            "We watch an action movie.",
            f"We watch a movie with {randchoice(['Schwarzenegger', 'Stallone', 'Statham'])}.",
            f"We watch a {randchoice(['Die Hard', 'Rambo', 'Dirty Harry', 'James Bond'])} sequel."
        ]))
    elif genre == "cartoon":
        "We watch a funny cartoon."
    elif genre == "discovery":
        "We watch a discovery channel."
    elif genre == "fashion":
        "We watch a fashion show."
    elif genre == "horror":
        $ renpy.dynamic("a", "b", "c", "d", "e", "t")
        $ a = randchoice(["dead", "bimbo", "nazi", "deathless", "zombie", "vampire", "mutant", "aliens", "flesh eaters", "sexy"])
        $ b = randchoice(["housewives", "cops", "millionaires", "geeks", "sluts", "nuns", "cats", "dogs", "grannys", "middle aged men", "government officials", "strippers", "doctors", "truck drivers"])
        $ c = randchoice(["massacre", "against", "kill", "torture", "eat"])
        $ d = randchoice(["bimbo", "smart", "real", "fake", "stupid", "angry", "cute", "racist", "socialist", "poor", "rich", "ugly", "sexy", "fat", "mean", "nice", "old", "young", "virgin"])
        $ e = randchoice(["housewives", "cops", "millionaires", "geeks", "sluts", "nuns", "cats", "dogs", "grannys", "middle aged men", "government officials", "strippers", "doctors", "truck drivers"])
        $ t = (f"{a} {b} {c} {d} {e}").title().strip()
        "We watch a horror movie titled [t]."
    elif genre == "music":
        "We watch a concert."
    elif genre == "news":
        "We watch the news."
    elif genre == "porn":
        if not all(map(lambda x: "kinky" in x.traits, people)):
            $ renpy.dynamic("who", "offset")
            $ offset, who = sorted([(person.love(), person) for person in people if "kinky" not in person.traits], key=lambda person: person[0])[0]
            if len(people) > 1:
                $ offset /= 2
            if hero.charm < 100 - offset:
                if renpy.has_label(f"{who.id}_porn_bad_reaction"):
                    call expression f"{who.id}_porn_bad_reaction" from _call_expression_190
                else:
                    $ who.say("Sorry, I don't want to watch this sort of thing.")
                python:
                    for person in people:
                        person = Person.find(person)
                        if person is None:
                            continue
                        person.love -= 1
                $ hero.cancel_activity()
                hide watch tv
                return
        "We watch some porn together."
    elif genre == "reality":
        $ renpy.dynamic("a", "b", "c", "d", "t")
        $ a = randchoice(["dead", "bimbo", "nazi", "smart", "real", "fake", "gay", "stupid", "angry", "cute", "white", "black", "racist", "socialist", "poor", "rich", "ugly", "sexy", "fat", "mean", "nice", "old", "young", "virgin"])
        $ b = randchoice(["housewives", "cops", "millionaires", "geeks", "sluts", "nuns", "cats", "dogs", "grannys", "middle aged men", "asians", "government officials", "strippers", "doctors", "truck drivers"])
        $ c = randchoice(["of", "against", "meet", "discover", "lost in"])
        $ d = randchoice(["the world", "venezuela", "paris", "mars", "the sewers", "new-york", "france", "spain", "seattle", "los angeles", "my basement", "texas", "mexico", "brazil", "space"])
        $ t = (f"{a} {b} {c} {d}").title()
        "We watch [t]."
    elif genre == "romcom":
        "We watch a romantic comedy."
    elif genre == "sci-fi":
        "We watch a Sci-Fi movie."
    else:
        $ hero.cancel_activity()
        return


    call apply_movie_gain (genre, *people) from _call_apply_movie_gain

    $ renpy.dynamic("reactions")
    $ reactions = _return
    $ renpy.log(f"reactions: {reactions}")


    if genre == "porn":
        $ renpy.dynamic("subgenre")
        menu:
            "SM porn":
                $ subgenre = "sm"
            "Femdom porn":
                $ subgenre = "femdom"
            "Gonzo porn":
                $ subgenre = "gonzo"
            "Lesbian porn":
                $ subgenre = "lesbian"
        call apply_porn_extra_gains (subgenre, *people) from _call_apply_porn_extra_gains


    if hero.is_male and genre == "porn" and bree in people and sasha in people and bree.love >= 150 and sasha.love >= 150 and Harem.together(*people, name="home"):


        hide tv
        call bj3_porn from _call_bj3_porn
    elif hero.is_male and genre == "porn" and len(people) == 1 and bree in people and bree.love >= 150 and bree.sexperience:
        call bree_tv_bj from _call_bree_tv_bj
    elif hero.is_male and genre == "porn" and len(people) == 1 and sasha in people and sasha.love >= 150 and sasha.sexperience:
        call sasha_tv_bj from _call_sasha_tv_bj
    elif hero.is_male and genre == "horror" and len(people) == 1 and sasha in people and not sasha.flags.zombietalk:
        call sasha_zombietalk from _call_sasha_zombietalk
    else:
        call movie_reactions (genre, reactions[0], reactions[1], reactions[2]) from _call_movie_reactions

    $ hero.fun += 1.5
    hide watch tv


    if hero.is_male and len(people) == 1 and sasha in people and hero.has_skill("massage") and (1 <= game.week_day <= 5) and game.hour > 20:
        if sasha.sub <= -50 and sasha.love >= 100 and sasha.flags.footrub == 4:
            call sasha_tv_footrub_3 from _call_sasha_tv_footrub_3
        elif sasha.sub <= -25 and sasha.love >= 100 and sasha.flags.footrub >= 5:
            call sasha_tv_footrub_2 from _call_sasha_tv_footrub_2
        elif sasha.sub <= 0 and sasha.love >= 50:
            call sasha_tv_footrub_1 from _call_sasha_tv_footrub_1
    return

label apply_movie_gain(genre, *people):
    python:


        results = ([], [], [])

        movie = Movie.find(genre)

        for person in people:
            person = Person.find(person)
            if person is None:
                continue
            
            gain = 0
            
            
            if movie is not None:
                for trait in person.traits:
                    symbol = 1
                    if trait.startswith("not_"):
                        symbol = -1
                        trait = trait[4:]
                    if trait in movie:
                        gain += symbol * movie[trait]
            
            
            try:
                personal_likes = person.movies
            except AttributeError:
                personal_likes = {}
            if genre in personal_likes:
                gain += personal_likes[genre]
            
            
            if game.active_date is None or isinstance(game.active_date, (NoDateEvent, ScavengerHuntAppointment)):
                person.love += gain
            else:
                if game.active_date.location.name == "cinema":
                    if "cinema" in person.desire_factors:
                        if gain > 1:
                            gain *= 2
                        else:
                            gain += 1
                    elif "not_cinema" in person.desire_factors:
                        if gain < -1:
                            gain *= 2
                        else:
                            gain -= 1
                elif game.active_date.location.name == "home":
                    if "home" in person.desire_factors:
                        if gain > 1:
                            gain *= 2
                        else:
                            gain += 1
                    elif "not_home" in person.desire_factors:
                        if gain < -1:
                            gain *= 2
                        else:
                            gain -= 1
                game.active_date.score += 5 * gain
            
            
            if gain > 0:
                results[0].append(person)
            elif gain == 0:
                results[1].append(person)
            else:
                results[2].append(person)

    return results

label apply_porn_extra_gains(subgenre, *people):
    python:

        if subgenre == "sm":
            for person in people:
                person = Person.find(person)
                if person is None:
                    continue
                if isinstance(person, Girl):
                    person.sub += 1
                elif isinstance(person, Guy):
                    person.sub -= 1

        elif subgenre == "femdom":
            for person in people:
                person = Person.find(person)
                if person is None:
                    continue
                if isinstance(person, Girl):
                    person.sub -= 1
                elif isinstance(person, Guy):
                    person.sub += 1

        elif subgenre == "gonzo":
            pass

        elif subgenre == "lesbian":
            for person in people:
                person = Person.find(person)
                if person is None:
                    continue
                if person.is_female and person.lesbian < 15:
                    person.lesbian += 1


        for person in people:
            if person.id in ("bree", "mike", "minami"):
                person.flags.porn = True
    return

label movie_reactions(genre, liked, indifferent, disliked):
    if len(liked) == 0 and len(indifferent) == 0 and len(disliked) == 0:

        return

    if len(liked) > 1 and len(indifferent) == 0 and len(disliked) == 0:
        "Everyone seems to enjoy themselves."
        return

    if len(liked) == 0 and len(indifferent) > 1 and len(disliked) == 0:
        "Everyone seems not to be paying too much attention to the screen."
        return

    if len(liked) == 0 and len(indifferent) == 0 and len(disliked) > 1:
        "Everyone seems completely bored."
        return

    $ renpy.dynamic("who")

    if len(liked) == 1:
        $ who = liked[0].name
        if renpy.has_label(f"{who.lower()}_movie_liked_reaction_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{who.lower()}_movie_liked_reaction_{hero.gender}" from _call_expression_191
        else:
            if genre == "fashion":
                "[who] seems mesmerized."
            elif genre == "horror":
                "[who] seems beaming."
            elif genre == "porn":
                "[who] seems to be quite excited by the sight."
            elif genre == "romcom":
                if isinstance(liked[0], Girl):
                    "[who] seems to enjoy herself very much."
                else:
                    "[who] seems to enjoy himself very much."
            else:
                if isinstance(liked[0], Girl):
                    "[who] seems to enjoy herself."
                else:
                    "[who] seems to enjoy himself."
    elif len(liked) > 1:
        $ who = ", ".join(map(lambda x: x.name, liked[:-1])) + " and " + liked[-1].name
        if genre == "fashion":
            "[who] seem mesmerized."
        elif genre == "horror":
            "[who] seem beaming."
        elif genre == "porn":
            "[who] seem to be quite excited by the sight."
        elif genre == "romcom":
            "[who] seem to enjoy themselves very much."
        else:
            "[who] seem to enjoy themselves."

    if len(indifferent) == 1:
        $ who = indifferent[0].name
        if renpy.has_label(f"{who.lower()}_movie_indifferent_reaction_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{who.lower()}_movie_indifferent_reaction_{hero.gender}" from _call_expression_192
        else:
            "[who] doesn't seem to be paying too much attention to the movie."
    elif len(indifferent) > 1:
        $ who = ", ".join(map(lambda x: x.name, indifferent[:-1])) + " and " + indifferent[-1].name
        "[who] seem not to be paying too much attention to the movie."

    if len(disliked) == 1:
        $ who = disliked[0].name
        if renpy.has_label(f"{who.lower()}_movie_disliked_reaction_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{who.lower()}_movie_disliked_reaction_{hero.gender}" from _call_expression_193
        else:
            if genre == "horror":
                "[who] seems to be more scared than entertained."
            else:
                "[who] seems completely bored."
    elif len(disliked) > 1:
        $ who = ", ".join(map(lambda x: x.name, disliked[:-1])) + " and " + disliked[-1].name
        if genre == "horror":
            "[who] seem to be more scared than entertained."
        else:
            "[who] seem completely bored."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
