init 1:
    layeredimage bg clairehouse:

        attribute_function DayNightPicker()
        attribute day null
        attribute night null

        attribute house
        attribute kitchen

        attribute adambedroom null
        group adambedroom auto if_any "adambedroom"

        attribute diningroom null
        group diningroom auto if_any "diningroom"

        attribute pool null
        group pool auto if_any "pool"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
