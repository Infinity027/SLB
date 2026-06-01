init -999:
    define base_list = list.__bases__[0]

init -100:
    define config.save_token_keys = [
                                    'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE4gM1qJt/k86hBLkoVuv3U5n3toTB+g6rtWRGNbvjhGhYhBotT5A0hFayPBXCW7ICRaCqus9gE1xmgk44igR7yg==', 
                                    'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEOM0mDVcnhy5KygRu/CLgxV+mPM2HkI8hllMOJkQSji+mt9NxRDgtA5i+NFa92vkeiUogrcO7byLY0QqbGsh4kg==', 
                                    'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEg10nhBZw/Zt2NmBHR7MKwP/oZPG7NAPPOmDoFkCp3qPXdMDieh1kz05ks7S0GUeFBo7s7/h6zyQSPiz9FjTxcw==', 
                                    ]
    define config.font_name_map["palanquin_bold"] = "gui/fonts/Palanquin_Dark/PalanquinDark-Bold.ttf"
    define config.font_name_map["palanquin_medium"] = "gui/fonts/Palanquin_Dark/PalanquinDark-Medium.ttf"
    define config.font_name_map["palanquin_regular"] = "gui/fonts/Palanquin_Dark/PalanquinDark-Regular.ttf"

    define config.font_name_map["exo2_regular"] = "gui/fonts/Exo_2/Exo2-Regular.ttf"
    define config.font_name_map["exo2_light"] = "gui/fonts/Exo_2/Exo2-Light.ttf"
    define config.font_name_map["exo2_bold"] = "gui/fonts/Exo_2/Exo2-Bold.ttf"

    define config.layers = ['master', 'fx', 'gallery', 'transient', 'screens', 'ui', 'namebox',  'overlay']

    define config.audio_directory = 'sd'

    define SEASONS = ["spring", "summer", "fall", "winter"]
    define DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    default LAST_HEARTBEAT = 0


    define MAX_LES_GUY_DATE = 18
    define MAX_LES_GUY_KISS = 16
    define MAX_LES_GUY_SEX = 12
    define MIN_LES_GIRL_SEX = 8
    define MIN_LES_GIRL_KISS = 4
    define MIN_LES_GIRL_DATE = 2
    define DECAY_PENALTY_MODIFIER = .25
    define GAIN_PENALTY_MODIFIER = .25


    define randint = renpy.random.randint
    define randchoice = renpy.random.choice
    define random = renpy.random.random

    default NOTIFICATIONS = []
    default COUNTERS = {}
    default STORY_HOLD = False

    define YAML_SKILLS = {}
    default DATA_SKILLS = {}

    define GALLERY_MODE = False
    define GALLERY = {}
    define HAREMS = {}
    define YAML = {}
    define MOVIES = {}

    default _portal_token = None

    define DLCS = {}


    define MC_DUPLICATES_PREFIXES = {'tattooparlor_': None,
                                     'bree_spoon': ('scottie',),
                                     'bree_titfuck': None,
                                     }

    default GALLERY_WARNING = False
    default GALLERY_ID = 'aletta'
    define ORIGINAL_PATCHED_VALUES = {}

    default FULL_SPOILERS = True

    define IN_EVENT_WITH = ""

    default DATA_GAME = {
        "days_played": 0,
        "hour": 10,
        "season": 1,
        "day": 5,
        "week": 1,
        "week_day": 1,
        "room": "office",
        "from_room": "livingroom"
    }

    define COMMON_HERO_NICKNAME = {}

    define anim_tag = []

