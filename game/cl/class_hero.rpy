












init -11 python:



    class Hero(Countered, Flagged, Proxied, object):
        def __init__(self):
            Proxied.__init__(
            self,
            "DATA_HERO",
            
            [
                
                "energy",
                "grooming",
                "hunger",
                "fun",
                
                "fitness",
                "knowledge",
                "charm",
                "morality",
                
                "money",
                "luck",
                
                "skills",
                
                "say",
                "counters",
                "outfits",
                "sold_back_items",
                "pregnancy_congratulations",
            ],
        )
            Flagged.__init__(self, "HERO!")
            self.skills = SkillsManager()
            self.energy = Need(
            "hero_energy",
            name="Energy",
            decay_value=0.5,
            icon="gui/icons/icon_energy.png",
        )
            self.grooming = Need(
            "hero_grooming",
            name="Grooming",
            decay_value=0.4,
            icon="gui/icons/icon_grooming.png",
        )
            self.hunger = Need(
            "hero_hunger",
            name="Hunger",
            decay_value=0.8,
            icon="gui/icons/icon_hunger.png",
        )
            self.fun = Need(
            "hero_fun", name="Fun", decay_value=0.3, icon="gui/icons/icon_fun.png"
        )
            self.money = Money("hero_money")
            self.fitness = Attribute(
            "hero_fitness",
            name="Fitness",
            icon="gui/icons/icon_fitness.png",
            up_hook={20: "hero.energy.update_max(hero.fitness)"},
        )
            self.knowledge = Attribute(
            "hero_knowledge",
            name="Knowledge",
            icon="gui/icons/icon_knowledge.png",
            up_hook={
                10: self.gain_talk_subject,
                20: "hero.fun.update_max(hero.knowledge)",
            },
        )
            self.charm = Attribute(
            "hero_charm",
            name="Charm",
            icon="gui/icons/icon_charm.png",
            up_hook={20: "hero.grooming.update_max(hero.charm)"},
        )
            self.morality = Attribute(
            "hero_morality",
            name="Morality",
            min=-100,
            icon="gui/icons/icon_good.png",
            negative_icon="gui/icons/icon_bad.png",
        )
            self.luck = Stat("hero_luck", name="Luck", min=-1, max=1)
            self.counters = CountersShortcut(self.id)
            self.outfits = None
            self.sold_back_items = set()
            self.pregnancy_congratulations = set()
        
        @property
        def is_lucky(self):
            return self.luck.is_max
        
        @property
        def is_unlucky(self):
            return self.luck.is_min
        
        @property
        def birthday_display_name(self):
            if isinstance(self.birthday, int) and self.birthday == 0:
                return "Unknown"
            else:
                season, birthday = self.birthday
                if birthday % 10 == 1:
                    ext = "st"
                elif birthday % 10 == 2:
                    ext = "nd"
                else:
                    ext = "th"
                return season.capitalize() + " " + str(birthday) + ext
        
        def __getattr__(self, attr):
            try:
                return Proxied.__getattr__(self, attr)
            except AttributeError as e:
                if attr == "activity":
                    return ""
                raise e
        
        @property
        def stamina(self):
            if self.flags.last_sex and not self.flags.god_mode:
                threshold = 120
                if self.has_skill("high_libido"):
                    threshold = 90
                if self.has_skill("low_libido"):
                    threshold = 240
                threshold += self.flags.bluepills
                threshold -= self.fitness + self.sexperience * 0.5
                return threshold <= 24 * (game.days_played - self.flags.last_sex[1]) + (
                game.hour - self.flags.last_sex[0]
            )
            return True
        
        @property
        def children(self):
            babies = 0
            for g in Person.all_people(ignore_hidden=False):
                babies += g.flags.mikeBabies
            return babies
        
        def get_needs(self):
            for value in self.__dict__.values():
                if isinstance(value, Need):
                    yield value
        
        def get_attributes(self):
            for value in self.__dict__.values():
                if isinstance(value, Attribute):
                    
                    if self.is_male and value.name == "Morality":
                        continue
                    yield value
        
        @property
        def name(self):
            """
        Evaluates conditions and returns the associated hero's nickname according to the current speaker.
        """
            current_speaker = renpy.last_say().who
            if current_speaker and hasattr(current_speaker, "name"):
                current_speaker = current_speaker.name.lower().replace("_name", "")
                return get_hero_nickname(current_speaker)
            return heroname
        
        def initialize(self, name, family_name, gender, money, day, month, start_plus):
            
            self.id = "HERO!"
            self.family_name = family_name.title()
            self.mc_gender = gender
            if day == "random":
                day = randint(1, 31)
            if month == "random":
                month = randchoice(SEASONS)
            self.birthday = [month, day]
            self.money.val = money
            
            
            if gender == "male":
                store.mike_name = heroname
                hero_file = "ch/mike/person/mike.yml"
                persistent.last_mc_male_name = (name, family_name)
                if persistent.last_mc_female_name and isinstance(
                persistent.last_mc_female_name, tuple
            ):
                    store.bree_name = persistent.last_mc_female_name[0]
            else:
                store.bree_name = heroname
                persistent.last_mc_female_name = (name, family_name)
                hero_file = "ch/bree/person/bree.yml"
                if persistent.last_mc_male_name and isinstance(
                persistent.last_mc_male_name, tuple
            ):
                    store.mike_name = persistent.last_mc_male_name[0]
            
            with renpy.file(hero_file) as stream:
                hero_yaml = yaml.load(stream, OrderedLoader)
            
            self.piercings = Piercings(
            "hero", hero_yaml["piercings"] if "piercings" in hero_yaml else {}
        )
            
            for b_girl in Person.all():
                if b_girl.get_flag("birthdayknown_" + gender):
                    b_girl.flags.birthdayknown = True
            
            if start_plus:
                if persistent.talk_subjects:
                    for talk_subject in self.talk_subjects:
                        if talk_subject.name in persistent.talk_subjects:
                            talk_subject.known = True
                
                if persistent.knowledge:
                    self.knowledge = persistent.knowledge
                    self.fun.update_max(self.knowledge)
                    if not any([i for i in self.talk_subjects if i.known]):
                        self.gain_talk_subject()
                else:
                    self.gain_talk_subject(rng=True)
                
                if persistent.money:
                    self.money += persistent.money
                if persistent.charm:
                    self.charm += persistent.charm
                    self.grooming.update_max(self.charm)
                if persistent.fitness:
                    self.fitness += persistent.fitness
                    self.energy.update_max(self.fitness)
                if persistent.sexperience:
                    self.flags.base_sexperience += persistent.sexperience
                if persistent.skills:
                    for k, v in persistent.skills.items():
                        if k in YAML_SKILLS and YAML_SKILLS.get(k).transferable is True:
                            self.skills[k].value = v
                            if YAML_SKILLS[k].gain_effects and self.has_skill(k):
                                for effect in YAML_SKILLS[k].gain_effects:
                                    exec(effect)
            else:
                self.gain_talk_subject(rng=True)
        
        @property
        def is_female(self):
            
            return bool(game.flags.female)
        
        @property
        def is_male(self):
            
            return not self.is_female
        
        @property
        def gender(self):
            if self.is_female:
                return "female"
            return "male"
        
        def layered_image(self):
            if self.is_female:
                return "breemc"
            return "mikemc"
        
        @property
        def bedroom(self):
            if self.is_female:
                return "bedroom4"
            return "bedroom1"
        
        @property
        def talk_subjects_valid(self):
            return [
            subject
            for subject in self.talk_subjects
            if subject.known and subject.test()
        ]
        
        @property
        def talk_subjects_known(self):
            return [subject for subject in self.talk_subjects if subject.known]
        
        @property
        def talk_subjects_unknown(self):
            return [subject for subject in self.talk_subjects if not subject.known]
        
        def gain_talk_subject(self, rng=False):
            if self.talk_subjects_unknown:
                while (
                len(self.talk_subjects_known) - 2 <= self.knowledge // 10
            ) and self.talk_subjects_unknown:
                    if rng:
                        subject = randchoice(self.talk_subjects_unknown)
                    else:
                        subject = renpy.invoke_in_new_context(self._m1_class_hero__gain_talk_subject)
                    subject.known = True
        
        def _m1_class_hero__gain_talk_subject(self):
            hide_cheats = renpy.get_screen("cheats")
            if hide_cheats:
                renpy.hide_screen("cheats")
            try:
                talk_subjects = [
                (subject.display_name, subject)
                for subject in self.talk_subjects_unknown
            ]
                return renpy.call_screen(
                "select", talk_subjects, "Choose a new talk subject", cancel=None
            )
            finally:
                if hide_cheats:
                    renpy.show_screen("cheats")
        
        @staticmethod
        def get_room():
            return game.room
        
        def get_clothes(self, clothes=None, variant=False):
            if not clothes:
                if self.on_date:
                    if game.active_date.clothes:
                        clothes = game.active_date.clothes
                    else:
                        clothes = "casual"
                elif game.room and Room.find(game.room).outfit:
                    clothes = Room.find(game.room).outfit
                    if variant:
                        if self.has_item(f"slutty_{clothes}_equip"):
                            if ItemBase.find("slutty_{clothes}_equip").test():
                                clothes = f"slutty{clothes}"
                        elif self.has_item("sexy_{clothes}_equip"):
                            if ItemBase.find("sexy_{clothes}_equip").test():
                                clothes = f"sexy{clothes}"
                else:
                    clothes = "casual"
            return clothes
        
        @property
        def fertility_modifier(self):
            if self.is_female:
                return (
                0
                if (self.has_skill("barren") or self.flags.pill)
                else 0.5
                if self.has_skill("low_fertility")
                else 1.5
                if self.has_skill("fertile")
                else 1
            )
            else:
                return (
                0.5
                if self.has_skill("smalldick")
                else 1.5
                if self.has_skill("hung")
                else 1
            )
        
        @property
        def fertility(self):
            if self.is_female:
                return int(
                max(
                    abs((game.days_played + self.birthday[1]) % 28 - 13) / 14.0 * 100
                    - 50,
                    0,
                )
                * self.fertility_modifier
            )
            else:
                return 100
        
        @staticmethod
        def impregnate(force=False):
            return False
        
        @property
        def pregnant(self):
            if self.is_female:
                return self.get_counter("pregnant") >= 1
            return False
        
        @property
        def knowingly_pregnant(self):
            return (
            self.counters.pregnant >= 10 and self.flags.foundpreg
        ) or self.is_visibly_pregnant
        
        @property
        def is_visibly_pregnant(self):
            if self.is_female:
                return self.get_counter("pregnant") >= 30
            return False
        
        def unpreg(self):
            self.counters.pregnant = None
            self.flags.pregnancy_father = False
            self.flags.foundpreg = False
        
        @property
        def is_collared(self):
            return self.flags.collared
        
        @property
        def sexperience(self):
            return self.base_sexperience + self.flags.sexperience
        
        @property
        def base_sexperience(self):
            return max(
            [
                sum(
                    [
                        3 + (girl.sexperience * 2)
                        for girl in Person.all_people(ignore_hidden=False)
                        if girl.sexperience
                    ]
                ),
                self.flags.base_sexperience,
            ]
        )
        
        @property
        def min_sexperience(self):
            return self.base_min_sexperience + self.flags.sexperience
        
        @property
        def base_min_sexperience(self):
            return max(
            [
                sum(
                    [
                        3 + (girl.sexperience * 2)
                        for girl in Person.all_people(ignore_hidden=False)
                        if girl.sexperience
                    ]
                ),
                self.flags.base_min_sexperience,
            ]
        )
        
        def lose_item(self, item, amount=1):
            if GALLERY_MODE:
                return
            
            if amount < 0:
                return
            if isinstance(item, ItemBase):
                item = item.name
            if item in self.inventory:
                self.inventory[item] -= amount
                if self.inventory[item] <= 0:
                    del self.inventory[item]
        
        def has_item(self, item):
            if isinstance(item, ItemBase):
                item = item.name
            if item in self.inventory:
                amount = self.inventory[item]
                
                item = ItemBase.find(item)
                if config.developer and item is None:
                    raise ValueError(
                    "requested amount of non-existent item {}".format(item_id)
                )
                if isinstance(item, Consumable):
                    
                    amount = int((amount + item.uses - 1.0) / item.uses)
                return amount
            else:
                return 0
        
        def gain_item(self, item_id, amount=1):
            if GALLERY_MODE:
                return
            item = ItemBase.find(item_id)
            if item is None:
                if config.developer:
                    raise ValueError("non-existent item {} gained".format(item_id))
                return
            
            if isinstance(item, Consumable):
                amount *= item.uses
                
                amount = int(amount)
            
            if amount <= 0:
                return
            if item_id in self.inventory:
                self.inventory[item_id] += amount
            else:
                self.inventory[item_id] = amount
        
        def has_skill(self, skill):
            return self.skills[skill]()
        
        def gain_skill(self, name, value=True):
            self.skills[name] += value
        
        def has_condom(self):
            return (
            any(
                [
                    x in self.inventory
                    for x in (
                        "condom",
                        "box_of_condoms",
                        "pierced_condom",
                        "box_of_pierced_condoms",
                    )
                ]
            )
            or GALLERY_MODE
        )
        
        def use_condom(self):
            if GALLERY_MODE:
                return True
            
            condom_types = {"condom", "pierced_condom"} & self.inventory.keys()
            if condom_types:
                condom = randchoice(list(condom_types))
                self.lose_item(condom)
                return condom != "pierced_condom"
            
            box_types = {"box_of_condoms", "box_of_pierced_condoms"} & self.inventory.keys()
            if box_types:
                condom_box = Consumable.find(randchoice(list(box_types)))
                condom_box.use()
                condom = condom_box.name.replace("box_of_", "")[:-1]
                self.lose_item(condom)
                return condom != "pierced_condom"
            
            return False
        
        
        
        def get_partners(self, defaults=None, ignore=None):
            return self._get_people(
            defaults, ignore, lambda x: x.sexperience and not x.is_gone_forever
        )
        
        def get_girlfriends(self, defaults=None, ignore=None):
            return self._get_people(
            defaults, ignore, lambda x: x.is_girlfriend and not x.is_gone_forever
        )
        
        def get_pregs(self, defaults=None, ignore=None):
            return self._get_people(defaults, ignore, lambda x: x.is_visibly_pregnant)
        
        @staticmethod
        def _get_people(defaults, ignore, fn):
            ignored = ignore if ignore else []
            result = defaults if defaults else set()
            
            result.update(
            [
                person.id
                for person in Person.all_people(ignore_hidden=False)
                if person.id not in ignored and fn(person)
            ]
        )
            return result
        
        @property
        def has_motor_vehicle(self):
            return any(vehicle in self.inventory for vehicle in ("car", "sports_car"))
        
        @property
        def has_vehicle(self):
            return any(
            vehicle in self.inventory for vehicle in ("bike", "car", "sports_car")
        )
        
        @property
        def has_items(self):
            return len(self.inventory) > 0
        
        @property
        def has_gifts(self):
            return (
            len([None for i in self.inventory if isinstance(ItemBase.find(i), Gift)])
            > 0
        )
        
        @property
        def on_date(self):
            return not isinstance(game.active_date, NoDateEvent)
        
        @property
        def equipment_for_ui(self):
            clothes = self.equipment.get("clothes", "")
            accessory = self.equipment.get("accessory", "")
            if clothes:
                clothes = self.equipment.get("clothes").display_name
            if accessory:
                accessory = self.equipment.get("accessory").display_name
            return clothes, accessory
        
        def cancel_activity(self, end_event=False):
            if self.activity and hasattr(self.activity, "flags"):
                self.activity.flags.canceled = True
                if end_event:
                    self.activity.flags.end_event = True
        
        def replace_activity(self, end_event=False):
            if self.activity and hasattr(self.activity, "flags"):
                self.activity.flags.replaced = True
                if end_event:
                    self.activity.flags.end_event = True
        
        @staticmethod
        def cancel_event():
            if "do_event" in globals() and do_event and hasattr(do_event, "flags"):
                do_event.flags.canceled = True
            elif config.developer:
                raise Exception("Using hero.cancel_event outside an event.")


    def random_npc_impregnate(npc_name, force=False, x="left", y="top"):
        """
    Use for BreeMC when impregnate by random npc (pornstar)
    """
        
        if game.flags.nopreg or hero.is_male:
            return False
        
        if hero.counters.pregnant == 0 and (force or (randint(1, 100) <= hero.fertility)):
            hero.set_counter("pregnant")
            hero.flags.pregnancy_father = npc_name
            if persistent.pregnancy_notification:
                renpy.show(
                f"fx impregnate rnd{randint(1, 5)}",
                at_list=[
                    impregnate_display(
                        0.05 if x == "left" else 0.95, 0.05 if y == "top" else 0.95
                    )
                ],
            )
            return True
        return False


    def artificial_impregnate():
        """
    Use for BreeMC when clinic impregnate at hospital
    """
        
        if game.flags.nopreg or hero.is_male:
            return False
        if hero.counters.pregnant == 0:
            hero.set_counter("pregnant")
            hero.flags.pregnancy_father = "unknown"
            return True
        return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
