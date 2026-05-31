
init -30 python:



    class Countered:
        def get_counters(self, counter=None):
            if self.id not in COUNTERS:
                COUNTERS[self.id] = {}
            
            if counter:
                return COUNTERS[self.id].get(counter, 0)
            else:
                return COUNTERS[self.id]
        
        def get_counter(self, counter):
            return self.get_counters(counter)
        
        def set_counter(self, counter, value=0):
            if self.id not in COUNTERS:
                COUNTERS[self.id] = {}
            
            if value is None:
                COUNTERS[self.id].pop(counter, None)
            else:
                
                
                COUNTERS[self.id][counter] = int(value)
        
        def increment_counters(self):
            counters = self.get_counters()
            for counter, value in counters.items():
                self.set_counter(counter, value + 1)


    class CountersShortcut(Countered):
        def __init__(self, id):
            self.__dict__["id"] = id
        
        def __getattr__(self, attr):
            if attr[0] == "_" or attr == "id":
                try:
                    return self.__dict__[attr]
                except KeyError:
                    raise AttributeError(attr)
            return self.get_counter(attr)
        
        def __setattr__(self, attr, val):
            if attr[0] == "_" or attr == "id":
                self.__dict__[attr] = val
            else:
                self.set_counter(attr, val)
        
        
        def __getitem__(self, attr):
            return self.__getattr__(attr)
        
        def __setitem__(self, attr, val):
            self.__setattr__(attr, val)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