init -100 python:
    import locale
    import copy
    import yaml
    import itertools
    import time
    import re

    config.auto_voice = "vo/{id}.ogg"
    FLAGS = {}
    DATES = {}

    HIDDEN = []
    HIDE_UI = False

    gallery_cg_items = []

    enable_debug_picker = False

    if not persistent.set_default:
        persistent.difficulty = 0
        persistent.notifications = True
        persistent.schedule_randomness = False
        persistent.needs_randomness = False
        persistent.choices_shuffle = True
        persistent.skip_tutorial = False
        persistent.fast = True
        persistent.room_display = "h"
        persistent.window_opacity = 1.0
        persistent.set_default = True
        persistent.pregnancy_end = True
        persistent.pregnancy_notification = True
        persistent.mute_characters = False
        persistent.tts_override = False
        persistent.selector = True
        persistent.new_ui = True

    # LIVE2D DISABLED — characters always render as static sprites, never animated.
    # Forced off every launch (overrides any saved value). To restore, revert to:
    # persistent.live2d_on = renpy.has_live2d() if persistent.live2d_on is None else persistent.live2d_on
    persistent.live2d_on = False

    def display_notifications():
        import re
        if not renpy.get_screen("notification_wave") and NOTIFICATIONS:
            for n in NOTIFICATIONS:
                
                n[0] = re.sub(r'=ui/', '=gui/', n[0])
                n[0] = re.sub(r'gui/icon_', 'gui/icons/icon_', n[0])
            renpy.show_screen("notification_wave", notifs=NOTIFICATIONS[-8:])

    def clean_notifications():
        global NOTIFICATIONS
        tmp_notifications = [
        [n_text, n_duration - 1]
        for n_text, n_duration in NOTIFICATIONS
        if n_duration - 1 != 0
    ]
        if tmp_notifications != NOTIFICATIONS:
            NOTIFICATIONS = tmp_notifications
            renpy.restart_interaction()

    def remove_notification(notification_text):
        global NOTIFICATIONS
        tmp_notifications = []
        removed = False
        for n_text, n_duration in NOTIFICATIONS:
            if n_text == notification_text and not removed:
                removed = True
                continue
            tmp_notifications.append([n_text, n_duration])
        
        if tmp_notifications != NOTIFICATIONS:
            NOTIFICATIONS = tmp_notifications
            renpy.restart_interaction()

    def find_full_day_name(day_fragment):
        matching_days = [day for day in DAYS if day.startswith(day_fragment.lower())]
        
        if matching_days:
            return matching_days
        else:
            return ""

init -11:

    default DATA_HERO = {
        "name": "Unnamed",
        "family_name": "Hero",
        "mc_gender": "male",
        "birthday": 0,
        "status": "single",
        "age": 25,
        "equipment": {"clothes": None, "accessory": None},
        "inventory": {},
        "skills": {},
        "smartphone_contacts": [],
        "activity": "",
        "calendar": Calendar(),
        "talk_subjects": sorted(GenericTalkSubject.all(), key=lambda x: x.display_name),
        "piercings": Piercings("hero", {}),

    }

init -10:
    define game = Game()
    define hero = Hero()

define bree_sasha = Character("[bree.name]/Sasha", who_outlines=[(1, "#FF00FF")], who_color="#ffffff", voice_tag="bree_sasha")
define breesdad = Character("[bree.name]'s dad", who_outlines=[(1, "#0099ff")], who_color="#ffffff", voice_tag="breesdad")
define thug_name = "Thug"
define thug_say = DynamicCharacter("thug_name")




default DATA_WRAPPERS = {}
define active_girl = PersonWrapper("active_girl")
define date_girl = PersonWrapper("date_girl")
define interact_girl = PersonWrapper("interact_girl")
define smartphone_girl = PersonWrapper("smartphone_girl")

init -10 python:
    renpy.dynamic("id", "person", "harem", "skill", "movie", "f")


    for id, person in load_yamls(
    lambda f: f.endswith(".yml") and "ch" in f and "person/" in f, Girl
):
        
        
        exec("{} = Person.find('{}')".format(id, id))
        STORY_PARTICIPANTS[id] = person.name

    if demo:
        for id, harem in load_yamls(
        lambda f: f.endswith("/harem_demo.yml") and "ch" in f,
        Harem,
        filetype="list",
        params="kwargs",
    ):
            HAREMS[id] = harem
    else:
        for id, harem in load_yamls(
        lambda f: f.endswith("/harem.yml") and "ch" in f,
        Harem,
        filetype="list",
        params="kwargs",
    ):
            HAREMS[id] = harem

    for id, skill in load_yamls(
    lambda f: f.endswith(".yml") and "hero_skills" in f,
    TrainableSkill,
    filetype="list",
    params="kwargs",
):
        YAML_SKILLS[id] = skill


    for id, movie in load_yamls(
    lambda f: f.endswith(".yml") and "movies" in f,
    Movie,
    filetype="list",
    params="kwargs",
):
        MOVIES[id] = movie

    STORY_PARTICIPANTS["office"] = "Office"
    STORY_PARTICIPANTS["hero"] = "[hero.name]"

