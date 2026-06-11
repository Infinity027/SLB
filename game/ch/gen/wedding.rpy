init python:
    class CG_Wedding_Picker(object):
        def __call__(self, attr):
            
            if attr & {"audrey", "bree", "kleio", "lexi", "mike", "minami", "samantha", "sasha", "shawn", "scottie"}:
                attr.add("01")
            elif attr & {"alexis", "camilla", "emma", "lavish", "master", "palla", "victor"}:
                attr.add("02")
            elif attr & {"amy", "cassidy", "cherie", "jack", "kat", "kiara", "morgan", "reona", "ryan"}:
                attr.add("03")
            elif attr & {"aletta", "angela", "anna", "claire", "danny", "dwayne", "hanna", "harmony", "shiori"}:
                attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_Wedding_Picker results: {attr}")
            return attr

init 1:
    layeredimage wedding:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, MCCGPicker, CG_Wedding_Picker], append_npc_from_attributes=True)


        attribute mc_casual null
        attribute mc_nohaircut null
        attribute mc_small null
        attribute mc_medium null
        attribute mc_big null

        attribute priest null


        group bg auto
        group priest auto when priest


        group mc auto variant 01 when 01
        group mc auto variant 03 when 03
        group mc auto variant 04 when 04
        group mc_haircut auto variant 01 when 01
        group mc_haircut auto variant 03 when 03
        group mc_haircut auto variant 04 when 04
        group mc_outfit auto variant 01 when 01
        group mc_outfit auto variant 03 when 03
        group mc_outfit auto variant 04 when 04
        group mc_outfit_preg auto variant 01 when 01 and mc_pregnant
        group mc_outfit_preg auto variant 03 when 03 and mc_pregnant
        group mc_outfit_preg auto variant 04 when 04 and mc_pregnant


        group npc auto


        group npc_makeup auto

        attribute sasha_nohaircut


        group npc_collars auto when (aletta or angela or anna or claire or hanna or shiori)


        group multiple auto variant npc_piercings


        group npc_outfit auto
        group npc_outfit_preg auto


        group npc_boobs auto


        group npc_collars auto when not (aletta or angela or anna or claire or hanna or shiori)


        group npc_hair auto


        group npc_accessories auto


        group mc auto variant 02 when 02
        group mc_haircut auto variant 02 when 02
        group mc_outfit auto variant 02 when 02
        group mc_outfit_preg auto variant 02 when 02 and mc_pregnant

        group mikemc_hand auto variant 03 when mikemc
        group breemc_hand auto variant 04 when breemc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
