init 1:
    layeredimage band threesome:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PubesPicker, PregnancyPicker, DickPicker, XrayPicker], npcs=[kleio], append_npc_from_attributes=True)


        always "band_threesome_bg"


        always "band_threesome_kleio_haircut_back" if_any ["kleio_haircut"]


        group mikehead auto:
            attribute normal default


        group mikeexp auto variant "normal" if_any ["normal"]:
            attribute happy default


        attribute kleio null
        always "band_threesome_bodies"


        group kleio_tattoo auto


        attribute kleio_collar


        group multiple auto variant piercings_kleio


        group kleiomouth auto:
            attribute kleio_happy default


        attribute kleio_haircut


        always "band_threesome_mikehand"


        attribute xray null
        group xray auto if_any ["xray"]


        attribute anna


        group multiple auto variant piercings_anna when anna


        attribute anna_pubes if_any ["anna"]


        group annahead auto if_any ["anna"]:
            attribute watch default


        attribute anna_collar null
        group anna_collar auto if_all ["anna", "anna_collar"]


        group multiple auto variant piercings_anna_watch when anna and watch
        group multiple auto variant piercings_anna_blowjob when anna and blowjob
        group multiple auto variant piercings_anna_deep when anna and deep


        group annaeyes auto if_all ["anna", "watch"]:
            attribute open default


        group annamouth auto if_all ["anna", "watch"]:
            attribute anna_happy default


        group fuckpos:
            attribute out null
            attribute vaginal null
            attribute anal null
            attribute blowjob null
            attribute deep null


        group dick auto
        group dick auto variant "out" if_any ["out"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cum"]
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cum"]
        group condomcum auto if_all ["out", "condom", "cum"]


        group mike_pubes auto
        group mike_pubes auto variant "out" if_any ["out"]


        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto if_all ["out", "dickcum"] if_not ["condom"]


        attribute bodycum


        attribute facecum if_all ["anna", "watch"]
        attribute facedrip if_all ["anna", "watch"]


        group annahand auto if_any ["anna"]:
            attribute stroke if_any ["out"]
            attribute finger if_not ["anal", "deep"]


        attribute anna_pregnant
        attribute kleio_pregnant


        group multiple auto variant piercings_anna_nav when anna_nav

    layeredimage empty_stage:
        always:
            "concert_bg_stage"
        always:
            "concert_fg"

    layeredimage bus_tour:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker], npcs=[anna, kleio, sasha])
        always:
            "bus_tour_bg"

        always:
            "bus_tour_mike"
        attribute anna
        attribute kleio
        attribute sasha

        group multiple auto variant collars
        group multiple auto variant piercings
        group multiple auto variant pregnancy
        attribute sasha_boobjob
        group multiple auto variant haircuts


    layeredimage picnic:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker, EndingKidPicker], npcs=[anna, kleio])
        always:
            "picnic_bg"

        attribute anna
        attribute kleio
        attribute kleio_haircut
        group multiple auto variant collars
        group multiple auto variant piercings

        attribute kleio_kid

        always:
            "picnic_mike"
        always:
            "picnic_food"
        attribute anna_kid
        always:
            "picnic_bg_shadow"

    layeredimage band foursome:
        attribute_function MultiPickers([DickPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, PubesPicker], npcs=[anna, kleio, sasha])


        always:
            "band_foursome_bg"


        attribute sasha


        group multiple auto variant pubic


        attribute kleio


        group tattoos auto


        attribute anna


        group multiple auto variant pregnancy


        attribute cum null
        group multiple auto variant cum when cum


        group multiple auto variant hair



        group exp_sasha auto:
            attribute sashanormal default
            attribute sashapleasure
            attribute sashaahegao

        group exp_kleio auto:
            attribute kleionormal default
            attribute kleiopleasure
            attribute kleioahegao


        group multiple auto variant piercings


        group mike auto:
            attribute fucksasha default
            attribute fuckkleio
            attribute fuckanna


        group dick auto


        group sashafucked auto:
            attribute blowjob null
            attribute vaginal null
            attribute anal null


        group dick auto variant "anal" if_any ["anal"]


        group multiple auto variant drip


        group dick auto variant "vaginal" if_any ["vaginal"]


        group multiple auto variant pubic_vaginal when vaginal


        group multiple auto variant piercings_vaginal when vaginal


        attribute sasha_pregnant


        group multiple auto variant collars


        attribute onsashabody if_any ["cum"]


        group multiple auto variant bb


        group multiple auto variant piercings_nav
        group multiple auto variant piercings_notbb when not sasha_boobjob
        group multiple auto variant piercings_bb when bb


        always:
            if_not ["blowjob"]
            "band_foursome_anna_head_nobj"
        always:
            if_any ["blowjob"]
            "band_foursome_anna_head_bj"


        group exp_anna auto variant "nobj" if_not ["blowjob"]:
            attribute annanormal default
            attribute annapleasure
            attribute annaahegao
        group exp_anna auto variant "bj" if_any ["blowjob"]:
            attribute annanormal default
            attribute annapleasure
            attribute annaahegao


        group multiple auto variant piercings_nobj when not blowjob
        group multiple auto variant piercings_bj when bj


        group dick auto variant "blowjob" if_any ["blowjob"]

        group dick_out auto variant "small" if_any ["small"] if_not ["blowjob", "vaginal", "anal"]
        group dick_out auto variant "medium" if_any ["medium"] if_not ["blowjob", "vaginal", "anal"]
        group dick_out auto variant "big" if_any ["big"] if_not ["blowjob", "vaginal", "anal"]


        attribute dickcum null
        group dickcum_out auto variant "small" if_all ["dickcum", "small"] if_not ["condom", "blowjob", "vaginal", "anal"]
        group dickcum_out auto variant "medium" if_all ["dickcum", "medium"] if_not ["condom", "blowjob", "vaginal", "anal"]
        group dickcum_out auto variant "big" if_all ["dickcum", "big"] if_not ["condom", "blowjob", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
        group cumshot_out auto variant "small" if_all ["cumshot", "small"] if_not ["condom", "blowjob", "vaginal", "anal"]
        group cumshot_out auto variant "medium" if_all ["cumshot", "medium"] if_not ["condom", "blowjob", "vaginal", "anal"]
        group cumshot_out auto variant "big" if_all ["cumshot", "big"] if_not ["condom", "blowjob", "vaginal", "anal"]
        group cumshot auto variant "blowjob" if_all ["cumshot", "blowjob"] if_not ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"]
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["condom"]
        group creampie auto variant "anal" if_all ["creampie", "anal"]


        attribute condom null
        group condom_out auto variant "small" if_all ["condom", "small"] if_not ["cumshot", "blowjob", "vaginal", "anal"]
        group condom_out auto variant "medium" if_all ["condom", "medium"] if_not ["cumshot", "blowjob", "vaginal", "anal"]
        group condom_out auto variant "big" if_all ["condom", "big"] if_not ["cumshot", "blowjob", "vaginal", "anal"]
        group condom auto variant "vaginal" if_all ["condom", "vaginal"] if_not ["cumshot"]


        group condomcum_out auto variant "small" if_all ["condom", "small"] if_any ["cumshot", "creampie"]
        group condomcum_out auto variant "medium" if_all ["condom", "medium"] if_any ["cumshot", "creampie"]
        group condomcum_out auto variant "big" if_all ["condom", "big"] if_any ["cumshot", "creampie"]

    layeredimage band foursome2:
        attribute_function MultiPickers([DickPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker], npcs=[anna, kleio, sasha])


        group bg auto:
            attribute bedroom1 default
            attribute bedroom3


        always:
            "band_foursome2_mike"


        attribute kleio
        attribute kleio_collar


        group multiple auto variant piercings_pussy


        attribute anna


        attribute sasha


        group multiple auto variant pregnancy



        group exp_kleio auto:
            attribute kleionormal default
            attribute kleiopleasure

        group exp_anna auto:
            attribute annanormal default
            attribute annapleasure
            attribute annaahegao


        always:
            "band_foursome2_sasha_eyes"


        attribute sasha_nohaircut
        attribute sasha_haircut


        group multiple auto variant piercings


        group multiple auto variant drip 


        attribute cum null
        group multiple auto variant cum 


        group dick auto:
            attribute blowjob
            attribute vaginal
            attribute anal


        always:
            if_not ["blowjob"]
            "band_foursome2_sasha_mouth"


        group dick_out auto if_not ["blowjob", "vaginal", "anal"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "blowjob", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
        group cumshot_out auto if_any ["cumshot"] if_not ["condom", "blowjob", "vaginal", "anal"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom_out auto if_any ["condom"] if_not ["cumshot", "blowjob", "vaginal", "anal"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["blowjob", "vaginal", "anal"]


        attribute mikehand if_any ["out"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