init -30 python:
    import re
    import imagesize
    import glob
    from collections import defaultdict
    from pathlib import Path
    import json


    with renpy.file("ch/common_hero_nickname.yml") as file:
        COMMON_HERO_NICKNAME = yaml.safe_load(file).get("common_heronickname", "")

    renpy.dynamic("files", "id", "people_ids", "f", "name", "img_name", "img_path", "split_path", "split_name", "size", "mc_name", "folder_name", "ch_name", "anims", "is_sprite", "expressions", "info", "anims_params", "attrs", "g", "r", "prefs", "pref", "s")

    files = renpy.list_files()
    rooms_temp = {}


    re_peoples = re.compile(r"(?:.+\/)?ch\/\w+\/person\/(\w+)\.yml")
    people_ids = []


    re_bg = re.compile(r"(?:.+\/)?bg\/(?:.+\/)?(\w+)\.(?:webp|png)")
    bg_files = []

    re_ch = re.compile(r"(?:.+\/)?ch\/(?:.+\/)?([\w-]+)\.webp")
    ch_files = []

    re_action_icons = re.compile(r".+\/action_icons\/(\w+)\.png")
    re_talk_icons = re.compile(r".+\/talk_icons\/(\w+)\.png")

    anim_files = defaultdict(list)

    for f in files:
        m = re_peoples.match(f)
        if m:
            people_ids.append(m.group(1))
            continue
        
        m = re_bg.match(f)
        if m:
            bg_files.append((m.group(1), m.group(0)))
            continue
        
        m = re_ch.match(f)
        if m:
            ch_files.append((m.group(1), m.group(0)))
            continue
        
        if "/st2_anim/" in f:
            folder_name = "/".join(f.split("/")[:5])
            anim_files[folder_name].append(f)
            ch_name = folder_name.split("/")[2]
            if not ch_name in anim_tag:
                anim_tag.append(ch_name)
            continue



    for img_name, img_path in bg_files:
        name = img_name.split("_")
        if "button" not in name:
            if name[0] not in rooms_temp:
                if "season" in name:
                    rooms_temp[name[0]] = {}
                    rooms_temp[name[0]]["day_night"] = True
                    rooms_temp[name[0]]["seasons"] = True
                    rooms_temp[name[0]]["custom"] = True
                elif len(name) == 1:
                    rooms_temp[name[0]] = {}
                    rooms_temp[name[0]]["day_night"] = False
                    rooms_temp[name[0]]["seasons"] = False
                elif len(name) == 2:
                    if name[1] in ["day", "night"]:
                        rooms_temp[name[0]] = {}
                        rooms_temp[name[0]]["day_night"] = True
                        rooms_temp[name[0]]["seasons"] = False
                    elif name[1] in ["0", "1", "2", "3"]:
                        rooms_temp[name[0]] = {}
                        rooms_temp[name[0]]["day_night"] = False
                        rooms_temp[name[0]]["seasons"] = True
                elif (
                len(name) == 3
                and name[1] in ["0", "1", "2", "3"]
                and name[2] in ["day", "night"]
            ):
                    rooms_temp[name[0]] = {}
                    rooms_temp[name[0]]["day_night"] = True
                    rooms_temp[name[0]]["seasons"] = True
            if rooms_temp.get(name[0]) and rooms_temp[name[0]].get("custom", False):
                name = ["bg"] + name
        renpy.image("_".join(name), img_path)

    for ch_file in ch_files:
        (img_name, img_path) = ch_file
        split_path = img_path.split("/")
        if "ev2" in split_path:
            renpy.image(img_name, img_path)
            
            for cg_prefix in MC_DUPLICATES_PREFIXES:
                if img_name.startswith(cg_prefix):
                    suffixes = MC_DUPLICATES_PREFIXES[cg_prefix]
                    split_name = img_name.split("_")
                    if suffixes:
                        for suffix in suffixes:
                            mc_image = [f"{split_name[0]}mc"]
                            mc_image.append(suffix)
                            mc_image.extend(split_name[1:])
                            mc_image = "_".join(mc_image)
                            renpy.image(mc_image, img_path)
                    else:
                        mc_image = [f"{split_name[0]}mc"]
                        mc_image.extend(split_name[1:])
                        mc_image = "_".join(mc_image)
                        renpy.image(mc_image, img_path)
        elif "st2" in split_path or "st" in split_path:
            
            
            
            
            
            
            size = (0, 0)
            if img_path.endswith(".webp") or img_path.endswith(".png"):
                try:
                    with renpy.file(img_path) as fio:
                        size = imagesize.get(fio)
                except Exception:
                    renpy.log(f"Img load issue with {img_name}")
            split_name = img_name.split("_")
            
            if size[0] == 1280:
                renpy.image(img_name, Transform(img_path, zoom=0.5))
                name = "_".join(split_name[:1] + ["close"] + split_name[1:])
                renpy.image(name, img_path)
                
                if split_name[0] in ["bree", "mike"]:
                    mc_name = f"{split_name[0]}mc"
                    img_name = "_".join([mc_name] + split_name[1:])
                    renpy.image(img_name, Transform(img_path, zoom=0.5))
            else:
                renpy.image(img_name, img_path)
                
                if split_name[0] in ["bree", "mike"]:
                    mc_name = f"{split_name[0]}mc"
                    img_name = "_".join([mc_name] + split_name[1:])
                    renpy.image(img_name, img_path)
        else:
            name = tuple(img_name.split("_"))
            renpy.image(name, img_path)



    if renpy.has_live2d():
        for anims in anim_files:
            
            is_sprite = True if "/st2_anim" in anims else False
            
            expressions = []
            info = None
            
            name = " ".join(anims.split("/")[-1].split("_"))
            name = (name + " anim") if is_sprite else ("cg anim " + name)
            
            if not getattr(store, name.replace(" ", "_") + "_filter"):
                continue
            
            for f in anim_files.get(anims):
                if f.endswith('exp3.json'):
                    expressions.append(Path(f).stem.split(".")[0])
                elif f.endswith('/info.json'):
                    info = json.load(renpy.file(f))
            
            anims_params = dict(
            zoom=info.get('zoom', None) if info else None,
            top=info.get('top', 0.0) if info else 0.0,
            base=info.get('base', 1.0) if info else 1.0,
            height=info.get('height', 1.0) if info else 1.0,
            loop=True,
            nonexclusive=expressions,
            seamless=True,
            default_fade=0.0,
            attribute_filter=getattr(store, name.replace(" ", "_") + "_filter"),
            xoffset=info.get('xoffset', 0) if info else 0,
            yoffset=info.get('yoffset', 0) if info else 0,
        )
            if info and 'xalign' in info:
                anims_params['xalign'] = info.get('xalign')
            if info and 'yalign' in info:
                anims_params['yalign'] = info.get('yalign')
            
            renpy.image(name, Live2D(anims, **anims_params))

    for f in files:
        m_action = re_action_icons.match(f)
        m_talk = re_talk_icons.match(f)
        if m_action:
            attrs = []
            attrs.append(Condition("True", "gui/icons/icon_bg.png"))
            attrs.append(Condition("True", f, xpos=5, ypos=5))
            attrs.append(Attribute("fg", "idle", "gui/icons/icon_fg_idle.png"))
            attrs.append(Attribute("fg", "hover", "gui/icons/icon_fg.png"))
            attrs.append(Attribute("fg", "selected_idle", "gui/icons/icon_fg_idle.png"))
            attrs.append(Attribute("fg", "selected_hover", "gui/icons/icon_fg.png"))
            renpy.image(
            f.split("/")[-1].split(".")[0],
            LayeredImage(attrs, name=f.split("/")[-1].split(".")[0]),
        )
            g = f.split("/")[-1].split(".")[0].split("_")[-1]
            if g in people_ids:
                renpy.image(f"sayicon {g}", Transform(f, maxsize=(40, 40)))
            renpy.image(f"notify {g}", Transform(f, maxsize=(25, 25)))
        elif m_talk:
            attrs = []
            attrs.append(Condition("True", "gui/icons/icon_bg.png"))
            attrs.append(Condition("True", f, xpos=5, ypos=5))
            attrs.append(Attribute("fg", "idle", "gui/icons/icon_fg_idle.png"))
            attrs.append(Attribute("fg", "hover", "gui/icons/icon_fg.png"))
            renpy.image(
            f.split("/")[-1].split(".")[0] + "_talk",
            LayeredImage(attrs, name=f.split("/")[-1].split(".")[0] + "_talk"),
        )

    for r in rooms_temp:
        prefs = ["button_"]
        if not rooms_temp[r].get("custom", False):
            prefs.append("")
        for pref in prefs:
            attrs = []
            if not rooms_temp[r]["day_night"] and not rooms_temp[r]["seasons"]:
                attrs.append(Condition("True", f"{pref}{r}"))
            elif not rooms_temp[r]["day_night"]:
                for s in range(4):
                    attrs.append(
                    Condition(f"game.season == {s}", f"{pref}{r}_{s}")
                )
            elif not rooms_temp[r]["seasons"]:
                attrs.append(
                Condition("game.hour >= 20 or game.hour <= 5", f"{pref}{r}_night")
            )
                attrs.append(
                Condition("not (game.hour >= 20 or game.hour <= 5)", f"{pref}{r}_day")
            )
            else:
                for s in range(4):
                    attrs.append(
                    Condition(
                        f"game.season == {s} and (game.hour >= 20 or game.hour <= 5)",
                        f"{pref}{r}_{s}_night",
                    )
                )
                    attrs.append(
                    Condition(
                        f"game.season == {s} and not (game.hour >= 20 or game.hour <= 5)",
                        f"{pref}{r}_{s}_day",
                    )
                )
            if pref == "button_":
                attrs.append(Attribute("fg", "hover", "gui/location_button_fg_hover.png"))
                attrs.append(Attribute("fg", "idle", "gui/location_button_fg_idle.png"))
                attrs.append(
                Attribute("fg", "insensitive", "gui/location_button_fg_insensitive.png")
            )
            renpy.image(
            f"{pref.replace('_', ' ')}bg {r}",
            LayeredImage(attrs, name=f"{pref.replace('_', ' ')}bg {r}"),
        )


    renpy.start_predict("gui/*.*")
    renpy.start_predict("button bg *")

