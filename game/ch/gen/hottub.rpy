init python:
    class HottubSexPicker(object):
        def __call__(self, attr):
            if attr & {"cassidy", "emma", "hanna", "harmony", "kleio", "lavish", "lexi", "minami", "palla", "amy", "kat", "reona", "cherie", "claire", "kiara"}:
                attr.add("01")
                attr.discard("02")
            else:
                attr.add("02")
                attr.discard("01")
            
            if game.calendar.is_today("valentine") and game.calendar.is_night:
                attr.add("valentine")
            elif game.calendar.is_night:
                attr.add("night")
            
            if enable_debug_picker:
                renpy.log(f"HottubSexPicker results: {attr}")
            return attr

    class HottubPicker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            else:
                
                g = None
                attr.add(randchoice(["center", "left"]))
                attr.add("mcalone")
            if g:
                if g.id in ["anna", "bree", "emma", "kleio", "lavish", "lexi", "samantha", "sasha", "shiori", "scottie", "ryan", "danny", "dwayne", "reona"]:
                    attr.add("center")
                    attr.discard("left")
                elif g.id in ["aletta", "alexis", "angela", "audrey", "cassidy", "hanna", "harmony", "minami", "morgan", "palla", "camila", "mike", "jack", "shawn", "master", "victor", "kat", "amy", "cherie", "claire", "kiara"]:
                    attr.add("left")
                    attr.discard("center")
            
            if enable_debug_picker:
                renpy.log(f"HottubPicker results: {attr}")
            return attr

