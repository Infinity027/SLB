



init -21 python:



    class BaseActivity(ParentRegistry, Action):
        def __init__(
        self,
        name,
        say=None,
        icon=None,
        notification=False,
        order=0,
        
        duration=1,
        **kwargs,
    ):
            if icon is None:
                raise Exception("Activity '%s' missing icon" % self.id)
            
            
            kwargs["duration"] = duration
            super(BaseActivity, self).__init__(name, **kwargs)
            
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
                            elif checker._stat_name == "fun":
                                min_fun_check = True
                            elif checker._stat_name == "grooming":
                                min_grooming_check = True
                            elif checker._stat_name == "hunger":
                                min_hunger_check = True
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
                self.conditions.append(HeroTarget(*checkers))
            
            self.say = say if say is not None else []
            self.icon = icon
            self.tooltip = ""
            self.notification = notification
            self.order = order
            
            
            self.action = {"action": None, "parameter": None}
        
        def __hash__(self):
            return hash(self.name)
        
        def __eq__(self, other):
            if isinstance(other, BaseActivity):
                return self.name == other.name
            return self.name == other
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def notify(self):
            if (
            hasattr(self, "notification")
            and self.notification
            and not [f"{{size=20}}{self.notification}{{/size}}", 2] in NOTIFICATIONS
            and not game.flags[f"{self.id}!last_notify"] == game.hour
        ):
                game.flags[f"{self.id}!last_notify"] = game.hour
                NOTIFICATIONS.append([f"{{size=20}}{self.notification}{{/size}}", 2])
        
        def get_tooltip(self):
            tt = []
            if self.tooltip:
                tt.append(self.tooltip)
            tt.extend(self.get_needs_tooltip())
            tt.extend(self.get_attributes_tooltip())
            tt.extend(self.get_money_tooltip())
            tt.extend(self.get_duration_tooltip())
            return tt
        
        def get_needs_tooltip(self):
            tooltips = []
            for need, value in self.needs.items():
                
                if value == 0:
                    continue
                
                decimal, value = modf(value)
                value = int(value)
                tooltip = "{{image=gui/icons/icon_{}.png}}".format(need)
                if persistent.needs_randomness and decimal != 0:
                    tooltip += "({:+}/{}%→{:+0.2f})".format(
                    value,
                    int(abs(decimal * 100)),
                    value + 1 if decimal > 0 else value - 1,
                )
                elif decimal != 0:
                    tooltip += "{:+0.2f}".format(value + decimal)
                else:
                    tooltip += "{:+}".format(value)
                
                tooltips.append(tooltip)
            return tooltips
        
        def get_attributes_tooltip(self):
            tooltips = []
            for attribute, value in self.attributes.items():
                
                if value == 0:
                    continue
                
                value *= Game.get_difficulty_mod(value)
                decimal, value = modf(value)
                value = int(value)
                
                tooltip = "{{image=gui/icons/icon_{}.png}}".format(attribute)
                if decimal != 0:
                    tooltip += "({:+}/{}%→{:+})".format(
                    value,
                    int(abs(decimal * 100)),
                    value + 1 if decimal > 0 else value - 1,
                )
                else:
                    tooltip += "{:+}".format(value)
                
                tooltips.append(tooltip)
            return tooltips
        
        def get_money_tooltip(self):
            money_gain = self.get_money_gain()
            if money_gain == 0:
                return []
            return ["{{image=gui/icons/icon_money.png}}{:+}".format(money_gain)]
        
        def get_duration_tooltip(self):
            if self.duration == 0:
                return []
            return ["{{image=gui/icons/icon_clock.png}}{:+}h".format(self.duration)]
        
        @classmethod
        def valid_activities(cls):
            if hasattr(cls, "_cache") and cls._cache is not None:
                
                if game.room in cls._cache:
                    for activity in cls._cache[game.room]:
                        if activity.test():
                            activity.notify()
                            yield activity
                
                if None in cls._cache:
                    for activity in cls._cache[None]:
                        if activity.test():
                            activity.notify()
                            yield activity
            else:
                for activity in cls.sorted_filter(
                
                key=lambda x: (x.order, x.display_name),
                
                filter=lambda x: x.test(),
            ):
                    activity.notify()
                    yield activity


    class Activity(CachedRegistry, BaseActivity):
        """normal activities."""
        
        def __init__(self, name, **kwargs):
            
            super(Activity, self).__init__(name, **kwargs)


    class InteractActivity(CachedRegistry, BaseActivity):
        """activities that require an interaction with a character."""
        
        def __init__(self, name, **kwargs):
            
            super(InteractActivity, self).__init__(name, **kwargs)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
