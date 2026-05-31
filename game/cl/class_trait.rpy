
init -17 python:



    class TraitsShortcut(python_object):
        __slots__ = "__dict__", "_person", "_defaults"
        
        def __init__(self, person, default_traits=()):
            self._person = person
            
            self._defaults = frozenset(default_traits)
        
        def _apply_deltas(self, target, add=True, remove=True):
            """mutates target with the deltas stored in the flag."""
            
            if "traits" not in self._person.flags:
                return
            
            for delta in self._person.flags.traits:
                if delta.startswith("-"):
                    if remove:
                        target.discard(delta[1:])
                elif delta.startswith("+"):
                    if add:
                        target.add(delta[1:])
                else:
                    if add:
                        target.add(delta)
        
        @property
        def _traits(self):
            
            traits = set(self._defaults)
            self._apply_deltas(traits)
            return traits
        
        @property
        def known(self):
            
            known_traits = set()
            if "knowntraits" in self._person.flags:
                known_traits = set(self._person.flags.knowntraits)
            
            
            self._apply_deltas(known_traits)
            return known_traits
        
        def __iadd__(self, trait):
            
            if trait in self._traits:
                return
            if "traits" not in self._person.flags:
                
                traits = {"+{}".format(trait)}
            else:
                traits = set(self._person.flags.traits)
                
                if trait in self._defaults:
                    traits.discard("-{}".format(trait))
                else:
                    traits.add("+{}".format(trait))
            self._person.flags.traits = traits
            return self
        
        def __isub__(self, trait):
            
            if trait not in self._traits:
                return
            if "traits" not in self._person.flags:
                
                traits = {"-{}".format(trait)}
            else:
                traits = set(self._person.flags.traits)
                
                if trait not in self._defaults:
                    traits.discard("+{}".format(trait))
                else:
                    traits.add("-{}".format(trait))
            self._person.flags.traits = traits
            return self
        
        def discover(self):
            
            known_traits = set()
            if "knowntraits" in self._person.flags:
                known_traits = set(self._person.flags.knowntraits)
            
            step = self._person.love.scale // len(self._defaults)
            should_know = self._person.love // step
            
            if len(known_traits) >= should_know:
                return
            
            while len(known_traits) < should_know and set(self._defaults - known_traits):
                known_traits.add(set(self._defaults - known_traits).pop())
            self._person.flags.knowntraits = known_traits
        
        @property
        def all_known(self):
            
            known_traits = set()
            if "knowntraits" in self._person.flags:
                known_traits = set(self._person.flags.knowntraits)
            return len(self._defaults - known_traits) == 0
        
        def discover_all(self):
            self._person.flags.knowntraits = set(self._defaults)
        
        
        
        def __len__(self):
            return len(self._traits)
        
        def __contains__(self, trait):
            return trait in self._traits
        
        def __eq__(self, other):
            return self._traits == other
        
        def __ne__(self, other):
            return self._traits != other
        
        def __le__(self, other):
            return self._traits <= other
        
        def __lt__(self, other):
            return self._traits < other
        
        def __ge__(self, other):
            return self._traits >= other
        
        def __gt__(self, other):
            return self._traits > other
        
        def __or__(self, other):
            return self._traits | other
        
        def __ror__(self, other):
            return other | self._traits
        
        def __and__(self, other):
            return self._traits & other
        
        def __rand__(self, other):
            return other & self._traits
        
        def __sub__(self, other):
            return self._traits - other
        
        def __rsub__(self, other):
            return other - self._traits
        
        def __xor__(self, other):
            return self._traits ^ other
        
        def __rxor__(self, other):
            return other ^ self._traits
        
        def __iter__(self):
            for trait in self._traits:
                yield trait
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
