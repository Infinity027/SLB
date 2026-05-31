
init -17 python:


    from math import modf, floor, ceil


    class Stat(object):
        @staticmethod
        def round(val):
            """Rounds a float away from 0."""
            if val > 0:
                return ceil(val)
            else:
                return floor(val)
        
        @staticmethod
        def randomly_round(val):
            """Randomly rounds a float based on its decimal part."""
            decimal, integer = modf(val)
            integer = int(integer)
            if random() <= abs(decimal):
                if decimal > 0:
                    integer += 1
                elif decimal < 0:
                    integer -= 1
            return integer
        
        def __init__(
        self,
        id,
        name=None,
        default=0,
        min=0,
        max=None,
        scale=None,
        scale_difficulty=False,
        inverse_scale=False,
        icon=None,
        negative_icon=None,
        hidden=False,
    ):
            
            if (min is not None and default < min) or (max is not None and default > max):
                raise ValueError("Default value for stat {} out of bounds".format(id))
            
            self.id = id
            self.name = name if name is not None else id.replace("_", " ").capitalize()
            self.val = default
            self.min = min
            self.max = max
            self.scale = (
            scale if scale is not None else 0
        )  
            self.scale_difficulty = scale_difficulty
            self.icon = (
            icon if icon is not None else ""
        )  
            self.negative_icon = (
            negative_icon if negative_icon is not None else ""
        )  
            self.hidden = hidden
            self.inverse_scale = inverse_scale
        
        def __call__(self):
            return self.val
        
        def __repr__(self):
            return str(self.val)
        
        def __str__(self):
            return str(self.val)
        
        @staticmethod
        def _sanitize_input(val):
            """Sanitizes the input. Can be overwritten by child classes."""
            return int(val)
        
        @property
        def val(self):
            return getattr(store, self.id)
        
        @val.setter
        def val(self, value):
            
            if isinstance(value, Stat):
                value = value.val
            
            
            value = self._sanitize_input(value)
            
            
            if self.max is not None and value > self.max:
                value = self.max
            elif self.min is not None and value < self.min:
                value = self.min
            
            setattr(store, self.id, value)
        
        @property
        def min(self):
            
            return getattr(store, "{}_min".format(self.id), None)
        
        @min.setter
        def min(self, value):
            
            if value is not None:
                value = self._sanitize_input(value)
            
            setattr(store, "{}_min".format(self.id), value)
            
            
            if value is not None and self.val < value:
                setattr(store, self.id, value)
        
        @property
        def max(self):
            
            return getattr(store, "{}_max".format(self.id), None)
        
        @max.setter
        def max(self, value):
            
            if value is not None:
                value = self._sanitize_input(value)
            
            setattr(store, "{}_max".format(self.id), value)
            
            
            if value is not None and self.val > value:
                setattr(store, self.id, value)
        
        @property
        def is_max(self):
            if self.max is None:
                return False
            return self.val == self.max
        
        @property
        def is_min(self):
            if self.min is None:
                return False
            return self.val == self.min
        
        @property
        def abs(self):
            return abs(self.val)
        
        def scaled_val(self):
            val = self.val
            
            if self.scale != 0:
                val = val * 100 / self.scale
                
                if val > 100:
                    val = 100
                elif val < -100:
                    val = -100
            
            val = int(val)
            
            if self.negative_icon:
                val = abs(val)
            return val
        
        
        
        def __add__(self, other):
            if isinstance(other, (int, float)):
                return self.val + other
            if isinstance(other, Stat):
                return self.val + other.val
            return NotImplemented
        
        def __sub__(self, other):
            if isinstance(other, (int, float)):
                return self.val - other
            if isinstance(other, Stat):
                return self.val - other.val
            return NotImplemented
        
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return self.val * other
            if isinstance(other, Stat):
                return self.val * other.val
            return NotImplemented
        
        def __truediv__(self, other):
            if isinstance(other, (int, float)):
                return self.val / other
            if isinstance(other, Stat):
                return self.val / other.val
            return NotImplemented
        
        def __floordiv__(self, other):
            if isinstance(other, (int, float)):
                return self.val // other
            if isinstance(other, Stat):
                return self.val // other.val
            return NotImplemented
        
        def __mod__(self, other):
            if isinstance(other, (int, float)):
                return self.val % other
            if isinstance(other, Stat):
                return self.val % other.val
            return NotImplemented
        
        def __divmod__(self, other):
            if isinstance(other, (int, float)):
                return self.val // other, self.val % other
            if isinstance(other, Stat):
                return self.val // other.val, self.val % other.val
            return NotImplemented
        
        
        
        def __radd__(self, other):
            if isinstance(other, (int, float)):
                return other + self.val
            if isinstance(other, Stat):
                return other.val + self.val
            return NotImplemented
        
        def __rsub__(self, other):
            if isinstance(other, (int, float)):
                return other - self.val
            if isinstance(other, Stat):
                return other.val - self.val
            return NotImplemented
        
        def __rmul__(self, other):
            if isinstance(other, (int, float)):
                return other * self.val
            if isinstance(other, Stat):
                return other.val * self.val
            return NotImplemented
        
        def __rtruediv__(self, other):
            if isinstance(other, (int, float)):
                return other / self.val
            if isinstance(other, Stat):
                return other.val / self.val
            return NotImplemented
        
        def __rfloordiv__(self, other):
            if isinstance(other, (int, float)):
                return other // self.val
            if isinstance(other, Stat):
                return other.val // self.val
            return NotImplemented
        
        def __rmod__(self, other):
            if isinstance(other, (int, float)):
                return other % self.val
            if isinstance(other, Stat):
                return other.val % self.val
            return NotImplemented
        
        def __rdivmod__(self, other):
            if isinstance(other, (int, float)):
                return other // self.val, other % self.val
            if isinstance(other, Stat):
                return other.val // self.val, other.val % self.val
            return NotImplemented
        
        
        
        def __iadd__(self, other):
            if isinstance(other, Stat):
                other = other.val
            self.update(other)
            return self
        
        def __isub__(self, other):
            if isinstance(other, Stat):
                other = other.val
            self.update(-other)
            return self
        
        
        
        def __lt__(self, other):
            if isinstance(other, (int, float)):
                return self.val < other
            if isinstance(other, Stat):
                return self.val < other.val
            return NotImplemented
        
        def __le__(self, other):
            if isinstance(other, (int, float)):
                return self.val <= other
            if isinstance(other, Stat):
                return self.val <= other.val
            return NotImplemented
        
        def __eq__(self, other):
            if isinstance(other, (int, float)):
                return self.val == other
            if isinstance(other, Stat):
                return self.val == other.val
            return NotImplemented
        
        def __ne__(self, other):
            if isinstance(other, (int, float)):
                return self.val != other
            if isinstance(other, Stat):
                return self.val != other.val
            return NotImplemented
        
        def __gt__(self, other):
            if isinstance(other, (int, float)):
                return self.val > other
            if isinstance(other, Stat):
                return self.val > other.val
            return NotImplemented
        
        def __ge__(self, other):
            if isinstance(other, (int, float)):
                return self.val >= other
            if isinstance(other, Stat):
                return self.val >= other.val
            return NotImplemented
        
        def __bool__(self):
            return self.val != 0
        
        def update(self, val=0, scale=True, limit=None):
            
            old_val = self.val
            
            
            if self.scale_difficulty and scale:
                if self.inverse_scale:
                    val *= Game.get_difficulty_mod(-val)
                else:
                    val *= Game.get_difficulty_mod(val)
            
            
            
            val = self._sanitize_input(val)
            
            if limit is not None:
                val = min(max(limit - self.val, 0), val)
            self.val += val
            
            
            self._notify(round(self.val - old_val, 1))
        
        def _notify(self, val):
            
            if self.hidden:
                return
            
            
            if self.scale != 0:
                val = val * 100 / self.scale
                
                if val > 0:
                    val = int(ceil(val))
                else:
                    val = int(floor(val))
            
            if val == 0:
                return
            
            
            if val < 0 and self.negative_icon:
                val = abs(val)
                icon = self.negative_icon
            
            elif self.icon:
                icon = self.icon
            else:
                icon = None
            
            if icon is not None:
                if isinstance(icon, (list, tuple)):
                    name = " ".join(["{{image={}}}".format(i) for i in icon])
                else:
                    name = "{{image={}}}".format(icon)
            
            else:
                name = self.name
            
            NOTIFICATIONS.append(["{} {:+}".format(name, val), 2])


    class Money(Stat):
        def __init__(self, id, **kwargs):
            super(Money, self).__init__(id=id, icon="gui/icons/icon_money.png", **kwargs)
        
        _coefficients = ("", "K", "M")
        
        def __str__(self):
            
            if self.val < 1000:
                return "{}".format(self.val)
            
            val, i = float(self.val), 0
            
            while val > 1000 and i < len(self._coefficients) - 1:
                val /= 1000
                i += 1
            return "{:.1f}{}".format(round(val, 1), self._coefficients[i])


    class Sexperience(Stat):
        def __init__(self, girl, **kwargs):
            super(Sexperience, self).__init__(
            id="{}_sexperience".format(girl.id),
            name="{}'s sexperience".format(girl.name),
            hidden=True,
            **kwargs,
        )
            
            self.last = 0
        
        @property
        def last(self):
            return getattr(store, f"{self.id}_last")
        
        @last.setter
        def last(self, value):
            setattr(store, f"{self.id}_last", value)
        
        def update(self, val=0, scale=True, limit=None):
            super(Sexperience, self).update(val, scale, limit)
            
            
            self.last = game.days_played
            
            hero.flags.last_sex = (game.hour, game.days_played)
            
            if hero.flags.bluepills > 0:
                hero.flags.bluepills -= 1
            
            hero.fun += 5


    class Need(Stat):
        def __init__(
        self,
        id,
        decay_value=1.0,
        
        default=10,
        max=10,
        decay_penalty=False,
        gain_penalty=False,
        **kwargs,
    ):
            
            kwargs["default"] = default
            kwargs["max"] = max
            super(Need, self).__init__(id, **kwargs)
            
            self.decay_value = decay_value
            self._max = max  
            self.decay_penalty = decay_penalty
            self.gain_penalty = gain_penalty
        
        def __str__(self):
            return str(int(self.val))
        
        @classmethod
        def _sanitize_input(cls, val):
            if isinstance(val, float) and persistent.needs_randomness:
                val = cls.randomly_round(val)
            return val
        
        @property
        def decay_penalty(self):
            return getattr(store, "{}_decay_penalty".format(self.id), False)
        
        @decay_penalty.setter
        def decay_penalty(self, value):
            if not isinstance(value, bool):
                raise ValueError("decay_penalty must be a boolean")
            setattr(store, "{}_decay_penalty".format(self.id), value)
        
        @property
        def gain_penalty(self):
            return getattr(store, "{}_gain_penalty".format(self.id), False)
        
        @gain_penalty.setter
        def gain_penalty(self, value):
            if not isinstance(value, bool):
                raise ValueError("gain_penalty must be a boolean")
            setattr(store, "{}_gain_penalty".format(self.id), value)
        
        def decay(self, duration):
            
            return self.val - duration * self.decay_value
        
        def get_decayed_action_value(self, value, duration):
            decayed_result = value - duration * self.decay_value
            decayed_result = decayed_result * Game.get_difficulty_mod(decayed_result)
            if self.decay_penalty and decayed_result < 0:
                decayed_result += decayed_result * DECAY_PENALTY_MODIFIER
            if self.gain_penalty and decayed_result > 0:
                decayed_result -= decayed_result * GAIN_PENALTY_MODIFIER
            return round(decayed_result, 1)
        
        def fill(self):
            if self.max is not None:
                self.val = self.max
        
        def update_max(self, value):
            self.max = self._max + value // 20


    class Attribute(Stat):
        def __init__(
        self,
        id,
        ui_icon=None,
        ui_negative_icon=None,
        up_hook=None,
        date=False,
        lock_bar=None,
        
        max=100,
        scale=100.0,
        scale_difficulty=True,
        **kwargs,
    ):
            
            kwargs["max"] = max
            kwargs["scale"] = scale
            kwargs["scale_difficulty"] = scale_difficulty
            super(Attribute, self).__init__(id, **kwargs)
            
            
            self.ui_icon = ui_icon if ui_icon is not None else kwargs.get("icon")
            self.ui_negative_icon = (
            ui_negative_icon
            if ui_negative_icon is not None
            else kwargs.get("negative_icon")
        )
            self.up_hook = up_hook if up_hook is not None else {}
            self.date = date
            self.lock_bar = lock_bar
        
        @classmethod
        def _sanitize_input(cls, val):
            if isinstance(val, float):
                val = cls.randomly_round(val)
            return val
        
        def update(self, val=1, scale=True, limit=None):
            
            old_val = self.val
            
            super(Attribute, self).update(val, scale, limit)
            
            
            for step, hook in self.up_hook.items():
                
                if isinstance(step, basestring):
                    step = step.replace("/", "")
                step = int(step)
                
                
                for i in range(old_val // step, self.val // step):
                    if isinstance(hook, basestring):
                        exec(hook)
                    else:
                        hook()
                
                
                for item in hero.equipment:
                    if (
                    hero.equipment[item]
                    and hasattr(hero.equipment[item], "conditions")
                    and not hero.equipment[item].test()
                ):
                        hero.equipment[item].unequip()
        
        def get_icon(self):
            if self.ui_negative_icon and self.val < 0:
                return self.ui_negative_icon
            else:
                return self.ui_icon
        
        def for_ui(self):
            
            lbar = (
            {"value": 0, "range": self.min, "left": "locked", "right": "thru"}
            if self.lock_bar == "min"
            else {
                "value": self.max,
                "range": self.scale,
                "left": "thru",
                "right": "locked",
            }
        )
            return {
            "text": str(self.scaled_val()) + "%",
            "icon": self.get_icon(),
            "vbar": {"value": self.scaled_val(), "range": 100},
            "lbar": lbar,
            "lock": self.val != 0
            and abs(self.val) != self.scale
            and (self.is_max or self.is_min),
        }
        
        def visible(self):
            return self.val != 0


    class Love(Attribute):
        def __init__(self, girl, **kwargs):
            super(Love, self).__init__(
            id="{}_love".format(girl.id),
            name="{}'s love".format(girl.name),
            scale=200.0,
            scale_difficulty=True,
            icon=["notify {}".format(girl.id), "gui/icons/icon_love.png"],
            ui_icon="gui/icons/icon_love.png",
            up_hook={5: girl.traits.discover},
            date=True,
            **kwargs,
        )
            self.girl_id = girl.id
        
        def visible(self):
            return True
        
        def update(self, val=1, scale=True, limit=None):
            
            if hasattr(self, "girl_id"):
                
                if Person.find(self.girl_id).flags.friendzone and (
                limit is None or limit > 25
            ):
                    limit = 25
                
                
                if game.active_date.on_date(self.girl_id):
                    if val > 0:
                        game.active_date.score += val * Game.get_difficulty_mod(val) * 5 + 5
                    else:
                        game.active_date.score += val * Game.get_difficulty_mod(val) * 5
            
            super(Love, self).update(val, scale, limit)


    class Sub(Attribute):
        def __init__(self, girl, **kwargs):
            super(Sub, self).__init__(
            id="{}_sub".format(girl.id),
            name="{}'s kink".format(girl.name),
            scale_difficulty=True,
            icon=["notify {}".format(girl.id), "gui/icons/icon_sub.png"],
            negative_icon=["notify " + girl.id, "gui/icons/icon_dom.png"],
            ui_icon="gui/icons/icon_sub.png",
            ui_negative_icon="gui/icons/icon_dom.png",
            **kwargs,
        )
        
        def update(self, val=0, scale=True, limit=None):
            if self.val < 0:
                old_scale = self.inverse_scale
                self.inverse_scale = True
                super(Sub, self).update(val=val, scale=scale, limit=limit)
                self.inverse_scale = old_scale
            else:
                super(Sub, self).update(val=val, scale=scale, limit=limit)
        
        def visible(self):
            return True


    class Lesbian(Attribute):
        def __init__(self, girl, **kwargs):
            super(Lesbian, self).__init__(
            id="{}_lesbian".format(girl.id),
            name="{}'s lesbian".format(girl.name),
            scale=20.0,
            icon=["notify {}".format(girl.id), "gui/icons/icon_lesbian.png"],
            ui_icon="gui/icons/icon_lesbian.png",
            **kwargs,
        )


    class Male(Attribute):
        def __init__(self, girl, **kwargs):
            super(Male, self).__init__(
            id="{}_male".format(girl.id),
            name="{}'s masculinity".format(girl.name),
            icon=["notify {}".format(girl.id), "gui/icons/icon_male.png"],
            ui_icon="gui/icons/icon_male.png",
            scale_difficulty=False,
            **kwargs,
        )


    class Yandere(Attribute):
        def __init__(self, girl, **kwargs):
            super(Yandere, self).__init__(
            id="{}_yandere".format(girl.id),
            name="{}'s yandere".format(girl.name),
            icon=["notify {}".format(girl.id), "gui/icons/icon_yandere.png"],
            ui_icon="gui/icons/icon_yandere.png",
            scale_difficulty=False,
            **kwargs,
        )
        
        def visible(self):
            return True


    class Siscon(Attribute):
        def __init__(self, girl, **kwargs):
            super(Siscon, self).__init__(
            id="{}_siscon".format(girl.id),
            name="{}'s siscon".format(girl.name),
            icon=["notify {}".format(girl.id)],
            ui_icon="notify {}".format(girl.id),
            **kwargs,
        )
        
        def visible(self):
            return False


    class Career(Attribute):
        def __init__(self, girl, **kwargs):
            self.girl = girl
            super(Career, self).__init__(
            id="{}_career".format(girl.id),
            name="{}'s career".format(girl.name),
            icon=["notify {}".format(girl.id), "gui/icons/icon_career.png"],
            ui_icon="gui/icons/icon_career.png",
            **kwargs,
        )
        
        def visible(self):
            return self.girl.flags.career


    class Purity(Attribute):
        def __init__(self, girl, **kwargs):
            super(Purity, self).__init__(
            id="{}_purity".format(girl.id),
            name="{}'s purity".format(girl.name),
            icon=["notify {}".format(girl.id), "gui/icons/icon_good.png"],
            ui_icon="gui/icons/icon_good.png",
            
            scale_difficulty=False,
            **kwargs,
        )
        
        def visible(self):
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
