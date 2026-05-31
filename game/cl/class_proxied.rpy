
init -31 python:




    class Proxied(object):
        def __init__(self, store, local=None):
            if not store:
                raise Error("Proxied didn't receive a store")
            self._store = store
            
            self._local = set(local) if local else {"id"}
            self._local.add("id")
        
        def _add_local(self, entry):
            self._local.add(entry)
        
        def __getattr__(self, attr):
            
            propobj = getattr(self.__class__, attr, None)
            if isinstance(propobj, property):
                return propobj.fget(self)
            try:
                if attr[0] == "_" or attr in self.__dict__["_local"]:
                    return self.__dict__[attr]
                else:
                    return getattr(store, self._store)[attr]
            except KeyError:
                raise AttributeError(attr)
        
        def __getitem__(self, attr):
            return self.__getattr__(attr)
        
        def __setattr__(self, attr, val):
            
            propobj = getattr(self.__class__, attr, None)
            if isinstance(propobj, property):
                propobj.fset(self, val)
            elif attr[0] == "_" or attr in self.__dict__["_local"]:
                var = self.__dict__.get(attr)
                if isinstance(var, Stat):
                    self.__dict__[attr].val = val
                else:
                    self.__dict__[attr] = val
            else:
                tempstore = getattr(store, self._store)
                tempstore[attr] = val
                setattr(store, self._store, tempstore)
        
        def __setitem__(self, attr, val):
            return self.__setattr__(attr, val)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