init 5 python:
    
    BaseEvent.sort_registry(key=lambda x: x[1].priority, reverse=True)
    Activity.build_cache_by_room(key=lambda x: (x.order, x.display_name))
    
    def VerticalSwipe(_time, downward, _ramplen=8, _reverse=False):
        img = (
            "gui/transition/swipe_down_vertical.png"
            if downward
            else "gui/transition/swipe_up_vertical.png"
        )
        return ImageDissolve(img, _time, ramplen=_ramplen, reverse=_reverse)
    
    
    
    timelaps = ImageDissolve("gui/transition/timelaps.png", 0.75, ramplen=8)
    rtimelaps = ImageDissolve("gui/transition/timelaps.png", 0.75, ramplen=8, reverse=True)
    
    
    def Timelaps(_time, _ramplen=8, _reverse=False):
        return ImageDissolve(
            "gui/transition/timelaps.png", _time, ramplen=_ramplen, reverse=_reverse
        )
    
    
    
    screenshot = Fade(0.05, 0.05, 0.05, color="#fff")
    
    
    def Screenshot(_dissolve=0.05, _pause=0.05):
        return Fade(_dissolve, _pause, _dissolve, color="#fff")
    
    def calculate_font_size(container_width, text_length, initial_font_size):
        """
        calculate_font_size(320, len("It's a to long text messages"), 30)
        calculate_font_size(320, len("It's a to long text messages"), gui.text_properties().get("size"))
        """
        if text_length == 0:
            return initial_font_size
        
        
        char_width_estimate = initial_font_size * 0.63 
        
        
        adjusted_font_size = min(initial_font_size, (container_width / text_length) / char_width_estimate * initial_font_size)
        
        return int(adjusted_font_size)
    
    def text_tag_resize(old_text, container_width, initial_font_size=None):
        """
        text_tag_resize("It's a to long text messages", 270, 30)
        text_tag_resize("It's a to long text messages", 270)

        textbutton text_tag_resize("It's a to long text messages", 270) action [SetScreenVariable("str", "pressed")]
        """
        if initial_font_size is None:
            if gui:
                initial_font_size = gui.text_properties().get("size")
            else:
                initial_font_size = 22
        
        new_size = calculate_font_size(container_width, len(old_text), initial_font_size)
        return "{size=" + str(new_size) + "}" + str(old_text) + "{/size}" 
    
    def replace_tags_alt(text_value):
        import re
        modified_text = re.sub(r'\{image=gui/icons/icon_(\w+).png\}', r'\1', text_value)      
        modified_text = re.sub(r'gui/icons/icon_(\w+).png', r'\1', modified_text)             
        modified_text = re.sub(r'notify (\w+)', r'\1', modified_text)                   
        modified_text = re.sub(r'\{color=#\w+\}(.+?)\{/color\}', r'\1', modified_text)  
        return modified_text
    
    def story_step_alt(text_value):
        switch = {
            'complete': 'completed',
            'active': 'active',
            'fail': 'failed',
        }
        return switch.get(text_value, "unknown_value")

