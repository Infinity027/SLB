label love_lesbian_adjust_female:
    python:

        for g in [g for g in Person.all_people(ignore_hidden=True) if hasattr(g, "lesbian") and g.love > 25 and g.lesbian < 5]:
            
            g.love -= (5 - g.lesbian.val)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
