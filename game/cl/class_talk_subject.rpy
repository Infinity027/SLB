
init -15 python:



    class TalkSubject(ParentRegistry, Conditioned):
        """activities that require an interaction with a character."""
        
        def __init__(
        self,
        name,
        display_name=None,
        label=None,
        duration=0,
        icon=None,
        music=None,
        do_once=True,
        once_hour=False,
        once_day=False,
        every_two_days=False,
        once_week=False,
        once_month=False,
        once_year=False,
        known=False,
        **kwargs,
    ):
            super(TalkSubject, self).__init__(name, **kwargs)
            self.name = name
            self.display_name = display_name if display_name else name.capitalize()
            self.label = label
            self.duration = duration
            self.icon = icon
            self.music = music
            
            self.do_once = do_once
            self.once_hour = once_hour
            self.once_day = once_day
            self.every_two_days = every_two_days
            self.once_week = once_week
            self.once_month = once_month
            self.once_year = once_year
            
            self.known = known
        
        @classmethod
        def valid_subjects(cls):
            return list(
            cls.sorted_filter(
                key=lambda x: x.display_name,
                filter=lambda x: x.test(),
            )
        )
        
        @classmethod
        def known_subjects(cls):
            return list(
            cls.sorted_filter(
                key=lambda x: x.display_name,
                filter=lambda x: x.known,
            )
        )
        
        @classmethod
        def unknown_subjects(cls):
            return list(
            cls.sorted_filter(
                key=lambda x: x.display_name,
                filter=lambda x: not x.known,
            )
        )
        
        @classmethod
        def valid_known_subjects(cls):
            return list(
            cls.sorted_filter(
                key=lambda x: x.display_name,
                filter=lambda x: x.known and x.test(),
            )
        )
        
        def test(self, debug=False):
            for func in (
            self.test_duration,
            self.test_do_once,
            self.test_once_hour,
            self.test_once_day,
        ):
                if not func():
                    if debug:
                        renpy.log("Test Failed: {}".format(func.__name__))
                        print("Test Failed: {}".format(func.__name__))
                    return False
            
            return super(TalkSubject, self).test(debug)
        
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
        
        def test_duration(self):
            opened, closed = Room.find(game.room).hours
            finish = game.hour + self.duration
            
            if closed < opened <= game.hour:
                closed += 24
            
            return finish <= closed
        
        def apply_changes(self):
            self.apply_duration()
            self.apply_once_hour()
            self.apply_once_day()
        
        def apply_duration(self):
            if self.duration > 0:
                game.pass_time(self.duration)
        
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


    class GenericTalkSubject(Registry, TalkSubject):
        """
    Generic talk subjects: politics, books, food...
    """
        
        def __init__(self, name, **kwargs):
            super(GenericTalkSubject, self).__init__(name, **kwargs)


    class SpecificTalkSubject(Registry, TalkSubject):
        """
    Specific talk subjects: Talk about Ryan, Anna, Kleio, Investigation...
    """
        
        def __init__(self, name, **kwargs):
            super(SpecificTalkSubject, self).__init__(name, **kwargs)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
