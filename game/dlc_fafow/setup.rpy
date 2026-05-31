init:
    $ renpy.write_log("Loading DLC: FAFOW")
init -50:
    if not hasattr(store, "DLCS"):
        $ DLCS = {}
    $ DLCS["fafow"] = "26.4.0c"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
