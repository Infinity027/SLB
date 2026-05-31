init 1:
    layeredimage bg taxi:
        attribute_function DayNightPicker()
        attribute day null
        attribute night null

        group back auto

        group shadow auto if_any ["car"]

        attribute car null
        group car auto variant "open" if_all ["open", "car"]
        group car auto variant "closed" if_all ["closed", "car"]
        group car_state:
            attribute open null
            attribute closed null default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
