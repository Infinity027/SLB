
init -20 python:



    class Flag(object):
        def __init__(self, value=True, duration=1, hook=None):
            self.duration = duration
            self.value = value
            self.hook = hook
        
        def update(self):
            if GALLERY_MODE:
                return
            if isinstance(self.duration, int) and not self.duration == 0:
                self.duration -= 1
            elif (self.duration == "week" and game.week_day == 1) or (
            self.duration == "month" and game.day == 1
        ):
                self.duration = 0
            if self.duration == 0 or self.duration == "day":
                if self.hook:
                    if isinstance(self.hook, basestring):
                        renpy.call_in_new_context(self.hook)
                    elif isinstance(self.hook, list):
                        
                        if isinstance(self.hook[1], list):
                            self.hook[1] = {
                            "girl": self.hook[1][0],
                            "flag": self.hook[1][1],
                            "value": self.hook[1][2],
                        }
                        self.hook[0](**self.hook[1])
                    else:
                        self.hook()
                return False
            return True



    def hook_set_flag(girl, flag, value):
        girl.flags[flag] = value


    class TemporaryFlag(object):
        def __init__(self, value, duration, hook=None):
            self.value = value
            self.duration = duration
            self.hook = hook
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
