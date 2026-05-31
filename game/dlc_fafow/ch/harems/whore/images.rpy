init 1:
    layeredimage whore reverse cowgirl:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, DickPicker, PubesPicker], npcs=[lexi, reona])


        group bg auto:
            attribute beach default


        attribute reona null
        group bodies_reona auto:
            attribute raising null default
            attribute lying null

        group bodies_reona auto variant "raising" if_any "raising"
        group bodies_reona auto variant "lying" if_any "lying"

        group bodies auto

        attribute lexi_nohaircut null
        attribute lexi_haircut null
        attribute lexi_pubes null

        group lexi_eyes auto:
            attribute looking_mike default


        group butt auto:
            attribute up default


        attribute lexi_tongue


        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute reona_clit null
            attribute reona_navel null
            attribute reona_pregnant_navel null
            attribute reona_nipples null
            attribute reona_tongue null


        group collar auto
        group collar auto variant "haircut" if_any "reona_haircut" if_not "lying"
        group collar auto variant "nohaircut" if_any "reona_nohaircut" if_not "lying"

        attribute reona_pureglasses if_not "lying"


        group dick auto if_not ["anal", "vaginal"]

        attribute anal null
        group anal auto if_any "anal":
            attribute up default

        attribute vaginal null
        group vaginal auto if_any "vaginal":
            attribute up default



        attribute cum null
        group cum auto if_any "cum"

        attribute cumshot null
        group cumshot auto if_any "cumshot":
            attribute medium default


        attribute condom null
        group condom auto if_any "condom":
            attribute medium default


        attribute lexi_pregnant


        attribute fx_shadow

    layeredimage whore lexiblowjob:

        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PiercingsPicker, DickPicker], npcs=[lexi, reona])


        group bg auto:
            attribute beach default


        always "whore_lexiblowjob_bodies"


        group multiple auto variant piercings


        attribute lexi_collar


        group lexi_eyes auto:
            attribute opened default
        always "whore_lexiblowjob_reona_eyes"


        group reona_tongue auto:
            attribute up default


        attribute lick
        attribute blowjob


        group dick auto if_not ["blowjob"]:
            attribute medium default


        attribute cum
        attribute cumshot null
        group cumshot auto if_any "cumshot"


        always "whore_lexiblowjob_thumb"


        group multiple auto variant fx


    layeredimage whore reonablowjob:

        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PiercingsPicker, MCCGPicker], npcs=[lexi, reona])

        attribute mikemc null
        attribute lexi null
        attribute reona null


        group bg auto:
            attribute beach default


        always "whore_reonablowjob_bodies"


        group lexi_eyes auto:
            attribute open default
        group lexi_mouth auto:
            attribute happy default


        attribute hand


        group head auto:
            attribute lick default


        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_tongue null
            attribute reona_clit null
            attribute reona_ears null
            attribute reona_navel null
            attribute reona_pregnant_navel null
            attribute reona_nipples null
            attribute reona_tongue null


        attribute reona_collar if_any ["blowjob"]
        attribute lexi_collar null


        group blowjob_eyes auto if_any ["blowjob"]:
            attribute opened default


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]


        group dick_lick auto if_any ["lick"]
        group dick auto if_any ["blowjob"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute handjob


        group fg auto

    layeredimage whore handjob:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, PubesPicker, OutfitPicker, MCCGPicker], npcs=[lexi, reona], add_simple_outfit_attribute=True, add_simple_naked_attribute=True)

        attribute lexi null
        attribute reona null
        attribute nomc null

        group bg auto:
            attribute beach default

        always:
            if_not "nomc"
            "whore_handjob_mikemc"

        always:
            if_not "nomc"
            "whore_handjob_mc_pubes"

        group hands_back auto:
            attribute still default

        always:
            "whore_handjob_bodies"

        group multiple auto variant pubes

        group multiple auto variant piercings_hidden when naked

        group multiple auto variant piercings
        group multiple:
            attribute lexi_ears null
            attribute lexi_tongue null
            attribute reona_ears null
            attribute reona_tongue null

        group multiple auto variant pregnancies

        group multiple auto variant piercings_front

        group multiple auto variant collars

        attribute naked null

        group bot auto variant "reona_nopregnant" if_not ["reona_pregnant", "naked"]
        group bot auto variant "reona_pregnant" if_any "reona_pregnant" if_not "naked"
        group bot auto variant "lexi_nopregnant" if_not ["lexi_pregnant", "naked"]
        group bot auto variant "lexi_pregnant" if_any "lexi_pregnant" if_not "naked"
        group multiple auto variant top when not naked:
            attribute swimsuit null default

        always:
            if_not "nomc"
            "whore_handjob_mc_hands"

        group dick auto if_not ["nomc"]:
            attribute hj default
            attribute limp

        group hands_front auto:
            attribute sign default

        group fx auto

        group cum auto

        group exp auto:
            attribute up default

        group fg auto

    layeredimage whore doggy:

        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PiercingsPicker, MCCGPicker], npcs=[lexi, reona])

        attribute nomc null
        attribute mikemc null
        attribute lexi null
        attribute reona null

        group bg auto:
            attribute beach default

        always:
            "whore_doggy_bodies"

        attribute reona_pregnant

        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_tongue null
            attribute reona_clit null
            attribute reona_tongue null

        group multiple auto variant collars

        group lexi_eyes auto:
            attribute opened default

        always:
            if_not ["nomc", "vaginal", "anal"]
            "whore_doggy_mc_position_far"

        always:
            if_not ["nomc", "out"]
            "whore_doggy_mc_position_near"

        group dick_positions auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto if_not ["nomc", "out"]
        group dick auto variant "out" if_any "out" if_not "nomc"

        attribute condom null
        group condom auto if_not ["nomc", "out"] if_any "condom"
        group condom auto variant "out" if_all ["out", "condom"] if_not "nomc"

        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["nomc", "condom"]

        attribute creampie null
        group creampie auto if_all ["creampie"] if_not ["nomc", "out", "condom"]

        attribute cum null
        group cum auto if_any "cum"

        group hand_positions auto:
            attribute onlexi null default
            attribute up null
            attribute down null

        group hand auto
        group hand auto variant "up" if_all ["up", "out"]
        group hand auto variant "down" if_all ["down", "out"]


        group fg auto

    layeredimage whore blowjob:
        attribute_function MultiPickers([PiercingsPicker, MCCGPicker], npcs=[lexi, reona])

        attribute mikemc null
        attribute lexi null
        attribute reona null
        attribute lexi_pregnant null
        attribute reona_pregnant null

        group bg auto:
            attribute beach default

        always "whore_blowjob_bodies"

        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_nose null
            attribute lexi_tongue null
            attribute reona_clit null
            attribute reona_ears null
            attribute reona_navel null
            attribute reona_pregnant_navel null
            attribute reona_tongue null

        group reonahead auto:
            attribute reonaup default

        group reonaeyes auto variant "reonaup" if_any "reonaup"
        group reonaeyes auto variant "reonablow" if_any "reonablow":
            attribute reonanormal default
        group reonamouth auto variant "reonaup" if_any "reonaup":
            attribute reonasmile default

        group lexihead auto:
            attribute lexiup default
        group lexieyes auto variant "lexiup" if_any "lexiup"
        group lexieyes auto variant "lexiblow" if_any "lexiblow":
            attribute lexinormal default
        group leximouth auto variant "lexiup" if_any "lexiup":
            attribute lexismile default

        group dick_positions auto:
            attribute out default null
            attribute lexiblow null
            attribute reonablow null

        group dick auto variant "out" if_any "out"

        group piercings_reonaup auto if_any "reonaup"

        group lexihand auto
        group reonahand auto

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        group cum auto

        group cum auto variant "lexiblow" if_all ["lexiblow"]
        group cum auto variant "lexiup" if_all ["lexiup"]

        group cum auto variant "reonablow" if_all ["reonablow"]
        group cum auto variant "reonaup" if_all ["reonaup"]

        attribute dickcum null
        group dickcum auto if_any "dickcum"

    layeredimage whore ending:
        attribute_function MultiPickers([EndingKidPicker], npcs=[lexi, reona])

        attribute lexi null
        attribute reona null
        attribute reona_haircut null
        attribute reona_nohaircut null

        always "whore_ending_bg"
        group multiple auto variant kids
        always "whore_ending_bodies"
        always "whore_ending_fg"
        attribute laugh
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
