




init -7 python:



    class Room(Registry, Conditioned):
        @hybridmethod
        def has_tag(cls, id, tag):
            if id is None:
                return False
            room = cls.find(id)
            if room is None:
                return False
            return room.has_tag(tag)
        
        @has_tag.instancemethod
        def has_tag(self, tag):
            return tag in self.tags
        
        def __init__(
        self,
        name,
        seasons=False,
        day_night=False,
        hours=(0, 100),
        money_cost=0,
        display_name=None,
        conditioned_bg=None,
        exits=None,
        linked_rooms=None,
        days="1234567",
        buy=None,
        required_item=None,
        music=None,
        random_music=False,
        valid=True,
        open_seasons=None,
        travel_time=0,
        outfit="casual",
        tags=None,
        itm_class_choice=None,
        inventory=None,
        lively_npc=None,
        ambience=None,
        **kwargs,
    ):
            super(Room, self).__init__(name, default_flags={"hidden": not valid}, **kwargs)
            
            self.open_seasons = [] if open_seasons is None else open_seasons
            self._display_name = display_name
            self.days = days
            self.hours = hours
            self.exits = [] if exits is None else exits
            self.linked_rooms = [] if linked_rooms is None else linked_rooms
            self.buy = [] if buy is None else buy
            self.money_cost = money_cost
            self._travel_time = travel_time
            self.image = True
            self.day_night = day_night
            self.seasons = seasons
            self.required_item = required_item
            self.tooltip = ""
            self.music = music
            self.ambience = ambience
            self.random_music = random_music
            self.present_npcs = []
            self.outfit = outfit
            self.conditioned_bg = conditioned_bg
            self.tags = tags if tags is not None else ()
            self.itm_class_choice = itm_class_choice
            
            self.inventory = (
            {None: inventory} if isinstance(inventory, tuple) else inventory
        )
            self.lively_npc = [] if lively_npc is None else lively_npc
        
        
        
        
        
        
        
        
        @property
        def display_name(self):
            try:
                if not hasattr(self, "_display_name") or self._display_name is None:
                    return self.id.capitalize()
                elif isinstance(self._display_name, basestring):
                    return self._display_name
                elif isinstance(self._display_name, dict):
                    for k, v in self._display_name.items():
                        if safe_eval(k):
                            return v
                else:
                    raise ValueError(
                    f"Room 'display_name' must be a string, a dict or None {self.id}"
                )
            except AttributeError as e:
                raise AttributeError(f"Issue with {self.id}") from e
        
        @property
        def present_girls(self):
            if hasattr(self, "present_npcs"):
                return self.present_npcs
            return []
        
        @present_girls.setter
        def present_girls(self, value):
            self.present_npcs = value
        
        @property
        def bg(self):
            if hasattr(self, "conditioned_bg") and self.conditioned_bg:
                if not isinstance(self.conditioned_bg, dict) and config.developer:
                    raise ValueError(
                    f"Room 'conditioned_bg' must be a dict {self.id} {self.conditioned_bg}"
                )
                for k, v in self.conditioned_bg.items():
                    if safe_eval(k):
                        return v
            return f"bg {self.id}"
        
        def play_music(self):
            if hasattr(self, "music"):
                music = ""
                if isinstance(self.music, list):
                    if self.random_music:
                        renpy.random.shuffle(self.music)
                    for music, condition in self.music:
                        if safe_eval(condition):
                            break
                else:
                    music = self.music
                if not music:
                    renpy.music.stop(fadeout=2)
                if not (renpy.music.get_playing() == music):
                    renpy.music.play(music, loop=True, fadein=2)
            else:
                renpy.music.stop(fadeout=2)
            if hasattr(self, "ambience"):
                if not self.ambience:
                    renpy.music.stop("ambience", fadeout=2)
                if not (renpy.music.get_playing("ambience") == self.ambience):
                    renpy.music.play(self.ambience, "ambience", loop=True, fadein=2)
            else:
                renpy.music.stop("ambience", fadeout=2)
        
        def stop_sounds_on_channels(self):
            for channel in renpy.audio.audio.channels:
                if renpy.music.is_playing(channel):
                    renpy.music.stop(channel)
        
        def get_tooltip(self):
            tt = []
            if self.money_cost and not (
            game.flags.paidrooms and self.id in game.flags.paidrooms
        ):
                tt.append(f"{{image=gui/icons/icon_money.png}}-{self.money_cost}")
            if self.travel_time:
                tt.append(f"{{image=gui/icons/icon_clock.png}}+{self.travel_time}h")
            if self.tooltip:
                tt = [self.tooltip] + tt
            return tt
        
        def get_present_girls(self, valid=True, girls=None):
            return self.get_present_npcs(valid=valid, npcs=girls)
        
        def get_present_girls_ids(self, valid=True, girls=None):
            return self.get_present_npcs_ids(valid=valid, npcs=girls)
        
        def get_present_girls_by_tag(self, valid=True, girls=None):
            return self.get_present_npcs_by_tag(valid=valid, npcs=girls)
        
        def get_present_girls_ids_by_tag(self, valid=True, girls=None):
            return self.get_present_npcs_ids_by_tag(valid=valid, npcs=girls)
        
        def get_present_npcs(self, valid=True, npcs=None):
            
            if not self.test():
                return []
            if npcs:
                return [Person.find(nid) for nid in npcs]
            result = set()
            for npc in Person.all_people(ignore_hidden=False):
                floc = npc.flags.forceLocation
                if floc != 0 and floc == (game.days_played, game.hour, self.id):
                    if floc[-1] != npc.room:
                        npc.set_room(floc[-1])
                    result.add(npc)
                elif hasattr(self, "present_npcs") and (
                (npc in self.present_npcs and valid and not npc.hidden)
                or (npc in self.present_npcs and not valid)
            ):
                    result.add(npc)
            return list(result)
        
        def get_present_npcs_ids(self, valid=True, npcs=None):
            return sorted([npc.id for npc in self.get_present_npcs(valid, npcs)])
        
        def get_present_npcs_by_tag(self, valid=True, npcs=None):
            result = self.get_present_npcs(valid=valid, npcs=npcs)
            if self.tags:
                
                for room in self.filter(lambda x: set(self.tags) & set(x.tags)):
                    result += room.get_present_npcs(valid)
            return list(set(result))
        
        def get_present_npcs_ids_by_tag(self, valid=True, npcs=None):
            return [npc.id for npc in self.get_present_npcs_by_tag(valid, npcs)]
        
        def test(self, debug=False):
            return not self.hidden and super().test(debug)
        
        def get_exits(self):
            
            return list(Room.filter(lambda x: x.id in self.exits and x.test())) + [self]
        
        @property
        def travel_time(self):
            game_room_object = Room.find(game.room)
            if hero.has_motor_vehicle:
                return 0
            elif game.room == self.id:
                return 0
            elif game.room in self.linked_rooms:
                return 0
            elif self.id in game_room_object.linked_rooms:
                return 0
            else:
                return max(game_room_object._travel_time, self._travel_time)
        
        def travel_to(self):
            travel_time = self.travel_time
            if travel_time:
                game.pass_time(travel_time, True)
        
        def pay_entrance(self):
            if (
            self.money_cost
            and (self.id not in (game.flags.paidrooms or []))
            and (self.id not in [game.flags.job_day, game.flags.job_night])
        ):
                hero.money -= self.money_cost
                game.set_flag("paidrooms", [self.id], 1, mod="+")
        
        def get_upset_girls(self, present_girls=None):
            return self.get_upset_npcs(present_npcs=present_girls)
        
        def get_upset_npcs(self, present_npcs=None):
            if not present_npcs:
                present_npcs = self.get_present_npcs()
            return [npc for npc in present_npcs if npc.is_upset]
        
        def _filter_items(self, items):
            for item in items:
                if isinstance(item, basestring):
                    yield item, None
                elif isinstance(item, dict):
                    if "conditions" in item and not all(
                    safe_eval(x) for x in item["conditions"]
                ):
                        continue
                    if "items" in item:
                        for subitem, price in self._filter_items(item["items"]):
                            yield subitem, price
                    elif "id" in item:
                        yield item["id"], item["price"] if "price" in item else None
                    elif config.developer:
                        raise ValueError(f"Malformed shop element {item}")
                elif config.developer:
                    raise ValueError(f"Malformed shop element {item}")
        
        def _replaced_items_discount(self, item_id):
            bought_item = ItemBase.find(item_id)
            replaced_items = [
            ItemBase.find(itm)
            for itm in bought_item.replace_items
            if itm in hero.inventory
        ]
            if not replaced_items:
                return bought_item.price
            elif len(replaced_items) == 1:
                discount = int(ceil(replaced_items[0].price * 0.1))
                old_items = f"{replaced_items[0].display_name}"
            else:
                discount = int(
                ceil(
                    sum([replaced_item.price * 0.1 for replaced_item in replaced_items])
                )
            )
                old_items = f"{', '.join([replaced_item.display_name for replaced_item in replaced_items[:-1]])} and {replaced_items[-1].display_name}".lower()
            renpy.say(
            "",
            f"The {self.display_name.lower()} will buy my old {old_items} for {discount}$.",
        )
            renpy.say(
            "",
            f"My new {bought_item.display_name.lower()} will only cost {bought_item.price - discount}",
        )
            return bought_item.price - discount
        
        def shop(self, clerk=None, discount=0):
            """
        Opens the shopping screen with the adequate items.

        If a clerk is provided, it should be a string that will be passed
        to the shopping screen to add the corresponding sprite.
        If a discount is provided, that percentage will discount the price of the items.
        """
            
            if self.inventory is None:
                if config.developer:
                    raise Exception(f"Trying to buy items in '{self.display_name}'")
                return
            
            if self.itm_class_choice:
                itm_class = renpy.call_screen("select", self.itm_class_choice)
                
                if itm_class == "None":
                    return
            
            section_items = dict.fromkeys(list(self.inventory.keys()), None)
            for s in section_items.keys():
                for item_id, price in self._filter_items(self.inventory[s]):
                    item = ItemBase.find(item_id)
                    
                    if item is None:
                        continue
                    
                    if not item.buyable:
                        continue
                    
                    if item_id in hero.sold_back_items:
                        continue
                    
                    if self.itm_class_choice and not isinstance(item, itm_class):
                        continue
                    
                    price = price if price is not None else item.price
                    price = int(price * (100.0 - discount) / 100)
                    
                    if section_items[s] is None:
                        section_items[s] = []
                    section_items[s].append(
                    (item.display_name, item.id, price, item.get_tooltip())
                )
            
            section_items = {k: v for k, v in section_items.items() if v}
            
            if len(section_items.keys()) == 1:
                section = list(section_items.keys())[0]
            elif len(section_items.keys()) > 1:
                section = renpy.call_screen("select", list(section_items.keys()))
                
                if section == "None":
                    return
            else:
                section = "empty"
            
            while True:
                
                if section == "empty" or not len(section_items[section]):
                    renpy.say("", "There is nothing for me here.")
                    break
                
                result = renpy.call_screen("shopping", section_items[section], clerk)
                
                if result == "exit":
                    break
                item_id, price = result
                if ItemBase.find(item_id).replace_items:
                    price = self._replaced_items_discount(item_id)
                
                if hero.money < price:
                    renpy.say("", "I don't have enough money.")
                    continue
                
                hero.money -= price
                hero.gain_item(item_id)
                if ItemBase.find(item_id).replace_items:
                    for old_item in ItemBase.find(item_id).replace_items:
                        if old_item in hero.inventory:
                            hero.lose_item(old_item)
                            hero.sold_back_items.add(old_item)
                
                section_items[section] = []
                for item_id, price in self._filter_items(self.inventory[section]):
                    item = ItemBase.find(item_id)
                    
                    if item is None:
                        continue
                    
                    if not item.buyable:
                        continue
                    
                    if item_id in hero.sold_back_items:
                        continue
                    
                    if self.itm_class_choice and not isinstance(item, itm_class):
                        continue
                    
                    price = price if price is not None else item.price
                    price = int(price * (100.0 - discount) / 100)
                    
                    section_items[section].append(
                    (item.display_name, item.id, price, item.get_tooltip())
                )
                
                if not any(section_items.values()):
                    renpy.say("", "I bought everything here.")
                    break
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
