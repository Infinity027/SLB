
init -20 python:



    class Movie(NoRollback):
        __slots__ = "_id", "_description", "_traits", "_cinema"
        
        @staticmethod
        def find(genre):
            
            if genre in MOVIES:
                return MOVIES[genre]
            return None
        
        @staticmethod
        def all_movies():
            
            return MOVIES.values()
        
        def __init__(self, id, description=None, traits=None, cinema=False):
            self._id = id
            self._description = description if description is not None else id.capitalize()
            self._traits = traits if traits is not None else {}
            self._cinema = cinema
        
        def __getitem__(self, item):
            return self._traits[item]
        
        def __contains__(self, item):
            return item in self._traits
        
        @property
        def id(self):
            return self._id
        
        @property
        def description(self):
            return self._description
        
        @property
        def cinema(self):
            return self._cinema
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
