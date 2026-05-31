
init -16 python:



    class Piercing:
        def __init__(self, id, location, pierced=False, outfits=None, expressions=None):
            self.id = id
            self.location = location
            self.default = pierced
            self.outfits = outfits if outfits is not None else ["all"]
            self.expressions = expressions if expressions is not None else ["all"]
        
        @property
        def pierced(self):
            if hasattr(store, self.id):
                return getattr(store, self.id)
            return self.default
        
        @pierced.setter
        def pierced(self, value):
            setattr(store, self.id, value)
        
        @property
        def worn(self):
            if hasattr(store, f"{self.id}_worn"):
                return getattr(store, f"{self.id}_worn")
            return self.pierced
        
        @worn.setter
        def worn(self, value):
            setattr(store, f"{self.id}_worn", value)


    class NoPiercing:
        
        
        
        def __init__(self):
            pass
        
        def __getattr__(self, attr):
            if attr == "id":
                return None
            if attr in ["default", "pierced", "worn"]:
                return False
            if attr in ["outfits", "expressions"]:
                return ["all"]
            raise AttributeError(attr)
        
        def __setattr__(self, attr, val):
            pass


    class Piercings:
        all_piercings = {
        "ears": 50,
        "nose": 50,
        "navel": 100,
        "tongue": 200,
        "lips": 300,
        "eyebrow": 400,
        "nipples": 500,
        "clit": 600,
        "dick": 600,
    }
        
        _DEFAULT_NONE = NoPiercing()
        
        def __init__(self, id, defaults):
            for name, values in defaults.items():
                self[name] = Piercing(f"{id}_piercings_{name}", name, **values)
        
        def __len__(self):
            """Returns how many piercings are pierced."""
            return len([None for p in self.__dict__.values() if p.pierced])
        
        def __contains__(self, key):
            return key in self.__dict__
        
        def __getitem__(self, key):
            if not isinstance(key, basestring):
                raise TypeError("piercing ids must be strings, not {}".format(type(key)))
            
            if key in self.__dict__:
                return self.__dict__[key]
            if key in self.all_piercings:
                return self._DEFAULT_NONE
            
            raise KeyError(key)
        
        def __setitem__(self, key, value):
            if not isinstance(key, basestring):
                raise TypeError("piercing ids must be strings, not {}".format(type(key)))
            if key not in self.all_piercings:
                raise KeyError(key)
            
            if isinstance(value, Piercing):
                self.__dict__[key] = value
            elif isinstance(value, bool):
                
                self[key].pierced = value
            else:
                raise TypeError("piercings expect a Piercing or a bool")
        
        def __getattr__(self, attr):
            try:
                return self[attr]
            except KeyError:
                raise AttributeError(attr)
        
        def __setattr__(self, attr, value):
            try:
                self[attr] = value
            except KeyError:
                raise AttributeError(attr)
        
        def items(self):
            return self.__dict__.items()
        
        def filter(self, function):
            for name, piercing in sorted(
            self.items(), key=lambda x: Piercings.all_piercings[x[0]]
        ):
                if function(piercing):
                    yield name, piercing
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
