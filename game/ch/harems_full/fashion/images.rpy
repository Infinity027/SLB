init 1:
    layeredimage fashion doggy:
        attribute_function MultiPickers([CollarPicker, DickPicker, PiercingsPicker, PregnancyPicker, HaircutPicker], npcs=[palla, sasha])

        attribute sasha null
        attribute palla_glasses null


        group bg auto:
            attribute store default
            attribute bedroom1
            attribute bedroom3


        attribute mike if_not ["bj"]


        attribute sasha_nohaircut
        attribute sasha_haircut


        always:
            if_not ["bj"]
            "fashion_doggy_palla_face"


        group exp_palla auto if_not ["bj"]:
            attribute normal default
            attribute pleasure
            attribute ahegao


        attribute palla_haircut null
        attribute palla_nohaircut null
        group hair auto if_not ["bj"]:
            attribute pony
            attribute loose
        group hair_hand auto if_any ["mike"] if_not ["bj"]:
            attribute pony
            attribute loose


        attribute cumonpalla null
        group cumonpalla auto if_any ["cumonpalla"] if_not ["bj"]:
            attribute facial default
            attribute mouth


        group exp_sasha auto:
            attribute open default
            attribute close


        attribute palla_collar
        attribute sasha_collar null


        group sasha_hand auto :
            attribute noleash default
            attribute leash if_any ["palla_collar"]


        always:
            "fashion_doggy_bodies"


        group strapon auto:
            attribute single default
            attribute double


        attribute palla_pregnant
        attribute sasha_pregnant


        attribute sasha_boobjob


        always:
            if_all ["leash", "palla_collar"]
            "fashion_doggy_palla_leash"


        attribute glasses


        attribute bj null
        always:
            if_any ["bj"]
            "fashion_doggy_bj_mike"


        attribute cuminside if_any ["bj"]


        group bj_hair auto if_any ["bj"]:
            attribute pony default
            attribute loose


        group multiple auto variant piercings
        group multiple auto variant piercings_bb when bb
        group multiple auto variant piercings_notbb when not sasha_boobjob
        group multiple auto variant piercings_bj when bj
        group multiple auto variant piercings_notbj when not bj
        attribute palla_clit null
        attribute palla_lips null
        attribute palla_tongue null
        attribute sasha_clit null
        attribute sasha_lips null
        attribute sasha_navel null
        attribute sasha_pregnant_navel null
        attribute sasha_tongue null


        group dick auto if_not ["bj"] if_all ["mike"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["mouth", "bj"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["bj"]


        always:
            if_any["bedroom3"]
            "fashion_doggy_curtains"


        attribute closeup null
        group closeup auto if_any ["closeup"]:
            attribute store default
            attribute bedroom1
            attribute bedroom3


        always:
            if_any ["closeup"]
            "fashion_doggy_closeup_palla"


        group closeup_sexpose auto if_any ["closeup"] if_not ["double"]:
            attribute vaginal default
            attribute analDP
        always:
            if_all ["closeup", "double"]
            "fashion_doggy_closeup_sexpose_analdp"

    layeredimage fashion licking:
        attribute_function MultiPickers([CollarPicker, PubesPicker, PiercingsPicker, PregnancyPicker, HaircutPicker], npcs=[palla, sasha])


        group bg auto:
            attribute store default
            attribute bedroom1
            attribute bedroom3


        always:
            "fashion_licking_bodies"


        attribute palla_pubes null
        attribute sasha_pubes


        attribute squirt


        group multiple auto variant collars


        group multiple auto variant nokiss when not mike


        group strand auto if_not ["mike"]:
            attribute sasha_nohaircut
            attribute sasha_haircut


        attribute mike


        attribute sasha_pregnant
        attribute palla_pregnant null


        always:
            if_not ["sasha_boobjob","mike"]
            "fashion_licking_sasha_notboobjob"
        always:
            if_not ["mike"]
            if_any ["sasha_boobjob"]
            "fashion_licking_sasha_boobjob"


        group multiple auto variant kiss when mike


        group exp_sasha auto if_not ["mike"]:
            attribute neutral default
            attribute pleasure
            attribute climax


        group multiple auto variant piercings
        group multiple auto variant piercings_kiss when kiss
        group multiple auto variant piercings_nokiss when not mike
        group multiple auto variant piercings_nokiss_bb when sasha_boobjob and not mike
        group multiple auto variant piercings_nokiss_notbb when not (sasha_boobjob or mike)
        attribute palla_clit null
        attribute palla_lips null
        attribute palla_tongue null
        attribute palla_navel null
        attribute palla_pregnant_navel null
        attribute sasha_lips null
        attribute sasha_tongue null


        group lick auto:
            attribute middle default
            attribute up
            attribute down


        attribute palla_haircut null
        attribute palla_nohaircut null
        group hair_palla auto:
            attribute pony default
            attribute loose
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
