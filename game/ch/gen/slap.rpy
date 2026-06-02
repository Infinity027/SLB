init python:
    class SlapPositionPicker(object):
        def __call__(self, attr):
            if hero.gender == "female":
                if attr & {"sasha"}:
                    attr.add("pose01")
                elif attr & {"ayesha"}:
                    attr.add("pose02")
                elif attr & {"lexi"}:
                    attr.add("pose03")
                elif attr & {"angela", "danny", "dwayne", "jack", "master", "mike", "ryan", "scottie", "shawn", "victor"}:
                    attr.add("pose04")
            else:
                if attr & {"bree", "emma", "kleio", "minami", "morgan", "sasha"}:
                    attr.add("pose01")
                elif attr & {"ayesha", "hanna", "lavish", "palla"}:
                    attr.add("pose02")
                elif attr & {"aletta", "anna", "cassidy", "harmony", "lexi", "samantha"}:
                    attr.add("pose03")
                elif attr & {"alexis", "angela", "audrey", "camila", "shiori", "amy", "reona", "kat", "cherie", "claire", "kiara"}:
                    attr.add("pose04")
                
                if {"mc_work"} & attr:
                    if attr & {"aletta", "audrey", "cassidy", "lavish", "shiori"}:
                        attr.add('mc_workoffice')
                    elif attr & {"ayesha", "hanna"}:
                        attr.add('mc_worksport')
                    elif attr & {"camila", "kleio"}:
                        attr.add('mc_workcasual')
            if enable_debug_picker:
                renpy.log(f"SlapPositionPicker results: {attr}")
            return attr

