
init -35 python:



    class RegistryMeta(type):
        """Creates a class-specific registry."""
        
        def __new__(cls, name, bases, dct):
            dct["_registry"] = {}
            return super(RegistryMeta, cls).__new__(cls, name, bases, dct)


    class Registry(metaclass=RegistryMeta):
        """
    Manages a class-specific registry of all known instances.

    It requires the first parameter in the __init__ method to be the id
    which will be used as the key in the registry.
    """
        
        def __init__(self, id, *args, **kwargs):
            super(Registry, self).__init__(id, *args, **kwargs)
            if config.developer and id in self._registry:
                raise ValueError(
                'Registry for "{}" found duplicate id "{}"'.format(
                    self.__class__.__name__, id
                )
            )
            self._registry[id] = self
        
        @classmethod
        def sort_registry(cls, key=None, reverse=False):
            cls._registry = OrderedDict(
            sorted(cls._registry.items(), key=key, reverse=reverse)
        )
        
        @classmethod
        def find(cls, id):
            """find returns the instance from the registry by id."""
            if id is None:
                if config.developer:
                    raise ValueError(
                    'Registry.find for "{}" passed None value'.format(cls.__name__)
                )
                return None
            return cls._registry.get(id, None)
        
        @classmethod
        def all(cls):
            """yields all the registry."""
            for value in cls._registry.values():
                yield value
        
        @classmethod
        def filter(cls, function=None):
            """yields a subset of the registry that verifies certain conditions."""
            for value in cls._registry.values():
                if function is None or function(value):
                    yield value
        
        @classmethod
        def sort(cls, key=None, reverse=False):
            """returns the sorted values from the registry."""
            return sorted(cls._registry.values(), key=key, reverse=reverse)
        
        
        
        
        
        
        
        
        
        
        
        @classmethod
        def filtered_sort(cls, filter=None, key=None, reverse=False):
            """sorts a previously filtered subset of the registry."""
            return sorted(cls.filter(filter), key=key, reverse=reverse)
        
        @classmethod
        def sorted_filter(cls, key=None, reverse=False, filter=None):
            """filters the previously sorted registry."""
            for value in cls.sort(key, reverse):
                if filter is None or filter(value):
                    yield value


    class CacheMeta(RegistryMeta):
        """Creates a class-specific cache."""
        
        def __new__(cls, name, bases, dct):
            dct["_cache"] = None
            return super(CacheMeta, cls).__new__(cls, name, bases, dct)
        
        def _iterate_over_rooms(cls, rooms):
            
            if isinstance(rooms, (basestring, NoneType)):
                rooms = (rooms,)
            
            for room_or_tag in rooms:
                if room_or_tag is None or Room.find(room_or_tag) is not None:
                    yield room_or_tag
                else:
                    for room in Room.filter(lambda x: x.has_tag(room_or_tag)):
                        yield room.id
        
        def build_cache_by_room(cls, key=None, reverse=False):
            cls._cache = {}
            for action in cls.all():
                for room in cls._iterate_over_rooms(action.rooms):
                    if room not in cls._cache:
                        cls._cache[room] = [action]
                    else:
                        cls._cache[room].append(action)
            for room, actions in cls._cache.items():
                cls._cache[room] = sorted(actions, key=key, reverse=reverse)


    class CachedRegistry(Registry, metaclass=CacheMeta):
        """
    Extends the registry managed by Registry with a cache to improve
    runtime performance.

    The cache is built after the registry is fully populated.
    """


    class ParentRegistry(object):
        """
    Manages a combined registry of all known instances of subclasses.

    Subclasses are expected to inherit from Registry before inheriting from
    the class that inherits from ParentRegistry.
    """
        
        @classmethod
        def sort_registry(cls, key=None, reverse=False):
            for sub_cls in cls.__subclasses__():
                if issubclass(sub_cls, Registry):
                    sub_cls.sort_registry(key, reverse)
        
        @classmethod
        def find(cls, id):
            for sub_cls in cls.__subclasses__():
                if issubclass(sub_cls, Registry):
                    value = sub_cls.find(id)
                    if value is not None:
                        return value
            return None
        
        @classmethod
        def all(cls):
            """yields all the registry."""
            for sub_cls in cls.__subclasses__():
                if issubclass(sub_cls, Registry):
                    for value in sub_cls.all():
                        yield value
        
        @classmethod
        def filter(cls, function=None):
            """yields a subset of the registry that verify certain conditions."""
            for sub_cls in cls.__subclasses__():
                if issubclass(sub_cls, Registry):
                    for value in sub_cls.filter(function):
                        yield value
        
        @classmethod
        def sort(cls, key=None, reverse=False):
            """returns the sorted values from the registry."""
            values = []
            for sub_cls in cls.__subclasses__():
                if issubclass(sub_cls, Registry):
                    values.extend(sub_cls.all())
            return sorted(values, key=key, reverse=reverse)
        
        @classmethod
        def filtered_sort(cls, filter=None, key=None, reverse=False):
            """sorts a previously filtered subset of the registry."""
            return sorted(cls.filter(filter), key=key, reverse=reverse)
        
        @classmethod
        def sorted_filter(cls, key=None, reverse=False, filter=None):
            """filters the previously sorted registry."""
            for value in cls.sort(key=key, reverse=reverse):
                if filter is None or filter(value):
                    yield value
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
