init 1:
    layeredimage alexis:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=alexis)


        attribute idle null


        group acc_back auto


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_sad when sad
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_flirt when flirt
        group multiple auto variant piercings_cry when cry
        group multiple auto variant piercings_confused when confused
        group multiple auto variant piercings_angry when angry
        group multiple auto variant piercings_wink when wink
        group multiple auto variant piercings_upset when upset
        group multiple auto variant piercings_mean when mean


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute nopatsies null
        group patsies auto variant "a" if_any ["a"] if_not ["nopatsies", "topless", "naked"]
        group patsies auto variant "b" if_any ["b"] if_not ["nopatsies", "topless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]

        group gloves auto variant "a" if_any ["a"] if_not ["pregnant", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["pregnant", "naked"]
        group gloves auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked"]
        group gloves auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked"]


        group acc_head auto


        attribute collar


        group necklace auto if_not "collar"


        group fx auto


        group arm auto

    layeredimage alexis close:
        yalign 0.05
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=alexis)


        attribute idle null


        group acc_back auto


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_sad when sad
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings_flirt when flirt
        group multiple auto variant piercings_cry when cry
        group multiple auto variant piercings_confused when confused
        group multiple auto variant piercings_angry when angry
        group multiple auto variant piercings_wink when wink
        group multiple auto variant piercings_upset when upset
        group multiple auto variant piercings_mean when mean


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute nopatsies null
        group patsies auto variant "a" if_any ["a"] if_not ["nopatsies", "topless", "naked"]
        group patsies auto variant "b" if_any ["b"] if_not ["nopatsies", "topless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]

        group gloves auto variant "a" if_any ["a"] if_not ["pregnant", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["pregnant", "naked"]
        group gloves auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked"]
        group gloves auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked"]


        group acc_head auto


        attribute collar


        group necklace auto if_not "collar"


        group fx auto


        group arm auto

    layeredimage alexis smartphone:
        always "alexis_smartphone"

    layeredimage alexis cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=alexis)

        attribute noacc null


        always "alexis_cowgirl_bg"


        group acc_back auto if_not ["noacc"]


        always "alexis_cowgirl_bodies"


        group acc_head auto if_not ["noacc"]


        attribute pregnant


        group outfit auto if_not ["pregnant"]
        group outfit auto variant "pregnant" if_any ["pregnant"]


        attribute anal if_not ["vaginal"]


        attribute drip null
        group drip auto if_any ["drip"]:
            attribute all default


        attribute vaginal if_not ["anal"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["hard", "condom"]


        group dick auto if_not ["vaginal", "anal"]:
            attribute limp default


        attribute condom null
        attribute cum null
        group condom auto:
            attribute hard if_all ["condom", "hard"] if_not ["cum", "vaginal", "anal"]
            attribute vaginal if_all ["condom", "vaginal"] if_not ["hard", "anal"]


        attribute collar


        group cum auto:
            attribute condom if_all ["cum", "condom", "hard"] if_not ["vaginal", "anal"]
            attribute onbody if_all ["cum", "onbody"] if_not ["condom", "vaginal", "anal"]


        group exp auto:
            attribute pleasure default


        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings


        attribute cumshot if_any ["hard"]

    layeredimage alexis kiss:
        attribute_function Pickers([OutfitPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=alexis)


        group multiple auto variant acc0 when not naked


        always:
            "alexis_kiss"


        attribute pregnant


        group multiple:
            attribute clit null
            attribute ears null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
        group multiple auto variant piercings


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "naked", "topless"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]


        group necklace auto if_not ["collar"]


        attribute collar


        group outfitmike auto if_not ["naked"]:
            attribute normal default


        group multiple auto variant acc when not naked

    layeredimage alexis movie bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker], npc=alexis)


        attribute clit null
        attribute ears null
        attribute lips null
        attribute navel null


        always "alexis_movie_bj_bg"


        always "alexis_movie_bj_bodies"


        attribute pregnant


        group head auto:
            attribute down default
        attribute collar null
        group collar auto when collar
        attribute blush null
        group blush auto when blush
        group eyes auto variant look when look:
            attribute open default
        group eyes auto variant down when down:
            attribute open default


        attribute facecum
        attribute cum "alexis_movie_bj_mouthcum" when down


        attribute hand null
        group hand auto when hand:
            attribute up null


        group multiple auto variant piercings
        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_look when look
        group multiple auto variant piercings_down when down


        attribute cum when up


        always "alexis_movie_bj_shade"

    layeredimage alexis bj:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=alexis)

        attribute cum null


        always "alexis_bj_bg"


        always "alexis_bj_body"


        attribute collar


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null



        group exp_mouth auto if_not ["blowjob"]:
            attribute smile default

        group exp_eyes auto:
            attribute open default


        attribute pregnant


        attribute onface if_all ["cum", "onface"]


        group dick auto:
            attribute limp default


        attribute inmouth if_all ["cum", "inmouth", "blowjob"]


        attribute speed


        attribute cumshot if_any ["hard"]


        attribute pinch

    layeredimage alexis lick:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker], npc=alexis)


        always "alexis_lick_bg"


        always "alexis_lick_body"


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings


        attribute collar


        attribute blush


        group exp auto:
            attribute normal default


        attribute spread


        group multiple auto variant piercings_spread when spread


        attribute mikewet


        attribute miketongue


        group liquid auto if_any ["spread"]

    layeredimage alexis doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PubesPicker, MCCGPicker], npc=alexis)

        group multiple auto variant unused_attributes
        group multiple:
            attribute mc_casual null
            attribute mc_date null


        always "alexis_doggy_bg"


        group alexis auto:
            attribute out default


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute clit null
        group clit if_any ["clit"]:
            attribute out
            attribute vaginal "alexis_doggy_clit_out" if_any ["nomc"]
            attribute anal


        attribute bodycum null
        group bodycum auto if_any ["bodycum"]


        always "alexis_doggy_head"
        group mouths auto:
            attribute normal default
        group eyes auto:
            attribute open default


        attribute nose


        attribute collar


        attribute nomc null
        attribute mikemc null
        group mc auto if_not ["nomc"]


        group dick auto if_not ["nomc"]
        group dick auto variant "out" if_any ["out"] if_not ["nomc"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["nomc"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["nomc"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom", "nomc"]
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom", "nomc"]


        group clit if_any ["clit"] if_not ["nomc"]:
            attribute vaginal


        group mc_pubes auto if_any ["mc_pubes"]


        always "alexis_doggy_fg"

    layeredimage alexis missionary:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=alexis)


        always "alexis_missionary_bg"


        always "alexis_missionary_bodies"


        attribute stockings


        attribute collar


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings


        attribute cum null
        group multiple auto variant cum when cum


        group fuck auto


        group multiple auto variant piercings_vaginal when vaginal


        attribute creampie null
        group creampie auto if_any ["creampie"]


        group dick auto if_not ["vaginal", "anal"]:
            attribute limp default


        attribute condom null
        group condom auto:
            attribute outside if_all ["condom", "hard"] if_not ["vaginal", "anal"]
            attribute cum if_all ["condom", "hard", "cum"] if_not ["vaginal", "anal"]
            attribute vaginal if_all ["condom", "vaginal"] if_not ["anal"]


        attribute cumshot null
        attribute cumshot if_all ["cumshot", "hard"] if_not ["condom"]

    layeredimage alexis ntr handjob:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=alexis)


        always "alexis_ntr_handjob_bg"


        group exp auto:
            attribute normal default


        attribute necklace if_not ["collar"]


        attribute collar


        attribute pregnant


        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_happy when happy
        group multiple auto variant piercings

        group multiple:
            attribute clit null
            attribute pregnant_navel null


        attribute cum null
        group cum auto if_any ["cum"]:
            attribute onbody default


        attribute dickcum null
        group multiple auto variant dickcum when dickcum


        attribute cumshot null
        group multiple auto variant cumshot when cumshot


        always "alexis_ntr_handjob_light"

    layeredimage alexis ntr bukake:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=alexis)


        always:
            "alexis_ntr_bukake_bg"


        always:
            "alexis_ntr_bukake_bodies"


        attribute pregnant


        group acc auto


        always "alexis_ntr_bukake_blush"


        group exp auto:
            attribute lookleft default


        group multiple auto variant piercings_swallow when swallow
        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null


        attribute cum null
        group multiple auto variant cum when cum


        attribute dickcum null
        group multiple auto variant dickcum when dickcum


        attribute cumshot null
        group multiple auto variant cumshot when cumshot

    layeredimage alexis ntr gangbang:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=alexis)


        always "alexis_ntr_gangbang_bg"


        always "alexis_ntr_gangbang_bodies"


        group exp auto:
            attribute normal default


        group dick_left auto:
            attribute leftout default
        group dick_middle auto:
            attribute middleout default
        group dick_right auto:
            attribute rightout default


        attribute condom null
        group condom auto if_any ["condom"]:
            attribute out default


        attribute creampie null
        group multiple auto variant creampie when creampie


        attribute dickcum null
        group multiple auto variant dickcum when dickcum


        attribute cumshot null
        group multiple auto variant cumshot when cumshot


        group multiple auto variant piercings_notvaginal when not vaginal
        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute navel null
            attribute pregnant_navel null


        group collar auto if_any ["collar"]:
            attribute classic default


        always "alexis_ntr_gangbang_light"

    layeredimage alexis reverse:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker, MCCGPicker], npc=alexis)


        attribute mc_casual null
        attribute mc_date null
        attribute lips null
        attribute mikemc null


        group bg auto:
            attribute bedroom default


        always "alexis_reverse_male_mikemc" when not ntr
        attribute ntr "alexis_reverse_male_ntr"


        always "alexis_reverse_alexis"
        attribute pregnant
        attribute pubes
        group mouths auto:
            attribute mouth_hurt default
        group eyes auto:
            attribute eyes_normal default
        attribute collar
        group multiple auto variant piercings
        group multiple auto variant piercings_notvaginal when not vaginal


        always "alexis_reverse_malehands_mikemc" when not ntr
        attribute ntr "alexis_reverse_malehands_ntr"


        group dick_ntr auto when ntr:
            attribute out default
        group dick_mikemc auto when not ntr:
            attribute out default null
        group dick_mikemc auto variant out when not ntr and out
        group multiple auto variant piercings_vaginal when vaginal


        attribute condom null
        group condom_ntr auto when condom and ntr
        group condom_mikemc auto when condom and not ntr
        group condom_mikemc auto variant out when condom and not ntr and out


        attribute cum null
        group cum_ntr auto when cum and not condom and ntr
        group cum_mikemc auto when cum and not condom and not ntr
        group cum_mikemc auto variant out when cum and not condom and not ntr and out


    layeredimage alexis halloween ntr foursome:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=alexis)


        always "alexis_halloween_ntr_foursome_bg"


        always "alexis_halloween_ntr_foursome_bodies"


        attribute collar


        group multiple auto variant piercings


        attribute pregnant


        group exp auto


        attribute cum

    layeredimage alexis ntr glory hole:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npc=alexis)


        always "alexis_ntr_glory_hole_bg"


        group multiple auto variant bg_cum 


        group multiple auto variant bg_dick 
        attribute cumdickleft if_any ["dickleft"]
        attribute cumdickright if_any ["dickright"]


        group left:
            attribute leftman
            attribute futa


        group right:
            attribute rightman
            attribute mike


        attribute alexis null
        always "alexis_ntr_glory_hole_lowbody" if_any ["alexis"]
        group upbody if_any ["alexis"]:
            attribute stand default
            attribute leftblowjob
            attribute rightblowjob


        attribute pubes if_any ["alexis"]


        group pregnancy auto if_all ["alexis", "pregnant"]


        group head if_any ["alexis"] if_not ["stand"]:
            attribute leftblowjob
            attribute rightblowjob
        group head if_all ["alexis", "stand"]:
            attribute wantleftcum
            attribute wantrightcum
        always "alexis_ntr_glory_hole_head" if_all ["alexis", "stand"] if_not ["wantleftcum", "wantrightcum"]


        group collar if_all ["alexis", "collar"] if_not ["stand"]:
            attribute leftblowjob
            attribute rightblowjob
        group collar if_all ["alexis", "collar", "stand"]:
            attribute wantleftcum
            attribute wantrightcum
        attribute collar if_all ["alexis", "stand"] if_not ["wantleftcum", "wantrightcum"]


        group eyes_leftblowjob if_all ["alexis", "leftblowjob"]:
            attribute opened default
            attribute closed
        group eyes_rightblowjob if_all ["alexis", "rightblowjob"]:
            attribute opened default
            attribute closed
        group exp if_all ["alexis", "stand"] if_not ["wantleftcum", "wantrightcum"]:
            attribute pleasure default
            attribute ahegao


        group multiple auto variant piercings_stand when alexis and stand
        group multiple auto variant piercings_leftblowjob when alexis and leftblowjob
        group multiple auto variant piercings_rightblowjob when alexis and rightblowjob
        group multiple auto variant piercings_wantleftcum when alexis and wantleftcum
        group multiple auto variant piercings_wantrightcum when alexis and wantrightcum
        group multiple auto variant piercings when alexis
        group multiple auto variant face_piercings_stand when alexis and stand and not (wantleftcum or wantrightcum)


        attribute facecum null
        group facecum auto if_all ["alexis", "facecum"]


        group rightman auto variant "dick" if_any ["rightman"]
        group rightman auto variant "cumshot" if_all ["rightman", "cumshot"]


        group mike auto variant "dick_stand" if_all ["mike", "stand"]
        group mike auto variant "dick_leftblowjob" if_all ["mike", "leftblowjob"]
        group mike auto variant "dick_rightblowjob" if_all ["mike", "rightblowjob"]
        attribute cumshot null
        group mike auto variant "cumshot_stand" if_all ["mike", "cumshot", "stand"]
        group mike auto variant "cumshot_leftblowjob" if_all ["mike", "cumshot", "leftblowjob"]
        group mike auto variant "cumshot_rightblowjob" if_all ["mike", "cumshot", "rightblowjob"]


        group futa auto variant "dick" if_all ["futa"]
        group futa auto variant "cumshot" if_all ["futa", "cumshot"]


        group leftman auto variant "dick" if_all ["leftman"]
        group leftman auto variant "cumshot" if_all ["leftman", "cumshot"] if_not ["wantleftcum"]
        group leftman auto variant "cumshot_wantleftcum" if_all ["leftman", "cumshot", "wantleftcum"]


        attribute peace null
        always "alexis_ntr_glory_hole_arm_peace" if_all ["alexis", "stand", "peace"] if_not ["leftblowjob", "rightblowjob"]
        always "alexis_ntr_glory_hole_arm_stand" if_all ["alexis", "stand"] if_not ["peace"]
        always "alexis_ntr_glory_hole_arm_leftblowjob" if_all ["alexis", "leftblowjob"]
        always "alexis_ntr_glory_hole_arm_rightblowjob" if_all ["alexis", "rightblowjob"]


        always "alexis_ntr_glory_hole_light"


        group multiple auto variant cum 
        always "alexis_ntr_glory_hole_cumed_onalexis" if_all ["alexisleftcum", "alexisrightcum"]


        attribute record null
        always "alexis_ntr_glory_hole_recordeffect" if_any ["record"]


        always "alexis_ntr_glory_hole_backlight"


        always:
            "alexis_ntr_glory_hole_watch_chair"


        attribute watch null
        always "alexis_ntr_glory_hole_watch_mike" if_any ["watch"] if_not ["mike"]


        always "alexis_ntr_glory_hole_forelight"

    layeredimage alexis ntr office:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker], npc=alexis)


        always "alexis_ntr_office_bg"


        always "alexis_ntr_office_alexis"


        attribute bodycum


        attribute pregnant


        group exp auto:
            attribute normal default


        attribute noguy null
        always "alexis_ntr_office_guy" if_not ["noguy"]


        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null


        attribute collar


        group dick auto if_not ["noguy"]:
            attribute out default


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cumshot", "noguy"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["noguy"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "noguy"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom", "noguy"]


        always "alexis_ntr_office_details"

    layeredimage alexis ntr bj school reunion:


        always "alexis_ntr_bj_school_reunion_bg"


        attribute mike
        always "alexis_ntr_bj_school_reunion_bodies"


        attribute naked null
        always "alexis_ntr_bj_school_reunion_outfit_casual" if_not ["naked"]

    layeredimage alexis ntr wedding:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker], npc=alexis)


        always "alexis_ntr_wedding_bg"


        always "alexis_ntr_wedding_mike"


        group exp auto:
            attribute sad default


        always "alexis_ntr_wedding_alexis"


        attribute pregnant


        attribute collar


        group mouth auto if_not ["blowjob"]:
            attribute tongueout default


        attribute mouthcum if_any ["tongueout"] if_not ["blowjob"]


        group eyes auto:
            attribute opened default


        group multiple auto variant piercings
        group multiple auto variant piercings_lips when lips
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null


        group dick auto:
            attribute out default


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]


        always "alexis_ntr_wedding_priest"


        always "alexis_ntr_wedding_petals"


        always "alexis_ntr_wedding_glitter"


        always "alexis_ntr_wedding_light"

    layeredimage alexis ending:


        always "alexis_ending_bg"


        if alexis.flags.mikeBabies >= 1 or alexis.is_visibly_pregnant:
            "alexis_ending_baby"
        else:
            "alexis_ending_dog"


        if alexis.flags.story != 2 and alexis.flags.mikeBabies < 1 and alexis.is_visibly_pregnant:
            "alexis_ending_blackskin"

        always "alexis_ending_alexis"

    layeredimage alexis beach threesome:



        attribute cum null


        always "alexis_beach_threesome_bg"


        attribute mike


        always "alexis_beach_threesome_malebodies"


        group head auto:
            attribute lick default


        attribute collar null
        group collar auto when collar


        group multiple auto variant piercings_lick when lick
        group multiple auto variant piercings_suck when suck


        attribute lick "alexis_beach_threesome_exp_lick"
        group exp_suck auto when suck:
            attribute normal default


        attribute facecum


        attribute lick "alexis_beach_threesome_dick_left_lick"


        group cum_dick_left auto when cum


        always "alexis_beach_threesome_bodies"


        group multiple auto variant piercings_notvaginal when not vaginal


        attribute pregnant


        attribute bulge when vaginal


        always "alexis_beach_threesome_water"


        group dick_right auto:
            attribute out default


        group cum_dick_right auto when cum


        group multiple auto variant piercings_vaginal when vaginal


        attribute pubes


        group multiple auto variant piercings


        group outfit auto
        group outfit auto variant nopreg when not pregnant
        group outfit auto variant preg when pregnant


        always "alexis_beach_threesome_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