init 1:
    layeredimage slap:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, SeasonPicker, IndoorOutdoorPicker, SlapPositionPicker, MCCGPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        group arms_position:
            attribute waiting null default
            attribute slapping null


        group mc_body auto variant "pose03" if_any ["pose03"]

        group mc_haircuts_breemc auto variant "pose03" if_all ["pose03", "breemc"]
        group mc_exp auto variant "pose03" if_all ["pose03"]


        group mc_outfits_mikemc auto variant "pose03" if_all ["mikemc", "pose03"]:
            attribute naked null


        group mc_outfits_breemc auto variant "pose03" if_all ["breemc", "pose03"]:
            attribute naked null




        group npc auto if_not ["bree_bowsette"]


        attribute pregnant null


        group pregnancy auto if_not ["aletta", "ayesha", "harmony", "minami_halloween", "minami_rpg", "samantha_sexyswimsuit"]


        group boobjob auto


        group collars auto if_not ["aletta_date", "aletta_sexyswimsuit", "aletta_wedding", "aletta_work", "morgan_whitetank", "morgan_redhalf", "morgan_tightsport", "hanna_date", "hanna_sexydate", "hanna_wedding", "hanna_sexyswimsuit", "lavish", "minami_bikini", "minami_rpg", "palla_casual", "palla_date" , "palla_sexydate", "palla_sexyswimsuit", "palla_swimsuit", "palla_wedding"]


        group necklace auto


        group multiple auto variant piercings when not palla_ears
        group multiple auto variant piercings_hidden when naked
        group multiple auto variant piercings_hidden when cassidy_work and cassidy_topless
        group multiple auto variant piercings_hidden when palla_sluttyswimsuit
        group multiple auto variant piercings_date when camila_date or camila_sexydate
        group multiple auto variant piercings_casual when camila and not (camila_date or camila_sexydate)
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_angry when angry



        group outfit auto variant "bot" if_not ["naked"]
        group multiple auto variant outfit_pregnant_bot when pregnant and not naked


        group multiple auto variant outfit_pregnant when alexis and pregnant and not naked


        group outfit auto if_not ["naked"]
        group outfit auto variant "gold" if_not ["naked"] if_all ["cassidy_gold"]
        group outfit auto variant "full" if_not ["naked", "cassidy_topless"]
        group outfit auto variant "topless" if_not ["naked"] if_all ["cassidy_topless"]
        group outfit_boobjob auto if_any ["sasha_boobjob"] if_not ["naked"]


        group pregnancy auto if_all ["aletta"] if_any ["naked", "aletta_cosplay", "aletta_swimsuit", "aletta_sexyswimsuit"]
        group pregnancy auto if_all ["ayesha"] if_any ["naked", "ayesha_sexydate", "ayesha_sport"]
        group pregnancy auto if_all ["harmony"] if_any ["naked", "harmony_underwear"]
        group pregnancy auto if_all ["samantha"] if_any ["naked", "samantha_sexyswimsuit"]


        group outfit auto variant "top" if_not ["naked"]
        group multiple auto variant outfit_pregnant_top when pregnant and not naked


        group multiple auto variant outfit_pregnant when pregnant and not (naked or alexis)
        group multiple auto variant outfit_pregnant_full when pregnant and cassidy and not (naked or cassidy_topless)
        group multiple auto variant outfit_pregnant_topless when pregnant and cassidy_topless and not naked


        group collars auto if_any ["aletta_date", "aletta_sexyswimsuit", "aletta_wedding", "aletta_work", "morgan_whitetank", "morgan_redhalf", "morgan_tightsport", "hanna_date", "hanna_sexydate", "hanna_wedding", "hanna_sexyswimsuit", "lavish", "minami_bikini", "minami_rpg", "palla_casual", "palla_date" , "palla_sexydate", "palla_sexyswimsuit", "palla_swimsuit", "palla_wedding"]


        group multiple auto variant piercings when palla_ears


        group hairs auto when not (harmony_nun or camila_halloween or (kiara_casual and not naked))


        group exp auto variant "angry" if_any ["angry"]
        group exp auto variant "happy" if_any ["happy"]
        group expressions:
            attribute happy null default
            attribute angry null


        group acc auto


        group hat auto if_not ["naked", "emma_casual"]


        group sam_hood:
            attribute hoodin null
            attribute hoodout null
        group hat auto variant "hoodin" if_any ["hoodin"] if_not ["naked"]
        group hat auto variant "hoodout" if_any ["hoodout"] if_not ["naked"]


        attribute hat null
        group hat auto if_all ["emma_casual", "hat"] if_any ["winter", "fall"] if_not ["naked"]
        group hat auto if_all ["emma_casual", "outdoor"] if_any ["winter", "fall"] if_not ["naked"]
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null


        attribute helmet null
        group helmet auto if_any ["helmet"] if_not ["naked"]


        attribute blazer null
        group blazer auto if_all ["outdoor"] if_any ["winter", "fall"] if_not ["naked"]
        group blazer auto if_any ["blazer"] if_not ["naked"]
        group inout:
            attribute indoor null
            attribute outdoor null





        group mc_body auto variant "pose01" if_any ["pose01"]
        group mc_body auto variant "pose02" if_any ["pose02"]
        group mc_body auto variant "pose04" if_any ["pose04"]

        attribute mc_nohaircut null
        group mc_haircuts_breemc auto variant "pose01" if_all ["pose01", "breemc"]
        group mc_haircuts_breemc auto variant "pose02" if_all ["pose02", "breemc"]
        group mc_haircuts_breemc auto variant "pose04" if_all ["pose04", "breemc"]




        group mc_outfits_mikemc auto variant "pose01" if_all ["pose01", "mikemc"]:
            attribute naked null

        group mc_outfits_breemc auto variant "pose01" if_all ["pose01", "breemc"]:
            attribute naked null


        group fx auto variant "pose01" if_all ["pose01"]


        group mc_arms_mikemc auto variant "pose01" if_all ["pose01", "mikemc"]
        group mc_arms_breemc auto variant "pose01" if_all ["pose01", "breemc"]


        group mc_arms_outfits_mikemc auto variant "pose01_waiting" if_all ["pose01", "waiting", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_mikemc auto variant "pose01_slapping" if_all ["pose01", "slapping", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose01_waiting" if_all ["pose01", "waiting", "breemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose01_slapping" if_all ["pose01", "slapping", "breemc"]:
            attribute naked null




        group mc_outfits_mikemc auto variant "pose02" if_all ["pose02", "mikemc"]:
            attribute naked null

        group mc_outfits_breemc auto variant "pose02" if_all ["pose02", "breemc"]:
            attribute naked null


        group fx auto variant "pose02" if_all ["pose02"]


        group mc_arms_mikemc auto variant "pose02" if_all ["pose02", "mikemc"]

        group mc_arms_breemc auto variant "pose02" if_all ["pose02", "breemc"]


        group mc_arms_outfits_mikemc auto variant "pose02_waiting" if_all ["pose02", "waiting", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_mikemc auto variant "pose02_slapping" if_all ["pose02", "slapping", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose02_waiting" if_all ["pose02", "waiting", "breemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose02_slapping" if_all ["pose02", "slapping", "breemc"]:
            attribute naked null




        group fx auto variant "pose03" if_all ["pose03"]


        group mc_arms_mikemc auto variant "pose03" if_all ["pose03", "mikemc"]

        group mc_arms_breemc auto variant "pose03" if_all ["pose03", "breemc"]


        group mc_arms_outfits_mikemc auto variant "pose03_waiting" if_all ["pose03", "waiting", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_mikemc auto variant "pose03_slapping" if_all ["pose03", "slapping", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose03_waiting" if_all ["pose03", "waiting", "breemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose03_slapping" if_all ["pose03", "slapping", "breemc"]:
            attribute naked null




        group mc_arms_mikemc auto variant "pose04" if_all ["pose04", "mikemc"]
        group mc_arms_breemc auto variant "pose04" if_all ["pose04", "breemc"]


        group mc_arms_outfits_mikemc auto variant "pose04_waiting" if_all ["pose04", "waiting", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_mikemc auto variant "pose04_slapping" if_all ["pose04", "slapping", "mikemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose04_waiting" if_all ["pose04", "waiting", "breemc"]:
            attribute naked null

        group mc_arms_outfits_breemc auto variant "pose04_slapping" if_all ["pose04", "slapping", "breemc"]:
            attribute naked null


        group mc_outfits_mikemc auto variant "pose04" if_all ["pose04", "mikemc"]:
            attribute naked null

        group mc_outfits_breemc auto variant "pose04" if_all ["pose04", "breemc"]:
            attribute naked null


        group fx auto variant "pose04" if_all ["pose04"]

        always:
            if_not ["danny_casual", "danny_date", "danny_halloween"]
            if_any "danny"
            "slap_arms_danny"
        group arms_outfits auto variant "danny" if_any "danny"
        always:
            if_not ["dwayne_casual", "dwayne_date"]
            if_any "dwayne"
            "slap_arms_dwayne"
        group arms_outfits auto variant "dwayne" if_any "dwayne"
        always:
            if_not ["jack_casual", "jack_date", "jack_halloween"]
            if_any "jack"
            "slap_arms_jack"
        group arms_outfits auto variant "jack" if_any "jack"
        always:
            if_not ["master_casual", "master_date", "master_swimsuit", "master_halloween"]
            if_any "master"
            "slap_arms_master"
        group arms_outfits auto variant "master" if_any "master"
        always:
            if_not ["mike_casual", "mike_date", "mike_halloween"]
            if_any "mike"
            "slap_arms_mike"
        group arms_outfits auto variant "mike" if_any "mike"
        always:
            if_not ["ryan_casual", "ryan_date", "ryan_halloween"]
            if_any "ryan"
            "slap_arms_ryan"
        group arms_outfits auto variant "ryan" if_any "ryan"
        always:
            if_not ["scottie_casual", "scottie_date"]
            if_any "scottie"
            "slap_arms_scottie"
        group arms_outfits auto variant "scottie" if_any "scottie"
        always:
            if_not ["shawn_casual", "shawn_date", "shawn_halloween"]
            if_any "shawn"
            "slap_arms_shawn"
        group arms_outfits auto variant "shawn" if_any "shawn"
        always:
            if_not ["victor_casual"]
            if_any "victor"
            "slap_arms_victor"
        group arms_outfits auto variant "victor" if_any "victor"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
