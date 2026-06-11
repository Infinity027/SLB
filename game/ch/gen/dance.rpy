init 1:
    layeredimage dance:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, PubesPicker, MCGenderPicker], add_simple_pregnant_attribute=True, add_simple_outfit_attribute=True, use_morgan_cg_outfits=True, append_npc_from_attributes=True)
        attribute date null
        attribute work null

        group mc auto if_all ["mikemc"]

        group mc_outfit auto variant "mikemc" if_all "mikemc":
            attribute mcdate default

        group mc_armsoutfit auto variant "mikemc_a" if_all "mikemc" if_any ["alexis", "angela", "audrey", "bree", "camila", "cassidy", "emma", "hanna", "harmony", "kleio", "lavish", "lexi", "morgan", "palla", "samantha", "sasha", "shiori", "amy", "kat", "reona", "cherie", "claire", "kiara"]:
            attribute mcdate default
        group mc_armsoutfit auto variant "mikemc_b" if_all "mikemc" if_any ["aletta"]:
            attribute mcdate default
        group mc_armsoutfit auto variant "mikemc_c" if_all "mikemc" if_any ["anna", "minami"]:
            attribute mcdate default


        group mc_outfit auto variant "breemc_pose01" if_all ["breemc", "halloween"]
        group mc_armsoutfit auto variant "breemc_pose01_b" if_all ["breemc", "halloween"]


        group mc_outfit auto variant "breemc_pose01" if_all "breemc" if_not ["danny", "dwayne", "jack", "master", "mike", "ryan", "sasha", "scottie", "shawn",  "victor"]:
            attribute mcdate default

        group mc_armsoutfit auto variant "breemc_pose01_a" if_all "breemc" if_any ["audrey", "camila", "cassidy", "emma", "hanna", "harmony", "kleio", "lavish", "lexi", "morgan", "samantha", "shiori"]:
            attribute mcdate default
        group mc_armsoutfit auto variant "breemc_pose01_b" if_all "breemc" if_any ["aletta", "alexis", "anna"]:
            attribute mcdate default

        group expbreemc auto if_any ["breemc"]


        group npc auto if_not ["bree_sexydate", "minami_date", "samantha_sexydate", "samantha_sluttydate", "sasha_sluttydate", "shiori_sexydate", "shiori_sexywork"]
        group npc auto variant "pose01" if_all ["mikemc"] if_any ["sasha"] if_not "sasha_sluttydate"
        group npc auto variant "pose02" if_any ["minami"] if_not ["minami_date"]

        group npc auto variant "pose02" if_all ["breemc"] if_not ["halloween"]
        group npc auto variant "pose02" if_all ["breemc", "sasha"]


        group npc auto variant "pose01" if_all ["breemc", "halloween"]

        group pubes auto


        group pregnancy auto
        group pregnancy auto variant "pose02" if_all ["breemc"] if_not ["halloween"]


        group boobjob:
            attribute sasha_boobjob null
            attribute sasha_noboobjob null


        group multiple auto variant piercings when not camila_halloween

        group underwear auto
        group underdress auto
        group underdress_pregnant auto if_any ["pregnant"]


        group outfit auto
        group outfit_pregnant auto if_any ["pregnant"]


        group outfit auto variant "pose01" if_all ["mikemc"]
        group outfit_pregnant auto variant "pose01" if_all ["mikemc", "pregnant", "sasha"]
        group outfit_pregnant auto variant "pose02" if_all ["breemc", "pregnant", "sasha"]

        group outfit_boobjob auto variant "pose01" if_all ["sasha_boobjob", "mikemc"]


        group outfit auto variant "pose02" if_all ["sasha", "breemc"]
        group outfit_boobjob auto variant "pose02" if_all ["sasha_boobjob", "breemc"]


        group multiple auto variant outfit_pose01 when mikemc and minami_date
        
        group outfit auto variant "pose02" if_all ["mikemc", "minami"] if_not "minami_date"
        group outfit_pregnant auto variant "pose02" if_all ["mikemc", "pregnant", "minami"] if_not ["minami_date"]


        group outfit auto variant "pose01" if_all ["breemc"] if_any ["minami_date"]
        group outfit_pregnant auto variant "pose01" if_all ["breemc", "pregnant"] if_any ["minami_date"]

        group outfit auto variant "pose02" if_all ["breemc"] if_not "minami_date"
        group outfit_pregnant auto variant "pose02" if_all ["breemc", "pregnant"] if_not ["minami_date"]


        group outfit auto variant "pose01" if_all ["breemc", "halloween"]
        group outfit_pregnant auto variant "pose01" if_all ["breemc", "pregnant", "halloween"]


        group outfit auto variant "pose02" if_all ["breemc"] if_not ["halloween"]
        group outfit_pregnant auto variant "pose02" if_all ["breemc", "pregnant"] if_not ["halloween"]

        group jacket auto


        group collars auto if_not ["morgan_halloween", "shiori_sexydate", "shiori_sexywork"]
        group collars auto variant "bree_sexydate" if_any ["bree_sexydate"]
        group collars auto variant "sasha_sluttydate" if_all ["sasha_sluttydate", "mikemc"]
        group collars auto variant "shiori_sexydate" if_any ["shiori_sexydate", "shiori_sexywork"] if_all ["mikemc"]

        group necklaces auto if_not ["reona_collar"]

        always "dance_hat_camila_sluttydate" if_all ["camila_sluttydate"]

        group hairs auto if_not ["camila_halloween", "camila_sluttydate", "samantha_sexydate", "samantha_sluttydate"]
        group hairs auto variant "pose02" if_all ["minami"] if_not ["minami_date"]
        group hairs auto variant "pose01" if_all ["minami", "minami_date"]

        group hairs auto variant "pose01" if_all ["sasha", "mikemc"] if_not ["sasha_sluttydate", "sasha_halloween"]
        group hairs auto variant "sexydate" if_all ["sasha_sluttydate", "mikemc"]
        group hairs auto variant "pose02" if_all ["sasha", "breemc"]

        group hat auto
        group hat auto variant "haircut" if_any ["cherie_haircut"]
        group hat auto variant "nohaircut" if_any ["cherie_nohaircut"]

        group exp auto variant "breemc" if_any "breemc"

        group acc auto if_not ["angela_pregnant"]
        group acc_pregnant auto if_any ["angela_pregnant"]
        group glasses auto


        group armsoutfit auto variant "breemc_pose02" if_all ["breemc", "mike"]

        group forearms auto variant "mikemc" if_all "mikemc" if_not ["minami_pregnant"]
        group forearms auto variant "mikemc_pregnant" if_all ["mikemc", "minami_pregnant"]

        group forearms auto variant "breemc" if_all "breemc" if_not ["harmony_pregnant"]
        group forearms auto variant "breemc_pregnant" if_all ["breemc", "harmony_pregnant"]
        group forearms auto variant "breemc_pose01" if_all ["breemc", "halloween"]


        group mc auto variant "pose02" if_all ["breemc"] if_not ["halloween"]
        group mc_outfit auto variant "breemc_pose02" if_all ["breemc"] if_not ["halloween"]:
            attribute mcdate default
        group forearms auto variant "breemc_pose02" if_all ["breemc"] if_not ["halloween"]


        group mc auto variant "pose02" if_all ["breemc"] if_any ["danny", "dwayne", "jack", "master", "mike", "ryan", "sasha", "scottie", "shawn",  "victor"]
        group mc_outfit auto variant "breemc_pose02" if_all "breemc" if_any ["danny", "dwayne", "jack", "master", "mike", "ryan", "sasha", "scottie", "shawn",  "victor"]:
            attribute mcdate default
        group forearms auto variant "breemc_pose02" if_all "breemc" if_any ["danny", "dwayne", "jack", "master", "mike", "ryan", "sasha", "scottie", "shawn",  "victor"]


        group npcsarms auto if_all "mikemc"
        group outfit_boobjob auto if_all ["sasha_boobjob", "sasha_sluttydate", "mikemc"]


        group mc_acc auto variant "breemc_pose02" if_all "breemc" if_any ["danny", "dwayne", "jack", "master", "mike", "ryan", "sasha", "scottie", "shawn",  "victor"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
