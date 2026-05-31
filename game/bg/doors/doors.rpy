init 1:
    layeredimage bg door:
        attribute_function DayNightPicker()


        group doors:
            attribute black null
            attribute double null
            attribute entrance null
            attribute fancy null
            attribute hallway null
            attribute house null
            attribute mansion null
            attribute mansionentrance null
            attribute mdr null
            attribute office null
            attribute palla null
            attribute pub null
            attribute pub2 null
            attribute restaurant null


        group black auto if_any "black":
            attribute secure default


        attribute double


        attribute fancy


        attribute hallway


        attribute mansion


        attribute mdr


        attribute palla


        attribute pub
        attribute pub2


        group house auto if_any "house":
            attribute bathroom default


        group houseentrance auto if_any "entrance"      


        group office auto if_any "office":
            attribute openspace default


        group restaurant auto if_any "restaurant"       


        group mansionentrance auto if_any "mansionentrance"       
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
