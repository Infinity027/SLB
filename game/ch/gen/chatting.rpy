init python:
    class CG_Chatting_Picker(object):
        def __call__(self, attr):
            if attr & {"aletta", "audrey", "bree", "jack", "lexi", "mike", "minami", "samantha", "sasha", "shiori"}:
                attr.add("01")
            elif attr & {"alexis", "camila", "cassidy", "danny", "lavish", "morgan", "palla", "scottie", "cherie", "claire", "kiara"}:
                attr.add("02")
            elif attr & {"angela", "ayesha", "harmony", "kleio", "shawn", "victor"}:
                attr.add("03")
            elif attr & {"amy", "anna", "dwayne", "emma", "hanna", "kat", "master", "reona", "ryan"}:
                attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_Chatting_Picker results: {attr}")
            return attr

init 1:
    layeredimage chatting:
        attribute_function MultiPickers([CG_Chatting_Picker, SeasonPicker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCCGPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True, add_simple_outfit_attribute=True)

        group mc_dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        group room auto:
            attribute livingroom null default
            attribute coffeeshop null
            attribute pub null
            attribute pubplay null
            attribute pubseat null
            attribute park null

        group seasons auto:
            attribute winter null
            attribute summer null
            attribute spring null
            attribute fall null

        group expressions auto:
            attribute normal null default
            attribute angry null
            attribute blush null
            attribute happy null
            attribute sad null


        group bg auto variant "livingroom" if_any ["livingroom"]
        group bg auto variant pub when pub or pubplay or pubseat
        group bg auto variant "coffeeshop" if_any ["coffeeshop"]
        group bg auto variant "park_spring" if_all ["park", "spring"]
        group bg auto variant "park_summer" if_all ["park", "summer"]
        group bg auto variant "park_fall" if_all ["park", "fall"]
        group bg auto variant "park_winter" if_all ["park", "winter"]


        attribute mikemc null
        group mikemc auto if_any ["mikemc"]
        group mikemc_exp auto variant "01" if_all ["mikemc", "01"]:
            attribute normal default
        group mikemc_exp auto variant "02" if_all ["mikemc", "02"]:
            attribute normal default
        group mikemc_exp auto variant "03" if_all ["mikemc", "03"]:
            attribute normal default
        group mikemc_exp auto variant "04" if_all ["mikemc", "04"]:
            attribute normal default


        group breemc auto if_any ["breemc"]
        group breemc_outfits if_any ["breemc"]:
            attribute mc_casual null default
            attribute mc_sport null
        group breemc_outfits auto variant "01" if_all ["breemc", "01"]
        group breemc_outfits auto variant "02" if_all ["breemc", "02"]
        group breemc_outfits auto variant "03" if_all ["breemc", "03"]
        group breemc_outfits auto variant "04" if_all ["breemc", "04"]

        group breemc_exp auto variant "01" if_all ["breemc", "01"]:
            attribute normal default
        group breemc_exp auto variant "02" if_all ["breemc", "02"]:
            attribute normal default
        group breemc_exp auto variant "03" if_all ["breemc", "03"]:
            attribute normal default
        group breemc_exp auto variant "04" if_all ["breemc", "04"]:
            attribute normal default


        group npc auto


        attribute morgan_makeup null
        group makeup auto variant "eyes" if_any ["morgan_makeup"]


        group npc_exp auto variant "angry" if_any "angry"
        group npc_exp auto variant "blush" if_any "blush"
        group npc_exp auto variant "happy" if_any "happy"
        group npc_exp auto variant "normal" if_any "normal"
        group npc_exp auto variant "sad" if_any "sad"


        group makeup auto variant "mouth" if_any ["morgan_makeup"]


        group pregnancies auto


        group boobjobs auto if_any ["naked", "sasha_naked"]:
            attribute sasha_noboobjob null


        group multiple auto variant piercings
        group piercings auto variant "noboobjob" if_any "sasha_noboobjob"
        group piercings auto variant "boobjob" if_any "sasha_boobjob"


        group outfits auto
        group outfits auto variant "pregnant" if_any "pregnant"


        group haircuts auto when not kiara_casual
        group haircuts auto variant casual when kiara_casual

        group outfits_boobjob auto if_any "sasha_boobjob"


        group bot auto if_not ["naked"] if_all ["morgan"]
        group bot auto variant "pregnant" if_all ["pregnant", "morgan"] if_not ["naked"]


        group piercings auto variant "sport" if_all ["pregnant", "sport"]
        group piercings auto variant "casual" if_all ["pregnant", "casual"]
        group piercings auto variant "underwear" if_all ["pregnant", "underwear"]
        group piercings auto variant "sleep" if_all ["pregnant", "sleep"]


        group top auto if_not ["naked"] if_all ["morgan"]
        group top auto variant "pregnant" if_all ["pregnant", "morgan"] if_not ["naked"]


        group collars auto

        group acc auto


        group fg auto variant "livingroom" if_any ["livingroom"]
        group fg auto variant pub when pub or pubplay or pubseat
        group fg auto variant "park" if_any ["park"]
        group fg auto variant "coffeeshop" if_any ["coffeeshop"]
        group fg auto variant pub_notsasha when pub or pubplay or pubseat and not sasha
        group fg auto variant "livingroom_notdwayne" if_any ["livingroom"] if_not ["dwayne"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
