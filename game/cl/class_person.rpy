





init -16 python:



    class Person(ParentRegistry, Countered, Flagged):
        @classmethod
        def find(cls, person):
            id = get_person_id(person)
            if id is None:
                return None
            return super(Person, cls).find(id)
        
        @classmethod
        def is_not_hidden(cls, id):
            person = cls.find(id)
            return person is not None and not person.hidden
        
        @staticmethod
        def all_people(ignore_hidden=True):
            
            return Person.filter(lambda x: not ignore_hidden or not x.hidden)
        
        @staticmethod
        def all_hidden_people():
            return Person.filter(lambda x: x.hidden)
        
        @staticmethod
        def get_fiances():
            return Person.filter(
            lambda x: not x.hidden and (x.flags.engagedmc or x.flags.engagedmike)
        )
        
        @staticmethod
        def get_housemates(ignore_hidden=True):
            housemates = [
            p for p in [bree, sasha, mike, minami] if not ignore_hidden or not p.hidden
        ]
            if hero.is_male and Harem.find_by_name("home", is_active=False):
                if Harem.find_by_name("home", is_active=False).is_active(samantha):
                    housemates.append(samantha)
                if Harem.find_by_name("home", is_active=False).is_active("lexi"):
                    housemates.append(lexi)
            return housemates
        
        def __init__(self, id, yaml):
            
            YAML[id] = yaml
            
            Flagged.__init__(
            self, id, default_flags=yaml["flags"] if "flags" in yaml else None
        )
            
            self.schedule = "default"
            self.counters = CountersShortcut(self.id)
            self.piercings = Piercings(
            self.id, yaml["piercings"] if "piercings" in yaml else {}
        )
            self.traits = TraitsShortcut(self, yaml["traits"])
            
            if persistent.last_mc_female_name and id == "bree":
                self.name = persistent.last_mc_female_name[0].capitalize()
            elif persistent.last_mc_male_name and id == "mike":
                self.name = persistent.last_mc_male_name[0].capitalize()
            else:
                self.name = yaml["name"]
            
            if persistent.last_mc_female_name and id == "bree":
                self.family_name = persistent.last_mc_female_name[1].capitalize()
            elif persistent.last_mc_male_name and id in ["mike", "minami", "angela"]:
                self.family_name = persistent.last_mc_male_name[1].capitalize()
            else:
                self.family_name = yaml.get("family_name", "")
            
            for attrname, keys in self.default_attributes.items():
                classname = attrname.capitalize()
                self.__dict__[attrname] = globals()[classname](self, **keys)
            
            self.clothes = {}
            self.room = None
            self.activity = None
            setattr(store, f"{self.id}_name", self.name)
            self.say = DynamicCharacter(
            f"{self.id}_name",
            who_outlines=[(1, "#FF00FF")],
            who_color="#ffffff",
            show_person=self,
            voice_tag=self.id,
        )
            self.gender = "female" if "gender" not in yaml else yaml["gender"]
            self.heronickname = yaml.get("heronickname", "")
        
        def __repr__(self):
            return self.name
        
        @property
        def default_attributes(self):
            return (
            YAML[self.id]["attributes"]
            if "attributes" in YAML[self.id]
            else {
                "love": {"min": 0, "max": 20, "default": 0},
                "sub": {"min": 0, "max": 100, "default": 0},
                "lesbian": {"min": 0, "max": 20, "default": 0},
                "sexperience": {"min": 0, "max": None, "default": 0},
            }
        )
        
        def __setattr__(self, attr, val):
            if attr == "status":
                
                
                if val == "girlfriend":
                    self.flags.girlfriend = True
                if val == "boyfriend":
                    self.flags.boyfriend = True
                self.flags.previous_status = self.status
                self.flags.status = val
            elif attr == "collared":
                self.flags.collared = val
            elif attr == "schedule":
                self.flags.schedule = val
            
            elif attr in self.__dict__ and isinstance(self.__dict__.get(attr), Stat):
                self.__dict__[attr].val = val
            else:
                self.__dict__[attr] = val
        
        def __getitem__(self, attr):
            return self.__getattr__(attr)
        
        def __setitem__(self, attr, val):
            return self.__setattr__(attr, val)
        
        def __call__(self):
            return self.name
        
        def __getattr__(self, attr):
            
            if attr == "id":
                return self.__dict__[attr] if attr in self.__dict__ else None
            elif attr == "collared":
                return self.is_collared
            elif self.id is not None and attr in YAML.get(self.id, {}):
                return YAML[self.id][attr]
            try:
                return self.__dict__[attr]
            except KeyError:
                raise AttributeError(attr)
        
        @property
        def is_female(self):
            return self.gender == "female"
        
        @property
        def is_male(self):
            return self.gender == "male"
        
        @property
        def personal_pronoun(self):
            if self.is_male:
                return "him"
            else:
                return "her"
        
        @property
        def subject_pronoun(self):
            if self.is_male:
                return "he"
            else:
                return "she"
        
        @property
        def possessive_pronoun(self):
            if self.is_male:
                return "his"
            else:
                return "hers"
        
        @property
        def possessive_adjective(self):
            if self.is_male:
                return "his"
            else:
                return "her"
        
        @property
        def outfits(self):
            return YAML[self.id]["outfits"] if "outfits" in YAML[self.id] else []
        
        @property
        def expressions(self):
            return YAML[self.id]["expressions"] if "expressions" in YAML[self.id] else []
        
        @property
        def heroname(self):
            return get_hero_nickname(self.id)
        
        @property
        def status(self):
            if "status" in self.flags:
                return self.flags.status
            if "status" in YAML[self.id]:
                status = YAML[self.id]["status"]
                if "[hero.name]" in status:
                    status = status.replace("[hero.name]", hero.name)
                elif "[bree.name]" in status:
                    if hero.gender == "female":
                        status = status.replace("[bree.name]", hero.name)
                    elif Person.find("bree"):
                        status = status.replace("[bree.name]", bree.name)
                elif "[mike.name]" in status:
                    if hero.gender == "male":
                        status = status.replace("[mike.name]", hero.name)
                    elif Person.find("mike"):
                        status = status.replace("[mike.name]", mike.name)
                return status
            return "friend"
        
        @status.setter
        def status(self, value):
            
            
            if value == "girlfriend":
                self.flags.girlfriend = True
            if value == "boyfriend":
                self.flags.boyfriend = True
            self.flags.previous_status = self.status
            self.flags.status = value
        
        @property
        def schedule(self):
            return self.get_schedule()
        
        @schedule.setter
        def schedule(self, value):
            self.flags.schedule = value
        
        @property
        def collared(self):
            return self.is_collared
        
        @collared.setter
        def collared(self, value):
            self.flags.collared = value
        
        @property
        def birthday_display_name(self):
            season, birthday = self.birthday
            if birthday % 10 == 1:
                ext = "st"
            elif birthday % 10 == 2:
                ext = "nd"
            else:
                ext = "th"
            return f"{season.capitalize()} {birthday}{ext}"
        
        def get_attributes(self):
            for value in self.__dict__.values():
                if isinstance(value, Attribute):
                    yield value
        
        def get_harems(self, **kwargs):
            return Harem.find(self.id, **kwargs)
        
        @staticmethod
        def showdown(*people):
            
            people = sorted(people, key=lambda person: person.sexperience.last)
            
            for person in people:
                if person.sexperience == 0:
                    return False
            if game.days_played - people[-1].sexperience.last >= 7:
                return False
            if people[-1].sexperience.last - people[0].sexperience.last >= 7:
                return False
            return True
        
        def discover_trait(self):
            
            
            self.traits.discover()
        
        def get_attention_needed(self):
            
            if persistent.difficulty < 1 or (
            self.flags.last_date_day <= 0 and self.sexperience <= 0
        ):
                return 0
            
            loss_from_date = (game.days_played - self.flags.last_date_day) // 7
            loss_from_sex = (game.days_played - self.sexperience.last) // 7
            return min(loss_from_date, loss_from_sex)
        
        @staticmethod
        def get_talk_subjects():
            talk_subjects = SpecificTalkSubject.valid_subjects()
            talk_subjects.extend(hero.talk_subjects_valid)
            talk_subjects.append(
            TalkSubject(name="cancel", label="cancel", icon="button_cancel")
        )
            return talk_subjects
        
        def get_clothes(self, clothes=None):
            if not clothes:
                if game.active_date.on_date(self.id):
                    if game.active_date.clothes:
                        clothes = game.active_date.clothes
                    else:
                        clothes = "casual"
                elif (
                self.room
                and game.room
                and self.room == game.room
                and self.activity.get("room", None) == game.room
                and self.activity.get("clothes", None)
            ):
                    clothes = self.activity["clothes"]
                elif game.room and Room.find(game.room).outfit:
                    clothes = Room.find(game.room).outfit
                else:
                    clothes = "casual"
            return clothes
        
        @property
        def get_chat(self):
            chat = randchoice(["love", "desire"])
            nbr = max(min(self.love // 40, 5), 0)
            if self.flags.randomChat:
                nbr = randint(0, nbr)
            return f"{self.id}_{chat}_{nbr}_{hero.gender}"
        
        def get_room(self):
            return self.room
        
        def hide(self):
            self.flags.hidden = True
            
            hero.calendar.find_and_remove(girl=self.id)
        
        def set_room(self, temp_room=None):
            
            if self.flags.forceLocation == (game.days_played, game.hour, self.room):
                return
            elif temp_room is None:
                self.set_activity()
                temp_room = self.activity.get("room", "none")
            
            if (
            self.room != temp_room
            and self.room is not None
            and Room.find(self.room) is not None
        ):
                try:
                    Room.find(self.room).present_girls.remove(self)
                except ValueError:
                    pass
            self.room = temp_room
            if (
            Room.find(self.room) is not None
            and self not in Room.find(self.room).present_girls
        ):
                Room.find(self.room).present_girls.append(self)
        
        @property
        def present(self):
            return game.room == self.room and not self.hidden
        
        def desire_bonus(self):
            if not self.flags.desireBonusDone:
                self.flags.desireBonusDone = TemporaryFlag(True, 1)
                bonus = 0
                for d in self.desire_factors:
                    if d in ["fitness", "charm", "knowledge"]:
                        if hero[d]() * 2 > self.love:
                            bonus += 1
                    elif "not_" in d and d.replace("not_", "") in [
                    "fitness",
                    "charm",
                    "knowledge",
                ]:
                        if hero[d.replace("not_", "")]() * 2 > self.love:
                            bonus -= 1
                    elif d == "career":
                        if game.flags.promoted * 10 >= self.love:
                            bonus += 1
                    elif hero.has_skill(d):
                        bonus += 1
                    elif "not_" in d and hero.has_skill(d.replace("not_", "")):
                        bonus -= 1
                    elif d == "money":
                        if hero.money >= 100 + self.love * self.love:
                            bonus += 1
                    elif hero.equipment["clothes"] or hero.equipment["accessory"]:
                        if hero.equipment["clothes"]:
                            for e in hero.equipment["clothes"].effects:
                                if e[0] == d and randint(1, 100) <= e[1]:
                                    bonus += 1
                        if hero.equipment["accessory"]:
                            for e in hero.equipment["accessory"].effects:
                                if e[0] == d and randint(1, 100) <= e[1]:
                                    bonus += 1
                    elif d == "injured" and game.flags.injured:
                        bonus += 1
                    elif d == "sickness" and game.flags.sick:
                        bonus += 1
                if bonus < 0 and self.love >= 190:
                    bonus = 0
                if bonus:
                    self.love += bonus
        
        def get_activity(self, hour="Now"):
            if hour != "Now":
                if hour > 23:
                    hour = 0
                    day = game.calendar.day_of_week + 1
                    if day > 7:
                        day = 1
                else:
                    day = game.calendar.day_of_week
            else:
                hour = game.hour
                day = game.calendar.day_of_week
            day = str(day)
            schedule = self.get_schedule()
            for k in schedule.keys():
                if day in k:
                    break
            hours = sorted([int(a) for a in schedule[k].keys()])
            for a in hours:
                if hour <= a:
                    break
            a = str(a)
            if game.active_date.on_date(self.id):
                if game.active_date.clothes:
                    result = {
                    "activity": "date",
                    "clothes": game.active_date.clothes,
                    "room": game.room,
                }
                else:
                    result = {"activity": "date", "clothes": "casual", "room": game.room}
            else:
                if (
                not self.flags[f"activity-{day}-{a}"]
                or self.flags[f"activity-{day}-{a}"].get("activity") == "date"
            ):
                    r = self.flags[k + a]
                    if r:
                        result = r
                    else:
                        tmp_list = []
                        for c in schedule[k][a]:
                            if (
                            "seasons" in c.keys()
                            and str(game.season) not in c["seasons"]
                        ):
                                continue
                            if "conditions" in c.keys():
                                
                                tmp_cond_list = all(
                                [safe_eval(cond) for cond in c["conditions"]]
                            )
                                if not tmp_cond_list:
                                    continue
                            tmp_list.append(c)
                        if tmp_list:
                            if persistent.schedule_randomness:
                                result = randchoice(tmp_list)
                                self.flags[k + str(a)] = TemporaryFlag(result, 1)
                            else:
                                result = tmp_list[0]
                                self.flags[k + str(a)] = TemporaryFlag(result, 1)
                        else:
                            _, result = self.get_activity(hour=int(a) + 1)
                else:
                    result = self.flags[f"activity-{day}-{a}"]
            return a, result
        
        @property
        def activity_name(self):
            _, _activity = self.get_activity()
            return _activity.get("activity")
        
        def set_activity(self):
            a, self.activity = self.get_activity()
            self.flags[f"activity-{game.week_day}-{a}"] = TemporaryFlag(
            self.activity, "day"
        )
        
        
        
        def get_schedule(self):
            schedule_name = self.flags.schedule
            if not schedule_name:
                self.schedule = "default"
                schedule_name = "default"
            return YAML[self.id]["schedule"].get(schedule_name)
        
        @property
        def is_sex_slave(self):
            return self.status == "sex slave" and self.sub >= 75
        
        @property
        def is_collared(self):
            return self.flags.collared and self.sub >= 50
        
        @property
        def is_girlfriend(self):
            return self.status in ["girlfriend", "fiance", "mistress", "pet", "sex slave"]
        
        @property
        def is_boyfriend(self):
            return self.status in ["boyfriend", "fiance", "master", "pet", "sex slave"]
        
        def set_gone_forever(self):
            self.love.val = 0
            self.love.max = 0
            self.flags.gone_forever = True
            self.hide()
            for harem in self.get_harems():
                harem.leave(self.id)
            
            if self.id in hero.smartphone_contacts:
                hero.smartphone_contacts.remove(self.id)
        
        @property
        def is_gone_forever(self):
            return self.flags.gone_forever
        
        def breakup(self):
            self.flags.breakup = True
            self.flags.friendzone = True
            self.flags.engagedmc = False
            self.flags.topless = False
            self.flags.bottomless = False
            self.flags.naked = False
            if self.is_male:
                self.flags.engagedmike = False
                self.flags.boyfriend = False
                self.flags.mikeNickname = None
            else:
                self.flags.girlfriend = False
                self.flags.breeNickname = None
            if self.status in ["girlfriend", "fiance", "boyfriend"]:
                self.status = "ex-" + self.status
            else:
                self.status = "just friend"
            for harem in Harem.find(self, is_active=True):
                harem.breakup(self)
            if self.sexperience >= 1:
                self.love -= 25
        
        def friendzone(self):
            self.flags.friendzone = True
            self.flags.engagedmc = False
            self.flags.topless = False
            self.flags.bottomless = False
            self.flags.naked = False
            if self.is_male:
                self.flags.engagedmike = False
                self.flags.boyfriend = False
                self.flags.mikeNickname = None
            else:
                self.flags.girlfriend = False
                self.flags.breeNickname = None
            self.status = "just friend"
            for harem in Harem.find(self, is_active=True):
                harem.breakup(self)
            if self.sexperience >= 1:
                self.love -= 15
        
        def set_sex_slave(self):
            self.collared = True
            self.status = "sex slave"
            if hero.gender == "male":
                self.flags.mikeNickname = "Master"
            else:
                self.flags.breeNickname = "Mistress"
        
        @staticmethod
        def are_in_same_room_now(
        people,
        schedule_randomness=persistent.schedule_randomness,
        room=None,
        is_tag=False,
        filter_by_room_tag=False,
    ):
            same_rooms_schedule = Person.is_in_same_room(
            people, schedule_randomness, room, is_tag, filter_by_room_tag
        )
            for same_room in same_rooms_schedule:
                if game.get_day_str(game.week_day) == same_room[0] and game.hour == int(
                same_room[1]
            ):
                    return True
            return False
        
        @staticmethod
        def is_in_same_room(
        people,
        schedule_randomness=persistent.schedule_randomness,
        room=None,
        is_tag=False,
        filter_by_room_tag=False,
    ):
            if not people:
                raise Exception("No people for comparison")
            elif not isinstance(people, list):
                raise Exception("Input people as a list")
            elif len(people) == 1:
                raise Exception("Multiple people required for function")
            first_person_done = False
            for person in people:
                if not first_person_done:
                    if room:
                        full_schedule = person.get_times_in_room(
                        room=room,
                        is_tag=is_tag,
                        schedule_randomness=schedule_randomness,
                    )
                    else:
                        full_schedule = person.get_full_schedule(
                        schedule_randomness=schedule_randomness
                    )
                    first_person_done = True
                    if filter_by_room_tag:
                        time_in_same_room = [
                        (day, hour, Room.find(hour_activity["room"]).tags)
                        for day in full_schedule
                        for hour in full_schedule[day]
                        for hour_activity in full_schedule[day][hour]
                        if Room.find(hour_activity["room"])
                        and Room.find(hour_activity["room"]).tags
                    ]
                    else:
                        time_in_same_room = [
                        (day, hour, hour_activity["room"])
                        for day in full_schedule
                        for hour in full_schedule[day]
                        for hour_activity in full_schedule[day][hour]
                    ]
                else:
                    full_schedule = person.get_full_schedule(
                    schedule_randomness=schedule_randomness
                )
                    if filter_by_room_tag:
                        person_time_in_same_room = [
                        (day, hour, Room.find(hour_activity["room"]).tags)
                        for day in full_schedule
                        for hour in full_schedule[day]
                        for hour_activity in full_schedule[day][hour]
                        if Room.find(hour_activity["room"])
                        and Room.find(hour_activity["room"]).tags
                    ]
                    else:
                        person_time_in_same_room = [
                        (day, hour, hour_activity["room"])
                        for day in full_schedule
                        for hour in full_schedule[day]
                        for hour_activity in full_schedule[day][hour]
                    ]
                    time_in_same_room = [
                    entry
                    for entry in time_in_same_room
                    if entry in person_time_in_same_room
                ]
            return [
            (game.calendar.get_day_of_week_name(nbr=day), hour, room)
            for day, hour, room in time_in_same_room
        ]
        
        def find_times_in_same_room(
        self,
        people,
        schedule_randomness=persistent.schedule_randomness,
        room=None,
        is_tag=False,
    ):
            if not people:
                raise Exception("No people for comparison")
            elif not isinstance(people, list):
                raise Exception("Input people as a list")
            return Person.is_in_same_room(
            people=[self] + people,
            room=room,
            is_tag=is_tag,
            schedule_randomness=schedule_randomness,
        )
        
        
        def get_times_in_room(
        self,
        room,
        schedule_randomness=persistent.schedule_randomness,
        is_tag=False,
        all_schedules=False,
    ):
            if all_schedules:
                schedule = self.get_full_schedules(schedule_randomness=schedule_randomness)
            else:
                schedule = self.get_full_schedule(schedule_randomness=schedule_randomness)
            times_in_room = {}
            for day in schedule:
                times_in_room[day] = {}
                for hour in schedule[day]:
                    times_in_room[day][hour] = []
                    for hour_activity in schedule[day][hour]:
                        if is_tag:
                            if Room.has_tag(hour_activity["room"], room):
                                times_in_room[day][hour].append(hour_activity)
                        else:
                            if hour_activity["room"] == room:
                                times_in_room[day][hour].append(hour_activity)
                    if not times_in_room[day][hour]:
                        del times_in_room[day][hour]
            return times_in_room
        
        def get_full_schedule(self, schedule_randomness=persistent.schedule_randomness):
            full_schedule = {}
            for day in self.schedule:
                generated_day = {}
                start_hour = 0
                for hour in self.schedule[day]:
                    for activity_hour in range(start_hour, int(hour) + 1):
                        if schedule_randomness:
                            generated_day[str(activity_hour)] = self.schedule[day][hour]
                        else:
                            generated_day[str(activity_hour)] = [
                            self.schedule[day][hour][0]
                        ]
                    start_hour = int(hour) + 1
                for hour in range(start_hour, 24):
                    generated_day[str(hour)] = [
                    OrderedDict({"room": "None", "activity": "None", "clothes": "None"})
                ]
                for sub_day in list(day):
                    full_schedule[sub_day] = generated_day
            return full_schedule
        
        def get_full_schedules(self, schedule_randomness=persistent.schedule_randomness):
            full_schedules = {}
            for schedule_name in YAML[self.id]["schedule"]:
                current_schedule = YAML[self.id]["schedule"][schedule_name]
                full_schedule = {}
                for day in current_schedule:
                    generated_day = {}
                    start_hour = 0
                    for hour in current_schedule[day]:
                        for activity_hour in range(start_hour, int(hour) + 1):
                            if schedule_randomness:
                                generated_day[str(activity_hour)] = current_schedule[day][
                                hour
                            ]
                            else:
                                generated_day[str(activity_hour)] = [
                                current_schedule[day][hour][0]
                            ]
                        start_hour = int(hour) + 1
                    for hour in range(start_hour, 24):
                        generated_day[str(hour)] = [
                        OrderedDict(
                            {"room": "None", "activity": "None", "clothes": "None"}
                        )
                    ]
                    for sub_day in list(day):
                        full_schedule[sub_day] = generated_day
                full_schedules[schedule_name] = full_schedule
            merged_schedules = {}
            for schedule_name, schedule in full_schedules.items():
                for day, hours in schedule.items():
                    for hour, activities in hours.items():
                        if day not in merged_schedules:
                            merged_schedules[day] = {hour: activities}
                        elif hour not in merged_schedules[day]:
                            merged_schedules[day][hour] = activities
                        else:
                            merged_schedules[day][hour].extend(activities)
            return merged_schedules
        
        @property
        def is_upset(self):
            return bool(
            (self.activity["clothes"] == "naked" and self.love < 140)
            or (self.activity["clothes"] in ["towel", "underwear"] and self.love < 100)
            or (self.id == "sasha" and self.flags.cheated)
            or (
                self.id == "minami"
                and self.activity["clothes"] == "naked"
                and self.siscon < 70
            )
            or (
                self.id == "minami"
                and self.activity["clothes"] == "underwear"
                and self.siscon < 50
            )
            
        )
        
        @property
        def on_date(self):
            return self.id in game.active_date.participants


    class PersonWrapper:
        """
    Wrapper that specifically wraps a person class.

    This keeps a local _id of where to look in DATA_WRAPPERS for, where we
    store which person this is wrapping. Then fetch the actual object out
    of the Person registry.

    That way it doesn't really matter if this object gets pickled and put
    into the store.
    """
        
        def __init__(self, id, obj=None):
            """
        @param id
          The ID in the store used to identify the current version of this object
        @param obj
          The initial obj
        """
            self._id = id
            self.id = obj
        
        def __getstore__(self):
            """Internal method to get DATA_WRAPPERS, potentially before it exists."""
            if not hasattr(store, "DATA_WRAPPERS"):
                setattr(store, "DATA_WRAPPERS", {})
            return getattr(store, "DATA_WRAPPERS")
        
        @property
        def id(self):
            """Get the current object's id."""
            wrappers = self.__getstore__()
            if self._id not in wrappers:
                return None
            return wrappers[self._id]
        
        @id.setter
        def id(self, person):
            """Set the wrapped object's id mid-flight. None is acceptable."""
            
            self.__getstore__()[self._id] = get_person_id(person)
        
        @property
        def object(self):
            """Get the current object."""
            return Person.find(self.id)
        
        @object.setter
        def object(self, person):
            """Set the wrapped object mid-flight. None is acceptable."""
            self.id = person
        
        def __getattr__(self, attr):
            """Provide proxy access to attributes of wrapped object."""
            
            
            
            
            
            if attr.startswith("_"):
                raise AttributeError(attr)
            return getattr(self.object, attr)
        
        def __setattr__(self, attr, val):
            """Provide proxy write access to attributes of wrapped object."""
            
            if attr.startswith("_") or isinstance(
            getattr(self.__class__, attr, None), property
        ):
                super(PersonWrapper, self).__setattr__(attr, val)
            else:
                setattr(self.object, attr, val)
        
        def __getitem__(self, attr):
            """Provide dict-like access to attributes of wrapped object."""
            try:
                return self.__getattr__(attr)
            except AttributeError:
                raise KeyError(attr)
        
        def __setitem__(self, attr, val):
            """Provide dict-like write access to attributes of wrapped object."""
            return self.__setattr__(attr, val)
        
        def say(self, *args, **kwargs):
            """Guarantee say exists for the linter."""
            if self.object is None:
                return renpy.say("", *args, **kwargs)
            else:
                return self.object.say(*args, **kwargs)
        
        def __bool__(self):
            return self.id is not None
        
        def __len__(self):
            
            return 1 if self.id is not None else 0
        
        def __eq__(self, other):
            return self.id == get_person_id(other)
        
        def __ne__(self, other):
            return self.id != get_person_id(other)


    def get_person_id(person):
        
        
        
        
        if isinstance(person, basestring):
            if any(
            sub_cls.find(person) is not None
            for sub_cls in Person.__subclasses__()
            if issubclass(sub_cls, Registry)
        ):
                
                return person
            if hasattr(store, "DATA_WRAPPERS") and person in DATA_WRAPPERS:
                
                return DATA_WRAPPERS[person]
        if isinstance(person, (Person, PersonWrapper)):
            
            return person.id
        
        return None



init 1 python:



    def hide_people():
        if renpy.showing("roomleft", "master"):
            renpy.hide("roomleft", layer="master")
        if renpy.showing("roomright", "master"):
            renpy.hide("roomright", layer="master")
        showexpr = game.flags.room_showing_people or []
        for expr in showexpr:
            if renpy.showing(expr[0], "master"):
                renpy.hide(expr[1], layer="master")
        return None


    def show_people():
        
        showexpr = [
        (g, o)
        for g, o in (game.flags.room_showing_people or [])
        if not (persistent.lively_bg and g in Room.find(game.room).lively_npc)
    ]
        if len(showexpr) == 1:
            renpy.show(showexpr[0][0], what=showexpr[0][1], layer="master")
        elif len(showexpr) == 2:
            renpy.show(showexpr[0][0], what=showexpr[0][1], at_list=[left], layer="master")
            renpy.show(showexpr[1][0], what=showexpr[1][1], at_list=[right], layer="master")
        elif len(showexpr) == 3:
            renpy.show(showexpr[0][0], what=showexpr[0][1], at_list=[left], layer="master")
            renpy.show(showexpr[1][0], what=showexpr[1][1], layer="master")
            renpy.show(showexpr[2][0], what=showexpr[2][1], at_list=[right], layer="master")
        return None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
