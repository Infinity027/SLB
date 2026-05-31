init 1:
    layeredimage minami:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=minami)


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


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


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
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c


        attribute collar null
        group collar auto if_any ["collar"] if_not ["swimsuit"]


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]

        attribute norobe null
        group kimono auto variant "a" if_any ["a"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "b" if_any ["b"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "c" if_any ["c"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["norobe", "naked"]
        group kimono auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["norobe", "naked"]
        group kimono auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["norobe", "naked"]


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
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=minami)


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


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


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
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_c when c


        attribute collar null
        group collar auto if_any ["collar"] if_not ["swimsuit"]


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["topless", "naked"]

        attribute norobe null
        group kimono auto variant "a" if_any ["a"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "b" if_any ["b"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "c" if_any ["c"] if_not ["pregnant", "norobe", "naked"]
        group kimono auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["norobe", "naked"]
        group kimono auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["norobe", "naked"]
        group kimono auto variant "c_pregnant" if_all ["c", "pregnant"] if_not ["norobe", "naked"]


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

    layeredimage minami kiss:
        attribute_function Pickers([HandcuffsPicker,PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker], npc=minami)


        group bodies auto


        attribute pregnant


        attribute collar


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "casual", "sexydate", "naked", "topless"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["casual", "sexydate", "naked", "topless"]
        group outfit_nohaircut auto if_all ["nohaircut"] if_any ["casual", "sexydate"] if_not ["pregnant", "naked", "topless"]
        group outfit_nohaircut auto if_all ["nohaircut", "pregnant"] if_any ["casual", "sexydate"] if_not ["naked", "topless"]
        group outfit_haircut auto if_all ["haircut"] if_any ["casual", "sexydate"] if_not ["pregnant", "naked", "topless"]
        group outfit_haircut auto if_all ["haircut", "pregnant"] if_any ["casual", "sexydate"] if_not ["naked", "topless"]


        group mikeoutfit auto if_not ["naked"]:
            attribute normal default


        group hat auto if_not ["naked"]


        attribute handcuffs


        attribute leash if_any ["collar"]

    layeredimage minami spank:
        attribute_function Pickers([PiercingsPicker,OutfitPicker, CollarPicker, PregnancyPicker, HaircutPicker, HandcuffsPicker], npc=minami)


        group bg auto:
            attribute livingroom default


        group mike auto:
            attribute mikecasual default


        always "minami_spank_body"

        attribute pregnant


        group multiple auto variant piercings


        group arms auto:
            attribute nohandcuffs default if_not ["handcuffs"]


        attribute marks


        group exp auto:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings_tongue when tongue


        attribute collar


        attribute leash


        group outfit auto:
            attribute naked null

        group outfit_pregnant auto if_any ["pregnant"]


        group outfit_arms auto if_any ["casual"]:
            attribute nohandcuffs default if_not ["handcuffs"]


        attribute nohaircut
        attribute haircut


        attribute speed if_any ["middle"]


        group arm_mikecasual auto if_not ["mikenaked"]:
            attribute up default


        group arm_mikenaked auto if_any ["mikenaked"]:
            attribute up default

    layeredimage minami cowgirl:
        attribute_function Pickers([HandcuffsPicker,PubesPicker, HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker], npc=minami)


        always "minami_cowgirl_bg"


        always "minami_cowgirl_mike_head_up" if_any ["up"] if_not ["halloween"]


        always "minami_cowgirl_body"


        group head auto


        group exp_haircut auto if_any ["haircut"]:
            attribute awkward default
        group exp_nohaircut auto if_any ["nohaircut"]:
            attribute awkward default


        attribute collar


        attribute down null
        always "minami_cowgirl_mike_down" if_not ["up"]


        attribute up null
        always "minami_cowgirl_mike_up" if_any ["up"] if_not ["halloween"]


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings
        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_down when not up


        group hands auto:
            attribute normal default if_not ["handcuffs"]


        attribute hung if_not ["pregnant"]


        attribute bottomless null
        group outfit_bot auto if_not ["pregnant", "bottomless"]
        group outfit_bot auto variant "pregnant" if_any ["pregnant"] if_not ["bottomless"]


        group multiple auto variant piercings_front


        attribute topless null
        group outfit_top auto if_not ["pregnant", "topless"]
        group outfit_top auto variant "pregnant" if_any ["pregnant"] if_not ["topless"]


        group dick auto:
            attribute outside default


        group multiple auto variant piercings_vaginal when vaginal


        attribute condom null
        group condom auto if_any ["condom"] if_not ["condomcum"]


        attribute condomcum null
        group condomcum auto if_any ["condomcum"] if_not ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute cumshot if_any ["outside"]


        attribute dickcum if_any ["outside"]


        attribute poke if_not ["pregnant"]


        attribute speed

    layeredimage minami doggy:
        attribute_function Pickers([HandcuffsPicker, HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker, OutfitPicker], npc=minami)


        group bg auto:
            attribute bedroom default


        always "minami_doggy_body"


        group outfit auto:
            attribute naked null default


        attribute blush


        group eyes auto:
            attribute normal default


        attribute collar


        group hair auto


        group mouth auto:
            attribute open default


        attribute tongue null
        group piercings_tongue auto if_any ["tongue"]


        attribute mike


        attribute pregnant


        group hidden_piercings auto if_any ["naked"]

        group piercings auto:
            attribute clit null
            attribute ears null


        group right auto if_any ['mike']:
            attribute ass default


        attribute inside null
        group dick auto if_all ['mike'] if_not ['inside']


        attribute cum null
        group cum auto if_all ['mike', 'cum'] if_not ['inside']


        attribute cumshot null
        group cumshot auto if_all ['mike','inside', 'cumshot'] if_not ['inside']


        attribute handcuffs


        attribute bodycum


        attribute cat_tail

    layeredimage minami missionary:
        attribute_function Pickers([HandcuffsPicker,PiercingsPicker, HaircutPicker, PregnancyPicker, CollarPicker], npc=minami)

        always "minami_missionary_bg"
        group bg auto:
            attribute bedroom1 default

        attribute speed
        always "minami_missionary_bodies"

        attribute pregnant

        group eye auto:
            attribute open default

        attribute collar

        group multiple auto variant piercings

        attribute nohaircut
        attribute haircut

        attribute handcuffs
        attribute leash

    layeredimage minami bj:
        attribute_function Pickers([PiercingsPicker,DickPicker,HandcuffsPicker,HaircutPicker], npc=minami)

        group bg auto:
            attribute bedroom1 default

        group bodies auto

        attribute blush

        group eye auto variant "haircut" if_any ["haircut"]:
            attribute open default
        group eye auto variant "nohaircut" if_any ["nohaircut"]:
            attribute open default
        group mouth auto:
            attribute surprised default

        group multiple auto variant piercings

        attribute facial

        attribute out null
        attribute suck null
        group dick_out auto if_any "out" if_not ["suck"]

        always "minami_dick_flacid" if_not ["suck", "out"]

        attribute cum null
        group cum auto if_all ["cum", "out"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot", "out"]

        always "minami_bj_mouthful" if_all ["cumshot", "suck"]

        attribute ambient
        attribute handcuffs
        attribute leash

    layeredimage minami cunnilingus:
        attribute_function Pickers([HandcuffsPicker, PubesPicker, CollarPicker, PregnancyPicker, HaircutPicker, PiercingsPicker], npc=minami)

        always "minami_cunnilingus_bg"

        group body auto

        attribute collar

        group exp auto:
            attribute normal default

        group minami_hands auto:
            attribute closed default
            attribute come if_not ["handcuffs"]

        attribute handcuffs

        group multiple auto variant fx

        group mike_lefthand auto if_any ["mike"]:
            attribute leftleg default
            attribute noleft null

        group mike_righthand auto if_any ["mike"]:
            attribute rightleg default
            attribute noright null

        group dildo auto

        attribute vibrate null
        attribute dildowet null
        group multiple auto variant fx when vibrate
        group multiple auto variant fx_dildowet when dildowet and dildopussy

        attribute mike null
        group mike auto if_any ["mike"]:
            attribute nohead null
            attribute lickpussy default

        attribute pubes

        attribute pregnant

        group multiple auto variant piercings

    layeredimage minami ending:
        attribute_function Pickers([CollarPicker, PregnancyPicker, HaircutPicker, EndingKidPicker], npc=minami)

        attribute pregnant null

        always "minami_ending_bg"

        attribute collar

        attribute haircut
        attribute nohaircut

        attribute kid

    layeredimage minami showersex:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, DickPicker], npc=minami)

        always "minami_showersex_bg"
        always "minami_showersex_bodies"

        attribute pregnant

        group multiple auto variant piercings

        group exp auto:
            attribute normal default

        attribute haircut
        attribute nohaircut

        attribute collar

        attribute outside null
        attribute vaginal null
        attribute anal null
        group outside auto if_any "outside" if_not ["vaginal", "anal"]
        group vaginal auto if_any "vaginal" if_not ["outside", "anal"]
        group anal auto if_any "anal" if_not ["vaginal", "outside"]

        attribute creampie null
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"]
        group creampie auto variant "anal" if_all ["creampie","anal"]
        group creampie auto variant "outside" if_all ["creampie","outside"]

    layeredimage minami stuck :
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker], append_npc_from_attributes=True)

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

        group multiple auto variant minamipiercings when naked
        group multiple auto variant piercings

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

        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_tryhard when tryhard

        always "minami_stuck_mikeexp_mikenormal" if_any ["mike"]

        always "minami_stuck_mike_botup" if_all ["mike", "up"]

        always "minami_stuck_fg"

        group top auto variant "pregnant" if_any ["minami_pregnant"]

        group arms auto if_not ["minami_casual"]
        group arms_outfit auto variant "lay" if_any ["lay"]
        group arms_outfit auto variant "pull" if_any ["pull"]

        attribute panel

    layeredimage minami mast:
        attribute_function Pickers([PiercingsPicker, HaircutPicker], npc=minami)

        group bg auto:
            attribute bedroom5 default

        always "minami_mast_body"

        group multiple auto variant piercings
        group haircuts auto

        attribute hand null
        attribute toy null

        group hand auto if_not "toy":
            attribute vaginal default

        group toy auto if_any "toy"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
