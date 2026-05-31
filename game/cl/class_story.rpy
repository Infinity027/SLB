
























init -20 python:


    from collections import OrderedDict




    class StoryTracker:
        STORY_KEYS = {
        "id",
        "name",
        "display_name",
        "start",
        "sort",
        "short",
        "outcome",
        "outcomes",
        "participants",
        "steps",
        "description",
        "condition",
        "conditions",
        "wiki_link",
        "type",
        "extra_data",
    }
        STORY_STEP_KEYS = {
        "name",
        "percentage",
        "outcome",
        "outcomes",
        "condition",
        "conditions",
        "icon",
        "optional",
        "toggle",
        "related_event",
    }
        STORY_OUTCOME_KEYS = {
        "description",
        "condition",
        "conditions",
        "hide",
        "next",
        "icon",
        "hide_story",
    }
        
        def __init__(self):
            self.notifications = OrderedDict()
            self._cache = {}
        
        
        
        def load(self):
            for id, story in load_yamls(
            lambda f: f.endswith(".yml") and "story/" in f, clazz=None
        ):
                if config.developer:
                    
                    self.test_yaml(id, story)
                store.STORIES[id] = Story(id, story)
        
        def test_yaml(self, id, data):
            diff = set(data.keys()) - self.STORY_KEYS
            if diff:
                raise Exception(f"Story '{id}' has unknown keys: {diff}")
            outcomes = (
            data["outcomes"] if "outcomes" in data else {"complete": data["outcome"]}
        )  
            self.test_yaml_outcomes(id, outcomes)
            steps = data["steps"]  
            self.test_yaml_steps(id, steps)
        
        def test_yaml_steps(self, parent_id, steps):
            for stepID in steps.keys():
                step = steps[stepID]
                diff = set(step.keys()) - self.STORY_STEP_KEYS
                if diff:
                    raise Exception(
                    f"StoryStep '{parent_id}.{stepID}' has unknown keys: {diff}"
                )
                
                if "steps" in step:
                    self.test_yaml_steps(f"{parent_id}.{stepID}", step["steps"])
                
                if "outcome" in step or "outcomes" in step:
                    outcomes = (
                    step["outcomes"]
                    if "outcomes" in step
                    else {"complete": step["outcome"]}
                )
                    self.test_yaml_outcomes(f"parent_id.{stepID}", outcomes)
                
                if "percentage" in step:
                    if "value" not in step["percentage"]:
                        raise Exception(
                        f"StoryStep '{parent_id}.{stepID}' percentage missing value"
                    )
                    if "scale" not in step["percentage"]:
                        raise Exception(
                        f"StoryStep '{parent_id}.{stepID}' percentage missing value"
                    )
                    if "invert" in step["percentage"] and not isinstance(
                    step["percentage"]["invert"], bool
                ):
                        raise Exception(
                        f"StoryStep '{parent_id}.{stepID}' percentage has invalid invert flag"
                    )
        
        def test_yaml_outcomes(self, parent_id, outcomes):
            
            for outcomeID in outcomes.keys():
                try:
                    diff = set(outcomes[outcomeID].keys()) - self.STORY_OUTCOME_KEYS
                    if diff:
                        raise Exception(
                        f"StoryOutcome '{parent_id}.{outcomeID}' has unknown keys: {diff}"
                    )
                except Exception as e:
                    raise Exception(
                    f"StoryOutcome '{parent_id}.{outcomeID}' failed validation: {e}"
                )
        
        
        
        
        
        
        
        @staticmethod
        def self_test():
            if not config.developer:
                return
            for story in STORIES.values():
                story.self_test()
        
        
        
        def __getitem__(self, key):
            return store.STORIES[key]
        
        
        
        def process(self, skip_notify=False, debug=False):
            
            self.notifications = OrderedDict()
            for story in store.STORIES.values():
                if debug:
                    renpy.log(f"DEBUG: Checking story {story.id}")
                if story.inactive and story.test(debug):
                    story.activate(debug)
                    if debug:
                        renpy.log(f"DEBUG: Notifying for activation: {story.id}")
                    story.notify(StoryStatus.NOTIFY_NEW)
                
                if story.active:
                    if debug:
                        renpy.log(f"DEBUG: Processing active story {story.id}")
                    story.process(debug)
            
            
            if skip_notify:
                self.notifications = OrderedDict()
            for notification in self.notifications.values():
                game.notify(notification)
            
            
            if self.get_stories_status != self._cache.get("stories_status", set()):
                self.build_cache()
        
        def notify(self, id, string):
            if id not in self.notifications:
                self.notifications[id] = string
        
        
        
        @staticmethod
        def find(participant, status=None):
            if status is None:
                status = StoryStatus.ACTIVE
            retval = {}
            for id, story in store.STORIES.items():
                if story.status == status and (
                participant == "all"
                or (participant in story.participants)
                or (participant == story._type)
            ):
                    retval[id] = story
            return sort_dict(retval, lambda x: x[1].sort)
        
        @property
        def get_sorted_stories(self):
            types = (StoryStatus.ACTIVE, StoryStatus.COMPLETED)
            filters = ["all", "harem", "generic"] + self.participants
            return {
            (t_filter, t_type): dict(self.find(t_filter, t_type))
            for t_filter, t_type in itertools.product(filters, types)
        }
        
        
        
        @property
        def participants(self):
            
            
            return list(
            set(
                [
                    participant
                    for story in store.STORIES.values()
                    for participant in story.participants
                    if not story.inactive
                ]
            )
        )
        
        @property
        def get_sorted_participants(self):
            participants = {}
            available_participants = self.participants
            for pid, participant in STORY_PARTICIPANTS.items():
                if pid in available_participants:
                    if participant == "[hero.name]":
                        participants[pid] = hero.name
                    else:
                        participants[pid] = participant
            participants = sort_dict(participants, lambda x: x[1])
            return participants
        
        @property
        def get_stories_status(self):
            return {(story.id, story.status) for story in store.STORIES.values()}
        
        def build_cache(self):
            self._cache["stories_status"] = self.get_stories_status
            self._cache["participants"] = self.get_sorted_participants
            self._cache["stories"] = self.get_sorted_stories
            return
        
        def for_ui(self, filter, type, story):
            stories = self._cache.get("stories", {}).get((filter, type), {})
            if story not in stories and len(stories) > 0:
                story = next(iter(stories.items()))[0]
            return self._cache.get("participants", {}), stories, story
        
        def refresh(self, skip_notify=False):
            for story in STORIES:
                STORIES[story].status = 0
                for k, v in STORIES[story].steps.items():
                    v.status = 0
            self.process(skip_notify)
            for story in STORIES:
                STORIES[story].process()




    class StoryStatus:
        INACTIVE = 0
        ACTIVE = 1
        COMPLETED = 2
        HIDDEN = 3
        NOTIFY_NEW = 1
        NOTIFY_UPDATE = 2
        
        
        
        def __init__(self, parent, id, steps, outcomes):
            self.parent = parent
            if parent and hasattr(parent, "id"):
                id = parent.id + "." + id
            self.id = id
            self.steps = OrderedDict()
            self.outcomes = OrderedDict()
            
            for stepid, step in steps.items():
                self.steps[stepid] = StoryStep(self, stepid, step)
            for outcomeid, outcome in outcomes.items():
                self.outcomes[outcomeid] = StoryOutcome(self, outcomeid, outcome)
        
        def __getitem__(self, key):
            
            
            
            if key in self.outcomes:
                return self.outcomes[key]
            if key in self.steps:
                return self.steps[key]
            raise AttributeError(key)
        
        
        
        def get_property(self, propname, default=None):
            id = self.id + "." + propname
            if id in store.DATA_STORIES:
                return store.DATA_STORIES[id]
            else:
                return default
        
        def set_property(self, propname, value):
            id = self.id + "." + propname
            DATA_STORIES[id] = value
        
        
        
        @property
        def status(self):
            return self.get_property("status", store.StoryStatus.INACTIVE)
        
        
        
        @status.setter
        def status(self, value):
            self.set_property("status", value)
        
        
        
        @property
        def outcome(self):
            return self.get_property("outcome")
        
        
        
        @outcome.setter
        def outcome(self, value):
            self.set_property("outcome", value)
        
        
        
        @property
        def inactive(self):
            return self.status == StoryStatus.INACTIVE
        
        
        
        @property
        def active(self):
            return self.status == StoryStatus.ACTIVE
        
        
        
        @property
        def complete(self):
            return self.status == StoryStatus.COMPLETED
        
        
        
        @property
        def desc(self):
            if (
            self.complete
            and self.outcome
            and self.outcome in self.outcomes
            and self.outcomes[self.outcome].description is not None
        ):
                return self.outcomes[self.outcome].description
            else:
                return self.name
        
        
        
        @property
        def status_icon(self):
            if self.inactive:
                return None
            elif self.active:
                return self.active_icon
            elif (
            self.outcome
            and self.outcome in self.outcomes
            and self.outcomes[self.outcome].icon is not None
        ):
                return self.outcomes[self.outcome].icon
            elif self.complete:
                return "complete"
            else:
                return ""
        
        
        
        
        
        def complete_item(self, id=None, debug=False):
            if id is None:
                id = next(iter(self.outcome.keys()))
            if debug:
                renpy.log(f"DEBUG: Completing {self.id} with outcome {id}")
            outcome = self.outcomes[id]
            self.outcome = id
            self.status = (
            StoryStatus.HIDDEN
            if isinstance(outcome, StoryOutcome) and outcome.hide_story
            else StoryStatus.COMPLETED
        )
            if debug:
                renpy.log(
                f"DEBUG: Looking for next steps for outcome {id} - {outcome.next}"
            )
            for next in outcome.next:
                if next is not None:
                    self.activate_next_step(next, debug=debug)
            if outcome.trigger:
                exec(outcome.trigger)
            self.notify()
        
        
        
        
        
        
        
        
        
        def activate_next_step(self, id, debug=False):
            if debug:
                renpy.log(f"DEBUG: {self.id} Finding next step {id}")
            if (
            id == StoryOutcome.NEXTSTEP
            and hasattr(self, "parent")
            and self.parent is not None
        ):
                
                
                newid = self.parent.find_next_step(self.id.split(".")[-1])
                if newid:
                    id = newid
                    if debug:
                        renpy.log(f"DEBUG: Next step is {id}")
            
            if id in self.steps or id in self.outcomes:
                if debug:
                    renpy.log(
                    f"DEBUG: id ({id}) in self.steps ({self.steps}): {id in self.steps}, id ({id}) in self.outcomes ({self.outcomes}): {id in self.outcomes}"
                )
                self[id].activate(debug)
            elif hasattr(self, "parent") and self.parent is not None:
                if debug:
                    renpy.log(f"DEBUG: Activate parent next step {id} - {self.parent}")
                self.parent.activate_next_step(id, debug=debug)
            else:
                if debug:
                    renpy.log("DEBUG: Cannot find next step.")
        
        
        
        def find_next_step(self, step):
            found = False
            for key in self.steps.keys():
                if key == step:
                    found = True
                elif found:
                    return key
            return False
        
        
        
        def process(self, debug=False):
            notified = False
            if debug:
                renpy.log(f"DEBUG: Processing steps and outcomes for {self.id}")
            if self.active:
                if debug:
                    renpy.log(f"DEBUG: Processing children for active {self.id}")
                for id, step in self.steps.items():
                    if (
                    step.inactive
                    and isinstance(step, StoryConditions)
                    and step.test(debug)
                ):
                        
                        
                        
                        step.activate(debug)
                        
                        if not notified:
                            self.notify()
                            notified = True
                    if step.active:
                        step.process(debug)
                    if step.active and step.toggle and not step.test(debug):
                        step.deactivate()
                if debug:
                    renpy.log(f"DEBUG: Processing outcomes for active {self.id}")
                for id, outcome in self.outcomes.items():
                    if outcome.test(debug):
                        if debug:
                            renpy.log(f"DEBUG: Outcome passed: {id}")
                        self.complete_item(id, debug)
                        
                        break
        
        
        
        def self_test(self):
            if isinstance(self, StoryConditions):
                
                StoryConditions.self_test(self)
            for step in self.steps.values():
                step.self_test()
            for outcome in self.outcomes.values():
                outcome.self_test()
        
        
        
        
        def activate(self, debug=False):
            
            if not self.inactive:
                return
            if debug:
                renpy.log(f"DEBUG: Activating {self.id}")
            self.status = StoryStatus.ACTIVE
            for start in self.start:
                if start and start in self.steps:
                    self[start].activate(debug)
        
        def deactivate(self, debug=False):
            if self.inactive:
                return
            
            if debug:
                renpy.log(f"DEBUG: Deactivating {self.id}")
            self.status = StoryStatus.INACTIVE
            for start in self.start:
                if start and start in self.steps:
                    self[start].deactivate()
        
        
        
        @staticmethod
        def find_outcomes(id, data):
            if "outcome" in data and "outcomes" in data:
                raise Exception("Cannot have both outcome and outcomes")
            elif "outcome" in data:
                return {"complete": data["outcome"]}
            elif "outcomes" in data:
                return data["outcomes"]
            else:
                raise Exception(id + " must have outcome or outcomes.")
        
        def notify(self, code=None):
            if code is None:
                code = StoryStatus.NOTIFY_UPDATE
            
            
            if hasattr(self, "parent") and self.parent is not None:
                self.parent.notify(code)




    class StoryConditions:
        def __init__(self, conditions):
            self.conditions = force_list(conditions)
        
        def test(self, debug=False):
            if debug:
                renpy.log(f"DEBUG: Testing {self.id}")
            for c in self.conditions:
                if debug:
                    renpy.log(f"DEBUG: Eval condition: {c}")
                try:
                    if c != True and (
                    c is None or c == False or not eval(c, locals=locals())
                ):
                        if debug:
                            renpy.log(f"DEBUG: Failed condition: {c}")
                        return False
                except Exception as e:
                    
                    raise Exception("Error in condition", self.id, c, e)
            if debug:
                renpy.log(f"DEBUG: Passed {self.id}")
            return True
        
        
        
        def self_test(self):
            for c in self.conditions:
                try:
                    if not isinstance(c, bool) and c is not None:
                        eval(c, locals=locals())
                except Exception as e:
                    
                    raise Exception("Error in condition", self.id, c, e)
        
        
        
        @staticmethod
        def find_conditions(data, required=False):
            if "condition" in data and "conditions" in data:
                raise Exception("Both condition and conditions")
            elif "condition" in data and "conditions" not in data:
                return force_list(data["condition"])
            elif "conditions" in data:
                return force_list(data["conditions"])
            elif required:
                raise Exception("Require conditions, none specified")
            else:
                return [None]


    class Story(StoryStatus, StoryConditions):
        
        
        def __init__(self, id, data):
            try:
                StoryStatus.__init__(
                self, None, id, data["steps"], self.find_outcomes(id, data)
            )
                StoryConditions.__init__(self, self.find_conditions(data))
                
                if not isinstance(data["name"], basestring):
                    
                    self.names = [
                    StoryName(self, idx, name)
                    for (idx, name) in enumerate(data["name"])
                ]
                else:
                    self.names = [StoryName.always(self, data["name"])]
                self._display_name = data.get("display_name")
                self.wiki_link = data.get("wiki_link")
                self.extra_data = data.get("extra_data")
                
                if not isinstance(data["description"], basestring):
                    self.descriptions = [
                    StoryDescription(self, idx, desc)
                    for (idx, desc) in enumerate(data["description"])
                ]
                else:
                    self.descriptions = [StoryDescription.always(self, data["description"])]
                self.short = data.get("short", False)
                self.participants = (
                force_list(data["participants"]) if "participants" in data else []
            )
                self._sort = data.get("sort")
                self._type = data.get("type", "npc")
                
                self.start = (
                force_list(data["start"])
                if "start" in data
                else [next(iter(self.steps.keys()))]
            )
            except Exception as e:
                raise Exception("Error creating story " + id, e)
        
        
        
        @property
        def desc(self):
            possible = [desc for desc in self.descriptions if desc.test()]
            return str(possible[0]) if possible else ""
        
        
        
        @property
        def name(self):
            if self._display_name:
                return Text(self._display_name).get_all_text()
            possible = [name for name in self.names if name.test()]
            return str(possible[0]) if possible else "Unnamed Story"
        
        
        
        @property
        def sort(self):
            return self._sort if self._sort else self.name
        
        
        
        def notify(self, code=None):
            string = False
            id = self.id
            name = self.short if self.short else self.name
            if code == StoryStatus.NOTIFY_NEW:
                id += "new"
                string = "{image=gui/icons/icon_story_new.png} " + name
            elif self.active:
                id += "new"
                string = "{image=gui/icons/icon_story_update.png} " + name
            elif self.complete:
                id += "completed"
                string = "{image=gui/icons/icon_story_complete.png} " + name
            if string:
                storytracker.notify(id, "{size=20}" + string + "{/size}")


    class StoryStep(StoryStatus, StoryConditions):
        
        
        def __init__(self, parent, id, data):
            try:
                steps = data["steps"] if "steps" in data else OrderedDict()
                StoryStatus.__init__(self, parent, id, steps, self.find_outcomes(id, data))
                StoryConditions.__init__(self, self.find_conditions(data))
                self.name = data["name"]
                self.hidden = data.get("hidden", False)
                self.percentage = data.get("percentage", None)
                
                if self.percentage and "invert" not in self.percentage:
                    self.percentage["invert"] = False
                self.active_icon = data.get("icon", "active")
                
                self.start = (
                force_list(data["start"])
                if "start" in data
                else force_list(list(self.steps.keys()))
            )
                self.optional = data.get("optional", False)
                self.toggle = data.get("toggle", False)
                self.related_event = data.get("related_event", False)
            
            except Exception as e:
                raise Exception(parent.id + "." + id, e)
        
        
        
        
        
        @property
        def hide(self):
            try:
                return self.hidden or (self.complete and self.outcomes[self.outcome].hide)
            except KeyError:
                raise Exception(self.id + " - Bad Outcome: " + str(self.outcome))
        
        @property
        def percentage_for_ui(self):
            scale = float(safe_eval(self.percentage["scale"]))
            value = float(safe_eval(self.percentage["value"]))
            if self.percentage["invert"]:
                value = abs(scale - value)
            percent = max(0, min(100, int(value / scale * 100)))
            return percent


    class StoryOutcome(StoryConditions):
        
        NEXTSTEP = -1
        
        
        
        def __init__(self, parent, id, data):
            self.parent = parent
            self.id = parent.id + "." + id
            self._id = id
            StoryConditions.__init__(self, self.find_conditions(data))
            self.description = data["description"] if "description" in data else None
            self.icon = data["icon"] if "icon" in data else None
            self.next = (
            force_list(data["next"]) if "next" in data else [StoryOutcome.NEXTSTEP]
        )
            self.hide = data["hide"] if "hide" in data else False
            self.hide_story = data["hide_story"] if "hide_story" in data else False
            self.trigger = data["trigger"] if "trigger" in data else False
            
            difference = set(data.keys()) - {
            "condition",
            "conditions",
            "description",
            "icon",
            "next",
            "hide",
            "hide_story",
            "trigger",
        }
            if difference:
                raise Exception(
                "Outcome " + self.id + " has wrong keys. Did you mean outcomes?",
                difference,
            )
        
        
        
        def activate(self, debug=False):
            self.parent.complete_item(self._id, debug)




    class StoryDescription(StoryConditions):
        def __init__(self, parent, index, data):
            StoryConditions.__init__(self, self.find_conditions(data))
            self.description = data["description"] if "description" in data else None
            self.id = parent.id + ".description." + str(index)
            self.parent = parent
        
        def __str__(self):
            return self.description
        
        @staticmethod
        def always(parent, desc):
            return StoryDescription(
            parent, 0, {"description": desc, "conditions": ["True"]}
        )




    class StoryName(StoryConditions):
        def __init__(self, parent, index, data):
            StoryConditions.__init__(self, self.find_conditions(data))
            self.name = data.get("name")
            self.id = f"{parent.id}.name.{index}"
            self.parent = parent
        
        def __str__(self):
            return self.name
        
        @staticmethod
        def always(parent, name):
            return StoryName(parent, 0, {"name": name, "conditions": ["True"]})




    class Line(renpy.Displayable):
        def __init__(self, color, startpos, endpos, width=1, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)
            self.color = color
            self.startpos = startpos
            self.endpos = endpos
            self.width = width
        
        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            c = rv.canvas()
            c.line(self.color, self.startpos, self.endpos, self.width)
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
