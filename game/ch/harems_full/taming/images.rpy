init 1:
    layeredimage taming threesome:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker], npcs=[ayesha, kylie])


        always:
            "taming_threesome_bg"
        group mike auto
        always:
            "taming_threesome_girlsbodies"


        group multiple auto variant collars


        group multiple auto variant pregnancy


        group head_ayesha auto:
            attribute ayesha_blush default

        group head_kylie auto:
            attribute kylie_blush default


        group multiple auto variant piercings
        group multiple auto variant piercings_ayesha_moan when ayesha_moan
        group multiple auto variant piercings_ayesha_blush when ayesha_blush
        group multiple auto variant piercings_kylie_moan when kylie_moan
        group multiple auto variant piercings_kylie_blush when kylie_blush

    layeredimage taming bj:

        attribute_function MultiPickers([DickPicker, CollarPicker, PiercingsPicker], npcs=[ayesha, kylie])


        always "taming_bj_bg"
        always "taming_bj_body_mike"
        attribute ayesha
        attribute kylie

        group penis auto

        group collars auto

        group multiple auto variant piercings

    layeredimage taming blowjob:
        attribute_function MultiPickers([DickPicker, CollarPicker, PiercingsPicker], npcs=[ayesha, kylie])

        always:
            "taming_blowjob_bg"

        always:
            "taming_blowjob_mike"

        attribute ayesha

        attribute kylie

        group multiple auto variant collars

        always:
            "taming_blowjob_ayesha_head"

        always:
            "taming_blowjob_kylie_head"

        group multiple auto variant piercings

        group ayeshamouth auto if_not ["ayeshasuck"]:
            attribute ayeshasmile default

        group kyliemouth auto if_not ["kyliesuck"]:
            attribute kyliesmile default

        group ayeshaeyes auto:
            attribute ayeshaopened default

        group kylieeyes auto:
            attribute kylieopened default

        group dick auto if_not ["ayeshasuck", "kyliesuck"]

        group suck auto

        group multiple auto variant cum

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        attribute hold null
        always:
            if_any "hold"
            "taming_blowjob_hands_rightayesha"

        always:
            "taming_blowjob_hands_rightkylie"

        always:
            "taming_blowjob_hands_leftayesha"

        group mikehands auto:
            attribute still default

        always:
            "taming_blowjob_fg"

    layeredimage taming bondage:
        attribute_function Pickers([DickPicker, CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npc=kylie)

        always:
            "taming_bondage_bg"

        always:
            "taming_bondage_kylie"

        attribute pubes

        attribute pregnant

        attribute collar

        group multiple auto variant piercings

        attribute blush

        group exp auto:
            attribute shy default

        group multiple auto variant acc

        group vibrator auto

        group dick_outside auto if_all "mike" if_not ["anal", "vaginal"]
        group dick_inside auto if_all "mike" if_any ["anal", "vaginal"]

        attribute condom null
        group condom_outside auto if_all ["mike", "condom"] if_not ["anal", "vaginal"]
        group condom_inside auto if_all ["mike", "condom", "vaginal"]

        attribute cum null
        group condomcum auto if_all ["mike", "condom", "cum"] if_not ["anal", "vaginal"]
        group dickcum auto if_all ["mike", "cum"] if_not ["condom", "anal", "vaginal"]

        attribute cumshot null
        group cumshot auto if_all ["mike", "cumshot"]

        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_any ["anal", "vaginal"]

        group strapon auto if_any "ayesha":
            attribute outside default

        attribute hand

        group body auto

        attribute squirt

    layeredimage taming threesome ayeshafuck:
        attribute_function MultiPickers([DickPicker, CollarPicker, PiercingsPicker, PregnancyPicker], npcs=[ayesha], append_npc_from_attributes=True)

        always:
            "taming_threesome_ayeshafuck_bg"

        attribute ayesha

        attribute ayesha_pregnant

        attribute ayesha_collar

        group multiple auto variant piercings_ayesha

        group exp_ayesha auto:
            attribute ayeshanormal default

        attribute kylie

        attribute kylie_collar if_any "kylie"

        attribute kylie_pregnant if_any "kylie"

        group exp_kylie auto if_any "kylie":
            attribute kylienormal default

        group multiple auto variant piercings_kylie when kylie

        group dick_outside auto if_not ["anal", "vaginal"]
        group dick_inside auto if_any ["anal", "vaginal"]

        attribute condom null
        group condom_outside auto if_all ["condom"] if_not ["anal", "vaginal"]
        group condom_inside auto if_all ["condom", "vaginal"]

        attribute cum null
        group cum auto if_any "cum" if_not ["condom", "anal", "vaginal"]
        group dickcum auto if_all ["cum"] if_not ["condom", "anal", "vaginal"]
        group condomcum auto if_all ["condom", "cum"] if_not ["anal", "vaginal"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot"]

        attribute creampie null
        group creampie auto if_all ["creampie"] if_any ["anal", "vaginal"]

        attribute lick null
        group tongue auto if_all ["lick", "kylie"]

        attribute kyliehand if_any "kylie"

        attribute squirt if_any "kylie"

    layeredimage taming threesome kyliefuck:
        attribute_function MultiPickers([DickPicker, CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npcs=[kylie], append_npc_from_attributes=True)

        always:
            "taming_threesome_kyliefuck_bg"

        attribute kylie

        attribute kylie_pubes
        attribute kylie_pregnant

        attribute kylie_collar

        group multiple auto variant piercings_kylie

        group exp_kylie auto:
            attribute kylienormal default

        attribute mike

        group dick_outside auto if_all ["mike"] if_not ["anal", "vaginal"]
        group dick_inside auto if_all ["mike"] if_any ["anal", "vaginal"]

        attribute condom null
        group condom_outside auto if_all ["condom", "mike"] if_not ["anal", "vaginal"]
        group condom_inside auto if_all ["condom", "vaginal", "mike"]

        attribute cum null
        group cum auto if_all ["mike"] if_any "cum" if_not ["condom", "anal", "vaginal"]
        group dickcum auto if_all ["cum", "mike"] if_not ["condom", "anal", "vaginal"]
        group condomcum auto if_all ["condom", "cum", "mike"] if_not ["anal", "vaginal"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot", "mike"]

        attribute creampie null
        group creampie auto if_all ["creampie", "mike"] if_any ["anal", "vaginal"]

        group ayeshahand auto if_any "ayesha":
            attribute grab default

        attribute ayesha

        attribute ayesha_collar if_any "ayesha"

        group multiple auto variant piercings_ayesha when ayesha

        group ayesha_eyes auto if_any "ayesha":
            attribute opened default

        attribute lick if_any "ayesha"

        attribute cumdrip

    layeredimage taming harem beach ending:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, EndingKidPicker], npcs=[ayesha, kylie])

        always:
            "taming_harem_beach_ending_bg"


        attribute kylie
        attribute ayesha

        group multiple auto variant collars
        group multiple auto variant piercings

        group multiple auto variant kids

        always:
            "taming_harem_beach_ending_mike"

        always:
            "taming_harem_beach_ending_fg"

    layeredimage taming harem wrestling ending:
        attribute_function MultiPickers([EndingKidPicker], npcs=[ayesha, kylie])
        always:
            "taming_harem_wrestling_ending_bg"

        always:
            "taming_harem_wrestling_ending_mike"

        group multiple auto variant kids

        always:
            "taming_harem_wrestling_ending_ring"

        attribute ayesha

        attribute kylie

        always:
            "taming_harem_wrestling_ending_lights"

    layeredimage shower fight:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker], npcs=[ayesha, kylie])

        always "shower_fight_bg"
        always "shower_fight_bodies"
        always "shower_fight_ayesha_collar"
        always "shower_fight_kylie_collar"
        always "shower_fight_blade"

        group exp_ayesha auto:
            attribute normal default

        group exp_kylie auto:
            attribute surprised default

        attribute kylie_pregnant

        group multiple auto variant piercings
        group multiple auto variant piercings_normal if_not "press"
        group multiple auto variant piercings_press if_any "press"

    layeredimage taming cunnilingus:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npcs=[ayesha, kylie])

        always "taming_cunnilingus_bg"

        attribute ayesha

        attribute ayesha_pubes

        attribute ayesha_pregnant

        attribute ayesha_collar

        group multiple auto variant ayesha_piercings
        group multiple:
            attribute ayesha_ears null
            attribute ayesha_tongue null

        attribute cum

        attribute squirt

        attribute kylie

        group multiple auto variant kylie_piercings
        group multiple:
            attribute kylie_clit null
            attribute kylie_ears null
            attribute kylie_navel null
            attribute kylie_pregnant_navel null

        attribute kylie_collar null
        attribute kylie_pubes null
        attribute kylie_pregnant null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
