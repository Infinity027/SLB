init 1:
    layeredimage audrey:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=audrey)
        attribute idle null
        group position auto
        attribute pubes null
        group pregnant auto if_any ["pregnant"]
        group multiple auto variant fx

        group exp auto:
            attribute normal default

        attribute ears null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        group sleeves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeves auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group bot auto variant "a" if_all ["a", "strapon"] if_not ["pregnant"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant", "strapon"] if_not ["bottomless"]
        group bot auto variant "b" if_all ["b", "strapon"] if_not ["pregnant"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant", "strapon"] if_not ["bottomless"]

        attribute collar

        group necklace auto if_not ["collar"]
        group hat auto if_not ["topless", "naked"]
        group glasses auto if_not ["topless", "naked"]
        group arm auto

    layeredimage audrey close:
        yalign 0.2
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=audrey)

        attribute idle null

        group position auto

        attribute pubes null
        group pregnant auto if_any ["pregnant"]
        group multiple auto variant fx
        group exp auto:
            attribute normal default

        attribute ears null
        attribute tongue null

        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["naked", "bottomless"]
        group stockings auto variant "b" if_any ["b"] if_not ["naked", "bottomless"]

        group sleeves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group sleeves auto variant "b" if_any ["b"] if_not ["topless", "naked"]

        attribute topless null

        attribute collar

        group necklace auto if_not ["collar"]
        group hat auto if_not ["topless", "naked"]
        group glasses auto if_not ["topless", "naked"]
        group arm auto

    layeredimage audrey smartphone:
        always "audrey_smartphone"

    layeredimage audrey note:
        always "audrey_note"

    layeredimage audrey ryan flirt:
        attribute_function Pickers([ CollarPicker], npc=audrey)

        always "audrey_ryan_flirt_ryan"
        always "audrey_ryan_flirt_audrey"

        attribute collar

    layeredimage audrey waterslide:
        attribute_function Pickers([ CollarPicker, OutfitPicker], npc=audrey)

        always "audrey_waterslide_bg"
        always "audrey_waterslide_bodies"

        attribute collar

        always "audrey_waterslide_mike_swimsuit" if_not ["naked"]

        group outfit auto if_not ["naked"]

        always "audrey_waterslide_fg"

    layeredimage audrey swing:
        attribute_function Pickers([SeasonPicker,  CollarPicker, OutfitPicker], npc=audrey)

        always "audrey_swing_bg"
        group seasons:
            attribute fall
            attribute winter

        always "audrey_swing_pole"
        group seasons:
            attribute spring
            attribute summer

        attribute mike

        group outfit auto variant "mike" if_any ["mike"] if_not ["naked"]
        group ambient auto

        always "audrey_swing_audrey"

        group outfit auto if_not ["naked"]
        attribute collar

        always "audrey_swing_chain"
        always "audrey_swing_sunlight"

    layeredimage audrey danny:

        always "audrey_danny"
        always "audrey_danny_glasses"
        
    layeredimage audrey eat:
        attribute_function Pickers([ OutfitPicker, DickPicker], npc=audrey)
        attribute alone null

        always "audrey_eat_bg"

        always "audrey_eat_mike"
        group audrey auto if_not ["alone"]:
            attribute eating default

                group multiple:
            attribute ears null
            attribute tongue null

        group outfit auto variant "eating" if_any ["eating"] if_not ["alone"]
        group outfit auto variant "handjob" if_any ["handjob"] if_not ["alone"]

        group exp auto if_not ["alone"]
        group exp auto variant "handjob" if_any ["handjob"] if_not ["alone"]:
            attribute open default

        attribute eating if_not ["alone"]

        group pants auto
        group pants auto variant "dick" if_any ["dick"]
        group pants auto variant "nodick" if_not ["dick"]

        group mikehead:
            attribute normal default
            attribute pleasure
        group mikehead if_any ["handjob"]:
            attribute kissing

        group hand auto variant "nodick" if_not ["dick", "alone"]
        group hand auto variant "dick" if_any ["dick"] if_not ["alone"]

        attribute dick null
        group dick auto if_any ["dick"]

        group finger auto variant "dick" if_any ["dick"] if_not ["alone"]

        attribute speed if_all ["handjob", "dick"] if_not ["alone"]

        group fg auto:
            attribute solid default

    layeredimage audrey desk:
        attribute_function Pickers([PubesPicker, OutfitPicker, DickPicker, RoomPicker], npc=audrey)

        group bg auto:
            attribute personal default

        group head auto:
            attribute normal default
        group eyes variant "normal" if_any ["normal"]:
            attribute open default
            attribute close
        group eyes variant "pulled" if_any ["pulled"]:
            attribute open default
            attribute lookback

        always "audrey_desk_body"
        attribute pubes

        attribute naked null
        group outfit auto if_not ["naked"]

        attribute bodycum
        attribute vaginaldrip
        attribute analdrip
        attribute squirt

        attribute mike null
        group mike auto if_any ["mike"]:
            attribute back default
        group dick_back auto if_all ["back", "mike"]:
            attribute out null default
        group dick_back auto variant "out" if_all ["back", "out", "mike"]
        group dick_forth auto if_all ["forth", "mike"]:
            attribute out null default
        group dick_forth auto variant "out" if_all ["forth", "out", "mike"]

        attribute cum null
        group cum_back auto if_all ["cum", "back", "mike"] if_not ["condom"]
        group cum_back auto variant "out" if_all ["cum", "back", "out", "mike"] if_not ["condom"]
        group cum_forth auto if_all ["cum", "forth", "mike"] if_not ["condom"]
        group cum_forth auto variant "out" if_all ["cum", "forth", "out", "mike"] if_not ["condom"]

        attribute condom null
        group condom_back auto if_all ["condom", "back", "mike"]
        group condom_back auto variant "out" if_all ["condom", "back", "out", "mike"] if_not ["cum"]
        group condom_back auto variant "cum" if_all ["condom", "back", "cum", "out", "mike"]
        group condom_forth auto if_all ["condom", "forth", "mike"]
        group condom_forth auto variant "out" if_all ["condom", "forth", "out", "mike"] if_not ["cum"]
        group condom_forth auto variant "cum" if_all ["condom", "forth", "cum", "out", "mike"]

        attribute mark
        attribute spank

        always "audrey_desk_fg"
        attribute fx

    layeredimage audrey grind:
        attribute_function Pickers([ CollarPicker], npc=audrey)

        always "audrey_grind_bodies"
        attribute collar

        
    layeredimage audrey ending bj:
        attribute_function Pickers([ CollarPicker, DickPicker], npc=audrey)

        always "audrey_ending_bj_bg"

                group eyes auto:
            attribute open default
        group mouth auto:
            attribute smile default
        group dick auto if_not ["blow", "lick"]
        always "audrey_ending_bj_dick_lick" if_any ["lick"]
        attribute cum null
        group cum auto if_any ["cum"]
        attribute inmouth
        attribute collar
        attribute phones

    layeredimage audrey ending fuck:
        attribute_function Pickers([ CollarPicker, PositionPicker], npc=audrey)

        always "audrey_ending_fuck_bg"

        group position auto:
            attribute a default
        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group top auto if_not ["pregnant"]:
            attribute a default
        group top auto variant "pregnant" if_any ["pregnant"]:
            attribute a default
        group stockings auto
        group dick auto
        group vaginal auto if_any ["vaginal"]
        group anal auto if_any ["anal"]
        group collar auto if_any ["collar"]

        attribute cum null
        group multiple auto variant cum when cum
        group acc auto
        attribute phones

    layeredimage audrey photocopy:

        always "audrey_photocopy_bg"

        always "audrey_photocopy_ass"

        attribute naked null
        always "audrey_photocopy_clothed" if_not ["naked"]

        attribute text
        attribute kiss

    layeredimage audrey cinema bj:
        attribute_function Pickers([ CollarPicker, OutfitPicker], npc=audrey)

        always "audrey_cinema_bj_bg"

        always "audrey_cinema_bj_mike"

        group mike_exp auto if_not ["fingering"]:
            attribute mikehappy default

        group audrey auto:
            attribute watching default

        attribute collar null

        group audrey_exp auto if_any ["watching"]:
            attribute audreynormal default

        attribute facecum if_any ["watching"]
        attribute naked null

        group audrey_outfit auto variant "watching" if_any ["watching"] if_not ["pregnant", "naked"]
        group audrey_outfit auto variant "watching_pregnant" if_all ["watching", "pregnant"] if_not ["naked"]
        group audrey_outfit auto variant "blowjob" if_any ["blowjob"] if_not ["pregnant", "naked"]
        group audrey_outfit auto variant "blowjob_pregnant" if_all ["blowjob", "pregnant"] if_not ["naked"]

        attribute cumshot if_any ["blowjob"]
        attribute popcorn if_not ["blowjob"]

        always "audrey_cinema_bj_light"

    layeredimage audrey standing:
        attribute_function Pickers([ CollarPicker, OutfitPicker, PubesPicker, RoomPicker], npc=audrey)

        group bg auto:
            attribute breakroom default

        always "audrey_standing_bodies"

        attribute collar
        attribute pubes

        attribute naked null
        group mike auto if_not ["naked"]

        attribute blush

        group exp auto:
            attribute normal default

                group top auto if_not ["pregnant", "naked"]
        group bot auto if_not "naked"

        attribute hand
        attribute cum

