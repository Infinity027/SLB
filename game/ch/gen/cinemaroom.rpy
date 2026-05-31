init python:
    class CG_WatchMovie_Picker(object):
        def __call__(self, attr):
            g = attr & set(p.id for p in Person.all())
            g = list(g)[0] if g else None
            
            if g in ["bree", "camila", "aletta", "anna", "hanna", "cassidy", "mike", "scottie"]:
                attr.add("01")
            elif g in ["harmony", "angela", "alexis", "kleio", "shiori", "shawn", "victor", "amy", "kat", "reona"]:
                attr.add("02")
            elif g in ["palla", "ayesha", "audrey", "minami", "lexi", "danny", "jack"]:
                attr.add("03")
            elif g in ["morgan", "samantha", "lavish", "emma", "sasha", "kylie", "ryan", "master", "dwayne", "cherie", "claire", "kiara"]:
                attr.add("04")
            exp = attr & {"blush", "happy"}
            if exp:
                attr.add(g + list(exp)[0])
            
            if enable_debug_picker:
                renpy.log(f"CG_WatchMovie_Picker results: {attr}")
            return attr

init 1:
    layeredimage watch movie:
        attribute_function MultiPickers([CG_WatchMovie_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCCGPicker], append_npc_from_attributes=True, add_simple_pregnant_attribute=True)


        group bg auto


        attribute mc_casual null

        group mikemc auto if_any ["mikemc"]
        group mc_dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null
        group breemc auto if_any ["breemc"] if_not ["blowjob"]

        attribute mc_haircut null
        attribute mc_nohaircut null
        group breemc_haircut auto if_all ["breemc", "mc_haircut"] if_not ["blowjob"]


        group mc_arms:
            attribute normal null default
            attribute leg null
            attribute finger null
            attribute grab null
            attribute handjob null
            attribute blowjob null 


        group chair_fg auto variant "breemc" if_all ["breemc", "04"]


        group popcorn auto variant "mikemc" if_any ["mikemc"]
        group popcorn auto variant "breemc" if_any ["breemc"] if_not ["blowjob", "finger"]
        group popcorn_piece auto variant "mikemc" if_any ["mikemc"]


        group mikemc_arm auto variant "normal" if_all ["mikemc", "normal"]

        always "watch_movie_breemc_arm_normal_01" if_all ["breemc", "01"] if_not ["blowjob", "handjob"]
        always "watch_movie_breemc_arm_normal_02" if_all ["breemc", "02"] if_not ["blowjob", "handjob"]
        always "watch_movie_breemc_arm_normal_03" if_all ["breemc", "03"] if_not ["blowjob", "handjob"]
        always "watch_movie_breemc_arm_normal_04" if_all ["breemc", "04"] if_not ["blowjob", "handjob"]


        group chair_fg auto variant "mikemc" if_any ["mikemc"]
        group chair_fg auto variant "breemc" if_any ["breemc"] if_not ["04"]


        group grab auto if_all ["grab", "mikemc"]


        group npc auto
        group npc auto variant "mikemc" if_any ["mikemc"]
        group npc auto variant "breemc" if_any ["breemc"]


        group boobjob auto if_any ["sasha_boobjob"]


        group bot auto when mikemc and not finger
        group bot auto variant "fingout" if_all ["finger", "outside", "mikemc"]
        group bot auto variant "nograb" if_not ["finger", "grab"] if_all ["mikemc"]
        group top auto if_not ["grab"] if_all ["mikemc"]
        group top auto variant "nofinger" if_not ["grab", "finger"] if_all ["mikemc"]
        group top auto variant insidefinger when mikemc and finger and inside and not morgan 
        group top auto variant noinsidefinger when mikemc and not inside 
        group top auto variant noinsidefinger when mikemc and not finger 


        group outfit auto


        group bot auto variant pregnant when mikemc and not finger and morgan_pregnant
        group bot auto variant fingout_pregnant when mikemc and finger and outside and morgan_pregnant

        group top auto when mikemc and morgan and not (grab and inside) and not morgan_pregnant
        group top auto variant insidefinger when mikemc and morgan and finger and inside

        group top auto variant pregnant when mikemc and morgan_pregnant and not (grab and inside)
        group top auto variant insidefinger_pregnant when mikemc and morgan_pregnant and inside and finger


        group popcorn_piece auto


        attribute pregnant null
        group pregnancies auto
        group pregnancies auto variant casual when reona_casual
        group pregnancies auto variant purecasual when reona_purecasual
        group pregnancies auto variant insidefinger when inside and finger 
        group pregnancies auto variant noinsidefinger when not (inside or finger) 


        group collars auto


        group posexp:
            attribute happy null default
            attribute blush null
        group exp auto
        attribute morgan_makeup null
        group makeup auto if_any ["morgan_makeup"]


        group multiple auto variant piercings

        group piercings_hidden auto when not (morgan_blackjacket or morgan_bluesweater or reona_purecasual)

        group npc_arm_positions auto:
            attribute still null default
            attribute leg null
            attribute grab null
            attribute finger null

        group npc_arm auto variant "still" if_all ["breemc", "still"] if_not ["blowjob", "handjob"]
        group npc_arm auto variant "leg" if_all ["breemc", "leg"] if_not ["blowjob", "handjob"]
        group npc_arm auto variant "grab_outside" if_all ["breemc", "grab", "outside"] if_not ["blowjob", "handjob"]
        group npc_arm auto variant "grab_inside" if_all ["breemc", "grab", "inside"] if_not ["blowjob", "handjob"]
        group npc_arm auto variant "finger_outside" if_all ["breemc", "finger", "outside"] if_not ["blowjob", "handjob"]
        group npc_arm auto variant "finger_inside" if_all ["breemc", "finger", "inside"] if_not ["blowjob", "handjob"]


        group handjob auto if_all ["handjob", "breemc"]
        group blowjob auto if_all ["blowjob", "breemc"]


        group clothsdepth:
            attribute outside null default
            attribute inside null


        group grab auto variant "inside" if_all ["grab", "inside", "mikemc"]
        group grab auto variant "inside_preg" if_all ["grab", "inside", "mikemc", "pregnant"]
        group grab auto variant "inside_nopreg" if_all ["grab", "inside", "mikemc"] if_not ["pregnant"]
        group grab auto variant "inside_bb" if_all ["grab", "inside", "sasha_boobjob", "mikemc"]
        group grab auto variant "inside_nobb" if_all ["grab", "inside", "mikemc"] if_not ["sasha_boobjob"]
        group grab auto variant "outside" if_all ["grab", "outside", "mikemc"]
        group grab auto variant "outside_preg" if_all ["grab", "outside", "mikemc", "pregnant"]
        group grab auto variant "outside_nopreg" if_all ["grab", "outside", "mikemc"] if_not ["pregnant"]

        group grab auto variant "inside_reona" if_all ["grab", "inside", "mikemc", "reona"]
        group grab auto variant "outside_reona" if_all ["grab", "outside", "mikemc", "reona"]


        group finger auto variant "inside" if_all ["finger", "inside", "mikemc"]
        group finger auto variant "inside_preg" if_all ["finger", "inside", "mikemc", "pregnant"]
        group finger auto variant "inside_nopreg" if_all ["finger", "inside", "mikemc"] if_not ["pregnant"]
        group finger auto variant "outside" if_all ["finger", "outside", "mikemc"]
        group finger auto variant "outside_preg" if_all ["finger", "outside", "mikemc", "pregnant"]
        group finger auto variant "outside_nopreg" if_all ["finger", "outside", "mikemc"] if_not ["pregnant"]

        group finger auto variant "inside_preg_reona" if_all ["finger", "inside", "mikemc", "pregnant", "reona"]
        group finger auto variant "inside_nopreg_reona" if_all ["finger", "inside", "mikemc", "reona"] if_not ["pregnant"]

        group top auto variant insidefinger when morgan and inside and finger and morgan_bluesweater and not pregnant
        group top auto variant insidefinger_pregnant when morgan and inside and finger and morgan_bluesweater and pregnant


        group glasses auto


        group haircuts auto


        group fg auto variant "03"


        group mikemc_arm auto variant "leg" if_all ["mikemc", "leg"]


        group breemc_arm auto variant "handjob" if_all ["breemc", "handjob"] if_not ["blowjob"]
        group breemc auto variant "blowjob" if_all ["breemc", "blowjob"]
        group breemc_haircut auto variant "blowjob" if_all ["breemc", "blowjob", "mc_haircut"]


        group fg auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
