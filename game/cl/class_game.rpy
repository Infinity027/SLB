
init -15 python:



    class GameCalendar(NoRollback):
        SPECIAL_DATES = {
        "independenceday": ("summer", 4),
        "newyear": ("spring", 1),
        "valentine": ("spring", 14),
        "halloween": ("fall", 31),
        "christmaseve": ("winter", 24),
        "christmas": ("winter", 25),
        "newyeareve": ("winter", 31),
    }
        
        
        
        def __init__(self, parent):
            self._m1_class_game__game = parent
        
        @property
        def days_played(self):
            return self._m1_class_game__game.days_played
        
        @property
        def season(self):
            return self._m1_class_game__game.season
        
        @property
        def season_name(self):
            return SEASONS[self.season]
        
        @property
        def day_of_season(self):
            return self._m1_class_game__game.day
        
        @property
        def day_of_week(self):
            return self._m1_class_game__game.week_day
        
        @property
        def day_of_week_name(self):
            return DAYS[self.day_of_week - 1]
        
        @property
        def day_of_week_short_name(self):
            return self.day_of_week_name[0:3]
        
        @property
        def hour_of_day(self):
            return self._m1_class_game__game.hour
        
        @property
        def time_of_day_name(self):
            return self.get_time_of_day()
        
        def is_today(self, season, day_of_season=None):
            if isinstance(season, int):
                season = self.get_season_name(season)
            if day_of_season is None and season in self.SPECIAL_DATES:
                season, day_of_season = self.SPECIAL_DATES[season]
            return self.season_name == season and self.day_of_season == day_of_season
        
        @property
        def is_day(self):
            return 5 < self._m1_class_game__game.hour < 20
        
        @property
        def is_night(self):
            return not self.is_day
        
        def get_time_of_day(self, hour_of_day=None):
            if hour_of_day is None:
                hour_of_day = self._m1_class_game__game.hour
            if hour_of_day < 6:  
                return "night"
            elif hour_of_day < 12:  
                return "morning"
            elif hour_of_day < 18:  
                return "afternoon"
            else:  
                return "evening"
        
        def get_image_time_of_day(self, hour_of_day=None):
            hour = hour_of_day if hour_of_day else self.hour_of_day
            return "night" if hour >= 20 or hour <= 5 else "day"
        
        def get_day_of_week(self, nbr=None):
            if nbr is None:
                return self.day_of_week
            else:
                
                return (int(nbr) - 1) % 7 + 1
        
        def get_day_of_week_name(self, nbr=None, short=False):
            result = DAYS[self.get_day_of_week(nbr) - 1]
            return result[0:3] if short else result
        
        def get_season_name(self, nbr=None):
            if nbr is None:
                return self.season_name
            else:
                return SEASONS[int(nbr) % 4]
        
        def get_future_season(self, future_days_played):
            if future_days_played < self.days_played:
                raise ValueError(
                "Future days is in the past: "
                + str(future_days_played)
                + " < "
                + str(self.days_played)
            )
            
            future_days = future_days_played - self.days_played
            
            return SEASONS[
            (self.season + ((self.day_of_season + -1 + future_days) // 31)) % 4
        ]
        
        def get_future_days_played(self, *args):
            
            if len(args) == 1 and args[0] in self.SPECIAL_DATES:
                return self.get_future_days_played(*self.SPECIAL_DATES[args[0]])
            elif len(args) == 2:
                
                season = (
                SEASONS.index(args[0]) if isinstance(args[0], basestring) else args[0]
            )
                day_of_season = args[1]
                
                
                future = (season * 31 + day_of_season) - (
                self.season * 31 + self.day_of_season
            )
                if future < 0:
                    future += 124
                return self.days_played + future
            else:
                raise Exception(
                "Invalid Argument count for game.calendar.get_future_days_played"
            )
        
        def get_future_day_of_week(self, future_days_played):
            if future_days_played < self.days_played:
                raise ValueError(
                "Future days is in the past: "
                + str(future_days_played)
                + " < "
                + str(self.days_played)
            )
            
            return self.get_day_of_week(
            future_days_played - self.days_played + self.day_of_week
        )
        
        def get_future_day_of_week_name(self, *args, **kwargs):
            
            if len(args) == 1:
                return self._m1_class_game__get_future_day_of_week_name_for_days_played(*args, **kwargs)
            elif len(args) == 2:
                return self._m1_class_game__get_future_day_of_week_name_for_season_and_day(
                *args, **kwargs
            )
            else:
                raise Exception(
                "Invalid Argument count for game.calendar.get_future_day_of_week_name"
            )
        
        def get_next_day_of_week(self, searched_next_day, future_days_played=None):
            try:
                searched_next_day_nbr = int(searched_next_day)
            except ValueError:
                searched_next_day_nbr = DAYS.index(searched_next_day) + 1
            except Exception:
                raise Exception(
                "Invalid Argument searched_next_day for game.calendar.get_next_day_of_week"
            )
            if not future_days_played:
                if searched_next_day_nbr > game.week_day:
                    return self.days_played + (searched_next_day_nbr - game.week_day)
                else:
                    return self.days_played + ((7 - game.week_day) + searched_next_day_nbr)
            else:
                
                future_week_day = self.get_future_day_of_week(future_days_played)
                if searched_next_day_nbr > future_week_day:
                    return future_days_played + (searched_next_day_nbr - future_week_day)
                else:
                    return future_days_played + (
                    (7 - future_week_day) + searched_next_day_nbr
                )
        
        def get_future_previous_day_of_week(
        self, future_day_number, searched_week_day, force_previous_if_today=False
    ):
            """
        Retrieve nearest week day of some day in the future.
        @param: future_day_number: targeted day from which previous week day is searched
        @param: week_day: day to retrieve (monday, tuesday, 1, 2)
        @param: force_previous_if_today: if searched searched_week_day is future today, return previous matching weekday
        @return:
        """
            try:
                target_day_number = int(future_day_number)
            except Exception:
                raise Exception(
                "Invalid Argument future_day_number for game.calendar.get_future_nearest_day_of_week"
            )
            
            try:
                searched_week_day_nbr = int(searched_week_day)
            except ValueError:
                searched_week_day_nbr = DAYS.index(searched_week_day) + 1
            except Exception:
                raise Exception(
                "Invalid Argument searched_week_day for game.calendar.get_future_nearest_day_of_week"
            )
            
            future_week_day_number = self.get_future_day_of_week(target_day_number)
            
            if searched_week_day_nbr == future_week_day_number:
                if force_previous_if_today:
                    days_offset = 7
                else:
                    days_offset = 0
            elif searched_week_day_nbr > future_week_day_number:
                days_offset = 7 - (searched_week_day_nbr - future_week_day_number)
            else:
                days_offset = future_week_day_number - searched_week_day_nbr
            
            return future_day_number - days_offset
        
        def _m1_class_game__get_future_day_of_week_name_for_days_played(
        self, future_days_played, short=False, use_today=True
    ):
            if future_days_played == self.days_played and use_today:
                return "Today"
            else:
                
                return self.get_day_of_week_name(
                nbr=self.get_future_day_of_week(future_days_played), short=short
            )
        
        def _m1_class_game__get_future_day_of_week_name_for_season_and_day(
        self, season, day_of_season, short=False, use_today=True
    ):
            
            future = self.get_future_days_played(season, day_of_season)
            return self.get_future_day_of_week_name(
            future, short=short, use_today=use_today
        )


    class Game(Flagged, Proxied, object):
        def __init__(self):
            Proxied.__init__(self, "DATA_GAME", ["girl_clothes", "active_date", "calendar"])
            Flagged.__init__(self, "HERO!")
            self.calendar = GameCalendar(self)
            self.girl_clothes = None
        
        @staticmethod
        def get_difficulty_mod(value=None):
            if persistent.difficulty == 0:
                return 1
            elif persistent.difficulty == -1:
                if value and value < 0:
                    return 0.5
                return 2.0
            else:
                if value and value < 0:
                    return 1.5
                return 0.5
        
        def get_rent_amount(self):
            return 100 * self.get_difficulty_mod(-1)
        
        @staticmethod
        def get_dates():
            return [date for date in DATES.values() if date.test()]
        
        @staticmethod
        def play_music(music):
            if not (renpy.music.get_playing() == music):
                renpy.music.play(music, loop=True, fadein=0.5)
        
        @staticmethod
        def set_new_game_plus():
            if not game.flags.cheat:
                persistent.start_plus = True
                if not persistent.fitness or hero.fitness > persistent.fitness:
                    persistent.fitness = hero.fitness.val
                if not persistent.knowledge or hero.knowledge > persistent.knowledge:
                    persistent.knowledge = hero.knowledge.val
                if not persistent.charm or hero.charm > persistent.charm:
                    persistent.charm = hero.charm.val
                if not persistent.money or hero.money > persistent.money:
                    persistent.money = hero.money.val
                if (
                not persistent.sexperience
                or hero.base_sexperience > persistent.sexperience
            ):
                    persistent.sexperience = hero.base_sexperience
                if not persistent.talk_subjects:
                    persistent.talk_subjects = [
                    subject.name for subject in hero.talk_subjects_known
                ]
                else:
                    persistent.talk_subjects = list(
                    set(persistent.talk_subjects).union(
                        [subject.name for subject in hero.talk_subjects_known]
                    )
                )
                if not persistent.skills:
                    persistent.skills = {
                    skill_id: hero.skills[skill_id].value for skill_id in YAML_SKILLS
                }
                else:
                    for skill_id in YAML_SKILLS:
                        if YAML_SKILLS[skill_id].transferable is True and (
                        skill_id not in persistent.skills
                        or hero.skills[skill_id].value > persistent.skills[skill_id]
                    ):
                            persistent.skills[skill_id] = hero.skills[skill_id].value
            return
        
        @staticmethod
        def clear_new_game_plus():
            persistent.fitness = 0
            persistent.knowledge = 0
            persistent.charm = 0
            persistent.money = 0
            persistent.sexperience = 0
            persistent.talk_subjects = []
            persistent.skills = dict()
            return
        
        @staticmethod
        def get_cheated_girls(not_girl=None):
            if not_girl:
                not_girl = Person.find(not_girl)
            cheated_girls = []
            for g in Room.find(game.room).get_present_girls():
                if {not_girl.id, g.id} == {"alexis", "kylie"}:
                    continue
                elif (
                (g.flags.kiss or g.sexperience)
                and ((not g.flags.breakup) or (hasattr(g, "yandere") and g.yandere > 0))
                and renpy.has_label(g.id + "_cheated")
            ):
                    cheated_girls.append(g)
            if not_girl and not_girl in cheated_girls:
                cheated_girls.remove(not_girl)
            
            if not_girl:
                not_girl_harems = Harem.find(not_girl)
                to_remove = set()
                for girl_harem in not_girl_harems:
                    to_remove.update(
                    [
                        c_girl
                        for c_girl in cheated_girls
                        if girl_harem.together(not_girl, c_girl)
                    ]
                )
                cheated_girls = list(set(cheated_girls) - to_remove)
            return cheated_girls
        
        def get_day_night(self):
            if self.hour >= 20 or self.hour <= 5:
                return "night"
            return "day"
        
        @staticmethod
        def get_day_str(nbr=None, short=False):
            if nbr:
                return game.calendar.get_day_of_week_name(nbr, short=short)
            if short:
                return game.calendar.day_of_week_short_name
            else:
                return game.calendar.day_of_week_name
        
        def new_week(self):
            
            if game.flags.cleaningservices and not hero.money >= 100:
                game.flags.cleaningservices = False
            
            hero.flags.peeped = 0
            
            
            if game.flags.cleaningservices:
                hero.money -= 100
            else:
                chores = self.flags.chores
                if not chores >= 100:
                    mad_people = [
                    person
                    for person in Person.get_housemates()
                    if person.sub <= 25 or person.love <= 50
                ]
                    if len(mad_people) != 0:
                        for person in mad_people:
                            person.love -= 10
                        if hero.is_female:
                            renpy.say(
                            "", "I didn't do my chores, my roommates will be mad..."
                        )
                        else:
                            renpy.say("", "I didn't do my chores, the girls will be mad...")
                else:
                    game.flags.chores_completed = True
            
            
            for g in Person.all_people(ignore_hidden=False):
                if g.flags.mikeBabies:
                    child_support = g.flags.mikeBabies * 100
                    if hero.money < child_support:
                        g.love -= 25
                        renpy.say("", "I couldn't pay my child support to %s." % g.name)
                    hero.money -= child_support
            
            
            if persistent.difficulty >= 1:
                for g in Person.all_people(ignore_hidden=True):
                    
                    loss = g.get_attention_needed()
                    
                    g.love = g.love - loss if g.love > 0 else g.love
                    g.sub = (
                    g.sub - loss if g.sub > 0 else g.sub + loss if g.sub < 0 else g.sub
                )
            self.new_day()
        
        def new_day(self):
            self.clean_up()
            self.flags.last_reset = game.day
            if hero.flags.hypnosisFailure:
                hero.flags.hypnosisFailure -= 1
            if not hero.flags.pubes:
                hero.flags.last_shave += 1
                if self.days_played - hero.flags.last_shave > 7:
                    hero.flags.pubes = True
            for event in DayTransitionEvent.valid_events():
                renpy.call_in_new_context("event_do", event)
            for g in Person.all_people(ignore_hidden=False):
                if g.sub <= -75 and "dominant" not in g.traits:
                    g.traits += "dominant"
                elif g.sub <= -25 and "submissive" in g.traits:
                    g.traits -= "submissive"
                elif g.sub >= 75 and "submissive" not in g.traits:
                    g.traits += "submissive"
                elif g.sub >= 25 and "dominant" in g.traits:
                    g.traits -= "dominant"
                if (
                self.calendar.is_today(*g.birthday)
                and g.flags.birthdayknown
                and not g.hidden
            ):
                    renpy.say("", "It's " + g() + "'s birthday.")
                    g.flags.age_increase += 1
                if g.counters.pregnant >= 60 and persistent.pregnancy_end:
                    g.flags.mikeBabies += 1
                    g.unpreg()
                    if not g.flags.engagedmike:
                        g.love -= g.flags.birthPenalty + 25
                        if g.id == "kylie":
                            g.yandere += 25
                    renpy.say("", g.name + " gave birth today.")
            if self.calendar.is_today("valentine"):
                renpy.say("", "It's Valentine's Day.")
            elif self.calendar.is_today("christmas"):
                renpy.say("", "It's Christmas.")
            elif self.calendar.is_today("newyear"):
                renpy.say("", "It's New Year's Day.")
            elif self.calendar.is_today("independenceday"):
                renpy.say("", "It's Independence Day.")
            elif self.calendar.is_today("halloween"):
                renpy.say("", "It's Halloween.")
            if self.calendar.is_today(*hero.birthday):
                renpy.say("", "It's my birthday.")
                hero.flags.age_increase += 1
            hero.activity = None
            
            if game.flags.reminders is not False:
                agenda = hero.calendar.get_agenda_day()
                if agenda:
                    
                    renpy.play("sd/cell_vibrate.ogg", "sound")
                    for entry in agenda:
                        game.notify("{image=gui/icons/icon_reminder.png}" + str(entry))
            for girl in Person.all_people(ignore_hidden=False):
                girl.increment_counters()
            hero.increment_counters()
        
        @staticmethod
        def update_rooms():
            for r in Room.all():
                r.present_girls = []
            
            for girl in Person.all_people(ignore_hidden=False):
                girl.set_room()
        
        def pass_time(self, duration=1, needs=False):
            if duration:
                del DONE_HOUR[:]
                self.hour = int(self.hour + duration)
                if self.hour >= 24:
                    self.hour -= 24
                    if (
                    self.flags.worksatisfaction
                    and not self.flags.hasworked
                    and self.week_day <= 5
                ):
                        self.set_flag("worksatisfaction", 1, mod="-")
                    self.day += 1
                    self.days_played += 1
                    self.week_day += 1
                    if self.week_day > 7:
                        self.week_day = 1
                    if self.day > 31:
                        self.day = 1
                        self.season += 1
                        if self.season > 3:
                            self.season = 0
                    hero.calendar.clean_up()
                if self.hour >= 6:
                    if (
                    self.flags.last_reset != self.day
                    and self.week_day == 1
                    and self.days_played > 0
                ):
                        self.new_week()
                    elif self.flags.last_reset != self.day and self.days_played > 0:
                        self.new_day()
                if needs:
                    for n in ["energy", "grooming", "fun", "hunger"]:
                        hero[n] = hero[n].decay(duration)
            
            self.update_rooms()
        
        @property
        def active_date(self):
            try:
                date = self.date
                if date is not None:
                    return date
            except:
                pass
            return NoDateEvent()
        
        @active_date.setter
        def active_date(self, value):
            if value is None:
                del self.date
            elif isinstance(value, DateEvent):
                self.date = value
        
        @staticmethod
        def notify(string, duration=2):
            NOTIFICATIONS.append([string, duration])
        
        @staticmethod
        def story_heartbeat():
            
            
            if hasattr(store, "DONE") and not STORY_HOLD:
                ts = int(time.time())
                if ts > store.LAST_HEARTBEAT + 3:
                    store.LAST_HEARTBEAT = ts
                    storytracker.process()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
