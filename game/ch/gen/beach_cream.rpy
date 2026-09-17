init python:
    class BeachCreamPicker(object):
        def __call__(self, attr):
            if hero.is_female:
                if attr & {"lexi", "sasha", "jack", "shawn", "master", "scottie"}:
                    attr.add("01")
                    if attr & {"lexi"}:
                        attr.add("right")
                elif attr & {"angela", "danny", "dwayne", "ryan", "victor", "mike"}:
                    attr.add("02")
            else:
                if attr & {"harmony", "anna", "palla", "hanna", "bree", "lexi", "shiori", "amy", "kat", "reona", "cherie", "claire", "kiara"}:
                    attr.add("01")
                    if randint(0, 1) == 1:
                        attr.add("right")
                elif attr & {"audrey", "alexis", "cassidy", "aletta", "samantha", "lavish", "minami", "morgan", "camila"}:
                    attr.add("02")
                elif attr & {"kleio", "sasha", "emma"}:
                    attr.add("03")
            
            if game.room in ["pool", "date_livingroom"]:
                attr.add("pool")
            if enable_debug_picker:
                renpy.log(f"BeachCreamPicker results: {attr}")
            return attr

init 1:
    layeredimage beach cream:
        attribute_function MultiPickers([BeachCreamPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker, MCCGPicker], use_morgan_cg_outfits=True, append_npc_from_attributes=True, add_simple_pregnant_attribute=True)

        attribute mikemc null
        attribute breemc null

        attribute nomc null
        attribute swimsuit null


        group bg auto
        group bg auto variant pool when pool


        group mikemc auto when mikemc and not nomc
        group mikemc auto variant left when mikemc and not (nomc or right)

        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group pillow auto


        group npc auto
        group npc auto variant mikemc when mikemc
        group npc auto variant breemc when breemc

        group boobjob auto variant breemc when breemc:
            attribute sasha_noboobjob null


        group collars auto:
            attribute aletta_collar null

        group collars auto variant mikemc when mikemc
        group collars auto variant breemc when breemc

        attribute naked null
        attribute topless null

        group top auto when not (naked or topless)
        group bot auto when not naked

        group top auto variant mikemc when mikemc and not (naked or topless)
        group bot auto variant mikemc when mikemc and not naked

        group top auto variant breemc when breemc and not (naked or topless)
        group top auto variant boobjob_breemc when breemc and sasha_boobjob and not (naked or topless)
        group top auto variant noboobjob_breemc when breemc and sasha_noboobjob and not (naked or topless)
        group bot auto variant breemc when breemc and not naked


        group pregnancies auto when not (cassidy_sexyswimsuit or lavish_swimsuit)
        group pregnancies auto variant mikemc when mikemc

        group top auto when morgan and not (naked or topless)
        group bot auto when morgan and not naked

        group haircuts auto
        group haircuts auto variant mikemc when mikemc
        group haircuts auto variant breemc when breemc

        group breemc auto when breemc and not nomc
        group mchaircuts auto variant 01 when breemc and 01 and not nomc:
            attribute mc_nohaircut null
        group mchaircuts auto variant 02 when breemc and 02 and not nomc:
            attribute mc_nohaircut null
        group mcoutfits auto variant 01 when breemc and 01 and not nomc:
            attribute mc_naked null
        group mcoutfits auto variant 02 when breemc and 02 and not nomc:
            attribute mc_naked null

        group npc auto variant breemc_right when breemc and right

        group collars auto variant breemc_right when breemc and right

        group top auto variant breemc_right when breemc and right and not (naked or topless)
        group bot auto variant breemc_right when breemc and right and not naked

        group haircuts auto variant breemc_right when breemc and right

        group hands auto
        group hands auto variant breemc when breemc
        group mchands auto when mikemc and not nomc
        group mchands auto variant right when mikemc and right and not nomc

        group bottle auto

        group glasses auto

        attribute morgan_makeup

        attribute right null
        group mikemcarm auto when mikemc and right and 01 and not nomc
        group mikemc auto variant right when mikemc and right and not nomc