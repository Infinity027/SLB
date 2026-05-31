init 1:
    layeredimage sleep:
        attribute_function Pickers([SeasonPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker], clear_npc=True)
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        group bg auto

        group bg auto variant lexi when lexi:
            attribute livingroom default

        group girl auto

        attribute collar null
        group collar auto if_any "collar"

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any "haircut"
        group nohaircut auto if_not "haircut"
        group line auto

        attribute pregnant null
        group preg auto if_any "pregnant"

        attribute boobjob null

        group piercings:
            attribute nipples null
            attribute navel null
            attribute nose null
            attribute clit null
            attribute lips null
            attribute ears null
            attribute tongue null

        group nipples auto if_any "nipples" if_not "boobjob"
        group nipples_bb auto if_all ["nipples", "boobjob"]
        group navel auto if_any "navel"
        group nose auto if_any "nose"
        group clit auto if_all ["clit", "summer"]
        group lips auto if_any "lips"
        group ears auto if_any "ears"
        group tongue auto if_any "tongue"

        group outfit auto if_not "summer"
        group outfit_bb auto if_any "boobjob" if_not "summer"
        group outfit_preg auto if_any "pregnant" if_not "summer"

        group dick auto if_any ["summer"]

        group cover auto if_any "fall"
        group warmcover auto if_any "winter"

    layeredimage multisleep sashasam:
        attribute_function MultiPickers([SeasonPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, HaircutPicker], append_npc_from_attributes=True)
        attribute sasha null
        attribute samantha null

        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        always:
            "multisleep_sashasam_bg"


        always:
            if_any "sasha"
            "multisleep_sashasam_sasha"
        attribute sasha_pregnant

        group multiple auto variant sashapiercings
        group multiple auto variant sashapiercings_sasha_noboobjob when not sasha_boobjob

        always:
            if_any "sasha"
            if_not "summer"
            "multisleep_sashasam_outfit_sasha_underwear"

        always:
            if_all ["sasha", "sasha_pregnant", "sasha_underwear"]
            if_not "summer"
            "multisleep_sashasam_pregnant_outfit_sasha_pregnant_sasha_underwear"

        attribute sasha_haircut
        attribute sasha_nohaircut

        attribute sasha_boobjob when summer
        group multiple auto variant sashapiercings_sasha_boobjob when sasha_boobjob

        always:
            if_all ["sasha", "sasha_boobjob"]
            if_not "summer"
            "multisleep_sashasam_outfit_sasha_boobjob_underwear"

        always:
            "multisleep_sashasam_samantha"
        attribute samantha_pregnant

        group multiple auto variant collars

        group multiple auto variant piercings

        always:
            if_not "summer"
            "multisleep_sashasam_outfit_samantha_underwear"
        always:
            if_all ["samantha_pregnant", "samantha_underwear"]
            if_not "summer"
            "multisleep_sashasam_pregnant_outfit_samantha_pregnant_samantha_underwear"

        group multiple auto variant cover when fall
        always:
            if_any "winter"
            "multisleep_sashasam_warmcover"

    layeredimage multisleep breesam:
        attribute_function MultiPickers([SeasonPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], append_npc_from_attributes=True)
        attribute bree null
        attribute samantha null

        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        always:
            "multisleep_breesam_bg"

        always:
            if_any "bree"
            "multisleep_breesam_bree"

        attribute bree_pregnant

        always:
            "multisleep_breesam_samantha"
        attribute samantha_pregnant

        group multiple auto variant collars
        group multiple:
            attribute bree_collar null

        group multiple auto variant piercings
        group multiple:
            attribute bree_clit null
            attribute bree_tongue null
            attribute samantha_ears null
            attribute samantha_tongue null
        group multiple auto variant outfit when not summer
        group multiple auto variant pregnant_outfit_bree_pregnant when bree_pregnant and not summer
        group multiple auto variant pregnant_outfit_samantha_pregnant when samantha_pregnant and not summer

        always:
            if_any "fall"
            "multisleep_breesam_cover"

        always:
            if_any "winter"
            "multisleep_breesam_warmcover"

    layeredimage multisleep minamisam:
        attribute_function MultiPickers([SeasonPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, HaircutPicker], append_npc_from_attributes=True)
        attribute minami null
        attribute samantha null
        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        always:
            "multisleep_minamisam_bg"

        always:
            if_any "minami"
            "multisleep_minamisam_minami"
        attribute minami_pregnant
        attribute minami_haircut
        attribute minami_nohaircut

        always:
            "multisleep_minamisam_samantha"
        attribute samantha_pregnant

        group multiple auto variant collars

        group multiple auto variant piercings
        group multiple auto variant outfit when not summer
        group multiple auto variant pregnant_outfit_minami_pregnant when minami_pregnant and not summer
        group multiple auto variant pregnant_outfit_samantha_pregnant when samantha_pregnant and not summer

        always:
            if_any "fall"
            "multisleep_minamisam_cover"
        always:
            if_any "winter"
            "multisleep_minamisam_warmcover"

    layeredimage multisleep homeharem:
        attribute_function MultiPickers([SeasonPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, HaircutPicker], append_npc_from_attributes=True)
        attribute bree
        attribute lexi
        attribute minami
        attribute samantha
        attribute sasha

        attribute sleep null
        attribute underwear null
        attribute naked null

        attribute nomc null

        group seasons:
            attribute summer null
            attribute spring null
            attribute winter null
            attribute fall null

        always:
            "multisleep_homeharem_bg"

        always:
            if_any ["bree", "bree_pregnant"]
            if_not "nomc"
            "multisleep_homeharem_mike_arm"


        always:
            if_any ["lexi", "lexi_pregnant"]
            "multisleep_homeharem_lexi"
        attribute lexi_pregnant
        attribute lexi_casual null
        attribute lexi_collar null
        attribute lexi_nohaircut null


        always:
            if_any ["bree", "bree_pregnant"]
            "multisleep_homeharem_bree_shade"


        always:
            if_any ["bree", "bree_pregnant"]
            if_not "nomc"
            "multisleep_homeharem_mike_noarm"
        always:
            if_not ["bree", "bree_pregnant", "nomc"]
            "multisleep_homeharem_mike"
        always:
            if_not "nomc"
            "multisleep_homeharem_mike_boxer"


        always:
            if_any ["bree", "bree_pregnant"]
            "multisleep_homeharem_bree"
        attribute bree_pregnant


        always:
            if_any ["sasha", "sasha_pregnant"]
            "multisleep_homeharem_sasha"
        attribute sasha_pregnant
        attribute sasha_boobjob
        attribute sasha_haircut
        attribute sasha_nohaircut
        attribute sasha_casual null
        attribute sasha_collar null


        attribute samantha_nohaircut null
        always:
            if_any ["samantha", "samantha_pregnant"]
            "multisleep_homeharem_samantha"
        attribute samantha_pregnant
        attribute samantha_collar



        always:
            if_any ["minami", "minami_pregnant"]
            "multisleep_homeharem_minami"
        attribute minami_pregnant
        attribute minami_haircut
        attribute minami_nohaircut


        group multiple auto variant piercings
        group multiple:
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_nipples null
            attribute lexi_tongue null
            attribute samantha_tongue null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_tongue null
        group multiple auto variant piercings_boobjob when sasha_boobjob
        group multiple auto variant piercings_noboobjob when not sasha_boobjob


        group multiple auto variant outfit when not (summer or naked)
        group multiple auto variant outfit_bree_pregnant when bree_pregnant and not (summer or naked)
        group multiple auto variant outfit_sasha_pregnant when sasha_pregnant and not (summer or naked)
        group multiple auto variant outfit_sasha_boobjob when sasha_boobjob and not (summer or naked)


        group collars multiple

        always:
            if_any "fall"
            "multisleep_homeharem_cover"
        always:
            if_any "winter"
            "multisleep_homeharem_warmcover"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
