init 1:
    layeredimage criminal harem bj:
        attribute_function MultiPickers([CollarPicker, HaircutPicker], npcs=[camila, lexi])


        group bg auto:
            attribute alley default


        always "criminal_harem_bj_bodies"


        attribute naked null
        always "criminal_harem_bj_mikeoutfit" if_not ["naked"]


        group collars auto


        always "criminal_harem_bj_lexi_date" if_not ["naked"]
        always "criminal_harem_bj_camila_work" if_not ["naked"]


        always "criminal_harem_bj_dick_out" if_not ["camsuck", "lexsuck", "flacid"]
        group dick:
            attribute camsuck null
            attribute lexsuck null
        always "criminal_harem_bj_cum_out" if_any ["cum"] if_not ["camsuck", "lexsuck", "flacid"]


        attribute dickcum null
        always "criminal_harem_bj_dickcum_out" if_any ["dickcum"] if_not ["camsuck", "lexsuck", "flacid"]


        group camilatongue auto if_any ["camlick"]:
            attribute camdown default
        group camilahead auto:
            attribute camnormal default


        group lexitongue auto if_any ["lexlick"]:
            attribute lexdown default
        group lexihead auto:
            attribute lexnormal default


        attribute cum null
        always "criminal_harem_bj_cum_camsuck" if_all ["cum", "camsuck"]
        always "criminal_harem_bj_cum_lexsuck" if_all ["cum", "lexsuck"]
        attribute facecum


        always "criminal_harem_bj_camilahand"
        always "criminal_harem_bj_lexihold" if_not ["camsuck", "lexsuck", "flacid"]
        attribute handjob if_not ["camsuck", "lexsuck", "flacid"]
        group lexihand auto


        group dick:
            attribute flacid
        always "criminal_harem_bj_dickcum_flacid" if_all ["dickcum", "flacid"] if_not ["camsuck", "lexsuck"]
        always "criminal_harem_bj_cum_flacid" if_all ["cum", "flacid"] if_not ["camsuck", "lexsuck"]


        always "criminal_harem_bj_ambient"

    layeredimage criminal harem threesome camilafuck:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, MCCGPicker], npcs=[camila, lexi])

        always:
            "criminal_harem_threesome_camilafuck_bg"

        always:
            "criminal_harem_threesome_camilafuck_bodies"

        group exp auto:
            attribute camilaopen default

        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group vaginal_position:
            attribute up null default
            attribute down null

        group dick auto variant "up" if_all ["up", "vaginal"]
        group dick auto variant "down" if_all ["down", "vaginal"]

        group dick auto variant "out" if_any "out"
        group dick auto

        attribute condom null
        group condom auto variant "up" if_all ["up", "vaginal", "condom"]
        group condom auto variant "down" if_all ["down", "vaginal", "condom"]
        group condom auto variant "out" if_all ["out", "condom"]

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        group condomcum auto if_all ["cumshot", "condom"]

        group multiple auto variant spank

        group arm auto:
            attribute normal default
            attribute pull null
            attribute out null

        group fx auto

        attribute gape
        attribute gapecum

        attribute beads null
        group beads auto if_any "beads" if_not "anal":
            attribute pull default


        always:
            "criminal_harem_threesome_camilafuck_fg"

    layeredimage criminal harem threesome lexifuck:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, MCCGPicker], npcs=[camila, lexi])

        always:
            "criminal_harem_threesome_lexifuck_bg"

        always:
            "criminal_harem_threesome_lexifuck_bodies"

        group arm auto variant "down" if_all ["hj", "down"]
        group arm auto variant "up" if_all ["hj", "up"]

        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        group condomcum auto if_all ["cumshot", "condom"]

        group hj_position:
            attribute up default null
            attribute down null

        group thumb auto variant "down" if_all ["hj", "down"]
        group thumb auto variant "up" if_all ["hj", "up"]

        group arm auto if_not "hj":
            attribute cheeks default
            attribute hj

        group exp auto:
            attribute normal default

        group fx auto

    layeredimage criminal harem ending:
        attribute_function MultiPickers([EndingKidPicker], npcs=[camila, lexi])

        always:
            "criminal_harem_ending_bg"

        attribute lexi

        group multiple auto variant kids

        attribute camila

        always:
            "criminal_harem_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