init python:
    import inspect
    import shutil
    import os

    def is_sub_screen(): 
        screens = ["game_save", "load", "preferences", "main_gallery", "warning_gallery", "help", "credits"]
        return any(renpy.get_screen(screen) for screen in screens)

    def is_input_screen(): 
        screens = ["get_surname_screen", "save_name_dialogue"]
        return any(renpy.get_screen(screen) for screen in screens)

    def move_rpa():
        if renpy.android:
            import android
            
            file_path = android.open_local_file()
            
            dest_dir = renpy.config.searchpath[-1] if renpy.config.searchpath else renpy.config.gamedir
            
            if file_path and (file_path.endswith(".rpa") or file_path.endswith(".rpy")):
                filename = os.path.basename(file_path)
                dest_path = os.path.join(dest_dir, filename)
                print(f"Moving file {file_path} to {dest_path}")
                shutil.copy(file_path, dest_path)
                renpy.utter_restart()


    def add_anim_attr(name):
        
        def no_prefix_exists(n):
            if len(n) < 2:
                return True
            return not any(renpy.has_image(n[:i], exact=True) for i in range(2, len(n) + 1))
        
        
        if persistent.live2d_on:
            if len(name) > 1 and name[1] == "close":
                anim_name = (*name[:2], "anim", *name[2:])
                if renpy.has_image(anim_name, exact=False):
                    return anim_name
            else:
                anim_name = (name[0], "anim", *name[1:])
                if renpy.has_image(anim_name, exact=False):
                    
                    if len(name) == 1 or no_prefix_exists(name):
                        return anim_name
        
        else:
            if "anim" in name:
                return tuple(n for n in name if n != "anim")
        
        return name


    def anim_attrs_filter(attrs, sgl_attrs, mult_attrs, prv_def_vals=[]):
        
        if not sgl_attrs:
            sgl_attrs = {}
        if not mult_attrs:
            mult_attrs = {}
        
        for attr in attrs:
            
            for attr_type, (current_value, possibilities) in sgl_attrs.items():
                if not current_value and attr in possibilities:
                    sgl_attrs[attr_type][0] = attr
                    break
            else:
                
                for attr_type, (current_value, possibilities) in mult_attrs.items():
                    if attr in possibilities and attr not in mult_attrs[attr_type][0]:
                        mult_attrs[attr_type][0].append(attr)
        
        
        for attr_type, (current_value, possibilities) in sgl_attrs.items():
            if not current_value and not attr_type in prv_def_vals:
                sgl_attrs[attr_type][0] = possibilities[0]
        
        
        if not "motions" in prv_def_vals and "motions" in mult_attrs:
            if not mult_attrs["motions"][0]:
                
                f_current = inspect.currentframe().f_back
                if f_current and f_current.f_code.co_name.endswith("_filter"):
                    correct_frame = f_current
                    
                    f_current = f_current.f_back
                    if f_current and f_current.f_code.co_name.endswith("_filter"):
                        correct_frame = f_current
                    
                    if not renpy.showing(correct_frame.f_code.co_name.replace("_", " ").rsplit(" ", 1)[0]):
                        mult_attrs["motions"][0].append(mult_attrs["motions"][1][0])
        
        
        return (sgl_attrs, mult_attrs)


    def filtered_attrs(*args):
        
        result = []
        
        for arg in args:
            if not arg:
                continue
            
            match arg:
                case str():
                    result.append(arg)
                case list() | set():
                    result.extend(filter(None, arg))
                case _:
                    raise TypeError(
                    f"{type(arg)} type of {arg} is not handled by `filtered_attrs`."
                )
        
        return tuple(dict.fromkeys(result))


