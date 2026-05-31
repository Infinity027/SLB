label hour_selection(fixed_hour=None):
    if isinstance(fixed_hour, int):
        $ fixed_hour = [fixed_hour]
    elif fixed_hour is None:
        $ fixed_hour = [14, 20]
    if game.hour in fixed_hour:
        return ("Now", ("now", 0))
    elif game.hour < max(fixed_hour):
        return ("Today", (game.days_played, game.week_day))
    return

label tomorrow_selection(fixed_season=None):
    if fixed_season:
        if isinstance(fixed_season, basestring):
            $ fixed_season = [fixed_season]
        $ future_season = game.calendar.get_future_season(game.days_played + 1)
        if future_season in fixed_season:
            if game.week_day != 7:
                $ tomorrow = ("Tomorrow", (game.days_played + 1, game.week_day + 1))
                $ start = 1
            else:
                $ tomorrow = ("Tomorrow", (game.days_played + 1, 1))
                $ start = 2
        else:
            $ start = game.week_day
            $ tomorrow = None
    else:
        if game.week_day != 7:
            $ tomorrow = ("Tomorrow", (game.days_played + 1, game.week_day + 1))
            $ start = 1
        else:
            $ tomorrow = ("Tomorrow", (game.days_played + 1, 1))
            $ start = 2
    return (tomorrow, start)

label end_of_week_selection(starting_day, fixed_season=None):
    $ other_week_days = []
    python:
        if fixed_season:
            if isinstance(fixed_season, basestring):
                fixed_season = [fixed_season]
            if game.week_day + 2 <= 7:
                for i in range(game.week_day + 2, 8):
                    if game.calendar.get_future_season(game.days_played - game.week_day + i) in fixed_season:
                        other_week_days.append((f"Next {game.get_day_str(i)}", (game.days_played - game.week_day + i, i)))
            
            if game.week_day > 1:
                for i in range(starting_day, game.week_day):
                    if game.calendar.get_future_season(game.days_played - game.week_day + i + 7) in fixed_season:
                        other_week_days.append((f"Next {game.get_day_str(i)}", (game.days_played - game.week_day + i + 7, i)))
        else:
            if game.week_day + 2 <= 7:
                for i in range(game.week_day + 2, 8):
                    other_week_days.append((f"Next {game.get_day_str(i)}", (game.days_played - game.week_day + i, i)))
            if game.week_day > 1:
                for i in range(starting_day, game.week_day):
                    other_week_days.append((f"Next {game.get_day_str(i)}", (game.days_played - game.week_day + i + 7, i)))
    return other_week_days

label select_date_time(fixed_hour=None, fixed_season=None, add_cancel=True):
    if fixed_hour and fixed_hour not in [14, 20]:
        $ renpy.error("fixed_hour must be 14 or 20")
    if fixed_season:
        if isinstance(fixed_season, basestring):
            $ fixed_season = [fixed_season]
        if not set(fixed_season) & {"spring", "summer", "fall", "winter"}:
            $ renpy.error("fixed_season must be spring, summer, fall or winter")

    $ choices = []
    call hour_selection (fixed_hour) from _call_hour_selection
    $ selected_hour = _return
    if selected_hour:
        $ choices.append(selected_hour)
    call tomorrow_selection (fixed_season) from _call_tomorrow_selection
    $ (tomorrow, start) = _return
    if tomorrow:
        $ choices.append(tomorrow)

    call end_of_week_selection (start, fixed_season) from _call_end_of_week_selection
    $ choices.extend(_return)
    if add_cancel:
        $ choices.append(("Cancel", ("cancel", None)))

    $ (day, week_day) = renpy.display_menu(choices)

    if day == "cancel":
        $ day = "cancel"
        $ hour = None
        $ s = None
    elif day != "now":
        if fixed_hour:
            if not game.days_played == day or (game.days_played == day and game.hour < fixed_hour):
                $ hour = fixed_hour
        else:
            if not game.days_played == day or (game.days_played == day and game.hour < 14):
                $ choices = [("Afternoon", 14), ("Evening", 20)]
                $ hour = renpy.display_menu(choices)
            else:
                $ hour = 20

        $ s = "Let's meet up "
        if day == game.days_played and hour == 20:
            $ s += "tonight."
        elif day == game.days_played and hour == 14:
            $ s += "this afternoon."
        elif day == game.days_played + 1 and hour == 20:
            $ s += "tomorrow night."
        elif day == game.days_played + 1 and hour == 14:
            $ s += "tomorrow afternoon."
        elif hour == 20:
            $ s += f"{game.get_day_str(week_day)} evening."
        elif hour == 14:
            $ s += f"{game.get_day_str(week_day)} afternoon."
    else:
        $ day = "now"
        $ hour = game.hour
        $ s = "Let's meet up now"
    return (day, hour, s)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
