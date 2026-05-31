



init -15 python:



    class Date(Conditioned):
        def __init__(
        self,
        name,
        grooming=0,
        fun=0,
        hunger=0,
        energy=0,
        knowledge=0,
        fitness=0,
        charm=0,
        money_cost=0,
        display_name=None,
        clothes="casual",
        love_gain=1,
        max_time=4,
        conditions=None,
        bypass_greetings=False,
    ):
            super(Date, self).__init__(name, conditions)
            
            min_energy_check = False
            min_hunger_check = False
            min_grooming_check = False
            min_fun_check = False
            for condition in self.conditions:
                if isinstance(condition, HeroTarget):
                    for checker in condition.checkers:
                        if isinstance(checker, MinStat):
                            if checker._stat_name == "energy":
                                min_energy_check = True
                            elif checker._stat_name == "hunger":
                                min_hunger_check = True
                            elif checker._stat_name == "grooming":
                                min_grooming_check = True
                            elif checker._stat_name == "fun":
                                min_fun_check = True
            checkers = []
            if not min_energy_check:
                checkers.append(MinStat("energy", 1))
            if not min_hunger_check:
                checkers.append(MinStat("hunger", 1))
            if not min_grooming_check:
                checkers.append(MinStat("grooming", 1))
            if not min_fun_check:
                checkers.append(MinStat("fun", 1))
            if len(checkers) != 0:
                conditions.append(HeroTarget(*checkers))
            
            self.name = name
            self.display_name = display_name if display_name else self.name.capitalize()
            self.clothes = clothes
            self.money_cost = money_cost
            self.needs = {
            "energy": energy,
            "grooming": grooming,
            "fun": fun,
            "hunger": hunger,
        }
            self.attributes = {"knowledge": knowledge, "fitness": fitness, "charm": charm}
            self.duration = 4
            self.love_gain = love_gain
            self.max_time = max_time
            self.tooltip = ""
            self.bypass_greetings = bypass_greetings
            
            self.abort = False
            self.stay = True
            self.stay_coffee = True
            
            if self.id not in DATES:
                DATES[self.id] = self
        
        def get_tooltip(self):
            tool_tip = []
            for need in self.needs:
                tip = f"{{image=gui/icons/icon_{need}.png}}{'+' if self.needs[need] > 0 else ''}"
                if need == "hunger":
                    needs_value = hero.hunger.get_decayed_action_value(
                    self.needs[need], self.duration
                )
                elif need == "grooming":
                    needs_value = hero.grooming.get_decayed_action_value(
                    self.needs[need], self.duration
                )
                elif need == "fun":
                    needs_value = hero.fun.get_decayed_action_value(
                    self.needs[need], self.duration
                )
                elif need == "energy":
                    needs_value = hero.energy.get_decayed_action_value(
                    self.needs[need], self.duration
                )
                decimal, needs_value = modf(needs_value)
                if persistent.needs_randomness:
                    chances = str(int(abs(decimal * 100))) + "%"
                    if decimal > 0.0:
                        tip += f"({int(needs_value)}/{chances}→{int(needs_value + 1)})"
                    elif decimal < 0.0:
                        tip += f"({int(needs_value)}/{chances}→{int(needs_value - 1)})"
                    else:
                        tip += f"{int(needs_value)}"
                else:
                    if not decimal:
                        tip += f"{int(needs_value)}"
                    else:
                        tip += f"{needs_value + decimal}"
                if needs_value != 0 or decimal != 0:
                    tool_tip.append(tip)
            for attribute in self.attributes:
                if self.attributes[attribute] != 0:
                    tip = f"{{image=gui/icons/icon_{attribute}.png}}{'+' if self.attributes[attribute] > 0 else ''}"
                    needs_value = self.attributes[attribute]
                    needs_value *= game.get_difficulty_mod(needs_value)
                    decimal, needs_value = modf(needs_value)
                    if decimal:
                        tip += f"({int(needs_value)}→{int(needs_value) + 1})"
                    else:
                        tip += f"{int(needs_value)}"
                    tool_tip.append(tip)
            if self.money_cost:
                tool_tip.append(f"{{image=gui/icons/icon_money.png}}-{self.money_cost}")
            if self.max_time:
                tool_tip.append(f"{{image=gui/icons/icon_clock.png}}+{self.max_time}")
            if self.tooltip:
                tool_tip = [self.tooltip] + tool_tip
            return tool_tip


    class DateEvent(object):
        def __init__(
        self,
        score=0,
        participants=None,
        clothes=None,
        skip_nightclub=False,
        *args,
        **kwargs,
    ):
            if participants is None:
                participants = []
            elif isinstance(participants, basestring):
                participants = [participants]
            elif isinstance(participants, tuple):
                participants = list(participants)
            self.score = score
            self.location = None
            self.participants = participants
            self.skip_nightclub = skip_nightclub
            
            self._clothes = clothes
        
        def on_date(self, girl):
            return get_person_id(girl) in self.participants
        
        @property
        def roaming(self):
            return False


    class DateAppointment(Appointment, DateEvent):
        def __init__(
        self,
        hours,
        participants,
        name=None,
        label=None,
        fail_label=None,
        *args,
        **kwargs,
    ):
            
            if participants is None:
                raise Exception("Expected a Person to create a Date")
            
            if not isinstance(participants, list):
                participants = [participants]
            DateEvent.__init__(
            self, participants=[get_person_id(x) for x in participants], *args, **kwargs
        )
            
            self.label = label
            self.fail_label = fail_label
            
            
            appointment_name = name if name else "Date (" + self._m1_class_date__participant_names() + ")"
            
            Appointment.__init__(self, hours, appointment_name)
        
        def _m1_class_date__participant_names(self):
            return " & ".join(Person.find(x).name for x in self.participants)
        
        def fail(self):
            if (
            hasattr(self, "fail_label")
            and self.fail_label is not None
            and renpy.has_label(self.fail_label)
        ):
                renpy.call_in_new_context(self.fail_label)
            else:
                
                if game.room == "map":
                    game.room = "street"
                
                for participant in self.participants:
                    if Person.find(participant):
                        Person.find(participant).love -= 10
                if any(Person.find(participant) for participant in self.participants):
                    renpy.say(
                    "", "Shit I missed my date with " + self._m1_class_date__participant_names() + "."
                )
        
        def find(self, **kwargs):
            
            if not kwargs:
                return False
            kwargs_npc = kwargs.get("npc", kwargs.get("girl"))
            kwargs_label = kwargs.get("label")
            
            def is_matching_npc():
                return kwargs_npc and self.on_date(kwargs_npc)
            
            def is_matching_label():
                return (
                kwargs_label and hasattr(self, "label") and self.label == kwargs_label
            )
            
            if kwargs_npc and kwargs_label:
                return is_matching_npc() and is_matching_label()
            if kwargs_npc:
                return is_matching_npc()
            if kwargs_label:
                return is_matching_label()
            
            return False
        
        def do(self):
            if hasattr(self, "label") and self.label is not None:
                if self.label not in DONE_HOUR:
                    DONE_HOUR.append(self.label)
                DONE[self.label] = game.days_played
                return self.label
            else:
                return "date_do_date"
        
        @property
        def clothes(self):
            if hasattr(self, "_clothes") and self._clothes:
                return self._clothes
            if self.location and self.location.clothes:
                return self.location.clothes
            return None
        
        @clothes.setter
        def clothes(self, value):
            self._clothes = value


    class NoDateEvent(DateEvent):
        @property
        def score(self):
            return 0
        
        @score.setter
        def score(self, value):
            pass
        
        @property
        def location(self):
            return None
        
        @location.setter
        def location(self, value):
            pass
        
        def __bool__(self):
            return False
        
        def __len__(self):
            
            return 0


    class ScavengerHuntAppointment(DateAppointment):
        """
    The base is the base used to construct the labels
    base + "_start" is the label shown upon starting the date.
    base + "_clue_X" is the label shown to get the clue.
    base + "_guess_X" is the label shown when guessing the clue.
    This should return True for correct and False for incorrect.
    base + "_finish" is the label shown when finishing the hunt.
    Length should never take us past midnight!
    """
        
        def __init__(
        self,
        hours,
        girl_id,
        base,
        start_location="street",
        length=4,
        max_attempts=3,
        points_per_attempt=10,
        **kwargs,
    ):
            DateAppointment.__init__(self, hours, girl_id, **kwargs)
            self.base = base
            self.total = 0
            self.current_clue = 1
            self.current_attempts = 0
            self.start_location = start_location
            self.end = game.hour + length
            self.max_attempts = max_attempts
            self.points_per_attempt = points_per_attempt
            self.tried = set()
        
        def do(self):
            return "scavenger_do_date"
        
        @property
        def roaming(self):
            return True
        
        @property
        def clothes(self):
            return "casual"
        
        @clothes.setter
        def clothes(self, value):
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
