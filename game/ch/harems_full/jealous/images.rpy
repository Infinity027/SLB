init 1:
    layeredimage jealous bj:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, MCCGPicker], npcs=[audrey, sasha])


        attribute audrey null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_nipples null
        attribute audrey_nohaircut null
        attribute audrey_tongue null
        attribute mc_casual null
        attribute mikemc null
        attribute sasha null
        attribute sasha_clit null
        attribute sasha_collar null
        attribute sasha_lips null
        attribute sasha_tongue null

        attribute audreysuck null
        attribute sashasuck null

        always:
            "jealous_bj_bg"

        always:
            "jealous_bj_mike"

        group dick auto:
            attribute normal default if_not ["sashasuck","audreysuck"]


        always:
            "jealous_bj_audrey"
        always:
            "jealous_bj_sasha"


        always:
            "jealous_bj_mike_hand"


        always:
            if_any "sashasuck"
            "jealous_bj_sasha_face_sashasuck"
        always:
            if_not "sashasuck"
            "jealous_bj_sasha_face_sashawatch"

        always:
            "jealous_bj_sashasuck_sasha_collar" when sashasuck


        always:
            if_any "audreysuck"
            "jealous_bj_audrey_face_audreysuck"
        always:
            if_not "audreysuck"
            "jealous_bj_audrey_face_audreywatch"

        group audreycollar auto variant "audreysuck" when audreysuck
        group audreycollar auto variant "audreywatch" when not audreysuck

        group multiple auto variant pregnancy

        attribute sasha_boobjob

        group multiple auto variant piercings_audreysuck when audreysuck
        group multiple auto variant piercings_audreywatch when not audreysuck
        group multiple auto variant piercings_sashasuck when sashasuck
        group multiple auto variant piercings_sashawatch when not sashasuck

        group multiple auto variant piercings_boobjob when sasha_boobjob
        group multiple auto variant piercings_noboobjob when not sasha_boobjob


        group haircuts auto variant "sashawatch" if_not "sashasuck"


        group sashaexp auto variant "sashasuck" if_any "sashasuck":
            attribute sashanormal default
        group sashaexp auto variant "sashawatch" if_not "sashasuck":
            attribute sashanormal default

        group audreyexp auto variant "audreysuck" if_any "audreysuck":
            attribute audreynormal default
        group audreyexp auto variant "audreywatch" if_not "audreysuck":
            attribute audreynormal default


        group haircuts auto variant "sashasuck" if_any "sashasuck"


        group dick auto variant sashasuck if_any "sashasuck"
        group cum auto variant sashasuck if_all ["sashasuck", "cum"]


        group dick auto variant audreysuck if_any "audreysuck"
        group cum auto variant audreysuck if_all ["audreysuck", "cum"]

        attribute cum null
        group multiple auto variant cum when cum

    layeredimage jealous cowgirl:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, MCCGPicker], npcs=[audrey, sasha])


        attribute audrey null
        attribute audrey_ears null
        attribute audrey_nohaircut null
        attribute audrey_tongue null
        attribute mc_casual null
        attribute mikemc null
        attribute sasha null
        attribute sasha_lips null
        attribute sasha_nose null
        attribute sasha_tongue null
        attribute sasha_pregnant_navel null

        always:
            "jealous_cowgirl_bg"
        always:
            "jealous_cowgirl_mike"



        always:
            "jealous_cowgirl_audrey"
        attribute audrey_pregnant


        group audreyexp auto:
            attribute audreynormal default


        group multiple auto variant audrey_piercings
        attribute audrey_collar


        attribute vaginal null
        attribute anal null
        attribute outside null
        group dick auto variant vaginal if_any ["vaginal"] if_not ["sashasuck", "anal"]
        group dick auto variant anal if_any ["anal"] if_not ["sashasuck", "vaginal"]

        attribute cum null
        group cum auto variant vaginal if_all ["vaginal", "cum"] if_not ["sashasuck", "anal"]
        group cum auto variant anal if_all ["anal", "cum"] if_not ["sashasuck", "vaginal"]



        always:
            if_any "sashasuck"
            "jealous_cowgirl_sashasuck_body"
        always:
            if_not "sashasuck"
            "jealous_cowgirl_sashafinger_hand"
        always:
            if_not "sashasuck"
            "jealous_cowgirl_sashafinger_body"


        group pregnancy auto variant sashasuck if_any "sashasuck"
        group pregnancy auto variant sashafinger if_not "sashasuck"


        attribute sasha_boobjob null
        group boobjob auto variant sashasuck if_all ["sashasuck", "sasha_boobjob"]
        group boobjob auto variant sashafinger if_any "sasha_boobjob" if_not "sashasuck"


        attribute sashasuck null
        group dick auto variant sashasuck if_any ["sashasuck"] if_not ["vaginal", "anal"]
        group cum auto variant sashasuck if_all ["sashasuck", "cum"] if_not ["vaginal", "anal"]


        group sashaexp auto variant sashasuck if_any "sashasuck":
            attribute sashanormal default
        group sashaexp auto variant sashafinger if_not "sashasuck":
            attribute sashanormal default


        group multiple auto variant sashapiercings_sashasuck if_any "sashasuck"
        group multiple auto variant sashapiercings_sashasuck_boobjob if_all ["sashasuck","sasha_boobjob"]
        group multiple auto variant sashapiercings_sashasuck_noboobjob if_not ["sasha_boobjob"]
        group multiple auto variant sashapiercings_sashafinger if_not "sashasuck"
        group multiple auto variant sashapiercings_sashafinger_boobjob if_not ["sashasuck"] if_any ["sasha_boobjob"]
        group multiple auto variant sashapiercings_sashafinger_noboobjob if_not ["sashasuck", "sasha_boobjob"]


        attribute sasha_collar if_not "sashasuck"


        group haircuts auto variant sashasuck if_any "sashasuck"
        group haircuts auto variant sashafinger if_not "sashasuck"


        attribute sasha_pubes null


        group dick auto variant outside if_not ["sashasuck", "vaginal", "anal"]


        group cum auto variant outside if_any ["cum"] if_not ["sashasuck", "vaginal", "anal"]


        attribute bodycum null

    layeredimage jealous doggy:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, MCCGPicker], npcs=[audrey, sasha])


        attribute audrey null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_navel null
        attribute audrey_nipples null
        attribute audrey_nohaircut null
        attribute audrey_tongue null
        attribute mc_casual null
        attribute sasha null
        attribute sasha_collar null
        attribute sasha_lips null
        attribute sasha_pregnant_navel null
        attribute sasha_tongue null
        attribute mikemc null


        always:
            "jealous_doggy_bg"




        always:
            "jealous_doggy_sasha_face"


        group haircuts auto


        group multiple auto variant facepiercings


        attribute mike null
        always:
            if_any "mike"
            "jealous_doggy_mike"


        always:
            "jealous_doggy_sasha_body"


        attribute sasha_pregnant


        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        always:
            if_any "sasha_boobjob"
            "jealous_doggy_sasha_boobjob"


        group multiple auto variant sashapiercings
        group multiple auto variant sashapiercings_boobjob if_any ["sasha_boobjob"]
        group multiple auto variant sashapiercings_noboobjob if_not ["sasha_boobjob"]


        group sashaexp auto:
            attribute sashanormal default



        attribute audreyfinger null
        attribute audreysuck null
        always:
            if_any "audreyfinger" if_not "audreysuck"
            "jealous_doggy_audreyfinger_body"
        always:
            if_any "audreysuck" if_not "audreyfinger"
            "jealous_doggy_audreysuck_body"


        group audreyexp auto variant audreyfinger if_any "audreyfinger" if_not "audreysuck":
            attribute audreynormal default
        group audreyexp auto variant audreysuck if_any "audreysuck" if_not "audreyfinger":
            attribute audreynormal default


        group multiple auto variant audreyacc_audreyfinger if_any "audreyfinger" if_not "audreysuck"
        group multiple auto variant audreyacc_audreysuck if_any "audreysuck" if_not "audreyfinger"


        attribute outside null
        attribute vaginal null
        attribute anal null
        group dick auto variant outside if_any ["outside"] if_not ["audreysuck", "vaginal", "anal"]
        group dick auto variant audreysuck if_any ["audreysuck"] if_not ["outside", "vaginal", "anal"]
        group dick auto variant vaginal if_any ["vaginal"] if_not ["audreysuck", "outside", "anal"]
        group dick auto variant anal if_any ["anal"] if_not ["audreysuck", "outside", "vaginal"]


        group condom auto variant vaginal if_all ["vaginal", "condom"] if_not ["audreysuck", "anal"]


        attribute cum null
        attribute onbody
        group cum auto variant outside if_all ["outside", "cum"] if_not ["audreysuck", "vaginal", "anal"]
        group cum auto variant audreysuck if_all ["audreysuck", "cum"] if_not ["vaginal", "anal"]
        group cum auto variant vaginal if_all ["vaginal", "cum"] if_not ["audreysuck", "anal"]
        group cum auto variant anal if_all ["anal", "cum"] if_not ["audreysuck", "vaginal"]

    layeredimage jealous missionary:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, MCCGPicker], npcs=[audrey, sasha])


        always:
            "jealous_missionary_bg"



        always:
            "jealous_missionary_audrey_body"


        attribute audrey_pregnant


        always:
            "jealous_missionary_audrey_shadow"


        attribute squirt


        attribute audrey_collar
        group multiple auto variant audrey_piercings


        attribute kiss null
        group audrey_exp auto variant "nokiss" if_not ["kiss"]:
            attribute normal default


        always:
            if_any ["kiss"]
            "jealous_missionary_audrey_kiss"
        group audrey_exp auto variant "kiss" if_any ["kiss"]




        group sasha_hairstrand auto


        always:
            "jealous_missionary_sasha_body"


        attribute sasha_pregnant


        attribute sasha_boobjob
        always:
            if_any "sasha_boobjob"
            "jealous_missionary_sasha_boobjob"


        group sasha_exp auto variant "nokiss" if_not ["kiss"]:
            attribute normal default


        group sasha_haircuts auto variant "nokiss" if_not ["kiss"]


        group multiple auto variant sasha_piercings
        group sasha_piercings auto variant "nokiss" if_any ["kiss"]
        group multiple auto variant sasha_piercings_boobjob if_any ["sasha_boobjob"]
        group multiple auto variant sasha_piercings_noboobjob if_not ["sasha_boobjob"]


        group sasha_exp auto variant "kiss" if_any ["kiss"]
        group sasha_haircuts auto variant "kiss" if_any ["kiss"]
        group sasha_piercings auto variant "kiss" if_any ["kiss"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