init:
    default SAVE_VERSION = config.version

    define config.adjust_attributes = dict.fromkeys(anim_tag, add_anim_attr)
    define config.log_live2d_loading = True


    define nickname_master = ["Master", "master"]
    define nickname_daddy = ["Daddy", "daddy"]
    define nickname_sweetie = ["Sweetie", "sweetie"]
    define nickname_handsome = ["Handsome", "handsome"]
    define nickname_bro = ["Bro", "bro"]
    define nickname_stud = ["Stud", "stud"]
    define nickname_husband = ["Husband", "husband"]
    define nickname_sugar = ["Sugar", "sugar"]
    define nickname_honey = ["Honey", "honey"]

    transform notification_popout:
        on show:
            xanchor 0.0
            easein_back 1.0 xanchor 1.0
        on hide:
            easeout_back 1.0 xanchor 0.0
        on replaced:
            easeout_back 1.0 xanchor 0.0
    transform flip:
        xzoom -1
        xalign 0.5
        yalign 0.5

    transform vflip:
        yzoom -1
        xalign 0.5
        yalign 0.5

    transform vshake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

    transform hshake:
        ease .06 xoffset 24
        ease .06 xoffset -24
        ease .05 xoffset 20
        ease .05 xoffset -20
        ease .04 xoffset 16
        ease .04 xoffset -16
        ease .03 xoffset 12
        ease .03 xoffset -12
        ease .02 xoffset 8
        ease .02 xoffset -8
        ease .01 xoffset 4
        ease .01 xoffset -4
        ease .01 xoffset 0

    transform startle(speed=0.1, h=-20):
        yoffset 0
        yanchor 1.0
        easein speed yoffset h
        easeout speed yoffset 0

    transform stepback(speed=0.1, h=-20, v=-20):
        ease speed/2 xoffset h/2 yoffset v
        ease speed/2 xoffset h yoffset 0
        pause speed
        ease speed*2 xoffset 0

    transform backforth(speed=0.5, h=-20, v=-20):
        ease speed/3 xoffset h yoffset v
        pause speed/3
        ease speed/3 xoffset 0 yoffset 0

    transform onknees:
        yalign -0.7
        yanchor -1.0

    transform cleavage:
        yalign 0.5

    transform zoomAt(power=1, xypos=(640, 360)):
        zoom power
        xpos xypos[0]
        ypos xypos[1]

    transform bottom_to_top:
        yalign 1.0
        linear 5.0 yalign 0.0

    transform top_to_bottom:
        yalign 0.0
        linear 5.0 yalign 1.0

    transform top:
        yalign 0.0

    transform bottom:
        yalign 1.0

    transform left:
        xalign 0.25
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform right:
        xalign 0.75
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform middle:
        xalign 0.5
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform mostleft5:
        xalign 0.16
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform left5:
        xalign 0.33
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform right5:
        xalign 0.66
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform mostright5:
        xalign 0.83
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform mostleft4:
        xalign 0.20
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform left4:
        xalign 0.40
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform right4:
        xalign 0.60
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform mostright4:
        xalign 0.80
        yalign 1.0
        yanchor 1.0
        xanchor 0.5

    transform top_left:
        xalign 0.25
        yalign 0.0
        xanchor 0.5

    transform top_right:
        xalign 0.75
        yalign 0.0
        xanchor 0.5

    transform top_mostleft:
        xalign 0.16
        yalign 0.0
        xanchor 0.5

    transform top_mostright:
        xalign 0.83
        yalign 0.0
        xanchor 0.5

    transform slide(h=-60, s=2.0):
        ease s xoffset h
        ease s xoffset -h
        repeat

    transform vslide(v=-60, s=2.0):
        ease s yoffset v
        ease s yoffset -v
        repeat

    transform rotate45:
        rotate -45

    transform rotation(degree=0):
        rotate degree

    transform clock(s=1):
        linear s rotate 360
        linear 0 rotate 0
        repeat

    transform tr_room:
        on show:
            xpos 1280
            linear .25 xpos 0
        on hide:
            xpos 0
            linear .25 xpos 1280

    transform npc_info_old_ui:
        on show:
            xalign -0.5
            linear .25 xalign 0.1

    transform show_actions:
        on show:
            xpos -110
            linear .25 xpos 10
        on hide:
            alpha 100
            linear .25 alpha 0


    transform show_locations:
        on show:
            ypos 100
            linear .25 ypos 0
        on hide:
            alpha 100
            linear .25 alpha 0

    transform npc_info:
        on show:
            xalign 1.5
            linear .25 xalign 0.7

    transform npc_info_npc:
        on show:
            xalign 0.5
            linear .25 xalign 0.3

    transform move_align(pa=0.3, pb=0.5):
        on show:
            xalign pa
            linear .25 xalign pb

    transform xalign(x):
        xalign x


    transform tr_action_menu:
        on show:
            ypos 360
            linear .25 ypos 0

    transform tr_ui:
        on show:
            ypos -150
            linear .25 ypos 10
        on hide:
            ypos 10
            linear .25 ypos -150

    transform swing(zoomA=1.0, rotationA=5.0, zoomB=1.1, rotationB=-5.0, linearX=1.0):
        linear linearX zoom zoomA rotate rotationA
        linear linearX zoom zoomB rotate rotationB
        repeat

    transform ride(speed=0.1, h=-20):
        yoffset 0
        yanchor 1.0
        easein speed yoffset h
        easeout speed yoffset 0
        repeat

    transform zoom(power=1, duration=1):
        linear duration zoom power

    transform traveling(power=1, duration=1, xypos=(640, 360)):
        linear duration xpos xypos[0] ypos xypos[1] zoom power


    transform traveling_easeinZoom(power=1, duration=1, xypos=(640, 360)):
        parallel:
            linear duration xpos xypos[0] ypos xypos[1]
        parallel:
            easein duration zoom power

    transform traveling_easeoutZoom(power=1, duration=1, xypos=(640, 360)):
        parallel:
            linear duration xpos xypos[0] ypos xypos[1]
        parallel:
            easeout duration zoom power



    transform blur(val=8):
        blur val

    transform opacity(val=0.5):
        alpha val

    transform flicker(duration=3):
        alpha 0
        block:
            linear duration alpha 1
            linear duration alpha 0
            repeat

    transform sepia:
        matrixcolor SepiaMatrix()

    transform grey:
        matrixcolor SaturationMatrix(0)

    transform blacker:
        matrixcolor TintMatrix("#000")

    transform dark:
        matrixcolor TintMatrix("#676767")

    transform litedark:
        matrixcolor TintMatrix("#ded0c8")

    transform brighter:
        matrixcolor TintMatrix("#fff")

    transform red:
        matrixcolor TintMatrix("#f00")

    transform blood:
        matrixcolor TintMatrix("#8A0303")

    transform watermelon:
        matrixcolor TintMatrix("#FD4C59")

    transform green:
        matrixcolor TintMatrix("#548C55")

    transform night:
        matrixcolor TintMatrix("#5681D1")

    transform party:
        matrixcolor TintMatrix("#f00")
        linear 3.0 matrixcolor TintMatrix("#00f")
        linear 3.0 matrixcolor TintMatrix("#f00")
        repeat

    transform lparty:
        matrixcolor TintMatrix("#ff6060")
        linear 3.0 matrixcolor TintMatrix("#5b97ff")
        linear 3.0 matrixcolor TintMatrix("#ff6060")
        repeat

    transform police_lights:
        matrixcolor TintMatrix("#f0000033")
        linear 1.0 matrixcolor TintMatrix("#00f00033")
        linear 1.0 matrixcolor TintMatrix("#f0000033")
        repeat

    transform fire:
        matrixcolor TintMatrix("#ed912133")
        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#e3cf5722")
        linear float(renpy.random.choice(["0.0", "0.0", "0.05"])) matrixcolor TintMatrix("#00000033")
        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#ed912133")
        linear float(renpy.random.choice(["0.0", "0.0", "0.05"])) matrixcolor TintMatrix("#00000033")
        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#ed912166")
        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#e3cf5733")
        linear float(renpy.random.choice(["0.0", "0.0", "0.05"])) matrixcolor TintMatrix("#00000033")
        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#ed912155")
        linear float(renpy.random.choice(["0.0", "0.0", "0.05"])) matrixcolor TintMatrix("#e3cf5722")


        linear float(renpy.random.choice(["0.4", "0.75", "1.0"])) matrixcolor TintMatrix("#ed912133")
        repeat


    transform katstream:
        matrixcolor TintMatrix("#49cdfc")
        linear 6.0 matrixcolor TintMatrix("#f687ea")
        linear 6.0 matrixcolor TintMatrix("#49cdfc")
        repeat


    transform delayed_blink(delay, cycle):
        alpha .5

        pause delay

        block:
            linear .2 alpha 1.0
            pause .2
            linear .2 alpha 0.5
            pause (cycle - .4)
            repeat

    transform photo_pos(degrees):
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.45
        rotate degrees

    transform FadeInTransform:
        alpha 0.0
        pause (0.5)
        alpha 1.0


