



init -22 python:



    class Action(Conditioned):
        def __init__(
        self,
        name,
        label=None,
        display_name=None,
        duration=0,
        music=None,
        rooms=None,
        
        energy=0,
        hunger=0,
        grooming=0,
        fun=0,
        
        knowledge=0,
        fitness=0,
        charm=0,
        
        money_gain=None,
        money_cost=0,
        
        do_once=False,
        once_hour=False,
        once_day=False,
        every_two_days=False,
        once_week=False,
        once_month=False,
        once_year=False,
        
        min_girls=0,
        max_girls=100,
        force_new_context=False,
        disable_clothing_policy=False,
        **kwargs,
    ):
            super(Action, self).__init__(name, **kwargs)
            
            self.name = name
            self.label = label
            self.display_name = display_name if display_name else name.capitalize()
            self.duration = duration
            self.music = music
            self.rooms = rooms
            self.energy = energy
            self.hunger = hunger
            self.grooming = grooming
            self.fun = fun
            
            self.attributes = {
            "knowledge": knowledge,
            "fitness": fitness,
            "charm": charm,
        }
            
            if money_gain is None:
                self.money_gain = False
            else:
                self.money_gain = {
                "base": 5,
                "bonus": (),
                "mult": (),
                "attributes": (),
            }
                self.money_gain.update(money_gain)
            self.money_cost = money_cost
            
            self.do_once = do_once
            self.once_hour = once_hour
            self.once_day = once_day
            self.every_two_days = every_two_days
            self.once_week = once_week
            self.once_month = once_month
            self.once_year = once_year
            
            self.min_girls = min_girls
            self.max_girls = max_girls
            
            self.force_new_context = force_new_context
            self.disable_clothing_policy = disable_clothing_policy
        
        @property
        def needs(self):
            return {
            "energy": round(
                hero.energy.get_decayed_action_value(self.energy, self.duration), 2
            ),
            "fun": round(hero.fun.get_decayed_action_value(self.fun, self.duration), 2),
            "grooming": round(
                hero.grooming.get_decayed_action_value(self.grooming, self.duration), 2
            ),
            "hunger": round(
                hero.hunger.get_decayed_action_value(self.hunger, self.duration), 2
            ),
        }
        
        def play_music(self):
            if renpy.music.get_playing() != self.music:
                renpy.music.play(self.music, loop=True, fadein=0.5, fadeout=0.5)
        
        def get_money_gain(self):
            money_gain = 0
            
            if self.money_gain:
                money_gain += self.money_gain["base"]
                for bonus in self.money_gain["bonus"]:
                    if isinstance(bonus, basestring):
                        money_gain += game.flags[bonus]
                    else:
                        money_gain += bonus
                
                for mult in self.money_gain["mult"]:
                    if isinstance(mult, basestring):
                        money_gain *= game.flags[mult]
                    else:
                        money_gain *= mult
                
                for attribute in self.money_gain["attributes"]:
                    money_gain *= 1 + hero[attribute] / 400.0
                
                money_gain *= Game.get_difficulty_mod(money_gain)
                
                money_gain *= self.duration
            
            if self.money_cost > 0:
                money_gain -= self.money_cost
            
            return round(money_gain)
        
        def test(self, debug=False):
            for func in (
            self.test_label,
            self.test_duration,
            self.test_money_cost,
            self.test_do_once,
            self.test_once_hour,
            self.test_once_day,
            self.test_every_two_days,
            self.test_once_week,
            self.test_once_month,
            self.test_once_year,
            self.test_minmax_girls,
        ):
                if not func():
                    if debug:
                        print("Test Failed: {}".format(func.__name__))
                    return False
            
            return super(Action, self).test(debug)
        
        def test_label(self):
            target_label = self.label
            if isinstance(target_label, tuple):
                target_label = target_label[0]
            if not isinstance(target_label, basestring):
                if target_label is not None and config.developer:
                    raise ValueError(
                    "Invalid label '{}' for {}".format(self.label, self.name)
                )
                return True
            
            
            if not any(s in target_label for s in ("ACTIVE_GIRL", "ROOM")):
                return True
            if active_girl and "ACTIVE_GIRL" in target_label:
                target_label = target_label.replace("ACTIVE_GIRL", active_girl.id)
            if "ROOM" in target_label:
                target_label = target_label.replace("ROOM", game.room)
            return renpy.has_label(target_label)
        
        def test_duration(self):
            current_room = Room.find(game.room)
            if current_room:
                opened, closed = current_room.hours
                finish = game.hour + self.duration
                
                if closed < opened <= game.hour:
                    closed += 24
                
                return finish <= closed
            else:
                renpy.log(f"Unable to find room {game.room} for action {self.name}")
                return False
        
        def test_money_cost(self):
            return hero.money >= self.money_cost
        
        def test_do_once(self):
            if self.do_once == "ACTIVE" and active_girl:
                return f"{self.name}_{active_girl.id}" not in DONE
            if self.do_once:
                return self.name not in DONE
            return True
        
        def test_once_hour(self):
            if self.once_hour == "ACTIVE" and active_girl:
                return f"{self.name}_{active_girl.id}" not in DONE_HOUR
            if self.once_hour:
                return self.name not in DONE_HOUR
            return True
        
        def test_once_day(self):
            if self.once_day == "ACTIVE" and active_girl:
                return not self.done_today(f"{self.name}_{active_girl.id}")
            if self.once_day:
                return not self.done_today(self.name)
            return True
        
        def test_every_two_days(self):
            if self.every_two_days:
                return not self.done_yesterday(self.name)
            return True
        
        def test_once_week(self):
            if self.once_week:
                return not self.done_this_week(self.name)
            return True
        
        def test_once_month(self):
            if self.once_month:
                return not self.done_this_month(self.name)
            return True
        
        def test_once_year(self):
            if self.once_year:
                return not self.done_this_year(self.name)
            return True
        
        def test_minmax_girls(self):
            numgirls = len(Room.find(game.room).get_present_girls())
            return self.min_girls <= numgirls <= self.max_girls
        
        def examine(self, indent_level=0):
            result = ""
            
            i = "    " * indent_level
            if self.duration > 0:
                result += "{}duration: {}\n".format(i, self.duration)
            if self.money_cost > 0:
                result += "{}cost: {}\n".format(i, self.money_cost)
            if self.do_once:
                result += "{}only once\n".format(i)
            if self.once_hour and not self.do_once:
                result += "{}once an hour\n".format(i)
            if self.once_day:
                result += "{}once a day\n".format(i)
            if self.once_week:
                result += "{}once a week\n".format(i)
            if self.once_month:
                result += "{}once a month\n".format(i)
            if self.once_year:
                result += "{}once a year\n".format(i)
            if self.min_girls > 0:
                result += "{}minimum characters present: {}\n".format(i, self.min_girls)
            if self.max_girls < 100:
                result += "{}maximum characters present: {}\n".format(i, self.max_girls)
            
            result += super(Action, self).examine(indent_level)
            return result
        
        @staticmethod
        def _visual_checks(value):
            return (
            "{color=#00ff00}{font=DejaVuSans.ttf}\u2713{/font}{/color}"
            if value
            else "{color=#f00}{font=DejaVuSans.ttf}\u2717{/font}{/color}"
        )
        
        def examine_ui(self, indent_level=0):
            result = (
            f"{{b}}'{self.display_name if self.display_name else self.name}':{{/b}}\n"
        )
            
            indent = "    " * indent_level
            if self.duration > 0 and not self.test_duration():
                result += "{}{} will close soon {}\n".format(
                indent,
                Room.find(game.room).display_name,
                self._visual_checks(self.test_duration()),
            )
            if self.money_cost > 0 and not self.test_money_cost():
                result += "{}You don't have enough money: {}$ {}\n".format(
                indent, self.money_cost, self._visual_checks(self.test_money_cost())
            )
            if self.do_once and not self.test_do_once():
                result += "{}Already done {}\n".format(
                indent, self._visual_checks(self.test_do_once())
            )
            if self.once_hour and not self.do_once and not self.test_once_hour():
                result += "{}Already done in the last hour {}\n".format(
                indent, self._visual_checks(self.test_once_hour())
            )
            if self.once_day and not self.test_once_day():
                result += "{}Already done today {}\n".format(
                indent, self._visual_checks(self.test_once_day())
            )
            if self.every_two_days and not self.test_every_two_days():
                result += "{}Already done in the last two days {}\n".format(
                indent, self._visual_checks(self.test_every_two_days())
            )
            if self.once_week and not self.test_once_week():
                result += "{}Already done this week {}\n".format(
                indent, self._visual_checks(self.test_once_week())
            )
            if self.once_month and not self.test_once_month():
                result += "{}Already done this month {}\n".format(
                indent, self._visual_checks(self.test_once_month())
            )
            if self.once_year and not self.test_once_year():
                result += "{}Already done this year {}\n".format(
                indent, self._visual_checks(self.test_once_year())
            )
            if self.min_girls > 0 and not self.test_minmax_girls():
                result += "{}There's not enough people in the room {} {}\n".format(
                indent, self.min_girls, self._visual_checks(self.test_once_year())
            )
            if self.max_girls < 100 and not self.test_minmax_girls():
                result += "{}The room is too crowded {} {}\n".format(
                indent, self.max_girls, self._visual_checks(self.test_minmax_girls())
            )
            result = result.split("\n")
            result += super(Action, self).examine_ui(indent_level)
            return [r for r in result if r]
        
        def apply_changes(self):
            self.apply_once_hour()
            self.apply_once_day()
            self.apply_duration()
            self.apply_needs()
            self.apply_attributes()
            self.apply_money()
        
        def apply_duration(self):
            if self.duration > 0:
                
                
                game.pass_time(self.duration)
        
        def apply_needs(self):
            for need, value in self.needs.items():
                hero[need] += value
        
        def apply_attributes(self):
            for attribute, value in self.attributes.items():
                hero[attribute] += value
        
        def apply_money(self):
            hero.money += self.get_money_gain()
        
        def apply_once_hour(self):
            if self.once_hour == "ACTIVE":
                if active_girl.object is None:
                    if config.developer:
                        raise ValueError("once_hour = 'ACTIVE' with no active target")
                    return
                name = "{}_{}".format(self.name, active_girl.id)
            elif self.once_hour:
                name = self.name
            else:
                return
            if name not in DONE_HOUR:
                DONE_HOUR.append(name)
        
        def apply_once_day(self):
            if self.once_day == "ACTIVE" or self.do_once == "ACTIVE":
                if active_girl.object is None:
                    if config.developer:
                        raise ValueError("once_day = 'ACTIVE' with no active target")
                    return
                name = "{}_{}".format(self.name, active_girl.id)
            else:
                name = self.name
            DONE[name] = game.days_played
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
