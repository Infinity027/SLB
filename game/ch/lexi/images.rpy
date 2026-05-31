init 1:
    layeredimage lexi:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=lexi)


        attribute idle null


        attribute nophone null
        always "lexi_phone_a" if_any ["a"] if_not ["nophone"]


        group position auto


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush null
        group blush auto if_any "blush"


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_b_topless when b and (topless or naked)
        group multiple auto variant piercings_c when c
        group multiple auto variant piercings_c_topless when c and (topless or naked)


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]
        group top auto variant "c_pregnant" if_all ["c","pregnant"] if_not ["topless","naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless","naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "c_pregnant" if_all ["c","pregnant"] if_not ["bottomless","naked"]


        always "lexi_phone_b" if_any ["b"] if_not ["nophone"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute lolly null
        group lolly auto if_any ["lolly"] if_not ["lollipop"]:
            attribute inside default


        attribute collar null
        group collar auto if_any ["collar"]


        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "c" if_any ["c"]


        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "c" if_any ["c"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage lexi close:
        yalign 0.2
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=lexi)


        attribute idle null


        attribute nophone null
        always "lexi_close_phone_a" if_any ["a"] if_not ["nophone"]


        group position auto


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush null
        group blush auto if_any "blush"


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]
        group top auto variant "c_pregnant" if_all ["c","pregnant"] if_not ["topless","naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless","naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "c_pregnant" if_all ["c","pregnant"] if_not ["bottomless","naked"]


        always "lexi_close_phone_b" if_any ["b"] if_not ["nophone"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute lolly null
        group lolly auto if_any ["lolly"] if_not ["lollipop"]:
            attribute inside default


        attribute collar null
        group collar auto if_any ["collar"]


        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "c" if_any ["c"]


        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "c" if_any ["c"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage lexi smartphone:
        always "lexi_smartphone"

    layeredimage lexi bj:
        attribute_function Pickers([OutfitPicker, PiercingsPicker], npc=lexi)


        group bg auto:
            attribute nightclub default
            attribute nobg null


        always "lexi_bj_butt"


        attribute naked null
        group outfit auto variant "butt" if_not ["naked"]


        always "lexi_bj_body"


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute nose null
            attribute tongue null


        group outfit auto if_not ["naked"]


        always "lexi_bj_hair"


        group head auto:
            attribute normal default


        group exp auto variant "normal" if_any ["normal"]:
            attribute smile default
        group exp auto variant "suck" if_any ["suck", "msuck"]:
            attribute open default
        group exp auto variant "deepthroat" if_any ["deepthroat"]:
            attribute open default


        attribute facial null
        group facial auto if_any ["facial"]:
            attribute nofacial null


        group man auto:
            attribute pants default


        group dick auto if_not ["suck","slap", "nodick", "master"]:
            attribute dick default
            attribute nodick null


        group mdick auto if_any ["master"] if_not ["msuck","slap", "nodick"]:
            attribute dick default
            attribute nodick null


        always "lexi_bj_mpubes" if_any ["master"] if_not ["nodick"]


        attribute slap if_any ["normal"] if_not ["master"]


        attribute cum null
        group cum auto if_any ["cum"]:
            attribute nocum null


        group multiple auto variant pull when not deepthroat
        group multiple auto variant pull_deepthroat when deepthroat

    layeredimage lexi kiss:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, CollarPicker, PregnancyPicker, MCCGPicker], npc=lexi)

        group multiple:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null


        group bodies auto if_not ["bowsette"]
        attribute bowsette "lexi_kiss_bodies_breemc_bowsette"

        attribute mc_pubes null

        group haircuts auto variant "breemc" if_any ["breemc"] if_not ["bowsette"]:
            attribute mc_nohaircut null


        group collars auto variant "mikemc" if_any ["mikemc"]


        attribute pregnant if_any ["mikemc"]


        group multiple auto variant piercings_mikemc when mikemc
        group multiple auto variant piercings_breemc when breemc
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null


        attribute naked null
        attribute topless null
        group outfits auto variant "mikemc" if_any ["mikemc"] if_not ["naked", "topless"]
        group outfits auto variant "breemc" if_any ["breemc"] if_not ["naked", "topless"]:
            attribute chinese "lexi_kiss_outfits_breemc_casual"
            attribute bowsette "lexi_kiss_outfits_breemc_halloween"
            attribute invisible "lexi_kiss_outfits_breemc_halloween"


        group collars auto variant "breemc" if_any ["breemc"]

        attribute mc_naked null

        group multiple auto variant mcpiercings_mikemc when mikemc
        group mcoutfits auto variant "mikemc" if_any ["mikemc"] if_not ["naked", "mc_naked"]


        group multiple auto variant mcpiercings_breemc when breemc
        group multiple:
            attribute mc_ears null
        group mcoutfits auto variant "breemc" if_any ["breemc"] if_not ["naked", "mc_naked"]
        group mccollar auto variant "breemc" if_any ["breemc"] if_not ["naked", "mc_naked"]


        group pregnancy auto if_any ["pregnant", "mikemc"]


        group acc auto variant "breemc" if_any ["breemc"]


        attribute cum null
        group cum auto if_all ["cum", "mikemc"]:
            attribute face
            attribute share

    layeredimage lexi stand:
        attribute_function Pickers([PregnancyPicker, XrayPicker, PiercingsPicker, PubesPicker, CollarPicker, DickPicker], npc=lexi)


        group bg auto:
            attribute bedroom default


        always "lexi_stand_bodies"
        attribute pregnant


        group exp auto:
            attribute normal default


        attribute pubes


        attribute anal null
        attribute vaginal null
        attribute condom null
        attribute xray null
        group xray_dick_vaginal auto if_all ["xray", "vaginal"]
        group xray_dick_anal auto if_all ["xray", "anal"]
        group xray_condom_vaginal auto if_all ["xray", "vaginal", "condom"]
        group xray_cum_vaginal auto if_all ["xray", "vaginal", "cum"] if_not ["condom"]
        group xray_cum_anal auto if_all ["xray", "anal", "cum"]


        attribute cum null
        group cum_anal auto if_all ["cum", "anal"]
        group cum_vaginal auto if_all ["cum", "vaginal"]

        group multiple auto variant piercings

        group hand auto:
            attribute pull default

        attribute collar

        always "lexi_stand_water" if_any ["pool"]

    layeredimage lexi stand2:
        attribute_function Pickers([XrayPicker, PiercingsPicker, CollarPicker, DickPicker], npc=lexi)

        group bg auto:
            attribute bedroom default

        always "lexi_stand2_body"

        group exp auto:
            attribute normal default

        group multiple auto variant piercings

        attribute collar

        group outfit auto:
            attribute naked null default

        attribute manoutfit

        attribute anal null
        attribute vaginal null
        attribute condom null
        attribute cum null
        attribute xray null
        group xray_dick_vaginal auto if_all ["xray", "vaginal"]
        group xray_dick_anal auto if_all ["xray", "anal"]
        group xray_condom_vaginal auto if_all ["xray", "vaginal", "condom"]
        group xray_cum_vaginal auto if_all ["xray", "vaginal", "cum"]
        group xray_cum_anal auto if_all ["xray", "anal", "cum"]

    layeredimage lexi pimping:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker], npc=lexi)

        always "lexi_pimping_bg"

        group pos auto

        attribute pregnant null
        group pregnant auto if_any ["pregnant"]

        attribute tongue if_any ["fuck"]
        attribute nose if_any ["fuck"]
        attribute nipples if_any ["fuck"]:
            "lexi_pimping_nipples_fuck"
        attribute nipples if_all ["blowjob","naked"]:
            "lexi_pimping_nipples_blowjob"

        group outfit auto if_any ["blowjob"]:
            attribute naked null default

        always "lexi_pimping_glass"

    layeredimage lexi missionary:
        attribute_function Pickers([PregnancyPicker, PubesPicker, DickPicker, PiercingsPicker, OutfitPicker], npc=lexi)

        group bg auto:
            attribute bedroom default

        group mike auto:
            attribute outside default

        always "lexi_missionary_bodies"

        attribute pregnant

        attribute pubes

        attribute blush

        group exp auto:
            attribute normal default

        attribute vaginalhit

        attribute ears null
        attribute tongue null
        group multiple auto variant piercings
        always "lexi_missionary_tits_speed" if_any ["speed"]
        group multiple auto variant piercings_speed when speed

        attribute naked null
        attribute topless null
        attribute bottomless null
        group top auto if_not ["topless", "naked", "speed"]
        group top auto variant "speed" if_any ["speed"] if_not ["topless", "naked"]
        group bot auto if_not ["bottomless", "naked"]

        group dick auto variant "outside" if_any ["outside"]
        group dick auto variant "vaginal" if_any ["vaginal"]
        group dick auto variant "anal" if_any ["anal"]

        attribute condom null
        group condom auto variant "vaginal" if_all ["vaginal", "condom"]
        group condom auto variant "outside" if_all ["outside", "condom"]

        attribute cum null
        group creampie auto if_any ["cum"] if_not ["outside"]
        group creampie auto variant "outside" if_all ["cum", "outside"] if_not ["condom"]
        group creampie auto variant "condom" if_all ["cum", "outside", "condom"]

        always "lexi_missionary_cum_onbody" if_all ["cum", "outside"] if_not ["condom"]

        attribute speed

        group gum auto

    layeredimage lexi cowgirl:
        attribute_function Pickers([PiercingsPicker, PubesPicker, DickPicker], npc=lexi)


        group bg auto:
            attribute bedroom default


        group bodies auto:
            attribute mike default

        always "lexi_cowgirl_lexibody"


        attribute clit null
        attribute navel null
        attribute tongue null
        group multiple auto variant piercings
        group piercings_naked auto when naked


        attribute naked null
        group outfits auto if_not ["naked"]



        attribute acc_arm default


        group butt auto:
            attribute up
            attribute middle
            attribute down default


        group pubes auto


        attribute cum null
        group cum_onbutt auto if_any ["cum"]


        group penis auto:
            attribute anal null
            attribute vaginal null
            attribute out null default


        group dick auto variant "vaginal" if_any ["vaginal"]
        group dick auto variant "anal" if_any ["anal"]


        group pubes auto variant "vaginal" if_any ["vaginal"]


        attribute condom null
        group condom auto variant "vaginal" if_all ["condom", "vaginal"]


        attribute creampie null
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["condom"]
        group creampie auto variant "anal" if_all ["creampie", "anal"]


        attribute vaginaldrip null
        attribute analdrip null
        group vaginaldrip auto if_any ["vaginaldrip"]
        group analdrip auto if_any ["analdrip"]


        group dick auto variant "out" if_any ["out"] if_not ["master"]
        attribute master "lexi_cowgirl_dick_out_medium" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "out"] if_not ["condom", "master"]
        attribute master "lexi_cowgirl_dickcum_medium" if_all ["dickcum", "out"] if_not ["condom"]


        group condom auto variant "out" if_all ["condom", "out"] if_not ["cumshot", "master"]
        attribute master "lexi_cowgirl_condom_out_medium" if_all ["condom", "out"] if_not ["cumshot"]


        group condomcum auto if_all ["condom", "cumshot", "out"] if_not ["master"]
        attribute master "lexi_cowgirl_condomcum_medium" if_all ["condom", "cumshot", "out"]


        attribute cumshot null
        group cumshot auto if_all ["cumshot", "out"] if_not ["condom", "master"]
        attribute master "lexi_cowgirl_cumshot_medium" if_all ["cumshot", "out"] if_not ["condom"]


        group mouth auto:
            attribute smile default
            attribute pleasure
            attribute panting


        attribute bubblegum null
        group bubblegum auto if_any ["bubblegum"]:
            attribute blow default
            attribute pop


        group eyes auto:
            attribute normal default
            attribute ahegao


        attribute mikehand


        attribute masterhand

    layeredimage lexi doggy:
        attribute_function Pickers([PregnancyPicker, PubesPicker, DickPicker, PiercingsPicker, CollarPicker], npc=lexi)


        group bg auto:
            attribute bedroom default


        always "lexi_doggy_bodies"

        attribute naked null
        group outfit_back auto if_not "naked"


        attribute pubes


        attribute collar


        attribute cum null
        group multiple auto variant cum when cum     


        group multiple auto variant piercings

        group multiple:
            attribute tongue null


        attribute vaginaldrip
        attribute analdrip


        group dick auto:
            attribute vaginal
            attribute anal


        attribute creampie null
        group creampie auto if_any ["creampie"]


        group condom auto if_any ["condom"]


        group dick_out auto if_not ["vaginal", "anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal", "anal"]


        attribute condom null
        group condom_out auto if_any ["condom"] if_not ["cumshot", "vaginal", "anal"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["vaginal", "anal"]


        group exp auto:
            attribute normal default
            attribute pleasure
            attribute ahegao


        attribute tongueout


        attribute acc_arm default


        attribute pregnant


        attribute slapmark

        group outfit_front auto if_not "naked"


        group hand auto:
            attribute noslap default
            attribute slap

    layeredimage nightclub 3bj:
        attribute_function MultiPickers([PiercingsPicker, HaircutPicker, OutfitPicker], npcs=[lexi, sasha])


        group bg auto:
            attribute bathroom default


        always "nightclub_3bj_body"
        attribute lexi_nohaircut null


        attribute sasha_boobjob
        attribute sasha_noboobjob null


        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_nose null
            attribute sasha_ears null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
        group multiple auto variant piercings_bb when bb
        group multiple auto variant piercings_nobb when not sasha_boobjob


        attribute naked null
        attribute lexi_naked null
        attribute sasha_naked null
        group outfit auto variant "sasha" if_not ["sasha_boobjob", "naked", "sasha_naked"]:
            attribute sasha_casual null
        group outfit auto variant "sasha_bb" if_any ["sasha_boobjob"] if_not ["naked", "sasha_naked"]
        group outfit auto variant "lexi" if_not ["naked", "lexi_naked"]


        group faces auto:
            attribute watch default
        group lexiexp auto
        group sashaexp auto


        group multiple auto variant piercings_watch when watch
        group multiple auto variant piercings_kiss when kiss


        group hair auto variant "watch" if_any ["watch"]
        group hair auto variant "kiss" if_any ["kiss"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute dick


        attribute cumshot if_any ["dick"]

    layeredimage nightclub threesome:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, HaircutPicker], npcs=[sasha], append_npc_from_attributes=True)
        attribute sasha null


        group bg auto:
            attribute toilet default


        attribute sasha


        group sashaexp auto:
            attribute sashanormal default


        attribute sasha_pregnant


        attribute sasha_boobjob
        attribute sasha_noboobjob null


        group multiple auto variant sashapiercings
        group multiple:
            attribute sasha_ears null
        attribute sasha_lips null
        attribute sasha_clit null
        attribute sasha_tongue null
        group multiple auto variant sashapiercings_bb when sasha_boobjob
        group multiple auto variant sashapiercings_nobb when not sasha_boobjob


        attribute sashanaked null
        attribute sasha_casual null
        group sashaclothing auto if_not ["sasha_boobjob", "sashanaked"]
        group sashaclothing auto variant "bb" if_any ["sasha_boobjob"] if_not ["sashanaked"]
        group sashaclothing auto variant "preg" if_any ["sasha_pregnant"] if_not ["sashanaked"]


        group hair auto


        attribute sasha_collar


        attribute mike null
        attribute mike_casual null
        attribute mike_date null
        attribute mike_nohaircut null
        group mikebody auto if_any ["mike"]:
            attribute fuck default
            attribute nodick null
        group dick auto if_any ["mike"] if_not ["nodick"]:
            attribute normal default
        group dick_size:
            attribute mike_big null
            attribute mike_medium null
            attribute mike_small null


        group shadow auto variant "lexinaked" if_all ["lexi", "lexinaked"]
        group shadow auto variant "clothes" if_all ["lexi"] if_not ["lexinaked"]


        attribute lexi null
        attribute lexi_collar null
        attribute lexi_nohaircut null
        group lexibody auto if_any ["lexi"]


        group lexipreg auto if_all ["lexi", "lexi_pregnant"]


        group lexiexp auto if_any ["lexi"]


        group multiple auto variant lexipiercings_fuck when lexi and fuck
        group multiple:
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_nose null
            attribute lexi_tongue null
        group multiple auto variant lexipiercings_suck when lexi and suck


        attribute lexinaked null
        attribute lexi_casual null
        group lexiclothing auto variant "fuck" if_all ["lexi", "fuck"] if_not ["lexi_pregnant"]
        group lexiclothing auto variant "fuck_preg" if_all ["lexi", "fuck", "lexi_pregnant"]
        group lexiclothing auto variant "suck" if_all ["lexi", "suck"]


        attribute cum null
        group cum auto if_any ["cum"]

    layeredimage nightclub bj lexi dwayne:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker], npc=lexi)

        always "nightclub_bj_lexi_dwayne_bg"
        always "nightclub_bj_lexi_dwayne_bodies"

        attribute pregnant

        group exp auto:
            attribute normal default null

        group multiple auto variant piercings

        attribute naked null
        always "nightclub_bj_lexi_dwayne_outfit_date" if_not ["naked"]

        attribute collar

        always "nightclub_bj_lexi_dwayne_mike_balls"
        group dick auto

        always "nightclub_bj_lexi_dwayne_lexi_arm"

        attribute cum null
        group mike_cum auto if_any ["cum"]
        always "nightclub_bj_lexi_dwayne_dwayne_cum" if_any ["cum"]

    layeredimage nightclub threesomelexi dwayne:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker], npc=lexi)

        always "nightclub_threesomelexi_dwayne_bg"
        always "nightclub_threesomelexi_dwayne_bodies"

        attribute pregnant

        group exp auto:
            attribute lewd default

        group multiple auto variant piercings

        attribute naked null
        always "nightclub_threesomelexi_dwayne_outfit_date" if_not ["naked"]

        attribute collar

        group dick auto

        attribute cum null
        always "nightclub_threesomelexi_dwayne_cum" if_any ["cum"]

    layeredimage lexi showersex:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, DickPicker, PubesPicker], npc=lexi)

        always "lexi_showersex_bg"

        always "lexi_showersex_bodies"

        attribute pubes

        attribute pregnant

        attribute nose null
        attribute tongue null
        group multiple auto variant piercings

        group exp auto:
            attribute normal default

        attribute collar

        attribute outside null
        attribute vaginal null
        attribute anal null
        group outside auto if_any ["outside"] if_not ["vaginal", "anal"]
        group vaginal auto if_any ["vaginal"] if_not ["outside", "anal"]
        group anal auto if_any ["anal"] if_not ["vaginal", "outside"]

        attribute creampie null
        group creampie auto variant "outside" if_all ["creampie", "outside"]
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"]
        group creampie auto variant "anal" if_all ["creampie", "anal"]

        group multiple auto variant fx

        always "lexi_showersex_fg"

    layeredimage lexi lapdance:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, MCCGPicker], npc=lexi)

        group bg auto:
            attribute stripclub default

        attribute mikemc null
        attribute naked null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mcoutfit auto when not naked:
            attribute mc_casual default

        attribute nonpc null
        always "lexi_lapdance_lexi" when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        attribute collar when not nonpc

        group multiple auto variant piercings when not nonpc

        attribute lexi_naked null
        group outfits auto when not (nonpc or naked or lexi_naked)

        always "lexi_lapdance_fg"
        always "lexi_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage lexi ending:
        always "lexi_ending_bg"

        group multiple auto variant kids

        always "lexi_ending_fg"

    layeredimage lexi ending2:
        always "lexi_ending2_bg"

        group outfit auto

        always "lexi_ending2_fg"

    layeredimage lexi mast:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker], npc=lexi)


        attribute clit null
        attribute ears null
        attribute navel null
        attribute nipples null
        attribute nose null
        attribute pubes null
        attribute tongue null


        always "lexi_mast_bg_livingroom"


        always "lexi_mast_hair"
        always "lexi_mast_body"
        attribute pubes


        attribute pregnant


        attribute squirt


        group lefthand auto:
            attribute finger default

        group righthand auto:
            attribute ltit default


        attribute ahegao

        always "lexi_mast_head_face" if_not ["ahegao"]
        group eyes auto if_not ["ahegao"]:
            attribute opened default
        group mouth auto if_not ["ahegao"]:
            attribute open default
        always "lexi_mast_head_hair" if_not ["ahegao"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
