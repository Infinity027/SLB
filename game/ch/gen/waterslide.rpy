init python:
    class WaterslidePositionPicker(object):
        def __call__(self, attr):
            if hero.is_female:
                g = attr & set(p.id for p in Person.all())
                g = list(g)[0] if g else None
                if g in ["angela", "lexi", "sasha"]:
                    attr.add("back")
                else:
                    attr.add("ahead")
                    attr.add(g + "normal")
            if enable_debug_picker:
                renpy.log(f"WaterslidePositionPicker results: {attr}")
            return attr

