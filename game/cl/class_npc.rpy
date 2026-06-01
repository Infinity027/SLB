



init -15 python:

    class Girl(Registry, Person):
        def __init__(self, id, yaml):
            super(Girl, self).__init__(id, yaml)
        
        @property
        def fertility_modifier(self):
            return (
            0
            if ("barren" in self.traits or self.flags.pill or self.is_visibly_pregnant)
            else 0.5
            if "low fertility" in self.traits
            else 1.5
            if "fertile" in self.traits
            else 1
        )
        
        @property
        def fertility(self):
            return int(
            max(
                abs((game.days_played + self.birthday[1]) % 28 - 13) / 14.0 * 100 - 50,
                0,
            )
            * self.fertility_modifier
        )
        
        def impregnate(self, force=False, x="left", y="top", secret=False):
            # PREGNANCY DISABLED — girls never get pregnant. This short-circuits the
            # only automatic trigger, so no call site can ever set the pregnant state.
            # To restore pregnancy, delete the single "return False" line below.
            return False

            if game.flags.nopreg or self.flags.nopreg:
                return False
            
            if (
            self.counters.pregnant == 0
            and not self.flags.NPCpregnancy
            and (force or (randint(1, 100) <= self.fertility * hero.fertility_modifier))
        ):
                self.set_counter("pregnant")
                self.flags.pregnancies_number += 1
                self.flags.pregrequest = False
                if persistent.pregnancy_notification and not secret:
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
        
        @property
        def pregnant(self):
            return self.counters.pregnant >= 1
        
        @property
        def is_visibly_pregnant(self):
            return self.counters.pregnant >= 9 or self.flags.NPCpregnancy
        
        def unpreg(self):
            self.counters.pregnant = None
            self.flags.toldpreg = False
            self.flags.NPCpregnancy = False
        
        def set_girlfriend(self):
            self.flags.girlfriend = True
            self.flags.girlfriend_day = game.days_played
            if self.status in ["friend", "roommate", "coworker", "pet", "ex-girlfriend"]:
                self.status = "girlfriend"
        
        def set_fiance(self):
            self.flags.engagedmike = True
            self.flags.engagedmc = True
            hero.lose_item("wedding_ring")
            if self.status in [
            "friend",
            "roommate",
            "coworker",
            "girlfriend",
            "ex-girlfriend",
        ]:
                self.status = "fiance"
        
        def cancel_fiance(self):
            self.flags.engagedmike = False
            self.flags.engagedmc = False
            if self.status == "fiance":
                self.status = self.flags.previous_status
            self.love -= 25
            self.sub -= 25
        
        def force_condom_use(self, love, drinks, sub):
            """
        Return False if:
          - on pill
          - pregnant
          - drunk (girl.flags.drinks)
          - on drugs
          - girl's love is higher or equal than love parameter
          - sub parameter is passed and girl's sub is higher or equal than sub parameter
        """
            if self.pregnant:
                return False
            if self.flags.pill:
                return False
            if self.flags.drinks >= drinks:
                return False
            if self.flags.drugs:
                return False
            if self.love >= love:
                return False
            if sub and self.sub >= sub:
                return False
            return True


    class Guy(Registry, Person):
        def __init__(self, id, yaml):
            super(Guy, self).__init__(id, yaml)
        
        @property
        def default_attributes(self):
            return (
            YAML[self.id]["attributes"]
            if "attributes" in YAML[self.id]
            else {
                "love": {"min": 0, "max": 20, "default": 0},
                "sub": {"min": 0, "max": 100, "default": 0},
                "sexperience": {"min": 0, "max": None, "default": 0},
            }
        )
        
        @property
        def fertility_modifier(self):
            return (
            0.5 if "smalldick" in self.traits else 1.5 if "hung" in self.traits else 1
        )
        
        @property
        def fertility(self):
            return 100
        
        def impregnate(self, force=False, x="left", y="top", secret=False):
            
            if game.flags.nopreg or hero.is_male:
                return False
            
            if hero.counters.pregnant == 0 and (
            force or (randint(1, 100) <= hero.fertility * self.fertility_modifier)
        ):
                hero.set_counter("pregnant")
                hero.flags.pregnancy_father = self.id
                hero.flags.abort_pregnancy = False
                if persistent.pregnancy_notification and not secret:
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
        
        @property
        def pregnant(self):
            return False
        
        @property
        def is_visibly_pregnant(self):
            return False
        
        def unpreg(self):
            pass
        
        def force_condom_use(self, love, drinks, sub):
            """
        Return False if:
          - hero on pill
          - hero pregnant
          - drunk (girl.flags.drinks)
          - on drugs
          - guy's love is higher or equal than love parameter
          - sub parameter is passed and guy's sub is higher or equal than sub parameter
        """
            if hero.pregnant:
                return False
            if hero.flags.pill:
                return False
            if self.flags.drinks >= drinks:
                return False
            if self.flags.drugs:
                return False
            if self.love >= love:
                return False
            if sub and self.sub >= sub:
                return False
            return True
        
        def set_boyfriend(self):
            self.flags.boyfriend = True
            self.flags.boyfriend_day = game.days_played
            if self.status in ["friend", "roommate", "coworker", "pet", "ex-boyfriend"]:
                self.status = "boyfriend"
        
        def set_fiance(self):
            self.flags.engagedmc = True
            hero.lose_item("wedding_ring")
            if self.status in [
            "friend",
            "roommate",
            "coworker",
            "boyfriend",
            "ex-boyfriend",
        ]:
                self.status = "fiance"
        
        def cancel_fiance(self):
            self.flags.engagedmc = False
            if self.status == "fiance":
                self.status = self.flags.previous_status
            self.love -= 25
            self.sub -= 25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
