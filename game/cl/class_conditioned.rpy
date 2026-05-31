



























init -25 python:



    class Conditioned(Flagged):
        def __init__(self, id, conditions=None, **kwargs):
            super(Conditioned, self).__init__(id, **kwargs)
            
            self.conditions = conditions if conditions is not None else []
            
            self.conditions = [
            c if isinstance(c, Checker) else RawChecker(c) for c in self.conditions
        ]
        
        
        
        
        @staticmethod
        def done(name):
            return name in DONE
        
        @staticmethod
        def done_today(name):
            return Conditioned.done_since(name, 1)
        
        @staticmethod
        def done_yesterday(name):
            return Conditioned.done_since(name, 2)
        
        @staticmethod
        def done_this_week(name):
            return Conditioned.done_since(name, 7)
        
        @staticmethod
        def done_this_month(name):
            return Conditioned.done_since(name, 31)
        
        @staticmethod
        def done_this_year(name):
            return Conditioned.done_since(name, 31 * 4)
        
        @staticmethod
        def done_since(name, days):
            return False if name not in DONE else game.days_played - DONE[name] < days
        
        def test(self, debug=False):
            
            for condition in self.conditions:
                try:
                    if not condition():
                        if debug:
                            print(
                            f"Unfulfilled condition:\n{condition.debug_message()}\n{condition}"
                        )
                        return False
                except Exception as e:
                    print(f"Exception on {self.id} for {condition.description()}  --- {e}")
                    raise type(e)(f"Exception on {self.id} for {condition.description()}")
            
            if debug:
                print("All conditions fulfilled")
            return True
        
        def examine(self, indent_level=0):
            result = ""
            for condition in self.conditions:
                result += "{}\n".format(condition.description(indent_level=indent_level))
            return result[:-1] if result.endswith("\n") else result  
        
        def examine_ui(self, indent_level=0):
            result = ""
            for condition in self.conditions:
                if condition.for_ui(indent_level=indent_level):
                    result += "{}\n".format(condition.for_ui(indent_level=indent_level))
            
            return [r for r in result.split("\n") if r]  
        
        def _recursive_search_checkers(self, checkers, stop_at=type(None)):
            for checker in checkers:
                if isinstance(checker, stop_at):
                    yield checker
                elif isinstance(checker, WrapperChecker):
                    for subchecker in self._recursive_search_checkers(
                    checker.checkers, stop_at
                ):
                        yield subchecker
                else:
                    yield checker
        
        def has_activity_condition(self, activity=None):
            for condition in self._recursive_search_checkers(self.conditions, HeroTarget):
                if isinstance(condition, HeroTarget):
                    for checker in self._recursive_search_checkers(condition.checkers):
                        if isinstance(checker, IsActivity):
                            if activity is None or activity in checker.values:
                                return True
            return False
        
        @property
        def rooms_in_conditions(self):
            rooms = set()
            for condition in self._recursive_search_checkers(self.conditions):
                if isinstance(condition, IsRoom):
                    rooms.update(condition.values)
                if isinstance(condition, HasRoomTag):
                    rooms.update(Room.filter(lambda x: x.has_tag(condition.tag)))
            return rooms
        
        @property
        def people_in_conditions(self):
            people = set()
            for condition in self._recursive_search_checkers(self.conditions, PersonTarget):
                if isinstance(condition, PersonTarget):
                    people.add(condition.id)
            return people
        
        @property
        def gender_condition(self):
            for condition in self._recursive_search_checkers(self.conditions):
                if isinstance(condition, IsGender):
                    return condition.gender
            return "both"
        
        @property
        def day_in_conditions(self):
            for condition in self._recursive_search_checkers(self.conditions, IsDayOfWeek):
                if isinstance(condition, IsDayOfWeek):
                    return [i for i in condition.values]
            return ""
        
        @property
        def seasons_in_conditions(self):
            for condition in self._recursive_search_checkers(self.conditions, IsSeason):
                if isinstance(condition, IsSeason):
                    return [i for i in condition.values]
            return ""



