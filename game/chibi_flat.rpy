# =============================================================================
#  CHIBI FLAT SYSTEM  (replaces the auto-discovered chibi_mike_* layer art)
#
#  The little MC "activity" sprite   show chibi <activity>   now resolves to a
#  single flat image:                game/images/chibi/<activity>.png
#  Optional shared backdrop:         game/images/chibi/bg.png
#
#  WHY THIS WORKS WITHOUT CHANGING THE LAYEREDIMAGE:
#  The `layeredimage chibi` in ch/gen/images.rpy is left UNCHANGED. Its
#     group mike auto      auto-discovers the image names  chibi_mike_<activity>
#     always "chibi_bg"    uses the image name             chibi_bg
#  We register exactly those names below (as flat images), so every existing
#  `show chibi <activity>` call site keeps working with no edits.
#
#  Missing art never crashes: an activity you haven't drawn yet shows blank
#  (Null) instead of raising a "missing image" error.
#
#  TO ADD a new activity later:  add its name to CHIBI_ACTIVITIES below and
#  drop game/images/chibi/<name>.png next to the others.
#
#  TO REVERT to the old layered chibi art: delete this file.
# =============================================================================

init 0 python:

    # --- every activity passed to `show chibi <activity>` in the scripts ---
    CHIBI_ACTIVITIES = [
        "arcade", "bakery", "bath", "beer", "bible", "book", "bookstore",
        "burger", "clawmachine", "cleanpool", "clover", "coffee", "coffeebreak",
        "coffeeshop", "console", "dishes", "eat", "electronic", "gym", "haircut",
        "hike", "hotdog", "hottub", "kart", "lap", "leaves", "lottery",
        "martialarts", "mass", "maw", "parknap", "parkthink", "party", "pushups",
        "ramen", "run", "sexshop", "shovel", "shower", "sleep", "spy", "study",
        "swim", "tan", "theater", "train", "trainhard", "traintalk", "tv",
        "vacuum", "work", "workhard", "workslack",
    ]

    # ---- resolver: images/chibi/<activity>.png at render time, blank if absent
    def _flat_chibi(st, at, activity=None):
        for path in (
            "images/chibi/%s.jpg" % activity,   # the drawn pose
            "images/chibi/idle.jpg",            # optional generic fallback pose
        ):
            if renpy.loadable(path):
                return Image(path), None
        return Null(), None                     # not drawn yet -> blank, never an error

    # ---- optional shared backdrop behind every pose (images/chibi/bg.jpg) ----
    def _flat_chibi_bg(st, at):
        if renpy.loadable("images/chibi/bg.jpg"):
            return Image("images/chibi/bg.jpg"), None
        return Null(), None                     # no bg file -> nothing drawn

    # register the names the layeredimage expects
    renpy.image("chibi_bg", DynamicDisplayable(_flat_chibi_bg))
    for _a in CHIBI_ACTIVITIES:
        renpy.image("chibi_mike_%s" % _a,
                    DynamicDisplayable(_flat_chibi, activity=_a))
