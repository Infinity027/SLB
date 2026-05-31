init 1:
    layeredimage camila:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=camila)


        attribute idle null


        group hairback auto if_not ["halloween"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        group multiple auto variant piercings


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]



        group bot auto variant "a_pregnant" if_all ["a", "pregnant", "halloween"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant", "halloween"] if_not ["bottomless", "naked"]

        group pregnant auto if_all ["pregnant", "halloween", "topless"]

        group multiple auto variant piercings_halloween when halloween



        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked", "halloween"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked", "halloween"]


        attribute collar


        group necklace auto if_not ["collar"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut and not (halloween or sluttydate)
        group nohaircut auto when nohaircut and not (halloween or sluttydate)
        group haircut auto variant sluttydate when sluttydate


        group multiple auto variant piercings_usual when not (date or sexydate or halloween)
        group multiple auto variant piercings_date when date
        group multiple auto variant piercings_sexydate when sexydate


        group helmet auto


        group exp auto if_not ["halloween"]:
            attribute normal default
        group exp auto variant "halloween" if_any ["halloween"]:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings_nothalloween when not halloween


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute nojacket null
        group jacket auto variant "a" if_all ["a"] if_not ["pregnant", "topless", "naked", "nojacket"]
        group jacket auto variant "b" if_all ["b"] if_not ["topless", "naked", "nojacket"]
        group jacket auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked", "nojacket"]


        group acc_hand auto variant "a" if_any ["a"]
        group acc_hand auto variant "b" if_any ["b"]

        group acc auto


        group arm auto

    layeredimage camila close:
        yalign 0.2
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=camila)


        attribute idle null


        group hairback auto if_not ["halloween"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        group multiple auto variant piercings


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]



        group bot auto variant "a_pregnant" if_all ["a", "pregnant", "halloween"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant", "halloween"] if_not ["bottomless", "naked"]

        group pregnant auto if_all ["pregnant", "halloween", "topless"]

        group multiple auto variant piercings_halloween when halloween



        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked", "halloween"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked", "halloween"]


        attribute collar


        group necklace auto if_not ["collar"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"] if_not ["halloween"]
        group nohaircut auto if_any ["nohaircut"] if_not ["halloween"]


        group multiple auto variant piercings_usual when not (date or sexydate or halloween)
        group multiple auto variant piercings_date when date
        group multiple auto variant piercings_sexydate when sexydate


        group helmet auto


        group exp auto if_not ["halloween"]:
            attribute normal default
        group exp auto variant "halloween" if_any ["halloween"]:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings_nothalloween when not halloween


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute nojacket null
        group jacket auto variant "a" if_all ["a"] if_not ["pregnant", "topless", "naked", "nojacket"]
        group jacket auto variant "b" if_all ["b"] if_not ["topless", "naked", "nojacket"]
        group jacket auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked", "nojacket"]


        group acc_hand auto variant "a" if_any ["a"]
        group acc_hand auto variant "b" if_any ["b"]


        group arm auto

    layeredimage camila smartphone:
        always "camila_smartphone"

    layeredimage camila kiss:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker], npc=camila)


        always "camila_kiss_body"


        attribute pregnant


        attribute ears null
        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null
        group multiple auto variant piercings
        group piercings_ears auto if_any ["ears"] if_not ["halloween"]:
            attribute usual default


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]
        group outfit_pregnant auto if_any ["pregnant"] if_not ["naked", "topless"]


        group hair auto if_not ["halloween"]
        group hair auto if_all ["naked", "halloween"]


        attribute mike_naked null
        group mikeoutfit auto if_not ["naked"]:
            attribute normal default
        group mikeoutfit auto if_any ["mike_naked"]:
            attribute mc_casual default

        attribute collar null
        group collars auto when collar and not (naked or halloween)

        group acc auto if_not ["naked"]

    layeredimage camila doggy:
        attribute_function Pickers([DickPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker], npc=camila)

        group bg auto:
            attribute bedroom default

        group multiple auto variant fx2

        always "camila_doggy_body"

        group outfit auto
        group acc_legs auto
        group acc_head auto

        attribute pregnant null
        group pregnant auto if_any ["pregnant"]:
            attribute naked default

        group head auto if_not ["halloween"]
        group fuck auto:
            attribute outside default
            attribute inside null

        attribute condom null
        group condom auto if_any ["condom"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        group exp auto if_not ["halloween"]:
            attribute pleasure default
        group exp auto variant "halloween" if_any ["halloween"]:
            attribute pleasure default

        attribute ears null
        group piercings auto
        group piercings auto variant "nothalloween" if_not ["halloween"]

        attribute collar if_not ["halloween"]

        group multiple auto variant fx

    layeredimage camila handlick kylie:


        always "camila_handlick_kylie_bg"


        always "camila_handlick_kylie_kylie"
        group eyes auto:
            attribute sad default
        group mouth auto if_not ["lick"]:
            attribute cry default
        group mouth_lick if_any ["lick"]:
            attribute down default


        group hand if_any ["camila"]:
            attribute stand
            attribute lick


        attribute cum null
        group cum auto if_all ["camila", "cum"]


        group mouth_lick if_any ["lick"]:
            attribute up


        always "camila_handlick_kylie_bars"


        group hand if_any ["camila"]:
            attribute hold default


        attribute naked null
        group person auto:
            attribute camila default
        always "camila_handlick_kylie_mike_outfit" if_any ["mike"] if_not ["naked"]

    layeredimage camila cowgirl:
        attribute_function Pickers([DickPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker], npc=camila)

        always "camila_cowgirl_bg"

        group multiple auto variant fx2

        always "camila_cowgirl_body"

        attribute pregnant

        group head auto

        attribute pubes

        group fuck auto:
            attribute outside null default
        group outside auto if_any ["outside"]

        attribute condom null
        group condom auto if_all ["condom"] if_not ["outside"]
        group condom_outside auto if_all ["condom", "outside"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["outside", "condom"]
        group cumshot auto variant "outside" if_all ["cumshot", "outside"] if_not ["condom"]

        group exp auto:
            attribute pleasure default

        attribute ears null
        group piercings auto

        attribute collar

        group multiple auto variant fx

    layeredimage camila carsex:
        attribute_function Pickers([DickPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker], npc=camila)


        always "camila_carsex_bg"


        always "camila_carsex_bodies"


        attribute collar


        attribute pubes


        always "camila_carsex_mike_exp"


        group exp auto:
            attribute normal default


        group fuckpos:
            attribute out default null
            attribute vaginal null
            attribute anal null


        group dick auto variant "out" if_any ["out"]


        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]


        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]


        attribute pregnant


        group dick auto


        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute nose null
            attribute tongue null


        attribute haircut
        attribute nohaircut


        attribute bodycum


        always "camila_carsex_light"

    layeredimage camila bj:
        attribute_function DickPicker()


        always "camila_bj_bodies"


        always "camila_bj_lick" if_not ["blow"]
        group eyes auto:
            attribute open default


        group dick:
            attribute out null default
            attribute blow
        group dick auto variant "out" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "out"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
        group cumshot auto variant "out" if_all ["cumshot", "out"]


        always "camila_bj_light"

    layeredimage camila cinema bj:
        attribute_function Pickers([HaircutPicker], npc=camila)

        always "camila_cinema_bj_bg"

        always "camila_cinema_bj_mike"

        group mike_exp auto:
            attribute mikenormal default

        group haircuts auto variant "watch" if_any "watch"
        group haircuts auto variant "blow" if_any "blow"

        group position auto:
            attribute watch default

        group exp auto variant "watch" if_any "watch":
            attribute normal default

        group acc auto variant "blow" if_any "blow"

        group outfits auto variant "watch" if_any "watch":
            attribute date default

        group outfits auto variant "blow" if_any "blow"

        group dick auto

        attribute cum


        always "camila_cinema_bj_fg"


        always "camila_cinema_bj_fx_lights"


    layeredimage camila ending:
        attribute_function Pickers([HaircutPicker, SeasonPicker, EndingKidPicker], npc=camila)


        group season auto


        always "camila_ending_bg"


        always "camila_ending_bodies"


        attribute nohaircut
        attribute haircut


        always "camila_ending_donuts"


        attribute kid

    layeredimage camila hospital:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=camila)


        always "camila_hospital_bg"


        attribute smile


        attribute collar


        attribute pregnancy


        group multiple auto variant piercings

    layeredimage camila stand:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, HaircutPicker, OutfitPicker, MCCGPicker], npc=camila)


        group bg auto:
            attribute bedroom default

        group sex_position:
            attribute lick default null
            attribute fuck null

        group fuck_position:
            attribute pose1 null
            attribute pose2 null
            attribute pose3 null

        group legs auto if_any "fuck"

        always "camila_stand_mike_leftarm"
        attribute mikemc

        attribute naked null
        group mcoutfit auto if_not "naked":
            attribute mc_casual default

        group head auto if_any "lick"
        group exp_lick auto if_any "lick":
            attribute normal default

        attribute cum null
        group cum auto if_any "cum"

        group dick auto

        group dickcum auto if_any "cum" if_not ["fuck", "condom"]

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["fuck", "condom"]

        attribute creampie null
        group creampie auto if_any "creampie" if_not "lick"

        attribute condom null
        group condom auto if_any "condom"

        group body auto if_any "lick"
        group multiple auto variant piercings_lick when lick
        group multiple:
            attribute ears null
            attribute clit null
            attribute lips null
            attribute nose null
            attribute tongue null

        group outfit auto variant "lick" if_any "lick" if_not "naked"
        group haircuts auto variant "lick" if_any "lick"
        group mike_rightarm auto if_any "lick"
        group mcoutfit_arm auto variant "lick" if_any "lick" if_not "naked"

        group head_fuck auto if_any "fuck"
        group exp_fuck auto variant "pose1" if_all ["fuck", "pose1"]
        group exp_fuck auto variant "pose2" if_all ["fuck", "pose2"]
        group exp_fuck auto variant "pose3" if_all ["fuck", "pose3"]

        group body_fuck auto if_any "fuck"
        attribute pregnant null
        group pregnant_fuck auto if_all ["fuck", "pregnant"]

        group multiple auto variant piercings_fuck_pose1 when fuck and pose1
        group multiple auto variant piercings_fuck_pose2 when fuck and pose2
        group multiple auto variant piercings_fuck_pose3 when fuck and pose3

        group outfit_fuck auto variant "pose1" if_all ["fuck", "pose1"] if_not "naked"
        group outfit_fuck auto variant "pose2" if_all ["fuck", "pose2"] if_not "naked"
        group outfit_fuck auto variant "pose3" if_all ["fuck", "pose3"] if_not "naked"

        group haircuts_fuck auto variant "pose1" if_all ["fuck", "pose1"]
        group haircuts_fuck auto variant "pose2" if_all ["fuck", "pose2"]
        group haircuts_fuck auto variant "pose3" if_all ["fuck", "pose3"]

        group mike_rightarm_fuck auto if_any "fuck"
        group mcoutfit_arm_fuck auto variant "pose1" if_all ["fuck", "pose1"] if_not "naked"
        group mcoutfit_arm_fuck auto variant "pose2" if_all ["fuck", "pose2"] if_not "naked"
        group mcoutfit_arm_fuck auto variant "pose3" if_all ["fuck", "pose3"] if_not "naked"

        always "camila_stand_fg"

    layeredimage carpatrol:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, PubesPicker, MCPicker], npc=dwayne)






        always "carpatrol_sit"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
