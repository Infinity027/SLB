init 1:
    layeredimage college oral:
        attribute_function MultiPickers([CollarPicker, DickPicker, PiercingsPicker, PregnancyPicker, DayNightPicker], npcs=[anna, bree])


        always:
            "college_oral_bg"


        group period auto


        always:
            "college_oral_bodies"


        group multiple auto variant collars


        always:
            "college_oral_electrodes"


        group exp_mike auto:
            attribute neutral default


        group multiple auto variant pregnancy


        attribute naked null
        always:
            if_not ["anna_pregnant", "naked"]
            "college_oral_outfit_anna_normoutfit"
        always:
            if_not "naked"
            if_all ["anna_pregnant"]
            "college_oral_outfit_anna_pregnoutfit"


        always:
            if_not "naked"
            "college_oral_outfit_bree_underwear"


        group dick auto if_not ["bj"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["bj"]


        attribute cum


        group bree_hand auto :
            attribute bhandonleg default
            attribute bhandjob


        group bree_head auto:
            attribute hj default


        group exp_bree auto variant "hj" if_any ["hj"]:
            attribute breeopen default

        group exp_bree auto variant "bj" if_any ["bj"]:
            attribute breeopen default


        group multiple auto variant bree_cum when cum and not bj


        group anna_head auto:
            attribute hj default


        group exp_anna auto variant "hj" if_any ["hj"]:
            attribute annaopen default

        group exp_anna auto variant "bj" if_any ["bj"]:
            attribute annaopen default


        group multiple auto variant mike_hand_bj when bj


        group multiple auto variant mike_hand_hj when hj


        group anna_hand auto:
            attribute ahandonleg default

        group anna_hand auto variant "outfit" if_not ["naked"]


        group multiple auto variant anna_cum when cum and not bj


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["bj"]


        group multiple auto variant piercings_bj when bj
        group multiple auto variant piercings_hj when hj
        attribute anna_clit null
        attribute anna_lips null
        attribute anna_navel null
        attribute anna_pregnant_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        attribute anna_ears null
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_pregnant_navel null
        attribute bree_tongue null
        attribute bree_ears null

    layeredimage college cowgirl:
        attribute_function MultiPickers([CollarPicker, DickPicker, PiercingsPicker, DayNightPicker], npcs=[bree], append_npc_from_attributes=True)


        attribute bedroom1 null
        always:
            if_any ["bedroom1"]
            "college_cowgirl_bg_bedroom1"


        attribute bedroom2 null
        group bg_bedroom2_period auto if_any ["bedroom2"]:
            attribute day
            attribute night


        attribute bree null
        always:
            "college_cowgirl_breemike"


        attribute pussywet


        group exp_bree auto:
            attribute normal default
            attribute close
            attribute ahegao


        attribute dickout null
        group sex_bot auto variant "vaginal" if_any ["vaginal"] if_not ["dickout", "anal"]
        group sex_bot auto variant "anal" if_any ["anal"] if_not ["dickout", "vaginal"]
        group sex_bot auto variant "dickout" if_any ["dickout"] if_not ["anal", "vaginal"]


        always:
            if_any ["anal"]
            "college_cowgirl_sex_bot_anal_dickin"


        always:
            if_any ["vaginal"]
            "college_cowgirl_sex_bot_vaginal_dickin"


        group sex_bot_cum auto if_any ["cum"] if_not ["condom"]:
            attribute anal
            attribute vaginal


        group sex_bot_condom auto if_any ["condom"] if_not ["cum"]:
            attribute anal
            attribute vaginal


        attribute phone
        attribute flash


        group mike_rhand auto :
            attribute pick
            attribute grab


        group anna_hand auto if_any ["anna"]:
            attribute fingering
            attribute electremote
            attribute vibremote


        attribute anna


        group exp_anna auto if_any ["anna"]:
            attribute lust default
            attribute evil
            attribute surprised


        group multiple auto variant collars


        always:
            "college_cowgirl_electrodes"

        attribute turnon


        group vibrator_bree auto :
            attribute analvib
            attribute vaginalvib


        group sex_bot_dickout_dick auto if_any ["dickout"]


        attribute cumshot null
        group sex_bot_dickout_cumshot auto if_any ["cumshot"] if_not ["condom", "anal", "vaginal"]


        attribute cum null
        group sex_bot_dickout_cum auto if_any ["cum"] if_not ["condom", "anal", "vaginal"]


        attribute cum null
        group sex_bot_dickout_condomcum auto if_all ["condom", "cum"] if_not ["anal", "vaginal"]


        attribute condom null
        group sex_bot_dickout_condom auto if_any ["condom"] if_not ["cum", "anal", "vaginal"]


        group multiple auto variant piercings
        group multiple auto variant piercings_anna when anna
        attribute anna_clit null
        attribute anna_lips null
        attribute anna_navel null
        attribute anna_pregnant_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        attribute anna_ears null
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_pregnant_navel null
        attribute bree_tongue null
        attribute bree_ears null

    layeredimage college experiment:


        always:
            "college_experiment_bg"


        always:
            "college_experiment_annabody"


        group exp_anna auto:
            attribute normal default
            attribute confused
            attribute panic


        group anna_rhand auto:
            attribute rtab default
            attribute rup


        group anna_lhand auto:
            attribute ltab default
            attribute lup


        group bree_leg auto:
            attribute legdown default
            attribute legup


        group bree_lhand auto:
            attribute ltense
            attribute thumb


        always:
            "college_experiment_breebody"
        always:
            "college_experiment_shoulder"


        attribute rstill null
        attribute rtense null
        always:
            if_not ["rtense"]
            "college_experiment_bree_rhand_rstill"


        attribute wet


        always:
            "college_experiment_electrodes"


        attribute turnon


        attribute electrofx


        group bree_head auto:
            attribute steady default
            attribute climax


        attribute blush if_not ["climax"]


        group exp_bree auto if_not ["climax"]:
            attribute wink
            attribute nervous default
            attribute look
            attribute pleasure


        always:
            if_any ["rtense"]
            if_not ["rstill"]
            "college_experiment_bree_rhand_rtense"


        always:
            if_not ["ltense", "thumb"]
            "college_experiment_bree_lhand_lstill"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
