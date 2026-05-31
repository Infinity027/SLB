




init -20 python:



    class BaseEvent(ParentRegistry, Action):
        def __init__(
        self,
        name,
        priority=50,
        clothes=None,
        quit=True,
        cancel_activity=None,
        girl=None,
        chances=None,
        
        do_once=True,
        once_hour=True,
        block_when_canceled=True,
        **kwargs,
    ):
            
            kwargs["do_once"] = do_once
            kwargs["once_hour"] = once_hour
            super(BaseEvent, self).__init__(name, **kwargs)
            
            self.priority = priority
            self.clothes = clothes
            self.quit = quit
            self.cancel_activity = (
            cancel_activity
            if cancel_activity is not None
            else self.has_activity_condition()
        )
            self.girl = girl
            if chances is None:
                self.chances = None
            elif isinstance(chances, tuple):
                self.chances = VariableChanceChecker(*chances)
            else:
                self.chances = ChanceChecker(chances)
            
            self.block_when_canceled = block_when_canceled
        
        def test(self, debug=False):
            for func in (self.test_blocked,):
                if not func():
                    if debug:
                        print("Test Failed: {}".format(func.__name__))
                    return False
            
            if not super(BaseEvent, self).test(debug):
                return False
            
            if self.chances is not None:
                if self.flags.lastchance != "{}-{}".format(game.days_played, game.hour):
                    self.flags.lastchance = "{}-{}".format(game.days_played, game.hour)
                    if not self.chances():
                        if debug:
                            print(
                            "Event didn't happen: {}".format(
                                self.chances.debug_message()
                            )
                        )
                        return False
                else:
                    if debug:
                        print(
                        "Event didn't happen: {}".format(self.chances.debug_message())
                    )
                    return False
            
            return True
        
        def test_blocked(self):
            return not self.get_flag_value("blocked")
        
        def examine(self, indent_level=0):
            result = super(BaseEvent, self).examine(indent_level)
            if self.chances is not None:
                result += "{}\n".format(self.chances.description(indent_level=indent_level))
            return result[:-1] if result.endswith("\n") else result  
        
        def examine_ui(self, indent_level=0):
            result = super(BaseEvent, self).examine_ui(indent_level)
            if self.chances is not None:
                result.append("{}".format(self.chances.for_ui(indent_level=indent_level)))
            return result
        
        @classmethod
        def valid_events(cls):
            
            if game.active_date.roaming:
                return []
            
            return [event for event in cls.filter() if event.test()]


    class Event(Registry, BaseEvent):
        """normal events."""
        
        def __init__(self, name, **kwargs):
            
            super(Event, self).__init__(name, **kwargs)


    class InteractEvent(Registry, BaseEvent):
        """events that require an interaction with a character."""
        
        def __init__(self, name, **kwargs):
            
            super(InteractEvent, self).__init__(name, **kwargs)


    class WakeUpEvent(Registry, BaseEvent):
        """events that wake up the hero while sleeping."""
        
        def __init__(
        self,
        name,
        
        quit=True,
        **kwargs,
    ):
            
            kwargs["quit"] = quit
            super(WakeUpEvent, self).__init__(name, **kwargs)
            
            
            if not quit:
                raise ValueError("quit must be True")


    class DayTransitionEvent(Registry, BaseEvent):
        """events that are triggered when changing day."""
        
        def __init__(
        self,
        name,
        
        do_once=False,
        once_hour=False,
        once_day=True,
        quit=False,
        **kwargs,
    ):
            
            kwargs["do_once"] = do_once
            kwargs["once_hour"] = once_hour
            kwargs["once_day"] = once_day
            kwargs["quit"] = quit
            super(DayTransitionEvent, self).__init__(name, **kwargs)
            
            
            if quit:
                raise ValueError("quit must be False")


    class CallEvent(Registry, BaseEvent):
        """events that are triggered when calling someone."""
        
        def __init__(
        self,
        name,
        
        quit=True,
        **kwargs,
    ):
            
            kwargs["quit"] = quit
            super(CallEvent, self).__init__(name, **kwargs)
            
            
            if not quit:
                raise ValueError("quit must be True")


    class AfterDateEvent(Registry, BaseEvent):
        """events that are triggered after a date."""
        
        def __init__(self, name, **kwargs):
            
            super(AfterDateEvent, self).__init__(name, **kwargs)


    class BeforeDateEvent(Registry, BaseEvent):
        """events that are triggered before a date."""
        
        def __init__(self, name, **kwargs):
            
            super(BeforeDateEvent, self).__init__(name, **kwargs)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
