init 1:
    layeredimage audrey:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=audrey)


        attribute idle null


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group multiple auto variant fx


        group exp auto:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


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
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)



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
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=audrey)


        attribute idle null


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group multiple auto variant fx


        group exp auto:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


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
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)


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
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker], npc=audrey)

        always "audrey_ryan_flirt_ryan"
        always "audrey_ryan_flirt_audrey"

        attribute pregnant

        attribute collar

        group multiple auto variant piercings

    layeredimage audrey waterslide:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker], npc=audrey)


        always "audrey_waterslide_bg"


        always "audrey_waterslide_bodies"


        attribute collar


        group multiple auto variant piercings


        attribute pregnant


        always "audrey_waterslide_mike_swimsuit" if_not ["naked"]


        group outfit auto if_not ["naked"]


        always "audrey_waterslide_fg"

    layeredimage audrey swing:
        attribute_function Pickers([SeasonPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker], npc=audrey)


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


        attribute pregnant


        attribute collar


        group multiple auto variant piercings


        always "audrey_swing_chain"


        always "audrey_swing_sunlight"

    layeredimage audrey bj:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, DickPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute bedroom1 default


        always "audrey_bj_bodies"


        attribute pregnant


        attribute collar


        attribute navel null
        attribute tongue null
        attribute clit null
        group multiple auto variant piercings


        group fuck:
            attribute out default null
            attribute blowjob null
        group dick auto
        group dick auto variant "out" if_any ["out"]


        attribute dickcum null
        group dickcum auto if_all ["out", "dickcum"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
        group cumshot auto variant "out" if_all ["out", "cumshot"]


        group exp auto:
            attribute normal default


        always "audrey_bj_light"

    layeredimage audrey spoon:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker], npc=audrey)


        always "audrey_spoon_bg"


        always "audrey_spoon_bodies"


        attribute pubes


        attribute pregnant


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        group outfit auto if_not ["pregnant"]
        group outfit auto variant "pregnant" if_any ["pregnant"]


        group hand auto
        group hand auto variant "halloween" if_any ["halloween"]


        attribute cumbody null
        group cumbody auto if_any ["cumbody"]:
            attribute nohand default


        attribute cumshot


        group dick auto:
            attribute limp default


        attribute condom null
        group condom auto if_any ["condom"] if_not ["condomcum"]


        attribute condomcum null
        group condomcum auto if_any ["condomcum"] if_not ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"]


        attribute leftover1
        attribute leftover2


        attribute xray if_any ["vaginal"]
        attribute xraycream if_all ["xray", "vaginal"]


        always "audrey_spoon_light"

    layeredimage audrey danny:
        attribute_function Pickers([PiercingsPicker], npc=audrey)

        always "audrey_danny"
        always "audrey_danny_glasses"
        group multiple auto variant piercings

    layeredimage audrey eat:
        attribute_function Pickers([PiercingsPicker, OutfitPicker, DickPicker], npc=audrey)

        attribute alone null


        always "audrey_eat_bg"


        always "audrey_eat_mike"
        group audrey auto if_not ["alone"]:
            attribute eating default


        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute tongue null
        group multiple auto variant piercings_eating when eating and not alone
        group multiple auto variant piercings_handjob when handjob and not alone


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
        attribute_function Pickers([PregnancyPicker, PubesPicker, OutfitPicker, DickPicker, RoomPicker], npc=audrey)


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
        attribute pregnant
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

    layeredimage audrey kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker], npc=audrey)


        always "audrey_kiss"


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]


        attribute collar


        group outfitmike auto if_not ["naked", "underwear", "swimsuit", "sexyswimsuit"]:
            attribute normal default


        group multiple auto variant acc when not naked

    layeredimage audrey grind:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker], npc=audrey)


        always "audrey_grind_bodies"


        attribute pregnant


        attribute collar


        group multiple auto variant piercings

    layeredimage audrey missionary:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, CollarPicker, DickPicker, RoomPicker], npc=audrey)

        attribute bodycum null
        attribute dickcum null
        attribute cum null
        attribute nomike null
        attribute tongue null
        attribute condom null
        attribute naked null
        attribute santa null
        attribute fx null

        group bg auto:
            attribute bedroom default

        always "audrey_missionary_audrey"

        attribute pubes

        group bot auto if_not ["naked"]

        group multiple auto variant piercings_down

        group exp auto:
            attribute normal default

        attribute collar

        group multiple auto variant piercings

        always "audrey_missionary_mike" if_not ["nomike", "dwayne"]
        attribute dwayne

        group top auto if_not ["topless", "naked"]

        group stockings auto if_not ["naked"]

        group bodycum auto if_any ["bodycum"]:
            attribute naked default
            attribute sexywork

        attribute creampie


        group dick auto if_not ["dwayne"]


        group dwayne_dick auto if_any ["dwayne"]

        group condom auto if_any ["condom"] if_not["dwayne"]

        group dwayne_condom auto if_all ["condom", "dwayne"]

        group creampie auto if_not ["condom"]:
            attribute vaginal if_all ["cum", "vaginal"]
            attribute anal if_all ["cum", "anal"]

        attribute pregnant

        attribute humping

        group top auto variant "pregnant" if_any ["pregnant"] if_not ["topless", "naked"]


        group outside_dick auto if_not ["anal", "vaginal", "nomike", "dwayne"]


        always "audrey_missionary_outside_dick_dwayne" if_any ["dwayne"] if_not ["anal", "vaginal"]

        group outside_condom auto if_not ["anal", "vaginal", "nomike", "cumshot", "dwayne"] if_any ["condom"]
        always "audrey_missionary_outside_condom_dwayne" if_all ["dwayne", "condom"] if_not ["anal", "vaginal"]

        group cumshot auto if_any ["cum"] if_not ["anal", "vaginal", "condom", "dwayne"]
        always "audrey_missionary_cumshot_dwayne" if_all ["dwayne", "cum"] if_not ["anal", "vaginal", "condom"]

        group dickcum auto if_any ["dickcum"] if_not ["condom", "dwayne", "anal", "vaginal"]
        always "audrey_missionary_dickcum_dwayne" if_all ["dwayne", "dickcum"] if_not ["condom", "anal", "vaginal"]

        group condomcum auto if_all ["condom", "cum"] if_not ["dwayne", "anal", "vaginal"]
        always "audrey_missionary_condomcum_dwayne" if_all ["dwayne", "condom", "cum"] if_not ["anal", "vaginal"]


        always "audrey_missionary_topmike_santa" if_any ["santa"] if_not ["nomike", "dwayne"]
        always "audrey_missionary_topdwayne_santa" if_all ["dwayne", "santa"]


        always "audrey_missionary_fx_slap" if_all ["slap", "fx"] if_not ["dwayne"]
        always "audrey_missionary_dwayne_fx_slap" if_all ["dwayne", "slap", "fx"]


        group arms auto if_not ["nomike", "dwayne"]:
            attribute hold default
        group arms auto variant "santa" if_any ["santa"] if_not ["nomike", "dwayne"]:
            attribute hold default


        group dwayne_arms auto if_any ["dwayne"]:
            attribute hold default
        group dwayne_arms auto variant "santa" if_all ["dwayne", "santa"]:
            attribute hold default


        always "audrey_missionary_fg_ceo_light" if_any ["ceo"]

    layeredimage audrey doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, OutfitPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute personal default


        always "audrey_doggy_body"


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        group bot auto
        group top auto


        group mikedick:
            attribute outside null default
            attribute inside null
        group outside auto if_any ["outside"]


        attribute condom null
        group condom auto if_all ["condom", "outside"] if_not ["cum"]
        group condom auto variant "cum" if_all ["condom", "outside", "cum"]


        attribute cum null
        group cum auto if_all ["cum", "outside"] if_not ["condom"]
        attribute bodycum


        attribute collar

    layeredimage audrey cowgirl:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, OutfitPicker, PregnancyPicker, PubesPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute personal default

        always "audrey_cowgirl_bodies"


        attribute pregnant


        group exp auto:
            attribute normal default


        group multiple auto variant piercings



        group outfit auto when not pregnant
        group outfit auto variant pregnant when pregnant

        group dicks auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dicks auto variant vaginal when vaginal
        group dicks auto variant anal when anal

        attribute condom null
        group condom auto variant vaginal when condom and vaginal

        attribute pubes

        group dicks auto variant out when out
        group condom auto variant out when condom and out


        attribute collar


        attribute onbody


        attribute cumshot null
        group cumshot auto when cumshot and not condom
        group condomcum auto when cumshot and condom


        attribute creampie null
        group creampie auto when creampie and not condom

        attribute dickcum null
        group dickcum auto when dickcum


        group fx auto
        group fx auto variant sexywork when sexywork

    layeredimage audrey reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, OutfitPicker, DickPicker, PregnancyPicker, DayNightPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute bedroom default
            attribute livingroom null
        group bg auto variant "livingroom" if_any ["livingroom"]


        always "audrey_reverse_cowgirl_bodies"


        group multiple auto variant piercings


        attribute naked null
        always "audrey_reverse_cowgirl_mike_outfit" if_not ["naked"]


        attribute pubes


        group mike_exp auto:
            attribute mikenormal default


        group audrey_exp auto:
            attribute audreypleasure default


        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null
            attribute exhausted null


        group dick auto variant "out" if_any ["out"]
        group dick auto


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["cumshot", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cumshot"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cumshot"]
        group condomcum auto if_all ["condom", "cumshot", "out"]


        attribute vaginaldrip


        group audrey_outfit auto variant "bot" if_not ["naked"]


        attribute pregnant


        group multiple auto variant piercings_preg


        group audrey_outfit auto variant "top" if_not ["naked"]


        attribute sunglass


        always "audrey_reverse_cowgirl_light" if_any ["cinema"]

    layeredimage audrey ending bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, PregnancyPicker], npc=audrey)


        always "audrey_ending_bj_bg"


        attribute pregnant


        group multiple auto variant piercings


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
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PositionPicker], npc=audrey)


        always "audrey_ending_fuck_bg"


        group position auto:
            attribute a default


        group pregnant auto if_any ["pregnant"]


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


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

    layeredimage audrey cunnilingus:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, DickPicker, PubesPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute bedroom default


        always "audrey_cunnilingus_bodies"


        attribute pubes


        attribute pregnant


        group exp auto:
            attribute normal default


        group multiple auto variant piercings
        always "audrey_cunnilingus_piercing_tongue" if_all ["tongue"] if_any ["ahegao", "pleasure", "gasp"]


        group outfit auto if_not ["pregnant"]
        group outfit auto variant "preg" if_any ["pregnant"]


        group dick auto


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
        attribute cumonhand null
        group cumonhand auto if_any ["cumonhand"]


        attribute collar


        attribute office
        attribute shake
        attribute squirt

    layeredimage audrey photocopy:


        always "audrey_photocopy_bg"


        always "audrey_photocopy_ass"


        attribute naked null
        always "audrey_photocopy_clothed" if_not ["naked"]


        attribute text
        attribute kiss

    layeredimage audrey cinema bj:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker], npc=audrey)


        always "audrey_cinema_bj_bg"


        always "audrey_cinema_bj_mike"


        group mike_exp auto if_not ["fingering"]:
            attribute mikehappy default


        group audrey auto:
            attribute watching default


        attribute collar null
        group collar auto if_any ["collar"]


        attribute pregnant null
        group pregnant auto if_all ["pregnant"]


        group audrey_exp auto if_any ["watching"]:
            attribute audreynormal default


        group multiple auto variant piercings_watching when watching
        group multiple auto variant piercings_blowjob when blowjob


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
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, OutfitPicker, PubesPicker, RoomPicker], npc=audrey)


        group bg auto:
            attribute breakroom default


        always "audrey_standing_bodies"


        attribute collar


        attribute pubes


        attribute pregnant


        attribute naked null
        group mike auto if_not ["naked"]


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        group top auto if_not ["pregnant", "naked"]
        group top auto variant "pregnant" if_any "pregnant" if_not "naked"
        group bot auto if_not "naked"


        attribute hand


        attribute cum
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
