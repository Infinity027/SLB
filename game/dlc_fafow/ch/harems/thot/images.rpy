init 1:
    layeredimage thot 3some blowjob:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, MCCGPicker], npcs=[alexis, reona])

        attribute alexis null
        attribute reona null



        group bg auto:
            attribute bedroom default



        attribute mikemc


        group alexis_body auto:
            attribute alicknipple default

        attribute alexis_pregnant null
        group alexis_pregnant auto if_any "alexis_pregnant"

        group alexis_exp auto if_any "ablowjob":
            attribute normal default
        attribute alexis_nohaircut null


        group multiple auto variant piercings_alicknipple when alicknipple
        group multiple auto variant piercings_alickdick when alickdick
        group multiple auto variant piercings_ablowjob when ablowjob


        group reona_body auto:
            attribute rlicknipple default

        attribute reona_haircut null
        attribute reona_nohaircut null
        group reona_haircut auto if_any "reona_haircut"
        group reona_nohaircut auto if_any "reona_nohaircut"

        attribute reona_pregnant null
        group reona_pregnant auto if_any "reona_pregnant"



        attribute alexis_collar null
        group alexis_collar auto if_any "alexis_collar"

        attribute reona_collar null
        group reona_collar auto if_any "reona_collar"


        group multiple auto variant null_piercings
        group multiple:
            attribute alexis_clit null
            attribute alexis_ears null
            attribute alexis_lips null
            attribute reona_clit null
            attribute reona_tongue null


        group multiple auto variant piercings_rlicknipple when rlicknipple
        group multiple auto variant piercings_rlickdick when rlickdick
        group multiple auto variant piercings_rblowjob when rblowjob



        group alexis_hands auto

        group reona_hands auto


        group mikehand_alexis auto
        group mikehand_reona auto


        group mikehand_alexis_alickdick auto if_any "alickdick":
            attribute acaress default

        group mikehand_reona_rlickdick auto if_any "rlickdick":
            attribute rcaress default


        group mikehand_alexis_ablowjob auto if_any "ablowjob":
            attribute acaress default

        group mikehand_reona_rblowjob auto if_any "rblowjob":
            attribute rcaress default



        group dick auto if_not ["ablowjob", "rblowjob"]:
            attribute mc_medium default


        always if_any ["alickdick", "rlickdick"]:
            "thot_3some_blowjob_mike_balls"

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        attribute dickcum null
        group dickcum auto if_any "dickcum"
        attribute cum null
        group cum auto variant "ablowjob" if_all ["ablowjob", "cum"]
        group cum auto variant "rblowjob" if_all ["rblowjob", "cum"]
        group cum auto variant "alexis_alickdick" if_all ["alickdick", "cum"] if_not ["ablowjob", "rblowjob"]
        group cum auto variant "reona_rlickdick" if_all ["rlickdick", "cum"] if_not ["ablowjob", "rblowjob"]


        group fg auto

    layeredimage thot 3some handjob:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, MCCGPicker], npcs=[alexis, reona])

        attribute mikemc null
        attribute alexis null
        attribute reona null

        group mc_outfits auto:
            attribute mc_casual null
            attribute mc_date null

        group bg auto:
            attribute bedroom default

        always:
            "thot_3some_handjob_bodies"

        always:
            "thot_3some_handjob_mc_hands"

        group mcexp auto:
            attribute mcnormal default

        group multiple auto variant pregnancies

        group multiple auto variant piercings
        group multiple:
            attribute alexis_clit null
            attribute alexis_ears null
            attribute alexis_lips null
            attribute reona_clit null
            attribute reona_tongue null

        group multiple auto variant collars

        attribute cumshot
        group cumshot auto if_all ["cumshot"]

        group dick auto

        group alexisexp auto:
            attribute alexisnormal default

        group reonaexp auto:
            attribute reonanormal default

        group reonahand auto:
            attribute reonasqueeze default

        group alexishand auto:
            attribute alexisup default

        group multiple auto variant haircuts

        group fg auto

        group multiple auto variant fx

    layeredimage thot 3some fuckalexis:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, MCCGPicker], npcs=[alexis, reona])

        attribute mikemc null
        attribute alexis null
        attribute reona null

        group mc_outfits auto:
            attribute mc_casual null
            attribute mc_date null

        group bg auto:
            attribute bedroom default

        always:
            "thot_3some_fuckalexis_bodies"

        group multiple auto variant pregnancies

        group multiple auto variant piercings
        group multiple:
            attribute alexis_clit null
            attribute alexis_ears null
            attribute alexis_lips null
            attribute alexis_navel null
            attribute reona_clit null
            attribute reona_navel null
            attribute reona_tongue null


        group dick_positions auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto if_not "out"

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto if_any "condom" if_not "out"

        attribute cumshot null
        group cumshot auto variant "out" if_all ["out", "cumshot"]

        attribute creampie null
        group creampie auto if_not ["out"] if_any "creampie"

        group alexiseyes auto:
            attribute alexisopened default

        group haircuts auto

        attribute alexis_nohaircut null
    layeredimage thot 3some fuckreona:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, PubesPicker, MCCGPicker], npcs=[alexis, reona])

        attribute mikemc null
        attribute alexis null
        attribute reona null

        group mc_outfits auto:
            attribute mc_casual null
            attribute mc_date null

        group bg auto:
            attribute bedroom default

        always:
            "thot_3some_fuckreona_bodies"

        attribute alexis_pubes
        group multiple auto variant pregnancies

        group multiple auto variant piercings
        group multiple:
            attribute alexis_ears null
            attribute alexis_lips null
            attribute reona_clit null
            attribute reona_navel null
            attribute reona_pregnant_navel null
            attribute reona_tongue null


        group dick_positions auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto if_not "out"

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto if_any "condom" if_not "out"

        attribute cumshot null
        group cumshot auto variant "out" if_all ["out", "cumshot"]

        attribute creampie null
        group creampie auto if_not ["out"] if_any "creampie"

        group alexiseyes auto:
            attribute alexisopened default

        group alexismouth auto:
            attribute alexisnormal default

        group reonaeyes auto:
            attribute reonaopened default

        group reonamouth auto:
            attribute reonanormal default

        group haircuts auto

        attribute alexis_nohaircut null

        attribute squirt

    layeredimage thot 4some bj:
        attribute_function MultiPickers([PiercingsPicker], npcs=[alexis, audrey, reona])


        group bg auto:
            attribute bedroom default


        attribute alexis null
        attribute audrey null
        attribute reona null
        always "thot_4some_bj_bodies"


        attribute alexis_clit null
        attribute alexis_ears null
        attribute alexis_lips null
        attribute alexis_navel null
        attribute audrey_clit null
        attribute audrey_ears null
        attribute audrey_navel null
        attribute audrey_nipples null
        attribute audrey_tongue null
        attribute reona_clit null
        attribute reona_ears null
        attribute reona_navel null
        attribute reona_tongue null
        group multiple auto variant piercings


        group hairs auto


        always "thot_4some_bj_reona_mouth" if_not ["reona_suck"]
        always "thot_4some_bj_alexis_mouth" if_not ["alexis_suck"]
        always "thot_4some_bj_audrey_mouth" if_not ["audrey_suck"]


        attribute mouthcum_reona if_not ["reona_suck"]
        attribute mouthcum_alexis if_not ["alexis_suck"]
        attribute mouthcum_audrey if_not ["audrey_suck"]


        attribute facecum_reona
        attribute facecum_alexis
        attribute facecum_audrey


        group dick:
            attribute out default


        attribute cum null
        group cum if_any ["cum"]:
            attribute out default


        attribute mikehand null
        group mikehand auto if_any ["mikehand"]:
            attribute back default


        group dick:
            attribute reona_suck
            attribute alexis_suck
            attribute audrey_suck


        group cum if_any ["cum"]:
            attribute reona_suck
            attribute alexis_suck
            attribute audrey_suck

    layeredimage thot 4some foreplay:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        always "thot_4some_foreplay_mikeleg"
        always "thot_4some_foreplay_mike"


        attribute audrey
        attribute bodycum if_any ["audrey"]
        group multiple auto variant audrey_piercings when audrey
        attribute audrey_collar if_any ["audrey"]
        attribute audrey_pregnant if_any ["audrey"]
        group audrey_exp auto if_any ["audrey"]:
            attribute audrey_normal default
        always "thot_4some_foreplay_audreyhair" if_any ["audrey"]
        attribute facecum if_any ["audrey"]


        always "thot_4some_foreplay_mikedick"


        group audreyhand auto if_any ["audrey"]:
            attribute audreyhand_down default


        attribute alexis
        attribute alexishand if_any ["alexis"]
        group multiple auto variant alexis_piercings when alexis
        attribute alexis_collar if_any ["alexis"]
        group alexis_exp auto if_any ["alexis"]:
            attribute alexis_normal default
        always "thot_4some_foreplay_alexishair" if_any ["alexis"]


        attribute reona
        attribute reona_pregnant if_any ["reona"]
        attribute reona_collar if_any ["reona"]
        group multiple auto variant reona_piercings when reona
        group reona_exp auto if_any ["reona"]:
            attribute reona_aroused default
        attribute reona_haircut if_any ["reona"]
        attribute reona_nohaircut if_any ["reona"]
        attribute reonahand if_any ["reona"]


        always "thot_4some_foreplay_mikehead"


        attribute handcum if_any ["audrey"]


        attribute cum

    layeredimage thot 4some fuckalexis:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, DickPicker], npcs=[alexis, reona], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        always "thot_4some_fuckalexis_bodies"
        attribute alexis_pubes
        attribute alexis_pregnant
        attribute bodycum
        group multiple auto variant piercings
        attribute alexis_collar
        attribute reona_collar
        attribute reona_pregnant
        group eyes auto:
            attribute open default
        always "thot_4some_fuckalexis_alexishead"
        attribute reona_haircut
        attribute reona_nohaircut


        group dick auto:
            attribute out null default
        group dick auto variant "out" if_any ["out"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["out", "condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom"]


        attribute audrey_breath if_any ["audrey"]
        attribute audrey
        attribute audrey_pregnant if_any ["audrey"]
        group multiple auto variant audrey_piercings when audrey
        attribute audrey_collar if_any ["audrey"]
        always "thot_4some_fuckalexis_audreyhead" if_any ["audrey"]

        attribute shade

    layeredimage thot 4some fuckaudrey:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, DickPicker], npcs=[audrey], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        always "thot_4some_fuckaudrey_mike"


        attribute reona
        attribute reona_pregnant if_any ["reona"]
        group multiple auto variant reona_piercings when reona
        attribute reona_collar if_any ["reona"]
        group reona_eyes auto if_any ["reona"]:
            attribute reona_eyes_open default
        attribute reona_haircut if_any ["reona"]
        attribute reona_nohaircut if_any ["reona"]


        attribute alexis
        attribute alexis_pregnant if_any ["alexis"]
        group multiple auto variant alexis_piercings when alexis
        attribute alexis_collar if_any ["alexis"]
        group alexis_eyes auto if_any ["alexis"]:
            attribute alexis_eyes_open default


        attribute audrey


        attribute bodycum


        group audreyhead auto:
            attribute lookback default
        group audrey_exp auto if_any ["lookback"]:
            attribute normal default


        group multiple auto variant audrey_piercings_lookback when lookback
        group multiple:
            attribute audrey_clit null
            attribute audrey_ears null
            attribute audrey_navel null
            attribute audrey_pregnant_navel null
            attribute audrey_nipples null
            attribute audrey_tongue null
        attribute audrey_collar if_any ["lookback"]


        attribute speed


        group dick auto:
            attribute out null default
        group dick auto variant "out" if_any ["out"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["out", "condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["out", "cum"] if_not ["condom"]


        group lefthand auto:
            attribute lefthand_hold
            attribute lefthand_finger if_any ["alexis"]
        group righthand auto:
            attribute righthand_hold
            attribute righthand_finger if_any ["reona"]

    layeredimage thot 4some fuckreona:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, DickPicker], npcs=[reona], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        attribute mike


        always "thot_4some_fuckreona_reona"


        group multiple auto variant reona_piercings_low
        attribute reona_pregnant
        group multiple auto variant reona_piercings
        attribute reona_pubes
        attribute reona_collar


        attribute bodycum


        attribute speed


        group reona_mouth auto:
            attribute reona_mouth_lick default
        attribute reona_tongueout if_any ["reona_mouth_open"]
        group reona_eyes auto:
            attribute reona_eyes_open default


        attribute reona_haircut
        attribute reona_nohaircut


        group dick auto if_any ["mike"]:
            attribute out null default
        group dick auto variant "out" if_all ["mike", "out"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "out", "condom"]


        attribute cum null
        group cum auto if_all ["mike", "cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["mike", "out", "cum"] if_not ["condom"]


        attribute audrey
        attribute audrey_pubes if_any ["audrey"]
        attribute audrey_pregnant if_any ["audrey"]
        group multiple auto variant audrey_piercings when audrey
        group audrey_mouth auto if_any ["audrey"]:
            attribute audrey_mouth_normal default


        attribute alexis
        attribute alexis_pregnant if_any ["alexis"]
        attribute alexis_pubes if_any ["alexis"]
        attribute alexis_collar if_any ["alexis"]
        group multiple auto variant alexis_piercings when alexis
        group alexis_mouth auto if_any ["alexis"]:
            attribute alexis_mouth_normal default
        always "thot_4some_fuckreona_alexishair" if_any ["alexis"]


        always "thot_4some_fuckreona_lefthand_lefthand_hold" if_any ["mike"] if_not ["audrey"]
        always "thot_4some_fuckreona_righthand_righthand_hold" if_any ["mike"] if_not ["alexis"]
        group lefthand auto if_all ["mike", "audrey"]:
            attribute lefthand_hold default
        group righthand auto if_all ["mike", "alexis"]:
            attribute righthand_hold default


        attribute squirt_audrey if_any ["audrey"]
        attribute squirt_alexis if_any ["alexis"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
