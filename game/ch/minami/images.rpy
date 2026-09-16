init 1:
    layeredimage minami:
        attribute_function Pickers([PositionPicker,  CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=minami)

        attribute idle null

        group tail_haircut auto variant "a" if_all ["a", "haircut"] if_not ["bottomless", "naked"]
        group tail_haircut auto variant "b" if_all ["b", "haircut"] if_not ["bottomless", "naked"]
        group tail_haircut auto variant "c" if_all ["c", "haircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "a" if_all ["a", "nohaircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "b" if_all ["b", "nohaircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "c" if_all ["c", "nohaircut"] if_not ["bottomless", "naked"]

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        attribute ears null
        attribute collar null
        group collar auto if_any ["collar"] if_not ["swimsuit"]

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null

        attribute topless null

        attribute norobe null

        group collar auto if_all ["collar","swimsuit"]

        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group hat auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group hat_haircut auto variant "a" if_all ["a", "rpg", "haircut"]
        group hat_haircut auto variant "b" if_all ["b", "rpg", "haircut"]
        group hat_haircut auto variant "c" if_all ["c", "rpg", "haircut"]
        group hat_nohaircut auto variant "a" if_all ["a", "rpg", "nohaircut"]
        group hat_nohaircut auto variant "b" if_all ["b", "rpg", "nohaircut"]
        group hat_nohaircut auto variant "c" if_all ["c", "rpg", "nohaircut"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage minami close:
        yalign 0.2
        attribute_function Pickers([PositionPicker,  CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=minami)

        attribute idle null

        group tail_haircut auto variant "a" if_all ["a", "haircut"] if_not ["bottomless", "naked"]
        group tail_haircut auto variant "b" if_all ["b", "haircut"] if_not ["bottomless", "naked"]
        group tail_haircut auto variant "c" if_all ["c", "haircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "a" if_all ["a", "nohaircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "b" if_all ["b", "nohaircut"] if_not ["bottomless", "naked"]
        group tail_nohaircut auto variant "c" if_all ["c", "nohaircut"] if_not ["bottomless", "naked"]

        group position auto

        attribute pubes null
        group pubes auto if_any ["pubes"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default

        attribute ears null

        attribute collar null
        group collar auto if_any ["collar"] if_not ["swimsuit"]

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null

        attribute topless null

        attribute norobe null

        group collar auto if_all ["collar","swimsuit"]

        group hat auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group hat auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group hat auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        group hat_haircut auto variant "a" if_all ["a", "rpg", "haircut"]
        group hat_haircut auto variant "b" if_all ["b", "rpg", "haircut"]
        group hat_haircut auto variant "c" if_all ["c", "rpg", "haircut"]
        group hat_nohaircut auto variant "a" if_all ["a", "rpg", "nohaircut"]
        group hat_nohaircut auto variant "b" if_all ["b", "rpg", "nohaircut"]
        group hat_nohaircut auto variant "c" if_all ["c", "rpg", "nohaircut"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "c" if_any ["c"]

    layeredimage minami smartphone:
        always "minami_smartphone"

    layeredimage minami ending:
        attribute_function Pickers([CollarPicker, HaircutPicker, EndingKidPicker], npc=minami)

        attribute pregnant null

        always "minami_ending_bg"

        attribute collar

        attribute haircut
        attribute nohaircut

        attribute kid

    layeredimage minami stuck :
        attribute_function MultiPickers([CollarPicker,  HaircutPicker], append_npc_from_attributes=True)

        attribute minami default
        attribute mike

        group dress_position:
            attribute up null
            attribute down null default

        group arms_position:
            attribute pull null
            attribute lay null default

        group mikeoutfits:
            attribute mikenaked
            attribute mikecasual default

        always "minami_stuck_bg"

        group leg auto if_any ["mike"]

        group multiple auto variant body
        group multiple auto variant pregnancy

        always "minami_stuck_catflap"

        group multiple auto variant collars

        group top auto:
            attribute naked null
            attribute minami_casual default

        group bot auto variant "up" if_any ["up"]:
            attribute naked null

        group bot auto variant "down" if_any ["down"]:
            attribute naked null

        group bot_pregnant auto variant "up" if_all ["up", "minami_pregnant"]:
            attribute naked null
        group bot_pregnant auto variant "down" if_all ["down", "minami_pregnant"]:
            attribute naked null

        group outfit auto if_any ["bree"]:
            attribute bree_casual default
            attribute nakedbree null
        group outfit_pregnant auto if_any ["bree_pregnant"]:
            attribute nakedbree null

        always "minami_stuck_bodymike" if_any ["mike"]

        group mikeoutfit auto if_any ["mike"]:
            attribute nakedmike null

        group hairs auto

        group minamiexp auto:
            attribute minamitryhard default
        group breeexp auto if_any ["bree"]:
            attribute breesurprised default

        always "minami_stuck_mikeexp_mikenormal" if_any ["mike"]

        always "minami_stuck_mike_botup" if_all ["mike", "up"]

        always "minami_stuck_fg"

        group top auto variant "pregnant" if_any ["minami_pregnant"]

        group arms auto if_not ["minami_casual"]
        group arms_outfit auto variant "lay" if_any ["lay"]
        group arms_outfit auto variant "pull" if_any ["pull"]

        attribute panel

    layeredimage minami mast:
        attribute_function Pickers([ HaircutPicker], npc=minami)

        group bg auto:
            attribute bedroom5 default

        always "minami_mast_body"

        group haircuts auto

        attribute hand null
        attribute toy null

        group hand auto if_not "toy":
            attribute vaginal default

        group toy auto if_any "toy"