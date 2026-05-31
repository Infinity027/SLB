init 1:
    layeredimage ayesha:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, OutfitPicker], npc=ayesha)


        attribute idle null


        group position auto

        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings
        group multiple auto variant piercings_lips when lips
        group multiple auto variant piercings_casual when not halloween
        group multiple auto variant piercings_halloween when halloween


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "naked", "topless"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "naked", "topless"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked", "topless"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked", "topless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "naked", "bottomless"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "naked", "bottomless"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked", "bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked", "bottomless"]


        attribute collar


        group hat auto if_not ["topless", "naked"]


        group acc_arm auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group acc_neck auto if_not ["topless", "naked"]


        group arm auto

    layeredimage ayesha close:
        yalign 0.04
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker, OutfitPicker], npc=ayesha)


        attribute idle null


        group position auto

        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings
        group multiple auto variant piercings_lips when lips
        group multiple auto variant piercings_casual when not halloween
        group multiple auto variant piercings_halloween when halloween


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "naked", "topless"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "naked", "topless"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked", "topless"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked", "topless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "naked", "bottomless"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "naked", "bottomless"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked", "bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked", "bottomless"]


        attribute collar


        group hat auto if_not ["topless", "naked"]


        group acc_arm auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless", "naked"]


        group acc_neck auto if_not ["topless", "naked"]


        group arm auto

    layeredimage ayesha smartphone:
        always "ayesha_smartphone"

    layeredimage ayesha kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, MCCGPicker], npc=ayesha)

        group dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null


        group base auto if_not ["bowsette"]
        attribute bowsette "ayesha_kiss_base_breemc_bowsette"
        group haircuts auto variant "breemc" if_any "breemc" if_not ["bowsette"]:
            attribute mc_nohaircut null


        group mcoutfits auto variant mikemc when mikemc and not naked
        group mcoutfits auto variant breemc when breemc and not naked


        group multiple auto variant piercings_mikemc when mikemc
        group multiple:
            attribute clit null
            attribute lips null
            attribute nipples null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        group multiple auto variant piercings_breemc when breemc


        attribute naked null
        attribute topless null
        group outfits auto variant "mikemc" if_any "mikemc" if_not ["naked", "topless"]
        group outfits auto variant "breemc" if_any "breemc" if_not ["naked", "topless"]:
            attribute chinese "ayesha_kiss_outfits_breemc_casual"
            attribute bowsette "ayesha_kiss_outfits_breemc_halloween"
            attribute invisible "ayesha_kiss_outfits_breemc_halloween"


        group collars auto variant "mikemc" if_any "mikemc"
        group collars auto variant "breemc" if_any "breemc"

    layeredimage ayesha missionary:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, MCCGPicker], npc=ayesha)

        attribute nomc null


        always "ayesha_missionary_bg"


        always "ayesha_missionary_ayesha"
        attribute pregnant
        attribute pubes


        group multiple auto variant piercings


        group mouth auto:
            attribute mouth_smile default
        group eyes auto:
            attribute eyes_open default


        attribute vaginalgape if_not ["vaginalgape"]
        always "ayesha_missionary_vaginalgape" if_any ["vaginaldrip"]
        attribute vaginaldrip

        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null


        attribute mikemc if_not "nomc"
        group dick auto if_any ["mikemc"] if_not "nomc"


        attribute condom null
        group condom auto if_all ["condom", "mikemc"] if_not "nomc"


        attribute cum null
        group cum auto if_all ["cum", "mikemc"] if_not ["condom", "nomc"]


        group multiple auto variant piercings_attop


        attribute squirt


        group dick auto variant "out" if_all ["out", "mikemc"] if_not "nomc"
        group condom auto variant "out" if_all ["condom", "out", "mikemc"] if_not ["cum", "nomc"]
        group condom auto variant "cum" if_all ["condom", "cum", "out", "mikemc"] if_not "nomc"
        group cum auto variant "out" if_all ["cum", "out", "mikemc"] if_not ["condom", "nomc"]


        attribute masturbate null
        group mast:
            attribute back null default
            attribute forth null
        group masturbate auto variant "back" if_all ["masturbate", "mikemc", "back"] if_not "nomc"
        group masturbate auto variant "forth" if_all ["masturbate", "mikemc", "forth"] if_not "nomc"

    layeredimage ayesha cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker], npc=ayesha)


        always "ayesha_cunnilingus_bg"


        always "ayesha_cunnilingus_ayesha"
        attribute pregnant
        group multiple auto variant piercings
        attribute pubes


        attribute plug


        attribute whipmarks_up
        attribute whipmarks_down


        attribute squirt


        group mouth auto:
            attribute mouth_normal default
        group eyes auto:
            attribute eyes_open default


        attribute mike null
        group mike auto if_any ["mike"]:
            attribute vaginal default


        attribute whip null
        group whip auto if_any ["whip"] if_not ["mike"]:
            attribute swing default

    layeredimage ayesha doggy:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=ayesha)


        always "ayesha_doggy_bg"


        always "ayesha_doggy_bodies"


        attribute pregnant


        attribute collar


        group exp auto:
            attribute angry default


        attribute clit null
        attribute navel null
        attribute nipples null
        attribute pregnant_navel null
        group multiple auto variant piercings
        group multiple auto variant piercings_notahegao when not ahegao


        group tattoo auto


        group outfit auto


        group multiple auto variant piercings_halloween when halloween


        group dick_in auto


        attribute xray null
        group xray auto if_any "xray"


        attribute creampie null
        group xray_creampie auto if_all ["xray","creampie"] if_not "condom"


        attribute condom null
        group xray_condom auto if_all ["xray","condom"] if_not "creampie"


        group xray_condomcum auto if_all ["xray","condom","creampie"]


        attribute cum null
        group multiple auto variant cum when cum


        group dick_out auto if_not ["vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not ["vaginal","anal","condom"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["vaginal","anal","condom"]


        group condom_out auto if_any "condom" if_not ["vaginal","anal","cumshot"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]

    layeredimage ayesha reversecowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker], npc=ayesha)

        always "ayesha_reversecowgirl_bg"
        always "ayesha_reversecowgirl_body"

        group exp auto:
            attribute normal default

        attribute pregnant

        group multiple auto variant piercings
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_moan when moan
        group multiple auto variant piercings_orgasm when orgasm

        group dick auto:
            attribute out default

        attribute cum null
        group cum auto if_any ["cum"]

        attribute condom if_any ["pussy"]

        attribute facial

    layeredimage ayesha handjob:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, DickPicker], npc=ayesha)


        always "ayesha_handjob_bg"


        always "ayesha_handjob_bodies"
        attribute pregnant
        group multiple auto variant piercings


        group dick auto


        attribute cum null
        group cum auto if_any ["cum"]


        group handpos:
            attribute down null default
            attribute mid null
            attribute up null
        group hj auto variant "down" if_any ["down"]
        group hj auto variant "mid" if_any ["mid"]
        group hj auto variant "up" if_any ["up"]

    layeredimage ayesha blowjob:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, DickPicker], npc=ayesha)


        always "ayesha_blowjob_bg"


        always "ayesha_blowjob_mikemc"
        always "ayesha_blowjob_body"
        attribute pregnant


        attribute lips null
        attribute clit null
        attribute tongue null
        group multiple auto variant piercings


        always "ayesha_blowjob_head_suck" if_any ["out"]
        group head auto:
            attribute out null default


        attribute collar null
        group collar auto if_any ["collar"]


        group eyes auto variant "suck" if_any ["out", "suck"]:
            attribute opened default
        group eyes auto variant "deepthroat" if_any ["deepthroat"]:
            attribute opened default


        group mouth auto


        group multiple auto variant piercings_suck when out or suck
        group multiple auto variant piercings_deepthroat when deepthroat


        always "ayesha_blowjob_mike_hand_suck" if_any ["out"]
        group mike_hand auto


        attribute facecum


        group dick auto variant "out" if_any ["out"]


        attribute cum null
        group cum auto if_any ["cum"]
        group cum auto variant "out" if_all ["cum", "out"]


        always "ayesha_blowjob_fg"

    layeredimage ayesha bdsm:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=ayesha)

        always "ayesha_bdsm_bg"

        always "ayesha_bdsm_ayesha"

        attribute squirt
        attribute sweat

        group exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        attribute collar
        attribute blindfold

        attribute ropes null
        group ropes auto if_any ["ropes"]:
            attribute nopreg default

        group multiple auto variant whipmarks

        attribute wax

        attribute cum null
        group cum auto if_any ["cum"]

        attribute out null
        group dick_out auto if_all ["mike", "out"]
        group dick auto if_any ["anal", "vaginal"] if_all ["mike"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        attribute condom null
        group condom auto if_any ["condom"]

        group condomcum auto if_all ["cum", "condom"]

        attribute creampie null
        group creampie auto if_any ["creampie"]

        attribute finger

        group candle auto:
            attribute availablecandle default

        group vibrator auto:
            attribute availablevibrator default

        group whip auto:
            attribute availablewhip default

        group paddle auto:
            attribute availablepaddle default

        group electrodes auto

        attribute clamps

        group multiple auto variant fx

        attribute mike null
        always "ayesha_bdsm_mike_back" if_all ["mike"] if_not ["anal", "vaginal", "out"]
        always "ayesha_bdsm_mike_front" if_all ["mike"] if_any ["anal", "vaginal", "out"]


    layeredimage ayesha cowgirl:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, PubesPicker, DickPicker], npc=ayesha)
        always "ayesha_cowgirl_bg"

        group bodies auto:
            attribute pose1 default

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute pregnant null
        group pregnant auto if_any "pregnant" if_not "pose1"

        attribute collar null
        group collars auto if_any "collar"

        group exp auto variant "pose1" if_any "pose1":
            attribute normal default
        group exp auto variant "pose2" if_any "pose2"
        group exp auto variant "pose3" if_any "pose3"

        group multiple auto variant piercings_pose1 when pose1
        group multiple auto variant piercings_pose2 when pose2
        group multiple auto variant piercings_pose3 when pose3

        group dick_location:
            attribute out null default
            attribute anal null
            attribute vaginal null

        group dick_out auto if_all "out"

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto variant "vaginal" if_all ["vaginal", "condom"]:
            attribute pose3 null

        group condomcum auto if_all ["cum", "condom"]

        group dick_in auto variant "anal" if_any "anal":
            attribute pose3 null

        group dick_in auto variant "vaginal" if_any "vaginal":
            attribute pose3 null

        attribute creampie null
        group creampie auto variant "anal" if_all ["anal", "creampie"]
        group creampie auto variant "vaginal" if_all ["vaginal", "creampie"]

        group pregnant auto if_all ["pregnant", "pose1"]
        group multiple auto variant piercings_fg_pose1 when pose1

    layeredimage ayesha ending:
        attribute_function Pickers([EndingKidPicker], npc=ayesha)


        always "ayesha_ending_bg"
        always "ayesha_ending_bodies"
        always "ayesha_ending_light"
        always "ayesha_ending_bubble"
        always "ayesha_ending_mike"


        attribute kid

    layeredimage ayesha stand:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, OutfitPicker, MCPicker], npc=ayesha)

        attribute mikemc null

        group mike_position:
            attribute fuck null default
            attribute lick null

        group fuck_position:
            attribute pose1 null default
            attribute pose2 null

        group dick_position:
            attribute outside null default
            attribute vaginal null
            attribute anal null

        group bg auto:
            attribute bedroom default

        always "ayesha_stand_ayesha"
        attribute pregnant

        group multiple auto variant piercings

        group outfit auto if_not "pregnant":
            attribute casual null
        group outfit auto variant "pregnant" if_any "pregnant"

        group exp auto:
            attribute normal default

        group hands auto

        group mike auto if_any "lick"
        group mike auto variant "pose1" if_all ["fuck", "pose1"]
        group mike auto variant "pose2" if_all ["fuck", "pose2"]

        group dick_outside auto if_all ["pose1", "outside"]

        group dick auto variant "outside" if_all ["fuck", "outside"]
        group dick auto variant "pose1" if_all ["fuck", "pose1"] if_not "outside"
        group dick auto variant "pose2" if_all ["fuck", "pose2"] if_not "outside"

        attribute creampie null
        group creampie auto variant "pose1" if_all ["creampie", "pose1"]
        group creampie auto variant "pose2" if_all ["creampie", "pose2"]

        attribute condom null
        group condom auto variant "outside" if_all ["condom", "outside"]
        group condom auto variant "pose1" if_all ["condom", "pose1"]
        group condom auto variant "pose2" if_all ["condom", "pose2"]

        attribute cum null
        group condomcum auto variant "outside" if_all ["cum", "condom", "outside"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot", "condom", "outside"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
