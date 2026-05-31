











init -900 python:

    from itertools import cycle









    DEBUG_FILES = []


    def capwords(text):
        
        return " ".join([x.capitalize() for x in text.split(" ")])


    def sort_dict(input_dict, sort_func):
        from collections import OrderedDict
        
        return OrderedDict(sorted(input_dict.items(), key=sort_func))


    def force_list(val):
        """
    Take anything that is not a list, and wrap it in a list
    """
        if not isinstance(val, base_list):
            return [val]
        else:
            return val


    def safe_eval(c):
        if isinstance(c, (float, int, bool)):
            return c
        try:
            return eval(c)
        except Exception as e:
            if config.developer:
                raise Exception("Invalid Condition: " + str(c) + "\n" + str(e))
            return False


    def find_next(c, lst):
        elems = cycle(lst)
        for elem in elems:
            if elem == c:
                next_elem = next(elems)
                return next_elem
        return None


    def find_prev(c, lst):
        if isinstance(lst, set):
            lst = list(lst)
        return find_next(c, list(reversed(lst)))



init -100 python:




    from yaml import SafeLoader


    class OrderedLoader(SafeLoader):
        def construct_ordered_mapping(self, node, deep=False):
            from collections import OrderedDict
            
            SafeLoader.flatten_mapping(self, node)
            return OrderedDict(SafeLoader.construct_pairs(self, node, deep))
        
        def __init__(self, stream):
            SafeLoader.__init__(self, stream)



    OrderedLoader.add_constructor(
    OrderedLoader.DEFAULT_MAPPING_TAG, OrderedLoader.construct_ordered_mapping
)


    def load_yamls(matcher_func, clazz, **kwargs):
        """
    Scans the list of files known to RenPy, and for any that match, instantiate a class with the data.
    Returns a tuple of id and the new object for use elsewhere for each discovered yaml_file.

    This is a generator function, so it should be used as `for (id, obj) in load_yamls` or in list comprehension []

    This function assumes the following:
        - Filename, without extensions is the id, by default
        - If id is in the data, it will use that instead
        - If the YAML contains the 'class' key, it will use that for the class instead
        - If clazz is None, we will return the OrderedDict directly
        - The class to instantiate has one of these constructors:
            - (id, data) - (Default)
            - (**kwargs)
        - You can use the kwargs constructor if you specify params="kwargs" to load_yamls
        - You can load a list from a yaml yaml_file if you use filetype="list" to load_yamls
            - In this mode, you will get a list of Class.
    """
        import os
        
        def read_data(yaml_file):
            with renpy.file(yaml_file) as stream:
                
                try:
                    return yaml.load(stream, OrderedLoader)
                except ParserError as e:
                    raise ParserError(f"Issue with yaml_file: {yaml_file}") from e
        
        def construct_obj(clazz, args, kwargs):
            
            if clazz is None:
                return kwargs
            else:
                
                return clazz(*args, **kwargs)
        
        
        params = kwargs["params"] if kwargs and "params" in kwargs else "legacy"
        filetype = kwargs["filetype"] if kwargs and "filetype" in kwargs else "each"
        files = [f for f in renpy.list_files() if matcher_func(f)]
        for file in files:
            data = read_data(file)
            if filetype == "each":
                
                try:
                    id = (
                    data["id"]
                    if "id" in data
                    else os.path.splitext(os.path.basename(file))[0]
                )
                except TypeError:
                    renpy.log(f"Issue while reading {file}")
                    raise
                
                c = globals()[data["class"]] if "class" in data else clazz
                
                if params == "kwargs" or clazz is None:
                    data["id"] = id
                    obj = construct_obj(c, [], data)
                else:
                    obj = construct_obj(c, [id, data], {})
                yield (id, obj)
            elif filetype == "list":
                
                for item in data:
                    c = globals()[item["class"]] if "class" in item else clazz
                    yield (item["id"], construct_obj(c, [], item))







    def conditional_choice_picker(choices):
        chats = []
        for label, data in choices.items():
            if data[0] == True or safe_eval(data[0]):
                for i in range(0, data[1]):
                    chats.append(label)
        return randchoice(chats)




    def day_chooser(hour=None):
        choices = []
        for i in range(1, 7):
            day = game.week_day + i
            if day > 7:
                day -= 7
            if not hero.calendar.has_appointment(game.days_played + i, hour):
                if i == 1:
                    choices.append(("Tomorrow", (game.days_played + i, day)))
                else:
                    choices.append(
                    (
                        "Next " + game.get_day_str(day).capitalize(),
                        (game.days_played + i, day),
                    )
                )
        
        return renpy.display_menu(choices)


    position_123people = [[[center]], [[left], [right]], [[left], [center], [right]]]






    def show123people(always, extra=None, expression=None, extra_expression=None):
        if extra is None:
            extra = []
        always_id = [get_person_id(x) for x in always]
        extra_id = [get_person_id(x) for x in extra]
        
        if extra_expression is None:
            extra_expression = expression
        
        
        while len(always_id + extra_id) > 3:
            if extra_id:
                extra_id.remove(randchoice(extra_id))
            else:
                always_id.remove(randchoice(always_id))
        
        always_image = [
        (p, " ".join([p, expression]))
        if expression and renpy.has_image(" ".join([p, expression]))
        else (p, p)
        for p in always_id
    ]
        extra_image = [
        (p, " ".join([p, extra_expression]))
        if extra_expression and renpy.has_image(" ".join([p, extra_expression]))
        else (p, p)
        for p in extra_id
    ]
        
        shown_images = always_image + extra_image
        shown_people = set()
        renpy.random.shuffle(shown_images)
        for idx, (p, image_name) in enumerate(shown_images):
            shown_people.add(p)
            renpy.show(image_name, at_list=position_123people[len(shown_images) - 1][idx])
        
        return [Person.find(p) for p in shown_people]


    def search_in_path(filename="environment.txt"):
        
        if not filename:
            return None
        paths = [renpy.config.basedir, renpy.config.savedir]
        
        alt_path = os.path.abspath("renpy_base")
        if ".app" in alt_path:
            paths.append(alt_path[: alt_path.find(".app") + 4])
        positive_results = set()
        for i in paths:
            print(f"Looking for {filename} in {i}")
            if os.path.isfile(os.path.join(i, "environment.txt")):
                positive_results.add(i)
        
        print(f"Found {filename} in {positive_results}")
        return positive_results



