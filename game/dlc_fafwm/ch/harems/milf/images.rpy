init 1:
    layeredimage milf 4some blowjob:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, MCCGPicker], npcs=[cherie, claire, kiara])


        attribute mikemc null
        attribute cherie null
        attribute claire null
        attribute kiara null
        attribute cherie_clit null
        attribute cherie_ears null
        attribute cherie_navel null
        attribute cherie_nipples null
        attribute cherie_pregnant_navel null
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nipples null
        attribute claire_pregnant_navel null
        attribute kiara_clit null
        attribute kiara_ears null
        attribute kiara_navel null
        attribute kiara_nipples null
        attribute kiara_pregnant_navel null
        attribute claire_collar null
        attribute kiara_collar null


        group bg auto:
            attribute bedroom default


        always "milf_4some_blowjob_bodies"


        attribute cherie_collar


        attribute cherie_blush


        group claire_mouth auto:
            attribute claire_lick default
        group kiara_mouth auto:
            attribute kiara_lick default
        group cherie_mouth auto:
            attribute cherie_lick default
            attribute cherie_suck null
        group cherie_mouth auto variant cherie_suck when cherie_suck

        attribute cum null
        group cum auto variant cherie_suck when cherie_suck and cum


        group multiple auto variant haircuts:
            attribute kiara_haircut
            attribute kiara_nohaircut
            attribute claire_haircut
            attribute claire_nohaircut
            attribute cherie_haircut
            attribute cherie_nohaircut


        group multiple auto variant piercings


        group multiple auto variant facecum


        group dick auto when cherie_lick
        group cum auto when cherie_lick and cum


        attribute mc_pubes


        always "milf_4some_blowjob_fg"

    layeredimage milf 4some fuckcherie:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker, MCCGPicker], npcs=[cherie, claire, kiara])


        attribute mikemc null
        attribute cherie null
        attribute claire null
        attribute kiara null
        attribute cherie_ears null
        attribute cherie_navel null
        attribute cherie_nose null
        attribute cherie_pregnant_navel null
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nipples null
        attribute claire_pregnant_navel null
        attribute claire_pubes null
        attribute kiara_ears null
        attribute kiara_pubes null
        group dickpos:
            attribute out null default
            attribute vaginal null
            attribute anal null
        attribute cherie_topless null
        attribute claire_topless null
        attribute kiara_topless null
        attribute cherie_bottomless null
        attribute claire_bottomless null
        attribute kiara_bottomless null
        attribute cum null


        group bg auto:
            attribute bedroom default

        always "milf_4some_fuckcherie_bodies"


        group multiple auto variant pregnancies


        group multiple auto variant piercings


        group multiple auto variant collars


        group top auto variant cherie when not cherie_topless:
            attribute cherie_naked null
        group top auto variant claire when not claire_topless:
            attribute claire_naked null
        group top auto variant kiara when not kiara_topless:
            attribute kiara_naked null
        group top_preg auto variant kiara when kiara_pregnant and not kiara_topless:
            attribute kiara_naked null
        group top_nopreg auto variant kiara when not kiara_pregnant and not kiara_topless:
            attribute kiara_naked null
        group bot auto variant cherie when not cherie_bottomless:
            attribute cherie_naked null
        group bot auto variant claire when not claire_bottomless:
            attribute claire_naked null
        group bot auto variant kiara when not kiara_bottomless:
            attribute kiara_naked null


        group multiple auto variant haircuts


        group dick auto variant vaginal when vaginal
        group dick auto variant anal when anal


        attribute cum null
        group cum auto variant vaginal when cum and vaginal
        group cum auto when cum


        group multiple auto variant pubes


        group dick auto variant out when out


        group cum auto variant out when cum and out


        group fg auto

    layeredimage milf 4some fuckclaire:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, HaircutPicker, MCCGPicker], npcs=[cherie, claire, kiara])


        attribute mikemc null
        attribute cherie null
        attribute claire null
        attribute kiara null
        attribute cherie_clit null
        attribute cherie_nose null
        attribute claire_clit null
        attribute claire_navel null
        attribute claire_nose null
        attribute claire_pregnant_navel null
        attribute kiara_clit null
        attribute kiara_ears null
        attribute kiara_navel null
        attribute kiara_nipples null
        attribute kiara_nose null
        attribute kiara_pregnant_navel null
        attribute cum null


        group bg auto:
            attribute bedroom default


        always "milf_4some_fuckclaire_bodies"


        group claire_exp auto:
            attribute claire_normal default


        group multiple auto variant pregnancies


        group multiple auto variant piercings


        group multiple auto variant collars


        group kiara_outfits auto variant nopreg when not kiara_pregnant:
            attribute kiara_naked null
        group kiara_outfits auto variant preg when kiara_pregnant:
            attribute kiara_naked null
        group cherie_outfits auto variant nopreg when not cherie_pregnant:
            attribute cherie_naked null
        group cherie_outfits auto variant preg when cherie_pregnant:
            attribute cherie_naked null
        group cherie_chains auto
        group claire_outfits auto:
            attribute claire_naked null


        group multiple auto variant haircuts


        group dickpos:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group dick auto variant out when out
        group dick auto variant vaginal when vaginal
        group dick auto variant anal when anal


        attribute condom null
        group condom auto variant out when condom and out
        group condom auto variant vaginal when condom and vaginal
        group condom auto variant anal when condom and anal


        attribute cum null
        group cum auto variant out when cum and out
        group cum auto variant vaginal when cum and vaginal and not condom
        group cum auto variant anal when cum and anal


        attribute bodycum


        group fg auto

    layeredimage milf 4some fuckkiara:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker, MCCGPicker], npcs=[cherie, claire, kiara])


        attribute mikemc null
        attribute cherie null
        attribute claire null
        attribute kiara null
        attribute cherie_collar null
        attribute cherie_ears null
        attribute cherie_navel null
        attribute cherie_pregnant_navel null


        group bg auto:
            attribute bedroom default


        always "milf_4some_fuckkiara_bodies1"
        always "milf_4some_fuckkiara_bodies2"


        group multiple auto variant pregnancy


        group multiple auto variant pubic


        attribute kiara_clit when not vaginal
        group multiple auto variant piercings_back


        group multiple auto variant outfits
        group multiple auto variant outfits_top when not cherie_pregnant
        group multiple auto variant outfits_top_preg when cherie_pregnant
        group multiple auto variant outfits_bot when not claire_pregnant
        group multiple auto variant outfits_bot_preg when claire_pregnant


        group kiara_exp auto:
            attribute kiara_normal default


        group multiple auto variant collars


        group multiple auto variant haircuts


        group multiple auto variant piercings_front


        attribute bodycum


        group dickpos:
            attribute out null default
            attribute vaginal null
            attribute anal null
        group dick auto variant out when out
        group dick auto variant vaginal when vaginal
        group dick auto variant anal when anal


        attribute dickcum null
        group dickcum auto variant out when dickcum and out
        group dickcum auto variant vaginal when dickcum and vaginal
        group dickcum auto variant anal when dickcum and  anal


        attribute cum null
        group cum auto variant out when cum and out
        group cum auto variant vaginal when cum and vaginal
        group cum auto variant anal when cum and  anal


        attribute kiara_clit variant vaginal_mc_big when vaginal and mc_big
        attribute kiara_clit variant vaginal_mc_medium when vaginal and mc_medium
        attribute kiara_clit variant vaginal_mc_small when vaginal and mc_small


        attribute vaginaldrip


        group fg auto

    layeredimage milf ending:
        attribute_function MultiPickers([EndingKidPicker], npcs=[claire, cherie, kiara])

        attribute claire null
        attribute cherie null
        attribute kiara null
        attribute claire_haircut null
        attribute claire_nohaircut null
        attribute cherie_haircut null
        attribute cherie_nohaircut null
        attribute kiara_haircut null
        attribute kiara_nohaircut null

        always "milf_ending_bg"
        always "milf_ending_mike"
        always "milf_ending_claire"
        always "milf_ending_kiara"
        always "milf_ending_cherie"
        always "milf_ending_snack_1"
        always "milf_ending_snack_2"
        always "milf_ending_bottle"
        group multiple auto variant kids:
            attribute cherie_kid
            attribute claire_kid
            attribute kiara_kid
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
