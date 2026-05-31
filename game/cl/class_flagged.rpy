
init -30 python:





    class Flagged(object):
        @staticmethod
        def clean_up():
            for f in FLAGS.copy().keys():
                if not FLAGS[f].update():
                    del FLAGS[f]
        
        def __init__(self, id, default_flags=None, **kwargs):
            
            if Proxied in type(self).mro():
                self._add_local("default_flags")
                self._add_local("flags")
                self._add_local("timers")
            self.__dict__["id"] = id
            self.__dict__["default_flags"] = default_flags if default_flags else {}
            self.flags = FlagsShortcut(self)
            self.timers = TimersShortcut(self)
        
        @property
        def hidden(self):
            return self.flags.hidden or False  
        
        def hide(self):
            self.flags.hidden = True
        
        def unhide(self):
            self.flags.hidden = False
        
        def set_flag(self, flag, val=True, duration="permanent", mod="=", hook=None):
            flag = self.id + flag
            if flag in FLAGS:
                flag = FLAGS[flag]
                if mod == "=":
                    flag.value = val
                elif mod == "+":
                    flag.value += val
                elif mod == "-":
                    flag.value -= val
            else:
                if mod == "-":
                    val = -val
                FLAGS[flag] = Flag(val, duration, hook)
        
        def has_flag(self, flag):
            flag = self.id + flag
            if flag in FLAGS:
                return True
            else:
                return False
        
        def get_flag_value(self, flag, default=None):
            
            if self.id + flag in FLAGS:
                return FLAGS[self.id + flag].value
            elif (
            "default_flags" in self.__dict__ and flag in self.__dict__["default_flags"]
        ):
                return self.__dict__["default_flags"][flag]
            elif default is not None:
                return default
            else:
                return 0
        
        def get_flag(self, flag):
            if self.id + flag in FLAGS:
                return FLAGS[self.id + flag]
            elif (
            "default_flags" in self.__dict__ and flag in self.__dict__["default_flags"]
        ):
                return TemporaryFlag(
                value=self.__dict__["default_flags"][flag], duration="permanent"
            )
            else:
                return None


    class FlagsShortcut:
        def __init__(self, parent):
            self._parent = parent
        
        def __contains__(self, attr):
            return self._parent.has_flag(attr)
        
        def __getitem__(self, attr):
            if attr[0] == "_":
                return self.__dict__[attr]
            return self._parent.get_flag_value(attr)
        
        def __getattr__(self, attr):
            try:
                return self.__getitem__(attr)
            except (AttributeError, KeyError):
                raise AttributeError(attr)
        
        def __setitem__(self, attr, val):
            
            self.__setattr__(attr, val)
        
        def __setattr__(self, attr, val):
            if attr[0] == "_":
                self.__dict__[attr] = val
            elif isinstance(val, TemporaryFlag):
                self._parent.set_flag(attr, val.value, duration=val.duration, hook=val.hook)
            else:
                self._parent.set_flag(attr, val)


    class TimersShortcut:
        def __init__(self, parent):
            self.__dict__["_parent"] = parent
        
        def __getitem__(self, attr):
            if attr[0] == "_":
                return self.__dict__[attr]
            else:
                
                flag = self._parent.get_flag(attr)
                
                if flag:
                    dur = flag.duration
                    if dur == "month":
                        
                        return 31 - (game.day - 1)
                    elif dur == "week":
                        return 7 - (game.week_day - 1)
                    elif dur == "day":
                        return 1
                    elif isinstance(dur, int):
                        return dur
                    else:
                        
                        return pow(2, 16)
                else:
                    return 0
        
        def __getattr__(self, attr):
            try:
                return self.__getitem__(attr)
            except (AttributeError, KeyError):
                raise AttributeError(attr)
        
        def __setitem__(self, attr, val):
            pass
        
        def __setattr__(self, attr, val):
            
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
