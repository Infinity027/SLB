init 1:
    layeredimage camila:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=camila)

        attribute idle null

        group hairback auto if_not ["halloween"]

        group position auto

        attribute pubes

        attribute naked null

        attribute topless null

        attribute bottomless null

        attribute collar

        group necklace auto if_not ["collar"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut and not (halloween or sluttydate)
        group nohaircut auto when nohaircut and not (halloween or sluttydate)
        group haircut auto variant sluttydate when sluttydate

        group helmet auto

        group exp auto if_not ["halloween"]:
            attribute normal default
        group exp auto variant "halloween" if_any ["halloween"]:
            attribute normal default

        attribute lips null
        attribute tongue null

        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute nojacket null
        group jacket auto variant "b" if_all ["b"] if_not ["topless", "naked", "nojacket"]

        group acc_hand auto variant "a" if_any ["a"]
        group acc_hand auto variant "b" if_any ["b"]

        group acc auto

        group arm auto

    layeredimage camila close:
        yalign 0.2
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker, HaircutPicker], npc=camila)

        attribute idle null

        group hairback auto if_not ["halloween"]

        group position auto

        attribute pubes

        attribute naked null

        attribute topless null

        attribute bottomless null

        attribute collar

        group necklace auto if_not ["collar"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"] if_not ["halloween"]
        group nohaircut auto if_any ["nohaircut"] if_not ["halloween"]

        group helmet auto

        group exp auto if_not ["halloween"]:
            attribute normal default
        group exp auto variant "halloween" if_any ["halloween"]:
            attribute normal default

        attribute lips null
        attribute tongue null
        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        attribute nojacket null
        group jacket auto variant "b" if_all ["b"] if_not ["topless", "naked", "nojacket"]

        group acc_hand auto variant "a" if_any ["a"]
        group acc_hand auto variant "b" if_any ["b"]

        group arm auto

    layeredimage camila smartphone:
        always "camila_smartphone"

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
        attribute_function Pickers([ CollarPicker], npc=camila)

        always "camila_hospital_bg"

        attribute smile

        attribute collar

    layeredimage camila stand:
        attribute_function Pickers([ HaircutPicker, OutfitPicker, MCCGPicker], npc=camila)

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

        group outfit auto variant "lick" if_any "lick" if_not "naked"
        group haircuts auto variant "lick" if_any "lick"
        group mike_rightarm auto if_any "lick"
        group mcoutfit_arm auto variant "lick" if_any "lick" if_not "naked"

        group head_fuck auto if_any "fuck"
        group exp_fuck auto variant "pose1" if_all ["fuck", "pose1"]
        group exp_fuck auto variant "pose2" if_all ["fuck", "pose2"]
        group exp_fuck auto variant "pose3" if_all ["fuck", "pose3"]

        group body_fuck auto if_any "fuck"

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
        attribute_function Pickers([OutfitPicker,  PubesPicker, MCPicker], npc=dwayne)

        always "carpatrol_sit"
