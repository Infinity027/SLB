init 1:
    layeredimage college oral:
        attribute_function MultiPickers([CollarPicker, DickPicker, DayNightPicker], npcs=[anna, bree])


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

        attribute anna_clit null
        attribute anna_lips null
        attribute anna_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        attribute anna_ears null
        attribute bree_clit null
        attribute bree_lips null
        attribute bree_navel null
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