init 1:
    layeredimage hottub sex male:
        attribute_function Pickers([PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, PiercingsPicker, OutfitPicker, DickPicker, HottubSexPicker], clear_npc=True)


        group tattoo:
            attribute angel null
            attribute wolf null


        group bg auto if_not ["valentine", "night"]
        group bg auto variant "valentine" if_any ["valentine"]
        group bg auto variant "night" if_any ["night"]


        group body auto


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]


        group line auto


        attribute boobjob null
        group bb auto if_any ["boobjob"]


        attribute ahegao null
        group ahegao auto if_any ["ahegao"]
        group normal auto if_not ["ahegao"]



        attribute lips null
        group piercings_lips auto if_any ["lips"]

        attribute tongue null
        group piercings_tongue auto if_any ["tongue"]

        attribute nipples null
        group piercings_nipples auto if_any ["nipples"] if_not ["boobjob", "aletta"]
        group piercings_nipples_bb auto if_all ["nipples", "boobjob"]

        attribute nose null
        group piercings_nose auto if_any ["nose"]

        attribute ears null
        group piercings_ears auto if_any ["nose"]

        attribute clit null
        group piercings_clit auto if_any ["clit"] if_not ["inside"]
        group piercings_clit auto variant "inside" if_all ["clit", "inside"]

        attribute navel null
        attribute pregnant_navel null
        group piercings_navel auto if_any ["navel"] if_not ["pregnant"]
        group piercings_navel_pregnant auto if_all ["navel", "pregnant"]


        always:
            if_all ["aletta","nipples", "naked"]
            "hottub_sex_male_piercings_nipples_aletta"


        group fuck:
            attribute inside null
            attribute outside null
            attribute nodick null default


        attribute naked null
        attribute swimsuit null default
        attribute sexyswimsuit null
        group swimsuit auto if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto if_any ["sexyswimsuit"] if_not ["naked"]

        group pregnant auto if_all ["pregnant"] if_any ["cassidy"]

        attribute big null
        group dick_inside auto variant "big" if_all ["inside", "big"]
        attribute medium null
        group dick_inside auto variant "medium" if_all ["inside", "medium"]
        attribute small null
        group dick_inside auto variant "small" if_all ["inside", "small"]


        group pregnant auto if_all ["pregnant"] if_not ["cassidy"]


        group swimsuit auto variant "pregnant" if_any ["pregnant"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "pregnant" if_all ["sexyswimsuit", "pregnant"] if_not ["naked"]


        group swimsuit auto variant "bb" if_any ["boobjob"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "bb" if_all ["sexyswimsuit", "boobjob"] if_not ["naked"]


        group swimsuit auto variant "outside" if_any ["outside"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "outside" if_all ["sexyswimsuit", "outside"] if_not ["naked"]


        group swimsuit auto variant "inside" if_any ["inside"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside" if_all ["sexyswimsuit", "inside"] if_not ["naked"]

        group swimsuit auto variant "inside_big" if_all ["inside", "big"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_big" if_all ["sexyswimsuit", "inside", "big"] if_not ["naked"]

        group swimsuit auto variant "inside_medium" if_all ["inside", "medium"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_medium" if_all ["sexyswimsuit", "inside", "medium"] if_not ["naked"]

        group swimsuit auto variant "inside_small" if_all ["inside", "small"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_small" if_all ["sexyswimsuit", "inside", "small"] if_not ["naked"]



        group swimsuit auto variant "inside_pregnant_big" if_all ["inside", "pregnant", "big"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_pregnant_big" if_all ["sexyswimsuit", "inside", "pregnant", "big"] if_not ["naked"]

        group swimsuit auto variant "inside_pregnant_medium" if_all ["inside", "pregnant", "medium"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_pregnant_medium" if_all ["sexyswimsuit", "inside", "pregnant", "medium"] if_not ["naked"]

        group swimsuit auto variant "inside_pregnant_small" if_all ["inside", "pregnant", "small"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "inside_pregnant_small" if_all ["sexyswimsuit", "inside", "pregnant", "small"] if_not ["naked"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute makeup null
        group makeup auto if_any ["makeup"]


        group dick_outside auto variant "big" if_all ["outside", "big"]
        group dick_outside auto variant "small" if_all ["outside", "small"]
        group dick_outside auto variant "medium" if_all ["outside", "medium"]


        attribute cumshot null

        group cumshot auto variant "big" if_all ["cumshot", "outside", "big"]
        group cumshot auto variant "small" if_all ["cumshot", "outside", "small"]
        group cumshot auto variant "medium" if_all ["cumshot", "outside", "medium"]

        group cumshot auto variant "inside_big" if_all ["cumshot", "inside", "big"]
        group cumshot auto variant "inside_small" if_all ["cumshot", "inside", "small"]
        group cumshot auto variant "inside_medium" if_all ["cumshot", "inside", "medium"]


        group fg auto


        group petals auto if_any ["valentine"]


        group light auto

    layeredimage hottub:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker, OutfitPicker, PubesPicker, HottubPicker, MCCGPicker, DayNightPicker, SeasonPicker, SpecialDayPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        attribute mikemc null
        attribute breemc null

        attribute naked null
        attribute day null
        attribute mcalone null
        attribute nomc null
        attribute valentine null
        attribute collar null

        attribute mc_nohaircut null
        attribute mc_pubes null

        group bg auto variant "spring" if_any "spring"
        group bg auto variant "summer" if_any "summer"
        group bg auto variant "fall" if_any "fall"
        group bg auto variant "winter" if_any "winter"
        group bg auto variant "night" if_any "night"

        group mikemc_outfits if_any ["mikemc"]:
            attribute mc_swimsuit null

        group mikemc_dick:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        group mikemc auto if_any ["mikemc"] if_not "nomc"
        group mikemc_swimsuit auto if_any ["mikemc"] if_not ["naked", "nomc"]
        group mikemc_water auto if_any ["mikemc"] if_not "nomc"

        group breemc auto if_any ["breemc"] if_not ["scottie", "ryan", "danny", "dwayne", "nomc"]
        group breemc_swimsuit auto if_all ["breemc", "mc_swimsuit"] if_not ["naked", "mc_sexyswimsuit", "scottie", "ryan", "danny", "dwayne", "nomc"]
        group breemc_sexyswimsuit auto if_all ["breemc", "mc_sexyswimsuit"] if_not ["naked", "scottie", "ryan", "danny", "dwayne", "nomc"]
        group breemc_water auto if_any ["breemc"] if_not ["scottie", "ryan", "danny", "dwayne", "nomc"]

        group npc auto if_not "mcalone"
        group boobjobs auto if_not "mcalone":
            attribute sasha_noboobjob null

        group haircuts auto

        group pubes auto

        group glasses auto if_not "mcalone"
        group tattoo auto if_not "mcalone":
            attribute angel null
            attribute wolf null
        group smoke auto if_not "mcalone"

        group collars auto if_any "collar" if_not "mcalone"

        group multiple auto variant piercings

        group outfits auto if_not "naked"
        group outfits_boobjob auto if_any "sasha_boobjob" if_not "naked"
        group pregnancies auto if_not ["mcalone"]
        group outfits_pregnant auto if_any "pregnant" if_not "naked"

        attribute morgan_makeup

        group breemc_guys auto if_all ["breemc"] if_any ["scottie", "ryan", "danny", "dwayne"] if_not "mcalone"
        group breemc_guys_swimsuit auto if_all ["breemc"] if_any ["scottie", "ryan", "danny", "dwayne"] if_not ["naked", "mc_sexyswimsuit", "mcalone"]
        group breemc_guys_sexyswimsuit auto if_all ["breemc", "mc_sexyswimsuit"] if_any ["scottie", "ryan", "danny", "dwayne"] if_not ["naked", "mcalone"]
        group breemc_guys_water auto if_all ["breemc"] if_any ["scottie", "ryan", "danny", "dwayne"] if_not "mcalone"

        group water auto if_not "mcalone"
        always:
            if_all ["left", "mikemc"]
            "hottub_fg_water_left"
        always:
            if_all ["center", "mcalone", "mikemc"]
            "hottub_fg_water_center"
        group fg auto variant "summer" if_any "summer"
        group fg auto variant "autumn" if_any "autumn"
        group fg auto variant "winter" if_any "winter"
        group fg auto variant "valentine" if_any "valentine"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