init -30 python:










    class PartialChecker(python_object):
        """Base class for condition checkers that need to be wrapped."""
        
        __slots__ = "__dict__"
        
        def __call__(self):
            
            raise NotImplementedError
        
        def __eq__(self, other):
            """
        Checker comparison.

        Checks that the classes are the same and that all slotted
        attributes match. This allows checking if an exact checker is
        inside a list of conditions.
        """
            
            if self.__class__ != other.__class__:
                return False
            
            for cls in self.__class__.__mro__:
                for attr in getattr(cls, "__slots__", []):
                    if getattr(self, attr) != getattr(other, attr):
                        return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(self.__class__.__name__, indent_level)
        
        def description(self, indent_level=0, negated=False):
            
            return self._indent(self.__class__.__name__, indent_level)
        
        def for_ui(self, indent_level=0, negated=False):
            
            return self._indent(self.__class__.__name__, indent_level)
        
        @staticmethod
        def _indent(message, indent_level):
            
            
            return f"{'    ' * indent_level}{message}"
        
        @staticmethod
        def _visual_checks(value, negated):
            if negated:
                return (
                "{color=#00ff00}{font=DejaVuSans.ttf}\u2713{/font}{/color}"
                if not value
                else "{color=#f00}{font=DejaVuSans.ttf}\u2717{/font}{/color}"
            )
            return (
            "{color=#00ff00}{font=DejaVuSans.ttf}\u2713{/font}{/color}"
            if value
            else "{color=#f00}{font=DejaVuSans.ttf}\u2717{/font}{/color}"
        )


    class Checker(PartialChecker):
        """
    Base class for condition checkers.

    Classes that inherit from this are expected to define the following:
    - __slots__: [required] as thousands of these checkers will exist
    - __init__: [optional] initialize the checker. Everything that can be
        done during init should be moved here because it reduces the time
        required to perform this check as init is not done at runtime.
        Additionally, raising exceptions during init for badly formed
        checks is recommended as they will be easier to debug.
    # TODO: Post-init method called once all Events/Activities are defined
    - __call__: [required] returns a boolean whether this check passes or
        not. This code will only be executed at runtime, so moving
        everything that can be done earlier to the previous methods makes
        debugging easier. It also helps performance.
        Raising exceptions must be gated with config.developer.
    - debug_message: [optional] String representation that will be logged
        when a check fails. By default, the checker's class name.
        It accepts the following parameters:
          - indent: indentation level of the returned string, defaults to 0
          - negated: whether it is negated or not, defaults to False
    - description: [optional] String representation that describes with
        words what a check does. By default, the checker's class name.
        It accepts the following parameters:
          - indent: indentation level of the returned string, defaults to 0
          - negated: whether it is negated or not, defaults to False
    """
        
        __slots__ = ()


    class RawChecker(Checker):
        """Checker that evaluates a raw Python expression."""
        
        __slots__ = ("_expression",)
        
        def __init__(self, expression="True"):
            if not isinstance(expression, basestring):
                raise TypeError("expression expected to be a string: " + str(expression))
            self._expression = expression
        
        def __call__(self):
            try:
                return eval(self._expression)
            except Exception as e:
                if config.developer:
                    raise Exception(
                    "invalid condition: " + str(self._expression) + "\n" + str(e)
                )
                return False
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                msg = "'{}' succeeded".format(self._expression)
            else:
                msg = "'{}' failed".format(self._expression)
            return self._indent(msg, indent_level)
        
        def description(self, indent_level=0, negated=False):
            if negated:
                msg = "Not '{}'".format(self._expression)
            else:
                msg = "'{}'".format(self._expression)
            return self._indent(msg, indent_level)
        
        def for_ui(self, indent_level=0, negated=False):
            if negated:
                msg = "Not '{}' {}".format(
                self._expression, self._visual_checks(self.__call__(), negated)
            )
            else:
                msg = "'{}' {}".format(
                self._expression, self._visual_checks(self.__call__(), negated)
            )
            return self._indent(msg, indent_level)



    class TargetedChecker(PartialChecker):
        """Base class for checkers that require to specify a target."""
        
        __slots__ = ("_target", "_id")
        
        def __init__(self):
            self._target = None
            self._id = None
        
        def set_target(self, target):
            self._target = target
            if hasattr(self, "post_set_target"):
                self.post_set_target()
            return self._target
        
        @property
        def _name(self):
            if isinstance(self._target, Game):
                return "game"
            if isinstance(self._target, Hero):
                
                return getattr(self._target, "name", "hero")
            if isinstance(self._target, Person):
                return self._target.name
            if isinstance(self._target, Room):
                return self._target.id
            
            return "target"


    class WrapperChecker(Checker):
        """Base class for checkers that wrap other checkers."""
        
        __slots__ = ("_checkers",)
        
        def __init__(self, *checkers):
            filtered_checkers = []
            for checker in checkers:
                if isinstance(checker, basestring):
                    checker = RawChecker(checker)
                if not isinstance(checker, PartialChecker):
                    raise ValueError("non-checker provided to wrapper checker")
                filtered_checkers.append(checker)
            
            self._checkers = tuple(filtered_checkers)
        
        @property
        def checkers(self):
            return self._checkers
        
        def __call__(self):
            
            
            return all(checker() for checker in self._checkers)
        
        def debug_message(self, indent_level=0, negated=False):
            
            
            if negated:
                return "\n".join(
                [self._indent("Any of:", indent_level)]
                + [
                    checker.debug_message(
                        indent_level=indent_level + 1,
                        negated=negated,
                    )
                    for checker in self._checkers
                ]
            )
            
            for checker in self._checkers:
                if not checker():
                    print(f"checker: {checker} failed: {checker.debug_message()}")
                    return checker.debug_message(
                    indent_level=indent_level,
                    negated=negated,
                )
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            return "\n".join(
            checker.description(indent_level=indent_level, negated=negated)
            for checker in self._checkers
        )
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            return "\n".join(checkers_ui)
        
        
        
        def set_target(self, target):
            _target = set()
            for checker in self._checkers:
                if hasattr(checker, "set_target"):
                    _target.add(checker.set_target(target))
            if _target:
                return list(_target)[0]
            print(f"ERROR in checker target: {self._checkers}")
            for checker in self._checkers:
                if isinstance(checker, store.IsHour):
                    print(
                    f"    checker None IsHour: start {checker._start} end {checker._end}"
                )
                elif isinstance(checker, store.IsDone):
                    print(f"    checker None IsDone: values {checker._values}")
                else:
                    print(f"    checker None Unknown instance: {checker}")
            return None


    class SetChecker(Checker):
        """Base class for checkers that accept a set of inputs."""
        
        __slots__ = ("_values",)
        
        def __init__(self, *args):
            if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
                args = args[0]
            self._values = set(args)
        
        @property
        def values(self):
            
            return set(self._values)
        
        def _stringify_set(
        self,
        sort_key=None,  
        stringify=str,  
        join_by=", ",  
        last_join_by=None,  
    ):
            if len(self._values) > 1 and last_join_by is not None:
                
                values = sorted(self._values, key=sort_key)
                return (
                join_by.join(map(stringify, values[:-1]))
                + last_join_by
                + stringify(values[-1])
            )
            return join_by.join(map(stringify, sorted(self._values, key=sort_key)))



    class TargetedSetChecker(TargetedChecker):
        """Base class for checkers that accept a set of inputs and require to specify a target."""
        
        __slots__ = ("_values",)
        
        def __init__(self, *args):
            super(TargetedSetChecker, self).__init__()
            if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
                args = args[0]
            self._values = set(args)
        
        @property
        def values(self):
            
            return set(self._values)
        
        def _stringify_set(
        self,
        sort_key=None,  
        stringify=str,  
        join_by=", ",  
        last_join_by=None,  
        quote_values=False,
    ):
            if quote_values:
                values_for_ui = sorted({f"'{i}'" for i in self._values}, key=sort_key)
            else:
                values_for_ui = sorted(self._values, key=sort_key)
            if len(values_for_ui) > 1 and last_join_by is not None:
                
                return (
                join_by.join(map(stringify, values_for_ui[:-1]))
                + last_join_by
                + stringify(values_for_ui[-1])
            )
            return join_by.join(map(stringify, values_for_ui))


    class IntSetChecker(SetChecker):
        """Base class for checkers that accept a set of integers as input."""
        
        __slots__ = ()
        
        def __init__(self, *args):
            if len(args) == 1 and isinstance(args[0], (list, tuple, set, basestring)):
                args = args[0]
            self._values = set(int(arg) for arg in args)


    class StatChecker(TargetedChecker):
        """Base class for checkers that act on a Stat."""
        
        __slots__ = "_stat", "_value", "_stat_name"
        
        def __init__(self, stat, value=None):
            super(StatChecker, self).__init__()
            self._stat_name = stat
            self._value = value
            self._stat = None
        
        def post_set_target(self):
            
            if not isinstance(self._target[self._stat_name], Stat):
                raise ValueError(
                "{} is not a valid stat of {}".format(self._stat_name, self._name)
            )
            self._stat = self._target[self._stat_name]


    class FlagChecker(TargetedChecker):
        """Base class for checkers that act on a flag."""
        
        __slots__ = "_flag", "_value", "_flags"
        
        def __init__(self, flag, value):
            super(FlagChecker, self).__init__()
            if not isinstance(flag, basestring):
                raise TypeError("flag expected to be a string")
            self._flag = flag
            self._value = value
            self._flags = None
        
        def post_set_target(self):
            
            if not isinstance(self._target, Flagged):
                raise ValueError("{} doesn't have flags".format(self._name))
            self._flags = self._target.flags


    class TimerChecker(TargetedChecker):
        """Base class for checkers that act on a timer."""
        
        __slots__ = "_timer", "_value", "_timers"
        
        def __init__(self, timer, value):
            super(TimerChecker, self).__init__()
            if not isinstance(timer, basestring):
                raise TypeError("timer expected to be a string")
            self._timer = timer
            self._value = value
            self._timers = None
        
        def post_set_target(self):
            
            if not isinstance(self._target, Flagged):
                raise ValueError("{} doesn't have timers".format(self._name))
            self._timers = self._target.timers


    class CounterChecker(TargetedChecker):
        """Base class for checkers that act on a counter."""
        
        __slots__ = "_counter", "_value", "_counters"
        
        def __init__(self, counter, value):
            super(CounterChecker, self).__init__()
            if not isinstance(counter, basestring):
                raise TypeError("counter expected to be a string")
            self._counter = counter
            self._value = value
            self._counters = None
        
        def post_set_target(self):
            
            if not isinstance(self._target, Countered):
                raise ValueError("{} doesn't have counters".format(self._name))
            self._counters = self._target.counters









    class ChanceChecker(Checker):
        """RNG checker."""
        
        __slots__ = ("_threshold",)
        
        def __init__(self, threshold):
            if 0 > threshold or threshold > 100:
                raise ValueError("chance threshold must be in 0-100")
            self._threshold = threshold
        
        def __call__(self):
            return randint(1, 100) <= self._threshold
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                raise ValueError("chances checkers should not be negated")
            return self._indent("{}% chance".format(self._threshold), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self.debug_message(indent_level, negated)
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "{}% chance {}".format(
                self._threshold, self._visual_checks(self.__call__(), negated)
            ),
            indent_level,
        )


    class VariableChanceChecker(ChanceChecker):
        """RNG checker with a variable threshold."""
        
        __slots__ = "_target", "_stat"
        
        def __init__(self, target, stat, threshold):
            super(VariableChanceChecker, self).__init__(threshold)
            if not isinstance(getattr(target, stat, None), Stat):
                raise ValueError("{} is not a valid target stat".format(stat))
            self._target = target
            self._stat = stat
        
        def __call__(self):
            stat = self._target[self._stat]
            return randint(1, 100) <= self._threshold * stat() / stat.scale
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                raise ValueError("chances checkers should not be negated")
            if isinstance(self._target, Hero):
                stat = "hero's {}".format(self._stat)
            elif isinstance(self._target, Person):
                stat = "{}'s {}".format(self._target.name, self._stat)
            else:
                stat = self._stat
            return self._indent(
            "{}*{}/{}% chance".format(
                self._threshold, stat, self._target[self._stat].scale
            ),
            indent_level,
        )


    class FlagChanceChecker(FlagChecker):
        """RNG checker with a variable threshold based on a flag."""
        
        __slots__ = "_threshold", "_target", "_flag"
        
        def __init__(self, flag, threshold):
            super(FlagChanceChecker, self).__init__(flag, threshold)
            if not isinstance(flag, basestring):
                raise TypeError("flag expected to be a string")
            self._flag = flag
            self._threshold = threshold
            self._rand_result = None
        
        def __call__(self):
            flag = self._flags[self._flag]
            self._rand_result = randint(1, 100)
            return self._rand_result + flag >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                raise ValueError("chances checkers should not be negated")
            return self._indent(
            "{}+{} vs {}% chance".format(
                self._rand_result, self._flags[self._flag], self._threshold
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self.debug_message(indent_level, negated)
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "{}+{} vs {}% chance {}".format(
                self._rand_result,
                self._flags[self._flag],
                self._threshold,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class CounterChanceChecker(CounterChecker):
        """RNG checker with a variable threshold based on a counter."""
        
        __slots__ = ("_threshold",)
        
        def __init__(self, counter, threshold):
            super(CounterChanceChecker, self).__init__(counter, threshold)
            if not isinstance(counter, basestring):
                raise TypeError("flag expected to be a string")
            self._rand_result = None
        
        def __call__(self):
            counter = self._counters[self._counter]
            self._rand_result = randint(1, 100)
            return self._rand_result + counter >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                raise ValueError("chances checkers should not be negated")
            return self._indent(
            "{}+{} vs {}% chance".format(
                self._rand_result, self._counters[self._counter], self._value
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self.debug_message(indent_level, negated)
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "{}+{} vs {}% chance {}".format(
                self._rand_result,
                self._counters[self._counter],
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )








    class IsDone(SetChecker):
        """Checker that verifies that a previous event is completed."""
        
        __slots__ = ()
        
        def __call__(self):
            for dependency in self._values:
                if dependency not in DONE:
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent("'{}' done".format(*self._values), indent_level)
                return "\n".join(
                [
                    self._indent(
                        "All of the following events are done:",
                        indent_level,
                    )
                ]
                + [
                    self._indent("- '{}'".format(dependency), indent_level + 1)
                    for dependency in self._values
                ]
            )
            
            for dependency in self._values:
                if dependency not in DONE:
                    return self._indent("'{}' not done".format(dependency), indent_level)
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be done".format(*self._values),
                    indent_level,
                )
                return self._indent("'{}' must be done".format(*self._values), indent_level)
            if negated:
                msg = "Any of the following events must not be done:"
            else:
                msg = "All of the following events must be done:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(dependency), indent_level + 1)
                for dependency in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                values_for_ui = {value_display_name(*self._values)}
            else:
                values_for_ui = [value_display_name(i) for i in self._values]
            
            if len(values_for_ui) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be done {}".format(
                        *values_for_ui, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' must be done {}".format(
                    *values_for_ui, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "Any of the following events must not be done:"
            else:
                msg = "All of the following events must be done:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        value_display_name(dependency),
                        self._visual_checks(dependency in DONE, negated),
                    ),
                    indent_level + 1,
                )
                for dependency in self._values
            ]
        )


    class IsNotDone(SetChecker):
        """Checker that verifies that a previous event isn't completed."""
        
        __slots__ = ()
        
        def __call__(self):
            for dependency in self._values:
                if dependency in DONE:
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent("'{}' not done".format(*self._values), indent_level)
                return "\n".join(
                [
                    self._indent(
                        "All of the following events are not done:",
                        indent_level,
                    )
                ]
                + [
                    self._indent("- '{}'".format(dependency), indent_level + 1)
                    for dependency in self._values
                ]
            )
            
            for dependency in self._values:
                if dependency in DONE:
                    return self._indent("'{}' done".format(dependency), indent_level)
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must be done".format(*self._values),
                    indent_level,
                )
                return self._indent(
                "'{}' must not be done".format(*self._values),
                indent_level,
            )
            if negated:
                msg = "Any of the following events must be done:"
            else:
                msg = "All of the following events must not be done:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(dependency), indent_level + 1)
                for dependency in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must be done {}".format(
                        *self._values, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' must not be done {}".format(
                    *self._values, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "Any of the following events must be done:"
            else:
                msg = "All of the following events must not be done:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        dependency,
                        self._visual_checks(dependency not in DONE, negated),
                    ),
                    indent_level + 1,
                )
                for dependency in self._values
            ]
        )


    class HasStamina(TargetedChecker):
        """Checker that verifies a specific if the hero has stamina."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero)):
                raise ValueError("{} don't have stamina".format(self._name))
        
        def __call__(self):
            return self._target.stamina
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} {}have stamina".format(self._name, "don't " if negated else ""),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} have stamina".format(self._name, " not" if negated else ""),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} have stamina {{image=gui/icons/icon_stamina_{}.png}}".format(
                    " not" if negated else "", hero.gender
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} have stamina {{image=gui/icons/icon_stamina_{}.png}} {}".format(
                    " not" if negated else "",
                    hero.gender,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MinStat(StatChecker):
        """Checker that verifies a minimum value of a Stat."""
        
        __slots__ = ()
        
        def __call__(self):
            
            if self._value is None:
                return self._stat.is_min
            
            
            return self._stat >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            if self._value is None:
                msg = "{}'s {} is{} at its min".format(
                self._name, self._stat_name, "" if negated else " not"
            )
            else:
                msg = "{}'s {} is {} than {}".format(
                self._name,
                self._stat_name,
                "higher (or equal)" if negated else "lower",
                self._value,
            )
            return self._indent(msg, indent_level)
        
        def description(self, indent_level=0, negated=False):
            if self._value is None:
                msg = "{}'s {} must{} be at its min".format(
                self._name, self._stat_name, " not" if negated else ""
            )
            else:
                msg = "{}'s {} must be {} than {}".format(
                self._name,
                self._stat_name,
                "lower" if negated else "higher (or equal)",
                self._value,
            )
            return self._indent(msg, indent_level)
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                if self._value is None:
                    msg = "{{image=gui/icons/icon_{}.png}} must{} be at its min".format(
                    self._stat_name, " not" if negated else ""
                )
                else:
                    if self._stat_name == "love":
                        visual_value = int(self._value / 2)
                    elif self._stat_name == "lesbian":
                        visual_value = int(self._value * 5)
                    else:
                        visual_value = self._value
                    if self._stat_name in ["love", "sub", "lesbian", "yandere", "siscon"]:
                        visual_value = f"{visual_value}%"
                    msg = "{{image=gui/icons/icon_{}.png}} {} {}".format(
                    self._stat_name, "<" if negated else ">=", visual_value
                )
            else:
                if self._value is None:
                    msg = "{{image=gui/icons/icon_{}.png}} must{} be at its min {}".format(
                    self._stat_name,
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                )
                else:
                    if self._stat_name == "love":
                        visual_value = int(self._value / 2)
                    elif self._stat_name == "lesbian":
                        visual_value = int(self._value * 5)
                    else:
                        visual_value = self._value
                    if self._stat_name in ["love", "sub", "lesbian", "yandere", "siscon"]:
                        visual_value = f"{visual_value}%"
                    msg = "{{image=gui/icons/icon_{}.png}} {} {} {}".format(
                    self._stat_name,
                    "<" if negated else ">=",
                    visual_value,
                    self._visual_checks(self.__call__(), negated),
                )
            return self._indent(msg, indent_level)


    class MaxStat(StatChecker):
        """Checker that verifies a maximum value of a Stat."""
        
        __slots__ = ()
        
        def __call__(self):
            
            if self._value is None:
                return self._stat.is_max
            
            
            return self._stat <= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            if self._value is None:
                msg = "{}'s {} is{} maxed out".format(
                self._name, self._stat_name, "" if negated else " not"
            )
            else:
                msg = "{}'s {} is {} than {}".format(
                self._name,
                self._stat_name,
                "lower (or equal)" if negated else "higher",
                self._value,
            )
            return self._indent(msg, indent_level)
        
        def description(self, indent_level=0, negated=False):
            if self._value is None:
                msg = "{}'s {} must{} be maxed out".format(
                self._name, self._stat_name, " not" if negated else ""
            )
            else:
                msg = "{}'s {} must be {} than {}".format(
                self._name,
                self._stat_name,
                "higher" if negated else "lower (or equal)",
                self._value,
            )
            return self._indent(msg, indent_level)
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                if self._value is None:
                    msg = "{{image=gui/icons/icon_{}.png}} must{} be maxed out".format(
                    self._stat_name, " not" if negated else ""
                )
                else:
                    if self._stat_name == "love":
                        visual_value = int(self._value / 2)
                    elif self._stat_name == "lesbian":
                        visual_value = int(self._value * 5)
                    else:
                        visual_value = self._value
                    if self._stat_name in ["love", "sub", "lesbian", "yandere", "siscon"]:
                        visual_value = f"{visual_value}%"
                    msg = "{{image=gui/icons/icon_{}.png}} {} {}".format(
                    self._stat_name, ">" if negated else "<=", visual_value
                )
            else:
                if self._value is None:
                    msg = "{{image=gui/icons/icon_{}.png}} must{} be maxed out {}".format(
                    self._stat_name,
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                )
                else:
                    if self._stat_name == "love":
                        visual_value = int(self._value / 2)
                    elif self._stat_name == "lesbian":
                        visual_value = int(self._value * 5)
                    else:
                        visual_value = self._value
                    if self._stat_name in ["love", "sub", "lesbian", "yandere", "siscon"]:
                        visual_value = f"{visual_value}%"
                    msg = "{{image=gui/icons/icon_{}.png}} {} {} {}".format(
                    self._stat_name,
                    ">" if negated else "<=",
                    visual_value,
                    self._visual_checks(self.__call__(), negated),
                )
            return self._indent(msg, indent_level)


    class IsActivity(TargetedSetChecker):
        """Checker that verifies the current ongoing activity."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero, Person)):
                raise ValueError("{} can't perform activities".format(self._name))
        
        def _get_activity(self):
            if isinstance(self._target, Hero):
                if isinstance(self._target.activity, basestring):
                    return self._target.activity
                
                return getattr(self._target.activity, "name", "None")
            if isinstance(self._target, Person):
                return self._target.activity_name
            return None
        
        def __call__(self):
            return self._get_activity() in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} is doing {}".format(self._name, self._get_activity()),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be doing {}".format(
                self._name,
                " not" if negated else "",
                self._stringify_set(last_join_by=" or "),
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            activity_for_ui = self._stringify_set(last_join_by=" or ", quote_values=True)
            if activity_for_ui == "'None'":
                if negated:
                    activity_for_ui = "any activity"
                else:
                    activity_for_ui = "no activity"
            if self._name == "target":
                return self._indent(
                "ust{} be doing {}".format(
                    " not" if negated else "",
                    activity_for_ui,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be doing {} {}".format(
                    " not" if negated else "",
                    activity_for_ui,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class ValidActivities(SetChecker):
        """Checker that verifies that some activities can be performed."""
        
        __slots__ = ()
        
        def __call__(self):
            
            
            
            for activity_name in self._values:
                
                activity = BaseActivity.find(activity_name)
                if activity is None:
                    if config.developer:
                        raise ValueError("nonexistent activity: {}".format(activity_name))
                    
                    
                    continue
                if not activity.test():
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent("'{}' is valid".format(*self._values), indent_level)
                return "\n".join(
                [
                    self._indent(
                        "All of the following activities are valid:",
                        indent_level,
                    )
                ]
                + [
                    self._indent("- '{}'".format(activity), indent_level + 1)
                    for activity in self._values
                ]
            )
            
            for activity_name in self._values:
                activity = BaseActivity.find(activity_name)
                if activity is None:
                    return self._indent(
                    "{} does not exist".format(activity_name),
                    indent_level,
                )
                if not activity.test():
                    return self._indent(
                    "{} is not valid".format(activity_name), indent_level
                )
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be valid".format(*self._values),
                    indent_level,
                )
                return self._indent(
                "'{}' must be valid".format(*self._values), indent_level
            )
            if negated:
                msg = "Any of the following activities must not be valid:"
            else:
                msg = "All of the following activities must be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(activity), indent_level + 1)
                for activity in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be valid {}".format(
                        *self._values, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' must be valid {}".format(
                    *self._values, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "Any of the following activities must not be valid:"
            else:
                msg = "All of the following activities must be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        activity, self._visual_checks(activity.test(), negated)
                    ),
                    indent_level + 1,
                )
                for activity in self._values
            ]
        )


    class InvalidActivities(SetChecker):
        """Checker that verifies that some activities can't be performed."""
        
        __slots__ = ()
        
        def __call__(self):
            
            
            
            for activity_name in self._values:
                
                activity = BaseActivity.find(activity_name)
                if activity is None:
                    if config.developer:
                        raise ValueError("nonexistent activity: {}".format(activity_name))
                    
                    
                    continue
                if activity.test():
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent(
                    "'{}' is not valid".format(*self._values),
                    indent_level,
                )
                return "\n".join(
                [
                    self._indent(
                        "All of the following activities are not valid:",
                        indent_level,
                    )
                ]
                + [
                    self._indent("- '{}'".format(activity), indent_level + 1)
                    for activity in self._values
                ]
            )
            
            for activity_name in self._values:
                activity = BaseActivity.find(activity_name)
                if activity is None:
                    return self._indent(
                    "{} does not exist".format(activity_name),
                    indent_level,
                )
                if activity.test():
                    return self._indent("{} is valid".format(activity_name), indent_level)
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must be valid".format(*self._values),
                    indent_level,
                )
                return self._indent(
                "'{}' must not be valid".format(*self._values),
                indent_level,
            )
            if negated:
                msg = "Any of the following activities must be valid:"
            else:
                msg = "All of the following activities must not be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(activity), indent_level + 1)
                for activity in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must be valid {}".format(
                        *self._values, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' must not be valid {}".format(
                    *self._values, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "Any of the following activities must be valid:"
            else:
                msg = "All of the following activities must not be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        BaseActivity.find(activity).display_name
                        if BaseActivity.find(activity)
                        and hasattr(BaseActivity.find(activity), "display_name")
                        else activity,
                        self._visual_checks(
                            BaseActivity.find(activity)
                            and not BaseActivity.find(activity).test(),
                            negated,
                        ),
                    ),
                    indent_level + 1,
                )
                for activity in self._values
            ]
        )


    class IsRoom(TargetedSetChecker):
        """Checker that verifies the current location."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero, Person)):
                raise ValueError("{} can't be in a room".format(self._name))
        
        def __call__(self):
            return self._target.get_room() in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} is in {}".format(self._name, self._target.get_room()),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be in {}".format(
                self._name,
                " not" if negated else "",
                self._stringify_set(last_join_by=" or "),
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be in {}".format(
                    " not" if negated else "",
                    self._stringify_set(
                        stringify=lambda i: Room.find(i).display_name
                        if hasattr(Room.find(i), "display_name")
                        else i.capitalize(),
                        last_join_by=" or ",
                    ),
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be in {} {}".format(
                    " not" if negated else "",
                    self._stringify_set(
                        stringify=lambda i: Room.find(i).display_name
                        if hasattr(Room.find(i), "display_name")
                        else i.capitalize(),
                        last_join_by=" or ",
                    ),
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class HasRoomTag(TargetedChecker):
        """Checker that verifies that the current location has a tag."""
        
        __slots__ = ("_tag",)
        
        def __init__(self, tag):
            super(HasRoomTag, self).__init__()
            if not isinstance(tag, basestring):
                raise ValueError("tag expected to be a string")
            self._tag = tag
        
        @property
        def tag(self):
            return self._tag
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero, Person)):
                raise ValueError("{} can't be in a room".format(self._name))
        
        def __call__(self):
            return Room.has_tag(self._target.get_room(), self._tag)
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} is in {}".format(self._name, self._target.get_room()),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be in a room with tag '{}'".format(
                self._name, " not" if negated else "", self._tag
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be in a room with tag '{}'".format(
                    " not" if negated else "", self._tag
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be in a room with tag '{}' {}".format(
                    " not" if negated else "",
                    self._tag,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class ValidRooms(SetChecker):
        """Checker that verifies that some rooms can be visited."""
        
        __slots__ = ()
        
        def __call__(self):
            
            
            
            for room_name in self._values:
                room = Room.find(room_name)
                if room is None:
                    if config.developer:
                        raise ValueError("nonexistent room: {}".format(room_name))
                    return False
                if not room.test():
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent("'{}' is valid".format(*self._values), indent_level)
                return "\n".join(
                [
                    self._indent(
                        "All of the following rooms are valid:",
                        indent_level,
                    )
                ]
                + [self._indent(room, indent_level + 1) for room in self._values]
            )
            
            for room_name in self._values:
                room = Room.find(room_name)
                if room is None:
                    return self._indent("{} does not exist".format(room_name), indent_level)
                if not room.test():
                    return self._indent("{} is not valid".format(room_name), indent_level)
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be valid".format(*self._values),
                    indent_level,
                )
                return self._indent(
                "'{}' must be valid".format(*self._values), indent_level
            )
            if negated:
                msg = "Any of the following rooms must not be valid:"
            else:
                msg = "All of the following rooms must be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(room), indent_level + 1)
                for room in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' must not be valid {}".format(
                        *self._values, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' must be valid {}".format(
                    *self._values, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "Any of the following rooms must not be valid:"
            else:
                msg = "All of the following rooms must be valid:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        room,
                        self._visual_checks(
                            Room.find(room) and Room.find(room).test(), negated
                        ),
                    ),
                    indent_level + 1,
                )
                for room in self._values
            ]
        )


    class MinDaysPlayed(Checker):
        """Checker that ensures a certain number of days played."""
        
        __slots__ = ("_days",)
        
        def __init__(self, days):
            if not isinstance(days, int):
                raise ValueError("days played expected to be an integer")
            self._days = days
        
        def __call__(self):
            return game.days_played >= self._days
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent("{} days played".format(game.days_played), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have played {} days".format(" not" if negated else "", self._days),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} have played {} days {}".format(
                " not" if negated else "",
                self._days,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsSpecialDate(Checker):
        """Checker that verifies special dates."""
        
        __slots__ = (
        "_season",
        "_day",
        "_date",
    )
        
        def __init__(self, date):
            if date not in game.calendar.SPECIAL_DATES:
                raise ValueError("unknown special date: {}".format(date))
            self._season, self._day = game.calendar.SPECIAL_DATES[date]
            self._date = date
        
        def __call__(self):
            return (
            self._season == game.calendar.season_name
            and self._day == game.calendar.day_of_season
        )
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "is{} the {} of {}".format(
                "" if negated else " not", self._season, self._day
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            if self._date == "independenceday":
                msg = "on National Day"
            elif self._date == "newyear":
                msg = "on New Year's Day"
            elif self._date == "valentine":
                msg = "on Valentine's Day"
            elif self._date == "halloween":
                msg = "on Halloween"
            elif self._date == "christmaseve":
                msg = "on Christmas Eve"
            elif self._date == "christmas":
                msg = "on Christmas Day"
            elif self._date == "newyeareve":
                msg = "on New Year's Eve"
            else:
                msg = "on the {} of {}".format(self._day, self._season)
            return self._indent("{}{}".format("not " if negated else "", msg), indent_level)
        
        def for_ui(self, indent_level=0, negated=False):
            if self._date == "independenceday":
                msg = "on National Day"
            elif self._date == "newyear":
                msg = "on New Year's Day"
            elif self._date == "valentine":
                msg = "on Valentine's Day"
            elif self._date == "halloween":
                msg = "on Halloween"
            elif self._date == "christmaseve":
                msg = "on Christmas Eve"
            elif self._date == "christmas":
                msg = "on Christmas Day"
            elif self._date == "newyeareve":
                msg = "on New Year's Eve"
            else:
                msg = "On the {} of {}".format(self._day, self._season)
            return self._indent(
            "{}{} {}".format(
                "not " if negated else "",
                msg,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsBirthday(TargetedChecker):
        """Checker that verifies birthday date."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero, Person)):
                raise ValueError("{} doesn't have a birthday".format(self._name))
        
        
        def __call__(self):
            if isinstance(self._target, Person) and not self._target.flags.birthdayknown:
                return False
            return self._target.birthday == [
            game.calendar.season_name,
            game.calendar.day_of_season,
        ]
        
        def debug_message(self, indent_level=0, negated=False):
            if isinstance(self._target, Person) and not self._target.flags.birthdayknown:
                return "you don't know {}'s birthday".format(self._name)
            return self._indent(
            "is{} {}'s birthday".format("" if negated else " not", self._name),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}on {}'s birthday".format("not " if negated else "", self._name),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "{} {}'s birthday".format("Not on" if negated else "On", self._name),
                indent_level,
            )
            else:
                return self._indent(
                "{} {}'s birthday {}".format(
                    "Not on" if negated else "On",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsGender(TargetedChecker):
        __slots__ = ("_gender",)
        
        def __init__(self, gender):
            if not isinstance(gender, basestring):
                raise TypeError("gender must be a string")
            gender = gender.lower()
            if gender in ("male", "m"):
                self._gender = "male"
            elif gender in ("female", "f"):
                self._gender = "female"
            else:
                raise ValueError("gender must be male or female")
        
        @property
        def gender(self):
            return self._gender
        
        def __call__(self):
            return self._target.gender == self._gender
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent("{} is {}".format(self._name, self._gender), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be {}".format(
                self._name, " not" if negated else "", self._gender
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if isinstance(self._target, Hero):
                return
            if self._name == "target":
                return self._indent(
                "Must{} be {}".format(" not" if negated else "", self._gender),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be {} {}".format(
                    " not" if negated else "",
                    self._gender,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsSeason(IntSetChecker):
        """Checker that verifies valid seasons."""
        
        __slots__ = ()
        
        def __call__(self):
            return game.season in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent("Is {}".format(SEASONS[game.season]), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "Season must{} be {}".format(
                " not" if negated else "",
                self._stringify_set(
                    stringify=lambda i: SEASONS[i], last_join_by=" or "
                ),
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Season must{} be {} {}".format(
                " not" if negated else "",
                self._stringify_set(
                    stringify=lambda i: SEASONS[i], last_join_by=" or "
                ),
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsDayOfWeek(IntSetChecker):
        """Checker that verifies that the current week day is valid."""
        
        __slots__ = ()
        
        def __call__(self):
            return game.week_day in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent("Is {}".format(DAYS[game.week_day - 1]), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "Day of week must{} be {}".format(
                " not" if negated else "",
                self._stringify_set(
                    stringify=lambda i: DAYS[i - 1], last_join_by=" or "
                ),
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Day of week must{} be {} {}".format(
                " not" if negated else "",
                self._stringify_set(
                    stringify=lambda i: DAYS[i - 1].capitalize(), last_join_by=" or "
                ),
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsHour(Checker):
        """Checker that verifies that the current time is between two hours."""
        
        __slots__ = "_start", "_end", "_reverse"
        
        def __init__(self, start, end=None):
            if end is None:
                end = start
            if not (0 <= start < 24):
                raise ValueError("the starting hour must be 0-23")
            if not (0 <= end < 24):
                raise ValueError("the finishing hour must be 0-23")
            self._start = start
            self._end = end
            self._reverse = start > end
        
        def __call__(self):
            if self._reverse:
                return self._start <= game.hour or game.hour <= self._end
            return self._start <= game.hour <= self._end
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent("Is {}:00".format(game.hour), indent_level)
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} be between {}:00 and {}:00".format(
                " not" if negated else "", self._start, self._end
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} be between {}:00 and {}:00 {}".format(
                " not" if negated else "",
                self._start,
                self._end,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsTimeOfDay(SetChecker):
        """Checker that verifies that the current time period is valid."""
        
        __slots__ = ()
        
        def __call__(self):
            return game.calendar.get_time_of_day() in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "is {}".format(game.calendar.get_time_of_day()), indent_level
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} be {}".format(
                " not" if negated else "", self._stringify_set(last_join_by=" or ")
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} be {} {}".format(
                " not" if negated else "",
                self._stringify_set(last_join_by=" or "),
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class HasVehicle(Checker):
        """Checker that verifies that the MC has a vehicle."""
        
        __slots__ = ("_property",)
        
        def __init__(self, motor=False):
            if motor:
                self._property = "has_motor_vehicle"
            else:
                self._property = "has_vehicle"
        
        def __call__(self):
            return hero[self._property]
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "has {} {}".format(
                "a" if negated else "no",
                "car" if self._property == "has_motor_vehicle" else "vehicle",
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "you need to have {} {}".format(
                "no" if negated else "a",
                "car" if self._property == "has_motor_vehicle" else "vehicle",
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "You need to have {} {} {}".format(
                "no" if negated else "a",
                "car" if self._property == "has_motor_vehicle" else "vehicle",
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class HasSkill(Checker):
        """Checker that verifies if the MC has some skill."""
        
        __slots__ = ("_skill",)
        
        def __init__(self, skill):
            if not isinstance(skill, basestring):
                raise TypeError("skill expected to be a string")
            self._skill = skill
        
        def __call__(self):
            return hero.has_skill(self._skill)
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} how to {}".format("knows" if negated else "doesn't know", self._skill),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} posses {} skill".format(" not" if negated else "", self._skill),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} posses {} skill {}".format(
                " not" if negated else "",
                self._skill,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class InInventory(Checker):
        """Checker that verifies if the MC has some item."""
        
        __slots__ = ("_item",)
        
        def __init__(self, item):
            if not isinstance(item, basestring):
                raise TypeError("item expected to be a string")
            self._item = item
        
        def __call__(self):
            return self._item in hero.inventory
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "has {} {}".format("a" if negated else "no", self._item),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have {}".format(" not" if negated else "", self._item),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} have {} {}".format(
                " not" if negated else "",
                self._item,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsWearing(Checker):
        """Checker that verifies if the MC has some item equipped."""
        
        __slots__ = ("_item",)
        
        def __init__(self, item):
            if not isinstance(item, basestring):
                raise TypeError("item expected to be a string")
            self._item = item
        
        def __call__(self):
            return (
            hero.equipment["clothes"] and hero.equipment["clothes"].name == self._item
        ) or (
            hero.equipment["accessory"]
            and hero.equipment["accessory"].name == self._item
        )
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "must {}wearing {}".format("not " if negated else "", self._item),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} be wearing {}".format(" not" if negated else "", self._item),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} be wearing {} {}".format(
                " not" if negated else "",
                self._item,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class InHarem(TargetedChecker):
        """Checker that verifies that the target is active in the given value."""
        
        __slots__ = ()
        
        def __init__(self, harem):
            super(InHarem, self).__init__()
            if not isinstance(harem, basestring):
                raise ValueError("harem expected to be a string")
            self._harem = harem
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("{} can't be in a harem".format(self._name))
        
        def __call__(self):
            return Harem.find(self._target, name=self._harem)
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} is in {} harem".format(self._name, self._harem),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be in {} harem".format(
                self._name, " not" if negated else "", self._harem
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be in {} harem".format(
                    " not" if negated else "", self._harem.title()
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be in {} harem {}".format(
                    " not" if negated else "",
                    self._harem.title(),
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsActiveHarem(SetChecker):
        """Checker that verifies if a list of harems is active."""
        
        __slots__ = ()
        
        def __call__(self):
            
            for harem_name in self._values:
                if not isinstance(harem_name, str):
                    raise ValueError(f"Harem name must be a string, got {type(harem_name)}")
                
                harem = Harem.find_by_name(harem_name)
                if not harem:
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                if len(self._values) == 1:
                    return self._indent(
                    "'{}' harem must not be active".format(*self._values),
                    indent_level,
                )
                return "\n".join(
                [
                    self._indent(
                        "None of the following harems must be active:",
                        indent_level,
                    )
                ]
                + [
                    self._indent("- '{}'".format(harem_name), indent_level + 1)
                    for harem_name in self._values
                ]
            )
            
            for harem_name in self._values:
                harem = Harem.find_by_name(harem_name)
                if harem is None or not harem.is_active():
                    return self._indent(
                    "'{}' harem is not active".format(harem_name),
                    indent_level,
                )
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' harem must not be active".format(*self._values),
                    indent_level,
                )
                return self._indent(
                "'{}' harem must be active".format(*self._values),
                indent_level,
            )
            if negated:
                msg = "None of the following harems must be active:"
            else:
                msg = "All of the following harems must be active:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent("- '{}'".format(harem_name), indent_level + 1)
                for harem_name in self._values
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                if negated:
                    return self._indent(
                    "'{}' harem must not be active {}".format(
                        *self._values, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level,
                )
                return self._indent(
                "'{}' harem must be active {}".format(
                    *self._values, self._visual_checks(self.__call__(), negated)
                ),
                indent_level,
            )
            if negated:
                msg = "None of the following harems must be active:"
            else:
                msg = "All of the following harems must be active:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                self._indent(
                    "- '{}' {}".format(
                        harem_name, self._visual_checks(self.__call__(), negated)
                    ),
                    indent_level + 1,
                )
                for harem_name in self._values
            ]
        )


    class TogetherInHarem(SetChecker):
        """Checker that verifies if a group of people are together in a specified harem.

    TogetherInHarem('Harem_name', 'name_A', 'name_B', 'name_C', ...)

    ex: TogetherInHarem('home', 'bree', 'sasha')
        Not(TogetherInHarem('home', 'minami', 'shiori', 'morgan')),
    """
        
        __slots__ = ()
        
        def __init__(self, room_tag, *people):
            super(TogetherInHarem, self).__init__()
            if not isinstance(room_tag, str):
                raise ValueError(f"Room tag must be a string, got {type(room_tag)}")
            if not all(isinstance(person, str) for person in people):
                raise ValueError("All people must be strings representing their names.")
            self._room_tag = room_tag
            self._people = people
        
        def __call__(self):
            
            return Harem.together(*self._people, name=self._room_tag)
        
        def debug_message(self, indent_level=0, negated=False):
            if negated:
                return self._indent(
                "None of these people should be together in the '{}' harem: {}".format(
                    self._room_tag, ", ".join(self._people)
                ),
                indent_level,
            )
            else:
                return self._indent(
                "All of these people must be together in the '{}' harem: {}".format(
                    self._room_tag, ", ".join(self._people)
                ),
                indent_level,
            )
        
        def description(self, indent_level=0, negated=False):
            if negated:
                return self._indent(
                "None of the following people should be together in the '{}' harem: {}".format(
                    self._room_tag, ", ".join(self._people)
                ),
                indent_level,
            )
            else:
                return self._indent(
                "All of the following people must be together in the '{}' harem: {}".format(
                    self._room_tag, ", ".join(self._people)
                ),
                indent_level,
            )
        
        def for_ui(self, indent_level=0, negated=False):
            if negated:
                return self._indent(
                "None of the following people should be together in the '{}' harem: {} {}".format(
                    self._room_tag,
                    ", ".join(self._people),
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )
            else:
                return self._indent(
                "All of the following people must be together in the '{}' harem: {} {}".format(
                    self._room_tag,
                    ", ".join(self._people),
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsFlag(TargetedSetChecker):
        """Checker that verifies that the flag is one of the given values."""
        
        __slots__ = "_flag", "_flags", "_timers"
        
        def __init__(self, flag, *values):
            if len(values) == 0:
                values = (True,)
            super(IsFlag, self).__init__(*values)
            if not isinstance(flag, basestring):
                raise TypeError("flag expected to be a string")
            self._flag = flag
            self._flags = None
        
        def post_set_target(self):
            
            if not isinstance(self._target, Flagged):
                raise ValueError("{} doesn't have flags".format(self._name))
            self._flags = self._target.flags
        
        def __call__(self):
            return self._flags[self._flag] in self._values
        
        def debug_message(self, indent_level=0, negated=False):
            
            if (
            self._name != "target"
            and self._target.timers[self._flag] > 0
            and self._target.timers[self._flag] != 65536
        ):
                return self._indent(
                "{}'s timer '{}' is {} ({} day{})".format(
                    self._name,
                    self._flag,
                    self._target.flags[self._flag],
                    self._target.timers[self._flag],
                    "s" if self._target.timers[self._flag] > 1 else "",
                ),
                indent_level,
            )
            return self._indent(
            "{}'s flag '{}' is {}".format(
                self._name, self._flag, self._target.flags[self._flag]
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            if (
            self._name != "target"
            and self._target.timers[self._flag] > 0
            and self._target.timers[self._flag] != 65536
        ):
                return self._indent(
                "{}'s timer '{}' must{} be {} ({} day{})".format(
                    self._name,
                    self._flag,
                    " not" if negated else "",
                    self._stringify_set(last_join_by=" or "),
                    self._target.timers[self._flag],
                    "s" if self._target.timers[self._flag] > 1 else "",
                ),
                indent_level,
            )
            return self._indent(
            "{}'s flag '{}' must{} be {}".format(
                self._name,
                self._flag,
                " not" if negated else "",
                self._stringify_set(last_join_by=" or "),
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Flag '{}' must{} be {}".format(
                    self._flag,
                    " not" if negated else "",
                    self._stringify_set(last_join_by=" or "),
                ),
                indent_level,
            )
            else:
                if (
                self._target.timers[self._flag] > 0
                and self._target.timers[self._flag] != 65536
            ):
                    return self._indent(
                    "Timer '{}' must{} be {} {} ({} day{})".format(
                        self._flag,
                        " not" if negated else "",
                        self._stringify_set(last_join_by=" or "),
                        self._visual_checks(self.__call__(), negated),
                        self._target.timers[self._flag],
                        "s" if self._target.timers[self._flag] > 1 else "",
                    ),
                    indent_level,
                )
                return self._indent(
                "Flag '{}' must{} be {} {}".format(
                    self._flag,
                    " not" if negated else "",
                    self._stringify_set(last_join_by=" or "),
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class HasCheated(IsFlag):
        """Checker that verifies that the cheated flag is one of the given values."""
        
        __slots__ = "_flag", "_flags"
        
        def __init__(self):
            super(HasCheated, self).__init__("cheated", [True])
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{}'s flag '{}' is {}".format(
                self._name, self._flag, self._target.flags[self._flag]
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "You must{} have cheated on {}".format(
                " not" if negated else "", self._name
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "You must{} have cheated on {}".format(
                    " not" if negated else "", self._name
                ),
                indent_level,
            )
            else:
                return self._indent(
                "You must{} have cheated on {} {}".format(
                    " not" if negated else "",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class InFlag(FlagChecker):
        """Checker that verifies that the value is in the flag (iterable)."""
        
        __slots__ = ()
        
        def __call__(self):
            if not self._flags[self._flag]:
                return False
            if not isinstance(self._flags[self._flag], (list, tuple, set)):
                raise TypeError(
                "{} must be an iterable and not {}".format(
                    self._name, self._flags[self._flag]
                )
            )
            return self._value in self._flags[self._flag]
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} value is in {}'s flag '{}' {}".format(
                self._value, self._name, self._flag, self._target.flags[self._flag]
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} value must{} be {} in {}'s flag '{}'".format(
                self._value,
                " not" if negated else "",
                self._name,
                self._flag,
                self._target.flags[self._flag],
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "{} value must{} be {} in flag '{}'".format(
                    self._value,
                    " not" if negated else "",
                    self._flag,
                    self._target.flags[self._flag],
                ),
                indent_level,
            )
            else:
                return self._indent(
                "{} value must{} be {} in flag '{}' {}".format(
                    self._value,
                    " not" if negated else "",
                    self._flag,
                    self._target.flags[self._flag],
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MinFlag(FlagChecker):
        """Checker that verifies that a flag is over a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._flags[self._flag] >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}' is {} than {}".format(
                self._name,
                self._flag,
                "higher (or equal)" if negated else "lower",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}' must be {} than {}".format(
                self._name,
                self._flag,
                "lower" if negated else "higher (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Flag '{}' must be {} than {}".format(
                    self._flag,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Flag '{}' must be {} than {} {}".format(
                    self._flag,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MaxFlag(FlagChecker):
        """Checker that verifies that a flag is below a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._flags[self._flag] <= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}' is {} than {}".format(
                self._name,
                self._flag,
                "lower (or equal)" if negated else "higher",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}' must be {} than {}".format(
                self._name,
                self._flag,
                "higher" if negated else "lower (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Flag '{}' must be {} than {}".format(
                    self._flag,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Flag '{}' must be {} than {} {}".format(
                    self._flag,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MinTimer(TimerChecker):
        """Checker that verifies that a timer is over a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._timers[self._timer] >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}'s duration is {} than {}".format(
                self._name,
                self._timer,
                "higher (or equal)" if negated else "lower",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}'s duration must be {} than {}".format(
                self._name,
                self._timer,
                "lower" if negated else "higher (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Timer '{}'s duration must be {} than {}".format(
                    self._timer,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Timer '{}'s duration must be {} than {} {}".format(
                    self._timer,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MaxTimer(TimerChecker):
        """Checker that verifies that a timer is below a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._timers[self._timer] <= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}'s duration is {} than {}".format(
                self._name,
                self._timer,
                "lower (or equal)" if negated else "higher",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s flag '{}''s duration must be {} than {}".format(
                self._name,
                self._timer,
                "higher" if negated else "lower (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Timer '{}''s duration must be {} than {}".format(
                    self._timer,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Timer '{}''s duration must be {} than {} {}".format(
                    self._timer,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MinCounter(CounterChecker):
        """Checker that verifies that a counter is over a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._counters[self._counter] >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s counter '{}' is {} than {}".format(
                self._name,
                self._counter,
                "higher (or equal)" if negated else "lower",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s counter '{}' must be {} than {}".format(
                self._name,
                self._counter,
                "lower" if negated else "higher (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Counter '{}' must be {} than {}".format(
                    self._counter,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Counter '{}' must be {} than {} {}".format(
                    self._counter,
                    "lower" if negated else "higher (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MaxCounter(CounterChecker):
        """Checker that verifies that a counter is below a threshold."""
        
        __slots__ = ()
        
        def __call__(self):
            return self._counters[self._counter] <= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s counter '{}' is {} than {}".format(
                self._name,
                self._counter,
                "lower (or equal)" if negated else "higher",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{}'s counter '{}' must be {} than {}".format(
                self._name,
                self._counter,
                "higher" if negated else "lower (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Counter '{}' must be {} than {}".format(
                    self._counter,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Counter '{}' must be {} than {} {}".format(
                    self._counter,
                    "higher" if negated else "lower (or equal)",
                    self._value,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class HasTrait(TargetedChecker):
        """Checker that verifies if a person has a trait."""
        
        __slots__ = "_trait", "_traits"
        
        def __init__(self, trait):
            super(HasTrait, self).__init__()
            if not isinstance(trait, basestring):
                raise ValueError("trait expected to be a string")
            self._trait = trait
            self._traits = None
        
        @property
        def trait(self):
            return self._trait
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("{} can't have traits".format(self._name))
            self._traits = self._target.traits
        
        def __call__(self):
            return self._trait in self._traits
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} {} '{}' trait".format(
                self._name, "has" if negated else "doesn't have", self._trait
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} have '{}' trait".format(
                self._name, " not" if negated else "", self._trait
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                if self._trait not in self._traits.known:
                    return self._indent(
                    "Must{} have one trait you don't know yet".format(
                        " not" if negated else ""
                    ),
                    indent_level,
                )
                else:
                    return self._indent(
                    "Must{} have '{}' trait".format(
                        " not" if negated else "", self._trait
                    ),
                    indent_level,
                )
            else:
                if self._trait not in self._traits.known:
                    return self._indent(
                    "Must{} have one trait you don'y know yet {}".format(
                        " not" if negated else "",
                        self._visual_checks(self.__call__(), negated),
                    ),
                    indent_level,
                )
                else:
                    return self._indent(
                    "Must{} have '{}' trait {}".format(
                        " not" if negated else "",
                        self._trait,
                        self._visual_checks(self.__call__(), negated),
                    ),
                    indent_level,
                )


    class OnDate(TargetedChecker):
        """Checker that verifies if there is an ongoing date."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, (Hero, Person)):
                raise ValueError("{} can't be on a date".format(self._name))
        
        def __call__(self):
            return self._target.on_date
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} is{} on a date".format(self._name, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be on a date".format(self._name, " not" if negated else ""),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be on a date".format(" not" if negated else ""),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be on a date {}".format(
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class MinDateScore(Checker):
        """Checker that verifies the date score is over a threshold."""
        
        __slots__ = ("_value",)
        
        def __init__(self, value):
            if not isinstance(value, int):
                raise TypeError("value expected to be an integer")
            self._value = value
        
        def __call__(self):
            return game.active_date.score >= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "date score is {} than {}%".format(
                "higher (or equal)" if negated else "lower", self._value
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "date score must be {} than {}%".format(
                "lower" if negated else "higher (or equal)", self._value
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Date score must be {} than {}% {}".format(
                "lower" if negated else "higher (or equal)",
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsHidden(TargetedChecker):
        """Checker that verifies if the character is hidden."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("{} can't be hidden".format(self._name))
        
        def __call__(self):
            return self._target.hidden
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} is{} hidden".format(self._name, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be hidden".format(self._name, " not" if negated else ""),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be hidden".format(" not" if negated else ""),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be hidden {}".format(
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsPresent(TargetedChecker):
        """Checker that verifies if the character is present."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("{} can't be present".format(self._name))
        
        def __call__(self):
            return self._target.get_room() == game.room
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} is{} present".format(self._name, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be present".format(self._name, " not" if negated else ""),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be present".format(" not" if negated else ""),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be present {}".format(
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsVisiblyPregnant(TargetedChecker):
        """Checker that verifies if the character is visibly pregnant."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Girl):
                raise ValueError("{} can't be visibly pregnant".format(self._name))
        
        def __call__(self):
            return self._target.is_visibly_pregnant
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} is{} visibly pregnant".format(self._name, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be visibly pregnant".format(
                self._name, " not" if negated else ""
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be visibly pregnant".format(" not" if negated else ""),
                indent_level,
            )
            else:
                if self._target.flags.NPCpregnancy:
                    info = f"({self._target.flags.NPCpregnancy})"
                elif self._target.counters.pregnant:
                    info = f"({self._target.counters.pregnant}/9)"
                else:
                    info = ""
                return self._indent(
                "Must{} be visibly pregnant {}{} ".format(
                    " not" if negated else "",
                    info,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsActive(TargetedChecker):
        """Checker that verifies that the target is the active character."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("Can't interact with {} ".format(self._name))
        
        def __call__(self):
            return self._target == active_girl
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "MC {}interact with {}".format("" if negated else "doesn't ", self._name),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "You must{} interact with {}".format("n't " if negated else "", self._name),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "You must{} interact with {}".format(
                    "n't " if negated else "", self._name
                ),
                indent_level,
            )
            else:
                return self._indent(
                "You must{} interact with {} {}".format(
                    "n't " if negated else "",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsGone(TargetedChecker):
        """Checker that verifies whether the target character is gone."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("{} can't be gone".format(self._name))
        
        def __call__(self):
            return self._target.is_gone_forever
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "{} is{} gone".format(self._name, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be gone".format(self._name, " not" if negated else ""),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} be gone".format(" not" if negated else ""),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} be gone {}".format(
                    " not" if negated else "",
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsDatePlanned(TargetedChecker):
        """Checker that verifies if there is a date planned."""
        
        __slots__ = ("_id",)
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("can't have dates planned with {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            return len(hero.calendar.find(girl=self._id, date_only=True)) != 0
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "date{} planned with {}".format("" if negated else " not", self._name),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have date planned with {}".format(
                " not" if negated else "", self._name
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} have date planned with {}".format(
                    " not" if negated else "", self._name
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} have date planned with {} {}".format(
                    " not" if negated else "",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class IsLabelAppointmentPlanned(Checker):
        """Checker that verifies if there is an appointment with label label planned."""
        
        __slots__ = ("_label",)
        
        def __init__(self, label):
            if not isinstance(label, basestring):
                raise TypeError("appointment label expected to be a string")
            self._label = label
        
        def __call__(self):
            return len(hero.calendar.find(label=self._label)) != 0
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "appointment {}{} planned".format(self._label, "" if negated else " not"),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have appointment {} planned".format(
                " not" if negated else "", self._value
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "Must{} have appointment planned {} {}".format(
                " not" if negated else "",
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class IsDateTime(TargetedChecker):
        """Checker that verifies if there is a date planned right now."""
        
        __slots__ = ("_id",)
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("can't have dates planned with {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            return hero.calendar.has_appointment(girl=self._id)
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "date{} planned with {} right now".format(
                "" if negated else " not", self._name
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have date planned with {} right now".format(
                " not" if negated else "", self._name
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} have date planned with {} right now".format(
                    " not" if negated else "", self._name
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} have date planned with {} right now {}".format(
                    " not" if negated else "",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class ContactKnown(TargetedChecker):
        """Checker that verifies if the hero has the contact of the target."""
        
        __slots__ = ("_id",)
        
        def post_set_target(self):
            if not isinstance(self._target, Person):
                raise ValueError("can't have contacts of {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            return self._id in hero.smartphone_contacts
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "hero {} {}'s contact".format(
                "has" if negated else "doesn't have", self._name
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "must{} have {}'s contact".format(" not" if negated else "", self._name),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if self._name == "target":
                return self._indent(
                "Must{} have {}'s contact".format(
                    " not" if negated else "", self._name
                ),
                indent_level,
            )
            else:
                return self._indent(
                "Must{} have {}'s contact {}".format(
                    " not" if negated else "",
                    self._name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class NPCInRoom(TargetedSetChecker):
        """Checker that verifies that the npcs are in the room (iterable)."""
        
        __slots__ = ()
        
        def post_set_target(self):
            if not isinstance(self._target, Room):
                raise ValueError("can't have an NPC check of {}".format(self._name))
        
        def __call__(self):
            present_npcs = set(self._target.get_present_npcs_ids())
            return self._values.issubset(present_npcs)
        
        def debug_message(self, indent_level=0, negated=False):
            
            return self._indent(
            "{} is in {}".format(" ".join(self._values), self._target.display_name),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "{} must{} be in {}".format(
                " ".join(self._values),
                " not" if negated else "",
                self._target.display_name,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            if len(self._values) == 1:
                return self._indent(
                "{} must{} be in {} {}".format(
                    " ".join([Person.find(v).name for v in self._values]),
                    " not" if negated else "",
                    self._target.display_name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )
            else:
                who = (
                ", ".join(
                    map(
                        lambda x: x.name,
                        [Person.find(v) for v in list(self._values)[:-1]],
                    )
                )
                + " and "
                + Person.find(list(self._values)[-1]).name
            )
                return self._indent(
                "{} must{} be in {} {}".format(
                    who,
                    " not" if negated else "",
                    self._target.display_name,
                    self._visual_checks(self.__call__(), negated),
                ),
                indent_level,
            )


    class NPCNumber(TargetedChecker):
        """Checker that verifies that there are at least value NPC in a room"""
        
        __slots__ = "_id", "_value"
        
        def __init__(self, value):
            super(TargetedChecker, self).__init__()
            self._value = value
        
        def post_set_target(self):
            if not isinstance(self._target, Room):
                raise ValueError("can't have an NPC check of {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            present_npc = len(self._target.get_present_npcs())
            return present_npc == self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} is{} {}".format(
                self._target.display_name, "" if negated else " not", self._value
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must{} be {}".format(
                self._target.display_name, " not" if negated else "", self._value
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must{} be {} {}".format(
                self._target.display_name,
                " not" if negated else "",
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class NPCMin(TargetedChecker):
        """Checker that verifies that there are at least value NPC in a room"""
        
        __slots__ = "_id", "_value"
        
        def __init__(self, value):
            super(TargetedChecker, self).__init__()
            self._value = value
        
        def post_set_target(self):
            if not isinstance(self._target, Room):
                raise ValueError("can't have an NPC check of {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            present_npc = len(self._target.get_present_npcs())
            return self._value <= present_npc <= 100
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} is {} than {}".format(
                self._target.display_name,
                "higher (or equal)" if negated else "lower",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must be {} than {}".format(
                self._target.display_name,
                "lower" if negated else "higher (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must be {} than {} {}".format(
                self._target.display_name,
                "lower" if negated else "higher (or equal)",
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )


    class NPCMax(TargetedChecker):
        """Checker that verifies that a flag is below a threshold."""
        
        __slots__ = "_id", "_value"
        
        def __init__(self, value):
            super(TargetedChecker, self).__init__()
            self._value = value
        
        def post_set_target(self):
            if not isinstance(self._target, Room):
                raise ValueError("can't have an NPC check of {}".format(self._name))
            self._id = self._target.id
        
        def __call__(self):
            present_npc = len(self._target.get_present_npcs())
            return 0 <= present_npc <= self._value
        
        def debug_message(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} is {} than {}".format(
                self._target.display_name,
                "lower (or equal)" if negated else "higher",
                self._value,
            ),
            indent_level,
        )
        
        def description(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must be {} than {}".format(
                self._target.display_name,
                "higher" if negated else "lower (or equal)",
                self._value,
            ),
            indent_level,
        )
        
        def for_ui(self, indent_level=0, negated=False):
            return self._indent(
            "NPC number in {} must be {} than {} {}".format(
                self._target.display_name,
                "higher" if negated else "lower (or equal)",
                self._value,
                self._visual_checks(self.__call__(), negated),
            ),
            indent_level,
        )





    class GameTarget(WrapperChecker):
        """Sets the target to game."""
        
        __slots__ = ("_target",)
        
        def __init__(self, *checkers):
            super(GameTarget, self).__init__(*checkers)
            self._target = self.set_target(game)
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join([self._indent("Game:", indent_level)] + checkers_ui)
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join([self._indent("{b}Game:{/b}", indent_level)] + checkers_ui)
            return


    class HeroTarget(WrapperChecker):
        """Sets the target to "hero"."""
        
        __slots__ = ("_target",)
        
        def __init__(self, *checkers):
            super(HeroTarget, self).__init__(*checkers)
            self._target = self.set_target(hero)
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{self._target.name}:",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{{b}}{self._target.name}:{{/b}}",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return


    class PersonTarget(WrapperChecker):
        """Sets the target to the provided person."""
        
        __slots__ = ("_id", "_target")
        
        def __init__(self, person, *checkers):
            if any(
            isinstance(checker, Not) and isinstance(checker._checker, IsGone)
            for checker in checkers
        ):
                raise ValueError("PersonTarget provided Not(IsGone()) checker (illegal)")
            if not isgone_in_checkers(checkers):
                checkers = (Not(IsGone()), *checkers)
            super(PersonTarget, self).__init__(*checkers)
            person = Person.find(person)
            if person is not None:
                self._id = person.id
                self._target = self.set_target(person)
            else:
                self._id = None
        
        def __call__(self):
            
            if self._id is None:
                return False
            return super(PersonTarget, self).__call__()
        
        @property
        def id(self):
            return self._id
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{self._target.name}:",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{{b}}{self._target.name}:{{/b}}",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return


    class ActiveTarget(WrapperChecker):
        """Sets the target to the active person."""
        
        __slots__ = ("_target",)
        
        def __call__(self):
            
            if active_girl.id is None:
                return False
            for checker in self._checkers:
                
                if hasattr(checker, "set_target"):
                    self._target = checker.set_target(active_girl.object)
                if not checker():
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if active_girl.id is None:
                return self._indent("No active person", indent_level)
            super(ActiveTarget, self).debug_message(indent_level, negated)
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join(
                [self._indent(f"{self._target}:", indent_level)] + checkers_ui
            )
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                if hasattr(self, "_target"):
                    return "\n".join(
                    [self._indent(f"{{b}}{self._target}:{{/b}}", indent_level)]
                    + checkers_ui
                )
                else:
                    return "\n".join(
                    [self._indent(f"{{b}}Active npc:{{/b}}", indent_level)]
                    + checkers_ui
                )
            return


    class DateTarget(WrapperChecker):
        """Sets the target to the date person."""
        
        __slots__ = ("_target",)
        
        def __call__(self):
            
            if date_girl.id is None:
                return False
            for checker in self._checkers:
                
                if hasattr(checker, "set_target"):
                    self._target = checker.set_target(date_girl.object)
                if not checker():
                    return False
            return True
        
        def debug_message(self, indent_level=0, negated=False):
            if date_girl.id is None:
                return self._indent("No date person", indent_level)
            super(DateTarget, self).debug_message(indent_level, negated)
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join(
                [self._indent(f"{self._target}:", indent_level)] + checkers_ui
            )
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join(
                [self._indent(f"{{b}}{self._target}:{{/b}}", indent_level)]
                + checkers_ui
            )
            return


    class RoomTarget(WrapperChecker):
        """Sets the target to the provided room."""
        
        __slots__ = ("_id", "_target")
        
        def __init__(self, room, *checkers):
            super(RoomTarget, self).__init__(*checkers)
            room = Room.find(room)
            if room is not None:
                self._id = room.id
                self._target = self.set_target(room)
            else:
                self._id = None
        
        def __call__(self):
            
            if self._id is None:
                return False
            return super(RoomTarget, self).__call__()
        
        @property
        def id(self):
            return self._id
        
        def description(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{self._target.name}:",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return
        
        def for_ui(self, indent_level=0, negated=False):
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join(
                [
                    self._indent(
                        f"{{b}}{self._target.display_name}:{{/b}}",
                        indent_level,
                    )
                ]
                + checkers_ui
            )
            return






    class And(WrapperChecker):
        """Logic AND combination of checkers."""
        
        __slots__ = ()
        
        def debug_message(self, indent_level=0, negated=False):
            
            if negated:
                return "\n".join(
                [self._indent("Any of:", indent_level)]
                + [
                    checker.debug_message(
                        indent_level=indent_level + 1,
                        negated=negated,
                    )
                    for checker in self._checkers
                ]
            )
            
            for checker in self._checkers:
                if not checker():
                    return checker.debug_message(indent_level=indent_level, negated=negated)
            raise Exception("printing a debug message of a successful condition")
        
        def description(self, indent_level=0, negated=False):
            
            if negated:
                msg = "Any of:"
            else:
                msg = "All of:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                checker.description(indent_level=indent_level + 1, negated=negated)
                for checker in self._checkers
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            
            if negated:
                msg = "Any of:"
            else:
                msg = "All of:"
            checkers_ui = [
            checker.for_ui(
                indent_level=indent_level + 1,
                negated=negated,
            )
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join([self._indent(msg, indent_level)] + checkers_ui)
            return


    class Or(WrapperChecker):
        """Logic OR combination of checkers."""
        
        __slots__ = ()
        
        def __call__(self):
            return any(checker() for checker in self._checkers)
        
        def debug_message(self, indent_level=0, negated=False):
            
            if negated:
                
                for checker in self._checkers:
                    if checker():
                        return checker.debug_message(
                        indent_level=indent_level, negated=negated
                    )
                raise Exception("printing a debug message of a successful condition")
            return "\n".join(
            [self._indent("Any of:", indent_level)]
            + [
                checker.debug_message(indent_level=indent_level + 1, negated=negated)
                for checker in self._checkers
            ]
        )
        
        def description(self, indent_level=0, negated=False):
            
            if negated:
                msg = "All of:"
            else:
                msg = "Any of:"
            return "\n".join(
            [self._indent(msg, indent_level)]
            + [
                checker.description(indent_level=indent_level + 1, negated=negated)
                for checker in self._checkers
            ]
        )
        
        def for_ui(self, indent_level=0, negated=False):
            
            if negated:
                msg = "All of:"
            else:
                msg = "Any of:"
            checkers_ui = [
            checker.for_ui(indent_level=indent_level + 1, negated=negated)
            for checker in self._checkers
        ]
            checkers_ui = [i for i in checkers_ui if i is not None]
            if checkers_ui:
                return "\n".join([self._indent(msg, indent_level)] + checkers_ui)
            return


    class Not(Checker):
        """Logic NOT operation on checker."""
        
        __slots__ = ("_checker",)
        
        def __init__(self, checker):
            if isinstance(checker, basestring):
                checker = RawChecker(checker)
            if not isinstance(checker, PartialChecker):
                raise ValueError("non-checker provided to NOT checker")
            self._checker = checker
        
        def __call__(self):
            return not self._checker()
        
        def set_target(self, target):
            if hasattr(self._checker, "set_target"):
                return self._checker.set_target(target)
            return
        
        def debug_message(self, indent_level=0, negated=False):
            return self._checker.debug_message(
            indent_level=indent_level, negated=not negated
        )
        
        def description(self, indent_level=0, negated=False):
            return self._checker.description(indent_level=indent_level, negated=not negated)
        
        def for_ui(self, indent_level=0, negated=False):
            return self._checker.for_ui(indent_level=indent_level, negated=not negated)


    def isgone_in_checkers(checkers):
        for c in checkers:
            if isinstance(c, IsGone):
                return True
            elif isinstance(c, (And, Or)):
                if isgone_in_checkers(c._checkers):
                    return True
        return False


    def value_display_name(value):
        if BaseEvent.find(value):
            return BaseEvent.find(value).display_name
        elif BaseActivity.find(value):
            return BaseActivity.find(value).display_name
        elif TalkSubject.find(value):
            return TalkSubject.find(value).display_name
        return value
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
