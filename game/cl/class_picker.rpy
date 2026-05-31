


























































init python:

    import inspect


    OUTFITS = [
    "apron",
    "bikini",
    "bowsette",
    "casual",
    "casual2",
    "chinese",
    "christmas",
    "cosplay",
    "cowkini",
    "crossdress",
    "daddy",
    "date",
    "halloween",
    "innocentcasual",
    "innocentdate",
    "innocentswimsuit",
    "invisible",
    "jail",
    "karate",
    "lpswimsuit",
    "maid",
    "naked",
    "nun",
    "pinkmaid",
    "puredate",
    "rope",
    "rpg",
    "santa",
    "sexycasual",
    "sexydate",
    "sexynun",
    "sexyswimsuit",
    "sexyunderwear",
    "sexywork",
    "sleep",
    "sluttydate",
    "sluttyswimsuit",
    "sport",
    "strapon",
    "stripper",
    "suit",
    "swimsuit",
    "swimsuitb",
    "towel",
    "tux",
    "underwear",
    "wedding",
    "work",
    "casual_date",
    "casual_swimsuit",
    "casual_underwear",
    "casual_work",
    "bunny",
    "dominatrix",
    "funeral",
]



    class DayNightPicker(object):
        def __call__(self, attr):
            if game.hour >= 20 or game.hour <= 5:
                attr.add("night")
            else:
                attr.add("day")
            if enable_debug_picker:
                renpy.log(f"DayNightPicker results: {attr}")
            return attr


    class IndoorOutdoorPicker(object):
        def __call__(self, attr):
            if game.room in [
            "alley",
            "beach",
            "cinema",
            "forest",
            "house",
            "map",
            "neighborhood",
            "park",
            "pond",
            "rooftop",
            "street",
            "university",
        ]:
                attr.add("outdoor")
            else:
                attr.add("indoor")
            if enable_debug_picker:
                renpy.log(f"IndoorOutdoorPicker results: {attr}")
            return attr


    class RoomPicker(object):
        def __call__(self, attr):
            if game.room.startswith("date_"):
                room = game.room.replace("date_", "")
            else:
                room = game.room
            attr.add(room)
            if enable_debug_picker:
                renpy.log(f"RoomPicker results: {attr}")
            return attr


    class SeasonPicker(object):
        def __init__(self, replace_season=False):
            """
        Special days and season ar often used together.
        It can be useful to prefer special day to seasons.
        """
            self.replace_season = replace_season
        
        def __call__(self, attr):
            if not (
            self.replace_season and any(attr & {"halloween", "christmas", "valentine"})
        ):
                attr.add(game.calendar.season_name)
            if enable_debug_picker:
                renpy.log(f"SeasonPicker results: {attr}")
            return attr


    class SpecialDayPicker(object):
        def __init__(self, replace_season=False, bypass_days=None):
            """
        Special days and season ar often used together.
        It can be useful to prefer special day to seasons.
        bypass_days is used to avoid specific dates
        """
            self.replace_season = replace_season
            self.bypass_days = bypass_days if bypass_days else []
        
        def __call__(self, attr):
            
            if game.calendar.is_today("fall", 31) and game.hour >= 8:
                if "halloween" not in self.bypass_days:
                    attr.add("halloween")
            elif game.calendar.is_today("winter", 1) and game.hour < 6:
                if "halloween" not in self.bypass_days:
                    attr.add("halloween")
            elif game.calendar.is_today("winter", 25) and game.hour >= 8:
                if "christmas" not in self.bypass_days:
                    attr.add("christmas")
            elif game.calendar.is_today("winter", 26) and game.hour < 6:
                if "christmas" not in self.bypass_days:
                    attr.add("christmas")
            elif game.calendar.is_today("valentine"):
                if "valentine" not in self.bypass_days:
                    attr.add("valentine")
            if self.replace_season and any(attr & {"halloween", "christmas", "valentine"}):
                attr.difference_update(SEASONS)
            if enable_debug_picker:
                renpy.log(f"SpecialDayPicker results: {attr}")
            return attr



    class DickPicker(object):
        def __call__(self, attr):
            if hero.is_male and not any(
            {"small", "medium", "big", "mc_small", "mc_medium", "mc_big"} & attr
        ):
                if hero.has_skill("smalldick"):
                    attr.add("small")
                elif hero.has_skill("hung"):
                    attr.add("big")
                else:
                    attr.add("medium")
            if enable_debug_picker:
                renpy.log(f"DickPicker results: {attr}")
            return attr


    class VehiclePicker(object):
        def __call__(self, attr):
            if "sports_car" in hero.inventory:
                attr.add("sportscar")
            elif "car" in hero.inventory:
                attr.add("car")
            elif "bike" in hero.inventory:
                attr.add("bike")
            if enable_debug_picker:
                renpy.log(f"VehiclePicker results: {attr}")
            return attr


    class XrayPicker(object):
        def __call__(self, attr):
            if persistent.xray:
                attr.add("xray")
            if enable_debug_picker:
                renpy.log(f"XrayPicker results: {attr}")
            return attr



    class MCCGPicker(object):
        """
    MCPicker when defined in the Pickers/MultiPickers list WILL be called first.
        - MCGenderPicker will add `breemc`/`mikemc` attribute
    Then regarding the gender:
    For MikeMC:
        - Dick size (small, medium, big) ----> Should be replaced by MCDickPicker at some point
        - MC outfits prefixed by `mc_` (`mc_casual`, `mc_date`...)
    For BreeMC:
        - MC wearing a collar or not, prefixed by `mc_` (`mc_collar`)
        - MC piercings, prefixed by `mc_` (`mc_nose`, `mc_navel`, `mc_pregnant_navel`...)
        - MC pubes, prefixed by `mc_` (`mc_pubes`)
        - MC pregnancy, prefixed by `mc_` (`mc_pregnant`)
        - MC outfits prefixed by `mc_` (`mc_casual`, `mc_date`, `mc_sexydate`...)
    When displaying MC sprites, disable `mc_` prefix addition on attributes
    """
        
        def __init__(self, add_mc_prefix=True):
            """
        If replace_npc_by_mc is True, just use MC related pickers and don't go further.
        This is useful for shared scenes/cg where only one person (MC/NPC) is shown.
        """
            self.add_mc_prefix = add_mc_prefix
        
        def __call__(self, attr):
            attr = MCGenderPicker().__call__(attr)
            
            if hero.is_male:
                attr = MCDickPicker().__call__(attr, self.add_mc_prefix)
            else:
                attr = MCCollarPicker().__call__(attr, self.add_mc_prefix)
                attr = MCHaircutPicker().__call__(attr, self.add_mc_prefix)
                attr = MCPiercingsPicker().__call__(attr, self.add_mc_prefix)
                attr = MCPubesPicker().__call__(attr, self.add_mc_prefix)
                attr = MCPregnancyPicker().__call__(attr, self.add_mc_prefix)
            attr = MCOutfitPicker().__call__(attr, self.add_mc_prefix)
            if enable_debug_picker:
                renpy.log(f"MCCGPicker results: {attr}")
            return attr


    class MCPicker(MCCGPicker):
        """
    MCPicker when defined in the Pickers/MultiPickers list WILL be called first.
        - MCGenderPicker will add `breemc`/`mikemc` attribute
    Then regarding the gender:
    For MikeMC:
        - Dick size (small, medium, big) ----> Should be replaced by MCDickPicker at some point
        - MC outfits prefixed by `mc_` (`mc_casual`, `mc_date`...)
    For BreeMC:
        - MC wearing a collar or not, prefixed by `mc_` (`mc_collar`)
        - MC piercings, prefixed by `mc_` (`mc_nose`, `mc_navel`, `mc_pregnant_navel`...)
        - MC pubes, prefixed by `mc_` (`mc_pubes`)
        - MC pregnancy, prefixed by `mc_` (`mc_pregnant`)
        - MC outfits prefixed by `mc_` (`mc_casual`, `mc_date`, `mc_sexydate`...)
    When displaying MC sprites, disable `mc_` prefix addition on attributes
    """
        
        def __call__(self, attr):
            attr = super(MCPicker, self).__call__(attr)
            attr = MCPositionPicker().__call__(attr, self.add_mc_prefix)
            if enable_debug_picker:
                renpy.log(f"MCPicker results: {attr}")
            return attr


    class MCGenderPicker(object):
        def __call__(self, attr):
            if hero.is_female:
                attr.add("breemc")
            else:
                attr.add("mikemc")
            if enable_debug_picker:
                renpy.log(f"MCGenderPicker results: {attr}")
            return attr


    class MCDickPicker(object):
        def __call__(self, attr, add_mc_prefix):
            if hero.is_male and not any(
            {"small", "medium", "big", "mc_small", "mc_medium", "mc_big"} & attr
        ):
                if hero.has_skill("smalldick"):
                    dick_attr = "small"
                elif hero.has_skill("hung"):
                    dick_attr = "big"
                else:
                    dick_attr = "medium"
                if add_mc_prefix:
                    dick_attr = f"mc_{dick_attr}"
                attr.add(dick_attr)
            if enable_debug_picker:
                renpy.log(f"MCDickPicker results: {attr}")
            return attr


    class MCOutfitPicker(object):
        """
    Will check if an outfit is passed in attributes. Prefix it with `mc_` if something's found.
    If not, call `hero.get_clothes()`. It will check if on a date, and the current room clothes.
    Prefix it with `mc_` if something's found.

    Then the whole check on sexy/slutty outfit is done. Removing the simple `mc_OUTFIT` if required.
    """
        
        def __call__(self, attr, add_mc_prefix):
            
            outfit_list = OUTFITS
            mc_prefixed_outfit_list = {f"mc_{outfit}" for outfit in outfit_list}
            
            if mc_prefixed_outfit_list & attr:
                mc_outfit = list(mc_prefixed_outfit_list & attr)[0]
                if enable_debug_picker:
                    renpy.log(f"MCOutfitPicker: {hero.gender} mc fixed {mc_outfit}")
            else:
                for o in copy.copy(attr):
                    if o in outfit_list:
                        mc_outfit = o
                        if enable_debug_picker:
                            renpy.log(f"MCOutfitPicker: {hero.gender} fixed {mc_outfit}")
                        break
                else:
                    mc_outfit = hero.get_clothes()
                    if enable_debug_picker:
                        renpy.log(f"MCOutfitPicker: {hero.gender} getclothes {mc_outfit}")
                
                
                mc_outfit = mc_outfit.removeprefix("sexy")
                mc_outfit = mc_outfit.removeprefix("slutty")
                if add_mc_prefix:
                    attr.add(f"mc_{mc_outfit}")
                else:
                    attr.add(mc_outfit)
            
            if enable_debug_picker:
                renpy.log(
                f"MCOutfitPicker between for: {hero.gender} with {mc_outfit} attrs: {attr}"
            )
            if (
            hero.has_item(f"slutty_{mc_outfit}_equip")
            and ItemBase.find(f"slutty_{mc_outfit}_equip").test()
        ):
                if enable_debug_picker:
                    renpy.log(
                    f"MCOutfitPicker found in inventory slutty{mc_outfit} --- {attr}"
                )
                attr.discard(f"mc_{mc_outfit}")
                attr.discard(f"{mc_outfit}")
                if add_mc_prefix:
                    attr.add(f"mc_slutty{mc_outfit}")
                else:
                    attr.add(f"slutty{mc_outfit}")
            
            elif (
            hero.has_item(f"sexy_{mc_outfit}_equip")
            and ItemBase.find(f"sexy_{mc_outfit}_equip").test()
        ):
                if enable_debug_picker:
                    renpy.log(
                    f"MCOutfitPicker found in inventory sexy{mc_outfit} --- {attr}"
                )
                attr.discard(f"mc_{mc_outfit}")
                attr.discard(f"{mc_outfit}")
                if add_mc_prefix:
                    attr.add(f"mc_sexy{mc_outfit}")
                else:
                    attr.add(f"sexy{mc_outfit}")
            
            elif (
            hero.has_item(f"pure_{mc_outfit}_equip")
            and ItemBase.find(f"pure_{mc_outfit}_equip").test()
        ):
                if enable_debug_picker:
                    renpy.log(
                    f"MCOutfitPicker found in inventory pure{mc_outfit} --- {attr}"
                )
                attr.discard(f"mc_{mc_outfit}")
                attr.discard(f"{mc_outfit}")
                if add_mc_prefix:
                    attr.add(f"mc_pure{mc_outfit}")
                else:
                    attr.add(f"pure{mc_outfit}")
            
            elif (
            hero.has_item(f"innocent_{mc_outfit}_equip")
            and ItemBase.find(f"innocent_{mc_outfit}_equip").test()
        ):
                if enable_debug_picker:
                    renpy.log(
                    f"MCOutfitPicker found in inventory innocent{mc_outfit} --- {attr}"
                )
                attr.discard(f"mc_{mc_outfit}")
                attr.discard(f"{mc_outfit}")
                if add_mc_prefix:
                    attr.add(f"mc_innocent{mc_outfit}")
                else:
                    attr.add(f"innocent{mc_outfit}")
            
            if enable_debug_picker:
                renpy.log(f"MCOutfitPicker results: {attr}")
            return attr


    class MCCollarPicker(object):
        """
    Check if the hero is collared, add 'collar' attribute if it is.
    """
        
        def __call__(self, attr, add_mc_prefix):
            if hero.is_collared:
                if add_mc_prefix:
                    attr.add("mc_collar")
                else:
                    attr.add("collar")
            if enable_debug_picker:
                renpy.log(f"MCCollarPicker results: {attr}")
            return attr


    class MCPiercingsPicker(object):
        """
    Iteration over piercings. No check on outfits or expressions.
    """
        
        def __call__(self, attr, add_mc_prefix):
            for p, status in hero.piercings.items():
                if status.worn:
                    if p == "navel" and hero.is_visibly_pregnant:
                        if add_mc_prefix:
                            attr.add("mc_pregnant_navel")
                        else:
                            attr.add("pregnant_navel")
                        attr.discard("navel")
                    else:
                        if add_mc_prefix:
                            attr.add(f"mc_{p}")
                        else:
                            attr.add(f"{p}")
            if enable_debug_picker:
                renpy.log(f"MCPiercingsPicker results: {attr}")
            return attr


    class MCPubesPicker(object):
        """
    Check if the hero has pubes, add 'pubes' attribute if that's the case.
    """
        
        def __call__(self, attr, add_mc_prefix):
            if hero.flags.pubes:
                if add_mc_prefix:
                    attr.add("mc_pubes")
                else:
                    attr.add("pubes")
            if enable_debug_picker:
                renpy.log(f"MCPubesPicker results: {attr}")
            return attr


    class MCHaircutPicker(object):
        """
    Check if the hero has haircut, add 'haircut' attribute if that's the case, else add 'nohaircut'.
    """
        
        def __call__(self, attr, add_mc_prefix):
            if hero.flags.haircut:
                haircut_attr = "haircut"
            else:
                haircut_attr = "nohaircut"
            
            if add_mc_prefix:
                haircut_attr = f"mc_{haircut_attr}"
            
            attr.add(haircut_attr)
            if enable_debug_picker:
                renpy.log(f"MCPubesPicker results: {attr}")
            return attr


    class MCPregnancyPicker(object):
        """
    Check if the hero is pregnant, add 'pregnant' attribute if that's the case.
    """
        
        def __call__(self, attr, add_mc_prefix):
            if hero.is_visibly_pregnant:
                if add_mc_prefix:
                    attr.add("mc_pregnant")
                else:
                    attr.add("pregnant")
            if enable_debug_picker:
                renpy.log(f"MCPregnancyPicker results: {attr}")
            return attr


    class MCPositionPicker(object):
        def __call__(self, attr, add_mc_prefix):
            if enable_debug_picker:
                renpy.log(f"MCPositionPicker attr: {attr}")
            if not {"a", "b", "d", "p", "z"} & attr:
                positions = [["a", "-b", "-d", "-p"], ["-a", "b", "-d", "-p"]]
                attr.update(randchoice(positions))
            if enable_debug_picker:
                renpy.log(f"PositionPicker results: {attr}")
            return attr



    class NPCPicker(object):
        _specific_picker_cache = {}
        
        def __init__(self, npc=None, id_prefix=False, clear_npc=False):
            self.npc = Person.find(npc) if npc else npc
            self.id_prefix = id_prefix
            self.clear_npc = clear_npc
            self._npc_id_cached = None
            self._specific_picker_class_cached = None
            self._specific_picker_class_checked = False
        
        @property
        def npc_id(self):
            if self._npc_id_cached is None:
                if self.npc == hero:
                    if hero.is_female:
                        self._npc_id_cached = "breemc"
                    else:
                        self._npc_id_cached = "mikemc"
                else:
                    self._npc_id_cached = get_person_id(self.npc)
            return self._npc_id_cached
        
        def __call__(self, attr):
            attr = self.set_npc(attr, self.id_prefix)
            return attr
        
        def set_npc(self, attr, id_prefix=False):
            if enable_debug_picker:
                renpy.log(f"NPCPicker: {self.npc} --- {attr}")
            if not self.npc:
                
                people_ids = getattr(renpy.store, "people_ids", [])
                for a in attr:
                    if a in people_ids:
                        g = Person.find(a)
                        if g is not None:
                            break
                else:
                    raise ValueError("No npc found")
                self.npc = g
                self._npc_id_cached = None  
                self._specific_picker_class_checked = False
            else:
                if enable_debug_picker:
                    renpy.log(f"NPCPicker self.npc already set: {self.npc.id}")
            
            
            if not self._specific_picker_class_checked:
                npc_id = self.npc_id
                if npc_id not in self._specific_picker_cache:
                    npc_id_cap = npc_id.capitalize()
                    picker_class_name = f"{npc_id_cap}Picker"
                    self._specific_picker_cache[npc_id] = globals().get(picker_class_name)
                self._specific_picker_class_cached = self._specific_picker_cache[npc_id]
                self._specific_picker_class_checked = True
            
            if self._specific_picker_class_cached:
                specific_picker = self._specific_picker_class_cached(id_prefix)
                attr = specific_picker.__call__(attr)
            
            if enable_debug_picker:
                renpy.log(f"NPCPicker results: {attr}")
            return attr
        
        def clean(self):
            if self.clear_npc:
                self.npc = None


    class HandcuffsPicker(NPCPicker):
        """
    Check if Mike has bought handcuffs and the npc has accepted wearing them, add 'handcuffs' attribute if he has.
    """
        
        def __call__(self, attr):
            attr = super(HandcuffsPicker, self).__call__(attr)
            
            if "handcuffs" in hero.inventory and self.npc.flags.handcuffs:
                if self.id_prefix:
                    attr.add(f"{self.npc_id}_handcuffs")
                else:
                    attr.add("handcuffs")
            
            if enable_debug_picker:
                renpy.log(f"HandcuffsPicker results: {attr}")
            self.clean()
            return attr


    class OutfitPicker(NPCPicker):
        """
    id_prefix: Prefix npc id to outfit: casual -> bree_casual
    add_simple_outfit_attribute: With MultiPicker (id_prefix=True), outfit attribute is prefixed and deleted (casuals -> bree_casual).
                                 If the variable is True, outfit attribute is kept.
    """
        
        WORK_NPCS = ["aletta", "audrey", "cassidy", "lavish", "shiori"]
        HOME_NPCS = ["bree", "lexi", "minami", "samantha", "sasha"]
        STRIPCLUB_NPCS = ["bree", "hanna", "harmony", "lexi", "reona", "shiori"]
        ATTR_CONTEXT = {"casual_", "slutty", "sexy", "pure", "innocent"}
        
        def __init__(
        self,
        npc=None,
        id_prefix=False,
        clear_npc=None,
        add_simple_outfit_attribute=False,
        add_simple_naked_attribute=False,
        use_morgan_cg_outfits=False,
    ):
            super().__init__(npc, id_prefix, clear_npc)
            self.add_simple_outfit_attribute = add_simple_outfit_attribute
            self.add_simple_naked_attribute = add_simple_naked_attribute
            self.use_morgan_cg_outfits = use_morgan_cg_outfits
        
        def __call__(self, attr):
            attr = self.set_npc(attr, self.id_prefix)
            
            if self._has_specific_picker(attr):
                return attr
            
            
            added_outfit_attribute = self._process_general_outfits(attr)
            
            if enable_debug_picker:
                renpy.log(f"OutfitPicker added outfit attribute: {added_outfit_attribute}")
            
            self._handle_room_logic(attr, added_outfit_attribute)
            
            
            self._handle_topless_logic(attr, added_outfit_attribute)
            
            
            self._handle_bottomless_logic(attr, added_outfit_attribute)
            
            
            self._handle_naked_logic(attr, added_outfit_attribute)
            
            if enable_debug_picker:
                renpy.log(f"OutfitPicker results: {attr}")
            self.clean()
            return attr
        
        def _has_specific_picker(self, attr):
            npc_id = self.npc_id
            cache_key = f"{npc_id}_OutfitPicker"
            if cache_key not in self._specific_picker_cache:
                npc_id_cap = npc_id.capitalize()
                picker_class_name = f"{npc_id_cap}OutfitPicker"
                self._specific_picker_cache[cache_key] = globals().get(picker_class_name)
            
            specific_picker_class = self._specific_picker_cache[cache_key]
            if specific_picker_class:
                specific_picker = specific_picker_class(
                id_prefix=self.id_prefix,
                use_morgan_cg_outfits=self.use_morgan_cg_outfits,
                add_simple_outfit_attribute=self.add_simple_outfit_attribute,
            )
                specific_picker.__call__(attr)
                if enable_debug_picker:
                    renpy.log(
                    f"OutfitPicker Found specific outfit picker for {self.npc_id} --- {attr}"
                )
                return True
            return False
        
        def _process_general_outfits(self, attr):
            added_outfit_attribute = None
            outfit_list = self.npc.outfits if self.npc.outfits else OUTFITS
            
            for outfit in copy.copy(attr):
                if self._is_valid_outfit(outfit, outfit_list):
                    added_outfit_attribute = self._update_outfit(attr, outfit)
                    break
            else:
                added_outfit_attribute = self._default_outfit(attr)
            
            self._process_context_attributes(attr, added_outfit_attribute)
            if enable_debug_picker:
                renpy.log(
                f"OutfitPicker _process_general_outfits: {added_outfit_attribute} - attr: {attr}"
            )
            return added_outfit_attribute
        
        def _is_valid_outfit(self, outfit, outfit_list):
            return outfit in outfit_list and (
            (outfit == "crossdress" and self.npc_id == "mike") or outfit != "crossdress"
        )
        
        def _update_outfit(self, attr, outfit):
            if self.id_prefix:
                if outfit != "naked" and not self.add_simple_outfit_attribute:
                    attr.discard(outfit)
                added_outfit_attribute = f"{self.npc_id}_{outfit}"
            else:
                added_outfit_attribute = outfit
            attr.add(added_outfit_attribute)
            if enable_debug_picker:
                renpy.log(
                f"OutfitPicker _update_outfit: {added_outfit_attribute} - attr: {attr}"
            )
            return added_outfit_attribute
        
        def _default_outfit(self, attr):
            outfit = self.npc.get_clothes()
            if self.id_prefix:
                added_outfit_attribute = f"{self.npc_id}_{outfit}"
                if self.add_simple_outfit_attribute:
                    attr.add(outfit)
            else:
                added_outfit_attribute = outfit
            attr.add(added_outfit_attribute)
            if enable_debug_picker:
                renpy.log(
                f"OutfitPicker _default_outfit: {added_outfit_attribute} - attr: {attr}"
            )
            return added_outfit_attribute
        
        def _process_context_attributes(self, attr, added_outfit_attribute):
            for context in self.ATTR_CONTEXT:
                for outfit in copy.copy(attr):
                    if context == "casual_" and self._is_in_appearance_screen_context(
                    outfit, context
                ):
                        attr.discard(outfit)
                        new_outfit = outfit.replace(context, "")
                        attr.add(new_outfit)
                    elif self._is_contextual_outfit_valid(outfit, context):
                        if not self.add_simple_outfit_attribute:
                            attr.discard(outfit)
                        attr.discard(f"{self.npc_id}_{outfit}")
                        new_outfit = f"{context}{outfit.replace(self.npc_id + '_', '')}"
                        added_outfit_attribute = (
                        f"{self.npc_id}_{new_outfit}" if self.id_prefix else new_outfit
                    )
                        attr.add(added_outfit_attribute)
            if enable_debug_picker:
                renpy.log(
                f"OutfitPicker _process_context_attributes: {added_outfit_attribute} - attr: {attr}"
            )
        
        @staticmethod
        def _is_in_appearance_screen_context(outfit, context):
            return outfit.startswith(context)
        
        def _is_contextual_outfit_valid(self, outfit, context):
            return self.npc.flags[f"{context}{outfit}"] or (
            self.id_prefix
            and self.npc.flags[f"{context}{outfit.replace(self.npc_id + '_', '')}"]
        )
        
        def _handle_topless_logic(self, attr, added_outfit_attribute):
            if self.npc.flags.topless and not game.flags.disable_clothing_policy:
                if Room.has_tag(game.room, "work") and self.npc_id in self.WORK_NPCS:
                    attr.add(f"{self.npc_id}_topless" if self.id_prefix else "topless")
                elif Room.has_tag(game.room, "home") and self.npc_id in self.HOME_NPCS:
                    attr.add(f"{self.npc_id}_topless" if self.id_prefix else "topless")
        
        def _handle_bottomless_logic(self, attr, added_outfit_attribute):
            if self.npc.flags.bottomless and not game.flags.disable_clothing_policy:
                if Room.has_tag(game.room, "work") and self.npc_id in self.WORK_NPCS:
                    attr.add(
                    f"{self.npc_id}_bottomless" if self.id_prefix else "bottomless"
                )
        
        
        
        def _handle_naked_logic(self, attr, added_outfit_attribute):
            if (
            self.npc.flags.naked
            and not game.flags.disable_clothing_policy
            and Room.has_tag(game.room, "home")
            and self.npc_id in self.HOME_NPCS
        ):
                attr.discard(added_outfit_attribute)
                attr.add(f"{self.npc_id}_naked" if self.id_prefix else "naked")
            elif (
            self.npc.flags.naked
            and not game.flags.disable_clothing_policy
            and Room.has_tag(game.room, "work")
            and self.npc_id in self.WORK_NPCS
        ):
                attr.discard(added_outfit_attribute)
                attr.add(f"{self.npc_id}_naked" if self.id_prefix else "naked")
            if enable_debug_picker:
                renpy.log(f"_handle_naked_logic results: {attr}")
        
        def _handle_room_logic(self, attr, added_outfit_attribute):
            current_screen_name = CurrentScreenName()
            if (
            self.npc.flags.stripper_outfit
            and not game.flags.disable_clothing_policy
            and game.room == "stripclub"
            and self.npc_id in self.STRIPCLUB_NPCS
            and current_screen_name != "appearance"
        ):
                attr.discard(added_outfit_attribute)
                attr.add(
                f"{self.npc_id}_{self.npc.flags.stripper_outfit}"
                if self.id_prefix
                else self.npc.flags.stripper_outfit
            )
            if enable_debug_picker:
                renpy.log(
                f"_handle_room_logic results: {attr} - current screen name: {current_screen_name}"
            )


    class PiercingsPicker(NPCPicker):
        """
    Iteration over piercings. No check on outfits or expressions.
    Now with smart attribute prefixing for layeredimage optimization.
    """
        
        def __init__(
        self, npc=None, id_prefix=False, clear_npc=None, piercings_prefix=False
    ):
            super().__init__(npc, id_prefix, clear_npc)
            self.piercings_prefix = piercings_prefix
        
        def __call__(self, attr):
            attr = super(PiercingsPicker, self).__call__(attr)
            
            for p, status in self.npc.piercings.items():
                if status.worn:
                    p_name = p
                    if p == "navel" and self.npc.is_visibly_pregnant:
                        p_name = "pregnant_navel"
                    
                    
                    if self.id_prefix or self.piercings_prefix:
                        attr.add(f"{self.npc_id}_{p_name}")
                    else:
                        attr.add(p_name)
            
            if enable_debug_picker:
                renpy.log(f"PiercingsPicker results: {attr}")
            self.clean()
            return attr


    class PositionPicker(NPCPicker):
        """
    Selects a position for an NPC based on their attributes and available images.

    The position selection depends on:
    - Available position images for the NPC
    - NPC's love level (if >= LOVE_THRESHOLD)
    - NPC's submission level (if >= SUB_THRESHOLD)
    - NPC's yandere level (if >= YANDERE_THRESHOLD)

    If a position is already specified in the attributes, it will be used.
    Otherwise, a position will be randomly selected based on the above criteria.
    """
        
        
        LOVE_THRESHOLD = 100
        SUB_THRESHOLD = 75
        YANDERE_THRESHOLD = 50
        
        
        POSITION_ATTRIBUTES = {"a", "b", "bbis", "c", "d", "e", "p", "y", "z", "_a", "_b"}
        
        _available_positions_cache = {}
        _has_image_cache = {}
        
        def _has_image(self, img_name):
            if img_name not in self._has_image_cache:
                self._has_image_cache[img_name] = renpy.has_image(img_name)
            return self._has_image_cache[img_name]
        
        def __init__(self, npc=None, id_prefix=False, clear_npc=False):
            """Initialize the PositionPicker with the given NPC."""
            super().__init__(npc, id_prefix, clear_npc)
        
        def __call__(self, attr):
            """
        Select a position for the NPC and update the attributes.

        Args:
            attr: Set of attributes to update

        Returns:
            Updated set of attributes
        """
            attr = super(PositionPicker, self).__call__(attr)
            
            if enable_debug_picker:
                renpy.log(f"PositionPicker npc: {self.npc_id}")
            
            
            if not self.POSITION_ATTRIBUTES & attr:
                if enable_debug_picker:
                    renpy.log(
                    f"PositionPicker: no position found in attribute: {attr} --- {self.POSITION_ATTRIBUTES & attr}"
                )
                positions = self._get_available_positions()
                
                
                if positions:
                    attr.update(randchoice(positions))
                else:
                    
                    attr.update(["a", "-b"])
                    if enable_debug_picker:
                        renpy.log("PositionPicker: No positions available, using default")
            else:
                if enable_debug_picker:
                    renpy.log(
                    f"PositionPicker: found position attribute: {attr} --- {self.POSITION_ATTRIBUTES & attr}"
                )
            
            if enable_debug_picker:
                renpy.log(f"PositionPicker results: {attr}")
            
            self.clean()
            return attr
        
        def _get_available_positions(self):
            """
        Get all available positions for the NPC based on their attributes.

        Returns:
            List of position attribute sets
        """
            npc_id = self.npc_id
            
            cache_key = (
            npc_id,
            self.npc.love >= self.LOVE_THRESHOLD,
            self.npc.sub >= self.SUB_THRESHOLD,
            getattr(self.npc, "yandere", 0) >= self.YANDERE_THRESHOLD,
        )
            if cache_key in self._available_positions_cache:
                return self._available_positions_cache[cache_key]
            
            positions = []
            
            
            
            positions.append(self._get_default_position())
            
            
            love_position = self._get_love_position()
            if love_position:
                positions.append(love_position)
            
            
            sub_position = self._get_submission_position()
            if sub_position:
                positions.append(sub_position)
            
            
            yandere_position = self._get_yandere_position()
            if yandere_position:
                positions.append(yandere_position)
            
            self._available_positions_cache[cache_key] = positions
            return positions
        
        def _get_default_position(self):
            """Get the default position attributes."""
            position = ["a", "-b"]
            
            
            self._add_optional_positions(position)
            
            return position
        
        def _get_love_position(self):
            """Get position attributes based on love level. (b/bbis position)"""
            if not hasattr(self.npc, "love") or self.npc.love < self.LOVE_THRESHOLD:
                return None
            
            position = ["-a"]
            
            
            if self._has_image(f"{self.npc_id}_position_bbis"):
                if randint(0, 1) == 0:
                    position.extend(["-b", "bbis"])
                else:
                    position.append("b")
            else:
                position.append("b")
            
            
            self._add_optional_positions(position)
            
            return position
        
        def _get_submission_position(self):
            """Get position attributes based on submission level. (c position)"""
            if (
            not hasattr(self.npc, "sub")
            or self.npc.sub < self.SUB_THRESHOLD
            or not self._has_image(f"{self.npc_id}_position_c")
        ):
                return None
            
            position = ["-a", "-b", "c"]
            
            
            if self._has_image(f"{self.npc_id}_position_bbis"):
                position.append("-bbis")
            if self._has_image(f"{self.npc_id}_position_y"):
                position.append("-y")
            
            return position
        
        def _get_yandere_position(self):
            """Get position attributes based on yandere level."""
            if (
            not hasattr(self.npc, "yandere")
            or self.npc.yandere < self.YANDERE_THRESHOLD
            or not self._has_image(f"{self.npc_id}_position_y")
        ):
                return None
            
            position = ["-a", "-b", "y"]
            
            
            if self._has_image(f"{self.npc_id}_position_c"):
                position.append("-c")
            if self._has_image(f"{self.npc_id}_position_bbis"):
                position.append("-bbis")
            
            return position
        
        def _add_optional_positions(self, position):
            """
        Add optional position attributes if their images exist.

        Args:
            position: List of position attributes to modify

        Note:
            This method modifies the position list in-place.
        """
            if self._has_image(f"{self.npc_id}_position_c"):
                position.append("-c")
            if self._has_image(f"{self.npc_id}_position_bbis"):
                position.append("-bbis")
            if self._has_image(f"{self.npc_id}_position_y"):
                position.append("-y")


    class PregnancyPicker(NPCPicker):
        """
    Check if a npc is pregnant, add 'pregnant' attribute if she is.
    """
        
        def __init__(
        self,
        npc=None,
        id_prefix=False,
        clear_npc=None,
        add_simple_pregnant_attribute=False,
    ):
            super().__init__(npc, id_prefix, clear_npc)
            self.add_simple_pregnant_attribute = add_simple_pregnant_attribute
        
        def __call__(self, attr):
            attr = super(PregnancyPicker, self).__call__(attr)
            
            if self.npc.is_visibly_pregnant:
                if self.id_prefix:
                    attr.add(f"{self.npc_id}_pregnant")
                    if self.add_simple_pregnant_attribute:
                        attr.add("pregnant")
                else:
                    attr.add("pregnant")
            if enable_debug_picker:
                renpy.log(f"PregnancyPicker results: {attr}")
            self.clean()
            return attr


    class ButtplugPicker(NPCPicker):
        """
    Check if a npc is buttplugged, add 'buttplug' attribute if she is.
    """
        
        def __call__(self, attr):
            attr = super(ButtplugPicker, self).__call__(attr)
            
            if self.npc.flags.buttplug:
                if self.id_prefix:
                    attr.add(f"{self.npc_id}_buttplug")
                else:
                    attr.add("buttplug")
            if enable_debug_picker:
                renpy.log(f"ButtplugPicker results: {attr}")
            self.clean()
            return attr


    class CollarPicker(NPCPicker):
        """
    Check if a npc is collared, add 'collar' attribute if she is.
    """
        
        def __call__(self, attr):
            attr = super(CollarPicker, self).__call__(attr)
            
            if self.npc.is_collared and "-collar" not in attr:
                if self.id_prefix:
                    attr.add(f"{self.npc_id}_collar")
                else:
                    attr.add("collar")
            if enable_debug_picker:
                renpy.log(f"CollarPicker results: {attr}")
            self.clean()
            return attr


    class PubesPicker(NPCPicker):
        """
    Check if a npc has pubes, add 'pubes' attribute if she is.
    """
        
        def __call__(self, attr):
            attr = super(PubesPicker, self).__call__(attr)
            
            if self.npc.flags.pubes and "-pubes" not in attr:
                if self.id_prefix:
                    attr.add(f"{self.npc_id}_pubes")
                else:
                    attr.add("pubes")
            if enable_debug_picker:
                renpy.log(f"PubesPicker results: {attr}")
            self.clean()
            return attr


    class ArmpitsPicker(NPCPicker):
        """
    Check if a npc has armpits hair, add 'armpits' attribute if she is.
    """
        
        def __call__(self, attr):
            attr = super(ArmpitsPicker, self).__call__(attr)
            
            if self.npc.flags.armpits:
                if self.id_prefix and "-armpits" not in attr:
                    attr.add(f"{self.npc_id}_armpits")
                else:
                    attr.add("armpits")
            if enable_debug_picker:
                renpy.log(f"ArmpitsPicker results: {attr}")
            self.clean()
            return attr


    class HaircutPicker(NPCPicker):
        """
    Check if a npc has haircut changes, add 'haircut' attribute if she has and "nohaircut" if she does not.
    """
        
        def __call__(self, attr):
            attr = super(HaircutPicker, self).__call__(attr)
            if {f"{self.npc_id}_haircut", f"{self.npc_id}_nohaircut"} & attr:
                if enable_debug_picker:
                    renpy.log(f"HaircutPicker fixed haircut: {attr}")
                self.clean()
                return attr
            elif {"haircut", "nohaircut"} & attr:
                if "haircut" in attr:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            else:
                if self.npc.flags.haircut:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            if self.id_prefix:
                attr.add(f"{self.npc_id}_{haircut}")
            else:
                attr.add(haircut)
            if enable_debug_picker:
                renpy.log(f"HaircutPicker results: {attr}")
            self.clean()
            return attr



    class EndingKidPicker(NPCPicker):
        """
    Should manage kid's skin and hair here:
    danny: latin - dark
    dwayne: black - ???
    jack: white - dark
    master: white - ???
    mike: white - dark
    ryan: white - blond
    scottie: white - blond
    shawn: white - blond
    victor: white - dark
    """
        
        def __call__(self, attr):
            if enable_debug_picker:
                renpy.log(f"EndingKidPicker _call_ params: {attr}")
            if hero.is_male:
                attr = super(EndingKidPicker, self).__call__(attr)
                if self.npc.flags.mikeBabies >= 1 or self.npc.is_visibly_pregnant:
                    if self.id_prefix:
                        attr.add(f"{self.npc_id}_kid")
                    else:
                        attr.add("kid")
                if enable_debug_picker:
                    renpy.log(f"NPCEndingKidPicker results: {attr}")
                self.clean()
            elif hero.is_female:
                if hero.pregnant:
                    if hero.flags.pregnancy_father in {"dwayne"}:
                        attr.add("black")
                    elif hero.flags.pregnancy_father in {"jack"}:
                        attr.add("fat")
                        attr.add("white")
                        attr.add("dark")
                    elif hero.flags.pregnancy_father in {"danny"}:
                        attr.add("latin")
                    elif hero.flags.pregnancy_father in {
                    "mike",
                    "victor",
                }:
                        attr.add("white")
                        attr.add("dark")
                    elif hero.flags.pregnancy_father in {
                    "master",
                }:
                        attr.add("white")
                        attr.add("brown")
                    elif hero.flags.pregnancy_father in {
                    "ryan",
                    "scottie",
                    "shawn",
                }:
                        attr.add("white")
                        attr.add("blond")
                    else:
                        skin = randchoice(["black", "fat", "latin", "white"])
                        attr.add(skin)
                        if skin == "white":
                            attr.add(randchoice(["dark", "blond", "brown", "red"]))
                if enable_debug_picker:
                    renpy.log(f"MCEndingKidPicker results: {attr}")
            if enable_debug_picker:
                renpy.log(f"EndingKidPicker results: {attr}")
            return attr



    class Pickers(object):
        _signature_cache = {}
        
        def _get_signature_params(self, cls):
            if cls not in self._signature_cache:
                self._signature_cache[cls] = set(inspect.signature(cls.__init__).parameters)
            return self._signature_cache[cls]
        
        def __init__(self, pickers, **kwargs):
            if getattr(self, "_initialized", False):
                return
            self.attr_pickers = []
            self.kwargs = kwargs or {}
            if isinstance(pickers, list):
                
                for picker in pickers:
                    if issubclass(picker, MCPicker):
                        self._check_init_args(picker)
                
                
                for picker in pickers:
                    if not issubclass(picker, MCPicker) and not issubclass(
                    picker, NPCSpecific
                ):
                        self._check_init_args(picker)
                
                
                for picker in pickers:
                    if issubclass(picker, NPCSpecific):
                        self._check_init_args(picker)
                self._initialized = True
            else:
                raise TypeError("Expected a list of Picker class")
        
        def _check_init_args(self, picker):
            default_params = {"self", "args", "kwargs"}
            remaining_params = self._get_signature_params(picker) - default_params
            if remaining_params:
                init_kwargs = {
                init_arg: self.kwargs.get(init_arg)
                for init_arg in remaining_params
                if init_arg in self.kwargs
            }
                if init_kwargs:
                    inst = picker(**init_kwargs)
                    self.attr_pickers.append(inst)
                else:
                    inst = picker()
                    self.attr_pickers.append(inst)
            else:
                self.attr_pickers.append(picker())
        
        def __call__(self, attr):
            if not renpy.store.game.room:  
                return attr
            for attr_picker in self.attr_pickers:
                attr.update(attr_picker.__call__(attr))
                if "replace_npc" in attr:
                    if enable_debug_picker:
                        renpy.log(
                        f"Pickers stopping iteration on picker as 'replace_npc' attribute found in layered image: {attr_picker} --- {attr}"
                    )
                    break
            
            if enable_debug_picker:
                renpy.log(f"Pickers results: {attr}")
            return attr


    class MultiPickers(object):
        _signature_cache = {}
        
        def _get_signature_params(self, cls):
            if cls not in self._signature_cache:
                self._signature_cache[cls] = set(inspect.signature(cls.__init__).parameters)
            return self._signature_cache[cls]
        
        def __init__(
        self,
        pickers,
        npcs=None,
        append_npc_from_attributes=False,
        clear_npcs=True,
        **kwargs,
    ):
            if isinstance(pickers, list):
                self.mc_pickers = []
                self.npc_pickers = []
                self.generic_pickers = []
                self.npc_specific_pickers = []
                for picker in pickers:
                    if issubclass(picker, MCCGPicker):
                        self.mc_pickers.append(picker)
                    elif issubclass(picker, NPCPicker):
                        self.npc_pickers.append(picker)
                    elif issubclass(picker, NPCSpecific):
                        self.npc_specific_pickers.append(picker)
                    else:
                        self.generic_pickers.append(picker)
                
                self.npcs = [Person.find(g) for g in npcs] if npcs else []
                self.clear_npcs = clear_npcs
                self.append_npc_from_attributes = append_npc_from_attributes
                self.kwargs = kwargs
                if not self.npcs and not self.append_npc_from_attributes:
                    renpy.log(
                    "WARNING: MultiPickers npcs is None and no append from attribute"
                )
            else:
                raise TypeError("Expected a list of Picker class")
        
        def set_npcs(self, attr):
            if not self.npcs or self.append_npc_from_attributes:
                if "replace_npc" in attr:
                    self.npcs = ["hero"]
                    if enable_debug_picker:
                        renpy.log(
                        f"MultiPickers set_npcs found 'replace_npc' attribute: {self.npcs}"
                    )
                else:
                    npcs_in_attr = []
                    people_ids = getattr(renpy.store, "people_ids", [])
                    
                    
                    
                    for p_id in people_ids:
                        if p_id in attr:
                            p = Person.find(p_id)
                            if p is not None:
                                npcs_in_attr.append(p)
                    
                    if self.npcs and self.append_npc_from_attributes:
                        
                        current_npc_ids = {n.id for n in self.npcs if n}
                        for n in npcs_in_attr:
                            if n.id not in current_npc_ids:
                                self.npcs.append(n)
                    else:
                        self.npcs = npcs_in_attr
                    
                    if enable_debug_picker:
                        renpy.log(
                        f"MultiPickers set_npcs if not self.npcs: {self.npcs} - {attr}"
                    )
            else:
                if enable_debug_picker:
                    renpy.log(f"MultiPickers set_npcs if self.npcs: {self.npcs}")
        
        def __call__(self, attr):
            if not renpy.store.game.room:  
                return attr
            if enable_debug_picker:
                renpy.log(
                f"MultiPickers __call__: {attr} --- {self.generic_pickers} --- {self.kwargs} --- orig self.npcs: {self.npcs}"
            )
            
            if not hasattr(self, "_mc_pickers_inst"):
                self._mc_pickers_inst = Pickers(
                self.mc_pickers, id_prefix=True, **self.kwargs
            )
            attr.update(self._mc_pickers_inst.__call__(attr))
            
            if not hasattr(self, "_generic_pickers_inst"):
                self._generic_pickers_inst = Pickers(
                self.generic_pickers, id_prefix=True, **self.kwargs
            )
            attr.update(self._generic_pickers_inst.__call__(attr))
            
            initial_npcs = self.npcs
            self.set_npcs(attr)
            
            
            if not hasattr(self, "_npc_pickers_inst_cache"):
                self._npc_pickers_inst_cache = {}
            
            for npc in list(filter(None, self.npcs)):
                attr.add(npc.id)
                if npc.id not in self._npc_pickers_inst_cache:
                    self._npc_pickers_inst_cache[npc.id] = Pickers(
                    self.npc_pickers, npc=npc, id_prefix=True, **self.kwargs
                )
                attr.update(self._npc_pickers_inst_cache[npc.id].__call__(attr))
            
            if not hasattr(self, "_npc_specific_pickers_inst"):
                self._npc_specific_pickers_inst = Pickers(
                self.npc_specific_pickers, id_prefix=True, **self.kwargs
            )
            attr.update(self._npc_specific_pickers_inst.__call__(attr))
            
            if enable_debug_picker:
                renpy.log(f"MultiPickers results: {attr}")
            try:
                return attr
            finally:
                if self.append_npc_from_attributes:
                    self.npcs = initial_npcs
                if enable_debug_picker:
                    renpy.log(f"MultiPickers finally: {attr}")



    class NPCSpecific(object):
        def __init__(self, id_prefix):
            self.id_prefix = id_prefix


    class AlettaPicker(NPCSpecific):
        def __call__(self, attr):
            if self.id_prefix:
                attr.add("aletta_glasses")
            else:
                attr.add("glasses")
            if enable_debug_picker:
                renpy.log(f"AlettaPicker results: {attr}")
            return attr


    class CamilaPicker(NPCSpecific):
        def __call__(self, attr):
            if camila.piercings.ears.worn:
                if "date" in attr:
                    if self.id_prefix:
                        attr.add("camila_date_ears")
                    else:
                        attr.add("date_ears")
                    attr.discard("ears")
                    attr.discard("camila_ears")
                elif "sexydate" in attr:
                    if self.id_prefix:
                        attr.add("camila_sexydate_ears")
                    else:
                        attr.add("sexydate_ears")
                    attr.discard("ears")
                    attr.discard("camila_ears")
            if enable_debug_picker:
                renpy.log(f"CamilaPicker results: {attr}")
            return attr


    class MikePicker(NPCSpecific):
        def __call__(self, attr):
            if mike.flags.dicksize == "hung":
                if self.id_prefix:
                    attr.add("mike_big")
                else:
                    attr.add("big")
            elif mike.flags.dicksize == "smalldick":
                if self.id_prefix:
                    attr.add("mike_small")
                else:
                    attr.add("small")
            else:
                if self.id_prefix:
                    attr.add("mike_medium")
                else:
                    attr.add("medium")
            if enable_debug_picker:
                renpy.log(f"MikePicker results: {attr}")
            return attr


    class HannaPicker(NPCSpecific):
        def __call__(self, attr):
            if hanna.flags.armpits:
                if self.id_prefix:
                    attr.add("hanna_armpits")
                else:
                    attr.add("armpits")
            return attr


    class HarmonyPicker(NPCSpecific):
        def __call__(self, attr):
            if "nun" in attr and harmony.purity < VLP:
                attr.discard("nun")
                attr.add("sexynun")
            
            
            
            
            if enable_debug_picker:
                renpy.log(f"HarmonyPicker results: {attr}")
            return attr


    class PallaPicker(NPCSpecific):
        def __call__(self, attr):
            if self.id_prefix:
                attr.add("palla_glasses")
            else:
                attr.add("glasses")
            if enable_debug_picker:
                renpy.log(f"PallaPicker results: {attr}")
            return attr


    class SamanthaPicker(NPCSpecific):
        def __call__(self, attr):
            if samantha.flags.engaged:
                if self.id_prefix:
                    attr.add("samantha_ring")
                else:
                    attr.add("ring")
            return attr


    class SashaPicker(NPCSpecific):
        def __call__(self, attr):
            if sasha.flags.boobjob:
                if self.id_prefix:
                    attr.add("sasha_boobjob")
                    attr.discard("sasha_noboobjob")
                else:
                    attr.add("boobjob")
                    attr.discard("noboobjob")
            else:
                if self.id_prefix:
                    attr.add("sasha_noboobjob")
                    attr.discard("sasha_boobjob")
                else:
                    attr.add("noboobjob")
                    attr.discard("boobjob")
            return attr


    class KleioPicker(NPCSpecific):
        def __call__(self, attr):
            if kleio.flags.tattoo == "wolf":
                if self.id_prefix:
                    attr.add("kleio_wolf")
                else:
                    attr.add("wolf")
            elif kleio.flags.tattoo == "angel":
                if self.id_prefix:
                    attr.add("kleio_angel")
                else:
                    attr.add("angel")
            return attr


    class CassidyPicker(NPCSpecific):
        def __call__(self, attr):
            if cassidy.flags.gold:
                if self.id_prefix:
                    attr.add("cassidy_gold")
                else:
                    attr.add("gold")
            if cassidy.flags.topless and (
            Room.has_tag(cassidy.room, "work") or Room.has_tag(cassidy.room, "home")
        ):
                if self.id_prefix:
                    attr.add("cassidy_topless")
                else:
                    attr.add("topless")
            return attr


    class ShioriPicker(NPCSpecific):
        def __call__(self, attr):
            if Room.has_tag(shiori.room, "work") and attr & {
            "work",
            "shiori_work",
            "sexywork",
            "shiori_sexywork",
        }:
                if "a" in attr:
                    attr.discard("a")
                    attr.discard("-c")
                    attr.add("c")
                elif "b" in attr:
                    attr.discard("b")
                    attr.discard("-d")
                    attr.add("d")
            elif "c" in attr:
                attr.discard("c")
                attr.discard("-a")
                attr.add("a")
            elif "d" in attr:
                attr.discard("d")
                attr.discard("-b")
                attr.add("b")
            
            if not (attr & {"nopeace", "peace"}):
                attr.add(randchoice(["nopeace", "peace"]))
            if not (attr & {"notpressed", "pressed"}):
                attr.add(randchoice(["notpressed", "pressed"]))
            return attr


    class ReonaPicker(NPCSpecific):
        def __call__(self, attr):
            if {"haircut", "nohaircut"} & attr:
                if "haircut" in attr:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            elif {"halloween"} & attr:
                haircut = "nohaircut"
            else:
                if reona.purity >= 50 and reona.flags.haircut:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            if self.id_prefix:
                attr.add(f"reona_{haircut}")
            else:
                attr.add(haircut)
            
            if {"glasses"} & attr:
                if self.id_prefix:
                    attr.add("reona_glasses")
                    attr.discard("glasses")
            
            if {"glasses", "reona_glasses"} & attr:
                if reona.purity >= 50:
                    if self.id_prefix:
                        attr.add("reona_pureglasses")
                        attr.discard("reona_glasses")
                        attr.discard("glasses")
                    else:
                        attr.add("pureglasses")
                        attr.discard("reona_glasses")
                        attr.discard("glasses")
            return attr


    class MorganPicker(NPCSpecific):
        def __call__(self, attr):
            if {"haircut", "nohaircut"} & attr:
                if "haircut" in attr:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            else:
                if morgan.male < 60:
                    haircut = "haircut"
                else:
                    haircut = "nohaircut"
            if self.id_prefix:
                attr.add(f"morgan_{haircut}")
            else:
                attr.add(haircut)
            
            if morgan.male < 40 and not morgan.flags.nomakeup:
                if self.id_prefix:
                    attr.add("morgan_makeup")
                else:
                    attr.add("makeup")
            if enable_debug_picker:
                renpy.log(f"MorganPicker results: {attr}")
            return attr



    class ReonaOutfitPicker(OutfitPicker):
        def __call__(self, attr):
            self.npc = reona
            
            
            added_outfit_attribute = self._process_general_outfits(attr)
            
            if enable_debug_picker:
                renpy.log(
                f"ReonaOutfitPicker added outfit attribute: {added_outfit_attribute}"
            )
            
            
            if reona.purity < 20 and reona.sub >= 50 and reona.flags.sexyunderwear:
                attr.add("reona_innersexy" if self.id_prefix else "innersexy")
            
            
            self._handle_room_logic(attr, added_outfit_attribute)
            
            renpy.log(f"ReonaOutfitPicker results: {attr}")
            self.clean()
            return attr
        
        def _process_general_outfits(self, attr):
            added_outfit_attribute = None
            reona_outfits = {
            "casual",
            "date",
            "halloween",
            "purecasual",
            "puredate",
            "rpg",
            "sexydate",
            "sexyswimsuit",
            "sexyunderwear",
            "sluttydate",
            "sport",
            "stripper",
            "swimsuit",
            "underwear",
            "wedding",
            "casual_date",
            "casual_swimsuit",
            "casual_underwear",
        }
            
            for outfit in copy.copy(attr):
                if self._is_valid_outfit(outfit, reona_outfits):
                    added_outfit_attribute = self._update_outfit(attr, outfit)
                    break
            else:
                added_outfit_attribute = self._default_outfit(attr)
            
            self._process_context_attributes(attr, added_outfit_attribute)
            if enable_debug_picker:
                renpy.log(
                f"ReonaOutfitPicker _process_general_outfits: {added_outfit_attribute} - attr: {attr}"
            )
            return added_outfit_attribute
        
        def _is_contextual_outfit_valid(self, outfit, context):
            if context == "pure":
                if "casual" == outfit:
                    return reona.purity >= 50 and reona.flags.purecasual
                elif "date" == outfit:
                    return reona.purity >= 60 and reona.flags.puredate
            elif context == "sexy":
                if "underwear" == outfit:
                    return (
                    reona.purity < 20 and reona.sub >= 50 and reona.flags.sexyunderwear
                )
                elif "date" == outfit:
                    return reona.purity < 20 and reona.flags.sexydate
            elif context == "slutty":
                if "date" == outfit:
                    return reona.purity < 10 and reona.flags.sluttydate
            
            return reona.flags[f"{context}{outfit}"] or (
            self.id_prefix and reona.flags[f"{context}{outfit.replace('reona_', '')}"]
        )


    class MorganOutfitPicker(OutfitPicker):
        def __call__(self, attr):
            if any(
            {
                "date",
                "casual",
                "swimsuit",
                "sexyswimsuit",
                "sport",
                "wedding",
                "sexydate",
                "sluttydate",
            }
            & attr
        ):
                
                tmp_outfit = list(
                {
                    "date",
                    "casual",
                    "swimsuit",
                    "sexyswimsuit",
                    "sport",
                    "wedding",
                    "sexydate",
                    "sluttydate",
                }
                & attr
            )[0]
            else:
                
                tmp_outfit = morgan.get_clothes()
                attr.add(tmp_outfit)
            
            male = morgan.male
            if "halloween" in attr:
                if self.id_prefix:
                    attr.add("morgan_halloween")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("halloween")
            elif "mermaid" in attr:
                if self.id_prefix:
                    attr.add("morgan_mermaid")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("mermaid")
            elif self.use_morgan_cg_outfits:
                if "date" in tmp_outfit:
                    if (
                    morgan.flags.sluttydate or "sluttydate" in tmp_outfit
                ) and "sexydate" not in tmp_outfit:
                        attr.add("sluttydate_morgan")
                        attr.discard("slutty")
                    elif (
                    morgan.flags.sexydate or "sexydate" in tmp_outfit
                ) and "sluttydate" not in tmp_outfit:
                        attr.add("sexydate_morgan")
                        attr.discard("sexy")
                    elif male >= 80:
                        
                        attr.add("tux_morgan")
                    elif male >= 60:
                        
                        attr.add("bluejacket_morgan")
                    elif male >= 40:
                        
                        attr.add("blackshorts_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 20:
                        
                        attr.add("blackmini_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    else:
                        
                        attr.add("dotdress_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("date")
                elif "wedding" in tmp_outfit:
                    if male >= 80:
                        
                        attr.add("tux_morgan")
                    elif male >= 60:
                        
                        attr.add("tux_morgan")
                    elif male >= 40:
                        
                        attr.add("weddingdress")
                    elif male >= 20:
                        
                        attr.add("weddingdress")
                    else:
                        
                        attr.add("weddingdress")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("wedding")
                elif "swimsuit" in tmp_outfit:
                    if morgan.flags.sexyswimsuit or "sexyswimsuit" in tmp_outfit:
                        attr.add("sexyswimsuit_morgan")
                        attr.discard("sexy")
                    elif male >= 60:
                        
                        attr.add("blueblackswimsuit_morgan")
                    elif male >= 20:
                        
                        attr.add("redbluebikini_morgan")
                    else:
                        
                        attr.add("bluebikini_morgan")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("swimsuit")
                else:
                    if male >= 80:
                        
                        attr.add("camo_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 60:
                        
                        attr.add("bluesweater_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 50:
                        
                        attr.add("blackjacket_morgan")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 20:
                        
                        attr.add("redhalf_morgan")
                    else:
                        
                        attr.add("whitetank_morgan")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("casual")
            else:
                if "casual" in tmp_outfit:
                    if male >= 80:
                        if self.id_prefix:
                            attr.add("morgan_blackjacket")
                        else:
                            attr.add("blackjacket")
                        if self.id_prefix:
                            attr.add("morgan_camopants")
                        else:
                            attr.add("camopants")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 60:
                        if self.id_prefix:
                            attr.add("morgan_bluesweater")
                        else:
                            attr.add("bluesweater")
                        if self.id_prefix:
                            attr.add("morgan_blackpants")
                        else:
                            attr.add("blackpants")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 50:
                        if self.id_prefix:
                            attr.add("morgan_blackjacket")
                        else:
                            attr.add("blackjacket")
                        if self.id_prefix:
                            attr.add("morgan_blackpants")
                        else:
                            attr.add("blackpants")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 20:
                        if self.id_prefix:
                            attr.add("morgan_redhalf")
                        else:
                            attr.add("redhalf")
                        if self.id_prefix:
                            attr.add("morgan_blackskirt")
                        else:
                            attr.add("blackskirt")
                    else:
                        if self.id_prefix:
                            attr.add("morgan_whitetank")
                        else:
                            attr.add("whitetank")
                        if self.id_prefix:
                            attr.add("morgan_blueskirt")
                        else:
                            attr.add("blueskirt")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("casual")
                elif "date" in tmp_outfit:
                    if (
                    morgan.flags.sluttydate or "sluttydate" in tmp_outfit
                ) and "sexydate" not in tmp_outfit:
                        if self.id_prefix:
                            attr.add("morgan_sluttydate")
                        else:
                            attr.add("sluttydate")
                        attr.discard("slutty")
                    elif (
                    morgan.flags.sexydate or "sexydate" in tmp_outfit
                ) and "sluttydate" not in tmp_outfit:
                        if self.id_prefix:
                            attr.add("morgan_sexydate")
                        else:
                            attr.add("sexydate")
                        attr.discard("sexy")
                    elif male >= 80:
                        if self.id_prefix:
                            attr.add("morgan_tuxtop")
                        else:
                            attr.add("tuxtop")
                        if self.id_prefix:
                            attr.add("morgan_tuxbottom")
                        else:
                            attr.add("tuxbottom")
                    elif male >= 60:
                        if self.id_prefix:
                            attr.add("morgan_bluejacket")
                        else:
                            attr.add("bluejacket")
                        if self.id_prefix:
                            attr.add("morgan_blackpants")
                        else:
                            attr.add("blackpants")
                    elif male >= 40:
                        if self.id_prefix:
                            attr.add("morgan_blacktube")
                        else:
                            attr.add("blacktube")
                        if self.id_prefix:
                            attr.add("morgan_blackshorts")
                        else:
                            attr.add("blackshorts")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    elif male >= 20:
                        if self.id_prefix:
                            attr.add("morgan_blacktube")
                        else:
                            attr.add("blacktube")
                        if self.id_prefix:
                            attr.add("morgan_blackmini")
                        else:
                            attr.add("blackmini")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    else:
                        if self.id_prefix:
                            attr.add("morgan_dotdress")
                        else:
                            attr.add("dotdress")
                        if "collar" not in attr or "morgan_collar" not in attr:
                            if self.id_prefix:
                                attr.add("morgan_necklace")
                            else:
                                attr.add("necklace")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("date")
                elif "wedding" in tmp_outfit:
                    if male >= 80:
                        if self.id_prefix:
                            attr.add("morgan_tuxtop")
                        else:
                            attr.add("tuxtop")
                        if self.id_prefix:
                            attr.add("morgan_tuxbottom")
                        else:
                            attr.add("tuxbottom")
                    elif male >= 60:
                        if self.id_prefix:
                            attr.add("morgan_tuxtop")
                        else:
                            attr.add("tuxtop")
                        if self.id_prefix:
                            attr.add("morgan_tuxbottom")
                        else:
                            attr.add("tuxbottom")
                    elif male >= 40:
                        if self.id_prefix:
                            attr.add("morgan_weddingdress")
                        else:
                            attr.add("weddingdress")
                    elif male >= 20:
                        if self.id_prefix:
                            attr.add("morgan_weddingdress")
                        else:
                            attr.add("weddingdress")
                    else:
                        if self.id_prefix:
                            attr.add("morgan_weddingdress")
                        else:
                            attr.add("weddingdress")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("wedding")
                elif "sport" in tmp_outfit:
                    if male >= 60:
                        if self.id_prefix:
                            attr.add("morgan_stripedworkout")
                        else:
                            attr.add("stripedworkout")
                        if self.id_prefix:
                            attr.add("morgan_sweatpants")
                        else:
                            attr.add("sweatpants")
                    elif male >= 50:
                        if self.id_prefix:
                            attr.add("morgan_sweatshirt")
                        else:
                            attr.add("sweatshirt")
                        if self.id_prefix:
                            attr.add("morgan_sweatpants")
                        else:
                            attr.add("sweatpants")
                    elif male >= 20:
                        if self.id_prefix:
                            attr.add("morgan_blacksport")
                        else:
                            attr.add("blacksport")
                        if self.id_prefix:
                            attr.add("morgan_blacktights")
                        else:
                            attr.add("blacktights")
                    else:
                        if self.id_prefix:
                            attr.add("morgan_tightsport")
                        else:
                            attr.add("tightsport")
                        if self.id_prefix:
                            attr.add("morgan_blacktights")
                        else:
                            attr.add("blacktights")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("sport")
                elif "swimsuit" in tmp_outfit:
                    if morgan.flags.sexyswimsuit or "sexyswimsuit" in tmp_outfit:
                        if self.id_prefix:
                            attr.add("morgan_sexyswimsuit")
                        else:
                            attr.add("sexyswimsuit")
                        attr.discard("sexy")
                    elif male >= 60:
                        if self.id_prefix:
                            attr.add("morgan_blueblackswimsuit")
                        else:
                            attr.add("blueblackswimsuit")
                    elif male >= 20:
                        if self.id_prefix:
                            attr.add("morgan_redbluebikinitop")
                        else:
                            attr.add("redbluebikinitop")
                        if self.id_prefix:
                            attr.add("morgan_redbluebikinibottom")
                        else:
                            attr.add("redbluebikinibottom")
                    else:
                        if self.id_prefix:
                            attr.add("morgan_bluebikinitop")
                        else:
                            attr.add("bluebikinitop")
                        if self.id_prefix:
                            attr.add("morgan_bluebikinibottom")
                        else:
                            attr.add("bluebikinibottom")
                    if not self.add_simple_outfit_attribute:
                        attr.discard("swimsuit")
            if enable_debug_picker:
                renpy.log(f"MorganOutfitPicker results: {attr}")
            return attr
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
