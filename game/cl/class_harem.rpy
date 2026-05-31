



init -11 python:



    class Harem(NoRollback, Conditioned):
        
        
        
        
        
        
        
        
        
        @staticmethod
        def find_by_name(harem_name, is_active=True):
            if is_active:
                return (
                HAREMS[harem_name]
                if HAREMS.get(harem_name, None) and HAREMS[harem_name].is_active()
                else None
            )
            else:
                return HAREMS.get(harem_name, None)
        
        @staticmethod
        def find(person, name=None, is_active=True):
            
            
            
            search_key = get_person_id(person)
            if search_key is None:
                return []
            func = Harem.is_active if is_active else Harem.is_member
            return [
            HAREMS[x]
            for x in HAREMS
            if (name is None or name == x) and func(HAREMS[x], search_key)
        ]
        
        @staticmethod
        def together(*people, **kwargs):
            
            
            
            if len(people) < 2:  
                return False
            sets = [set(Harem.find(person, **kwargs)) for person in people]
            return any(set.intersection(*sets))
        
        @staticmethod
        def update_lesbian(person):
            
            person = Person.find(person)
            if person.is_female:
                if any(Harem.find(person.id)):
                    person.lesbian.val = 10
                    person.lesbian.min = 10
                    person.lesbian.max = 10
                else:
                    
                    person.lesbian.min = person.default_attributes["lesbian"]["min"]
                    person.lesbian.max = person.default_attributes["lesbian"]["max"]
            return
        
        def __init__(self, *args, **kwargs):
            if "id" not in kwargs:
                raise Exception("Harem missing id")
            if "members" not in kwargs:
                raise Exception("Harem missing members")
            if any([x for x in kwargs["members"] if x is None]):
                raise Exception("Harem members include None")
            self.id = kwargs.pop("id")
            self.members = [x for x in kwargs["members"] if Person.find(x)]
            self.flag = f"harem_{self.id}"
            self.ending_conditions = kwargs.get("ending_conditions", [])
            super(Harem, self).__init__(
            id=self.id, conditions=self.ending_conditions, **kwargs
        )
        
        @property
        def active_members(self):
            """Returns a list of all Active members"""
            return [x for x in self.members if self.is_active(x)]
        
        @property
        def active_members_objects(self):
            """Returns a list of all Active members"""
            return [
            Person.find(x) for x in self.members if Person.find(x) and self.is_active(x)
        ]
        
        @property
        def active_members_in_room(self):
            """Returns a list of all Active members in game.room"""
            return sorted(
            [x for x in self.active_members if Person.find(x).room == game.room]
        )
        
        def active_members_in_room_tag(self, room_tag):
            """Returns a list of all Active members in game.room"""
            return sorted(
            [
                x
                for x in self.active_members
                if Room.has_tag(Person.find(x).room, room_tag)
            ]
        )
        
        def is_member(self, person):
            return get_person_id(person) in self.members
        
        def destroy(self):
            
            for person in self.members:
                if self.is_active(person):
                    Person.find(person).set_gone_forever()
        
        def join(self, *people):
            
            
            for person in people:
                person = Person.find(person)
                if self.is_member(person.id):
                    person.flags[self.flag] = 1
                    
                    if person.flags.nonexclusive != "harem":
                        person.flags.previous_nonexclusive = person.flags.nonexclusive
                        person.flags.nonexclusive = "harem"
                    
                    Harem.update_lesbian(person.id)
        
        @staticmethod
        def join_by_name(harem_name, *people):
            harem = Harem.find_by_name(harem_name, is_active=False)
            if harem is not None:
                harem.join(*people)
        
        def leave(self, *people):
            
            for person in people:
                person = Person.find(person)
                if self.is_member(person.id):
                    person.flags[self.flag] = 0
                    
                    if person.flags.nonexclusive == "harem":
                        person.flags.nonexclusive = person.flags.previous_nonexclusive
                    
                    Harem.update_lesbian(person.id)
        
        @staticmethod
        def leave_by_name(harem_name, *people):
            harem = Harem.find_by_name(harem_name)
            if harem is not None:
                harem.leave(*people)
        
        def breakup(self, *persons):
            
            
            for person in persons:
                person = Person.find(person)
                if self.is_member(person.id) and person.flags[self.flag] == 1:
                    person.flags[self.flag] = -1
                    
                    if person.flags.nonexclusive == "harem":
                        person.flags.nonexclusive = person.flags.previous_nonexclusive
                    
                    Harem.update_lesbian(person.id)
        
        def apologize(self, *persons):
            
            for person in persons:
                person = Person.find(person)
                if self.is_member(person.id) and person.flags[self.flag] == -1:
                    person.flags[self.flag] = 1
                    
                    
                    
                    
                    if person.flags.nonexclusive:
                        person.flags.previous_nonexclusive = person.flags.nonexclusive
                        person.flags.nonexclusive = "harem"
                    
                    Harem.update_lesbian(person.id)
        
        def is_active(self, person=None):
            
            if person is None:
                return any([Person.find(pid).flags[self.flag] == 1 for pid in self.members])
            
            return self.is_member(person) and Person.find(person).flags[self.flag] == 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
