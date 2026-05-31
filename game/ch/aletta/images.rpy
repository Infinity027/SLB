init 1:
    layeredimage aletta:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=aletta)


        attribute idle null


        attribute haircut null
        attribute nohaircut null
        group nohaircut auto if_not ["helmet", "haircut", "halloween"]
        group halloween_haircut auto if_any ["halloween"] if_not ["helmet"]


        group tail auto if_not ["bottomless", "naked"]


        group wings auto if_not ["topless", "naked"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group tattoo auto if_not ["pregnant"]
        group tattoo auto variant "pregnant" if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings


        group watch auto variant "a" if_any ["a"]
        group watch auto variant "b" if_any ["b"]


        attribute naked null

        group stockings auto if_not ["naked", "bottomless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute collar if_any ["sexywork"]



        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        attribute nopatsies null
        group patsies auto if_not ["nopatsies", "topless", "naked"]


        attribute collar if_not ["sexywork"]





        group haircut auto if_any ["haircut"] if_not ["helmet", "halloween"]
        group haircut auto variant "halloween" if_any ["halloween"] if_not ["helmet"]


        group hat auto if_not ["topless", "naked"]


        attribute glasses null
        attribute noglasses null
        group glasses auto if_any "glasses" if_not ["helmet", "noglasses"]


        attribute helmet null
        group helmet auto if_any ["helmet"]


        group book auto variant "a" if_any ["a"]


        attribute leash if_any ["collar"]


        group fx auto


        group arm auto

    layeredimage aletta close:
        yalign 0.04
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=aletta)


        attribute idle null


        attribute haircut null
        attribute nohaircut null
        group nohaircut auto if_not ["helmet", "haircut", "halloween"]
        group halloween_haircut auto if_any ["halloween"] if_not ["helmet"]


        group tail auto if_not ["bottomless", "naked"]


        group wings auto if_not ["topless", "naked"]


        group position auto


        attribute pubes


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group tattoo auto if_not ["pregnant"]
        group tattoo auto variant "pregnant" if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings


        group watch auto variant "a" if_any ["a"]
        group watch auto variant "b" if_any ["b"]


        attribute naked null

        group stockings auto if_not ["naked", "bottomless"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute collar if_any ["sexywork"]



        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        attribute nopatsies null
        group patsies auto if_not ["nopatsies", "topless", "naked"]


        attribute collar if_not ["sexywork"]





        group haircut auto if_any ["haircut"] if_not ["helmet", "halloween"]
        group haircut auto variant "halloween" if_any ["halloween"] if_not ["helmet"]


        group hat auto if_not ["topless", "naked"]


        attribute noglasses null
        attribute glasses null
        group glasses auto if_any "glasses" if_not ["helmet", "noglasses"]


        attribute helmet null
        group helmet auto if_any ["helmet"]


        group book auto variant "a" if_any ["a"]


        attribute leash if_any ["collar"]


        group fx auto


        group arm auto

    layeredimage aletta smartphone:
        always "aletta_smartphone"

    layeredimage aletta oral:


        always "aletta_oral_bg"


        always "aletta_oral_body"


        group exp:
            attribute normal default
            attribute orgasm


        always "aletta_oral_glasses"


        group man:
            attribute noman null
            attribute mana default
            attribute manb


        attribute arm if_any ["mana"]


        group eyes auto variant "mana" if_any ["mana"]:
            attribute open default
            attribute closed
        group eyes auto variant "manb" if_any ["manb"]:
            attribute open default
            attribute closed


        attribute tongue if_any ["mana"]


        attribute cum null
        always "aletta_oral_cum_a" if_all ["cum", "mana"]
        always "aletta_oral_cum_b" if_all ["cum", "manb"]




    layeredimage aletta kiss:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, OutfitPicker], npc=aletta)


        group multiple auto variant acc1 when naked


        always "aletta_kiss"


        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null
            attribute nose null
            attribute tongue null
        group multiple auto variant piercings


        group multiple auto variant glasses


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]


        group necklace auto if_not ["collar"]


        attribute collar


        always "aletta_kiss_collar_letter" if_any ["collar"] if_not ["suit"]


        group outfitmike auto if_not ["naked"]:
            attribute normal default


        group hair auto if_not ["halloween"]
        always "aletta_kiss_hair_halloween" if_any ["halloween"]


        group multiple auto variant acc2 when not naked

    layeredimage aletta titjob:
        attribute_function Pickers([DickPicker, PiercingsPicker, CollarPicker, HaircutPicker, OutfitPicker], npc=aletta)


        group bg auto:
            attribute bedroom default


        always "aletta_titjob_bodies"


        attribute collar


        group outfit auto:
            attribute sexydate null
            attribute date null


        group exp auto:
            attribute normal default


        attribute cum null
        group multiple auto variant cum when cum


        group hair auto


        attribute glasses


        group dick auto


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null

    layeredimage aletta cowgirl:
        attribute_function Pickers([DickPicker, PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker], npc=aletta)


        group bg auto:
            attribute bedroom default


        always "aletta_cowgirl_bodies"


        group mike_outfit_top auto


        group multiple auto variant fx


        attribute chain


        attribute pregnant


        group exp_aletta auto:
            attribute normal default
        group exp_mike auto:
            attribute smile default


        attribute clit null
        attribute ears null
        attribute lips null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings

        attribute naked null

        attribute date null
        attribute sexydate null
        attribute nobra null
        group outfit_top auto if_not ["nobra", "naked"]
        group outfit_top auto variant "nobra" if_any ["nobra"] if_not ["naked"]


        attribute glasses


        group hair auto


        group booty auto:
            attribute raised default


        group outfit_bot auto variant "down" if_any ["down"] if_not ["naked"]
        group outfit_bot auto variant "raised" if_any ["raised"] if_not ["naked"]


        attribute vaginal null
        attribute anal null
        group dick auto variant "vaginal" if_any ["vaginal"]
        group dick auto variant "anal" if_any ["anal"]
        group dick auto variant "out" if_not ["vaginal","anal"]


        attribute condom null
        group condom auto variant "vaginal" if_all ["condom","vaginal"]
        group condom auto variant "out" if_any ["condom"] if_not ["vaginal","anal"]


        attribute creampie null
        group creampie auto variant "vaginal" if_all ["creampie","vaginal"] if_not ["condom"]
        group creampie auto variant "anal" if_all ["creampie","anal"] if_not ["condom"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom","vaginal","anal"]


        group hand auto:
            attribute raised default


        group mike_outfit auto variant "down" if_any ["down"] if_not ["naked"]
        group mike_outfit auto variant "raised" if_any ["raised"] if_not ["naked"]


        group mike_outfit auto


        attribute collar

    layeredimage aletta shooting:
        attribute_function Pickers([PubesPicker], npc=aletta)


        group bg auto:
            attribute range default


        attribute mike


        group expmike auto if_any ["mike"]:
            attribute normal default


        attribute finger null if_not ["mike", "bj"]
        always "aletta_shooting_finger" if_any ["finger"]


        always "aletta_shooting_body" if_not ["mike"]


        attribute pubes if_not ["mike"]


        group outfit auto if_not ["mike"]:
            attribute closed default
            attribute naked null


        group exp auto if_not ["mike"]:
            attribute normal default


        always "aletta_shooting_glasses" if_not ["mike"]


        always "aletta_shooting_arms" if_not ["mike"]


        group outfitarms auto if_not ["mike"]:
            attribute clothed default
            attribute naked null


        attribute fire null
        always "aletta_shooting_fire1" if_any ["fire"] if_not ["mike"]
        always "aletta_shooting_fire2" if_all ["fire", "mike"]


        attribute juice if_not ["mike"]


        always "aletta_shooting_finger_arms" if_any ["finger"]


        always "aletta_shooting_finger_head" if_any ["finger"]


        attribute bj if_any ["mike"] if_not ["finger"]


        group bj auto if_any ["bj"]:
            attribute suck default


        group bj_cumshot auto if_any ["bj"]


        group fg auto

    layeredimage aletta ride:

        attribute nobg null
        attribute noglasses null


        always "aletta_ride_bg" if_not["nobg"]


        always "aletta_ride_bike"


        attribute mike


        always "aletta_ride_body"


        group suit auto:
            attribute closed default


        always "aletta_ride_mike_leg" if_any ["mike"]


        group righthand auto if_any ["mike"]:
            attribute waist default


        group lefthand auto if_any ["mike"]:
            attribute lwaist default


        always "aletta_ride_bike_front"


        group exp auto:
            attribute normal default


        always "aletta_ride_mike_face" if_any ["mike"]


        always "aletta_ride_glasses" if_not ["noglasses"]


        always "aletta_ride_arm"


        always "aletta_ride_helmet"


        always "aletta_ride_blur" if_not ["nobg"]

    layeredimage aletta missionary:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker, MCCGPicker], npc=aletta)

        group multiple auto variant unused_attributes
        group multiple:
            attribute mc_casual null
            attribute mc_date null
            attribute glasses null

        attribute nomc null


        always "aletta_missionary_bg"

        always "aletta_missionary_mc_back_bodyparts" if_not "nomc"

        group aletta_back_bodyparts auto:
            attribute out default

        attribute mikemc if_not "nomc"


        always "aletta_missionary_aletta_body"

        group aletta_front_bodyparts auto:
            attribute anal null


        group exp auto:
            attribute normal default

        attribute collar
        attribute pregnant
        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute lips null

        attribute cum null
        group multiple auto variant cum when cum

        group dick auto variant "vaginal" if_any "vaginal" if_not "nomc"
        group dick auto variant "out" if_any "out" if_not "nomc"

        attribute condom null
        group condom auto variant "vaginal" if_all ["vaginal", "condom"] if_not "nomc"
        group condom auto variant "out" if_all ["out", "condom"] if_not "nomc"

        attribute creampie null
        group creampie auto variant "vaginal" if_all ["vaginal", "creampie"] if_not "nomc"
        group creampie auto variant "anal" if_any ["anal", "creampie"] if_not "nomc"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["nomc", "condom"]

        always "aletta_missionary_mc_front_bodyparts" if_not "nomc"

        group aletta_front_bodyparts auto:
            attribute vaginal null
            attribute out null


        attribute inserts null
        always "aletta_missionary_inserts_bg" if_any "inserts"
        group inserts_aletta auto if_any "inserts"

        always "aletta_missionary_inserts_mikemc" if_any "inserts" if_not "nomc"

        group inserts_dick auto variant "vaginal" if_all ["vaginal", "inserts"] if_not "nomc"
        group inserts_dick auto variant "anal" if_all ["anal", "inserts"] if_not "nomc"
        group inserts_dick auto variant "out" if_all ["out", "inserts"] if_not "nomc"

        group inserts_condom auto if_all ["inserts", "condom"] if_not "nomc"

        group inserts_creampie auto variant "vaginal" if_all ["vaginal", "inserts", "creampie"] if_not "nomc"
        group inserts_creampie auto variant "anal" if_all ["anal", "inserts", "creampie"] if_not "nomc"

        group inserts_cum auto if_all ["inserts", "cum"]

        always "aletta_missionary_inserts_fg" if_any "inserts"

    layeredimage aletta doggy:
        attribute_function Pickers([PubesPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=aletta)


        group bg auto:
            attribute bedroom default


        group backhair auto:
            attribute hairup default


        attribute pregnant null
        group pregnant auto if_any "pregnant":
            attribute naked default


        always:
            "aletta_doggy_aletta"


        attribute pubes


        attribute vaginaldrip


        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute nose null
            attribute tongue null


        group outfit auto


        attribute acc null
        group neck auto variant "collar" if_any "collar"
        group neck auto variant "acc" if_any "acc" if_not "collar"
        attribute leash if_any "collar"


        group exp auto:
            attribute normal default


        attribute plug null
        group plug auto if_any "plug":
            attribute ass default


        attribute cumbody


        attribute glasses null
        group glasses auto if_any "glasses"


        group fronthair auto


        attribute cumface


        attribute mike null
        attribute tron null
        always:
            if_any "mike"
            "aletta_doggy_mike"
        always:
            if_all ["mike", "tron", "halloween"]
            "aletta_doggy_tron_mike"


        group dick auto if_any "mike":
            attribute out default


        attribute condom null
        group condom auto if_all ["mike", "condom"] if_not "condomcum"



        attribute condomcum null
        group condomcum auto if_all ["mike", "condomcum"] if_not "condom"


        attribute squirt if_any "vaginal"


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["out", "condom"]


        attribute dickcum if_all ["mike", "out"]


        attribute cumshot if_all ["mike", "out"]


        attribute hand null
        always:
            if_all ["mike", "hand"]
            "aletta_doggy_mikehand"

    layeredimage aletta rimming:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker], npc=aletta)


        always "aletta_rimming_bg"


        always "aletta_rimming_body"


        attribute pregnant


        group exp auto:
            attribute normal default


        group multiple auto variant piercings


        attribute toys if_not ["finger"]


        attribute hand null
        group hand auto if_any ["hand"]:
            attribute pussy default


        attribute cum null
        group cum auto if_any ["cum"]

    layeredimage aletta vibrator:

        attribute nobg null
        attribute noshiori null
        attribute noglasses null


        always "aletta_vibrator_bg" if_not ["nobg"]


        always "aletta_vibrator_shiori" if_not ["noshiori"]


        always "aletta_vibrator_aletta"


        group exp auto:
            attribute embarrassed default


        group shiori_exp auto:
            attribute shiori_worried default


        group location auto:
            attribute inside default
            attribute novibrator null


        attribute open if_not ["inside"]


        attribute squirt if_not ["inside"]


        attribute on if_any ["inside"]
        attribute blurry if_any ["fall"]


        always "aletta_vibrator_glasses" if_not ["noglasses"]

    layeredimage aletta ropeplay:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker,PubesPicker, OutfitPicker], npc=aletta)


        always "aletta_ropeplay_bg"


        group position auto:
            attribute a default


        group pubes auto variant "a" if_all ["a", "pubes"]
        group pubes auto variant "b" if_all ["b", "pubes"]


        attribute pregnant if_not ["a"]


        group exp auto:
            attribute normal default


        attribute blindfold


        always "aletta_ropeplay_glasses" if_not ["blindfold"]


        attribute gag


        group multiple auto variant nippiercings_a when a and (topless or naked)
        group multiple auto variant nippiercings_b when b and (topless or naked)


        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute chain


        attribute nopanties null
        group panties auto variant "a" if_any ["a"] if_not ["nopanties", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["pregnant", "nopanties", "naked"]
        group panties auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["nopanties", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]

        group stockings auto variant "a" if_any "a" if_not ["bottomless", "naked"]
        group stockings auto variant "b" if_any "b" if_not ["pregnant", "bottomless", "naked"]
        group stockings auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]

        attribute ropes null
        group ropes auto variant "b" if_all ["b", "ropes"] if_not ["pregnant"]
        group ropes auto variant "b_pregnant" if_all ["b", "pregnant", "ropes"]


        attribute collar


        attribute leash if_any ["collar"]


        group multiple auto variant vibrator_a when a and (nopanties or naked)
        group multiple auto variant vibrator_b when b and (nopanties or naked)


        always "aletta_ropeplay_nohaircut" if_not ["haircut"]
        always "aletta_ropeplay_haircut" if_any ["haircut"]


        group multiple auto variant fx
        group multiple auto variant fx_a when a
        group multiple auto variant fx_b when b

    layeredimage aletta ceofuck:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, DickPicker], npc=aletta)

        attribute dwayne null


        always "aletta_ceofuck_bg"


        always "aletta_ceofuck_aletta"


        group exp auto:
            attribute normal default


        attribute glasses null
        attribute noglasses null
        always "aletta_ceofuck_glasses" if_not ["noglasses"]


        group hair auto:
            attribute nohaircut default


        attribute collar


        group mike auto if_not ["dwayne"]


        always "aletta_ceofuck_dwayne" if_any ["dwayne"]

        attribute santa if_any ["dwayne"]


        attribute pregnant


        group multiple auto variant piercings
        group piercings auto variant "default" if_any ["clit"] if_not ["vaginal"]


        group outside auto if_any "outside" if_not ["vaginal", "anal", "dwayne"]
        group vaginal auto if_any "vaginal" if_not ["outside", "anal", "dwayne"]
        group anal auto if_any "anal" if_not ["vaginal", "outside", "dwayne"]


        group dwayne_dick auto if_any ["dwayne"]:
            attribute outside default


        attribute condom null
        group dwayne_condom auto if_all ["condom", "dwayne"]:
            attribute outside default
            attribute anal null


        group piercings auto variant "vaginal_dwayne" if_all ["clit", "vaginal", "dwayne"]
        group piercings auto variant "vaginal_big" if_all ["clit", "vaginal", "big"]
        group piercings auto variant "vaginal_medium" if_all ["clit", "vaginal", "medium"]
        group piercings auto variant "vaginal_small" if_all ["clit", "vaginal", "small"]


        attribute creampie null
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["condom"]
        group creampie auto variant "anal" if_all ["creampie", "anal"]
        group creampie auto variant "outside" if_all ["creampie", "outside"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "pregnant" if_all ["cum", "pregnant"] if_not ["condom"]


        always "aletta_ceofuck_fg"

    layeredimage aletta blowjob:

        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, DickPicker], npc=aletta)


        group bg auto:
            attribute restaurant default


        always "aletta_blowjob_bodies"


        attribute pregnant


        group multiple auto variant piercings


        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute date default
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]:
            attribute date default


        always "aletta_blowjob_pants"


        group dick auto


        group exp auto:
            attribute normal default


        attribute collar


        attribute glasses


        attribute cum


        group fg auto

    layeredimage aletta cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker, DickPicker], npc=aletta)

        attribute noglasses null


        group bg auto:
            attribute restaurant default


        always "aletta_cunnilingus_body"


        attribute pregnant


        group multiple auto variant piercings


        attribute naked null
        group outfit auto if_not ["naked"]:
            attribute date default
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]:
            attribute date default


        always "aletta_cunnilingus_mike"


        always "aletta_cunnilingus_mikeoutfit" if_not ["naked"]


        always "aletta_cunnilingus_arm"


        group armoutfit auto


        group exp auto:
            attribute normal default


        attribute collar


        always "aletta_cunnilingus_glasses" if_not ["noglasses"]


        group fg auto

    layeredimage aletta ending:
        attribute_function Pickers([HaircutPicker], npc=aletta)


        always "aletta_ending_bg"


        group base auto


        group hair auto if_any "aletta"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
