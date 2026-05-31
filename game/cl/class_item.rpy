





init -10 python:



    class ItemBase(ParentRegistry, Flagged):
        def __init__(
        self,
        name,
        display_name=None,
        one_only=False,
        tooltip="",
        price=0,
        replace_items=None,
        **kwargs,
    ):
            super(ItemBase, self).__init__(name, **kwargs)
            
            self.name = name
            self.display_name = _(
            display_name
            if display_name is not None
            else name.replace("_", " ").capitalize()
        )
            self.one_only = one_only
            self.tooltip = tooltip
            self.price = price
            self.replace_items = replace_items if replace_items else []
        
        @staticmethod
        def get_sub_tooltip(icon, value):
            
            if value == 0:
                raise ValueError("value must not be 0")
            return "{{image={}}} {:+}".format(icon, value)
        
        def get_tooltip(self, in_inventory=False):
            if not self.tooltip:
                return []
            return [self.tooltip]
        
        @property
        def buyable(self):
            return not self.one_only or self.name not in hero.inventory


    class Item(Registry, ItemBase):
        def __init__(
        self,
        name,
        
        one_only=True,
        **kwargs,
    ):
            
            kwargs["one_only"] = one_only
            super(Item, self).__init__(name, **kwargs)
        
        @property
        def icon(self):
            return "📦"


    class Gift(Registry, ItemBase):
        def __init__(
        self,
        name,
        love_bonus=0,
        sub_bonus=0,
        les_bonus=0,
        purity_bonus=0,
        tags=None,
        label=None,
        once=False,
        bonus_traits=None,
        
        tooltip="Gift",
        **kwargs,
    ):
            if bonus_traits is None:
                bonus_traits = []
            
            kwargs["tooltip"] = tooltip
            super(Gift, self).__init__(name, **kwargs)
            
            self.love_bonus = love_bonus
            self.sub_bonus = sub_bonus
            self.les_bonus = les_bonus
            self.purity_bonus = purity_bonus
            self.tags = tags if tags is not None else ()
            self.label = label
            self.once = once
            self.bonus_traits = bonus_traits
        
        @property
        def icon(self):
            return "🎁"
        
        def get_tooltip(self, in_inventory=False):
            tt = super(Gift, self).get_tooltip()
            if tt:
                tt.append("\n")
            effects_list = []  
            
            for bonus in ["love", "sub", "les", "purity"]:
                value = getattr(self, f"{bonus}_bonus", 0)
                if value == 0:
                    continue
                
                icon_filename = "gui/icons/icon_{}.png".format(
                bonus
                if bonus not in ["les", "purity"]
                else "lesbian"
                if bonus == "les"
                else "good"
                if bonus == "purity"
                else bonus
            )
                effects_list.append(self.get_sub_tooltip(icon_filename, value))
            tt.append("\n".join(effects_list))
            return tt
        
        def use(self, npc):
            if GALLERY_MODE:
                return
            
            love_gain = self.love_bonus
            if len(self.bonus_traits) != 0:
                for trait in npc.traits:
                    if trait in self.bonus_traits:
                        if love_gain > 0:
                            love_gain *= 1.5
                        else:
                            love_gain += 1
                    elif f"not_{trait}" in self.bonus_traits:
                        if love_gain < 0:
                            love_gain *= 1.5
                        else:
                            love_gain -= 1
            for factor in npc.desire_factors:
                if factor in self.tags or factor == self.name:
                    if love_gain > 0:
                        love_gain *= 1.5
                    else:
                        love_gain += 1
                elif (
                factor.replace("not_", "") in self.tags
                or factor.replace("not_", "") == self.name
            ):
                    if love_gain > 0:
                        love_gain = 0
                    elif love_gain < 0:
                        love_gain *= 1.5
                    else:
                        love_gain -= 1
            if game.calendar.is_today(*npc.birthday):
                love_gain *= 1.5
            love_gain -= npc.flags[f"gift{self.name}"]
            
            self._restricted_stat_change(npc, "love", love_gain)
            self._restricted_stat_change(npc, "sub", self.sub_bonus)
            self._restricted_stat_change(npc, "lesbian", self.les_bonus)
            self._restricted_stat_change(npc, "purity", self.purity_bonus)
            
            hero.lose_item(self.id)
            if self.once:
                npc.flags[f"gift{self.name}"] = True
            else:
                npc.flags[f"gift{self.name}"] = TemporaryFlag(
                npc.flags[f"gift{self.name}"] + 1, 7
            )
            if love_gain > 0:
                return True
            elif love_gain == 0:
                return "neutral"
            else:
                return False
        
        @staticmethod
        def _restricted_stat_change(person, stat, value):
            
            if not hasattr(person, stat):
                return
            getattr(person, stat).update(value)


    class Equip(Registry, ItemBase, Conditioned):
        def __init__(
        self,
        name,
        type="clothes",
        gender=None,
        effects=None,
        
        one_only=True,
        **kwargs,
    ):
            
            kwargs["one_only"] = one_only
            super(Equip, self).__init__(name, **kwargs)
            
            self.type = type
            self.gender = gender
            self.effects = effects if effects else {}
        
        @property
        def icon(self):
            if self.type == "clothes":
                return "👔"
            elif self.type == "accessory":
                return "👟"
            else:
                return "❌"
        
        def get_tooltip(self, in_inventory=False):
            tt = super(Equip, self).get_tooltip()
            if tt:
                tt.append("\n")
            tt.append(f"{self.type.capitalize()}: ")
            effects_list = []  
            
            for effect, value in self.effects.items():
                if value == 0:
                    continue
                if effect in [
                "energy",
                "hunger",
                "grooming",
                "fun",
                "knowledge",
                "fitness",
                "charm",
            ]:
                    if effect in ["charm", "fitness", "knowledge"]:
                        value *= game.get_difficulty_mod(value)
                    effects_list.append(
                    self.get_sub_tooltip(
                        f"gui/icons/icon_{effect}.png",
                        int(value),
                    )
                )
            tt.append("\n".join(effects_list))
            return tt
        
        @property
        def buyable(self):
            return super(Equip, self).buyable and (
            self.gender is None or self.gender == hero.gender
        )
        
        def equip(self):
            if hero.equipment[self.type] == self:
                self._unequip()
            else:
                if hero.equipment[self.type] is not None:
                    hero.equipment[self.type]._unequip()
                self._equip()
        
        def unequip(self):
            if hero.equipment[self.type] == self:
                self._unequip()
        
        
        
        def _equip(self):
            hero.equipment[self.type] = self
            for e, val in self.effects.items():
                if e in ["fitness", "charm", "knowledge"]:
                    if val < 0:
                        hero[e].update(val, False)
                        hero[e].max += val
                    else:
                        hero[e].max += val
                        hero[e].update(val, False)
        
        def _unequip(self):
            hero.equipment[self.type] = None
            for e, val in self.effects.items():
                if e in ["fitness", "charm", "knowledge"]:
                    if val < 0:
                        hero[e].max -= val
                        hero[e].update(-val, False)
                    else:
                        hero[e].update(-val, False)
                        hero[e].max -= val


    class Consumable(Registry, ItemBase, Conditioned):
        def __init__(
        self,
        name,
        effects=None,
        money_gain=(),
        label=None,
        frequency_limit=None,
        uses=1,
        say=None,
        inventory_usable=True,
        **kwargs,
    ):
            super(Consumable, self).__init__(name, **kwargs)
            
            if say is None:
                say = []
            self.effects = effects if effects else []
            self.money_gain = money_gain
            self.label = label
            self.frequency_limit = frequency_limit
            self.uses = uses
            self.say = say
            self.inventory_usable = inventory_usable
        
        @property
        def icon(self):
            return "🫙"
        
        def get_tooltip(self, in_inventory=False):
            tt = super(Consumable, self).get_tooltip()
            if tt:
                tt.append("\n")
            effects_list = []  
            
            for effect, value in self.effects:
                if value == 0:
                    continue
                if effect in [
                "energy",
                "hunger",
                "grooming",
                "fun",
                "charm",
                "fitness",
                "knowledge",
            ]:
                    if effect in ["charm", "fitness", "knowledge"]:
                        value *= game.get_difficulty_mod(value)
                    effects_list.append(
                    self.get_sub_tooltip(f"gui/icons/icon_{effect}.png", int(value))
                )
                elif effect == "time":
                    effects_list.append(
                    "{{image=gui/icons/icon_clock.png}} +{} h".format(value)
                )
            if self.uses:
                if self.uses == 1:
                    effects_list.append("1 use")
                else:
                    effects_list.append(
                    "{} uses".format(
                        hero.inventory[self.name] if in_inventory else self.uses
                    )
                )
            tt.append("\n".join(effects_list))
            return tt
        
        def test(self, debug=False):
            if self.frequency_limit is not None and f"{self.name}_last_used" in hero.flags:
                if debug:
                    renpy.log("Test Failed: frequency limit")
                return False
            
            return super(Consumable, self).test(debug)
        
        def use(self):
            if self.inventory_usable:
                if GALLERY_MODE:
                    return
                
                if self.label:
                    if isinstance(self.label, tuple):
                        renpy.call_in_new_context(*self.label)
                    elif isinstance(self.label, basestring):
                        renpy.call_in_new_context(self.label)
                
                for effect, value in self.effects:
                    if effect in [
                    "fitness",
                    "knowledge",
                    "charm",
                    "fun",
                    "hunger",
                    "energy",
                    "grooming",
                ]:
                        hero[effect] += value
                    elif effect == "time":
                        game.pass_time(value, needs=True)
                    elif effect in ["siscon"]:
                        minami.siscon += value
                hero.lose_item(self.id)
                
                if self.name.endswith("_tea"):
                    game.flags.tea_drank.add(self.name)
                    if (
                    len(game.flags.tea_drank) >= 29
                    and renpy.has_label("tea_achievement_1")
                    and not game.flags.cheat
                ):
                        renpy.call("tea_achievement_1")
                elif self.name in ["coffee", "cappuccino", "moka"]:
                    game.flags.coffee_drank += 1
                
                if self.frequency_limit:
                    game.flags[f"{self.name}_last_used"] = TemporaryFlag(
                    True, self.frequency_limit
                )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
