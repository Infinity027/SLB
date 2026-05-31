init:
    $ renpy.write_log("Loading DLC: LIVELY")
init -50:
    if not hasattr(store, "DLCS"):
        $ DLCS = {}
    $ DLCS["lively"] = "26.4.0c"
    $ persistent.lively_bg = True if persistent.lively_bg is None else persistent.lively_bg
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
