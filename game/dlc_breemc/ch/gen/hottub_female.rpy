init python:
    class CG_HottubSexFemale_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["danny", "dwayne", "master", "victor"]:
                    attr.add("01")
                    attr.discard("02")
                else:
                    attr.add("02")
                    attr.discard("01")
            
            if game.calendar.is_today("valentine") and game.calendar.is_night:
                attr.discard("night")
                attr.add("valentine")
            
            if enable_debug_picker:
                renpy.log(f"CG_HottubSexFemale_Picker results: {attr}")
            return attr


init 1:
    layeredimage hottub sex female:
        attribute_function Pickers([MCPicker, PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker, DayNightPicker, OutfitPicker, CG_HottubSexFemale_Picker], clear_npc=True)
        attribute nodick null
        attribute valentine null

        group bg auto if_not ["valentine", "night"]
        group bg auto variant "valentine" if_any ["valentine"]
        group bg auto variant "night" if_any ["night"] if_not ["valentine"]
        group bg auto variant "day" if_any ["day"]


        group body auto


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]


        attribute naked null
        attribute swimsuit null default
        attribute sexyswimsuit null
        group swimsuit auto if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto if_any ["sexyswimsuit"] if_not ["naked"]

        attribute mc_swimsuit null default
        attribute mc_sexyswimsuit null
        group mc_swimsuit auto if_not ["mc_sexyswimsuit", "naked"]
        group mc_sexyswimsuit auto if_any ["mc_sexyswimsuit"] if_not ["naked"]


        group fg auto


        group petals auto if_any ["valentine"]


        group light auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
