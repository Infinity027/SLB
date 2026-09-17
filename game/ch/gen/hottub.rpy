init python:
    class HottubSexPicker(object):
        def __call__(self, attr):
            if attr & {"cassidy", "emma", "hanna", "harmony", "kleio", "lavish", "lexi", "minami", "palla", "amy", "kat", "reona", "cherie", "claire", "kiara"}:
                attr.add("01")
                attr.discard("02")
            else:
                attr.add("02")
                attr.discard("01")
            
            if game.calendar.is_today("valentine") and game.calendar.is_night:
                attr.add("valentine")
            elif game.calendar.is_night:
                attr.add("night")
            
            if enable_debug_picker:
                renpy.log(f"HottubSexPicker results: {attr}")
            return attr

    class HottubPicker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            else:
                
                g = None
                attr.add(randchoice(["center", "left"]))
                attr.add("mcalone")
            if g:
                if g.id in ["anna", "bree", "emma", "kleio", "lavish", "lexi", "samantha", "sasha", "shiori", "scottie", "ryan", "danny", "dwayne", "reona"]:
                    attr.add("center")
                    attr.discard("left")
                elif g.id in ["aletta", "alexis", "angela", "audrey", "cassidy", "hanna", "harmony", "minami", "morgan", "palla", "camila", "mike", "jack", "shawn", "master", "victor", "kat", "amy", "cherie", "claire", "kiara"]:
                    attr.add("left")
                    attr.discard("center")
            
            if enable_debug_picker:
                renpy.log(f"HottubPicker results: {attr}")
            return attr
