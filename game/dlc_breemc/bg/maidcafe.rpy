label work_maidcafe:
    show chibi maidcafe
    "I think that customer is watching me weirdly..."
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