init -9 python:



    KEY_TO_NICKNAME = {
    "Mister hero.family_name": lambda: f"Mister {hero.family_name}",
    "Miss hero.family_name": lambda: f"Miss {hero.family_name}",
    "hero.family_name": lambda: hero.family_name,
    "heroname": lambda: heroname,
}


    def get_hero_nickname(person_name):
        """
    Retrieves a nickname for a given person, based on 'COMMON_HERO_NICKNAME' and conditions specified in 'person.heronickname'.
    """
        person = Person.find(person_name)
        if not person or not isinstance(person.heronickname, OrderedDict):
            return heroname
        
        
        for k, v in COMMON_HERO_NICKNAME.items():
            if hero.gender == "female" and person.flags.breeNickname == v:
                return COMMON_HERO_NICKNAME[k]
            elif hero.gender == "male" and person.flags.mikeNickname == v:
                return COMMON_HERO_NICKNAME[k]
        
        
        
        for k, v in person.heronickname.items():
            if safe_eval(v):
                
                if KEY_TO_NICKNAME.get(k):
                    return KEY_TO_NICKNAME[k]()
                
                else:
                    return k
        else:
            
            return heroname



init python:



    def get_string_size_in_pixel(string, font_name=gui.text_font, font_size=gui.text_size):
        """
    Returns, width, height of a string in pixels.
    """
        
        string = string.replace("[", "[[").replace("]", "]]")
        return Text(string, substitute=True, font=font_name, size=font_size).size()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
