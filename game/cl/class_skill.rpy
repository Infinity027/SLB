
init -20 python:



    class Skill(object):
        def __init__(self, name, display_name):
            self.name = name
            self.display_name = display_name if display_name else name
            self.notify()
        
        def notify(self):
            NOTIFICATIONS.append([f"{{size=20}}+ {str(self).capitalize()}{{/size}}", 2])
        
        def __str__(self):
            return self.display_name


    class TrainableSkill(object):
        def __init__(
        self,
        id,
        display_name,
        maximum=100,
        conditions=None,
        gain_effects=None,
        transferable=True,
    ):
            self.id = id
            self.maximum = maximum
            self.conditions = conditions if conditions else []
            self.gain_effects = gain_effects if gain_effects else []
            self.display_name = display_name
            self.transferable = transferable
        
        def __getattr__(self, attr):
            if attr == "value":
                return DATA_SKILLS[self.id] if self.id in DATA_SKILLS else 0
            else:
                try:
                    return self.__dict__[attr]
                except KeyError:
                    raise AttributeError(attr)
        
        @property
        def gainable(self):
            return all([safe_eval(x) for x in self.conditions])
        
        def gain(self):
            for gain_effect in self.gain_effects:
                exec(gain_effect)
        
        def __setattr__(self, attr, value):
            if attr == "value":
                DATA_SKILLS[self.id] = value
            else:
                self.__dict__[attr] = value
        
        def __call__(self):
            
            return self.value == self.maximum and all(
            [safe_eval(c) for c in self.conditions]
        )
        
        def __iadd__(self, value):
            old_val = self.value
            if isinstance(value, bool):
                self.value = self.maximum if value else 0
            else:
                self.value += int(value)
            
            if self.value > self.maximum:
                self.value = self.maximum
            if self.value < 0:
                self.value = 0
            if self.value == self.maximum:
                self.gain()
            if int(self.value) != int(old_val):
                self.notify()
            return self
        
        def notify(self):
            if self.value == self.maximum:
                NOTIFICATIONS.append([f"{{size=20}}+ {self.display_name}{{/size}}", 2])
            elif self.value > 0:
                NOTIFICATIONS.append(
                [
                    f"{{size=20}}{self.display_name} {int(self.value * 100 // self.maximum)}%{{/size}}",
                    2,
                ]
            )
            else:
                NOTIFICATIONS.append([f"{{size=20}}- {self.display_name}{{/size}}", 2])


    class NotSkill(TrainableSkill):
        def __init__(self):
            pass
        
        def __iadd__(self, value):
            pass
        
        def __call__(self):
            return False
        
        def __getattr__(self, attr):
            pass
        
        def __setattr__(self, attr, value):
            pass
        
        def __getitem__(self, item):
            pass
        
        def __setitem__(self, item, value):
            pass


    class SkillsManager(NoRollback):
        
        
        
        def __init__(self):
            pass
        
        def __getitem__(self, item):
            if item in YAML_SKILLS:
                return YAML_SKILLS[item]
            return NotSkill()
        
        def __iter__(self):
            for id in YAML_SKILLS:
                if YAML_SKILLS[id]():
                    yield YAML_SKILLS[id]
        
        def __getattr__(self, attr):
            try:
                if attr[0] == "_":
                    return self.__dict__[attr]
                else:
                    return self.__getitem__(attr)
            except KeyError:
                raise AttributeError(attr)
        
        def __setitem__(self, item, value):
            
            
            pass
        
        def __setattr__(self, attr, value):
            
            
            
            if attr[0] == "_":
                self.__dict__[attr] = value
            else:
                pass
        
        def __setstate__(self, value):
            
            pass
        
        def __getstate__(self):
            rv = self.__dict__.copy()
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
