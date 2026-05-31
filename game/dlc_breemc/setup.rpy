init:
    $ renpy.write_log("Loading DLC: BreeMC")
init -50:
    if not hasattr(store, "DLCS"):
        $ DLCS = {}
    $ DLCS["breemc"] = "26.4.0c"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