init python:
    
    def masking(pos, zoom_val, crop_pos, crop_size):
        """
        Creates a transform that crops, positions, and scales a layeredimage character.

        Parameters:
            pos: (x, y) screen position as floats 0.0-1.0
            zoom_val: scale factor (1.0 = normal, 2.0 = double size)
            crop_pos: (x, y) top-left corner of crop rectangle in pixels
            crop_size: (width, height) dimensions of crop rectangle in pixels

        Returns:
            Transform object ready for use with 'at' statement

        Usage:
            show amy normal at masking((0.5, 0.5), 2.0, (100, 50), (200, 200))
        """
        return Transform(
                crop=(crop_pos[0], crop_pos[1], crop_size[0], crop_size[1]),
                xalign=pos[0],
                yalign=pos[1],
                zoom=zoom_val)

image bg blank = "bg/blank.webp"
image bg white = "bg/blank.webp"
image bg black = "bg/black.webp"
image flashback = "gui/flashback.webp"
label before_main_menu:
    $ game.play_music("music/roa_music/journey.ogg")
    return

label splashscreen:
    show screen disclaimer with fade
    pause
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] *= .5
            _preferences.volumes['sfx'] *= .5
            _preferences.volumes['sexsfx'] *= .5
        if not persistent.set_mute_alarm_clock:
            persistent.set_mute_alarm_clock = True
            persistent.mute_alarm_clock = False
    hide screen disclaimer with fade
    show screen promo with fade
    pause
    hide screen promo
    scene bg white
    with dissolve
    return


label start_plus:
    call start (True) from _call_start

label start(start_plus=False):
    python:
        store.DONE = {}
        store.DONE_HOUR = []
        store.FLAGS = copy.deepcopy(FLAGS)
        store.HIDDEN = list(HIDDEN)
        renpy.dynamic('g')
        for g in Person.all():
            exec(g.id + " = g")
            g.set_room()
        game.room = "map"
    call intro (start_plus) from _call_intro

    # AYESHA REMOVED — make her permanently "gone forever" at game start: hidden
    # everywhere, dropped from all harems (taming/sporty/etc.), phone contact removed,
    # stats zeroed. Her files stay in place so the 1000+ `ayesha` references never break.
    # To restore Ayesha, delete this python block.
    python:
        _ayesha = Person.find("ayesha")
        if _ayesha and not _ayesha.is_gone_forever:
            _ayesha.set_gone_forever()

label main:
    call enter_room from _call_enter_room
    jump main

label after_load:
    python:
        for girl in Person.all():
            girl.set_room()

        achievement.sync()
    return
return
