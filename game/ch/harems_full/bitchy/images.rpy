init 1:
    layeredimage bitchy threesome pallafuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[audrey, palla])
        attribute cum null
        always "bitchy_threesome_pallafuck_bg"
        always "bitchy_threesome_pallafuck_girls"

        group audrey_exp auto:
            attribute audreyopen default

        group palla_exp auto:
            attribute pallaopen default

        group multiple auto variant pregnancy

        group multiple auto variant collars

        group multiple auto variant piercings

        attribute strapon

        group multiple auto variant acc

        always:
            "bitchy_threesome_pallafuck_audrey_arm"

        attribute mike

        group dick auto if_any "mike":
            attribute anal null
            attribute vaginal null

        group cum auto if_any "cum"
        group multiple auto variant fx

    layeredimage bitchy foursome audreyfuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[audrey], append_npc_from_attributes=True)

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        always:
            "bitchy_foursome_audreyfuck_bg"


        attribute audrey


        group exp auto:
            attribute normal default


        group exp_mike auto:
            attribute opened default


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute audrey_pubes


        attribute audrey_pregnant


        group multiple auto variant piercings_aud


        attribute audrey_collar


        attribute bodycum


        group dick auto variant "out" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["out", "dickcum"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]


        group condom auto variant "out" if_any ["condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]


        attribute cassidy
        group multiple auto variant piercings_cass when cass
        attribute cassidy_collar if_any ["cassidy"]
        attribute cassidy_pregnant if_any ["cassidy"]
        always:
            if_all ["cassidy", "out", "dickcum"] if_not ["condom"]
            "bitchy_foursome_audreyfuck_cassidyhand_dickcum"


        attribute palla
        attribute palla_pregnant if_any ["palla"]
        group pallabody auto if_any ["palla"]
        attribute palla_collar if_any ["palla"]
        group multiple auto variant piercings_pal when pal


        always:
            "bitchy_foursome_audreyfuck_light"

    layeredimage bitchy foursome cassidyfuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[cassidy], append_npc_from_attributes=True)

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        always:
            "bitchy_foursome_cassidyfuck_bg"


        attribute cassidy


        attribute cassidy_pubes


        attribute cassidy_pregnant


        group multiple auto variant piercings_cass


        group dick auto
        group dick auto variant "out" if_any ["out"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]


        attribute cassidy_collar


        group eyes auto:
            attribute opened default
        group mouth auto if_not ["lick"]:
            attribute normal default


        attribute vaginaldrip


        attribute palla
        attribute palla_pubes if_any ["palla"]
        attribute palla_pregnant if_any ["palla"]
        group multiple auto variant piercings_pal when pal
        attribute lick if_any ["palla"]
        attribute pallasquirt if_any ["palla"]
        attribute palla_collar if_any ["palla"]


        attribute audrey
        attribute audrey_pubes if_any ["audrey"]
        attribute audrey_pregnant if_any ["audrey"]
        attribute audreysquirt if_any ["audrey"]
        attribute audrey_collar if_any ["audrey"]
        group multiple auto variant piercings_aud when aud


        always:
            "bitchy_foursome_cassidyfuck_light"

    layeredimage bitchy foursome pallafuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[palla], append_npc_from_attributes=True)

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        always:
            "bitchy_foursome_pallafuck_bg"


        attribute palla
        always:
            "bitchy_foursome_pallafuck_palla"


        attribute palla_collar


        attribute palla_pubes


        group exp auto:
            attribute normal default


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute hand null
        group hand auto if_all ["cassidy", "hand"]


        attribute creampie null
        group creampie auto if_any ["creampie"]


        group multiple auto variant piercings_pal


        group dick auto variant "out" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["out", "dickcum"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]


        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]


        attribute audrey
        attribute audrey_pregnant if_any ["audrey"]
        group multiple auto variant piercings_aud when aud
        attribute audrey_collar if_any ["audrey"]
        attribute audrey_pubes if_any ["audrey"]


        attribute palla_pregnant
        group multiple auto variant piercings_palpreg


        attribute cassidy
        group multiple auto variant piercings_cass when cass
        attribute cassidydrip if_any ["cassidy"]
        attribute cassidy_pregnant if_any ["cassidy"]
        attribute cassidy_pubes if_any ["cassidy"]

    layeredimage bitchy foursome cumshare:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker], append_npc_from_attributes=True)


        group bg auto:
            attribute mansion default


        always:
            "bitchy_foursome_cumshare_mike"


        attribute palla


        always:
            if_all ["palla"]
            "bitchy_foursome_cumshare_palla_leftarm"
        always:
            if_all ["palla"]
            "bitchy_foursome_cumshare_palla_rightarm"


        group eyes_pal auto if_all ["palla"]:
            attribute pallaopened default


        group mouth_pal auto if_all ["palla"] if_not ["pallasuck"]:
            attribute pallamouth default
        attribute pallasuck if_all ["palla"]


        attribute pallamouthcum if_all ["palla", "pallamouth"] if_not ["pallasuck"]


        group multiple auto variant piercings_pal when palla


        attribute cassidy
        attribute audrey


        group eyes_cass auto if_all ["cassidy"]:
            attribute cassidyopened default
        group eyes_aud auto if_all ["audrey"]:
            attribute audreyopened default


        group mouth_cass auto if_all ["cassidy"] if_not ["cassidysuck"]:
            attribute cassidymouth default
        attribute cassidysuck if_all ["cassidy"]
        group mouth_aud auto if_all ["audrey"] if_not ["audreysuck"]:
            attribute audreymouth default
        attribute audreysuck if_all ["audrey"]


        attribute cassidymouthcum if_all ["cassidy", "cassidymouth"] if_not ["cassidysuck"]
        attribute audreymouthcum if_all ["audrey", "audreymouth"] if_not ["audreysuck"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["out"]:
            attribute pallasuck if_all ["palla"]
            attribute cassidysuck if_all ["cassidy"]


        attribute cassidy_collar if_all ["cassidy"]
        attribute audrey_collar if_all ["audrey"]


        group multiple auto variant piercings_cass when cassidy
        group multiple auto variant piercings_aud when audrey


        attribute cassidy_pregnant if_all ["cassidy"]
        attribute audrey_pregnant if_all ["audrey"]


        group fg auto

        group dickpos:
            attribute limp null
            attribute out null default
            attribute pallasuck null
            attribute cassidysuck null
            attribute audreysuck null


        group dick auto
        group dick auto variant "out" if_all ["out"]


        attribute dickcum null
        group dickcum auto variant "out" if_all ["dickcum", "out"]


        group cumshot auto variant "out" if_all ["cumshot", "out"]


        attribute share if_all ["palla", "pallamouthcum", "cassidy", "cassidymouthcum", "audrey", "audreymouthcum"]


        always:
            "bitchy_foursome_cumshare_mikehand"

    layeredimage bitchy blowjob:
        attribute_function MultiPickers([DickPicker, OutfitPicker], npcs=[audrey, cassidy, palla])

        group bg auto:
            attribute office default

        always:
            "bitchy_blowjob_mike"


        group bodiesblow auto


        group bodiessuck auto

        attribute naked null
        group outfits auto variant "audreyblow" if_any "audreyblow"
        group outfits auto variant "audreysuck" if_any "audreysuck"
        group outfits auto variant "cassidyblow" if_any "cassidyblow"
        group outfits auto variant "cassidysuck" if_any "cassidysuck"
        group outfits auto variant "pallablow" if_any "pallablow"
        group outfits auto variant "pallasuck" if_any "pallasuck"

        group multiple auto variant heads
        group heads auto variant "tip" if_not "deep"
        group heads auto variant "deep" if_any "deep"

        group expblow:
            attribute normal default null

        group expsuck:
            attribute open default null

        group expblow auto variant "audreyblow" if_any "audreyblow" if_not "deep"
        group expsuck auto variant "audreysuck" if_any "audreysuck"
        group expblow auto variant "cassidyblow" if_any "cassidyblow" if_not "deep"
        group expsuck auto variant "cassidysuck" if_any "cassidysuck"
        group expblow auto variant "pallablow" if_any "pallablow" if_not "deep"
        group expsuck auto variant "pallasuck" if_any "pallasuck"

        always:
            "bitchy_blowjob_balls_right"
        group balls_left auto:
            attribute still default

        attribute blow null
        group dick auto if_not "blow":
            attribute out default

        group dickblow auto if_all "blow" if_any ["audreyblow", "cassidyblow", "pallablow"]:
            attribute out default

        attribute cumshot null
        group cumshot auto if_any "cumshot":
            attribute straight default

        attribute cum null
        group cum auto if_any "cum"

        group multiple auto variant cum_deep when cum and deep

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        group fg auto

        attribute cassidy_gold null

    layeredimage bitchy harem ending:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, EndingKidPicker], npcs=[audrey, palla], append_npc_from_attributes=True)

        always:
            "bitchy_harem_ending_bg"

        attribute cassidy
        attribute audrey
        attribute palla
        group multiple auto variant collars
        group multiple auto variant piercings

        group multiple auto variant kids

        attribute cassidy_kid null
        always "bitchy_harem_ending_mike_kid" when cassidy and cassidy_kid
        always "bitchy_harem_ending_mike_nokid" when (cassidy and not cassidy_kid) or not cassidy

        always:
            "bitchy_harem_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
