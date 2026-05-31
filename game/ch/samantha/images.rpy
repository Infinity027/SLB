init 1:
    layeredimage samantha:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=samantha)


        attribute idle null


        always:
            if_not ["halloween"]
            "samantha_backhair"
        always:
            if_any ["halloween"]
            "samantha_backhair_halloween"


        group acc_back auto if_not ["topless", "naked"]


        always:
            "samantha_body"


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings_body


        attribute naked null


        attribute bottomless null
        group stockings auto when not (naked or bottomless)
        group bot auto if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["topless", "naked"]


        group necklace auto if_not ["collar"]


        attribute collar


        always:
            "samantha_head"


        attribute blush


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings_face
        group multiple auto variant piercings_face_lips when lips


        always:
            "samantha_fronthair"


        group acc_head auto if_not ["topless", "naked"]


        group arm auto


        group handpos auto


        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        attribute ring null
        group ring auto if_any ["ring"]


        group fx auto

    layeredimage samantha close:
        yalign 0.14
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=samantha)


        attribute idle null


        always:
            if_not ["halloween"]
            "samantha_close_backhair"
        always:
            if_any ["halloween"]
            "samantha_close_backhair_halloween"


        group acc_back auto if_not ["topless", "naked"]


        always:
            "samantha_close_body"


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings_body


        attribute naked null

        attribute bottomless null
        group stockings auto when not (naked or bottomless)
        group bot auto if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["topless", "naked"]


        group necklace auto if_not ["collar"]


        attribute collar


        always:
            "samantha_close_head"


        attribute blush


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings_face
        group multiple auto variant piercings_face_lips when lips


        always:
            "samantha_close_fronthair"


        group acc_head auto if_not ["topless", "naked"]


        group arm auto


        group handpos auto


        group acc_hand auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_hand auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        attribute ring null
        group ring auto if_any ["ring"]


        group fx auto

    layeredimage samantha smartphone:
        always "samantha_smartphone"

    layeredimage samantha babyshopping:
        always "samantha_babyshopping"

    layeredimage samantha cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, DickPicker, CollarPicker], npc=samantha)

        attribute samantha default
        always "samantha_cowgirl_bg"
        always "samantha_cowgirl_mike"

        group position:
            attribute down null default
            attribute up null

        group body auto variant "down" if_any "down"
        group body auto variant "up" if_any "up"

        group pregnancy auto variant "down" if_any "down"
        group pregnancy auto variant "up" if_any "up"

        group collars auto variant "down" if_any "down"
        group collars auto variant "up" if_any "up"

        group sampubes auto variant "down" if_any "down"
        group sampubes auto variant "up" if_any "up"

        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute lips null
            attribute tongue null
        group multiple auto variant piercings_down when down
        group multiple auto variant piercings_up when up

        group dick auto variant "outside" if_not ["vaginal", "anal"]
        group dick auto variant "up" if_any "up"
        group dick_vaginal auto variant "down" if_all ["down", "vaginal"]

        group mikepubes auto

        attribute condom null
        group condom auto variant "outside" if_not ["anal", "vaginal"] if_any "condom"
        group condom auto variant "up" if_all ["condom", "up"]
        group condom auto variant "down" if_all ["condom", "down"]

        group exp auto variant "down" if_any "down":
            attribute normal default
        group exp auto variant "up" if_any "up"

        group fx auto

        attribute creampie null
        group creampies auto variant "down" if_all ["down", "creampie"]
        group creampies auto variant "up" if_all ["up", "creampie"]

        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal"]

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["condom", "vaginal"," anal"]

        group condomcum auto if_all ["cumshot", "condom"] if_not ["vaginal", "anal"]

        attribute cum null
        group cum auto variant "down" if_all ["down", "cum"]
        group cum auto variant "up" if_all ["up", "cum"]

    layeredimage samantha reversecowgirl:
        attribute_function Pickers([PregnancyPicker, CollarPicker, DickPicker], npc=samantha)

        always "samantha_reversecowgirl_bg"

        always "samantha_reversecowgirl_mike"
        always "samantha_reversecowgirl_samantha"

        attribute pregnant
        attribute collar

        group body_layer auto

        group dick auto
        group dick auto variant "outside" if_not ["anal", "vaginal"]

        attribute condom null
        group condom auto if_all "condom" if_any ["anal", "vaginal"]
        group condom auto variant "outside" if_not ["anal", "vaginal"] if_any "condom"

        always:
            "samantha_reversecowgirl_mike_pubes"

        group exp auto:
            attribute normal default

        group multiple auto variant fx

        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]

        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal"," anal"]

        group condomcum auto if_all ["cumshot", "condom"] if_not ["vaginal", "anal"]

        attribute cum null
        group cum auto if_any ["cum"]



    layeredimage samantha kiss:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker], npc=samantha)


        always:
            "samantha_kiss"


        attribute collar


        group necklace auto if_not ["collar"]


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute navel null
            attribute tongue null
            attribute nose null
            attribute pregnant_navel null


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]


        group acc auto if_not ["naked"]


        attribute ring


        attribute mc_casual null
        group mikeoutfit auto when not (naked or mc_casual):
            attribute normal default
        always "samantha_kiss_mikeoutfit_normal" when mc_casual

    layeredimage samantha bj:

        group stuff:
            attribute suck null
            attribute nosuck default

        attribute cumshot null

        always "samantha_bj_bg"

        always "samantha_bj_body"

        always "samantha_bj_man"

        always:
            if_any ["suck"]
            "samantha_bj_head_suck"

        always:
            if_not ["suck"]
            "samantha_bj_head_normal"

        group exp:
            attribute closed default:
                if_any ["suck"]
                "samantha_bj_exp_sucka"
            attribute open:
                if_any ["suck"]
                "samantha_bj_exp_suckb"

        group exp2:
            attribute normal default:
                if_not ["suck"]
                "samantha_bj_exp_normal"
            attribute surprise:
                if_not ["suck"]
                "samantha_bj_exp_surprise"

        if samantha.piercings.tongue.worn:
            if_any ["surprise"]
            if_not ["normal", "suck"]
            "samantha_bj_piercings_tongueb"

        if samantha.piercings.tongue.worn:
            if_not ["surprise", "suck"]
            if_any ["normal"]
            "samantha_bj_piercings_tonguea"

        group dick:
            attribute nodick null
            attribute out default:
                if_not ["suck"]
                "samantha_bj_dick"
            attribute inside:
                if_not ["suck"]
                "samantha_bj_dick_tits"

        always:
            if_all ["suck", "cumshot"]
            "samantha_bj_cum_mouth"

        always:
            if_not ["suck"]
            if_any ["cumshot"]
            "samantha_bj_cumshot"

        group arms auto

        attribute cumface:
            if_not ["suck"]
            "samantha_bj_cum_face"

        attribute cumchest:
            if_not ["suck"]
            "samantha_bj_cum_chest"

        attribute lotion:
            if_not ["suck"]
            "samantha_bj_lotion"

        if samantha.piercings.nipples.worn:
            "samantha_bj_piercings_nipples"

        always:
            "samantha_bj_shadow"

    layeredimage samantha doggy:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, XrayPicker, PubesPicker], npc=samantha)

        attribute pregnant null

        group bg auto:
            attribute bedroom default

        always "samantha_doggy_body"

        attribute nomike null
        group position auto if_not ["nomike"]:
            attribute vaginal default

        attribute milk

        attribute red
        attribute write

        group dick auto if_not ["nomike"]

        attribute condom null
        group condom auto if_any ["condom"] if_not ["nomike"]
        attribute cum null
        group condomcum auto if_all ["condom", "cum"] if_not ["nomike"]

        attribute arm null
        group hands auto if_any ["arm"] if_not ["nomike"]

        attribute xray null
        group xray auto if_any ["xray"] if_not ["nomike"]

        attribute creampie null
        group xray_cum auto if_all ["xray"] if_any ["creampie"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        always "samantha_doggy_dick_hair" if_not ["nomike"]

        group eyes auto:
            attribute wink default
        group mouth auto:
            attribute scream default
        always "samantha_doggy_gag_drool" if_any ["gag"]

        group multiple auto variant cum when cum and not nomike

        attribute beads if_not ["anal"]
        attribute dildo if_not ["vaginal"]

        attribute squirt if_any ["dildo"] if_not ["vaginal"]:
            "samantha_doggy_dildo_squirt"

        attribute spank

        group multiple auto variant piercings
        group multiple:
            attribute navel null
            attribute pregnant_navel null
            attribute ears null
        group multiple auto variant piercings_smile when smile
        group piercings auto variant "pant" if_not ["smile"]

        attribute pubes

    layeredimage samantha mmf:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker], npc=samantha)

        always "samantha_mmf_bg"

        always "samantha_mmf_body"

        attribute pregnant

        group mouth auto

        group eyes auto:
            attribute up default

        group multiple auto variant piercings

        attribute ryan:
            "samantha_mmf_ryan"

        group ryandick:
            if_any "ryan"
            attribute out default
            attribute suck

        group multiple auto variant cum

    layeredimage samantha missionary:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, XrayPicker], npc=samantha)

        always "samantha_missionary_base"

        attribute pregnant

        group mouth auto:
            attribute normal default

        group eyes auto:
            attribute normaleyes default

        group multiple auto variant piercings
        group piercings auto variant "ahegao" if_any "ahegao"

        always:
            if_any "navel"
            "samantha_missionary_piercings_hip"


        group dick auto:
            attribute dickout default
            attribute anal null






        group multiple auto variant cum

    layeredimage samantha bj2:

        always "samantha_bj2_base"

        group mouth auto:
            attribute lick default

        group eyes auto:
            attribute open default

        group multiple auto variant fx

    layeredimage samantha ending:
        attribute_function Pickers([PregnancyPicker, OutfitPicker, EndingKidPicker], npc=samantha)

        attribute pregnant null
        attribute kid

        always:
            if_not "pregnant"
            "samantha_ending_bg"

        always:
            if_not "pregnant"
            "samantha_ending_bodies"

        attribute naked null

        group samantha auto if_not ["pregnant", "naked"]:
            attribute swimsuit default

        group mike auto if_not ["pregnant"]:
            attribute swimsuit if_any ["swimsuit", "sexyswimsuit"]

        always:
            if_not "pregnant"
            "samantha_ending_fg"

    layeredimage samantha bj3:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker, OutfitPicker], npc=samantha)
        attribute naked null
        attribute cum null

        always "samantha_bj3_bg"
        always "samantha_bj3_body"

        attribute pregnant

        group outfits auto:
            attribute naked default null

        group outfits auto variant "pregnant" if_any "pregnant" if_not "naked"

        group p auto:
            attribute lick default

        group tongue auto

        always:
            "samantha_bj3_expmike_normal"

        attribute pregnant

        group eyes auto:
            attribute open default

        group multiple auto variant piercings
        group multiple auto variant piercings_lick when lick
        group multiple auto variant piercings_blow when blow

        group cum auto if_any "cum"

    layeredimage samantha bj4:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=samantha)

        always "samantha_bj4_bg"
        always "samantha_bj4_mike"

        group pose auto:
            attribute lick default

        group eyes_lick auto if_any ["lick"]:
            attribute down default
        group eyes_deep auto if_any ["deep"]:
            attribute deepclosed default
        group mouth auto if_any ["lick"]:
            attribute smile default

        attribute collar if_not ["deep"]

        group piercings auto
        group multiple auto variant piercings_deep when deep
        group multiple auto variant piercings_lick when lick
        group multiple auto variant piercings_lick_close when lick and not openmouth
        group multiple auto variant piercings_lick_open when lick and openmouth

        attribute naked null
        group clothes auto if_not ["naked"]

        group hands auto variant "deep" if_any ["deep"]:
            attribute rest default
        group hands auto variant "lick" if_any ["lick"]:
            attribute rest default

        group cum auto

    layeredimage samantha selfie:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=samantha)

        always "samantha_selfie_bg"
        always "samantha_selfie_base"

        attribute pregnant
        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute tongue null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null

        attribute collar
        attribute cum

    layeredimage samantha reverse:
        attribute_function Pickers([PubesPicker, CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker], npc=samantha)


        always:
            "samantha_reverse_bg"


        attribute phone if_not "calling"


        group down_dick auto if_all ["down", "anal"]
        group down_creampie auto if_all ["down", "creampie", "anal"]

        group samantha auto:
            attribute down default


        group exp_up auto if_any "up":
            attribute pleasure default
        group exp_down auto if_any "down":
            attribute pleasure default


        attribute tongue null
        attribute ears null
        group multiple auto variant piercings_up_smile when up and smile
        group multiple auto variant piercings_up_pleasure when up and pleasure
        group multiple auto variant piercings_up_orgasm when up and orgasm
        group multiple auto variant piercings_up_ahegao when up and ahegao
        group multiple auto variant piercings_down_smile when down and smile
        group multiple auto variant piercings_down_pleasure when down and pleasure
        group multiple auto variant piercings_down_orgasm when down and orgasm
        group multiple auto variant piercings_down_ahegao when down and ahegao


        group outfit_up auto if_any "up" if_not "naked"
        group outfit_down auto if_any "down" if_not "naked"


        attribute collar null
        group collar auto if_any "collar"


        group pose_up auto if_any "up":
            attribute fuck default
        group pose_down auto if_any "down":
            attribute fuck default


        group acc_arm_up_fuck auto if_all ["up", "fuck"] if_not "naked"
        group acc_arm_up_calling auto if_all ["up", "calling"] if_not "naked"
        group acc_arm_down_fuck auto if_all ["down", "fuck"] if_not "naked"
        group acc_arm_down_calling auto if_all ["down", "calling"] if_not "naked"


        group legs_up auto if_any "up":
            attribute naked default
        group legs_down auto if_any "down":
            attribute naked default


        group pregnant auto if_any "pregnant" if_not "halloween"
        group pregnant auto variant "halloween" if_all ["pregnant", "halloween"]


        group up_dick auto if_any "up"
        group down_dick auto if_any "down" if_not "anal"


        attribute creampie null
        group up_creampie auto if_all ["up", "creampie"] if_any ["vaginal", "anal"]
        group down_creampie auto if_all ["down", "creampie", "vaginal"]


        attribute condom null
        group up_condom auto if_all ["up", "condom", "vaginal"]
        group down_condom auto if_all ["down", "condom", "vaginal"]


        group pubes auto if_any "pubes"


        group multiple auto variant piercings_up when up and not halloween
        group multiple auto variant piercings_up_vaginal when up and vaginal
        group multiple auto variant piercings_up_outside when up and not (vaginal or anal)
        group multiple auto variant piercings_down when down and not halloween
        group multiple auto variant piercings_down_vaginal when down and vaginal
        group multiple auto variant piercings_down_outside when down and not (vaginal or anal)


        group dick_outside auto if_not ["vaginal", "anal"]


        group condom_outside auto if_any "condom" if_not ["condomcum", "vaginal", "anal"]


        attribute condomcum
        group condomcum_outside auto if_any "condomcum" if_not ["condom", "vaginal", "anal"]


        attribute cumshotfx null
        group cumshotfx auto if_all ["cumshot", "cumshotfx"] if_not ["vaginal", "anal", "condom", "condomcum"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["vaginal", "anal", "condom", "condomcum"]


        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not ["vaginal", "anal", "condom", "condomcum"]


        always:
            "samantha_reverse_light"

    layeredimage samantha flat doggy:
        attribute_function Pickers([OutfitPicker, PiercingsPicker], npc=samantha)

        attribute naked null
        attribute topless null
        attribute bottomless null

        group bg auto:
            attribute beach default

        always "samantha_flat_doggy_body"

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        group top auto if_not ["naked", "topless"]:
            attribute casual null
        group bot auto if_not ["naked", "bottomless"]

        group exp auto:
            attribute normal default

        attribute spankmark

        attribute nomc null
        always "samantha_flat_doggy_mikemc"

        group dick auto:
            attribute out default

        attribute condom null
        attribute cum null
        group condom auto if_any "condom"
        group condomcum auto if_all ["condom", "cum"]
        group creampie auto if_any "cum" if_not "condom"

        attribute cumshot

        group cum auto if_any "cum"

    layeredimage samantha threesome1:
        attribute_function Pickers([DickPicker])
        attribute cum null

        always "samantha_threesome1_bg"
        always "samantha_threesome1_body"

        group exp auto:
            attribute normal default

        group dick auto

        group cum auto if_any "cum"

        attribute glasses:
            "samantha_threesome1_glasses"

    layeredimage samantha threesome2:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npc=samantha)

        attribute cum null

        always "samantha_threesome2_bg"
        always "samantha_threesome2_body"

        attribute collar

        group dick auto

        group cum auto if_any "cum"

        attribute pregnant

        group multiple auto variant piercings

    layeredimage samantha threesome3:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npc=samantha)

        always "samantha_threesome3_bg"
        always "samantha_threesome3_body_natalie"
        always "samantha_threesome3_body_samantha"

        attribute collar

        group expsamantha auto:
            attribute normal default
        group expnatalie auto:
            attribute normal default

        group dick auto

        attribute glasses:
            "samantha_threesome3_glasses"

        group multiple auto variant piercings

        group multiple auto variant cum

    layeredimage sam nightclub sex:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, OutfitPicker, DickPicker], npc=samantha)

        attribute cum null
        attribute wet null

        always:
            "sam_nightclub_sex_bg"

        always:
            "sam_nightclub_sex_body"

        attribute pregnant

        group outfits auto:
            attribute date default
        group outfits auto variant "pregnant" if_any "pregnant"

        group multiple auto variant piercings

        group dick auto

        always:
            "sam_nightclub_sex_mike"

        attribute cum null
        group cum auto if_any "cum"

        attribute wet null
        group wet auto if_any "wet"

    layeredimage samantha cunnilingus:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, PubesPicker, CollarPicker], npc=samantha)
        attribute vibrate
        attribute notongue
        attribute phone

        always:
            "samantha_cunnilingus_bg"
        always:
            "samantha_cunnilingus_body_samantha"

        group exp auto:
            attribute normal default

        attribute pubes

        attribute pregnant

        attribute collar

        group multiple auto variant piercings

        group vibrator auto

        group multiple auto variant fx_vibrate when vibrate

        group tongue auto

        always:
            if_not ["up", "middle", "down", "notongue"]
            "samantha_cunnilingus_body_mike"

        always:
            if_any ["up", "middle", "down", "notongue"]
            "samantha_cunnilingus_body_mike_lickpussy"

        always:
            if_any "phone"
            "samantha_cunnilingus_samantha_hands"

        always:
            if_any "vibrate"
            "samantha_cunnilingus_remote"

        group finger auto

        group multiple auto variant samantha_fx

    layeredimage samantha showersex:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker], npc=samantha)
        attribute creampie null
        attribute outside null
        attribute vaginal null
        attribute anal null
        always:
            "samantha_showersex_bg"

        always:
            "samantha_showersex_bodies"

        attribute pregnant

        group multiple auto variant piercings
        group exp auto:
            attribute normal default

        group outside auto if_any "outside" if_not ["vaginal", "anal"]
        group vaginal auto if_any "vaginal" if_not ["outside", "anal"]
        group anal auto if_any "anal" if_not ["vaginal", "outside"]

        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"]
        group creampie auto variant "anal" if_all ["creampie","anal"]
        group creampie auto variant "outside" if_all ["creampie","outside"]

        group multiple auto variant fx


    layeredimage samantha handjob:
        attribute_function Pickers([PiercingsPicker, OutfitPicker, CollarPicker, MCCGPicker], npc=samantha)

        attribute mikemc null
        attribute samantha null

        always "samantha_handjob_bedroom"
        always "samantha_handjob_bodies"

        group mc_exp auto:
            attribute mc_normal default

        group mouth auto:
            attribute open default

        group eyes auto:
            attribute ondick default

        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        group piercings_lips if_any "lips"

        attribute naked null
        attribute mc_naked null
        attribute mc_casual if_not "naked"
        attribute casual if_not "naked"

        always "samantha_handjob_hand"

        attribute collar

        group dicks auto

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute speed
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
